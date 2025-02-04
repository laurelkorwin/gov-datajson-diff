# Change History for nasa.json (Part 77)

### Changes from 31606f9 to dd2190f (Part 66/162)
**Author:** Automated

**Date:** 2025-02-01 15:02:16+00:00

**Message:** Updated data: Sat Feb  1 15:02:16 UTC 2025

```diff
+            "description": "APXS, ChemCam, DAN, Hazcam, MAHLI, MARDI, Mastcam, Navcam, RAD, REMS, SPICE, SAM",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://pds.jpl.nasa.gov/tools/subscription_service/SS-20130830.shtml",
+                    "mediaType": "application/html"
+                }
             ],
+            "identifier": "NASA-470",
+            "issued": "2018-06-25",
             "keyword": [
                 "apxs",
                 "spice",
@@ -686218,70 +686227,37 @@
                 "hazcam",
                 "dan"
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
-            "identifier": "NASA-470",
-            "description": "APXS, ChemCam, DAN, Hazcam, MAHLI, MARDI, Mastcam, Navcam, RAD, REMS, SPICE, SAM",
-            "title": "PDS Mars  Science Laboratory Data Release 3",
-            "programCode": [
-                "026:005"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://pds.jpl.nasa.gov/tools/subscription_service/SS-20130830.shtml",
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
+            "title": "PDS Mars  Science Laboratory Data Release 3"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1332654097-GES_DISC.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Tropical Rainfall Measuring Mission (TRMM). 2007-01-01. TRMM_2A54. TRMM Ground Validation Radar Site Rain Type Map L2 1 hour 2 km V7. Greenbelt, MD. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://disc.gsfc.nasa.gov/datacollection/TRMM_2A54_7.html.",
-            "issued": "2011-07-01",
-            "temporal": "1997-11-27T00:00:00Z/2014-12-31T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2016-05-09",
-            "keyword": [
-                "radar",
-                "spectral/engineering",
-                "precipitation",
-                "atmosphere",
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
-            "identifier": "C1332654097-GES_DISC",
-            "description": "'Radar Site Convective/Stratiform Map', is an instantaneous map in Cartesian coordinates with a 2 km resolution. At single radar sites, the map covers an area of 300 km x 300 km. For the multiple radar site in Texas, the map covers a region of 724 km x 568 km, and in Florida 512 km x 704 km. The map identifies the surface precipitation as convective or stratiform. \n\nA key component of the TRMM project is the Ground Validation (GV) effort which consists of collecting data from ground-based radar, rain gauges and disdrometers. The data is quality-controlled, and then validation products are produced for comparison with TRMM satellite products.\n\nThe four primary GV sites are:\n\n+ Darwin, Australia; \n+ Houston, Texas; \n+ Kwajalein, Republic of the Marshall Islands;\n+ Melbourne, Florida. \n\nA significant effort is also being supported at NASA Wallops Flight Facility (WFF) and vicinity to provide high quality, long-term measurements of rain rates (via a network of rain gauges collocated with National Weather Service gauges), as well as drop size distributions (DSD) using a variety of instruments, including impact-type Joss Waldvogel, laser-optical Parsivel, as well as two-dimensional video disdrometers.  DSD measurements are also being collected at Melbourne and Kwajalein using Joss-Waldvogel disdrometers.",
-            "release-place": "Greenbelt, MD",
-            "series-name": "TRMM_2A54",
             "creator": "Tropical Rainfall Measuring Mission (TRMM)",
-            "title": "TRMM Ground Validation Radar Site Rain Type Map L2 1 hour 2 km V7 (TRMM_2A54) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/GPM/browse/2A54_BR.081016.15.HSTN.5.PNG",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "'Radar Site Convective/Stratiform Map', is an instantaneous map in Cartesian coordinates with a 2 km resolution. At single radar sites, the map covers an area of 300 km x 300 km. For the multiple radar site in Texas, the map covers a region of 724 km x 568 km, and in Florida 512 km x 704 km. The map identifies the surface precipitation as convective or stratiform. \n\nA key component of the TRMM project is the Ground Validation (GV) effort which consists of collecting data from ground-based radar, rain gauges and disdrometers. The data is quality-controlled, and then validation products are produced for comparison with TRMM satellite products.\n\nThe four primary GV sites are:\n\n+ Darwin, Australia; \n+ Houston, Texas; \n+ Kwajalein, Republic of the Marshall Islands;\n+ Melbourne, Florida. \n\nA significant effort is also being supported at NASA Wallops Flight Facility (WFF) and vicinity to provide high quality, long-term measurements of rain rates (via a network of rain gauges collocated with National Weather Service gauges), as well as drop size distributions (DSD) using a variety of instruments, including impact-type Joss Waldvogel, laser-optical Parsivel, as well as two-dimensional video disdrometers.  DSD measurements are also being collected at Melbourne and Kwajalein using Joss-Waldvogel disdrometers.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -686290,73 +686266,111 @@
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/TRMM_2A54_7.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/TRMM_2A54_7.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc2.gesdisc.eosdis.nasa.gov/data/TRMM_GV_L2/TRMM_2A54.7",
-                    "description": "Access the data via HTTPS",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS",
+                    "downloadURL": "https://disc2.gesdisc.eosdis.nasa.gov/data/TRMM_GV_L2/TRMM_2A54.7",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=TRMM_2A54",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=TRMM_2A54",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://trmm-fc.gsfc.nasa.gov/trmm_gv/",
-                    "description": "TRMM Project Home Page",
                     "@type": "dcat:Distribution",
+                    "description": "TRMM Project Home Page",
+                    "downloadURL": "https://trmm-fc.gsfc.nasa.gov/trmm_gv/",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://pps.gsfc.nasa.gov/Documents/ICSVol4.pdf",
-                    "description": "File specification document",
                     "@type": "dcat:Distribution",
+                    "description": "File specification document",
+                    "downloadURL": "https://pps.gsfc.nasa.gov/Documents/ICSVol4.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View the primary investigator's documentation for this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://trmm-fc.gsfc.nasa.gov/",
-                    "description": "TRMM Field Campaign Project Page",
                     "@type": "dcat:Distribution",
+                    "description": "TRMM Field Campaign Project Page",
+                    "downloadURL": "https://trmm-fc.gsfc.nasa.gov/",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
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
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/GPM/browse/2A54_BR.081016.15.HSTN.5.PNG",
+            "identifier": "C1332654097-GES_DISC",
+            "issued": "2011-07-01",
+            "keyword": [
+                "radar",
+                "spectral/engineering",
+                "precipitation",
+                "atmosphere",
+                "earth science"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1332654097-GES_DISC.html",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2016-05-09",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
+            },
+            "release-place": "Greenbelt, MD",
+            "series-name": "TRMM_2A54",
             "spatial": "-180.0 -40.0 180.0 40.0",
+            "temporal": "1997-11-27T00:00:00Z/2014-12-31T23:59:59.999Z",
             "theme": [
                 "TRMM",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "TRMM Ground Validation Radar Site Rain Type Map L2 1 hour 2 km V7 (TRMM_2A54) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.nasa.gov/d/e774-t35i",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "GeneLab Outreach",
+                "hasEmail": "mailto:genelab-outreach@lists.nasa.gov"
+            },
+            "description": "Genomic and proteomic characterization of the Aspergillus niger isolate JSC-093350089 collected from U.S. segment surfaces of the International Space Station (ISS) is reported along with a comparison to the experimentally established strain ATCC 1015. Whole-genome sequencing of JSC-093350089 revealed enhanced genetic variance when compared to publicly available sequences of A. niger strains. Analysis of the isolate xe2 x80 x9a xc3 x84 xc3 xb4s proteome revealed significant differences in the molecular phenotype of JSC-093350089 including increased abundance of proteins involved in the A. niger starvation response oxidative stress resistance cell wall integrity and modulation and nutrient acquisition. Together these data reveal the existence of a distinct strain of A. niger onboard the ISS and provide insight into the molecular phenotype that is selected for by melanized fungal species inhabiting spacecraft environments.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "GeneLab Study Page",
+                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-260",
+                    "mediaType": "text/html",
+                    "title": "Genomic and Proteomic characterization of Aspergillus niger isolated from the International Space Station"
+                }
+            ],
+            "identifier": "nasa_genelab_GLDS-260_e774-t35i",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
             "keyword": [
                 "mass spectrometry",
                 "data transformation",
@@ -686367,2448 +686381,2443 @@
                 "spaceflight",
                 "labeling"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "GeneLab Outreach",
-                "hasEmail": "mailto:genelab-outreach@lists.nasa.gov"
-            },
+            "landingPage": "https://data.nasa.gov/d/e774-t35i",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "nasa_genelab_GLDS-260_e774-t35i",
-            "description": "Genomic and proteomic characterization of the Aspergillus niger isolate JSC-093350089 collected from U.S. segment surfaces of the International Space Station (ISS) is reported along with a comparison to the experimentally established strain ATCC 1015. Whole-genome sequencing of JSC-093350089 revealed enhanced genetic variance when compared to publicly available sequences of A. niger strains. Analysis of the isolate xe2 x80 x9a xc3 x84 xc3 xb4s proteome revealed significant differences in the molecular phenotype of JSC-093350089 including increased abundance of proteins involved in the A. niger starvation response oxidative stress resistance cell wall integrity and modulation and nutrient acquisition. Together these data reveal the existence of a distinct strain of A. niger onboard the ISS and provide insight into the molecular phenotype that is selected for by melanized fungal species inhabiting spacecraft environments.",
-            "title": "Genomic and Proteomic characterization of Aspergillus niger isolated from the International Space Station",
-            "programCode": [
-                "026:005"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-260",
-                    "description": "GeneLab Study Page",
-                    "@type": "dcat:Distribution",
-                    "title": "Genomic and Proteomic characterization of Aspergillus niger isolated from the International Space Station"
-                }
-            ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "Genomic and Proteomic characterization of Aspergillus niger isolated from the International Space Station"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-PRL-0416-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the PRELANDING phase 2014-01-21 to 2014-11-18. It is a Global Gravity measurement at the comet 67P and covers the time 2014-11-08T14:57:05.000 to 2014-11-08T20:53:19.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-prl-0416-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-PRL-0416-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-prl-0416-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the PRELANDING phase 2014-01-21 to 2014-11-18. It is a Global Gravity measurement at the comet 67P and covers the time 2014-11-08T14:57:05.000 to 2014-11-08T20:53:19.000.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     PRELANDING 0416 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     PRELANDING 0416 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-4-ESC3-67P-M20-STRLIGHT-V1.0",
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
+            "description": "This CODMAC level 4 data set contains solar stray light corrected, radiometric calibrated and geometric distortion corrected (resampled) image data in W/m^2/sr/nm, acquired by the OSIRIS Wide Angle Camera on the Rosetta spacecraft during the COMET ESCORT 3 mission phase, covering the period from 2015-08-25T23:25:00.000 to 2015-09-22T23:24:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V1.0 is the first version of this dataset: Lien corrected dataset after October 2018 PSA/PDS external peer review.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-4-esc3-67p-m20-strlight-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-4-ESC3-67P-M20-STRLIGHT-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-4-esc3-67p-m20-strlight-v1.0",
-            "description": "This CODMAC level 4 data set contains solar stray light corrected, radiometric calibrated and geometric distortion corrected (resampled) image data in W/m^2/sr/nm, acquired by the OSIRIS Wide Angle Camera on the Rosetta spacecraft during the COMET ESCORT 3 mission phase, covering the period from 2015-08-25T23:25:00.000 to 2015-09-22T23:24:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V1.0 is the first version of this dataset: Lien corrected dataset after October 2018 PSA/PDS external peer review.",
-            "title": "ROSETTA-ORBITER 67P OSIWAC 4 ESC3-MTP020 RDR-STRLIGHT V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P OSIWAC 4 ESC3-MTP020 RDR-STRLIGHT V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1113",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Deegan, L.A., C. Neill, S.M. Thomas, A.V. Krusche, M.V.R. Ballester, and R.L. Victoria. 2012. LBA-ECO ND-03 Stream and Soil Water Data, Fazenda Nova Vida, Rondonia: 1994-2001 . ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/1113",
-            "issued": "2023-10-03",
-            "temporal": "1994-04-24T00:00:00Z/2001-09-12T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-10-11",
-            "keyword": [
-                "earth science",
-                "surface water",
-                "ground water",
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
-            "identifier": "C2780901460-ORNL_CLOUD",
             "description": "This data set provides the results of (1) the physical and chemical characterization of streams and (2) comparable chemical analyses of extracted soil water in the Aldeia River basin at Fazenda Nova Vida, a large cattle ranch 50 km from the city of Ariquemes, in central Rondonia, Brazil, from 1994-2001. Data are provided on the stream beds including cross-sectional depth and stream bed surface type. Stream discharge is reported. Streamwater was sampled and analyzed periodically over the eight year duration of the study at numerous steam locations. Soil solution samples were collected at the same frequency with lysimeters placed at 30 cm and 100 cm depths on the floodplain and at upland forest and pasture sites in the Aldeia River watershed. There are five comma-delimited data files in this data set.",
-            "graphic-preview-description": "Browse Image",
-            "title": "LBA-ECO ND-03 Stream and Soil Water Data, Fazenda Nova Vida, Rondonia: 1994-2001",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/lba_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1113",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1113",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/lba/nutrient_dynamics/ND03_Streams_Soilwater/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/lba/nutrient_dynamics/ND03_Streams_Soilwater/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/LBA/guides/ND03_Streams_Soilwater.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/LBA/guides/ND03_Streams_Soilwater.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1113",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1113",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/nutrient_dynamics/ND03_Streams_Soilwater/comp/ND03_Streams_Soilwater.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/nutrient_dynamics/ND03_Streams_Soilwater/comp/ND03_Streams_Soilwater.pdf",
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
+            "identifier": "C2780901460-ORNL_CLOUD",
+            "issued": "2023-10-03",
+            "keyword": [
+                "earth science",
+                "surface water",
+                "ground water",
+                "terrestrial hydrosphere"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1113",
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
             "spatial": "-10.16 -62.81",
+            "temporal": "1994-04-24T00:00:00Z/2001-09-12T23:59:59Z",
             "theme": [
                 "LBA-ECO",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "LBA-ECO ND-03 Stream and Soil Water Data, Fazenda Nova Vida, Rondonia: 1994-2001"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://c3.nasa.gov/dashlink/resources/282/",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2010-12-22",
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
-            "identifier": "DASHLINK_282",
             "description": "Multivariate Time-Series (MTS) are ubiquitous, and are generated in areas as disparate as sensor recordings in aerospace systems, music and video streams, medical monitoring, and financial systems. Domain experts are often interested in searching for interesting multivariate patterns from these MTS databases which can contain up to several gigabytes of data. Surprisingly, research on MTS search is very limited. Most existing work only supports queries with the same length of data, or queries on a fixed set of variables. In this paper, we propose an efficient and flexible subsequence search framework for massive MTS databases, that, for the first time, enables querying on any subset of variables with arbitrary time delays between them. We propose two provably correct algorithms to solve this problem \u2014 (1) an R-tree Based Search (RBS) which uses Minimum Bounding Rectangles (MBR) to organize the subsequences, and (2) a List Based Search (LBS) algorithm which uses sorted lists for indexing. We demonstrate the performance of these algorithms using two large MTS databases from the aviation domain, each containing several millions of observations. Both these tests show that our algorithms have very high prune rates (>95%) thus needing actual disk access for only less than 5% of the observations. To the best of our knowledge, this is the first flexible MTS search algorithm capable of subsequence search on any subset of variables. Moreover, MTS subsequence search has never been attempted on datasets of the size we have used in this paper.",
-            "title": "Fast and Flexible Multivariate Time Series Subsequence Search",
-            "programCode": [
-                "026:029"
-            ],
             "distribution": [
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/publication/mts_paper_2.pdf",
-                    "description": "mts_paper.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "mts_paper.pdf",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/publication/mts_paper_2.pdf",
+                    "mediaType": "application/pdf",
                     "title": "mts_paper.pdf"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/publication/supplemental_2.pdf",
-                    "description": "supplemental.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "supplemental.pdf",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/publication/supplemental_2.pdf",
+                    "mediaType": "application/pdf",
                     "title": "supplemental.pdf"
                 }
             ],
-            "accrualPeriodicity": "irregular"
+            "identifier": "DASHLINK_282",
+            "issued": "2010-12-22",
+            "keyword": [
+                "dashlink",
+                "ames",
+                "nasa"
+            ],
+            "landingPage": "https://c3.nasa.gov/dashlink/resources/282/",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:029"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Dashlink"
+            },
+            "title": "Fast and Flexible Multivariate Time Series Subsequence Search"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://c3.nasa.gov/dashlink/resources/624/",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2012-11-12",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
-            "keyword": [
-                "ames",
-                "nasa",
-                "dashlink"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Kevin Driscoll",
                 "hasEmail": "mailto:kevinrdriscoll@gmail.com"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Dashlink"
-            },
-            "identifier": "DASHLINK_624",
             "description": "This resource area contains descriptions of actual electronic systems failure\r\nscenarios with an emphasis on the diversity of failure modes and effects that\r\ncan befall dependable systems.\r\n\r\nIntroductory pages begin [here](/dashlink/static/media/other/Introduction1.html).<br>\r\nThe descriptions begin\r\n[here](/dashlink/static/media/other/ObservedFailures1.html).  These pages are\r\nseparated into sections.  Each section starts with a List of failure scenarios.  \r\nIn between the List slides are slides that give more information on those\r\nscenarios which warrant more than a bullet or two of explanation.<br>\r\nSome references are listed [here](/dashlink/static/media/other/References.html).<br>\r\nA list of acronyms and initialisms is\r\n[here](/dashlink/static/media/other/Acronyms_Initialisms.html).\r\n\r\nIf you would like to add a story to this list or add additional significant\r\ndetails to an existing story, please contact Kevin Driscoll at\r\n![](/dashlink/static/media/other/KevinDriscoll-email.PNG)\r\n\r\nFor a not-quite-working wiki subset of this Resource area, click on the Wiki link just to the left of this Summary or go to the URL [https://c3.nasa.gov/dashlink/projects/79/wiki/test_stories_split](/dashlink/projects/79/wiki/test_stories_split).\r\n\r\nAlso, those who log in can add comments to the Discussions at the bottom of this\r\npage.",
-            "title": "Real System Failures",
-            "programCode": [
-                "026:029"
-            ],
             "distribution": [
                 {
-                    "mediaType": "image/gif",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/home.gif",
-                    "description": "home.gif",
                     "@type": "dcat:Distribution",
+                    "description": "home.gif",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/home.gif",
+                    "mediaType": "image/gif",
                     "title": "home.gif"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/Introduction2.html",
-                    "description": "Introduction2.html",
                     "@type": "dcat:Distribution",
+                    "description": "Introduction2.html",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/Introduction2.html",
+                    "mediaType": "text/html",
                     "title": "Introduction2.html"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/Introduction3.html",
-                    "description": "Introduction3.html",
                     "@type": "dcat:Distribution",
+                    "description": "Introduction3.html",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/Introduction3.html",
+                    "mediaType": "text/html",
                     "title": "Introduction3.html"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/Introduction3.PNG",
-                    "description": "Introduction3.PNG",
                     "@type": "dcat:Distribution",
+                    "description": "Introduction3.PNG",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/Introduction3.PNG",
+                    "mediaType": "image/png",
                     "title": "Introduction3.PNG"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/Introduction4.html",
-                    "description": "Introduction4.html",
                     "@type": "dcat:Distribution",
+                    "description": "Introduction4.html",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/Introduction4.html",
+                    "mediaType": "text/html",
                     "title": "Introduction4.html"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/Introduction4.PNG",
-                    "description": "Introduction4.PNG",
                     "@type": "dcat:Distribution",
+                    "description": "Introduction4.PNG",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/Introduction4.PNG",
+                    "mediaType": "image/png",
                     "title": "Introduction4.PNG"
                 },
                 {
-                    "mediaType": "image/gif",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/next.gif",
-                    "description": "next.gif",
                     "@type": "dcat:Distribution",
+                    "description": "next.gif",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/next.gif",
+                    "mediaType": "image/gif",
                     "title": "next.gif"
                 },
                 {
-                    "mediaType": "image/gif",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/nonext.gif",
-                    "description": "nonext.gif",
                     "@type": "dcat:Distribution",
+                    "description": "nonext.gif",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/nonext.gif",
+                    "mediaType": "image/gif",
                     "title": "nonext.gif"
                 },
                 {
-                    "mediaType": "image/gif",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/noprevious.gif",
-                    "description": "noprevious.gif",
                     "@type": "dcat:Distribution",
+                    "description": "noprevious.gif",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/noprevious.gif",
+                    "mediaType": "image/gif",
                     "title": "noprevious.gif"
                 },
                 {
-                    "mediaType": "image/gif",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/previous.gif",
-                    "description": "previous.gif",
                     "@type": "dcat:Distribution",
+                    "description": "previous.gif",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/previous.gif",
+                    "mediaType": "image/gif",
                     "title": "previous.gif"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/Acronyms_Initialisms.html",
-                    "description": "Acronyms_Initialisms.html",
                     "@type": "dcat:Distribution",
+                    "description": "Acronyms_Initialisms.html",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/Acronyms_Initialisms.html",
+                    "mediaType": "text/html",
                     "title": "Acronyms_Initialisms.html"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/References.html",
-                    "description": "References.html",
                     "@type": "dcat:Distribution",
+                    "description": "References.html",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/References.html",
+                    "mediaType": "text/html",
                     "title": "References.html"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/ObservedFailures2.html",
-                    "description": "ObservedFailures2.html",
                     "@type": "dcat:Distribution",
+                    "description": "ObservedFailures2.html",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/ObservedFailures2.html",
+                    "mediaType": "text/html",
                     "title": "ObservedFailures2.html"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/ObservedFailures2.PNG",
-                    "description": "ObservedFailures2.PNG",
                     "@type": "dcat:Distribution",
+                    "description": "ObservedFailures2.PNG",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/ObservedFailures2.PNG",
+                    "mediaType": "image/png",
                     "title": "ObservedFailures2.PNG"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/ObservedFailures3.html",
-                    "description": "ObservedFailures3.html",
                     "@type": "dcat:Distribution",
+                    "description": "ObservedFailures3.html",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/ObservedFailures3.html",
+                    "mediaType": "text/html",
                     "title": "ObservedFailures3.html"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/ObservedFailures3.PNG",
-                    "description": "ObservedFailures3.PNG",
                     "@type": "dcat:Distribution",
+                    "description": "ObservedFailures3.PNG",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/ObservedFailures3.PNG",
+                    "mediaType": "image/png",
                     "title": "ObservedFailures3.PNG"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/ObservedFailures4.html",
-                    "description": "ObservedFailures4.html",
                     "@type": "dcat:Distribution",
+                    "description": "ObservedFailures4.html",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/ObservedFailures4.html",
+                    "mediaType": "text/html",
                     "title": "ObservedFailures4.html"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/ObservedFailures4.PNG",
-                    "description": "ObservedFailures4.PNG",
                     "@type": "dcat:Distribution",
+                    "description": "ObservedFailures4.PNG",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/ObservedFailures4.PNG",
+                    "mediaType": "image/png",
                     "title": "ObservedFailures4.PNG"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/ObservedFailures5.html",
-                    "description": "ObservedFailures5.html",
                     "@type": "dcat:Distribution",
+                    "description": "ObservedFailures5.html",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/ObservedFailures5.html",
+                    "mediaType": "text/html",
                     "title": "ObservedFailures5.html"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/ObservedFailures5.PNG",
-                    "description": "ObservedFailures5.PNG",
                     "@type": "dcat:Distribution",
+                    "description": "ObservedFailures5.PNG",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/ObservedFailures5.PNG",
+                    "mediaType": "image/png",
                     "title": "ObservedFailures5.PNG"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/ObservedFailures6.html",
-                    "description": "ObservedFailures6.html",
                     "@type": "dcat:Distribution",
+                    "description": "ObservedFailures6.html",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/ObservedFailures6.html",
+                    "mediaType": "text/html",
                     "title": "ObservedFailures6.html"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/ObservedFailures7.html",
-                    "description": "ObservedFailures7.html",
                     "@type": "dcat:Distribution",
+                    "description": "ObservedFailures7.html",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/ObservedFailures7.html",
+                    "mediaType": "text/html",
                     "title": "ObservedFailures7.html"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/ObservedFailures7.PNG",
-                    "description": "ObservedFailures7.PNG",
                     "@type": "dcat:Distribution",
+                    "description": "ObservedFailures7.PNG",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/ObservedFailures7.PNG",
+                    "mediaType": "image/png",
                     "title": "ObservedFailures7.PNG"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/ObservedFailures8.PNG",
-                    "description": "ObservedFailures8.PNG",
                     "@type": "dcat:Distribution",
+                    "description": "ObservedFailures8.PNG",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/ObservedFailures8.PNG",
+                    "mediaType": "image/png",
                     "title": "ObservedFailures8.PNG"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/ObservedFailures9.PNG",
-                    "description": "ObservedFailures9.PNG",
                     "@type": "dcat:Distribution",
+                    "description": "ObservedFailures9.PNG",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/ObservedFailures9.PNG",
+                    "mediaType": "image/png",
                     "title": "ObservedFailures9.PNG"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/ObservedFailures10.html",
-                    "description": "ObservedFailures10.html",
                     "@type": "dcat:Distribution",
+                    "description": "ObservedFailures10.html",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/ObservedFailures10.html",
+                    "mediaType": "text/html",
                     "title": "ObservedFailures10.html"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/ObservedFailures10.PNG",
-                    "description": "ObservedFailures10.PNG",
                     "@type": "dcat:Distribution",
+                    "description": "ObservedFailures10.PNG",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/ObservedFailures10.PNG",
+                    "mediaType": "image/png",
                     "title": "ObservedFailures10.PNG"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/ObservedFailures11.PNG",
-                    "description": "ObservedFailures11.PNG",
                     "@type": "dcat:Distribution",
+                    "description": "ObservedFailures11.PNG",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/ObservedFailures11.PNG",
+                    "mediaType": "image/png",
                     "title": "ObservedFailures11.PNG"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/ObservedFailures12.PNG",
-                    "description": "ObservedFailures12.PNG",
                     "@type": "dcat:Distribution",
+                    "description": "ObservedFailures12.PNG",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/ObservedFailures12.PNG",
+                    "mediaType": "image/png",
                     "title": "ObservedFailures12.PNG"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/ObservedFailures12.html",
-                    "description": "ObservedFailures12.html",
                     "@type": "dcat:Distribution",
+                    "description": "ObservedFailures12.html",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/ObservedFailures12.html",
+                    "mediaType": "text/html",
                     "title": "ObservedFailures12.html"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/ObservedFailures13.html",
-                    "description": "ObservedFailures13.html",
                     "@type": "dcat:Distribution",
+                    "description": "ObservedFailures13.html",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/ObservedFailures13.html",
+                    "mediaType": "text/html",
                     "title": "ObservedFailures13.html"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/ObservedFailures13.PNG",
-                    "description": "ObservedFailures13.PNG",
                     "@type": "dcat:Distribution",
+                    "description": "ObservedFailures13.PNG",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/ObservedFailures13.PNG",
+                    "mediaType": "image/png",
                     "title": "ObservedFailures13.PNG"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/ObservedFailures14.html",
-                    "description": "ObservedFailures14.html",
                     "@type": "dcat:Distribution",
+                    "description": "ObservedFailures14.html",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/ObservedFailures14.html",
+                    "mediaType": "text/html",
                     "title": "ObservedFailures14.html"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/ObservedFailures14.PNG",
-                    "description": "ObservedFailures14.PNG",
                     "@type": "dcat:Distribution",
+                    "description": "ObservedFailures14.PNG",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/ObservedFailures14.PNG",
+                    "mediaType": "image/png",
                     "title": "ObservedFailures14.PNG"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/ObservedFailures15.html",
-                    "description": "ObservedFailures15.html",
                     "@type": "dcat:Distribution",
+                    "description": "ObservedFailures15.html",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/ObservedFailures15.html",
+                    "mediaType": "text/html",
                     "title": "ObservedFailures15.html"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/ObservedFailures15.PNG",
-                    "description": "ObservedFailures15.PNG",
                     "@type": "dcat:Distribution",
+                    "description": "ObservedFailures15.PNG",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/ObservedFailures15.PNG",
+                    "mediaType": "image/png",
                     "title": "ObservedFailures15.PNG"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/ObservedFailures16.html",
-                    "description": "ObservedFailures16.html",
                     "@type": "dcat:Distribution",
+                    "description": "ObservedFailures16.html",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/ObservedFailures16.html",
+                    "mediaType": "text/html",
                     "title": "ObservedFailures16.html"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/ObservedFailures16.PNG",
-                    "description": "ObservedFailures16.PNG",
                     "@type": "dcat:Distribution",
+                    "description": "ObservedFailures16.PNG",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/ObservedFailures16.PNG",
+                    "mediaType": "image/png",
                     "title": "ObservedFailures16.PNG"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/ObservedFailures17.html",
-                    "description": "ObservedFailures17.html",
                     "@type": "dcat:Distribution",
+                    "description": "ObservedFailures17.html",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/ObservedFailures17.html",
+                    "mediaType": "text/html",
                     "title": "ObservedFailures17.html"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/ObservedFailures17.PNG",
-                    "description": "ObservedFailures17.PNG",
                     "@type": "dcat:Distribution",
+                    "description": "ObservedFailures17.PNG",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/ObservedFailures17.PNG",
+                    "mediaType": "image/png",
                     "title": "ObservedFailures17.PNG"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/ObservedFailures18.html",
-                    "description": "ObservedFailures18.html",
                     "@type": "dcat:Distribution",
+                    "description": "ObservedFailures18.html",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/ObservedFailures18.html",
+                    "mediaType": "text/html",
                     "title": "ObservedFailures18.html"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/ObservedFailures18.PNG",
-                    "description": "ObservedFailures18.PNG",
                     "@type": "dcat:Distribution",
+                    "description": "ObservedFailures18.PNG",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/ObservedFailures18.PNG",
+                    "mediaType": "image/png",
                     "title": "ObservedFailures18.PNG"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/ObservedFailures19.html",
-                    "description": "ObservedFailures19.html",
                     "@type": "dcat:Distribution",
+                    "description": "ObservedFailures19.html",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/ObservedFailures19.html",
+                    "mediaType": "text/html",
                     "title": "ObservedFailures19.html"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/ObservedFailures19.PNG",
-                    "description": "ObservedFailures19.PNG",
                     "@type": "dcat:Distribution",
+                    "description": "ObservedFailures19.PNG",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/ObservedFailures19.PNG",
+                    "mediaType": "image/png",
                     "title": "ObservedFailures19.PNG"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/ObservedFailures20.PNG",
-                    "description": "ObservedFailures20.PNG",
                     "@type": "dcat:Distribution",
+                    "description": "ObservedFailures20.PNG",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/ObservedFailures20.PNG",
+                    "mediaType": "image/png",
                     "title": "ObservedFailures20.PNG"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/ObservedFailures20.html",
-                    "description": "ObservedFailures20.html",
                     "@type": "dcat:Distribution",
+                    "description": "ObservedFailures20.html",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/ObservedFailures20.html",
+                    "mediaType": "text/html",
                     "title": "ObservedFailures20.html"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/ObservedFailures21.html",
-                    "description": "ObservedFailures21.html",
                     "@type": "dcat:Distribution",
+                    "description": "ObservedFailures21.html",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/ObservedFailures21.html",
+                    "mediaType": "text/html",
                     "title": "ObservedFailures21.html"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/ObservedFailures21.PNG",
-                    "description": "ObservedFailures21.PNG",
                     "@type": "dcat:Distribution",
+                    "description": "ObservedFailures21.PNG",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/ObservedFailures21.PNG",
+                    "mediaType": "image/png",
                     "title": "ObservedFailures21.PNG"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/ObservedFailures22.html",
-                    "description": "ObservedFailures22.html",
                     "@type": "dcat:Distribution",
+                    "description": "ObservedFailures22.html",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/ObservedFailures22.html",
+                    "mediaType": "text/html",
                     "title": "ObservedFailures22.html"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/ObservedFailures22.PNG",
-                    "description": "ObservedFailures22.PNG",
                     "@type": "dcat:Distribution",
+                    "description": "ObservedFailures22.PNG",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/ObservedFailures22.PNG",
+                    "mediaType": "image/png",
                     "title": "ObservedFailures22.PNG"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/ObservedFailures23.PNG",
-                    "description": "ObservedFailures23.PNG",
                     "@type": "dcat:Distribution",
+                    "description": "ObservedFailures23.PNG",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/ObservedFailures23.PNG",
+                    "mediaType": "image/png",
                     "title": "ObservedFailures23.PNG"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/ObservedFailures23.html",
-                    "description": "ObservedFailures23.html",
                     "@type": "dcat:Distribution",
+                    "description": "ObservedFailures23.html",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/ObservedFailures23.html",
+                    "mediaType": "text/html",
                     "title": "ObservedFailures23.html"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/ObservedFailures24.html",
-                    "description": "ObservedFailures24.html",
                     "@type": "dcat:Distribution",
+                    "description": "ObservedFailures24.html",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/ObservedFailures24.html",
+                    "mediaType": "text/html",
                     "title": "ObservedFailures24.html"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/ObservedFailures24.PNG",
-                    "description": "ObservedFailures24.PNG",
                     "@type": "dcat:Distribution",
+                    "description": "ObservedFailures24.PNG",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/ObservedFailures24.PNG",
+                    "mediaType": "image/png",
                     "title": "ObservedFailures24.PNG"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/ObservedFailures25.html",
-                    "description": "ObservedFailures25.html",
                     "@type": "dcat:Distribution",
+                    "description": "ObservedFailures25.html",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/ObservedFailures25.html",
+                    "mediaType": "text/html",
                     "title": "ObservedFailures25.html"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/ObservedFailures26.html",
-                    "description": "ObservedFailures26.html",
                     "@type": "dcat:Distribution",
+                    "description": "ObservedFailures26.html",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/ObservedFailures26.html",
+                    "mediaType": "text/html",
                     "title": "ObservedFailures26.html"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/ObservedFailures26.PNG",
-                    "description": "ObservedFailures26.PNG",
                     "@type": "dcat:Distribution",
+                    "description": "ObservedFailures26.PNG",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/ObservedFailures26.PNG",
+                    "mediaType": "image/png",
                     "title": "ObservedFailures26.PNG"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/ObservedFailures27.html",
-                    "description": "ObservedFailures27.html",
                     "@type": "dcat:Distribution",
+                    "description": "ObservedFailures27.html",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/ObservedFailures27.html",
+                    "mediaType": "text/html",
                     "title": "ObservedFailures27.html"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/ObservedFailures27.PNG",
-                    "description": "ObservedFailures27.PNG",
                     "@type": "dcat:Distribution",
+                    "description": "ObservedFailures27.PNG",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/ObservedFailures27.PNG",
+                    "mediaType": "image/png",
                     "title": "ObservedFailures27.PNG"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/ObservedFailures28.html",
-                    "description": "ObservedFailures28.html",
                     "@type": "dcat:Distribution",
+                    "description": "ObservedFailures28.html",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/ObservedFailures28.html",
+                    "mediaType": "text/html",
                     "title": "ObservedFailures28.html"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/ObservedFailures28.PNG",
-                    "description": "ObservedFailures28.PNG",
                     "@type": "dcat:Distribution",
+                    "description": "ObservedFailures28.PNG",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/ObservedFailures28.PNG",
+                    "mediaType": "image/png",
                     "title": "ObservedFailures28.PNG"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/ObservedFailures29.html",
-                    "description": "ObservedFailures29.html",
                     "@type": "dcat:Distribution",
+                    "description": "ObservedFailures29.html",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/ObservedFailures29.html",
+                    "mediaType": "text/html",
                     "title": "ObservedFailures29.html"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/ObservedFailures29.PNG",
-                    "description": "ObservedFailures29.PNG",
                     "@type": "dcat:Distribution",
+                    "description": "ObservedFailures29.PNG",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/ObservedFailures29.PNG",
+                    "mediaType": "image/png",
                     "title": "ObservedFailures29.PNG"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/ObservedFailures30.html",
-                    "description": "ObservedFailures30.html",
                     "@type": "dcat:Distribution",
+                    "description": "ObservedFailures30.html",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/ObservedFailures30.html",
+                    "mediaType": "text/html",
                     "title": "ObservedFailures30.html"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/ObservedFailures31.html",
-                    "description": "ObservedFailures31.html",
                     "@type": "dcat:Distribution",
+                    "description": "ObservedFailures31.html",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/ObservedFailures31.html",
+                    "mediaType": "text/html",
                     "title": "ObservedFailures31.html"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/ObservedFailures30.PNG",
-                    "description": "ObservedFailures30.PNG",
                     "@type": "dcat:Distribution",
+                    "description": "ObservedFailures30.PNG",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/ObservedFailures30.PNG",
+                    "mediaType": "image/png",
                     "title": "ObservedFailures30.PNG"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/ObservedFailures31.PNG",
-                    "description": "ObservedFailures31.PNG",
                     "@type": "dcat:Distribution",
+                    "description": "ObservedFailures31.PNG",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/ObservedFailures31.PNG",
+                    "mediaType": "image/png",
                     "title": "ObservedFailures31.PNG"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/ObservedFailures32.html",
-                    "description": "ObservedFailures32.html",
                     "@type": "dcat:Distribution",
+                    "description": "ObservedFailures32.html",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/ObservedFailures32.html",
+                    "mediaType": "text/html",
                     "title": "ObservedFailures32.html"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/ObservedFailures32.PNG",
-                    "description": "ObservedFailures32.PNG",
                     "@type": "dcat:Distribution",
+                    "description": "ObservedFailures32.PNG",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/ObservedFailures32.PNG",
+                    "mediaType": "image/png",
                     "title": "ObservedFailures32.PNG"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/ObservedFailures33.html",
-                    "description": "ObservedFailures33.html",
                     "@type": "dcat:Distribution",
+                    "description": "ObservedFailures33.html",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/ObservedFailures33.html",
+                    "mediaType": "text/html",
                     "title": "ObservedFailures33.html"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/ObservedFailures33.PNG",
-                    "description": "ObservedFailures33.PNG",
                     "@type": "dcat:Distribution",
+                    "description": "ObservedFailures33.PNG",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/ObservedFailures33.PNG",
+                    "mediaType": "image/png",
                     "title": "ObservedFailures33.PNG"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/ObservedFailures34.html",
-                    "description": "ObservedFailures34.html",
                     "@type": "dcat:Distribution",
+                    "description": "ObservedFailures34.html",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/ObservedFailures34.html",
+                    "mediaType": "text/html",
                     "title": "ObservedFailures34.html"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/ObservedFailures35.html",
-                    "description": "ObservedFailures35.html",
                     "@type": "dcat:Distribution",
+                    "description": "ObservedFailures35.html",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/ObservedFailures35.html",
+                    "mediaType": "text/html",
                     "title": "ObservedFailures35.html"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/ObservedFailures35.PNG",
-                    "description": "ObservedFailures35.PNG",
                     "@type": "dcat:Distribution",
+                    "description": "ObservedFailures35.PNG",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/ObservedFailures35.PNG",
+                    "mediaType": "image/png",
                     "title": "ObservedFailures35.PNG"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/ObservedFailures36.html",
-                    "description": "ObservedFailures36.html",
                     "@type": "dcat:Distribution",
+                    "description": "ObservedFailures36.html",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/ObservedFailures36.html",
+                    "mediaType": "text/html",
                     "title": "ObservedFailures36.html"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/ObservedFailures36.PNG",
-                    "description": "ObservedFailures36.PNG",
                     "@type": "dcat:Distribution",
+                    "description": "ObservedFailures36.PNG",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/ObservedFailures36.PNG",
+                    "mediaType": "image/png",
                     "title": "ObservedFailures36.PNG"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/ObservedFailures37.html",
-                    "description": "ObservedFailures37.html",
                     "@type": "dcat:Distribution",
+                    "description": "ObservedFailures37.html",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/ObservedFailures37.html",
+                    "mediaType": "text/html",
                     "title": "ObservedFailures37.html"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/ObservedFailures37.PNG",
-                    "description": "ObservedFailures37.PNG",
                     "@type": "dcat:Distribution",
+                    "description": "ObservedFailures37.PNG",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/ObservedFailures37.PNG",
+                    "mediaType": "image/png",
                     "title": "ObservedFailures37.PNG"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/ObservedFailures38.html",
-                    "description": "ObservedFailures38.html",
                     "@type": "dcat:Distribution",
+                    "description": "ObservedFailures38.html",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/ObservedFailures38.html",
+                    "mediaType": "text/html",
                     "title": "ObservedFailures38.html"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/ObservedFailures38.PNG",
-                    "description": "ObservedFailures38.PNG",
                     "@type": "dcat:Distribution",
+                    "description": "ObservedFailures38.PNG",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/ObservedFailures38.PNG",
+                    "mediaType": "image/png",
                     "title": "ObservedFailures38.PNG"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/ObservedFailures39.PNG",
-                    "description": "ObservedFailures39.PNG",
                     "@type": "dcat:Distribution",
+                    "description": "ObservedFailures39.PNG",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/ObservedFailures39.PNG",
+                    "mediaType": "image/png",
                     "title": "ObservedFailures39.PNG"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/ObservedFailures40.html",
-                    "description": "ObservedFailures40.html",
                     "@type": "dcat:Distribution",
+                    "description": "ObservedFailures40.html",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/ObservedFailures40.html",
+                    "mediaType": "text/html",
                     "title": "ObservedFailures40.html"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/ObservedFailures40.PNG",
-                    "description": "ObservedFailures40.PNG",
                     "@type": "dcat:Distribution",
+                    "description": "ObservedFailures40.PNG",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/ObservedFailures40.PNG",
+                    "mediaType": "image/png",
                     "title": "ObservedFailures40.PNG"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/ObservedFailures41.html",
-                    "description": "ObservedFailures41.html",
                     "@type": "dcat:Distribution",
+                    "description": "ObservedFailures41.html",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/ObservedFailures41.html",
+                    "mediaType": "text/html",
                     "title": "ObservedFailures41.html"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/ObservedFailures41.PNG",
-                    "description": "ObservedFailures41.PNG",
                     "@type": "dcat:Distribution",
+                    "description": "ObservedFailures41.PNG",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/ObservedFailures41.PNG",
+                    "mediaType": "image/png",
                     "title": "ObservedFailures41.PNG"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/ObservedFailures42.html",
-                    "description": "ObservedFailures42.html",
                     "@type": "dcat:Distribution",
+                    "description": "ObservedFailures42.html",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/ObservedFailures42.html",
+                    "mediaType": "text/html",
                     "title": "ObservedFailures42.html"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/ObservedFailures42.PNG",
-                    "description": "ObservedFailures42.PNG",
                     "@type": "dcat:Distribution",
+                    "description": "ObservedFailures42.PNG",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/ObservedFailures42.PNG",
+                    "mediaType": "image/png",
                     "title": "ObservedFailures42.PNG"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/ObservedFailures43.html",
-                    "description": "ObservedFailures43.html",
                     "@type": "dcat:Distribution",
+                    "description": "ObservedFailures43.html",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/ObservedFailures43.html",
+                    "mediaType": "text/html",
                     "title": "ObservedFailures43.html"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/ObservedFailures44.html",
-                    "description": "ObservedFailures44.html",
                     "@type": "dcat:Distribution",
+                    "description": "ObservedFailures44.html",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/ObservedFailures44.html",
+                    "mediaType": "text/html",
                     "title": "ObservedFailures44.html"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/ObservedFailures45.html",
-                    "description": "ObservedFailures45.html",
                     "@type": "dcat:Distribution",
+                    "description": "ObservedFailures45.html",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/ObservedFailures45.html",
+                    "mediaType": "text/html",
                     "title": "ObservedFailures45.html"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/ObservedFailures45.PNG",
-                    "description": "ObservedFailures45.PNG",
                     "@type": "dcat:Distribution",
+                    "description": "ObservedFailures45.PNG",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/ObservedFailures45.PNG",
+                    "mediaType": "image/png",
                     "title": "ObservedFailures45.PNG"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/ObservedFailures46.html",
-                    "description": "ObservedFailures46.html",
                     "@type": "dcat:Distribution",
+                    "description": "ObservedFailures46.html",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/ObservedFailures46.html",
+                    "mediaType": "text/html",
                     "title": "ObservedFailures46.html"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/ObservedFailures46.PNG",
-                    "description": "ObservedFailures46.PNG",
                     "@type": "dcat:Distribution",
+                    "description": "ObservedFailures46.PNG",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/ObservedFailures46.PNG",
+                    "mediaType": "image/png",
                     "title": "ObservedFailures46.PNG"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/ObservedFailures47.html",
-                    "description": "ObservedFailures47.html",
                     "@type": "dcat:Distribution",
+                    "description": "ObservedFailures47.html",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/ObservedFailures47.html",
+                    "mediaType": "text/html",
                     "title": "ObservedFailures47.html"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/ObservedFailures47.PNG",
-                    "description": "ObservedFailures47.PNG",
                     "@type": "dcat:Distribution",
+                    "description": "ObservedFailures47.PNG",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/ObservedFailures47.PNG",
+                    "mediaType": "image/png",
                     "title": "ObservedFailures47.PNG"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/ObservedFailures48.html",
-                    "description": "ObservedFailures48.html",
                     "@type": "dcat:Distribution",
+                    "description": "ObservedFailures48.html",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/ObservedFailures48.html",
+                    "mediaType": "text/html",
                     "title": "ObservedFailures48.html"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/ObservedFailures48.PNG",
-                    "description": "ObservedFailures48.PNG",
                     "@type": "dcat:Distribution",
+                    "description": "ObservedFailures48.PNG",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/ObservedFailures48.PNG",
+                    "mediaType": "image/png",
                     "title": "ObservedFailures48.PNG"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/ObservedFailures49.html",
-                    "description": "ObservedFailures49.html",
                     "@type": "dcat:Distribution",
+                    "description": "ObservedFailures49.html",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/ObservedFailures49.html",
+                    "mediaType": "text/html",
                     "title": "ObservedFailures49.html"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/ObservedFailures49.PNG",
-                    "description": "ObservedFailures49.PNG",
                     "@type": "dcat:Distribution",
+                    "description": "ObservedFailures49.PNG",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/ObservedFailures49.PNG",
+                    "mediaType": "image/png",
                     "title": "ObservedFailures49.PNG"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/ObservedFailures50.html",
-                    "description": "ObservedFailures50.html",
                     "@type": "dcat:Distribution",
+                    "description": "ObservedFailures50.html",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/ObservedFailures50.html",
+                    "mediaType": "text/html",
                     "title": "ObservedFailures50.html"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/ObservedFailures50.PNG",
-                    "description": "ObservedFailures50.PNG",
                     "@type": "dcat:Distribution",
+                    "description": "ObservedFailures50.PNG",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/ObservedFailures50.PNG",
+                    "mediaType": "image/png",
                     "title": "ObservedFailures50.PNG"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/ObservedFailures51.html",
-                    "description": "ObservedFailures51.html",
                     "@type": "dcat:Distribution",
+                    "description": "ObservedFailures51.html",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/ObservedFailures51.html",
+                    "mediaType": "text/html",
                     "title": "ObservedFailures51.html"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/ObservedFailures51.PNG",
-                    "description": "ObservedFailures51.PNG",
                     "@type": "dcat:Distribution",
+                    "description": "ObservedFailures51.PNG",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/ObservedFailures51.PNG",
+                    "mediaType": "image/png",
                     "title": "ObservedFailures51.PNG"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/ObservedFailures52.html",
-                    "description": "ObservedFailures52.html",
                     "@type": "dcat:Distribution",
+                    "description": "ObservedFailures52.html",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/ObservedFailures52.html",
+                    "mediaType": "text/html",
                     "title": "ObservedFailures52.html"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/ObservedFailures52.PNG",
-                    "description": "ObservedFailures52.PNG",
                     "@type": "dcat:Distribution",
+                    "description": "ObservedFailures52.PNG",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/ObservedFailures52.PNG",
+                    "mediaType": "image/png",
                     "title": "ObservedFailures52.PNG"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/ObservedFailures53.html",
-                    "description": "ObservedFailures53.html",
                     "@type": "dcat:Distribution",
+                    "description": "ObservedFailures53.html",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/ObservedFailures53.html",
+                    "mediaType": "text/html",
                     "title": "ObservedFailures53.html"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/ObservedFailures54.PNG",
-                    "description": "ObservedFailures54.PNG",
                     "@type": "dcat:Distribution",
+                    "description": "ObservedFailures54.PNG",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/ObservedFailures54.PNG",
+                    "mediaType": "image/png",
                     "title": "ObservedFailures54.PNG"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/ObservedFailures54.html",
-                    "description": "ObservedFailures54.html",
                     "@type": "dcat:Distribution",
+                    "description": "ObservedFailures54.html",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/ObservedFailures54.html",
+                    "mediaType": "text/html",
                     "title": "ObservedFailures54.html"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/ObservedFailures55.html",
-                    "description": "ObservedFailures55.html",
                     "@type": "dcat:Distribution",
+                    "description": "ObservedFailures55.html",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/ObservedFailures55.html",
+                    "mediaType": "text/html",
                     "title": "ObservedFailures55.html"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/ObservedFailures55.PNG",
-                    "description": "ObservedFailures55.PNG",
                     "@type": "dcat:Distribution",
+                    "description": "ObservedFailures55.PNG",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/ObservedFailures55.PNG",
+                    "mediaType": "image/png",
                     "title": "ObservedFailures55.PNG"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/ObservedFailures56.html",
-                    "description": "ObservedFailures56.html",
                     "@type": "dcat:Distribution",
+                    "description": "ObservedFailures56.html",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/ObservedFailures56.html",
+                    "mediaType": "text/html",
                     "title": "ObservedFailures56.html"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/ObservedFailures56.PNG",
-                    "description": "ObservedFailures56.PNG",
                     "@type": "dcat:Distribution",
+                    "description": "ObservedFailures56.PNG",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/ObservedFailures56.PNG",
+                    "mediaType": "image/png",
                     "title": "ObservedFailures56.PNG"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/ObservedFailures57.html",
-                    "description": "ObservedFailures57.html",
                     "@type": "dcat:Distribution",
+                    "description": "ObservedFailures57.html",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/ObservedFailures57.html",
+                    "mediaType": "text/html",
                     "title": "ObservedFailures57.html"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/ObservedFailures58.html",
-                    "description": "ObservedFailures58.html",
                     "@type": "dcat:Distribution",
+                    "description": "ObservedFailures58.html",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/ObservedFailures58.html",
+                    "mediaType": "text/html",
                     "title": "ObservedFailures58.html"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/ObservedFailures59.PNG",
-                    "description": "ObservedFailures59.PNG",
                     "@type": "dcat:Distribution",
+                    "description": "ObservedFailures59.PNG",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/ObservedFailures59.PNG",
+                    "mediaType": "image/png",
                     "title": "ObservedFailures59.PNG"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/ObservedFailures59.html",
-                    "description": "ObservedFailures59.html",
                     "@type": "dcat:Distribution",
+                    "description": "ObservedFailures59.html",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/ObservedFailures59.html",
+                    "mediaType": "text/html",
                     "title": "ObservedFailures59.html"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/ObservedFailures11.html",
-                    "description": "ObservedFailures11.html",
                     "@type": "dcat:Distribution",
+                    "description": "ObservedFailures11.html",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/ObservedFailures11.html",
+                    "mediaType": "text/html",
                     "title": "ObservedFailures11.html"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/ObservedFailures39.html",
-                    "description": "ObservedFailures39.html",
                     "@type": "dcat:Distribution",
+                    "description": "ObservedFailures39.html",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/ObservedFailures39.html",
+                    "mediaType": "text/html",
                     "title": "ObservedFailures39.html"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/KevinDriscoll-email.PNG",
-                    "description": "KevinDriscoll-email.PNG",
                     "@type": "dcat:Distribution",
+                    "description": "KevinDriscoll-email.PNG",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/KevinDriscoll-email.PNG",
+                    "mediaType": "image/png",
                     "title": "KevinDriscoll-email.PNG"
                 },
                 {
-                    "mediaType": "image/x-png",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/ObservedFailures25.PNG",
-                    "description": "ObservedFailures25.PNG",
                     "@type": "dcat:Distribution",
+                    "description": "ObservedFailures25.PNG",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/ObservedFailures25.PNG",
+                    "mediaType": "image/x-png",
                     "title": "ObservedFailures25.PNG"
                 },
                 {
-                    "mediaType": "image/x-png",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/ObservedFailures43.PNG",
-                    "description": "ObservedFailures43.PNG",
                     "@type": "dcat:Distribution",
+                    "description": "ObservedFailures43.PNG",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/ObservedFailures43.PNG",
+                    "mediaType": "image/x-png",
                     "title": "ObservedFailures43.PNG"
                 },
                 {
-                    "mediaType": "image/x-png",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/ObservedFailures44.PNG",
-                    "description": "ObservedFailures44.PNG",
                     "@type": "dcat:Distribution",
+                    "description": "ObservedFailures44.PNG",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/ObservedFailures44.PNG",
+                    "mediaType": "image/x-png",
                     "title": "ObservedFailures44.PNG"
                 },
                 {
-                    "mediaType": "image/x-png",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/ObservedFailures53.PNG",
-                    "description": "ObservedFailures53.PNG",
                     "@type": "dcat:Distribution",
+                    "description": "ObservedFailures53.PNG",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/ObservedFailures53.PNG",
+                    "mediaType": "image/x-png",
                     "title": "ObservedFailures53.PNG"
                 },
                 {
-                    "mediaType": "image/x-png",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/ObservedFailures57.PNG",
-                    "description": "ObservedFailures57.PNG",
                     "@type": "dcat:Distribution",
+                    "description": "ObservedFailures57.PNG",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/ObservedFailures57.PNG",
+                    "mediaType": "image/x-png",
                     "title": "ObservedFailures57.PNG"
                 },
                 {
-                    "mediaType": "image/x-png",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/ObservedFailures58.PNG",
-                    "description": "ObservedFailures58.PNG",
                     "@type": "dcat:Distribution",
+                    "description": "ObservedFailures58.PNG",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/ObservedFailures58.PNG",
+                    "mediaType": "image/x-png",
                     "title": "ObservedFailures58.PNG"
                 },
                 {
-                    "mediaType": "image/x-png",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/Introduction2.PNG",
-                    "description": "Introduction2.PNG",
                     "@type": "dcat:Distribution",
+                    "description": "Introduction2.PNG",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/Introduction2.PNG",
+                    "mediaType": "image/x-png",
                     "title": "Introduction2.PNG"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/Introduction5_2.html",
-                    "description": "Introduction5.html",
                     "@type": "dcat:Distribution",
+                    "description": "Introduction5.html",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/Introduction5_2.html",
+                    "mediaType": "text/html",
                     "title": "Introduction5.html"
                 },
                 {
-                    "mediaType": "image/x-png",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/Introduction6.PNG",
-                    "description": "Introduction6.PNG",
                     "@type": "dcat:Distribution",
+                    "description": "Introduction6.PNG",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/Introduction6.PNG",
+                    "mediaType": "image/x-png",
                     "title": "Introduction6.PNG"
                 },
                 {
-                    "mediaType": "image/x-png",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/ObservedFailures6.PNG",
-                    "description": "ObservedFailures6.PNG",
                     "@type": "dcat:Distribution",
+                    "description": "ObservedFailures6.PNG",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/ObservedFailures6.PNG",
+                    "mediaType": "image/x-png",
                     "title": "ObservedFailures6.PNG"
                 },
                 {
-                    "mediaType": "image/x-png",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/ObservedFailures34.PNG",
-                    "description": "ObservedFailures34.PNG",
                     "@type": "dcat:Distribution",
+                    "description": "ObservedFailures34.PNG",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/ObservedFailures34.PNG",
+                    "mediaType": "image/x-png",
                     "title": "ObservedFailures34.PNG"
                 },
                 {
-                    "mediaType": "image/x-png",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/ObservedFailures1.PNG",
-                    "description": "ObservedFailures1.PNG",
                     "@type": "dcat:Distribution",
+                    "description": "ObservedFailures1.PNG",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/ObservedFailures1.PNG",
+                    "mediaType": "image/x-png",
                     "title": "ObservedFailures1.PNG"
                 },
                 {
-                    "mediaType": "image/x-png",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/Introduction5.PNG",
-                    "description": "Introduction5.PNG",
                     "@type": "dcat:Distribution",
+                    "description": "Introduction5.PNG",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/Introduction5.PNG",
+                    "mediaType": "image/x-png",
                     "title": "Introduction5.PNG"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/Introduction1_2.html",
-                    "description": "Introduction1.html",
                     "@type": "dcat:Distribution",
+                    "description": "Introduction1.html",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/Introduction1_2.html",
+                    "mediaType": "text/html",
                     "title": "Introduction1.html"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/Introduction5.html",
-                    "description": "Introduction5.html",
                     "@type": "dcat:Distribution",
+                    "description": "Introduction5.html",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/Introduction5.html",
+                    "mediaType": "text/html",
                     "title": "Introduction5.html"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/Introduction6.html",
-                    "description": "Introduction6.html",
                     "@type": "dcat:Distribution",
+                    "description": "Introduction6.html",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/Introduction6.html",
+                    "mediaType": "text/html",
                     "title": "Introduction6.html"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/ObservedFailures9.html",
-                    "description": "ObservedFailures9.html",
                     "@type": "dcat:Distribution",
+                    "description": "ObservedFailures9.html",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/ObservedFailures9.html",
+                    "mediaType": "text/html",
                     "title": "ObservedFailures9.html"
                 },
                 {
-                    "mediaType": "image/x-png",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/ObservedFailures8_2.PNG",
-                    "description": "ObservedFailures8.PNG",
                     "@type": "dcat:Distribution",
+                    "description": "ObservedFailures8.PNG",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/ObservedFailures8_2.PNG",
+                    "mediaType": "image/x-png",
                     "title": "ObservedFailures8.PNG"
                 },
                 {
-                    "mediaType": "image/x-png",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/Introduction1.PNG",
-                    "description": "Introduction1.PNG",
                     "@type": "dcat:Distribution",
+                    "description": "Introduction1.PNG",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/Introduction1.PNG",
+                    "mediaType": "image/x-png",
                     "title": "Introduction1.PNG"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/Introduction1.html",
-                    "description": "Introduction1.html",
                     "@type": "dcat:Distribution",
+                    "description": "Introduction1.html",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/Introduction1.html",
+                    "mediaType": "text/html",
                     "title": "Introduction1.html"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/ObservedFailures1.html",
-                    "description": "ObservedFailures1.html",
                     "@type": "dcat:Distribution",
+                    "description": "ObservedFailures1.html",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/ObservedFailures1.html",
+                    "mediaType": "text/html",
                     "title": "ObservedFailures1.html"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/ObservedFailures8.html",
-                    "description": "ObservedFailures8.html",
                     "@type": "dcat:Distribution",
+                    "description": "ObservedFailures8.html",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/ObservedFailures8.html",
+                    "mediaType": "text/html",
                     "title": "ObservedFailures8.html"
                 }
             ],
-            "accrualPeriodicity": "irregular"
+            "identifier": "DASHLINK_624",
+            "issued": "2012-11-12",
+            "keyword": [
+                "ames",
+                "nasa",
+                "dashlink"
+            ],
+            "landingPage": "https://c3.nasa.gov/dashlink/resources/624/",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:029"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Dashlink"
+            },
+            "title": "Real System Failures"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Wood, E. F. 1994. 15 Minute Stream Flow Data: USGS (FIFE). Data set. Available on-line [http://www.daac.ornl.gov] from Oak Ridge National Laboratory Distributed Active Archive Center, Oak Ridge, Tennessee, U.S.A. Also published in D. E. Strebel, D. R. Landis, K. F. Huemmrich, and B. W. Meeson (eds.), Collected Data of the First ISLSCP Field Experiment, Vol. 1: Surface Observations and Non-Image Data Sets. CD-ROM. National Aeronautics and Space Administration, Goddard Space Flight Center, Greenbelt, Maryland, U.S.A. (available from http://www.daac.ornl.gov). doi:10.3334/ORNLDAAC/1",
-            "issued": "2024-05-04",
-            "temporal": "1984-12-25T00:00:00Z/1988-03-04T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-06",
-            "keyword": [
-                "surface water",
-                "earth science",
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
-            "identifier": "C2977827088-ORNL_CLOUD",
             "description": "USGS 15 minute stream flow data for Kings Creek on the Konza Prairie",
-            "graphic-preview-description": "Browse Image",
-            "title": "15 Minute Stream Flow Data: USGS (FIFE)",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/fife_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/fife/fife_hydrology_strm_15m/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/fife/fife_hydrology_strm_15m/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/FIFE/guides/15_min_strm_flow.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/FIFE/guides/15_min_strm_flow.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/fife/fife_hydrology_strm_15m/comp/15_min_strm_flow.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/fife/fife_hydrology_strm_15m/comp/15_min_strm_flow.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/msword",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/fife/fife_hydrology_strm_15m/comp/strm_15m.doc",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/fife/fife_hydrology_strm_15m/comp/strm_15m.doc",
+                    "mediaType": "application/msword",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/fife/fife_hydrology_strm_15m/comp/strm_15m.tdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/fife/fife_hydrology_strm_15m/comp/strm_15m.tdf",
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
+            "identifier": "C2977827088-ORNL_CLOUD",
+            "issued": "2024-05-04",
+            "keyword": [
+                "surface water",
+                "earth science",
+                "terrestrial hydrosphere"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1",
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
             "spatial": "39.1 -96.6",
+            "temporal": "1984-12-25T00:00:00Z/1988-03-04T23:59:59Z",
             "theme": [
                 "FIFE",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "15 Minute Stream Flow Data: USGS (FIFE)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-2-PRL-67PCHURYUMOV-M06-V1.0",
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
+            "description": "This data set contains raw EDR images acquired by the OSIRIS Wide Angle\nCamera during the prelanding phase of the Rosetta mission at the comet 67P,\ncovering the period from 2014-08-01 to 2014-09-02.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-2-prl-67pchuryumov-m06-v1.0_e7je-yk25",
+            "issued": "2018-06-26",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-2-PRL-67PCHURYUMOV-M06-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-2-prl-67pchuryumov-m06-v1.0_e7je-yk25",
-            "description": "This data set contains raw EDR images acquired by the OSIRIS Wide Angle\nCamera during the prelanding phase of the Rosetta mission at the comet 67P,\ncovering the period from 2014-08-01 to 2014-09-02.",
-            "title": "ROSETTA-ORBITER COMET PRELANDING OSIWAC 2 EDR MTP 006 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "ROSETTA-ORBITER COMET PRELANDING OSIWAC 2 EDR MTP 006 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=LP-L-ENG-6-ATTITUDE-V1.0",
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
-                "lunar prospector"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "The Lunar Prospector attitude data set consists of values for the spacecraft spin rate and spin axis orientation (attitude) as a function of time. These values are determined from spacecraft attitude data (sun and limb crossing sensors) and ephemeris data. Spacecraft orientations are given as right ascension and declination of the spacecraft spin axis in the Mean-of-J2000 Ecliptic reference frame. The attitude data set consists of a single, cumulative file for the entire mission. Records are added to this file following each significant change in either the spin rate or spin axis orientation. The spacecraft spin rates and attitudes in this data set are orbit averages. The instantaneous spin rate can be determined from the sun pulse data set. The instantaneous spin rate varies as the spacecraft passes into and out of the Moon's shadow and after each spacecraft maneuver. Generally, an attitude record is included for times immediately before and after each maneuver.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.lp-l-eng-6-attitude-v1.0_e7kc-ctq3",
+            "issued": "2018-06-26",
+            "keyword": [
+                "moon",
+                "lunar prospector"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=LP-L-ENG-6-ATTITUDE-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.lp-l-eng-6-attitude-v1.0_e7kc-ctq3",
-            "description": "The Lunar Prospector attitude data set consists of values for the spacecraft spin rate and spin axis orientation (attitude) as a function of time. These values are determined from spacecraft attitude data (sun and limb crossing sensors) and ephemeris data. Spacecraft orientations are given as right ascension and declination of the spacecraft spin axis in the Mean-of-J2000 Ecliptic reference frame. The attitude data set consists of a single, cumulative file for the entire mission. Records are added to this file following each significant change in either the spin rate or spin axis orientation. The spacecraft spin rates and attitudes in this data set are orbit averages. The instantaneous spin rate can be determined from the sun pulse data set. The instantaneous spin rate varies as the spacecraft passes into and out of the Moon's shadow and after each spacecraft maneuver. Generally, an attitude record is included for times immediately before and after each maneuver.",
-            "title": "LP MOON SPACECRAFT ATTITUDE V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "LP MOON SPACECRAFT ATTITUDE V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.7927/H4BR8Q45",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Center for Hazards and Risk Research - CHRR - Columbia University, and Center for International Earth Science Information Network - CIESIN - Columbia University. 2005-12-31. Global Volcano Hazard Frequency and Distribution. Version 1.00. Palisades, NY. Archived by National Aeronautics and Space Administration, U.S. Government, Center for Hazards and Risk Research (CHRR)/Columbia University. https://doi.org/10.7927/H4BR8Q45. https://doi.org/10.7927/H4BR8Q45.",
-            "issued": "2005-12-31",
-            "temporal": "1979-01-01T00:00:00Z/2000-12-31T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2005-12-31",
-            "references": [
-                "https://doi.org/10.7927/H4ZK5DMF",
-                "https://doi.org/10.7927/H43B5X3R",
-                "https://doi.org/10.7927/H4736NT2"
-            ],
-            "keyword": [
-                "natural hazards",
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
-            "identifier": "C179001791-SEDAC",
-            "description": "Global Volcano Hazard Frequency and Distribution is a 2.5 minute gridded data set based upon the National Geophysical Data Center (NGDC) Volcano Database spanning the period  of 79 through 2000. This database includes nearly 4,000 volcanic events categorized as moderate or above (values 2 through 8) according to the Volcano Explosivity Index (VEI). Most volcanoes are georeferenced to the nearest tenth or hundredth of a degree with a few to the nearest thousandth of a degree. To produce the final output, the frequency of a volcanic hazard is computed for each grid cell, with the data set consequently being classified into deciles (10 classes of approximately equal number of grid cells). The higher the grid cell value in the final output, the higher the relative frequency of hazard posed by volcanoes. This data set is the result of collaboration among the Columbia University Center for Hazards and Risk Research (CHRR) and Columbia University Center for International Earth Science Information Network (CIESIN).",
-            "release-place": "Palisades, NY",
-            "graphic-preview-description": "Maps Download Page",
             "creator": "Center for Hazards and Risk Research - CHRR - Columbia University, and Center for International Earth Science Information Network - CIESIN - Columbia University",
-            "title": "Global Volcano Hazard Frequency and Distribution",
-            "graphic-preview-file": "https://sedac.ciesin.columbia.edu/data/set/ndh-volcano-hazard-frequency-distribution/maps",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "Global Volcano Hazard Frequency and Distribution is a 2.5 minute gridded data set based upon the National Geophysical Data Center (NGDC) Volcano Database spanning the period  of 79 through 2000. This database includes nearly 4,000 volcanic events categorized as moderate or above (values 2 through 8) according to the Volcano Explosivity Index (VEI). Most volcanoes are georeferenced to the nearest tenth or hundredth of a degree with a few to the nearest thousandth of a degree. To produce the final output, the frequency of a volcanic hazard is computed for each grid cell, with the data set consequently being classified into deciles (10 classes of approximately equal number of grid cells). The higher the grid cell value in the final output, the higher the relative frequency of hazard posed by volcanoes. This data set is the result of collaboration among the Columbia University Center for Hazards and Risk Research (CHRR) and Columbia University Center for International Earth Science Information Network (CIESIN).",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.7927%2FH4BR8Q45",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.7927%2FH4BR8Q45",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/downloads/maps/ndh/ndh-volcano-hazard-frequency-distribution/volcano-frequency-distribution-thumbnail.jpg",
-                    "description": "Sample browse graphic of the data set.",
                     "@type": "dcat:Distribution",
+                    "description": "Sample browse graphic of the data set.",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/downloads/maps/ndh/ndh-volcano-hazard-frequency-distribution/volcano-frequency-distribution-thumbnail.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/ndh-volcano-hazard-frequency-distribution/data-download",
-                    "description": "Data Download Page",
                     "@type": "dcat:Distribution",
+                    "description": "Data Download Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/ndh-volcano-hazard-frequency-distribution/data-download",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/ndh-volcano-hazard-frequency-distribution/maps",
-                    "description": "Maps Download Page",
                     "@type": "dcat:Distribution",
+                    "description": "Maps Download Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/ndh-volcano-hazard-frequency-distribution/maps",
+                    "mediaType": "text/html",
                     "title": "Get a related map visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/ndh-volcano-hazard-frequency-distribution/maps/services",
-                    "description": "Web Map Service Page",
                     "@type": "dcat:Distribution",
+                    "description": "Web Map Service Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/ndh-volcano-hazard-frequency-distribution/maps/services",
+                    "mediaType": "text/html",
                     "title": "Use Web Map Service (WMS) to download the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/ndh-volcano-hazard-frequency-distribution",
-                    "description": "Data Set\u00a0Overview Page",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set\u00a0Overview Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/ndh-volcano-hazard-frequency-distribution",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "graphic-preview-description": "Maps Download Page",
+            "graphic-preview-file": "https://sedac.ciesin.columbia.edu/data/set/ndh-volcano-hazard-frequency-distribution/maps",
+            "identifier": "C179001791-SEDAC",
+            "issued": "2005-12-31",
+            "keyword": [
+                "natural hazards",
+                "earth science",
+                "human dimensions"
+            ],
+            "landingPage": "https://doi.org/10.7927/H4BR8Q45",
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
+                "https://doi.org/10.7927/H4ZK5DMF",
+                "https://doi.org/10.7927/H43B5X3R",
+                "https://doi.org/10.7927/H4736NT2"
+            ],
+            "release-place": "Palisades, NY",
             "spatial": "-180.0 -58.0 180.0 85.0",
+            "temporal": "1979-01-01T00:00:00Z/2000-12-31T00:00:00Z",
             "theme": [
                 "NDH",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Global Volcano Hazard Frequency and Distribution"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://c3.nasa.gov/dashlink/resources/873/",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2013-12-22",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
-            "keyword": [
-                "nasa",
-                "ames",
-                "dashlink"
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
-            "identifier": "DASHLINK_873",
             "description": "NASA researchers recently demonstrated\r\nsuccessful real-time fault detection and isolation of a virtual reusable launch vehicle main propulsion system. Using a detailed simulation of a vehicle propulsion system to produce synthesized sensor readings, the NASA team demonstrated that advanced diagnostic algorithms, running on flight-like computers, can, in real time, successfully diagnose the presence and cause of faults.\r\nThis demonstration was conducted as part of the NASA Propulsion IVHM Technology Experiment, or PITEX.",
-            "title": "Propulsion IVHM Technology Experiment Overview",
-            "programCode": [
-                "026:029"
-            ],
             "distribution": [
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/publication/Meyer_et_al._-_2003_-_Propulsion_IVHM_Technology_Experiment_Overview.pdf",
-                    "description": "Meyer et al. - 2003 - Propulsion IVHM Technology Experiment Overview.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "Meyer et al. - 2003 - Propulsion IVHM Technology Experiment Overview.pdf",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/publication/Meyer_et_al._-_2003_-_Propulsion_IVHM_Technology_Experiment_Overview.pdf",
+                    "mediaType": "application/pdf",
                     "title": "Meyer et al. - 2003 - Propulsion IVHM Technology Experiment Overview.pdf"
                 }
             ],
-            "accrualPeriodicity": "irregular"
+            "identifier": "DASHLINK_873",
+            "issued": "2013-12-22",
+            "keyword": [
+                "nasa",
+                "ames",
+                "dashlink"
+            ],
+            "landingPage": "https://c3.nasa.gov/dashlink/resources/873/",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:029"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Dashlink"
+            },
+            "title": "Propulsion IVHM Technology Experiment Overview"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/WCKDBPDU85KO",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "SnowEx20 COSMOS Stationary Soil Moisture V001. Version 1. Archived by National Aeronautics and Space Administration, U.S. Government, NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/WCKDBPDU85KO.",
-            "issued": "2019-09-26",
-            "temporal": "2019-08-26T00:00:00Z/2020-05-31T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-01",
-            "keyword": [
-                "land surface",
-                "soils",
-                "atmosphere",
-                "atmospheric pressure",
-                "atmospheric temperature",
-                "atmospheric water vapor",
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
-            "identifier": "C1997891597-NSIDC_ECS",
             "description": "These data contain raw and processed hourly observations from a Hydroinnova COSMOS Stationary sensor probe. Parameters in the raw files include atmospheric pressure, temperature, and relative humidity. These observations were converted to volumetric soil moisture in the processed data files. Data were collected between 26 August 2019 and 31 May 2020 at Grand Mesa, Colorado and represent a 200 m to 300 m area around the instrument.",
-            "title": "SnowEx20 COSMOS Stationary Soil Moisture V001",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FWCKDBPDU85KO",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FWCKDBPDU85KO",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1997891597-NSIDC_ECS&pg%5B0%5D%5Bgsk%5D=-start_date&q=SNEX20_CSSM&m=38.35552775499695%21-113.57226562500001%215%211%210%210%2C2&tl=1596643427%214%21%21",
-                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1997891597-NSIDC_ECS&pg%5B0%5D%5Bgsk%5D=-start_date&q=SNEX20_CSSM&m=38.35552775499695%21-113.57226562500001%215%211%210%210%2C2&tl=1596643427%214%21%21",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/SNOWEX/SNEX20_CSSM.001/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/SNOWEX/SNEX20_CSSM.001/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/data/data-access-tool/SNEX20_CSSM/versions/1/",
-                    "description": "Data Access link for ITSD project",
                     "@type": "dcat:Distribution",
+                    "description": "Data Access link for ITSD project",
+                    "downloadURL": "https://nsidc.org/data/data-access-tool/SNEX20_CSSM/versions/1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1997891597-NSIDC_ECS&pg%5B0%5D%5Bgsk%5D=-start_date&q=SNEX20_CSSM&m=38.35552775499695%21-113.57226562500001%215%211%210%210%2C2&tl=1596643427%214%21%21",
-                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1997891597-NSIDC_ECS&pg%5B0%5D%5Bgsk%5D=-start_date&q=SNEX20_CSSM&m=38.35552775499695%21-113.57226562500001%215%211%210%210%2C2&tl=1596643427%214%21%21",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/SNOWEX/SNEX20_CSSM.001/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/SNOWEX/SNEX20_CSSM.001/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/data/data-access-tool/SNEX20_CSSM/versions/1/",
-                    "description": "Data Access link for ITSD project",
                     "@type": "dcat:Distribution",
+                    "description": "Data Access link for ITSD project",
+                    "downloadURL": "https://nsidc.org/data/data-access-tool/SNEX20_CSSM/versions/1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/WCKDBPDU85KO",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/WCKDBPDU85KO",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/WCKDBPDU85KO",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/WCKDBPDU85KO",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C1997891597-NSIDC_ECS",
+            "issued": "2019-09-26",
+            "keyword": [
+                "land surface",
+                "soils",
+                "atmosphere",
+                "atmospheric pressure",
+                "atmospheric temperature",
+                "atmospheric water vapor",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/WCKDBPDU85KO",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2020-05-01",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA NSIDC DAAC"
+            },
             "spatial": "-108.215 39.033 -108.215 39.033",
+            "temporal": "2019-08-26T00:00:00Z/2020-05-31T23:59:59.999Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "SnowEx20 COSMOS Stationary Soil Moisture V001"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/MODIS/MCD43D64.061",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Crystal Schaaf, Zhuosen Wang\r\n. 2021-02-22. MODIS/Terra+Aqua BRDF/Albedo Nadir BRDF-Adjusted Ref Band3 Daily L3 Global 30ArcSec CMG V061. Sioux Falls, South Dakota, USA. Archived by National Aeronautics and Space Administration, U.S. Government, NASA EOSDIS Land Processes Distributed Active Archive Center. https://doi.org/10.5067/MODIS/MCD43D64.061. https://doi.org/10.5067/MODIS/MCD43D64.061. The DOI landing page provides citations in APA and Chicago styles..",
-            "issued": "2021-02-22",
-            "temporal": "2000-02-16T00:00:00Z/2024-05-20T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2021-02-22",
-            "keyword": [
-                "surface radiative properties",
-                "ngda",
-                "national geospatial data asset",
-                "land surface",
-                "earth science"
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
-            "identifier": "C2540275694-LPCLOUD",
-            "description": "The MCD43D64 Version 6.1 Bidirectional Reflectance Distribution Function and Albedo (BRDF/Albedo) Nadir BRDF-Adjusted Reflectance (NBAR) dataset is produced daily using 16 days of Terra and Aqua Moderate Resolution Imaging Spectroradiometer (MODIS) data at 30 arc second (1,000 meter (m)) resolution. Data are temporally weighted to the ninth day which is reflected in the Julian date in the file name. This Climate Modeling Grid (CMG) product covers the entire globe for use in climate simulation models. Due to the large file size, each MCD43D product contains just one data layer. \r\n\r\nMCD43D62 through MCD43D68 are the NBAR products of the MCD43D BRDF/Albedo product suite for MODIS bands 1 through 7. The NBAR algorithm removes view angle effects from directional reflectances to model the values as if they were collected from a nadir view at local solar noon.\r\n\r\nMCD43D64 is the NBAR for MODIS band 3. \r\n\r\nImprovements/Changes from Previous Versions\r\n\r\n* The Version 6.1 Level-1B (L1B) products have been improved by undergoing various calibration changes that include: changes to the response-versus-scan angle (RVS) approach that affects reflectance bands for Aqua and Terra MODIS, corrections to adjust for the optical crosstalk in Terra MODIS infrared (IR) bands, and corrections to the Terra MODIS forward look-up table (LUT) update for the period 2012 - 2017.\r\n* A polarization correction has been applied to the L1B Reflective Solar Bands (RSB).",
-            "release-place": "Sioux Falls, South Dakota, USA",
             "creator": "Crystal Schaaf, Zhuosen Wang",
-            "title": "MODIS/Terra+Aqua BRDF/Albedo Nadir BRDF-Adjusted Ref Band3 Daily L3 Global 30ArcSec CMG V061",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The MCD43D64 Version 6.1 Bidirectional Reflectance Distribution Function and Albedo (BRDF/Albedo) Nadir BRDF-Adjusted Reflectance (NBAR) dataset is produced daily using 16 days of Terra and Aqua Moderate Resolution Imaging Spectroradiometer (MODIS) data at 30 arc second (1,000 meter (m)) resolution. Data are temporally weighted to the ninth day which is reflected in the Julian date in the file name. This Climate Modeling Grid (CMG) product covers the entire globe for use in climate simulation models. Due to the large file size, each MCD43D product contains just one data layer. \r\n\r\nMCD43D62 through MCD43D68 are the NBAR products of the MCD43D BRDF/Albedo product suite for MODIS bands 1 through 7. The NBAR algorithm removes view angle effects from directional reflectances to model the values as if they were collected from a nadir view at local solar noon.\r\n\r\nMCD43D64 is the NBAR for MODIS band 3. \r\n\r\nImprovements/Changes from Previous Versions\r\n\r\n* The Version 6.1 Level-1B (L1B) products have been improved by undergoing various calibration changes that include: changes to the response-versus-scan angle (RVS) approach that affects reflectance bands for Aqua and Terra MODIS, corrections to adjust for the optical crosstalk in Terra MODIS infrared (IR) bands, and corrections to the Terra MODIS forward look-up table (LUT) update for the period 2012 - 2017.\r\n* A polarization correction has been applied to the L1B Reflective Solar Bands (RSB).",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMODIS%2FMCD43D64.061",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMODIS%2FMCD43D64.061",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "application/x-hdf",
-                    "downloadURL": "https://e4ftl01.cr.usgs.gov/MOTA/MCD43D64.061/",
-                    "description": "LP DAAC Data Pool provides direct access to available products via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "LP DAAC Data Pool provides direct access to available products via HTTPS.",
+                    "downloadURL": "https://e4ftl01.cr.usgs.gov/MOTA/MCD43D64.061/",
+                    "mediaType": "application/x-hdf",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "application/x-hdf",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=C2540275694-LPCLOUD",
-                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=C2540275694-LPCLOUD",
+                    "mediaType": "application/x-hdf",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/MODIS/MCD43D64.061",
-                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
+                    "downloadURL": "https://doi.org/10.5067/MODIS/MCD43D64.061",
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
-                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/filespec/MODIS/6/MCD43D64",
-                    "description": "The File Specification provides a description of the product file including Scientific Data Sets and their attributes.",
                     "@type": "dcat:Distribution",
+                    "description": "The File Specification provides a description of the product file including Scientific Data Sets and their attributes.",
+                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/filespec/MODIS/6/MCD43D64",
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
-                    "downloadURL": "https://opendap.cr.usgs.gov/opendap/hyrax/DP137/MOTA/MCD43D64.061/contents.html",
-                    "description": "Access data via Open-source Project for a Network Data Access Protocol",
                     "@type": "dcat:Distribution",
+                    "description": "Access data via Open-source Project for a Network Data Access Protocol",
+                    "downloadURL": "https://opendap.cr.usgs.gov/opendap/hyrax/DP137/MOTA/MCD43D64.061/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 }
             ],
+            "identifier": "C2540275694-LPCLOUD",
+            "issued": "2021-02-22",
+            "keyword": [
+                "surface radiative properties",
+                "ngda",
+                "national geospatial data asset",
+                "land surface",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/MODIS/MCD43D64.061",
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
+            "title": "MODIS/Terra+Aqua BRDF/Albedo Nadir BRDF-Adjusted Ref Band3 Daily L3 Global 30ArcSec CMG V061"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/MODIS/MYD21C1.061",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Glynn Hulley, Simon Hook. 2021-02-08. MODIS/Aqua Land Surface Temperature/3-Band Emissivity Daily L3 Global 0.05Deg CMG V061. Sioux Falls, South Dakota, USA. Archived by National Aeronautics and Space Administration, U.S. Government, NASA EOSDIS Land Processes Distributed Active Archive Center. https://doi.org/10.5067/MODIS/MYD21C1.061. https://doi.org/10.5067/MODIS/MYD21C1.061. The DOI landing page provides citations in APA and Chicago styles..",
-            "issued": "2021-02-08",
-            "temporal": "2002-07-04T00:00:00Z/2024-06-03T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2021-02-08",
-            "keyword": [
-                "national geospatial data asset",
-                "land surface",
-                "earth science",
-                "surface thermal properties",
-                "surface radiative properties",
-                "ngda"
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
-            "identifier": "C2565805805-LPCLOUD",
-            "description": "A new suite of MODIS Land Surface Temperature and Emissivity  (LST&E) products are available in Collection 6.1. The MYD21 LST algorithm differs from the algorithm of the MYD11 (https://doi.org/10.5067/modis/myd11_l2.061) LST products, in that the MYD21 algorithm is based on the ASTER Temperature/Emissivity Separation (TES) technique, whereas the MYD11 uses the split-window technique. The MYD21 TES algorithm uses a physics-based algorithm to retrieve dynamically both the LST and spectral emissivity simultaneously from the three MODIS thermal infrared bands 29, 31, and 32. The TES algorithm is combined with an improved Water Vapor Scaling (WVS) atmospheric correction scheme to stabilize the retrieval during very warm and humid conditions. \n\nThe MYD21C1 Version 6.1 dataset is produced daily from daytime Level 2 Gridded (L2G) intermediate LST products. The L2G process maps the daily MYD21 (https://doi.org/10.5067/MODIS/MYD21.061) swath granules onto a sinusoidal MODIS grid and stores all observations falling over a gridded cell for a given day. The MOD21C1 algorithm sorts through all these observations for each cell and estimates the final LST value as an average from all observations that are cloud free and have good LST&E accuracies. The daytime average is weighted by the observation coverage for that cell. Only observations having observation coverage more than a certain threshold (15%) are considered for this averaging. The MYD21C1 product contains seven Science Datasets (SDS), which include the calculated LST as well as quality control, the three emissivity bands, view zenith angle, and time of observation. Additional details regarding the methodology used to create this Level 3 (L3) product are available in the Algorithm Theoretical Basis Document (ATBD (https://lpdaac.usgs.gov/documents/1399/MOD21_ATBD.pdf)).\n\nValidation at stage 1 (https://modis-land.gsfc.nasa.gov/MODLAND_val.html) has been achieved for the MODIS Land Surface Temperature and Emissivity data products. Further details regarding MODIS land product validation for the MYD21 data products are available from the MODIS Land Team Validation site (https://modis-land.gsfc.nasa.gov/ValStatus.php?ProductID=MOD21).\n\nImprovements/Changes from Previous Versions\n* The Version 6.1 Level-1B (L1B) products have been improved by undergoing various calibration changes that include: changes to the response-versus-scan angle (RVS) approach that affects reflectance bands for Aqua and Terra MODIS, corrections to adjust for the optical crosstalk in Terra MODIS infrared (IR) bands, and corrections to the Terra MODIS forward look-up table (LUT) update for the period 2012 - 2017.\n* A polarization correction has been applied to the L1B Reflective Solar Bands (RSB).\n* Three new CMG products are available in the MxD21 suite (MxD21C1/C2/C3).",
-            "release-place": "Sioux Falls, South Dakota, USA",
-            "graphic-preview-description": "Browse image for Earthdata Search",
             "creator": "Glynn Hulley, Simon Hook",
-            "title": "MODIS/Aqua Land Surface Temperature/3-Band Emissivity Daily L3 Global 0.05Deg CMG V061",
-            "graphic-preview-file": "https://cmr.earthdata.nasa.gov/browse-scaler/browse_images/granules/G2678420219-LPCLOUD?h=85&w=85",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "A new suite of MODIS Land Surface Temperature and Emissivity  (LST&E) products are available in Collection 6.1. The MYD21 LST algorithm differs from the algorithm of the MYD11 (https://doi.org/10.5067/modis/myd11_l2.061) LST products, in that the MYD21 algorithm is based on the ASTER Temperature/Emissivity Separation (TES) technique, whereas the MYD11 uses the split-window technique. The MYD21 TES algorithm uses a physics-based algorithm to retrieve dynamically both the LST and spectral emissivity simultaneously from the three MODIS thermal infrared bands 29, 31, and 32. The TES algorithm is combined with an improved Water Vapor Scaling (WVS) atmospheric correction scheme to stabilize the retrieval during very warm and humid conditions. \n\nThe MYD21C1 Version 6.1 dataset is produced daily from daytime Level 2 Gridded (L2G) intermediate LST products. The L2G process maps the daily MYD21 (https://doi.org/10.5067/MODIS/MYD21.061) swath granules onto a sinusoidal MODIS grid and stores all observations falling over a gridded cell for a given day. The MOD21C1 algorithm sorts through all these observations for each cell and estimates the final LST value as an average from all observations that are cloud free and have good LST&E accuracies. The daytime average is weighted by the observation coverage for that cell. Only observations having observation coverage more than a certain threshold (15%) are considered for this averaging. The MYD21C1 product contains seven Science Datasets (SDS), which include the calculated LST as well as quality control, the three emissivity bands, view zenith angle, and time of observation. Additional details regarding the methodology used to create this Level 3 (L3) product are available in the Algorithm Theoretical Basis Document (ATBD (https://lpdaac.usgs.gov/documents/1399/MOD21_ATBD.pdf)).\n\nValidation at stage 1 (https://modis-land.gsfc.nasa.gov/MODLAND_val.html) has been achieved for the MODIS Land Surface Temperature and Emissivity data products. Further details regarding MODIS land product validation for the MYD21 data products are available from the MODIS Land Team Validation site (https://modis-land.gsfc.nasa.gov/ValStatus.php?ProductID=MOD21).\n\nImprovements/Changes from Previous Versions\n* The Version 6.1 Level-1B (L1B) products have been improved by undergoing various calibration changes that include: changes to the response-versus-scan angle (RVS) approach that affects reflectance bands for Aqua and Terra MODIS, corrections to adjust for the optical crosstalk in Terra MODIS infrared (IR) bands, and corrections to the Terra MODIS forward look-up table (LUT) update for the period 2012 - 2017.\n* A polarization correction has been applied to the L1B Reflective Solar Bands (RSB).\n* Three new CMG products are available in the MxD21 suite (MxD21C1/C2/C3).",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMODIS%2FMYD21C1.061",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMODIS%2FMYD21C1.061",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "application/x-hdf",
-                    "downloadURL": "https://e4ftl01.cr.usgs.gov/MOLA/MYD21C1.061/",
-                    "description": "LP DAAC Data Pool provides direct access to available products via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "LP DAAC Data Pool provides direct access to available products via HTTPS.",
+                    "downloadURL": "https://e4ftl01.cr.usgs.gov/MOLA/MYD21C1.061/",
+                    "mediaType": "application/x-hdf",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "application/x-hdf",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=C2565805805-LPCLOUD",
-                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=C2565805805-LPCLOUD",
+                    "mediaType": "application/x-hdf",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/MODIS/MYD21C1.061",
-                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
+                    "downloadURL": "https://doi.org/10.5067/MODIS/MYD21C1.061",
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
-                    "downloadURL": "https://lpdaac.usgs.gov/documents/1398/MOD21_User_Guide_V61.pdf",
-                    "description": "The technical information in the User's Guide enables users to interpret and use the data products.",
                     "@type": "dcat:Distribution",
+                    "description": "The technical information in the User's Guide enables users to interpret and use the data products.",
+                    "downloadURL": "https://lpdaac.usgs.gov/documents/1398/MOD21_User_Guide_V61.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://lpdaac.usgs.gov/documents/1399/MOD21_ATBD.pdf",
-                    "description": "The ATBD provides physical theory and mathematical procedures for the calculations used to produce the data products.",
                     "@type": "dcat:Distribution",
+                    "description": "The ATBD provides physical theory and mathematical procedures for the calculations used to produce the data products.",
+                    "downloadURL": "https://lpdaac.usgs.gov/documents/1399/MOD21_ATBD.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's algorithm theoretical basis document"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/filespec/MODIS/61/MYD21C1",
-                    "description": "The File Specification provides a description of the product file including Scientific Data Sets and their attributes.",
                     "@type": "dcat:Distribution",
+                    "description": "The File Specification provides a description of the product file including Scientific Data Sets and their attributes.",
+                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/filespec/MODIS/61/MYD21C1",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://modis-land.gsfc.nasa.gov/MODLAND_val.html",
-                    "description": "Validation at stage 1 has been achieved for the MODIS Land Surface Temperature and Emissivity data products.",
                     "@type": "dcat:Distribution",
+                    "description": "Validation at stage 1 has been achieved for the MODIS Land Surface Temperature and Emissivity data products.",
+                    "downloadURL": "https://modis-land.gsfc.nasa.gov/MODLAND_val.html",
+                    "mediaType": "text/html",
                     "title": "View this dataset's science data product validation documentation"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://modis-land.gsfc.nasa.gov/ValStatus.php?ProductID=MOD21",
-                    "description": "Further details regarding MODIS land product validation for the MYD21 data products are available from the MODIS Land Team Validation site.",
                     "@type": "dcat:Distribution",
+                    "description": "Further details regarding MODIS land product validation for the MYD21 data products are available from the MODIS Land Team Validation site.",
+                    "downloadURL": "https://modis-land.gsfc.nasa.gov/ValStatus.php?ProductID=MOD21",
+                    "mediaType": "text/html",
                     "title": "View this dataset's science data product validation documentation"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/browse-scaler/browse_images/granules/G2678420219-LPCLOUD?h=85&w=85",
-                    "description": "Browse image for Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse image for Earthdata Search",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/browse-scaler/browse_images/granules/G2678420219-LPCLOUD?h=85&w=85",
+                    "mediaType": "text/html",
                     "title": "Get a related visualization"
                 }
             ],
+            "graphic-preview-description": "Browse image for Earthdata Search",
+            "graphic-preview-file": "https://cmr.earthdata.nasa.gov/browse-scaler/browse_images/granules/G2678420219-LPCLOUD?h=85&w=85",
+            "identifier": "C2565805805-LPCLOUD",
+            "issued": "2021-02-08",
+            "keyword": [
+                "national geospatial data asset",
+                "land surface",
+                "earth science",
+                "surface thermal properties",
+                "surface radiative properties",
+                "ngda"
+            ],
+            "landingPage": "https://doi.org/10.5067/MODIS/MYD21C1.061",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2021-02-08",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "LP DAAC"
+            },
+            "release-place": "Sioux Falls, South Dakota, USA",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2002-07-04T00:00:00Z/2024-06-03T00:00:00Z",
             "theme": [
                 "Aqua",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "MODIS/Aqua Land Surface Temperature/3-Band Emissivity Daily L3 Global 0.05Deg CMG V061"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=HP-SSA-DTWG-6-TRAJECTORY-V1.0",
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
-                "titan",
-                "cassini-huygens"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "Unknown",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.hp-ssa-dtwg-6-trajectory-v1.0_e7t8-xqtw",
+            "issued": "2021-05-21",
+            "keyword": [
+                "titan",
+                "cassini-huygens"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=HP-SSA-DTWG-6-TRAJECTORY-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.hp-ssa-dtwg-6-trajectory-v1.0_e7t8-xqtw",
-            "description": "Unknown",
-            "title": "HUYGENS TRAJECTORY",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "HUYGENS TRAJECTORY"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/2316",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Hessilt, T.D., B.M. Rogers, R.C. Scholten, S. Potter, T.A.J. Janssen, and S. Veraverbeke. 2023. ABoVE: Ignitions of ABoVE-FED Fires in Alaska and Canada. ORNL DAAC, Oak Ridge, Tennessee, USA. https://doi.org/10.3334/ORNLDAAC/2316",
-            "issued": "2024-06-14",
-            "temporal": "2001-01-01T00:00:00Z/2019-12-31T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-06-17",
-            "keyword": [
-                "human dimensions",
-                "natural hazards",
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
-            "identifier": "C3103956593-ORNL_CLOUD",
             "description": "This dataset provides daily fire ignition locations and timing for boreal fires in Alaska, U.S., and Canada between 2001 and 2019. The fire ignition locations and timing are extracted from the ABoVE Fire Emission Database; however, the temperate prairies of Canada, the Atlantic Highlands, and Mixed Wood Plains were not included. Fires were detected from Landsat differenced normalized burn ratio (dNBR) and the daily MODIS burned area and active fire products. Detections by dNBR were limited to fire perimeters from national fire databases. Fire ignition locations were retrieved using a local minimum within the fire perimeters. However, when fire locations were confounded due to simultaneous active fire detections, the fire ignition location was set as the centroid of these pixels. A spatial uncertainty equaling the standard deviation of the pixels' coordinates and the nominal nadir of 1000 m was applied to the fire ignition location. The temporal resolution of the ignition timing is within one day. Data is provided in comma separated values (CSV) and shapefile formats.",
-            "graphic-preview-description": "Fire ignition locations across Canada and Alaska, U.S., for 2001 - 2019. For Canada, temperate prairies, the Atlantic Highlands, and Mixed Wood Plains were not included.",
-            "title": "ABoVE: Ignitions of ABoVE-FED Fires in Alaska and Canada",
-            "graphic-preview-file": "https://daac.ornl.gov/ABOVE/guides/Fire_Ignitions_Locations_AK_CA_Fig1.jpg",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F2316",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F2316",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/above/Fire_Ignitions_Locations_AK_CA/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/above/Fire_Ignitions_Locations_AK_CA/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/ABOVE/guides/Fire_Ignitions_Locations_AK_CA.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/ABOVE/guides/Fire_Ignitions_Locations_AK_CA.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/2316",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/2316",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/Fire_Ignitions_Locations_AK_CA/comp/Fire_Ignitions_Locations_AK_CA.pdf",
-                    "description": "ABoVE: Ignitions of ABoVE-FED Fires in Alaska and Canada: Fire_Ignitions_Locations_AK_CA.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "ABoVE: Ignitions of ABoVE-FED Fires in Alaska and Canada: Fire_Ignitions_Locations_AK_CA.pdf",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/Fire_Ignitions_Locations_AK_CA/comp/Fire_Ignitions_Locations_AK_CA.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://daac.ornl.gov/ABOVE/guides/Fire_Ignitions_Locations_AK_CA_Fig1.jpg",
-                    "description": "Fire ignition locations across Canada and Alaska, U.S., for 2001 - 2019. For Canada, temperate prairies, the Atlantic Highlands, and Mixed Wood Plains were not included.",
                     "@type": "dcat:Distribution",
+                    "description": "Fire ignition locations across Canada and Alaska, U.S., for 2001 - 2019. For Canada, temperate prairies, the Atlantic Highlands, and Mixed Wood Plains were not included.",
+                    "downloadURL": "https://daac.ornl.gov/ABOVE/guides/Fire_Ignitions_Locations_AK_CA_Fig1.jpg",
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
+            "graphic-preview-description": "Fire ignition locations across Canada and Alaska, U.S., for 2001 - 2019. For Canada, temperate prairies, the Atlantic Highlands, and Mixed Wood Plains were not included.",
+            "graphic-preview-file": "https://daac.ornl.gov/ABOVE/guides/Fire_Ignitions_Locations_AK_CA_Fig1.jpg",
+            "identifier": "C3103956593-ORNL_CLOUD",
+            "issued": "2024-06-14",
+            "keyword": [
+                "human dimensions",
+                "natural hazards",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/2316",
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
             "spatial": "-166.19 44.91 -52.89 73.01",
+            "temporal": "2001-01-01T00:00:00Z/2019-12-31T23:59:59Z",
             "theme": [
                 "ABoVE",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "ABoVE: Ignitions of ABoVE-FED Fires in Alaska and Canada"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC3-0970-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 3 phase 2015-07-01 to 2015-10-21. It is a Global Gravity measurement at the comet 67P and covers the time 2015-08-18T21:32:25.000 to 2015-08-19T00:17:11.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc3-0970-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC3-0970-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc3-0970-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 3 phase 2015-07-01 to 2015-10-21. It is a Global Gravity measurement at the comet 67P and covers the time 2015-08-18T21:32:25.000 to 2015-08-19T00:17:11.000.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 3 0970 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 3 0970 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ATLAS/ATL08.006",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "ATLAS/ICESat-2 L3A Land and Vegetation Height V006. Version 006. Archived by National Aeronautics and Space Administration, U.S. Government, NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/ATLAS/ATL08.006.",
-            "issued": "2018-10-14",
-            "temporal": "2018-10-14T00:00:00Z/2025-01-27T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-07",
-            "keyword": [
-                "earth science",
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
-            "identifier": "C2613553260-NSIDC_CPRD",
             "description": "This data set (ATL08) contains along-track heights above the WGS84 ellipsoid (ITRF2014 reference frame) for the ground and canopy surfaces. The canopy and ground surfaces are processed in fixed 100 m data segments, which typically contain more than 100 signal photons. The data were acquired by the Advanced Topographic Laser Altimeter System (ATLAS) instrument on board the Ice, Cloud and land Elevation Satellite-2 (ICESat-2) observatory.",
-            "title": "ATLAS/ICESat-2 L3A Land and Vegetation Height V006",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FATLAS%2FATL08.006",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FATLAS%2FATL08.006",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=ATL08+V006",
-                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=ATL08+V006",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2613553260-NSIDC_CPRD",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2613553260-NSIDC_CPRD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/ATLAS/ATL08.006",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/ATLAS/ATL08.006",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/ATLAS/ATL08.006",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/ATLAS/ATL08.006",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C2613553260-NSIDC_CPRD",
+            "issued": "2018-10-14",
+            "keyword": [
+                "earth science",
+                "land surface",
+                "topography"
+            ],
+            "landingPage": "https://doi.org/10.5067/ATLAS/ATL08.006",
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
+            "title": "ATLAS/ICESat-2 L3A Land and Vegetation Height V006"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ASDC/SUBORBITAL/ACCLIP_Model_WB57_Data_1",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2023-05-31. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/ASDC/SUBORBITAL/ACCLIP_Model_WB57_Data_1.",
-            "issued": "2022-07-14",
-            "temporal": "2022-07-14T00:00:00Z/2022-09-14T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-09-14",
-            "keyword": [
-                "human dimensions",
-                "atmospheric temperature",
-                "atmosphere",
-                "aerosols",
-                "environmental impacts",
-                "atmospheric pressure",
-                "atmospheric chemistry",
-                "earth science",
-                "atmospheric water vapor",
-                "atmospheric winds"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Paul Newman",
                 "hasEmail": "mailto:paul.a.newman@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/LARC/SD/ASDC"
-            },
-            "identifier": "C2609869612-LARC_ASDC",
             "description": "ACCLIP_Model_WB57_Data contains modeled meteorological, chemical, and aerosol data along the flight tracks of the WB-57 aircraft during the Asian Summer Monsoon Chemical & Climate Impact Project (ACCLIP). Data collection for this product is complete.\r\n\r\nACCLIP is an international, multi-organizational suborbital campaign that aims to study aerosols and chemical transport that is associated with the Asian Summer Monsoon (ASM) in the Western Pacific region from 15 July 2022 to 31 August 2022. The ASM is the largest meteorological pattern in the Northern Hemisphere (NH) during the summer and is associated with persistent convection and large anticyclonic flow patterns in the upper troposphere and lower stratosphere (UTLS). This leads to significant enhancements in the UTLS of trace species that originate from pollution or biomass burning. Convection connected to the ASM occurs over South, Southeast, and East Asia, a region with complex and rapidly changing emissions due to its high population density and economic growth. Pollution that reaches the UTLS from this region can have significant effects on the climate and chemistry of the atmosphere, making it important to have an accurate representation and understanding of ASM transport, chemical, and microphysical processes for chemistry-climate models to characterize these interactions and for predicting future impacts on climate.\r\n\r\nThe ACCLIP campaign is conducted by the National Aeronautics and Space Administration (NASA) and the National Center for Atmospheric Research (NCAR) with the primary goal of investigating the impacts of Asian gas and aerosol emissions on global chemistry and climate. The NASA WB-57 and NCAR G-V aircraft are outfitted with state-of-the-art sensors to accomplish this. ACCLIP seeks to address four scientific objectives related to its main goal. The first is to investigate the transport pathways of ASM uplifted air from inside of the anticyclone to the global UTLS. Another objective is to sample the chemical content of air processed in the ASM in order to quantify the role of the ASM in transporting chemically active species and short-lived climate forcing agents to the UTLS to determine their impact on stratospheric ozone chemistry and global climate. Third, information is obtained on aerosol size, mass, and chemical composition that is necessary for determining the radiative effects of the ASM to constrain models of aerosol formation and for contrasting the organic-rich ASM UTLS aerosol population with that of the background aerosols. Last, ACCLIP seeks to measure the water vapor distribution associated with the monsoon dynamical structure to evaluate transport across the tropopause and determine the role of the ASM in water vapor transport in the stratosphere.",
-            "title": "ACCLIP WB-57 Aircraft Model Data",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC%2FSUBORBITAL%2FACCLIP_Model_WB57_Data_1",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC%2FSUBORBITAL%2FACCLIP_Model_WB57_Data_1",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
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
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2609869612-LARC_ASDC",
-                    "description": "Earthdata Search for ACCLIP_Model_WB57_Data_1",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for ACCLIP_Model_WB57_Data_1",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2609869612-LARC_ASDC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/ASDC/SUBORBITAL/ACCLIP_Model_WB57_Data_1",
-                    "description": "DOI Data Set Landing Page",
                     "@type": "dcat:Distribution",
+                    "description": "DOI Data Set Landing Page",
+                    "downloadURL": "https://doi.org/10.5067/ASDC/SUBORBITAL/ACCLIP_Model_WB57_Data_1",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 }
             ],
+            "identifier": "C2609869612-LARC_ASDC",
+            "issued": "2022-07-14",
+            "keyword": [
+                "human dimensions",
+                "atmospheric temperature",
+                "atmosphere",
+                "aerosols",
+                "environmental impacts",
+                "atmospheric pressure",
+                "atmospheric chemistry",
+                "earth science",
+                "atmospheric water vapor",
+                "atmospheric winds"
+            ],
+            "landingPage": "https://doi.org/10.5067/ASDC/SUBORBITAL/ACCLIP_Model_WB57_Data_1",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2022-09-14",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/LARC/SD/ASDC"
+            },
             "spatial": "-180.0 16.6 180.0 61.5",
+            "temporal": "2022-07-14T00:00:00Z/2022-09-14T23:59:59Z",
             "theme": [
                 "ACCLIP",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "ACCLIP WB-57 Aircraft Model Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/TRD91YO9S6E7",
             "citation": "Global Modeling and Assimilation Office (GMAO). 2015-06-30. M2IUNPANA. Version 5.12.4. MERRA-2 instU_3d_ana_Np: 3d,diurnal,Instantaneous,Pressure-Level,Analysis,Analyzed Meteorological Fields V5.12.4. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/TRD91YO9S6E7. https://disc.gsfc.nasa.gov/datacollection/M2IUNPANA_5.12.4.html. Digital Science Data.",
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
-                "atmospheric chemistry",
-                "earth science",
-                "atmospheric winds",
-                "atmospheric water vapor",
-                "atmospheric temperature",
-                "atmospheric pressure",
-                "atmosphere",
-                "altitude"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "DANA OSTRENGA",
                 "hasEmail": "mailto:dana.ostrenga@nasa.gov"
             },
+            "creator": "Global Modeling and Assimilation Office (GMAO)",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C1276812907-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "M2IUNPANA (or  instU_3d_ana_Np) is an instantaneous 3-dimensional monthly diurnal means data collection in Modern-Era Retrospective analysis for Research and Applications version 2 (MERRA-2).  This collection consists of  analyzed meteorological fields at 42 pressure levels, such as  temperature, wind components, specific humidity, ozone mixing ratio, and geopotential height.   It is the monthly mean of data fields every six hour starting from 00:00 UTC, e.g.:  00:00, 06:00, \u2026 , 18:00 UTC.  The information on the pressure levels can be found in the section 4.2 of the MERRA-2 File Specification document. \n\nMERRA-2 is the latest version of global atmospheric reanalysis for the satellite era produced by NASA Global Modeling and Assimilation Office (GMAO) using the Goddard Earth Observing System Model (GEOS) version 5.12.4.  The dataset covers the period of 1980-present with the latency of ~3 weeks after the end of a month. \n\nData Reprocessing:  Please check \u201cRecords of MERRA-2 Data Reprocessing and Service Changes\u201d linked from the \u201cDocumentation\u201d tab on this page.  Note that a reprocessed data filename is different from the original file.\n\nMERRA-2 Mailing List: Sign up to receive information on reprocessing of data, changing of tools and services, as well as data announcements from GMAO. Contact the GES DISC Help Desk (gsfc-dl-help-disc@mail.nasa.gov) to be added to the list.\n\nQuestions: If you have a question, please read \"MERRA-2 File Specification Document\",  \u201cMERRA-2 Data Access \u2013 Quick Start Guide\u201d, and FAQs linked from the \u201dDocumentation\u201d tab on this page.  If that does not answer your question, you may email the question on data access to the GES DISC Help Desk (gsfc-dl-help-disc@mail.nasa.gov), or the question on science to the MERRA-2 science team (merra-questions@lists.nasa.gov).",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "M2IUNPANA",
-            "creator": "Global Modeling and Assimilation Office (GMAO)",
-            "graphic-preview-description": "M2IUNPANA variable",
-            "title": "MERRA-2 instU_3d_ana_Np: 3d,diurnal,Instantaneous,Pressure-Level,Analysis,Analyzed Meteorological Fields 0.625 x 0.5 degree V5.12.4 (M2IUNPANA) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/M2IUNPANA_5.12.4.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FTRD91YO9S6E7",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FTRD91YO9S6E7",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/M2IUNPANA_5.12.4.png",
-                    "description": "M2IUNPANA variable",
                     "@type": "dcat:Distribution",
+                    "description": "M2IUNPANA variable",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/M2IUNPANA_5.12.4.png",
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
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/M2IUNPANA_5.12.4.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/M2IUNPANA_5.12.4.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://goldsmr5.gesdisc.eosdis.nasa.gov/data/MERRA2_DIURNAL/M2IUNPANA.5.12.4/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://goldsmr5.gesdisc.eosdis.nasa.gov/data/MERRA2_DIURNAL/M2IUNPANA.5.12.4/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=M2IUNPANA",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=M2IUNPANA",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://goldsmr5.gesdisc.eosdis.nasa.gov/dods/M2IUNPANA.info",
-                    "description": "The GrADS Data Server (GDS) is another form of OPeNDAP that provides subsetting and some analysis services across the Internet.",
                     "@type": "dcat:Distribution",
+                    "description": "The GrADS Data Server (GDS) is another form of OPeNDAP that provides subsetting and some analysis services across the Internet.",
+                    "downloadURL": "https://goldsmr5.gesdisc.eosdis.nasa.gov/dods/M2IUNPANA.info",
+                    "mediaType": "text/html",
                     "title": "Use GRADS DATA SERVER (GDS) to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://goldsmr5.gesdisc.eosdis.nasa.gov/opendap/MERRA2_DIURNAL/M2IUNPANA.5.12.4/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://goldsmr5.gesdisc.eosdis.nasa.gov/opendap/MERRA2_DIURNAL/M2IUNPANA.5.12.4/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://goldsmr5.gesdisc.eosdis.nasa.gov/thredds/catalog/MERRA2_DIURNAL_aggregation/catalog.html?dataset=merra2_diurnal_aggregation%2FM2IUNPANA.5.12.4_Aggregation.ncml",
-                    "description": "Time aggregated THREDDS Data Server (TDS) ",
                     "@type": "dcat:Distribution",
+                    "description": "Time aggregated THREDDS Data Server (TDS) ",
+                    "downloadURL": "https://goldsmr5.gesdisc.eosdis.nasa.gov/thredds/catalog/MERRA2_DIURNAL_aggregation/catalog.html?dataset=merra2_diurnal_aggregation%2FM2IUNPANA.5.12.4_Aggregation.ncml",
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
-                    "downloadURL": "https://goldsmr5.gesdisc.eosdis.nasa.gov/data/MERRA2_DIURNAL/M2IUNPANA.5.12.4/doc/MERRA2.README.pdf",
-                    "description": "README Document",
                     "@type": "dcat:Distribution",
+                    "description": "README Document",
+                    "downloadURL": "https://goldsmr5.gesdisc.eosdis.nasa.gov/data/MERRA2_DIURNAL/M2IUNPANA.5.12.4/doc/MERRA2.README.pdf",
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
+            "graphic-preview-description": "M2IUNPANA variable",
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/M2IUNPANA_5.12.4.png",
+            "identifier": "C1276812907-GES_DISC",
+            "issued": "2007-06-14",
+            "keyword": [
+                "atmospheric chemistry",
+                "earth science",
+                "atmospheric winds",
+                "atmospheric water vapor",
+                "atmospheric temperature",
+                "atmospheric pressure",
+                "atmosphere",
+                "altitude"
+            ],
+            "landingPage": "https://doi.org/10.5067/TRD91YO9S6E7",
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
+            "series-name": "M2IUNPANA",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "1980-01-01T00:00:00Z/2022-01-17T00:00:00Z",
             "theme": [
                 "MERRA-2",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "MERRA-2 instU_3d_ana_Np: 3d,diurnal,Instantaneous,Pressure-Level,Analysis,Analyzed Meteorological Fields 0.625 x 0.5 degree V5.12.4 (M2IUNPANA) at GES DISC"
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
+            "description": "ASE, MECA, MET, OM, RAC, SSI, TEGA, TT",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://pds.jpl.nasa.gov/tools/subscription_service/SS-20090429.shtml",
+                    "mediaType": "application/html"
+                }
             ],
+            "identifier": "NASA-774",
+            "issued": "2018-06-25",
             "keyword": [
                 "meca",
                 "met",
@@ -688820,45 +688829,45 @@
                 "tega",
                 "rac"
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
-            "identifier": "NASA-774",
-            "description": "ASE, MECA, MET, OM, RAC, SSI, TEGA, TT",
-            "title": "PDS Phoenix Data Release 3",
-            "programCode": [
-                "026:005"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://pds.jpl.nasa.gov/tools/subscription_service/SS-20090429.shtml",
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
+            "title": "PDS Phoenix Data Release 3"
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
+            "description": "APXS(EDRs), HAZCAM, NAVCAM, MI, MOESSBAUER (EDRs), PANCAM, Rover Motion Counter, SPICE",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://pds.jpl.nasa.gov/tools/subscription_service/SS-20121121.shtml",
+                    "mediaType": "application/html"
+                }
             ],
+            "identifier": "NASA-497",
+            "issued": "2018-06-25",
             "keyword": [
                 "pancam",
                 "pds",
@@ -688870,218 +688879,223 @@
                 "apxs(edrs)",
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
-            "identifier": "NASA-497",
-            "description": "APXS(EDRs), HAZCAM, NAVCAM, MI, MOESSBAUER (EDRs), PANCAM, Rover Motion Counter, SPICE",
-            "title": "PDS Mars Exploration Rovers Data Release 34",
-            "programCode": [
-                "026:005"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://pds.jpl.nasa.gov/tools/subscription_service/SS-20121121.shtml",
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
+            "title": "PDS Mars Exploration Rovers Data Release 34"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=ULY-J-EPAC-4-SUMM-OMNI-ELE-FLUX-1HR-V1.0",
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
+            "description": "This data set contains Ulysses Energetic Particle Composition Experiment (EPAC) 1 hour averaged omni-directional electron flux data from the Ulysses Jupiter encounter 1992-Jan-25 to 1992-Feb-28. These data were recorded by Electrons Low Spin Averages Telescopes (ELTL) 1-4, Electrons High Spin Averages Telescopes (EHTL) 1-4, and Event-Rate Low, Medium, and High Omni-directional Channels (ERL/ERM/ERH).",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.uly-j-epac-4-summ-omni-ele-flux-1hr-v1.0_e7zq-du3a",
+            "issued": "2018-06-26",
+            "keyword": [
+                "jupiter",
+                "ulysses"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=ULY-J-EPAC-4-SUMM-OMNI-ELE-FLUX-1HR-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.uly-j-epac-4-summ-omni-ele-flux-1hr-v1.0_e7zq-du3a",
-            "description": "This data set contains Ulysses Energetic Particle Composition Experiment (EPAC) 1 hour averaged omni-directional electron flux data from the Ulysses Jupiter encounter 1992-Jan-25 to 1992-Feb-28. These data were recorded by Electrons Low Spin Averages Telescopes (ELTL) 1-4, Electrons High Spin Averages Telescopes (EHTL) 1-4, and Event-Rate Low, Medium, and High Omni-directional Channels (ERL/ERM/ERH).",
-            "title": "ULYSSES JUPITER EPAC OMNI-DIRECTIONAL ELECTRON FLUX",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "ULYSSES JUPITER EPAC OMNI-DIRECTIONAL ELECTRON FLUX"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/IMPACTS/EXRAD/DATA101",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Heymsfield, Gerald M, Lihua  Li and Matthew  McLinden.2022. ER-2 X-Band Doppler Radar (EXRAD) IMPACTS [indicate subset used]. Dataset available online from the NASA Global Hydrometeorology Resource Center DAAC, Huntsville, Alabama, U.S.A. DOI: http://dx.doi.org/10.5067/IMPACTS/EXRAD/DATA101",
-            "issued": "2022-03-23",
-            "temporal": "2020-01-25T18:19:57Z/2020-02-27T14:50:09Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-31",
-            "keyword": [
-                "atmosphere",
-                "earth science",
-                "clouds"
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
-            "identifier": "C1997744595-GHRC_DAAC",
             "description": "The ER-2 X-band Radar (EXRAD) IMPACTS dataset consists of radar reflectivity and Doppler velocity estimates collected by the EXRAD onboard the NASA ER-2 high-altitude research aircraft. These data were gathered during the Investigation of Microphysics and Precipitation for Atlantic Coast-Threatening Snowstorms (IMPACTS) field campaign. IMPACTS was a three-year sequence of winter season deployments conducted to study snowstorms over the U.S Atlantic Coast (2020-2022). The campaign aimed to (1) Provide observations critical to understanding the mechanisms of snowband formation, organization, and evolution; (2) Examine how the microphysical characteristics and likely growth mechanisms of snow particles vary across snowbands; and (3) Improve snowfall remote sensing interpretation and modeling to significantly advance prediction capabilities. The EXRAD IMPACTS dataset files are available from January 25 through February 27, 2020 in HDF-5 format.",
-            "title": "ER-2 X-Band Doppler Radar (EXRAD) IMPACTS V1",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FIMPACTS%2FEXRAD%2FDATA101",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FIMPACTS%2FEXRAD%2FDATA101",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=exradimpacts",
-                    "description": "Files may be downloaded directly to your workstation from this link",
                     "@type": "dcat:Distribution",
+                    "description": "Files may be downloaded directly to your workstation from this link",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=exradimpacts",
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
-                    "downloadURL": "http://har.gsfc.nasa.gov/index.php?section=14",
-                    "description": "EXRAD Description and Sample Measurements from the Nadir Beam",
                     "@type": "dcat:Distribution",
+                    "description": "EXRAD Description and Sample Measurements from the Nadir Beam",
+                    "downloadURL": "http://har.gsfc.nasa.gov/index.php?section=14",
+                    "mediaType": "text/html",
                     "title": "View information related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "http://science.gsfc.nasa.gov/sci/content/uploadFiles/scihi_atmos_ppt/2013_4_highlights.pdf",
-                    "description": "First Flights of ER-2 X-band Radar - EXRAD",
                     "@type": "dcat:Distribution",
+                    "description": "First Flights of ER-2 X-band Radar - EXRAD",
+                    "downloadURL": "http://science.gsfc.nasa.gov/sci/content/uploadFiles/scihi_atmos_ppt/2013_4_highlights.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View information related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/impacts/EXRAD/doc/exradimpacts_dataset.pdf",
-                    "description": "The guide document contains detailed information about the dataset",
                     "@type": "dcat:Distribution",
+                    "description": "The guide document contains detailed information about the dataset",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/impacts/EXRAD/doc/exradimpacts_dataset.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.1175/1520-0426(1997)014%3C0203:COSEIO%3E2.0.CO;2",
-                    "description": "Correction of Sampling Errors in Ocean Surface Cross-Sectional Estimates from Nadir-Looking Weather Radar, Notes and Correspondence",
                     "@type": "dcat:Distribution",
+                    "description": "Correction of Sampling Errors in Ocean Surface Cross-Sectional Estimates from Nadir-Looking Weather Radar, Notes and Correspondence",
+                    "downloadURL": "https://doi.org/10.1175/1520-0426(1997)014%3C0203:COSEIO%3E2.0.CO;2",
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
+            "identifier": "C1997744595-GHRC_DAAC",
+            "issued": "2022-03-23",
+            "keyword": [
+                "atmosphere",
+                "earth science",
+                "clouds"
+            ],
+            "landingPage": "https://doi.org/10.5067/IMPACTS/EXRAD/DATA101",
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
             "spatial": "-90.774 32.392 -71.691 44.76",
+            "temporal": "2020-01-25T18:19:57Z/2020-02-27T14:50:09Z",
             "theme": [
                 "IMPACTS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "ER-2 X-Band Doppler Radar (EXRAD) IMPACTS V1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.nasa.gov/d/e82b-rknz",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "GeneLab Outreach",
+                "hasEmail": "mailto:genelab-outreach@lists.nasa.gov"
+            },
+            "description": "We investigated differentially regulated genes in human myelomonocytic U937 cells in 20s and 5min microgravity and in hypergravity and compared expression profiles to identify potential gravity-regulated genes and adaptation processes. Overall design: Human myelomonocytic U937 cells were exposed to altered gravity during a sounding rocket mission.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "GeneLab Study Page",
+                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-297",
+                    "mediaType": "text/html",
+                    "title": "Dynamic gene expression response to altered gravity in human myelomonocytic U937 cells [sounding rocket]"
+                }
+            ],
+            "identifier": "nasa_genelab_GLDS-297_e82b-rknz",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
             "keyword": [
                 "sample collection",
                 "nucleic acid hybridization",
@@ -689093,45 +689107,45 @@
                 "growth",
                 "rna extraction"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "GeneLab Outreach",
-                "hasEmail": "mailto:genelab-outreach@lists.nasa.gov"
-            },
+            "landingPage": "https://data.nasa.gov/d/e82b-rknz",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "nasa_genelab_GLDS-297_e82b-rknz",
-            "description": "We investigated differentially regulated genes in human myelomonocytic U937 cells in 20s and 5min microgravity and in hypergravity and compared expression profiles to identify potential gravity-regulated genes and adaptation processes. Overall design: Human myelomonocytic U937 cells were exposed to altered gravity during a sounding rocket mission.",
-            "title": "Dynamic gene expression response to altered gravity in human myelomonocytic U937 cells [sounding rocket]",
-            "programCode": [
-                "026:005"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-297",
-                    "description": "GeneLab Study Page",
-                    "@type": "dcat:Distribution",
-                    "title": "Dynamic gene expression response to altered gravity in human myelomonocytic U937 cells [sounding rocket]"
-                }
-            ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "Dynamic gene expression response to altered gravity in human myelomonocytic U937 cells [sounding rocket]"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.nasa.gov/d/e82r-sxqj",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "GeneLab Outreach",
+                "hasEmail": "mailto:genelab-outreach@lists.nasa.gov"
+            },
+            "description": "In March 2006 murine Bone Marrow Stromal Cells (BMSC) were flown in the Soyuz 12S to the International Space Station to investigate the effects of microgravity on their osteogenic potential in a three-dimensional environment. BMSC were grown in porous bioceramic Skelite disks (dia 9 mm x T 1.2 mm). The constructs were exposed to microgravity for ca. 8 days then fixed for RNA extraction. While the flight experiment was performed in fully automated hardware inside the KUBIK incubator one group of control samples were incubated inside manually operated hardwares (flight control) and the other control group was incubated under routine laboratory conditions (lab control). The altered gene expression profile was analyzed by Mouse Gene 1.0 ST array (Affymetrix) representing whole-transcript coverage. Each one of the 28853 genes is represented on the array by approximately 26 probes spread across the full length of the gene providing a more complete and more accurate picture of gene expression than the 3   based expression array design. A few days of microgravity were sufficient to determinate at least at the molecular level an effect in the BMSC; this response expressed a stress condition able to determinate consequences on several compartments and cellular functions. In particular it seems to promote a gene expression known to be associated with neurogenic activity (e.g. axon guidance) perhaps promoting the BMSC capability to be committed in that direction. The osteo-induction by dexamethasone-based medium due to the short duration of stimulation did not have the possibility to manifest itself at the phenotypic level but only partially at the molecular level.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "GeneLab Study Page",
+                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-29",
+                    "mediaType": "text/html",
+                    "title": "Genechip analysis of bone marrow osteoprogenitors exposed to microgravity"
+                }
+            ],
+            "identifier": "nasa_genelab_GLDS-29_e82r-sxqj",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
             "keyword": [
                 "grow",
                 "feature_extraction",
@@ -689154,45 +689168,45 @@
                 "p-gse17696-9",
                 "spaceflight"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "GeneLab Outreach",
-                "hasEmail": "mailto:genelab-outreach@lists.nasa.gov"
-            },
+            "landingPage": "https://data.nasa.gov/d/e82r-sxqj",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "nasa_genelab_GLDS-29_e82r-sxqj",
-            "description": "In March 2006 murine Bone Marrow Stromal Cells (BMSC) were flown in the Soyuz 12S to the International Space Station to investigate the effects of microgravity on their osteogenic potential in a three-dimensional environment. BMSC were grown in porous bioceramic Skelite disks (dia 9 mm x T 1.2 mm). The constructs were exposed to microgravity for ca. 8 days then fixed for RNA extraction. While the flight experiment was performed in fully automated hardware inside the KUBIK incubator one group of control samples were incubated inside manually operated hardwares (flight control) and the other control group was incubated under routine laboratory conditions (lab control). The altered gene expression profile was analyzed by Mouse Gene 1.0 ST array (Affymetrix) representing whole-transcript coverage. Each one of the 28853 genes is represented on the array by approximately 26 probes spread across the full length of the gene providing a more complete and more accurate picture of gene expression than the 3   based expression array design. A few days of microgravity were sufficient to determinate at least at the molecular level an effect in the BMSC; this response expressed a stress condition able to determinate consequences on several compartments and cellular functions. In particular it seems to promote a gene expression known to be associated with neurogenic activity (e.g. axon guidance) perhaps promoting the BMSC capability to be committed in that direction. The osteo-induction by dexamethasone-based medium due to the short duration of stimulation did not have the possibility to manifest itself at the phenotypic level but only partially at the molecular level.",
-            "title": "Genechip analysis of bone marrow osteoprogenitors exposed to microgravity",
-            "programCode": [
-                "026:005"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-29",
-                    "description": "GeneLab Study Page",
-                    "@type": "dcat:Distribution",
-                    "title": "Genechip analysis of bone marrow osteoprogenitors exposed to microgravity"
-                }
-            ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "Genechip analysis of bone marrow osteoprogenitors exposed to microgravity"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.nasa.gov/d/e846-75g3",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "GeneLab Outreach",
+                "hasEmail": "mailto:genelab-outreach@lists.nasa.gov"
+            },
+            "description": "Lettuce crops grown in the Veggie payload aboard ISS harvested and returned for chemical microbiological and molecular analysis",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "GeneLab Study Page",
+                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-267",
+                    "mediaType": "text/html",
+                    "title": "Microbiological and nutritional analysis of lettuce crops grown on the International Space Station-VEG01A"
+                }
+            ],
+            "identifier": "nasa_genelab_GLDS-267_e846-75g3",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
             "keyword": [
                 "nucleic acid extraction",
                 "library construction-its",
@@ -689205,1112 +689219,1112 @@
                 "spaceflight",
                 "sample collection"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "GeneLab Outreach",
-                "hasEmail": "mailto:genelab-outreach@lists.nasa.gov"
-            },
+            "landingPage": "https://data.nasa.gov/d/e846-75g3",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "nasa_genelab_GLDS-267_e846-75g3",
-            "description": "Lettuce crops grown in the Veggie payload aboard ISS harvested and returned for chemical microbiological and molecular analysis",
-            "title": "Microbiological and nutritional analysis of lettuce crops grown on the International Space Station-VEG01A",
-            "programCode": [
-                "026:005"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-267",
-                    "description": "GeneLab Study Page",
-                    "@type": "dcat:Distribution",
-                    "title": "Microbiological and nutritional analysis of lettuce crops grown on the International Space Station-VEG01A"
-                }
-            ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "Microbiological and nutritional analysis of lettuce crops grown on the International Space Station-VEG01A"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MEX-M-MARSIS-5-DDR-ELEDENS%2FBMAG-V1.0",
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
+            "description": "This data set tabulates local electron densities and local magnetic field strengths magnetic field strengths obtained from Mars Advanced Radar for Subsurface and Ionosphere Sounding (MARSIS) Active Ionospheric Sounding (AIS) mode ionograms.  The electron density is obtained by measuring the increment in frequency between the plasma frequency harmonics, visible as bright vertical lines at low frequency and delay time in many MARSIS ionograms.  Similarly, the local magnetic field strength is found by measuring the difference in delay time between electron cyclotron echoes, visible as bright horizontal lines at low frequency on many ionograms.  Both the measured quantity and the derived result are included in the archive product.  We also include a data quality flag giving the impression of the archivist as to how reliable each result is.  This archive product includes only data from the nominal mission, which starts about orbit 1850 and ends on orbit 2539.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mex-m-marsis-5-ddr-eledens-bmag-v1.0_e84u-68ei",
+            "issued": "2021-05-21",
+            "keyword": [
+                "mars express",
+                "mars"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MEX-M-MARSIS-5-DDR-ELEDENS%2FBMAG-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mex-m-marsis-5-ddr-eledens-bmag-v1.0_e84u-68ei",
-            "description": "This data set tabulates local electron densities and local magnetic field strengths magnetic field strengths obtained from Mars Advanced Radar for Subsurface and Ionosphere Sounding (MARSIS) Active Ionospheric Sounding (AIS) mode ionograms.  The electron density is obtained by measuring the increment in frequency between the plasma frequency harmonics, visible as bright vertical lines at low frequency and delay time in many MARSIS ionograms.  Similarly, the local magnetic field strength is found by measuring the difference in delay time between electron cyclotron echoes, visible as bright horizontal lines at low frequency on many ionograms.  Both the measured quantity and the derived result are included in the archive product.  We also include a data quality flag giving the impression of the archivist as to how reliable each result is.  This archive product includes only data from the nominal mission, which starts about orbit 1850 and ends on orbit 2539.",
-            "title": "MEX: MARSIS ELECTRON PLASMA DENSITY AND\n                               MAGNETIC FIELD DATA",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "MEX: MARSIS ELECTRON PLASMA DENSITY AND\n                               MAGNETIC FIELD DATA"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1074",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Markewitz, D., E.A. Davidson, R.D.O. Figueiredo, P.R. Moutinho, and D.C. Nepstad. 2012. LBA-ECO ND-02 Cation Leaching from Forest and Pasture Soils, Para, Brazil. ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/1074",
-            "issued": "2023-10-03",
-            "temporal": "2002-01-01T00:00:00Z/2002-10-31T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-10-10",
-            "keyword": [
-                "earth science",
-                "terrestrial hydrosphere",
-                "water quality/water chemistry",
-                "land use/land cover",
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
-            "identifier": "C2780107886-ORNL_CLOUD",
             "description": "This data set provides a time series of calcium, magnesium, and potassium extracted from soil samples from a laboratory column extraction study conducted in 2002. Soils used in the columns were originally collected in 1998 in Fazenda Vitoria, a cattle ranch 6 km north of the town of Paragominas, Para, Brazil. The soils were from contrasting land uses of primary forest (mata), secondary forest (capoeira), or pasture (pasto). Water equilibrated with increasing concentrations of CO2 was used to extract cations from the soil columns. Data represent the time series of cation concentrations in the extract solutions as well as the total content of cations removed from the soils. There is one comma-delimited ASCII file with this data set.",
-            "graphic-preview-description": "Browse Image",
-            "title": "LBA-ECO ND-02 Cation Leaching from Forest and Pasture Soils, Para, Brazil",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/lba_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1074",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1074",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/lba/nutrient_dynamics/ND02_Soil_CO2_Extracts/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/lba/nutrient_dynamics/ND02_Soil_CO2_Extracts/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/LBA/guides/ND02_Soil_CO2_Extracts.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/LBA/guides/ND02_Soil_CO2_Extracts.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1074",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1074",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/nutrient_dynamics/ND02_Soil_CO2_Extracts/comp/ND02_Soil_CO2_Extracts.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/nutrient_dynamics/ND02_Soil_CO2_Extracts/comp/ND02_Soil_CO2_Extracts.pdf",
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
+            "identifier": "C2780107886-ORNL_CLOUD",
+            "issued": "2023-10-03",
+            "keyword": [
+                "earth science",
+                "terrestrial hydrosphere",
+                "water quality/water chemistry",
+                "land use/land cover",
+                "land surface",
+                "soils"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1074",
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
             "spatial": "-2.98 -47.52",
+            "temporal": "2002-01-01T00:00:00Z/2002-10-31T23:59:59Z",
             "theme": [
                 "LBA-ECO",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "LBA-ECO ND-02 Cation Leaching from Forest and Pasture Soils, Para, Brazil"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG1-S-PLS-5-ELE-BR-96.0SEC",
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
+            "description": "THIS DATA SET CONTAINS THE THERMAL ELECTRON DENSITY AND TEMPERATURE IN THE PLS ENERGY RANGE (10-5950 EV) FROM VOYAGER 1 AT SATURN DERIVED BY FITTING THE LOW ENERGY ELECTRON COMPONENT WITH A MAXWELLIAN DISTRIBUTION, AND THE MOMENT DENSITY AND TEMPERATURE OF THE HOT ELECTRONS CALCULATED AFTER THE SIGNAL FROM THE THERMAL COMPONENT IS SUBTRACTED FROM THE ELECTRON SPECTRA. IT IS A SUBSET OF THE DATA SET VG1-S-PLS-5-ELE-FIT-96.0SEC WHICH SHOULD BE OBTAINED BEFORE THIS DATA IS USED. SPACECRAFT CHARGING MAY RESULT IN FACTOR OF 2-3 ERRORS IN THE THERMAL ELECTRON DENSITY. THE FIRST SIX COLUMNS ARE THE TIME TAG (YEAR, DAY, HOUR, MIN, SEC, MSEC), COLUMN 7 AND 8 ARE THE FIT DENSITY AND TEMPERATURE OF THE THERMAL ELECTRON COMPONENT, AND 9 AND 10 ARE THE MOMENT DENSITY AND TEMPERATURE OF THE SUPRATHERMAL ELECTRONS. EACH ROW HAS THE FORMAT (6I5,4E12.4). VALUES OF 1.E32 INDICATE THAT THE PARAMETER COULD NOT BE OBTAINED FROM THE DATA USING THE STANDARD ANALYSIS TECHNIQUE. ADDITIONAL INFORMATION ABOUT THIS DATASET AND THE INSTRUMENT WHICH PRODUCED IT CAN BE FOUND ELSEWHERE IN THIS CATALOG. AN OVERVIEW OF THE DATA IN THIS DATA SET CAN BE FOUND IN SITTLER ET AL. (1983) AND A COMPLETE INSTRUMENT DESCRIPTION CAN BE FOUND IN BRIDGE (1977).",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg1-s-pls-5-ele-br-96.0sec_e864-646c",
+            "issued": "2018-06-26",
+            "keyword": [
+                "voyager",
+                "saturn"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG1-S-PLS-5-ELE-BR-96.0SEC",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg1-s-pls-5-ele-br-96.0sec_e864-646c",
-            "description": "THIS DATA SET CONTAINS THE THERMAL ELECTRON DENSITY AND TEMPERATURE IN THE PLS ENERGY RANGE (10-5950 EV) FROM VOYAGER 1 AT SATURN DERIVED BY FITTING THE LOW ENERGY ELECTRON COMPONENT WITH A MAXWELLIAN DISTRIBUTION, AND THE MOMENT DENSITY AND TEMPERATURE OF THE HOT ELECTRONS CALCULATED AFTER THE SIGNAL FROM THE THERMAL COMPONENT IS SUBTRACTED FROM THE ELECTRON SPECTRA. IT IS A SUBSET OF THE DATA SET VG1-S-PLS-5-ELE-FIT-96.0SEC WHICH SHOULD BE OBTAINED BEFORE THIS DATA IS USED. SPACECRAFT CHARGING MAY RESULT IN FACTOR OF 2-3 ERRORS IN THE THERMAL ELECTRON DENSITY. THE FIRST SIX COLUMNS ARE THE TIME TAG (YEAR, DAY, HOUR, MIN, SEC, MSEC), COLUMN 7 AND 8 ARE THE FIT DENSITY AND TEMPERATURE OF THE THERMAL ELECTRON COMPONENT, AND 9 AND 10 ARE THE MOMENT DENSITY AND TEMPERATURE OF THE SUPRATHERMAL ELECTRONS. EACH ROW HAS THE FORMAT (6I5,4E12.4). VALUES OF 1.E32 INDICATE THAT THE PARAMETER COULD NOT BE OBTAINED FROM THE DATA USING THE STANDARD ANALYSIS TECHNIQUE. ADDITIONAL INFORMATION ABOUT THIS DATASET AND THE INSTRUMENT WHICH PRODUCED IT CAN BE FOUND ELSEWHERE IN THIS CATALOG. AN OVERVIEW OF THE DATA IN THIS DATA SET CAN BE FOUND IN SITTLER ET AL. (1983) AND A COMPLETE INSTRUMENT DESCRIPTION CAN BE FOUND IN BRIDGE (1977).",
-            "title": "VOYAGER 1 SATURN PLASMA DERIVED ELECTRON BROWSE 96 SEC",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "VOYAGER 1 SATURN PLASMA DERIVED ELECTRON BROWSE 96 SEC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-CAL-ALICE-2-CR5-V1.0",
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
+            "description": "This data set contains CODMAC level 2 data acquired by the Rosetta Orbiter ALICE UV Spectrometer during the Cruise 5 mission phase, which took place between 2009-12-14 and 2010-06-06, and includes Payload Checkout #12.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-cal-alice-2-cr5-v1.0_e87b-khm2",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "calibration"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-CAL-ALICE-2-CR5-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-cal-alice-2-cr5-v1.0_e87b-khm2",
-            "description": "This data set contains CODMAC level 2 data acquired by the Rosetta Orbiter ALICE UV Spectrometer during the Cruise 5 mission phase, which took place between 2009-12-14 and 2010-06-06, and includes Payload Checkout #12.",
-            "title": "ROSETTA-ORBITER CAL ALICE 2 CR5 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER CAL ALICE 2 CR5 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MGN-V-RDRS-5-MIDR-C2-V1.0",
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
+            "description": "This data set contains the Magellan Compressed Twice Mosaicked Image Data Records (C2-MIDRs) which consists of mosaics generated by computing 3x3 pixel arithmetic moving averages from the C1-MIDRs. Each C2-MIDR is in a sinusoidal equal area projection and has an origin at 0 degrees latitude, with the central meridian defined as the longitude bisecting the mosaic. Each C2-MIDR has 7168 lines (aligned with latitudes) and 8192 samples, arranged as 56 1024x1024 files on CD-ROM. C2-MIDRs, with their 675 m pixel widths, are designed to cover the planet at reasonably high resolution and high signal to noise ratio.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mgn-v-rdrs-5-midr-c2-v1.0_e89i-c8ck",
+            "issued": "2021-05-21",
+            "keyword": [
+                "venus",
+                "magellan"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MGN-V-RDRS-5-MIDR-C2-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mgn-v-rdrs-5-midr-c2-v1.0_e89i-c8ck",
-            "description": "This data set contains the Magellan Compressed Twice Mosaicked Image Data Records (C2-MIDRs) which consists of mosaics generated by computing 3x3 pixel arithmetic moving averages from the C1-MIDRs. Each C2-MIDR is in a sinusoidal equal area projection and has an origin at 0 degrees latitude, with the central meridian defined as the longitude bisecting the mosaic. Each C2-MIDR has 7168 lines (aligned with latitudes) and 8192 samples, arranged as 56 1024x1024 files on CD-ROM. C2-MIDRs, with their 675 m pixel widths, are designed to cover the planet at reasonably high resolution and high signal to noise ratio.",
-            "title": "MGN V RADAR SYSTEM DERIVED MIDR COMPRESSED TWICE V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "MGN V RADAR SYSTEM DERIVED MIDR COMPRESSED TWICE V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-4-EXT2-67P-M29-INF-REFL-V1.0",
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
+            "description": "This CODMAC level 4 data set contains solar stray-light corrected, in-field stray-light corrected,  radiometric calibrated and geometric distortion corrected  (resampled) image data in reflectance units (normalized  and thus without unit),  acquired by the OSIRIS Wide Angle Camera on the Rosetta spacecraft  during the ROSETTA EXTENSION 2 mission phase, covering the period  from 2016-05-03T23:25:00.000 to 2016-05-31T23:24:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V1.0 is the first version of this dataset: Lien corrected dataset after September 2019 PSA/PDS external peer review.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-4-ext2-67p-m29-inf-refl-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-4-EXT2-67P-M29-INF-REFL-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-4-ext2-67p-m29-inf-refl-v1.0",
-            "description": "This CODMAC level 4 data set contains solar stray-light corrected, in-field stray-light corrected,  radiometric calibrated and geometric distortion corrected  (resampled) image data in reflectance units (normalized  and thus without unit),  acquired by the OSIRIS Wide Angle Camera on the Rosetta spacecraft  during the ROSETTA EXTENSION 2 mission phase, covering the period  from 2016-05-03T23:25:00.000 to 2016-05-31T23:24:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V1.0 is the first version of this dataset: Lien corrected dataset after September 2019 PSA/PDS external peer review.",
-            "title": "ROSETTA-ORBITER 67P OSIWAC 4 EXT2-MTP029 RDR-INF-REFL V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P OSIWAC 4 EXT2-MTP029 RDR-INF-REFL V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=DAWN-A-FC2-5-CERESMOSAIC-V1.0",
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
+            "description": "Abstract ======== This accumulating data set includes Ceres global mosaics and quadrangles derived from images acquired by the Framing Camera 2 (FC2) on the NASA Dawn spacecraft. Global mosaics are provided in cylindrical and polar stereographic projections. The quadrangle mosaics use Mercator (equatorial), Lambert conformal (mid-latitude) and stereographic projections. Clear and color mosaics are provided for high altitude mapping orbit (HAMO) and clear filter mosaics only in the low altitude mapping orbit (LAMO) science phases. This data set spans three PDS archive volumes which were created at different times during the mission. Volume DWNCHCFC2_2 contains HAMO clear filter mosaics, DWNCHFFC2_2 contains HAMO color filter mosaics, and DWNCLCFC2_2 contains LAMO clear mosaics.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.dawn-a-fc2-5-ceresmosaic-v1.0_e8e6-jiuj",
+            "issued": "2021-05-21",
+            "keyword": [
+                "dawn mission to vesta and ceres",
+                "1 ceres"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=DAWN-A-FC2-5-CERESMOSAIC-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.dawn-a-fc2-5-ceresmosaic-v1.0_e8e6-jiuj",
-            "description": "Abstract ======== This accumulating data set includes Ceres global mosaics and quadrangles derived from images acquired by the Framing Camera 2 (FC2) on the NASA Dawn spacecraft. Global mosaics are provided in cylindrical and polar stereographic projections. The quadrangle mosaics use Mercator (equatorial), Lambert conformal (mid-latitude) and stereographic projections. Clear and color mosaics are provided for high altitude mapping orbit (HAMO) and clear filter mosaics only in the low altitude mapping orbit (LAMO) science phases. This data set spans three PDS archive volumes which were created at different times during the mission. Volume DWNCHCFC2_2 contains HAMO clear filter mosaics, DWNCHFFC2_2 contains HAMO color filter mosaics, and DWNCLCFC2_2 contains LAMO clear mosaics.",
-            "title": "DAWN FC2 DERIVED CERES MOSAICS V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "DAWN FC2 DERIVED CERES MOSAICS V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/J8SGO1E0Y9XZ",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "SMAP L2 Radar Half-Orbit 3 km EASE-Grid Soil Moisture V003. Version 003. Archived by National Aeronautics and Space Administration, U.S. Government, NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/J8SGO1E0Y9XZ.",
-            "issued": "2015-04-13",
-            "temporal": "2015-04-13T00:00:00Z/2015-07-07T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2015-07-07",
-            "keyword": [
-                "land surface",
-                "spectral/engineering",
-                "soils",
-                "radar",
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
-            "identifier": "C2812935277-NSIDC_CPRD",
             "description": "This Level-2 (L2) soil moisture product provides estimates of global land surface conditions retrieved by the Soil Moisture Active Passive (SMAP) active radar during 6:00 a.m. descending half-orbit passes, as well as ancillary data such as surface temperature and vegetation water content. Input backscatter data used to derive soil moisture are resampled to an Earth-fixed, global, cylindrical 3 km Equal-Area Scalable Earth Grid, Version 2.0 (EASE-Grid 2.0).",
-            "title": "SMAP L2 Radar Half-Orbit 3 km EASE-Grid Soil Moisture V003",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FJ8SGO1E0Y9XZ",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FJ8SGO1E0Y9XZ",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=SPL2SMA+V003",
-                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=SPL2SMA+V003",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2812935277-NSIDC_CPRD",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2812935277-NSIDC_CPRD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/J8SGO1E0Y9XZ",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/J8SGO1E0Y9XZ",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/J8SGO1E0Y9XZ",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/J8SGO1E0Y9XZ",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C2812935277-NSIDC_CPRD",
+            "issued": "2015-04-13",
+            "keyword": [
+                "land surface",
+                "spectral/engineering",
+                "soils",
+                "radar",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/J8SGO1E0Y9XZ",
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
+            "title": "SMAP L2 Radar Half-Orbit 3 km EASE-Grid Soil Moisture V003"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC4-1253-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 4 phase 2015-10-22 to 2015-12-31. It is a Global Gravity measurement at the comet 67P and covers the time 2015-12-12T13:27:05.000 to 2015-12-12T15:45:09.500.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc4-1253-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC4-1253-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc4-1253-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 4 phase 2015-10-22 to 2015-12-31. It is a Global Gravity measurement at the comet 67P and covers the time 2015-12-12T13:27:05.000 to 2015-12-12T15:45:09.500.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 4 1253 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 4 1253 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/MODIS/MCD18C2.062",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Dongdong Wang. 2024-03-07. MCD18C2.062. MODIS/Terra+Aqua Photosynthetically Active Radiation Daily/3-Hour L3 Global 0.05Deg CMG V062. Sioux Falls, South Dakota, USA. Archived by National Aeronautics and Space Administration, U.S. Government, NASA EOSDIS Land Processes Distributed Active Archive Center. https://doi.org/10.5067/MODIS/MCD18C2.062. https://doi.org/10.5067/MODIS/MCD18C2.062. The DOI landing page provides citations in APA and Chicago styles..",
-            "issued": "2021-03-18",
-            "temporal": "2000-02-24T00:00:00Z/2024-06-03T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2021-03-18",
-            "keyword": [
-                "national geospatial data asset",
-                "land surface",
-                "earth science",
-                "ngda",
-                "land use/land cover"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Dongdong Wang",
                 "hasEmail": "mailto:ddwang@umd.edu"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "LP DAAC"
-            },
-            "identifier": "C2486294617-LPCLOUD",
-            "description": "The MCD18C2 Version 6.2 is a Moderate Resolution Imaging Spectroradiometer (MODIS) Terra and Aqua combined Photosynthetically Active Radiation (PAR) gridded Level 3 product produced daily at 0.05 degree (5,600 meters at the equator) resolution with estimates of PAR every 3 hours. PAR is incident solar radiation in the visible spectrum (400-700 nanometers) and is an important variable in land-surface models that address a variety of scientific and application issues. The MCD18 products are based on a prototyping algorithm that uses multi-temporal signatures of MODIS data to derive surface reflectance and then calculate incident PAR using the look-up table (LUT) approach. The LUTs consider different types of loadings of aerosols and clouds at a variety of illumination/viewing geometry. Global PAR products are generated from MODIS and geostationary satellite data. Additional details regarding the methodology used to create the data are available in the Algorithm Theoretical Basis Document (ATBD) (https://lpdaac.usgs.gov/documents/106/MCD18_ATBD.pdf)).\r\n\r\nProvided in the MOD18C2 product are layers for instantaneous PAR array for each individual MODIS overpass and 3-hour PAR array along with a View Zenith Angle layer.\r\n\r\nValidation at stage 1 (https://modis-land.gsfc.nasa.gov/MODLAND_val.html) has been achieved for the MODIS Surface Radiation products. Further details regarding MODIS land product validation for the MCD18 data products are available from the MODIS Land Team Validation site (https://modis-land.gsfc.nasa.gov/ValStatus.php?ProductID=MCD18). \r\n\r\nThe Version 6.2 Level-1B (L1B) products have been improved by undergoing various calibration changes that include: 1) MODIS shortwave infrared bands are included in the retrieval algorithm, which significantly reduces estimation uncertainties in cloud- and snow-covered pixels. \r\n2) An improved climatology of surface reflectance was produced and used in the retrieval algorithm.",
-            "release-place": "Sioux Falls, South Dakota, USA",
-            "series-name": "MCD18C2.062",
-            "graphic-preview-description": "Browse image for Earthdata Search",
             "creator": "Dongdong Wang",
-            "title": "MODIS/Terra+Aqua Photosynthetically Active Radiation Daily/3-Hour L3 Global 0.05Deg CMG V062",
-            "graphic-preview-file": "https://cmr.earthdata.nasa.gov/browse-scaler/browse_images/granules/G2800165003-LPCLOUD?h=85&w=85",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The MCD18C2 Version 6.2 is a Moderate Resolution Imaging Spectroradiometer (MODIS) Terra and Aqua combined Photosynthetically Active Radiation (PAR) gridded Level 3 product produced daily at 0.05 degree (5,600 meters at the equator) resolution with estimates of PAR every 3 hours. PAR is incident solar radiation in the visible spectrum (400-700 nanometers) and is an important variable in land-surface models that address a variety of scientific and application issues. The MCD18 products are based on a prototyping algorithm that uses multi-temporal signatures of MODIS data to derive surface reflectance and then calculate incident PAR using the look-up table (LUT) approach. The LUTs consider different types of loadings of aerosols and clouds at a variety of illumination/viewing geometry. Global PAR products are generated from MODIS and geostationary satellite data. Additional details regarding the methodology used to create the data are available in the Algorithm Theoretical Basis Document (ATBD) (https://lpdaac.usgs.gov/documents/106/MCD18_ATBD.pdf)).\r\n\r\nProvided in the MOD18C2 product are layers for instantaneous PAR array for each individual MODIS overpass and 3-hour PAR array along with a View Zenith Angle layer.\r\n\r\nValidation at stage 1 (https://modis-land.gsfc.nasa.gov/MODLAND_val.html) has been achieved for the MODIS Surface Radiation products. Further details regarding MODIS land product validation for the MCD18 data products are available from the MODIS Land Team Validation site (https://modis-land.gsfc.nasa.gov/ValStatus.php?ProductID=MCD18). \r\n\r\nThe Version 6.2 Level-1B (L1B) products have been improved by undergoing various calibration changes that include: 1) MODIS shortwave infrared bands are included in the retrieval algorithm, which significantly reduces estimation uncertainties in cloud- and snow-covered pixels. \r\n2) An improved climatology of surface reflectance was produced and used in the retrieval algorithm.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMODIS%2FMCD18C2.062",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMODIS%2FMCD18C2.062",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://e4ftl01.cr.usgs.gov/MOTA/MCD18C2.062/",
-                    "description": "LP DAAC Data Pool provides direct access to available products via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "LP DAAC Data Pool provides direct access to available products via HTTPS.",
+                    "downloadURL": "https://e4ftl01.cr.usgs.gov/MOTA/MCD18C2.062/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=C2486294617-LPCLOUD",
-                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=C2486294617-LPCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/MODIS/MCD18C2.062",
-                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
+                    "downloadURL": "https://doi.org/10.5067/MODIS/MCD18C2.062",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://lpdaac.usgs.gov/documents/1658/MCD18_User_Guide_V62.pdf",
-                    "description": "The technical information in the User's Guide enables users to interpret and use the data products.",
                     "@type": "dcat:Distribution",
+                    "description": "The technical information in the User's Guide enables users to interpret and use the data products.",
+                    "downloadURL": "https://lpdaac.usgs.gov/documents/1658/MCD18_User_Guide_V62.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://lpdaac.usgs.gov/documents/106/MCD18_ATBD.pdf",
-                    "description": "The ATBD provides physical theory and mathematical procedures for the calculations used to produce the data products.",
                     "@type": "dcat:Distribution",
+                    "description": "The ATBD provides physical theory and mathematical procedures for the calculations used to produce the data products.",
+                    "downloadURL": "https://lpdaac.usgs.gov/documents/106/MCD18_ATBD.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's algorithm theoretical basis document"
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
-                    "downloadURL": "https://modis-land.gsfc.nasa.gov/MODLAND_val.html",
-                    "description": "Validation at stage 1 has been achieved for the MODIS Surface Radiation products.",
                     "@type": "dcat:Distribution",
+                    "description": "Validation at stage 1 has been achieved for the MODIS Surface Radiation products.",
+                    "downloadURL": "https://modis-land.gsfc.nasa.gov/MODLAND_val.html",
+                    "mediaType": "text/html",
                     "title": "View this dataset's science data product validation documentation"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://modis-land.gsfc.nasa.gov/ValStatus.php?ProductID=MCD18",
-                    "description": "Further details regarding MODIS land product validation for the MCD18 data products are available from the MODIS Land Team Validation site.",
                     "@type": "dcat:Distribution",
+                    "description": "Further details regarding MODIS land product validation for the MCD18 data products are available from the MODIS Land Team Validation site.",
+                    "downloadURL": "https://modis-land.gsfc.nasa.gov/ValStatus.php?ProductID=MCD18",
+                    "mediaType": "text/html",
                     "title": "View this dataset's science data product validation documentation"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/browse-scaler/browse_images/granules/G2800165003-LPCLOUD?h=85&w=85",
-                    "description": "Browse image for Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse image for Earthdata Search",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/browse-scaler/browse_images/granules/G2800165003-LPCLOUD?h=85&w=85",
+                    "mediaType": "text/html",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://opendap.cr.usgs.gov/opendap/hyrax/DP113/MOTA/MCD18C2.062/contents.html",
-                    "description": "Access data via Open-source Project for a Network Data Access Protocol",
                     "@type": "dcat:Distribution",
+                    "description": "Access data via Open-source Project for a Network Data Access Protocol",
+                    "downloadURL": "https://opendap.cr.usgs.gov/opendap/hyrax/DP113/MOTA/MCD18C2.062/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/filespec/MODIS/61/MCD18C2",
-                    "description": "The File Specification provides a description of the product file including Scientific Data Sets and their attributes.",
                     "@type": "dcat:Distribution",
+                    "description": "The File Specification provides a description of the product file including Scientific Data Sets and their attributes.",
+                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/filespec/MODIS/61/MCD18C2",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "graphic-preview-description": "Browse image for Earthdata Search",
+            "graphic-preview-file": "https://cmr.earthdata.nasa.gov/browse-scaler/browse_images/granules/G2800165003-LPCLOUD?h=85&w=85",
+            "identifier": "C2486294617-LPCLOUD",
+            "issued": "2021-03-18",
+            "keyword": [
+                "national geospatial data asset",
+                "land surface",
+                "earth science",
+                "ngda",
+                "land use/land cover"
+            ],
+            "landingPage": "https://doi.org/10.5067/MODIS/MCD18C2.062",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2021-03-18",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "LP DAAC"
+            },
+            "release-place": "Sioux Falls, South Dakota, USA",
+            "series-name": "MCD18C2.062",
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
+            "title": "MODIS/Terra+Aqua Photosynthetically Active Radiation Daily/3-Hour L3 Global 0.05Deg CMG V062"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://c3.nasa.gov/dashlink/resources/786/",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2013-06-19",
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
-            "identifier": "DASHLINK_786",
             "description": "The success of model-based approaches to systems health management depends largely on the quality of the underly- ing models. In model-based prognostics, it is especially the quality of the damage progression models, i.e., the models describing how damage evolves as the system operates, that determines the accuracy and precision of remaining useful life predictions. Several common forms of these models are gen- erally assumed in the literature, but are often not supported by physical evidence or physics-based analysis. In this paper, using a centrifugal pump as a case study, we develop differ- ent damage progression models. In simulation, we investigate how model changes influence prognostics performance. Re- sults demonstrate that, in some cases, simple damage progres- sion models are sufficient. But, in general, the results show a clear need for damage progression models that are accurate over long time horizons under varied loading conditions.",
-            "title": "Investigating the Effect of Damage Progression Model Choice on Prognostics Performance",
-            "programCode": [
-                "026:029"
-            ],
             "distribution": [
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/publication/2011_PHM_Granularity.pdf",
-                    "description": "2011_PHM_Granularity.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "2011_PHM_Granularity.pdf",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/publication/2011_PHM_Granularity.pdf",
+                    "mediaType": "application/pdf",
                     "title": "2011_PHM_Granularity.pdf"
                 }
             ],
-            "accrualPeriodicity": "irregular"
+            "identifier": "DASHLINK_786",
+            "issued": "2013-06-19",
+            "keyword": [
+                "dashlink",
+                "ames",
+                "nasa"
+            ],
+            "landingPage": "https://c3.nasa.gov/dashlink/resources/786/",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:029"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Dashlink"
+            },
+            "title": "Investigating the Effect of Damage Progression Model Choice on Prognostics Performance"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-4-ESC3-67P-M18-STR-REFL-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This CODMAC level 4 data set contains solar stray light corrected, radiometric calibrated and geometric distortion corrected (resampled) image data in in reflectance units (normalized and thus without unit), acquired by the OSIRIS Wide Angle Camera on the Rosetta spacecraft during the COMET ESCORT 3 mission phase, covering the period from 2015-06-30T23:25:00.000 to 2015-07-28T23:24:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V1.0 is the first version of this dataset: Lien corrected dataset after October 2018 PSA/PDS external peer review.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-4-esc3-67p-m18-str-refl-v1.0",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2021-05-21",
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
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-4-ESC3-67P-M18-STR-REFL-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-4-esc3-67p-m18-str-refl-v1.0",
-            "description": "This CODMAC level 4 data set contains solar stray light corrected, radiometric calibrated and geometric distortion corrected (resampled) image data in in reflectance units (normalized and thus without unit), acquired by the OSIRIS Wide Angle Camera on the Rosetta spacecraft during the COMET ESCORT 3 mission phase, covering the period from 2015-06-30T23:25:00.000 to 2015-07-28T23:24:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V1.0 is the first version of this dataset: Lien corrected dataset after October 2018 PSA/PDS external peer review.",
-            "title": "ROSETTA-ORBITER 67P OSIWAC 4 ESC3-MTP018 RDR-STR-REFL V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P OSIWAC 4 ESC3-MTP018 RDR-STR-REFL V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/IMPACTS/AMPR/DATA101",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Lang, Timothy .2022. Advanced Microwave Precipitation Radiometer (AMPR) IMPACTS [indicate subset used]. Dataset available online from the NASA Global Hydrometeorology Resource Center DAAC, Huntsville, Alabama, U.S.A. DOI: http://dx.doi.org/10.5067/IMPACTS/AMPR/DATA101",
-            "issued": "2022-03-23",
-            "temporal": "2020-01-18T13:39:13Z/2022-02-28T20:09:54Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-31",
-            "keyword": [
-                "spectral/engineering",
-                "microwave",
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
-            "identifier": "C2004708841-GHRC_DAAC",
             "description": "The Advanced Microwave Precipitation Radiometer (AMPR) IMPACTS dataset consists of brightness temperature measurements collected by the Advanced Microwave Precipitation Radiometer (AMPR) onboard the NASA ER-2 high-altitude research aircraft. AMPR provides multi-frequency microwave imagery, with high spatial and temporal resolution for deriving cloud, precipitation, water vapor and surface properties. These measurements were taken during the Investigation of Microphysics and Precipitation for Atlantic Coast-Threatening Snowstorms (IMPACTS) campaign. Funded by NASA\u2019s Earth Venture program, IMPACTS is the first comprehensive study of East Coast snowstorms in 30 years. Data files are available from January 18, 2020 through February 28, 2022 in netCDF-4 format.",
-            "title": "Advanced Microwave Precipitation Radiometer (AMPR) IMPACTS V1",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FIMPACTS%2FAMPR%2FDATA101",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FIMPACTS%2FAMPR%2FDATA101",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/portal/ghrc/search?q=amprimpacts&ghrccloud%2Fdata%2F=",
-                    "description": "Files may be downloaded directly to your workstation from this link",
                     "@type": "dcat:Distribution",
+                    "description": "Files may be downloaded directly to your workstation from this link",
+                    "downloadURL": "https://search.earthdata.nasa.gov/portal/ghrc/search?q=amprimpacts&ghrccloud%2Fdata%2F=",
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
-                    "downloadURL": "https://weather.msfc.nasa.gov/ampr",
-                    "description": "Advanced Microwave Precipitation Radiometer (AMPR)",
                     "@type": "dcat:Distribution",
+                    "description": "Advanced Microwave Precipitation Radiometer (AMPR)",
+                    "downloadURL": "https://weather.msfc.nasa.gov/ampr",
+                    "mediaType": "text/html",
                     "title": "View information related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/impacts/AMPR/doc/amprimpacts_dataset.pdf",
-                    "description": "The guide document contains detailed information about the dataset",
                     "@type": "dcat:Distribution",
+                    "description": "The guide document contains detailed information about the dataset",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/impacts/AMPR/doc/amprimpacts_dataset.pdf",
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
-                    "downloadURL": "https://doi.org/10.1109/ICMWFT.1989.763744",
-                    "description": "Advanced microwave precipitation radiometer",
                     "@type": "dcat:Distribution",
+                    "description": "Advanced microwave precipitation radiometer",
+                    "downloadURL": "https://doi.org/10.1109/ICMWFT.1989.763744",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://doi.org/http://doi.org/10.1175/jas3606.1",
-                    "description": "Classification of tropical oceanic precipitation using high-altitude aircraft microwave and electric field measurements",
                     "@type": "dcat:Distribution",
+                    "description": "Classification of tropical oceanic precipitation using high-altitude aircraft microwave and electric field measurements",
+                    "downloadURL": "http://doi.org/http://doi.org/10.1175/jas3606.1",
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
-                    "downloadURL": "http://doi.org/10.1109/36.239909",
-                    "description": "Comparisons of Precipitation Measurements by the Advanced Microwave Precipitation Radiometer and Multiparameter Radar",
                     "@type": "dcat:Distribution",
+                    "description": "Comparisons of Precipitation Measurements by the Advanced Microwave Precipitation Radiometer and Multiparameter Radar",
+                    "downloadURL": "http://doi.org/10.1109/36.239909",
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
+            "identifier": "C2004708841-GHRC_DAAC",
+            "issued": "2022-03-23",
+            "keyword": [
+                "spectral/engineering",
+                "microwave",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/IMPACTS/AMPR/DATA101",
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
             "spatial": "-118.51 30.6918 -64.3661 48.2585",
+            "temporal": "2020-01-18T13:39:13Z/2022-02-28T20:09:54Z",
             "theme": [
                 "IMPACTS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Advanced Microwave Precipitation Radiometer (AMPR) IMPACTS V1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC3-1025-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 3 phase 2015-07-01 to 2015-10-21. It is a Global Gravity measurement at the comet 67P and covers the time 2015-09-11T10:02:10.000 to 2015-09-11T17:31:24.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc3-1025-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC3-1025-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc3-1025-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 3 phase 2015-07-01 to 2015-10-21. It is a Global Gravity measurement at the comet 67P and covers the time 2015-09-11T10:02:10.000 to 2015-09-11T17:31:24.000.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 3 1025 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 3 1025 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://c3.nasa.gov/dashlink/resources/392/",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2011-06-07",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
-            "keyword": [
-                "nasa",
-                "ames",
-                "dashlink"
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
-            "identifier": "DASHLINK_392",
             "description": "The authors have formulated a Comprehensive Systems Engineering approach to Electro-Mechanical Actuator (EMA) Prognostics and Health Management (PHM) system development. The approach implements software tools to integrate simulation-based design principles and dynamic failure mode and effects analysis. It also provides automated failure mode insertion and propagation analysis, PHM algorithm design and verification, full dynamic simulations, code generation, and validation testing. This process aims to produce the appropriate fault detection and prediction algorithms needed for successful development of an EMA PHM system. \r\n\r\nAs an initial use case, the developed approach was implemented to develop and validate a model-based, virtual sensor software package for landing gear EMA PHM. This effort included creation of a dynamic, component-level system model that can be used to virtually sense parameters, detect degradation, isolate probable root cause, and assess severity. This model is also used as a virtual test bed for performing fault insertion analysis to address algorithm development and experimental prioritization. The developed model was validated using data from a test stand, which was specifically constructed for EMA PHM development. The model-based predictor was then coupled with failure mode diagnostics, advanced knowledge fusion, and failure mode progression algorithms to form a complete prototype EMA PHM solution.\r\n\r\nReproduced by kind permission of MFPT (www.mfpt.org).",
-            "title": "A Systems Engineering Approach to Electro-Mechanical Actuator Diagnostic and Prognostic Development",
-            "programCode": [
-                "026:029"
-            ],
             "distribution": [
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/publication/MFPT_2009_EMA.pdf",
-                    "description": "MFPT_2009_EMA.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "MFPT_2009_EMA.pdf",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/publication/MFPT_2009_EMA.pdf",
+                    "mediaType": "application/pdf",
                     "title": "MFPT_2009_EMA.pdf"
                 }
             ],
-            "accrualPeriodicity": "irregular"
+            "identifier": "DASHLINK_392",
+            "issued": "2011-06-07",
+            "keyword": [
+                "nasa",
+                "ames",
+                "dashlink"
+            ],
+            "landingPage": "https://c3.nasa.gov/dashlink/resources/392/",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:029"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Dashlink"
+            },
+            "title": "A Systems Engineering Approach to Electro-Mechanical Actuator Diagnostic and Prognostic Development"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-3-RDR-OCCULTATIONS-V3.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This data set is intended to include all reported timings of observed asteroid occultation events through Feb. 23, 2005, as well as asteroid occultation axes derived from those timings by David W. Dunham and David Herald. Some occultations by planetary satellites are also included.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-3-rdr-occultations-v3.0_e8xm-7fwi",
             "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "asteroid",
                 "support archives",
                 "satellite"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-3-RDR-OCCULTATIONS-V3.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-3-rdr-occultations-v3.0_e8xm-7fwi",
-            "description": "This data set is intended to include all reported timings of observed asteroid occultation events through Feb. 23, 2005, as well as asteroid occultation axes derived from those timings by David W. Dunham and David Herald. Some occultations by planetary satellites are also included.",
-            "title": "ASTEROID OCCULTATIONS",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "ASTEROID OCCULTATIONS"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=IHW-C-PPSTOKE-3-RDR-HALLEY-V1.0",
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
+            "description": "NASA's International Halley Watch (IHW) has created a Comet Halley Archive. The collection of data spans the full wavelength range as submitted by scientists to the IHW. The observations belong to one of the following Disciplines: Amateur, Astrometry, Infrared Studies, Large-Scale Phenomena, Meteor Studies, Near-Nucleus Studies, Photometry and Polarimetry, Radio Studies, and Spectroscopy and Spectrophotometry. The data collected by these nine disciplines were augmented by Spacecraft measurements. The data were submitted to IHW, but the evaluation and selection for the Archive has been the primary responsibility of the Discipline Specialist Teams for each network in cooperation with the Lead Center. The Photometry and Polarimetry Network collected 132 observations for the Stokes Parameters Subnetwork. These data cover the date range from 1985 December 30 through 1986 April 16.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ihw-c-ppstoke-3-rdr-halley-v1.0_e8xv-grd8",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international halley watch",
+                "halley"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=IHW-C-PPSTOKE-3-RDR-HALLEY-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ihw-c-ppstoke-3-rdr-halley-v1.0_e8xv-grd8",
-            "description": "NASA's International Halley Watch (IHW) has created a Comet Halley Archive. The collection of data spans the full wavelength range as submitted by scientists to the IHW. The observations belong to one of the following Disciplines: Amateur, Astrometry, Infrared Studies, Large-Scale Phenomena, Meteor Studies, Near-Nucleus Studies, Photometry and Polarimetry, Radio Studies, and Spectroscopy and Spectrophotometry. The data collected by these nine disciplines were augmented by Spacecraft measurements. The data were submitted to IHW, but the evaluation and selection for the Archive has been the primary responsibility of the Discipline Specialist Teams for each network in cooperation with the Lead Center. The Photometry and Polarimetry Network collected 132 observations for the Stokes Parameters Subnetwork. These data cover the date range from 1985 December 30 through 1986 April 16.",
-            "title": "IHW COMET HALLEY POLARIMETRIC STOKES PARAMETERS DATA V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "IHW COMET HALLEY POLARIMETRIC STOKES PARAMETERS DATA V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG1%2FVG2-J-ISS-2-EDR-V3.0",
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
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg1-vg2-j-iss-2-edr-v3.0_e8zb-d8hr",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "voyager",
                 "comet sl9/jupiter collision",
                 "j rings",
                 "jupiter"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG1%2FVG2-J-ISS-2-EDR-V3.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg1-vg2-j-iss-2-edr-v3.0_e8zb-d8hr",
-            "description": "not applicable",
-            "title": "VG1/VG2 JUPITER IMAGING SCIENCE SUBSYSTEM EDITED EDR V3.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "VG1/VG2 JUPITER IMAGING SCIENCE SUBSYSTEM EDITED EDR V3.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/699",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Stone, T.A., and P. Schlesinger. 2003. RLC State and Regional Boundaries for the Former Soviet Union. ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/699",
-            "issued": "2023-11-21",
-            "temporal": "1998-08-01T00:00:00Z/1999-08-03T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-12-02",
-            "keyword": [
-                "earth science",
-                "human dimensions",
-                "boundaries"
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
-            "identifier": "C2810672148-ORNL_CLOUD",
             "description": "This data set of state and regional boundaries was derived from the 1:3 million scale administrative boundaries (ESRI, 1998) for the land area of the Former Soviet Union. There are 162 administrative regions distinguished in this data set.  The vector map of state and regional boundaries for the FSU is in ArcView shapefile format.",
-            "graphic-preview-description": "Browse Image",
-            "title": "RLC State and Regional Boundaries for the Former Soviet Union",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/vegetation_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F699",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F699",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/global_vegetation/rlc_admin_boundaries/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/global_vegetation/rlc_admin_boundaries/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/RLC/guides/RLC_admin_bound.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/RLC/guides/RLC_admin_bound.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/699",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/699",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/global_vegetation/rlc_admin_boundaries/comp/fsuadm_projection.txt",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/global_vegetation/rlc_admin_boundaries/comp/fsuadm_projection.txt",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/global_vegetation/rlc_admin_boundaries/comp/fsuadm_readme.txt",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/global_vegetation/rlc_admin_boundaries/comp/fsuadm_readme.txt",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/global_vegetation/rlc_admin_boundaries/comp/RLC_admin_bound.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/global_vegetation/rlc_admin_boundaries/comp/RLC_admin_bound.pdf",
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
+            "identifier": "C2810672148-ORNL_CLOUD",
+            "issued": "2023-11-21",
+            "keyword": [
+                "earth science",
+                "human dimensions",
+                "boundaries"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/699",
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
             "spatial": "25.0 23.21 180.0 71.0",
+            "temporal": "1998-08-01T00:00:00Z/1999-08-03T23:59:59Z",
             "theme": [
                 "Vegetation",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "RLC State and Regional Boundaries for the Former Soviet Union"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.nasa.gov/d/e94p-rvxg",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "GeneLab Outreach",
+                "hasEmail": "mailto:genelab-outreach@lists.nasa.gov"
+            },
+            "description": "The environmental samples were collected with the polyester wipes from eight different locations in the International Space Station (ISS) during two consecutive sampling sessions (three months apart) within the ISS Microbial Observatory Experiment. DNA extracted from each of the samples was used to create amplicon libraries based on customized panel of 500 antimicrobial resistance genes followed by next-generation sequencing. This is the first study of that shows the reservoir of antimicrobial genes in the ISS. The International Space Station (ISS) as a closed built environment has its own environmental microbiome which is shaped by microgravity radiation and limited human presence. The microbial diversity associated with ISS environmental surfaces was investigated during this study. Polyester wipes and contact slides were used for sampling of eight various surface locations on the ISS at different time periods. The samples were retrieved and analyzed immediately upon the return to the Earth (via Soyuz TMA-14M or Dragon capsule from SpaceX). After surface sample collection contact slides containing nutrient media for the growth of bacteria and fungi were incubated at 25 xcb x9aC. The polyester wipes were processed to measure microbial burden (R2A Blood Agar and Potato Dextrose Agar) and recover cultivable bacteria as well as fungi. Subsequently viable microbial burden was assessed using Adenosine Triphosphate (ATP) assay and quantitative polymerase chain reaction (PCR) methods after propidium monoazide (PMA) treatment. The 16S-tag and metagenome analyses were used to elucidate viable microbial diversity. The cultivable bacterial population yield from the polyester wipes was very high (5 to 7-logs) when compared with the contact slides (102 to 103 CFU/m2). The PMA-qPCR analysis showed considerable variation of viable bacterial population (105 to 109 16S rDNA gene copies/m2) among locations sampled. Unlike contact slides polyester wipes cover much larger sample surface (~1 m2) and produce much more reliable results of the microbial diversity of the ISS covering both cultivable and non-cultivable species. The cultivable total and viable microbial diversity was determined utilizing state-of-the art molecular techniques. The implementation of the PMA assay before DNA extraction allowed distinguishing viable microorganisms which is crucial for determining their role to the crew health the ISS maintenance and the general knowledge of the closed environmentally controlled built systems.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "GeneLab Study Page",
+                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-66",
+                    "mediaType": "text/html",
+                    "title": "Microbial Observatory (ISS-MO): Antimicrobial resistance genes"
+                }
+            ],
+            "identifier": "nasa_genelab_GLDS-66_e94p-rvxg",
             "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
             "keyword": [
                 "sample processing",
                 "nucleic acid sequencing",
@@ -690319,1079 +690333,1041 @@
                 "sample collection",
                 "sequence analysis data transformation"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "GeneLab Outreach",
-                "hasEmail": "mailto:genelab-outreach@lists.nasa.gov"
-            },
+            "landingPage": "https://data.nasa.gov/d/e94p-rvxg",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "nasa_genelab_GLDS-66_e94p-rvxg",
-            "description": "The environmental samples were collected with the polyester wipes from eight different locations in the International Space Station (ISS) during two consecutive sampling sessions (three months apart) within the ISS Microbial Observatory Experiment. DNA extracted from each of the samples was used to create amplicon libraries based on customized panel of 500 antimicrobial resistance genes followed by next-generation sequencing. This is the first study of that shows the reservoir of antimicrobial genes in the ISS. The International Space Station (ISS) as a closed built environment has its own environmental microbiome which is shaped by microgravity radiation and limited human presence. The microbial diversity associated with ISS environmental surfaces was investigated during this study. Polyester wipes and contact slides were used for sampling of eight various surface locations on the ISS at different time periods. The samples were retrieved and analyzed immediately upon the return to the Earth (via Soyuz TMA-14M or Dragon capsule from SpaceX). After surface sample collection contact slides containing nutrient media for the growth of bacteria and fungi were incubated at 25 xcb x9aC. The polyester wipes were processed to measure microbial burden (R2A Blood Agar and Potato Dextrose Agar) and recover cultivable bacteria as well as fungi. Subsequently viable microbial burden was assessed using Adenosine Triphosphate (ATP) assay and quantitative polymerase chain reaction (PCR) methods after propidium monoazide (PMA) treatment. The 16S-tag and metagenome analyses were used to elucidate viable microbial diversity. The cultivable bacterial population yield from the polyester wipes was very high (5 to 7-logs) when compared with the contact slides (102 to 103 CFU/m2). The PMA-qPCR analysis showed considerable variation of viable bacterial population (105 to 109 16S rDNA gene copies/m2) among locations sampled. Unlike contact slides polyester wipes cover much larger sample surface (~1 m2) and produce much more reliable results of the microbial diversity of the ISS covering both cultivable and non-cultivable species. The cultivable total and viable microbial diversity was determined utilizing state-of-the art molecular techniques. The implementation of the PMA assay before DNA extraction allowed distinguishing viable microorganisms which is crucial for determining their role to the crew health the ISS maintenance and the general knowledge of the closed environmentally controlled built systems.",
-            "title": "Microbial Observatory (ISS-MO): Antimicrobial resistance genes",
-            "programCode": [
-                "026:005"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-66",
-                    "description": "GeneLab Study Page",
-                    "@type": "dcat:Distribution",
-                    "title": "Microbial Observatory (ISS-MO): Antimicrobial resistance genes"
-                }
-            ],
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "Microbial Observatory (ISS-MO): Antimicrobial resistance genes"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ASTER/AST_09.003",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "NASA/METI/AIST/Japan Spacesystems and U.S./Japan ASTER Science Team. AST_09.003. ASTER Level 2 Surface Radiance Product (SWIR & VNIR). Sioux Falls, South Dakota, USA. Archived by National Aeronautics and Space Administration, U.S. Government, NASA EOSDIS Land Processes Distributed Active Archive Center. https://doi.org/10.5067/ASTER/AST_09.003. https://doi.org/10.5067/ASTER/AST_09.003. The DOI landing page provides citations in APA and Chicago styles..",
-            "issued": "2000-03-06",
-            "temporal": "2000-03-06T00:30:05Z/2024-12-16T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-28",
-            "keyword": [
-                "visible wavelengths",
-                "spectral/engineering",
-                "earth science",
-                "ngda",
-                "national geospatial data asset",
-                "infrared wavelengths"
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
-            "identifier": "C1299783574-LPDAAC_ECS",
-            "description": "The ASTER Surface Radiance VNIR and SWIR (AST_09) is a multi-file product (https://lpdaac.usgs.gov/documents/996/ASTER_Earthdata_Search_Order_Instructions.pdf) that contains atmospherically corrected data for both the Visible and Near Infrared (VNIR) and Shortwave Infrared (SWIR) sensors. Each product delivery includes two Hierarchical Data Format - Earth Observing System (HDF-EOS) files: one for the VNIR, and the other for the SWIR. They are distinguished from one another by a one-second difference in the production time that appears as part of the file name. The more obvious distinguishing feature is the file size; the VNIR file is always the larger of the two. Both the VNIR and SWIR data are atmospherically corrected and are generated using the bands of the corresponding (ASTER Level 1B) (https://doi.org/10.5067/ASTER/AST_L1B.003) image.\r\n\r\nASTER Level 2 data requests for observations that occurred after May 27, 2020 will resort back to using the climatology ozone input. Additional information can be found in the ASTER L2 Processing Options Update (https://lpdaac.usgs.gov/news/aster-l2-processing-options-update/).\r\n\r\nStarting June 23, 2021, radiometric calibration coefficient Version 5 (RCC V5) will be applied to newly observed ASTER data and archived ASTER data products. Details regarding RCC V5 are described in the following journal article.\r\n\r\nTsuchida, S., Yamamoto, H., Kouyama, T., Obata, K., Sakuma, F., Tachikawa, T., Kamei, A., Arai, K., Czapla-Myers, J.S., Biggar, S.F., and Thome, K.J., 2020, Radiometric Degradation Curves for the ASTER VNIR Processing Using Vicarious and Lunar Calibrations: Remote Sensing, v. 12, no. 3, at https://doi.org/10.3390/rs12030427.\r\n\r\nAs of December 15, 2021, the LP DAAC has implemented changes to ASTER PGE Version 3.4, which will affect all ASTER Level 2 on-demand products.  Changes include:\r\n\u2022\tAura Ozone Monitoring Instrument (OMI) has been added as one of the ancillary ozone inputs for any observations made after May 27, 2020.  The sequence of fallbacks for ozone will remain the same.\r\n\u2022\tToolkit has been updated from Version 5.2.17 to 5.2.20.  Users may notice minor differences between the two versions.  Differences may include minuscule changes in digital numbers around the peripheral of the granule and boundaries of a cloud for Surface Reflectance and Surface Radiance (AST07 and AST09) QA Data Plane depending on the Operating System and libraries being used by the user to process the data.\r\n\r\nAdditionally, Climatology, which is one of the inputs for Ozone and Moisture, Temperature and Pressures (MTP) will be removed from the Earthdata Order Form.  It has been observed that PGEs generated with Climatology as an input yield noticeable differences statistically during image and spectral analysis.  Climatology will continue to be used as the final default if neither of the first two selectable options are available for Ozone and MTP.  Users can check the OPERATIONALQUALITYFLAGEXPLANATION field in the metadata or the output file for atmospheric parameters that were applied.\r\n\r\nAura OMI data are no longer available as an input for ASTER Level 2 data acquisitions after October 6, 2023. For data acquired after this date, ozone inputs will automatically fall back to climatology ozone inputs when Aura OMI is selected as an input. For more details, please refer to the Discontinuation of Aura OMI as an Input news announcement (https://lpdaac.usgs.gov/news/discontinuation-of-aura-omi-as-an-ancillary-ozone-input-for-aster-products/).",
-            "release-place": "Sioux Falls, South Dakota, USA",
-            "series-name": "AST_09.003",
-            "graphic-preview-description": "Browse image for Earthdata Search",
             "creator": "NASA/METI/AIST/Japan Spacesystems and U.S./Japan ASTER Science Team",
-            "title": "ASTER L2 Surface Radiance VNIR and SWIR V003",
-            "graphic-preview-file": "https://e4ftl01.cr.usgs.gov/WORKING/BRWS/Browse.001/2020.11.18/pg-BR1A0000-2020111801_014_003.1.VNIR.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The ASTER Surface Radiance VNIR and SWIR (AST_09) is a multi-file product (https://lpdaac.usgs.gov/documents/996/ASTER_Earthdata_Search_Order_Instructions.pdf) that contains atmospherically corrected data for both the Visible and Near Infrared (VNIR) and Shortwave Infrared (SWIR) sensors. Each product delivery includes two Hierarchical Data Format - Earth Observing System (HDF-EOS) files: one for the VNIR, and the other for the SWIR. They are distinguished from one another by a one-second difference in the production time that appears as part of the file name. The more obvious distinguishing feature is the file size; the VNIR file is always the larger of the two. Both the VNIR and SWIR data are atmospherically corrected and are generated using the bands of the corresponding (ASTER Level 1B) (https://doi.org/10.5067/ASTER/AST_L1B.003) image.\r\n\r\nASTER Level 2 data requests for observations that occurred after May 27, 2020 will resort back to using the climatology ozone input. Additional information can be found in the ASTER L2 Processing Options Update (https://lpdaac.usgs.gov/news/aster-l2-processing-options-update/).\r\n\r\nStarting June 23, 2021, radiometric calibration coefficient Version 5 (RCC V5) will be applied to newly observed ASTER data and archived ASTER data products. Details regarding RCC V5 are described in the following journal article.\r\n\r\nTsuchida, S., Yamamoto, H., Kouyama, T., Obata, K., Sakuma, F., Tachikawa, T., Kamei, A., Arai, K., Czapla-Myers, J.S., Biggar, S.F., and Thome, K.J., 2020, Radiometric Degradation Curves for the ASTER VNIR Processing Using Vicarious and Lunar Calibrations: Remote Sensing, v. 12, no. 3, at https://doi.org/10.3390/rs12030427.\r\n\r\nAs of December 15, 2021, the LP DAAC has implemented changes to ASTER PGE Version 3.4, which will affect all ASTER Level 2 on-demand products.  Changes include:\r\n\u2022\tAura Ozone Monitoring Instrument (OMI) has been added as one of the ancillary ozone inputs for any observations made after May 27, 2020.  The sequence of fallbacks for ozone will remain the same.\r\n\u2022\tToolkit has been updated from Version 5.2.17 to 5.2.20.  Users may notice minor differences between the two versions.  Differences may include minuscule changes in digital numbers around the peripheral of the granule and boundaries of a cloud for Surface Reflectance and Surface Radiance (AST07 and AST09) QA Data Plane depending on the Operating System and libraries being used by the user to process the data.\r\n\r\nAdditionally, Climatology, which is one of the inputs for Ozone and Moisture, Temperature and Pressures (MTP) will be removed from the Earthdata Order Form.  It has been observed that PGEs generated with Climatology as an input yield noticeable differences statistically during image and spectral analysis.  Climatology will continue to be used as the final default if neither of the first two selectable options are available for Ozone and MTP.  Users can check the OPERATIONALQUALITYFLAGEXPLANATION field in the metadata or the output file for atmospheric parameters that were applied.\r\n\r\nAura OMI data are no longer available as an input for ASTER Level 2 data acquisitions after October 6, 2023. For data acquired after this date, ozone inputs will automatically fall back to climatology ozone inputs when Aura OMI is selected as an input. For more details, please refer to the Discontinuation of Aura OMI as an Input news announcement (https://lpdaac.usgs.gov/news/discontinuation-of-aura-omi-as-an-ancillary-ozone-input-for-aster-products/).",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASTER%2FAST_09.003",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASTER%2FAST_09.003",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://lpdaac.usgs.gov",
-                    "description": "The LP DAAC website provides detailed information on discovery, distribution, access, and support of land data products.",
                     "@type": "dcat:Distribution",
+                    "description": "The LP DAAC website provides detailed information on discovery, distribution, access, and support of land data products.",
+                    "downloadURL": "https://lpdaac.usgs.gov",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asterweb.jpl.nasa.gov",
-                    "description": "The ASTER home page is maintained through NASA's Jet Propulsion Laboratory and documents various aspects of the ASTER mission.",
                     "@type": "dcat:Distribution",
+                    "description": "The ASTER home page is maintained through NASA's Jet Propulsion Laboratory and documents various aspects of the ASTER mission.",
+                    "downloadURL": "https://asterweb.jpl.nasa.gov",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/ASTER/AST_09.003",
-                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
+                    "downloadURL": "https://doi.org/10.5067/ASTER/AST_09.003",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/x-hdf",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=C1299783574-LPDAAC_ECS",
-                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=C1299783574-LPDAAC_ECS",
+                    "mediaType": "application/x-hdf",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://lpdaac.usgs.gov/documents/76/AST_09_ATBD.pdf",
-                    "description": "The ATBD provides physical theory and mathematical procedures for the calculations used to produce the data products.",
                     "@type": "dcat:Distribution",
+                    "description": "The ATBD provides physical theory and mathematical procedures for the calculations used to produce the data products.",
+                    "downloadURL": "https://lpdaac.usgs.gov/documents/76/AST_09_ATBD.pdf",
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
-                    "downloadURL": "https://lpdaac.usgs.gov/documents/75/AST_09_User_Guide_V3.pdf",
-                    "description": "ASTER Higher-Level Product User Guide",
                     "@type": "dcat:Distribution",
+                    "description": "ASTER Higher-Level Product User Guide",
+                    "downloadURL": "https://lpdaac.usgs.gov/documents/75/AST_09_User_Guide_V3.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://lpdaac.usgs.gov/documents/175/ASTER_L1_Product_Specifications.pdf",
-                    "description": "The ASTER Level-1 Products Specification provides a description of the data file.",
                     "@type": "dcat:Distribution",
+                    "description": "The ASTER Level-1 Products Specification provides a description of the data file.",
+                    "downloadURL": "https://lpdaac.usgs.gov/documents/175/ASTER_L1_Product_Specifications.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View information related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://lpdaac.usgs.gov/documents/996/ASTER_Earthdata_Search_Order_Instructions.pdf",
-                    "description": "ASTER Order Instructions",
                     "@type": "dcat:Distribution",
+                    "description": "ASTER Order Instructions",
+                    "downloadURL": "https://lpdaac.usgs.gov/documents/996/ASTER_Earthdata_Search_Order_Instructions.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's how-to documentation"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://e4ftl01.cr.usgs.gov/WORKING/BRWS/Browse.001/2020.11.18/pg-BR1A0000-2020111801_014_003.1.VNIR.jpg",
-                    "description": "Browse image for Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse image for Earthdata Search",
+                    "downloadURL": "https://e4ftl01.cr.usgs.gov/WORKING/BRWS/Browse.001/2020.11.18/pg-BR1A0000-2020111801_014_003.1.VNIR.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://lpdaac.usgs.gov/documents/1319/ASTER_User_Handbook_v4.pdf",
-                    "description": "The ASTER User Handbook provides in depth information on ASTER data products.",
                     "@type": "dcat:Distribution",
+                    "description": "The ASTER User Handbook provides in depth information on ASTER data products.",
+                    "downloadURL": "https://lpdaac.usgs.gov/documents/1319/ASTER_User_Handbook_v4.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
                 }
             ],
+            "graphic-preview-description": "Browse image for Earthdata Search",
+            "graphic-preview-file": "https://e4ftl01.cr.usgs.gov/WORKING/BRWS/Browse.001/2020.11.18/pg-BR1A0000-2020111801_014_003.1.VNIR.jpg",
+            "identifier": "C1299783574-LPDAAC_ECS",
+            "issued": "2000-03-06",
+            "keyword": [
+                "visible wavelengths",
+                "spectral/engineering",
+                "earth science",
+                "ngda",
+                "national geospatial data asset",
+                "infrared wavelengths"
+            ],
+            "landingPage": "https://doi.org/10.5067/ASTER/AST_09.003",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2024-11-28",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "LP DAAC"
+            },
+            "release-place": "Sioux Falls, South Dakota, USA",
+            "series-name": "AST_09.003",
             "spatial": "-180.0 -83.0 180.0 83.0",
+            "temporal": "2000-03-06T00:30:05Z/2024-12-16T00:00:00Z",
             "theme": [
                 "Terra",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "ASTER L2 Surface Radiance VNIR and SWIR V003"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.7265/27c5-gz36",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Yup'ik Environmental Knowledge Project (Community Page), Version 1. Version 1. Archived by National Aeronautics and Space Administration, U.S. Government, NSIDC. https://doi.org/10.7265/27c5-gz36.",
-            "issued": "2000-01-01",
-            "temporal": "2000-01-01T00:00:00Z/2020-12-31T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-12-31",
-            "keyword": [
-                "environmental features & use",
-                "human dimensions",
-                "indigenous knowledge",
-                "youth involvement",
-                "place names",
-                "community-based monitoring",
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
-            "identifier": "C1728290490-NSIDCV0",
             "description": "Since 2000, the Calista Elders Council (CEC) staff has worked with elders from Bering Sea coastal communities to document Yup'ik place names. Elders have been eager to teach young people their rich history and named places of their homeland, including camp and settlement sites, rivers, sloughs, rocks, ponds, even sandbars and underwater channels. More than 3,000 names have been identified with Yup'ik views on the importance of place names, the land, values, and language.\n\nSupporting Yup\u2019ik Education\nOne area of growth stemming from the Yup\u2019ik Environmental Knowledge Project has been collaboration with the Lower Kuskokwim School District. Teachers and their students have participated in training sessions on atlas technology and how to add content. As part of the district\u2019s curriculum development, high school students collect and share the history and culture of the Yup\u2019ik way of life.",
-            "title": "Yup'ik Environmental Knowledge Project (Community Page), Version 1",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.7265%2F27c5-gz36",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.7265%2F27c5-gz36",
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
-                    "downloadURL": "https://doi.org/10.7265/27c5-gz36",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.7265/27c5-gz36",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.7265/27c5-gz36",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.7265/27c5-gz36",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
-            "theme": [
-                "geospatial"
+            "identifier": "C1728290490-NSIDCV0",
+            "issued": "2000-01-01",
+            "keyword": [
+                "environmental features & use",
+                "human dimensions",
+                "indigenous knowledge",
+                "youth involvement",
+                "place names",
+                "community-based monitoring",
+                "earth science"
             ],
+            "landingPage": "https://doi.org/10.7265/27c5-gz36",
             "language": [
                 "en-US"
-            ]
+            ],
+            "modified": "2020-12-31",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NSIDC"
+            },
+            "temporal": "2000-01-01T00:00:00Z/2020-12-31T23:59:59.999Z",
+            "theme": [
+                "geospatial"
+            ],
+            "title": "Yup'ik Environmental Knowledge Project (Community Page), Version 1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-3-PRL-67PCHURYUMOV-M05-V1.0",
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
+            "description": "This data set contains calibrated images acquired by the OSIRIS Narrow Angle\nCamera during the prelanding phase of the Rosetta mission at the comet 67P,\ncovering the period from 2014-07-02 to 2014-08-01.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-3-prl-67pchuryumov-m05-v1.0_e9a8-w6r2",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-3-PRL-67PCHURYUMOV-M05-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-3-prl-67pchuryumov-m05-v1.0_e9a8-w6r2",
-            "description": "This data set contains calibrated images acquired by the OSIRIS Narrow Angle\nCamera during the prelanding phase of the Rosetta mission at the comet 67P,\ncovering the period from 2014-07-02 to 2014-08-01.",
-            "title": "ROSETTA-ORBITER COMET PRELANDING OSINAC 3 RDR MTP 005 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER COMET PRELANDING OSINAC 3 RDR MTP 005 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/AQR50-3S1CS",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "NASA Aquarius project. 2017-12-07. Aquarius Official Release Level 3 Sea Surface Salinity Standard Mapped Image Daily Data. Version 5.0. Aquarius Sea Surface Salinity Products. Goddard Space Flight Center, 8800 Greenbelt Rd.; Greeenbelt, MD., 20771, USA. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/GSFC OBPG. https://doi.org/10.5067/AQR50-3S1CS. http://podaac.jpl.nasa.gov/SeaSurfaceSalinity/Aquarius. NASA Aquarius project, NASA/GSFC OBPG, 2017-12-07, Aquarius Official Release Level 3 Sea Surface Salinity Standard Mapped Image Daily Data V5.0, http://podaac.jpl.nasa.gov/SeaSurfaceSalinity/Aquarius.",
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
-            "identifier": "C2491756421-POCLOUD",
-            "description": "Aquarius Level 3 sea surface salinity (SSS) standard mapped image data contains gridded 1 degree spatial resolution SSS averaged over daily, 7 day, monthly, and seasonal time scales.\nThis particular data set is the Daily sea surface salinity product for version 5.0 of the Aquarius data set, which is the official end of mission public data release from the AQUARIUS/SAC-D mission. The Aquarius instrument is onboard the AQUARIUS/SAC-D satellite, a collaborative effort between NASA and the Argentinian Space Agency Comision Nacional de Actividades Espaciales (CONAE). The instrument consists of three radiometers in push broom alignment at incidence angles of 29, 38, and 46 degrees incidence angles relative to the shadow side of the orbit.  Footprints for the beams are: 76 km (along-track) x 94 km (cross-track), 84 km x 120 km and 96km x 156 km, yielding a total cross-track swath of 370 km. The radiometers measure brightness temperature at 1.413 GHz in their respective horizontal and vertical polarizations (TH and TV). A scatterometer operating at 1.26 GHz measures ocean backscatter in each footprint that is used for surface roughness corrections in the estimation of salinity. The scatterometer has an approximate 390km swath.",
-            "release-place": "Goddard Space Flight Center, 8800 Greenbelt Rd.; Greeenbelt, MD., 20771, USA",
-            "series-name": "Aquarius Official Release Level 3 Sea Surface Salinity Standard Mapped Image Daily Data",
-            "graphic-preview-description": "Thumbnail",
             "creator": "NASA Aquarius project",
-            "title": "Aquarius Official Release Level 3 Sea Surface Salinity Standard Mapped Image Daily Data V5.0",
-            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/AQUARIUS_L3_SSS_SMI_DAILY_V5.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "Aquarius Level 3 sea surface salinity (SSS) standard mapped image data contains gridded 1 degree spatial resolution SSS averaged over daily, 7 day, monthly, and seasonal time scales.\nThis particular data set is the Daily sea surface salinity product for version 5.0 of the Aquarius data set, which is the official end of mission public data release from the AQUARIUS/SAC-D mission. The Aquarius instrument is onboard the AQUARIUS/SAC-D satellite, a collaborative effort between NASA and the Argentinian Space Agency Comision Nacional de Actividades Espaciales (CONAE). The instrument consists of three radiometers in push broom alignment at incidence angles of 29, 38, and 46 degrees incidence angles relative to the shadow side of the orbit.  Footprints for the beams are: 76 km (along-track) x 94 km (cross-track), 84 km x 120 km and 96km x 156 km, yielding a total cross-track swath of 370 km. The radiometers measure brightness temperature at 1.413 GHz in their respective horizontal and vertical polarizations (TH and TV). A scatterometer operating at 1.26 GHz measures ocean backscatter in each footprint that is used for surface roughness corrections in the estimation of salinity. The scatterometer has an approximate 390km swath.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAQR50-3S1CS",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAQR50-3S1CS",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://podaac.jpl.nasa.gov/aquarius/gallery",
-                    "description": "Level 3 Data Browser",
                     "@type": "dcat:Distribution",
+                    "description": "Level 3 Data Browser",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/aquarius/gallery",
+                    "mediaType": "text/html",
                     "title": "Use this dataset in a web based tool"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/aquarius/open/docs/v5/AQ-010-UG-0008_AquariusUserGuide_DatasetV5.0.pdf",
-                    "description": "Aquarius Data User's Guide",
                     "@type": "dcat:Distribution",
+                    "description": "Aquarius Data User's Guide",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/aquarius/open/docs/v5/AQ-010-UG-0008_AquariusUserGuide_DatasetV5.0.pdf",
+                    "mediaType": "application/pdf",
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
-                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/AQUARIUS_L3_SSS_SMI_DAILY_V5.jpg",
-                    "description": "Thumbnail",
                     "@type": "dcat:Distribution",
+                    "description": "Thumbnail",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/AQUARIUS_L3_SSS_SMI_DAILY_V5.jpg",
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
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2491756421-POCLOUD",
-                    "description": "HTTPS endpoint for data browse and download",
                     "@type": "dcat:Distribution",
+                    "description": "HTTPS endpoint for data browse and download",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2491756421-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2491756421-POCLOUD",
-                    "description": "Browse granule search results in Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse granule search results in Earthdata Search",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2491756421-POCLOUD",
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
+            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/AQUARIUS_L3_SSS_SMI_DAILY_V5.jpg",
+            "identifier": "C2491756421-POCLOUD",
+            "issued": "2017-10-21",
+            "keyword": [
+                "oceans",
+                "earth science",
+                "salinity/density"
+            ],
+            "landingPage": "https://doi.org/10.5067/AQR50-3S1CS",
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
+            "series-name": "Aquarius Official Release Level 3 Sea Surface Salinity Standard Mapped Image Daily Data",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2011-08-25T01:45:23Z/2015-06-07T12:45:21Z",
             "theme": [
                 "AQUARIUS SAC-D",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Aquarius Official Release Level 3 Sea Surface Salinity Standard Mapped Image Daily Data V5.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/GPMGV/OLYMPEX/NPOL/DATA301",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Wolff, David , David A Marks, Walter A Petersen and Jason  Pippit.2017. GPM Ground Validation NASA S-Band Dual Polarimetric (NPOL) Doppler Radar OLYMPEX [indicate subset used]. Dataset available online from the NASA Global Hydrometeorology Resource Center DAAC, Huntsville, Alabama, U.S.A. DOI: http://dx.doi.org/10.5067/GPMGV/OLYMPEX/NPOL/DATA301",
-            "issued": "2017-10-10",
-            "temporal": "2015-11-05T16:12:56Z/2016-01-15T00:17:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-04-28",
-            "keyword": [
-                "atmospheric water vapor",
-                "atmosphere",
-                "earth science",
-                "precipitation",
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
-            "identifier": "C1979639066-GHRC_DAAC",
             "description": "The GPM Ground Validation NASA S-Band Dual Polarimetric (NPOL) Doppler Radar OLYMPEX V2 dataset consists of rain rate, reflectivity, Doppler velocity, and other radar measurements obtained from the NPOL radar during the Global Precipitation Mission (GPM) Olympic Mountains Experiment (OLYMPEX) campaign. NPOL,developed by a research team from Wallops Flight Facility,  is a fully transportable and self-contained S-band (10 cm), scanning dual-polarimetric Doppler research radar that was placed near the ocean on the Olympic Peninsula. Data files are available from November 5, 2015 thru January 15, 2016 in Universal Format (UF), with browse imagery files in PNG format containing corrected radar reflectivity, differential reflectivity, specific differential phase, differential phase, co-polar correlation, and Doppler velocity images.",
-            "graphic-preview-description": "Browse images illustrate the nature and coverage of the data",
-            "title": "GPM Ground Validation NASA S-Band Dual Polarimetric (NPOL) Doppler Radar OLYMPEX V2",
-            "graphic-preview-file": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/olympex/NPOL/browse/",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGPMGV%2FOLYMPEX%2FNPOL%2FDATA301",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGPMGV%2FOLYMPEX%2FNPOL%2FDATA301",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=gpmnpololyx2",
-                    "description": "Files may be downloaded directly to your workstation from this link",
                     "@type": "dcat:Distribution",
+                    "description": "Files may be downloaded directly to your workstation from this link",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=gpmnpololyx2",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/olympex/NPOL/browse/olympex_npol1_20160106_003728_CZ_sw00_PPI.png",
-                    "description": "Sample browse image",
                     "@type": "dcat:Distribution",
+                    "description": "Sample browse image",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/olympex/NPOL/browse/olympex_npol1_20160106_003728_CZ_sw00_PPI.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://wallops-prf.gsfc.nasa.gov/Field_Campaigns/Olympex/",
-                    "description": "Olympic Mountain Experiment (Olympex)",
                     "@type": "dcat:Distribution",
+                    "description": "Olympic Mountain Experiment (Olympex)",
+                    "downloadURL": "https://wallops-prf.gsfc.nasa.gov/Field_Campaigns/Olympex/",
+                    "mediaType": "text/html",
                     "title": "View information related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://olympex.atmos.washington.edu/",
-                    "description": "University of Washington OLYMPEX project web site",
                     "@type": "dcat:Distribution",
+                    "description": "University of Washington OLYMPEX project web site",
+                    "downloadURL": "http://olympex.atmos.washington.edu/",
+                    "mediaType": "text/html",
                     "title": "View information related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/olympex/NPOL/doc/gpmnpololyx2_dataset.pdf",
-                    "description": "The guide document contains detailed information about the dataset",
                     "@type": "dcat:Distribution",
+                    "description": "The guide document contains detailed information about the dataset",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/olympex/NPOL/doc/gpmnpololyx2_dataset.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/olympex/NPOL/doc/DSDflowchart.png",
-                    "description": "GPM-GV DSD Retrievals Flowchart",
                     "@type": "dcat:Distribution",
+                    "description": "GPM-GV DSD Retrievals Flowchart",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/olympex/NPOL/doc/DSDflowchart.png",
+                    "mediaType": "image/png",
                     "title": "View the primary investigator's documentation for this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/olympex/NPOL/doc/NPOL_OLYMPEXv2_README.txt",
-                    "description": "NPOL OLYMPEX Data Processing V2.0 Read Me File",
                     "@type": "dcat:Distribution",
+                    "description": "NPOL OLYMPEX Data Processing V2.0 Read Me File",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/olympex/NPOL/doc/NPOL_OLYMPEXv2_README.txt",
+                    "mediaType": "text/html",
                     "title": "View the primary investigator's documentation for this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.1175/2008BAMS2177.1",
-                    "description": "Potential Role of Dual-Polarization Radar in the Validation of Satellite Precipitation Measurements",
                     "@type": "dcat:Distribution",
+                    "description": "Potential Role of Dual-Polarization Radar in the Validation of Satellite Precipitation Measurements",
+                    "downloadURL": "https://doi.org/10.1175/2008BAMS2177.1",
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
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/home/field-campaigns/olympex",
-                    "description": "GHRC OLYMPEX project web page",
                     "@type": "dcat:Distribution",
+                    "description": "GHRC OLYMPEX project web page",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/home/field-campaigns/olympex",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
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
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/olympex/NPOL/browse/",
-                    "description": "Browse images illustrate the nature and coverage of the data",
                     "@type": "dcat:Distribution",
+                    "description": "Browse images illustrate the nature and coverage of the data",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/olympex/NPOL/browse/",
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
+            "graphic-preview-file": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/olympex/NPOL/browse/",
+            "identifier": "C1979639066-GHRC_DAAC",
+            "issued": "2017-10-10",
+            "keyword": [
+                "atmospheric water vapor",
+                "atmosphere",
+                "earth science",
+                "precipitation",
+                "radar",
+                "spectral/engineering"
+            ],
+            "landingPage": "https://doi.org/10.5067/GPMGV/OLYMPEX/NPOL/DATA301",
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
             "spatial": "-126.275 45.9605 -122.256 48.6684",
+            "temporal": "2015-11-05T16:12:56Z/2016-01-15T00:17:00Z",
             "theme": [
                 "OLYMPEX",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "GPM Ground Validation NASA S-Band Dual Polarimetric (NPOL) Doppler Radar OLYMPEX V2"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ECL5S-SIV44",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "ECCO Consortium, Fukumori, I., Wang, O., Fenty, I., Forget, G., Heimbach, P., & Ponte, R. M.. 2021-04-19. ECCO Sea-Ice Velocity - Snapshot llc90 Grid (Version 4 Release 4). Version V4r4. PO.DAAC. Archived by National Aeronautics and Space Administration, U.S. Government, PO.DAAC. https://doi.org/10.5067/ECL5S-SIV44. ECCO; ECCO Consortium, Fukumori, I., Wang, O., Fenty, I., Forget, G., Heimbach, P., & Ponte, R. M.; 2020; ECCO Sea-Ice Velocity - Snapshot llc90 Grid (Version 4 Release 4); 10.5067/ECL5S-SIV44; https://podaac.jpl.nasa.gov/ECCO.",
-            "issued": "2021-01-01",
-            "temporal": "1992-01-01T00:00:00Z/2018-01-01T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2017-12-31",
-            "references": [
-                "https://doi.org/10.5281/zenodo.3765928"
-            ],
-            "keyword": [
-                "cryosphere",
-                "models",
-                "earth science reanalyses/assimilation models",
-                "earth science services",
-                "earth science",
-                "sea ice"
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
-            "identifier": "C1991543768-POCLOUD",
-            "description": "This dataset provides instantaneous sea-ice velocity on the native Lat-Lon-Cap 90 (LLC90) model grid from the ECCO Version 4 Release 4 (V4r4) ocean and sea-ice state estimate. Estimating the Circulation and Climate of the Ocean (ECCO) ocean and sea-ice state estimates are dynamically and kinematically-consistent reconstructions of the three-dimensional time-evolving ocean, sea-ice, and surface atmospheric states. ECCO V4r4 is a free-running solution of the 1-degree global configuration of the MIT general circulation model (MITgcm) that has been fit to observations in a least-squares sense. Observational data constraints used in V4r4 include sea surface height (SSH) from satellite altimeters [ERS-1/2, TOPEX/Poseidon, GFO, ENVISAT, Jason-1,2,3, CryoSat-2, and SARAL/AltiKa]; sea surface temperature (SST) from satellite radiometers [AVHRR], sea surface salinity (SSS) from the Aquarius satellite radiometer/scatterometer, ocean bottom pressure (OBP) from the GRACE satellite gravimeter; sea ice concentration from satellite radiometers [SSM/I and SSMIS], and in-situ ocean temperature and salinity measured with conductivity-temperature-depth (CTD) sensors and expendable bathythermographs (XBTs) from several programs [e.g., WOCE, GO-SHIP, Argo, and others] and platforms [e.g., research vessels, gliders, moorings, ice-tethered profilers, and instrumented pinnipeds]. V4r4 covers the period 1992-01-01T12:00:00 to 2018-01-01T00:00:00.",
-            "release-place": "PO.DAAC",
-            "graphic-preview-description": "Thumbnail image for Website",
             "creator": "ECCO Consortium, Fukumori, I., Wang, O., Fenty, I., Forget, G., Heimbach, P., & Ponte, R. M.",
-            "title": "ECCO Sea-Ice Velocity - Snapshot llc90 Grid (Version 4 Release 4)",
-            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/ECCO_L4_SEA_ICE_VELOCITY_LLC0090GRID_SNAPSHOT_V4R4.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "This dataset provides instantaneous sea-ice velocity on the native Lat-Lon-Cap 90 (LLC90) model grid from the ECCO Version 4 Release 4 (V4r4) ocean and sea-ice state estimate. Estimating the Circulation and Climate of the Ocean (ECCO) ocean and sea-ice state estimates are dynamically and kinematically-consistent reconstructions of the three-dimensional time-evolving ocean, sea-ice, and surface atmospheric states. ECCO V4r4 is a free-running solution of the 1-degree global configuration of the MIT general circulation model (MITgcm) that has been fit to observations in a least-squares sense. Observational data constraints used in V4r4 include sea surface height (SSH) from satellite altimeters [ERS-1/2, TOPEX/Poseidon, GFO, ENVISAT, Jason-1,2,3, CryoSat-2, and SARAL/AltiKa]; sea surface temperature (SST) from satellite radiometers [AVHRR], sea surface salinity (SSS) from the Aquarius satellite radiometer/scatterometer, ocean bottom pressure (OBP) from the GRACE satellite gravimeter; sea ice concentration from satellite radiometers [SSM/I and SSMIS], and in-situ ocean temperature and salinity measured with conductivity-temperature-depth (CTD) sensors and expendable bathythermographs (XBTs) from several programs [e.g., WOCE, GO-SHIP, Argo, and others] and platforms [e.g., research vessels, gliders, moorings, ice-tethered profilers, and instrumented pinnipeds]. V4r4 covers the period 1992-01-01T12:00:00 to 2018-01-01T00:00:00.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FECL5S-SIV44",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FECL5S-SIV44",
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
-                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/ECCO_L4_SEA_ICE_VELOCITY_LLC0090GRID_SNAPSHOT_V4R4.jpg",
-                    "description": "Thumbnail image for Website",
                     "@type": "dcat:Distribution",
+                    "description": "Thumbnail image for Website",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/ECCO_L4_SEA_ICE_VELOCITY_LLC0090GRID_SNAPSHOT_V4R4.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/ECL5S-SIV44",
-                    "description": "Access the data set landing page for the collection.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data set landing page for the collection.",
+                    "downloadURL": "https://doi.org/10.5067/ECL5S-SIV44",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1991543768-POCLOUD",
-                    "description": "Browse granule search results in Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse granule search results in Earthdata Search",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1991543768-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C1991543768-POCLOUD/temporal",
-                    "description": "Browse and download granules over HTTPS using the virtual directories service",
                     "@type": "dcat:Distribution",
+                    "description": "Browse and download granules over HTTPS using the virtual directories service",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C1991543768-POCLOUD/temporal",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 }
             ],
+            "graphic-preview-description": "Thumbnail image for Website",
+            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/ECCO_L4_SEA_ICE_VELOCITY_LLC0090GRID_SNAPSHOT_V4R4.jpg",
+            "identifier": "C1991543768-POCLOUD",
+            "issued": "2021-01-01",
+            "keyword": [
+                "cryosphere",
+                "models",
+                "earth science reanalyses/assimilation models",
+                "earth science services",
+                "earth science",
+                "sea ice"
+            ],
+            "landingPage": "https://doi.org/10.5067/ECL5S-SIV44",
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
+            "title": "ECCO Sea-Ice Velocity - Snapshot llc90 Grid (Version 4 Release 4)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/516",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Fitzjarrald, D.R. 2000. BOREAS TF-08 NSA-OJP Tower Flux, Meteorological, and Soil Temperature Data. ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/516",
-            "issued": "2023-11-22",
-            "temporal": "1994-05-24T00:00:00Z/1996-11-12T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-11-28",
-            "keyword": [
-                "biosphere",
-                "precipitation",
-                "atmospheric winds",
-                "atmospheric water vapor",
-                "atmospheric temperature",
-                "vegetation",
-                "soils",
-                "atmospheric radiation",
-                "atmospheric pressure",
-                "atmospheric chemistry",
-                "atmosphere",
-                "earth science",
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
-            "identifier": "C2808093089-ORNL_CLOUD",
             "description": "Energy, carbon dioxide, and water vapor flux data collected by the BOREAS TF-08 team.",
-            "graphic-preview-description": "Browse Image",
-            "title": "BOREAS TF-08 NSA-OJP Tower Flux, Meteorological, and Soil Temperature Data",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/boreas_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F516",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F516",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/boreas/TF/tf08tflx/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/boreas/TF/tf08tflx/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/BOREAS/guides/TF08_Flux.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/BOREAS/guides/TF08_Flux.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/516",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/516",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TF/tf08tflx/comp/tf08tflx.def",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TF/tf08tflx/comp/tf08tflx.def",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/msword",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TF/tf08tflx/comp/TF08_Flux.doc",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TF/tf08tflx/comp/TF08_Flux.doc",
+                    "mediaType": "application/msword",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TF/tf08tflx/comp/TF08_Flux.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TF/tf08tflx/comp/TF08_Flux.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TF/tf08tflx/comp/TF08_Flux.txt",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TF/tf08tflx/comp/TF08_Flux.txt",
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
+            "identifier": "C2808093089-ORNL_CLOUD",
+            "issued": "2023-11-22",
+            "keyword": [
+                "biosphere",
+                "precipitation",
+                "atmospheric winds",
+                "atmospheric water vapor",
+                "atmospheric temperature",
+                "vegetation",
+                "soils",
+                "atmospheric radiation",
+                "atmospheric pressure",
+                "atmospheric chemistry",
+                "atmosphere",
+                "earth science",
+                "land surface"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/516",
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
             "spatial": "55.93 -98.62",
+            "temporal": "1994-05-24T00:00:00Z/1996-11-12T23:59:59Z",
             "theme": [
                 "BOREAS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "BOREAS TF-08 NSA-OJP Tower Flux, Meteorological, and Soil Temperature Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-5-EXT2-67P-M30-GEO-V1.0",
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
+            "description": "This CODMAC level 5 data set contains derived data products that include pixel-precise georeferencing information, acquired by the OSIRIS Narrow Angle Camera on the Rosetta spacecraft during the ROSETTA EXTENSION 2 mission phase, covering the period from 2016-05-31T23:25:00.000 to 2016-06-28T23:24:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V1.0 is the first version of this dataset: Lien corrected dataset after October 2018 PSA/PDS external peer review.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-5-ext2-67p-m30-geo-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-5-EXT2-67P-M30-GEO-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-5-ext2-67p-m30-geo-v1.0",
-            "description": "This CODMAC level 5 data set contains derived data products that include pixel-precise georeferencing information, acquired by the OSIRIS Narrow Angle Camera on the Rosetta spacecraft during the ROSETTA EXTENSION 2 mission phase, covering the period from 2016-05-31T23:25:00.000 to 2016-06-28T23:24:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V1.0 is the first version of this dataset: Lien corrected dataset after October 2018 PSA/PDS external peer review.",
-            "title": "ROSETTA-ORBITER 67P OSINAC 5 EXT2-MTP030 DDR-GEO V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P OSINAC 5 EXT2-MTP030 DDR-GEO V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG1-S-CRS-4-SUMM-D1%2FD2-192SEC-V1.0",
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
+            "description": "This data set describes the counting\nrate data from detectors D1 and D2 in the Cosmic Ray System (CRS) electron\ntelescope (TET) on Voyager 1 during the Saturn encounter. The D1 detector\nnominally responds to electrons with kinetic energies above approximately\n1 MeV, and the D2 detector, above approximately 2.5 MeV (see detector\ndescription for details).",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg1-s-crs-4-summ-d1-d2-192sec-v1.0_e9n2-ccyg",
+            "issued": "2021-05-21",
+            "keyword": [
+                "voyager",
+                "saturn"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG1-S-CRS-4-SUMM-D1%2FD2-192SEC-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg1-s-crs-4-summ-d1-d2-192sec-v1.0_e9n2-ccyg",
-            "description": "This data set describes the counting\nrate data from detectors D1 and D2 in the Cosmic Ray System (CRS) electron\ntelescope (TET) on Voyager 1 during the Saturn encounter. The D1 detector\nnominally responds to electrons with kinetic energies above approximately\n1 MeV, and the D2 detector, above approximately 2.5 MeV (see detector\ndescription for details).",
-            "title": "VG1 SAT CRS RESAMPLED SUMMARY D1 RATE\n                                      ELEC 192SEC V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "VG1 SAT CRS RESAMPLED SUMMARY D1 RATE\n                                      ELEC 192SEC V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://spotthestation.nasa.gov",
+            "accrualPeriodicity": "R/P1D",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2021-10-07",
-            "temporal": "2021-10-07T00:00:00Z/P1D",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-31",
-            "keyword": [
-                "location",
-                "trajectory",
-                "topo",
-                "space",
-                "ephemeris",
-                "station",
-                "coordinates",
-                "coords",
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
-            "identifier": "nasa-iss-data_2021-10-07_e9n3-fzyh",
+            "dataQuality": true,
             "description": "This data represents the best estimated real-time trajectory and local sightings opportunities for the International Space Station (ISS) as generated by the Trajectory Operations and Planning (TOPO) flight controllers at Johnson Space Center.",
-            "title": "ISS_COORDS_2021-10-07",
-            "programCode": [
-                "026:004"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -691514,439 +691490,480 @@
                     "title": "XMLsightingData_natparksUSA02"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "nasa-iss-data_2021-10-07_e9n3-fzyh",
+            "issued": "2021-10-07",
+            "keyword": [
+                "location",
+                "trajectory",
+                "topo",
+                "space",
+                "ephemeris",
+                "station",
+                "coordinates",
+                "coords",
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
+            "temporal": "2021-10-07T00:00:00Z/P1D",
             "theme": [
                 "Space Science"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "ISS_COORDS_2021-10-07"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC2-0781-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 2 phase 2015-03-11 to 2015-06-30. It is a Global Gravity measurement at the comet 67P and covers the time 2015-05-16T09:29:25.000 to 2015-05-16T12:08:18.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc2-0781-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC2-0781-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc2-0781-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 2 phase 2015-03-11 to 2015-06-30. It is a Global Gravity measurement at the comet 67P and covers the time 2015-05-16T09:29:25.000 to 2015-05-16T12:08:18.000.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 2 0781 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 2 0781 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ISS/CATS/L2O_D-M7.2-V3-00_05KMLAY",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2018-10-31. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/ISS/CATS/L2O_D-M7.2-V3-00_05KMLAY. https://asdc.larc.nasa.gov/project/CATS-ISS.",
-            "issued": "2018-08-13",
-            "temporal": "2015-03-25T00:00:00Z/2017-10-29T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2018-08-13",
-            "keyword": [
-                "earth science",
-                "aerosols",
-                "atmosphere",
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
-            "identifier": "C1577484498-LARC_ASDC",
             "description": "CATS-ISS_L2O_D-M7.2-V3-00_05kmLay is the Cloud-Aerosol Transport System (CATS) International Space Station (ISS) Level 2 Operational Day Mode 7.2 Version 3-00 5 km Layer data product. This collection spans from March 25, 2015 to October 29, 2017. CATS, which was launched on January 10, 2015, was a lidar remote sensing instrument that provided range-resolved profile measurements of atmospheric aerosols and clouds from the ISS. CATS was intended to operate on-orbit for up to three years. CATS provides vertical profiles at three wavelengths, orbiting between ~230 and ~270 miles above the Earth's surface at a 51-degree inclination with nearly a three-day repeat cycle. For the first time, scientists were able to study diurnal (day-to-night) changes in cloud and aerosol effects from space by observing the same spot on Earth at different times each day. CATS Level 2 Layer data products contain geophysical parameters derived and are from Level 1 data, at 60m vertical and 5km horizontal resolution.",
-            "graphic-preview-description": "CATS Browse and Granule Availability",
-            "title": "CATS-ISS Level 2 Operational Day Mode 7.2 Version 3-00 5 km Layer",
-            "graphic-preview-file": "https://cats.gsfc.nasa.gov/data/browse/",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FISS%2FCATS%2FL2O_D-M7.2-V3-00_05KMLAY",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FISS%2FCATS%2FL2O_D-M7.2-V3-00_05KMLAY",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
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
-                    "downloadURL": "https://asdc.larc.nasa.gov/project/CATS-ISS",
-                    "description": "ASDC Data and Information for CATS",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Data and Information for CATS",
+                    "downloadURL": "https://asdc.larc.nasa.gov/project/CATS-ISS",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
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
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1577484498-LARC_ASDC",
-                    "description": "Earthdata Search for CATS-ISS_L2O_D-M7.2-V3-00_05kmLay_V3-00 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for CATS-ISS_L2O_D-M7.2-V3-00_05kmLay_V3-00 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1577484498-LARC_ASDC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/ISS/CATS/L2O_D-M7.2-V3-00_05KMLAY",
-                    "description": "DOI data set landing page for CATS-ISS_L2O_D-M7.2-V3-00_05kmLay_V3-00",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for CATS-ISS_L2O_D-M7.2-V3-00_05kmLay_V3-00",
+                    "downloadURL": "https://doi.org/10.5067/ISS/CATS/L2O_D-M7.2-V3-00_05KMLAY",
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
-                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/CATS/L2O_D-M7.2-V3-00_05kmLay/contents.html",
-                    "description": "OPeNDAP data access for CATS-ISS_L2O_D-M7.2-V3-00_05kmLay_V3-00",
                     "@type": "dcat:Distribution",
+                    "description": "OPeNDAP data access for CATS-ISS_L2O_D-M7.2-V3-00_05kmLay_V3-00",
+                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/CATS/L2O_D-M7.2-V3-00_05kmLay/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/CATS/L2O_D-M7.2-V3-00_05kmLay/",
-                    "description": "ASDC Direct Data Download for CATS-ISS_L2O_D-M7.2-V3-00_05kmLay_V3-00",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for CATS-ISS_L2O_D-M7.2-V3-00_05kmLay_V3-00",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/CATS/L2O_D-M7.2-V3-00_05kmLay/",
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
+            "identifier": "C1577484498-LARC_ASDC",
+            "issued": "2018-08-13",
+            "keyword": [
+                "earth science",
+                "aerosols",
+                "atmosphere",
+                "clouds"
+            ],
+            "landingPage": "https://doi.org/10.5067/ISS/CATS/L2O_D-M7.2-V3-00_05KMLAY",
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
+            "title": "CATS-ISS Level 2 Operational Day Mode 7.2 Version 3-00 5 km Layer"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-EXT1-1425-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the ROSETTA EXTENSION 1 phase 2016-01-01 to 2016-04-05. It is a Global Gravity measurement at the comet 67P and covers the time 2016-02-15T14:11:35.000 to 2016-02-15T17:00:32.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-ext1-1425-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-EXT1-1425-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-ext1-1425-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the ROSETTA EXTENSION 1 phase 2016-01-01 to 2016-04-05. It is a Global Gravity measurement at the comet 67P and covers the time 2016-02-15T14:11:35.000 to 2016-02-15T17:00:32.000.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     ROSETTA EXTENSION 1 1425 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     ROSETTA EXTENSION 1 1425 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://c3.nasa.gov/dashlink/resources/719/",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2013-05-07",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
-            "keyword": [
-                "ames",
-                "dashlink",
-                "nasa"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Sriram Narasimhan",
                 "hasEmail": "mailto:sriram@email.arc.nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Dashlink"
-            },
-            "identifier": "DASHLINK_719",
             "description": "DXC Framework for Linux and Unix type operating systems",
-            "title": "DXC Framework Linux",
-            "programCode": [
-                "026:029"
-            ],
             "distribution": [
                 {
-                    "mediaType": "application/x-zip-compressed",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/DXC_Framework_Linux.zip",
-                    "description": "DXC Framework Linux",
                     "@type": "dcat:Distribution",
+                    "description": "DXC Framework Linux",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/DXC_Framework_Linux.zip",
+                    "mediaType": "application/x-zip-compressed",
                     "title": "DXC_Framework_Linux.zip"
                 }
             ],
-            "accrualPeriodicity": "irregular"
+            "identifier": "DASHLINK_719",
+            "issued": "2013-05-07",
+            "keyword": [
+                "ames",
+                "dashlink",
+                "nasa"
+            ],
+            "landingPage": "https://c3.nasa.gov/dashlink/resources/719/",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:029"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Dashlink"
+            },
+            "title": "DXC Framework Linux"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/MODIS/MCD18A1.062",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Dongdong Wang. 2024-03-07. MCD18A1.062. MODIS/Terra+Aqua Surface Radiation Daily/3-Hour L3 Global 1km SIN Grid V062. Sioux Falls, South Dakota, USA. Archived by National Aeronautics and Space Administration, U.S. Government, NASA EOSDIS Land Processes Distributed Active Archive Center. https://doi.org/10.5067/MODIS/MCD18A1.062. https://doi.org/10.5067/MODIS/MCD18A1.062. The DOI landing page provides citations in APA and Chicago styles..",
-            "issued": "2021-03-18",
-            "temporal": "2000-02-24T00:00:00Z/2024-06-03T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2021-03-18",
-            "keyword": [
-                "land surface",
-                "ngda",
-                "surface radiative properties",
-                "atmospheric radiation",
-                "earth science",
-                "national geospatial data asset",
-                "atmosphere"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Dongdong Wang",
                 "hasEmail": "mailto:ddwang@umd.edu"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "LP DAAC"
-            },
-            "identifier": "C2486249220-LPCLOUD",
-            "description": "The MCD18A1 Version 6.2 is a Moderate Resolution Imaging Spectroradiometer (MODIS) Terra and Aqua combined Downward Shortwave Radiation (DSR) gridded Level 3 product produced daily at 1 kilometer pixel resolution with estimates of DSR every 3 hours. DSR is incident solar radiation over land surfaces in the shortwave spectrum (300-4,000 nanometers) and is an important variable in land-surface models that address a variety of scientific and application issues. The MCD18 products are based on a prototyping algorithm that uses multi-temporal signatures of MODIS data to derive surface reflectance and then calculate incident DSR using the look-up table (LUT) approach. The LUTs consider different types of loadings of aerosols and clouds at a variety of illumination/viewing geometry. Global DSR products are generated from MODIS and geostationary satellite data. Additional details regarding the methodology used to create the data are available in the Algorithm Theoretical Basis Document (ATBD) (https://lpdaac.usgs.gov/documents/106/MCD18_ATBD.pdf)).\r\n\r\nProvided in the MOD18A1 product are layers for instantaneous DSR array for each individual MODIS overpass and 3-hour DSR array along with a View Zenith Angle layer.\r\n\r\nValidation at stage 1 (https://modis-land.gsfc.nasa.gov/MODLAND_val.html) has been achieved for the MODIS Surface Radiation products. Further details regarding MODIS land product validation for the MCD18 data products are available from the MODIS Land Team Validation site (https://modis-land.gsfc.nasa.gov/ValStatus.php?ProductID=MCD18). \r\n\r\nThe Version 6.2 Level-1B (L1B) products have been improved by undergoing various calibration changes that include: 1) MODIS shortwave infrared bands are included in the retrieval algorithm, which significantly reduces estimation uncertainties in cloud- and snow-covered pixels. \r\n2) An improved climatology of surface reflectance was produced and used in the retrieval algorithm.",
-            "release-place": "Sioux Falls, South Dakota, USA",
-            "series-name": "MCD18A1.062",
-            "graphic-preview-description": "Browse image for Earthdata Search",
             "creator": "Dongdong Wang",
-            "title": "MODIS/Terra+Aqua Surface Radiation Daily/3-Hour L3 Global 1km SIN Grid V062",
-            "graphic-preview-file": "https://cmr.earthdata.nasa.gov/browse-scaler/browse_images/granules/G2800166742-LPCLOUD?h=85&w=85",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The MCD18A1 Version 6.2 is a Moderate Resolution Imaging Spectroradiometer (MODIS) Terra and Aqua combined Downward Shortwave Radiation (DSR) gridded Level 3 product produced daily at 1 kilometer pixel resolution with estimates of DSR every 3 hours. DSR is incident solar radiation over land surfaces in the shortwave spectrum (300-4,000 nanometers) and is an important variable in land-surface models that address a variety of scientific and application issues. The MCD18 products are based on a prototyping algorithm that uses multi-temporal signatures of MODIS data to derive surface reflectance and then calculate incident DSR using the look-up table (LUT) approach. The LUTs consider different types of loadings of aerosols and clouds at a variety of illumination/viewing geometry. Global DSR products are generated from MODIS and geostationary satellite data. Additional details regarding the methodology used to create the data are available in the Algorithm Theoretical Basis Document (ATBD) (https://lpdaac.usgs.gov/documents/106/MCD18_ATBD.pdf)).\r\n\r\nProvided in the MOD18A1 product are layers for instantaneous DSR array for each individual MODIS overpass and 3-hour DSR array along with a View Zenith Angle layer.\r\n\r\nValidation at stage 1 (https://modis-land.gsfc.nasa.gov/MODLAND_val.html) has been achieved for the MODIS Surface Radiation products. Further details regarding MODIS land product validation for the MCD18 data products are available from the MODIS Land Team Validation site (https://modis-land.gsfc.nasa.gov/ValStatus.php?ProductID=MCD18). \r\n\r\nThe Version 6.2 Level-1B (L1B) products have been improved by undergoing various calibration changes that include: 1) MODIS shortwave infrared bands are included in the retrieval algorithm, which significantly reduces estimation uncertainties in cloud- and snow-covered pixels. \r\n2) An improved climatology of surface reflectance was produced and used in the retrieval algorithm.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMODIS%2FMCD18A1.062",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMODIS%2FMCD18A1.062",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://e4ftl01.cr.usgs.gov/MOTA/MCD18A1.062/",
-                    "description": "LP DAAC Data Pool provides direct access to available products via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "LP DAAC Data Pool provides direct access to available products via HTTPS.",
+                    "downloadURL": "https://e4ftl01.cr.usgs.gov/MOTA/MCD18A1.062/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=C2486249220-LPCLOUD",
-                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=C2486249220-LPCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/MODIS/MCD18A1.062",
-                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
+                    "downloadURL": "https://doi.org/10.5067/MODIS/MCD18A1.062",
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
-                    "downloadURL": "https://lpdaac.usgs.gov/documents/1658/MCD18_User_Guide_V62.pdf",
-                    "description": "The technical information in the User's Guide enables users to interpret and use the data products.",
                     "@type": "dcat:Distribution",
+                    "description": "The technical information in the User's Guide enables users to interpret and use the data products.",
+                    "downloadURL": "https://lpdaac.usgs.gov/documents/1658/MCD18_User_Guide_V62.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://lpdaac.usgs.gov/documents/106/MCD18_ATBD.pdf",
-                    "description": "The ATBD provides physical theory and mathematical procedures for the calculations used to produce the data products.",
                     "@type": "dcat:Distribution",
+                    "description": "The ATBD provides physical theory and mathematical procedures for the calculations used to produce the data products.",
+                    "downloadURL": "https://lpdaac.usgs.gov/documents/106/MCD18_ATBD.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's algorithm theoretical basis document"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/filespec/MODIS/61/MCD18A1",
-                    "description": "The File Specification provides a description of the product file including Scientific Data Sets and their attributes.",
                     "@type": "dcat:Distribution",
+                    "description": "The File Specification provides a description of the product file including Scientific Data Sets and their attributes.",
+                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/filespec/MODIS/61/MCD18A1",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://modis-land.gsfc.nasa.gov/MODLAND_val.html",
-                    "description": "Validation at stage 1 has been achieved for the MODIS Surface Radiation products.",
                     "@type": "dcat:Distribution",
+                    "description": "Validation at stage 1 has been achieved for the MODIS Surface Radiation products.",
+                    "downloadURL": "https://modis-land.gsfc.nasa.gov/MODLAND_val.html",
+                    "mediaType": "text/html",
                     "title": "View this dataset's science data product validation documentation"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://modis-land.gsfc.nasa.gov/ValStatus.php?ProductID=MCD18",
-                    "description": "Further details regarding MODIS land product validation for the MCD18 data products are available from the MODIS Land Team Validation site.",
                     "@type": "dcat:Distribution",
+                    "description": "Further details regarding MODIS land product validation for the MCD18 data products are available from the MODIS Land Team Validation site.",
+                    "downloadURL": "https://modis-land.gsfc.nasa.gov/ValStatus.php?ProductID=MCD18",
+                    "mediaType": "text/html",
                     "title": "View this dataset's science data product validation documentation"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://opendap.cr.usgs.gov/opendap/hyrax/DP137/MOTA/MCD18A1.062/contents.html",
-                    "description": "Access data via Open-source Project for a Network Data Access Protocol",
                     "@type": "dcat:Distribution",
+                    "description": "Access data via Open-source Project for a Network Data Access Protocol",
+                    "downloadURL": "https://opendap.cr.usgs.gov/opendap/hyrax/DP137/MOTA/MCD18A1.062/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/browse-scaler/browse_images/granules/G2800166742-LPCLOUD?h=85&w=85",
-                    "description": "Browse image for Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse image for Earthdata Search",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/browse-scaler/browse_images/granules/G2800166742-LPCLOUD?h=85&w=85",
+                    "mediaType": "text/html",
                     "title": "Get a related visualization"
                 }
             ],
+            "graphic-preview-description": "Browse image for Earthdata Search",
+            "graphic-preview-file": "https://cmr.earthdata.nasa.gov/browse-scaler/browse_images/granules/G2800166742-LPCLOUD?h=85&w=85",
+            "identifier": "C2486249220-LPCLOUD",
+            "issued": "2021-03-18",
+            "keyword": [
+                "land surface",
+                "ngda",
+                "surface radiative properties",
+                "atmospheric radiation",
+                "earth science",
+                "national geospatial data asset",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.5067/MODIS/MCD18A1.062",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2021-03-18",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "LP DAAC"
+            },
+            "release-place": "Sioux Falls, South Dakota, USA",
+            "series-name": "MCD18A1.062",
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
+            "title": "MODIS/Terra+Aqua Surface Radiation Daily/3-Hour L3 Global 1km SIN Grid V062"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://planetarynames.wr.usgs.gov/Page/moon1to10mShadedRelief",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Michael Kelly",
+                "hasEmail": "mailto:Michael.S.Kelley@nasa.gov"
+            },
+            "description": "These lunar maps display the four different areas of the moon with color-coded topography in low and high resolution approved by the International Astronomical Union (IAU).",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://planetarynames.wr.usgs.gov/images/moon_np.jpg",
+                    "mediaType": "image/jpg"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://planetarynames.wr.usgs.gov/images/moon_np.pdf",
+                    "mediaType": "application/pdf"
+                }
+            ],
+            "identifier": "OCIO-Fitara-160",
             "issued": "2013-02-13",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
             "keyword": [
                 "imagery",
                 "north pole",
@@ -691961,87 +691978,80 @@
                 "moon",
                 "working group for planetary system nomenclature"
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
-            "identifier": "OCIO-Fitara-160",
-            "description": "These lunar maps display the four different areas of the moon with color-coded topography in low and high resolution approved by the International Astronomical Union (IAU).",
-            "title": "Gazetteer of Planetary Nomenclature: Moon: 1:10 million-scale Shaded Relief and Color-coded Topography: North Pole",
+            "landingPage": "http://planetarynames.wr.usgs.gov/Page/moon1to10mShadedRelief",
+            "modified": "2020-01-29",
             "programCode": [
                 "026:007"
             ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://planetarynames.wr.usgs.gov/images/moon_np.jpg",
-                    "mediaType": "image/jpg"
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "International Astronomical Union (IAU) Working Group for Planetary System Nomenclature (WGPSN)"
             },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://planetarynames.wr.usgs.gov/images/moon_np.pdf",
-                    "mediaType": "application/pdf"
-                }
-            ],
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Space Science"
-            ]
+            ],
+            "title": "Gazetteer of Planetary Nomenclature: Moon: 1:10 million-scale Shaded Relief and Color-coded Topography: North Pole"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-J-SWAP-2-JUPITER-V1.0",
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
+            "description": "This data set contains Raw data taken by the New Horizons Solar Wind Around Pluto instrument during the Jupiter encounter mission phase.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-j-swap-2-jupiter-v1.0_e9ve-j2nr",
+            "issued": "2018-06-26",
+            "keyword": [
+                "solar wind",
+                "new horizons"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-J-SWAP-2-JUPITER-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-j-swap-2-jupiter-v1.0_e9ve-j2nr",
-            "description": "This data set contains Raw data taken by the New Horizons Solar Wind Around Pluto instrument during the Jupiter encounter mission phase.",
-            "title": "NEW HORIZONS SWAP JUPITER ENCOUNTER V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "NEW HORIZONS SWAP JUPITER ENCOUNTER V1.0"
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
+                    "downloadURL": "http://aeronet.gsfc.nasa.gov/data_push/INV/INV_PFN_Level15_All_Points_V2.tar.gz",
+                    "mediaType": "application/x-tar"
+                }
             ],
+            "identifier": "NASA-0000005",
+            "issued": "2018-06-25",
             "keyword": [
                 "inversions",
                 "earth science",
@@ -692051,46 +692061,47 @@
                 "satellite",
                 "precipitable water"
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
-            "identifier": "NASA-0000005",
-            "description": "AERONET inversion code provides aerosoloptical properties in the total atmospheric column derived from the direct and diffuse radiation measured byAERONETCimel sun/sky-radiometers. AERONET inversion developmentand researchactivitiesare described in the papers by Dubovik and King, [2000], Dubovik et al. [2000], Dubovik et al. [2002a], Dubovik et al. [2002b], Dubovik et al., [2006a], Sinyuk et al. [2006]. The Version 2(V2)inversion (or retrieval)products are summarized below. These products are available through the internal analysis system&#x0022;demonstrat&#x0022; and the AERONET website. Adetailed description of V2 AERONET retrieval will be provided in the paper by Dubovik et al., [2006b].",
-            "title": "Level 1.5 Almucantar Inversion Products Phase Functions",
-            "describedByType": "application/pdf",
-            "programCode": [
-                "026:001"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://aeronet.gsfc.nasa.gov/data_push/INV/INV_PFN_Level15_All_Points_V2.tar.gz",
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
+            "description": "The Fermi Gamma-ray Space Telescope (Fermi) Large Area Telescope (LAT) is a successor to EGRET, with greatly improved sensitivity, resolution, and energy range. This web page presents the first full catalog of LAT sources, based on the first eleven months of survey data. For a full explanation about the catalog and its construction see the LAT 1-year Catalog Paper.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://dx.doi.org/10.1088/0067-0049/188/2/405",
+                    "mediaType": "text/html"
+                }
+            ],
+            "identifier": "NASA-0000221__2",
             "issued": "2018-06-25",
-            "temporal": "2008-08-01/2009-07-01",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
             "keyword": [
                 "fermi",
                 "bursts",
@@ -692108,210 +692119,181 @@
                 "gamma-ray",
                 "gamma"
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
-            "identifier": "NASA-0000221__2",
-            "description": "The Fermi Gamma-ray Space Telescope (Fermi) Large Area Telescope (LAT) is a successor to EGRET, with greatly improved sensitivity, resolution, and energy range. This web page presents the first full catalog of LAT sources, based on the first eleven months of survey data. For a full explanation about the catalog and its construction see the LAT 1-year Catalog Paper.",
-            "title": "LAT 1-year Point Source Catalog",
-            "programCode": [
-                "026:014"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://dx.doi.org/10.1088/0067-0049/188/2/405",
-                    "mediaType": "text/html"
-                }
-            ],
-            "accrualPeriodicity": "irregular",
+            "temporal": "2008-08-01/2009-07-01",
             "theme": [
                 "Space Science"
-            ]
+            ],
+            "title": "LAT 1-year Point Source Catalog"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/MODIS/MYD09GQ.061",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Eric Vermote, Robert Wolfe. 2021-02-01. MODIS/Aqua Surface Reflectance Daily L2G Global 250m SIN Grid V061. Sioux Falls, South Dakota, USA. Archived by National Aeronautics and Space Administration, U.S. Government, NASA EOSDIS Land Processes Distributed Active Archive Center. https://doi.org/10.5067/MODIS/MYD09GQ.061. https://doi.org/10.5067/MODIS/MYD09GQ.061. The DOI landing page provides citations in APA and Chicago styles..",
-            "issued": "2021-02-01",
-            "temporal": "2002-07-04T00:00:00Z/2024-06-03T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2021-02-01",
-            "keyword": [
-                "land surface",
-                "national geospatial data asset",
-                "ngda",
-                "surface radiative properties",
-                "earth science"
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
-            "identifier": "C2343109950-LPCLOUD",
-            "description": "The MYD09GQ Version 6.1 product provides an estimate of the surface spectral reflectance of Aqua Moderate Resolution Imaging Spectroradiometer (MODIS) 250 meter (m) bands 1 and 2, corrected for atmospheric conditions such as gasses, aerosols, and Rayleigh scattering. Along with the 250 m bands are the Quality Assurance (QA) layer and five observation layers. This product is intended to be used in conjunction with the quality and viewing geometry information of the 500 m product (MYD09GA). \r\n\r\nValidation at stage 3 (https://modis-land.gsfc.nasa.gov/MODLAND_val.html) has been achieved for the MODIS Surface Reflectance products. Further details regarding MODIS land product validation for the MYD09 data product is available from the MODIS Land Team Validation site (https://modis-land.gsfc.nasa.gov/ValStatus.php?ProductID=MOD09).\r\n\r\nImprovements/Changes from Previous Versions\r\n\r\n* The Version 6.1 Level-1B (L1B) products have been improved by undergoing various calibration changes that include: changes to the response-versus-scan angle (RVS) approach that affects reflectance bands for Aqua and Terra MODIS, corrections to adjust for the optical crosstalk in Terra MODIS infrared (IR) bands, and corrections to the Terra MODIS forward look-up table (LUT) update for the period 2012 - 2017.\r\n* A polarization correction has been applied to the L1B Reflective Solar Bands (RSB).",
-            "release-place": "Sioux Falls, South Dakota, USA",
-            "graphic-preview-description": "Browse image for Earthdata Search.",
             "creator": "Eric Vermote, Robert Wolfe",
-            "title": "MODIS/Aqua Surface Reflectance Daily L2G Global 250m SIN Grid V061",
-            "graphic-preview-file": "https://cmr.earthdata.nasa.gov/browse-scaler/browse_images/granules/G2359475509-LPCLOUD?h=500&w=500",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The MYD09GQ Version 6.1 product provides an estimate of the surface spectral reflectance of Aqua Moderate Resolution Imaging Spectroradiometer (MODIS) 250 meter (m) bands 1 and 2, corrected for atmospheric conditions such as gasses, aerosols, and Rayleigh scattering. Along with the 250 m bands are the Quality Assurance (QA) layer and five observation layers. This product is intended to be used in conjunction with the quality and viewing geometry information of the 500 m product (MYD09GA). \r\n\r\nValidation at stage 3 (https://modis-land.gsfc.nasa.gov/MODLAND_val.html) has been achieved for the MODIS Surface Reflectance products. Further details regarding MODIS land product validation for the MYD09 data product is available from the MODIS Land Team Validation site (https://modis-land.gsfc.nasa.gov/ValStatus.php?ProductID=MOD09).\r\n\r\nImprovements/Changes from Previous Versions\r\n\r\n* The Version 6.1 Level-1B (L1B) products have been improved by undergoing various calibration changes that include: changes to the response-versus-scan angle (RVS) approach that affects reflectance bands for Aqua and Terra MODIS, corrections to adjust for the optical crosstalk in Terra MODIS infrared (IR) bands, and corrections to the Terra MODIS forward look-up table (LUT) update for the period 2012 - 2017.\r\n* A polarization correction has been applied to the L1B Reflective Solar Bands (RSB).",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMODIS%2FMYD09GQ.061",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMODIS%2FMYD09GQ.061",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/MODIS/MYD09GQ.061",
-                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
+                    "downloadURL": "https://doi.org/10.5067/MODIS/MYD09GQ.061",
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
-                    "downloadURL": "https://e4ftl01.cr.usgs.gov/MOLA/MYD09GQ.061/",
-                    "description": "LP DAAC Data Pool provides direct access to available products via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "LP DAAC Data Pool provides direct access to available products via HTTPS.",
+                    "downloadURL": "https://e4ftl01.cr.usgs.gov/MOLA/MYD09GQ.061/",
+                    "mediaType": "application/x-hdf",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "application/x-hdf",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2343109950-LPCLOUD",
-                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2343109950-LPCLOUD",
+                    "mediaType": "application/x-hdf",
                     "title": "Download this dataset through Earthdata Search"
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
-                    "downloadURL": "https://opendap.cr.usgs.gov/opendap/hyrax/MYD09GQ.061/contents.html",
-                    "description": "Access data via Open-source Project for a Network Data Access Protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access data via Open-source Project for a Network Data Access Protocol.",
+                    "downloadURL": "https://opendap.cr.usgs.gov/opendap/hyrax/MYD09GQ.061/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://lpdaac.usgs.gov/documents/305/MOD09_ATBD.pdf",
-                    "description": "The Algorithm Theoretical Basis Document (ATBD) describes the physical and mathematical algorithms for the product.",
                     "@type": "dcat:Distribution",
+                    "description": "The Algorithm Theoretical Basis Document (ATBD) describes the physical and mathematical algorithms for the product.",
+                    "downloadURL": "https://lpdaac.usgs.gov/documents/305/MOD09_ATBD.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's algorithm theoretical basis document"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://lpdaac.usgs.gov/documents/925/MOD09_User_Guide_V61.pdf",
-                    "description": "The technical information in the User's Guide enables users to interpret and use the data products.",
                     "@type": "dcat:Distribution",
+                    "description": "The technical information in the User's Guide enables users to interpret and use the data products.",
+                    "downloadURL": "https://lpdaac.usgs.gov/documents/925/MOD09_User_Guide_V61.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/filespec/MODIS/61/MYD09GQ",
-                    "description": "The File Specification provides a description of the product file including Scientific Data Sets and their attributes.",
                     "@type": "dcat:Distribution",
+                    "description": "The File Specification provides a description of the product file including Scientific Data Sets and their attributes.",
+                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/filespec/MODIS/61/MYD09GQ",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://modis-land.gsfc.nasa.gov/ValStatus.php?ProductID=MYD09",
-                    "description": "Further details regarding MODIS land product validation for the MYD09 data products are available from the MODIS Land Team Validation site.",
                     "@type": "dcat:Distribution",
+                    "description": "Further details regarding MODIS land product validation for the MYD09 data products are available from the MODIS Land Team Validation site.",
+                    "downloadURL": "https://modis-land.gsfc.nasa.gov/ValStatus.php?ProductID=MYD09",
+                    "mediaType": "text/html",
                     "title": "View this dataset's science data product validation documentation"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://modis-land.gsfc.nasa.gov/MODLAND_val.html",
-                    "description": "Validation at stage 3 has been achieved for the MODIS Surface Reflectance products.",
                     "@type": "dcat:Distribution",
+                    "description": "Validation at stage 3 has been achieved for the MODIS Surface Reflectance products.",
+                    "downloadURL": "https://modis-land.gsfc.nasa.gov/MODLAND_val.html",
+                    "mediaType": "text/html",
                     "title": "View this dataset's science data product validation documentation"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://landweb.modaps.eosdis.nasa.gov/cgi-bin/QA_WWW/qaFlagPage.cgi?sat=aqua&ver=C6",
-                    "description": "Quality Assessment provides information regarding the usability and usefulness of the data product.",
                     "@type": "dcat:Distribution",
+                    "description": "Quality Assessment provides information regarding the usability and usefulness of the data product.",
+                    "downloadURL": "https://landweb.modaps.eosdis.nasa.gov/cgi-bin/QA_WWW/qaFlagPage.cgi?sat=aqua&ver=C6",
+                    "mediaType": "text/html",
                     "title": "View this dataset's product quality assessment"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/browse-scaler/browse_images/granules/G2359475509-LPCLOUD?h=500&w=500",
-                    "description": "Browse image for Earthdata Search.",
                     "@type": "dcat:Distribution",
+                    "description": "Browse image for Earthdata Search.",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/browse-scaler/browse_images/granules/G2359475509-LPCLOUD?h=500&w=500",
+                    "mediaType": "text/html",
                     "title": "Get a related visualization"
                 }
             ],
+            "graphic-preview-description": "Browse image for Earthdata Search.",
+            "graphic-preview-file": "https://cmr.earthdata.nasa.gov/browse-scaler/browse_images/granules/G2359475509-LPCLOUD?h=500&w=500",
+            "identifier": "C2343109950-LPCLOUD",
+            "issued": "2021-02-01",
+            "keyword": [
+                "land surface",
+                "national geospatial data asset",
+                "ngda",
+                "surface radiative properties",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/MODIS/MYD09GQ.061",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2021-02-01",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "LP DAAC"
+            },
+            "release-place": "Sioux Falls, South Dakota, USA",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2002-07-04T00:00:00Z/2024-06-03T00:00:00Z",
             "theme": [
                 "Aqua",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "MODIS/Aqua Surface Reflectance Daily L2G Global 250m SIN Grid V061"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.nasa.gov/d/e9yn-9xrg",
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
-            "identifier": "NASA-0000038__19",
+            "describedBy": "http://planetarynames.wr.usgs.gov/Page/Website",
             "description": "Planetary nomenclature, like terrestrial nomenclature, is used to uniquely identify a feature on the surface of a planet or satellite so that the feature can be easily located, described, and discussed. This gazetteer contains detailed information about all names of topographic and albedo features on planets and satellites (and some planetary ring and ring-gap systems) that the International Astronomical Union (IAU) has named and approved from its founding in 1919 through the present time.",
-            "title": "Gazetteer of Planetary Nomenclature",
-            "programCode": [
-                "026:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -692319,752 +692301,781 @@
                     "mediaType": "application/zip"
                 }
             ],
-            "describedBy": "http://planetarynames.wr.usgs.gov/Page/Website",
-            "accrualPeriodicity": "irregular"
+            "identifier": "NASA-0000038__19",
+            "issued": "2018-06-25",
+            "keyword": [
+                "nen",
+                "wise",
+                "space science",
+                "geography"
+            ],
+            "landingPage": "https://data.nasa.gov/d/e9yn-9xrg",
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
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-5-DDR-FAMILY-V2.0",
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
+            "description": "This data set contains the Zappala et al. (1995) [ZAPPALAETAL1995] asteroid dynamical families classifications, based on the hierarchical clustering method applied to the proper elements of Milani & Knezevic (1994) [MILANI&KNEZEVIC1994]. It includes 12,487 numbered and unnumbered asteroids.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-5-ddr-family-v2.0_e9zm-96bj",
+            "issued": "2018-06-26",
+            "keyword": [
+                "support archives",
+                "asteroid"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-5-DDR-FAMILY-V2.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-5-ddr-family-v2.0_e9zm-96bj",
-            "description": "This data set contains the Zappala et al. (1995) [ZAPPALAETAL1995] asteroid dynamical families classifications, based on the hierarchical clustering method applied to the proper elements of Milani & Knezevic (1994) [MILANI&KNEZEVIC1994]. It includes 12,487 numbered and unnumbered asteroids.",
-            "title": "ASTEROID DYNAMICAL FAMILIES V2.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "ASTEROID DYNAMICAL FAMILIES V2.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/MEASURES/DMSP-F16/SSMIS/DATA304",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Wentz, Frank J, Kyle Hilburn and Deborah K Smith.2012. RSS SSMIS OCEAN PRODUCT GRIDS MONTHLY AVERAGE FROM DMSP F16 NETCDF [indicate subset used]. Dataset available online from the NASA Global Hydrometeorology Resource Center DAAC, Huntsville, Alabama, U.S.A. DOI: http://dx.doi.org/10.5067/MEASURES/DMSP-F16/SSMIS/DATA304",
-            "issued": "2012-10-01",
-            "temporal": "2003-10-01T00:00:00Z/2022-05-03T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-04-28",
-            "keyword": [
-                "atmospheric water vapor",
-                "atmospheric winds",
-                "clouds",
-                "earth science",
-                "oceans",
-                "ocean winds",
-                "precipitation",
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
-            "identifier": "C1996546916-GHRC_DAAC",
             "description": "The RSS SSMIS Ocean Product Grids Monthly Average from DMSP F16 netCDF dataset is part of the collection of Special Sensor Microwave/Imager (SSM/I) and Special Sensor Microwave Imager Sounder (SSMIS) data products produced as part of NASA's MEaSUREs Program. Remote Sensing Systems generates SSM/I and SSMIS binary data products using a unified, physically based algorithm to simultaneously retrieve ocean wind speed, water vapor, cloud water, and rain rate. The SSMIS data have been carefully intercalibrated to the brightness temperature level of the previous SSM/I and therefore extend this important time series of ocean winds, vapor, cloud and rain values. This algorithm is a product of 20 years of refinements, improvements, and verifications. The Global Hydrology Resource Center has reformatted the binary data into a netCDF data product for each temporal group for each satellite. The netCDF SSMI/SSMIS collection will be available for F16 for a monthly average.",
-            "graphic-preview-description": "N/A",
-            "title": "RSS SSMIS OCEAN PRODUCT GRIDS MONTHLY AVERAGE FROM DMSP F16 NETCDF V7",
-            "graphic-preview-file": "https://ghrc.nsstc.nasa.gov/pub/ssmis/f16/monthly/browse/",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMEASURES%2FDMSP-F16%2FSSMIS%2FDATA304",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMEASURES%2FDMSP-F16%2FSSMIS%2FDATA304",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=rssmif16m",
-                    "description": "Files may be downloaded directly to your workstation from this link",
                     "@type": "dcat:Distribution",
+                    "description": "Files may be downloaded directly to your workstation from this link",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=rssmif16m",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/ssmis/f16/monthly/browse/2010/f16_ssmis_201009v7_CW.png",
-                    "description": "Sample browse image",
                     "@type": "dcat:Distribution",
+                    "description": "Sample browse image",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/ssmis/f16/monthly/browse/2010/f16_ssmis_201009v7_CW.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/ssmis/f16/monthly/browse/2010/f16_ssmis_201009v7_WS.png",
-                    "description": "Sample browse image",
                     "@type": "dcat:Distribution",
+                    "description": "Sample browse image",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/ssmis/f16/monthly/browse/2010/f16_ssmis_201009v7_WS.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/ssmis/f16/monthly/browse/2010/f16_ssmis_201009v7_WV.png",
-                    "description": "Sample browse image",
                     "@type": "dcat:Distribution",
+                    "description": "Sample browse image",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/ssmis/f16/monthly/browse/2010/f16_ssmis_201009v7_WV.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/ssmis/f16/monthly/browse/2010/f16_ssmis_201009v7_RR.png",
-                    "description": "Sample browse image",
                     "@type": "dcat:Distribution",
+                    "description": "Sample browse image",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/ssmis/f16/monthly/browse/2010/f16_ssmis_201009v7_RR.png",
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
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/doc/ssmi_netcdf/ssmi.pdf",
-                    "description": "A Well Calibrated Ocean Algorithm for SSM/I",
                     "@type": "dcat:Distribution",
+                    "description": "A Well Calibrated Ocean Algorithm for SSM/I",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/doc/ssmi_netcdf/ssmi.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View the primary investigator's documentation for this dataset"
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
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/opendap/ssmis/f16/monthly/",
-                    "description": "OPeNDAP server dataset access",
                     "@type": "dcat:Distribution",
+                    "description": "OPeNDAP server dataset access",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/opendap/ssmis/f16/monthly/",
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
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/doc/ssmi_netcdf/2012_Wentz_011012_Version-7_SSMI_Calibration.pdf",
-                    "description": "SSM/I Version-7 Calibration Report",
                     "@type": "dcat:Distribution",
+                    "description": "SSM/I Version-7 Calibration Report",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/doc/ssmi_netcdf/2012_Wentz_011012_Version-7_SSMI_Calibration.pdf",
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
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/ssmis/f16/monthly/browse/",
-                    "description": "N/A",
                     "@type": "dcat:Distribution",
+                    "description": "N/A",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/ssmis/f16/monthly/browse/",
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
+            "graphic-preview-file": "https://ghrc.nsstc.nasa.gov/pub/ssmis/f16/monthly/browse/",
+            "identifier": "C1996546916-GHRC_DAAC",
+            "issued": "2012-10-01",
+            "keyword": [
+                "atmospheric water vapor",
+                "atmospheric winds",
+                "clouds",
+                "earth science",
+                "oceans",
+                "ocean winds",
+                "precipitation",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.5067/MEASURES/DMSP-F16/SSMIS/DATA304",
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
+            "temporal": "2003-10-01T00:00:00Z/2022-05-03T00:00:00Z",
             "theme": [
                 "DISCOVER",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "RSS SSMIS OCEAN PRODUCT GRIDS MONTHLY AVERAGE FROM DMSP F16 NETCDF V7"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ASDC/SUBORBITAL/KORUSAQ_Merge_Data_1",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2022-01-27. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/ASDC/SUBORBITAL/KORUSAQ_Merge_Data_1.",
-            "issued": "2021-05-14",
-            "temporal": "2016-04-24T00:00:00Z/2016-06-21T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-04-18",
-            "keyword": [
-                "atmospheric chemistry",
-                "aerosols",
-                "earth science",
-                "air quality",
-                "atmospheric winds",
-                "atmospheric water vapor",
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
-            "identifier": "C2211408197-LARC_ASDC",
             "description": "KORUSAQ_Merge_Data are pre-generated merge data files combining various products collected during the KORUS-AQ field campaign. This collection features pre-generated merge files for the DC-8 aircraft. Data collection for this product is complete.\r\n\r\nThe KORUS-AQ field study was conducted in South Korea during May-June, 2016. The study was jointly sponsored by NASA and Korea\u2019s National Institute of Environmental Research (NIER). The primary objectives were to investigate the factors controlling air quality in Korea (e.g., local emissions, chemical processes, and transboundary transport) and to assess future air quality observing strategies incorporating geostationary satellite observations. To achieve these science objectives, KORUS-AQ adopted a highly coordinated sampling strategy involved surface and airborne measurements including both in-situ and remote sensing instruments.\r\n\r\nSurface observations provided details on ground-level air quality conditions while airborne sampling provided an assessment of conditions aloft relevant to satellite observations and necessary to understand the role of emissions, chemistry, and dynamics in determining air quality outcomes. The sampling region covers the South Korean peninsula and surrounding waters with a primary focus on the Seoul Metropolitan Area. Airborne sampling was primarily conducted from near surface to about 8 km with extensive profiling to characterize the vertical distribution of pollutants and their precursors. The airborne observational data were collected from three aircraft platforms: the NASA DC-8, NASA B-200, and Hanseo King Air. Surface measurements were conducted from 16 ground sites and 2 ships: R/V Onnuri and R/V Jang Mok.\r\n\r\nThe major data products collected from both the ground and air include in-situ measurements of trace gases (e.g., ozone, reactive nitrogen species, carbon monoxide and dioxide, methane, non-methane and oxygenated hydrocarbon species), aerosols (e.g., microphysical and optical properties and chemical composition), active remote sensing of ozone and aerosols, and passive remote sensing of NO2, CH2O, and O3 column densities. These data products support research focused on examining the impact of photochemistry and transport on ozone and aerosols, evaluating emissions inventories, and assessing the potential use of satellite observations in air quality studies.",
-            "title": "KORUS-AQ Aircraft Merge Data Files",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC%2FSUBORBITAL%2FKORUSAQ_Merge_Data_1",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC%2FSUBORBITAL%2FKORUSAQ_Merge_Data_1",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://espo.nasa.gov/korus-aq",
-                    "description": "KORUS-AQ Earth Science Project Office (ESPO) home page",
                     "@type": "dcat:Distribution",
+                    "description": "KORUS-AQ Earth Science Project Office (ESPO) home page",
+                    "downloadURL": "https://espo.nasa.gov/korus-aq",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.nier.go.kr/NIER/eng/index.do",
-                    "description": "National Institute of Environmental Research home page",
                     "@type": "dcat:Distribution",
+                    "description": "National Institute of Environmental Research home page",
+                    "downloadURL": "https://www.nier.go.kr/NIER/eng/index.do",
+                    "mediaType": "text/html",
                     "title": "The dataset's home page"
                 },
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.nasa.gov/feature/langley/the-future-of-monitoring-air-quality-from-space",
-                    "description": "Article, The Future of Monitoring Air Quality from Space",
+                {
                     "@type": "dcat:Distribution",
+                    "description": "Article, The Future of Monitoring Air Quality from Space",
+                    "downloadURL": "https://www.nasa.gov/feature/langley/the-future-of-monitoring-air-quality-from-space",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.nasa.gov/feature/airborne-expedition-tackles-global-air-quality-problem",
-                    "description": "Article, Airborne Expedition Tackles Global Air Quality Problem",
                     "@type": "dcat:Distribution",
+                    "description": "Article, Airborne Expedition Tackles Global Air Quality Problem",
+                    "downloadURL": "https://www.nasa.gov/feature/airborne-expedition-tackles-global-air-quality-problem",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://www-air.larc.nasa.gov/missions/korus-aq/docs/White_paper_NASA_KORUS-AQ.pdf",
-                    "description": "KORUS-AQ White Paper Outlining NASA\u2019s contribution",
                     "@type": "dcat:Distribution",
+                    "description": "KORUS-AQ White Paper Outlining NASA\u2019s contribution",
+                    "downloadURL": "https://www-air.larc.nasa.gov/missions/korus-aq/docs/White_paper_NASA_KORUS-AQ.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://espo.nasa.gov/sites/default/files/documents/MAPS-Seoul_White%20Paper_26%20Feb%202015_Final.pdf",
-                    "description": "KORUS-AQ White Paper outlining Korea\u2019s contribution (the Megacity Air Pollution Study [MAPS] - Seoul)",
                     "@type": "dcat:Distribution",
+                    "description": "KORUS-AQ White Paper outlining Korea\u2019s contribution (the Megacity Air Pollution Study [MAPS] - Seoul)",
+                    "downloadURL": "https://espo.nasa.gov/sites/default/files/documents/MAPS-Seoul_White%20Paper_26%20Feb%202015_Final.pdf",
+                    "mediaType": "application/pdf",
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
-                    "downloadURL": "https://www.nasa.gov/content/earth-expeditions-korus-aq",
-                    "description": "Earth Expeditions Tagged Posts",
                     "@type": "dcat:Distribution",
+                    "description": "Earth Expeditions Tagged Posts",
+                    "downloadURL": "https://www.nasa.gov/content/earth-expeditions-korus-aq",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://espo.nasa.gov/sites/default/files/documents/KORUS-AQ-ENG.pdf",
-                    "description": "KORUS-AQ Rapid Science Synthesis Report",
                     "@type": "dcat:Distribution",
+                    "description": "KORUS-AQ Rapid Science Synthesis Report",
+                    "downloadURL": "https://espo.nasa.gov/sites/default/files/documents/KORUS-AQ-ENG.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://edition.cnn.com/2016/06/02/asia/nasa-air-pollution-south-korea-photos/",
-                    "description": "KORUS-AQ CNN Photo Release",
                     "@type": "dcat:Distribution",
+                    "description": "KORUS-AQ CNN Photo Release",
+                    "downloadURL": "https://edition.cnn.com/2016/06/02/asia/nasa-air-pollution-south-korea-photos/",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.cnn.com/2016/06/02/asia/nasa-south-korea-dc-8-pollution/index.html",
-                    "description": "KORUS-AQ CNN Article",
                     "@type": "dcat:Distribution",
+                    "description": "KORUS-AQ CNN Article",
+                    "downloadURL": "https://www.cnn.com/2016/06/02/asia/nasa-south-korea-dc-8-pollution/index.html",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/ASDC/SUBORBITAL/KORUSAQ_Merge_Data_1",
-                    "description": "DOI Data Set Landing Page for KORUSAQ_Merge_Data_1",
                     "@type": "dcat:Distribution",
+                    "description": "DOI Data Set Landing Page for KORUSAQ_Merge_Data_1",
+                    "downloadURL": "https://doi.org/10.5067/ASDC/SUBORBITAL/KORUSAQ_Merge_Data_1",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2211408197-LARC_ASDC",
-                    "description": "Earthdata Search Client for KORUSAQ_Merge_Data_1",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search Client for KORUSAQ_Merge_Data_1",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2211408197-LARC_ASDC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/KORUS-AQ/Merge_Data_1/",
-                    "description": "ASDC Direct Data Download for KORUSAQ_Merge_Data_1",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for KORUSAQ_Merge_Data_1",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/KORUS-AQ/Merge_Data_1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 }
             ],
+            "identifier": "C2211408197-LARC_ASDC",
+            "issued": "2021-05-14",
+            "keyword": [
+                "atmospheric chemistry",
+                "aerosols",
+                "earth science",
+                "air quality",
+                "atmospheric winds",
+                "atmospheric water vapor",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.5067/ASDC/SUBORBITAL/KORUSAQ_Merge_Data_1",
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
             "spatial": "<?xml version=\"1.0\" encoding=\"UTF-8\"?><gml:Polygon xmlns:gml=\"http://www.opengis.net/gml/3.2\" srsName=\"EPSG:9825\"><gml:outerBoundaryIs><gml:LinearRing><gml:posList>25.0 -180.0 25.0 180.0 67.0 180.0 67.0 -180.0 25.0 -180.0</gml:posList></gml:LinearRing></gml:outerBoundaryIs><gml:innerBoundaryIs></gml:innerBoundaryIs></gml:Polygon>",
+            "temporal": "2016-04-24T00:00:00Z/2016-06-21T23:59:59.999Z",
             "theme": [
                 "KORUS-AQ",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "KORUS-AQ Aircraft Merge Data Files"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/B0L38R609B0R",
             "citation": "David Mocko, NASA/GSFC/HSL. 2014-03-01. NLDAS_VIC0125_MC. Version 002. NLDAS VIC Land Surface Model L4 Monthly Climatology 0.125 x 0.125 degree V002. Greenbelt, Maryland, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/B0L38R609B0R. https://disc.gsfc.nasa.gov/datacollection/NLDAS_VIC0125_MC_002.html. Digital Science Data.",
-            "issued": "2014-03-01",
-            "temporal": "1980-01-01T00:00:00Z/2009-12-31T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2014-03-01",
-            "references": [
-                "https://doi.org/10.1029/2011JD016048",
-                "https://doi.org/10.1029/2011JD016051",
-                "https://doi.org/10.1175/1520-0493(1997)125<2896:AOTLSA>2.0.CO;2",
-                "https://doi.org/10.1023/A:1000531001463",
-                "https://doi.org/10.1029/2002JD003296",
-                "https://doi.org/10.1029/1999JD900232",
-                "https://doi.org/10.1175/2009JHM1174.1",
-                "https://doi.org/10.1002/hyp.9214"
-            ],
-            "keyword": [
-                "soils",
-                "atmospheric water vapor",
-                "biosphere",
-                "terrestrial hydrosphere",
-                "atmospheric temperature",
-                "atmospheric radiation",
-                "earth science",
-                "vegetation",
-                "land surface",
-                "atmosphere",
-                "snow/ice",
-                "precipitation",
-                "surface radiative properties",
-                "surface thermal properties",
-                "surface water"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "DAVID SILBERSTEIN",
                 "hasEmail": "mailto:david.s.silberstein@nasa.gov"
             },
+            "creator": "David Mocko, NASA/GSFC/HSL",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C1233767676-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "Abstract: This data set contains a series of land surface parameters simulated from the VIC land-surface model (LSM) for Phase 2 of the North American Land Data Assimilation System (NLDAS-2). The data are in 1/8th degree grid spacing. The temporal resolution is monthly, ranging from January to December. The file format is WMO GRIB-1. The NLDAS-2 monthly climatology data are the monthly data averaged over the thirty years (1980-2009) of the NLDAS-2 monthly data. \n\nA brief description about the NLDAS-2 hourly and monthly VIC LSM data can be found from the GCMD DIFs for GES_DISC_NLDAS_VIC0125_H_V002 and GES_DISC_NLDAS_VIC0125_M_V002. \n\nDetails about the NLDAS-2 configuration of the VIC LSM can be found in Xia et al. (2012). The version of the VIC model for the NLDAS-2 VIC data available from the NASA GES DISC is VIC-4.0.3; this version of the VIC model is the same as used in Sheffield et al. (2003). \n\nThe NLDAS-2 VIC monthly climatology data contain forty-three fields. The data set applies a user-defined parameter table to indicate the contents and parameter number. The GRIBTAB file shows a list of parameters for this data set, along with their Product Definition Section (PDS) IDs and units. \n\nFor information about the vertical layers of the Soil Moisture Content (PDS 086), Soil Temperature (PDS 085), and Liquid Soil Moisture Content (PDS 151), please see the README Document or the GrADS ctl file.",
-            "release-place": "Greenbelt, Maryland, USA",
-            "series-name": "NLDAS_VIC0125_MC",
-            "creator": "David Mocko, NASA/GSFC/HSL",
-            "graphic-preview-description": "NLDAS-2 VIC Monthly Climatology 0.125 degree Top 1-meter Soil Moisture Content [kg/m^2] July (1980 - 2009).",
-            "title": "NLDAS VIC Land Surface Model L4 Monthly Climatology 0.125 x 0.125 degree V002 (NLDAS_VIC0125_MC) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/NLDAS_VIC0125_MC_002.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FB0L38R609B0R",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FB0L38R609B0R",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/NLDAS_VIC0125_MC_002.png",
-                    "description": "NLDAS-2 VIC Monthly Climatology 0.125 degree Top 1-meter Soil Moisture Content [kg/m^2] July (1980 - 2009).",
                     "@type": "dcat:Distribution",
+                    "description": "NLDAS-2 VIC Monthly Climatology 0.125 degree Top 1-meter Soil Moisture Content [kg/m^2] July (1980 - 2009).",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/NLDAS_VIC0125_MC_002.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/NLDAS_VIC0125_MC_002.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/NLDAS_VIC0125_MC_002.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://hydro1.gesdisc.eosdis.nasa.gov/data/NLDAS/NLDAS_VIC0125_MC.002/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://hydro1.gesdisc.eosdis.nasa.gov/data/NLDAS/NLDAS_VIC0125_MC.002/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=NLDAS_VIC0125_MC",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=NLDAS_VIC0125_MC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://hydro1.gesdisc.eosdis.nasa.gov/dods/NLDAS_VIC0125_MC.002",
-                    "description": "The GrADS Data Server (GDS) is another form of OPeNDAP that provides subsetting and some analysis services across the Internet.",
                     "@type": "dcat:Distribution",
+                    "description": "The GrADS Data Server (GDS) is another form of OPeNDAP that provides subsetting and some analysis services across the Internet.",
+                    "downloadURL": "https://hydro1.gesdisc.eosdis.nasa.gov/dods/NLDAS_VIC0125_MC.002",
+                    "mediaType": "text/html",
                     "title": "Use GRADS DATA SERVER (GDS) to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://hydro1.gesdisc.eosdis.nasa.gov/data/NLDAS/NLDAS_VIC0125_MC.002/doc/gribtab_NLDAS_VIC.002.txt",
-                    "description": "The GRIBTAB file contains a list of variables, along with the GRIB Product Definition Section (PDS) ID, variable short name, long names, and unit.",
                     "@type": "dcat:Distribution",
+                    "description": "The GRIBTAB file contains a list of variables, along with the GRIB Product Definition Section (PDS) ID, variable short name, long names, and unit.",
+                    "downloadURL": "https://hydro1.gesdisc.eosdis.nasa.gov/data/NLDAS/NLDAS_VIC0125_MC.002/doc/gribtab_NLDAS_VIC.002.txt",
+                    "mediaType": "text/html",
                     "title": "Access to this dataset's extended metadata"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://hydro1.gesdisc.eosdis.nasa.gov/data/NLDAS/README.NLDAS2.pdf",
-                    "description": "README Document",
                     "@type": "dcat:Distribution",
+                    "description": "README Document",
+                    "downloadURL": "https://hydro1.gesdisc.eosdis.nasa.gov/data/NLDAS/README.NLDAS2.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's read me document"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ldas.gsfc.nasa.gov/nldas/",
-                    "description": "NLDAS Project Web Site",
                     "@type": "dcat:Distribution",
+                    "description": "NLDAS Project Web Site",
+                    "downloadURL": "https://ldas.gsfc.nasa.gov/nldas/",
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
                 }
             ],
+            "graphic-preview-description": "NLDAS-2 VIC Monthly Climatology 0.125 degree Top 1-meter Soil Moisture Content [kg/m^2] July (1980 - 2009).",
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/NLDAS_VIC0125_MC_002.png",
+            "identifier": "C1233767676-GES_DISC",
+            "issued": "2014-03-01",
+            "keyword": [
+                "soils",
+                "atmospheric water vapor",
+                "biosphere",
+                "terrestrial hydrosphere",
+                "atmospheric temperature",
+                "atmospheric radiation",
+                "earth science",
+                "vegetation",
+                "land surface",
+                "atmosphere",
+                "snow/ice",
+                "precipitation",
+                "surface radiative properties",
+                "surface thermal properties",
+                "surface water"
+            ],
+            "landingPage": "https://doi.org/10.5067/B0L38R609B0R",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2014-03-01",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
+            },
+            "references": [
+                "https://doi.org/10.1029/2011JD016048",
+                "https://doi.org/10.1029/2011JD016051",
+                "https://doi.org/10.1175/1520-0493(1997)125<2896:AOTLSA>2.0.CO;2",
+                "https://doi.org/10.1023/A:1000531001463",
+                "https://doi.org/10.1029/2002JD003296",
+                "https://doi.org/10.1029/1999JD900232",
+                "https://doi.org/10.1175/2009JHM1174.1",
+                "https://doi.org/10.1002/hyp.9214"
+            ],
+            "release-place": "Greenbelt, Maryland, USA",
+            "series-name": "NLDAS_VIC0125_MC",
             "spatial": "-125.0 25.0 -67.0 53.0",
+            "temporal": "1980-01-01T00:00:00Z/2009-12-31T23:59:59.999Z",
             "theme": [
                 "NLDAS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "NLDAS VIC Land Surface Model L4 Monthly Climatology 0.125 x 0.125 degree V002 (NLDAS_VIC0125_MC) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC4-1137-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 4 phase 2015-10-22 to 2015-12-31. It is a Global Gravity measurement at the comet 67P and covers the time 2015-10-28T10:24:55.000 to 2015-10-28T17:16:04.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc4-1137-v1.0_eaac-8jqn",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC4-1137-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc4-1137-v1.0_eaac-8jqn",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 4 phase 2015-10-22 to 2015-12-31. It is a Global Gravity measurement at the comet 67P and covers the time 2015-10-28T10:24:55.000 to 2015-10-28T17:16:04.000.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 4 1137 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 4 1137 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-5-ESC3-67P-M21-GEO-V1.0",
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
+            "description": "This CODMAC level 5 data set contains derived data products that include pixel-precise georeferencing information, acquired by the OSIRIS Narrow Angle Camera on the Rosetta spacecraft during the COMET ESCORT 3 mission phase, covering the period from 2015-09-22T23:25:00.000 to 2015-10-20T23:24:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V1.0 is the first version of this dataset: Lien corrected dataset after October 2018 PSA/PDS external peer review.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-5-esc3-67p-m21-geo-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-5-ESC3-67P-M21-GEO-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-5-esc3-67p-m21-geo-v1.0",
-            "description": "This CODMAC level 5 data set contains derived data products that include pixel-precise georeferencing information, acquired by the OSIRIS Narrow Angle Camera on the Rosetta spacecraft during the COMET ESCORT 3 mission phase, covering the period from 2015-09-22T23:25:00.000 to 2015-10-20T23:24:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V1.0 is the first version of this dataset: Lien corrected dataset after October 2018 PSA/PDS external peer review.",
-            "title": "ROSETTA-ORBITER 67P OSINAC 5 ESC3-MTP021 DDR-GEO V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P OSINAC 5 ESC3-MTP021 DDR-GEO V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/MODIS/MCD64A1.061",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Louis Giglio, Christopher Justice, Luigi Boschetti, David Roy. 2021-11-08. MODIS/Terra+Aqua Burned Area Monthly L3 Global 500m SIN Grid V061. Sioux Falls, South Dakota, USA. Archived by National Aeronautics and Space Administration, U.S. Government, NASA EOSDIS Land Processes Distributed Active Archive Center. https://doi.org/10.5067/MODIS/MCD64A1.061. https://doi.org/10.5067/MODIS/MCD64A1.061. The DOI landing page provides citations in APA and Chicago styles..",
-            "issued": "2021-04-08",
-            "temporal": "2000-11-01T00:00:00Z/2024-06-03T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2021-04-08",
-            "keyword": [
-                "natural hazards",
-                "human dimensions",
-                "earth science",
-                "biosphere",
-                "environmental impacts",
-                "ecological dynamics",
-                "national geospatial data asset",
-                "ngda"
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
-            "identifier": "C2565786756-LPCLOUD",
-            "description": "The Terra and Aqua combined MCD64A1 Version 6.1 Burned Area data product is a monthly, global gridded 500 meter (m) product containing per-pixel burned-area and quality information. The MCD64A1 burned-area mapping approach employs 500 m Moderate Resolution Imaging Spectroradiometer (MODIS) Surface Reflectance imagery coupled with 1 kilometer (km) MODIS active fire observations. The algorithm uses a burn sensitive Vegetation Index (VI) to create dynamic thresholds that are applied to the composite data. The VI is derived from MODIS shortwave infrared atmospherically corrected surface reflectance bands 5 and 7 with a measure of temporal texture. The algorithm identifies the date of burn for the 500 m grid cells within each individual MODIS tile. The date is encoded in a single data layer as the ordinal day of the calendar year on which the burn occurred with values assigned to unburned land pixels and additional special values reserved for missing data and water grid cells. \r\n\r\nThe data layers provided in the MCD64A1 product include Burn Date, Burn Data Uncertainty, Quality Assurance, along with First Day and Last Day of reliable change detection of the year. \r\n\r\nValidation at stage 3 ( https://modis-land.gsfc.nasa.gov/MODLAND_val.html) has been achieved for the MODIS Burned Area product. Further details regarding MODIS land product validation for the MCD64A1 data product is available from the MODIS Land Team Validation site ( https://modis-land.gsfc.nasa.gov/ValStatus.php?ProductID=MOD64).\r\n      \r\nImprovements/Changes from Previous Versions\r\n\r\n* The Version 6.1 Level-1B (L1B) products have been improved by undergoing various calibration changes that include: changes to the response-versus-scan angle (RVS) approach that affects reflectance bands for Aqua and Terra MODIS, corrections to adjust for the optical crosstalk in Terra MODIS infrared (IR) bands, and corrections to the Terra MODIS forward look-up table (LUT) update for the period 2012 - 2017.\r\n* A polarization correction has been applied to the L1B Reflective Solar Bands (RSB).",
-            "release-place": "Sioux Falls, South Dakota, USA",
-            "graphic-preview-description": "Browse image for Earthdata Search",
             "creator": "Louis Giglio, Christopher Justice, Luigi Boschetti, David Roy",
-            "title": "MODIS/Terra+Aqua Direct Broadcast Burned Area Monthly L3 Global 500m SIN Grid V061",
-            "graphic-preview-file": "https://cmr.earthdata.nasa.gov/browse-scaler/browse_images/granules/G2603088876-LPCLOUD?h=85&w=85",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The Terra and Aqua combined MCD64A1 Version 6.1 Burned Area data product is a monthly, global gridded 500 meter (m) product containing per-pixel burned-area and quality information. The MCD64A1 burned-area mapping approach employs 500 m Moderate Resolution Imaging Spectroradiometer (MODIS) Surface Reflectance imagery coupled with 1 kilometer (km) MODIS active fire observations. The algorithm uses a burn sensitive Vegetation Index (VI) to create dynamic thresholds that are applied to the composite data. The VI is derived from MODIS shortwave infrared atmospherically corrected surface reflectance bands 5 and 7 with a measure of temporal texture. The algorithm identifies the date of burn for the 500 m grid cells within each individual MODIS tile. The date is encoded in a single data layer as the ordinal day of the calendar year on which the burn occurred with values assigned to unburned land pixels and additional special values reserved for missing data and water grid cells. \r\n\r\nThe data layers provided in the MCD64A1 product include Burn Date, Burn Data Uncertainty, Quality Assurance, along with First Day and Last Day of reliable change detection of the year. \r\n\r\nValidation at stage 3 ( https://modis-land.gsfc.nasa.gov/MODLAND_val.html) has been achieved for the MODIS Burned Area product. Further details regarding MODIS land product validation for the MCD64A1 data product is available from the MODIS Land Team Validation site ( https://modis-land.gsfc.nasa.gov/ValStatus.php?ProductID=MOD64).\r\n      \r\nImprovements/Changes from Previous Versions\r\n\r\n* The Version 6.1 Level-1B (L1B) products have been improved by undergoing various calibration changes that include: changes to the response-versus-scan angle (RVS) approach that affects reflectance bands for Aqua and Terra MODIS, corrections to adjust for the optical crosstalk in Terra MODIS infrared (IR) bands, and corrections to the Terra MODIS forward look-up table (LUT) update for the period 2012 - 2017.\r\n* A polarization correction has been applied to the L1B Reflective Solar Bands (RSB).",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMODIS%2FMCD64A1.061",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMODIS%2FMCD64A1.061",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "application/x-hdf",
-                    "downloadURL": "https://e4ftl01.cr.usgs.gov/MOTA/MCD64A1.061/",
-                    "description": "LP DAAC Data Pool provides direct access to available products via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "LP DAAC Data Pool provides direct access to available products via HTTPS.",
+                    "downloadURL": "https://e4ftl01.cr.usgs.gov/MOTA/MCD64A1.061/",
+                    "mediaType": "application/x-hdf",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "application/x-hdf",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=C2565786756-LPCLOUD",
-                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=C2565786756-LPCLOUD",
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
-                    "downloadURL": "https://doi.org/10.5067/MODIS/MCD64A1.061",
-                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
+                    "downloadURL": "https://doi.org/10.5067/MODIS/MCD64A1.061",
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
-                    "downloadURL": "https://lpdaac.usgs.gov/documents/1006/MCD64_User_Guide_V61.pdf",
-                    "description": "The technical information in the User's Guide enables users to interpret and use the data products.",
                     "@type": "dcat:Distribution",
+                    "description": "The technical information in the User's Guide enables users to interpret and use the data products.",
+                    "downloadURL": "https://lpdaac.usgs.gov/documents/1006/MCD64_User_Guide_V61.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://lpdaac.usgs.gov/documents/115/MCD64_ATBD_V6.pdf",
-                    "description": "The ATBD provides physical theory and mathematical procedures for the calculations used to produce the data products.",
                     "@type": "dcat:Distribution",
+                    "description": "The ATBD provides physical theory and mathematical procedures for the calculations used to produce the data products.",
+                    "downloadURL": "https://lpdaac.usgs.gov/documents/115/MCD64_ATBD_V6.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's algorithm theoretical basis document"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/filespec/MODIS/61/MCD64A1",
-                    "description": "The File Specification provides a description of the product file including Scientific Data Sets and their attributes.",
                     "@type": "dcat:Distribution",
+                    "description": "The File Specification provides a description of the product file including Scientific Data Sets and their attributes.",
+                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/filespec/MODIS/61/MCD64A1",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://modis-land.gsfc.nasa.gov/MODLAND_val.html",
-                    "description": "Validation at stage 3 has been achieved for the MODIS Burned Area product.",
                     "@type": "dcat:Distribution",
+                    "description": "Validation at stage 3 has been achieved for the MODIS Burned Area product.",
+                    "downloadURL": "https://modis-land.gsfc.nasa.gov/MODLAND_val.html",
+                    "mediaType": "text/html",
                     "title": "View this dataset's science data product validation documentation"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://modis-land.gsfc.nasa.gov/ValStatus.php?ProductID=MOD64",
-                    "description": "Further details regarding MODIS land product validation for the MCD64A1 data product is available from the MODIS Land Team Validation site.",
                     "@type": "dcat:Distribution",
+                    "description": "Further details regarding MODIS land product validation for the MCD64A1 data product is available from the MODIS Land Team Validation site.",
+                    "downloadURL": "https://modis-land.gsfc.nasa.gov/ValStatus.php?ProductID=MOD64",
+                    "mediaType": "text/html",
                     "title": "View this dataset's science data product validation documentation"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://opendap.cr.usgs.gov/opendap/hyrax/DP131/MOTA/MCD64A1.061/contents.html",
-                    "description": "Access data via Open-source Project for a Network Data Access Protocol",
                     "@type": "dcat:Distribution",
+                    "description": "Access data via Open-source Project for a Network Data Access Protocol",
+                    "downloadURL": "https://opendap.cr.usgs.gov/opendap/hyrax/DP131/MOTA/MCD64A1.061/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/browse-scaler/browse_images/granules/G2603088876-LPCLOUD?h=85&w=85",
-                    "description": "Browse image for Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse image for Earthdata Search",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/browse-scaler/browse_images/granules/G2603088876-LPCLOUD?h=85&w=85",
+                    "mediaType": "text/html",
                     "title": "Get a related visualization"
                 }
             ],
+            "graphic-preview-description": "Browse image for Earthdata Search",
+            "graphic-preview-file": "https://cmr.earthdata.nasa.gov/browse-scaler/browse_images/granules/G2603088876-LPCLOUD?h=85&w=85",
+            "identifier": "C2565786756-LPCLOUD",
+            "issued": "2021-04-08",
+            "keyword": [
+                "natural hazards",
+                "human dimensions",
+                "earth science",
+                "biosphere",
+                "environmental impacts",
+                "ecological dynamics",
+                "national geospatial data asset",
+                "ngda"
+            ],
+            "landingPage": "https://doi.org/10.5067/MODIS/MCD64A1.061",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2021-04-08",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "LP DAAC"
+            },
+            "release-place": "Sioux Falls, South Dakota, USA",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2000-11-01T00:00:00Z/2024-06-03T00:00:00Z",
             "theme": [
                 "Terra",
                 "Aqua",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "MODIS/Terra+Aqua Direct Broadcast Burned Area Monthly L3 Global 500m SIN Grid V061"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.nasa.gov/d/eabz-dvjd",
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
+                    "downloadURL": "https://eosweb.larc.nasa.gov/project/calipso/cal_lid_l2_05kmclay-prov-v3-02_table",
+                    "mediaType": "text/html"
+                }
+            ],
+            "identifier": "NASA-0000167",
             "issued": "2018-06-25",
-            "temporal": "2011-11-01/2013-02-28",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
             "keyword": [
                 "atmospheric science",
                 "satellite",
@@ -693074,511 +693085,473 @@
                 "cloud",
                 "aerosol"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "John M. Kusterer",
-                "hasEmail": "mailto:john.m.kusterer@nasa.gov"
-            },
+            "landingPage": "https://data.nasa.gov/d/eabz-dvjd",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:004"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "NASA-0000167",
-            "description": "Cloud-Aerosol Lidar and Infrared Pathfinder Satellite Observations (CALIPSO) was launched on April 28, 2006 to study the impact of clouds and aerosols on the Earth\u2019s radiation budget and climate. It flies in formation with five other satellites in the international \u201cA-Train\u201d (PDF) constellation for coincident Earth observations. The CALIPSO satellite comprises three instruments, the Cloud-Aerosol LIdar with Orthogonal Polarization (CALIOP), the Imaging Infrared Radiometer (IIR), and the Wide Field Camera (WFC). CALIPSO is a joint satellite mission between NASA and the French Agency, CNES. These data consist 5 km aerosol layer data.",
-            "title": "CALIPSO Lidar L2 5 km Cloud Layer Data V3-02",
-            "programCode": [
-                "026:004"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://eosweb.larc.nasa.gov/project/calipso/cal_lid_l2_05kmclay-prov-v3-02_table",
-                    "mediaType": "text/html"
-                }
-            ],
-            "accrualPeriodicity": "irregular",
+            "temporal": "2011-11-01/2013-02-28",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "CALIPSO Lidar L2 5 km Cloud Layer Data V3-02"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC4-1235-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 4 phase 2015-10-22 to 2015-12-31. It is a Global Gravity measurement at the comet 67P and covers the time 2015-12-04T09:57:10.000 to 2015-12-04T15:48:56.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc4-1235-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC4-1235-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc4-1235-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 4 phase 2015-10-22 to 2015-12-31. It is a Global Gravity measurement at the comet 67P and covers the time 2015-12-04T09:57:10.000 to 2015-12-04T15:48:56.000.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 4 1235 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 4 1235 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RL-CAL-ROLIS-2-PHC-V1.0",
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
+            "description": "This archive contains raw images from the ROLIS instrument onboard ROSETTA Lander, acquired during the PHC (Post Hibernation Commissioning) phase. It also contains documentation which describes the ROLIS experiment. The data archived in this data set conform to the Planetary Data System (PDS) Standards, Version 3.6.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.rl-cal-rolis-2-phc-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "calibration"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RL-CAL-ROLIS-2-PHC-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.rl-cal-rolis-2-phc-v1.0",
-            "description": "This archive contains raw images from the ROLIS instrument onboard ROSETTA Lander, acquired during the PHC (Post Hibernation Commissioning) phase. It also contains documentation which describes the ROLIS experiment. The data archived in this data set conform to the Planetary Data System (PDS) Standards, Version 3.6.",
-            "title": "ROSETTA-LANDER CAL ROLIS 2 PHC V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-LANDER CAL ROLIS 2 PHC V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-ROSINA-4-EXT1-V2.0",
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
+            "description": "This data set contains CODMAC level 4 science data acquired by the ROSINA COPS sensor between 2016-01-13 and 2016-04-05 during the Extension phase 1 of the Rosetta mission to comet 67P/CG. V2.0: Minor species (CH4, NH3, HCN, H2CO, C2H6, CH3OH, H2S, C2H5OH, OCS, CS2) detected by DFMS were added.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rosina-4-ext1-v2.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-ROSINA-4-EXT1-V2.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rosina-4-ext1-v2.0",
-            "description": "This data set contains CODMAC level 4 science data acquired by the ROSINA COPS sensor between 2016-01-13 and 2016-04-05 during the Extension phase 1 of the Rosetta mission to comet 67P/CG. V2.0: Minor species (CH4, NH3, HCN, H2CO, C2H6, CH3OH, H2S, C2H5OH, OCS, CS2) detected by DFMS were added.",
-            "title": "ROSETTA-ORBITER 67P ROSINA 4\n                                      EXT1 V2.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P ROSINA 4\n                                      EXT1 V2.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/152",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Gilmanov, T.G. 2015. NPP Grassland: Otradnoe, Russia 1969-1973, R1. ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/152",
-            "issued": "2015-05-26",
-            "temporal": "1968-01-01T00:00:00Z/1973-12-31T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-08-17",
-            "keyword": [
-                "vegetation",
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
-            "identifier": "C2751939511-ORNL_CLOUD",
             "description": "This data set provides three data files in text format (.txt). Two files contain biomass and above-ground net primary production (ANPP) estimates for two upland meadows with contrasting soil types at the Otradnoe research station of the V.L. Komarov Botanical Institute of the Russian Academy of Sciences located on the Karelian peninsula 100-km to the north of St. Petersburg, Russia. The third file contains monthly and annual climate data recorded at the study site for the period 1968-1973. Measurements of above- and below-ground live and dead biomass were made at a sandy meadow (OTRS) from 1969 to 1972 and at a loamy meadow (OTRL) from 1969 to 1973. Additional biomass measurements were made at OTRS in June 1972 and at OTRL in May 1973. Monthly N, P, and S content of above-ground live biomass were measured 1969-1971 at OTRS.Revision Notes: Only the documentation for this data set has been modified. The data files have been checked for accuracy and are identical to those originally published in 1996.",
-            "graphic-preview-description": "Browse Image",
-            "title": "NPP Grassland: Otradnoe, Russia 1969-1973, R1",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/npp_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F152",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F152",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/npp/grassland/NPP_OTR/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/npp/grassland/NPP_OTR/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/NPP/guides/NPP_OTR.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/NPP/guides/NPP_OTR.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/152",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/152",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/npp/grassland/NPP_OTR/comp/NPP_OTR.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/npp/grassland/NPP_OTR/comp/NPP_OTR.pdf",
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
+            "identifier": "C2751939511-ORNL_CLOUD",
+            "issued": "2015-05-26",
+            "keyword": [
+                "vegetation",
+                "earth science",
+                "biosphere",
+                "ecological dynamics"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/152",
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
             "spatial": "60.83 30.25",
+            "temporal": "1968-01-01T00:00:00Z/1973-12-31T23:59:59Z",
             "theme": [
                 "NPP",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "NPP Grassland: Otradnoe, Russia 1969-1973, R1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/GHOHN-4GM20",
             "citation": "Institute of Atmospheric Sciences and Climate (CNR - Rome). 2016-05-31. Mediterranean Sea High Resolution SST L4 Analysis 1/16deg Resolution. Version 2.0. Mediterranean Sea High Resolution SST L4 Analysis 1/16 deg daily. Institute of Atmospheric Sciences and Climate (CNR - Rome). Archived by National Aeronautics and Space Administration, U.S. Government, Institute of Atmospheric Sciences and Climate (CNR - Rome). https://doi.org/10.5067/GHOHN-4GM20. Institute of Atmospheric Sciences and Climate (CNR - Rome), Institute of Atmospheric Sciences and Climate (CNR - Rome), 2016-05-31, Mediterranean Sea High Resolution SST L4 Analysis 1/16deg Resolution, none.",
-            "issued": "2016-04-19",
-            "temporal": "2007-12-31T19:00:00Z/2023-02-28T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2017-04-28",
-            "references": [
-                "https://doi.org/10.1016%20j.rse.2012.10.012"
-            ],
-            "keyword": [
-                "national geospatial data asset",
-                "oceans",
-                "ngda",
-                "earth science",
-                "ocean temperature"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "undefined",
                 "hasEmail": "mailto:podaac@podaac.jpl.nasa.gov"
             },
-            "identifier": "C2036878073-POCLOUD",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/JPL/PODAAC"
-            },
-            "description": "CNR MED Sea Surface Temperature provides daily gap-free maps (L4) at 0.0625deg. x 0.0625deg. horizontal resolution over the Mediterranean Sea. The data are obtained from infra-red measurements collected by satellite radiometers and statistical interpolation. It is the CMEMS sea surface temperature nominal operational product for the Mediterranean sea.",
-            "release-place": "Institute of Atmospheric Sciences and Climate (CNR - Rome)",
-            "series-name": "Mediterranean Sea High Resolution SST L4 Analysis 1/16deg Resolution",
             "creator": "Institute of Atmospheric Sciences and Climate (CNR - Rome)",
-            "title": "Mediterranean Sea High Resolution SST L4 Analysis 1/16deg Resolution",
-            "graphic-preview-description": "Thumbnail",
-            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/OISST_HR_NRT-GOS-L4-MED-v2.0.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "CNR MED Sea Surface Temperature provides daily gap-free maps (L4) at 0.0625deg. x 0.0625deg. horizontal resolution over the Mediterranean Sea. The data are obtained from infra-red measurements collected by satellite radiometers and statistical interpolation. It is the CMEMS sea surface temperature nominal operational product for the Mediterranean sea.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGHOHN-4GM20",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGHOHN-4GM20",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://gosweb.artov.isac.cnr.it/",
-                    "description": "Data creator project web site",
                     "@type": "dcat:Distribution",
+                    "description": "Data creator project web site",
+                    "downloadURL": "http://gosweb.artov.isac.cnr.it/",
+                    "mediaType": "text/html",
                     "title": "View information related to this dataset"
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
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/OISST_HR_NRT-GOS-L4-MED-v2.0.jpg",
-                    "description": "Thumbnail",
                     "@type": "dcat:Distribution",
+                    "description": "Thumbnail",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/OISST_HR_NRT-GOS-L4-MED-v2.0.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
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
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2036878073-POCLOUD",
-                    "description": "Browse and download granules over HTTPS using the virtual directories",
                     "@type": "dcat:Distribution",
+                    "description": "Browse and download granules over HTTPS using the virtual directories",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2036878073-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2036878073-POCLOUD",
-                    "description": "Browse granule search results in Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse granule search results in Earthdata Search",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2036878073-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://podaac.jpl.nasa.gov/forum/viewtopic.php?f=7&t=298",
-                    "description": "Sea Surface Temperature measurement description",
                     "@type": "dcat:Distribution",
+                    "description": "Sea Surface Temperature measurement description",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/forum/viewtopic.php?f=7&t=298",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "graphic-preview-description": "Thumbnail",
+            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/OISST_HR_NRT-GOS-L4-MED-v2.0.jpg",
+            "identifier": "C2036878073-POCLOUD",
+            "issued": "2016-04-19",
+            "keyword": [
+                "national geospatial data asset",
+                "oceans",
+                "ngda",
+                "earth science",
+                "ocean temperature"
+            ],
+            "landingPage": "https://doi.org/10.5067/GHOHN-4GM20",
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
+            "references": [
+                "https://doi.org/10.1016%20j.rse.2012.10.012"
+            ],
+            "release-place": "Institute of Atmospheric Sciences and Climate (CNR - Rome)",
+            "series-name": "Mediterranean Sea High Resolution SST L4 Analysis 1/16deg Resolution",
             "spatial": "-18.125 30.25 36.25 46.0",
+            "temporal": "2007-12-31T19:00:00Z/2023-02-28T00:00:00Z",
             "theme": [
                 "GHRSST",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Mediterranean Sea High Resolution SST L4 Analysis 1/16deg Resolution"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=GO-J%2FSW-MAG-2-EDR-JA%2FI0%2FJ0-OPTAVMRO-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This data set contains magnetic field vectors acquired by the Galileo magnetometer before and during inbound shock and magnetopause crossings, the Io flyby on Dec 7 (341), 1995, and the part of the J0 orbital cruise. The data were acquired in the optimal averager mode of the instrument. These are raw data provided in their original EDR form. Processing done internal to the instrument remains in the data set.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.go-j-sw-mag-2-edr-ja-i0-j0-optavmro-v1.0_eaj2-nyib",
             "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "jupiter",
                 "galileo",
                 "io"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=GO-J%2FSW-MAG-2-EDR-JA%2FI0%2FJ0-OPTAVMRO-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.go-j-sw-mag-2-edr-ja-i0-j0-optavmro-v1.0_eaj2-nyib",
-            "description": "This data set contains magnetic field vectors acquired by the Galileo magnetometer before and during inbound shock and magnetopause crossings, the Io flyby on Dec 7 (341), 1995, and the part of the J0 orbital cruise. The data were acquired in the optimal averager mode of the instrument. These are raw data provided in their original EDR form. Processing done internal to the instrument remains in the data set.",
-            "title": "GO JUP/SW MAG EDR JUPAPPROACH/IO/JUP OPTAVG MRO V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "GO JUP/SW MAG EDR JUPAPPROACH/IO/JUP OPTAVG MRO V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/MODIS/MYD09GA.NRT.061",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "LANCEMODIS. 2015-09-10. MODIS/Aqua Surface Reflectance Daily L2G Global 1km and 500m SIN Grid. Version 6.1NRT. MODAPS at NASA/GSFC. Archived by National Aeronautics and Space Administration, U.S. Government, The Land, Atmosphere Near real-time Capability for EOS (LANCE). https://doi.org/10.5067/MODIS/MYD09GA.NRT.061.",
-            "issued": "2021-02-07",
-            "temporal": "2021-02-07T00:00:00Z/2023-07-24T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-20",
-            "keyword": [
-                "earth science",
-                "land surface",
-                "national geospatial data asset",
-                "ngda",
-                "surface radiative properties"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "MODAPS USER SUPPORT TEAM",
                 "hasEmail": "mailto:MODAPSUSO@lists.nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/EOS/ESDIS/LANCE MODIS"
-            },
-            "identifier": "C2007651331-LANCEMODIS",
-            "description": "The MODIS/Aqua Surface Reflectance Daily L2G Global 1km and 500m SIN Grid Near Real Time (NRT) product is an estimate of the surface spectral reflectance as it would be measured at ground level in the absence of atmospheric scattering or absorption. Low-level data are corrected for atmospheric gases and aerosols, yielding a level-2 basis for several higher-order gridded level-2 (L2G) and level-3 products.MYD09GA provides Bands 1-7 in a daily gridded L2G product in the Sinusoidal projection, which includes 500-meter reflectance values and 1-kilometerobservation and geolocation statistics. 500-meter Science Data Sets provided by this product include reflectance for Bands 1-7, a quality rating, observation coverage, observation number, and 250-meter scan information.1-kilometer Science Data Sets provided include number of observations, quality state, sensor angles, solar angles, geolocation flags, and orbit pointers.",
-            "release-place": "MODAPS at NASA/GSFC",
             "creator": "LANCEMODIS",
-            "title": "MODIS/Aqua Surface Reflectance Daily L2G Global 1km and 500m SIN Grid NRT",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The MODIS/Aqua Surface Reflectance Daily L2G Global 1km and 500m SIN Grid Near Real Time (NRT) product is an estimate of the surface spectral reflectance as it would be measured at ground level in the absence of atmospheric scattering or absorption. Low-level data are corrected for atmospheric gases and aerosols, yielding a level-2 basis for several higher-order gridded level-2 (L2G) and level-3 products.MYD09GA provides Bands 1-7 in a daily gridded L2G product in the Sinusoidal projection, which includes 500-meter reflectance values and 1-kilometerobservation and geolocation statistics. 500-meter Science Data Sets provided by this product include reflectance for Bands 1-7, a quality rating, observation coverage, observation number, and 250-meter scan information.1-kilometer Science Data Sets provided include number of observations, quality state, sensor angles, solar angles, geolocation flags, and orbit pointers.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMODIS%2FMYD09GA.NRT.061",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMODIS%2FMYD09GA.NRT.061",
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
-                    "description": "Access Collection 6 data set from the MODAPS LANCE-MODIS page.",
                     "@type": "dcat:Distribution",
+                    "description": "Access Collection 6 data set from the MODAPS LANCE-MODIS page.",
+                    "downloadURL": "http://lance3.modaps.eosdis.nasa.gov/data_products/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through MODAPS"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nrt3.modaps.eosdis.nasa.gov/archive/allData/61/MYD09GA",
-                    "description": "Direct access to the download site and directory hosting the MYD09GA 6.1NRT data set.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct access to the download site and directory hosting the MYD09GA 6.1NRT data set.",
+                    "downloadURL": "https://nrt3.modaps.eosdis.nasa.gov/archive/allData/61/MYD09GA",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 }
             ],
+            "identifier": "C2007651331-LANCEMODIS",
+            "issued": "2021-02-07",
+            "keyword": [
+                "earth science",
+                "land surface",
+                "national geospatial data asset",
+                "ngda",
+                "surface radiative properties"
+            ],
+            "landingPage": "https://doi.org/10.5067/MODIS/MYD09GA.NRT.061",
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
+            "temporal": "2021-02-07T00:00:00Z/2023-07-24T00:00:00Z",
             "theme": [
                 "Aqua",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "MODIS/Aqua Surface Reflectance Daily L2G Global 1km and 500m SIN Grid NRT"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/MEASURES/OZONE/DATA308",
             "citation": "Richard D. McPeters. 2012-08-28. SBUV2N18L3zm. Version 1. SBUV2/NOAA-18 Ozone (O3) Profile and Total Column Ozone 1 Month Zonal Mean L3 Global 5.0 degree Latitude Zones V1. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/MEASURES/OZONE/DATA308. https://disc.gsfc.nasa.gov/datacollection/SBUV2N18L3zm_1.html. Digital Science Data. Revised on 2012-05-09 with 2011 data.",
-            "issued": "2013-04-03",
-            "temporal": "2005-07-01T00:00:00Z/2012-12-30T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2013-04-03",
-            "references": [
-                "https://doi.org/doi:10.5194/amt-5-2951-2012",
-                "https://doi.org/doi:10.5194/amt-6-2533-2013",
-                "https://doi.org/doi:10.1002/jgrd.50597"
-            ],
-            "keyword": [
-                "atmospheric chemistry",
-                "atmosphere",
-                "earth science"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "RICHARD MCPETERS, PH. D",
                 "hasEmail": "mailto:richard.d.mcpeters@nasa.gov"
             },
+            "creator": "Richard D. McPeters",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C1251051612-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "The Solar Backscattered Ultraviolet (SBUV) from NOAA-18 Level-3 monthly zonal mean (MZM) product (SBUV2N18L3zm) is derived from the Level-2 retrieved ozone profiles. Ozone retrievals are generated from the v8.6 SBUV algorithm. A Level-3 MZM file computes zonal means covering 5 degree latitude bands for each calendar month. For this product there are 90 months of data from July 2005 through December 2012. There are a total of 36 latitudinal bands, 18 in each hemisphere. Profile data are provided at 21 layers from 1013.25, 639.318, 403.382,254.517, 160.589, 101.325,63.9317, 40.3382, 25.4517, 16.0589, 10.1325, 6.39317,4.03382, 2.54517, 1.60589, 1.01325,0.639317, 0.403382, 0.254517, 0.160589 and 0.101325 hPa (measured at bottom of layer). NOTE: Some profiles have 20 layers and do not report the top most layer. Mixing ratios are reported at 15 layers from 0.5, 0.7, 1.0, 1.5, 2.0, 3.0, 4.0, 5.0, 7.0, 10.0, 15.0, 20.0, 30.0, 40.0 and 50.0 hPa (measured at middle of layer). \n\nThe MZM product averages retrievals that meet the criteria for a good retrieval as determined by error flags in the Level 2 data. A good retrieval is defined as satisfying the following conditions:\n\n 1) Profile Error Flag = 0 or 1 (0 = good retrieval; 1 = solar zenith angle > 84 degrees).\n 2) Total Error Flags = 0, 1, 2 or 5 (0 = good retrieval; 1 = not used; 2 = solar zenith angle > 84 degrees; large discrepancy between profile total and best total ozone).\n\nNOTE - Total error flag = 5 is anomalously applied at high latitudes and high solar zenith angles where the B-Pair total ozone estimate is not as reliable as the ozone profile under these conditions. This error flag may be removed in future version of algorithm.\n\nThe zonal means computed for each month are screened according to the following statistical criteria:\n\n 1) Number of good retrievals for the month greater than or equal to 2/3 of the samples for a nominal month.\n 2) Mean latitude of good retrievals less than or equal to 1 degree from center of latitude band.\n 3) Mean time of good retrievals less than or equal to 4 days from center of month (i.e., day = 15).",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "SBUV2N18L3zm",
-            "creator": "Richard D. McPeters",
-            "title": "SBUV2/NOAA-18 Ozone (O3) Profile and Total Column Ozone 1 Month Zonal Mean L3 Global 5.0 degree Latitude Zones V1 (SBUV2N18L3zm) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/SBUV2N18L3zm_1.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMEASURES%2FOZONE%2FDATA308",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMEASURES%2FOZONE%2FDATA308",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
@@ -693588,184 +693561,182 @@
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/SBUV2N18L3zm_1.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/SBUV2N18L3zm_1.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://measures.gesdisc.eosdis.nasa.gov/data/Ozone/SBUV2N18L3zm.1/",
-                    "description": "Access the data via HTTP.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTP.",
+                    "downloadURL": "https://measures.gesdisc.eosdis.nasa.gov/data/Ozone/SBUV2N18L3zm.1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://measures.gesdisc.eosdis.nasa.gov/opendap/Ozone/SBUV2N18L3zm.1/SBUV2-NOAA18_L3zm_v01-02-2013m0403t071112.h5.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://measures.gesdisc.eosdis.nasa.gov/opendap/Ozone/SBUV2N18L3zm.1/SBUV2-NOAA18_L3zm_v01-02-2013m0403t071112.h5.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://measures.gesdisc.eosdis.nasa.gov/opendap/Ozone/SBUV2N18L3zm.1/catalog.xml",
-                    "description": "Access the data using the THREDDS Catalog.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data using the THREDDS Catalog.",
+                    "downloadURL": "https://measures.gesdisc.eosdis.nasa.gov/opendap/Ozone/SBUV2N18L3zm.1/catalog.xml",
+                    "mediaType": "text/html",
                     "title": "Use THREDDS DATA to download the dataset's data"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://measures.gesdisc.eosdis.nasa.gov/data/Ozone/SBUV2N18L3zm.1/doc/README.SBUVL3MZM.pdf",
-                    "description": "README Document",
                     "@type": "dcat:Distribution",
+                    "description": "README Document",
+                    "downloadURL": "https://measures.gesdisc.eosdis.nasa.gov/data/Ozone/SBUV2N18L3zm.1/doc/README.SBUVL3MZM.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's read me document"
                 }
             ],
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/SBUV2N18L3zm_1.png",
+            "identifier": "C1251051612-GES_DISC",
+            "issued": "2013-04-03",
+            "keyword": [
+                "atmospheric chemistry",
+                "atmosphere",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/MEASURES/OZONE/DATA308",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2013-04-03",
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
+            "series-name": "SBUV2N18L3zm",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2005-07-01T00:00:00Z/2012-12-30T23:59:59.999Z",
             "theme": [
                 "MEaSUREs",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "SBUV2/NOAA-18 Ozone (O3) Profile and Total Column Ozone 1 Month Zonal Mean L3 Global 5.0 degree Latitude Zones V1 (SBUV2N18L3zm) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/911",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Chambers, J.Q., J.P. Schimel, A.D. Nobre, N. Higuchi, L.V. Ferreira, J.M. Melack, and S.E. Trumbore. 2009. LBA-ECO CD-08 Coarse Wood Litter Respiration and Decomposition, Manaus, Brazil. ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/911",
-            "issued": "2023-10-03",
-            "temporal": "1996-07-01T00:00:00Z/1997-08-31T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-10-04",
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
-            "identifier": "C2777409227-ORNL_CLOUD",
             "description": "This data sets contains data on coarse wood density, moisture content, respiration rates and decomposition rate constants in csv format from Manaus Brazil measured from 1/1/1996 through 12/31/1997. The data for respiration reports CO2 flux from coarse litter (trunks and large branches > 10 cm diameter) that was studied in central Amazon forests (Chambers et al. 2001). The respiration study took place during the transition from wet to dry season of 1997 (June-August),and sampling from the decomposition study (Chambers et al. 2000) was carried out during both the dry and wet seasons of 1996-97 (see below). Respiration rates varied over almost two orders of magnitude (1.003-0.014 micro g C g-1 C min-1, n=61), and were significantly correlated with wood density (r2adj = 0.42), and moisture content (r2adj = 0.39). Additional samples taken from a nearby pasture indicated that wood moisture content was the most important factor controlling respiration rates across sites (r2adj = 0.65). Based on average coarse litter wood density and moisture content, the mean long-term carbon loss rate due to respiration was estimated to be 0.13 yr-1 (range of 95% prediction interval (PI) = 0.11-0.15 yr-1).Decomposition rate constants are reported as mass loss fraction per year, for boles of 155 large dead trees (> 10 cm diameter) in central Amazon forests (Chambers et al. 2000). The measurements were carried out over a 2-year period (1996-1997) on permanent plots monitored by the Biological Dynamics of Forest Fragments Project (BDFFP) of the Smithsonian Institution (Lovejoy and Bierregaard 1990; Rankin-De Merona et al. 1992) and the Biomass and Nutrient Experiment (BIONTE) of the National Institute for Amazon Research (Instituto Nacional de Pesquisas da Amazonia-INPA). Mortality data from 21 hectares of permanent inventory plots, monitored for 10-15 years, were used to select dead trees for sampling. A single csv formatted data file includes dates when trees died, their diameter and breast height (DBH, i.e., at 1.3 m) and taxonomic information.Measured rate constants varied by over 1.5 orders of magnitude (0.015-0.67 /yr), averaged 0.19 /yr with predicted error averaging 0.026 /yr. Wood density and bole diameter were significantly and inversely correlated with rate constants. A tree of average biomass was predicted to decompose at 0.17 /yr.Understanding how tropical forest carbon balance will respond to global change requires knowledge of individual heterotrophic and autotrophic respiratory sources, together with factors that control respiratory variability. These data, along with estimates of ecosystem leaf, live wood and soil respiration, were used to estimate total carbon balance as described in Chambers et al (2004).",
-            "graphic-preview-description": "Browse Image",
-            "title": "LBA-ECO CD-08 Coarse Wood Litter Respiration and Decomposition, Manaus, Brazil",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/lba_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F911",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F911",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/lba/carbon_dynamics/CD08_CWD_Res_and_Decomp_Manaus/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/lba/carbon_dynamics/CD08_CWD_Res_and_Decomp_Manaus/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/LBA/guides/CD08_CWD_Resp_and_Decomp_Manaus.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/LBA/guides/CD08_CWD_Resp_and_Decomp_Manaus.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/911",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/911",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/carbon_dynamics/CD08_CWD_Res_and_Decomp_Manaus/comp/CD08_CWD_Resp_and_Decomp_Manaus.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/carbon_dynamics/CD08_CWD_Res_and_Decomp_Manaus/comp/CD08_CWD_Resp_and_Decomp_Manaus.pdf",
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
+            "identifier": "C2777409227-ORNL_CLOUD",
+            "issued": "2023-10-03",
+            "keyword": [
+                "biosphere",
+                "ecological dynamics",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/911",
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
             "spatial": "-60.21 -2.61 -60.12 -2.59",
+            "temporal": "1996-07-01T00:00:00Z/1997-08-31T23:59:59Z",
             "theme": [
                 "LBA-ECO",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "LBA-ECO CD-08 Coarse Wood Litter Respiration and Decomposition, Manaus, Brazil"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/11TMFK7VSHDY",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Gary L. Fahnenstiel, Michael J. Sayers, Robert A. Shuchman, Foad Yousef, & Steven A. Pothoven. 2019-10-31. CMSLakeHuronPPY. Version 1. Carbon Monitoring System Lake Huron Primary Production Yearly. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/11TMFK7VSHDY. https://disc.gsfc.nasa.gov/datacollection/CMSLakeHuronPPY_1.html.",
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
-                "ngda",
-                "ecological dynamics",
-                "national geospatial data asset",
-                "biosphere",
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
-            "identifier": "C1652491701-GES_DISC",
-            "description": "Yearly Average primary production/carbon fixation data for Lake Huron.  The primary production data is derived using MODIS imagery with model data.\n\nThe NASA Carbon Monitoring System (CMS) is designed to make significant contributions in characterizing, quantifying, understanding, and predicting the evolution of global carbon sources and sinks through improved monitoring of carbon stocks and fluxes. The System will use the full range of NASA satellite observations and modeling/analysis capabilities to establish the accuracy, quantitative uncertainties, and utility of products for supporting national and international policy, regulatory, and management activities. CMS will maintain a global emphasis while providing finer scale regional information, utilizing space-based and surface-based data and will rapidly initiate generation and distribution of products both for user evaluation and to inform near-term policy development and planning.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "CMSLakeHuronPPY",
             "creator": "Gary L. Fahnenstiel, Michael J. Sayers, Robert A. Shuchman, Foad Yousef, & Steven A. Pothoven",
-            "title": "Carbon Monitoring System Lake Huron Primary Production Yearly V1 (CMSLakeHuronPPY) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/CMS/CMSLakeHuronPPY_1.png",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "Yearly Average primary production/carbon fixation data for Lake Huron.  The primary production data is derived using MODIS imagery with model data.\n\nThe NASA Carbon Monitoring System (CMS) is designed to make significant contributions in characterizing, quantifying, understanding, and predicting the evolution of global carbon sources and sinks through improved monitoring of carbon stocks and fluxes. The System will use the full range of NASA satellite observations and modeling/analysis capabilities to establish the accuracy, quantitative uncertainties, and utility of products for supporting national and international policy, regulatory, and management activities. CMS will maintain a global emphasis while providing finer scale regional information, utilizing space-based and surface-based data and will rapidly initiate generation and distribution of products both for user evaluation and to inform near-term policy development and planning.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2F11TMFK7VSHDY",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2F11TMFK7VSHDY",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
@@ -693775,45 +693746,45 @@
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/CMSLakeHuronPPY_1.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/CMSLakeHuronPPY_1.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://acdisc.gsfc.nasa.gov/data/CMS/CMSLakeHuronPPY.1",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://acdisc.gsfc.nasa.gov/data/CMS/CMSLakeHuronPPY.1",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://acdisc.gsfc.nasa.gov/data/CMS/CMSLakeHuronPPY.1/doc/README.CMSGreatLakesPrimaryProductivity.V1.pdf",
-                    "description": "README Document",
                     "@type": "dcat:Distribution",
+                    "description": "README Document",
+                    "downloadURL": "https://acdisc.gsfc.nasa.gov/data/CMS/CMSLakeHuronPPY.1/doc/README.CMSGreatLakesPrimaryProductivity.V1.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's read me document"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://acdisc.gsfc.nasa.gov/opendap/CMS/CMSLakeHuronPPY.1",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://acdisc.gsfc.nasa.gov/opendap/CMS/CMSLakeHuronPPY.1",
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
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=CMSLakeHuronPPY",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=CMSLakeHuronPPY",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
@@ -693823,309 +693794,340 @@
                     "title": "This dataset's landing page"
                 }
             ],
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/CMS/CMSLakeHuronPPY_1.png",
+            "identifier": "C1652491701-GES_DISC",
+            "issued": "2019-10-21",
+            "keyword": [
+                "ngda",
+                "ecological dynamics",
+                "national geospatial data asset",
+                "biosphere",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/11TMFK7VSHDY",
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
+            "series-name": "CMSLakeHuronPPY",
             "spatial": "-84.762 43.001 -79.652 46.591",
+            "temporal": "2010-01-01T00:00:00Z/2013-12-31T23:59:59.999Z",
             "theme": [
                 "CMS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Carbon Monitoring System Lake Huron Primary Production Yearly V1 (CMSLakeHuronPPY) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MEX-M-OMEGA-2-EDR-FLIGHT-EXT2-V1.0",
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
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mex-m-omega-2-edr-flight-ext2-v1.0",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2021-05-21",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "mars",
                 "phobos",
                 "deimos",
                 "mars express"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MEX-M-OMEGA-2-EDR-FLIGHT-EXT2-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mex-m-omega-2-edr-flight-ext2-v1.0",
-            "description": "N/A",
-            "title": "OMEGA FLIGHT EXPERIMENT DATA RECORDS FROM FIRST MISSION EXT",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "OMEGA FLIGHT EXPERIMENT DATA RECORDS FROM FIRST MISSION EXT"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/CAMEX-4/CAMERA/DATA101",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Miller, Christopher R.2002. CAMEX-4 DC-8 FORWARD AND NADIR VIDEO [indicate subset used]. Dataset available online from the NASA Global Hydrometeorology Resource Center DAAC, Huntsville, Alabama, U.S.A. DOI: http://dx.doi.org/10.5067/CAMEX-4/CAMERA/DATA101",
-            "issued": "2002-05-08",
-            "temporal": "2001-08-03T00:00:00Z/2001-09-26T23:59:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-05-23",
-            "keyword": [
-                "earth science",
-                "visible wavelengths",
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
-            "identifier": "C1995553210-GHRC_DAAC",
             "description": "The CAMEX-4 DC-8 Forward and NADIR Video dataset consists of DVDs which capture the forward and nadir views from the NASA DC-8 aircraft during CAMEX-4 flights. These videos contain timestamps and the recorded voice channels of the scientists and mission managers aboard the aircraft during flights studying storm conditions.  For further information and to obtain this data, please contact GHRC at support-ghrc@earthdata.nasa.gov",
-            "title": "CAMEX-4 DC-8 FORWARD AND NADIR VIDEO V1",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FCAMEX-4%2FCAMERA%2FDATA101",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FCAMEX-4%2FCAMERA%2FDATA101",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://dx.doi.org/10.5067/CAMEX-4/CAMERA/DATA101",
-                    "description": "Files may be downloaded directly to your workstation from this link",
                     "@type": "dcat:Distribution",
+                    "description": "Files may be downloaded directly to your workstation from this link",
+                    "downloadURL": "http://dx.doi.org/10.5067/CAMEX-4/CAMERA/DATA101",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/doc/camex4/c4dvid/c4dvid_dataset.pdf",
-                    "description": "The guide document contains detailed information about the dataset",
                     "@type": "dcat:Distribution",
+                    "description": "The guide document contains detailed information about the dataset",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/doc/camex4/c4dvid/c4dvid_dataset.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/uso/ds_docs/camex4/c4dvid/c4Flights.pdf",
-                    "description": "DC-8 Flight Dates designating Forward or Nadir",
                     "@type": "dcat:Distribution",
+                    "description": "DC-8 Flight Dates designating Forward or Nadir",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/uso/ds_docs/camex4/c4dvid/c4Flights.pdf",
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
+            "identifier": "C1995553210-GHRC_DAAC",
+            "issued": "2002-05-08",
+            "keyword": [
+                "earth science",
+                "visible wavelengths",
+                "spectral/engineering"
+            ],
+            "landingPage": "https://doi.org/10.5067/CAMEX-4/CAMERA/DATA101",
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
             "spatial": "-100.0 10.0 -60.0 50.0",
+            "temporal": "2001-08-03T00:00:00Z/2001-09-26T23:59:00Z",
             "theme": [
                 "CAMEX-4",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "CAMEX-4 DC-8 FORWARD AND NADIR VIDEO V1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=PVO-V-ONMS-3-SUPERTHRMLOXYGN-HIRES-V1.0",
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
+            "description": "This dataset has one point for each point measured, that went into a successful data fitting for that time interval. The individual flux and density values are computed by dividing each data value by the value of the fitting function at the corresponding time.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.pvo-v-onms-3-superthrmloxygn-hires-v1.0_earn-xt5m",
+            "issued": "2018-06-26",
+            "keyword": [
+                "venus",
+                "pioneer venus"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=PVO-V-ONMS-3-SUPERTHRMLOXYGN-HIRES-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.pvo-v-onms-3-superthrmloxygn-hires-v1.0_earn-xt5m",
-            "description": "This dataset has one point for each point measured, that went into a successful data fitting for that time interval. The individual flux and density values are computed by dividing each data value by the value of the fitting function at the corresponding time.",
-            "title": "PVO VENUS ONMS CALIBRATED SUPERTHERMAL OXYGEN HIGH RES. V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "PVO VENUS ONMS CALIBRATED SUPERTHERMAL OXYGEN HIGH RES. V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/4UH0WF2HOHHB",
             "citation": "Kevin W. Bowman. 2023-10-05. TRPSDL2ALLCRSMGLAG. Version 1. TROPESS CrIS-SNPP L2 for Lagos Megacity, Standard Product V1. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/4UH0WF2HOHHB. https://disc.gsfc.nasa.gov/datacollection/TRPSDL2ALLCRSMGLAG_1.html. Digital Science Data.",
-            "issued": "2023-08-29",
-            "temporal": "2016-01-02T00:00:00Z/2023-10-09T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-08-29",
-            "references": [
-                "https://doi.org/10.1126/sciadv.abf7460"
-            ],
-            "keyword": [
-                "atmospheric temperature",
-                "atmosphere",
-                "atmospheric chemistry",
-                "atmospheric water vapor",
-                "earth science"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "KEVIN BOWMAN",
                 "hasEmail": "mailto:kevin.w.bowman@jpl.nasa.gov"
             },
+            "creator": "Kevin W. Bowman",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C2569837035-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "The TROPESS CrIS-SNPP L2 for Lagos Megacity, Standard Product contains the vertical distribution of seven retrieved atmospheric gases (CH4, CO, H2O, HDO, NH3, O3 and PAN) and temperature, along with formal uncertainties measured by the CrIS instrument on the Suomi-NPP satellite. The forward stream standard product is centered on a 3x3 degree region over Lagos for the time period from 2021-02-01 to present. The NASA TRopospheric Ozone and Precursors from Earth System Sounding (TROPESS) project, uses an optimal estimation algorithm, known as the MUlti-SpEctra, MUlti-SpEcies, Multi-SEnsors (MUSES).\n\nThe data files are written in the netCDF version 4 file format, and each file contains one day of data. The data have a spatial resolution of 14 km (CrIS nadir FOV), and are reported at 17 vertical levels from the surface to 0.1 hPa. The principal investigator for the TROPESS project is Kevin W. Bowman.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "TRPSDL2ALLCRSMGLAG",
-            "creator": "Kevin W. Bowman",
-            "graphic-preview-description": "TROPESS CrIS-SNPP Lagos Megacity (Forward Stream, Standard Product) at 681 hPa on 01 April 2021.",
-            "title": "TROPESS CrIS-SNPP L2 for Lagos Megacity, Standard Product V1 (TRPSDL2ALLCRSMGLAG) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TROPESS/images/TRPSDL2ALLCRSMGLAG_Sample.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2F4UH0WF2HOHHB",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2F4UH0WF2HOHHB",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TROPESS/images/TRPSDL2ALLCRSMGLAG_Sample.png",
-                    "description": "TROPESS CrIS-SNPP Lagos Megacity (Forward Stream, Standard Product) at 681 hPa on 01 April 2021.",
                     "@type": "dcat:Distribution",
+                    "description": "TROPESS CrIS-SNPP Lagos Megacity (Forward Stream, Standard Product) at 681 hPa on 01 April 2021.",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TROPESS/images/TRPSDL2ALLCRSMGLAG_Sample.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/TRPSDL2ALLCRSMGLAG_1.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/TRPSDL2ALLCRSMGLAG_1.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/data/TROPESS_MegaCities_Standard/TRPSDL2ALLCRSMGLAG.1/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/data/TROPESS_MegaCities_Standard/TRPSDL2ALLCRSMGLAG.1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=TRPSDL2ALLCRSMGLAG_1",
-                    "description": "Use the Earthdata Search Client to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search Client to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=TRPSDL2ALLCRSMGLAG_1",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/opendap/TROPESS_MegaCities_Standard/TRPSDL2ALLCRSMGLAG.1/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/opendap/TROPESS_MegaCities_Standard/TRPSDL2ALLCRSMGLAG.1/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/data/TROPESS_MegaCities_Standard/TRPSDL2ALLCRSMGLAG.1/doc/TROPESS_Forward_Stream_README.pdf",
-                    "description": "README Document",
                     "@type": "dcat:Distribution",
+                    "description": "README Document",
+                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/data/TROPESS_MegaCities_Standard/TRPSDL2ALLCRSMGLAG.1/doc/TROPESS_Forward_Stream_README.pdf",
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
+            "graphic-preview-description": "TROPESS CrIS-SNPP Lagos Megacity (Forward Stream, Standard Product) at 681 hPa on 01 April 2021.",
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TROPESS/images/TRPSDL2ALLCRSMGLAG_Sample.png",
+            "identifier": "C2569837035-GES_DISC",
+            "issued": "2023-08-29",
+            "keyword": [
+                "atmospheric temperature",
+                "atmosphere",
+                "atmospheric chemistry",
+                "atmospheric water vapor",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/4UH0WF2HOHHB",
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
+            "series-name": "TRPSDL2ALLCRSMGLAG",
             "spatial": "2.0 5.0 5.0 8.0",
+            "temporal": "2016-01-02T00:00:00Z/2023-10-09T00:00:00Z",
             "theme": [
                 "TROPESS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "TROPESS CrIS-SNPP L2 for Lagos Megacity, Standard Product V1 (TRPSDL2ALLCRSMGLAG) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MESS-E%2FV%2FH%2FSW-MAG-4-SUMM-CALIBRATED-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "Abstract ======== This data set consists of the MESSENGER MAG reduced observations, also known as RDRs. The MAG experiment is a miniature three-axis ring-core fluxgate magnetometer with low- noise electronics. There are five types of MAG RDR data products, which differ in the coordinate system. For each type, one or more averaging intervals are available.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mess-e-v-h-sw-mag-4-summ-calibrated-v1.0_eats-98m2",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "messenger",
                 "venus",
@@ -694133,100 +694135,76 @@
                 "earth",
                 "mercury"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MESS-E%2FV%2FH%2FSW-MAG-4-SUMM-CALIBRATED-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mess-e-v-h-sw-mag-4-summ-calibrated-v1.0_eats-98m2",
-            "description": "Abstract ======== This data set consists of the MESSENGER MAG reduced observations, also known as RDRs. The MAG experiment is a miniature three-axis ring-core fluxgate magnetometer with low- noise electronics. There are five types of MAG RDR data products, which differ in the coordinate system. For each type, one or more averaging intervals are available.",
-            "title": "MAG REDUCED (RDR) DATA E/V/H/SW V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "MAG REDUCED (RDR) DATA E/V/H/SW V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG2-J-UVS-3-RDR-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This data set contains reformatted records derived from data returned by the Voyager Ultraviolet Spectrometer Subsystem on board Voyager 2 during the Jupiter encounter phase of the Voyager mission. Original instrument data were merged with ancillary data from footprint SEDR files provided by the Voyager Project at the Jet Propulsion Laboratory. The final product files are formatted as PDS binary tables.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg2-j-uvs-3-rdr-v1.0_eatx-4j9z",
             "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "comet sl9/jupiter collision",
                 "jupiter",
                 "voyager"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG2-J-UVS-3-RDR-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg2-j-uvs-3-rdr-v1.0_eatx-4j9z",
-            "description": "This data set contains reformatted records derived from data returned by the Voyager Ultraviolet Spectrometer Subsystem on board Voyager 2 during the Jupiter encounter phase of the Voyager mission. Original instrument data were merged with ancillary data from footprint SEDR files provided by the Voyager Project at the Jet Propulsion Laboratory. The final product files are formatted as PDS binary tables.",
-            "title": "VG2 JUPITER ULTRAVIOLET SPECTROMETER SUBSYSTEM 3 RDR V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "VG2 JUPITER ULTRAVIOLET SPECTROMETER SUBSYSTEM 3 RDR V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1273652183-GES_DISC.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Stassinopoulos, E. G.. 1979-01-01. BUVN4L1DCM. Version 001. BUV/Nimbus-4 Dark Current Study Master Data V001. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://disc.gsfc.nasa.gov/datacollection/BUVN4L1DCM_001.html. Digital Science Data.",
-            "issued": "2014-12-14",
-            "temporal": "1970-04-10T00:00:00Z/1971-12-16T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2014-12-14",
-            "keyword": [
-                "spectral/engineering",
-                "earth science",
-                "ultraviolet wavelengths"
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
-            "identifier": "C1273652183-GES_DISC",
-            "description": "The Nimbus-4 BUV Level-1 Dark Current Study Master Data is derived from the BUV Level 1 Radiance (RUT) product and contains the geophysical indices and classification, geographic and geomagnetic coordinates, solar magnetic parameters and angles; monochromator and photometer pulse count and analog data, and energetic trapped particles. There is one-to-one correspondence between this product and the dark current working data files, the difference is the working product data have been filtered.\n\nThe data were originally created on IBM 360 machines and archived on magnetic tapes. The data have been restored from the tapes and are now archived on disk in their original IBM binary file format. Each file contains about one orbit of data from the nighttime descending node. The data files consist of 140 4-byte word records which are blocked with up to 25 records. The average size of an orbit file is 480 kB.\n\nThis product was previously available from the NSSDC with the identifier ESAC-00045 (old ID 70-025A-05H).",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "BUVN4L1DCM",
             "creator": "Stassinopoulos, E. G.",
-            "title": "BUV/Nimbus-4 Dark Current Study Master Data V001 (BUVN4L1DCM) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/BUVN4L1DCM_001.png",
-            "programCode": [
-                "026:001"
-            ],
+            "data-presentation-form": "Digital Science Data",
+            "description": "The Nimbus-4 BUV Level-1 Dark Current Study Master Data is derived from the BUV Level 1 Radiance (RUT) product and contains the geophysical indices and classification, geographic and geomagnetic coordinates, solar magnetic parameters and angles; monochromator and photometer pulse count and analog data, and energetic trapped particles. There is one-to-one correspondence between this product and the dark current working data files, the difference is the working product data have been filtered.\n\nThe data were originally created on IBM 360 machines and archived on magnetic tapes. The data have been restored from the tapes and are now archived on disk in their original IBM binary file format. Each file contains about one orbit of data from the nighttime descending node. The data files consist of 140 4-byte word records which are blocked with up to 25 records. The average size of an orbit file is 480 kB.\n\nThis product was previously available from the NSSDC with the identifier ESAC-00045 (old ID 70-025A-05H).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -694235,244 +694213,245 @@
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/BUVN4L1DCM_001.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/BUVN4L1DCM_001.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/Nimbus4_BUV_Level1/BUVN4L1DCM.001/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/Nimbus4_BUV_Level1/BUVN4L1DCM.001/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=BUVN4L1DCM",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=BUVN4L1DCM",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/Nimbus4_BUV_Level1/BUVN4L1DCM.001/doc/README.BUVN4L1DCS.001.pdf",
-                    "description": "README Document",
                     "@type": "dcat:Distribution",
+                    "description": "README Document",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/Nimbus4_BUV_Level1/BUVN4L1DCM.001/doc/README.BUVN4L1DCS.001.pdf",
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
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/repository/Mission/Nimbus/3.4_Mission_Calibration/3.4.2_Calibration_Data/N4_BUV_DCS_Format.pdf",
-                    "description": "BUV Dark Current Study: Master Data and Working Data",
                     "@type": "dcat:Distribution",
+                    "description": "BUV Dark Current Study: Master Data and Working Data",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/repository/Mission/Nimbus/3.4_Mission_Calibration/3.4.2_Calibration_Data/N4_BUV_DCS_Format.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/repository/Mission/Nimbus/3.4_Mission_Calibration/3.4.1_Calibration_Method/N4_BUV_DarkCurrent_DataFiltering.pdf",
-                    "description": "BUV Dark Current Study: Data Filtering",
                     "@type": "dcat:Distribution",
+                    "description": "BUV Dark Current Study: Data Filtering",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/repository/Mission/Nimbus/3.4_Mission_Calibration/3.4.1_Calibration_Method/N4_BUV_DarkCurrent_DataFiltering.pdf",
+                    "mediaType": "application/pdf",
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
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/BUVN4L1DCM_001.png",
+            "identifier": "C1273652183-GES_DISC",
+            "issued": "2014-12-14",
+            "keyword": [
+                "spectral/engineering",
+                "earth science",
+                "ultraviolet wavelengths"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1273652183-GES_DISC.html",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2014-12-14",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
+            },
+            "release-place": "Greenbelt, MD, USA",
+            "series-name": "BUVN4L1DCM",
             "spatial": "-180.0 -80.1 180.0 80.1",
+            "temporal": "1970-04-10T00:00:00Z/1971-12-16T23:59:59.999Z",
             "theme": [
                 "Nimbus",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "BUV/Nimbus-4 Dark Current Study Master Data V001 (BUVN4L1DCM) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewBundle.jsp?identifier=urn%3Anasa%3Apds%3Amaven.mag.calibrated&version=2.3",
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
-                "mars atmosphere and volatile evolution mission",
-                "mars"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This bundle contains MAG supplied ASCII files containing a time series of  magnetic-field vectors in geophysical units (nanotesla, nT) that have been  corrected for instrumental and spacecraft effects (calibrated). In addition,  these data have been transformed into physically meaningful coordinate systems. MAG data products are generated for all mission phases.",
+            "identifier": "urn:nasa:pds:maven.mag.calibrated_eavn-h74s",
+            "issued": "2018-06-26",
+            "keyword": [
+                "mars atmosphere and volatile evolution mission",
+                "mars"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewBundle.jsp?identifier=urn%3Anasa%3Apds%3Amaven.mag.calibrated&version=2.3",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:maven.mag.calibrated_eavn-h74s",
-            "description": "This bundle contains MAG supplied ASCII files containing a time series of  magnetic-field vectors in geophysical units (nanotesla, nT) that have been  corrected for instrumental and spacecraft effects (calibrated). In addition,  these data have been transformed into physically meaningful coordinate systems. MAG data products are generated for all mission phases.",
-            "title": "MAVEN MAG Calibrated Data Bundle",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "MAVEN MAG Calibrated Data Bundle"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.7927/tmsp-sg82",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Anderson, W., W. Baethgen, F. Capitanio, P. Ciais, G. Rocca da Cunha, L. Goddard, B. Schauberger , K. Sonder, G. Podesta, M. van der Velde, L. You, and Y. Ru. 2022-08-19. Twentieth Century Crop Statistics, 1900-2017. Version 1.00. Palisades, NY. Archived by National Aeronautics and Space Administration, U.S. Government, NASA Socioeconomic Data and Applications Center (SEDAC). https://doi.org/10.7927/tmsp-sg82. https://doi.org/10.7927/tmsp-sg82.",
-            "issued": "2022-08-19",
-            "temporal": "1900-01-01T00:00:00Z/2017-12-31T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-08-19",
-            "references": [
-                "https://doi.org/10.7927/8zwk-nr08"
-            ],
-            "keyword": [
-                "human dimensions",
-                "earth science",
-                "economic resources"
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
-            "identifier": "C2418990437-SEDAC",
-            "description": "The Twentieth Century Crop Statistics, 1900-2017 data set consists of national or subnational maize and wheat production, yield, and harvested area statistics for all available years for the period 1900-2017. It combines a new digitization of crop statistics from Italy, Spain, Indonesia, China, Mexico, Uruguay, Chile, Sweden, and Morocco with existing, publicly available, digitized data sets from India, Australia, the United States, Canada, Southern Brazil, Argentina, England, Austria, Belgium, Croatia, Czech Republic, Finland, Germany, Spain, Portugal, France, the Netherlands, and South Africa. All Units are converted to hectares (ha) for Units of harvested areas, tonnes for Units of production, and tonnes/ha for Units of yield. A ratio of 1/36.744 is used to convert wheat bushels to tonnes, and a value of 1/39.368 is used to convert maize bushels to tonnes. In all cases, the Harvest_year reported in the data set is the harvest year for the crop.",
-            "release-place": "Palisades, NY",
-            "graphic-preview-description": "Sample browse graphic of the data set.",
             "creator": "Anderson, W., W. Baethgen, F. Capitanio, P. Ciais, G. Rocca da Cunha, L. Goddard, B. Schauberger , K. Sonder, G. Podesta, M. van der Velde, L. You, and Y. Ru",
-            "title": "Twentieth Century Crop Statistics, 1900-2017",
-            "graphic-preview-file": "https://sedac.ciesin.columbia.edu/downloads/maps/cddc/food-twentieth-century-crop-statistics-1900-2017/sedac-logo.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The Twentieth Century Crop Statistics, 1900-2017 data set consists of national or subnational maize and wheat production, yield, and harvested area statistics for all available years for the period 1900-2017. It combines a new digitization of crop statistics from Italy, Spain, Indonesia, China, Mexico, Uruguay, Chile, Sweden, and Morocco with existing, publicly available, digitized data sets from India, Australia, the United States, Canada, Southern Brazil, Argentina, England, Austria, Belgium, Croatia, Czech Republic, Finland, Germany, Spain, Portugal, France, the Netherlands, and South Africa. All Units are converted to hectares (ha) for Units of harvested areas, tonnes for Units of production, and tonnes/ha for Units of yield. A ratio of 1/36.744 is used to convert wheat bushels to tonnes, and a value of 1/39.368 is used to convert maize bushels to tonnes. In all cases, the Harvest_year reported in the data set is the harvest year for the crop.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.7927%2Ftmsp-sg82",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.7927%2Ftmsp-sg82",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/downloads/maps/cddc/food-twentieth-century-crop-statistics-1900-2017/sedac-logo.jpg",
-                    "description": "Sample browse graphic of the data set.",
                     "@type": "dcat:Distribution",
+                    "description": "Sample browse graphic of the data set.",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/downloads/maps/cddc/food-twentieth-century-crop-statistics-1900-2017/sedac-logo.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/food-twentieth-century-crop-statistics-1900-2017/data-download",
-                    "description": "Data Download Page",
                     "@type": "dcat:Distribution",
+                    "description": "Data Download Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/food-twentieth-century-crop-statistics-1900-2017/data-download",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/food-twentieth-century-crop-statistics-1900-2017/docs",
-                    "description": "Documentation Page",
                     "@type": "dcat:Distribution",
+                    "description": "Documentation Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/food-twentieth-century-crop-statistics-1900-2017/docs",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/food-twentieth-century-crop-statistics-1900-2017",
-                    "description": "Data Set\u00a0Overview Page",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set\u00a0Overview Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/food-twentieth-century-crop-statistics-1900-2017",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "graphic-preview-description": "Sample browse graphic of the data set.",
+            "graphic-preview-file": "https://sedac.ciesin.columbia.edu/downloads/maps/cddc/food-twentieth-century-crop-statistics-1900-2017/sedac-logo.jpg",
+            "identifier": "C2418990437-SEDAC",
+            "issued": "2022-08-19",
+            "keyword": [
+                "human dimensions",
+                "earth science",
+                "economic resources"
+            ],
+            "landingPage": "https://doi.org/10.7927/tmsp-sg82",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2022-08-19",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "SEDAC"
+            },
+            "references": [
+                "https://doi.org/10.7927/8zwk-nr08"
+            ],
+            "release-place": "Palisades, NY",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "1900-01-01T00:00:00Z/2017-12-31T00:00:00Z",
             "theme": [
                 "FOOD",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Twentieth Century Crop Statistics, 1900-2017"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/GNSS/GDGPS_daily_eop_glo_001",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "NASA Jet Propulsion Laboratory, JPL GDGPS GLONASS Earth orientation parameters product, Greenbelt, MD, USA:NASA Crustal Dynamics Data Information System (CDDIS), Accessed [[enter user data access date]] at doi:10.5067/GNSS/GDGPS_daily_eop_glo_001",
-            "issued": "1992-01-01",
-            "temporal": "2023-10-01T00:00:00Z/2025-01-06T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-03",
-            "keyword": [
-                "solid earth",
-                "tectonics",
-                "earth science",
-                "gravity/gravitational field",
-                "geodetics"
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
-            "identifier": "C2792566257-CDDIS",
             "description": "This product contains a time series of Earth orientation parameters from the IERS Bulletin A for the GLONASS constellation of satellites. The product is generated at JPL's Global Differential GPS Operations Centers.",
-            "title": "Ground-Based Global Navigation Satellite System (GNSS) Guardian GLONASS Earth Orientation Parameters (1-day sampling, 7-day files) from NASA CDDIS",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGNSS%2FGDGPS_daily_eop_glo_001%0D%0A",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGNSS%2FGDGPS_daily_eop_glo_001%0D%0A",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
@@ -694488,515 +694467,518 @@
                     "title": "Download this dataset"
                 }
             ],
+            "identifier": "C2792566257-CDDIS",
+            "issued": "1992-01-01",
+            "keyword": [
+                "solid earth",
+                "tectonics",
+                "earth science",
+                "gravity/gravitational field",
+                "geodetics"
+            ],
+            "landingPage": "https://doi.org/10.5067/GNSS/GDGPS_daily_eop_glo_001",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2025-01-03",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "CDDIS"
+            },
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2023-10-01T00:00:00Z/2025-01-06T00:00:00Z",
             "theme": [
                 "IGS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Ground-Based Global Navigation Satellite System (GNSS) Guardian GLONASS Earth Orientation Parameters (1-day sampling, 7-day files) from NASA CDDIS"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-X-SDC-2-LAUNCH-V2.0",
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
+            "description": "This data set contains Raw data taken by the New Horizons Student Dust Counter instrument during the post-launch checkout mission phase.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-x-sdc-2-launch-v2.0_eaxz-jbeg",
+            "issued": "2021-05-21",
+            "keyword": [
+                "new horizons",
+                "dust"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-X-SDC-2-LAUNCH-V2.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-x-sdc-2-launch-v2.0_eaxz-jbeg",
-            "description": "This data set contains Raw data taken by the New Horizons Student Dust Counter instrument during the post-launch checkout mission phase.",
-            "title": "NEW HORIZONS SDC POST-LAUNCH CHECKOUT V2.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "NEW HORIZONS SDC POST-LAUNCH CHECKOUT V2.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-4-ESC2-67P-M17-INF-REFL-V1.0",
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
+            "description": "This CODMAC level 4 data set contains solar stray-light corrected, in-field stray-light corrected,  radiometric calibrated and geometric distortion corrected  (resampled) image data in reflectance units (normalized  and thus without unit),  acquired by the OSIRIS Wide Angle Camera on the Rosetta spacecraft  during the COMET ESCORT 2 mission phase, covering the period  from 2015-06-02T23:25:00.000 to 2015-06-30T23:24:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V1.0 is the first version of this dataset: Lien corrected dataset after September 2019 PSA/PDS external peer review.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-4-esc2-67p-m17-inf-refl-v1.0_eb2m-qepw",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-4-ESC2-67P-M17-INF-REFL-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-4-esc2-67p-m17-inf-refl-v1.0_eb2m-qepw",
-            "description": "This CODMAC level 4 data set contains solar stray-light corrected, in-field stray-light corrected,  radiometric calibrated and geometric distortion corrected  (resampled) image data in reflectance units (normalized  and thus without unit),  acquired by the OSIRIS Wide Angle Camera on the Rosetta spacecraft  during the COMET ESCORT 2 mission phase, covering the period  from 2015-06-02T23:25:00.000 to 2015-06-30T23:24:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V1.0 is the first version of this dataset: Lien corrected dataset after September 2019 PSA/PDS external peer review.",
-            "title": "ROSETTA-ORBITER 67P OSIWAC 4 ESC2-MTP017 RDR-INF-REFL V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P OSIWAC 4 ESC2-MTP017 RDR-INF-REFL V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/SCKWZSWQ7HPL",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "SMAP Radar Twice-Daily SAR and SIR-Enhanced Scatterometer EASE-Grid 2.0 Radar Backscatter V001. Version 1. Archived by National Aeronautics and Space Administration, U.S. Government, NASA NSIDC DAAC. https://doi.org/10.5067/SCKWZSWQ7HPL.",
-            "issued": "2015-04-19",
-            "temporal": "2015-04-13T00:00:00Z/2015-07-12T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2015-07-12",
-            "keyword": [
-                "spectral/engineering",
-                "radar",
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
-            "identifier": "C2568349136-NSIDC_ECS",
             "description": "This data set contains twice-daily synthetic aperture radar (SAR) and enhanced-resolution scatterometer radar backscatter derived from SMAP radar data. Data are available on the Northern Hemisphere, Southern Hemisphere, Temperate, and Mid-Latitude (sub-set of Global) EASE-Grid 2.0 projections and as either 25 km or 3.125 km resolution grids. This new product uses the drop-in-the bucket gridding (GRD) algorithm and Scatterometer Image Reconstruction (SIR) algorithm to process the individual swath-based data from the input data sets into twice-daily images, producing SAR images (high-resolution), slice and footprint images (both lower-resolution), respectively. Note, that as a companion product, the radiometer form of the SIR algorithm (rSIR) was used to derive brightness temperatures from SMAP radiometer data for the <i>SMAP Radiometer Twice-Daily rSIR-Enhanced EASE-Grid 2.0 Brightness Temperatures, Version 2</i>, data set (<a href=\"https://nsidc.org/data/nsidc-0738\">NSIDC-0738</a>).",
-            "title": "SMAP Radar Twice-Daily SAR and SIR-Enhanced Scatterometer EASE-Grid 2.0 Radar Backscatter V001",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSCKWZSWQ7HPL",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSCKWZSWQ7HPL",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/SMAP/NSIDC-0774.001/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/SMAP/NSIDC-0774.001/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=NSIDC-0774+V001",
-                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=NSIDC-0774+V001",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/data/data-access-tool/NSIDC-0774/versions/1",
-                    "description": "Search and filter data files using a map-based interface",
                     "@type": "dcat:Distribution",
+                    "description": "Search and filter data files using a map-based interface",
+                    "downloadURL": "https://nsidc.org/data/data-access-tool/NSIDC-0774/versions/1",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/SCKWZSWQ7HPL",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/SCKWZSWQ7HPL",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/SCKWZSWQ7HPL",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/SCKWZSWQ7HPL",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C2568349136-NSIDC_ECS",
+            "issued": "2015-04-19",
+            "keyword": [
+                "spectral/engineering",
+                "radar",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/SCKWZSWQ7HPL",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2015-07-12",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA NSIDC DAAC"
+            },
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2015-04-13T00:00:00Z/2015-07-12T23:59:59.999Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "SMAP Radar Twice-Daily SAR and SIR-Enhanced Scatterometer EASE-Grid 2.0 Radar Backscatter V001"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MR9-M-ISS-2-EDR-V1.0",
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
+            "description": "These Mariner 9 Imaging Science Subsystem Experiment Data Records arein the process of being archived. The image products currently available online are in PDS format, but are not the final products. There are being provided to assist with studies of the South Polar region of Mars, in preparation for the Mars Surveyor 98 landing this December.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mr9-m-iss-2-edr-v1.0_eb76-38ay",
+            "issued": "2018-06-26",
+            "keyword": [
+                "pds"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MR9-M-ISS-2-EDR-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mr9-m-iss-2-edr-v1.0_eb76-38ay",
-            "description": "These Mariner 9 Imaging Science Subsystem Experiment Data Records arein the process of being archived. The image products currently available online are in PDS format, but are not the final products. There are being provided to assist with studies of the South Polar region of Mars, in preparation for the Mars Surveyor 98 landing this December.",
-            "title": "MARINER 9 MARS IMAGING SCI SUBSYSTEM EXP DATA RECORDS V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "MARINER 9 MARS IMAGING SCI SUBSYSTEM EXP DATA RECORDS V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC2-0705-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 2 phase 2015-03-11 to 2015-06-30. It is a Global Gravity measurement at the comet 67P and covers the time 2015-04-12T08:28:35.000 to 2015-04-12T13:19:09.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc2-0705-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC2-0705-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc2-0705-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 2 phase 2015-03-11 to 2015-06-30. It is a Global Gravity measurement at the comet 67P and covers the time 2015-04-12T08:28:35.000 to 2015-04-12T13:19:09.000.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 2 0705 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 2 0705 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/CALIOP/CALIPSO/LID_L2_01KMCLAY-STANDARD-V4-20",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2018-10-10. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/CALIOP/CALIPSO/LID_L2_01KMCLAY-STANDARD-V4-20. https://asdc.larc.nasa.gov/project/CALIPSO.",
-            "issued": "2018-09-05",
-            "temporal": "2006-06-12T00:00:00Z/2022-01-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2018-09-05",
-            "keyword": [
-                "earth science",
-                "lidar",
-                "clouds",
-                "spectral/engineering",
-                "atmosphere"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "CHARLES TREPTE",
                 "hasEmail": "mailto:charles.r.trepte@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/LARC/SD/ASDC"
-            },
-            "identifier": "C1556717898-LARC_ASDC",
             "description": "CAL_LID_L2_01kmCLay-Standard-V4-20 is the Cloud-Aerosol Lidar and Infrared Pathfinder Satellite Observations (CALIPSO) Lidar Level 2 1 km Cloud Layer, Version 4-20 data product. Data for this product was collected using the CALIPSO Cloud-Aerosol Lidar with Orthogonal Polarization (CALIOP) instrument. Data collection for this product is ongoing.\nCALIPSO was launched on April 28, 2006 to study the impact of clouds and aerosols on the Earth's radiation budget and climate. It flies in the international A-Train constellation for coincident Earth observations. The CALIPSO satellite comprises three instruments, CALIOP, Imaging Infrared Radiometer (IIR), and Wide Field Camera (WFC). CALIPSO is a joint satellite mission between NASA and the French Agency, CNES.",
-            "title": "CALIPSO Lidar Level 2 1 km Cloud Layer, V4-20",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FCALIOP%2FCALIPSO%2FLID_L2_01KMCLAY-STANDARD-V4-20",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FCALIOP%2FCALIPSO%2FLID_L2_01KMCLAY-STANDARD-V4-20",
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
-                    "downloadURL": "https://www-calipso.larc.nasa.gov/resources/calipso_users_guide/qs/cal_lid_l2_all_v4-20.php",
-                    "description": "Data Quality Summary for the CALIPSO Version 4.20 Lidar Level 2 Data Products",
                     "@type": "dcat:Distribution",
+                    "description": "Data Quality Summary for the CALIPSO Version 4.20 Lidar Level 2 Data Products",
+                    "downloadURL": "https://www-calipso.larc.nasa.gov/resources/calipso_users_guide/qs/cal_lid_l2_all_v4-20.php",
+                    "mediaType": "text/html",
                     "title": "View this dataset's product quality assessment"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1556717898-LARC_ASDC",
-                    "description": "Earthdata Search for CAL_LID_L2_01kmCLay-Standard-V4-20_V4-20 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for CAL_LID_L2_01kmCLay-Standard-V4-20_V4-20 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1556717898-LARC_ASDC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/CALIPSO/LID_L2_01kmCLay-Standard-V4-20/contents.html",
-                    "description": "OPeNDAP data access for CAL_LID_L2_01kmCLay-Standard-V4-20_V4-20",
                     "@type": "dcat:Distribution",
+                    "description": "OPeNDAP data access for CAL_LID_L2_01kmCLay-Standard-V4-20_V4-20",
+                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/CALIPSO/LID_L2_01kmCLay-Standard-V4-20/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/CALIOP/CALIPSO/LID_L2_01KMCLAY-STANDARD-V4-20",
-                    "description": "DOI data set landing page for CAL_LID_L2_01kmCLay-Standard-V4-20_V4-20",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for CAL_LID_L2_01kmCLay-Standard-V4-20_V4-20",
+                    "downloadURL": "https://doi.org/10.5067/CALIOP/CALIPSO/LID_L2_01KMCLAY-STANDARD-V4-20",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
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
-                    "downloadURL": "https://www-calipso.larc.nasa.gov/resources/calipso_users_guide/browse/index.php",
-                    "description": "CALIPSO - Data User's Guide - Browse Image Tutorial",
                     "@type": "dcat:Distribution",
+                    "description": "CALIPSO - Data User's Guide - Browse Image Tutorial",
+                    "downloadURL": "https://www-calipso.larc.nasa.gov/resources/calipso_users_guide/browse/index.php",
+                    "mediaType": "text/html",
                     "title": "View this dataset's user's guide"
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
-                    "downloadURL": "https://www-calipso.larc.nasa.gov/resources/calipso_users_guide/",
-                    "description": "CALIPSO Data User\u2019s Guide",
                     "@type": "dcat:Distribution",
+                    "description": "CALIPSO Data User\u2019s Guide",
+                    "downloadURL": "https://www-calipso.larc.nasa.gov/resources/calipso_users_guide/",
+                    "mediaType": "text/html",
                     "title": "View this dataset's user's guide"
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
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/calipso/TiltModeGeometry.pdf",
-                    "description": "CALIPSO Tilt Mode Geometry Anomaly Anomalies",
                     "@type": "dcat:Distribution",
+                    "description": "CALIPSO Tilt Mode Geometry Anomaly Anomalies",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/calipso/TiltModeGeometry.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's documented anomalies"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://www.nasa.gov/pdf/137028main_FS-2005-09-120-LaRC.pdf",
-                    "description": "CALIPSO: Cloud-Aerosol Lidar and Infrared Pathfinder Satellite Observations Fact Sheet",
                     "@type": "dcat:Distribution",
+                    "description": "CALIPSO: Cloud-Aerosol Lidar and Infrared Pathfinder Satellite Observations Fact Sheet",
+                    "downloadURL": "https://www.nasa.gov/pdf/137028main_FS-2005-09-120-LaRC.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's publications"
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
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.icare.univ-lille.fr/category/icare-news/tools/",
-                    "description": "ICARE Programmers Toolbox",
                     "@type": "dcat:Distribution",
+                    "description": "ICARE Programmers Toolbox",
+                    "downloadURL": "https://www.icare.univ-lille.fr/category/icare-news/tools/",
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
-                    "downloadURL": "https://www.nasa.gov/mission_pages/calipso/main/index.html",
-                    "description": "NASA Mission Overview of CALIPSO",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Mission Overview of CALIPSO",
+                    "downloadURL": "https://www.nasa.gov/mission_pages/calipso/main/index.html",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/calipso/ASDC_CALIPSO_Overview_2015.pdf",
-                    "description": "Overview of CALIPSO Data at the ASDC",
                     "@type": "dcat:Distribution",
+                    "description": "Overview of CALIPSO Data at the ASDC",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/calipso/ASDC_CALIPSO_Overview_2015.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/CALIPSO/LID_L2_01kmCLay-Standard-V4-20/",
-                    "description": "ASDC Direct Data Download for CAL_LID_L2_01kmCLay-Standard-V4-20_V4-20",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for CAL_LID_L2_01kmCLay-Standard-V4-20_V4-20",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/CALIPSO/LID_L2_01kmCLay-Standard-V4-20/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://subset.larc.nasa.gov/calipso/",
-                    "description": "CALIPSO Search and Subsetting Web Application",
                     "@type": "dcat:Distribution",
+                    "description": "CALIPSO Search and Subsetting Web Application",
+                    "downloadURL": "https://subset.larc.nasa.gov/calipso/",
+                    "mediaType": "text/html",
                     "title": "Subset this dataset using a web based subsetter"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/calipso/data_product_maturity.html",
-                    "description": "Overview of CALIPSO Data Product Maturity",
                     "@type": "dcat:Distribution",
+                    "description": "Overview of CALIPSO Data Product Maturity",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/calipso/data_product_maturity.html",
+                    "mediaType": "text/html",
                     "title": "View this dataset's product usage"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/calipso/data_release_summary_statement.html",
-                    "description": "CALIPSO Data Release Summary Statement",
                     "@type": "dcat:Distribution",
+                    "description": "CALIPSO Data Release Summary Statement",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/calipso/data_release_summary_statement.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/news/calipso-caliop-l2-lidar-standard-v420-release-announcement",
-                    "description": "ASDC List of CALIPSO CALIOP L2 Lidar Standard V4.20 Release Announcements",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC List of CALIPSO CALIOP L2 Lidar Standard V4.20 Release Announcements",
+                    "downloadURL": "https://asdc.larc.nasa.gov/news/calipso-caliop-l2-lidar-standard-v420-release-announcement",
+                    "mediaType": "text/html",
                     "title": "View this dataset's product history"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www-calipso.larc.nasa.gov/products/",
-                    "description": "CALIPSO Products Overview",
                     "@type": "dcat:Distribution",
+                    "description": "CALIPSO Products Overview",
+                    "downloadURL": "https://www-calipso.larc.nasa.gov/products/",
+                    "mediaType": "text/html",
                     "title": "View this dataset's production history"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.icare.univ-lille.fr/",
-                    "description": "ICARE Data and Services Center Home Page",
                     "@type": "dcat:Distribution",
+                    "description": "ICARE Data and Services Center Home Page",
+                    "downloadURL": "https://www.icare.univ-lille.fr/",
+                    "mediaType": "text/html",
                     "title": "The dataset's home page"
                 }
             ],
+            "identifier": "C1556717898-LARC_ASDC",
+            "issued": "2018-09-05",
+            "keyword": [
+                "earth science",
+                "lidar",
+                "clouds",
+                "spectral/engineering",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.5067/CALIOP/CALIPSO/LID_L2_01KMCLAY-STANDARD-V4-20",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2018-09-05",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/LARC/SD/ASDC"
+            },
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2006-06-12T00:00:00Z/2022-01-17T00:00:00Z",
             "theme": [
                 "CALIPSO",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "CALIPSO Lidar Level 2 1 km Cloud Layer, V4-20"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.nasa.gov/d/ebe6-is69",
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
-            "identifier": "NASA-0000038__46",
+            "describedBy": "http://planetarynames.wr.usgs.gov/Page/Website",
             "description": "Planetary nomenclature, like terrestrial nomenclature, is used to uniquely identify a feature on the surface of a planet or satellite so that the feature can be easily located, described, and discussed. This gazetteer contains detailed information about all names of topographic and albedo features on planets and satellites (and some planetary ring and ring-gap systems) that the International Astronomical Union (IAU) has named and approved from its founding in 1919 through the present time.",
-            "title": "Gazetteer of Planetary Nomenclature",
-            "programCode": [
-                "026:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -695004,146 +694986,140 @@
                     "mediaType": "application/vnd.google-earth.kmz"
                 }
             ],
-            "describedBy": "http://planetarynames.wr.usgs.gov/Page/Website",
-            "accrualPeriodicity": "irregular"
+            "identifier": "NASA-0000038__46",
+            "issued": "2018-06-25",
+            "keyword": [
+                "space science",
+                "nen",
+                "geography",
+                "wise"
+            ],
+            "landingPage": "https://data.nasa.gov/d/ebe6-is69",
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
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MGN-V-RSS-5-LOSAPDR-L2-V1.13",
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
+            "description": "Line of Sight Acceleration Profile Data Records (LOSAPDR) consist of data from Doppler tracking of the orbiting spacecraft. The relative motion of the spacecraft and the earth-based radio receiver is measured very precisely, and known motions are removed a priori (i.e. earth rotation, planetary motions, spacecraft orbital motion, solar pressure, drag), leaving small velocity changes caused by variations in the mass distribution of the planet. The residual Doppler frequency shifts are linearly proportional to the component of velocity in the Earth direction. Numerical differentiation of these velocity residuals with respect to time produces line-of-sight (LOS) gravity. These measures are accelerations at spacecraft altitude which can be modeled for geophysical interpretation. For information on Magellan gravity investigations see papers in [ICARUSMGN1994].",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mgn-v-rss-5-losapdr-l2-v1.13_ebg9-e8a5",
+            "issued": "2021-05-21",
+            "keyword": [
+                "magellan",
+                "venus"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MGN-V-RSS-5-LOSAPDR-L2-V1.13",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mgn-v-rss-5-losapdr-l2-v1.13_ebg9-e8a5",
-            "description": "Line of Sight Acceleration Profile Data Records (LOSAPDR) consist of data from Doppler tracking of the orbiting spacecraft. The relative motion of the spacecraft and the earth-based radio receiver is measured very precisely, and known motions are removed a priori (i.e. earth rotation, planetary motions, spacecraft orbital motion, solar pressure, drag), leaving small velocity changes caused by variations in the mass distribution of the planet. The residual Doppler frequency shifts are linearly proportional to the component of velocity in the Earth direction. Numerical differentiation of these velocity residuals with respect to time produces line-of-sight (LOS) gravity. These measures are accelerations at spacecraft altitude which can be modeled for geophysical interpretation. For information on Magellan gravity investigations see papers in [ICARUSMGN1994].",
-            "title": "MGN V RSS LINE OF SIGHT ACCELERATION PROFILES V1.13",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "MGN V RSS LINE OF SIGHT ACCELERATION PROFILES V1.13"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/GPM/SSMIS/F17/GPROFCLIM/3A-DAY/07",
             "citation": "GPM Science Team. 2022-05-09. GPM_3GPROFF17SSMIS_DAY_CLIM. Version 07. GPM SSMIS on F17 (GPROF) Climate-based Radiometer Precipitation Profiling L3 1 day 0.25 degree x 0.25 degree V07. Greenbelt, MD. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/GPM/SSMIS/F17/GPROFCLIM/3A-DAY/07. https://disc.gsfc.nasa.gov/datacollection/GPM_3GPROFF17SSMIS_DAY_CLIM_07.html. Digital Science Data.",
-            "issued": "2022-05-09",
-            "temporal": "2008-03-19T00:00:00Z/2023-02-28T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-05-01",
-            "keyword": [
-                "atmosphere",
-                "atmospheric water vapor",
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
-            "identifier": "C2264135388-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "Version 07 is the current version of the data set. Older versions will no longer be available and have been superseded by Version 07. \n\nThe \"CLIM\"  products differ from their \"regular\" counterparts (without the \"CLIM\" in the name) by the ancillary data they use. They are Climate-Reference products, which requires homogeneous ancillary data over the climate time series.  Hence, the ECMWF-Interim (European Centre for Medium-Range Weather Forecasts, 2-3 months lag behind the regular production) reanalysis is used as ancillary data to derive surface and atmospheric conditions required by the GPROF algorithm for the \"CLIM\" output. The GPROF databases are also adjusted accordingly for these climate-referenced retrievals.\n\n3GPROF products provide global gridded monthly/daily precipitation averages from multiple satellites that can be used for climate studies. The 3GPROF products are based on retrievals from high-quality microwave sensors, which are sensitive to liquid and ice-phase precipitation hydrometeors in the atmosphere.",
-            "release-place": "Greenbelt, MD",
-            "series-name": "GPM_3GPROFF17SSMIS_DAY_CLIM",
-            "creator": "GPM Science Team",
-            "title": "GPM SSMIS on F17 (GPROF) Climate-based Radiometer Precipitation Profiling L3 1 day 0.25 degree x 0.25 degree V07 (GPM_3GPROFF17SSMIS_DAY_CLIM) at GES DISC",
-            "graphic-preview-description": "Surface Precipitation from GPM SSMIS on F17 GPROF (25 km x 25 km) (GPM_3GPROFF17SSMIS_DAY_CLIM)",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/GPM/browse/GPM_3GPROFF17SSMIS_DAY_CLIM_07.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGPM%2FSSMIS%2FF17%2FGPROFCLIM%2F3A-DAY%2F07",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGPM%2FSSMIS%2FF17%2FGPROFCLIM%2F3A-DAY%2F07",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/GPM/browse/GPM_3GPROFF17SSMIS_DAY_CLIM_07.png",
-                    "description": "Surface Precipitation from GPM SSMIS on F17 GPROF (25 km x 25 km) (GPM_3GPROFF17SSMIS_DAY_CLIM)",
                     "@type": "dcat:Distribution",
+                    "description": "Surface Precipitation from GPM SSMIS on F17 GPROF (25 km x 25 km) (GPM_3GPROFF17SSMIS_DAY_CLIM)",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/GPM/browse/GPM_3GPROFF17SSMIS_DAY_CLIM_07.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/GPM_3GPROFF17SSMIS_DAY_CLIM_07.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/GPM_3GPROFF17SSMIS_DAY_CLIM_07.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://gpm1.gesdisc.eosdis.nasa.gov/data/GPM_L3/GPM_3GPROFF17SSMIS_DAY_CLIM.07/",
-                    "description": "Access the data via HTTPS",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS",
+                    "downloadURL": "https://gpm1.gesdisc.eosdis.nasa.gov/data/GPM_L3/GPM_3GPROFF17SSMIS_DAY_CLIM.07/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://gpm1.gesdisc.eosdis.nasa.gov/opendap/GPM_L3/GPM_3GPROFF17SSMIS_DAY_CLIM.07/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://gpm1.gesdisc.eosdis.nasa.gov/opendap/GPM_L3/GPM_3GPROFF17SSMIS_DAY_CLIM.07/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://gpm1.gesdisc.eosdis.nasa.gov/dods/GPM_3GPROFF17SSMIS_DAY_CLIM_07.info",
-                    "description": "The GrADS Data Server (GDS) is another form of OPeNDAP that provides subsetting and some analysis services across the Internet.",
                     "@type": "dcat:Distribution",
+                    "description": "The GrADS Data Server (GDS) is another form of OPeNDAP that provides subsetting and some analysis services across the Internet.",
+                    "downloadURL": "https://gpm1.gesdisc.eosdis.nasa.gov/dods/GPM_3GPROFF17SSMIS_DAY_CLIM_07.info",
+                    "mediaType": "text/html",
                     "title": "Use GRADS DATA SERVER (GDS) to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=GPM_3GPROFF17SSMIS_DAY_CLIM_07",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=GPM_3GPROFF17SSMIS_DAY_CLIM_07",
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
@@ -695153,611 +695129,649 @@
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
+            "graphic-preview-description": "Surface Precipitation from GPM SSMIS on F17 GPROF (25 km x 25 km) (GPM_3GPROFF17SSMIS_DAY_CLIM)",
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/GPM/browse/GPM_3GPROFF17SSMIS_DAY_CLIM_07.png",
+            "identifier": "C2264135388-GES_DISC",
+            "issued": "2022-05-09",
+            "keyword": [
+                "atmosphere",
+                "atmospheric water vapor",
+                "earth science",
+                "precipitation"
+            ],
+            "landingPage": "https://doi.org/10.5067/GPM/SSMIS/F17/GPROFCLIM/3A-DAY/07",
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
+            "series-name": "GPM_3GPROFF17SSMIS_DAY_CLIM",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2008-03-19T00:00:00Z/2023-02-28T00:00:00Z",
             "theme": [
                 "GPM",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "GPM SSMIS on F17 (GPROF) Climate-based Radiometer Precipitation Profiling L3 1 day 0.25 degree x 0.25 degree V07 (GPM_3GPROFF17SSMIS_DAY_CLIM) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/TEMSC-3JC634",
             "citation": "D. N. Wiese, D.-N. Yuan, C. Boening, F. W. Landerer, M. M. Watkins. 2023-01-25. JPL Mascon Ocean, Ice, and Hydrology Equivalent Water Height Coastal Resolution Improvement (CRI) Filtered. Version RL06.3Mv04. JPL GRACE and GRACE-FO Mascon Ocean, Ice, and Hydrology Equivalent Water Height CRI Filtered RL06.3Mv04. PO.DAAC. Archived by National Aeronautics and Space Administration, U.S. Government, PO.DAAC. https://doi.org/10.5067/TEMSC-3JC634. http://grace.jpl.nasa.gov/data/get-data/jpl_global_mascons/. D. N. Wiese, D.-N. Yuan, C. Boening, F. W. Landerer, M. M. Watkins, TELLUS, 2019-11-26, JPL GRACE and GRACE-FO Mascon Ocean, Ice, and Hydrology Equivalent Water Height Coastal Resolution Improvement (CRI) Filtered Release 06 Version 02, http://grace.jpl.nasa.gov/data/get-data/jpl_global_mascons/.",
-            "issued": "2019-10-24",
-            "temporal": "2002-04-04T00:00:00Z/2024-09-16T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2019-10-24",
-            "references": [
-                "https://doi.org/10.1002/2014JB011547",
-                "https://doi.org/10.1002/2016WR019344"
-            ],
-            "keyword": [
-                "terrestrial hydrosphere",
-                "water budget",
-                "cryosphere",
-                "glaciers/ice sheets",
-                "earth science",
-                "ground water"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Wen-Hao Li",
                 "hasEmail": "mailto:wen-hao.li@jpl.nasa.gov"
             },
-            "identifier": "C3195527175-POCLOUD",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/JPL/PODAAC"
-            },
-            "description": "This dataset contains gridded monthly global water storage/height anomalies relative to a time-mean, derived from GRACE and GRACE-FO and processed at JPL using the Mascon approach (RL06.3Mv04). A Coastal Resolution Improvement (CRI) filter has been applied to this data set to reduce signal leakage errors across coastlines. For most land hydrology, oceanographic as well as land-ice applications this is the recommend data set for the analysis of surface mass changes. The data are provided in a single data file in netCDF format, with water storage/height anomalies in equivalent water thickness units (cm). The data are derived from solving for monthly gravity field variations on geolocated spherical cap mass concentration functions, rather than global spherical harmonic coefficients. Additionally, realistic geophysical information is introduced during the computation to intrinsically remove correlated errors. Thus, these Mascon grids do not need to be de-correlated or smoothed, like traditional spherical harmonic gravity solutions.\n<br><br> \nThe complete Mascon solution consists of 4,551 independent estimates of surface mass change that have been derived using an equal-area 3-degree grid of individual mascons. A subset of these individual mascons span coastlines, and contain mixed land and ocean mass change signals. In a post-processing step, the CRI filter is applied to those mixed land/ocean Mascons to separate land and ocean mass. The land mask used to perform this separation is provided in the same directory as this dataset, as are uncertainty values, and the gridded mascon-ID number to enable further analysis. Since the individual mascons act as an inherent smoother on the gravity field, a set of optional gain factors (for continental hydrology applications) that can be applied to the solution to study mass change signals at sub-mascon resolution is also provided within the same data directory as the Mascon data. For use-case examples and further background on the gain factors, please see Wiese, Landerer & Watkins, 2016, https://doi.org/10.1002/2016WR019344.\n<br><br>\nThis RL06.3Mv04 is an updated version of the previous Tellus JPL Mascon RL06.1Mv03 (DOI, 10.5067/TEMSC-3JC63). For a detailed description on the Mascon solution, including the mathematical derivation, implementation of geophysical constraints, and solution validation, please see Watkins et al., 2015, doi: 10.1002/2014JB011547. For a detailed description of the CRI filter implementation, please see Wiese et al., 2016, doi:10.1002/2016WR019344.",
-            "release-place": "PO.DAAC",
-            "series-name": "JPL Mascon Ocean, Ice, and Hydrology Equivalent Water Height Coastal Resolution Improvement (CRI) Filtered",
             "creator": "D. N. Wiese, D.-N. Yuan, C. Boening, F. W. Landerer, M. M. Watkins",
-            "title": "JPL GRACE and GRACE-FO Mascon Ocean, Ice, and Hydrology Equivalent Water Height Coastal Resolution Improvement (CRI) Filtered Release 06.3 Version 04",
-            "graphic-preview-description": "SOTO (State Of The Ocean) Visualization (total water storage anomaly)",
-            "graphic-preview-file": "https://soto.podaac.earthdatacloud.nasa.gov/?l=GRACE_Tellus_Liquid_Water_Equivalent_Thickness_Mascon_CRI,BlueMarble_ShadedRelief_Bathymetry,Coastlines_15m",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "This dataset contains gridded monthly global water storage/height anomalies relative to a time-mean, derived from GRACE and GRACE-FO and processed at JPL using the Mascon approach (RL06.3Mv04). A Coastal Resolution Improvement (CRI) filter has been applied to this data set to reduce signal leakage errors across coastlines. For most land hydrology, oceanographic as well as land-ice applications this is the recommend data set for the analysis of surface mass changes. The data are provided in a single data file in netCDF format, with water storage/height anomalies in equivalent water thickness units (cm). The data are derived from solving for monthly gravity field variations on geolocated spherical cap mass concentration functions, rather than global spherical harmonic coefficients. Additionally, realistic geophysical information is introduced during the computation to intrinsically remove correlated errors. Thus, these Mascon grids do not need to be de-correlated or smoothed, like traditional spherical harmonic gravity solutions.\n<br><br> \nThe complete Mascon solution consists of 4,551 independent estimates of surface mass change that have been derived using an equal-area 3-degree grid of individual mascons. A subset of these individual mascons span coastlines, and contain mixed land and ocean mass change signals. In a post-processing step, the CRI filter is applied to those mixed land/ocean Mascons to separate land and ocean mass. The land mask used to perform this separation is provided in the same directory as this dataset, as are uncertainty values, and the gridded mascon-ID number to enable further analysis. Since the individual mascons act as an inherent smoother on the gravity field, a set of optional gain factors (for continental hydrology applications) that can be applied to the solution to study mass change signals at sub-mascon resolution is also provided within the same data directory as the Mascon data. For use-case examples and further background on the gain factors, please see Wiese, Landerer & Watkins, 2016, https://doi.org/10.1002/2016WR019344.\n<br><br>\nThis RL06.3Mv04 is an updated version of the previous Tellus JPL Mascon RL06.1Mv03 (DOI, 10.5067/TEMSC-3JC63). For a detailed description on the Mascon solution, including the mathematical derivation, implementation of geophysical constraints, and solution validation, please see Watkins et al., 2015, doi: 10.1002/2014JB011547. For a detailed description of the CRI filter implementation, please see Wiese et al., 2016, doi:10.1002/2016WR019344.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FTEMSC-3JC634",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FTEMSC-3JC634",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/tellus/open/L3/docs/GRACE_GRACE-FO_ReleaseNotes_JPL_MASCON.pdf",
-                    "description": "Release Note",
                     "@type": "dcat:Distribution",
+                    "description": "Release Note",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/tellus/open/L3/docs/GRACE_GRACE-FO_ReleaseNotes_JPL_MASCON.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://grace.jpl.nasa.gov/data/get-data/jpl_global_mascons/",
-                    "description": "Provides additional resources and information for the Global Mascon datasets.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides additional resources and information for the Global Mascon datasets.",
+                    "downloadURL": "https://grace.jpl.nasa.gov/data/get-data/jpl_global_mascons/",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://podaac.jpl.nasa.gov/GRACE-FO",
-                    "description": "PODAAC GRACE-FO Project-Page",
                     "@type": "dcat:Distribution",
+                    "description": "PODAAC GRACE-FO Project-Page",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/GRACE-FO",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://podaac.jpl.nasa.gov/GRACE",
-                    "description": "GRACE-FO Project Website (external to PO.DAAC)",
                     "@type": "dcat:Distribution",
+                    "description": "GRACE-FO Project Website (external to PO.DAAC)",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/GRACE",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://grace.jpl.nasa.gov/about/faq/",
-                    "description": "GRACE Tellus Project page for Frequently Asked Questions.",
                     "@type": "dcat:Distribution",
+                    "description": "GRACE Tellus Project page for Frequently Asked Questions.",
+                    "downloadURL": "https://grace.jpl.nasa.gov/about/faq/",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://grace.jpl.nasa.gov/data/data-updates/",
-                    "description": "Grace Tellus Project site for announcing recent and historical updates regarding Tellus datasets.",
                     "@type": "dcat:Distribution",
+                    "description": "Grace Tellus Project site for announcing recent and historical updates regarding Tellus datasets.",
+                    "downloadURL": "https://grace.jpl.nasa.gov/data/data-updates/",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://github.com/podaac/GRACE",
-                    "description": "Python script of converting netCDF4 to GeoTIFF",
                     "@type": "dcat:Distribution",
+                    "description": "Python script of converting netCDF4 to GeoTIFF",
+                    "downloadURL": "https://github.com/podaac/GRACE",
+                    "mediaType": "text/html",
                     "title": "View this dataset's data recipes"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/TELLUS_GRAC-GRFO_MASCON_CRI_GRID_RL06.3_V4.jpg",
-                    "description": "Thumbnail",
                     "@type": "dcat:Distribution",
+                    "description": "Thumbnail",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/TELLUS_GRAC-GRFO_MASCON_CRI_GRID_RL06.3_V4.jpg",
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
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C3195527175-POCLOUD",
-                    "description": "HTTPS endpoint for data browse and download",
                     "@type": "dcat:Distribution",
+                    "description": "HTTPS endpoint for data browse and download",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C3195527175-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C3195527175-POCLOUD",
-                    "description": "Browse granule search results in Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse granule search results in Earthdata Search",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C3195527175-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://soto.podaac.earthdatacloud.nasa.gov/?l=GRACE_Tellus_Liquid_Water_Equivalent_Thickness_Mascon_CRI%2CBlueMarble_ShadedRelief_Bathymetry%2CCoastlines_15m",
-                    "description": "SOTO (State Of The Ocean) Visualization (total water storage anomaly)",
                     "@type": "dcat:Distribution",
+                    "description": "SOTO (State Of The Ocean) Visualization (total water storage anomaly)",
+                    "downloadURL": "https://soto.podaac.earthdatacloud.nasa.gov/?l=GRACE_Tellus_Liquid_Water_Equivalent_Thickness_Mascon_CRI%2CBlueMarble_ShadedRelief_Bathymetry%2CCoastlines_15m",
+                    "mediaType": "text/html",
                     "title": "Get a related map visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://podaac.jpl.nasa.gov/gravity/grace-documentation",
-                    "description": "Page that includes all GRACE-FO Documentation and Technical Notes",
                     "@type": "dcat:Distribution",
+                    "description": "Page that includes all GRACE-FO Documentation and Technical Notes",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/gravity/grace-documentation",
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
+            "graphic-preview-description": "SOTO (State Of The Ocean) Visualization (total water storage anomaly)",
+            "graphic-preview-file": "https://soto.podaac.earthdatacloud.nasa.gov/?l=GRACE_Tellus_Liquid_Water_Equivalent_Thickness_Mascon_CRI,BlueMarble_ShadedRelief_Bathymetry,Coastlines_15m",
+            "identifier": "C3195527175-POCLOUD",
+            "issued": "2019-10-24",
+            "keyword": [
+                "terrestrial hydrosphere",
+                "water budget",
+                "cryosphere",
+                "glaciers/ice sheets",
+                "earth science",
+                "ground water"
+            ],
+            "landingPage": "https://doi.org/10.5067/TEMSC-3JC634",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2019-10-24",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/JPL/PODAAC"
+            },
+            "references": [
+                "https://doi.org/10.1002/2014JB011547",
+                "https://doi.org/10.1002/2016WR019344"
+            ],
+            "release-place": "PO.DAAC",
+            "series-name": "JPL Mascon Ocean, Ice, and Hydrology Equivalent Water Height Coastal Resolution Improvement (CRI) Filtered",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2002-04-04T00:00:00Z/2024-09-16T00:00:00Z",
             "theme": [
                 "GRACE",
                 "GRACE-FO",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "JPL GRACE and GRACE-FO Mascon Ocean, Ice, and Hydrology Equivalent Water Height Coastal Resolution Improvement (CRI) Filtered Release 06.3 Version 04"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1798",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Miles, N.L., S.J. Richardson, D.K. Martins, K.J. Davis, and B.J. Haupt. 2020. ACT-America: L1 Raw, Uncalibrated In-Situ CO2, CO, and CH4 Mole Fractions from Towers. ORNL DAAC, Oak Ridge, Tennessee, USA. https://doi.org/10.3334/ORNLDAAC/1798",
-            "issued": "2020-10-30",
-            "temporal": "2015-01-01T00:00:00Z/2019-12-31T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-06-12",
-            "keyword": [
-                "atmosphere",
-                "atmospheric chemistry",
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
-            "identifier": "C2706327711-ORNL_CLOUD",
             "description": "This dataset provides Level 1 (L1) in situ atmospheric carbon dioxide (CO2), carbon monoxide (CO), and methane (CH4) concentrations as measured on a network of instrumented communications towers across the central and eastern USA operated by the Atmospheric Carbon and Transport-America (ACT-America) project. There were 11 towers instrumented with cavity ring-down spectrometers (CRDS; Picarro Inc.) with measurements beginning in January 2015 and continuing to October 2019. The measurement period varied by tower site. The Picarro analyzers continuously measured total CH4, isotopic ratio of CH4, CO2, CO, and other greenhouse gas concentrations. Not all species were measured at all sites. Complete tower location, elevation, instrument height, and date/time information are also provided. Determination of greenhouse gas fluxes and uncertainty bounds is essential for the evaluation of the effectiveness of mitigation strategies. These L1 data are raw instrument outputs from the Picarro instruments. A Level 2 (L2) product derived from this L1 data is available and generally would be the preferred data for most use cases.",
-            "graphic-preview-description": "The communication tower at the Wessington, South Dakota site. This site was instrumented from January of 2017 to September of 2019.",
-            "title": "ACT-America: L1 Raw, Uncalibrated In-Situ CO2, CO, and CH4 Mole Fractions from Towers",
-            "graphic-preview-file": "https://daac.ornl.gov/ACTAMERICA/guides/Insitu_Tower_Greenhouse_Gas_Fig1.jpg",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1798",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1798",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/actamerica/Insitu_Tower_Greenhouse_Gas/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/actamerica/Insitu_Tower_Greenhouse_Gas/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/ACTAMERICA/guides/Insitu_Tower_Greenhouse_Gas.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/ACTAMERICA/guides/Insitu_Tower_Greenhouse_Gas.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1798",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1798",
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
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/actamerica/Insitu_Tower_Greenhouse_Gas/comp/ACT_GCI_Install_Decommission_dates.xlsx",
-                    "description": "ACT-America: L1 Raw, Uncalibrated In-Situ CO2, CO, and CH4 Mole Fractions from Towers: ACT_GCI_Install_Decommission_dates.xlsx",
                     "@type": "dcat:Distribution",
+                    "description": "ACT-America: L1 Raw, Uncalibrated In-Situ CO2, CO, and CH4 Mole Fractions from Towers: ACT_GCI_Install_Decommission_dates.xlsx",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/actamerica/Insitu_Tower_Greenhouse_Gas/comp/ACT_GCI_Install_Decommission_dates.xlsx",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/actamerica/Insitu_Tower_Greenhouse_Gas/comp/datasheet-g2301-crds-analyzer-co2-ch4-h2o-air-oct15.pdf",
-                    "description": "ACT-America: L1 Raw, Uncalibrated In-Situ CO2, CO, and CH4 Mole Fractions from Towers: datasheet-g2301-crds-analyzer-co2-ch4-h2o-air-oct15.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "ACT-America: L1 Raw, Uncalibrated In-Situ CO2, CO, and CH4 Mole Fractions from Towers: datasheet-g2301-crds-analyzer-co2-ch4-h2o-air-oct15.pdf",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/actamerica/Insitu_Tower_Greenhouse_Gas/comp/datasheet-g2301-crds-analyzer-co2-ch4-h2o-air-oct15.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/actamerica/Insitu_Tower_Greenhouse_Gas/comp/G2301-m+Manual+rev+2-11-11.pdf",
-                    "description": "ACT-America: L1 Raw, Uncalibrated In-Situ CO2, CO, and CH4 Mole Fractions from Towers: G2301-m+Manual+rev+2-11-11.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "ACT-America: L1 Raw, Uncalibrated In-Situ CO2, CO, and CH4 Mole Fractions from Towers: G2301-m+Manual+rev+2-11-11.pdf",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/actamerica/Insitu_Tower_Greenhouse_Gas/comp/G2301-m+Manual+rev+2-11-11.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/actamerica/Insitu_Tower_Greenhouse_Gas/comp/Insitu_Tower_Greenhouse_Gas.pdf",
-                    "description": "ACT-America: L1 Raw, Uncalibrated In-Situ CO2, CO, and CH4 Mole Fractions from Towers: Insitu_Tower_Greenhouse_Gas.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "ACT-America: L1 Raw, Uncalibrated In-Situ CO2, CO, and CH4 Mole Fractions from Towers: Insitu_Tower_Greenhouse_Gas.pdf",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/actamerica/Insitu_Tower_Greenhouse_Gas/comp/Insitu_Tower_Greenhouse_Gas.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/actamerica/Insitu_Tower_Greenhouse_Gas/comp/Tank_log_raw_data.xlsx",
-                    "description": "ACT-America: L1 Raw, Uncalibrated In-Situ CO2, CO, and CH4 Mole Fractions from Towers: Tank_log_raw_data.xlsx",
                     "@type": "dcat:Distribution",
+                    "description": "ACT-America: L1 Raw, Uncalibrated In-Situ CO2, CO, and CH4 Mole Fractions from Towers: Tank_log_raw_data.xlsx",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/actamerica/Insitu_Tower_Greenhouse_Gas/comp/Tank_log_raw_data.xlsx",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://daac.ornl.gov/ACTAMERICA/guides/Insitu_Tower_Greenhouse_Gas_Fig1.jpg",
-                    "description": "The communication tower at the Wessington, South Dakota site. This site was instrumented from January of 2017 to September of 2019.",
                     "@type": "dcat:Distribution",
+                    "description": "The communication tower at the Wessington, South Dakota site. This site was instrumented from January of 2017 to September of 2019.",
+                    "downloadURL": "https://daac.ornl.gov/ACTAMERICA/guides/Insitu_Tower_Greenhouse_Gas_Fig1.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://actamerica.ornl.gov",
-                    "description": "ACT-America Campaign Site",
                     "@type": "dcat:Distribution",
+                    "description": "ACT-America Campaign Site",
+                    "downloadURL": "https://actamerica.ornl.gov",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 }
             ],
+            "graphic-preview-description": "The communication tower at the Wessington, South Dakota site. This site was instrumented from January of 2017 to September of 2019.",
+            "graphic-preview-file": "https://daac.ornl.gov/ACTAMERICA/guides/Insitu_Tower_Greenhouse_Gas_Fig1.jpg",
+            "identifier": "C2706327711-ORNL_CLOUD",
+            "issued": "2020-10-30",
+            "keyword": [
+                "atmosphere",
+                "atmospheric chemistry",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1798",
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
             "spatial": "-98.59 30.2 -76.42 44.05",
+            "temporal": "2015-01-01T00:00:00Z/2019-12-31T23:59:59Z",
             "theme": [
                 "ACT-America",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "ACT-America: L1 Raw, Uncalibrated In-Situ CO2, CO, and CH4 Mole Fractions from Towers"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1640",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "van de Kerk, M., D. Verbyla, A.W. Nolin, K.J. Sivy, and L.R. Prugh. 2018. ABoVE: Dall Sheep Lamb Recruitment and Climate Data, Alaska and NW Canada, 2000-2015. ORNL DAAC, Oak Ridge, Tennessee, USA. https://doi.org/10.3334/ORNLDAAC/1640",
-            "issued": "2022-11-28",
-            "temporal": "2000-01-01T00:00:00Z/2015-12-31T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-06-12",
-            "keyword": [
-                "atmospheric temperature",
-                "animals/vertebrates",
-                "atmosphere",
-                "biological classification",
-                "biosphere",
-                "biospheric indicators",
-                "climate indicators",
-                "earth science",
-                "ecological dynamics",
-                "national geospatial data asset",
-                "ngda",
-                "precipitation",
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
-            "identifier": "C2162145802-ORNL_CLOUD",
             "description": "This dataset contains estimated annual average Dall sheep (Ovis dalli dalli) lamb-to-ewe ratios for each year from 2000-2015 across the full species range in Alaska and Northwestern Canada. Sheep population data are from surveys conducted over the 14 major mountain ranges encompassing the range of Dall sheep. For this study, the mountain ranges were divided into 24 mountain units due to differing climate gradients. Estimated covariate environmental and climate data used to examine the relationship between environmental conditions and Dall sheep population performance (per mountain unit) are also provided and include precipitation, temperature, snow cover, elevation, and distance to the center of the range.",
-            "graphic-preview-description": "A herd of Dall sheep ewes and lambs are dwarfed by the mountainous landscape in Wrangell St. Elias National Park, Alaska, March 2017. Photo credit: Laura Prugh.",
-            "title": "ABoVE: Dall Sheep Lamb Recruitment and Climate Data, Alaska and NW Canada, 2000-2015",
-            "graphic-preview-file": "https://daac.ornl.gov/ABOVE/guides/Dall_Sheep_Population_Dynamics_Fig1.jpg",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1640",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1640",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/above/Dall_Sheep_Population_Dynamics/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/above/Dall_Sheep_Population_Dynamics/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/ABOVE/guides/Dall_Sheep_Population_Dynamics.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/ABOVE/guides/Dall_Sheep_Population_Dynamics.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1640",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1640",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/Dall_Sheep_Population_Dynamics/comp/Dall_Sheep_Population_Dynamics.pdf",
-                    "description": "ABoVE: Range-wide Dall Sheep Lamb-to-Ewe Ratios, Environment and Climate, 2000-2015: Dall_Sheep_Population_Dynamics.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "ABoVE: Range-wide Dall Sheep Lamb-to-Ewe Ratios, Environment and Climate, 2000-2015: Dall_Sheep_Population_Dynamics.pdf",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/Dall_Sheep_Population_Dynamics/comp/Dall_Sheep_Population_Dynamics.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/vnd.google-earth.kmz",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/Dall_Sheep_Population_Dynamics/comp/mountainunits.kmz",
-                    "description": "ABoVE: Range-wide Dall Sheep Lamb-to-Ewe Ratios, Environment and Climate, 2000-2015: mountainunits.kmz",
                     "@type": "dcat:Distribution",
+                    "description": "ABoVE: Range-wide Dall Sheep Lamb-to-Ewe Ratios, Environment and Climate, 2000-2015: mountainunits.kmz",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/Dall_Sheep_Population_Dynamics/comp/mountainunits.kmz",
+                    "mediaType": "application/vnd.google-earth.kmz",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://daac.ornl.gov/ABOVE/guides/Dall_Sheep_Population_Dynamics_Fig1.jpg",
-                    "description": "A herd of Dall sheep ewes and lambs are dwarfed by the mountainous landscape in Wrangell St. Elias National Park, Alaska, March 2017. Photo credit: Laura Prugh.",
                     "@type": "dcat:Distribution",
+                    "description": "A herd of Dall sheep ewes and lambs are dwarfed by the mountainous landscape in Wrangell St. Elias National Park, Alaska, March 2017. Photo credit: Laura Prugh.",
+                    "downloadURL": "https://daac.ornl.gov/ABOVE/guides/Dall_Sheep_Population_Dynamics_Fig1.jpg",
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
+            "graphic-preview-description": "A herd of Dall sheep ewes and lambs are dwarfed by the mountainous landscape in Wrangell St. Elias National Park, Alaska, March 2017. Photo credit: Laura Prugh.",
+            "graphic-preview-file": "https://daac.ornl.gov/ABOVE/guides/Dall_Sheep_Population_Dynamics_Fig1.jpg",
+            "identifier": "C2162145802-ORNL_CLOUD",
+            "issued": "2022-11-28",
+            "keyword": [
+                "atmospheric temperature",
+                "animals/vertebrates",
+                "atmosphere",
+                "biological classification",
+                "biosphere",
+                "biospheric indicators",
+                "climate indicators",
+                "earth science",
+                "ecological dynamics",
+                "national geospatial data asset",
+                "ngda",
+                "precipitation",
+                "snow/ice",
+                "terrestrial hydrosphere"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1640",
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
             "spatial": "-163.28 59.6 -123.55 69.71",
+            "temporal": "2000-01-01T00:00:00Z/2015-12-31T23:59:59Z",
             "theme": [
                 "ABoVE",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "ABoVE: Dall Sheep Lamb Recruitment and Climate Data, Alaska and NW Canada, 2000-2015"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC1-0483-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 1 phase 2014-11-20 to 2015-03-10. It is a Global Gravity measurement at the comet 67P and covers the time 2014-12-11T04:10:05.000 to 2014-12-11T12:41:36.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc1-0483-v1.0_ebr3-7rvw",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC1-0483-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc1-0483-v1.0_ebr3-7rvw",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 1 phase 2014-11-20 to 2015-03-10. It is a Global Gravity measurement at the comet 67P and covers the time 2014-12-11T04:10:05.000 to 2014-12-11T12:41:36.000.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 1 0483 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 1 0483 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/VIIRS/VNP43D46.001",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Crystal Schaaf, Zhuosen Wang, Xiaoyang Zhang, Alan Strahler\r\n. 2019-11-07. VNP43D46. Version 001. VIIRS/NPP BRDF/Albedo Valid Observation Band M5 Daily L3 Global 30ArcSec CMG V001\r\n. Sioux Falls, South Dakota, USA. Archived by National Aeronautics and Space Administration, U.S. Government, NASA EOSDIS Land Processes Distributed Active Archive Center. https://doi.org/10.5067/VIIRS/VNP43D46.001. https://doi.org/10.5067/VIIRS/VNP43D46.001. Digital Science Data. The DOI landing page provides citations in APA and Chicago styles.\r\n.",
-            "issued": "2019-11-07",
-            "temporal": "2012-01-19T00:00:00Z/2024-05-20T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2019-11-07",
-            "keyword": [
-                "land surface",
-                "earth science",
-                "surface radiative properties"
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
-            "identifier": "C1607332049-LPDAAC_ECS",
-            "description": "The NASA/NOAA Suomi National Polar-orbiting Partnership (Suomi NPP) Visible Infrared Imaging Radiometer Suite (VIIRS) Bidirectional Reflectance Distribution Function (BRDF) and Albedo Valid Observation Band M5 product (VNP43D46) is produced daily using 16 days of data at 30 arc second (1,000 meter) resolution. Data are temporally weighted to the ninth day, which is reflected in the file name. The VNP43D product suite is provided in a Climate Modeling Grid (CMG), which covers the entire globe for use in climate simulation models. Due to the large file size, each VNP43D product contains just one data layer for each of the parameters included in the VNP43MA2 (https://doi.org/10.5067/VIIRS/VNP43MA2.001) product. VNP43D40 through VNP43D53 are the 30 arc second BRDF/Albedo Quality values, the Local Solar Noon values, the Valid Observations of the moderate resolution bands (M1 through M5, M7, M8, M10, and M11) plus the Day/Night Band (DNB), the Snow Status, and the Uncertainty. Details regarding methodology are available on the[VNP43MA2 product page and in the Algorithm Theoretical Basis Document (ATBD). \r\n\r\nVNP43D46 contains the valid observation quality layer representing each of the 16 days of the retrieval period for VIIRS band M5.",
-            "release-place": "Sioux Falls, South Dakota, USA",
-            "series-name": "VNP43D46",
             "creator": "Crystal Schaaf, Zhuosen Wang, Xiaoyang Zhang, Alan Strahler",
-            "title": "VIIRS/NPP BRDF/Albedo Valid Observation Band M5 Daily L3 Global 30ArcSec CMG V001",
-            "programCode": [
-                "026:001"
-            ],
+            "data-presentation-form": "Digital Science Data",
+            "description": "The NASA/NOAA Suomi National Polar-orbiting Partnership (Suomi NPP) Visible Infrared Imaging Radiometer Suite (VIIRS) Bidirectional Reflectance Distribution Function (BRDF) and Albedo Valid Observation Band M5 product (VNP43D46) is produced daily using 16 days of data at 30 arc second (1,000 meter) resolution. Data are temporally weighted to the ninth day, which is reflected in the file name. The VNP43D product suite is provided in a Climate Modeling Grid (CMG), which covers the entire globe for use in climate simulation models. Due to the large file size, each VNP43D product contains just one data layer for each of the parameters included in the VNP43MA2 (https://doi.org/10.5067/VIIRS/VNP43MA2.001) product. VNP43D40 through VNP43D53 are the 30 arc second BRDF/Albedo Quality values, the Local Solar Noon values, the Valid Observations of the moderate resolution bands (M1 through M5, M7, M8, M10, and M11) plus the Day/Night Band (DNB), the Snow Status, and the Uncertainty. Details regarding methodology are available on the[VNP43MA2 product page and in the Algorithm Theoretical Basis Document (ATBD). \r\n\r\nVNP43D46 contains the valid observation quality layer representing each of the 16 days of the retrieval period for VIIRS band M5.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FVIIRS%2FVNP43D46.001",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FVIIRS%2FVNP43D46.001",
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
-                    "downloadURL": "https://doi.org/10.5067/VIIRS/VNP43D46.001",
-                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
+                    "downloadURL": "https://doi.org/10.5067/VIIRS/VNP43D46.001",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/xhdf5",
-                    "downloadURL": "https://e4ftl01.cr.usgs.gov/VIIRS/VNP43D46.001/",
-                    "description": "LP DAAC Data Pool provides direct access to available products via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "LP DAAC Data Pool provides direct access to available products via HTTPS.",
+                    "downloadURL": "https://e4ftl01.cr.usgs.gov/VIIRS/VNP43D46.001/",
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
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=C1607332049-LPDAAC_ECS",
-                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=C1607332049-LPDAAC_ECS",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://opendap.cr.usgs.gov/opendap/hyrax/VNP43D46.001/contents.html",
-                    "description": "Access data via Open-source Project for a Network Data Access Protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access data via Open-source Project for a Network Data Access Protocol.",
+                    "downloadURL": "https://opendap.cr.usgs.gov/opendap/hyrax/VNP43D46.001/contents.html",
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
-                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/filespec/VIIRS/1/VNP43D46",
-                    "description": "The File Specification provides a description of the product file including Scientific Data Sets and their attributes.",
                     "@type": "dcat:Distribution",
+                    "description": "The File Specification provides a description of the product file including Scientific Data Sets and their attributes.",
+                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/filespec/VIIRS/1/VNP43D46",
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
+            "identifier": "C1607332049-LPDAAC_ECS",
+            "issued": "2019-11-07",
+            "keyword": [
+                "land surface",
+                "earth science",
+                "surface radiative properties"
+            ],
+            "landingPage": "https://doi.org/10.5067/VIIRS/VNP43D46.001",
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
+            "series-name": "VNP43D46",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2012-01-19T00:00:00Z/2024-05-20T00:00:00Z",
             "theme": [
                 "NPP-JPSS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "VIIRS/NPP BRDF/Albedo Valid Observation Band M5 Daily L3 Global 30ArcSec CMG V001"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.nasa.gov/d/ebsb-mf4m",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "GeneLab Outreach",
+                "hasEmail": "mailto:genelab-outreach@lists.nasa.gov"
+            },
+            "description": "We investigated differentially regulated and stably expressed genes in human Jurkat T lymphocytic cells in 5min simulated microgravity and hypergravity and compared expression profiles to identify gravity-regulated and unaffected genes as well as adaptation processes. This dataset is part of a series of three and the other two datasets are deposited in GLDS-172 and GLDS-188.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "GeneLab Study Page",
+                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-189",
+                    "mediaType": "text/html",
+                    "title": "Gene expression response to simulated gravity and hypergravity in human T cells"
+                }
+            ],
+            "identifier": "nasa_genelab_GLDS-189_ebsb-mf4m",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
             "keyword": [
                 "labeling",
                 "hypergravity",
@@ -695769,200 +695783,164 @@
                 "scan protocol",
                 "normalization data transformation"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "GeneLab Outreach",
-                "hasEmail": "mailto:genelab-outreach@lists.nasa.gov"
-            },
+            "landingPage": "https://data.nasa.gov/d/ebsb-mf4m",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "nasa_genelab_GLDS-189_ebsb-mf4m",
-            "description": "We investigated differentially regulated and stably expressed genes in human Jurkat T lymphocytic cells in 5min simulated microgravity and hypergravity and compared expression profiles to identify gravity-regulated and unaffected genes as well as adaptation processes. This dataset is part of a series of three and the other two datasets are deposited in GLDS-172 and GLDS-188.",
-            "title": "Gene expression response to simulated gravity and hypergravity in human T cells",
-            "programCode": [
-                "026:005"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-189",
-                    "description": "GeneLab Study Page",
-                    "@type": "dcat:Distribution",
-                    "title": "Gene expression response to simulated gravity and hypergravity in human T cells"
-                }
-            ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "Gene expression response to simulated gravity and hypergravity in human T cells"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/VIIRS/VNP43D38.001",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Crystal Schaaf, Zhuosen Wang, Xiaoyang Zhang, Alan Strahler\r\n. 2019-11-07. VNP43D38. Version 001. VIIRS/NPP BRDF/Albedo Parameter 2 DNB Daily L3 Global 30 ArcSec CMG V001\r\n. Sioux Falls, South Dakota, USA. Archived by National Aeronautics and Space Administration, U.S. Government, NASA EOSDIS Land Processes Distributed Active Archive Center. https://doi.org/10.5067/VIIRS/VNP43D38.001. https://doi.org/10.5067/VIIRS/VNP43D38.001. Digital Science Data. The DOI landing page provides citations in APA and Chicago styles.\r\n.",
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
-            "identifier": "C1607327867-LPDAAC_ECS",
-            "description": "The NASA/NOAA Suomi National Polar-orbiting Partnership (Suomi NPP) Visible Infrared Imaging Radiometer Suite (VIIRS) Bidirectional Reflectance Distribution Function (BRDF) and Albedo Model Parameter 2 Day/Night Band (DNB) product (VNP43D38) is produced daily using 16 days of data at 30 arc second (1,000 meter) resolution. Data are temporally weighted to the ninth day, which is reflected in the file name. The VNP43D product suite is provided in a Climate Modeling Grid (CMG), which covers the entire globe for use in climate simulation models. Due to the large file size, each VNP43D product contains just one data layer. Each of the three model parameters (isotropic, volumetric, and geometric) for each of the nine VIIRS moderate resolution bands along with the visible, near-infrared (NIR), and shortwave bands included in the VNP43MA1 (https://doi.org/10.5067/VIIRS/VNP43MA1.001) product is stored in a separate file as VNP43D01 through VNP43D36. In addition to the bands included in VNP43MA1, this product suite includes model parameters for the VIIRS Day/Night Band (DNB) as VNP43D37 through VNP43D39. Details regarding methodology are available on the VNP43MA1 product page and in the Algorithm Theoretical Basis Document (ATBD).\r\n\r\nVNP43D38 is the BRDF volumetric parameter for the VIIRS DNB (0.7 \u03bcm). The volumetric parameter, in conjunction with the isotropic and geometric parameters, is used to derive the BRDF/Albedo values for the VIIRS DNB.",
-            "release-place": "Sioux Falls, South Dakota, USA",
-            "series-name": "VNP43D38",
             "creator": "Crystal Schaaf, Zhuosen Wang, Xiaoyang Zhang, Alan Strahler",
-            "title": "VIIRS/NPP BRDF/Albedo Parameter 2 DNB Daily L3 Global 30 ArcSec CMG V001",
-            "programCode": [
-                "026:001"
-            ],
+            "data-presentation-form": "Digital Science Data",
+            "description": "The NASA/NOAA Suomi National Polar-orbiting Partnership (Suomi NPP) Visible Infrared Imaging Radiometer Suite (VIIRS) Bidirectional Reflectance Distribution Function (BRDF) and Albedo Model Parameter 2 Day/Night Band (DNB) product (VNP43D38) is produced daily using 16 days of data at 30 arc second (1,000 meter) resolution. Data are temporally weighted to the ninth day, which is reflected in the file name. The VNP43D product suite is provided in a Climate Modeling Grid (CMG), which covers the entire globe for use in climate simulation models. Due to the large file size, each VNP43D product contains just one data layer. Each of the three model parameters (isotropic, volumetric, and geometric) for each of the nine VIIRS moderate resolution bands along with the visible, near-infrared (NIR), and shortwave bands included in the VNP43MA1 (https://doi.org/10.5067/VIIRS/VNP43MA1.001) product is stored in a separate file as VNP43D01 through VNP43D36. In addition to the bands included in VNP43MA1, this product suite includes model parameters for the VIIRS Day/Night Band (DNB) as VNP43D37 through VNP43D39. Details regarding methodology are available on the VNP43MA1 product page and in the Algorithm Theoretical Basis Document (ATBD).\r\n\r\nVNP43D38 is the BRDF volumetric parameter for the VIIRS DNB (0.7 \u03bcm). The volumetric parameter, in conjunction with the isotropic and geometric parameters, is used to derive the BRDF/Albedo values for the VIIRS DNB.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FVIIRS%2FVNP43D38.001",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FVIIRS%2FVNP43D38.001",
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
-                    "downloadURL": "https://doi.org/10.5067/VIIRS/VNP43D38.001",
-                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
+                    "downloadURL": "https://doi.org/10.5067/VIIRS/VNP43D38.001",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/xhdf5",
-                    "downloadURL": "https://e4ftl01.cr.usgs.gov/VIIRS/VNP43D38.001/",
-                    "description": "LP DAAC Data Pool provides direct access to available products via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "LP DAAC Data Pool provides direct access to available products via HTTPS.",
+                    "downloadURL": "https://e4ftl01.cr.usgs.gov/VIIRS/VNP43D38.001/",
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
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=C1607327867-LPDAAC_ECS",
-                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=C1607327867-LPDAAC_ECS",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://opendap.cr.usgs.gov/opendap/hyrax/VNP43D38.001/contents.html",
-                    "description": "Access data via Open-source Project for a Network Data Access Protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access data via Open-source Project for a Network Data Access Protocol.",
+                    "downloadURL": "https://opendap.cr.usgs.gov/opendap/hyrax/VNP43D38.001/contents.html",
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
-                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/filespec/VIIRS/1/VNP43D38",
-                    "description": "The File Specification provides a description of the product file including Scientific Data Sets and their attributes.",
                     "@type": "dcat:Distribution",
+                    "description": "The File Specification provides a description of the product file including Scientific Data Sets and their attributes.",
+                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/filespec/VIIRS/1/VNP43D38",
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
+            "identifier": "C1607327867-LPDAAC_ECS",
+            "issued": "2019-11-07",
+            "keyword": [
+                "surface radiative properties",
+                "land surface",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/VIIRS/VNP43D38.001",
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
+            "series-name": "VNP43D38",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2012-01-19T00:00:00Z/2024-05-20T00:00:00Z",
             "theme": [
                 "NPP-JPSS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "VIIRS/NPP BRDF/Albedo Parameter 2 DNB Daily L3 Global 30 ArcSec CMG V001"
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
-                "cases",
-                "incompressible",
-                "models",
-                "flow",
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
-            "identifier": "NASA-844__27",
             "description": "This grouping contains the incompressible-flow cases from the 1980-81 Data Library.",
-            "title": "Collaborative Testing of Turbulence Models: Incompressible Flow Cases from 1980-81 Data Library",
-            "programCode": [
-                "026:023"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -695970,692 +695948,687 @@
                     "mediaType": "application/txt"
                 }
             ],
-            "accrualPeriodicity": "irregular",
+            "identifier": "NASA-844__27",
+            "issued": "2018-06-25",
+            "keyword": [
+                "cases",
+                "incompressible",
+                "models",
+                "flow",
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
-            "landingPage": "https://doi.org/10.5067/ASDC/SUBORBITAL/ARCTAS_AircraftRemoteSensing_P3B_CAR_Data_1",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2022-09-06. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/ASDC/SUBORBITAL/ARCTAS_AircraftRemoteSensing_P3B_CAR_Data_1.",
-            "issued": "2022-01-06",
-            "temporal": "2008-03-25T00:00:00Z/2008-07-13T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-09-06",
-            "keyword": [
-                "atmosphere",
-                "atmospheric radiation",
-                "earth science",
-                "clouds"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Charles Gatebe",
                 "hasEmail": "mailto:charles.k.gatebe@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/LARC/SD/ASDC"
-            },
-            "identifier": "C2449574114-LARC_ASDC",
             "description": "ARCTAS_AircraftRemoteSensing_P3B_CAR_Data contains remotely sensed data collected via the Cloud Absorption Radiometer (CAR) onboard the P-3B aircraft during the Arctic Research of the Composition of the Troposphere from Aircraft & Satellites (ARCTAS) mission. Data collection for this product is complete.\r\n\r\nThe Arctic is a critical region in understanding climate change. The responses of the Arctic to environmental perturbations such as warming, pollution, and emissions from forest fires in boreal Eurasia and North America include key processes such as the melting of ice sheets and permafrost, a decrease in snow albedo, and the deposition of halogen radical chemistry from sea salt aerosols to ice. ARCTAS was a field campaign that explored environmental processes related to the high degree of climate sensitivity in the Arctic. ARCTAS was part of NASA\u2019s contribution to the International Global Atmospheric Chemistry (IGAC) Polar Study using Aircraft, Remote Sensing, Surface Measurements, and Models of Climate, Chemistry, Aerosols, and Transport (POLARCAT) Experiment for the International Polar Year 2007-2008.\r\n\r\nARCTAS had four primary objectives. The first was to understand long-range transport of pollution to the Arctic. Pollution brought to the Arctic from northern mid-latitude continents has environmental consequences, such as modifying regional and global climate and affecting the ozone budget. Prior to ARCTAS, these pathways remained largely uncertain. The second objective was to understand the atmospheric composition and climate implications of boreal forest fires; the smoke emissions from which act as an atmospheric perturbation to the Arctic by impacting the radiation budget and cloud processes and contributing to the production of tropospheric ozone. The third objective was to understand aerosol radiative forcing from climate perturbations, as the Arctic is an important place for understanding radiative forcing due to the rapid pace of climate change in the region and its unique radiative environment. The fourth objective of ARCTAS was to understand chemical processes with a focus on ozone, aerosols, mercury, and halogens. Additionally, ARCTAS sought to develop capabilities for incorporating data from aircraft and satellites related to pollution and related environmental perturbations in the Arctic into earth science models, expanding the potential for those models to predict future environmental change.\r\n\r\nARCTAS consisted of two, three-week aircraft deployments conducted in April and July 2008. The spring deployment sought to explore arctic haze, stratosphere-troposphere exchange, and sunrise photochemistry. April was chosen for the deployment phase due to historically being the peak in the seasonal accumulation of pollution from northern mid-latitude continents in the Arctic. The summer deployment sought to understand boreal forest fires at their most active seasonal phase in addition to stratosphere-troposphere exchange and summertime photochemistry.\r\n\r\nDuring ARCTAS, three NASA aircrafts, the DC-8, P-3B, and BE-200, conducted measurements and were equipped with suites of in-situ and remote sensing instrumentation. Airborne data was used in conjunction with satellite observations from AURA, AQUA, CloudSat, PARASOL, CALIPSO, and MISR.\r\n\r\nThe ASDC houses ARCTAS aircraft data, along with data related to MISR, a satellite instrument aboard the Terra satellite which provides measurements that provide information about the Earth\u2019s environment and climate.",
-            "title": "ARCTAS P-3B Aircraft CAR Data",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC%2FSUBORBITAL%2FARCTAS_AircraftRemoteSensing_P3B_CAR_Data_1",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC%2FSUBORBITAL%2FARCTAS_AircraftRemoteSensing_P3B_CAR_Data_1",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://espo.nasa.gov/arctas",
-                    "description": "ESPO Home Page for ARCTAS",
                     "@type": "dcat:Distribution",
+                    "description": "ESPO Home Page for ARCTAS",
+                    "downloadURL": "https://espo.nasa.gov/arctas",
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
-                    "downloadURL": "https://www.nasa.gov/mission_pages/arctas/",
-                    "description": "ARCTAS Home Page",
                     "@type": "dcat:Distribution",
+                    "description": "ARCTAS Home Page",
+                    "downloadURL": "https://www.nasa.gov/mission_pages/arctas/",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://www-air.larc.nasa.gov/missions/arctas/docs/arctas_wp.pdf",
-                    "description": "ARCTAS White Paper",
                     "@type": "dcat:Distribution",
+                    "description": "ARCTAS White Paper",
+                    "downloadURL": "https://www-air.larc.nasa.gov/missions/arctas/docs/arctas_wp.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/project/MISR",
-                    "description": "ASDC Home Page for MISR",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Home Page for MISR",
+                    "downloadURL": "https://asdc.larc.nasa.gov/project/MISR",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www-air.larc.nasa.gov/cgi-bin/ic2008r",
-                    "description": "ARCTAS Final Data Comparison Results",
                     "@type": "dcat:Distribution",
+                    "description": "ARCTAS Final Data Comparison Results",
+                    "downloadURL": "https://www-air.larc.nasa.gov/cgi-bin/ic2008r",
+                    "mediaType": "text/html",
                     "title": "View this dataset's science data product validation documentation"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://acp.copernicus.org/articles/10/5191/2010/",
-                    "description": "ARCTAS Overview Paper",
                     "@type": "dcat:Distribution",
+                    "description": "ARCTAS Overview Paper",
+                    "downloadURL": "https://acp.copernicus.org/articles/10/5191/2010/",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/ASDC/SUBORBITAL/ARCTAS_AircraftRemoteSensing_P3B_CAR_Data_1",
-                    "description": "DOI for ARCTAS_AircraftRemoteSensing_P3B_CAR_Data_1",
                     "@type": "dcat:Distribution",
+                    "description": "DOI for ARCTAS_AircraftRemoteSensing_P3B_CAR_Data_1",
+                    "downloadURL": "https://doi.org/10.5067/ASDC/SUBORBITAL/ARCTAS_AircraftRemoteSensing_P3B_CAR_Data_1",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2449574114-LARC_ASDC",
-                    "description": "Earthdata search client for ARCTAS_AircraftRemoteSensing_P3B_CAR_Data_1",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata search client for ARCTAS_AircraftRemoteSensing_P3B_CAR_Data_1",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2449574114-LARC_ASDC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/ARCTAS/AircraftRemoteSensing_P3B_CAR_Data_1/",
-                    "description": "ASDC Direct Data Download for ARCTAS_AircraftRemoteSensing_P3B_CAR_Data_1",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for ARCTAS_AircraftRemoteSensing_P3B_CAR_Data_1",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/ARCTAS/AircraftRemoteSensing_P3B_CAR_Data_1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/ARCTAS/AircraftRemoteSensing_P3B_CAR_Data_1/contents.html",
-                    "description": "OPeNDAP data access for ARCTAS_AircraftRemoteSensing_P3B_CAR_Data_1",
                     "@type": "dcat:Distribution",
+                    "description": "OPeNDAP data access for ARCTAS_AircraftRemoteSensing_P3B_CAR_Data_1",
+                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/ARCTAS/AircraftRemoteSensing_P3B_CAR_Data_1/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 }
             ],
+            "identifier": "C2449574114-LARC_ASDC",
+            "issued": "2022-01-06",
+            "keyword": [
+                "atmosphere",
+                "atmospheric radiation",
+                "earth science",
+                "clouds"
+            ],
+            "landingPage": "https://doi.org/10.5067/ASDC/SUBORBITAL/ARCTAS_AircraftRemoteSensing_P3B_CAR_Data_1",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2022-09-06",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/LARC/SD/ASDC"
+            },
             "spatial": "<?xml version=\"1.0\" encoding=\"UTF-8\"?><gml:Polygon xmlns:gml=\"http://www.opengis.net/gml/3.2\" srsName=\"EPSG:9825\"><gml:outerBoundaryIs><gml:LinearRing><gml:posList>32.0 -164.0 32.0 -46.5 81.0 -46.5 81.0 -164.0 32.0 -164.0</gml:posList></gml:LinearRing></gml:outerBoundaryIs><gml:innerBoundaryIs></gml:innerBoundaryIs></gml:Polygon>",
+            "temporal": "2008-03-25T00:00:00Z/2008-07-13T23:59:59.999Z",
             "theme": [
                 "ARCTAS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "ARCTAS P-3B Aircraft CAR Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=IRAS-A-FPA-3-RDR-IMPS-V6.0",
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
+            "description": "The Supplemental IRAS Minor Planet Survey (SIMPS) presents additional and revised diameters and albedos for asteroids detected by the 1983 IRAS mission. SIMPS is considered to supersede the diameters and albedos of the original 1992 IRAS Minor Planet Survey (IMPS).",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.iras-a-fpa-3-rdr-imps-v6.0_ebyb-n6zi",
+            "issued": "2018-06-26",
+            "keyword": [
+                "support archives",
+                "asteroid"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=IRAS-A-FPA-3-RDR-IMPS-V6.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.iras-a-fpa-3-rdr-imps-v6.0_ebyb-n6zi",
-            "description": "The Supplemental IRAS Minor Planet Survey (SIMPS) presents additional and revised diameters and albedos for asteroids detected by the 1983 IRAS mission. SIMPS is considered to supersede the diameters and albedos of the original 1992 IRAS Minor Planet Survey (IMPS).",
-            "title": "IRAS MINOR PLANET SURVEY V6.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "IRAS MINOR PLANET SURVEY V6.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/SUOMI-NPP/VIIRS/L3M/RRS/2022",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/GSFC/SED/ESD/GCDC/OB.DAAC. https://doi.org/10.5067/SUOMI-NPP/VIIRS/L3M/RRS/2022.",
-            "issued": "2022-09-14",
-            "temporal": "2012-01-02T00:00:00Z/2023-02-28T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-09-14",
-            "keyword": [
-                "earth science",
-                "aerosols",
-                "atmosphere",
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
-            "identifier": "C2340494442-OB_DAAC",
             "description": "The Visible and Infrared Imager/Radiometer Suite (VIIRS) is a multi-disciplinary instrument that is being flown on the Joint Polar Satellite System (JPSS) series of spacecraft, including the Suomi National Polar-orbiting Partnership (S-NPP) that launched in October 2011. JPSS is a multi-platform, multi-agency program that consolidates the polar orbiting spacecraft of NASA and the National Oceanic and Atmospheric Administration (NOAA). S-NPP is the initial spacecraft in this series, and VIIRS is the successor to MODIS for Earth science data product generation. VIIRS has 22 spectral bands ranging from 412 nm to 12 nm. There are 16 moderate-resolution bands (750m at nadir), 5 image-resolution bands (375m), and one day-night band (DNB).",
-            "title": "Suomi-NPP VIIRS Global Mapped Remote-Sensing Reflectance (RRS) Data, version R2022.0",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSUOMI-NPP%2FVIIRS%2FL3M%2FRRS%2F2022",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSUOMI-NPP%2FVIIRS%2FL3M%2FRRS%2F2022",
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
-                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/data/10.5067/SUOMI-NPP/VIIRS/L3M/RRS/2022",
-                    "description": "VIIRS-Suomi-NPP L3M Remote-Sensing Reflectance (RRS) Dataset Landing Page",
                     "@type": "dcat:Distribution",
+                    "description": "VIIRS-Suomi-NPP L3M Remote-Sensing Reflectance (RRS) Dataset Landing Page",
+                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/data/10.5067/SUOMI-NPP/VIIRS/L3M/RRS/2022",
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
+            "identifier": "C2340494442-OB_DAAC",
+            "issued": "2022-09-14",
+            "keyword": [
+                "earth science",
+                "aerosols",
+                "atmosphere",
+                "ocean optics",
+                "oceans"
+            ],
+            "landingPage": "https://doi.org/10.5067/SUOMI-NPP/VIIRS/L3M/RRS/2022",
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
+            "title": "Suomi-NPP VIIRS Global Mapped Remote-Sensing Reflectance (RRS) Data, version R2022.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC2-0683-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 2 phase 2015-03-11 to 2015-06-30. It is a Global Gravity measurement at the comet 67P and covers the time 2015-03-30T14:53:05.000 to 2015-03-30T21:04:20.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc2-0683-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC2-0683-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc2-0683-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 2 phase 2015-03-11 to 2015-06-30. It is a Global Gravity measurement at the comet 67P and covers the time 2015-03-30T14:53:05.000 to 2015-03-30T21:04:20.000.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 2 0683 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 2 0683 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-3-RDR-OCCULTATIONS-V1.0",
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
+            "description": "This data set is a collection of reported timings of observed asteroid occultations though 1998, and reliable occultation diameters published through the given STOP TIME. The timing data are previously unpublished; the diameters are reproduced from Millis and Dunham (1989) and Dunham, et al. (2002).",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-3-rdr-occultations-v1.0_ebzd-73ci",
+            "issued": "2021-05-21",
+            "keyword": [
+                "asteroid",
+                "support archives"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-3-RDR-OCCULTATIONS-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-3-rdr-occultations-v1.0_ebzd-73ci",
-            "description": "This data set is a collection of reported timings of observed asteroid occultations though 1998, and reliable occultation diameters published through the given STOP TIME. The timing data are previously unpublished; the diameters are reproduced from Millis and Dunham (1989) and Dunham, et al. (2002).",
-            "title": "ASTEROID OCCULTATIONS V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ASTEROID OCCULTATIONS V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC3-0939-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 3 phase 2015-07-01 to 2015-10-21. It is a Global Gravity measurement at the comet 67P and covers the time 2015-08-03T16:20:45.000 to 2015-08-03T17:27:19.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc3-0939-v1.0_ebzt-xms8",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC3-0939-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc3-0939-v1.0_ebzt-xms8",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 3 phase 2015-07-01 to 2015-10-21. It is a Global Gravity measurement at the comet 67P and covers the time 2015-08-03T16:20:45.000 to 2015-08-03T17:27:19.000.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 3 0939 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 3 0939 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-5-EXT1-67P-M25-GEO-V1.0",
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
+            "description": "This CODMAC level 5 data set contains derived data products that include pixel-precise georeferencing information, acquired by the OSIRIS Wide Angle Camera on the Rosetta spacecraft during the ROSETTA EXTENSION 1 mission phase, covering the period from 2016-01-12T23:25:00.000 to 2016-02-09T23:24:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V1.0 is the first version of this dataset: Lien corrected dataset after October 2018 PSA/PDS external peer review.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-5-ext1-67p-m25-geo-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-5-EXT1-67P-M25-GEO-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-5-ext1-67p-m25-geo-v1.0",
-            "description": "This CODMAC level 5 data set contains derived data products that include pixel-precise georeferencing information, acquired by the OSIRIS Wide Angle Camera on the Rosetta spacecraft during the ROSETTA EXTENSION 1 mission phase, covering the period from 2016-01-12T23:25:00.000 to 2016-02-09T23:24:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V1.0 is the first version of this dataset: Lien corrected dataset after October 2018 PSA/PDS external peer review.",
-            "title": "ROSETTA-ORBITER 67P OSIWAC 5 EXT1-MTP025 DDR-GEO V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P OSIWAC 5 EXT1-MTP025 DDR-GEO V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/SENTINEL-3B/OLCI/L2/EFR/OC/2022",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/GSFC/SED/ESD/GCDC/OB.DAAC. https://doi.org/10.5067/SENTINEL-3B/OLCI/L2/EFR/OC/2022.",
-            "issued": "2022-09-13",
-            "temporal": "2018-04-25T00:00:00Z/2024-04-22T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-04-13",
-            "keyword": [
-                "earth science",
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
-            "identifier": "C2250852705-OB_DAAC",
             "description": "The Ocean and Land Colour Instrument (OLCI) is the successor to ENVISAT's Medium Resolution Imaging Spectrometer (MERIS) having additional spectral channels, different camera arrangements and simplified on-board processing. The OLCI is a push-broom instrument with five camera modules sharing the field of view. The field of view of the five cameras is arranged in a fan-shaped configuration in the vertical plane, perpendicular to the platform velocity. Each camera has an individual field of view of 14.2\u00b0 and a 0.6\u00b0 overlap with its neighbors. The whole field of view is shifted across track by 12.6\u00b0 away from the sun to minimize the impact of sun glint. OLCI is equipped with on-board calibration hardware based on sun diffusers. There are three sun diffusers--two 'white' diffusers dedicated to radiometric calibration and one dedicated to spectral calibration, with spectral reflectance features. The native resolution is approximately 300m, refered to as Full Resolution (FR). A Reduced Resolution (RR) processing mode provides Level-1B data at sampling rates decreased by a factor of four in both spatial dimensions resulting to resolution of approximately 1.2 km.",
-            "title": "Sentinel-3B OLCI Level-2 Earth-observation Full Resolution (EFR) Ocean Color (OC) Data, version R2022.0",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSENTINEL-3B%2FOLCI%2FL2%2FEFR%2FOC%2F2022",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSENTINEL-3B%2FOLCI%2FL2%2FEFR%2FOC%2F2022",
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
+            "identifier": "C2250852705-OB_DAAC",
+            "issued": "2022-09-13",
+            "keyword": [
+                "earth science",
+                "ocean optics",
+                "oceans"
+            ],
+            "landingPage": "https://doi.org/10.5067/SENTINEL-3B/OLCI/L2/EFR/OC/2022",
+            "language": [
```

