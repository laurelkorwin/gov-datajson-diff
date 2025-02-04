# Change History for nasa.json (Part 143)

### Changes from 31606f9 to dd2190f (Part 132/162)
**Author:** Automated

**Date:** 2025-02-01 15:02:16+00:00

**Message:** Updated data: Sat Feb  1 15:02:16 UTC 2025

```diff
-                    "description": "Earthdata Search for GloSSAC_2.2 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for GloSSAC_2.2 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2284299943-LARC_ASDC",
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
-                    "downloadURL": "https://doi.org/10.5067/GLOSSAC-L3-V2.2",
-                    "description": "DOI data set landing page for GloSSAC_2.2",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for GloSSAC_2.2",
+                    "downloadURL": "https://doi.org/10.5067/GLOSSAC-L3-V2.2",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://creativecommons.org/licenses/by/4.0/",
-                    "description": "Creative Commons License CC BY 4.0",
                     "@type": "dcat:Distribution",
+                    "description": "Creative Commons License CC BY 4.0",
+                    "downloadURL": "https://creativecommons.org/licenses/by/4.0/",
+                    "mediaType": "text/html",
                     "title": "View this dataset's data citation policy"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/GloSSAC/GloSSAC_2.2/",
-                    "description": "ASDC Direct Data Download for GloSSAC_2.2",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for GloSSAC_2.2",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/GloSSAC/GloSSAC_2.2/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/GloSSAC/GloSSAC_2.2/contents.html",
-                    "description": "OPeNDAP data access for GloSSAC_2.2",
                     "@type": "dcat:Distribution",
+                    "description": "OPeNDAP data access for GloSSAC_2.2",
+                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/GloSSAC/GloSSAC_2.2/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 }
             ],
+            "identifier": "C2284299943-LARC_ASDC",
+            "issued": "2022-03-31",
+            "keyword": [
+                "aerosols",
+                "atmosphere",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/GLOSSAC-L3-V2.2",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2022-03-31",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/LARC/SD/ASDC"
+            },
             "spatial": "<?xml version=\"1.0\" encoding=\"UTF-8\"?><gml:Polygon xmlns:gml=\"http://www.opengis.net/gml/3.2\" srsName=\"EPSG:9825\"><gml:outerBoundaryIs><gml:LinearRing><gml:posList>-80.0 -180.0 -80.0 180.0 80.0 180.0 80.0 -180.0 -80.0 -180.0</gml:posList></gml:LinearRing></gml:outerBoundaryIs><gml:innerBoundaryIs></gml:innerBoundaryIs></gml:Polygon>",
+            "temporal": "1979-01-01T00:00:00Z/2021-12-31T23:59:59.999Z",
             "theme": [
                 "GloSSAC",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Global Space-based Stratospheric Aerosol Climatology Version 2.2"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-J-LEISA-3-JUPITER-V1.0",
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
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-j-leisa-3-jupiter-v1.0_sz6i-be49",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "ganymede",
                 "j rings",
@@ -1387202,794 +1387204,771 @@
                 "jupiter",
                 "new horizons"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-J-LEISA-3-JUPITER-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-j-leisa-3-jupiter-v1.0_sz6i-be49",
-            "description": "This data set contains Calibrated data taken by the New Horizons Linear Etalon Imaging Spectral Array instrument during the Jupiter encounter mission phase.",
-            "title": "NEW HORIZONS LEISA JUPITER ENCOUNTER V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "NEW HORIZONS LEISA JUPITER ENCOUNTER V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://c3.nasa.gov/dashlink/resources/764/",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2013-06-19",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
-            "keyword": [
-                "ames",
-                "dashlink",
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
-            "identifier": "DASHLINK_764",
             "description": "Electro-mechanical actuators (EMA) are finding increasing use in aerospace applications, especially with the trend towards all all-electric aircraft and spacecraft designs. However, electro-mechanical actuators still lack the knowledge base accumulated for other fielded actuator types, particularly with regard to fault detection and characterization. This paper presents a thorough analysis of some of the critical failure modes documented for EMAs and describes experiments conducted on detecting and isolating a subset of them. The list of failures has been prepared through an extensive Failure Modes and Criticality Analysis (FMECA) reference, literature review, and accessible industry experience. Methods for data acquisition and validation of algorithms on EMA test stands are described. A variety of condition indicators were developed that enabled detection, identification, and isolation among the various fault modes. A diagnostic algorithm based on an artificial neural network is shown to operate successfully using these condition indicators and furthermore, robustness of these diagnostic routines to sensor faults is demonstrated by showing their ability to distinguish between them and component failures. The paper concludes with a roadmap leading from this effort towards developing successful prognostic algorithms for electromechanical actuators.",
-            "title": "A Diagnostic Approach for Electro-Mechanical Actuators in Aerospace Systems",
-            "programCode": [
-                "026:029"
-            ],
             "distribution": [
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/publication/2009_IEEEAerospace_EMADiagnostics.pdf",
-                    "description": "2009_IEEEAerospace_EMADiagnostics.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "2009_IEEEAerospace_EMADiagnostics.pdf",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/publication/2009_IEEEAerospace_EMADiagnostics.pdf",
+                    "mediaType": "application/pdf",
                     "title": "2009_IEEEAerospace_EMADiagnostics.pdf"
                 }
             ],
-            "accrualPeriodicity": "irregular"
+            "identifier": "DASHLINK_764",
+            "issued": "2013-06-19",
+            "keyword": [
+                "ames",
+                "dashlink",
+                "nasa"
+            ],
+            "landingPage": "https://c3.nasa.gov/dashlink/resources/764/",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:029"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Dashlink"
+            },
+            "title": "A Diagnostic Approach for Electro-Mechanical Actuators in Aerospace Systems"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-X-OSINAC-3-CVP1-CHECKOUT-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This CODMAC level 3 data set contains radiometric calibrated image data in W/m^2/sr/nm,  acquired by the OSIRIS Narrow Angle Camera on the Rosetta spacecraft  during the COMMISSIONING 1 mission phase, covering the period  from 2004-03-05T00:00:00.000 to 2004-06-06T23:59:59.000. The prime objective was commissioning / calibration. Several targets of opportunity were observed, but none of them is identifiable as prime target. After the October 2018 PSA/PDS external peer review, the COMMISSIONING  data set was reprocessed and split into multiple data sets.  This  version V1.0 is one part and supersedes the previous delivery.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-x-osinac-3-cvp1-checkout-v1.0",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2021-05-21",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "international rosetta mission",
                 "c/linear (2002 t7)",
                 "eps aqr"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-X-OSINAC-3-CVP1-CHECKOUT-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-x-osinac-3-cvp1-checkout-v1.0",
-            "description": "This CODMAC level 3 data set contains radiometric calibrated image data in W/m^2/sr/nm,  acquired by the OSIRIS Narrow Angle Camera on the Rosetta spacecraft  during the COMMISSIONING 1 mission phase, covering the period  from 2004-03-05T00:00:00.000 to 2004-06-06T23:59:59.000. The prime objective was commissioning / calibration. Several targets of opportunity were observed, but none of them is identifiable as prime target. After the October 2018 PSA/PDS external peer review, the COMMISSIONING  data set was reprocessed and split into multiple data sets.  This  version V1.0 is one part and supersedes the previous delivery.",
-            "title": "ROSETTA-ORBITER CHECKOUT OSINAC 3 CVP1 RDR V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER CHECKOUT OSINAC 3 CVP1 RDR V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-I0065-3-TD10PHOT-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "The outer solar system object (29981) 1999 TD10 was observed in the R band in September 2001, and in B, V, R, and I in October 2002. We derive B- V=0.80+/-0.05mag, V-R=0.48+/-0.05mag, and R-I=0.44+/-0.05mag. Combining our data with the data from Rousselot et. al. 2003, we derive a synodic period of 15.382+/-0.001hr in agreement with the period from Rousselot et. al. 2003. Our observations show no evidence of a coma.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-i0065-3-td10phot-v1.0_sz94-d8wj",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "support archives",
                 "asteroid 29981",
                 "calibration"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-I0065-3-TD10PHOT-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-i0065-3-td10phot-v1.0_sz94-d8wj",
-            "description": "The outer solar system object (29981) 1999 TD10 was observed in the R band in September 2001, and in B, V, R, and I in October 2002. We derive B- V=0.80+/-0.05mag, V-R=0.48+/-0.05mag, and R-I=0.44+/-0.05mag. Combining our data with the data from Rousselot et. al. 2003, we derive a synodic period of 15.382+/-0.001hr in agreement with the period from Rousselot et. al. 2003. Our observations show no evidence of a coma.",
-            "title": "VISUAL IMAGING AND PHOTOMETRY OF (29981) 1999 TD10 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "VISUAL IMAGING AND PHOTOMETRY OF (29981) 1999 TD10 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=PHX-M-SSI-2-EDR-V1.0",
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
+            "description": "The Surface Stereo Imager (SSI)  experiment on the Mars Phoenix Lander consists of one instrument  component plus command electronics. This SSI Imaging Operations EDR  data set contains raw data from the Surface Stereo Imager (SSI).",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.phx-m-ssi-2-edr-v1.0_sza2-y7ux",
+            "issued": "2021-05-21",
+            "keyword": [
+                "mars",
+                "phoenix"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=PHX-M-SSI-2-EDR-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.phx-m-ssi-2-edr-v1.0_sza2-y7ux",
-            "description": "The Surface Stereo Imager (SSI)  experiment on the Mars Phoenix Lander consists of one instrument  component plus command electronics. This SSI Imaging Operations EDR  data set contains raw data from the Surface Stereo Imager (SSI).",
-            "title": "PHOENIX MARS SURFACE STEREO IMAGER 2 \n                                      EDR VERSION 1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "PHOENIX MARS SURFACE STEREO IMAGER 2 \n                                      EDR VERSION 1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/IFFMYHMDBEHW",
             "citation": "AIRS project. 2019-11-15. AIRS3SPM. Version 7.0. Aqua/AIRS L3 Monthly Support Product (AIRS-only) 1 degree x 1 degree V7.0. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/IFFMYHMDBEHW. https://disc.gsfc.nasa.gov/datacollection/AIRS3SPM_7.0.html. Digital Science Data.",
-            "issued": "2002-09-01",
-            "temporal": "2002-09-01T00:00:00Z/2025-01-13T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-01",
-            "references": [
-                "https://doi.org/10.1117/1.JRS.8.084994",
-                "https://doi.org/10.5194/acp-14-399-2014"
-            ],
-            "keyword": [
-                "precipitation",
-                "atmosphere",
-                "atmospheric chemistry",
-                "ocean temperature",
-                "air quality",
-                "atmospheric pressure",
-                "oceans",
-                "atmospheric radiation",
-                "land surface",
-                "earth science",
-                "atmospheric water vapor",
-                "clouds",
-                "atmospheric temperature",
-                "altitude",
-                "surface radiative properties",
-                "surface thermal properties"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "LENA IREDELL",
                 "hasEmail": "mailto:lena.iredell@nasa.gov"
             },
+            "creator": "AIRS project",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C1701805668-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "The Atmospheric Infrared Sounder (AIRS) is a grating spectrometer (R = 1200) aboard the second Earth Observing System (EOS) polar-orbiting platform, EOS Aqua. In combination with the Advanced Microwave Sounding Unit (AMSU) and the Humidity Sounder for Brazil (HSB), AIRS constitutes an innovative atmospheric sounding group of visible, infrared, and microwave sensors. The L3 support products are similar to the L3 standard products but contain fields which are not fully validated, or are inputs or intermediary values. Because no quality control information is available for some of these fields, values from failed retrievals may be included.\n\nThe value for each grid box is the sum of the values that fall within the 1x1 area divided by the number of points in the\nbox.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "AIRS3SPM",
-            "creator": "AIRS project",
-            "graphic-preview-description": "Sample data of the \"AIRS/Aqua Level 3 monthly standard physical retrieval product (AIRS only)\".",
-            "title": "Aqua/AIRS L3 Monthly Support Product (AIRS-only) 1 degree x 1 degree V7.0 at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/AIRS3SPM_7.0.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FIFFMYHMDBEHW",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FIFFMYHMDBEHW",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/AIRS3SPM_7.0.png",
-                    "description": "Sample data of the \"AIRS/Aqua Level 3 monthly standard physical retrieval product (AIRS only)\".",
                     "@type": "dcat:Distribution",
+                    "description": "Sample data of the \"AIRS/Aqua Level 3 monthly standard physical retrieval product (AIRS only)\".",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/AIRS3SPM_7.0.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/AIRS3SPM_7.0.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/AIRS3SPM_7.0.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/Aqua_AIRS_Level3/AIRS3SPM.7.0/",
-                    "description": "Access the data via HTTP.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTP.",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/Aqua_AIRS_Level3/AIRS3SPM.7.0/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/opendap/Aqua_AIRS_Level3/AIRS3SPM.7.0/",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/opendap/Aqua_AIRS_Level3/AIRS3SPM.7.0/",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=AIRS3SPM+7.0",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=AIRS3SPM+7.0",
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
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/AIRS/V7_L3_User_Guide.pdf",
-                    "description": "AIRS Version 7 Level 3 Product User Guide",
                     "@type": "dcat:Distribution",
+                    "description": "AIRS Version 7 Level 3 Product User Guide",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/AIRS/V7_L3_User_Guide.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
                 }
             ],
+            "graphic-preview-description": "Sample data of the \"AIRS/Aqua Level 3 monthly standard physical retrieval product (AIRS only)\".",
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/AIRS3SPM_7.0.png",
+            "identifier": "C1701805668-GES_DISC",
+            "issued": "2002-09-01",
+            "keyword": [
+                "precipitation",
+                "atmosphere",
+                "atmospheric chemistry",
+                "ocean temperature",
+                "air quality",
+                "atmospheric pressure",
+                "oceans",
+                "atmospheric radiation",
+                "land surface",
+                "earth science",
+                "atmospheric water vapor",
+                "clouds",
+                "atmospheric temperature",
+                "altitude",
+                "surface radiative properties",
+                "surface thermal properties"
+            ],
+            "landingPage": "https://doi.org/10.5067/IFFMYHMDBEHW",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2025-01-01",
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
+            "series-name": "AIRS3SPM",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2002-09-01T00:00:00Z/2025-01-13T00:00:00Z",
             "theme": [
                 "Aqua",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Aqua/AIRS L3 Monthly Support Product (AIRS-only) 1 degree x 1 degree V7.0 at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ECL5M-OBP4B",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "ECCO Consortium, Fukumori, I., Wang, O., Fenty, I., Forget, G., Heimbach, P., & Ponte, R. M.. 2021-10-01. ECCO Ocean Bottom Pressure - Monthly Mean llc90 Grid (Version 4 Release 4 Errata). Version V4r4b. PO.DAAC. Archived by National Aeronautics and Space Administration, U.S. Government, PO.DAAC. https://doi.org/10.5067/ECL5M-OBP4B.",
-            "issued": "1992-01-01",
-            "temporal": "1992-01-01T00:00:00Z/2018-01-01T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2017-12-31",
-            "references": [
-                "https://doi.org/10.5281/zenodo.3765928"
-            ],
-            "keyword": [
-                "earth science",
-                "ocean pressure",
-                "oceans"
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
-            "identifier": "C2129197196-POCLOUD",
-            "description": "This dataset provides monthly-averaged ocean bottom pressure and model ocean bottom pressure anomaly on the native Lat-Lon-Cap 90 (LLC90) model grid from the ECCO Version 4 Release 4b (V4r4b) ocean and sea-ice state estimate. V4r4b is an errata for ECCO Version 4, Release 4 (V4r4). Estimating the Circulation and Climate of the Ocean (ECCO) ocean and sea-ice state estimates are dynamically and kinematically-consistent reconstructions of the three-dimensional time-evolving ocean, sea-ice, and surface atmospheric states. ECCO V4r4b is a free-running solution of the 1-degree global configuration of the MIT general circulation model (MITgcm) that has been fit to observations in a least-squares sense. Observational data constraints used in V4r4b include sea surface height (SSH) from satellite altimeters [ERS-1/2, TOPEX/Poseidon, GFO, ENVISAT, Jason-1,2,3, CryoSat-2, and SARAL/AltiKa]; sea surface temperature (SST) from satellite radiometers [AVHRR], sea surface salinity (SSS) from the Aquarius satellite radiometer/scatterometer, ocean bottom pressure (OBP) from the GRACE satellite gravimeter; sea ice concentration from satellite radiometers [SSM/I and SSMIS], and in-situ ocean temperature and salinity measured with conductivity-temperature-depth (CTD) sensors and expendable bathythermographs (XBTs) from several programs [e.g., WOCE, GO-SHIP, Argo, and others] and platforms [e.g., research vessels, gliders, moorings, ice-tethered profilers, and instrumented pinnipeds]. V4r4b covers the period 1992-01-01T12:00:00 to 2018-01-01T00:00:00.",
-            "release-place": "PO.DAAC",
-            "graphic-preview-description": "Thumbnail",
             "creator": "ECCO Consortium, Fukumori, I., Wang, O., Fenty, I., Forget, G., Heimbach, P., & Ponte, R. M.",
-            "title": "ECCO Ocean Bottom Pressure - Monthly Mean llc90 Grid (Version 4 Release 4b)",
-            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/ECCO_L4_OBP_LLC0090GRID_MONTHLY_V4R4.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "This dataset provides monthly-averaged ocean bottom pressure and model ocean bottom pressure anomaly on the native Lat-Lon-Cap 90 (LLC90) model grid from the ECCO Version 4 Release 4b (V4r4b) ocean and sea-ice state estimate. V4r4b is an errata for ECCO Version 4, Release 4 (V4r4). Estimating the Circulation and Climate of the Ocean (ECCO) ocean and sea-ice state estimates are dynamically and kinematically-consistent reconstructions of the three-dimensional time-evolving ocean, sea-ice, and surface atmospheric states. ECCO V4r4b is a free-running solution of the 1-degree global configuration of the MIT general circulation model (MITgcm) that has been fit to observations in a least-squares sense. Observational data constraints used in V4r4b include sea surface height (SSH) from satellite altimeters [ERS-1/2, TOPEX/Poseidon, GFO, ENVISAT, Jason-1,2,3, CryoSat-2, and SARAL/AltiKa]; sea surface temperature (SST) from satellite radiometers [AVHRR], sea surface salinity (SSS) from the Aquarius satellite radiometer/scatterometer, ocean bottom pressure (OBP) from the GRACE satellite gravimeter; sea ice concentration from satellite radiometers [SSM/I and SSMIS], and in-situ ocean temperature and salinity measured with conductivity-temperature-depth (CTD) sensors and expendable bathythermographs (XBTs) from several programs [e.g., WOCE, GO-SHIP, Argo, and others] and platforms [e.g., research vessels, gliders, moorings, ice-tethered profilers, and instrumented pinnipeds]. V4r4b covers the period 1992-01-01T12:00:00 to 2018-01-01T00:00:00.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FECL5M-OBP4B",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FECL5M-OBP4B",
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
-                    "description": "The project website for the ECCO Consortium",
                     "@type": "dcat:Distribution",
+                    "description": "The project website for the ECCO Consortium",
+                    "downloadURL": "https://www.ecco-group.org",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://github.com/ECCO-GROUP/",
-                    "description": "Software maintained by ECCO Consortium on GitHub",
                     "@type": "dcat:Distribution",
+                    "description": "Software maintained by ECCO Consortium on GitHub",
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
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/web-misc/ecco/docs/v4r4_reproduction_howto.pdf",
-                    "description": "Instructions for reproducing ECCO Version 4 Release 4",
                     "@type": "dcat:Distribution",
+                    "description": "Instructions for reproducing ECCO Version 4 Release 4",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/web-misc/ecco/docs/v4r4_reproduction_howto.pdf",
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
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/web-misc/ecco/docs/v4r4_user_guide.pdf",
-                    "description": "ECCO Version 4 Release 4 User Guide",
                     "@type": "dcat:Distribution",
+                    "description": "ECCO Version 4 Release 4 User Guide",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/web-misc/ecco/docs/v4r4_user_guide.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/web-misc/ecco/docs/v4r4_synopsis.pdf",
-                    "description": "Synopsis of ECCO Version 4 Release 4",
                     "@type": "dcat:Distribution",
+                    "description": "Synopsis of ECCO Version 4 Release 4",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/web-misc/ecco/docs/v4r4_synopsis.pdf",
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
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/web-misc/ecco/docs/v4r4_overview_plots.pdf",
-                    "description": "Sample Plots -- gcmfaces analysis of ECCO V4, Release 4 (1992-2017)",
                     "@type": "dcat:Distribution",
+                    "description": "Sample Plots -- gcmfaces analysis of ECCO V4, Release 4 (1992-2017)",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/web-misc/ecco/docs/v4r4_overview_plots.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's product usage"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/ECCO_L4_OBP_LLC0090GRID_MONTHLY_V4R4.jpg",
-                    "description": "Thumbnail",
                     "@type": "dcat:Distribution",
+                    "description": "Thumbnail",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/ECCO_L4_OBP_LLC0090GRID_MONTHLY_V4R4.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/ECL5M-OBP4B",
-                    "description": "Access the data set landing page for the collection",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data set landing page for the collection",
+                    "downloadURL": "https://doi.org/10.5067/ECL5M-OBP4B",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2129197196-POCLOUD",
-                    "description": "Browse granule search results in Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse granule search results in Earthdata Search",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2129197196-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2129197196-POCLOUD",
-                    "description": "HTTPS endpoint for data browse and download",
                     "@type": "dcat:Distribution",
+                    "description": "HTTPS endpoint for data browse and download",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2129197196-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://ecco-group.org/docs/ECCO_V4r4_errata.pdf",
-                    "description": "ECCO V4r4b (V4r4 Errata) Document",
                     "@type": "dcat:Distribution",
+                    "description": "ECCO V4r4b (V4r4 Errata) Document",
+                    "downloadURL": "https://ecco-group.org/docs/ECCO_V4r4_errata.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View an important notice for this dataset"
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
+            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/ECCO_L4_OBP_LLC0090GRID_MONTHLY_V4R4.jpg",
+            "identifier": "C2129197196-POCLOUD",
+            "issued": "1992-01-01",
+            "keyword": [
+                "earth science",
+                "ocean pressure",
+                "oceans"
+            ],
+            "landingPage": "https://doi.org/10.5067/ECL5M-OBP4B",
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
+            "title": "ECCO Ocean Bottom Pressure - Monthly Mean llc90 Grid (Version 4 Release 4b)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ECTSS-MAP44",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "ECCO Consortium, Fukumori, I., Wang, O., Fenty, I., Forget, G., Heimbach, P., & Ponte, R. M.. 2021-04-19. ECCO Global Mean Atmospheric Pressure - Snapshot (Version 4 Release 4). Version V4r4. PO.DAAC. Archived by National Aeronautics and Space Administration, U.S. Government, PO.DAAC. https://doi.org/10.5067/ECTSS-MAP44. ECCO; ECCO Consortium, Fukumori, I., Wang, O., Fenty, I., Forget, G., Heimbach, P., & Ponte, R. M.; 2020; ECCO Global Mean Atmospheric Pressure - Snapshot (Version 4 Release 4); 10.5067/ECTSS-MAP44; https://podaac.jpl.nasa.gov/ECCO.",
-            "issued": "2021-01-01",
-            "temporal": "1992-01-01T00:00:00Z/2018-01-01T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2018-01-01",
-            "references": [
-                "https://doi.org/10.5281/zenodo.3765928"
-            ],
-            "keyword": [
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
-            "identifier": "C1991543729-POCLOUD",
-            "description": "This dataset provides instantaneous hourly global mean atmospheric pressure from the ECCO Version 4 Release 4 (V4r4) ocean and sea-ice state estimate. Estimating the Circulation and Climate of the Ocean (ECCO) ocean and sea-ice state estimates are dynamically and kinematically-consistent reconstructions of the three-dimensional time-evolving ocean, sea-ice, and surface atmospheric states. ECCO V4r4 is a free-running solution of the 1-degree global configuration of the MIT general circulation model (MITgcm) that has been fit to observations in a least-squares sense. Observational data constraints used in V4r4 include sea surface height and model sea level anomaly (SSH) from satellite altimeters [ERS-1/2, TOPEX/Poseidon, GFO, ENVISAT, Jason-1,2,3, CryoSat-2, and SARAL/AltiKa]; sea surface temperature (SST) from satellite radiometers [AVHRR], sea surface salinity (SSS) from the Aquarius satellite radiometer/scatterometer, ocean bottom pressure (OBP) from the GRACE satellite gravimeter; sea ice concentration from satellite radiometers [SSM/I and SSMIS], and in-situ ocean temperature and salinity measured with conductivity-temperature-depth (CTD) sensors and expendable bathythermographs (XBTs) from several programs [e.g., WOCE, GO-SHIP, Argo, and others] and platforms [e.g., research vessels, gliders, moorings, ice-tethered profilers, and instrumented pinnipeds]. V4r4 covers the period 1992-01-01T12:00:00 to 2018-01-01T00:00:00.",
-            "release-place": "PO.DAAC",
-            "graphic-preview-description": "Thumbnail image for Website",
             "creator": "ECCO Consortium, Fukumori, I., Wang, O., Fenty, I., Forget, G., Heimbach, P., & Ponte, R. M.",
-            "title": "ECCO Global Mean Atmospheric Pressure - Snapshot (Version 4 Release 4)",
-            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/ECCO_L4_GMAP_TIME_SERIES_SNAPSHOT_V4R4.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "This dataset provides instantaneous hourly global mean atmospheric pressure from the ECCO Version 4 Release 4 (V4r4) ocean and sea-ice state estimate. Estimating the Circulation and Climate of the Ocean (ECCO) ocean and sea-ice state estimates are dynamically and kinematically-consistent reconstructions of the three-dimensional time-evolving ocean, sea-ice, and surface atmospheric states. ECCO V4r4 is a free-running solution of the 1-degree global configuration of the MIT general circulation model (MITgcm) that has been fit to observations in a least-squares sense. Observational data constraints used in V4r4 include sea surface height and model sea level anomaly (SSH) from satellite altimeters [ERS-1/2, TOPEX/Poseidon, GFO, ENVISAT, Jason-1,2,3, CryoSat-2, and SARAL/AltiKa]; sea surface temperature (SST) from satellite radiometers [AVHRR], sea surface salinity (SSS) from the Aquarius satellite radiometer/scatterometer, ocean bottom pressure (OBP) from the GRACE satellite gravimeter; sea ice concentration from satellite radiometers [SSM/I and SSMIS], and in-situ ocean temperature and salinity measured with conductivity-temperature-depth (CTD) sensors and expendable bathythermographs (XBTs) from several programs [e.g., WOCE, GO-SHIP, Argo, and others] and platforms [e.g., research vessels, gliders, moorings, ice-tethered profilers, and instrumented pinnipeds]. V4r4 covers the period 1992-01-01T12:00:00 to 2018-01-01T00:00:00.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FECTSS-MAP44",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FECTSS-MAP44",
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
-                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/ECCO_L4_GMAP_TIME_SERIES_SNAPSHOT_V4R4.jpg",
-                    "description": "Thumbnail image for Website",
                     "@type": "dcat:Distribution",
+                    "description": "Thumbnail image for Website",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/ECCO_L4_GMAP_TIME_SERIES_SNAPSHOT_V4R4.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/ECTSS-MAP44",
-                    "description": "Access the data set landing page for the collection.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data set landing page for the collection.",
+                    "downloadURL": "https://doi.org/10.5067/ECTSS-MAP44",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1991543729-POCLOUD",
-                    "description": "Browse granule search results in Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse granule search results in Earthdata Search",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1991543729-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C1991543729-POCLOUD/temporal",
-                    "description": "Browse and download granules over HTTPS using the virtual directories service",
                     "@type": "dcat:Distribution",
+                    "description": "Browse and download granules over HTTPS using the virtual directories service",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C1991543729-POCLOUD/temporal",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 }
             ],
+            "graphic-preview-description": "Thumbnail image for Website",
+            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/ECCO_L4_GMAP_TIME_SERIES_SNAPSHOT_V4R4.jpg",
+            "identifier": "C1991543729-POCLOUD",
+            "issued": "2021-01-01",
+            "keyword": [
+                "earth science",
+                "atmosphere",
+                "atmospheric pressure"
+            ],
+            "landingPage": "https://doi.org/10.5067/ECTSS-MAP44",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2018-01-01",
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
+            "title": "ECCO Global Mean Atmospheric Pressure - Snapshot (Version 4 Release 4)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ASDC/SUBORBITAL/SOLVE1_jValue_AircraftInSitu_DC8_Data_1",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2023-07-19. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/ASDC/SUBORBITAL/SOLVE1_jValue_AircraftInSitu_DC8_Data_1.",
-            "issued": "2022-09-07",
-            "temporal": "1999-11-16T00:00:00Z/2000-03-15T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-09-07",
-            "keyword": [
-                "atmospheric chemistry",
-                "atmosphere",
-                "surface radiative properties",
-                "land surface",
-                "earth science",
-                "clouds",
-                "atmospheric water vapor",
-                "atmospheric temperature"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Swartz",
                 "hasEmail": "mailto:bill.swartz@jhuapl.edu"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/LARC/SD/ASDC"
-            },
-            "identifier": "C2569836834-LARC_ASDC",
             "description": "SOLVE1_jValue_AircraftInSitu_DC8_Data is the in-situ photolysis rate data collected by the DC-8 aircraft during the SAGE III Ozone Loss and Validation Experiment (SOLVE). Data was collected by the John Hopkins University Applied Physics Laboratory radiative transfer model and the Scanning Actinic Flux Spectroradiometer (SAFS). Data collection for this product is complete.\r\n\r\nThe SOLVE campaign was a NASA multi-program effort of the Upper Atmosphere Research Program (UARP), Atmospheric Effects of Aviation Project (AEAP), Atmospheric Chemistry Modeling and Analysis Program (ACMAP) and Earth Observing System (EOS) of NASA\u2019s Earth Science Enterprise (ESE). SOLVE\u2019s primary objective was for calibrating and validating the Stratospheric Aerosol and Gas Experiment (SAGE) III satellite measurements, while examining the processes that controlled ozone levels at a mid- to high-latitude range. The major goal of SAGE III was to quantitatively assess ozone loss at high latitudes. SOLVE was a two-phase experiment, the first phase, SOLVE, occurred during the fall of 1999 through the spring of 2000. The second phase, SOLVE II, occurred during the winter of 2003.\r\n\r\nSOLVE took place in the Arctic high-latitude region during the winter. The polar ozone depletion processes cause by human-produced chlorine and bromine are most active in mid-to-late winter and early spring in the high Arctic. In order to conduct this validation experiment, NASA deployed the NASA ER-2 aircraft and NASA DC-8 aircraft. The ER-2 measured a variety of atmospheric data, including ozone (O3), H2O, CO2, ClONO2, HCl, ClO/BrO, and Cl2O2. The DC-8 aircraft measured ozone, ClO/BrO, and aerosol, among other atmospheric data. SOLVE also utilized balloon platforms, ground-based instruments, and collaborations with the German Aerospace Center\u2019s (DLR) FALCON aircraft equipped with the OLEX Lidar to achieve the mission objectives. Overall, the campaign had 28 flights, with SOLVE featuring 17 total flights among the different aircrafts and SOLVE II featuring 11 flights.",
-            "title": "SOLVE I DC-8 Aircraft In-situ Photolysis Rate Data",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC%2FSUBORBITAL%2FSOLVE1_jValue_AircraftInSitu_DC8_Data_1",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC%2FSUBORBITAL%2FSOLVE1_jValue_AircraftInSitu_DC8_Data_1",
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
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/SOLVE/jValue_AircraftInSitu_DC8_Data_1/",
-                    "description": "ASDC Direct Data Download for SOLVE1_jValue_AircraftInSitu_DC8_Data_1",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for SOLVE1_jValue_AircraftInSitu_DC8_Data_1",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/SOLVE/jValue_AircraftInSitu_DC8_Data_1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 }
             ],
+            "identifier": "C2569836834-LARC_ASDC",
+            "issued": "2022-09-07",
+            "keyword": [
+                "atmospheric chemistry",
+                "atmosphere",
+                "surface radiative properties",
+                "land surface",
+                "earth science",
+                "clouds",
+                "atmospheric water vapor",
+                "atmospheric temperature"
+            ],
+            "landingPage": "https://doi.org/10.5067/ASDC/SUBORBITAL/SOLVE1_jValue_AircraftInSitu_DC8_Data_1",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2022-09-07",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/LARC/SD/ASDC"
+            },
             "spatial": "<?xml version=\"1.0\" encoding=\"UTF-8\"?><gml:Polygon xmlns:gml=\"http://www.opengis.net/gml/3.2\" srsName=\"EPSG:9825\"><gml:outerBoundaryIs><gml:LinearRing><gml:posList>-31.4 -180.0 -31.4 180.0 90.0 180.0 90.0 -180.0 -31.4 -180.0</gml:posList></gml:LinearRing></gml:outerBoundaryIs><gml:innerBoundaryIs></gml:innerBoundaryIs></gml:Polygon>",
+            "temporal": "1999-11-16T00:00:00Z/2000-03-15T23:59:59.999Z",
             "theme": [
                 "SOLVE",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "SOLVE I DC-8 Aircraft In-situ Photolysis Rate Data"
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
-                "knowledge",
-                "ask the academy",
-                "sharing",
-                "appel"
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
-            "identifier": "NASA-862__32",
             "description": "Academy of Program/Project & Engineering Leadership's Ask the Academy magazine past issues.",
-            "title": "Academy of Program/Project & Engineering Leadership ASK the Academy Past Issues",
-            "programCode": [
-                "026:045"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -1387997,578 +1387976,577 @@
                     "mediaType": "application/html"
                 }
             ],
-            "accrualPeriodicity": "R/P1M",
+            "identifier": "NASA-862__32",
+            "issued": "2018-06-25",
+            "keyword": [
+                "knowledge",
+                "ask the academy",
+                "sharing",
+                "appel"
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
-            "landingPage": "https://doi.org/10.7927/H4Q23X5Q",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Center for International Earth Science Information Network - CIESIN - Columbia University, and Centro Internacional de Agricultura Tropical - CIAT. 2005-12-31. Gridded Population of the World, Version 3 (GPWv3): Coastlines. Version 3.00. Palisades, NY. Archived by National Aeronautics and Space Administration, U.S. Government, NASA Socioeconomic Data and Applications Center (SEDAC). https://doi.org/10.7927/H4Q23X5Q. https://doi.org/10.7927/H4Q23X5Q.",
-            "issued": "2005-12-31",
-            "temporal": "2000-07-01T00:00:00Z/2000-07-01T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2005-12-31",
-            "references": [
-                "https://doi.org/10.7927/H4XK8CG2",
-                "https://doi.org/10.7927/H4P26W1B",
-                "https://doi.org/10.7927/H4K935FC",
-                "https://doi.org/10.7927/H4FJ2DQN",
-                "https://doi.org/10.7927/H49W0CDN",
-                "https://doi.org/10.7927/H4639MPP",
-                "https://doi.org/10.7927/H42B8VZZ",
-                "https://doi.org/10.7927/H4ST7MRB",
-                "https://doi.org/10.7927/H4TT4NWQ"
-            ],
-            "keyword": [
-                "human dimensions",
-                "boundaries",
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
-            "identifier": "C1000000003-SEDAC",
-            "description": "The Gridded Population of the World, Version 3 (GPWv3): Coastlines are derived from the land area grid to show the outlines of pixels (cells) that contain administrative Units in GPWv3. The coastlines are designed for cartographic use with the GPWv3 population raster data sets. GPWv3 is produced by the Columbia University Center for International Earth Science Information Network (CIESIN) in collaboration with Centro Internacional de Agricultura Tropical (CIAT).",
-            "release-place": "Palisades, NY",
-            "graphic-preview-description": "Sample browse graphic of the data set.",
             "creator": "Center for International Earth Science Information Network - CIESIN - Columbia University, and Centro Internacional de Agricultura Tropical - CIAT",
-            "title": "Gridded Population of the World, Version 3 (GPWv3): Coastlines",
-            "graphic-preview-file": "https://sedac.ciesin.columbia.edu/downloads/maps/gpw-v3/gpw-v3-coastlines/sedac-logo.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The Gridded Population of the World, Version 3 (GPWv3): Coastlines are derived from the land area grid to show the outlines of pixels (cells) that contain administrative Units in GPWv3. The coastlines are designed for cartographic use with the GPWv3 population raster data sets. GPWv3 is produced by the Columbia University Center for International Earth Science Information Network (CIESIN) in collaboration with Centro Internacional de Agricultura Tropical (CIAT).",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.7927%2FH4Q23X5Q",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.7927%2FH4Q23X5Q",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/downloads/maps/gpw-v3/gpw-v3-coastlines/sedac-logo.jpg",
-                    "description": "Sample browse graphic of the data set.",
                     "@type": "dcat:Distribution",
+                    "description": "Sample browse graphic of the data set.",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/downloads/maps/gpw-v3/gpw-v3-coastlines/sedac-logo.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/gpw-v3-coastlines/data-download",
-                    "description": "Data Download Page",
                     "@type": "dcat:Distribution",
+                    "description": "Data Download Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/gpw-v3-coastlines/data-download",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/gpw-v3-coastlines/maps/services",
-                    "description": "Web Map Service Page",
                     "@type": "dcat:Distribution",
+                    "description": "Web Map Service Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/gpw-v3-coastlines/maps/services",
+                    "mediaType": "text/html",
                     "title": "Use Web Map Service (WMS) to download the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/gpw-v3-coastlines",
-                    "description": "Data Set\u00a0Overview Page",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set\u00a0Overview Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/gpw-v3-coastlines",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "graphic-preview-description": "Sample browse graphic of the data set.",
+            "graphic-preview-file": "https://sedac.ciesin.columbia.edu/downloads/maps/gpw-v3/gpw-v3-coastlines/sedac-logo.jpg",
+            "identifier": "C1000000003-SEDAC",
+            "issued": "2005-12-31",
+            "keyword": [
+                "human dimensions",
+                "boundaries",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.7927/H4Q23X5Q",
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
+                "https://doi.org/10.7927/H4XK8CG2",
+                "https://doi.org/10.7927/H4P26W1B",
+                "https://doi.org/10.7927/H4K935FC",
+                "https://doi.org/10.7927/H4FJ2DQN",
+                "https://doi.org/10.7927/H49W0CDN",
+                "https://doi.org/10.7927/H4639MPP",
+                "https://doi.org/10.7927/H42B8VZZ",
+                "https://doi.org/10.7927/H4ST7MRB",
+                "https://doi.org/10.7927/H4TT4NWQ"
+            ],
+            "release-place": "Palisades, NY",
             "spatial": "-179.199552 -54.751503 179.848323 79.89196",
+            "temporal": "2000-07-01T00:00:00Z/2000-07-01T00:00:00Z",
             "theme": [
                 "GPW",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Gridded Population of the World, Version 3 (GPWv3): Coastlines"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG2-N-LECP-3-RDR-FAR-ENC-400MSEC-V1.0",
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
-                "voyager"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This far encounter data set consists of electron and ion counting rate data from the Low Energy Charged Particle (LECP) experiment on Voyager 2 while the spacecraft was within the vicinity of Neptune. This instrument measures the intensities of in-situ charged particles ( >13 keV electrons and >24 keV ions) with various levels of discrimination based on energy range and mass species. A subset of almost 100 LECP channels are included in this data set. The LECP data are globally calibrated to the extent possible. Particles include electrons, protons, alpha particles, and light, medium, and heavy nuclei particles.  The far encounter data are 0.4 second rate measurements within 1/8 of the LECP instrumental motor rotation period (the angular scanning periods, or step period).",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg2-n-lecp-3-rdr-far-enc-400msec-v1.0_szmp-9fz5",
+            "issued": "2018-06-26",
+            "keyword": [
+                "voyager"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG2-N-LECP-3-RDR-FAR-ENC-400MSEC-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg2-n-lecp-3-rdr-far-enc-400msec-v1.0_szmp-9fz5",
-            "description": "This far encounter data set consists of electron and ion counting rate data from the Low Energy Charged Particle (LECP) experiment on Voyager 2 while the spacecraft was within the vicinity of Neptune. This instrument measures the intensities of in-situ charged particles ( >13 keV electrons and >24 keV ions) with various levels of discrimination based on energy range and mass species. A subset of almost 100 LECP channels are included in this data set. The LECP data are globally calibrated to the extent possible. Particles include electrons, protons, alpha particles, and light, medium, and heavy nuclei particles.  The far encounter data are 0.4 second rate measurements within 1/8 of the LECP instrumental motor rotation period (the angular scanning periods, or step period).",
-            "title": "VG2 LECP 0.4S HIGH RESOLUTION NEPTUNE FAR ENCOUNTER DATA",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "VG2 LECP 0.4S HIGH RESOLUTION NEPTUNE FAR ENCOUNTER DATA"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.7927/H4CC0XNV",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Center for International Earth Science Information Network - CIESIN - Columbia University. 2017-10-13. Global Population Density Grid Time Series Estimates. Version 1.00. Palisades, NY. Archived by National Aeronautics and Space Administration, U.S. Government, NASA Socioeconomic Data and Applications Center (SEDAC). https://doi.org/10.7927/H4CC0XNV. https://doi.org/10.7927/H47M05W2.",
-            "issued": "2017-10-13",
-            "temporal": "1970-01-01T00:00:00Z/2000-12-31T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2017-10-13",
-            "references": [
-                "https://doi.org/10.7927/H4CC0XNV",
-                "https://doi.org/10.1111/j.1466-8238.2010.00587.x",
-                "https://doi.org/10.1177/0959683609356587",
-                "https://doi.org/10.7927/H4W093VW"
-            ],
-            "keyword": [
-                "human dimensions",
-                "population",
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
-            "identifier": "C1427603020-SEDAC",
-            "description": "The Global Population Density Grid Time Series Estimates provide a back-cast time series of population density grids based on the year 2000 population grid from SEDAC's Global Rural-Urban Mapping Project, Version 1 (GRUMPv1) data set. The grids were created by using rates of population change between decades from the coarser resolution History Database of the Global Environment (HYDE) database to back-cast the GRUMPv1 population density grids. Mismatches between the spatial extent of the HYDE calculated rates and GRUMPv1 population data were resolved via infilling rate cells based on a focal mean of values. Finally, the grids were adjusted so that the population totals for each country equaled the UN World Population Prospects (2008 Revision) estimates for that country for the respective year (1970, 1980, 1990, and 2000).  These data do not represent census observations for the years prior to 2000, and therefore can at best be thought of as estimations of the populations in given locations. The population grids are consistent internally within the time series, but are not recommended for use in creating longer time series with any other population grids, including GRUMPv1, Gridded Population of the World, Version 4 (GPWv4), or non-SEDAC developed population grids. These population grids served as an input to SEDAC's Global Estimated Net Migration Grids by Decade: 1970-2000 data set.",
-            "release-place": "Palisades, NY",
-            "graphic-preview-description": "Maps Download Page",
             "creator": "Center for International Earth Science Information Network - CIESIN - Columbia University",
-            "title": "Global Population Density Grid Time Series Estimates",
-            "graphic-preview-file": "https://sedac.ciesin.columbia.edu/data/set/popdynamics-global-pop-density-time-series-estimates/maps",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The Global Population Density Grid Time Series Estimates provide a back-cast time series of population density grids based on the year 2000 population grid from SEDAC's Global Rural-Urban Mapping Project, Version 1 (GRUMPv1) data set. The grids were created by using rates of population change between decades from the coarser resolution History Database of the Global Environment (HYDE) database to back-cast the GRUMPv1 population density grids. Mismatches between the spatial extent of the HYDE calculated rates and GRUMPv1 population data were resolved via infilling rate cells based on a focal mean of values. Finally, the grids were adjusted so that the population totals for each country equaled the UN World Population Prospects (2008 Revision) estimates for that country for the respective year (1970, 1980, 1990, and 2000).  These data do not represent census observations for the years prior to 2000, and therefore can at best be thought of as estimations of the populations in given locations. The population grids are consistent internally within the time series, but are not recommended for use in creating longer time series with any other population grids, including GRUMPv1, Gridded Population of the World, Version 4 (GPWv4), or non-SEDAC developed population grids. These population grids served as an input to SEDAC's Global Estimated Net Migration Grids by Decade: 1970-2000 data set.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.7927%2FH4CC0XNV",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.7927%2FH4CC0XNV",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/downloads/maps/popdynamics/popdynamics-global-pop-density-time-series-estimates/popdynamics-global-pop-density-time-series-estimates-1990-thumbnail.jpg",
-                    "description": "Sample browse graphic of the data set.",
                     "@type": "dcat:Distribution",
+                    "description": "Sample browse graphic of the data set.",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/downloads/maps/popdynamics/popdynamics-global-pop-density-time-series-estimates/popdynamics-global-pop-density-time-series-estimates-1990-thumbnail.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/popdynamics-global-pop-density-time-series-estimates/data-download",
-                    "description": "Data Download Page",
                     "@type": "dcat:Distribution",
+                    "description": "Data Download Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/popdynamics-global-pop-density-time-series-estimates/data-download",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/popdynamics-global-pop-density-time-series-estimates/maps",
-                    "description": "Maps Download Page",
                     "@type": "dcat:Distribution",
+                    "description": "Maps Download Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/popdynamics-global-pop-density-time-series-estimates/maps",
+                    "mediaType": "text/html",
                     "title": "Get a related map visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://sedac.ciesin.columbia.edu/data/set/popdynamics-global-pop-density-time-series-estimates/docs",
-                    "description": "Documentation Page",
                     "@type": "dcat:Distribution",
+                    "description": "Documentation Page",
+                    "downloadURL": "http://sedac.ciesin.columbia.edu/data/set/popdynamics-global-pop-density-time-series-estimates/docs",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/popdynamics-global-pop-density-time-series-estimates/maps/services",
-                    "description": "Web Map Service Page",
                     "@type": "dcat:Distribution",
+                    "description": "Web Map Service Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/popdynamics-global-pop-density-time-series-estimates/maps/services",
+                    "mediaType": "text/html",
                     "title": "Use Web Map Service (WMS) to download the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/popdynamics-global-pop-density-time-series-estimates",
-                    "description": "Data Set\u00a0Overview Page",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set\u00a0Overview Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/popdynamics-global-pop-density-time-series-estimates",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "graphic-preview-description": "Maps Download Page",
+            "graphic-preview-file": "https://sedac.ciesin.columbia.edu/data/set/popdynamics-global-pop-density-time-series-estimates/maps",
+            "identifier": "C1427603020-SEDAC",
+            "issued": "2017-10-13",
+            "keyword": [
+                "human dimensions",
+                "population",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.7927/H4CC0XNV",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2017-10-13",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "SEDAC"
+            },
+            "references": [
+                "https://doi.org/10.7927/H4CC0XNV",
+                "https://doi.org/10.1111/j.1466-8238.2010.00587.x",
+                "https://doi.org/10.1177/0959683609356587",
+                "https://doi.org/10.7927/H4W093VW"
+            ],
+            "release-place": "Palisades, NY",
             "spatial": "-180.0 -55.77 180.0 83.63",
+            "temporal": "1970-01-01T00:00:00Z/2000-12-31T00:00:00Z",
             "theme": [
                 "POPDYNAMICS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Global Population Density Grid Time Series Estimates"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.7265/N52R3PNT",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Yup'ik Environmental Knowledge Project, Version 1. Version 1. Archived by National Aeronautics and Space Administration, U.S. Government, National Snow and Ice Data Center. https://doi.org/10.7265/N52R3PNT.",
-            "issued": "2000-01-01",
-            "temporal": "2000-01-01T00:00:00Z/2025-01-27T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-25",
-            "keyword": [
-                "earth science",
-                "environmental impacts",
-                "land surface",
-                "land use/land cover",
-                "landscape",
-                "oceans",
-                "sea ice",
-                "infrastructure",
-                "geomorphology",
-                "human dimensions"
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
-            "identifier": "C1386246205-NSIDCV0",
             "description": "Over the last ten years the Calista Elders Council (CEC) staff has worked with elders from Bering Sea coastal communities to document Yup'ik place names. Elders have been eager to teach young people their rich history and named places of their homeland, including camp and settlement sites, rivers, sloughs, rocks, ponds, even sandbars and underwater channels. More than 3,000 names have been identified. Also included are Yup'ik views on the importance of place names, the land, values, and language.",
-            "title": "Yup'ik Environmental Knowledge Project, Version 1",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.7265%2FN52R3PNT",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.7265%2FN52R3PNT",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://eloka-arctic.org/communities/yupik/",
-                    "description": "Product website where you can access the data.",
                     "@type": "dcat:Distribution",
+                    "description": "Product website where you can access the data.",
+                    "downloadURL": "https://eloka-arctic.org/communities/yupik/",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.7265/N52R3PNT",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.7265/N52R3PNT",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.7265/N52R3PNT",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.7265/N52R3PNT",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C1386246205-NSIDCV0",
+            "issued": "2000-01-01",
+            "keyword": [
+                "earth science",
+                "environmental impacts",
+                "land surface",
+                "land use/land cover",
+                "landscape",
+                "oceans",
+                "sea ice",
+                "infrastructure",
+                "geomorphology",
+                "human dimensions"
+            ],
+            "landingPage": "https://doi.org/10.7265/N52R3PNT",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2025-01-25",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NSIDC"
+            },
             "spatial": "-163.7 61.4 -163.7 61.4",
+            "temporal": "2000-01-01T00:00:00Z/2025-01-27T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Yup'ik Environmental Knowledge Project, Version 1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/GRIP/DROPSONDE/DATA202",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Heymsfield, Gerald M and Kate  Young.2016. GRIP DC-8 DROPSONDE V3 [indicate subset used]. Dataset available online from the NASA Global Hydrometeorology Resource Center DAAC, Huntsville, Alabama, U.S.A. DOI: http://dx.doi.org/10.5067/GRIP/DROPSONDE/DATA202",
-            "issued": "2016-10-25",
-            "temporal": "2010-08-17T15:44:06Z/2010-09-22T21:41:13Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-05-20",
-            "keyword": [
-                "earth science",
-                "atmospheric winds",
-                "atmospheric water vapor",
-                "atmospheric temperature",
-                "atmospheric pressure",
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
-            "identifier": "C1979835081-GHRC_DAAC",
             "description": "The GRIP DC-8 Dropsonde V3 dataset consists of atmospheric pressure, dry-bulb temperature, dew point temperature, relative humidity, wind direction, wind speed, and fall rate measurements taken during 16 research flights during the Genesis and Rapid Intensification Processes (GRIP) campaign from August 17, 2010 to September 22, 2010. The GRIP campaign was conducted to better understand how tropical storms form and how these storms develop into major hurricanes. The DC-8 Airborne Vertical Atmospheric Profiling System (AVAPS) deploys integrated, highly accurate, GPS-located atmospheric profiling dropsondes to measure and record current atmospheric conditions in a vertical column below the aircraft. The dropsondes are ejected from a tube in the underside of the DC-8 aircraft. As the dropsonde descends to the surface via a parachute, it continuously measures and transmits data to the aircraft using a 400 MHz meteorological band telemetry link. Pressure, temperature and relative humidity, as well as GPS-based wind data were collected from 328 dropsondes. These Dropsonde data are in ASCII-csv file format.",
-            "title": "GRIP DC-8 DROPSONDE V3",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGRIP%2FDROPSONDE%2FDATA202",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGRIP%2FDROPSONDE%2FDATA202",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=gripdropdc83",
-                    "description": "Files may be downloaded directly to your workstation from this link",
                     "@type": "dcat:Distribution",
+                    "description": "Files may be downloaded directly to your workstation from this link",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=gripdropdc83",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
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
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/grip/Dropsonde_DC8/doc/gripdropdc83_dataset.pdf",
-                    "description": "The guide document contains detailed information about the dataset",
                     "@type": "dcat:Distribution",
+                    "description": "The guide document contains detailed information about the dataset",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/grip/Dropsonde_DC8/doc/gripdropdc83_dataset.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
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
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/home/about-ghrc/citing-ghrc-daac-data",
-                    "description": "Instructions for citing GHRC data",
                     "@type": "dcat:Distribution",
+                    "description": "Instructions for citing GHRC data",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/home/about-ghrc/citing-ghrc-daac-data",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C1979835081-GHRC_DAAC",
+            "issued": "2016-10-25",
+            "keyword": [
+                "earth science",
+                "atmospheric winds",
+                "atmospheric water vapor",
+                "atmospheric temperature",
+                "atmospheric pressure",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.5067/GRIP/DROPSONDE/DATA202",
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
             "spatial": "-96.7127 12.0041 -55.3201 34.7358",
+            "temporal": "2010-08-17T15:44:06Z/2010-09-22T21:41:13Z",
             "theme": [
                 "GRIP (HURRICANE)",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "GRIP DC-8 DROPSONDE V3"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MRO-M-MCS-2-EDR-V1.0",
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
+            "description": "Unknown",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mro-m-mcs-2-edr-v1.0_sztj-gj4i",
+            "issued": "2021-05-21",
+            "keyword": [
+                "mars",
+                "mars reconnaissance orbiter"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MRO-M-MCS-2-EDR-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mro-m-mcs-2-edr-v1.0_sztj-gj4i",
-            "description": "Unknown",
-            "title": "MRO MARS CLIMATE SOUNDER LEVEL 2 EDR V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "MRO MARS CLIMATE SOUNDER LEVEL 2 EDR V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1778",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Elder, C., P. Hanke, K.W. Anthony, D.R. Thompson, C.E. Miller, and A.K. Thorpe. 2020. ABoVE: Methane Flux across Two Thermokarst Lake Ecosystems, Interior Alaska, 2018. ORNL DAAC, Oak Ridge, Tennessee, USA. https://doi.org/10.3334/ORNLDAAC/1778",
-            "issued": "2020-06-26",
-            "temporal": "2018-07-17T00:00:00Z/2018-07-29T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-06-12",
-            "keyword": [
-                "atmosphere",
-                "biosphere",
-                "atmospheric chemistry",
-                "vegetation",
-                "earth science",
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
-            "identifier": "C2143402530-ORNL_CLOUD",
             "description": "This dataset provides diffusive methane (CH4) fluxes collected from two thermokarst lakes in the Goldstream Valley, north of Fairbanks in interior Alaska. Fluxes were collected from the littoral zones, adjacent shoreline, and upland vegetation. The data were collected during July 2018. Measurements were made using a mobile, closed chamber technique where chamber air was recirculated through a Los Gatos Research (LGR) Ultraportable Cavity Ring-down Spectrometer. The chamber was large enough to enclose emergent and upland vegetation up to 1.5 m in height, allowing plant-facilitated fluxes to be measured. These in situ measurements were used to verify spatial patterns in methane flux (i.e., exponential decay with distance from water) detected by NASA's Next Generation Airborne Visible/Infrared Imaging Spectrometer (AVIRIS-NG).",
-            "graphic-preview-description": "Photo of the custom-built chamber for measuring in situ trace gas fluxes from soil/vegetation and water surfaces (with flotation). The chamber (0.71 m x 0.71 m x 1.07 m = 0.533 m3) provides adequate height to enclose emergent grasses and reeds. The chamber is connected by tubing to a Los Gatos Ultra-Portable Greenhouse Gas Analyzer capable of measuring trace gasses at 1 Hz in recirculating air. Photo courtesy C. Elder.",
-            "title": "ABoVE: Methane Flux across Two Thermokarst Lake Ecosystems, Interior Alaska, 2018",
-            "graphic-preview-file": "https://daac.ornl.gov/ABOVE/guides/CH4_Flux_BigTrail_Goldstream_Fig1.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1778",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1778",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/above/CH4_Flux_BigTrail_Goldstream/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/above/CH4_Flux_BigTrail_Goldstream/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/ABOVE/guides/CH4_Flux_BigTrail_Goldstream.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/ABOVE/guides/CH4_Flux_BigTrail_Goldstream.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1778",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1778",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/CH4_Flux_BigTrail_Goldstream/comp/CH4_Flux_BigTrail_Goldstream.pdf",
-                    "description": "ABoVE: Methane Flux across Two Thermokarst Lake Ecosystems, Interior Alaska, 2018: CH4_Flux_BigTrail_Goldstream.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "ABoVE: Methane Flux across Two Thermokarst Lake Ecosystems, Interior Alaska, 2018: CH4_Flux_BigTrail_Goldstream.pdf",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/CH4_Flux_BigTrail_Goldstream/comp/CH4_Flux_BigTrail_Goldstream.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://daac.ornl.gov/ABOVE/guides/CH4_Flux_BigTrail_Goldstream_Fig1.png",
-                    "description": "Photo of the custom-built chamber for measuring in situ trace gas fluxes from soil/vegetation and water surfaces (with flotation). The chamber (0.71 m x 0.71 m x 1.07 m = 0.533 m3) provides adequate height to enclose emergent grasses and reeds. The chamber is connected by tubing to a Los Gatos Ultra-Portable Greenhouse Gas Analyzer capable of measuring trace gasses at 1 Hz in recirculating air. Photo courtesy C. Elder.",
                     "@type": "dcat:Distribution",
+                    "description": "Photo of the custom-built chamber for measuring in situ trace gas fluxes from soil/vegetation and water surfaces (with flotation). The chamber (0.71 m x 0.71 m x 1.07 m = 0.533 m3) provides adequate height to enclose emergent grasses and reeds. The chamber is connected by tubing to a Los Gatos Ultra-Portable Greenhouse Gas Analyzer capable of measuring trace gasses at 1 Hz in recirculating air. Photo courtesy C. Elder.",
+                    "downloadURL": "https://daac.ornl.gov/ABOVE/guides/CH4_Flux_BigTrail_Goldstream_Fig1.png",
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
+            "graphic-preview-description": "Photo of the custom-built chamber for measuring in situ trace gas fluxes from soil/vegetation and water surfaces (with flotation). The chamber (0.71 m x 0.71 m x 1.07 m = 0.533 m3) provides adequate height to enclose emergent grasses and reeds. The chamber is connected by tubing to a Los Gatos Ultra-Portable Greenhouse Gas Analyzer capable of measuring trace gasses at 1 Hz in recirculating air. Photo courtesy C. Elder.",
+            "graphic-preview-file": "https://daac.ornl.gov/ABOVE/guides/CH4_Flux_BigTrail_Goldstream_Fig1.png",
+            "identifier": "C2143402530-ORNL_CLOUD",
+            "issued": "2020-06-26",
+            "keyword": [
+                "atmosphere",
+                "biosphere",
+                "atmospheric chemistry",
+                "vegetation",
+                "earth science",
+                "surface water",
+                "terrestrial hydrosphere"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1778",
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
             "spatial": "-147.85 64.92 -147.82 64.92",
+            "temporal": "2018-07-17T00:00:00Z/2018-07-29T23:59:59Z",
             "theme": [
                 "ABoVE",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "ABoVE: Methane Flux across Two Thermokarst Lake Ecosystems, Interior Alaska, 2018"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/MEASURES/DMSPF11/SSMI/DATA201",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Chris Kidd. PRECIP_SSMI_F11. Version 1. NASA MEASURES Precipitation Ensemble based on SSM/I DMSP F11 NASA PPS L1C V06 Tbs. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/MEASURES/DMSPF11/SSMI/DATA201. https://measures.gsfc.nasa.gov/datacollection/PRECIP_SSMI_F11_1.html. Digital Science Data.",
-            "issued": "2021-06-10",
-            "temporal": "1991-12-03T18:06:03Z/2000-05-16T16:57:56Z",
-            "@type": "dcat:Dataset",
-            "modified": "2021-06-10",
-            "keyword": [
-                "earth science",
-                "precipitation",
-                "atmosphere"
-            ],
-            "data-presentation-form": "Digital Science Data",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Chris Kidd",
                 "hasEmail": "mailto:chris.kidd@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
-            "identifier": "C2368308779-GES_DISC",
-            "description": "The data presented in this level 2 orbital product are rain rate estimates expressed as mm/hour determined from brightness temperatures (Tbs) obtained from the Special Sensor Microwave/Imager (SSM/I) flown on the US Defense Meteorological Satellite Program (DMSP) F11 mission. Most of the products generated in this data set are based upon the algorithms developed for the 3rd Algorithm Intercomparison Project (AIP-3) of the Global Precipitation Climatology Project (GPCP).  Details of these 15 algorithms and development of a quality score which is a measure of confidence in the estimate, along with processing and algorithmic flags, can be found in the Algorithm Theoretical Basis Document  (ATBD).  The data in this product cover the period from 1991 to 2000 with one file per orbit.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "PRECIP_SSMI_F11",
             "creator": "Chris Kidd",
-            "title": "NASA MEASURES Precipitation Ensemble based on SSM/I DMSP F11 NASA PPS L1C V06 Tbs 1-orbit L2 Swath 12x12km V1 (PRECIP_SSMI_F11) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/PRECIP_SSMI_F11.png",
-            "programCode": [
-                "026:001"
-            ],
+            "data-presentation-form": "Digital Science Data",
+            "description": "The data presented in this level 2 orbital product are rain rate estimates expressed as mm/hour determined from brightness temperatures (Tbs) obtained from the Special Sensor Microwave/Imager (SSM/I) flown on the US Defense Meteorological Satellite Program (DMSP) F11 mission. Most of the products generated in this data set are based upon the algorithms developed for the 3rd Algorithm Intercomparison Project (AIP-3) of the Global Precipitation Climatology Project (GPCP).  Details of these 15 algorithms and development of a quality score which is a measure of confidence in the estimate, along with processing and algorithmic flags, can be found in the Algorithm Theoretical Basis Document  (ATBD).  The data in this product cover the period from 1991 to 2000 with one file per orbit.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMEASURES%2FDMSPF11%2FSSMI%2FDATA201",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMEASURES%2FDMSPF11%2FSSMI%2FDATA201",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
@@ -1388608,306 +1388586,304 @@
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://measures.gesdisc.eosdis.nasa.gov/opendap/Precipitation/PRECIP_SSMI_F11.1/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://measures.gesdisc.eosdis.nasa.gov/opendap/Precipitation/PRECIP_SSMI_F11.1/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 }
             ],
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/PRECIP_SSMI_F11.png",
+            "identifier": "C2368308779-GES_DISC",
+            "issued": "2021-06-10",
+            "keyword": [
+                "earth science",
+                "precipitation",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.5067/MEASURES/DMSPF11/SSMI/DATA201",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2021-06-10",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
+            },
+            "release-place": "Greenbelt, MD, USA",
+            "series-name": "PRECIP_SSMI_F11",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "1991-12-03T18:06:03Z/2000-05-16T16:57:56Z",
             "theme": [
                 "MEaSUREs",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "NASA MEASURES Precipitation Ensemble based on SSM/I DMSP F11 NASA PPS L1C V06 Tbs 1-orbit L2 Swath 12x12km V1 (PRECIP_SSMI_F11) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/DARPX4AR2OYO",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "High Mountain Asia 2 m DEM, Surface Velocity, and Lagrangian Surface Mass Balance for Select Debris Covered Glaciers V001. Version 1. Archived by National Aeronautics and Space Administration, U.S. Government, NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/DARPX4AR2OYO.",
-            "issued": "2012-12-23",
-            "temporal": "2012-12-23T00:00:00Z/2017-12-22T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2017-12-22",
-            "keyword": [
-                "glaciers/ice sheets",
-                "models",
-                "snow/ice",
-                "cryosphere",
-                "digital elevation/digital terrain models",
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
-            "identifier": "C3226193732-NSIDC_ECS",
             "description": "This High Mountain Asia data set contains 2 m resolution digital elevation models (DEMs), surface velocities, surface mass balance (SMB) rates, and SMB uncertainties for six debris-covered glaciers in Nepal.\n\nSMB rate is estimated by applying a Lagrangian specification to DEMs derived from very-high-resolution optical stereo imagery acquired by Maxar Technologies satellites WorldView-1, WorldView-2, WorldView-3, and GeoEye-1.\n\nThis data set was granted permission for public release on 1 March 2024 under the National Reconnaissance Office (NRO) Electro-Optical Commercial Layer (EOCL) program.",
-            "title": "High Mountain Asia 2 m DEM, Surface Velocity, and Lagrangian Surface Mass Balance for Select Debris Covered Glaciers V001",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FDARPX4AR2OYO",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FDARPX4AR2OYO",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/HMA/HMA2_DCG_SMB.001/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/HMA/HMA2_DCG_SMB.001/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/data/data-access-tool/HMA2_DCG_SMB/versions/1/",
-                    "description": "Search and filter data files using a map-based interface",
                     "@type": "dcat:Distribution",
+                    "description": "Search and filter data files using a map-based interface",
+                    "downloadURL": "https://nsidc.org/data/data-access-tool/HMA2_DCG_SMB/versions/1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=HMA2_DCG_SMB+V001",
-                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=HMA2_DCG_SMB+V001",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/DARPX4AR2OYO",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/DARPX4AR2OYO",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/DARPX4AR2OYO",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/DARPX4AR2OYO",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C3226193732-NSIDC_ECS",
+            "issued": "2012-12-23",
+            "keyword": [
+                "glaciers/ice sheets",
+                "models",
+                "snow/ice",
+                "cryosphere",
+                "digital elevation/digital terrain models",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/DARPX4AR2OYO",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2017-12-22",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA NSIDC DAAC"
+            },
             "spatial": "85.51 28.2 85.77 28.39",
+            "temporal": "2012-12-23T00:00:00Z/2017-12-22T23:59:59.999Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "High Mountain Asia 2 m DEM, Surface Velocity, and Lagrangian Surface Mass Balance for Select Debris Covered Glaciers V001"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-VIRTIS-3-ESC3-MTP019-V2.0",
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
+            "description": "This release contains the calibrated data of the VIRTIS instrument on board of the spacecraft Rosetta. This volume contains data from the ESCORT  3 MTP019 phase, which occurred from 2015-07-29 to 2015-08-26 when at the vicinity of comet 67P. This data set V2.0 supersedes V1.0. It includes major updates on the data and documentation.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-virtis-3-esc3-mtp019-v2.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-VIRTIS-3-ESC3-MTP019-V2.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-virtis-3-esc3-mtp019-v2.0",
-            "description": "This release contains the calibrated data of the VIRTIS instrument on board of the spacecraft Rosetta. This volume contains data from the ESCORT  3 MTP019 phase, which occurred from 2015-07-29 to 2015-08-26 when at the vicinity of comet 67P. This data set V2.0 supersedes V1.0. It includes major updates on the data and documentation.",
-            "title": "ROSETTA-ORBITER 67P VIRTIS 3 ESCORT 3 MTP019 V2.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P VIRTIS 3 ESCORT 3 MTP019 V2.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/VIIRS/VNP09A1.002",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Eric Vermote, Belen Franch, Martin Claverie. 2023-06-12. VIIRS/NPP Surface Reflectance 8-Day L3 Global 1km SIN Grid V002. Sioux Falls, South Dakota, USA. Archived by National Aeronautics and Space Administration, U.S. Government, NASA EOSDIS Land Processes Distributed Active Archive Center. https://doi.org/10.5067/VIIRS/VNP09A1.002. https://doi.org/10.5067/VIIRS/VNP09A1.002. This data set was provided by the NASA/NOAA NPP Project..",
-            "issued": "2023-06-12",
-            "temporal": "2012-01-01T00:00:00Z/2024-06-03T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-06-12",
-            "keyword": [
-                "land surface",
-                "earth science",
-                "surface radiative properties"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Eric Vermote",
                 "hasEmail": "mailto:eric.f.vermote@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "LP DAAC"
-            },
-            "identifier": "C2519124793-LPCLOUD",
-            "description": "The 8-day Visible Infrared Imaging Radiometer Suite (VIIRS) (https://lpdaac.usgs.gov/dataset_discovery/viirs) surface reflectance (VNP09A1) Version 2 composite product provides an estimate of land surface reflectance from the NASA/NOAA Suomi National Polar-orbiting Partnership (Suomi NPP) VIIRS sensor for nine moderate resolution bands (M1 - M5, M7, M8, M10, M11) at nominal 1 kilometer resolution (~926 meter). The 1 kilometer dataset is derived through resampling the native 750 meter VIIRS resolution in the Level 2 input product. The data are corrected for atmospheric conditions such as the effects of molecular gases, including ozone and water vapor, and for the effects of atmospheric aerosols. Each pixel represents the best possible Level 2G observation during an 8-day period that is selected on the basis of high observation coverage, low sensor angle, the absence of clouds or cloud shadow, and aerosol loading. Included in the product along with the nine reflectance bands are day of year, reflectance band quality, control, reflectance state quality assurance, relative azimuth angle, sensor zenith angle, and solar zenith angle layers.",
-            "release-place": "Sioux Falls, South Dakota, USA",
-            "graphic-preview-description": "Browse image for Earthdata Search",
             "creator": "Eric Vermote, Belen Franch, Martin Claverie",
-            "title": "VIIRS/NPP Surface Reflectance 8-Day L3 Global 1km SIN Grid V002",
-            "graphic-preview-file": "https://cmr.earthdata.nasa.gov/browse-scaler/browse_images/granules/G2691784394-LPCLOUD?h=85&w=85",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The 8-day Visible Infrared Imaging Radiometer Suite (VIIRS) (https://lpdaac.usgs.gov/dataset_discovery/viirs) surface reflectance (VNP09A1) Version 2 composite product provides an estimate of land surface reflectance from the NASA/NOAA Suomi National Polar-orbiting Partnership (Suomi NPP) VIIRS sensor for nine moderate resolution bands (M1 - M5, M7, M8, M10, M11) at nominal 1 kilometer resolution (~926 meter). The 1 kilometer dataset is derived through resampling the native 750 meter VIIRS resolution in the Level 2 input product. The data are corrected for atmospheric conditions such as the effects of molecular gases, including ozone and water vapor, and for the effects of atmospheric aerosols. Each pixel represents the best possible Level 2G observation during an 8-day period that is selected on the basis of high observation coverage, low sensor angle, the absence of clouds or cloud shadow, and aerosol loading. Included in the product along with the nine reflectance bands are day of year, reflectance band quality, control, reflectance state quality assurance, relative azimuth angle, sensor zenith angle, and solar zenith angle layers.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FVIIRS%2FVNP09A1.002",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FVIIRS%2FVNP09A1.002",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2519124793-LPCLOUD",
-                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2519124793-LPCLOUD",
+                    "mediaType": "text/html",
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
-                    "downloadURL": "https://doi.org/10.5067/VIIRS/VNP09A1.002",
-                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
+                    "downloadURL": "https://doi.org/10.5067/VIIRS/VNP09A1.002",
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
-                    "downloadURL": "https://lpdaac.usgs.gov/documents/1657/VNP09_User_Guide_V2.pdf",
-                    "description": "The technical information in the Version 2.0 User's Guide enables users to interpret and use the data products.",
                     "@type": "dcat:Distribution",
+                    "description": "The technical information in the Version 2.0 User's Guide enables users to interpret and use the data products.",
+                    "downloadURL": "https://lpdaac.usgs.gov/documents/1657/VNP09_User_Guide_V2.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://lpdaac.usgs.gov/documents/122/VNP09_ATBD.pdf",
-                    "description": "The ATBD provides physical theory and mathematical procedures for the calculations used to produce the data products.",
                     "@type": "dcat:Distribution",
+                    "description": "The ATBD provides physical theory and mathematical procedures for the calculations used to produce the data products.",
+                    "downloadURL": "https://lpdaac.usgs.gov/documents/122/VNP09_ATBD.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's algorithm theoretical basis document"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/browse-scaler/browse_images/granules/G2691784394-LPCLOUD?h=85&w=85",
-                    "description": "Browse image for Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse image for Earthdata Search",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/browse-scaler/browse_images/granules/G2691784394-LPCLOUD?h=85&w=85",
+                    "mediaType": "text/html",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://viirsland.gsfc.nasa.gov/Val/LSR_Val.html",
-                    "description": "Validation at stage 3 has been achieved for the VIIRS surface reflectance product suite.",
                     "@type": "dcat:Distribution",
+                    "description": "Validation at stage 3 has been achieved for the VIIRS surface reflectance product suite.",
+                    "downloadURL": "https://viirsland.gsfc.nasa.gov/Val/LSR_Val.html",
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
+            "graphic-preview-file": "https://cmr.earthdata.nasa.gov/browse-scaler/browse_images/granules/G2691784394-LPCLOUD?h=85&w=85",
+            "identifier": "C2519124793-LPCLOUD",
+            "issued": "2023-06-12",
+            "keyword": [
+                "land surface",
+                "earth science",
+                "surface radiative properties"
+            ],
+            "landingPage": "https://doi.org/10.5067/VIIRS/VNP09A1.002",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2023-06-12",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "LP DAAC"
+            },
+            "release-place": "Sioux Falls, South Dakota, USA",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2012-01-01T00:00:00Z/2024-06-03T00:00:00Z",
             "theme": [
                 "NPP-JPSS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "VIIRS/NPP Surface Reflectance 8-Day L3 Global 1km SIN Grid V002"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1685783883-GES_DISC.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "OCO-2 Science Team/Michael Gunson, Annmarie Eldering. 2019-07-01. OCO2_L1B_Calibration. Version 10r. OCO-2 Level 1B calibrated, geolocated calibration spectra, Retrospective Processing V10r. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://disc.gsfc.nasa.gov/datacollection/OCO2_L1B_Calibration_10r.html. Digital Science Data.",
-            "issued": "2019-06-27",
-            "temporal": "2014-09-06T00:00:00Z/2022-01-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2017-06-17",
-            "keyword": [
-                "atmosphere",
-                "atmospheric chemistry",
-                "infrared wavelengths",
-                "spectral/engineering",
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
-            "identifier": "C1685783883-GES_DISC",
-            "description": "Version 10r is the current version of the data set. Older versions will no longer be available and are superseded by Version 10r.\n\nVersion 8r is the current version of the data set. Version 7r has been superseded by Version 8r.\nThe Orbiting Carbon Observatory is the first NASA missiondesigned to collect space-based measurements of atmospheric carbon dioxidewith the precision, resolution, and coverage needed to characterize theprocesses controlling its buildup in the atmosphere. The OCO-2 project uses the LEOStar-2 spacecraft that carries a single instrument. It incorporates three high-resolution spectrometers that make coincident measurements ofreflected sunlight in the near-infrared CO2 near 1.61 and 2.06 micrometers and inmolecular oxygen (O2) A-Band at 0.76 micrometers. The three spectrometers have different characteristics and are calibrated independently. Their raw data numbers (DN) are delivered correlated in time tothe Level 1B process as Level 1A products. Each band has 1016 spectralelements, although some are masked out in the L2 retrieval.This L1B product results from calibration mode measurements (e.g., Lunar,Solar, Dark observations), and thus it differs from the OCO2_L1B_Science(L1bSc) product. The differences in the product formats are only in the geolocation information provided. Whereas the L1bSc products report geolocation data for each sounding, calibration products report the directionof the boresight vector.This is the retrospective processing where the calibration data is estimated from the full timeseries of data (before, during, and after the measurements), and is expected to be of slightly higher quality.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "OCO2_L1B_Calibration",
             "creator": "OCO-2 Science Team/Michael Gunson, Annmarie Eldering",
-            "title": "OCO-2 Level 1B calibrated, geolocated calibration spectra, Retrospective Processing V10r (OCO2_L1B_Calibration) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/OCO2_L1B_Calibration_8r.jpeg",
-            "programCode": [
-                "026:001"
-            ],
+            "data-presentation-form": "Digital Science Data",
+            "description": "Version 10r is the current version of the data set. Older versions will no longer be available and are superseded by Version 10r.\n\nVersion 8r is the current version of the data set. Version 7r has been superseded by Version 8r.\nThe Orbiting Carbon Observatory is the first NASA missiondesigned to collect space-based measurements of atmospheric carbon dioxidewith the precision, resolution, and coverage needed to characterize theprocesses controlling its buildup in the atmosphere. The OCO-2 project uses the LEOStar-2 spacecraft that carries a single instrument. It incorporates three high-resolution spectrometers that make coincident measurements ofreflected sunlight in the near-infrared CO2 near 1.61 and 2.06 micrometers and inmolecular oxygen (O2) A-Band at 0.76 micrometers. The three spectrometers have different characteristics and are calibrated independently. Their raw data numbers (DN) are delivered correlated in time tothe Level 1B process as Level 1A products. Each band has 1016 spectralelements, although some are masked out in the L2 retrieval.This L1B product results from calibration mode measurements (e.g., Lunar,Solar, Dark observations), and thus it differs from the OCO2_L1B_Science(L1bSc) product. The differences in the product formats are only in the geolocation information provided. Whereas the L1bSc products report geolocation data for each sounding, calibration products report the directionof the boresight vector.This is the retrospective processing where the calibration data is estimated from the full timeseries of data (before, during, and after the measurements), and is expected to be of slightly higher quality.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -1388916,744 +1388892,787 @@
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/OCO2_L1B_Calibration_10r.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/OCO2_L1B_Calibration_10r.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=OCO2_L1B_Calibration",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=OCO2_L1B_Calibration",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://oco2.gesdisc.eosdis.nasa.gov/opendap/OCO2_L1B_Calibration.10r/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://oco2.gesdisc.eosdis.nasa.gov/opendap/OCO2_L1B_Calibration.10r/contents.html",
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
-                    "downloadURL": "https://oco2.gesdisc.eosdis.nasa.gov/data/OCO2_DATA/OCO2_L1B_Calibration.10r/",
-                    "description": "Access the data via HTTP.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTP.",
+                    "downloadURL": "https://oco2.gesdisc.eosdis.nasa.gov/data/OCO2_DATA/OCO2_L1B_Calibration.10r/",
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
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/OCO2_L1B_Calibration_8r.jpeg",
+            "identifier": "C1685783883-GES_DISC",
+            "issued": "2019-06-27",
+            "keyword": [
+                "atmosphere",
+                "atmospheric chemistry",
+                "infrared wavelengths",
+                "spectral/engineering",
+                "earth science"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1685783883-GES_DISC.html",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2017-06-17",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
+            },
+            "release-place": "Greenbelt, MD, USA",
+            "series-name": "OCO2_L1B_Calibration",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2014-09-06T00:00:00Z/2022-01-17T00:00:00Z",
             "theme": [
                 "OCO-2",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "OCO-2 Level 1B calibrated, geolocated calibration spectra, Retrospective Processing V10r (OCO2_L1B_Calibration) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ASDC_DAAC/FIRE/0083",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "1999-10-15. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/ASDC_DAAC/FIRE/0083.",
-            "issued": "1999-10-15",
-            "temporal": "1986-09-30T00:00:00Z/1986-10-31T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2018-07-11",
-            "keyword": [
-                "spectral/engineering",
-                "earth science",
-                "visible wavelengths",
-                "infrared wavelengths"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "WILLIAM ROSSOW",
                 "hasEmail": "mailto:wbrossow@ccny.cuny.edu"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/LARC/SD/ASDC"
-            },
-            "identifier": "C1000001104-LARC_ASDC",
             "description": "Results from ISCCP analysis of B3 radiance data (sampled to 25 km). Unlike the standard ISCCP product, these data are reported at original pixel resolution and contain detailed information about the algorithm decision.Data covers the region from: 55 degrees South to 90 degrees South (-55 to -90), 180 degrees West to 180 degrees East (-180 to +180). (Polar projection covers 55S - 90S or 55N - 90N, maximum; Midlatitude maps cover 55S to 55N, maximum.)Spatially sampled imaging data. Nominal spatial resolution is 25 km. Pixel field of view is 4 km (NOAA data). Earth location (latitude +/- 90 degrees, longitude +/- 180 degrees) is obtained for each pixel from ancillary data.",
-            "title": "First ISCCP Regional Experiment (FIRE) Cirrus 1 Surface Radiation Budget (SRB) Data over the South Pole",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC_DAAC%2FFIRE%2F0083",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC_DAAC%2FFIRE%2F0083",
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
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1000001104-LARC_ASDC",
-                    "description": "Earthdata Search for FIRE_CI1_SRB_SO_POLE_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for FIRE_CI1_SRB_SO_POLE_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1000001104-LARC_ASDC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/guide/base_fire_ci1_srb_dataset.pdf",
-                    "description": "FIRE Cirrus 1 SRB Langley DAAC Data Set Document",
                     "@type": "dcat:Distribution",
+                    "description": "FIRE Cirrus 1 SRB Langley DAAC Data Set Document",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/guide/base_fire_ci1_srb_dataset.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/readme/ci1_srb_sp.hdr",
-                    "description": "AU.NOA.S - Pixel-by-scanline map grid (tape files table)",
                     "@type": "dcat:Distribution",
+                    "description": "AU.NOA.S - Pixel-by-scanline map grid (tape files table)",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/readme/ci1_srb_sp.hdr",
+                    "mediaType": "text/html",
                     "title": "Access to this dataset's extended metadata"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/readme/ci1_srb_sp.toc",
-                    "description": "FIRE_CI1_SRB_SO_POLE_1 data table",
                     "@type": "dcat:Distribution",
+                    "description": "FIRE_CI1_SRB_SO_POLE_1 data table",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/readme/ci1_srb_sp.toc",
+                    "mediaType": "text/html",
                     "title": "Access to this dataset's extended metadata"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/readme/readme_fire_ci1_srb_so_pole.txt",
-                    "description": "FIRE Cirrus 1 SRB South Pole Data Set Read Software",
                     "@type": "dcat:Distribution",
+                    "description": "FIRE Cirrus 1 SRB South Pole Data Set Read Software",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/readme/readme_fire_ci1_srb_so_pole.txt",
+                    "mediaType": "text/html",
                     "title": "View this dataset's science data product software documentation"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/read_software/fci1srb_read.c",
-                    "description": "Read and verify program to use with FIRE I Cirrus (SRB) data experiments. - Direct File Download (.c)",
                     "@type": "dcat:Distribution",
+                    "description": "Read and verify program to use with FIRE I Cirrus (SRB) data experiments. - Direct File Download (.c)",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/read_software/fci1srb_read.c",
+                    "mediaType": "text/html",
                     "title": "View this dataset's science data product software documentation"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/read_software/fire_lib.c",
-                    "description": "fsdf_lib Program for reading FIRE Cirrus I, Cirrus II, and MS data sets - Direct File Download (.c)",
                     "@type": "dcat:Distribution",
+                    "description": "fsdf_lib Program for reading FIRE Cirrus I, Cirrus II, and MS data sets - Direct File Download (.c)",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/read_software/fire_lib.c",
+                    "mediaType": "text/html",
                     "title": "View this dataset's science data product software documentation"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/read_software/fire_sdf.h",
-                    "description": "Program to Read D2 HDF Format Files Produced by ISCCP - Direct File Download (.f)",
                     "@type": "dcat:Distribution",
+                    "description": "Program to Read D2 HDF Format Files Produced by ISCCP - Direct File Download (.f)",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/read_software/fire_sdf.h",
+                    "mediaType": "text/html",
                     "title": "View this dataset's science data product software documentation"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/read_software/firesdf_read.c",
-                    "description": "Readme to produce a general read program for users to access FIRE data set files in Standard Data Format (SDF) - Direct File Download (.c)",
                     "@type": "dcat:Distribution",
+                    "description": "Readme to produce a general read program for users to access FIRE data set files in Standard Data Format (SDF) - Direct File Download (.c)",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/read_software/firesdf_read.c",
+                    "mediaType": "text/html",
                     "title": "View this dataset's how-to documentation"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/read_software/fsdf_header.c",
-                    "description": "SDF_HEADER used to parse the FIRE SDF defined header file, and two supporting functions (SDF_DDR, DDR_VAR) - Direct File Download (.c)",
                     "@type": "dcat:Distribution",
+                    "description": "SDF_HEADER used to parse the FIRE SDF defined header file, and two supporting functions (SDF_DDR, DDR_VAR) - Direct File Download (.c)",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/read_software/fsdf_header.c",
+                    "mediaType": "text/html",
                     "title": "View this dataset's science data product software documentation"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/read_software/fsdf_vtoc.c",
-                    "description": "VTOC_read Program for reading records of FIRE Standard Data Format (SDF) Table Of Contents (VTOC) - Direct File Download (.c)",
                     "@type": "dcat:Distribution",
+                    "description": "VTOC_read Program for reading records of FIRE Standard Data Format (SDF) Table Of Contents (VTOC) - Direct File Download (.c)",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/read_software/fsdf_vtoc.c",
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
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/read_software/Makefile.fci1",
-                    "description": "Makefile.fci1 Release: 1.1 Date: 7/29/94",
                     "@type": "dcat:Distribution",
+                    "description": "Makefile.fci1 Release: 1.1 Date: 7/29/94",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/read_software/Makefile.fci1",
+                    "mediaType": "text/html",
                     "title": "View this dataset's science data product software documentation"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/ASDC_DAAC/FIRE/0083",
-                    "description": "DOI data set landing page for FIRE_CI1_SRB_SO_POLE_1",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for FIRE_CI1_SRB_SO_POLE_1",
+                    "downloadURL": "https://doi.org/10.5067/ASDC_DAAC/FIRE/0083",
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
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/FIRE/FIRE_CI1_SRB_SO_POLE/",
-                    "description": "ASDC Direct Data Download for FIRE_CI1_SRB_SO_POLE_1",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for FIRE_CI1_SRB_SO_POLE_1",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/FIRE/FIRE_CI1_SRB_SO_POLE/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/FIRE/FIRE_CI1_SRB_SO_POLE/contents.html",
-                    "description": "OPeNDAP data access for FIRE_CI1_SRB_SO_POLE_1",
                     "@type": "dcat:Distribution",
+                    "description": "OPeNDAP data access for FIRE_CI1_SRB_SO_POLE_1",
+                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/FIRE/FIRE_CI1_SRB_SO_POLE/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 }
             ],
+            "identifier": "C1000001104-LARC_ASDC",
+            "issued": "1999-10-15",
+            "keyword": [
+                "spectral/engineering",
+                "earth science",
+                "visible wavelengths",
+                "infrared wavelengths"
+            ],
+            "landingPage": "https://doi.org/10.5067/ASDC_DAAC/FIRE/0083",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2018-07-11",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/LARC/SD/ASDC"
+            },
             "spatial": "<?xml version=\"1.0\" encoding=\"UTF-8\"?><gml:Polygon xmlns:gml=\"http://www.opengis.net/gml/3.2\" srsName=\"EPSG:9825\"><gml:outerBoundaryIs><gml:LinearRing><gml:posList>-90.0 -180.0 -90.0 180.0 -55.0 180.0 -55.0 -180.0 -90.0 -180.0</gml:posList></gml:LinearRing></gml:outerBoundaryIs><gml:innerBoundaryIs></gml:innerBoundaryIs></gml:Polygon>",
+            "temporal": "1986-09-30T00:00:00Z/1986-10-31T23:59:59.999Z",
             "theme": [
                 "FIRE",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "First ISCCP Regional Experiment (FIRE) Cirrus 1 Surface Radiation Budget (SRB) Data over the South Pole"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG2-J-PLS-5-ELE-MOM-96.0SEC",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "THIS DATA SET CONTAINS THE DERIVED VALUES FOR THE ELECTRON MOMENT DENSITY AND TEMPERATURE AT JUPITER IN THE PLS ENERGY RANGE (10-5950 EV) DURING THE VOYAGER 2 ENCOUNTER. ADJACENT LOW AND HIGH ENERGY ELECTRON MEASUREMENTS ARE COMBINED TO FORM A COMPOSITE SPECTRA WHICH IS USED FOR THE MOMENT CALCULATION. THE MOMENT CALCULATIONS ARE PERFORMED AS DESCRIBED IN SCUDDER ET AL. (1981). THESE ASSUME ISOTROPIC DISTRIBUTIONS AND CORRECT FOR POSITIVE SPACECRAFT CHARGE WHEN APPLICABLE AND INTERPOLATE ELECTRON SPECTRA BELOW THE 10 EV INSTRUMENT THRESHOLD BEFORE PERFORMING THE INTEGRATION OVER VELOCITY. DATA FORMAT: COLUMNS 1-6 ARE TIME (YEAR, DAY, HOUR, MIN, SEC, MSEC) COLUMN 7 IS THE MOMENT DENSITY IN CM-3, COLUMN 8 THE TEMPERATURE IN EV. EACH ROW HAS FORMAT (6I4, 2E12.3). VALUES OF 1.E32 INDICATE THAT THE PARAMETER COULD NOT BE OBTAINED FROM THE DATA USING THE STANDARD ANALYSIS TECHNIQUE. ADDITIONAL INFORMATION ABOUT THIS DATASET AND THE INSTRUMENT WHICH PRODUCED IT CAN BE FOUND ELSEWHERE IN THIS CATALOG. AN OVERVIEW OF THE DATA IN THIS DATA SET CAN BE FOUND IN SCUDDER ET AL. (1981) AND A COMPLETE INSTRUMENT DESCRIPTION CAN BE FOUND IN BRIDGE (1977).",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg2-j-pls-5-ele-mom-96.0sec_szzh-dyyn",
             "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "comet sl9/jupiter collision",
                 "voyager",
                 "jupiter"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG2-J-PLS-5-ELE-MOM-96.0SEC",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg2-j-pls-5-ele-mom-96.0sec_szzh-dyyn",
-            "description": "THIS DATA SET CONTAINS THE DERIVED VALUES FOR THE ELECTRON MOMENT DENSITY AND TEMPERATURE AT JUPITER IN THE PLS ENERGY RANGE (10-5950 EV) DURING THE VOYAGER 2 ENCOUNTER. ADJACENT LOW AND HIGH ENERGY ELECTRON MEASUREMENTS ARE COMBINED TO FORM A COMPOSITE SPECTRA WHICH IS USED FOR THE MOMENT CALCULATION. THE MOMENT CALCULATIONS ARE PERFORMED AS DESCRIBED IN SCUDDER ET AL. (1981). THESE ASSUME ISOTROPIC DISTRIBUTIONS AND CORRECT FOR POSITIVE SPACECRAFT CHARGE WHEN APPLICABLE AND INTERPOLATE ELECTRON SPECTRA BELOW THE 10 EV INSTRUMENT THRESHOLD BEFORE PERFORMING THE INTEGRATION OVER VELOCITY. DATA FORMAT: COLUMNS 1-6 ARE TIME (YEAR, DAY, HOUR, MIN, SEC, MSEC) COLUMN 7 IS THE MOMENT DENSITY IN CM-3, COLUMN 8 THE TEMPERATURE IN EV. EACH ROW HAS FORMAT (6I4, 2E12.3). VALUES OF 1.E32 INDICATE THAT THE PARAMETER COULD NOT BE OBTAINED FROM THE DATA USING THE STANDARD ANALYSIS TECHNIQUE. ADDITIONAL INFORMATION ABOUT THIS DATASET AND THE INSTRUMENT WHICH PRODUCED IT CAN BE FOUND ELSEWHERE IN THIS CATALOG. AN OVERVIEW OF THE DATA IN THIS DATA SET CAN BE FOUND IN SCUDDER ET AL. (1981) AND A COMPLETE INSTRUMENT DESCRIPTION CAN BE FOUND IN BRIDGE (1977).",
-            "title": "VOYAGER 2 JUPITER PLASMA DERIVED ELECTRON MOMENTS 96 SEC",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "VOYAGER 2 JUPITER PLASMA DERIVED ELECTRON MOMENTS 96 SEC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=SDU-C-NAVCAM-3-RDR-WILD2-V1.0",
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
+            "description": "This data set contains calibrated images and calibration data from the Stardust Navigation Camera (NAVCAM) observations of comet 81P/Wild 2. 206 calibrated images were obtained over the 5-day period 2003-12-29 to 2004-01-02.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.sdu-c-navcam-3-rdr-wild2-v1.0_t23z-qcmd",
+            "issued": "2021-05-21",
+            "keyword": [
+                "81p/wild 2 (1978 a2)",
+                "stardust"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=SDU-C-NAVCAM-3-RDR-WILD2-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.sdu-c-navcam-3-rdr-wild2-v1.0_t23z-qcmd",
-            "description": "This data set contains calibrated images and calibration data from the Stardust Navigation Camera (NAVCAM) observations of comet 81P/Wild 2. 206 calibrated images were obtained over the 5-day period 2003-12-29 to 2004-01-02.",
-            "title": "STARDUST NAVCAM CALIBRATED IMAGES OF 81P/WILD 2",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "STARDUST NAVCAM CALIBRATED IMAGES OF 81P/WILD 2"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/NBBVU83OJYY1",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Hydrologic Outlets of the Greenland Ice Sheet, Version 1. Version 1. Archived by National Aeronautics and Space Administration, U.S. Government, NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/NBBVU83OJYY1.",
-            "issued": "1991-01-01",
-            "temporal": "1991-01-01T00:00:00Z/2000-12-31T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2000-12-31",
-            "keyword": [
-                "earth science",
-                "terrestrial hydrosphere",
-                "surface water",
-                "snow/ice",
-                "cryosphere"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Sarah Lewis",
                 "hasEmail": "mailto:sarahlewis@berkeley.edu"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA NSIDC DAAC"
-            },
-            "identifier": "C1386250445-NSIDCV0",
             "description": "The Hydrologic Outlets of the Greenland Ice Sheet data set contains GIS point shapefiles that include 891 observed and potential hydrologic outlets of the Greenland Ice Sheet, as identified by Lewis and Smith (2009), using satellite imagery. There are 460 observed hydrologic outlets that include proglacial streams and rivers emerging from the ice sheet (length scale >1 km), proglacial lakes touching the ice edge or clearly connected to it via streams or rivers (length scale >3 km), and sediment-rich plumes exiting tidewater glaciers into fjords. Also, there are 431 potential hydrologic outlets that include point locations with release of meltwater from fjords without obvious sediment discharge, as well as locations where the ice sheet directly connects to the ocean that cannot be proven to release meltwater.\n\nMeltwater features along the entire edge of the ice sheet were mapped via photo interpretation of GoogleEarth and Landsat ETM+ 15 m panchromatic data. The exact acquisition dates of the imagery are not available; however, owing to the light and relatively snow-free conditions seen in the GoogleEarth and Landsat images, it is presumed that they were taken during the summer season. Neither Landsat or GoogleEarth images were available for a section of ice sheet within the northern Tunu region; therefore, that region was excluded from the study. This excluded area represents approximately 0.9 percent of the ice sheet perimeter. Data are available via FTP, and can be read in any GIS software. The following journal article provides documentation for this data set: Lewis, Sarah and Laurence Smith. 2009. Hydrologic Drainage of the Greenland Ice Sheet. Hydrological Processes doi: 10.1002/hyp.7343. This journal article can be accessed from the Documentation link at the top of this Web page.",
-            "title": "Hydrologic Outlets of the Greenland Ice Sheet, Version 1",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FNBBVU83OJYY1",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FNBBVU83OJYY1",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/parca/nsidc-0372-hydrologic-outlets",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/parca/nsidc-0372-hydrologic-outlets",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/NBBVU83OJYY1",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/NBBVU83OJYY1",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/NBBVU83OJYY1",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/NBBVU83OJYY1",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C1386250445-NSIDCV0",
+            "issued": "1991-01-01",
+            "keyword": [
+                "earth science",
+                "terrestrial hydrosphere",
+                "surface water",
+                "snow/ice",
+                "cryosphere"
+            ],
+            "landingPage": "https://doi.org/10.5067/NBBVU83OJYY1",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2000-12-31",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA NSIDC DAAC"
+            },
             "spatial": "-80.79734 59.58015 -8.96739 85.02649",
+            "temporal": "1991-01-01T00:00:00Z/2000-12-31T23:59:59.999Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Hydrologic Outlets of the Greenland Ice Sheet, Version 1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.7927/H48050JH",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Center for International Earth Science Information Network - CIESIN - Columbia University, International Food Policy Research Institute - IFPRI, The World Bank, and Centro Internacional de Agricultura Tropical - CIAT. 2011-09-26. Global Rural-Urban Mapping Project, Version 1 (GRUMPv1): Land and Geographic Unit Area Grids. Version 1.00. Palisades, NY. Archived by National Aeronautics and Space Administration, U.S. Government, NASA Socioeconomic Data and Applications Center (SEDAC). https://doi.org/10.7927/H48050JH. https://doi.org/10.7927/H48050JH.",
-            "issued": "2011-09-26",
-            "temporal": "2000-07-01T00:00:00Z/2000-07-01T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2011-09-26",
-            "references": [
-                "https://doi.org/10.7927/H4VT1Q1H",
-                "https://doi.org/10.7927/H4CR5R8J",
-                "https://doi.org/10.7927/H44B2Z74",
-                "https://doi.org/10.7927/H40K26HS",
-                "https://doi.org/10.7927/H4R20Z93",
-                "https://doi.org/10.7927/H4M906KR",
-                "https://doi.org/10.7927/H4GH9FVG"
-            ],
-            "keyword": [
-                "land surface",
-                "land use/land cover",
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
-            "identifier": "C2210238389-SEDAC",
-            "description": "The Global Rural-Urban Mapping Project, Version 1 (GRUMPv1): Land and Geographic Unit Area Grids measure land areas in square kilometers and the mean Unit size (population-weighted) in square kilometers. The land area grid permits the summation of areas (net of permanent ice and water) at the same resolution as the population density, count, and urban-rural grids. The mean Unit size grids provide a quantitative surface that indicates the size of the input Unit(s) from which population count and density grids are derived. Additional global grids are created from the 30 arc-second grid at 1/4, 1/2, and 1 degree resolutions. This data set is produced by the Columbia University Center for International Earth Science Information Network (CIESIN) in collaboration with the International Food Policy Research Institute (IFPRI), The World Bank, and Centro Internacional de Agricultura Tropical (CIAT).",
-            "release-place": "Palisades, NY",
-            "graphic-preview-description": "Maps Download Page",
             "creator": "Center for International Earth Science Information Network - CIESIN - Columbia University, International Food Policy Research Institute - IFPRI, The World Bank, and Centro Internacional de Agricultura Tropical - CIAT",
-            "title": "Global Rural-Urban Mapping Project, Version 1 (GRUMPv1): Land and Geographic Unit Area Grids",
-            "graphic-preview-file": "https://sedac.ciesin.columbia.edu/data/set/grump-v1-land-geographic-unit-area/maps",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The Global Rural-Urban Mapping Project, Version 1 (GRUMPv1): Land and Geographic Unit Area Grids measure land areas in square kilometers and the mean Unit size (population-weighted) in square kilometers. The land area grid permits the summation of areas (net of permanent ice and water) at the same resolution as the population density, count, and urban-rural grids. The mean Unit size grids provide a quantitative surface that indicates the size of the input Unit(s) from which population count and density grids are derived. Additional global grids are created from the 30 arc-second grid at 1/4, 1/2, and 1 degree resolutions. This data set is produced by the Columbia University Center for International Earth Science Information Network (CIESIN) in collaboration with the International Food Policy Research Institute (IFPRI), The World Bank, and Centro Internacional de Agricultura Tropical (CIAT).",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.7927%2FH48050JH",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.7927%2FH48050JH",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/downloads/maps/grump-v1/grump-v1-land-geographic-unit-area/sedac-logo.jpg",
-                    "description": "Sample browse graphic of the data set.",
                     "@type": "dcat:Distribution",
+                    "description": "Sample browse graphic of the data set.",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/downloads/maps/grump-v1/grump-v1-land-geographic-unit-area/sedac-logo.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/grump-v1-land-geographic-unit-area/data-download",
-                    "description": "Data Download Page",
                     "@type": "dcat:Distribution",
+                    "description": "Data Download Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/grump-v1-land-geographic-unit-area/data-download",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/grump-v1-land-geographic-unit-area/maps",
-                    "description": "Maps Download Page",
                     "@type": "dcat:Distribution",
+                    "description": "Maps Download Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/grump-v1-land-geographic-unit-area/maps",
+                    "mediaType": "text/html",
                     "title": "Get a related map visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/grump-v1-land-geographic-unit-area/maps/services",
-                    "description": "Web Map Service Page",
                     "@type": "dcat:Distribution",
+                    "description": "Web Map Service Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/grump-v1-land-geographic-unit-area/maps/services",
+                    "mediaType": "text/html",
                     "title": "Use Web Map Service (WMS) to download the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/grump-v1-land-geographic-unit-area",
-                    "description": "Data Set\u00a0Overview Page",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set\u00a0Overview Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/grump-v1-land-geographic-unit-area",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "graphic-preview-description": "Maps Download Page",
+            "graphic-preview-file": "https://sedac.ciesin.columbia.edu/data/set/grump-v1-land-geographic-unit-area/maps",
+            "identifier": "C2210238389-SEDAC",
+            "issued": "2011-09-26",
+            "keyword": [
+                "land surface",
+                "land use/land cover",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.7927/H48050JH",
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
+                "https://doi.org/10.7927/H44B2Z74",
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
+            "title": "Global Rural-Urban Mapping Project, Version 1 (GRUMPv1): Land and Geographic Unit Area Grids"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/444",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Smith, E.A., and H.J. Cooper. 1999. BOREAS RSS-14 GOES-7 Level-1 Visible, Infrared, and Water Vapor Images. ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/444",
-            "issued": "2023-11-22",
-            "temporal": "1994-01-04T00:00:00Z/1995-07-08T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-04-11",
-            "keyword": [
-                "atmosphere",
-                "surface radiative properties",
-                "land surface",
-                "earth science",
-                "atmospheric water vapor",
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
-            "identifier": "C2929421613-ORNL_CLOUD",
             "description": "The level-1 BOREAS GOES-7 image data were collected by Remote Sensing Science Team 14 (RSS-14) personnel at Florida State University (FSU) and delivered to BORIS. The data cover the period of 01-Jan-1994 through 08-Jul-1995, with partial to complete coverage on the majority of the days. The data include three bands with eight-bit pixel values.",
-            "graphic-preview-description": "Browse Image",
-            "title": "BOREAS RSS-14 GOES-7 Level-1 Visible, Infrared, and Water Vapor Images",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/boreas_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F444",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F444",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/boreas/RSS/goes71/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/boreas/RSS/goes71/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/BOREAS/guides/RSS14_GOES7_L1.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/BOREAS/guides/RSS14_GOES7_L1.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/444",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/444",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/RSS/goes71/comp/goes71.def",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/RSS/goes71/comp/goes71.def",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/RSS/goes71/comp/README",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/RSS/goes71/comp/README",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/msword",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/RSS/goes71/comp/RSS14_GOES7_L1.doc",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/RSS/goes71/comp/RSS14_GOES7_L1.doc",
+                    "mediaType": "application/msword",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/RSS/goes71/comp/RSS14_GOES7_L1.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/RSS/goes71/comp/RSS14_GOES7_L1.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/RSS/goes71/comp/RSS14_GOES7_L1.txt",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/RSS/goes71/comp/RSS14_GOES7_L1.txt",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/RSS/goes71/comp/rss14_goes7_l1_inv.dat",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/RSS/goes71/comp/rss14_goes7_l1_inv.dat",
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
+            "identifier": "C2929421613-ORNL_CLOUD",
+            "issued": "2023-11-22",
+            "keyword": [
+                "atmosphere",
+                "surface radiative properties",
+                "land surface",
+                "earth science",
+                "atmospheric water vapor",
+                "atmospheric radiation"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/444",
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
             "spatial": "-111.0 50.09 -93.5 59.98",
+            "temporal": "1994-01-04T00:00:00Z/1995-07-08T23:59:59Z",
             "theme": [
                 "BOREAS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "BOREAS RSS-14 GOES-7 Level-1 Visible, Infrared, and Water Vapor Images"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NEAR-A-MSI-3-EDR-EROS%2FORBIT-V1.0",
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
-                "eros",
-                "near earth asteroid rendezvous"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This data set contains calibrated images of Eros taken in orbit by the NEAR Multi-Spectral Imager.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.near-a-msi-3-edr-eros-orbit-v1.0_t29c-qvkm",
+            "issued": "2018-06-26",
+            "keyword": [
+                "eros",
+                "near earth asteroid rendezvous"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NEAR-A-MSI-3-EDR-EROS%2FORBIT-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.near-a-msi-3-edr-eros-orbit-v1.0_t29c-qvkm",
-            "description": "This data set contains calibrated images of Eros taken in orbit by the NEAR Multi-Spectral Imager.",
-            "title": "NEAR MSI IMAGES FOR EROS/ORBIT",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "NEAR MSI IMAGES FOR EROS/ORBIT"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/SeaBASS/JGOFS_ARABIAN_SEA/DATA001",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/GSFC/SED/ESD/GCDC/OB.DAAC. https://doi.org/10.5067/SeaBASS/JGOFS_ARABIAN_SEA/DATA001.",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "undefined",
+                "hasEmail": "mailto:data@oceancolor.gsfc.nasa.gov"
+            },
+            "description": "Joint Global Ocean Flux Study (JGOFS) Arabian Sea measurements from 1994 and 1995.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSeaBASS%2FJGOFS_ARABIAN_SEA%2FDATA001",
+                    "mediaType": "text/html",
+                    "title": "Google Scholar search results"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "Detailed information about the SeaBASS Experiment such as cruises, funding, and investigators",
+                    "downloadURL": "https://seabass.gsfc.nasa.gov/experiment/JGOFS_Arabian_Sea/",
+                    "mediaType": "text/html",
+                    "title": "This dataset's landing page"
+                }
+            ],
+            "identifier": "C1633360384-OB_DAAC",
             "issued": "1994-03-15",
-            "temporal": "1994-03-15T00:00:02Z/2023-04-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-04-06",
             "keyword": [
                 "oceans",
                 "ocean optics",
@@ -1389662,54 +1389681,49 @@
                 "salinity/density",
                 "ocean temperature"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "undefined",
-                "hasEmail": "mailto:data@oceancolor.gsfc.nasa.gov"
-            },
+            "landingPage": "https://doi.org/10.5067/SeaBASS/JGOFS_ARABIAN_SEA/DATA001",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2023-04-06",
+            "programCode": [
+                "026:001"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "NASA/GSFC/SED/ESD/GCDC/OB.DAAC"
             },
-            "identifier": "C1633360384-OB_DAAC",
-            "description": "Joint Global Ocean Flux Study (JGOFS) Arabian Sea measurements from 1994 and 1995.",
-            "title": "Joint Global Ocean Flux Study (JGOFS) Arabian Sea measurements",
-            "programCode": [
-                "026:001"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSeaBASS%2FJGOFS_ARABIAN_SEA%2FDATA001",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
-                    "@type": "dcat:Distribution",
-                    "title": "Google Scholar search results"
-                },
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://seabass.gsfc.nasa.gov/experiment/JGOFS_Arabian_Sea/",
-                    "description": "Detailed information about the SeaBASS Experiment such as cruises, funding, and investigators",
-                    "@type": "dcat:Distribution",
-                    "title": "This dataset's landing page"
-                }
-            ],
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "1994-03-15T00:00:02Z/2023-04-17T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Joint Global Ocean Flux Study (JGOFS) Arabian Sea measurements"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.nasa.gov/d/t2c2-e9u8",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "GeneLab Outreach",
+                "hasEmail": "mailto:genelab-outreach@lists.nasa.gov"
+            },
+            "description": "Transcriptional profiling of human lymphoblastoid TK6 cells comparing mock irradiated cells with cells exposed 24 hours previously to 1.67 Gy HZE (1 GeV/amu iron ions accelerated at the NASA Space Research Laboratory (NSRL) of Brookhaven National Laboratory) or 2.5 Gy 137Cs gamma rays. TK6 cells were mock irradiated or exposed to HZE or gamma-rays and RNA was harvested 24 hours later. 3 biological replicates were independently grown and harvested during three different runs at the NSRL. One replicate per array.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "GeneLab Study Page",
+                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-2",
+                    "mediaType": "text/html",
+                    "title": "Response of human lymphoblastoid cells to HZE (iron ions) or gamma-rays"
+                }
+            ],
+            "identifier": "nasa_genelab_GLDS-2_t2c2-e9u8",
             "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
             "keyword": [
                 "p-gse16518-3",
                 "image_aquisition",
@@ -1389729,424 +1389743,419 @@
                 "bioassay_data_transformation",
                 "p-gse16518-5"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "GeneLab Outreach",
-                "hasEmail": "mailto:genelab-outreach@lists.nasa.gov"
-            },
+            "landingPage": "https://data.nasa.gov/d/t2c2-e9u8",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "nasa_genelab_GLDS-2_t2c2-e9u8",
-            "description": "Transcriptional profiling of human lymphoblastoid TK6 cells comparing mock irradiated cells with cells exposed 24 hours previously to 1.67 Gy HZE (1 GeV/amu iron ions accelerated at the NASA Space Research Laboratory (NSRL) of Brookhaven National Laboratory) or 2.5 Gy 137Cs gamma rays. TK6 cells were mock irradiated or exposed to HZE or gamma-rays and RNA was harvested 24 hours later. 3 biological replicates were independently grown and harvested during three different runs at the NSRL. One replicate per array.",
-            "title": "Response of human lymphoblastoid cells to HZE (iron ions) or gamma-rays",
-            "programCode": [
-                "026:005"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-2",
-                    "description": "GeneLab Study Page",
-                    "@type": "dcat:Distribution",
-                    "title": "Response of human lymphoblastoid cells to HZE (iron ions) or gamma-rays"
-                }
-            ],
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "Response of human lymphoblastoid cells to HZE (iron ions) or gamma-rays"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/GPMGV/MC3E/MULTIPLE/DATA202",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Heymsfield, Andrew J, Aaron  Bansemer and Michael R Poellot.2013. GPM GROUND VALIDATION NCAR CLOUD MICROPHYSICS PARTICLE PROBES MC3E [indicate subset used]. Dataset available online from the NASA Global Hydrometeorology Resource Center DAAC, Huntsville, Alabama, U.S.A. DOI: http://dx.doi.org/10.5067/GPMGV/MC3E/MULTIPLE/DATA202",
-            "issued": "2013-02-12",
-            "temporal": "2011-04-22T21:49:38Z/2011-06-02T18:19:36Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-04-28",
-            "keyword": [
-                "earth science",
-                "clouds",
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
-            "identifier": "C1979667818-GHRC_DAAC",
             "description": "The GPM Ground Validation NCAR Cloud Microphysics Particle Probes MC3E dataset was collected during the Midlatitude Continental Convective Clouds Experiment (MC3E), which took place in central Oklahoma during the April-June 2011 period. The overarching goal was to provide the most complete characterization of convective cloud systems, precipitation, and the environment that has ever been obtained, providing constraints for model cumulus parameterization and space-based rainfall retrieval algorithms over land that had never before been available. The GPM Ground Validation NCAR Cloud Microphysics Particle Probes MC3E dataset was obtained from three instruments carried aboard the University of North Dakota (UND) Cessna Citation aircraft. These probes, the 2D-C, Cloud Imaging Probe (CIP) and High Volume Precipitation Spectrometer (HVPS-3), collected particle size distributions and particle images which were processed by the National Center for Atmospheric Research (NCAR). Data were collected April 22, 2011 through June 2, 2011.",
-            "graphic-preview-description": "N/A",
-            "title": "GPM GROUND VALIDATION NCAR CLOUD MICROPHYSICS PARTICLE PROBES MC3E V1",
-            "graphic-preview-file": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/mc3e/cloud_microphysics_Citation/NCAR_particle_probes/browse/",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGPMGV%2FMC3E%2FMULTIPLE%2FDATA202",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGPMGV%2FMC3E%2FMULTIPLE%2FDATA202",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=gpmparprbmc3e",
-                    "description": "Files may be downloaded directly to your workstation from this link",
                     "@type": "dcat:Distribution",
+                    "description": "Files may be downloaded directly to your workstation from this link",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=gpmparprbmc3e",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/mc3e/cloud_microphysics_Citation/NCAR_particle_probes/browse/20110511/20110511_170200_2DC7.png",
-                    "description": "Sample browse image",
                     "@type": "dcat:Distribution",
+                    "description": "Sample browse image",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/mc3e/cloud_microphysics_Citation/NCAR_particle_probes/browse/20110511/20110511_170200_2DC7.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/mc3e/cloud_microphysics_Citation/NCAR_particle_probes/browse/20110511/20110511_171900_HVPS3.png",
-                    "description": "Sample browse image",
                     "@type": "dcat:Distribution",
+                    "description": "Sample browse image",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/mc3e/cloud_microphysics_Citation/NCAR_particle_probes/browse/20110511/20110511_171900_HVPS3.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/mc3e/cloud_microphysics_Citation/NCAR_particle_probes/browse/20110511/20110511_165500_CIP.png",
-                    "description": "Sample browse image",
                     "@type": "dcat:Distribution",
+                    "description": "Sample browse image",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/mc3e/cloud_microphysics_Citation/NCAR_particle_probes/browse/20110511/20110511_165500_CIP.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
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
-                    "downloadURL": "http://ghrc.nsstc.nasa.gov/uso/ds_docs/gpmgv/particle_probe/gpm_ncarparprb_dataset.html",
-                    "description": "The guide document contains detailed information about the dataset",
                     "@type": "dcat:Distribution",
+                    "description": "The guide document contains detailed information about the dataset",
+                    "downloadURL": "http://ghrc.nsstc.nasa.gov/uso/ds_docs/gpmgv/particle_probe/gpm_ncarparprb_dataset.html",
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
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/mc3e/cloud_microphysics_Citation/NCAR_particle_probes/browse/",
-                    "description": "N/A",
                     "@type": "dcat:Distribution",
+                    "description": "N/A",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/mc3e/cloud_microphysics_Citation/NCAR_particle_probes/browse/",
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
+            "graphic-preview-file": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/mc3e/cloud_microphysics_Citation/NCAR_particle_probes/browse/",
+            "identifier": "C1979667818-GHRC_DAAC",
+            "issued": "2013-02-12",
+            "keyword": [
+                "earth science",
+                "clouds",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.5067/GPMGV/MC3E/MULTIPLE/DATA202",
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
             "spatial": "-98.5 35.5 -96.5 37.5",
+            "temporal": "2011-04-22T21:49:38Z/2011-06-02T18:19:36Z",
             "theme": [
                 "MC3E",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "GPM GROUND VALIDATION NCAR CLOUD MICROPHYSICS PARTICLE PROBES MC3E V1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/6S7UHUH2K5RI",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Greenland Climate Network (GC-Net) Radiation for Arctic System Reanalysis, Version 1. Version 1. Archived by National Aeronautics and Space Administration, U.S. Government, NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/6S7UHUH2K5RI.",
-            "issued": "1995-01-01",
-            "temporal": "1995-01-01T00:00:00Z/2008-05-09T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2008-05-09",
-            "keyword": [
-                "earth science",
-                "atmospheric radiation",
-                "atmosphere"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "David Kindig",
                 "hasEmail": "mailto:kindig@nsidc.org"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA NSIDC DAAC"
-            },
-            "identifier": "C1386205153-NSIDCV0",
             "description": "This data set provides incoming shortwave radiation measurements from fourteen stations of the Greenland Climate Network (GC-Net) distributed over the Greenland Ice Sheet. The original data were obtained from the GC-Net and subsequently quality controlled. The data span from 01 January 1995 through 09 May 2008. The data set is approximately 15 MB comprised of fourteen Network Common Data Form (netCDF) files. The data are available via FTP.",
-            "title": "Greenland Climate Network (GC-Net) Radiation for Arctic System Reanalysis, Version 1",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2F6S7UHUH2K5RI",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2F6S7UHUH2K5RI",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/GCNet/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/GCNet/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/6S7UHUH2K5RI",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/6S7UHUH2K5RI",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/6S7UHUH2K5RI",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/6S7UHUH2K5RI",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C1386205153-NSIDCV0",
+            "issued": "1995-01-01",
+            "keyword": [
+                "earth science",
+                "atmospheric radiation",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.5067/6S7UHUH2K5RI",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2008-05-09",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA NSIDC DAAC"
+            },
             "spatial": "-61.09 63.15 -42.5 80.75",
+            "temporal": "1995-01-01T00:00:00Z/2008-05-09T23:59:59.999Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Greenland Climate Network (GC-Net) Radiation for Arctic System Reanalysis, Version 1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/2JA2F0NF99TF",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "SnowEx21 Prairie Station Digital Surface Models from UAV-LiDAR V001. Version 1. Archived by National Aeronautics and Space Administration, U.S. Government, NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/2JA2F0NF99TF.",
-            "issued": "2021-01-15",
-            "temporal": "2021-01-15T00:00:00Z/2021-03-04T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2021-03-04",
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
-            "identifier": "C3241729770-NSIDC_ECS",
             "description": "This dataset consists of Digital Surface Models (DSMs) derived from UAV-LiDAR acquired during the SnowEx 2021 field campaign at the Central Agricultural Research Center in central Montana (USA). The DSMs are at 0.3 m resolution and consist of one snow-off and seven snow-on flights.",
-            "title": "SnowEx21 Prairie Station Digital Surface Models from UAV-LiDAR V001",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2F2JA2F0NF99TF",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2F2JA2F0NF99TF",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/SNOWEX/SNEX21_PS_DSM.001/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/SNOWEX/SNEX21_PS_DSM.001/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=SNEX21_PS_DSM+V001",
-                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=SNEX21_PS_DSM+V001",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/data/data-access-tool/SNEX21_PS_DSM/versions/1",
-                    "description": "Search and filter data files using a map-based interface",
                     "@type": "dcat:Distribution",
+                    "description": "Search and filter data files using a map-based interface",
+                    "downloadURL": "https://nsidc.org/data/data-access-tool/SNEX21_PS_DSM/versions/1",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/2JA2F0NF99TF",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/2JA2F0NF99TF",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/2JA2F0NF99TF",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/2JA2F0NF99TF",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C3241729770-NSIDC_ECS",
+            "issued": "2021-01-15",
+            "keyword": [
+                "topography",
+                "land surface",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/2JA2F0NF99TF",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2021-03-04",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA NSIDC DAAC"
+            },
             "spatial": "-109.9595558 47.0562694 -109.945955 47.0655368",
+            "temporal": "2021-01-15T00:00:00Z/2021-03-04T23:59:59.999Z",
             "theme": [
                 "SnowEx",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "SnowEx21 Prairie Station Digital Surface Models from UAV-LiDAR V001"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-4-PRL-67P-M02-STRLIGHT-V1.0",
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
+            "description": "This CODMAC level 4 data set contains solar stray light corrected, radiometric calibrated and geometric distortion corrected (resampled) image data in W/m^2/sr/nm, acquired by the OSIRIS Narrow Angle Camera on the Rosetta spacecraft during the PRELANDING mission phase, covering the period from 2014-01-20T10:00:00.000 to 2014-05-07T12:47:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V1.0 is the first version of this dataset: Lien corrected dataset after October 2018 PSA/PDS external peer review.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-4-prl-67p-m02-strlight-v1.0_t2k9-7gvt",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-4-PRL-67P-M02-STRLIGHT-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-4-prl-67p-m02-strlight-v1.0_t2k9-7gvt",
-            "description": "This CODMAC level 4 data set contains solar stray light corrected, radiometric calibrated and geometric distortion corrected (resampled) image data in W/m^2/sr/nm, acquired by the OSIRIS Narrow Angle Camera on the Rosetta spacecraft during the PRELANDING mission phase, covering the period from 2014-01-20T10:00:00.000 to 2014-05-07T12:47:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V1.0 is the first version of this dataset: Lien corrected dataset after October 2018 PSA/PDS external peer review.",
-            "title": "ROSETTA-ORBITER 67P OSINAC 4 PRL-MTP002 RDR-STRLIGHT V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P OSINAC 4 PRL-MTP002 RDR-STRLIGHT V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG2-N-PRA-3-RDR-LOWBAND-6SEC-V1.0",
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
-                "neptune",
-                "voyager"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "Voyager 2 PRA lowband 6 second data recorded at Neptune.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg2-n-pra-3-rdr-lowband-6sec-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "neptune",
+                "voyager"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG2-N-PRA-3-RDR-LOWBAND-6SEC-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg2-n-pra-3-rdr-lowband-6sec-v1.0",
-            "description": "Voyager 2 PRA lowband 6 second data recorded at Neptune.",
-            "title": "VG2 N PRA 3 RDR LOWBAND 6SEC V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "VG2 N PRA 3 RDR LOWBAND 6SEC V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-X-ALICE-2-CR1-V1.0",
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
-                "unknown",
-                "international rosetta mission"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This data set contains CODMAC level 2 instrument checkout data acquired by the Rosetta Orbiter ALICE UV Spectrometer during the first cruise phase of the Rosetta mission, which occurred 2004-06-07 to 2004-09-05.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-x-alice-2-cr1-v1.0_t2q9-pi9u",
+            "issued": "2018-06-26",
+            "keyword": [
+                "unknown",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-X-ALICE-2-CR1-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-x-alice-2-cr1-v1.0_t2q9-pi9u",
-            "description": "This data set contains CODMAC level 2 instrument checkout data acquired by the Rosetta Orbiter ALICE UV Spectrometer during the first cruise phase of the Rosetta mission, which occurred 2004-06-07 to 2004-09-05.",
-            "title": "ROSETTA-ORBITER CHECK ALICE 2 CR1 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "ROSETTA-ORBITER CHECK ALICE 2 CR1 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://nasa3d.arc.nasa.gov/detail/sorce",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2018-06-25",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
-            "references": [
-                "http://lasp.colorado.edu/sorce/index.htm"
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Brian Kumanchik",
+                "hasEmail": "mailto:brian.kumanchik@jpl.nasa.gov"
+            },
+            "description": "The Solar Radiation and Climate Experiment (SORCE) is a NASA-sponsored satellite mission that is providing state-of-the-art measurements of incoming x-ray, ultraviolet, visible, near-infrared, and total solar radiation.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://nasa3d.arc.nasa.gov/shared_assets/models/sorce/SORCE-vFINAL.fbx.zip",
+                    "mediaType": "application/octet-stream"
+                }
             ],
+            "identifier": "NASA-406",
+            "issued": "2018-06-25",
             "keyword": [
                 "3d model",
                 "sorce",
@@ -1390155,66 +1390164,36 @@
                 "eyes on the solar system",
                 "spacecraft"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Brian Kumanchik",
-                "hasEmail": "mailto:brian.kumanchik@jpl.nasa.gov"
-            },
+            "landingPage": "http://nasa3d.arc.nasa.gov/detail/sorce",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:007"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "NASA-406",
-            "description": "The Solar Radiation and Climate Experiment (SORCE) is a NASA-sponsored satellite mission that is providing state-of-the-art measurements of incoming x-ray, ultraviolet, visible, near-infrared, and total solar radiation.",
-            "title": "NASA 3D Models: SORCE",
-            "programCode": [
-                "026:007"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://nasa3d.arc.nasa.gov/shared_assets/models/sorce/SORCE-vFINAL.fbx.zip",
-                    "mediaType": "application/octet-stream"
-                }
+            "references": [
+                "http://lasp.colorado.edu/sorce/index.htm"
             ],
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Space Science"
-            ]
+            ],
+            "title": "NASA 3D Models: SORCE"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1294627248-CDDIS.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/GSFC/SED/ESD/GGL/CDDIS.",
-            "issued": "2016-01-01",
-            "temporal": "1992-01-01T00:00:00Z/2022-01-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2016-08-12",
-            "keyword": [
-                "earth science",
-                "tectonics",
-                "solid earth",
-                "gravity/gravitational field",
-                "geodetics"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Carey Noll",
                 "hasEmail": "mailto:Carey.Noll@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GGL/CDDIS"
-            },
-            "identifier": "C1294627248-CDDIS",
             "description": "SLR Satellite Orbit solutions available from the Crustal Dynamics Data Information System (CDDIS). Precise Orbit Determination (POD) solutions in Standard Product 3 (SP3) format derived from analysis of Satellite Laser Ranging (SLR) data. These products are the generated by analysis centers in support of the International Laser Ranging Service (ILRS) and combined by the ILRS analysis coordinator to form the official ILRS orbit product (weekly), available approximately 5 days after the end of the solution week.",
-            "title": "Satellite Laser Ranging Satellite Orbit Product from NASA CDDIS",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -1390223,99 +1390202,134 @@
                     "title": "Download this dataset"
                 }
             ],
+            "identifier": "C1294627248-CDDIS",
+            "issued": "2016-01-01",
+            "keyword": [
+                "earth science",
+                "tectonics",
+                "solid earth",
+                "gravity/gravitational field",
+                "geodetics"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1294627248-CDDIS.html",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2016-08-12",
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
                 "ILRS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Satellite Laser Ranging Satellite Orbit Product from NASA CDDIS"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewBundle.jsp?identifier=urn%3Anasa%3Apds%3Agbo.ast-neo.whiteley.ecas-phot&version=1.0",
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
-                "none",
-                "multiple asteroids"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This data set includes the ECAS system (Eight Color Asteroid Survey) photometry and\ntaxonomic types of 77 Near Earth Objects published by R.J. Whiteley in his thesis\n(Whiteley, 2001.  A compositional and dynamical survey of the near-earth asteroids. \nPh.D. thesis, University of Hawaii), [WHITELEY2001] The ECAS system is established in\nZellner et al. 1985, Icarus 61, 355-416 [ZELLNERETAL1985].  The original ECAS survey\nis available in PDS as data set EAR-A-2CP-3-RDR-ECAS-V3.0.  The data presented here\nare new measurements based on the ECAS system.",
+            "identifier": "urn:nasa:pds:gbo.ast-neo.whiteley.ecas-phot",
+            "issued": "2021-05-21",
+            "keyword": [
+                "none",
+                "multiple asteroids"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewBundle.jsp?identifier=urn%3Anasa%3Apds%3Agbo.ast-neo.whiteley.ecas-phot&version=1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:gbo.ast-neo.whiteley.ecas-phot",
-            "description": "This data set includes the ECAS system (Eight Color Asteroid Survey) photometry and\ntaxonomic types of 77 Near Earth Objects published by R.J. Whiteley in his thesis\n(Whiteley, 2001.  A compositional and dynamical survey of the near-earth asteroids. \nPh.D. thesis, University of Hawaii), [WHITELEY2001] The ECAS system is established in\nZellner et al. 1985, Icarus 61, 355-416 [ZELLNERETAL1985].  The original ECAS survey\nis available in PDS as data set EAR-A-2CP-3-RDR-ECAS-V3.0.  The data presented here\nare new measurements based on the ECAS system.",
-            "title": "Whiteley NEO Photometry V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "Whiteley NEO Photometry V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C%2FCAL-ALICE-2-ESC2-V2.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This data set contains CODMAC Level 2 data acquired by the Rosetta Orbiter ALICE UV Spectrometer during the comet 67P/Churyumov-Gerasimenko Comet Escort 2 mission phase, which took place between 2015-03-11 and 2015-06-30.  The current V2.0 data set supersedes the previous V1.0 data set with improved documentation.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-cal-alice-2-esc2-v2.0",
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
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C%2FCAL-ALICE-2-ESC2-V2.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-cal-alice-2-esc2-v2.0",
-            "description": "This data set contains CODMAC Level 2 data acquired by the Rosetta Orbiter ALICE UV Spectrometer during the comet 67P/Churyumov-Gerasimenko Comet Escort 2 mission phase, which took place between 2015-03-11 and 2015-06-30.  The current V2.0 data set supersedes the previous V1.0 data set with improved documentation.",
-            "title": "ROSETTA-ORBITER 67P/CAL ALICE 2 ESC2 V2.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P/CAL ALICE 2 ESC2 V2.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.nasa.gov/d/t2xy-h9jv",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "GeneLab Outreach",
+                "hasEmail": "mailto:genelab-outreach@lists.nasa.gov"
+            },
+            "description": "Using a novel flood source construct we performed a direct comparison of genome-wide gene expression regulations resulting from exposure of primary human prostate fibroblast cultures to acute (10cGy and 200cGy) and longer-term chronic (1.0-2.45cGy cumulative over 24hr) exposures.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "GeneLab Study Page",
+                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-285",
+                    "mediaType": "text/html",
+                    "title": "Chronic low dose-rate versus acute ionizing radiation induced gene expression in primary derived prostate fibroblasts"
+                }
+            ],
+            "identifier": "nasa_genelab_GLDS-285_t2xy-h9jv",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
             "keyword": [
                 "absorbed radiation dose",
                 "scan protocol",
@@ -1390330,589 +1390344,556 @@
                 "ionizing radiation",
                 "sample treatment protocol"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "GeneLab Outreach",
-                "hasEmail": "mailto:genelab-outreach@lists.nasa.gov"
-            },
+            "landingPage": "https://data.nasa.gov/d/t2xy-h9jv",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "nasa_genelab_GLDS-285_t2xy-h9jv",
-            "description": "Using a novel flood source construct we performed a direct comparison of genome-wide gene expression regulations resulting from exposure of primary human prostate fibroblast cultures to acute (10cGy and 200cGy) and longer-term chronic (1.0-2.45cGy cumulative over 24hr) exposures.",
-            "title": "Chronic low dose-rate versus acute ionizing radiation induced gene expression in primary derived prostate fibroblasts",
-            "programCode": [
-                "026:005"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-285",
-                    "description": "GeneLab Study Page",
-                    "@type": "dcat:Distribution",
-                    "title": "Chronic low dose-rate versus acute ionizing radiation induced gene expression in primary derived prostate fibroblasts"
-                }
-            ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "Chronic low dose-rate versus acute ionizing radiation induced gene expression in primary derived prostate fibroblasts"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-X-HK-3-OCMRCS-V1.0",
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
+            "description": "This CODMAC level 3 data set contains the key parameters of the Orbit    Control Manouevres and the Thruster based Reaction Control Subsystem.    In particular, it provides information on the Orbit Control Manoeuvre    measured impulse, acceleration and disturbance torques. It also          provides Housekeeping data from the Thruster based Reaction Control      Subsystem covering areas such as # of on-cycles.                         It covers the period from launch in 2004, through the 3 Earth and        1 Mars flyby, plus the hibernation phases, plus the asteroid flybys      and finally covers the Prelanding, comet escort & Extension phases       of the prime target of the mission.                                      The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1).         This version V1.0 is the first version of this dataset.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-x-hk-3-ocmrcs-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-X-HK-3-OCMRCS-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-x-hk-3-ocmrcs-v1.0",
-            "description": "This CODMAC level 3 data set contains the key parameters of the Orbit    Control Manouevres and the Thruster based Reaction Control Subsystem.    In particular, it provides information on the Orbit Control Manoeuvre    measured impulse, acceleration and disturbance torques. It also          provides Housekeeping data from the Thruster based Reaction Control      Subsystem covering areas such as # of on-cycles.                         It covers the period from launch in 2004, through the 3 Earth and        1 Mars flyby, plus the hibernation phases, plus the asteroid flybys      and finally covers the Prelanding, comet escort & Extension phases       of the prime target of the mission.                                      The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1).         This version V1.0 is the first version of this dataset.",
-            "title": "ROSETTA ORBIT CONTROL MANOEUVRE                  \n                             ENGINEERING DATA",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA ORBIT CONTROL MANOEUVRE                  \n                             ENGINEERING DATA"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://c3.nasa.gov/dashlink/resources/919/",
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
-            "identifier": "DASHLINK_919",
             "description": "Ballscrew jam fault datasets (diagnostic and prognostic)",
-            "title": "2010_09_12 Jam 2 Lab",
-            "programCode": [
-                "026:029"
-            ],
             "distribution": [
                 {
-                    "mediaType": "application/x-zip-compressed",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/2010_09_12_Jam_2.zip",
-                    "description": "2010_09_12 Jam 2.zip",
                     "@type": "dcat:Distribution",
+                    "description": "2010_09_12 Jam 2.zip",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/2010_09_12_Jam_2.zip",
+                    "mediaType": "application/x-zip-compressed",
                     "title": "2010_09_12 Jam 2.zip"
                 }
             ],
-            "accrualPeriodicity": "irregular"
+            "identifier": "DASHLINK_919",
+            "issued": "2014-07-02",
+            "keyword": [
+                "nasa",
+                "dashlink",
+                "ames"
+            ],
+            "landingPage": "https://c3.nasa.gov/dashlink/resources/919/",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:029"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Dashlink"
+            },
+            "title": "2010_09_12 Jam 2 Lab"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-D-MIDAS-3-PRL-SAMPLES-V1.0",
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
+            "description": "The Micro-Imaging Dust Analysis System (MIDAS) is an instrument on the\nROSETTA Orbiter that will provide 3D images and statistical parameters\nof pristine cometary particles hitting the detector. This data set\nincludes all data from the PRELANDING mission phase.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-d-midas-3-prl-samples-v1.0_t2zq-43ei",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-D-MIDAS-3-PRL-SAMPLES-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-d-midas-3-prl-samples-v1.0_t2zq-43ei",
-            "description": "The Micro-Imaging Dust Analysis System (MIDAS) is an instrument on the\nROSETTA Orbiter that will provide 3D images and statistical parameters\nof pristine cometary particles hitting the detector. This data set\nincludes all data from the PRELANDING mission phase.",
-            "title": "ROSETTA-ORBITER DUST MIDAS 3 PRL SAMPLES V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER DUST MIDAS 3 PRL SAMPLES V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=GRAIL-L-SPICE-6-V1.0",
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
-                "gravity recovery and interior laboratory"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This data set includes the complete set of GRAIL SPICE data files (``kernel files''), which can be accessed using SPICE software. The SPICE data contain geometric and other ancillary information needed to recover the full value of science instrument data. In particular SPICE kernels provide spacecraft and planetary ephemerides, instrument mounting alignments, spacecraft orientation, and data needed for relevant time conversions.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.grail-l-spice-6-v1.0_t32p-jkp8",
+            "issued": "2021-05-21",
+            "keyword": [
+                "moon",
+                "gravity recovery and interior laboratory"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=GRAIL-L-SPICE-6-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.grail-l-spice-6-v1.0_t32p-jkp8",
-            "description": "This data set includes the complete set of GRAIL SPICE data files (``kernel files''), which can be accessed using SPICE software. The SPICE data contain geometric and other ancillary information needed to recover the full value of science instrument data. In particular SPICE kernels provide spacecraft and planetary ephemerides, instrument mounting alignments, spacecraft orientation, and data needed for relevant time conversions.",
-            "title": "GRAIL SPICE KERNELS V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "GRAIL SPICE KERNELS V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/MODIS/MOD14A1.061",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Louis Giglio, Christopher Justice. 2021-02-11. MODIS/Terra Thermal Anomalies/Fire Daily L3 Global 1km SIN Grid V061. Sioux Falls, South Dakota, USA. Archived by National Aeronautics and Space Administration, U.S. Government, NASA EOSDIS Land Processes Distributed Active Archive Center. https://doi.org/10.5067/MODIS/MOD14A1.061. https://doi.org/10.5067/MODIS/MOD14A1.061. The DOI landing page provides citations in APA and Chicago styles..",
-            "issued": "2021-02-11",
-            "temporal": "2000-02-18T00:00:00Z/2024-05-27T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2021-02-11",
-            "keyword": [
-                "biosphere",
-                "national geospatial data asset",
-                "surface thermal properties",
-                "ngda",
-                "earth science",
-                "land surface",
-                "ecological dynamics"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Louis Giglio",
                 "hasEmail": "mailto:lgiglio@umd.edu"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "LP DAAC"
-            },
-            "identifier": "C2565791013-LPCLOUD",
-            "description": "The Terra Moderate Resolution Imaging Spectroradiometer (MODIS) Thermal Anomalies and Fire Daily (MOD14A1) Version 6.1 data are generated every eight days at 1 kilometer (km) spatial resolution as a Level 3 product. MOD14A1 contains eight consecutive days of fire data conveniently packaged into a single file.\n\nThe Science Dataset (SDS) layers include the fire mask, pixel quality indicators, maximum fire radiative power (MaxFRP), and the position of the fire pixel within the scan. Each layer consists of daily per pixel information for each of the eight days of data acquisition.  \n\nValidation at stage 3 (https://modis-land.gsfc.nasa.gov/MODLAND_val.html) has been achieved for all MODIS Thermal Anomalies and Fire products. Further details regarding MODIS land product validation for the MOD14 data product is available from the MODIS land team validation site (https://modis-land.gsfc.nasa.gov/ValStatus.php?ProductID=MOD14).\n\n Improvements/Changes from Previous Versions\n\n* The Version 6.1 Level-1B (L1B) products have been improved by undergoing various calibration changes that include: changes to the response-versus-scan angle (RVS) approach that affects reflectance bands for Aqua and Terra MODIS, corrections to adjust for the optical crosstalk in Terra MODIS infrared (IR) bands, and corrections to the Terra MODIS forward look-up table (LUT) update for the period 2012 - 2017.\n* A polarization correction has been applied to the L1B Reflective Solar Bands (RSB).",
-            "release-place": "Sioux Falls, South Dakota, USA",
-            "graphic-preview-description": "Browse image for Earthdata Search",
             "creator": "Louis Giglio, Christopher Justice",
-            "title": "MODIS/Terra Thermal Anomalies/Fire Daily L3 Global 1km SIN Grid V061",
-            "graphic-preview-file": "https://cmr.earthdata.nasa.gov/browse-scaler/browse_images/granules/G2622745074-LPCLOUD?h=85&w=85",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The Terra Moderate Resolution Imaging Spectroradiometer (MODIS) Thermal Anomalies and Fire Daily (MOD14A1) Version 6.1 data are generated every eight days at 1 kilometer (km) spatial resolution as a Level 3 product. MOD14A1 contains eight consecutive days of fire data conveniently packaged into a single file.\n\nThe Science Dataset (SDS) layers include the fire mask, pixel quality indicators, maximum fire radiative power (MaxFRP), and the position of the fire pixel within the scan. Each layer consists of daily per pixel information for each of the eight days of data acquisition.  \n\nValidation at stage 3 (https://modis-land.gsfc.nasa.gov/MODLAND_val.html) has been achieved for all MODIS Thermal Anomalies and Fire products. Further details regarding MODIS land product validation for the MOD14 data product is available from the MODIS land team validation site (https://modis-land.gsfc.nasa.gov/ValStatus.php?ProductID=MOD14).\n\n Improvements/Changes from Previous Versions\n\n* The Version 6.1 Level-1B (L1B) products have been improved by undergoing various calibration changes that include: changes to the response-versus-scan angle (RVS) approach that affects reflectance bands for Aqua and Terra MODIS, corrections to adjust for the optical crosstalk in Terra MODIS infrared (IR) bands, and corrections to the Terra MODIS forward look-up table (LUT) update for the period 2012 - 2017.\n* A polarization correction has been applied to the L1B Reflective Solar Bands (RSB).",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMODIS%2FMOD14A1.061",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMODIS%2FMOD14A1.061",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "application/x-hdf",
-                    "downloadURL": "https://e4ftl01.cr.usgs.gov/MOLT/MOD14A1.061/",
-                    "description": "LP DAAC Data Pool provides direct access to available products via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "LP DAAC Data Pool provides direct access to available products via HTTPS.",
+                    "downloadURL": "https://e4ftl01.cr.usgs.gov/MOLT/MOD14A1.061/",
+                    "mediaType": "application/x-hdf",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "application/x-hdf",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=C2565791013-LPCLOUD",
-                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=C2565791013-LPCLOUD",
+                    "mediaType": "application/x-hdf",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/MODIS/MOD14A1.061",
-                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
+                    "downloadURL": "https://doi.org/10.5067/MODIS/MOD14A1.061",
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
-                    "downloadURL": "https://lpdaac.usgs.gov/documents/1005/MOD14_User_Guide_V61.pdf",
-                    "description": "The technical information in the User's Guide enables users to interpret and use the data products.",
                     "@type": "dcat:Distribution",
+                    "description": "The technical information in the User's Guide enables users to interpret and use the data products.",
+                    "downloadURL": "https://lpdaac.usgs.gov/documents/1005/MOD14_User_Guide_V61.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://lpdaac.usgs.gov/documents/87/MOD14_ATBD.pdf",
-                    "description": "The ATBD provides physical theory and mathematical procedures for the calculations used to produce the data products.",
                     "@type": "dcat:Distribution",
+                    "description": "The ATBD provides physical theory and mathematical procedures for the calculations used to produce the data products.",
+                    "downloadURL": "https://lpdaac.usgs.gov/documents/87/MOD14_ATBD.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's algorithm theoretical basis document"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/filespec/MODIS/61/MOD14A1",
-                    "description": "The File Specification provides a description of the product file including Scientific Data Sets and their attributes.",
                     "@type": "dcat:Distribution",
+                    "description": "The File Specification provides a description of the product file including Scientific Data Sets and their attributes.",
+                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/filespec/MODIS/61/MOD14A1",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://modis-land.gsfc.nasa.gov/MODLAND_val.html",
-                    "description": "Validation at stage 3 has been achieved for the MODIS Thermal Anomalies and Fire products.",
                     "@type": "dcat:Distribution",
+                    "description": "Validation at stage 3 has been achieved for the MODIS Thermal Anomalies and Fire products.",
+                    "downloadURL": "https://modis-land.gsfc.nasa.gov/MODLAND_val.html",
+                    "mediaType": "text/html",
                     "title": "View this dataset's science data product validation documentation"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://modis-land.gsfc.nasa.gov/ValStatus.php?ProductID=MOD14",
-                    "description": "Further details regarding MODIS land product validation for the MOD14 data product is available from the MODIS Land Team Validation site.",
                     "@type": "dcat:Distribution",
+                    "description": "Further details regarding MODIS land product validation for the MOD14 data product is available from the MODIS Land Team Validation site.",
+                    "downloadURL": "https://modis-land.gsfc.nasa.gov/ValStatus.php?ProductID=MOD14",
+                    "mediaType": "text/html",
                     "title": "View this dataset's science data product validation documentation"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://opendap.cr.usgs.gov/opendap/hyrax/DP131/MOLT/MOD14A1.061/contents.html",
-                    "description": "Access data via Open-source Project for a Network Data Access Protocol",
                     "@type": "dcat:Distribution",
+                    "description": "Access data via Open-source Project for a Network Data Access Protocol",
+                    "downloadURL": "https://opendap.cr.usgs.gov/opendap/hyrax/DP131/MOLT/MOD14A1.061/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/browse-scaler/browse_images/granules/G2622745074-LPCLOUD?h=85&w=85",
-                    "description": "Browse image for Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse image for Earthdata Search",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/browse-scaler/browse_images/granules/G2622745074-LPCLOUD?h=85&w=85",
+                    "mediaType": "text/html",
                     "title": "Get a related visualization"
                 }
             ],
+            "graphic-preview-description": "Browse image for Earthdata Search",
+            "graphic-preview-file": "https://cmr.earthdata.nasa.gov/browse-scaler/browse_images/granules/G2622745074-LPCLOUD?h=85&w=85",
+            "identifier": "C2565791013-LPCLOUD",
+            "issued": "2021-02-11",
+            "keyword": [
+                "biosphere",
+                "national geospatial data asset",
+                "surface thermal properties",
+                "ngda",
+                "earth science",
+                "land surface",
+                "ecological dynamics"
+            ],
+            "landingPage": "https://doi.org/10.5067/MODIS/MOD14A1.061",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2021-02-11",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "LP DAAC"
+            },
+            "release-place": "Sioux Falls, South Dakota, USA",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2000-02-18T00:00:00Z/2024-05-27T00:00:00Z",
             "theme": [
                 "Terra",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "MODIS/Terra Thermal Anomalies/Fire Daily L3 Global 1km SIN Grid V061"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "issue-identification": "GSSTF_F14_2c",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/MEASURES/GSSTF/DATA325",
             "citation": "Shie, C.-L., K. Hilburn, L. S. Chiu, R. Adler, I-I Lin, E. Nelkin, and J. Ardizzone. Andrey Savtchenko. 2011-11-18. GSSTF_F14. Version 2c. Goddard Satellite-Based Surface Turbulent Fluxes, 1x1 deg Daily Grid, Satellite F14 V2c. Greenbelt, MD, USA. GSSTF_F14_2c. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/MEASURES/GSSTF/DATA325. https://disc.gsfc.nasa.gov/datacollection/GSSTF_F14_2c.html. Digital Science Data.",
-            "issued": "2011-11-18",
-            "temporal": "1997-05-08T00:00:00Z/2008-08-08T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2011-11-18",
-            "keyword": [
-                "ocean heat budget",
-                "atmospheric temperature",
-                "ocean pressure",
-                "earth science",
-                "atmospheric radiation",
-                "atmospheric pressure",
-                "atmosphere",
-                "ocean winds",
-                "atmospheric water vapor",
-                "ocean temperature",
-                "oceans",
-                "atmospheric winds"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "DAVID SILBERSTEIN",
                 "hasEmail": "mailto:david.s.silberstein@nasa.gov"
             },
+            "creator": "Shie, C.-L., K. Hilburn, L. S. Chiu, R. Adler, I-I Lin, E. Nelkin, and J. Ardizzone",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C1237113407-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "These data are part of the Goddard Satellite-based Surface Turbulent Fluxes Version-2c (GSSTF 2c) Dataset recently produced through a MEaSURES funded project led by Dr. Chung-Lin Shie (UMBC/GEST, NASA/GSFC), converted to HDF-EOS5 format. The stewardship of this HDF-EOS5 dataset is part of the MEaSUREs project. \n\nThis is a Daily (24-hour) product; data are projected to equidistant Grid that covers the globe at 1x1 degree cell size, resulting in data arrays of 360x180 size.  A finer resolution, 0.25 deg,  of this product has been released as Version 3. \n\nThe daily fluxes  are produced for each individual available SSM/I satellite tapes (e.g., F08, F10, F11, F13, F14 and F15), and then serve as input to the Combined daily fluxes (GSSTF_2c).\n      \nThe short name for this data set is GSSTF_F14.",
-            "editor": "Andrey Savtchenko",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "GSSTF_F14",
-            "creator": "Shie, C.-L., K. Hilburn, L. S. Chiu, R. Adler, I-I Lin, E. Nelkin, and J. Ardizzone",
-            "graphic-preview-description": "Goddard Satellite-based Surface Turbulent Fluxes (GSSTF)  Satellite F14 Total Precipitable Water 1 x 1 degree 01/01/2001 [g/cm2]",
-            "title": "Goddard Satellite-Based Surface Turbulent Fluxes, 1x1 deg Daily Grid, Satellite F14 V2c (GSSTF_F14) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/GSSTF_F14_2c.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMEASURES%2FGSSTF%2FDATA325",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMEASURES%2FGSSTF%2FDATA325",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/GSSTF_F14_2c.png",
-                    "description": "Goddard Satellite-based Surface Turbulent Fluxes (GSSTF)  Satellite F14 Total Precipitable Water 1 x 1 degree 01/01/2001 [g/cm2]\n      ",
                     "@type": "dcat:Distribution",
+                    "description": "Goddard Satellite-based Surface Turbulent Fluxes (GSSTF)  Satellite F14 Total Precipitable Water 1 x 1 degree 01/01/2001 [g/cm2]\n      ",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/GSSTF_F14_2c.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/GSSTF_F14_2c.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/GSSTF_F14_2c.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://measures.gesdisc.eosdis.nasa.gov/data/GSSTF/GSSTF_F14.2c/",
-                    "description": "Access the data via HTTP.\n   ",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTP.\n   ",
+                    "downloadURL": "https://measures.gesdisc.eosdis.nasa.gov/data/GSSTF/GSSTF_F14.2c/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://measures.gesdisc.eosdis.nasa.gov/data/GSSTF/GSSTF_F14.2c/doc/Readme.GSSTF2c.pdf",
-                    "description": "README Document\n   ",
                     "@type": "dcat:Distribution",
+                    "description": "README Document\n   ",
+                    "downloadURL": "https://measures.gesdisc.eosdis.nasa.gov/data/GSSTF/GSSTF_F14.2c/doc/Readme.GSSTF2c.pdf",
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
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=GSSTF_F14_2c",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=GSSTF_F14_2c",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://measures.gesdisc.eosdis.nasa.gov/opendap/GSSTF/GSSTF_F14.2c",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://measures.gesdisc.eosdis.nasa.gov/opendap/GSSTF/GSSTF_F14.2c",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 }
             ],
+            "editor": "Andrey Savtchenko",
+            "graphic-preview-description": "Goddard Satellite-based Surface Turbulent Fluxes (GSSTF)  Satellite F14 Total Precipitable Water 1 x 1 degree 01/01/2001 [g/cm2]",
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/GSSTF_F14_2c.png",
+            "identifier": "C1237113407-GES_DISC",
+            "issue-identification": "GSSTF_F14_2c",
+            "issued": "2011-11-18",
+            "keyword": [
+                "ocean heat budget",
+                "atmospheric temperature",
+                "ocean pressure",
+                "earth science",
+                "atmospheric radiation",
+                "atmospheric pressure",
+                "atmosphere",
+                "ocean winds",
+                "atmospheric water vapor",
+                "ocean temperature",
+                "oceans",
+                "atmospheric winds"
+            ],
+            "landingPage": "https://doi.org/10.5067/MEASURES/GSSTF/DATA325",
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
+            "series-name": "GSSTF_F14",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "1997-05-08T00:00:00Z/2008-08-08T23:59:59.999Z",
             "theme": [
                 "MEaSUREs",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Goddard Satellite-Based Surface Turbulent Fluxes, 1x1 deg Daily Grid, Satellite F14 V2c (GSSTF_F14) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=CO-S-RSS-1-SROC24-V1.0",
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
+            "description": "The Cassini Radio Science Saturn Ring and Atmospheric Occultation experiments (SROC24) Raw Data Archive is a time-ordered collection of radio science raw data acquired on January 2, 10, 17, and on March 22, 2017, during the Cassini Extended Extended Mission.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.co-s-rss-1-sroc24-v1.0_t385-wkf3",
+            "issued": "2021-05-21",
+            "keyword": [
+                "saturn",
+                "cassini-huygens"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=CO-S-RSS-1-SROC24-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.co-s-rss-1-sroc24-v1.0_t385-wkf3",
-            "description": "The Cassini Radio Science Saturn Ring and Atmospheric Occultation experiments (SROC24) Raw Data Archive is a time-ordered collection of radio science raw data acquired on January 2, 10, 17, and on March 22, 2017, during the Cassini Extended Extended Mission.",
-            "title": "CASSINI RSS RAW DATA SET - SROC24 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "CASSINI RSS RAW DATA SET - SROC24 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1615905769-OB_DAAC.html",
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
-                "national geospatial data asset",
-                "ngda",
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
-            "identifier": "C1615905769-OB_DAAC",
             "description": "MODIS (or Moderate Resolution Imaging Spectroradiometer) is a key instrument aboard the Terra (EOS AM) and Aqua (EOS PM) satellites. Terra's orbit around the Earth is timed so that it passes from north to south across the equator in the morning, while Aqua passes south to north over the equator in the afternoon. Terra MODIS and Aqua MODIS are viewing the entire Earth's surface every 1 to 2 days, acquiring data in 36 spectral bands, or groups of wavelengths (see MODIS Technical Specifications). These data will improve our understanding of global dynamics and processes occurring on the land, in the oceans, and in the lower atmosphere. MODIS is playing a vital role in the development of validated, global, interactive Earth system models able to predict global change accurately enough to assist policy makers in making sound decisions concerning the protection of our environment.",
-            "title": "Aqua MODIS Global Binned 11\u00b5m Daytime Sea Surface Temperature (SST) Data, version R2019.0",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://oceandata.sci.gsfc.nasa.gov/directaccess/MODIS-Aqua/L3BIN/",
-                    "description": "NASA Ocean Color Web - Data Distribution Site",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Ocean Color Web - Data Distribution Site",
+                    "downloadURL": "https://oceandata.sci.gsfc.nasa.gov/directaccess/MODIS-Aqua/L3BIN/",
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
-                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/data/10.5067/AQUA/MODIS/L3B/SST/R2019.0",
-                    "description": "MODIS-Aqua L3B 11\u00b5m Daytime Sea Surface Temperature (SST) Dataset Landing Page",
                     "@type": "dcat:Distribution",
+                    "description": "MODIS-Aqua L3B 11\u00b5m Daytime Sea Surface Temperature (SST) Dataset Landing Page",
+                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/data/10.5067/AQUA/MODIS/L3B/SST/R2019.0",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 }
             ],
+            "identifier": "C1615905769-OB_DAAC",
+            "issued": "2019-06-23",
+            "keyword": [
+                "earth science",
+                "national geospatial data asset",
+                "ngda",
+                "oceans",
+                "ocean temperature"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1615905769-OB_DAAC.html",
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
+            "title": "Aqua MODIS Global Binned 11\u00b5m Daytime Sea Surface Temperature (SST) Data, version R2019.0"
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
-                "rss",
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
-            "identifier": "NASA-760",
             "description": "RSS",
-            "title": "PDS Odyssey Radio Science Data (41)",
-            "programCode": [
-                "026:005"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -1390920,54 +1390901,44 @@
                     "mediaType": "application/html"
                 }
             ],
-            "accrualPeriodicity": "irregular",
+            "identifier": "NASA-760",
+            "issued": "2018-06-25",
+            "keyword": [
+                "rss",
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
+            "title": "PDS Odyssey Radio Science Data (41)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "issue-identification": "MAC03S0",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1236350906-GES_DISC.html",
             "citation": "MODIS Science Team. GES DISC. 2006-10-01. MAC03S0. Version 002. MODIS/Aqua Geolocation Fields 1km 5-Min 1A Narrow Swath Subset along CloudSat. Greenbelt, MD, USA. MAC03S0. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://disc.gsfc.nasa.gov/datacollection/MAC03S0_002.html. Digital Science Data.",
-            "issued": "2006-06-02",
-            "temporal": "2006-06-02T00:00:00Z/2018-03-01T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2018-03-01",
-            "keyword": [
-                "earth science",
-                "ngda",
-                "land surface",
-                "sensor characteristics",
-                "spectral/engineering",
-                "topography",
-                "national geospatial data asset",
-                "platform characteristics"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "ANDREY SAVTCHENKO",
                 "hasEmail": "mailto:Andrey.Savtchenko@nasa.gov"
             },
+            "creator": "MODIS Science Team",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C1236350906-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "This is the narrow-swath MODIS/Aqua subset along CloudSat field of view track. The goal of the narrow-swath subset is to select and return MODIS data that are within +-5 km across the CloudSat track. I.e. the resultant MODIS subset swath is about 10 km cross-track. Thus, MAC03S0 cross-track width is 11 pixels. Along-track, all MODIS pixels from the original product are preserved.\n      \nIn the standard product, geolocation fields are calculated for each 1 km MODIS Instantaneous Field of Views (IFOV) for all orbits daily. The locations and ancillary information corresponds to the intersection of the centers of each IFOV from 10 detectors in an ideal 1 km band on the Earth's surface. A digital terrain model is used to model the Earth's surface. The main inputs are the spacecraft attitude and orbit, the instrument telemetry and the digital elevation model. The geolocation fields include geodetic Latitude, Longitude, surface height above geoid, solar zenith and azimuth angles, satellite zenith and azimuth angles, and a land/sea mask for each 1 km sample. Additional information is included in the header to enable the calculation of the approximate location of the center of the detectors of any of the 36 MODIS bands. This product is used as input by a large number of subsequent MODIS products, particularly the products produced by the Land team. \n      \n(The shortname for this product is MAC03S0).",
-            "editor": "GES DISC",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "MAC03S0",
-            "creator": "MODIS Science Team",
-            "title": "MODIS/Aqua Geolocation Fields 1km 5-Min 1A Narrow Swath Subset along CloudSat V002 (MAC03S0) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/MAC03S0_002.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -1390976,1420 +1390947,1463 @@
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/MAC03S0_002.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/MAC03S0_002.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://atrain.gesdisc.eosdis.nasa.gov/data/MAC/MAC03S0.002/",
-                    "description": "Access the data via HTTPS",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS",
+                    "downloadURL": "https://atrain.gesdisc.eosdis.nasa.gov/data/MAC/MAC03S0.002/",
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
-                    "description": "Quality Assurance for the original product.",
                     "@type": "dcat:Distribution",
+                    "description": "Quality Assurance for the original product.",
+                    "downloadURL": "https://modaps.nascom.nasa.gov/services/qa/science.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "editor": "GES DISC",
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/MAC03S0_002.png",
+            "identifier": "C1236350906-GES_DISC",
+            "issue-identification": "MAC03S0",
+            "issued": "2006-06-02",
+            "keyword": [
+                "earth science",
+                "ngda",
+                "land surface",
+                "sensor characteristics",
+                "spectral/engineering",
+                "topography",
+                "national geospatial data asset",
+                "platform characteristics"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1236350906-GES_DISC.html",
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
+            "series-name": "MAC03S0",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2006-06-02T00:00:00Z/2018-03-01T23:59:59.999Z",
             "theme": [
                 "ATDD",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "MODIS/Aqua Geolocation Fields 1km 5-Min 1A Narrow Swath Subset along CloudSat V002 (MAC03S0) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-X-SREM-2-EXT1-MTP027-V1.0",
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
+            "description": "This data set contains count rates (1/s) as measured by the Standard Radiation Environment Monitor (SREM) instrument on the Rosetta spacecraft, along with their standard deviations.  The primary target is comet 67P/Churyumov-Gerasimenko. These are CODMAC Level 2 Experiment Data Record data, and provide a measure of the radiation in the spacecraft environment during the Medium Term Plan 27 period of the EXTENSION 1 mission phase.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-x-srem-2-ext1-mtp027-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-X-SREM-2-EXT1-MTP027-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-x-srem-2-ext1-mtp027-v1.0",
-            "description": "This data set contains count rates (1/s) as measured by the Standard Radiation Environment Monitor (SREM) instrument on the Rosetta spacecraft, along with their standard deviations.  The primary target is comet 67P/Churyumov-Gerasimenko. These are CODMAC Level 2 Experiment Data Record data, and provide a measure of the radiation in the spacecraft environment during the Medium Term Plan 27 period of the EXTENSION 1 mission phase.",
-            "title": "ROSETTA-ORBITER 67P SREM 2 EXTENSION 1\n    MTP027 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P SREM 2 EXTENSION 1\n    MTP027 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ATLAS/ATL07.006",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "ATLAS/ICESat-2 L3A Sea Ice Height V006. Version 006. Archived by National Aeronautics and Space Administration, U.S. Government, NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/ATLAS/ATL07.006.",
-            "issued": "2018-10-14",
-            "temporal": "2018-10-14T00:00:00Z/2025-01-27T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-07",
-            "keyword": [
-                "sea ice",
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
-            "identifier": "C2713030505-NSIDC_CPRD",
             "description": "The data set (ATL07) contains along-track heights for sea ice and open water leads (at varying length scales) relative to the WGS84 ellipsoid (ITRF2014 reference frame) after adjustment for geoidal and tidal variations, and inverted barometer effects. Height statistics and apparent reflectance are also provided. The data were acquired by the Advanced Topographic Laser Altimeter System (ATLAS) instrument on board the Ice, Cloud and land Elevation Satellite-2 (ICESat-2) observatory.",
-            "title": "ATLAS/ICESat-2 L3A Sea Ice Height V006",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FATLAS%2FATL07.006",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FATLAS%2FATL07.006",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=ATL07+V006",
-                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=ATL07+V006",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2713030505-NSIDC_CPRD",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2713030505-NSIDC_CPRD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/ATLAS/ATL07.006",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/ATLAS/ATL07.006",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/ATLAS/ATL07.006",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/ATLAS/ATL07.006",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C2713030505-NSIDC_CPRD",
+            "issued": "2018-10-14",
+            "keyword": [
+                "sea ice",
+                "cryosphere",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/ATLAS/ATL07.006",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2024-11-07",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA NSIDC DAAC"
+            },
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2018-10-14T00:00:00Z/2025-01-27T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "ATLAS/ICESat-2 L3A Sea Ice Height V006"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-2-ESC2-67PCHURYUMOV-M16-V1.0",
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
+            "description": "This data set contains raw EDR images acquired by the OSIRIS Wide Angle\nCamera during the escort phase of the Rosetta mission at the comet 67P,\ncovering the period from 2015-05-05 to 2015-06-02.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-2-esc2-67pchuryumov-m16-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-2-ESC2-67PCHURYUMOV-M16-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-2-esc2-67pchuryumov-m16-v1.0",
-            "description": "This data set contains raw EDR images acquired by the OSIRIS Wide Angle\nCamera during the escort phase of the Rosetta mission at the comet 67P,\ncovering the period from 2015-05-05 to 2015-06-02.",
-            "title": "ROSETTA-ORBITER COMET ESCORT OSIWAC 2 EDR MTP 016 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER COMET ESCORT OSIWAC 2 EDR MTP 016 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/TOGACOARE/AMPR/DATA101",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Petersen, Walter A and Timothy  Lang.1993. AMPR BRIGHTNESS TEMPERATURE (TB) TOGA COARE [indicate subset used]. Dataset available online from the NASA Global Hydrometeorology Resource Center DAAC, Huntsville, Alabama, U.S.A. DOI: http://dx.doi.org/10.5067/TOGACOARE/AMPR/DATA101",
-            "issued": "1993-01-11",
-            "temporal": "1993-01-12T21:32:01Z/1993-02-25T03:13:58Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-04-28",
-            "keyword": [
-                "microwave",
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
-            "identifier": "C1979080426-GHRC_DAAC",
             "description": "The Advanced Microwave Precipitation Radiometer (AMPR) data set was part of the atmospheric measurements collected during the intensive observation period of the Tropical Ocean Global Atmosphere-Coupled Ocean Atmosphere Response Experiment (TOGA COARE). AMPR brightness temperature data were collected at a combination of frequencies (10.7, 19.35, 37.1, and 85.5 GHz) and for the period Jan. 12, 1993 - Feb. 25, 1993. The TOGA COARE geographic domain pertinent to the AMPR data set was from the equator to 21 S latitude and 145 E - 161 E longitude.",
-            "graphic-preview-description": "N/A",
-            "title": "AMPR BRIGHTNESS TEMPERATURE (TB) TOGA COARE V2",
-            "graphic-preview-file": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/ampr/toga_coare/browse/",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FTOGACOARE%2FAMPR%2FDATA101",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FTOGACOARE%2FAMPR%2FDATA101",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=amprtbtc",
-                    "description": "Files may be downloaded directly to your workstation from this link",
                     "@type": "dcat:Distribution",
+                    "description": "Files may be downloaded directly to your workstation from this link",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=amprtbtc",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "image/gif",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/ampr/toga_coare/browse/ampr_TOGA_COARE_f104A_1993.026_v2.gif",
-                    "description": "Sample browse image",
                     "@type": "dcat:Distribution",
+                    "description": "Sample browse image",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/ampr/toga_coare/browse/ampr_TOGA_COARE_f104A_1993.026_v2.gif",
+                    "mediaType": "image/gif",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "image/gif",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/ampr/toga_coare/browse/ampr_TOGA_COARE_f109_1993.039_v2.gif",
-                    "description": "Sample browse image",
                     "@type": "dcat:Distribution",
+                    "description": "Sample browse image",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/ampr/toga_coare/browse/ampr_TOGA_COARE_f109_1993.039_v2.gif",
+                    "mediaType": "image/gif",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://ghrc.nsstc.nasa.gov/uso/ds_docs/ampr/ampr_dataset.html",
-                    "description": "The guide document contains detailed information about the dataset",
                     "@type": "dcat:Distribution",
+                    "description": "The guide document contains detailed information about the dataset",
+                    "downloadURL": "http://ghrc.nsstc.nasa.gov/uso/ds_docs/ampr/ampr_dataset.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/doc/ampr/ampr.pdf",
-                    "description": "Brief Instrument Description of the Advanced Microwave Precipitation Radiometer (AMPR)",
                     "@type": "dcat:Distribution",
+                    "description": "Brief Instrument Description of the Advanced Microwave Precipitation Radiometer (AMPR)",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/doc/ampr/ampr.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View the primary investigator's documentation for this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/doc/ampr/example_ampr_read_program.f",
-                    "description": "Example program to read AMPR data from a text file into arrays",
                     "@type": "dcat:Distribution",
+                    "description": "Example program to read AMPR data from a text file into arrays",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/doc/ampr/example_ampr_read_program.f",
+                    "mediaType": "text/html",
                     "title": "Downloadable software applications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://weather.msfc.nasa.gov/ampr/",
-                    "description": "The home page for the project or program which sponsored the dataset",
                     "@type": "dcat:Distribution",
+                    "description": "The home page for the project or program which sponsored the dataset",
+                    "downloadURL": "https://weather.msfc.nasa.gov/ampr/",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/ampr/toga_coare/browse/",
-                    "description": "N/A",
                     "@type": "dcat:Distribution",
+                    "description": "N/A",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/ampr/toga_coare/browse/",
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
+            "graphic-preview-file": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/ampr/toga_coare/browse/",
+            "identifier": "C1979080426-GHRC_DAAC",
+            "issued": "1993-01-11",
+            "keyword": [
+                "microwave",
+                "spectral/engineering",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/TOGACOARE/AMPR/DATA101",
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
             "spatial": "144.774 -21.3571 160.679 0.22934",
+            "temporal": "1993-01-12T21:32:01Z/1993-02-25T03:13:58Z",
             "theme": [
                 "TOGA COARE",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "AMPR BRIGHTNESS TEMPERATURE (TB) TOGA COARE V2"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://c3.nasa.gov/dashlink/resources/331/",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2011-03-25",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
-            "keyword": [
-                "ames",
-                "nasa",
-                "dashlink"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Kamalika Das",
                 "hasEmail": "mailto:kamalika.das@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Dashlink"
-            },
-            "identifier": "DASHLINK_331",
             "description": "**Citation**:\r\n#######################\r\nIf using this dataset please cite the following in your work:\r\n\r\n@misc{VotDasNemSri2010 ,\r\nauthor = \"Petr Votava and Kamalika Das and Rama Nemani and Ashok N. Srivastava\",\r\nyear = \"2010\",\r\ntitle = \"MODIS surface reflectance data repository\",\r\nurl = \"https://c3.ndc.nasa.gov/dashlink/resources/331/\",\r\ninstitution = \"NASA Ames Research Center\" }\r\n\r\nPetr Votava, Kamalika Das, Rama Nemani, Ashok N. Srivastava. (2010). MODIS surface reflectance data repository. NASA Ames Research Center. \r\n\r\n**Data Description:**\r\n####################\r\n\r\nThe California satellite dataset using the MODerate-resolution Imaging Spectroradiometer (MODIS) product MCD43A4 provides reflectance data adjusted using a bidirectional reflectance distribution function (BRDF) to model the values as if they were taken from nadir view.\r\n\r\nBoth Terra and Aqua data are used in the generation of this product, providing the highest probability for \r\nquality input data.\r\n\r\nMore information at: \r\nhttps://lpdaac.usgs.gov/lpdaac/products/modis_products_table/nadir_brdf_adjusted_reflectance/16_day_l3_global_500m/v5/combined\r\n\r\n\r\n**Data Organization:**\r\n####################\r\n\r\nThe nine data folders correspond to three years of data.Under this top level directory structure are separate files for each band (1 - 7) and each 8-day period of the particular year. Within the period the best observations were selected for each location.\r\n\r\n\r\n**File Naming Conventions:**\r\n###########################\r\n\r\nEach of the files represent a 2D dataset with the naming conventions as follows:\r\n\r\nMCD43A4.CA_1KM.005.<YYYYDDD>. <BAND>.flt32\r\n\r\nwhere \r\n   <YYYYDDD> is the beginning year-day of the period that where YYYY = year and DDD = day of year (001 - 366)\r\n\r\n   <BAND> represents the observations in particular (spectral) band (band 1 - band 7) - since the indexing is 0-based,\r\n    the range of indexes on the files is from 0 - 6 (where 0 = band 1, and 6 = band 7)\r\n\r\nThe spectral band frequencies for the MODIS acquisitions are as follows:\r\n   BAND1\t620 - 670 nm\r\n   BAND2\t841 - 876 nm \r\n   BAND3 \t459 - 479 nm\r\n   BAND4 \t545 - 565 nm\r\n   BAND5\t1230 - 1250 nm\r\n   BAND6 \t1628 - 1652 nm\r\n   BAND7 \t2105 - 2155 nm\r\n\r\n\r\n**File Specifications:**\r\n######################\r\nEach file is a single 2D dataset.\r\n\r\nDATA TYPE: 32-bit floating point (IEEE754) with little-Endian byte ordering\r\nNUMBER OF ROWS: 1203\r\nNUMBER OF COLUMNS: 738\r\nFILL VALUES (observations that are either not valid or not on land, such as ocean etc.): -999.0       \r\n\r\n\r\n**Overview:**\r\n###########\r\n\r\nDATASET: MODIS 8-day Surface Reflectance BRDF-adjusted from Terra and Aqua\r\n\r\nCOLLECTION: 5\r\n\r\nDATA TYPE: IEEE754 float (32-bit float)\r\n\r\nBYTE ORDER: LITTLE ENDIAN (Intel)\r\n\r\nDIMS: 1203 rows x 738 columns\r\n\r\nFILL VALUE: -999.0\r\n\r\nSPATIAL RESOLUTION: 1km\r\n\r\nPROJECTION: Lambert Azimuthal Equal Area",
-            "title": "California Satellite Data",
-            "programCode": [
-                "026:029"
-            ],
             "distribution": [
                 {
-                    "mediaType": "application/x-tar",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Y2001.tar.gz",
-                    "description": "Y2001.tar.gz",
                     "@type": "dcat:Distribution",
+                    "description": "Y2001.tar.gz",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Y2001.tar.gz",
+                    "mediaType": "application/x-tar",
                     "title": "Y2001.tar.gz"
                 },
                 {
-                    "mediaType": "application/x-tar",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Y2002.tar.gz",
-                    "description": "Y2002.tar.gz",
                     "@type": "dcat:Distribution",
+                    "description": "Y2002.tar.gz",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Y2002.tar.gz",
+                    "mediaType": "application/x-tar",
                     "title": "Y2002.tar.gz"
                 },
                 {
-                    "mediaType": "application/x-gzip",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Y2003.tar.gz",
-                    "description": "Y2003.tar.gz",
                     "@type": "dcat:Distribution",
+                    "description": "Y2003.tar.gz",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Y2003.tar.gz",
+                    "mediaType": "application/x-gzip",
                     "title": "Y2003.tar.gz"
                 },
                 {
-                    "mediaType": "application/x-gzip",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Y2004.tar.gz",
-                    "description": "Y2004.tar.gz",
                     "@type": "dcat:Distribution",
+                    "description": "Y2004.tar.gz",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Y2004.tar.gz",
+                    "mediaType": "application/x-gzip",
                     "title": "Y2004.tar.gz"
                 },
                 {
-                    "mediaType": "application/x-gzip",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Y2005.tar.gz",
-                    "description": "Y2005.tar.gz",
                     "@type": "dcat:Distribution",
+                    "description": "Y2005.tar.gz",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Y2005.tar.gz",
+                    "mediaType": "application/x-gzip",
                     "title": "Y2005.tar.gz"
                 },
                 {
-                    "mediaType": "application/x-gzip",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Y2006.tar.gz",
-                    "description": "Y2006.tar.gz",
                     "@type": "dcat:Distribution",
+                    "description": "Y2006.tar.gz",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Y2006.tar.gz",
+                    "mediaType": "application/x-gzip",
                     "title": "Y2006.tar.gz"
                 },
                 {
-                    "mediaType": "application/x-gzip",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Y2007.tar.gz",
-                    "description": "Y2007.tar.gz",
                     "@type": "dcat:Distribution",
+                    "description": "Y2007.tar.gz",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Y2007.tar.gz",
+                    "mediaType": "application/x-gzip",
                     "title": "Y2007.tar.gz"
                 },
                 {
-                    "mediaType": "application/x-gzip",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Y2008.tar.gz",
-                    "description": "Y2008.tar.gz",
                     "@type": "dcat:Distribution",
+                    "description": "Y2008.tar.gz",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Y2008.tar.gz",
+                    "mediaType": "application/x-gzip",
                     "title": "Y2008.tar.gz"
                 },
                 {
-                    "mediaType": "application/x-gzip",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Y2009.tar.gz",
-                    "description": "Y2009.tar.gz",
                     "@type": "dcat:Distribution",
+                    "description": "Y2009.tar.gz",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Y2009.tar.gz",
+                    "mediaType": "application/x-gzip",
                     "title": "Y2009.tar.gz"
                 }
             ],
-            "accrualPeriodicity": "irregular"
+            "identifier": "DASHLINK_331",
+            "issued": "2011-03-25",
+            "keyword": [
+                "ames",
+                "nasa",
+                "dashlink"
+            ],
+            "landingPage": "https://c3.nasa.gov/dashlink/resources/331/",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:029"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Dashlink"
+            },
+            "title": "California Satellite Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-X-SREM-5-CR1-V1.0",
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
+            "description": "This data set contains derived electron and proton flux energies in MeV from the Standard Radiation Environment Monitor (SREM) instrument on the Rosetta spacecraft.  These are CODMAC Level 5 derived data, and measure the radiation in the spacecraft environment during the CRUISE 1 mission phase.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-x-srem-5-cr1-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "calibration",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-X-SREM-5-CR1-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-x-srem-5-cr1-v1.0",
-            "description": "This data set contains derived electron and proton flux energies in MeV from the Standard Radiation Environment Monitor (SREM) instrument on the Rosetta spacecraft.  These are CODMAC Level 5 derived data, and measure the radiation in the spacecraft environment during the CRUISE 1 mission phase.",
-            "title": "ROSETTA-ORBITER X SREM 5 CRUISE 1\n    V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER X SREM 5 CRUISE 1\n    V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1641945731-OB_DAAC.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, OB.DAAC.",
-            "issued": "2019-06-23",
-            "temporal": "2002-07-04T00:00:00Z/2022-01-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2019-10-01",
-            "keyword": [
-                "national geospatial data asset",
-                "ngda",
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
-            "identifier": "C1641945731-OB_DAAC",
             "description": "The Ocean Biology DAAC produces near real-time (quicklook) products using the best-available combination of ancillary data from meteorological and ozone data. As such, the inputs and the calibration used are less than optimal. Quicklook products provide a snapshot of the data during a short time period within a single orbit.",
-            "title": "Aqua MODIS Global Binned 4\u00b5m Day/Night Sea Surface Temperature (SST4) - Near Real Time (NRT) Data, version R2019.0",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://oceandata.sci.gsfc.nasa.gov/directaccess/MODIS-Aqua/L3BIN/",
-                    "description": "NASA Ocean Color Web - Data Distribution Site",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Ocean Color Web - Data Distribution Site",
+                    "downloadURL": "https://oceandata.sci.gsfc.nasa.gov/directaccess/MODIS-Aqua/L3BIN/",
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
-                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/data/10.5067/AQUA/MODIS/L3B/SST/R2019.0",
-                    "description": "MODIS-Aqua L3B 4\u00b5m Day/Night Sea Surface Temperature (SST4) - Near Real Time (NRT) Dataset Landing Page",
                     "@type": "dcat:Distribution",
+                    "description": "MODIS-Aqua L3B 4\u00b5m Day/Night Sea Surface Temperature (SST4) - Near Real Time (NRT) Dataset Landing Page",
+                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/data/10.5067/AQUA/MODIS/L3B/SST/R2019.0",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 }
             ],
+            "identifier": "C1641945731-OB_DAAC",
+            "issued": "2019-06-23",
+            "keyword": [
+                "national geospatial data asset",
+                "ngda",
+                "earth science",
+                "oceans",
+                "ocean temperature"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1641945731-OB_DAAC.html",
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
+            "title": "Aqua MODIS Global Binned 4\u00b5m Day/Night Sea Surface Temperature (SST4) - Near Real Time (NRT) Data, version R2019.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/889",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Asner, G.P., K.M. Carlson, and D.E. Knapp. 2008. LBA-ECO LC-18 Hyperion 30-m Surface Reflectance, Mato Grosso, Brazil: July 2004. ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/889",
-            "issued": "2023-10-03",
-            "temporal": "2004-07-10T00:00:00Z/2004-07-10T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-10-05",
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
-            "identifier": "C2777370025-ORNL_CLOUD",
             "description": "This image was collected by the Hyperion sensor on 10-July-2004 at 13:16:16 GMT.  It was calibrated to apparent surface reflectance using the ACORN atmospheric model.The Hyperion imager has a spectral range of 400-2500 nm, a spectral resolution of 10 nm, spatial resolution of 30 m, and a swath width of 7.8 km. Sampling is scene based (256 samples, 512 lines) (http://eo1.usgs.gov/sensors.php).  Through these large number of spectral bands, complex land ecosystems can be imaged and accurately classified.Data from the EO-1 Hyperion imaging spectrometer may greatly increase our ability to estimate the presence and structural attributes of selective logging in the Amazon Basin using four biogeophysical indicators not yet derived simultaneously from any satellite sensor: 1) green canopy leaf area index; 2) degree of shadowing; 3) presence of exposed soil and; 4) non-photosynthetic vegetation material. Airborne, field and modeling studies have shown that the optical reflectance continuum (400-2500 nm) contains sufficient information to derive estimates of each of these indicators. Our ongoing studies in the eastern Amazon basin also suggest that these four indicators are sensitive to logging intensity. Satellite-based estimates of these indicators should provide a means to quantify both the presence and degree of structural disturbance caused by various logging regimes.",
-            "graphic-preview-description": "Browse Image",
-            "title": "LBA-ECO LC-18 Hyperion 30-m Surface Reflectance, Mato Grosso, Brazil: July 2004",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/lba_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F889",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F889",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/lba/land_use_land_cover_change/LC18_Hyperion/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/lba/land_use_land_cover_change/LC18_Hyperion/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/LBA/guides/LC18_Hyperion.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/LBA/guides/LC18_Hyperion.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/889",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/889",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC18_Hyperion/comp/Hyperion_Spectral_Coverage.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC18_Hyperion/comp/Hyperion_Spectral_Coverage.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC18_Hyperion/comp/LC18_Hyperion.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC18_Hyperion/comp/LC18_Hyperion.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC18_Hyperion/comp/Mato_Grasso_July_2004_image_bands.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC18_Hyperion/comp/Mato_Grasso_July_2004_image_bands.pdf",
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
+            "identifier": "C2777370025-ORNL_CLOUD",
+            "issued": "2023-10-03",
+            "keyword": [
+                "land surface",
+                "surface radiative properties",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/889",
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
             "spatial": "-52.46 -13.17 -52.28 -12.66",
+            "temporal": "2004-07-10T00:00:00Z/2004-07-10T23:59:59Z",
             "theme": [
                 "LBA-ECO",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "LBA-ECO LC-18 Hyperion 30-m Surface Reflectance, Mato Grosso, Brazil: July 2004"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-MIDAS-3-ESC2-SAMPLES-V3.0",
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
+            "description": "The Micro-Imaging Dust Analysis System (MIDAS) is an instrument on the\nROSETTA Orbiter that will provide 3D images and statistical parameters\nof pristine cometary particles, collected in the vicinity of comet\n67P/Churyumov-Gerasimenko. This data set includes all data from the\nCOMET ESCORT 2 mission phase. This release supersedes version 2.0.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-midas-3-esc2-samples-v3.0_t3ny-x5d4",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-MIDAS-3-ESC2-SAMPLES-V3.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-midas-3-esc2-samples-v3.0_t3ny-x5d4",
-            "description": "The Micro-Imaging Dust Analysis System (MIDAS) is an instrument on the\nROSETTA Orbiter that will provide 3D images and statistical parameters\nof pristine cometary particles, collected in the vicinity of comet\n67P/Churyumov-Gerasimenko. This data set includes all data from the\nCOMET ESCORT 2 mission phase. This release supersedes version 2.0.",
-            "title": "ROSETTA-ORBITER 67P MIDAS 3 ESC2 SAMPLES V3.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P MIDAS 3 ESC2 SAMPLES V3.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.7927/k9t6-gh59",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Oakleaf, J. R., C. M. Kennedy, S. Baruch-Mordo, J. S. Gerber, P. C. West, J. A. Johnson, and J. Kiesecker. 2020-03-26. Global Development Potential Indices. Version 1.00. Palisades, NY. Archived by National Aeronautics and Space Administration, U.S. Government, NASA Socioeconomic Data and Applications Center (SEDAC). https://doi.org/10.7927/k9t6-gh59. https://doi.org/10.7927/k9t6-gh59.",
-            "issued": "2020-03-26",
-            "temporal": "2016-01-01T00:00:00Z/2016-12-31T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-03-26",
-            "keyword": [
-                "earth science",
-                "environmental impacts",
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
-            "identifier": "C1739457324-SEDAC",
-            "description": "The Global Development Potential Indices (DPIs) data set contains thirteen sector-level DPIs for sectors related to renewable energy  (concentrated solar power, photovoltaic solar, wind, hydropower), fossil fuels (coal, conventional and unconventional oil and gas), mining (metallic, non-metallic), and agriculture (crop, biofuels expansion). The DPI for each sector represents land suitability that accounts for both resource potential and development feasibility. Each DPI is a 1-km spatially-explicit, global land suitability map that has been validated using locations of current and planned development, and examined for uncertainty and sensitivity. The DPIs can be used to identify lands with current favorable economic and physical conditions for individual sector expansion and assist in planning for sector and cumulative development across the globe.",
-            "release-place": "Palisades, NY",
-            "graphic-preview-description": "Maps Download Page",
             "creator": "Oakleaf, J. R., C. M. Kennedy, S. Baruch-Mordo, J. S. Gerber, P. C. West, J. A. Johnson, and J. Kiesecker",
-            "title": "Global Development Potential Indices",
-            "graphic-preview-file": "https://sedac.ciesin.columbia.edu/data/set/lulc-development-potential-indices/maps",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The Global Development Potential Indices (DPIs) data set contains thirteen sector-level DPIs for sectors related to renewable energy  (concentrated solar power, photovoltaic solar, wind, hydropower), fossil fuels (coal, conventional and unconventional oil and gas), mining (metallic, non-metallic), and agriculture (crop, biofuels expansion). The DPI for each sector represents land suitability that accounts for both resource potential and development feasibility. Each DPI is a 1-km spatially-explicit, global land suitability map that has been validated using locations of current and planned development, and examined for uncertainty and sensitivity. The DPIs can be used to identify lands with current favorable economic and physical conditions for individual sector expansion and assist in planning for sector and cumulative development across the globe.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.7927%2Fk9t6-gh59",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.7927%2Fk9t6-gh59",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/downloads/maps/lulc/lulc-development-potential-indices/lulc-development-potential-indices-bio-thumbnail.jpg",
-                    "description": "Sample browse graphic of the data set.",
                     "@type": "dcat:Distribution",
+                    "description": "Sample browse graphic of the data set.",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/downloads/maps/lulc/lulc-development-potential-indices/lulc-development-potential-indices-bio-thumbnail.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/lulc-development-potential-indices/data-download",
-                    "description": "Data Download Page",
                     "@type": "dcat:Distribution",
+                    "description": "Data Download Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/lulc-development-potential-indices/data-download",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/lulc-development-potential-indices/maps",
-                    "description": "Maps Download Page",
                     "@type": "dcat:Distribution",
+                    "description": "Maps Download Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/lulc-development-potential-indices/maps",
+                    "mediaType": "text/html",
                     "title": "Get a related map visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://sedac.ciesin.columbia.edu/data/set/lulc-development-potential-indices/docs",
-                    "description": "Documentation Page",
                     "@type": "dcat:Distribution",
+                    "description": "Documentation Page",
+                    "downloadURL": "http://sedac.ciesin.columbia.edu/data/set/lulc-development-potential-indices/docs",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/lulc-development-potential-indices/maps/services",
-                    "description": "Web Map Service Page",
                     "@type": "dcat:Distribution",
+                    "description": "Web Map Service Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/lulc-development-potential-indices/maps/services",
+                    "mediaType": "text/html",
                     "title": "Use Web Map Service (WMS) to download the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/lulc-development-potential-indices",
-                    "description": "Data Set\u00a0Overview Page",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set\u00a0Overview Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/lulc-development-potential-indices",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "graphic-preview-description": "Maps Download Page",
+            "graphic-preview-file": "https://sedac.ciesin.columbia.edu/data/set/lulc-development-potential-indices/maps",
+            "identifier": "C1739457324-SEDAC",
+            "issued": "2020-03-26",
+            "keyword": [
+                "earth science",
+                "environmental impacts",
+                "human dimensions"
+            ],
+            "landingPage": "https://doi.org/10.7927/k9t6-gh59",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2020-03-26",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "SEDAC"
+            },
+            "release-place": "Palisades, NY",
             "spatial": "-180.0 -60.0 180.0 85.0",
+            "temporal": "2016-01-01T00:00:00Z/2016-12-31T00:00:00Z",
             "theme": [
                 "LULC",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Global Development Potential Indices"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/D7ZJT02NGCC1",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "IceBridge LVIS-GH L1B Geolocated Return Energy Waveforms V001. Version 1. Archived by National Aeronautics and Space Administration, U.S. Government, NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/D7ZJT02NGCC1.",
-            "issued": "2013-10-30",
-            "temporal": "2013-10-30T00:00:00Z/2013-11-14T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2013-11-14",
-            "keyword": [
-                "earth science",
-                "topography",
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
-            "identifier": "C1000000800-NSIDC_ECS",
             "description": "This data set contains energy waveform data measured by the NASA Land, Vegetation, and Ice Sensor (LVIS), an airborne lidar scanning laser altimeter, aboard the Global Hawk Unmanned Aerial Vehicle. The data were collected as part of NASA Operation IceBridge funded campaigns.",
-            "title": "IceBridge LVIS-GH L1B Geolocated Return Energy Waveforms V001",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FD7ZJT02NGCC1",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FD7ZJT02NGCC1",
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
-                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/ICEBRIDGE/ILVGH1B.001/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/ICEBRIDGE/ILVGH1B.001/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1000000800-NSIDC_ECS&m=-32.203125%2127.5625%211%211%210%210%2C2&q=ILVGH1B",
-                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1000000800-NSIDC_ECS&m=-32.203125%2127.5625%211%211%210%210%2C2&q=ILVGH1B",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/data/data-access-tool/ILVGH1B/versions/1/",
-                    "description": "Data Access link for ITSD project",
                     "@type": "dcat:Distribution",
+                    "description": "Data Access link for ITSD project",
+                    "downloadURL": "https://nsidc.org/data/data-access-tool/ILVGH1B/versions/1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/D7ZJT02NGCC1",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/D7ZJT02NGCC1",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/D7ZJT02NGCC1",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/D7ZJT02NGCC1",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
-            "spatial": "-180.0 60.0 180.0 90.0",
-            "theme": [
-                "2013_AN_NASA",
-                "2013_GR_NASA",
-                "geospatial"
+            "identifier": "C1000000800-NSIDC_ECS",
+            "issued": "2013-10-30",
+            "keyword": [
+                "earth science",
+                "topography",
+                "land surface"
             ],
+            "landingPage": "https://doi.org/10.5067/D7ZJT02NGCC1",
             "language": [
                 "en-US"
-            ]
-        },
-        {
-            "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=PHX-M-SSI-5-ROUGHNESS-OPS-V1.0",
-            "bureauCode": [
-                "026:00"
             ],
-            "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
+            "modified": "2013-11-14",
+            "programCode": [
+                "026:001"
             ],
-            "keyword": [
-                "phoenix",
-                "mars"
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA NSIDC DAAC"
+            },
+            "spatial": "-180.0 60.0 180.0 90.0",
+            "temporal": "2013-10-30T00:00:00Z/2013-11-14T23:59:59.999Z",
+            "theme": [
+                "2013_AN_NASA",
+                "2013_GR_NASA",
+                "geospatial"
+            ],
+            "title": "IceBridge LVIS-GH L1B Geolocated Return Energy Waveforms V001"
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
+            "description": "The Surface Stereo Imager (SSI) experiment on the Mars Phoenix Lander consists of one instrument component plus command electronics. This SSI Imaging Operations RDR data set contains roughness data from the Surface Stereo Imager (SSI).",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.phx-m-ssi-5-roughness-ops-v1.0_t3v2-xbby",
+            "issued": "2018-06-26",
+            "keyword": [
+                "phoenix",
+                "mars"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=PHX-M-SSI-5-ROUGHNESS-OPS-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.phx-m-ssi-5-roughness-ops-v1.0_t3v2-xbby",
-            "description": "The Surface Stereo Imager (SSI) experiment on the Mars Phoenix Lander consists of one instrument component plus command electronics. This SSI Imaging Operations RDR data set contains roughness data from the Surface Stereo Imager (SSI).",
-            "title": "PHOENIX MARS SURFACE STEREO IMAGER 5 ROUGHNESS OPS V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "PHOENIX MARS SURFACE STEREO IMAGER 5 ROUGHNESS OPS V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ECTSM-MSL44",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "ECCO Consortium, Fukumori, I., Wang, O., Fenty, I., Forget, G., Heimbach, P., & Ponte, R. M.. 2021-04-19. ECCO Global Mean Sea Level - Monthly Mean (Version 4 Release 4). Version V4r4. PO.DAAC. Archived by National Aeronautics and Space Administration, U.S. Government, PO.DAAC. https://doi.org/10.5067/ECTSM-MSL44. ECCO; ECCO Consortium, Fukumori, I., Wang, O., Fenty, I., Forget, G., Heimbach, P., & Ponte, R. M.; 2020; ECCO Global Mean Sea Level - Monthly Mean (Version 4 Release 4); 10.5067/ECTSM-MSL44; https://podaac.jpl.nasa.gov/ECCO.",
-            "issued": "2021-01-01",
-            "temporal": "1992-01-01T00:00:00Z/2018-01-01T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2018-01-01",
-            "references": [
-                "https://doi.org/10.5281/zenodo.3765928"
-            ],
-            "keyword": [
-                "climate indicators",
-                "earth science",
-                "atmospheric/ocean indicators"
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
-            "identifier": "C1991543742-POCLOUD",
-            "description": "This dataset provides monthly-averaged global mean sea level from the ECCO Version 4 Release 4 (V4r4) ocean and sea-ice state estimate. Estimating the Circulation and Climate of the Ocean (ECCO) ocean and sea-ice state estimates are dynamically and kinematically-consistent reconstructions of the three-dimensional time-evolving ocean, sea-ice, and surface atmospheric states. ECCO V4r4 is a free-running solution of the 1-degree global configuration of the MIT general circulation model (MITgcm) that has been fit to observations in a least-squares sense. Observational data constraints used in V4r4 include sea surface height and model sea level anomaly (SSH) from satellite altimeters [ERS-1/2, TOPEX/Poseidon, GFO, ENVISAT, Jason-1,2,3, CryoSat-2, and SARAL/AltiKa]; sea surface temperature (SST) from satellite radiometers [AVHRR], sea surface salinity (SSS) from the Aquarius satellite radiometer/scatterometer, ocean bottom pressure (OBP) from the GRACE satellite gravimeter; sea ice concentration from satellite radiometers [SSM/I and SSMIS], and in-situ ocean temperature and salinity measured with conductivity-temperature-depth (CTD) sensors and expendable bathythermographs (XBTs) from several programs [e.g., WOCE, GO-SHIP, Argo, and others] and platforms [e.g., research vessels, gliders, moorings, ice-tethered profilers, and instrumented pinnipeds]. V4r4 covers the period 1992-01-01T12:00:00 to 2018-01-01T00:00:00.",
-            "release-place": "PO.DAAC",
-            "graphic-preview-description": "Thumbnail image for Website",
             "creator": "ECCO Consortium, Fukumori, I., Wang, O., Fenty, I., Forget, G., Heimbach, P., & Ponte, R. M.",
-            "title": "ECCO Global Mean Sea Level - Monthly Mean (Version 4 Release 4)",
-            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/ECCO_L4_GMSL_TIME_SERIES_MONTHLY_V4R4.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "This dataset provides monthly-averaged global mean sea level from the ECCO Version 4 Release 4 (V4r4) ocean and sea-ice state estimate. Estimating the Circulation and Climate of the Ocean (ECCO) ocean and sea-ice state estimates are dynamically and kinematically-consistent reconstructions of the three-dimensional time-evolving ocean, sea-ice, and surface atmospheric states. ECCO V4r4 is a free-running solution of the 1-degree global configuration of the MIT general circulation model (MITgcm) that has been fit to observations in a least-squares sense. Observational data constraints used in V4r4 include sea surface height and model sea level anomaly (SSH) from satellite altimeters [ERS-1/2, TOPEX/Poseidon, GFO, ENVISAT, Jason-1,2,3, CryoSat-2, and SARAL/AltiKa]; sea surface temperature (SST) from satellite radiometers [AVHRR], sea surface salinity (SSS) from the Aquarius satellite radiometer/scatterometer, ocean bottom pressure (OBP) from the GRACE satellite gravimeter; sea ice concentration from satellite radiometers [SSM/I and SSMIS], and in-situ ocean temperature and salinity measured with conductivity-temperature-depth (CTD) sensors and expendable bathythermographs (XBTs) from several programs [e.g., WOCE, GO-SHIP, Argo, and others] and platforms [e.g., research vessels, gliders, moorings, ice-tethered profilers, and instrumented pinnipeds]. V4r4 covers the period 1992-01-01T12:00:00 to 2018-01-01T00:00:00.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FECTSM-MSL44",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FECTSM-MSL44",
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
-                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/ECCO_L4_GMSL_TIME_SERIES_MONTHLY_V4R4.jpg",
-                    "description": "Thumbnail image for Website",
                     "@type": "dcat:Distribution",
+                    "description": "Thumbnail image for Website",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/ECCO_L4_GMSL_TIME_SERIES_MONTHLY_V4R4.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/ECTSM-MSL44",
-                    "description": "Access the data set landing page for the collection.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data set landing page for the collection.",
+                    "downloadURL": "https://doi.org/10.5067/ECTSM-MSL44",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1991543742-POCLOUD",
-                    "description": "Browse granule search results in Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse granule search results in Earthdata Search",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1991543742-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C1991543742-POCLOUD/temporal",
-                    "description": "Browse and download granules over HTTPS using the virtual directories service",
                     "@type": "dcat:Distribution",
+                    "description": "Browse and download granules over HTTPS using the virtual directories service",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C1991543742-POCLOUD/temporal",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 }
             ],
+            "graphic-preview-description": "Thumbnail image for Website",
+            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/ECCO_L4_GMSL_TIME_SERIES_MONTHLY_V4R4.jpg",
+            "identifier": "C1991543742-POCLOUD",
+            "issued": "2021-01-01",
+            "keyword": [
+                "climate indicators",
+                "earth science",
+                "atmospheric/ocean indicators"
+            ],
+            "landingPage": "https://doi.org/10.5067/ECTSM-MSL44",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2018-01-01",
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
+            "title": "ECCO Global Mean Sea Level - Monthly Mean (Version 4 Release 4)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/doi:10.5067/FY616726UXSR",
             "citation": "Global Modeling and Assimilation Office (GMAO). 2021-12-15. M2_TMAX_PM25. Version 1. MERRA-2 avgM_2d_pm25_admin0, 2d, Single-Level, Country-Level Surface PM2.5 Monthly Mean Products V1. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/doi:10.5067/FY616726UXSR. https://disc.gsfc.nasa.gov/datacollection/M2_TMAX_PM25_1.html. Digital Science Data.",
-            "issued": "2023-02-10",
-            "temporal": "1980-01-01T00:00:00Z/2023-02-28T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-02-10",
-            "references": [
-                "https://doi.org/%20http%3A//doi.org/10.1016/j.atmosenv.2015.11.004",
-                "https://doi.org/10.1175/JCLI-D-16-0758.1",
-                "https://doi.org/10.1175/JCLI-D-16-0613.1",
-                "https://doi.org/10.4209/aaqr.2016.04.0145",
-                "https://doi.org/10.1016/j.apr.2016.10.009",
-                "https://doi.org/10.1175/JCLI-D-16-0609.1"
-            ],
-            "keyword": [
-                "air quality",
-                "aerosols",
-                "earth science",
-                "public health",
-                "human dimensions",
-                "atmosphere"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Suhung Shen",
                 "hasEmail": "mailto:suhung.shen-1@nasa.gov"
             },
+            "creator": "Global Modeling and Assimilation Office (GMAO)",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C2184005745-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "M2_TMAX_PM25 is a value-added product derived from the MERRA-2 aerosol monthly product M2TMNXAER_5.12.4 (or tavgM_2d_aer_Nx).  The surface concentration of fine particulate matter (PM2.5) is calculated as the sum of individual aerosol components (organic carbon, black carbon, sulfate, sea salt, and dust) (Buchard et al., 2017) and is recast from the native MERRA-2 model grid.  This data collection includes separate files for country-level (and territories) PM2.5 concentrations with and without population weighting applied. \n\nMERRA-2 Mailing List: Sign up to receive information on reprocessing of data, changing of tools and services, as well as data announcements from GMAO. Contact the GES DISC Help Desk (gsfc-dl-help-disc@mail.nasa.gov) to be added to the list.\n\nQuestions: If you have a question on data access, email to the GES DISC Help Desk (gsfc-dl-help-disc@mail.nasa.gov), and the question on science, email to the MERRA-2 science team (merra-questions@lists.nasa.gov).",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "M2_TMAX_PM25",
-            "creator": "Global Modeling and Assimilation Office (GMAO)",
-            "graphic-preview-description": "Sample image:`the annual mean surface PM2.5 at country level for 2019.",
-            "title": "MERRA-2 avgM_2d_pm25_admin0, 2d, Single-Level, Country-Level Surface PM2.5 Monthly Mean Products V1 (M2_TMAX_PM25) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/M2_TMAX_PM25_1.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FFY616726UXSR",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FFY616726UXSR",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/M2_TMAX_PM25_1.png",
-                    "description": "Sample image:`the annual mean surface PM2.5 at country level for 2019.",
                     "@type": "dcat:Distribution",
+                    "description": "Sample image:`the annual mean surface PM2.5 at country level for 2019.",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/M2_TMAX_PM25_1.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://goldsmr4.gesdisc.eosdis.nasa.gov/data/MERRA2_CLIM/M2_TMAX_PM25.1/doc/README_M2PM25.pdf",
-                    "description": "README Document",
                     "@type": "dcat:Distribution",
+                    "description": "README Document",
+                    "downloadURL": "https://goldsmr4.gesdisc.eosdis.nasa.gov/data/MERRA2_CLIM/M2_TMAX_PM25.1/doc/README_M2PM25.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's read me document"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://gmao.gsfc.nasa.gov/pubs/docs/Keller1364.pdf",
-                    "description": "File Specification Document",
                     "@type": "dcat:Distribution",
+                    "description": "File Specification Document",
+                    "downloadURL": "https://gmao.gsfc.nasa.gov/pubs/docs/Keller1364.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View the primary investigator's documentation for this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/M2_TMAX_PM25_1.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/M2_TMAX_PM25_1.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://goldsmr4.gesdisc.eosdis.nasa.gov/data/MERRA2_CLIM/M2_TMAX_PM25.1/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://goldsmr4.gesdisc.eosdis.nasa.gov/data/MERRA2_CLIM/M2_TMAX_PM25.1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=M2_TMAX_PM25",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=M2_TMAX_PM25",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
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
-                    "downloadURL": "https://disc.gsfc.nasa.gov/information/howto?title=How+to+remotely+access+MERRA-2+with+Python3+and+calculate+monthly+average+surface+PM2.5+for+world+countries",
-                    "description": "How to calculate MERRA-2 PM2.5",
                     "@type": "dcat:Distribution",
+                    "description": "How to calculate MERRA-2 PM2.5",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/information/howto?title=How+to+remotely+access+MERRA-2+with+Python3+and+calculate+monthly+average+surface+PM2.5+for+world+countries",
+                    "mediaType": "text/html",
                     "title": "View this dataset's how-to documentation"
                 }
             ],
+            "graphic-preview-description": "Sample image:`the annual mean surface PM2.5 at country level for 2019.",
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/M2_TMAX_PM25_1.png",
+            "identifier": "C2184005745-GES_DISC",
+            "issued": "2023-02-10",
+            "keyword": [
+                "air quality",
+                "aerosols",
+                "earth science",
+                "public health",
+                "human dimensions",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/doi:10.5067/FY616726UXSR",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2023-02-10",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
+            },
+            "references": [
+                "https://doi.org/%20http%3A//doi.org/10.1016/j.atmosenv.2015.11.004",
+                "https://doi.org/10.1175/JCLI-D-16-0758.1",
+                "https://doi.org/10.1175/JCLI-D-16-0613.1",
+                "https://doi.org/10.4209/aaqr.2016.04.0145",
+                "https://doi.org/10.1016/j.apr.2016.10.009",
+                "https://doi.org/10.1175/JCLI-D-16-0609.1"
+            ],
+            "release-place": "Greenbelt, MD, USA",
+            "series-name": "M2_TMAX_PM25",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "1980-01-01T00:00:00Z/2023-02-28T00:00:00Z",
             "theme": [
                 "MERRA-2",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "MERRA-2 avgM_2d_pm25_admin0, 2d, Single-Level, Country-Level Surface PM2.5 Monthly Mean Products V1 (M2_TMAX_PM25) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MER2-M-PANCAM-5-NORMAL-OPS-V1.0",
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
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mer2-m-pancam-5-normal-ops-v1.0_t43g-2n9t",
+            "issued": "2018-06-26",
+            "keyword": [
+                "mars exploration rover",
+                "mars"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MER2-M-PANCAM-5-NORMAL-OPS-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mer2-m-pancam-5-normal-ops-v1.0_t43g-2n9t",
-            "description": "not applicable",
-            "title": "MER 2 MARS PANORAMIC CAMERA SURFACE NORMAL RDR OPS V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "MER 2 MARS PANORAMIC CAMERA SURFACE NORMAL RDR OPS V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/SENTINEL-3B/OLCI/L3M/ERR/KD/2022",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/GSFC/SED/ESD/GCDC/OB.DAAC. https://doi.org/10.5067/SENTINEL-3B/OLCI/L3M/ERR/KD/2022.",
-            "issued": "2022-09-13",
-            "temporal": "2018-04-25T00:00:00Z/2024-04-22T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-04-13",
-            "keyword": [
-                "atmospheric radiation",
-                "atmosphere",
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
-            "identifier": "C2264534486-OB_DAAC",
             "description": "The Ocean and Land Colour Instrument (OLCI) is the successor to ENVISAT's Medium Resolution Imaging Spectrometer (MERIS) having additional spectral channels, different camera arrangements and simplified on-board processing. The OLCI is a push-broom instrument with five camera modules sharing the field of view. The field of view of the five cameras is arranged in a fan-shaped configuration in the vertical plane, perpendicular to the platform velocity. Each camera has an individual field of view of 14.2\u00b0 and a 0.6\u00b0 overlap with its neighbors. The whole field of view is shifted across track by 12.6\u00b0 away from the sun to minimize the impact of sun glint. OLCI is equipped with on-board calibration hardware based on sun diffusers. There are three sun diffusers--two 'white' diffusers dedicated to radiometric calibration and one dedicated to spectral calibration, with spectral reflectance features. The native resolution is approximately 300m, refered to as Full Resolution (FR). A Reduced Resolution (RR) processing mode provides Level-1B data at sampling rates decreased by a factor of four in both spatial dimensions resulting to resolution of approximately 1.2 km.",
-            "title": "Sentinel-3B OLCI Level-3M Global Mapped Earth-observation Reduced Resolution (ERR) Diffuse Attenuation Coefficient for Downwelling Irradiance (KD) Data, version R2022.0",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSENTINEL-3B%2FOLCI%2FL3M%2FERR%2FKD%2F2022",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSENTINEL-3B%2FOLCI%2FL3M%2FERR%2FKD%2F2022",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
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
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://oceandata.sci.gsfc.nasa.gov/opendap/S3BOLCI/",
-                    "description": "OB.DAAC OPeNDAP Site for Sentinel-3B OLCI Standard Mapped Image (SMI) Product",
                     "@type": "dcat:Distribution",
+                    "description": "OB.DAAC OPeNDAP Site for Sentinel-3B OLCI Standard Mapped Image (SMI) Product",
+                    "downloadURL": "https://oceandata.sci.gsfc.nasa.gov/opendap/S3BOLCI/",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 }
             ],
+            "identifier": "C2264534486-OB_DAAC",
+            "issued": "2022-09-13",
+            "keyword": [
+                "atmospheric radiation",
+                "atmosphere",
+                "ocean optics",
+                "earth science",
+                "oceans"
+            ],
+            "landingPage": "https://doi.org/10.5067/SENTINEL-3B/OLCI/L3M/ERR/KD/2022",
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
+            "title": "Sentinel-3B OLCI Level-3M Global Mapped Earth-observation Reduced Resolution (ERR) Diffuse Attenuation Coefficient for Downwelling Irradiance (KD) Data, version R2022.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/TERRA/MODIS/L4M/GSM/2022",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/GSFC/SED/ESD/GCDC/OB.DAAC. https://doi.org/10.5067/TERRA/MODIS/L4M/GSM/2022.",
-            "issued": "2023-11-16",
-            "temporal": "2000-02-24T00:00:00Z/2023-12-04T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-11-16",
-            "keyword": [
-                "ngda",
-                "oceans",
-                "earth science",
-                "national geospatial data asset",
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
-            "identifier": "C2802700398-OB_DAAC",
             "description": "MODIS (or Moderate-Resolution Imaging Spectroradiometer) is a key instrument aboard the Terra (EOS AM) and Aqua (EOS PM) satellites. Terra's orbit around the Earth is timed so that it passes from north to south across the equator in the morning, while Aqua passes south to north over the equator in the afternoon. Terra MODIS and Aqua MODIS are viewing the entire Earth's surface every 1 to 2 days, acquiring data in 36 spectral bands, or groups of wavelengths (see MODIS Technical Specifications). These data will improve our understanding of global dynamics and processes occurring on the land, in the oceans, and in the lower atmosphere. MODIS is playing a vital role in the development of validated, global, interactive Earth system models able to predict global change accurately enough to assist policy makers in making sound decisions concerning the protection of our environment.",
-            "title": "Terra MODIS 4M Global Mapped Garver-Siegel-Maritorena Model (GSM) Data, version R2022.0",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FTERRA%2FMODIS%2FL4M%2FGSM%2F2022",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FTERRA%2FMODIS%2FL4M%2FGSM%2F2022",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://oceandata.sci.gsfc.nasa.gov/directdataaccess/Level-4%20Mapped/Terra-MODIS/",
-                    "description": "NASA Ocean Color Web - Data Distribution Site",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Ocean Color Web - Data Distribution Site",
+                    "downloadURL": "https://oceandata.sci.gsfc.nasa.gov/directdataaccess/Level-4%20Mapped/Terra-MODIS/",
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
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/data/10.5067/TERRA/MODIS/L4M/GSM/2022",
-                    "description": "Terra MODIS Level-4M Garver-Siegel-Maritorena Model (GSM) Dataset Landing Page",
                     "@type": "dcat:Distribution",
+                    "description": "Terra MODIS Level-4M Garver-Siegel-Maritorena Model (GSM) Dataset Landing Page",
+                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/data/10.5067/TERRA/MODIS/L4M/GSM/2022",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://oceandata.sci.gsfc.nasa.gov/opendap/MODIST/L4SMI/",
-                    "description": "OB.DAAC OPeNDAP Site for Terra MODIS Standard Mapped Image (SMI) Product",
                     "@type": "dcat:Distribution",
+                    "description": "OB.DAAC OPeNDAP Site for Terra MODIS Standard Mapped Image (SMI) Product",
+                    "downloadURL": "https://oceandata.sci.gsfc.nasa.gov/opendap/MODIST/L4SMI/",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 }
             ],
+            "identifier": "C2802700398-OB_DAAC",
+            "issued": "2023-11-16",
+            "keyword": [
+                "ngda",
+                "oceans",
+                "earth science",
+                "national geospatial data asset",
+                "ocean optics"
+            ],
+            "landingPage": "https://doi.org/10.5067/TERRA/MODIS/L4M/GSM/2022",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2023-11-16",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GCDC/OB.DAAC"
+            },
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2000-02-24T00:00:00Z/2023-12-04T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Terra MODIS 4M Global Mapped Garver-Siegel-Maritorena Model (GSM) Data, version R2022.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewBundle.jsp?identifier=urn%3Anasa%3Apds%3Agbo.kbo-centaur.magnitudes&version=1.0",
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
-                "multiple asteroids",
-                "none"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This data set contains absolute visual   magnitudes of 90 Kuiper belt objects and Centaurs from Romanishin and  Tegler (2005).  The absolute magnitudes are derived from V magnitudes  observed by Romanishin and Tegler and their collaborators, with        geometry from the JPL Horizons data base.  As a convenience, R-band    absolute magnitudes derived from the V absolute magnitudes and         published V-R colors are also provided.",
+            "identifier": "urn:nasa:pds:gbo.kbo-centaur.magnitudes",
+            "issued": "2021-05-21",
+            "keyword": [
+                "multiple asteroids",
+                "none"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewBundle.jsp?identifier=urn%3Anasa%3Apds%3Agbo.kbo-centaur.magnitudes&version=1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:gbo.kbo-centaur.magnitudes",
-            "description": "This data set contains absolute visual   magnitudes of 90 Kuiper belt objects and Centaurs from Romanishin and  Tegler (2005).  The absolute magnitudes are derived from V magnitudes  observed by Romanishin and Tegler and their collaborators, with        geometry from the JPL Horizons data base.  As a convenience, R-band    absolute magnitudes derived from the V absolute magnitudes and         published V-R colors are also provided.",
-            "title": "KBO AND CENTAUR ABSOLUTE MAGNITUDES",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "KBO AND CENTAUR ABSOLUTE MAGNITUDES"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.nasa.gov/d/t4an-hdn6",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "GeneLab Outreach",
+                "hasEmail": "mailto:genelab-outreach@lists.nasa.gov"
+            },
+            "description": "Life in spaceflight demonstrates remarkable adaptive processes within the specialized environments of space vehicles which are subject to the myriad of attending and unique environmental issues associated with orbital trajectories. To examine the adaptive processes that occur in plants in space leaves and roots from Arabidopsis seedlings that were grown from seed for 12 days on the International Space Station and preserved on orbit in RNAlater were returned to earth and analyzed using iTRAQ broad scale proteomics procedures.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "GeneLab Study Page",
+                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-16",
+                    "mediaType": "text/html",
+                    "title": "Spaceflight adaptation requires organ specific alterations in the proteomes of Arabidopsis"
+                }
+            ],
+            "identifier": "nasa_genelab_GLDS-16_t4an-hdn6",
             "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
             "keyword": [
                 "mass spectrometry",
                 "labeling",
@@ -1392400,80 +1392414,40 @@
                 "sample collection",
                 "spaceflight"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "GeneLab Outreach",
-                "hasEmail": "mailto:genelab-outreach@lists.nasa.gov"
-            },
+            "landingPage": "https://data.nasa.gov/d/t4an-hdn6",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "nasa_genelab_GLDS-16_t4an-hdn6",
-            "description": "Life in spaceflight demonstrates remarkable adaptive processes within the specialized environments of space vehicles which are subject to the myriad of attending and unique environmental issues associated with orbital trajectories. To examine the adaptive processes that occur in plants in space leaves and roots from Arabidopsis seedlings that were grown from seed for 12 days on the International Space Station and preserved on orbit in RNAlater were returned to earth and analyzed using iTRAQ broad scale proteomics procedures.",
-            "title": "Spaceflight adaptation requires organ specific alterations in the proteomes of Arabidopsis",
-            "programCode": [
-                "026:005"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-16",
-                    "description": "GeneLab Study Page",
-                    "@type": "dcat:Distribution",
-                    "title": "Spaceflight adaptation requires organ specific alterations in the proteomes of Arabidopsis"
-                }
-            ],
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "Spaceflight adaptation requires organ specific alterations in the proteomes of Arabidopsis"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/3NEABMVV58N2",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Charles Gatebe; Michael King; Rajesh Poudyal. 2019-03-06. CAR_SKUKUZA_BRDF. Version 2. CAR SKUKUZA BRDF Measurements L1 V2. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/3NEABMVV58N2. https://disc.gsfc.nasa.gov/datacollection/CAR_SKUKUZA_BRDF_2.html.",
-            "issued": "2019-01-27",
-            "temporal": "2005-05-18T00:00:00Z/2007-01-01T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2019-01-27",
-            "keyword": [
-                "oceans",
-                "ocean optics",
-                "surface radiative properties",
-                "earth science",
-                "land surface",
-                "atmospheric radiation",
-                "atmosphere"
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
-            "identifier": "C1617621694-GES_DISC",
-            "description": "CAR mission Skukuza measured bidirectional reflection functions over different natural surfaces and ecosystems in southern Africa. The measurements were conducted to characterize surface anisotropy in support of the CAR SAFARI mission and to validate products from NASA's Earth Observing System satellites.\n\nThis data set consists of observations made with the CAR instrument and includes values for bidirectional reflectance factor at varying spectral bands.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "CAR_SKUKUZA_BRDF",
             "creator": "Charles Gatebe; Michael King; Rajesh Poudyal",
-            "title": "CAR SKUKUZA BRDF Measurements L1 V2 (CAR_SKUKUZA_BRDF) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/CAR_SKUKUZA_L1C_1.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "CAR mission Skukuza measured bidirectional reflection functions over different natural surfaces and ecosystems in southern Africa. The measurements were conducted to characterize surface anisotropy in support of the CAR SAFARI mission and to validate products from NASA's Earth Observing System satellites.\n\nThis data set consists of observations made with the CAR instrument and includes values for bidirectional reflectance factor at varying spectral bands.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2F3NEABMVV58N2",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2F3NEABMVV58N2",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
@@ -1392483,542 +1392457,550 @@
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/CAR_SKUKUZA_BRDF_2.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/CAR_SKUKUZA_BRDF_2.html",
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
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/CAR/CAR_SKUKUZA_BRDF.2/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/CAR/CAR_SKUKUZA_BRDF.2/",
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
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov//public/project/CAR/CAR_BRDF_README-v2.pdf",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov//public/project/CAR/CAR_BRDF_README-v2.pdf",
+                    "mediaType": "application/pdf",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=CAR_SKUKUZA_BRDF",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=CAR_SKUKUZA_BRDF",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 }
             ],
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/CAR_SKUKUZA_L1C_1.jpg",
+            "identifier": "C1617621694-GES_DISC",
+            "issued": "2019-01-27",
+            "keyword": [
+                "oceans",
+                "ocean optics",
+                "surface radiative properties",
+                "earth science",
+                "land surface",
+                "atmospheric radiation",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.5067/3NEABMVV58N2",
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
+            "series-name": "CAR_SKUKUZA_BRDF",
             "spatial": "31.3266 -25.1111 31.8365 -24.7593",
+            "temporal": "2005-05-18T00:00:00Z/2007-01-01T23:59:59.999Z",
             "theme": [
                 "CAR",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "CAR SKUKUZA BRDF Measurements L1 V2 (CAR_SKUKUZA_BRDF) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=JNO-SS-3-FGM-CAL-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "Abstract ======== This data set consists of the Juno FGM calibrated cruise observations. The FGM sensor block uses two miniature ring-core fluxgate sensors to measure the magnetic field in three components of the vector field. There are multiple FGM data products to accomodate different coordinate systems.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.jno-ss-3-fgm-cal-v1.0_t4br-but5",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "solar system",
                 "jupiter",
                 "juno",
                 "earth"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=JNO-SS-3-FGM-CAL-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.jno-ss-3-fgm-cal-v1.0_t4br-but5",
-            "description": "Abstract ======== This data set consists of the Juno FGM calibrated cruise observations. The FGM sensor block uses two miniature ring-core fluxgate sensors to measure the magnetic field in three components of the vector field. There are multiple FGM data products to accomodate different coordinate systems.",
-            "title": "JUNO SS FLUXGATE MAGNETOMETER\nCALIBRATED DATA V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "JUNO SS FLUXGATE MAGNETOMETER\nCALIBRATED DATA V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-X-SREM-2-EXT3-MTP033-V1.0",
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
+            "description": "This data set contains count rates (1/s) as measured by the Standard Radiation Environment Monitor (SREM) instrument on the Rosetta spacecraft, along with their standard deviations.  The primary target is comet 67P/Churyumov-Gerasimenko. These are CODMAC Level 2 Experiment Data Record data, and provide a measure of the radiation in the spacecraft environment during the Medium Term Plan 33 period of the EXTENSION 3 mission phase.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-x-srem-2-ext3-mtp033-v1.0_t4ep-9jmf",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-X-SREM-2-EXT3-MTP033-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-x-srem-2-ext3-mtp033-v1.0_t4ep-9jmf",
-            "description": "This data set contains count rates (1/s) as measured by the Standard Radiation Environment Monitor (SREM) instrument on the Rosetta spacecraft, along with their standard deviations.  The primary target is comet 67P/Churyumov-Gerasimenko. These are CODMAC Level 2 Experiment Data Record data, and provide a measure of the radiation in the spacecraft environment during the Medium Term Plan 33 period of the EXTENSION 3 mission phase.",
-            "title": "ROSETTA-ORBITER 67P SREM 2 EXTENSION 3\n    MTP033 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P SREM 2 EXTENSION 3\n    MTP033 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/VIIRS/CLDMSK_L2_VIIRS_NOAA20.001",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "NASA VIIRS Atmosphere SIPS. 2020-11-10. VIIRS/NOAA20 Cloud Mask and Spectral Test Results 6-Min L2 Swath 750m. Version 1. MODAPS at NASA/GSFC. Archived by National Aeronautics and Space Administration, U.S. Government, L1 and Atmosphere Archive and Distribution System (LAADS). https://doi.org/10.5067/VIIRS/CLDMSK_L2_VIIRS_NOAA20.001. https://doi.org/10.5067/VIIRS/CLDMSK_L2_VIIRS_NOAA20.001.",
-            "issued": "2020-10-13",
-            "temporal": "2012-03-01T00:00:00Z/2024-06-10T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-06-05",
-            "keyword": [
-                "clouds",
-                "earth science",
-                "spectral/engineering",
-                "infrared wavelengths",
-                "atmosphere",
-                "visible wavelengths"
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
-            "identifier": "C1964798938-LAADS",
-            "description": "The VIIRS/NOAA20 Cloud Mask and Spectral Test Results 6-Min L2 Swath 750m product Mask is one of three continuity products designed to sustain the long-term records of both Moderate Resolution Imaging Spectroradiometer (MODIS) and VIIRS heritages. CLDMSK_L2_VIIRS_NOAA20 is the shortname for the NOAA-20 VIIRS incarnation of the Cloud Mask continuity product derived from the MODIS-VIIRS cloud mask (MVCM) algorithm, which itself is based on the MODIS (MOD35) algorithm.  MVCM describes a continuity algorithm that is central to both MODIS data (from Terra and Aqua missions) and VIIRS data (from Suomi National Polar-orbiting Partnership (SNPP) and Joint Polar Satellite System missions).  Please bear in mind that the term MVCM does not appear as an attribute within the product\u2019s metadata.  Implemented to consistently handle MODIS and VIIRS inputs, the NOAA-20 VIIRS collection-1 products use calibration-adjusted NASA VIIRS L1B as inputs.  The nominal spatial resolution of the NOAA-20 VIIRS L2 Cloud mask is 750 meters.\r\n\r\nFor more information consult Product Page at: \r\nhttps://cimss.ssec.wisc.edu/MVCM/",
-            "release-place": "MODAPS at NASA/GSFC",
             "creator": "NASA VIIRS Atmosphere SIPS",
-            "title": "VIIRS/NOAA20 Cloud Mask and Spectral Test Results 6-Min L2 Swath 750m",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The VIIRS/NOAA20 Cloud Mask and Spectral Test Results 6-Min L2 Swath 750m product Mask is one of three continuity products designed to sustain the long-term records of both Moderate Resolution Imaging Spectroradiometer (MODIS) and VIIRS heritages. CLDMSK_L2_VIIRS_NOAA20 is the shortname for the NOAA-20 VIIRS incarnation of the Cloud Mask continuity product derived from the MODIS-VIIRS cloud mask (MVCM) algorithm, which itself is based on the MODIS (MOD35) algorithm.  MVCM describes a continuity algorithm that is central to both MODIS data (from Terra and Aqua missions) and VIIRS data (from Suomi National Polar-orbiting Partnership (SNPP) and Joint Polar Satellite System missions).  Please bear in mind that the term MVCM does not appear as an attribute within the product\u2019s metadata.  Implemented to consistently handle MODIS and VIIRS inputs, the NOAA-20 VIIRS collection-1 products use calibration-adjusted NASA VIIRS L1B as inputs.  The nominal spatial resolution of the NOAA-20 VIIRS L2 Cloud mask is 750 meters.\r\n\r\nFor more information consult Product Page at: \r\nhttps://cimss.ssec.wisc.edu/MVCM/",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FVIIRS%2FCLDMSK_L2_VIIRS_NOAA20.001",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FVIIRS%2FCLDMSK_L2_VIIRS_NOAA20.001",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/VIIRS/CLDMSK_L2_VIIRS_NOAA20.001",
-                    "description": "Data product's landing page",
                     "@type": "dcat:Distribution",
+                    "description": "Data product's landing page",
+                    "downloadURL": "https://doi.org/10.5067/VIIRS/CLDMSK_L2_VIIRS_NOAA20.001",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/search/order/1/CLDMSK_L2_VIIRS_NOAA20--5110",
-                    "description": "Search and order products from LAADS website.",
                     "@type": "dcat:Distribution",
+                    "description": "Search and order products from LAADS website.",
+                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/search/order/1/CLDMSK_L2_VIIRS_NOAA20--5110",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through LAADS"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/opendap/RemoteResources/laads/allData/5110/CLDMSK_L2_VIIRS_NOAA20/contents.html",
-                    "description": "Direct access to CLDMSK_L2_VIIRS_SNPP OPeNDAP data set.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct access to CLDMSK_L2_VIIRS_SNPP OPeNDAP data set.",
+                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/opendap/RemoteResources/laads/allData/5110/CLDMSK_L2_VIIRS_NOAA20/contents.html",
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
+            "identifier": "C1964798938-LAADS",
+            "issued": "2020-10-13",
+            "keyword": [
+                "clouds",
+                "earth science",
+                "spectral/engineering",
+                "infrared wavelengths",
+                "atmosphere",
+                "visible wavelengths"
+            ],
+            "landingPage": "https://doi.org/10.5067/VIIRS/CLDMSK_L2_VIIRS_NOAA20.001",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2024-06-05",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/HBSL/BISB/MODAPS"
+            },
+            "release-place": "MODAPS at NASA/GSFC",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2012-03-01T00:00:00Z/2024-06-10T00:00:00Z",
             "theme": [
                 "NOAA - SPACE WEATHER PROGRAM",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "VIIRS/NOAA20 Cloud Mask and Spectral Test Results 6-Min L2 Swath 750m"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/AURA/TES/TL1BSOL_L1.006",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2016-12-09. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/AURA/TES/TL1BSOL_L1.006. https://asdc.larc.nasa.gov/project/TES.",
-            "issued": "2015-08-27",
-            "temporal": "2004-09-13T00:00:00Z/2018-01-22T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2019-06-19",
-            "keyword": [
-                "spectral/engineering",
-                "infrared wavelengths",
-                "earth science"
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
-            "identifier": "C1386637578-LARC",
             "description": "TL1BSOL_6 is the Tropospheric Emission Spectrometer (TES)/Aura L1B Spectra Special Observation Low Resolution Version 6 data product. TES was an instrument aboard NASA's Aura satellite and was launched from California on July 15, 2004. Data collection for TES is complete. TES Level 1B Spectra data contains radiometric calibrated spectral radiances and their corresponding noise equivalent spectral radiances (NESR). The geolocation, quality and some engineering data were also provided. Each L1B data file contains spectra data composed of the Global Survey Nadir observations from a single TES orbit starting from the South Pole Apex. \r\rA nadir sequence within the TES Global Survey was a fixed number of observations within an orbit for a Global Survey. Prior to April 24, 2005, it consisted of two low resolution scans over the same ground locations. After April 24, 2005, Global Survey data consisted of three low resolution scans. The Nadir standard product consisted of four files, where each file was composed of the Global Survey Nadir observations from one of four focal planes for a single orbit, i.e. 72 orbit sequences. The Global Survey Limb observations used a repeating sequence of filter wheel positions. Special Observations could only be scheduled during the 9 or 10 orbit gaps in the Global Surveys, and were conducted in any of three basic modes: stare, transect, step-and-stare. The mode used depended on the science requirement. A Global Survey consisted of observations along 16 consecutive orbits at the start of a two day cycle, over which 4,608 retrievals were performed (1,152 nadir retrievals and 1,152 retrievals in time ordered sequence for each limb observation). Each observation was the input for retrievals of species volume mixing ratios (VMRs), temperature profiles, surface temperature and other data parameters with associated pressure levels, precision, total error, vertical resolution, total column density and other diagnostic quantities. Each TES Level 2 standard product reported information in a swath format conforming to the HDF-EOS Aura File Format Guidelines. Each Swath object was bounded by the number of observations in a global survey and a predefined set of pressure levels representing slices through the atmosphere. Each standard product could have had a variable number of observations depending upon the Global Survey configuration and whether averaging is employed. Also, missing or bad retrievals were not reported. \r\rThe Global Survey Limb observations use a repeating sequence of filter wheel positions. Special Observations can only be scheduled during the 9 or 10 orbit gaps in the Global Surveys, and are conducted in any of three basic modes: stare, transect, step-and-stare. The mode used depends on the science requirement.",
-            "title": "TES/Aura L1B Spectra Special Observation Low Resolution V006",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAURA%2FTES%2FTL1BSOL_L1.006",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAURA%2FTES%2FTL1BSOL_L1.006",
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
-                    "downloadURL": "https://l0dup05.larc.nasa.gov/public/cgi-bin/DUE/tes_L1B.cgi",
-                    "description": "Report of TES Level 1B Products Available from the ASDC",
                     "@type": "dcat:Distribution",
+                    "description": "Report of TES Level 1B Products Available from the ASDC",
+                    "downloadURL": "https://l0dup05.larc.nasa.gov/public/cgi-bin/DUE/tes_L1B.cgi",
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
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/tes/readme/level_1b_std.pdf",
-                    "description": "TES Level 1B Versioning - Level 1B Standard and Special Observation Products",
                     "@type": "dcat:Distribution",
+                    "description": "TES Level 1B Versioning - Level 1B Standard and Special Observation Products",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/tes/readme/level_1b_std.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's processing history"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/tes/readme/README_L1BReadSoftwareV3.txt",
-                    "description": "Basic IDL Tools for extraction information from TES L1B HDF product files Readme",
                     "@type": "dcat:Distribution",
+                    "description": "Basic IDL Tools for extraction information from TES L1B HDF product files Readme",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/tes/readme/README_L1BReadSoftwareV3.txt",
+                    "mediaType": "text/html",
                     "title": "View this dataset's read me document"
                 },
                 {
-                    "mediaType": "application/x-tar",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/tes/read_software/TES_L1BReadSoftwareV3.tar",
-                    "description": "TES Level 1B Version 3 Read Software Package - Direct File Download (.tar)",
                     "@type": "dcat:Distribution",
+                    "description": "TES Level 1B Version 3 Read Software Package - Direct File Download (.tar)",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/tes/read_software/TES_L1BReadSoftwareV3.tar",
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
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1386637578-LARC",
-                    "description": "Earthdata Search for TL1BSOL_6 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for TL1BSOL_6 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1386637578-LARC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/AURA/TES/TL1BSOL_L1.006",
-                    "description": "DOI data set landing page for TL1BSOL_6",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for TL1BSOL_6",
+                    "downloadURL": "https://doi.org/10.5067/AURA/TES/TL1BSOL_L1.006",
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
-                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/TES/TL1BSOL.006/contents.html",
-                    "description": "OPeNDAP data access for TL1BSOL_6",
                     "@type": "dcat:Distribution",
+                    "description": "OPeNDAP data access for TL1BSOL_6",
+                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/TES/TL1BSOL.006/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/TES/TL1BSOL.006/",
-                    "description": "ASDC Direct Data Download for TL1BSOL_6",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for TL1BSOL_6",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/TES/TL1BSOL.006/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 }
             ],
+            "identifier": "C1386637578-LARC",
+            "issued": "2015-08-27",
+            "keyword": [
+                "spectral/engineering",
+                "infrared wavelengths",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/AURA/TES/TL1BSOL_L1.006",
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
+            "title": "TES/Aura L1B Spectra Special Observation Low Resolution V006"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.7265/N5SB43P0",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Recurring Spring Leads and Landfast Ice in the Beaufort and Chukchi Seas, 1993-2004, Version 1. Version 1. Archived by National Aeronautics and Space Administration, U.S. Government, National Snow and Ice Data Center. https://doi.org/10.7265/N5SB43P0.",
-            "issued": "1993-12-09",
-            "temporal": "1993-12-09T00:00:00Z/2004-07-29T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2004-07-29",
-            "keyword": [
-                "earth science",
-                "oceans",
-                "cryosphere",
-                "sea ice"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Allison Gaylord",
                 "hasEmail": "mailto:NunaTech@usa.net"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NSIDC"
-            },
-            "identifier": "C1386206510-NSIDCV0",
             "description": "This data set contains information on recurring spring leads and landfast ice extent in the Beaufort and Chukchi Seas. This data set maps and documents the spatial and temporal distribution of recurring leads and landfast ice in this area spanning 1993 through 2004 and are based on visible and infrared Advanced Very High Resolution Radiometer (AVHRR) data.",
-            "title": "Recurring Spring Leads and Landfast Ice in the Beaufort and Chukchi Seas, 1993-2004, Version 1",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.7265%2FN5SB43P0",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.7265%2FN5SB43P0",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/forms/G02173_or.html?major_version=1",
-                    "description": "Direct download, with optional registration page.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download, with optional registration page.",
+                    "downloadURL": "https://nsidc.org/forms/G02173_or.html?major_version=1",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/forms/G02173_or.html?major_version=1",
-                    "description": "Direct download, with optional registration page.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download, with optional registration page.",
+                    "downloadURL": "https://nsidc.org/forms/G02173_or.html?major_version=1",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/forms/G02173_or.html?major_version=1",
-                    "description": "Direct download, with optional registration page.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download, with optional registration page.",
+                    "downloadURL": "https://nsidc.org/forms/G02173_or.html?major_version=1",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/forms/G02173_or.html?major_version=1",
-                    "description": "Direct download, with optional registration page.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download, with optional registration page.",
+                    "downloadURL": "https://nsidc.org/forms/G02173_or.html?major_version=1",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/forms/G02173_or.html?major_version=1",
-                    "description": "Direct download, with optional registration page.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download, with optional registration page.",
+                    "downloadURL": "https://nsidc.org/forms/G02173_or.html?major_version=1",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/forms/G02173_or.html?major_version=1",
-                    "description": "Direct download, with optional registration page.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download, with optional registration page.",
+                    "downloadURL": "https://nsidc.org/forms/G02173_or.html?major_version=1",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/forms/G02173_or.html?major_version=1",
-                    "description": "Direct download, with optional registration page.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download, with optional registration page.",
+                    "downloadURL": "https://nsidc.org/forms/G02173_or.html?major_version=1",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/forms/G02173_or.html?major_version=1",
-                    "description": "Direct download, with optional registration page.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download, with optional registration page.",
+                    "downloadURL": "https://nsidc.org/forms/G02173_or.html?major_version=1",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.7265/N5SB43P0",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.7265/N5SB43P0",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.7265/N5SB43P0",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.7265/N5SB43P0",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C1386206510-NSIDCV0",
+            "issued": "1993-12-09",
+            "keyword": [
+                "earth science",
+                "oceans",
+                "cryosphere",
+                "sea ice"
+            ],
+            "landingPage": "https://doi.org/10.7265/N5SB43P0",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2004-07-29",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NSIDC"
+            },
             "spatial": "-164.08084 68.48204 -129.87714 73.95769",
+            "temporal": "1993-12-09T00:00:00Z/2004-07-29T23:59:59.999Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Recurring Spring Leads and Landfast Ice in the Beaufort and Chukchi Seas, 1993-2004, Version 1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=LP-L-ENG-6-ATTITUDE-V1.0",
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
+            "description": "The Lunar Prospector attitude data set consists of values for the spacecraft spin rate and spin axis orientation (attitude) as a function of time. These values are determined from spacecraft attitude data (sun and limb crossing sensors) and ephemeris data. Spacecraft orientations are given as right ascension and declination of the spacecraft spin axis in the Mean-of-J2000 Ecliptic reference frame. The attitude data set consists of a single, cumulative file for the entire mission. Records are added to this file following each significant change in either the spin rate or spin axis orientation. The spacecraft spin rates and attitudes in this data set are orbit averages. The instantaneous spin rate can be determined from the sun pulse data set. The instantaneous spin rate varies as the spacecraft passes into and out of the Moon's shadow and after each spacecraft maneuver. Generally, an attitude record is included for times immediately before and after each maneuver.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.lp-l-eng-6-attitude-v1.0_t4qb-79i2",
+            "issued": "2021-05-21",
+            "keyword": [
+                "moon",
+                "lunar prospector"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=LP-L-ENG-6-ATTITUDE-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.lp-l-eng-6-attitude-v1.0_t4qb-79i2",
-            "description": "The Lunar Prospector attitude data set consists of values for the spacecraft spin rate and spin axis orientation (attitude) as a function of time. These values are determined from spacecraft attitude data (sun and limb crossing sensors) and ephemeris data. Spacecraft orientations are given as right ascension and declination of the spacecraft spin axis in the Mean-of-J2000 Ecliptic reference frame. The attitude data set consists of a single, cumulative file for the entire mission. Records are added to this file following each significant change in either the spin rate or spin axis orientation. The spacecraft spin rates and attitudes in this data set are orbit averages. The instantaneous spin rate can be determined from the sun pulse data set. The instantaneous spin rate varies as the spacecraft passes into and out of the Moon's shadow and after each spacecraft maneuver. Generally, an attitude record is included for times immediately before and after each maneuver.",
-            "title": "LP MOON SPACECRAFT ATTITUDE V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "LP MOON SPACECRAFT ATTITUDE V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.nasa.gov/d/t4t5-wb6u",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2018-06-25",
-            "temporal": "1977-01-01/1996-01-01",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
-            "keyword": [
-                "space science",
-                "wise",
-                "geography",
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
-            "identifier": "NASA-0000037__16",
+            "describedBy": "http://www.lpi.usra.edu/resources/gc/gcreadme.html",
             "description": "Planetary nomenclature, like terrestrial nomenclature, is used to uniquely identify a feature on the surface of a planet or satellite so that the feature can be easily located, described, and discussed. This gazetteer contains detailed information about all names of topographic and albedo features on planets and satellites (and some planetary ring and ring-gap systems) that the International Astronomical Union (IAU) has named and approved from its founding in 1919 through the present time.",
-            "title": "Gateway to Astronaut Photography of Earth",
-            "programCode": [
-                "026:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -1393026,350 +1393008,370 @@
                     "mediaType": "text/html"
                 }
             ],
-            "describedBy": "http://www.lpi.usra.edu/resources/gc/gcreadme.html",
-            "accrualPeriodicity": "irregular"
+            "identifier": "NASA-0000037__16",
+            "issued": "2018-06-25",
+            "keyword": [
+                "space science",
+                "wise",
+                "geography",
+                "nen"
+            ],
+            "landingPage": "https://data.nasa.gov/d/t4t5-wb6u",
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
-            "landingPage": "https://c3.nasa.gov/dashlink/resources/663/",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2012-12-04",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
-            "keyword": [
-                "dashlink",
-                "ames",
-                "nasa"
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
-            "identifier": "DASHLINK_663",
             "description": "The following zip files contain individual flight recorded data in Matlab file format. There are 186 parameters each with a data structure that contains the following:\r\n\r\n<pre>\r\n-sensor recordings\r\n-sampling rate\r\n-units\r\n-parameter description\r\n-parameter ID\r\n</pre>",
-            "title": "Flight Data For Tail 686",
-            "programCode": [
-                "026:029"
-            ],
             "distribution": [
                 {
-                    "mediaType": "application/zip",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Tail_686_1.zip",
-                    "description": "Tail 686 Set 1",
                     "@type": "dcat:Distribution",
+                    "description": "Tail 686 Set 1",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Tail_686_1.zip",
+                    "mediaType": "application/zip",
                     "title": "Tail_686_1.zip"
                 },
                 {
-                    "mediaType": "application/zip",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Tail_686_2.zip",
-                    "description": "Tail 686 Set 2",
                     "@type": "dcat:Distribution",
+                    "description": "Tail 686 Set 2",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Tail_686_2.zip",
+                    "mediaType": "application/zip",
                     "title": "Tail_686_2.zip"
                 },
                 {
-                    "mediaType": "application/zip",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Tail_686_3.zip",
-                    "description": "Tail_686 Set 3\n",
                     "@type": "dcat:Distribution",
+                    "description": "Tail_686 Set 3\n",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Tail_686_3.zip",
+                    "mediaType": "application/zip",
                     "title": "Tail_686_3.zip"
                 },
                 {
-                    "mediaType": "application/zip",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Tail_686_4.zip",
-                    "description": "Tail_686 Set 4\n",
                     "@type": "dcat:Distribution",
+                    "description": "Tail_686 Set 4\n",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Tail_686_4.zip",
+                    "mediaType": "application/zip",
                     "title": "Tail_686_4.zip"
                 },
                 {
-                    "mediaType": "application/zip",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Tail_686_5.zip",
-                    "description": "Tail_686 Set 5\n",
                     "@type": "dcat:Distribution",
+                    "description": "Tail_686 Set 5\n",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Tail_686_5.zip",
+                    "mediaType": "application/zip",
                     "title": "Tail_686_5.zip"
                 },
                 {
-                    "mediaType": "application/zip",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Tail_686_6.zip",
-                    "description": "Tail_686 Set 6\n",
                     "@type": "dcat:Distribution",
+                    "description": "Tail_686 Set 6\n",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Tail_686_6.zip",
+                    "mediaType": "application/zip",
                     "title": "Tail_686_6.zip"
                 },
                 {
-                    "mediaType": "application/zip",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Tail_686_7.zip",
-                    "description": "Tail_686 Set 7\n",
                     "@type": "dcat:Distribution",
+                    "description": "Tail_686 Set 7\n",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Tail_686_7.zip",
+                    "mediaType": "application/zip",
                     "title": "Tail_686_7.zip"
                 },
                 {
-                    "mediaType": "application/zip",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Tail_686_8.zip",
-                    "description": "Tail_686 Set 8\n",
                     "@type": "dcat:Distribution",
+                    "description": "Tail_686 Set 8\n",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Tail_686_8.zip",
+                    "mediaType": "application/zip",
                     "title": "Tail_686_8.zip"
                 },
                 {
-                    "mediaType": "application/zip",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Tail_686_9.zip",
-                    "description": "Tail_686 Set 9\n",
                     "@type": "dcat:Distribution",
+                    "description": "Tail_686 Set 9\n",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Tail_686_9.zip",
+                    "mediaType": "application/zip",
                     "title": "Tail_686_9.zip"
                 }
             ],
-            "accrualPeriodicity": "irregular"
+            "identifier": "DASHLINK_663",
+            "issued": "2012-12-04",
+            "keyword": [
+                "dashlink",
+                "ames",
+                "nasa"
+            ],
+            "landingPage": "https://c3.nasa.gov/dashlink/resources/663/",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:029"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Dashlink"
+            },
+            "title": "Flight Data For Tail 686"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC1-0512-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 1 phase 2014-11-20 to 2015-03-10. It is a Global Gravity measurement at the comet 67P and covers the time 2014-12-29T00:09:25.000 to 2014-12-29T12:10:10.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc1-0512-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC1-0512-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc1-0512-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 1 phase 2014-11-20 to 2015-03-10. It is a Global Gravity measurement at the comet 67P and covers the time 2014-12-29T00:09:25.000 to 2014-12-29T12:10:10.000.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 1 0512 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 1 0512 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=CLEM1-L-LIDAR-5-TOPO-V1.0",
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
-                "deep space program science experiment",
-                "moon"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "The Clementine spacecraft included a Light Imaging Detection and Ranging (LIDAR) instrument. The LIDAR instrument measured the slant range from the spacecraft to the lunar surface. This data set contains topography data derived from the LIDAR measurements.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.clem1-l-lidar-5-topo-v1.0_t4x6-c373",
+            "issued": "2018-06-26",
+            "keyword": [
+                "deep space program science experiment",
+                "moon"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=CLEM1-L-LIDAR-5-TOPO-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.clem1-l-lidar-5-topo-v1.0_t4x6-c373",
-            "description": "The Clementine spacecraft included a Light Imaging Detection and Ranging (LIDAR) instrument. The LIDAR instrument measured the slant range from the spacecraft to the lunar surface. This data set contains topography data derived from the LIDAR measurements.",
-            "title": "CLEM1 LUNAR TOPOGRAPHY V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "CLEM1 LUNAR TOPOGRAPHY V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/VIIRS/VJ109A1.002",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Eric Vermote, Belen Franch, Martin Claverie. 2023-06-12. VIIRS/JPSS1 Surface Reflectance 8-Day L3 Global 1km SIN Grid V002. Sioux Falls, South Dakota, USA. Archived by National Aeronautics and Space Administration, U.S. Government, NASA EOSDIS Land Processes Distributed Active Archive Center. https://doi.org/10.5067/VIIRS/VJ109A1.002. https://doi.org/10.5067/VIIRS/VJ109A1.002. This data set was provided by the NASA/NOAA NPP Project. The DOI landing page provides citations in APA and Chicago styles.\r\n.",
-            "issued": "2023-06-12",
-            "temporal": "2018-01-01T00:00:00Z/2024-06-03T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-06-12",
-            "keyword": [
-                "earth science",
-                "surface radiative properties",
-                "land surface"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Eric Vermote",
                 "hasEmail": "mailto:eric.f.vermote@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "LP DAAC"
-            },
-            "identifier": "C2501959919-LPCLOUD",
-            "description": "The 8-day Visible Infrared Imaging Radiometer Suite (VIIRS) (https://lpdaac.usgs.gov/dataset_discovery/viirs) surface reflectance (VJ109A1) Version 2 composite product provides an estimate of land surface reflectance from the NOAA-20 VIIRS sensor for nine moderate resolution bands (M1 - M5, M7, M8, M10, M11) at nominal 1 kilometer resolution (~926 meter). The 1 kilometer dataset is derived through resampling the native 750 meter VIIRS resolution in the Level 2 input product. The data are corrected for atmospheric conditions such as the effects of molecular gases, including ozone and water vapor, and for the effects of atmospheric aerosols. Each pixel represents the best possible Level 2G observation during an 8-day period that is selected on the basis of high observation coverage, low sensor angle, the absence of clouds or cloud shadow, and aerosol loading. Included in the product along with the nine reflectance bands are day of year, reflectance band quality, control, reflectance state quality assurance, relative azimuth angle, sensor zenith angle, and solar zenith angle layers.",
-            "release-place": "Sioux Falls, South Dakota, USA",
-            "graphic-preview-description": "Browse image for Earthdata Search",
             "creator": "Eric Vermote, Belen Franch, Martin Claverie",
-            "title": "VIIRS/JPSS1 Surface Reflectance 8-Day L3 Global 1km SIN Grid V002",
-            "graphic-preview-file": "https://cmr.earthdata.nasa.gov/browse-scaler/browse_images/granules/G2706715309-LPCLOUD?h=85&w=85",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The 8-day Visible Infrared Imaging Radiometer Suite (VIIRS) (https://lpdaac.usgs.gov/dataset_discovery/viirs) surface reflectance (VJ109A1) Version 2 composite product provides an estimate of land surface reflectance from the NOAA-20 VIIRS sensor for nine moderate resolution bands (M1 - M5, M7, M8, M10, M11) at nominal 1 kilometer resolution (~926 meter). The 1 kilometer dataset is derived through resampling the native 750 meter VIIRS resolution in the Level 2 input product. The data are corrected for atmospheric conditions such as the effects of molecular gases, including ozone and water vapor, and for the effects of atmospheric aerosols. Each pixel represents the best possible Level 2G observation during an 8-day period that is selected on the basis of high observation coverage, low sensor angle, the absence of clouds or cloud shadow, and aerosol loading. Included in the product along with the nine reflectance bands are day of year, reflectance band quality, control, reflectance state quality assurance, relative azimuth angle, sensor zenith angle, and solar zenith angle layers.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FVIIRS%2FVJ109A1.002",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FVIIRS%2FVJ109A1.002",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "application/x-hdf",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=C2501959919-LPCLOUD",
-                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=C2501959919-LPCLOUD",
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
-                    "downloadURL": "https://doi.org/10.5067/VIIRS/VJ109A1.002",
-                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
+                    "downloadURL": "https://doi.org/10.5067/VIIRS/VJ109A1.002",
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
-                    "downloadURL": "https://lpdaac.usgs.gov/documents/1657/VNP09_User_Guide_V2.pdf",
-                    "description": "The technical information in the Version 2.0 User's Guide enables users to interpret and use the data products.",
                     "@type": "dcat:Distribution",
+                    "description": "The technical information in the Version 2.0 User's Guide enables users to interpret and use the data products.",
+                    "downloadURL": "https://lpdaac.usgs.gov/documents/1657/VNP09_User_Guide_V2.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://lpdaac.usgs.gov/documents/122/VNP09_ATBD.pdf",
-                    "description": "The ATBD provides physical theory and mathematical procedures for the calculations used to produce the data products.",
                     "@type": "dcat:Distribution",
+                    "description": "The ATBD provides physical theory and mathematical procedures for the calculations used to produce the data products.",
+                    "downloadURL": "https://lpdaac.usgs.gov/documents/122/VNP09_ATBD.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's algorithm theoretical basis document"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/browse-scaler/browse_images/granules/G2706715309-LPCLOUD?h=85&w=85",
-                    "description": "Browse image for Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse image for Earthdata Search",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/browse-scaler/browse_images/granules/G2706715309-LPCLOUD?h=85&w=85",
+                    "mediaType": "text/html",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://viirsland.gsfc.nasa.gov/Val/LSR_Val.html",
-                    "description": "Validation at stage 3 has been achieved for the VIIRS surface reflectance product suite.",
                     "@type": "dcat:Distribution",
+                    "description": "Validation at stage 3 has been achieved for the VIIRS surface reflectance product suite.",
+                    "downloadURL": "https://viirsland.gsfc.nasa.gov/Val/LSR_Val.html",
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
+            "graphic-preview-file": "https://cmr.earthdata.nasa.gov/browse-scaler/browse_images/granules/G2706715309-LPCLOUD?h=85&w=85",
+            "identifier": "C2501959919-LPCLOUD",
+            "issued": "2023-06-12",
+            "keyword": [
+                "earth science",
+                "surface radiative properties",
+                "land surface"
+            ],
+            "landingPage": "https://doi.org/10.5067/VIIRS/VJ109A1.002",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2023-06-12",
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
+            "title": "VIIRS/JPSS1 Surface Reflectance 8-Day L3 Global 1km SIN Grid V002"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-5-ESC3-67P-M19-GEO-V1.0",
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
+            "description": "This CODMAC level 5 data set contains derived data products that include pixel-precise georeferencing information, acquired by the OSIRIS Narrow Angle Camera on the Rosetta spacecraft during the COMET ESCORT 3 mission phase, covering the period from 2015-07-28T23:25:00.000 to 2015-08-25T23:24:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V1.0 is the first version of this dataset: Lien corrected dataset after October 2018 PSA/PDS external peer review.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-5-esc3-67p-m19-geo-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-5-ESC3-67P-M19-GEO-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-5-esc3-67p-m19-geo-v1.0",
-            "description": "This CODMAC level 5 data set contains derived data products that include pixel-precise georeferencing information, acquired by the OSIRIS Narrow Angle Camera on the Rosetta spacecraft during the COMET ESCORT 3 mission phase, covering the period from 2015-07-28T23:25:00.000 to 2015-08-25T23:24:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V1.0 is the first version of this dataset: Lien corrected dataset after October 2018 PSA/PDS external peer review.",
-            "title": "ROSETTA-ORBITER 67P OSINAC 5 ESC3-MTP019 DDR-GEO V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P OSINAC 5 ESC3-MTP019 DDR-GEO V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-X-OSIWAC-2-CR5-CHECKOUT-V2.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This CODMAC level 2 data set contains uncalibrated image data in DN unit,  acquired by the OSIRIS Wide Angle Camera on the Rosetta spacecraft  during the CRUISE 5 mission phase, covering the period  from 2009-12-14T00:00:00.000 to 2010-05-16T23:59:59.000. The prime objective was commissioning / calibration. Several targets of opportunity were observed, but none of them is identifiable as prime target. This version V2.0 supersedes previous deliveries of the same dataset with the following changes since the last version: Reprocessed dataset after October 2018 PSA/PDS external peer review.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-x-osiwac-2-cr5-checkout-v2.0",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2021-05-21",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "vega",
                 "international rosetta mission",
@@ -1393379,849 +1393381,856 @@
                 "dark",
                 "bias"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-X-OSIWAC-2-CR5-CHECKOUT-V2.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-x-osiwac-2-cr5-checkout-v2.0",
-            "description": "This CODMAC level 2 data set contains uncalibrated image data in DN unit,  acquired by the OSIRIS Wide Angle Camera on the Rosetta spacecraft  during the CRUISE 5 mission phase, covering the period  from 2009-12-14T00:00:00.000 to 2010-05-16T23:59:59.000. The prime objective was commissioning / calibration. Several targets of opportunity were observed, but none of them is identifiable as prime target. This version V2.0 supersedes previous deliveries of the same dataset with the following changes since the last version: Reprocessed dataset after October 2018 PSA/PDS external peer review.",
-            "title": "ROSETTA-ORBITER CHECKOUT OSIWAC 2 CR5 EDR V2.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER CHECKOUT OSIWAC 2 CR5 EDR V2.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/AIRCRAFT/AIRMSPI/PODEX/RADIANCE/ELLIPSOID_V005",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2013-07-02. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/AIRCRAFT/AIRMSPI/PODEX/RADIANCE/ELLIPSOID_V005.",
-            "issued": "2017-07-18",
-            "temporal": "2013-01-14T00:00:00Z/2013-02-06T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2018-07-23",
-            "keyword": [
-                "ultraviolet wavelengths",
-                "visible wavelengths",
-                "earth science",
-                "spectral/engineering"
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
-            "identifier": "C1461089729-LARC_ASDC",
             "description": "AirMSPI_PODEX_Ellipsoid-projected_Georegistered_Radiance_Data are AirMSPI Ellipsoid-projected georegistered radiance product acquired during the NASA Polarimeter Definition Experiment (PODEX) flight campaign.\r\n\r\nAirMSPI Level 1B2 products contain radiometric and polarimetric images of clouds, aerosols, and the surface of the Earth. In particular, products contain map-projected data at 8 wavelengths: 355, 380, 445, 470, 555, 660, 865, and 935 nm. The data products include radiance, time, solar zenith, solar azimuth, view zenith, and view azimuth for all spectral bands. Wavelengths for which polarization information is available (470, 660, and 865 nm) also include the Stokes parameters Q and U, as well as degree of linear polarization (DOLP) and angle of linear polarization (AOLP). Q, U, and AOLP are reported relative to both the scattering and view meridian planes. Files are distributed in HDF-EOS-5 format.\r\n\r\nThis release of AirMSPI data contains all targets acquired during the Polarimeter Definition Experiment (PODEX) flight campaign. PODEX was based out of NASA\u2019s Armstrong (formerly Dryden) Flight Research Center in Palmdale, CA, and focused on clouds and aerosols in and around California. AirMSPI data were acquired from January 14 through February 6, 2013.",
-            "title": "AirMSPI version 5 ellipsoid-projected georegistered radiance product acquired during the NASA PODEX flight campaign January-February 2013",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAIRCRAFT%2FAIRMSPI%2FPODEX%2FRADIANCE%2FELLIPSOID_V005",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAIRCRAFT%2FAIRMSPI%2FPODEX%2FRADIANCE%2FELLIPSOID_V005",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1461089729-LARC_ASDC",
-                    "description": "Earthdata Search for AirMSPI_PODEX_Ellipsoid-projected_Georegistered_Radiance_Data_5 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for AirMSPI_PODEX_Ellipsoid-projected_Georegistered_Radiance_Data_5 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1461089729-LARC_ASDC",
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
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/airmspi/quality_summaries/AirMSPI-Data_Quality_PODEX_V005.pdf",
-                    "description": "AirMSPI Data Quality Statement: PODEX Campaign (January - February 2013)",
                     "@type": "dcat:Distribution",
+                    "description": "AirMSPI Data Quality Statement: PODEX Campaign (January - February 2013)",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/airmspi/quality_summaries/AirMSPI-Data_Quality_PODEX_V005.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's data quality document"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/airmspi/guide/AirMSPI_L1B2_DPS.20180205.pdf",
-                    "description": "Data Product Specification for the AirMSPI Level 1B2 Products (V005)",
                     "@type": "dcat:Distribution",
+                    "description": "Data Product Specification for the AirMSPI Level 1B2 Products (V005)",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/airmspi/guide/AirMSPI_L1B2_DPS.20180205.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's product usage"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://airbornescience.jpl.nasa.gov/instruments/airmspi",
-                    "description": "NASA JPL Airborne Instrument AirMSPI Overview",
                     "@type": "dcat:Distribution",
+                    "description": "NASA JPL Airborne Instrument AirMSPI Overview",
+                    "downloadURL": "https://airbornescience.jpl.nasa.gov/instruments/airmspi",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://airbornescience.nasa.gov/instrument/AirMSPI",
-                    "description": "NASA Airborne Science Program Instrumentation page for AirMSPI",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Airborne Science Program Instrumentation page for AirMSPI",
+                    "downloadURL": "https://airbornescience.nasa.gov/instrument/AirMSPI",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
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
-                    "downloadURL": "https://doi.org/10.5067/AIRCRAFT/AIRMSPI/PODEX/RADIANCE/ELLIPSOID_V005",
-                    "description": "DOI data set landing page for AirMSPI_PODEX_Ellipsoid-projected_Georegistered_Radiance_Data_5",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for AirMSPI_PODEX_Ellipsoid-projected_Georegistered_Radiance_Data_5",
+                    "downloadURL": "https://doi.org/10.5067/AIRCRAFT/AIRMSPI/PODEX/RADIANCE/ELLIPSOID_V005",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/airmspi/guide/DPS-AirMSPI_2013_23Sep2013.pdf",
-                    "description": "Data Product Specification for the AirMSPILevel 1B2 Products",
                     "@type": "dcat:Distribution",
+                    "description": "Data Product Specification for the AirMSPILevel 1B2 Products",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/airmspi/guide/DPS-AirMSPI_2013_23Sep2013.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's product usage"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/airmspi/guide/USER-AirMSPI_2013_April2013.pdf",
-                    "description": "User Guide for the AirMSPI Level 1B2 Products, April 27, 2013",
                     "@type": "dcat:Distribution",
+                    "description": "User Guide for the AirMSPI Level 1B2 Products, April 27, 2013",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/airmspi/guide/USER-AirMSPI_2013_April2013.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/project/AIRMSPI",
-                    "description": "ASDC Data and Information for AirMSPI",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Data and Information for AirMSPI",
+                    "downloadURL": "https://asdc.larc.nasa.gov/project/AIRMSPI",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
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
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/AirMSPI/PODEX/ER2_GRP_ELLIPSOID/V005/",
-                    "description": "ASDC Direct Data Download for AirMSPI_PODEX_Ellipsoid-projected_Georegistered_Radiance_Data_5",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for AirMSPI_PODEX_Ellipsoid-projected_Georegistered_Radiance_Data_5",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/AirMSPI/PODEX/ER2_GRP_ELLIPSOID/V005/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/AirMSPI/PODEX/ER2_GRP_ELLIPSOID/V005/contents.html",
-                    "description": "OPeNDAP data access for AirMSPI_PODEX_Ellipsoid-projected_Georegistered_Radiance_Data_5",
                     "@type": "dcat:Distribution",
+                    "description": "OPeNDAP data access for AirMSPI_PODEX_Ellipsoid-projected_Georegistered_Radiance_Data_5",
+                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/AirMSPI/PODEX/ER2_GRP_ELLIPSOID/V005/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 }
             ],
+            "identifier": "C1461089729-LARC_ASDC",
+            "issued": "2017-07-18",
+            "keyword": [
+                "ultraviolet wavelengths",
+                "visible wavelengths",
+                "earth science",
+                "spectral/engineering"
+            ],
+            "landingPage": "https://doi.org/10.5067/AIRCRAFT/AIRMSPI/PODEX/RADIANCE/ELLIPSOID_V005",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2018-07-23",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/LARC/SD/ASDC"
+            },
             "spatial": "<?xml version=\"1.0\" encoding=\"UTF-8\"?><gml:Polygon xmlns:gml=\"http://www.opengis.net/gml/3.2\" srsName=\"EPSG:9825\"><gml:outerBoundaryIs><gml:LinearRing><gml:posList>28.0 -130.0 28.0 -114.0 42.5 -114.0 42.5 -130.0 28.0 -130.0</gml:posList></gml:LinearRing></gml:outerBoundaryIs><gml:innerBoundaryIs></gml:innerBoundaryIs></gml:Polygon>",
+            "temporal": "2013-01-14T00:00:00Z/2013-02-06T23:59:59.999Z",
             "theme": [
                 "AIRMSPI",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "AirMSPI version 5 ellipsoid-projected georegistered radiance product acquired during the NASA PODEX flight campaign January-February 2013"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-E-OSIWAC-2-EAR1-EARTHSWINGBY1-V1.4",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This data set contains images acquired by the OSIRIS Wide Angle Camera during the EARTH SWING-BY 1 mission phase",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-e-osiwac-2-ear1-earthswingby1-v1.4_t53z-u3rs",
             "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "dark",
                 "international rosetta mission",
                 "calibration"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-E-OSIWAC-2-EAR1-EARTHSWINGBY1-V1.4",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-e-osiwac-2-ear1-earthswingby1-v1.4_t53z-u3rs",
-            "description": "This data set contains images acquired by the OSIRIS Wide Angle Camera during the EARTH SWING-BY 1 mission phase",
-            "title": "ROSETTA-ORBITER EARTH SWING-BY 1 OSIWAC 2 EDR V1.4",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "ROSETTA-ORBITER EARTH SWING-BY 1 OSIWAC 2 EDR V1.4"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/XQV4UWX1XJ8Q",
             "citation": "NASA/GSFC. 2021-06-18. TIROS3L1FMRT. Version 001. TIROS-3 Medium-Resolution Scanning Radiometer Level 1 Final Meteorological Radiation Data V001. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/XQV4UWX1XJ8Q. https://disc.gsfc.nasa.gov/datacollection/TIROS3L1FMRT_001.html. Digital Science Data.",
-            "issued": "2021-04-01",
-            "temporal": "1961-07-12T00:00:00Z/1961-09-30T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2021-04-01",
-            "keyword": [
-                "earth science",
-                "infrared wavelengths",
-                "spectral/engineering",
-                "visible wavelengths"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "JAMES JOHNSON",
                 "hasEmail": "mailto:James.Johnson@nasa.gov"
             },
+            "creator": "NASA/GSFC",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C2071514571-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "TIROS-3 Medium-Resolution Scanning Radiometer Level 1 Final Meteorological Radiation Data (FMRT) product contains radiances expressed in five infrared/visible wavelength regions, expressed in either equivalent blackbody temperature (IR channels 1, 2 and 4) or effective radiant emmitance (visible channels 3 and 5). The data will trace an elliptical, parabolic, or hyperbolic pattern on the ground due to the rotating of the instrument about the satellite spin axis. There is one orbit per file. The data were originally written on IBM 7094 machines, and these have been recovered from magnetic tapes, referred to as the Final Meteorological Radiation Tapes (FMRT). The data are archived in their original IBM 36-bit word proprietary format, also referred to as a binary TAP file.\n\nThe TIROS-3 satellite was successfully launched on July 12, 1961. The Medium-Resolution Scanning Radiometer experiment returned data for about two and a half months. A previous instrument flew on TIROS-2 and two follow-on instruments were flown on TIROS-4 and -7. Response characteristics of all channels degraded rapidly after launch. The greatest uncertainty in the radiation measurements is due to the apparent shift in the zero radiation level. Data are usable for channels 1, 2,  3, 4, and 5 up to orbits 118, 875, 875, 130 and 300, respectively. The instrument is a five channel radiometer with a 55 km footprint at nadir with the following characteristics:\n\nChannel 1: 6.0 to 6.5 microns - water vapor absorption\nChannel 2: 8.0 to 12.0 microns - atmospheric window\nChannel 3: 0.2 to 6.0 microns - reflected solar radiation\nChannel 4: 8.0 to 30 - terrestial radiation\nChannel 5: 0.55 to 0.75 microns - response to the TV system\n\nThe Principal Investigator for these data was Joseph D. Barksdale from NASA Goddard Space Flight Center. This product was previously available from the NSSDC with the identifier ESAD-00141 (old id 61-017A-03A).",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "TIROS3L1FMRT",
-            "creator": "NASA/GSFC",
-            "title": "TIROS-3 Medium-Resolution Scanning Radiometer Level 1 Final Meteorological Radiation Data V001 (TIROS3L1FMRT) at GES DISC",
-            "graphic-preview-description": "TIROS-3 L1 FMRT data showing data coverage from the scanning radiometer channel 2 (8-12 microns) for the first orbit on July 12, 1961.",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/TIROS3L1FMRT_Sample.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FXQV4UWX1XJ8Q",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FXQV4UWX1XJ8Q",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/TIROS3L1FMRT_Sample.png",
-                    "description": "TIROS-3 L1 FMRT data showing data coverage from the scanning radiometer channel 2 (8-12 microns) for the first orbit on July 12, 1961.",
                     "@type": "dcat:Distribution",
+                    "description": "TIROS-3 L1 FMRT data showing data coverage from the scanning radiometer channel 2 (8-12 microns) for the first orbit on July 12, 1961.",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/TIROS3L1FMRT_Sample.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/TIROS/TIROS3L1FMRT.001/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/TIROS/TIROS3L1FMRT.001/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=TIROS3L1FMRT",
-                    "description": "Use the Earthdata Search Client to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search Client to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=TIROS3L1FMRT",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/TIROS/TIROS3L1FMRT.001/doc/README.TIROS3FMRT.001.pdf",
-                    "description": "README Document",
                     "@type": "dcat:Distribution",
+                    "description": "README Document",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/TIROS/TIROS3L1FMRT.001/doc/README.TIROS3FMRT.001.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's read me document"
                 },
                 {
-                    "mediaType": "application/zip",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/repository/Mission/Nimbus/3.3_Product_Documentation/3.3.5_Product_Quality/TIROS_III_Radiation_Data_Users_Manual.zip",
-                    "description": "TIROS III Radiation Data Users' Manual",
                     "@type": "dcat:Distribution",
+                    "description": "TIROS III Radiation Data Users' Manual",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/repository/Mission/Nimbus/3.3_Product_Documentation/3.3.5_Product_Quality/TIROS_III_Radiation_Data_Users_Manual.zip",
+                    "mediaType": "application/zip",
                     "title": "View this dataset's user's guide"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/repository/Mission/Nimbus/3.3_Product_Documentation/3.3.5_Product_Quality/TIROS_3_Radiation_Data_Catalog.pdf",
-                    "description": "TIROS III Radiation Data Catalog",
                     "@type": "dcat:Distribution",
+                    "description": "TIROS III Radiation Data Catalog",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/repository/Mission/Nimbus/3.3_Product_Documentation/3.3.5_Product_Quality/TIROS_3_Radiation_Data_Catalog.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TIROS/Tiros_Inventory.xlsx",
-                    "description": "TIROS Inventory",
                     "@type": "dcat:Distribution",
+                    "description": "TIROS Inventory",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TIROS/Tiros_Inventory.xlsx",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "graphic-preview-description": "TIROS-3 L1 FMRT data showing data coverage from the scanning radiometer channel 2 (8-12 microns) for the first orbit on July 12, 1961.",
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/TIROS3L1FMRT_Sample.png",
+            "identifier": "C2071514571-GES_DISC",
+            "issued": "2021-04-01",
+            "keyword": [
+                "earth science",
+                "infrared wavelengths",
+                "spectral/engineering",
+                "visible wavelengths"
+            ],
+            "landingPage": "https://doi.org/10.5067/XQV4UWX1XJ8Q",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2021-04-01",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
+            },
+            "release-place": "Greenbelt, MD, USA",
+            "series-name": "TIROS3L1FMRT",
             "spatial": "-180.0 -66.0 180.0 66.0",
+            "temporal": "1961-07-12T00:00:00Z/1961-09-30T23:59:59.999Z",
             "theme": [
                 "TIROS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "TIROS-3 Medium-Resolution Scanning Radiometer Level 1 Final Meteorological Radiation Data V001 (TIROS3L1FMRT) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/146",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Gilmanov, T.G. 2015. NPP Grassland: Khomutov, Ukraine, 1948 and 1967-1970, R1. ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/146",
-            "issued": "2015-05-26",
-            "temporal": "1948-07-04T00:00:00Z/1972-12-31T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-08-17",
-            "keyword": [
-                "ecological dynamics",
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
-            "identifier": "C2751936985-ORNL_CLOUD",
             "description": "This data set provides two data files in text format (.txt). One file contains biomass measurements made in 1948 and between 1967 and 1970 for a humid temperate steppe in the Khomutovskaya Steppe Nature Reserve in the Donezk Region of Ukraine. The second file contains monthly and annual climate data for the study site for the period 1955-1972.Biomass measurements were made once in July of 1948 and biweekly to monthly during the growing season (April-August/September) from 1967 to 1970 at the permanent Khomutovskaya research station. ANPP was calculated for each sampling date and cumulatively over the four years, 1967-1970. Averaged over the time series, above-ground live phytomass, standing dead, and litter biomass were estimated to be 340, 90, and 240 g/m2 (dry matter weight), respectively, while below-ground phytomass and mortmass were estimated to be 1,675 and 792 g/m2 (dry matter weight), respectively. ANPP was estimated to be 460 g/m2/yr. BNPP was estimated to be 1,340 g/m2/yr.",
-            "graphic-preview-description": "Browse Image",
-            "title": "NPP Grassland: Khomutov, Ukraine, 1948 and 1967-1970, R1",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/npp_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F146",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F146",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/npp/grassland/NPP_KHM/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/npp/grassland/NPP_KHM/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/NPP/guides/NPP_KHM.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/NPP/guides/NPP_KHM.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/146",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/146",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/npp/grassland/NPP_KHM/comp/NPP_KHM.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/npp/grassland/NPP_KHM/comp/NPP_KHM.pdf",
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
+            "identifier": "C2751936985-ORNL_CLOUD",
+            "issued": "2015-05-26",
+            "keyword": [
+                "ecological dynamics",
+                "earth science",
+                "biosphere",
+                "vegetation"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/146",
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
             "spatial": "47.17 38.0",
+            "temporal": "1948-07-04T00:00:00Z/1972-12-31T23:59:59Z",
             "theme": [
                 "NPP",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "NPP Grassland: Khomutov, Ukraine, 1948 and 1967-1970, R1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://c3.nasa.gov/dashlink/resources/928/",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2015-04-20",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
-            "keyword": [
-                "dashlink",
-                "ames",
-                "nasa"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Kamalika Das",
                 "hasEmail": "mailto:kamalika.das@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Dashlink"
-            },
-            "identifier": "DASHLINK_928",
             "description": "not available",
-            "title": "Learning curve for Apriori fix",
-            "programCode": [
-                "026:029"
-            ],
             "distribution": [
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/figure4_new_noerrbar.png",
-                    "description": "figure4_new_noerrbar.png",
                     "@type": "dcat:Distribution",
+                    "description": "figure4_new_noerrbar.png",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/figure4_new_noerrbar.png",
+                    "mediaType": "image/png",
                     "title": "figure4_new_noerrbar.png"
                 }
             ],
-            "accrualPeriodicity": "irregular"
+            "identifier": "DASHLINK_928",
+            "issued": "2015-04-20",
+            "keyword": [
+                "dashlink",
+                "ames",
+                "nasa"
+            ],
+            "landingPage": "https://c3.nasa.gov/dashlink/resources/928/",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:029"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Dashlink"
+            },
+            "title": "Learning curve for Apriori fix"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/SWOT-SSH-2.0",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Surface Water Ocean Topography (SWOT). 2024-02-01. SWOT Level 2 KaRIn Low Rate Sea Surface Height Data Product - Basic. Version 2.0. SWOT Level 2 KaRIn Low Rate Sea Surface Height Data Product - Basic, Version 2.0. Jet Propulsion Laboratory. Archived by National Aeronautics and Space Administration, U.S. Government, JPL NASA. https://doi.org/10.5067/SWOT-SSH-2.0. https://swot.jpl.nasa.gov/.",
-            "issued": "2022-07-21",
-            "temporal": "2022-12-16T00:00:00Z/2024-03-27T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-07-21",
-            "keyword": [
-                "ocean waves",
-                "sea surface topography",
-                "oceans",
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
-            "identifier": "C2799465428-POCLOUD",
-            "description": "The SWOT Level 2 KaRIn Low Rate Sea Surface Height Basic Data Product from the Surface Water Ocean Topography (SWOT) mission provides global sea surface height and significant wave height observations derived from low rate (LR) measurements from the Ka-band Radar Interferometer (KaRIn). SWOT launched on December 16, 2022 from Vandenberg Air Force Base in California into a 1-day repeat orbit for the \"calibration\" or \"fast-sampling\" phase of the mission, which completed in early July 2023. After the calibration phase, SWOT entered a 21-day repeat orbit in August 2023 to start the \"science\" phase of the mission, which is expected to continue through 2025. <br>\r\nThe L2 sea surface height data product is distributed in one netCDF-4 file per pass (half-orbit) covering the full KaRIn swath width, which spans 10-60km on each side of the nadir track. Sea surface height, sea surface height anomaly, wind speed, significant waveheight, and related parameters are provided on a geographically fixed, swath-aligned 2x2 km2 grid (Basic, Expert, Windwave). The sea surface height data are also provided on a finer 250x250 m2 \"native\" grid with minimal smoothing applied (Unsmoothed). <br>\r\nThis collection is a sub-collection of its parent: https://podaac.jpl.nasa.gov/dataset/SWOT_L2_LR_SSH_2.0  It provides the \"Basic\" file from each L2 SSH product, which contains a limited set of variables and is aimed at the general user.",
-            "release-place": "Jet Propulsion Laboratory",
-            "series-name": "SWOT Level 2 KaRIn Low Rate Sea Surface Height Data Product - Basic",
-            "graphic-preview-description": "Thumbnail",
             "creator": "Surface Water Ocean Topography (SWOT)",
-            "title": "SWOT Level 2 KaRIn Low Rate Sea Surface Height Data Product - Basic, Version 2.0",
-            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/SWOT_L2_LR_SSH_2.0.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The SWOT Level 2 KaRIn Low Rate Sea Surface Height Basic Data Product from the Surface Water Ocean Topography (SWOT) mission provides global sea surface height and significant wave height observations derived from low rate (LR) measurements from the Ka-band Radar Interferometer (KaRIn). SWOT launched on December 16, 2022 from Vandenberg Air Force Base in California into a 1-day repeat orbit for the \"calibration\" or \"fast-sampling\" phase of the mission, which completed in early July 2023. After the calibration phase, SWOT entered a 21-day repeat orbit in August 2023 to start the \"science\" phase of the mission, which is expected to continue through 2025. <br>\r\nThe L2 sea surface height data product is distributed in one netCDF-4 file per pass (half-orbit) covering the full KaRIn swath width, which spans 10-60km on each side of the nadir track. Sea surface height, sea surface height anomaly, wind speed, significant waveheight, and related parameters are provided on a geographically fixed, swath-aligned 2x2 km2 grid (Basic, Expert, Windwave). The sea surface height data are also provided on a finer 250x250 m2 \"native\" grid with minimal smoothing applied (Unsmoothed). <br>\r\nThis collection is a sub-collection of its parent: https://podaac.jpl.nasa.gov/dataset/SWOT_L2_LR_SSH_2.0  It provides the \"Basic\" file from each L2 SSH product, which contains a limited set of variables and is aimed at the general user.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSWOT-SSH-2.0",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSWOT-SSH-2.0",
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
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2799465428-POCLOUD",
-                    "description": "HTTPS endpoint for data browse and download",
                     "@type": "dcat:Distribution",
+                    "description": "HTTPS endpoint for data browse and download",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2799465428-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2799465428-POCLOUD",
-                    "description": "Browse granule search results in Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse granule search results in Earthdata Search",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2799465428-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/SWOT_L2_LR_SSH_2.0.jpg",
-                    "description": "Thumbnail",
                     "@type": "dcat:Distribution",
+                    "description": "Thumbnail",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/SWOT_L2_LR_SSH_2.0.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/web-misc/swot_mission_docs/pdd/D-56407_SWOT_Product_Description_L2_LR_SSH_20231026_RevBcite.pdf",
-                    "description": "Product Description Document (PDD)",
                     "@type": "dcat:Distribution",
+                    "description": "Product Description Document (PDD)",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/web-misc/swot_mission_docs/pdd/D-56407_SWOT_Product_Description_L2_LR_SSH_20231026_RevBcite.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/web-misc/swot_mission_docs/atbd/D-105502_SWOT_ATBD_L2_LR_SSH_20230724a_cite.pdf",
-                    "description": "Algorithm Theoretical Basis Document (ATBD)",
                     "@type": "dcat:Distribution",
+                    "description": "Algorithm Theoretical Basis Document (ATBD)",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/web-misc/swot_mission_docs/atbd/D-105502_SWOT_ATBD_L2_LR_SSH_20230724a_cite.pdf",
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
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2799465428-POCLOUD&pg%5B0%5D%5Bid%5D=*PIC0*",
-                    "description": "Search Granules from Forward Processing (PIC0)",
                     "@type": "dcat:Distribution",
+                    "description": "Search Granules from Forward Processing (PIC0)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2799465428-POCLOUD&pg%5B0%5D%5Bid%5D=*PIC0*",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2799465428-POCLOUD&pg%5B0%5D%5Bid%5D=*PGC0*",
-                    "description": "Search Granules from Bulk Reprocessing (PGC0)",
                     "@type": "dcat:Distribution",
+                    "description": "Search Granules from Bulk Reprocessing (PGC0)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2799465428-POCLOUD&pg%5B0%5D%5Bid%5D=*PGC0*",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 }
             ],
+            "graphic-preview-description": "Thumbnail",
+            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/SWOT_L2_LR_SSH_2.0.jpg",
+            "identifier": "C2799465428-POCLOUD",
+            "issued": "2022-07-21",
+            "keyword": [
+                "ocean waves",
+                "sea surface topography",
+                "oceans",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/SWOT-SSH-2.0",
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
+            "series-name": "SWOT Level 2 KaRIn Low Rate Sea Surface Height Data Product - Basic",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2022-12-16T00:00:00Z/2024-03-27T00:00:00Z",
             "theme": [
                 "SWOT",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "SWOT Level 2 KaRIn Low Rate Sea Surface Height Data Product - Basic, Version 2.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-3-DDR-APC-LIGHTCURVE-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "The Asteroid Photometric Catalog (3rd update), Lagerkvist, et.al., 1993 [LAGERKVISTETAL1993], is a compilation of all asteroid lightcurve photometry published up to and including the year 1992. The dataset includes the lightcurves in digital form and a table of references to all original publications.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-3-ddr-apc-lightcurve-v1.0_t58k-kduw",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "asteroid",
                 "support archives"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-3-DDR-APC-LIGHTCURVE-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-3-ddr-apc-lightcurve-v1.0_t58k-kduw",
-            "description": "The Asteroid Photometric Catalog (3rd update), Lagerkvist, et.al., 1993 [LAGERKVISTETAL1993], is a compilation of all asteroid lightcurve photometry published up to and including the year 1992. The dataset includes the lightcurves in digital form and a table of references to all original publications.",
-            "title": "ASTEROID PHOTOMETRIC CATALOG V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ASTEROID PHOTOMETRIC CATALOG V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-3-ESC4-67PCHURYUMOV-M24-V3.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This CODMAC level 3 data set contains radiometric calibrated image data in W/m^2/sr/nm, acquired by the OSIRIS Wide Angle Camera on the Rosetta spacecraft during the COMET ESCORT 4 mission phase, covering the period from 2015-12-15T23:25:00.000 to 2016-01-12T23:24:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V3.0 supersedes previous deliveries of the same dataset with the following changes since the last version: Lien corrected dataset after the July and October 2018 PSA/PDS external peer reviews. Updated documentation and ancillary files, added document on bandpass filter. Updated SCIENCE_USER_GUIDE_V03.PDF to include one section about FAQ and one section about image data quality. Added shutter backtravel and readout issues to image quality map. Updated DATA_QUALITY_ID keyword in image header. Improved handling of images with missing packets. Included FITs files. Browse products changed to the same size as the original image. Corrected START_TIME and STOP_TIME for BALLISTIC_STACKED images. Improved calibration of WAC balistic mode images.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-3-esc4-67pchuryumov-m24-v3.0",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2021-05-21",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "vega",
                 "international rosetta mission",
                 "67p/churyumov-gerasimenko 1 (1969 r1)",
                 "zeta cas"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-3-ESC4-67PCHURYUMOV-M24-V3.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-3-esc4-67pchuryumov-m24-v3.0",
-            "description": "This CODMAC level 3 data set contains radiometric calibrated image data in W/m^2/sr/nm, acquired by the OSIRIS Wide Angle Camera on the Rosetta spacecraft during the COMET ESCORT 4 mission phase, covering the period from 2015-12-15T23:25:00.000 to 2016-01-12T23:24:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V3.0 supersedes previous deliveries of the same dataset with the following changes since the last version: Lien corrected dataset after the July and October 2018 PSA/PDS external peer reviews. Updated documentation and ancillary files, added document on bandpass filter. Updated SCIENCE_USER_GUIDE_V03.PDF to include one section about FAQ and one section about image data quality. Added shutter backtravel and readout issues to image quality map. Updated DATA_QUALITY_ID keyword in image header. Improved handling of images with missing packets. Included FITs files. Browse products changed to the same size as the original image. Corrected START_TIME and STOP_TIME for BALLISTIC_STACKED images. Improved calibration of WAC balistic mode images.",
-            "title": "ROSETTA-ORBITER 67P OSIWAC 3 ESC4-MTP024 RDR V3.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P OSIWAC 3 ESC4-MTP024 RDR V3.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/2372",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Clark, M., L. Salas, R. Snyder, A. Lee, A.A. Turner, C. Seymour, J. Measey, and A. Ferraz. 2024. BioSCape: BioSoundSCape Acoustic Recordings, South Africa, 2023. ORNL DAAC, Oak Ridge, Tennessee, USA. https://doi.org/10.3334/ORNLDAAC/2372",
-            "issued": "2024-12-04",
-            "temporal": "2023-06-05T00:00:00Z/2023-12-16T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-12",
-            "keyword": [
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
-            "identifier": "C3366080352-ORNL_CLOUD",
             "description": "This dataset holds in situ sound recordings from sites in Greater Cape Floristic Region (GCFR), South Africa from June to December 2023. The recordings were collected as part of the Biodiversity Survey of the Cape (BioSCape) project, a multi-agency, NASA-led research project that integrates airborne imaging spectroscopy and lidar with a suite of measurements of biodiversity. BioSoundSCape is a BioSCape subproject seeking to relate ground-based measures of bioacoustic diversity to remote imagery. AudioMoth recorders were deployed at sites for 4 to 10 days of data collection (median = 7), and programmed to record 1 min of every 10, thus providing temporal sampling through day and night. Each recording was saved in a waveform audio file format with 16-bit digitization depth and a 48 kHz sampling rate. The recordings contain a wide range of environmental sounds such as biophony (e.g., birds, frogs, insects), anthropophony (e.g,. automobiles, airplanes) and geophony (e.g,. wind, rain). Sampling locations were stratified with respect to elevation, broad land use/land cover types, and time since wildfire disturbance. Most sites were within protected fynbos and Afromontane forest ecosystems. There were 538 sites in the wet season and 543 sites in the dry season, with most sites co-located between seasons. All sites were located within AVIRIS-NG hyperspectral acquisitions and 61% of sites were in LVIS lidar acquisitions. The dataset includes site information in tabular form and photographs of field sites.",
-            "graphic-preview-description": "AudioMoth automated recording devices were deployed in a variety of habitats.",
-            "title": "BioSCape: BioSoundSCape Acoustic Recordings, South Africa, 2023",
-            "graphic-preview-file": "https://daac.ornl.gov/bioscape/guides/Acoustic_Data_Cape_Floristic_Fig1.jpg",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F2372",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F2372",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/bioscape/Acoustic_Data_Cape_Floristic/data/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/bioscape/Acoustic_Data_Cape_Floristic/data/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/bioscape/guides/Acoustic_Data_Cape_Floristic.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/bioscape/guides/Acoustic_Data_Cape_Floristic.html",
+                    "mediaType": "text/html",
                     "title": "View this dataset's user's guide"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/2372",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/2372",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/bioscape/Acoustic_Data_Cape_Floristic/comp/Acoustic_Data_Cape_Floristic.pdf",
-                    "description": "BioSCape: BioSoundSCape Acoustic Recordings, South Africa, 2023: Acoustic_Data_Cape_Floristic.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "BioSCape: BioSoundSCape Acoustic Recordings, South Africa, 2023: Acoustic_Data_Cape_Floristic.pdf",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/bioscape/Acoustic_Data_Cape_Floristic/comp/Acoustic_Data_Cape_Floristic.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/bioscape/Acoustic_Data_Cape_Floristic/comp/Acoustic_Data_Cape_Floristic.pdf",
-                    "description": "BioSCape: BioSoundSCape Acoustic Recordings, South Africa, 2023: Acoustic_Data_Cape_Floristic.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "BioSCape: BioSoundSCape Acoustic Recordings, South Africa, 2023: Acoustic_Data_Cape_Floristic.pdf",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/bioscape/Acoustic_Data_Cape_Floristic/comp/Acoustic_Data_Cape_Floristic.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://daac.ornl.gov/bioscape/guides/Acoustic_Data_Cape_Floristic_Fig1.jpg",
-                    "description": "AudioMoth automated recording devices were deployed in a variety of habitats.",
                     "@type": "dcat:Distribution",
+                    "description": "AudioMoth automated recording devices were deployed in a variety of habitats.",
+                    "downloadURL": "https://daac.ornl.gov/bioscape/guides/Acoustic_Data_Cape_Floristic_Fig1.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://bioscape.io/",
-                    "description": "BioSCAPE Project Website",
                     "@type": "dcat:Distribution",
+                    "description": "BioSCAPE Project Website",
+                    "downloadURL": "https://bioscape.io/",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 }
             ],
+            "graphic-preview-description": "AudioMoth automated recording devices were deployed in a variety of habitats.",
+            "graphic-preview-file": "https://daac.ornl.gov/bioscape/guides/Acoustic_Data_Cape_Floristic_Fig1.jpg",
+            "identifier": "C3366080352-ORNL_CLOUD",
+            "issued": "2024-12-04",
+            "keyword": [
+                "biosphere",
+                "ecological dynamics",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/2372",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2025-01-12",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "ORNL_DAAC"
+            },
             "spatial": "18.01 -34.82 23.92 -31.37",
+            "temporal": "2023-06-05T00:00:00Z/2023-12-16T23:59:59Z",
             "theme": [
                 "BioSCape",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "BioSCape: BioSoundSCape Acoustic Recordings, South Africa, 2023"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-4-ESC1-67P-M10-INF-REFL-V1.0",
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
+            "description": "This CODMAC level 4 data set contains solar stray-light corrected, in-field stray-light corrected,  radiometric calibrated and geometric distortion corrected  (resampled) image data in reflectance units (normalized  and thus without unit),  acquired by the OSIRIS Narrow Angle Camera on the Rosetta spacecraft  during the COMET ESCORT 1 mission phase, covering the period  from 2014-11-21T23:25:00.000 to 2014-12-19T23:24:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V1.0 is the first version of this dataset: Lien corrected dataset after September 2019 PSA/PDS external peer review.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-4-esc1-67p-m10-inf-refl-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-4-ESC1-67P-M10-INF-REFL-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-4-esc1-67p-m10-inf-refl-v1.0",
-            "description": "This CODMAC level 4 data set contains solar stray-light corrected, in-field stray-light corrected,  radiometric calibrated and geometric distortion corrected  (resampled) image data in reflectance units (normalized  and thus without unit),  acquired by the OSIRIS Narrow Angle Camera on the Rosetta spacecraft  during the COMET ESCORT 1 mission phase, covering the period  from 2014-11-21T23:25:00.000 to 2014-12-19T23:24:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V1.0 is the first version of this dataset: Lien corrected dataset after September 2019 PSA/PDS external peer review.",
-            "title": "ROSETTA-ORBITER 67P OSINAC 4 ESC1-MTP010 RDR-INF-REFL V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P OSINAC 4 ESC1-MTP010 RDR-INF-REFL V1.0"
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
+            "description": "2-D Coanda Airfoil with Tangential Wall Jet. This web page provides data from experiments that may be useful for the validation of turbulence models. This resource is expected to grow gradually over time. All data herein arepublicly available.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://turbmodels.larc.nasa.gov/Other_exp_Data/Coanda/ldv_upper_xc_0.8_cm_0.115.dat",
+                    "mediaType": "application/dat"
+                }
             ],
+            "identifier": "NASA-851__9",
+            "issued": "2018-06-25",
             "keyword": [
                 "models",
                 "validation",
@@ -1394233,237 +1394242,210 @@
                 "coanda",
                 "airfoil"
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
-            "identifier": "NASA-851__9",
-            "description": "2-D Coanda Airfoil with Tangential Wall Jet. This web page provides data from experiments that may be useful for the validation of turbulence models. This resource is expected to grow gradually over time. All data herein arepublicly available.",
-            "title": "Turbulence Models: Data from Other Experiments: 2-D Coanda Airfoil with Tangential Wall Jet",
-            "programCode": [
-                "026:023"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://turbmodels.larc.nasa.gov/Other_exp_Data/Coanda/ldv_upper_xc_0.8_cm_0.115.dat",
-                    "mediaType": "application/dat"
-                }
+            "references": [
+                "http://turbmodels.larc.nasa.gov/index.html"
             ],
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Aerospace"
-            ]
+            ],
+            "title": "Turbulence Models: Data from Other Experiments: 2-D Coanda Airfoil with Tangential Wall Jet"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-E-OSIWAC-4-EAR1-EARTHSWINGBY1-V1.0",
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
-                "international rosetta mission"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This CODMAC level 4 data set contains radiometric calibrated and geometric distortion corrected (resampled) image data in W/m^2/sr/nm,  acquired by the OSIRIS Wide Angle Camera on the Rosetta spacecraft  during the EARTH SWING-BY 1 mission phase, covering the period  from 2004-10-17T00:00:00.000 to 2005-04-04T23:59:59.000. The prime target is planet Earth. This version V1.0 is the first version of this dataset.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-e-osiwac-4-ear1-earthswingby1-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-E-OSIWAC-4-EAR1-EARTHSWINGBY1-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-e-osiwac-4-ear1-earthswingby1-v1.0",
-            "description": "This CODMAC level 4 data set contains radiometric calibrated and geometric distortion corrected (resampled) image data in W/m^2/sr/nm,  acquired by the OSIRIS Wide Angle Camera on the Rosetta spacecraft  during the EARTH SWING-BY 1 mission phase, covering the period  from 2004-10-17T00:00:00.000 to 2005-04-04T23:59:59.000. The prime target is planet Earth. This version V1.0 is the first version of this dataset.",
-            "title": "ROSETTA-ORBITER EARTH OSIWAC 4 EAR1 RDR V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER EARTH OSIWAC 4 EAR1 RDR V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/SWOT-NALT-GDR-2.0",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Surface Water Ocean Topography (SWOT). 2023-06-01. SWOT Level 2 Nadir Altimeter Geophysical Data Record with Waveforms. Version 2.0. SWOT Level 2 Nadir Altimeter Geophysical Data Record with Waveforms Version 1.0. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/JPL/PODAAC. https://doi.org/10.5067/SWOT-NALT-GDR-2.0.",
-            "issued": "2022-06-28",
-            "temporal": "2022-12-16T00:00:00Z/2024-03-27T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-06-28",
-            "keyword": [
-                "sea surface topography",
-                "earth science",
-                "oceans",
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
-            "identifier": "C2799438313-POCLOUD",
-            "description": "The SWOT Level 2 Nadir Altimeter Geophysical Data Record (GDR) with Waveforms dataset produced by the Surface Water and Ocean Topography (SWOT) mission provides sea surface height, significant wave height and wind speed measurements from the Poseidon-3C nadir altimeter, a Jason-class dual frequency (Ku/C) altimeter. SWOT is a joint mission between NASA and CNES that launched on December 16, 2022. It aims to measure ocean surface topography with unprecedented resolution and accuracy, as well as map inland water bodies globally. The GDR dataset consists of discrete measurements for each half orbit along the ground track with sampling resolutions of approximately 6-km and 300-m at 1Hz and 20Hz, respectively. The data were processed using restituted auxiliary data and the Precise Orbit Ephemeris (POE). The data are available with latency of < 90 days and distributed in netCDF-4 file format.\r\n<br>This collection is the parent collection to the following sub-collections: <br>\r\nhttps://podaac.jpl.nasa.gov/dataset/SWOT_L2_NALT_GDR_SSHA_2.0 <br>\r\nhttps://podaac.jpl.nasa.gov/dataset/SWOT_L2_NALT_GDR_GDR_2.0 <br>\r\nhttps://podaac.jpl.nasa.gov/dataset/SWOT_L2_NALT_GDR_SGDR_2.0 <br>",
-            "series-name": "SWOT Level 2 Nadir Altimeter Geophysical Data Record with Waveforms",
-            "graphic-preview-description": "Thumbnail",
             "creator": "Surface Water Ocean Topography (SWOT)",
-            "title": "SWOT Level 2 Nadir Altimeter Geophysical Data Record with Waveforms",
-            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/SWOT_L2_NALT_GDR_2.0.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The SWOT Level 2 Nadir Altimeter Geophysical Data Record (GDR) with Waveforms dataset produced by the Surface Water and Ocean Topography (SWOT) mission provides sea surface height, significant wave height and wind speed measurements from the Poseidon-3C nadir altimeter, a Jason-class dual frequency (Ku/C) altimeter. SWOT is a joint mission between NASA and CNES that launched on December 16, 2022. It aims to measure ocean surface topography with unprecedented resolution and accuracy, as well as map inland water bodies globally. The GDR dataset consists of discrete measurements for each half orbit along the ground track with sampling resolutions of approximately 6-km and 300-m at 1Hz and 20Hz, respectively. The data were processed using restituted auxiliary data and the Precise Orbit Ephemeris (POE). The data are available with latency of < 90 days and distributed in netCDF-4 file format.\r\n<br>This collection is the parent collection to the following sub-collections: <br>\r\nhttps://podaac.jpl.nasa.gov/dataset/SWOT_L2_NALT_GDR_SSHA_2.0 <br>\r\nhttps://podaac.jpl.nasa.gov/dataset/SWOT_L2_NALT_GDR_GDR_2.0 <br>\r\nhttps://podaac.jpl.nasa.gov/dataset/SWOT_L2_NALT_GDR_SGDR_2.0 <br>",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSWOT-NALT-GDR-2.0",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSWOT-NALT-GDR-2.0",
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
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2799438313-POCLOUD",
-                    "description": "HTTPS endpoint for data browse and download",
                     "@type": "dcat:Distribution",
+                    "description": "HTTPS endpoint for data browse and download",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2799438313-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2799438313-POCLOUD",
-                    "description": "Browse granule search results in Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse granule search results in Earthdata Search",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2799438313-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/SWOT_L2_NALT_GDR_2.0.jpg",
-                    "description": "Thumbnail",
                     "@type": "dcat:Distribution",
+                    "description": "Thumbnail",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/SWOT_L2_NALT_GDR_2.0.jpg",
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
+            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/SWOT_L2_NALT_GDR_2.0.jpg",
+            "identifier": "C2799438313-POCLOUD",
+            "issued": "2022-06-28",
+            "keyword": [
+                "sea surface topography",
+                "earth science",
+                "oceans",
+                "ocean waves"
+            ],
+            "landingPage": "https://doi.org/10.5067/SWOT-NALT-GDR-2.0",
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
+            "series-name": "SWOT Level 2 Nadir Altimeter Geophysical Data Record with Waveforms",
             "spatial": "-180.0 -77.6 180.0 77.6",
+            "temporal": "2022-12-16T00:00:00Z/2024-03-27T00:00:00Z",
             "theme": [
                 "SWOT",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "SWOT Level 2 Nadir Altimeter Geophysical Data Record with Waveforms"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.nasa.gov/d/t5jy-3kej",
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
-            "identifier": "NASA-0000038__10",
+            "describedBy": "http://planetarynames.wr.usgs.gov/Page/Website",
             "description": "Planetary nomenclature, like terrestrial nomenclature, is used to uniquely identify a feature on the surface of a planet or satellite so that the feature can be easily located, described, and discussed. This gazetteer contains detailed information about all names of topographic and albedo features on planets and satellites (and some planetary ring and ring-gap systems) that the International Astronomical Union (IAU) has named and approved from its founding in 1919 through the present time.",
-            "title": "Gazetteer of Planetary Nomenclature",
-            "programCode": [
-                "026:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -1394471,397 +1394453,429 @@
                     "mediaType": "application/vnd.google-earth.kmz"
                 }
             ],
-            "describedBy": "http://planetarynames.wr.usgs.gov/Page/Website",
-            "accrualPeriodicity": "irregular"
+            "identifier": "NASA-0000038__10",
+            "issued": "2018-06-25",
+            "keyword": [
+                "wise",
+                "geography",
+                "nen",
+                "space science"
+            ],
+            "landingPage": "https://data.nasa.gov/d/t5jy-3kej",
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
-            "landingPage": "https://doi.org/10.5067/SMMRN-2WAF0",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "REMSS. 1995-02-28. NIMBUS-7 SMMR GLOBAL AIR-SEA PARAMETERS IN SWATH (Wentz). Version 1. NIMBUS-7 SMMR GLOBAL AIR-SEA PARAMETERS IN SWATH (Wentz). PO.DAAC. Archived by National Aeronautics and Space Administration, U.S. Government, PO.DAAC. https://doi.org/10.5067/SMMRN-2WAF0. https://podaac-tools.jpl.nasa.gov/drive/files/pub/documents/dataset_docs/smmr_wentz.html. REMSS, PO.DAAC, 1995-02-28, NIMBUS-7 SMMR GLOBAL AIR-SEA PARAMETERS IN SWATH (Wentz), https://podaac-tools.jpl.nasa.gov/drive/files/pub/documents/dataset_docs/smmr_wentz.html.",
-            "issued": "2009-06-15",
-            "temporal": "1979-11-01T00:00:00Z/1984-09-30T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2011-01-21",
-            "keyword": [
-                "oceans",
-                "earth science",
-                "ocean winds"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "David Moroni",
                 "hasEmail": "mailto:David.F.Moroni@jpl.nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/JPL/PODAAC"
-            },
-            "identifier": "C2617197620-POCLOUD",
-            "description": "Contains three parameters: ocean near-surface wind speed, columnar water vapor, and columnar liquid water. Product is produced by Frank Wentz at Remote Sensing Systems using data obtained from the Nimbus-7 Scanning Multichannel Microwave Radiometer (SMMR). Observations within 100 km of land are excluded; ice flags are also utilized. Data is obtained from all 10 individual SMMR channels, which closely correspond to the SMM/I channels and utilizing the same processing algorithms that were used to produce similar products derived from SSM/I observations (see PO.DAAC products 33 and 34).",
-            "release-place": "PO.DAAC",
-            "series-name": "NIMBUS-7 SMMR GLOBAL AIR-SEA PARAMETERS IN SWATH (Wentz)",
-            "graphic-preview-description": "Thumbnail",
             "creator": "REMSS",
-            "title": "NIMBUS-7 SMMR GLOBAL AIR-SEA PARAMETERS IN SWATH (Wentz)",
-            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/WENTZ_NIMBUS-7_SMMR_L2.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "Contains three parameters: ocean near-surface wind speed, columnar water vapor, and columnar liquid water. Product is produced by Frank Wentz at Remote Sensing Systems using data obtained from the Nimbus-7 Scanning Multichannel Microwave Radiometer (SMMR). Observations within 100 km of land are excluded; ice flags are also utilized. Data is obtained from all 10 individual SMMR channels, which closely correspond to the SMM/I channels and utilizing the same processing algorithms that were used to produce similar products derived from SSM/I observations (see PO.DAAC products 33 and 34).",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSMMRN-2WAF0",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSMMRN-2WAF0",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://podaac-tools.jpl.nasa.gov/drive/files/pub/documents/dataset_docs/smmr_wentz.html",
-                    "description": "Dataset User Guide",
                     "@type": "dcat:Distribution",
+                    "description": "Dataset User Guide",
+                    "downloadURL": "https://podaac-tools.jpl.nasa.gov/drive/files/pub/documents/dataset_docs/smmr_wentz.html",
+                    "mediaType": "text/html",
                     "title": "View this dataset's user's guide"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/WENTZ_NIMBUS-7_SMMR_L2.jpg",
-                    "description": "Thumbnail",
                     "@type": "dcat:Distribution",
+                    "description": "Thumbnail",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/WENTZ_NIMBUS-7_SMMR_L2.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/aop/retired/L2/ers1_adjusted_phase_c_v10/README",
-                    "description": "PO.DAAC Drive",
                     "@type": "dcat:Distribution",
+                    "description": "PO.DAAC Drive",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/aop/retired/L2/ers1_adjusted_phase_c_v10/README",
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
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2617197620-POCLOUD",
-                    "description": "HTTPS endpoint for data browse and download",
                     "@type": "dcat:Distribution",
+                    "description": "HTTPS endpoint for data browse and download",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2617197620-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2617197620-POCLOUD",
-                    "description": "Browse granule search results in Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse granule search results in Earthdata Search",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2617197620-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 }
             ],
+            "graphic-preview-description": "Thumbnail",
+            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/WENTZ_NIMBUS-7_SMMR_L2.jpg",
+            "identifier": "C2617197620-POCLOUD",
+            "issued": "2009-06-15",
+            "keyword": [
+                "oceans",
+                "earth science",
+                "ocean winds"
+            ],
+            "landingPage": "https://doi.org/10.5067/SMMRN-2WAF0",
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
+            "release-place": "PO.DAAC",
+            "series-name": "NIMBUS-7 SMMR GLOBAL AIR-SEA PARAMETERS IN SWATH (Wentz)",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "1979-11-01T00:00:00Z/1984-09-30T23:59:59.999Z",
             "theme": [
                 "NIMBUS-7",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "NIMBUS-7 SMMR GLOBAL AIR-SEA PARAMETERS IN SWATH (Wentz)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/AQUA/CERES/CCCM-FM3-MODIS-CAL-CS_L2.RELD2",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2024-06-14. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/AQUA/CERES/CCCM-FM3-MODIS-CAL-CS_L2.RELD2. https://doi.org/10.5067/AQUA/CERES/CCCM-FM3-MODIS-CAL-CS_L2.RELD2.",
-            "issued": "2024-05-28",
-            "temporal": "2006-07-01T00:00:00Z/2011-04-30T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-28",
-            "keyword": [
-                "clouds",
-                "aerosols",
-                "atmosphere",
-                "atmospheric radiation",
-                "atmospheric temperature",
-                "atmospheric water vapor",
-                "atmospheric winds",
-                "surface radiative properties",
-                "ngda",
-                "national geospatial data asset",
-                "land surface",
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
-            "identifier": "C3091018780-LARC_ASDC",
             "description": "CER_CCCM_Aqua-FM3-MODIS-CAL-CS_RelD2 is Release D2 of a highly fused Level 2 data product that uses multiple satellites and instruments in the Afternoon Train or A-Train to produce high-resolution vertical computed atmosphere fluxes. From Aqua, the Clouds and the Earth's Radiant Energy System (CERES) Flight Model 3 (FM3) and Moderate-Resolution Imaging Spectroradiometer (MODIS); from Cloud-Aerosol Lidar and Infrared Pathfinder Satellite Observations (CALIPSO), the Cloud-Aerosol Lidar with Orthogonal Polarization (CALIOP); and from CloudSat, the Cloud Profiling Radar (CPR) instruments are used in the product. The CCCM product name indicates the CALIPSO, CloudSat, CERES, and MODIS merged data synergy. The cloud and aerosol properties from CALIOP and cloud properties from the CPR are used to create high-resolution vertical profiles and sixteen horizontal groupings of cloud and aerosol that are then matched to a MODIS pixel and then convolved into Aqua CERES footprints. The product contains only the CERES footprint in each scan, which has the highest CALIPSO and CloudSat ground track coverage. The high-resolution information is used to compute within-atmosphere irradiance profiles using the Fu-Liou radiation transfer model (RTM). Four assumptions are used in the RTM: Total-sky, clear-sky (no clouds, but aerosol), pristine (no clouds or aerosols), and total-sky, no aerosol. The product also contains variables from the Single Scanner Footprint (SSF) product, including CERES-derived top-of-atmosphere (TOA) shortwave (SW), longwave (LW), and window (WN) irradiances obtained using angular distribution models and computed irradiances included in the Cloud Radiative Swath (CRS) product based on cloud and aerosol properties derived only from MODIS radiances. Two sets of SSF variables are included in the CCCM data. One set uses imager data covering the entire CERES footprint, and the other set only uses imager pixel data that matches with the CALIOP and CPR ground track. However, the CCCM product should not be considered a climate data record since various input data product versions and algorithm modifications will occur during the measurement period. The scan and packet numbers unique to the CERES footprint provide the means to match the data to other CERES products, although the CCCM product contains more near-nadir CERES footprints that are not in the standard SSF, CER_SSF_Aqua-FM3-MODIS_Edition4A, and CRS, CER_CRS_Aqua-FM3-MODIS_Edition2C, products. The resulting daily HDF granule contains 24 hours of data along the satellite track covering the globe. CERES is a key component of the Earth Observing System (EOS) program. The CERES instruments provide radiometric measurements of the Earth's atmosphere from three broadband channels. The CERES missions follow the successful Earth Radiation Budget Experiment (ERBE) mission. The CERES instrument, Flight Models 3 (FM3), was launched onboard Earth Observing System (EOS) Aqua on May 4, 2002. CALIPSO is a joint satellite mission between NASA and the French Agency CNES (Centre National d'Etudes Spatiales). CALIPSO was launched on April 28, 2006, to study the impact of clouds and aerosols on the Earth's radiation budget and climate. CloudSat was selected as a NASA Earth System Science Pathfinder satellite mission in 1999 to provide observations necessary to advance our understanding of cloud abundance, distribution, structure, and radiative properties. It also launched on April 28, 2006.",
-            "graphic-preview-description": "Mission Logo",
-            "title": "CERES A-Train Integrated CALIPSO, CloudSat, CERES, and MODIS (CCCM) Merged Release D2",
-            "graphic-preview-file": "https://asdc.larc.nasa.gov/static/images/project_logos/ceres.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAQUA%2FCERES%2FCCCM-FM3-MODIS-CAL-CS_L2.RELD2",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAQUA%2FCERES%2FCCCM-FM3-MODIS-CAL-CS_L2.RELD2",
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
-                    "downloadURL": "https://doi.org/10.5067/AQUA/CERES/CCCM-FM3-MODIS-CAL-CS_L2.RELD2",
-                    "description": "DOI data set landing page for CER_CCCM_Aqua-FM3-MODIS-CAL-CS_RelD2",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for CER_CCCM_Aqua-FM3-MODIS-CAL-CS_RelD2",
+                    "downloadURL": "https://doi.org/10.5067/AQUA/CERES/CCCM-FM3-MODIS-CAL-CS_L2.RELD2",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C3091018780-LARC_ASDC",
-                    "description": "Earthdata Search for CER_CCCM_Aqua-FM3-MODIS-CAL-CS_RelD2 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for CER_CCCM_Aqua-FM3-MODIS-CAL-CS_RelD2 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C3091018780-LARC_ASDC",
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
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://ceres.larc.nasa.gov/documents/DQ_summaries/CERES_CCCM_DQS_RelD2.pdf",
-                    "description": "Quality Summary: CERES CCCM Rel D2",
                     "@type": "dcat:Distribution",
+                    "description": "Quality Summary: CERES CCCM Rel D2",
+                    "downloadURL": "https://ceres.larc.nasa.gov/documents/DQ_summaries/CERES_CCCM_DQS_RelD2.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's product quality assessment"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://ceres.larc.nasa.gov/documents/DPC/DPC_current/pdfs/DPC_SSF_CRS_C3M_RelD1.pdf",
-                    "description": "Variable Descriptions of the A-Train Integrated CALIPSO, CloudSat, CERES, and MODIS Merged Product (CCCM or C3M),",
                     "@type": "dcat:Distribution",
+                    "description": "Variable Descriptions of the A-Train Integrated CALIPSO, CloudSat, CERES, and MODIS Merged Product (CCCM or C3M),",
+                    "downloadURL": "https://ceres.larc.nasa.gov/documents/DPC/DPC_current/pdfs/DPC_SSF_CRS_C3M_RelD1.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View information related to this dataset"
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
                     "title": "View this dataset's processing history"
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
-                    "downloadURL": "https://ceres.larc.nasa.gov/data/#cccm-level-2",
-                    "description": "CERES Subsetter",
                     "@type": "dcat:Distribution",
+                    "description": "CERES Subsetter",
+                    "downloadURL": "https://ceres.larc.nasa.gov/data/#cccm-level-2",
+                    "mediaType": "text/html",
                     "title": "Subset this dataset using a web based subsetter"
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
-                    "downloadURL": "https://www-calipso.larc.nasa.gov/",
-                    "description": "CALIPSO Mission Project Page",
                     "@type": "dcat:Distribution",
+                    "description": "CALIPSO Mission Project Page",
+                    "downloadURL": "https://www-calipso.larc.nasa.gov/",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://eospso.nasa.gov/missions/cloudsat",
-                    "description": "CloudSat Mission Project Page",
                     "@type": "dcat:Distribution",
+                    "description": "CloudSat Mission Project Page",
+                    "downloadURL": "https://eospso.nasa.gov/missions/cloudsat",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/CERES/CCCM/Aqua-FM3-MODIS-CAL-CS_RelD2/",
-                    "description": "ASDC Direct Data Download for CER_CCCM_Aqua-FM3-MODIS-CAL-CS_RelD2",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for CER_CCCM_Aqua-FM3-MODIS-CAL-CS_RelD2",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/CERES/CCCM/Aqua-FM3-MODIS-CAL-CS_RelD2/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/CERES/CCCM/Aqua-FM3-MODIS-CAL-CS_RelD2/contents.html",
-                    "description": "OPeNDAP data access for CER_CCCM_Aqua-FM3-MODIS-CAL-CS_RelD2",
                     "@type": "dcat:Distribution",
+                    "description": "OPeNDAP data access for CER_CCCM_Aqua-FM3-MODIS-CAL-CS_RelD2",
+                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/CERES/CCCM/Aqua-FM3-MODIS-CAL-CS_RelD2/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 }
             ],
+            "graphic-preview-description": "Mission Logo",
+            "graphic-preview-file": "https://asdc.larc.nasa.gov/static/images/project_logos/ceres.png",
+            "identifier": "C3091018780-LARC_ASDC",
+            "issued": "2024-05-28",
+            "keyword": [
+                "clouds",
+                "aerosols",
+                "atmosphere",
+                "atmospheric radiation",
+                "atmospheric temperature",
+                "atmospheric water vapor",
+                "atmospheric winds",
+                "surface radiative properties",
+                "ngda",
+                "national geospatial data asset",
+                "land surface",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/AQUA/CERES/CCCM-FM3-MODIS-CAL-CS_L2.RELD2",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2024-05-28",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/LARC/SD/ASDC"
+            },
             "spatial": "<?xml version=\"1.0\" encoding=\"UTF-8\"?><gml:Polygon xmlns:gml=\"http://www.opengis.net/gml/3.2\" srsName=\"EPSG:9825\"><gml:outerBoundaryIs><gml:LinearRing><gml:posList>-90.0 -180.0 -90.0 180.0 90.0 180.0 90.0 -180.0 -90.0 -180.0</gml:posList></gml:LinearRing></gml:outerBoundaryIs><gml:innerBoundaryIs></gml:innerBoundaryIs></gml:Polygon>",
+            "temporal": "2006-07-01T00:00:00Z/2011-04-30T23:59:59Z",
             "theme": [
                 "CERES",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "CERES A-Train Integrated CALIPSO, CloudSat, CERES, and MODIS (CCCM) Merged Release D2"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewBundle.jsp?identifier=urn%3Anasa%3Apds%3Ampf_mpim&version=1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "Derived opacities from Mars Pathfinder",
+            "identifier": "urn:nasa:pds:mpf_mpim_t5mu-5rnf",
             "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "pathfinder",
                 "mars",
                 "opacities"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewBundle.jsp?identifier=urn%3Anasa%3Apds%3Ampf_mpim&version=1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:mpf_mpim_t5mu-5rnf",
-            "description": "Derived opacities from Mars Pathfinder",
-            "title": "IMP Opacities Bundle",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "IMP Opacities Bundle"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO%2FRL-C-CONSERT-4-SDL-V1.0",
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
+            "description": "This archive contains REFORMATTED data (CODMAC level 4) that refers to target 67P/CHURYUMOV-GERASIMENKO 1 (1969 R1) from the CONSERT instrument onboard ROSETTA Orbiter and Lander, acquired during the SDL phase. In addition to the scientific signal of interest, it contains all the values applied to the signal for calibration. It also contains documentation which describes the CONSERT experiment. The L4 dataset includes interpolated signals using a specific CONSERT method. It also provide fine propagation travel times of the signal between Philae and Rosetta. The data archived in this data set conform to the Planetary Data System (PDS) Standards, Version 3.6.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-rl-c-consert-4-sdl-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO%2FRL-C-CONSERT-4-SDL-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-rl-c-consert-4-sdl-v1.0",
-            "description": "This archive contains REFORMATTED data (CODMAC level 4) that refers to target 67P/CHURYUMOV-GERASIMENKO 1 (1969 R1) from the CONSERT instrument onboard ROSETTA Orbiter and Lander, acquired during the SDL phase. In addition to the scientific signal of interest, it contains all the values applied to the signal for calibration. It also contains documentation which describes the CONSERT experiment. The L4 dataset includes interpolated signals using a specific CONSERT method. It also provide fine propagation travel times of the signal between Philae and Rosetta. The data archived in this data set conform to the Planetary Data System (PDS) Standards, Version 3.6.",
-            "title": "ROSETTA-ORBITER/ROSETTA-LANDER 67P CONSERT 4 SDL V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER/ROSETTA-LANDER 67P CONSERT 4 SDL V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO%2FRL-CAL-CONSERT-4-GRND-V1.0",
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
+            "description": "This archive contains REFORMATTED calibration data (CODMAC level 4) that refers to laboratory and AIT/AIV GROUND measurements of the lab bench of the CONSERT instrument. The L4 dataset includes interpolated signals using a specific CONSERT method. During this GROUND phase, CONSERT instrument has performed numerous technical and calibration tests. For archiving purposes, only calibration tests during which CONSERT orbiter flight model (FMO) and CONSERT lander spare model (FSL) is operated in synchronization (Ping-Pong mode) with another unit : Qualification Model Lander (QML) or Orbiter (QMO) and lab bench. The data archived in this dataset conform to the Planetary Data System (PDS) Standards, Version 3.6.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-rl-cal-consert-4-grnd-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "calibration"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO%2FRL-CAL-CONSERT-4-GRND-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-rl-cal-consert-4-grnd-v1.0",
-            "description": "This archive contains REFORMATTED calibration data (CODMAC level 4) that refers to laboratory and AIT/AIV GROUND measurements of the lab bench of the CONSERT instrument. The L4 dataset includes interpolated signals using a specific CONSERT method. During this GROUND phase, CONSERT instrument has performed numerous technical and calibration tests. For archiving purposes, only calibration tests during which CONSERT orbiter flight model (FMO) and CONSERT lander spare model (FSL) is operated in synchronization (Ping-Pong mode) with another unit : Qualification Model Lander (QML) or Orbiter (QMO) and lab bench. The data archived in this dataset conform to the Planetary Data System (PDS) Standards, Version 3.6.",
-            "title": "ROSETTA-ORBITER/ROSETTA-LANDER CAL CONSERT 4 GRND V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER/ROSETTA-LANDER CAL CONSERT 4 GRND V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://www.nasa.gov/mission_pages/station/expeditions/expedition12/index.html",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Brian Dunbar",
+                "hasEmail": "mailto:brian.dunbar@nasa.gov"
+            },
+            "description": "Press kit for ISS mission Expedition 12 from 10/2005-04/2006. Press kits contain information about each mission overview, crew, mission timeline, benefits, and media contact information.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "Press Kit PDF",
+                    "downloadURL": "http://www.nasa.gov/pdf/135404main_exp12_presskit.pdf",
+                    "mediaType": "application/pdf",
+                    "title": "ISS 12 Press Kit"
+                }
+            ],
+            "identifier": "OCIO-Fitara-24",
             "issued": "2006-12-31",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
             "keyword": [
                 "press kit",
                 "schedule",
@@ -1394874,138 +1394888,80 @@
                 "launch",
                 "12"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Brian Dunbar",
-                "hasEmail": "mailto:brian.dunbar@nasa.gov"
-            },
+            "landingPage": "http://www.nasa.gov/mission_pages/station/expeditions/expedition12/index.html",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:037"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "JSC"
             },
-            "identifier": "OCIO-Fitara-24",
-            "description": "Press kit for ISS mission Expedition 12 from 10/2005-04/2006. Press kits contain information about each mission overview, crew, mission timeline, benefits, and media contact information.",
-            "title": "ISS Expedition 12 Press Kit",
-            "programCode": [
-                "026:037"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "http://www.nasa.gov/pdf/135404main_exp12_presskit.pdf",
-                    "description": "Press Kit PDF",
-                    "@type": "dcat:Distribution",
-                    "title": "ISS 12 Press Kit"
-                }
-            ],
-            "accrualPeriodicity": "irregular"
+            "title": "ISS Expedition 12 Press Kit"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/RXHQI7P4AGIL",
             "citation": "Chris Barnet. 2019-01-15. SNDRAQIML3CMCCP. Version 2. Sounder SIPS: AQUA AIRS IR + MW Level 3 CLIMCAPS : Comprehensive Quality Control Gridded Monthly V2. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/RXHQI7P4AGIL. https://disc.gsfc.nasa.gov/datacollection/SNDRAQIML3CMCCP_2.html. Digital Science Data.",
-            "issued": "2002-09-01",
-            "temporal": "2002-08-31T00:00:00Z/2016-10-01T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2016-10-01",
-            "references": [
-                "https://doi.org/10.3390/rs11101227",
-                "https://doi.org/10.1109/TGRS.2012.2220369",
-                "https://doi.org/Sounder SIPS: Suomi NPP CrIMSS Level 3 Comprehensive Quality Control Gridded Daily CLIMCAPS Normal Spectral Resolution V1",
-                "https://doi.org/10.1109/TGRS.2002.808236",
-                "https://doi.org/10.1029/2005/JD007020",
-                "https://doi.org/10.5194/amt-13-4437-2020"
-            ],
-            "keyword": [
-                "atmospheric temperature",
-                "altitude",
-                "atmospheric radiation",
-                "atmospheric pressure",
-                "atmospheric chemistry",
-                "atmosphere",
-                "air quality",
-                "land surface",
-                "precipitation",
-                "oceans",
-                "earth science",
-                "surface radiative properties",
-                "surface thermal properties",
-                "clouds",
-                "ocean temperature",
-                "atmospheric water vapor"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Lena Iredell",
                 "hasEmail": "mailto:lena.iredell@nasa.gov"
             },
+            "creator": "Chris Barnet",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C1693440807-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Not provided"
-            },
             "description": "The CLIMCAPS (Community Long-term Infrared Microwave Coupled Product System) algorithm is used to analyze data from the AIRS (Atmospheric Infrared Sounder) and AMSU (Advanced Microwave Sounding Unit). The AIRS instrument is a grating spectrometer (R = 1200) aboard the second Earth Observing System (EOS) polar-orbiting platform, EOS Aqua. The AIRS in combination with the AMSU constitutes an innovative atmospheric sounding group of infrared and microwave sensors. The AIRS Standard Retrieval Product consists of retrieved estimates of cloud and surface properties, plus profiles of retrieved temperature, water vapor, ozone, carbon monoxide and methane. The temperature profile vertical resolution is 100 levels total between 1100 mb and 0.1 mb, while moisture profile is reported at atmospheric layers between 1100 mb and 300 mb. The horizontal resolution is 50 km.\n \nThe CLIMCAPS algorithm uses an Optimal Estimation methodology and uses an a-priori first guess to start the process. A CLIMCAPS sounding is comprised of a set of parameters that characterizes the full atmospheric state and includes a variety of geophysical parameters derived from the CrIMSS data. These include surface temperature and infrared emissivity; full atmosphere profiles of temperature, water vapor and ozone; infrared effective cloud top characteristics; carbon monoxide, methane, carbon dioxide, sulfur dioxide, nitrous oxide, and nitric acid.\n \nThis monthly one degree latitude by one degree longitude level-3 product starts with level-2 retrieval products applying the comprehensive quality control (QC) methodology. Comprehensive QC accepts a retrieval if the profile is good to the surface and ensures consistent analysis across all levels and variables.\n\nWARNING: To users of the derived product \u201cco_mmr_midtrop\u201d (carbon monoxide mass mixing ratio to dry air [kg/kg] at ~500 hPa). This variable has a significant bias due to a conversion error: the molecular weight of carbon dioxide (CO2, 48.01 g/mol) was used instead of carbon monoxide (CO, 28.01 g/mol). To correct, simply multiply \u201cco_mmr_midtrop\u201d by 28.01/48.01. Alternatively, derive a profile of mass mixing ratio from scratch using the retrieved column density values (\u201cmol_lay/co_mol_lay\u201d) in the Level 2 files. For further questions or concerns please contact the Sounder SIPS at: sounder.sips@jpl.nasa.gov",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "SNDRAQIML3CMCCP",
-            "creator": "Chris Barnet",
-            "graphic-preview-description": "Sample plot of AIRS/AMSU Level 3 Retrieval.",
-            "title": "Sounder SIPS: AQUA AIRS IR + MW Level 3 CLIMCAPS : Comprehensive Quality Control Gridded Monthly V2 (SNDRAQIML3CMCCP) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/SNDRAQIML3CMCCP_2.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FRXHQI7P4AGIL",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FRXHQI7P4AGIL",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/SNDRAQIML3CMCCP_2.png",
-                    "description": "Sample plot of AIRS/AMSU Level 3 Retrieval.",
                     "@type": "dcat:Distribution",
+                    "description": "Sample plot of AIRS/AMSU Level 3 Retrieval.",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/SNDRAQIML3CMCCP_2.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sounder.gesdisc.eosdis.nasa.gov/data/Aqua_Sounder_Level3/SNDRAQIML3CMCCP.2",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://sounder.gesdisc.eosdis.nasa.gov/data/Aqua_Sounder_Level3/SNDRAQIML3CMCCP.2",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sounder.gesdisc.eosdis.nasa.gov/opendap/Aqua_Sounder_Level3/SNDRAQIML3CMCCP.2/",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://sounder.gesdisc.eosdis.nasa.gov/opendap/Aqua_Sounder_Level3/SNDRAQIML3CMCCP.2/",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=SNDRAQIML3CMCCP+2",
-                    "description": "Search the Earthdata website",
                     "@type": "dcat:Distribution",
+                    "description": "Search the Earthdata website",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=SNDRAQIML3CMCCP+2",
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
                 },
                 {
@@ -1395015,177 +1394971,193 @@
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
                 }
             ],
+            "graphic-preview-description": "Sample plot of AIRS/AMSU Level 3 Retrieval.",
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/SNDRAQIML3CMCCP_2.png",
+            "identifier": "C1693440807-GES_DISC",
+            "issued": "2002-09-01",
+            "keyword": [
+                "atmospheric temperature",
+                "altitude",
+                "atmospheric radiation",
+                "atmospheric pressure",
+                "atmospheric chemistry",
+                "atmosphere",
+                "air quality",
+                "land surface",
+                "precipitation",
+                "oceans",
+                "earth science",
+                "surface radiative properties",
+                "surface thermal properties",
+                "clouds",
+                "ocean temperature",
+                "atmospheric water vapor"
+            ],
+            "landingPage": "https://doi.org/10.5067/RXHQI7P4AGIL",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2016-10-01",
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
+                "https://doi.org/Sounder SIPS: Suomi NPP CrIMSS Level 3 Comprehensive Quality Control Gridded Daily CLIMCAPS Normal Spectral Resolution V1",
+                "https://doi.org/10.1109/TGRS.2002.808236",
+                "https://doi.org/10.1029/2005/JD007020",
+                "https://doi.org/10.5194/amt-13-4437-2020"
+            ],
+            "release-place": "Greenbelt, MD, USA",
+            "series-name": "SNDRAQIML3CMCCP",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2002-08-31T00:00:00Z/2016-10-01T23:59:59.999Z",
             "theme": [
                 "Aqua",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Sounder SIPS: AQUA AIRS IR + MW Level 3 CLIMCAPS : Comprehensive Quality Control Gridded Monthly V2 (SNDRAQIML3CMCCP) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/242",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Wilczak, J. 1999. BOREAS AFM-06 Mean Wind Profile Data. ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/242",
-            "issued": "2023-11-22",
-            "temporal": "1994-05-21T00:00:00Z/1994-09-21T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-11-27",
-            "keyword": [
-                "earth science",
-                "atmosphere",
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
-            "identifier": "C2807620384-ORNL_CLOUD",
             "description": "Contains the AFM-06 wind profiler data near the Old Jack Pine site in the Southern Study Area.",
-            "graphic-preview-description": "Browse Image",
-            "title": "BOREAS AFM-06 Mean Wind Profile Data",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/boreas_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F242",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F242",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/boreas/AFM/afm06pwd/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/boreas/AFM/afm06pwd/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/BOREAS/guides/AFM06_WindProf.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/BOREAS/guides/AFM06_WindProf.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/242",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/242",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/AFM/afm06pwd/comp/afm06pwd.def",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/AFM/afm06pwd/comp/afm06pwd.def",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/msword",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/AFM/afm06pwd/comp/AFM06_WindProf.doc",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/AFM/afm06pwd/comp/AFM06_WindProf.doc",
+                    "mediaType": "application/msword",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/AFM/afm06pwd/comp/AFM06_WindProf.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/AFM/afm06pwd/comp/AFM06_WindProf.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/AFM/afm06pwd/comp/AFM06_WindProf.txt",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/AFM/afm06pwd/comp/AFM06_WindProf.txt",
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
+            "identifier": "C2807620384-ORNL_CLOUD",
+            "issued": "2023-11-22",
+            "keyword": [
+                "earth science",
+                "atmosphere",
+                "atmospheric winds"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/242",
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
             "spatial": "53.91 -104.4",
+            "temporal": "1994-05-21T00:00:00Z/1994-09-21T23:59:59Z",
             "theme": [
                 "BOREAS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "BOREAS AFM-06 Mean Wind Profile Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/Aura/OMI/DATA3004",
             "citation": "Deborah Stein-Zweers, and Pepijn Veefkind. 2012-03-24. OMAEROe. Version 003. OMI/Aura Multi-wavelength Aerosol Optical Depth and Single Scattering Albedo L3 1 day Best Pixel in 0.25 degree x 0.25 degree V3. NASA Goddard Space Flight Center. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/Aura/OMI/DATA3004. https://disc.gsfc.nasa.gov/datacollection/OMAEROe_003.html. Digital Science Data.",
-            "issued": "2004-10-01",
-            "temporal": "2004-10-01T00:00:00Z/2022-01-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2012-03-22",
-            "references": [
-                "https://doi.org/10.1109/TGRS.2006.869987",
-                "https://doi.org/10.1109/TGRS.2006.872935",
-                "https://doi.org/10.1117/12.627013"
-            ],
-            "keyword": [
-                "atmosphere",
-                "aerosols",
-                "earth science"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "JENNIFER WEI",
                 "hasEmail": "mailto:jennifer.c.wei@nasa.gov"
             },
+            "creator": "Deborah Stein-Zweers, and Pepijn Veefkind",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C1266136062-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "The OMI science team produces this Level-3 Aura/OMI Global Aerosol Data Products OMAEROe (0.25deg Lat/Lon grids). The OMAEROe product selects best aerosol value from the Level2G good quality data that are reported in each grid, based on the multi-wavelength algorithm that uses up to 20 wavelength bands between 331 nm and 500 nm.  The selection criteria is based on the shortest optical path length (secant of solar zenith angle + secant of viewing zenith angle).\n\nThe OMAEROe files are stored in the version 5 EOS Hierarchical Data Format (HDF-EOS5). Each file contains daily data from approximately 15 orbits. The maximum file size for the OMAEROe data product is about 7 Mbytes. (The shortname for this Level-3 Global Gridded Aerosol Product is OMAEROe)",
-            "release-place": "NASA Goddard Space Flight Center",
-            "series-name": "OMAEROe",
-            "creator": "Deborah Stein-Zweers, and Pepijn Veefkind",
-            "graphic-preview-description": "The GES-DISC Interactive Online Visualization ANd aNalysis Interface (Giovanni) is a web-based tool that allows users to interactively visualize and analyze data.",
-            "title": "OMI/Aura Multi-wavelength Aerosol Optical Depth and Single Scattering Albedo L3 1 day Best Pixel in 0.25 degree x 0.25 degree V3 (OMAEROe) at GES DISC",
-            "graphic-preview-file": "https://giovanni.gsfc.nasa.gov/giovanni/#dataKeyword=OMAEROe",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAura%2FOMI%2FDATA3004",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAura%2FOMI%2FDATA3004",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
@@ -1395195,73 +1395167,73 @@
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/OMAEROe_003.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/OMAEROe_003.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://acdisc.gsfc.nasa.gov/data/Aura_OMI_Level3/OMAEROe.003/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://acdisc.gsfc.nasa.gov/data/Aura_OMI_Level3/OMAEROe.003/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://giovanni.gsfc.nasa.gov/giovanni/#dataKeyword=OMAEROe",
-                    "description": "The GES-DISC Interactive Online Visualization ANd aNalysis Interface (Giovanni) is a web-based tool that allows users to interactively visualize and analyze data.",
                     "@type": "dcat:Distribution",
+                    "description": "The GES-DISC Interactive Online Visualization ANd aNalysis Interface (Giovanni) is a web-based tool that allows users to interactively visualize and analyze data.",
+                    "downloadURL": "https://giovanni.gsfc.nasa.gov/giovanni/#dataKeyword=OMAEROe",
+                    "mediaType": "text/html",
                     "title": "Get a related visualization through GIOVANNI"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=OMAEROe_003",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=OMAEROe_003",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://acdisc.gsfc.nasa.gov/opendap/HDF-EOS5/Aura_OMI_Level3/OMAEROe.003/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://acdisc.gsfc.nasa.gov/opendap/HDF-EOS5/Aura_OMI_Level3/OMAEROe.003/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "application/msword",
-                    "downloadURL": "https://acdisc.gsfc.nasa.gov/data/Aura_OMI_Level3/OMAEROe.003/doc/OMAEROe_OSIPS_README_V003.doc",
-                    "description": "README Document",
                     "@type": "dcat:Distribution",
+                    "description": "README Document",
+                    "downloadURL": "https://acdisc.gsfc.nasa.gov/data/Aura_OMI_Level3/OMAEROe.003/doc/OMAEROe_OSIPS_README_V003.doc",
+                    "mediaType": "application/msword",
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
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/repository/Mission/OMI/3.3_ScienceDataProductDocumentation/3.3.2_ProductRequirements_Designs/OMAEROe_FileSpec_V003.pdf",
-                    "description": "File Specification Document",
                     "@type": "dcat:Distribution",
+                    "description": "File Specification Document",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/repository/Mission/OMI/3.3_ScienceDataProductDocumentation/3.3.2_ProductRequirements_Designs/OMAEROe_FileSpec_V003.pdf",
+                    "mediaType": "application/pdf",
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
@@ -1395271,272 +1395243,276 @@
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc1.gsfc.nasa.gov/daac-bin/wms_omi?LAYERS=OMAEROe_AerosolOpticalThicknessMW&TRANSPARENT=TRUE&HEIGHT=300&WIDTH=600&request=GetMap&SRS=EPSG%3A4326&bbox=-180%2C-90%2C180%2C90&time=2013-09-02&version=1.1.1&FORMAT=image%2Fpng&service=WMS",
-                    "description": "Get map from GES DISC WMS for AerosolOpticalThicknessMW",
                     "@type": "dcat:Distribution",
+                    "description": "Get map from GES DISC WMS for AerosolOpticalThicknessMW",
+                    "downloadURL": "https://disc1.gsfc.nasa.gov/daac-bin/wms_omi?LAYERS=OMAEROe_AerosolOpticalThicknessMW&TRANSPARENT=TRUE&HEIGHT=300&WIDTH=600&request=GetMap&SRS=EPSG%3A4326&bbox=-180%2C-90%2C180%2C90&time=2013-09-02&version=1.1.1&FORMAT=image%2Fpng&service=WMS",
+                    "mediaType": "text/html",
                     "title": "Use Web Map Service (WMS) to download the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc1.gsfc.nasa.gov/daac-bin/wms_omi?LAYERS=OMAEROe_AbsorbingAerosolOpticalThicknessMW&TRANSPARENT=TRUE&HEIGHT=300&WIDTH=600&request=GetMap&SRS=EPSG%3A4326&bbox=-180%2C-90%2C180%2C90&time=2013-09-02&version=1.1.1&FORMAT=image%2Fpng&service=WMS",
-                    "description": "Get map from GES DISC WMS for AbsorbingAerosolOpticalThicknessMW",
                     "@type": "dcat:Distribution",
+                    "description": "Get map from GES DISC WMS for AbsorbingAerosolOpticalThicknessMW",
+                    "downloadURL": "https://disc1.gsfc.nasa.gov/daac-bin/wms_omi?LAYERS=OMAEROe_AbsorbingAerosolOpticalThicknessMW&TRANSPARENT=TRUE&HEIGHT=300&WIDTH=600&request=GetMap&SRS=EPSG%3A4326&bbox=-180%2C-90%2C180%2C90&time=2013-09-02&version=1.1.1&FORMAT=image%2Fpng&service=WMS",
+                    "mediaType": "text/html",
                     "title": "Use Web Map Service (WMS) to download the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc1.gsfc.nasa.gov/daac-bin/wms_omi?LAYERS=OMAEROe_SingleScatteringAlbedoMW&TRANSPARENT=TRUE&HEIGHT=300&WIDTH=600&request=GetMap&SRS=EPSG%3A4326&bbox=-180%2C-90%2C180%2C90&time=2013-09-02&version=1.1.1&FORMAT=image%2Fpng&service=WMS",
-                    "description": "Get map from GES DISC WMS for SingleScatteringAlbedoMW",
                     "@type": "dcat:Distribution",
+                    "description": "Get map from GES DISC WMS for SingleScatteringAlbedoMW",
+                    "downloadURL": "https://disc1.gsfc.nasa.gov/daac-bin/wms_omi?LAYERS=OMAEROe_SingleScatteringAlbedoMW&TRANSPARENT=TRUE&HEIGHT=300&WIDTH=600&request=GetMap&SRS=EPSG%3A4326&bbox=-180%2C-90%2C180%2C90&time=2013-09-02&version=1.1.1&FORMAT=image%2Fpng&service=WMS",
+                    "mediaType": "text/html",
                     "title": "Use Web Map Service (WMS) to download the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/daac-bin/wcsL3?coverage=OMAEROe%3AColumnAmountAerosol%3AAbsorbingAerosolOpticalThicknessMW&resy=0.25&CRS=CRS%3A84&request=getCoverage&bbox=-179.875%2C-89.875%2C179.875%2C89.875&version=1.0.0&resx=0.25&service=WCS&format=netCDF",
-                    "description": "WCS for AbsorbingAerosolOpticalThicknessMW",
                     "@type": "dcat:Distribution",
+                    "description": "WCS for AbsorbingAerosolOpticalThicknessMW",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/daac-bin/wcsL3?coverage=OMAEROe%3AColumnAmountAerosol%3AAbsorbingAerosolOpticalThicknessMW&resy=0.25&CRS=CRS%3A84&request=getCoverage&bbox=-179.875%2C-89.875%2C179.875%2C89.875&version=1.0.0&resx=0.25&service=WCS&format=netCDF",
+                    "mediaType": "text/html",
                     "title": "Use Web Coverage Service (WCS) to download the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/daac-bin/wcsL3?coverage=OMAEROe%3AColumnAmountAerosol%3AAerosolOpticalThicknessMW&resy=0.25&CRS=CRS%3A84&request=getCoverage&bbox=-179.875%2C-89.875%2C179.875%2C89.875&version=1.0.0&resx=0.25&service=WCS&format=netCDF",
-                    "description": "WCS for AerosolOpticalThicknessMW",
                     "@type": "dcat:Distribution",
+                    "description": "WCS for AerosolOpticalThicknessMW",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/daac-bin/wcsL3?coverage=OMAEROe%3AColumnAmountAerosol%3AAerosolOpticalThicknessMW&resy=0.25&CRS=CRS%3A84&request=getCoverage&bbox=-179.875%2C-89.875%2C179.875%2C89.875&version=1.0.0&resx=0.25&service=WCS&format=netCDF",
+                    "mediaType": "text/html",
                     "title": "Use Web Coverage Service (WCS) to download the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/daac-bin/wcsL3?coverage=OMAEROe%3AColumnAmountAerosol%3ASingleScatteringAlbedoMW&resy=0.25&CRS=CRS%3A84&request=getCoverage&bbox=-179.875%2C-89.875%2C179.875%2C89.875&version=1.0.0&resx=0.25&service=WCS&format=netCDF",
-                    "description": "WCS for SingleScatteringAlbedoMW",
                     "@type": "dcat:Distribution",
+                    "description": "WCS for SingleScatteringAlbedoMW",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/daac-bin/wcsL3?coverage=OMAEROe%3AColumnAmountAerosol%3ASingleScatteringAlbedoMW&resy=0.25&CRS=CRS%3A84&request=getCoverage&bbox=-179.875%2C-89.875%2C179.875%2C89.875&version=1.0.0&resx=0.25&service=WCS&format=netCDF",
+                    "mediaType": "text/html",
                     "title": "Use Web Coverage Service (WCS) to download the dataset's data"
                 }
             ],
+            "graphic-preview-description": "The GES-DISC Interactive Online Visualization ANd aNalysis Interface (Giovanni) is a web-based tool that allows users to interactively visualize and analyze data.",
+            "graphic-preview-file": "https://giovanni.gsfc.nasa.gov/giovanni/#dataKeyword=OMAEROe",
+            "identifier": "C1266136062-GES_DISC",
+            "issued": "2004-10-01",
+            "keyword": [
+                "atmosphere",
+                "aerosols",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/Aura/OMI/DATA3004",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2012-03-22",
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
+            "release-place": "NASA Goddard Space Flight Center",
+            "series-name": "OMAEROe",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2004-10-01T00:00:00Z/2022-01-17T00:00:00Z",
             "theme": [
                 "Aura",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "OMI/Aura Multi-wavelength Aerosol Optical Depth and Single Scattering Albedo L3 1 day Best Pixel in 0.25 degree x 0.25 degree V3 (OMAEROe) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/H38Q5FTBPZ8K",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "SnowEx20 Jemez UNM 800 MHz MALA GPR V001. Version 1. Archived by National Aeronautics and Space Administration, U.S. Government, NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/H38Q5FTBPZ8K.",
-            "issued": "2020-01-22",
-            "temporal": "2020-01-22T00:00:00Z/2020-03-04T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-03-04",
-            "keyword": [
-                "spectral/engineering",
-                "earth science",
-                "snow/ice",
-                "radar",
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
-            "identifier": "C2059268385-NSIDC_ECS",
             "description": "This data set contains two-way travel times from a ground penetrating radar survey conducted at Jemez, New Mexico. Data were collected between 12 February 2020 and 04 March 2020 as part of the SnowEx 2020 campaign.",
-            "title": "SnowEx20 Jemez UNM 800 MHz MALA GPR V001",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FH38Q5FTBPZ8K",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FH38Q5FTBPZ8K",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/SNOWEX/SNEX20_J_UNM_GPR.001/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/SNOWEX/SNEX20_J_UNM_GPR.001/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=SNEX20_J_UNM_GPR+V001",
-                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=SNEX20_J_UNM_GPR+V001",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/data/data-access-tool/SNEX20_J_UNM_GPR/versions/1/",
-                    "description": "Search and filter data files using a map-based interface",
                     "@type": "dcat:Distribution",
+                    "description": "Search and filter data files using a map-based interface",
+                    "downloadURL": "https://nsidc.org/data/data-access-tool/SNEX20_J_UNM_GPR/versions/1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/H38Q5FTBPZ8K",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/H38Q5FTBPZ8K",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/H38Q5FTBPZ8K",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/H38Q5FTBPZ8K",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C2059268385-NSIDC_ECS",
+            "issued": "2020-01-22",
+            "keyword": [
+                "spectral/engineering",
+                "earth science",
+                "snow/ice",
+                "radar",
+                "cryosphere"
+            ],
+            "landingPage": "https://doi.org/10.5067/H38Q5FTBPZ8K",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2020-03-04",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA NSIDC DAAC"
+            },
             "spatial": "-106.537 35.85 -106.505 35.889",
+            "temporal": "2020-01-22T00:00:00Z/2020-03-04T23:59:59.999Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "SnowEx20 Jemez UNM 800 MHz MALA GPR V001"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=IHW-C-RSOH-3-EDR-HALLEY-V1.0",
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
-                "halley"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "NASA's International Halley Watch (IHW) has created a Comet Halley Archive. The collection of data spans the full wavelength range as submitted by scientists to the IHW. The observations belong to one of the following Disciplines: Amateur, Astrometry, Infrared Studies, Large-Scale Phenomena, Meteor Studies, Near-Nucleus Studies, Photometry and Polarimetry, Radio Studies, and Spectroscopy and Spectrophotometry. The data collected by these nine disciplines were augmented by Spacecraft measurements. The data were submitted to IHW, but the evaluation and selection for the Archive has been the primary responsibility of the Discipline Specialist Teams for each network in cooperation with the Lead Center. The data from the Radio Studies Spectral Line Subnetwork contains 1657 spectra of Halley, spanning dates from 1985 January 26 through 1986 July 29.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ihw-c-rsoh-3-edr-halley-v1.0_t5tu-bmwz",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international halley watch",
+                "halley"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=IHW-C-RSOH-3-EDR-HALLEY-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ihw-c-rsoh-3-edr-halley-v1.0_t5tu-bmwz",
-            "description": "NASA's International Halley Watch (IHW) has created a Comet Halley Archive. The collection of data spans the full wavelength range as submitted by scientists to the IHW. The observations belong to one of the following Disciplines: Amateur, Astrometry, Infrared Studies, Large-Scale Phenomena, Meteor Studies, Near-Nucleus Studies, Photometry and Polarimetry, Radio Studies, and Spectroscopy and Spectrophotometry. The data collected by these nine disciplines were augmented by Spacecraft measurements. The data were submitted to IHW, but the evaluation and selection for the Archive has been the primary responsibility of the Discipline Specialist Teams for each network in cooperation with the Lead Center. The data from the Radio Studies Spectral Line Subnetwork contains 1657 spectra of Halley, spanning dates from 1985 January 26 through 1986 July 29.",
-            "title": "IHW COMET HALLEY RADIO SPECTRAL DATA V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "IHW COMET HALLEY RADIO SPECTRAL DATA V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/GPM/MHS/METOPA/GPROFCLIM/2A/07",
             "citation": "GPM Science Team. 2022-05-09. GPM_2AGPROFMETOPAMHS_CLIM. Version 07. GPM MHS on METOP-A (GPROF) Radiometer Precipitation Profiling L2A 1.5 hours 17 km V07. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/GPM/MHS/METOPA/GPROFCLIM/2A/07. https://disc.gsfc.nasa.gov/datacollection/GPM_2AGPROFMETOPAMHS_CLIM_07.html. Digital Science Data.",
-            "issued": "2022-05-09",
-            "temporal": "2006-11-23T00:00:00Z/2023-02-28T00:00:00Z",
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
                 "fn": "CHRISTIAN KUMMEROW",
                 "hasEmail": "mailto:kummerow@atmos.colostate.edu"
             },
+            "creator": "GPM Science Team",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C2264134196-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "Version 07 is the current version of the data set. Older versions are no longer available and have been superseded by Version 07.\n\nThe \"CLIM\"  products differ from their \"regular\" counterparts (without the \"CLIM\" in the name) by the ancillary data they use. They are Climate-Reference products, which requires homogeneous ancillary data over the climate time series.  Hence, the ECMWF-Interim (European Centre for Medium-Range Weather Forecasts, 2-3 months lag behind the regular production) reanalysis is used as ancillary data to derive surface and atmospheric conditions required by the GPROF algorithm for the \"CLIM\" output. The GPROF databases are also adjusted accordingly for these climate-referenced retrievals.\n\nThe 2AGPROF (Goddard Profiling) algorithm retrieves consistent precipitation and related science fields from the following GMI and partner passive microwave sensors:\n+ TMI (TRMM)\n+ GMI, (GPM)\n+ SSMI (DMSP F15), SSMIS (DMSP F16, F17, F18, F19)\n+ AMSR2 (GCOM-W1)\n+ MHS (NOAA 18,19) \n+ MHS (METOP A,B)\n+ ATMS (NPP)\n+ SAPHIR (MT1)\n\nThis provides the bulk of the 3-hour coverage achieved by GPM. For each sensor, there are nearrealtime (NRT) products, standard products, and climate products. These differ only in the amount of data that are available within 3 hours, 48 hours, and 3 months of collection, as well as the ancillary data used. The NRT product uses GANAL forecast fields. Standard products use the GANAL analysis product, while the climate product uses ECMWF reanalysis in order to allow for consistent data records with earlier missions. These earlier data may be archived separately. The main strength of the product is the large sampling provided.\n\nThe GPM radiometer algorithms are Bayesian-type algorithms. These algorithms search an apriori database of potential rain profiles and retrieve a weighted average of these entries based upon the proximity of the observed brightness temperature (Tb) to the simulated Tb corresponding to each rain profile. By using the same a-priori database of rain profiles, with appropriate simulated Tb for each constellation sensor, the Bayesian method is completely parametric and thus well suited for GPM's constellation approach. The a-priori information will be supplied by the combined algorithm supplied by GPM's core satellite as soon after launch as feasible. Databases for V0 of the algorithm had to be constructed from various sources as described in the ATBD. The solution provides a mean rain rate as well as the vertical structure of cloud and precipitation hydrometeors and their uncertainty.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "GPM_2AGPROFMETOPAMHS_CLIM",
-            "creator": "GPM Science Team",
-            "title": "GPM MHS on METOP-A (GPROF) Radiometer Precipitation Profiling L2A 1.5 hours 17 km V07 (GPM_2AGPROFMETOPAMHS_CLIM) at GES DISC",
-            "graphic-preview-description": "Surface Precipitation from GPM MHS on METOP-A GPROF (17 km x 17 km) (GPM_2AGPROFMETOPAMHS)",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/GPM/browse/GPM_2AGPROFMETOPAMHS_CLIM_07.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGPM%2FMHS%2FMETOPA%2FGPROFCLIM%2F2A%2F07",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGPM%2FMHS%2FMETOPA%2FGPROFCLIM%2F2A%2F07",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/GPM/browse/GPM_2AGPROFMETOPAMHS_CLIM_07.png",
-                    "description": "Surface Precipitation from GPM MHS on METOP-A GPROF (17 km x 17 km) (GPM_2AGPROFMETOPAMHS)",
                     "@type": "dcat:Distribution",
+                    "description": "Surface Precipitation from GPM MHS on METOP-A GPROF (17 km x 17 km) (GPM_2AGPROFMETOPAMHS)",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/GPM/browse/GPM_2AGPROFMETOPAMHS_CLIM_07.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/GPM_2AGPROFMETOPAMHS_CLIM_07.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/GPM_2AGPROFMETOPAMHS_CLIM_07.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://gpm1.gesdisc.eosdis.nasa.gov/data/GPM_L2/GPM_2AGPROFMETOPAMHS_CLIM.07/",
-                    "description": "Access the data via HTTPS",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS",
+                    "downloadURL": "https://gpm1.gesdisc.eosdis.nasa.gov/data/GPM_L2/GPM_2AGPROFMETOPAMHS_CLIM.07/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://gpm1.gesdisc.eosdis.nasa.gov/opendap/GPM_L2/GPM_2AGPROFMETOPAMHS_CLIM.07/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol",
+                    "downloadURL": "https://gpm1.gesdisc.eosdis.nasa.gov/opendap/GPM_L2/GPM_2AGPROFMETOPAMHS_CLIM.07/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=GPM_2AGPROFMETOPAMHS_CLIM_07",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=GPM_2AGPROFMETOPAMHS_CLIM_07",
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
@@ -1395546,308 +1395522,308 @@
                     "title": "View documentation related to this dataset"
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
-                    "downloadURL": "https://www.eumetsat.int/mhs",
-                    "description": "Instrument Description from EUMETSAT",
                     "@type": "dcat:Distribution",
+                    "description": "Instrument Description from EUMETSAT",
+                    "downloadURL": "https://www.eumetsat.int/mhs",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.star.nesdis.noaa.gov/mirs/mhs.php",
-                    "description": "Instrument Description from NOAA",
                     "@type": "dcat:Distribution",
+                    "description": "Instrument Description from NOAA",
+                    "downloadURL": "https://www.star.nesdis.noaa.gov/mirs/mhs.php",
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
+            "graphic-preview-description": "Surface Precipitation from GPM MHS on METOP-A GPROF (17 km x 17 km) (GPM_2AGPROFMETOPAMHS)",
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/GPM/browse/GPM_2AGPROFMETOPAMHS_CLIM_07.png",
+            "identifier": "C2264134196-GES_DISC",
+            "issued": "2022-05-09",
+            "keyword": [
+                "atmospheric water vapor",
+                "earth science",
+                "atmosphere",
+                "precipitation"
+            ],
+            "landingPage": "https://doi.org/10.5067/GPM/MHS/METOPA/GPROFCLIM/2A/07",
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
+            "series-name": "GPM_2AGPROFMETOPAMHS_CLIM",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2006-11-23T00:00:00Z/2023-02-28T00:00:00Z",
             "theme": [
                 "GPM",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "GPM MHS on METOP-A (GPROF) Radiometer Precipitation Profiling L2A 1.5 hours 17 km V07 (GPM_2AGPROFMETOPAMHS_CLIM) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/GPMGV/MC3E/AMPR/DATA101",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Roberts, Jason Brent .2012. GPM GROUND VALIDATION ADVANCED MICROWAVE PRECIPITATION RADIOMETER (AMPR) MC3E [indicate subset used]. Dataset available online from the NASA Global Hydrometeorology Resource Center DAAC, Huntsville, Alabama, U.S.A. DOI: http://dx.doi.org/10.5067/GPMGV/MC3E/AMPR/DATA101",
-            "issued": "2012-02-06",
-            "temporal": "2011-04-25T07:14:09Z/2011-06-01T23:33:14Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-04-28",
-            "keyword": [
-                "microwave",
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
-            "identifier": "C1979126507-GHRC_DAAC",
             "description": "The GPM Ground Validation Advanced Microwave Precipitaiton Radiometer (AMPR) MC3E dataset was collected by the Advanced Microwave Precipitation Radiometer (AMPR) instrument, which played a key role in the Midlatitude Continental Convective Clouds Experiment (MC3E). The AMPR remotely sensed passive microwave signatures of geophysical parameters from an airborne platform. The instrument is a low noise system which provided multi-frequency microwave imagery with high spatial and temporal resolution. AMPR data were collected at a combination of four microwave frequencies (10.7, 19.35, 37.1, and 85.5 GHz) with two orientations each (Vpol-to-Hpol and Hpol-to-Vpol), which were complimentary to current aircraft and satellite instrumentation. These frequencies are best suited to the study of rain systems, but were also useful to studies of other atmospheric, oceanic, and land surface processes.",
-            "graphic-preview-description": "N/A",
-            "title": "GPM GROUND VALIDATION ADVANCED MICROWAVE PRECIPITATION RADIOMETER (AMPR) MC3E V1",
-            "graphic-preview-file": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/mc3e/ampr/browse/",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGPMGV%2FMC3E%2FAMPR%2FDATA101",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGPMGV%2FMC3E%2FAMPR%2FDATA101",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=gpmamprmc3e",
-                    "description": "Files may be downloaded directly to your workstation from this link",
                     "@type": "dcat:Distribution",
+                    "description": "Files may be downloaded directly to your workstation from this link",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=gpmamprmc3e",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "image/gif",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/mc3e/ampr/browse/mc3e_ampr_20110520_tbs_v01_swath3.gif",
-                    "description": "Sample browse image",
                     "@type": "dcat:Distribution",
+                    "description": "Sample browse image",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/mc3e/ampr/browse/mc3e_ampr_20110520_tbs_v01_swath3.gif",
+                    "mediaType": "image/gif",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "image/gif",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/mc3e/ampr/browse/mc3e_ampr_20110507_tbs_v01_swath2.gif",
-                    "description": "Sample browse image",
                     "@type": "dcat:Distribution",
+                    "description": "Sample browse image",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/mc3e/ampr/browse/mc3e_ampr_20110507_tbs_v01_swath2.gif",
+                    "mediaType": "image/gif",
                     "title": "Get a related visualization"
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
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/mc3e/ampr/doc/gpmamprmc3e_dataset.pdf",
-                    "description": "The guide document contains detailed information about the dataset",
                     "@type": "dcat:Distribution",
+                    "description": "The guide document contains detailed information about the dataset",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/mc3e/ampr/doc/gpmamprmc3e_dataset.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/doc/gpmgv/mc3e/gpmamprmc3e/ampr_reader_MC3E.f",
-                    "description": "Sample read program for AMPR data from MC3E",
                     "@type": "dcat:Distribution",
+                    "description": "Sample read program for AMPR data from MC3E",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/doc/gpmgv/mc3e/gpmamprmc3e/ampr_reader_MC3E.f",
+                    "mediaType": "text/html",
                     "title": "Downloadable software applications"
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
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/mc3e/ampr/browse/",
-                    "description": "N/A",
                     "@type": "dcat:Distribution",
+                    "description": "N/A",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/mc3e/ampr/browse/",
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
+            "graphic-preview-file": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/mc3e/ampr/browse/",
+            "identifier": "C1979126507-GHRC_DAAC",
+            "issued": "2012-02-06",
+            "keyword": [
+                "microwave",
+                "spectral/engineering",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/GPMGV/MC3E/AMPR/DATA101",
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
             "spatial": "-105.64 27.8598 -91.3954 42.4929",
+            "temporal": "2011-04-25T07:14:09Z/2011-06-01T23:33:14Z",
             "theme": [
                 "MC3E",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "GPM GROUND VALIDATION ADVANCED MICROWAVE PRECIPITATION RADIOMETER (AMPR) MC3E V1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=GO-E-PWS-2-EDR-E2WFRM-V1.0",
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
+            "description": "This data set includes wideband waveform measurements from the Galileo plasma wave receiver obtained during the second Earth encounter.  These measurements are electric or magnetic waveforms obtained by rapidly sampling the potential at the input to the receiver from either the electric dipole antenna or the magnetic search coil antenna.  The sample rates are 201,600 s^-1, 25,200 s^-1, or 3,150 s^-1 taken through bandpass filters of 80, 10, or 1 kHz, respectively.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.go-e-pws-2-edr-e2wfrm-v1.0_t5v2-7e9z",
+            "issued": "2021-05-21",
+            "keyword": [
+                "earth",
+                "galileo"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=GO-E-PWS-2-EDR-E2WFRM-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.go-e-pws-2-edr-e2wfrm-v1.0_t5v2-7e9z",
-            "description": "This data set includes wideband waveform measurements from the Galileo plasma wave receiver obtained during the second Earth encounter.  These measurements are electric or magnetic waveforms obtained by rapidly sampling the potential at the input to the receiver from either the electric dipole antenna or the magnetic search coil antenna.  The sample rates are 201,600 s^-1, 25,200 s^-1, or 3,150 s^-1 taken through bandpass filters of 80, 10, or 1 kHz, respectively.",
-            "title": "GO E PWS EDITED EARTH 2 WAVEFORM RECEIVER V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "GO E PWS EDITED EARTH 2 WAVEFORM RECEIVER V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/GLOSSAC-L3-V2.0",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2018-09-12. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/GLOSSAC-L3-V2.0. https://eosweb.larc.nasa.gov/project/glossac/glossac_table.",
-            "issued": "2017-05-04",
-            "temporal": "1979-01-01T00:00:00Z/2018-12-31T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2017-05-04",
-            "keyword": [
-                "atmosphere",
-                "earth science",
-                "aerosols"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Larry Thomason",
                 "hasEmail": "mailto:l.w.thomason@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/LARC/SD/ASDC"
-            },
-            "identifier": "C1684217303-LARC_ASDC",
             "description": "The Global Space-based Stratospheric Aerosol Climatology, or GloSSAC, is a 40-year climatology of stratospheric aerosol properties focused on extinction coefficient measurements by the Stratospheric Aerosol and Gas Experiment (SAGE) series of instruments through mid-2005 and on the Optical Spectrograph and InfraRed Imager System (OSIRIS) and the Cloud-Aerosol Lidar and Infrared Pathfinder Satellite Observation (CALIPSO) data thereafter. Data from other space instruments and from ground-based, air and balloon borne instruments to fill in key gaps in the data set. The end result is a global and gap-free data set focused on aerosol extinction coefficient at 525 and 1020 nm and other parameters on an \u2018as available\u2019 basis.",
-            "title": "Global Space-based Stratospheric Aerosol Climatology Version 2.0",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGLOSSAC-L3-V2.0",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGLOSSAC-L3-V2.0",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://www.sparc-ssirc.org/",
-                    "description": "SSiRC Activity Summary",
                     "@type": "dcat:Distribution",
+                    "description": "SSiRC Activity Summary",
+                    "downloadURL": "http://www.sparc-ssirc.org/",
+                    "mediaType": "text/html",
                     "title": "The dataset's home page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/project/GloSSAC",
-                    "description": "ASDC Data and Information for GloSSAC",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Data and Information for GloSSAC",
+                    "downloadURL": "https://asdc.larc.nasa.gov/project/GloSSAC",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://eosweb.larc.nasa.gov/sites/default/files/project/glossac/guide/GloSSAC_Data_Products_User_Guide_v1.1.pdf",
-                    "description": "GloSSAC Data Products User\u2019s Guide - August 2017",
                     "@type": "dcat:Distribution",
+                    "description": "GloSSAC Data Products User\u2019s Guide - August 2017",
+                    "downloadURL": "https://eosweb.larc.nasa.gov/sites/default/files/project/glossac/guide/GloSSAC_Data_Products_User_Guide_v1.1.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://eosweb.larc.nasa.gov/project/glossac/guide/GloSSAC_Project_Guide_Document_v1.1.pdf",
-                    "description": "GloSSAC Project Guide Document",
                     "@type": "dcat:Distribution",
+                    "description": "GloSSAC Project Guide Document",
+                    "downloadURL": "https://eosweb.larc.nasa.gov/project/glossac/guide/GloSSAC_Project_Guide_Document_v1.1.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
                 }
             ],
+            "identifier": "C1684217303-LARC_ASDC",
+            "issued": "2017-05-04",
+            "keyword": [
+                "atmosphere",
+                "earth science",
+                "aerosols"
+            ],
+            "landingPage": "https://doi.org/10.5067/GLOSSAC-L3-V2.0",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2017-05-04",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/LARC/SD/ASDC"
+            },
             "spatial": "-180.0 -80.0 180.0 80.0",
+            "temporal": "1979-01-01T00:00:00Z/2018-12-31T23:59:59Z",
             "theme": [
                 "GloSSAC",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Global Space-based Stratospheric Aerosol Climatology Version 2.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1282032627-GES_DISC.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Tropical Rainfall Measuring Mission (TRMM). 2011-07-01. TRMM_3A25. TRMM Radar Rainfall Statistics L3 1 month (5 x 5) and (0.5  x 0.5) degree V7. Greenbelt, MD. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://disc.gsfc.nasa.gov/datacollection/TRMM_3A25_7.html.",
-            "issued": "2011-07-01",
-            "temporal": "1997-12-01T00:00:00Z/2015-04-01T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2016-04-20",
-            "keyword": [
-                "atmosphere",
-                "spectral/engineering",
-                "radar",
-                "precipitation",
-                "earth science"
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
-            "identifier": "C1282032627-GES_DISC",
-            "description": "The new version of these data is in GPM-like format (consistent with the GPM Dual-frequency Radar data format), and can be found under the name GPM_3PR.\n\nThis product consists of monthly statistics of the PR measurements at both a low (5 degrees x 5 degrees) and a high (0.5 degrees x 0.5 degrees) horizontal resolution. The low resolution grids are in the Planetary Grid 1 structure and include 1) mean and standard deviation of the rain rate, reflectivity, path-integrated attenuation (PIA), storm height, Xi, bright band height and the NUBF (Non-Uniform Beam Filling) correction; 2) rain fractions; 3) histograms of the storm height, bright-band height, snow-ice layer, reflectivity, rain rate, path-attenuation and NUBF correction; 4) correlation coefficients. The high resolution grids are in the Planetary Grid 2 structure and contain mean rain rate along with standard deviation and rain fractions.",
-            "release-place": "Greenbelt, MD",
-            "series-name": "TRMM_3A25",
             "creator": "Tropical Rainfall Measuring Mission (TRMM)",
-            "title": "TRMM Radar Rainfall Statistics L3 1 month (5 x 5) and (0.5  x 0.5) degree V7 (TRMM_3A25) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/TRMM_3A25_7.png",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The new version of these data is in GPM-like format (consistent with the GPM Dual-frequency Radar data format), and can be found under the name GPM_3PR.\n\nThis product consists of monthly statistics of the PR measurements at both a low (5 degrees x 5 degrees) and a high (0.5 degrees x 0.5 degrees) horizontal resolution. The low resolution grids are in the Planetary Grid 1 structure and include 1) mean and standard deviation of the rain rate, reflectivity, path-integrated attenuation (PIA), storm height, Xi, bright band height and the NUBF (Non-Uniform Beam Filling) correction; 2) rain fractions; 3) histograms of the storm height, bright-band height, snow-ice layer, reflectivity, rain rate, path-attenuation and NUBF correction; 4) correlation coefficients. The high resolution grids are in the Planetary Grid 2 structure and contain mean rain rate along with standard deviation and rain fractions.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -1395856,298 +1395832,302 @@
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/TRMM_3A25_7.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/TRMM_3A25_7.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc2.gesdisc.eosdis.nasa.gov/data/TRMM_L3/TRMM_3A25.7",
-                    "description": "Access the data via HTTPS",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS",
+                    "downloadURL": "https://disc2.gesdisc.eosdis.nasa.gov/data/TRMM_L3/TRMM_3A25.7",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc2.gesdisc.eosdis.nasa.gov/opendap/TRMM_L3/TRMM_3A25.7/",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://disc2.gesdisc.eosdis.nasa.gov/opendap/TRMM_L3/TRMM_3A25.7/",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc2.gesdisc.eosdis.nasa.gov/thredds/catalog/aggregation/TRMM_3A25.7/catalog.html",
-                    "description": "Access the data via the THREDDS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the THREDDS.",
+                    "downloadURL": "https://disc2.gesdisc.eosdis.nasa.gov/thredds/catalog/aggregation/TRMM_3A25.7/catalog.html",
+                    "mediaType": "text/html",
                     "title": "Use THREDDS DATA to download the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=TRMM_3A25",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=TRMM_3A25",
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
-                    "downloadURL": "https://disc2.gesdisc.eosdis.nasa.gov/data/TRMM_L3/TRMM_3A25/doc/README.TRMM_V7.pdf",
-                    "description": "README Document",
                     "@type": "dcat:Distribution",
+                    "description": "README Document",
+                    "downloadURL": "https://disc2.gesdisc.eosdis.nasa.gov/data/TRMM_L3/TRMM_3A25/doc/README.TRMM_V7.pdf",
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
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/TRMM_3A25_7.png",
+            "identifier": "C1282032627-GES_DISC",
+            "issued": "2011-07-01",
+            "keyword": [
+                "atmosphere",
+                "spectral/engineering",
+                "radar",
+                "precipitation",
+                "earth science"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1282032627-GES_DISC.html",
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
+            "series-name": "TRMM_3A25",
             "spatial": "-180.0 -40.0 180.0 40.0",
+            "temporal": "1997-12-01T00:00:00Z/2015-04-01T23:59:59.999Z",
             "theme": [
                 "TRMM",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "TRMM Radar Rainfall Statistics L3 1 month (5 x 5) and (0.5  x 0.5) degree V7 (TRMM_3A25) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/GCPEX/NEXRAD/DATA207",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "National Climatic Data Center.2015. GPM GROUND VALIDATION KTYX NEXRAD GCPEX [indicate subset used]. Dataset available online from the NASA Global Hydrometeorology Resource Center DAAC, Huntsville, Alabama, U.S.A. DOI: http://dx.doi.org/10.5067/GCPEX/NEXRAD/DATA207",
-            "issued": "2015-06-09",
-            "temporal": "2012-01-09T16:51:47Z/2012-03-12T13:11:15Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-05-10",
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
-            "identifier": "C1982757348-GHRC_DAAC",
             "description": "The GPM Ground Validation KTYX NEXRAD GCPEx dataset was collected during January 9, 2012 to March 12, 2012 for the GPM Cold-season Precipitation Experiment (GCPEx). GCPEx addressed shortcomings in GPM snowfall retrieval algorithm by collecting microphysical properties, associated remote sensing observations, and coordinated model simulations of precipitating snow. These data sets were collected toward achieving the overarching goal of GCPEx which is to characterize the ability of multi-frequency active and passive microwave sensors to detect and estimate falling snow. The Next Generation Weather Radar system (NEXRAD) is comprised of 160 Weather Surveillance Radar-1988 Doppler (WSR-88D) sites throughout the United States and select overseas locations. The GPM Ground Validation NEXRAD GCPEx data files are available as level 2 binary files and level 3 compressed binary files.",
-            "graphic-preview-description": "N/A",
-            "title": "GPM GROUND VALIDATION KTYX NEXRAD GCPEX V1",
-            "graphic-preview-file": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/gcpex/NEXRAD/KTYX/browse/",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGCPEX%2FNEXRAD%2FDATA207",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGCPEX%2FNEXRAD%2FDATA207",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=gpmktyxgcpex",
-                    "description": "Files may be downloaded directly to your workstation from this link",
                     "@type": "dcat:Distribution",
+                    "description": "Files may be downloaded directly to your workstation from this link",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=gpmktyxgcpex",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/gcpex/NEXRAD/KTYX/browse/2012-01-31/2012-01-31_05-16-38_KTYX_ELEV_01.png",
-                    "description": "Sample browse image",
                     "@type": "dcat:Distribution",
+                    "description": "Sample browse image",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/gcpex/NEXRAD/KTYX/browse/2012-01-31/2012-01-31_05-16-38_KTYX_ELEV_01.png",
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
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/doc/gpmgv/gcpex/doc_aggregate/nexradgcpex/gpmnexradgcpex_dataset.html",
-                    "description": "The guide document contains detailed information about the dataset",
                     "@type": "dcat:Distribution",
+                    "description": "The guide document contains detailed information about the dataset",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/doc/gpmgv/gcpex/doc_aggregate/nexradgcpex/gpmnexradgcpex_dataset.html",
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
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/gcpex/NEXRAD/KTYX/browse/",
-                    "description": "N/A",
                     "@type": "dcat:Distribution",
+                    "description": "N/A",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/gcpex/NEXRAD/KTYX/browse/",
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
+            "graphic-preview-file": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/gcpex/NEXRAD/KTYX/browse/",
+            "identifier": "C1982757348-GHRC_DAAC",
+            "issued": "2015-06-09",
+            "keyword": [
+                "radar",
+                "earth science",
+                "spectral/engineering"
+            ],
+            "landingPage": "https://doi.org/10.5067/GCPEX/NEXRAD/DATA207",
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
             "spatial": "-81.39 39.62 -69.96 47.89",
+            "temporal": "2012-01-09T16:51:47Z/2012-03-12T13:11:15Z",
             "theme": [
                 "GCPEx",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "GPM GROUND VALIDATION KTYX NEXRAD GCPEX V1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-E-OSINAC-2-EAR1-EARTHSWINGBY1-V1.4",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This data set contains images acquired by the OSIRIS Narrow Angle Camera\nduring the EARTH SWING-BY 1 mission phase",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-e-osinac-2-ear1-earthswingby1-v1.4_t63f-uqmy",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "international rosetta mission",
                 "dark",
                 "calibration"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-E-OSINAC-2-EAR1-EARTHSWINGBY1-V1.4",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-e-osinac-2-ear1-earthswingby1-v1.4_t63f-uqmy",
-            "description": "This data set contains images acquired by the OSIRIS Narrow Angle Camera\nduring the EARTH SWING-BY 1 mission phase",
-            "title": "ROSETTA-ORBITER EARTH SWING-BY 1 OSINAC\n                                      2 EDR V1.4",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER EARTH SWING-BY 1 OSINAC\n                                      2 EDR V1.4"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=JUNO-J-JUNOCAM-3-RDR-L1A-V1.0",
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
-                "juno"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "NULL",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.juno-j-junocam-3-rdr-l1a-v1.0_t64u-hapz",
+            "issued": "2018-06-26",
+            "keyword": [
+                "jupiter",
+                "juno"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=JUNO-J-JUNOCAM-3-RDR-L1A-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.juno-j-junocam-3-rdr-l1a-v1.0_t64u-hapz",
-            "description": "NULL",
-            "title": "JUNO JUPITER JUNOCAM 3 RDR\n\t\t\t\t      L1A V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "JUNO JUPITER JUNOCAM 3 RDR\n\t\t\t\t      L1A V1.0"
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
-                "validation",
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
-            "identifier": "NASA-581",
             "description": "PDS Validation Tool (2.1.0)",
-            "title": "PDS Software Release Validation Tool (2.1.0)",
-            "programCode": [
-                "026:005"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -1396155,437 +1396135,459 @@
                     "mediaType": "application/html"
                 }
             ],
-            "accrualPeriodicity": "irregular",
+            "identifier": "NASA-581",
+            "issued": "2018-06-25",
+            "keyword": [
+                "tool",
+                "validation",
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
+            "title": "PDS Software Release Validation Tool (2.1.0)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/CYGNS-L2H20",
             "citation": "CYGNSS. 2022-08-01. CYGNSS Level 2 Ocean Surface Heat Flux Science Data Record. Version 2.0. CYGNSS Level 2 Ocean Surface Heat Flux Science Data Record Version 2.0. PO.DAAC. Archived by National Aeronautics and Space Administration, U.S. Government, PO.DAAC. https://doi.org/10.5067/CYGNS-L2H20. https://cygnss.engin.umich.edu/. CYGNSS, PO.DAAC, 2019-08-11, CYGNSS Level 2 Ocean Surface Heat Flux Science Data Record Version 1.0, https://cygnss.engin.umich.edu/.",
-            "issued": "2022-04-16",
-            "temporal": "2018-08-01T00:00:00Z/2023-02-28T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-04-29",
-            "references": [
-                "https://doi.org/10.3390/rs11192294"
-            ],
-            "keyword": [
-                "ocean temperature",
-                "oceans",
-                "ocean heat budget",
-                "earth science"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "undefined",
                 "hasEmail": "mailto:podaac@podaac.jpl.nasa.gov"
             },
-            "identifier": "C2247621105-POCLOUD",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/JPL/PODAAC"
-            },
-            "description": "This dataset contains the Version 2.0 CYGNSS Level 2 Ocean Surface Heat Flux Science Data Record, which provides time-tagged and geolocated ocean surface heat flux parameters with 25x25 kilometer footprint resolution from the Delay Doppler Mapping Instrument (DDMI) aboard the CYGNSS satellite constellation. The reported sample locations are determined by the specular points corresponding to the Delay Doppler Maps (DDMs). Version 2.0 represents the second release of this product, which now uses CYGNSS Level 2 (L2) Science Data Record (SDR) Version 3.1 surface wind speeds and ECMWF Reanalysis, Version 5 (ERA5). Version 1.0 used CYGNSS L2 SDR Version 2.1 surface wind speeds and NASA Modern-Era Retrospective Analysis for Research and Applications Version 2 (MERRA-2). The Coupled Ocean-Atmosphere Response Experiment (COARE) algorithm is what is used in this dataset to estimate the latent and sensible heat fluxes and their respective transfer coefficients. While COARE's initial intentions were for low to moderate wind speeds, the version used for this product, COARE 3.5, has been verified with direct in situ flux measurements for wind speeds up to 25 m/s. As CYGNSS does not provide air/sea temperature, humidity, surface pressure or density, the producer of this dataset obtains these values from this dataset obtains these values from ERA5. The Cyclone Global Navigation Satellite System (CYGNSS), launched on 15 December 2016, is a NASA Earth System Science Pathfinder Mission that was launched with the purpose to collect the first frequent space-based measurements of surface wind speeds in the inner core of tropical cyclones. Made up of a constellation of eight micro-satellites, the CYGNSS observatories provide nearly gap-free Earth coverage with a mean (i.e., average) revisit time of seven hours and a median revisit time of three hours. As a result of the CYGNSS constellation coverage, this data is made available from 1 August 2018 to present with an approximate 1 week latency in the netCDF-4 formatted data files, where each file contains data within a 24-hour UTC period from a combination of up to 8 unique CYGNSS spacecraft. More information on CYGNSS can be found on the CYGNSS mission page.",
-            "release-place": "PO.DAAC",
-            "series-name": "CYGNSS Level 2 Ocean Surface Heat Flux Science Data Record",
             "creator": "CYGNSS",
-            "title": "CYGNSS Level 2 Ocean Surface Heat Flux Science Data Record Version 2.0",
-            "graphic-preview-description": "Thumbnail",
-            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/CYGNSS_L2_SURFACE_FLUX_V2.0.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "This dataset contains the Version 2.0 CYGNSS Level 2 Ocean Surface Heat Flux Science Data Record, which provides time-tagged and geolocated ocean surface heat flux parameters with 25x25 kilometer footprint resolution from the Delay Doppler Mapping Instrument (DDMI) aboard the CYGNSS satellite constellation. The reported sample locations are determined by the specular points corresponding to the Delay Doppler Maps (DDMs). Version 2.0 represents the second release of this product, which now uses CYGNSS Level 2 (L2) Science Data Record (SDR) Version 3.1 surface wind speeds and ECMWF Reanalysis, Version 5 (ERA5). Version 1.0 used CYGNSS L2 SDR Version 2.1 surface wind speeds and NASA Modern-Era Retrospective Analysis for Research and Applications Version 2 (MERRA-2). The Coupled Ocean-Atmosphere Response Experiment (COARE) algorithm is what is used in this dataset to estimate the latent and sensible heat fluxes and their respective transfer coefficients. While COARE's initial intentions were for low to moderate wind speeds, the version used for this product, COARE 3.5, has been verified with direct in situ flux measurements for wind speeds up to 25 m/s. As CYGNSS does not provide air/sea temperature, humidity, surface pressure or density, the producer of this dataset obtains these values from this dataset obtains these values from ERA5. The Cyclone Global Navigation Satellite System (CYGNSS), launched on 15 December 2016, is a NASA Earth System Science Pathfinder Mission that was launched with the purpose to collect the first frequent space-based measurements of surface wind speeds in the inner core of tropical cyclones. Made up of a constellation of eight micro-satellites, the CYGNSS observatories provide nearly gap-free Earth coverage with a mean (i.e., average) revisit time of seven hours and a median revisit time of three hours. As a result of the CYGNSS constellation coverage, this data is made available from 1 August 2018 to present with an approximate 1 week latency in the netCDF-4 formatted data files, where each file contains data within a 24-hour UTC period from a combination of up to 8 unique CYGNSS spacecraft. More information on CYGNSS can be found on the CYGNSS mission page.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FCYGNS-L2H20",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FCYGNS-L2H20",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
-                },
-                {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/cygnss/open/L2/docs/148-0138_ATBD_L2_Wind_Speed_Retrieval_Rev5_Aug2018_release.pdf",
-                    "description": "Level 2 Wind Speed Retrieval Algorithm Theoretical Basis Document, M. P. Clarizia, V. Zavarotny, C. Ruf, CYGNSS Project Document 148-0138, Rev 5, 17 Aug. 2018.",
+                },
+                {
                     "@type": "dcat:Distribution",
+                    "description": "Level 2 Wind Speed Retrieval Algorithm Theoretical Basis Document, M. P. Clarizia, V. Zavarotny, C. Ruf, CYGNSS Project Document 148-0138, Rev 5, 17 Aug. 2018.",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/cygnss/open/L2/docs/148-0138_ATBD_L2_Wind_Speed_Retrieval_Rev5_Aug2018_release.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's algorithm theoretical basis document"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.1109/TGRS.2016.2541343",
-                    "description": "Clarizia, M. P., and C. S. Ruf, 'Wind Speed Retrieval Algorithm for the Cyclone Global Navigation Satellite System (CYGNSS) Mission', IEEE Trans Geosci. Remote Sens., doi:10.1109/TGRS.2016.2541343, 2016.",
                     "@type": "dcat:Distribution",
+                    "description": "Clarizia, M. P., and C. S. Ruf, 'Wind Speed Retrieval Algorithm for the Cyclone Global Navigation Satellite System (CYGNSS) Mission', IEEE Trans Geosci. Remote Sens., doi:10.1109/TGRS.2016.2541343, 2016.",
+                    "downloadURL": "https://doi.org/10.1109/TGRS.2016.2541343",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/cygnss/open/L2/docs/cygnss_l2_sdr_heat_flux_user_guide_v2.0.pdf",
-                    "description": "User Guide for the CYGNSS Surface Flux Dataset",
                     "@type": "dcat:Distribution",
+                    "description": "User Guide for the CYGNSS Surface Flux Dataset",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/cygnss/open/L2/docs/cygnss_l2_sdr_heat_flux_user_guide_v2.0.pdf",
+                    "mediaType": "application/pdf",
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
-                    "downloadURL": "https://cygnss.engin.umich.edu/",
-                    "description": "CYGNSS Mission Page at University of Michigan",
                     "@type": "dcat:Distribution",
+                    "description": "CYGNSS Mission Page at University of Michigan",
+                    "downloadURL": "https://cygnss.engin.umich.edu/",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/CYGNSS_L2_SURFACE_FLUX_V2.0.jpg",
-                    "description": "Thumbnail",
                     "@type": "dcat:Distribution",
+                    "description": "Thumbnail",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/CYGNSS_L2_SURFACE_FLUX_V2.0.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.1175/BAMS-D-14-00218.1",
-                    "description": "Ruf, C., R. Atlas, P. Chang, M. Clarizia, J. Garrison, S. Gleason, S. Katzberg, Z. Jelenak, J. Johnson, S. Majumdar, A. O'Brien, D. Posselt, A. Ridley, R. Rose, V. Zavorotny (2015). New Ocean Winds Satellite Mission to Probe Hurricanes and Tropical Convection. Bull. Amer. Meteor. Soc., doi:10.1175/BAMS-D-14-00218.1.",
                     "@type": "dcat:Distribution",
+                    "description": "Ruf, C., R. Atlas, P. Chang, M. Clarizia, J. Garrison, S. Gleason, S. Katzberg, Z. Jelenak, J. Johnson, S. Majumdar, A. O'Brien, D. Posselt, A. Ridley, R. Rose, V. Zavorotny (2015). New Ocean Winds Satellite Mission to Probe Hurricanes and Tropical Convection. Bull. Amer. Meteor. Soc., doi:10.1175/BAMS-D-14-00218.1.",
+                    "downloadURL": "https://doi.org/10.1175/BAMS-D-14-00218.1",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
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
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/cygnss/open/L2/docs/148-0382-4_Level_2_Surface_Flux_netCDF_Data_Dictionary.xlsx",
-                    "description": "Data Variable Dictionary",
                     "@type": "dcat:Distribution",
+                    "description": "Data Variable Dictionary",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/cygnss/open/L2/docs/148-0382-4_Level_2_Surface_Flux_netCDF_Data_Dictionary.xlsx",
+                    "mediaType": "text/html",
                     "title": "View this dataset's user's guide"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.1175/BAMS-D-18-0337.1",
-                    "description": "Ruf, C., S. Asharaf, R. Balasubramaniam, S. Gleason, T. Lang, D. McKague, D. Twigg, and D. Waliser. (2019). In-Orbit Performance of the Constellation of CYGNSS Hurricane Satellites. Bull. Amer. Meteor. Soc., 100, 2009 - 2023, https://doi.org/10.1175/BAMS-D-18-0337.1.",
                     "@type": "dcat:Distribution",
+                    "description": "Ruf, C., S. Asharaf, R. Balasubramaniam, S. Gleason, T. Lang, D. McKague, D. Twigg, and D. Waliser. (2019). In-Orbit Performance of the Constellation of CYGNSS Hurricane Satellites. Bull. Amer. Meteor. Soc., 100, 2009 - 2023, https://doi.org/10.1175/BAMS-D-18-0337.1.",
+                    "downloadURL": "https://doi.org/10.1175/BAMS-D-18-0337.1",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3390/rs11192294",
-                    "description": "Crespo, J. A., Posselt, D. J., & Asharaf, S. (2019). CYGNSS Surface Heat Flux Product Development. Remote Sens. 2019, 11, 2294. DOI: 10.3390/rs11192294.",
                     "@type": "dcat:Distribution",
+                    "description": "Crespo, J. A., Posselt, D. J., & Asharaf, S. (2019). CYGNSS Surface Heat Flux Product Development. Remote Sens. 2019, 11, 2294. DOI: 10.3390/rs11192294.",
+                    "downloadURL": "https://doi.org/10.3390/rs11192294",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.1109/JSTARS.2018.2833075",
-                    "description": "Ruf, C., R. Balasubramaniam, 'Development of the CYGNSS Geophysical Model Function for Wind Speed', IEEE J. Sel. Topics Appl. Earth Obs. Remote Sens., doi: 10.1109/JSTARS.2018.2833075, 2018.",
                     "@type": "dcat:Distribution",
+                    "description": "Ruf, C., R. Balasubramaniam, 'Development of the CYGNSS Geophysical Model Function for Wind Speed', IEEE J. Sel. Topics Appl. Earth Obs. Remote Sens., doi: 10.1109/JSTARS.2018.2833075, 2018.",
+                    "downloadURL": "https://doi.org/10.1109/JSTARS.2018.2833075",
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
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2247621105-POCLOUD",
-                    "description": "HTTPS endpoint for data browse and download",
                     "@type": "dcat:Distribution",
+                    "description": "HTTPS endpoint for data browse and download",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2247621105-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=+C2247621105-POCLOUD",
-                    "description": "Browse granule search results in Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse granule search results in Earthdata Search",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=+C2247621105-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
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
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/cygnss/open/L1/docs/att_tables/Attitude_Table_FM_1.txt",
-                    "description": "Spacecraft Attitude Tables Updated Monthly",
                     "@type": "dcat:Distribution",
+                    "description": "Spacecraft Attitude Tables Updated Monthly",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/cygnss/open/L1/docs/att_tables/Attitude_Table_FM_1.txt",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/cygnss/open/L1/docs/att_tables/Attitude_Table_FM_2.txt",
-                    "description": "Spacecraft Attitude Tables Updated Monthly",
                     "@type": "dcat:Distribution",
+                    "description": "Spacecraft Attitude Tables Updated Monthly",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/cygnss/open/L1/docs/att_tables/Attitude_Table_FM_2.txt",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/cygnss/open/L1/docs/att_tables/Attitude_Table_FM_3.txt",
-                    "description": "Spacecraft Attitude Tables Updated Monthly",
                     "@type": "dcat:Distribution",
+                    "description": "Spacecraft Attitude Tables Updated Monthly",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/cygnss/open/L1/docs/att_tables/Attitude_Table_FM_3.txt",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/cygnss/open/L1/docs/att_tables/Attitude_Table_FM_4.txt",
-                    "description": "Spacecraft Attitude Tables Updated Monthly",
                     "@type": "dcat:Distribution",
+                    "description": "Spacecraft Attitude Tables Updated Monthly",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/cygnss/open/L1/docs/att_tables/Attitude_Table_FM_4.txt",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/cygnss/open/L1/docs/att_tables/Attitude_Table_FM_5.txt",
-                    "description": "Spacecraft Attitude Tables Updated Monthly",
                     "@type": "dcat:Distribution",
+                    "description": "Spacecraft Attitude Tables Updated Monthly",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/cygnss/open/L1/docs/att_tables/Attitude_Table_FM_5.txt",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/cygnss/open/L1/docs/att_tables/Attitude_Table_FM_6.txt",
-                    "description": "Spacecraft Attitude Tables Updated Monthly",
                     "@type": "dcat:Distribution",
+                    "description": "Spacecraft Attitude Tables Updated Monthly",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/cygnss/open/L1/docs/att_tables/Attitude_Table_FM_6.txt",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/cygnss/open/L1/docs/att_tables/Attitude_Table_FM_7.txt",
-                    "description": "Spacecraft Attitude Tables Updated Monthly",
                     "@type": "dcat:Distribution",
+                    "description": "Spacecraft Attitude Tables Updated Monthly",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/cygnss/open/L1/docs/att_tables/Attitude_Table_FM_7.txt",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/cygnss/open/L1/docs/att_tables/Attitude_Table_FM_8.txt",
-                    "description": "Spacecraft Attitude Tables Updated Monthly",
                     "@type": "dcat:Distribution",
+                    "description": "Spacecraft Attitude Tables Updated Monthly",
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
+            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/CYGNSS_L2_SURFACE_FLUX_V2.0.jpg",
+            "identifier": "C2247621105-POCLOUD",
+            "issued": "2022-04-16",
+            "keyword": [
+                "ocean temperature",
+                "oceans",
+                "ocean heat budget",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/CYGNS-L2H20",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2022-04-29",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/JPL/PODAAC"
+            },
+            "references": [
+                "https://doi.org/10.3390/rs11192294"
+            ],
+            "release-place": "PO.DAAC",
+            "series-name": "CYGNSS Level 2 Ocean Surface Heat Flux Science Data Record",
             "spatial": "-180.0 -38.0 180.0 38.0",
+            "temporal": "2018-08-01T00:00:00Z/2023-02-28T00:00:00Z",
             "theme": [
                 "CYGNSS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "CYGNSS Level 2 Ocean Surface Heat Flux Science Data Record Version 2.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/SUOMI-NPP/VIIRS/L3M/CHL/2022",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/GSFC/SED/ESD/GCDC/OB.DAAC. https://doi.org/10.5067/SUOMI-NPP/VIIRS/L3M/CHL/2022.",
-            "issued": "2022-09-14",
-            "temporal": "2012-01-02T00:00:00Z/2023-02-28T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-09-14",
-            "keyword": [
-                "earth science",
-                "oceans",
-                "ocean optics",
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
-            "identifier": "C2340494100-OB_DAAC",
             "description": "The Visible and Infrared Imager/Radiometer Suite (VIIRS) is a multi-disciplinary instrument that is being flown on the Joint Polar Satellite System (JPSS) series of spacecraft, including the Suomi National Polar-orbiting Partnership (S-NPP) that launched in October 2011.  JPSS is a multi-platform, multi-agency program that consolidates the polar orbiting spacecraft of NASA and the National Oceanic and Atmospheric Administration (NOAA).  S-NPP is the initial spacecraft in this series, and VIIRS is the successor to MODIS for Earth science data product generation.  VIIRS has 22 spectral bands ranging from 412 nm to 12 nm.  There are 16 moderate-resolution bands (750m at nadir), 5 image-resolution bands (375m), and one day-night band (DNB).",
-            "title": "Suomi-NPP VIIRS Global Mapped Chlorophyll (CHL) Data, version R2022.0",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSUOMI-NPP%2FVIIRS%2FL3M%2FCHL%2F2022",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSUOMI-NPP%2FVIIRS%2FL3M%2FCHL%2F2022",
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
-                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/data/10.5067/SUOMI-NPP/VIIRS/L3M/CHL/2022",
-                    "description": "VIIRS-Suomi-NPP L3M Chlorophyll (CHL) Dataset Landing Page",
                     "@type": "dcat:Distribution",
+                    "description": "VIIRS-Suomi-NPP L3M Chlorophyll (CHL) Dataset Landing Page",
+                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/data/10.5067/SUOMI-NPP/VIIRS/L3M/CHL/2022",
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
+            "identifier": "C2340494100-OB_DAAC",
+            "issued": "2022-09-14",
+            "keyword": [
+                "earth science",
+                "oceans",
+                "ocean optics",
+                "ocean chemistry"
+            ],
+            "landingPage": "https://doi.org/10.5067/SUOMI-NPP/VIIRS/L3M/CHL/2022",
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
+            "title": "Suomi-NPP VIIRS Global Mapped Chlorophyll (CHL) Data, version R2022.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.7265/N59884X1",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "March through August Ice Edge Positions in the Nordic Seas, 1750-2002, Version 1. Version 1. Archived by National Aeronautics and Space Administration, U.S. Government, National Snow and Ice Data Center. https://doi.org/10.7265/N59884X1.",
-            "issued": "1750-03-01",
-            "temporal": "1750-03-01T00:00:00Z/2002-08-31T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2002-08-31",
-            "keyword": [
-                "oceans",
-                "sea ice",
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
-                "name": "NSIDC"
-            },
-            "identifier": "C1386246265-NSIDCV0",
             "description": "This product contains ice edge coordinates for the Nordic Seas from 1750 through 2002 for months March through August. Ice edge in this product is defined as the outer boundary of ice having at least 30 percent ice concentration. Data are derived from publicly available sea ice products and use observational data from ship logbooks, diaries, and other sources in addition to more recent satellite data products from the Scanning Multichannel Microwave Radiometer (SMMR) and the Special Sensor Microwave Imager (SSM/I).",
-            "title": "March through August Ice Edge Positions in the Nordic Seas, 1750-2002, Version 1",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.7265%2FN59884X1",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.7265%2FN59884X1",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/forms/G02169_or.html?major_version=1",
-                    "description": "Direct download, with optional registration page.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download, with optional registration page.",
+                    "downloadURL": "https://nsidc.org/forms/G02169_or.html?major_version=1",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/forms/G02169_or.html?major_version=1",
-                    "description": "Direct download, with optional registration page.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download, with optional registration page.",
+                    "downloadURL": "https://nsidc.org/forms/G02169_or.html?major_version=1",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/forms/G02169_or.html?major_version=1",
-                    "description": "Direct download, with optional registration page.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download, with optional registration page.",
+                    "downloadURL": "https://nsidc.org/forms/G02169_or.html?major_version=1",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.7265/N59884X1",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.7265/N59884X1",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.7265/N59884X1",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.7265/N59884X1",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C1386246265-NSIDCV0",
+            "issued": "1750-03-01",
+            "keyword": [
+                "oceans",
+                "sea ice",
+                "cryosphere",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.7265/N59884X1",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2002-08-31",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NSIDC"
+            },
             "spatial": "-36.2 57.7 64.2 86.0",
+            "temporal": "1750-03-01T00:00:00Z/2002-08-31T23:59:59.999Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "March through August Ice Edge Positions in the Nordic Seas, 1750-2002, Version 1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=LCROSS-E%2FL-MIR1-2-RAW-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "Raw, uncalibrated image data from the Mid Infrared Camera 1 (MIR1) aboard the Lunar Crater Observation and Sensing Satellite (LCROSS).",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.lcross-e-l-mir1-2-raw-v1.0_t696-mfdr",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "calibration",
                 "earth",
@@ -1396593,111 +1396595,120 @@
                 "moon",
                 "test image"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=LCROSS-E%2FL-MIR1-2-RAW-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.lcross-e-l-mir1-2-raw-v1.0_t696-mfdr",
-            "description": "Raw, uncalibrated image data from the Mid Infrared Camera 1 (MIR1) aboard the Lunar Crater Observation and Sensing Satellite (LCROSS).",
-            "title": "LCROSS EARTH/MOON 1ST MID IR CAMERA 2 RAW V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "LCROSS EARTH/MOON 1ST MID IR CAMERA 2 RAW V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=CO-S-RSS-1-SROC26-V1.0",
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
-                "saturn",
-                "cassini-huygens"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "The Cassini Radio Science Saturn Ring and Atmospheric Occultation experiments (SROC26) Raw Data Archive is a time-ordered collection of radio science raw data acquired on July 6 and on September 15, 2017, during the Cassini Extended Extended Mission.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.co-s-rss-1-sroc26-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "saturn",
+                "cassini-huygens"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=CO-S-RSS-1-SROC26-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.co-s-rss-1-sroc26-v1.0",
-            "description": "The Cassini Radio Science Saturn Ring and Atmospheric Occultation experiments (SROC26) Raw Data Archive is a time-ordered collection of radio science raw data acquired on July 6 and on September 15, 2017, during the Cassini Extended Extended Mission.",
-            "title": "CASSINI RSS RAW DATA SET - SROC26 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "CASSINI RSS RAW DATA SET - SROC26 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG1-S-PLS-5-SUMM-IONFIT-96SEC-V1.0",
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
+            "description": "THIS DATA SET CONTAINS THE ION PARAMETERS IN THE PLS VOLTAGE RANGE (10-5950 EV/Q) WITH FORMAL 1 SIGMA ERRORS OBTAINED FROM VOYAGER 1 DATA AT SATURN BY FITTING THE MEASURED SPECTRA WITH ISOTROPIC MAXWELLIAN DISTRIBUTIONS TO OBTAIN PLASMA DENSITIES, TEMPERATURES, AND VELOCITY.  ONLY SPECTRA WHICH HAD DISTINCT CURRENT PEAKS WERE FIT.  SPECTRA WERE FIT USING ONE OR TWO ION SPECIES, PROTONS AND/OR A HEAVY ION WHICH WAS TAKEN TO BE NITROGEN OUTSIDE OF 14 RS AND OXYGEN ELSEWHERE.  OUTSIDE L=10-12 ION SPECTRA CHANGE RAPIDLY, SO THE VALUES IN THIS DATA SET DO NOT REPRESENT AVERAGE PLASMA CONDITIONS IN THE OUTER MAGNETOSPHERE.  THE VALUES FOR POSITION AND MAGNETIC FIELD GIVEN IN THE DATA SET ARE ONLY APPROXIMATE AND SHOULD NOT BE USED FOR PUBLICATION.  PARAMETERS WHICH ARE IDENTICALLY 0 AND HAVE UNCERTAINTIES OF 0 WERE NOT FIT DUE TO INSUFFICIENT DATA; THESE NUMBERS ARE THUS NOT REAL VALUES.  A COMPLETE DESCRIPTION OF THIS DATA SET IS GIVEN IN RICHARDSON (1986).",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg1-s-pls-5-summ-ionfit-96sec-v1.0_t6di-jtym",
+            "issued": "2021-05-21",
+            "keyword": [
+                "voyager",
+                "saturn"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG1-S-PLS-5-SUMM-IONFIT-96SEC-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg1-s-pls-5-summ-ionfit-96sec-v1.0_t6di-jtym",
-            "description": "THIS DATA SET CONTAINS THE ION PARAMETERS IN THE PLS VOLTAGE RANGE (10-5950 EV/Q) WITH FORMAL 1 SIGMA ERRORS OBTAINED FROM VOYAGER 1 DATA AT SATURN BY FITTING THE MEASURED SPECTRA WITH ISOTROPIC MAXWELLIAN DISTRIBUTIONS TO OBTAIN PLASMA DENSITIES, TEMPERATURES, AND VELOCITY.  ONLY SPECTRA WHICH HAD DISTINCT CURRENT PEAKS WERE FIT.  SPECTRA WERE FIT USING ONE OR TWO ION SPECIES, PROTONS AND/OR A HEAVY ION WHICH WAS TAKEN TO BE NITROGEN OUTSIDE OF 14 RS AND OXYGEN ELSEWHERE.  OUTSIDE L=10-12 ION SPECTRA CHANGE RAPIDLY, SO THE VALUES IN THIS DATA SET DO NOT REPRESENT AVERAGE PLASMA CONDITIONS IN THE OUTER MAGNETOSPHERE.  THE VALUES FOR POSITION AND MAGNETIC FIELD GIVEN IN THE DATA SET ARE ONLY APPROXIMATE AND SHOULD NOT BE USED FOR PUBLICATION.  PARAMETERS WHICH ARE IDENTICALLY 0 AND HAVE UNCERTAINTIES OF 0 WERE NOT FIT DUE TO INSUFFICIENT DATA; THESE NUMBERS ARE THUS NOT REAL VALUES.  A COMPLETE DESCRIPTION OF THIS DATA SET IS GIVEN IN RICHARDSON (1986).",
-            "title": "VOYAGER 1 SATURN PLASMA DERIVED ION\n                                      FITS 96 SEC",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "VOYAGER 1 SATURN PLASMA DERIVED ION\n                                      FITS 96 SEC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.nasa.gov/d/t6jr-uws2",
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
+                    "downloadURL": "https://eosweb.larc.nasa.gov/project/calipso/cal_lid_l1-prov-v1-22_table",
+                    "mediaType": "text/html"
+                }
+            ],
+            "identifier": "NASA-0000197",
             "issued": "2018-06-25",
-            "temporal": "2007-08-06/2007-11-11",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
             "keyword": [
                 "climate",
                 "eos",
@@ -1396707,61 +1396718,34 @@
                 "atmospheric science",
                 "cloud"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "John M. Kusterer",
-                "hasEmail": "mailto:john.m.kusterer@nasa.gov"
-            },
+            "landingPage": "https://data.nasa.gov/d/t6jr-uws2",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:004"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "NASA-0000197",
-            "description": "Cloud-Aerosol Lidar and Infrared Pathfinder Satellite Observations (CALIPSO) was launched on April 28, 2006 to study the impact of clouds and aerosols on the Earth\u2019s radiation budget and climate. It flies in formation with five other satellites in the international \u201cA-Train\u201d (PDF) constellation for coincident Earth observations. The CALIPSO satellite comprises three instruments, the Cloud-Aerosol LIdar with Orthogonal Polarization (CALIOP), the Imaging Infrared Radiometer (IIR), and the Wide Field Camera (WFC). CALIPSO is a joint satellite mission between NASA and the French Agency, CNES. These data consist 5 km aerosol layer data.",
-            "title": "CALIPSO Lidar L1B Profile Data V1-22",
-            "programCode": [
-                "026:004"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://eosweb.larc.nasa.gov/project/calipso/cal_lid_l1-prov-v1-22_table",
-                    "mediaType": "text/html"
-                }
-            ],
-            "accrualPeriodicity": "irregular",
+            "temporal": "2007-08-06/2007-11-11",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "CALIPSO Lidar L1B Profile Data V1-22"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://curator.jsc.nasa.gov/antmet/hed/hed_compendium.cfm",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2018-06-25",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
-            "keyword": [
-                "space science",
-                "meteorites"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Nancy Todd",
                 "hasEmail": "mailto:nancy.s.todd@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Aeronautics and Space Administration"
-            },
-            "identifier": "NASA-0000015",
             "description": "Image database of meteorites believed to have originated from Vesta.",
-            "title": "HED Compendium",
-            "programCode": [
-                "026:007"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -1396769,244 +1396753,262 @@
                     "mediaType": "text/html"
                 }
             ],
-            "accrualPeriodicity": "irregular",
+            "identifier": "NASA-0000015",
+            "issued": "2018-06-25",
+            "keyword": [
+                "space science",
+                "meteorites"
+            ],
+            "landingPage": "http://curator.jsc.nasa.gov/antmet/hed/hed_compendium.cfm",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:007"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Aeronautics and Space Administration"
+            },
             "theme": [
                 "Space Science"
-            ]
+            ],
+            "title": "HED Compendium"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/AURA/TES/TL3HDOM_L3.005",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2004-07-15. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/AURA/TES/TL3HDOM_L3.005. https://asdc.larc.nasa.gov/project/TES.",
-            "issued": "2015-08-27",
-            "temporal": "2004-09-03T00:00:00Z/2018-01-24T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2019-06-19",
-            "keyword": [
-                "atmospheric water vapor",
-                "atmosphere",
-                "atmospheric chemistry",
-                "atmospheric temperature",
-                "earth science"
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
-            "identifier": "C1536988699-LARC",
             "description": "TL3HDOM_5 is the Tropospheric Emission Spectrometer (TES)/Aura L3 Deuterium Oxide Monthly Gridded Version 5 data product. TES was an instrument aboard NASA's Aura satellite and was launched from California on July 15, 2004. Data collection for TES is complete. This product consisted of daily atmospheric temperature and volume mixing ratio (VMR) for the atmospheric species, which were provided at 2 degree latitude by 4 degree longitude spatial grids and at a subset of TES standard pressure levels. The TES Science Data Processing L3 subsystem interpolated the L2 atmospheric profiles collected in a Global Survey onto a global grid uniform in latitude and longitude to provide a 3-D representation of the distribution of atmospheric gasses. Daily and monthly averages of L2 profiles and browse images are available. \r\rThe L3 standard data products were composed of L3 HDF-EOS grid data. A separate product file was produced for each different atmospheric species. TES obtained data in two basic observation modes: Limb or Nadir. The product file may have contained, in separate folders, limb data, nadir data, or both folders may have been present. Specific to L3 processing were the terms Daily and Monthly, which represented the approximate time coverage of the L3 products. However, the input data granules to the L3 process were completed Global Surveys; in other words a Global Survey were not split in relation to time when input to the L3 processes even if they exceed the usual understood meanings of a day or month. More specifically, Daily L3 products represented a single Global Survey (approximately 26 hours) and Monthly L3 products represented Global Surveys that were initiated within that calendar month. The data granules defined for L3 standard products were daily and monthly. Details of the format of this product can be found in the TES Data Products Specifications (DPS).",
-            "title": "TES/Aura L3 Deuterium Oxide Monthly Gridded V005",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAURA%2FTES%2FTL3HDOM_L3.005",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAURA%2FTES%2FTL3HDOM_L3.005",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/tes/readme/level_3.pdf",
-                    "description": "TES Level 3 Versioning - Level 3 Global Survey Products",
                     "@type": "dcat:Distribution",
+                    "description": "TES Level 3 Versioning - Level 3 Global Survey Products",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/tes/readme/level_3.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's processing history"
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
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/tes/guide/TES_L3_Data_Users_Guide.pdf",
-                    "description": "TES Level 3 (L3) Data/Plot User\u2019s Guide Version 1.0 December 17, 2007",
                     "@type": "dcat:Distribution",
+                    "description": "TES Level 3 (L3) Data/Plot User\u2019s Guide Version 1.0 December 17, 2007",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/tes/guide/TES_L3_Data_Users_Guide.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/tes/guide/TES_L3_alg_req_prod.pdf",
-                    "description": "TES Level 3 Algorithms, Requirements & Products",
                     "@type": "dcat:Distribution",
+                    "description": "TES Level 3 Algorithms, Requirements & Products",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/tes/guide/TES_L3_alg_req_prod.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View the documentation for this dataset's algorithms"
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
-                    "downloadURL": "https://doi.org/10.5067/AURA/TES/TL3HDOM_L3.005",
-                    "description": "DOI data set landing page for TL3HDOM_5",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for TL3HDOM_5",
+                    "downloadURL": "https://doi.org/10.5067/AURA/TES/TL3HDOM_L3.005",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/TES/TL3HDOM.005/contents.html",
-                    "description": "OPeNDAP data access for TL3HDOM_5",
                     "@type": "dcat:Distribution",
+                    "description": "OPeNDAP data access for TL3HDOM_5",
+                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/TES/TL3HDOM.005/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1536988699-LARC",
-                    "description": "Earthdata Search for TL3HDOM_5 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for TL3HDOM_5 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1536988699-LARC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/TES/TL3HDOM.005/",
-                    "description": "ASDC Direct Data Download for TL3HDOM_5",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for TL3HDOM_5",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/TES/TL3HDOM.005/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
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
                 }
             ],
+            "identifier": "C1536988699-LARC",
+            "issued": "2015-08-27",
+            "keyword": [
+                "atmospheric water vapor",
+                "atmosphere",
+                "atmospheric chemistry",
+                "atmospheric temperature",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/AURA/TES/TL3HDOM_L3.005",
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
+            "temporal": "2004-09-03T00:00:00Z/2018-01-24T23:59:59Z",
             "theme": [
                 "TES",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "TES/Aura L3 Deuterium Oxide Monthly Gridded V005"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-4-ESC2-67P-M14-STR-REFL-V1.0",
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
+            "description": "This CODMAC level 4 data set contains solar stray light corrected, radiometric calibrated and geometric distortion corrected (resampled) image data in in reflectance units (normalized and thus without unit), acquired by the OSIRIS Narrow Angle Camera on the Rosetta spacecraft during the COMET ESCORT 2 mission phase, covering the period from 2015-03-10T23:25:00.000 to 2015-04-08T11:24:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V1.0 is the first version of this dataset: Lien corrected dataset after October 2018 PSA/PDS external peer review.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-4-esc2-67p-m14-str-refl-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-4-ESC2-67P-M14-STR-REFL-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-4-esc2-67p-m14-str-refl-v1.0",
-            "description": "This CODMAC level 4 data set contains solar stray light corrected, radiometric calibrated and geometric distortion corrected (resampled) image data in in reflectance units (normalized and thus without unit), acquired by the OSIRIS Narrow Angle Camera on the Rosetta spacecraft during the COMET ESCORT 2 mission phase, covering the period from 2015-03-10T23:25:00.000 to 2015-04-08T11:24:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V1.0 is the first version of this dataset: Lien corrected dataset after October 2018 PSA/PDS external peer review.",
-            "title": "ROSETTA-ORBITER 67P OSINAC 4 ESC2-MTP014 RDR-STR-REFL V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P OSINAC 4 ESC2-MTP014 RDR-STR-REFL V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-J-MVIC-2-JUPITER-V2.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This data set contains Raw data taken by the New Horizons Multispectral Visible Imaging Camera instrument during the Jupiter encounter mission phase.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-j-mvic-2-jupiter-v2.0_t6pp-8ggb",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "jupiter",
                 "ganymede",
@@ -1397016,73 +1397018,85 @@
                 "j2 europa",
                 "new horizons"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-J-MVIC-2-JUPITER-V2.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-j-mvic-2-jupiter-v2.0_t6pp-8ggb",
-            "description": "This data set contains Raw data taken by the New Horizons Multispectral Visible Imaging Camera instrument during the Jupiter encounter mission phase.",
-            "title": "NEW HORIZONS MVIC JUPITER ENCOUNTER V2.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "NEW HORIZONS MVIC JUPITER ENCOUNTER V2.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MER2-M-NAVCAM-3-RADIOMETRIC-SCI-V1.0",
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
+            "description": "This data set contains radiometrically calibrated MER-2 Navcam data. The calibration has removed bias, dark current, and flatfield effects from the raw Navcam data, resulting in estimated radiance-on-sensor data in units of W/m^2/nm/sr. No geometric or camera-model calibrations or transformations have been applied.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mer2-m-navcam-3-radiometric-sci-v1.0_t6py-kxgi",
+            "issued": "2021-05-21",
+            "keyword": [
+                "mars exploration rover",
+                "mars"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MER2-M-NAVCAM-3-RADIOMETRIC-SCI-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mer2-m-navcam-3-radiometric-sci-v1.0_t6py-kxgi",
-            "description": "This data set contains radiometrically calibrated MER-2 Navcam data. The calibration has removed bias, dark current, and flatfield effects from the raw Navcam data, resulting in estimated radiance-on-sensor data in units of W/m^2/nm/sr. No geometric or camera-model calibrations or transformations have been applied.",
-            "title": "MER 2 MARS NAVCAM 3 RADIOMETRIC RDR SCI\n                                      V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "MER 2 MARS NAVCAM 3 RADIOMETRIC RDR SCI\n                                      V1.0"
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
+                    "description": "Budget Estimate PDF",
+                    "downloadURL": "http://www.nasa.gov/sites/default/files/files/NASA_FY_2016_Budget_Estimates.pdf",
+                    "mediaType": "application/pdf",
+                    "title": "NASA Budget Estimates 2016"
+                }
+            ],
+            "identifier": "OCIO-Fitara-54",
             "issued": "2014-12-31",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
             "keyword": [
                 "finance",
                 "performance",
@@ -1397091,682 +1397105,682 @@
                 "strategic",
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
-            "identifier": "OCIO-Fitara-54",
-            "description": "NASA Financial Budget Documents, Strategic Plans and Performance Reports for fiscal year 2016.",
-            "title": "NASA Financial Budget Documents, Strategic Plans and Performance Reports 2016: NASA Budget Estimates",
-            "programCode": [
-                "026:046"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "http://www.nasa.gov/sites/default/files/files/NASA_FY_2016_Budget_Estimates.pdf",
-                    "description": "Budget Estimate PDF",
-                    "@type": "dcat:Distribution",
-                    "title": "NASA Budget Estimates 2016"
-                }
-            ],
-            "accrualPeriodicity": "R/P1Y",
             "theme": [
                 "Management/Operations"
-            ]
+            ],
+            "title": "NASA Financial Budget Documents, Strategic Plans and Performance Reports 2016: NASA Budget Estimates"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/NOAA20/CERES/ES9-FM6_L3.001",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2020-05-01. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/NOAA20/CERES/ES9-FM6_L3.001.",
-            "issued": "2020-03-13",
-            "temporal": "2018-05-01T00:00:00Z/2023-03-01T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-03-13",
-            "keyword": [
-                "atmosphere",
-                "earth science",
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
-            "identifier": "C2246001698-LARC_ASDC",
             "description": "CER_ES9_NOAA20-FM6_Edition1, CERES ERBE-like Monthly Regional Averages NOAA-20 FM6 Edition 1, contains TOA fluxes from the Clouds and the Earth's Radiant Energy System (CERES) instrument using algorithms identical to those used by ERBE, regional averages of instantaneous footprint TOA fluxes only for the hours of satellite overpass (from ES-8 Level 2 product). \r\nThe ERBE-like Monthly Regional Averages (ES-9) product contains a month of space and time averaged CERES data for a single scanner instrument. The ES-9 is also produced for combinations of scanner instruments. All instantaneous shortwave and longwave fluxes at the Top-of-the-Atmosphere (TOA) from the CERES ES-8 product for a month are sorted by 2.5-degree spatial regions, by day number, and by the local hour of observation. The mean of the instantaneous fluxes for a given region-day-hour bin is determined and recorded on the ES-9 along with other flux statistics and scene information. For each region, the daily average flux is estimated from an algorithm that uses the available hourly data, scene identification data, and diurnal models. This algorithm is like the algorithm used for the Earth Radiation Budget Experiment (ERBE). The ES-9 also contains hourly average fluxes for the month and an overall monthly average for each region. These average fluxes are given for both clear-sky and total-sky scenes. \r\n\r\nCERES is a key component of the Earth Observing System (EOS) program. The CERES instruments provide radiometric measurements of the Earth's atmosphere from three broadband channels. The CERES missions are a follow-on to the successful Earth Radiation Budget Experiment (ERBE) mission. The first CERES instrument (PFM) was launched on November 27, 1997 as part of the Tropical Rainfall Measuring Mission (TRMM). Two CERES instruments (FM1 and FM2) were launched into polar orbit on board the EOS flagship Terra on December 18, 1999. Two additional CERES instruments (FM3 and FM4) were launched on board EOS Aqua on May 4, 2002. T The CERES instrument (FM5) was launched on board the Suomi National Polar-orbiting Partnership (NPP) satellite on October 28, 2011. The last CERES instrument (FM6) was launched on board the Joint Polar-Orbiting Satellite System 1 (JPSS-1) satellite on November 18, 2017.",
-            "title": "CERES ERBE-like Monthly Regional Averages NOAA-20 FM6 Edition1",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FNOAA20%2FCERES%2FES9-FM6_L3.001",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FNOAA20%2FCERES%2FES9-FM6_L3.001",
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
-                    "downloadURL": "https://doi.org/10.5067/NOAA20/CERES/ES9-FM6_L3.001",
-                    "description": "DOI data set landing page for CER_ES9_NOAA20-FM6_Edition1",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for CER_ES9_NOAA20-FM6_Edition1",
+                    "downloadURL": "https://doi.org/10.5067/NOAA20/CERES/ES9-FM6_L3.001",
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
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/ceres/quality_summaries/CER_ES9_NOAA20_Edition1.pdf",
-                    "description": "Quality Summary: CERES ES9 NOAA-20 Edition 1",
                     "@type": "dcat:Distribution",
+                    "description": "Quality Summary: CERES ES9 NOAA-20 Edition 1",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/ceres/quality_summaries/CER_ES9_NOAA20_Edition1.pdf",
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
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://earthobservatory.nasa.gov/features/DelicateBalance/balance2.php",
-                    "description": "NASA Earth Observatory Article: A Delicate Balance: Signs of Change in the Tropics\u00a0-\u00a0New data sets were also used from NASA's Clouds and the Earth's Radiant Energy System (CERES) instruments that fly aboard the Tropical Rainfall Measuring Mission (TRMM) as well as the newer Terra satellite.",
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
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2246001698-LARC_ASDC",
-                    "description": "Earthdata Search for CER_ES9_NOAA20-FM6_Edition1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for CER_ES9_NOAA20-FM6_Edition1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2246001698-LARC_ASDC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/CERES/ES9/NOAA20-FM6_Edition1/",
-                    "description": "ASDC Direct Data Download for CER_ES9_NOAA20-FM6_Edition1",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for CER_ES9_NOAA20-FM6_Edition1",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/CERES/ES9/NOAA20-FM6_Edition1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/CERES/ES9/NOAA20-FM6_Edition1/contents.html",
-                    "description": "OPeNDAP data access for CER_ES9_NOAA20-FM6_Edition1",
                     "@type": "dcat:Distribution",
+                    "description": "OPeNDAP data access for CER_ES9_NOAA20-FM6_Edition1",
+                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/CERES/ES9/NOAA20-FM6_Edition1/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 }
             ],
+            "identifier": "C2246001698-LARC_ASDC",
+            "issued": "2020-03-13",
+            "keyword": [
+                "atmosphere",
+                "earth science",
+                "atmospheric radiation"
+            ],
+            "landingPage": "https://doi.org/10.5067/NOAA20/CERES/ES9-FM6_L3.001",
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
+            "temporal": "2018-05-01T00:00:00Z/2023-03-01T00:00:00Z",
             "theme": [
                 "CERES",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "CERES ERBE-like Monthly Regional Averages NOAA-20 FM6 Edition1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/VU8MI4QOA4NI",
             "citation": "Kevin W. Bowman. 2023-11-02. TRPSYL2PANCRSRS. Version 1. TROPESS CrIS-SNPP L2 Peroxyacetyl Nitrate for Reanalysis Stream, Summary Product V1. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/VU8MI4QOA4NI. https://disc.gsfc.nasa.gov/datacollection/TRPSYL2PANCRSRS_1.html. Digital Science Data.",
-            "issued": "2023-10-23",
-            "temporal": "2015-12-01T00:00:00Z/2023-11-06T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-10-23",
-            "references": [
-                "https://doi.org/10.1126/sciadv.abf7460",
-                "https://doi.org/10.5194/amt-7-3737-2014",
-                "https://doi.org/10.1109/TGRS.2006.871234",
-                "https://doi.org/10.1029/2002JD002299"
-            ],
-            "keyword": [
-                "atmospheric chemistry",
-                "earth science",
-                "atmosphere"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "KEVIN BOWMAN",
                 "hasEmail": "mailto:kevin.w.bowman@jpl.nasa.gov"
             },
+            "creator": "Kevin W. Bowman",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C2756348390-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "The TROPESS CrIS L2 Peroxyacetyl Nitrate for Reanalysis Stream, Summary Product contains the vertical distribution of the retrieved atmospheric state of peroxyacetyl nitrate (PAN), and formal uncertainties measured by the CrIS instruments on the Suomi-NPP satellite through May 21, 2021 and from then on the JPSS-1 (NOAA-20) satellite. The reanalysis stream summary product is global for the time period from 2015-12-01 to 2022-12-31. The NASA TRopospheric Ozone and Precursors from Earth System Sounding (TROPESS) project, uses an optimal estimation algorithm, known as the MUlti-SpEctra, MUlti-SpEcies, Multi-SEnsors (MUSES).\n\nThe data files are written in the netCDF version 4 file format, and each file contains one day of data. The data have a spatial resolution of 14 km (CrIS nadir FOV), and are reported at 16 vertical levels from the surface to 0.1 hPa. The principal investigator for the TROPESS project is Kevin W. Bowman.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "TRPSYL2PANCRSRS",
-            "creator": "Kevin W. Bowman",
-            "graphic-preview-description": "TROPESS CrIS PAN (Reanalysis Stream, Summary Product) at 383 hPa on 01 April 2021.",
-            "title": "TROPESS CrIS-SNPP L2 Peroxyacetyl Nitrate for Reanalysis Stream, Summary Product V1 (TRPSYL2PANCRSRS) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TROPESS/images/TRPSYL2PANCRSRS_Sample.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FVU8MI4QOA4NI",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FVU8MI4QOA4NI",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
```

