# Change History for nasa.json (Part 44)

### Changes from 31606f9 to dd2190f (Part 33/162)
**Author:** Automated

**Date:** 2025-02-01 15:02:16+00:00

**Message:** Updated data: Sat Feb  1 15:02:16 UTC 2025

```diff
-            "language": [
-                "en-US"
-            ]
+            "title": "MISR Level 1A Calibration Data V002"
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
+                    "downloadURL": "http://www.nasa.gov/externalflash/double_edged_sword/index.html",
+                    "mediaType": "application/html"
+                }
             ],
+            "identifier": "NASA-867__3",
+            "issued": "2018-06-25",
             "keyword": [
                 "training",
                 "appel",
@@ -335480,152 +335489,154 @@
                 "project",
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
-            "identifier": "NASA-867__3",
-            "description": "Case studies illustrate the kinds of decisions and dilemmas managers face every day, and as such provide an effective learning tool for project management. Due to the dynamic and complex environment of projects, a great deal of project management knowledge is tacit and hard to formalize. A case study captures the complex nature of a project and identifies key decision points, allowing the reader an inside look at the project from a practitioner\u2019s point of view.",
-            "title": "Academy of Program/Project & Engineering Leadership: Interactive Case Studies",
-            "programCode": [
-                "026:045"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.nasa.gov/externalflash/double_edged_sword/index.html",
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
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-C-MCDIDS-3-RDR-MCDNLD-V1.0",
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
-                "comet",
-                "support archives"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "The McDonald Observatory Faint Comet Survey data set presents spectral data from 152 observations of 17 comets taken using the Intensified Dissector Scanner spectrograph.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-c-mcdids-3-rdr-mcdnld-v1.0_7zg7-q7qa",
+            "issued": "2018-06-26",
+            "keyword": [
+                "comet",
+                "support archives"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-C-MCDIDS-3-RDR-MCDNLD-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-c-mcdids-3-rdr-mcdnld-v1.0_7zg7-q7qa",
-            "description": "The McDonald Observatory Faint Comet Survey data set presents spectral data from 152 observations of 17 comets taken using the Intensified Dissector Scanner spectrograph.",
-            "title": "MCDONALD OBSERVATORY FAINT COMET SPECTRO-PHOTOMETRIC SURVEY",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "MCDONALD OBSERVATORY FAINT COMET SPECTRO-PHOTOMETRIC SURVEY"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-EXT1-1347-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the ROSETTA EXTENSION 1 phase 2016-01-01 to 2016-04-05. It is a Global Gravity measurement at the comet 67P and covers the time 2016-01-16T23:29:50.000 to 2016-01-17T01:47:55.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-ext1-1347-v1.0_7zi3-2nge",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-EXT1-1347-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-ext1-1347-v1.0_7zi3-2nge",
-            "description": "This is a Rosetta Radio Science data set, collected during the ROSETTA EXTENSION 1 phase 2016-01-01 to 2016-04-05. It is a Global Gravity measurement at the comet 67P and covers the time 2016-01-16T23:29:50.000 to 2016-01-17T01:47:55.000.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     ROSETTA EXTENSION 1 1347 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     ROSETTA EXTENSION 1 1347 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=LRO-L-DLRE-5-GDR-V1.0",
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
-                "lunar reconnaissance orbiter",
-                "moon"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This data set consists of the Diviner Lunar Radiometer Experiment Gridded Data Records also known as GDRs.   The DLRE is a surface pushbroom mapper that  measures emitted thermal radiation and reflected solar radiation  from the surface of the moon. Two Diviner solar channels measure 0.3-3 micrometers reflected solar radiation.  Three Diviner channels near 8 micrometers classify regolith mineralogy by mapping the location of the Christiansen feature.  The remaining four Diviner channels measure surface temperature in four spectral bands ranging from 12.5 micrometers to beyond 200 micrometers.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.lro-l-dlre-5-gdr-v1.0_7zke-mtqh",
+            "issued": "2018-06-26",
+            "keyword": [
+                "lunar reconnaissance orbiter",
+                "moon"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=LRO-L-DLRE-5-GDR-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.lro-l-dlre-5-gdr-v1.0_7zke-mtqh",
-            "description": "This data set consists of the Diviner Lunar Radiometer Experiment Gridded Data Records also known as GDRs.   The DLRE is a surface pushbroom mapper that  measures emitted thermal radiation and reflected solar radiation  from the surface of the moon. Two Diviner solar channels measure 0.3-3 micrometers reflected solar radiation.  Three Diviner channels near 8 micrometers classify regolith mineralogy by mapping the location of the Christiansen feature.  The remaining four Diviner channels measure surface temperature in four spectral bands ranging from 12.5 micrometers to beyond 200 micrometers.",
-            "title": "LRO DLRE 5 GRIDDED DATA RECORDS",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "LRO DLRE 5 GRIDDED DATA RECORDS"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.nasa.gov/d/7zku-mjcn",
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
+                    "downloadURL": "https://eosweb.larc.nasa.gov/project/calipso/cal_lid_l2_vfm-valstage1-v3-01_table",
+                    "mediaType": "text/html"
+                }
+            ],
+            "identifier": "NASA-0000180",
             "issued": "2018-06-25",
-            "temporal": "2006-06-13/2011-10-11",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
             "keyword": [
                 "climate",
                 "cloud",
@@ -335635,42 +335646,45 @@
                 "satellite",
                 "eos"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "John M. Kusterer",
-                "hasEmail": "mailto:john.m.kusterer@nasa.gov"
-            },
+            "landingPage": "https://data.nasa.gov/d/7zku-mjcn",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:004"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "NASA-0000180",
-            "description": "Cloud-Aerosol Lidar and Infrared Pathfinder Satellite Observations (CALIPSO) was launched on April 28, 2006 to study the impact of clouds and aerosols on the Earth\u2019s radiation budget and climate. It flies in formation with five other satellites in the international \u201cA-Train\u201d (PDF) constellation for coincident Earth observations. The CALIPSO satellite comprises three instruments, the Cloud-Aerosol LIdar with Orthogonal Polarization (CALIOP), the Imaging Infrared Radiometer (IIR), and the Wide Field Camera (WFC). CALIPSO is a joint satellite mission between NASA and the French Agency, CNES. These data consist 5 km aerosol layer data.",
-            "title": "CALIPSO Lidar L2 Vertical Feature Mask Data V3-01",
-            "programCode": [
-                "026:004"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://eosweb.larc.nasa.gov/project/calipso/cal_lid_l2_vfm-valstage1-v3-01_table",
-                    "mediaType": "text/html"
-                }
-            ],
-            "accrualPeriodicity": "irregular",
+            "temporal": "2006-06-13/2011-10-11",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "CALIPSO Lidar L2 Vertical Feature Mask Data V3-01"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.nasa.gov/d/7znk-heru",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "GeneLab Outreach",
+                "hasEmail": "mailto:genelab-outreach@lists.nasa.gov"
+            },
+            "description": "Microbes interact with humans in complex ways and understanding how they respond to the spaceflight environment is important to the success of future manned spaceflight missions. The BRIC-23 mission was designed to measure the response of Bacillus subtilis and Staphylococcus aureus to the spaceflight environment. This experiment aimed to produce high quality omics data from B. subtilis and S. aureus grown aboard the International Space Station (ISS) to allow comparison to matched ground controls. There were two primary objectives for this experiment: (1) Demonstrate all post-flight processes and operations required for successful completion of GeneLab Reference Missions conducted on ISS and (2) Generate high quality GeneLab Reference Mission omics data sets for two prokaryotic model organisms Bacillus subtilis and Staphylococcus aureus. Freezing Control Experiment: The BRIC hardware has significant thermal inertia thus the freezing rate of samples placed at -80 C is quite slow. This could affect RNA-sequencing proteomic and metabolic data sets. In an effort to understand how slow freezing could affect these data sets a control experiment was designed in which B. subtilis and S. aureus were grown in petri plates and either slow frozen to -80 C at a rate matching the BRIC-23 spaceflight samples or processed immediately to harvest RNA and protein.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "GeneLab Study Page",
+                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-138",
+                    "mediaType": "text/html",
+                    "title": "BRIC-23 GeneLab Process Verification Test: Bacillus subtilis transcriptomic proteomic and metabolomic data"
+                }
+            ],
+            "identifier": "nasa_genelab_GLDS-138_7znk-heru",
             "issued": "2018-09-05",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
             "keyword": [
                 "microgravity",
                 "sequence analysis data transformation",
@@ -335694,84 +335708,79 @@
                 "extraction",
                 "data transformation"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "GeneLab Outreach",
-                "hasEmail": "mailto:genelab-outreach@lists.nasa.gov"
-            },
+            "landingPage": "https://data.nasa.gov/d/7znk-heru",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "nasa_genelab_GLDS-138_7znk-heru",
-            "description": "Microbes interact with humans in complex ways and understanding how they respond to the spaceflight environment is important to the success of future manned spaceflight missions. The BRIC-23 mission was designed to measure the response of Bacillus subtilis and Staphylococcus aureus to the spaceflight environment. This experiment aimed to produce high quality omics data from B. subtilis and S. aureus grown aboard the International Space Station (ISS) to allow comparison to matched ground controls. There were two primary objectives for this experiment: (1) Demonstrate all post-flight processes and operations required for successful completion of GeneLab Reference Missions conducted on ISS and (2) Generate high quality GeneLab Reference Mission omics data sets for two prokaryotic model organisms Bacillus subtilis and Staphylococcus aureus. Freezing Control Experiment: The BRIC hardware has significant thermal inertia thus the freezing rate of samples placed at -80 C is quite slow. This could affect RNA-sequencing proteomic and metabolic data sets. In an effort to understand how slow freezing could affect these data sets a control experiment was designed in which B. subtilis and S. aureus were grown in petri plates and either slow frozen to -80 C at a rate matching the BRIC-23 spaceflight samples or processed immediately to harvest RNA and protein.",
-            "title": "BRIC-23 GeneLab Process Verification Test: Bacillus subtilis transcriptomic proteomic and metabolomic data",
-            "programCode": [
-                "026:005"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-138",
-                    "description": "GeneLab Study Page",
-                    "@type": "dcat:Distribution",
-                    "title": "BRIC-23 GeneLab Process Verification Test: Bacillus subtilis transcriptomic proteomic and metabolomic data"
-                }
-            ],
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "BRIC-23 GeneLab Process Verification Test: Bacillus subtilis transcriptomic proteomic and metabolomic data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewBundle.jsp?identifier=urn%3Anasa%3Apds%3Aody_accel&version=1.0",
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
-                "mars odyssey",
-                "mars"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This version of the ODYA bundle was created by the PDS Atmospheres node in 2015",
+            "identifier": "urn:nasa:pds:ody_accel",
+            "issued": "2021-05-21",
+            "keyword": [
+                "mars odyssey",
+                "mars"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewBundle.jsp?identifier=urn%3Anasa%3Apds%3Aody_accel&version=1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:ody_accel",
-            "description": "This version of the ODYA bundle was created by the PDS Atmospheres node in 2015",
-            "title": "ODYA Bundle",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ODYA Bundle"
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
+            "description": "APXS, Atmospheric Opacity, HAZCAM, NAVCAM, MI, PANCAM, RAT, Rover Motion Counter, SPICE",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://pds.jpl.nasa.gov/tools/subscription_service/SS-20140306.shtml",
+                    "mediaType": "application/html"
+                }
             ],
+            "identifier": "NASA-454",
+            "issued": "2018-06-25",
             "keyword": [
                 "rover motion counter",
                 "mi",
@@ -335784,107 +335793,79 @@
                 "pancam",
                 "navcam"
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
-            "identifier": "NASA-454",
-            "description": "APXS, Atmospheric Opacity, HAZCAM, NAVCAM, MI, PANCAM, RAT, Rover Motion Counter, SPICE",
-            "title": "PDS Mars Exploration Rovers Data Release 39",
-            "programCode": [
-                "026:005"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://pds.jpl.nasa.gov/tools/subscription_service/SS-20140306.shtml",
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
+            "title": "PDS Mars Exploration Rovers Data Release 39"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=CO-S-RSS-1-SROC2-V1.0",
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
+            "description": "The Cassini Radio Science Saturn and Ring Occultation Experiment (SROC2) Raw Data Archive is a time-ordered collection of radio science raw data acquired on July 15, August 2, August 20, and September 5, 2005 during the Tour subphase of the Cassini mission.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.co-s-rss-1-sroc2-v1.0_7zs6-js9t",
+            "issued": "2021-05-21",
+            "keyword": [
+                "saturn",
+                "cassini-huygens"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=CO-S-RSS-1-SROC2-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.co-s-rss-1-sroc2-v1.0_7zs6-js9t",
-            "description": "The Cassini Radio Science Saturn and Ring Occultation Experiment (SROC2) Raw Data Archive is a time-ordered collection of radio science raw data acquired on July 15, August 2, August 20, and September 5, 2005 during the Tour subphase of the Cassini mission.",
-            "title": "CASSINI RSS RAW DATA SET - SROC2 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "CASSINI RSS RAW DATA SET - SROC2 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C2404809434-CDDIS.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, CDDIS.",
-            "issued": "2002-01-01",
-            "temporal": "2002-01-01T00:00:00Z/2024-12-09T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-12-05",
-            "keyword": [
-                "earth science",
-                "coordinate reference system",
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
-            "identifier": "C2404809434-CDDIS",
             "description": "Terrestrial Reference Frame (TRF) product derived from the analysis of Very Long Baseline Interferometry (VLBI) data. The Terrestrial Reference Frame product includes station positions, velocities, and correlations. A minimum of three years of data are used in each solution. The TRF operational product is available quarterly at International VLBI Service for Geodesy and Astrometry (IVS) Data Centers.",
-            "title": "CDDIS VLBI products Terrestrial Reference Frame",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://cddis.nasa.gov/Data_and_Derived_Products/VLBI/VLBI_product_holdings.html",
-                    "description": "CDDIS VLBI products",
                     "@type": "dcat:Distribution",
+                    "description": "CDDIS VLBI products",
+                    "downloadURL": "https://cddis.nasa.gov/Data_and_Derived_Products/VLBI/VLBI_product_holdings.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
@@ -335900,161 +335881,155 @@
                     "title": "This dataset's landing page"
                 }
             ],
+            "identifier": "C2404809434-CDDIS",
+            "issued": "2002-01-01",
+            "keyword": [
+                "earth science",
+                "coordinate reference system",
+                "solid earth"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C2404809434-CDDIS.html",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2024-12-05",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "CDDIS"
+            },
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2002-01-01T00:00:00Z/2024-12-09T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "CDDIS VLBI products Terrestrial Reference Frame"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/VIIRS/VJ202GDC_NRT.002",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "VCST Team. 2024-01-22. VIIRS/JPSS2 Moderate-Resolution Dual Gain Bands Calibrated Radiance 6-Min L1B Swath 750m NRT. Version 2. MODAPS at NASA/GSFC. Archived by National Aeronautics and Space Administration, U.S. Government, LANCEMODIS. https://doi.org/10.5067/VIIRS/VJ202GDC_NRT.002. https://doi.org/10.5067/VIIRS/VJ202GDC.002.",
-            "issued": "2024-01-10",
-            "temporal": "2024-01-17T00:00:00Z/2025-01-13T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-07",
-            "keyword": [
-                "spectral/engineering",
-                "earth science",
-                "infrared wavelengths",
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
-            "identifier": "C2837615495-LANCEMODIS",
-            "description": "The Near Real Time (NRT) VIIRS/JPSS2 Moderate-Resolution Dual Gain Bands Calibrated Radiance 6-Min L1B Swath 750m product (VJ202GDC_NRT) contains unaggregated, calibrated TOA radiances for those VIIRS sub-pixel samples that are aggregated along-scan during post-calibration ground processing.  In other words, this file contains the calibrated M1 \u2013 M5, M7 and M13 dual gain band data from the nadir and near-nadir zones that would otherwise be discarded following post-calibration aggregation/Earth View Radiometric Calibration Unit.\r\n\r\nThe Level-1 and Level-2 swath products are generated from the processing of 6 minutes of VIIRS data acquired during theJPSS-2/NOAA-21 satellite overpass. The VIIRS sensor has 5 high-resolution imagery channels (I-bands) that have 32 detectors (32 rows of pixels per scan), with twice the resolution of the M-bands and the DNB, that span the wavelengths from 0.640 &#181;m to 11.45 &#181;m. There are also 7 dual-gain VIIRS bands. The dual gain moderate resolution bands (M1 to M5, M7 and M13) have 6304 samples and the other moderate resolution bands have 3200.\r\n\r\nFor additional information, see the Operational Algorithm Description (OAD) Document for the L1B product at http://npp.gsfc.nasa.gov/sciencedocs/2015-08/474-00090_OAD-VIIRS-CAL-GEO-SDR_H.pdf. The document describes how VIIRS operates in space and provides the equations implemented by the L1B software to generate the MODIS Level-1 intermediate products. It is a summary document that presents the formulae and error budges used to transform VIIRS digital counts to radiance and reflectance.",
-            "release-place": "MODAPS at NASA/GSFC",
             "creator": "VCST Team",
-            "title": "VIIRS/JPSS2 Moderate-Resolution Dual Gain Bands Calibrated Radiance 6-Min L1B Swath 750m NRT",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The Near Real Time (NRT) VIIRS/JPSS2 Moderate-Resolution Dual Gain Bands Calibrated Radiance 6-Min L1B Swath 750m product (VJ202GDC_NRT) contains unaggregated, calibrated TOA radiances for those VIIRS sub-pixel samples that are aggregated along-scan during post-calibration ground processing.  In other words, this file contains the calibrated M1 \u2013 M5, M7 and M13 dual gain band data from the nadir and near-nadir zones that would otherwise be discarded following post-calibration aggregation/Earth View Radiometric Calibration Unit.\r\n\r\nThe Level-1 and Level-2 swath products are generated from the processing of 6 minutes of VIIRS data acquired during theJPSS-2/NOAA-21 satellite overpass. The VIIRS sensor has 5 high-resolution imagery channels (I-bands) that have 32 detectors (32 rows of pixels per scan), with twice the resolution of the M-bands and the DNB, that span the wavelengths from 0.640 &#181;m to 11.45 &#181;m. There are also 7 dual-gain VIIRS bands. The dual gain moderate resolution bands (M1 to M5, M7 and M13) have 6304 samples and the other moderate resolution bands have 3200.\r\n\r\nFor additional information, see the Operational Algorithm Description (OAD) Document for the L1B product at http://npp.gsfc.nasa.gov/sciencedocs/2015-08/474-00090_OAD-VIIRS-CAL-GEO-SDR_H.pdf. The document describes how VIIRS operates in space and provides the equations implemented by the L1B software to generate the MODIS Level-1 intermediate products. It is a summary document that presents the formulae and error budges used to transform VIIRS digital counts to radiance and reflectance.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FVIIRS%2FVJ202GDC_NRT.002",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FVIIRS%2FVJ202GDC_NRT.002",
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
+            "identifier": "C2837615495-LANCEMODIS",
+            "issued": "2024-01-10",
+            "keyword": [
+                "spectral/engineering",
+                "earth science",
+                "infrared wavelengths",
+                "visible wavelengths"
+            ],
+            "landingPage": "https://doi.org/10.5067/VIIRS/VJ202GDC_NRT.002",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2025-01-07",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Not provided"
+            },
+            "release-place": "MODAPS at NASA/GSFC",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2024-01-17T00:00:00Z/2025-01-13T00:00:00Z",
             "theme": [
                 "NOAA - SPACE WEATHER PROGRAM",
                 "LANCE",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "VIIRS/JPSS2 Moderate-Resolution Dual Gain Bands Calibrated Radiance 6-Min L1B Swath 750m NRT"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewBundle.jsp?identifier=urn%3Anasa%3Apds%3Aast-lightcurve-database&version=3.0",
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
-                "none"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "The asteroid lightcurve database (LCDB) is one of the more widely-used research tools\nfor those doing research that compares and contrasts physical characteristics of\nasteroid spin axis rates, sizes, pole orientations, and/or taxonomic class - among\nothers. The v3.0 release includes lightcurve photometry results for more than 24500\ntargets. Each object has one to several dozen detail records that contain results\nobtained by scanning the literature.",
+            "identifier": "urn:nasa:pds:ast-lightcurve-database",
+            "issued": "2021-05-21",
+            "keyword": [
+                "none"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewBundle.jsp?identifier=urn%3Anasa%3Apds%3Aast-lightcurve-database&version=3.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:ast-lightcurve-database",
-            "description": "The asteroid lightcurve database (LCDB) is one of the more widely-used research tools\nfor those doing research that compares and contrasts physical characteristics of\nasteroid spin axis rates, sizes, pole orientations, and/or taxonomic class - among\nothers. The v3.0 release includes lightcurve photometry results for more than 24500\ntargets. Each object has one to several dozen detail records that contain results\nobtained by scanning the literature.",
-            "title": "Asteroid Lightcurve Database (LCDB) V3.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "Asteroid Lightcurve Database (LCDB) V3.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/RZAQB50RV3BS",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Jianxiong Sheng & Daniel Jacob. 2016-06-26. CMS_CH4_FLX_MX. Version 1. Methane (CH4) Flux for Mexican Oil/Gas Systems L4 V1. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/RZAQB50RV3BS. https://disc.gsfc.nasa.gov/datacollection/CMS_CH4_FLX_MX_1.html.",
-            "issued": "2010-01-01",
-            "temporal": "2010-01-01T00:00:00Z/2011-01-01T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2011-01-01",
-            "references": [
-                "https://doi.org/10.1016/j.atmosenv.2017.02.036"
-            ],
-            "keyword": [
-                "earth science",
-                "atmosphere",
-                "atmospheric chemistry"
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
-            "identifier": "C1405716390-GES_DISC",
-            "description": "This data set (CMS_CH4_FLX_MX) contains the yearly average methane (CH4) flux for Mexico's oil and gas systems based on a bottom up calculation of oil/gas emissions reported by the Mexican Petrolium Institute in 2010.  A related data set (CMS_CH4_FLX_CA) contains the yearly average methane (CH4) flux for Canada's oil and gas systems based on a bottom up calculation of oil/gas emissions reported by ICF International in 2013.  The Mexican emissions are concentrated along the east coast (oil production) and the Canadian emissions are concentrated in Alberta (gas production and processing).  More details about the observations, algorithm, and scientific findings are described in Sheng et al. 2017.\n\nThe NASA Carbon Monitoring System (CMS) is designed to make significant contributions in characterizing, quantifying, understanding, and predicting the evolution of global carbon sources and sinks through improved monitoring of carbon stocks and fluxes. The System will use the full range of NASA satellite observations and modeling/analysis capabilities to establish the accuracy, quantitative uncertainties, and utility of products for supporting national and international policy, regulatory, and management activities. CMS will maintain a global emphasis while providing finer scale regional information, utilizing space-based and surface-based data and will rapidly initiate generation and distribution of products both for user evaluation and to inform near-term policy development and planning.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "CMS_CH4_FLX_MX",
             "creator": "Jianxiong Sheng & Daniel Jacob",
-            "title": "Methane (CH4) Flux for Mexican Oil/Gas Systems L4 V1 (CMS_CH4_FLX_MX) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/CMS/CMS_CH4_FLX_MX.png",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "This data set (CMS_CH4_FLX_MX) contains the yearly average methane (CH4) flux for Mexico's oil and gas systems based on a bottom up calculation of oil/gas emissions reported by the Mexican Petrolium Institute in 2010.  A related data set (CMS_CH4_FLX_CA) contains the yearly average methane (CH4) flux for Canada's oil and gas systems based on a bottom up calculation of oil/gas emissions reported by ICF International in 2013.  The Mexican emissions are concentrated along the east coast (oil production) and the Canadian emissions are concentrated in Alberta (gas production and processing).  More details about the observations, algorithm, and scientific findings are described in Sheng et al. 2017.\n\nThe NASA Carbon Monitoring System (CMS) is designed to make significant contributions in characterizing, quantifying, understanding, and predicting the evolution of global carbon sources and sinks through improved monitoring of carbon stocks and fluxes. The System will use the full range of NASA satellite observations and modeling/analysis capabilities to establish the accuracy, quantitative uncertainties, and utility of products for supporting national and international policy, regulatory, and management activities. CMS will maintain a global emphasis while providing finer scale regional information, utilizing space-based and surface-based data and will rapidly initiate generation and distribution of products both for user evaluation and to inform near-term policy development and planning.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FRZAQB50RV3BS",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FRZAQB50RV3BS",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
@@ -336064,484 +336039,523 @@
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/CMS_CH4_FLX_MX_1.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/CMS_CH4_FLX_MX_1.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://acdisc.gsfc.nasa.gov/data/CMS/CMS_CH4_FLX_MX.1/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://acdisc.gsfc.nasa.gov/data/CMS/CMS_CH4_FLX_MX.1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://acdisc.gsfc.nasa.gov/opendap/CMS/CMS_CH4_FLX_MX.1/",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://acdisc.gsfc.nasa.gov/opendap/CMS/CMS_CH4_FLX_MX.1/",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://acdisc.gsfc.nasa.gov/data/CMS/CMS_CH4_FLX_MX.1/doc/README.CMS_CH4_FLX_CAMX_V1.pdf",
-                    "description": "README Document",
                     "@type": "dcat:Distribution",
+                    "description": "README Document",
+                    "downloadURL": "https://acdisc.gsfc.nasa.gov/data/CMS/CMS_CH4_FLX_MX.1/doc/README.CMS_CH4_FLX_CAMX_V1.pdf",
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
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=CMS_CH4_FLX_MX",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=CMS_CH4_FLX_MX",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 }
             ],
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/CMS/CMS_CH4_FLX_MX.png",
+            "identifier": "C1405716390-GES_DISC",
+            "issued": "2010-01-01",
+            "keyword": [
+                "earth science",
+                "atmosphere",
+                "atmospheric chemistry"
+            ],
+            "landingPage": "https://doi.org/10.5067/RZAQB50RV3BS",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2011-01-01",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
+            },
+            "references": [
+                "https://doi.org/10.1016/j.atmosenv.2017.02.036"
+            ],
+            "release-place": "Greenbelt, MD, USA",
+            "series-name": "CMS_CH4_FLX_MX",
             "spatial": "-119.05 13.05 -84.95 33.95",
+            "temporal": "2010-01-01T00:00:00Z/2011-01-01T23:59:59.999Z",
             "theme": [
                 "CMS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Methane (CH4) Flux for Mexican Oil/Gas Systems L4 V1 (CMS_CH4_FLX_MX) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/DHESIUQ7O4YG",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "IceBridge GPS L1B Time-Tagged Real-Time Position and Attitude Solution, Version 1. Version 1. Archived by National Aeronautics and Space Administration, U.S. Government, NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/DHESIUQ7O4YG.",
-            "issued": "2010-11-18",
-            "temporal": "2010-11-18T00:00:00Z/2012-12-29T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2012-12-29",
-            "keyword": [
-                "platform characteristics",
-                "earth science",
-                "spectral/engineering"
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
-            "identifier": "C1386246600-NSIDCV0",
             "description": "This data set contains elevation, roll, pitch, and heading measurements over Antarctica using the Ashtech GG24 GPS+ receiver and the Systron and Donner MMQ-50 Inertial Measurement Unit (IMU). The data were collected by scientists working on the Investigating the Cryospheric Evolution of the Central Antarctic Plate (ICECAP) project, which is funded by the National Science Foundation (NSF) and the Natural Environment Research Council (NERC), with additional support from NASA Operation IceBridge.",
-            "title": "IceBridge GPS L1B Time-Tagged Real-Time Position and Attitude Solution, Version 1",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FDHESIUQ7O4YG",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FDHESIUQ7O4YG",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/ICEBRIDGE/IPUTN1B_UTIGrtGPStimeTag_v01/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/ICEBRIDGE/IPUTN1B_UTIGrtGPStimeTag_v01/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/DHESIUQ7O4YG",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/DHESIUQ7O4YG",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/DHESIUQ7O4YG",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/DHESIUQ7O4YG",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C1386246600-NSIDCV0",
+            "issued": "2010-11-18",
+            "keyword": [
+                "platform characteristics",
+                "earth science",
+                "spectral/engineering"
+            ],
+            "landingPage": "https://doi.org/10.5067/DHESIUQ7O4YG",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2012-12-29",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA NSIDC DAAC"
+            },
             "spatial": "-180.0 -90.0 180.0 -53.0",
+            "temporal": "2010-11-18T00:00:00Z/2012-12-29T23:59:59.999Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "IceBridge GPS L1B Time-Tagged Real-Time Position and Attitude Solution, Version 1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/J2K5LZWPH0F3",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "CLPX-Model: Rapid Update Cycle 40km (RUC-40) Model Output Reduced Data, Version 1. Version 1. Archived by National Aeronautics and Space Administration, U.S. Government, NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/J2K5LZWPH0F3.",
-            "issued": "2002-10-01",
-            "temporal": "2002-10-01T00:00:00Z/2003-06-30T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2003-06-30",
-            "keyword": [
-                "cryosphere",
-                "altitude",
-                "atmosphere",
-                "atmospheric pressure",
-                "atmospheric radiation",
-                "atmospheric temperature",
-                "atmospheric water vapor",
-                "atmospheric winds",
-                "clouds",
-                "earth science",
-                "land surface",
-                "precipitation",
-                "snow/ice",
-                "soils",
-                "surface water",
-                "terrestrial hydrosphere"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Kristi Arsenault",
                 "hasEmail": "mailto:kristi@hsb.gsfc.nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA NSIDC DAAC"
-            },
-            "identifier": "C1386250242-NSIDCV0",
             "description": "The Rapid Update Cycle, version 2 at 40km (RUC-2, known to the Cold Land Processes community as RUC40) model is a Mesoscale Analysis and Prediction System (MAPS) data set that uses the Model Output Reduced Data Set (MORDS) version. This data set has been subsetted for use in the Cold Land Processes Field Experiment (CLPX).",
-            "title": "CLPX-Model: Rapid Update Cycle 40km (RUC-40) Model Output Reduced Data, Version 1",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FJ2K5LZWPH0F3",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FJ2K5LZWPH0F3",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/CLP/data/model/nsidc0211_ruc40/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/CLP/data/model/nsidc0211_ruc40/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/J2K5LZWPH0F3",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/J2K5LZWPH0F3",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/J2K5LZWPH0F3",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/J2K5LZWPH0F3",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C1386250242-NSIDCV0",
+            "issued": "2002-10-01",
+            "keyword": [
+                "cryosphere",
+                "altitude",
+                "atmosphere",
+                "atmospheric pressure",
+                "atmospheric radiation",
+                "atmospheric temperature",
+                "atmospheric water vapor",
+                "atmospheric winds",
+                "clouds",
+                "earth science",
+                "land surface",
+                "precipitation",
+                "snow/ice",
+                "soils",
+                "surface water",
+                "terrestrial hydrosphere"
+            ],
+            "landingPage": "https://doi.org/10.5067/J2K5LZWPH0F3",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2003-06-30",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA NSIDC DAAC"
+            },
             "spatial": "-108.615 38.394 -103.971 42.568",
+            "temporal": "2002-10-01T00:00:00Z/2003-06-30T23:59:59.999Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "CLPX-Model: Rapid Update Cycle 40km (RUC-40) Model Output Reduced Data, Version 1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/VIIRS/VNP10.001",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "VIIRS/NPP Snow Cover 6-Min L2 Swath 375m V001. Version 1. Archived by National Aeronautics and Space Administration, U.S. Government, NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/VIIRS/VNP10.001.",
-            "issued": "2012-01-19",
-            "temporal": "2012-01-19T00:00:00Z/2024-06-24T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-06-17",
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
-            "identifier": "C1365767075-NSIDC_ECS",
             "description": "This data set reports the location of snow cover using radiance data acquired by the Visible Infrared Imager Radiometer Suite (VIIRS) on board the Suomi National Polar-orbiting Partnership (NPP) satellite. Snow cover is identified using the Normalized Difference Snow Index (NDSI) and a series of quality control screens.",
-            "title": "VIIRS/NPP Snow Cover 6-Min L2 Swath 375m V001",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FVIIRS%2FVNP10.001",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FVIIRS%2FVNP10.001",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/VIIRS/VNP10.001",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/VIIRS/VNP10.001",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=VNP10+V001",
-                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=VNP10+V001",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/data/data-access-tool/VNP10/versions/1/",
-                    "description": "Search and filter data files using a map-based interface",
                     "@type": "dcat:Distribution",
+                    "description": "Search and filter data files using a map-based interface",
+                    "downloadURL": "https://nsidc.org/data/data-access-tool/VNP10/versions/1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/VIIRS/VNP10.001",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/VIIRS/VNP10.001",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/VIIRS/VNP10.001",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/VIIRS/VNP10.001",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C1365767075-NSIDC_ECS",
+            "issued": "2012-01-19",
+            "keyword": [
+                "cryosphere",
+                "earth science",
+                "snow/ice"
+            ],
+            "landingPage": "https://doi.org/10.5067/VIIRS/VNP10.001",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2024-06-17",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA NSIDC DAAC"
+            },
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2012-01-19T00:00:00Z/2024-06-24T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "VIIRS/NPP Snow Cover 6-Min L2 Swath 375m V001"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-A-OSINAC-4-AST1-STEINS-STR-REFL-V1.0",
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
-                "2867 steins"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This CODMAC level 4 data set contains solar stray light corrected, radiometric calibrated and geometric distortion corrected (resampled) image data in in reflectance units  (normalized and thus without unit),  acquired by the OSIRIS Narrow Angle Camera on the Rosetta spacecraft  during the STEINS FLY-BY mission phase, covering the period  from 2008-08-04T00:00:00.000 to 2008-10-05T23:59:59.000. The prime target is asteroid 2867 Steins. This version V1.0 is the first version of this dataset.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-a-osinac-4-ast1-steins-str-refl-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "2867 steins"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-A-OSINAC-4-AST1-STEINS-STR-REFL-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-a-osinac-4-ast1-steins-str-refl-v1.0",
-            "description": "This CODMAC level 4 data set contains solar stray light corrected, radiometric calibrated and geometric distortion corrected (resampled) image data in in reflectance units  (normalized and thus without unit),  acquired by the OSIRIS Narrow Angle Camera on the Rosetta spacecraft  during the STEINS FLY-BY mission phase, covering the period  from 2008-08-04T00:00:00.000 to 2008-10-05T23:59:59.000. The prime target is asteroid 2867 Steins. This version V1.0 is the first version of this dataset.",
-            "title": "ROSETTA-ORBITER STEINS OSINAC 4 AST1 RDR-STR-REFL V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER STEINS OSINAC 4 AST1 RDR-STR-REFL V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC3-0960-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 3 phase 2015-07-01 to 2015-10-21. It is a Global Gravity measurement at the comet 67P and covers the time 2015-08-14T03:04:05.000 to 2015-08-14T09:55:57.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc3-0960-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC3-0960-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc3-0960-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 3 phase 2015-07-01 to 2015-10-21. It is a Global Gravity measurement at the comet 67P and covers the time 2015-08-14T03:04:05.000 to 2015-08-14T09:55:57.000.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 3 0960 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 3 0960 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1616",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Brown, D.R.N. 2019. ABoVE: Riverbank Erosion and Vegetation Changes, Yukon River Basin, Alaska, 1984-2017. ORNL DAAC, Oak Ridge, Tennessee, USA. https://doi.org/10.3334/ORNLDAAC/1616",
-            "issued": "2019-01-18",
-            "temporal": "1984-01-01T00:00:00Z/2017-12-31T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-06-12",
-            "keyword": [
-                "biosphere",
-                "vegetation",
-                "land surface",
-                "landscape",
-                "erosion/sedimentation",
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
-            "identifier": "C2162145546-ORNL_CLOUD",
             "description": "This dataset provides a time series of riverbank erosion and vegetation colonization along reaches of the Yukon River (3 study areas), Tanana and Nenana Rivers (1 area), and Chandalar River (1 area) in interior Alaska over the period 1984-2017. The change data were derived from selected 30-m images from Landsat TM, Landsat ETM+, and Landsat Operational Land Imager (OLI) surface reflectance products. Image classification used the Normalized Differenced Vegetation Index (NDVI) with an NDVI threshold of 0.2 to differentiate vegetated from non-vegetated pixels. Images were assigned to one of seven or eight multiyear intervals, within the 1984-2017 overall range, for each study area. Time intervals vary by study site. Change detection identified shifts from one time interval to the next: changes from vegetated to non-vegetated classes were considered riverbank erosion and changes from non-vegetated to vegetated classes were considered vegetation colonization.",
-            "graphic-preview-description": "Riverbank erosion and vegetation colonization at the Yukon River 1 study area, located along the Middle Yukon River between Circle and Fort Yukon, Alaska, for multi-year intervals spanning the years 1985-2017.",
-            "title": "ABoVE: Riverbank Erosion and Vegetation Changes, Yukon River Basin, Alaska, 1984-2017",
-            "graphic-preview-file": "https://daac.ornl.gov/ABOVE/guides/Erosion_Vegetation_Yukon_Fig1.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1616",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1616",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/above/Erosion_Vegetation_Yukon/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/above/Erosion_Vegetation_Yukon/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/ABOVE/guides/Erosion_Vegetation_Yukon.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/ABOVE/guides/Erosion_Vegetation_Yukon.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1616",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1616",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/Erosion_Vegetation_Yukon/comp/Erosion_Vegetation_Yukon.pdf",
-                    "description": "ABoVE: Erosion and Vegetation Along the Yukon River and Tributaries: 1984-2017: Erosion_Vegetation_Yukon.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "ABoVE: Erosion and Vegetation Along the Yukon River and Tributaries: 1984-2017: Erosion_Vegetation_Yukon.pdf",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/Erosion_Vegetation_Yukon/comp/Erosion_Vegetation_Yukon.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/Erosion_Vegetation_Yukon/comp/LandsatImagery_DatesSatellitesSensors.csv",
-                    "description": "ABoVE: Erosion and Vegetation Along the Yukon River and Tributaries: 1984-2017: LandsatImagery_DatesSatellitesSensors.csv",
                     "@type": "dcat:Distribution",
+                    "description": "ABoVE: Erosion and Vegetation Along the Yukon River and Tributaries: 1984-2017: LandsatImagery_DatesSatellitesSensors.csv",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/Erosion_Vegetation_Yukon/comp/LandsatImagery_DatesSatellitesSensors.csv",
+                    "mediaType": "text/csv",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://daac.ornl.gov/ABOVE/guides/Erosion_Vegetation_Yukon_Fig1.png",
-                    "description": "Riverbank erosion and vegetation colonization at the Yukon River 1 study area, located along the Middle Yukon River between Circle and Fort Yukon, Alaska, for multi-year intervals spanning the years 1985-2017.",
                     "@type": "dcat:Distribution",
+                    "description": "Riverbank erosion and vegetation colonization at the Yukon River 1 study area, located along the Middle Yukon River between Circle and Fort Yukon, Alaska, for multi-year intervals spanning the years 1985-2017.",
+                    "downloadURL": "https://daac.ornl.gov/ABOVE/guides/Erosion_Vegetation_Yukon_Fig1.png",
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
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://webmap.ornl.gov/wcsdown/dataset.jsp?ds_id=1616",
-                    "description": "Web Coverage Service for this collection.",
                     "@type": "dcat:Distribution",
+                    "description": "Web Coverage Service for this collection.",
+                    "downloadURL": "https://webmap.ornl.gov/wcsdown/dataset.jsp?ds_id=1616",
+                    "mediaType": "text/html",
                     "title": "Use Web Coverage Service (WCS) to download the dataset's data"
                 }
             ],
+            "graphic-preview-description": "Riverbank erosion and vegetation colonization at the Yukon River 1 study area, located along the Middle Yukon River between Circle and Fort Yukon, Alaska, for multi-year intervals spanning the years 1985-2017.",
+            "graphic-preview-file": "https://daac.ornl.gov/ABOVE/guides/Erosion_Vegetation_Yukon_Fig1.png",
+            "identifier": "C2162145546-ORNL_CLOUD",
+            "issued": "2019-01-18",
+            "keyword": [
+                "biosphere",
+                "vegetation",
+                "land surface",
+                "landscape",
+                "erosion/sedimentation",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1616",
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
             "spatial": "-161.46 61.91 -143.3 68.15",
+            "temporal": "1984-01-01T00:00:00Z/2017-12-31T23:59:59Z",
             "theme": [
                 "ABoVE",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "ABoVE: Riverbank Erosion and Vegetation Changes, Yukon River Basin, Alaska, 1984-2017"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.nasa.gov/d/8289-nz53",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "GeneLab Outreach",
+                "hasEmail": "mailto:genelab-outreach@lists.nasa.gov"
+            },
+            "description": "Mitochondrial DNA-depleted human skin fibroblasts (HSF rho0) with suppressed oxidative phosphorylation were characterized by significant changes in the expression of 2100 nuclear genes encoding numerous protein classes in NF-kappaB and STAT3 signaling pathways and by decreased activity of the mitochondrial death pathway compared to the parent rho+ HSF. In contrast the extrinsic TRAIL/TRAIL-Receptor-mediated death pathway remained highly active and exogenous TRAIL induced higher levels of apoptosis in rho0 cells compared to rho+ HSF. Global gene expression analysis using microarray and quantitative RT-PCR demonstrated that expression levels of many growth factors and their adaptor proteins (FGF13 HGF IGFBP4 IGFBP6 IGFL2) cytokines (IL6 IL17B IL18 IL19 IL28B) and cytokine receptors (IL1R1 IL21R IL31RA) were substantially decreased after mitochondrial depletion. Some of these genes were targets of NF-kappaB and STAT3 and their protein products could regulate the STAT3 signaling pathway. Alpha-irradiation induced expression of several NF-kappaB/STAT3 target genes including IL1A IL1B IL6 PTGS2/COX2 and MMP12 in rho+ HSF but this response was substantially decreased in rho0 HSF. Suppression of the IKK-NF-kappaB pathway by the small molecular inhibitor BMS-345541 and of the JAK2-STAT3 pathway by AG490 dramatically increased TRAIL-induced apoptosis in the control and irradiated rho+ HSF. Inhibitory antibodies against IL6 the main activator of JAK2-STAT3 pathway added into the cell media also increased TRAIL-induced apoptosis in rho+ HSF. However NF-kappaB activation was partially lost in mitochondrial DNA-depleted HSF resulting in downregulation of the basal or radiation-induced expression of numerous NF-kappaB targets further suppressing IL6-JAK2-STAT3 that in concert with NF-kappaB regulated protection against TRAIL-induced apoptosis. There are 12 total samples 3 biological replicates each of HSF rho+ and rho0 cells that were not irradiated (control=C) or irradiated (alpha=A). Cells were harvested at 4 hours after treatment.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "GeneLab Study Page",
+                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-182",
+                    "mediaType": "text/html",
+                    "title": "Human skin fibroblast mitochondrial depletion 0.5 Gy alpha-particle"
+                }
+            ],
+            "identifier": "nasa_genelab_GLDS-182_8289-nz53",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
             "keyword": [
                 "p-gse24945-5",
                 "p-gse24945-2",
@@ -336563,266 +336577,253 @@
                 "specified_biomaterial_action",
                 "nucleic_acid_extraction"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "GeneLab Outreach",
-                "hasEmail": "mailto:genelab-outreach@lists.nasa.gov"
-            },
+            "landingPage": "https://data.nasa.gov/d/8289-nz53",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "nasa_genelab_GLDS-182_8289-nz53",
-            "description": "Mitochondrial DNA-depleted human skin fibroblasts (HSF rho0) with suppressed oxidative phosphorylation were characterized by significant changes in the expression of 2100 nuclear genes encoding numerous protein classes in NF-kappaB and STAT3 signaling pathways and by decreased activity of the mitochondrial death pathway compared to the parent rho+ HSF. In contrast the extrinsic TRAIL/TRAIL-Receptor-mediated death pathway remained highly active and exogenous TRAIL induced higher levels of apoptosis in rho0 cells compared to rho+ HSF. Global gene expression analysis using microarray and quantitative RT-PCR demonstrated that expression levels of many growth factors and their adaptor proteins (FGF13 HGF IGFBP4 IGFBP6 IGFL2) cytokines (IL6 IL17B IL18 IL19 IL28B) and cytokine receptors (IL1R1 IL21R IL31RA) were substantially decreased after mitochondrial depletion. Some of these genes were targets of NF-kappaB and STAT3 and their protein products could regulate the STAT3 signaling pathway. Alpha-irradiation induced expression of several NF-kappaB/STAT3 target genes including IL1A IL1B IL6 PTGS2/COX2 and MMP12 in rho+ HSF but this response was substantially decreased in rho0 HSF. Suppression of the IKK-NF-kappaB pathway by the small molecular inhibitor BMS-345541 and of the JAK2-STAT3 pathway by AG490 dramatically increased TRAIL-induced apoptosis in the control and irradiated rho+ HSF. Inhibitory antibodies against IL6 the main activator of JAK2-STAT3 pathway added into the cell media also increased TRAIL-induced apoptosis in rho+ HSF. However NF-kappaB activation was partially lost in mitochondrial DNA-depleted HSF resulting in downregulation of the basal or radiation-induced expression of numerous NF-kappaB targets further suppressing IL6-JAK2-STAT3 that in concert with NF-kappaB regulated protection against TRAIL-induced apoptosis. There are 12 total samples 3 biological replicates each of HSF rho+ and rho0 cells that were not irradiated (control=C) or irradiated (alpha=A). Cells were harvested at 4 hours after treatment.",
-            "title": "Human skin fibroblast mitochondrial depletion 0.5 Gy alpha-particle",
-            "programCode": [
-                "026:005"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-182",
-                    "description": "GeneLab Study Page",
-                    "@type": "dcat:Distribution",
-                    "title": "Human skin fibroblast mitochondrial depletion 0.5 Gy alpha-particle"
-                }
-            ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "Human skin fibroblast mitochondrial depletion 0.5 Gy alpha-particle"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ECOSTRESS/ECO_L2_LSTE.002",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Simon Hook, Glynn Hulley. 2022-11-14. ECOSTRESS Swath Land Surface Temperature and Emissivity Instantaneous L2 Global 70 m v002. Version Version 2. Sioux Falls, South Dakota, USA. Archived by National Aeronautics and Space Administration, U.S. Government, NASA EOSDIS Land Processes Distributed Active Archive Center. https://doi.org/10.5067/ECOSTRESS/ECO_L2_LSTE.002. https://doi.org/10.5067/ECOSTRESS/ECO_L2_LSTE.002. The DOI landing page provides citations in APA and Chicago styles..",
-            "issued": "2022-11-14",
-            "temporal": "2018-07-09T00:00:00Z/2024-12-23T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-12-19",
-            "keyword": [
-                "earth science",
-                "surface thermal properties",
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
-            "identifier": "C2076114664-LPCLOUD",
-            "description": "The ECOsystem Spaceborne Thermal Radiometer Experiment on Space Station (ECOSTRESS) mission measures the temperature of plants to better understand how much water plants need and how they respond to stress. ECOSTRESS is attached to the International Space Station (ISS) and collects data globally between 52\u00b0 N and 52\u00b0 S latitudes. A map of the acquisition coverage can be found in figure 2 on the ECOSTRESS website(https://ecostress.jpl.nasa.gov/science).\nThe ECOSTRESS Swath Land Surface Temperature and Emissivity Instantaneous L2 Global 70 m (ECO_L2_LSTE) Version 2 data product provides atmospherically corrected land surface temperature and emissivity (LST&E) values derived from five thermal infrared (TIR) bands. The ECO_L2_LSTE data product was derived using a physics-based Temperature and Emissivity Separation (TES) algorithm. The ECO_L2_LSTE is provided as swath data and has a spatial resolution of 70 meters (m). The corresponding ECO_L1B_GEO (https://doi.org/10.5067/ECOSTRESS/ECO_L1B_GEO.002) data product is required to georeference the ECO_L2_LSTE data product.\nThe ECO_L2_LSTE Version 2 data product contains layers of LST, emissivity for bands 1 through 5, quality control for LST&E, LST error, emissivity error for bands 1 through 5, wideband emissivity, Precipitable Water Vapor (PWV), cloud mask, and water mask.\n\nImprovements/Changes from Previous Versions\n\n-\tAddition of cloud mask and water mask layers.\n\n-\tAddition of ECOSTRESS Gridded Land Surface Temperature and Emissivity Instantaneous L2 Global 70 m v002 (ECO_L2G_LSTE.002 (https://doi.org/10.5067/ECOSTRESS/ECO_L2G_LSTE.002)) and ECOSTRESS Tiled Land Surface Temperature and Emissivity Instantaneous L2 Global 70 m v002 (ECO_L2T_LSTE.002 (https://doi.org/10.5067/ECOSTRESS/ECO_L2T_LSTE.002)) data products.\n\nKnown Issues\n\n-\tData acquisition gap: ECOSTRESS was launched on June 29, 2018, and moved to autonomous science operations on August 20, 2018, following a successful in-orbit checkout period. On September 29, 2018, ECOSTRESS experienced an anomaly with its primary mass storage unit (MSU). ECOSTRESS has a primary and secondary MSU (A and B). On December 5, 2018, the instrument was switched to the secondary MSU and science operations resumed. On March 14, 2019, the secondary MSU experienced a similar anomaly, temporarily halting science acquisitions. On May 15, 2019, a new data acquisition approach was implemented, and science acquisitions resumed. To optimize the new acquisition approach TIR bands 2, 4, and 5 are being downloaded. The data products are as previously, except the bands not downloaded contain fill values (L1 radiance and L2 emissivity). This approach was implemented from May 15, 2019, through April 28, 2023.\n\n-\tData acquisition gap: From February 8 to February 16, 2020, an ECOSTRESS instrument issue resulted in a data anomaly that created striping in band 4 (10.5 micron). These data products have been reprocessed and are available for download. No ECOSTRESS data were acquired on February 17, 2020, due to the instrument being in SAFEHOLD. Data acquired following the anomaly have not been affected.\n\n-\tData acquisition: ECOSTRESS has now successfully returned to 5-band mode after being in 3-band mode since 2019. This feature was successfully enabled following a Data Processing Unit firmware update (version 4.1) to the payload on April 28, 2023. To better balance contiguous science data scene variables, 3-band collection is currently being interleaved with 5-band acquisitions over the orbital day/night periods.\n\n-\tData alert: All users of ECOSTRESS L2 v002 products (ECO_L2T_LSTE, ECO_L2_LSTE, ECO_L2G_LSTE) should be aware that the cloud mask information previously available in the Quality Control (QC) layer in v001, is not available in the v002 QC layer. Instead, users should be using the \u2018cloud_mask\u2019 layer in the L2 LSTE product, or the cloud information in the standard cloud mask products (ECO_L2_CLOUD, ECO_L2T_CLOUD, ECO_L2G_CLOUD) to assess if a pixel is cle",
-            "release-place": "Sioux Falls, South Dakota, USA",
             "creator": "Simon Hook, Glynn Hulley",
-            "title": "ECOSTRESS Swath Land Surface Temperature and Emissivity Instantaneous L2 Global 70 m V002",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The ECOsystem Spaceborne Thermal Radiometer Experiment on Space Station (ECOSTRESS) mission measures the temperature of plants to better understand how much water plants need and how they respond to stress. ECOSTRESS is attached to the International Space Station (ISS) and collects data globally between 52\u00b0 N and 52\u00b0 S latitudes. A map of the acquisition coverage can be found in figure 2 on the ECOSTRESS website(https://ecostress.jpl.nasa.gov/science).\nThe ECOSTRESS Swath Land Surface Temperature and Emissivity Instantaneous L2 Global 70 m (ECO_L2_LSTE) Version 2 data product provides atmospherically corrected land surface temperature and emissivity (LST&E) values derived from five thermal infrared (TIR) bands. The ECO_L2_LSTE data product was derived using a physics-based Temperature and Emissivity Separation (TES) algorithm. The ECO_L2_LSTE is provided as swath data and has a spatial resolution of 70 meters (m). The corresponding ECO_L1B_GEO (https://doi.org/10.5067/ECOSTRESS/ECO_L1B_GEO.002) data product is required to georeference the ECO_L2_LSTE data product.\nThe ECO_L2_LSTE Version 2 data product contains layers of LST, emissivity for bands 1 through 5, quality control for LST&E, LST error, emissivity error for bands 1 through 5, wideband emissivity, Precipitable Water Vapor (PWV), cloud mask, and water mask.\n\nImprovements/Changes from Previous Versions\n\n-\tAddition of cloud mask and water mask layers.\n\n-\tAddition of ECOSTRESS Gridded Land Surface Temperature and Emissivity Instantaneous L2 Global 70 m v002 (ECO_L2G_LSTE.002 (https://doi.org/10.5067/ECOSTRESS/ECO_L2G_LSTE.002)) and ECOSTRESS Tiled Land Surface Temperature and Emissivity Instantaneous L2 Global 70 m v002 (ECO_L2T_LSTE.002 (https://doi.org/10.5067/ECOSTRESS/ECO_L2T_LSTE.002)) data products.\n\nKnown Issues\n\n-\tData acquisition gap: ECOSTRESS was launched on June 29, 2018, and moved to autonomous science operations on August 20, 2018, following a successful in-orbit checkout period. On September 29, 2018, ECOSTRESS experienced an anomaly with its primary mass storage unit (MSU). ECOSTRESS has a primary and secondary MSU (A and B). On December 5, 2018, the instrument was switched to the secondary MSU and science operations resumed. On March 14, 2019, the secondary MSU experienced a similar anomaly, temporarily halting science acquisitions. On May 15, 2019, a new data acquisition approach was implemented, and science acquisitions resumed. To optimize the new acquisition approach TIR bands 2, 4, and 5 are being downloaded. The data products are as previously, except the bands not downloaded contain fill values (L1 radiance and L2 emissivity). This approach was implemented from May 15, 2019, through April 28, 2023.\n\n-\tData acquisition gap: From February 8 to February 16, 2020, an ECOSTRESS instrument issue resulted in a data anomaly that created striping in band 4 (10.5 micron). These data products have been reprocessed and are available for download. No ECOSTRESS data were acquired on February 17, 2020, due to the instrument being in SAFEHOLD. Data acquired following the anomaly have not been affected.\n\n-\tData acquisition: ECOSTRESS has now successfully returned to 5-band mode after being in 3-band mode since 2019. This feature was successfully enabled following a Data Processing Unit firmware update (version 4.1) to the payload on April 28, 2023. To better balance contiguous science data scene variables, 3-band collection is currently being interleaved with 5-band acquisitions over the orbital day/night periods.\n\n-\tData alert: All users of ECOSTRESS L2 v002 products (ECO_L2T_LSTE, ECO_L2_LSTE, ECO_L2G_LSTE) should be aware that the cloud mask information previously available in the Quality Control (QC) layer in v001, is not available in the v002 QC layer. Instead, users should be using the \u2018cloud_mask\u2019 layer in the L2 LSTE product, or the cloud information in the standard cloud mask products (ECO_L2_CLOUD, ECO_L2T_CLOUD, ECO_L2G_CLOUD) to assess if a pixel is cle",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FECOSTRESS%2FECO_L2_LSTE.002",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FECOSTRESS%2FECO_L2_LSTE.002",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "application/x-hdf5",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=C2076114664-LPCLOUD",
-                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=C2076114664-LPCLOUD",
+                    "mediaType": "application/x-hdf5",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/ECOSTRESS/ECO_L2_LSTE.002",
-                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
+                    "downloadURL": "https://doi.org/10.5067/ECOSTRESS/ECO_L2_LSTE.002",
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
-                    "downloadURL": "https://lpdaac.usgs.gov/documents/1574/ECOL2_User_Guide_V2.pdf",
-                    "description": "The technical information in the User's Guide enables users to interpret and use the data products.",
                     "@type": "dcat:Distribution",
+                    "description": "The technical information in the User's Guide enables users to interpret and use the data products.",
+                    "downloadURL": "https://lpdaac.usgs.gov/documents/1574/ECOL2_User_Guide_V2.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://lpdaac.usgs.gov/documents/2235/ECO2_LSTE_ATBD_V1.1.pdf",
-                    "description": "The ATBD provides physical theory and mathematical procedures for the calculations used to produce the data products.",
                     "@type": "dcat:Distribution",
+                    "description": "The ATBD provides physical theory and mathematical procedures for the calculations used to produce the data products.",
+                    "downloadURL": "https://lpdaac.usgs.gov/documents/2235/ECO2_LSTE_ATBD_V1.1.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's algorithm theoretical basis document"
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
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://lpdaac.usgs.gov/documents/380/ECO2_PSD_V1.pdf",
-                    "description": "The Product Specification Document (PSD) describes the format and contents of the ECOSTRESS product.",
                     "@type": "dcat:Distribution",
+                    "description": "The Product Specification Document (PSD) describes the format and contents of the ECOSTRESS product.",
+                    "downloadURL": "https://lpdaac.usgs.gov/documents/380/ECO2_PSD_V1.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View information related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://lpdaac.usgs.gov/documents/299/ECO2_ASD_V1.pdf",
-                    "description": "The Radiance Algorithm Specification Document (ASD) describes the computer processing used to generate the ECOSTRESS products.",
                     "@type": "dcat:Distribution",
+                    "description": "The Radiance Algorithm Specification Document (ASD) describes the computer processing used to generate the ECOSTRESS products.",
+                    "downloadURL": "https://lpdaac.usgs.gov/documents/299/ECO2_ASD_V1.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View the documentation for this dataset's algorithms"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://lpdaac.usgs.gov/documents/1573/Quick_Guide_for_Accessing_ECOSTRESS_Swath_Data_in_NASA_Earthdata_Search.pdf",
-                    "description": "The Earthdata Search Quick Guide explains how to search ECOSTRESS data in NASA Earthdata Search.",
                     "@type": "dcat:Distribution",
+                    "description": "The Earthdata Search Quick Guide explains how to search ECOSTRESS data in NASA Earthdata Search.",
+                    "downloadURL": "https://lpdaac.usgs.gov/documents/1573/Quick_Guide_for_Accessing_ECOSTRESS_Swath_Data_in_NASA_Earthdata_Search.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's how-to documentation"
                 }
             ],
+            "identifier": "C2076114664-LPCLOUD",
+            "issued": "2022-11-14",
+            "keyword": [
+                "earth science",
+                "surface thermal properties",
+                "land surface"
+            ],
+            "landingPage": "https://doi.org/10.5067/ECOSTRESS/ECO_L2_LSTE.002",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2024-12-19",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "LP DAAC"
+            },
+            "release-place": "Sioux Falls, South Dakota, USA",
             "spatial": "-180.0 -54.0 180.0 54.0",
+            "temporal": "2018-07-09T00:00:00Z/2024-12-23T00:00:00Z",
             "theme": [
                 "ECOSTRESS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "ECOSTRESS Swath Land Surface Temperature and Emissivity Instantaneous L2 Global 70 m V002"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-X-OSIWAC-4-CR5-CHKOUT-REFLECT-V1.0",
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
-                "4 vesta",
-                "international rosetta mission"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This CODMAC level 4 data set contains radiometric calibrated and geometric distortion corrected (resampled)  image data in reflectance units (normalized and thus without unit),  acquired by the OSIRIS Wide Angle Camera on the Rosetta spacecraft  during the CRUISE 5 mission phase, covering the period  from 2009-12-14T00:00:00.000 to 2010-05-16T23:59:59.000. The prime objective was commissioning / calibration. Several targets of opportunity were observed, but none of them is identifiable as prime target. This version V1.0 is the first version of this dataset.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-x-osiwac-4-cr5-chkout-reflect-v1.0_82ch-t5wn",
+            "issued": "2021-05-21",
+            "keyword": [
+                "4 vesta",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-X-OSIWAC-4-CR5-CHKOUT-REFLECT-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-x-osiwac-4-cr5-chkout-reflect-v1.0_82ch-t5wn",
-            "description": "This CODMAC level 4 data set contains radiometric calibrated and geometric distortion corrected (resampled)  image data in reflectance units (normalized and thus without unit),  acquired by the OSIRIS Wide Angle Camera on the Rosetta spacecraft  during the CRUISE 5 mission phase, covering the period  from 2009-12-14T00:00:00.000 to 2010-05-16T23:59:59.000. The prime objective was commissioning / calibration. Several targets of opportunity were observed, but none of them is identifiable as prime target. This version V1.0 is the first version of this dataset.",
-            "title": "ROSETTA-ORBITER CHECKOUT OSIWAC 4 CR5 RDR-REFLECT V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER CHECKOUT OSIWAC 4 CR5 RDR-REFLECT V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=PHX-M-SSI-5-REACHABILITY-OPS-V1.0",
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
+            "description": "The Surface Stereo Imager (SSI) experiment on the Mars Phoenix Lander consists of one instrument component plus command electronics. This SSI Imaging Operations RDR data set contains reachability data from the Surface Stereo Imager (SSI).",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.phx-m-ssi-5-reachability-ops-v1.0_82da-ck52",
+            "issued": "2018-06-26",
+            "keyword": [
+                "phoenix",
+                "mars"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=PHX-M-SSI-5-REACHABILITY-OPS-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.phx-m-ssi-5-reachability-ops-v1.0_82da-ck52",
-            "description": "The Surface Stereo Imager (SSI) experiment on the Mars Phoenix Lander consists of one instrument component plus command electronics. This SSI Imaging Operations RDR data set contains reachability data from the Surface Stereo Imager (SSI).",
-            "title": "PHOENIX MARS SURFACE STEREO IMAGER 5 REACHABILITY OPS V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "PHOENIX MARS SURFACE STEREO IMAGER 5 REACHABILITY OPS V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1214419355-ASF.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, ASF.",
-            "issued": "2011-07-29",
-            "temporal": "2008-07-24T21:06:27Z/2024-11-11T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-07",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "undefined",
                 "hasEmail": "mailto:uso@asf.alaska.edu"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "ASF"
-            },
-            "identifier": "C1214419355-ASF",
             "description": "UAVSAR PolSAR Scene Stokes",
-            "title": "UAVSAR_POLSAR_STOKES",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.asf.alaska.edu/",
-                    "description": "ASF data search and download interface",
                     "@type": "dcat:Distribution",
+                    "description": "ASF data search and download interface",
+                    "downloadURL": "https://search.asf.alaska.edu/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 }
             ],
+            "identifier": "C1214419355-ASF",
+            "issued": "2011-07-29",
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1214419355-ASF.html",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2024-11-07",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "ASF"
+            },
             "spatial": "<?xml version=\"1.0\" encoding=\"UTF-8\"?><gml:Polygon xmlns:gml=\"http://www.opengis.net/gml/3.2\" srsName=\"EPSG:4326\"><gml:outerBoundaryIs><gml:LinearRing><gml:posList>64.623877 -9.140625 81.898451 -7.734375 83.84881 -34.453125 83.559717 -78.925781 77.915669 -124.804688 64.320872 -150.996094 55.776573 165.585938 45.58329 137.636719 36.456636 127.96875 29.840644 129.023438 18.646245 -159.433594 -47.989922 -76.640625 -47.989922 -64.6875 -37.160317 -52.382812 64.623877 -9.140625</gml:posList></gml:LinearRing></gml:outerBoundaryIs><gml:innerBoundaryIs></gml:innerBoundaryIs></gml:Polygon>",
+            "temporal": "2008-07-24T21:06:27Z/2024-11-11T00:00:00Z",
             "theme": [
                 "Hayward Fault, CA",
                 "Laurentides Reserve, QC, Canada",
@@ -337288,215 +337289,226 @@
                 "Peace River and I17 Corridor, FL",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "UAVSAR_POLSAR_STOKES"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-CAL%2FE-ALICE-2-EAR3-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This data set contains CODMAC level 2 data acquired by the Rosetta Orbiter ALICE UV Spectrometer during the third earth flyby mission phase, which took place between 2009-09-14 and 2009-12-13.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-cal-e-alice-2-ear3-v1.0_82fb-xckz",
             "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "international rosetta mission",
                 "calibration",
                 "moon",
                 "earth"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-CAL%2FE-ALICE-2-EAR3-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-cal-e-alice-2-ear3-v1.0_82fb-xckz",
-            "description": "This data set contains CODMAC level 2 data acquired by the Rosetta Orbiter ALICE UV Spectrometer during the third earth flyby mission phase, which took place between 2009-09-14 and 2009-12-13.",
-            "title": "ROSETTA-ORBITER CAL/EARTH ALICE 2 EAR3 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "ROSETTA-ORBITER CAL/EARTH ALICE 2 EAR3 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1625796322-LARC.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "MISR Science Team (2006), Terra/MISR Level 2, TOA/Cloud Stereo Product subset for the GoMACCS region, version 2, Hampton, VA, USA: NASA Atmospheric Science Data Center (ASDC), Accessed <author citing data inserts date here> at doi: TBD",
-            "issued": "2019-07-22",
-            "temporal": "2006-07-30T16:35:07Z/2006-10-16T17:15:34.106Z",
-            "@type": "dcat:Dataset",
-            "modified": "2019-07-22",
-            "keyword": [
-                "atmosphere",
-                "earth science",
-                "clouds"
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
-            "identifier": "C1625796322-LARC",
             "description": "Multi-angle Imaging SpectroRadiometer (MISR) is an instrument designed to view Earth with cameras pointed in 9 different directions. As the instrument flies overhead, each piece of Earth's surface below is successively imaged by all 9 cameras, in each of 4 wavelengths (blue, green, red, and near-infrared). The goal of MISR is to improve our understanding of the fate of sunlight in Earth environment, as well as distinguish different types of clouds, particles and surfaces. Specifically, MISR monitors the monthly, seasonal, and long-term trends in three areas: 1) amount and type of atmospheric particles (aerosols), including those formed by natural sources and by human activities; 2) amounts, types, and heights of clouds, and 3) distribution of land surface cover, including vegetation canopy structure. MISR Level 2 TOA/Cloud Stereo Product subset for the GoMACCS region V002 contains the Stereoscopically Derived Cloud Mask (SDCM), cloud winds, Reflecting Level Reference Altitude (RLRA), with associated data.",
-            "title": "MISR Level 2 TOA/Cloud Stereo Product subset for the GoMACCS region V002",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/search/concepts/C1625796322-LARC.html",
-                    "description": "View this dataset on the CMR (Common Metadata Repository)",
                     "@type": "dcat:Distribution",
+                    "description": "View this dataset on the CMR (Common Metadata Repository)",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/search/concepts/C1625796322-LARC.html",
+                    "mediaType": "text/html",
                     "title": "CMR"
                 }
             ],
+            "identifier": "C1625796322-LARC",
+            "issued": "2019-07-22",
+            "keyword": [
+                "atmosphere",
+                "earth science",
+                "clouds"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1625796322-LARC.html",
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
+            "temporal": "2006-07-30T16:35:07Z/2006-10-16T17:15:34.106Z",
             "theme": [
                 "GOMACCS_2006",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "MISR Level 2 TOA/Cloud Stereo Product subset for the GoMACCS region V002"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC3-0881-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 3 phase 2015-07-01 to 2015-10-21. It is a Global Gravity measurement at the comet 67P and covers the time 2015-07-08T09:47:40.000 to 2015-07-08T17:45:08.500.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc3-0881-v1.0_82gh-4xsj",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC3-0881-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc3-0881-v1.0_82gh-4xsj",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 3 phase 2015-07-01 to 2015-10-21. It is a Global Gravity measurement at the comet 67P and covers the time 2015-07-08T09:47:40.000 to 2015-07-08T17:45:08.500.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 3 0881 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 3 0881 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NEAR-A-SPICE-6-CRUISE1-V1.0",
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
+            "description": "This data set includes the complete set of SPICE data for one NEAR mission phase in the form of SPICE kernels, which can be accessed using SPICE software available to read these files.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.near-a-spice-6-cruise1-v1.0_82im-gpq8",
+            "issued": "2018-06-26",
+            "keyword": [
+                "eros",
+                "near earth asteroid rendezvous"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NEAR-A-SPICE-6-CRUISE1-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.near-a-spice-6-cruise1-v1.0_82im-gpq8",
-            "description": "This data set includes the complete set of SPICE data for one NEAR mission phase in the form of SPICE kernels, which can be accessed using SPICE software available to read these files.",
-            "title": "NEAR SPICE KERNELS CRUISE1",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "NEAR SPICE KERNELS CRUISE1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=PHX-M-SSI-5-NORMAL-OPS-V1.0",
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
+            "description": "The Surface Stereo Imager (SSI) experiment on the Mars Phoenix Lander consists of one instrument component plus command electronics. This SSI Imaging Operations RDR data set contains normal data from the Surface Stereo Imager (SSI).",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.phx-m-ssi-5-normal-ops-v1.0_82jt-tmb2",
+            "issued": "2018-06-26",
+            "keyword": [
+                "mars",
+                "phoenix"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=PHX-M-SSI-5-NORMAL-OPS-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.phx-m-ssi-5-normal-ops-v1.0_82jt-tmb2",
-            "description": "The Surface Stereo Imager (SSI) experiment on the Mars Phoenix Lander consists of one instrument component plus command electronics. This SSI Imaging Operations RDR data set contains normal data from the Surface Stereo Imager (SSI).",
-            "title": "PHOENIX MARS SURFACE STEREO IMAGER 5 NORMAL OPS V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "PHOENIX MARS SURFACE STEREO IMAGER 5 NORMAL OPS V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://planetarynames.wr.usgs.gov/Page/Images",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Michael Kelly",
+                "hasEmail": "mailto:Michael.S.Kelley@nasa.gov"
+            },
+            "description": "These images display several of Saturn's moons approved by the International Astronomical Union (IAU).",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://planetarynames.wr.usgs.gov/images/janusmap.pdf",
+                    "mediaType": "application/pdf"
+                }
+            ],
+            "identifier": "OCIO-Fitara-184",
             "issued": "1979-12-31",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
             "keyword": [
                 "dione",
                 "enceladus",
@@ -337516,991 +337528,991 @@
                 "saturn",
                 "rhea"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Michael Kelly",
-                "hasEmail": "mailto:Michael.S.Kelley@nasa.gov"
-            },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "International Astronomical Union (IAU) Working Group for Planetary System Nomenclature (WGPSN)"
-            },
-            "identifier": "OCIO-Fitara-184",
-            "description": "These images display several of Saturn's moons approved by the International Astronomical Union (IAU).",
-            "title": "Gazetteer of Planetary Nomenclature: Saturnian System: Janus",
-            "programCode": [
-                "026:007"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://planetarynames.wr.usgs.gov/images/janusmap.pdf",
-                    "mediaType": "application/pdf"
-                }
+            "landingPage": "http://planetarynames.wr.usgs.gov/Page/Images",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:007"
             ],
-            "accrualPeriodicity": "irregular",
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "International Astronomical Union (IAU) Working Group for Planetary System Nomenclature (WGPSN)"
+            },
             "theme": [
                 "Space Science"
-            ]
+            ],
+            "title": "Gazetteer of Planetary Nomenclature: Saturnian System: Janus"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-PRL-0234-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the PRELANDING phase 2014-01-21 to 2014-11-18. It is a Global Gravity measurement at the comet 67P and covers the time 2014-08-23T13:06:05.000 to 2014-08-23T18:14:48.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-prl-0234-v1.0_82ma-dnhk",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-PRL-0234-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-prl-0234-v1.0_82ma-dnhk",
-            "description": "This is a Rosetta Radio Science data set, collected during the PRELANDING phase 2014-01-21 to 2014-11-18. It is a Global Gravity measurement at the comet 67P and covers the time 2014-08-23T13:06:05.000 to 2014-08-23T18:14:48.000.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     PRELANDING 0234 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     PRELANDING 0234 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.7927/0gdn-6y33",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Center for International Earth Science Information Network - CIESIN - Columbia University. 2021-02-24. Global Subnational Infant Mortality Rates, Version 2.01. Version 2.01. Palisades, NY. Archived by National Aeronautics and Space Administration, U.S. Government, NASA Socioeconomic Data and Applications Center (SEDAC). https://doi.org/10.7927/0gdn-6y33. https://doi.org/10.7927/0gdn-6y33.",
-            "issued": "2021-02-24",
-            "temporal": "2015-01-01T00:00:00Z/2015-12-31T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2021-02-24",
-            "references": [
-                "https://doi.org/10.7927/H4PZ56R2",
-                "https://doi.org/10.7927/g739-5620"
-            ],
-            "keyword": [
-                "human dimensions",
-                "population",
-                "earth science"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "undefined",
                 "hasEmail": "mailto:ciesin.info@ciesin.columbia.edu"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "SEDAC"
-            },
-            "identifier": "C2013463595-SEDAC",
-            "description": "The Global Subnational Infant Mortality Rates, Version 2.01 consist of Infant Mortality Rate (IMR) estimates for 234 countries and territories, 143 of which include subnational Units. The data are benchmarked to the year 2015 (Version 1 was benchmarked to the year 2000), and are drawn from national offices, Demographic and Health Surveys (DHS), Multiple Indicator Cluster Surveys (MICS), and other sources from 2006 to 2014. In addition to Infant Mortality Rates, Version 2.01 includes crude estimates of births and infant deaths, which could be aggregated or disaggregated to different geographies to calculate infant mortality rates at different scales or resolutions, where births are the rate denominator and infant deaths are the rate numerator. Boundary inputs are derived primarily from the Gridded Population of the World, Version 4 (GPWv4) data collection. National and subnational data are mapped to grid cells at a spatial resolution of 30 arc-seconds (~1 km) (Version 1 has a spatial resolution of 1/4 degree, ~28 km at the equator), allowing for easy integration with demographic, environmental, and other spatial data.",
-            "release-place": "Palisades, NY",
-            "graphic-preview-description": "Maps Download Page",
             "creator": "Center for International Earth Science Information Network - CIESIN - Columbia University",
-            "title": "Global Subnational Infant Mortality Rates, Version 2.01",
-            "graphic-preview-file": "https://sedac.ciesin.columbia.edu/data/set/povmap-global-subnational-infant-mortality-rates-v2-01/maps",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The Global Subnational Infant Mortality Rates, Version 2.01 consist of Infant Mortality Rate (IMR) estimates for 234 countries and territories, 143 of which include subnational Units. The data are benchmarked to the year 2015 (Version 1 was benchmarked to the year 2000), and are drawn from national offices, Demographic and Health Surveys (DHS), Multiple Indicator Cluster Surveys (MICS), and other sources from 2006 to 2014. In addition to Infant Mortality Rates, Version 2.01 includes crude estimates of births and infant deaths, which could be aggregated or disaggregated to different geographies to calculate infant mortality rates at different scales or resolutions, where births are the rate denominator and infant deaths are the rate numerator. Boundary inputs are derived primarily from the Gridded Population of the World, Version 4 (GPWv4) data collection. National and subnational data are mapped to grid cells at a spatial resolution of 30 arc-seconds (~1 km) (Version 1 has a spatial resolution of 1/4 degree, ~28 km at the equator), allowing for easy integration with demographic, environmental, and other spatial data.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.7927%2F0gdn-6y33",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.7927%2F0gdn-6y33",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/downloads/maps/povmap/povmap-global-subnational-infant-mortality-rates-v2-01/povmap-global-subnational-infant-mortality-rates-v2-01-2015-thumbnail.jpg",
-                    "description": "Sample browse graphic of the data set.",
                     "@type": "dcat:Distribution",
+                    "description": "Sample browse graphic of the data set.",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/downloads/maps/povmap/povmap-global-subnational-infant-mortality-rates-v2-01/povmap-global-subnational-infant-mortality-rates-v2-01-2015-thumbnail.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/povmap-global-subnational-infant-mortality-rates-v2-01/data-download",
-                    "description": "Data Download Page",
                     "@type": "dcat:Distribution",
+                    "description": "Data Download Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/povmap-global-subnational-infant-mortality-rates-v2-01/data-download",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/povmap-global-subnational-infant-mortality-rates-v2-01/maps",
-                    "description": "Maps Download Page",
                     "@type": "dcat:Distribution",
+                    "description": "Maps Download Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/povmap-global-subnational-infant-mortality-rates-v2-01/maps",
+                    "mediaType": "text/html",
                     "title": "Get a related map visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://sedac.ciesin.columbia.edu/data/set/povmap-global-subnational-infant-mortality-rates-v2-01/docs",
-                    "description": "Documentation Page",
                     "@type": "dcat:Distribution",
+                    "description": "Documentation Page",
+                    "downloadURL": "http://sedac.ciesin.columbia.edu/data/set/povmap-global-subnational-infant-mortality-rates-v2-01/docs",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/povmap-global-subnational-infant-mortality-rates-v2-01",
-                    "description": "Data Set\u00a0Overview Page",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set\u00a0Overview Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/povmap-global-subnational-infant-mortality-rates-v2-01",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "graphic-preview-description": "Maps Download Page",
+            "graphic-preview-file": "https://sedac.ciesin.columbia.edu/data/set/povmap-global-subnational-infant-mortality-rates-v2-01/maps",
+            "identifier": "C2013463595-SEDAC",
+            "issued": "2021-02-24",
+            "keyword": [
+                "human dimensions",
+                "population",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.7927/0gdn-6y33",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2021-02-24",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "SEDAC"
+            },
+            "references": [
+                "https://doi.org/10.7927/H4PZ56R2",
+                "https://doi.org/10.7927/g739-5620"
+            ],
+            "release-place": "Palisades, NY",
             "spatial": "-180.0 -90.0 180.0 85.0",
+            "temporal": "2015-01-01T00:00:00Z/2015-12-31T00:00:00Z",
             "theme": [
                 "PMP",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Global Subnational Infant Mortality Rates, Version 2.01"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=PHX-M-SSI-5-ANAGLYPH-OPS-V1.0",
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
+            "description": "The Surface Stereo Imager (SSI)  experiment on the Mars Phoenix Lander consists of one instrument  component plus command electronics. This SSI Imaging Operations RDR  data set contains anaglyph data from the Surface Stereo Imager (SSI).",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.phx-m-ssi-5-anaglyph-ops-v1.0_82nv-4mdb",
+            "issued": "2021-05-21",
+            "keyword": [
+                "mars",
+                "phoenix"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=PHX-M-SSI-5-ANAGLYPH-OPS-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.phx-m-ssi-5-anaglyph-ops-v1.0_82nv-4mdb",
-            "description": "The Surface Stereo Imager (SSI)  experiment on the Mars Phoenix Lander consists of one instrument  component plus command electronics. This SSI Imaging Operations RDR  data set contains anaglyph data from the Surface Stereo Imager (SSI).",
-            "title": "PHOENIX MARS SURFACE STEREO IMAGER \n                                      5 ANAGLYPH OPS V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "PHOENIX MARS SURFACE STEREO IMAGER \n                                      5 ANAGLYPH OPS V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-4-ESC2-67P-M15-INF-REFL-V1.0",
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
+            "description": "This CODMAC level 4 data set contains solar stray-light corrected, in-field stray-light corrected,  radiometric calibrated and geometric distortion corrected  (resampled) image data in reflectance units (normalized  and thus without unit),  acquired by the OSIRIS Narrow Angle Camera on the Rosetta spacecraft  during the COMET ESCORT 2 mission phase, covering the period  from 2015-04-08T11:25:00.000 to 2015-05-05T23:24:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V1.0 is the first version of this dataset: Lien corrected dataset after September 2019 PSA/PDS external peer review.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-4-esc2-67p-m15-inf-refl-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-4-ESC2-67P-M15-INF-REFL-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-4-esc2-67p-m15-inf-refl-v1.0",
-            "description": "This CODMAC level 4 data set contains solar stray-light corrected, in-field stray-light corrected,  radiometric calibrated and geometric distortion corrected  (resampled) image data in reflectance units (normalized  and thus without unit),  acquired by the OSIRIS Narrow Angle Camera on the Rosetta spacecraft  during the COMET ESCORT 2 mission phase, covering the period  from 2015-04-08T11:25:00.000 to 2015-05-05T23:24:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V1.0 is the first version of this dataset: Lien corrected dataset after September 2019 PSA/PDS external peer review.",
-            "title": "ROSETTA-ORBITER 67P OSINAC 4 ESC2-MTP015 RDR-INF-REFL V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P OSINAC 4 ESC2-MTP015 RDR-INF-REFL V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=ULY-J-SCE-4-SUMM-RANGING-10MIN-V1.0",
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
-                "ulysses"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "The Ulysses spacecraft was occulted by the Io Plasma Torus (IPT) during its Jupiter encounter on 8 February 1992. The Ulysses dual-frequency radio subsystem used by the Ulysses Solar Corona Experiment (SCE) was utilized to measure the electron content (column density) of the IPT. In the nominal mode for radio-sounding observations, both downlinks (S-band: f_s = 2.3 GHz X-band: f_x = 8.4 GHz) are phase coherent with the uplink (S-band: f_u = 2.1 GHz). The dual-frequency radio-sounding technique exploits the dispersive nature of ionized media on the propagation of the two downlinks. The tiny Doppler shift due to plasma moving in and out of the ray path is greater at S-band than at the higher frequency X-band.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.uly-j-sce-4-summ-ranging-10min-v1.0_82u4-d9ky",
+            "issued": "2021-05-21",
+            "keyword": [
+                "jupiter",
+                "ulysses"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=ULY-J-SCE-4-SUMM-RANGING-10MIN-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.uly-j-sce-4-summ-ranging-10min-v1.0_82u4-d9ky",
-            "description": "The Ulysses spacecraft was occulted by the Io Plasma Torus (IPT) during its Jupiter encounter on 8 February 1992. The Ulysses dual-frequency radio subsystem used by the Ulysses Solar Corona Experiment (SCE) was utilized to measure the electron content (column density) of the IPT. In the nominal mode for radio-sounding observations, both downlinks (S-band: f_s = 2.3 GHz X-band: f_x = 8.4 GHz) are phase coherent with the uplink (S-band: f_u = 2.1 GHz). The dual-frequency radio-sounding technique exploits the dispersive nature of ionized media on the propagation of the two downlinks. The tiny Doppler shift due to plasma moving in and out of the ray path is greater at S-band than at the higher frequency X-band.",
-            "title": "ULYSSES JUPITER SOLAR CORONA EXPER.\n                                        RANGING DATA 10 MIN AVG",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ULYSSES JUPITER SOLAR CORONA EXPER.\n                                        RANGING DATA 10 MIN AVG"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-PRL-0250-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the PRELANDING phase 2014-01-21 to 2014-11-18. It is a Global Gravity measurement at the comet 67P and covers the time 2014-08-27T23:34:15.000 to 2014-08-28T01:02:29.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-prl-0250-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-PRL-0250-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-prl-0250-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the PRELANDING phase 2014-01-21 to 2014-11-18. It is a Global Gravity measurement at the comet 67P and covers the time 2014-08-27T23:34:15.000 to 2014-08-28T01:02:29.000.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     PRELANDING 0250 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     PRELANDING 0250 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/MAPS_OSTA3_CO5X5_HDF",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "1999-07-19. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/MAPS_OSTA3_CO5X5_HDF.",
-            "issued": "1999-07-07",
-            "temporal": "1984-10-06T00:00:00Z/1984-10-13T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2018-02-06",
-            "keyword": [
-                "air quality",
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
-            "identifier": "C1535917654-LARC_ASDC",
             "description": "MAPS Overview The MAPS experiment measures the global distribution of carbon monoxide (CO) mixing ratios in the free troposphere. Because of MAPS' previous flights on board the Space Shuttle, Earth system scientists now know that carbon monoxide concentrations in the troposphere are highly variable around the planet, and that widespread burning in the South American Amazon Basin and southern cerrados, the African savannahs,and the Australian grasslands and ranches are major sources of carbon monoxide in the southern hemisphere and tropical troposphere.InstrumentThe MAPS instrument is based on a technique called gas filter radiometry. Thermal energy from the Earth passes through the atmosphere and enters the viewport of the downlooking MAPS instrument. Carbon monoxide and nitrous oxide (N2O) in the atmosphere produce unique absorption lines in the transmitted energy. The energy which enters the MAPS instrument is split into &amp; three beams. One beam passes through a cell containing CO and falls onto a detector. This CO gas cell acts as a filter for the effects of CO present in the middle troposphere. A second beam falls directly onto a detector without passing through any gas filter. The difference in the voltage of the signals from these two detectors can be used to determine the amount of CO present in the atmosphere at an altitude of 7-8 km. A third beam of the incident energy passes through a cell containing N2O and falls onto a detector. This N2O gas cell acts as a filter for the effects of N2O present in the atmosphere. The global distribution of N2O is well known, so the N2O signal can be used to detect the presence of clouds in the field of view and to correct the simultaneous CO measurement for systematic errors in the data. The data that are available from MAPS OSTA3 include a 5 by 5 degree gridded box (MAPS_OSTA3_5X5_HDF) and a second by second data product (MAPS_OSTA3_COSEC_HDF). These data sets are available from the Langley DAAC.",
-            "title": "Measurement of Air Pollution from Satellites (MAPS) Office of Space and Terrestrial Applications - 3 (OSTA3) Carbon Monoxide 5 degree by 5 degree data",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMAPS_OSTA3_CO5X5_HDF",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMAPS_OSTA3_CO5X5_HDF",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.nasa.gov/centers/langley/news/factsheets/MAPS.html",
-                    "description": "NASA Langley Factsheet for MAPS",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Langley Factsheet for MAPS",
+                    "downloadURL": "https://www.nasa.gov/centers/langley/news/factsheets/MAPS.html",
+                    "mediaType": "text/html",
                     "title": "View a micro article on this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/MAPS_OSTA3_CO5X5_HDF",
-                    "description": "DOI data set landing page for MAPS_OSTA3_CO5X5_HDF_1",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for MAPS_OSTA3_CO5X5_HDF_1",
+                    "downloadURL": "https://doi.org/10.5067/MAPS_OSTA3_CO5X5_HDF",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1535917654-LARC_ASDC",
-                    "description": "Earthdata Search for MAPS_OSTA3_CO5X5_HDF_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for MAPS_OSTA3_CO5X5_HDF_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1535917654-LARC_ASDC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/maps/guide/base_maps_co5x5_dataset.pdf",
-                    "description": "MAPS 5 degree by 5 degree Langley DAAC Data Set Document",
                     "@type": "dcat:Distribution",
+                    "description": "MAPS 5 degree by 5 degree Langley DAAC Data Set Document",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/maps/guide/base_maps_co5x5_dataset.pdf",
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
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/maps/readme/readme_maps_osta3_co5x5_hdf.txt",
-                    "description": "Readme Information about the MAPS sample read software and data files",
                     "@type": "dcat:Distribution",
+                    "description": "Readme Information about the MAPS sample read software and data files",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/maps/readme/readme_maps_osta3_co5x5_hdf.txt",
+                    "mediaType": "text/html",
                     "title": "View this dataset's read me document"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/maps/read_software/compile_read_maps_co5x5.txt",
-                    "description": "Script that compiles the C code necessary to read the following MAPS HDF data files: 1) MAPS_OSTA3_CO5X5_HDF, 2) MAPS_SRL1_CO5X5_HDF, 3) MAPS_SRL2_CO5X5_HDF",
                     "@type": "dcat:Distribution",
+                    "description": "Script that compiles the C code necessary to read the following MAPS HDF data files: 1) MAPS_OSTA3_CO5X5_HDF, 2) MAPS_SRL1_CO5X5_HDF, 3) MAPS_SRL2_CO5X5_HDF",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/maps/read_software/compile_read_maps_co5x5.txt",
+                    "mediaType": "text/html",
                     "title": "View this dataset's science data product software documentation"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/maps/read_software/maps_co5x5_read.c",
-                    "description": "Sample read program for the following MAPS data sets: MAPS_SRL1_CO5x5_HDF, MAPS_SRL2_CO5x5_HDF, MAPS_OSTA3_CO5x5_HDF - Direct File Download (.c)",
                     "@type": "dcat:Distribution",
+                    "description": "Sample read program for the following MAPS data sets: MAPS_SRL1_CO5x5_HDF, MAPS_SRL2_CO5x5_HDF, MAPS_OSTA3_CO5x5_HDF - Direct File Download (.c)",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/maps/read_software/maps_co5x5_read.c",
+                    "mediaType": "text/html",
                     "title": "View this dataset's science data product software documentation"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/project/MAPS",
-                    "description": "ASDC Data and Information for MAPS",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Data and Information for MAPS",
+                    "downloadURL": "https://asdc.larc.nasa.gov/project/MAPS",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://cdiac.ess-dive.lbl.gov/epubs/db/db1020/db1020.html",
-                    "description": "CDIAC Overview of Measurement of Air Pollution from Satellites (MAPS) 1994 Correlative Atmospheric Carbon Monoxide Mixing Ratios",
                     "@type": "dcat:Distribution",
+                    "description": "CDIAC Overview of Measurement of Air Pollution from Satellites (MAPS) 1994 Correlative Atmospheric Carbon Monoxide Mixing Ratios",
+                    "downloadURL": "https://cdiac.ess-dive.lbl.gov/epubs/db/db1020/db1020.html",
+                    "mediaType": "text/html",
                     "title": "The dataset's home page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/MAPS/MAPS_OSTA3_CO5X5_HDF/",
-                    "description": "ASDC Direct Data Download for MAPS_OSTA3_CO5X5_HDF_1",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for MAPS_OSTA3_CO5X5_HDF_1",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/MAPS/MAPS_OSTA3_CO5X5_HDF/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/MAPS/MAPS_OSTA3_CO5X5_HDF/contents.html",
-                    "description": "OPeNDAP data access for MAPS_OSTA3_CO5X5_HDF_1",
                     "@type": "dcat:Distribution",
+                    "description": "OPeNDAP data access for MAPS_OSTA3_CO5X5_HDF_1",
+                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/MAPS/MAPS_OSTA3_CO5X5_HDF/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 }
             ],
+            "identifier": "C1535917654-LARC_ASDC",
+            "issued": "1999-07-07",
+            "keyword": [
+                "air quality",
+                "atmosphere",
+                "atmospheric chemistry",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/MAPS_OSTA3_CO5X5_HDF",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2018-02-06",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/LARC/SD/ASDC"
+            },
             "spatial": "<?xml version=\"1.0\" encoding=\"UTF-8\"?><gml:Polygon xmlns:gml=\"http://www.opengis.net/gml/3.2\" srsName=\"EPSG:9825\"><gml:outerBoundaryIs><gml:LinearRing><gml:posList>-70.0 -180.0 -70.0 180.0 70.0 180.0 70.0 -180.0 -70.0 -180.0</gml:posList></gml:LinearRing></gml:outerBoundaryIs><gml:innerBoundaryIs></gml:innerBoundaryIs></gml:Polygon>",
+            "temporal": "1984-10-06T00:00:00Z/1984-10-13T23:59:59.999Z",
             "theme": [
                 "MAPS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Measurement of Air Pollution from Satellites (MAPS) Office of Space and Terrestrial Applications - 3 (OSTA3) Carbon Monoxide 5 degree by 5 degree data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=PHX-M-RAC-4-LINEARIZED-OPS-V1.0",
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
+            "description": "The Robotic Arm Camera (RAC)  experiment on the Mars Phoenix Lander consists of one instrument  component plus command electronics. This RAC Imaging Operations RDR  data set contains linearized data from the Robotic Arm Camera (RAC).",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.phx-m-rac-4-linearized-ops-v1.0_834j-qpsz",
+            "issued": "2021-05-21",
+            "keyword": [
+                "phoenix",
+                "mars"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=PHX-M-RAC-4-LINEARIZED-OPS-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.phx-m-rac-4-linearized-ops-v1.0_834j-qpsz",
-            "description": "The Robotic Arm Camera (RAC)  experiment on the Mars Phoenix Lander consists of one instrument  component plus command electronics. This RAC Imaging Operations RDR  data set contains linearized data from the Robotic Arm Camera (RAC).",
-            "title": "PHOENIX MARS ROBOTIC ARM CAMERA \n                                      4 LINEARIZED OPS V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "PHOENIX MARS ROBOTIC ARM CAMERA \n                                      4 LINEARIZED OPS V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://c3.nasa.gov/dashlink/resources/81/",
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
                 "fn": "Abhinav Saxena",
                 "hasEmail": "mailto:abhinav.saxena@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Dashlink"
-            },
-            "identifier": "DASHLINK_81",
             "description": "This is the first version of the performance evaluation tool. Evaluation is based on point estimates of the RUL predictions.\r\n\r\na more detailed documentation will be available with the tool soon.\r\n\r\nin the meantime, please download the attached files/folder in the same root folder to run a demo. To evaluate your own results create results & application data files in .mat format and save in the results folder. please make sure you name your files as xxx_results.mat for results and yyy_appData.mat for application data.",
-            "title": "Prognostics Performance Evaluation",
-            "programCode": [
-                "026:029"
-            ],
             "distribution": [
                 {
-                    "mediaType": "application/zip",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/PE.zip",
-                    "description": "PE.zip",
                     "@type": "dcat:Distribution",
+                    "description": "PE.zip",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/PE.zip",
+                    "mediaType": "application/zip",
                     "title": "PE.zip"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/PerformanceEvaluator1.0.pdf",
-                    "description": "PerformanceEvaluator1.0.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "PerformanceEvaluator1.0.pdf",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/PerformanceEvaluator1.0.pdf",
+                    "mediaType": "application/pdf",
                     "title": "PerformanceEvaluator1.0.pdf"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/PHM-Conference09-Metrics-full-paper.pdf",
-                    "description": "PHM-Conference09-Metrics-full-paper.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "PHM-Conference09-Metrics-full-paper.pdf",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/PHM-Conference09-Metrics-full-paper.pdf",
+                    "mediaType": "application/pdf",
                     "title": "PHM-Conference09-Metrics-full-paper.pdf"
                 },
                 {
-                    "mediaType": "application/octet-stream",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/MCRInstaller.exe",
-                    "description": "MCRInstaller.exe",
                     "@type": "dcat:Distribution",
+                    "description": "MCRInstaller.exe",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/MCRInstaller.exe",
+                    "mediaType": "application/octet-stream",
                     "title": "MCRInstaller.exe"
                 }
             ],
-            "accrualPeriodicity": "irregular"
+            "identifier": "DASHLINK_81",
+            "issued": "2010-09-10",
+            "keyword": [
+                "nasa",
+                "ames",
+                "dashlink"
+            ],
+            "landingPage": "https://c3.nasa.gov/dashlink/resources/81/",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:029"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Dashlink"
+            },
+            "title": "Prognostics Performance Evaluation"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/751",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Landmann, T., and D.P. Roy. 2004. SAFARI 2000 Reflectance of Fire Residue, Kruger National Park, Dry Season 2000. ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/751",
-            "issued": "2023-10-18",
-            "temporal": "2000-08-14T00:00:00Z/2000-08-14T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-10-24",
-            "keyword": [
-                "ecological dynamics",
-                "land surface",
-                "biosphere",
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
-            "identifier": "C2789022996-ORNL_CLOUD",
             "description": "The goal of this study was to understand the change in reflectance caused by the action of fire and the heterogeneity of fire effects (i.e., the fraction of the observation that burned and the combustion completeness of that observation). A spectral mixture model and field and satellite observations were used to compare changes in Landsat reflectance associated with fire and combustion completeness derived from field measurements at prescribed fire sites in South Africa and to substantiate and illustrate the model findings. The data are stored in a single ASCII file in comma-separate-value format (.csv).",
-            "graphic-preview-description": "Browse Image",
-            "title": "SAFARI 2000 Reflectance of Fire Residue, Kruger National Park, Dry Season 2000",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/safari_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F751",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F751",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/safari2k/field_campaign/knp_fire_residue/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/safari2k/field_campaign/knp_fire_residue/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/S2K/guides/knp_fire_residue.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/S2K/guides/knp_fire_residue.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/751",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/751",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/safari2k/field_campaign/knp_fire_residue/comp/knp_fire_residue_readme.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/safari2k/field_campaign/knp_fire_residue/comp/knp_fire_residue_readme.pdf",
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
+            "identifier": "C2789022996-ORNL_CLOUD",
+            "issued": "2023-10-18",
+            "keyword": [
+                "ecological dynamics",
+                "land surface",
+                "biosphere",
+                "surface radiative properties",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/751",
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
             "spatial": "21.83 -25.75 22.33 -24.16",
+            "temporal": "2000-08-14T00:00:00Z/2000-08-14T23:59:59Z",
             "theme": [
                 "SAFARI 2000",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "SAFARI 2000 Reflectance of Fire Residue, Kruger National Park, Dry Season 2000"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NEAR-A-XRS-2-EDR-CRUISE3-V1.0",
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
-                "solar system"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This data set contains X-Ray Spectrometer (XRS) observations made during the third cruise phase of the NEAR mission. The individual observations are combined into a single file per day for each sensor.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.near-a-xrs-2-edr-cruise3-v1.0_838h-xnzv",
+            "issued": "2018-06-26",
+            "keyword": [
+                "near earth asteroid rendezvous",
+                "solar system"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NEAR-A-XRS-2-EDR-CRUISE3-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.near-a-xrs-2-edr-cruise3-v1.0_838h-xnzv",
-            "description": "This data set contains X-Ray Spectrometer (XRS) observations made during the third cruise phase of the NEAR mission. The individual observations are combined into a single file per day for each sensor.",
-            "title": "NEAR XRS SPECTRA FOR CRUISE 3 PHASE",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "NEAR XRS SPECTRA FOR CRUISE 3 PHASE"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.7927/H4CF9N1K",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Millennium Ecosystem Assessment. 2005-05-29. Millennium Ecosystem Assessment: MA Population. Version 1.00. Washington, DC. Archived by National Aeronautics and Space Administration, U.S. Government, Island Press. https://doi.org/10.7927/H4CF9N1K. https://doi.org/10.7927/H4CF9N1K.",
-            "issued": "2005-05-29",
-            "temporal": "1990-01-01T00:00:00Z/2002-12-31T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2005-05-29",
-            "references": [
-                "https://doi.org/10.7927/H47P8WB9",
-                "https://doi.org/10.7927/H4V9860B",
-                "https://doi.org/10.7927/H4QJ7F8M",
-                "https://doi.org/10.7927/H4G44N76",
-                "https://doi.org/10.7927/H4KW5CZ6"
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
-            "identifier": "C1000000441-SEDAC",
-            "description": "The Millennium Ecosystem Assessment: MA Population provides data and information on baseline population as one of the drivers of ecosystem change. The data was used in estimating the magnitude of regional pressures on ecosystems. The MA Population data sets include Gridded Population of the World (GPW) Version 3, population grids from the Alpha version of the Global Rural-Urban Mapping Project (GRUMP), Global Subnational Infant Mortality Rates (Alpha version), and Global Subnational Prevalence of Child Malnutrition (Alpha version).",
-            "release-place": "Washington, DC",
-            "graphic-preview-description": "Sample browse graphic of the data set.",
             "creator": "Millennium Ecosystem Assessment",
-            "title": "Millennium Ecosystem Assessment: MA Population",
-            "graphic-preview-file": "https://sedac.ciesin.columbia.edu/downloads/maps/ma/ma-population/sedac-logo.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The Millennium Ecosystem Assessment: MA Population provides data and information on baseline population as one of the drivers of ecosystem change. The data was used in estimating the magnitude of regional pressures on ecosystems. The MA Population data sets include Gridded Population of the World (GPW) Version 3, population grids from the Alpha version of the Global Rural-Urban Mapping Project (GRUMP), Global Subnational Infant Mortality Rates (Alpha version), and Global Subnational Prevalence of Child Malnutrition (Alpha version).",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.7927%2FH4CF9N1K",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.7927%2FH4CF9N1K",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/downloads/maps/ma/ma-population/sedac-logo.jpg",
-                    "description": "Sample browse graphic of the data set.",
                     "@type": "dcat:Distribution",
+                    "description": "Sample browse graphic of the data set.",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/downloads/maps/ma/ma-population/sedac-logo.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/ma-population/data-download",
-                    "description": "Data Download Page",
                     "@type": "dcat:Distribution",
+                    "description": "Data Download Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/ma-population/data-download",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://sedac.ciesin.columbia.edu/data/set/ma-population/docs",
-                    "description": "Documentation Page",
                     "@type": "dcat:Distribution",
+                    "description": "Documentation Page",
+                    "downloadURL": "http://sedac.ciesin.columbia.edu/data/set/ma-population/docs",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/ma-population",
-                    "description": "Data Set\u00a0Overview Page",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set\u00a0Overview Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/ma-population",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "graphic-preview-description": "Sample browse graphic of the data set.",
+            "graphic-preview-file": "https://sedac.ciesin.columbia.edu/downloads/maps/ma/ma-population/sedac-logo.jpg",
+            "identifier": "C1000000441-SEDAC",
+            "issued": "2005-05-29",
+            "keyword": [
+                "population",
+                "earth science",
+                "human dimensions"
+            ],
+            "landingPage": "https://doi.org/10.7927/H4CF9N1K",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2005-05-29",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "SEDAC"
+            },
+            "references": [
+                "https://doi.org/10.7927/H47P8WB9",
+                "https://doi.org/10.7927/H4V9860B",
+                "https://doi.org/10.7927/H4QJ7F8M",
+                "https://doi.org/10.7927/H4G44N76",
+                "https://doi.org/10.7927/H4KW5CZ6"
+            ],
+            "release-place": "Washington, DC",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "1990-01-01T00:00:00Z/2002-12-31T00:00:00Z",
             "theme": [
                 "MA",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Millennium Ecosystem Assessment: MA Population"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/QB4JHGKXH16O",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "SMAPVEX12 Surface Roughness Data for Agricultural Area V001. Version 1. Archived by National Aeronautics and Space Administration, U.S. Government, NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/QB4JHGKXH16O.",
-            "issued": "2012-06-07",
-            "temporal": "2012-06-07T00:00:00Z/2012-07-19T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2012-07-19",
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
-            "identifier": "C1000000222-NSIDC_ECS",
             "description": "This data set contains surface roughness data collected at several agricultural sites as a part of the Soil Moisture Active Passive Validation Experiment 2012 (SMAPVEX12).",
-            "title": "SMAPVEX12 Surface Roughness Data for Agricultural Area V001",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FQB4JHGKXH16O",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FQB4JHGKXH16O",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/SMAP_VAL/SV12SRA.001/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/SMAP_VAL/SV12SRA.001/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1000000222-NSIDC_ECS&m=42.46875%21-98.525390625%214%211%210%210%2C2&q=SMAPVEX12&ok=SMAPVEX12",
-                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1000000222-NSIDC_ECS&m=42.46875%21-98.525390625%214%211%210%210%2C2&q=SMAPVEX12&ok=SMAPVEX12",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/data/data-access-tool/SV12SRA/versions/1/",
-                    "description": "Data Access link for ITSD project",
                     "@type": "dcat:Distribution",
+                    "description": "Data Access link for ITSD project",
+                    "downloadURL": "https://nsidc.org/data/data-access-tool/SV12SRA/versions/1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/QB4JHGKXH16O",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/QB4JHGKXH16O",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/QB4JHGKXH16O",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/QB4JHGKXH16O",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C1000000222-NSIDC_ECS",
+            "issued": "2012-06-07",
+            "keyword": [
+                "topography",
+                "land surface",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/QB4JHGKXH16O",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2012-07-19",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA NSIDC DAAC"
+            },
             "spatial": "-98.51 49.44 -97.85 49.96",
+            "temporal": "2012-06-07T00:00:00Z/2012-07-19T23:59:59.999Z",
             "theme": [
                 "SMAPVEX12",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "SMAPVEX12 Surface Roughness Data for Agricultural Area V001"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-X-REX-2-LAUNCH-V2.0",
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
-                "new horizons",
-                "calibration"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This data set contains Raw data taken by the New Horizons Radio Science Experiment instrument during the post-launch checkout mission phase.  This is VERSION 2.0 of this data set. The REX datasets over the mission include calibrations using known radio sources, Jupiter, and cold sky measurements; operational readiness tests (ORTs); internal test pattern calibration; and prime science radiometry and occultation observations during the Pluto Encounter.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-x-rex-2-launch-v2.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "new horizons",
+                "calibration"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-X-REX-2-LAUNCH-V2.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-x-rex-2-launch-v2.0",
-            "description": "This data set contains Raw data taken by the New Horizons Radio Science Experiment instrument during the post-launch checkout mission phase.  This is VERSION 2.0 of this data set. The REX datasets over the mission include calibrations using known radio sources, Jupiter, and cold sky measurements; operational readiness tests (ORTs); internal test pattern calibration; and prime science radiometry and occultation observations during the Pluto Encounter.",
-            "title": "NEW HORIZONS\n      REX POST-LAUNCH CHECKOUT\n      RAW V2.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "NEW HORIZONS\n      REX POST-LAUNCH CHECKOUT\n      RAW V2.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/2111",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Brock, C.A., K.D. Froyd, M. Dollner, C.J. Williamson, G.P. Schill, D.M. Murphy, N.L. Wagner, A. Kupc, J.L. Jimenez, P. Campuzano-Jost, B.A. Nault, J.C. Schroder, D.A. Day, D.J. Price, B.B. Weinzierl, J.P. Schwarz, J.M. Katich, S. Wang, L.H. Zeng, R. Webb, J.E. Dibb, E. Scheuer, G.S. Diskin, J.P. DiGangi, T.P. Bui, J.M. Dean-Day, C.R. Thompson, J. Peischl, T.B. Ryerson, I. Bourgeois, B.C. Daube, R. Commane, and S.C. Wofsy. 2022. ATom: Comprehensive Aerosol Properties, 2016-2018, Version 2. ORNL DAAC, Oak Ridge, Tennessee, USA. https://doi.org/10.3334/ORNLDAAC/2111",
-            "issued": "2023-08-18",
-            "temporal": "2016-07-29T02:42:40Z/2018-05-22T12:01:38Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-08-20",
-            "keyword": [
-                "atmosphere",
-                "aerosols",
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
-            "identifier": "C2698465642-ORNL_CLOUD",
             "description": "This dataset contains comprehensive measurements of aerosol microphysical, chemical, and optical properties derived for both dry and ambient conditions from in situ measurements made during the four ATom campaigns. The dataset includes composition-resolved size distributions the integrated mass of sulfate, organics, nitrate, sea salt, dust, black carbon, and other compounds in coarse and fine fractions; extinction and absorption coefficients from each species at both dry and ambient conditions; asymmetry parameters; Angstrom exponents; and fitted lognormal functions to describe the size distribution. Optical parameters are calculated for 10 wavelengths from the near UV to the near IR, and size distributions range from 3 nm to 50 um in diameter. One file contains these data at 1-minute time intervals. Another file contains a subset of these data averaged into 1-km vertical bins for each vertical profile the aircraft made, as well as composition-resolved integrated aerosol optical depth derived from each profile. The concentration of cloud condensation nuclei is calculated for 5 supersaturations.",
-            "graphic-preview-description": "Aerosol extinction across ATom campaigns. Sea salt is shown in (g) and (h), dust in (i) and (j), and water in (k) and (l). Source: Brock et al., 2021",
-            "title": "ATom: Comprehensive Aerosol Properties, 2016-2018, Version 2",
-            "graphic-preview-file": "https://daac.ornl.gov/ATOM/guides/ATom_Aerosol_Properties_V2_Fig1.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F2111",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F2111",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/atom/ATom_Aerosol_Properties_V2/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/atom/ATom_Aerosol_Properties_V2/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/ATOM/guides/ATom_Aerosol_Properties_V2.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/ATOM/guides/ATom_Aerosol_Properties_V2.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/2111",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/2111",
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
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/atom/ATom_Aerosol_Properties_V2/comp/ATom_Aerosol_Properties_V2.pdf",
-                    "description": "ATom: Comprehensive Aerosol Properties, 2016-2018, Version 2: ATom_Aerosol_Properties_V2.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "ATom: Comprehensive Aerosol Properties, 2016-2018, Version 2: ATom_Aerosol_Properties_V2.pdf",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/atom/ATom_Aerosol_Properties_V2/comp/ATom_Aerosol_Properties_V2.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/atom/ATom_Aerosol_Properties_V2/comp/Data_Dictionary_ATom_Aerosol_Properties_V2.csv",
-                    "description": "ATom: Comprehensive Aerosol Properties, 2016-2018, Version 2: Data_Dictionary_ATom_Aerosol_Properties_V2.csv",
                     "@type": "dcat:Distribution",
+                    "description": "ATom: Comprehensive Aerosol Properties, 2016-2018, Version 2: Data_Dictionary_ATom_Aerosol_Properties_V2.csv",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/atom/ATom_Aerosol_Properties_V2/comp/Data_Dictionary_ATom_Aerosol_Properties_V2.csv",
+                    "mediaType": "text/csv",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://daac.ornl.gov/ATOM/guides/ATom_Aerosol_Properties_V2_Fig1.png",
-                    "description": "Aerosol extinction across ATom campaigns. Sea salt is shown in (g) and (h), dust in (i) and (j), and water in (k) and (l). Source: Brock et al., 2021",
                     "@type": "dcat:Distribution",
+                    "description": "Aerosol extinction across ATom campaigns. Sea salt is shown in (g) and (h), dust in (i) and (j), and water in (k) and (l). Source: Brock et al., 2021",
+                    "downloadURL": "https://daac.ornl.gov/ATOM/guides/ATom_Aerosol_Properties_V2_Fig1.png",
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
+            "graphic-preview-description": "Aerosol extinction across ATom campaigns. Sea salt is shown in (g) and (h), dust in (i) and (j), and water in (k) and (l). Source: Brock et al., 2021",
+            "graphic-preview-file": "https://daac.ornl.gov/ATOM/guides/ATom_Aerosol_Properties_V2_Fig1.png",
+            "identifier": "C2698465642-ORNL_CLOUD",
+            "issued": "2023-08-18",
+            "keyword": [
+                "atmosphere",
+                "aerosols",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/2111",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2023-08-20",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "ORNL_DAAC"
+            },
             "spatial": "-180.0 -86.5 180.0 82.93",
+            "temporal": "2016-07-29T02:42:40Z/2018-05-22T12:01:38Z",
             "theme": [
                 "ATom",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "ATom: Comprehensive Aerosol Properties, 2016-2018, Version 2"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.nasa.gov/d/83ar-prbm",
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
+                    "downloadURL": "http://heasarc.gsfc.nasa.gov/db-perl/W3Browse/w3table.pl?tablehead=name%3Dfermilbsl&Action=More+Options",
+                    "mediaType": "text/html"
+                }
+            ],
+            "identifier": "NASA-0000222",
             "issued": "2018-06-25",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
             "keyword": [
                 "glast",
                 "glast ssc",
@@ -338518,44 +338530,44 @@
                 "fermi",
                 "high-energy"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Phil Newman",
-                "hasEmail": "mailto:panewman@lheapop.gsfc.nasa.gov"
-            },
+            "landingPage": "https://data.nasa.gov/d/83ar-prbm",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:014"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "NASA-0000222",
-            "description": "The Fermi Gamma-ray Space Telescope (Fermi) Large Area Telescope (LAT) is a successor to EGRET, with greatly improved sensitivity, resolution, and energy range. This web page presents the first full catalog of LAT sources, based on the first eleven months of survey data. For a full explanation about the catalog and its construction see the LAT 1-year Catalog Paper.",
-            "title": "LAT Bright Source List",
-            "programCode": [
-                "026:014"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://heasarc.gsfc.nasa.gov/db-perl/W3Browse/w3table.pl?tablehead=name%3Dfermilbsl&Action=More+Options",
-                    "mediaType": "text/html"
-                }
-            ],
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Space Science"
-            ]
+            ],
+            "title": "LAT Bright Source List"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1243119801-ASF.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, ASF.",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "undefined",
+                "hasEmail": "mailto:uso@asf.alaska.edu"
+            },
+            "description": "SMAP Level 1A Radar Product Metadata Version 2",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "Vertex, the ASF search and download interface",
+                    "downloadURL": "https://vertex.daac.asf.alaska.edu/",
+                    "mediaType": "text/html",
+                    "title": "Download this dataset"
+                }
+            ],
+            "identifier": "C1243119801-ASF",
             "issued": "2015-08-04",
-            "temporal": "2015-02-12T16:02:58Z/2022-01-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2015-12-20",
             "keyword": [
                 "earth science",
                 "smap",
@@ -338568,231 +338580,195 @@
                 "nasa decadal survey",
                 "radar"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "undefined",
-                "hasEmail": "mailto:uso@asf.alaska.edu"
-            },
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1243119801-ASF.html",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2015-12-20",
+            "programCode": [
+                "026:001"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "ASF"
             },
-            "identifier": "C1243119801-ASF",
-            "description": "SMAP Level 1A Radar Product Metadata Version 2",
-            "title": "SMAP_L1A_RADAR_METADATA_V002",
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
+            "title": "SMAP_L1A_RADAR_METADATA_V002"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1536049400-LARC_ASDC.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "1999-01-06.",
-            "issued": "1999-06-16",
-            "temporal": "1994-09-10T00:00:00Z/1994-09-19T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2015-09-29",
-            "keyword": [
-                "earth science",
-                "aerosols",
-                "atmosphere"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "DAVID WINKER",
                 "hasEmail": "mailto:david.m.winker@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Not provided"
-            },
-            "identifier": "C1536049400-LARC_ASDC",
             "description": "LITE_L1 data are LIDAR Vertical profile data along the orbital flight path of STS-64.Lidar In-Space Technology Experiment (LITE) used a three-wavelength (355 nm, 532 nm and 1064 nm) backscatter lidar which flew on the space shuttle Discovery as part of the STS-64 mission between September 9 and September 20, 1994. The LITE instrument was designed with the capability to make measurements of clouds, aerosols in the stratosphere and troposphere, the height of the planetary boundary layer, and atmospheric temperature and density in the stratosphere between 25 km and 40 km altitude. Additionally, limited measurements of the surface return strength over both land and ocean were collected to explore retrievals of surface properties.The LITE data were transmitted real time the by Ku-band system through TDRSS downlink to the LITE operations center at JSC. There was a gap in the high-rate coverage between 60 E and 85 E due to the zone of exclusion, where neither TDRSS satellite was in view. Additional random gaps in the data occurred due to telemetry dropouts during data transmission.The LITE L1 data product was formed by processing and reformatting the LITE high-rate telemetry data. The LITE L1 processing steps included:Correcting the profiles for instrument artifacts. Subtracting the DC offset from each lidar profile. Interpolating lidar profiles to a geolocated, common altitude grid, which extends from -4.985 to 40.0 km with a 15 m vertical resolution. Determining the LITE system calibration constants for the 355 nm and 532 nm wavelength profiles.Merged with the LITE L1 lidar profiles are: Identification Parameters, Time Parameters, Location Parameters, Operation Mode Parameters, Validity Flags, Measurement Location Descriptions, Temperature and Pressure Profiles Derived from NMC Data, Instrument Status Information.The archived files are concatenations of about 1000 (depending on data gaps) sets of headers and profiles. Read software programs written in C or IDL are available.",
-            "graphic-preview-description": "LITE images, including an orbit selection table with orbit tracks grouped by mission day",
-            "title": "Lidar In-Space Technology Experiment (LITE) L1",
-            "graphic-preview-file": "https://science-data.larc.nasa.gov/LITE/n_the_images.html",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/project/LITE",
-                    "description": "ASDC Data and Information for LITE",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Data and Information for LITE",
+                    "downloadURL": "https://asdc.larc.nasa.gov/project/LITE",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://science-data.larc.nasa.gov/LITE/",
-                    "description": "LITE mission home page",
                     "@type": "dcat:Distribution",
+                    "description": "LITE mission home page",
+                    "downloadURL": "https://science-data.larc.nasa.gov/LITE/",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1536049400-LARC_ASDC",
-                    "description": "Earthdata Search for LITE_L1_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for LITE_L1_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1536049400-LARC_ASDC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/lite/readme/L1formatdesc.txt",
-                    "description": "LITE Level 1 Data Format Description Document: LITE Level 1 Data Format",
                     "@type": "dcat:Distribution",
+                    "description": "LITE Level 1 Data Format Description Document: LITE Level 1 Data Format",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/lite/readme/L1formatdesc.txt",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/lite/readme/lite.readme",
-                    "description": "Readme Information about the LITE Sample Read Software and Data Files",
                     "@type": "dcat:Distribution",
+                    "description": "Readme Information about the LITE Sample Read Software and Data Files",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/lite/readme/lite.readme",
+                    "mediaType": "text/html",
                     "title": "View this dataset's read me document"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/lite/read_software/L1read.c",
-                    "description": "Sample C Code for Reading Lite Level 1 Data - Direct File Download (.c)",
                     "@type": "dcat:Distribution",
+                    "description": "Sample C Code for Reading Lite Level 1 Data - Direct File Download (.c)",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/lite/read_software/L1read.c",
+                    "mediaType": "text/html",
                     "title": "View this dataset's science data product software documentation"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/lite/read_software/L1scan.pro",
-                    "description": "Pro Level 1 Scan Code Updates Overview - October 2016",
                     "@type": "dcat:Distribution",
+                    "description": "Pro Level 1 Scan Code Updates Overview - October 2016",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/lite/read_software/L1scan.pro",
+                    "mediaType": "text/html",
                     "title": "View this dataset's science data product software documentation"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://science-data.larc.nasa.gov/LITE/n_the_publications.html",
-                    "description": "List of LITE Publications",
                     "@type": "dcat:Distribution",
+                    "description": "List of LITE Publications",
+                    "downloadURL": "https://science-data.larc.nasa.gov/LITE/n_the_publications.html",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://science-data.larc.nasa.gov/LITE/n_lite_camera.html",
-                    "description": "LITE Camera Photographs",
                     "@type": "dcat:Distribution",
+                    "description": "LITE Camera Photographs",
+                    "downloadURL": "https://science-data.larc.nasa.gov/LITE/n_lite_camera.html",
+                    "mediaType": "text/html",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://science-data.larc.nasa.gov/LITE/n_users_guide.html",
-                    "description": "LITE Data User's Guide",
                     "@type": "dcat:Distribution",
+                    "description": "LITE Data User's Guide",
+                    "downloadURL": "https://science-data.larc.nasa.gov/LITE/n_users_guide.html",
+                    "mediaType": "text/html",
                     "title": "View this dataset's user's guide"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://science-data.larc.nasa.gov/LITE/n_photo_imgs.html",
-                    "description": "LITE Images and Photographs",
                     "@type": "dcat:Distribution",
+                    "description": "LITE Images and Photographs",
+                    "downloadURL": "https://science-data.larc.nasa.gov/LITE/n_photo_imgs.html",
+                    "mediaType": "text/html",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://science-data.larc.nasa.gov/LITE/n_the_images.html",
-                    "description": "LITE images, including an orbit selection table with orbit tracks grouped by mission day",
                     "@type": "dcat:Distribution",
+                    "description": "LITE images, including an orbit selection table with orbit tracks grouped by mission day",
+                    "downloadURL": "https://science-data.larc.nasa.gov/LITE/n_the_images.html",
+                    "mediaType": "text/html",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/project/LITE/LITE_L1_1",
-                    "description": "Data set landing page for LITE_L1_1",
                     "@type": "dcat:Distribution",
+                    "description": "Data set landing page for LITE_L1_1",
+                    "downloadURL": "https://asdc.larc.nasa.gov/project/LITE/LITE_L1_1",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/citing-data",
-                    "description": "ASDC data citation policy",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC data citation policy",
+                    "downloadURL": "https://asdc.larc.nasa.gov/citing-data",
+                    "mediaType": "text/html",
                     "title": "View this dataset's data citation policy"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/LITE/LITE_L1/",
-                    "description": "ASDC Direct Data Download for LITE_L1_1",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for LITE_L1_1",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/LITE/LITE_L1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/LITE/LITE_L1/contents.html",
-                    "description": "OPeNDAP data access for LITE_L1_1",
                     "@type": "dcat:Distribution",
+                    "description": "OPeNDAP data access for LITE_L1_1",
+                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/LITE/LITE_L1/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 }
             ],
+            "graphic-preview-description": "LITE images, including an orbit selection table with orbit tracks grouped by mission day",
+            "graphic-preview-file": "https://science-data.larc.nasa.gov/LITE/n_the_images.html",
+            "identifier": "C1536049400-LARC_ASDC",
+            "issued": "1999-06-16",
+            "keyword": [
+                "earth science",
+                "aerosols",
+                "atmosphere"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1536049400-LARC_ASDC.html",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2015-09-29",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Not provided"
+            },
             "spatial": "<?xml version=\"1.0\" encoding=\"UTF-8\"?><gml:Polygon xmlns:gml=\"http://www.opengis.net/gml/3.2\" srsName=\"EPSG:9825\"><gml:outerBoundaryIs><gml:LinearRing><gml:posList>-60.0 -180.0 -60.0 180.0 60.0 180.0 60.0 -180.0 -60.0 -180.0</gml:posList></gml:LinearRing></gml:outerBoundaryIs><gml:innerBoundaryIs></gml:innerBoundaryIs></gml:Polygon>",
+            "temporal": "1994-09-10T00:00:00Z/1994-09-19T23:59:59.999Z",
             "theme": [
                 "LITE",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Lidar In-Space Technology Experiment (LITE) L1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://spotthestation.nasa.gov",
+            "accrualPeriodicity": "R/P1D",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2022-01-18",
-            "temporal": "2022-01-18T00:00:00Z/P1D",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-31",
-            "keyword": [
-                "coordinates",
-                "trajectory",
-                "topo",
-                "station",
-                "space",
-                "location",
-                "coords",
-                "ephemeris",
-                "international",
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
-            "identifier": "nasa-iss-data_2022-01-18_83dn-n826",
+            "dataQuality": true,
             "description": "This data represents the best estimated real-time trajectory and local sightings opportunities for the International Space Station (ISS) as generated by the Trajectory Operations and Planning (TOPO) flight controllers at Johnson Space Center.",
-            "title": "ISS_COORDS_2022-01-18",
-            "programCode": [
-                "026:004"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -338915,175 +338891,208 @@
                     "title": "XMLsightingData_natparksUSA02"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "nasa-iss-data_2022-01-18_83dn-n826",
+            "issued": "2022-01-18",
+            "keyword": [
+                "coordinates",
+                "trajectory",
+                "topo",
+                "station",
+                "space",
+                "location",
+                "coords",
+                "ephemeris",
+                "international",
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
+            "temporal": "2022-01-18T00:00:00Z/P1D",
             "theme": [
                 "Space Science"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "ISS_COORDS_2022-01-18"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-2-PRL-67PCHURYUMOV-M02-V3.0",
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
+            "description": "This CODMAC level 2 data set contains uncalibrated image data in DN unit, acquired by the OSIRIS Wide Angle Camera on the Rosetta spacecraft during the PRELANDING mission phase, covering the period from 2014-01-20T10:00:00.000 to 2014-05-07T12:47:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V3.0 supersedes previous deliveries of the same dataset with the following changes since the last version: Lien corrected dataset after the July and October 2018 PSA/PDS external peer reviews. Updated documentation and ancillary files, added document on bandpass filter. Updated SCIENCE_USER_GUIDE_V03.PDF to include one section about FAQ and one section about image data quality. Added shutter backtravel and readout issues to image quality map. Updated DATA_QUALITY_ID keyword in image header. Improved handling of images with missing packets. Included FITs files. Browse products changed to the same size as the original image.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-2-prl-67pchuryumov-m02-v3.0_83e9-szsd",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-2-PRL-67PCHURYUMOV-M02-V3.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-2-prl-67pchuryumov-m02-v3.0_83e9-szsd",
-            "description": "This CODMAC level 2 data set contains uncalibrated image data in DN unit, acquired by the OSIRIS Wide Angle Camera on the Rosetta spacecraft during the PRELANDING mission phase, covering the period from 2014-01-20T10:00:00.000 to 2014-05-07T12:47:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V3.0 supersedes previous deliveries of the same dataset with the following changes since the last version: Lien corrected dataset after the July and October 2018 PSA/PDS external peer reviews. Updated documentation and ancillary files, added document on bandpass filter. Updated SCIENCE_USER_GUIDE_V03.PDF to include one section about FAQ and one section about image data quality. Added shutter backtravel and readout issues to image quality map. Updated DATA_QUALITY_ID keyword in image header. Improved handling of images with missing packets. Included FITs files. Browse products changed to the same size as the original image.",
-            "title": "ROSETTA-ORBITER 67P OSIWAC 2 PRL-MTP002 EDR V3.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P OSIWAC 2 PRL-MTP002 EDR V3.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-5-DDR-ALBEDOS-V1.0",
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
+            "description": "Collected geometric albedos at various frequencies for 2030 asteroids.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-5-ddr-albedos-v1.0_83iu-vcag",
+            "issued": "2021-05-21",
+            "keyword": [
+                "asteroid",
+                "support archives"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-5-DDR-ALBEDOS-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-5-ddr-albedos-v1.0_83iu-vcag",
-            "description": "Collected geometric albedos at various frequencies for 2030 asteroids.",
-            "title": "ASTEROID ALBEDOS V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ASTEROID ALBEDOS V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RPCIES-5-EXT3-V1.0",
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
+            "description": "This dataset contains DERIVED DATA of the Rosetta RPCIES instrument taken during the mission extension 3 (EXT3). The target of this phase was comet 67P/CHURYUMOV-GERASIMENKO 1 (1969 R1). Included are the data taken between 01 Jul 2016 and 30 Sep 2016.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rpcies-5-ext3-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RPCIES-5-EXT3-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rpcies-5-ext3-v1.0",
-            "description": "This dataset contains DERIVED DATA of the Rosetta RPCIES instrument taken during the mission extension 3 (EXT3). The target of this phase was comet 67P/CHURYUMOV-GERASIMENKO 1 (1969 R1). Included are the data taken between 01 Jul 2016 and 30 Sep 2016.",
-            "title": "ROSETTA-ORBITER 67P RPCIES 5 EXT3 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RPCIES 5 EXT3 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=ULY-J-HISCALE-4-SUMM-LEMS120-V1.0",
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
-                "ulysses",
-                "jupiter"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This data set consists of HISCALE Low-Energy Magnetic Spectrometer (LEFS) ion counts at 120 degrees from the spacecraft spin axis. These measurements were taken during the Ulysses Jupiter encounter 1991-12-31 to 1992-02-16, and include 1 hour averaged inbound cruise data (1991-12-31 to 1992-02-01), and 15 minute averaged encounter data (1992-02-02 to 1992-02-16).",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.uly-j-hiscale-4-summ-lems120-v1.0_83nd-pgjx",
+            "issued": "2018-06-26",
+            "keyword": [
+                "ulysses",
+                "jupiter"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=ULY-J-HISCALE-4-SUMM-LEMS120-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.uly-j-hiscale-4-summ-lems120-v1.0_83nd-pgjx",
-            "description": "This data set consists of HISCALE Low-Energy Magnetic Spectrometer (LEFS) ion counts at 120 degrees from the spacecraft spin axis. These measurements were taken during the Ulysses Jupiter encounter 1991-12-31 to 1992-02-16, and include 1 hour averaged inbound cruise data (1991-12-31 to 1992-02-01), and 15 minute averaged encounter data (1992-02-02 to 1992-02-16).",
-            "title": "ULYSSES JUPITER HISCALE LEMS 120 ION COUNTS",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "ULYSSES JUPITER HISCALE LEMS 120 ION COUNTS"
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
+            "description": "CRISM, CTX, HiRISE, MARCI, MCS, RSS, SHARAD, SPICE",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://pds.jpl.nasa.gov/tools/subscription_service/SS-20081208.shtml",
+                    "mediaType": "application/html"
+                }
             ],
+            "identifier": "NASA-602",
+            "issued": "2018-06-25",
             "keyword": [
                 "rss",
                 "hirise",
@@ -339095,403 +339104,405 @@
                 "sharad",
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
-            "identifier": "NASA-602",
-            "description": "CRISM, CTX, HiRISE, MARCI, MCS, RSS, SHARAD, SPICE",
-            "title": "PDS Mars Reconnaissance Orbiter Data 7",
-            "programCode": [
-                "026:005"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://pds.jpl.nasa.gov/tools/subscription_service/SS-20081208.shtml",
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
+            "title": "PDS Mars Reconnaissance Orbiter Data 7"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-2-PRL-67PCHURYUMOV-M03-V1.0",
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
+            "description": "This data set contains images acquired between 2014-05-07 and 2014-06-04 by\nthe OSIRIS Narrow Angle Camera during the prelanding phase of the Rosetta\nmission at the comet 67P",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-2-prl-67pchuryumov-m03-v1.0_83si-fsg6",
+            "issued": "2018-06-26",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-2-PRL-67PCHURYUMOV-M03-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-2-prl-67pchuryumov-m03-v1.0_83si-fsg6",
-            "description": "This data set contains images acquired between 2014-05-07 and 2014-06-04 by\nthe OSIRIS Narrow Angle Camera during the prelanding phase of the Rosetta\nmission at the comet 67P",
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
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1220567906-USGS_LTA.html",
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
-                "land surface",
-                "surface radiative properties",
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
-            "identifier": "C1220567906-USGS_LTA",
             "description": "The surface reflectance CDR is generated from specialized software called Landsat Ecosystem Disturbance Adaptive Processing System (LEDAPS). LEDAPS was originally developed through a National Aeronautics and Space Administration (NASA) Making Earth System Data Records for Use in Research Environments (MEaSUREs)grant by NASA Goddard Space Flight Center (GSFC) and the University of Maryland (Masek et al., 2006). The software applies Moderate Resolution Imaging spectroradiometer (MODIS) atmospheric correction routines to Level-1 Landsat Thematic Mapper (TM) or Enhanced Thematic Mapper Plus (ETM+)data.  Water,vapor, ozone, geopotential height, aerosol optical thickness,and digital elevation are input with Landsat data to the Second Simulation of a Satellite Signal in the Solar Spectrum (6S) radiative transfer models to generate top of atmosphere (TOA)reflectance, surface reflectance, brightness temperature, and masks for clouds, cloud shadows, adjacent clouds, land, and water.  The result is delivered as the Landsat surface reflectance CDR.",
-            "title": "Land Surface Reflectance - 17-ETM+",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://earthexplorer.usgs.gov",
-                    "description": "\n         Data set searching and ordering capabilities are available through EarthExplorer at the above URL.  Query and order satellite images, aerial photographs, and cartographic products through the U.S. Geological Survey. Log in as a guest or as a registered user. Registered users have access to more features than guests do. If you plan on using EarthExplorer frequently, you may wish to register. Please note that this site uses Session Cookies and Java applets.\n      ",
                     "@type": "dcat:Distribution",
+                    "description": "\n         Data set searching and ordering capabilities are available through EarthExplorer at the above URL.  Query and order satellite images, aerial photographs, and cartographic products through the U.S. Geological Survey. Log in as a guest or as a registered user. Registered users have access to more features than guests do. If you plan on using EarthExplorer frequently, you may wish to register. Please note that this site uses Session Cookies and Java applets.\n      ",
+                    "downloadURL": "http://earthexplorer.usgs.gov",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 }
             ],
+            "identifier": "C1220567906-USGS_LTA",
+            "issued": "2019-09-20",
+            "keyword": [
+                "earth science",
+                "land surface",
+                "surface radiative properties",
+                "topography"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1220567906-USGS_LTA.html",
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
+            "title": "Land Surface Reflectance - 17-ETM+"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-P-LEISA-3-PLUTO-V2.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This data set contains Calibrated data taken by the New Horizons         Linear Etalon Imaging Spectral Array                                   instrument during the                                                    Pluto encounter                                                        mission phase.  This is VERSION 2.0 of this data set.                    This data set contains LEISA observations taken during the               the Approach (Jan-Jul, 2015) and Encounter mission sub-phases,           including flyby observations taken on 14.July, 2015; the data are        limited to those downlinked from the spacecraft as of the end of         January, 2016.  The rest of the downlinked data for this mission         phase will be delivered in a future data set.  Refer to the data         set description above and the sequence table provided in the             documentation for more detail about which observations are present       in this data set.                                                        This is version 2.0 of this data set.  Changes since version 1.0         include data downlinked between the end of July, 2015 and the end of     January, 2016.  These include Pluto observations around the time of      the flyby, the Charon hi-resolution observations and co-observations     with LORRI, Multi-map observations on 02.July, and Multi departure       longitude observations.                                                  Also, updates were made to the documentation and catalog files,          primarily to resolve liens from the V1.0 peer review.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-p-leisa-3-pluto-v2.0_83x7-b534",
             "issued": "2018-09-05",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "new horizons",
                 "charon",
                 "pluto"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-P-LEISA-3-PLUTO-V2.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-p-leisa-3-pluto-v2.0_83x7-b534",
-            "description": "This data set contains Calibrated data taken by the New Horizons         Linear Etalon Imaging Spectral Array                                   instrument during the                                                    Pluto encounter                                                        mission phase.  This is VERSION 2.0 of this data set.                    This data set contains LEISA observations taken during the               the Approach (Jan-Jul, 2015) and Encounter mission sub-phases,           including flyby observations taken on 14.July, 2015; the data are        limited to those downlinked from the spacecraft as of the end of         January, 2016.  The rest of the downlinked data for this mission         phase will be delivered in a future data set.  Refer to the data         set description above and the sequence table provided in the             documentation for more detail about which observations are present       in this data set.                                                        This is version 2.0 of this data set.  Changes since version 1.0         include data downlinked between the end of July, 2015 and the end of     January, 2016.  These include Pluto observations around the time of      the flyby, the Charon hi-resolution observations and co-observations     with LORRI, Multi-map observations on 02.July, and Multi departure       longitude observations.                                                  Also, updates were made to the documentation and catalog files,          primarily to resolve liens from the V1.0 peer review.",
-            "title": "NEW HORIZONS                            \n      LEISA PLUTO ENCOUNTER                                                   \n      CALIBRATED V2.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "NEW HORIZONS                            \n      LEISA PLUTO ENCOUNTER                                                   \n      CALIBRATED V2.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/VIIRS/VNP43D41.001",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Crystal Schaaf, Zhuosen Wang, Xiaoyang Zhang, Alan Strahler\r\n. 2019-11-07. VNP43D41. Version 001. VIIRS/NPP BRDF/Albedo Local Solar Noon Daily L3 Global 30ArcSec CMG V001\r\n. Sioux Falls, South Dakota, USA. Archived by National Aeronautics and Space Administration, U.S. Government, NASA EOSDIS Land Processes Distributed Active Archive Center. https://doi.org/10.5067/VIIRS/VNP43D41.001. https://doi.org/10.5067/VIIRS/VNP43D41.001. Digital Science Data. The DOI landing page provides citations in APA and Chicago styles.\r\n.",
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
-            "identifier": "C1607329254-LPDAAC_ECS",
-            "description": "The NASA/NOAA Suomi National Polar-orbiting Partnership (Suomi NPP) Visible Infrared Imaging Radiometer Suite (VIIRS) Bidirectional Reflectance Distribution Function (BRDF) and Albedo Local Solar Noon product (VNP43D41) is produced daily using 16 days of data at 30 arc second (1,000 meter) resolution. Data are temporally weighted to the ninth day, which is reflected in the file name. The VNP43D product suite is provided in a Climate Modeling Grid (CMG), which covers the entire globe for use in climate simulation models. Due to the large file size, each VNP43D product contains just one data layer for each of the parameters included in the VNP43MA2 (https://doi.org/10.5067/VIIRS/VNP43MA2.001) product. VNP43D40 through VNP43D53 are the 30 arc second BRDF/Albedo Quality values, the Local Solar Noon values, the Valid Observations of the moderate resolution bands (M1 through M5, M7, M8, M10, and M11) plus the Day/Night Band (DNB), the Snow Status, and the Uncertainty. Details regarding methodology are available on the VNP43MA2 product page and in the Algorithm Theoretical Basis Document (ATBD). \r\n\r\nVNP43D41 contains the local solar zenith angle at the local solar noon of the representative pixel for the retrieval period.",
-            "release-place": "Sioux Falls, South Dakota, USA",
-            "series-name": "VNP43D41",
             "creator": "Crystal Schaaf, Zhuosen Wang, Xiaoyang Zhang, Alan Strahler",
-            "title": "VIIRS/NPP BRDF/Albedo Local Solar Noon Daily L3 Global 30ArcSec CMG V001",
-            "programCode": [
-                "026:001"
-            ],
+            "data-presentation-form": "Digital Science Data",
+            "description": "The NASA/NOAA Suomi National Polar-orbiting Partnership (Suomi NPP) Visible Infrared Imaging Radiometer Suite (VIIRS) Bidirectional Reflectance Distribution Function (BRDF) and Albedo Local Solar Noon product (VNP43D41) is produced daily using 16 days of data at 30 arc second (1,000 meter) resolution. Data are temporally weighted to the ninth day, which is reflected in the file name. The VNP43D product suite is provided in a Climate Modeling Grid (CMG), which covers the entire globe for use in climate simulation models. Due to the large file size, each VNP43D product contains just one data layer for each of the parameters included in the VNP43MA2 (https://doi.org/10.5067/VIIRS/VNP43MA2.001) product. VNP43D40 through VNP43D53 are the 30 arc second BRDF/Albedo Quality values, the Local Solar Noon values, the Valid Observations of the moderate resolution bands (M1 through M5, M7, M8, M10, and M11) plus the Day/Night Band (DNB), the Snow Status, and the Uncertainty. Details regarding methodology are available on the VNP43MA2 product page and in the Algorithm Theoretical Basis Document (ATBD). \r\n\r\nVNP43D41 contains the local solar zenith angle at the local solar noon of the representative pixel for the retrieval period.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FVIIRS%2FVNP43D41.001",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FVIIRS%2FVNP43D41.001",
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
-                    "downloadURL": "https://doi.org/10.5067/VIIRS/VNP43D41.001",
-                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
+                    "downloadURL": "https://doi.org/10.5067/VIIRS/VNP43D41.001",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/xhdf5",
-                    "downloadURL": "https://e4ftl01.cr.usgs.gov/VIIRS/VNP43D41.001/",
-                    "description": "LP DAAC Data Pool provides direct access to available products via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "LP DAAC Data Pool provides direct access to available products via HTTPS.",
+                    "downloadURL": "https://e4ftl01.cr.usgs.gov/VIIRS/VNP43D41.001/",
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
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=C1607329254-LPDAAC_ECS",
-                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=C1607329254-LPDAAC_ECS",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://opendap.cr.usgs.gov/opendap/hyrax/VNP43D41.001/contents.html",
-                    "description": "Access data via Open-source Project for a Network Data Access Protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access data via Open-source Project for a Network Data Access Protocol.",
+                    "downloadURL": "https://opendap.cr.usgs.gov/opendap/hyrax/VNP43D41.001/contents.html",
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
-                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/filespec/VIIRS/1/VNP43D41",
-                    "description": "The File Specification provides a description of the product file including Scientific Data Sets and their attributes.",
                     "@type": "dcat:Distribution",
+                    "description": "The File Specification provides a description of the product file including Scientific Data Sets and their attributes.",
+                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/filespec/VIIRS/1/VNP43D41",
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
+            "identifier": "C1607329254-LPDAAC_ECS",
+            "issued": "2019-11-07",
+            "keyword": [
+                "surface radiative properties",
+                "earth science",
+                "land surface"
+            ],
+            "landingPage": "https://doi.org/10.5067/VIIRS/VNP43D41.001",
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
+            "series-name": "VNP43D41",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2012-01-19T00:00:00Z/2024-05-20T00:00:00Z",
             "theme": [
                 "NPP-JPSS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "VIIRS/NPP BRDF/Albedo Local Solar Noon Daily L3 Global 30ArcSec CMG V001"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RL-C-MUPUS-2-FSS-V1.0",
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
+            "description": "This archive contains edited data from the MUPUS instrument onboard ROSETTA Lander, acquired during the FSS phase. The primary target is the comet 67P/CHURYUMOV-GERASIMENKO. It also contains documentation which describes the MUPUS experiment. The data archived in this data set conform to the Planetary Data System Standards, Version 3.6.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.rl-c-mupus-2-fss-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RL-C-MUPUS-2-FSS-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.rl-c-mupus-2-fss-v1.0",
-            "description": "This archive contains edited data from the MUPUS instrument onboard ROSETTA Lander, acquired during the FSS phase. The primary target is the comet 67P/CHURYUMOV-GERASIMENKO. It also contains documentation which describes the MUPUS experiment. The data archived in this data set conform to the Planetary Data System Standards, Version 3.6.",
-            "title": "ROSETTA-LANDER 67P MUPUS 2 FSS V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-LANDER 67P MUPUS 2 FSS V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/SENTINEL-3B/OLCI/L3B/ERR/RRS/2022",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/GSFC/SED/ESD/GCDC/OB.DAAC. https://doi.org/10.5067/SENTINEL-3B/OLCI/L3B/ERR/RRS/2022.",
-            "issued": "2022-09-13",
-            "temporal": "2018-04-25T00:00:00Z/2024-04-22T00:00:00Z",
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
-            "identifier": "C2264534479-OB_DAAC",
             "description": "The Ocean and Land Colour Instrument (OLCI) is the successor to ENVISAT's Medium Resolution Imaging Spectrometer (MERIS) having additional spectral channels, different camera arrangements and simplified on-board processing. The OLCI is a push-broom instrument with five camera modules sharing the field of view. The field of view of the five cameras is arranged in a fan-shaped configuration in the vertical plane, perpendicular to the platform velocity. Each camera has an individual field of view of 14.2\u00b0 and a 0.6\u00b0 overlap with its neighbors. The whole field of view is shifted across track by 12.6\u00b0 away from the sun to minimize the impact of sun glint. OLCI is equipped with on-board calibration hardware based on sun diffusers. There are three sun diffusers--two 'white' diffusers dedicated to radiometric calibration and one dedicated to spectral calibration, with spectral reflectance features. The native resolution is approximately 300m, refered to as Full Resolution (FR). A Reduced Resolution (RR) processing mode provides Level-1B data at sampling rates decreased by a factor of four in both spatial dimensions resulting to resolution of approximately 1.2 km.",
-            "title": "Sentinel-3B OLCI Level-3B Global Binned Earth-observation Reduced Resolution (ERR) Remote-Sensing Reflectance (RRS) Data, version R2022.0",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSENTINEL-3B%2FOLCI%2FL3B%2FERR%2FRRS%2F2022",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSENTINEL-3B%2FOLCI%2FL3B%2FERR%2FRRS%2F2022",
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
                 }
             ],
+            "identifier": "C2264534479-OB_DAAC",
+            "issued": "2022-09-13",
+            "keyword": [
+                "atmospheric radiation",
+                "atmosphere",
+                "oceans",
+                "ocean optics",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/SENTINEL-3B/OLCI/L3B/ERR/RRS/2022",
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
+            "title": "Sentinel-3B OLCI Level-3B Global Binned Earth-observation Reduced Resolution (ERR) Remote-Sensing Reflectance (RRS) Data, version R2022.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.nasa.gov/d/83yz-nhj6",
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
+                    "downloadURL": "https://eosweb.larc.nasa.gov/project/calipso/cal_lid_l2_05kmclay-prov-v3-01_table",
+                    "mediaType": "text/html"
+                }
+            ],
+            "identifier": "NASA-0000168",
             "issued": "2018-06-25",
-            "temporal": "2006-06-13/2011-10-31",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
             "keyword": [
                 "climate",
                 "radiation",
@@ -339501,45 +339512,36 @@
                 "atmospheric science",
                 "satellite"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "John M. Kusterer",
-                "hasEmail": "mailto:john.m.kusterer@nasa.gov"
-            },
+            "landingPage": "https://data.nasa.gov/d/83yz-nhj6",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:004"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "NASA-0000168",
-            "description": "Cloud-Aerosol Lidar and Infrared Pathfinder Satellite Observations (CALIPSO) was launched on April 28, 2006 to study the impact of clouds and aerosols on the Earth\u2019s radiation budget and climate. It flies in formation with five other satellites in the international \u201cA-Train\u201d (PDF) constellation for coincident Earth observations. The CALIPSO satellite comprises three instruments, the Cloud-Aerosol LIdar with Orthogonal Polarization (CALIOP), the Imaging Infrared Radiometer (IIR), and the Wide Field Camera (WFC). CALIPSO is a joint satellite mission between NASA and the French Agency, CNES. These data consist 5 km aerosol layer data.",
-            "title": "CALIPSO Lidar L2 5 km Cloud Layer Data V3-01",
-            "programCode": [
-                "026:004"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://eosweb.larc.nasa.gov/project/calipso/cal_lid_l2_05kmclay-prov-v3-01_table",
-                    "mediaType": "text/html"
-                }
-            ],
-            "accrualPeriodicity": "irregular",
+            "temporal": "2006-06-13/2011-10-31",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "CALIPSO Lidar L2 5 km Cloud Layer Data V3-01"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=CO-S-ISSNA%2FISSWA-2-EDR-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "NULL",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.co-s-issna-isswa-2-edr-v1.0_83za-xdb9",
             "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "surtur",
                 "erriapo",
@@ -339599,385 +339601,354 @@
                 "hyrokkin",
                 "aegaeon"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=CO-S-ISSNA%2FISSWA-2-EDR-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.co-s-issna-isswa-2-edr-v1.0_83za-xdb9",
-            "description": "NULL",
-            "title": "CASSINI ORBITER SATURN\n                              ISSNA/ISSWA 2 EDR VERSION 1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "CASSINI ORBITER SATURN\n                              ISSNA/ISSWA 2 EDR VERSION 1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG2-U-POS-5-SUMM-HGCOORDS-48SEC-V1.0",
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
+            "description": "This dataset contains Voyager 2 position vectors relative to the Sun in both cartesian and spherical Heliographic coordinates for the time when Voyager 2 was near Uranus but not within its magnetosphere. The position vectors are given every 48 seconds. The units of the vector components are Au and degrees.  Vectors are stored as 4-byte floating point values.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg2-u-pos-5-summ-hgcoords-48sec-v1.0_842j-j8pn",
+            "issued": "2021-05-21",
+            "keyword": [
+                "voyager",
+                "uranus"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG2-U-POS-5-SUMM-HGCOORDS-48SEC-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg2-u-pos-5-summ-hgcoords-48sec-v1.0_842j-j8pn",
-            "description": "This dataset contains Voyager 2 position vectors relative to the Sun in both cartesian and spherical Heliographic coordinates for the time when Voyager 2 was near Uranus but not within its magnetosphere. The position vectors are given every 48 seconds. The units of the vector components are Au and degrees.  Vectors are stored as 4-byte floating point values.",
-            "title": "VG2 URA TRAJECTORY DERIV SUMM\n                                      HELIOGRAPHIC COORDS 48SEC V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "VG2 URA TRAJECTORY DERIV SUMM\n                                      HELIOGRAPHIC COORDS 48SEC V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1316",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Karion, A., C. Sweeney, J.B. Miller, A.E. Andrews, R. Commane, S.J. Dinardo, J. Henderson, J.O.W. Lindaas, J. Lin, K. Luus, T. Newberger, P. Tans, S.C. Wofsy, S. Wolter, and C.E. Miller. 2016. CARVE: CH4, CO2, and CO Atmospheric Concentrations, CARVE Tower, Alaska, 2012-2014. ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/1316",
-            "issued": "2016-05-12",
-            "temporal": "2012-01-01T00:00:00Z/2014-12-31T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-06-12",
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
-            "identifier": "C2236240052-ORNL_CLOUD",
             "description": "This data set provides hourly atmospheric concentrations of methane (CH4), carbon dioxide (CO2), and carbon monoxide (CO) as mole fractions, from January 2012 to December 2014 measured at the CARVE flux tower in Fox, Alaska (17 km north of Fairbanks) as part of NASA's Carbon in Arctic Reservoirs Vulnerability Experiment (CARVE). High-resolution meteorological fields from the Polar Weather Research and Forecasting (WRF) model coupled with the Stochastic Time-Inverted Lagrangian Transport model (WRF- STILT), along with the Polar Vegetation Photosynthesis and Respiration Model (PolarVPRM) were used to determine the influence region of the tower site and investigate the inter-annual and seasonal variability of regional fluxes of CO2 and CH4 in boreal Alaska using the tower observations. Modeled estimates of CH4, CO2, and CO background concentrations are provided. The WRF-STILT model \"footprints\" for the CARVE tower are provided with this data set.",
-            "graphic-preview-description": "Browse Image",
-            "title": "CARVE: CH4, CO2, and CO Atmospheric Concentrations, CARVE Tower, Alaska, 2012-2014",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/sdat-tds/1316_1_fit.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1316",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1316",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/carve/Alaskan_CH4_CO2_Fluxes/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/carve/Alaskan_CH4_CO2_Fluxes/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/CARVE/guides/Alaskan_CH4_CO2_Fluxes.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/CARVE/guides/Alaskan_CH4_CO2_Fluxes.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1316",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1316",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/carve/Alaskan_CH4_CO2_Fluxes/comp/Alaskan_CH4_CO2_Fluxes.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/carve/Alaskan_CH4_CO2_Fluxes/comp/Alaskan_CH4_CO2_Fluxes.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://daac.ornl.gov/graphics/browse/sdat-tds/1316_1_fit.png",
-                    "description": "Browse Image",
                     "@type": "dcat:Distribution",
+                    "description": "Browse Image",
+                    "downloadURL": "https://daac.ornl.gov/graphics/browse/sdat-tds/1316_1_fit.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://carve.ornl.gov",
-                    "description": "CARVE campaign site",
                     "@type": "dcat:Distribution",
+                    "description": "CARVE campaign site",
+                    "downloadURL": "https://carve.ornl.gov",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://thredds.daac.ornl.gov/thredds/catalog/ornldaac/1316/catalog.html",
-                    "description": "The THREDDS location for this Collection.",
                     "@type": "dcat:Distribution",
+                    "description": "The THREDDS location for this Collection.",
+                    "downloadURL": "https://thredds.daac.ornl.gov/thredds/catalog/ornldaac/1316/catalog.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "graphic-preview-description": "Browse Image",
+            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/sdat-tds/1316_1_fit.png",
+            "identifier": "C2236240052-ORNL_CLOUD",
+            "issued": "2016-05-12",
+            "keyword": [
+                "earth science",
+                "atmospheric chemistry",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1316",
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
             "spatial": "64.99 -147.6",
+            "temporal": "2012-01-01T00:00:00Z/2014-12-31T23:59:59Z",
             "theme": [
                 "CARVE",
                 "ABoVE",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "CARVE: CH4, CO2, and CO Atmospheric Concentrations, CARVE Tower, Alaska, 2012-2014"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/JWONK1ZTSBXX",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "SnowEx17 Radiometrics Surface-Based Radiometer Brightness Temperatures V001. Version 1. Archived by National Aeronautics and Space Administration, U.S. Government, NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/JWONK1ZTSBXX.",
-            "issued": "2017-02-14",
-            "temporal": "2017-02-14T00:00:00Z/2017-02-18T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2017-02-18",
-            "keyword": [
-                "earth science",
-                "microwave",
-                "spectral/engineering",
-                "cryosphere",
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
-            "identifier": "C1597736755-NSIDC_ECS",
             "description": "This data set consists of surface-based radiometer (SBR) brightness temperatures of the snow surface and vegetation at Grand Mesa, CO, USA, acquired during NASA's 2017 SnowEx campaign. Four SBRs were deployed in the field and obtained measurements at 89, 37, 19, and 10.67 GHz in both vertical (V-pol) and horizontal (H-pol) polarizations. Data are available for 37 locations across Grand Mesa collected over five days in February, 2017. They include both 2-4 minute observations and 20 minute, continuous measurements during surface melt, with the latter designed to capture the brightness temperature increase caused by the presence of liquid water in the snow. \n\nThis data set also contains snowfork measurements of snow wetness for 13 sites.",
-            "title": "SnowEx17 Radiometrics Surface-Based Radiometer Brightness Temperatures V001",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FJWONK1ZTSBXX",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FJWONK1ZTSBXX",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/SNOWEX/SNEX17_SBR.001/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/SNOWEX/SNEX17_SBR.001/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1597736755-NSIDC_ECS&m=20.84765625%21-108.59765625%213%211%210%210%2C2&q=SNEX17_SBR&ok=SNEX17_SBR",
-                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1597736755-NSIDC_ECS&m=20.84765625%21-108.59765625%213%211%210%210%2C2&q=SNEX17_SBR&ok=SNEX17_SBR",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/data/data-access-tool/SNEX17_SBR/versions/1/",
-                    "description": "Data Access link for ITSD project",
                     "@type": "dcat:Distribution",
+                    "description": "Data Access link for ITSD project",
+                    "downloadURL": "https://nsidc.org/data/data-access-tool/SNEX17_SBR/versions/1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/SNOWEX/SNEX17_SBR.001/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/SNOWEX/SNEX17_SBR.001/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1597736755-NSIDC_ECS&m=20.84765625%21-108.59765625%213%211%210%210%2C2&q=SNEX17_SBR&ok=SNEX17_SBR",
-                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1597736755-NSIDC_ECS&m=20.84765625%21-108.59765625%213%211%210%210%2C2&q=SNEX17_SBR&ok=SNEX17_SBR",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/data/data-access-tool/SNEX17_SBR/versions/1/",
-                    "description": "Data Access link for ITSD project",
                     "@type": "dcat:Distribution",
+                    "description": "Data Access link for ITSD project",
+                    "downloadURL": "https://nsidc.org/data/data-access-tool/SNEX17_SBR/versions/1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/JWONK1ZTSBXX",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/JWONK1ZTSBXX",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/JWONK1ZTSBXX",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/JWONK1ZTSBXX",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C1597736755-NSIDC_ECS",
+            "issued": "2017-02-14",
+            "keyword": [
+                "earth science",
+                "microwave",
+                "spectral/engineering",
+                "cryosphere",
+                "snow/ice"
+            ],
+            "landingPage": "https://doi.org/10.5067/JWONK1ZTSBXX",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2017-02-18",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA NSIDC DAAC"
+            },
             "spatial": "-108.2313453 39.02098 -107.846975 39.10552",
+            "temporal": "2017-02-14T00:00:00Z/2017-02-18T23:59:59.999Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "SnowEx17 Radiometrics Surface-Based Radiometer Brightness Temperatures V001"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-A-MIRO-2-AST2-LUTETIA-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This data set contains Spectroscopic, Continuum and Engineering data, in the form of table files, taken during the LUTETIA flyby phase of the Rosetta mission by the MIRO instrument.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-a-miro-2-ast2-lutetia-v1.0_845q-6vaq",
             "issued": "2021-05-21",
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
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-A-MIRO-2-AST2-LUTETIA-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-a-miro-2-ast2-lutetia-v1.0_845q-6vaq",
-            "description": "This data set contains Spectroscopic, Continuum and Engineering data, in the form of table files, taken during the LUTETIA flyby phase of the Rosetta mission by the MIRO instrument.",
-            "title": "ROSETTA-ORBITER LUTETIA MIRO 2 AST2 LUTETIA V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER LUTETIA MIRO 2 AST2 LUTETIA V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-3-ESC1-67PCHURYUMOV-M13-V1.0",
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
+            "description": "This data set contains calibrated images acquired by the OSIRIS Narrow Angle\nCamera during the escort phase of the Rosetta mission at the comet 67P,\ncovering the period from 2015-02-10 to 2015-03-10.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-3-esc1-67pchuryumov-m13-v1.0_845v-n4xa",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-3-ESC1-67PCHURYUMOV-M13-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-3-esc1-67pchuryumov-m13-v1.0_845v-n4xa",
-            "description": "This data set contains calibrated images acquired by the OSIRIS Narrow Angle\nCamera during the escort phase of the Rosetta mission at the comet 67P,\ncovering the period from 2015-02-10 to 2015-03-10.",
-            "title": "ROSETTA-ORBITER COMET ESCORT OSINAC 3 RDR MTP 013 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER COMET ESCORT OSINAC 3 RDR MTP 013 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://techport.nasa.gov/view/10964",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2011-04-01",
-            "temporal": "2011-04-01T00:00:00Z/2014-03-01T00:00:00Z",
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
-                "active",
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
-            "identifier": "TECHPORT_10964",
             "description": "&lt;p&gt;\r\n\tBuild and test a full size (4x2 meter aperture) breadboard antenna for SMLS.&lt;/p&gt;\r\n&lt;ul&gt;\r\n\t&lt;li&gt;\r\n\t\tDemonstrate critical azimuth scanning capability of a 4m SMLS antenna and its performance under thermal load environments.&lt;/li&gt;\r\n&lt;/ul&gt;",
-            "title": "A deployable 4-meter 180 to 680 GHz antenna for the Scanning Microwave Limb Sounder Project",
-            "programCode": [
-                "026:005"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -339985,42 +339956,51 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "TECHPORT_10964",
+            "issued": "2011-04-01",
+            "keyword": [
+                "project",
+                "active",
+                "nasa headquarters"
+            ],
+            "landingPage": "http://techport.nasa.gov/view/10964",
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
+            "temporal": "2011-04-01T00:00:00Z/2014-03-01T00:00:00Z",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "A deployable 4-meter 180 to 680 GHz antenna for the Scanning Microwave Limb Sounder Project"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://eros.usgs.gov/imagegallery/earth-art-3",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2014-04-29",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
-            "keyword": [
-                "earth science",
-                "landsat",
-                "usgs",
-                "imagery",
-                "images",
-                "earth as art"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Charles Ichoku",
                 "hasEmail": "mailto:james.r.irons@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Aeronautics and Space Administration"
-            },
-            "identifier": "NASA-911",
             "description": "The Earth Resources Observation and Science (EROS) Center manages the Earth as Art Three exhibit, which provides fresh and inspiring glimpses of different parts of our planet's complex surface.",
-            "title": "Earth Resources Observation and Science (EROS) Center's Earth as Art Image Gallery 3",
-            "programCode": [
-                "026:005"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -340028,358 +340008,356 @@
                     "mediaType": "application/html"
                 }
             ],
-            "accrualPeriodicity": "irregular",
+            "identifier": "NASA-911",
+            "issued": "2014-04-29",
+            "keyword": [
+                "earth science",
+                "landsat",
+                "usgs",
+                "imagery",
+                "images",
+                "earth as art"
+            ],
+            "landingPage": "http://eros.usgs.gov/imagegallery/earth-art-3",
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
+            "title": "Earth Resources Observation and Science (EROS) Center's Earth as Art Image Gallery 3"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/12",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Dabberdt, W. F. 1994. AMS (Automated Met Station) Data (FIFE). Data set. Available on-line [http://www.daac.ornl.gov] from Oak Ridge National Laboratory Distributed Active Archive Center, Oak Ridge, Tennessee, U.S.A. Also published in D. E. Strebel, D. R. Landis, K. F. Huemmrich, and B. W. Meeson (eds.), Collected Data of the First ISLSCP Field Experiment, Vol. 1: Surface Observations and Non-Image Data Sets. CD-ROM. National Aeronautics and Space Administration, Goddard Space Flight Center, Greenbelt, Maryland, U.S.A. (available from http://www.daac.ornl.gov). doi:10.3334/ORNLDAAC/12",
-            "issued": "2024-05-05",
-            "temporal": "1987-05-01T00:00:00Z/1989-11-10T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-06",
-            "keyword": [
-                "earth science",
-                "atmospheric radiation",
-                "atmospheric pressure",
-                "atmosphere",
-                "agriculture",
-                "atmospheric winds",
-                "biosphere",
-                "vegetation",
-                "atmospheric temperature",
-                "soils",
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
-            "identifier": "C2978103551-ORNL_CLOUD",
             "description": "30 minute average meteorological data from NCARs Portable Automated Mesonet Station",
-            "graphic-preview-description": "Browse Image",
-            "title": "AMS (Automated Met Station) Data (FIFE)",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/fife_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F12",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F12",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/fife/fife_sur_met_ams/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/fife/fife_sur_met_ams/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/FIFE/guides/AMS_Data.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/FIFE/guides/AMS_Data.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/12",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/12",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/msword",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/fife/fife_sur_met_ams/comp/ams_data.doc",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/fife/fife_sur_met_ams/comp/ams_data.doc",
+                    "mediaType": "application/msword",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/fife/fife_sur_met_ams/comp/AMS_Data.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/fife/fife_sur_met_ams/comp/AMS_Data.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/fife/fife_sur_met_ams/comp/ams_data.tdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/fife/fife_sur_met_ams/comp/ams_data.tdf",
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
+            "identifier": "C2978103551-ORNL_CLOUD",
+            "issued": "2024-05-05",
+            "keyword": [
+                "earth science",
+                "atmospheric radiation",
+                "atmospheric pressure",
+                "atmosphere",
+                "agriculture",
+                "atmospheric winds",
+                "biosphere",
+                "vegetation",
+                "atmospheric temperature",
+                "soils",
+                "precipitation"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/12",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2024-05-06",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "ORNL_DAAC"
+            },
             "spatial": "-96.61 38.98 -96.47 39.12",
+            "temporal": "1987-05-01T00:00:00Z/1989-11-10T23:59:59Z",
             "theme": [
                 "FIFE",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "AMS (Automated Met Station) Data (FIFE)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-PRL-0274-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the PRELANDING phase 2014-01-21 to 2014-11-18. It is a Global Gravity measurement at the comet 67P and covers the time 2014-09-06T06:47:05.000 to 2014-09-06T17:27:14.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-prl-0274-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-PRL-0274-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-prl-0274-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the PRELANDING phase 2014-01-21 to 2014-11-18. It is a Global Gravity measurement at the comet 67P and covers the time 2014-09-06T06:47:05.000 to 2014-09-06T17:27:14.000.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     PRELANDING 0274 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     PRELANDING 0274 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/E7TYRXPJKWOQ",
             "citation": "Beaudoing, H. and M. Rodell,  NASA/GSFC/HSL. 2020-01-30. GLDAS_NOAH025_3H. Version 2.1. GLDAS Noah Land Surface Model L4 3 hourly 0.25 x 0.25 degree V2.1. Greenbelt, Maryland, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/E7TYRXPJKWOQ. https://disc.gsfc.nasa.gov/datacollection/GLDAS_NOAH025_3H_2.1.html. Digital Science Data.",
-            "issued": "2020-01-30",
-            "temporal": "2000-01-01T00:00:00Z/2022-01-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-30",
-            "references": [
-                "https://doi.org/10.1175/BAMS-85-3-381"
-            ],
-            "keyword": [
-                "surface water",
-                "atmosphere",
-                "atmospheric pressure",
-                "atmospheric radiation",
-                "atmospheric temperature",
-                "atmospheric water vapor",
-                "atmospheric winds",
-                "terrestrial hydrosphere",
-                "earth science",
-                "land surface",
-                "precipitation",
-                "snow/ice",
-                "soils",
-                "surface thermal properties"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "HUALAN RUI",
                 "hasEmail": "mailto:Hualan.Rui@nasa.gov"
             },
+            "creator": "Beaudoing, H. and M. Rodell,  NASA/GSFC/HSL",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C1342986035-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "NASA Global Land Data Assimilation System Version 2 (GLDAS-2) has three components: GLDAS-2.0, GLDAS-2.1, and GLDAS-2.2.  GLDAS-2.0 is forced entirely with the Princeton meteorological forcing input data and provides a temporally consistent series from 1948 through 2014.  GLDAS-2.1 is forced with a combination of model and observation data from 2000 to present.  GLDAS-2.2 product suites use data assimilation (DA), whereas the GLDAS-2.0 and GLDAS-2.1 products are \"open-loop\" (i.e., no data assimilation).  The choice of forcing data, as well as DA observation source, variable, and scheme, vary for different GLDAS-2.2 products.\n\nGLDAS-2.1 data products are now available in two production streams: one stream is forced with combined forcing data including GPCP version 1.3 (the main production stream), and the other stream is processed without this forcing data (the early production stream). Since the GPCP Version 1.3 data have a 3-4 month latency, the GLDAS-2.1 data products are first created without it, and are designated as Early Products (EPs), with about 1.5 month latency. Once the GPCP Version 1.3 data become available, the GLDAS-2.1 data products are processed in the main production stream and are removed from the Early Products archive.\n\nThis data product, reprocessed in January 2020, is for GLDAS-2.1 Noah 3-hourly 0.25 degree data from the main production stream and it is a replacement to its previous version.\n\nThe 3-hourly data product was simulated with the Noah Model 3.6 in Land Information System (LIS) Version 7.  The data product contains 36 land surface fields from January 2000 to present.  The GLDAS-2.1 data are archived and distributed in NetCDF format. The GLDAS-2.1 products supersede their corresponding GLDAS-1 products.\n\nThe GLDAS-2.1 simulation started on January 1, 2000 using the conditions from the GLDAS-2.0 simulation. This simulation was forced with National Oceanic and Atmospheric Administration (NOAA)/Global Data Assimilation System (GDAS) atmospheric analysis fields (Derber et al., 1991), the disaggregated Global Precipitation Climatology Project (GPCP) V1.3 Daily Analysis precipitation fields (Adler et al., 2003; Huffman et al., 2001), and the Air Force Weather Agency's AGRicultural METeorological modeling system (AGRMET) radiation fields.  The simulation used with GDAS and GPCP only from 2000 to February 2001, followed by addition of AGRMET for March 1, 2001 onwards.\n\nIn October 2020, all 3-hourly and monthly GLDAS-2 data were post-processed with the MOD44W MODIS land mask. Previously, some grid boxes over inland water were considered as over land and, thus, had non-missing values. The post-processing corrected this issue and masked out all model output data over inland water; the post-processing did not affect the meteorological forcing variables. More information can be found in the GLDAS-2 README. The MOD44W MODIS land mask is available on the GLDAS Project site.\n\nIf you had downloaded the GLDAS data prior to November 2020, please download the data again to receive the post-processed data.",
-            "release-place": "Greenbelt, Maryland, USA",
-            "series-name": "GLDAS_NOAH025_3H",
-            "creator": "Beaudoing, H. and M. Rodell,  NASA/GSFC/HSL",
-            "graphic-preview-description": "The GES-DISC Interactive Online Visualization ANd aNalysis Interface (Giovanni) is a web-based tool that allows users to interactively visualize and analyze data.",
-            "title": "GLDAS Noah Land Surface Model L4 3 hourly 0.25 x 0.25 degree V2.1 (GLDAS_NOAH025_3H) at GES DISC",
-            "graphic-preview-file": "https://giovanni.gsfc.nasa.gov/giovanni/#dataKeyword=GLDAS_NOAH025_3H_2_1",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FE7TYRXPJKWOQ",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FE7TYRXPJKWOQ",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/GLDAS_NOAH025_3H_2.1.png",
-                    "description": "GLDAS-2.1 Noah 3-hourly 0.25 Degree 0-10 cm Soil Moisture [kg m-2] for 03Z Jan 01, 2000.",
                     "@type": "dcat:Distribution",
+                    "description": "GLDAS-2.1 Noah 3-hourly 0.25 Degree 0-10 cm Soil Moisture [kg m-2] for 03Z Jan 01, 2000.",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/GLDAS_NOAH025_3H_2.1.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/GLDAS_NOAH025_3H_2.1.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/GLDAS_NOAH025_3H_2.1.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://hydro1.gesdisc.eosdis.nasa.gov/data/GLDAS/GLDAS_NOAH025_3H.2.1/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://hydro1.gesdisc.eosdis.nasa.gov/data/GLDAS/GLDAS_NOAH025_3H.2.1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=GLDAS_NOAH025_3H_2.1",
-                    "description": "Use the Earthdata Search Client (EDSC) to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search Client (EDSC) to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=GLDAS_NOAH025_3H_2.1",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://giovanni.gsfc.nasa.gov/giovanni/#dataKeyword=GLDAS_NOAH025_3H_2_1",
-                    "description": "The GES-DISC Interactive Online Visualization ANd aNalysis Interface (Giovanni) is a web-based tool that allows users to interactively visualize and analyze data.",
                     "@type": "dcat:Distribution",
+                    "description": "The GES-DISC Interactive Online Visualization ANd aNalysis Interface (Giovanni) is a web-based tool that allows users to interactively visualize and analyze data.",
+                    "downloadURL": "https://giovanni.gsfc.nasa.gov/giovanni/#dataKeyword=GLDAS_NOAH025_3H_2_1",
+                    "mediaType": "text/html",
                     "title": "Get a related visualization through GIOVANNI"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://hydro1.gesdisc.eosdis.nasa.gov/opendap/GLDAS/GLDAS_NOAH025_3H.2.1/",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://hydro1.gesdisc.eosdis.nasa.gov/opendap/GLDAS/GLDAS_NOAH025_3H.2.1/",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://hydro1.gesdisc.eosdis.nasa.gov/dods/GLDAS_NOAH025_3H.2.1/",
-                    "description": "The GrADS Data Server (GDS) is another form of OPeNDAP that provides subsetting and some analysis services across the Internet.",
                     "@type": "dcat:Distribution",
+                    "description": "The GrADS Data Server (GDS) is another form of OPeNDAP that provides subsetting and some analysis services across the Internet.",
+                    "downloadURL": "https://hydro1.gesdisc.eosdis.nasa.gov/dods/GLDAS_NOAH025_3H.2.1/",
+                    "mediaType": "text/html",
                     "title": "Use GRADS DATA SERVER (GDS) to access the dataset's data"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://hydro1.gesdisc.eosdis.nasa.gov/data/GLDAS/GLDAS_NOAH025_3H.2.1/doc/README_GLDAS2.pdf",
-                    "description": "README Document",
                     "@type": "dcat:Distribution",
+                    "description": "README Document",
+                    "downloadURL": "https://hydro1.gesdisc.eosdis.nasa.gov/data/GLDAS/GLDAS_NOAH025_3H.2.1/doc/README_GLDAS2.pdf",
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
-                    "downloadURL": "https://disc.gsfc.nasa.gov/information/tools?title=Hydrology+Data+Rods",
-                    "description": "GES DISC Data Rods Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "GES DISC Data Rods Documentation",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/information/tools?title=Hydrology+Data+Rods",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://hydro1.gesdisc.eosdis.nasa.gov/thredds/catalog/GLDAS_aggregation/GLDAS_NOAH025_3H.2.1/catalog.html",
-                    "description": "Time aggregated THREDDS Data Server (TDS)",
                     "@type": "dcat:Distribution",
+                    "description": "Time aggregated THREDDS Data Server (TDS)",
+                    "downloadURL": "https://hydro1.gesdisc.eosdis.nasa.gov/thredds/catalog/GLDAS_aggregation/GLDAS_NOAH025_3H.2.1/catalog.html",
+                    "mediaType": "text/html",
                     "title": "Use THREDDS DATA to download the dataset's data"
                 }
             ],
+            "graphic-preview-description": "The GES-DISC Interactive Online Visualization ANd aNalysis Interface (Giovanni) is a web-based tool that allows users to interactively visualize and analyze data.",
+            "graphic-preview-file": "https://giovanni.gsfc.nasa.gov/giovanni/#dataKeyword=GLDAS_NOAH025_3H_2_1",
+            "identifier": "C1342986035-GES_DISC",
+            "issued": "2020-01-30",
+            "keyword": [
+                "surface water",
+                "atmosphere",
+                "atmospheric pressure",
+                "atmospheric radiation",
+                "atmospheric temperature",
+                "atmospheric water vapor",
+                "atmospheric winds",
+                "terrestrial hydrosphere",
+                "earth science",
+                "land surface",
+                "precipitation",
+                "snow/ice",
+                "soils",
+                "surface thermal properties"
+            ],
+            "landingPage": "https://doi.org/10.5067/E7TYRXPJKWOQ",
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
+            "series-name": "GLDAS_NOAH025_3H",
             "spatial": "-180.0 -60.0 180.0 90.0",
+            "temporal": "2000-01-01T00:00:00Z/2022-01-17T00:00:00Z",
             "theme": [
                 "GLDAS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "GLDAS Noah Land Surface Model L4 3 hourly 0.25 x 0.25 degree V2.1 (GLDAS_NOAH025_3H) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/Aura/MLS/DATA/3543",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Froidevaux, L., Livesey, N., Read, W., and Fuller, R.. 2021-04-29. ML3MBHOCL. Version 005. MLS/Aura Level 3 Monthly Binned Hypochlorous Acid (HOCl) Mixing Ratio on Assorted Grids V005. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/Aura/MLS/DATA/3543. https://disc.gsfc.nasa.gov/datacollection/ML3MBHOCL_005.html. Digital Science Data.",
-            "issued": "2021-04-29",
-            "temporal": "2004-08-02T00:00:00Z/2022-01-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2021-04-29",
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
-            "identifier": "C2042568517-GES_DISC",
-            "description": "ML3MBHOCL is the EOS Aura Microwave Limb Sounder (MLS) monthly binned on various vertical grids product for hypochlorous acid (HOCl) derived from radiances measured primarily by the 640 GHz radiometer. The data version is 5.1. Spatial coverage is near-global (-82 to +82 degrees latitude) at a spatial resolution of 4 degrees latitude by 5 degrees longitude. The recommended useful vertical range is from 10 to 2.15 hPa, and the vertical resolution is about 6 km. Users of the ML3MBOHCL data product should read chapter 4 and section 3.14 of the EOS MLS Level 2 Version 5 Quality Document for more information.\n\nThe data files are archived in the netCDF4 format, which is also compatible with HDF5 readers and tools. Each file contains six group objects: lat-lon map vs pressure, lat vs pressure zonal mean, lat-lon map vs \"potential temperature\", lat vs \"potential temperature\" zonal mean, \"equivalent latitude\" vs \"potential temperature\" zonal mean, and vortex average vs \"potential temperature\". These are further subdivided into groups with all valid, ascending orbit, descending orbit, daytime (SZA < 90), and nighttime (SZA > 110) profiles. Each group has a set of data (average, min, max, std dev, rms) and geolocation fields, grid attributes, and metadata.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "ML3MBHOCL",
             "creator": "Froidevaux, L., Livesey, N., Read, W., and Fuller, R.",
-            "title": "MLS/Aura Level 3 Monthly Binned Hypochlorous Acid (HOCl) Mixing Ratio on Assorted Grids V005 (ML3MBHOCL) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/ML3MBHOCL_005.png",
-            "programCode": [
-                "026:001"
-            ],
+            "data-presentation-form": "Digital Science Data",
+            "description": "ML3MBHOCL is the EOS Aura Microwave Limb Sounder (MLS) monthly binned on various vertical grids product for hypochlorous acid (HOCl) derived from radiances measured primarily by the 640 GHz radiometer. The data version is 5.1. Spatial coverage is near-global (-82 to +82 degrees latitude) at a spatial resolution of 4 degrees latitude by 5 degrees longitude. The recommended useful vertical range is from 10 to 2.15 hPa, and the vertical resolution is about 6 km. Users of the ML3MBOHCL data product should read chapter 4 and section 3.14 of the EOS MLS Level 2 Version 5 Quality Document for more information.\n\nThe data files are archived in the netCDF4 format, which is also compatible with HDF5 readers and tools. Each file contains six group objects: lat-lon map vs pressure, lat vs pressure zonal mean, lat-lon map vs \"potential temperature\", lat vs \"potential temperature\" zonal mean, \"equivalent latitude\" vs \"potential temperature\" zonal mean, and vortex average vs \"potential temperature\". These are further subdivided into groups with all valid, ascending orbit, descending orbit, daytime (SZA < 90), and nighttime (SZA > 110) profiles. Each group has a set of data (average, min, max, std dev, rms) and geolocation fields, grid attributes, and metadata.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAura%2FMLS%2FDATA%2F3543",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAura%2FMLS%2FDATA%2F3543",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
@@ -340389,234 +340367,270 @@
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/ML3MBHOCL_005.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/ML3MBHOCL_005.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/Aura_MLS_Level3/ML3MBHOCL.005/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/Aura_MLS_Level3/ML3MBHOCL.005/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/opendap/HDF-EOS5/Aura_MLS_Level3/ML3MBHOCL.005/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/opendap/HDF-EOS5/Aura_MLS_Level3/ML3MBHOCL.005/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=ML3MBHOCL_005",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=ML3MBHOCL_005",
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
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/ML3MBHOCL_005.png",
+            "identifier": "C2042568517-GES_DISC",
+            "issued": "2021-04-29",
+            "keyword": [
+                "earth science",
+                "atmosphere",
+                "atmospheric chemistry"
+            ],
+            "landingPage": "https://doi.org/10.5067/Aura/MLS/DATA/3543",
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
+            "series-name": "ML3MBHOCL",
             "spatial": "-180.0 -82.0 180.0 82.0",
+            "temporal": "2004-08-02T00:00:00Z/2022-01-17T00:00:00Z",
             "theme": [
                 "Aura",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "MLS/Aura Level 3 Monthly Binned Hypochlorous Acid (HOCl) Mixing Ratio on Assorted Grids V005 (ML3MBHOCL) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/370",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Valentine, D. 1998. BOREAS TF-11 CO2 and CH4 Concentration Data from the SSA-Fen. ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/370",
-            "issued": "2023-11-22",
-            "temporal": "1994-06-08T00:00:00Z/1994-09-17T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-11-28",
-            "keyword": [
-                "earth science",
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
-            "identifier": "C2808131091-ORNL_CLOUD",
             "description": "Contains temperature, pH, and CH4 and CO2 concentration profiles in the surface 50 cm of peat.",
-            "graphic-preview-description": "Browse Image",
-            "title": "BOREAS TF-11 CO2 and CH4 Concentration Data from the SSA-Fen",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/boreas_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F370",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F370",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/boreas/TF/tf11conc/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/boreas/TF/tf11conc/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/BOREAS/guides/TF11_CH4_CO2_Conc.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/BOREAS/guides/TF11_CH4_CO2_Conc.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/370",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/370",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TF/tf11conc/comp/tf11conc.def",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TF/tf11conc/comp/tf11conc.def",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/msword",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TF/tf11conc/comp/TF11_CH4_CO2_Conc.doc",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TF/tf11conc/comp/TF11_CH4_CO2_Conc.doc",
+                    "mediaType": "application/msword",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TF/tf11conc/comp/TF11_CH4_CO2_Conc.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TF/tf11conc/comp/TF11_CH4_CO2_Conc.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TF/tf11conc/comp/TF11_CH4_CO2_Conc.txt",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TF/tf11conc/comp/TF11_CH4_CO2_Conc.txt",
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
+            "identifier": "C2808131091-ORNL_CLOUD",
+            "issued": "2023-11-22",
+            "keyword": [
+                "earth science",
+                "land surface",
+                "soils"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/370",
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
             "spatial": "53.8 -104.62",
+            "temporal": "1994-06-08T00:00:00Z/1994-09-17T23:59:59Z",
             "theme": [
                 "BOREAS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "BOREAS TF-11 CO2 and CH4 Concentration Data from the SSA-Fen"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://c3.nasa.gov/dashlink/resources/67/",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2010-09-10",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
-            "keyword": [
-                "dashlink",
-                "nasa",
-                "ames"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ole Mengshoel",
                 "hasEmail": "mailto:ole.j.mengshoel@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Dashlink"
-            },
-            "identifier": "DASHLINK_67",
             "description": "We present in this article a case study of the probabilistic\r\napproach to model-based diagnosis. Here, the diagnosed\r\nsystem is a real-world electrical power system, namely the\r\nAdvanced Diagnostic and Prognostic Testbed (ADAPT) located\r\nat the NASA Ames Research Center. Our probabilistic approach\r\nis formally well-founded, and based on Bayesian networks and\r\narithmetic circuits. We pay special attention to meeting two of the\r\nmain challenges \u0097 model development and real-time reasoning\r\n\u0097 often associated with real-world application of model-based\r\ndiagnosis technologies. To address the challenge of model development,\r\nwe develop a systematic approach to representing electrical\r\npower systems as Bayesian networks, supported by an easy-touse\r\nspeci\u0002cation language. To address the real-time reasoning\r\nchallenge, we compile Bayesian networks into arithmetic circuits.\r\nArithmetic circuit evaluation supports real-time diagnosis by\r\nbeing predictable and fast. In experiments with the ADAPT\r\nBayesian network, which contains 503 discrete nodes and 579\r\nedges and produces accurate results, the time taken to compute\r\nthe most probable explanation using arithmetic circuits has a\r\nmean of 0.2625 milliseconds and a standard deviation of 0.2028\r\nmilliseconds. In comparative experiments, we found that while\r\nthe variable elimination and join tree propagation algorithms\r\nalso perform very well in the ADAPT setting, arithmetic circuit\r\nevaluation was an order of magnitude or more faster.\r\n\r\n**Reference:**\r\n\r\nO. J. Mengshoel, M. Chavira, K. Cascio, S. Poll, A. Darwiche,\r\nand S. Uckun. \"Probabilistic Model-Based Diagnosis: An Electrical\r\nPower System Case Study\u201d. Accepted to IEEE Transactions on\r\nSystems, Man, and Cybernetics, Part A, 2009.",
-            "title": "Probabilistic Model-Based Diagnosis for Electrical Power Systems",
-            "programCode": [
-                "026:029"
-            ],
             "distribution": [
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/publication/SMCA08-04-0141-Paper.pdf",
-                    "description": "Article",
                     "@type": "dcat:Distribution",
+                    "description": "Article",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/publication/SMCA08-04-0141-Paper.pdf",
+                    "mediaType": "application/pdf",
                     "title": "SMCA08-04-0141-Paper.pdf"
                 }
             ],
-            "accrualPeriodicity": "irregular"
+            "identifier": "DASHLINK_67",
+            "issued": "2010-09-10",
+            "keyword": [
+                "dashlink",
+                "nasa",
+                "ames"
+            ],
+            "landingPage": "https://c3.nasa.gov/dashlink/resources/67/",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:029"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Dashlink"
+            },
+            "title": "Probabilistic Model-Based Diagnosis for Electrical Power Systems"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.nasa.gov/d/84ea-fpze",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "GeneLab Outreach",
+                "hasEmail": "mailto:genelab-outreach@lists.nasa.gov"
+            },
+            "description": "BACKGROUND: Ionizing radiation (IR) can be extremely harmful for human cells since an improper DNA-damage response (DDR) to IR can contribute to carcinogenesis initiation. Perturbations in DDR pathway can originate from alteration in the functionality of the microRNA-mediated gene regulation being microRNAs (miRNAs) small noncoding RNA that act as post-transcriptional regulators of gene expression. In this study we gained insight into the role of miRNAs in the regulation of DDR to IR under microgravity a condition of weightlessness experienced by astronauts during space missions which could have a synergistic action on cells increasing the risk of radiation exposure. METHODOLOGY/PRINCIPAL FINDINGS: We analyzed miRNA expression profile of human peripheral blood lymphocytes (PBL) incubated for 4 and 24 h in normal gravity (1 g) and in modeled microgravity (MMG) during the repair time after irradiation with 0.2 and 2Gy of gamma-rays. Our results show that MMG alters miRNA expression signature of irradiated PBL by decreasing the number of radio-responsive miRNAs. Moreover let-7i* miR-7 miR-7-1* miR-27a miR-144 miR-200a miR-598 miR-650 are deregulated by the combined action of radiation and MMG. Integrated analyses of miRNA and mRNA expression profiles carried out on PBL of the same donors identified significant miRNA-mRNA anti-correlations of DDR pathway. Gene Ontology analysis reports that the biological category of Response to DNA damage is enriched when PBL are incubated in 1 g but not in MMG. Moreover some anti-correlated genes of p53-pathway show a different expression level between 1 g and MMG. Functional validation assays using luciferase reporter constructs confirmed miRNA-mRNA interactions derived from target prediction analyses. CONCLUSIONS/SIGNIFICANCE: On the whole by integrating the transcriptome and microRNome we provide evidence that modeled microgravity can affects the DNA-damage response to IR in human PBL. Overall Design: Gene expression signature was defined in PBL irradiated with gamma-rays (2.0 Gy) and incubated in modeled microgravity (mmg) and in parallel ground conditions (1g) for 24h. Five independent experiments were performed for each donor to address which mRNAs were regulated on IR stress. The level of each transcript was represented as Log2.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "GeneLab Study Page",
+                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-129",
+                    "mediaType": "text/html",
+                    "title": "Gene expression profiling of PBL in response to ionising radiation and modeled microgravity"
+                }
+            ],
+            "identifier": "nasa_genelab_GLDS-129_84ea-fpze",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
             "keyword": [
                 "simulated microgravity",
                 "labeling",
@@ -340627,95 +340641,90 @@
                 "nucleic acid hybridization",
                 "rna extraction"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "GeneLab Outreach",
-                "hasEmail": "mailto:genelab-outreach@lists.nasa.gov"
-            },
+            "landingPage": "https://data.nasa.gov/d/84ea-fpze",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "nasa_genelab_GLDS-129_84ea-fpze",
-            "description": "BACKGROUND: Ionizing radiation (IR) can be extremely harmful for human cells since an improper DNA-damage response (DDR) to IR can contribute to carcinogenesis initiation. Perturbations in DDR pathway can originate from alteration in the functionality of the microRNA-mediated gene regulation being microRNAs (miRNAs) small noncoding RNA that act as post-transcriptional regulators of gene expression. In this study we gained insight into the role of miRNAs in the regulation of DDR to IR under microgravity a condition of weightlessness experienced by astronauts during space missions which could have a synergistic action on cells increasing the risk of radiation exposure. METHODOLOGY/PRINCIPAL FINDINGS: We analyzed miRNA expression profile of human peripheral blood lymphocytes (PBL) incubated for 4 and 24 h in normal gravity (1 g) and in modeled microgravity (MMG) during the repair time after irradiation with 0.2 and 2Gy of gamma-rays. Our results show that MMG alters miRNA expression signature of irradiated PBL by decreasing the number of radio-responsive miRNAs. Moreover let-7i* miR-7 miR-7-1* miR-27a miR-144 miR-200a miR-598 miR-650 are deregulated by the combined action of radiation and MMG. Integrated analyses of miRNA and mRNA expression profiles carried out on PBL of the same donors identified significant miRNA-mRNA anti-correlations of DDR pathway. Gene Ontology analysis reports that the biological category of Response to DNA damage is enriched when PBL are incubated in 1 g but not in MMG. Moreover some anti-correlated genes of p53-pathway show a different expression level between 1 g and MMG. Functional validation assays using luciferase reporter constructs confirmed miRNA-mRNA interactions derived from target prediction analyses. CONCLUSIONS/SIGNIFICANCE: On the whole by integrating the transcriptome and microRNome we provide evidence that modeled microgravity can affects the DNA-damage response to IR in human PBL. Overall Design: Gene expression signature was defined in PBL irradiated with gamma-rays (2.0 Gy) and incubated in modeled microgravity (mmg) and in parallel ground conditions (1g) for 24h. Five independent experiments were performed for each donor to address which mRNAs were regulated on IR stress. The level of each transcript was represented as Log2.",
-            "title": "Gene expression profiling of PBL in response to ionising radiation and modeled microgravity",
-            "programCode": [
-                "026:005"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-129",
-                    "description": "GeneLab Study Page",
-                    "@type": "dcat:Distribution",
-                    "title": "Gene expression profiling of PBL in response to ionising radiation and modeled microgravity"
-                }
-            ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "Gene expression profiling of PBL in response to ionising radiation and modeled microgravity"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://c3.nasa.gov/dashlink/resources/717/",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2013-05-07",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
-            "keyword": [
-                "dashlink",
-                "ames",
-                "nasa"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Adam Sweet",
                 "hasEmail": "mailto:adam.sweet@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Dashlink"
-            },
-            "identifier": "DASHLINK_717",
             "description": "The sample scenarios provided here are competition scenarios from previous DXC competitions. They are identical to the competition data associated with previous years' projects, but also listed here for convenience. The zip files have a spreadsheet that lists the scenarios and relevant fault information. Each scenario is provided in three formats: tab-delimited .txt file, Matlab .mat file, and tab-delimited .scn file. The different formats are provided for your convenience; they have the same data. The scenario (.scn) files are the format read by the DXC framework. See the system catalogs and schematics for additional information.",
-            "title": "DXC'13 Industrial Track Sample Data",
-            "programCode": [
-                "026:029"
-            ],
             "distribution": [
                 {
-                    "mediaType": "application/zip",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/dxc13_sample_dxc11_comp_dp1_20110819.zip",
-                    "description": "DXC'13 Diagnostic Problem I Sample Data (Competition Data from DXC'11)",
                     "@type": "dcat:Distribution",
+                    "description": "DXC'13 Diagnostic Problem I Sample Data (Competition Data from DXC'11)",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/dxc13_sample_dxc11_comp_dp1_20110819.zip",
+                    "mediaType": "application/zip",
                     "title": "dxc13_sample_dxc11_comp_dp1_20110819.zip"
                 },
                 {
-                    "mediaType": "application/zip",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/dxc13_sample_dxc10_comp_dp2_20101105.zip",
-                    "description": "DXC'13 Diagnostic Problem 2 Sample Data (Competition Data from DXC'10)",
                     "@type": "dcat:Distribution",
+                    "description": "DXC'13 Diagnostic Problem 2 Sample Data (Competition Data from DXC'10)",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/dxc13_sample_dxc10_comp_dp2_20101105.zip",
+                    "mediaType": "application/zip",
                     "title": "dxc13_sample_dxc10_comp_dp2_20101105.zip"
                 }
             ],
-            "accrualPeriodicity": "irregular"
+            "identifier": "DASHLINK_717",
+            "issued": "2013-05-07",
+            "keyword": [
+                "dashlink",
+                "ames",
+                "nasa"
+            ],
+            "landingPage": "https://c3.nasa.gov/dashlink/resources/717/",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:029"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Dashlink"
+            },
+            "title": "DXC'13 Industrial Track Sample Data"
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
+            "description": "CFD Validation of Synthetic Jets and Turbulent Separation Control. This web page provides data from experiments that may be useful for the validation of turbulence models. This resource is expected to grow gradually over time. All data herein arepublicly available.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://cfdval2004.larc.nasa.gov/Presentations/case1figsonly.pdf",
+                    "mediaType": "application/pdf"
+                }
             ],
+            "identifier": "NASA-848__2",
+            "issued": "2018-06-25",
             "keyword": [
                 "experiment",
                 "turbulence",
@@ -340726,75 +340735,44 @@
                 "validation",
                 "control"
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
-            "identifier": "NASA-848__2",
-            "description": "CFD Validation of Synthetic Jets and Turbulent Separation Control. This web page provides data from experiments that may be useful for the validation of turbulence models. This resource is expected to grow gradually over time. All data herein arepublicly available.",
-            "title": "Turbulence Models: Data from Other Experiments: CFD Validation of Synthetic Jets and Turbulent Separation Control",
-            "programCode": [
-                "026:023"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://cfdval2004.larc.nasa.gov/Presentations/case1figsonly.pdf",
-                    "mediaType": "application/pdf"
-                }
+            "references": [
+                "http://turbmodels.larc.nasa.gov/index.html"
             ],
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Aerospace"
-            ]
+            ],
+            "title": "Turbulence Models: Data from Other Experiments: CFD Validation of Synthetic Jets and Turbulent Separation Control"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/MEASURES/WVCC/DATA211",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Eric Fetzer, Qing Yue, Gerald Manipon, and Likun Wang. 2022-04-30. SNPP_CrIS_VIIRS750m_IND. Version 1. SNPP CrIS-VIIRS 750-m Matchup Indexes V1. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/MEASURES/WVCC/DATA211. https://disc.gsfc.nasa.gov/datacollection/SNPP_CrIS_VIIRS750m_IND_1.html. Digital Science Data.",
-            "issued": "2022-04-12",
-            "temporal": "2015-01-01T00:00:00Z/2023-03-01T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-04-12",
-            "keyword": [
-                "atmosphere",
-                "earth science",
-                "clouds"
-            ],
-            "data-presentation-form": "Digital Science Data",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "GERALD MANIPON",
                 "hasEmail": "mailto:Geraldjohn.M.Manipon@jpl.nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
-            "identifier": "C2278117672-GES_DISC",
-            "description": "This dataset includes SNPP VIIRS-CrIS collocation index product, within the framework of the Multidecadal Satellite Record of Water Vapor, Temperature, and Clouds (PI: Eric Fetzer) funded by NASA\u2019s Making Earth System Data Records for Use in Research Environments (MEaSUREs) Program, 2017. The dataset is built upon work by Wang et al. (doi: 10.3390/rs8010076) and Yue (doi:10.5194/amt-15-2099-2022).\n\nThe short name for this collections is SNPP_CrIS_VIIRS750m_IND",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "SNPP_CrIS_VIIRS750m_IND",
             "creator": "Eric Fetzer, Qing Yue, Gerald Manipon, and Likun Wang",
-            "title": "SNPP CrIS-VIIRS 750-m Matchup Indexes V1 (SNPP_CrIS_VIIRS750m_IND) at GES_DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/MEaSUREs/Fetzer/AIRS_MLS_H2O.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "data-presentation-form": "Digital Science Data",
+            "description": "This dataset includes SNPP VIIRS-CrIS collocation index product, within the framework of the Multidecadal Satellite Record of Water Vapor, Temperature, and Clouds (PI: Eric Fetzer) funded by NASA\u2019s Making Earth System Data Records for Use in Research Environments (MEaSUREs) Program, 2017. The dataset is built upon work by Wang et al. (doi: 10.3390/rs8010076) and Yue (doi:10.5194/amt-15-2099-2022).\n\nThe short name for this collections is SNPP_CrIS_VIIRS750m_IND",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMEASURES%2FWVCC%2FDATA211",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMEASURES%2FWVCC%2FDATA211",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
@@ -340804,10 +340782,10 @@
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/SNPP_CrIS_VIIRS750m_IND_1.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/SNPP_CrIS_VIIRS750m_IND_1.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
@@ -340817,10 +340795,10 @@
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=SNPP_CrIS_VIIRS750m_IND",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=SNPP_CrIS_VIIRS750m_IND",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
@@ -340836,438 +340814,442 @@
                     "title": "View this dataset's user's guide"
                 }
             ],
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/MEaSUREs/Fetzer/AIRS_MLS_H2O.jpg",
+            "identifier": "C2278117672-GES_DISC",
+            "issued": "2022-04-12",
+            "keyword": [
+                "atmosphere",
+                "earth science",
+                "clouds"
+            ],
+            "landingPage": "https://doi.org/10.5067/MEASURES/WVCC/DATA211",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2022-04-12",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
+            },
+            "release-place": "Greenbelt, MD, USA",
+            "series-name": "SNPP_CrIS_VIIRS750m_IND",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2015-01-01T00:00:00Z/2023-03-01T00:00:00Z",
             "theme": [
                 "MEaSUREs",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "SNPP CrIS-VIIRS 750-m Matchup Indexes V1 (SNPP_CrIS_VIIRS750m_IND) at GES_DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/MODIS/MCD43D67.061",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Crystal Schaaf, Zhuosen Wang\r\n. 2021-02-22. MODIS/Terra+Aqua BRDF/Albedo Nadir BRDF-Adjusted Ref Band6 Daily L3 Global 30ArcSec CMG V061. Sioux Falls, South Dakota, USA. Archived by National Aeronautics and Space Administration, U.S. Government, NASA EOSDIS Land Processes Distributed Active Archive Center. https://doi.org/10.5067/MODIS/MCD43D67.061. https://doi.org/10.5067/MODIS/MCD43D67.061.  The DOI landing page provides citations in APA and Chicago styles..",
-            "issued": "2021-02-22",
-            "temporal": "2000-02-16T00:00:00Z/2024-05-20T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2021-02-22",
-            "keyword": [
-                "ngda",
-                "earth science",
-                "surface radiative properties",
-                "national geospatial data asset",
-                "land surface"
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
-            "identifier": "C2540275748-LPCLOUD",
-            "description": "The MCD43D67 Version 6.1 Bidirectional Reflectance Distribution Function and Albedo (BRDF/Albedo) Nadir BRDF-Adjusted Reflectance (NBAR) dataset is produced daily using 16 days of Terra and Aqua Moderate Resolution Imaging Spectroradiometer (MODIS) data at 30 arc second (1,000 meter (m)) resolution. Data are temporally weighted to the ninth day which is reflected in the Julian date in the file name. This Climate Modeling Grid (CMG) product covers the entire globe for use in climate simulation models. Due to the large file size, each MCD43D product contains just one data layer. \r\n\r\nMCD43D62 through MCD43D68 are the NBAR products of the MCD43D BRDF/Albedo product suite for MODIS bands 1 through 7. The NBAR algorithm removes view angle effects from directional reflectances to model the values as if they were collected from a nadir view at local solar noon.\r\n\r\nMCD43D67 is the NBAR for MODIS band 6. \r\n\r\nImprovements/Changes from Previous Versions\r\n\r\n* The Version 6.1 Level-1B (L1B) products have been improved by undergoing various calibration changes that include: changes to the response-versus-scan angle (RVS) approach that affects reflectance bands for Aqua and Terra MODIS, corrections to adjust for the optical crosstalk in Terra MODIS infrared (IR) bands, and corrections to the Terra MODIS forward look-up table (LUT) update for the period 2012 - 2017.\r\n* A polarization correction has been applied to the L1B Reflective Solar Bands (RSB).",
-            "release-place": "Sioux Falls, South Dakota, USA",
             "creator": "Crystal Schaaf, Zhuosen Wang",
-            "title": "MODIS/Terra+Aqua BRDF/Albedo Nadir BRDF-Adjusted Ref Band6 Daily L3 Global 30ArcSec CMG V061",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The MCD43D67 Version 6.1 Bidirectional Reflectance Distribution Function and Albedo (BRDF/Albedo) Nadir BRDF-Adjusted Reflectance (NBAR) dataset is produced daily using 16 days of Terra and Aqua Moderate Resolution Imaging Spectroradiometer (MODIS) data at 30 arc second (1,000 meter (m)) resolution. Data are temporally weighted to the ninth day which is reflected in the Julian date in the file name. This Climate Modeling Grid (CMG) product covers the entire globe for use in climate simulation models. Due to the large file size, each MCD43D product contains just one data layer. \r\n\r\nMCD43D62 through MCD43D68 are the NBAR products of the MCD43D BRDF/Albedo product suite for MODIS bands 1 through 7. The NBAR algorithm removes view angle effects from directional reflectances to model the values as if they were collected from a nadir view at local solar noon.\r\n\r\nMCD43D67 is the NBAR for MODIS band 6. \r\n\r\nImprovements/Changes from Previous Versions\r\n\r\n* The Version 6.1 Level-1B (L1B) products have been improved by undergoing various calibration changes that include: changes to the response-versus-scan angle (RVS) approach that affects reflectance bands for Aqua and Terra MODIS, corrections to adjust for the optical crosstalk in Terra MODIS infrared (IR) bands, and corrections to the Terra MODIS forward look-up table (LUT) update for the period 2012 - 2017.\r\n* A polarization correction has been applied to the L1B Reflective Solar Bands (RSB).",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMODIS%2FMCD43D67.061",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMODIS%2FMCD43D67.061",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "application/x-hdf",
-                    "downloadURL": "https://e4ftl01.cr.usgs.gov/MOTA/MCD43D67.061/",
-                    "description": "LP DAAC Data Pool provides direct access to available products via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "LP DAAC Data Pool provides direct access to available products via HTTPS.",
+                    "downloadURL": "https://e4ftl01.cr.usgs.gov/MOTA/MCD43D67.061/",
+                    "mediaType": "application/x-hdf",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "application/x-hdf",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=C2540275748-LPCLOUD",
-                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=C2540275748-LPCLOUD",
+                    "mediaType": "application/x-hdf",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/MODIS/MCD43D67.061",
-                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
+                    "downloadURL": "https://doi.org/10.5067/MODIS/MCD43D67.061",
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
-                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/filespec/MODIS/6/MCD43D67",
-                    "description": "The File Specification provides a description of the product file including Scientific Data Sets and their attributes.",
                     "@type": "dcat:Distribution",
+                    "description": "The File Specification provides a description of the product file including Scientific Data Sets and their attributes.",
+                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/filespec/MODIS/6/MCD43D67",
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
-                    "downloadURL": "https://opendap.cr.usgs.gov/opendap/hyrax/DP137/MOTA/MCD43D67.061/contents.html",
-                    "description": "Access data via Open-source Project for a Network Data Access Protocol",
                     "@type": "dcat:Distribution",
+                    "description": "Access data via Open-source Project for a Network Data Access Protocol",
+                    "downloadURL": "https://opendap.cr.usgs.gov/opendap/hyrax/DP137/MOTA/MCD43D67.061/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 }
             ],
+            "identifier": "C2540275748-LPCLOUD",
+            "issued": "2021-02-22",
+            "keyword": [
+                "ngda",
+                "earth science",
+                "surface radiative properties",
+                "national geospatial data asset",
+                "land surface"
+            ],
+            "landingPage": "https://doi.org/10.5067/MODIS/MCD43D67.061",
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
+            "title": "MODIS/Terra+Aqua BRDF/Albedo Nadir BRDF-Adjusted Ref Band6 Daily L3 Global 30ArcSec CMG V061"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MSL-M-APXS-4%2F5-RDR-V1.0",
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
+            "description": "The MSL APXS RDR data set contains calibrated spectra and oxide weight percent data derived from observations of the APXS instrument aboard the Mars Science Laboratory rover. Two types of products are included: summed X-ray spectra in counts as a function of energy, and abundance data for a set of standard elements and oxides, derived from the summed spectra. Both product types are given as ASCII text files in comma-separated-value (CSV) format, suitable for reading with spreadsheet software.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.msl-m-apxs-4-5-rdr-v1.0_84rc-7htk",
+            "issued": "2018-06-26",
+            "keyword": [
+                "mars science laboratory",
+                "mars"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MSL-M-APXS-4%2F5-RDR-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.msl-m-apxs-4-5-rdr-v1.0_84rc-7htk",
-            "description": "The MSL APXS RDR data set contains calibrated spectra and oxide weight percent data derived from observations of the APXS instrument aboard the Mars Science Laboratory rover. Two types of products are included: summed X-ray spectra in counts as a function of energy, and abundance data for a set of standard elements and oxides, derived from the summed spectra. Both product types are given as ASCII text files in comma-separated-value (CSV) format, suitable for reading with spreadsheet software.",
-            "title": "MSL MARS ALPHA PARTICLE X-RAY SPECTROMETER 4/5 RDR V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "MSL MARS ALPHA PARTICLE X-RAY SPECTROMETER 4/5 RDR V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.7927/10.7927/a4mb-4t86",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Requia, W. J., Y. Wei, A. Shtein, C. Hultquist, X. Xing, Q. Di, R. Silvern, J. T. Kelly, P. Koutrakis, L. J. Mickley, M. P. Sulprizio, H. Amini, L. Shi, and J. Schwartz. 2021-12-13. Daily 8-Hour Maximum and Annual O3 Concentrations for the Contiguous United States, 1-km Grids, v1 (2000 - 2016). Version 1.00. Palisades, NY. Archived by National Aeronautics and Space Administration, U.S. Government, NASA Socioeconomic Data and Applications Center (SEDAC). https://doi.org/10.7927/10.7927/a4mb-4t86. https://doi.org/10.7927/a4mb-4t86.",
-            "issued": "2021-12-20",
-            "temporal": "2000-01-01T00:00:00Z/2016-12-31T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2021-12-20",
-            "keyword": [
-                "earth science",
-                "atmospheric chemistry",
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
-            "identifier": "C2187535796-SEDAC",
-            "description": "The Daily 8-Hour Maximum and Annual O3 Concentrations for the Contiguous United States, 1-km Grids, v1 (2000 - 2016) data set contains estimates of ozone concentrations at a high resolution in space (1 km x 1 km grid cells) and time (daily) for the years 2000 to 2016. These predictions incorporated various predictor variables such as Ozone (O3) ground measurements from the U.S. Environmental Protection Agency (EPA) Air Quality System (AQS) monitoring data, land-use variables, meteorological variables, chemical transport models and remote sensing data, along with other data sources. After imputing missing data with machine learning algorithms, a geographically weighted ensemble model was applied that combined estimates from three types of machine learners (neural network, random forest, and gradient boosting). The annual predictions were computed by averaging the daily 8-hour maximum predictions in each year for each grid cell. The results demonstrate high overall model performance with a cross-validated R-squared value against daily observations of 0.90 and 0.86 for annual averages.",
-            "release-place": "Palisades, NY",
-            "graphic-preview-description": "Sample browse graphic of the data set.",
             "creator": "Requia, W. J., Y. Wei, A. Shtein, C. Hultquist, X. Xing, Q. Di, R. Silvern, J. T. Kelly, P. Koutrakis, L. J. Mickley, M. P. Sulprizio, H. Amini, L. Shi, and J. Schwartz",
-            "title": "Daily 8-Hour Maximum and Annual O3 Concentrations for the Contiguous United States, 1-km Grids, v1 (2000 - 2016)",
-            "graphic-preview-file": "https://sedac.ciesin.columbia.edu/downloads/maps/aqdh/aqdh-o3-concentrations-contiguous-us-1-km-2000-2016/sedac-logo.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The Daily 8-Hour Maximum and Annual O3 Concentrations for the Contiguous United States, 1-km Grids, v1 (2000 - 2016) data set contains estimates of ozone concentrations at a high resolution in space (1 km x 1 km grid cells) and time (daily) for the years 2000 to 2016. These predictions incorporated various predictor variables such as Ozone (O3) ground measurements from the U.S. Environmental Protection Agency (EPA) Air Quality System (AQS) monitoring data, land-use variables, meteorological variables, chemical transport models and remote sensing data, along with other data sources. After imputing missing data with machine learning algorithms, a geographically weighted ensemble model was applied that combined estimates from three types of machine learners (neural network, random forest, and gradient boosting). The annual predictions were computed by averaging the daily 8-hour maximum predictions in each year for each grid cell. The results demonstrate high overall model performance with a cross-validated R-squared value against daily observations of 0.90 and 0.86 for annual averages.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.7927%2F10.7927%2Fa4mb-4t86",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.7927%2F10.7927%2Fa4mb-4t86",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/downloads/maps/aqdh/aqdh-o3-concentrations-contiguous-us-1-km-2000-2016/sedac-logo.jpg",
-                    "description": "Sample browse graphic of the data set.",
                     "@type": "dcat:Distribution",
+                    "description": "Sample browse graphic of the data set.",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/downloads/maps/aqdh/aqdh-o3-concentrations-contiguous-us-1-km-2000-2016/sedac-logo.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/aqdh-o3-concentrations-contiguous-us-1-km-2000-2016/data-download",
-                    "description": "Data Download Page",
                     "@type": "dcat:Distribution",
+                    "description": "Data Download Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/aqdh-o3-concentrations-contiguous-us-1-km-2000-2016/data-download",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/aqdh-o3-concentrations-contiguous-us-1-km-2000-2016/docs",
-                    "description": "Documentation Page",
                     "@type": "dcat:Distribution",
+                    "description": "Documentation Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/aqdh-o3-concentrations-contiguous-us-1-km-2000-2016/docs",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/aqdh-o3-concentrations-contiguous-us-1-km-2000-2016",
-                    "description": "Data Set\u00a0Overview Page",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set\u00a0Overview Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/aqdh-o3-concentrations-contiguous-us-1-km-2000-2016",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "graphic-preview-description": "Sample browse graphic of the data set.",
+            "graphic-preview-file": "https://sedac.ciesin.columbia.edu/downloads/maps/aqdh/aqdh-o3-concentrations-contiguous-us-1-km-2000-2016/sedac-logo.jpg",
+            "identifier": "C2187535796-SEDAC",
+            "issued": "2021-12-20",
+            "keyword": [
+                "earth science",
+                "atmospheric chemistry",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.7927/10.7927/a4mb-4t86",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2021-12-20",
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
+            "title": "Daily 8-Hour Maximum and Annual O3 Concentrations for the Contiguous United States, 1-km Grids, v1 (2000 - 2016)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-PRL-0295-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the PRELANDING phase 2014-01-21 to 2014-11-18. It is a Global Gravity measurement at the comet 67P and covers the time 2014-09-15T06:17:02.000 to 2014-09-15T15:10:07.500.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-prl-0295-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-PRL-0295-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-prl-0295-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the PRELANDING phase 2014-01-21 to 2014-11-18. It is a Global Gravity measurement at the comet 67P and covers the time 2014-09-15T06:17:02.000 to 2014-09-15T15:10:07.500.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     PRELANDING 0295 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     PRELANDING 0295 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C2340494092-OB_DAAC.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/GSFC/SED/ESD/GCDC/OB.DAAC.",
-            "issued": "2022-09-14",
-            "temporal": "2012-01-02T00:00:00Z/2023-02-28T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-09-14",
-            "keyword": [
-                "earth science",
-                "ocean chemistry",
-                "ocean optics",
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
-            "identifier": "C2340494092-OB_DAAC",
             "description": "The Ocean Biology DAAC produces near real-time (quicklook) products using the best-available combination of ancillary data from meteorological and ozone data. As such, the inputs and the calibration used are less than optimal. Quicklook products provide a snapshot of the data during a short time period within a single orbit.",
-            "title": "Suomi-NPP VIIRS Global Mapped Chlorophyll (CHL) - NRT Data, version R2022.0",
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
-                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/data/10.5067/SNPP/VIIRS/L3M/CHL/2022",
-                    "description": "VIIRS-Suomi-NPP L3M Chlorophyll (CHL) - NRT Dataset Landing Page",
                     "@type": "dcat:Distribution",
+                    "description": "VIIRS-Suomi-NPP L3M Chlorophyll (CHL) - NRT Dataset Landing Page",
+                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/data/10.5067/SNPP/VIIRS/L3M/CHL/2022",
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
+            "identifier": "C2340494092-OB_DAAC",
+            "issued": "2022-09-14",
+            "keyword": [
+                "earth science",
+                "ocean chemistry",
+                "ocean optics",
+                "oceans"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C2340494092-OB_DAAC.html",
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
+            "title": "Suomi-NPP VIIRS Global Mapped Chlorophyll (CHL) - NRT Data, version R2022.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-COMPIL-5-BINMP-V1.0",
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
+            "description": "We present a data table giving basic physical and orbital parameters for known binary minor planets in the Solar System (and Pluto/Charon) based on published literature. For the purposes of this table, a binary minor planet is any mutually orbiting pair of minor planets in our Solar System, where a minor planet is any substantial body orbiting the Sun that is not a major planet, nor is bound to a major planet.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-compil-5-binmp-v1.0_84z7-uk9u",
+            "issued": "2021-05-21",
+            "keyword": [
+                "asteroid",
+                "support archives"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-COMPIL-5-BINMP-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-compil-5-binmp-v1.0_84z7-uk9u",
-            "description": "We present a data table giving basic physical and orbital parameters for known binary minor planets in the Solar System (and Pluto/Charon) based on published literature. For the purposes of this table, a binary minor planet is any mutually orbiting pair of minor planets in our Solar System, where a minor planet is any substantial body orbiting the Sun that is not a major planet, nor is bound to a major planet.",
-            "title": "BINARY MINOR PLANETS V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "BINARY MINOR PLANETS V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.nasa.gov/d/84zx-tdqg",
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
-                "wise",
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
-            "identifier": "NASA-0000038__17",
+            "describedBy": "http://planetarynames.wr.usgs.gov/Page/Website",
             "description": "Planetary nomenclature, like terrestrial nomenclature, is used to uniquely identify a feature on the surface of a planet or satellite so that the feature can be easily located, described, and discussed. This gazetteer contains detailed information about all names of topographic and albedo features on planets and satellites (and some planetary ring and ring-gap systems) that the International Astronomical Union (IAU) has named and approved from its founding in 1919 through the present time.",
-            "title": "Gazetteer of Planetary Nomenclature",
-            "programCode": [
-                "026:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -341275,21 +341257,48 @@
                     "mediaType": "application/zip"
                 }
             ],
-            "describedBy": "http://planetarynames.wr.usgs.gov/Page/Website",
-            "accrualPeriodicity": "irregular"
+            "identifier": "NASA-0000038__17",
+            "issued": "2018-06-25",
+            "keyword": [
+                "space science",
+                "wise",
+                "geography",
+                "nen"
+            ],
+            "landingPage": "https://data.nasa.gov/d/84zx-tdqg",
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
+            "description": "EPPS, GRNS, MAG, MASCS, MDIS, MLA, RSS, SPICE, XRS",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://pds.jpl.nasa.gov/tools/subscription_service/SS-20120308.shtml",
+                    "mediaType": "application/html"
+                }
             ],
+            "identifier": "NASA-514",
+            "issued": "2018-06-25",
             "keyword": [
                 "mla",
                 "mdis",
@@ -341302,119 +341311,112 @@
                 "grns",
                 "rss"
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
-            "identifier": "NASA-514",
-            "description": "EPPS, GRNS, MAG, MASCS, MDIS, MLA, RSS, SPICE, XRS",
-            "title": "PDS MESSENGER Data Release 7",
-            "programCode": [
-                "026:005"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://pds.jpl.nasa.gov/tools/subscription_service/SS-20120308.shtml",
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
+            "title": "PDS MESSENGER Data Release 7"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RPCLAP-2-PRL-MTP003-V2.0",
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
+            "description": "This data set contains\nEDITED data from Rosetta RPC-LAP, acquired during the PRELANDING\nMTP003 mission phase. Comet C-G/67P was the primary target.\nThis data set supersedes RO-C-RPCLAP-2-PRL-EDITED-V1.0 and is only\nMTP003 part of it.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rpclap-2-prl-mtp003-v2.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RPCLAP-2-PRL-MTP003-V2.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rpclap-2-prl-mtp003-v2.0",
-            "description": "This data set contains\nEDITED data from Rosetta RPC-LAP, acquired during the PRELANDING\nMTP003 mission phase. Comet C-G/67P was the primary target.\nThis data set supersedes RO-C-RPCLAP-2-PRL-EDITED-V1.0 and is only\nMTP003 part of it.",
-            "title": "ROSETTA-ORBITER 67P RPCLAP 2\nPRL MTP003 V2.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RPCLAP 2\nPRL MTP003 V2.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-5-ESC2-67P-M17-GEO-V1.0",
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
+            "description": "This CODMAC level 5 data set contains derived data products that include pixel-precise georeferencing information, acquired by the OSIRIS Narrow Angle Camera on the Rosetta spacecraft during the COMET ESCORT 2 mission phase, covering the period from 2015-06-02T23:25:00.000 to 2015-06-30T23:24:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V1.0 is the first version of this dataset: Lien corrected dataset after October 2018 PSA/PDS external peer review.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-5-esc2-67p-m17-geo-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-5-ESC2-67P-M17-GEO-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-5-esc2-67p-m17-geo-v1.0",
-            "description": "This CODMAC level 5 data set contains derived data products that include pixel-precise georeferencing information, acquired by the OSIRIS Narrow Angle Camera on the Rosetta spacecraft during the COMET ESCORT 2 mission phase, covering the period from 2015-06-02T23:25:00.000 to 2015-06-30T23:24:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V1.0 is the first version of this dataset: Lien corrected dataset after October 2018 PSA/PDS external peer review.",
-            "title": "ROSETTA-ORBITER 67P OSINAC 5 ESC2-MTP017 DDR-GEO V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P OSINAC 5 ESC2-MTP017 DDR-GEO V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=SDU-C-SPICE-6-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This data set includes the complete set of Stardust SPICE data files (``kernel files''), which can be accessed using SPICE software. The SPICE data contains geometric and other ancillary information needed to recover the full value of science instrument data. In particular SPICE kernels provide spacecraft and planetary ephemerides, instrument mounting alignments, spacecraft orientation, spacecraft sequences of events, and data needed for relevant time conversions.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.sdu-c-spice-6-v1.0_8576-yxbs",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "5535 annefrank",
                 "stardust",
@@ -341422,394 +341424,373 @@
                 "9p/tempel 1 (1867 g1)",
                 "next"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=SDU-C-SPICE-6-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.sdu-c-spice-6-v1.0_8576-yxbs",
-            "description": "This data set includes the complete set of Stardust SPICE data files (``kernel files''), which can be accessed using SPICE software. The SPICE data contains geometric and other ancillary information needed to recover the full value of science instrument data. In particular SPICE kernels provide spacecraft and planetary ephemerides, instrument mounting alignments, spacecraft orientation, spacecraft sequences of events, and data needed for relevant time conversions.",
-            "title": "STARDUST SPICE KERNELS V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "STARDUST SPICE KERNELS V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/NOAA20/CERES/FLUXBYCLDTYP-DAY_L3.001B",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2023-08-18. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/NOAA20/CERES/FLUXBYCLDTYP-DAY_L3.001B.",
-            "issued": "2023-08-16",
-            "temporal": "2018-05-01T00:00:00Z/2023-10-02T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-08-16",
-            "keyword": [
-                "earth science",
-                "clouds",
-                "atmosphere",
-                "atmospheric radiation"
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
-            "identifier": "C2765798375-LARC_ASDC",
             "description": "CER_FluxByCldTyp-Day_NOAA20-VIIRS_Edition1B is the Clouds and the Earth's Radiant Energy System (CERES) Monthly Daytime Mean Regionally Averaged NOAA-20 Top-of-Atmosphere (TOA) Fluxes and Associated Cloud Properties Stratified by Optical Depth and Effective Pressure Edition 1B data product. Data was collected using CERES Flight Model 6 (FM6) and Visible Infrared Inaging Radiometer Suite (VIIRS) on NOAA-20 Data collection for this product is ongoing. \r\n\r\nCER_FluxByCldTyp-Day_NOAA20-VIIRS_Edition1B provides the monthly mean daytime CERES fluxes and CERES-VIIRS cloud properties that have been spatially gridded into 1\u00b0 regions along both the NOAA-20 ground tracks where the TOA fluxes and cloud properties have been stratified by six cloud optical depth bins and seven cloud effective pressure layers. The CERES FluxByCldTyp-Day Edition1B product uses Single Scanner Footprint (SSF) Edition1B footprint data as input. Within each footprint, all 1-km pixel-level VIIRS-retrieved cloud properties are stratified into three possible sub-footprint components: two cloud layers and a clear portion. For each sub-footprint component, the VIIRS channel radiances are converted to broadband (BB) radiances. The CERES angular directional models are then applied to obtain BB fluxes. Each of the CERES sub-footprint cloud layers and associated fluxes are assigned to one of the 42 cloud types, similarly to the stratification process in the CldTypHist product. FluxByCloudTyp is an hourly instantaneous gridded daytime-only product with a global extent. Each netCDF4 file covers a  month.\r\n\r\nCERES is a key component of the Earth Observing System (EOS) program. The CERES instruments provide radiometric measurements of the Earth's atmosphere from three broadband channels. The CERES missions are a follow-on to the successful Earth Radiation Budget Experiment (ERBE) mission. The first CERES instrument, the proto flight model (PFM), was launched on November 27, 1997, as part of the Tropical Rainfall Measuring Mission (TRMM). Two CERES instruments (FM1 and FM2) were launched into polar orbit onboard the Earth Observing System (EOS) flagship Terra on December 18, 1999. Two additional CERES instruments (FM3 and FM4) were launched onboard Earth Observing System (EOS) Aqua on May 4, 2002. The CERES FM5 instrument was launched onboard the Suomi National Polar-orbiting Partnership (NPP) satellite on October 28, 2011. The newest CERES instrument (FM6) was launched onboard the Joint Polar-Orbiting Satellite System 1 (JPSS-1) satellite, now called NOAA-20, on November 18, 2017.",
-            "title": "CERES Daily Daytime Mean Regionally Averaged NOAA-20 TOA Fluxes and Associated Cloud Properties Stratified by Optical Depth and Effective Pressure Edition1B",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FNOAA20%2FCERES%2FFLUXBYCLDTYP-DAY_L3.001B",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FNOAA20%2FCERES%2FFLUXBYCLDTYP-DAY_L3.001B",
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
-                    "downloadURL": "https://doi.org/10.5067/NOAA20/CERES/FLUXBYCLDTYP-DAY_L3.001B",
-                    "description": "DOI data set landing page for CER_FluxByCldTyp-Day_NOAA20-VIIRS_Edition1B",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for CER_FluxByCldTyp-Day_NOAA20-VIIRS_Edition1B",
+                    "downloadURL": "https://doi.org/10.5067/NOAA20/CERES/FLUXBYCLDTYP-DAY_L3.001B",
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
-                    "downloadURL": "https://earthobservatory.nasa.gov/features/DelicateBalance/balance2.php",
-                    "description": "NASA Earth Observeratory Article: A Delicate Balance: Signs of Change in the Tropics - New data sets were also used from NASA's Clouds and the Earth's Radiant Energy System (CERES) instruments that fly aboard the Tropical Rainfall Measuring...",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Earth Observeratory Article: A Delicate Balance: Signs of Change in the Tropics - New data sets were also used from NASA's Clouds and the Earth's Radiant Energy System (CERES) instruments that fly aboard the Tropical Rainfall Measuring...",
+                    "downloadURL": "https://earthobservatory.nasa.gov/features/DelicateBalance/balance2.php",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://earthobservatory.nasa.gov/images/2654/aqua-ceres-first-light",
-                    "description": "NASA Earth Observatory Article: Aqua CERES First Light: Image of the Day - The Clouds and the Earth's Radiant Energy System (CERES) instrument is one of six on board the Aqua satellite.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Earth Observatory Article: Aqua CERES First Light: Image of the Day - The Clouds and the Earth's Radiant Energy System (CERES) instrument is one of six on board the Aqua satellite.",
+                    "downloadURL": "https://earthobservatory.nasa.gov/images/2654/aqua-ceres-first-light",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://earthobservatory.nasa.gov/images/563/ceres-detects-earths-heat-and-energy",
-                    "description": "NASA Earth Observatory Article: CERES Detects Earth's Heat and Energy: Image of the Day - Clouds and the Earth's Radiant Energy System (CERES) monitors solar energy reflected from the Earth and heat energy emitted from the Earth.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Earth Observatory Article: CERES Detects Earth's Heat and Energy: Image of the Day - Clouds and the Earth's Radiant Energy System (CERES) monitors solar energy reflected from the Earth and heat energy emitted from the Earth.",
+                    "downloadURL": "https://earthobservatory.nasa.gov/images/563/ceres-detects-earths-heat-and-energy",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://earthobservatory.nasa.gov/images/535/ceres-first-light-images",
-                    "description": "NASA Earth Observatory Article: CERES First Light Images: Image of the Day - These two Terra instruments join a previous CERES scanner on the Tropical Rainfall Measuring Mission (TRMM) which was launched on November 27, 1997",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Earth Observatory Article: CERES First Light Images: Image of the Day - These two Terra instruments join a previous CERES scanner on the Tropical Rainfall Measuring Mission (TRMM) which was launched on November 27, 1997",
+                    "downloadURL": "https://earthobservatory.nasa.gov/images/535/ceres-first-light-images",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://earthobservatory.nasa.gov/images/36518/ceres-global-cloud-fraction",
-                    "description": "NASA Earth Observatory Article: CERES Global Cloud Fraction - Each map combines observations from the CERES sensors on NASA's Terra and Aqua satellites collected on December 27, 2008",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Earth Observatory Article: CERES Global Cloud Fraction - Each map combines observations from the CERES sensors on NASA's Terra and Aqua satellites collected on December 27, 2008",
+                    "downloadURL": "https://earthobservatory.nasa.gov/images/36518/ceres-global-cloud-fraction",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://earthobservatory.nasa.gov/features/Iris/iris3.php",
-                    "description": "NASA Earth Observatory Article: Does the Earth Have an Iris Analog - Sensors on the TRMM and Terra satellite missions routinely measure these cloud physical properties, which scientists will match in time and space with CERES.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Earth Observatory Article: Does the Earth Have an Iris Analog - Sensors on the TRMM and Terra satellite missions routinely measure these cloud physical properties, which scientists will match in time and space with CERES.",
+                    "downloadURL": "https://earthobservatory.nasa.gov/features/Iris/iris3.php",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://earthobservatory.nasa.gov/images/600/first-monthly-ceres-global-longwave-and-shortwave-radiation",
-                    "description": "NASA Earth Observatory Article: First Monthly CERES Global Longwave and Shortwave Radiation - These measurements were acquired by NASA's Clouds and the Earth's Radiant Energy System (CERES) sensors during March 2000.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Earth Observatory Article: First Monthly CERES Global Longwave and Shortwave Radiation - These measurements were acquired by NASA's Clouds and the Earth's Radiant Energy System (CERES) sensors during March 2000.",
+                    "downloadURL": "https://earthobservatory.nasa.gov/images/600/first-monthly-ceres-global-longwave-and-shortwave-radiation",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://earthobservatory.nasa.gov/global-maps/CERES_NETFLUX_M",
-                    "description": "NASA Earth Observatory Article: Net Radiation - The measurements were made by the Clouds and the Earth's Radiant Energy System (CERES) sensors on NASA's Terra and Aqua satellites.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Earth Observatory Article: Net Radiation - The measurements were made by the Clouds and the Earth's Radiant Energy System (CERES) sensors on NASA's Terra and Aqua satellites.",
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
-                    "description": "NASA Earth Observatory Article: Terra Spacecraft Fact Sheet - Clouds and the Earth's Radiant Energy System (CERES) CERES will measure the Earth's energy balance\u2014comparing the amount of energy from the sun that reaches the Earth's surface vs. the amount of heat energy emitted by the Earth and its atmosphere.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Earth Observatory Article: Terra Spacecraft Fact Sheet - Clouds and the Earth's Radiant Energy System (CERES) CERES will measure the Earth's energy balance\u2014comparing the amount of energy from the sun that reaches the Earth's surface vs. the amount of heat energy emitted by the Earth and its atmosphere.",
+                    "downloadURL": "https://earthobservatory.nasa.gov/features/AM1/terra_animations.php",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://earthobservatory.nasa.gov/images/84930/the-arctic-is-absorbing-more-sunlight",
-                    "description": "NASA Earth Observatory Article: The Arctic Is Absorbing More Sunlight - The radiation measurements were made by NASA's Clouds and the Earth's Radiant Energy System (CERES) instruments which fly on multiple satellites.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Earth Observatory Article: The Arctic Is Absorbing More Sunlight - The radiation measurements were made by NASA's Clouds and the Earth's Radiant Energy System (CERES) instruments which fly on multiple satellites.",
+                    "downloadURL": "https://earthobservatory.nasa.gov/images/84930/the-arctic-is-absorbing-more-sunlight",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://earthobservatory.nasa.gov/features/Water/page4.php",
-                    "description": "NASA Earth Observatory Article: The Water Cycle - MODIS, CERES, and AIRS all collect data relevant to the study of clouds.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Earth Observatory Article: The Water Cycle - MODIS, CERES, and AIRS all collect data relevant to the study of clouds.",
+                    "downloadURL": "https://earthobservatory.nasa.gov/features/Water/page4.php",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://earthobservatory.nasa.gov/images/2984/tropical-cloud-systems-and-ceres",
-                    "description": "NASA Earth Observatory Article: Tropical Cloud Systems and CERES: Image of the Day - CERES detects the amount of outgoing heat and reflected sunlight leaving the planet.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Earth Observatory Article: Tropical Cloud Systems and CERES: Image of the Day - CERES detects the amount of outgoing heat and reflected sunlight leaving the planet.",
+                    "downloadURL": "https://earthobservatory.nasa.gov/images/2984/tropical-cloud-systems-and-ceres",
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
-                    "downloadURL": "https://ceres.larc.nasa.gov/documents/DQ_summaries/CERES_FluxByCldTyp_Ed4A_DQS_V2.pdf",
-                    "description": "Quality Summary: CERES_FluxByCldTyp-Day/Month_Ed1B",
                     "@type": "dcat:Distribution",
+                    "description": "Quality Summary: CERES_FluxByCldTyp-Day/Month_Ed1B",
+                    "downloadURL": "https://ceres.larc.nasa.gov/documents/DQ_summaries/CERES_FluxByCldTyp_Ed4A_DQS_V2.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's product quality assessment"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2765798375-LARC_ASDC",
-                    "description": "Earthdata Search for CER_FluxByCldTyp-Day_NOAA20-VIIRS_Edition1B (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for CER_FluxByCldTyp-Day_NOAA20-VIIRS_Edition1B (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2765798375-LARC_ASDC",
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
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ceres-tool.larc.nasa.gov/ord-tool/jsp/FluxByCldTypSelection.jsp",
-                    "description": "CERES Subsetting and Browsing Tool",
                     "@type": "dcat:Distribution",
+                    "description": "CERES Subsetting and Browsing Tool",
+                    "downloadURL": "https://ceres-tool.larc.nasa.gov/ord-tool/jsp/FluxByCldTypSelection.jsp",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through the CERES Ordering Tool"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/CERES/FluxByCldTyp-Day/NOAA20-VIIRS_Edition1B/",
-                    "description": "ASDC Direct Data Download for CER_FluxByCldTyp-Day_NOAA20-VIIRS_Edition1B",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for CER_FluxByCldTyp-Day_NOAA20-VIIRS_Edition1B",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/CERES/FluxByCldTyp-Day/NOAA20-VIIRS_Edition1B/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/CERES/FluxByCldTyp-Day/NOAA20-VIIRS_Edition1B/contents.html",
-                    "description": "OPeNDAP data access for CER_FluxByCldTyp-Day_NOAA20-VIIRS_Edition1B",
                     "@type": "dcat:Distribution",
+                    "description": "OPeNDAP data access for CER_FluxByCldTyp-Day_NOAA20-VIIRS_Edition1B",
+                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/CERES/FluxByCldTyp-Day/NOAA20-VIIRS_Edition1B/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 }
             ],
+            "identifier": "C2765798375-LARC_ASDC",
+            "issued": "2023-08-16",
+            "keyword": [
+                "earth science",
+                "clouds",
+                "atmosphere",
+                "atmospheric radiation"
+            ],
+            "landingPage": "https://doi.org/10.5067/NOAA20/CERES/FLUXBYCLDTYP-DAY_L3.001B",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2023-08-16",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/LARC/SD/ASDC"
+            },
             "spatial": "<?xml version=\"1.0\" encoding=\"UTF-8\"?><gml:Polygon xmlns:gml=\"http://www.opengis.net/gml/3.2\" srsName=\"EPSG:9825\"><gml:outerBoundaryIs><gml:LinearRing><gml:posList>-90.0 -180.0 -90.0 180.0 90.0 180.0 90.0 -180.0 -90.0 -180.0</gml:posList></gml:LinearRing></gml:outerBoundaryIs><gml:innerBoundaryIs></gml:innerBoundaryIs></gml:Polygon>",
+            "temporal": "2018-05-01T00:00:00Z/2023-10-02T00:00:00Z",
             "theme": [
                 "CERES",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "CERES Daily Daytime Mean Regionally Averaged NOAA-20 TOA Fluxes and Associated Cloud Properties Stratified by Optical Depth and Effective Pressure Edition1B"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/GloSSAC-L3-V1.1",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2017-05-04. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/GloSSAC-L3-V1.1. https://eosweb.larc.nasa.gov/project/glossac/glossac_table.",
-            "issued": "2017-05-04",
-            "temporal": "1979-01-01T00:00:00Z/2016-12-31T23:59:59Z",
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
-            "identifier": "C1544296224-LARC_ASDC",
             "description": "The Global Space-based Stratospheric Aerosol Climatology, or GloSSAC, is a 38-year climatology of stratospheric aerosol properties focused on extinction coefficient measurements by the Stratospheric Aerosol and Gas Experiment (SAGE) series of instruments through mid-2005 and on the Optical Spectrograph and InfraRed Imager System (OSIRIS) and the Cloud-Aerosol Lidar and Infrared Pathfinder Satellite Observation (CALIPSO) data thereafter. Data from other space instruments and from ground-based, air and balloon borne instruments to fill in key gaps in the data set. The end result is a global and gap-free data set focused on aerosol extinction coefficient at 525 and 1020 nm and other parameters on an \u2018as available\u2019 basis.",
-            "title": "Global Space-based Stratospheric Aerosol Climatology Version 1.1",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGloSSAC-L3-V1.1",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGloSSAC-L3-V1.1",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
@@ -341861,338 +341842,359 @@
                     "title": "View this dataset's how-to documentation"
                 }
             ],
+            "identifier": "C1544296224-LARC_ASDC",
+            "issued": "2017-05-04",
+            "keyword": [
+                "atmosphere",
+                "earth science",
+                "aerosols"
+            ],
+            "landingPage": "https://doi.org/10.5067/GloSSAC-L3-V1.1",
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
             "spatial": "180.0 80.0 180.0 80.0",
+            "temporal": "1979-01-01T00:00:00Z/2016-12-31T23:59:59Z",
             "theme": [
                 "GloSSAC",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Global Space-based Stratospheric Aerosol Climatology Version 1.1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/SeaBASS/CUSTARD/DATA001",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/GSFC/SED/ESD/GCDC/OB.DAAC. https://doi.org/10.5067/SeaBASS/CUSTARD/DATA001.",
-            "issued": "2019-12-03",
-            "temporal": "2019-12-03T00:00:01Z/2020-01-23T00:00:01Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-23",
-            "keyword": [
-                "oceans",
-                "earth science",
-                "ocean chemistry",
-                "ocean optics",
-                "salinity/density",
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
-            "identifier": "C2795192628-OB_DAAC",
             "description": "The surface ocean is home to billions of microscopic plants called phytoplankton which produce organic matter in the surface ocean using sunlight and carbon dioxide. When they die many of them sink, taking this carbon into the deep ocean, where it may be stored for hundreds to thousands of years, which helps keep our climate the way it is today.In this project we will tackle this by making new observations in a remote region of the Southern Ocean using an exciting combination of robotic vehicles and sophisticated new sensors. We will make new observations of how much carbon the ocean takes up in this key motorway junction of the Southern Ocean. We will examine the processes that control the uptake of carbon and its fate, in particular how seasonal availability of nutrients can affect the make-up of the phytoplankton which changes the depth to which carbon sinks before being dissolved.",
-            "title": "Carbon Uptake and SeasonalTraitsin Antarctic Remineralisation Depth(CUSTARD)",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSeaBASS%2FCUSTARD%2FDATA001",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSeaBASS%2FCUSTARD%2FDATA001",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://seabass.gsfc.nasa.gov/experiment/CUSTARD/",
-                    "description": "Detailed information about the SeaBASS Experiment such as cruises, funding, and investigators",
                     "@type": "dcat:Distribution",
+                    "description": "Detailed information about the SeaBASS Experiment such as cruises, funding, and investigators",
+                    "downloadURL": "https://seabass.gsfc.nasa.gov/experiment/CUSTARD/",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 }
             ],
+            "identifier": "C2795192628-OB_DAAC",
+            "issued": "2019-12-03",
+            "keyword": [
+                "oceans",
+                "earth science",
+                "ocean chemistry",
+                "ocean optics",
+                "salinity/density",
+                "ocean temperature"
+            ],
+            "landingPage": "https://doi.org/10.5067/SeaBASS/CUSTARD/DATA001",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2020-01-23",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GCDC/OB.DAAC"
+            },
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2019-12-03T00:00:01Z/2020-01-23T00:00:01Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Carbon Uptake and SeasonalTraitsin Antarctic Remineralisation Depth(CUSTARD)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://techport.nasa.gov/view/10616",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2012-01-01",
-            "temporal": "2012-01-01T00:00:00Z/2014-01-01T00:00:00Z",
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
-                "active"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Douglas Hudgins",
                 "hasEmail": "mailto:douglas.m.hudgins@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Science Mission Directorate"
-            },
-            "identifier": "TECHPORT_10616",
             "description": "Phase-Induced Amplitude Apodization (PIAA) is a high performance coronagraphic technique well suited for direct imaging and\nspectroscopic characterization of potentially habitable Earth-like planets from space. It delivers high contrast images by performing a\nlossless geometric remapping of the telescope beam with two aspheric mirrors, and simultaneously offers nearly full throughput, full\nangular resolution of the telescope, small inner working angle, high contrast and low chromatism. While the early PIAA systems\n(which are currently undergoing testing at several facilities) were designed to deliver high contrast at 2 l/D, newer hybrid designs can\ntheoretically deliver on a point source a 1e-10 contrast down to 0.64 l/D inner working angle with full throughput, approaching limits\nimposed by fundamental principles. PIAA coronagraph designs offer nearly optimal coronagraphic solutions for a wide range of\ntelescope size and astrophysical goals, from debris disks and giant planet imaging with a small size (",
-            "title": "ADVANCES IN PUPIL REMAPPING (PIAA) CORONAGRAPHY: IMPROVING BANDWIDTH, THROUGHPUT AND INNER WORKING ANGLE Project",
-            "programCode": [
-                "026:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "http://techport.nasa.gov/xml-api/10616",
                     "mediaType": "application/xml"
                 }
-            ]
+            ],
+            "identifier": "TECHPORT_10616",
+            "issued": "2012-01-01",
+            "keyword": [
+                "project",
+                "active"
+            ],
+            "landingPage": "http://techport.nasa.gov/view/10616",
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
+            "temporal": "2012-01-01T00:00:00Z/2014-01-01T00:00:00Z",
+            "title": "ADVANCES IN PUPIL REMAPPING (PIAA) CORONAGRAPHY: IMPROVING BANDWIDTH, THROUGHPUT AND INNER WORKING ANGLE Project"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/VIIRS/VJ113A2.002",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Eric Vermote. 2023-07-19. VIIRS/JPSS1 Vegetation Indices 16-Day L3 Global 1km SIN Grid V002. Sioux Falls, South Dakota, USA. Archived by National Aeronautics and Space Administration, U.S. Government, NASA EOSDIS Land Processes Distributed Active Archive Center. https://doi.org/10.5067/VIIRS/VJ113A2.002. https://doi.org/10.5067/VIIRS/VJ113A2.002. This data set was provided by the NASA/NOAA NPP Project. The DOI landing page provides citations in APA and Chicago styles.\r\n.",
-            "issued": "2023-07-19",
-            "temporal": "2018-01-01T00:00:00Z/2024-06-03T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-19",
-            "keyword": [
-                "earth science",
-                "vegetation",
-                "biosphere"
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
-            "identifier": "C2519122898-LPCLOUD",
-            "description": "The NOAA-20 Visible Infrared Imaging Radiometer Suite (VIIRS) (https://lpdaac.usgs.gov/dataset_discovery/viirs) Vegetation Indices (VJ113A2) Version 2 data product provides vegetation indices by a process of selecting the best available pixel over a 16-day acquisition period at 1 kilometer (km) resolution. The VJ113 data products are designed after the Moderate Resolution Imaging Spectroradiometer (MODIS) Terra and Aqua Vegetation Indices product suite to promote the continuity of the Earth Observation System (EOS) mission.\r\n\r\nThe VJ113 algorithm process produces three vegetation indices: The Normalized Difference Vegetation Index (NDVI), the Enhanced Vegetation Index (EVI), and the Enhanced Vegetation Index-2 (EVI2). NDVI is one of the longest continual remotely sensed time series observations, using both the red and near-infrared (NIR) bands. EVI is a slightly different vegetation index that is more sensitive to canopy cover, while NDVI is more sensitive to chlorophyll. EVI2 is a reformation of the standard 3-band EVI, using the red band and NIR band. This reformation addresses arising issues when comparing VIIRS EVI to other EVI models that do not include a blue band. EVI2 will eventually become the standard EVI. \r\n\r\nAlong with the three Vegetation Indices layers, this product also includes layers for NIR reflectance; three shortwave infrared (SWIR) reflectance; red, blue, and green reflectance; composite day of year; pixel reliability; relative azimuth, view, and sun angles, and a quality layer. Two low resolution browse images are also available for each VJ113A2 product: EVI and NDVI.",
-            "release-place": "Sioux Falls, South Dakota, USA",
-            "graphic-preview-description": "Browse image for Earthdata Search",
             "creator": "Eric Vermote",
-            "title": "VIIRS/JPSS1 Vegetation Indices 16-Day L3 Global 1km SIN Grid V002",
-            "graphic-preview-file": "https://cmr.earthdata.nasa.gov/browse-scaler/browse_images/granules/G2732429371-LPCLOUD?h=85&w=85",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The NOAA-20 Visible Infrared Imaging Radiometer Suite (VIIRS) (https://lpdaac.usgs.gov/dataset_discovery/viirs) Vegetation Indices (VJ113A2) Version 2 data product provides vegetation indices by a process of selecting the best available pixel over a 16-day acquisition period at 1 kilometer (km) resolution. The VJ113 data products are designed after the Moderate Resolution Imaging Spectroradiometer (MODIS) Terra and Aqua Vegetation Indices product suite to promote the continuity of the Earth Observation System (EOS) mission.\r\n\r\nThe VJ113 algorithm process produces three vegetation indices: The Normalized Difference Vegetation Index (NDVI), the Enhanced Vegetation Index (EVI), and the Enhanced Vegetation Index-2 (EVI2). NDVI is one of the longest continual remotely sensed time series observations, using both the red and near-infrared (NIR) bands. EVI is a slightly different vegetation index that is more sensitive to canopy cover, while NDVI is more sensitive to chlorophyll. EVI2 is a reformation of the standard 3-band EVI, using the red band and NIR band. This reformation addresses arising issues when comparing VIIRS EVI to other EVI models that do not include a blue band. EVI2 will eventually become the standard EVI. \r\n\r\nAlong with the three Vegetation Indices layers, this product also includes layers for NIR reflectance; three shortwave infrared (SWIR) reflectance; red, blue, and green reflectance; composite day of year; pixel reliability; relative azimuth, view, and sun angles, and a quality layer. Two low resolution browse images are also available for each VJ113A2 product: EVI and NDVI.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FVIIRS%2FVJ113A2.002",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FVIIRS%2FVJ113A2.002",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "application/x-hdf",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=C2519122898-LPCLOUD",
-                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=C2519122898-LPCLOUD",
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
-                    "downloadURL": "https://doi.org/10.5067/VIIRS/VJ113A2.002",
-                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
+                    "downloadURL": "https://doi.org/10.5067/VIIRS/VJ113A2.002",
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
-                    "downloadURL": "https://lpdaac.usgs.gov/documents/1372/VNP13_User_Guide_ATBD_V2.1.2.pdf",
-                    "description": "The technical information in the User's Guide enables users to interpret and use the data products.",
                     "@type": "dcat:Distribution",
+                    "description": "The technical information in the User's Guide enables users to interpret and use the data products.",
+                    "downloadURL": "https://lpdaac.usgs.gov/documents/1372/VNP13_User_Guide_ATBD_V2.1.2.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://lpdaac.usgs.gov/documents/1372/VNP13_User_Guide_ATBD_V2.1.2.pdf",
-                    "description": "The ATBD provides physical theory and mathematical procedures for the calculations used to produce the data products.",
                     "@type": "dcat:Distribution",
+                    "description": "The ATBD provides physical theory and mathematical procedures for the calculations used to produce the data products.",
+                    "downloadURL": "https://lpdaac.usgs.gov/documents/1372/VNP13_User_Guide_ATBD_V2.1.2.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's algorithm theoretical basis document"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/filespec/VIIRS/2/VNP13A2",
-                    "description": "The File Specification provides a description of the product file including Scientific Data Sets and their attributes.",
                     "@type": "dcat:Distribution",
+                    "description": "The File Specification provides a description of the product file including Scientific Data Sets and their attributes.",
+                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/filespec/VIIRS/2/VNP13A2",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/browse-scaler/browse_images/granules/G2732429371-LPCLOUD?h=85&w=85",
-                    "description": "Browse image for Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse image for Earthdata Search",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/browse-scaler/browse_images/granules/G2732429371-LPCLOUD?h=85&w=85",
+                    "mediaType": "text/html",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://viirsland.gsfc.nasa.gov/Val/VI_Val.html",
-                    "description": "Validation at stage 1 has been achieved for the VIIRS Vegetation Index (VI) product suite.",
                     "@type": "dcat:Distribution",
+                    "description": "Validation at stage 1 has been achieved for the VIIRS Vegetation Index (VI) product suite.",
+                    "downloadURL": "https://viirsland.gsfc.nasa.gov/Val/VI_Val.html",
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
+            "graphic-preview-file": "https://cmr.earthdata.nasa.gov/browse-scaler/browse_images/granules/G2732429371-LPCLOUD?h=85&w=85",
+            "identifier": "C2519122898-LPCLOUD",
+            "issued": "2023-07-19",
+            "keyword": [
+                "earth science",
+                "vegetation",
+                "biosphere"
+            ],
+            "landingPage": "https://doi.org/10.5067/VIIRS/VJ113A2.002",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2023-07-19",
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
+            "title": "VIIRS/JPSS1 Vegetation Indices 16-Day L3 Global 1km SIN Grid V002"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/NOAA-21/VIIRS/L3B/KD/2022",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/GSFC/SED/ESD/GCDC/OB.DAAC. https://doi.org/10.5067/NOAA-21/VIIRS/L3B/KD/2022.",
-            "issued": "2023-04-04",
-            "temporal": "2022-11-10T00:00:00Z/2023-04-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-04-04",
-            "keyword": [
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
-            "identifier": "C2652675318-OB_DAAC",
             "description": "The Visible and Infrared Imager/Radiometer Suite (VIIRS) is a multi-disciplinary instrument that is being flown on the Joint Polar Satellite System (JPSS) series of spacecraft, including the Suomi National Polar-orbiting Partnership (S-NPP) that launched in October 2011.  JPSS is a multi-platform, multi-agency program that consolidates the polar orbiting spacecraft of NASA and the National Oceanic and Atmospheric Administration (NOAA).  S-NPP is the initial spacecraft in this series, and VIIRS is the successor to MODIS for Earth science data product generation.  VIIRS has 22 spectral bands ranging from 412 nm to 12 nm.  There are 16 moderate-resolution bands (750m at nadir), 5 image-resolution bands (375m), and one day-night band (DNB).",
-            "title": "NOAA-21 VIIRS Global Binned Diffuse Attenuation Coefficient for Downwelling Irradiance (KD) Data, version R2022.0",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FNOAA-21%2FVIIRS%2FL3B%2FKD%2F2022",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FNOAA-21%2FVIIRS%2FL3B%2FKD%2F2022",
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
-                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/data/10.5067/NOAA-21/VIIRS/L3B/KD/2022",
-                    "description": "VIIRS-NOAA-21 L3B Diffuse Attenuation Coefficient for Downwelling Irradiance (KD) Dataset Landing Page",
                     "@type": "dcat:Distribution",
+                    "description": "VIIRS-NOAA-21 L3B Diffuse Attenuation Coefficient for Downwelling Irradiance (KD) Dataset Landing Page",
+                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/data/10.5067/NOAA-21/VIIRS/L3B/KD/2022",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 }
             ],
+            "identifier": "C2652675318-OB_DAAC",
+            "issued": "2023-04-04",
+            "keyword": [
+                "oceans",
+                "ocean optics",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/NOAA-21/VIIRS/L3B/KD/2022",
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
+            "title": "NOAA-21 VIIRS Global Binned Diffuse Attenuation Coefficient for Downwelling Irradiance (KD) Data, version R2022.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-X-OSIWAC-2-CR4A-CRUISE4A-V1.4",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This data set contains images acquired by the OSIRIS Wide Angle Camera\nduring the CRUISE 4-1 mission phase",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-x-osiwac-2-cr4a-cruise4a-v1.4_85e8-ym8h",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "international rosetta mission",
                 "16 cyg b",
@@ -342202,292 +342204,272 @@
                 "dark",
                 "jupiter"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-X-OSIWAC-2-CR4A-CRUISE4A-V1.4",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-x-osiwac-2-cr4a-cruise4a-v1.4_85e8-ym8h",
-            "description": "This data set contains images acquired by the OSIRIS Wide Angle Camera\nduring the CRUISE 4-1 mission phase",
-            "title": "ROSETTA-ORBITER CRUISE 4-1 OSIWAC 2 EDR\n                                      V1.4",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER CRUISE 4-1 OSIWAC 2 EDR\n                                      V1.4"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1561",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Walker, X.J., B.M. Rogers, J.L. Baltzer, S.R. Cummings, N.J. Day, S.J. Goetz, J.F. Johnstone, M.R. Turetsky, and M.C. Mack. 2018. ABoVE: Wildfire Carbon Emissions and Burned Plot Characteristics, NWT, CA, 2014-2016. ORNL DAAC, Oak Ridge, Tennessee, USA. https://doi.org/10.3334/ORNLDAAC/1561",
-            "issued": "2018-07-30",
-            "temporal": "2014-07-02T00:00:00Z/2016-08-01T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-06-12",
-            "keyword": [
-                "agriculture",
-                "air quality",
-                "atmosphere",
-                "earth science",
-                "forest science",
-                "ecological dynamics",
-                "vegetation",
-                "biosphere",
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
-            "identifier": "C2111710292-ORNL_CLOUD",
             "description": "This dataset provides estimates of wildfire carbon emissions and uncertainties at 30-m resolution, and measurements collected at burned and unburned field plots from the 2014 wildfire sites near Yellowknife, Northwest Territories (NWT), Canada. Field data were collected at 211 burned plots in 2015 and include site characteristics, tree cover and species, basal area, delta normalized burn ratio (dNBR), plot characteristics, soil carbon, and carbon combusted. Data were collected at 36 unburned plots with characteristics similar to the burned plots in 2016. The emission estimates were derived from a statistical modeling approach based on measurements of carbon consumption at the 211 burned field plots located in seven independent burn scars. Estimates include uncertainty of field observations of aboveground and belowground combustion, as well as prediction uncertainty from a multiplicative regression model. To apply the model across all 2014 NWT fire perimeters, the final model covariates were re-gridded to a common 30-m grid defined by the Arctic Boreal and Vulnerability Experiment (ABoVE) Project. The regression model was then applied to burned pixels defined by a threshold of Landsat-derived differenced Normalized Burn Ratio (dNBR) within fire perimeters. Derived carbon emissions and uncertainty in g/m2 are provided for each 30-m grid cell. The modeled NWT domain encompasses 29 tiles within the ABoVE 30-m reference grid system.",
-            "graphic-preview-description": "Maps of the 2014 NWT fire complex showing a) estimated total combustion, b) uncertainty in total combustion, and details of landscape heterogeneity in c) combustion and d) uncertainty within one of the major fire scars.",
-            "title": "ABoVE: Wildfire Carbon Emissions and Burned Plot Characteristics, NWT, CA, 2014-2016",
-            "graphic-preview-file": "https://daac.ornl.gov/ABOVE/guides/Fire_Emissions_NWT_Fig1.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1561",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1561",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/above/Fire_Emissions_NWT/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/above/Fire_Emissions_NWT/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/ABOVE/guides/Fire_Emissions_NWT.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/ABOVE/guides/Fire_Emissions_NWT.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1561",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1561",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/Fire_Emissions_NWT/comp/Fire_Emissions_NWT.pdf",
-                    "description": "This is a PDF of this guide document",
                     "@type": "dcat:Distribution",
+                    "description": "This is a PDF of this guide document",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/Fire_Emissions_NWT/comp/Fire_Emissions_NWT.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://daac.ornl.gov/ABOVE/guides/Fire_Emissions_NWT_Fig1.png",
-                    "description": "Maps of the 2014 NWT fire complex showing a) estimated total combustion, b) uncertainty in total combustion, and details of landscape heterogeneity in c) combustion and d) uncertainty within one of the major fire scars.",
                     "@type": "dcat:Distribution",
+                    "description": "Maps of the 2014 NWT fire complex showing a) estimated total combustion, b) uncertainty in total combustion, and details of landscape heterogeneity in c) combustion and d) uncertainty within one of the major fire scars.",
+                    "downloadURL": "https://daac.ornl.gov/ABOVE/guides/Fire_Emissions_NWT_Fig1.png",
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
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://webmap.ornl.gov/wcsdown/dataset.jsp?ds_id=1561",
-                    "description": "Web Coverage Service for this collection.",
                     "@type": "dcat:Distribution",
+                    "description": "Web Coverage Service for this collection.",
+                    "downloadURL": "https://webmap.ornl.gov/wcsdown/dataset.jsp?ds_id=1561",
+                    "mediaType": "text/html",
                     "title": "Use Web Coverage Service (WCS) to download the dataset's data"
                 }
             ],
+            "graphic-preview-description": "Maps of the 2014 NWT fire complex showing a) estimated total combustion, b) uncertainty in total combustion, and details of landscape heterogeneity in c) combustion and d) uncertainty within one of the major fire scars.",
+            "graphic-preview-file": "https://daac.ornl.gov/ABOVE/guides/Fire_Emissions_NWT_Fig1.png",
+            "identifier": "C2111710292-ORNL_CLOUD",
+            "issued": "2018-07-30",
+            "keyword": [
+                "agriculture",
+                "air quality",
+                "atmosphere",
+                "earth science",
+                "forest science",
+                "ecological dynamics",
+                "vegetation",
+                "biosphere",
+                "land surface",
+                "soils"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1561",
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
             "spatial": "-136.13 56.25 -102.0 71.7",
+            "temporal": "2014-07-02T00:00:00Z/2016-08-01T23:59:59Z",
             "theme": [
                 "ABoVE",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "ABoVE: Wildfire Carbon Emissions and Burned Plot Characteristics, NWT, CA, 2014-2016"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/GHSIO-3CO01",
             "citation": "EUMETSAT/OSI SAF. 2017-03-28. SEVIRI Indian Ocean SST. Version 1.0. GHRSST Level 3C OSISAF Indian-Ocean sub-skin Sea Surface Temperature from SEVIRI on MSG . EUMETSAT Ocean and Sea Ice Satellite Application Facility, Lannion, France. Archived by National Aeronautics and Space Administration, U.S. Government, PO.DAAC. https://doi.org/10.5067/GHSIO-3CO01. https://www.osi-saf.org. EUMETSAT/OSI SAF, EUMETSAT Ocean and Sea Ice Satellite Application Facility, Meteo-France/CMS, Lannion, France, 2017-03-28, GHRSST Level 3C Indian-Ocean (IO) sub-skin Sea Surface Temperature from the Spinning Enhanced Visible and Infrared Imager (SEVIRI) on MSG1 in GDS2 format produced by OSISAF, www.osi-saf.org.",
-            "issued": "2017-07-19",
-            "temporal": "2017-03-28T13:30:00Z/2023-02-28T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2017-07-19",
-            "references": [
-                "http://www.osi-saf.org/lml/doc/osisaf_cdop3_ss1_atbd_geo_sst.pdf"
-            ],
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
-            "identifier": "C2036877550-POCLOUD",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/JPL/PODAAC"
-            },
-            "description": "This dataset is produced by the Ocean and Sea Ice Satellite Application Facility (OSI SAF) from the Spinning Enhanced Visible and InfraRed Imager (SEVIRI) instrument onboard the Meteosat Second Generation (MSG-1), Meteosat-8 satellite (launched on 28 August 2002).  The dataset covers the Indian Ocean region with latitude of 60S-60N and longitude of 101.5E-18.5W. Level-3C SST, in the NetCDF format recommended by Group for High Resolution Sea Surface Temperature (GHRSST), is identical to Level-2P GHRSST products, 3 refers to gridded products and C to the fact that hourly products result from compositing 15 minutes (MSG) or 30 minutes (GOES-E) data.\r\nThe European Organization for the Exploitation of Meteorological Satellites (EUMETSAT), OSI SAF is producing SST products in near real time from MSG/SEVIRI. SEVIRI level 1.5 data are acquired at Meteo-France/Centre de Meteorologie Spatiale (CMS) through the EUMETSAT/EUMETCAST system. SST is retrieved from the SEVIRI infrared channels (10.8 and 12.0 micrometer) using a multispectral algorithm. Atmospheric profiles of water vapor and temperature from a numerical weather prediction model, together with a radiatiave transfer model, are used to correct the multispectral algorithm for regional and seasonal biases due to changing atmospheric conditions. Every 15 minutes slot is processed at full satellite resolution. The operational products are then produced by remapping over a 0.05-degree regular grid (60S-60N and 135W-15W) SST fields obtained by aggregating all 15-minute SST data available in one-hour time, and the priority being given to the value the closest in time to the product nominal hour. The product format is compliant with the GHRSST Data Specification (GDS) version 2.",
-            "release-place": "EUMETSAT Ocean and Sea Ice Satellite Application Facility, Lannion, France",
-            "series-name": "SEVIRI Indian Ocean SST",
             "creator": "EUMETSAT/OSI SAF",
-            "title": "GHRSST Level 3C Indian-Ocean (IO) sub-skin Sea Surface Temperature from the Spinning Enhanced Visible and Infrared Imager (SEVIRI) on MSG in GDS2 format produced by OSISAF",
-            "graphic-preview-description": "Thumbnail",
-            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/SEVIRI_IO_SST-OSISAF-L3C-v1.0.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "This dataset is produced by the Ocean and Sea Ice Satellite Application Facility (OSI SAF) from the Spinning Enhanced Visible and InfraRed Imager (SEVIRI) instrument onboard the Meteosat Second Generation (MSG-1), Meteosat-8 satellite (launched on 28 August 2002).  The dataset covers the Indian Ocean region with latitude of 60S-60N and longitude of 101.5E-18.5W. Level-3C SST, in the NetCDF format recommended by Group for High Resolution Sea Surface Temperature (GHRSST), is identical to Level-2P GHRSST products, 3 refers to gridded products and C to the fact that hourly products result from compositing 15 minutes (MSG) or 30 minutes (GOES-E) data.\r\nThe European Organization for the Exploitation of Meteorological Satellites (EUMETSAT), OSI SAF is producing SST products in near real time from MSG/SEVIRI. SEVIRI level 1.5 data are acquired at Meteo-France/Centre de Meteorologie Spatiale (CMS) through the EUMETSAT/EUMETCAST system. SST is retrieved from the SEVIRI infrared channels (10.8 and 12.0 micrometer) using a multispectral algorithm. Atmospheric profiles of water vapor and temperature from a numerical weather prediction model, together with a radiatiave transfer model, are used to correct the multispectral algorithm for regional and seasonal biases due to changing atmospheric conditions. Every 15 minutes slot is processed at full satellite resolution. The operational products are then produced by remapping over a 0.05-degree regular grid (60S-60N and 135W-15W) SST fields obtained by aggregating all 15-minute SST data available in one-hour time, and the priority being given to the value the closest in time to the product nominal hour. The product format is compliant with the GHRSST Data Specification (GDS) version 2.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGHSIO-3CO01",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGHSIO-3CO01",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/SEVIRI_IO_SST-OSISAF-L3C-v1.0.jpg",
-                    "description": "Thumbnail",
                     "@type": "dcat:Distribution",
+                    "description": "Thumbnail",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/SEVIRI_IO_SST-OSISAF-L3C-v1.0.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "http://www.osi-saf.org/lml/doc/osisaf_cdop3_ss1_atbd_geo_sst.pdf",
-                    "description": "Algorithm Theoretical Basis Document",
                     "@type": "dcat:Distribution",
+                    "description": "Algorithm Theoretical Basis Document",
+                    "downloadURL": "http://www.osi-saf.org/lml/doc/osisaf_cdop3_ss1_atbd_geo_sst.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
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
-                    "downloadURL": "https://www.ghrsst.org",
-                    "description": "Description of the GHRSST Project",
                     "@type": "dcat:Distribution",
+                    "description": "Description of the GHRSST Project",
+                    "downloadURL": "https://www.ghrsst.org",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/ghrsst/open/data/GDS2/L3C/Indian-Ocean/SEVIRI_IO/OSISAF/docs/osisaf_cdop3_ss1_svr_meteosat08_io_sst.pdf",
-                    "description": "validation report",
                     "@type": "dcat:Distribution",
+                    "description": "validation report",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/ghrsst/open/data/GDS2/L3C/Indian-Ocean/SEVIRI_IO/OSISAF/docs/osisaf_cdop3_ss1_svr_meteosat08_io_sst.pdf",
+                    "mediaType": "application/pdf",
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
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2036877550-POCLOUD",
-                    "description": "HTTPS endpoint for data browse and download",
                     "@type": "dcat:Distribution",
+                    "description": "HTTPS endpoint for data browse and download",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2036877550-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2036877550-POCLOUD",
-                    "description": "Browse granule search results in Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse granule search results in Earthdata Search",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2036877550-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 }
             ],
+            "graphic-preview-description": "Thumbnail",
+            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/SEVIRI_IO_SST-OSISAF-L3C-v1.0.jpg",
+            "identifier": "C2036877550-POCLOUD",
+            "issued": "2017-07-19",
+            "keyword": [
+                "ocean temperature",
+                "oceans",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/GHSIO-3CO01",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2017-07-19",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/JPL/PODAAC"
+            },
+            "references": [
+                "http://www.osi-saf.org/lml/doc/osisaf_cdop3_ss1_atbd_geo_sst.pdf"
+            ],
+            "release-place": "EUMETSAT Ocean and Sea Ice Satellite Application Facility, Lannion, France",
+            "series-name": "SEVIRI Indian Ocean SST",
             "spatial": "-18.5 -60.0 101.5 60.0",
+            "temporal": "2017-03-28T13:30:00Z/2023-02-28T00:00:00Z",
             "theme": [
                 "GHRSST",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "GHRSST Level 3C Indian-Ocean (IO) sub-skin Sea Surface Temperature from the Spinning Enhanced Visible and Infrared Imager (SEVIRI) on MSG in GDS2 format produced by OSISAF"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.nasa.gov/d/85mn-8d4c",
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
-                "geography",
-                "nen",
-                "wise"
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
-            "identifier": "NASA-0000037__5",
+            "describedBy": "http://www.lpi.usra.edu/resources/gc/gcreadme.html",
             "description": "Planetary nomenclature, like terrestrial nomenclature, is used to uniquely identify a feature on the surface of a planet or satellite so that the feature can be easily located, described, and discussed. This gazetteer contains detailed information about all names of topographic and albedo features on planets and satellites (and some planetary ring and ring-gap systems) that the International Astronomical Union (IAU) has named and approved from its founding in 1919 through the present time.",
-            "title": "Gateway to Astronaut Photography of Earth",
-            "programCode": [
-                "026:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -342495,321 +342477,314 @@
                     "mediaType": "text/html"
                 }
             ],
-            "describedBy": "http://www.lpi.usra.edu/resources/gc/gcreadme.html",
-            "accrualPeriodicity": "irregular"
+            "identifier": "NASA-0000037__5",
+            "issued": "2018-06-25",
+            "keyword": [
+                "space science",
+                "geography",
+                "nen",
+                "wise"
+            ],
+            "landingPage": "https://data.nasa.gov/d/85mn-8d4c",
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
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C156141682-LARC.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "The data used in this study were produced by the MISR Science Team;processed/stored at the Langley DAAC;Product is the MISR Level 3 FIRSTLOOK Component Global Land Product covering a day's products;See ProductionDateTime for Published date.",
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
-            "identifier": "C156141682-LARC",
             "description": "This file contains the MISR Level 3 FIRSTLOOK Component Global Land Product covering a day",
-            "graphic-preview-description": "ASDC List of MISR Imagery and Articles",
-            "title": "MISR Level 3 FIRSTLOOK Component Global Land Product covering a day V002",
-            "graphic-preview-file": "https://asdc.larc.nasa.gov/documents/misr/imagery.html",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/search/concepts/C156141682-LARC.html",
-                    "description": "View this dataset on the CMR (Common Metadata Repository)",
                     "@type": "dcat:Distribution",
+                    "description": "View this dataset on the CMR (Common Metadata Repository)",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/search/concepts/C156141682-LARC.html",
+                    "mediaType": "text/html",
                     "title": "CMR"
                 }
             ],
+            "graphic-preview-description": "ASDC List of MISR Imagery and Articles",
+            "graphic-preview-file": "https://asdc.larc.nasa.gov/documents/misr/imagery.html",
+            "identifier": "C156141682-LARC",
+            "issued": "2007-07-30",
+            "keyword": [
+                "nasa"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C156141682-LARC.html",
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
+            "title": "MISR Level 3 FIRSTLOOK Component Global Land Product covering a day V002"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ASDC/AJAX_O3",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2021-11-04. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/ASDC/AJAX_O3.",
-            "issued": "2021-03-09",
-            "temporal": "2011-02-01T00:00:00Z/2023-03-01T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2021-11-16",
-            "keyword": [
-                "atmosphere",
-                "atmospheric chemistry",
-                "earth science"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Laura Iraci",
                 "hasEmail": "mailto:laura.t.iraci@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/LARC/SD/ASDC"
-            },
-            "identifier": "C2166631705-LARC_ASDC",
             "description": "The Alpha Jet Atmospheric eXperiment (AJAX) is a partnership between NASA's Ames Research Center and H211, L.L.C., facilitating routine in-situ measurements over California, Nevada, and the coastal Pacific in support of satellite validation. The standard payload complement includes rigorously-calibrated ozone (O3), formaldehyde (HCHO), carbon dioxide (CO2), and methane (CH4) mixing ratios, as well as meteorological data including 3-D winds. Multiple vertical profiles (to ~8.5 km) can be accomplished in each 2-hr flight. The AJAX project has been collecting trace gas data on a regular basis in all seasons for over a decade, helping to assess satellite sensors' health and calibration over significant portions of their lifetimes, and complementing surface and tower-based observations collected elsewhere in the region.\r\n\r\nAJAX supports NASA's Orbiting Carbon Observatory (OCO-2/3) and Japan's Greenhouse Gases Observing Satellite (GOSAT) and GOSAT-2, and collaborates with many other research organizations (e.g. California Air Resources Board (CARB), NOAA, United States Forest Service (USFS), Environmental Protection Agency (EPA)). AJAX celebrated its 200th science flight in 2016, and previous studies have investigated topics as varied as stratospheric-to-tropospheric transport, forest fire plumes, atmospheric river events, long-range transport of pollution from Asia to the western US, urban outflow, and emissions from gas leaks, oil fields, and dairies.",
-            "title": "Alpha Jet Atmospheric eXperiment Ozone Data",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC%2FAJAX_O3",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC%2FAJAX_O3",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/citing-data",
-                    "description": "ASDC Data Citation Policy",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Data Citation Policy",
+                    "downloadURL": "https://asdc.larc.nasa.gov/citing-data",
+                    "mediaType": "text/html",
                     "title": "View this dataset's data citation policy"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.nasa.gov/centers/ames/earthscience/programs/ajax",
-                    "description": "AJAX Project Website",
                     "@type": "dcat:Distribution",
+                    "description": "AJAX Project Website",
+                    "downloadURL": "https://www.nasa.gov/centers/ames/earthscience/programs/ajax",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://journals.ametsoc.org/view/journals/bams/97/3/bams-d-14-00241.1.xml",
-                    "description": "AJAX Overview Paper - Bulletin of the American Meteorological Society",
                     "@type": "dcat:Distribution",
+                    "description": "AJAX Overview Paper - Bulletin of the American Meteorological Society",
+                    "downloadURL": "https://journals.ametsoc.org/view/journals/bams/97/3/bams-d-14-00241.1.xml",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.nasa.gov/centers/ames/earthscience/programs/ajax/media",
-                    "description": "AJAX on Daily Planet (Discovery Channel Canada, aired Feb 15, 2018)",
                     "@type": "dcat:Distribution",
+                    "description": "AJAX on Daily Planet (Discovery Channel Canada, aired Feb 15, 2018)",
+                    "downloadURL": "https://www.nasa.gov/centers/ames/earthscience/programs/ajax/media",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://youtu.be/ZtGQLrkepes",
-                    "description": "AJAX YouTube Video",
                     "@type": "dcat:Distribution",
+                    "description": "AJAX YouTube Video",
+                    "downloadURL": "https://youtu.be/ZtGQLrkepes",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.youtube.com/watch?v=6WSQ5Ga9awI",
-                    "description": "This Week at NASA (Aug 2016 at 0:48, Soberanes wildfire flights)",
                     "@type": "dcat:Distribution",
+                    "description": "This Week at NASA (Aug 2016 at 0:48, Soberanes wildfire flights)",
+                    "downloadURL": "https://www.youtube.com/watch?v=6WSQ5Ga9awI",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.youtube.com/watch?v=slLTUMgEoFM&feature=youtu.be",
-                    "description": "Ames focus of Years of Living Dangerously documentary",
                     "@type": "dcat:Distribution",
+                    "description": "Ames focus of Years of Living Dangerously documentary",
+                    "downloadURL": "https://www.youtube.com/watch?v=slLTUMgEoFM&feature=youtu.be",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.youtube.com/watch?v=eyFAGnhnsM0",
-                    "description": "This Week at NASA (15 Feb 2013 at 5:53)",
                     "@type": "dcat:Distribution",
+                    "description": "This Week at NASA (15 Feb 2013 at 5:53)",
+                    "downloadURL": "https://www.youtube.com/watch?v=eyFAGnhnsM0",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.youtube.com/watch?v=rjxNZ3CwCFE",
-                    "description": "2014 Seminar at Ames Research Center",
                     "@type": "dcat:Distribution",
+                    "description": "2014 Seminar at Ames Research Center",
+                    "downloadURL": "https://www.youtube.com/watch?v=rjxNZ3CwCFE",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://cdn.earthdata.nasa.gov/conduit/upload/6158/ESDS-RFC-029v2.pdf",
-                    "description": "ICARTT V2.0 Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ICARTT V2.0 Documentation",
+                    "downloadURL": "https://cdn.earthdata.nasa.gov/conduit/upload/6158/ESDS-RFC-029v2.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/ASDC/AJAX_O3",
-                    "description": "DOI data set landing page for AJAX_O3_1",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for AJAX_O3_1",
+                    "downloadURL": "https://doi.org/10.5067/ASDC/AJAX_O3",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2166631705-LARC_ASDC",
-                    "description": "Earthdata Search for AJAX_O3_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for AJAX_O3_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2166631705-LARC_ASDC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://agupubs.onlinelibrary.wiley.com/doi/full/10.1029/2021EA002116",
-                    "description": "A Collection of Airborne Measurements and Analyses of Trace Gases Emitted From Multiple Fires in California",
                     "@type": "dcat:Distribution",
+                    "description": "A Collection of Airborne Measurements and Analyses of Trace Gases Emitted From Multiple Fires in California",
+                    "downloadURL": "https://agupubs.onlinelibrary.wiley.com/doi/full/10.1029/2021EA002116",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/ajax/AJAX-DefinitionofFlightObjectivesTags.pdf",
-                    "description": "AJAX Flight Objectives",
                     "@type": "dcat:Distribution",
+                    "description": "AJAX Flight Objectives",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/ajax/AJAX-DefinitionofFlightObjectivesTags.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/ajax/AJAX-WildfireMeasurementsCompendium.pdf",
-                    "description": "AJAX Wildfire Measurements Compendium",
                     "@type": "dcat:Distribution",
+                    "description": "AJAX Wildfire Measurements Compendium",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/ajax/AJAX-WildfireMeasurementsCompendium.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/outreach-materials#name-alpha-jet-experiment-ajax-flight-catalog-storymap",
-                    "description": "AJAX Flight Catalog Tutorial",
                     "@type": "dcat:Distribution",
+                    "description": "AJAX Flight Catalog Tutorial",
+                    "downloadURL": "https://asdc.larc.nasa.gov/outreach-materials#name-alpha-jet-experiment-ajax-flight-catalog-storymap",
+                    "mediaType": "text/html",
                     "title": "View this dataset's how-to documentation"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/soot/power-user/AJAX/2011",
-                    "description": "AJAX Data on the Sub-Orbital Order Tool (SOOT) Power User Interface (UI)",
                     "@type": "dcat:Distribution",
+                    "description": "AJAX Data on the Sub-Orbital Order Tool (SOOT) Power User Interface (UI)",
+                    "downloadURL": "https://asdc.larc.nasa.gov/soot/power-user/AJAX/2011",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through the Sub-Orbital Order Tool"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://creativecommons.org/licenses/by/4.0/",
-                    "description": "Creative Commons License (CC BY 4.0)",
                     "@type": "dcat:Distribution",
+                    "description": "Creative Commons License (CC BY 4.0)",
+                    "downloadURL": "https://creativecommons.org/licenses/by/4.0/",
+                    "mediaType": "text/html",
                     "title": "View this dataset's data citation policy"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/AJAX/O3_1/",
-                    "description": "ASDC Direct Data Download for AJAX_O3_1",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for AJAX_O3_1",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/AJAX/O3_1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 }
             ],
+            "identifier": "C2166631705-LARC_ASDC",
+            "issued": "2021-03-09",
+            "keyword": [
+                "atmosphere",
+                "atmospheric chemistry",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/ASDC/AJAX_O3",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2021-11-16",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/LARC/SD/ASDC"
+            },
             "spatial": "<?xml version=\"1.0\" encoding=\"UTF-8\"?><gml:Polygon xmlns:gml=\"http://www.opengis.net/gml/3.2\" srsName=\"EPSG:9825\"><gml:outerBoundaryIs><gml:LinearRing><gml:posList>34.0 -125.0 34.0 -114.0 42.0 -114.0 42.0 -125.0 34.0 -125.0</gml:posList></gml:LinearRing></gml:outerBoundaryIs><gml:innerBoundaryIs></gml:innerBoundaryIs></gml:Polygon>",
+            "temporal": "2011-02-01T00:00:00Z/2023-03-01T00:00:00Z",
             "theme": [
                 "AJAX",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Alpha Jet Atmospheric eXperiment Ozone Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-4-ESC3-67P-M20-INFLDSTR-V1.0",
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
+            "description": "This CODMAC level 4 data set contains solar stray-light corrected, in-field stray-light corrected,  radiometric calibrated and geometric distortion corrected  (resampled) image data in W/m^2/sr/nm,  acquired by the OSIRIS Wide Angle Camera on the Rosetta spacecraft  during the COMET ESCORT 3 mission phase, covering the period  from 2015-08-25T23:25:00.000 to 2015-09-22T23:24:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V1.0 is the first version of this dataset: Lien corrected dataset after September 2019 PSA/PDS external peer review.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-4-esc3-67p-m20-infldstr-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-4-ESC3-67P-M20-INFLDSTR-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-4-esc3-67p-m20-infldstr-v1.0",
-            "description": "This CODMAC level 4 data set contains solar stray-light corrected, in-field stray-light corrected,  radiometric calibrated and geometric distortion corrected  (resampled) image data in W/m^2/sr/nm,  acquired by the OSIRIS Wide Angle Camera on the Rosetta spacecraft  during the COMET ESCORT 3 mission phase, covering the period  from 2015-08-25T23:25:00.000 to 2015-09-22T23:24:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V1.0 is the first version of this dataset: Lien corrected dataset after September 2019 PSA/PDS external peer review.",
-            "title": "ROSETTA-ORBITER 67P OSIWAC 4 ESC3-MTP020 RDR-INFLDSTR V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P OSIWAC 4 ESC3-MTP020 RDR-INFLDSTR V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/CJAALTQUCLO2",
             "citation": "Joanna Joiner. 2020-02-26. OMPS_NPP_NMCLDRR_L2. Version 2. OMPS-NPP L2 NM Cloud Pressure and Fraction swath orbital V2. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/CJAALTQUCLO2. https://disc.gsfc.nasa.gov/datacollection/OMPS_NPP_NMCLDRR_L2_2.html. Digital Science Data.",
-            "issued": "2020-02-26",
-            "temporal": "2011-11-13T00:00:00Z/2022-01-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-02-26",
-            "references": [
-                "https://doi.org/10.1109/TGRS.2005.861385"
-            ],
-            "keyword": [
-                "atmosphere",
-                "earth science",
-                "clouds"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "JOANNA JOINER, PH. D",
                 "hasEmail": "mailto:Joanna.Joiner@nasa.gov"
             },
+            "creator": "Joanna Joiner",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C1701674727-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "The OMPS-NPP L2 NM Cloud Pressure and Fraction swath orbital product provides effective cloud fraction and effective cloud pressure retrievals from the Ozone Mapping and Profiling Suite (OMPS) Nadir-Mapper (NM) instrument on the Suomi-NPP satellite. The cloud pressure algorithm retrieves effective cloud pressus, a.k.a optical centroid pressure (OCP) and effective cloud fraction (ECF) using a concept of Mixed Lambert Equivalent Reflectivity (MLER) at 354.1 nm.\n\nEach granule contains data from the daylight portion of each orbit measured for a full day. Spatial coverage is global (-90 to  90 degrees latitude), and there are about 14.5 orbits per day each measuring three limb profiles spaced approximately 250 km in the cross-track direction. The profiles are measured from the ground up to about 80 km with a vertical resolution of the retrieved profiles of approximately 1.8 km.\n\nThe files are written using the Hierarchical Data Format Version 5 or HDF5.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "OMPS_NPP_NMCLDRR_L2",
-            "creator": "Joanna Joiner",
-            "title": "OMPS-NPP L2 NM Cloud Pressure and Fraction swath orbital V2 (OMPS_NPP_NMCLDRR_L2) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/OMPS_NPP_NMCLDRR_L2_2.jpeg",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FCJAALTQUCLO2",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FCJAALTQUCLO2",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
@@ -342819,1260 +342794,1260 @@
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/OMPS_NPP_NMCLDRR_L2_2.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/OMPS_NPP_NMCLDRR_L2_2.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://omps.gesdisc.eosdis.nasa.gov/data/SNPP_OMPS_Level2/OMPS_NPP_NMCLDRR_L2.2/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://omps.gesdisc.eosdis.nasa.gov/data/SNPP_OMPS_Level2/OMPS_NPP_NMCLDRR_L2.2/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://omps.gesdisc.eosdis.nasa.gov/opendap/SNPP_OMPS_Level2/OMPS_NPP_NMCLDRR_L2.2/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://omps.gesdisc.eosdis.nasa.gov/opendap/SNPP_OMPS_Level2/OMPS_NPP_NMCLDRR_L2.2/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=OMPS_NPP_NMCLDRR_L2_2",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=OMPS_NPP_NMCLDRR_L2_2",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://omps.gesdisc.eosdis.nasa.gov/data/SNPP_OMPS_Level2/OMPS_NPP_NMCLDRR_L2.2/doc/README.OMPS_NPP_NMCLDRR_L2.pdf",
-                    "description": "README Document",
                     "@type": "dcat:Distribution",
+                    "description": "README Document",
+                    "downloadURL": "https://omps.gesdisc.eosdis.nasa.gov/data/SNPP_OMPS_Level2/OMPS_NPP_NMCLDRR_L2.2/doc/README.OMPS_NPP_NMCLDRR_L2.pdf",
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
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/OMPS_NPP_NMCLDRR_L2_2.jpeg",
+            "identifier": "C1701674727-GES_DISC",
+            "issued": "2020-02-26",
+            "keyword": [
+                "atmosphere",
+                "earth science",
+                "clouds"
+            ],
+            "landingPage": "https://doi.org/10.5067/CJAALTQUCLO2",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2020-02-26",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
+            },
+            "references": [
+                "https://doi.org/10.1109/TGRS.2005.861385"
+            ],
+            "release-place": "Greenbelt, MD, USA",
+            "series-name": "OMPS_NPP_NMCLDRR_L2",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2011-11-13T00:00:00Z/2022-01-17T00:00:00Z",
             "theme": [
                 "NPP-JPSS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "OMPS-NPP L2 NM Cloud Pressure and Fraction swath orbital V2 (OMPS_NPP_NMCLDRR_L2) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-X-RSI-1%2F2%2F3-CVP1-0008-V1.0",
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
+            "description": "This is a Commissioning measurement covering the time 2004-05-05T20:11:52.500 to 2004-05-06T02:21:10.500.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-x-rsi-1-2-3-cvp1-0008-v1.0_85ug-fiz9",
+            "issued": "2021-05-21",
+            "keyword": [
+                "unknown",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-X-RSI-1%2F2%2F3-CVP1-0008-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-x-rsi-1-2-3-cvp1-0008-v1.0_85ug-fiz9",
-            "description": "This is a Commissioning measurement covering the time 2004-05-05T20:11:52.500 to 2004-05-06T02:21:10.500.",
-            "title": "ROSETTA-ORBITER CHECK RSI 1/2/3 COMMISSIONING 1 0008 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER CHECK RSI 1/2/3 COMMISSIONING 1 0008 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/GPMGV/IFLOODS/MULTIPLE/DATA201",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Huffman, George J, Erich  Stocker, David T Bolvin and Eric J Nelkin.2018. GPM Ground Validation TRMM Multi-satellite Precipitation Analysis (TMPA) IFloodS [indicate subset used]. Dataset available online from the NASA Global Hydrometeorology Resource Center DAAC, Huntsville, Alabama, U.S.A. DOI: http://dx.doi.org/10.5067/GPMGV/IFLOODS/MULTIPLE/DATA201",
-            "issued": "2018-07-19",
-            "temporal": "2013-04-01T00:00:00Z/2013-06-30T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-05-09",
-            "keyword": [
-                "precipitation",
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
-            "identifier": "C1979823036-GHRC_DAAC",
             "description": "The GPM Ground Validation TRMM Multi-satellite Precipitation Analysis (TMPA) IFloodS dataset is a subset of the TMPA 3B42RT gridded precipitation real-time product selected for the time period of the GPM Ground Validation Iowa Flood Studies (IFloodS) held in Iowa during April 1, 2013 to June 30, 2013. The goals of IFloodS were  to collect detailed measurements of precipitation at the Earth\u2019s surface using ground instruments and advanced weather radars and to simultaneously collect data from satellites passing overhead.  TMPA is a calibration-based sequential scheme for combining microwave (MW) and infrared (IR) precipitation estimates from multiple satellites, as well as surface precipitation gauge analyses where feasible, to produce precipitation estimates at fine scales: 3-hourly, 0.25 degree maps. The TMPA IFloodS product is available in netCDF-4 and binary formats, as well as 3-hour rainfall browse images in JPG format.",
-            "graphic-preview-description": "Browse images illustrate the nature and coverage of the data",
-            "title": "GPM Ground Validation TRMM Multi-satellite Precipitation Analysis (TMPA) IFloodS V7",
-            "graphic-preview-file": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/ifloods/TMPA/browse/",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGPMGV%2FIFLOODS%2FMULTIPLE%2FDATA201",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGPMGV%2FIFLOODS%2FMULTIPLE%2FDATA201",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=gpmtmpaifld",
-                    "description": "Files may be downloaded directly to your workstation from this link",
                     "@type": "dcat:Distribution",
+                    "description": "Files may be downloaded directly to your workstation from this link",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=gpmtmpaifld",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/ifloods/TMPA/browse/2013-06-26/ifloods_tmpa_3hrly_rain_2013062612.jpg",
-                    "description": "Sample Browse Image",
                     "@type": "dcat:Distribution",
+                    "description": "Sample Browse Image",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/ifloods/TMPA/browse/2013-06-26/ifloods_tmpa_3hrly_rain_2013062612.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://dx.doi.org/10.1007/978-90-481-2915-7",
-                    "description": "The TRMM Multi-satellite Precipitation Analysis (TMPA)",
                     "@type": "dcat:Distribution",
+                    "description": "The TRMM Multi-satellite Precipitation Analysis (TMPA)",
+                    "downloadURL": "http://dx.doi.org/10.1007/978-90-481-2915-7",
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
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/ifloods/TMPA/doc/gpmtmpaifld_dataset.pdf",
-                    "description": "The guide document contains detailed information about the dataset",
                     "@type": "dcat:Distribution",
+                    "description": "The guide document contains detailed information about the dataset",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/ifloods/TMPA/doc/gpmtmpaifld_dataset.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://dx.doi.org/10.1175/JHM560.1",
-                    "description": "The TRMM Multi-satellite Precipitation Analysis (TMPA): Quasi-global, multiyear, combined-sensor precipitation estimates at fine scales",
                     "@type": "dcat:Distribution",
+                    "description": "The TRMM Multi-satellite Precipitation Analysis (TMPA): Quasi-global, multiyear, combined-sensor precipitation estimates at fine scales",
+                    "downloadURL": "http://dx.doi.org/10.1175/JHM560.1",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://dx.doi.org/10.1016/j.atmosres.2014.07.032",
-                    "description": "Comparison of precipitation estimates between Version 7 3-hourly TRMM Multi-Satellite Precipitation Analysis (TMPA) near-real-time and research products",
                     "@type": "dcat:Distribution",
+                    "description": "Comparison of precipitation estimates between Version 7 3-hourly TRMM Multi-Satellite Precipitation Analysis (TMPA) near-real-time and research products",
+                    "downloadURL": "http://dx.doi.org/10.1016/j.atmosres.2014.07.032",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://dx.doi.org/10.1016/j.atmosres.2014.11.012",
-                    "description": "Validation of TRMM multi-satellite precipitation analysis (TMPA) products in the Peruvian Andes",
                     "@type": "dcat:Distribution",
+                    "description": "Validation of TRMM multi-satellite precipitation analysis (TMPA) products in the Peruvian Andes",
+                    "downloadURL": "http://dx.doi.org/10.1016/j.atmosres.2014.11.012",
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
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/ifloods/TMPA/browse/",
-                    "description": "Browse images illustrate the nature and coverage of the data",
                     "@type": "dcat:Distribution",
+                    "description": "Browse images illustrate the nature and coverage of the data",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/ifloods/TMPA/browse/",
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
+            "graphic-preview-description": "Browse images illustrate the nature and coverage of the data",
+            "graphic-preview-file": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/ifloods/TMPA/browse/",
+            "identifier": "C1979823036-GHRC_DAAC",
+            "issued": "2018-07-19",
+            "keyword": [
+                "precipitation",
+                "atmosphere",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/GPMGV/IFLOODS/MULTIPLE/DATA201",
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
             "spatial": "-179.875 -59.875 179.875 59.875",
+            "temporal": "2013-04-01T00:00:00Z/2013-06-30T23:59:59Z",
             "theme": [
                 "IFloodS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "GPM Ground Validation TRMM Multi-satellite Precipitation Analysis (TMPA) IFloodS V7"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-P-LEISA-2-PLUTO-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This data set contains Raw data taken by the New Horizons Linear Etalon Imaging Spectral Array instrument during the Pluto encounter mission phase.  This is VERSION 1.0 of this data set.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-p-leisa-2-pluto-v1.0_85wh-e9t2",
             "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "vega",
                 "charon",
                 "pluto",
                 "new horizons"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-P-LEISA-2-PLUTO-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-p-leisa-2-pluto-v1.0_85wh-e9t2",
-            "description": "This data set contains Raw data taken by the New Horizons Linear Etalon Imaging Spectral Array instrument during the Pluto encounter mission phase.  This is VERSION 1.0 of this data set.",
-            "title": "NEW HORIZONS\n      LEISA PLUTO ENCOUNTER\n      RAW V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "NEW HORIZONS\n      LEISA PLUTO ENCOUNTER\n      RAW V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ASDC_DAAC/FIRE/0096",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "1999-11-15. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/ASDC_DAAC/FIRE/0096.",
-            "issued": "1999-11-09",
-            "temporal": "1991-11-13T00:00:00Z/1991-12-08T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2018-07-11",
-            "keyword": [
-                "atmospheric winds",
-                "atmospheric radiation",
-                "atmospheric temperature",
-                "atmospheric water vapor",
-                "atmosphere",
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
-            "identifier": "C1000001163-LARC_ASDC",
             "description": "The First ISCCP Regional Experiments have been designed to improve data products and cloud/radiation parameterizations used in general circulation models (GCMs). Specifically, the goals of FIRE are (1) to improve basic understanding of the interaction of physical processes in determining life cycles of cirrus and marine stratocumulus systems and the radiative properties of these clouds during their life cycles and (2) to investigate the interrelationships between the ISCCP data, GCM parameterizations, and higher space and time resolution cloud data.To-date, four intensive field-observation periods were planned and executed: a cirrus IFO (October 13-November 2, 1986); a marine stratocumulus IFO off the southwestern coast of California (June 29-July 20, 1987); a second cirrus IFO in southeastern Kansas (November 13-December 7, 1991); and a second marine stratocumulus IFO in the eastern North Atlantic Ocean (June 1-June 28, 1992). Each mission combined coordinated satellite, airborne, and surface observations with modeling studies to investigate the cloud properties and physical processes of the cloud systems.The CSU Station 2 surface radiation data set was collected every 2 minutes for the period from Nov. 13, 1991 through Dec. 8, 1991 at the Tri-City Airport, Parsons, Kansas (37 deg. 20 min. N, 95 deg. 30 min. 30 sec. W.) NOTE: the 2 minute values were instantaneous readings.",
-            "title": "First ISCCP Regional Experiment (FIRE) Cirrus Phase II Colorado State University (CSU) Station 2 Data",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC_DAAC%2FFIRE%2F0096",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC_DAAC%2FFIRE%2F0096",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1000001163-LARC_ASDC",
-                    "description": "Earthdata Search for FIRE_CI2_CSU_STN2_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for FIRE_CI2_CSU_STN2_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1000001163-LARC_ASDC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/FIRE/FIRE_CI2_CSU_STN2/contents.html",
-                    "description": "OPeNDAP data access for FIRE_CI2_CSU_STN2_1",
                     "@type": "dcat:Distribution",
+                    "description": "OPeNDAP data access for FIRE_CI2_CSU_STN2_1",
+                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/FIRE/FIRE_CI2_CSU_STN2/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/guide/base_fire_ci2_csu_dataset.pdf",
-                    "description": "FIRE Cirrus 2 Colorado State University (CSU) Langley DAAC Data Set Document",
                     "@type": "dcat:Distribution",
+                    "description": "FIRE Cirrus 2 Colorado State University (CSU) Langley DAAC Data Set Document",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/guide/base_fire_ci2_csu_dataset.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/postscript",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/readme/readme_fire_ci2_csu_stn2.ps",
-                    "description": "FIRE Cirrus 2 - Direct File Download (.ps)",
                     "@type": "dcat:Distribution",
+                    "description": "FIRE Cirrus 2 - Direct File Download (.ps)",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/readme/readme_fire_ci2_csu_stn2.ps",
+                    "mediaType": "application/postscript",
                     "title": "View this dataset's science data product software documentation"
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
-                    "downloadURL": "https://doi.org/10.5067/ASDC_DAAC/FIRE/0096",
-                    "description": "DOI data set landing page for FIRE_CI2_CSU_STN2_1",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for FIRE_CI2_CSU_STN2_1",
+                    "downloadURL": "https://doi.org/10.5067/ASDC_DAAC/FIRE/0096",
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
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/FIRE/FIRE_CI2_CSU_STN2/",
-                    "description": "ASDC Direct Data Download for FIRE_CI2_CSU_STN2_1",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for FIRE_CI2_CSU_STN2_1",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/FIRE/FIRE_CI2_CSU_STN2/",
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
+            "identifier": "C1000001163-LARC_ASDC",
+            "issued": "1999-11-09",
+            "keyword": [
+                "atmospheric winds",
+                "atmospheric radiation",
+                "atmospheric temperature",
+                "atmospheric water vapor",
+                "atmosphere",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/ASDC_DAAC/FIRE/0096",
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
             "spatial": "37.33 -95.5",
+            "temporal": "1991-11-13T00:00:00Z/1991-12-08T23:59:59.999Z",
             "theme": [
                 "FIRE",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "First ISCCP Regional Experiment (FIRE) Cirrus Phase II Colorado State University (CSU) Station 2 Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/2081",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Christensen, A.L., J.M. Mallard, J. Nghiem, M. Simard, T.M. Pavelsky, and M.P. Lamb. 2022. Delta-X: Acoustic Doppler Current Profiler Channel Surveys, MRD, Louisiana, 2021, V2. ORNL DAAC, Oak Ridge, Tennessee, USA. https://doi.org/10.3334/ORNLDAAC/2081",
-            "issued": "2022-09-23",
-            "temporal": "2021-03-25T00:00:00Z/2021-09-25T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-06-12",
-            "keyword": [
-                "terrestrial hydrosphere",
-                "biosphere",
-                "earth science",
-                "ecosystems",
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
-            "identifier": "C2484970169-ORNL_CLOUD",
             "description": "This dataset provides river discharge measurements collected at selected locations in the Atchafalaya and Terrebonne Basins within the Mississippi River Delta (MRD) floodplain in coastal Louisiana, USA. The measurements were made during the Delta-X 2021 field efforts from 2021-03-25 to 2021-04-11 (spring) and 2021-08-16 to 2021-09-25 (fall). Channel surveys were conducted with a Teledyne RiverPro acoustic doppler current profiler (ADCP) or a Sontek M9 RiverSurveyor ADCP on selected wide channels (>100 m wide) and a few selected narrow channels (approximately 10 m wide) near the Delta-X intensive study sites. River discharge was measured on cross-channel transects. Reported data include bathymetry, discharge (m3 s-1), and flow velocity.",
-            "graphic-preview-description": "Locations of river discharge measurements (black triangles) in the Atchafalaya and Terrebonne Basins within the Mississippi River Delta (MRD) floodplain in coastal Louisiana, U.S. Measurements were taken by Delta-X project in March and April 2021. Source: DeltaX_RiverDischarge_Spring2021.csv",
-            "title": "Delta-X: Acoustic Doppler Current Profiler Channel Surveys, MRD, Louisiana, 2021, V2",
-            "graphic-preview-file": "https://daac.ornl.gov/DELTAX/guides/DeltaX_ADCP_Measurements_V2_Fig1.jpg",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F2081",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F2081",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/deltax/DeltaX_ADCP_Measurements_V2/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/deltax/DeltaX_ADCP_Measurements_V2/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/DELTAX/guides/DeltaX_ADCP_Measurements_V2.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/DELTAX/guides/DeltaX_ADCP_Measurements_V2.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/2081",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/2081",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/deltax/DeltaX_ADCP_Measurements_V2/comp/DeltaX_ADCP_Measurements_V2.pdf",
-                    "description": "Delta-X: Acoustic Doppler Current Profiler Channel Surveys, MRD, Louisiana, 2021, V2: DeltaX_ADCP_Measurements_V2.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "Delta-X: Acoustic Doppler Current Profiler Channel Surveys, MRD, Louisiana, 2021, V2: DeltaX_ADCP_Measurements_V2.pdf",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/deltax/DeltaX_ADCP_Measurements_V2/comp/DeltaX_ADCP_Measurements_V2.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://daac.ornl.gov/DELTAX/guides/DeltaX_ADCP_Measurements_V2_Fig1.jpg",
-                    "description": "Locations of river discharge measurements (black triangles) in the Atchafalaya and Terrebonne Basins within the Mississippi River Delta (MRD) floodplain in coastal Louisiana, U.S. Measurements were taken by Delta-X project in March and April 2021. Source: DeltaX_RiverDischarge_Spring2021.csv",
                     "@type": "dcat:Distribution",
+                    "description": "Locations of river discharge measurements (black triangles) in the Atchafalaya and Terrebonne Basins within the Mississippi River Delta (MRD) floodplain in coastal Louisiana, U.S. Measurements were taken by Delta-X project in March and April 2021. Source: DeltaX_RiverDischarge_Spring2021.csv",
+                    "downloadURL": "https://daac.ornl.gov/DELTAX/guides/DeltaX_ADCP_Measurements_V2_Fig1.jpg",
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
+            "graphic-preview-description": "Locations of river discharge measurements (black triangles) in the Atchafalaya and Terrebonne Basins within the Mississippi River Delta (MRD) floodplain in coastal Louisiana, U.S. Measurements were taken by Delta-X project in March and April 2021. Source: DeltaX_RiverDischarge_Spring2021.csv",
+            "graphic-preview-file": "https://daac.ornl.gov/DELTAX/guides/DeltaX_ADCP_Measurements_V2_Fig1.jpg",
+            "identifier": "C2484970169-ORNL_CLOUD",
+            "issued": "2022-09-23",
+            "keyword": [
+                "terrestrial hydrosphere",
+                "biosphere",
+                "earth science",
+                "ecosystems",
+                "surface water"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/2081",
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
             "spatial": "-91.45 29.16 -90.67 29.7",
+            "temporal": "2021-03-25T00:00:00Z/2021-09-25T23:59:59Z",
             "theme": [
                 "Delta-X",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Delta-X: Acoustic Doppler Current Profiler Channel Surveys, MRD, Louisiana, 2021, V2"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/MERGED-S3/OLCI/L3M/ILW/4",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/GSFC/SED/ESD/GCDC/OB.DAAC. https://doi.org/10.5067/MERGED-S3/OLCI/L3M/ILW/4.",
-            "issued": "2022-09-13",
-            "temporal": "2016-04-25T00:00:00Z/2024-05-06T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-04-26",
-            "keyword": [
-                "biological classification",
-                "ocean optics",
-                "oceans",
-                "coastal processes",
-                "earth science",
-                "biosphere",
-                "earth science services",
-                "marine environment monitoring",
-                "ecosystems",
-                "environmental advisories",
-                "environmental governance/management",
-                "surface water",
-                "hydrological advisories",
-                "terrestrial hydrosphere",
-                "human dimensions",
-                "water quality/water chemistry",
-                "aquatic sciences",
-                "bacteria/archaea"
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
-            "identifier": "C2954423973-OB_DAAC",
             "description": "The Inland Waters dataset (ILW) provides data for lakes and other water bodies across the contiguous United States (CONUS) and Alaska. ILW significantly reduces the processing effort required by end users and is a standardized community resource for lake and reservoir algorithm development and performance assessment.The data is provided for 15,450 CONUS waterbodies with a size of at least one 300 m pixel and over 2,300 resolvable lakes with sizes greater than three 300 m pixels. Alaska has 5,874 lakes resolvable lakes. ILW is a times series containing 10 years of MERIS (2002-2012) and OLCI from both Sentinel-3a (2016-present) and Sentinel-3b (2018-present).",
-            "title": "Merged Sentinel-3A and Sentinel-3B OLCI Regional Mapped Inland Waters (ILW) Data, version 4",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMERGED-S3%2FOLCI%2FL3M%2FILW%2F4",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMERGED-S3%2FOLCI%2FL3M%2FILW%2F4",
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
-                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/data/10.5067/MERGED-S3/OLCI/L3M/ILW/4",
-                    "description": "Merged Sentinel-3A and Sentinel-3B OLCI 3M Inland Waters (ILW) Dataset Landing Page",
                     "@type": "dcat:Distribution",
+                    "description": "Merged Sentinel-3A and Sentinel-3B OLCI 3M Inland Waters (ILW) Dataset Landing Page",
+                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/data/10.5067/MERGED-S3/OLCI/L3M/ILW/4",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 }
             ],
+            "identifier": "C2954423973-OB_DAAC",
+            "issued": "2022-09-13",
+            "keyword": [
+                "biological classification",
+                "ocean optics",
+                "oceans",
+                "coastal processes",
+                "earth science",
+                "biosphere",
+                "earth science services",
+                "marine environment monitoring",
+                "ecosystems",
+                "environmental advisories",
+                "environmental governance/management",
+                "surface water",
+                "hydrological advisories",
+                "terrestrial hydrosphere",
+                "human dimensions",
+                "water quality/water chemistry",
+                "aquatic sciences",
+                "bacteria/archaea"
+            ],
+            "landingPage": "https://doi.org/10.5067/MERGED-S3/OLCI/L3M/ILW/4",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2024-04-26",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GCDC/OB.DAAC"
+            },
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2016-04-25T00:00:00Z/2024-05-06T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Merged Sentinel-3A and Sentinel-3B OLCI Regional Mapped Inland Waters (ILW) Data, version 4"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ASDC_DAAC/FIRE/0121",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2000-04-07. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/ASDC_DAAC/FIRE/0121.",
-            "issued": "2000-03-17",
-            "temporal": "1991-11-18T00:00:00Z/1991-12-06T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2018-07-11",
-            "keyword": [
-                "earth science",
-                "atmosphere",
-                "clouds",
-                "infrared wavelengths",
-                "spectral/engineering",
-                "visible wavelengths"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "EDWIN ELORANTA",
                 "hasEmail": "mailto:eloranta@lidar.meteor.wisc.edu"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/LARC/SD/ASDC"
-            },
-            "identifier": "C1000001200-LARC_ASDC",
             "description": "The First ISCCP Regional Experiments have been designed to improve data products and cloud/radiation parameterizations used in general circulation models (GCMs). Specifically, the goals of FIRE are (1) to seek the basic understanding of the interaction of physical processes in determining life cycles of cirrus and marine stratocumulus systems and the radiative properties of these clouds during their life cycles and (2) to investigate the interrelationships between ISCCP data, GCM parameterizations, and higher space and time resolution cloud data. To-date, four intensive field-observation periods were planned and executed: a cirrus IFO (October 13 - November 2, 1986); a marine stratocumulus IFO off the southwestern coast of California (June 29 - July 20, 1987); a second cirrus IFO in southeastern Kansas (November 13 - December 7, 1991); and a second marine stratocumulus IFO in the eastern North Atlantic Ocean (June 1 - June 28, 1992). Each mission combined coordinated satellite, airborne, and surface observations with modeling studies to investigate the cloud properties and physical processes of the cloud systems.This data set contains images of cirrus cloud scans of 120 km extent both along the wind and across the wind (at the cirrus clouds heights). These images were collected during FIRE Cirrus 2 in Coffeyville, Kansas.",
-            "title": "First ISCCP Regional Experiment (FIRE) Cirrus 2 Volume Imaging Lidar (VIL) Cirrus Scan Data",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC_DAAC%2FFIRE%2F0121",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC_DAAC%2FFIRE%2F0121",
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
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1000001200-LARC_ASDC",
-                    "description": "Earthdata Search for FIRE_CI2_VIL_SCAN_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for FIRE_CI2_VIL_SCAN_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1000001200-LARC_ASDC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/guide/base_fire_ci2_hsrl_vil_dataset.pdf",
-                    "description": "FIRE Cirrus 2 High Spectral Resolution Lidar (HSRL)/Volume Imaging Lidar (VIL) Langley DAAC Data Set Document",
                     "@type": "dcat:Distribution",
+                    "description": "FIRE Cirrus 2 High Spectral Resolution Lidar (HSRL)/Volume Imaging Lidar (VIL) Langley DAAC Data Set Document",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/guide/base_fire_ci2_hsrl_vil_dataset.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/readme/readme_fire_ci2_vil_scan.txt",
-                    "description": "FIRE II experiment data with Altitude vs. Time (RTI) and Cirrus Scan gif pictures Readme",
                     "@type": "dcat:Distribution",
+                    "description": "FIRE II experiment data with Altitude vs. Time (RTI) and Cirrus Scan gif pictures Readme",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/readme/readme_fire_ci2_vil_scan.txt",
+                    "mediaType": "text/html",
                     "title": "View this dataset's read me document"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/ASDC_DAAC/FIRE/0121",
-                    "description": "DOI data set landing page for FIRE_CI2_VIL_SCAN_1",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for FIRE_CI2_VIL_SCAN_1",
+                    "downloadURL": "https://doi.org/10.5067/ASDC_DAAC/FIRE/0121",
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
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/fire2_cirrus/mission_summaries.html",
-                    "description": "ASDC List of FIRE II - Cirrus Mission Summaries Available",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC List of FIRE II - Cirrus Mission Summaries Available",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/fire2_cirrus/mission_summaries.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/FIRE/FIRE_CI2_VIL_SCAN/",
-                    "description": "ASDC Direct Data Download for FIRE_CI2_VIL_SCAN_1",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for FIRE_CI2_VIL_SCAN_1",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/FIRE/FIRE_CI2_VIL_SCAN/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/FIRE/FIRE_CI2_VIL_SCAN/contents.html",
-                    "description": "OPeNDAP data access for FIRE_CI2_VIL_SCAN_1",
                     "@type": "dcat:Distribution",
+                    "description": "OPeNDAP data access for FIRE_CI2_VIL_SCAN_1",
+                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/FIRE/FIRE_CI2_VIL_SCAN/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 }
             ],
+            "identifier": "C1000001200-LARC_ASDC",
+            "issued": "2000-03-17",
+            "keyword": [
+                "earth science",
+                "atmosphere",
+                "clouds",
+                "infrared wavelengths",
+                "spectral/engineering",
+                "visible wavelengths"
+            ],
+            "landingPage": "https://doi.org/10.5067/ASDC_DAAC/FIRE/0121",
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
             "spatial": "36.93 -95.7",
+            "temporal": "1991-11-18T00:00:00Z/1991-12-06T23:59:59.999Z",
             "theme": [
                 "FIRE",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "First ISCCP Regional Experiment (FIRE) Cirrus 2 Volume Imaging Lidar (VIL) Cirrus Scan Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/Y67YQ1L3ZZ4R",
             "citation": "Global Modeling and Assimilation Office (GMAO). 2015-06-30. M2T1NXOCN. Version 5.12.4. MERRA-2 tavg1_2d_ocn_Nx: 2d,1-Hourly,Time-Averaged,Single-Level,Assimilation,Ocean Surface Diagnostics V5.12.4. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/Y67YQ1L3ZZ4R. https://disc.gsfc.nasa.gov/datacollection/M2T1NXOCN_5.12.4.html. Digital Science Data.",
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
-                "land surface",
-                "atmospheric radiation",
-                "ocean heat budget",
-                "cryosphere",
-                "snow/ice",
-                "atmospheric water vapor",
-                "sea ice",
-                "precipitation",
-                "ocean temperature",
-                "oceans",
-                "clouds",
-                "atmosphere",
-                "surface thermal properties",
-                "terrestrial hydrosphere",
-                "atmospheric temperature",
-                "earth science"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "DANA OSTRENGA",
                 "hasEmail": "mailto:dana.ostrenga@nasa.gov"
             },
+            "creator": "Global Modeling and Assimilation Office (GMAO)",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C1276812862-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "M2T1NXOCN (or  tavg1_2d_ocn_Nx) is an hourly time-averaged 2-dimensional data collection in Modern-Era Retrospective analysis for Research and Applications version 2 (MERRA-2).  This collection consists of ocean surface diagnostics, such as open water skin temperature (sea surface temperature), open water latent energy flux, open water upward sensible heat flux, and open water net downward longwave ( or shortwave ) flux .  The data field is time-stamped with the central time of an hour starting from 00:30 UTC, e.g.: 00:30, 01:30, \u2026 , 23:30 UTC.\n\nMERRA-2 is the latest version of global atmospheric reanalysis for the satellite era produced by NASA Global Modeling and Assimilation Office (GMAO) using the Goddard Earth Observing System Model (GEOS) version 5.12.4.  The dataset covers the period of 1980-present with the latency of ~3 weeks after the end of a month. \n\nData Reprocessing:  Please check \u201cRecords of MERRA-2 Data Reprocessing and Service Changes\u201d linked from the \u201cDocumentation\u201d tab on this page.  Note that a reprocessed data filename is different from the original file.\n\nMERRA-2 Mailing List: Sign up to receive information on reprocessing of data, changing of tools and services, as well as data announcements from GMAO. Contact the GES DISC Help Desk (gsfc-dl-help-disc@mail.nasa.gov) to be added to the list.\n\nQuestions: If you have a question, please read \"MERRA-2 File Specification Document\",  \u201cMERRA-2 Data Access \u2013 Quick Start Guide\u201d, and FAQs linked from the \u201dDocumentation\u201d tab on this page.  If that does not answer your question, you may email the question on data access to the GES DISC Help Desk (gsfc-dl-help-disc@mail.nasa.gov), or the question on science to the MERRA-2 science team (merra-questions@lists.nasa.gov).",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "M2T1NXOCN",
-            "creator": "Global Modeling and Assimilation Office (GMAO)",
-            "graphic-preview-description": "The GES-DISC Interactive Online Visualization ANd aNalysis Interface (Giovanni) is a web-based tool that allows users to interactively visualize and analyze data.",
-            "title": "MERRA-2 tavg1_2d_ocn_Nx: 2d,1-Hourly,Time-Averaged,Single-Level,Assimilation,Ocean Surface Diagnostics 0.625 x 0.5 degree V5.12.4 (M2T1NXOCN) at GES DISC",
-            "graphic-preview-file": "https://giovanni.gsfc.nasa.gov/giovanni/#variableFacets=dataProductPlatformInstrument%3AMERRA-2%20Model%3B",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FY67YQ1L3ZZ4R",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FY67YQ1L3ZZ4R",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/M2T1NXOCN_5.12.4.png",
-                    "description": "M2T1NXOCN variable",
                     "@type": "dcat:Distribution",
+                    "description": "M2T1NXOCN variable",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/M2T1NXOCN_5.12.4.png",
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
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/M2T1NXOCN_5.12.4.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/M2T1NXOCN_5.12.4.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://goldsmr4.gesdisc.eosdis.nasa.gov/data/MERRA2/M2T1NXOCN.5.12.4/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://goldsmr4.gesdisc.eosdis.nasa.gov/data/MERRA2/M2T1NXOCN.5.12.4/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://giovanni.gsfc.nasa.gov/giovanni/#variableFacets=dataProductPlatformInstrument%3AMERRA-2%20Model%3B",
-                    "description": "The GES-DISC Interactive Online Visualization ANd aNalysis Interface (Giovanni) is a web-based tool that allows users to interactively visualize and analyze data.",
                     "@type": "dcat:Distribution",
+                    "description": "The GES-DISC Interactive Online Visualization ANd aNalysis Interface (Giovanni) is a web-based tool that allows users to interactively visualize and analyze data.",
+                    "downloadURL": "https://giovanni.gsfc.nasa.gov/giovanni/#variableFacets=dataProductPlatformInstrument%3AMERRA-2%20Model%3B",
+                    "mediaType": "text/html",
                     "title": "Get a related visualization through GIOVANNI"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=M2T1NXOCN",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=M2T1NXOCN",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://goldsmr4.gesdisc.eosdis.nasa.gov/dods/M2T1NXOCN.info",
-                    "description": "The GrADS Data Server (GDS) is another form of OPeNDAP that provides subsetting and some analysis services across the Internet.",
                     "@type": "dcat:Distribution",
+                    "description": "The GrADS Data Server (GDS) is another form of OPeNDAP that provides subsetting and some analysis services across the Internet.",
+                    "downloadURL": "https://goldsmr4.gesdisc.eosdis.nasa.gov/dods/M2T1NXOCN.info",
+                    "mediaType": "text/html",
                     "title": "Use GRADS DATA SERVER (GDS) to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://goldsmr4.gesdisc.eosdis.nasa.gov/opendap/MERRA2/M2T1NXOCN.5.12.4/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://goldsmr4.gesdisc.eosdis.nasa.gov/opendap/MERRA2/M2T1NXOCN.5.12.4/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://goldsmr4.gesdisc.eosdis.nasa.gov/thredds/catalog/MERRA2_aggregation/M2T1NXOCN.5.12.4/catalog.html",
-                    "description": "Time aggregated THREDDS Data Server (TDS) ",
                     "@type": "dcat:Distribution",
+                    "description": "Time aggregated THREDDS Data Server (TDS) ",
+                    "downloadURL": "https://goldsmr4.gesdisc.eosdis.nasa.gov/thredds/catalog/MERRA2_aggregation/M2T1NXOCN.5.12.4/catalog.html",
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
-                    "downloadURL": "https://goldsmr4.gesdisc.eosdis.nasa.gov/data/MERRA2/M2T1NXOCN.5.12.4/doc/MERRA2.README.pdf",
-                    "description": "README Document",
                     "@type": "dcat:Distribution",
+                    "description": "README Document",
+                    "downloadURL": "https://goldsmr4.gesdisc.eosdis.nasa.gov/data/MERRA2/M2T1NXOCN.5.12.4/doc/MERRA2.README.pdf",
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
+            "graphic-preview-file": "https://giovanni.gsfc.nasa.gov/giovanni/#variableFacets=dataProductPlatformInstrument%3AMERRA-2%20Model%3B",
+            "identifier": "C1276812862-GES_DISC",
+            "issued": "2007-06-14",
+            "keyword": [
+                "land surface",
+                "atmospheric radiation",
+                "ocean heat budget",
+                "cryosphere",
+                "snow/ice",
+                "atmospheric water vapor",
+                "sea ice",
+                "precipitation",
+                "ocean temperature",
+                "oceans",
+                "clouds",
+                "atmosphere",
+                "surface thermal properties",
+                "terrestrial hydrosphere",
+                "atmospheric temperature",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/Y67YQ1L3ZZ4R",
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
+            "series-name": "M2T1NXOCN",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "1980-01-01T00:00:00Z/2022-01-17T00:00:00Z",
             "theme": [
                 "MERRA-2",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "MERRA-2 tavg1_2d_ocn_Nx: 2d,1-Hourly,Time-Averaged,Single-Level,Assimilation,Ocean Surface Diagnostics 0.625 x 0.5 degree V5.12.4 (M2T1NXOCN) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.7265/N55H7D6Q",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Monthly Mean Precipitation Sums at Russian Arctic Stations, 1966-1990, Version 1. Version 1. Archived by National Aeronautics and Space Administration, U.S. Government, National Snow and Ice Data Center. https://doi.org/10.7265/N55H7D6Q.",
-            "issued": "1966-01-01",
-            "temporal": "1966-01-01T00:00:00Z/1990-12-31T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "1990-12-31",
-            "keyword": [
-                "precipitation",
-                "atmosphere",
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
-            "identifier": "C1386206509-NSIDCV0",
             "description": "This data set contains monthly mean precipitation sums from Russian arctic stations. Precipitation measurements were acquired using a Tretyakov precipitation gauge. Data have not been adjusted for wind bias. Data from 1967 and later are corrected for wetting loss (this correction was made by observers as they recorded the station data). Precipitation measurements from 216 stations are available. An analysis of existing precipitation data sets confirmed that data from these stations are not, at the time of publication, available in other commonly used precipitation data sets. Most data records begin in 1966 and end in 1990.",
-            "title": "Monthly Mean Precipitation Sums at Russian Arctic Stations, 1966-1990, Version 1",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.7265%2FN55H7D6Q",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.7265%2FN55H7D6Q",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/forms/G02170_or.html?major_version=1",
-                    "description": "Direct download, with optional registration page.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download, with optional registration page.",
+                    "downloadURL": "https://nsidc.org/forms/G02170_or.html?major_version=1",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.7265/N55H7D6Q",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.7265/N55H7D6Q",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.7265/N55H7D6Q",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.7265/N55H7D6Q",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C1386206509-NSIDCV0",
+            "issued": "1966-01-01",
+            "keyword": [
+                "precipitation",
+                "atmosphere",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.7265/N55H7D6Q",
+            "language": [
+                "en-US"
+            ],
+            "modified": "1990-12-31",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NSIDC"
+            },
             "spatial": "38.25 50.17 164.17 69.77",
+            "temporal": "1966-01-01T00:00:00Z/1990-12-31T23:59:59.999Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Monthly Mean Precipitation Sums at Russian Arctic Stations, 1966-1990, Version 1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=CO-E%2FJ%2FS%2FSW-CAPS-2-UNCALIBRATED-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This data set consists of all of the uncalibrated data collected by the Cassini Plasma Spectrometer on-board the CO spacecraft during the entire mission.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.co-e-j-s-sw-caps-2-uncalibrated-v1.0_8648-m27i",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "jupiter",
                 "saturn",
                 "earth",
                 "cassini-huygens"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=CO-E%2FJ%2FS%2FSW-CAPS-2-UNCALIBRATED-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.co-e-j-s-sw-caps-2-uncalibrated-v1.0_8648-m27i",
-            "description": "This data set consists of all of the uncalibrated data collected by the Cassini Plasma Spectrometer on-board the CO spacecraft during the entire mission.",
-            "title": "CASSINI E/J/S/SW CAPS UNCALIBRATED V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "CASSINI E/J/S/SW CAPS UNCALIBRATED V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/EPOCH/EXRAD/DATA101",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "McLinden, Matthew .2021. ER-2 X-Band Doppler Radar (EXRAD) EPOCH [indicate subset used]. Dataset available online from the NASA Global Hydrometeorology Resource Center DAAC, Huntsville, Alabama, U.S.A. DOI: http://dx.doi.org/10.5067/EPOCH/EXRAD/DATA101",
-            "issued": "2021-09-23",
-            "temporal": "2017-08-09T04:15:27Z/2017-08-31T15:57:21Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-09-21",
-            "keyword": [
-                "spectral/engineering",
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
-            "identifier": "C2132312390-GHRC_DAAC",
             "description": "The ER-2 X-Band Doppler Radar (EXRAD) EPOCH dataset consists of radar reflectivity and Doppler velocity estimates collected by the EXRAD onboard the AV-6 Global Hawk Unmanned Aerial Vehicle research aircraft, though traditionally this instrument is flown on the NASA ER-2 aircraft. These data were gathered during the East Pacific Origins and Characteristics of Hurricanes (EPOCH) project. EPOCH was a NASA program manager training opportunity directed at training NASA young scientists in conceiving, planning, and executing a major airborne science field program. The goals of the EPOCH project were to sample tropical cyclogenesis or intensification of an Eastern Pacific hurricane and to train the next generation of NASA Airborne Science Program leadership. The EXRAD EPOCH dataset files are available from August 9, 2017 through August 31, 2017 in HDF-5 format.",
-            "title": "ER-2 X-Band Doppler Radar (EXRAD) EPOCH V1",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FEPOCH%2FEXRAD%2FDATA101",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FEPOCH%2FEXRAD%2FDATA101",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/portal/ghrc/search?q=exradimpacts&ghrccloud%2Fdata%2F=",
-                    "description": "Files may be downloaded directly to your workstation from this link",
                     "@type": "dcat:Distribution",
+                    "description": "Files may be downloaded directly to your workstation from this link",
+                    "downloadURL": "https://search.earthdata.nasa.gov/portal/ghrc/search?q=exradimpacts&ghrccloud%2Fdata%2F=",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://har.gsfc.nasa.gov/index.php?section=14",
-                    "description": "EXRAD Description and Sample Measurements from the Nadir Beam",
                     "@type": "dcat:Distribution",
+                    "description": "EXRAD Description and Sample Measurements from the Nadir Beam",
+                    "downloadURL": "http://har.gsfc.nasa.gov/index.php?section=14",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "http://science.gsfc.nasa.gov/sci/content/uploadFiles/scihi_atmos_ppt/2013_4_highlights.pdf",
-                    "description": "First Flights of ER-2 X-band Radar - EXRAD",
                     "@type": "dcat:Distribution",
+                    "description": "First Flights of ER-2 X-band Radar - EXRAD",
+                    "downloadURL": "http://science.gsfc.nasa.gov/sci/content/uploadFiles/scihi_atmos_ppt/2013_4_highlights.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://earth.gsfc.nasa.gov/meso/campaigns/epoch",
-                    "description": "EPOCH: East Pacific Origins and Characteristics of Hurricanes",
                     "@type": "dcat:Distribution",
+                    "description": "EPOCH: East Pacific Origins and Characteristics of Hurricanes",
+                    "downloadURL": "https://earth.gsfc.nasa.gov/meso/campaigns/epoch",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://uas.noaa.gov/News/Articles/ArtMID/6699/ArticleID/401/NOAA-UAS-Program-Participates-in-NASAs-East-Pacific-Origins-and-Characteristics-of-Hurricanes-EPOCH-Project",
-                    "description": "Program Participates in NASA\u2019s East Pacific Origins and Characteristics of Hurricanes (EPOCH) Project",
                     "@type": "dcat:Distribution",
+                    "description": "Program Participates in NASA\u2019s East Pacific Origins and Characteristics of Hurricanes (EPOCH) Project",
+                    "downloadURL": "https://uas.noaa.gov/News/Articles/ArtMID/6699/ArticleID/401/NOAA-UAS-Program-Participates-in-NASAs-East-Pacific-Origins-and-Characteristics-of-Hurricanes-EPOCH-Project",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.7924/G8CC0XMR",
-                    "description": "NASA GPM-Ground Validation: Integrated Precipitation and Hydrology Experiment 2014 Science Plan",
                     "@type": "dcat:Distribution",
+                    "description": "NASA GPM-Ground Validation: Integrated Precipitation and Hydrology Experiment 2014 Science Plan",
+                    "downloadURL": "https://doi.org/10.7924/G8CC0XMR",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.1175/1520-0426(1997)014%3C0203:COSEIO%3E2.0.CO;2",
-                    "description": "Correction of Sampling Errors in Ocean Surface Cross-Sectional Estimates from Nadir-Looking Weather Radar",
                     "@type": "dcat:Distribution",
+                    "description": "Correction of Sampling Errors in Ocean Surface Cross-Sectional Estimates from Nadir-Looking Weather Radar",
+                    "downloadURL": "https://doi.org/10.1175/1520-0426(1997)014%3C0203:COSEIO%3E2.0.CO;2",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.sciencedirect.com/science/article/pii/S2225603218301358",
-                    "description": "An Introduction to the Nasa East Pacific Origins and Characteristics of Hurricanes (Epoch) Field Campaign",
                     "@type": "dcat:Distribution",
+                    "description": "An Introduction to the Nasa East Pacific Origins and Characteristics of Hurricanes (Epoch) Field Campaign",
+                    "downloadURL": "https://www.sciencedirect.com/science/article/pii/S2225603218301358",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.1175/1520-0426(1996)013%3C0795:TERSOT%3E2.0.CO;2",
-                    "description": "The EDOP Radar System on the High-Altitude NASA ER-2 Aircraft",
                     "@type": "dcat:Distribution",
+                    "description": "The EDOP Radar System on the High-Altitude NASA ER-2 Aircraft",
+                    "downloadURL": "https://doi.org/10.1175/1520-0426(1996)013%3C0795:TERSOT%3E2.0.CO;2",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.1175/1520-0450(2001)040%3C2080:TPRRPA%3E2.0.CO;2",
-                    "description": "TRMM Precipitation Radar Reflectivity Profiles as Compared with High-Resolution Airborne and Ground-Based Radar Measurements",
                     "@type": "dcat:Distribution",
+                    "description": "TRMM Precipitation Radar Reflectivity Profiles as Compared with High-Resolution Airborne and Ground-Based Radar Measurements",
+                    "downloadURL": "https://doi.org/10.1175/1520-0450(2001)040%3C2080:TPRRPA%3E2.0.CO;2",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/home/field-campaigns/epoch",
-                    "description": "EPOCH Field Campaign Project Home Page",
                     "@type": "dcat:Distribution",
+                    "description": "EPOCH Field Campaign Project Home Page",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/home/field-campaigns/epoch",
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
+            "identifier": "C2132312390-GHRC_DAAC",
+            "issued": "2021-09-23",
+            "keyword": [
+                "spectral/engineering",
+                "atmosphere",
+                "earth science",
+                "precipitation",
+                "radar"
+            ],
+            "landingPage": "https://doi.org/10.5067/EPOCH/EXRAD/DATA101",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2022-09-21",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/MSFC/GHRC"
+            },
             "spatial": "-124.717 16.603 -83.6115 34.9083",
+            "temporal": "2017-08-09T04:15:27Z/2017-08-31T15:57:21Z",
             "theme": [
                 "EPOCH",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "ER-2 X-Band Doppler Radar (EXRAD) EPOCH V1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1273348589-GES_DISC.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Waters, Joe W., et al.. 2001-01-09. UARML3AL. Version 005. UARS Microwave Limb Sounder (MLS) Level 3AL V005. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://disc.gsfc.nasa.gov/datacollection/UARML3AL_005.html. Digital Science Data.",
-            "issued": "1998-10-14",
-            "temporal": "1991-09-18T00:00:00Z/1999-07-27T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "1998-10-14",
-            "keyword": [
-                "altitude",
-                "atmospheric chemistry",
-                "atmospheric water vapor",
-                "earth science",
-                "atmosphere",
-                "atmospheric temperature"
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
-            "identifier": "C1273348589-GES_DISC",
-            "description": "The Microwave Limb Sounder (MLS) Level 3AL data product consists of daily, 4 degree increment latitude-ordered vertical profiles of temperature, geopotential height, concentrations of O3, H2O, CH3CN, ClO, HNO3, and SO2. The insrument measures in the microwave spectral region at frequencies of 63, 183 and 205 GHz. MLS was flown on NASA's Upper Atmosphere Research Satellite (UARS) and designed to measure the chemical composition of the stratosphere and mesosphere, relationship between chlorine monoxide and ozone destruction. Limb measurements were made in the altitude range between 10 and 85 km at about 2.5 km resolution. Data were collected between latitude 34S and 80N and 80S and 34N, alternating each satellite yaw cycle of about 36 days. The MLS Level 3AL data were processed with the version 5 algorithm, except SO2 which remained version 4. Note: H2O and O3 at 183 GHz data are available only through April 15, 1993 when the 183 GHz radiometer failed.\n\nThe MLS level 3AL product consists of 9 granules per day. A data granule is one MLS species or subtype per day.\n\nData are on the UARS standard pressure levels (in mbars) given by:\n\nP(i) = 1000 * 10**(-i/6)  for i = 0, 1, 2, ...\n\nEach of the 9 MLS granules is accompanied by an additional parameter file, designated as level 3LP. The parameter file, contains the additional ancillary and quality information, as well as total column amounts not found in the 3AL files. The data files are available in a binary record oriented format.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "UARML3AL",
             "creator": "Waters, Joe W., et al.",
-            "title": "UARS Microwave Limb Sounder (MLS) Level 3AL V005 (UARML3AL) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/UARML3AL_005.png",
-            "programCode": [
-                "026:001"
-            ],
+            "data-presentation-form": "Digital Science Data",
+            "description": "The Microwave Limb Sounder (MLS) Level 3AL data product consists of daily, 4 degree increment latitude-ordered vertical profiles of temperature, geopotential height, concentrations of O3, H2O, CH3CN, ClO, HNO3, and SO2. The insrument measures in the microwave spectral region at frequencies of 63, 183 and 205 GHz. MLS was flown on NASA's Upper Atmosphere Research Satellite (UARS) and designed to measure the chemical composition of the stratosphere and mesosphere, relationship between chlorine monoxide and ozone destruction. Limb measurements were made in the altitude range between 10 and 85 km at about 2.5 km resolution. Data were collected between latitude 34S and 80N and 80S and 34N, alternating each satellite yaw cycle of about 36 days. The MLS Level 3AL data were processed with the version 5 algorithm, except SO2 which remained version 4. Note: H2O and O3 at 183 GHz data are available only through April 15, 1993 when the 183 GHz radiometer failed.\n\nThe MLS level 3AL product consists of 9 granules per day. A data granule is one MLS species or subtype per day.\n\nData are on the UARS standard pressure levels (in mbars) given by:\n\nP(i) = 1000 * 10**(-i/6)  for i = 0, 1, 2, ...\n\nEach of the 9 MLS granules is accompanied by an additional parameter file, designated as level 3LP. The parameter file, contains the additional ancillary and quality information, as well as total column amounts not found in the 3AL files. The data files are available in a binary record oriented format.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -344081,96 +344056,135 @@
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/UARML3AL_005.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/UARML3AL_005.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/UARS_MLS_Level3/UARML3AL/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/UARS_MLS_Level3/UARML3AL/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=UARML3AL",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=UARML3AL",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://uars.gsfc.nasa.gov/",
-                    "description": "The UARS Project Homepage.",
                     "@type": "dcat:Distribution",
+                    "description": "The UARS Project Homepage.",
+                    "downloadURL": "https://uars.gsfc.nasa.gov/",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "application/msword",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/UARS_MLS_Level3/UARML3AL/doc/README.UARML3A.doc",
-                    "description": "README",
                     "@type": "dcat:Distribution",
+                    "description": "README",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/UARS_MLS_Level3/UARML3AL/doc/README.UARML3A.doc",
+                    "mediaType": "application/msword",
                     "title": "View this dataset's read me document"
                 }
             ],
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/UARML3AL_005.png",
+            "identifier": "C1273348589-GES_DISC",
+            "issued": "1998-10-14",
+            "keyword": [
+                "altitude",
+                "atmospheric chemistry",
+                "atmospheric water vapor",
+                "earth science",
+                "atmosphere",
+                "atmospheric temperature"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1273348589-GES_DISC.html",
+            "language": [
+                "en-US"
+            ],
+            "modified": "1998-10-14",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
+            },
+            "release-place": "Greenbelt, MD, USA",
+            "series-name": "UARML3AL",
             "spatial": "-180.0 -80.0 180.0 80.0",
+            "temporal": "1991-09-18T00:00:00Z/1999-07-27T23:59:59.999Z",
             "theme": [
                 "UARS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "UARS Microwave Limb Sounder (MLS) Level 3AL V005 (UARML3AL) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MGS-M-ACCEL-5-ALTITUDE-V1.1",
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
+            "description": "All ALTITUDE data are packaged by periapsis number for each aerobraking orbit. ALTITUDE data are provided in a table labeled Pyyyy.tab where 'yyyy' is the four digit periapsis number.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mgs-m-accel-5-altitude-v1.1_8689-5iix",
+            "issued": "2021-05-21",
+            "keyword": [
+                "mars global surveyor",
+                "mars"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MGS-M-ACCEL-5-ALTITUDE-V1.1",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mgs-m-accel-5-altitude-v1.1_8689-5iix",
-            "description": "All ALTITUDE data are packaged by periapsis number for each aerobraking orbit. ALTITUDE data are provided in a table labeled Pyyyy.tab where 'yyyy' is the four digit periapsis number.",
-            "title": "MGS ALTITUDE DATA RECORDS V1.1",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "MGS ALTITUDE DATA RECORDS V1.1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.nasa.gov/d/869n-2mc7",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "GeneLab Outreach",
+                "hasEmail": "mailto:genelab-outreach@lists.nasa.gov"
+            },
+            "description": "A recent physiological study established that hindlimb unloading of rats at 3 and 7 weeks inhibits healing of injured ligaments resulting in a badly aligned discontinuous collagen matrix. Using tissue from these rats we focused on the 3-week time point employing microarray analysis to identify what cellular processes or lack of processes could account for these observed deficiencies. We used the Affymetrix RG_U34A GeneChip and performed image analysis with Microarray Suite 5.0. For normalization we used the MAS global normalization protocol with a default target mean signal of 500. Gene expression in medial collateral ligament tissue under 4 different treatment conditions was measured: loaded control loaded wound healing unloaded control and unloaded wound healing. From our results it appears that unloaded tissue lags behind loaded tissue in its progression through the healing process and at 3 weeks is still engaged in the proliferative phase whereas loaded tissue is actively remodeling its collagen matrix.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "GeneLab Study Page",
+                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-19",
+                    "mediaType": "text/html",
+                    "title": "Transcription profiling of rat to study the effect of hindlimb unloading on healing of medial collateral ligaments 3 weeks after injury"
+                }
+            ],
+            "identifier": "nasa_genelab_GLDS-19_869n-2mc7",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
             "keyword": [
                 "genelab microarray data processing protocol",
                 "p-affy-6",
@@ -344182,555 +344196,550 @@
                 "treatment protocol",
                 "feature_extraction"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "GeneLab Outreach",
-                "hasEmail": "mailto:genelab-outreach@lists.nasa.gov"
-            },
+            "landingPage": "https://data.nasa.gov/d/869n-2mc7",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "nasa_genelab_GLDS-19_869n-2mc7",
-            "description": "A recent physiological study established that hindlimb unloading of rats at 3 and 7 weeks inhibits healing of injured ligaments resulting in a badly aligned discontinuous collagen matrix. Using tissue from these rats we focused on the 3-week time point employing microarray analysis to identify what cellular processes or lack of processes could account for these observed deficiencies. We used the Affymetrix RG_U34A GeneChip and performed image analysis with Microarray Suite 5.0. For normalization we used the MAS global normalization protocol with a default target mean signal of 500. Gene expression in medial collateral ligament tissue under 4 different treatment conditions was measured: loaded control loaded wound healing unloaded control and unloaded wound healing. From our results it appears that unloaded tissue lags behind loaded tissue in its progression through the healing process and at 3 weeks is still engaged in the proliferative phase whereas loaded tissue is actively remodeling its collagen matrix.",
-            "title": "Transcription profiling of rat to study the effect of hindlimb unloading on healing of medial collateral ligaments 3 weeks after injury",
-            "programCode": [
-                "026:005"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-19",
-                    "description": "GeneLab Study Page",
-                    "@type": "dcat:Distribution",
-                    "title": "Transcription profiling of rat to study the effect of hindlimb unloading on healing of medial collateral ligaments 3 weeks after injury"
-                }
-            ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "Transcription profiling of rat to study the effect of hindlimb unloading on healing of medial collateral ligaments 3 weeks after injury"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-3-RDR-SAWYER-ASTEROID-SPECTRA-V1.0",
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
+            "description": "This data set contains 94 asteroid spectra obtained by Scott Sawyer as part of his Ph.D. dissertation at the University of Texas at Austin.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-3-rdr-sawyer-asteroid-spectra-v1.0_869x-fp38",
+            "issued": "2021-05-21",
+            "keyword": [
+                "asteroid",
+                "support archives"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-3-RDR-SAWYER-ASTEROID-SPECTRA-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-3-rdr-sawyer-asteroid-spectra-v1.0_869x-fp38",
-            "description": "This data set contains 94 asteroid spectra obtained by Scott Sawyer as part of his Ph.D. dissertation at the University of Texas at Austin.",
-            "title": "SAWYER ASTEROID SPECTRA V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "SAWYER ASTEROID SPECTRA V1.0"
         },
         {
-            "accessLevel": "public",
-            "bureauCode": [
-                "026:00"
-            ],
-            "landingPage": "https://c3.nasa.gov/dashlink/resources/164/",
-            "issued": "2010-09-22",
             "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
-            "keyword": [
-                "dashlink",
-                "nasa",
-                "ames"
+            "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "026:00"
             ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ashok Srivastava",
                 "hasEmail": "mailto:ashok.n.srivastava@gmail.com"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Dashlink"
-            },
-            "identifier": "DASHLINK_164",
             "description": "NASA has some of the largest and most complex data sources in the world, with data sources ranging from the earth sciences, space sciences, and massive distributed engineering data sets from commercial aircraft and spacecraft. This talk will discuss some of the issues and algorithms developed to analyze and discover patterns in these data sets. We will also provide an overview of a large research program in Integrated Vehicle Health Management. The goal of this program is to develop advanced technologies to automatically detect, diagnose, predict, and mitigate adverse events during the flight of an aircraft. A case study will be presented on a recent data mining analysis performed to support the Flight Readiness Review of the Space Shuttle Mission STS-119.",
-            "title": "Data Mining at NASA: From Theory to Applications",
+            "identifier": "DASHLINK_164",
+            "issued": "2010-09-22",
+            "keyword": [
+                "dashlink",
+                "nasa",
+                "ames"
+            ],
+            "landingPage": "https://c3.nasa.gov/dashlink/resources/164/",
+            "modified": "2020-01-29",
             "programCode": [
                 "026:029"
             ],
-            "accrualPeriodicity": "irregular"
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Dashlink"
+            },
+            "title": "Data Mining at NASA: From Theory to Applications"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/S6AGN-1PODH",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Ocean Surface Topography Science Team. 2021-06-22. Sentinel-6A MF Jason-CS L1B GNSS-POD Tracking Data Hourly. Version F. PO.DAAC. Archived by National Aeronautics and Space Administration, U.S. Government, PO.DAAC. https://doi.org/10.5067/S6AGN-1PODH.",
-            "issued": "2020-11-26",
-            "temporal": "2020-11-26T12:47:28.213Z/2023-04-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-04-13",
-            "references": [
-                "https://doi.org/10.1016/j.rse.2021.112395"
-            ],
-            "keyword": [
-                "solid earth",
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
-            "identifier": "C1968979643-POCLOUD",
-            "description": "Provides L1B hourly GNSS-POD tracking data for the Sentinel-6A radar altimetry mission.",
-            "release-place": "PO.DAAC",
-            "graphic-preview-description": "Thumbnail image for Website",
             "creator": "Ocean Surface Topography Science Team",
-            "title": "Sentinel-6A MF Jason-CS L1B GNSS-POD Tracking Data Hourly",
-            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/JASON_CS_S6A_L1B_GNSS_POD_HOURLY.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "Provides L1B hourly GNSS-POD tracking data for the Sentinel-6A radar altimetry mission.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FS6AGN-1PODH",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FS6AGN-1PODH",
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
-                    "downloadURL": "https://podaac.jpl.nasa.gov/dataset/JASON_CS_S6A_L1B_GNSS_POD_HOURLY",
-                    "description": "Data Set Landing Page",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Landing Page",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/dataset/JASON_CS_S6A_L1B_GNSS_POD_HOURLY",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/JASON_CS_S6A_L1B_GNSS_POD_HOURLY.jpg",
-                    "description": "Thumbnail image for Website",
                     "@type": "dcat:Distribution",
+                    "description": "Thumbnail image for Website",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/JASON_CS_S6A_L1B_GNSS_POD_HOURLY.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C1968979643-POCLOUD",
-                    "description": "HTTPS endpoint for data browse and download",
                     "@type": "dcat:Distribution",
+                    "description": "HTTPS endpoint for data browse and download",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C1968979643-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1968979643-POCLOUD",
-                    "description": "Browse granule search results in Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse granule search results in Earthdata Search",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1968979643-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 }
             ],
+            "graphic-preview-description": "Thumbnail image for Website",
+            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/JASON_CS_S6A_L1B_GNSS_POD_HOURLY.jpg",
+            "identifier": "C1968979643-POCLOUD",
+            "issued": "2020-11-26",
+            "keyword": [
+                "solid earth",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/S6AGN-1PODH",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2023-04-13",
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
+            "temporal": "2020-11-26T12:47:28.213Z/2023-04-17T00:00:00Z",
             "theme": [
                 "Sentinel-6",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Sentinel-6A MF Jason-CS L1B GNSS-POD Tracking Data Hourly"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/SeaBASS/GULFOFMAINE/DATA001",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/GSFC/SED/ESD/GCDC/OB.DAAC. https://doi.org/10.5067/SeaBASS/GULFOFMAINE/DATA001.",
-            "issued": "2008-09-16",
-            "temporal": "2008-09-16T00:00:02Z/2023-04-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-04-06",
-            "keyword": [
-                "salinity/density",
-                "ocean temperature",
-                "ocean optics",
-                "oceans",
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
-            "identifier": "C1633360355-OB_DAAC",
             "description": "Measurements from the Gulf Of Maine during 2008 and 2009.",
-            "title": "Measurements from the Gulf Of Maine during 2008 and 2009",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSeaBASS%2FGULFOFMAINE%2FDATA001",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSeaBASS%2FGULFOFMAINE%2FDATA001",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://seabass.gsfc.nasa.gov/experiment/GulfOfMaine/",
-                    "description": "Detailed information about the SeaBASS Experiment such as cruises, funding, and investigators",
                     "@type": "dcat:Distribution",
+                    "description": "Detailed information about the SeaBASS Experiment such as cruises, funding, and investigators",
+                    "downloadURL": "https://seabass.gsfc.nasa.gov/experiment/GulfOfMaine/",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 }
             ],
+            "identifier": "C1633360355-OB_DAAC",
+            "issued": "2008-09-16",
+            "keyword": [
+                "salinity/density",
+                "ocean temperature",
+                "ocean optics",
+                "oceans",
+                "earth science",
+                "ocean chemistry"
+            ],
+            "landingPage": "https://doi.org/10.5067/SeaBASS/GULFOFMAINE/DATA001",
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
+            "temporal": "2008-09-16T00:00:02Z/2023-04-17T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Measurements from the Gulf Of Maine during 2008 and 2009"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/AURA/TES/TESH2OLS_L2.006",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "The data used in this study were produced by the TES Science Team at the TES SIPS and archived at the Langley DAAC. See ProductionDateTime for Published date.",
-            "issued": "2013-03-29",
-            "temporal": "2004-07-15T00:00:00Z/2022-01-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2015-10-28",
-            "keyword": [
-                "atmosphere",
-                "atmospheric temperature",
-                "atmospheric water vapor",
-                "earth science"
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
-            "identifier": "C191856312-LARC",
             "description": "Atmospheric vertical profile estimates and associated errors (diagonals and covariance matrices), along with retrieved surface temperature, cloud effective optical depth, column estimates, quality flags, averaging kernels and a priori constraint vectors.",
-            "title": "TES/Aura L2 H2O Limb Special Observation V006",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAURA%2FTES%2FTESH2OLS_L2.006",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAURA%2FTES%2FTESH2OLS_L2.006",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 }
             ],
+            "identifier": "C191856312-LARC",
+            "issued": "2013-03-29",
+            "keyword": [
+                "atmosphere",
+                "atmospheric temperature",
+                "atmospheric water vapor",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/AURA/TES/TESH2OLS_L2.006",
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
+            "title": "TES/Aura L2 H2O Limb Special Observation V006"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/XTPEDYJ62GGN",
             "citation": "Kevin W. Bowman. 2021-05-27. TRPSDL2HDOCRSFS. Version 1. TROPESS CrIS-SNPP L2 Deuterated Water Vapor for Forward Stream, Standard Product V1. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/XTPEDYJ62GGN. https://disc.gsfc.nasa.gov/datacollection/TRPSDL2HDOCRSFS_1.html. Digital Science Data.",
-            "issued": "2021-05-18",
-            "temporal": "2021-02-01T00:00:00Z/2021-05-21T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2021-05-18",
-            "references": [
-                "https://doi.org/10.1126/sciadv.abf7460",
-                "https://doi.org/10.5194/amt-13-1825-2020",
-                "https://doi.org/10.1109/TGRS.2006.871234",
-                "https://doi.org/10.1029/2002JD002299",
-                "https://doi.org/10.5194/amt-5-397-2012",
-                "https://doi.org/10.1029/2005JD006606",
-                "https://doi.org/10.1029/2011JD016621",
-                "https://doi.org/10.1002/wrcr.20312"
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
-            "identifier": "C2041965312-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "The TROPESS CrIS-SNPP L2 Deuterated Water Vapor for Forward Stream, Standard Product contains the vertical distribution of the retrieved atmospheric state of semi-heavy water (HDO), formal uncertainties, and diagnostic information measured by the CrIS instrument on the Suomi-NPP satellite. The forward stream standard product is global for the time period from 2021-02-01 to 2021-05-21, when the CrIS-SNPP processing was discontinued. The NASA TRopospheric Ozone and Precursors from Earth System Sounding (TROPESS) project, uses an optimal estimation algorithm, known as the MUlti-SpEctra, MUlti-SpEcies, Multi-SEnsors (MUSES).\n\nThe data files are written in the netCDF version 4 file format, and each file contains one day of data. The data have a spatial resolution of 14 km (CrIS nadir FOV), and are reported at 17 vertical levels from the surface to 0.1 hPa. The principal investigator for the TROPESS project is Kevin W. Bowman.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "TRPSDL2HDOCRSFS",
-            "creator": "Kevin W. Bowman",
-            "graphic-preview-description": "TROPESS CrIS-SNPP HDO (Forward Stream, Standard Product) at 681 hPa on 01 April 2021.",
-            "title": "TROPESS CrIS-SNPP L2 Deuterated Water Vapor for Forward Stream, Standard Product V1 (TRPSDL2HDOCRSFS) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TROPESS/images/TRPSDL2HDOCRSFS_Sample.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FXTPEDYJ62GGN",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FXTPEDYJ62GGN",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TROPESS/images/TRPSDL2HDOCRSFS_Sample.png",
-                    "description": "TROPESS CrIS-SNPP HDO (Forward Stream, Standard Product) at 681 hPa on 01 April 2021.",
                     "@type": "dcat:Distribution",
+                    "description": "TROPESS CrIS-SNPP HDO (Forward Stream, Standard Product) at 681 hPa on 01 April 2021.",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TROPESS/images/TRPSDL2HDOCRSFS_Sample.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/TRPSDL2HDOCRSFS_1.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/TRPSDL2HDOCRSFS_1.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/data/TROPESS_Standard/TRPSDL2HDOCRSFS.1/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/data/TROPESS_Standard/TRPSDL2HDOCRSFS.1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=TRPSDL2HDOCRSFS_1",
-                    "description": "Use the Earthdata Search Client to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search Client to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=TRPSDL2HDOCRSFS_1",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/opendap/TROPESS_Standard/TRPSDL2HDOCRSFS.1/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/opendap/TROPESS_Standard/TRPSDL2HDOCRSFS.1/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/data/TROPESS_Standard/TRPSDL2HDOCRSFS.1/doc/TROPESS_Forward_Stream_README.pdf",
-                    "description": "README Document",
                     "@type": "dcat:Distribution",
+                    "description": "README Document",
+                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/data/TROPESS_Standard/TRPSDL2HDOCRSFS.1/doc/TROPESS_Forward_Stream_README.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's read me document"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TROPESS/User_Guides/TROPESS-AIRS-HDO_L2_Product_User_Guide_20201102.pdf",
-                    "description": "User's Guide",
                     "@type": "dcat:Distribution",
+                    "description": "User's Guide",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TROPESS/User_Guides/TROPESS-AIRS-HDO_L2_Product_User_Guide_20201102.pdf",
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
+            "graphic-preview-description": "TROPESS CrIS-SNPP HDO (Forward Stream, Standard Product) at 681 hPa on 01 April 2021.",
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TROPESS/images/TRPSDL2HDOCRSFS_Sample.png",
+            "identifier": "C2041965312-GES_DISC",
+            "issued": "2021-05-18",
+            "keyword": [
+                "atmosphere",
+                "earth science",
+                "atmospheric chemistry"
+            ],
+            "landingPage": "https://doi.org/10.5067/XTPEDYJ62GGN",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2021-05-18",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
+            },
+            "references": [
+                "https://doi.org/10.1126/sciadv.abf7460",
+                "https://doi.org/10.5194/amt-13-1825-2020",
+                "https://doi.org/10.1109/TGRS.2006.871234",
+                "https://doi.org/10.1029/2002JD002299",
+                "https://doi.org/10.5194/amt-5-397-2012",
+                "https://doi.org/10.1029/2005JD006606",
+                "https://doi.org/10.1029/2011JD016621",
+                "https://doi.org/10.1002/wrcr.20312"
+            ],
+            "release-place": "Greenbelt, MD, USA",
+            "series-name": "TRPSDL2HDOCRSFS",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2021-02-01T00:00:00Z/2021-05-21T23:59:59.999Z",
             "theme": [
                 "TROPESS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "TROPESS CrIS-SNPP L2 Deuterated Water Vapor for Forward Stream, Standard Product V1 (TRPSDL2HDOCRSFS) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/SeaBASS/JGOFS_BOFS/DATA001",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/GSFC/SED/ESD/GCDC/OB.DAAC. https://doi.org/10.5067/SeaBASS/JGOFS_BOFS/DATA001.",
-            "issued": "1991-06-19",
-            "temporal": "1991-06-19T00:00:02Z/2023-04-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-04-06",
-            "keyword": [
-                "ocean chemistry",
-                "ocean optics",
-                "ocean temperature",
-                "oceans",
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
-            "identifier": "C1633360385-OB_DAAC",
             "description": "Joint Global Ocean Flux Study (JGOFS)  measurements taken by Germany, The Netherlands, and the United Kingdom from 1991.",
-            "title": "Joint Global Ocean Flux Study (JGOFS) Arabian Sea measurements - Biogeochemical Ocean Flux Study (BOFS)",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSeaBASS%2FJGOFS_BOFS%2FDATA001",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSeaBASS%2FJGOFS_BOFS%2FDATA001",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://seabass.gsfc.nasa.gov/experiment/JGOFS_BOFS/",
-                    "description": "Detailed information about the SeaBASS Experiment such as cruises, funding, and investigators",
                     "@type": "dcat:Distribution",
+                    "description": "Detailed information about the SeaBASS Experiment such as cruises, funding, and investigators",
+                    "downloadURL": "https://seabass.gsfc.nasa.gov/experiment/JGOFS_BOFS/",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 }
             ],
+            "identifier": "C1633360385-OB_DAAC",
+            "issued": "1991-06-19",
+            "keyword": [
+                "ocean chemistry",
+                "ocean optics",
+                "ocean temperature",
+                "oceans",
+                "salinity/density",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/SeaBASS/JGOFS_BOFS/DATA001",
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
+            "temporal": "1991-06-19T00:00:02Z/2023-04-17T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Joint Global Ocean Flux Study (JGOFS) Arabian Sea measurements - Biogeochemical Ocean Flux Study (BOFS)"
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
+                    "downloadURL": "http://turbmodels.larc.nasa.gov/Other_exp_Data/Coanda/Cmu_0.114_Chordwise_Pressures.dat",
+                    "mediaType": "application/dat"
+                }
             ],
+            "identifier": "NASA-851__7",
+            "issued": "2018-06-25",
             "keyword": [
                 "tangential",
                 "turbulence",
@@ -344742,108 +344751,74 @@
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
-            "identifier": "NASA-851__7",
-            "description": "2-D Coanda Airfoil with Tangential Wall Jet. This web page provides data from experiments that may be useful for the validation of turbulence models. This resource is expected to grow gradually over time. All data herein arepublicly available.",
-            "title": "Turbulence Models: Data from Other Experiments: 2-D Coanda Airfoil with Tangential Wall Jet",
-            "programCode": [
-                "026:023"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://turbmodels.larc.nasa.gov/Other_exp_Data/Coanda/Cmu_0.114_Chordwise_Pressures.dat",
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
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-A-SDC-2-KEM1-V3.0",
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
-                "new horizons kuiper belt extended mission",
-                "dust"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This data set contains Raw data taken by the New Horizons Student Dust Counter instrument during the KEM1 ENCOUNTER mission phase. This is VERSION 3.0 of this data set. This data set contains data acquired by the spacecraft between 08/14/2018 and 07/31/2019. It only includes data downlinked before 08/01/2019. Future datasets may include more data acquired by the spacecraft after 08/13/2018 but downlinked after 07/31/2019.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-a-sdc-2-kem1-v3.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "new horizons kuiper belt extended mission",
+                "dust"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-A-SDC-2-KEM1-V3.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-a-sdc-2-kem1-v3.0",
-            "description": "This data set contains Raw data taken by the New Horizons Student Dust Counter instrument during the KEM1 ENCOUNTER mission phase. This is VERSION 3.0 of this data set. This data set contains data acquired by the spacecraft between 08/14/2018 and 07/31/2019. It only includes data downlinked before 08/01/2019. Future datasets may include more data acquired by the spacecraft after 08/13/2018 but downlinked after 07/31/2019.",
-            "title": "NEW HORIZONS\n      SDC KEM1\n      RAW V3.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "NEW HORIZONS\n      SDC KEM1\n      RAW V3.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1282248333-GES_DISC.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Tropical Rainfall Measuring Mission (TRMM). 2011-07-01. TRMM_1A11. TRMM Attitude and TMI Packets and Header Record L1A V7. Greenbelt, MD. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://disc.gsfc.nasa.gov/datacollection/TRMM_1A11_7.html.",
-            "issued": "2011-07-01",
-            "temporal": "1997-12-07T00:00:00Z/2015-04-08T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2016-04-20",
-            "keyword": [
-                "platform characteristics",
-                "earth science",
-                "sensor characteristics",
-                "visible wavelengths",
-                "infrared wavelengths",
-                "spectral/engineering"
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
-            "identifier": "C1282248333-GES_DISC",
-            "description": "The Level-1A Product file, \"1A11\", is a concatenation of Header record, Spacecraft Attitude packets, TMI Housekeeping packets, TMI Science Data packets, QACs and an MDUL. As such, it is reversible to Level 0. The header record contains information pertaining to orbit times, orbit number, times of the first scan, and number of scans, among other things. The Level 0 data contain the actual channel data expressed as\"sensor counts\". A Level 1A file contains data for a single orbit and has a file size of about 31 MB (uncompressed). \n\nSpatial coverage is between 38 degrees North and 38 degrees South owing to the 35 degree inclination of the TRMM satellite. This orbit provides extensive coverage in the tropics and allows each location to be covered at a different local time each day, enabling the analysis of the diurnal cycle of precipitation.",
-            "release-place": "Greenbelt, MD",
-            "series-name": "TRMM_1A11",
             "creator": "Tropical Rainfall Measuring Mission (TRMM)",
-            "title": "TRMM Attitude and TMI Packets and Header Record L1A V7 (TRMM_1A11) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/TRMM_1A11_7.png",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The Level-1A Product file, \"1A11\", is a concatenation of Header record, Spacecraft Attitude packets, TMI Housekeeping packets, TMI Science Data packets, QACs and an MDUL. As such, it is reversible to Level 0. The header record contains information pertaining to orbit times, orbit number, times of the first scan, and number of scans, among other things. The Level 0 data contain the actual channel data expressed as\"sensor counts\". A Level 1A file contains data for a single orbit and has a file size of about 31 MB (uncompressed). \n\nSpatial coverage is between 38 degrees North and 38 degrees South owing to the 35 degree inclination of the TRMM satellite. This orbit provides extensive coverage in the tropics and allows each location to be covered at a different local time each day, enabling the analysis of the diurnal cycle of precipitation.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -344852,764 +344827,791 @@
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/TRMM_1A11_7.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/TRMM_1A11_7.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc2.gesdisc.eosdis.nasa.gov/data/TRMM_L1A/TRMM_1A11.7",
-                    "description": "Access the data via HTTPS",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS",
+                    "downloadURL": "https://disc2.gesdisc.eosdis.nasa.gov/data/TRMM_L1A/TRMM_1A11.7",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=TRMM_1A11",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=TRMM_1A11",
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
-                    "downloadURL": "https://disc2.gesdisc.eosdis.nasa.gov/data/TRMM_L1/TRMM_1B01/doc/README.TRMM_V7.pdf",
-                    "description": "README Document",
                     "@type": "dcat:Distribution",
+                    "description": "README Document",
+                    "downloadURL": "https://disc2.gesdisc.eosdis.nasa.gov/data/TRMM_L1/TRMM_1B01/doc/README.TRMM_V7.pdf",
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
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/TRMM_1A11_7.png",
+            "identifier": "C1282248333-GES_DISC",
+            "issued": "2011-07-01",
+            "keyword": [
+                "platform characteristics",
+                "earth science",
+                "sensor characteristics",
+                "visible wavelengths",
+                "infrared wavelengths",
+                "spectral/engineering"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1282248333-GES_DISC.html",
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
+            "series-name": "TRMM_1A11",
             "spatial": "-180.0 -38.0 180.0 38.0",
+            "temporal": "1997-12-07T00:00:00Z/2015-04-08T23:59:59.999Z",
             "theme": [
                 "TRMM",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "TRMM Attitude and TMI Packets and Header Record L1A V7 (TRMM_1A11) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-EXT1-1392-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the ROSETTA EXTENSION 1 phase 2016-01-01 to 2016-04-05. It is a Global Gravity measurement at the comet 67P and covers the time 2016-02-02T20:04:40.000 to 2016-02-02T22:06:57.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-ext1-1392-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-EXT1-1392-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-ext1-1392-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the ROSETTA EXTENSION 1 phase 2016-01-01 to 2016-04-05. It is a Global Gravity measurement at the comet 67P and covers the time 2016-02-02T20:04:40.000 to 2016-02-02T22:06:57.000.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     ROSETTA EXTENSION 1 1392 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     ROSETTA EXTENSION 1 1392 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ECTSS-SBO44",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "ECCO Consortium, Fukumori, I., Wang, O., Fenty, I., Forget, G., Heimbach, P., & Ponte, R. M.. 2021-04-19. ECCO SBO Core Products - Snapshot (Version 4 Release 4). Version V4r4. PO.DAAC. Archived by National Aeronautics and Space Administration, U.S. Government, PO.DAAC. https://doi.org/10.5067/ECTSS-SBO44. ECCO; ECCO Consortium, Fukumori, I., Wang, O., Fenty, I., Forget, G., Heimbach, P., & Ponte, R. M.; 2020; ECCO SBO Core Products - Snapshot (Version 4 Release 4); 10.5067/ECTSS-SBO44; https://podaac.jpl.nasa.gov/ECCO.",
-            "issued": "2021-01-01",
-            "temporal": "1992-01-01T00:00:00Z/2018-01-01T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2018-01-01",
-            "references": [
-                "https://doi.org/10.5281/zenodo.3765928"
-            ],
-            "keyword": [
-                "oceans",
-                "earth science services",
-                "models",
-                "ocean circulation",
-                "earth science",
-                "earth science reanalyses/assimilation models"
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
-            "identifier": "C1991543766-POCLOUD",
-            "description": "This dataset provides instantaneous hourly SBO core products from the ECCO Version 4 Release 4 (V4r4) ocean and sea-ice state estimate. Estimating the Circulation and Climate of the Ocean (ECCO) ocean and sea-ice state estimates are dynamically and kinematically-consistent reconstructions of the three-dimensional time-evolving ocean, sea-ice, and surface atmospheric states. ECCO V4r4 is a free-running solution of the 1-degree global configuration of the MIT general circulation model (MITgcm) that has been fit to observations in a least-squares sense. Observational data constraints used in V4r4 include sea surface height and model sea level anomaly (SSH) from satellite altimeters [ERS-1/2, TOPEX/Poseidon, GFO, ENVISAT, Jason-1,2,3, CryoSat-2, and SARAL/AltiKa]; sea surface temperature (SST) from satellite radiometers [AVHRR], sea surface salinity (SSS) from the Aquarius satellite radiometer/scatterometer, ocean bottom pressure (OBP) from the GRACE satellite gravimeter; sea ice concentration from satellite radiometers [SSM/I and SSMIS], and in-situ ocean temperature and salinity measured with conductivity-temperature-depth (CTD) sensors and expendable bathythermographs (XBTs) from several programs [e.g., WOCE, GO-SHIP, Argo, and others] and platforms [e.g., research vessels, gliders, moorings, ice-tethered profilers, and instrumented pinnipeds]. V4r4 covers the period 1992-01-01T12:00:00 to 2018-01-01T00:00:00.",
-            "release-place": "PO.DAAC",
-            "graphic-preview-description": "Thumbnail image for Website",
             "creator": "ECCO Consortium, Fukumori, I., Wang, O., Fenty, I., Forget, G., Heimbach, P., & Ponte, R. M.",
-            "title": "ECCO SBO Core Products - Snapshot (Version 4 Release 4)",
-            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/ECCO_L4_SBO_CORE_TIME_SERIES_SNAPSHOT_V4R4.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "This dataset provides instantaneous hourly SBO core products from the ECCO Version 4 Release 4 (V4r4) ocean and sea-ice state estimate. Estimating the Circulation and Climate of the Ocean (ECCO) ocean and sea-ice state estimates are dynamically and kinematically-consistent reconstructions of the three-dimensional time-evolving ocean, sea-ice, and surface atmospheric states. ECCO V4r4 is a free-running solution of the 1-degree global configuration of the MIT general circulation model (MITgcm) that has been fit to observations in a least-squares sense. Observational data constraints used in V4r4 include sea surface height and model sea level anomaly (SSH) from satellite altimeters [ERS-1/2, TOPEX/Poseidon, GFO, ENVISAT, Jason-1,2,3, CryoSat-2, and SARAL/AltiKa]; sea surface temperature (SST) from satellite radiometers [AVHRR], sea surface salinity (SSS) from the Aquarius satellite radiometer/scatterometer, ocean bottom pressure (OBP) from the GRACE satellite gravimeter; sea ice concentration from satellite radiometers [SSM/I and SSMIS], and in-situ ocean temperature and salinity measured with conductivity-temperature-depth (CTD) sensors and expendable bathythermographs (XBTs) from several programs [e.g., WOCE, GO-SHIP, Argo, and others] and platforms [e.g., research vessels, gliders, moorings, ice-tethered profilers, and instrumented pinnipeds]. V4r4 covers the period 1992-01-01T12:00:00 to 2018-01-01T00:00:00.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FECTSS-SBO44",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FECTSS-SBO44",
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
-                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/ECCO_L4_SBO_CORE_TIME_SERIES_SNAPSHOT_V4R4.jpg",
-                    "description": "Thumbnail image for Website",
                     "@type": "dcat:Distribution",
+                    "description": "Thumbnail image for Website",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/ECCO_L4_SBO_CORE_TIME_SERIES_SNAPSHOT_V4R4.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/ECTSS-SBO44",
-                    "description": "Access the data set landing page for the collection.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data set landing page for the collection.",
+                    "downloadURL": "https://doi.org/10.5067/ECTSS-SBO44",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1991543766-POCLOUD",
-                    "description": "Browse granule search results in Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse granule search results in Earthdata Search",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1991543766-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C1991543766-POCLOUD/temporal",
-                    "description": "Browse and download granules over HTTPS using the virtual directories service",
                     "@type": "dcat:Distribution",
+                    "description": "Browse and download granules over HTTPS using the virtual directories service",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C1991543766-POCLOUD/temporal",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 }
             ],
+            "graphic-preview-description": "Thumbnail image for Website",
+            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/ECCO_L4_SBO_CORE_TIME_SERIES_SNAPSHOT_V4R4.jpg",
+            "identifier": "C1991543766-POCLOUD",
+            "issued": "2021-01-01",
+            "keyword": [
+                "oceans",
+                "earth science services",
+                "models",
+                "ocean circulation",
+                "earth science",
+                "earth science reanalyses/assimilation models"
+            ],
+            "landingPage": "https://doi.org/10.5067/ECTSS-SBO44",
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
+            "title": "ECCO SBO Core Products - Snapshot (Version 4 Release 4)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/5SZA7GSQI0YT",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "CryoSat-2 Level-1B Waveforms, Sea Ice Elevation, and Surface Roughness V001. Version 1. Archived by National Aeronautics and Space Administration, U.S. Government, NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/5SZA7GSQI0YT.",
-            "issued": "2010-09-15",
-            "temporal": "2010-09-15T00:00:00Z/2025-01-27T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-12-18",
-            "keyword": [
-                "earth science",
-                "cryosphere",
-                "sea ice",
-                "land surface",
-                "topography"
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
-            "identifier": "C1454786108-NSIDC_ECS",
             "description": "This data set contains surface elevations from retracked CryoSat-2 waveforms, as well as model fitting parameters used to retrack the waveform. The primary data set used in the production of these data come from the ESA CryoSat-2 satellite.",
-            "title": "CryoSat-2 Level-1B Waveforms, Sea Ice Elevation, and Surface Roughness V001",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2F5SZA7GSQI0YT",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2F5SZA7GSQI0YT",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://nsidc.org/icebridge/portal/",
-                    "description": "Tool to visualize, search, and download IceBridge data.",
                     "@type": "dcat:Distribution",
+                    "description": "Tool to visualize, search, and download IceBridge data.",
+                    "downloadURL": "http://nsidc.org/icebridge/portal/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/ICEBRIDGE/RDWES1B.001/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/ICEBRIDGE/RDWES1B.001/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=RDWES1B+V001",
-                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=RDWES1B+V001",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/data/data-access-tool/RDWES1B/versions/1/",
-                    "description": "Search and filter data files using a map-based interface",
                     "@type": "dcat:Distribution",
+                    "description": "Search and filter data files using a map-based interface",
+                    "downloadURL": "https://nsidc.org/data/data-access-tool/RDWES1B/versions/1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/5SZA7GSQI0YT",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/5SZA7GSQI0YT",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/5SZA7GSQI0YT",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/5SZA7GSQI0YT",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C1454786108-NSIDC_ECS",
+            "issued": "2010-09-15",
+            "keyword": [
+                "earth science",
+                "cryosphere",
+                "sea ice",
+                "land surface",
+                "topography"
+            ],
+            "landingPage": "https://doi.org/10.5067/5SZA7GSQI0YT",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2024-12-18",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA NSIDC DAAC"
+            },
             "spatial": "-180.0 55.0 180.0 90.0",
+            "temporal": "2010-09-15T00:00:00Z/2025-01-27T00:00:00Z",
             "theme": [
                 "MULTI_NASA",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "CryoSat-2 Level-1B Waveforms, Sea Ice Elevation, and Surface Roughness V001"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/GHMDT-2PJ19",
             "citation": "JPL/OBPG/RSMAS. 2020-01-15. GHRSST Level 2P Global Sea Surface Skin Temperature from the Moderate Resolution Imaging Spectroradiometer (MODIS) on NASA Terra. Version 2019.0. MODIS Terra L2P swath SST data set. Jet Propulsion Laboratory, CA, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Jet Propulsion Laboratory. https://doi.org/10.5067/GHMDT-2PJ19. JPL/OBPG/RSMAS, Jet Propulsion Laboratory, 2020-01-15, GHRSST Level 2P Global Sea Surface Skin Temperature from the Moderate Resolution Imaging Spectroradiometer (MODIS) on the NASA Terra satellite (GDS2), Information on the the MODIS SST algorithm can be found in the following documents: http://modis.gsfc.nasa.gov/data/atbd/atbd_mod25.pdf and http://oceancolor.gsfc.nasa.gov/DOCS/modis_sst/.",
-            "issued": "2019-12-31",
-            "temporal": "2000-02-24T00:00:00Z/2023-03-01T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2019-12-31",
-            "references": [
-                "http://dx.doi.org/10.1016/j.rse.2015.04.023"
-            ],
-            "keyword": [
-                "ngda",
-                "ocean temperature",
-                "oceans",
-                "earth science",
-                "national geospatial data asset"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "undefined",
                 "hasEmail": "mailto:cmr-support@earthdata.nasa.gov"
             },
-            "identifier": "C1940475563-POCLOUD",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/JPL/PODAAC"
-            },
-            "description": "NASA produces skin sea surface temperature (SST) products from the Infrared (IR) channels of the Moderate-resolution Imaging Spectroradiometer (MODIS) onboard the Terra satellite. Terra was launched by NASA on December 18, 1999, into a sun synchronous, polar orbit with a daylight descending node at 10:30 am, to study the global dynamics of the Earth atmosphere, land and oceans. The MODIS captures data in 36 spectral bands at a variety of spatial resolutions.  Two SST products can be present in these files. The first is a skin SST produced for both day and night observations, derived from the long wave IR 11 and 12 micron wavelength channels, using a modified nonlinear SST algorithm intended to provide continuity with SST derived from heritage and current NASA sensors. At night, a second SST product is produced using the mid-infrared 3.95 and 4.05 micron channels which are unique to MODIS; the SST derived from these measurements is identified as SST4. The SST4 product has lower uncertainty, but due to sun glint can only be produced at night. MODIS L2P SST data have a 1 km spatial resolution at nadir and are stored in 288 five minute granules per day. Full global coverage is obtained every two days, with coverage poleward of 32.3 degree being complete each day. The production of MODIS L2P SST files is part of the Group for High Resolution Sea Surface Temperature (GHRSST) project, and is a joint collaboration between the NASA Jet Propulsion Laboratory (JPL), the NASA Ocean Biology Processing Group (OBPG), and the Rosenstiel School of Marine and Atmospheric Science (RSMAS). Researchers at RSMAS are responsible for SST algorithm development, error statistics and quality flagging, while the OBPG, as the NASA ground data system, is responsible for the production of daily MODIS ocean products. JPL acquires MODIS ocean granules from the OBPG and reformats them to the GHRSST L2P netCDF specification with complete metadata and ancillary variables, and distributes the data as the official Physical Oceanography Data Archive (PO.DAAC) for SST.  The R2019.0 supersedes the previous R2014.0 datasets which can be found at  https://doi.org/10.5067/GHMDT-2PJ02",
-            "release-place": "Jet Propulsion Laboratory, CA, USA",
-            "series-name": "GHRSST Level 2P Global Sea Surface Skin Temperature from the Moderate Resolution Imaging Spectroradiometer (MODIS) on NASA Terra",
             "creator": "JPL/OBPG/RSMAS",
-            "title": "GHRSST Level 2P Global Sea Surface Skin Temperature from the Moderate Resolution Imaging Spectroradiometer (MODIS) on the NASA Terra satellite (GDS2)",
-            "graphic-preview-description": "Thumbnail",
-            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/MODIS_T-JPL-L2P-v2019.0.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "NASA produces skin sea surface temperature (SST) products from the Infrared (IR) channels of the Moderate-resolution Imaging Spectroradiometer (MODIS) onboard the Terra satellite. Terra was launched by NASA on December 18, 1999, into a sun synchronous, polar orbit with a daylight descending node at 10:30 am, to study the global dynamics of the Earth atmosphere, land and oceans. The MODIS captures data in 36 spectral bands at a variety of spatial resolutions.  Two SST products can be present in these files. The first is a skin SST produced for both day and night observations, derived from the long wave IR 11 and 12 micron wavelength channels, using a modified nonlinear SST algorithm intended to provide continuity with SST derived from heritage and current NASA sensors. At night, a second SST product is produced using the mid-infrared 3.95 and 4.05 micron channels which are unique to MODIS; the SST derived from these measurements is identified as SST4. The SST4 product has lower uncertainty, but due to sun glint can only be produced at night. MODIS L2P SST data have a 1 km spatial resolution at nadir and are stored in 288 five minute granules per day. Full global coverage is obtained every two days, with coverage poleward of 32.3 degree being complete each day. The production of MODIS L2P SST files is part of the Group for High Resolution Sea Surface Temperature (GHRSST) project, and is a joint collaboration between the NASA Jet Propulsion Laboratory (JPL), the NASA Ocean Biology Processing Group (OBPG), and the Rosenstiel School of Marine and Atmospheric Science (RSMAS). Researchers at RSMAS are responsible for SST algorithm development, error statistics and quality flagging, while the OBPG, as the NASA ground data system, is responsible for the production of daily MODIS ocean products. JPL acquires MODIS ocean granules from the OBPG and reformats them to the GHRSST L2P netCDF specification with complete metadata and ancillary variables, and distributes the data as the official Physical Oceanography Data Archive (PO.DAAC) for SST.  The R2019.0 supersedes the previous R2014.0 datasets which can be found at  https://doi.org/10.5067/GHMDT-2PJ02",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGHMDT-2PJ19",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGHMDT-2PJ19",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
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
-                    "mediaType": "text/html",
-                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/atbd/sst4/",
-                    "description": "Short-Wave Sea Surface Temperature (SST4) documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Short-Wave Sea Surface Temperature (SST4) documentation",
+                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/atbd/sst4/",
+                    "mediaType": "text/html",
                     "title": "View the documentation for this dataset's algorithms"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/reprocessing/r2019/sst/",
-                    "description": "Release Notes",
                     "@type": "dcat:Distribution",
+                    "description": "Release Notes",
+                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/reprocessing/r2019/sst/",
+                    "mediaType": "text/html",
                     "title": "View this dataset's processing history"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/atbd/sst/flag/",
-                    "description": "Data Quality Flag description",
                     "@type": "dcat:Distribution",
+                    "description": "Data Quality Flag description",
+                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/atbd/sst/flag/",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ghrsst.jpl.nasa.gov",
-                    "description": "Group for High Resolution Sea Surface Temperature information",
                     "@type": "dcat:Distribution",
+                    "description": "Group for High Resolution Sea Surface Temperature information",
+                    "downloadURL": "https://ghrsst.jpl.nasa.gov",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://modis.gsfc.nasa.gov/data/atbd/atbd_mod25.pdf",
-                    "description": "Algorithm Theoretical Basis Document",
                     "@type": "dcat:Distribution",
+                    "description": "Algorithm Theoretical Basis Document",
+                    "downloadURL": "https://modis.gsfc.nasa.gov/data/atbd/atbd_mod25.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's algorithm theoretical basis document"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/MODIS_T-JPL-L2P-v2019.0.jpg",
-                    "description": "Thumbnail",
                     "@type": "dcat:Distribution",
+                    "description": "Thumbnail",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/MODIS_T-JPL-L2P-v2019.0.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://podaac.jpl.nasa.gov/forum/viewforum.php?f=18&sid=e2d67e5a01815fc6e39fcd2087ed8bc8",
-                    "description": "PO.DAAC User Forum",
                     "@type": "dcat:Distribution",
+                    "description": "PO.DAAC User Forum",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/forum/viewforum.php?f=18&sid=e2d67e5a01815fc6e39fcd2087ed8bc8",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/atbd/sst/",
-                    "description": "Long-Wave Sea Surface Temperature (SST) documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Long-Wave Sea Surface Temperature (SST) documentation",
+                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/atbd/sst/",
+                    "mediaType": "text/html",
                     "title": "View the documentation for this dataset's algorithms"
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
-                    "downloadURL": "http://www.ghrsst.org",
-                    "description": "GHRSST Project Office homepage",
                     "@type": "dcat:Distribution",
+                    "description": "GHRSST Project Office homepage",
+                    "downloadURL": "http://www.ghrsst.org",
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
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C1940475563-POCLOUD",
-                    "description": "HTTPS endpoint for data browse and download",
                     "@type": "dcat:Distribution",
+                    "description": "HTTPS endpoint for data browse and download",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C1940475563-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://github.com/podaac/tutorials/blob/master/notebooks/MODIS_L2P_SST_DataCube.ipynb",
-                    "description": "Jupyter python notebook to create a gridded \"data cube\"",
                     "@type": "dcat:Distribution",
+                    "description": "Jupyter python notebook to create a gridded \"data cube\"",
+                    "downloadURL": "https://github.com/podaac/tutorials/blob/master/notebooks/MODIS_L2P_SST_DataCube.ipynb",
+                    "mediaType": "text/html",
                     "title": "View this dataset's data recipes"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1940475563-POCLOUD",
-                    "description": "Browse granule search results in Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse granule search results in Earthdata Search",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1940475563-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 }
             ],
+            "graphic-preview-description": "Thumbnail",
+            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/MODIS_T-JPL-L2P-v2019.0.jpg",
+            "identifier": "C1940475563-POCLOUD",
+            "issued": "2019-12-31",
+            "keyword": [
+                "ngda",
+                "ocean temperature",
+                "oceans",
+                "earth science",
+                "national geospatial data asset"
+            ],
+            "landingPage": "https://doi.org/10.5067/GHMDT-2PJ19",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2019-12-31",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/JPL/PODAAC"
+            },
+            "references": [
+                "http://dx.doi.org/10.1016/j.rse.2015.04.023"
+            ],
+            "release-place": "Jet Propulsion Laboratory, CA, USA",
+            "series-name": "GHRSST Level 2P Global Sea Surface Skin Temperature from the Moderate Resolution Imaging Spectroradiometer (MODIS) on NASA Terra",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2000-02-24T00:00:00Z/2023-03-01T00:00:00Z",
             "theme": [
                 "GHRSST",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "GHRSST Level 2P Global Sea Surface Skin Temperature from the Moderate Resolution Imaging Spectroradiometer (MODIS) on the NASA Terra satellite (GDS2)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=CO-SSA-RSS-1-TBOC4-V1.0",
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
+            "description": "The Cassini Radio Science Titan Bistatic and Occultation Experiment (TBOC4) Raw Data Archive is a time-ordered collection of radio science raw data acquired on November 3, 2008, during the Cassini Extended Mission.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.co-ssa-rss-1-tboc4-v1.0_876c-8j2k",
+            "issued": "2021-05-21",
+            "keyword": [
+                "cassini-huygens",
+                "titan"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=CO-SSA-RSS-1-TBOC4-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.co-ssa-rss-1-tboc4-v1.0_876c-8j2k",
-            "description": "The Cassini Radio Science Titan Bistatic and Occultation Experiment (TBOC4) Raw Data Archive is a time-ordered collection of radio science raw data acquired on November 3, 2008, during the Cassini Extended Mission.",
-            "title": "CASSINI RSS RAW DATA SET - TBOC4 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "CASSINI RSS RAW DATA SET - TBOC4 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/AURA/TES/TL3HDOD_L3.005",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2004-07-15. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/AURA/TES/TL3HDOD_L3.005. https://asdc.larc.nasa.gov/project/TES.",
-            "issued": "2015-08-27",
-            "temporal": "2004-09-18T00:00:00Z/2018-01-22T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2019-06-19",
-            "keyword": [
-                "atmosphere",
-                "atmospheric temperature",
-                "atmospheric pressure",
-                "atmospheric water vapor",
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
-            "identifier": "C1429943812-LARC",
             "description": "TL3HDOD_5 is the Tropospheric Emission Spectrometer (TES)/Aura Level 3 (L3) 3 Deuterium Oxide Daily Gridded Version 5 data product. It consists of daily atmospheric temperature and volume mixing ratio (VMR) for the deuterium oxide atmospheric species, which are provided at 2 degree latitude by 4 degree longitude spatial grids and at a subset of TES standard pressure levels. TES was an instrument aboard NASA's Aura satellite and was launched from California on July 15, 2004. Data collection for TES is complete. \r\rThe TES Science Data Processing L3 subsystem interpolated L2 atmospheric profiles collected in a Global Survey onto a global grid uniform in latitude and longitude to provide a 3-D representation of the distribution of atmospheric gasses. The L3 standard data products are composed of L3 HDF-EOS grid data. A separate product file was produced for each different atmospheric species. TES obtained data in two basic observation modes: Limb or Nadir; Nadir observations, which point directly to the surface of the Earth, are different from limb observations, which are pointed at various off-nadir angles into the atmosphere. The product file may contain, in separate folders, limb data, nadir data, or both folders may be present. Specific to L3 processing were the terms Daily and Monthly representing the approximate time coverage of the L3 products. However, the input data granules to the L3 process are complete Global Surveys; in other words a Global Survey was not split in relation to time when input to the L3 processes even if they exceed the usual understood meanings of a day or month. More specifically, Daily L3 products represented a single Global Survey (approximately 26 hours) and Monthly L3 products represent Global Surveys that are initiated within that calendar month. The data granules defined for L3 standard products were daily and monthly.",
-            "title": "TES/Aura L3 Deuterium Oxide Daily Gridded V005",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAURA%2FTES%2FTL3HDOD_L3.005",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAURA%2FTES%2FTL3HDOD_L3.005",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
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
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/tes/guide/tes_project.pdf",
-                    "description": "TES Langley ASDC Project Guide",
                     "@type": "dcat:Distribution",
+                    "description": "TES Langley ASDC Project Guide",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/tes/guide/tes_project.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's product usage"
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
-                    "downloadURL": "https://doi.org/10.5067/AURA/TES/TL3HDOD_L3.005",
-                    "description": "DOI data set landing page for TL3HDOD_5",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for TL3HDOD_5",
+                    "downloadURL": "https://doi.org/10.5067/AURA/TES/TL3HDOD_L3.005",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/TES/TL3HDOD.005/contents.html",
-                    "description": "OPeNDAP data access for TL3HDOD_5",
                     "@type": "dcat:Distribution",
+                    "description": "OPeNDAP data access for TL3HDOD_5",
+                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/TES/TL3HDOD.005/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1429943812-LARC",
-                    "description": "Earthdata Search for TL3HDOD_5 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for TL3HDOD_5 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1429943812-LARC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/TES/TL3HDOD.005/",
-                    "description": "ASDC Direct Data Download for TL3HDOD_5",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for TL3HDOD_5",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/TES/TL3HDOD.005/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 }
             ],
+            "identifier": "C1429943812-LARC",
+            "issued": "2015-08-27",
+            "keyword": [
+                "atmosphere",
+                "atmospheric temperature",
+                "atmospheric pressure",
+                "atmospheric water vapor",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/AURA/TES/TL3HDOD_L3.005",
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
+            "temporal": "2004-09-18T00:00:00Z/2018-01-22T23:59:59Z",
             "theme": [
                 "TES",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "TES/Aura L3 Deuterium Oxide Daily Gridded V005"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC1-0561-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 1 phase 2014-11-20 to 2015-03-10. It is a Global Gravity measurement at the comet 67P and covers the time 2015-02-02T23:32:10.000 to 2015-02-03T10:51:46.500.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc1-0561-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC1-0561-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc1-0561-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 1 phase 2014-11-20 to 2015-03-10. It is a Global Gravity measurement at the comet 67P and covers the time 2015-02-02T23:32:10.000 to 2015-02-03T10:51:46.500.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 1 0561 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 1 0561 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-X-OSIWAC-2-CR2-CHECKOUT-V2.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This CODMAC level 2 data set contains uncalibrated image data in DN unit,  acquired by the OSIRIS Wide Angle Camera on the Rosetta spacecraft  during the CRUISE 2 mission phase, covering the period  from 2005-04-05T00:00:00.000 to 2006-07-28T23:59:59.000. The prime objective was commissioning / calibration. Several targets of opportunity were observed, but none of them is identifiable as prime target. This version V2.0 supersedes previous deliveries of the same dataset with the following changes since the last version: Reprocessed dataset after October 2018 PSA/PDS external peer review.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-x-osiwac-2-cr2-checkout-v2.0",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2021-05-21",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "16 cyg b",
                 "9p/tempel 1 (1867 g1)",
@@ -345618,133 +345620,109 @@
                 "starfield",
                 "international rosetta mission"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-X-OSIWAC-2-CR2-CHECKOUT-V2.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-x-osiwac-2-cr2-checkout-v2.0",
-            "description": "This CODMAC level 2 data set contains uncalibrated image data in DN unit,  acquired by the OSIRIS Wide Angle Camera on the Rosetta spacecraft  during the CRUISE 2 mission phase, covering the period  from 2005-04-05T00:00:00.000 to 2006-07-28T23:59:59.000. The prime objective was commissioning / calibration. Several targets of opportunity were observed, but none of them is identifiable as prime target. This version V2.0 supersedes previous deliveries of the same dataset with the following changes since the last version: Reprocessed dataset after October 2018 PSA/PDS external peer review.",
-            "title": "ROSETTA-ORBITER CHECKOUT OSIWAC 2 CR2 EDR V2.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER CHECKOUT OSIWAC 2 CR2 EDR V2.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.7265/N5NP22C0",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Western Italian Alps Monthly Snowfall and Snow Cover Duration, Version 1. Version 1. Archived by National Aeronautics and Space Administration, U.S. Government, National Snow and Ice Data Center. https://doi.org/10.7265/N5NP22C0.",
-            "issued": "1877-01-01",
-            "temporal": "1877-01-01T00:00:00Z/1996-12-31T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "1996-12-31",
-            "keyword": [
-                "terrestrial hydrosphere",
-                "snow/ice",
-                "earth science",
-                "cryosphere"
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
-            "identifier": "C1386206489-NSIDCV0",
             "description": "This data set consists of snow observations for 18 stations in the western Italian Alps. Two types of data are included: monthly snowfall amounts and monthly snow cover duration in days. The period of record varies with each station, with the longest station record including data from 1877 to 1996. The average station record duration is approximately 61 years. Available stations range from 565 meters to 2720 meters in elevation. The data are summaries of snow stake measurements. Daily observations of total snow depth were generally made at 8 a.m. local time. Data were aquired using a snow measuring rod. Snowfall amount was defined as being any increase over the previous day's reading. This measurement may be an underestimate of as much as 10-20% due to snow pack settlement. However, this underestimation is fairly consistent for all measurements. The daily data were then totaled to yield the monthly values.",
-            "title": "Western Italian Alps Monthly Snowfall and Snow Cover Duration, Version 1",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.7265%2FN5NP22C0",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.7265%2FN5NP22C0",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/forms/G01186_or.html?major_version=1",
-                    "description": "Direct download, with optional registration page.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download, with optional registration page.",
+                    "downloadURL": "https://nsidc.org/forms/G01186_or.html?major_version=1",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.7265/N5NP22C0",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.7265/N5NP22C0",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.7265/N5NP22C0",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.7265/N5NP22C0",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C1386206489-NSIDCV0",
+            "issued": "1877-01-01",
+            "keyword": [
+                "terrestrial hydrosphere",
+                "snow/ice",
+                "earth science",
+                "cryosphere"
+            ],
+            "landingPage": "https://doi.org/10.7265/N5NP22C0",
+            "language": [
+                "en-US"
+            ],
+            "modified": "1996-12-31",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NSIDC"
+            },
             "spatial": "6.695 44.192 8.436 46.425",
+            "temporal": "1877-01-01T00:00:00Z/1996-12-31T23:59:59.999Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Western Italian Alps Monthly Snowfall and Snow Cover Duration, Version 1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1273652190-GES_DISC.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Goddard Space Flight Center (GSFC). 2009-05-29. HRIRN3L1. Version 001. HRIR/Nimbus-3 Level 1 Meteorological Radiation Data V001. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://disc.gsfc.nasa.gov/datacollection/HRIRN3L1_001.html. Digital Science Data.",
-            "issued": "1969-04-17",
-            "temporal": "1969-04-17T00:00:00Z/1970-03-21T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "1970-03-21",
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
-            "identifier": "C1273652190-GES_DISC",
-            "description": "HRIRN3L1 is the High Resolution Infrared Radiometer (HRIR) Nimbus-3 Level 1 Meteorological Radiance Data (NMRT) product and contains infrared radiances converted to equivalent black-body temperature or \"brightness\" temperature values. The data, originally written on IBM 360 machines, were recovered from magnetic tapes, also referred to as Nimbus Meteorological Radiation Tapes (NMRT). The data are archived in their original IBM 36-bit word proprietary format, also referred to as a binary TAP file.\n\nThe HRIR instrument was designed to perform two major functions: first to map the Earth's cloud cover at night to complement the television coverage during the daytime portion of the orbit, and second to measure the temperature of cloud tops and terrain features.  The HRIR flown on Nimbus-3 was modified to allow nighttime and daytime cloud cover mapping  by use of dual band-pass filter which transmits 0.7 to 1.3 micron, and 3.4 to 4.2 micron radiation.  The HRIR instrument was launched on the Nimbus-3 satellite and was operational from April 14, 1966 through July 22, 1969. Nighttime operation was made in the 3.4 to 4.2 micron near infrared region.  Daytime operation was based on the predominance of reflected solar energy in the 0.7 to 1.3 micron region.  Change-over from nighttime to daytime operation was accomplished automatically (or by ground station command), by actuating a relay in the early stages of the radiometer electronics.  The system gain was reduced in the daytime mode to compensate for the higher energy levels.\n\nThis product was previously available from the NSSDC with the identifier ESAD-00222 (old ID 69-037A-02C).",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "HRIRN3L1",
             "creator": "Goddard Space Flight Center (GSFC)",
-            "title": "HRIR/Nimbus-3 Level 1 Meteorological Radiation Data V001 (HRIRN3L1) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/HRIRN3L1_001.png",
-            "programCode": [
-                "026:001"
-            ],
+            "data-presentation-form": "Digital Science Data",
+            "description": "HRIRN3L1 is the High Resolution Infrared Radiometer (HRIR) Nimbus-3 Level 1 Meteorological Radiance Data (NMRT) product and contains infrared radiances converted to equivalent black-body temperature or \"brightness\" temperature values. The data, originally written on IBM 360 machines, were recovered from magnetic tapes, also referred to as Nimbus Meteorological Radiation Tapes (NMRT). The data are archived in their original IBM 36-bit word proprietary format, also referred to as a binary TAP file.\n\nThe HRIR instrument was designed to perform two major functions: first to map the Earth's cloud cover at night to complement the television coverage during the daytime portion of the orbit, and second to measure the temperature of cloud tops and terrain features.  The HRIR flown on Nimbus-3 was modified to allow nighttime and daytime cloud cover mapping  by use of dual band-pass filter which transmits 0.7 to 1.3 micron, and 3.4 to 4.2 micron radiation.  The HRIR instrument was launched on the Nimbus-3 satellite and was operational from April 14, 1966 through July 22, 1969. Nighttime operation was made in the 3.4 to 4.2 micron near infrared region.  Daytime operation was based on the predominance of reflected solar energy in the 0.7 to 1.3 micron region.  Change-over from nighttime to daytime operation was accomplished automatically (or by ground station command), by actuating a relay in the early stages of the radiometer electronics.  The system gain was reduced in the daytime mode to compensate for the higher energy levels.\n\nThis product was previously available from the NSSDC with the identifier ESAD-00222 (old ID 69-037A-02C).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -345753,80 +345731,116 @@
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/HRIRN3L1_001.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/HRIRN3L1_001.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/Nimbus3_HRIR_Level1/HRIRN3L1.001/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/Nimbus3_HRIR_Level1/HRIRN3L1.001/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=HRIRN3L1",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=HRIRN3L1",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/Nimbus3_HRIR_Level1/HRIRN3L1.001/doc/README.HRIRN3L1.001.pdf",
-                    "description": "README Document",
                     "@type": "dcat:Distribution",
+                    "description": "README Document",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/Nimbus3_HRIR_Level1/HRIRN3L1.001/doc/README.HRIRN3L1.001.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's read me document"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/repository/Mission/Nimbus/3.3_Product_Documentation/3.3.5_Product_Quality/NimbusIIIUG.pdf",
-                    "description": "Nimbus 3 Users Guide",
                     "@type": "dcat:Distribution",
+                    "description": "Nimbus 3 Users Guide",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/repository/Mission/Nimbus/3.3_Product_Documentation/3.3.5_Product_Quality/NimbusIIIUG.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
                 },
                 {
-                    "mediaType": "application/gzip",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/repository/Mission/Nimbus/3.3_Product_Documentation/3.3.5_Product_Quality/DataCatalogNimbus3.tar.gz",
-                    "description": "Nimbus 3 Data Catalog",
                     "@type": "dcat:Distribution",
+                    "description": "Nimbus 3 Data Catalog",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/repository/Mission/Nimbus/3.3_Product_Documentation/3.3.5_Product_Quality/DataCatalogNimbus3.tar.gz",
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
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Nimbus/N3_HRIR_Inventory.xlsx",
-                    "description": "N3 HRIR Inventory",
                     "@type": "dcat:Distribution",
+                    "description": "N3 HRIR Inventory",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Nimbus/N3_HRIR_Inventory.xlsx",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/HRIRN3L1_001.png",
+            "identifier": "C1273652190-GES_DISC",
+            "issued": "1969-04-17",
+            "keyword": [
+                "spectral/engineering",
+                "earth science",
+                "infrared wavelengths"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1273652190-GES_DISC.html",
+            "language": [
+                "en-US"
+            ],
+            "modified": "1970-03-21",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
+            },
+            "release-place": "Greenbelt, MD, USA",
+            "series-name": "HRIRN3L1",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "1969-04-17T00:00:00Z/1970-03-21T23:59:59.999Z",
             "theme": [
                 "Nimbus",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "HRIR/Nimbus-3 Level 1 Meteorological Radiation Data V001 (HRIRN3L1) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.nasa.gov/d/87pb-v3z9",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "GeneLab Outreach",
+                "hasEmail": "mailto:genelab-outreach@lists.nasa.gov"
+            },
+            "description": "Genome sequencing and assembly of lower Eukaryotic isolates belonging to class Tremellomycetes isolated from International Space Station",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "GeneLab Study Page",
+                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-290",
+                    "mediaType": "text/html",
+                    "title": "Lower eukaryotic isolates belonging to class Tremellomycetes isolated from International Space Station Genome sequencing and assembly"
+                }
+            ],
+            "identifier": "nasa_genelab_GLDS-290_87pb-v3z9",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
             "keyword": [
                 "library construction",
                 "nucleic acid sequencing",
@@ -345836,1182 +345850,1177 @@
                 "strain",
                 "nucleic acid extraction"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "GeneLab Outreach",
-                "hasEmail": "mailto:genelab-outreach@lists.nasa.gov"
-            },
+            "landingPage": "https://data.nasa.gov/d/87pb-v3z9",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "nasa_genelab_GLDS-290_87pb-v3z9",
-            "description": "Genome sequencing and assembly of lower Eukaryotic isolates belonging to class Tremellomycetes isolated from International Space Station",
-            "title": "Lower eukaryotic isolates belonging to class Tremellomycetes isolated from International Space Station Genome sequencing and assembly",
-            "programCode": [
-                "026:005"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-290",
-                    "description": "GeneLab Study Page",
-                    "@type": "dcat:Distribution",
-                    "title": "Lower eukaryotic isolates belonging to class Tremellomycetes isolated from International Space Station Genome sequencing and assembly"
-                }
-            ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "Lower eukaryotic isolates belonging to class Tremellomycetes isolated from International Space Station Genome sequencing and assembly"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1102",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Moorcroft, P.R., G.C. Hurtt, and S.W. Pacala. 2012. LBA-ECO LC-08 Ecosystem Demography Model Estimated C, NPP, and Biomass For Amazonia. ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/1102",
-            "issued": "2023-10-15",
-            "temporal": "1987-01-01T00:00:00Z/1988-12-31T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-10-17",
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
-            "identifier": "C2784856942-ORNL_CLOUD",
             "description": "This data set provides Ecosystem Demography Model (ED) estimates of potential above-ground net primary production (NPP) (kg C/m2/y), potential average live biomass (kg C/m2), and potential average soil carbon (kg C/m2) for the Brazilian Amazon at 1 degree resolution. Ecosystem Demography Model predicts both ecosystem structure (e.g. above and below-ground biomass, vegetation height and basal area, and soil carbon stocks) and corresponding ecosystem fluxes (e.g. NPP, NEP, and evapotranspiration) from climate, soil, and land-use inputs. Estimates for the Brazilian Amazon include the effects of natural disturbances such as windthrow and fire, but do not include the effects of human land use. To produce these estimates, ED was forced with ISLSCP I data for 1987 and 1988 and averaged into a single average year (Moorcroft et al., 2001).The data are provided for the three estimates in both ASCII text and in NetCDF formatted files.",
-            "graphic-preview-description": "Browse Image",
-            "title": "LBA-ECO LC-08 Ecosystem Demography Model Estimated C, NPP, and Biomass For Amazonia",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/sdat-tds/1102_1_fit.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1102",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1102",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/lba/land_use_land_cover_change/LC08_Ecosystem_Demography_Model/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/lba/land_use_land_cover_change/LC08_Ecosystem_Demography_Model/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/LBA/guides/LC08_Ecosystem_Dynamics_Model.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/LBA/guides/LC08_Ecosystem_Dynamics_Model.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1102",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1102",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC08_Ecosystem_Demography_Model/comp/LC08_Ecosystem_Dynamics_model.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC08_Ecosystem_Demography_Model/comp/LC08_Ecosystem_Dynamics_model.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://daac.ornl.gov/graphics/browse/sdat-tds/1102_1_fit.png",
-                    "description": "Browse Image",
                     "@type": "dcat:Distribution",
+                    "description": "Browse Image",
+                    "downloadURL": "https://daac.ornl.gov/graphics/browse/sdat-tds/1102_1_fit.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://webmap.ornl.gov/wcsdown/dataset.jsp?ds_id=1102",
-                    "description": "Web Coverage Service for this collection.",
                     "@type": "dcat:Distribution",
+                    "description": "Web Coverage Service for this collection.",
+                    "downloadURL": "https://webmap.ornl.gov/wcsdown/dataset.jsp?ds_id=1102",
+                    "mediaType": "text/html",
                     "title": "Use Web Coverage Service (WCS) to download the dataset's data"
                 }
             ],
+            "graphic-preview-description": "Browse Image",
+            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/sdat-tds/1102_1_fit.png",
+            "identifier": "C2784856942-ORNL_CLOUD",
+            "issued": "2023-10-15",
+            "keyword": [
+                "vegetation",
+                "ecological dynamics",
+                "earth science",
+                "biosphere"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1102",
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
             "spatial": "-85.0 -15.0 -30.0 15.0",
+            "temporal": "1987-01-01T00:00:00Z/1988-12-31T23:59:59Z",
             "theme": [
                 "LBA-ECO",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "LBA-ECO LC-08 Ecosystem Demography Model Estimated C, NPP, and Biomass For Amazonia"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/689",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Stone, T.A., and P. Schlesinger. 2003. RLC AVHRR-Derived Land Cover, Former Soviet Union, 15-km, 1984-1993. ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/689",
-            "issued": "2023-11-21",
-            "temporal": "1984-01-01T00:00:00Z/1993-12-31T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-12-02",
-            "keyword": [
-                "land surface",
-                "earth science",
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
-            "identifier": "C2810670679-ORNL_CLOUD",
             "description": "This dataset is a 15-kilometer resolution land cover map for the land area of the Former Soviet Union. There are sixty land cover classes distinguished in this dataset, of which 38 are forest cover classes.  The data set is useful for stratification of the FSU into general sub-regions of land cover for subsequent study using higher resolution satellite data.",
-            "graphic-preview-description": "Browse Image",
-            "title": "RLC AVHRR-Derived Land Cover, Former Soviet Union, 15-km, 1984-1993",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/vegetation_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F689",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F689",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/global_vegetation/rlc_land_cover/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/global_vegetation/rlc_land_cover/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/RLC/guides/RLC_AVHRR_FSU_15_km.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/RLC/guides/RLC_AVHRR_FSU_15_km.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/689",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/689",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/global_vegetation/rlc_land_cover/comp/dlcmap.jpg",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/global_vegetation/rlc_land_cover/comp/dlcmap.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/global_vegetation/rlc_land_cover/comp/dlcmap_legend.dbf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/global_vegetation/rlc_land_cover/comp/dlcmap_legend.dbf",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/global_vegetation/rlc_land_cover/comp/dlcmap_legend.txt",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/global_vegetation/rlc_land_cover/comp/dlcmap_legend.txt",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/global_vegetation/rlc_land_cover/comp/dlcmap_projection.txt",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/global_vegetation/rlc_land_cover/comp/dlcmap_projection.txt",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/global_vegetation/rlc_land_cover/comp/dlcmap_readme.txt",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/global_vegetation/rlc_land_cover/comp/dlcmap_readme.txt",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/global_vegetation/rlc_land_cover/comp/RLC_AVHRR_FSU_15_km.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/global_vegetation/rlc_land_cover/comp/RLC_AVHRR_FSU_15_km.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://daac.ornl.gov/graphics/browse/project/square/vegetation_logo_square.png",
-                    "description": "Browse Image",
                     "@type": "dcat:Distribution",
+                    "description": "Browse Image",
+                    "downloadURL": "https://daac.ornl.gov/graphics/browse/project/square/vegetation_logo_square.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 }
             ],
+            "graphic-preview-description": "Browse Image",
+            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/vegetation_logo_square.png",
+            "identifier": "C2810670679-ORNL_CLOUD",
+            "issued": "2023-11-21",
+            "keyword": [
+                "land surface",
+                "earth science",
+                "land use/land cover"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/689",
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
             "spatial": "19.82 35.24 180.0 75.0",
+            "temporal": "1984-01-01T00:00:00Z/1993-12-31T23:59:59Z",
             "theme": [
                 "Vegetation",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "RLC AVHRR-Derived Land Cover, Former Soviet Union, 15-km, 1984-1993"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ADGA209V9GC4",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Soil Moisture Active Passive (SMAP) L4 Carbon Ancillary Surface Meteorological Forcing Data V001. Version 1. Archived by National Aeronautics and Space Administration, U.S. Government, NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/ADGA209V9GC4.",
-            "issued": "2015-03-31",
-            "temporal": "2015-01-31T00:00:00Z/2023-03-01T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-07-31",
-            "keyword": [
-                "earth science",
-                "atmospheric radiation",
-                "atmosphere",
-                "atmospheric temperature",
-                "atmospheric water vapor"
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
-            "identifier": "C1539057357-NSIDC_ECS",
             "description": "This ancillary SMAP product contains dynamic surface meteorological forcing data. The meteorological model is derived from the Modern-Era Retrospective Analysis for Research and Applications (MERRA) data set and used as an input in the SMAP L4 Carbon algorithm. The forcing data is processed from hourly GEOS-5 files into daily values. Daily files are processed every eight days.",
-            "title": "Soil Moisture Active Passive (SMAP) L4 Carbon Ancillary Surface Meteorological Forcing Data V001",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FADGA209V9GC4",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FADGA209V9GC4",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/SMAP_ANC/SMAP_L4_C_ANC_MET.001/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/SMAP_ANC/SMAP_L4_C_ANC_MET.001/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=SMAP_L4_C_ANC_MET+V001",
-                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=SMAP_L4_C_ANC_MET+V001",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/ADGA209V9GC4",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/ADGA209V9GC4",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/ADGA209V9GC4",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/ADGA209V9GC4",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C1539057357-NSIDC_ECS",
+            "issued": "2015-03-31",
+            "keyword": [
+                "earth science",
+                "atmospheric radiation",
+                "atmosphere",
+                "atmospheric temperature",
+                "atmospheric water vapor"
+            ],
+            "landingPage": "https://doi.org/10.5067/ADGA209V9GC4",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2022-07-31",
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
+            "title": "Soil Moisture Active Passive (SMAP) L4 Carbon Ancillary Surface Meteorological Forcing Data V001"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ASDC/SUBORBITAL/DISCOVERAQ_California_Aerosol_AircraftInSitu_P3B_Data_1",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2022-03-30. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/ASDC/SUBORBITAL/DISCOVERAQ_California_Aerosol_AircraftInSitu_P3B_Data_1.",
-            "issued": "2021-08-17",
-            "temporal": "2013-01-09T00:00:00Z/2013-02-10T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-03-30",
-            "keyword": [
-                "earth science",
-                "atmosphere",
-                "aerosols"
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
-            "identifier": "C2245997372-LARC_ASDC",
             "description": "DISCOVERAQ_California_Aerosol_AircraftInSitu_P3B_Data contains in situ aerosol data collected onboard NASA's P-3B aircraft during the California (San Joaquin Valley) deployment of NASA's DISCOVER-AQ field study. Instruments utilized to collect data found in this data product include the PSAP, APS, CPC, CCN Counter, Nephelometer/PI-Neph, LAS, PILS, Ion Chromatographs, PILS/Total Organic Carbon Analyzer (TOC), SMPS, SP2 and UHSAS. This data product contains data for only the California deployment, and data collection is complete.\r\n\r\nUnderstanding the factors that contribute to near surface pollution is difficult using only satellite-based observations. The incorporation of surface-level measurements from aircraft and ground-based platforms provides the crucial information necessary to validate and expand upon the use of satellites in understanding near surface pollution. Deriving Information on Surface conditions from Column and Vertically Resolved Observations Relevant to Air Quality (DISCOVER-AQ) was a four-year campaign conducted in collaboration between NASA Langley Research Center, NASA Goddard Space Flight Center, NASA Ames Research Center, and multiple universities to improve the use of satellites to monitor air quality for public health and environmental benefit. Through targeted airborne and ground-based observations, DISCOVER-AQ enabled more effective use of current and future satellites to diagnose ground level conditions influencing air quality.\r\n\r\nDISCOVER-AQ employed two NASA aircraft, the P-3B and King Air, with the P-3B completing in-situ spiral profiling of the atmosphere (aerosol properties, meteorological variables, and trace gas species). The King Air conducted both passive and active remote sensing of the atmospheric column extending below the aircraft to the surface. Data from an existing network of surface air quality monitors, AERONET sun photometers, Pandora UV/vis spectrometers and model simulations were also collected. Further, DISCOVER-AQ employed many surface monitoring sites, with measurements being made on the ground, in conjunction with the aircraft. The B200 and P-3B conducted flights in Baltimore-Washington, D.C. in 2011, Houston, TX in 2013, San Joaquin Valley, CA in 2013, and Denver, CO in 2014. These regions were targeted due to being in violation of the National Ambient Air Quality Standards (NAAQS).\r\n\r\nThe first objective of DISCOVER-AQ was to determine and investigate correlations between surface measurements and satellite column observations for the trace gases ozone (O3), nitrogen dioxide (NO2), and formaldehyde (CH2O) to understand how satellite column observations can diagnose surface conditions. DISCOVER-AQ also had the objective of using surface-level measurements to understand how satellites measure diurnal variability and to understand what factors control diurnal variability. Lastly, DISCOVER-AQ aimed to explore horizontal scales of variability, such as regions with steep gradients and urban plumes.",
-            "title": "DISCOVER-AQ California Deployment P-3B Aircraft In Situ Aerosol Data",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC%2FSUBORBITAL%2FDISCOVERAQ_California_Aerosol_AircraftInSitu_P3B_Data_1",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC%2FSUBORBITAL%2FDISCOVERAQ_California_Aerosol_AircraftInSitu_P3B_Data_1",
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
-                    "downloadURL": "https://doi.org/10.5067/ASDC/SUBORBITAL/DISCOVERAQ_California_Aerosol_AircraftInSitu_P3B_Data_1",
-                    "description": "DOI Data Set Landing Page for DISCOVERAQ_California_Aerosol_AircraftInSitu_P3B_Data_1",
                     "@type": "dcat:Distribution",
+                    "description": "DOI Data Set Landing Page for DISCOVERAQ_California_Aerosol_AircraftInSitu_P3B_Data_1",
+                    "downloadURL": "https://doi.org/10.5067/ASDC/SUBORBITAL/DISCOVERAQ_California_Aerosol_AircraftInSitu_P3B_Data_1",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2245997372-LARC_ASDC",
-                    "description": "Earthdata Search for DISCOVERAQ_California_Aerosol_AircraftInSitu_P3B_Data_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for DISCOVERAQ_California_Aerosol_AircraftInSitu_P3B_Data_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2245997372-LARC_ASDC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/DISCOVER-AQ/California_Aerosol_AircraftInSitu_P3B_Data_1/",
-                    "description": "ASDC Direct Data Download for DISCOVERAQ_California_Aerosol_AircraftInSitu_P3B_Data_1",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for DISCOVERAQ_California_Aerosol_AircraftInSitu_P3B_Data_1",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/DISCOVER-AQ/California_Aerosol_AircraftInSitu_P3B_Data_1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 }
             ],
+            "identifier": "C2245997372-LARC_ASDC",
+            "issued": "2021-08-17",
+            "keyword": [
+                "earth science",
+                "atmosphere",
+                "aerosols"
+            ],
+            "landingPage": "https://doi.org/10.5067/ASDC/SUBORBITAL/DISCOVERAQ_California_Aerosol_AircraftInSitu_P3B_Data_1",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2022-03-30",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/LARC/SD/ASDC"
+            },
             "spatial": "<?xml version=\"1.0\" encoding=\"UTF-8\"?><gml:Polygon xmlns:gml=\"http://www.opengis.net/gml/3.2\" srsName=\"EPSG:9825\"><gml:outerBoundaryIs><gml:LinearRing><gml:posList>25.0 -130.0 25.0 -70.0 45.0 -70.0 45.0 -130.0 25.0 -130.0</gml:posList></gml:LinearRing></gml:outerBoundaryIs><gml:innerBoundaryIs></gml:innerBoundaryIs></gml:Polygon>",
+            "temporal": "2013-01-09T00:00:00Z/2013-02-10T23:59:59.999Z",
             "theme": [
                 "DISCOVER-AQ",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "DISCOVER-AQ California Deployment P-3B Aircraft In Situ Aerosol Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-5-PRL-67P-M06-GEO-V1.0",
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
+            "description": "This CODMAC level 5 data set contains derived data products that include pixel-precise georeferencing information, acquired by the OSIRIS Wide Angle Camera on the Rosetta spacecraft during the PRELANDING mission phase, covering the period from 2014-08-01T10:00:00.000 to 2014-09-02T09:59:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V1.0 is the first version of this dataset: Lien corrected dataset after October 2018 PSA/PDS external peer review.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-5-prl-67p-m06-geo-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-5-PRL-67P-M06-GEO-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-5-prl-67p-m06-geo-v1.0",
-            "description": "This CODMAC level 5 data set contains derived data products that include pixel-precise georeferencing information, acquired by the OSIRIS Wide Angle Camera on the Rosetta spacecraft during the PRELANDING mission phase, covering the period from 2014-08-01T10:00:00.000 to 2014-09-02T09:59:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V1.0 is the first version of this dataset: Lien corrected dataset after October 2018 PSA/PDS external peer review.",
-            "title": "ROSETTA-ORBITER 67P OSIWAC 5 PRL-MTP006 DDR-GEO V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P OSIWAC 5 PRL-MTP006 DDR-GEO V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=PHB2-M-TS-2-THERM%2FVIS-IMGEDR-V1.0",
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
-                "phobos 2"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "In February and March, 1989, the Termoskan instrument on board the Phobos '88 spacecraft of the USSR acquired a limited set of very high resolution simultaneous observations of the reflected solar flux (hereafter referred to as the visible channel) and emitted thermal flux (thermal infrared (IR)) from Mars's equatorial region. These are, so far, the highest spatial resolution thermal data ever obtained for Mars. Four slightly overlapping thermal panoramas (also called scans or swaths) cover a large portion of the equatorial region from 30 deg.S to 6 deg.N latitude. Simultaneous visible panoramas were taken during each of the four observing sessions; due to spacecraft memory limitations, visible channel processing was stopped early relative to the thermal channel for 2 of the sessions (2 and 4). Thus, the visible channel panoramas are shorter than the thermal panoramas for these sessions. These data are saved for historical reasons; they are not considered to be of archival quality.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.phb2-m-ts-2-therm-vis-imgedr-v1.0_884x-kg7q",
+            "issued": "2021-05-21",
+            "keyword": [
+                "mars",
+                "phobos 2"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=PHB2-M-TS-2-THERM%2FVIS-IMGEDR-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.phb2-m-ts-2-therm-vis-imgedr-v1.0_884x-kg7q",
-            "description": "In February and March, 1989, the Termoskan instrument on board the Phobos '88 spacecraft of the USSR acquired a limited set of very high resolution simultaneous observations of the reflected solar flux (hereafter referred to as the visible channel) and emitted thermal flux (thermal infrared (IR)) from Mars's equatorial region. These are, so far, the highest spatial resolution thermal data ever obtained for Mars. Four slightly overlapping thermal panoramas (also called scans or swaths) cover a large portion of the equatorial region from 30 deg.S to 6 deg.N latitude. Simultaneous visible panoramas were taken during each of the four observing sessions; due to spacecraft memory limitations, visible channel processing was stopped early relative to the thermal channel for 2 of the sessions (2 and 4). Thus, the visible channel panoramas are shorter than the thermal panoramas for these sessions. These data are saved for historical reasons; they are not considered to be of archival quality.",
-            "title": "PHOBOS 2 MARS TERMOSCAN THERMAL/VISIBLE IMAGING EDR V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "PHOBOS 2 MARS TERMOSCAN THERMAL/VISIBLE IMAGING EDR V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewBundle.jsp?identifier=urn%3Anasa%3Apds%3Aizenberg_pdart14_meap&version=2.0",
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
-                "messenger"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "MESSENGER Advanced Products (MEAP) by Noam Izenberg, PDART 2014",
+            "identifier": "urn:nasa:pds:izenberg_pdart14_meap_885d-zixd",
+            "issued": "2021-05-21",
+            "keyword": [
+                "mercury",
+                "messenger"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewBundle.jsp?identifier=urn%3Anasa%3Apds%3Aizenberg_pdart14_meap&version=2.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:izenberg_pdart14_meap_885d-zixd",
-            "description": "MESSENGER Advanced Products (MEAP) by Noam Izenberg, PDART 2014",
-            "title": "Izenberg PDART 2014 MESSENGER Advanced Products Bundle",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "Izenberg PDART 2014 MESSENGER Advanced Products Bundle"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-X-RSI-1%2F2%2F3-CVP1-0003-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This is a Commissioning measurement covering the time 2004-03-28T21:51:03.500 to 2004-03-29T06:51:57.950.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-x-rsi-1-2-3-cvp1-0003-v1.0_885q-iisb",
             "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "international rosetta mission",
                 "unknown"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-X-RSI-1%2F2%2F3-CVP1-0003-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-x-rsi-1-2-3-cvp1-0003-v1.0_885q-iisb",
-            "description": "This is a Commissioning measurement covering the time 2004-03-28T21:51:03.500 to 2004-03-29T06:51:57.950.",
-            "title": "ROSETTA-ORBITER CHECK RSI 1/2/3 COMMISSIONING 1 0003 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "ROSETTA-ORBITER CHECK RSI 1/2/3 COMMISSIONING 1 0003 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-EXT1-1402-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the ROSETTA EXTENSION 1 phase 2016-01-01 to 2016-04-05. It is a Global Gravity measurement at the comet 67P and covers the time 2016-02-06T09:10:10.000 to 2016-02-06T11:06:53.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-ext1-1402-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-EXT1-1402-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-ext1-1402-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the ROSETTA EXTENSION 1 phase 2016-01-01 to 2016-04-05. It is a Global Gravity measurement at the comet 67P and covers the time 2016-02-06T09:10:10.000 to 2016-02-06T11:06:53.000.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     ROSETTA EXTENSION 1 1402 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     ROSETTA EXTENSION 1 1402 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/GPMGV/GCPEX/VERTIX/DATA301",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Kollias, Pavlos .2013. GPM GROUND VALIDATION MCGILL VERTICAL POINTING X-BAND (VERTIX) RADAR GCPEX [indicate subset used]. Dataset available online from the NASA Global Hydrometeorology Resource Center DAAC, Huntsville, Alabama, U.S.A. DOI: http://dx.doi.org/10.5067/GPMGV/GCPEX/VERTIX/DATA301",
-            "issued": "2013-12-17",
-            "temporal": "2012-01-15T17:19:09Z/2012-02-29T23:59:58Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-05-23",
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
-            "identifier": "C1979830182-GHRC_DAAC",
             "description": "The GPM Ground Validation McGill Vertical Pointing X-Band (VertiX) Radar GCPEx dataset consists of radar reflectivity and Doppler velocity data collected by the Vertically Pointing X-band (VertiX) radar during the Global Precipitation Measurement (GPM) mission Cold-season Precipitation Experiment (GCPEx) field campaign in Ontario, Canada during the 2011-2012 winter season. VertiX can detect all precipitation targets and some ice clouds, as well as measure the Doppler velocity of precipitation targets. These measurements contributed to the overarching goal of GCPEx to collect various snowfall data for the improvement of GPM satellite winter precipitation estimates. These data files are available from January 15 through February 29, 2012 in netCDF-3 format with browse imagery available in GIF format.",
-            "graphic-preview-description": "N/A",
-            "title": "GPM GROUND VALIDATION MCGILL VERTICAL POINTING X-BAND (VERTIX) RADAR GCPEX V1",
-            "graphic-preview-file": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/gcpex/VERTIX/browse/",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGPMGV%2FGCPEX%2FVERTIX%2FDATA301",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGPMGV%2FGCPEX%2FVERTIX%2FDATA301",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=gpmvertixgcpex",
-                    "description": "Files may be downloaded directly to your workstation from this link",
                     "@type": "dcat:Distribution",
+                    "description": "Files may be downloaded directly to your workstation from this link",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=gpmvertixgcpex",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "image/gif",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/gcpex/VERTIX/browse/EC_CARE_xband_vertix_20120211.gif",
-                    "description": "Sample Browse Image",
                     "@type": "dcat:Distribution",
+                    "description": "Sample Browse Image",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/gcpex/VERTIX/browse/EC_CARE_xband_vertix_20120211.gif",
+                    "mediaType": "image/gif",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://pmm.nasa.gov/sites/default/files/document_files/GCPEx_science_plan_CURRENT.pdf",
-                    "description": "GPM Cold-season Precipitation Experiment (GCPEx) Science Plan",
                     "@type": "dcat:Distribution",
+                    "description": "GPM Cold-season Precipitation Experiment (GCPEx) Science Plan",
+                    "downloadURL": "https://pmm.nasa.gov/sites/default/files/document_files/GCPEx_science_plan_CURRENT.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
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
-                    "downloadURL": "https://pmm.nasa.gov/GCPEx/field-site",
-                    "description": "GCPEx Field Site",
                     "@type": "dcat:Distribution",
+                    "description": "GCPEx Field Site",
+                    "downloadURL": "https://pmm.nasa.gov/GCPEx/field-site",
+                    "mediaType": "text/html",
                     "title": "View information related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://www.radar.mcgill.ca/facilities/vertixmenu.html",
-                    "description": "McGill X-band radar",
                     "@type": "dcat:Distribution",
+                    "description": "McGill X-band radar",
+                    "downloadURL": "http://www.radar.mcgill.ca/facilities/vertixmenu.html",
+                    "mediaType": "text/html",
                     "title": "View information related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://www.radar.mcgill.ca/science/ex-instrument/ex-vertix.html",
-                    "description": "VertiX - Example: Vertically pointing X-band radar (VertiX)",
                     "@type": "dcat:Distribution",
+                    "description": "VertiX - Example: Vertically pointing X-band radar (VertiX)",
+                    "downloadURL": "http://www.radar.mcgill.ca/science/ex-instrument/ex-vertix.html",
+                    "mediaType": "text/html",
                     "title": "View information related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/gcpex/VERTIX/doc/gpmvertixgcpex_dataset.pdf",
-                    "description": "The guide document contains detailed information about the dataset",
                     "@type": "dcat:Distribution",
+                    "description": "The guide document contains detailed information about the dataset",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/gcpex/VERTIX/doc/gpmvertixgcpex_dataset.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/gcpex/VERTIX/doc/McGill_data_documentation_gcpex.txt",
-                    "description": "McGill GCPEx VertiX and W-band Radar NetCDF Data Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "McGill GCPEx VertiX and W-band Radar NetCDF Data Documentation",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/gcpex/VERTIX/doc/McGill_data_documentation_gcpex.txt",
+                    "mediaType": "text/html",
                     "title": "View the primary investigator's documentation for this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.1029/97RS00492",
-                    "description": "Measurements of melting layer attenuation at X-band frequencies",
                     "@type": "dcat:Distribution",
+                    "description": "Measurements of melting layer attenuation at X-band frequencies",
+                    "downloadURL": "https://doi.org/10.1029/97RS00492",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.1175/BAMS-D-13-00262.1",
```

