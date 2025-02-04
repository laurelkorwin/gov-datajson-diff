# Change History for nasa.json (Part 136)

### Changes from 31606f9 to dd2190f (Part 125/162)
**Author:** Automated

**Date:** 2025-02-01 15:02:16+00:00

**Message:** Updated data: Sat Feb  1 15:02:16 UTC 2025

```diff
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
+            "identifier": "C1979128148-GHRC_DAAC",
+            "issued": "2017-05-24",
+            "keyword": [
+                "earth science",
+                "atmosphere",
+                "precipitation"
+            ],
+            "landingPage": "https://doi.org/10.5067/GPMGV/OLYMPEX/APU/DATA301",
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
             "spatial": "-124.369 47.2025 -123.478 48.3871",
+            "temporal": "2015-01-10T09:24:00Z/2016-01-31T23:59:59Z",
             "theme": [
                 "OLYMPEX",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "GPM Ground Validation Autonomous Parsivel Unit (APU) OLYMPEX V1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG1-S-PWS-4-SUMM-SA-48SEC-V1.0",
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
+            "description": "This data set consists of 48-second calibrated, averaged wave electric field intensities from the Voyager 1 Plasma Wave Receiver spectrum analyzer obtained in the vicinity of the Jovian magnetosphere. For each 48-second interval, a geometric average field strength is determined for each of the 16 spectrum analyzer channels whose center frequencies range from  10 Hertz to 56.2 kiloHertz and which are logarithmically spaced in frequency, four channels per decade. The time associated with each set of averages is the beginning of the averaging interval. Averages are stored in units of volt/meter. During data gaps where complete 48-second intervals are missing, no entries exist in the file, that is, the gaps are not zero-filled or tagged in any other way. Additional information about this data set and the instrument which produced it can be found elsewhere in this catalog.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg1-s-pws-4-summ-sa-48sec-v1.0_rk92-v6a5",
+            "issued": "2021-05-21",
+            "keyword": [
+                "saturn",
+                "voyager"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG1-S-PWS-4-SUMM-SA-48SEC-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg1-s-pws-4-summ-sa-48sec-v1.0_rk92-v6a5",
-            "description": "This data set consists of 48-second calibrated, averaged wave electric field intensities from the Voyager 1 Plasma Wave Receiver spectrum analyzer obtained in the vicinity of the Jovian magnetosphere. For each 48-second interval, a geometric average field strength is determined for each of the 16 spectrum analyzer channels whose center frequencies range from  10 Hertz to 56.2 kiloHertz and which are logarithmically spaced in frequency, four channels per decade. The time associated with each set of averages is the beginning of the averaging interval. Averages are stored in units of volt/meter. During data gaps where complete 48-second intervals are missing, no entries exist in the file, that is, the gaps are not zero-filled or tagged in any other way. Additional information about this data set and the instrument which produced it can be found elsewhere in this catalog.",
-            "title": "VG1 SAT PWS RESAMPLED SPECTRAL ANALYZER\n                                      48SEC V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "VG1 SAT PWS RESAMPLED SPECTRAL ANALYZER\n                                      48SEC V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-3-PRL-67PCHURYUMOV-M07B-V1.0",
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
+            "description": "This data set contains calibrated images acquired by the OSIRIS Wide Angle\nCamera during the prelanding phase of the Rosetta mission at the comet 67P,\ncovering the period from 2014-09-16 to 2014-09-23.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-3-prl-67pchuryumov-m07b-v1.0_rk9n-v9z8",
+            "issued": "2018-06-26",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-3-PRL-67PCHURYUMOV-M07B-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-3-prl-67pchuryumov-m07b-v1.0_rk9n-v9z8",
-            "description": "This data set contains calibrated images acquired by the OSIRIS Wide Angle\nCamera during the prelanding phase of the Rosetta mission at the comet 67P,\ncovering the period from 2014-09-16 to 2014-09-23.",
-            "title": "ROSETTA-ORBITER COMET PRELANDING OSIWAC 3 RDR MTP 007B V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "ROSETTA-ORBITER COMET PRELANDING OSIWAC 3 RDR MTP 007B V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewBundle.jsp?identifier=urn%3Anasa%3Apds%3Agbo.ast.wisniewski.magnitudes&version=1.0",
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
+            "description": "Photometric observations of 125          asteroids, including absolute magnitudes, reported in Wisniewski et    al. 1997.",
+            "identifier": "urn:nasa:pds:gbo.ast.wisniewski.magnitudes",
+            "issued": "2021-05-21",
+            "keyword": [
+                "multiple asteroids",
+                "none"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewBundle.jsp?identifier=urn%3Anasa%3Apds%3Agbo.ast.wisniewski.magnitudes&version=1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:gbo.ast.wisniewski.magnitudes",
-            "description": "Photometric observations of 125          asteroids, including absolute magnitudes, reported in Wisniewski et    al. 1997.",
-            "title": "WISNIEWSKI ASTEROID ABSOLUTE MAGNITUDES",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "WISNIEWSKI ASTEROID ABSOLUTE MAGNITUDES"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/MODIS/MOD21.NRT.061",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "LANCEMODIS. 2021-02-07. MODIS/Terra Land Surface Temperature/3-Band Emissivity 5-Min L2 1km NRT. Version 6.1NRT. MODAPS at NASA/GSFC. Archived by National Aeronautics and Space Administration, U.S. Government, The Land, Atmosphere Near real-time Capability for EOS (LANCE). https://doi.org/10.5067/MODIS/MOD21.NRT.061. https://doi.org/10.5067/MODIS/MOD21.NRT.061.",
-            "issued": "2021-06-01",
-            "temporal": "2021-06-01T00:00:00Z/2023-07-24T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-20",
-            "keyword": [
-                "earth science",
-                "surface thermal properties",
-                "ngda",
-                "national geospatial data asset",
-                "land surface",
-                "surface radiative properties"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "MODAPS USER SUPPORT TEAM",
                 "hasEmail": "mailto:MODAPSUSO@lists.nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Not provided"
-            },
-            "identifier": "C2070234343-LANCEMODIS",
-            "description": "The  MODIS/Terra Land Surface Temperature/3-Band Emissivity (LST&E) 5-Min L2 1km data product, short-name MOD21 is produced daily in five minute temporal increments of satellite acquisition. The swath is approximately 2,030 pixels along track and 1,354 pixels per line, at a nadir resolution of 1,000 meters. The MOD21 Land Surface Temperature (LST) algorithm differs from the MOD11 (https://doi.org/10.5067/modis/mod11_l2.061) algorithm in that the MOD21 LST algorithm is based on the ASTER Temperature/Emissivity Separation (TES) technique, whereas the MOD11 uses the split-window technique. Additional details regarding the method used to create this Level 2 (L2) product are available in the Algorithm Theoretical Basis Document (ATBD (https://lpdaac.usgs.gov/documents/107/MOD21_ATBD.pdf)). \r\n\r\nThe Version 6.1 Level-1B (L1B) products have been improved by undergoing various calibration changes that include: changes to the response-versus-scan angle (RVS) approach that affects reflectance bands for Aqua and Terra MODIS, corrections to adjust for the optical crosstalk in Terra MODIS infrared (IR) bands, and more.",
-            "release-place": "MODAPS at NASA/GSFC",
             "creator": "LANCEMODIS",
-            "title": "MODIS/Terra Land Surface Temperature/3-Band Emissivity 5-Min L2 1km NRT",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The  MODIS/Terra Land Surface Temperature/3-Band Emissivity (LST&E) 5-Min L2 1km data product, short-name MOD21 is produced daily in five minute temporal increments of satellite acquisition. The swath is approximately 2,030 pixels along track and 1,354 pixels per line, at a nadir resolution of 1,000 meters. The MOD21 Land Surface Temperature (LST) algorithm differs from the MOD11 (https://doi.org/10.5067/modis/mod11_l2.061) algorithm in that the MOD21 LST algorithm is based on the ASTER Temperature/Emissivity Separation (TES) technique, whereas the MOD11 uses the split-window technique. Additional details regarding the method used to create this Level 2 (L2) product are available in the Algorithm Theoretical Basis Document (ATBD (https://lpdaac.usgs.gov/documents/107/MOD21_ATBD.pdf)). \r\n\r\nThe Version 6.1 Level-1B (L1B) products have been improved by undergoing various calibration changes that include: changes to the response-versus-scan angle (RVS) approach that affects reflectance bands for Aqua and Terra MODIS, corrections to adjust for the optical crosstalk in Terra MODIS infrared (IR) bands, and more.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMODIS%2FMOD21.NRT.061",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMODIS%2FMOD21.NRT.061",
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
-                    "downloadURL": "https://lance3.modaps.eosdis.nasa.gov/data_products/",
-                    "description": "Access Collection 6.1 data set from the MODAPS LANCE-MODIS page.",
                     "@type": "dcat:Distribution",
+                    "description": "Access Collection 6.1 data set from the MODAPS LANCE-MODIS page.",
+                    "downloadURL": "https://lance3.modaps.eosdis.nasa.gov/data_products/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through MODAPS"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nrt3.modaps.eosdis.nasa.gov/archive/allData/61/MOD21/",
-                    "description": "Direct access to the download site and directory hosting the MOD21 6.1NRT data set.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct access to the download site and directory hosting the MOD21 6.1NRT data set.",
+                    "downloadURL": "https://nrt3.modaps.eosdis.nasa.gov/archive/allData/61/MOD21/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through MODAPS"
                 }
             ],
+            "identifier": "C2070234343-LANCEMODIS",
+            "issued": "2021-06-01",
+            "keyword": [
+                "earth science",
+                "surface thermal properties",
+                "ngda",
+                "national geospatial data asset",
+                "land surface",
+                "surface radiative properties"
+            ],
+            "landingPage": "https://doi.org/10.5067/MODIS/MOD21.NRT.061",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2023-07-20",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Not provided"
+            },
+            "release-place": "MODAPS at NASA/GSFC",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2021-06-01T00:00:00Z/2023-07-24T00:00:00Z",
             "theme": [
                 "Terra",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "MODIS/Terra Land Surface Temperature/3-Band Emissivity 5-Min L2 1km NRT"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-EXT1-1405-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the ROSETTA EXTENSION 1 phase 2016-01-01 to 2016-04-05. It is a Global Gravity measurement at the comet 67P and covers the time 2016-02-07T11:24:10.000 to 2016-02-07T12:29:16.500.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-ext1-1405-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-EXT1-1405-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-ext1-1405-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the ROSETTA EXTENSION 1 phase 2016-01-01 to 2016-04-05. It is a Global Gravity measurement at the comet 67P and covers the time 2016-02-07T11:24:10.000 to 2016-02-07T12:29:16.500.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     ROSETTA EXTENSION 1 1405 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     ROSETTA EXTENSION 1 1405 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/SeaBASS/IMECOCAL/DATA001",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/GSFC/SED/ESD/GCDC/OB.DAAC. https://doi.org/10.5067/SeaBASS/IMECOCAL/DATA001.",
-            "issued": "2002-01-21",
-            "temporal": "2002-01-21T00:00:02Z/2023-04-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-04-06",
-            "keyword": [
-                "ocean temperature",
-                "oceans",
-                "ocean optics",
-                "ocean chemistry",
-                "earth science",
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
-            "identifier": "C1633360378-OB_DAAC",
             "description": "Measurements made under the IMECOCAL program (Investigaciones Mexicanas de la Corriente de California, translated: Mexican Research of the California Current) from 2002 to 2004.",
-            "title": "Investigaciones Mexicanas de la Corriente de California (IMECOCAL)",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSeaBASS%2FIMECOCAL%2FDATA001",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSeaBASS%2FIMECOCAL%2FDATA001",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://seabass.gsfc.nasa.gov/experiment/IMECOCAL/",
-                    "description": "Detailed information about the SeaBASS Experiment such as cruises, funding, and investigators",
                     "@type": "dcat:Distribution",
+                    "description": "Detailed information about the SeaBASS Experiment such as cruises, funding, and investigators",
+                    "downloadURL": "https://seabass.gsfc.nasa.gov/experiment/IMECOCAL/",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 }
             ],
+            "identifier": "C1633360378-OB_DAAC",
+            "issued": "2002-01-21",
+            "keyword": [
+                "ocean temperature",
+                "oceans",
+                "ocean optics",
+                "ocean chemistry",
+                "earth science",
+                "salinity/density"
+            ],
+            "landingPage": "https://doi.org/10.5067/SeaBASS/IMECOCAL/DATA001",
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
+            "temporal": "2002-01-21T00:00:02Z/2023-04-17T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Investigaciones Mexicanas de la Corriente de California (IMECOCAL)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ICESAT/GLAS/DATA210",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "GLAS/ICESat L2 Sea Ice Altimetry Data (HDF5) V034. Version 034. Archived by National Aeronautics and Space Administration, U.S. Government, NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/ICESAT/GLAS/DATA210.",
-            "issued": "2003-02-20",
-            "temporal": "2003-02-20T00:00:00Z/2009-10-11T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2009-10-11",
-            "keyword": [
-                "cryosphere",
-                "sea ice",
-                "oceans",
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
-            "identifier": "C1000000464-NSIDC_ECS",
             "description": "GLAH06 is used in conjunction with GLAH05 to create the Level-2 altimetry products. Level-2 altimetry data provide surface elevations for ice sheets (GLAH12), sea ice (GLAH13), land (GLAH14), and oceans (GLAH15). Data also include the laser footprint geolocation and reflectance, as well as geodetic, instrument, and atmospheric corrections for range measurements. The Level-2 elevation products, are regional products archived at 14 orbits per granule, starting and stopping at the same demarcation (\u00b1 50\u00b0 latitude) as GLAH05 and GLAH06. Each regional product is processed with algorithms specific to that surface type. Surface type masks define which data are written to each of the products. If any data within a given record fall within a specific mask, the entire record is written to the product. Masks can overlap: for example, non-land data in the sea ice region may be written to the sea ice and ocean products. This means that an algorithm may write the same data to more than one Level-2 product. In this case, different algorithms calculate the elevations in their respective products. The surface type masks are versioned and archived at NSIDC, so users can tell which data to expect in each product.  Each data granule has an associated browse product.",
-            "title": "GLAS/ICESat L2 Sea Ice Altimetry Data (HDF5) V034",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FICESAT%2FGLAS%2FDATA210",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FICESAT%2FGLAS%2FDATA210",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/GLAS/GLAH13.034/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/GLAS/GLAH13.034/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1000000464-NSIDC_ECS&m=-32.203125%210.84375%211%211%210%210%2C2&q=GLAH13",
-                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1000000464-NSIDC_ECS&m=-32.203125%210.84375%211%211%210%210%2C2&q=GLAH13",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/data/data-access-tool/GLAH13/versions/34/",
-                    "description": "Data Access link for ITSD project",
                     "@type": "dcat:Distribution",
+                    "description": "Data Access link for ITSD project",
+                    "downloadURL": "https://nsidc.org/data/data-access-tool/GLAH13/versions/34/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/ICESAT/GLAS/DATA210",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/ICESAT/GLAS/DATA210",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/ICESAT/GLAS/DATA210",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/ICESAT/GLAS/DATA210",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C1000000464-NSIDC_ECS",
+            "issued": "2003-02-20",
+            "keyword": [
+                "cryosphere",
+                "sea ice",
+                "oceans",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/ICESAT/GLAS/DATA210",
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
+            "title": "GLAS/ICESat L2 Sea Ice Altimetry Data (HDF5) V034"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/MODIS/MYD021KM.NRT.061",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "LANCEMODIS. 2017-10-20. MODIS/Aqua Calibrated Radiances 5-Min L1B Swath 1km. Version 6.1NRT. MODAPS at NASA/GSFC. Archived by National Aeronautics and Space Administration, U.S. Government, The Land, Atmosphere Near real-time Capability for EOS (LANCE). https://doi.org/10.5067/MODIS/MYD021KM.NRT.061. https://earthdata.nasa.gov/staging/earth-observation-data/near-real-time/download-nrt-data/modis-nrt.",
-            "issued": "2017-10-12",
-            "temporal": "2017-10-20T00:00:00Z/2023-07-24T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-20",
-            "keyword": [
-                "infrared wavelengths",
-                "earth science",
-                "national geospatial data asset",
-                "ngda",
-                "spectral/engineering",
-                "visible wavelengths"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "MODAPS USER SUPPORT TEAM",
                 "hasEmail": "mailto:MODAPSUSO@lists.nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/EOS/ESDIS/LANCEMODIS"
-            },
-            "identifier": "C1426616847-LANCEMODIS",
-            "description": "The MODIS Level 1B Near Real Time (NRT) data set contains calibrated and geolocated at-aperture radiances for 36 discrete bands located in the 0.4 to 14.4 micron region of electromagentic spectrum. These data are generated from the MODIS Level 1A scans of raw radiance and in the process converted to geophysical units of W/(m^2 um sr). In addition, the Earth Bi-directional Reflectance Distribution Function (BRDF) may be determined for the solar reflective bands (1-19, 26) through knowledge of the solar irradiance (e.g., determined from MODIS solar diffuser data, and from the target illumination geometry).  Additional data are provided including quality flags, error estimates and calibration data.               Visible, shortwave infrared, and near infrared measurements are only made during the daytime, while radiances for the thermal infrared region (bands 20-25, 27-36) are measured continuously.                                    Channel locations for MODIS are as follows:                                         Band   Center Wavelength (um)    Primary Use----   ----------------------    -----------1          0.620  - 0.670        Land/Cloud Boundaries2          0.841  - 0.876        Land/Cloud Boundaries3          0.459  - 0.479        Land/Cloud Properties4          0.545  - 0.565        Land/Cloud Properties5          1.230  - 1.250        Land/Cloud Properties6          1.628  - 1.652        Land/Cloud Properties7          2.105  - 2.155        Land/Cloud Properties8          0.405  - 0.420        Ocean Color/Phytoplankton9          0.438  - 0.448        Ocean Color/Phytoplankton10         0.483  - 0.493        Ocean Color/Phytoplankton11         0.526  - 0.536        Ocean Color/Phytoplankton12         0.546  - 0.556        Ocean Color/Phytoplankton13         0.662  - 0.672        Ocean Color/Phytoplankton14         0.673  - 0.683        Ocean Color/Phytoplankton15         0.743  - 0.753        Ocean Color/Phytoplankton16         0.862  - 0.877        Ocean Color/Phytoplankton17         0.890  - 0.920        Atmospheric Water Vapor18         0.931  - 0.941        Atmospheric Water Vapor19         0.915  - 0.965        Atmospheric Water Vapor20         3.660  - 3.840        Surface/Cloud Temperature21         3.929  - 3.989        Surface/Cloud Temperature22         3.929  - 3.989        Surface/Cloud Temperature23         4.020  - 4.080        Surface/Cloud Temperature24         4.433  - 4.498        Atmospheric Temperature25         4.482  - 4.549        Atmospheric Temperature26         1.360  - 1.390        Cirrus Clouds27         6.535  - 6.895        Water Vapor Profile28         7.175  - 7.475        Water Vapor Profile29         8.400  - 8.700        Water Vapor Profile30         9.580  - 9.880        Ozone Overburden31         10.780 - 11.280       Surface/Cloud Temperature32         11.770 - 12.270       Surface/Cloud Temperature33         13.185 - 13.485       Cloud Top Altitude34         13.485 - 13.785       Cloud Top Altitude35         13.785 - 14.085       Cloud Top Altitude36         14.085 - 14.385       Cloud Top Altitude                                         Channels 1 and 2 have 250 m resolution, channels 3 through 7 have 500m resolution, and the rest have 1 km resolution. However, for the MODIS L1B 1 km product, the 250 m and 500 m band radiance data and their associated uncertainties have been aggregated to 1km resolution. Thus the entire channel data set is referenced to the same spatial and geolocation scales. Separate L1B products are available for the 250 m channels (MYD02QKM) and 500 m channels (MYD02HKM) that preserve the original resolution of the data.                                         Spatial resolution for pixels at nadir is 1 km, degrading to 4.8 km in the along-scan direction at the scan extremes. However, thanks to the overlapping of consecutive swaths and respectively pixels there, the resulting resolution at the scan extremes is about 2km.  A 55 degree scanning pattern at the EO",
-            "release-place": "MODAPS at NASA/GSFC",
             "creator": "LANCEMODIS",
-            "title": "MODIS/Aqua Calibrated Radiances 5-Min L1B Swath 1km - NRT",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The MODIS Level 1B Near Real Time (NRT) data set contains calibrated and geolocated at-aperture radiances for 36 discrete bands located in the 0.4 to 14.4 micron region of electromagentic spectrum. These data are generated from the MODIS Level 1A scans of raw radiance and in the process converted to geophysical units of W/(m^2 um sr). In addition, the Earth Bi-directional Reflectance Distribution Function (BRDF) may be determined for the solar reflective bands (1-19, 26) through knowledge of the solar irradiance (e.g., determined from MODIS solar diffuser data, and from the target illumination geometry).  Additional data are provided including quality flags, error estimates and calibration data.               Visible, shortwave infrared, and near infrared measurements are only made during the daytime, while radiances for the thermal infrared region (bands 20-25, 27-36) are measured continuously.                                    Channel locations for MODIS are as follows:                                         Band   Center Wavelength (um)    Primary Use----   ----------------------    -----------1          0.620  - 0.670        Land/Cloud Boundaries2          0.841  - 0.876        Land/Cloud Boundaries3          0.459  - 0.479        Land/Cloud Properties4          0.545  - 0.565        Land/Cloud Properties5          1.230  - 1.250        Land/Cloud Properties6          1.628  - 1.652        Land/Cloud Properties7          2.105  - 2.155        Land/Cloud Properties8          0.405  - 0.420        Ocean Color/Phytoplankton9          0.438  - 0.448        Ocean Color/Phytoplankton10         0.483  - 0.493        Ocean Color/Phytoplankton11         0.526  - 0.536        Ocean Color/Phytoplankton12         0.546  - 0.556        Ocean Color/Phytoplankton13         0.662  - 0.672        Ocean Color/Phytoplankton14         0.673  - 0.683        Ocean Color/Phytoplankton15         0.743  - 0.753        Ocean Color/Phytoplankton16         0.862  - 0.877        Ocean Color/Phytoplankton17         0.890  - 0.920        Atmospheric Water Vapor18         0.931  - 0.941        Atmospheric Water Vapor19         0.915  - 0.965        Atmospheric Water Vapor20         3.660  - 3.840        Surface/Cloud Temperature21         3.929  - 3.989        Surface/Cloud Temperature22         3.929  - 3.989        Surface/Cloud Temperature23         4.020  - 4.080        Surface/Cloud Temperature24         4.433  - 4.498        Atmospheric Temperature25         4.482  - 4.549        Atmospheric Temperature26         1.360  - 1.390        Cirrus Clouds27         6.535  - 6.895        Water Vapor Profile28         7.175  - 7.475        Water Vapor Profile29         8.400  - 8.700        Water Vapor Profile30         9.580  - 9.880        Ozone Overburden31         10.780 - 11.280       Surface/Cloud Temperature32         11.770 - 12.270       Surface/Cloud Temperature33         13.185 - 13.485       Cloud Top Altitude34         13.485 - 13.785       Cloud Top Altitude35         13.785 - 14.085       Cloud Top Altitude36         14.085 - 14.385       Cloud Top Altitude                                         Channels 1 and 2 have 250 m resolution, channels 3 through 7 have 500m resolution, and the rest have 1 km resolution. However, for the MODIS L1B 1 km product, the 250 m and 500 m band radiance data and their associated uncertainties have been aggregated to 1km resolution. Thus the entire channel data set is referenced to the same spatial and geolocation scales. Separate L1B products are available for the 250 m channels (MYD02QKM) and 500 m channels (MYD02HKM) that preserve the original resolution of the data.                                         Spatial resolution for pixels at nadir is 1 km, degrading to 4.8 km in the along-scan direction at the scan extremes. However, thanks to the overlapping of consecutive swaths and respectively pixels there, the resulting resolution at the scan extremes is about 2km.  A 55 degree scanning pattern at the EO",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMODIS%2FMYD021KM.NRT.061",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMODIS%2FMYD021KM.NRT.061",
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
-                    "description": "Access Collection 6.1 data set from the MODAPS LANCE-MODIS page.",
                     "@type": "dcat:Distribution",
+                    "description": "Access Collection 6.1 data set from the MODAPS LANCE-MODIS page.",
+                    "downloadURL": "http://lance3.modaps.eosdis.nasa.gov/data_products/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through MODAPS"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nrt3.modaps.eosdis.nasa.gov/allData/61/MYD021KM/",
-                    "description": "Direct access to the directory hosting the MYD021KM 6.1 NRT data set.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct access to the directory hosting the MYD021KM 6.1 NRT data set.",
+                    "downloadURL": "https://nrt3.modaps.eosdis.nasa.gov/allData/61/MYD021KM/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through MODAPS"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://modis.gsfc.nasa.gov/sci_team/",
-                    "description": "MODIS Science Team",
                     "@type": "dcat:Distribution",
+                    "description": "MODIS Science Team",
+                    "downloadURL": "http://modis.gsfc.nasa.gov/sci_team/",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 }
             ],
+            "identifier": "C1426616847-LANCEMODIS",
+            "issued": "2017-10-12",
+            "keyword": [
+                "infrared wavelengths",
+                "earth science",
+                "national geospatial data asset",
+                "ngda",
+                "spectral/engineering",
+                "visible wavelengths"
+            ],
+            "landingPage": "https://doi.org/10.5067/MODIS/MYD021KM.NRT.061",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2023-07-20",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/EOS/ESDIS/LANCEMODIS"
+            },
+            "release-place": "MODAPS at NASA/GSFC",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2017-10-20T00:00:00Z/2023-07-24T00:00:00Z",
             "theme": [
                 "AQUA",
                 "DODS",
@@ -1312021,333 +1312022,334 @@
                 "OPENDAP",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "MODIS/Aqua Calibrated Radiances 5-Min L1B Swath 1km - NRT"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NEAR-A-MAG-3-RDR-CRUISE3-V1.0",
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
-                "solar wind",
-                "near earth asteroid rendezvous"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "NEAR MAG RDR volume sets contain a single data set, from one instrument and one mission phase (defined in the phase table in /AAREADME.TXT).",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.near-a-mag-3-rdr-cruise3-v1.0_rkdy-q9b3",
+            "issued": "2021-05-21",
+            "keyword": [
+                "solar wind",
+                "near earth asteroid rendezvous"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NEAR-A-MAG-3-RDR-CRUISE3-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.near-a-mag-3-rdr-cruise3-v1.0_rkdy-q9b3",
-            "description": "NEAR MAG RDR volume sets contain a single data set, from one instrument and one mission phase (defined in the phase table in /AAREADME.TXT).",
-            "title": "NEAR MAG DATA FOR CRUISE3",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "NEAR MAG DATA FOR CRUISE3"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.7927/7ppx-6m60",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Center for International Earth Science Information Network - CIESIN - Columbia University. 2020-12-31. Natural Resource Protection and Child Health Indicators, 2020 Release. Version 2020.00. Palisades, NY. Archived by National Aeronautics and Space Administration, U.S. Government, NASA Socioeconomic Data and Applications Center (SEDAC). https://doi.org/10.7927/7ppx-6m60. https://doi.org/10.7927/7ppx-6m60.",
-            "issued": "2010-01-01",
-            "temporal": "2010-01-01T00:00:00Z/2020-12-31T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-12-31",
-            "references": [
-                "https://doi.org/10.7927/H49G5JRZ",
-                "https://doi.org/10.7927/H45Q4T1N",
-                "https://doi.org/10.7927/H41Z4299",
-                "https://doi.org/10.7927/H4NZ85MP",
-                "https://doi.org/10.7927/H46M34RP",
-                "https://doi.org/10.7927/H4G73BM2",
-                "https://doi.org/10.7927/H48913TX",
-                "https://doi.org/10.7927/H4SQ8XGT",
-                "https://doi.org/10.7927/6t8a-es66",
-                "https://doi.org/10.7927/r6mv-sv82",
-                "https://doi.org/10.7927/n1br-dz33",
-                "https://doi.org/10.7927/5bbs-e174"
-            ],
-            "keyword": [
-                "earth science",
-                "environmental impacts",
-                "sustainability",
-                "human dimensions",
-                "public health"
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
-            "identifier": "C2146191194-SEDAC",
-            "description": "The Natural Resource Protection and Child Health Indicators, 2020 Release, is produced in support of the U.S. Millennium Challenge Corporation as selection criteria for funding eligibility. The Natural Resource Protection Indicator (NRPI) and Child Health Indicator (CHI) are based on proximity-to-target scores ranging from 0 to 100 (at target). The NRPI covers 250 countries and is calculated based on the weighted average percentage of biomes under protected status. The CHI is a composite index for 194 countries derived from the average of three proximity-to-target scores for access to at least basic water and sanitation, along with child mortality. The 2020 release includes a consistent time series of NRPI scores for 2010 to 2020 and CHI scores for 2010 to 2019.",
-            "release-place": "Palisades, NY",
-            "graphic-preview-description": "Sample browse graphic of the data set.",
             "creator": "Center for International Earth Science Information Network - CIESIN - Columbia University",
-            "title": "Natural Resource Protection and Child Health Indicators, 2020 Release",
-            "graphic-preview-file": "https://sedac.ciesin.columbia.edu/downloads/maps/nrmi/nrmi-natural-resource-protection-child-health-indicators-2020/sedac-logo.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The Natural Resource Protection and Child Health Indicators, 2020 Release, is produced in support of the U.S. Millennium Challenge Corporation as selection criteria for funding eligibility. The Natural Resource Protection Indicator (NRPI) and Child Health Indicator (CHI) are based on proximity-to-target scores ranging from 0 to 100 (at target). The NRPI covers 250 countries and is calculated based on the weighted average percentage of biomes under protected status. The CHI is a composite index for 194 countries derived from the average of three proximity-to-target scores for access to at least basic water and sanitation, along with child mortality. The 2020 release includes a consistent time series of NRPI scores for 2010 to 2020 and CHI scores for 2010 to 2019.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.7927%2F7ppx-6m60",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.7927%2F7ppx-6m60",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/downloads/maps/nrmi/nrmi-natural-resource-protection-child-health-indicators-2020/sedac-logo.jpg",
-                    "description": "Sample browse graphic of the data set.",
                     "@type": "dcat:Distribution",
+                    "description": "Sample browse graphic of the data set.",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/downloads/maps/nrmi/nrmi-natural-resource-protection-child-health-indicators-2020/sedac-logo.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/nrmi-natural-resource-protection-child-health-indicators-2020/data-download",
-                    "description": "Data Download Page",
                     "@type": "dcat:Distribution",
+                    "description": "Data Download Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/nrmi-natural-resource-protection-child-health-indicators-2020/data-download",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://sedac.ciesin.columbia.edu/data/set/nrmi-natural-resource-protection-child-health-indicators-2020/docs",
-                    "description": "Documentation Page",
                     "@type": "dcat:Distribution",
+                    "description": "Documentation Page",
+                    "downloadURL": "http://sedac.ciesin.columbia.edu/data/set/nrmi-natural-resource-protection-child-health-indicators-2020/docs",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/nrmi-natural-resource-protection-child-health-indicators-2020",
-                    "description": "Data Set\u00a0Overview Page",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set\u00a0Overview Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/nrmi-natural-resource-protection-child-health-indicators-2020",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "graphic-preview-description": "Sample browse graphic of the data set.",
+            "graphic-preview-file": "https://sedac.ciesin.columbia.edu/downloads/maps/nrmi/nrmi-natural-resource-protection-child-health-indicators-2020/sedac-logo.jpg",
+            "identifier": "C2146191194-SEDAC",
+            "issued": "2010-01-01",
+            "keyword": [
+                "earth science",
+                "environmental impacts",
+                "sustainability",
+                "human dimensions",
+                "public health"
+            ],
+            "landingPage": "https://doi.org/10.7927/7ppx-6m60",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2020-12-31",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "SEDAC"
+            },
+            "references": [
+                "https://doi.org/10.7927/H49G5JRZ",
+                "https://doi.org/10.7927/H45Q4T1N",
+                "https://doi.org/10.7927/H41Z4299",
+                "https://doi.org/10.7927/H4NZ85MP",
+                "https://doi.org/10.7927/H46M34RP",
+                "https://doi.org/10.7927/H4G73BM2",
+                "https://doi.org/10.7927/H48913TX",
+                "https://doi.org/10.7927/H4SQ8XGT",
+                "https://doi.org/10.7927/6t8a-es66",
+                "https://doi.org/10.7927/r6mv-sv82",
+                "https://doi.org/10.7927/n1br-dz33",
+                "https://doi.org/10.7927/5bbs-e174"
+            ],
+            "release-place": "Palisades, NY",
             "spatial": "-180.0 -55.0 180.0 90.0",
+            "temporal": "2010-01-01T00:00:00Z/2020-12-31T00:00:00Z",
             "theme": [
                 "NRMI",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Natural Resource Protection and Child Health Indicators, 2020 Release"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-MIRO-2-ESC1-67P-V1.0",
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
+            "description": "This data set contains Spectroscopic, Continuum, and Engineering level 2 data, in the form of table files, taken during the COMET ESCORT 1 phase of the Rosetta mission by the MIRO instrument. The primary target of this phase of mission is 67P.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-miro-2-esc1-67p-v1.0_rkf5-stc8",
+            "issued": "2018-06-26",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-MIRO-2-ESC1-67P-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-miro-2-esc1-67p-v1.0_rkf5-stc8",
-            "description": "This data set contains Spectroscopic, Continuum, and Engineering level 2 data, in the form of table files, taken during the COMET ESCORT 1 phase of the Rosetta mission by the MIRO instrument. The primary target of this phase of mission is 67P.",
-            "title": "ROSETTA-ORBITER 67P MIRO 2 ESC1 67P V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "ROSETTA-ORBITER 67P MIRO 2 ESC1 67P V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/IMPACTS/2DVD/DATA101",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Tokay, Ali , David  Wolff and Charanjit  Pabla.2022. Two-Dimensional Video Disdrometer (2DVD) IMPACTS [indicate subset used]. Dataset available online from the NASA Global Hydrometeorology Resource Center DAAC, Huntsville, Alabama, U.S.A. DOI: http://dx.doi.org/10.5067/IMPACTS/2DVD/DATA101",
-            "issued": "2022-03-23",
-            "temporal": "2020-01-15T01:37:06Z/2020-02-28T20:41:44Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-31",
-            "keyword": [
-                "atmosphere",
-                "clouds",
-                "earth science",
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
-            "identifier": "C1995564612-GHRC_DAAC",
             "description": "The Two-Dimensional Video Disdrometer (2DVD) IMPACTS data were collected in support of the Investigation of Microphysics and Precipitation for Atlantic Coast-Threatening Snowstorms (IMPACTS) campaign. The IMPACTS field campaign addressed providing observations critical to understanding the mechanisms of snowband formation, organization, and evolution, examining how the microphysical characteristics and likely growth mechanisms of snow particles vary across snowbands, and improving snowfall remote sensing interpretation and modeling to significantly advance prediction capabilities. These data consist of the size, equivalent diameter, fall speed, oblateness, cross-sectional area of raindrops, particle concentration, total number of drops, total drop concentration, liquid water content, rain rate, reflectivity, and rain event characteristics. Data files are available from January 15, 2020 through February 28, 2020 in ASCII format.",
-            "title": "Two-Dimensional Video Disdrometer (2DVD) IMPACTS V1",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FIMPACTS%2F2DVD%2FDATA101",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FIMPACTS%2F2DVD%2FDATA101",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=2dimpacts",
-                    "description": "Files may be downloaded directly to your workstation from this link",
                     "@type": "dcat:Distribution",
+                    "description": "Files may be downloaded directly to your workstation from this link",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=2dimpacts",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
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
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/impacts/2DVD/doc/2dimpacts_dataset.pdf",
-                    "description": "The guide document contains detailed information about the dataset",
                     "@type": "dcat:Distribution",
+                    "description": "The guide document contains detailed information about the dataset",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/impacts/2DVD/doc/2dimpacts_dataset.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.1175/1520-0426(2002)019%3C0602:TDVDAD%3E2.0.CO;2",
-                    "description": "Two-Dimensional Video Disdrometer: A Description",
                     "@type": "dcat:Distribution",
+                    "description": "Two-Dimensional Video Disdrometer: A Description",
+                    "downloadURL": "https://doi.org/10.1175/1520-0426(2002)019%3C0602:TDVDAD%3E2.0.CO;2",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.1007/978-3-540-77655-0_1",
-                    "description": "The 2D-video-disdrometer, Precipitation: Advances in Measurement, Estimation and Prediction",
                     "@type": "dcat:Distribution",
+                    "description": "The 2D-video-disdrometer, Precipitation: Advances in Measurement, Estimation and Prediction",
+                    "downloadURL": "https://doi.org/10.1007/978-3-540-77655-0_1",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://dx.doi.org/10.1175/JTECH2051.1",
-                    "description": "Drop Shapes, Model Comparisons, and Calculations of Polarimetric Radar Parameters in Rain",
                     "@type": "dcat:Distribution",
+                    "description": "Drop Shapes, Model Comparisons, and Calculations of Polarimetric Radar Parameters in Rain",
+                    "downloadURL": "http://dx.doi.org/10.1175/JTECH2051.1",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.1175/1520-0450(2001)040%3C2083:CODSDM%3E2.0.CO;2",
-                    "description": "Comparison of Drop Size Distribution Measurements by Impact and Optical Disdrometers",
                     "@type": "dcat:Distribution",
+                    "description": "Comparison of Drop Size Distribution Measurements by Impact and Optical Disdrometers",
+                    "downloadURL": "https://doi.org/10.1175/1520-0450(2001)040%3C2083:CODSDM%3E2.0.CO;2",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.1175/1520-0450(1998)037%3C0912:RMARPA%3E2.0.CO;2",
-                    "description": "Rainfall Microphysics and Radar Properties: Analysis Methods for Drop Size Spectra",
                     "@type": "dcat:Distribution",
+                    "description": "Rainfall Microphysics and Radar Properties: Analysis Methods for Drop Size Spectra",
+                    "downloadURL": "https://doi.org/10.1175/1520-0450(1998)037%3C0912:RMARPA%3E2.0.CO;2",
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
+            "identifier": "C1995564612-GHRC_DAAC",
+            "issued": "2022-03-23",
+            "keyword": [
+                "atmosphere",
+                "clouds",
+                "earth science",
+                "precipitation"
+            ],
+            "landingPage": "https://doi.org/10.5067/IMPACTS/2DVD/DATA101",
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
             "spatial": "-75.4912 37.9194 -75.4462 37.9543",
+            "temporal": "2020-01-15T01:37:06Z/2020-02-28T20:41:44Z",
             "theme": [
                 "IMPACTS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Two-Dimensional Video Disdrometer (2DVD) IMPACTS V1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewBundle.jsp?identifier=urn%3Anasa%3Apds%3Agbo.ast-trojan.fornasier-etal.spectra&version=1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This data set contains the results of    the visible spectroscopic and photometric survey of Jupiter Trojans    reported in Fornasier et al. 2004 and Fornasier et al. 2007.  The      survey was carried out in the years 2002-2005 at the 3.5 m New         Technology Telescope of the European Southern Observatory at La Silla, Chile.    Included are visible spectroscopy and BVRI photometry of 73  Jupiter Trojans.",
+            "identifier": "urn:nasa:pds:gbo.ast-trojan.fornasier-etal.spectra",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2021-05-21",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "(24380) 2000 aa160",
                 "(105685) 2000 sc51",
@@ -1312422,39 +1312424,39 @@
                 "multiple asteroids",
                 "none"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewBundle.jsp?identifier=urn%3Anasa%3Apds%3Agbo.ast-trojan.fornasier-etal.spectra&version=1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:gbo.ast-trojan.fornasier-etal.spectra",
-            "description": "This data set contains the results of    the visible spectroscopic and photometric survey of Jupiter Trojans    reported in Fornasier et al. 2004 and Fornasier et al. 2007.  The      survey was carried out in the years 2002-2005 at the 3.5 m New         Technology Telescope of the European Southern Observatory at La Silla, Chile.    Included are visible spectroscopy and BVRI photometry of 73  Jupiter Trojans.",
-            "title": "SPECTROSCOPY AND PHOTOMETRY OF JUPITER TROJANS",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "SPECTROSCOPY AND PHOTOMETRY OF JUPITER TROJANS"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=GO-J-NIMS-3-TUBE-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "The natural form of imaging spectrometer data is the spectral image cube. It is normally in band sequential format, but has a dual nature. It is a series of 'images' of the target, each in a different wavelength, in ascending order. It is also a set of spectra, each at a particular line and sample, over the target area. Each spectrum describes a small portion of the area. When transformed into cubes, the data may be analyzed spatially, an image at a time, or spectrally, a spectrum at a time, or in more complex spatial-spectral fashion.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.go-j-nims-3-tube-v1.0_rkhq-pzds",
             "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "j rings",
                 "jupiter",
@@ -1312466,99 +1312468,75 @@
                 "callisto",
                 "ganymede"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=GO-J-NIMS-3-TUBE-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.go-j-nims-3-tube-v1.0_rkhq-pzds",
-            "description": "The natural form of imaging spectrometer data is the spectral image cube. It is normally in band sequential format, but has a dual nature. It is a series of 'images' of the target, each in a different wavelength, in ascending order. It is also a set of spectra, each at a particular line and sample, over the target area. Each spectrum describes a small portion of the area. When transformed into cubes, the data may be analyzed spatially, an image at a time, or spectrally, a spectrum at a time, or in more complex spatial-spectral fashion.",
-            "title": "GALILEO NIMS SPECTRAL IMAGE TUBES: JUPITER OPERATIONS",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "GALILEO NIMS SPECTRAL IMAGE TUBES: JUPITER OPERATIONS"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG2-N-LECP-3-RDR-STEP-3MIN-V1.0",
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
-                "neptune"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This far encounter step data set consists of the counting rate and flux data for electrons and ions from the Low Energy Charged Particle (LECP) experiment on Voyager 2 while the spacecraft was within the vicinity of Neptune. This instrument measures the intensities of in-situ charged particles ( >13 keV electrons and >24 keV ions) with various levels of discrimination based on energy range and mass species. A subset of almost 100 LECP channels are included in this data set. The LECP data are globally calibrated to the extent possible.  Particles include electrons, protons, alpha particles, and light, medium, and heavy nuclei particles.  The far encounter data are 3.2 minute rate and flux measurements within 1/8 of the LECP instrumental motor rotation period (the angular scanning periods, or step period).",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg2-n-lecp-3-rdr-step-3min-v1.0_rkhy-ccvc",
+            "issued": "2021-05-21",
+            "keyword": [
+                "voyager",
+                "neptune"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG2-N-LECP-3-RDR-STEP-3MIN-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg2-n-lecp-3-rdr-step-3min-v1.0_rkhy-ccvc",
-            "description": "This far encounter step data set consists of the counting rate and flux data for electrons and ions from the Low Energy Charged Particle (LECP) experiment on Voyager 2 while the spacecraft was within the vicinity of Neptune. This instrument measures the intensities of in-situ charged particles ( >13 keV electrons and >24 keV ions) with various levels of discrimination based on energy range and mass species. A subset of almost 100 LECP channels are included in this data set. The LECP data are globally calibrated to the extent possible.  Particles include electrons, protons, alpha particles, and light, medium, and heavy nuclei particles.  The far encounter data are 3.2 minute rate and flux measurements within 1/8 of the LECP instrumental motor rotation period (the angular scanning periods, or step period).",
-            "title": "VG2 LECP 3.2 MINUTE NEPTUNE\n                                      FAR ENCOUNTER STEP DATA",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "VG2 LECP 3.2 MINUTE NEPTUNE\n                                      FAR ENCOUNTER STEP DATA"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C2248663220-GES_DISC.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "OCO-2 Science Team/Michael Gunson, Annmarie Eldering. 2019-07-01. OCO2_Eph. Version 11r. OCO-2 Level 0 spacecraft ephemerides, Retrospective Processing V11r. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://disc.gsfc.nasa.gov/datacollection/OCO2_Eph_11r.html. Digital Science Data.",
-            "issued": "2019-06-27",
-            "temporal": "2014-07-02T00:00:00Z/2023-02-28T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2017-06-17",
-            "keyword": [
-                "platform characteristics",
-                "spectral/engineering",
-                "earth science"
-            ],
-            "data-presentation-form": "Digital Science Data",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "KRISTAN MORGAN",
                 "hasEmail": "mailto:kristan.l.morgan@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
-            "identifier": "C2248663220-GES_DISC",
-            "description": "Version 11r is the current version of the data set. Older versions will no longer be available and are superseded by Version 11r.\n\nThe Orbiting Carbon Observatory is the first NASA mission designed to collect space-based measurements of atmospheric carbon dioxide with the precision, resolution, and coverage needed to characterize the processes controlling its buildup in the atmosphere. The OCO-2 project uses the LEOStar-2 spacecraft that carries a single instrument. It incorporates three high-resolution spectrometers that make coincident measurements of reflected sunlight in the near-infrared CO2 near 1.61 and 2.06 micrometers and in molecular oxygen (O2) A-Band at 0.76 micrometers . Each band has 1016 spectral elements.This product contains the position and velocity of the spacecraft for each orbit. It is generated using the following input data:+ APID 20 telemetry+ Orbit Boundary File.It is essential in generating the Geolocations of the science data.This is the retrospective processing where the calibration data is estimated from the full timeseries of data (before, during, and after the measurements), and is expected to be of slightly higher quality.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "OCO2_Eph",
             "creator": "OCO-2 Science Team/Michael Gunson, Annmarie Eldering",
-            "title": "OCO-2 Level 0 spacecraft ephemerides, Retrospective Processing V11r (OCO2_Eph) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/OCO2_Eph_8r.jpeg",
-            "programCode": [
-                "026:001"
-            ],
+            "data-presentation-form": "Digital Science Data",
+            "description": "Version 11r is the current version of the data set. Older versions will no longer be available and are superseded by Version 11r.\n\nThe Orbiting Carbon Observatory is the first NASA mission designed to collect space-based measurements of atmospheric carbon dioxide with the precision, resolution, and coverage needed to characterize the processes controlling its buildup in the atmosphere. The OCO-2 project uses the LEOStar-2 spacecraft that carries a single instrument. It incorporates three high-resolution spectrometers that make coincident measurements of reflected sunlight in the near-infrared CO2 near 1.61 and 2.06 micrometers and in molecular oxygen (O2) A-Band at 0.76 micrometers . Each band has 1016 spectral elements.This product contains the position and velocity of the spacecraft for each orbit. It is generated using the following input data:+ APID 20 telemetry+ Orbit Boundary File.It is essential in generating the Geolocations of the science data.This is the retrospective processing where the calibration data is estimated from the full timeseries of data (before, during, and after the measurements), and is expected to be of slightly higher quality.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -1312567,445 +1312545,447 @@
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/OCO2_Eph_11r.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/OCO2_Eph_11r.html",
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
-                    "downloadURL": "https://oco2.gesdisc.eosdis.nasa.gov/opendap/OCO2_Eph.11r/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://oco2.gesdisc.eosdis.nasa.gov/opendap/OCO2_Eph.11r/contents.html",
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
-                    "downloadURL": "https://oco2.gesdisc.eosdis.nasa.gov/data/OCO2_DATA/OCO2_Eph.11r/",
-                    "description": "Access the data via HTTP.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTP.",
+                    "downloadURL": "https://oco2.gesdisc.eosdis.nasa.gov/data/OCO2_DATA/OCO2_Eph.11r/",
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
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/OCO2_Eph_8r.jpeg",
+            "identifier": "C2248663220-GES_DISC",
+            "issued": "2019-06-27",
+            "keyword": [
+                "platform characteristics",
+                "spectral/engineering",
+                "earth science"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C2248663220-GES_DISC.html",
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
+            "series-name": "OCO2_Eph",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2014-07-02T00:00:00Z/2023-02-28T00:00:00Z",
             "theme": [
                 "OCO-2",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "OCO-2 Level 0 spacecraft ephemerides, Retrospective Processing V11r (OCO2_Eph) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "issue-identification": "GSSTFSC_2c",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/MEASURES/GSSTF/DATA319",
             "citation": "Shie, C.-L., K. Hilburn, L. S. Chiu, R. Adler, I-I Lin, E. Nelkin, and J. Ardizzone. Andrey Savtchenko. 2011-11-18. GSSTFSC. Version 2c. Goddard Satellite-Based Surface Turbulent Fluxes, 1x1 deg Seasonal Climatology, Set1 and NCEP V2c. Greenbelt, MD, USA. GSSTFSC_2c. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/MEASURES/GSSTF/DATA319. https://disc.gsfc.nasa.gov/datacollection/GSSTFSC_2c.html. Digital Science Data.",
-            "issued": "2011-11-18",
-            "temporal": "1988-03-01T00:00:00Z/2008-11-30T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2011-11-18",
-            "keyword": [
-                "ocean heat budget",
-                "atmosphere",
-                "atmospheric pressure",
-                "atmospheric radiation",
-                "atmospheric temperature",
-                "atmospheric water vapor",
-                "atmospheric winds",
-                "earth science",
-                "ocean pressure",
-                "oceans",
-                "ocean temperature",
-                "ocean winds"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "DAVID SILBERSTEIN",
                 "hasEmail": "mailto:david.s.silberstein@nasa.gov"
             },
+            "creator": "Shie, C.-L., K. Hilburn, L. S. Chiu, R. Adler, I-I Lin, E. Nelkin, and J. Ardizzone",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C1237113469-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "These data are the Goddard Satellite-based Surface Turbulent Fluxes Version-2c Dataset recently produced through a MEaSUREs funded project led by Dr. Chung-Lin Shie (UMBC/GEST, NASA/GSFC), converted to HDF-EOS5 format. The stewardship of this HDF-EOS5 dataset is part of the MEaSUREs project. \n\nThis is the Seasonal Climatology product; data are projected to equidistant Grid that covers the globe at 1x1 degree cell size, resulting in data arrays of 360x180 size. The seasonal product is a result of averaging of three consecutive months: December-February, March-May, June-August, and September-November.  There is one HDF-EOS5 file per season. A finer resolution, 0.25 deg,  of this product has been released as Version 3. \n\nStarting with Version 2c, there is only one set of Combined data, \"Set1\". The Seasonal Climatology HDF-EOS5 file also contains one extra grid of NCEP Climatology, \"NCEP\".\n      \nThe seasonal temporal and one-degree spatial resolution of the product can be used to examining climate variability at these scales. Oceanic evaporation contributes to the net fresh water input to the oceans and drives the upper ocean density structure and consequently the circulation of the oceans.\n\nThe short name for this product is GSSTFSC.",
-            "editor": "Andrey Savtchenko",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "GSSTFSC",
-            "creator": "Shie, C.-L., K. Hilburn, L. S. Chiu, R. Adler, I-I Lin, E. Nelkin, and J. Ardizzone",
-            "graphic-preview-description": "Goddard Satellite-based Surface Turbulent Fluxes (GSSTF)  Precipitable Water Seasonal Climatology 1 x 1 degree June-August (1988-2008) [g/cm2]",
-            "title": "Goddard Satellite-Based Surface Turbulent Fluxes, 1x1 deg Seasonal Climatology, Set1 and NCEP V2c (GSSTFSC) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/GSSTFSC_2c.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMEASURES%2FGSSTF%2FDATA319",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMEASURES%2FGSSTF%2FDATA319",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/GSSTFSC_2c.png",
-                    "description": "Goddard Satellite-based Surface Turbulent Fluxes (GSSTF)  Precipitable Water Seasonal Climatology 1 x 1 degree June-August (1988-2008) [g/cm2]\n      ",
                     "@type": "dcat:Distribution",
+                    "description": "Goddard Satellite-based Surface Turbulent Fluxes (GSSTF)  Precipitable Water Seasonal Climatology 1 x 1 degree June-August (1988-2008) [g/cm2]\n      ",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/GSSTFSC_2c.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/GSSTFSC_2c.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/GSSTFSC_2c.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://measures.gesdisc.eosdis.nasa.gov/data/GSSTF/GSSTFSC.2c/",
-                    "description": "Access the data via HTTP.\n     ",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTP.\n     ",
+                    "downloadURL": "https://measures.gesdisc.eosdis.nasa.gov/data/GSSTF/GSSTFSC.2c/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://measures.gesdisc.eosdis.nasa.gov/data/GSSTF/GSSTFSC.2c/doc/Readme.GSSTF2c.pdf",
-                    "description": "README Document\n      ",
                     "@type": "dcat:Distribution",
+                    "description": "README Document\n      ",
+                    "downloadURL": "https://measures.gesdisc.eosdis.nasa.gov/data/GSSTF/GSSTFSC.2c/doc/Readme.GSSTF2c.pdf",
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
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=GSSTFSC_2c",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=GSSTFSC_2c",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://measures.gesdisc.eosdis.nasa.gov/opendap/GSSTF/GSSTFSC.2c",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://measures.gesdisc.eosdis.nasa.gov/opendap/GSSTF/GSSTFSC.2c",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 }
             ],
+            "editor": "Andrey Savtchenko",
+            "graphic-preview-description": "Goddard Satellite-based Surface Turbulent Fluxes (GSSTF)  Precipitable Water Seasonal Climatology 1 x 1 degree June-August (1988-2008) [g/cm2]",
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/GSSTFSC_2c.png",
+            "identifier": "C1237113469-GES_DISC",
+            "issue-identification": "GSSTFSC_2c",
+            "issued": "2011-11-18",
+            "keyword": [
+                "ocean heat budget",
+                "atmosphere",
+                "atmospheric pressure",
+                "atmospheric radiation",
+                "atmospheric temperature",
+                "atmospheric water vapor",
+                "atmospheric winds",
+                "earth science",
+                "ocean pressure",
+                "oceans",
+                "ocean temperature",
+                "ocean winds"
+            ],
+            "landingPage": "https://doi.org/10.5067/MEASURES/GSSTF/DATA319",
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
+            "series-name": "GSSTFSC",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "1988-03-01T00:00:00Z/2008-11-30T23:59:59.999Z",
             "theme": [
                 "MEaSUREs",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Goddard Satellite-Based Surface Turbulent Fluxes, 1x1 deg Seasonal Climatology, Set1 and NCEP V2c (GSSTFSC) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-EXT1-1382-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the ROSETTA EXTENSION 1 phase 2016-01-01 to 2016-04-05. It is a Global Gravity measurement at the comet 67P and covers the time 2016-01-30T05:35:00.000 to 2016-01-30T09:01:21.500.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-ext1-1382-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-EXT1-1382-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-ext1-1382-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the ROSETTA EXTENSION 1 phase 2016-01-01 to 2016-04-05. It is a Global Gravity measurement at the comet 67P and covers the time 2016-01-30T05:35:00.000 to 2016-01-30T09:01:21.500.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     ROSETTA EXTENSION 1 1382 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     ROSETTA EXTENSION 1 1382 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-PRL-0306-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the PRELANDING phase 2014-01-21 to 2014-11-18. It is a Global Gravity measurement at the comet 67P and covers the time 2014-09-20T16:50:05.000 to 2014-09-21T00:27:41.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-prl-0306-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-PRL-0306-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-prl-0306-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the PRELANDING phase 2014-01-21 to 2014-11-18. It is a Global Gravity measurement at the comet 67P and covers the time 2014-09-20T16:50:05.000 to 2014-09-21T00:27:41.000.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     PRELANDING 0306 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     PRELANDING 0306 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MRO-M-CRISM-6-DDR-V1.0",
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
+            "description": "This dataset is intended to include information on observation conditions, physical properties and coordinates of IR and VNIR data cubes from the CRISM instrument on MRO when the data cubes are pointed at Mars' surface. The information is mapped to the sensor space of non-map-projected data, EDRs and TRDRs.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mro-m-crism-6-ddr-v1.0_rm4i-a9mq",
+            "issued": "2021-05-21",
+            "keyword": [
+                "mars",
+                "mars reconnaissance orbiter"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MRO-M-CRISM-6-DDR-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mro-m-crism-6-ddr-v1.0_rm4i-a9mq",
-            "description": "This dataset is intended to include information on observation conditions, physical properties and coordinates of IR and VNIR data cubes from the CRISM instrument on MRO when the data cubes are pointed at Mars' surface. The information is mapped to the sensor space of non-map-projected data, EDRs and TRDRs.",
-            "title": "MRO CRISM DERIVED DATA RECORD V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "MRO CRISM DERIVED DATA RECORD V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.nasa.gov/d/rm4k-r5gy",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "keyword": [
-                "['sample collection' 'extraction' 'mass spectrometry' 'data transformation']",
-                "['spaceflight' 'bed rest' 'time' 'dry immersion']"
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
-            "identifier": "nasa_genelab_GLDS-353_rm4k-r5gy",
             "description": "['The aim of the study was to continue of the proteomic data accumulation on the effects of space flight factors on the human body, including ground-based model experiments. Blood plasma samples were collected from 5 healthy men included in the 21 days head-down bed rest experiment (HDBR) and 5 volunteers participating in a 21 day long dry immersion experiment.']",
-            "title": "['The Effects of Spaceflight Factors on the Human Plasma Proteome, Including Both Real Space Missions and Ground-Based Experiments']",
-            "programCode": [
-                "026:005"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-353",
-                    "description": "GeneLab Study Page",
                     "@type": "dcat:Distribution",
+                    "description": "GeneLab Study Page",
+                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-353",
+                    "mediaType": "text/html",
                     "title": "['The Effects of Spaceflight Factors on the Human Plasma Proteome, Including Both Real Space Missions and Ground-Based Experiments']"
                 }
             ],
+            "identifier": "nasa_genelab_GLDS-353_rm4k-r5gy",
+            "issued": "2021-05-21",
+            "keyword": [
+                "['sample collection' 'extraction' 'mass spectrometry' 'data transformation']",
+                "['spaceflight' 'bed rest' 'time' 'dry immersion']"
+            ],
+            "landingPage": "https://data.nasa.gov/d/rm4k-r5gy",
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
+            "title": "['The Effects of Spaceflight Factors on the Human Plasma Proteome, Including Both Real Space Missions and Ground-Based Experiments']"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC1-0578-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 1 phase 2014-11-20 to 2015-03-10. It is a Global Gravity measurement at the comet 67P and covers the time 2015-02-13T00:50:05.000 to 2015-02-13T10:27:32.500.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc1-0578-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC1-0578-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc1-0578-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 1 phase 2014-11-20 to 2015-03-10. It is a Global Gravity measurement at the comet 67P and covers the time 2015-02-13T00:50:05.000 to 2015-02-13T10:27:32.500.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 1 0578 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 1 0578 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.nasa.gov/d/rm5p-3gg4",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2018-06-25",
-            "temporal": "1977-01-01/1996-01-01",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
-            "keyword": [
-                "knowledge sharing",
-                "space science",
-                "planetary science",
-                "safety",
-                "forums",
-                "geography"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Paul Schenk",
                 "hasEmail": "mailto:schenk@lpi.usra.edu"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Aeronautics and Space Administration"
-            },
-            "identifier": "NASA-0000036__2",
+            "describedBy": "http://www.lpi.usra.edu/resources/gc/gcreadme.html",
             "description": "This web page leads to a database of images and information about the 150 major impact craters on Ganymede and is updated semi-regularly based on continuing analysis of Voyager 2 images.",
-            "title": "Ganymede Crater Database",
-            "programCode": [
-                "026:009"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -1313013,256 +1312993,290 @@
                     "mediaType": "text/html"
                 }
             ],
-            "describedBy": "http://www.lpi.usra.edu/resources/gc/gcreadme.html",
-            "accrualPeriodicity": "irregular",
+            "identifier": "NASA-0000036__2",
+            "issued": "2018-06-25",
+            "keyword": [
+                "knowledge sharing",
+                "space science",
+                "planetary science",
+                "safety",
+                "forums",
+                "geography"
+            ],
+            "landingPage": "https://data.nasa.gov/d/rm5p-3gg4",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:009"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Aeronautics and Space Administration"
+            },
+            "temporal": "1977-01-01/1996-01-01",
             "theme": [
                 "Space Science"
-            ]
+            ],
+            "title": "Ganymede Crater Database"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/IMPACTS/CEILOMETERS/DATA101",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Kollias, Pavlos  and Mariko  Oue.2022. SBU Ceilometers IMPACTS [indicate subset used]. Dataset available online from the NASA Global Hydrometeorology Resource Center DAAC, Huntsville, Alabama, U.S.A. DOI: http://dx.doi.org/10.5067/IMPACTS/CEILOMETERS/DATA101",
-            "issued": "2022-03-23",
-            "temporal": "2020-01-01T00:00:00Z/2020-02-27T23:59:47Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-31",
-            "keyword": [
-                "clouds",
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
-            "identifier": "C1995869065-GHRC_DAAC",
             "description": "The SBU Ceilometers IMPACTS dataset includes ceilometer cloud height measurements collected by the Vaisala CL51, Vaisala CT25K, and Lufft Ceilometer CHM 15k ceilometers operated by the State University of New York (SUNY) Stony Brook University. These data were collected during the Investigation of Microphysics and Precipitation for Atlantic Coast-Threatening Snowstorms (IMPACTS) field campaign, a three-year sequence of winter season deployments conducted to study snowstorms over the U.S. Atlantic coast. IMPACTS aimed to (1) Provide observations critical to understanding the mechanisms of snowband formation, organization, and evolution; (2) Examine how the microphysical characteristics and likely growth mechanisms of snow particles vary across snowbands;  and (3) Improve snowfall remote sensing interpretation and modeling to significantly advance prediction capabilities. The ceilometer dataset files are available from January 1 through February 27, 2020 in netCDF-3 format.",
-            "title": "SBU Ceilometers IMPACTS V1",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FIMPACTS%2FCEILOMETERS%2FDATA101",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FIMPACTS%2FCEILOMETERS%2FDATA101",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=sbuceilimpacts",
-                    "description": "Files may be downloaded directly to your workstation from this link",
                     "@type": "dcat:Distribution",
+                    "description": "Files may be downloaded directly to your workstation from this link",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=sbuceilimpacts",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
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
-                    "downloadURL": "https://you.stonybrook.edu/radar/observatory/ancillary-instruments/",
-                    "description": "SBU Ancillary Instruments Information",
                     "@type": "dcat:Distribution",
+                    "description": "SBU Ancillary Instruments Information",
+                    "downloadURL": "https://you.stonybrook.edu/radar/observatory/ancillary-instruments/",
+                    "mediaType": "text/html",
                     "title": "View information related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://www.vaisala.com/sites/default/files/documents/CL51-Datasheet-B210861EN.pdf",
-                    "description": "Ceilometer Instrument Information",
                     "@type": "dcat:Distribution",
+                    "description": "Ceilometer Instrument Information",
+                    "downloadURL": "https://www.vaisala.com/sites/default/files/documents/CL51-Datasheet-B210861EN.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View information related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/uso/ds_docs/gpmgv/gcpex/gpmceilgcpex/CEILOMETER_CT25K_UserGuide.pdf",
-                    "description": "Ceilometer Instrument Information",
                     "@type": "dcat:Distribution",
+                    "description": "Ceilometer Instrument Information",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/uso/ds_docs/gpmgv/gcpex/gpmceilgcpex/CEILOMETER_CT25K_UserGuide.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View information related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://www.esrl.noaa.gov/psd/psd3/cruises/CT25K.pdf",
-                    "description": "Ceilometer Instrument Information",
                     "@type": "dcat:Distribution",
+                    "description": "Ceilometer Instrument Information",
+                    "downloadURL": "https://www.esrl.noaa.gov/psd/psd3/cruises/CT25K.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View information related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/impacts/SBU_Ceilometer/doc/sbuceilimpacts_dataset.pdf",
-                    "description": "The guide document contains detailed information about the dataset",
                     "@type": "dcat:Distribution",
+                    "description": "The guide document contains detailed information about the dataset",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/impacts/SBU_Ceilometer/doc/sbuceilimpacts_dataset.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
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
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/home/field-campaigns/impacts",
-                    "description": "IMPACTS Field Campaign Project Page",
                     "@type": "dcat:Distribution",
+                    "description": "IMPACTS Field Campaign Project Page",
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
+            "identifier": "C1995869065-GHRC_DAAC",
+            "issued": "2022-03-23",
+            "keyword": [
+                "clouds",
+                "earth science",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.5067/IMPACTS/CEILOMETERS/DATA101",
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
             "spatial": "-73.1278 40.8967 -73.0297 40.9653",
+            "temporal": "2020-01-01T00:00:00Z/2020-02-27T23:59:47Z",
             "theme": [
                 "IMPACTS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "SBU Ceilometers IMPACTS V1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/71",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Blad, B. L., and R. Vining. 1994. Radiant Temp[erature]. Multiangle Data (FIFE). Data set. Available on-line [http://www.daac.ornl.gov] from Oak Ridge National Laboratory Distributed Active Archive Center, Oak Ridge, Tennessee, U.S.A. Also published in D. E. Strebel, D. R. Landis, K. F. Huemmrich, and B. W. Meeson (eds.), Collected Data of the First ISLSCP Field Experiment, Vol. 1: Surface Observations and Non-Image Data Sets. CD-ROM. National Aeronautics and Space Administration, Goddard Space Flight Center, Greenbelt, Maryland, U.S.A. (available from http://www.daac.ornl.gov). doi:10.3334/ORNLDAAC/71",
-            "issued": "2024-05-05",
-            "temporal": "1989-07-12T00:00:00Z/1989-08-10T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-07",
-            "keyword": [
-                "surface thermal properties",
-                "land surface",
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
-            "identifier": "C2980518647-ORNL_CLOUD",
             "description": "Surface temp. measured w/ Everest IRT, multiple angles & Eppley IR Radiometer",
-            "graphic-preview-description": "Browse Image",
-            "title": "Radiant Temp. Multiangle Data (FIFE)",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/fife_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F71",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F71",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/fife/fife_sur_refl_irt_mult/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/fife/fife_sur_refl_irt_mult/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/FIFE/guides/Radiant_Temp_Multiangle_Data.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/FIFE/guides/Radiant_Temp_Multiangle_Data.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/71",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/71",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/msword",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/fife/fife_sur_refl_irt_grnd/comp/irt_mult.doc",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/fife/fife_sur_refl_irt_grnd/comp/irt_mult.doc",
+                    "mediaType": "application/msword",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/fife/fife_sur_refl_irt_grnd/comp/irt_mult.tdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/fife/fife_sur_refl_irt_grnd/comp/irt_mult.tdf",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/fife/fife_sur_refl_irt_grnd/comp/Radiant_Temp_Multiangle_Data.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/fife/fife_sur_refl_irt_grnd/comp/Radiant_Temp_Multiangle_Data.pdf",
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
+            "identifier": "C2980518647-ORNL_CLOUD",
+            "issued": "2024-05-05",
+            "keyword": [
+                "surface thermal properties",
+                "land surface",
+                "atmospheric radiation",
+                "earth science",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/71",
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
             "spatial": "-96.55 39.05 -96.54 39.09",
+            "temporal": "1989-07-12T00:00:00Z/1989-08-10T23:59:59Z",
             "theme": [
                 "FIFE",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Radiant Temp. Multiangle Data (FIFE)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.nasa.gov/d/rm9m-qfwu",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "GeneLab Outreach",
+                "hasEmail": "mailto:genelab-outreach@lists.nasa.gov"
+            },
+            "description": "The microbial tracking-1 (MT-1) investigation allowed the characterization of the microbial population aboard the International Space Station (ISS).",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "GeneLab Study Page",
+                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-302",
+                    "mediaType": "text/html",
+                    "title": "ISS Enterobacteriales Genomes"
+                }
+            ],
+            "identifier": "nasa_genelab_GLDS-302_rm9m-qfwu",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
             "keyword": [
                 "sequence assembly",
                 "nucleic acid sequencing",
@@ -1313272,175 +1313286,136 @@
                 "library construction",
                 "nucleic acid extraction"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "GeneLab Outreach",
-                "hasEmail": "mailto:genelab-outreach@lists.nasa.gov"
-            },
+            "landingPage": "https://data.nasa.gov/d/rm9m-qfwu",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "nasa_genelab_GLDS-302_rm9m-qfwu",
-            "description": "The microbial tracking-1 (MT-1) investigation allowed the characterization of the microbial population aboard the International Space Station (ISS).",
-            "title": "ISS Enterobacteriales Genomes",
-            "programCode": [
-                "026:005"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-302",
-                    "description": "GeneLab Study Page",
-                    "@type": "dcat:Distribution",
-                    "title": "ISS Enterobacteriales Genomes"
-                }
-            ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ISS Enterobacteriales Genomes"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-CAL%2FX-ALICE-2-EAR1-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This data set contains CODMAC level 2 instrument checkout data acquired by the Rosetta Orbiter ALICE UV Spectrometer during the first earth swing-by phase of the Rosetta mission, which occurred 2004-10-17 to 2005-04-04.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-cal-x-alice-2-ear1-v1.0_rmak-92dy",
             "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "international rosetta mission",
                 "unknown",
                 "calibration",
                 "moon"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-CAL%2FX-ALICE-2-EAR1-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-cal-x-alice-2-ear1-v1.0_rmak-92dy",
-            "description": "This data set contains CODMAC level 2 instrument checkout data acquired by the Rosetta Orbiter ALICE UV Spectrometer during the first earth swing-by phase of the Rosetta mission, which occurred 2004-10-17 to 2005-04-04.",
-            "title": "ROSETTA-ORBITER CAL/CHECK ALICE 2 EAR1 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "ROSETTA-ORBITER CAL/CHECK ALICE 2 EAR1 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/8XXUQU7HBGBL",
             "citation": "OCO-2/OCO-3 Science Team, Vivienne Payne, Abhishek Chatterjee. 2024-04-01. OCO2_L2_Lite_SIF. Version 11.2r. OCO-2 Level 2 bias-corrected solar-induced fluorescence and other select fields from the IMAP-DOAS algorithm aggregated as daily files, Retrospective processing V11.2r. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/8XXUQU7HBGBL. https://disc.gsfc.nasa.gov/datacollection/OCO2_L2_Lite_SIF_11.2r.html. Digital Science Data.",
-            "issued": "2020-08-01",
-            "temporal": "2014-09-01T00:00:00Z/2024-10-07T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-03-01",
-            "keyword": [
-                "vegetation",
-                "atmosphere",
-                "atmospheric chemistry",
-                "biosphere",
-                "earth science"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "KRISTAN MORGAN",
                 "hasEmail": "mailto:kristan.l.morgan@nasa.gov"
             },
+            "creator": "OCO-2/OCO-3 Science Team, Vivienne Payne, Abhishek Chatterjee",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C2912084771-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "Version 11.2r is the current version of the data set. Older versions will no longer be available and are superseded by Version 11r.\n\nThe OCO-2 SIF Lite files contain bias-corrected solar induced chlorophyll fluorescence along with other select fields aggregated as daily files. \n\nThe Orbiting Carbon Observatory is the first NASA mission designed to collect space-based measurements of atmospheric carbon dioxide with the precision, resolution, and coverage needed to characterize the processes controlling its buildup in the atmosphere. The OCO-2 project uses the LEOStar-2 spacecraft that carries a single instrument. It incorporates three high-resolution spectrometers that make coincident measurements of reflected sunlight in the near-infrared CO2 near 1.61 and 2.06 micrometers and in molecular oxygen (O2) A-Band at 0.76 micrometers.\nThis collection encompass the output from the IMAP-DOAS preprocessor, which is used for both screening of the official XCO2 product as well as for the retrieval of Solar-Induced Fluorescence from the 0.76 micrometer O2 A-band. The IMAP-DOAS preprocessor, just as the ABO2 cloud screen, is implemented in the operational OCO-2 processing pipeline.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "OCO2_L2_Lite_SIF",
-            "creator": "OCO-2/OCO-3 Science Team, Vivienne Payne, Abhishek Chatterjee",
-            "title": "OCO-2 Level 2 bias-corrected solar-induced fluorescence and other select fields from the IMAP-DOAS algorithm aggregated as daily files, Retrospective processing V11.2r (OCO2_L2_Lite_SIF) at GES DISC",
-            "graphic-preview-description": "OCO-2 L2 Lite Product , Solar-Induced Chlorophyll Fluorescence, (SIF) at 757nm, one day (3/31/2022), variable \"Daily_SIF_757nm\", in W/m^2/sr/micron units. Note that, although the data range is truncated at 0, small negatives values are retained in the data to avoid positive biases in SIF distributions.",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/OCO/OCO2_L2_Lite_SIF_v11r__20220331.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2F8XXUQU7HBGBL",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2F8XXUQU7HBGBL",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/OCO/OCO2_L2_Lite_SIF_v11r__20220331.png",
-                    "description": "OCO-2 L2 Lite Product , Solar-Induced Chlorophyll Fluorescence, (SIF) at 757nm, one day (3/31/2022), variable \"Daily_SIF_757nm\", in W/m^2/sr/micron units. Note that, although the data range is truncated at 0, small negatives values are retained in the data to avoid positive biases in SIF distributions.",
                     "@type": "dcat:Distribution",
+                    "description": "OCO-2 L2 Lite Product , Solar-Induced Chlorophyll Fluorescence, (SIF) at 757nm, one day (3/31/2022), variable \"Daily_SIF_757nm\", in W/m^2/sr/micron units. Note that, although the data range is truncated at 0, small negatives values are retained in the data to avoid positive biases in SIF distributions.",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/OCO/OCO2_L2_Lite_SIF_v11r__20220331.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/OCO2_L2_Lite_SIF_11.2r.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/OCO2_L2_Lite_SIF_11.2r.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://oco2.gesdisc.eosdis.nasa.gov/data/OCO2_DATA/OCO2_L2_Lite_SIF.11.2r/",
-                    "description": "Access the data via HTTP",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTP",
+                    "downloadURL": "https://oco2.gesdisc.eosdis.nasa.gov/data/OCO2_DATA/OCO2_L2_Lite_SIF.11.2r/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=OCO2_L2_Lite_SIF",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=OCO2_L2_Lite_SIF",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
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
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/OCO/OCO23_SIF_B10_Product_Description.pdf",
-                    "description": "User's Guide",
                     "@type": "dcat:Distribution",
+                    "description": "User's Guide",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/OCO/OCO23_SIF_B10_Product_Description.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/OCO/OCO2_XCO2_Lite_Files_and_Bias_Correction.pdf",
-                    "description": "Details of the Lite files contents",
                     "@type": "dcat:Distribution",
+                    "description": "Details of the Lite files contents",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/OCO/OCO2_XCO2_Lite_Files_and_Bias_Correction.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
@@ -1313450,98 +1313425,125 @@
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
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://oco2.gesdisc.eosdis.nasa.gov/opendap/OCO2_L2_Lite_SIF.11r/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://oco2.gesdisc.eosdis.nasa.gov/opendap/OCO2_L2_Lite_SIF.11r/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 }
             ],
+            "graphic-preview-description": "OCO-2 L2 Lite Product , Solar-Induced Chlorophyll Fluorescence, (SIF) at 757nm, one day (3/31/2022), variable \"Daily_SIF_757nm\", in W/m^2/sr/micron units. Note that, although the data range is truncated at 0, small negatives values are retained in the data to avoid positive biases in SIF distributions.",
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/OCO/OCO2_L2_Lite_SIF_v11r__20220331.png",
+            "identifier": "C2912084771-GES_DISC",
+            "issued": "2020-08-01",
+            "keyword": [
+                "vegetation",
+                "atmosphere",
+                "atmospheric chemistry",
+                "biosphere",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/8XXUQU7HBGBL",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2022-03-01",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
+            },
+            "release-place": "Greenbelt, MD, USA",
+            "series-name": "OCO2_L2_Lite_SIF",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2014-09-01T00:00:00Z/2024-10-07T00:00:00Z",
             "theme": [
                 "OCO-2",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "OCO-2 Level 2 bias-corrected solar-induced fluorescence and other select fields from the IMAP-DOAS algorithm aggregated as daily files, Retrospective processing V11.2r (OCO2_L2_Lite_SIF) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-X-LORRI-3-LAUNCH-V1.0",
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
+            "description": "This data set contains Calibrated data taken by the New Horizons Long Range Reconnaissance Imager instrument during the post-launch checkout mission phase.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-x-lorri-3-launch-v1.0_rmit-vbyf",
+            "issued": "2018-06-26",
+            "keyword": [
+                "new horizons",
+                "calibration"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-X-LORRI-3-LAUNCH-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-x-lorri-3-launch-v1.0_rmit-vbyf",
-            "description": "This data set contains Calibrated data taken by the New Horizons Long Range Reconnaissance Imager instrument during the post-launch checkout mission phase.",
-            "title": "NEW HORIZONS LORRI POST-LAUNCH CHECKOUT V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "NEW HORIZONS LORRI POST-LAUNCH CHECKOUT V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-X-MIRO-2-CVP-COMMISSIONING-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This data set contains Spectroscopic, Continuum and Engineering data, in the form of table files, taken during the Commissioning phase of the Rosetta mission by the MIRO instrument.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-x-miro-2-cvp-commissioning-v1.0_rmp5-ttn7",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "c/linear (2002 t7)",
                 "earth",
@@ -1313551,112 +1313553,112 @@
                 "vega",
                 "unknown"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-X-MIRO-2-CVP-COMMISSIONING-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-x-miro-2-cvp-commissioning-v1.0_rmp5-ttn7",
-            "description": "This data set contains Spectroscopic, Continuum and Engineering data, in the form of table files, taken during the Commissioning phase of the Rosetta mission by the MIRO instrument.",
-            "title": "ROSETTA-ORBITER CHECK MIRO 2 CVP COMMISSIONING V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER CHECK MIRO 2 CVP COMMISSIONING V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC4-1255-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 4 phase 2015-10-22 to 2015-12-31. It is a Global Gravity measurement at the comet 67P and covers the time 2015-12-13T09:54:35.000 to 2015-12-13T15:56:44.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc4-1255-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC4-1255-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc4-1255-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 4 phase 2015-10-22 to 2015-12-31. It is a Global Gravity measurement at the comet 67P and covers the time 2015-12-13T09:54:35.000 to 2015-12-13T15:56:44.000.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 4 1255 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 4 1255 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=DAWN-A-VIR-2-EDR-VIS-VESTA-SPECTRA-V1.0",
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
-                "4 vesta"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This volume contains the digital numbers (DN) contained in the telemetry (TM) packages of the VIR instrument on board of the spacecraft DAWN. The data are from the Vesta Encounter phase, which occurred 2011-05-03 to 2012-07-18.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.dawn-a-vir-2-edr-vis-vesta-spectra-v1.0_rmrs-emgb",
+            "issued": "2018-06-26",
+            "keyword": [
+                "dawn mission to vesta and ceres",
+                "4 vesta"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=DAWN-A-VIR-2-EDR-VIS-VESTA-SPECTRA-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.dawn-a-vir-2-edr-vis-vesta-spectra-v1.0_rmrs-emgb",
-            "description": "This volume contains the digital numbers (DN) contained in the telemetry (TM) packages of the VIR instrument on board of the spacecraft DAWN. The data are from the Vesta Encounter phase, which occurred 2011-05-03 to 2012-07-18.",
-            "title": "DAWN VIR RAW (EDR) VESTA VISIBLE SPECTRA V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "DAWN VIR RAW (EDR) VESTA VISIBLE SPECTRA V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=IUE-C-LWR-3-EDR-IUECDB-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "IUE Long-Wavelength Redundant (LWR) observations of comets",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.iue-c-lwr-3-edr-iuecdb-v1.0_rms5-qf84",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "26p/grigg-skjellerup 1 (1922 k1)",
                 "comet",
@@ -1313680,216 +1313682,189 @@
                 "c/suga-saigusa-fujikawa (1983 j1)",
                 "international ultraviolet explorer"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=IUE-C-LWR-3-EDR-IUECDB-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.iue-c-lwr-3-edr-iuecdb-v1.0_rms5-qf84",
-            "description": "IUE Long-Wavelength Redundant (LWR) observations of comets",
-            "title": "IUE LWR DATA OF COMETS",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "IUE LWR DATA OF COMETS"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VEGA2-C-SP2-2-RDR-HALLEY-V1.0",
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
-                "vega 2"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "The SP-2 experiment on Vega spacecraft was intended for studying the spatial and mass distributions of dust particles in the cometary coma over the mass range 1.e-16 to 1.e-6 g. Covering such a broad mass range was made possible by using sensors of two types, namely, impact plasma and acoustic.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vega2-c-sp2-2-rdr-halley-v1.0_rmuk-ifqv",
+            "issued": "2021-05-21",
+            "keyword": [
+                "halley",
+                "vega 2"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VEGA2-C-SP2-2-RDR-HALLEY-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vega2-c-sp2-2-rdr-halley-v1.0_rmuk-ifqv",
-            "description": "The SP-2 experiment on Vega spacecraft was intended for studying the spatial and mass distributions of dust particles in the cometary coma over the mass range 1.e-16 to 1.e-6 g. Covering such a broad mass range was made possible by using sensors of two types, namely, impact plasma and acoustic.",
-            "title": "VEGA2 DUST PARTICLE IMPACT DETECTOR DATA V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "VEGA2 DUST PARTICLE IMPACT DETECTOR DATA V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/264",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Hardy, J.P., and R.E. Davis. 1998. BOREAS HYD-03 SSA/OLD Aspen DBH Data. ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/264",
-            "issued": "2023-11-22",
-            "temporal": "1996-03-08T00:00:00Z/1996-03-08T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-11-27",
-            "keyword": [
-                "biosphere",
-                "earth science",
-                "ecosystems",
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
-            "identifier": "C2807625200-ORNL_CLOUD",
             "description": "The BOREAS HYD-03 team collected several data sets related to the hydrology of forested areas. This data set contains measurements of tree diameter at breast height (DBH) from a variety of sites. This study was undertaken to predict spatial distributions of energy transfer, snow properties important to the hydrology, remote sensing signatures, and transmissivity of gases through the snow and their relation to forests in boreal ecosystems.",
-            "graphic-preview-description": "Browse Image",
-            "title": "BOREAS HYD-03 SSA/OLD Aspen DBH Data",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/boreas_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F264",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F264",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/boreas/HYD/h03dbhd/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/boreas/HYD/h03dbhd/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/BOREAS/guides/HYD03_DBH.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/BOREAS/guides/HYD03_DBH.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/264",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/264",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/HYD/h03dbhd/comp/h03dbhd.def",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/HYD/h03dbhd/comp/h03dbhd.def",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/HYD/h03dbhd/comp/HYD03_DBH.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/HYD/h03dbhd/comp/HYD03_DBH.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/msword",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/HYD/h03dbhd/comp/HYD03_Tree_Meas.doc",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/HYD/h03dbhd/comp/HYD03_Tree_Meas.doc",
+                    "mediaType": "application/msword",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/HYD/h03dbhd/comp/HYD03_Tree_Meas.txt",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/HYD/h03dbhd/comp/HYD03_Tree_Meas.txt",
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
+            "identifier": "C2807625200-ORNL_CLOUD",
+            "issued": "2023-11-22",
+            "keyword": [
+                "biosphere",
+                "earth science",
+                "ecosystems",
+                "vegetation"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/264",
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
             "spatial": "-106.2 53.63 -105.12 53.99",
+            "temporal": "1996-03-08T00:00:00Z/1996-03-08T23:59:59Z",
             "theme": [
                 "BOREAS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "BOREAS HYD-03 SSA/OLD Aspen DBH Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/OMGEV-AXBT1",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "OMG. 2021-10-31. OMG Airborne eXpendable Bathy Thermograph (AXBT) Profiles. Version 1. OMG Airborne eXpendable Bathy Thermograph (AXBT) Profiles Version 1. NASA/JPL/PODAAC. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/JPL/OMG. https://doi.org/10.5067/OMGEV-AXBT1. OMG, NASA/JPL/OMG, 2021-10-31, OMG Level 2 Airborne eXpendable Bathy Thermograph (AXBT) Profiles, .",
-            "issued": "2021-10-06",
-            "temporal": "2020-09-02T17:52:10Z/2021-09-16T18:14:06Z",
-            "@type": "dcat:Dataset",
-            "modified": "2021-10-06",
-            "keyword": [
-                "salinity/density",
-                "ocean temperature",
-                "oceans",
-                "earth science",
-                "bathymetry/seafloor topography"
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
-            "identifier": "C2491772153-POCLOUD",
-            "description": "This dataset contains Level 2 in situ temperature profile measurements from the Airborne eXpendable BathyThermograph (AXBT) probes. It provides science quality temperature measurements as a function of depth in the water column. The AXBTs were jettisoned from a plane to collect temperature readings around Greenland, where a ship would have had difficulties maneuvering. After landing in the water, the AXBTs drop a weighted sensor from the surface that falls at a well-calibrated rate, measuring water temperature as it falls.  An equation is used to determine the depth of the measurements as the probe falls. The AXBTs are part of the Oceans Melting Greenland (OMG) mission. In the fall of 2020 and 2021, the AXBT probes were used to supplement the ocean-per-year survey of ocean properties on the continental shelf surrounding Greenland. The goal of the mission is to find out what contributions the ocean has on Greenland's melting glaciers.",
-            "release-place": "NASA/JPL/PODAAC",
-            "series-name": "OMG Airborne eXpendable Bathy Thermograph (AXBT) Profiles",
-            "graphic-preview-description": "Thumbnail",
             "creator": "OMG",
-            "title": "OMG Level 2 Airborne eXpendable Bathy Thermograph (AXBT) Profiles",
-            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/OMG_L2_AXBT.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "This dataset contains Level 2 in situ temperature profile measurements from the Airborne eXpendable BathyThermograph (AXBT) probes. It provides science quality temperature measurements as a function of depth in the water column. The AXBTs were jettisoned from a plane to collect temperature readings around Greenland, where a ship would have had difficulties maneuvering. After landing in the water, the AXBTs drop a weighted sensor from the surface that falls at a well-calibrated rate, measuring water temperature as it falls.  An equation is used to determine the depth of the measurements as the probe falls. The AXBTs are part of the Oceans Melting Greenland (OMG) mission. In the fall of 2020 and 2021, the AXBT probes were used to supplement the ocean-per-year survey of ocean properties on the continental shelf surrounding Greenland. The goal of the mission is to find out what contributions the ocean has on Greenland's melting glaciers.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FOMGEV-AXBT1",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FOMGEV-AXBT1",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
@@ -1313905,17 +1313880,17 @@
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/omg/open/L2/docs/omg-ocean-axbt-users-guide.pdf",
-                    "description": "User guide documentation for this dataset",
                     "@type": "dcat:Distribution",
+                    "description": "User guide documentation for this dataset",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/omg/open/L2/docs/omg-ocean-axbt-users-guide.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/OMG_L2_AXBT.jpg",
-                    "description": "Thumbnail",
                     "@type": "dcat:Distribution",
+                    "description": "Thumbnail",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/OMG_L2_AXBT.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 },
                 {
@@ -1313925,52 +1313900,91 @@
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
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2491772153-POCLOUD",
-                    "description": "HTTPS endpoint for data browse and download",
                     "@type": "dcat:Distribution",
+                    "description": "HTTPS endpoint for data browse and download",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2491772153-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2491772153-POCLOUD",
-                    "description": "Browse granule search results in Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse granule search results in Earthdata Search",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2491772153-POCLOUD",
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
+            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/OMG_L2_AXBT.jpg",
+            "identifier": "C2491772153-POCLOUD",
+            "issued": "2021-10-06",
+            "keyword": [
+                "salinity/density",
+                "ocean temperature",
+                "oceans",
+                "earth science",
+                "bathymetry/seafloor topography"
+            ],
+            "landingPage": "https://doi.org/10.5067/OMGEV-AXBT1",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2021-10-06",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/JPL/PODAAC"
+            },
+            "release-place": "NASA/JPL/PODAAC",
+            "series-name": "OMG Airborne eXpendable Bathy Thermograph (AXBT) Profiles",
             "spatial": "73.6 59.1 180.0 83.6",
+            "temporal": "2020-09-02T17:52:10Z/2021-09-16T18:14:06Z",
             "theme": [
                 "OMG",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "OMG Level 2 Airborne eXpendable Bathy Thermograph (AXBT) Profiles"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.nasa.gov/d/rn4b-gh7h",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "GeneLab Outreach",
+                "hasEmail": "mailto:genelab-outreach@lists.nasa.gov"
+            },
+            "description": "Arabidopsis were grown on horizontal or vertical clinostat for 4 8 or 12 days. Seedlings on horizontal clinostat were in simulated microgravity and seedlings on vertical clinostat are considered as a control. Comparison was made between plants grown on simulated microgravitry and vertical position. 6 dye-swap - treated vs untreated comparison",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "GeneLab Study Page",
+                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-45",
+                    "mediaType": "text/html",
+                    "title": "Action of microgravity on root development"
+                }
+            ],
+            "identifier": "nasa_genelab_GLDS-45_rn4b-gh7h",
             "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
             "keyword": [
                 "p-gse39631-21",
                 "p-gse39631-14",
@@ -1314016,69 +1314030,33 @@
                 "p-gse39631-1",
                 "nucleic acid labeling protocol"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "GeneLab Outreach",
-                "hasEmail": "mailto:genelab-outreach@lists.nasa.gov"
-            },
+            "landingPage": "https://data.nasa.gov/d/rn4b-gh7h",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "nasa_genelab_GLDS-45_rn4b-gh7h",
-            "description": "Arabidopsis were grown on horizontal or vertical clinostat for 4 8 or 12 days. Seedlings on horizontal clinostat were in simulated microgravity and seedlings on vertical clinostat are considered as a control. Comparison was made between plants grown on simulated microgravitry and vertical position. 6 dye-swap - treated vs untreated comparison",
-            "title": "Action of microgravity on root development",
-            "programCode": [
-                "026:005"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-45",
-                    "description": "GeneLab Study Page",
-                    "@type": "dcat:Distribution",
-                    "title": "Action of microgravity on root development"
-                }
-            ],
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "Action of microgravity on root development"
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
-                "lunar",
-                "sample",
-                "msc",
-                "catalog",
-                "apollo"
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
-            "identifier": "NASA-875",
             "description": "Apollo 15 Coarse Fines (4-10 mm): Sample Classification, Description, and Inventory; MSC 03228; B. Powell",
-            "title": "Apollo 15 Coarse Fines (4-10 mm): Sample Classification, Description, and Inventory",
-            "programCode": [
-                "026:008"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -1314086,214 +1314064,238 @@
                     "mediaType": "application/pdf"
                 }
             ],
-            "accrualPeriodicity": "irregular",
+            "identifier": "NASA-875",
+            "issued": "2018-06-25",
+            "keyword": [
+                "lunar",
+                "sample",
+                "msc",
+                "catalog",
+                "apollo"
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
+            "title": "Apollo 15 Coarse Fines (4-10 mm): Sample Classification, Description, and Inventory"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/AIRCRAFT/AIRMSPI/ACEPOL/RADIANCE/ELLIPSOID_V006",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2018-04-04. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/AIRCRAFT/AIRMSPI/ACEPOL/RADIANCE/ELLIPSOID_V006.",
-            "issued": "2018-03-05",
-            "temporal": "2017-10-19T00:00:00Z/2017-11-09T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2018-05-14",
-            "keyword": [
-                "ultraviolet wavelengths",
-                "visible wavelengths",
-                "spectral/engineering",
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
-            "identifier": "C1497270064-LARC_ASDC",
             "description": "AirMSPI_ACEPOL_Ellipsoid-projected_Georegistered_Radiance_Data are AirMSPI ellipsoid-projected georegistered radiance products acquired during the Aerosol Characterization from Polarimeter and Lidar (ACEPOL) flight campaign.\r\n\r\nAirMSPI Level 1B2 products contain radiometric and polarimetric images of clouds, aerosols, and the surface of the Earth. In particular, products contain map-projected data at 8 wavelengths: 355, 380, 445, 470, 555, 660, 865, and 935 nm. The data products include radiance, time, solar zenith, solar azimuth, view zenith, and view azimuth for all spectral bands. Wavelengths for which polarization information is available (470, 660, and 865 nm) also include the Stokes parameters Q and U, as well as degree of linear polarization (DOLP) and angle of linear polarization (AOLP). Q, U, and AOLP are reported relative to both the scattering and view meridian planes. Files are distributed in HDF-EOS-5 format.\r\n\r\nThis release of AirMSPI data contains all targets acquired during the Aerosol Characterization from Polarimeter and Lidar (ACEPOL) flight campaign. ACEPOL was based out of Armstrong Flight Research Center in Palmdale, CA, and focused on assessing the capabilities of proposed future instruments by the ACE pre-formulation study to answer fundamental science questions associated with aerosols, clouds, air quality and global ocean ecosystems. AirMSPI data were acquired from October 19 through November 9, 2017.",
-            "title": "AirMSPI verison 6 ellipsoid-projected georegistered radiance product acquired during the NASA ACEPOL flight campaign Oct-Nov 2017",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAIRCRAFT%2FAIRMSPI%2FACEPOL%2FRADIANCE%2FELLIPSOID_V006",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAIRCRAFT%2FAIRMSPI%2FACEPOL%2FRADIANCE%2FELLIPSOID_V006",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/AIRCRAFT/AIRMSPI/ACEPOL/RADIANCE/ELLIPSOID_V006",
-                    "description": "DOI data set landing page for AirMSPI_ACEPOL_Ellipsoid-projected_Georegistered_Radiance_Data_6",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for AirMSPI_ACEPOL_Ellipsoid-projected_Georegistered_Radiance_Data_6",
+                    "downloadURL": "https://doi.org/10.5067/AIRCRAFT/AIRMSPI/ACEPOL/RADIANCE/ELLIPSOID_V006",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
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
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1497270064-LARC_ASDC",
-                    "description": "Earthdata Search for AirMSPI_ACEPOL_Ellipsoid-projected_Georegistered_Radiance_Data_6 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for AirMSPI_ACEPOL_Ellipsoid-projected_Georegistered_Radiance_Data_6 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1497270064-LARC_ASDC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
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
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/airmspi/quality_summaries/AirMSPI-Data_Quality-V006_ACEPOL.pdf",
-                    "description": "AirMSPI Data Quality Statement: ACEPOL Campaign",
                     "@type": "dcat:Distribution",
+                    "description": "AirMSPI Data Quality Statement: ACEPOL Campaign",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/airmspi/quality_summaries/AirMSPI-Data_Quality-V006_ACEPOL.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's data quality document"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/airmspi/guide/AirMSPI_L1B2_DPS.RevC.20180223.pdf",
-                    "description": "Data Product Specification for the AirMSPI Level 1B2 Products (V006)",
                     "@type": "dcat:Distribution",
+                    "description": "Data Product Specification for the AirMSPI Level 1B2 Products (V006)",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/airmspi/guide/AirMSPI_L1B2_DPS.RevC.20180223.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's product usage"
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
-                    "downloadURL": "https://l0dup05.larc.nasa.gov/misr_loc/misr_loc.html",
-                    "description": "Tool to identify MISR Paths/Blocks intersecting a specified lat/lon box",
                     "@type": "dcat:Distribution",
+                    "description": "Tool to identify MISR Paths/Blocks intersecting a specified lat/lon box",
+                    "downloadURL": "https://l0dup05.larc.nasa.gov/misr_loc/misr_loc.html",
+                    "mediaType": "text/html",
                     "title": "Use this dataset in a web based tool"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/airmspi/guide/USER-AirMSPI_2013_April2013.pdf",
-                    "description": "User Guide for the AirMSPI Level 1B2 Products",
                     "@type": "dcat:Distribution",
+                    "description": "User Guide for the AirMSPI Level 1B2 Products",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/airmspi/guide/USER-AirMSPI_2013_April2013.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/AirMSPI/ACEPOL/ER2_GRP_ELLIPSOID/V006/",
-                    "description": "ASDC Direct Data Download for AirMSPI_ACEPOL_Ellipsoid-projected_Georegistered_Radiance_Data_6",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for AirMSPI_ACEPOL_Ellipsoid-projected_Georegistered_Radiance_Data_6",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/AirMSPI/ACEPOL/ER2_GRP_ELLIPSOID/V006/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/AirMSPI/ACEPOL/ER2_GRP_ELLIPSOID/V006/contents.html",
-                    "description": "OPeNDAP data access for AirMSPI_ACEPOL_Ellipsoid-projected_Georegistered_Radiance_Data_6",
                     "@type": "dcat:Distribution",
+                    "description": "OPeNDAP data access for AirMSPI_ACEPOL_Ellipsoid-projected_Georegistered_Radiance_Data_6",
+                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/AirMSPI/ACEPOL/ER2_GRP_ELLIPSOID/V006/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 }
             ],
+            "identifier": "C1497270064-LARC_ASDC",
+            "issued": "2018-03-05",
+            "keyword": [
+                "ultraviolet wavelengths",
+                "visible wavelengths",
+                "spectral/engineering",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/AIRCRAFT/AIRMSPI/ACEPOL/RADIANCE/ELLIPSOID_V006",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2018-05-14",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/LARC/SD/ASDC"
+            },
             "spatial": "<?xml version=\"1.0\" encoding=\"UTF-8\"?><gml:Polygon xmlns:gml=\"http://www.opengis.net/gml/3.2\" srsName=\"EPSG:9825\"><gml:outerBoundaryIs><gml:LinearRing><gml:posList>-90.0 -180.0 -90.0 180.0 90.0 180.0 90.0 -180.0 -90.0 -180.0</gml:posList></gml:LinearRing></gml:outerBoundaryIs><gml:innerBoundaryIs></gml:innerBoundaryIs></gml:Polygon>",
+            "temporal": "2017-10-19T00:00:00Z/2017-11-09T23:59:59.999Z",
             "theme": [
                 "AIRMSPI",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "AirMSPI verison 6 ellipsoid-projected georegistered radiance product acquired during the NASA ACEPOL flight campaign Oct-Nov 2017"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-COMPIL-3-TNO-CEN-COLOR-V5.0",
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
+            "description": "This data set is intended to include published broadband colors of centaurs and Transneptunian Objects (TNOs) published through December 2007. It supersedes all versions of the TNO colors data set EAR-A-3-RDR-TNO-PHOT.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-compil-3-tno-cen-color-v5.0_rnfd-gbdg",
+            "issued": "2018-06-26",
+            "keyword": [
+                "support archives",
+                "asteroid"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-COMPIL-3-TNO-CEN-COLOR-V5.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-compil-3-tno-cen-color-v5.0_rnfd-gbdg",
-            "description": "This data set is intended to include published broadband colors of centaurs and Transneptunian Objects (TNOs) published through December 2007. It supersedes all versions of the TNO colors data set EAR-A-3-RDR-TNO-PHOT.",
-            "title": "TNO AND CENTAUR COLORS V5.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "TNO AND CENTAUR COLORS V5.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=DI%2FEAR-C-SQIID-3-9PNIRIMAGES-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This dataset contains raw and reduced near-infrared images of comet 9P/Tempel 1, the target of the Deep Impact mission. Images were obtained from UT July 2-9, 2005 by M. Knight, R. Swaters, and N. Samarasinha using the Simultaneous Quad Infrared Imaging Device at the KPNO 2.1-m telescope. Results are published in the paper 'Ground-based visible and near-IR observations of Comet 9P/Tempel 1 during the Deep Impact encounter' by Knight et al. 2007 [KNIGHTETAL2007].",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.di-ear-c-sqiid-3-9pnirimages-v1.0_rngq-hjz4",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "calibration",
                 "support archives",
@@ -1314301,58 +1314303,38 @@
                 "sky",
                 "deep impact"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=DI%2FEAR-C-SQIID-3-9PNIRIMAGES-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.di-ear-c-sqiid-3-9pnirimages-v1.0_rngq-hjz4",
-            "description": "This dataset contains raw and reduced near-infrared images of comet 9P/Tempel 1, the target of the Deep Impact mission. Images were obtained from UT July 2-9, 2005 by M. Knight, R. Swaters, and N. Samarasinha using the Simultaneous Quad Infrared Imaging Device at the KPNO 2.1-m telescope. Results are published in the paper 'Ground-based visible and near-IR observations of Comet 9P/Tempel 1 during the Deep Impact encounter' by Knight et al. 2007 [KNIGHTETAL2007].",
-            "title": "NEAR-INFRARED IMAGES OF COMET 9P/TEMPEL 1 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "NEAR-INFRARED IMAGES OF COMET 9P/TEMPEL 1 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.nasa.gov/d/rnh6-tkkd",
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
-                "nen",
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
-            "identifier": "NASA-0000038__11",
+            "describedBy": "http://planetarynames.wr.usgs.gov/Page/Website",
             "description": "Planetary nomenclature, like terrestrial nomenclature, is used to uniquely identify a feature on the surface of a planet or satellite so that the feature can be easily located, described, and discussed. This gazetteer contains detailed information about all names of topographic and albedo features on planets and satellites (and some planetary ring and ring-gap systems) that the International Astronomical Union (IAU) has named and approved from its founding in 1919 through the present time.",
-            "title": "Gazetteer of Planetary Nomenclature",
-            "programCode": [
-                "026:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -1314360,191 +1314342,177 @@
                     "mediaType": "application/zip"
                 }
             ],
-            "describedBy": "http://planetarynames.wr.usgs.gov/Page/Website",
-            "accrualPeriodicity": "irregular"
+            "identifier": "NASA-0000038__11",
+            "issued": "2018-06-25",
+            "keyword": [
+                "wise",
+                "space science",
+                "nen",
+                "geography"
+            ],
+            "landingPage": "https://data.nasa.gov/d/rnh6-tkkd",
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
-            "landingPage": "https://doi.org/10.5067/J9R0LXGH48JR",
             "citation": "Global Modeling and Assimilation Office (GMAO). 2015-06-30. M2TMNPCLD. Version 5.12.4. MERRA-2 tavgM_3d_cld_Np: 3d,Monthly mean,Time-Averaged,Pressure-Level,Assimilation,Cloud Diagnostics V5.12.4. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/J9R0LXGH48JR. https://disc.gsfc.nasa.gov/datacollection/M2TMNPCLD_5.12.4.html. Digital Science Data.",
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
-                "atmospheric water vapor",
-                "clouds",
-                "atmosphere"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "DANA OSTRENGA",
                 "hasEmail": "mailto:dana.ostrenga@nasa.gov"
             },
+            "creator": "Global Modeling and Assimilation Office (GMAO)",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C1276812942-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "M2TMNPCLD (or tavgM_3d_cld_Np) is a 3-dimensional monthly mean data collection in Modern-Era Retrospective analysis for Research and Applications version 2 (MERRA-2).  This collection consists of assimilations of cloud diagnostics on 42 the pressure levels, such as  updraft areal fraction, cloud fraction for radiation, in-cloud cloud liquid (or ice) for radiation, and  mass fraction of cloud liquid (or ice) water. The information on the pressure levels can be found in the section 4.2 of the MERRA-2 File Specification document.  The collection also includes variance of certain parameters.\n\nMERRA-2 is the latest version of global atmospheric reanalysis for the satellite era produced by NASA Global Modeling and Assimilation Office (GMAO) using the Goddard Earth Observing System Model (GEOS) version 5.12.4.  The dataset covers the period of 1980-present with the latency of ~3 weeks after the end of a month. \n\nData Reprocessing:  Please check \u201cRecords of MERRA-2 Data Reprocessing and Service Changes\u201d linked from the \u201cDocumentation\u201d tab on this page.  Note that a reprocessed data filename is different from the original file.\n\nMERRA-2 Mailing List: Sign up to receive information on reprocessing of data, changing of tools and services, as well as data announcements from GMAO. Contact the GES DISC Help Desk (gsfc-dl-help-disc@mail.nasa.gov) to be added to the list.\n\nQuestions: If you have a question, please read \"MERRA-2 File Specification Document\",  \u201cMERRA-2 Data Access \u2013 Quick Start Guide\u201d, and FAQs linked from the \u201dDocumentation\u201d tab on this page.  If that does not answer your question, you may email the question on data access to the GES DISC Help Desk (gsfc-dl-help-disc@mail.nasa.gov), or the question on science to the MERRA-2 science team (merra-questions@lists.nasa.gov).",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "M2TMNPCLD",
-            "creator": "Global Modeling and Assimilation Office (GMAO)",
-            "graphic-preview-description": "The GES-DISC Interactive Online Visualization ANd aNalysis Interface (Giovanni) is a web-based tool that allows users to interactively visualize and analyze data.",
-            "title": "MERRA-2 tavgM_3d_cld_Np: 3d,Monthly mean,Time-Averaged,Pressure-Level,Assimilation,Cloud Diagnostics 0.625 x 0.5 degree V5.12.4 (M2TMNPCLD) at GES DISC",
-            "graphic-preview-file": "https://giovanni.gsfc.nasa.gov/giovanni/#dataKeyword=M2TMNPCLD",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FJ9R0LXGH48JR",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FJ9R0LXGH48JR",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/M2TMNPCLD_5.12.4.png",
-                    "description": "M2TMNPCLD variable",
                     "@type": "dcat:Distribution",
+                    "description": "M2TMNPCLD variable",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/M2TMNPCLD_5.12.4.png",
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
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/M2TMNPCLD_5.12.4.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/M2TMNPCLD_5.12.4.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://goldsmr5.gesdisc.eosdis.nasa.gov/data/MERRA2_MONTHLY/M2TMNPCLD.5.12.4/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://goldsmr5.gesdisc.eosdis.nasa.gov/data/MERRA2_MONTHLY/M2TMNPCLD.5.12.4/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://giovanni.gsfc.nasa.gov/giovanni/#dataKeyword=M2TMNPCLD",
-                    "description": "The GES-DISC Interactive Online Visualization ANd aNalysis Interface (Giovanni) is a web-based tool that allows users to interactively visualize and analyze data.",
                     "@type": "dcat:Distribution",
+                    "description": "The GES-DISC Interactive Online Visualization ANd aNalysis Interface (Giovanni) is a web-based tool that allows users to interactively visualize and analyze data.",
+                    "downloadURL": "https://giovanni.gsfc.nasa.gov/giovanni/#dataKeyword=M2TMNPCLD",
+                    "mediaType": "text/html",
                     "title": "Get a related visualization through GIOVANNI"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=M2TMNPCLD",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=M2TMNPCLD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://goldsmr5.gesdisc.eosdis.nasa.gov/dods/M2TMNPCLD.info",
-                    "description": "The GrADS Data Server (GDS) is another form of OPeNDAP that provides subsetting and some analysis services across the Internet.",
                     "@type": "dcat:Distribution",
+                    "description": "The GrADS Data Server (GDS) is another form of OPeNDAP that provides subsetting and some analysis services across the Internet.",
+                    "downloadURL": "https://goldsmr5.gesdisc.eosdis.nasa.gov/dods/M2TMNPCLD.info",
+                    "mediaType": "text/html",
                     "title": "Use GRADS DATA SERVER (GDS) to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://goldsmr5.gesdisc.eosdis.nasa.gov/opendap/MERRA2_MONTHLY/M2TMNPCLD.5.12.4/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://goldsmr5.gesdisc.eosdis.nasa.gov/opendap/MERRA2_MONTHLY/M2TMNPCLD.5.12.4/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://goldsmr5.gesdisc.eosdis.nasa.gov/thredds/catalog/MERRA2_MONTHLY_aggregation//M2TMNPCLD.5.12.4/catalog.html",
-                    "description": "Time aggregated THREDDS Data Server (TDS) ",
                     "@type": "dcat:Distribution",
+                    "description": "Time aggregated THREDDS Data Server (TDS) ",
+                    "downloadURL": "https://goldsmr5.gesdisc.eosdis.nasa.gov/thredds/catalog/MERRA2_MONTHLY_aggregation//M2TMNPCLD.5.12.4/catalog.html",
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
-                    "downloadURL": "https://goldsmr5.gesdisc.eosdis.nasa.gov/data/MERRA2_MONTHLY/M2TMNPCLD.5.12.4/doc/MERRA2.README.pdf",
-                    "description": "README Document",
                     "@type": "dcat:Distribution",
+                    "description": "README Document",
+                    "downloadURL": "https://goldsmr5.gesdisc.eosdis.nasa.gov/data/MERRA2_MONTHLY/M2TMNPCLD.5.12.4/doc/MERRA2.README.pdf",
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
-            "spatial": "-180.0 -90.0 180.0 90.0",
-            "theme": [
-                "MERRA-2",
-                "geospatial"
+            "graphic-preview-description": "The GES-DISC Interactive Online Visualization ANd aNalysis Interface (Giovanni) is a web-based tool that allows users to interactively visualize and analyze data.",
+            "graphic-preview-file": "https://giovanni.gsfc.nasa.gov/giovanni/#dataKeyword=M2TMNPCLD",
+            "identifier": "C1276812942-GES_DISC",
+            "issued": "2007-06-14",
+            "keyword": [
+                "earth science",
+                "atmospheric water vapor",
+                "clouds",
+                "atmosphere"
             ],
+            "landingPage": "https://doi.org/10.5067/J9R0LXGH48JR",
             "language": [
                 "en-US"
-            ]
-        },
-        {
-            "accessLevel": "public",
-            "bureauCode": [
-                "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/RCMZA6TL70BG",
-            "citation": "Global Modeling and Assimilation Office (GMAO). 2015-06-30. M2I1NXLFO. Version 5.12.4. MERRA-2 inst1_2d_lfo_Nx: 2d,1-Hourly,Instantaneous,Single-Level,Assimilation,Land Surface Forcings V5.12.4. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/RCMZA6TL70BG. https://disc.gsfc.nasa.gov/datacollection/M2I1NXLFO_5.12.4.html. Digital Science Data.",
-            "issued": "2007-06-14",
-            "temporal": "1980-01-01T00:00:00Z/2022-01-17T00:00:00Z",
-            "@type": "dcat:Dataset",
             "modified": "2015-07-07",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
+            },
             "references": [
                 "https://doi.org/10.1175/JCLI-D-16-0758.1",
                 "https://doi.org/10.5194/gmd-8-1339-2015",
@@ -1314555,568 +1314523,614 @@
                 "https://doi.org/NASA/TM%E2%80%932015-104606/Vol.%2043",
                 "https://doi.org/10.1177/1094342005056120"
             ],
-            "keyword": [
-                "earth science",
-                "atmosphere",
-                "atmospheric water vapor",
-                "altitude",
-                "atmospheric pressure",
-                "atmospheric temperature",
-                "atmospheric winds"
+            "release-place": "Greenbelt, MD, USA",
+            "series-name": "M2TMNPCLD",
+            "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "1980-01-01T00:00:00Z/2022-01-17T00:00:00Z",
+            "theme": [
+                "MERRA-2",
+                "geospatial"
+            ],
+            "title": "MERRA-2 tavgM_3d_cld_Np: 3d,Monthly mean,Time-Averaged,Pressure-Level,Assimilation,Cloud Diagnostics 0.625 x 0.5 degree V5.12.4 (M2TMNPCLD) at GES DISC"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "026:00"
             ],
+            "citation": "Global Modeling and Assimilation Office (GMAO). 2015-06-30. M2I1NXLFO. Version 5.12.4. MERRA-2 inst1_2d_lfo_Nx: 2d,1-Hourly,Instantaneous,Single-Level,Assimilation,Land Surface Forcings V5.12.4. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/RCMZA6TL70BG. https://disc.gsfc.nasa.gov/datacollection/M2I1NXLFO_5.12.4.html. Digital Science Data.",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "DANA OSTRENGA",
                 "hasEmail": "mailto:dana.ostrenga@nasa.gov"
             },
+            "creator": "Global Modeling and Assimilation Office (GMAO)",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C1276812822-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "M2I1NXLFO (or  inst1_2d_lfo_Nx) is an instantaneous 2-dimensional hourly data collection in Modern-Era Retrospective analysis for Research and Applications version 2 (MERRA-2).  This collection consists of land surface forcing parameters, such as height, specific humidity, wind, and air temperature of the model surface layer.  The timestamp of a data field is on each hour starting from 00:00 UTC, e.g.:  00:00, 01:00, \u2026 , 23:00 UTC. \n\nMERRA-2 is the latest version of global atmospheric reanalysis for the satellite era produced by NASA Global Modeling and Assimilation Office (GMAO) using the Goddard Earth Observing System Model (GEOS) version 5.12.4.  The dataset covers the period of 1980-present with the latency of ~3 weeks after the end of a month. \n\nData Reprocessing:  Please check \u201cRecords of MERRA-2 Data Reprocessing and Service Changes\u201d linked from the \u201cDocumentation\u201d tab on this page.  Note that a reprocessed data filename is different from the original file.\n\nMERRA-2 Mailing List: Sign up to receive information on reprocessing of data, changing of tools and services, as well as data announcements from GMAO. Contact the GES DISC Help Desk (gsfc-dl-help-disc@mail.nasa.gov) to be added to the list.\n\nQuestions: If you have a question, please read \"MERRA-2 File Specification Document\",  \u201cMERRA-2 Data Access \u2013 Quick Start Guide\u201d, and FAQs linked from the \u201dDocumentation\u201d tab on this page.  If that does not answer your question, you may email the question on data access to the GES DISC Help Desk (gsfc-dl-help-disc@mail.nasa.gov), or the question on science to the MERRA-2 science team (merra-questions@lists.nasa.gov).",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "M2I1NXLFO",
-            "creator": "Global Modeling and Assimilation Office (GMAO)",
-            "graphic-preview-description": "The GES-DISC Interactive Online Visualization ANd aNalysis Interface (Giovanni) is a web-based tool that allows users to interactively visualize and analyze data.",
-            "title": "MERRA-2 inst1_2d_lfo_Nx: 2d,1-Hourly,Instantaneous,Single-Level,Assimilation,Land Surface Forcings 0.625 x 0.5 degree V5.12.4 (M2I1NXLFO) at GES DISC",
-            "graphic-preview-file": "https://giovanni.gsfc.nasa.gov/giovanni/#dataKeyword=M2I1NXLFO",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FRCMZA6TL70BG",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FRCMZA6TL70BG",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/M2I1NXLFO_5.12.4.png",
-                    "description": "M2I1NXLFO variable",
                     "@type": "dcat:Distribution",
+                    "description": "M2I1NXLFO variable",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/M2I1NXLFO_5.12.4.png",
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
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/M2I1NXLFO_5.12.4.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/M2I1NXLFO_5.12.4.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://goldsmr4.gesdisc.eosdis.nasa.gov/data/MERRA2/M2I1NXLFO.5.12.4/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://goldsmr4.gesdisc.eosdis.nasa.gov/data/MERRA2/M2I1NXLFO.5.12.4/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://giovanni.gsfc.nasa.gov/giovanni/#dataKeyword=M2I1NXLFO",
-                    "description": "The GES-DISC Interactive Online Visualization ANd aNalysis Interface (Giovanni) is a web-based tool that allows users to interactively visualize and analyze data.",
                     "@type": "dcat:Distribution",
+                    "description": "The GES-DISC Interactive Online Visualization ANd aNalysis Interface (Giovanni) is a web-based tool that allows users to interactively visualize and analyze data.",
+                    "downloadURL": "https://giovanni.gsfc.nasa.gov/giovanni/#dataKeyword=M2I1NXLFO",
+                    "mediaType": "text/html",
                     "title": "Get a related visualization through GIOVANNI"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=M2I1NXLFO",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=M2I1NXLFO",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://goldsmr4.gesdisc.eosdis.nasa.gov/dods/M2I1NXLFO.info",
-                    "description": "The GrADS Data Server (GDS) is another form of OPeNDAP that provides subsetting and some analysis services across the Internet.",
                     "@type": "dcat:Distribution",
+                    "description": "The GrADS Data Server (GDS) is another form of OPeNDAP that provides subsetting and some analysis services across the Internet.",
+                    "downloadURL": "https://goldsmr4.gesdisc.eosdis.nasa.gov/dods/M2I1NXLFO.info",
+                    "mediaType": "text/html",
                     "title": "Use GRADS DATA SERVER (GDS) to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://goldsmr4.gesdisc.eosdis.nasa.gov/opendap/MERRA2/M2I1NXLFO.5.12.4/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://goldsmr4.gesdisc.eosdis.nasa.gov/opendap/MERRA2/M2I1NXLFO.5.12.4/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://goldsmr4.gesdisc.eosdis.nasa.gov/thredds/catalog/MERRA2_aggregation/M2I1NXLFO.5.12.4/catalog.html",
-                    "description": "Time aggregated THREDDS Data Server (TDS) ",
                     "@type": "dcat:Distribution",
+                    "description": "Time aggregated THREDDS Data Server (TDS) ",
+                    "downloadURL": "https://goldsmr4.gesdisc.eosdis.nasa.gov/thredds/catalog/MERRA2_aggregation/M2I1NXLFO.5.12.4/catalog.html",
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
-                    "downloadURL": "https://goldsmr4.gesdisc.eosdis.nasa.gov/data/MERRA2/M2I1NXLFO.5.12.4/doc/MERRA2.README.pdf",
-                    "description": "README Document",
                     "@type": "dcat:Distribution",
+                    "description": "README Document",
+                    "downloadURL": "https://goldsmr4.gesdisc.eosdis.nasa.gov/data/MERRA2/M2I1NXLFO.5.12.4/doc/MERRA2.README.pdf",
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
+            "graphic-preview-file": "https://giovanni.gsfc.nasa.gov/giovanni/#dataKeyword=M2I1NXLFO",
+            "identifier": "C1276812822-GES_DISC",
+            "issued": "2007-06-14",
+            "keyword": [
+                "earth science",
+                "atmosphere",
+                "atmospheric water vapor",
+                "altitude",
+                "atmospheric pressure",
+                "atmospheric temperature",
+                "atmospheric winds"
+            ],
+            "landingPage": "https://doi.org/10.5067/RCMZA6TL70BG",
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
+            "series-name": "M2I1NXLFO",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "1980-01-01T00:00:00Z/2022-01-17T00:00:00Z",
             "theme": [
                 "MERRA-2",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "MERRA-2 inst1_2d_lfo_Nx: 2d,1-Hourly,Instantaneous,Single-Level,Assimilation,Land Surface Forcings 0.625 x 0.5 degree V5.12.4 (M2I1NXLFO) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-4-ESC2-67P-M14-INFLDSTR-V1.0",
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
+            "description": "This CODMAC level 4 data set contains solar stray-light corrected, in-field stray-light corrected,  radiometric calibrated and geometric distortion corrected  (resampled) image data in W/m^2/sr/nm,  acquired by the OSIRIS Wide Angle Camera on the Rosetta spacecraft  during the COMET ESCORT 2 mission phase, covering the period  from 2015-03-10T23:25:00.000 to 2015-04-08T11:24:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V1.0 is the first version of this dataset: Lien corrected dataset after September 2019 PSA/PDS external peer review.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-4-esc2-67p-m14-infldstr-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-4-ESC2-67P-M14-INFLDSTR-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-4-esc2-67p-m14-infldstr-v1.0",
-            "description": "This CODMAC level 4 data set contains solar stray-light corrected, in-field stray-light corrected,  radiometric calibrated and geometric distortion corrected  (resampled) image data in W/m^2/sr/nm,  acquired by the OSIRIS Wide Angle Camera on the Rosetta spacecraft  during the COMET ESCORT 2 mission phase, covering the period  from 2015-03-10T23:25:00.000 to 2015-04-08T11:24:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V1.0 is the first version of this dataset: Lien corrected dataset after September 2019 PSA/PDS external peer review.",
-            "title": "ROSETTA-ORBITER 67P OSIWAC 4 ESC2-MTP014 RDR-INFLDSTR V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P OSIWAC 4 ESC2-MTP014 RDR-INFLDSTR V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-C-COMPIL-5-COMET-NUC-PROPERTIES-V1.0",
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
-                "comet"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This data set presents tables 1, 2, 3, 4, 5 and 7 of 'Sizes, Shapes, Albedos, and Colors of Cometary Nuclei' (Lamy et al., 2004), and includes references for the sources cited. The authors culled this data from published or well-known unpublished sources, and have indicated what they judge to be the most reliable value available.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-c-compil-5-comet-nuc-properties-v1.0_rnkb-3x38",
+            "issued": "2021-05-21",
+            "keyword": [
+                "support archives",
+                "comet"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-C-COMPIL-5-COMET-NUC-PROPERTIES-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-c-compil-5-comet-nuc-properties-v1.0_rnkb-3x38",
-            "description": "This data set presents tables 1, 2, 3, 4, 5 and 7 of 'Sizes, Shapes, Albedos, and Colors of Cometary Nuclei' (Lamy et al., 2004), and includes references for the sources cited. The authors culled this data from published or well-known unpublished sources, and have indicated what they judge to be the most reliable value available.",
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
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=CH1-ORB-L-MRFFR-1-PDR-V1.0",
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
-                "chandrayaan-1",
-                "moon"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This data set contains archival raw data acquired from the Mini-RF (Forerunner) instrument during the Chandrayaan-1 mission.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ch1-orb-l-mrffr-1-pdr-v1.0_rnpc-wtun",
+            "issued": "2021-05-21",
+            "keyword": [
+                "chandrayaan-1",
+                "moon"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=CH1-ORB-L-MRFFR-1-PDR-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ch1-orb-l-mrffr-1-pdr-v1.0_rnpc-wtun",
-            "description": "This data set contains archival raw data acquired from the Mini-RF (Forerunner) instrument during the Chandrayaan-1 mission.",
-            "title": "CH1-ORB MOON MINI-RF 1 PACKETIZED DATA RECORD V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "CH1-ORB MOON MINI-RF 1 PACKETIZED DATA RECORD V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1955",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Baltzer, J.L., N.J. Day, X.J. Walker, D.F. Greene, M.C. Mack, D. Arseneault, J. Barnes, Y. Bergeron, Y. Boucher, L.L. Bourgeau-Chavez, C.D. Brown, S. Carri\u00e8re, B.K. Howard, S. Gauthier, M.A. Parisien, K.A. Reid, B.M. Rogers, C. Roland, L. Sirois, S. Stehn, D.K. Thompson, M.R. Turetsky, E. Whitman, and J.F. Johnstone. 2022. ABoVE: Synthesis of Post-Fire Regeneration Across Boreal North America. ORNL DAAC, Oak Ridge, Tennessee, USA. https://doi.org/10.3334/ORNLDAAC/1955",
-            "issued": "2022-11-09",
-            "temporal": "1989-01-01T00:00:00Z/2018-12-31T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-06-12",
-            "keyword": [
-                "human dimensions",
-                "ecosystems",
-                "biosphere",
-                "earth science",
-                "natural hazards",
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
-            "identifier": "C2539840222-ORNL_CLOUD",
             "description": "This dataset is a synthesis of species-specific pre- and post-fire tree stem density estimates, field plot characterization data, and acquired climate moisture deficit data for sites from Alaska, USA eastward to Quebec, Canada in fires that burned between 1989 and 2014. Data are from 1,538 sites across 58 fire perimeters encompassing 4.52 Mha of forest and all major boreal ecozones in North America. To be included in this synthesis, a site had to contain information on species-specific post-fire seedling densities. This included sites where seedlings had been counted 2-13 years post-fire, a timeframe over which there was little change in relative dominance of species based on densities. Plot characterization data includes stand age, site drainage, disturbance history, crown combustion severity, seedbed conditions, and stand structural attributes. Gridded values of Hargreaves Climate Moisture Deficit (CMD) were obtained for each plot where plot coordinates were available. These values included 30-year normals (1981-2010) and CMD in the two years immediately following the fire year. CMD anomalies were calculated as the difference between the 30-year normal and the single year values for each of the first two years after a fire. These synthesis data are provided in comma-separated values (CSV) format.",
-            "graphic-preview-description": "Number of fires and sites across combined ecozones as follows from west to east: Alaskan Boreal Interior, Cordillera (Boreal Cordillera and Taiga Cordillera), Plains West (Taiga Plains and Boreal Plains), Shield West (western portions of Taiga Shield and Softwood Shield), Plans East (Hudson Plains), Shield East (eastern portions of Taiga Shield and Softwood Shield). Alternate trajectories indicate the most common state changes away from black spruce dominance as quantified in the associated synthesis manuscript (Baltzer et al., 2021).",
-            "title": "ABoVE: Synthesis of Post-Fire Regeneration Across Boreal North America",
-            "graphic-preview-file": "https://daac.ornl.gov/ABOVE/guides/PostFire_Tree_Regeneration_Fig1.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1955",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1955",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/above/PostFire_Tree_Regeneration/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/above/PostFire_Tree_Regeneration/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/ABOVE/guides/PostFire_Tree_Regeneration.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/ABOVE/guides/PostFire_Tree_Regeneration.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1955",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1955",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/PostFire_Tree_Regeneration/comp/PostFire_Tree_Regeneration.pdf",
-                    "description": "ABoVE: Synthesis of Post-Fire Regeneration Across Boreal North America: PostFire_Tree_Regeneration.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "ABoVE: Synthesis of Post-Fire Regeneration Across Boreal North America: PostFire_Tree_Regeneration.pdf",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/PostFire_Tree_Regeneration/comp/PostFire_Tree_Regeneration.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://daac.ornl.gov/ABOVE/guides/PostFire_Tree_Regeneration_Fig1.png",
-                    "description": "Number of fires and sites across combined ecozones as follows from west to east: Alaskan Boreal Interior, Cordillera (Boreal Cordillera and Taiga Cordillera), Plains West (Taiga Plains and Boreal Plains), Shield West (western portions of Taiga Shield and Softwood Shield), Plans East (Hudson Plains), Shield East (eastern portions of Taiga Shield and Softwood Shield). Alternate trajectories indicate the most common state changes away from black spruce dominance as quantified in the associated synthesis manuscript (Baltzer et al., 2021).",
                     "@type": "dcat:Distribution",
+                    "description": "Number of fires and sites across combined ecozones as follows from west to east: Alaskan Boreal Interior, Cordillera (Boreal Cordillera and Taiga Cordillera), Plains West (Taiga Plains and Boreal Plains), Shield West (western portions of Taiga Shield and Softwood Shield), Plans East (Hudson Plains), Shield East (eastern portions of Taiga Shield and Softwood Shield). Alternate trajectories indicate the most common state changes away from black spruce dominance as quantified in the associated synthesis manuscript (Baltzer et al., 2021).",
+                    "downloadURL": "https://daac.ornl.gov/ABOVE/guides/PostFire_Tree_Regeneration_Fig1.png",
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
+            "graphic-preview-description": "Number of fires and sites across combined ecozones as follows from west to east: Alaskan Boreal Interior, Cordillera (Boreal Cordillera and Taiga Cordillera), Plains West (Taiga Plains and Boreal Plains), Shield West (western portions of Taiga Shield and Softwood Shield), Plans East (Hudson Plains), Shield East (eastern portions of Taiga Shield and Softwood Shield). Alternate trajectories indicate the most common state changes away from black spruce dominance as quantified in the associated synthesis manuscript (Baltzer et al., 2021).",
+            "graphic-preview-file": "https://daac.ornl.gov/ABOVE/guides/PostFire_Tree_Regeneration_Fig1.png",
+            "identifier": "C2539840222-ORNL_CLOUD",
+            "issued": "2022-11-09",
+            "keyword": [
+                "human dimensions",
+                "ecosystems",
+                "biosphere",
+                "earth science",
+                "natural hazards",
+                "vegetation"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1955",
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
             "spatial": "-152.2 49.12 -71.01 66.96",
+            "temporal": "1989-01-01T00:00:00Z/2018-12-31T23:59:59Z",
             "theme": [
                 "ABoVE",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "ABoVE: Synthesis of Post-Fire Regeneration Across Boreal North America"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MER1-M-PANCAM-3-ILUT-OPS-V1.0",
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
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mer1-m-pancam-3-ilut-ops-v1.0_rnrq-kz3t",
+            "issued": "2018-06-26",
+            "keyword": [
+                "mars exploration rover",
+                "mars"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MER1-M-PANCAM-3-ILUT-OPS-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mer1-m-pancam-3-ilut-ops-v1.0_rnrq-kz3t",
-            "description": "not applicable",
-            "title": "MER 1 MARS PANORAMIC CAMERA INVERSE LUT RDR OPS V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "MER 1 MARS PANORAMIC CAMERA INVERSE LUT RDR OPS V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-X-SREM-2-ESC3-MTP020-V1.0",
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
+            "description": "This data set contains count rates (1/s) as measured by the Standard Radiation Environment Monitor (SREM) instrument on the Rosetta spacecraft, along with their standard deviations.  The primary target is comet 67P/Churyumov-Gerasimenko. These are CODMAC Level 2 Experiment Data Record data, and provide a measure of the radiation in the spacecraft environment during the Medium Term Plan 20 period of the ESCORT 3 mission phase.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-x-srem-2-esc3-mtp020-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-X-SREM-2-ESC3-MTP020-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-x-srem-2-esc3-mtp020-v1.0",
-            "description": "This data set contains count rates (1/s) as measured by the Standard Radiation Environment Monitor (SREM) instrument on the Rosetta spacecraft, along with their standard deviations.  The primary target is comet 67P/Churyumov-Gerasimenko. These are CODMAC Level 2 Experiment Data Record data, and provide a measure of the radiation in the spacecraft environment during the Medium Term Plan 20 period of the ESCORT 3 mission phase.",
-            "title": "ROSETTA-ORBITER 67P SREM 2 ESCORT 3\n    MTP020 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P SREM 2 ESCORT 3\n    MTP020 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-3-RDR-TRIAD-POLARIMETRY-V1.0",
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
+            "description": "This data set contains the data originally archived in TRIAD and reported in Asteroids (T. Gehrels, Ed., The University of Arizona Press, 1979). It tabulates the reduced values of the polarization curves of the asteroids, namely minimum polarization, inversion angle, and polarimetric slope.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-3-rdr-triad-polarimetry-v1.0_rnxh-hwcb",
+            "issued": "2021-05-21",
+            "keyword": [
+                "asteroid",
+                "support archives"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-3-RDR-TRIAD-POLARIMETRY-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-3-rdr-triad-polarimetry-v1.0_rnxh-hwcb",
-            "description": "This data set contains the data originally archived in TRIAD and reported in Asteroids (T. Gehrels, Ed., The University of Arizona Press, 1979). It tabulates the reduced values of the polarization curves of the asteroids, namely minimum polarization, inversion angle, and polarimetric slope.",
-            "title": "TRIAD ASTEROID POLARIMETRY V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "TRIAD ASTEROID POLARIMETRY V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/I0T1I4WNQ462",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "High Mountain Asia GFDL FLOR Modeled Daily Precipitation for Extreme Analysis V001. Version 1. Archived by National Aeronautics and Space Administration, U.S. Government, NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/I0T1I4WNQ462.",
-            "issued": "1961-01-01",
-            "temporal": "1961-01-01T00:00:00Z/2100-12-31T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2100-12-31",
-            "keyword": [
-                "atmosphere",
-                "precipitation",
-                "earth science"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Sarah Kapnick",
                 "hasEmail": "mailto:Sarah.Kapnick@noaa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA NSIDC DAAC"
-            },
-            "identifier": "C1624006981-NSIDC_ECS",
             "description": "This data set includes three climate simulations of daily precipitation over the Himalayan region for summer and winter, covering different time periods: two 30-member ensemble simulations spanning 40-year time periods in the 20th century (1961-2000) and 21st century (2061-2100), and a present-day climate simulation from 1982 to 2017 nudged to reanalysis winds. These precipitation estimates were simulated by the National Oceanic and Atmospheric Administration (NOAA) Geophysical Fluid Dynamics Laboratory (GFDL) Forecast-oriented Low Ocean Resolution version of the CM2.5 model (GFDL FLOR).",
-            "title": "High Mountain Asia GFDL FLOR Modeled Daily Precipitation for Extreme Analysis V001",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FI0T1I4WNQ462",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FI0T1I4WNQ462",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/HMA/HMA_EAPrecip_FLOR.001/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/HMA/HMA_EAPrecip_FLOR.001/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?tag_key=gov.nasa.eosdis&p=C1624006981-NSIDC_ECS&m=8.293304443359375%2182.02008056640625%213%211%210%210%2C2&tl=1547070406%214%21%21&ac=true",
-                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?tag_key=gov.nasa.eosdis&p=C1624006981-NSIDC_ECS&m=8.293304443359375%2182.02008056640625%213%211%210%210%2C2&tl=1547070406%214%21%21&ac=true",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/data/data-access-tool/HMA_EAPrecip_FLOR/versions/1/",
-                    "description": "Data Access link for ITSD project",
                     "@type": "dcat:Distribution",
+                    "description": "Data Access link for ITSD project",
+                    "downloadURL": "https://nsidc.org/data/data-access-tool/HMA_EAPrecip_FLOR/versions/1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/I0T1I4WNQ462",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/I0T1I4WNQ462",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/I0T1I4WNQ462",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/I0T1I4WNQ462",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C1624006981-NSIDC_ECS",
+            "issued": "1961-01-01",
+            "keyword": [
+                "atmosphere",
+                "precipitation",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/I0T1I4WNQ462",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2100-12-31",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA NSIDC DAAC"
+            },
             "spatial": "72.8125 26.75 87.8125 35.25",
+            "temporal": "1961-01-01T00:00:00Z/2100-12-31T23:59:59.999Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "High Mountain Asia GFDL FLOR Modeled Daily Precipitation for Extreme Analysis V001"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.nasa.gov/d/rp24-jkbu",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "GeneLab Outreach",
+                "hasEmail": "mailto:genelab-outreach@lists.nasa.gov"
+            },
+            "description": "Prolonged skeletal unloading through bedrest results in bone loss similar to that observed in elderly osteoporotic patients but with an accelerated timeframe. This rapid effect on weight-bearing bones is also observed in astronauts who lose up to 2% of their bone mass per month spent in Space. Despite important implications for Spaceflight travellers and bedridden patients on Earth the exact mechanisms involved in disuse osteoporosis have not been elucidated. Parathyroid hormone-related protein (PTHrP) regulates many physiological processes including skeletal development and has been proposed as a gravisensor. To investigate the role of PTHrP in microgravity-induced bone loss trabecular osteoblasts (TOs) from Pthrp+/+ and -/- mice were exposed to simulated microgravity for 6 days. Viability of TOs decreased in inverse proportion to PTHrP expression levels. Microarray analysis of Pthrp+/+ TOs after 6 days at 0g revealed expression changes in genes encoding prolactins,apoptosis and survival molecules bone metabolism and extra-cellular matrix composition proteins chemokines IGF family and Wnt-related signalling molecules. Importantly 88% of 0g-induced expression changes in Pthrp+/+ cells overlap those observed in Pthrp-/- cells in normal gravity. Pulsatile treatment with PTHrP1-36 peptide during microgravity exposure reversed a large proportion of 0g-induced changes in Pthrp+/+ TOs. Our results confirm PTHrP efficacy as an anabolic agent to prevent microgravity-induced cell death in TOs. Total RNA samples extracted from Pthrp+/+and -/- trabecular osteoblasts (TOs) exposed for 6 days to simulated 0g in Synthecon rotating cell or left 6 days in culture at 1g. Cells had either been treated with a pulsatile treatment (2 h/day) of PTHrP1-36 peptide (10-8M) or received a change in growth medium. In total: 8 different conditions with 2 replicates each i.e. Pthrp+/+ TOs at 0g or 1g with or without PTHrP1-36 treatment and Pthrp-/- TOs at 0g or 1 g,with or without PTHrP1-36 treatment.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "GeneLab Study Page",
+                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-107",
+                    "mediaType": "text/html",
+                    "title": "The Role of PTHrP in Osteoblast Response to Microgravity: Implications for Osteoporosis Development."
+                }
+            ],
+            "identifier": "nasa_genelab_GLDS-107_rp24-jkbu",
             "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
             "keyword": [
                 "treatment",
                 "normalization data transformation protocol",
@@ -1315131,142 +1315145,130 @@
                 "p-gse78980-4",
                 "p-gse78980-5"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "GeneLab Outreach",
-                "hasEmail": "mailto:genelab-outreach@lists.nasa.gov"
-            },
+            "landingPage": "https://data.nasa.gov/d/rp24-jkbu",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "nasa_genelab_GLDS-107_rp24-jkbu",
-            "description": "Prolonged skeletal unloading through bedrest results in bone loss similar to that observed in elderly osteoporotic patients but with an accelerated timeframe. This rapid effect on weight-bearing bones is also observed in astronauts who lose up to 2% of their bone mass per month spent in Space. Despite important implications for Spaceflight travellers and bedridden patients on Earth the exact mechanisms involved in disuse osteoporosis have not been elucidated. Parathyroid hormone-related protein (PTHrP) regulates many physiological processes including skeletal development and has been proposed as a gravisensor. To investigate the role of PTHrP in microgravity-induced bone loss trabecular osteoblasts (TOs) from Pthrp+/+ and -/- mice were exposed to simulated microgravity for 6 days. Viability of TOs decreased in inverse proportion to PTHrP expression levels. Microarray analysis of Pthrp+/+ TOs after 6 days at 0g revealed expression changes in genes encoding prolactins,apoptosis and survival molecules bone metabolism and extra-cellular matrix composition proteins chemokines IGF family and Wnt-related signalling molecules. Importantly 88% of 0g-induced expression changes in Pthrp+/+ cells overlap those observed in Pthrp-/- cells in normal gravity. Pulsatile treatment with PTHrP1-36 peptide during microgravity exposure reversed a large proportion of 0g-induced changes in Pthrp+/+ TOs. Our results confirm PTHrP efficacy as an anabolic agent to prevent microgravity-induced cell death in TOs. Total RNA samples extracted from Pthrp+/+and -/- trabecular osteoblasts (TOs) exposed for 6 days to simulated 0g in Synthecon rotating cell or left 6 days in culture at 1g. Cells had either been treated with a pulsatile treatment (2 h/day) of PTHrP1-36 peptide (10-8M) or received a change in growth medium. In total: 8 different conditions with 2 replicates each i.e. Pthrp+/+ TOs at 0g or 1g with or without PTHrP1-36 treatment and Pthrp-/- TOs at 0g or 1 g,with or without PTHrP1-36 treatment.",
-            "title": "The Role of PTHrP in Osteoblast Response to Microgravity: Implications for Osteoporosis Development.",
-            "programCode": [
-                "026:005"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-107",
-                    "description": "GeneLab Study Page",
-                    "@type": "dcat:Distribution",
-                    "title": "The Role of PTHrP in Osteoblast Response to Microgravity: Implications for Osteoporosis Development."
-                }
-            ],
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "The Role of PTHrP in Osteoblast Response to Microgravity: Implications for Osteoporosis Development."
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO%2FRL-CAL-CONSERT-2-CR4B-V1.0",
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
+            "description": "This archive contains data from the CONSERT instrument onboard ROSETTA Orbiter and Lander, acquired during the CR4B (Cruise 4B) phase. It also contains documentation which describes the CONSERT experiment. The data archived in this data set conform to the Planetary Data System (PDS) Standards, Version 3.6.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-rl-cal-consert-2-cr4b-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "calibration",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO%2FRL-CAL-CONSERT-2-CR4B-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-rl-cal-consert-2-cr4b-v1.0",
-            "description": "This archive contains data from the CONSERT instrument onboard ROSETTA Orbiter and Lander, acquired during the CR4B (Cruise 4B) phase. It also contains documentation which describes the CONSERT experiment. The data archived in this data set conform to the Planetary Data System (PDS) Standards, Version 3.6.",
-            "title": "ROSETTA-ORBITER/ROSETTA-LANDER CAL\n                           CONSERT 2 CR4B V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER/ROSETTA-LANDER CAL\n                           CONSERT 2 CR4B V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/SeaBASS/GEO-CAPE/DATA001",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/GSFC/SED/ESD/GCDC/OB.DAAC. https://doi.org/10.5067/SeaBASS/GEO-CAPE/DATA001.",
-            "issued": "2011-07-11",
-            "temporal": "2011-07-11T00:00:02Z/2023-04-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-04-06",
-            "keyword": [
-                "ocean chemistry",
-                "ocean optics",
-                "ocean temperature",
-                "salinity/density",
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
-            "identifier": "C1633360241-OB_DAAC",
             "description": "GEO-CAPE : Geostationary Coastal and Air Pollution Events",
-            "title": "GEO-CAPE : Geostationary Coastal and Air Pollution Events",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSeaBASS%2FGEO-CAPE%2FDATA001",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSeaBASS%2FGEO-CAPE%2FDATA001",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://seabass.gsfc.nasa.gov/experiment/GEO-CAPE/",
-                    "description": "Detailed information about the SeaBASS Experiment such as cruises, funding, and investigators",
                     "@type": "dcat:Distribution",
+                    "description": "Detailed information about the SeaBASS Experiment such as cruises, funding, and investigators",
+                    "downloadURL": "https://seabass.gsfc.nasa.gov/experiment/GEO-CAPE/",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 }
             ],
+            "identifier": "C1633360241-OB_DAAC",
+            "issued": "2011-07-11",
+            "keyword": [
+                "ocean chemistry",
+                "ocean optics",
+                "ocean temperature",
+                "salinity/density",
+                "oceans",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/SeaBASS/GEO-CAPE/DATA001",
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
+            "temporal": "2011-07-11T00:00:02Z/2023-04-17T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "GEO-CAPE : Geostationary Coastal and Air Pollution Events"
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
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-j-leisa-3-jupiter-v1.1_rp76-2vn9",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "new horizons",
                 "earth",
@@ -1315277,834 +1315279,846 @@
                 "j1 io",
                 "ganymede"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-J-LEISA-3-JUPITER-V1.1",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-j-leisa-3-jupiter-v1.1_rp76-2vn9",
-            "description": "This data set contains Calibrated data taken by the New Horizons Linear Etalon Imaging Spectral Array instrument during the Jupiter encounter mission phase.",
-            "title": "NEW HORIZONS LEISA JUPITER ENCOUNTER V1.1",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "NEW HORIZONS LEISA JUPITER ENCOUNTER V1.1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=CO-S-RSS-1-SROC18-V1.0",
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
-                "saturn"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "The Cassini Radio Science Saturn Ring and Atmospheric Occultation experiments (SROC18) Raw Data Archive is a time-ordered collection of radio science raw data acquired on January 5, 18, 31 and February 25, 2013, during the Cassini Extended Extended Mission.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.co-s-rss-1-sroc18-v1.0_rp7g-jagh",
+            "issued": "2021-05-21",
+            "keyword": [
+                "cassini-huygens",
+                "saturn"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=CO-S-RSS-1-SROC18-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.co-s-rss-1-sroc18-v1.0_rp7g-jagh",
-            "description": "The Cassini Radio Science Saturn Ring and Atmospheric Occultation experiments (SROC18) Raw Data Archive is a time-ordered collection of radio science raw data acquired on January 5, 18, 31 and February 25, 2013, during the Cassini Extended Extended Mission.",
-            "title": "CASSINI RSS RAW DATA SET - SROC18 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "CASSINI RSS RAW DATA SET - SROC18 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC1-0609-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 1 phase 2014-11-20 to 2015-03-10. It is a Global Gravity measurement at the comet 67P and covers the time 2015-02-28T03:37:05.000 to 2015-02-28T09:51:37.500.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc1-0609-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC1-0609-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc1-0609-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 1 phase 2014-11-20 to 2015-03-10. It is a Global Gravity measurement at the comet 67P and covers the time 2015-02-28T03:37:05.000 to 2015-02-28T09:51:37.500.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 1 0609 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 1 0609 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/163",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Hall, F. G., K. F. Huemmrich, D. E. Strebel, S. J. Goetz, J. E. Nickeson, and K. D. Woods. 1996. NWS Daily Climatology Data: 1976 (SNF). [National Weather Service Daily Climatology Data: 1976 (Superior National Forest)]. Data set. Available on-line [http://www.daac.ornl.gov] from Oak Ridge National Laboratory Distributed Active Archive Center, Oak Ridge, Tennessee, U.S.A. Based on F. G. Hall, K. F. Huemmrich, D. E. Strebel, S. J. Goetz, J. E. Nickeson, and K. D. Woods, Biophysical, Morphological, Canopy Optical Property, and Productivity Data from the Superior National Forest, NASA Technical Memorandum 104568, National Aeronautics and Space Administration, Goddard Space Flight Center, Greenbelt, Maryland, U.S.A., 1992. doi:10.3334/ORNLDAAC/163",
-            "issued": "2024-03-01",
-            "temporal": "1976-01-01T00:00:00Z/1976-12-31T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-03-04",
-            "keyword": [
-                "precipitation",
-                "atmosphere",
-                "earth science",
-                "atmospheric temperature",
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
-            "identifier": "C2884974230-ORNL_CLOUD",
             "description": "Daily min, max, average temperature (F), precipitation (water equivalent in inches), and daily insolation (Langleys) for the Superior National Forest area as collected by NWS and U. of Minnesota",
-            "graphic-preview-description": "Browse Image",
-            "title": "NWS Daily Climatology Data: 1976 (SNF)",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/snf_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F163",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F163",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/snf/SNF_MET_1976/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/snf/SNF_MET_1976/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/SNF/guides/nws_daily_climate_1976.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/SNF/guides/nws_daily_climate_1976.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/163",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/163",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/snf/SNF_MET_1976/comp/met_1976.def",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/snf/SNF_MET_1976/comp/met_1976.def",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/snf/SNF_MET_1976/comp/met_1976.txt",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/snf/SNF_MET_1976/comp/met_1976.txt",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/snf/SNF_MET_1976/comp/nws_daily_climate_1976.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/snf/SNF_MET_1976/comp/nws_daily_climate_1976.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/snf/SNF_MET_1976/comp/nws_daily_climate_1976.txt",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/snf/SNF_MET_1976/comp/nws_daily_climate_1976.txt",
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
+            "identifier": "C2884974230-ORNL_CLOUD",
+            "issued": "2024-03-01",
+            "keyword": [
+                "precipitation",
+                "atmosphere",
+                "earth science",
+                "atmospheric temperature",
+                "atmospheric water vapor",
+                "atmospheric radiation"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/163",
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
+            "temporal": "1976-01-01T00:00:00Z/1976-12-31T23:59:59Z",
             "theme": [
                 "SNF",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "NWS Daily Climatology Data: 1976 (SNF)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RPCLAP-2-EXT1-MTP027-V1.0",
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
+            "description": "This data set contains\nEDITED data from Rosetta RPC-LAP, acquired during the ROSETTA\nEXTENSION 1 MTP027 mission phase. Comet C-G/67P was the primary target.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rpclap-2-ext1-mtp027-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RPCLAP-2-EXT1-MTP027-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rpclap-2-ext1-mtp027-v1.0",
-            "description": "This data set contains\nEDITED data from Rosetta RPC-LAP, acquired during the ROSETTA\nEXTENSION 1 MTP027 mission phase. Comet C-G/67P was the primary target.",
-            "title": "ROSETTA-ORBITER 67P RPCLAP 2\nEXT1 MTP027 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RPCLAP 2\nEXT1 MTP027 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-ROSINA-2-ESC2-V1.0",
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
+            "description": "This data set contains science data acquired by the COPS, DFMS and RTOF ROSINA sensors between 2015-03-11 and 2015-06-30 during the Escort phase 2 of the Rosetta mission at the comet 67P/CG",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rosina-2-esc2-v1.0_rpb4-auuu",
+            "issued": "2018-06-26",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-ROSINA-2-ESC2-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rosina-2-esc2-v1.0_rpb4-auuu",
-            "description": "This data set contains science data acquired by the COPS, DFMS and RTOF ROSINA sensors between 2015-03-11 and 2015-06-30 during the Escort phase 2 of the Rosetta mission at the comet 67P/CG",
-            "title": "ROSETTA-ORBITER 67P ROSINA 2\n                                    ESC2 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "ROSETTA-ORBITER 67P ROSINA 2\n                                    ESC2 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=DS1-C-PEPE-2-RAW-DATA-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This data set contains ion and electron flux as a function of energy and angle, and ion composition data acquired during the Deep Space 1 encounter with comet 19P/Borrelly. The data are uncalibrated and provided in spacecraft coordinates.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ds1-c-pepe-2-raw-data-v1.0_rpch-v7ef",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "deep space 1",
                 "solar wind",
                 "9969 braille",
                 "19p/borrelly 1 (1904 y2)"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=DS1-C-PEPE-2-RAW-DATA-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ds1-c-pepe-2-raw-data-v1.0_rpch-v7ef",
-            "description": "This data set contains ion and electron flux as a function of energy and angle, and ion composition data acquired during the Deep Space 1 encounter with comet 19P/Borrelly. The data are uncalibrated and provided in spacecraft coordinates.",
-            "title": "DEEP SPACE 1 19P/BORRELLY ENCOUNTER UNCALIBRATED PEPE V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "DEEP SPACE 1 19P/BORRELLY ENCOUNTER UNCALIBRATED PEPE V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-GST-3-RDR-GEOGRAPHOS-RADAR-V1.1",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "Delay-Doppler images and continuous wave, dual-polarization spectra of 1620 Geographos taken during the August 1994 closest approach to Earth (0.0333AU at minimum).",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-gst-3-rdr-geographos-radar-v1.1_rpdu-expf",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "1620 geographos",
                 "support archives",
                 "geographos"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-GST-3-RDR-GEOGRAPHOS-RADAR-V1.1",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-gst-3-rdr-geographos-radar-v1.1_rpdu-expf",
-            "description": "Delay-Doppler images and continuous wave, dual-polarization spectra of 1620 Geographos taken during the August 1994 closest approach to Earth (0.0333AU at minimum).",
-            "title": "GEOGRAPHOS RADAR V1.1",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "GEOGRAPHOS RADAR V1.1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MEX-M-MRS-1%2F2%2F3-EXT3-3266-V1.0",
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
+            "description": "This is a Mars Express Radio Science data set, collected during the extended mission phase 2010-01-01 to 2012-12-31. It is a Global Gravity measurement and covers the time 2012-07-26T05:00:43.000 to 2012-07-26T07:31:13.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mex-m-mrs-1-2-3-ext3-3266-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "mars",
+                "mars express"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MEX-M-MRS-1%2F2%2F3-EXT3-3266-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mex-m-mrs-1-2-3-ext3-3266-v1.0",
-            "description": "This is a Mars Express Radio Science data set, collected during the extended mission phase 2010-01-01 to 2012-12-31. It is a Global Gravity measurement and covers the time 2012-07-26T05:00:43.000 to 2012-07-26T07:31:13.000.",
-            "title": "MARS EXPRESS MARS MRS 1/2/3\n                                     EXTENDED MISSION 3 3266 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "MARS EXPRESS MARS MRS 1/2/3\n                                     EXTENDED MISSION 3 3266 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1737",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Guevara, M., C.E. Arroyo-cruz, N. Brunsell, C.O. Cruz-gaistardo, G.M. Domke, J. Equihua, J. Etchevers, D.J. Hayes, T. Hengl, A. Ibelles, K. Johnson, B. de Jong, Z. Libohova, R. Llamas, L. Nave, J.L. Ornelas, F. Paz, R. Ressl, A. Schwartz, S. Wills, and R. Vargas. 2020. Soil Organic Carbon Estimates for 30-cm Depth, Mexico and Conterminous USA, 1991-2011. ORNL DAAC, Oak Ridge, Tennessee, USA. https://doi.org/10.3334/ORNLDAAC/1737",
-            "issued": "2020-05-14",
-            "temporal": "1991-01-01T00:00:00Z/2011-12-31T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-06-12",
-            "keyword": [
-                "earth science",
-                "land surface",
-                "soils"
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
-            "identifier": "C2389105307-ORNL_CLOUD",
-            "description": "This dataset provides two sets of gridded estimates of estimated soil organic carbon (SOC) and associated uncertainties for 0-30 cm topsoil layer in kg SOC/m2 at 250-m resolution across Mexico and the conterminous USA (CONUS). The first set of gridded SOC estimates, for the period 1991-2010, were derived using multi-source SOC field data and multiple environmental variables representative of the soil forming environment coupled with a machine learning approach (i.e., simulated annealing) and regression tree ensemble modeling for optimized SOC prediction. Predictions of gridded SOC and uncertainty based on multiple bulk density (BD) pedotransfer functions (PFTs) are also included. The second set of gridded SOC estimates, for the period 2009-2011, were derived from two fully independent validation field datasets from across both countries. Note that the same environmental variables and modeling approach used for the first set of estimates were applied to the second set to assess the models' sensitivity to multiple SOC data sources. The SOC field data for the first set of estimates are provided in this dataset and the other data sources, including the two independent validation field datasets, are referenced.",
-            "graphic-preview-description": "Soil organic carbon (SOC) for 0-30 cm topsoil layer in kg SOC/m2 at 250-m resolution across Mexico and the conterminous USA (CONUS) for the period 1991-2010. Source: data file SOC_prediction_1991_2010.tif",
-            "title": "Soil Organic Carbon Estimates for 30-cm Depth, Mexico and Conterminous USA, 1991-2011",
-            "graphic-preview-file": "https://daac.ornl.gov/CMS/guides/CMS_SOC_Mexico_CONUS_Fig1.png",
-            "programCode": [
-                "026:001"
-            ],
+                "hasEmail": "mailto:uso@daac.ornl.gov"
+            },
+            "description": "This dataset provides two sets of gridded estimates of estimated soil organic carbon (SOC) and associated uncertainties for 0-30 cm topsoil layer in kg SOC/m2 at 250-m resolution across Mexico and the conterminous USA (CONUS). The first set of gridded SOC estimates, for the period 1991-2010, were derived using multi-source SOC field data and multiple environmental variables representative of the soil forming environment coupled with a machine learning approach (i.e., simulated annealing) and regression tree ensemble modeling for optimized SOC prediction. Predictions of gridded SOC and uncertainty based on multiple bulk density (BD) pedotransfer functions (PFTs) are also included. The second set of gridded SOC estimates, for the period 2009-2011, were derived from two fully independent validation field datasets from across both countries. Note that the same environmental variables and modeling approach used for the first set of estimates were applied to the second set to assess the models' sensitivity to multiple SOC data sources. The SOC field data for the first set of estimates are provided in this dataset and the other data sources, including the two independent validation field datasets, are referenced.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1737",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1737",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/cms/CMS_SOC_Mexico_CONUS/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/cms/CMS_SOC_Mexico_CONUS/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/CMS/guides/CMS_SOC_Mexico_CONUS.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/CMS/guides/CMS_SOC_Mexico_CONUS.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1737",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1737",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/cms/CMS_SOC_Mexico_CONUS/comp/CMS_SOC_Mexico_CONUS.pdf",
-                    "description": "Soil Organic Carbon Estimates for 30 cm Depth, Mexico and Conterminous USA, 1991-2011: CMS_SOC_Mexico_CONUS.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "Soil Organic Carbon Estimates for 30 cm Depth, Mexico and Conterminous USA, 1991-2011: CMS_SOC_Mexico_CONUS.pdf",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/cms/CMS_SOC_Mexico_CONUS/comp/CMS_SOC_Mexico_CONUS.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://daac.ornl.gov/CMS/guides/CMS_SOC_Mexico_CONUS_Fig1.png",
-                    "description": "Soil organic carbon (SOC) for 0-30 cm topsoil layer in kg SOC/m2 at 250-m resolution across Mexico and the conterminous USA (CONUS) for the period 1991-2010. Source: data file SOC_prediction_1991_2010.tif",
                     "@type": "dcat:Distribution",
+                    "description": "Soil organic carbon (SOC) for 0-30 cm topsoil layer in kg SOC/m2 at 250-m resolution across Mexico and the conterminous USA (CONUS) for the period 1991-2010. Source: data file SOC_prediction_1991_2010.tif",
+                    "downloadURL": "https://daac.ornl.gov/CMS/guides/CMS_SOC_Mexico_CONUS_Fig1.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 }
             ],
+            "graphic-preview-description": "Soil organic carbon (SOC) for 0-30 cm topsoil layer in kg SOC/m2 at 250-m resolution across Mexico and the conterminous USA (CONUS) for the period 1991-2010. Source: data file SOC_prediction_1991_2010.tif",
+            "graphic-preview-file": "https://daac.ornl.gov/CMS/guides/CMS_SOC_Mexico_CONUS_Fig1.png",
+            "identifier": "C2389105307-ORNL_CLOUD",
+            "issued": "2020-05-14",
+            "keyword": [
+                "earth science",
+                "land surface",
+                "soils"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1737",
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
             "spatial": "-129.79 11.32 -65.58 49.61",
+            "temporal": "1991-01-01T00:00:00Z/2011-12-31T23:59:59Z",
             "theme": [
                 "CMS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Soil Organic Carbon Estimates for 30-cm Depth, Mexico and Conterminous USA, 1991-2011"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-4-PRL-67P-M08-REFLECT-V1.0",
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
+            "description": "This CODMAC level 4 data set contains radiometric calibrated and geometric distortion corrected (resampled) image data in reflectance units (normalized and thus without unit), acquired by the OSIRIS Narrow Angle Camera on the Rosetta spacecraft during the PRELANDING mission phase, covering the period from 2014-09-23T10:00:00.000 to 2014-10-24T09:59:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V1.0 is the first version of this dataset: Lien corrected dataset after October 2018 PSA/PDS external peer review.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-4-prl-67p-m08-reflect-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-4-PRL-67P-M08-REFLECT-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-4-prl-67p-m08-reflect-v1.0",
-            "description": "This CODMAC level 4 data set contains radiometric calibrated and geometric distortion corrected (resampled) image data in reflectance units (normalized and thus without unit), acquired by the OSIRIS Narrow Angle Camera on the Rosetta spacecraft during the PRELANDING mission phase, covering the period from 2014-09-23T10:00:00.000 to 2014-10-24T09:59:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V1.0 is the first version of this dataset: Lien corrected dataset after October 2018 PSA/PDS external peer review.",
-            "title": "ROSETTA-ORBITER 67P OSINAC 4 PRL-MTP008 RDR-REFLECT V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P OSINAC 4 PRL-MTP008 RDR-REFLECT V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-EXT1-1419-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the ROSETTA EXTENSION 1 phase 2016-01-01 to 2016-04-05. It is a Global Gravity measurement at the comet 67P and covers the time 2016-02-12T14:59:32.000 to 2016-02-12T20:18:36.500.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-ext1-1419-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-EXT1-1419-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-ext1-1419-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the ROSETTA EXTENSION 1 phase 2016-01-01 to 2016-04-05. It is a Global Gravity measurement at the comet 67P and covers the time 2016-02-12T14:59:32.000 to 2016-02-12T20:18:36.500.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     ROSETTA EXTENSION 1 1419 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     ROSETTA EXTENSION 1 1419 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/141",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Hall, F. G., K. F. Huemmrich, D. E. Strebel, S. J. Goetz, J. E. Nickeson, and K. D. Woods. 1996. Biomass of Sacrificed Spruce/Aspen (SNF). [Biomass of Sacrificed Spruce/Aspen (Superior National Forest)]. Data set. Available on-line [http://www.daac.ornl.gov] from Oak Ridge National Laboratory Distributed Active Archive Center, Oak Ridge, Tennessee, U.S.A. Based on F. G. Hall, K. F. Huemmrich, D. E. Strebel, S. J. Goetz, J. E. Nickeson, and K. D. Woods, Biophysical, Morphological, Canopy Optical Property, and Productivity Data from the Superior National Forest, NASA Technical Memorandum 104568, National Aeronautics and Space Administration, Goddard Space Flight Center, Greenbelt, Maryland, U.S.A., 1992. doi:10.3334/ORNLDAAC/141",
-            "issued": "2024-03-01",
-            "temporal": "1983-08-01T00:00:00Z/1984-08-14T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-03-04",
-            "keyword": [
-                "earth science",
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
-            "identifier": "C2884971856-ORNL_CLOUD",
             "description": "Dimension analysis (diameter at breast high, tree height, depth of crown), estimated leaf area, and total aboveground biomass for sacrificed spruce and aspens in Superior National Forest, MN",
-            "graphic-preview-description": "Browse Image",
-            "title": "Biomass of Sacrificed Spruce/Aspen (SNF)",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/snf_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F141",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F141",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/snf/SNF_BIOMASS/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/snf/SNF_BIOMASS/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/SNF/guides/biomass_spruce_aspen.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/SNF/guides/biomass_spruce_aspen.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/141",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/141",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/snf/SNF_BIOMASS/comp/biomass.def",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/snf/SNF_BIOMASS/comp/biomass.def",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/snf/SNF_BIOMASS/comp/biomass.txt",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/snf/SNF_BIOMASS/comp/biomass.txt",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/snf/SNF_BIOMASS/comp/biomass_spruce_aspen.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/snf/SNF_BIOMASS/comp/biomass_spruce_aspen.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/snf/SNF_BIOMASS/comp/biomass_spruce_aspen.txt",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/snf/SNF_BIOMASS/comp/biomass_spruce_aspen.txt",
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
+            "identifier": "C2884971856-ORNL_CLOUD",
+            "issued": "2024-03-01",
+            "keyword": [
+                "earth science",
+                "vegetation",
+                "biosphere"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/141",
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
+            "temporal": "1983-08-01T00:00:00Z/1984-08-14T23:59:59Z",
             "theme": [
                 "SNF",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Biomass of Sacrificed Spruce/Aspen (SNF)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://techport.nasa.gov/view/12100",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2012-10-01",
-            "temporal": "2012-10-01T00:00:00Z/2014-12-01T00:00:00Z",
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
-                "johnson space center"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Douglas Terrier",
                 "hasEmail": "mailto:douglas.a.terrier@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Space Technology Mission Directorate"
-            },
-            "identifier": "TECHPORT_12100",
             "description": "&lt;p&gt;Currently, the Air Quality Monitor (AQM) on-board ISS provides specific information for a number of target compounds in the air. However, there is a significant subset of common target compounds between air and water.&amp;nbsp; Naturally, the following question arises, &amp;ldquo;Can the AQM be used for both air and water quality monitoring?&amp;rdquo;&amp;nbsp; Previous directorate-level IR&amp;amp;D funding led to the development of a water sample introduction method for mass spectrometry using electro-thermal vaporization (ETV).&amp;nbsp; This vaporization source allows analytes in water samples to enter the gas phase, where they can be analyzed using a variety of techniques.&amp;nbsp; This project will focus on the integration of the ETV with a ground-based AQM.&amp;nbsp; The capabilities of this integrated platform will be evaluated using a subset of toxicologically important compounds.&lt;/p&gt;&lt;p&gt;The ETV unit was constructed using two glass tubes and a nichrome ribbon powered by a programmable DC power supply (G W Instec, PSM-3004).&amp;nbsp; The nichrome ribbon was threaded through two 3-mm wide, 1-cm-long slot cuts on the inner tube placed 1.5 cm past the inlet.&amp;nbsp; The ribbon was held securely by compressing it between the inner tube and two halves of an outer glass tube.&amp;nbsp; These halves were held together using a flexible metal clamp.&amp;nbsp; Inside the inner tube the ribbon was slightly curved, and an indent (1 mm diameter) was made on its surface for depositing a measured liquid sample drop.&amp;nbsp; The ribbon was positioned in the upper half of the inner tube in such a way that the edge of the ribbon faced the front (inlet) side of the ETV unit.&amp;nbsp; Holes (1 mm diameter) were made on the outer and inner glass tubes for sample introduction and were aligned with the ribbon indent.&lt;/p&gt;&lt;p&gt;The viability of the ETV approach for the analysis of water analytes was demonstrated using a ground-based, laboratory scale analyzer (reference:&amp;nbsp; Dwivedi, P. et al.&amp;nbsp; &amp;ldquo;Electro-Thermal Vaporization Direct Analysis in Real Time-Mass Spectrometry for Water Contaminant Analysis During Space Missions,&amp;rdquo; Analytical Chemistry, 85, 9898-9906 (2013)).&amp;nbsp; The work in this proposal will extend that effort and interface the ETV to a ground version of the current in-flight AQM.&amp;nbsp; Liquid sample will be introduce via a pipet through the sample injection port and placed onto the nichrome ribbon heated to a set temperature by an external, programmable power supply.&amp;nbsp; Upon vaporization of the water sample, the target analytes will be swept into the AQM Sample-In port using nitrogen carrier gas.&amp;nbsp; A vapor-phase analysis can then be performed by the AQM to identify and quantify the target analytes in the water samples.&amp;nbsp; Parameters to be optimized include water sample size, carrier gas sweep rate, and ribbon temperature.&amp;nbsp; The operating parameters of the vapor-phase analysis performed by the AQM will also need to be modified for this type of sampling methodology.&amp;nbsp; A simple two-position valve attached to the ETV and a diverter tube will allow for manual selection of either a water sample through the ETV or an air sample through the diverter tube.&amp;nbsp; The primary objective of this effort is to evaluate the viability of the ETV with ground-based, flight hardware.&amp;nbsp; A proof-of-concept unit capable of water and air analysis utilizing the ETV will be developed.&amp;nbsp; The target water analytes to be used in this work will come from a list provided by the water SMEs in the Toxicology and Environmental Chemistry Laboratories at JSC.&amp;nbsp; These analytes are commonly observed in the ground analysis of water samples from ISS.&amp;nbsp; A preliminary engineering evaluation of this set-up could potentially be performed with the goal of formulating a viable plan of integrating the ETV to the control soft",
-            "title": "Use of the Operational Air Quality Monitor (AQM) for In-Flight Water Testing Project",
-            "programCode": [
-                "026:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "http://techport.nasa.gov/xml-api/12100",
                     "mediaType": "application/xml"
                 }
-            ]
+            ],
+            "identifier": "TECHPORT_12100",
+            "issued": "2012-10-01",
+            "keyword": [
+                "active",
+                "project",
+                "johnson space center"
+            ],
+            "landingPage": "http://techport.nasa.gov/view/12100",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Space Technology Mission Directorate"
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
+            "temporal": "2012-10-01T00:00:00Z/2014-12-01T00:00:00Z",
+            "title": "Use of the Operational Air Quality Monitor (AQM) for In-Flight Water Testing Project"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/T5MXF865107T",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Soil Moisture Active Passive (SMAP) L1-L3 Ancillary Satellite Data V001. Version 1. Archived by National Aeronautics and Space Administration, U.S. Government, NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/T5MXF865107T.",
-            "issued": "2015-01-31",
-            "temporal": "2015-01-31T00:00:00Z/2024-11-04T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-01",
-            "keyword": [
-                "earth science",
-                "platform characteristics",
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
-            "identifier": "C1539129338-NSIDC_ECS",
             "description": "This ancillary SMAP product contains two dynamic data sets describing 1) the attitude and 2) the trajectory of the SMAP satellite. The data files are generated using quaternions from the SMAP spacecraft and inputs from earth receiving stations, respectively.",
-            "title": "Soil Moisture Active Passive (SMAP) L1-L3 Ancillary Satellite Data V001",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FT5MXF865107T",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FT5MXF865107T",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/SMAP_ANC/SMAP_L1_L3_ANC_SATELLITE.001/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/SMAP_ANC/SMAP_L1_L3_ANC_SATELLITE.001/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=SMAP_L1_L3_ANC_SATELLITE+V001",
-                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=SMAP_L1_L3_ANC_SATELLITE+V001",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/T5MXF865107T",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/T5MXF865107T",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/T5MXF865107T",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/T5MXF865107T",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C1539129338-NSIDC_ECS",
+            "issued": "2015-01-31",
+            "keyword": [
+                "earth science",
+                "platform characteristics",
+                "spectral/engineering"
+            ],
+            "landingPage": "https://doi.org/10.5067/T5MXF865107T",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2024-11-01",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA NSIDC DAAC"
+            },
             "spatial": "-180.0 -86.4 180.0 86.4",
+            "temporal": "2015-01-31T00:00:00Z/2024-11-04T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Soil Moisture Active Passive (SMAP) L1-L3 Ancillary Satellite Data V001"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-J-PEPSSI-3-JUPITER-V1.1",
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
+            "description": "This data set contains Calibrated data taken by the New Horizons Pluto Energetic Particle Spectrometer Science Investigation instrument during the Jupiter encounter mission phase.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-j-pepssi-3-jupiter-v1.1_rpt9-jpkz",
+            "issued": "2018-06-26",
+            "keyword": [
+                "new horizons",
+                "solar wind"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-J-PEPSSI-3-JUPITER-V1.1",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-j-pepssi-3-jupiter-v1.1_rpt9-jpkz",
-            "description": "This data set contains Calibrated data taken by the New Horizons Pluto Energetic Particle Spectrometer Science Investigation instrument during the Jupiter encounter mission phase.",
-            "title": "NEW HORIZONS PEPSSI JUPITER ENCOUNTER V1.1",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "NEW HORIZONS PEPSSI JUPITER ENCOUNTER V1.1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.nasa.gov/d/rpve-yf52",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "GeneLab Outreach",
+                "hasEmail": "mailto:genelab-outreach@lists.nasa.gov"
+            },
+            "description": "Microgravity has a dramatic impact on human physiology illustrated in particular with skeletal muscle impairment. A thorough understanding of the mechanisms leading to loss of muscle mass and structural disorders is necessary for the definition of efficient clinical and spaceflight countermeasures. We investigated the effects of long-term bed rest on transcriptome of soleus (SOL) and vastus lateralis (VL) muscles in healthy women (BRC group n=8) and the potential beneficial impact of protein supplementation (BRN group n=8) and of a combined resistance and aerobic training (BRE group n=8). Gene expression profiles were obtained using an in-house made microarray containing 6681 muscles-relevant genes. A two-class statistical analysis was applied on the 2103 genes with consolidated expression. We identified 472 and 207 modified genes respectively for SOL and VL in BRC group. Further clustering approaches identifying relevant biological mechanisms or pathways underlined five main subclusters. Three are composed almost of upregulated genes involved mainly in nucleic acid and protein metabolism and two composed almost of downregulated genes involved in energy metabolism. Exercise countermeasure demonstrated a drastic compensatory effect decreasing the number of differentially-expressed genes by 89 and 96% in SOL and VL. In contrast nutrition countermeasure had a moderate effect and decreased the number of differentially-expressed genes by 40 and 25% in SOL and VL. Our results allowed reporting a systematic global and comprehensive view of long-term woman muscle atrophy and brought new lights and insights for space environment and for women who undergo a long-term clinical bed rest. Biological samples were collected from Pre- and Post- bed rest (BR) soleus and vastus lateralis biopsies of each subject from the three groups (bed rest only: BRC; Exercise: BRE; Nutrition: BRN). six technical replicate values (2 duplicate hybridizations a et b to chips with triplicate spots xxx) were obtained for each skeletal muscle sample. Thus for each subject 12 expression measurements (6 before BR and 6 after BR) were obtained for each muscle.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "GeneLab Study Page",
+                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-51",
+                    "mediaType": "text/html",
+                    "title": "Woman skeletal muscle transcriptome with bed rest and countermeasures."
+                }
+            ],
+            "identifier": "nasa_genelab_GLDS-51_rpve-yf52",
             "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
             "keyword": [
                 "p-gse14798-6",
                 "nucleic_acid_extraction",
@@ -1316123,153 +1316137,153 @@
                 "p-gse14798-4",
                 "image_aquisition"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "GeneLab Outreach",
-                "hasEmail": "mailto:genelab-outreach@lists.nasa.gov"
-            },
+            "landingPage": "https://data.nasa.gov/d/rpve-yf52",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "nasa_genelab_GLDS-51_rpve-yf52",
-            "description": "Microgravity has a dramatic impact on human physiology illustrated in particular with skeletal muscle impairment. A thorough understanding of the mechanisms leading to loss of muscle mass and structural disorders is necessary for the definition of efficient clinical and spaceflight countermeasures. We investigated the effects of long-term bed rest on transcriptome of soleus (SOL) and vastus lateralis (VL) muscles in healthy women (BRC group n=8) and the potential beneficial impact of protein supplementation (BRN group n=8) and of a combined resistance and aerobic training (BRE group n=8). Gene expression profiles were obtained using an in-house made microarray containing 6681 muscles-relevant genes. A two-class statistical analysis was applied on the 2103 genes with consolidated expression. We identified 472 and 207 modified genes respectively for SOL and VL in BRC group. Further clustering approaches identifying relevant biological mechanisms or pathways underlined five main subclusters. Three are composed almost of upregulated genes involved mainly in nucleic acid and protein metabolism and two composed almost of downregulated genes involved in energy metabolism. Exercise countermeasure demonstrated a drastic compensatory effect decreasing the number of differentially-expressed genes by 89 and 96% in SOL and VL. In contrast nutrition countermeasure had a moderate effect and decreased the number of differentially-expressed genes by 40 and 25% in SOL and VL. Our results allowed reporting a systematic global and comprehensive view of long-term woman muscle atrophy and brought new lights and insights for space environment and for women who undergo a long-term clinical bed rest. Biological samples were collected from Pre- and Post- bed rest (BR) soleus and vastus lateralis biopsies of each subject from the three groups (bed rest only: BRC; Exercise: BRE; Nutrition: BRN). six technical replicate values (2 duplicate hybridizations a et b to chips with triplicate spots xxx) were obtained for each skeletal muscle sample. Thus for each subject 12 expression measurements (6 before BR and 6 after BR) were obtained for each muscle.",
-            "title": "Woman skeletal muscle transcriptome with bed rest and countermeasures.",
-            "programCode": [
-                "026:005"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-51",
-                    "description": "GeneLab Study Page",
-                    "@type": "dcat:Distribution",
-                    "title": "Woman skeletal muscle transcriptome with bed rest and countermeasures."
-                }
-            ],
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "Woman skeletal muscle transcriptome with bed rest and countermeasures."
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=DIF-CAL-HRII-2-GROUND-TV1-V1.0",
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
-                "deep impact"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This data set contains 2-dimensional spectral images acquired by the High Resolution Instrument's Infrared Spectrometer (HRII) during the the first preflight thermal-vacuum test (TV1) of the Deep Impact instruments.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.dif-cal-hrii-2-ground-tv1-v1.0_rpwb-5ssu",
+            "issued": "2018-06-26",
+            "keyword": [
+                "calibration",
+                "deep impact"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=DIF-CAL-HRII-2-GROUND-TV1-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.dif-cal-hrii-2-ground-tv1-v1.0_rpwb-5ssu",
-            "description": "This data set contains 2-dimensional spectral images acquired by the High Resolution Instrument's Infrared Spectrometer (HRII) during the the first preflight thermal-vacuum test (TV1) of the Deep Impact instruments.",
-            "title": "DEEP IMPACT PREFLIGHT THERMAL-VACUUM 1 HRII DATA",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "DEEP IMPACT PREFLIGHT THERMAL-VACUUM 1 HRII DATA"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.7265/4sc0-n729",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Map of Natural (Landscape) and Permafrost Zones and the Net of Soil Temperature Meteorological Stations in Russia and Middle Asian Mountains, Version 1. Version 1. Archived by National Aeronautics and Space Administration, U.S. Government, Russian Academy of Sciences Earth Cryosphere Institute and Institute for Phytoch. https://doi.org/10.7265/4sc0-n729.",
-            "issued": "2019-09-20",
-            "temporal": "1970-01-01T00:00:00Z/2024-12-23T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-12-19",
-            "keyword": [
-                "terrestrial hydrosphere",
-                "cryosphere",
-                "earth science",
-                "frozen ground",
-                "landscape",
-                "land surface",
-                "snow/ice"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "David Gilichinsky",
                 "hasEmail": "mailto:gilichin@online.stack.net"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NSIDC"
-            },
-            "identifier": "C1386206886-NSIDCV0",
             "description": "This data set is a vector coverage of the Map of Natural Landscape and Permafrost Zones and the Net of Soil Temperature Meteorological Stations in Russia and Middle Asian Mountains  (scale 1:4000000), published by the Russian Academy of Sciences Earth Cryosphere Institute and Institute for Phytochemical and Biological Problems in Earth Science  The original map was compiled by E. Melnikov and D.A. Gilichinsky.  The digital map was created in Geograph, which is a Geographic Information System developed by the GIS Research Center, Institute of Geography, Russian Academy of Sciences. Data are available through FTP.",
-            "title": "Map of Natural (Landscape) and Permafrost Zones and the Net of Soil Temperature Meteorological Stations in Russia and Middle Asian Mountains, Version 1",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.7265%2F4sc0-n729",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.7265%2F4sc0-n729",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/forms/GGD618_or.html?major_version=1",
-                    "description": "Direct download, with optional registration page.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download, with optional registration page.",
+                    "downloadURL": "https://nsidc.org/forms/GGD618_or.html?major_version=1",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.7265/4sc0-n729",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.7265/4sc0-n729",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.7265/4sc0-n729",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.7265/4sc0-n729",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C1386206886-NSIDCV0",
+            "issued": "2019-09-20",
+            "keyword": [
+                "terrestrial hydrosphere",
+                "cryosphere",
+                "earth science",
+                "frozen ground",
+                "landscape",
+                "land surface",
+                "snow/ice"
+            ],
+            "landingPage": "https://doi.org/10.7265/4sc0-n729",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2024-12-19",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NSIDC"
+            },
             "spatial": "10.0 32.0 163.0 90.0",
+            "temporal": "1970-01-01T00:00:00Z/2024-12-23T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Map of Natural (Landscape) and Permafrost Zones and the Net of Soil Temperature Meteorological Stations in Russia and Middle Asian Mountains, Version 1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.nasa.gov/d/rpx5-th7s",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "GeneLab Outreach",
+                "hasEmail": "mailto:genelab-outreach@lists.nasa.gov"
+            },
+            "description": "Bacterial behavior has been observed to change during spaceflight. Higher final cell counts enhanced biofilm formation increased virulence and reduced susceptibility to antibiotics have been reported to occur for cells cultured in space . Most of these phenomena are theorized as being an indirect effect of an altered extracellular environment where the carbon source uptake is inhibited and excreted acidic byproducts buildup around the cell due to the lack of gravity-driven transport forces. However to date neither spaceflight results ground-based studies physical measurement techniques nor computational approaches have provided sufficient evidence needed to confirm this model. Gene expression data from the Antibiotic Effectiveness in Space (AES-1) experiment however have now allowed us to look into the biomolecular processes behind these observations and showed a systematic activation of glucose starvation and acid resistance genes. These results corroborate the reduced mass transport model proposed to govern bacterial responses to spaceflight. Furthermore the gene expression data suggests that metabolism was stimulated in space which could play a role in causing the observed increase in bacterial cell concentrations in microgravity. Similarly the decrease in extracellular pH may also be involved with the reported increase in virulence in space.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "GeneLab Study Page",
+                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-95",
+                    "mediaType": "text/html",
+                    "title": "A Molecular Genetic Basis Explaining Altered Bacterial Behavior in Space"
+                }
+            ],
+            "identifier": "nasa_genelab_GLDS-95_rpx5-th7s",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
             "keyword": [
                 "treatment protocol",
                 "library construction",
@@ -1316280,634 +1316294,634 @@
                 "nucleic acid sequencing",
                 "sequence analysis data transformation"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "GeneLab Outreach",
-                "hasEmail": "mailto:genelab-outreach@lists.nasa.gov"
-            },
+            "landingPage": "https://data.nasa.gov/d/rpx5-th7s",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "nasa_genelab_GLDS-95_rpx5-th7s",
-            "description": "Bacterial behavior has been observed to change during spaceflight. Higher final cell counts enhanced biofilm formation increased virulence and reduced susceptibility to antibiotics have been reported to occur for cells cultured in space . Most of these phenomena are theorized as being an indirect effect of an altered extracellular environment where the carbon source uptake is inhibited and excreted acidic byproducts buildup around the cell due to the lack of gravity-driven transport forces. However to date neither spaceflight results ground-based studies physical measurement techniques nor computational approaches have provided sufficient evidence needed to confirm this model. Gene expression data from the Antibiotic Effectiveness in Space (AES-1) experiment however have now allowed us to look into the biomolecular processes behind these observations and showed a systematic activation of glucose starvation and acid resistance genes. These results corroborate the reduced mass transport model proposed to govern bacterial responses to spaceflight. Furthermore the gene expression data suggests that metabolism was stimulated in space which could play a role in causing the observed increase in bacterial cell concentrations in microgravity. Similarly the decrease in extracellular pH may also be involved with the reported increase in virulence in space.",
-            "title": "A Molecular Genetic Basis Explaining Altered Bacterial Behavior in Space",
-            "programCode": [
-                "026:005"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-95",
-                    "description": "GeneLab Study Page",
-                    "@type": "dcat:Distribution",
-                    "title": "A Molecular Genetic Basis Explaining Altered Bacterial Behavior in Space"
-                }
-            ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "A Molecular Genetic Basis Explaining Altered Bacterial Behavior in Space"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/191",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Daubenmire, J. 2014. NPP Grassland: Canas, Costa Rica, 1969-1970, R1 . ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/191",
-            "issued": "2013-11-12",
-            "temporal": "1969-07-10T00:00:00Z/1970-06-14T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-08-17",
-            "keyword": [
-                "biosphere",
-                "earth science",
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
-            "identifier": "C2751940644-ORNL_CLOUD",
             "description": "This data set contains two ASCII text files; one providing above-ground biomass, productivity, and bioelement concentration data for a derived savanna at Canas (10.4 N 85.1 W Elevation 45 m) in northwestern Costa Rica, and the other providing climate data from the La Pacifica weather station near Canas and rom other sources. Monthly dynamics of above-ground plant matter were monitored from July 1969 to June 1970 using harvest procedures within an exclosure to restrict grazing. The climate data are available from three time periods: 1951-1960, 1963, and 1969-1970. The climate is characterized by a dry season from late November to April, with little seasonal differences in temperature. The Canas study site is dominated almost exclusively by Hyparrhenia rufa, a perennial grass of African origin introduced extensively throughout the tropics. The original vegetation cover was closed semideciduous forest. The study area was deforested and converted to a grass savanna around January 1947, 22.5 years before the start of the present study. Light grazing by cattle and horses is accompanied by burning of the Canas savanna annually between December and April. Above-ground net primary productivity (ANPP) was estimated by two methods: maximum standing crop of herbaceous shoot tissue (peak live + dead matter) (968 g/m2/year); and the sum of monthly estimates of shoot production (including estimated mortality) (1,387 g/m2/year). End-of-season (November, 1969) live root biomass estimates of 1,220 g/m2 at 0-20 cm depth and 2,254 g/m2 at 0-100 cm depth are available in the literature.",
-            "graphic-preview-description": "Browse Image",
-            "title": "NPP Grassland: Canas, Costa Rica, 1969-1970, R1",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/npp_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F191",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F191",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/npp/grassland/NPP_CNS/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/npp/grassland/NPP_CNS/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/NPP/guides/NPP_CNS.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/NPP/guides/NPP_CNS.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/191",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/191",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/npp/grassland/NPP_CNS/comp/NPP_CNS.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/npp/grassland/NPP_CNS/comp/NPP_CNS.pdf",
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
+            "identifier": "C2751940644-ORNL_CLOUD",
+            "issued": "2013-11-12",
+            "keyword": [
+                "biosphere",
+                "earth science",
+                "ecological dynamics"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/191",
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
             "spatial": "10.4 -85.1",
+            "temporal": "1969-07-10T00:00:00Z/1970-06-14T23:59:59Z",
             "theme": [
                 "NPP",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "NPP Grassland: Canas, Costa Rica, 1969-1970, R1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/AQR50-3Y3AE",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "NASA Aquarius project. 2017-12-07. Aquarius Official Release Level 3 Rain-flagged Sea Surface Salinity Standard Mapped Image Ascending Seasonal Data. Version 5.0. Aquarius Sea Surface Salinity Products. Goddard Space Flight Center, 8800 Greenbelt Rd.; Greeenbelt, MD., 20771, USA. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/GSFC OBPG. https://doi.org/10.5067/AQR50-3Y3AE. http://podaac.jpl.nasa.gov/SeaSurfaceSalinity/Aquarius. NASA Aquarius project, NASA/GSFC OBPG, 2017-12-07, Aquarius Official Release Level 3 Rain-flagged Sea Surface Salinity Standard Mapped Image Ascending Seasonal Data V5.0, http://podaac.jpl.nasa.gov/SeaSurfaceSalinity/Aquarius.",
-            "issued": "2017-10-21",
-            "temporal": "2011-08-25T01:55:23Z/2015-06-07T11:41:38Z",
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
-            "identifier": "C2491757014-POCLOUD",
-            "description": "Aquarius Level 3 sea surface salinity (SSS) rain-flagged standard mapped image data contains gridded 1 degree spatial resolution SSS averaged over daily, 7 day, monthly, and seasonal time\nscales. This particular data set is the Seasonal, Ascending rain-flagged rain-flagged sea surface salinity product for version 5.0 of the Aquarius data set. Only retrieved values for Ascending passes have been used to create this product.  The Aquarius instrument is onboard the AQUARIUS/SAC-D satellite, a collaborative effort between NASA and the Argentinian Space Agency Comision Nacional de Actividades Espaciales (CONAE). The instrument consists of three radiometers in push broom alignment at incidence angles of 29, 38, and 46 degrees incidence angles relative to the shadow side of the orbit.  Footprints for the beams are: 76 km (along-track) x 94 km (cross-track), 84 km x 120 km and 96km x 156 km, yielding a total cross-track swath of 370 km. The radiometers measure brightness temperature at 1.413 GHz in their respective horizontal and vertical polarizations (TH and TV). A scatterometer operating at 1.26 GHz measures ocean backscatter in each footprint that is used for surface roughness corrections in the estimation of salinity. The scatterometer has an approximate 390km swath.",
-            "release-place": "Goddard Space Flight Center, 8800 Greenbelt Rd.; Greeenbelt, MD., 20771, USA",
-            "series-name": "Aquarius Official Release Level 3 Rain-flagged Sea Surface Salinity Standard Mapped Image Ascending Seasonal Data",
-            "graphic-preview-description": "Thumbnail",
             "creator": "NASA Aquarius project",
-            "title": "Aquarius Official Release Level 3 Rain-flagged Sea Surface Salinity Standard Mapped Image Ascending Seasonal Data V5.0",
-            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/AQUARIUS_L3_SSS-RainFlagged_SMIA_3MONTH_V5.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "Aquarius Level 3 sea surface salinity (SSS) rain-flagged standard mapped image data contains gridded 1 degree spatial resolution SSS averaged over daily, 7 day, monthly, and seasonal time\nscales. This particular data set is the Seasonal, Ascending rain-flagged rain-flagged sea surface salinity product for version 5.0 of the Aquarius data set. Only retrieved values for Ascending passes have been used to create this product.  The Aquarius instrument is onboard the AQUARIUS/SAC-D satellite, a collaborative effort between NASA and the Argentinian Space Agency Comision Nacional de Actividades Espaciales (CONAE). The instrument consists of three radiometers in push broom alignment at incidence angles of 29, 38, and 46 degrees incidence angles relative to the shadow side of the orbit.  Footprints for the beams are: 76 km (along-track) x 94 km (cross-track), 84 km x 120 km and 96km x 156 km, yielding a total cross-track swath of 370 km. The radiometers measure brightness temperature at 1.413 GHz in their respective horizontal and vertical polarizations (TH and TV). A scatterometer operating at 1.26 GHz measures ocean backscatter in each footprint that is used for surface roughness corrections in the estimation of salinity. The scatterometer has an approximate 390km swath.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAQR50-3Y3AE",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAQR50-3Y3AE",
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
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/AQUARIUS_L3_SSS-RainFlagged_SMIA_3MONTH_V5.jpg",
-                    "description": "Thumbnail",
                     "@type": "dcat:Distribution",
+                    "description": "Thumbnail",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/AQUARIUS_L3_SSS-RainFlagged_SMIA_3MONTH_V5.jpg",
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
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2491757014-POCLOUD",
-                    "description": "HTTPS endpoint for data browse and download",
                     "@type": "dcat:Distribution",
+                    "description": "HTTPS endpoint for data browse and download",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2491757014-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2491757014-POCLOUD",
-                    "description": "Browse granule search results in Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse granule search results in Earthdata Search",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2491757014-POCLOUD",
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
+            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/AQUARIUS_L3_SSS-RainFlagged_SMIA_3MONTH_V5.jpg",
+            "identifier": "C2491757014-POCLOUD",
+            "issued": "2017-10-21",
+            "keyword": [
+                "oceans",
+                "earth science",
+                "salinity/density"
+            ],
+            "landingPage": "https://doi.org/10.5067/AQR50-3Y3AE",
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
+            "series-name": "Aquarius Official Release Level 3 Rain-flagged Sea Surface Salinity Standard Mapped Image Ascending Seasonal Data",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2011-08-25T01:55:23Z/2015-06-07T11:41:38Z",
             "theme": [
                 "AQUARIUS SAC-D",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Aquarius Official Release Level 3 Rain-flagged Sea Surface Salinity Standard Mapped Image Ascending Seasonal Data V5.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/VIIRS/VNP43D11.001",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Crystal Schaaf, Zhuosen Wang, Xiaoyang Zhang, Alan Strahler\r\n. 2019-11-07. VNP43D11. Version 001. VIIRS/NPP BRDF/Albedo Parameter 2 Band M4 Daily L3 Global 30 ArcSec CMG V001\r\n. Sioux Falls, South Dakota, USA. Archived by National Aeronautics and Space Administration, U.S. Government, NASA EOSDIS Land Processes Distributed Active Archive Center. https://doi.org/10.5067/VIIRS/VNP43D11.001. https://doi.org/10.5067/VIIRS/VNP43D11.001. Digital Science Data. The DOI landing page provides citations in APA and Chicago styles.\r\n.",
-            "issued": "2019-11-07",
-            "temporal": "2012-01-19T00:00:00Z/2024-05-20T00:00:00Z",
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
-            "identifier": "C1607315698-LPDAAC_ECS",
-            "description": "The NASA/NOAA Suomi National Polar-orbiting Partnership (Suomi NPP) Visible Infrared Imaging Radiometer Suite (VIIRS) Bidirectional Reflectance Distribution Function (BRDF) and Albedo Model Parameter 2 Band M4 product (VNP43D11) is produced daily using 16 days of data at 30 arc second (1,000 meter) resolution. Data are temporally weighted to the ninth day, which is reflected in the file name. The VNP43D product suite is provided in a Climate Modeling Grid (CMG), which covers the entire globe for use in climate simulation models. Due to the large file size, each VNP43D product contains just one data layer. Each of the three model parameters (isotropic, volumetric, and geometric) for each of the nine VIIRS moderate resolution bands along with the visible, near-infrared (NIR), and shortwave bands included in the VNP43MA1 (https://doi.org/10.5067/VIIRS/VNP43MA1.001) product is stored in a separate file as VNP43D01 through VNP43D36. In addition to the bands included in VNP43MA1, this product suite includes model parameters for the VIIRS Day/Night Band (DNB) as VNP43D37 through VNP43D39. Details regarding methodology are available on the VNP43MA1 product page and in the Algorithm Theoretical Basis Document (ATBD).\r\n\r\nVNP43D11 is the BRDF volumetric parameter for VIIRS band M4 (0.555 \u03bcm). The volumetric parameter, in conjunction with the isotropic and geometric parameters, is used to derive the BRDF/Albedo values for VIIRS band M4.",
-            "release-place": "Sioux Falls, South Dakota, USA",
-            "series-name": "VNP43D11",
             "creator": "Crystal Schaaf, Zhuosen Wang, Xiaoyang Zhang, Alan Strahler",
-            "title": "VIIRS/NPP BRDF/Albedo Parameter 2 Band M4 Daily L3 Global 30 ArcSec CMG V001",
-            "programCode": [
-                "026:001"
-            ],
+            "data-presentation-form": "Digital Science Data",
+            "description": "The NASA/NOAA Suomi National Polar-orbiting Partnership (Suomi NPP) Visible Infrared Imaging Radiometer Suite (VIIRS) Bidirectional Reflectance Distribution Function (BRDF) and Albedo Model Parameter 2 Band M4 product (VNP43D11) is produced daily using 16 days of data at 30 arc second (1,000 meter) resolution. Data are temporally weighted to the ninth day, which is reflected in the file name. The VNP43D product suite is provided in a Climate Modeling Grid (CMG), which covers the entire globe for use in climate simulation models. Due to the large file size, each VNP43D product contains just one data layer. Each of the three model parameters (isotropic, volumetric, and geometric) for each of the nine VIIRS moderate resolution bands along with the visible, near-infrared (NIR), and shortwave bands included in the VNP43MA1 (https://doi.org/10.5067/VIIRS/VNP43MA1.001) product is stored in a separate file as VNP43D01 through VNP43D36. In addition to the bands included in VNP43MA1, this product suite includes model parameters for the VIIRS Day/Night Band (DNB) as VNP43D37 through VNP43D39. Details regarding methodology are available on the VNP43MA1 product page and in the Algorithm Theoretical Basis Document (ATBD).\r\n\r\nVNP43D11 is the BRDF volumetric parameter for VIIRS band M4 (0.555 \u03bcm). The volumetric parameter, in conjunction with the isotropic and geometric parameters, is used to derive the BRDF/Albedo values for VIIRS band M4.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FVIIRS%2FVNP43D11.001",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FVIIRS%2FVNP43D11.001",
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
-                    "downloadURL": "https://doi.org/10.5067/VIIRS/VNP43D11.001",
-                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
+                    "downloadURL": "https://doi.org/10.5067/VIIRS/VNP43D11.001",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/xhdf5",
-                    "downloadURL": "https://e4ftl01.cr.usgs.gov/VIIRS/VNP43D11.001/",
-                    "description": "LP DAAC Data Pool provides direct access to available products via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "LP DAAC Data Pool provides direct access to available products via HTTPS.",
+                    "downloadURL": "https://e4ftl01.cr.usgs.gov/VIIRS/VNP43D11.001/",
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
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=C1607315698-LPDAAC_ECS",
-                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=C1607315698-LPDAAC_ECS",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://opendap.cr.usgs.gov/opendap/hyrax/VNP43D11.001/contents.html",
-                    "description": "Access data via Open-source Project for a Network Data Access Protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access data via Open-source Project for a Network Data Access Protocol.",
+                    "downloadURL": "https://opendap.cr.usgs.gov/opendap/hyrax/VNP43D11.001/contents.html",
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
-                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/filespec/VIIRS/1/VNP43D11",
-                    "description": "The File Specification provides a description of the product file including Scientific Data Sets and their attributes.",
                     "@type": "dcat:Distribution",
+                    "description": "The File Specification provides a description of the product file including Scientific Data Sets and their attributes.",
+                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/filespec/VIIRS/1/VNP43D11",
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
+            "identifier": "C1607315698-LPDAAC_ECS",
+            "issued": "2019-11-07",
+            "keyword": [
+                "earth science",
+                "surface radiative properties",
+                "land surface"
+            ],
+            "landingPage": "https://doi.org/10.5067/VIIRS/VNP43D11.001",
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
+            "series-name": "VNP43D11",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2012-01-19T00:00:00Z/2024-05-20T00:00:00Z",
             "theme": [
                 "NPP-JPSS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "VIIRS/NPP BRDF/Albedo Parameter 2 Band M4 Daily L3 Global 30 ArcSec CMG V001"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/SLR/SLR_ILRSORB_001",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "International Laser Ranging Service (ILRS), SLR Combination Center (CC) Orbit Product, Greenbelt, MD, USA:NASA Crustal Dynamics Data Information System (CDDIS), Accessed [[enter user data access date]] at doi: 10.5067/SLR/SLR_ILRSORB_001",
-            "issued": "2016-01-01",
-            "temporal": "2016-01-01T00:00:00Z/2025-01-27T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-11",
-            "keyword": [
-                "earth science",
-                "geodetics",
-                "solid earth",
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
-            "identifier": "C1537291495-CDDIS",
             "description": "This derived product set consists of Satellite Laser Ranging Final Orbit Product (weekly files, generated weekly) from the NASA Crustal Dynamics Data Information System (CDDIS). SLR provides unambiguous range measurements to mm precision that can be aggregated over the global network to provide very accurate satellite orbits, time histories of station position and motion, and many other geophysical parameters. SLR operates in the optical region and is the only space geodetic technique that measures unambiguous range directly. Analysis of SLR data contributes to the terrestrial reference frame, modeling of the spatial and temporal variations of the Earth's gravitational field, and monitoring of millimeter-level variations in the location of the center of mass of the total Earth system (solid Earth-atmosphere-oceans). In addition, SLR provides precise orbit determination for spaceborne radar altimeter missions. It provides a means for sub-nanosecond global time transfer, and a basis for special tests of the Theory of General Relativity. Analysis Centers (ACs) of the International Laser Ranging Service (ILRS) retrieve SLR data on regular schedules to produce precise orbits identifying the position and velocity of satellites equipped with retroreflectors. The ILRS Analysis Center Coordinators (ACC) uses these individual AC solutions to generate the official ILRS final combined orbit products, as well as backup combination. The final products are considered the most consistent and highest quality ILRS solutions; they consist of weekly orbit files, generated on a weekly basis with a typical delay of 3 days. All orbit solution files utilize the extended standard product-3 (SP3) format and span 7 days from 00:00 to 23:45 UTC.",
-            "title": "Satellite Laser Ranging (SLR) Final Orbit Product (daily files, generated weekly) from NASA CDDIS",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSLR%2FSLR_ILRSORB_001",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSLR%2FSLR_ILRSORB_001",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://cddis.nasa.gov/archive/slr/products",
-                    "description": "URL for retrieval of SLR derived products through https",
                     "@type": "dcat:Distribution",
+                    "description": "URL for retrieval of SLR derived products through https",
+                    "downloadURL": "https://cddis.nasa.gov/archive/slr/products",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://cddis.nasa.gov/Data_and_Derived_Products/SLR/SLR_product_holdings.html",
-                    "description": "URL for more information about SLR derived products",
                     "@type": "dcat:Distribution",
+                    "description": "URL for more information about SLR derived products",
+                    "downloadURL": "https://cddis.nasa.gov/Data_and_Derived_Products/SLR/SLR_product_holdings.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://doi.org/10.5067/SLR/SLR_ILRSORB_001",
-                    "description": "URL for more information about SLR derived products",
                     "@type": "dcat:Distribution",
+                    "description": "URL for more information about SLR derived products",
+                    "downloadURL": "http://doi.org/10.5067/SLR/SLR_ILRSORB_001",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 }
             ],
+            "identifier": "C1537291495-CDDIS",
+            "issued": "2016-01-01",
+            "keyword": [
+                "earth science",
+                "geodetics",
+                "solid earth",
+                "gravity/gravitational field",
+                "tectonics"
+            ],
+            "landingPage": "https://doi.org/10.5067/SLR/SLR_ILRSORB_001",
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
+            "temporal": "2016-01-01T00:00:00Z/2025-01-27T00:00:00Z",
             "theme": [
                 "ILRS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Satellite Laser Ranging (SLR) Final Orbit Product (daily files, generated weekly) from NASA CDDIS"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=ICE-C-ULECA-3-RDR-GIACOBINI-ZIN-V1.0",
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
-                "giacobini-zinner",
-                "international cometary explorer"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "Energetic particle observations made with the ULECA sensor on the International Cometary Explorer encounter with comet Giacobini-Zinner in Sept, 1985.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ice-c-uleca-3-rdr-giacobini-zin-v1.0_rqaa-9g3w",
+            "issued": "2021-05-21",
+            "keyword": [
+                "giacobini-zinner",
+                "international cometary explorer"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=ICE-C-ULECA-3-RDR-GIACOBINI-ZIN-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ice-c-uleca-3-rdr-giacobini-zin-v1.0_rqaa-9g3w",
-            "description": "Energetic particle observations made with the ULECA sensor on the International Cometary Explorer encounter with comet Giacobini-Zinner in Sept, 1985.",
-            "title": "ULECA SELECTED COUNTS FOR GZ ENCOUNTER",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ULECA SELECTED COUNTS FOR GZ ENCOUNTER"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.nasa.gov/d/rqbb-ipi5",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "GeneLab Outreach",
+                "hasEmail": "mailto:genelab-outreach@lists.nasa.gov"
+            },
+            "description": "The objective of the Rodent Research-6 (RR-6) study was to evaluate muscle atrophy in mice during spaceflight and to test the efficacy of a novel therapeutic to mitigate muscle wasting. The experiment involved an implantable subcutaneous nanochannel delivery system (nDS; between scapula) which delivered the drug formoterol (FMT; a selective Beta-2 adrenoceptor agonist) over the course of time. To this end a cohort of forty 32-weeks-old female C57BL/6NTac mice were either sham operated. or implanted with vehicle or treatment-filled nDS and launched in two Transporters (20 mice per Transporter) on SpaceX-13 on December 15 2017. They were transferred to Rodent Habitats onboard the International Space Station (ISS) and maintained in microgravity for 29 days (N=20 Live Animal Return [LAR]) or >50 days (N=20 ISS Terminal). After 29 days the 20 LAR animals were returned live to back to Earth on January 13 2018. After splashdown the animals were ambulatory on-ground for ~4 days until all subjects were processed during one day of dissections. There were two Baseline groups of animals sacrificed (LAR Baseline & FLT Baseline; N=20; 40 animals; ~36 weeks old) at Kennedy Space Center (KSC; 12/9/17). A Ground Control group mimicked the Flight LAR group which was housed at KSC then shipped alive to Novartis   facilities where both the LAR and LAR Ground Control groups were processed (~41 weeks old; 1/16/18). All were anesthetized with isoflurane blood samples were obtained by closed-chest cardiac puncture and the animals were euthanized by exsanguination and thoracotomy. The 20 ISS Terminal mice were anesthetized via intraperitoneal injection of ketamine/xylazine/acepromazine over the course of a four days of dissections (2/6/18 until 2/9/18; 53-56 days after launch; 44 weeks old at time of on-orbit dissections). Blood samples and euthanasia were conducted the same as LAR and Baseline. Following blood draw and hind limb dissection the ISS-terminal animal carcasses were wrapped in aluminum foil placed in a ziploc bag and placed in storage at -80C or colder until return. The ISS-terminal Ground Controls (at KSC) followed the same euthanasia timeline methods and preservation. The final processing of frozen ISS-terminal frozen ISS-terminal Ground Controls and frozen 0-day FLT baseline animals were completed at Houston Methodist Research Institute in Houston TX (5/21/18 until 5/24/18). GeneLab received samples of dorsal skin from only sham treated animals (no drug treated animals) from the following groups Flight: LAR (n=9) ISS Terminal (n=9); Ground Controls: LAR GC (N=9) ISS Terminal GC (N=10) LAR Baseline (n=10) ISS Terminal Baseline (n=6). Total RNA was extracted and sequenced at a target depth of 60 M clusters per sample (ribodepleted paired end 150).",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "GeneLab Study Page",
+                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-243",
+                    "mediaType": "text/html",
+                    "title": "Transcriptional analysis of dorsal skin from mice flown on the RR-6 mission"
+                }
+            ],
+            "identifier": "nasa_genelab_GLDS-243_rqbb-ipi5",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
             "keyword": [
                 "animal husbandry",
                 "spike-in protocol",
@@ -1316923,694 +1316937,656 @@
                 "spaceflight",
                 "genelab rnaseq data processing protocol"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "GeneLab Outreach",
-                "hasEmail": "mailto:genelab-outreach@lists.nasa.gov"
-            },
+            "landingPage": "https://data.nasa.gov/d/rqbb-ipi5",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "nasa_genelab_GLDS-243_rqbb-ipi5",
-            "description": "The objective of the Rodent Research-6 (RR-6) study was to evaluate muscle atrophy in mice during spaceflight and to test the efficacy of a novel therapeutic to mitigate muscle wasting. The experiment involved an implantable subcutaneous nanochannel delivery system (nDS; between scapula) which delivered the drug formoterol (FMT; a selective Beta-2 adrenoceptor agonist) over the course of time. To this end a cohort of forty 32-weeks-old female C57BL/6NTac mice were either sham operated. or implanted with vehicle or treatment-filled nDS and launched in two Transporters (20 mice per Transporter) on SpaceX-13 on December 15 2017. They were transferred to Rodent Habitats onboard the International Space Station (ISS) and maintained in microgravity for 29 days (N=20 Live Animal Return [LAR]) or >50 days (N=20 ISS Terminal). After 29 days the 20 LAR animals were returned live to back to Earth on January 13 2018. After splashdown the animals were ambulatory on-ground for ~4 days until all subjects were processed during one day of dissections. There were two Baseline groups of animals sacrificed (LAR Baseline & FLT Baseline; N=20; 40 animals; ~36 weeks old) at Kennedy Space Center (KSC; 12/9/17). A Ground Control group mimicked the Flight LAR group which was housed at KSC then shipped alive to Novartis   facilities where both the LAR and LAR Ground Control groups were processed (~41 weeks old; 1/16/18). All were anesthetized with isoflurane blood samples were obtained by closed-chest cardiac puncture and the animals were euthanized by exsanguination and thoracotomy. The 20 ISS Terminal mice were anesthetized via intraperitoneal injection of ketamine/xylazine/acepromazine over the course of a four days of dissections (2/6/18 until 2/9/18; 53-56 days after launch; 44 weeks old at time of on-orbit dissections). Blood samples and euthanasia were conducted the same as LAR and Baseline. Following blood draw and hind limb dissection the ISS-terminal animal carcasses were wrapped in aluminum foil placed in a ziploc bag and placed in storage at -80C or colder until return. The ISS-terminal Ground Controls (at KSC) followed the same euthanasia timeline methods and preservation. The final processing of frozen ISS-terminal frozen ISS-terminal Ground Controls and frozen 0-day FLT baseline animals were completed at Houston Methodist Research Institute in Houston TX (5/21/18 until 5/24/18). GeneLab received samples of dorsal skin from only sham treated animals (no drug treated animals) from the following groups Flight: LAR (n=9) ISS Terminal (n=9); Ground Controls: LAR GC (N=9) ISS Terminal GC (N=10) LAR Baseline (n=10) ISS Terminal Baseline (n=6). Total RNA was extracted and sequenced at a target depth of 60 M clusters per sample (ribodepleted paired end 150).",
-            "title": "Transcriptional analysis of dorsal skin from mice flown on the RR-6 mission",
-            "programCode": [
-                "026:005"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-243",
-                    "description": "GeneLab Study Page",
-                    "@type": "dcat:Distribution",
-                    "title": "Transcriptional analysis of dorsal skin from mice flown on the RR-6 mission"
-                }
-            ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "Transcriptional analysis of dorsal skin from mice flown on the RR-6 mission"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=HP-SSA-HK-2%2F3-V1.0",
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
+            "description": "The Huygens Atmospheric Instrument is one of the six experiment onboard the Huygens probe. HASI is a muultisensor package designed to measure the physical quantities characterizing Titan's atmosphere during entry and descent phase and at the surface.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.hp-ssa-hk-2-3-v1.0_rqcj-ayck",
+            "issued": "2018-06-26",
+            "keyword": [
+                "cassini-huygens",
+                "titan"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=HP-SSA-HK-2%2F3-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.hp-ssa-hk-2-3-v1.0_rqcj-ayck",
-            "description": "The Huygens Atmospheric Instrument is one of the six experiment onboard the Huygens probe. HASI is a muultisensor package designed to measure the physical quantities characterizing Titan's atmosphere during entry and descent phase and at the surface.",
-            "title": "HUYGENS ENGINEERING DATA",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "HUYGENS ENGINEERING DATA"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.7927/H4222RQJ",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "National Oceanic and Atmospheric Administration - NOAA National Geophysical Data Center - NGDC. 2018-12-06. West Africa Coastal Vulnerability Mapping: Subset of DMSP-OLS Nighttime Lights for Economic Activity, 2010. Version 1.00. Palisades, NY. Archived by National Aeronautics and Space Administration, U.S. Government, Socioeconomic Data and Applications Center (SEDAC). https://doi.org/10.7927/H4222RQJ. https://doi.org/10.7927/H4222RQJ.",
-            "issued": "2018-12-06",
-            "temporal": "2010-01-01T00:00:00Z/2010-12-31T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2018-12-06",
-            "references": [
-                "https://doi.org/10.7927/H4F769H4",
-                "https://doi.org/10.7927/H45T3HFZ",
-                "https://doi.org/10.7927/H4X9287N",
-                "https://doi.org/10.7927/H4SJ1HHX",
-                "https://doi.org/10.7927/H4J10131",
-                "https://doi.org/10.7927/H4DB7ZR7",
-                "https://doi.org/10.7927/H48K7719",
-                "https://doi.org/10.7927/H44T6G9K",
-                "https://doi.org/10.7927/H4125QK5",
-                "https://doi.org/10.7927/H4W95738",
-                "https://doi.org/10.7927/H4RJ4GCJ",
-                "https://doi.org/10.7927/H4MS3QP8",
-                "https://doi.org/10.7927/H4H41PCK",
-                "https://doi.org/10.7927/H49K485P",
-                "https://doi.org/10.7927/H4K0726D",
-                "http://doi.org/10.3390/ijgi4042561",
-                "https://doi.org/10.3390/rs70201855"
-            ],
-            "keyword": [
-                "human settlements",
-                "earth science",
-                "economic resources",
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
-            "identifier": "C1577564961-SEDAC",
-            "description": "The West Africa Coastal Vulnerability Mapping: Subset of DMSP-OLS Nighttime Lights for Economic Activity, 2010 data set is based on Version 4 of the Defense Meteorological Satellite Program Operational Linescan System (DMSP-OLS) Nighttime Lights Time Series, 2010 annual global composite of radiance lights inter-calibrated to the digital number (DN) values of gain 55 for satellite F16 (2006). These data are commonly used for identifying human settlements and economic activity. The DNs are on a Unitless scale ranging from 0 (no light) to 4,000 (greatest light intensity). This data set is a proxy for economic activity within 200 kilometers of the coast of West Africa. The resolution of the grid is 30 arc-second, or approximately 1 km at the equator. The data were provided courtesy of Christopher Elvidge and Kimberly Baugh of the Earth Observation Group, NOAA National Geophysical Data Center (NGDC), where image and data processing were performed.",
-            "release-place": "Palisades, NY",
-            "graphic-preview-description": "Sample browse graphic of the data set.",
             "creator": "National Oceanic and Atmospheric Administration - NOAA National Geophysical Data Center - NGDC",
-            "title": "West Africa Coastal Vulnerability Mapping: Subset of DMSP-OLS Nighttime Lights for Economic Activity, 2010",
-            "graphic-preview-file": "https://sedac.ciesin.columbia.edu/downloads/maps/wacvm/wacvm-subset-dmsp-ols-nighttime-lights-economic-activity-2010/sedac-logo.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The West Africa Coastal Vulnerability Mapping: Subset of DMSP-OLS Nighttime Lights for Economic Activity, 2010 data set is based on Version 4 of the Defense Meteorological Satellite Program Operational Linescan System (DMSP-OLS) Nighttime Lights Time Series, 2010 annual global composite of radiance lights inter-calibrated to the digital number (DN) values of gain 55 for satellite F16 (2006). These data are commonly used for identifying human settlements and economic activity. The DNs are on a Unitless scale ranging from 0 (no light) to 4,000 (greatest light intensity). This data set is a proxy for economic activity within 200 kilometers of the coast of West Africa. The resolution of the grid is 30 arc-second, or approximately 1 km at the equator. The data were provided courtesy of Christopher Elvidge and Kimberly Baugh of the Earth Observation Group, NOAA National Geophysical Data Center (NGDC), where image and data processing were performed.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.7927%2FH4222RQJ",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.7927%2FH4222RQJ",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/downloads/maps/wacvm/wacvm-subset-dmsp-ols-nighttime-lights-economic-activity-2010/sedac-logo.jpg",
-                    "description": "Sample browse graphic of the data set.",
                     "@type": "dcat:Distribution",
+                    "description": "Sample browse graphic of the data set.",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/downloads/maps/wacvm/wacvm-subset-dmsp-ols-nighttime-lights-economic-activity-2010/sedac-logo.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/wacvm-subset-dmsp-ols-nighttime-lights-economic-activity-2010/data-download",
-                    "description": "Data Download Page",
                     "@type": "dcat:Distribution",
+                    "description": "Data Download Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/wacvm-subset-dmsp-ols-nighttime-lights-economic-activity-2010/data-download",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://sedac.ciesin.columbia.edu/data/set/wacvm-subset-dmsp-ols-nighttime-lights-economic-activity-2010/docs",
-                    "description": "Documentation Page",
                     "@type": "dcat:Distribution",
+                    "description": "Documentation Page",
+                    "downloadURL": "http://sedac.ciesin.columbia.edu/data/set/wacvm-subset-dmsp-ols-nighttime-lights-economic-activity-2010/docs",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/wacvm-subset-dmsp-ols-nighttime-lights-economic-activity-2010",
-                    "description": "Data Set\u00a0Overview Page",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set\u00a0Overview Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/wacvm-subset-dmsp-ols-nighttime-lights-economic-activity-2010",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "graphic-preview-description": "Sample browse graphic of the data set.",
+            "graphic-preview-file": "https://sedac.ciesin.columbia.edu/downloads/maps/wacvm/wacvm-subset-dmsp-ols-nighttime-lights-economic-activity-2010/sedac-logo.jpg",
+            "identifier": "C1577564961-SEDAC",
+            "issued": "2018-12-06",
+            "keyword": [
+                "human settlements",
+                "earth science",
+                "economic resources",
+                "human dimensions"
+            ],
+            "landingPage": "https://doi.org/10.7927/H4222RQJ",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2018-12-06",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "SEDAC"
+            },
+            "references": [
+                "https://doi.org/10.7927/H4F769H4",
+                "https://doi.org/10.7927/H45T3HFZ",
+                "https://doi.org/10.7927/H4X9287N",
+                "https://doi.org/10.7927/H4SJ1HHX",
+                "https://doi.org/10.7927/H4J10131",
+                "https://doi.org/10.7927/H4DB7ZR7",
+                "https://doi.org/10.7927/H48K7719",
+                "https://doi.org/10.7927/H44T6G9K",
+                "https://doi.org/10.7927/H4125QK5",
+                "https://doi.org/10.7927/H4W95738",
+                "https://doi.org/10.7927/H4RJ4GCJ",
+                "https://doi.org/10.7927/H4MS3QP8",
+                "https://doi.org/10.7927/H4H41PCK",
+                "https://doi.org/10.7927/H49K485P",
+                "https://doi.org/10.7927/H4K0726D",
+                "http://doi.org/10.3390/ijgi4042561",
+                "https://doi.org/10.3390/rs70201855"
+            ],
+            "release-place": "Palisades, NY",
             "spatial": "-16.71 1.65 16.21 13.9",
+            "temporal": "2010-01-01T00:00:00Z/2010-12-31T00:00:00Z",
             "theme": [
                 "WACVM",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "West Africa Coastal Vulnerability Mapping: Subset of DMSP-OLS Nighttime Lights for Economic Activity, 2010"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1708",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Vetrita, Y., and M.A. Cochrane. 2019. Annual Burned Area from Landsat, Mawas, Central Kalimantan, Indonesia, 1997-2015. ORNL DAAC, Oak Ridge, Tennessee, USA. https://doi.org/10.3334/ORNLDAAC/1708",
-            "issued": "2019-10-08",
-            "temporal": "1997-01-01T00:00:00Z/2015-12-31T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-06-12",
-            "keyword": [
-                "earth science",
-                "human dimensions",
-                "natural hazards",
-                "biosphere",
-                "ecosystems",
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
-            "identifier": "C2389021866-ORNL_CLOUD",
             "description": "This dataset provides maps of annual burned area for the part of Mawas conservation program in Central Kalimantan, Indonesia from 1997 through 2015. Landsat imagery (TM, ETM+, OLI/TIR) at 30 m resolution was obtained for this 19-year period, including the variables surface reflectance, brightness temperature, and pixel quality assurance, plus the indices NDVI, NDMI, NBR, NBR2, SAVI, and MSAVI. The MODIS active fire product (MCD14) was used to define when fires occurred. Random Forest classifications were used to separate burned and unburned 30-m pixels with inputs of composites of Landsat indices and thermal bands, based on the pre- and post-fire values.",
-            "graphic-preview-description": "The area burned in 1997 and 1998 in Mawas area, Central Kalimantan, Indonesia is shown in pink. Inset with white dot, shows location of Mawas study site on the Island of Borneo. Source: Mawas.BA.1997.001.shp",
-            "title": "Annual Burned Area from Landsat, Mawas, Central Kalimantan, Indonesia, 1997-2015",
-            "graphic-preview-file": "https://daac.ornl.gov/CMS/guides/Annual_Burned_Area_Maps_Fig1.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1708",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1708",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/cms/Annual_Burned_Area_Maps/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/cms/Annual_Burned_Area_Maps/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/CMS/guides/Annual_Burned_Area_Maps.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/CMS/guides/Annual_Burned_Area_Maps.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1708",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1708",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/cms/Annual_Burned_Area_Maps/comp/Annual_Burned_Area_Maps.pdf",
-                    "description": "CMS: Landsat-derived Annual Burned Maps for Mawas, Kalimantan, Indonesia, 1997-2015: Annual_Burned_Area_Maps.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "CMS: Landsat-derived Annual Burned Maps for Mawas, Kalimantan, Indonesia, 1997-2015: Annual_Burned_Area_Maps.pdf",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/cms/Annual_Burned_Area_Maps/comp/Annual_Burned_Area_Maps.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://daac.ornl.gov/CMS/guides/Annual_Burned_Area_Maps_Fig1.png",
-                    "description": "The area burned in 1997 and 1998 in Mawas area, Central Kalimantan, Indonesia is shown in pink. Inset with white dot, shows location of Mawas study site on the Island of Borneo. Source: Mawas.BA.1997.001.shp",
                     "@type": "dcat:Distribution",
+                    "description": "The area burned in 1997 and 1998 in Mawas area, Central Kalimantan, Indonesia is shown in pink. Inset with white dot, shows location of Mawas study site on the Island of Borneo. Source: Mawas.BA.1997.001.shp",
+                    "downloadURL": "https://daac.ornl.gov/CMS/guides/Annual_Burned_Area_Maps_Fig1.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 }
             ],
+            "graphic-preview-description": "The area burned in 1997 and 1998 in Mawas area, Central Kalimantan, Indonesia is shown in pink. Inset with white dot, shows location of Mawas study site on the Island of Borneo. Source: Mawas.BA.1997.001.shp",
+            "graphic-preview-file": "https://daac.ornl.gov/CMS/guides/Annual_Burned_Area_Maps_Fig1.png",
+            "identifier": "C2389021866-ORNL_CLOUD",
+            "issued": "2019-10-08",
+            "keyword": [
+                "earth science",
+                "human dimensions",
+                "natural hazards",
+                "biosphere",
+                "ecosystems",
+                "ecological dynamics"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1708",
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
             "spatial": "114.39 -2.5 114.61 -2.21",
+            "temporal": "1997-01-01T00:00:00Z/2015-12-31T23:59:59Z",
             "theme": [
                 "CMS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Annual Burned Area from Landsat, Mawas, Central Kalimantan, Indonesia, 1997-2015"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/CAMEX-4/PHOTOMETER/DATA101",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Kelly, Kenneth K, Karen H Rosenlof, Kenneth C Aikin and Erik C Richard.2002. CAMEX-4 DUAL-BEAM UV-ABSORPTION OZONE PHOTOMETER [indicate subset used]. Dataset available online from the NASA Global Hydrometeorology Resource Center DAAC, Huntsville, Alabama, U.S.A. DOI: http://dx.doi.org/10.5067/CAMEX-4/PHOTOMETER/DATA101",
-            "issued": "2002-03-27",
-            "temporal": "2001-08-09T00:00:00Z/2001-09-26T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-04-28",
-            "keyword": [
-                "earth science",
-                "atmosphere",
-                "atmospheric chemistry"
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
-            "identifier": "C1979099896-GHRC_DAAC",
             "description": "The CAMEX-4 Dual-Beam UV-Absorption Ozone Photometer dataset was measured by using a photometer consisting of a mercury lamp, two sample chambers that could be peridically scrubbed of ozone, and two detectors that measured the 254-nm radiation transmitted through the chamber from the lamp. The ozone number density was calculated using the ozone absorption cross-section at 254nm and the Beer-Lambert Law. The one second data collection rate at the minimum detectable concentration of ozone (one sigma) was 1.5 x 1010 molecules/cm3.",
-            "title": "CAMEX-4 DUAL-BEAM UV-ABSORPTION OZONE PHOTOMETER V1",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FCAMEX-4%2FPHOTOMETER%2FDATA101",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FCAMEX-4%2FPHOTOMETER%2FDATA101",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=c4eo3p",
-                    "description": "Files may be downloaded directly to your workstation from this link",
                     "@type": "dcat:Distribution",
+                    "description": "Files may be downloaded directly to your workstation from this link",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=c4eo3p",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://ghrc.nsstc.nasa.gov/uso/ds_docs/camex4/c4eo3p/c4eo3p_dataset.html",
-                    "description": "The guide document contains detailed information about the dataset",
                     "@type": "dcat:Distribution",
+                    "description": "The guide document contains detailed information about the dataset",
+                    "downloadURL": "http://ghrc.nsstc.nasa.gov/uso/ds_docs/camex4/c4eo3p/c4eo3p_dataset.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/doc/camex4/c4eo3p/noaao3.pdf",
-                    "description": "Dual-Beam UV-Absorption Ozone Photometer",
                     "@type": "dcat:Distribution",
+                    "description": "Dual-Beam UV-Absorption Ozone Photometer",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/doc/camex4/c4eo3p/noaao3.pdf",
+                    "mediaType": "application/pdf",
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
+            "identifier": "C1979099896-GHRC_DAAC",
+            "issued": "2002-03-27",
+            "keyword": [
+                "earth science",
+                "atmosphere",
+                "atmospheric chemistry"
+            ],
+            "landingPage": "https://doi.org/10.5067/CAMEX-4/PHOTOMETER/DATA101",
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
             "spatial": "-100.0 10.0 -60.0 50.0",
+            "temporal": "2001-08-09T00:00:00Z/2001-09-26T23:59:59Z",
             "theme": [
                 "CAMEX-4",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "CAMEX-4 DUAL-BEAM UV-ABSORPTION OZONE PHOTOMETER V1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/279",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Kouwen, N., R. Soulis, W. Jenkinson, A. Graham, and T. Neff. 1998. BOREAS HYD-09 Streamflow Data . ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/279",
-            "issued": "2023-11-22",
-            "temporal": "1994-01-01T00:00:00Z/1996-12-31T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-11-27",
-            "keyword": [
-                "ecosystems",
-                "earth science",
-                "snow/ice",
-                "ground water",
-                "biosphere",
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
-            "identifier": "C2807632835-ORNL_CLOUD",
             "description": "Contains the stream gauge data that was collected by the HYD09 group.",
-            "graphic-preview-description": "Browse Image",
-            "title": "BOREAS HYD-09 Streamflow Data",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/boreas_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F279",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F279",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/boreas/HYD/h09stmgd/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/boreas/HYD/h09stmgd/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/BOREAS/guides/HYD09_STRMFLOW.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/BOREAS/guides/HYD09_STRMFLOW.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/279",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/279",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/HYD/h09stmgd/comp/h09stmgd.def",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/HYD/h09stmgd/comp/h09stmgd.def",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/msword",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/HYD/h09stmgd/comp/HYD09_STRMFLOW.doc",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/HYD/h09stmgd/comp/HYD09_STRMFLOW.doc",
+                    "mediaType": "application/msword",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/HYD/h09stmgd/comp/HYD09_STRMFLOW.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/HYD/h09stmgd/comp/HYD09_STRMFLOW.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/HYD/h09stmgd/comp/HYD09_STRMFLOW.txt",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/HYD/h09stmgd/comp/HYD09_STRMFLOW.txt",
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
+            "identifier": "C2807632835-ORNL_CLOUD",
+            "issued": "2023-11-22",
+            "keyword": [
+                "ecosystems",
+                "earth science",
+                "snow/ice",
+                "ground water",
+                "biosphere",
+                "surface water",
+                "terrestrial hydrosphere"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/279",
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
             "spatial": "-104.82 53.86 -98.38 55.92",
+            "temporal": "1994-01-01T00:00:00Z/1996-12-31T23:59:59Z",
             "theme": [
                 "BOREAS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "BOREAS HYD-09 Streamflow Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-3-ESC2-67PCHURYUMOV-M16-V3.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This CODMAC level 3 data set contains radiometric calibrated image data in W/m^2/sr/nm, acquired by the OSIRIS Wide Angle Camera on the Rosetta spacecraft during the COMET ESCORT 2 mission phase, covering the period from 2015-05-05T23:25:00.000 to 2015-06-02T23:24:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V3.0 supersedes previous deliveries of the same dataset with the following changes since the last version: Lien corrected dataset after the July and October 2018 PSA/PDS external peer reviews. Updated documentation and ancillary files, added document on bandpass filter. Updated SCIENCE_USER_GUIDE_V03.PDF to include one section about FAQ and one section about image data quality. Added shutter backtravel and readout issues to image quality map. Updated DATA_QUALITY_ID keyword in image header. Improved handling of images with missing packets. Included FITs files. Browse products changed to the same size as the original image.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-3-esc2-67pchuryumov-m16-v3.0",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2021-05-21",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "vega",
                 "67p/churyumov-gerasimenko 1 (1969 r1)",
                 "international rosetta mission"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-3-ESC2-67PCHURYUMOV-M16-V3.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-3-esc2-67pchuryumov-m16-v3.0",
-            "description": "This CODMAC level 3 data set contains radiometric calibrated image data in W/m^2/sr/nm, acquired by the OSIRIS Wide Angle Camera on the Rosetta spacecraft during the COMET ESCORT 2 mission phase, covering the period from 2015-05-05T23:25:00.000 to 2015-06-02T23:24:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V3.0 supersedes previous deliveries of the same dataset with the following changes since the last version: Lien corrected dataset after the July and October 2018 PSA/PDS external peer reviews. Updated documentation and ancillary files, added document on bandpass filter. Updated SCIENCE_USER_GUIDE_V03.PDF to include one section about FAQ and one section about image data quality. Added shutter backtravel and readout issues to image quality map. Updated DATA_QUALITY_ID keyword in image header. Improved handling of images with missing packets. Included FITs files. Browse products changed to the same size as the original image.",
-            "title": "ROSETTA-ORBITER 67P OSIWAC 3 ESC2-MTP016 RDR V3.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P OSIWAC 3 ESC2-MTP016 RDR V3.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/2328",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Loboda, T.V., J.V. Hall, D. Chen, A. Hoffman-Hall, V.S. Shevade, F. Argueta, and X. Liang. 2024. Arctic Boreal Annual Burned Area, Circumpolar Boreal Forest and Tundra, V2, 2002-2022. ORNL DAAC, Oak Ridge, Tennessee, USA. https://doi.org/10.3334/ORNLDAAC/2328",
-            "issued": "2024-03-18",
-            "temporal": "2002-01-01T00:00:00Z/2022-12-31T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-03-19",
-            "keyword": [
-                "vegetation",
-                "national geospatial data asset",
-                "human dimensions",
-                "ecosystems",
-                "ecological dynamics",
-                "earth science",
-                "biosphere",
-                "natural hazards",
-                "ngda"
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
-            "identifier": "C2902140502-ORNL_CLOUD",
             "description": "This dataset provides annual cumulative end-of-season burned area in circumpolar boreal forests and tundra for the years 2002-2022. The data were generated using the Arctic Boreal Burned Area (ABBA) version 2 algorithm with MODIS collection 6 products. The algorithm is based on Normalized Burned Ratio differencing (dNBR) and is designed specifically to capture late season fires. The annual MODIS Vegetation Continuous Fields (VCF) 250-m Collection 5.1 (MOD44B) product allowed for additional vegetation-dependent dNBR thresholds within the algorithm's processing steps. The spatial domain is circumpolar regions above 50 degrees north latitude. The data are provided in cloud-optimized GeoTIFF format with 463-m resolution.",
-            "graphic-preview-description": "The distribution of burned areas between 2002 and 2022 as mapped by ABBA V2.",
-            "title": "Arctic Boreal Annual Burned Area, Circumpolar Boreal Forest and Tundra, V2, 2002-2022",
-            "graphic-preview-file": "https://daac.ornl.gov/ABOVE/guides/Arctic_Boreal_Burned_Area_V2_Fig1.jpg",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F2328",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F2328",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/above/Arctic_Boreal_Burned_Area_V2/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/above/Arctic_Boreal_Burned_Area_V2/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/ABOVE/guides/Arctic_Boreal_Burned_Area_V2.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/ABOVE/guides/Arctic_Boreal_Burned_Area_V2.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/2328",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/2328",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/Arctic_Boreal_Burned_Area_V2/comp/Arctic_Boreal_Burned_Area_V2.pdf",
-                    "description": "Arctic Boreal Annual Burned Area, Circumpolar Boreal Forest and Tundra, V2, 2002-2022: Arctic_Boreal_Burned_Area_V2.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "Arctic Boreal Annual Burned Area, Circumpolar Boreal Forest and Tundra, V2, 2002-2022: Arctic_Boreal_Burned_Area_V2.pdf",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/Arctic_Boreal_Burned_Area_V2/comp/Arctic_Boreal_Burned_Area_V2.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://daac.ornl.gov/ABOVE/guides/Arctic_Boreal_Burned_Area_V2_Fig1.jpg",
-                    "description": "The distribution of burned areas between 2002 and 2022 as mapped by ABBA V2.",
                     "@type": "dcat:Distribution",
+                    "description": "The distribution of burned areas between 2002 and 2022 as mapped by ABBA V2.",
+                    "downloadURL": "https://daac.ornl.gov/ABOVE/guides/Arctic_Boreal_Burned_Area_V2_Fig1.jpg",
+                    "mediaType": "image/jpeg",
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
+            "graphic-preview-description": "The distribution of burned areas between 2002 and 2022 as mapped by ABBA V2.",
+            "graphic-preview-file": "https://daac.ornl.gov/ABOVE/guides/Arctic_Boreal_Burned_Area_V2_Fig1.jpg",
+            "identifier": "C2902140502-ORNL_CLOUD",
+            "issued": "2024-03-18",
+            "keyword": [
+                "vegetation",
+                "national geospatial data asset",
+                "human dimensions",
+                "ecosystems",
+                "ecological dynamics",
+                "earth science",
+                "biosphere",
+                "natural hazards",
+                "ngda"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/2328",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2024-03-19",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "ORNL_DAAC"
+            },
             "spatial": "-179.52 50.0 177.16 83.63",
+            "temporal": "2002-01-01T00:00:00Z/2022-12-31T23:59:59Z",
             "theme": [
                 "ABoVE",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Arctic Boreal Annual Burned Area, Circumpolar Boreal Forest and Tundra, V2, 2002-2022"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewBundle.jsp?identifier=urn%3Anasa%3Apds%3Aphx_ao_bundle&version=1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "The original PHX AO dataset was submitted in 2009 by Mark Lemmon",
+            "identifier": "urn:nasa:pds:phx_ao_bundle_rqpc-ccj3",
             "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "phoenix atmospheric opacity surface stereo imager ssi mars",
                 "phoenix",
                 "mars"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewBundle.jsp?identifier=urn%3Anasa%3Apds%3Aphx_ao_bundle&version=1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:phx_ao_bundle_rqpc-ccj3",
-            "description": "The original PHX AO dataset was submitted in 2009 by Mark Lemmon",
-            "title": "Phoenix AO SSI Bundle",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "Phoenix AO SSI Bundle"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1376",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Breen, A.L. 2018. Arctic Vegetation Plots, Poplars, Arctic and Interior AK and YT, Canada, 2003-2005. ORNL DAAC, Oak Ridge, Tennessee, USA. https://doi.org/10.3334/ORNLDAAC/1376",
-            "issued": "2018-12-31",
-            "temporal": "2003-06-18T00:00:00Z/2005-08-17T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-06-12",
-            "keyword": [
-                "land surface",
-                "topography",
-                "soils",
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
-            "identifier": "C2170969941-ORNL_CLOUD",
             "description": "This data set provides vegetation cover and environmental plot data collected from 32 balsam poplar (Populus balsamifera L., Salicaceae) vegetation plots located on the Arctic Slope of Alaska and in the interior boreal forests of Alaska and the Yukon from 2003 to 2005. The estimated percent land cover by species per plot are according to the older Braun-Blanquet cover-abundance scale. Plot data includes moisture, topographic position, slope, aspect, shape, and soil data.",
-            "graphic-preview-description": "Browse Image",
-            "title": "Arctic Vegetation Plots, Poplars, Arctic and Interior AK and YT, Canada, 2003-2005",
-            "graphic-preview-file": "https://daac.ornl.gov/ABOVE/guides/Poplar_Veg_Plots_Fig1.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1376",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1376",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/above/Poplar_Veg_Plots/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/above/Poplar_Veg_Plots/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/ABOVE/guides/Poplar_Veg_Plots.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/ABOVE/guides/Poplar_Veg_Plots.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1376",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1376",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
@@ -1317632,268 +1317608,270 @@
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://daac.ornl.gov/ABOVE/guides/Poplar_Veg_Plots_Fig1.png",
-                    "description": "Browse Image",
                     "@type": "dcat:Distribution",
+                    "description": "Browse Image",
+                    "downloadURL": "https://daac.ornl.gov/ABOVE/guides/Poplar_Veg_Plots_Fig1.png",
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
+            "graphic-preview-file": "https://daac.ornl.gov/ABOVE/guides/Poplar_Veg_Plots_Fig1.png",
+            "identifier": "C2170969941-ORNL_CLOUD",
+            "issued": "2018-12-31",
+            "keyword": [
+                "land surface",
+                "topography",
+                "soils",
+                "biosphere",
+                "earth science",
+                "vegetation"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1376",
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
             "spatial": "-162.74 61.08 -135.22 69.47",
+            "temporal": "2003-06-18T00:00:00Z/2005-08-17T23:59:59Z",
             "theme": [
                 "ABoVE",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Arctic Vegetation Plots, Poplars, Arctic and Interior AK and YT, Canada, 2003-2005"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/NAMMA/LASE/DATA201",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Browell, Edward V, Syed Ismail, Richard A Ferrare, Susan Kooi, Anthony Notari, Carolyn Butler, Sharon Burton and Marta Fenn.2006. NAMMA LIDAR ATMOSPHERIC SENSING EXPERIMENT (LASE) [indicate subset used]. Dataset available online from the NASA Global Hydrometeorology Resource Center DAAC, Huntsville, Alabama, U.S.A. DOI: http://dx.doi.org/10.5067/NAMMA/LASE/DATA201",
-            "issued": "2006-06-01",
-            "temporal": "2006-08-15T03:25:21Z/2006-09-12T19:07:37Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-05-19",
-            "keyword": [
-                "earth science",
-                "aerosols",
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
-            "identifier": "C1979887067-GHRC_DAAC",
             "description": "The NAMMA Lidar Atmospheric Sensing Experiment (LASE) dataset used the LASE system using the Differential Absorption Lidar (DIAL) system was operated during the NASA African Monsoon Multidisciplinary Analyses (NAMMA) campaign to gather water vapor mixing ratio and aerosol scattering ratio (815 nm) profiles. Other derived parameters include: relative humidity, equivalent potential temperature, virtual potential temperature, precipitable water vapor profiles, aerosol backscatter, aerosol extinction, and aerosol optical thickness profiles (815 nm). Aerosol data are reported as atmospheric scattering ratios on a logarithmic scale. Water vapor data are reported as mixing ratios (g/kg) on both a linear and logarithmic scale. LASE was operated from the NASA DC-8 aircraft during 14 NAMMA campaign flights between August 15 and September 12, 2006.",
-            "graphic-preview-description": "N/A",
-            "title": "NAMMA LIDAR ATMOSPHERIC SENSING EXPERIMENT (LASE) V1",
-            "graphic-preview-file": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/namma/LASE/browse/",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FNAMMA%2FLASE%2FDATA201",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FNAMMA%2FLASE%2FDATA201",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=namlase",
-                    "description": "Files may be downloaded directly to your workstation from this link",
                     "@type": "dcat:Distribution",
+                    "description": "Files may be downloaded directly to your workstation from this link",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=namlase",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "image/gif",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/namma/LASE/browse/NAMMA_LASE_20060905_ASR_ATTN_CORR_DC8_R3.gif",
-                    "description": "Sample browse image",
                     "@type": "dcat:Distribution",
+                    "description": "Sample browse image",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/namma/LASE/browse/NAMMA_LASE_20060905_ASR_ATTN_CORR_DC8_R3.gif",
+                    "mediaType": "image/gif",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "image/gif",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/namma/LASE/browse/NAMMA_LASE_20060905_H2O-LOG_R1.gif",
-                    "description": "Sample browse image",
                     "@type": "dcat:Distribution",
+                    "description": "Sample browse image",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/namma/LASE/browse/NAMMA_LASE_20060905_H2O-LOG_R1.gif",
+                    "mediaType": "image/gif",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "image/gif",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/namma/LASE/browse/NAMMA_LASE_20060905_H2O-LIN_R1.gif",
-                    "description": "Sample browse image",
                     "@type": "dcat:Distribution",
+                    "description": "Sample browse image",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/namma/LASE/browse/NAMMA_LASE_20060905_H2O-LIN_R1.gif",
+                    "mediaType": "image/gif",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://ghrc.nsstc.nasa.gov/uso/ds_docs/namma/namlase/namlase_dataset.html",
-                    "description": "The guide document contains detailed information about the dataset",
                     "@type": "dcat:Distribution",
+                    "description": "The guide document contains detailed information about the dataset",
+                    "downloadURL": "http://ghrc.nsstc.nasa.gov/uso/ds_docs/namma/namlase/namlase_dataset.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/doc/namma/namlase/Gaines_Hipskind.pdf",
-                    "description": "Format Specication for Data Exchange",
                     "@type": "dcat:Distribution",
+                    "description": "Format Specication for Data Exchange",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/doc/namma/namlase/Gaines_Hipskind.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View the primary investigator's documentation for this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/doc/namma/namlase/read_lase_gh.c",
-                    "description": "Code to demonstrate reading LASE SOLVE/AFWEX data files",
                     "@type": "dcat:Distribution",
+                    "description": "Code to demonstrate reading LASE SOLVE/AFWEX data files",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/doc/namma/namlase/read_lase_gh.c",
+                    "mediaType": "text/html",
                     "title": "View the primary investigator's documentation for this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/home/field-campaigns/namma",
-                    "description": "The home page for the project or program which sponsored the dataset",
                     "@type": "dcat:Distribution",
+                    "description": "The home page for the project or program which sponsored the dataset",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/home/field-campaigns/namma",
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
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/namma/LASE/browse/",
-                    "description": "N/A",
                     "@type": "dcat:Distribution",
+                    "description": "N/A",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/namma/LASE/browse/",
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
+            "graphic-preview-file": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/namma/LASE/browse/",
+            "identifier": "C1979887067-GHRC_DAAC",
+            "issued": "2006-06-01",
+            "keyword": [
+                "earth science",
+                "aerosols",
+                "atmospheric water vapor",
+                "atmosphere",
+                "atmospheric temperature"
+            ],
+            "landingPage": "https://doi.org/10.5067/NAMMA/LASE/DATA201",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2022-05-19",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/MSFC/GHRC"
+            },
             "spatial": "-96.5259 7.0367 -10.5579 47.8839",
+            "temporal": "2006-08-15T03:25:21Z/2006-09-12T19:07:37Z",
             "theme": [
                 "NAMMA",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "NAMMA LIDAR ATMOSPHERIC SENSING EXPERIMENT (LASE) V1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MER1-M-HAZCAM-5-REACHABILITY-OPS-V1.0",
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
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mer1-m-hazcam-5-reachability-ops-v1.0_rr2g-36mh",
+            "issued": "2021-05-21",
+            "keyword": [
+                "mars",
+                "mars exploration rover"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MER1-M-HAZCAM-5-REACHABILITY-OPS-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mer1-m-hazcam-5-reachability-ops-v1.0_rr2g-36mh",
-            "description": "NULL",
-            "title": "MER 1 MARS HAZARD AVOID CAMERA\n                                  REACHABILITY RDR OPS V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "MER 1 MARS HAZARD AVOID CAMERA\n                                  REACHABILITY RDR OPS V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=ULY-D-UDDS-5-DUST-V2.0",
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
-                "ulysses"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "Dataset Overview ================ This data set contains information on dust the dust environment in interplanetary space within the inner solar system, between Jupiter and the Sun, and at high polar latitudes of the Sun. Both interplanetary and interstellar dust particles have been detected. This information is collected with a dust impact experiment, from which may be inferred direction of motion, mass, velocity and charge (see ULYDINST.CAT). The data presented in this dataset include instrumental readouts, inferred metadata, calibration information and a calendar of events. Specifically:",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.uly-d-udds-5-dust-v2.0_rr3d-nyf8",
+            "issued": "2018-06-26",
+            "keyword": [
+                "dust",
+                "ulysses"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=ULY-D-UDDS-5-DUST-V2.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.uly-d-udds-5-dust-v2.0_rr3d-nyf8",
-            "description": "Dataset Overview ================ This data set contains information on dust the dust environment in interplanetary space within the inner solar system, between Jupiter and the Sun, and at high polar latitudes of the Sun. Both interplanetary and interstellar dust particles have been detected. This information is collected with a dust impact experiment, from which may be inferred direction of motion, mass, velocity and charge (see ULYDINST.CAT). The data presented in this dataset include instrumental readouts, inferred metadata, calibration information and a calendar of events. Specifically:",
-            "title": "ULYSSES DUST DETECTION SYSTEM V2.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "ULYSSES DUST DETECTION SYSTEM V2.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C2082387278-GES_DISC.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "OCO Science Team/Michael Gunson, AnnmarieEldering. 2021-06-10. OCO3_L2_ABand. Version 10. OCO-3 Level 2 spatially ordered geolocated retrievals screened using the A-band Preprocessor, Forward Processing V10. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://disc.gsfc.nasa.gov/datacollection/OCO3_L2_ABand_10.html. Digital Science Data.",
-            "issued": "2021-05-31",
-            "temporal": "2019-08-06T00:00:00Z/2023-03-01T00:00:00Z",
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
-            "identifier": "C2082387278-GES_DISC",
-            "description": "Version 10 is the current version of the data set. Older versions will no longer be available and are superseded by Version 10.\n\nThe Orbiting Carbon Observatory -3 (OCO-3) was deployed to the International Space Station in May, 2019. It is technically a single instrument, almost identical to OCO-2.\n\nThe Orbiting Carbon Observatory is the first NASA mission designed to collect space-based measurements of atmospheric carbon dioxide with the precision, resolution, and coverage needed to characterize the processes controlling its buildup in the atmosphere.\n\nOCO-3 incorporates three high-resolution spectrometers that make coincident measurements of reflected sunlight in the near-infrared CO2 near 1.61 and 2.06 micrometers and in molecular oxygen (O2) A-Band at 0.76 micrometers. The three spectrometers have different characteristics and are calibrated independently. \n\nOxygen-A Band cloud screening algorithm is one of the primary cloud screening tools implemented in the operational OCO processing pipeline. The algorithm was introduced and applied to early GOSAT data  with further analysis performed on OCO-2 simulations.\n\nThe OCO ABO2 algorithm employs a fast Bayesian retrieval to estimate surface pressure and surface albedo from high resolution spectra of the molecular oxygen (O2) A-band, near 0.765 \u00b5m. The radiative transfer forward model (FM) assumes a clear-sky condition, i.e. Rayleigh scattering only, such that differences between the modeled and measured radiances are apparent when the measurement scene contains cloud or aerosol.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "OCO3_L2_ABand",
             "creator": "OCO Science Team/Michael Gunson, AnnmarieEldering",
-            "title": "OCO-3 Level 2 spatially ordered geolocated retrievals screened using the A-band Preprocessor, Forward Processing V10 (OCO3_L2_ABand) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/OCO/OCO3_logo.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "data-presentation-form": "Digital Science Data",
+            "description": "Version 10 is the current version of the data set. Older versions will no longer be available and are superseded by Version 10.\n\nThe Orbiting Carbon Observatory -3 (OCO-3) was deployed to the International Space Station in May, 2019. It is technically a single instrument, almost identical to OCO-2.\n\nThe Orbiting Carbon Observatory is the first NASA mission designed to collect space-based measurements of atmospheric carbon dioxide with the precision, resolution, and coverage needed to characterize the processes controlling its buildup in the atmosphere.\n\nOCO-3 incorporates three high-resolution spectrometers that make coincident measurements of reflected sunlight in the near-infrared CO2 near 1.61 and 2.06 micrometers and in molecular oxygen (O2) A-Band at 0.76 micrometers. The three spectrometers have different characteristics and are calibrated independently. \n\nOxygen-A Band cloud screening algorithm is one of the primary cloud screening tools implemented in the operational OCO processing pipeline. The algorithm was introduced and applied to early GOSAT data  with further analysis performed on OCO-2 simulations.\n\nThe OCO ABO2 algorithm employs a fast Bayesian retrieval to estimate surface pressure and surface albedo from high resolution spectra of the molecular oxygen (O2) A-band, near 0.765 \u00b5m. The radiative transfer forward model (FM) assumes a clear-sky condition, i.e. Rayleigh scattering only, such that differences between the modeled and measured radiances are apparent when the measurement scene contains cloud or aerosol.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -1317902,66 +1317880,66 @@
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/OCO3_L2_ABand_10.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/OCO3_L2_ABand_10.html",
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
-                    "downloadURL": "https://oco2.gesdisc.eosdis.nasa.gov/data/OCO3_DATA/OCO3_L2_ABand.10/",
-                    "description": "Access the data via HTTP",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTP",
+                    "downloadURL": "https://oco2.gesdisc.eosdis.nasa.gov/data/OCO3_DATA/OCO3_L2_ABand.10/",
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
-                    "downloadURL": "https://oco2.gesdisc.eosdis.nasa.gov/opendap/OCO3_L2_ABand.10/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://oco2.gesdisc.eosdis.nasa.gov/opendap/OCO3_L2_ABand.10/contents.html",
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
@@ -1317971,176 +1317949,212 @@
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
+            "identifier": "C2082387278-GES_DISC",
+            "issued": "2021-05-31",
+            "keyword": [
+                "atmosphere",
+                "earth science",
+                "atmospheric chemistry"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C2082387278-GES_DISC.html",
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
+            "temporal": "2019-08-06T00:00:00Z/2023-03-01T00:00:00Z",
             "theme": [
                 "OCO-3",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "OCO-3 Level 2 spatially ordered geolocated retrievals screened using the A-band Preprocessor, Forward Processing V10 (OCO3_L2_ABand) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/MODIS/MCD43D27.061",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Crystal Schaaf, Zhuosen Wang. 2021-02-22. MODIS/Terra+Aqua BRDF/Albedo Parameter3 NIR Daily L3 Global 30ArcSec CMG V061. Sioux Falls, South Dakota, USA. Archived by National Aeronautics and Space Administration, U.S. Government, NASA EOSDIS Land Processes Distributed Active Archive Center. https://doi.org/10.5067/MODIS/MCD43D27.061. https://doi.org/10.5067/MODIS/MCD43D27.061. The DOI landing page provides citations in APA and Chicago styles..",
-            "issued": "2021-02-22",
-            "temporal": "2000-02-16T00:00:00Z/2024-05-20T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2021-02-22",
-            "keyword": [
-                "national geospatial data asset",
-                "earth science",
-                "land surface",
-                "ngda",
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
-            "identifier": "C2540268577-LPCLOUD",
-            "description": "The MCD43D27 Version 6.1 Bidirectional Reflectance Distribution Function and Albedo (BRDF/Albedo) Model Parameter dataset is produced daily using 16 days of Terra and Aqua Moderate Resolution Imaging Spectroradiometer (MODIS) data at 30 arc second (1,000 meter) resolution. Data are temporally weighted to the ninth day which is reflected in the Julian date in the file name. This Climate Modeling Grid (CMG) product covers the entire globe for use in climate simulation models. Due to the large file size, each MCD43D product contains just one data layer. Each of the three model parameters (isotropic, volumetric, and geometric) for each of the MODIS bands 1 through 7 and the visible, near infrared (NIR), and shortwave bands included in MCD43C1 (https://doi.org/10.5067/MODIS/MCD43C1.061) are stored in a separate file as MCD43D01 through MCD43D30. \r\n\r\nMCD43D27 is the BRDF geometric parameter for the MODIS NIR broadband. The geometric parameter, in conjunction with the isotropic and volumetric parameters, is used to derive the BRDF/Albedo values for the MODIS NIR broadband. \r\n\r\nImprovements/Changes from Previous Versions\r\n\r\n* The Version 6.1 Level-1B (L1B) products have been improved by undergoing various calibration changes that include: changes to the response-versus-scan angle (RVS) approach that affects reflectance bands for Aqua and Terra MODIS, corrections to adjust for the optical crosstalk in Terra MODIS infrared (IR) bands, and corrections to the Terra MODIS forward look-up table (LUT) update for the period 2012 - 2017.\r\n* A polarization correction has been applied to the L1B Reflective Solar Bands (RSB).",
-            "release-place": "Sioux Falls, South Dakota, USA",
             "creator": "Crystal Schaaf, Zhuosen Wang",
-            "title": "MODIS/Terra+Aqua BRDF/Albedo Parameter3 NIR Daily L3 Global 30ArcSec CMG V061",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The MCD43D27 Version 6.1 Bidirectional Reflectance Distribution Function and Albedo (BRDF/Albedo) Model Parameter dataset is produced daily using 16 days of Terra and Aqua Moderate Resolution Imaging Spectroradiometer (MODIS) data at 30 arc second (1,000 meter) resolution. Data are temporally weighted to the ninth day which is reflected in the Julian date in the file name. This Climate Modeling Grid (CMG) product covers the entire globe for use in climate simulation models. Due to the large file size, each MCD43D product contains just one data layer. Each of the three model parameters (isotropic, volumetric, and geometric) for each of the MODIS bands 1 through 7 and the visible, near infrared (NIR), and shortwave bands included in MCD43C1 (https://doi.org/10.5067/MODIS/MCD43C1.061) are stored in a separate file as MCD43D01 through MCD43D30. \r\n\r\nMCD43D27 is the BRDF geometric parameter for the MODIS NIR broadband. The geometric parameter, in conjunction with the isotropic and volumetric parameters, is used to derive the BRDF/Albedo values for the MODIS NIR broadband. \r\n\r\nImprovements/Changes from Previous Versions\r\n\r\n* The Version 6.1 Level-1B (L1B) products have been improved by undergoing various calibration changes that include: changes to the response-versus-scan angle (RVS) approach that affects reflectance bands for Aqua and Terra MODIS, corrections to adjust for the optical crosstalk in Terra MODIS infrared (IR) bands, and corrections to the Terra MODIS forward look-up table (LUT) update for the period 2012 - 2017.\r\n* A polarization correction has been applied to the L1B Reflective Solar Bands (RSB).",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMODIS%2FMCD43D27.061",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMODIS%2FMCD43D27.061",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "application/x-hdf",
-                    "downloadURL": "https://e4ftl01.cr.usgs.gov/MOTA/MCD43D27.061/",
-                    "description": "LP DAAC Data Pool provides direct access to available products via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "LP DAAC Data Pool provides direct access to available products via HTTPS.",
+                    "downloadURL": "https://e4ftl01.cr.usgs.gov/MOTA/MCD43D27.061/",
+                    "mediaType": "application/x-hdf",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "application/x-hdf",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=C2540268577-LPCLOUD",
-                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=C2540268577-LPCLOUD",
+                    "mediaType": "application/x-hdf",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/MODIS/MCD43D27.061",
-                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
+                    "downloadURL": "https://doi.org/10.5067/MODIS/MCD43D27.061",
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
-                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/filespec/MODIS/61/MCD43D27",
-                    "description": "The File Specification provides a description of the product file including Scientific Data Sets and their attributes.",
                     "@type": "dcat:Distribution",
+                    "description": "The File Specification provides a description of the product file including Scientific Data Sets and their attributes.",
+                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/filespec/MODIS/61/MCD43D27",
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
-                    "downloadURL": "https://opendap.cr.usgs.gov/opendap/hyrax/DP137/MOTA/MCD43D27.061/contents.html",
-                    "description": "Access data via Open-source Project for a Network Data Access Protocol",
                     "@type": "dcat:Distribution",
+                    "description": "Access data via Open-source Project for a Network Data Access Protocol",
+                    "downloadURL": "https://opendap.cr.usgs.gov/opendap/hyrax/DP137/MOTA/MCD43D27.061/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 }
             ],
+            "identifier": "C2540268577-LPCLOUD",
+            "issued": "2021-02-22",
+            "keyword": [
+                "national geospatial data asset",
+                "earth science",
+                "land surface",
+                "ngda",
+                "surface radiative properties"
+            ],
+            "landingPage": "https://doi.org/10.5067/MODIS/MCD43D27.061",
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
+            "title": "MODIS/Terra+Aqua BRDF/Albedo Parameter3 NIR Daily L3 Global 30ArcSec CMG V061"
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
+            "description": "NASA Financial Budget Documents, Strategic Plans and Performance Reports for fiscal year 2006.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "FY06 NASA Document",
+                    "downloadURL": "http://www.nasa.gov/pdf/107486main_FY06_high.pdf",
+                    "mediaType": "application/pdf",
+                    "title": "FY06 NASA Document"
+                }
+            ],
+            "identifier": "OCIO-Fitara-86",
             "issued": "2005-05-01",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
             "keyword": [
                 "strategic",
                 "plan",
@@ -1318149,130 +1318163,118 @@
                 "finance",
                 "performance"
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
-            "identifier": "OCIO-Fitara-86",
-            "description": "NASA Financial Budget Documents, Strategic Plans and Performance Reports for fiscal year 2006.",
-            "title": "NASA Financial Budget Documents, Strategic Plans and Performance Reports 2006",
-            "programCode": [
-                "026:046"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "http://www.nasa.gov/pdf/107486main_FY06_high.pdf",
-                    "description": "FY06 NASA Document",
-                    "@type": "dcat:Distribution",
-                    "title": "FY06 NASA Document"
-                }
-            ],
-            "accrualPeriodicity": "R/P1Y",
             "theme": [
                 "Management/Operations"
-            ]
+            ],
+            "title": "NASA Financial Budget Documents, Strategic Plans and Performance Reports 2006"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/IKBWW4RYHF1Q",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "MEaSUREs Antarctic Grounding Line from Differential Satellite Radar Interferometry V002. Version 2. Archived by National Aeronautics and Space Administration, U.S. Government, NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/IKBWW4RYHF1Q.",
-            "issued": "1992-02-07",
-            "temporal": "1992-02-07T00:00:00Z/2014-12-17T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2014-12-17",
-            "keyword": [
-                "glaciers/ice sheets",
-                "earth science",
-                "cryosphere"
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
-            "identifier": "C1573480652-NSIDC_ECS",
             "description": "This data set, part of the NASA Making Earth System Data Records for Use in Research Environments (MEaSUREs) program, provides 22 years of comprehensive high-resolution mapping of grounding lines in Antarctica from 1992 to 2014. The data were derived using differential satellite synthetic aperture radar interferometry (DInSAR) measurements from the following platforms: Earth Remote Sensing Satellites 1 and 2 (ERS-1 and ERS-2), RADARSAT-1, RADARSAT-2, the Advanced Land Observing System Phased Array type L-band Synthetic Aperture Radar (ALOS PALSAR), Cosmo Skymed, and Copernicus Sentinel-1.\n\nSee <a href=\"https://nsidc.org/data/measures/aiv\">Antarctic Ice Sheet Velocity and Mapping Data</a> for related data.",
-            "title": "MEaSUREs Antarctic Grounding Line from Differential Satellite Radar Interferometry V002",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FIKBWW4RYHF1Q",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FIKBWW4RYHF1Q",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/MEASURES/NSIDC-0498.002/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/MEASURES/NSIDC-0498.002/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1573480652-NSIDC_ECS&q=nsidc-0498&m=-67.1%21-95.78%210%212%210%210%2C2&tl=1576701501%214%21%21",
-                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1573480652-NSIDC_ECS&q=nsidc-0498&m=-67.1%21-95.78%210%212%210%210%2C2&tl=1576701501%214%21%21",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/data/data-access-tool/NSIDC-0498/versions/2/",
-                    "description": "Data Access link for ITSD project",
                     "@type": "dcat:Distribution",
+                    "description": "Data Access link for ITSD project",
+                    "downloadURL": "https://nsidc.org/data/data-access-tool/NSIDC-0498/versions/2/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/IKBWW4RYHF1Q",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/IKBWW4RYHF1Q",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/IKBWW4RYHF1Q",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/IKBWW4RYHF1Q",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C1573480652-NSIDC_ECS",
+            "issued": "1992-02-07",
+            "keyword": [
+                "glaciers/ice sheets",
+                "earth science",
+                "cryosphere"
+            ],
+            "landingPage": "https://doi.org/10.5067/IKBWW4RYHF1Q",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2014-12-17",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA NSIDC DAAC"
+            },
             "spatial": "-180.0 -90.0 180.0 -60.0",
+            "temporal": "1992-02-07T00:00:00Z/2014-12-17T23:59:59.999Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "MEaSUREs Antarctic Grounding Line from Differential Satellite Radar Interferometry V002"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-4-PRL-67PCHURYUMOV-M04-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This CODMAC level 4 data set contains radiometric calibrated and geometric distortion corrected (resampled) image data in W/m^2/sr/nm acquired by the OSIRIS Wide Angle Camera during the PRELANDING phase of the Rosetta mission, covering the period from 2014-06-04T10:50:00.000 to 2014-07-02T08:34:59.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-4-prl-67pchuryumov-m04-v1.0",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2021-05-21",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "beta car",
                 "beta cen",
@@ -1318283,389 +1318285,399 @@
                 "canopus",
                 "achernar"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-4-PRL-67PCHURYUMOV-M04-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-4-prl-67pchuryumov-m04-v1.0",
-            "description": "This CODMAC level 4 data set contains radiometric calibrated and geometric distortion corrected (resampled) image data in W/m^2/sr/nm acquired by the OSIRIS Wide Angle Camera during the PRELANDING phase of the Rosetta mission, covering the period from 2014-06-04T10:50:00.000 to 2014-07-02T08:34:59.000.",
-            "title": "ROSETTA-ORBITER 67P OSIWAC 4 PRL-MTP004 RDR V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P OSIWAC 4 PRL-MTP004 RDR V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/WM2A4FX7L9OC",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "SMEX04 Regional Soil Moisture Data: Arizona, Version 1. Version 1. Archived by National Aeronautics and Space Administration, U.S. Government, NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/WM2A4FX7L9OC.",
-            "issued": "2004-08-03",
-            "temporal": "2004-08-03T00:00:00Z/2004-08-26T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2004-08-26",
-            "keyword": [
-                "atmosphere",
-                "agriculture",
-                "land surface",
-                "earth science",
-                "surface thermal properties",
-                "precipitation",
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
-            "identifier": "C1386205072-NSIDCV0",
             "description": "Notice to Data Users: The documentation for this data set was provided solely by the Principal Investigator(s) and was not further developed, thoroughly reviewed, or edited by NSIDC. Thus, support for this data set may be limited.\n\nThis data set combines data for several parameters measured as part of the Soil Moisture Experiment 2004 (SMEX04) in the regional study area of Arizona, USA.",
-            "title": "SMEX04 Regional Soil Moisture Data: Arizona, Version 1",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FWM2A4FX7L9OC",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FWM2A4FX7L9OC",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/AVDM/data/soil_moisture/SMEX04/Arizona/ground_soil_moisture/watershed_GSM/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/AVDM/data/soil_moisture/SMEX04/Arizona/ground_soil_moisture/watershed_GSM/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/AVDM/data/soil_moisture/SMEX04/Arizona/ground_soil_moisture/watershed_GSM/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/AVDM/data/soil_moisture/SMEX04/Arizona/ground_soil_moisture/watershed_GSM/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/WM2A4FX7L9OC",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/WM2A4FX7L9OC",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/WM2A4FX7L9OC",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/WM2A4FX7L9OC",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C1386205072-NSIDCV0",
+            "issued": "2004-08-03",
+            "keyword": [
+                "atmosphere",
+                "agriculture",
+                "land surface",
+                "earth science",
+                "surface thermal properties",
+                "precipitation",
+                "soils"
+            ],
+            "landingPage": "https://doi.org/10.5067/WM2A4FX7L9OC",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2004-08-26",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA NSIDC DAAC"
+            },
             "spatial": "-110.3 31.4 -109.7 32.1",
+            "temporal": "2004-08-03T00:00:00Z/2004-08-26T23:59:59.999Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "SMEX04 Regional Soil Moisture Data: Arizona, Version 1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-COMPIL-3-TNO-CEN-COLOR-V6.0",
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
+            "description": "This data set is intended to include published broadband colors of centaurs and Transneptunian Objects (TNOs) published through April 2009. It supersedes all versions of the TNO colors data set EAR-A-3-RDR-TNO-PHOT.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-compil-3-tno-cen-color-v6.0_rri7-hqk8",
+            "issued": "2018-06-26",
+            "keyword": [
+                "support archives",
+                "asteroid"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-COMPIL-3-TNO-CEN-COLOR-V6.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-compil-3-tno-cen-color-v6.0_rri7-hqk8",
-            "description": "This data set is intended to include published broadband colors of centaurs and Transneptunian Objects (TNOs) published through April 2009. It supersedes all versions of the TNO colors data set EAR-A-3-RDR-TNO-PHOT.",
-            "title": "TNO AND CENTAUR COLORS V6.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "TNO AND CENTAUR COLORS V6.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/TERRA/MISR/MISBR_L1.005",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "The data used in this study were produced by the MISR Science Team;processed/stored at the Langley DAAC;Product is the MISR Level 1B2 ellipsoid-projected Browse parameters;See ProductionDateTime for published date.",
-            "issued": "2003-03-24",
-            "temporal": "1999-12-18T00:00:00Z/2022-01-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2017-02-22",
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
-            "identifier": "C43677744-LARC",
             "description": "This is the browse data associated with a particular granule.",
-            "title": "MISR Browse data V005",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FTERRA%2FMISR%2FMISBR_L1.005",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FTERRA%2FMISR%2FMISBR_L1.005",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 }
             ],
-            "theme": [
-                "geospatial"
+            "identifier": "C43677744-LARC",
+            "issued": "2003-03-24",
+            "keyword": [
+                "nasa"
             ],
+            "landingPage": "https://doi.org/10.5067/TERRA/MISR/MISBR_L1.005",
             "language": [
                 "en-US"
-            ]
+            ],
+            "modified": "2017-02-22",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "LaRC"
+            },
+            "temporal": "1999-12-18T00:00:00Z/2022-01-17T00:00:00Z",
+            "theme": [
+                "geospatial"
+            ],
+            "title": "MISR Browse data V005"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MER1-M-HAZCAM-5-DISPARITY-OPS-V1.0",
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
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mer1-m-hazcam-5-disparity-ops-v1.0_rrmd-kuz4",
+            "issued": "2021-05-21",
+            "keyword": [
+                "mars exploration rover",
+                "mars"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MER1-M-HAZCAM-5-DISPARITY-OPS-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mer1-m-hazcam-5-disparity-ops-v1.0_rrmd-kuz4",
-            "description": "NULL",
-            "title": "MER 1 MARS HAZARD AVOID CAMERA\n                                     DISPARITY RDR OPS V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "MER 1 MARS HAZARD AVOID CAMERA\n                                     DISPARITY RDR OPS V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=PVO-V-ONMS-4-IONMAXCOUNTRATE-12SEC-V1.0",
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
-                "pioneer venus"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This data set contains PVO Neutral Mass Spectrometer superthermal ion data. Each record contains the maximum count rate per second in a 12 second period beginning with the time of the first data point for a given mass number.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.pvo-v-onms-4-ionmaxcountrate-12sec-v1.0_rrmn-5ead",
+            "issued": "2018-06-26",
+            "keyword": [
+                "venus",
+                "pioneer venus"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=PVO-V-ONMS-4-IONMAXCOUNTRATE-12SEC-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.pvo-v-onms-4-ionmaxcountrate-12sec-v1.0_rrmn-5ead",
-            "description": "This data set contains PVO Neutral Mass Spectrometer superthermal ion data. Each record contains the maximum count rate per second in a 12 second period beginning with the time of the first data point for a given mass number.",
-            "title": "PVO VENUS ONMS BROWSE SUPRTHRML ION MAX COUNT RATE 12S V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "PVO VENUS ONMS BROWSE SUPRTHRML ION MAX COUNT RATE 12S V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.7927/H4RV0KMH",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Intergovernmental Panel on Climate Change - IPCC. 2000-07-31. IPCC Special Report on Emissions Scenarios (SRES) 1x1 Degree Gridded Emissions Dataset. Version 1.00. New York, NY. Archived by National Aeronautics and Space Administration, U.S. Government, Cambridge University Press. https://doi.org/10.7927/H4RV0KMH. https://doi.org/10.7927/H4RV0KMH.",
-            "issued": "2000-07-31",
-            "temporal": "1990-01-01T00:00:00Z/2100-12-31T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2000-07-31",
-            "references": [
-                "https://doi.org/10.7927/H4N29TWJ",
-                "https://doi.org/10.7927/H4HD7SKJ",
-                "https://doi.org/10.7927/H41C1TT4",
-                "https://doi.org/10.7927/H4WM1BB7",
-                "https://doi.org/10.7927/H4XG9P2R",
-                "https://doi.org/10.7927/H4542KJV",
-                "https://doi.org/10.7927/H4FT8J0X"
-            ],
-            "keyword": [
-                "air quality",
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
-            "identifier": "C179001931-SEDAC",
-            "description": "The Intergovernmental Panel on Climate Change (IPCC) Special Report on Emissions Scenarios (SRES) 1x1 Degree Gridded Emissions Dataset consists of global gridded emissions for greenhouse gases (GHGs) projected every 10 years beginning in 1990 through 2100. The grids are produced for reactive gases Methane (CH4), Carbon Monoxide (CO), Nitrogen Oxides (NOx), and Non-Methane Volatile Organic Compounds (NMVOC), along with Sulfur Dioxide (SO2), based on the IPCC SRES Emissions Scenarios Data Set Version 1.1. This data set is produced by the IPCC and is distributed by the Columbia University Center for International Earth Science Information Network (CIESIN).",
-            "release-place": "New York, NY",
-            "graphic-preview-description": "Sample browse graphic of the data set.",
             "creator": "Intergovernmental Panel on Climate Change - IPCC",
-            "title": "IPCC Special Report on Emissions Scenarios (SRES) 1x1 Degree Gridded Emissions Dataset",
-            "graphic-preview-file": "https://sedac.ciesin.columbia.edu/downloads/maps/ipcc/ipcc-gridded-emissions/sedac-logo.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The Intergovernmental Panel on Climate Change (IPCC) Special Report on Emissions Scenarios (SRES) 1x1 Degree Gridded Emissions Dataset consists of global gridded emissions for greenhouse gases (GHGs) projected every 10 years beginning in 1990 through 2100. The grids are produced for reactive gases Methane (CH4), Carbon Monoxide (CO), Nitrogen Oxides (NOx), and Non-Methane Volatile Organic Compounds (NMVOC), along with Sulfur Dioxide (SO2), based on the IPCC SRES Emissions Scenarios Data Set Version 1.1. This data set is produced by the IPCC and is distributed by the Columbia University Center for International Earth Science Information Network (CIESIN).",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.7927%2FH4RV0KMH",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.7927%2FH4RV0KMH",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/downloads/maps/ipcc/ipcc-gridded-emissions/sedac-logo.jpg",
-                    "description": "Sample browse graphic of the data set.",
                     "@type": "dcat:Distribution",
+                    "description": "Sample browse graphic of the data set.",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/downloads/maps/ipcc/ipcc-gridded-emissions/sedac-logo.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/ipcc-gridded-emissions/data-download",
-                    "description": "Data Download Page",
                     "@type": "dcat:Distribution",
+                    "description": "Data Download Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/ipcc-gridded-emissions/data-download",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/ipcc-gridded-emissions",
-                    "description": "Data Set\u00a0Overview Page",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set\u00a0Overview Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/ipcc-gridded-emissions",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "graphic-preview-description": "Sample browse graphic of the data set.",
+            "graphic-preview-file": "https://sedac.ciesin.columbia.edu/downloads/maps/ipcc/ipcc-gridded-emissions/sedac-logo.jpg",
+            "identifier": "C179001931-SEDAC",
+            "issued": "2000-07-31",
+            "keyword": [
+                "air quality",
+                "earth science",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.7927/H4RV0KMH",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2000-07-31",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "SEDAC"
+            },
+            "references": [
+                "https://doi.org/10.7927/H4N29TWJ",
+                "https://doi.org/10.7927/H4HD7SKJ",
+                "https://doi.org/10.7927/H41C1TT4",
+                "https://doi.org/10.7927/H4WM1BB7",
+                "https://doi.org/10.7927/H4XG9P2R",
+                "https://doi.org/10.7927/H4542KJV",
+                "https://doi.org/10.7927/H4FT8J0X"
+            ],
+            "release-place": "New York, NY",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "1990-01-01T00:00:00Z/2100-12-31T00:00:00Z",
             "theme": [
                 "IPCC",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "IPCC Special Report on Emissions Scenarios (SRES) 1x1 Degree Gridded Emissions Dataset"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=GO-J-UVS-2-EDR-JUPITER-V1.0",
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
+            "description": "TBD",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.go-j-uvs-2-edr-jupiter-v1.0_rrmw-6e7y",
+            "issued": "2021-05-21",
+            "keyword": [
+                "galileo"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=GO-J-UVS-2-EDR-JUPITER-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.go-j-uvs-2-edr-jupiter-v1.0_rrmw-6e7y",
-            "description": "TBD",
-            "title": "GALILEO ORBITER UVS JUPITER OPERATIONS EDR DATA",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "GALILEO ORBITER UVS JUPITER OPERATIONS EDR DATA"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://c3.ndc.nasa.gov/dashlink/algorithm/sequenceminer-algorithm/",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Dennis Koga",
+                "hasEmail": "mailto:dennis.koga@nasa.gov"
+            },
+            "description": "The sequenceMiner was developed to address the problem of detecting and describing anomalies in large sets of high-dimensional symbol sequences. sequenceMiner works by performing unsupervised clustering (grouping) of sequences using the normalized longest common subsequence (LCS) as a similarity measure, followed by a detailed analysis of outliers to detect anomalies. sequenceMiner utilizes a new hybrid algorithm for computing the LCS that has been shown to outperform existing algorithms by a factor of five. sequenceMiner also includes new algorithms for outlier analysis that provide comprehensible indicators as to why a particular sequence was deemed to be an outlier. This provides analysts with a coherent description of the anomalies identified in the sequence, and why they differ from more 'normal' sequences.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://ti.arc.nasa.gov/m/opensource/downloads/SequenceMiner.tar.gz",
+                    "mediaType": "application/x-tar"
+                }
+            ],
+            "identifier": "OCIO-Fitara-137",
             "issued": "2015-01-07",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
             "keyword": [
                 "algorithm",
                 "detection",
@@ -1318675,65 +1318687,33 @@
                 "outlier",
                 "cluster"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Dennis Koga",
-                "hasEmail": "mailto:dennis.koga@nasa.gov"
-            },
+            "landingPage": "https://c3.ndc.nasa.gov/dashlink/algorithm/sequenceminer-algorithm/",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:046"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Ames Research Center"
             },
-            "identifier": "OCIO-Fitara-137",
-            "description": "The sequenceMiner was developed to address the problem of detecting and describing anomalies in large sets of high-dimensional symbol sequences. sequenceMiner works by performing unsupervised clustering (grouping) of sequences using the normalized longest common subsequence (LCS) as a similarity measure, followed by a detailed analysis of outliers to detect anomalies. sequenceMiner utilizes a new hybrid algorithm for computing the LCS that has been shown to outperform existing algorithms by a factor of five. sequenceMiner also includes new algorithms for outlier analysis that provide comprehensible indicators as to why a particular sequence was deemed to be an outlier. This provides analysts with a coherent description of the anomalies identified in the sequence, and why they differ from more 'normal' sequences.",
-            "title": "ARC Code TI: sequenceMiner",
-            "programCode": [
-                "026:046"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://ti.arc.nasa.gov/m/opensource/downloads/SequenceMiner.tar.gz",
-                    "mediaType": "application/x-tar"
-                }
-            ],
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Management/Operations"
-            ]
+            ],
+            "title": "ARC Code TI: sequenceMiner"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://turbmodels.larc.nasa.gov/ke-rt.html",
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
-                "k-e-rt",
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
-            "identifier": "NASA-838",
             "description": "This web page gives detailed information on the equations for various forms of the K-e-Rt turbulence model.",
-            "title": "K-e-Rt Turbulence Model",
-            "programCode": [
-                "026:023"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -1318741,58 +1318721,103 @@
                     "mediaType": "application/html"
                 }
             ],
-            "accrualPeriodicity": "irregular",
+            "identifier": "NASA-838",
+            "issued": "2018-06-25",
+            "keyword": [
+                "k-e-rt",
+                "turbulence",
+                "models"
+            ],
+            "landingPage": "http://turbmodels.larc.nasa.gov/ke-rt.html",
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
+            "title": "K-e-Rt Turbulence Model"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewBundle.jsp?identifier=urn%3Anasa%3Apds%3Ainsight_edl&version=1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This PDS4 bundle contains the InSight EDL atmospheric reconstruction",
+            "identifier": "urn:nasa:pds:insight_edl",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2021-05-21",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "insight",
                 "mars",
                 "atmospheric reconstruction"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewBundle.jsp?identifier=urn%3Anasa%3Apds%3Ainsight_edl&version=1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:insight_edl",
-            "description": "This PDS4 bundle contains the InSight EDL atmospheric reconstruction",
-            "title": "InSight EDL Bundle",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "InSight EDL Bundle"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "http://techport.nasa.gov/view/230",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Paul Hertz",
+                "hasEmail": "mailto:paul.hertz@nasa.gov"
+            },
+            "description": "&lt;p&gt;\r\n\tStrategic Technology Development&lt;/p&gt;",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://techport.nasa.gov/xml-api/230",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "identifier": "TECHPORT_230",
             "issued": "2018-06-25",
-            "@type": "dcat:Dataset",
+            "keyword": [
+                "nasa headquarters",
+                "program",
+                "active"
+            ],
+            "landingPage": "http://techport.nasa.gov/view/230",
             "modified": "2020-01-29",
+            "programCode": [
+                "026:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Science Mission Directorate"
+            },
             "references": [
                 "http://techport.nasa.gov/home",
                 "http://techport.nasa.gov/doc/home/TechPort_Advanced_Search.pdf",
@@ -1318803,91 +1318828,68 @@
                 "http://techport.nasa.gov/fetchFile?objectId=6560",
                 "http://techport.nasa.gov/fetchFile?objectId=3448"
             ],
-            "keyword": [
-                "nasa headquarters",
-                "program",
-                "active"
+            "title": "Strategic Astrophysics Technology Program"
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
-                "fn": "Paul Hertz",
-                "hasEmail": "mailto:paul.hertz@nasa.gov"
-            },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Science Mission Directorate"
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
-            "identifier": "TECHPORT_230",
-            "description": "&lt;p&gt;\r\n\tStrategic Technology Development&lt;/p&gt;",
-            "title": "Strategic Astrophysics Technology Program",
-            "programCode": [
-                "026:000"
-            ],
+            "description": "LGRS, RSS, SPICE",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "downloadURL": "http://techport.nasa.gov/xml-api/230",
-                    "mediaType": "application/xml"
+                    "downloadURL": "https://pds.jpl.nasa.gov/tools/subscription_service/SS-20130612.shtml",
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
+            "identifier": "NASA-478",
             "issued": "2018-06-25",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
-            "references": [
-                "https://pds.jpl.nasa.gov/"
-            ],
             "keyword": [
                 "rss",
                 "pds",
                 "lgrs",
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
-            "identifier": "NASA-478",
-            "description": "LGRS, RSS, SPICE",
-            "title": "PDS GRAIL (Gravity Recovery and Interior Laboratory) Release 2",
-            "programCode": [
-                "026:005"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://pds.jpl.nasa.gov/tools/subscription_service/SS-20130612.shtml",
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
+            "title": "PDS GRAIL (Gravity Recovery and Interior Laboratory) Release 2"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-4-ESC3-67PCHURYUMOV-M18-V2.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This CODMAC level 4 data set contains radiometric calibrated and geometric distortion corrected (resampled) image data in W/m^2/sr/nm, acquired by the OSIRIS Wide Angle Camera on the Rosetta spacecraft during the COMET ESCORT 3 mission phase, covering the period from 2015-06-30T23:25:00.000 to 2015-07-28T23:24:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V2.0 supersedes previous deliveries of the same dataset with the following changes since the last version: Lien corrected dataset after October 2018 PSA/PDS external peer review. Updated documentation and ancillary files, added document on bandpass filter. Updated SCIENCE_USER_GUIDE_V03.PDF to include one section about FAQ and one section about image data quality. Added shutter backtravel and readout issues to image quality map. Updated DATA_QUALITY_ID keyword in image header. Improved handling of images with missing packets.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-4-esc3-67pchuryumov-m18-v2.0",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2021-05-21",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "67p/churyumov-gerasimenko 1 (1969 r1)",
                 "international rosetta mission",
@@ -1318895,76 +1318897,76 @@
                 "vega",
                 "pluto"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-4-ESC3-67PCHURYUMOV-M18-V2.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-4-esc3-67pchuryumov-m18-v2.0",
-            "description": "This CODMAC level 4 data set contains radiometric calibrated and geometric distortion corrected (resampled) image data in W/m^2/sr/nm, acquired by the OSIRIS Wide Angle Camera on the Rosetta spacecraft during the COMET ESCORT 3 mission phase, covering the period from 2015-06-30T23:25:00.000 to 2015-07-28T23:24:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V2.0 supersedes previous deliveries of the same dataset with the following changes since the last version: Lien corrected dataset after October 2018 PSA/PDS external peer review. Updated documentation and ancillary files, added document on bandpass filter. Updated SCIENCE_USER_GUIDE_V03.PDF to include one section about FAQ and one section about image data quality. Added shutter backtravel and readout issues to image quality map. Updated DATA_QUALITY_ID keyword in image header. Improved handling of images with missing packets.",
-            "title": "ROSETTA-ORBITER 67P OSIWAC 4 ESC3-MTP018 RDR V2.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P OSIWAC 4 ESC3-MTP018 RDR V2.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NEAR-A-GRS-2-EDR-CRUISE4-V1.0",
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
+            "description": "This data set contains Gamma Ray Spectrometer (GRS) observations made during the fourth cruise phase of the NEAR mission. The individual observations are combined into a single file per day for each sensor.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.near-a-grs-2-edr-cruise4-v1.0_rryj-dg5c",
+            "issued": "2021-05-21",
+            "keyword": [
+                "solar system",
+                "near earth asteroid rendezvous"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NEAR-A-GRS-2-EDR-CRUISE4-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.near-a-grs-2-edr-cruise4-v1.0_rryj-dg5c",
-            "description": "This data set contains Gamma Ray Spectrometer (GRS) observations made during the fourth cruise phase of the NEAR mission. The individual observations are combined into a single file per day for each sensor.",
-            "title": "NEAR GRS SPECTRA FOR CRUISE 4 PHASE",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "NEAR GRS SPECTRA FOR CRUISE 4 PHASE"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-J-LEISA-2-JUPITER-V1.1",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This data set contains Raw data taken by the New Horizons Linear Etalon Imaging Spectral Array instrument during the Jupiter encounter mission phase.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-j-leisa-2-jupiter-v1.1_rrzp-f56m",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "earth",
                 "j2 europa",
@@ -1318975,750 +1318977,757 @@
                 "j rings",
                 "callisto"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-J-LEISA-2-JUPITER-V1.1",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-j-leisa-2-jupiter-v1.1_rrzp-f56m",
-            "description": "This data set contains Raw data taken by the New Horizons Linear Etalon Imaging Spectral Array instrument during the Jupiter encounter mission phase.",
-            "title": "NEW HORIZONS LEISA JUPITER ENCOUNTER V1.1",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "NEW HORIZONS LEISA JUPITER ENCOUNTER V1.1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/GNSS/GNSS_HOURLY_O_001",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "International GNSS Service, Hourly 30-second observation data, Greenbelt, MD, USA:NASA Crustal Dynamics Data Information System (CDDIS), Accessed [[enter user data access date]] at doi:10.5067/GNSS/gnss_hourly_o_001",
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
-            "identifier": "C1419754347-CDDIS",
             "description": "This dataset consists of ground-based Global Navigation Satellite System (GNSS) Observation Data (30-second sampling, hourly files) from the NASA Crustal Dynamics Data Information System (CDDIS). GNSS provide autonomous geo-spatial positioning with global coverage. GNSS data sets from ground receivers at the CDDIS consist primarily of the data from the U.S. Global Positioning System (GPS) and the Russian GLObal NAvigation Satellite System (GLONASS). Since 2011, the CDDIS GNSS archive includes data from other GNSS (Europe\u2019s Galileo, China\u2019s Beidou, Japan\u2019s Quasi-Zenith Satellite System/QZSS, the Indian Regional Navigation Satellite System/IRNSS, and worldwide Satellite Based Augmentation Systems/SBASs), which are similar to the U.S. GPS in terms of the satellite constellation, orbits, and signal structure. The hourly GNSS observation files (un-compacted) contain one hour of GPS or multi-GNSS observation (30-second sampling) data in RINEX format from a global permanent network of ground-based receivers, one file per hour per site. More information about these data is available on the CDDIS website at https://cddis.nasa.gov/Data_and_Derived_Products/GNSS/hourly_30second_data.html.",
-            "title": "Ground-Based Global Navigation Satellite System (GNSS) Observation Data (30-second sampling, hourly files) from NASA CDDIS",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGNSS%2FGNSS_HOURLY_O_001",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGNSS%2FGNSS_HOURLY_O_001",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://cddis.nasa.gov/archive/gnss/data/hourly",
-                    "description": "URL for retrieval of GNSS hourly observation data through https",
                     "@type": "dcat:Distribution",
+                    "description": "URL for retrieval of GNSS hourly observation data through https",
+                    "downloadURL": "https://cddis.nasa.gov/archive/gnss/data/hourly",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://cddis.nasa.gov/Data_and_Derived_Products/GNSS/hourly_30second_data.html",
-                    "description": "URL for more information about GNSS hourly observation data",
                     "@type": "dcat:Distribution",
+                    "description": "URL for more information about GNSS hourly observation data",
+                    "downloadURL": "https://cddis.nasa.gov/Data_and_Derived_Products/GNSS/hourly_30second_data.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/GNSS/GNSS_HOURLY_O_001",
-                    "description": "URL for more information about GNSS hourly observation data",
                     "@type": "dcat:Distribution",
+                    "description": "URL for more information about GNSS hourly observation data",
+                    "downloadURL": "https://doi.org/10.5067/GNSS/GNSS_HOURLY_O_001",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 }
             ],
+            "identifier": "C1419754347-CDDIS",
+            "issued": "1992-01-01",
+            "keyword": [
+                "earth science",
+                "solid earth",
+                "geodetics",
+                "gravity/gravitational field",
+                "tectonics"
+            ],
+            "landingPage": "https://doi.org/10.5067/GNSS/GNSS_HOURLY_O_001",
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
+            "title": "Ground-Based Global Navigation Satellite System (GNSS) Observation Data (30-second sampling, hourly files) from NASA CDDIS"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-A-SWAP-3-KEM1-V2.0",
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
-                "new horizons kuiper belt extended mission"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This data set contains Calibrated data taken by the New Horizons Solar Wind Around Pluto instrument during the KEM1 ENCOUNTER mission phase. This is VERSION 2.0 of this data set. This data set contains data acquired by the spacecraft between 08/14/2018 and 01/31/2019. It only includes data downlinked before 02/01/2019. Future datasets may include more data acquired by the spacecraft after 08/13/2018 but downlinked after 01/31/2019. The data includes SWAP observations and plasma rolls in the approach and departure of MU69. A gain test was also performed.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-a-swap-3-kem1-v2.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "new horizons kuiper belt extended mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-A-SWAP-3-KEM1-V2.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-a-swap-3-kem1-v2.0",
-            "description": "This data set contains Calibrated data taken by the New Horizons Solar Wind Around Pluto instrument during the KEM1 ENCOUNTER mission phase. This is VERSION 2.0 of this data set. This data set contains data acquired by the spacecraft between 08/14/2018 and 01/31/2019. It only includes data downlinked before 02/01/2019. Future datasets may include more data acquired by the spacecraft after 08/13/2018 but downlinked after 01/31/2019. The data includes SWAP observations and plasma rolls in the approach and departure of MU69. A gain test was also performed.",
-            "title": "NEW HORIZONS\n      SWAP KEM1\n      CALIBRATED V2.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "NEW HORIZONS\n      SWAP KEM1\n      CALIBRATED V2.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-5-DDR-TAXONOMY-V2.0",
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
+            "description": "This dataset provides taxonomic classifications of asteroids in each of four different systems: Tholen (1984, 1989) [THOLEN1984, THOLEN1989] (1989) [TEDESCOETAL1989]",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-5-ddr-taxonomy-v2.0_rs9e-f8jt",
+            "issued": "2018-06-26",
+            "keyword": [
+                "support archives",
+                "asteroid"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-5-DDR-TAXONOMY-V2.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-5-ddr-taxonomy-v2.0_rs9e-f8jt",
-            "description": "This dataset provides taxonomic classifications of asteroids in each of four different systems: Tholen (1984, 1989) [THOLEN1984, THOLEN1989] (1989) [TEDESCOETAL1989]",
-            "title": "ASTEROID TAXONOMY V2.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "ASTEROID TAXONOMY V2.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/IMPACTS/AVAPS/DATA101",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Thornhill, Kenneth L and Claire  Robinson.2022. Advanced Vertical Atmospheric Profiling System Dropsondes (AVAPS) IMPACTS [indicate subset used]. Dataset available online from the NASA Global Hydrometeorology Resource Center DAAC, Huntsville, Alabama, U.S.A. DOI: http://dx.doi.org/10.5067/IMPACTS/AVAPS/DATA101",
-            "issued": "2022-03-23",
-            "temporal": "2020-01-12T21:04:13Z/2022-02-25T18:43:40Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "keyword": [
-                "atmosphere",
-                "earth science",
-                "atmospheric winds",
-                "atmospheric water vapor",
-                "atmospheric temperature",
-                "atmospheric pressure"
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
-            "identifier": "C2004708338-GHRC_DAAC",
             "description": "The Advanced Vertical Atmospheric Profiling System (AVAPS) IMPACTS dataset consists of vertical atmospheric profile measurements collected by the Advanced Vertical Atmospheric Profiling System (AVAPS) dropsondes released from the NASA P-3 aircraft during the Investigation of Microphysics and Precipitation for Atlantic Coast-Threatening Snowstorms (IMPACTS) field campaign. IMPACTS was a three-year sequence of winter season deployments conducted to study snowstorms over the U.S Atlantic Coast (2020-2023). The campaign aimed to (1) Provide observations critical to understanding the mechanisms of snowband formation, organization, and evolution; (2) Examine how the microphysical characteristics and likely growth mechanisms of snow particles vary across snowbands; and (3) Improve snowfall remote sensing interpretation and modeling to significantly advance prediction capabilities. AVAPS uses a Global Positioning System (GPS) dropsonde to measure atmospheric state parameters (temperature, humidity, wind speed/direction, pressure) and location in 3-dimensional space during the dropsonde\u2019s descent. The AVAPS dataset files are available from January 12, 2020 through February 25, 2022 in ASCII-ict format.",
-            "title": "Advanced Vertical Atmospheric Profiling System Dropsondes (AVAPS) IMPACTS V1",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FIMPACTS%2FAVAPS%2FDATA101",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FIMPACTS%2FAVAPS%2FDATA101",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/portal/ghrc/search?q=avapsimpacts&ghrccloud%2Fdata%2F=",
-                    "description": "Files may be downloaded directly to your workstation from this link",
                     "@type": "dcat:Distribution",
+                    "description": "Files may be downloaded directly to your workstation from this link",
+                    "downloadURL": "https://search.earthdata.nasa.gov/portal/ghrc/search?q=avapsimpacts&ghrccloud%2Fdata%2F=",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.eol.ucar.edu/observing_facilities/avaps-dropsonde-system",
-                    "description": "NCAR Airborne Vertical Atmospheric Profiling System (AVAPS)",
                     "@type": "dcat:Distribution",
+                    "description": "NCAR Airborne Vertical Atmospheric Profiling System (AVAPS)",
+                    "downloadURL": "https://www.eol.ucar.edu/observing_facilities/avaps-dropsonde-system",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.eol.ucar.edu/content/what-dropsonde",
-                    "description": "What is a Dropsonde?",
                     "@type": "dcat:Distribution",
+                    "description": "What is a Dropsonde?",
+                    "downloadURL": "https://www.eol.ucar.edu/content/what-dropsonde",
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
-                    "mediaType": "text/html",
-                    "downloadURL": "https://espo.nasa.gov/impacts/content/IMPACTS",
-                    "description": "IMPACTS Field Campaign Information",
                     "@type": "dcat:Distribution",
+                    "description": "IMPACTS Field Campaign Information",
+                    "downloadURL": "https://espo.nasa.gov/impacts/content/IMPACTS",
+                    "mediaType": "text/html",
                     "title": "View information related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://www.mbw.ch/wp-content/uploads/2015/05/ITS-90_Formulations.pdf",
-                    "description": "ITS-90 Formulations for Vapor Pressure, Frostpoint Temperature, Dewpoint Temperature, and Enhancement Factors in the Range -100 to +100 C",
                     "@type": "dcat:Distribution",
+                    "description": "ITS-90 Formulations for Vapor Pressure, Frostpoint Temperature, Dewpoint Temperature, and Enhancement Factors in the Range -100 to +100 C",
+                    "downloadURL": "https://www.mbw.ch/wp-content/uploads/2015/05/ITS-90_Formulations.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View information related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/impacts/AVAPS/doc/avapsimpacts_dataset.pdf",
-                    "description": "The guide document contains detailed information about the dataset",
                     "@type": "dcat:Distribution",
+                    "description": "The guide document contains detailed information about the dataset",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/impacts/AVAPS/doc/avapsimpacts_dataset.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.1175/1520-0477(1999)080%3C0407:TNGD%3E2.0.CO;2",
-                    "description": "The NCAR GPS Dropwindsonde",
                     "@type": "dcat:Distribution",
+                    "description": "The NCAR GPS Dropwindsonde",
+                    "downloadURL": "https://doi.org/10.1175/1520-0477(1999)080%3C0407:TNGD%3E2.0.CO;2",
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
-                    "description": "IMPACTS Field Campaign Project Home Page",
                     "@type": "dcat:Distribution",
+                    "description": "IMPACTS Field Campaign Project Home Page",
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
+            "identifier": "C2004708338-GHRC_DAAC",
+            "issued": "2022-03-23",
+            "keyword": [
+                "atmosphere",
+                "earth science",
+                "atmospheric winds",
+                "atmospheric water vapor",
+                "atmospheric temperature",
+                "atmospheric pressure"
+            ],
+            "landingPage": "https://doi.org/10.5067/IMPACTS/AVAPS/DATA101",
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
             "spatial": "-77.8148 33.5415 -65.44 44.1677",
+            "temporal": "2020-01-12T21:04:13Z/2022-02-25T18:43:40Z",
             "theme": [
                 "IMPACTS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Advanced Vertical Atmospheric Profiling System Dropsondes (AVAPS) IMPACTS V1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/SeaBASS/Apero/DATA001",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/GSFC/SED/ESD/GCDC/OB.DAAC. https://doi.org/10.5067/SeaBASS/Apero/DATA001.",
-            "issued": "2023-06-04",
-            "temporal": "2022-02-01T23:59:59Z/2024-02-01T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-11",
-            "keyword": [
-                "salinity/density",
-                "earth science",
-                "ocean temperature",
-                "oceans",
-                "ocean optics",
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
-            "identifier": "C3184807056-OB_DAAC",
             "description": "The APERO project proposes a mechanistic approach to the biological carbon pump (export of surface biogenic carbon production and fate in the water column -200/2000m). APERO aims to reduce the gap between the amount of photosynthetically produced organic carbon transferred to the deep ocean and the metabolic demand for carbon in the water column. The project is built around a campaign with two oceanographic vessels in the Northeast Atlantic, at the level of the British permanent station PAP (58N, 16W). It lasted 40 days and took place in June and July of 2023, at the time of maximum particulate carbon export to the deep ocean. The three major contributions of APERO are the study of the role of small-scale dynamics (~1-10km) on the water column using autonomous platforms, imagery and innovative instrumentation, the construction of a comprehensive database based on the simultaneous multidisciplinary observation of all processes regulating the attenuation of carbon flux in the water column  and the quantification of the fluxes associated with these processes. Relying on a significant international collaboration with the JETZON consortium (https://www.jetzon.org/) and an ambitious observation strategy, complemented by molecular biology and innovative modeling approaches, this study will contribute to a significant reduction of uncertainties on carbon storage by the ocean.",
-            "title": "Assessing marine biogenic matter Production, Export and Remineralization: from the surface to the dark Ocean",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSeaBASS%2FApero%2FDATA001",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSeaBASS%2FApero%2FDATA001",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://seabass.gsfc.nasa.gov/experiment/Apero/",
-                    "description": "Detailed information about the SeaBASS Experiment such as cruises, funding, and investigators",
                     "@type": "dcat:Distribution",
+                    "description": "Detailed information about the SeaBASS Experiment such as cruises, funding, and investigators",
+                    "downloadURL": "https://seabass.gsfc.nasa.gov/experiment/Apero/",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 }
             ],
+            "identifier": "C3184807056-OB_DAAC",
+            "issued": "2023-06-04",
+            "keyword": [
+                "salinity/density",
+                "earth science",
+                "ocean temperature",
+                "oceans",
+                "ocean optics",
+                "ocean chemistry"
+            ],
+            "landingPage": "https://doi.org/10.5067/SeaBASS/Apero/DATA001",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2023-07-11",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GCDC/OB.DAAC"
+            },
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2022-02-01T23:59:59Z/2024-02-01T23:59:59Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Assessing marine biogenic matter Production, Export and Remineralization: from the surface to the dark Ocean"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/NAMMA/MODIS/DATA201",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Warner, Jeremy .2006. NAMMA MODIS/AQUA AND MODIS/TERRA DEEP BLUE PRODUCTS [indicate subset used]. Dataset available online from the NASA Global Hydrometeorology Resource Center DAAC, Huntsville, Alabama, U.S.A. DOI: http://dx.doi.org/10.5067/NAMMA/MODIS/DATA201",
-            "issued": "2006-06-01",
-            "temporal": "2006-08-13T00:00:00Z/2006-09-30T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-04-28",
-            "keyword": [
-                "national geospatial data asset",
-                "aerosols",
-                "ngda",
-                "spectral/engineering",
-                "visible wavelengths",
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
-            "identifier": "C1979885686-GHRC_DAAC",
             "description": "The NAMMA MODIS/AQUA and MODIS/TERRA Deep Blue Products dataset is a collection of images depicting the aerosol optical depth derived from the MODIS deep blue algorithm from both AQUA and TERRA satellites. Additional imagery includes the RGB and Angstrom Exponent. These data files were generated during support of the NASA African Monsoon Multidisciplinary Analyses (NAMMA) campaign, a field research investigation sponsored by the Science Mission Directorate of the National Aeronautics and Space Administration (NASA). This mission was based in the Cape Verde Islands, 350 miles off the coast of Senegal in west Africa. Commencing in August 2006, NASA scientists employed surface observation networks and aircraft to characterize the evolution and structure of African Easterly Waves (AEWs) and Mesoscale Convective Systems over continental western Africa, and their associated impacts on regional water and energy budgets.",
-            "graphic-preview-description": "N/A",
-            "title": "NAMMA MODIS/AQUA AND MODIS/TERRA DEEP BLUE PRODUCTS V1",
-            "graphic-preview-file": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/namma/Deep-Blue/browse/",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FNAMMA%2FMODIS%2FDATA201",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FNAMMA%2FMODIS%2FDATA201",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=namdblue",
-                    "description": "Files may be downloaded directly to your workstation from this link",
                     "@type": "dcat:Distribution",
+                    "description": "Files may be downloaded directly to your workstation from this link",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=namdblue",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "image/gif",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/namma/Deep-Blue/browse/nam_aqu_060818_DBv2_GridAeroOptDep550nm.gif",
-                    "description": "Sample browse image",
                     "@type": "dcat:Distribution",
+                    "description": "Sample browse image",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/namma/Deep-Blue/browse/nam_aqu_060818_DBv2_GridAeroOptDep550nm.gif",
+                    "mediaType": "image/gif",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "image/gif",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/namma/Deep-Blue/browse/nam_aqu_060818_DBv2_GridAngExp.gif",
-                    "description": "Sample browse image",
                     "@type": "dcat:Distribution",
+                    "description": "Sample browse image",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/namma/Deep-Blue/browse/nam_aqu_060818_DBv2_GridAngExp.gif",
+                    "mediaType": "image/gif",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://ghrc.nsstc.nasa.gov/uso/ds_docs/namma/namdblue/namdblue_dataset.html",
-                    "description": "The guide document contains detailed information about the dataset",
                     "@type": "dcat:Distribution",
+                    "description": "The guide document contains detailed information about the dataset",
+                    "downloadURL": "http://ghrc.nsstc.nasa.gov/uso/ds_docs/namma/namdblue/namdblue_dataset.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/doc/namma/namdblue/Deep-Blue_Readme",
-                    "description": "Deep Blue data for NAMMA",
                     "@type": "dcat:Distribution",
+                    "description": "Deep Blue data for NAMMA",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/doc/namma/namdblue/Deep-Blue_Readme",
+                    "mediaType": "text/html",
                     "title": "View the primary investigator's documentation for this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/home/field-campaigns/namma",
-                    "description": "The home page for the project or program which sponsored the dataset",
                     "@type": "dcat:Distribution",
+                    "description": "The home page for the project or program which sponsored the dataset",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/home/field-campaigns/namma",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/namma/Deep-Blue/browse/",
-                    "description": "N/A",
                     "@type": "dcat:Distribution",
+                    "description": "N/A",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/namma/Deep-Blue/browse/",
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
+            "graphic-preview-file": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/namma/Deep-Blue/browse/",
+            "identifier": "C1979885686-GHRC_DAAC",
+            "issued": "2006-06-01",
+            "keyword": [
+                "national geospatial data asset",
+                "aerosols",
+                "ngda",
+                "spectral/engineering",
+                "visible wavelengths",
+                "atmosphere",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/NAMMA/MODIS/DATA201",
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
             "spatial": "-50.0 -5.0 10.0 30.0",
+            "temporal": "2006-08-13T00:00:00Z/2006-09-30T23:59:59Z",
             "theme": [
                 "NAMMA",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "NAMMA MODIS/AQUA AND MODIS/TERRA DEEP BLUE PRODUCTS V1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-X-SDC-3-PLUTOCRUISE-V2.0",
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
+            "description": "This data set contains Calibrated data taken by the New Horizons         Student Dust Counter                                                   instrument during the                                                    pluto cruise                                                           mission phase.  This is VERSION 2.0 of this data set.                    SDC collected science data intermittently during the hibernation         years following the Jupiter encounter, designated as the PLUTOCRUISE     phase.  There were also Annual Checkouts (ACOs), STIM calibrations,      Noise calibrations, and an anomaly in November, 2007.                    SDC's main science data collection periods were during hibernation.      During ACOs, science data are taken intermittently but the user must     be careful in analyzing these data since there is usually more           activity on the spacecraft during hibernation.  STIM and Noise refer     to scheduled calibrations and are done with a regular cadence of one     per year after the Jupiter encounter; they occurred sporadically in      the early years of the mission.                                          Note that some SDC data files have the same stop and start time and      a zero exposure time.  The reason for this is that the start and         stop time for SDC data files are the event times for the first and       last events in the files, so for files that contain a single event,      these two values are the same.                                           The changes in Version 2.0 were re-running of the ancillary data         in the data product, updated geometry from newer SPICE kernels,          minor editing of the documentation, catalogs, etc., and resolution       of liens from the December, 2014 review, plus those from the May,        2016 review of the Pluto Encounter data sets.                            New observations added with this version (V2.0) include ongoing          cruise observations from August, 2014 through January, 2015.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-x-sdc-3-plutocruise-v2.0_rsey-usaj",
+            "issued": "2018-09-05",
+            "keyword": [
+                "dust",
+                "new horizons"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-X-SDC-3-PLUTOCRUISE-V2.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-x-sdc-3-plutocruise-v2.0_rsey-usaj",
-            "description": "This data set contains Calibrated data taken by the New Horizons         Student Dust Counter                                                   instrument during the                                                    pluto cruise                                                           mission phase.  This is VERSION 2.0 of this data set.                    SDC collected science data intermittently during the hibernation         years following the Jupiter encounter, designated as the PLUTOCRUISE     phase.  There were also Annual Checkouts (ACOs), STIM calibrations,      Noise calibrations, and an anomaly in November, 2007.                    SDC's main science data collection periods were during hibernation.      During ACOs, science data are taken intermittently but the user must     be careful in analyzing these data since there is usually more           activity on the spacecraft during hibernation.  STIM and Noise refer     to scheduled calibrations and are done with a regular cadence of one     per year after the Jupiter encounter; they occurred sporadically in      the early years of the mission.                                          Note that some SDC data files have the same stop and start time and      a zero exposure time.  The reason for this is that the start and         stop time for SDC data files are the event times for the first and       last events in the files, so for files that contain a single event,      these two values are the same.                                           The changes in Version 2.0 were re-running of the ancillary data         in the data product, updated geometry from newer SPICE kernels,          minor editing of the documentation, catalogs, etc., and resolution       of liens from the December, 2014 review, plus those from the May,        2016 review of the Pluto Encounter data sets.                            New observations added with this version (V2.0) include ongoing          cruise observations from August, 2014 through January, 2015.",
-            "title": "NEW HORIZONS                            \n      SDC PLUTO CRUISE                                                        \n      CALIBRATED V2.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "NEW HORIZONS                            \n      SDC PLUTO CRUISE                                                        \n      CALIBRATED V2.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-VIRTIS-3-ESC2-MTP014-V2.0",
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
+            "description": "This release contains the calibrated data of the VIRTIS instrument on board of the spacecraft Rosetta. This volume contains data from the ESCORT 2 MTP014 phase, which occurred from 2015-03-11 to 2015-04-08 when at the vicinity of comet 67P. This data set V2.0 supersedes V1.0. It includes major updates on the data and documentation.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-virtis-3-esc2-mtp014-v2.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-VIRTIS-3-ESC2-MTP014-V2.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-virtis-3-esc2-mtp014-v2.0",
-            "description": "This release contains the calibrated data of the VIRTIS instrument on board of the spacecraft Rosetta. This volume contains data from the ESCORT 2 MTP014 phase, which occurred from 2015-03-11 to 2015-04-08 when at the vicinity of comet 67P. This data set V2.0 supersedes V1.0. It includes major updates on the data and documentation.",
-            "title": "ROSETTA-ORBITER 67P VIRTIS 3 ESCORT 2 MTP014 V2.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P VIRTIS 3 ESCORT 2 MTP014 V2.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=CO-SSA-RADAR-3-ABDR-SUMMARY-V1.0",
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
+            "description": "N/A",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.co-ssa-radar-3-abdr-summary-v1.0_rsht-etaj",
+            "issued": "2021-05-21",
+            "keyword": [
+                "cassini-huygens",
+                "titan"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=CO-SSA-RADAR-3-ABDR-SUMMARY-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.co-ssa-radar-3-abdr-summary-v1.0_rsht-etaj",
-            "description": "N/A",
-            "title": "CASSINI ORBITER RADAR ALTIMETER BURST DATA RECORD SUMMARY",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "CASSINI ORBITER RADAR ALTIMETER BURST DATA RECORD SUMMARY"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/347",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Middleton, E.M., and J. Sullivan. 1998. BOREAS TE-10 Photosynthetic Response Data. ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/347",
-            "issued": "2023-11-22",
-            "temporal": "1994-05-25T00:00:00Z/1996-10-13T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-11-28",
-            "keyword": [
-                "vegetation",
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
-            "identifier": "C2808129694-ORNL_CLOUD",
             "description": "Contains the 1994 oxygen evolution and leaf characteristics data collected by TE-10.",
-            "graphic-preview-description": "Browse Image",
-            "title": "BOREAS TE-10 Photosynthetic Response Data",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/boreas_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F347",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F347",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/boreas/TE/te10prd/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/boreas/TE/te10prd/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/BOREAS/guides/TE10_PhotoResp.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/BOREAS/guides/TE10_PhotoResp.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/347",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/347",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TE/te10prd/comp/te10prd.def",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TE/te10prd/comp/te10prd.def",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/msword",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TE/te10prd/comp/TE10_PhotoResp.doc",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TE/te10prd/comp/TE10_PhotoResp.doc",
+                    "mediaType": "application/msword",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TE/te10prd/comp/TE10_PhotoResp.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TE/te10prd/comp/TE10_PhotoResp.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TE/te10prd/comp/TE10_PhotoResp.txt",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TE/te10prd/comp/TE10_PhotoResp.txt",
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
+            "identifier": "C2808129694-ORNL_CLOUD",
+            "issued": "2023-11-22",
+            "keyword": [
+                "vegetation",
+                "earth science",
+                "ecological dynamics",
+                "biosphere"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/347",
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
             "spatial": "-106.2 53.63 -104.65 53.99",
+            "temporal": "1994-05-25T00:00:00Z/1996-10-13T23:59:59Z",
             "theme": [
                 "BOREAS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "BOREAS TE-10 Photosynthetic Response Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG2-S-LECP-3-RDR-NEAR-ENC-400MSEC-V1.0",
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
+            "description": "This near encounter data set consists of electron and ion counting rate data from the Low Energy Charged Particle (LECP) experiment on Voyager 1 while the spacecraft was within the very close vicinity of Saturn. This instrument measures the intensities of in-situ charged particles ( >13 keV electrons and >24 keV ions) with various levels of discrimination based on energy range and mass species. A subset of almost 100 LECP channels are included in this data set. The LECP data are globally calibrated to the extent possible.  During Saturn near encounter, the LEMPA (Low Energy Magnetospheric Particle Analyzer) subsystem was turned on for data collection. Particles include low energy electrons, protons, alpha particles, medium energy protons and ions, high energy and intensity protons, electrons, alpha particles, and Z >= nuclei. The near encounter data are 0.4 second rate measurements within 1/8 of the LECP instrumental motor rotation period (the angular scanning periods, or step period).",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg2-s-lecp-3-rdr-near-enc-400msec-v1.0_rsic-7ria",
+            "issued": "2021-05-21",
+            "keyword": [
+                "voyager",
+                "saturn"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG2-S-LECP-3-RDR-NEAR-ENC-400MSEC-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg2-s-lecp-3-rdr-near-enc-400msec-v1.0_rsic-7ria",
-            "description": "This near encounter data set consists of electron and ion counting rate data from the Low Energy Charged Particle (LECP) experiment on Voyager 1 while the spacecraft was within the very close vicinity of Saturn. This instrument measures the intensities of in-situ charged particles ( >13 keV electrons and >24 keV ions) with various levels of discrimination based on energy range and mass species. A subset of almost 100 LECP channels are included in this data set. The LECP data are globally calibrated to the extent possible.  During Saturn near encounter, the LEMPA (Low Energy Magnetospheric Particle Analyzer) subsystem was turned on for data collection. Particles include low energy electrons, protons, alpha particles, medium energy protons and ions, high energy and intensity protons, electrons, alpha particles, and Z >= nuclei. The near encounter data are 0.4 second rate measurements within 1/8 of the LECP instrumental motor rotation period (the angular scanning periods, or step period).",
-            "title": "VG2 LECP 0.4S HIGH RESOLUTION SATURN NEAR ENCOUNTER DATA",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "VG2 LECP 0.4S HIGH RESOLUTION SATURN NEAR ENCOUNTER DATA"
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
+            "description": "APXS, HAZCAM, MB, MI, MTES, NAVCAM, PANCAM, SPICE",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://pds.jpl.nasa.gov/tools/subscription_service/PDS-Subscription-Service-01-Nov-05.shtml",
+                    "mediaType": "application/html"
+                }
             ],
+            "identifier": "NASA-626",
+            "issued": "2018-06-25",
             "keyword": [
                 "pds",
                 "apxs",
@@ -1319730,641 +1319739,644 @@
                 "pancam",
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
-            "identifier": "NASA-626",
-            "description": "APXS, HAZCAM, MB, MI, MTES, NAVCAM, PANCAM, SPICE",
-            "title": "PDS Mars Exploration Rovers Data Release 6",
-            "programCode": [
-                "026:005"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://pds.jpl.nasa.gov/tools/subscription_service/PDS-Subscription-Service-01-Nov-05.shtml",
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
+            "title": "PDS Mars Exploration Rovers Data Release 6"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1114",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Dias, M.A., P.L.S. Dias, M. Longo, D.R. Fitzjarrald, and A.S. Denning. 2012. LBA-ECO CD-01 Meteorological Data, Tapajos and Amazon Rivers, Santarem, Brazil: 2001. ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/1114",
-            "issued": "2023-10-03",
-            "temporal": "2001-06-01T00:00:00Z/2001-08-16T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-10-11",
-            "keyword": [
-                "atmospheric temperature",
-                "atmosphere",
-                "aerosols",
-                "earth science",
-                "atmospheric winds",
-                "atmospheric pressure",
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
-            "identifier": "C2780905665-ORNL_CLOUD",
             "description": "This data set contains meteorological data collected around the confluence of the Tapajos River with the Amazon River in the Amazon Basin near Santarem, Brazil, in July and August 2001. Boundary layer and upper air measurements were collected with an acoustic sounder-sodar instrument, pilot balloons with optical theodolites, and radiosondes. Radiosondes also measured pressure, temperature, and relative humidity in addition to wind speed and direction. Measurements were made from five local stations at varying frequencies. There are 41 comma-delimited data files with this data set. Supporting information provided with the data set as companion files include: Weather forecasts: Weather forecasts were used to determine the presence of favorable conditions for the balloon flights during the CIRSAN experiment, as well as to help decide the radiosonde launch frequency. The daily observed and forecast weather descriptions for the study period (Weather_forecasts_Santarem.txt) are included. Satellite images: All the satellite images during the CIRSAN period are provided. This is a compilation of images from various instruments and satellite platforms. (See readme_sat.txt). There are 42 images in .gif format. CPTEC Analysis files: The CIRSAN measurement data were used in the CPTEC Global Analysis modeling activity. Model output results for the Pacific and South American region are provided in GRIB format. (See readme_GPSA.txt)",
-            "graphic-preview-description": "Browse Image",
-            "title": "LBA-ECO CD-01 Meteorological Data, Tapajos and Amazon Rivers, Santarem, Brazil: 2001",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/lba_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1114",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1114",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/lba/carbon_dynamics/CD01_CIRSAN_Meteorology_2001/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/lba/carbon_dynamics/CD01_CIRSAN_Meteorology_2001/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/LBA/guides/CD01_CIRSAN_Meteorology_2001.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/LBA/guides/CD01_CIRSAN_Meteorology_2001.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1114",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1114",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "image/gif",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/carbon_dynamics/CD01_CIRSAN_Meteorology_2001/comp/200106031200.gif",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/carbon_dynamics/CD01_CIRSAN_Meteorology_2001/comp/200106031200.gif",
+                    "mediaType": "image/gif",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/gif",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/carbon_dynamics/CD01_CIRSAN_Meteorology_2001/comp/200106040900.gif",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/carbon_dynamics/CD01_CIRSAN_Meteorology_2001/comp/200106040900.gif",
+                    "mediaType": "image/gif",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/gif",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/carbon_dynamics/CD01_CIRSAN_Meteorology_2001/comp/200106090900.gif",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/carbon_dynamics/CD01_CIRSAN_Meteorology_2001/comp/200106090900.gif",
+                    "mediaType": "image/gif",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/gif",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/carbon_dynamics/CD01_CIRSAN_Meteorology_2001/comp/200106111800.gif",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/carbon_dynamics/CD01_CIRSAN_Meteorology_2001/comp/200106111800.gif",
+                    "mediaType": "image/gif",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/gif",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/carbon_dynamics/CD01_CIRSAN_Meteorology_2001/comp/200106131200.gif",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/carbon_dynamics/CD01_CIRSAN_Meteorology_2001/comp/200106131200.gif",
+                    "mediaType": "image/gif",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/gif",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/carbon_dynamics/CD01_CIRSAN_Meteorology_2001/comp/200106150600.gif",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/carbon_dynamics/CD01_CIRSAN_Meteorology_2001/comp/200106150600.gif",
+                    "mediaType": "image/gif",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/gif",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/carbon_dynamics/CD01_CIRSAN_Meteorology_2001/comp/200106150900.gif",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/carbon_dynamics/CD01_CIRSAN_Meteorology_2001/comp/200106150900.gif",
+                    "mediaType": "image/gif",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/gif",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/carbon_dynamics/CD01_CIRSAN_Meteorology_2001/comp/200106161200.gif",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/carbon_dynamics/CD01_CIRSAN_Meteorology_2001/comp/200106161200.gif",
+                    "mediaType": "image/gif",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/gif",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/carbon_dynamics/CD01_CIRSAN_Meteorology_2001/comp/200106170600.gif",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/carbon_dynamics/CD01_CIRSAN_Meteorology_2001/comp/200106170600.gif",
+                    "mediaType": "image/gif",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/gif",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/carbon_dynamics/CD01_CIRSAN_Meteorology_2001/comp/200106190300.gif",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/carbon_dynamics/CD01_CIRSAN_Meteorology_2001/comp/200106190300.gif",
+                    "mediaType": "image/gif",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/gif",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/carbon_dynamics/CD01_CIRSAN_Meteorology_2001/comp/200106202100.gif",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/carbon_dynamics/CD01_CIRSAN_Meteorology_2001/comp/200106202100.gif",
+                    "mediaType": "image/gif",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/gif",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/carbon_dynamics/CD01_CIRSAN_Meteorology_2001/comp/200106212100.gif",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/carbon_dynamics/CD01_CIRSAN_Meteorology_2001/comp/200106212100.gif",
+                    "mediaType": "image/gif",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/gif",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/carbon_dynamics/CD01_CIRSAN_Meteorology_2001/comp/200106230300.gif",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/carbon_dynamics/CD01_CIRSAN_Meteorology_2001/comp/200106230300.gif",
+                    "mediaType": "image/gif",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/gif",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/carbon_dynamics/CD01_CIRSAN_Meteorology_2001/comp/200106252100.gif",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/carbon_dynamics/CD01_CIRSAN_Meteorology_2001/comp/200106252100.gif",
+                    "mediaType": "image/gif",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/gif",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/carbon_dynamics/CD01_CIRSAN_Meteorology_2001/comp/200106280600.gif",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/carbon_dynamics/CD01_CIRSAN_Meteorology_2001/comp/200106280600.gif",
+                    "mediaType": "image/gif",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/gif",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/carbon_dynamics/CD01_CIRSAN_Meteorology_2001/comp/200106291800.gif",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/carbon_dynamics/CD01_CIRSAN_Meteorology_2001/comp/200106291800.gif",
+                    "mediaType": "image/gif",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/gif",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/carbon_dynamics/CD01_CIRSAN_Meteorology_2001/comp/200107031500.gif",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/carbon_dynamics/CD01_CIRSAN_Meteorology_2001/comp/200107031500.gif",
+                    "mediaType": "image/gif",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/gif",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/carbon_dynamics/CD01_CIRSAN_Meteorology_2001/comp/200107050300.gif",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/carbon_dynamics/CD01_CIRSAN_Meteorology_2001/comp/200107050300.gif",
+                    "mediaType": "image/gif",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/gif",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/carbon_dynamics/CD01_CIRSAN_Meteorology_2001/comp/200107090900.gif",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/carbon_dynamics/CD01_CIRSAN_Meteorology_2001/comp/200107090900.gif",
+                    "mediaType": "image/gif",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/gif",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/carbon_dynamics/CD01_CIRSAN_Meteorology_2001/comp/200107111800.gif",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/carbon_dynamics/CD01_CIRSAN_Meteorology_2001/comp/200107111800.gif",
+                    "mediaType": "image/gif",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/gif",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/carbon_dynamics/CD01_CIRSAN_Meteorology_2001/comp/200107121200.gif",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/carbon_dynamics/CD01_CIRSAN_Meteorology_2001/comp/200107121200.gif",
+                    "mediaType": "image/gif",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/gif",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/carbon_dynamics/CD01_CIRSAN_Meteorology_2001/comp/200107121800.gif",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/carbon_dynamics/CD01_CIRSAN_Meteorology_2001/comp/200107121800.gif",
+                    "mediaType": "image/gif",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/gif",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/carbon_dynamics/CD01_CIRSAN_Meteorology_2001/comp/200107130600.gif",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/carbon_dynamics/CD01_CIRSAN_Meteorology_2001/comp/200107130600.gif",
+                    "mediaType": "image/gif",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/gif",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/carbon_dynamics/CD01_CIRSAN_Meteorology_2001/comp/200107161200.gif",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/carbon_dynamics/CD01_CIRSAN_Meteorology_2001/comp/200107161200.gif",
+                    "mediaType": "image/gif",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/gif",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/carbon_dynamics/CD01_CIRSAN_Meteorology_2001/comp/200107181500.gif",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/carbon_dynamics/CD01_CIRSAN_Meteorology_2001/comp/200107181500.gif",
+                    "mediaType": "image/gif",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/gif",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/carbon_dynamics/CD01_CIRSAN_Meteorology_2001/comp/200107182100.gif",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/carbon_dynamics/CD01_CIRSAN_Meteorology_2001/comp/200107182100.gif",
+                    "mediaType": "image/gif",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/gif",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/carbon_dynamics/CD01_CIRSAN_Meteorology_2001/comp/200107200300.gif",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/carbon_dynamics/CD01_CIRSAN_Meteorology_2001/comp/200107200300.gif",
+                    "mediaType": "image/gif",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/gif",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/carbon_dynamics/CD01_CIRSAN_Meteorology_2001/comp/200107201500.gif",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/carbon_dynamics/CD01_CIRSAN_Meteorology_2001/comp/200107201500.gif",
+                    "mediaType": "image/gif",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/gif",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/carbon_dynamics/CD01_CIRSAN_Meteorology_2001/comp/200107230300.gif",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/carbon_dynamics/CD01_CIRSAN_Meteorology_2001/comp/200107230300.gif",
+                    "mediaType": "image/gif",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/gif",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/carbon_dynamics/CD01_CIRSAN_Meteorology_2001/comp/200107240900.gif",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/carbon_dynamics/CD01_CIRSAN_Meteorology_2001/comp/200107240900.gif",
+                    "mediaType": "image/gif",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/gif",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/carbon_dynamics/CD01_CIRSAN_Meteorology_2001/comp/200107250000.gif",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/carbon_dynamics/CD01_CIRSAN_Meteorology_2001/comp/200107250000.gif",
+                    "mediaType": "image/gif",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/gif",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/carbon_dynamics/CD01_CIRSAN_Meteorology_2001/comp/200107260000.gif",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/carbon_dynamics/CD01_CIRSAN_Meteorology_2001/comp/200107260000.gif",
+                    "mediaType": "image/gif",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/gif",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/carbon_dynamics/CD01_CIRSAN_Meteorology_2001/comp/200107291500.gif",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/carbon_dynamics/CD01_CIRSAN_Meteorology_2001/comp/200107291500.gif",
+                    "mediaType": "image/gif",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/gif",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/carbon_dynamics/CD01_CIRSAN_Meteorology_2001/comp/200107301500.gif",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/carbon_dynamics/CD01_CIRSAN_Meteorology_2001/comp/200107301500.gif",
+                    "mediaType": "image/gif",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/gif",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/carbon_dynamics/CD01_CIRSAN_Meteorology_2001/comp/200108011500.gif",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/carbon_dynamics/CD01_CIRSAN_Meteorology_2001/comp/200108011500.gif",
+                    "mediaType": "image/gif",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/gif",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/carbon_dynamics/CD01_CIRSAN_Meteorology_2001/comp/200108040900.gif",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/carbon_dynamics/CD01_CIRSAN_Meteorology_2001/comp/200108040900.gif",
+                    "mediaType": "image/gif",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/gif",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/carbon_dynamics/CD01_CIRSAN_Meteorology_2001/comp/200108060600.gif",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/carbon_dynamics/CD01_CIRSAN_Meteorology_2001/comp/200108060600.gif",
+                    "mediaType": "image/gif",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/gif",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/carbon_dynamics/CD01_CIRSAN_Meteorology_2001/comp/200108091200.gif",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/carbon_dynamics/CD01_CIRSAN_Meteorology_2001/comp/200108091200.gif",
+                    "mediaType": "image/gif",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/gif",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/carbon_dynamics/CD01_CIRSAN_Meteorology_2001/comp/200108091500.gif",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/carbon_dynamics/CD01_CIRSAN_Meteorology_2001/comp/200108091500.gif",
+                    "mediaType": "image/gif",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/gif",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/carbon_dynamics/CD01_CIRSAN_Meteorology_2001/comp/200108100600.gif",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/carbon_dynamics/CD01_CIRSAN_Meteorology_2001/comp/200108100600.gif",
+                    "mediaType": "image/gif",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/gif",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/carbon_dynamics/CD01_CIRSAN_Meteorology_2001/comp/200108101200.gif",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/carbon_dynamics/CD01_CIRSAN_Meteorology_2001/comp/200108101200.gif",
+                    "mediaType": "image/gif",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/gif",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/carbon_dynamics/CD01_CIRSAN_Meteorology_2001/comp/200108150900.gif",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/carbon_dynamics/CD01_CIRSAN_Meteorology_2001/comp/200108150900.gif",
+                    "mediaType": "image/gif",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/carbon_dynamics/CD01_CIRSAN_Meteorology_2001/comp/CD01_CIRSAN_Meteorology_2001.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/carbon_dynamics/CD01_CIRSAN_Meteorology_2001/comp/CD01_CIRSAN_Meteorology_2001.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/carbon_dynamics/CD01_CIRSAN_Meteorology_2001/comp/readme_GPSA.txt",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/carbon_dynamics/CD01_CIRSAN_Meteorology_2001/comp/readme_GPSA.txt",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/carbon_dynamics/CD01_CIRSAN_Meteorology_2001/comp/readme_sat.txt",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/carbon_dynamics/CD01_CIRSAN_Meteorology_2001/comp/readme_sat.txt",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/zip",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/carbon_dynamics/CD01_CIRSAN_Meteorology_2001/comp/stratosphere.zip",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/carbon_dynamics/CD01_CIRSAN_Meteorology_2001/comp/stratosphere.zip",
+                    "mediaType": "application/zip",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/zip",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/carbon_dynamics/CD01_CIRSAN_Meteorology_2001/comp/troposphere.zip",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/carbon_dynamics/CD01_CIRSAN_Meteorology_2001/comp/troposphere.zip",
+                    "mediaType": "application/zip",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/carbon_dynamics/CD01_CIRSAN_Meteorology_2001/comp/Weather_forecasts_Santarem.txt",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/carbon_dynamics/CD01_CIRSAN_Meteorology_2001/comp/Weather_forecasts_Santarem.txt",
+                    "mediaType": "text/html",
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
+            "identifier": "C2780905665-ORNL_CLOUD",
+            "issued": "2023-10-03",
+            "keyword": [
+                "atmospheric temperature",
+                "atmosphere",
+                "aerosols",
+                "earth science",
+                "atmospheric winds",
+                "atmospheric pressure",
+                "atmospheric water vapor"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1114",
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
             "spatial": "-55.17 -2.78 -54.72 -2.43",
+            "temporal": "2001-06-01T00:00:00Z/2001-08-16T23:59:59Z",
             "theme": [
                 "LBA-ECO",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "LBA-ECO CD-01 Meteorological Data, Tapajos and Amazon Rivers, Santarem, Brazil: 2001"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=PHX-M-SSI-5-MOSAIC-OPS-V1.0",
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
+            "description": "The Surface Stereo Imager (SSI) experiment on the Mars Phoenix Lander consists of one instrument component plus command electronics. This SSI Imaging Operations RDR data set contains mosaic data from the Surface Stereo Imager (SSI).",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.phx-m-ssi-5-mosaic-ops-v1.0_rsmh-5q3q",
+            "issued": "2018-06-26",
+            "keyword": [
+                "mars",
+                "phoenix"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=PHX-M-SSI-5-MOSAIC-OPS-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.phx-m-ssi-5-mosaic-ops-v1.0_rsmh-5q3q",
-            "description": "The Surface Stereo Imager (SSI) experiment on the Mars Phoenix Lander consists of one instrument component plus command electronics. This SSI Imaging Operations RDR data set contains mosaic data from the Surface Stereo Imager (SSI).",
-            "title": "PHOENIX MARS SURFACE STEREO IMAGER 5 MOSAIC OPS V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "PHOENIX MARS SURFACE STEREO IMAGER 5 MOSAIC OPS V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ASDC_DAAC/FIRE/0069",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "1999-11-15. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/ASDC_DAAC/FIRE/0069.",
-            "issued": "1999-11-03",
-            "temporal": "1992-06-02T00:00:00Z/1992-06-26T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2018-07-11",
-            "keyword": [
-                "earth science",
-                "atmospheric water vapor",
-                "atmosphere",
-                "aerosols",
-                "clouds"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "HERMANN GERBER",
                 "hasEmail": "mailto:gerber@access.digex.net"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/LARC/SD/ASDC"
-            },
-            "identifier": "C1000001053-LARC_ASDC",
             "description": "The First ISCCP Regional Experiments have been designed to improve data products and cloud/radiation parameterizations used in general circulation models (GCMs). Specifically, the goals of FIRE are (1) to improve basic understanding of the interaction of physical processes in determining life cycles of cirrus and marine stratocumulus systems and the radiative properties of these clouds during their life cycles and (2) to investigate the interrelationships between the ISCCP data, GCM parameterizations, and higher space and time resolution cloud data.To-date, four intensive field-observation periods were planned and executed: a cirrus IFO (October 13-November 2, 1986); a marine stratocumulus IFO off the southwestern coast of California (June 29-July 20, 1987); a second cirrus IFO in southeastern Kansas (November 13-December 7, 1991); and a second marine stratocumulus IFO in the eastern North Atlantic Ocean (June 1-June 28, 1992). Each mission combined coordinated satellite, airborne, and surface observations with modeling studies to investigate the cloud properties and physical processes of the cloud systems. The development of parameterizations requires an understanding of the processes that generate, maintain, and dissipate boundary layer clouds. This development is currently impeded by lack of understanding of the transition from stratocumulus clouds to trade cumulus clouds and the factors that control cloud type and amount in the boundary layer. The Atlantic Stratocumulus Transition EXperiment (ASTEX) was designed to address key issues related to stratocumulus to trade cumulus transition and mode selection. ASTEX involved intensive measurements from several platforms operating from 1-28 June 1992 in the area of the Azores and Madeira Islands. The purpose was to study how the transition and mode selection are effected by 1) cloud-top entrainment instability, 2) diurnal decoupling and clearing due to solar absorption, 3) patchy drizzle and a transition to horizontally inhomogeneous clouds through decoupling, 4) mesoscale variability in cloud thickness and associated mesoscale circulations, and 5) episodic strong subsidence lowering the inversion below the LCL. Detailed descriptions of the scientific goals of ASTEX are in the FIRE Phase II: Research plan (1989) and in the ASTEX Operations Plan (1992).This ASCII formatted data set includes data collected aboard the University of Washington's Corsair 131A airplane. The cloud microphysics probe (PVM-100A) was used to gather data on cloud liquid water content, particle surface area, and effective droplet radius. Please refer to the reference authored by H. Gerber to obtain information on how the raw data were reduced to produce this data set.",
-            "title": "First ISCCP Regional Experiment (FIRE) Atlantic Stratocumulus Transition Experiment (ASTEX) University of Washington C-131A 10Hz Data",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC_DAAC%2FFIRE%2F0069",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC_DAAC%2FFIRE%2F0069",
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
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1000001053-LARC_ASDC",
-                    "description": "Earthdata Search for FIRE_AX_UW_GERB_10HZ_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for FIRE_AX_UW_GERB_10HZ_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1000001053-LARC_ASDC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/ASDC_DAAC/FIRE/0069",
-                    "description": "DOI data set landing page for FIRE_AX_UW_GERB_10HZ_1",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for FIRE_AX_UW_GERB_10HZ_1",
+                    "downloadURL": "https://doi.org/10.5067/ASDC_DAAC/FIRE/0069",
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
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/guide/base_fire_ax_uw_dataset.pdf",
-                    "description": "FIRE ASTEX University of Washington (UW) Langley DAAC Data Set Document",
                     "@type": "dcat:Distribution",
+                    "description": "FIRE ASTEX University of Washington (UW) Langley DAAC Data Set Document",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/guide/base_fire_ax_uw_dataset.pdf",
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
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/FIRE/FIRE_AX_UW_GERB_10HZ/",
-                    "description": "ASDC Direct Data Download for FIRE_AX_UW_GERB_10HZ_1",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for FIRE_AX_UW_GERB_10HZ_1",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/FIRE/FIRE_AX_UW_GERB_10HZ/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/FIRE/FIRE_AX_UW_GERB_10HZ/contents.html",
-                    "description": "OPeNDAP data access for FIRE_AX_UW_GERB_10HZ_1",
                     "@type": "dcat:Distribution",
+                    "description": "OPeNDAP data access for FIRE_AX_UW_GERB_10HZ_1",
+                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/FIRE/FIRE_AX_UW_GERB_10HZ/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 }
             ],
+            "identifier": "C1000001053-LARC_ASDC",
+            "issued": "1999-11-03",
+            "keyword": [
+                "earth science",
+                "atmospheric water vapor",
+                "atmosphere",
+                "aerosols",
+                "clouds"
+            ],
+            "landingPage": "https://doi.org/10.5067/ASDC_DAAC/FIRE/0069",
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
             "spatial": "<?xml version=\"1.0\" encoding=\"UTF-8\"?><gml:Polygon xmlns:gml=\"http://www.opengis.net/gml/3.2\" srsName=\"EPSG:4326\"><gml:outerBoundaryIs><gml:LinearRing><gml:posList>32.34 -26.65 32.34 -22.22 37.34 -22.22 37.34 -26.65 32.34 -26.65</gml:posList></gml:LinearRing></gml:outerBoundaryIs><gml:innerBoundaryIs></gml:innerBoundaryIs></gml:Polygon>",
+            "temporal": "1992-06-02T00:00:00Z/1992-06-26T23:59:59.999Z",
             "theme": [
                 "FIRE",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "First ISCCP Regional Experiment (FIRE) Atlantic Stratocumulus Transition Experiment (ASTEX) University of Washington C-131A 10Hz Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1214473550-ASF.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, ASF.",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "undefined",
+                "hasEmail": "mailto:uso@asf.alaska.edu"
+            },
+            "description": "SMAP Level 1B Sigma Naught Low Res Product Metadata",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "Vertex, the ASF search and download interface",
+                    "downloadURL": "https://vertex.daac.asf.alaska.edu/",
+                    "mediaType": "text/html",
+                    "title": "Download this dataset"
+                }
+            ],
+            "identifier": "C1214473550-ASF",
             "issued": "2015-07-31",
-            "temporal": "2015-02-12T16:02:58Z/2022-01-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2016-05-07",
             "keyword": [
                 "spectral/engineering",
                 "platform characteristics",
@@ -1320373,87 +1320385,77 @@
                 "land surface",
                 "earth science"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "undefined",
-                "hasEmail": "mailto:uso@asf.alaska.edu"
-            },
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1214473550-ASF.html",
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
-            "identifier": "C1214473550-ASF",
-            "description": "SMAP Level 1B Sigma Naught Low Res Product Metadata",
-            "title": "SMAP_L1B_SIGMA_NAUGHT_LOW_RES_METADATA_V001",
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
+            "title": "SMAP_L1B_SIGMA_NAUGHT_LOW_RES_METADATA_V001"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-2-ESC2-67PCHURYUMOV-M14-V1.0",
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
+            "description": "This data set contains raw EDR images acquired by the OSIRIS Narrow Angle\nCamera during the escort phase of the Rosetta mission at the comet 67P,\ncovering the period from 2015-03-10 to 2015-04-08.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-2-esc2-67pchuryumov-m14-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-2-ESC2-67PCHURYUMOV-M14-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-2-esc2-67pchuryumov-m14-v1.0",
-            "description": "This data set contains raw EDR images acquired by the OSIRIS Narrow Angle\nCamera during the escort phase of the Rosetta mission at the comet 67P,\ncovering the period from 2015-03-10 to 2015-04-08.",
-            "title": "ROSETTA-ORBITER COMET ESCORT OSINAC 2 EDR MTP 014 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER COMET ESCORT OSINAC 2 EDR MTP 014 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=IUE-C-LWP-3-EDR-IUECDB-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "IUE Long-Wavelength Prime (LWP) observations of comets",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.iue-c-lwp-3-edr-iuecdb-v1.0_rsuh-id44",
             "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "97p/metcalf-brewington 1 (1906 v2)",
                 "109p/swift-tuttle 1 (1862 o1)",
@@ -1320497,475 +1320499,448 @@
                 "p/mcnaught-russell 1 (1994 x1)",
                 "support archives"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=IUE-C-LWP-3-EDR-IUECDB-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.iue-c-lwp-3-edr-iuecdb-v1.0_rsuh-id44",
-            "description": "IUE Long-Wavelength Prime (LWP) observations of comets",
-            "title": "IUE LWP DATA OF COMETS",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "IUE LWP DATA OF COMETS"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/EPIC/DSCOVR_L2_SO2_02",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2017-11-09. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/EPIC/DSCOVR_L2_SO2_02. https://asdc.larc.nasa.gov/project/DSCOVR.",
-            "issued": "2017-06-07",
-            "temporal": "2016-01-02T00:00:00Z/2022-01-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2017-06-07",
-            "keyword": [
-                "atmosphere",
-                "atmospheric chemistry",
-                "air quality",
-                "earth science"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Marshall Sutton",
                 "hasEmail": "mailto:marshall.h.sutton@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/LARC/SD/ASDC"
-            },
-            "identifier": "C1725575876-LARC_ASDC",
             "description": "DSCOVR_EPIC_L2_SO2_v03 is the Deep Space Climate Observatory (DSCOVR) Enhanced Polychromatic Imaging Camera (EPIC) Level 2 Sulfur Dioxide (SO2) product with EPIC version 03 inputs. It has key UV channels suitable for retrievals of volcanic sulfur dioxide (SO2) and ash, enabling timely tracking and forecasting of volcanic plumes and enhancing our ability to mitigate aviation hazard. EPIC measurements will also be co-located with all satellite UV and infrared sensors, offering ample opportunities for data inter-comparisons and for demonstrating advanced retrievals of volcanic ash mass through a synergistic approach. We propose to implement our mature algorithms previously developed for Total Ozone Mapping Spectrometer (TOMS) and Ozone Monitoring Instrument (OMI) to enable SO2 and Ash Index (AI) products from EPIC UV observations to demonstrate improved estimates of volcanic SO2 and ash mass, height and sulfate aerosol loading.",
-            "title": "DSCOVR EPIC Level 2 Sulfur dioxide (SO2) Product with EPIC Version 3 Input Version 2",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FEPIC%2FDSCOVR_L2_SO2_02",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FEPIC%2FDSCOVR_L2_SO2_02",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://epic.gsfc.nasa.gov/science/products/so2",
-                    "description": "Science description on EPIC home page.",
                     "@type": "dcat:Distribution",
+                    "description": "Science description on EPIC home page.",
+                    "downloadURL": "https://epic.gsfc.nasa.gov/science/products/so2",
+                    "mediaType": "text/html",
                     "title": "The dataset's home page"
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
-                    "downloadURL": "https://doi.org/10.5067/EPIC/DSCOVR_L2_SO2_02",
-                    "description": "DOI data set landing page for DSCOVR_EPIC_L2_SO2_02",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for DSCOVR_EPIC_L2_SO2_02",
+                    "downloadURL": "https://doi.org/10.5067/EPIC/DSCOVR_L2_SO2_02",
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
-                    "downloadURL": "https://epic.gsfc.nasa.gov/",
-                    "description": "DSCOVR EPIC Visualization Tool",
                     "@type": "dcat:Distribution",
+                    "description": "DSCOVR EPIC Visualization Tool",
+                    "downloadURL": "https://epic.gsfc.nasa.gov/",
+                    "mediaType": "text/html",
                     "title": "Use this dataset in a web based map viewerf"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1725575876-LARC_ASDC",
-                    "description": "Earthdata Search for DSCOVR_EPIC_L2_SO2_02 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for DSCOVR_EPIC_L2_SO2_02 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1725575876-LARC_ASDC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/DSCOVR/EPIC/L2_SO2_02/",
-                    "description": "ASDC Direct Data Download for DSCOVR_EPIC_L2_SO2_02",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for DSCOVR_EPIC_L2_SO2_02",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/DSCOVR/EPIC/L2_SO2_02/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/DSCOVR/EPIC/L2_SO2_02/contents.html",
-                    "description": "OPeNDAP data access for DSCOVR_EPIC_L2_SO2_02",
                     "@type": "dcat:Distribution",
+                    "description": "OPeNDAP data access for DSCOVR_EPIC_L2_SO2_02",
+                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/DSCOVR/EPIC/L2_SO2_02/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/dscovr/EPICSO2_L2_summary_final.pdf",
-                    "description": "Description of the DSCOVR/EPIC volcanic SO2 Level 2 Algorithm",
                     "@type": "dcat:Distribution",
+                    "description": "Description of the DSCOVR/EPIC volcanic SO2 Level 2 Algorithm",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/dscovr/EPICSO2_L2_summary_final.pdf",
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
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/dscovr/DSCOVR_EPIC_Calibration_Factors_V02.pdf",
-                    "description": "EPIC level 1 A & B Calibration factors table",
                     "@type": "dcat:Distribution",
+                    "description": "EPIC level 1 A & B Calibration factors table",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/dscovr/DSCOVR_EPIC_Calibration_Factors_V02.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's calibration documentation"
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
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/dscovr/DSCOVR_EPIC_Geolocation_V03.pdf",
-                    "description": "EPIC Geolocation and Color Imagery Algorithm Revision 5 July 5, 2017",
                     "@type": "dcat:Distribution",
+                    "description": "EPIC Geolocation and Color Imagery Algorithm Revision 5 July 5, 2017",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/dscovr/DSCOVR_EPIC_Geolocation_V03.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View the documentation for this dataset's algorithms"
                 }
             ],
+            "identifier": "C1725575876-LARC_ASDC",
+            "issued": "2017-06-07",
+            "keyword": [
+                "atmosphere",
+                "atmospheric chemistry",
+                "air quality",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/EPIC/DSCOVR_L2_SO2_02",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2017-06-07",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/LARC/SD/ASDC"
+            },
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2016-01-02T00:00:00Z/2022-01-17T00:00:00Z",
             "theme": [
                 "DSCOVR",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "DSCOVR EPIC Level 2 Sulfur dioxide (SO2) Product with EPIC Version 3 Input Version 2"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/604",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Wofsy, S.C., and A. Dunn. 2001. BOREAS Follow-On FLX-01 NSA-OBS Tower Flux, Meteorological, and Soil Temp. Data. ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/604",
-            "issued": "2024-04-27",
-            "temporal": "1996-10-31T00:00:00Z/1999-01-01T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-04-28",
-            "keyword": [
-                "atmospheric chemistry",
-                "atmosphere",
-                "atmospheric winds",
-                "atmospheric radiation",
-                "vegetation",
-                "land surface",
-                "earth science",
-                "biosphere",
-                "precipitation",
-                "atmospheric water vapor",
-                "atmospheric temperature",
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
-            "identifier": "C2956524589-ORNL_CLOUD",
             "description": "The BOREAS Follow-On FLX-01 team collected tower flux, surface meteorological, and soil temperature data at the BOREAS NSA-OBS site continuously from March 1994 through December 1998.  Data from March 1994 through October 1996 are included in the BOREAS TF-03 effort while data from the end of October 1996 through December 1998 are included in the BOREAS Follow-on FLX-01 effort.",
-            "graphic-preview-description": "Browse Image",
-            "title": "BOREAS Follow-On FLX-01 NSA-OBS Tower Flux, Meteorological, and Soil Temp. Data",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/boreas_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F604",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F604",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/boreas/TF/BFO_flx01_flux_met_temp/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/boreas/TF/BFO_flx01_flux_met_temp/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/BOREAS/FollowOn/guides/flx01_flux_met_temp_doc.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/BOREAS/FollowOn/guides/flx01_flux_met_temp_doc.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/604",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/604",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TF/BFO_flx01_flux_met_temp/comp/0_readme.txt",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TF/BFO_flx01_flux_met_temp/comp/0_readme.txt",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TF/BFO_flx01_flux_met_temp/comp/0_site_list.txt",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TF/BFO_flx01_flux_met_temp/comp/0_site_list.txt",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TF/BFO_flx01_flux_met_temp/comp/flx01_flux_met_temp_doc.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TF/BFO_flx01_flux_met_temp/comp/flx01_flux_met_temp_doc.pdf",
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
+            "identifier": "C2956524589-ORNL_CLOUD",
+            "issued": "2024-04-27",
+            "keyword": [
+                "atmospheric chemistry",
+                "atmosphere",
+                "atmospheric winds",
+                "atmospheric radiation",
+                "vegetation",
+                "land surface",
+                "earth science",
+                "biosphere",
+                "precipitation",
+                "atmospheric water vapor",
+                "atmospheric temperature",
+                "soils"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/604",
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
             "spatial": "55.88 -98.48",
+            "temporal": "1996-10-31T00:00:00Z/1999-01-01T23:59:59Z",
             "theme": [
                 "BOREAS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "BOREAS Follow-On FLX-01 NSA-OBS Tower Flux, Meteorological, and Soil Temp. Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/GPM/DPR/Ku/2A/07",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Toshio Iguchi, Robert Meneghini. 2021-12-10. GPM_2AKu. Version 07. GPM DPR Ku Precipitation Profile 2A 1.5 hours 5 km V07. Greenbelt, MD. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/GPM/DPR/Ku/2A/07. https://disc.gsfc.nasa.gov/datacollection/GPM_2AKu_07.html. Digital Science Data.",
-            "issued": "2021-12-06",
-            "temporal": "2014-03-08T00:00:00Z/2023-02-28T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2021-12-06",
-            "keyword": [
-                "spectral/engineering",
-                "atmosphere",
-                "earth science",
-                "precipitation",
-                "radar",
-                "atmospheric water vapor"
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
-            "identifier": "C2179081538-GES_DISC",
-            "description": "Version 07 is the current version of the data set. Older versions will no longer be available and have been superseded by Version 07.\n\n   The 2AKu algorithm is a single-frequency retrieval that relies on Ku-band data only, and provides precipitation estimates from the Ku radar of the Dual-Frequency Precipitation Radar on the core GPM spacecraft. \n\n   The Ku Level-2A product, 2AKu, \u201dKu precipitation,\u201d is written as a 1 swath structure. The swath is NS, normal scans.\n\n   Since the Ku-band channel of the Dual-Frequency Precipitaiton Radar (DPR)  is very similar to the TRMM PR, the principal challenge in the development of the DPR level 2 algorithms is to combine the new Ka-band data with the Ku-band data.\n\t\n   It is important to note the difference between the single- and the dual-frequency (DF) algorithms. While this 2AKu dataset is a single-frequency retrieval, the DF algorithm employs both KuPR and KaPR L1B standard products as inputs. The DF algorithm cannot be executed unless both L1B products are available. Pixels observed by DPR can be categorized into three types: pixels in the inner swath of normal scans (observed both by KuPR and KaPR), pixels in the outer swath of normal scans (observed only by KuPR), and pixels in the interleaved scans (observed only by KaPR in the high-sensitivity mode). The KuPR algorithm is executed for pixels in both inner and outer swaths of normal scans. The KaPR algorithm is executed for pixels in the inner swath of normal scans and in the interleaved scans. The DF algorithm is executed for pixels of all the three kinds.",
-            "release-place": "Greenbelt, MD",
-            "series-name": "GPM_2AKu",
             "creator": "Toshio Iguchi, Robert Meneghini",
-            "title": "GPM DPR Ku Precipitation Profile 2A 1.5 hours 5 km V07 (GPM_2AKu) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/GPM/browse/GPM_2AKu.png",
-            "programCode": [
-                "026:001"
-            ],
+            "data-presentation-form": "Digital Science Data",
+            "description": "Version 07 is the current version of the data set. Older versions will no longer be available and have been superseded by Version 07.\n\n   The 2AKu algorithm is a single-frequency retrieval that relies on Ku-band data only, and provides precipitation estimates from the Ku radar of the Dual-Frequency Precipitation Radar on the core GPM spacecraft. \n\n   The Ku Level-2A product, 2AKu, \u201dKu precipitation,\u201d is written as a 1 swath structure. The swath is NS, normal scans.\n\n   Since the Ku-band channel of the Dual-Frequency Precipitaiton Radar (DPR)  is very similar to the TRMM PR, the principal challenge in the development of the DPR level 2 algorithms is to combine the new Ka-band data with the Ku-band data.\n\t\n   It is important to note the difference between the single- and the dual-frequency (DF) algorithms. While this 2AKu dataset is a single-frequency retrieval, the DF algorithm employs both KuPR and KaPR L1B standard products as inputs. The DF algorithm cannot be executed unless both L1B products are available. Pixels observed by DPR can be categorized into three types: pixels in the inner swath of normal scans (observed both by KuPR and KaPR), pixels in the outer swath of normal scans (observed only by KuPR), and pixels in the interleaved scans (observed only by KaPR in the high-sensitivity mode). The KuPR algorithm is executed for pixels in both inner and outer swaths of normal scans. The KaPR algorithm is executed for pixels in the inner swath of normal scans and in the interleaved scans. The DF algorithm is executed for pixels of all the three kinds.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGPM%2FDPR%2FKu%2F2A%2F07",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGPM%2FDPR%2FKu%2F2A%2F07",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
@@ -1320975,45 +1320950,45 @@
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/GPM_2AKu_07.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/GPM_2AKu_07.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://gpm1.gesdisc.eosdis.nasa.gov/data/GPM_L2/GPM_2AKu.07/",
-                    "description": "Access the data via HTTPS",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS",
+                    "downloadURL": "https://gpm1.gesdisc.eosdis.nasa.gov/data/GPM_L2/GPM_2AKu.07/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://gpm1.gesdisc.eosdis.nasa.gov/opendap/GPM_L2/GPM_2AKu.07/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://gpm1.gesdisc.eosdis.nasa.gov/opendap/GPM_L2/GPM_2AKu.07/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=GPM_2AKu_07",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=GPM_2AKu_07",
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
@@ -1321023,203 +1320998,229 @@
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
-                    "downloadURL": "https://pps.gsfc.nasa.gov/gpminstruments.html",
-                    "description": "Instrument Description",
                     "@type": "dcat:Distribution",
+                    "description": "Instrument Description",
+                    "downloadURL": "https://pps.gsfc.nasa.gov/gpminstruments.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/GPM/browse/GPM_2AKu.png",
+            "identifier": "C2179081538-GES_DISC",
+            "issued": "2021-12-06",
+            "keyword": [
+                "spectral/engineering",
+                "atmosphere",
+                "earth science",
+                "precipitation",
+                "radar",
+                "atmospheric water vapor"
+            ],
+            "landingPage": "https://doi.org/10.5067/GPM/DPR/Ku/2A/07",
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
+            "release-place": "Greenbelt, MD",
+            "series-name": "GPM_2AKu",
             "spatial": "-180.0 -70.0 180.0 70.0",
+            "temporal": "2014-03-08T00:00:00Z/2023-02-28T00:00:00Z",
             "theme": [
                 "GPM",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "GPM DPR Ku Precipitation Profile 2A 1.5 hours 5 km V07 (GPM_2AKu) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MESS-H-MDIS-5-RDR-HIW-V1.0",
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
-                "messenger",
-                "mercury"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "Abstract ======== The Mercury Dual Imaging System (MDIS) consists of two cameras, a Wide Angle Camera (WAC) and a Narrow Angle Camera (NAC), mounted on a common pivot platform. This dataset includes Map Projected High- Incidence Angle Basemap Illuminated from the West RDRs (HIWs) which comprise a global map of I/F measured by the NAC or WAC filter 7 (both centered near 750 nm) during the the Extended Mission at high incidence angles to accentuate subtle topography, photometrically normalized to a solar incidence angle (i) = 30 degrees, emission angle (e) = 0 degrees, and phase angle (g) = 30 degrees at a spatial sampling of 256 pixels per degree. The HIW data set is a companion to the Map Projected High-Incidence Angle Basemap Illuminated from the East RDR (HIE) data set. Together the two data sets are intended to detect and allow the mapping of subtle topography. They complement a Basemap Data Record (BDR) data set also composed of WAC filter 7 and NAC images acquired at moderate/high solar incidence angles centered near 68 degrees (changed to 74 degrees in the find end-of-mission data delivery), and an Low Incidence Angle (LOI) data set also composed of WAC filter 7 and NAC images acquired at lower incidence centered near 45 degrees, analogous to the geometry used for color imaging. The map is divided into 54 'tiles', each representing the NW, NE, SW, or SE quadrant of one of the 13 non-polar or one of the 2 polar quadrangles or 'Mercury charts' already defined by the USGS. Each tile also contains 5 backplanes: observation ID; BDR metric, a metric used to determine the stacking order of component images, modified for the higher incidence angle centered near 78 degrees; solar incidence angle; emission angle; and phase angle.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mess-h-mdis-5-rdr-hiw-v1.0_rt2y-cn5j",
+            "issued": "2021-05-21",
+            "keyword": [
+                "messenger",
+                "mercury"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MESS-H-MDIS-5-RDR-HIW-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mess-h-mdis-5-rdr-hiw-v1.0_rt2y-cn5j",
-            "description": "Abstract ======== The Mercury Dual Imaging System (MDIS) consists of two cameras, a Wide Angle Camera (WAC) and a Narrow Angle Camera (NAC), mounted on a common pivot platform. This dataset includes Map Projected High- Incidence Angle Basemap Illuminated from the West RDRs (HIWs) which comprise a global map of I/F measured by the NAC or WAC filter 7 (both centered near 750 nm) during the the Extended Mission at high incidence angles to accentuate subtle topography, photometrically normalized to a solar incidence angle (i) = 30 degrees, emission angle (e) = 0 degrees, and phase angle (g) = 30 degrees at a spatial sampling of 256 pixels per degree. The HIW data set is a companion to the Map Projected High-Incidence Angle Basemap Illuminated from the East RDR (HIE) data set. Together the two data sets are intended to detect and allow the mapping of subtle topography. They complement a Basemap Data Record (BDR) data set also composed of WAC filter 7 and NAC images acquired at moderate/high solar incidence angles centered near 68 degrees (changed to 74 degrees in the find end-of-mission data delivery), and an Low Incidence Angle (LOI) data set also composed of WAC filter 7 and NAC images acquired at lower incidence centered near 45 degrees, analogous to the geometry used for color imaging. The map is divided into 54 'tiles', each representing the NW, NE, SW, or SE quadrant of one of the 13 non-polar or one of the 2 polar quadrangles or 'Mercury charts' already defined by the USGS. Each tile also contains 5 backplanes: observation ID; BDR metric, a metric used to determine the stacking order of component images, modified for the higher incidence angle centered near 78 degrees; solar incidence angle; emission angle; and phase angle.",
-            "title": "MESS MDIS MAP PROJ HIGH-INCIDENCE\n                                      BASEMAP WEST RDR V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "MESS MDIS MAP PROJ HIGH-INCIDENCE\n                                      BASEMAP WEST RDR V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/S3A/OLCI/L3B/ILW/4",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/GSFC/SED/ESD/GCDC/OB.DAAC. https://doi.org/10.5067/S3A/OLCI/L3B/ILW/4.",
-            "issued": "2022-09-13",
-            "temporal": "2016-04-25T00:00:00Z/2024-05-06T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-04-26",
-            "keyword": [
-                "bacteria/archaea",
-                "surface water",
-                "oceans",
-                "ocean optics",
-                "hydrological advisories",
-                "marine environment monitoring",
-                "water quality/water chemistry",
-                "aquatic sciences",
-                "biological classification",
-                "biosphere",
-                "coastal processes",
-                "human dimensions",
-                "environmental governance/management",
-                "earth science",
-                "terrestrial hydrosphere",
-                "environmental advisories",
-                "ecosystems",
-                "earth science services"
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
-            "identifier": "C2954424104-OB_DAAC",
             "description": "The Inland Waters dataset (ILW) provides data for lakes and other water bodies across the contiguous United States (CONUS) and Alaska. ILW significantly reduces the processing effort required by end users and is a standardized community resource for lake and reservoir algorithm development and performance assessment. The data is provided for 15,450 CONUS waterbodies with a size of at least one 300 m pixel and over 2,300 resolvable lakes with sizes greater than three 300 m pixels. Alaska has 5,874 lakes resolvable lakes. ILW was developed in collaboration with the Cyanobacteria Assessment Network (CyAN). Additional inland water details and resources, including maps of resolvable lakes and additional inland water products, such as true color imagery, are available at the CyAN site.",
-            "title": "Sentinel-3A OLCI Regional Binned Inland Waters (ILW) Data, version 4",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FS3A%2FOLCI%2FL3B%2FILW%2F4",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FS3A%2FOLCI%2FL3B%2FILW%2F4",
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
-                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/data/10.5067/S3A/OLCI/L3B/ILW/4",
-                    "description": "OLCI-Sentinel-3A 3B Inland Waters (ILW) Dataset Landing Page",
                     "@type": "dcat:Distribution",
+                    "description": "OLCI-Sentinel-3A 3B Inland Waters (ILW) Dataset Landing Page",
+                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/data/10.5067/S3A/OLCI/L3B/ILW/4",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 }
             ],
+            "identifier": "C2954424104-OB_DAAC",
+            "issued": "2022-09-13",
+            "keyword": [
+                "bacteria/archaea",
+                "surface water",
+                "oceans",
+                "ocean optics",
+                "hydrological advisories",
+                "marine environment monitoring",
+                "water quality/water chemistry",
+                "aquatic sciences",
+                "biological classification",
+                "biosphere",
+                "coastal processes",
+                "human dimensions",
+                "environmental governance/management",
+                "earth science",
+                "terrestrial hydrosphere",
+                "environmental advisories",
+                "ecosystems",
+                "earth science services"
+            ],
+            "landingPage": "https://doi.org/10.5067/S3A/OLCI/L3B/ILW/4",
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
+            "title": "Sentinel-3A OLCI Regional Binned Inland Waters (ILW) Data, version 4"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1213928209-ASF.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, ASF.",
-            "issued": "2012-02-20",
-            "temporal": "1993-06-08T00:00:00Z/2004-12-04T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2012-02-20",
-            "keyword": [
-                "nasa"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "undefined",
                 "hasEmail": "mailto:uso@asf.alaska.edu"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "ASF"
-            },
-            "identifier": "C1213928209-ASF",
             "description": "AIRSAR topographic SAR digital elevation model P_Stokes product",
-            "title": "AIRSAR_TOPSAR_P-BAND_STOKES",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://vertex.daac.asf.alaska.edu/",
-                    "description": "Vertex, the ASF search and download interface",
                     "@type": "dcat:Distribution",
+                    "description": "Vertex, the ASF search and download interface",
+                    "downloadURL": "https://vertex.daac.asf.alaska.edu/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 }
             ],
+            "identifier": "C1213928209-ASF",
+            "issued": "2012-02-20",
+            "keyword": [
+                "nasa"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1213928209-ASF.html",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2012-02-20",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "ASF"
+            },
             "spatial": "<?xml version=\"1.0\" encoding=\"UTF-8\"?><gml:Polygon xmlns:gml=\"http://www.opengis.net/gml/3.2\" srsName=\"EPSG:4326\"><gml:outerBoundaryIs><gml:LinearRing><gml:posList>-26.198199 -143.26613 -23.096323 -62.958179 -18.867366 -62.30596 69.178089 -49.704356 69.25925 -49.871916 64.601354 -147.320616 64.503195 -147.324715 -27.021632 -172.880269 -27.388834 -172.532316 -26.198199 -143.26613</gml:posList></gml:LinearRing></gml:outerBoundaryIs><gml:innerBoundaryIs></gml:innerBoundaryIs></gml:Polygon>",
+            "temporal": "1993-06-08T00:00:00Z/2004-12-04T23:59:59Z",
             "theme": [
                 "St. Charles, MO",
                 "Web County, TX",
@@ -1321520,41 +1321521,22 @@
                 "Uthai Thani, Thailand",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "AIRSAR_TOPSAR_P-BAND_STOKES"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.nasa.gov/d/rt5y-hsd7",
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
-                "nen",
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
-            "identifier": "NASA-0000038__76",
+            "describedBy": "http://planetarynames.wr.usgs.gov/Page/Website",
             "description": "Planetary nomenclature, like terrestrial nomenclature, is used to uniquely identify a feature on the surface of a planet or satellite so that the feature can be easily located, described, and discussed. This gazetteer contains detailed information about all names of topographic and albedo features on planets and satellites (and some planetary ring and ring-gap systems) that the International Astronomical Union (IAU) has named and approved from its founding in 1919 through the present time.",
-            "title": "Gazetteer of Planetary Nomenclature",
-            "programCode": [
-                "026:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -1321562,1350 +1321544,1370 @@
                     "mediaType": "application/vnd.google-earth.kmz"
                 }
             ],
-            "describedBy": "http://planetarynames.wr.usgs.gov/Page/Website",
-            "accrualPeriodicity": "irregular"
+            "identifier": "NASA-0000038__76",
+            "issued": "2018-06-25",
+            "keyword": [
+                "wise",
+                "nen",
+                "space science",
+                "geography"
+            ],
+            "landingPage": "https://data.nasa.gov/d/rt5y-hsd7",
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
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/34",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Weaver, H. L. 1994. Eddy Corr[elation]. Surface Flux: USGS (FIFE). Data set. Available on-line [http://www.daac.ornl.gov] from Oak Ridge National Laboratory Distributed Active Archive Center, Oak Ridge, Tennessee, U.S.A. Also published in D. E. Strebel, D. R. Landis, K. F. Huemmrich, and B. W. Meeson (eds.), Collected Data of the First ISLSCP Field Experiment, Vol. 1: Surface Observations and Non-Image Data Sets. CD-ROM. National Aeronautics and Space Administration, Goddard Space Flight Center, Greenbelt, Maryland, U.S.A. (available from http://www.daac.ornl.gov). doi:10.3334/ORNLDAAC/34",
-            "issued": "2024-05-05",
-            "temporal": "1987-05-25T00:00:00Z/1987-10-17T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-07",
-            "keyword": [
-                "atmospheric winds",
-                "atmospheric water vapor",
-                "atmospheric radiation",
-                "earth science",
-                "atmosphere",
-                "agriculture",
-                "land surface",
-                "soils",
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
-            "identifier": "C2980065160-ORNL_CLOUD",
             "description": "FIFE observations of surface fluxes",
-            "graphic-preview-description": "Browse Image",
-            "title": "Eddy Corr. Surface Flux: USGS (FIFE)",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/fife_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F34",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F34",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/fife/fife_sur_flux_30_min_ecw/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/fife/fife_sur_flux_30_min_ecw/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/FIFE/guides/Eddy_Correlation_USGS.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/FIFE/guides/Eddy_Correlation_USGS.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/34",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/34",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/fife/fife_sur_flux_30_min_ecw/comp/Eddy_Correlation_USGS.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/fife/fife_sur_flux_30_min_ecw/comp/Eddy_Correlation_USGS.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/msword",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/fife/fife_sur_flux_30_min_ecw/comp/sflux_ew.doc",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/fife/fife_sur_flux_30_min_ecw/comp/sflux_ew.doc",
+                    "mediaType": "application/msword",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/fife/fife_sur_flux_30_min_ecw/comp/sf_30min.tdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/fife/fife_sur_flux_30_min_ecw/comp/sf_30min.tdf",
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
+            "identifier": "C2980065160-ORNL_CLOUD",
+            "issued": "2024-05-05",
+            "keyword": [
+                "atmospheric winds",
+                "atmospheric water vapor",
+                "atmospheric radiation",
+                "earth science",
+                "atmosphere",
+                "agriculture",
+                "land surface",
+                "soils",
+                "atmospheric temperature"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/34",
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
+            "temporal": "1987-05-25T00:00:00Z/1987-10-17T23:59:59Z",
             "theme": [
                 "FIFE",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Eddy Corr. Surface Flux: USGS (FIFE)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RPCLAP-2-ESC4-MTP023-V1.0",
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
+            "description": "This dataset contains EDITED data from Rosetta RPC-LAP, acquired during MTP23 of the COMET ESCORT 4 mission phase. The primary target observed was comet 67P/C-G.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rpclap-2-esc4-mtp023-v1.0_rtay-tr22",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RPCLAP-2-ESC4-MTP023-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rpclap-2-esc4-mtp023-v1.0_rtay-tr22",
-            "description": "This dataset contains EDITED data from Rosetta RPC-LAP, acquired during MTP23 of the COMET ESCORT 4 mission phase. The primary target observed was comet 67P/C-G.",
-            "title": "ROSETTA-ORBITER 67P RPCLAP 2 ESC4\n        MTP023 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RPCLAP 2 ESC4\n        MTP023 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/IMPACTS/NEXRAD/DATA113",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Brodzik, Stacy .2022. KFCX NEXRAD IMPACTS [indicate subset used]. Dataset available online from the NASA Global Hydrometeorology Resource Center DAAC, Huntsville, Alabama, U.S.A. DOI: http://dx.doi.org/10.5067/IMPACTS/NEXRAD/DATA113",
-            "issued": "2022-03-23",
-            "temporal": "2020-01-01T00:09:50Z/2020-03-01T00:02:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-31",
-            "keyword": [
-                "spectral/engineering",
-                "earth science",
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
-            "identifier": "C2025222404-GHRC_DAAC",
             "description": "The KFCX NEXRAD IMPACTS dataset consists of Next Generation Weather Radar (NEXRAD) Level II surveillance data that were collected at 31 NEXRAD sites from January 1 to March 1, 2020 during the Investigation of Microphysics and Precipitation for Atlantic Coast-Threatening Snowstorms  (IMPACTS) field campaign. IMPACTS was a three-year sequence of winter season deployments conducted to study snowstorms over the U.S Atlantic Coast. The campaign aimed to (1) Provide observations critical to understanding the mechanisms of snowband formation, organization, and evolution; (2) Examine how the microphysical characteristics and likely growth mechanisms of snow particles vary across snowbands; and (3) Improve snowfall remote sensing interpretation and modeling to significantly advance prediction capabilities. There are currently 160 Weather Surveillance Radar-1988 Doppler (WSR-88D) or NEXRAD sites throughout the United States and abroad. These Level II datasets contain meteorological and dual-polarization base data quantities including: radar reflectivity, radial velocity, spectrum width, differential reflectivity, differential phase, and cross correlation ratio. The IMPACTS NEXRAD Level II data files are available in netCDF-4 format. It should be noted that this dataset will be updated in subsequent years of the IMPACTS campaign.",
-            "title": "KFCX NEXRAD IMPACTS V1",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FIMPACTS%2FNEXRAD%2FDATA113",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FIMPACTS%2FNEXRAD%2FDATA113",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=kfcximpacts",
-                    "description": "Files may be downloaded directly to your workstation from this link",
                     "@type": "dcat:Distribution",
+                    "description": "Files may be downloaded directly to your workstation from this link",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=kfcximpacts",
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
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/impacts/NEXRAD/KFCX/doc/nexrad_datasets.pdf",
-                    "description": "NEXRAD IMPACTS User Guide",
                     "@type": "dcat:Distribution",
+                    "description": "NEXRAD IMPACTS User Guide",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/impacts/NEXRAD/KFCX/doc/nexrad_datasets.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
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
+            "identifier": "C2025222404-GHRC_DAAC",
+            "issued": "2022-03-23",
+            "keyword": [
+                "spectral/engineering",
+                "earth science",
+                "radar"
+            ],
+            "landingPage": "https://doi.org/10.5067/IMPACTS/NEXRAD/DATA113",
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
             "spatial": "-85.449 32.895 -75.099 41.154",
+            "temporal": "2020-01-01T00:09:50Z/2020-03-01T00:02:00Z",
             "theme": [
                 "IMPACTS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "KFCX NEXRAD IMPACTS V1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/Not Applicable",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2008-10-03. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/Not Applicable. https://asdc.larc.nasa.gov/project/MISR.",
-            "issued": "2007-06-12",
-            "temporal": "2007-07-01T00:00:00Z/2024-03-27T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2019-06-19",
-            "keyword": [
-                "atmosphere",
-                "earth science",
-                "land surface",
-                "land use/land cover",
-                "atmospheric radiation",
-                "vegetation",
-                "biosphere"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "DAVID, DR. DINER",
                 "hasEmail": "mailto:david.j.diner@jpl.nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/LARC/SD/ASDC"
-            },
-            "identifier": "C156141677-LARC",
             "description": "MI3MLSNF_2 is the Multi-angle Imaging SpectroRadiometer (MISR) Level 3 FIRSTLOOK Global Land product in netCDF format covering a month version 2 data product. It contains a monthly statistical summary of directional hemispherical reflectance (DHR), photosynthetically active spectral region (DHR-PAR), DHR for near-infrared band (DHR-NIR), fractional absorbed photosynthetically active radiation (FPAR), DHR-based normalized difference vegetation index (NDVI) and land surface bidirectional reflectance factor (BRF) model parameters. It is classified into six vegetated and one non-vegetated types. This data product is a global summary of the Level 2 land/surface parameters of interest averaged over a month and reported on a geographic grid, with resolution of 0.5 degree by 0.5 degree. Data collection for this product is ongoing. This collection contains Leaf Area Index (LAI).\r\rFIRSTLOOK processing uses the new time dependence of the Atmospheric and Surface Climatology (TASC) from the same month/previous year. The TASC data set now contains snow-ice and ocean surface wind speed values that are updated on a monthly basis. Therefore, these data sets cannot be generated until the end of the month. Products generated are distinguished by the presence of FIRSTLOOK in the file names. The MISR instrument consists of nine pushbroom cameras which measure radiance in four spectral bands. Global coverage is achieved in nine days. The cameras are arranged with one camera pointing toward the nadir, four cameras pointing forward, and four cameras pointing aftward. It takes seven minutes for all nine cameras to view the same surface location. The view angles relative to the surface reference ellipsoid, are 0, 26.1, 45.6, 60.0, and 70.5 degrees. The spectral band shapes are nominally Gaussian, centered at 443, 555, 670, and 865 nm.\r\rMISR itself is an instrument designed to view Earth with cameras pointed in 9 different directions. As the instrument flies overhead, each piece of Earth's surface below is successively imaged by all 9 cameras, in each of 4 wavelengths (blue, green, red, and near-infrared). The goal of MISR is to improve our understanding of the affects of sunlight on Earth, as well as distinguish different types of clouds, particles and surfaces. Specifically, MISR monitors the monthly, seasonal, and long-term trends in three areas: 1) amount and type of atmospheric particles (aerosols), including those formed by natural sources and by human activities; 2) amounts, types, and heights of clouds, and 3) distribution of land surface cover, including vegetation canopy structure.",
-            "graphic-preview-description": "ASDC List of MISR Imagery and Articles",
-            "title": "MISR Level 3 FIRSTLOOK Global Land product in netCDF format covering a month V002",
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
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C156141677-LARC",
-                    "description": "Earthdata Search for MI3MLSNF_2 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for MI3MLSNF_2 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C156141677-LARC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/MISR/MI3MLSNF.002/contents.html",
-                    "description": "OPeNDAP data access for MI3MLSNF_2",
                     "@type": "dcat:Distribution",
+                    "description": "OPeNDAP data access for MI3MLSNF_2",
+                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/MISR/MI3MLSNF.002/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/misr/quality_summaries/L3_Products.pdf",
-                    "description": "MISR Level 3 Component Products Quality Statement - December 1, 2005",
                     "@type": "dcat:Distribution",
+                    "description": "MISR Level 3 Component Products Quality Statement - December 1, 2005",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/misr/quality_summaries/L3_Products.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's product quality assessment"
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
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/MISR/MI3MLSNF.002/",
-                    "description": "ASDC Direct Data Download for MI3MLSNF_2",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for MI3MLSNF_2",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/MISR/MI3MLSNF.002/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
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
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/misr/version/pge12c.html",
-                    "description": "ASDC overview of MISR Level 3 Land Surface and Aerosol Versioning",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC overview of MISR Level 3 Land Surface and Aerosol Versioning",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/misr/version/pge12c.html",
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
+            "identifier": "C156141677-LARC",
+            "issued": "2007-06-12",
+            "keyword": [
+                "atmosphere",
+                "earth science",
+                "land surface",
+                "land use/land cover",
+                "atmospheric radiation",
+                "vegetation",
+                "biosphere"
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
+            "temporal": "2007-07-01T00:00:00Z/2024-03-27T00:00:00Z",
             "theme": [
                 "MISR",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "MISR Level 3 FIRSTLOOK Global Land product in netCDF format covering a month V002"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://c3.nasa.gov/dashlink/resources/375/",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2011-05-16",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
-            "keyword": [
-                "ames",
-                "dashlink",
-                "nasa"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Marilyn Smith",
                 "hasEmail": "mailto:marilyn.smith@ae.gatech.edu"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Dashlink"
-            },
-            "identifier": "DASHLINK_375",
             "description": "This is the RSW Mixed Element Unstructured Fine Grid Set.",
-            "title": "RSW Mixed Element Fine Grid",
-            "programCode": [
-                "026:029"
-            ],
             "distribution": [
                 {
-                    "mediaType": "application/octet-stream",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/rswf_fine_2.mapbc",
-                    "description": "mapbc file (FUN3D)",
                     "@type": "dcat:Distribution",
+                    "description": "mapbc file (FUN3D)",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/rswf_fine_2.mapbc",
+                    "mediaType": "application/octet-stream",
                     "title": "rswf_fine.mapbc"
                 },
                 {
-                    "mediaType": "application/octet-stream",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/rswf_fine_2.surf",
-                    "description": "surface file",
                     "@type": "dcat:Distribution",
+                    "description": "surface file",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/rswf_fine_2.surf",
+                    "mediaType": "application/octet-stream",
                     "title": "rswf_fine.surf"
                 },
                 {
-                    "mediaType": "application/octet-stream",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/rswf_fine.ugrid",
-                    "description": "ugrid file",
                     "@type": "dcat:Distribution",
+                    "description": "ugrid file",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/rswf_fine.ugrid",
+                    "mediaType": "application/octet-stream",
                     "title": "rswf_fine.ugrid"
                 }
             ],
-            "accrualPeriodicity": "irregular"
+            "identifier": "DASHLINK_375",
+            "issued": "2011-05-16",
+            "keyword": [
+                "ames",
+                "dashlink",
+                "nasa"
+            ],
+            "landingPage": "https://c3.nasa.gov/dashlink/resources/375/",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:029"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Dashlink"
+            },
+            "title": "RSW Mixed Element Fine Grid"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC1-0487-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 1 phase 2014-11-20 to 2015-03-10. It is a Global Gravity measurement at the comet 67P and covers the time 2014-12-13T04:19:20.000 to 2014-12-13T12:37:14.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc1-0487-v1.0_rtfn-uimh",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC1-0487-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc1-0487-v1.0_rtfn-uimh",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 1 phase 2014-11-20 to 2015-03-10. It is a Global Gravity measurement at the comet 67P and covers the time 2014-12-13T04:19:20.000 to 2014-12-13T12:37:14.000.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 1 0487 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 1 0487 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1254",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Salas, W.A., D.S. Alves, M.J. Ducey, D.J. Zarin, and J. Qi. 2014. LBA-ECO CD-17 Secondary Forest Survey, Para and Rondonia, Brazil: 2002-2003. ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/1254",
-            "issued": "2023-10-03",
-            "temporal": "1997-07-13T00:00:00Z/2003-11-01T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-10-12",
-            "keyword": [
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
-            "identifier": "C2781621763-ORNL_CLOUD",
             "description": "This data set provides measurements for diameter at breast height (DBH), tree height, distance from tree stems to the furthest canopy element, and a species survey of secondary forests in Para and Rondonia, Brazil, from 2002-2003. The forest areas were defined as Type A and Type B stands. Measurements were made in the overstory, understory, and midstory of each stand. Type A stands were sampled intensively, with the goal of providing high-fidelity spatial information about the 3-dimensional structure of the stand. These stands were 60 x 60-m (0.36-ha) areas divided into 10 x 10-m grids of uniform clearing and abandonment history and were identifiable from Landsat images. Type B stands were sampled extensively, with the goal of providing unbiased estimates of biomass, along with some information about the vertical structure of the stand and of spatial variability. These stands were polygons of uniform clearing and afforestation history based on multitemporal Landsat imagery, and varied in size and shape. The Landsat files provide classified land cover for each scene and can be used as a time series to evaluate land cover change over time. Each Landsat file is a geolocated land cover map based on 30-m Landsat data. NOTE: There were additional files which could not be archived due to file problems. Data Quality Statement: The Data Center has determined that this data set has missing or incomplete data, metadata, or other documentation resulting in diminished usability of this product. Known Problems: Some unresolved issues remain where data values are inconsistent with the variable descriptions provided with the data set. The site identification and plot identification values are not consistently used in all three data files. The variables are not adequately described.",
-            "graphic-preview-description": "Browse Image",
-            "title": "LBA-ECO CD-17 Secondary Forest Survey, Para and Rondonia, Brazil: 2002-2003",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/lba_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1254",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1254",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/lba/grab_bag/CD17_Forest_Survey/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/lba/grab_bag/CD17_Forest_Survey/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/LBA/guides/CD17_Forest_Survey.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/LBA/guides/CD17_Forest_Survey.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1254",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1254",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/grab_bag/CD17_Forest_Survey/comp/CD17_Forest_Survey.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/grab_bag/CD17_Forest_Survey/comp/CD17_Forest_Survey.pdf",
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
+            "identifier": "C2781621763-ORNL_CLOUD",
+            "issued": "2023-10-03",
+            "keyword": [
+                "biosphere",
+                "earth science",
+                "vegetation"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1254",
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
             "spatial": "-63.33 -9.69 -47.75 -1.67",
+            "temporal": "1997-07-13T00:00:00Z/2003-11-01T23:59:59Z",
             "theme": [
                 "LBA-ECO",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "LBA-ECO CD-17 Secondary Forest Survey, Para and Rondonia, Brazil: 2002-2003"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://landslides.nasa.gov",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2018-04-02",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
-            "keyword": [
-                "hazards",
-                "citizen science",
-                "landslide",
-                "mudslide",
-                "earth"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Dalia B. Kirschbaum",
                 "hasEmail": "mailto:dalia.b.kirschbaum@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Aeronautics and Space Administration"
-            },
-            "identifier": "Global-Landslide-Catalog-Export",
             "description": "The Global Landslide Catalog (GLC) was developed with the goal of identifying rainfall-triggered landslide events around the world, regardless of size, impacts or location. The GLC considers all types of mass movements triggered by rainfall, which have been reported in the media, disaster databases, scientific reports, or other sources. The GLC has been compiled since 2007 at NASA Goddard Space Flight Center. This is a unique data set with the ID tag \u201cGLC\u201d in the landslide editor. This dataset on data.nasa.gov was a one-time export from the Global Landslide Catalog maintained separately. It is current as of March 7, 2016. The original catalog is available here: http://www.arcgis.com/home/webmap/viewer.html?url=https%3A%2F%2Fmaps.nccs.nasa.gov%2Fserver%2Frest%2Fservices%2Fglobal_landslide_catalog%2Fglc_viewer_service%2FFeatureServer&source=sd. To export GLC data, you must agree to the \u201cTerms and Conditions\u201d. We request that anyone using the GLC cite the two sources of this database: Kirschbaum, D. B., Adler, R., Hong, Y., Hill, S., & Lerner-Lam, A. (2010). A global landslide catalog for hazard applications: method, results, and limitations. Natural Hazards, 52(3), 561\u2013575. doi:10.1007/s11069-009-9401-4. [1] Kirschbaum, D.B., T. Stanley, Y. Zhou (In press, 2015). Spatial and Temporal Analysis of a Global Landslide Catalog. Geomorphology. doi:10.1016/j.geomorph.2015.03.016. [2]",
-            "title": "Global Landslide Catalog Export",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
```

