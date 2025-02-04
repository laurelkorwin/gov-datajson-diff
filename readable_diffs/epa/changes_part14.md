# Change History for epa.json (Part 14)

### Changes from 31606f9 to dd2190f (Part 4/33)
**Author:** Automated

**Date:** 2025-02-01 15:02:16+00:00

**Message:** Updated data: Sat Feb  1 15:02:16 UTC 2025

```diff
-                    "accessURL": "https://www.ncbi.nlm.nih.gov/assembly?LinkName=nuccore_assembly&from_uid=650319607"
+                    "accessURL": "https://www.ncbi.nlm.nih.gov/assembly?LinkName=nuccore_assembly&from_uid=650319607",
+                    "title": "https://www.ncbi.nlm.nih.gov/assembly?LinkName=nuccore_assembly&from_uid=650319607"
                 },
                 {
-                    "title": "https://www.ncbi.nlm.nih.gov/assembly/GCA_000700965.1/",
-                    "accessURL": "https://www.ncbi.nlm.nih.gov/assembly/GCA_000700965.1/"
+                    "accessURL": "https://www.ncbi.nlm.nih.gov/assembly/GCA_000700965.1/",
+                    "title": "https://www.ncbi.nlm.nih.gov/assembly/GCA_000700965.1/"
                 },
                 {
-                    "title": "FHM Diversity Data.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/349/FHM%20Diversity%20Data.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "FHM Diversity Data.xlsx"
                 }
             ],
+            "identifier": "A-thtw-349",
+            "keyword": [
+                "genome",
+                "pathfinder innovation project",
+                "adverse outcome pathway",
+                "computational toxicology",
+                "aquatic ecosystems"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2014-06-10",
-            "references": [
-                "https://doi.org/10.1002/etc.3186"
+            "programCode": [
+                "020:095"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -36593,19 +36587,29 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1002/etc.3186"
+            ],
+            "rights": null,
+            "title": "SEQUENCING AND DE NOVO DRAFT ASSEMBLIES OF A FATHEAD MINNOW (Pimpehales promelas) reference genome"
         },
         {
-            "title": "Farraj_NO2-O3 Sequential exposure study_All data",
-            "description": "Cardiovascular Physiologic and Systemic Responses to Sequential Exposure to Nitrogen Dioxide and Ozone in Rats. \n\nThis dataset is associated with the following publication:\nFarraj , A., F. Malik, N. Coates , L. Walsh , D. Winsett , D. Terrell , L. Thompson, W. Cascio , and M. Hazari. Morning NO2 Exposure Sensitizes Hypertensive Rats to the Cardiovascular Effects of Same Day O3 Exposure in the Afternoon.   INHALATION TOXICOLOGY. Informa Healthcare USA, New York, NY, USA, 28(4): 170-179, (2016).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:094"
+            "contactPoint": {
+                "fn": "Aimen Farraj",
+                "hasEmail": "mailto:farraj.aimen@epa.gov"
+            },
+            "description": "Cardiovascular Physiologic and Systemic Responses to Sequential Exposure to Nitrogen Dioxide and Ozone in Rats. \n\nThis dataset is associated with the following publication:\nFarraj , A., F. Malik, N. Coates , L. Walsh , D. Winsett , D. Terrell , L. Thompson, W. Cascio , and M. Hazari. Morning NO2 Exposure Sensitizes Hypertensive Rats to the Cardiovascular Effects of Same Day O3 Exposure in the Afternoon.   INHALATION TOXICOLOGY. Informa Healthcare USA, New York, NY, USA, 28(4): 170-179, (2016).",
+            "distribution": [
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/235/AF13_NO2-O3%20Sequential%20exposure%20study_All%20data.xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "AF13_NO2-O3 Sequential exposure study_All data.xlsx"
+                }
             ],
             "identifier": "A-3xsn-235",
             "keyword": [
@@ -36625,20 +36629,10 @@
                 "autonomic nervous system",
                 "cardiovascular"
             ],
-            "contactPoint": {
-                "fn": "Aimen Farraj",
-                "hasEmail": "mailto:farraj.aimen@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "AF13_NO2-O3 Sequential exposure study_All data.xlsx",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/235/AF13_NO2-O3%20Sequential%20exposure%20study_All%20data.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2016-08-24",
-            "references": [
-                "https://doi.org/10.3109/08958378.2016.1148088"
+            "programCode": [
+                "020:094"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -36648,19 +36642,43 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.3109/08958378.2016.1148088"
+            ],
+            "rights": null,
+            "title": "Farraj_NO2-O3 Sequential exposure study_All data"
         },
         {
-            "title": "Land use and beach closure 2004-2013 in the United States",
-            "description": "The dataset contains the beach closure data and land use information around each beach in 2006 and 2011 in the United States. The original data are created by EPA and USGS and publicly available (the links are provided). \n\nThis dataset is associated with the following publication:\nWu, J., and L. Jackson. Association of land use and its change with beach closure in the United States, 2004-2013.   SCIENCE OF THE TOTAL ENVIRONMENT. Elsevier BV, AMSTERDAM,  NETHERLANDS, 571: 67-76, (2016).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
+            "contactPoint": {
+                "fn": "Jianyong Wu",
+                "hasEmail": "mailto:wu.jianyong@epa.gov"
+            },
+            "describedBy": "https://pasteur.epa.gov/uploads/90/documents/Data%20dictonary.docx",
+            "describedByType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+            "description": "The dataset contains the beach closure data and land use information around each beach in 2006 and 2011 in the United States. The original data are created by EPA and USGS and publicly available (the links are provided). \n\nThis dataset is associated with the following publication:\nWu, J., and L. Jackson. Association of land use and its change with beach closure in the United States, 2004-2013.   SCIENCE OF THE TOTAL ENVIRONMENT. Elsevier BV, AMSTERDAM,  NETHERLANDS, 571: 67-76, (2016).",
+            "distribution": [
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/90/Beach%20closure%20and%20land%20use%20dataset.xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Beach closure and land use dataset.xlsx"
+                },
+                {
+                    "accessURL": "https://watersgeo.epa.gov/beacon2/",
+                    "title": "https://watersgeo.epa.gov/beacon2/"
+                },
+                {
+                    "accessURL": "https://nhd.usgs.gov/data.html",
+                    "title": "https://nhd.usgs.gov/data.html"
+                },
+                {
+                    "accessURL": "https://www.mrlc.gov/data",
+                    "title": "https://www.mrlc.gov/data"
+                }
             ],
             "identifier": "A-ns28-90",
             "keyword": [
@@ -36679,32 +36697,10 @@
                 "urbanization",
                 "ecosystem health"
             ],
-            "contactPoint": {
-                "fn": "Jianyong Wu",
-                "hasEmail": "mailto:wu.jianyong@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "Beach closure and land use dataset.xlsx",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/90/Beach%20closure%20and%20land%20use%20dataset.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
-                },
-                {
-                    "title": "https://watersgeo.epa.gov/beacon2/",
-                    "accessURL": "https://watersgeo.epa.gov/beacon2/"
-                },
-                {
-                    "title": "https://nhd.usgs.gov/data.html",
-                    "accessURL": "https://nhd.usgs.gov/data.html"
-                },
-                {
-                    "title": "https://www.mrlc.gov/data",
-                    "accessURL": "https://www.mrlc.gov/data"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2016-05-31",
-            "references": [
-                "https://doi.org/10.1016/j.scitotenv.2016.07.116"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -36715,20 +36711,28 @@
                     }
                 }
             },
-            "describedBy": "https://pasteur.epa.gov/uploads/90/documents/Data%20dictonary.docx",
-            "describedByType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
+            "references": [
+                "https://doi.org/10.1016/j.scitotenv.2016.07.116"
+            ],
+            "rights": null,
+            "title": "Land use and beach closure 2004-2013 in the United States"
         },
         {
-            "title": "ORD-017311_Data_Brown_DermPerm.xlsx",
-            "description": "List of chemicals used for model evaluation, their MW, log KOW, and references for the original data source(s), the review(s) the data was collected from, and reference for log KOW as cited in the reviews. [Table SI-3 of research article]. \n\nThis dataset is associated with the following publication:\nBrown, T., J. Armitage, P. Egeghy, I. Kircanski, and J. Arnot. Dermal permeation data and models for the prioritization and screening-level exposure assessment of organic chemicals.   ENVIRONMENT INTERNATIONAL. Elsevier Science Ltd, New York, NY, USA, 94: 424-435, (2016).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:095"
+            "contactPoint": {
+                "fn": "Peter Egeghy",
+                "hasEmail": "mailto:egeghy.peter@epa.gov"
+            },
+            "description": "List of chemicals used for model evaluation, their MW, log KOW, and references for the original data source(s), the review(s) the data was collected from, and reference for log KOW as cited in the reviews. [Table SI-3 of research article]. \n\nThis dataset is associated with the following publication:\nBrown, T., J. Armitage, P. Egeghy, I. Kircanski, and J. Arnot. Dermal permeation data and models for the prioritization and screening-level exposure assessment of organic chemicals.   ENVIRONMENT INTERNATIONAL. Elsevier Science Ltd, New York, NY, USA, 94: 424-435, (2016).",
+            "distribution": [
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/288/ORD-017311_Data_Brown_DermPerm.xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "ORD-017311_Data_Brown_DermPerm.xlsx"
+                }
             ],
             "identifier": "A-9s4x-288",
             "keyword": [
@@ -36741,20 +36745,10 @@
                 "Permeation Database",
                 "ExpoCast"
             ],
-            "contactPoint": {
-                "fn": "Peter Egeghy",
-                "hasEmail": "mailto:egeghy.peter@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "ORD-017311_Data_Brown_DermPerm.xlsx",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/288/ORD-017311_Data_Brown_DermPerm.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2016-05-20",
-            "references": [
-                "http://www.sciencedirect.com/science/article/pii/S0160412016302094"
+            "programCode": [
+                "020:095"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -36764,42 +36758,42 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "http://www.sciencedirect.com/science/article/pii/S0160412016302094"
+            ],
+            "rights": null,
+            "title": "ORD-017311_Data_Brown_DermPerm.xlsx"
         },
         {
-            "title": "Modeling Tribal Exposures to Methyl Mercury from Fish Consumption ",
-            "description": "data is from NHANES study and EPA fish intake and HG concentration in fish tissue. \n\nThis dataset is associated with the following publication:\nXue , J., V. Zartarian , B. Mintz , M. Weber , K. Bailey , and A. Geller. Modeling tribal exposures to methyl mercury from fish consumption.   SCIENCE OF THE TOTAL ENVIRONMENT. Elsevier BV, AMSTERDAM,  NETHERLANDS, 533: 102-109, (2015).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "A-5dv8-206",
-            "keyword": [
-                "mercury",
-                "tribal",
-                "fish consumption",
-                "exposures",
-                "SHEDS-Dietary"
-            ],
             "contactPoint": {
                 "fn": "Jianping Xue",
                 "hasEmail": "mailto:xue.jianping@epa.gov"
             },
+            "description": "data is from NHANES study and EPA fish intake and HG concentration in fish tissue. \n\nThis dataset is associated with the following publication:\nXue , J., V. Zartarian , B. Mintz , M. Weber , K. Bailey , and A. Geller. Modeling tribal exposures to methyl mercury from fish consumption.   SCIENCE OF THE TOTAL ENVIRONMENT. Elsevier BV, AMSTERDAM,  NETHERLANDS, 533: 102-109, (2015).",
             "distribution": [
                 {
-                    "title": "tribal fish HG paper data.zip",
                     "downloadURL": "https://pasteur.epa.gov/uploads/206/tribal%20fish%20HG%20paper%20data.zip",
-                    "mediaType": "application/x-zip-compressed"
+                    "mediaType": "application/x-zip-compressed",
+                    "title": "tribal fish HG paper data.zip"
                 }
             ],
+            "identifier": "A-5dv8-206",
+            "keyword": [
+                "mercury",
+                "tribal",
+                "fish consumption",
+                "exposures",
+                "SHEDS-Dietary"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2015-03-04",
-            "references": [
-                "https://doi.org/10.1016/j.scitotenv.2015.06.070"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -36809,44 +36803,47 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.scitotenv.2015.06.070"
+            ],
+            "rights": null,
+            "title": "Modeling Tribal Exposures to Methyl Mercury from Fish Consumption "
         },
         {
-            "title": "EPA True NO2 ground site measurements \u2013 multiple sites, TCEQ ground site measurements of meteorological and air pollution parameters \u2013 multiple sites ,GeoTASO NO2 Vertical Column ",
-            "description": "EPA True NO2 ground site measurements \u2013 multiple sites - http://www-air.larc.nasa.gov/cgi-bin/ArcView/discover-aq.tx-2013; TCEQ ground site measurements of meteorological and air pollution parameters \u2013 multiple sites - http://www-air.larc.nasa.gov/cgi-bin/ArcView/discover-aq.tx-2013; GeoTASO NO2 Vertical Column - http://www-air.larc.nasa.gov/cgi-bin/ArcView/discover-aq.tx-2013?FALCON=1. \n\nThis dataset is associated with the following publication:\nNowlan, C., X. Lu, J. Leitch, K. Chance, G. Gonz\u00e1lez Abad, C. Lu, P. Zoogman, J. Cole, T. Delker, W. Good, F. Murcray, L. Ruppert, D. Soo, M. Follette-Cook, S. Janz, M. Kowalewski, C. Loughner, K. Pickering, J. Herman, M. Beaver, R. Long, J. Szykman, L. Judd, P. Kelley, W. Luke, X. Ren, and J. Al-Saadi. Nitrogen dioxide observations from the Geostationary Trace gas and Aerosol Sensor Optimization (GeoTASO) airborne instrument: Retrieval algorithm and measurements during DISCOVER-AQ Texas 2013.   Atmospheric Measurement Techniques. Copernicus Publications, Katlenburg-Lindau,  GERMANY, 9(6): 2647-2668, (2016).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:094"
-            ],
-            "identifier": "A-8pk8-342",
-            "keyword": [
-                "nitrogen dioxide",
-                "column density",
-                "air quality from space",
-                "GeoTASO",
-                "True NO2"
-            ],
             "contactPoint": {
                 "fn": "James Szykman",
                 "hasEmail": "mailto:szykman.jim@epa.gov"
             },
+            "describedBy": "https://www-air.larc.nasa.gov/cgi-bin/ArcView/discover-aq.tx-2013",
+            "description": "EPA True NO2 ground site measurements \u2013 multiple sites - http://www-air.larc.nasa.gov/cgi-bin/ArcView/discover-aq.tx-2013; TCEQ ground site measurements of meteorological and air pollution parameters \u2013 multiple sites - http://www-air.larc.nasa.gov/cgi-bin/ArcView/discover-aq.tx-2013; GeoTASO NO2 Vertical Column - http://www-air.larc.nasa.gov/cgi-bin/ArcView/discover-aq.tx-2013?FALCON=1. \n\nThis dataset is associated with the following publication:\nNowlan, C., X. Lu, J. Leitch, K. Chance, G. Gonz\u00e1lez Abad, C. Lu, P. Zoogman, J. Cole, T. Delker, W. Good, F. Murcray, L. Ruppert, D. Soo, M. Follette-Cook, S. Janz, M. Kowalewski, C. Loughner, K. Pickering, J. Herman, M. Beaver, R. Long, J. Szykman, L. Judd, P. Kelley, W. Luke, X. Ren, and J. Al-Saadi. Nitrogen dioxide observations from the Geostationary Trace gas and Aerosol Sensor Optimization (GeoTASO) airborne instrument: Retrieval algorithm and measurements during DISCOVER-AQ Texas 2013.   Atmospheric Measurement Techniques. Copernicus Publications, Katlenburg-Lindau,  GERMANY, 9(6): 2647-2668, (2016).",
             "distribution": [
                 {
-                    "title": "https://www-air.larc.nasa.gov/cgi-bin/ArcView/discover-aq.tx-2013",
-                    "accessURL": "https://www-air.larc.nasa.gov/cgi-bin/ArcView/discover-aq.tx-2013"
+                    "accessURL": "https://www-air.larc.nasa.gov/cgi-bin/ArcView/discover-aq.tx-2013",
+                    "title": "https://www-air.larc.nasa.gov/cgi-bin/ArcView/discover-aq.tx-2013"
                 },
                 {
-                    "title": "https://www-air.larc.nasa.gov/cgi-bin/ArcView/discover-aq.tx-2013?FALCON=1",
-                    "accessURL": "https://www-air.larc.nasa.gov/cgi-bin/ArcView/discover-aq.tx-2013?FALCON=1"
+                    "accessURL": "https://www-air.larc.nasa.gov/cgi-bin/ArcView/discover-aq.tx-2013?FALCON=1",
+                    "title": "https://www-air.larc.nasa.gov/cgi-bin/ArcView/discover-aq.tx-2013?FALCON=1"
                 }
             ],
+            "identifier": "A-8pk8-342",
+            "keyword": [
+                "nitrogen dioxide",
+                "column density",
+                "air quality from space",
+                "GeoTASO",
+                "True NO2"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2016-09-16",
-            "references": null,
+            "programCode": [
+                "020:094"
+            ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
                 "subOrganizationOf": {
@@ -36856,52 +36853,51 @@
                     }
                 }
             },
-            "describedBy": "https://www-air.larc.nasa.gov/cgi-bin/ArcView/discover-aq.tx-2013"
+            "references": null,
+            "rights": null,
+            "title": "EPA True NO2 ground site measurements \u2013 multiple sites, TCEQ ground site measurements of meteorological and air pollution parameters \u2013 multiple sites ,GeoTASO NO2 Vertical Column "
         },
         {
-            "title": "GADEP Continuous PM2.5 mass concentration data, VIIRS Day Night Band SDR (SVDNB), MODIS Terra Level 2 water vapor profiles (infrared algorithm for atmospheric profiles for both day and night, NWS surface meteorological data",
-            "description": "Data descriptions are provided at the following urls:\nGADEP Continuous PM2.5 mass concentration data - https://aqs.epa.gov/aqsweb/documents/data_mart_welcome.html\nhttps://www3.epa.gov/ttn/amtic/files/ambient/pm25/qa/QA-Handbook-Vol-II.pdf\n\nVIIRS Day Night Band SDR (SVDNB) http://www.class.ngdc.noaa.gov/saa/products/search?datatype_family=VIIRS_SDR\n\nMODIS Terra Level 2 water vapor profiles (infrared algorithm for atmospheric profiles for both day and night -MOD0&_L2;  http://modis-atmos.gsfc.nasa.gov/MOD07_L2/index.html \n\nNWS surface meteorological data - https://www.ncdc.noaa.gov/isd. \n\nThis dataset is associated with the following publication:\nWang, J., C. Aegerter, and J. Szykman. Potential Application of VIIRS Day/Night Band for Monitoring Nighttime Surface PM2.5 Air Quality From Space.   ATMOSPHERIC ENVIRONMENT. Elsevier Science Ltd, New York, NY, USA, 124(0): 55-63, (2016).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:094"
-            ],
-            "identifier": "A-4j14-348",
-            "keyword": [
-                "Suomi National Polar-orbiting Partnership (S-NPP) satellite",
-                "Visible Infrared Imaging Radiometer Suite (VIIRS)",
-                "day-night band (DNB)",
-                "particulate matter (PM)",
-                "air quality monitoring at night"
-            ],
             "contactPoint": {
                 "fn": "James Szykman",
                 "hasEmail": "mailto:szykman.jim@epa.gov"
             },
+            "description": "Data descriptions are provided at the following urls:\nGADEP Continuous PM2.5 mass concentration data - https://aqs.epa.gov/aqsweb/documents/data_mart_welcome.html\nhttps://www3.epa.gov/ttn/amtic/files/ambient/pm25/qa/QA-Handbook-Vol-II.pdf\n\nVIIRS Day Night Band SDR (SVDNB) http://www.class.ngdc.noaa.gov/saa/products/search?datatype_family=VIIRS_SDR\n\nMODIS Terra Level 2 water vapor profiles (infrared algorithm for atmospheric profiles for both day and night -MOD0&_L2;  http://modis-atmos.gsfc.nasa.gov/MOD07_L2/index.html \n\nNWS surface meteorological data - https://www.ncdc.noaa.gov/isd. \n\nThis dataset is associated with the following publication:\nWang, J., C. Aegerter, and J. Szykman. Potential Application of VIIRS Day/Night Band for Monitoring Nighttime Surface PM2.5 Air Quality From Space.   ATMOSPHERIC ENVIRONMENT. Elsevier Science Ltd, New York, NY, USA, 124(0): 55-63, (2016).",
             "distribution": [
                 {
-                    "title": "https://aqs.epa.gov/aqsweb/documents/data_mart_welcome.html",
-                    "accessURL": "https://aqs.epa.gov/aqsweb/documents/data_mart_welcome.html"
+                    "accessURL": "https://aqs.epa.gov/aqsweb/documents/data_mart_welcome.html",
+                    "title": "https://aqs.epa.gov/aqsweb/documents/data_mart_welcome.html"
                 },
                 {
-                    "title": "https://modis-atmos.gsfc.nasa.gov/MOD07_L2/index.html",
-                    "accessURL": "https://modis-atmos.gsfc.nasa.gov/MOD07_L2/index.html"
+                    "accessURL": "https://modis-atmos.gsfc.nasa.gov/MOD07_L2/index.html",
+                    "title": "https://modis-atmos.gsfc.nasa.gov/MOD07_L2/index.html"
                 },
                 {
-                    "title": "https://www.ncdc.noaa.gov/isd",
-                    "accessURL": "https://www.ncdc.noaa.gov/isd"
+                    "accessURL": "https://www.ncdc.noaa.gov/isd",
+                    "title": "https://www.ncdc.noaa.gov/isd"
                 },
                 {
-                    "title": "https://eogdata.mines.edu/products/vnl/",
-                    "accessURL": "https://eogdata.mines.edu/products/vnl/"
+                    "accessURL": "https://eogdata.mines.edu/products/vnl/",
+                    "title": "https://eogdata.mines.edu/products/vnl/"
                 }
             ],
+            "identifier": "A-4j14-348",
+            "keyword": [
+                "Suomi National Polar-orbiting Partnership (S-NPP) satellite",
+                "Visible Infrared Imaging Radiometer Suite (VIIRS)",
+                "day-night band (DNB)",
+                "particulate matter (PM)",
+                "air quality monitoring at night"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2016-09-19",
-            "references": null,
+            "programCode": [
+                "020:094"
+            ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
                 "subOrganizationOf": {
@@ -36910,43 +36906,41 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": null,
+            "rights": null,
+            "title": "GADEP Continuous PM2.5 mass concentration data, VIIRS Day Night Band SDR (SVDNB), MODIS Terra Level 2 water vapor profiles (infrared algorithm for atmospheric profiles for both day and night, NWS surface meteorological data"
         },
         {
-            "title": "Hance_WestForkSmithRiver_flasher_location_data",
-            "description": "This entry contains two files.  The first file, \"Hance_WFSR Flasher locations.xlxs\", contains information describing the location of installed landmark 'flashers' consisting of 2\" square aluminum metal tags.  Each tag was inscribed with a number to aid field personnel in the identification of landmark location within the West Fork Smith River watershed in southern coastal Oregon. These landmarks were used to calculate stream distances between points in the watershed, including distances between tagging locations and detection events for tagged fish. \n\nA second file, named \"Hance_fish_detection_data1.xlxs\" contains information on the detection of tagged fish within the West Fork Smith River stream network.  The file includes both the location where the fish were tagged and where they were subsequently detected.  Together with the information in the WFSR flasher location dataset, these data allow estimation of the minimum distances and directions moved by juvenile coho salmon during the fall transition period.\n\nA map locator is provided in Figure 1 in the accompanying manuscript: Dalton J. Hance, Lisa M. Ganio, Kelly M. Burnett & Joseph L. Ebersole (2016) Basin-Scale Variation in the Spatial Pattern of Fall Movement of Juvenile Coho Salmon in the West Fork Smith River, Oregon, Transactions of the American Fisheries Society, 145:5, 1018-1034, DOI: 10.1080/00028487.2016.1194892\". \n\nThis dataset is associated with the following publication:\nHance, D.J., L.M. Ganio, K.M. Burnett, and J. Ebersole. Basin-Scale Variation in the Spatial Pattern of Fall Movement of Juvenile Coho Salmon in the West Fork Smith River, Oregon.   TRANSACTIONS OF THE AMERICAN FISHERIES SOCIETY. American Fisheries Society, Bethesda, MD, USA, 5(145): 1018-1034, (2016).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:096"
-            ],
-            "identifier": "A-fqzj-326",
-            "keyword": [
-                "Salmon"
-            ],
             "contactPoint": {
                 "fn": "Joseph Ebersole",
                 "hasEmail": "mailto:ebersole.joe@epa.gov"
             },
+            "description": "This entry contains two files.  The first file, \"Hance_WFSR Flasher locations.xlxs\", contains information describing the location of installed landmark 'flashers' consisting of 2\" square aluminum metal tags.  Each tag was inscribed with a number to aid field personnel in the identification of landmark location within the West Fork Smith River watershed in southern coastal Oregon. These landmarks were used to calculate stream distances between points in the watershed, including distances between tagging locations and detection events for tagged fish. \n\nA second file, named \"Hance_fish_detection_data1.xlxs\" contains information on the detection of tagged fish within the West Fork Smith River stream network.  The file includes both the location where the fish were tagged and where they were subsequently detected.  Together with the information in the WFSR flasher location dataset, these data allow estimation of the minimum distances and directions moved by juvenile coho salmon during the fall transition period.\n\nA map locator is provided in Figure 1 in the accompanying manuscript: Dalton J. Hance, Lisa M. Ganio, Kelly M. Burnett & Joseph L. Ebersole (2016) Basin-Scale Variation in the Spatial Pattern of Fall Movement of Juvenile Coho Salmon in the West Fork Smith River, Oregon, Transactions of the American Fisheries Society, 145:5, 1018-1034, DOI: 10.1080/00028487.2016.1194892\". \n\nThis dataset is associated with the following publication:\nHance, D.J., L.M. Ganio, K.M. Burnett, and J. Ebersole. Basin-Scale Variation in the Spatial Pattern of Fall Movement of Juvenile Coho Salmon in the West Fork Smith River, Oregon.   TRANSACTIONS OF THE AMERICAN FISHERIES SOCIETY. American Fisheries Society, Bethesda, MD, USA, 5(145): 1018-1034, (2016).",
             "distribution": [
                 {
-                    "title": "Hance_WFSR flasher locations.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/326/Hance_WFSR%20flasher%20locations.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Hance_WFSR flasher locations.xlsx"
                 },
                 {
-                    "title": "Hance_fish_detection_data1.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/326/Hance_fish_detection_data1.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Hance_fish_detection_data1.xlsx"
                 }
             ],
+            "identifier": "A-fqzj-326",
+            "keyword": [
+                "Salmon"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2016-09-14",
-            "references": [
-                "https://doi.org/10.1080/00028487.2016.1194892"
+            "programCode": [
+                "020:096"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -36956,19 +36950,29 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1080/00028487.2016.1194892"
+            ],
+            "rights": null,
+            "title": "Hance_WestForkSmithRiver_flasher_location_data"
         },
         {
-            "title": "National Aquatic Resource Survey Rivers and Streams Data",
-            "description": "Data are from 1,000 river and stream sites across the conterminous US where consistent biological, chemical, physical and watershed data were gathered.  The sites were selected using a probability survey design so that the results provide inferences to all perennial flowing waters in the lower 48 states. \n\nThis dataset is associated with the following publication:\nOmernik, J., S. Paulsen , M. Weber , and G. Griffith. Regional patterns of total nitrogen concentrations in the National Rivers and Streams Assessment.   JOURNAL OF SOIL AND WATER CONSERVATION. Soil and Water Conservation Society,    71(3): 167-181, (2016).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
+            "contactPoint": {
+                "fn": "Steven Paulsen",
+                "hasEmail": "mailto:paulsen.steve@epa.gov"
+            },
+            "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/data-national-aquatic-resource-surveys",
+            "description": "Data are from 1,000 river and stream sites across the conterminous US where consistent biological, chemical, physical and watershed data were gathered.  The sites were selected using a probability survey design so that the results provide inferences to all perennial flowing waters in the lower 48 states. \n\nThis dataset is associated with the following publication:\nOmernik, J., S. Paulsen , M. Weber , and G. Griffith. Regional patterns of total nitrogen concentrations in the National Rivers and Streams Assessment.   JOURNAL OF SOIL AND WATER CONSERVATION. Soil and Water Conservation Society,    71(3): 167-181, (2016).",
+            "distribution": [
+                {
+                    "accessURL": "https://www.epa.gov/national-aquatic-resource-surveys/data-national-aquatic-resource-surveys",
+                    "title": "https://www.epa.gov/national-aquatic-resource-surveys/data-national-aquatic-resource-surveys"
+                }
             ],
             "identifier": "A-7d84-341",
             "keyword": [
@@ -36979,19 +36983,10 @@
                 "nitrogen",
                 "watersheds"
             ],
-            "contactPoint": {
-                "fn": "Steven Paulsen",
-                "hasEmail": "mailto:paulsen.steve@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "https://www.epa.gov/national-aquatic-resource-surveys/data-national-aquatic-resource-surveys",
-                    "accessURL": "https://www.epa.gov/national-aquatic-resource-surveys/data-national-aquatic-resource-surveys"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2016-08-01",
-            "references": [
-                "https://doi.org/10.2489/jswc.71.3.167"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -37002,19 +36997,27 @@
                     }
                 }
             },
-            "describedBy": "https://www.epa.gov/national-aquatic-resource-surveys/data-national-aquatic-resource-surveys"
+            "references": [
+                "https://doi.org/10.2489/jswc.71.3.167"
+            ],
+            "rights": null,
+            "title": "National Aquatic Resource Survey Rivers and Streams Data"
         },
         {
-            "title": "National Aquatic Resource Survey data",
-            "description": "Surface water monitoring data from national aquatic surveys (lakes, streams, rivers). \n\nThis dataset is associated with the following publication:\nStoddard , J., J. Van Sickle, A. Herlihy, J. Brahney, S. Paulsen , D. Peck , R. Mitchell , and A. Pollard. Continental-scale increase in stream and lake phosphorus: Are oligotrophic systems disappearing in the U.S.?.   ENVIRONMENTAL SCIENCE & TECHNOLOGY. American Chemical Society, Washington, DC, USA, 50(7): 3409-3415, (2016).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:096"
+            "contactPoint": {
+                "fn": "John Stoddard",
+                "hasEmail": "mailto:stoddard.john@epa.gov"
+            },
+            "description": "Surface water monitoring data from national aquatic surveys (lakes, streams, rivers). \n\nThis dataset is associated with the following publication:\nStoddard , J., J. Van Sickle, A. Herlihy, J. Brahney, S. Paulsen , D. Peck , R. Mitchell , and A. Pollard. Continental-scale increase in stream and lake phosphorus: Are oligotrophic systems disappearing in the U.S.?.   ENVIRONMENTAL SCIENCE & TECHNOLOGY. American Chemical Society, Washington, DC, USA, 50(7): 3409-3415, (2016).",
+            "distribution": [
+                {
+                    "accessURL": "https://www.epa.gov/national-aquatic-resource-surveys/data-national-aquatic-resource-surveys",
+                    "title": "https://www.epa.gov/national-aquatic-resource-surveys/data-national-aquatic-resource-surveys"
+                }
             ],
             "identifier": "A-5x6h-325",
             "keyword": [
@@ -37024,19 +37027,10 @@
                 "monitoring",
                 "trends"
             ],
-            "contactPoint": {
-                "fn": "John Stoddard",
-                "hasEmail": "mailto:stoddard.john@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "https://www.epa.gov/national-aquatic-resource-surveys/data-national-aquatic-resource-surveys",
-                    "accessURL": "https://www.epa.gov/national-aquatic-resource-surveys/data-national-aquatic-resource-surveys"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2016-09-14",
-            "references": [
-                "https://doi.org/10.1021/acs.est.5b05950"
+            "programCode": [
+                "020:096"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -37046,50 +37040,54 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1021/acs.est.5b05950"
+            ],
+            "rights": null,
+            "title": "National Aquatic Resource Survey data"
         },
         {
-            "title": "Nitrous Oxide flux measurements under various amendments",
-            "description": "The dataset consists of measurements of soil nitrous oxide emissions from soils under three different amendments: glucose, cellulose, and manure. Data includes the four isotopomers of nitrous oxide (14N15N16O, 15N14N16O, 14N14N18O, 14N14N16O), and the site preference. \n\nThis dataset is associated with the following publication:\nChen , H., D. Williams , P. Deshmukh , F. Birgand, B. Maxwell, and J. Walker. Probing the Biological Sources of Soil N2O Emissions by Quantum Cascade Laser-Based 15N Isotopocule Analysis.   SOIL SCIENCE SOCIETY OF AMERICA JOURNAL. Soil Science Society of America, Madison, WI, USA, 100(0): 175-181, (2016).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:094"
-            ],
-            "identifier": "A-9p8p-365",
-            "keyword": [
-                "site preference",
-                "nitrous oxide",
-                "crop agriculture",
-                "stable isotopes"
-            ],
             "contactPoint": {
                 "fn": "David Williams",
                 "hasEmail": "mailto:williams.davidj@epa.gov"
             },
+            "describedBy": "https://pasteur.epa.gov/uploads/365/documents/Data%20Dictionary.docx",
+            "describedByType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+            "description": "The dataset consists of measurements of soil nitrous oxide emissions from soils under three different amendments: glucose, cellulose, and manure. Data includes the four isotopomers of nitrous oxide (14N15N16O, 15N14N16O, 14N14N18O, 14N14N16O), and the site preference. \n\nThis dataset is associated with the following publication:\nChen , H., D. Williams , P. Deshmukh , F. Birgand, B. Maxwell, and J. Walker. Probing the Biological Sources of Soil N2O Emissions by Quantum Cascade Laser-Based 15N Isotopocule Analysis.   SOIL SCIENCE SOCIETY OF AMERICA JOURNAL. Soil Science Society of America, Madison, WI, USA, 100(0): 175-181, (2016).",
             "distribution": [
                 {
-                    "title": "Data for Science Hub.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/365/Data%20for%20Science%20Hub.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Data for Science Hub.xlsx"
                 },
                 {
-                    "title": "Calibration_June.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/365/Calibration_June.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Calibration_June.xlsx"
                 },
                 {
-                    "title": "Calibration_May.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/365/Calibration_May.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Calibration_May.xlsx"
                 }
             ],
+            "identifier": "A-9p8p-365",
+            "keyword": [
+                "site preference",
+                "nitrous oxide",
+                "crop agriculture",
+                "stable isotopes"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2016-09-21",
-            "references": null,
+            "programCode": [
+                "020:094"
+            ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
                 "subOrganizationOf": {
@@ -37099,20 +37097,26 @@
                     }
                 }
             },
-            "describedBy": "https://pasteur.epa.gov/uploads/365/documents/Data%20Dictionary.docx",
-            "describedByType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
+            "references": null,
+            "rights": null,
+            "title": "Nitrous Oxide flux measurements under various amendments"
         },
         {
-            "title": " Sorption of Radionuclides to Building Materials and its Removal Using Simple Wash Solutions",
-            "description": "Data corresponding to the figures in the paper. \n\nThis dataset is associated with the following publication:\nKaminski, M., C. Mertz, L. Ortega, and N. Kivenas. Sorption of Radionuclides to Building Materials and its Removal Using Simple Wash Solutions.   Journal of Environmental Chemical Engineering. Elsevier B.V., Amsterdam,  NETHERLANDS,  ., (2016).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:060"
+            "contactPoint": {
+                "fn": "Matthew Magnuson",
+                "hasEmail": "mailto:magnuson.matthew@epa.gov"
+            },
+            "description": "Data corresponding to the figures in the paper. \n\nThis dataset is associated with the following publication:\nKaminski, M., C. Mertz, L. Ortega, and N. Kivenas. Sorption of Radionuclides to Building Materials and its Removal Using Simple Wash Solutions.   Journal of Environmental Chemical Engineering. Elsevier B.V., Amsterdam,  NETHERLANDS,  ., (2016).",
+            "distribution": [
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/310/Data%20for%20A-t1gn.xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Data for A-t1gn.xlsx"
+                }
             ],
             "identifier": "A-t1gn-310",
             "keyword": [
@@ -37126,20 +37130,10 @@
                 "radiological disperal device",
                 "nuclear power plant"
             ],
-            "contactPoint": {
-                "fn": "Matthew Magnuson",
-                "hasEmail": "mailto:magnuson.matthew@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "Data for A-t1gn.xlsx",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/310/Data%20for%20A-t1gn.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2012-01-01",
-            "references": [
-                "https://doi.org/10.1016/j.jece.2016.02.004"
+            "programCode": [
+                "020:060"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -37149,20 +37143,24 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.jece.2016.02.004"
+            ],
+            "rights": null,
+            "title": " Sorption of Radionuclides to Building Materials and its Removal Using Simple Wash Solutions"
         },
         {
-            "title": "Wide-Area Decontamination in an Urban Environment after Radiological Dispersion: A Review and Perspectives",
-            "description": "This is a literature review, so contains no original data. This dataset is not publicly accessible because: This paper is a literature review and contains no data. It can be accessed through the following means: This paper is a literature review and contains no data.  The paper contains the literature reviewed. Format: This paper is a literature review and contains no data. \n\nThis dataset is associated with the following publication:\nKaminski, M., S. Lee , and M. Magnuson. Wide-Area Decontamination in an Urban Environment after Radiological Dispersion:  A Review and Perspectives.   ENVIRONMENTAL SCIENCE & TECHNOLOGY. American Chemical Society, Washington, DC, USA, 305: 67-86, (2015).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:060"
-            ],
+            "contactPoint": {
+                "fn": "Matthew Magnuson",
+                "hasEmail": "mailto:magnuson.matthew@epa.gov"
+            },
+            "description": "This is a literature review, so contains no original data. This dataset is not publicly accessible because: This paper is a literature review and contains no data. It can be accessed through the following means: This paper is a literature review and contains no data.  The paper contains the literature reviewed. Format: This paper is a literature review and contains no data. \n\nThis dataset is associated with the following publication:\nKaminski, M., S. Lee , and M. Magnuson. Wide-Area Decontamination in an Urban Environment after Radiological Dispersion:  A Review and Perspectives.   ENVIRONMENTAL SCIENCE & TECHNOLOGY. American Chemical Society, Washington, DC, USA, 305: 67-86, (2015).",
+            "distribution": [],
             "identifier": "A-2ngh-311",
             "keyword": [
                 "remediation",
@@ -37172,14 +37170,10 @@
                 "Decontamination",
                 "nuclear power plant"
             ],
-            "contactPoint": {
-                "fn": "Matthew Magnuson",
-                "hasEmail": "mailto:magnuson.matthew@epa.gov"
-            },
-            "distribution": [],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2015-11-06",
-            "references": [
-                "https://doi.org/10.1016/j.jhazmat.2015.11.014"
+            "programCode": [
+                "020:060"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -37189,40 +37183,42 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.jhazmat.2015.11.014"
+            ],
+            "rights": null,
+            "title": "Wide-Area Decontamination in an Urban Environment after Radiological Dispersion: A Review and Perspectives"
         },
         {
-            "title": "Pulsed and Continuous UV LED Reactor for Water Treatment",
-            "description": "Numerical data represented in the figures which are graphs. \n\nThis dataset is associated with the following publication:\nSpencer, M., M. Miller, J. Richwine, K. Duckworth, L. Racz, M. Grimaila, M. Magnuson , S. Willison , and R. Phillips. Pulsed and Continuous UV LED Reactor for Water Treatment.   Aqua - Journal of Water Supply Research and Technology, International Water Supply Association (London, England). Blackwell Publishing, Malden, MA, USA,  1-75, (2016).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:060"
-            ],
-            "identifier": "A-sn0q-317",
-            "keyword": [
-                "Ultraviolet",
-                "advanced oxidation process",
-                "light emitting diode",
-                "reactor design"
-            ],
             "contactPoint": {
                 "fn": "Matthew Magnuson",
                 "hasEmail": "mailto:magnuson.matthew@epa.gov"
             },
+            "description": "Numerical data represented in the figures which are graphs. \n\nThis dataset is associated with the following publication:\nSpencer, M., M. Miller, J. Richwine, K. Duckworth, L. Racz, M. Grimaila, M. Magnuson , S. Willison , and R. Phillips. Pulsed and Continuous UV LED Reactor for Water Treatment.   Aqua - Journal of Water Supply Research and Technology, International Water Supply Association (London, England). Blackwell Publishing, Malden, MA, USA,  1-75, (2016).",
             "distribution": [
                 {
-                    "title": "Dataset for sn0q.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/317/Dataset%20for%20sn0q.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Dataset for sn0q.xlsx"
                 }
             ],
+            "identifier": "A-sn0q-317",
+            "keyword": [
+                "Ultraviolet",
+                "advanced oxidation process",
+                "light emitting diode",
+                "reactor design"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2014-10-01",
-            "references": null,
+            "programCode": [
+                "020:060"
+            ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
                 "subOrganizationOf": {
@@ -37231,19 +37227,27 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": null,
+            "rights": null,
+            "title": "Pulsed and Continuous UV LED Reactor for Water Treatment"
         },
         {
-            "title": "Chemical agent recoveries",
-            "description": "Dataset shows the calculation of reported decontamination efficacies from the raw data (i.e., measured amount of chemical recovered from test coupons and positive controls) to actual decontamination efficacy for all chemicals and decontaminants. \n\nThis dataset is associated with the following publication:\nOudejans , L., J. O'Kelly, A. Evans, B. Barbara Wyrzykowska-Ceradini, A. Toauati, D. Tabor , and E. Snyder. Efficacy of decontaminant solutions for remediation on TICs on PPE materials.   JOURNAL OF HAZARDOUS MATERIALS. Elsevier Science Ltd, New York, NY, USA,  1-5, (2016).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
+            "contactPoint": {
+                "fn": "Lukas Oudejans",
+                "hasEmail": "mailto:oudejans.lukas@epa.gov"
+            },
+            "description": "Dataset shows the calculation of reported decontamination efficacies from the raw data (i.e., measured amount of chemical recovered from test coupons and positive controls) to actual decontamination efficacy for all chemicals and decontaminants. \n\nThis dataset is associated with the following publication:\nOudejans , L., J. O'Kelly, A. Evans, B. Barbara Wyrzykowska-Ceradini, A. Toauati, D. Tabor , and E. Snyder. Efficacy of decontaminant solutions for remediation on TICs on PPE materials.   JOURNAL OF HAZARDOUS MATERIALS. Elsevier Science Ltd, New York, NY, USA,  1-5, (2016).",
+            "distribution": [
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/217/Recovery%20data%20PPE%20decon%20w%20TICs.xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Recovery data PPE decon w TICs.xlsx"
+                }
             ],
             "identifier": "A-8sfg-217",
             "keyword": [
@@ -37255,19 +37259,11 @@
                 "toxic industrial chemical",
                 "chemical warfare agent"
             ],
-            "contactPoint": {
-                "fn": "Lukas Oudejans",
-                "hasEmail": "mailto:oudejans.lukas@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "Recovery data PPE decon w TICs.xlsx",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/217/Recovery%20data%20PPE%20decon%20w%20TICs.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2016-08-20",
-            "references": null,
+            "programCode": [
+                "020:000"
+            ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
                 "subOrganizationOf": {
@@ -37276,19 +37272,27 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": null,
+            "rights": null,
+            "title": "Chemical agent recoveries"
         },
         {
-            "title": "Diurnal Ensemble Surface Meteorology Statistics",
-            "description": "Excel file containing diurnal ensemble statistics of 2-m temperature, 2-m mixing ratio and 10-m wind speed. This Excel file contains figures for Figure 2 in the paper and worksheets containing all statistics for the 14 members of the ensemble and a base simulation. \n\nThis dataset is associated with the following publication:\nGilliam , R., C. Hogrefe , J. Godowitch, S. Napelenok , R. Mathur , and S.T. Rao. Impact of inherent meteorology uncertainty on air quality model predictions.   JOURNAL OF GEOPHYSICAL RESEARCH-ATMOSPHERES. American Geophysical Union, Washington, DC, USA, 120(23): 12,259\u201312,280, (2015).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:094"
+            "contactPoint": {
+                "fn": "Robert Gilliam",
+                "hasEmail": "mailto:gilliam.robert@epa.gov"
+            },
+            "description": "Excel file containing diurnal ensemble statistics of 2-m temperature, 2-m mixing ratio and 10-m wind speed. This Excel file contains figures for Figure 2 in the paper and worksheets containing all statistics for the 14 members of the ensemble and a base simulation. \n\nThis dataset is associated with the following publication:\nGilliam , R., C. Hogrefe , J. Godowitch, S. Napelenok , R. Mathur , and S.T. Rao. Impact of inherent meteorology uncertainty on air quality model predictions.   JOURNAL OF GEOPHYSICAL RESEARCH-ATMOSPHERES. American Geophysical Union, Washington, DC, USA, 120(23): 12,259\u201312,280, (2015).",
+            "distribution": [
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/369/ENS_WRF_Stats_June2011.V2.xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "ENS_WRF_Stats_June2011.V2.xlsx"
+                }
             ],
             "identifier": "A-6q5f-369",
             "keyword": [
@@ -37305,20 +37309,10 @@
                 "WRF-CMAQ",
                 "Ozone"
             ],
-            "contactPoint": {
-                "fn": "Robert Gilliam",
-                "hasEmail": "mailto:gilliam.robert@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "ENS_WRF_Stats_June2011.V2.xlsx",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/369/ENS_WRF_Stats_June2011.V2.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2012-11-15",
-            "references": [
-                "https://doi.org/10.1002/2015jd023674"
+            "programCode": [
+                "020:094"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -37328,37 +37322,37 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1002/2015jd023674"
+            ],
+            "rights": null,
+            "title": "Diurnal Ensemble Surface Meteorology Statistics"
         },
         {
-            "title": "Linking high resolution mass spectrometry data with exposure and toxicity forecasts to advance high-throughput environmental monitoring",
-            "description": "There is a growing need in the field of exposure science for monitoring methods that rapidly screen environmental media for suspect contaminants. Measurement and analysis platforms, based on high resolution mass spectrometry (HRMS), now exist to meet this need. Here we describe results of a study that links HRMS data with exposure predictions from the U.S. EPA's ExpoCast\u2122 program and in vitro bioassay data from the U.S. interagency Tox21 consortium. Vacuum dust samples were collected from 56 households across the U.S. as part of the American Healthy Homes Survey (AHHS). Sample extracts were analyzed using liquid chromatography time-of-flight mass spectrometry (LC\u2013TOF/MS) with electrospray ionization. On average, approximately 2000 molecular features were identified per sample (based on accurate mass) in negative ion mode, and 3000 in positive ion mode. Exact mass, isotope distribution, and isotope spacing were used to match molecular features with a unique listing of chemical formulas extracted from EPA's Distributed Structure-Searchable Toxicity (DSSTox) database. A total of 978 DSSTox formulas were consistent with the dust LC\u2013TOF/molecular feature data (match score \u2265 90); these formulas mapped to 3228 possible chemicals in the database. Correct assignment of a unique chemical to a given formula required additional validation steps. Each suspect chemical was prioritized for follow-up confirmation using abundance and detection frequency results, along with exposure and bioactivity estimates from ExpoCast and Tox21, respectively. Chemicals with elevated exposure and/or toxicity potential were further examined using a mixture of 100 chemical standards. A total of 33 chemicals were confirmed present in the dust samples by formula and retention time match; nearly half of these do not appear to have been associated with house dust in the published literature. Chemical matches found in at least 10 of the 56 dust samples include Piperine, N,N-Diethyl-m-toluamide (DEET), Triclocarban, Diethyl phthalate (DEP), Propylparaben, Methylparaben, Tris(1,3-dichloro-2-propyl)phosphate (TDCPP), and Nicotine. This study demonstrates a novel suspect screening methodology to prioritize chemicals of interest for subsequent targeted analysis. The methods described here rely on strategic integration of available public resources and should be considered in future non-targeted and suspect screening assessments of environmental and biological media. \n\nThis dataset is associated with the following publication:\nRager, J.E., M. Strynar , S. Liang, R.L. McMahen, A. Richard , C.M. Grukle, J. Wambaugh , K. Isaacs , R. Judson , A. Williams , and J. Sobus. Linking high resolution mass spectrometry data with exposure and toxicity forecasts to advance high-throughput environmental monitoring.   ENVIRONMENT INTERNATIONAL. Elsevier Science Ltd, New York, NY, USA, 88: 269-280, (2016).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:095"
-            ],
-            "identifier": "A-dbs5-231",
-            "keyword": [
-                "Non-targeted; Suspect screening; Exposome; ExpoCast; ToxCast; Dust"
-            ],
             "contactPoint": {
                 "fn": "Jon Sobus",
                 "hasEmail": "mailto:sobus.jon@epa.gov"
             },
+            "description": "There is a growing need in the field of exposure science for monitoring methods that rapidly screen environmental media for suspect contaminants. Measurement and analysis platforms, based on high resolution mass spectrometry (HRMS), now exist to meet this need. Here we describe results of a study that links HRMS data with exposure predictions from the U.S. EPA's ExpoCast\u2122 program and in vitro bioassay data from the U.S. interagency Tox21 consortium. Vacuum dust samples were collected from 56 households across the U.S. as part of the American Healthy Homes Survey (AHHS). Sample extracts were analyzed using liquid chromatography time-of-flight mass spectrometry (LC\u2013TOF/MS) with electrospray ionization. On average, approximately 2000 molecular features were identified per sample (based on accurate mass) in negative ion mode, and 3000 in positive ion mode. Exact mass, isotope distribution, and isotope spacing were used to match molecular features with a unique listing of chemical formulas extracted from EPA's Distributed Structure-Searchable Toxicity (DSSTox) database. A total of 978 DSSTox formulas were consistent with the dust LC\u2013TOF/molecular feature data (match score \u2265 90); these formulas mapped to 3228 possible chemicals in the database. Correct assignment of a unique chemical to a given formula required additional validation steps. Each suspect chemical was prioritized for follow-up confirmation using abundance and detection frequency results, along with exposure and bioactivity estimates from ExpoCast and Tox21, respectively. Chemicals with elevated exposure and/or toxicity potential were further examined using a mixture of 100 chemical standards. A total of 33 chemicals were confirmed present in the dust samples by formula and retention time match; nearly half of these do not appear to have been associated with house dust in the published literature. Chemical matches found in at least 10 of the 56 dust samples include Piperine, N,N-Diethyl-m-toluamide (DEET), Triclocarban, Diethyl phthalate (DEP), Propylparaben, Methylparaben, Tris(1,3-dichloro-2-propyl)phosphate (TDCPP), and Nicotine. This study demonstrates a novel suspect screening methodology to prioritize chemicals of interest for subsequent targeted analysis. The methods described here rely on strategic integration of available public resources and should be considered in future non-targeted and suspect screening assessments of environmental and biological media. \n\nThis dataset is associated with the following publication:\nRager, J.E., M. Strynar , S. Liang, R.L. McMahen, A. Richard , C.M. Grukle, J. Wambaugh , K. Isaacs , R. Judson , A. Williams , and J. Sobus. Linking high resolution mass spectrometry data with exposure and toxicity forecasts to advance high-throughput environmental monitoring.   ENVIRONMENT INTERNATIONAL. Elsevier Science Ltd, New York, NY, USA, 88: 269-280, (2016).",
             "distribution": [
                 {
-                    "title": "https://www.sciencedirect.com/science/article/pii/S0160412015301112",
-                    "accessURL": "https://www.sciencedirect.com/science/article/pii/S0160412015301112"
+                    "accessURL": "https://www.sciencedirect.com/science/article/pii/S0160412015301112",
+                    "title": "https://www.sciencedirect.com/science/article/pii/S0160412015301112"
                 }
             ],
+            "identifier": "A-dbs5-231",
+            "keyword": [
+                "Non-targeted; Suspect screening; Exposome; ExpoCast; ToxCast; Dust"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2015-12-15",
-            "references": [
-                "https://doi.org/10.1016/j.envint.2015.12.008"
+            "programCode": [
+                "020:095"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -37368,57 +37362,59 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.envint.2015.12.008"
+            ],
+            "rights": null,
+            "title": "Linking high resolution mass spectrometry data with exposure and toxicity forecasts to advance high-throughput environmental monitoring"
         },
         {
-            "title": "Biomarker analysis of liver cells exposed to surfactant-wrapped and oxidized multi-walled carbon nanotubes (MWCNTs)",
-            "description": "Carbon nanotubes (CNTs) have great potential in industrial, consumer, and mechanical applications, based partly on their unique structural, optical and electronic properties. CNTs are commonly oxidized or treated with surfactants to facilitate aqueous solution processing, and these CNT surface modifications also increase possible human and ecological exposures to nanoparticle-contaminated waters. To determine the exposure outcomes of oxidized and surfactant-wrapped multiwalled carbon nanotubes (MWCNTs) on biochemical processes, metabolomics based profiling of human liver cells (C3A) was utilized. Cells were exposed to 0, 10, or 100 ng/mL of MWCNTs for 24 and 48 hr. MWCNT particle size distribution, charge, and aggregation were monitored concurrently during exposures. Following MWCNT exposure, cellular metabolites were extracted, lyophilized, and buffered for 1H NMR analysis. Acquired spectra were subjected to both multivariate and univariate analysis to determine the consequences of nanotube exposure on the metabolite profile of C3A cells. Resulting scores plots illustrated temporal and dose-dependent metabolite responses to all MWCNTs tested. Loadings plots coupled with t-test filtered spectra identified metabolites of interest. XPS analysis revealed the presence of hydroxyl and carboxyl functionalities on both MWCNTs surfaces. Metal content analysis by ICP-AES indicated that the total mass concentration of the potentially toxic impurities in the exposure experiments were extremely low (i.e. [Ni] \u2264 2 \u00d7 10\u221210 g/mL). Preliminary data suggested that MWCNT exposure causes perturbations in biochemical processes involved in cellular oxidation as well as fluxes in amino acid metabolism and fatty acid synthesis. Dose-response trajectories were apparent and spectral peaks related to both dose and MWCNT dispersion methodologies were determined. Correlations of the significant changes in metabolites will help to identify potential biomarkers associated with carbonaceous nanoparticle exposure. \n\nThis dataset is associated with the following publication:\nHenderson, M., D. Bouchard, X. Chang, S. Al-Abed, and Q. Teng. Biomarker analysis of liver cells exposed to surfactant-wrapped and oxidized multi-walled carbon nanotubes (MWCNTs).   SCIENCE OF THE TOTAL ENVIRONMENT. Elsevier BV, AMSTERDAM,  NETHERLANDS, 565: 777\u2013786, (2016).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:097"
-            ],
-            "identifier": "A-j104-344",
-            "keyword": [
-                "carbon nanoparticles",
-                "carbon nanotubes",
-                "biomarker profiling",
-                "metabolomics",
-                "ecotoxicity"
-            ],
             "contactPoint": {
                 "fn": "William Henderson",
                 "hasEmail": "mailto:henderson.matt@epa.gov"
             },
+            "describedBy": "https://pasteur.epa.gov/uploads/344/documents/HendersonWilliam_A-j104_DataDictionary_20160916.docx",
+            "describedByType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+            "description": "Carbon nanotubes (CNTs) have great potential in industrial, consumer, and mechanical applications, based partly on their unique structural, optical and electronic properties. CNTs are commonly oxidized or treated with surfactants to facilitate aqueous solution processing, and these CNT surface modifications also increase possible human and ecological exposures to nanoparticle-contaminated waters. To determine the exposure outcomes of oxidized and surfactant-wrapped multiwalled carbon nanotubes (MWCNTs) on biochemical processes, metabolomics based profiling of human liver cells (C3A) was utilized. Cells were exposed to 0, 10, or 100 ng/mL of MWCNTs for 24 and 48 hr. MWCNT particle size distribution, charge, and aggregation were monitored concurrently during exposures. Following MWCNT exposure, cellular metabolites were extracted, lyophilized, and buffered for 1H NMR analysis. Acquired spectra were subjected to both multivariate and univariate analysis to determine the consequences of nanotube exposure on the metabolite profile of C3A cells. Resulting scores plots illustrated temporal and dose-dependent metabolite responses to all MWCNTs tested. Loadings plots coupled with t-test filtered spectra identified metabolites of interest. XPS analysis revealed the presence of hydroxyl and carboxyl functionalities on both MWCNTs surfaces. Metal content analysis by ICP-AES indicated that the total mass concentration of the potentially toxic impurities in the exposure experiments were extremely low (i.e. [Ni] \u2264 2 \u00d7 10\u221210 g/mL). Preliminary data suggested that MWCNT exposure causes perturbations in biochemical processes involved in cellular oxidation as well as fluxes in amino acid metabolism and fatty acid synthesis. Dose-response trajectories were apparent and spectral peaks related to both dose and MWCNT dispersion methodologies were determined. Correlations of the significant changes in metabolites will help to identify potential biomarkers associated with carbonaceous nanoparticle exposure. \n\nThis dataset is associated with the following publication:\nHenderson, M., D. Bouchard, X. Chang, S. Al-Abed, and Q. Teng. Biomarker analysis of liver cells exposed to surfactant-wrapped and oxidized multi-walled carbon nanotubes (MWCNTs).   SCIENCE OF THE TOTAL ENVIRONMENT. Elsevier BV, AMSTERDAM,  NETHERLANDS, 565: 777\u2013786, (2016).",
             "distribution": [
                 {
-                    "title": "ohmwntc3a24hr.csv",
                     "downloadURL": "https://pasteur.epa.gov/uploads/344/ohmwntc3a24hr.csv",
-                    "mediaType": "application/vnd.ms-excel"
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "ohmwntc3a24hr.csv"
                 },
                 {
-                    "title": "ohmwntc3a48hr.csv",
                     "downloadURL": "https://pasteur.epa.gov/uploads/344/ohmwntc3a48hr.csv",
-                    "mediaType": "application/vnd.ms-excel"
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "ohmwntc3a48hr.csv"
                 },
                 {
-                    "title": "sdsmwntc3a24h.csv",
                     "downloadURL": "https://pasteur.epa.gov/uploads/344/sdsmwntc3a24h.csv",
-                    "mediaType": "application/vnd.ms-excel"
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "sdsmwntc3a24h.csv"
                 },
                 {
-                    "title": "sdsmwntc3a48hr.csv",
                     "downloadURL": "https://pasteur.epa.gov/uploads/344/sdsmwntc3a48hr.csv",
-                    "mediaType": "application/vnd.ms-excel"
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "sdsmwntc3a48hr.csv"
                 }
             ],
+            "identifier": "A-j104-344",
+            "keyword": [
+                "carbon nanoparticles",
+                "carbon nanotubes",
+                "biomarker profiling",
+                "metabolomics",
+                "ecotoxicity"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2015-12-04",
-            "references": [
-                "https://doi.org/10.1016/j.scitotenv.2016.05.025"
+            "programCode": [
+                "020:097"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -37429,43 +37425,41 @@
                     }
                 }
             },
-            "describedBy": "https://pasteur.epa.gov/uploads/344/documents/HendersonWilliam_A-j104_DataDictionary_20160916.docx",
-            "describedByType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
+            "references": [
+                "https://doi.org/10.1016/j.scitotenv.2016.05.025"
+            ],
+            "rights": null,
+            "title": "Biomarker analysis of liver cells exposed to surfactant-wrapped and oxidized multi-walled carbon nanotubes (MWCNTs)"
         },
         {
-            "title": "Anaerobic Toxicity of Cationic Silver Nanoparticles",
-            "description": "Toxicity data for the impact of nano-silver on anaerobic degradation. \n\nThis dataset is associated with the following publication:\nGitipour, A., S. Thiel, K. Scheckel, and T. Tolaymat. Anaerobic Toxicity of Cationic Silver Nanoparticles.  D. Barcelo Culleres, and J. Gan  SCIENCE OF THE TOTAL ENVIRONMENT. Elsevier BV, AMSTERDAM,  NETHERLANDS, 557: 363-368, (2016).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:095"
-            ],
-            "identifier": "A-p5j7-301",
-            "keyword": [
-                "Nanoparticles",
-                "Silver",
-                "toxicity",
-                "cationic",
-                "anaerobic"
-            ],
             "contactPoint": {
                 "fn": "Thabet Tolaymat",
                 "hasEmail": "mailto:tolaymat.thabet@epa.gov"
             },
+            "description": "Toxicity data for the impact of nano-silver on anaerobic degradation. \n\nThis dataset is associated with the following publication:\nGitipour, A., S. Thiel, K. Scheckel, and T. Tolaymat. Anaerobic Toxicity of Cationic Silver Nanoparticles.  D. Barcelo Culleres, and J. Gan  SCIENCE OF THE TOTAL ENVIRONMENT. Elsevier BV, AMSTERDAM,  NETHERLANDS, 557: 363-368, (2016).",
             "distribution": [
                 {
-                    "title": "AN.TOX (data).xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/301/AN.TOX%20%28data%29.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "AN.TOX (data).xlsx"
                 }
             ],
+            "identifier": "A-p5j7-301",
+            "keyword": [
+                "Nanoparticles",
+                "Silver",
+                "toxicity",
+                "cationic",
+                "anaerobic"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2015-12-25",
-            "references": [
-                "https://doi.org/10.1016/j.scitotenv.2016.02.190"
+            "programCode": [
+                "020:095"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -37475,50 +37469,50 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.scitotenv.2016.02.190"
+            ],
+            "rights": null,
+            "title": "Anaerobic Toxicity of Cationic Silver Nanoparticles"
         },
         {
-            "title": "Molecular Detection of Legionella spp. and their associations with Mycobacterium spp., Pseudomonas aeruginosa and amoeba hosts in a drinking water distribution system ",
-            "description": "Quantity of Legionella spp., Mycobacterium spp., Acanthamoeba,Vermamoeba vermiformis and Pseudomonas aeruginosa were estimated using qPCR methods. \n\nThis dataset is associated with the following publication:\nLu , J., I. Struewing, E. Vereen, A.E. Kirby, K. Levy, C. Moe, and N. Ashbolt. Molecular detection of Legionella spp. and their associations with Mycobacterium spp., Pseudomonas aeruginosa and amoeba hosts in a drinking water distribution system (Journal Article).   JOURNAL OF APPLIED MICROBIOLOGY. Blackwell Publishing, Malden, MA, USA, 120(2): 509-521, (2016).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "A-rv1r-292",
-            "keyword": [
-                "legionella",
-                "opportunistic parthogens",
-                "Drinking water distribution system",
-                "qPCR",
-                "opportunistic pathogen",
-                "drinking water",
-                "molecular detection",
-                "sequence"
-            ],
             "contactPoint": {
                 "fn": "Jingrang Lu",
                 "hasEmail": "mailto:lu.jingrang@epa.gov"
             },
+            "description": "Quantity of Legionella spp., Mycobacterium spp., Acanthamoeba,Vermamoeba vermiformis and Pseudomonas aeruginosa were estimated using qPCR methods. \n\nThis dataset is associated with the following publication:\nLu , J., I. Struewing, E. Vereen, A.E. Kirby, K. Levy, C. Moe, and N. Ashbolt. Molecular detection of Legionella spp. and their associations with Mycobacterium spp., Pseudomonas aeruginosa and amoeba hosts in a drinking water distribution system (Journal Article).   JOURNAL OF APPLIED MICROBIOLOGY. Blackwell Publishing, Malden, MA, USA, 120(2): 509-521, (2016).",
             "distribution": [
                 {
-                    "title": "Data dictionary_LegionellaDistributionSystem JAM.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/292/Data%20dictionary_LegionellaDistributionSystem%20JAM.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Data dictionary_LegionellaDistributionSystem JAM.xlsx"
                 },
                 {
-                    "title": "DataSet_LegionellaDistributionSystem JAM.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/292/DataSet_LegionellaDistributionSystem%20JAM.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "DataSet_LegionellaDistributionSystem JAM.xlsx"
                 }
             ],
+            "identifier": "A-rv1r-292",
+            "keyword": [
+                "legionella",
+                "opportunistic parthogens",
+                "Drinking water distribution system",
+                "qPCR",
+                "opportunistic pathogen",
+                "drinking water",
+                "molecular detection",
+                "sequence"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2016-09-09",
-            "references": [
-                "https://doi.org/10.1111/jam.12996"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -37528,19 +37522,28 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1111/jam.12996"
+            ],
+            "rights": null,
+            "title": "Molecular Detection of Legionella spp. and their associations with Mycobacterium spp., Pseudomonas aeruginosa and amoeba hosts in a drinking water distribution system "
         },
         {
-            "title": "CERAPP: Collaborative Estrogen Receptor Activity Prediction Project",
-            "description": "Data from a large-scale modeling project called CERAPP (Collaborative Estrogen Receptor Activity Prediction Project) demonstrating using predictive computational models on high-throughput screening data to screen thousands of chemicals against the estrogen receptor. \n\nThis dataset is associated with the following publication:\nMansouri , K., A. Abdelaziz, A. Rybacka, A. Roncaglioni, A. Tropsha, A. Varnek, A. Zakharov, A. Worth, A. Richard , C. Grulke , D. Trisciuzzi, D. Fourches, D. Horvath, E. Benfenati , E. Muratov, E.B. Wedebye, F. Grisoni, G.F. Mangiatordi, G.M. Incisivo, H. Hong, H.W. Ng, I.V. Tetko, I. Balabin, J. Kancherla , J. Shen, J. Burton, M. Nicklaus, M. Cassotti, N.G. Nikolov, O. Nicolotti, P.L. Andersson, Q. Zang, R. Politi, R.D. Beger , R. Todeschini, R. Huang, S. Farag, S.A. Rosenberg, S. Slavov, X. Hu, and R. Judson. (Environmental Health Perspectives)  CERAPP: Collaborative Estrogen Receptor Activity Prediction Project.   ENVIRONMENTAL HEALTH PERSPECTIVES. National Institute of Environmental Health Sciences (NIEHS), Research Triangle Park, NC, USA,  1-49, (2016).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:095"
+            "contactPoint": {
+                "fn": "Ann Richard",
+                "hasEmail": "mailto:richard.ann@epa.gov"
+            },
+            "description": "Data from a large-scale modeling project called CERAPP (Collaborative Estrogen Receptor Activity Prediction Project) demonstrating using predictive computational models on high-throughput screening data to screen thousands of chemicals against the estrogen receptor. \n\nThis dataset is associated with the following publication:\nMansouri , K., A. Abdelaziz, A. Rybacka, A. Roncaglioni, A. Tropsha, A. Varnek, A. Zakharov, A. Worth, A. Richard , C. Grulke , D. Trisciuzzi, D. Fourches, D. Horvath, E. Benfenati , E. Muratov, E.B. Wedebye, F. Grisoni, G.F. Mangiatordi, G.M. Incisivo, H. Hong, H.W. Ng, I.V. Tetko, I. Balabin, J. Kancherla , J. Shen, J. Burton, M. Nicklaus, M. Cassotti, N.G. Nikolov, O. Nicolotti, P.L. Andersson, Q. Zang, R. Politi, R.D. Beger , R. Todeschini, R. Huang, S. Farag, S.A. Rosenberg, S. Slavov, X. Hu, and R. Judson. (Environmental Health Perspectives)  CERAPP: Collaborative Estrogen Receptor Activity Prediction Project.   ENVIRONMENTAL HEALTH PERSPECTIVES. National Institute of Environmental Health Sciences (NIEHS), Research Triangle Park, NC, USA,  1-49, (2016).",
+            "distribution": [
+                {
+                    "accessURL": "https://gaftp.epa.gov/COMPTOX/Sustainable_Chemistry_Data/CERAPP_QSAR_Models/",
+                    "title": "https://gaftp.epa.gov/COMPTOX/Sustainable_Chemistry_Data/CERAPP_QSAR_Models/"
+                }
             ],
             "identifier": "A-6t1n-312",
             "keyword": [
@@ -37552,19 +37555,10 @@
                 "Chemistry Dashboard",
                 "Read Across"
             ],
-            "contactPoint": {
-                "fn": "Ann Richard",
-                "hasEmail": "mailto:richard.ann@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "https://gaftp.epa.gov/COMPTOX/Sustainable_Chemistry_Data/CERAPP_QSAR_Models/",
-                    "accessURL": "https://gaftp.epa.gov/COMPTOX/Sustainable_Chemistry_Data/CERAPP_QSAR_Models/"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2016-07-01",
-            "references": [
-                "https://doi.org/10.1289/ehp.1510267"
+            "programCode": [
+                "020:095"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -37574,19 +37568,28 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1289/ehp.1510267"
+            ],
+            "rights": null,
+            "title": "CERAPP: Collaborative Estrogen Receptor Activity Prediction Project"
         },
         {
-            "title": "Evaluation of food-relevant chemicals in the ToxCast high-throughput screening program",
-            "description": "Thousands of chemicals are directly added to or come in contact with food, many of which have undergone little to no toxicological evaluation. The landscape of the food-relevant chemical universe was evaluated using cheminformatics, and subsequently the bioactivity of food-relevant chemicals across the publicly available ToxCast highthroughput screening program was assessed. In total, 8659 food-relevant chemicals were compiled including direct food additives, food contact substances, and pesticides. Of these food-relevant chemicals, 4719 had curated structure definition files amenable to defining chemical fingerprints, which were used to cluster chemicals using a selforganizing map approach. Pesticides, and direct food additives clustered apart from one another with food contact substances generally in between, supporting that these categories not only reflect different uses but also distinct chemistries. Subsequently, 1530 food-relevant chemicals were identified in ToxCast comprising 616 direct food additives, 371 food contact substances, and 543 pesticides. Bioactivity across ToxCast was filtered for cytotoxicity to identify selective chemical effects. Initiating analyses from strictly chemical-based methodology or bioactivity/cytotoxicity-driven evaluation presents unbiased approaches for prioritizing chemicals. Although bioactivity in vitro is not necessarily predictive of adverse effects in vivo, these data provide insight into chemical properties and cellular targets through which foodrelevant chemicals elicit bioactivity. \n\nThis dataset is associated with the following publication:\nKarmaus , A., D. Filer , M. Martin , and K. Houck. (FOOD AND CHEMICAL TOXICOLOGY) Evaluation of food-relevant chemicals in the ToxCast high-throughput screening program.   FOOD AND CHEMICAL TOXICOLOGY. Elsevier Science Ltd, New York, NY, USA, 92: 188-196, (2016).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:095"
+            "contactPoint": {
+                "fn": "Keith Houck",
+                "hasEmail": "mailto:houck.keith@epa.gov"
+            },
+            "description": "Thousands of chemicals are directly added to or come in contact with food, many of which have undergone little to no toxicological evaluation. The landscape of the food-relevant chemical universe was evaluated using cheminformatics, and subsequently the bioactivity of food-relevant chemicals across the publicly available ToxCast highthroughput screening program was assessed. In total, 8659 food-relevant chemicals were compiled including direct food additives, food contact substances, and pesticides. Of these food-relevant chemicals, 4719 had curated structure definition files amenable to defining chemical fingerprints, which were used to cluster chemicals using a selforganizing map approach. Pesticides, and direct food additives clustered apart from one another with food contact substances generally in between, supporting that these categories not only reflect different uses but also distinct chemistries. Subsequently, 1530 food-relevant chemicals were identified in ToxCast comprising 616 direct food additives, 371 food contact substances, and 543 pesticides. Bioactivity across ToxCast was filtered for cytotoxicity to identify selective chemical effects. Initiating analyses from strictly chemical-based methodology or bioactivity/cytotoxicity-driven evaluation presents unbiased approaches for prioritizing chemicals. Although bioactivity in vitro is not necessarily predictive of adverse effects in vivo, these data provide insight into chemical properties and cellular targets through which foodrelevant chemicals elicit bioactivity. \n\nThis dataset is associated with the following publication:\nKarmaus , A., D. Filer , M. Martin , and K. Houck. (FOOD AND CHEMICAL TOXICOLOGY) Evaluation of food-relevant chemicals in the ToxCast high-throughput screening program.   FOOD AND CHEMICAL TOXICOLOGY. Elsevier Science Ltd, New York, NY, USA, 92: 188-196, (2016).",
+            "distribution": [
+                {
+                    "accessURL": "https://gaftp.epa.gov/COMPTOX/NCCT_Publication_Data/Houck_Karmaus/ToxCast_Food_Relevant/",
+                    "title": "https://gaftp.epa.gov/COMPTOX/NCCT_Publication_Data/Houck_Karmaus/ToxCast_Food_Relevant/"
+                }
             ],
             "identifier": "A-x0kx-328",
             "keyword": [
@@ -37600,19 +37603,10 @@
                 "ToxCast",
                 "computational toxicology"
             ],
-            "contactPoint": {
-                "fn": "Keith Houck",
-                "hasEmail": "mailto:houck.keith@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "https://gaftp.epa.gov/COMPTOX/NCCT_Publication_Data/Houck_Karmaus/ToxCast_Food_Relevant/",
-                    "accessURL": "https://gaftp.epa.gov/COMPTOX/NCCT_Publication_Data/Houck_Karmaus/ToxCast_Food_Relevant/"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2016-06-30",
-            "references": [
-                "https://doi.org/10.1016/j.fct.2016.04.012"
+            "programCode": [
+                "020:095"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -37622,19 +37616,28 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.fct.2016.04.012"
+            ],
+            "rights": null,
+            "title": "Evaluation of food-relevant chemicals in the ToxCast high-throughput screening program"
         },
         {
-            "title": "Systems Toxicology of Male Reproductive Development: Profiling 774 Chemicals for Molecular Targets and Adverse Outcomes",
-            "description": "Background: Trends in male reproductive health have been reported for increased rates of testicular germ cell tumors, low semen quality, cryptorchidism, and hypospadias, which have been associated with prenatal environmental chemical exposure based on human and animal studies.\n\nObjective: In the present study we aimed to identify significant correlations between environmental chemicals, molecular targets, and adverse outcomes across a broad chemical landscape with emphasis on developmental toxicity of the male reproductive system.\n\nMethods: We used U.S. EPA\u2019s animal study database (ToxRefDB) and a comprehensive literature analysis to identify 774 chemicals that have been evaluated for adverse effects on male reproductive parameters, and then used U.S. EPA\u2019s in vitro high-throughput screening (HTS) database (ToxCastDB) to profile their bioactivity across approximately 800 molecular and cellular features. \n\nResults: A phenotypic hierarchy of testicular atrophy, sperm effects, tumors, and malformations, a composite resembling the human testicular dysgenesis syndrome (TDS) hypothesis, was observed in 281 chemicals. A subset of 54 chemicals with male developmental consequences had in vitro bioactivity on molecular targets that could be condensed into 156 gene annotations in a bipartite network. \n\nConclusion: Computational modeling of available in vivo and in vitro data for chemicals that produce adverse effects on male reproductive end points revealed a phenotypic hierarchy across animal studies consistent with the human TDS hypothesis. We confirmed the known role of estrogen and androgen signaling pathways in rodent TDS, and importantly, broadened the list of molecular targets to include retinoic acid signaling, vascular remodeling proteins, G-protein coupled receptors (GPCRs), and cytochrome P450s. \n\nThis dataset is associated with the following publication:\nLeung , M., J. Phuong , N. Baker , N. Sipes , G. Klinefelter , M. Martin , K. McLaurin, W. Setzer , S. Darney , R. Judson , and T. Knudsen. (ENVIRONMENTAL HEALTH PERSPECTIVES) Systems Toxicology of Male Reproductive Development: Profiling 774 Chemicals for Molecular Targets and Adverse Outcomes.   ENVIRONMENTAL HEALTH PERSPECTIVES. National Institute of Environmental Health Sciences (NIEHS), Research Triangle Park, NC, USA,  1-47, (2015).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:095"
+            "contactPoint": {
+                "fn": "Thomas Knudsen",
+                "hasEmail": "mailto:knudsen.thomas@epa.gov"
+            },
+            "description": "Background: Trends in male reproductive health have been reported for increased rates of testicular germ cell tumors, low semen quality, cryptorchidism, and hypospadias, which have been associated with prenatal environmental chemical exposure based on human and animal studies.\n\nObjective: In the present study we aimed to identify significant correlations between environmental chemicals, molecular targets, and adverse outcomes across a broad chemical landscape with emphasis on developmental toxicity of the male reproductive system.\n\nMethods: We used U.S. EPA\u2019s animal study database (ToxRefDB) and a comprehensive literature analysis to identify 774 chemicals that have been evaluated for adverse effects on male reproductive parameters, and then used U.S. EPA\u2019s in vitro high-throughput screening (HTS) database (ToxCastDB) to profile their bioactivity across approximately 800 molecular and cellular features. \n\nResults: A phenotypic hierarchy of testicular atrophy, sperm effects, tumors, and malformations, a composite resembling the human testicular dysgenesis syndrome (TDS) hypothesis, was observed in 281 chemicals. A subset of 54 chemicals with male developmental consequences had in vitro bioactivity on molecular targets that could be condensed into 156 gene annotations in a bipartite network. \n\nConclusion: Computational modeling of available in vivo and in vitro data for chemicals that produce adverse effects on male reproductive end points revealed a phenotypic hierarchy across animal studies consistent with the human TDS hypothesis. We confirmed the known role of estrogen and androgen signaling pathways in rodent TDS, and importantly, broadened the list of molecular targets to include retinoic acid signaling, vascular remodeling proteins, G-protein coupled receptors (GPCRs), and cytochrome P450s. \n\nThis dataset is associated with the following publication:\nLeung , M., J. Phuong , N. Baker , N. Sipes , G. Klinefelter , M. Martin , K. McLaurin, W. Setzer , S. Darney , R. Judson , and T. Knudsen. (ENVIRONMENTAL HEALTH PERSPECTIVES) Systems Toxicology of Male Reproductive Development: Profiling 774 Chemicals for Molecular Targets and Adverse Outcomes.   ENVIRONMENTAL HEALTH PERSPECTIVES. National Institute of Environmental Health Sciences (NIEHS), Research Triangle Park, NC, USA,  1-47, (2015).",
+            "distribution": [
+                {
+                    "accessURL": "https://gaftp.epa.gov/comptox/NCCT_Publication_Data/Knudsen/Virtual_Tissues_Male_Repro_Tox/Leung%20et%20al.%202016_EHP/",
+                    "title": "https://gaftp.epa.gov/comptox/NCCT_Publication_Data/Knudsen/Virtual_Tissues_Male_Repro_Tox/Leung%20et%20al.%202016_EHP/"
+                }
             ],
             "identifier": "A-dncw-331",
             "keyword": [
@@ -37645,19 +37648,10 @@
                 "virtual liver",
                 "tipping points"
             ],
-            "contactPoint": {
-                "fn": "Thomas Knudsen",
-                "hasEmail": "mailto:knudsen.thomas@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "https://gaftp.epa.gov/comptox/NCCT_Publication_Data/Knudsen/Virtual_Tissues_Male_Repro_Tox/Leung%20et%20al.%202016_EHP/",
-                    "accessURL": "https://gaftp.epa.gov/comptox/NCCT_Publication_Data/Knudsen/Virtual_Tissues_Male_Repro_Tox/Leung%20et%20al.%202016_EHP/"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2016-07-01",
-            "references": [
-                "https://doi.org/10.1289/ehp.1510385"
+            "programCode": [
+                "020:095"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -37667,20 +37661,24 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1289/ehp.1510385"
+            ],
+            "rights": null,
+            "title": "Systems Toxicology of Male Reproductive Development: Profiling 774 Chemicals for Molecular Targets and Adverse Outcomes"
         },
         {
-            "title": "In vivo and In vitro neurochemical-based assessments of wastewater effluents from the Maumee River area of concern.",
-            "description": "All primary data reported in this paper were generated by non-federal collaborators from the University of Michigan and McGill University. US EPA-ORD personnel collected and supplied water, sediment, and fish tissue samples used in these analyses and contributed to development of the manuscript, however, no data were directly generated by US EPA personnel. This dataset is not publicly accessible because: No EPA data (see comments). It can be accessed through the following means: Data set can be obtained upon request from the corresponding author. Format: n/a. \n\nThis dataset is associated with the following publication:\nArini, A., J. Cavallin , J. Berninger, R. Marfil-Vega, M. Mills , D. Villeneuve , and N. Basu. In vivo and in vitro neurochemical-based assessments of wastewater effluents from the Maumee River area of concern..   SOCIETY OF ENVIRONMENTAL TOXICOLOGY AND CHEMISTRY JOURNAL. Society of Environmental Toxicology and Chemistry, Pensacola, FL, USA, 211: 9-19, (2016).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:095"
-            ],
+            "contactPoint": {
+                "fn": "Daniel Villeneuve",
+                "hasEmail": "mailto:villeneuve.dan@epa.gov"
+            },
+            "description": "All primary data reported in this paper were generated by non-federal collaborators from the University of Michigan and McGill University. US EPA-ORD personnel collected and supplied water, sediment, and fish tissue samples used in these analyses and contributed to development of the manuscript, however, no data were directly generated by US EPA personnel. This dataset is not publicly accessible because: No EPA data (see comments). It can be accessed through the following means: Data set can be obtained upon request from the corresponding author. Format: n/a. \n\nThis dataset is associated with the following publication:\nArini, A., J. Cavallin , J. Berninger, R. Marfil-Vega, M. Mills , D. Villeneuve , and N. Basu. In vivo and in vitro neurochemical-based assessments of wastewater effluents from the Maumee River area of concern..   SOCIETY OF ENVIRONMENTAL TOXICOLOGY AND CHEMISTRY JOURNAL. Society of Environmental Toxicology and Chemistry, Pensacola, FL, USA, 211: 9-19, (2016).",
+            "distribution": [],
             "identifier": "A-4xh3-350",
             "keyword": [
                 "adverse outcome pathway",
@@ -37690,14 +37688,10 @@
                 "Great Lakes Research Initiative",
                 "neuroendocrine"
             ],
-            "contactPoint": {
-                "fn": "Daniel Villeneuve",
-                "hasEmail": "mailto:villeneuve.dan@epa.gov"
-            },
-            "distribution": [],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2015-12-15",
-            "references": [
-                "http://www.sciencedirect.com/science/article/pii/S0269749115302426"
+            "programCode": [
+                "020:095"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -37707,46 +37701,49 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "http://www.sciencedirect.com/science/article/pii/S0269749115302426"
+            ],
+            "rights": null,
+            "title": "In vivo and In vitro neurochemical-based assessments of wastewater effluents from the Maumee River area of concern."
         },
         {
-            "title": "MOD13Q1",
-            "description": "Normalized Difference Vegetation Index (NDVI). \n\nThis dataset is associated with the following publication:\nShao, Y., R. Lunetta , B. Wheeler, J. Iiames , and J. Campbell. An Evaluation of Time-Series Smoothing Algorithms for Landcover Classifications Using MODIS-NDVI Multi-Temporal Data.   REMOTE SENSING OF ENVIRONMENT. Elsevier Science Ltd, New York, NY, USA, 174(0): 258-265, (2016).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:096"
-            ],
-            "identifier": "A-kwhq-353",
-            "keyword": [
-                "MODIS-NDVI",
-                "MODIS-NDVI Smoothing"
-            ],
             "contactPoint": {
                 "fn": "Ross Lunetta",
                 "hasEmail": "mailto:lunetta.ross@epa.gov"
             },
+            "describedBy": "https://modis.gsfc.nasa.gov/",
+            "description": "Normalized Difference Vegetation Index (NDVI). \n\nThis dataset is associated with the following publication:\nShao, Y., R. Lunetta , B. Wheeler, J. Iiames , and J. Campbell. An Evaluation of Time-Series Smoothing Algorithms for Landcover Classifications Using MODIS-NDVI Multi-Temporal Data.   REMOTE SENSING OF ENVIRONMENT. Elsevier Science Ltd, New York, NY, USA, 174(0): 258-265, (2016).",
             "distribution": [
                 {
-                    "title": "Time-Series Smoothing_rse.2016.pdf",
                     "downloadURL": "https://pasteur.epa.gov/uploads/353/Time-Series%20Smoothing_rse.2016.pdf",
-                    "mediaType": "application/pdf"
+                    "mediaType": "application/pdf",
+                    "title": "Time-Series Smoothing_rse.2016.pdf"
                 },
                 {
-                    "title": "https://modis.gsfc.nasa.gov/",
-                    "accessURL": "https://modis.gsfc.nasa.gov/"
+                    "accessURL": "https://modis.gsfc.nasa.gov/",
+                    "title": "https://modis.gsfc.nasa.gov/"
                 },
                 {
-                    "title": "https://nassgeodata.gmu.edu/CropScape/",
-                    "accessURL": "https://nassgeodata.gmu.edu/CropScape/"
+                    "accessURL": "https://nassgeodata.gmu.edu/CropScape/",
+                    "title": "https://nassgeodata.gmu.edu/CropScape/"
                 }
             ],
+            "identifier": "A-kwhq-353",
+            "keyword": [
+                "MODIS-NDVI",
+                "MODIS-NDVI Smoothing"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2015-11-20",
-            "references": null,
+            "programCode": [
+                "020:096"
+            ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
                 "subOrganizationOf": {
@@ -37756,48 +37753,45 @@
                     }
                 }
             },
-            "describedBy": "https://modis.gsfc.nasa.gov/"
+            "references": null,
+            "rights": null,
+            "title": "MOD13Q1"
         },
         {
-            "title": "Assessment of the Bioaccessibility of Micronized Copper Wood on Simulated Stomach Fluid",
-            "description": "The widespread use of copper-treated lumber has increased the potential for human exposure. Moreover, there is a lack of information on the fate and behavior of copper-treated wood particles following oral ingestion. In this study, the in vitro bioaccessibility of copper from copper-treated wood dust in simulated stomach fluid and DI water was determined. Three copper-treated wood products, liquid alkali copper quaternary and two micronized copper quarternary from different manufacturers, were incubated in the extraction media then fractionated by centrifugation and filtration through 0.45 \uf06dm and 10 kDa filters. The copper concentrations from isolated fractions were measured using Inductively Coupled Plasma-Optical Emission Spectrometry (ICP-OES). Total amounts of copper from each wood product were also determined using microwave-assisted acid digestion of dried wood samples and quantification using ICP-OES. The percent in vitro bioaccessible copper was between 83 and 90 % for all treated wood types. However, the percent of copper released in DI water was between 14 and 25 % for all wood products. This data suggests that copper is highly bioaccessible at low pH and may pose a potential human exposure risk upon ingestion. \n\nThis dataset is associated with the following publication:\nSantiago-Rodrigues, L., J.L. Griggs, K. Bradham , C. Nelson , T. Luxton , W. Platten , and K. Rogers. Assessment of the bioaccessibility of micronized copper wood in synthetic stomach fluid.   Environmental Nanotechnology, Monitoring and Management. Elsevier B.V., Amsterdam,  NETHERLANDS, 4: 85-92, (2015).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "A-tx9t-277",
-            "keyword": [
-                "Copper",
-                "Micronized Copper",
-                "Wood",
-                "Bioaccessibility",
-                "Synthetic stomach fluid",
-                "Human Exposure"
-            ],
             "contactPoint": {
                 "fn": "Kim Rogers",
                 "hasEmail": "mailto:rogers.kim@epa.gov"
             },
+            "description": "The widespread use of copper-treated lumber has increased the potential for human exposure. Moreover, there is a lack of information on the fate and behavior of copper-treated wood particles following oral ingestion. In this study, the in vitro bioaccessibility of copper from copper-treated wood dust in simulated stomach fluid and DI water was determined. Three copper-treated wood products, liquid alkali copper quaternary and two micronized copper quarternary from different manufacturers, were incubated in the extraction media then fractionated by centrifugation and filtration through 0.45 \uf06dm and 10 kDa filters. The copper concentrations from isolated fractions were measured using Inductively Coupled Plasma-Optical Emission Spectrometry (ICP-OES). Total amounts of copper from each wood product were also determined using microwave-assisted acid digestion of dried wood samples and quantification using ICP-OES. The percent in vitro bioaccessible copper was between 83 and 90 % for all treated wood types. However, the percent of copper released in DI water was between 14 and 25 % for all wood products. This data suggests that copper is highly bioaccessible at low pH and may pose a potential human exposure risk upon ingestion. \n\nThis dataset is associated with the following publication:\nSantiago-Rodrigues, L., J.L. Griggs, K. Bradham , C. Nelson , T. Luxton , W. Platten , and K. Rogers. Assessment of the bioaccessibility of micronized copper wood in synthetic stomach fluid.   Environmental Nanotechnology, Monitoring and Management. Elsevier B.V., Amsterdam,  NETHERLANDS, 4: 85-92, (2015).",
             "distribution": [
                 {
-                    "title": "Table S2.docx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/277/Table%20S2.docx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+                    "title": "Table S2.docx"
                 },
                 {
-                    "title": "Table S3.docx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/277/Table%20S3.docx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+                    "title": "Table S3.docx"
                 }
             ],
+            "identifier": "A-tx9t-277",
+            "keyword": [
+                "Copper",
+                "Micronized Copper",
+                "Wood",
+                "Bioaccessibility",
+                "Synthetic stomach fluid",
+                "Human Exposure"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2016-09-07",
-            "references": [
-                "https://doi.org/10.1016/j.enmm.2015.07.003"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -37807,41 +37801,41 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.enmm.2015.07.003"
+            ],
+            "rights": null,
+            "title": "Assessment of the Bioaccessibility of Micronized Copper Wood on Simulated Stomach Fluid"
         },
         {
-            "title": "Pacific Ocean buoy temperature date - TAO/TRITON database & National Buoy Data Center database",
-            "description": "Pacific Ocean buoy temperature data. \n\nThis dataset is associated with the following publication:\nCarbone, F., M. Landis, C.N. Gencarelli, A. Naccarato, F. Sprovieri, F. De Simone, I.M. Hedgecock, and N. Pirrone. Sea surface temperature variation linked to elemental mercury concentrations measured on Mauna Loa.   GEOPHYSICAL RESEARCH LETTERS. American Geophysical Union, Washington, DC, USA,  online, (2016).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:094"
-            ],
-            "identifier": "A-47dd-363",
-            "keyword": [
-                "Ocean Evation"
-            ],
             "contactPoint": {
                 "fn": "Matthew Landis",
                 "hasEmail": "mailto:landis.matthew@epa.gov"
             },
+            "description": "Pacific Ocean buoy temperature data. \n\nThis dataset is associated with the following publication:\nCarbone, F., M. Landis, C.N. Gencarelli, A. Naccarato, F. Sprovieri, F. De Simone, I.M. Hedgecock, and N. Pirrone. Sea surface temperature variation linked to elemental mercury concentrations measured on Mauna Loa.   GEOPHYSICAL RESEARCH LETTERS. American Geophysical Union, Washington, DC, USA,  online, (2016).",
             "distribution": [
                 {
-                    "title": "https://www.pmel.noaa.gov/tao/index.shtml",
-                    "accessURL": "https://www.pmel.noaa.gov/tao/index.shtml"
+                    "accessURL": "https://www.pmel.noaa.gov/tao/index.shtml",
+                    "title": "https://www.pmel.noaa.gov/tao/index.shtml"
                 },
                 {
-                    "title": "https://www.ndbc.noaa.gov/",
-                    "accessURL": "https://www.ndbc.noaa.gov/"
+                    "accessURL": "https://www.ndbc.noaa.gov/",
+                    "title": "https://www.ndbc.noaa.gov/"
                 }
             ],
+            "identifier": "A-47dd-363",
+            "keyword": [
+                "Ocean Evation"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2016-04-21",
-            "references": [
-                "https://doi.org/10.1002/2016gl069252"
+            "programCode": [
+                "020:094"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -37851,40 +37845,40 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1002/2016gl069252"
+            ],
+            "rights": null,
+            "title": "Pacific Ocean buoy temperature date - TAO/TRITON database & National Buoy Data Center database"
         },
         {
-            "title": "CMAPS Study Wet Only Mercury in Precipitation Data Set from Chippiwa Lake and G.T. Graig Monitoring Sites",
-            "description": "Total mercury in precipitation collected using ASPS automated wet-only instrument and analyzed by cold vapor atomic fluorescence spectroscopy. \n\nThis dataset is associated with the following publication:\nLynam, M., J.T. Dvonch, J. Barres, M. Landis , and A. Kamal. Investigating the impact of local urban sources on total atmospheric mercury wet deposition in Cleveland, Ohio, USA.   ATMOSPHERIC ENVIRONMENT. Elsevier Science Ltd, New York, NY, USA, 127: 262-271, (2016).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:094"
-            ],
-            "identifier": "A-8939-373",
-            "keyword": [
-                "Mercury Deposition Network",
-                "Meteorological Case Study",
-                "Lake Erie"
-            ],
             "contactPoint": {
                 "fn": "Matthew Landis",
                 "hasEmail": "mailto:landis.matthew@epa.gov"
             },
+            "description": "Total mercury in precipitation collected using ASPS automated wet-only instrument and analyzed by cold vapor atomic fluorescence spectroscopy. \n\nThis dataset is associated with the following publication:\nLynam, M., J.T. Dvonch, J. Barres, M. Landis , and A. Kamal. Investigating the impact of local urban sources on total atmospheric mercury wet deposition in Cleveland, Ohio, USA.   ATMOSPHERIC ENVIRONMENT. Elsevier Science Ltd, New York, NY, USA, 127: 262-271, (2016).",
             "distribution": [
                 {
-                    "title": "Hg_event_wet_deposition.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/373/Hg_event_wet_deposition.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Hg_event_wet_deposition.xlsx"
                 }
             ],
+            "identifier": "A-8939-373",
+            "keyword": [
+                "Mercury Deposition Network",
+                "Meteorological Case Study",
+                "Lake Erie"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2015-09-25",
-            "references": [
-                "https://doi.org/10.1016/j.atmosenv.2015.12.048"
+            "programCode": [
+                "020:094"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -37894,43 +37888,43 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.atmosenv.2015.12.048"
+            ],
+            "rights": null,
+            "title": "CMAPS Study Wet Only Mercury in Precipitation Data Set from Chippiwa Lake and G.T. Graig Monitoring Sites"
         },
         {
-            "title": "Data used in Xu et al., 2016 paper entitled \"Characteristics and distributions of atmospheric mercury emitted from anthropogenic sources in Guiyang, southwestern China",
-            "description": "Mercury emissions data from anthropogenic sources as described in Xu et al., 2016. \n\nThis dataset is associated with the following publication:\nXu, X., N. Liu, M. Landis, X. Feng, and G. Qiu. Characteristics and distributions of atmospheric mercury emitted from anthropogenic sources in Guiyang, southwestern China.   Acta Geochimica. Springer, Heidelburg,  GERMANY,  1-11, (2016).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:094"
-            ],
-            "identifier": "A-4tmv-359",
-            "keyword": [
-                "Atmospheric mercury",
-                "Speciation",
-                "Antrhopogenic Sources",
-                "GEM",
-                "RGM",
-                "PHg"
-            ],
             "contactPoint": {
                 "fn": "Matthew Landis",
                 "hasEmail": "mailto:landis.matthew@epa.gov"
             },
+            "description": "Mercury emissions data from anthropogenic sources as described in Xu et al., 2016. \n\nThis dataset is associated with the following publication:\nXu, X., N. Liu, M. Landis, X. Feng, and G. Qiu. Characteristics and distributions of atmospheric mercury emitted from anthropogenic sources in Guiyang, southwestern China.   Acta Geochimica. Springer, Heidelburg,  GERMANY,  1-11, (2016).",
             "distribution": [
                 {
-                    "title": "Xu_et_al_data.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/359/Xu_et_al_data.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Xu_et_al_data.xlsx"
                 }
             ],
+            "identifier": "A-4tmv-359",
+            "keyword": [
+                "Atmospheric mercury",
+                "Speciation",
+                "Antrhopogenic Sources",
+                "GEM",
+                "RGM",
+                "PHg"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2016-04-08",
-            "references": [
-                "http://link.springer.com/article/10.1007/s11631-016-0111-9"
+            "programCode": [
+                "020:094"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -37940,38 +37934,38 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "http://link.springer.com/article/10.1007/s11631-016-0111-9"
+            ],
+            "rights": null,
+            "title": "Data used in Xu et al., 2016 paper entitled \"Characteristics and distributions of atmospheric mercury emitted from anthropogenic sources in Guiyang, southwestern China"
         },
         {
-            "title": "Carbone_et_al_2016_ambient_data - Sea surface temperature variation linked to elemental mercury concentrationsmeasured on Mauna Loa",
-            "description": "This data set has two sets of gaseous elemental mercury data. The first column contains all Hg related data some of which may have been affected by the upslope events such as the emissions from the nearby volcano. The next column contain values that were flagged and excluded as being affected by the nearby volcanic events. The flagging method used to eliminate these values was developed using an episode identification scheme using SO2 data. For the years of 2002 through 2004, hourly SO2 data were used to llag the upslope values. For the years of 2005-2009, 5 minute SO2 values were used to flag upslope events.\n\nWhile SO2 and O3 data were collected by EPA as part of this study, the CO2 data were downloaded from NOAA data website along with the flag related information provided below. (http://www.esrl.noaa.gov/gmd/dv/data/index.php?parameter_name=Carbon%2BDioxide&showall=1&site=MLO). \n\nThis dataset is associated with the following publication:\nCarbone, F., M. Landis, C.N. Gencarelli, A. Naccarato, F. Sprovieri, F. De Simone, I.M. Hedgecock, and N. Pirrone. Sea surface temperature variation linked to elemental mercury concentrations measured on Mauna Loa.   GEOPHYSICAL RESEARCH LETTERS. American Geophysical Union, Washington, DC, USA,  online, (2016).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:094"
-            ],
-            "identifier": "A-47dd-361",
-            "keyword": [
-                "Ocean Evation"
-            ],
             "contactPoint": {
                 "fn": "Matthew Landis",
                 "hasEmail": "mailto:landis.matthew@epa.gov"
             },
+            "description": "This data set has two sets of gaseous elemental mercury data. The first column contains all Hg related data some of which may have been affected by the upslope events such as the emissions from the nearby volcano. The next column contain values that were flagged and excluded as being affected by the nearby volcanic events. The flagging method used to eliminate these values was developed using an episode identification scheme using SO2 data. For the years of 2002 through 2004, hourly SO2 data were used to llag the upslope values. For the years of 2005-2009, 5 minute SO2 values were used to flag upslope events.\n\nWhile SO2 and O3 data were collected by EPA as part of this study, the CO2 data were downloaded from NOAA data website along with the flag related information provided below. (http://www.esrl.noaa.gov/gmd/dv/data/index.php?parameter_name=Carbon%2BDioxide&showall=1&site=MLO). \n\nThis dataset is associated with the following publication:\nCarbone, F., M. Landis, C.N. Gencarelli, A. Naccarato, F. Sprovieri, F. De Simone, I.M. Hedgecock, and N. Pirrone. Sea surface temperature variation linked to elemental mercury concentrations measured on Mauna Loa.   GEOPHYSICAL RESEARCH LETTERS. American Geophysical Union, Washington, DC, USA,  online, (2016).",
             "distribution": [
                 {
-                    "title": "Carbone_et_al-2016_data.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/361/Carbone_et_al-2016_data.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Carbone_et_al-2016_data.xlsx"
                 }
             ],
+            "identifier": "A-47dd-361",
+            "keyword": [
+                "Ocean Evation"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2016-04-21",
-            "references": [
-                "https://doi.org/10.1002/2016gl069252"
+            "programCode": [
+                "020:094"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -37981,19 +37975,31 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1002/2016gl069252"
+            ],
+            "rights": null,
+            "title": "Carbone_et_al_2016_ambient_data - Sea surface temperature variation linked to elemental mercury concentrationsmeasured on Mauna Loa"
         },
         {
-            "title": "Establishing the \u201cBiological Relevance\u201d of Dipentyl Phthalate Reductions in Fetal Rat Testosterone Production and Plasma and Testis Testosterone Levels ",
-            "description": "metadata sheet, data sheet for each table and figure in the published manuscript. \n\nThis dataset is associated with the following publication:\nGray , E., J. Furr , K. Tatum-Gibbs, C. Lambright , H. Sampson, B. Hannas, V. Wilson , A. Hotchkiss , and P. Foster. Establishing the Biological Relevance of Dipentyl Phthalate Reductions in Fetal Rat Testosterone Production and Plasma and Testis Testosterone Levels.   TOXICOLOGICAL SCIENCES. Society of Toxicology,    149(1): 178-91, (2016).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:095"
+            "contactPoint": {
+                "fn": "Leon Gray",
+                "hasEmail": "mailto:gray.earl@epa.gov"
+            },
+            "describedBy": "https://pasteur.epa.gov/uploads/347/documents/DATA%20DICTIONARY.xlsx",
+            "describedByType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+            "description": "metadata sheet, data sheet for each table and figure in the published manuscript. \n\nThis dataset is associated with the following publication:\nGray , E., J. Furr , K. Tatum-Gibbs, C. Lambright , H. Sampson, B. Hannas, V. Wilson , A. Hotchkiss , and P. Foster. Establishing the Biological Relevance of Dipentyl Phthalate Reductions in Fetal Rat Testosterone Production and Plasma and Testis Testosterone Levels.   TOXICOLOGICAL SCIENCES. Society of Toxicology,    149(1): 178-91, (2016).",
+            "distribution": [
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/347/science%20hub%20data%20sets%20and%20metadata%20file.xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "science hub data sets and metadata file.xlsx"
+                }
             ],
             "identifier": "A-9cnz-347",
             "keyword": [
@@ -38004,21 +38010,10 @@
                 "Phthalates",
                 "reproductive development"
             ],
-            "contactPoint": {
-                "fn": "Leon Gray",
-                "hasEmail": "mailto:gray.earl@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "science hub data sets and metadata file.xlsx",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/347/science%20hub%20data%20sets%20and%20metadata%20file.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2016-09-18",
-            "references": [
-                "https://doi.org/10.1093/toxsci/kfv224",
-                "https://pasteur.epa.gov/uploads/347/documents/gray%20et%20al%202016%20brrt%20dpep%20tox%20sci.pdf"
+            "programCode": [
+                "020:095"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -38029,106 +38024,105 @@
                     }
                 }
             },
-            "describedBy": "https://pasteur.epa.gov/uploads/347/documents/DATA%20DICTIONARY.xlsx",
-            "describedByType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+            "references": [
+                "https://doi.org/10.1093/toxsci/kfv224",
+                "https://pasteur.epa.gov/uploads/347/documents/gray%20et%20al%202016%20brrt%20dpep%20tox%20sci.pdf"
+            ],
+            "rights": null,
+            "title": "Establishing the \u201cBiological Relevance\u201d of Dipentyl Phthalate Reductions in Fetal Rat Testosterone Production and Plasma and Testis Testosterone Levels "
         },
         {
-            "title": "Data supporting Al-Abed et al., Environ. Sci.: Nano, 2016,",
-            "description": "Data files representing each of the Figures and Tables published in Al-Abed et al., Environ. Sci.: Nano, 2016,\n3, 593.  The data file names identify the Figure or Table and each file contains an internal set of data definitions. \n\nThis dataset is associated with the following publication:\nAl-Abed, S.R., J. Virkutyte, J. Ortenzio , R.M. McCarrick, L. Degn, R. Zucker , N. Coates , K. Cleveland, H. Ma, S. Diamond, K. Dreher , and W. Boyes. Environmental aging alters AI(OH)3 coating of TiO2 nanoparticles enhancing their photocatalytic and phototoxicity activities.   Environmental Science: Nano. RSC Publishing, Cambridge,  UK,  N/A, (2016).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:095"
-            ],
-            "identifier": "A-m64f-298",
-            "keyword": [
-                "sunscreen",
-                "environmental degredation",
-                "engineered nanomaterials",
-                "Engineered nanoparticles (NP)",
-                "nanomaterials",
-                "phototoxicity",
-                "environmental transformations",
-                "titanium dioxide"
-            ],
             "contactPoint": {
                 "fn": "William Boyes",
                 "hasEmail": "mailto:boyes.william@epa.gov"
             },
+            "description": "Data files representing each of the Figures and Tables published in Al-Abed et al., Environ. Sci.: Nano, 2016,\n3, 593.  The data file names identify the Figure or Table and each file contains an internal set of data definitions. \n\nThis dataset is associated with the following publication:\nAl-Abed, S.R., J. Virkutyte, J. Ortenzio , R.M. McCarrick, L. Degn, R. Zucker , N. Coates , K. Cleveland, H. Ma, S. Diamond, K. Dreher , and W. Boyes. Environmental aging alters AI(OH)3 coating of TiO2 nanoparticles enhancing their photocatalytic and phototoxicity activities.   Environmental Science: Nano. RSC Publishing, Cambridge,  UK,  N/A, (2016).",
             "distribution": [
                 {
-                    "title": "TiO2_POOL_FIG_1_EDS data from Souhail.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/298/TiO2_POOL_FIG_1_EDS%20data%20from%20Souhail.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "TiO2_POOL_FIG_1_EDS data from Souhail.xlsx"
                 },
                 {
-                    "title": "TiO2_POOL_FIG_2_XPS data from Souhail.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/298/TiO2_POOL_FIG_2_XPS%20data%20from%20Souhail.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "TiO2_POOL_FIG_2_XPS data from Souhail.xlsx"
                 },
                 {
-                    "title": "TIO2_POOL_FIG_3_EPR_data.docx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/298/TIO2_POOL_FIG_3_EPR_data.docx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+                    "title": "TIO2_POOL_FIG_3_EPR_data.docx"
                 },
                 {
-                    "title": "TiO2_POOL_FIG_4_PHOTOTOX data from Jayna.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/298/TiO2_POOL_FIG_4_PHOTOTOX%20data%20from%20Jayna.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "TiO2_POOL_FIG_4_PHOTOTOX data from Jayna.xlsx"
                 },
                 {
-                    "title": "TIO2_POOL_FIG_5_FLOW_SIDE_SCATTER.docx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/298/TIO2_POOL_FIG_5_FLOW_SIDE_SCATTER.docx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+                    "title": "TIO2_POOL_FIG_5_FLOW_SIDE_SCATTER.docx"
                 },
                 {
-                    "title": "TIO2_POOL_FIG_6_FLUOR_IMAGES.docx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/298/TIO2_POOL_FIG_6_FLUOR_IMAGES.docx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+                    "title": "TIO2_POOL_FIG_6_FLUOR_IMAGES.docx"
                 },
                 {
-                    "title": "TIO2_POOL_Suppl_Fig1_SEM.docx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/298/TIO2_POOL_Suppl_Fig1_SEM.docx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+                    "title": "TIO2_POOL_Suppl_Fig1_SEM.docx"
                 },
                 {
-                    "title": "TIO2_POOL_Suppl_Fig2_TEM.docx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/298/TIO2_POOL_Suppl_Fig2_TEM.docx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+                    "title": "TIO2_POOL_Suppl_Fig2_TEM.docx"
                 },
                 {
-                    "title": "TIO2_POOL_Suppl_Fig3_EDS_graph.docx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/298/TIO2_POOL_Suppl_Fig3_EDS_graph.docx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+                    "title": "TIO2_POOL_Suppl_Fig3_EDS_graph.docx"
                 },
                 {
-                    "title": "TiO2_POOL_Suppl_Fig4_APF_TBARS.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/298/TiO2_POOL_Suppl_Fig4_APF_TBARS.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "TiO2_POOL_Suppl_Fig4_APF_TBARS.xlsx"
                 },
                 {
-                    "title": "TIO2_POOL_Suppl_Table1_FLOW_TABLE.docx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/298/TIO2_POOL_Suppl_Table1_FLOW_TABLE.docx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+                    "title": "TIO2_POOL_Suppl_Table1_FLOW_TABLE.docx"
                 },
                 {
-                    "title": "TIO2_POOL_TABLE1_WICOXON_STATS.docx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/298/TIO2_POOL_TABLE1_WICOXON_STATS.docx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+                    "title": "TIO2_POOL_TABLE1_WICOXON_STATS.docx"
                 },
                 {
-                    "title": "TIO2_POOL_TABLE2_AGGOLMERATION.docx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/298/TIO2_POOL_TABLE2_AGGOLMERATION.docx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+                    "title": "TIO2_POOL_TABLE2_AGGOLMERATION.docx"
                 }
             ],
+            "identifier": "A-m64f-298",
+            "keyword": [
+                "sunscreen",
+                "environmental degredation",
+                "engineered nanomaterials",
+                "Engineered nanoparticles (NP)",
+                "nanomaterials",
+                "phototoxicity",
+                "environmental transformations",
+                "titanium dioxide"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2016-09-12",
-            "references": [
-                "https://doi.org/10.1039/c5en00250h"
+            "programCode": [
+                "020:095"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -38138,19 +38132,28 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1039/c5en00250h"
+            ],
+            "rights": null,
+            "title": "Data supporting Al-Abed et al., Environ. Sci.: Nano, 2016,"
         },
         {
-            "title": "Computational Modeling and Simulation of Genital Tubercle Development",
-            "description": "Hypospadias is a developmental defect of urethral tube closure that has a complex etiology involving genetic and environmental factors, including anti-androgenic and estrogenic disrupting chemicals; however, little is known about the morphoregulatory consequences of androgen/estrogen balance during genital tubercle (GT) development. Computer models that predictively model sexual dimorphism of the GT may provide a useful resource to translate chemical-target bipartite networks and their developmental consequences across the human-relevant chemical universe. Here, we describe a multicellular agent-based model of genital tubercle (GT) development that simulates urethrogenesis from the sexually-indifferent urethral plate stage to urethral tube closure. The prototype model, constructed in CompuCell3D, recapitulates key aspects of GT morphogenesis controlled by SHH, FGF10, and androgen pathways through modulation of stochastic cell behaviors, including differential adhesion, motility, proliferation, and apoptosis. Proper urethral tube closure in the model was shown to depend quantitatively on SHH- and FGF10-induced effects on mesenchymal proliferation and epithelial apoptosis\u2014both ultimately linked to androgen signaling. In the absence of androgen, GT development was feminized and with partial androgen deficiency, the model resolved with incomplete urethral tube closure, thereby providing an in silico platform for probabilistic prediction of hypospadias risk across combinations of minor perturbations to the GT system at various stages of embryonic development. \n\nThis dataset is associated with the following publication:\nLeung , M.C.K., S. Hutson, A. Seifert, R. Spencer, and T. Knudsen. (REPRODUCTIVE TOXICOLOGY) Computational Modeling and Simulation of Genital Tubercle Development.   REPRODUCTIVE TOXICOLOGY. Elsevier Science Ltd, New York, NY, USA,  1-11, (2016).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:095"
+            "contactPoint": {
+                "fn": "Thomas Knudsen",
+                "hasEmail": "mailto:knudsen.thomas@epa.gov"
+            },
+            "description": "Hypospadias is a developmental defect of urethral tube closure that has a complex etiology involving genetic and environmental factors, including anti-androgenic and estrogenic disrupting chemicals; however, little is known about the morphoregulatory consequences of androgen/estrogen balance during genital tubercle (GT) development. Computer models that predictively model sexual dimorphism of the GT may provide a useful resource to translate chemical-target bipartite networks and their developmental consequences across the human-relevant chemical universe. Here, we describe a multicellular agent-based model of genital tubercle (GT) development that simulates urethrogenesis from the sexually-indifferent urethral plate stage to urethral tube closure. The prototype model, constructed in CompuCell3D, recapitulates key aspects of GT morphogenesis controlled by SHH, FGF10, and androgen pathways through modulation of stochastic cell behaviors, including differential adhesion, motility, proliferation, and apoptosis. Proper urethral tube closure in the model was shown to depend quantitatively on SHH- and FGF10-induced effects on mesenchymal proliferation and epithelial apoptosis\u2014both ultimately linked to androgen signaling. In the absence of androgen, GT development was feminized and with partial androgen deficiency, the model resolved with incomplete urethral tube closure, thereby providing an in silico platform for probabilistic prediction of hypospadias risk across combinations of minor perturbations to the GT system at various stages of embryonic development. \n\nThis dataset is associated with the following publication:\nLeung , M.C.K., S. Hutson, A. Seifert, R. Spencer, and T. Knudsen. (REPRODUCTIVE TOXICOLOGY) Computational Modeling and Simulation of Genital Tubercle Development.   REPRODUCTIVE TOXICOLOGY. Elsevier Science Ltd, New York, NY, USA,  1-11, (2016).",
+            "distribution": [
+                {
+                    "accessURL": "https://gaftp.epa.gov/COMPTOX/NCCT_Publication_Data/Knudsen/Virtual_Tissues_Male_Repro_Tox/Leung_2016_RTX/",
+                    "title": "https://gaftp.epa.gov/COMPTOX/NCCT_Publication_Data/Knudsen/Virtual_Tissues_Male_Repro_Tox/Leung_2016_RTX/"
+                }
             ],
             "identifier": "A-dncw-339",
             "keyword": [
@@ -38162,19 +38165,10 @@
                 "virtual liver",
                 "tipping points"
             ],
-            "contactPoint": {
-                "fn": "Thomas Knudsen",
-                "hasEmail": "mailto:knudsen.thomas@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "https://gaftp.epa.gov/COMPTOX/NCCT_Publication_Data/Knudsen/Virtual_Tissues_Male_Repro_Tox/Leung_2016_RTX/",
-                    "accessURL": "https://gaftp.epa.gov/COMPTOX/NCCT_Publication_Data/Knudsen/Virtual_Tissues_Male_Repro_Tox/Leung_2016_RTX/"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2016-09-01",
-            "references": [
-                "https://doi.org/10.1016/j.reprotox.2016.05.005"
+            "programCode": [
+                "020:095"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -38184,47 +38178,47 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.reprotox.2016.05.005"
+            ],
+            "rights": null,
+            "title": "Computational Modeling and Simulation of Genital Tubercle Development"
         },
         {
-            "title": "Data from Tiered High-Throughput Screening Approach to Identify Thyroperoxidase Inhibitors within the ToxCast Phase I and II Chemical Libraries ",
-            "description": "High-throughput screening for potential thyroid-disrupting chemicals requires a system of assays to capture multiple molecular-initiating events (MIEs) that converge on perturbed thyroid hormone (TH) homeostasis. Screening for MIEs specific to TH-disrupting pathways is limited in the U.S. Environmental Protection Agency ToxCast screening assay portfolio. To fill 1 critical screening gap, the Amplex UltraRed-thyroperoxidase (AUR-TPO) assay was developed to identify chemicals that inhibit TPO, as decreased TPO activity reduces TH synthesis. The ToxCast phase I and II chemical libraries, comprised of 1074 unique chemicals, were initially screened using a single, high concentration to identify potential TPO inhibitors. Chemicals positive in the single-concentration screen were retested in concentration-response. Due to high false-positive rates typically observed with loss-of-signal assays such as AUR-TPO, we also employed 2 additional assays in parallel to identify possible sources of nonspecific assay signal loss, enabling stratification of roughly 300 putative TPO inhibitors based upon selective AUR-TPO activity. A cell-free luciferase inhibition assay was used to identify nonspecific enzyme inhibition among the putative TPO inhibitors, and a cytotoxicity assay using a human cell line was used to estimate the cellular tolerance limit. Additionally, the TPO inhibition activities of 150 chemicals were compared between the AUR-TPO and an orthogonal peroxidase oxidation assay using guaiacol as a substrate to confirm the activity profiles of putative TPO inhibitors. This effort represents the most extensive TPO inhibition screening campaign to date and illustrates a tiered screening approach that focuses resources, maximizes assay throughput, and reduces animal use. \n\nThis dataset is associated with the following publication:\nPaul-Friedman, K., E.D. Watt , M.W. Hornung , J.M. Hedge , R.S. Judson , K.M. Crofton , K.A. Houck , and S.O. Simmons. (TOXICOLOGICAL SCIENCES) Tiered High-Throughput Screening Approach to Identify Thyroperoxidase Inhibitors within the ToxCast Phase I and II Chemical Libraries.   TOXICOLOGICAL SCIENCES. Society of Toxicology,     1-59, (2016).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:095"
-            ],
-            "identifier": "A-z35j-97",
-            "keyword": [
-                "ToxCast",
-                "chemical safety research",
-                "chemical safety for sustainablity",
-                "high-throughput toxicology",
-                "Thyroperoxidase",
-                "endocrine disruption"
-            ],
             "contactPoint": {
                 "fn": "Steven Simmons",
                 "hasEmail": "mailto:simmons.steve@epa.gov"
             },
+            "description": "High-throughput screening for potential thyroid-disrupting chemicals requires a system of assays to capture multiple molecular-initiating events (MIEs) that converge on perturbed thyroid hormone (TH) homeostasis. Screening for MIEs specific to TH-disrupting pathways is limited in the U.S. Environmental Protection Agency ToxCast screening assay portfolio. To fill 1 critical screening gap, the Amplex UltraRed-thyroperoxidase (AUR-TPO) assay was developed to identify chemicals that inhibit TPO, as decreased TPO activity reduces TH synthesis. The ToxCast phase I and II chemical libraries, comprised of 1074 unique chemicals, were initially screened using a single, high concentration to identify potential TPO inhibitors. Chemicals positive in the single-concentration screen were retested in concentration-response. Due to high false-positive rates typically observed with loss-of-signal assays such as AUR-TPO, we also employed 2 additional assays in parallel to identify possible sources of nonspecific assay signal loss, enabling stratification of roughly 300 putative TPO inhibitors based upon selective AUR-TPO activity. A cell-free luciferase inhibition assay was used to identify nonspecific enzyme inhibition among the putative TPO inhibitors, and a cytotoxicity assay using a human cell line was used to estimate the cellular tolerance limit. Additionally, the TPO inhibition activities of 150 chemicals were compared between the AUR-TPO and an orthogonal peroxidase oxidation assay using guaiacol as a substrate to confirm the activity profiles of putative TPO inhibitors. This effort represents the most extensive TPO inhibition screening campaign to date and illustrates a tiered screening approach that focuses resources, maximizes assay throughput, and reduces animal use. \n\nThis dataset is associated with the following publication:\nPaul-Friedman, K., E.D. Watt , M.W. Hornung , J.M. Hedge , R.S. Judson , K.M. Crofton , K.A. Houck , and S.O. Simmons. (TOXICOLOGICAL SCIENCES) Tiered High-Throughput Screening Approach to Identify Thyroperoxidase Inhibitors within the ToxCast Phase I and II Chemical Libraries.   TOXICOLOGICAL SCIENCES. Society of Toxicology,     1-59, (2016).",
             "distribution": [
                 {
-                    "title": "Figures and Tables_v10.docx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/97/Figures%20and%20Tables_v10.docx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+                    "title": "Figures and Tables_v10.docx"
                 },
                 {
-                    "title": "https://gaftp.epa.gov/COMPTOX/NCCT_Publication_Data/FriedmanPaul_K/2016_TPO_ToxCast_ToxSci",
-                    "accessURL": "https://gaftp.epa.gov/COMPTOX/NCCT_Publication_Data/FriedmanPaul_K/2016_TPO_ToxCast_ToxSci"
+                    "accessURL": "https://gaftp.epa.gov/COMPTOX/NCCT_Publication_Data/FriedmanPaul_K/2016_TPO_ToxCast_ToxSci",
+                    "title": "https://gaftp.epa.gov/COMPTOX/NCCT_Publication_Data/FriedmanPaul_K/2016_TPO_ToxCast_ToxSci"
                 }
             ],
+            "identifier": "A-z35j-97",
+            "keyword": [
+                "ToxCast",
+                "chemical safety research",
+                "chemical safety for sustainablity",
+                "high-throughput toxicology",
+                "Thyroperoxidase",
+                "endocrine disruption"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2016-04-01",
-            "references": [
-                "https://doi.org/10.1093/toxsci/kfw034"
+            "programCode": [
+                "020:095"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -38234,48 +38228,50 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1093/toxsci/kfw034"
+            ],
+            "rights": null,
+            "title": "Data from Tiered High-Throughput Screening Approach to Identify Thyroperoxidase Inhibitors within the ToxCast Phase I and II Chemical Libraries "
         },
         {
-            "title": "Watershed impervious cover relative to stream location",
-            "description": "Estimates of watershed (12-digit huc) impervious cover and impervious cover near streams and water body shorelines for three dates (2001, 2006, 2011) using NLCD data.  Differences between watershed impervious cover and impervious cover near streams can be used to assess the spatial pattern of impervious cover within a watershed. \n\nThis dataset is associated with the following publication:\nWickham , J., A. Neale , M. Mehaffey , T. Jarnagin , and D. Norton. Temporal Trends in Impervious Cover Relative to Stream Location..   JOURNAL OF AMERICAN WATER RESOURCES ASSOCIATION. American Water Resources Association, Middleburg, VA, USA, 52(2): 409-419, (2016).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:097"
-            ],
-            "identifier": "A-n03c-254",
-            "keyword": [
-                "Impervious cover",
-                "National Land Cover Database (NLCD)",
-                "Clean Water Act",
-                "change detection",
-                "roads",
-                "spatial pattern"
-            ],
             "contactPoint": {
                 "fn": "James Wickham",
                 "hasEmail": "mailto:wickham.james@epa.gov"
             },
+            "describedBy": "https://pasteur.epa.gov/uploads/254/documents/SciHub_Metadata.docx",
+            "describedByType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+            "description": "Estimates of watershed (12-digit huc) impervious cover and impervious cover near streams and water body shorelines for three dates (2001, 2006, 2011) using NLCD data.  Differences between watershed impervious cover and impervious cover near streams can be used to assess the spatial pattern of impervious cover within a watershed. \n\nThis dataset is associated with the following publication:\nWickham , J., A. Neale , M. Mehaffey , T. Jarnagin , and D. Norton. Temporal Trends in Impervious Cover Relative to Stream Location..   JOURNAL OF AMERICAN WATER RESOURCES ASSOCIATION. American Water Resources Association, Middleburg, VA, USA, 52(2): 409-419, (2016).",
             "distribution": [
                 {
-                    "title": "SciHub_data.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/254/SciHub_data.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "SciHub_data.xlsx"
                 },
                 {
-                    "title": "SciHub_Metadata.docx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/254/SciHub_Metadata.docx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+                    "title": "SciHub_Metadata.docx"
                 }
             ],
+            "identifier": "A-n03c-254",
+            "keyword": [
+                "Impervious cover",
+                "National Land Cover Database (NLCD)",
+                "Clean Water Act",
+                "change detection",
+                "roads",
+                "spatial pattern"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2015-01-31",
-            "references": [
-                "https://www.epa.gov/enviroatlas"
+            "programCode": [
+                "020:097"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -38286,42 +38282,40 @@
                     }
                 }
             },
-            "describedBy": "https://pasteur.epa.gov/uploads/254/documents/SciHub_Metadata.docx",
-            "describedByType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
+            "references": [
+                "https://www.epa.gov/enviroatlas"
+            ],
+            "rights": null,
+            "title": "Watershed impervious cover relative to stream location"
         },
         {
-            "title": "Permeable pavement study (Edison)",
-            "description": "While permeable pavement is increasingly being used to control stormwater runoff, field-based, side-by-side investigations on the effects different pavement types have on nutrient concentrations present in stormwater runoff are limited.  In 2009, the U.S. EPA constructed a 0.4-ha parking lot in Edison, New Jersey, that incorporated permeable interlocking concrete pavement (PICP), pervious concrete (PC), and porous asphalt (PA).  Each permeable pavement type has four, 54.9-m2, lined sections that direct all infiltrate into 5.7-m3 tanks enabling complete volume collection and sampling.  This paper highlights the results from a 12-month period when samples were collected from 13 rainfall/runoff events and analyzed for nitrogen species, orthophosphate, and organic carbon.  Differences in infiltrate concentrations among the three permeable pavement types were assessed and compared with concentrations in rainwater samples and impervious asphalt runoff samples, which were collected as controls.  Contrary to expectations based on the literature, the PA infiltrate had significantly larger total nitrogen (TN) concentrations than runoff and infiltrate from the other two permeable pavement types, indicating that nitrogen leached from materials in the PA strata.  There was no significant difference in TN concentration between runoff and infiltrate from either PICP or PC, but TN in runoff was significantly larger than in the rainwater, suggesting meaningful inter-event dry deposition.  Similar to other permeable pavement studies, nitrate was the dominant nitrogen species in the infiltrate.  The PA infiltrate had significantly larger nitrite and ammonia concentrations than PICP and PC, and this was presumably linked to unexpectedly high pH in the PA infiltrate that greatly exceeded the optimal pH range for nitrifying bacteria.  Contrary to the nitrogen results, the PA infiltrate had significantly smaller orthophosphate concentrations than in rainwater, runoff, and infiltrate from PICP and PC, and this was attributed to the high pH in PA infiltrate possibly causing rapid precipitation of orthophosphate with metal cations.  Orthophosphate was exported from the PICP and PC, as evidenced by the significantly larger infiltrate concentrations compared with influent sources of rainwater and runoff. \n\nThis dataset is associated with the following publication:\nBrown , R., and M. Borst. Nutrient Infiltrate Concentrations from Three Permeable Pavement Types.   JOURNAL OF ENVIRONMENTAL MANAGEMENT. Elsevier Science Ltd, New York, NY, USA, 164: 74-85, (2015).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "A-ghxg-275",
-            "keyword": [
-                "Green Infrastructure",
-                "bmp",
-                "stormwater management",
-                "GI perrormance"
-            ],
             "contactPoint": {
                 "fn": "Michael Borst",
                 "hasEmail": "mailto:borst.mike@epa.gov"
             },
+            "description": "While permeable pavement is increasingly being used to control stormwater runoff, field-based, side-by-side investigations on the effects different pavement types have on nutrient concentrations present in stormwater runoff are limited.  In 2009, the U.S. EPA constructed a 0.4-ha parking lot in Edison, New Jersey, that incorporated permeable interlocking concrete pavement (PICP), pervious concrete (PC), and porous asphalt (PA).  Each permeable pavement type has four, 54.9-m2, lined sections that direct all infiltrate into 5.7-m3 tanks enabling complete volume collection and sampling.  This paper highlights the results from a 12-month period when samples were collected from 13 rainfall/runoff events and analyzed for nitrogen species, orthophosphate, and organic carbon.  Differences in infiltrate concentrations among the three permeable pavement types were assessed and compared with concentrations in rainwater samples and impervious asphalt runoff samples, which were collected as controls.  Contrary to expectations based on the literature, the PA infiltrate had significantly larger total nitrogen (TN) concentrations than runoff and infiltrate from the other two permeable pavement types, indicating that nitrogen leached from materials in the PA strata.  There was no significant difference in TN concentration between runoff and infiltrate from either PICP or PC, but TN in runoff was significantly larger than in the rainwater, suggesting meaningful inter-event dry deposition.  Similar to other permeable pavement studies, nitrate was the dominant nitrogen species in the infiltrate.  The PA infiltrate had significantly larger nitrite and ammonia concentrations than PICP and PC, and this was presumably linked to unexpectedly high pH in the PA infiltrate that greatly exceeded the optimal pH range for nitrifying bacteria.  Contrary to the nitrogen results, the PA infiltrate had significantly smaller orthophosphate concentrations than in rainwater, runoff, and infiltrate from PICP and PC, and this was attributed to the high pH in PA infiltrate possibly causing rapid precipitation of orthophosphate with metal cations.  Orthophosphate was exported from the PICP and PC, as evidenced by the significantly larger infiltrate concentrations compared with influent sources of rainwater and runoff. \n\nThis dataset is associated with the following publication:\nBrown , R., and M. Borst. Nutrient Infiltrate Concentrations from Three Permeable Pavement Types.   JOURNAL OF ENVIRONMENTAL MANAGEMENT. Elsevier Science Ltd, New York, NY, USA, 164: 74-85, (2015).",
             "distribution": [
                 {
-                    "title": "edison parking lot nutrient data base period.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/275/edison%20parking%20lot%20nutrient%20data%20base%20period.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "edison parking lot nutrient data base period.xlsx"
                 }
             ],
+            "identifier": "A-ghxg-275",
+            "keyword": [
+                "Green Infrastructure",
+                "bmp",
+                "stormwater management",
+                "GI perrormance"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2016-09-06",
-            "references": [
-                "http://www.ncbi.nlm.nih.gov/pubmed/26348134"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -38331,19 +38325,29 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "http://www.ncbi.nlm.nih.gov/pubmed/26348134"
+            ],
+            "rights": null,
+            "title": "Permeable pavement study (Edison)"
         },
         {
-            "title": "Evaluating the Accuracy of Common Runoff Estimation Methods for New Impervious Hot-Mix Asphalt",
-            "description": "Excel workbook,  First sheet is data dictionary.  second sheet is the data representing the abstraction for events with short antecedent dry period (less than 24 hr). \n\nThis dataset is associated with the following publication:\nBrown , R., and M. Borst. Evaluating the Accuracy of Common Runoff Estimation Methods for New Impervious Hot-Mix Asphalt.   Journal of Sustainable Water in the Built Environment. American Society of Civil Engineers (ASCE), New York, NY, USA,  online, (2015).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
+            "contactPoint": {
+                "fn": "Michael Borst",
+                "hasEmail": "mailto:borst.mike@epa.gov"
+            },
+            "description": "Excel workbook,  First sheet is data dictionary.  second sheet is the data representing the abstraction for events with short antecedent dry period (less than 24 hr). \n\nThis dataset is associated with the following publication:\nBrown , R., and M. Borst. Evaluating the Accuracy of Common Runoff Estimation Methods for New Impervious Hot-Mix Asphalt.   Journal of Sustainable Water in the Built Environment. American Society of Civil Engineers (ASCE), New York, NY, USA,  online, (2015).",
+            "distribution": [
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/352/Borst-ScID%20A-4qrm.xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Borst-ScID A-4qrm.xlsx"
+                }
             ],
             "identifier": "A-4qrm-352",
             "keyword": [
@@ -38355,20 +38359,10 @@
                 "stormwater",
                 "stormwater management"
             ],
-            "contactPoint": {
-                "fn": "Michael Borst",
-                "hasEmail": "mailto:borst.mike@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "Borst-ScID A-4qrm.xlsx",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/352/Borst-ScID%20A-4qrm.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2014-08-01",
-            "references": [
-                "https://doi.org/10.1061/jswbay.0000806"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -38378,20 +38372,26 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1061/jswbay.0000806"
+            ],
+            "rights": null,
+            "title": "Evaluating the Accuracy of Common Runoff Estimation Methods for New Impervious Hot-Mix Asphalt"
         },
         {
-            "title": "Ensemble standar deviation of wind speed and direction of the FDDA input to WRF",
-            "description": "NetCDF file of the SREF standard deviation of wind speed and direction that was used to inject variability in the FDDA input.\r\n\r\nvariable U_NDG_OLD contains standard deviation of wind speed (m/s)\r\nvariable V_NDG_OLD contains the standard deviation of wind direction (deg). This dataset is not publicly accessible because: This is a netcdf file that is 3.9Gb. It can be accessed through the following means: On the HPC system sol (2016). In the asm archive here: /asm/grc/JGR_ENSEMBLE_ScienceHub/figure1.nc. Format: Figure 1 data. This is the variability of wind speed and direction of the four dimensional data assimilation inputs. The variability includes the 14 members of the ensemble. \n\nThis dataset is associated with the following publication:\nGilliam , R., C. Hogrefe , J. Godowitch, S. Napelenok , R. Mathur , and S.T. Rao. Impact of inherent meteorology uncertainty on air quality model predictions.   JOURNAL OF GEOPHYSICAL RESEARCH-ATMOSPHERES. American Geophysical Union, Washington, DC, USA, 120(23): 12,259\u201312,280, (2015).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:094"
-            ],
+            "contactPoint": {
+                "fn": "Robert Gilliam",
+                "hasEmail": "mailto:gilliam.robert@epa.gov"
+            },
+            "describedBy": "https://pasteur.epa.gov/uploads/374/documents/figure1.data.dictionary.txt",
+            "describedByType": "text/plain",
+            "description": "NetCDF file of the SREF standard deviation of wind speed and direction that was used to inject variability in the FDDA input.\r\n\r\nvariable U_NDG_OLD contains standard deviation of wind speed (m/s)\r\nvariable V_NDG_OLD contains the standard deviation of wind direction (deg). This dataset is not publicly accessible because: This is a netcdf file that is 3.9Gb. It can be accessed through the following means: On the HPC system sol (2016). In the asm archive here: /asm/grc/JGR_ENSEMBLE_ScienceHub/figure1.nc. Format: Figure 1 data. This is the variability of wind speed and direction of the four dimensional data assimilation inputs. The variability includes the 14 members of the ensemble. \n\nThis dataset is associated with the following publication:\nGilliam , R., C. Hogrefe , J. Godowitch, S. Napelenok , R. Mathur , and S.T. Rao. Impact of inherent meteorology uncertainty on air quality model predictions.   JOURNAL OF GEOPHYSICAL RESEARCH-ATMOSPHERES. American Geophysical Union, Washington, DC, USA, 120(23): 12,259\u201312,280, (2015).",
+            "distribution": [],
             "identifier": "A-6q5f-374",
             "keyword": [
                 "FDDA",
@@ -38402,14 +38402,10 @@
                 "WRF-CMAQ",
                 "Ozone"
             ],
-            "contactPoint": {
-                "fn": "Robert Gilliam",
-                "hasEmail": "mailto:gilliam.robert@epa.gov"
-            },
-            "distribution": [],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2015-07-21",
-            "references": [
-                "https://doi.org/10.1002/2015jd023674"
+            "programCode": [
+                "020:094"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -38420,21 +38416,23 @@
                     }
                 }
             },
-            "describedBy": "https://pasteur.epa.gov/uploads/374/documents/figure1.data.dictionary.txt",
-            "describedByType": "text/plain"
+            "references": [
+                "https://doi.org/10.1002/2015jd023674"
+            ],
+            "rights": null,
+            "title": "Ensemble standar deviation of wind speed and direction of the FDDA input to WRF"
         },
         {
-            "title": "Figure 3",
-            "description": "The Figure.tar.gz contains a directory for each WRF ensemble run. In these directories are *.csv files for each meteorology variable examined. These are comma delimited text files that contain statistics for each observation site. Also provided is an R script that reads these files (user would need to change directory pointers) and computes the variability of error and bias of the ensemble at each site and plots these for reproduction of figure 3. This dataset is not publicly accessible because: 30Mb tar, 15 Mb tar.gz. It can be accessed through the following means: On the EPA HPC system sol archive: /asm/grc/JGR_ENSEMBLE_ScienceHub/figure3.tar. Format: tar.gz file of text files that contain the surface meteorology statistics that were used to created Figure 3. Also included is a R script that will allow anyone interested to re-generate the figure. \n\nThis dataset is associated with the following publication:\nGilliam , R., C. Hogrefe , J. Godowitch, S. Napelenok , R. Mathur , and S.T. Rao. Impact of inherent meteorology uncertainty on air quality model predictions.   JOURNAL OF GEOPHYSICAL RESEARCH-ATMOSPHERES. American Geophysical Union, Washington, DC, USA, 120(23): 12,259\u201312,280, (2015).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:094"
-            ],
+            "contactPoint": {
+                "fn": "Robert Gilliam",
+                "hasEmail": "mailto:gilliam.robert@epa.gov"
+            },
+            "description": "The Figure.tar.gz contains a directory for each WRF ensemble run. In these directories are *.csv files for each meteorology variable examined. These are comma delimited text files that contain statistics for each observation site. Also provided is an R script that reads these files (user would need to change directory pointers) and computes the variability of error and bias of the ensemble at each site and plots these for reproduction of figure 3. This dataset is not publicly accessible because: 30Mb tar, 15 Mb tar.gz. It can be accessed through the following means: On the EPA HPC system sol archive: /asm/grc/JGR_ENSEMBLE_ScienceHub/figure3.tar. Format: tar.gz file of text files that contain the surface meteorology statistics that were used to created Figure 3. Also included is a R script that will allow anyone interested to re-generate the figure. \n\nThis dataset is associated with the following publication:\nGilliam , R., C. Hogrefe , J. Godowitch, S. Napelenok , R. Mathur , and S.T. Rao. Impact of inherent meteorology uncertainty on air quality model predictions.   JOURNAL OF GEOPHYSICAL RESEARCH-ATMOSPHERES. American Geophysical Union, Washington, DC, USA, 120(23): 12,259\u201312,280, (2015).",
+            "distribution": [],
             "identifier": "A-6q5f-375",
             "keyword": [
                 "variability",
@@ -38447,14 +38445,10 @@
                 "WRF-CMAQ",
                 "Ozone"
             ],
-            "contactPoint": {
-                "fn": "Robert Gilliam",
-                "hasEmail": "mailto:gilliam.robert@epa.gov"
-            },
-            "distribution": [],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2015-09-02",
-            "references": [
-                "https://doi.org/10.1002/2015jd023674"
+            "programCode": [
+                "020:094"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -38464,20 +38458,26 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1002/2015jd023674"
+            ],
+            "rights": null,
+            "title": "Figure 3"
         },
         {
-            "title": "Figure4",
-            "description": "NetCDF files of PBL height (m), Shortwave Radiation, 10 m wind speed from WRF and Ozone from CMAQ. The data is the standard deviation of these variables for each hour of the 4 day simulation. Figure 4 is only one of the time periods: June 8, 2100 UTC. The NetCDF files have a time stamp (Times) that can be used to find this time in order to reproduce the Figure 4. Also included is a data dictionary that describes the domain and all other attributes of the model simulation. This dataset is not publicly accessible because: The file is 202Mb binary NetCDF file that is too large. It can be accessed through the following means: Archived on the US EPA HPC Sol computer system:/asm/grc/JGR_ENSEMBLE_ScienceHub/Figure4.tar.gz. Format: Tar.gz file that contains NetCDF files required to reproduce Figure 4. \n\nThis dataset is associated with the following publication:\nGilliam , R., C. Hogrefe , J. Godowitch, S. Napelenok , R. Mathur , and S.T. Rao. Impact of inherent meteorology uncertainty on air quality model predictions.   JOURNAL OF GEOPHYSICAL RESEARCH-ATMOSPHERES. American Geophysical Union, Washington, DC, USA, 120(23): 12,259\u201312,280, (2015).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:094"
-            ],
+            "contactPoint": {
+                "fn": "Robert Gilliam",
+                "hasEmail": "mailto:gilliam.robert@epa.gov"
+            },
+            "describedBy": "https://pasteur.epa.gov/uploads/376/documents/figure4.data.dictionary.txt",
+            "describedByType": "text/plain",
+            "description": "NetCDF files of PBL height (m), Shortwave Radiation, 10 m wind speed from WRF and Ozone from CMAQ. The data is the standard deviation of these variables for each hour of the 4 day simulation. Figure 4 is only one of the time periods: June 8, 2100 UTC. The NetCDF files have a time stamp (Times) that can be used to find this time in order to reproduce the Figure 4. Also included is a data dictionary that describes the domain and all other attributes of the model simulation. This dataset is not publicly accessible because: The file is 202Mb binary NetCDF file that is too large. It can be accessed through the following means: Archived on the US EPA HPC Sol computer system:/asm/grc/JGR_ENSEMBLE_ScienceHub/Figure4.tar.gz. Format: Tar.gz file that contains NetCDF files required to reproduce Figure 4. \n\nThis dataset is associated with the following publication:\nGilliam , R., C. Hogrefe , J. Godowitch, S. Napelenok , R. Mathur , and S.T. Rao. Impact of inherent meteorology uncertainty on air quality model predictions.   JOURNAL OF GEOPHYSICAL RESEARCH-ATMOSPHERES. American Geophysical Union, Washington, DC, USA, 120(23): 12,259\u201312,280, (2015).",
+            "distribution": [],
             "identifier": "A-6q5f-376",
             "keyword": [
                 "PBL Height",
@@ -38489,14 +38489,10 @@
                 "ensemble modeling",
                 "WRF-CMAQ"
             ],
-            "contactPoint": {
-                "fn": "Robert Gilliam",
-                "hasEmail": "mailto:gilliam.robert@epa.gov"
-            },
-            "distribution": [],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2015-07-22",
-            "references": [
-                "https://doi.org/10.1002/2015jd023674"
+            "programCode": [
+                "020:094"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -38507,20 +38503,28 @@
                     }
                 }
             },
-            "describedBy": "https://pasteur.epa.gov/uploads/376/documents/figure4.data.dictionary.txt",
-            "describedByType": "text/plain"
+            "references": [
+                "https://doi.org/10.1002/2015jd023674"
+            ],
+            "rights": null,
+            "title": "Figure4"
         },
         {
-            "title": "Figure5",
-            "description": "This is an R statistics package script that allows the reproduction of Figure 5. The script includes the links to large NetCDF files that the figures access for O3, CO, wind speed, radiation and PBL height. It pulls the timeseries for each variable at a number of cities (lat-lon specified). \n\nThis dataset is associated with the following publication:\nGilliam , R., C. Hogrefe , J. Godowitch, S. Napelenok , R. Mathur , and S.T. Rao. Impact of inherent meteorology uncertainty on air quality model predictions.   JOURNAL OF GEOPHYSICAL RESEARCH-ATMOSPHERES. American Geophysical Union, Washington, DC, USA, 120(23): 12,259\u201312,280, (2015).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:094"
+            "contactPoint": {
+                "fn": "Robert Gilliam",
+                "hasEmail": "mailto:gilliam.robert@epa.gov"
+            },
+            "description": "This is an R statistics package script that allows the reproduction of Figure 5. The script includes the links to large NetCDF files that the figures access for O3, CO, wind speed, radiation and PBL height. It pulls the timeseries for each variable at a number of cities (lat-lon specified). \n\nThis dataset is associated with the following publication:\nGilliam , R., C. Hogrefe , J. Godowitch, S. Napelenok , R. Mathur , and S.T. Rao. Impact of inherent meteorology uncertainty on air quality model predictions.   JOURNAL OF GEOPHYSICAL RESEARCH-ATMOSPHERES. American Geophysical Union, Washington, DC, USA, 120(23): 12,259\u201312,280, (2015).",
+            "distribution": [
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/377/Figure5.txt",
+                    "mediaType": "text/plain",
+                    "title": "Figure5.txt"
+                }
             ],
             "identifier": "A-6q5f-377",
             "keyword": [
@@ -38535,20 +38539,10 @@
                 "WRF-CMAQ",
                 "Ozone"
             ],
-            "contactPoint": {
-                "fn": "Robert Gilliam",
-                "hasEmail": "mailto:gilliam.robert@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "Figure5.txt",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/377/Figure5.txt",
-                    "mediaType": "text/plain"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2012-10-01",
-            "references": [
-                "https://doi.org/10.1002/2015jd023674"
+            "programCode": [
+                "020:094"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -38558,19 +38552,29 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1002/2015jd023674"
+            ],
+            "rights": null,
+            "title": "Figure5"
         },
         {
-            "title": "Figure6",
-            "description": "R script for the reproduction of Figure6. This script accesses archived CMAQ and WRF model output on US EPA's HPC sol computer system and plots forward trajectories and ozone concentrations from major cities in the US. \n\nThis dataset is associated with the following publication:\nGilliam , R., C. Hogrefe , J. Godowitch, S. Napelenok , R. Mathur , and S.T. Rao. Impact of inherent meteorology uncertainty on air quality model predictions.   JOURNAL OF GEOPHYSICAL RESEARCH-ATMOSPHERES. American Geophysical Union, Washington, DC, USA, 120(23): 12,259\u201312,280, (2015).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:094"
+            "contactPoint": {
+                "fn": "Robert Gilliam",
+                "hasEmail": "mailto:gilliam.robert@epa.gov"
+            },
+            "description": "R script for the reproduction of Figure6. This script accesses archived CMAQ and WRF model output on US EPA's HPC sol computer system and plots forward trajectories and ozone concentrations from major cities in the US. \n\nThis dataset is associated with the following publication:\nGilliam , R., C. Hogrefe , J. Godowitch, S. Napelenok , R. Mathur , and S.T. Rao. Impact of inherent meteorology uncertainty on air quality model predictions.   JOURNAL OF GEOPHYSICAL RESEARCH-ATMOSPHERES. American Geophysical Union, Washington, DC, USA, 120(23): 12,259\u201312,280, (2015).",
+            "distribution": [
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/379/Figure6.txt",
+                    "mediaType": "text/plain",
+                    "title": "Figure6.txt"
+                }
             ],
             "identifier": "A-6q5f-379",
             "keyword": [
@@ -38581,20 +38585,10 @@
                 "WRF-CMAQ",
                 "Ozone"
             ],
-            "contactPoint": {
-                "fn": "Robert Gilliam",
-                "hasEmail": "mailto:gilliam.robert@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "Figure6.txt",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/379/Figure6.txt",
-                    "mediaType": "text/plain"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2013-02-12",
-            "references": [
-                "https://doi.org/10.1002/2015jd023674"
+            "programCode": [
+                "020:094"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -38604,49 +38598,49 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1002/2015jd023674"
+            ],
+            "rights": null,
+            "title": "Figure6"
         },
         {
-            "title": "Figure 7",
-            "description": "Two files provided. The ENS.tar file contains text data files (*.csv) used to create Figure 7 and Figure 8. The Figure7.txt is an R script that reads these files and generates the plots for various cities including the four published in Figure 7 and Figure 8. \n\nThis dataset is associated with the following publication:\nGilliam , R., C. Hogrefe , J. Godowitch, S. Napelenok , R. Mathur , and S.T. Rao. Impact of inherent meteorology uncertainty on air quality model predictions.   JOURNAL OF GEOPHYSICAL RESEARCH-ATMOSPHERES. American Geophysical Union, Washington, DC, USA, 120(23): 12,259\u201312,280, (2015).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:094"
-            ],
-            "identifier": "A-6q5f-380",
-            "keyword": [
-                "variability",
-                "O3",
-                "Probablistic Evaluation",
-                "probabilistic modeling",
-                "ensemble modeling",
-                "WRF-CMAQ",
-                "Ozone"
-            ],
             "contactPoint": {
                 "fn": "Robert Gilliam",
                 "hasEmail": "mailto:gilliam.robert@epa.gov"
             },
+            "description": "Two files provided. The ENS.tar file contains text data files (*.csv) used to create Figure 7 and Figure 8. The Figure7.txt is an R script that reads these files and generates the plots for various cities including the four published in Figure 7 and Figure 8. \n\nThis dataset is associated with the following publication:\nGilliam , R., C. Hogrefe , J. Godowitch, S. Napelenok , R. Mathur , and S.T. Rao. Impact of inherent meteorology uncertainty on air quality model predictions.   JOURNAL OF GEOPHYSICAL RESEARCH-ATMOSPHERES. American Geophysical Union, Washington, DC, USA, 120(23): 12,259\u201312,280, (2015).",
             "distribution": [
                 {
-                    "title": "ENS.city.tar",
                     "downloadURL": "https://pasteur.epa.gov/uploads/380/ENS.city.tar",
-                    "mediaType": "application/x-tar"
+                    "mediaType": "application/x-tar",
+                    "title": "ENS.city.tar"
                 },
                 {
-                    "title": "Figure7.txt",
                     "downloadURL": "https://pasteur.epa.gov/uploads/380/Figure7.txt",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "Figure7.txt"
                 }
             ],
+            "identifier": "A-6q5f-380",
+            "keyword": [
+                "variability",
+                "O3",
+                "Probablistic Evaluation",
+                "probabilistic modeling",
+                "ensemble modeling",
+                "WRF-CMAQ",
+                "Ozone"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2015-08-03",
-            "references": [
-                "https://doi.org/10.1002/2015jd023674"
+            "programCode": [
+                "020:094"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -38656,20 +38650,24 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1002/2015jd023674"
+            ],
+            "rights": null,
+            "title": "Figure 7"
         },
         {
-            "title": "Figure 9",
-            "description": "This is a NetCDF file in ioapi format that contains the probability that ozone is above the 8 hr max O3 standard for the four days of the simulation. This dataset is not publicly accessible because: The file size is a large binary NetCDF file of 56Mb. It can be accessed through the following means: File is located on US EPA's HPC system sol file archive: /asm/grc/JGR_ENSEMBLE_ScienceHub/Figure9.nc. Format: NetCDF file that contains the O3 gridded data to reproduce Figure 9. \n\nThis dataset is associated with the following publication:\nGilliam , R., C. Hogrefe , J. Godowitch, S. Napelenok , R. Mathur , and S.T. Rao. Impact of inherent meteorology uncertainty on air quality model predictions.   JOURNAL OF GEOPHYSICAL RESEARCH-ATMOSPHERES. American Geophysical Union, Washington, DC, USA, 120(23): 12,259\u201312,280, (2015).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:094"
-            ],
+            "contactPoint": {
+                "fn": "Robert Gilliam",
+                "hasEmail": "mailto:gilliam.robert@epa.gov"
+            },
+            "description": "This is a NetCDF file in ioapi format that contains the probability that ozone is above the 8 hr max O3 standard for the four days of the simulation. This dataset is not publicly accessible because: The file size is a large binary NetCDF file of 56Mb. It can be accessed through the following means: File is located on US EPA's HPC system sol file archive: /asm/grc/JGR_ENSEMBLE_ScienceHub/Figure9.nc. Format: NetCDF file that contains the O3 gridded data to reproduce Figure 9. \n\nThis dataset is associated with the following publication:\nGilliam , R., C. Hogrefe , J. Godowitch, S. Napelenok , R. Mathur , and S.T. Rao. Impact of inherent meteorology uncertainty on air quality model predictions.   JOURNAL OF GEOPHYSICAL RESEARCH-ATMOSPHERES. American Geophysical Union, Washington, DC, USA, 120(23): 12,259\u201312,280, (2015).",
+            "distribution": [],
             "identifier": "A-6q5f-381",
             "keyword": [
                 "O3",
@@ -38679,14 +38677,10 @@
                 "WRF-CMAQ",
                 "Ozone"
             ],
-            "contactPoint": {
-                "fn": "Robert Gilliam",
-                "hasEmail": "mailto:gilliam.robert@epa.gov"
-            },
-            "distribution": [],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2015-07-22",
-            "references": [
-                "https://doi.org/10.1002/2015jd023674"
+            "programCode": [
+                "020:094"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -38696,50 +38690,49 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1002/2015jd023674"
+            ],
+            "rights": null,
+            "title": "Figure 9"
         },
         {
-            "title": "Data from Phelan et al. 2016 (Water Air and Soil Pollution 227:84. DOI 10.1007/s11270-016-2762-x). \"Assessing the effects of climate change and air pollution on soil properties and plant diversity in sugar-maple-beech-yellow birch hardwood...\"",
-            "description": "This dataset describes the simulations at two pilot sites in the northeast from 1900-2100 for several soil and plant community responses to climate and nitrogen deposition across a number of future scenarios. \n\nThis dataset is associated with the following publications:\nPhelan, J., S. Belyazid, C. Clark , P. Jones, and J. Cajka. Assessing the Effects of Climate Change and Air Pollution on Soil Properties and Plant Diversity in Sugar Maple-Beech-Yellow Birch Hardwood Forests in the Northeastern United States:  Model Simulations from 1900-2100.   WATER, AIR, & SOIL POLLUTION. Springer, New York, NY, USA, 227(3): 1-30, (2016).\nBelyazid, S., J. Phelan, B. Nihlgard, H. Sverdrup, C. Driscoll, I. Fernandez, J. Aherne, L.M. Teeling-Adams, S. Bailey, M. Arsenault, N. Cleavitt, B. Engstrom, R. Dennis, D. Sperduto, D. Werier, and C. Clark. Assessing the Effects of Climate Change and Air Pollution on Soil Properties and Plant Diversity in Northeastern U.S. Hardwood Forests: Model Setup and Evaluation.   WATER, AIR, & SOIL POLLUTION. Springer, New York, NY, USA, 230: 106, (2019).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:094"
-            ],
-            "identifier": "A-c5b9-356",
-            "keyword": [
-                "nitrogen",
-                "nitrogen deposition",
-                "critical loads",
-                "air quality",
-                "biogeochemical cycling",
-                "ecosystem services",
-                "biodiversity"
-            ],
             "contactPoint": {
                 "fn": "Christopher Clark",
                 "hasEmail": "mailto:clark.christopher@epa.gov"
             },
+            "description": "This dataset describes the simulations at two pilot sites in the northeast from 1900-2100 for several soil and plant community responses to climate and nitrogen deposition across a number of future scenarios. \n\nThis dataset is associated with the following publications:\nPhelan, J., S. Belyazid, C. Clark , P. Jones, and J. Cajka. Assessing the Effects of Climate Change and Air Pollution on Soil Properties and Plant Diversity in Sugar Maple-Beech-Yellow Birch Hardwood Forests in the Northeastern United States:  Model Simulations from 1900-2100.   WATER, AIR, & SOIL POLLUTION. Springer, New York, NY, USA, 227(3): 1-30, (2016).\nBelyazid, S., J. Phelan, B. Nihlgard, H. Sverdrup, C. Driscoll, I. Fernandez, J. Aherne, L.M. Teeling-Adams, S. Bailey, M. Arsenault, N. Cleavitt, B. Engstrom, R. Dennis, D. Sperduto, D. Werier, and C. Clark. Assessing the Effects of Climate Change and Air Pollution on Soil Properties and Plant Diversity in Northeastern U.S. Hardwood Forests: Model Setup and Evaluation.   WATER, AIR, & SOIL POLLUTION. Springer, New York, NY, USA, 230: 106, (2019).",
             "distribution": [
                 {
-                    "title": "Model_data_file_catalogue_FSV-Scen.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/356/Model_data_file_catalogue_FSV-Scen.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Model_data_file_catalogue_FSV-Scen.xlsx"
                 },
                 {
-                    "title": "Data_Zipped.zip",
                     "downloadURL": "https://pasteur.epa.gov/uploads/356/Data_Zipped.zip",
-                    "mediaType": "application/x-zip-compressed"
+                    "mediaType": "application/x-zip-compressed",
+                    "title": "Data_Zipped.zip"
                 }
             ],
+            "identifier": "A-c5b9-356",
+            "keyword": [
+                "nitrogen",
+                "nitrogen deposition",
+                "critical loads",
+                "air quality",
+                "biogeochemical cycling",
+                "ecosystem services",
+                "biodiversity"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2016-07-08",
-            "references": [
-                "https://doi.org/10.1007/s11270-016-2762-x",
-                "https://doi.org/10.1007/s11270-019-4145-6"
+            "programCode": [
+                "020:094"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -38749,19 +38742,30 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1007/s11270-016-2762-x",
+                "https://doi.org/10.1007/s11270-019-4145-6"
+            ],
+            "rights": null,
+            "title": "Data from Phelan et al. 2016 (Water Air and Soil Pollution 227:84. DOI 10.1007/s11270-016-2762-x). \"Assessing the effects of climate change and air pollution on soil properties and plant diversity in sugar-maple-beech-yellow birch hardwood...\""
         },
         {
-            "title": "Pb Speciation Data to Estimate Lead Bioavailability to Quail",
-            "description": "Linear combination fitting data for lead speciation of soil samples evaluated through an in-vivo/in-vitro correlation for quail exposure. \n\nThis dataset is associated with the following publication:\nBeyer, W.N., N. Basta, R. Chaney, P. Henry, D. Mosby, B. Rattner, K. Scheckel , D. Sprague, and J. Weber. BIOACCESSIBILITY TESTS ACCURATELY ESTIMATE BIOAVAILABILITY OF LEAD TO QUAIL.  G.A. Burton, Jr., and C. H. Ward  ENVIRONMENTAL TOXICOLOGY AND CHEMISTRY. Society of Environmental Toxicology and Chemistry, Pensacola, FL, USA, 35(9): 2311-2319, (2016).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:097"
+            "contactPoint": {
+                "fn": "Kirk Scheckel",
+                "hasEmail": "mailto:scheckel.kirk@epa.gov"
+            },
+            "description": "Linear combination fitting data for lead speciation of soil samples evaluated through an in-vivo/in-vitro correlation for quail exposure. \n\nThis dataset is associated with the following publication:\nBeyer, W.N., N. Basta, R. Chaney, P. Henry, D. Mosby, B. Rattner, K. Scheckel , D. Sprague, and J. Weber. BIOACCESSIBILITY TESTS ACCURATELY ESTIMATE BIOAVAILABILITY OF LEAD TO QUAIL.  G.A. Burton, Jr., and C. H. Ward  ENVIRONMENTAL TOXICOLOGY AND CHEMISTRY. Society of Environmental Toxicology and Chemistry, Pensacola, FL, USA, 35(9): 2311-2319, (2016).",
+            "distribution": [
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/383/BeyeretalQuailPbPaper_LCFDate_Table3.xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "BeyeretalQuailPbPaper_LCFDate_Table3.xlsx"
+                }
             ],
             "identifier": "A-66t7-383",
             "keyword": [
@@ -38772,20 +38776,10 @@
                 "soil amendments",
                 "wildlife toxicology"
             ],
-            "contactPoint": {
-                "fn": "Kirk Scheckel",
-                "hasEmail": "mailto:scheckel.kirk@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "BeyeretalQuailPbPaper_LCFDate_Table3.xlsx",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/383/BeyeretalQuailPbPaper_LCFDate_Table3.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2016-05-09",
-            "references": [
-                "https://doi.org/10.1002/etc.3399"
+            "programCode": [
+                "020:097"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -38795,34 +38789,34 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1002/etc.3399"
+            ],
+            "rights": null,
+            "title": "Pb Speciation Data to Estimate Lead Bioavailability to Quail"
         },
         {
-            "title": "an Integrated science based methodology",
-            "description": "The data is secondary in nature.  Meaning that no data was generated as part of this review effort.  Rather, data that was available in the peer-reviewed literature was used. This dataset is not publicly accessible because: This is a review manuscript, there was not data generated under this effort. All data used was secondary data and sources of the data were identified in the manuscript. It can be accessed through the following means: there is no database. Format: there is no data base. \n\nThis dataset is associated with the following publication:\nTolaymat , T., A. El Badawy, R. Sequeira, and A. Genaidy. An integrated science-based methodology to assess potential risks and implications of engineered nanomaterials.  Diana Aga, Wonyong Choi, Andrew Daugulis, Gianluca Li Puma, Gerasimos Lyberatos, and Joo Hwa Tay  JOURNAL OF HAZARDOUS MATERIALS. Elsevier Science Ltd, New York, NY, USA, 298: 270-281, (2015).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:095"
-            ],
+            "contactPoint": {
+                "fn": "Thabet Tolaymat",
+                "hasEmail": "mailto:tolaymat.thabet@epa.gov"
+            },
+            "description": "The data is secondary in nature.  Meaning that no data was generated as part of this review effort.  Rather, data that was available in the peer-reviewed literature was used. This dataset is not publicly accessible because: This is a review manuscript, there was not data generated under this effort. All data used was secondary data and sources of the data were identified in the manuscript. It can be accessed through the following means: there is no database. Format: there is no data base. \n\nThis dataset is associated with the following publication:\nTolaymat , T., A. El Badawy, R. Sequeira, and A. Genaidy. An integrated science-based methodology to assess potential risks and implications of engineered nanomaterials.  Diana Aga, Wonyong Choi, Andrew Daugulis, Gianluca Li Puma, Gerasimos Lyberatos, and Joo Hwa Tay  JOURNAL OF HAZARDOUS MATERIALS. Elsevier Science Ltd, New York, NY, USA, 298: 270-281, (2015).",
+            "distribution": [],
             "identifier": "A-k0pj-378",
             "keyword": [
                 "nanomaterials",
                 "Risk",
                 "Methodology"
             ],
-            "contactPoint": {
-                "fn": "Thabet Tolaymat",
-                "hasEmail": "mailto:tolaymat.thabet@epa.gov"
-            },
-            "distribution": [],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2016-09-09",
-            "references": [
-                "https://doi.org/10.1016/j.jhazmat.2015.04.019"
+            "programCode": [
+                "020:095"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -38832,19 +38826,29 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.jhazmat.2015.04.019"
+            ],
+            "rights": null,
+            "title": "an Integrated science based methodology"
         },
         {
-            "title": "In vivo plasma concentration for lindane after 6 hour exposure in human skin",
-            "description": "Dataset is a time course description of lindane disappearance in blood plasma after dermal exposure in human volunteers. \n\nThis dataset is associated with the following publication:\nSawyer, M.E., M.V. Evans , C. Wilson, L.J. Beesley, L. Leon, C. Eklund , E. Croom, and R. Pegram. Development of a Human Physiologically Based Pharmacokinetics (PBPK) Model For Dermal Permeability for Lindane.   TOXICOLOGY LETTERS. Elsevier Science Ltd, New York, NY, USA, 14(245): pp106-109, (2016).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
+            "contactPoint": {
+                "fn": "Marina Evans",
+                "hasEmail": "mailto:evans.marina@epa.gov"
+            },
+            "description": "Dataset is a time course description of lindane disappearance in blood plasma after dermal exposure in human volunteers. \n\nThis dataset is associated with the following publication:\nSawyer, M.E., M.V. Evans , C. Wilson, L.J. Beesley, L. Leon, C. Eklund , E. Croom, and R. Pegram. Development of a Human Physiologically Based Pharmacokinetics (PBPK) Model For Dermal Permeability for Lindane.   TOXICOLOGY LETTERS. Elsevier Science Ltd, New York, NY, USA, 14(245): pp106-109, (2016).",
+            "distribution": [
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/313/sawyer_2016_sciencehib.xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "sawyer_2016_sciencehib.xlsx"
+                }
             ],
             "identifier": "A-0cfz-313",
             "keyword": [
@@ -38859,20 +38863,10 @@
                 "dermal lag time",
                 "dermal cumulative absorption"
             ],
-            "contactPoint": {
-                "fn": "Marina Evans",
-                "hasEmail": "mailto:evans.marina@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "sawyer_2016_sciencehib.xlsx",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/313/sawyer_2016_sciencehib.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2016-09-14",
-            "references": [
-                "https://doi.org/10.1016/j.toxlet.2016.01.008"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -38882,19 +38876,29 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.toxlet.2016.01.008"
+            ],
+            "rights": null,
+            "title": "In vivo plasma concentration for lindane after 6 hour exposure in human skin"
         },
         {
-            "title": "Data submission for A-d25f",
-            "description": "Includes 1) list of genes in the STAT5b biomarker and 2) list of accession numbers for microarray datasets used in study. \n\nThis dataset is associated with the following publication:\nOshida, K., N. Vasani, D. Waxman, and C. Corton. Disruption of STAT5b-Regulated Sexual Dimorphism of the Liver Transcriptome by Diverse Factors Is a Common Event.   PLoS ONE. Public Library of Science, San Francisco, CA, USA, 11(3): NA, (2016).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:095"
+            "contactPoint": {
+                "fn": "Jon Corton",
+                "hasEmail": "mailto:corton.chris@epa.gov"
+            },
+            "description": "Includes 1) list of genes in the STAT5b biomarker and 2) list of accession numbers for microarray datasets used in study. \n\nThis dataset is associated with the following publication:\nOshida, K., N. Vasani, D. Waxman, and C. Corton. Disruption of STAT5b-Regulated Sexual Dimorphism of the Liver Transcriptome by Diverse Factors Is a Common Event.   PLoS ONE. Public Library of Science, San Francisco, CA, USA, 11(3): NA, (2016).",
+            "distribution": [
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/177/Data%20submission%20for%20A-d25f.xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Data submission for A-d25f.xlsx"
+                }
             ],
             "identifier": "A-d25f-177",
             "keyword": [
@@ -38906,20 +38910,10 @@
                 "androgens",
                 "estrogens"
             ],
-            "contactPoint": {
-                "fn": "Jon Corton",
-                "hasEmail": "mailto:corton.chris@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "Data submission for A-d25f.xlsx",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/177/Data%20submission%20for%20A-d25f.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2016-03-01",
-            "references": [
-                "https://doi.org/10.1371/journal.pone.0148308"
+            "programCode": [
+                "020:095"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -38929,19 +38923,29 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1371/journal.pone.0148308"
+            ],
+            "rights": null,
+            "title": "Data submission for A-d25f"
         },
         {
-            "title": "Data submission for A-p8dg",
-            "description": "Accession numbers for microarray datasets used in Oshida et al. Chemical and Hormonal Effects on STAT5b-Dependent Sexual Dimorphism of the Liver Transcriptome.  PLoS One. 2016 Mar 9;11(3):e0150284. \n\nThis dataset is associated with the following publication:\nOshida, K., D. Waxman, and C. Corton. Chemical and Hormonal Effects on STAT5b-Dependent Sexual Dimorphism of the Liver Transcriptome..   PLoS ONE. Public Library of Science, San Francisco, CA, USA, 11(3): NA, (2016).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:095"
+            "contactPoint": {
+                "fn": "Jon Corton",
+                "hasEmail": "mailto:corton.chris@epa.gov"
+            },
+            "description": "Accession numbers for microarray datasets used in Oshida et al. Chemical and Hormonal Effects on STAT5b-Dependent Sexual Dimorphism of the Liver Transcriptome.  PLoS One. 2016 Mar 9;11(3):e0150284. \n\nThis dataset is associated with the following publication:\nOshida, K., D. Waxman, and C. Corton. Chemical and Hormonal Effects on STAT5b-Dependent Sexual Dimorphism of the Liver Transcriptome..   PLoS ONE. Public Library of Science, San Francisco, CA, USA, 11(3): NA, (2016).",
+            "distribution": [
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/181/Data%20submission%20for%20A-p8dg.xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Data submission for A-p8dg.xlsx"
+                }
             ],
             "identifier": "A-p8dg-181",
             "keyword": [
@@ -38954,20 +38958,10 @@
                 "growth hormone",
                 "hypothalamic-pituitary-liver axis"
             ],
-            "contactPoint": {
-                "fn": "Jon Corton",
-                "hasEmail": "mailto:corton.chris@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "Data submission for A-p8dg.xlsx",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/181/Data%20submission%20for%20A-p8dg.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2016-03-01",
-            "references": [
-                "https://doi.org/10.1371/journal.pone.0150284"
+            "programCode": [
+                "020:095"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -38977,19 +38971,29 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1371/journal.pone.0150284"
+            ],
+            "rights": null,
+            "title": "Data submission for A-p8dg"
         },
         {
-            "title": "Data submission for A-0k6f",
-            "description": "List of biomarker genes used to predict estrogen receptor activity in MCF-7 cells; list of microarray accession numbers used in the study. \n\nThis dataset is associated with the following publication:\nVanduyn, N., B. Chorley , R. Tice, R. Judson , and C. Corton. Moving Toward Integrating Gene Expression Profiling into High-throughput Testing:A Gene Expression Biomarker Accurately Predicts Estrogen Receptor \u03b1 Modulation in a Microarray Compendium.   TOXICOLOGICAL SCIENCES. Society of Toxicology,    151(1): 88-103, (2016).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:095"
+            "contactPoint": {
+                "fn": "Jon Corton",
+                "hasEmail": "mailto:corton.chris@epa.gov"
+            },
+            "description": "List of biomarker genes used to predict estrogen receptor activity in MCF-7 cells; list of microarray accession numbers used in the study. \n\nThis dataset is associated with the following publication:\nVanduyn, N., B. Chorley , R. Tice, R. Judson , and C. Corton. Moving Toward Integrating Gene Expression Profiling into High-throughput Testing:A Gene Expression Biomarker Accurately Predicts Estrogen Receptor \u03b1 Modulation in a Microarray Compendium.   TOXICOLOGICAL SCIENCES. Society of Toxicology,    151(1): 88-103, (2016).",
+            "distribution": [
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/182/Data%20submission%20for%20A-0k6f.xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Data submission for A-0k6f.xlsx"
+                }
             ],
             "identifier": "A-0k6f-182",
             "keyword": [
@@ -39000,20 +39004,10 @@
                 "transcriptomics",
                 "microarray"
             ],
-            "contactPoint": {
-                "fn": "Jon Corton",
-                "hasEmail": "mailto:corton.chris@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "Data submission for A-0k6f.xlsx",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/182/Data%20submission%20for%20A-0k6f.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2016-01-01",
-            "references": [
-                "https://doi.org/10.1093/toxsci/kfw026"
+            "programCode": [
+                "020:095"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -39023,19 +39017,29 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1093/toxsci/kfw026"
+            ],
+            "rights": null,
+            "title": "Data submission for A-0k6f"
         },
         {
-            "title": "Data submission for A-gf27",
-            "description": "Biomarker genes used to predict AhR activity; accession numbers of microarray datasets used in the study. \n\nThis dataset is associated with the following publication:\nOshida, K., N. Vasani, W. Ward , R. Thomas , D. Applegate, F. Gonzalez, L. Aleksunes, C. Klaassen, and C. Corton. Screening a mouse liver gene expression Compendium Identifies Effectors of the Aryl Hydrocarbon reeptors (AhR).   TOXICOLOGICAL SCIENCES. Society of Toxicology,    336: 99-112, (2015).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:095"
+            "contactPoint": {
+                "fn": "Jon Corton",
+                "hasEmail": "mailto:corton.chris@epa.gov"
+            },
+            "description": "Biomarker genes used to predict AhR activity; accession numbers of microarray datasets used in the study. \n\nThis dataset is associated with the following publication:\nOshida, K., N. Vasani, W. Ward , R. Thomas , D. Applegate, F. Gonzalez, L. Aleksunes, C. Klaassen, and C. Corton. Screening a mouse liver gene expression Compendium Identifies Effectors of the Aryl Hydrocarbon reeptors (AhR).   TOXICOLOGICAL SCIENCES. Society of Toxicology,    336: 99-112, (2015).",
+            "distribution": [
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/183/Data%20submission%20for%20A-gf27.xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Data submission for A-gf27.xlsx"
+                }
             ],
             "identifier": "A-gf27-183",
             "keyword": [
@@ -39049,20 +39053,10 @@
                 "pregnane x receptor (PXR)",
                 "peroxisome proliferator activated receptor alpha"
             ],
-            "contactPoint": {
-                "fn": "Jon Corton",
-                "hasEmail": "mailto:corton.chris@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "Data submission for A-gf27.xlsx",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/183/Data%20submission%20for%20A-gf27.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2016-01-01",
-            "references": [
-                "https://doi.org/10.1016/j.tox.2015.07.005"
+            "programCode": [
+                "020:095"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -39072,40 +39066,42 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.tox.2015.07.005"
+            ],
+            "rights": null,
+            "title": "Data submission for A-gf27"
         },
         {
-            "title": "Effect of genetic strain and gender on age-related changes in body composition of the laboratory rat.",
-            "description": "Body composition data for common laboratory strains of rat as a function of age. \n\nThis dataset is associated with the following publication:\nGordon , C., K. Jarema , A. Johnstone , and P. Phillips. Effect of Genetic Strain and Gender on Age-Related Changes in Body Composition of the Laboratory Rat.   Physiology & Behavior. Elsevier B.V., Amsterdam,  NETHERLANDS, 153(1): 56-63, (2016).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "A-tqkb-176",
-            "keyword": [
-                "Genetic strain",
-                "gender",
-                "Aging",
-                "Body composition"
-            ],
             "contactPoint": {
                 "fn": "Christopher Gordon",
                 "hasEmail": "mailto:gordon.christopher@epa.gov"
             },
+            "description": "Body composition data for common laboratory strains of rat as a function of age. \n\nThis dataset is associated with the following publication:\nGordon , C., K. Jarema , A. Johnstone , and P. Phillips. Effect of Genetic Strain and Gender on Age-Related Changes in Body Composition of the Laboratory Rat.   Physiology & Behavior. Elsevier B.V., Amsterdam,  NETHERLANDS, 153(1): 56-63, (2016).",
             "distribution": [
                 {
-                    "title": "E314 Science hub Effects of Genetic Strain and aging Data for MS.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/176/E314%20Science%20hub%20Effects%20of%20Genetic%20Strain%20and%20aging%20Data%20for%20MS.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "E314 Science hub Effects of Genetic Strain and aging Data for MS.xlsx"
                 }
             ],
+            "identifier": "A-tqkb-176",
+            "keyword": [
+                "Genetic strain",
+                "gender",
+                "Aging",
+                "Body composition"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2016-03-11",
-            "references": null,
+            "programCode": [
+                "020:000"
+            ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
                 "subOrganizationOf": {
@@ -39114,19 +39110,27 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": null,
+            "rights": null,
+            "title": "Effect of genetic strain and gender on age-related changes in body composition of the laboratory rat."
         },
         {
-            "title": "Figure10",
-            "description": "Fortran/NCARgraphics program to compute and plot RRF mean and variability:map_rrf_variability_13runs_epimax.f\r\n\r\nIoapi files needed by Fortran/NCARGraphics code:\r\nCMAQ.CONC.SREF.June2011.New.13runs.o3_8hrdm\r\nCMAQ.CONC.SREF.June2011.N50V25.New.13runs.o3_8hrdm\r\nGRIDCRO2D_060607\r\n\r\nPlotting routines \r\nmap_rrf_mean_sigma_ne_13runs_epimax.ps\r\nmap_rrf_mean_sigma_ne_13runs_epimax.ncgm. \n\nThis dataset is associated with the following publication:\nGilliam , R., C. Hogrefe , J. Godowitch, S. Napelenok , R. Mathur , and S.T. Rao. Impact of inherent meteorology uncertainty on air quality model predictions.   JOURNAL OF GEOPHYSICAL RESEARCH-ATMOSPHERES. American Geophysical Union, Washington, DC, USA, 120(23): 12,259\u201312,280, (2015).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:094"
+            "contactPoint": {
+                "fn": "Robert Gilliam",
+                "hasEmail": "mailto:gilliam.robert@epa.gov"
+            },
+            "description": "Fortran/NCARgraphics program to compute and plot RRF mean and variability:map_rrf_variability_13runs_epimax.f\r\n\r\nIoapi files needed by Fortran/NCARGraphics code:\r\nCMAQ.CONC.SREF.June2011.New.13runs.o3_8hrdm\r\nCMAQ.CONC.SREF.June2011.N50V25.New.13runs.o3_8hrdm\r\nGRIDCRO2D_060607\r\n\r\nPlotting routines \r\nmap_rrf_mean_sigma_ne_13runs_epimax.ps\r\nmap_rrf_mean_sigma_ne_13runs_epimax.ncgm. \n\nThis dataset is associated with the following publication:\nGilliam , R., C. Hogrefe , J. Godowitch, S. Napelenok , R. Mathur , and S.T. Rao. Impact of inherent meteorology uncertainty on air quality model predictions.   JOURNAL OF GEOPHYSICAL RESEARCH-ATMOSPHERES. American Geophysical Union, Washington, DC, USA, 120(23): 12,259\u201312,280, (2015).",
+            "distribution": [
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/387/Figure10.tar",
+                    "mediaType": "application/x-tar",
+                    "title": "Figure10.tar"
+                }
             ],
             "identifier": "A-6q5f-387",
             "keyword": [
@@ -39139,20 +39143,10 @@
                 "WRF-CMAQ",
                 "Ozone"
             ],
-            "contactPoint": {
-                "fn": "Robert Gilliam",
-                "hasEmail": "mailto:gilliam.robert@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "Figure10.tar",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/387/Figure10.tar",
-                    "mediaType": "application/x-tar"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2012-11-02",
-            "references": [
-                "https://doi.org/10.1002/2015jd023674"
+            "programCode": [
+                "020:094"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -39162,19 +39156,29 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1002/2015jd023674"
+            ],
+            "rights": null,
+            "title": "Figure10"
         },
         {
-            "title": "Figure11",
-            "description": "R script: ensemble_rrf_sigma_vs_mean_play.R\r\nData: ensemble_mean_sigma_rrf_allgrids_epismax_new_13runs.csv\r\nPlot: boxplot_ensemble_rrf_sigma_vs_mean_nowater_new_13runs_epimax.pdf. \n\nThis dataset is associated with the following publication:\nGilliam , R., C. Hogrefe , J. Godowitch, S. Napelenok , R. Mathur , and S.T. Rao. Impact of inherent meteorology uncertainty on air quality model predictions.   JOURNAL OF GEOPHYSICAL RESEARCH-ATMOSPHERES. American Geophysical Union, Washington, DC, USA, 120(23): 12,259\u201312,280, (2015).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:094"
+            "contactPoint": {
+                "fn": "Robert Gilliam",
+                "hasEmail": "mailto:gilliam.robert@epa.gov"
+            },
+            "description": "R script: ensemble_rrf_sigma_vs_mean_play.R\r\nData: ensemble_mean_sigma_rrf_allgrids_epismax_new_13runs.csv\r\nPlot: boxplot_ensemble_rrf_sigma_vs_mean_nowater_new_13runs_epimax.pdf. \n\nThis dataset is associated with the following publication:\nGilliam , R., C. Hogrefe , J. Godowitch, S. Napelenok , R. Mathur , and S.T. Rao. Impact of inherent meteorology uncertainty on air quality model predictions.   JOURNAL OF GEOPHYSICAL RESEARCH-ATMOSPHERES. American Geophysical Union, Washington, DC, USA, 120(23): 12,259\u201312,280, (2015).",
+            "distribution": [
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/388/Figure11.tar",
+                    "mediaType": "application/x-tar",
+                    "title": "Figure11.tar"
+                }
             ],
             "identifier": "A-6q5f-388",
             "keyword": [
@@ -39185,20 +39189,10 @@
                 "ensemble modeling",
                 "WRF-CMAQ"
             ],
-            "contactPoint": {
-                "fn": "Robert Gilliam",
-                "hasEmail": "mailto:gilliam.robert@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "Figure11.tar",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/388/Figure11.tar",
-                    "mediaType": "application/x-tar"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2012-11-13",
-            "references": [
-                "https://doi.org/10.1002/2015jd023674"
+            "programCode": [
+                "020:094"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -39208,20 +39202,24 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1002/2015jd023674"
+            ],
+            "rights": null,
+            "title": "Figure11"
         },
         {
-            "title": "Figure12",
-            "description": "NCL script: cmaq_ensemble_isam_4panels_subdomain.ncl\r\n\r\nNetcdf input file for NCL script, containing ensemble means and standard deviation of ISAM SO4 and O3 contributions from IPM: test.nc\r\n\r\nPlot (ps): maps_isam_mean_std_lasthour_ipm_so4_o3_east.ps\r\n\r\nPlot (pdf): maps_isam_mean_std_lasthour_ipm_so4_o3_east.pdf\r\n\r\nPlot (ncgm): maps_isam_mean_std_lasthour_ipm_so4_o3_east.ncgm. This dataset is not publicly accessible because: This contains a dataset that is well over 1Gb, so link provided to US EPA's HPC system where all information can be retrieved. It can be accessed through the following means: /asm/grc/JGR_ENSEMBLE_ScienceHub/Figure12.tar.gz. Format: Tar file with scripts and datasets needed to reproduce Figure 12. \n\nThis dataset is associated with the following publication:\nGilliam , R., C. Hogrefe , J. Godowitch, S. Napelenok , R. Mathur , and S.T. Rao. Impact of inherent meteorology uncertainty on air quality model predictions.   JOURNAL OF GEOPHYSICAL RESEARCH-ATMOSPHERES. American Geophysical Union, Washington, DC, USA, 120(23): 12,259\u201312,280, (2015).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:094"
-            ],
+            "contactPoint": {
+                "fn": "Robert Gilliam",
+                "hasEmail": "mailto:gilliam.robert@epa.gov"
+            },
+            "description": "NCL script: cmaq_ensemble_isam_4panels_subdomain.ncl\r\n\r\nNetcdf input file for NCL script, containing ensemble means and standard deviation of ISAM SO4 and O3 contributions from IPM: test.nc\r\n\r\nPlot (ps): maps_isam_mean_std_lasthour_ipm_so4_o3_east.ps\r\n\r\nPlot (pdf): maps_isam_mean_std_lasthour_ipm_so4_o3_east.pdf\r\n\r\nPlot (ncgm): maps_isam_mean_std_lasthour_ipm_so4_o3_east.ncgm. This dataset is not publicly accessible because: This contains a dataset that is well over 1Gb, so link provided to US EPA's HPC system where all information can be retrieved. It can be accessed through the following means: /asm/grc/JGR_ENSEMBLE_ScienceHub/Figure12.tar.gz. Format: Tar file with scripts and datasets needed to reproduce Figure 12. \n\nThis dataset is associated with the following publication:\nGilliam , R., C. Hogrefe , J. Godowitch, S. Napelenok , R. Mathur , and S.T. Rao. Impact of inherent meteorology uncertainty on air quality model predictions.   JOURNAL OF GEOPHYSICAL RESEARCH-ATMOSPHERES. American Geophysical Union, Washington, DC, USA, 120(23): 12,259\u201312,280, (2015).",
+            "distribution": [],
             "identifier": "A-6q5f-389",
             "keyword": [
                 "CMAQ ISAM",
@@ -39232,14 +39230,10 @@
                 "WRF-CMAQ",
                 "Ozone"
             ],
-            "contactPoint": {
-                "fn": "Robert Gilliam",
-                "hasEmail": "mailto:gilliam.robert@epa.gov"
-            },
-            "distribution": [],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2014-11-10",
-            "references": [
-                "https://doi.org/10.1002/2015jd023674"
+            "programCode": [
+                "020:094"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -39249,19 +39243,28 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1002/2015jd023674"
+            ],
+            "rights": null,
+            "title": "Figure12"
         },
         {
-            "title": "Predicted median July stream/river temperature regime in New England",
-            "description": "This shapefile includes the predicted thermal regime for all NHDPlus version 1 stream and river reaches in New England within the model domain based on the spatial statistical network model published in Detenbeck et al. 2016 (Detenbeck, N. E., Morrison, A., Abele, R. W. and Kopp, D. (2016), Spatial statistical network models for stream and river temperature in New England, USA. Water Resour. Res. Accepted Author Manuscript. doi:10.1002/2015WR018349). Portions of this dataset are inaccessible because: The dataset can be accessed for download via the EPA application Estuary Data Mapper, downloadable from www.epa.gov/edm. They can be accessed through the following means: The dataset can be accessed for download via the EPA application Estuary Data Mapper, downloadable from www.epa.gov/edm. Format: Shapefile with associated metadata. \n\nThis dataset is associated with the following publication:\nDetenbeck , N., A. Morrison, R. Abele , and D. Kopp. Spatial statistical network models for stream and river temperature in New England, USA.   WATER RESOURCES RESEARCH. American Geophysical Union, Washington, DC, USA, 52: 6018\u20136040, (2016).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:096"
+            "contactPoint": {
+                "fn": "Naomi Detenbeck",
+                "hasEmail": "mailto:detenbeck.naomi@epa.gov"
+            },
+            "description": "This shapefile includes the predicted thermal regime for all NHDPlus version 1 stream and river reaches in New England within the model domain based on the spatial statistical network model published in Detenbeck et al. 2016 (Detenbeck, N. E., Morrison, A., Abele, R. W. and Kopp, D. (2016), Spatial statistical network models for stream and river temperature in New England, USA. Water Resour. Res. Accepted Author Manuscript. doi:10.1002/2015WR018349). Portions of this dataset are inaccessible because: The dataset can be accessed for download via the EPA application Estuary Data Mapper, downloadable from www.epa.gov/edm. They can be accessed through the following means: The dataset can be accessed for download via the EPA application Estuary Data Mapper, downloadable from www.epa.gov/edm. Format: Shapefile with associated metadata. \n\nThis dataset is associated with the following publication:\nDetenbeck , N., A. Morrison, R. Abele , and D. Kopp. Spatial statistical network models for stream and river temperature in New England, USA.   WATER RESOURCES RESEARCH. American Geophysical Union, Washington, DC, USA, 52: 6018\u20136040, (2016).",
+            "distribution": [
+                {
+                    "accessURL": "https://www.epa.gov/hesc/estuary-data-mapper-edm",
+                    "title": "https://www.epa.gov/hesc/estuary-data-mapper-edm"
+                }
             ],
             "identifier": "A-j9kt-120",
             "keyword": [
@@ -39275,19 +39278,10 @@
                 "aquatic biota",
                 "habitat"
             ],
-            "contactPoint": {
-                "fn": "Naomi Detenbeck",
-                "hasEmail": "mailto:detenbeck.naomi@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "https://www.epa.gov/hesc/estuary-data-mapper-edm",
-                    "accessURL": "https://www.epa.gov/hesc/estuary-data-mapper-edm"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2016-07-17",
-            "references": [
-                "https://doi.org/10.1002/2015wr018349"
+            "programCode": [
+                "020:096"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -39297,20 +39291,24 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1002/2015wr018349"
+            ],
+            "rights": null,
+            "title": "Predicted median July stream/river temperature regime in New England"
         },
         {
-            "title": "New England observed and predicted median July stream/river temperature points",
-            "description": "The shapefile contains points with associated observed and predicted median July stream/river temperatures in New England based on a spatial statistical network model published in Detenbeck et al. (2016): Raw stream/temperature data were received from a variety of state agencies, watershed organizations, and Federal agencies (see Detenbeck et al. 2016 for complete list: Detenbeck, N. E., Morrison, A., Abele, R. W. and Kopp, D. (2016), Spatial statistical network models for stream and river temperature in New England, USA. Water Resour. Res. Accepted Author Manuscript. doi:10.1002/2015WR018349). This dataset is not publicly accessible because: The dataset is being made available as part of a collection of stream/river temperature model results through EPA's Estuary Data Mapper (publically available application at www.epa.gov/edm for discovering, viewing and accessing geospatial data). It can be accessed through the following means: The dataset is being made available as part of a collection of stream/river temperature model results through EPA's Estuary Data Mapper (publically available application at www.epa.gov/edm for discovering, viewing and accessing geospatial data). Format: Shapefile. \n\nThis dataset is associated with the following publication:\nDetenbeck , N., A. Morrison, R. Abele , and D. Kopp. Spatial statistical network models for stream and river temperature in New England, USA.   WATER RESOURCES RESEARCH. American Geophysical Union, Washington, DC, USA, 52: 6018\u20136040, (2016).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:096"
-            ],
+            "contactPoint": {
+                "fn": "Naomi Detenbeck",
+                "hasEmail": "mailto:detenbeck.naomi@epa.gov"
+            },
+            "description": "The shapefile contains points with associated observed and predicted median July stream/river temperatures in New England based on a spatial statistical network model published in Detenbeck et al. (2016): Raw stream/temperature data were received from a variety of state agencies, watershed organizations, and Federal agencies (see Detenbeck et al. 2016 for complete list: Detenbeck, N. E., Morrison, A., Abele, R. W. and Kopp, D. (2016), Spatial statistical network models for stream and river temperature in New England, USA. Water Resour. Res. Accepted Author Manuscript. doi:10.1002/2015WR018349). This dataset is not publicly accessible because: The dataset is being made available as part of a collection of stream/river temperature model results through EPA's Estuary Data Mapper (publically available application at www.epa.gov/edm for discovering, viewing and accessing geospatial data). It can be accessed through the following means: The dataset is being made available as part of a collection of stream/river temperature model results through EPA's Estuary Data Mapper (publically available application at www.epa.gov/edm for discovering, viewing and accessing geospatial data). Format: Shapefile. \n\nThis dataset is associated with the following publication:\nDetenbeck , N., A. Morrison, R. Abele , and D. Kopp. Spatial statistical network models for stream and river temperature in New England, USA.   WATER RESOURCES RESEARCH. American Geophysical Union, Washington, DC, USA, 52: 6018\u20136040, (2016).",
+            "distribution": [],
             "identifier": "A-j9kt-121",
             "keyword": [
                 "spatial statistical network model",
@@ -39324,14 +39322,10 @@
                 "aquatic biota",
                 "habitat"
             ],
-            "contactPoint": {
-                "fn": "Naomi Detenbeck",
-                "hasEmail": "mailto:detenbeck.naomi@epa.gov"
-            },
-            "distribution": [],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2015-09-10",
-            "references": [
-                "https://doi.org/10.1002/2015wr018349"
+            "programCode": [
+                "020:096"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -39341,19 +39335,28 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1002/2015wr018349"
+            ],
+            "rights": null,
+            "title": "New England observed and predicted median July stream/river temperature points"
         },
         {
-            "title": "New England observed and predicted median August stream/river temperature points",
-            "description": "The shapefile contains points with associated observed and predicted median August stream/river temperatures in New England based on a spatial statistical network model published in Detenbeck et al. (2016): Raw stream/temperature data were received from a variety of state agencies, watershed organizations, and Federal agencies (see Detenbeck et al. 2016 for complete list: Detenbeck, N. E., Morrison, A., Abele, R. W. and Kopp, D. (2016), Spatial statistical network models for stream and river temperature in New England, USA. Water Resour. Res. Accepted Author Manuscript. doi:10.1002/2015WR018349). Portions of this dataset are inaccessible because: The dataset is being made available as part of a collection of stream/river temperature model results through EPA's Estuary Data Mapper (publically available application at www.epa.gov/edm for discovering, viewing and accessing geospatial data). They can be accessed through the following means: The dataset is being made available as part of a collection of stream/river temperature model results through EPA's Estuary Data Mapper (publically available application at www.epa.gov/edm for discovering, viewing and accessing geospatial data). Format: Shapefile. \n\nThis dataset is associated with the following publication:\nDetenbeck , N., A. Morrison, R. Abele , and D. Kopp. Spatial statistical network models for stream and river temperature in New England, USA.   WATER RESOURCES RESEARCH. American Geophysical Union, Washington, DC, USA, 52: 6018\u20136040, (2016).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:096"
+            "contactPoint": {
+                "fn": "Naomi Detenbeck",
+                "hasEmail": "mailto:detenbeck.naomi@epa.gov"
+            },
+            "description": "The shapefile contains points with associated observed and predicted median August stream/river temperatures in New England based on a spatial statistical network model published in Detenbeck et al. (2016): Raw stream/temperature data were received from a variety of state agencies, watershed organizations, and Federal agencies (see Detenbeck et al. 2016 for complete list: Detenbeck, N. E., Morrison, A., Abele, R. W. and Kopp, D. (2016), Spatial statistical network models for stream and river temperature in New England, USA. Water Resour. Res. Accepted Author Manuscript. doi:10.1002/2015WR018349). Portions of this dataset are inaccessible because: The dataset is being made available as part of a collection of stream/river temperature model results through EPA's Estuary Data Mapper (publically available application at www.epa.gov/edm for discovering, viewing and accessing geospatial data). They can be accessed through the following means: The dataset is being made available as part of a collection of stream/river temperature model results through EPA's Estuary Data Mapper (publically available application at www.epa.gov/edm for discovering, viewing and accessing geospatial data). Format: Shapefile. \n\nThis dataset is associated with the following publication:\nDetenbeck , N., A. Morrison, R. Abele , and D. Kopp. Spatial statistical network models for stream and river temperature in New England, USA.   WATER RESOURCES RESEARCH. American Geophysical Union, Washington, DC, USA, 52: 6018\u20136040, (2016).",
+            "distribution": [
+                {
+                    "accessURL": "https://www.epa.gov/hesc/estuary-data-mapper-edm",
+                    "title": "https://www.epa.gov/hesc/estuary-data-mapper-edm"
+                }
             ],
             "identifier": "A-j9kt-122",
             "keyword": [
@@ -39367,19 +39370,10 @@
                 "aquatic biota",
                 "habitat"
             ],
-            "contactPoint": {
-                "fn": "Naomi Detenbeck",
-                "hasEmail": "mailto:detenbeck.naomi@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "https://www.epa.gov/hesc/estuary-data-mapper-edm",
-                    "accessURL": "https://www.epa.gov/hesc/estuary-data-mapper-edm"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2015-09-10",
-            "references": [
-                "https://doi.org/10.1002/2015wr018349"
+            "programCode": [
+                "020:096"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -39389,19 +39383,28 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1002/2015wr018349"
+            ],
+            "rights": null,
+            "title": "New England observed and predicted median August stream/river temperature points"
         },
         {
-            "title": "New England observed and predicted July stream/river temperature daily range points",
-            "description": "The shapefile contains points with associated observed and predicted July stream/river temperature daily ranges in New England based on a spatial statistical network model published in Detenbeck et al. (2016): Detenbeck, N. E., Morrison, A., Abele, R. W. and Kopp, D. (2016), Spatial statistical network models for stream and river temperature in New England, USA. Water Resour. Res. Accepted Author Manuscript. doi:10.1002/2015WR018349). Portions of this dataset are inaccessible because: The dataset is being made available as part of a collection of stream/river temperature model results through EPA's Estuary Data Mapper (publically available application at www.epa.gov/edm for discovering, viewing and accessing geospatial data). They can be accessed through the following means: The dataset is being made available as part of a collection of stream/river temperature model results through EPA's Estuary Data Mapper (publically available application at www.epa.gov/edm for discovering, viewing and accessing geospatial data). Format: Shapefile. \n\nThis dataset is associated with the following publication:\nDetenbeck , N., A. Morrison, R. Abele , and D. Kopp. Spatial statistical network models for stream and river temperature in New England, USA.   WATER RESOURCES RESEARCH. American Geophysical Union, Washington, DC, USA, 52: 6018\u20136040, (2016).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:096"
+            "contactPoint": {
+                "fn": "Naomi Detenbeck",
+                "hasEmail": "mailto:detenbeck.naomi@epa.gov"
+            },
+            "description": "The shapefile contains points with associated observed and predicted July stream/river temperature daily ranges in New England based on a spatial statistical network model published in Detenbeck et al. (2016): Detenbeck, N. E., Morrison, A., Abele, R. W. and Kopp, D. (2016), Spatial statistical network models for stream and river temperature in New England, USA. Water Resour. Res. Accepted Author Manuscript. doi:10.1002/2015WR018349). Portions of this dataset are inaccessible because: The dataset is being made available as part of a collection of stream/river temperature model results through EPA's Estuary Data Mapper (publically available application at www.epa.gov/edm for discovering, viewing and accessing geospatial data). They can be accessed through the following means: The dataset is being made available as part of a collection of stream/river temperature model results through EPA's Estuary Data Mapper (publically available application at www.epa.gov/edm for discovering, viewing and accessing geospatial data). Format: Shapefile. \n\nThis dataset is associated with the following publication:\nDetenbeck , N., A. Morrison, R. Abele , and D. Kopp. Spatial statistical network models for stream and river temperature in New England, USA.   WATER RESOURCES RESEARCH. American Geophysical Union, Washington, DC, USA, 52: 6018\u20136040, (2016).",
+            "distribution": [
+                {
+                    "accessURL": "https://www.epa.gov/hesc/estuary-data-mapper-edm",
+                    "title": "https://www.epa.gov/hesc/estuary-data-mapper-edm"
+                }
             ],
             "identifier": "A-j9kt-123",
             "keyword": [
@@ -39415,19 +39418,10 @@
                 "aquatic biota",
                 "habitat"
             ],
-            "contactPoint": {
-                "fn": "Naomi Detenbeck",
-                "hasEmail": "mailto:detenbeck.naomi@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "https://www.epa.gov/hesc/estuary-data-mapper-edm",
-                    "accessURL": "https://www.epa.gov/hesc/estuary-data-mapper-edm"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2015-09-10",
-            "references": [
-                "https://doi.org/10.1002/2015wr018349"
+            "programCode": [
+                "020:096"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -39437,19 +39431,28 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1002/2015wr018349"
+            ],
+            "rights": null,
+            "title": "New England observed and predicted July stream/river temperature daily range points"
         },
         {
-            "title": "New England observed and predicted August stream/river temperature daily range points",
-            "description": "The shapefile contains points with associated observed and predicted August stream/river temperature daily ranges in New England based on a spatial statistical network model published in Detenbeck et al. (2016): Detenbeck, N. E., Morrison, A., Abele, R. W. and Kopp, D. (2016), Spatial statistical network models for stream and river temperature in New England, USA. Water Resour. Res. Accepted Author Manuscript. doi:10.1002/2015WR018349). Portions of this dataset are inaccessible because: The dataset is being made available as part of a collection of stream/river temperature model results through EPA's Estuary Data Mapper (publically available application at www.epa.gov/edm for discovering, viewing and accessing geospatial data). They can be accessed through the following means: The dataset is being made available as part of a collection of stream/river temperature model results through EPA's Estuary Data Mapper (publically available application at www.epa.gov/edm for discovering, viewing and accessing geospatial data). Format: Shapefile. \n\nThis dataset is associated with the following publication:\nDetenbeck , N., A. Morrison, R. Abele , and D. Kopp. Spatial statistical network models for stream and river temperature in New England, USA.   WATER RESOURCES RESEARCH. American Geophysical Union, Washington, DC, USA, 52: 6018\u20136040, (2016).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:096"
+            "contactPoint": {
+                "fn": "Naomi Detenbeck",
+                "hasEmail": "mailto:detenbeck.naomi@epa.gov"
+            },
+            "description": "The shapefile contains points with associated observed and predicted August stream/river temperature daily ranges in New England based on a spatial statistical network model published in Detenbeck et al. (2016): Detenbeck, N. E., Morrison, A., Abele, R. W. and Kopp, D. (2016), Spatial statistical network models for stream and river temperature in New England, USA. Water Resour. Res. Accepted Author Manuscript. doi:10.1002/2015WR018349). Portions of this dataset are inaccessible because: The dataset is being made available as part of a collection of stream/river temperature model results through EPA's Estuary Data Mapper (publically available application at www.epa.gov/edm for discovering, viewing and accessing geospatial data). They can be accessed through the following means: The dataset is being made available as part of a collection of stream/river temperature model results through EPA's Estuary Data Mapper (publically available application at www.epa.gov/edm for discovering, viewing and accessing geospatial data). Format: Shapefile. \n\nThis dataset is associated with the following publication:\nDetenbeck , N., A. Morrison, R. Abele , and D. Kopp. Spatial statistical network models for stream and river temperature in New England, USA.   WATER RESOURCES RESEARCH. American Geophysical Union, Washington, DC, USA, 52: 6018\u20136040, (2016).",
+            "distribution": [
+                {
+                    "accessURL": "https://www.epa.gov/hesc/estuary-data-mapper-edm",
+                    "title": "https://www.epa.gov/hesc/estuary-data-mapper-edm"
+                }
             ],
             "identifier": "A-j9kt-124",
             "keyword": [
@@ -39463,19 +39466,10 @@
                 "aquatic biota",
                 "habitat"
             ],
-            "contactPoint": {
-                "fn": "Naomi Detenbeck",
-                "hasEmail": "mailto:detenbeck.naomi@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "https://www.epa.gov/hesc/estuary-data-mapper-edm",
-                    "accessURL": "https://www.epa.gov/hesc/estuary-data-mapper-edm"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2015-09-10",
-            "references": [
-                "https://doi.org/10.1002/2015wr018349"
+            "programCode": [
+                "020:096"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -39485,19 +39479,28 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1002/2015wr018349"
+            ],
+            "rights": null,
+            "title": "New England observed and predicted August stream/river temperature daily range points"
         },
         {
-            "title": "New England observed and predicted growing season maximum stream/river temperature points",
-            "description": "The shapefile contains points with associated observed and predicted growing season maximum stream/river temperatures in New England based on a spatial statistical network model published in Detenbeck et al. (2016): Detenbeck, N. E., Morrison, A., Abele, R. W. and Kopp, D. (2016), Spatial statistical network models for stream and river temperature in New England, USA. Water Resour. Res. Accepted Author Manuscript. doi:10.1002/2015WR018349). Portions of this dataset are inaccessible because: The dataset is being made available as part of a collection of stream/river temperature model results through EPA's Estuary Data Mapper (publically available application at www.epa.gov/edm for discovering, viewing and accessing geospatial data). They can be accessed through the following means: The dataset is being made available as part of a collection of stream/river temperature model results through EPA's Estuary Data Mapper (publically available application at www.epa.gov/edm for discovering, viewing and accessing geospatial data). Format: Shapefile. \n\nThis dataset is associated with the following publication:\nDetenbeck , N., A. Morrison, R. Abele , and D. Kopp. Spatial statistical network models for stream and river temperature in New England, USA.   WATER RESOURCES RESEARCH. American Geophysical Union, Washington, DC, USA, 52: 6018\u20136040, (2016).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:096"
+            "contactPoint": {
+                "fn": "Naomi Detenbeck",
+                "hasEmail": "mailto:detenbeck.naomi@epa.gov"
+            },
+            "description": "The shapefile contains points with associated observed and predicted growing season maximum stream/river temperatures in New England based on a spatial statistical network model published in Detenbeck et al. (2016): Detenbeck, N. E., Morrison, A., Abele, R. W. and Kopp, D. (2016), Spatial statistical network models for stream and river temperature in New England, USA. Water Resour. Res. Accepted Author Manuscript. doi:10.1002/2015WR018349). Portions of this dataset are inaccessible because: The dataset is being made available as part of a collection of stream/river temperature model results through EPA's Estuary Data Mapper (publically available application at www.epa.gov/edm for discovering, viewing and accessing geospatial data). They can be accessed through the following means: The dataset is being made available as part of a collection of stream/river temperature model results through EPA's Estuary Data Mapper (publically available application at www.epa.gov/edm for discovering, viewing and accessing geospatial data). Format: Shapefile. \n\nThis dataset is associated with the following publication:\nDetenbeck , N., A. Morrison, R. Abele , and D. Kopp. Spatial statistical network models for stream and river temperature in New England, USA.   WATER RESOURCES RESEARCH. American Geophysical Union, Washington, DC, USA, 52: 6018\u20136040, (2016).",
+            "distribution": [
+                {
+                    "accessURL": "https://www.epa.gov/hesc/estuary-data-mapper-edm",
+                    "title": "https://www.epa.gov/hesc/estuary-data-mapper-edm"
+                }
             ],
             "identifier": "A-j9kt-125",
             "keyword": [
@@ -39510,19 +39513,10 @@
                 "aquatic biota",
                 "habitat"
             ],
-            "contactPoint": {
-                "fn": "Naomi Detenbeck",
-                "hasEmail": "mailto:detenbeck.naomi@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "https://www.epa.gov/hesc/estuary-data-mapper-edm",
-                    "accessURL": "https://www.epa.gov/hesc/estuary-data-mapper-edm"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2015-09-10",
-            "references": [
-                "https://doi.org/10.1002/2015wr018349"
+            "programCode": [
+                "020:096"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -39532,19 +39526,28 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1002/2015wr018349"
+            ],
+            "rights": null,
+            "title": "New England observed and predicted growing season maximum stream/river temperature points"
         },
         {
-            "title": "New England observed and predicted Julian day of maximum growing season stream/river temperature points",
-            "description": "The shapefile contains points with associated observed and predicted Julian day of maximum growing season stream/river temperatures in New England based on a spatial statistical network model published in Detenbeck et al. (2016): Detenbeck, N. E., Morrison, A., Abele, R. W. and Kopp, D. (2016), Spatial statistical network models for stream and river temperature in New England, USA. Water Resour. Res. Accepted Author Manuscript. doi:10.1002/2015WR018349). Portions of this dataset are inaccessible because: The dataset is being made available as part of a collection of stream/river temperature model results through EPA's Estuary Data Mapper (publically available application at www.epa.gov/edm for discovering, viewing and accessing geospatial data). They can be accessed through the following means: The dataset is being made available as part of a collection of stream/river temperature model results through EPA's Estuary Data Mapper (publically available application at www.epa.gov/edm for discovering, viewing and accessing geospatial data). Format: Shapefile. \n\nThis dataset is associated with the following publication:\nDetenbeck , N., A. Morrison, R. Abele , and D. Kopp. Spatial statistical network models for stream and river temperature in New England, USA.   WATER RESOURCES RESEARCH. American Geophysical Union, Washington, DC, USA, 52: 6018\u20136040, (2016).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:096"
+            "contactPoint": {
+                "fn": "Naomi Detenbeck",
+                "hasEmail": "mailto:detenbeck.naomi@epa.gov"
+            },
+            "description": "The shapefile contains points with associated observed and predicted Julian day of maximum growing season stream/river temperatures in New England based on a spatial statistical network model published in Detenbeck et al. (2016): Detenbeck, N. E., Morrison, A., Abele, R. W. and Kopp, D. (2016), Spatial statistical network models for stream and river temperature in New England, USA. Water Resour. Res. Accepted Author Manuscript. doi:10.1002/2015WR018349). Portions of this dataset are inaccessible because: The dataset is being made available as part of a collection of stream/river temperature model results through EPA's Estuary Data Mapper (publically available application at www.epa.gov/edm for discovering, viewing and accessing geospatial data). They can be accessed through the following means: The dataset is being made available as part of a collection of stream/river temperature model results through EPA's Estuary Data Mapper (publically available application at www.epa.gov/edm for discovering, viewing and accessing geospatial data). Format: Shapefile. \n\nThis dataset is associated with the following publication:\nDetenbeck , N., A. Morrison, R. Abele , and D. Kopp. Spatial statistical network models for stream and river temperature in New England, USA.   WATER RESOURCES RESEARCH. American Geophysical Union, Washington, DC, USA, 52: 6018\u20136040, (2016).",
+            "distribution": [
+                {
+                    "accessURL": "https://www.epa.gov/hesc/estuary-data-mapper-edm",
+                    "title": "https://www.epa.gov/hesc/estuary-data-mapper-edm"
+                }
             ],
             "identifier": "A-j9kt-126",
             "keyword": [
@@ -39558,19 +39561,10 @@
                 "aquatic biota",
                 "habitat"
             ],
-            "contactPoint": {
-                "fn": "Naomi Detenbeck",
-                "hasEmail": "mailto:detenbeck.naomi@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "https://www.epa.gov/hesc/estuary-data-mapper-edm",
-                    "accessURL": "https://www.epa.gov/hesc/estuary-data-mapper-edm"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2015-09-10",
-            "references": [
-                "https://doi.org/10.1002/2015wr018349"
+            "programCode": [
+                "020:096"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -39580,19 +39574,28 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1002/2015wr018349"
+            ],
+            "rights": null,
+            "title": "New England observed and predicted Julian day of maximum growing season stream/river temperature points"
         },
         {
-            "title": "New England observed and predicted July stream/river temperature maximum positive daily rate of change points",
-            "description": "The shapefile contains points with associated observed and predicted July stream/river temperature maximum positive daily rate of change in New England based on a spatial statistical network model published in Detenbeck et al. (2016): Detenbeck, N. E., Morrison, A., Abele, R. W. and Kopp, D. (2016), Spatial statistical network models for stream and river temperature in New England, USA. Water Resour. Res. Accepted Author Manuscript. doi:10.1002/2015WR018349). Portions of this dataset are inaccessible because: The dataset is being made available as part of a collection of stream/river temperature model results through EPA's Estuary Data Mapper (publically available application at www.epa.gov/edm for discovering, viewing and accessing geospatial data). They can be accessed through the following means: The dataset is being made available as part of a collection of stream/river temperature model results through EPA's Estuary Data Mapper (publically available application at www.epa.gov/edm for discovering, viewing and accessing geospatial data). Format: Shapefile. \n\nThis dataset is associated with the following publication:\nDetenbeck , N., A. Morrison, R. Abele , and D. Kopp. Spatial statistical network models for stream and river temperature in New England, USA.   WATER RESOURCES RESEARCH. American Geophysical Union, Washington, DC, USA, 52: 6018\u20136040, (2016).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:096"
+            "contactPoint": {
+                "fn": "Naomi Detenbeck",
+                "hasEmail": "mailto:detenbeck.naomi@epa.gov"
+            },
+            "description": "The shapefile contains points with associated observed and predicted July stream/river temperature maximum positive daily rate of change in New England based on a spatial statistical network model published in Detenbeck et al. (2016): Detenbeck, N. E., Morrison, A., Abele, R. W. and Kopp, D. (2016), Spatial statistical network models for stream and river temperature in New England, USA. Water Resour. Res. Accepted Author Manuscript. doi:10.1002/2015WR018349). Portions of this dataset are inaccessible because: The dataset is being made available as part of a collection of stream/river temperature model results through EPA's Estuary Data Mapper (publically available application at www.epa.gov/edm for discovering, viewing and accessing geospatial data). They can be accessed through the following means: The dataset is being made available as part of a collection of stream/river temperature model results through EPA's Estuary Data Mapper (publically available application at www.epa.gov/edm for discovering, viewing and accessing geospatial data). Format: Shapefile. \n\nThis dataset is associated with the following publication:\nDetenbeck , N., A. Morrison, R. Abele , and D. Kopp. Spatial statistical network models for stream and river temperature in New England, USA.   WATER RESOURCES RESEARCH. American Geophysical Union, Washington, DC, USA, 52: 6018\u20136040, (2016).",
+            "distribution": [
+                {
+                    "accessURL": "https://www.epa.gov/hesc/estuary-data-mapper-edm",
+                    "title": "https://www.epa.gov/hesc/estuary-data-mapper-edm"
+                }
             ],
             "identifier": "A-j9kt-127",
             "keyword": [
@@ -39606,19 +39609,10 @@
                 "aquatic biota",
                 "habitat"
             ],
-            "contactPoint": {
-                "fn": "Naomi Detenbeck",
-                "hasEmail": "mailto:detenbeck.naomi@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "https://www.epa.gov/hesc/estuary-data-mapper-edm",
-                    "accessURL": "https://www.epa.gov/hesc/estuary-data-mapper-edm"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2015-09-10",
-            "references": [
-                "https://doi.org/10.1002/2015wr018349"
+            "programCode": [
+                "020:096"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -39628,19 +39622,28 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1002/2015wr018349"
+            ],
+            "rights": null,
+            "title": "New England observed and predicted July stream/river temperature maximum positive daily rate of change points"
         },
         {
-            "title": "New England observed and predicted August stream/river temperature maximum positive daily rate of change points",
-            "description": "The shapefile contains points with associated observed and predicted August stream/river temperature maximum positive daily rate of change in New England based on a spatial statistical network model published in Detenbeck et al. (2016): Detenbeck, N. E., Morrison, A., Abele, R. W. and Kopp, D. (2016), Spatial statistical network models for stream and river temperature in New England, USA. Water Resour. Res. Accepted Author Manuscript. doi:10.1002/2015WR018349). Portions of this dataset are inaccessible because: The dataset is being made available as part of a collection of stream/river temperature model results through EPA's Estuary Data Mapper (publically available application at www.epa.gov/edm for discovering, viewing and accessing geospatial data). They can be accessed through the following means: The dataset is being made available as part of a collection of stream/river temperature model results through EPA's Estuary Data Mapper (publically available application at www.epa.gov/edm for discovering, viewing and accessing geospatial data). Format: Shapefile. \n\nThis dataset is associated with the following publication:\nDetenbeck , N., A. Morrison, R. Abele , and D. Kopp. Spatial statistical network models for stream and river temperature in New England, USA.   WATER RESOURCES RESEARCH. American Geophysical Union, Washington, DC, USA, 52: 6018\u20136040, (2016).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:096"
+            "contactPoint": {
+                "fn": "Naomi Detenbeck",
+                "hasEmail": "mailto:detenbeck.naomi@epa.gov"
+            },
+            "description": "The shapefile contains points with associated observed and predicted August stream/river temperature maximum positive daily rate of change in New England based on a spatial statistical network model published in Detenbeck et al. (2016): Detenbeck, N. E., Morrison, A., Abele, R. W. and Kopp, D. (2016), Spatial statistical network models for stream and river temperature in New England, USA. Water Resour. Res. Accepted Author Manuscript. doi:10.1002/2015WR018349). Portions of this dataset are inaccessible because: The dataset is being made available as part of a collection of stream/river temperature model results through EPA's Estuary Data Mapper (publically available application at www.epa.gov/edm for discovering, viewing and accessing geospatial data). They can be accessed through the following means: The dataset is being made available as part of a collection of stream/river temperature model results through EPA's Estuary Data Mapper (publically available application at www.epa.gov/edm for discovering, viewing and accessing geospatial data). Format: Shapefile. \n\nThis dataset is associated with the following publication:\nDetenbeck , N., A. Morrison, R. Abele , and D. Kopp. Spatial statistical network models for stream and river temperature in New England, USA.   WATER RESOURCES RESEARCH. American Geophysical Union, Washington, DC, USA, 52: 6018\u20136040, (2016).",
+            "distribution": [
+                {
+                    "accessURL": "https://www.epa.gov/hesc/estuary-data-mapper-edm",
+                    "title": "https://www.epa.gov/hesc/estuary-data-mapper-edm"
+                }
             ],
             "identifier": "A-j9kt-128",
             "keyword": [
@@ -39654,19 +39657,10 @@
                 "aquatic biota",
                 "habitat"
             ],
-            "contactPoint": {
-                "fn": "Naomi Detenbeck",
-                "hasEmail": "mailto:detenbeck.naomi@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "https://www.epa.gov/hesc/estuary-data-mapper-edm",
-                    "accessURL": "https://www.epa.gov/hesc/estuary-data-mapper-edm"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2015-09-10",
-            "references": [
-                "https://doi.org/10.1002/2015wr018349"
+            "programCode": [
+                "020:096"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -39676,19 +39670,28 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1002/2015wr018349"
+            ],
+            "rights": null,
+            "title": "New England observed and predicted August stream/river temperature maximum positive daily rate of change points"
         },
         {
-            "title": "New England observed and predicted July maximum negative stream/river temperature daily rate of change points",
-            "description": "The shapefile contains points with associated observed and predicted July stream/river temperature maximum negative daily rate of change in New England based on a spatial statistical network model published in Detenbeck et al. (2016): Detenbeck, N. E., Morrison, A., Abele, R. W. and Kopp, D. (2016), Spatial statistical network models for stream and river temperature in New England, USA. Water Resour. Res. Accepted Author Manuscript. doi:10.1002/2015WR018349). Portions of this dataset are inaccessible because: The dataset is being made available as part of a collection of stream/river temperature model results through EPA's Estuary Data Mapper (publically available application at www.epa.gov/edm for discovering, viewing and accessing geospatial data). They can be accessed through the following means: The dataset is being made available as part of a collection of stream/river temperature model results through EPA's Estuary Data Mapper (publically available application at www.epa.gov/edm for discovering, viewing and accessing geospatial data). Format: Shapefile. \n\nThis dataset is associated with the following publication:\nDetenbeck , N., A. Morrison, R. Abele , and D. Kopp. Spatial statistical network models for stream and river temperature in New England, USA.   WATER RESOURCES RESEARCH. American Geophysical Union, Washington, DC, USA, 52: 6018\u20136040, (2016).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:096"
+            "contactPoint": {
+                "fn": "Naomi Detenbeck",
+                "hasEmail": "mailto:detenbeck.naomi@epa.gov"
+            },
+            "description": "The shapefile contains points with associated observed and predicted July stream/river temperature maximum negative daily rate of change in New England based on a spatial statistical network model published in Detenbeck et al. (2016): Detenbeck, N. E., Morrison, A., Abele, R. W. and Kopp, D. (2016), Spatial statistical network models for stream and river temperature in New England, USA. Water Resour. Res. Accepted Author Manuscript. doi:10.1002/2015WR018349). Portions of this dataset are inaccessible because: The dataset is being made available as part of a collection of stream/river temperature model results through EPA's Estuary Data Mapper (publically available application at www.epa.gov/edm for discovering, viewing and accessing geospatial data). They can be accessed through the following means: The dataset is being made available as part of a collection of stream/river temperature model results through EPA's Estuary Data Mapper (publically available application at www.epa.gov/edm for discovering, viewing and accessing geospatial data). Format: Shapefile. \n\nThis dataset is associated with the following publication:\nDetenbeck , N., A. Morrison, R. Abele , and D. Kopp. Spatial statistical network models for stream and river temperature in New England, USA.   WATER RESOURCES RESEARCH. American Geophysical Union, Washington, DC, USA, 52: 6018\u20136040, (2016).",
+            "distribution": [
+                {
+                    "accessURL": "https://www.epa.gov/hesc/estuary-data-mapper-edm",
+                    "title": "https://www.epa.gov/hesc/estuary-data-mapper-edm"
+                }
             ],
             "identifier": "A-j9kt-129",
             "keyword": [
@@ -39702,19 +39705,10 @@
                 "aquatic biota",
                 "habitat"
             ],
-            "contactPoint": {
-                "fn": "Naomi Detenbeck",
-                "hasEmail": "mailto:detenbeck.naomi@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "https://www.epa.gov/hesc/estuary-data-mapper-edm",
-                    "accessURL": "https://www.epa.gov/hesc/estuary-data-mapper-edm"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2015-09-10",
-            "references": [
-                "https://doi.org/10.1002/2015wr018349"
+            "programCode": [
+                "020:096"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -39724,19 +39718,28 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1002/2015wr018349"
+            ],
+            "rights": null,
+            "title": "New England observed and predicted July maximum negative stream/river temperature daily rate of change points"
         },
         {
-            "title": "New England observed and predicted August stream/river temperature maximum daily rate of change points",
-            "description": "The shapefile contains points with associated observed and predicted August stream/river temperature maximum negative rate of change in New England based on a spatial statistical network model published in Detenbeck et al. (2016): Detenbeck, N. E., Morrison, A., Abele, R. W. and Kopp, D. (2016), Spatial statistical network models for stream and river temperature in New England, USA. Water Resour. Res. Accepted Author Manuscript. doi:10.1002/2015WR018349). Portions of this dataset are inaccessible because: The dataset is being made available as part of a collection of stream/river temperature model results through EPA's Estuary Data Mapper (publically available application at www.epa.gov/edm for discovering, viewing and accessing geospatial data). They can be accessed through the following means: The dataset is being made available as part of a collection of stream/river temperature model results through EPA's Estuary Data Mapper (publically available application at www.epa.gov/edm for discovering, viewing and accessing geospatial data). Format: Shapefile. \n\nThis dataset is associated with the following publication:\nDetenbeck , N., A. Morrison, R. Abele , and D. Kopp. Spatial statistical network models for stream and river temperature in New England, USA.   WATER RESOURCES RESEARCH. American Geophysical Union, Washington, DC, USA, 52: 6018\u20136040, (2016).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:096"
+            "contactPoint": {
+                "fn": "Naomi Detenbeck",
+                "hasEmail": "mailto:detenbeck.naomi@epa.gov"
+            },
+            "description": "The shapefile contains points with associated observed and predicted August stream/river temperature maximum negative rate of change in New England based on a spatial statistical network model published in Detenbeck et al. (2016): Detenbeck, N. E., Morrison, A., Abele, R. W. and Kopp, D. (2016), Spatial statistical network models for stream and river temperature in New England, USA. Water Resour. Res. Accepted Author Manuscript. doi:10.1002/2015WR018349). Portions of this dataset are inaccessible because: The dataset is being made available as part of a collection of stream/river temperature model results through EPA's Estuary Data Mapper (publically available application at www.epa.gov/edm for discovering, viewing and accessing geospatial data). They can be accessed through the following means: The dataset is being made available as part of a collection of stream/river temperature model results through EPA's Estuary Data Mapper (publically available application at www.epa.gov/edm for discovering, viewing and accessing geospatial data). Format: Shapefile. \n\nThis dataset is associated with the following publication:\nDetenbeck , N., A. Morrison, R. Abele , and D. Kopp. Spatial statistical network models for stream and river temperature in New England, USA.   WATER RESOURCES RESEARCH. American Geophysical Union, Washington, DC, USA, 52: 6018\u20136040, (2016).",
+            "distribution": [
+                {
+                    "accessURL": "https://www.epa.gov/hesc/estuary-data-mapper-edm",
+                    "title": "https://www.epa.gov/hesc/estuary-data-mapper-edm"
+                }
             ],
             "identifier": "A-j9kt-130",
             "keyword": [
@@ -39750,19 +39753,10 @@
                 "aquatic biota",
                 "habitat"
             ],
-            "contactPoint": {
-                "fn": "Naomi Detenbeck",
-                "hasEmail": "mailto:detenbeck.naomi@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "https://www.epa.gov/hesc/estuary-data-mapper-edm",
-                    "accessURL": "https://www.epa.gov/hesc/estuary-data-mapper-edm"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2015-09-10",
-            "references": [
-                "https://doi.org/10.1002/2015wr018349"
+            "programCode": [
+                "020:096"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -39772,69 +39766,71 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1002/2015wr018349"
+            ],
+            "rights": null,
+            "title": "New England observed and predicted August stream/river temperature maximum daily rate of change points"
         },
         {
-            "title": "Gene expression and chemical exposure data for larval Pimephales promelas exposed to one of  four pyrethroid pesticides.",
-            "description": "Uploaded datasets are detailed exposure information (chemical concentrations and water quality parameters) for exposures conducted in a flow through diluter system with larval Pimephales promelas to four different pyrethroid pesticides.  The GEO submission URL links to the NCBI GEO database and contains gene expression data from whole larvae exposed to different concentrations of the pyrethroids across multiple experiments. \n\nThis dataset is associated with the following publication:\nBiales, A., M. Kostich, A. Batt, M. See, R. Flick, D. Gordon, J. Lazorchak, and D. Bencic. Initial Development of a Multigene Omics-Based Exposure Biomarker for Pyrethroid Pesticides.   CRITICAL REVIEWS IN ENVIRONMENTAL SCIENCE AND TECHNOLOGY. CRC Press LLC, Boca Raton, FL, USA, 179(0): 27-35, (2016).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "A-mcvw-158",
-            "keyword": [
-                "transcriptomics",
-                "biomarker",
-                "fish",
-                "pyrethroids"
-            ],
             "contactPoint": {
                 "fn": "Adam Biales",
                 "hasEmail": "mailto:biales.adam@epa.gov"
             },
+            "description": "Uploaded datasets are detailed exposure information (chemical concentrations and water quality parameters) for exposures conducted in a flow through diluter system with larval Pimephales promelas to four different pyrethroid pesticides.  The GEO submission URL links to the NCBI GEO database and contains gene expression data from whole larvae exposed to different concentrations of the pyrethroids across multiple experiments. \n\nThis dataset is associated with the following publication:\nBiales, A., M. Kostich, A. Batt, M. See, R. Flick, D. Gordon, J. Lazorchak, and D. Bencic. Initial Development of a Multigene Omics-Based Exposure Biomarker for Pyrethroid Pesticides.   CRITICAL REVIEWS IN ENVIRONMENTAL SCIENCE AND TECHNOLOGY. CRC Press LLC, Boca Raton, FL, USA, 179(0): 27-35, (2016).",
             "distribution": [
                 {
-                    "title": "Table 1 - Water Quality Parameters.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/158/Table%201%20-%20Water%20Quality%20Parameters.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Table 1 - Water Quality Parameters.xlsx"
                 },
                 {
-                    "title": "Table 2 - Phase 1 per tank per day chemistry.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/158/Table%202%20-%20Phase%201%20per%20tank%20per%20day%20chemistry.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Table 2 - Phase 1 per tank per day chemistry.xlsx"
                 },
                 {
-                    "title": "Table 3 - P2 Chemistry Results Per Day and Per Tank.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/158/Table%203%20-%20P2%20Chemistry%20Results%20Per%20Day%20and%20Per%20Tank.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Table 3 - P2 Chemistry Results Per Day and Per Tank.xlsx"
                 },
                 {
-                    "title": "Table 4  - Functional Annotation Clustering_DAVID.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/158/Table%204%20%20-%20Functional%20Annotation%20Clustering_DAVID.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Table 4  - Functional Annotation Clustering_DAVID.xlsx"
                 },
                 {
-                    "title": "Table 5 - Uncalibrated eAUCs.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/158/Table%205%20-%20Uncalibrated%20eAUCs.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Table 5 - Uncalibrated eAUCs.xlsx"
                 },
                 {
-                    "title": "Table 6 CALIBRATED EAUCS.docx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/158/Table%206%20CALIBRATED%20EAUCS.docx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+                    "title": "Table 6 CALIBRATED EAUCS.docx"
                 },
                 {
-                    "title": "https://www.ncbi.nlm.nih.gov/gquery/?term=GSE84475",
-                    "accessURL": "https://www.ncbi.nlm.nih.gov/gquery/?term=GSE84475"
+                    "accessURL": "https://www.ncbi.nlm.nih.gov/gquery/?term=GSE84475",
+                    "title": "https://www.ncbi.nlm.nih.gov/gquery/?term=GSE84475"
                 }
             ],
+            "identifier": "A-mcvw-158",
+            "keyword": [
+                "transcriptomics",
+                "biomarker",
+                "fish",
+                "pyrethroids"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2016-07-13",
-            "references": null,
+            "programCode": [
+                "020:000"
+            ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
                 "subOrganizationOf": {
@@ -39843,19 +39839,27 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": null,
+            "rights": null,
+            "title": "Gene expression and chemical exposure data for larval Pimephales promelas exposed to one of  four pyrethroid pesticides."
         },
         {
-            "title": "Supplemental Information: Phototransformation-Induced Aggregation of Functionalized Single-Walled Carbon Nanotubes: the Importance of Amorphous Carbon",
-            "description": "Additional information about the carboxylated SWCNT calibration curve, AFM images, EDS results, solar simulator light and UVB lamp spectra, TEM image of\nparent carboxylated SWCNTs, XPS spectra of the dark control P3 sample and the irradiated P3 sample, and a table summarizing the kinetic parameters (PDF). \n\nThis dataset is associated with the following publication:\nHou, W., C. He, Y. Wang, D. Wang, and R. Zepp. Phototransformation-Induced Aggregation of Functionalized Single-Walled Carbon Nanotubes: The Importance of Amorphous Carbon.   ENVIRONMENTAL SCIENCE & TECHNOLOGY. American Chemical Society, Washington, DC, USA, 50(7): 3494\u20133502, (2016).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:095"
+            "contactPoint": {
+                "fn": "Richard Zepp",
+                "hasEmail": "mailto:zepp.richard@epa.gov"
+            },
+            "description": "Additional information about the carboxylated SWCNT calibration curve, AFM images, EDS results, solar simulator light and UVB lamp spectra, TEM image of\nparent carboxylated SWCNTs, XPS spectra of the dark control P3 sample and the irradiated P3 sample, and a table summarizing the kinetic parameters (PDF). \n\nThis dataset is associated with the following publication:\nHou, W., C. He, Y. Wang, D. Wang, and R. Zepp. Phototransformation-Induced Aggregation of Functionalized Single-Walled Carbon Nanotubes: The Importance of Amorphous Carbon.   ENVIRONMENTAL SCIENCE & TECHNOLOGY. American Chemical Society, Washington, DC, USA, 50(7): 3494\u20133502, (2016).",
+            "distribution": [
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/330/es5b04727_si_001.pd.pdf",
+                    "mediaType": "application/pdf",
+                    "title": "es5b04727_si_001.pd.pdf"
+                }
             ],
             "identifier": "A-sqvz-330",
             "keyword": [
@@ -39871,20 +39875,10 @@
                 "phototransformations",
                 "amorphous carbon"
             ],
-            "contactPoint": {
-                "fn": "Richard Zepp",
-                "hasEmail": "mailto:zepp.richard@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "es5b04727_si_001.pd.pdf",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/330/es5b04727_si_001.pd.pdf",
-                    "mediaType": "application/pdf"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2016-02-24",
-            "references": [
-                "https://doi.org/10.1021/acs.est.5b04727"
+            "programCode": [
+                "020:095"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -39894,19 +39888,29 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1021/acs.est.5b04727"
+            ],
+            "rights": null,
+            "title": "Supplemental Information: Phototransformation-Induced Aggregation of Functionalized Single-Walled Carbon Nanotubes: the Importance of Amorphous Carbon"
         },
         {
-            "title": "Database to support \"Quanitfying groundwater dependency of riparian surface hydrologic features using the exit gradient\" by Faulkner et al. 2016.",
-            "description": "Collections of publically available secondary data used to develop the conclusions described in the journal article. \n\nThis dataset is associated with the following publication:\nFaulkner , B., S. Leibowitz , T. Canfield , and J. Groves. Quantifying groundwater dependency of riparian surface hydrologic features using the exit gradient.   Hydrological Processes. John Wiley & Sons, Ltd., Indianapolis, IN, USA,  1-11, (2015).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
+            "contactPoint": {
+                "fn": "Azadeh Azadpour-Keeley",
+                "hasEmail": "mailto:keeley.ann@epa.gov"
+            },
+            "description": "Collections of publically available secondary data used to develop the conclusions described in the journal article. \n\nThis dataset is associated with the following publication:\nFaulkner , B., S. Leibowitz , T. Canfield , and J. Groves. Quantifying groundwater dependency of riparian surface hydrologic features using the exit gradient.   Hydrological Processes. John Wiley & Sons, Ltd., Indianapolis, IN, USA,  1-11, (2015).",
+            "distribution": [
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/384/cala_owrd_science_hub.zip",
+                    "mediaType": "application/x-zip-compressed",
+                    "title": "cala_owrd_science_hub.zip"
+                }
             ],
             "identifier": "A-d25g-384",
             "keyword": [
@@ -39917,20 +39921,10 @@
                 "groundwater dependency of ecosystem services",
                 "exit gradient; basin fill aquifer; shallow groundwater management; wetland management; groundwater dependency"
             ],
-            "contactPoint": {
-                "fn": "Azadeh Azadpour-Keeley",
-                "hasEmail": "mailto:keeley.ann@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "cala_owrd_science_hub.zip",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/384/cala_owrd_science_hub.zip",
-                    "mediaType": "application/x-zip-compressed"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2016-09-26",
-            "references": [
-                "https://doi.org/10.1002/hyp.10766"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -39940,33 +39934,35 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1002/hyp.10766"
+            ],
+            "rights": null,
+            "title": "Database to support \"Quanitfying groundwater dependency of riparian surface hydrologic features using the exit gradient\" by Faulkner et al. 2016."
         },
         {
-            "title": "Towards Universal Screening for Toxoplasmosis: Rapid, Cost-effective and Simultaneous Detection of Toxoplasma Anti-IgG, IgM and IgA Antibodies Using Very Small Serum Volumes",
-            "description": "No dataset associated with this publication. This dataset is not publicly accessible because: This is a commentary and no data was generated. It can be accessed through the following means: There is no data associated with this commentary. Format: This is a commentary and no data was generated. \n\nThis dataset is associated with the following publication:\nAugustine, S. Towards Universal Screening for Toxoplasmosis: Rapid, Cost-effective and Simultaneous Detection of Toxoplasma Anti-IgG, IgM and IgA Antibodies Using Very Small Serum Volumes.   JOURNAL OF CLINICAL MICROBIOLOGY. American Society for Microbiology, Washington, DC, USA, 56(7): 1-2, (2016).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:096"
-            ],
+            "contactPoint": {
+                "fn": "Swinburne Augustine",
+                "hasEmail": "mailto:augustine.swinburne@epa.gov"
+            },
+            "description": "No dataset associated with this publication. This dataset is not publicly accessible because: This is a commentary and no data was generated. It can be accessed through the following means: There is no data associated with this commentary. Format: This is a commentary and no data was generated. \n\nThis dataset is associated with the following publication:\nAugustine, S. Towards Universal Screening for Toxoplasmosis: Rapid, Cost-effective and Simultaneous Detection of Toxoplasma Anti-IgG, IgM and IgA Antibodies Using Very Small Serum Volumes.   JOURNAL OF CLINICAL MICROBIOLOGY. American Society for Microbiology, Washington, DC, USA, 56(7): 1-2, (2016).",
+            "distribution": [],
             "identifier": "A-bzkt-293",
             "keyword": [
                 "Toxoplasma gondii",
                 "universal screening",
                 "commentary"
             ],
-            "contactPoint": {
-                "fn": "Swinburne Augustine",
-                "hasEmail": "mailto:augustine.swinburne@epa.gov"
-            },
-            "distribution": [],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2016-09-09",
-            "references": null,
+            "programCode": [
+                "020:096"
+            ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
                 "subOrganizationOf": {
@@ -39975,39 +39971,37 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": null,
+            "rights": null,
+            "title": "Towards Universal Screening for Toxoplasmosis: Rapid, Cost-effective and Simultaneous Detection of Toxoplasma Anti-IgG, IgM and IgA Antibodies Using Very Small Serum Volumes"
         },
         {
-            "title": " Effects of Cr(III) and CR(VI) on nitrification inhibition as determined by SOUR, function-specific gene expression and 16S rRNA sequence analysis of wastewater nitrifying enrichments",
-            "description": "Data generated to test nitrification inhibition of chromium. \n\nThis dataset is associated with the following publication:\nKapoor, V., M. Elk, X. Li, C. Impellitteri , and J. Santodomingo. Effects of Cr(III) and CR(VI) on nitrification inhibition as determined by SOUR, function-specific gene expression and 16S rRNA sequence analysis of wastewater nitrifying enrichments.   CHEMOSPHERE. Elsevier Science Ltd, New York, NY, USA, 147: 361-367, (2016).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "A-bk3v-396",
-            "keyword": [
-                "nitrification",
-                "RNA"
-            ],
             "contactPoint": {
                 "fn": "Jorge Santo Domingo",
                 "hasEmail": "mailto:santodomingo.jorge@epa.gov"
             },
+            "description": "Data generated to test nitrification inhibition of chromium. \n\nThis dataset is associated with the following publication:\nKapoor, V., M. Elk, X. Li, C. Impellitteri , and J. Santodomingo. Effects of Cr(III) and CR(VI) on nitrification inhibition as determined by SOUR, function-specific gene expression and 16S rRNA sequence analysis of wastewater nitrifying enrichments.   CHEMOSPHERE. Elsevier Science Ltd, New York, NY, USA, 147: 361-367, (2016).",
             "distribution": [
                 {
-                    "title": "cDNA CN-_061715.xls",
                     "downloadURL": "https://pasteur.epa.gov/uploads/396/cDNA%20CN-_061715.xls",
-                    "mediaType": "application/vnd.ms-excel"
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "cDNA CN-_061715.xls"
                 }
             ],
+            "identifier": "A-bk3v-396",
+            "keyword": [
+                "nitrification",
+                "RNA"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2016-03-01",
-            "references": [
-                "https://doi.org/10.1016/j.chemosphere.2015.12.119"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -40017,20 +40011,24 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.chemosphere.2015.12.119"
+            ],
+            "rights": null,
+            "title": " Effects of Cr(III) and CR(VI) on nitrification inhibition as determined by SOUR, function-specific gene expression and 16S rRNA sequence analysis of wastewater nitrifying enrichments"
         },
         {
-            "title": "Conference Report: The 6th International Symposium on Waterborne Pathogens ",
-            "description": "A review of current literature on the occurrence of waterborne pathogens in DW systems. This dataset is not publicly accessible because: I am using published data from a journal not generated by EPA. It can be accessed through the following means: N/A. Format: no unique data has been generated. \n\nThis dataset is associated with the following publication:\nRochelle, P., P. Klonicki, G. DiGiovanni, V. Hill, Y. Akagi, and E. Villegas. Conference Report: The 6th International Symposium on Waterborne Pathogens ISWP 2015.   JOURNAL OF THE AMERICAN WATER WORKS ASSOCIATION. American Water Works Association, Denver, CO, USA, 107(10): 24-32, (2015).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:096"
-            ],
+            "contactPoint": {
+                "fn": "Eric Villegas",
+                "hasEmail": "mailto:villegas.eric@epa.gov"
+            },
+            "description": "A review of current literature on the occurrence of waterborne pathogens in DW systems. This dataset is not publicly accessible because: I am using published data from a journal not generated by EPA. It can be accessed through the following means: N/A. Format: no unique data has been generated. \n\nThis dataset is associated with the following publication:\nRochelle, P., P. Klonicki, G. DiGiovanni, V. Hill, Y. Akagi, and E. Villegas. Conference Report: The 6th International Symposium on Waterborne Pathogens ISWP 2015.   JOURNAL OF THE AMERICAN WATER WORKS ASSOCIATION. American Water Works Association, Denver, CO, USA, 107(10): 24-32, (2015).",
+            "distribution": [],
             "identifier": "A-2283-294",
             "keyword": [
                 "drinking water",
@@ -40040,14 +40038,10 @@
                 "legionella",
                 "waterborne pathogens"
             ],
-            "contactPoint": {
-                "fn": "Eric Villegas",
-                "hasEmail": "mailto:villegas.eric@epa.gov"
-            },
-            "distribution": [],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2016-09-21",
-            "references": [
-                "https://doi.org/10.5942/jawwa.2015.107.0156"
+            "programCode": [
+                "020:096"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -40057,19 +40051,29 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.5942/jawwa.2015.107.0156"
+            ],
+            "rights": null,
+            "title": "Conference Report: The 6th International Symposium on Waterborne Pathogens "
         },
         {
-            "title": "Human infective potential of Cryptosporidium spp., Giardia duodenalis and Enterocytozoon bieneusi in urban wastewater treatment plant effluents",
-            "description": "Cryptosporidiosis, giardiasis, and microsporidiosis are important waterborne diseases. In the\nstandard for wastewater treatment plant (WWTP) effluents in China and other countries, fecal\ncoliform is the only microbial indicator, raising concerns about the potential for pathogen\ntransmission through WWPT effluent reuse. In this study, we collected 50 effluent samples\n(30 L/sample) from three municipal WWTPs in Shanghai, China and analyzed for Cryptosporidium\nspp., Giardia duodenalis and Enterocytozoon bieneusi by microscopy and/or PCR. Moreover,\npropidium monoazide (PMA)-PCR was used to assess the viability of oocysts/cysts. The microscopy\nand PCR-positive rates for Cryptosporidium spp. were 62% and 40%, respectively. The occurrence\nrates of G. duodenalis were 96% by microscopy and 92\u2013100% by PCR analysis of three genetic loci.\nFurthermore, E. bieneusi was detected in 70% (35/50) of samples by PCR. Altogether, ten\nCryptosporidium species or genotypes, two G. duodenalis genotypes, and 11 E. bieneusi genotypes\nwere found, most of which were human-pathogenic. The chlorine dioxide disinfection employed in\nWWTP1 and WWTP3 failed to inactivate the residual pathogens; 93% of the samples from WWTP1 and\n83% from WWTP3 did not meet the national standard on fecal coliform levels. Thus, urban WWTP\neffluents often contain residual waterborne human pathogens. \n\nThis dataset is associated with the following publication:\nMa, J., Y. Feng, Y. Hu, E. Villegas , and L. Xiao. Human infective potential of Cryptosporidium spp., Giardia duodenalis and Enterocytozoon bieneusi in urban wastewater treatment plant effluents.   JOURNAL OF WATER AND HEALTH. IWA Publishing, London,  UK, 14(4): 411-423, (2016).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:096"
+            "contactPoint": {
+                "fn": "Eric Villegas",
+                "hasEmail": "mailto:villegas.eric@epa.gov"
+            },
+            "description": "Cryptosporidiosis, giardiasis, and microsporidiosis are important waterborne diseases. In the\nstandard for wastewater treatment plant (WWTP) effluents in China and other countries, fecal\ncoliform is the only microbial indicator, raising concerns about the potential for pathogen\ntransmission through WWPT effluent reuse. In this study, we collected 50 effluent samples\n(30 L/sample) from three municipal WWTPs in Shanghai, China and analyzed for Cryptosporidium\nspp., Giardia duodenalis and Enterocytozoon bieneusi by microscopy and/or PCR. Moreover,\npropidium monoazide (PMA)-PCR was used to assess the viability of oocysts/cysts. The microscopy\nand PCR-positive rates for Cryptosporidium spp. were 62% and 40%, respectively. The occurrence\nrates of G. duodenalis were 96% by microscopy and 92\u2013100% by PCR analysis of three genetic loci.\nFurthermore, E. bieneusi was detected in 70% (35/50) of samples by PCR. Altogether, ten\nCryptosporidium species or genotypes, two G. duodenalis genotypes, and 11 E. bieneusi genotypes\nwere found, most of which were human-pathogenic. The chlorine dioxide disinfection employed in\nWWTP1 and WWTP3 failed to inactivate the residual pathogens; 93% of the samples from WWTP1 and\n83% from WWTP3 did not meet the national standard on fecal coliform levels. Thus, urban WWTP\neffluents often contain residual waterborne human pathogens. \n\nThis dataset is associated with the following publication:\nMa, J., Y. Feng, Y. Hu, E. Villegas , and L. Xiao. Human infective potential of Cryptosporidium spp., Giardia duodenalis and Enterocytozoon bieneusi in urban wastewater treatment plant effluents.   JOURNAL OF WATER AND HEALTH. IWA Publishing, London,  UK, 14(4): 411-423, (2016).",
+            "distribution": [
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/295/NO%20EPA%20DATASETS%20WERE%20GENERATED%20IN%20THIS%20STUDY.docx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+                    "title": "NO EPA DATASETS WERE GENERATED IN THIS STUDY.docx"
+                }
             ],
             "identifier": "A-dfnd-295",
             "keyword": [
@@ -40081,20 +40085,10 @@
                 "occurrence",
                 "water reuse"
             ],
-            "contactPoint": {
-                "fn": "Eric Villegas",
-                "hasEmail": "mailto:villegas.eric@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "NO EPA DATASETS WERE GENERATED IN THIS STUDY.docx",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/295/NO%20EPA%20DATASETS%20WERE%20GENERATED%20IN%20THIS%20STUDY.docx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2016-09-21",
-            "references": [
-                "http://jwh.iwaponline.com/content/early/2016/01/04/wh.2016.192"
+            "programCode": [
+                "020:096"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -40104,19 +40098,31 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "http://jwh.iwaponline.com/content/early/2016/01/04/wh.2016.192"
+            ],
+            "rights": null,
+            "title": "Human infective potential of Cryptosporidium spp., Giardia duodenalis and Enterocytozoon bieneusi in urban wastewater treatment plant effluents"
         },
         {
-            "title": "Detection and Quantification of Silver Nanoparticles at Environmentally Relevant Concentrations Using Asymmetric Flow Field\u2212Flow Fractionation Online with Single Particle Inductively Coupled Plasma Mass Spectrometry",
-            "description": "The presence of silver nanoparticles (AgNPs) in aquatic environments could potentially cause adverse impacts on ecosystems and human health.  However, current understanding of the environmental fate and transport of AgNPs is still limited because their properties in complex environmental samples cannot be accurately determined.  In this study, the feasibility of using asymmetric flow field-flow fractionation (AF4) connected online with single particle inductively coupled plasma mass spectrometry (spICPMS) to detect and quantify AgNPs at environmentally relevant concentrations was investigated.  The AF4 channel had a thickness of 350 \u00b5m and its accumulation wall was a 10 kDa regenerated cellulose membrane.  A 0.02 % FL-70 surfactant solution was used as an AF4 carrier.  With 1.2 mL/min AF4 cross flow rate, 1.5 mL/min AF4 channel flow rate, and 5 ms spICPMS dwell time, the AF4\u2013spICPMS can detect and quantify 40 \u2013 80 nm AgNPs, as well as Ag-SiO2 nanoparticles (51.0 nm diameter Ag core and 21.6 nm SiO2 shell), with good recovery within 30 min.  This system was not only effective in differentiating and quantifying different types of AgNPs with similar hydrodynamic diameters, such as in mixtures containing Ag-SiO2 core-shell nanoparticles and 40 \u2013 80 nm AgNPs, but also suitable for differentiating between 40 nm AgNPs and elevated dissolved Ag content.  The study results indicate that AF4\u2013spICPMS is capable of detecting and quantifying AgNPs and other engineered metal- nanomaterials in environmental samples.  Nevertheless, further studies are needed before AF4\u2013spICPMS can become a routine analytical technique. \n\nThis dataset is associated with the following publication:\nHuynh, K.A., E. Siska, E. Heithmar, S. Tadjiki, and S. Pergantis. Detection and Quantification of Silver Nanoparticles at Environmentally Relevant Concentrations Using Asymmetric Flow Field\u2013Flow Fractionation Online with Single Particle Inductively Coupled Plasma Mass Spectrometry.   Analytical Chemistry. American Chemical Society, Washington, DC, USA, 88(9): 4909\u20134916, (2016).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:095"
+            "contactPoint": {
+                "fn": "Edward Heithmar",
+                "hasEmail": "mailto:heithmar.ed@epa.gov"
+            },
+            "describedBy": "https://pasteur.epa.gov/uploads/210/documents/Data%20Dictionary%20for%20Supporting%20Information.docx",
+            "describedByType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+            "description": "The presence of silver nanoparticles (AgNPs) in aquatic environments could potentially cause adverse impacts on ecosystems and human health.  However, current understanding of the environmental fate and transport of AgNPs is still limited because their properties in complex environmental samples cannot be accurately determined.  In this study, the feasibility of using asymmetric flow field-flow fractionation (AF4) connected online with single particle inductively coupled plasma mass spectrometry (spICPMS) to detect and quantify AgNPs at environmentally relevant concentrations was investigated.  The AF4 channel had a thickness of 350 \u00b5m and its accumulation wall was a 10 kDa regenerated cellulose membrane.  A 0.02 % FL-70 surfactant solution was used as an AF4 carrier.  With 1.2 mL/min AF4 cross flow rate, 1.5 mL/min AF4 channel flow rate, and 5 ms spICPMS dwell time, the AF4\u2013spICPMS can detect and quantify 40 \u2013 80 nm AgNPs, as well as Ag-SiO2 nanoparticles (51.0 nm diameter Ag core and 21.6 nm SiO2 shell), with good recovery within 30 min.  This system was not only effective in differentiating and quantifying different types of AgNPs with similar hydrodynamic diameters, such as in mixtures containing Ag-SiO2 core-shell nanoparticles and 40 \u2013 80 nm AgNPs, but also suitable for differentiating between 40 nm AgNPs and elevated dissolved Ag content.  The study results indicate that AF4\u2013spICPMS is capable of detecting and quantifying AgNPs and other engineered metal- nanomaterials in environmental samples.  Nevertheless, further studies are needed before AF4\u2013spICPMS can become a routine analytical technique. \n\nThis dataset is associated with the following publication:\nHuynh, K.A., E. Siska, E. Heithmar, S. Tadjiki, and S. Pergantis. Detection and Quantification of Silver Nanoparticles at Environmentally Relevant Concentrations Using Asymmetric Flow Field\u2013Flow Fractionation Online with Single Particle Inductively Coupled Plasma Mass Spectrometry.   Analytical Chemistry. American Chemical Society, Washington, DC, USA, 88(9): 4909\u20134916, (2016).",
+            "distribution": [
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/210/20160407%20-%20Revised%20Supporting%20Information_Final.pdf",
+                    "mediaType": "application/pdf",
+                    "title": "20160407 - Revised Supporting Information_Final.pdf"
+                }
             ],
             "identifier": "A-n2zk-210",
             "keyword": [
@@ -40127,20 +40133,10 @@
                 "characterization",
                 "environmental matrices"
             ],
-            "contactPoint": {
-                "fn": "Edward Heithmar",
-                "hasEmail": "mailto:heithmar.ed@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "20160407 - Revised Supporting Information_Final.pdf",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/210/20160407%20-%20Revised%20Supporting%20Information_Final.pdf",
-                    "mediaType": "application/pdf"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2016-04-11",
-            "references": [
-                "http://pubs.acs.org/doi/abs/10.1021/acs.analchem.6b00764"
+            "programCode": [
+                "020:095"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -40151,20 +40147,27 @@
                     }
                 }
             },
-            "describedBy": "https://pasteur.epa.gov/uploads/210/documents/Data%20Dictionary%20for%20Supporting%20Information.docx",
-            "describedByType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
+            "references": [
+                "http://pubs.acs.org/doi/abs/10.1021/acs.analchem.6b00764"
+            ],
+            "rights": null,
+            "title": "Detection and Quantification of Silver Nanoparticles at Environmentally Relevant Concentrations Using Asymmetric Flow Field\u2212Flow Fractionation Online with Single Particle Inductively Coupled Plasma Mass Spectrometry"
         },
         {
-            "title": "High-throughput screening of chemical effects on steroidogenesis using H295R human adrenocortical carcinoma cells",
-            "description": "Disruption of steroidogenesis by environmental chemicals can result in altered hormone levels causing adverse reproductive and developmental effects. A high-throughput assay using H295R human adrenocortical carcinoma cells was used to evaluate the effect of 2060 chemical samples on steroidogenesis via high-performance liquid chromatography followed by tandem mass spectrometry quantification of 10 steroid hormones, including progestagens, glucocorticoids, androgens, and estrogens. The study employed a 3 stage screening strategy. The first stage established the maximum tolerated concentration (MTC; \u2265 70% viability) per sample. The second stage quantified changes in hormone levels at the MTC whereas the third stage performed concentration-response (CR) on a subset of samples. At all stages, cells were prestimulated with 10 \u00b5M forskolin for 48\u2009h to induce steroidogenesis followed by chemical treatment for 48\u2009h. Of the 2060 chemical samples evaluated, 524 samples were selected for 6-point CR screening, based in part on significantly altering at least 4 hormones at the MTC. CR screening identified 232 chemical samples with concentration-dependent effects on 17\u03b2-estradiol and/or testosterone, with 411 chemical samples showing an effect on at least one hormone across the steroidogenesis pathway. Clustering of the concentration-dependent chemical-mediated steroid hormone effects grouped chemical samples into 5 distinct profiles generally representing putative mechanisms of action, including CYP17A1 and HSD3B inhibition. A distinct pattern was observed between imidazole and triazole fungicides suggesting potentially distinct mechanisms of action. From a chemical testing and prioritization perspective, this assay platform provides a robust model for high-throughput screening of chemicals for effects on steroidogenesis. \n\nThis dataset is associated with the following publication:\nKarmaus , A., C. Toole, D. Filer , K. Lewis, and M. Martin. (Toxicological Sciences) High-throughput screening of chemical effects on steroidogenesis using H295R human adrenocortical carcinoma cells.   TOXICOLOGICAL SCIENCES. Society of Toxicology,    150(2): 323-332, (2016).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:095"
+            "contactPoint": {
+                "fn": "Keith Houck",
+                "hasEmail": "mailto:houck.keith@epa.gov"
+            },
+            "description": "Disruption of steroidogenesis by environmental chemicals can result in altered hormone levels causing adverse reproductive and developmental effects. A high-throughput assay using H295R human adrenocortical carcinoma cells was used to evaluate the effect of 2060 chemical samples on steroidogenesis via high-performance liquid chromatography followed by tandem mass spectrometry quantification of 10 steroid hormones, including progestagens, glucocorticoids, androgens, and estrogens. The study employed a 3 stage screening strategy. The first stage established the maximum tolerated concentration (MTC; \u2265 70% viability) per sample. The second stage quantified changes in hormone levels at the MTC whereas the third stage performed concentration-response (CR) on a subset of samples. At all stages, cells were prestimulated with 10 \u00b5M forskolin for 48\u2009h to induce steroidogenesis followed by chemical treatment for 48\u2009h. Of the 2060 chemical samples evaluated, 524 samples were selected for 6-point CR screening, based in part on significantly altering at least 4 hormones at the MTC. CR screening identified 232 chemical samples with concentration-dependent effects on 17\u03b2-estradiol and/or testosterone, with 411 chemical samples showing an effect on at least one hormone across the steroidogenesis pathway. Clustering of the concentration-dependent chemical-mediated steroid hormone effects grouped chemical samples into 5 distinct profiles generally representing putative mechanisms of action, including CYP17A1 and HSD3B inhibition. A distinct pattern was observed between imidazole and triazole fungicides suggesting potentially distinct mechanisms of action. From a chemical testing and prioritization perspective, this assay platform provides a robust model for high-throughput screening of chemicals for effects on steroidogenesis. \n\nThis dataset is associated with the following publication:\nKarmaus , A., C. Toole, D. Filer , K. Lewis, and M. Martin. (Toxicological Sciences) High-throughput screening of chemical effects on steroidogenesis using H295R human adrenocortical carcinoma cells.   TOXICOLOGICAL SCIENCES. Society of Toxicology,    150(2): 323-332, (2016).",
+            "distribution": [
+                {
+                    "accessURL": "https://gaftp.epa.gov/COMPTOX/NCCT_Publication_Data/MartinMatt/ToxCast_Steroidogenesis/",
+                    "title": "https://gaftp.epa.gov/COMPTOX/NCCT_Publication_Data/MartinMatt/ToxCast_Steroidogenesis/"
+                }
             ],
             "identifier": "A-x0kx-385",
             "keyword": [
@@ -40176,19 +40179,10 @@
                 "ToxCast",
                 "computational toxicology"
             ],
-            "contactPoint": {
-                "fn": "Keith Houck",
-                "hasEmail": "mailto:houck.keith@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "https://gaftp.epa.gov/COMPTOX/NCCT_Publication_Data/MartinMatt/ToxCast_Steroidogenesis/",
-                    "accessURL": "https://gaftp.epa.gov/COMPTOX/NCCT_Publication_Data/MartinMatt/ToxCast_Steroidogenesis/"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2016-04-02",
-            "references": [
-                "https://doi.org/10.1093/toxsci/kfw002"
+            "programCode": [
+                "020:095"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -40198,19 +40192,28 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1093/toxsci/kfw002"
+            ],
+            "rights": null,
+            "title": "High-throughput screening of chemical effects on steroidogenesis using H295R human adrenocortical carcinoma cells"
         },
         {
-            "title": "Using ToxCast data to reconstruct dynamic cell state trajectories and estimate toxicological points of departure.",
-            "description": "Background: High-content imaging (HCI) allows simultaneous measurement of multiple cellular phenotypic changes and is an important tool for evaluating the biological activity of chemicals.\r\nObjectives: Our goal was to analyze dynamic cellular changes using HCI to identify the \u201ctipping point\u201d at which the cells did not show recovery towards a normal phenotypic state.\r\nMethods: HCI was used to evaluate the effects of 967 chemicals (in concentrations ranging from 0.4 to 200 \u03bcM) on HepG2 cells over a 72-hr exposure period. The HCI end points included p53, c-Jun, histone H2A.x, \u03b1-tubulin, histone H3, alpha tubulin, mitochondrial membrane potential, mitochondrial mass, cell cycle arrest, nuclear size, and cell number. A computational model was developed to interpret HCI responses as cell-state trajectories.\r\nResults: Analysis of cell-state trajectories showed that 336 chemicals produced tipping points and that HepG2 cells were resilient to the effects of 334 chemicals up to the highest concentration (200 \u03bcM) and duration (72 hr) tested. Tipping points were identified as concentration-dependent transitions in system recovery, and the corresponding critical concentrations were generally between 5 and 15 times (25th and 75th percentiles, respectively) lower than the concentration that produced any significant effect on HepG2 cells. The remaining 297 chemicals require more data before they can be placed in either of these categories.\r\nConclusions: These findings show the utility of HCI data for reconstructing cell state trajectories and provide insight into the adaptation and resilience of in vitro cellular systems based on tipping points. Cellular tipping points could be used to define a point of departure for risk-based prioritization of environmental chemicals. \n\nThis dataset is associated with the following publication:\nShah , I., W. Setzer , J. Jack, K. Houck , R. Judson , T. Knudsen , J. Liu, M. Martin , D. Reif, A.M. Richard , R.S. Thomas , K. Crofton , D.J. Dix , and R.J. Kavlock. (Envir. Health Perspect.)   Using ToxCast data to reconstruct dynamic cell state trajectories and estimate toxicological points of departure.   ENVIRONMENTAL HEALTH PERSPECTIVES. National Institute of Environmental Health Sciences (NIEHS), Research Triangle Park, NC, USA,  1-33, (2015).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:095"
+            "contactPoint": {
+                "fn": "Thomas Knudsen",
+                "hasEmail": "mailto:knudsen.thomas@epa.gov"
+            },
+            "description": "Background: High-content imaging (HCI) allows simultaneous measurement of multiple cellular phenotypic changes and is an important tool for evaluating the biological activity of chemicals.\r\nObjectives: Our goal was to analyze dynamic cellular changes using HCI to identify the \u201ctipping point\u201d at which the cells did not show recovery towards a normal phenotypic state.\r\nMethods: HCI was used to evaluate the effects of 967 chemicals (in concentrations ranging from 0.4 to 200 \u03bcM) on HepG2 cells over a 72-hr exposure period. The HCI end points included p53, c-Jun, histone H2A.x, \u03b1-tubulin, histone H3, alpha tubulin, mitochondrial membrane potential, mitochondrial mass, cell cycle arrest, nuclear size, and cell number. A computational model was developed to interpret HCI responses as cell-state trajectories.\r\nResults: Analysis of cell-state trajectories showed that 336 chemicals produced tipping points and that HepG2 cells were resilient to the effects of 334 chemicals up to the highest concentration (200 \u03bcM) and duration (72 hr) tested. Tipping points were identified as concentration-dependent transitions in system recovery, and the corresponding critical concentrations were generally between 5 and 15 times (25th and 75th percentiles, respectively) lower than the concentration that produced any significant effect on HepG2 cells. The remaining 297 chemicals require more data before they can be placed in either of these categories.\r\nConclusions: These findings show the utility of HCI data for reconstructing cell state trajectories and provide insight into the adaptation and resilience of in vitro cellular systems based on tipping points. Cellular tipping points could be used to define a point of departure for risk-based prioritization of environmental chemicals. \n\nThis dataset is associated with the following publication:\nShah , I., W. Setzer , J. Jack, K. Houck , R. Judson , T. Knudsen , J. Liu, M. Martin , D. Reif, A.M. Richard , R.S. Thomas , K. Crofton , D.J. Dix , and R.J. Kavlock. (Envir. Health Perspect.)   Using ToxCast data to reconstruct dynamic cell state trajectories and estimate toxicological points of departure.   ENVIRONMENTAL HEALTH PERSPECTIVES. National Institute of Environmental Health Sciences (NIEHS), Research Triangle Park, NC, USA,  1-33, (2015).",
+            "distribution": [
+                {
+                    "accessURL": "https://gaftp.epa.gov/COMPTOX/NCCT_Publication_Data/ShahImran/PODTipping_Point/",
+                    "title": "https://gaftp.epa.gov/COMPTOX/NCCT_Publication_Data/ShahImran/PODTipping_Point/"
+                }
             ],
             "identifier": "A-dncw-386",
             "keyword": [
@@ -40220,19 +40223,10 @@
                 "virtual liver",
                 "tipping points"
             ],
-            "contactPoint": {
-                "fn": "Thomas Knudsen",
-                "hasEmail": "mailto:knudsen.thomas@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "https://gaftp.epa.gov/COMPTOX/NCCT_Publication_Data/ShahImran/PODTipping_Point/",
-                    "accessURL": "https://gaftp.epa.gov/COMPTOX/NCCT_Publication_Data/ShahImran/PODTipping_Point/"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2016-07-01",
-            "references": [
-                "https://doi.org/10.1289/ehp.1409029"
+            "programCode": [
+                "020:095"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -40242,19 +40236,29 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1289/ehp.1409029"
+            ],
+            "rights": null,
+            "title": "Using ToxCast data to reconstruct dynamic cell state trajectories and estimate toxicological points of departure."
         },
         {
-            "title": "Rumsey and Walker_AMT_2016_Table 1",
-            "description": "Table summarizes instrument analytical detection limits, including liquid and equivalent air concentrations. \n\nThis dataset is associated with the following publication:\nRumsey, I. Application of an online ion chromatography-based instrument for gradient flux measurements of speciated nitrogen and sulfur.   ENVIRONMENTAL SCIENCE & TECHNOLOGY. American Chemical Society, Washington, DC, USA, 9(6): 2581-2592, (2016).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
+            "contactPoint": {
+                "fn": "John Walker",
+                "hasEmail": "mailto:walker.johnt@epa.gov"
+            },
+            "description": "Table summarizes instrument analytical detection limits, including liquid and equivalent air concentrations. \n\nThis dataset is associated with the following publication:\nRumsey, I. Application of an online ion chromatography-based instrument for gradient flux measurements of speciated nitrogen and sulfur.   ENVIRONMENTAL SCIENCE & TECHNOLOGY. American Chemical Society, Washington, DC, USA, 9(6): 2581-2592, (2016).",
+            "distribution": [
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/392/Rumsey%20and%20Walker_AMT_2016_Table%201.xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Rumsey and Walker_AMT_2016_Table 1.xlsx"
+                }
             ],
             "identifier": "A-fn3b-392",
             "keyword": [
@@ -40266,20 +40270,10 @@
                 "sulfur",
                 "micrometeorology"
             ],
-            "contactPoint": {
-                "fn": "John Walker",
-                "hasEmail": "mailto:walker.johnt@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "Rumsey and Walker_AMT_2016_Table 1.xlsx",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/392/Rumsey%20and%20Walker_AMT_2016_Table%201.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2016-06-17",
-            "references": [
-                "https://doi.org/10.5194/amt-9-2581-2016"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -40289,19 +40283,29 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.5194/amt-9-2581-2016"
+            ],
+            "rights": null,
+            "title": "Rumsey and Walker_AMT_2016_Table 1"
         },
         {
-            "title": "Rumsey and Walker_AMT_2016_Table 2.xlsx",
-            "description": "Table summarizes instrument precision assessed by collocating the two sample boxes. Precision is quantified as the standard deviation of the residuals of an orthogonal least squares regression of concentrations from the two sample boxes. This allows for an estimation of gradient precision and ultimately gradient and flux detection limits. \n\nThis dataset is associated with the following publication:\nRumsey, I. Application of an online ion chromatography-based instrument for gradient flux measurements of speciated nitrogen and sulfur.   ENVIRONMENTAL SCIENCE & TECHNOLOGY. American Chemical Society, Washington, DC, USA, 9(6): 2581-2592, (2016).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
+            "contactPoint": {
+                "fn": "John Walker",
+                "hasEmail": "mailto:walker.johnt@epa.gov"
+            },
+            "description": "Table summarizes instrument precision assessed by collocating the two sample boxes. Precision is quantified as the standard deviation of the residuals of an orthogonal least squares regression of concentrations from the two sample boxes. This allows for an estimation of gradient precision and ultimately gradient and flux detection limits. \n\nThis dataset is associated with the following publication:\nRumsey, I. Application of an online ion chromatography-based instrument for gradient flux measurements of speciated nitrogen and sulfur.   ENVIRONMENTAL SCIENCE & TECHNOLOGY. American Chemical Society, Washington, DC, USA, 9(6): 2581-2592, (2016).",
+            "distribution": [
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/393/Rumsey%20and%20Walker_AMT_2016_Table%202.xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Rumsey and Walker_AMT_2016_Table 2.xlsx"
+                }
             ],
             "identifier": "A-fn3b-393",
             "keyword": [
@@ -40316,20 +40320,10 @@
                 "sulfur",
                 "micrometeorology"
             ],
-            "contactPoint": {
-                "fn": "John Walker",
-                "hasEmail": "mailto:walker.johnt@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "Rumsey and Walker_AMT_2016_Table 2.xlsx",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/393/Rumsey%20and%20Walker_AMT_2016_Table%202.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2016-06-17",
-            "references": [
-                "https://doi.org/10.5194/amt-9-2581-2016"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -40339,19 +40333,29 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.5194/amt-9-2581-2016"
+            ],
+            "rights": null,
+            "title": "Rumsey and Walker_AMT_2016_Table 2.xlsx"
         },
         {
-            "title": "Rumsey and Walker_AMT_2016_Figure 1.xlsx",
-            "description": "Figure summarizes diurnal profiles of uncertainty in the chemical gradient and transfer velocity measurements from which fluxes are calculated. \n\nThis dataset is associated with the following publication:\nRumsey, I. Application of an online ion chromatography-based instrument for gradient flux measurements of speciated nitrogen and sulfur.   ENVIRONMENTAL SCIENCE & TECHNOLOGY. American Chemical Society, Washington, DC, USA, 9(6): 2581-2592, (2016).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
+            "contactPoint": {
+                "fn": "John Walker",
+                "hasEmail": "mailto:walker.johnt@epa.gov"
+            },
+            "description": "Figure summarizes diurnal profiles of uncertainty in the chemical gradient and transfer velocity measurements from which fluxes are calculated. \n\nThis dataset is associated with the following publication:\nRumsey, I. Application of an online ion chromatography-based instrument for gradient flux measurements of speciated nitrogen and sulfur.   ENVIRONMENTAL SCIENCE & TECHNOLOGY. American Chemical Society, Washington, DC, USA, 9(6): 2581-2592, (2016).",
+            "distribution": [
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/399/Rumsey%20and%20Walker_AMT_2016_Figure%201.xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Rumsey and Walker_AMT_2016_Figure 1.xlsx"
+                }
             ],
             "identifier": "A-fn3b-399",
             "keyword": [
@@ -40363,20 +40367,10 @@
                 "sulfur",
                 "micrometeorology"
             ],
-            "contactPoint": {
-                "fn": "John Walker",
-                "hasEmail": "mailto:walker.johnt@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "Rumsey and Walker_AMT_2016_Figure 1.xlsx",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/399/Rumsey%20and%20Walker_AMT_2016_Figure%201.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2016-06-17",
-            "references": [
-                "https://doi.org/10.5194/amt-9-2581-2016"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -40386,19 +40380,29 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.5194/amt-9-2581-2016"
+            ],
+            "rights": null,
+            "title": "Rumsey and Walker_AMT_2016_Figure 1.xlsx"
         },
         {
-            "title": "Rumsey and Walker_AMT_2016_Figure 2.xlsx",
-            "description": "Figure summarizes uncertainty (error) in hourly gradient flux measurements by individual analyte. Flux uncertainty is derived from estimates of uncertainty in chemical gradients and turbulent transfer velocity. \n\nThis dataset is associated with the following publication:\nRumsey, I. Application of an online ion chromatography-based instrument for gradient flux measurements of speciated nitrogen and sulfur.   ENVIRONMENTAL SCIENCE & TECHNOLOGY. American Chemical Society, Washington, DC, USA, 9(6): 2581-2592, (2016).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
+            "contactPoint": {
+                "fn": "John Walker",
+                "hasEmail": "mailto:walker.johnt@epa.gov"
+            },
+            "description": "Figure summarizes uncertainty (error) in hourly gradient flux measurements by individual analyte. Flux uncertainty is derived from estimates of uncertainty in chemical gradients and turbulent transfer velocity. \n\nThis dataset is associated with the following publication:\nRumsey, I. Application of an online ion chromatography-based instrument for gradient flux measurements of speciated nitrogen and sulfur.   ENVIRONMENTAL SCIENCE & TECHNOLOGY. American Chemical Society, Washington, DC, USA, 9(6): 2581-2592, (2016).",
+            "distribution": [
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/400/Rumsey%20and%20Walker_AMT_2016_Figure%202.xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Rumsey and Walker_AMT_2016_Figure 2.xlsx"
+                }
             ],
             "identifier": "A-fn3b-400",
             "keyword": [
@@ -40411,20 +40415,10 @@
                 "sulfur",
                 "micrometeorology"
             ],
-            "contactPoint": {
-                "fn": "John Walker",
-                "hasEmail": "mailto:walker.johnt@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "Rumsey and Walker_AMT_2016_Figure 2.xlsx",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/400/Rumsey%20and%20Walker_AMT_2016_Figure%202.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2016-06-17",
-            "references": [
-                "https://doi.org/10.5194/amt-9-2581-2016"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -40434,53 +40428,53 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.5194/amt-9-2581-2016"
+            ],
+            "rights": null,
+            "title": "Rumsey and Walker_AMT_2016_Figure 2.xlsx"
         },
         {
-            "title": "Draft genome sequence of two Shingopyxis sp. strains H107 and H115 isolated from a chloraminated drinking water distriburion system simulator",
-            "description": "Draft genome sequence of two Shingopyxis sp. strains H107 and H115 isolated from a chloraminated drinking water distriburion system simulator. \n\nThis dataset is associated with the following publication:\nGomez-Alvarez, V., S. Pfaller , and R. Revetta. Draft Genome of Two Sphingopyxis sp. Strains, Dominant Members of the Bacterial Community Associated with a Drinking Water Distribution System Simulator.   Genome Announcements. American Society for Microbiology, Washington, DC, USA, 4(2): e00183-16, (2016).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "A-kps7-405",
-            "keyword": [
-                "drinkig water",
-                "genome",
-                "Shingopyxis",
-                "antibiotic resistance",
-                "genes",
-                "drinking water",
-                "Sphingopyxis"
-            ],
             "contactPoint": {
                 "fn": "Randy Revetta",
                 "hasEmail": "mailto:revetta.randy@epa.gov"
             },
+            "description": "Draft genome sequence of two Shingopyxis sp. strains H107 and H115 isolated from a chloraminated drinking water distriburion system simulator. \n\nThis dataset is associated with the following publication:\nGomez-Alvarez, V., S. Pfaller , and R. Revetta. Draft Genome of Two Sphingopyxis sp. Strains, Dominant Members of the Bacterial Community Associated with a Drinking Water Distribution System Simulator.   Genome Announcements. American Society for Microbiology, Washington, DC, USA, 4(2): e00183-16, (2016).",
             "distribution": [
                 {
-                    "title": "H107.txt",
                     "downloadURL": "https://pasteur.epa.gov/uploads/405/H107.txt",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "H107.txt"
                 },
                 {
-                    "title": "H115.txt",
                     "downloadURL": "https://pasteur.epa.gov/uploads/405/H115.txt",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "H115.txt"
                 },
                 {
-                    "title": "https://www.ncbi.nlm.nih.gov/genbank/",
-                    "accessURL": "https://www.ncbi.nlm.nih.gov/genbank/"
+                    "accessURL": "https://www.ncbi.nlm.nih.gov/genbank/",
+                    "title": "https://www.ncbi.nlm.nih.gov/genbank/"
                 }
             ],
+            "identifier": "A-kps7-405",
+            "keyword": [
+                "drinkig water",
+                "genome",
+                "Shingopyxis",
+                "antibiotic resistance",
+                "genes",
+                "drinking water",
+                "Sphingopyxis"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2016-02-01",
-            "references": [
-                "https://doi.org/10.1128/genomea.00183-16"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -40490,20 +40484,24 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1128/genomea.00183-16"
+            ],
+            "rights": null,
+            "title": "Draft genome sequence of two Shingopyxis sp. strains H107 and H115 isolated from a chloraminated drinking water distriburion system simulator"
         },
         {
-            "title": "Bench-Scale and Pilot-Scale Treatment Technologies for the Removal of Total Dissolved Solids from Coal Mine Water: A Review.  ",
-            "description": "There is no database. This dataset is not publicly accessible because: This is a review manuscript, there was not data generated under this effort. All data used was secondary data and sources of the data were identified in the manuscript. It can be accessed through the following means: there is no database. Format: There is no database. \n\nThis dataset is associated with the following publication:\nPinto, P., S. Al-Abed , D. Balz, B. Butler , R. Landy , and S. Smith. Bench-Scale and Pilot-Scale Treatment Technologies for the Removal of Total Dissolved Solids from Coal Mine Water: A Review.  Robert Kleinmann  Mine Water and the Environment. Springer-Verlag, BERLIN-HEIDELBERG,  GERMANY, 35(1): 94-112, (2016).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
+            "contactPoint": {
+                "fn": "Souhail Al-Abed",
+                "hasEmail": "mailto:al-abed.souhail@epa.gov"
+            },
+            "description": "There is no database. This dataset is not publicly accessible because: This is a review manuscript, there was not data generated under this effort. All data used was secondary data and sources of the data were identified in the manuscript. It can be accessed through the following means: there is no database. Format: There is no database. \n\nThis dataset is associated with the following publication:\nPinto, P., S. Al-Abed , D. Balz, B. Butler , R. Landy , and S. Smith. Bench-Scale and Pilot-Scale Treatment Technologies for the Removal of Total Dissolved Solids from Coal Mine Water: A Review.  Robert Kleinmann  Mine Water and the Environment. Springer-Verlag, BERLIN-HEIDELBERG,  GERMANY, 35(1): 94-112, (2016).",
+            "distribution": [],
             "identifier": "A-rr5h-406",
             "keyword": [
                 "There is no database",
@@ -40515,14 +40513,10 @@
                 "precipitation",
                 "reverse osmosis"
             ],
-            "contactPoint": {
-                "fn": "Souhail Al-Abed",
-                "hasEmail": "mailto:al-abed.souhail@epa.gov"
-            },
-            "distribution": [],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2016-09-28",
-            "references": [
-                "https://doi.org/10.1007/s10230-015-0351-7"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -40532,19 +40526,29 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1007/s10230-015-0351-7"
+            ],
+            "rights": null,
+            "title": "Bench-Scale and Pilot-Scale Treatment Technologies for the Removal of Total Dissolved Solids from Coal Mine Water: A Review.  "
         },
         {
-            "title": "Dataset of Atmospheric Environment Publication in 2016, Characterization of organophosphorus flame retardants\u2019 sorption on building materials and consumer products",
-            "description": "The data presented in this data file is a product of a journal publication. The dataset contains OPFR sorption concentrations on building materials and consumer products and comparison to the i-SVOC model predictions. \n\nThis dataset is associated with the following publication:\nLiu , X., M. Allen, and N. Roache. Characterization of organophosphorus flame retardants' sorption on building materials and consumer products.   ATMOSPHERIC ENVIRONMENT. Elsevier Science Ltd, New York, NY, USA, 140: 333-341, (2016).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
+            "contactPoint": {
+                "fn": "Xiaoyu Liu",
+                "hasEmail": "mailto:liu.xiaoyu@epa.gov"
+            },
+            "description": "The data presented in this data file is a product of a journal publication. The dataset contains OPFR sorption concentrations on building materials and consumer products and comparison to the i-SVOC model predictions. \n\nThis dataset is associated with the following publication:\nLiu , X., M. Allen, and N. Roache. Characterization of organophosphorus flame retardants' sorption on building materials and consumer products.   ATMOSPHERIC ENVIRONMENT. Elsevier Science Ltd, New York, NY, USA, 140: 333-341, (2016).",
+            "distribution": [
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/164/XiaoyuLiu_A-6q5d_Data%20Tables%26Dictionary.xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "XiaoyuLiu_A-6q5d_Data Tables&Dictionary.xlsx"
+                }
             ],
             "identifier": "A-6q5d-164",
             "keyword": [
@@ -40558,20 +40562,10 @@
                 "Material-phase diffusion coefficient",
                 "Sink"
             ],
-            "contactPoint": {
-                "fn": "Xiaoyu Liu",
-                "hasEmail": "mailto:liu.xiaoyu@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "XiaoyuLiu_A-6q5d_Data Tables&Dictionary.xlsx",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/164/XiaoyuLiu_A-6q5d_Data%20Tables%26Dictionary.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2016-08-04",
-            "references": [
-                "https://doi.org/10.1016/j.atmosenv.2016.06.019"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -40581,53 +40575,52 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.atmosenv.2016.06.019"
+            ],
+            "rights": null,
+            "title": "Dataset of Atmospheric Environment Publication in 2016, Characterization of organophosphorus flame retardants\u2019 sorption on building materials and consumer products"
         },
         {
-            "title": "Gulf of Mexico Nutrient, carbon, CTD data",
-            "description": "Gulf of Mexico cruise, nearshore and CTD data collected by the USEPA during 2002 - 2008. \n\nThis dataset is associated with the following publications:\nPauer , J., T. Feist, A. Anstead, P. DePetro, W. Melendez, J. Lehrter , M. Murrell , X. Zhang, and D. Ko. A modeling study examining the impact of nutrient boundaries on primary production on the Louisiana Continental Shelf.   ECOLOGICAL MODELLING. Elsevier Science BV, Amsterdam,  NETHERLANDS, 328: 136-147, (2016).\nFeist, T., J. Pauer , W. Melendez, J. Lehrter , P. DePetro, K. Rygwelski , D. Ko, and R. Kreis. Modeling the relative importance of nutrient and carbon loads, boundary fluxes, and sediment fluxes on Gulf of Mexico hypoxia.   ENVIRONMENTAL SCIENCE & TECHNOLOGY. American Chemical Society, Washington, DC, USA, 50(16): 88713-8721, (2016).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "A-76hn-404",
-            "keyword": [
-                "Gulf of Mexico",
-                "Hypoxia",
-                "nutrients",
-                "CTD",
-                "Nutrient loadings"
-            ],
             "contactPoint": {
                 "fn": "James Pauer",
                 "hasEmail": "mailto:pauer.james@epa.gov"
             },
+            "description": "Gulf of Mexico cruise, nearshore and CTD data collected by the USEPA during 2002 - 2008. \n\nThis dataset is associated with the following publications:\nPauer , J., T. Feist, A. Anstead, P. DePetro, W. Melendez, J. Lehrter , M. Murrell , X. Zhang, and D. Ko. A modeling study examining the impact of nutrient boundaries on primary production on the Louisiana Continental Shelf.   ECOLOGICAL MODELLING. Elsevier Science BV, Amsterdam,  NETHERLANDS, 328: 136-147, (2016).\nFeist, T., J. Pauer , W. Melendez, J. Lehrter , P. DePetro, K. Rygwelski , D. Ko, and R. Kreis. Modeling the relative importance of nutrient and carbon loads, boundary fluxes, and sediment fluxes on Gulf of Mexico hypoxia.   ENVIRONMENTAL SCIENCE & TECHNOLOGY. American Chemical Society, Washington, DC, USA, 50(16): 88713-8721, (2016).",
             "distribution": [
                 {
-                    "title": "GED GoM Nutrients for Science Hub.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/404/GED%20GoM%20Nutrients%20for%20Science%20Hub.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "GED GoM Nutrients for Science Hub.xlsx"
                 },
                 {
-                    "title": "EPA_GED_INSHORE for Science Hub.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/404/EPA_GED_INSHORE%20for%20Science%20Hub.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "EPA_GED_INSHORE for Science Hub.xlsx"
                 },
                 {
-                    "title": "GED GoM CTD for Science Hub.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/404/GED%20GoM%20CTD%20for%20Science%20Hub.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "GED GoM CTD for Science Hub.xlsx"
                 }
             ],
+            "identifier": "A-76hn-404",
+            "keyword": [
+                "Gulf of Mexico",
+                "Hypoxia",
+                "nutrients",
+                "CTD",
+                "Nutrient loadings"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2016-09-27",
-            "references": [
-                "https://doi.org/10.1016/j.ecolmodel.2016.02.007",
-                "https://doi.org/10.1021/acs.est.6b01684"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -40637,42 +40630,43 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.ecolmodel.2016.02.007",
+                "https://doi.org/10.1021/acs.est.6b01684"
+            ],
+            "rights": null,
+            "title": "Gulf of Mexico Nutrient, carbon, CTD data"
         },
         {
-            "title": "Dataset of Building and Environment Publication in 2016, A reference method for measuring emissions of SVOCs in small chambers ",
-            "description": "The data presented in this data file is a product of a journal publication. The dataset contains DEHP air concentrations in the emission test chamber. \n\nThis dataset is associated with the following publication:\nWu, Y., S. Cox, Y. Xu, Y. Liang, D. Wong, X. Liu, J. Benning, P. Clausen, Y. Zhang, C. Liu, and J. Little. A Reference Method for Measuring Emissions of SVOCs in Small Chambers.   ENVIRONMENTAL SCIENCE & TECHNOLOGY. American Chemical Society, Washington, DC, USA, 95: 126-132, (2016).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "A-pk16-188",
-            "keyword": [
-                "Semi-volatile organic compounds",
-                "DEHP",
-                "Phthalates",
-                "Inter-laboratory study",
-                "Reference method"
-            ],
             "contactPoint": {
                 "fn": "Xiaoyu Liu",
                 "hasEmail": "mailto:liu.xiaoyu@epa.gov"
             },
+            "description": "The data presented in this data file is a product of a journal publication. The dataset contains DEHP air concentrations in the emission test chamber. \n\nThis dataset is associated with the following publication:\nWu, Y., S. Cox, Y. Xu, Y. Liang, D. Wong, X. Liu, J. Benning, P. Clausen, Y. Zhang, C. Liu, and J. Little. A Reference Method for Measuring Emissions of SVOCs in Small Chambers.   ENVIRONMENTAL SCIENCE & TECHNOLOGY. American Chemical Society, Washington, DC, USA, 95: 126-132, (2016).",
             "distribution": [
                 {
-                    "title": "XiaoyuLiu_A-pk16_Data Tables&Dictionary.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/188/XiaoyuLiu_A-pk16_Data%20Tables%26Dictionary.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "XiaoyuLiu_A-pk16_Data Tables&Dictionary.xlsx"
                 }
             ],
+            "identifier": "A-pk16-188",
+            "keyword": [
+                "Semi-volatile organic compounds",
+                "DEHP",
+                "Phthalates",
+                "Inter-laboratory study",
+                "Reference method"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2016-08-12",
-            "references": [
-                "https://doi.org/10.1016/j.buildenv.2015.08.025"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -40682,19 +40676,29 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.buildenv.2015.08.025"
+            ],
+            "rights": null,
+            "title": "Dataset of Building and Environment Publication in 2016, A reference method for measuring emissions of SVOCs in small chambers "
         },
         {
-            "title": "Dataset of Atmospheric Environment Publication in 2016, Source emission and model evaluation of formaldehyde from composite and solid wood furniture in a full-scale chamber ",
-            "description": "The data presented in this data file is a product of a journal publication. The dataset contains formaldehyde air concentrations in the emission test chamber and source emission model simulation results. \n\nThis dataset is associated with the following publication:\nLiu , X., M. Mason , Z. Guo , K. Krebs , and N. Roache. Source emission and model evaluation of formaldehyde from composite and solid wood furniture in a full-scale chamber.   ATMOSPHERIC ENVIRONMENT. Elsevier Science Ltd, New York, NY, USA, 122: 561-568, (2015).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
+            "contactPoint": {
+                "fn": "Xiaoyu Liu",
+                "hasEmail": "mailto:liu.xiaoyu@epa.gov"
+            },
+            "description": "The data presented in this data file is a product of a journal publication. The dataset contains formaldehyde air concentrations in the emission test chamber and source emission model simulation results. \n\nThis dataset is associated with the following publication:\nLiu , X., M. Mason , Z. Guo , K. Krebs , and N. Roache. Source emission and model evaluation of formaldehyde from composite and solid wood furniture in a full-scale chamber.   ATMOSPHERIC ENVIRONMENT. Elsevier Science Ltd, New York, NY, USA, 122: 561-568, (2015).",
+            "distribution": [
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/189/XiaoyuLiu_A-2bvs_Data%20Tables%26Dictionary.xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "XiaoyuLiu_A-2bvs_Data Tables&Dictionary.xlsx"
+                }
             ],
             "identifier": "A-2bvs-189",
             "keyword": [
@@ -40707,20 +40711,10 @@
                 "First-order decay model",
                 "Power-law decay model"
             ],
-            "contactPoint": {
-                "fn": "Xiaoyu Liu",
-                "hasEmail": "mailto:liu.xiaoyu@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "XiaoyuLiu_A-2bvs_Data Tables&Dictionary.xlsx",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/189/XiaoyuLiu_A-2bvs_Data%20Tables%26Dictionary.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2016-08-12",
-            "references": [
-                "https://doi.org/10.1016/j.atmosenv.2015.09.062"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -40730,44 +40724,44 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.atmosenv.2015.09.062"
+            ],
+            "rights": null,
+            "title": "Dataset of Atmospheric Environment Publication in 2016, Source emission and model evaluation of formaldehyde from composite and solid wood furniture in a full-scale chamber "
         },
         {
-            "title": "Simulating the hydrologic impacts of land cover and climate changes in a semi-arid watershed",
-            "description": "Changes in climate and land cover are among the principal variables affecting watershed hydrology.\nThis paper uses a cell-based model to examine the hydrologic impacts of climate and land-cover changes in the\nsemi-arid Lower Virgin River (LVR) watershed located upstream of Lake Mead, Nevada, USA. The cell-based\nmodel is developed by considering direct runoff based on the Soil Conservation Service - Curve Number (SCSCN)\nmethod and surplus runoff based on the Thornthwaite water balance theory. After calibration and validation,\nthe model is used to predict LVR discharge under future climate and land-cover changes. The hydrologic\nsimulation results reveal climate change as the dominant factor and land-cover change as a secondary factor in\nregulating future river discharge. The combined effects of climate and land-cover changes will slightly increase\nriver discharge in summer but substantially decrease discharge in winter. This impact on water resources deserves\nattention in climate change adaptation planning. \n\nThis dataset is associated with the following publication:\nChen, H., S. Tong, H. Yang, and J. Yang. Simulating the hydrologic impacts of land cover and climate changes in a semi-arid watershed.   Hydrological Sciences Journal. IAHS LIMITED, Oxford,  UK, 60(10): 1739-1758, (2015).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "A-v6xk-362",
-            "keyword": [
-                "land-cover change; climate change adaptation; hydrologic impacts; cell-based modeling",
-                "Regional adaptation case studies for sustainable water resources"
-            ],
             "contactPoint": {
                 "fn": "Yingping Yang",
                 "hasEmail": "mailto:yang.jeff@epa.gov"
             },
+            "description": "Changes in climate and land cover are among the principal variables affecting watershed hydrology.\nThis paper uses a cell-based model to examine the hydrologic impacts of climate and land-cover changes in the\nsemi-arid Lower Virgin River (LVR) watershed located upstream of Lake Mead, Nevada, USA. The cell-based\nmodel is developed by considering direct runoff based on the Soil Conservation Service - Curve Number (SCSCN)\nmethod and surplus runoff based on the Thornthwaite water balance theory. After calibration and validation,\nthe model is used to predict LVR discharge under future climate and land-cover changes. The hydrologic\nsimulation results reveal climate change as the dominant factor and land-cover change as a secondary factor in\nregulating future river discharge. The combined effects of climate and land-cover changes will slightly increase\nriver discharge in summer but substantially decrease discharge in winter. This impact on water resources deserves\nattention in climate change adaptation planning. \n\nThis dataset is associated with the following publication:\nChen, H., S. Tong, H. Yang, and J. Yang. Simulating the hydrologic impacts of land cover and climate changes in a semi-arid watershed.   Hydrological Sciences Journal. IAHS LIMITED, Oxford,  UK, 60(10): 1739-1758, (2015).",
             "distribution": [
                 {
-                    "title": "Lake Mead_Colorado River_ Data.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/362/Lake%20Mead_Colorado%20River_%20Data.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Lake Mead_Colorado River_ Data.xlsx"
                 },
                 {
-                    "title": "NCDC_Monthly Climate Data_LowerVStations.xls",
                     "downloadURL": "https://pasteur.epa.gov/uploads/362/NCDC_Monthly%20Climate%20Data_LowerVStations.xls",
-                    "mediaType": "application/vnd.ms-excel"
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "NCDC_Monthly Climate Data_LowerVStations.xls"
                 }
             ],
+            "identifier": "A-v6xk-362",
+            "keyword": [
+                "land-cover change; climate change adaptation; hydrologic impacts; cell-based modeling",
+                "Regional adaptation case studies for sustainable water resources"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2015-12-09",
-            "references": [
-                "http://www.tandfonline.com/doi/abs/10.1080/02626667.2014.948445#preview"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -40777,45 +40771,45 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "http://www.tandfonline.com/doi/abs/10.1080/02626667.2014.948445#preview"
+            ],
+            "rights": null,
+            "title": "Simulating the hydrologic impacts of land cover and climate changes in a semi-arid watershed"
         },
         {
-            "title": "Water consumption estimates of the biodiesel process in the US",
-            "description": "Electronic supplementary material The online version of this\narticle (doi:10.1007/s10098-015-1032-8) contains supplementary\nmaterial, which is available to authorized users. \n\nThis dataset is associated with the following publication:\nTu, Q., M. Lu, J. Yang , and D. Scott. Water Consumption Estimates of Biodiesel Process in the US.   CLEAN TECHNOLOGIES AND ENVIRONMENTAL POLICY. Springer-Verlag, New York, NY, USA, 18(2): 507-516, (2016).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "A-4mwc-358",
-            "keyword": [
-                "biodiesel",
-                "Water consumption",
-                "Irrigation"
-            ],
             "contactPoint": {
                 "fn": "Yingping Yang",
                 "hasEmail": "mailto:yang.jeff@epa.gov"
             },
+            "description": "Electronic supplementary material The online version of this\narticle (doi:10.1007/s10098-015-1032-8) contains supplementary\nmaterial, which is available to authorized users. \n\nThis dataset is associated with the following publication:\nTu, Q., M. Lu, J. Yang , and D. Scott. Water Consumption Estimates of Biodiesel Process in the US.   CLEAN TECHNOLOGIES AND ENVIRONMENTAL POLICY. Springer-Verlag, New York, NY, USA, 18(2): 507-516, (2016).",
             "distribution": [
                 {
-                    "title": "Supporting Information_Final_7000_sub.docx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/358/Supporting%20Information_Final_7000_sub.docx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+                    "title": "Supporting Information_Final_7000_sub.docx"
                 },
                 {
-                    "title": "Tu et al (15) Wat consumption of biofuel in US.pdf",
                     "downloadURL": "https://pasteur.epa.gov/uploads/358/Tu%20et%20al%20%2815%29%20Wat%20consumption%20of%20biofuel%20in%20US.pdf",
-                    "mediaType": "application/pdf"
+                    "mediaType": "application/pdf",
+                    "title": "Tu et al (15) Wat consumption of biofuel in US.pdf"
                 }
             ],
+            "identifier": "A-4mwc-358",
+            "keyword": [
+                "biodiesel",
+                "Water consumption",
+                "Irrigation"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2016-02-29",
-            "references": [
-                "http://link.springer.com/article/10.1007%2Fs10098-015-1032-8"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -40825,46 +40819,46 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "http://link.springer.com/article/10.1007%2Fs10098-015-1032-8"
+            ],
+            "rights": null,
+            "title": "Water consumption estimates of the biodiesel process in the US"
         },
         {
-            "title": " Near-road ultrafine particle and carbon monoxide measurements at North Carolina locations with and without roadside barriers",
-            "description": "These data are measurement time series collected onboard multiple mobile monitoring vehicles.  The data are at a high time resolution (seconds to minutes). \n\nThis dataset is associated with the following publication:\nLin, M., G. Hagler , R. Baldauf , V. Isakov , and A. Khlystov. The Effects of Vegetation Barriers on Near-road Ultrafine Particle Number and Carbon Monoxide Concentrations.   SCIENCE OF THE TOTAL ENVIRONMENT. Elsevier BV, AMSTERDAM,  NETHERLANDS, 553: 372-379, (2016).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "A-djhn-218",
-            "keyword": [
-                "near-road",
-                "vegetation",
-                "mitigation",
-                "air quality"
-            ],
             "contactPoint": {
                 "fn": "Gayle Hagler",
                 "hasEmail": "mailto:hagler.gayle@epa.gov"
             },
+            "description": "These data are measurement time series collected onboard multiple mobile monitoring vehicles.  The data are at a high time resolution (seconds to minutes). \n\nThis dataset is associated with the following publication:\nLin, M., G. Hagler , R. Baldauf , V. Isakov , and A. Khlystov. The Effects of Vegetation Barriers on Near-road Ultrafine Particle Number and Carbon Monoxide Concentrations.   SCIENCE OF THE TOTAL ENVIRONMENT. Elsevier BV, AMSTERDAM,  NETHERLANDS, 553: 372-379, (2016).",
             "distribution": [
                 {
-                    "title": "Hagler_SDMP_DataDictionary.docx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/218/Hagler_SDMP_DataDictionary.docx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+                    "title": "Hagler_SDMP_DataDictionary.docx"
                 },
                 {
-                    "title": "datasets.zip",
                     "downloadURL": "https://pasteur.epa.gov/uploads/218/datasets.zip",
-                    "mediaType": "application/x-zip-compressed"
+                    "mediaType": "application/x-zip-compressed",
+                    "title": "datasets.zip"
                 }
             ],
+            "identifier": "A-djhn-218",
+            "keyword": [
+                "near-road",
+                "vegetation",
+                "mitigation",
+                "air quality"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2016-08-22",
-            "references": [
-                "https://doi.org/10.1016/j.scitotenv.2016.02.035"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -40874,19 +40868,29 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.scitotenv.2016.02.035"
+            ],
+            "rights": null,
+            "title": " Near-road ultrafine particle and carbon monoxide measurements at North Carolina locations with and without roadside barriers"
         },
         {
-            "title": "Data Set for Characterization of nanoparticles in wood based consumer products",
-            "description": "The data include is for all of the tables and figures associated with the published journal article. \n\nThis dataset is associated with the following publication:\nPlatten, W., N. Sylvest, C. Warren, M. Arambewela, S. Harmon , K. Bradham, K. Rogers, T. Thomas, and T. Luxton. Estimating Dermal Exposure to Copper Nanoparticles from the Surfaces of Pressure-Treated Lumber and Implications for Toxicity.  D. Barcelo Culleres, and J. Gan  SCIENCE OF THE TOTAL ENVIRONMENT. Elsevier BV, AMSTERDAM,  NETHERLANDS, 548: 441-449, (2016).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:097"
+            "contactPoint": {
+                "fn": "Todd Luxton",
+                "hasEmail": "mailto:luxton.todd@epa.gov"
+            },
+            "description": "The data include is for all of the tables and figures associated with the published journal article. \n\nThis dataset is associated with the following publication:\nPlatten, W., N. Sylvest, C. Warren, M. Arambewela, S. Harmon , K. Bradham, K. Rogers, T. Thomas, and T. Luxton. Estimating Dermal Exposure to Copper Nanoparticles from the Surfaces of Pressure-Treated Lumber and Implications for Toxicity.  D. Barcelo Culleres, and J. Gan  SCIENCE OF THE TOTAL ENVIRONMENT. Elsevier BV, AMSTERDAM,  NETHERLANDS, 548: 441-449, (2016).",
+            "distribution": [
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/391/Data-Set.xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Data-Set.xlsx"
+                }
             ],
             "identifier": "A-8w9r-391",
             "keyword": [
@@ -40897,20 +40901,10 @@
                 "Ionic Copper",
                 "Copper Speciation"
             ],
-            "contactPoint": {
-                "fn": "Todd Luxton",
-                "hasEmail": "mailto:luxton.todd@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "Data-Set.xlsx",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/391/Data-Set.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2015-12-01",
-            "references": [
-                "https://doi.org/10.1016/j.scitotenv.2015.12.108"
+            "programCode": [
+                "020:097"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -40920,19 +40914,29 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.scitotenv.2015.12.108"
+            ],
+            "rights": null,
+            "title": "Data Set for Characterization of nanoparticles in wood based consumer products"
         },
         {
-            "title": "Influence of reservoir water-level fluctuations on mercury methylation downstream of the historic Black Butte mercury mine, OR.",
-            "description": "The data set contains the raw data used to develop the figures and tables associated with the published manuscript. \n\nThis dataset is associated with the following publication:\nEckley , C., T. Luxton , J. McKernan , J. Goetz , and J. Goulet. Influence of Reservoir Water-Level Fluctuations on Mercury Methylation Downstream of the Historic Black Butte Mercury Mine, OR.  Michael Kersten  APPLIED GEOCHEMISTRY. Elsevier Science Ltd, New York, NY, USA, 61: 284-293, (2015).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:097"
+            "contactPoint": {
+                "fn": "Todd Luxton",
+                "hasEmail": "mailto:luxton.todd@epa.gov"
+            },
+            "description": "The data set contains the raw data used to develop the figures and tables associated with the published manuscript. \n\nThis dataset is associated with the following publication:\nEckley , C., T. Luxton , J. McKernan , J. Goetz , and J. Goulet. Influence of Reservoir Water-Level Fluctuations on Mercury Methylation Downstream of the Historic Black Butte Mercury Mine, OR.  Michael Kersten  APPLIED GEOCHEMISTRY. Elsevier Science Ltd, New York, NY, USA, 61: 284-293, (2015).",
+            "distribution": [
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/408/Data-Set.xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Data-Set.xlsx"
+                }
             ],
             "identifier": "A-bp03-408",
             "keyword": [
@@ -40943,20 +40947,10 @@
                 "sediment",
                 "mining"
             ],
-            "contactPoint": {
-                "fn": "Todd Luxton",
-                "hasEmail": "mailto:luxton.todd@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "Data-Set.xlsx",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/408/Data-Set.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2014-10-21",
-            "references": [
-                "https://doi.org/10.1016/j.apgeochem.2015.06.011"
+            "programCode": [
+                "020:097"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -40966,40 +40960,42 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.apgeochem.2015.06.011"
+            ],
+            "rights": null,
+            "title": "Influence of reservoir water-level fluctuations on mercury methylation downstream of the historic Black Butte mercury mine, OR."
         },
         {
-            "title": "The evaluation of hollow-fiber ultrafiltration and celite concentration of enteroviruses, adenoviruses and bacteriophage from different water matrices",
-            "description": "The data to support the evaluation of hollow-fiber ultrafiltration and celite concentration of enteroviruses, adenoviruses and bacteriophage from different water matrices. \n\nThis dataset is associated with the following publication:\nRhodes , E., E. Huff, D. Hamilton, and J. Jones. The evaluation of hollow-fiber ultrafiltration and celite concentration of enteroviruses, adenoviruses and bacteriophage from different water matrices.   JOURNAL OF VIROLOGICAL METHODS. Elsevier Science Ltd, New York, NY, USA, 228(2): 31-38, (2016).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "A-cc2s-279",
-            "keyword": [
-                "Ultrafiltration",
-                "Viruses",
-                "Bacteriophage",
-                "Water Concentration"
-            ],
             "contactPoint": {
                 "fn": "Eric Rhodes",
                 "hasEmail": "mailto:rhodes.eric@epa.gov"
             },
+            "description": "The data to support the evaluation of hollow-fiber ultrafiltration and celite concentration of enteroviruses, adenoviruses and bacteriophage from different water matrices. \n\nThis dataset is associated with the following publication:\nRhodes , E., E. Huff, D. Hamilton, and J. Jones. The evaluation of hollow-fiber ultrafiltration and celite concentration of enteroviruses, adenoviruses and bacteriophage from different water matrices.   JOURNAL OF VIROLOGICAL METHODS. Elsevier Science Ltd, New York, NY, USA, 228(2): 31-38, (2016).",
             "distribution": [
                 {
-                    "title": "HFUF Virus Summary Table (1).xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/279/HFUF%20Virus%20Summary%20Table%20%281%29.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "HFUF Virus Summary Table (1).xlsx"
                 }
             ],
+            "identifier": "A-cc2s-279",
+            "keyword": [
+                "Ultrafiltration",
+                "Viruses",
+                "Bacteriophage",
+                "Water Concentration"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2015-06-01",
-            "references": null,
+            "programCode": [
+                "020:000"
+            ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
                 "subOrganizationOf": {
@@ -41008,46 +41004,44 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": null,
+            "rights": null,
+            "title": "The evaluation of hollow-fiber ultrafiltration and celite concentration of enteroviruses, adenoviruses and bacteriophage from different water matrices"
         },
         {
-            "title": "Complete Genome of Stachybotrys chartarum strain 51-11",
-            "description": "Complete genome sequence of the fungus Stachybotrys chartarum.  Sequences can be used to identify genes, genetic pathways, gene clusters, genetic organization, etc. utilizing appropriate bioinformatics software. \n\nThis dataset is associated with the following publication:\nBetancourt , D., T. Dean , J. Kim, and J. Levy. Genome sequence of Stachybotrys chartarum Strain 51-11.   Genome Announcements. American Society for Microbiology, Washington, DC, USA, 3(6): 1114-1115, (2015).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "A-jq2s-68",
-            "keyword": [
-                "stachybotrys chartarum",
-                "complete genome",
-                "fungi",
-                "genome",
-                "indoor biocontaminants"
-            ],
             "contactPoint": {
                 "fn": "Timothy Dean",
                 "hasEmail": "mailto:dean.timothy@epa.gov"
             },
+            "description": "Complete genome sequence of the fungus Stachybotrys chartarum.  Sequences can be used to identify genes, genetic pathways, gene clusters, genetic organization, etc. utilizing appropriate bioinformatics software. \n\nThis dataset is associated with the following publication:\nBetancourt , D., T. Dean , J. Kim, and J. Levy. Genome sequence of Stachybotrys chartarum Strain 51-11.   Genome Announcements. American Society for Microbiology, Washington, DC, USA, 3(6): 1114-1115, (2015).",
             "distribution": [
                 {
-                    "title": "Schartarum5111_hybrid_illumina_pacbio.fasta.zip",
                     "downloadURL": "https://pasteur.epa.gov/uploads/68/Schartarum5111_hybrid_illumina_pacbio.fasta.zip",
-                    "mediaType": "application/x-zip-compressed"
+                    "mediaType": "application/x-zip-compressed",
+                    "title": "Schartarum5111_hybrid_illumina_pacbio.fasta.zip"
                 },
                 {
-                    "title": "https://www.ncbi.nlm.nih.gov/Traces/wgs/wgsviewer.cgi?val=LDEE01&search=LDEE01000000&display=contigs",
-                    "accessURL": "https://www.ncbi.nlm.nih.gov/Traces/wgs/wgsviewer.cgi?val=LDEE01&search=LDEE01000000&display=contigs"
+                    "accessURL": "https://www.ncbi.nlm.nih.gov/Traces/wgs/wgsviewer.cgi?val=LDEE01&search=LDEE01000000&display=contigs",
+                    "title": "https://www.ncbi.nlm.nih.gov/Traces/wgs/wgsviewer.cgi?val=LDEE01&search=LDEE01000000&display=contigs"
                 }
             ],
+            "identifier": "A-jq2s-68",
+            "keyword": [
+                "stachybotrys chartarum",
+                "complete genome",
+                "fungi",
+                "genome",
+                "indoor biocontaminants"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2015-10-01",
-            "references": [
-                "https://doi.org/10.1128/genomea.01114-15"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -41057,19 +41051,29 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1128/genomea.01114-15"
+            ],
+            "rights": null,
+            "title": "Complete Genome of Stachybotrys chartarum strain 51-11"
         },
         {
-            "title": "Raw data used to generate figures 2 through 6 in Biological Responses of Raw 264.7 Macrophage Exposed to Two Strains of Stachybotrys chartarum Spores Grown on Four Different Wallboard Types manuscript.",
-            "description": "Excel files containing raw data used to generate figures throughout manuscript. \n\nThis dataset is associated with the following publication:\nDean , T., D. Betancourt , J. Kim, L. Harvey, A. Evans, and B. Grace. Biological Responses of Raw 264.7 Macrophage Exposed to Two Strains of Stachybotrys chartarum Spores Grown on Four Different Wallboard Types.   INHALATION TOXICOLOGY. Taylor & Francis, Inc., Philadelphia, PA, USA, 28(7): 303-307, (2016).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
+            "contactPoint": {
+                "fn": "Timothy Dean",
+                "hasEmail": "mailto:dean.timothy@epa.gov"
+            },
+            "description": "Excel files containing raw data used to generate figures throughout manuscript. \n\nThis dataset is associated with the following publication:\nDean , T., D. Betancourt , J. Kim, L. Harvey, A. Evans, and B. Grace. Biological Responses of Raw 264.7 Macrophage Exposed to Two Strains of Stachybotrys chartarum Spores Grown on Four Different Wallboard Types.   INHALATION TOXICOLOGY. Taylor & Francis, Inc., Philadelphia, PA, USA, 28(7): 303-307, (2016).",
+            "distribution": [
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/74/Biological%20Response%20Raw%20Data%20in%20Excel%20format.xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Biological Response Raw Data in Excel format.xlsx"
+                }
             ],
             "identifier": "A-8w9q-74",
             "keyword": [
@@ -41083,20 +41087,10 @@
                 "toxicity",
                 "wallboard"
             ],
-            "contactPoint": {
-                "fn": "Timothy Dean",
-                "hasEmail": "mailto:dean.timothy@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "Biological Response Raw Data in Excel format.xlsx",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/74/Biological%20Response%20Raw%20Data%20in%20Excel%20format.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2016-03-13",
-            "references": [
-                "https://doi.org/10.3109/08958378.2016.1170909"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -41106,49 +41100,49 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.3109/08958378.2016.1170909"
+            ],
+            "rights": null,
+            "title": "Raw data used to generate figures 2 through 6 in Biological Responses of Raw 264.7 Macrophage Exposed to Two Strains of Stachybotrys chartarum Spores Grown on Four Different Wallboard Types manuscript."
         },
         {
-            "title": "Water quality modeling in the dead end sections of drinking water (Supplement)",
-            "description": "Dead-end sections of drinking water distribution networks are known to be problematic zones in terms of water quality degradation. Extended residence time due to water stagnation leads to rapid reduction of disinfectant residuals allowing the regrowth of microbial pathogens. Water quality models developed so far apply spatial aggregation and temporal averaging techniques for hydraulic parameters by assigning hourly averaged water demands to the main nodes of the network. Although this practice has generally resulted in minimal loss of accuracy for the predicted disinfectant concentrations in main water transmission lines, this is not the case for the peripheries of the distribution network. This study proposes a new approach for simulating disinfectant residuals in dead end pipes while accounting for both spatial and temporal variability in hydraulic and transport parameters. A stochastic demand generator was developed to represent residential water pulses based on a non-homogenous Poisson process. Dispersive solute transport was considered using highly dynamic dispersion rates. A genetic algorithm was used to\ncalibrate the axial hydraulic profile of the dead-end pipe based on the different demand shares of the withdrawal nodes. A parametric sensitivity analysis was done to assess the model performance under variation of different simulation parameters. A group of Monte-Carlo ensembles was carried out to investigate the influence of spatial and temporal variations in flow demands on the simulation accuracy.\nA set of three correction factors were analytically derived to adjust residence time, dispersion rate and wall demand to overcome simulation error caused by spatial aggregation approximation. The current model results show better agreement with field-measured concentrations of conservative fluoride tracer and free chlorine disinfectant than the simulations of recent advection dispersion reaction models\npublished in the literature. Accuracy of the simulated concentration profiles showed significant dependence on the spatial distribution of the flow demands compared to temporal variation. \n\nThis dataset is associated with the following publication:\nAbokifa, A., J. Yang , C. Lo, and P. Biswas. Water Quality Modeling in the Dead End Sections of Drinking Water Distribution Networks.   WATER RESEARCH. Elsevier Science Ltd, New York, NY, USA, 18(89): 107-117, (2015).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "A-h9wf-367",
-            "keyword": [
-                "Chlorine",
-                "Dead end pipe",
-                "Advection dispersion",
-                "Genetic algorithm",
-                "Stochastic demands",
-                "Spatial distribution",
-                "Correction factors"
-            ],
             "contactPoint": {
                 "fn": "Yingping Yang",
                 "hasEmail": "mailto:yang.jeff@epa.gov"
             },
+            "description": "Dead-end sections of drinking water distribution networks are known to be problematic zones in terms of water quality degradation. Extended residence time due to water stagnation leads to rapid reduction of disinfectant residuals allowing the regrowth of microbial pathogens. Water quality models developed so far apply spatial aggregation and temporal averaging techniques for hydraulic parameters by assigning hourly averaged water demands to the main nodes of the network. Although this practice has generally resulted in minimal loss of accuracy for the predicted disinfectant concentrations in main water transmission lines, this is not the case for the peripheries of the distribution network. This study proposes a new approach for simulating disinfectant residuals in dead end pipes while accounting for both spatial and temporal variability in hydraulic and transport parameters. A stochastic demand generator was developed to represent residential water pulses based on a non-homogenous Poisson process. Dispersive solute transport was considered using highly dynamic dispersion rates. A genetic algorithm was used to\ncalibrate the axial hydraulic profile of the dead-end pipe based on the different demand shares of the withdrawal nodes. A parametric sensitivity analysis was done to assess the model performance under variation of different simulation parameters. A group of Monte-Carlo ensembles was carried out to investigate the influence of spatial and temporal variations in flow demands on the simulation accuracy.\nA set of three correction factors were analytically derived to adjust residence time, dispersion rate and wall demand to overcome simulation error caused by spatial aggregation approximation. The current model results show better agreement with field-measured concentrations of conservative fluoride tracer and free chlorine disinfectant than the simulations of recent advection dispersion reaction models\npublished in the literature. Accuracy of the simulated concentration profiles showed significant dependence on the spatial distribution of the flow demands compared to temporal variation. \n\nThis dataset is associated with the following publication:\nAbokifa, A., J. Yang , C. Lo, and P. Biswas. Water Quality Modeling in the Dead End Sections of Drinking Water Distribution Networks.   WATER RESEARCH. Elsevier Science Ltd, New York, NY, USA, 18(89): 107-117, (2015).",
             "distribution": [
                 {
-                    "title": "Supplementary Material_Final_YangYingping_A-h9wf_20160921.docx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/367/Supplementary%20Material_Final_YangYingping_A-h9wf_20160921.docx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+                    "title": "Supplementary Material_Final_YangYingping_A-h9wf_20160921.docx"
                 },
                 {
-                    "title": "Abokifa et al (16) Deadend model.pdf",
                     "downloadURL": "https://pasteur.epa.gov/uploads/367/Abokifa%20et%20al%20%2816%29%20Deadend%20model.pdf",
-                    "mediaType": "application/pdf"
+                    "mediaType": "application/pdf",
+                    "title": "Abokifa et al (16) Deadend model.pdf"
                 }
             ],
+            "identifier": "A-h9wf-367",
+            "keyword": [
+                "Chlorine",
+                "Dead end pipe",
+                "Advection dispersion",
+                "Genetic algorithm",
+                "Stochastic demands",
+                "Spatial distribution",
+                "Correction factors"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2015-12-14",
-            "references": [
-                "https://www.researchgate.net/publication/284233815_Water_Quality_Modeling_in_the_Dead_End_Sections_of_Drinking_Water_Distribution_Networks"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -41158,39 +41152,39 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://www.researchgate.net/publication/284233815_Water_Quality_Modeling_in_the_Dead_End_Sections_of_Drinking_Water_Distribution_Networks"
+            ],
+            "rights": null,
+            "title": "Water quality modeling in the dead end sections of drinking water (Supplement)"
         },
         {
-            "title": " Metabolic and genomic analysis elucidates strain-level variation in Microbacterium spp. isolated from chromate contaminated sediment",
-            "description": "The data is in the form of genomic sequences deposited in a public database, growth curves, and bioinformatic analysis of sequences. \n\nThis dataset is associated with the following publication:\nHenson, M., J. Santodomingo , P. Kourtev, R. Jensen, and D. Learman. Metabolic and genomic analysis elucidates strain-level variation in Microbacterium spp. isolated from chromate contaminated sediment.   PeerJ. PeerJ Inc., Corte Madera, CA, USA,  e1395, (2015).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "A-80gk-394",
-            "keyword": [
-                "heavy metal",
-                "genomics"
-            ],
             "contactPoint": {
                 "fn": "Jorge Santo Domingo",
                 "hasEmail": "mailto:santodomingo.jorge@epa.gov"
             },
+            "description": "The data is in the form of genomic sequences deposited in a public database, growth curves, and bioinformatic analysis of sequences. \n\nThis dataset is associated with the following publication:\nHenson, M., J. Santodomingo , P. Kourtev, R. Jensen, and D. Learman. Metabolic and genomic analysis elucidates strain-level variation in Microbacterium spp. isolated from chromate contaminated sediment.   PeerJ. PeerJ Inc., Corte Madera, CA, USA,  e1395, (2015).",
             "distribution": [
                 {
-                    "title": "Henson et al dataset.docx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/394/Henson%20et%20al%20dataset.docx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+                    "title": "Henson et al dataset.docx"
                 }
             ],
+            "identifier": "A-80gk-394",
+            "keyword": [
+                "heavy metal",
+                "genomics"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2015-04-01",
-            "references": [
-                "https://doi.org/10.7717/peerj.1395"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -41200,41 +41194,43 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.7717/peerj.1395"
+            ],
+            "rights": null,
+            "title": " Metabolic and genomic analysis elucidates strain-level variation in Microbacterium spp. isolated from chromate contaminated sediment"
         },
         {
-            "title": "Phosphate adsorption using modified iron oxide-based sorbents",
-            "description": "Phosphate Removal. \n\nThis dataset is associated with the following publication:\nLalley , J., C. Han , G. RamMohan , T. Speth , J. Garland , M. Nadagouda , and D. Dionysiou. Phosphate Removal using Modified Bayoxide\u00aeE33 Adsorption Media.   WATER RESEARCH. Elsevier Science Ltd, New York, NY, USA, issue}: 96-107, (2015).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:096"
-            ],
-            "identifier": "A-51cb-351",
-            "keyword": [
-                "Phosphate Removal",
-                "nutrients",
-                "adsorption",
-                "Nutrient removal/recovery"
-            ],
             "contactPoint": {
                 "fn": "Mallikarjuna Nadagouda",
                 "hasEmail": "mailto:nadagouda.mallikarjuna@epa.gov"
             },
+            "describedBy": "https://pasteur.epa.gov/uploads/351/documents/Supplemental.docx",
+            "describedByType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+            "description": "Phosphate Removal. \n\nThis dataset is associated with the following publication:\nLalley , J., C. Han , G. RamMohan , T. Speth , J. Garland , M. Nadagouda , and D. Dionysiou. Phosphate Removal using Modified Bayoxide\u00aeE33 Adsorption Media.   WATER RESEARCH. Elsevier Science Ltd, New York, NY, USA, issue}: 96-107, (2015).",
             "distribution": [
                 {
-                    "title": "Supplemental.docx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/351/Supplemental.docx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+                    "title": "Supplemental.docx"
                 }
             ],
+            "identifier": "A-51cb-351",
+            "keyword": [
+                "Phosphate Removal",
+                "nutrients",
+                "adsorption",
+                "Nutrient removal/recovery"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2016-09-19",
-            "references": [
-                "http://pubs.rsc.org/en/Content/ArticleLanding/2015/EW/c4ew00020j#divAbstract"
+            "programCode": [
+                "020:096"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -41245,41 +41241,39 @@
                     }
                 }
             },
-            "describedBy": "https://pasteur.epa.gov/uploads/351/documents/Supplemental.docx",
-            "describedByType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
+            "references": [
+                "http://pubs.rsc.org/en/Content/ArticleLanding/2015/EW/c4ew00020j#divAbstract"
+            ],
+            "rights": null,
+            "title": "Phosphate adsorption using modified iron oxide-based sorbents"
         },
         {
-            "title": " Measuring nitrification inhibition in wastewater treatment systems: current state of science and fundamental research needs",
-            "description": "There is no data as no experiments were conducted (literature review). \n\nThis dataset is associated with the following publication:\nLi , X., V. Kapoor , C. Impellitteri , and K. Chandran. Measuring nitrification inhibition in wastewater treatment systems: current state of science and fundamental research needs.   CRITICAL REVIEWS IN ENVIRONMENTAL SCIENCE AND TECHNOLOGY. CRC Press LLC, Boca Raton, FL, USA, 46(3): 249-289, (2016).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "A-79cw-397",
-            "keyword": [
-                "nitrification inhibition",
-                "nitrification",
-                "sequence"
-            ],
             "contactPoint": {
                 "fn": "Jorge Santo Domingo",
                 "hasEmail": "mailto:santodomingo.jorge@epa.gov"
             },
+            "description": "There is no data as no experiments were conducted (literature review). \n\nThis dataset is associated with the following publication:\nLi , X., V. Kapoor , C. Impellitteri , and K. Chandran. Measuring nitrification inhibition in wastewater treatment systems: current state of science and fundamental research needs.   CRITICAL REVIEWS IN ENVIRONMENTAL SCIENCE AND TECHNOLOGY. CRC Press LLC, Boca Raton, FL, USA, 46(3): 249-289, (2016).",
             "distribution": [
                 {
-                    "title": "Li et al dataset.docx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/397/Li%20et%20al%20dataset.docx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+                    "title": "Li et al dataset.docx"
                 }
             ],
+            "identifier": "A-79cw-397",
+            "keyword": [
+                "nitrification inhibition",
+                "nitrification",
+                "sequence"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2016-09-01",
-            "references": [
-                "https://doi.org/10.1080/10643389.2015.1085234"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -41289,19 +41283,28 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1080/10643389.2015.1085234"
+            ],
+            "rights": null,
+            "title": " Measuring nitrification inhibition in wastewater treatment systems: current state of science and fundamental research needs"
         },
         {
-            "title": "NLCD 2011 database",
-            "description": "National Land Cover Database 2011 (NLCD 2011) is the most recent national land cover product created by the Multi-Resolution Land Characteristics (MRLC) Consortium. NLCD 2011 provides - for the first time - the capability to assess wall-to-wall, spatially explicit, national land cover changes and trends across the United States from 2001 to 2011. As with two previous NLCD land cover products NLCD 2011 keeps the same 16-class land cover classification scheme that has been applied consistently across the United States at a spatial resolution of 30 meters. NLCD 2011 is based primarily on a decision-tree classification of circa 2011 Landsat satellite data. \n\nThis dataset is associated with the following publication:\nHomer, C., J. Dewitz, L. Yang, S. Jin, P. Danielson, G. Xian, J. Coulston, N. Herold, J. Wickham , and K. Megown. Completion of the 2011 National Land Cover Database for the Conterminous United States \u2013 Representing a Decade of Land Cover Change Information.   PHOTOGRAMMETRIC ENGINEERING AND REMOTE SENSING. American Society for Photogrammetry and Remote Sensing, Bethesda, MD, USA, 81(0): 345-354, (2015).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:097"
+            "contactPoint": {
+                "fn": "James Wickham",
+                "hasEmail": "mailto:wickham.james@epa.gov"
+            },
+            "description": "National Land Cover Database 2011 (NLCD 2011) is the most recent national land cover product created by the Multi-Resolution Land Characteristics (MRLC) Consortium. NLCD 2011 provides - for the first time - the capability to assess wall-to-wall, spatially explicit, national land cover changes and trends across the United States from 2001 to 2011. As with two previous NLCD land cover products NLCD 2011 keeps the same 16-class land cover classification scheme that has been applied consistently across the United States at a spatial resolution of 30 meters. NLCD 2011 is based primarily on a decision-tree classification of circa 2011 Landsat satellite data. \n\nThis dataset is associated with the following publication:\nHomer, C., J. Dewitz, L. Yang, S. Jin, P. Danielson, G. Xian, J. Coulston, N. Herold, J. Wickham , and K. Megown. Completion of the 2011 National Land Cover Database for the Conterminous United States \u2013 Representing a Decade of Land Cover Change Information.   PHOTOGRAMMETRIC ENGINEERING AND REMOTE SENSING. American Society for Photogrammetry and Remote Sensing, Bethesda, MD, USA, 81(0): 345-354, (2015).",
+            "distribution": [
+                {
+                    "accessURL": "https://www.mrlc.gov/data",
+                    "title": "https://www.mrlc.gov/data"
+                }
             ],
             "identifier": "A-3txd-118",
             "keyword": [
@@ -41315,18 +41318,11 @@
                 "snow-cover albedo",
                 "snow-free albedo"
             ],
-            "contactPoint": {
-                "fn": "James Wickham",
-                "hasEmail": "mailto:wickham.james@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "https://www.mrlc.gov/data",
-                    "accessURL": "https://www.mrlc.gov/data"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2014-10-10",
-            "references": null,
+            "programCode": [
+                "020:097"
+            ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
                 "subOrganizationOf": {
@@ -41335,19 +41331,27 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": null,
+            "rights": null,
+            "title": "NLCD 2011 database"
         },
         {
-            "title": "NLCD - MODIS land cover- albedo dataset for the continental United States",
-            "description": "The NLCD-MODIS land cover-albedo database integrates high-quality MODIS albedo observations with areas of homogeneous land cover from NLCD. The spatial resolution (pixel size) of the database is 480m-x-480m aligned to the standardized UGSG Albers Equal-Area projection. The spatial extent of the database is the continental United States. \n\nThis dataset is associated with the following publication:\nWickham , J., C.A. Barnes, and T. Wade. Combining NLCD and MODIS to Create a Land Cover-Albedo Dataset for the Continental United States.   REMOTE SENSING OF ENVIRONMENT. Elsevier Science Ltd, New York, NY, USA, 170(0): 143-153, (2015).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:097"
+            "contactPoint": {
+                "fn": "James Wickham",
+                "hasEmail": "mailto:wickham.james@epa.gov"
+            },
+            "describedBy": "https://www.mrlc.gov/nlcdalbedo.php",
+            "description": "The NLCD-MODIS land cover-albedo database integrates high-quality MODIS albedo observations with areas of homogeneous land cover from NLCD. The spatial resolution (pixel size) of the database is 480m-x-480m aligned to the standardized UGSG Albers Equal-Area projection. The spatial extent of the database is the continental United States. \n\nThis dataset is associated with the following publication:\nWickham , J., C.A. Barnes, and T. Wade. Combining NLCD and MODIS to Create a Land Cover-Albedo Dataset for the Continental United States.   REMOTE SENSING OF ENVIRONMENT. Elsevier Science Ltd, New York, NY, USA, 170(0): 143-153, (2015).",
+            "distribution": [
+                {
+                    "accessURL": "https://www.mrlc.gov/data",
+                    "title": "https://www.mrlc.gov/data"
+                }
             ],
             "identifier": "A-3txd-117",
             "keyword": [
@@ -41358,18 +41362,11 @@
                 "snow-cover albedo",
                 "snow-free albedo"
             ],
-            "contactPoint": {
-                "fn": "James Wickham",
-                "hasEmail": "mailto:wickham.james@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "https://www.mrlc.gov/data",
-                    "accessURL": "https://www.mrlc.gov/data"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2015-11-03",
-            "references": null,
+            "programCode": [
+                "020:097"
+            ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
                 "subOrganizationOf": {
@@ -41379,19 +41376,25 @@
                     }
                 }
             },
-            "describedBy": "https://www.mrlc.gov/nlcdalbedo.php"
+            "references": null,
+            "rights": null,
+            "title": "NLCD - MODIS land cover- albedo dataset for the continental United States"
         },
         {
-            "title": "Systematically evaluating read-across prediction and performance using a local validity approach characterized by chemical structure and bioactivity information",
-            "description": "Read-across is a popular data gap filling technique within category and analogue approaches for regulatory purposes. Acceptance of read-across remains an ongoing challenge with several efforts underway for identifying and addressing uncertainties. Here we demonstrate an algorithmic, automated approach to evaluate the utility of using in vitro bioactivity data (\u201cbioactivity descriptors\u201d, from EPA\u2019s ToxCast program) in conjunction with chemical descriptor information to derive local validity domains (specific sets of nearest neighbors) to facilitate read-across for a number of in vivo repeated dose toxicity study types. Over 3400 different chemical structure descriptors were generated for a set of 976 chemicals and supplemented with the outcomes from 821 in vitro assays. The read-across prediction for a given chemical was based on the similarity weighted endpoint outcomes of its nearest neighbors. The approach enabled a performance baseline for read-across predictions of specific study outcomes to be established. Bioactivity descriptors were often found to be more predictive of in vivo toxicity outcomes than chemical descriptors or a combination of both. This generic read across (GenRA) is intended to form a first step in systemizing read-across prediction and serves as a useful tool as part of a screening level hazard assessment for new untested chemicals. \n\nThis dataset is associated with the following publication:\nShah , I., J. Liu , R.S. Judson , R.S. Thomas , and G. Patlewicz. (Reg. Tox. Pharm.) Systematically evaluating read-across prediction and performance using a local validity approach characterized by chemical structure and bioactivity information.   REGULATORY TOXICOLOGY AND PHARMACOLOGY. Elsevier Science Ltd, New York, NY, USA, 79: 12-24, (2016).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:095"
+            "contactPoint": {
+                "fn": "Ann Richard",
+                "hasEmail": "mailto:richard.ann@epa.gov"
+            },
+            "description": "Read-across is a popular data gap filling technique within category and analogue approaches for regulatory purposes. Acceptance of read-across remains an ongoing challenge with several efforts underway for identifying and addressing uncertainties. Here we demonstrate an algorithmic, automated approach to evaluate the utility of using in vitro bioactivity data (\u201cbioactivity descriptors\u201d, from EPA\u2019s ToxCast program) in conjunction with chemical descriptor information to derive local validity domains (specific sets of nearest neighbors) to facilitate read-across for a number of in vivo repeated dose toxicity study types. Over 3400 different chemical structure descriptors were generated for a set of 976 chemicals and supplemented with the outcomes from 821 in vitro assays. The read-across prediction for a given chemical was based on the similarity weighted endpoint outcomes of its nearest neighbors. The approach enabled a performance baseline for read-across predictions of specific study outcomes to be established. Bioactivity descriptors were often found to be more predictive of in vivo toxicity outcomes than chemical descriptors or a combination of both. This generic read across (GenRA) is intended to form a first step in systemizing read-across prediction and serves as a useful tool as part of a screening level hazard assessment for new untested chemicals. \n\nThis dataset is associated with the following publication:\nShah , I., J. Liu , R.S. Judson , R.S. Thomas , and G. Patlewicz. (Reg. Tox. Pharm.) Systematically evaluating read-across prediction and performance using a local validity approach characterized by chemical structure and bioactivity information.   REGULATORY TOXICOLOGY AND PHARMACOLOGY. Elsevier Science Ltd, New York, NY, USA, 79: 12-24, (2016).",
+            "distribution": [
+                {
+                    "accessURL": "https://gaftp.epa.gov/Comptox/NCCT_Publication_Data/ShahImran/Read_Across/",
+                    "title": "https://gaftp.epa.gov/Comptox/NCCT_Publication_Data/ShahImran/Read_Across/"
+                }
             ],
             "identifier": "A-6t1n-421",
             "keyword": [
@@ -41405,19 +41408,10 @@
                 "Chemistry Dashboard",
                 "Read Across"
             ],
-            "contactPoint": {
-                "fn": "Ann Richard",
-                "hasEmail": "mailto:richard.ann@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "https://gaftp.epa.gov/Comptox/NCCT_Publication_Data/ShahImran/Read_Across/",
-                    "accessURL": "https://gaftp.epa.gov/Comptox/NCCT_Publication_Data/ShahImran/Read_Across/"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2015-09-09",
-            "references": [
-                "https://doi.org/10.1016/j.yrtph.2016.05.008"
+            "programCode": [
+                "020:095"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -41427,19 +41421,28 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.yrtph.2016.05.008"
+            ],
+            "rights": null,
+            "title": "Systematically evaluating read-across prediction and performance using a local validity approach characterized by chemical structure and bioactivity information"
         },
         {
-            "title": "Analysis of the Effects of Cell Stress and Cytotoxicity on In Vitro Assay Activity Across a Diverse Chemical and Assay Space",
-            "description": "Chemical toxicity can arise from disruption of specific biomolecular functions or through more generalized cell stress and cytotoxicity-mediated processes. Here, concentration-dependent responses of 1063 chemicals including pharmaceuticals, natural products, pesticidals, consumer, and industrial chemicals across a diverse battery of 821 in vitro assay endpoints from 7 high-throughput assay technology platforms were analyzed in order to better distinguish between these types of activities. Both cell-based and cell-free assays showed a rapid increase in the frequency of responses at concentrations where cell stress / cytotoxicity responses were observed in cell-based assays. Chemicals that were positive on at least two viability/cytotoxicity assays within the concentration range tested (typically up to 100 \uf06dM) activated a median of 12% of assay endpoints while those that were not cytotoxic in this concentration range activated 1.3% of the assays endpoints. The results suggest that activity can be broadly divided into: (1) specific biomolecular interactions against one or more targets (e.g., receptors or enzymes) at concentrations below which overt cytotoxicity-associated activity is observed; and (2) activity associated with cell stress or cytotoxicity, which may result from triggering of specific cell stress pathways, chemical reactivity, physico-chemical disruption of proteins or membranes, or broad low-affinity non-covalent interactions. Chemicals showing a greater number of specific biomolecular interactions are generally designed to be bioactive (pharmaceuticals or pesticidal active ingredients), while intentional food-use chemicals tended to show the fewest specific interactions. The analyses presented here provide context for use of these data in ongoing studies to predict in vivo toxicity from chemicals lacking extensive hazard assessment. \n\nThis dataset is associated with the following publication:\nJudson , R., K. Houck , M. Martin , A. Richard , T. Knudsen , I. Shah , S. Little , J. Wambaugh , W. Setzer , P. Kothiya , J. Phuong , D. Filer , D. Smith , D. Reif, D. Rotroff, N. Kleinstreuer, N. Sipes, M. Xia, R. Huang, K. Crofton , and R. Thomas. (Toxicological Sciences) Analysis of the Effects of Cell Stress and Cytotoxicity on In Vitro Assay Activity Across a Diverse Chemical and Assay Space.   TOXICOLOGICAL SCIENCES. Society of Toxicology,     1-47, (2016).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:095"
+            "contactPoint": {
+                "fn": "Keith Houck",
+                "hasEmail": "mailto:houck.keith@epa.gov"
+            },
+            "description": "Chemical toxicity can arise from disruption of specific biomolecular functions or through more generalized cell stress and cytotoxicity-mediated processes. Here, concentration-dependent responses of 1063 chemicals including pharmaceuticals, natural products, pesticidals, consumer, and industrial chemicals across a diverse battery of 821 in vitro assay endpoints from 7 high-throughput assay technology platforms were analyzed in order to better distinguish between these types of activities. Both cell-based and cell-free assays showed a rapid increase in the frequency of responses at concentrations where cell stress / cytotoxicity responses were observed in cell-based assays. Chemicals that were positive on at least two viability/cytotoxicity assays within the concentration range tested (typically up to 100 \uf06dM) activated a median of 12% of assay endpoints while those that were not cytotoxic in this concentration range activated 1.3% of the assays endpoints. The results suggest that activity can be broadly divided into: (1) specific biomolecular interactions against one or more targets (e.g., receptors or enzymes) at concentrations below which overt cytotoxicity-associated activity is observed; and (2) activity associated with cell stress or cytotoxicity, which may result from triggering of specific cell stress pathways, chemical reactivity, physico-chemical disruption of proteins or membranes, or broad low-affinity non-covalent interactions. Chemicals showing a greater number of specific biomolecular interactions are generally designed to be bioactive (pharmaceuticals or pesticidal active ingredients), while intentional food-use chemicals tended to show the fewest specific interactions. The analyses presented here provide context for use of these data in ongoing studies to predict in vivo toxicity from chemicals lacking extensive hazard assessment. \n\nThis dataset is associated with the following publication:\nJudson , R., K. Houck , M. Martin , A. Richard , T. Knudsen , I. Shah , S. Little , J. Wambaugh , W. Setzer , P. Kothiya , J. Phuong , D. Filer , D. Smith , D. Reif, D. Rotroff, N. Kleinstreuer, N. Sipes, M. Xia, R. Huang, K. Crofton , and R. Thomas. (Toxicological Sciences) Analysis of the Effects of Cell Stress and Cytotoxicity on In Vitro Assay Activity Across a Diverse Chemical and Assay Space.   TOXICOLOGICAL SCIENCES. Society of Toxicology,     1-47, (2016).",
+            "distribution": [
+                {
+                    "accessURL": "https://gaftp.epa.gov/COMPTOX/NCCT_Publication_Data/Judson/CytotoxBurst",
+                    "title": "https://gaftp.epa.gov/COMPTOX/NCCT_Publication_Data/Judson/CytotoxBurst"
+                }
             ],
             "identifier": "A-x0kx-419",
             "keyword": [
@@ -41450,19 +41453,10 @@
                 "ToxCast",
                 "computational toxicology"
             ],
-            "contactPoint": {
-                "fn": "Keith Houck",
-                "hasEmail": "mailto:houck.keith@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "https://gaftp.epa.gov/COMPTOX/NCCT_Publication_Data/Judson/CytotoxBurst",
-                    "accessURL": "https://gaftp.epa.gov/COMPTOX/NCCT_Publication_Data/Judson/CytotoxBurst"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2016-08-28",
-            "references": [
-                "https://doi.org/10.1093/toxsci/kfw092"
+            "programCode": [
+                "020:095"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -41472,40 +41466,40 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1093/toxsci/kfw092"
+            ],
+            "rights": null,
+            "title": "Analysis of the Effects of Cell Stress and Cytotoxicity on In Vitro Assay Activity Across a Diverse Chemical and Assay Space"
         },
         {
-            "title": "Is Skin penetration a determining factor in skin sensitisation potential and potency? Refuting the notion of a LogKow threshold for Skin Sensitisation",
-            "description": "t is widely accepted that substances that cannot penetrate through the skin will not be sensitizers. LogKow and molecular weight (MW) have been used to set thresholds for sensitization potential. Highly hydrophilic substances e.g. LogKow \u2264 1 are expected not to penetrate effectively to induce sensitization. To investigate whether LogKow >1 is a true requirement for sensitization, a large dataset of substances that had been evaluated for their skin sensitization potential under Registration, Evaluation, Authorisation and restriction of CHemicals (REACH), together with available measured LogKow values was compiled using the OECD eChemPortal. The incidence of sensitizers relative to non-sensitizers above and below a LogKow of 1 was explored. Reaction chemistry principles were used to explain the sensitization observed for the subset of substances with a LogKow \u22640. 1482 substances were identified with skin sensitization data and measured LogKow values. 525 substances had a measured LogKow \u2264 1, 100 of those were sensitizers. There was no significant difference in the incidence of sensitizers above and below a LogKow of 1. Reaction chemistry principles that had been established for lower MW and more hydrophobic substances were found to be still valid in rationalizing the skin sensitizers with a LogKow \u2264 0. The LogKow threshold arises from the widespread misconception that the ability to efficiently penetrate the stratum corneum is a key determinant of sensitization potential and potency. \n\nThis dataset is associated with the following publication:\nFitzpatrick, J., D. Roberts, and G. Patlewicz. (Journal of Applied Toxicology) Is skin penetration a determining factor in skin sensitisation potential and potency? Refuting the notion of a LogKow threshold for Skin Sensitisation.   JOURNAL OF APPLIED TOXICOLOGY. John Wiley & Sons, Ltd., Indianapolis, IN, USA,  1-11, (2016).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:095"
-            ],
-            "identifier": "A-6t1n-316",
-            "keyword": [
-                "skin sensitization",
-                "DSSTox",
-                "Chemistry Dashboard",
-                "Read Across"
-            ],
             "contactPoint": {
                 "fn": "Ann Richard",
                 "hasEmail": "mailto:richard.ann@epa.gov"
             },
+            "description": "t is widely accepted that substances that cannot penetrate through the skin will not be sensitizers. LogKow and molecular weight (MW) have been used to set thresholds for sensitization potential. Highly hydrophilic substances e.g. LogKow \u2264 1 are expected not to penetrate effectively to induce sensitization. To investigate whether LogKow >1 is a true requirement for sensitization, a large dataset of substances that had been evaluated for their skin sensitization potential under Registration, Evaluation, Authorisation and restriction of CHemicals (REACH), together with available measured LogKow values was compiled using the OECD eChemPortal. The incidence of sensitizers relative to non-sensitizers above and below a LogKow of 1 was explored. Reaction chemistry principles were used to explain the sensitization observed for the subset of substances with a LogKow \u22640. 1482 substances were identified with skin sensitization data and measured LogKow values. 525 substances had a measured LogKow \u2264 1, 100 of those were sensitizers. There was no significant difference in the incidence of sensitizers above and below a LogKow of 1. Reaction chemistry principles that had been established for lower MW and more hydrophobic substances were found to be still valid in rationalizing the skin sensitizers with a LogKow \u2264 0. The LogKow threshold arises from the widespread misconception that the ability to efficiently penetrate the stratum corneum is a key determinant of sensitization potential and potency. \n\nThis dataset is associated with the following publication:\nFitzpatrick, J., D. Roberts, and G. Patlewicz. (Journal of Applied Toxicology) Is skin penetration a determining factor in skin sensitisation potential and potency? Refuting the notion of a LogKow threshold for Skin Sensitisation.   JOURNAL OF APPLIED TOXICOLOGY. John Wiley & Sons, Ltd., Indianapolis, IN, USA,  1-11, (2016).",
             "distribution": [
                 {
-                    "title": "https://gaftp.epa.gov/COMPTOX/NCCT_Publication_Data/PatlewiczGrace/LOGKOW_Skin_Sensistization/",
-                    "accessURL": "https://gaftp.epa.gov/COMPTOX/NCCT_Publication_Data/PatlewiczGrace/LOGKOW_Skin_Sensistization/"
+                    "accessURL": "https://gaftp.epa.gov/COMPTOX/NCCT_Publication_Data/PatlewiczGrace/LOGKOW_Skin_Sensistization/",
+                    "title": "https://gaftp.epa.gov/COMPTOX/NCCT_Publication_Data/PatlewiczGrace/LOGKOW_Skin_Sensistization/"
                 }
             ],
+            "identifier": "A-6t1n-316",
+            "keyword": [
+                "skin sensitization",
+                "DSSTox",
+                "Chemistry Dashboard",
+                "Read Across"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2016-06-29",
-            "references": [
-                "https://doi.org/10.1002/jat.3354"
+            "programCode": [
+                "020:095"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -41515,42 +41509,44 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1002/jat.3354"
+            ],
+            "rights": null,
+            "title": "Is Skin penetration a determining factor in skin sensitisation potential and potency? Refuting the notion of a LogKow threshold for Skin Sensitisation"
         },
         {
-            "title": "Concentrations of individual fine particulate matter components in the United States around July 4th ",
-            "description": "Data used in these analyses was obtained from publically-available sources, specifically the EPA's AirNow website (https://www.epa.gov/outdoor-air-quality-data). The dataset provided includes the subset of data from AirNow that was used in our analyses. \n\nThis dataset is associated with the following publication:\nDickerson, A., A. Benson, B. Buckley, and E. Chan. Concentrations of individual fine particulate matter components in the United States around July 4th.   Air Quality, Atmosphere & Health. Springer Netherlands, NETHERLANDS,  1-10, (2016).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:062"
-            ],
-            "identifier": "A-qfvc-338",
-            "keyword": [
-                "air quality",
-                "Ambient air quality",
-                "Fireworks",
-                "air pollution",
-                "Fine Particulate Matter"
-            ],
             "contactPoint": {
                 "fn": "Elizabeth Chan",
                 "hasEmail": "mailto:chan.elizabeth@epa.gov"
             },
+            "describedBy": "https://pasteur.epa.gov/uploads/338/documents/Data%20Dictionary.docx",
+            "describedByType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+            "description": "Data used in these analyses was obtained from publically-available sources, specifically the EPA's AirNow website (https://www.epa.gov/outdoor-air-quality-data). The dataset provided includes the subset of data from AirNow that was used in our analyses. \n\nThis dataset is associated with the following publication:\nDickerson, A., A. Benson, B. Buckley, and E. Chan. Concentrations of individual fine particulate matter components in the United States around July 4th.   Air Quality, Atmosphere & Health. Springer Netherlands, NETHERLANDS,  1-10, (2016).",
             "distribution": [
                 {
-                    "title": "Raw speciation data.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/338/Raw%20speciation%20data.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Raw speciation data.xlsx"
                 }
             ],
+            "identifier": "A-qfvc-338",
+            "keyword": [
+                "air quality",
+                "Ambient air quality",
+                "Fireworks",
+                "air pollution",
+                "Fine Particulate Matter"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2016-08-16",
-            "references": [
-                "http://link.springer.com/article/10.1007/s11869-016-0433-0"
+            "programCode": [
+                "020:062"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -41561,20 +41557,27 @@
                     }
                 }
             },
-            "describedBy": "https://pasteur.epa.gov/uploads/338/documents/Data%20Dictionary.docx",
-            "describedByType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
+            "references": [
+                "http://link.springer.com/article/10.1007/s11869-016-0433-0"
+            ],
+            "rights": null,
+            "title": "Concentrations of individual fine particulate matter components in the United States around July 4th "
         },
         {
-            "title": "Coastal 2010: Site Information, Hydrographic Profile, Water Chemistry",
-            "description": "Data from the National Aquatic Resource Surveys:  \nThe following data are available for download as comma separated values (.csv) files. Sort the table using the pull down menus or headers to more easily locate the data. Right click on the file name and select Save Link As to save the file to your computer. Make sure to also download the companion metadata file (.txt) for the list of field labels. See the survey technical document for more information on the data analyses. \n\nThis dataset is associated with the following publications:\nYurista , P., J. Kelly , and J. Scharold. Great Lakes nearshore-offshore: Distinct water quality regions.   JOURNAL OF GREAT LAKES RESEARCH. International Association for Great Lakes Research, Ann Arbor, MI, USA, 42: 375-385, (2016).\nKelly , J., P. Yurista , M. Starry, J. Scharold , W. Bartsch , and A. Cotter. The first US National Coastal Condition Assessment survey in the Great Lakes: Development of the GIS frame and exploration of spatial variation in nearshore water quality results.   JOURNAL OF GREAT LAKES RESEARCH. International Association for Great Lakes Research, Ann Arbor, MI, USA, 41: 1060-1074, (2015).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:096"
+            "contactPoint": {
+                "fn": "Jill Scharold",
+                "hasEmail": "mailto:scharold.jill@epa.gov"
+            },
+            "description": "Data from the National Aquatic Resource Surveys:  \nThe following data are available for download as comma separated values (.csv) files. Sort the table using the pull down menus or headers to more easily locate the data. Right click on the file name and select Save Link As to save the file to your computer. Make sure to also download the companion metadata file (.txt) for the list of field labels. See the survey technical document for more information on the data analyses. \n\nThis dataset is associated with the following publications:\nYurista , P., J. Kelly , and J. Scharold. Great Lakes nearshore-offshore: Distinct water quality regions.   JOURNAL OF GREAT LAKES RESEARCH. International Association for Great Lakes Research, Ann Arbor, MI, USA, 42: 375-385, (2016).\nKelly , J., P. Yurista , M. Starry, J. Scharold , W. Bartsch , and A. Cotter. The first US National Coastal Condition Assessment survey in the Great Lakes: Development of the GIS frame and exploration of spatial variation in nearshore water quality results.   JOURNAL OF GREAT LAKES RESEARCH. International Association for Great Lakes Research, Ann Arbor, MI, USA, 41: 1060-1074, (2015).",
+            "distribution": [
+                {
+                    "accessURL": "https://www.epa.gov/national-aquatic-resource-surveys/data-national-aquatic-resource-surveys",
+                    "title": "https://www.epa.gov/national-aquatic-resource-surveys/data-national-aquatic-resource-surveys"
+                }
             ],
             "identifier": "A-98sq-382",
             "keyword": [
@@ -41584,20 +41587,10 @@
                 "National Coastal Condition Assessment",
                 "Great Lakes"
             ],
-            "contactPoint": {
-                "fn": "Jill Scharold",
-                "hasEmail": "mailto:scharold.jill@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "https://www.epa.gov/national-aquatic-resource-surveys/data-national-aquatic-resource-surveys",
-                    "accessURL": "https://www.epa.gov/national-aquatic-resource-surveys/data-national-aquatic-resource-surveys"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2016-09-09",
-            "references": [
-                "https://doi.org/10.1016/j.jglr.2015.12.002",
-                "https://doi.org/10.1016/j.jglr.2015.09.007"
+            "programCode": [
+                "020:096"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -41607,19 +41600,30 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.jglr.2015.12.002",
+                "https://doi.org/10.1016/j.jglr.2015.09.007"
+            ],
+            "rights": null,
+            "title": "Coastal 2010: Site Information, Hydrographic Profile, Water Chemistry"
         },
         {
-            "title": "EPA data for EMMA of Peatland Discharge to an Alaskan Stream Journal of Hydrology 2015",
-            "description": "This dataset contains primarily the EPA generated data for the EMMA (End-Member-Mixing Analysis) model that was presented in the associated J. of Hydrology (2015) publication.  Part of the data for the EMMA and all the data for the water budget  were not produced by EPA and were not included here.  EPA did the analyses for SO4, Cl, and K and these results are in this dataset.  An independent set of lab analysis was done by a non-EPA lab for K and this data is included as one quality control measure.  The field collections of the samples for all of the data were collected jointly between several EPA field scientists along with the non-EPA cooperative agreement principal investigator and primary author of the J. of Hydrology (2015) publication.  The site description data along with site locations are given in the dataset. \n\nThis dataset is associated with the following publication:\nGracz, M., M. Moffett , D. Siegel, and P. Glaser. Analyzing peatland discharge to streams in an Alaskan Watershed: An integration of end-member mixing analysis and a water balance approach.   JOURNAL OF HYDROLOGY. Elsevier Science Ltd, New York, NY, USA, 530: 667-676, (2015).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:096"
+            "contactPoint": {
+                "fn": "Mary Moffett",
+                "hasEmail": "mailto:moffett.mary@epa.gov"
+            },
+            "description": "This dataset contains primarily the EPA generated data for the EMMA (End-Member-Mixing Analysis) model that was presented in the associated J. of Hydrology (2015) publication.  Part of the data for the EMMA and all the data for the water budget  were not produced by EPA and were not included here.  EPA did the analyses for SO4, Cl, and K and these results are in this dataset.  An independent set of lab analysis was done by a non-EPA lab for K and this data is included as one quality control measure.  The field collections of the samples for all of the data were collected jointly between several EPA field scientists along with the non-EPA cooperative agreement principal investigator and primary author of the J. of Hydrology (2015) publication.  The site description data along with site locations are given in the dataset. \n\nThis dataset is associated with the following publication:\nGracz, M., M. Moffett , D. Siegel, and P. Glaser. Analyzing peatland discharge to streams in an Alaskan Watershed: An integration of end-member mixing analysis and a water balance approach.   JOURNAL OF HYDROLOGY. Elsevier Science Ltd, New York, NY, USA, 530: 667-676, (2015).",
+            "distribution": [
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/411/MoffettMary_A-8672_Dataset1_20160928_SciHub_JofHydrology2015.xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "MoffettMary_A-8672_Dataset1_20160928_SciHub_JofHydrology2015.xlsx"
+                }
             ],
             "identifier": "A-8672-411",
             "keyword": [
@@ -41638,20 +41642,10 @@
                 "Watershed",
                 "functional assessment"
             ],
-            "contactPoint": {
-                "fn": "Mary Moffett",
-                "hasEmail": "mailto:moffett.mary@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "MoffettMary_A-8672_Dataset1_20160928_SciHub_JofHydrology2015.xlsx",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/411/MoffettMary_A-8672_Dataset1_20160928_SciHub_JofHydrology2015.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2016-09-28",
-            "references": [
-                "https://doi.org/10.1016/j.jhydrol.2015.09.072"
+            "programCode": [
+                "020:096"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -41661,40 +41655,40 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.jhydrol.2015.09.072"
+            ],
+            "rights": null,
+            "title": "EPA data for EMMA of Peatland Discharge to an Alaskan Stream Journal of Hydrology 2015"
         },
         {
-            "title": "Data Sources for NetZero Ft Carson Model ",
-            "description": "Table of values used to parameterize and evaluate the Ft Carson NetZero integrated Model with published reference sources for each value. \n\nThis dataset is associated with the following publication:\nProcter, A., O. Kaplan , and R. Araujo. Net Zero Fort Carson: Integrating Energy, Water, and Waste Strategies to Lower the Environmental Impact of a Military Base.   JOURNAL OF INDUSTRIAL ECOLOGY. Berkeley Electronic Press, Berkeley, CA, USA,  online, (2015).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "A-573t-291",
-            "keyword": [
-                "NetZero",
-                "sustainability",
-                "systems modeling"
-            ],
             "contactPoint": {
                 "fn": "Rochelle Araujo",
                 "hasEmail": "mailto:araujo.rochelle@epa.gov"
             },
+            "description": "Table of values used to parameterize and evaluate the Ft Carson NetZero integrated Model with published reference sources for each value. \n\nThis dataset is associated with the following publication:\nProcter, A., O. Kaplan , and R. Araujo. Net Zero Fort Carson: Integrating Energy, Water, and Waste Strategies to Lower the Environmental Impact of a Military Base.   JOURNAL OF INDUSTRIAL ECOLOGY. Berkeley Electronic Press, Berkeley, CA, USA,  online, (2015).",
             "distribution": [
                 {
-                    "title": "Araujo SDM Data sources for NetZero Model 20160909.docx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/291/Araujo%20SDM%20Data%20sources%20for%20NetZero%20Model%2020160909.docx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+                    "title": "Araujo SDM Data sources for NetZero Model 20160909.docx"
                 }
             ],
+            "identifier": "A-573t-291",
+            "keyword": [
+                "NetZero",
+                "sustainability",
+                "systems modeling"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2015-10-15",
-            "references": [
-                "http://onlinelibrary.wiley.com/doi/10.1111/jiec.12359/abstract"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -41704,38 +41698,40 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "http://onlinelibrary.wiley.com/doi/10.1111/jiec.12359/abstract"
+            ],
+            "rights": null,
+            "title": "Data Sources for NetZero Ft Carson Model "
         },
         {
-            "title": "Data Fusion approach for spatial analysis of speciated PM2.5 across time",
-            "description": "speciated pm2.5 monitoring data and total pm2.5 monitoring data. \n\nThis dataset is associated with the following publication:\nRundel, C., E. Schliep, A. Gelfand, and D. Holland. A data fusion approach for spatial analysis of speciated PM2:5 across time.   Annals of Applied Statistics. Institute of Mathematical Statistics, Beachwood, OH, USA, 26(0): 515-526, (2015).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:094"
-            ],
-            "identifier": "A-70s4-214",
-            "keyword": [
-                "downscaling",
-                "speciated fine particulate matter"
-            ],
             "contactPoint": {
                 "fn": "David Holland",
                 "hasEmail": "mailto:holland.david@epa.gov"
             },
+            "description": "speciated pm2.5 monitoring data and total pm2.5 monitoring data. \n\nThis dataset is associated with the following publication:\nRundel, C., E. Schliep, A. Gelfand, and D. Holland. A data fusion approach for spatial analysis of speciated PM2:5 across time.   Annals of Applied Statistics. Institute of Mathematical Statistics, Beachwood, OH, USA, 26(0): 515-526, (2015).",
             "distribution": [
                 {
-                    "title": "paper_data.tar",
                     "downloadURL": "https://pasteur.epa.gov/uploads/214/paper_data.tar",
-                    "mediaType": "application/x-tar"
+                    "mediaType": "application/x-tar",
+                    "title": "paper_data.tar"
                 }
             ],
+            "identifier": "A-70s4-214",
+            "keyword": [
+                "downscaling",
+                "speciated fine particulate matter"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2016-09-14",
-            "references": null,
+            "programCode": [
+                "020:094"
+            ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
                 "subOrganizationOf": {
@@ -41744,19 +41740,27 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": null,
+            "rights": null,
+            "title": "Data Fusion approach for spatial analysis of speciated PM2.5 across time"
         },
         {
-            "title": "Mild Thyroid Hormone Insufficiency During Development Compromises Activity-Dependent Neuroplasticity in the Hippocampus of Adult Male Rats",
-            "description": "behavioral measures of learning and memory in adult offspring of rats treated with thyroid hormone synthesis inhibitor, propylthiouracil.\nElectrophysiological measures of 'memory' in form of plasticity model known as long term potentiation (LTP)\nMolecular changes induced by LTP. \n\nThis dataset is associated with the following publication:\nGilbert , M., K. Sanchez-Huerta, and C. Wood. Mild Thyroid Hormone Insufficiency During Development Compromises Activity-Dependent Neuroplasticity in the Hippocampus of Adult Make Rats.   ENDOCRINOLOGY. Endocrine Society,    157(2): 774-87, (2016).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
+            "contactPoint": {
+                "fn": "Mary Gilbert",
+                "hasEmail": "mailto:gilbert.mary@epa.gov"
+            },
+            "description": "behavioral measures of learning and memory in adult offspring of rats treated with thyroid hormone synthesis inhibitor, propylthiouracil.\nElectrophysiological measures of 'memory' in form of plasticity model known as long term potentiation (LTP)\nMolecular changes induced by LTP. \n\nThis dataset is associated with the following publication:\nGilbert , M., K. Sanchez-Huerta, and C. Wood. Mild Thyroid Hormone Insufficiency During Development Compromises Activity-Dependent Neuroplasticity in the Hippocampus of Adult Make Rats.   ENDOCRINOLOGY. Endocrine Society,    157(2): 774-87, (2016).",
+            "distribution": [
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/403/M0710_BDNF%20LTP%20Data.xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "M0710_BDNF LTP Data.xlsx"
+                }
             ],
             "identifier": "A-v42b-403",
             "keyword": [
@@ -41775,20 +41779,10 @@
                 "brain",
                 "thyroid"
             ],
-            "contactPoint": {
-                "fn": "Mary Gilbert",
-                "hasEmail": "mailto:gilbert.mary@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "M0710_BDNF LTP Data.xlsx",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/403/M0710_BDNF%20LTP%20Data.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2015-10-27",
-            "references": [
-                "https://doi.org/10.1210/en.2015-1643"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -41798,42 +41792,42 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1210/en.2015-1643"
+            ],
+            "rights": null,
+            "title": "Mild Thyroid Hormone Insufficiency During Development Compromises Activity-Dependent Neuroplasticity in the Hippocampus of Adult Male Rats"
         },
         {
-            "title": "Enhancing climate adaptation capacity for drinking water treatment facilities (supplement)",
-            "description": "Historical water quality data of the Ohio River. \n\nThis dataset is associated with the following publication:\nLevine, A., J. Yang , and J. Goodrich. Enhancing climate Adaptation Capacity for Drinking Water Treatment Facilities.   Journal of Water and Climate Change. IWA Publishing, London,  UK, 7(3): 1-13, (2016).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "A-qfvd-417",
-            "keyword": [
-                "climate adaptation",
-                "coagulation",
-                "conventional treatment",
-                "resilience",
-                "surface water"
-            ],
             "contactPoint": {
                 "fn": "Yingping Yang",
                 "hasEmail": "mailto:yang.jeff@epa.gov"
             },
+            "description": "Historical water quality data of the Ohio River. \n\nThis dataset is associated with the following publication:\nLevine, A., J. Yang , and J. Goodrich. Enhancing climate Adaptation Capacity for Drinking Water Treatment Facilities.   Journal of Water and Climate Change. IWA Publishing, London,  UK, 7(3): 1-13, (2016).",
             "distribution": [
                 {
-                    "title": "Enhancing Climate Adaptation Capacity for Drinking Water Treatment Facilities.pdf",
                     "downloadURL": "https://pasteur.epa.gov/uploads/417/Enhancing%20Climate%20Adaptation%20Capacity%20for%20Drinking%20Water%20Treatment%20Facilities.pdf",
-                    "mediaType": "application/pdf"
+                    "mediaType": "application/pdf",
+                    "title": "Enhancing Climate Adaptation Capacity for Drinking Water Treatment Facilities.pdf"
                 }
             ],
+            "identifier": "A-qfvd-417",
+            "keyword": [
+                "climate adaptation",
+                "coagulation",
+                "conventional treatment",
+                "resilience",
+                "surface water"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2016-07-03",
-            "references": [
-                "https://doi.org/10.2166/wcc.2016.011"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -41843,47 +41837,47 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.2166/wcc.2016.011"
+            ],
+            "rights": null,
+            "title": "Enhancing climate adaptation capacity for drinking water treatment facilities (supplement)"
         },
         {
-            "title": "Impact of water quality on chlorine demand of corroding copper (Supplement)",
-            "description": "Copper is widely used in drinking water premise plumbing system materials. In buildings such as\r\nhospitals, large and complicated plumbing networks make it difficult to maintain good water quality.\r\nSustaining safe disinfectant residuals throughout a building to protect against waterborne pathogens\r\nsuch as Legionella is particularly challenging since copper and other reactive distribution system materials\r\ncan exert considerable demands. The objective of this work was to evaluate the impact of pH and\r\northophosphate on the consumption of free chlorine associated with corroding copper pipes over time. A\r\ncopper test-loop pilot system was used to control test conditions and systematically meet the study\r\nobjectives. Chlorine consumption trends attributed to abiotic reactions with copper over time were\r\ndifferent for each pH condition tested, and the total amount of chlorine consumed over the test runs\r\nincreased with increasing pH. Orthophosphate eliminated chlorine consumption trends with elapsed\r\ntime (i.e., chlorine demand was consistent across entire test runs). Orthophosphate also greatly reduced\r\nthe total amount of chlorine consumed over the test runs. Interestingly, the total amount of chlorine\r\nconsumed and the consumption rate were not pH dependent when orthophosphate was present. The\r\nfindings reflect the complex and competing reactions at the copper pipe wall including corrosion,\r\noxidation of Cu(I) minerals and ions, and possible oxidation of Cu(II) minerals, and the change in chlorine\r\nspecies all as a function of pH. The work has practical applications for maintaining chlorine residuals in\r\npremise plumbing drinking water systems including large buildings such as hospitals. \n\nThis dataset is associated with the following publication:\nLytle , D., and J. Liggett. Impact of Water Quality on Chlorine Demand of Corroding Copper.   WATER RESEARCH. Elsevier Science Ltd, New York, NY, USA, 92: 11-21, (2016).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "A-3ffg-425",
-            "keyword": [
-                "Oxidant demand",
-                "Chlorine",
-                "Copper",
-                "Orthophosphate",
-                "drinking water"
-            ],
             "contactPoint": {
                 "fn": "Darren Lytle",
                 "hasEmail": "mailto:lytle.darren@epa.gov"
             },
+            "description": "Copper is widely used in drinking water premise plumbing system materials. In buildings such as\r\nhospitals, large and complicated plumbing networks make it difficult to maintain good water quality.\r\nSustaining safe disinfectant residuals throughout a building to protect against waterborne pathogens\r\nsuch as Legionella is particularly challenging since copper and other reactive distribution system materials\r\ncan exert considerable demands. The objective of this work was to evaluate the impact of pH and\r\northophosphate on the consumption of free chlorine associated with corroding copper pipes over time. A\r\ncopper test-loop pilot system was used to control test conditions and systematically meet the study\r\nobjectives. Chlorine consumption trends attributed to abiotic reactions with copper over time were\r\ndifferent for each pH condition tested, and the total amount of chlorine consumed over the test runs\r\nincreased with increasing pH. Orthophosphate eliminated chlorine consumption trends with elapsed\r\ntime (i.e., chlorine demand was consistent across entire test runs). Orthophosphate also greatly reduced\r\nthe total amount of chlorine consumed over the test runs. Interestingly, the total amount of chlorine\r\nconsumed and the consumption rate were not pH dependent when orthophosphate was present. The\r\nfindings reflect the complex and competing reactions at the copper pipe wall including corrosion,\r\noxidation of Cu(I) minerals and ions, and possible oxidation of Cu(II) minerals, and the change in chlorine\r\nspecies all as a function of pH. The work has practical applications for maintaining chlorine residuals in\r\npremise plumbing drinking water systems including large buildings such as hospitals. \n\nThis dataset is associated with the following publication:\nLytle , D., and J. Liggett. Impact of Water Quality on Chlorine Demand of Corroding Copper.   WATER RESEARCH. Elsevier Science Ltd, New York, NY, USA, 92: 11-21, (2016).",
             "distribution": [
                 {
-                    "title": "Copper chlorine.pdf",
                     "downloadURL": "https://pasteur.epa.gov/uploads/425/Copper%20chlorine.pdf",
-                    "mediaType": "application/pdf"
+                    "mediaType": "application/pdf",
+                    "title": "Copper chlorine.pdf"
                 },
                 {
-                    "title": "chlorine paper data.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/425/chlorine%20paper%20data.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "chlorine paper data.xlsx"
                 }
             ],
+            "identifier": "A-3ffg-425",
+            "keyword": [
+                "Oxidant demand",
+                "Chlorine",
+                "Copper",
+                "Orthophosphate",
+                "drinking water"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2016-01-15",
-            "references": [
-                "https://doi.org/10.1016/j.watres.2016.01.032"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -41893,19 +41887,28 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.watres.2016.01.032"
+            ],
+            "rights": null,
+            "title": "Impact of water quality on chlorine demand of corroding copper (Supplement)"
         },
         {
-            "title": "Volatile and semivolatile organic compounds in laboratory peat fire emissions",
-            "description": "Supporting information Tables S3 and S4 list emission factors in g/kg of speciated volatile and particulate organic compounds emitted from peat burning. Peat samples were acquired from Alligator River (AR) and Pocosin Lakes (PL) National Wildlife Refuges. \n\nThis dataset is associated with the following publication:\nGeorge , I., R. Black, J. Walker , C. Geron , J. Aurell , M. Hays , W. Preston, and B. Gullett. Volatile and semivolatile organic compounds in laboratory peat fire emissions.   ATMOSPHERIC ENVIRONMENT. Elsevier Science Ltd, New York, NY, USA, 132: 163-170, (2016).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:094"
+            "contactPoint": {
+                "fn": "Ingrid George",
+                "hasEmail": "mailto:george.ingrid@epa.gov"
+            },
+            "description": "Supporting information Tables S3 and S4 list emission factors in g/kg of speciated volatile and particulate organic compounds emitted from peat burning. Peat samples were acquired from Alligator River (AR) and Pocosin Lakes (PL) National Wildlife Refuges. \n\nThis dataset is associated with the following publication:\nGeorge , I., R. Black, J. Walker , C. Geron , J. Aurell , M. Hays , W. Preston, and B. Gullett. Volatile and semivolatile organic compounds in laboratory peat fire emissions.   ATMOSPHERIC ENVIRONMENT. Elsevier Science Ltd, New York, NY, USA, 132: 163-170, (2016).",
+            "distribution": [
+                {
+                    "accessURL": "https://www.sciencedirect.com/science/article/pii/S1352231016301388",
+                    "title": "https://www.sciencedirect.com/science/article/pii/S1352231016301388"
+                }
             ],
             "identifier": "A-qrg3-41",
             "keyword": [
@@ -41916,18 +41919,11 @@
                 "polycyclic aromatic hydrocarbons",
                 "particulate matter"
             ],
-            "contactPoint": {
-                "fn": "Ingrid George",
-                "hasEmail": "mailto:george.ingrid@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "https://www.sciencedirect.com/science/article/pii/S1352231016301388",
-                    "accessURL": "https://www.sciencedirect.com/science/article/pii/S1352231016301388"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2015-12-17",
-            "references": null,
+            "programCode": [
+                "020:094"
+            ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
                 "subOrganizationOf": {
@@ -41936,41 +41932,39 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": null,
+            "rights": null,
+            "title": "Volatile and semivolatile organic compounds in laboratory peat fire emissions"
         },
         {
-            "title": "The Full-Scale Implementation of an Innovative (Supplemental)",
-            "description": "Across the United States, high levels of ammonia in drinking water\r\nsources can be found. Although ammonia in water does not pose\r\na direct health concern, ammonia nitrification can cause a number\r\nof issues and reduce the effectiveness of some treatment processes.\r\nAn innovative biological ammonia-removal drinking water\r\ntreatment process was developed and, after the success of a pilot\r\nstudy, a full-scale treatment system using the process was built in\r\na small Iowa community. The treatment plant included a unique\r\naeration contactor design that is able to consistently reduce\r\nammonia from 3.3 mg of nitrogen/L to nearly nondetectable after\r\na biofilm acclimation period. Close system monitoring was\r\nperformed to avoid excess nitrite release during acclimation, and\r\nphosphate was added to enhance biological activity on the basis\r\nof pilot study findings. The treatment system is robust, reliable,\r\nand relatively simple to operate. The operations and effectiveness\r\nof the treatment plant were documented in the study. \n\nThis dataset is associated with the following publication:\nLytle , D., D. Williams , C. Muhlen , M. Pham , K. Kelty , M. Wildman, G. Lang, M. Wilcox, and M. Kohne. The Full-Scale Implementation of an Innovative Biological Ammonia Treatment Process.   Journal AWWA. American Water Works Association, Denver, CO, USA, 107(12): E648-E665, (2015).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "A-nzss-420",
-            "keyword": [
-                "ammonia",
-                "biological treatment",
-                "drinking water",
-                "nitrification"
-            ],
             "contactPoint": {
                 "fn": "Darren Lytle",
                 "hasEmail": "mailto:lytle.darren@epa.gov"
             },
+            "description": "Across the United States, high levels of ammonia in drinking water\r\nsources can be found. Although ammonia in water does not pose\r\na direct health concern, ammonia nitrification can cause a number\r\nof issues and reduce the effectiveness of some treatment processes.\r\nAn innovative biological ammonia-removal drinking water\r\ntreatment process was developed and, after the success of a pilot\r\nstudy, a full-scale treatment system using the process was built in\r\na small Iowa community. The treatment plant included a unique\r\naeration contactor design that is able to consistently reduce\r\nammonia from 3.3 mg of nitrogen/L to nearly nondetectable after\r\na biofilm acclimation period. Close system monitoring was\r\nperformed to avoid excess nitrite release during acclimation, and\r\nphosphate was added to enhance biological activity on the basis\r\nof pilot study findings. The treatment system is robust, reliable,\r\nand relatively simple to operate. The operations and effectiveness\r\nof the treatment plant were documented in the study. \n\nThis dataset is associated with the following publication:\nLytle , D., D. Williams , C. Muhlen , M. Pham , K. Kelty , M. Wildman, G. Lang, M. Wilcox, and M. Kohne. The Full-Scale Implementation of an Innovative Biological Ammonia Treatment Process.   Journal AWWA. American Water Works Association, Denver, CO, USA, 107(12): E648-E665, (2015).",
             "distribution": [
                 {
-                    "title": "jaw201512lytle_es.pdf",
                     "downloadURL": "https://pasteur.epa.gov/uploads/420/jaw201512lytle_es.pdf",
-                    "mediaType": "application/pdf"
+                    "mediaType": "application/pdf",
+                    "title": "jaw201512lytle_es.pdf"
                 }
             ],
+            "identifier": "A-nzss-420",
+            "keyword": [
+                "ammonia",
+                "biological treatment",
+                "drinking water",
+                "nitrification"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2015-12-01",
-            "references": [
-                "https://doi.org/10.5942/jawwa.2015.107.0176"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -41980,19 +41974,29 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.5942/jawwa.2015.107.0176"
+            ],
+            "rights": null,
+            "title": "The Full-Scale Implementation of an Innovative (Supplemental)"
         },
         {
-            "title": "Comparison of Bottomless Lift Nets and Breder Traps for Sampling Salt-Marsh Nekton",
-            "description": "Data set contains: the length of mummichogs (Fundulus heteroclitus) caught on lift nets and Breder traps from May to September 2002; the sizes of green crabs caught in the lift nets and Breder traps during same time frame; the mean density and sample size data for each sampling time and each site (3 sites total) for total nekton sampled and total nekton minus shrimp. \n\nThis dataset is associated with the following publication:\nRaposa, K., and M. Chintala. Comparison of Bottomless Lift Nets and Breder Traps for Sampling Salt-Marsh Nekton.   TRANSACTIONS OF THE AMERICAN FISHERIES SOCIETY. American Fisheries Society, Bethesda, MD, USA, 145(1): 163-172, (2016).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
+            "contactPoint": {
+                "fn": "Marnita Chintala",
+                "hasEmail": "mailto:chintala.marty@epa.gov"
+            },
+            "description": "Data set contains: the length of mummichogs (Fundulus heteroclitus) caught on lift nets and Breder traps from May to September 2002; the sizes of green crabs caught in the lift nets and Breder traps during same time frame; the mean density and sample size data for each sampling time and each site (3 sites total) for total nekton sampled and total nekton minus shrimp. \n\nThis dataset is associated with the following publication:\nRaposa, K., and M. Chintala. Comparison of Bottomless Lift Nets and Breder Traps for Sampling Salt-Marsh Nekton.   TRANSACTIONS OF THE AMERICAN FISHERIES SOCIETY. American Fisheries Society, Bethesda, MD, USA, 145(1): 163-172, (2016).",
+            "distribution": [
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/424/Raposa%20and%20Chintala%20data.xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Raposa and Chintala data.xlsx"
+                }
             ],
             "identifier": "A-2z38-424",
             "keyword": [
@@ -42007,20 +42011,10 @@
                 "nekton",
                 "sampling methods"
             ],
-            "contactPoint": {
-                "fn": "Marnita Chintala",
-                "hasEmail": "mailto:chintala.marty@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "Raposa and Chintala data.xlsx",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/424/Raposa%20and%20Chintala%20data.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2016-09-21",
-            "references": [
-                "https://doi.org/10.1080/00028487.2015.1111254"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -42030,40 +42024,42 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1080/00028487.2015.1111254"
+            ],
+            "rights": null,
+            "title": "Comparison of Bottomless Lift Nets and Breder Traps for Sampling Salt-Marsh Nekton"
         },
         {
-            "title": "GRE Enzymes for Vector Analysis",
-            "description": "Microbial enzyme data that were collected during the 2004-2006 EMAP-GRE program. These data were then used by Moorhead et al (2016) in their ecoenzyme vector analysis paper. \n\nThis dataset is associated with the following publication:\nMoorhead, D., R. Sinsabaugh, B. Hill , and M. Weintraub. Vector analysis of ecoenzyme activities reveal constraints on coupled C, N and P dynamics.   SOIL BIOLOGY AND BIOCHEMISTRY. Elsevier Science Ltd, New York, NY, USA, 93: 1-7, (2016).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "A-76hm-174",
-            "keyword": [
-                "microbial ecoenzymes",
-                "nutrient limitation",
-                "vector analysis"
-            ],
             "contactPoint": {
                 "fn": "Brian Hill",
                 "hasEmail": "mailto:hill.brian@epa.gov"
             },
+            "describedBy": "https://pasteur.epa.gov/uploads/174/documents/GRE%20Vectors%20Data%20Dictionary.docx",
+            "describedByType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+            "description": "Microbial enzyme data that were collected during the 2004-2006 EMAP-GRE program. These data were then used by Moorhead et al (2016) in their ecoenzyme vector analysis paper. \n\nThis dataset is associated with the following publication:\nMoorhead, D., R. Sinsabaugh, B. Hill , and M. Weintraub. Vector analysis of ecoenzyme activities reveal constraints on coupled C, N and P dynamics.   SOIL BIOLOGY AND BIOCHEMISTRY. Elsevier Science Ltd, New York, NY, USA, 93: 1-7, (2016).",
             "distribution": [
                 {
-                    "title": "GRE_VECTOR.csv",
                     "downloadURL": "https://pasteur.epa.gov/uploads/174/GRE_VECTOR.csv",
-                    "mediaType": "application/vnd.ms-excel"
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "GRE_VECTOR.csv"
                 }
             ],
+            "identifier": "A-76hm-174",
+            "keyword": [
+                "microbial ecoenzymes",
+                "nutrient limitation",
+                "vector analysis"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2016-08-10",
-            "references": [
-                "https://doi.org/10.1016/j.soilbio.2015.10.019"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -42074,42 +42070,40 @@
                     }
                 }
             },
-            "describedBy": "https://pasteur.epa.gov/uploads/174/documents/GRE%20Vectors%20Data%20Dictionary.docx",
-            "describedByType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
+            "references": [
+                "https://doi.org/10.1016/j.soilbio.2015.10.019"
+            ],
+            "rights": null,
+            "title": "GRE Enzymes for Vector Analysis"
         },
         {
-            "title": "Optimized UDP-glucuronosyltransferase (UGT) activity assay for trout liver S9 fractions",
-            "description": "This publication provides an optimized UGT assay for trout liver S9 fractions which can be used to perform in vitro-in vivo extrapolations of measured UGT activity. \n\nThis dataset is associated with the following publication:\nLadd, M., P. Fitzsimmons , and J. Nichols. Optimization of a UDP-glucuronosyltransferase assay for trout liver S9 fractions: Activity enhancement by alamethicin, a pore-forming peptide.   XENOBIOTICA. Taylor & Francis, Inc., Philadelphia, PA, USA, 46(12): 1066-1075, (2016).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:095"
-            ],
-            "identifier": "A-0p2p-89",
-            "keyword": [
-                "S9 fractions",
-                "UDP glucuronosyltransferase",
-                "rainbow trout",
-                "alamethicin"
-            ],
             "contactPoint": {
                 "fn": "John Nichols",
                 "hasEmail": "mailto:nichols.john@epa.gov"
             },
+            "description": "This publication provides an optimized UGT assay for trout liver S9 fractions which can be used to perform in vitro-in vivo extrapolations of measured UGT activity. \n\nThis dataset is associated with the following publication:\nLadd, M., P. Fitzsimmons , and J. Nichols. Optimization of a UDP-glucuronosyltransferase assay for trout liver S9 fractions: Activity enhancement by alamethicin, a pore-forming peptide.   XENOBIOTICA. Taylor & Francis, Inc., Philadelphia, PA, USA, 46(12): 1066-1075, (2016).",
             "distribution": [
                 {
-                    "title": "Ladd et al., 2016, Science Hub Data Summary.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/89/Ladd%20et%20al.%2C%202016%2C%20Science%20Hub%20Data%20Summary.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Ladd et al., 2016, Science Hub Data Summary.xlsx"
                 }
             ],
+            "identifier": "A-0p2p-89",
+            "keyword": [
+                "S9 fractions",
+                "UDP glucuronosyltransferase",
+                "rainbow trout",
+                "alamethicin"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2015-09-30",
-            "references": [
-                "https://doi.org/10.3109/00498254.2016.1149634"
+            "programCode": [
+                "020:095"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -42119,38 +42113,40 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.3109/00498254.2016.1149634"
+            ],
+            "rights": null,
+            "title": "Optimized UDP-glucuronosyltransferase (UGT) activity assay for trout liver S9 fractions"
         },
         {
-            "title": "SRHA calibration curve",
-            "description": "an UV calibration curve for SRHA quantitation. \n\nThis dataset is associated with the following publication:\nChang, X., and D. Bouchard. Surfactant-Wrapped Multiwalled Carbon Nanotubes in Aquatic Systems: Surfactant Displacement in the Presence of Humic Acid.   ENVIRONMENTAL SCIENCE & TECHNOLOGY. American Chemical Society, Washington, DC, USA, 50(0): 9214-9222, (2016).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:095"
-            ],
-            "identifier": "A-83bs-140",
-            "keyword": [
-                "humic acid; uv",
-                "MWCNTs; nanomaterials; surfactant; ENMs; humic acid"
-            ],
             "contactPoint": {
                 "fn": "Dermont Bouchard",
                 "hasEmail": "mailto:bouchard.dermont@epa.gov"
             },
+            "description": "an UV calibration curve for SRHA quantitation. \n\nThis dataset is associated with the following publication:\nChang, X., and D. Bouchard. Surfactant-Wrapped Multiwalled Carbon Nanotubes in Aquatic Systems: Surfactant Displacement in the Presence of Humic Acid.   ENVIRONMENTAL SCIENCE & TECHNOLOGY. American Chemical Society, Washington, DC, USA, 50(0): 9214-9222, (2016).",
             "distribution": [
                 {
-                    "title": "SRHA calibration curve.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/140/SRHA%20calibration%20curve.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "SRHA calibration curve.xlsx"
                 }
             ],
+            "identifier": "A-83bs-140",
+            "keyword": [
+                "humic acid; uv",
+                "MWCNTs; nanomaterials; surfactant; ENMs; humic acid"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2015-07-02",
-            "references": null,
+            "programCode": [
+                "020:095"
+            ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
                 "subOrganizationOf": {
@@ -42159,42 +42155,40 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": null,
+            "rights": null,
+            "title": "SRHA calibration curve"
         },
         {
-            "title": "Data for pilot-scale low level hydrogen peroxide tests using humidifiers",
-            "description": "Dataset includes data from each experiment conducted in the pilot-scale testing.  Each sheet of the Excel file pertains to each test. A data dictionary is included in the first sheet.  In each sheet there are microbiological data (colony forming units) for each test and positive control coupon used in the study. Also shown is the calculation of decontamination efficacy (log10 reduction). \n\nThis dataset is associated with the following publication:\nWood, J., W. Calfee, S. Ryan, L. Mickelsen, M. Clayton, and V. Rastogi. A Simple Decontamination Approach Using Hydrogen Peroxide Vapor for Bacillus anthracis Spore Inactivation.   JOURNAL OF APPLIED MICROBIOLOGY. Blackwell Publishing, Malden, MA, USA, 121(6): 1603-1615, (2016).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:060"
-            ],
-            "identifier": "A-73nd-242",
-            "keyword": [
-                "Bacillus anthracis",
-                "Decontamination",
-                "hydrogen peroxide vapor",
-                "bacterial spores",
-                "antimicrobial"
-            ],
             "contactPoint": {
                 "fn": "Joseph Wood",
                 "hasEmail": "mailto:wood.joe@epa.gov"
             },
+            "description": "Dataset includes data from each experiment conducted in the pilot-scale testing.  Each sheet of the Excel file pertains to each test. A data dictionary is included in the first sheet.  In each sheet there are microbiological data (colony forming units) for each test and positive control coupon used in the study. Also shown is the calculation of decontamination efficacy (log10 reduction). \n\nThis dataset is associated with the following publication:\nWood, J., W. Calfee, S. Ryan, L. Mickelsen, M. Clayton, and V. Rastogi. A Simple Decontamination Approach Using Hydrogen Peroxide Vapor for Bacillus anthracis Spore Inactivation.   JOURNAL OF APPLIED MICROBIOLOGY. Blackwell Publishing, Malden, MA, USA, 121(6): 1603-1615, (2016).",
             "distribution": [
                 {
-                    "title": "COMMANDER data.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/242/COMMANDER%20data.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "COMMANDER data.xlsx"
                 }
             ],
+            "identifier": "A-73nd-242",
+            "keyword": [
+                "Bacillus anthracis",
+                "Decontamination",
+                "hydrogen peroxide vapor",
+                "bacterial spores",
+                "antimicrobial"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2015-09-11",
-            "references": [
-                "http://onlinelibrary.wiley.com/doi/10.1111/jam.13284/full"
+            "programCode": [
+                "020:060"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -42204,42 +42198,42 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "http://onlinelibrary.wiley.com/doi/10.1111/jam.13284/full"
+            ],
+            "rights": null,
+            "title": "Data for pilot-scale low level hydrogen peroxide tests using humidifiers"
         },
         {
-            "title": "Lab-scale hydrogen peroxide data from ECBC",
-            "description": "Data from small lab scale tests conducted at ECBC.  It contains efficacy data as well as data on env conditions such as temperature, RH, and hydrogen peroxide vapor concentration. \n\nThis dataset is associated with the following publication:\nWood, J., W. Calfee, S. Ryan, L. Mickelsen, M. Clayton, and V. Rastogi. A Simple Decontamination Approach Using Hydrogen Peroxide Vapor for Bacillus anthracis Spore Inactivation.   JOURNAL OF APPLIED MICROBIOLOGY. Blackwell Publishing, Malden, MA, USA, 121(6): 1603-1615, (2016).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:060"
-            ],
-            "identifier": "A-73nd-244",
-            "keyword": [
-                "Bacillus anthracis",
-                "Decontamination",
-                "hydrogen peroxide vapor",
-                "bacterial spores",
-                "antimicrobial"
-            ],
             "contactPoint": {
                 "fn": "Joseph Wood",
                 "hasEmail": "mailto:wood.joe@epa.gov"
             },
+            "description": "Data from small lab scale tests conducted at ECBC.  It contains efficacy data as well as data on env conditions such as temperature, RH, and hydrogen peroxide vapor concentration. \n\nThis dataset is associated with the following publication:\nWood, J., W. Calfee, S. Ryan, L. Mickelsen, M. Clayton, and V. Rastogi. A Simple Decontamination Approach Using Hydrogen Peroxide Vapor for Bacillus anthracis Spore Inactivation.   JOURNAL OF APPLIED MICROBIOLOGY. Blackwell Publishing, Malden, MA, USA, 121(6): 1603-1615, (2016).",
             "distribution": [
                 {
-                    "title": "ECBC results summary.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/244/ECBC%20results%20summary.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "ECBC results summary.xlsx"
                 }
             ],
+            "identifier": "A-73nd-244",
+            "keyword": [
+                "Bacillus anthracis",
+                "Decontamination",
+                "hydrogen peroxide vapor",
+                "bacterial spores",
+                "antimicrobial"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2015-08-13",
-            "references": [
-                "http://onlinelibrary.wiley.com/doi/10.1111/jam.13284/full"
+            "programCode": [
+                "020:060"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -42249,39 +42243,41 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "http://onlinelibrary.wiley.com/doi/10.1111/jam.13284/full"
+            ],
+            "rights": null,
+            "title": "Lab-scale hydrogen peroxide data from ECBC"
         },
         {
-            "title": "CAIRSENSE-Atlanta Low Cost Sensor Evaluation Versus Reference Monitors",
-            "description": "Short time interval comparisons of low cost sensor response and corresponding Federal Reference or Federal Equivalent Monitors at an NCOR site located in proximity to Atlanta, Georgia. Portions of this dataset are inaccessible because: The data were integrated using R.  Currently there is no means of reporting \"R: database in the science hub. Data are still being reviewed as part of the journal publication process.  Release prior to journal acceptance could result in external parties inappropriately using the data (including sensor manufacturers who might use such data without a full understanding of its meaning). They can be accessed through the following means: Direct transfer from the Principal Investigator upon journal publication. Format: The dataset was created in R and represents an extensive short time resolution of thousands of lines of air quality measurements.  In addition, the data have been integrated into a manuscript which has yet to be published.  The manuscript was cleared  through STICs but has not yet rec'd journal based peer review acceptance. \n\nThis dataset is associated with the following publication:\nJiao, W., G. Hagler, R. Williams, R. Sharpe, R. Brown, D. Garver, R. Judge, M. Caudill, J. Rickard, M. Davis, L. Weinstock, S. Zimmer-Dauphinee, and K. Buckley. Community Air Sensor Network (CAIRSENSE) project: Evaluation of low-cost sensor performance in a suburban environment in the southeastern United States.   Atmospheric Measurement Techniques. Copernicus Publications, Katlenburg-Lindau,  GERMANY, 9: 5282-5292, (2016).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "A-hx3v-157",
-            "keyword": [
-                "criteria air polluants",
-                "low cost air quality sensors"
-            ],
             "contactPoint": {
                 "fn": "Ronald Williams",
                 "hasEmail": "mailto:williams.ronald@epa.gov"
             },
+            "describedBy": "https://pasteur.epa.gov/uploads/157/documents/Science%20Hub%20Data%20Dictionary.xlsx",
+            "describedByType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+            "description": "Short time interval comparisons of low cost sensor response and corresponding Federal Reference or Federal Equivalent Monitors at an NCOR site located in proximity to Atlanta, Georgia. Portions of this dataset are inaccessible because: The data were integrated using R.  Currently there is no means of reporting \"R: database in the science hub. Data are still being reviewed as part of the journal publication process.  Release prior to journal acceptance could result in external parties inappropriately using the data (including sensor manufacturers who might use such data without a full understanding of its meaning). They can be accessed through the following means: Direct transfer from the Principal Investigator upon journal publication. Format: The dataset was created in R and represents an extensive short time resolution of thousands of lines of air quality measurements.  In addition, the data have been integrated into a manuscript which has yet to be published.  The manuscript was cleared  through STICs but has not yet rec'd journal based peer review acceptance. \n\nThis dataset is associated with the following publication:\nJiao, W., G. Hagler, R. Williams, R. Sharpe, R. Brown, D. Garver, R. Judge, M. Caudill, J. Rickard, M. Davis, L. Weinstock, S. Zimmer-Dauphinee, and K. Buckley. Community Air Sensor Network (CAIRSENSE) project: Evaluation of low-cost sensor performance in a suburban environment in the southeastern United States.   Atmospheric Measurement Techniques. Copernicus Publications, Katlenburg-Lindau,  GERMANY, 9: 5282-5292, (2016).",
             "distribution": [
                 {
-                    "title": "Science Data Hub CAIRSENSE Atlanta Data Set -Reduced.csv",
                     "downloadURL": "https://pasteur.epa.gov/uploads/157/Science%20Data%20Hub%20CAIRSENSE%20Atlanta%20Data%20Set%20-Reduced.csv",
-                    "mediaType": "application/vnd.ms-excel"
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Science Data Hub CAIRSENSE Atlanta Data Set -Reduced.csv"
                 }
             ],
+            "identifier": "A-hx3v-157",
+            "keyword": [
+                "criteria air polluants",
+                "low cost air quality sensors"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2016-04-01",
-            "references": [
-                "https://doi.org/10.5194/amt-9-5281-2016"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -42292,164 +42288,163 @@
                     }
                 }
             },
-            "describedBy": "https://pasteur.epa.gov/uploads/157/documents/Science%20Hub%20Data%20Dictionary.xlsx",
-            "describedByType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+            "references": [
+                "https://doi.org/10.5194/amt-9-5281-2016"
+            ],
+            "rights": null,
+            "title": "CAIRSENSE-Atlanta Low Cost Sensor Evaluation Versus Reference Monitors"
         },
         {
-            "title": "Flow list and test results",
-            "description": "These data accompany the manuscript 'Critical Review of Elementary Flows in LCA Data'. Each file presents a subgroup of the elementary flows (data used for analysis) and all the analysis results. Files are separated by flow types. The 'Element or Compound' types contained over 115,000 flows and was broken into three files (a, b,and c).  A guide to the file contents and explanation of flow types are provided in the 'CriticalReviewofElementaryFlows_Data_Guide' file. \n\nThis dataset is associated with the following publication:\nEdelen, A., W. Ingwersen, C. Rodriguez, R. Alvarenga, A.R. de Almeida, and G. Wernet. Critical Review of Elementary Flows in LCA data.   INTERNATIONAL JOURNAL OF LIFE CYCLE ASSESSMENT. Ecomed Verlagsgesellschaft AG, Landsberg,  GERMANY,  01-13, (2017).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:097"
-            ],
-            "identifier": "A-p2p0-450",
-            "keyword": [
-                "nomenclature",
-                "critical review",
-                "life cycle assessment",
-                "life cycle inventory data",
-                "interoperability"
-            ],
             "contactPoint": {
                 "fn": "Wesley Ingwersen",
                 "hasEmail": "mailto:ingwersen.wesley@epa.gov"
             },
+            "describedBy": "https://pasteur.epa.gov/uploads/450/documents/CriticalReviewofElementaryFlows_DataDictionary.xlsx",
+            "describedByType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+            "description": "These data accompany the manuscript 'Critical Review of Elementary Flows in LCA Data'. Each file presents a subgroup of the elementary flows (data used for analysis) and all the analysis results. Files are separated by flow types. The 'Element or Compound' types contained over 115,000 flows and was broken into three files (a, b,and c).  A guide to the file contents and explanation of flow types are provided in the 'CriticalReviewofElementaryFlows_Data_Guide' file. \n\nThis dataset is associated with the following publication:\nEdelen, A., W. Ingwersen, C. Rodriguez, R. Alvarenga, A.R. de Almeida, and G. Wernet. Critical Review of Elementary Flows in LCA data.   INTERNATIONAL JOURNAL OF LIFE CYCLE ASSESSMENT. Ecomed Verlagsgesellschaft AG, Landsberg,  GERMANY,  01-13, (2017).",
             "distribution": [
                 {
-                    "title": "Biological_Analysis.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/450/Biological_Analysis.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Biological_Analysis.xlsx"
                 },
                 {
-                    "title": "Element or Compound_Analysis.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/450/Element%20or%20Compound_Analysis.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Element or Compound_Analysis.xlsx"
                 },
                 {
-                    "title": "Element or Compound_Compartment_a.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/450/Element%20or%20Compound_Compartment_a.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Element or Compound_Compartment_a.xlsx"
                 },
                 {
-                    "title": "Element or Compound_Compartment_b.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/450/Element%20or%20Compound_Compartment_b.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Element or Compound_Compartment_b.xlsx"
                 },
                 {
-                    "title": "Element or Compound_Compartment_c.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/450/Element%20or%20Compound_Compartment_c.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Element or Compound_Compartment_c.xlsx"
                 },
                 {
-                    "title": "Element or Compound_Elementary Flow_a.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/450/Element%20or%20Compound_Elementary%20Flow_a.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Element or Compound_Elementary Flow_a.xlsx"
                 },
                 {
-                    "title": "Element or Compound_Elementary Flow_b.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/450/Element%20or%20Compound_Elementary%20Flow_b.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Element or Compound_Elementary Flow_b.xlsx"
                 },
                 {
-                    "title": "Element or Compound_Elementary Flow_c.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/450/Element%20or%20Compound_Elementary%20Flow_c.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Element or Compound_Elementary Flow_c.xlsx"
                 },
                 {
-                    "title": "Element or Compound_flow by source.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/450/Element%20or%20Compound_flow%20by%20source.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Element or Compound_flow by source.xlsx"
                 },
                 {
-                    "title": "Element or Compound_formating.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/450/Element%20or%20Compound_formating.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Element or Compound_formating.xlsx"
                 },
                 {
-                    "title": "Element or Compound_Input_Output_a.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/450/Element%20or%20Compound_Input_Output_a.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Element or Compound_Input_Output_a.xlsx"
                 },
                 {
-                    "title": "Element or Compound_Input_Output_b.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/450/Element%20or%20Compound_Input_Output_b.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Element or Compound_Input_Output_b.xlsx"
                 },
                 {
-                    "title": "Element or Compound_Input_Output_c.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/450/Element%20or%20Compound_Input_Output_c.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Element or Compound_Input_Output_c.xlsx"
                 },
                 {
-                    "title": "Element or Compound_Linked identifier_a.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/450/Element%20or%20Compound_Linked%20identifier_a.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Element or Compound_Linked identifier_a.xlsx"
                 },
                 {
-                    "title": "Element or Compound_Linked identifier_b.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/450/Element%20or%20Compound_Linked%20identifier_b.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Element or Compound_Linked identifier_b.xlsx"
                 },
                 {
-                    "title": "Element or Compound_Linked identifier_c.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/450/Element%20or%20Compound_Linked%20identifier_c.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Element or Compound_Linked identifier_c.xlsx"
                 },
                 {
-                    "title": "Element or Compound_Metadata_a.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/450/Element%20or%20Compound_Metadata_a.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Element or Compound_Metadata_a.xlsx"
                 },
                 {
-                    "title": "Element or Compound_Metadata_b.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/450/Element%20or%20Compound_Metadata_b.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Element or Compound_Metadata_b.xlsx"
                 },
                 {
-                    "title": "Element or Compound_Metadata_c.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/450/Element%20or%20Compound_Metadata_c.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Element or Compound_Metadata_c.xlsx"
                 },
                 {
-                    "title": "Energy_Analysis.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/450/Energy_Analysis.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Energy_Analysis.xlsx"
                 },
                 {
-                    "title": "Fossil and Nuclear Fuels_Analysis.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/450/Fossil%20and%20Nuclear%20Fuels_Analysis.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Fossil and Nuclear Fuels_Analysis.xlsx"
                 },
                 {
-                    "title": "Groups_Chemicals_Analysis_.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/450/Groups_Chemicals_Analysis_.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Groups_Chemicals_Analysis_.xlsx"
                 },
                 {
-                    "title": "Land_Analysis.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/450/Land_Analysis.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Land_Analysis.xlsx"
                 },
                 {
-                    "title": "Other_Analysis.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/450/Other_Analysis.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Other_Analysis.xlsx"
                 },
                 {
-                    "title": "Water_Analysis.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/450/Water_Analysis.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Water_Analysis.xlsx"
                 }
             ],
+            "identifier": "A-p2p0-450",
+            "keyword": [
+                "nomenclature",
+                "critical review",
+                "life cycle assessment",
+                "life cycle inventory data",
+                "interoperability"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2016-11-22",
-            "references": [
-                "https://doi.org/10.1007/s11367-017-1354-3",
-                "https://pasteur.epa.gov/uploads/450/documents/CriticalReviewofElementaryFlows_DataGuide.xlsx"
+            "programCode": [
+                "020:097"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -42460,43 +42455,44 @@
                     }
                 }
             },
-            "describedBy": "https://pasteur.epa.gov/uploads/450/documents/CriticalReviewofElementaryFlows_DataDictionary.xlsx",
-            "describedByType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+            "references": [
+                "https://doi.org/10.1007/s11367-017-1354-3",
+                "https://pasteur.epa.gov/uploads/450/documents/CriticalReviewofElementaryFlows_DataGuide.xlsx"
+            ],
+            "rights": null,
+            "title": "Flow list and test results"
         },
         {
-            "title": "Ozone-induced systemic and pulmonary effects are diminished in adrenalectomized rats",
-            "description": "This data set is an excel file pertaining to the study that examined ozone-induced systemic and pulmonary effects in rats that underwent SHAM surgery (control), adrenal demedullation or total bilateral adrenalectomy. Different pages of the spreadsheet shows individual animal data for markers of lung injury and inflammation, body weights, whole body plethysmography measurements, levels of circulating hormones and lipids, and circulating white blood cell count as well as platelet count. \n\nThis dataset is associated with the following publication:\nMiller, D., S. Snow, M. Schladweiler , J. Richards , A. Ghio , A. Ledbetter , and U. Kodavanti. Acute Ozone-Induced Pulmonary and Systemic Metabolic Effects are Diminished in Adrenalectomized Rats#.   TOXICOLOGICAL SCIENCES. Society of Toxicology,    150(2): 312-22, (2016).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "A-xsjt-216",
-            "keyword": [
-                "Ozone",
-                "adrenalectomy",
-                "Stress Response",
-                "HPA-axis",
-                "lung injury"
-            ],
             "contactPoint": {
                 "fn": "Urmila Kodavanti",
                 "hasEmail": "mailto:kodavanti.urmila@epa.gov"
             },
+            "describedBy": "https://pasteur.epa.gov/uploads/216/documents/Miller%20et%20al%20ToxSci%202016%20Science%20hub%20data.xlsx",
+            "describedByType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+            "description": "This data set is an excel file pertaining to the study that examined ozone-induced systemic and pulmonary effects in rats that underwent SHAM surgery (control), adrenal demedullation or total bilateral adrenalectomy. Different pages of the spreadsheet shows individual animal data for markers of lung injury and inflammation, body weights, whole body plethysmography measurements, levels of circulating hormones and lipids, and circulating white blood cell count as well as platelet count. \n\nThis dataset is associated with the following publication:\nMiller, D., S. Snow, M. Schladweiler , J. Richards , A. Ghio , A. Ledbetter , and U. Kodavanti. Acute Ozone-Induced Pulmonary and Systemic Metabolic Effects are Diminished in Adrenalectomized Rats#.   TOXICOLOGICAL SCIENCES. Society of Toxicology,    150(2): 312-22, (2016).",
             "distribution": [
                 {
-                    "title": "Miller et al ToxSci 2016 Science hub data.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/216/Miller%20et%20al%20ToxSci%202016%20Science%20hub%20data.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Miller et al ToxSci 2016 Science hub data.xlsx"
                 }
             ],
+            "identifier": "A-xsjt-216",
+            "keyword": [
+                "Ozone",
+                "adrenalectomy",
+                "Stress Response",
+                "HPA-axis",
+                "lung injury"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2016-08-22",
-            "references": [
-                "https://doi.org/10.1093/toxsci/kfv331"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -42507,20 +42503,28 @@
                     }
                 }
             },
-            "describedBy": "https://pasteur.epa.gov/uploads/216/documents/Miller%20et%20al%20ToxSci%202016%20Science%20hub%20data.xlsx",
-            "describedByType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+            "references": [
+                "https://doi.org/10.1093/toxsci/kfv331"
+            ],
+            "rights": null,
+            "title": "Ozone-induced systemic and pulmonary effects are diminished in adrenalectomized rats"
         },
         {
-            "title": "Locomotor activity and tissues levels following acute administration of lambda- and gamma-cyhalothrin in rats",
-            "description": "raw motor activity counts and tissue levels. \n\nThis dataset is associated with the following publication:\nMoser, G., Z. Liu, C. Schlosser, T. Spanogle, A. Chandrasekaran, and K. Mcdaniel. Locomotor activity and tissue levels following acute administration of lambda- and gamma-cyhalothrin in rats.   TOXICOLOGY AND APPLIED PHARMACOLOGY. Academic Press Incorporated, Orlando, FL, USA, 313: 97-103, (2016).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
+            "contactPoint": {
+                "fn": "Virginia Moser",
+                "hasEmail": "mailto:moser.ginger@epa.gov"
+            },
+            "description": "raw motor activity counts and tissue levels. \n\nThis dataset is associated with the following publication:\nMoser, G., Z. Liu, C. Schlosser, T. Spanogle, A. Chandrasekaran, and K. Mcdaniel. Locomotor activity and tissue levels following acute administration of lambda- and gamma-cyhalothrin in rats.   TOXICOLOGY AND APPLIED PHARMACOLOGY. Academic Press Incorporated, Orlando, FL, USA, 313: 97-103, (2016).",
+            "distribution": [
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/249/science%20hub%20data%20summary.xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "science hub data summary.xlsx"
+                }
             ],
             "identifier": "A-t4bx-249",
             "keyword": [
@@ -42531,20 +42535,10 @@
                 "toxicokineticscyhalothrin",
                 "toxicokinetics"
             ],
-            "contactPoint": {
-                "fn": "Virginia Moser",
-                "hasEmail": "mailto:moser.ginger@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "science hub data summary.xlsx",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/249/science%20hub%20data%20summary.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2016-08-29",
-            "references": [
-                "https://doi.org/10.1016/j.taap.2016.10.020"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -42554,39 +42548,41 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.taap.2016.10.020"
+            ],
+            "rights": null,
+            "title": "Locomotor activity and tissues levels following acute administration of lambda- and gamma-cyhalothrin in rats"
         },
         {
-            "title": "Tox_esterase_2016",
-            "description": "individual values for liver detoxification for each human sample and for each chemical. \n\nThis dataset is associated with the following publication:\nMoser, G., and S. Padilla. Esterase detoxification of acetylcholinesterase inhibitors using human liver samples in vitro.   TOXICOLOGY. Elsevier Science Ltd, New York, NY, USA,  11-20, (2016).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "A-str5-59",
-            "keyword": [
-                "pesticides",
-                "detoxification",
-                "esterases"
-            ],
             "contactPoint": {
                 "fn": "Virginia Moser",
                 "hasEmail": "mailto:moser.ginger@epa.gov"
             },
+            "description": "individual values for liver detoxification for each human sample and for each chemical. \n\nThis dataset is associated with the following publication:\nMoser, G., and S. Padilla. Esterase detoxification of acetylcholinesterase inhibitors using human liver samples in vitro.   TOXICOLOGY. Elsevier Science Ltd, New York, NY, USA,  11-20, (2016).",
             "distribution": [
                 {
-                    "title": "all human data for scihub.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/59/all%20human%20data%20for%20scihub.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "all human data for scihub.xlsx"
                 }
             ],
+            "identifier": "A-str5-59",
+            "keyword": [
+                "pesticides",
+                "detoxification",
+                "esterases"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2016-05-12",
-            "references": null,
+            "programCode": [
+                "020:000"
+            ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
                 "subOrganizationOf": {
@@ -42595,19 +42591,27 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": null,
+            "rights": null,
+            "title": "Tox_esterase_2016"
         },
         {
-            "title": "Neurophysiological assessment of auditory, peripheral nerve, somatosensory, and visual system function after developmental exposure to gasoline, E15, and E85 vapors.",
-            "description": "Visual, auditory, somatosensory, and peripheral nerve evoked responses. \n\nThis dataset is associated with the following publication:\nHerr , D., D. Freeborn , L. Degn , S.A. Martin, J. Ortenzio, L. Pantlin, C. Hamm , and W. Boyes. Neurophysiological Assessment of Auditory, Peripheral Nerve, Somatosensory, and Visual System Function After Developmental Exposure to Gasoline, E15 and E85 Vapors.   NEUROTOXICOLOGY AND TERATOLOGY. Elsevier Science Ltd, New York, NY, USA, 54: 78-88, (2016).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
+            "contactPoint": {
+                "fn": "David Herr",
+                "hasEmail": "mailto:herr.david@epa.gov"
+            },
+            "description": "Visual, auditory, somatosensory, and peripheral nerve evoked responses. \n\nThis dataset is associated with the following publication:\nHerr , D., D. Freeborn , L. Degn , S.A. Martin, J. Ortenzio, L. Pantlin, C. Hamm , and W. Boyes. Neurophysiological Assessment of Auditory, Peripheral Nerve, Somatosensory, and Visual System Function After Developmental Exposure to Gasoline, E15 and E85 Vapors.   NEUROTOXICOLOGY AND TERATOLOGY. Elsevier Science Ltd, New York, NY, USA, 54: 78-88, (2016).",
+            "distribution": [
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/145/A-98sp_BiofuelsE0E15E85_Data.zip",
+                    "mediaType": "application/x-zip-compressed",
+                    "title": "A-98sp_BiofuelsE0E15E85_Data.zip"
+                }
             ],
             "identifier": "A-98sp-145",
             "keyword": [
@@ -42622,20 +42626,10 @@
                 "vapors",
                 "neurophysiology"
             ],
-            "contactPoint": {
-                "fn": "David Herr",
-                "hasEmail": "mailto:herr.david@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "A-98sp_BiofuelsE0E15E85_Data.zip",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/145/A-98sp_BiofuelsE0E15E85_Data.zip",
-                    "mediaType": "application/x-zip-compressed"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2016-06-07",
-            "references": [
-                "https://doi.org/10.1016/j.ntt.2015.12.006"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -42645,50 +42639,50 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.ntt.2015.12.006"
+            ],
+            "rights": null,
+            "title": "Neurophysiological assessment of auditory, peripheral nerve, somatosensory, and visual system function after developmental exposure to gasoline, E15, and E85 vapors."
         },
         {
-            "title": "Ohmic resistance affects microbial community and electrochemical kinetics in a multi-anode microbial electrochemical cell ",
-            "description": "A-3txf_sequence summary.xksx: Abundance of contigs or unique sequences for each biofilm samples from anodes in the MEC reactor\nHodon Waterloo final_fasta_working.docx: Raw sequences with their identification numbers\nRNA S1_MEC.docx: Representative sequences with their ID number and taxonomy. \n\nThis dataset is associated with the following publication:\nSantodomingo, J., H. Ryu, B. Dhar, and H. Lee. Ohmic resistance affects microbial community and electrochemical kinetics in a multi-anode microbial electrochemical cell.   JOURNAL OF POWER SOURCES. Elsevier Science Ltd, New York, NY, USA, 331: 315-321, (2016).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "A-3txf-448",
-            "keyword": [
-                "Abundance",
-                "Raw sequences",
-                "Fasta file",
-                "Anode potential",
-                "Half-saturation anode potential",
-                "Microbial electrochemical cells",
-                "Multi-anode",
-                "Ohmic energy loss"
-            ],
             "contactPoint": {
                 "fn": "Hodon Ryu",
                 "hasEmail": "mailto:ryu.hodon@epa.gov"
             },
+            "description": "A-3txf_sequence summary.xksx: Abundance of contigs or unique sequences for each biofilm samples from anodes in the MEC reactor\nHodon Waterloo final_fasta_working.docx: Raw sequences with their identification numbers\nRNA S1_MEC.docx: Representative sequences with their ID number and taxonomy. \n\nThis dataset is associated with the following publication:\nSantodomingo, J., H. Ryu, B. Dhar, and H. Lee. Ohmic resistance affects microbial community and electrochemical kinetics in a multi-anode microbial electrochemical cell.   JOURNAL OF POWER SOURCES. Elsevier Science Ltd, New York, NY, USA, 331: 315-321, (2016).",
             "distribution": [
                 {
-                    "title": "Hodon Waterloo final_fasta_working.docx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/448/Hodon%20Waterloo%20final_fasta_working.docx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+                    "title": "Hodon Waterloo final_fasta_working.docx"
                 },
                 {
-                    "title": "RNA S1_MEC.docx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/448/RNA%20S1_MEC.docx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+                    "title": "RNA S1_MEC.docx"
                 }
             ],
+            "identifier": "A-3txf-448",
+            "keyword": [
+                "Abundance",
+                "Raw sequences",
+                "Fasta file",
+                "Anode potential",
+                "Half-saturation anode potential",
+                "Microbial electrochemical cells",
+                "Multi-anode",
+                "Ohmic energy loss"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2016-11-17",
-            "references": [
-                "http://www.sciencedirect.com/science/article/pii/S0378775316312174"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -42698,19 +42692,28 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "http://www.sciencedirect.com/science/article/pii/S0378775316312174"
+            ],
+            "rights": null,
+            "title": "Ohmic resistance affects microbial community and electrochemical kinetics in a multi-anode microbial electrochemical cell "
         },
         {
-            "title": "Sediment Resuspension Data",
-            "description": "The full report on sediment resuspension in drinking water storage tanks and a link to an animation of results. \n\nThis dataset is associated with the following publication:\nHo, C., R. Murray , J. Christian, E. Ching, J. Slavin, J. Ortega, and L. Rossman. Sediment Resuspension and Transport in Water Distribution Storage Tanks.   JOURNAL OF THE AMERICAN WATER WORKS ASSOCIATION. American Water Works Association, Denver, CO, USA, 108(6): ., (2016).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:060"
+            "contactPoint": {
+                "fn": "Regan Murray",
+                "hasEmail": "mailto:murray.regan@epa.gov"
+            },
+            "description": "The full report on sediment resuspension in drinking water storage tanks and a link to an animation of results. \n\nThis dataset is associated with the following publication:\nHo, C., R. Murray , J. Christian, E. Ching, J. Slavin, J. Ortega, and L. Rossman. Sediment Resuspension and Transport in Water Distribution Storage Tanks.   JOURNAL OF THE AMERICAN WATER WORKS ASSOCIATION. American Water Works Association, Denver, CO, USA, 108(6): ., (2016).",
+            "distribution": [
+                {
+                    "accessURL": "https://www.sandia.gov/cfd-water/sediment-resuspension-in-water-distribution-storage-tanks/",
+                    "title": "https://www.sandia.gov/cfd-water/sediment-resuspension-in-water-distribution-storage-tanks/"
+                }
             ],
             "identifier": "A-69pf-148",
             "keyword": [
@@ -42724,19 +42727,10 @@
                 "modeling",
                 "CFD"
             ],
-            "contactPoint": {
-                "fn": "Regan Murray",
-                "hasEmail": "mailto:murray.regan@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "https://www.sandia.gov/cfd-water/sediment-resuspension-in-water-distribution-storage-tanks/",
-                    "accessURL": "https://www.sandia.gov/cfd-water/sediment-resuspension-in-water-distribution-storage-tanks/"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2016-04-01",
-            "references": [
-                "https://doi.org/10.5942/jawwa.2016.108.0077"
+            "programCode": [
+                "020:060"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -42746,19 +42740,29 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.5942/jawwa.2016.108.0077"
+            ],
+            "rights": null,
+            "title": "Sediment Resuspension Data"
         },
         {
-            "title": "USEEIO Elementary Flows and Life Cycle Impact Assessment (LCIA) Characterization Factors",
-            "description": "This file contains all the elementary flows (defined in ISO 14044) used in the USEEIO model. The elementary flows come from a draft master list used by USEPA modified from the openLCA 1.4 software master list with original flows added. The characterization factors come from the openLCA 1.5.4 method pack or directly from TRACI 2.1 for the TRACI categories, or for the Non-TRACI categories, are originals used simply to sum up all types of resource use of a given type. \n\nThis dataset is associated with the following publication:\nYang, Y., W. Ingwersen, T. Hawkins, and D. Meyer. USEEIO: A new and transparent United States environmentally extended input-output model.   JOURNAL OF CLEANER PRODUCTION. Elsevier Science Ltd, New York, NY, USA, 158: 308-318, (2017).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:097"
+            "contactPoint": {
+                "fn": "Wesley Ingwersen",
+                "hasEmail": "mailto:ingwersen.wesley@epa.gov"
+            },
+            "description": "This file contains all the elementary flows (defined in ISO 14044) used in the USEEIO model. The elementary flows come from a draft master list used by USEPA modified from the openLCA 1.4 software master list with original flows added. The characterization factors come from the openLCA 1.5.4 method pack or directly from TRACI 2.1 for the TRACI categories, or for the Non-TRACI categories, are originals used simply to sum up all types of resource use of a given type. \n\nThis dataset is associated with the following publication:\nYang, Y., W. Ingwersen, T. Hawkins, and D. Meyer. USEEIO: A new and transparent United States environmentally extended input-output model.   JOURNAL OF CLEANER PRODUCTION. Elsevier Science Ltd, New York, NY, USA, 158: 308-318, (2017).",
+            "distribution": [
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/458/USEEIO_ElementaryFlows%26LCIAFactors.xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "USEEIO_ElementaryFlows&LCIAFactors.xlsx"
+                }
             ],
             "identifier": "A-sj4g-458",
             "keyword": [
@@ -42769,20 +42773,10 @@
                 "sustainability",
                 "input-output data"
             ],
-            "contactPoint": {
-                "fn": "Wesley Ingwersen",
-                "hasEmail": "mailto:ingwersen.wesley@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "USEEIO_ElementaryFlows&LCIAFactors.xlsx",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/458/USEEIO_ElementaryFlows%26LCIAFactors.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2016-12-07",
-            "references": [
-                "https://doi.org/10.1016/j.jclepro.2017.04.150"
+            "programCode": [
+                "020:097"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -42792,19 +42786,29 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.jclepro.2017.04.150"
+            ],
+            "rights": null,
+            "title": "USEEIO Elementary Flows and Life Cycle Impact Assessment (LCIA) Characterization Factors"
         },
         {
-            "title": "Data to support \"Boosted Regression Tree Models to Explain Watershed Nutrient Concentrations & Biological Condition\"",
-            "description": "Spreadsheets are included here to support the manuscript \"Boosted Regression Tree Models to Explain Watershed Nutrient Concentrations and Biological Condition\". \n\nThis dataset is associated with the following publication:\nGolden , H., C. Lane , A. Prues, and E. D'Amico. Boosted Regression Tree Models to Explain Watershed Nutrient Concentrations and Biological Condition.   JAWRA. American Water Resources Association, Middleburg, VA, USA, 52(5): 1251-1274, (2016).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:096"
+            "contactPoint": {
+                "fn": "Heather Golden",
+                "hasEmail": "mailto:golden.heather@epa.gov"
+            },
+            "description": "Spreadsheets are included here to support the manuscript \"Boosted Regression Tree Models to Explain Watershed Nutrient Concentrations and Biological Condition\". \n\nThis dataset is associated with the following publication:\nGolden , H., C. Lane , A. Prues, and E. D'Amico. Boosted Regression Tree Models to Explain Watershed Nutrient Concentrations and Biological Condition.   JAWRA. American Water Resources Association, Middleburg, VA, USA, 52(5): 1251-1274, (2016).",
+            "distribution": [
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/162/ScienceHubData_080416.zip",
+                    "mediaType": "application/x-zip-compressed",
+                    "title": "ScienceHubData_080416.zip"
+                }
             ],
             "identifier": "A-7pvt-162",
             "keyword": [
@@ -42816,20 +42820,10 @@
                 "Index of Biotic Integrity",
                 "statistical model"
             ],
-            "contactPoint": {
-                "fn": "Heather Golden",
-                "hasEmail": "mailto:golden.heather@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "ScienceHubData_080416.zip",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/162/ScienceHubData_080416.zip",
-                    "mediaType": "application/x-zip-compressed"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2014-11-10",
-            "references": [
-                "http://onlinelibrary.wiley.com/doi/10.1111/1752-1688.12447/abstract"
+            "programCode": [
+                "020:096"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -42839,19 +42833,31 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "http://onlinelibrary.wiley.com/doi/10.1111/1752-1688.12447/abstract"
+            ],
+            "rights": null,
+            "title": "Data to support \"Boosted Regression Tree Models to Explain Watershed Nutrient Concentrations & Biological Condition\""
         },
         {
-            "title": "USEEIO Satellite Files",
-            "description": "These files contain the environmental data as particular emissions or resources associated with a BEA sectors that are used in the USEEIO model. They are organized by the emission or resources type, as described in the manuscript. The main files (without SI) show the final \"satellite tables\" in the 'Exchanges' sheet which have emissions or resource use per USD for 2013. The other sheets in these files provide meta data for the create of the tables, including general information, sources, etc. The 'export' sheet is used for saving the satellite table for csv export. The data dictionary describes the fields in this sheet. The supporting files provide all the details data transformation and organization for the development of the satellite tables. \n\nThis dataset is associated with the following publication:\nYang, Y., W. Ingwersen, T. Hawkins, and D. Meyer. USEEIO: A new and transparent United States environmentally extended input-output model.   JOURNAL OF CLEANER PRODUCTION. Elsevier Science Ltd, New York, NY, USA, 158: 308-318, (2017).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:097"
+            "contactPoint": {
+                "fn": "Wesley Ingwersen",
+                "hasEmail": "mailto:ingwersen.wesley@epa.gov"
+            },
+            "describedBy": "https://pasteur.epa.gov/uploads/455/documents/USEEIO%20Data%20Dictionary.xlsx",
+            "describedByType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+            "description": "These files contain the environmental data as particular emissions or resources associated with a BEA sectors that are used in the USEEIO model. They are organized by the emission or resources type, as described in the manuscript. The main files (without SI) show the final \"satellite tables\" in the 'Exchanges' sheet which have emissions or resource use per USD for 2013. The other sheets in these files provide meta data for the create of the tables, including general information, sources, etc. The 'export' sheet is used for saving the satellite table for csv export. The data dictionary describes the fields in this sheet. The supporting files provide all the details data transformation and organization for the development of the satellite tables. \n\nThis dataset is associated with the following publication:\nYang, Y., W. Ingwersen, T. Hawkins, and D. Meyer. USEEIO: A new and transparent United States environmentally extended input-output model.   JOURNAL OF CLEANER PRODUCTION. Elsevier Science Ltd, New York, NY, USA, 158: 308-318, (2017).",
+            "distribution": [
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/455/USEEIO_Satellite_Tables.zip",
+                    "mediaType": "application/x-zip-compressed",
+                    "title": "USEEIO_Satellite_Tables.zip"
+                }
             ],
             "identifier": "A-sj4g-455",
             "keyword": [
@@ -42869,20 +42875,10 @@
                 "sustainability",
                 "input-output data"
             ],
-            "contactPoint": {
-                "fn": "Wesley Ingwersen",
-                "hasEmail": "mailto:ingwersen.wesley@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "USEEIO_Satellite_Tables.zip",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/455/USEEIO_Satellite_Tables.zip",
-                    "mediaType": "application/x-zip-compressed"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2016-12-01",
-            "references": [
-                "https://doi.org/10.1016/j.jclepro.2017.04.150"
+            "programCode": [
+                "020:097"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -42893,20 +42889,28 @@
                     }
                 }
             },
-            "describedBy": "https://pasteur.epa.gov/uploads/455/documents/USEEIO%20Data%20Dictionary.xlsx",
-            "describedByType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+            "references": [
+                "https://doi.org/10.1016/j.jclepro.2017.04.150"
+            ],
+            "rights": null,
+            "title": "USEEIO Satellite Files"
         },
         {
-            "title": "Mutagenicity of Whole Biodiesel Extracts in Salmonella",
-            "description": "Description is in the data set. \n\nThis dataset is associated with the following publication:\nMutlu, E., S. Warren , P. Matthews, C. King , L. Walsh , A. Kligerman, J. Schmid , D. Janek, I. Kooter, B. Linak , I. Gilmour , and D. DeMarini. Health Effects of Soy-Biodiesel Emissions: Mutagenicity-Emission Factors.   INHALATION TOXICOLOGY. Informa Healthcare USA, New York, NY, USA, 27(11): 585-596, (2015).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
+            "contactPoint": {
+                "fn": "David Demarini",
+                "hasEmail": "mailto:demarini.david@epa.gov"
+            },
+            "description": "Description is in the data set. \n\nThis dataset is associated with the following publication:\nMutlu, E., S. Warren , P. Matthews, C. King , L. Walsh , A. Kligerman, J. Schmid , D. Janek, I. Kooter, B. Linak , I. Gilmour , and D. DeMarini. Health Effects of Soy-Biodiesel Emissions: Mutagenicity-Emission Factors.   INHALATION TOXICOLOGY. Informa Healthcare USA, New York, NY, USA, 27(11): 585-596, (2015).",
+            "distribution": [
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/440/Science%20Hub%20Biodiesel%20Whole%20Extract%20data%20set.pdf",
+                    "mediaType": "application/pdf",
+                    "title": "Science Hub Biodiesel Whole Extract data set.pdf"
+                }
             ],
             "identifier": "A-fbgk-440",
             "keyword": [
@@ -42917,19 +42921,11 @@
                 "Combustion Emissions",
                 "Complex Mixtures"
             ],
-            "contactPoint": {
-                "fn": "David Demarini",
-                "hasEmail": "mailto:demarini.david@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "Science Hub Biodiesel Whole Extract data set.pdf",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/440/Science%20Hub%20Biodiesel%20Whole%20Extract%20data%20set.pdf",
-                    "mediaType": "application/pdf"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2016-02-12",
-            "references": null,
+            "programCode": [
+                "020:000"
+            ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
                 "subOrganizationOf": {
@@ -42938,19 +42934,27 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": null,
+            "rights": null,
+            "title": "Mutagenicity of Whole Biodiesel Extracts in Salmonella"
         },
         {
-            "title": "Liver steatosis study_PFAA treated mouse gene array data",
-            "description": "This file contains a link for Gene Expression Omnibus and the GSE designations for the publicly available gene expression data used in the study and reflected in Figures 6 and 7 for the Das et al., 2016 paper. \n\nThis dataset is associated with the following publication:\nDas, K., C. Wood, M. Lin, A.A. Starkov, C. Lau, K.B. Wallace, C. Corton, and B. Abbott. Perfluoroalky acids-induced liver steatosis:  Effects on genes controlling lipid homeostasis.   TOXICOLOGY. Elsevier Science Ltd, New York, NY, USA, 378: 32-52, (2017).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
+            "contactPoint": {
+                "fn": "Barbara Abbott",
+                "hasEmail": "mailto:abbott.barbara@epa.gov"
+            },
+            "description": "This file contains a link for Gene Expression Omnibus and the GSE designations for the publicly available gene expression data used in the study and reflected in Figures 6 and 7 for the Das et al., 2016 paper. \n\nThis dataset is associated with the following publication:\nDas, K., C. Wood, M. Lin, A.A. Starkov, C. Lau, K.B. Wallace, C. Corton, and B. Abbott. Perfluoroalky acids-induced liver steatosis:  Effects on genes controlling lipid homeostasis.   TOXICOLOGY. Elsevier Science Ltd, New York, NY, USA, 378: 32-52, (2017).",
+            "distribution": [
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/43/Data%20set%202%20Gene%20MicroArray%20analysis%20Das%20et%20al%202016.docx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+                    "title": "Data set 2 Gene MicroArray analysis Das et al 2016.docx"
+                }
             ],
             "identifier": "A-1zct-43",
             "keyword": [
@@ -42963,20 +42967,10 @@
                 "PFHxS",
                 "hepatotoxicity"
             ],
-            "contactPoint": {
-                "fn": "Barbara Abbott",
-                "hasEmail": "mailto:abbott.barbara@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "Data set 2 Gene MicroArray analysis Das et al 2016.docx",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/43/Data%20set%202%20Gene%20MicroArray%20analysis%20Das%20et%20al%202016.docx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2016-05-04",
-            "references": [
-                "https://doi.org/10.1016/j.tox.2016.12.007"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -42986,19 +42980,29 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.tox.2016.12.007"
+            ],
+            "rights": null,
+            "title": "Liver steatosis study_PFAA treated mouse gene array data"
         },
         {
-            "title": "Liver steatosis study_PFAA treated Wild type and PPAR KO mouse data",
-            "description": "Data set 1 consists of the experimental data for the Wild Type and PPAR KO animal study and includes data used to prepare Figures 1-4 and Table 1 of the Das et al, 2016 paper. \n\nThis dataset is associated with the following publication:\nDas, K., C. Wood, M. Lin, A.A. Starkov, C. Lau, K.B. Wallace, C. Corton, and B. Abbott. Perfluoroalky acids-induced liver steatosis:  Effects on genes controlling lipid homeostasis.   TOXICOLOGY. Elsevier Science Ltd, New York, NY, USA, 378: 32-52, (2017).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
+            "contactPoint": {
+                "fn": "Barbara Abbott",
+                "hasEmail": "mailto:abbott.barbara@epa.gov"
+            },
+            "description": "Data set 1 consists of the experimental data for the Wild Type and PPAR KO animal study and includes data used to prepare Figures 1-4 and Table 1 of the Das et al, 2016 paper. \n\nThis dataset is associated with the following publication:\nDas, K., C. Wood, M. Lin, A.A. Starkov, C. Lau, K.B. Wallace, C. Corton, and B. Abbott. Perfluoroalky acids-induced liver steatosis:  Effects on genes controlling lipid homeostasis.   TOXICOLOGY. Elsevier Science Ltd, New York, NY, USA, 378: 32-52, (2017).",
+            "distribution": [
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/42/Data%20set%201%20WT%20and%20KO%20data%20Das%20et%20al%202016.xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Data set 1 WT and KO data Das et al 2016.xlsx"
+                }
             ],
             "identifier": "A-1zct-42",
             "keyword": [
@@ -43017,20 +43021,10 @@
                 "PFHxS",
                 "hepatotoxicity"
             ],
-            "contactPoint": {
-                "fn": "Barbara Abbott",
-                "hasEmail": "mailto:abbott.barbara@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "Data set 1 WT and KO data Das et al 2016.xlsx",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/42/Data%20set%201%20WT%20and%20KO%20data%20Das%20et%20al%202016.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2016-05-04",
-            "references": [
-                "https://doi.org/10.1016/j.tox.2016.12.007"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -43040,46 +43034,46 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.tox.2016.12.007"
+            ],
+            "rights": null,
+            "title": "Liver steatosis study_PFAA treated Wild type and PPAR KO mouse data"
         },
         {
-            "title": "Scenarios for low carbon and low water electric power plant operations: implications for upstream water use",
-            "description": "The dataset includes all data used in the creation of figures and graphs in the paper: \"Scenarios for low carbon and low water electric power plant operations: implications for upstream water use.\"   Data includes regional electricity mixes, full life cycle water use, and water use for each life cycle stage.  These encompass a range of scenarios out to 2050, and should not be used as predictions, forecasts or official baselines.  The scenarios and results are for research purposes only, and do not represent current or future U.S. EPA policies or regulations. \n\nThis dataset is associated with the following publication:\nDodder , R., J. Barnwell , and W. Yelverton. Scenarios for low carbon and low water electric power plant operations: implications for upstream water use.   ENVIRONMENTAL SCIENCE & TECHNOLOGY. American Chemical Society, Washington, DC, USA, 50(21): 11460-11470, (2016).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:094"
-            ],
-            "identifier": "A-2v70-79",
-            "keyword": [
-                "water",
-                "water-",
-                "energy",
-                "energy system",
-                "energy modeling"
-            ],
             "contactPoint": {
                 "fn": "Rebecca Dodder",
                 "hasEmail": "mailto:dodder.rebecca@epa.gov"
             },
+            "description": "The dataset includes all data used in the creation of figures and graphs in the paper: \"Scenarios for low carbon and low water electric power plant operations: implications for upstream water use.\"   Data includes regional electricity mixes, full life cycle water use, and water use for each life cycle stage.  These encompass a range of scenarios out to 2050, and should not be used as predictions, forecasts or official baselines.  The scenarios and results are for research purposes only, and do not represent current or future U.S. EPA policies or regulations. \n\nThis dataset is associated with the following publication:\nDodder , R., J. Barnwell , and W. Yelverton. Scenarios for low carbon and low water electric power plant operations: implications for upstream water use.   ENVIRONMENTAL SCIENCE & TECHNOLOGY. American Chemical Society, Washington, DC, USA, 50(21): 11460-11470, (2016).",
             "distribution": [
                 {
-                    "title": "Water-energy_Dodder_ScienceHub_v2.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/79/Water-energy_Dodder_ScienceHub_v2.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Water-energy_Dodder_ScienceHub_v2.xlsx"
                 },
                 {
-                    "title": "https://pubs.acs.org/doi/suppl/10.1021/acs.est.6b03048",
-                    "accessURL": "https://pubs.acs.org/doi/suppl/10.1021/acs.est.6b03048"
+                    "accessURL": "https://pubs.acs.org/doi/suppl/10.1021/acs.est.6b03048",
+                    "title": "https://pubs.acs.org/doi/suppl/10.1021/acs.est.6b03048"
                 }
             ],
+            "identifier": "A-2v70-79",
+            "keyword": [
+                "water",
+                "water-",
+                "energy",
+                "energy system",
+                "energy modeling"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2016-05-18",
-            "references": [
-                "https://doi.org/10.1021/acs.est.6b03048"
+            "programCode": [
+                "020:094"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -43089,42 +43083,42 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1021/acs.est.6b03048"
+            ],
+            "rights": null,
+            "title": "Scenarios for low carbon and low water electric power plant operations: implications for upstream water use"
         },
         {
-            "title": "Supporting Information",
-            "description": "This is the supporting information for the journal article. \n\nThis dataset is associated with the following publication:\nRankin, K., S. Mabury, T. Jenkins, and J. Washington. A North American and global survey of perfluoroalkyl substances in surface soils: Distribution patterns and mode of occurrence.   CHEMOSPHERE. Elsevier Science Ltd, New York, NY, USA, 161: 333\u2013341, (2016).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "A-qjqm-141",
-            "keyword": [
-                "PFOA PFOS background soils"
-            ],
             "contactPoint": {
                 "fn": "John Washington",
                 "hasEmail": "mailto:washington.john@epa.gov"
             },
+            "description": "This is the supporting information for the journal article. \n\nThis dataset is associated with the following publication:\nRankin, K., S. Mabury, T. Jenkins, and J. Washington. A North American and global survey of perfluoroalkyl substances in surface soils: Distribution patterns and mode of occurrence.   CHEMOSPHERE. Elsevier Science Ltd, New York, NY, USA, 161: 333\u2013341, (2016).",
             "distribution": [
                 {
-                    "title": "160721 American-Global Soil PFASs SI.pdf",
                     "downloadURL": "https://pasteur.epa.gov/uploads/141/160721%20American-Global%20Soil%20PFASs%20SI.pdf",
-                    "mediaType": "application/pdf"
+                    "mediaType": "application/pdf",
+                    "title": "160721 American-Global Soil PFASs SI.pdf"
                 },
                 {
-                    "title": "https://www.sciencedirect.com/science/article/pii/S0045653516308803",
-                    "accessURL": "https://www.sciencedirect.com/science/article/pii/S0045653516308803"
+                    "accessURL": "https://www.sciencedirect.com/science/article/pii/S0045653516308803",
+                    "title": "https://www.sciencedirect.com/science/article/pii/S0045653516308803"
                 }
             ],
+            "identifier": "A-qjqm-141",
+            "keyword": [
+                "PFOA PFOS background soils"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2016-05-02",
-            "references": [
-                "https://doi.org/10.1016/j.chemosphere.2016.06.109"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -43134,19 +43128,28 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.chemosphere.2016.06.109"
+            ],
+            "rights": null,
+            "title": "Supporting Information"
         },
         {
-            "title": "Link to paper",
-            "description": "Link to the paper. \n\nThis dataset is associated with the following publication:\nNaile, J., A.W. Garrison, J. Avants, and J. Washington. Isomers/enantiomers of perfluorocarboxylic acids: Method development and detection in environmental samples.   CHEMOSPHERE. Elsevier Science Ltd, New York, NY, USA, 144: 1722-1728, (2016).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:095"
+            "contactPoint": {
+                "fn": "John Washington",
+                "hasEmail": "mailto:washington.john@epa.gov"
+            },
+            "description": "Link to the paper. \n\nThis dataset is associated with the following publication:\nNaile, J., A.W. Garrison, J. Avants, and J. Washington. Isomers/enantiomers of perfluorocarboxylic acids: Method development and detection in environmental samples.   CHEMOSPHERE. Elsevier Science Ltd, New York, NY, USA, 144: 1722-1728, (2016).",
+            "distribution": [
+                {
+                    "accessURL": "https://www.sciencedirect.com/science/article/pii/S0045653515302708",
+                    "title": "https://www.sciencedirect.com/science/article/pii/S0045653515302708"
+                }
             ],
             "identifier": "A-v6xj-276",
             "keyword": [
@@ -43158,18 +43161,11 @@
                 "Enantiomers",
                 "Enantioselectivity"
             ],
-            "contactPoint": {
-                "fn": "John Washington",
-                "hasEmail": "mailto:washington.john@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "https://www.sciencedirect.com/science/article/pii/S0045653515302708",
-                    "accessURL": "https://www.sciencedirect.com/science/article/pii/S0045653515302708"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2016-02-29",
-            "references": null,
+            "programCode": [
+                "020:095"
+            ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
                 "subOrganizationOf": {
@@ -43178,38 +43174,36 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": null,
+            "rights": null,
+            "title": "Link to paper"
         },
         {
-            "title": "Supporting Info",
-            "description": "Supporting Information. \n\nThis dataset is associated with the following publication:\nWashington , J., T. Jenkins, and E. Weber. Identification of Unsaturated and 2H Polyfluorocarboxylate Homologous Series and Their Detection in Environmental Samples and as Polymer Degradation Products.   ENVIRONMENTAL SCIENCE & TECHNOLOGY. American Chemical Society, Washington, DC, USA, 49(22): 13256-13263, (2015).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:095"
-            ],
-            "identifier": "A-t4bw-87",
-            "keyword": [
-                "uPFOA HPFOA uPFCA HPFCA"
-            ],
             "contactPoint": {
                 "fn": "John Washington",
                 "hasEmail": "mailto:washington.john@epa.gov"
             },
+            "description": "Supporting Information. \n\nThis dataset is associated with the following publication:\nWashington , J., T. Jenkins, and E. Weber. Identification of Unsaturated and 2H Polyfluorocarboxylate Homologous Series and Their Detection in Environmental Samples and as Polymer Degradation Products.   ENVIRONMENTAL SCIENCE & TECHNOLOGY. American Chemical Society, Washington, DC, USA, 49(22): 13256-13263, (2015).",
             "distribution": [
                 {
-                    "title": "151008 uPFOA Changes Accepted SI.docx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/87/151008%20uPFOA%20Changes%20Accepted%20SI.docx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+                    "title": "151008 uPFOA Changes Accepted SI.docx"
                 }
             ],
+            "identifier": "A-t4bw-87",
+            "keyword": [
+                "uPFOA HPFOA uPFCA HPFCA"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2015-10-08",
-            "references": [
-                "https://doi.org/10.1021/acs.est.5b03379"
+            "programCode": [
+                "020:095"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -43219,38 +43213,38 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1021/acs.est.5b03379"
+            ],
+            "rights": null,
+            "title": "Supporting Info"
         },
         {
-            "title": "Supporting Info",
-            "description": "Supporting Info. \n\nThis dataset is associated with the following publication:\nWashington , J., and T. Jenkins. Abiotic Hydrolysis of Fluorotelomer-Based Polymers as a Source of Perfluorocarboxylates at the Global Scale.   ENVIRONMENTAL SCIENCE & TECHNOLOGY. American Chemical Society, Washington, DC, USA, 49(24): 14129-14135, (2015).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:095"
-            ],
-            "identifier": "A-8938-86",
-            "keyword": [
-                "FTP PFOA"
-            ],
             "contactPoint": {
                 "fn": "John Washington",
                 "hasEmail": "mailto:washington.john@epa.gov"
             },
+            "description": "Supporting Info. \n\nThis dataset is associated with the following publication:\nWashington , J., and T. Jenkins. Abiotic Hydrolysis of Fluorotelomer-Based Polymers as a Source of Perfluorocarboxylates at the Global Scale.   ENVIRONMENTAL SCIENCE & TECHNOLOGY. American Chemical Society, Washington, DC, USA, 49(24): 14129-14135, (2015).",
             "distribution": [
                 {
-                    "title": "151027 WashingtonJenkinsFTPHydrolysisES&TSuppInfo.docx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/86/151027%20WashingtonJenkinsFTPHydrolysisES%26TSuppInfo.docx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+                    "title": "151027 WashingtonJenkinsFTPHydrolysisES&TSuppInfo.docx"
                 }
             ],
+            "identifier": "A-8938-86",
+            "keyword": [
+                "FTP PFOA"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2015-10-27",
-            "references": [
-                "https://doi.org/10.1021/acs.est.5b03686"
+            "programCode": [
+                "020:095"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -43260,19 +43254,29 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1021/acs.est.5b03686"
+            ],
+            "rights": null,
+            "title": "Supporting Info"
         },
         {
-            "title": "Future United States Domestic Water Demand  ",
-            "description": "Population projections, estimated per capita consumption rate, and estimated total annual water demand to 2100 for four future projections based off the IPCC SRES climate scenarios.  The estimates for water use are based Bayesian regression analysis on 1985, 1990, 1995, 2005 and 2010 water use from USGS. \n\nThis dataset is associated with the following publication:\nPickard, B., M. Nash, J. Baynes, and M. Mehaffey. Planning for community resilience to future United States domestic water demand.   LANDSCAPE AND URBAN PLANNING. Elsevier Science Ltd, New York, NY, USA, 158: 75-86, (2017).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
+            "contactPoint": {
+                "fn": "Megan Mehaffey",
+                "hasEmail": "mailto:mehaffey.megan@epa.gov"
+            },
+            "description": "Population projections, estimated per capita consumption rate, and estimated total annual water demand to 2100 for four future projections based off the IPCC SRES climate scenarios.  The estimates for water use are based Bayesian regression analysis on 1985, 1990, 1995, 2005 and 2010 water use from USGS. \n\nThis dataset is associated with the following publication:\nPickard, B., M. Nash, J. Baynes, and M. Mehaffey. Planning for community resilience to future United States domestic water demand.   LANDSCAPE AND URBAN PLANNING. Elsevier Science Ltd, New York, NY, USA, 158: 75-86, (2017).",
+            "distribution": [
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/193/LUP_Demand%20final%20datas%20and%20regressions.xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "LUP_Demand final datas and regressions.xlsx"
+                }
             ],
             "identifier": "A-xgz3-193",
             "keyword": [
@@ -43285,20 +43289,10 @@
                 "ecosystem services",
                 "Landscape Ecology"
             ],
-            "contactPoint": {
-                "fn": "Megan Mehaffey",
-                "hasEmail": "mailto:mehaffey.megan@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "LUP_Demand final datas and regressions.xlsx",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/193/LUP_Demand%20final%20datas%20and%20regressions.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2016-08-16",
-            "references": [
-                "https://doi.org/10.1016/j.landurbplan.2016.07.014"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -43308,46 +43302,46 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.landurbplan.2016.07.014"
+            ],
+            "rights": null,
+            "title": "Future United States Domestic Water Demand  "
         },
         {
-            "title": "Aquatic concentrations of chemical analytes compared to ecotoxicity estimates",
-            "description": "We describe screening level estimates of potential aquatic toxicity posed by 227 chemical analytes that were measured in 25 ambient water samples collected as part of a joint USGS/USEPA drinking water plant study. Measured concentrations were compared to biological effect concentration (EC) estimates, including USEPA aquatic life criteria, effective plasma concentrations of pharmaceuticals, published toxicity data summarized in the USEPA ECOTOX database, and chemical structure-based predictions. Potential dietary exposures were estimated using a generic 3-tiered food web accumulation scenario. \n\nThis dataset is associated with the following publication:\nKostich , M., R. Flick , A. Batt , H. Mash , S. Boone , E. Furlong, D. Kolpin, and S. Glassmeyer. Aquatic concentrations of chemical analytes compared to ecotoxicity estimates.   SCIENCE OF THE TOTAL ENVIRONMENT. Elsevier BV, AMSTERDAM,  NETHERLANDS, 579: 1649-1657, (2017).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:096"
-            ],
-            "identifier": "A-xd2v-243",
-            "keyword": [
-                "water",
-                "hazard ratio",
-                "ecotoxicity",
-                "chemical"
-            ],
             "contactPoint": {
                 "fn": "Mitchell Kostich",
                 "hasEmail": "mailto:kostich.mitchell@epa.gov"
             },
+            "description": "We describe screening level estimates of potential aquatic toxicity posed by 227 chemical analytes that were measured in 25 ambient water samples collected as part of a joint USGS/USEPA drinking water plant study. Measured concentrations were compared to biological effect concentration (EC) estimates, including USEPA aquatic life criteria, effective plasma concentrations of pharmaceuticals, published toxicity data summarized in the USEPA ECOTOX database, and chemical structure-based predictions. Potential dietary exposures were estimated using a generic 3-tiered food web accumulation scenario. \n\nThis dataset is associated with the following publication:\nKostich , M., R. Flick , A. Batt , H. Mash , S. Boone , E. Furlong, D. Kolpin, and S. Glassmeyer. Aquatic concentrations of chemical analytes compared to ecotoxicity estimates.   SCIENCE OF THE TOTAL ENVIRONMENT. Elsevier BV, AMSTERDAM,  NETHERLANDS, 579: 1649-1657, (2017).",
             "distribution": [
                 {
-                    "title": "Tables20160526a.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/243/Tables20160526a.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Tables20160526a.xlsx"
                 },
                 {
-                    "title": "InputData20160526a.xls",
                     "downloadURL": "https://pasteur.epa.gov/uploads/243/InputData20160526a.xls",
-                    "mediaType": "application/vnd.ms-excel"
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "InputData20160526a.xls"
                 }
             ],
+            "identifier": "A-xd2v-243",
+            "keyword": [
+                "water",
+                "hazard ratio",
+                "ecotoxicity",
+                "chemical"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2016-05-26",
-            "references": [
-                "https://doi.org/10.1016/j.scitotenv.2016.06.234"
+            "programCode": [
+                "020:096"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -43357,19 +43351,29 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.scitotenv.2016.06.234"
+            ],
+            "rights": null,
+            "title": "Aquatic concentrations of chemical analytes compared to ecotoxicity estimates"
         },
         {
-            "title": "Waterline ATS B. globigii spore water disinfection data",
-            "description": "Disinfection of B. globigii spores (a non-pathogenic surrogate for B. anthracis) in clean and dirty water using the ATS-Waterline system, which uses ultraviolet light and a charged membrane filter. \n\nThis dataset is associated with the following publication:\nSilva, G., J. Szabo, V. Namboodiri, R. Krishnan, J. Rodriguez, and A. Zeigler. Evaluation of and environmentally sustainable UV-assisted water treatment system for removal of Bacillus spores in water.   WATER SCIENCE AND TECHNOLOGY. IWA Publishing, London,  UK, 18(3): 968-975, (2018).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:060"
+            "contactPoint": {
+                "fn": "Jeffrey Szabo",
+                "hasEmail": "mailto:szabo.jeff@epa.gov"
+            },
+            "description": "Disinfection of B. globigii spores (a non-pathogenic surrogate for B. anthracis) in clean and dirty water using the ATS-Waterline system, which uses ultraviolet light and a charged membrane filter. \n\nThis dataset is associated with the following publication:\nSilva, G., J. Szabo, V. Namboodiri, R. Krishnan, J. Rodriguez, and A. Zeigler. Evaluation of and environmentally sustainable UV-assisted water treatment system for removal of Bacillus spores in water.   WATER SCIENCE AND TECHNOLOGY. IWA Publishing, London,  UK, 18(3): 968-975, (2018).",
+            "distribution": [
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/452/B.globigii%20bacterial%20counts%20and%20water%20quallity%20parameters.xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "B.globigii bacterial counts and water quallity parameters.xlsx"
+                }
             ],
             "identifier": "A-brvb-452",
             "keyword": [
@@ -43380,20 +43384,10 @@
                 "membrane filter",
                 "homeland security"
             ],
-            "contactPoint": {
-                "fn": "Jeffrey Szabo",
-                "hasEmail": "mailto:szabo.jeff@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "B.globigii bacterial counts and water quallity parameters.xlsx",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/452/B.globigii%20bacterial%20counts%20and%20water%20quallity%20parameters.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2016-11-25",
-            "references": [
-                "https://doi.org/10.2166/ws.2017.165"
+            "programCode": [
+                "020:060"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -43403,41 +43397,41 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.2166/ws.2017.165"
+            ],
+            "rights": null,
+            "title": "Waterline ATS B. globigii spore water disinfection data"
         },
         {
-            "title": "\u201cThe influence of control group reproduction on the statistical power of the Environmental Protection Agency\u2019s Medaka Extended One Generation Reproduction Test (MEOGRT) data for simulations\u201d Dataset",
-            "description": "Excel spreadsheet that contains the raw fecundity data used to conduct power simulations specific to the MEOGRT reproductive assessment. \n\nThis dataset is associated with the following publication:\nFlynn, K., J. Swintek, and R. Johnson. The influence of control group reproduction on the statistical power of the Environmental Protection Agency&rsquo;s medaka Extended One-Generation Reproduction Test (MEOGRT).   ECOTOXICOLOGY AND ENVIRONMENTAL SAFETY. Elsevier Science Ltd,  NY, USA, 136: 8-13, (2016).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:095"
-            ],
-            "identifier": "A-rv1s-446",
-            "keyword": [
-                "statistical power",
-                "endocrine disruption",
-                "fish",
-                "aquatic toxicity"
-            ],
             "contactPoint": {
                 "fn": "Kevin Flynn",
                 "hasEmail": "mailto:flynn.kevin@epa.gov"
             },
+            "description": "Excel spreadsheet that contains the raw fecundity data used to conduct power simulations specific to the MEOGRT reproductive assessment. \n\nThis dataset is associated with the following publication:\nFlynn, K., J. Swintek, and R. Johnson. The influence of control group reproduction on the statistical power of the Environmental Protection Agency&rsquo;s medaka Extended One-Generation Reproduction Test (MEOGRT).   ECOTOXICOLOGY AND ENVIRONMENTAL SAFETY. Elsevier Science Ltd,  NY, USA, 136: 8-13, (2016).",
             "distribution": [
                 {
-                    "title": "Flynn et al 2016 Science Hub.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/446/Flynn%20et%20al%202016%20Science%20Hub.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Flynn et al 2016 Science Hub.xlsx"
                 }
             ],
+            "identifier": "A-rv1s-446",
+            "keyword": [
+                "statistical power",
+                "endocrine disruption",
+                "fish",
+                "aquatic toxicity"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2015-12-03",
-            "references": [
-                "http://dx.doi.org/10.1016/j.ecoenv.2016.10.024"
+            "programCode": [
+                "020:095"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -43447,19 +43441,29 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "http://dx.doi.org/10.1016/j.ecoenv.2016.10.024"
+            ],
+            "rights": null,
+            "title": "\u201cThe influence of control group reproduction on the statistical power of the Environmental Protection Agency\u2019s Medaka Extended One Generation Reproduction Test (MEOGRT) data for simulations\u201d Dataset"
         },
         {
-            "title": "A demonstration of the uncertainty in predicting the estrogenic activity of individual chemicals and mixtures from an in vitro estrogen receptor transcriptional activation assay (T47D-KBluc) to the in vivo uterotrophic assay using oral exposure",
-            "description": "the data set contains the figures and tables from the publication in addition to the means, standard errors of the mean and the sample sizes used in each group for every experiment.  the data set also contains a description of the genes, their function and acronyms on the QPCR arrays used in the study.  Finally, the dataset includes the histopathology reports on the uterine changes induced by the different chemicals and the criteria used by the pathologist to classify the estrogenic effects of the chemicals. \n\nThis dataset is associated with the following publication:\nConley, J., B. Hannas, V. Wilson, E. Gray, and J. Furr. A demonstration of the uncertainty in predicting the estrogenic activity of individual chemicals and mixtures from an in vitro estrogen receptor transcriptional activation assay (T47D-KBluc) to the in vivo uterotrophic assay using oral exposure.   TOXICOLOGICAL SCIENCES. Society of Toxicology,     382-395, (2016).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:095"
+            "contactPoint": {
+                "fn": "Justin Conley",
+                "hasEmail": "mailto:conley.justin@epa.gov"
+            },
+            "description": "the data set contains the figures and tables from the publication in addition to the means, standard errors of the mean and the sample sizes used in each group for every experiment.  the data set also contains a description of the genes, their function and acronyms on the QPCR arrays used in the study.  Finally, the dataset includes the histopathology reports on the uterine changes induced by the different chemicals and the criteria used by the pathologist to classify the estrogenic effects of the chemicals. \n\nThis dataset is associated with the following publication:\nConley, J., B. Hannas, V. Wilson, E. Gray, and J. Furr. A demonstration of the uncertainty in predicting the estrogenic activity of individual chemicals and mixtures from an in vitro estrogen receptor transcriptional activation assay (T47D-KBluc) to the in vivo uterotrophic assay using oral exposure.   TOXICOLOGICAL SCIENCES. Society of Toxicology,     382-395, (2016).",
+            "distribution": [
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/428/Conley_IVIVE_Science%20hub%20file%20final%2010%203%202016.docx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+                    "title": "Conley_IVIVE_Science hub file final 10 3 2016.docx"
+                }
             ],
             "identifier": "A-280k-428",
             "keyword": [
@@ -43472,20 +43476,10 @@
                 "in vitro to in vivo extrapolation",
                 "uterine estrogenic response"
             ],
-            "contactPoint": {
-                "fn": "Justin Conley",
-                "hasEmail": "mailto:conley.justin@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "Conley_IVIVE_Science hub file final 10 3 2016.docx",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/428/Conley_IVIVE_Science%20hub%20file%20final%2010%203%202016.docx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2016-10-03",
-            "references": [
-                "https://doi.org/10.1093/toxsci/kfw134"
+            "programCode": [
+                "020:095"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -43495,41 +43489,41 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1093/toxsci/kfw134"
+            ],
+            "rights": null,
+            "title": "A demonstration of the uncertainty in predicting the estrogenic activity of individual chemicals and mixtures from an in vitro estrogen receptor transcriptional activation assay (T47D-KBluc) to the in vivo uterotrophic assay using oral exposure"
         },
         {
-            "title": "Potential Vorticity based parameterization for specification of Upper troposphere/lower stratosphere ozone in atmospheric models",
-            "description": "Potential Vorticity based parameterization for specification of Upper troposphere/lower stratosphere ozone in atmospheric models - the data set consists of 3D O3 fields from the CMAQ modeling system across the northern hemisphere,  potential vorticity fields from the WRF model, and observated ozone from the WOUDC ozonesonde launches. \n\nThis dataset is associated with the following publication:\nMathur, R., J. Pleim, C. Hogrefe, M. Gan, G. Sarwar, D. Wong, J. Wang, S. McKeen, J. Xing, and J. Wang. Representing the effects of stratosphere\u2013troposphere exchange on 3-D O3 distributions in chemistry transport models using a potential vorticity-based parameterization.   Atmospheric Chemistry and Physics. Copernicus Publications, Katlenburg-Lindau,  GERMANY, 16: 10865-10877, (2016).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:094"
-            ],
-            "identifier": "A-ffbt-207",
-            "keyword": [
-                "stratosphere-troposphere exchange",
-                "Ozone",
-                "CMAQ",
-                "Potential vorticity"
-            ],
             "contactPoint": {
                 "fn": "Rohit Mathur",
                 "hasEmail": "mailto:mathur.rohit@epa.gov"
             },
+            "description": "Potential Vorticity based parameterization for specification of Upper troposphere/lower stratosphere ozone in atmospheric models - the data set consists of 3D O3 fields from the CMAQ modeling system across the northern hemisphere,  potential vorticity fields from the WRF model, and observated ozone from the WOUDC ozonesonde launches. \n\nThis dataset is associated with the following publication:\nMathur, R., J. Pleim, C. Hogrefe, M. Gan, G. Sarwar, D. Wong, J. Wang, S. McKeen, J. Xing, and J. Wang. Representing the effects of stratosphere\u2013troposphere exchange on 3-D O3 distributions in chemistry transport models using a potential vorticity-based parameterization.   Atmospheric Chemistry and Physics. Copernicus Publications, Katlenburg-Lindau,  GERMANY, 16: 10865-10877, (2016).",
             "distribution": [
                 {
-                    "title": "PV_Fig_plot_data_location_updated.docx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/207/PV_Fig_plot_data_location_updated.docx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+                    "title": "PV_Fig_plot_data_location_updated.docx"
                 }
             ],
+            "identifier": "A-ffbt-207",
+            "keyword": [
+                "stratosphere-troposphere exchange",
+                "Ozone",
+                "CMAQ",
+                "Potential vorticity"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2016-07-11",
-            "references": [
-                "https://doi.org/10.5194/acp-16-10865-2016"
+            "programCode": [
+                "020:094"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -43539,47 +43533,47 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.5194/acp-16-10865-2016"
+            ],
+            "rights": null,
+            "title": "Potential Vorticity based parameterization for specification of Upper troposphere/lower stratosphere ozone in atmospheric models"
         },
         {
-            "title": "Phoenix Study",
-            "description": "Phoenix Traffic and Mobile Data. \n\nThis dataset is associated with the following publication:\nBaldauf , R., V. Isakov , P. Deshmukh, and A. Venkatram. Influence of Solid Noise Barriers on Near-Road and On-Road Air Quality.   ATMOSPHERIC ENVIRONMENT. Elsevier Science Ltd, New York, NY, USA, 129: 265-276, (2016).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:094"
-            ],
-            "identifier": "A-vmdh-416",
-            "keyword": [
-                "air quality",
-                "near road",
-                "noise barriers",
-                "emissions",
-                "traffic"
-            ],
             "contactPoint": {
                 "fn": "Vladilen Isakov",
                 "hasEmail": "mailto:isakov.vlad@epa.gov"
             },
+            "description": "Phoenix Traffic and Mobile Data. \n\nThis dataset is associated with the following publication:\nBaldauf , R., V. Isakov , P. Deshmukh, and A. Venkatram. Influence of Solid Noise Barriers on Near-Road and On-Road Air Quality.   ATMOSPHERIC ENVIRONMENT. Elsevier Science Ltd, New York, NY, USA, 129: 265-276, (2016).",
             "distribution": [
                 {
-                    "title": "Phoenix Traffic Data Analysis.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/416/Phoenix%20Traffic%20Data%20Analysis.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Phoenix Traffic Data Analysis.xlsx"
                 },
                 {
-                    "title": "Phoenix Open_Barrier Data Analysis.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/416/Phoenix%20Open_Barrier%20Data%20Analysis.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Phoenix Open_Barrier Data Analysis.xlsx"
                 }
             ],
+            "identifier": "A-vmdh-416",
+            "keyword": [
+                "air quality",
+                "near road",
+                "noise barriers",
+                "emissions",
+                "traffic"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2014-10-21",
-            "references": [
-                "https://doi.org/10.1016/j.atmosenv.2016.01.025"
+            "programCode": [
+                "020:094"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -43589,19 +43583,29 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.atmosenv.2016.01.025"
+            ],
+            "rights": null,
+            "title": "Phoenix Study"
         },
         {
-            "title": "Figures",
-            "description": "data for figures 1-8 in journal article \"Assessment of port-related air quality impacts: geographic analysis of population\", International Journal of Environment and Pollution, 58, 231-250, (2015). \n\nThis dataset is associated with the following publication:\nArunachalam , S., H. Brantley , T. Barzyk , G. Hagler , V. Isakov , S. Kimbrough , B. Naess, N. Rice, M. Snyder, K. Talgo, and A. Venkatram. Assessment of port-related air quality impacts: geographic analysis of population.   INTERNATIONAL JOURNAL OF ENVIRONMENT AND POLLUTION. Inderscience Enterprises Limited, Geneva,  SWITZERLAND, 58(4): 231 - 250, (2015).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:097"
+            "contactPoint": {
+                "fn": "Vladilen Isakov",
+                "hasEmail": "mailto:isakov.vlad@epa.gov"
+            },
+            "description": "data for figures 1-8 in journal article \"Assessment of port-related air quality impacts: geographic analysis of population\", International Journal of Environment and Pollution, 58, 231-250, (2015). \n\nThis dataset is associated with the following publication:\nArunachalam , S., H. Brantley , T. Barzyk , G. Hagler , V. Isakov , S. Kimbrough , B. Naess, N. Rice, M. Snyder, K. Talgo, and A. Venkatram. Assessment of port-related air quality impacts: geographic analysis of population.   INTERNATIONAL JOURNAL OF ENVIRONMENT AND POLLUTION. Inderscience Enterprises Limited, Geneva,  SWITZERLAND, 58(4): 231 - 250, (2015).",
+            "distribution": [
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/208/Figures1to8.zip",
+                    "mediaType": "application/x-zip-compressed",
+                    "title": "Figures1to8.zip"
+                }
             ],
             "identifier": "A-hqcc-208",
             "keyword": [
@@ -43613,20 +43617,10 @@
                 "Population",
                 "exposure"
             ],
-            "contactPoint": {
-                "fn": "Vladilen Isakov",
-                "hasEmail": "mailto:isakov.vlad@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "Figures1to8.zip",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/208/Figures1to8.zip",
-                    "mediaType": "application/x-zip-compressed"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2014-12-18",
-            "references": [
-                "https://doi.org/10.1504/ijep.2015.077455"
+            "programCode": [
+                "020:097"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -43636,77 +43630,79 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1504/ijep.2015.077455"
+            ],
+            "rights": null,
+            "title": "Figures"
         },
         {
-            "title": "Detroit Exposure and Aerosol Research Study",
-            "description": "The DEARS represents a multipollutant spatial characterization of six neighborhoods and their residents in and around Detroit, Michigan.  Personal, residential indoor, residential outdoor, and ambient monitoring was performed.  Survey information was collected simultaneously with air quality monitoring to provide the means to examine a wide variety of exposure factors on personal exposure. \n\nThis dataset is associated with the following publication:\nLogue, J., M. Sherman, M. Lunden, N. Klepeis, R. Williams , C. Croghan , and B. Singer. Development and assessment of a physics-based simulation model to investigate residential PM2.5 infiltration across the US housing stock.   BUILDING AND ENVIRONMENT. Elsevier Science Ltd, New York, NY, USA, 94(1): 21-32, (2015).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:094"
-            ],
-            "identifier": "A-ttfk-15",
-            "keyword": [
-                "DEARS",
-                "personal",
-                "residential",
-                "particulate matter",
-                "ambient",
-                "air quality"
-            ],
             "contactPoint": {
                 "fn": "Ronald Williams",
                 "hasEmail": "mailto:williams.ronald@epa.gov"
             },
+            "describedBy": "https://pasteur.epa.gov/uploads/15/documents/dictionary.csv",
+            "describedByType": "text/csv",
+            "description": "The DEARS represents a multipollutant spatial characterization of six neighborhoods and their residents in and around Detroit, Michigan.  Personal, residential indoor, residential outdoor, and ambient monitoring was performed.  Survey information was collected simultaneously with air quality monitoring to provide the means to examine a wide variety of exposure factors on personal exposure. \n\nThis dataset is associated with the following publication:\nLogue, J., M. Sherman, M. Lunden, N. Klepeis, R. Williams , C. Croghan , and B. Singer. Development and assessment of a physics-based simulation model to investigate residential PM2.5 infiltration across the US housing stock.   BUILDING AND ENVIRONMENT. Elsevier Science Ltd, New York, NY, USA, 94(1): 21-32, (2015).",
             "distribution": [
                 {
-                    "title": "fuqdoors.csv",
                     "downloadURL": "https://pasteur.epa.gov/uploads/15/fuqdoors.csv",
-                    "mediaType": "application/vnd.ms-excel"
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "fuqdoors.csv"
                 },
                 {
-                    "title": "fuqETS.csv",
                     "downloadURL": "https://pasteur.epa.gov/uploads/15/fuqETS.csv",
-                    "mediaType": "application/vnd.ms-excel"
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "fuqETS.csv"
                 },
                 {
-                    "title": "fuqwindowfan.csv",
                     "downloadURL": "https://pasteur.epa.gov/uploads/15/fuqwindowfan.csv",
-                    "mediaType": "application/vnd.ms-excel"
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "fuqwindowfan.csv"
                 },
                 {
-                    "title": "fuqwindows.csv",
                     "downloadURL": "https://pasteur.epa.gov/uploads/15/fuqwindows.csv",
-                    "mediaType": "application/vnd.ms-excel"
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "fuqwindows.csv"
                 },
                 {
-                    "title": "fuqbase.csv",
                     "downloadURL": "https://pasteur.epa.gov/uploads/15/fuqbase.csv",
-                    "mediaType": "application/vnd.ms-excel"
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "fuqbase.csv"
                 },
                 {
-                    "title": "pmall.csv",
                     "downloadURL": "https://pasteur.epa.gov/uploads/15/pmall.csv",
-                    "mediaType": "application/vnd.ms-excel"
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "pmall.csv"
                 },
                 {
-                    "title": "residence.csv",
                     "downloadURL": "https://pasteur.epa.gov/uploads/15/residence.csv",
-                    "mediaType": "application/vnd.ms-excel"
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "residence.csv"
                 },
                 {
-                    "title": "https://archive.epa.gov/heasd/archive-dears/web/html/info-2.html",
-                    "accessURL": "https://archive.epa.gov/heasd/archive-dears/web/html/info-2.html"
+                    "accessURL": "https://archive.epa.gov/heasd/archive-dears/web/html/info-2.html",
+                    "title": "https://archive.epa.gov/heasd/archive-dears/web/html/info-2.html"
                 }
             ],
+            "identifier": "A-ttfk-15",
+            "keyword": [
+                "DEARS",
+                "personal",
+                "residential",
+                "particulate matter",
+                "ambient",
+                "air quality"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2014-11-12",
-            "references": [
-                "https://doi.org/10.1016/j.buildenv.2015.06.032"
+            "programCode": [
+                "020:094"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -43717,21 +43713,23 @@
                     }
                 }
             },
-            "describedBy": "https://pasteur.epa.gov/uploads/15/documents/dictionary.csv",
-            "describedByType": "text/csv"
+            "references": [
+                "https://doi.org/10.1016/j.buildenv.2015.06.032"
+            ],
+            "rights": null,
+            "title": "Detroit Exposure and Aerosol Research Study"
         },
         {
-            "title": "Insights into the deterministic skill of air quality ensembles from the analysis of AQMEII data",
-            "description": "This dataset documents the source of the data analyzed in the manuscript \" Insights into the deterministic skill of air quality ensembles from the analysis of AQMEII data\" led by Dr. Ioannis Kioutsioukis of the European Commission's Joint Research Center. All of the data were contributed by non-EPA research groups from Europe. This dataset is not publicly accessible because: None of the data analyzed in this manuscript was contributed by EPA. It can be accessed through the following means: The datasets used for analysis by the external author of this manuscript were provided by researchers from more than ten non-EPA research groups from Europe participating in the first and second phase of the Air Quality Model Evaluation International Initiative (AQMEII). All data used in the manuscript are stored on the web-based password-protected ENSEMBLE platform hosted by the European Commission\u2019s Joint Research Centre at http://ensemble3.jrc.it/. Interested researchers can request access to the AQMEII dataset hosted on the ENSEMBLE platform by contacting Dr. Stefano Galmarini (stefano.galmarini@jrc.ec.europa.eu). Format: N/A. \n\nThis dataset is associated with the following publication:\nKioutsioukis, I., U. Im, E. Solazzo, R. Bianconi, A. Badia, A. Balzarini, R. Baro, R. Bellasio, D. Brunner, C. Chemel, G. Curci, H. Denier va der Gon, J. Flemming, R. Forkel, L. Giordano, P. Jimenez-Guerrero, M. Hirtl, O. Jorba, A. Manders-Groot, L. Neal, J. Perez, G. Pirovano, R. San Jose, N. Savage, W. Schroder, R. Sokhi, D. Syrakov, P. Tuccella, J. Werhahn, R. Wolke, C. Hogrefe, and S. Galmarini. Insights into the deterministic skill of air quality ensembles from the analysis of AQMEII data.   Atmospheric Chemistry and Physics. Copernicus Publications, Katlenburg-Lindau,  GERMANY, 16(24): 15629-15652, (2016).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:094"
-            ],
+            "contactPoint": {
+                "fn": "Christian Hogrefe",
+                "hasEmail": "mailto:hogrefe.christian@epa.gov"
+            },
+            "description": "This dataset documents the source of the data analyzed in the manuscript \" Insights into the deterministic skill of air quality ensembles from the analysis of AQMEII data\" led by Dr. Ioannis Kioutsioukis of the European Commission's Joint Research Center. All of the data were contributed by non-EPA research groups from Europe. This dataset is not publicly accessible because: None of the data analyzed in this manuscript was contributed by EPA. It can be accessed through the following means: The datasets used for analysis by the external author of this manuscript were provided by researchers from more than ten non-EPA research groups from Europe participating in the first and second phase of the Air Quality Model Evaluation International Initiative (AQMEII). All data used in the manuscript are stored on the web-based password-protected ENSEMBLE platform hosted by the European Commission\u2019s Joint Research Centre at http://ensemble3.jrc.it/. Interested researchers can request access to the AQMEII dataset hosted on the ENSEMBLE platform by contacting Dr. Stefano Galmarini (stefano.galmarini@jrc.ec.europa.eu). Format: N/A. \n\nThis dataset is associated with the following publication:\nKioutsioukis, I., U. Im, E. Solazzo, R. Bianconi, A. Badia, A. Balzarini, R. Baro, R. Bellasio, D. Brunner, C. Chemel, G. Curci, H. Denier va der Gon, J. Flemming, R. Forkel, L. Giordano, P. Jimenez-Guerrero, M. Hirtl, O. Jorba, A. Manders-Groot, L. Neal, J. Perez, G. Pirovano, R. San Jose, N. Savage, W. Schroder, R. Sokhi, D. Syrakov, P. Tuccella, J. Werhahn, R. Wolke, C. Hogrefe, and S. Galmarini. Insights into the deterministic skill of air quality ensembles from the analysis of AQMEII data.   Atmospheric Chemistry and Physics. Copernicus Publications, Katlenburg-Lindau,  GERMANY, 16(24): 15629-15652, (2016).",
+            "distribution": [],
             "identifier": "A-3n5x-494",
             "keyword": [
                 "ensemble modeling ensemble averaging",
@@ -43739,14 +43737,10 @@
                 "AQMEII",
                 "air quality forecasting"
             ],
-            "contactPoint": {
-                "fn": "Christian Hogrefe",
-                "hasEmail": "mailto:hogrefe.christian@epa.gov"
-            },
-            "distribution": [],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2014-01-01",
-            "references": [
-                "https://doi.org/10.5194/acp-16-15629-2016"
+            "programCode": [
+                "020:094"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -43756,19 +43750,31 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.5194/acp-16-15629-2016"
+            ],
+            "rights": null,
+            "title": "Insights into the deterministic skill of air quality ensembles from the analysis of AQMEII data"
         },
         {
-            "title": "Excel file of salivary antibody analysis for Boqueron Beach study, Puerto Rico for six waterborne pathogens.",
-            "description": "This dataset is the raw Luminex antibody responses to six common waterborne pathogens reported in MFI (Median Fluorescence Intensity) units. \n\nThis dataset is associated with the following publication:\nAugustine , S., T. Eason , K. Simmons, C. Curioso, S. Griffin , M. Ramudit, and T. Plunkett. Developing a Salivary Antibody Multiplex Immunoassay to Measure Human Exposure to Environmental Pathogens.   Journal of Visualized Experiments. JoVE, Somerville, MA, USA, 115: e54415, (2016).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:096"
+            "contactPoint": {
+                "fn": "Swinburne Augustine",
+                "hasEmail": "mailto:augustine.swinburne@epa.gov"
+            },
+            "describedBy": "https://pasteur.epa.gov/uploads/136/documents/Data%20dictionary_saliva%20JoVE.xlsx",
+            "describedByType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+            "description": "This dataset is the raw Luminex antibody responses to six common waterborne pathogens reported in MFI (Median Fluorescence Intensity) units. \n\nThis dataset is associated with the following publication:\nAugustine , S., T. Eason , K. Simmons, C. Curioso, S. Griffin , M. Ramudit, and T. Plunkett. Developing a Salivary Antibody Multiplex Immunoassay to Measure Human Exposure to Environmental Pathogens.   Journal of Visualized Experiments. JoVE, Somerville, MA, USA, 115: e54415, (2016).",
+            "distribution": [
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/136/Copy%20of%20JOVE%206Ag%28raw%20data%20only%29.xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Copy of JOVE 6Ag(raw data only).xlsx"
+                }
             ],
             "identifier": "A-k0ph-136",
             "keyword": [
@@ -43782,20 +43788,10 @@
                 "bead coupling",
                 "coupling confirmation"
             ],
-            "contactPoint": {
-                "fn": "Swinburne Augustine",
-                "hasEmail": "mailto:augustine.swinburne@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "Copy of JOVE 6Ag(raw data only).xlsx",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/136/Copy%20of%20JOVE%206Ag%28raw%20data%20only%29.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2015-09-04",
-            "references": [
-                "https://doi.org/10.3791/54415"
+            "programCode": [
+                "020:096"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -43806,44 +43802,42 @@
                     }
                 }
             },
-            "describedBy": "https://pasteur.epa.gov/uploads/136/documents/Data%20dictionary_saliva%20JoVE.xlsx",
-            "describedByType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+            "references": [
+                "https://doi.org/10.3791/54415"
+            ],
+            "rights": null,
+            "title": "Excel file of salivary antibody analysis for Boqueron Beach study, Puerto Rico for six waterborne pathogens."
         },
         {
-            "title": "Significance of dissolved methane in effluents of anaerobically treated low strength wastewater and potential for recovery as an energy product: A review",
-            "description": "The data set includes estimations of energy required for processes related to the operation of Anaerobic Membrane Bioreactors. \n\nThis dataset is associated with the following publication:\nCrone, B., J. Garland, G. Sorial, and L. Vane. Significance of dissolved methane in effluents of anaerobically treated low strength wastewater and potential for recovery as an energy product: A review.   WATER RESEARCH. Elsevier Science Ltd, New York, NY, USA, 104: 520-531, (2016).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:096"
-            ],
-            "identifier": "A-hx3w-371",
-            "keyword": [
-                "Anaerobic Treatment",
-                "energy and water"
-            ],
             "contactPoint": {
                 "fn": "Jay Garland",
                 "hasEmail": "mailto:garland.jay@epa.gov"
             },
+            "description": "The data set includes estimations of energy required for processes related to the operation of Anaerobic Membrane Bioreactors. \n\nThis dataset is associated with the following publication:\nCrone, B., J. Garland, G. Sorial, and L. Vane. Significance of dissolved methane in effluents of anaerobically treated low strength wastewater and potential for recovery as an energy product: A review.   WATER RESEARCH. Elsevier Science Ltd, New York, NY, USA, 104: 520-531, (2016).",
             "distribution": [
                 {
-                    "title": "Science Hub Data Submission.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/371/Science%20Hub%20Data%20Submission.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Science Hub Data Submission.xlsx"
                 },
                 {
-                    "title": "https://www.sciencedirect.com/science/article/pii/S0043135416306194",
-                    "accessURL": "https://www.sciencedirect.com/science/article/pii/S0043135416306194"
+                    "accessURL": "https://www.sciencedirect.com/science/article/pii/S0043135416306194",
+                    "title": "https://www.sciencedirect.com/science/article/pii/S0043135416306194"
                 }
             ],
+            "identifier": "A-hx3w-371",
+            "keyword": [
+                "Anaerobic Treatment",
+                "energy and water"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2016-09-19",
-            "references": [
-                "https://doi.org/10.1016/j.watres.2016.08.019"
+            "programCode": [
+                "020:096"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -43853,19 +43847,29 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.watres.2016.08.019"
+            ],
+            "rights": null,
+            "title": "Significance of dissolved methane in effluents of anaerobically treated low strength wastewater and potential for recovery as an energy product: A review"
         },
         {
-            "title": "LenoxKaplan_Role of natural gas in meeting electric sector emissions reduction strategy_dataset",
-            "description": "This dataset is for an analysis that used the MARKAL linear optimization model to compare the carbon emissions profiles and system-wide global warming potential of the U.S. energy system over a series of model runs in which the power sector is required to meet a specific carbon dioxide reduction target across a number of scenarios in which the availability of natural gas changes.  Scenarios are run with carbon dioxide emissions and a range of upstream methane emission leakage rates from natural gas production along with upstream methane and carbon dioxide emissions associated with production of coal and oil. \n\nThis dataset is associated with the following publication:\nLenox , C., and O. Kaplan. Role of natural gas in meeting an electric sector emissions reduction strategy and effects on greenhouse gas emissions.   Energy Economics. Elsevier B.V., Amsterdam,  NETHERLANDS, 60: 460-468, (2016).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:094"
+            "contactPoint": {
+                "fn": "Carol Lenox",
+                "hasEmail": "mailto:lenox.carol@epa.gov"
+            },
+            "description": "This dataset is for an analysis that used the MARKAL linear optimization model to compare the carbon emissions profiles and system-wide global warming potential of the U.S. energy system over a series of model runs in which the power sector is required to meet a specific carbon dioxide reduction target across a number of scenarios in which the availability of natural gas changes.  Scenarios are run with carbon dioxide emissions and a range of upstream methane emission leakage rates from natural gas production along with upstream methane and carbon dioxide emissions associated with production of coal and oil. \n\nThis dataset is associated with the following publication:\nLenox , C., and O. Kaplan. Role of natural gas in meeting an electric sector emissions reduction strategy and effects on greenhouse gas emissions.   Energy Economics. Elsevier B.V., Amsterdam,  NETHERLANDS, 60: 460-468, (2016).",
+            "distribution": [
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/83/LenoxKaplan%20NatGas%20EMF31%20paper%20data%20tables%20with%20data%20dictionary.xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "LenoxKaplan NatGas EMF31 paper data tables with data dictionary.xlsx"
+                }
             ],
             "identifier": "A-nvxh-83",
             "keyword": [
@@ -43881,20 +43885,10 @@
                 "air quality",
                 "MARKAL"
             ],
-            "contactPoint": {
-                "fn": "Carol Lenox",
-                "hasEmail": "mailto:lenox.carol@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "LenoxKaplan NatGas EMF31 paper data tables with data dictionary.xlsx",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/83/LenoxKaplan%20NatGas%20EMF31%20paper%20data%20tables%20with%20data%20dictionary.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2016-05-26",
-            "references": [
-                "https://doi.org/10.1016/j.eneco.2016.06.009"
+            "programCode": [
+                "020:094"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -43904,42 +43898,42 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.eneco.2016.06.009"
+            ],
+            "rights": null,
+            "title": "LenoxKaplan_Role of natural gas in meeting electric sector emissions reduction strategy_dataset"
         },
         {
-            "title": "A Reduced Form Model for Ozone Based on Two Decades of CMAQ Simulations for the Continental United States",
-            "description": "File containing the locations where the gridded datasets used in the analysis presented in this manuscript are archived. The actual gridded datasets are too large to upload to sciencehub (several terabytes). \n\nThis dataset is associated with the following publication:\nPorter, P.S., S.T. Rao, C. Hogrefe, and R. Mathur. A Reduced Form Model for Ozone Based on Two Decades of CMAQ Simulations for the Continental United States.   Atmospheric Pollution Research. Turkish National Committee for Air Pollution Research and Control, Izmir,  TURKEY, 8(2): 275-284, (2017).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:094"
-            ],
-            "identifier": "A-6m95-260",
-            "keyword": [
-                "Reduced form model",
-                "meteorological adjustment",
-                "emission trends",
-                "Air quality trends",
-                "long-term CMAQ modeling"
-            ],
             "contactPoint": {
                 "fn": "Christian Hogrefe",
                 "hasEmail": "mailto:hogrefe.christian@epa.gov"
             },
+            "description": "File containing the locations where the gridded datasets used in the analysis presented in this manuscript are archived. The actual gridded datasets are too large to upload to sciencehub (several terabytes). \n\nThis dataset is associated with the following publication:\nPorter, P.S., S.T. Rao, C. Hogrefe, and R. Mathur. A Reduced Form Model for Ozone Based on Two Decades of CMAQ Simulations for the Continental United States.   Atmospheric Pollution Research. Turkish National Committee for Air Pollution Research and Control, Izmir,  TURKEY, 8(2): 275-284, (2017).",
             "distribution": [
                 {
-                    "title": "PorterEtAl_APR_Data_Locations.docx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/260/PorterEtAl_APR_Data_Locations.docx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+                    "title": "PorterEtAl_APR_Data_Locations.docx"
                 }
             ],
+            "identifier": "A-6m95-260",
+            "keyword": [
+                "Reduced form model",
+                "meteorological adjustment",
+                "emission trends",
+                "Air quality trends",
+                "long-term CMAQ modeling"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2015-12-22",
-            "references": [
-                "https://doi.org/10.1016/j.apr.2016.09.005"
+            "programCode": [
+                "020:094"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -43949,41 +43943,41 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.apr.2016.09.005"
+            ],
+            "rights": null,
+            "title": "A Reduced Form Model for Ozone Based on Two Decades of CMAQ Simulations for the Continental United States"
         },
         {
-            "title": "An Integrated Approach for Identifying Priority Contaminant in the Great Lakes Basin \u2013Investigations in the Lower Green Bay/Fox River and Milwaukee Estuary Areas of Concern",
-            "description": "Prioritization of chemicals was performed on two Areas of Concerns in the Great Lakes\nAn integrated risk surveillance and monitoring approach was applied\nBio-effect prediction methodologies were used to identify additional biological pathways. \n\nEnvironmental assessment of complex mixtures typically requires integration of chemical and biological measurements. This study demonstrates the use of a combination of instrumental chemical analyses, effects-based monitoring, and  bio-effects prediction approaches to help identify potential hazards and priority contaminants in two Great Lakes Areas of Concern (AOCs), the Lower Green Bay/Fox River  located near Green Bay, WI, USA and the Milwaukee Estuary, located near Milwaukee, WI, USA. Fathead minnows were caged  at four sites within each AOC (eight sites total). Following 4 d of in situ exposure, tissues and biofluids were sampled and used for targeted biological effects analyses. Additionally, 4 d composite water samples were collected concurrently at each caged fish site and analyzed for 132 analytes as well as evaluated for total estrogenic and androgenic activity using cell-based bioassays. Of the analytes examined, 75 were detected in composite samples from at least one site. Based on multiple analyses, one site in the East River and another site near a paper mill discharge in the Lower Green Bay/Fox River AOC, were prioritized due to their estrogenic and androgenic activity, respectively. The water samples from other sites generally did not exhibit significant estrogenic or androgenic activity, nor was there evidence for endocrine disruption in the fish exposed at these sites as indicated by the lack of alterations in ex vivo steroid production, circulating steroid concentrations, or vitellogenin mRNA expression in males. Induction of hepatic cyp1a mRNA expression was detected at several sites, suggesting the presence of chemicals that activate the Ah receptor.  To expand the scope beyond targeted investigation of endpoints selected a priori, several bio-effects prediction approaches were employed to identify other potentially disturbed biological pathways and related chemical constituents that may warrant future monitoring at these sites. For example, several  chemicals such as diethylphthalate and naphthalene , and genes and related pathways, such as cholinergic receptor muscarinic 3 (CHRM3), estrogen receptor alpha1 (esr1), chemokine ligand 10 protein (CXCL10), tumor protein p53 (p53), and monoamine oxidase B (Maob), were identified as candidates for future assessments at these AOCs. Overall, this study demonstrates that a better prioritization of contaminants and associated hazards can be achieved through integrated evaluation of multiple lines of evidence. Such prioritization can guide more comprehensive follow-up risk assessment efforts. \n\nThis dataset is associated with the following publication:\nLi, S., D. Villeneuve, J. Berninger, B. Blackwell, J. Cavallin, M. Hughes, K. Jensen, Z. Jorgenson, M. Kahl, A. Schroeder, K. Stevens, L. Thomas, M. Weberg, and G. Ankley. An integrated approach for identifying priority contaminant in the Great Lakes Basin -Investigations in the Lower Green Bay/Fox River and Milwaukee Estuary areas of concern.   SCIENCE OF THE TOTAL ENVIRONMENT. Elsevier BV, AMSTERDAM,  NETHERLANDS, 579: 825-837, (2017).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:095"
-            ],
-            "identifier": "A-5tb8-418",
-            "keyword": [
-                "adverse outcome pathway",
-                "biomarkers",
-                "screening and prioritization",
-                "aquatic ecosystems"
-            ],
             "contactPoint": {
                 "fn": "Daniel Villeneuve",
                 "hasEmail": "mailto:villeneuve.dan@epa.gov"
             },
+            "description": "Prioritization of chemicals was performed on two Areas of Concerns in the Great Lakes\nAn integrated risk surveillance and monitoring approach was applied\nBio-effect prediction methodologies were used to identify additional biological pathways. \n\nEnvironmental assessment of complex mixtures typically requires integration of chemical and biological measurements. This study demonstrates the use of a combination of instrumental chemical analyses, effects-based monitoring, and  bio-effects prediction approaches to help identify potential hazards and priority contaminants in two Great Lakes Areas of Concern (AOCs), the Lower Green Bay/Fox River  located near Green Bay, WI, USA and the Milwaukee Estuary, located near Milwaukee, WI, USA. Fathead minnows were caged  at four sites within each AOC (eight sites total). Following 4 d of in situ exposure, tissues and biofluids were sampled and used for targeted biological effects analyses. Additionally, 4 d composite water samples were collected concurrently at each caged fish site and analyzed for 132 analytes as well as evaluated for total estrogenic and androgenic activity using cell-based bioassays. Of the analytes examined, 75 were detected in composite samples from at least one site. Based on multiple analyses, one site in the East River and another site near a paper mill discharge in the Lower Green Bay/Fox River AOC, were prioritized due to their estrogenic and androgenic activity, respectively. The water samples from other sites generally did not exhibit significant estrogenic or androgenic activity, nor was there evidence for endocrine disruption in the fish exposed at these sites as indicated by the lack of alterations in ex vivo steroid production, circulating steroid concentrations, or vitellogenin mRNA expression in males. Induction of hepatic cyp1a mRNA expression was detected at several sites, suggesting the presence of chemicals that activate the Ah receptor.  To expand the scope beyond targeted investigation of endpoints selected a priori, several bio-effects prediction approaches were employed to identify other potentially disturbed biological pathways and related chemical constituents that may warrant future monitoring at these sites. For example, several  chemicals such as diethylphthalate and naphthalene , and genes and related pathways, such as cholinergic receptor muscarinic 3 (CHRM3), estrogen receptor alpha1 (esr1), chemokine ligand 10 protein (CXCL10), tumor protein p53 (p53), and monoamine oxidase B (Maob), were identified as candidates for future assessments at these AOCs. Overall, this study demonstrates that a better prioritization of contaminants and associated hazards can be achieved through integrated evaluation of multiple lines of evidence. Such prioritization can guide more comprehensive follow-up risk assessment efforts. \n\nThis dataset is associated with the following publication:\nLi, S., D. Villeneuve, J. Berninger, B. Blackwell, J. Cavallin, M. Hughes, K. Jensen, Z. Jorgenson, M. Kahl, A. Schroeder, K. Stevens, L. Thomas, M. Weberg, and G. Ankley. An integrated approach for identifying priority contaminant in the Great Lakes Basin -Investigations in the Lower Green Bay/Fox River and Milwaukee Estuary areas of concern.   SCIENCE OF THE TOTAL ENVIRONMENT. Elsevier BV, AMSTERDAM,  NETHERLANDS, 579: 825-837, (2017).",
             "distribution": [
                 {
-                    "title": "ScienceHub.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/418/ScienceHub.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "ScienceHub.xlsx"
                 }
             ],
+            "identifier": "A-5tb8-418",
+            "keyword": [
+                "adverse outcome pathway",
+                "biomarkers",
+                "screening and prioritization",
+                "aquatic ecosystems"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2016-09-29",
-            "references": [
-                "https://doi.org/10.1016/j.scitotenv.2016.11.021"
+            "programCode": [
+                "020:095"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -43993,41 +43987,40 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.scitotenv.2016.11.021"
+            ],
+            "rights": null,
+            "title": "An Integrated Approach for Identifying Priority Contaminant in the Great Lakes Basin \u2013Investigations in the Lower Green Bay/Fox River and Milwaukee Estuary Areas of Concern"
         },
         {
-            "title": "Ecosystem services in the St. Louis River AOC",
-            "description": "Dataset indicates the presence or absence of each ecosystems service at each coordinate Location. Also included are depth, fetch, and aquatic vegetation data. See supporting information for SAS code used to process data, sources of public spatial data, logic of GIS models used to generate presence absence assignments, GIS processing metadata, and KMZ maps (zipped file). \n\nThis dataset is associated with the following publication:\nAngradi , T., J. Launspach, D. Bolgrien , B. Bellinger, M. Starry, J. Hoffman , A. Trebitz , M. Sierszen , and T. Hollenhorst. Mapping ecosystem service indicators in a Great Lakes estuarine Area of Concern.   JOURNAL OF GREAT LAKES RESEARCH. International Association for Great Lakes Research, Ann Arbor, MI, USA, 42(3): 717-727, (2016).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "A-1ns3-80",
-            "keyword": [
-                "Ecosystems services",
-                "ecosystem services",
-                "Area of Concern"
-            ],
             "contactPoint": {
                 "fn": "Theodore Angradi",
                 "hasEmail": "mailto:angradi.theodore@epa.gov"
             },
+            "description": "Dataset indicates the presence or absence of each ecosystems service at each coordinate Location. Also included are depth, fetch, and aquatic vegetation data. See supporting information for SAS code used to process data, sources of public spatial data, logic of GIS models used to generate presence absence assignments, GIS processing metadata, and KMZ maps (zipped file). \n\nThis dataset is associated with the following publication:\nAngradi , T., J. Launspach, D. Bolgrien , B. Bellinger, M. Starry, J. Hoffman , A. Trebitz , M. Sierszen , and T. Hollenhorst. Mapping ecosystem service indicators in a Great Lakes estuarine Area of Concern.   JOURNAL OF GREAT LAKES RESEARCH. International Association for Great Lakes Research, Ann Arbor, MI, USA, 42(3): 717-727, (2016).",
             "distribution": [
                 {
-                    "title": "Science_hub_combinepointproject_2_9_16.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/80/Science_hub_combinepointproject_2_9_16.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Science_hub_combinepointproject_2_9_16.xlsx"
                 }
             ],
+            "identifier": "A-1ns3-80",
+            "keyword": [
+                "Ecosystems services",
+                "ecosystem services",
+                "Area of Concern"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2016-02-09",
-            "references": [
-                "https://doi.org/10.1016/j.jglr.2016.03.012",
-                "https://pasteur.epa.gov/uploads/80/documents/Ecoservices_KMZ.zip"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -44037,40 +44030,41 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.jglr.2016.03.012",
+                "https://pasteur.epa.gov/uploads/80/documents/Ecoservices_KMZ.zip"
+            ],
+            "rights": null,
+            "title": "Ecosystem services in the St. Louis River AOC"
         },
         {
-            "title": "Influence of exposure differences on city-to-city heterogeneity in PM2.5-mortality associations in U.S. Cities",
-            "description": "This dataset contains information on the cluster characteristics, health effect estimates, and the meta-regression results. \n\nThis dataset is associated with the following publication:\nBaxter, L., J. Crooks, and J. Sacks. Influence of exposure differences on city-to-city heterogeneity in PM2.5-mortality associations in US cities.   ENVIRONMENTAL HEALTH. Academic Press Incorporated, Orlando, FL, USA, 16(1): 1-8, (2017).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:094"
-            ],
-            "identifier": "A-15dx-523",
-            "keyword": [
-                "Fine Particulate Matter",
-                "epidemiology",
-                "air pollution exposure"
-            ],
             "contactPoint": {
                 "fn": "Lisa Baxter",
                 "hasEmail": "mailto:baxter.lisa@epa.gov"
             },
+            "description": "This dataset contains information on the cluster characteristics, health effect estimates, and the meta-regression results. \n\nThis dataset is associated with the following publication:\nBaxter, L., J. Crooks, and J. Sacks. Influence of exposure differences on city-to-city heterogeneity in PM2.5-mortality associations in US cities.   ENVIRONMENTAL HEALTH. Academic Press Incorporated, Orlando, FL, USA, 16(1): 1-8, (2017).",
             "distribution": [
                 {
-                    "title": "Baxter_A-15dx_datasets.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/523/Baxter_A-15dx_datasets.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Baxter_A-15dx_datasets.xlsx"
                 }
             ],
+            "identifier": "A-15dx-523",
+            "keyword": [
+                "Fine Particulate Matter",
+                "epidemiology",
+                "air pollution exposure"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2016-12-20",
-            "references": [
-                "https://doi.org/10.1186/s12940-016-0208-y"
+            "programCode": [
+                "020:094"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -44080,19 +44074,29 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1186/s12940-016-0208-y"
+            ],
+            "rights": null,
+            "title": "Influence of exposure differences on city-to-city heterogeneity in PM2.5-mortality associations in U.S. Cities"
         },
         {
-            "title": "Quantitative Structure-Use Relationship Model Predictions to evaluate Tox21 Chemicals as Functional Substitutes and Candidate Alternatives",
-            "description": "This dataset provides a prediction for all Tox21 chemicals with available QSUR descriptors across all 41 valid QSUR models developed with FUse. \n\nThis dataset is associated with the following publication:\nPhillips, K., J. Wambaugh, C. Grulke, K. Dionisio, and K. Isaacs. High-throughput screening of chemicals as functional substitutes using structure-based classification models.   GREEN CHEMISTRY. Royal Society of Chemistry, Cambridge,  UK, 19: 1063-1074, (2017).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:095"
+            "contactPoint": {
+                "fn": "Katherine Phillips",
+                "hasEmail": "mailto:phillips.katherine@epa.gov"
+            },
+            "description": "This dataset provides a prediction for all Tox21 chemicals with available QSUR descriptors across all 41 valid QSUR models developed with FUse. \n\nThis dataset is associated with the following publication:\nPhillips, K., J. Wambaugh, C. Grulke, K. Dionisio, and K. Isaacs. High-throughput screening of chemicals as functional substitutes using structure-based classification models.   GREEN CHEMISTRY. Royal Society of Chemistry, Cambridge,  UK, 19: 1063-1074, (2017).",
+            "distribution": [
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/510/qsur_predictions_for_tox21_library.xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "qsur_predictions_for_tox21_library.xlsx"
+                }
             ],
             "identifier": "A-wdcg-510",
             "keyword": [
@@ -44104,20 +44108,10 @@
                 "alternatives assement",
                 "high-throughput screening"
             ],
-            "contactPoint": {
-                "fn": "Katherine Phillips",
-                "hasEmail": "mailto:phillips.katherine@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "qsur_predictions_for_tox21_library.xlsx",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/510/qsur_predictions_for_tox21_library.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2016-11-30",
-            "references": [
-                "https://doi.org/10.1039/c6gc02744j"
+            "programCode": [
+                "020:095"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -44127,19 +44121,29 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1039/c6gc02744j"
+            ],
+            "rights": null,
+            "title": "Quantitative Structure-Use Relationship Model Predictions to evaluate Tox21 Chemicals as Functional Substitutes and Candidate Alternatives"
         },
         {
-            "title": "Functional Use Database (FUse)",
-            "description": "There are five different files for this dataset:\n1. A dataset listing the reported functional uses of chemicals (FUse)\n2. All 729 ToxPrint descriptors obtained from ChemoTyper for chemicals in FUse\n3. All EPI Suite properties obtained for chemicals in FUse\n4. The confusion matrix values, similarity thresholds, and bioactivity index for each model.\n5. The functional use prediction, bioactivity index, and prediction classification (poor prediction, functional substitute, candidate alternative) for each Tox21 chemical. \n\nThis dataset is associated with the following publication:\nPhillips, K., J. Wambaugh, C. Grulke, K. Dionisio, and K. Isaacs. High-throughput screening of chemicals as functional substitutes using structure-based classification models.   GREEN CHEMISTRY. Royal Society of Chemistry, Cambridge,  UK, 19: 1063-1074, (2017).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:095"
+            "contactPoint": {
+                "fn": "Katherine Phillips",
+                "hasEmail": "mailto:phillips.katherine@epa.gov"
+            },
+            "description": "There are five different files for this dataset:\n1. A dataset listing the reported functional uses of chemicals (FUse)\n2. All 729 ToxPrint descriptors obtained from ChemoTyper for chemicals in FUse\n3. All EPI Suite properties obtained for chemicals in FUse\n4. The confusion matrix values, similarity thresholds, and bioactivity index for each model.\n5. The functional use prediction, bioactivity index, and prediction classification (poor prediction, functional substitute, candidate alternative) for each Tox21 chemical. \n\nThis dataset is associated with the following publication:\nPhillips, K., J. Wambaugh, C. Grulke, K. Dionisio, and K. Isaacs. High-throughput screening of chemicals as functional substitutes using structure-based classification models.   GREEN CHEMISTRY. Royal Society of Chemistry, Cambridge,  UK, 19: 1063-1074, (2017).",
+            "distribution": [
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/495/functional_use_database.xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "functional_use_database.xlsx"
+                }
             ],
             "identifier": "A-wdcg-495",
             "keyword": [
@@ -44151,20 +44155,10 @@
                 "alternatives assement",
                 "high-throughput screening"
             ],
-            "contactPoint": {
-                "fn": "Katherine Phillips",
-                "hasEmail": "mailto:phillips.katherine@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "functional_use_database.xlsx",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/495/functional_use_database.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2016-11-30",
-            "references": [
-                "https://doi.org/10.1039/c6gc02744j"
+            "programCode": [
+                "020:095"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -44174,49 +44168,49 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1039/c6gc02744j"
+            ],
+            "rights": null,
+            "title": "Functional Use Database (FUse)"
         },
         {
-            "title": "Quantitative Structure-Use Relationship (QSUR) Model Descriptors",
-            "description": "This data set contains ToxPrint finger prints for all chemicals in FUse that had QSAR-ready SMILES strings as well as select physicochemical properties from the Estimation Program Interface Suite (EPI Suite) program. \n\nThis dataset is associated with the following publication:\nPhillips, K., J. Wambaugh, C. Grulke, K. Dionisio, and K. Isaacs. High-throughput screening of chemicals as functional substitutes using structure-based classification models.   GREEN CHEMISTRY. Royal Society of Chemistry, Cambridge,  UK, 19: 1063-1074, (2017).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:095"
-            ],
-            "identifier": "A-wdcg-508",
-            "keyword": [
-                "ExpoCast",
-                "functional use",
-                "qsar",
-                "machine learning algorithms",
-                "consumer products",
-                "alternatives assement",
-                "high-throughput screening"
-            ],
             "contactPoint": {
                 "fn": "Katherine Phillips",
                 "hasEmail": "mailto:phillips.katherine@epa.gov"
             },
+            "description": "This data set contains ToxPrint finger prints for all chemicals in FUse that had QSAR-ready SMILES strings as well as select physicochemical properties from the Estimation Program Interface Suite (EPI Suite) program. \n\nThis dataset is associated with the following publication:\nPhillips, K., J. Wambaugh, C. Grulke, K. Dionisio, and K. Isaacs. High-throughput screening of chemicals as functional substitutes using structure-based classification models.   GREEN CHEMISTRY. Royal Society of Chemistry, Cambridge,  UK, 19: 1063-1074, (2017).",
             "distribution": [
                 {
-                    "title": "toxprint_structural_descriptors.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/508/toxprint_structural_descriptors.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "toxprint_structural_descriptors.xlsx"
                 },
                 {
-                    "title": "epi_suite_physicochemical_properties.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/508/epi_suite_physicochemical_properties.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "epi_suite_physicochemical_properties.xlsx"
                 }
             ],
+            "identifier": "A-wdcg-508",
+            "keyword": [
+                "ExpoCast",
+                "functional use",
+                "qsar",
+                "machine learning algorithms",
+                "consumer products",
+                "alternatives assement",
+                "high-throughput screening"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2016-11-30",
-            "references": [
-                "https://doi.org/10.1039/c6gc02744j"
+            "programCode": [
+                "020:095"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -44226,19 +44220,29 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1039/c6gc02744j"
+            ],
+            "rights": null,
+            "title": "Quantitative Structure-Use Relationship (QSUR) Model Descriptors"
         },
         {
-            "title": "Quantitative Structure-Use Relationship Model thresholds for Model Validation, Domain of Applicability, and Candidate Alternative Selection",
-            "description": "This file contains value of the model training set confusion matrix, domain of applicability evaluation based on training set to predicted chemicals structural similarity, and 75th percentile bioactivity index values for each QSUR model. \n\nThis dataset is associated with the following publication:\nPhillips, K., J. Wambaugh, C. Grulke, K. Dionisio, and K. Isaacs. High-throughput screening of chemicals as functional substitutes using structure-based classification models.   GREEN CHEMISTRY. Royal Society of Chemistry, Cambridge,  UK, 19: 1063-1074, (2017).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:095"
+            "contactPoint": {
+                "fn": "Katherine Phillips",
+                "hasEmail": "mailto:phillips.katherine@epa.gov"
+            },
+            "description": "This file contains value of the model training set confusion matrix, domain of applicability evaluation based on training set to predicted chemicals structural similarity, and 75th percentile bioactivity index values for each QSUR model. \n\nThis dataset is associated with the following publication:\nPhillips, K., J. Wambaugh, C. Grulke, K. Dionisio, and K. Isaacs. High-throughput screening of chemicals as functional substitutes using structure-based classification models.   GREEN CHEMISTRY. Royal Society of Chemistry, Cambridge,  UK, 19: 1063-1074, (2017).",
+            "distribution": [
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/509/qsur_model_rankings_and_thresholds.xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "qsur_model_rankings_and_thresholds.xlsx"
+                }
             ],
             "identifier": "A-wdcg-509",
             "keyword": [
@@ -44250,20 +44254,10 @@
                 "alternatives assement",
                 "high-throughput screening"
             ],
-            "contactPoint": {
-                "fn": "Katherine Phillips",
-                "hasEmail": "mailto:phillips.katherine@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "qsur_model_rankings_and_thresholds.xlsx",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/509/qsur_model_rankings_and_thresholds.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2016-11-30",
-            "references": [
-                "https://doi.org/10.1039/c6gc02744j"
+            "programCode": [
+                "020:095"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -44273,41 +44267,41 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1039/c6gc02744j"
+            ],
+            "rights": null,
+            "title": "Quantitative Structure-Use Relationship Model thresholds for Model Validation, Domain of Applicability, and Candidate Alternative Selection"
         },
         {
-            "title": "Turkey Run Landfill Emissions Dataset",
-            "description": "landfill emissions measurements for the Turkey run landfill in Georgia. \n\nThis dataset is associated with the following publication:\nDe la Cruz, F., R. Green, G. Hater, J. Chanton, E. Thoma , T. Harvey, and M. Barlaz. Comparison of Field Measurements at a New Landfill to Methane Emissions Models.   ENVIRONMENTAL SCIENCE & TECHNOLOGY. American Chemical Society, Washington, DC, USA, 50(17): 9483-9441, (2016).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:094"
-            ],
-            "identifier": "A-0gb7-449",
-            "keyword": [
-                "Methane",
-                "Landfill",
-                "OTM 33B",
-                "Mobile Measurements"
-            ],
             "contactPoint": {
                 "fn": "Eben Thoma",
                 "hasEmail": "mailto:thoma.eben@epa.gov"
             },
+            "description": "landfill emissions measurements for the Turkey run landfill in Georgia. \n\nThis dataset is associated with the following publication:\nDe la Cruz, F., R. Green, G. Hater, J. Chanton, E. Thoma , T. Harvey, and M. Barlaz. Comparison of Field Measurements at a New Landfill to Methane Emissions Models.   ENVIRONMENTAL SCIENCE & TECHNOLOGY. American Chemical Society, Washington, DC, USA, 50(17): 9483-9441, (2016).",
             "distribution": [
                 {
-                    "title": "Landfill Emissions Study Data Set and Dictionary.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/449/Landfill%20Emissions%20Study%20Data%20Set%20and%20Dictionary.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Landfill Emissions Study Data Set and Dictionary.xlsx"
                 }
             ],
+            "identifier": "A-0gb7-449",
+            "keyword": [
+                "Methane",
+                "Landfill",
+                "OTM 33B",
+                "Mobile Measurements"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2016-06-10",
-            "references": [
-                "https://doi.org/10.1021/acs.est.6b00415"
+            "programCode": [
+                "020:094"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -44317,62 +44311,62 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1021/acs.est.6b00415"
+            ],
+            "rights": null,
+            "title": "Turkey Run Landfill Emissions Dataset"
         },
         {
-            "title": "2016 Uinta Basin Pneumatic Controller Study Database",
-            "description": "2016 Uinta Basin Pneumatic Controller Study Database: This study along with select figures and calculations. \n\nThis dataset is associated with the following publication:\nThoma, E., P. Deshmukh, R. Logan, M. Stovern, C. Dresser, and H. Brantley. Assessment of Uinta Basin Oil and Natural Gas Well Pad Pneumatic Controller Emissions.   Journal of Environmental Protection. Scientific Research Publishing, Inc., Irvine, CA, USA, 8(4): 394-415, (2017).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:094"
-            ],
-            "identifier": "A-kh1r-460",
-            "keyword": [
-                "Pneumatic Controller",
-                "Oil and Natural Gas Production",
-                "Uinta Basin",
-                "Methane",
-                "volatile organic compounds"
-            ],
             "contactPoint": {
                 "fn": "Eben Thoma",
                 "hasEmail": "mailto:thoma.eben@epa.gov"
             },
+            "description": "2016 Uinta Basin Pneumatic Controller Study Database: This study along with select figures and calculations. \n\nThis dataset is associated with the following publication:\nThoma, E., P. Deshmukh, R. Logan, M. Stovern, C. Dresser, and H. Brantley. Assessment of Uinta Basin Oil and Natural Gas Well Pad Pneumatic Controller Emissions.   Journal of Environmental Protection. Scientific Research Publishing, Inc., Irvine, CA, USA, 8(4): 394-415, (2017).",
             "distribution": [
                 {
-                    "title": "2016 Uinta Basin PC Study Summary_122016.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/460/2016%20Uinta%20Basin%20PC%20Study%20Summary_122016.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "2016 Uinta Basin PC Study Summary_122016.xlsx"
                 },
                 {
-                    "title": "QAPP-1J16-019.R1 QT16006_04 QAPP Uinta Basin PC Study WA 1-037_final.pdf",
                     "downloadURL": "https://pasteur.epa.gov/uploads/460/QAPP-1J16-019.R1%20QT16006_04%20QAPP%20Uinta%20Basin%20PC%20Study%20WA%201-037_final.pdf",
-                    "mediaType": "application/pdf"
+                    "mediaType": "application/pdf",
+                    "title": "QAPP-1J16-019.R1 QT16006_04 QAPP Uinta Basin PC Study WA 1-037_final.pdf"
                 },
                 {
-                    "title": "Canister Data.pdf",
                     "downloadURL": "https://pasteur.epa.gov/uploads/460/Canister%20Data.pdf",
-                    "mediaType": "application/pdf"
+                    "mediaType": "application/pdf",
+                    "title": "Canister Data.pdf"
                 },
                 {
-                    "title": "Kimray Controller Vent Calculator.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/460/Kimray%20Controller%20Vent%20Calculator.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Kimray Controller Vent Calculator.xlsx"
                 },
                 {
-                    "title": "Alicat Viscosity correction.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/460/Alicat%20Viscosity%20correction.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Alicat Viscosity correction.xlsx"
                 }
             ],
+            "identifier": "A-kh1r-460",
+            "keyword": [
+                "Pneumatic Controller",
+                "Oil and Natural Gas Production",
+                "Uinta Basin",
+                "Methane",
+                "volatile organic compounds"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2016-12-16",
-            "references": [
-                "https://doi.org/10.4236/jep.2017.84029"
+            "programCode": [
+                "020:094"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -44382,19 +44376,29 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.4236/jep.2017.84029"
+            ],
+            "rights": null,
+            "title": "2016 Uinta Basin Pneumatic Controller Study Database"
         },
         {
-            "title": "Comparison of cryopreserved trout hepatocytes and liver S9 fractions as in vitro tools for bioaccumulation assessment of chemicals that undergo biotransformation in fish",
-            "description": "The purpose of this study was to compare two in vitro systems, cryopreserved trout hepatocytes and trout liver S9 fractions, used to predict in vivo levels of biotransformation in fish.  This information is needed to refine modeled estimates of bioaccumulation for hydrophobic organic chemicals that undergo biotransformation.  In this effort we used trout hepatocytes to measure in vitro biotransformation of 6 polycyclic aromatic hydrocarbons (PAHs).  The results were compared to metabolism rates reported previously for trout liver S9 fractions.  Results obtained using both in vitro systems were then used to predict measured levels of hepatic clearance for the same test chemicals exhibited by isolated perfused livers.  The results of this study suggest that both in vitro systems are well suited for performing in vitro-in vivo metabolism extrapolations with fish as a means for improving modeled bioaccumulation predictions. \n\nThis dataset is associated with the following publication:\nFay, K., P. Fitzsimmons, A. Hoffman, and J. Nichols. Comparison of trout hepatocytes and liver S9 fractions  as in vitro models for predicting hepatic clearance in fish.   ENVIRONMENTAL TOXICOLOGY AND CHEMISTRY. Society of Environmental Toxicology and Chemistry,  FL, USA, 36(2): 463-471, (2017).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:095"
+            "contactPoint": {
+                "fn": "John Nichols",
+                "hasEmail": "mailto:nichols.john@epa.gov"
+            },
+            "description": "The purpose of this study was to compare two in vitro systems, cryopreserved trout hepatocytes and trout liver S9 fractions, used to predict in vivo levels of biotransformation in fish.  This information is needed to refine modeled estimates of bioaccumulation for hydrophobic organic chemicals that undergo biotransformation.  In this effort we used trout hepatocytes to measure in vitro biotransformation of 6 polycyclic aromatic hydrocarbons (PAHs).  The results were compared to metabolism rates reported previously for trout liver S9 fractions.  Results obtained using both in vitro systems were then used to predict measured levels of hepatic clearance for the same test chemicals exhibited by isolated perfused livers.  The results of this study suggest that both in vitro systems are well suited for performing in vitro-in vivo metabolism extrapolations with fish as a means for improving modeled bioaccumulation predictions. \n\nThis dataset is associated with the following publication:\nFay, K., P. Fitzsimmons, A. Hoffman, and J. Nichols. Comparison of trout hepatocytes and liver S9 fractions  as in vitro models for predicting hepatic clearance in fish.   ENVIRONMENTAL TOXICOLOGY AND CHEMISTRY. Society of Environmental Toxicology and Chemistry,  FL, USA, 36(2): 463-471, (2017).",
+            "distribution": [
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/195/Fay%20et%20al%202016_IPL_Hep_Comparison_%20Science%20Hub%20Data%20Summary_final.xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Fay et al 2016_IPL_Hep_Comparison_ Science Hub Data Summary_final.xlsx"
+                }
             ],
             "identifier": "A-b2rm-195",
             "keyword": [
@@ -44405,20 +44409,10 @@
                 "fish",
                 "rainbow trout"
             ],
-            "contactPoint": {
-                "fn": "John Nichols",
-                "hasEmail": "mailto:nichols.john@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "Fay et al 2016_IPL_Hep_Comparison_ Science Hub Data Summary_final.xlsx",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/195/Fay%20et%20al%202016_IPL_Hep_Comparison_%20Science%20Hub%20Data%20Summary_final.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2016-04-18",
-            "references": [
-                "https://doi.org/10.1002/etc.3572"
+            "programCode": [
+                "020:095"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -44428,42 +44422,42 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1002/etc.3572"
+            ],
+            "rights": null,
+            "title": "Comparison of cryopreserved trout hepatocytes and liver S9 fractions as in vitro tools for bioaccumulation assessment of chemicals that undergo biotransformation in fish"
         },
         {
-            "title": "E331 Behavior TP HF RW O3 SHC2.63",
-            "description": "Human and animal studies indicate that maternal obesity can negatively impact aspects of metabolism and neurodevelopment in the offspring.  Not known, however, is whether maternal exercise can alter these adverse outcomes.  In this study, Long-Evans female rats were provided a high fat (60%; HFD) or control diet (CD) 44 days before mating and throughout gestation and lactation.  Running wheels were available to half of each diet group during the gestational period only: CD diet with (CDRW) or without (sedentary; CDSED) exercise, and HFD with (HFRW) or without (HFSED) exercise.  The offspring in this study were put on control diet after weaning and examined using a number of behavioral evaluations up to 4 months of age.  Offspring of CDRW dams weighed less than offspring from CDSED dams, as well as from HFD dams.  After weaning, the lower weight in CDRW offspring persisted in male, but not female, rats.  Male (females not tested) offspring from HFSED dams performed worse than other groups in a Morris water maze during initial spatial training as well as reversal learning; memory was not impacted.  Female, but not male, offspring from the HFSED dams showed less preference for chocolate milk during a 2-bottle choice test.  No differences were seen in tests of novel object recognition, social approach, or locomotor activity.  Thus, maternal diet and exercise produced differential effects on growth and selective behaviors in the offspring, and the data demonstrate a positive impact of maternal exercise on the offspring in that it ameliorated some deleterious behavioral effects of a maternal high fat diet. \n\nThis dataset is associated with the following publication:\nMoser, V., K. Mcdaniel, E. Wooland, P. Phillips, J. Franklin, and C. Gordon. IMPACTS OF MATERNAL DIET AND EXERCISE ON OFFSPRING BEHAVIOR AND GROWTH.   NEUROTOXICOLOGY AND TERATOLOGY. Elsevier Science Ltd, New York, NY, USA,  46-50, (2017).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "A-jdg3-531",
-            "keyword": [
-                "Maternal Diet",
-                "Offspring",
-                "behavior",
-                "Exercise",
-                "Rat"
-            ],
             "contactPoint": {
                 "fn": "Christopher Gordon",
                 "hasEmail": "mailto:gordon.christopher@epa.gov"
             },
+            "description": "Human and animal studies indicate that maternal obesity can negatively impact aspects of metabolism and neurodevelopment in the offspring.  Not known, however, is whether maternal exercise can alter these adverse outcomes.  In this study, Long-Evans female rats were provided a high fat (60%; HFD) or control diet (CD) 44 days before mating and throughout gestation and lactation.  Running wheels were available to half of each diet group during the gestational period only: CD diet with (CDRW) or without (sedentary; CDSED) exercise, and HFD with (HFRW) or without (HFSED) exercise.  The offspring in this study were put on control diet after weaning and examined using a number of behavioral evaluations up to 4 months of age.  Offspring of CDRW dams weighed less than offspring from CDSED dams, as well as from HFD dams.  After weaning, the lower weight in CDRW offspring persisted in male, but not female, rats.  Male (females not tested) offspring from HFSED dams performed worse than other groups in a Morris water maze during initial spatial training as well as reversal learning; memory was not impacted.  Female, but not male, offspring from the HFSED dams showed less preference for chocolate milk during a 2-bottle choice test.  No differences were seen in tests of novel object recognition, social approach, or locomotor activity.  Thus, maternal diet and exercise produced differential effects on growth and selective behaviors in the offspring, and the data demonstrate a positive impact of maternal exercise on the offspring in that it ameliorated some deleterious behavioral effects of a maternal high fat diet. \n\nThis dataset is associated with the following publication:\nMoser, V., K. Mcdaniel, E. Wooland, P. Phillips, J. Franklin, and C. Gordon. IMPACTS OF MATERNAL DIET AND EXERCISE ON OFFSPRING BEHAVIOR AND GROWTH.   NEUROTOXICOLOGY AND TERATOLOGY. Elsevier Science Ltd, New York, NY, USA,  46-50, (2017).",
             "distribution": [
                 {
-                    "title": "GordonChristopher_E331 Behavior TP HF O3 SHC 2_63_dataset_20170314 SCID A-jdg3.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/531/GordonChristopher_E331%20Behavior%20TP%20HF%20O3%20SHC%202_63_dataset_20170314%20SCID%20A-jdg3.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "GordonChristopher_E331 Behavior TP HF O3 SHC 2_63_dataset_20170314 SCID A-jdg3.xlsx"
                 }
             ],
+            "identifier": "A-jdg3-531",
+            "keyword": [
+                "Maternal Diet",
+                "Offspring",
+                "behavior",
+                "Exercise",
+                "Rat"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2017-03-24",
-            "references": [
-                "https://doi.org/10.1016/j.ntt.2017.07.002"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -44473,19 +44467,29 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.ntt.2017.07.002"
+            ],
+            "rights": null,
+            "title": "E331 Behavior TP HF RW O3 SHC2.63"
         },
         {
-            "title": "E331 TP HF RW O3 SHC2.63 SCID: A-bvqk",
-            "description": "Data for differing physiological measures of dams on high fat or control diet with/without exercise and physiological effects on male and female offspring. \n\nThis dataset is associated with the following publication:\nGordon, C., P. Phillips, A. Johnstone, J. Schmid, M. Schladweiler, A. Ledbetter, S. Snow, and U. Kodavanti. EFFECTS OF MATERNAL HIGH FAT DIET AND SEDENTARY LIFESTYLE ON SUSCEPTIBILITY OF ADULT OFFSPRING TO OZONE EXPOSURE IN RATS.   INHALATION TOXICOLOGY. Informa Healthcare USA, New York, NY, USA,  239-254, (2017).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
+            "contactPoint": {
+                "fn": "Christopher Gordon",
+                "hasEmail": "mailto:gordon.christopher@epa.gov"
+            },
+            "description": "Data for differing physiological measures of dams on high fat or control diet with/without exercise and physiological effects on male and female offspring. \n\nThis dataset is associated with the following publication:\nGordon, C., P. Phillips, A. Johnstone, J. Schmid, M. Schladweiler, A. Ledbetter, S. Snow, and U. Kodavanti. EFFECTS OF MATERNAL HIGH FAT DIET AND SEDENTARY LIFESTYLE ON SUSCEPTIBILITY OF ADULT OFFSPRING TO OZONE EXPOSURE IN RATS.   INHALATION TOXICOLOGY. Informa Healthcare USA, New York, NY, USA,  239-254, (2017).",
+            "distribution": [
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/530/GordonChristopher_E331%20TP%20HF%20O3%20SHC%202_63_dataset_20170309%20SCID%20A-bvqk.xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "GordonChristopher_E331 TP HF O3 SHC 2_63_dataset_20170309 SCID A-bvqk.xlsx"
+                }
             ],
             "identifier": "A-bvqk-530",
             "keyword": [
@@ -44497,20 +44501,10 @@
                 "Offspring",
                 "Ozone"
             ],
-            "contactPoint": {
-                "fn": "Christopher Gordon",
-                "hasEmail": "mailto:gordon.christopher@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "GordonChristopher_E331 TP HF O3 SHC 2_63_dataset_20170309 SCID A-bvqk.xlsx",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/530/GordonChristopher_E331%20TP%20HF%20O3%20SHC%202_63_dataset_20170309%20SCID%20A-bvqk.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2017-03-17",
-            "references": [
-                "https://doi.org/10.1080/08958378.2017.1342719"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -44520,19 +44514,29 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1080/08958378.2017.1342719"
+            ],
+            "rights": null,
+            "title": "E331 TP HF RW O3 SHC2.63 SCID: A-bvqk"
         },
         {
-            "title": "PM mass and elemental species concentration data for I-96 monitoring sites",
-            "description": "PM2.5 (fine) and PM10-2.5 (coarse) mass concentrations for monitoring sites located 10 m, 100 m and 300 m north of Interstate I-96 in Detroit, the water-soluble and acid-soluble elemental species concentrations for each, and results of factor analysis using these data. \n\nThis dataset is associated with the following publication:\nOakes, M., J. Burke, G. Norris, K. Kovalcik, J.P. Pancras, and M. Landis. Near-road enhancement and solubility of fine and coarse particulate matter trace elements near a major interstate in Detroit, Michigan.   ATMOSPHERIC ENVIRONMENT. Elsevier Science Ltd, New York, NY, USA, 145: 213-224, (2016).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:094"
+            "contactPoint": {
+                "fn": "Janet Burke-Norris",
+                "hasEmail": "mailto:burke.janet@epa.gov"
+            },
+            "description": "PM2.5 (fine) and PM10-2.5 (coarse) mass concentrations for monitoring sites located 10 m, 100 m and 300 m north of Interstate I-96 in Detroit, the water-soluble and acid-soluble elemental species concentrations for each, and results of factor analysis using these data. \n\nThis dataset is associated with the following publication:\nOakes, M., J. Burke, G. Norris, K. Kovalcik, J.P. Pancras, and M. Landis. Near-road enhancement and solubility of fine and coarse particulate matter trace elements near a major interstate in Detroit, Michigan.   ATMOSPHERIC ENVIRONMENT. Elsevier Science Ltd, New York, NY, USA, 145: 213-224, (2016).",
+            "distribution": [
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/518/A-69pg_Data_Files.zip",
+                    "mediaType": "application/x-zip-compressed",
+                    "title": "A-69pg_Data_Files.zip"
+                }
             ],
             "identifier": "A-69pg-518",
             "keyword": [
@@ -44543,20 +44547,10 @@
                 "Traffic sources",
                 "Brake wear"
             ],
-            "contactPoint": {
-                "fn": "Janet Burke-Norris",
-                "hasEmail": "mailto:burke.janet@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "A-69pg_Data_Files.zip",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/518/A-69pg_Data_Files.zip",
-                    "mediaType": "application/x-zip-compressed"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2016-09-12",
-            "references": [
-                "https://doi.org/10.1016/j.atmosenv.2016.09.034"
+            "programCode": [
+                "020:094"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -44566,19 +44560,29 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.atmosenv.2016.09.034"
+            ],
+            "rights": null,
+            "title": "PM mass and elemental species concentration data for I-96 monitoring sites"
         },
         {
-            "title": "Data for GMD article \"A framework for expanding aqueous chemistry in the Community Multiscale Air Quality (CMAQ) model version 5.1\"",
-            "description": "These data were used to generate the figures included in the following manuscript: Fahey, et al. (2017) \"A framework for expanding aqueous chemistry in the Community Multiscale Air Quality (CMAQ) model version 5.1\". Geosci. Mod. Dev. \n\nThis dataset is associated with the following publication:\nFahey, K., A. Carlton, H. Pye, J. Baek, B. Hutzell, C. Stanier, K. Baker, W. Appel, M. Jaoui, and J. Offenberg. A framework for expanding aqueous chemistry in the Community Multiscale Air Quality (CMAQ) model version 5.1.   Geoscientific Model Development. Copernicus Publications, Katlenburg-Lindau,  GERMANY, 10: 1587-1605, (2017).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:094"
+            "contactPoint": {
+                "fn": "Kathleen Fahey",
+                "hasEmail": "mailto:fahey.kathleen@epa.gov"
+            },
+            "description": "These data were used to generate the figures included in the following manuscript: Fahey, et al. (2017) \"A framework for expanding aqueous chemistry in the Community Multiscale Air Quality (CMAQ) model version 5.1\". Geosci. Mod. Dev. \n\nThis dataset is associated with the following publication:\nFahey, K., A. Carlton, H. Pye, J. Baek, B. Hutzell, C. Stanier, K. Baker, W. Appel, M. Jaoui, and J. Offenberg. A framework for expanding aqueous chemistry in the Community Multiscale Air Quality (CMAQ) model version 5.1.   Geoscientific Model Development. Copernicus Publications, Katlenburg-Lindau,  GERMANY, 10: 1587-1605, (2017).",
+            "distribution": [
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/547/Figure-data_Fahey.xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Figure-data_Fahey.xlsx"
+                }
             ],
             "identifier": "A-wh7p-547",
             "keyword": [
@@ -44589,20 +44593,10 @@
                 "sulfate",
                 "SOA"
             ],
-            "contactPoint": {
-                "fn": "Kathleen Fahey",
-                "hasEmail": "mailto:fahey.kathleen@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "Figure-data_Fahey.xlsx",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/547/Figure-data_Fahey.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2017-04-04",
-            "references": [
-                "https://doi.org/10.5194/gmd-10-1587-2017"
+            "programCode": [
+                "020:094"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -44612,70 +44606,72 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.5194/gmd-10-1587-2017"
+            ],
+            "rights": null,
+            "title": "Data for GMD article \"A framework for expanding aqueous chemistry in the Community Multiscale Air Quality (CMAQ) model version 5.1\""
         },
         {
-            "title": "Laboratory simulations of the atmospheric mixed layer in flow over complex terrain",
-            "description": "A laboratory study of the influence of complex terrain on the interface between a well-mixed boundary layer and an elevated stratified layer was conducted in the towing-tank facility of the U.S. Environmental Protection Agency.  The height of the mixed layer in the daytime boundary layer can have a strong influence on the concentration of pollutants within this layer.  Deflections of streamlines at the height of the interface are primarily a function of hill Froude number (Fr), the ratio of mixed-layer height (zi) to terrain height (h), and the crosswind dimension of the terrain.  The magnitude of the deflections increases as Fr increases and zi / h decreases.  For mixing-height streamlines that are initially below the terrain top, the response is linear with Fr; for those initially above the terrain feature the response to Fr is more complex.  Once Fr exceeds about 2, the terrain-related response of the mixed layer interface decreases somewhat with increasing Fr (toward more neutral flow).  Deflections are also shown to increase as the crosswind dimensions of the terrain increases.  Comparisons with numerical modeling, limited field data and other laboratory measurements reported in the literature are favorable. Additionally, visual observations of dye streamers suggests that the flow structure exhibited for our elevated inversions passing over three dimensional hills is similar to that reported in the literature for continuously stratified flow over two-dimensional hills. \n\nThis dataset is associated with the following publication:\nPerry, S., and W. Snyder. Laboratory simulations of the atmospheric mixed-layer in flow over complex topography.   PHYSICS OF FLUIDS. Physics of Fluids,    29(2): 020702, (2017).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:094"
-            ],
-            "identifier": "A-w6n0-522",
-            "keyword": [
-                "atmospheric mixed layer",
-                "complex terrain",
-                "stratified water channel"
-            ],
             "contactPoint": {
                 "fn": "Steven Perry",
                 "hasEmail": "mailto:perry.steven@epa.gov"
             },
+            "describedBy": "https://pasteur.epa.gov/uploads/522/documents/A-w6n0-DataDictionaryMLCT-Perry-20160805.docx",
+            "describedByType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+            "description": "A laboratory study of the influence of complex terrain on the interface between a well-mixed boundary layer and an elevated stratified layer was conducted in the towing-tank facility of the U.S. Environmental Protection Agency.  The height of the mixed layer in the daytime boundary layer can have a strong influence on the concentration of pollutants within this layer.  Deflections of streamlines at the height of the interface are primarily a function of hill Froude number (Fr), the ratio of mixed-layer height (zi) to terrain height (h), and the crosswind dimension of the terrain.  The magnitude of the deflections increases as Fr increases and zi / h decreases.  For mixing-height streamlines that are initially below the terrain top, the response is linear with Fr; for those initially above the terrain feature the response to Fr is more complex.  Once Fr exceeds about 2, the terrain-related response of the mixed layer interface decreases somewhat with increasing Fr (toward more neutral flow).  Deflections are also shown to increase as the crosswind dimensions of the terrain increases.  Comparisons with numerical modeling, limited field data and other laboratory measurements reported in the literature are favorable. Additionally, visual observations of dye streamers suggests that the flow structure exhibited for our elevated inversions passing over three dimensional hills is similar to that reported in the literature for continuously stratified flow over two-dimensional hills. \n\nThis dataset is associated with the following publication:\nPerry, S., and W. Snyder. Laboratory simulations of the atmospheric mixed-layer in flow over complex topography.   PHYSICS OF FLUIDS. Physics of Fluids,    29(2): 020702, (2017).",
             "distribution": [
                 {
-                    "title": "Figure 4 data.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/522/Figure%204%20data.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Figure 4 data.xlsx"
                 },
                 {
-                    "title": "Figure 6 data.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/522/Figure%206%20data.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Figure 6 data.xlsx"
                 },
                 {
-                    "title": "Figure 7 data.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/522/Figure%207%20data.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Figure 7 data.xlsx"
                 },
                 {
-                    "title": "Figure 8 data.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/522/Figure%208%20data.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Figure 8 data.xlsx"
                 },
                 {
-                    "title": "Figure 9 data.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/522/Figure%209%20data.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Figure 9 data.xlsx"
                 },
                 {
-                    "title": "Figure 10 data.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/522/Figure%2010%20data.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Figure 10 data.xlsx"
                 },
                 {
-                    "title": "Figure 11 data.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/522/Figure%2011%20data.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Figure 11 data.xlsx"
                 }
             ],
+            "identifier": "A-w6n0-522",
+            "keyword": [
+                "atmospheric mixed layer",
+                "complex terrain",
+                "stratified water channel"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2016-10-03",
-            "references": [
-                "https://doi.org/10.1063/1.4974505"
+            "programCode": [
+                "020:094"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -44686,56 +44682,54 @@
                     }
                 }
             },
-            "describedBy": "https://pasteur.epa.gov/uploads/522/documents/A-w6n0-DataDictionaryMLCT-Perry-20160805.docx",
-            "describedByType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
+            "references": [
+                "https://doi.org/10.1063/1.4974505"
+            ],
+            "rights": null,
+            "title": "Laboratory simulations of the atmospheric mixed layer in flow over complex terrain"
         },
         {
-            "title": "Estimation of pyrethroid pesticide intake using regression modeling of food groups based on composite dietary samples",
-            "description": "Population-based estimates of pesticide intake are needed to characterize exposure for particular demographic groups based on their dietary behaviors. Regression modeling performed on measurements of selected pesticides in composited duplicate diet samples allowed 1) estimation of pesticide intakes for a defined demographic community, and 2) comparison of dietary pesticide intakes between the composite and individual samples. Extant databases were useful for assigning individual samples to composites, but they could not provide the breadth of information needed to facilitate measurable levels in every composite. Composite sample measurements were found to be good predictors of pyrethroid pesticide levels in their individual sample constituents where sufficient measurements are available above the method detection limit. Statistical inference shows little evidence of differences between individual and composite measurements and suggests that regression modeling of food groups based on composite dietary samples may provide an effective tool for estimating dietary pesticide intake for a defined population. \n\nThis dataset is associated with the following publication:\nMichael, L., G.G. Brown, and L. Melnyk. Estimation of pyrethroid pesticide intake using regression modeling of food groups based on composite dietary samples...   Journal of Environmental Science and Health. Part B, Pesticides, Food Contaminants, and Agricultural Wastes. Marcel Dekker Incorporated, New York, NY, USA, 51(11): 751, (2016).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "A-4qrk-161",
-            "keyword": [
-                "pesticides",
-                "food analysis",
-                "dietary exposure",
-                "community duplicat diet",
-                "dietary pesticide intake",
-                "regression modeling",
-                "sample compositing",
-                "pyrethroids"
-            ],
             "contactPoint": {
                 "fn": "Lisa Melnyk",
                 "hasEmail": "mailto:melnyk.lisa@epa.gov"
             },
+            "description": "Population-based estimates of pesticide intake are needed to characterize exposure for particular demographic groups based on their dietary behaviors. Regression modeling performed on measurements of selected pesticides in composited duplicate diet samples allowed 1) estimation of pesticide intakes for a defined demographic community, and 2) comparison of dietary pesticide intakes between the composite and individual samples. Extant databases were useful for assigning individual samples to composites, but they could not provide the breadth of information needed to facilitate measurable levels in every composite. Composite sample measurements were found to be good predictors of pyrethroid pesticide levels in their individual sample constituents where sufficient measurements are available above the method detection limit. Statistical inference shows little evidence of differences between individual and composite measurements and suggests that regression modeling of food groups based on composite dietary samples may provide an effective tool for estimating dietary pesticide intake for a defined population. \n\nThis dataset is associated with the following publication:\nMichael, L., G.G. Brown, and L. Melnyk. Estimation of pyrethroid pesticide intake using regression modeling of food groups based on composite dietary samples...   Journal of Environmental Science and Health. Part B, Pesticides, Food Contaminants, and Agricultural Wastes. Marcel Dekker Incorporated, New York, NY, USA, 51(11): 751, (2016).",
             "distribution": [
                 {
-                    "title": "Sets 1-4 composites pesticides & phth rev3.2.xls",
                     "downloadURL": "https://pasteur.epa.gov/uploads/161/Sets%201-4%20composites%20pesticides%20%26%20phth%20rev3.2.xls",
-                    "mediaType": "application/vnd.ms-excel"
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Sets 1-4 composites pesticides & phth rev3.2.xls"
                 },
                 {
-                    "title": "Bags proportions.xls",
                     "downloadURL": "https://pasteur.epa.gov/uploads/161/Bags%20proportions.xls",
-                    "mediaType": "application/vnd.ms-excel"
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Bags proportions.xls"
                 },
                 {
-                    "title": "Food list addins(lcm_msm 08162010).xls",
                     "downloadURL": "https://pasteur.epa.gov/uploads/161/Food%20list%20addins%28lcm_msm%2008162010%29.xls",
-                    "mediaType": "application/vnd.ms-excel"
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Food list addins(lcm_msm 08162010).xls"
                 }
             ],
+            "identifier": "A-4qrk-161",
+            "keyword": [
+                "pesticides",
+                "food analysis",
+                "dietary exposure",
+                "community duplicat diet",
+                "dietary pesticide intake",
+                "regression modeling",
+                "sample compositing",
+                "pyrethroids"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2010-09-30",
-            "references": [
-                "https://doi.org/10.1080/03601234.2016.1198640"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -44745,34 +44739,34 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1080/03601234.2016.1198640"
+            ],
+            "rights": null,
+            "title": "Estimation of pyrethroid pesticide intake using regression modeling of food groups based on composite dietary samples"
         },
         {
-            "title": "Multiscale predictions of aviation-attributable PM 2.5 for US airports modeled using CMAQ with plume-in-grid and an aircraft-specific 1-D emission model ",
-            "description": "NA. This dataset is not publicly accessible because: No EPA generated data was used in this work. It can be accessed through the following means: NA. Format: No EPA generated data was used in this work. \n\nThis dataset is associated with the following publication:\nWoody, M., H. Hsi-Wu Wong, J.J. West, and S. Arunachalam. Multiscale predictions of aviation-attributable PM2.5 for U.S. airports modeled using CMAQ with plume-in-grid and an aircraft-specific 1-D emission model.   ATMOSPHERIC ENVIRONMENT. Elsevier Science Ltd, New York, NY, USA, 147: 384-394, (2016).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:094"
-            ],
+            "contactPoint": {
+                "fn": "Matthew Woody",
+                "hasEmail": "mailto:woody.matthew@epa.gov"
+            },
+            "description": "NA. This dataset is not publicly accessible because: No EPA generated data was used in this work. It can be accessed through the following means: NA. Format: No EPA generated data was used in this work. \n\nThis dataset is associated with the following publication:\nWoody, M., H. Hsi-Wu Wong, J.J. West, and S. Arunachalam. Multiscale predictions of aviation-attributable PM2.5 for U.S. airports modeled using CMAQ with plume-in-grid and an aircraft-specific 1-D emission model.   ATMOSPHERIC ENVIRONMENT. Elsevier Science Ltd, New York, NY, USA, 147: 384-394, (2016).",
+            "distribution": [],
             "identifier": "A-fqzk-548",
             "keyword": [
                 "CMAQ",
                 "Aircraft emissions",
                 "Plume-in-grid"
             ],
-            "contactPoint": {
-                "fn": "Matthew Woody",
-                "hasEmail": "mailto:woody.matthew@epa.gov"
-            },
-            "distribution": [],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2017-02-15",
-            "references": [
-                "https://doi.org/10.1016/j.atmosenv.2016.10.016"
+            "programCode": [
+                "020:094"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -44782,113 +44776,113 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.atmosenv.2016.10.016"
+            ],
+            "rights": null,
+            "title": "Multiscale predictions of aviation-attributable PM 2.5 for US airports modeled using CMAQ with plume-in-grid and an aircraft-specific 1-D emission model "
         },
         {
-            "title": "Tables and figures from Gavett 2016 paper in Particle and Fibre Toxicology",
-            "description": "The files in the dataset are labeled according to table or figure number as listed in the paper (Gavett et al., Particle and Fibre Toxicology, 13:17, 2016). The paper itself and an online additional file are also included. Data files from the additional file are labeled as Extra File with figures and tables labeled Table S1, Figure S1, etc. The files are all self explanatory with clearly labeled headers and notes explaining the data. Derived data can be traced back to original data by following the formula links in excel files. PDF report titles contain page numbers which reference summary tables used in the paper. \n\nThis dataset is associated with the following publication:\nGavett , S., C. Parkinson, G. Willson, C. Wood , A. Jarabek , K. Roberts, U. Kodavanti , and D. Dodd. Persistent Effects of Libby Amphibole and Amosite Asbestos Following Subchronic Inhalation in Rats.   Particle and Fibre Toxicology. BioMed Central Ltd, London,  UK, 13(1): 17, (2016).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "A-bvqj-228",
-            "keyword": [
-                "asbestos",
-                "Libby amphibole",
-                "amosite",
-                "inflammasome",
-                "inflammation",
-                "Inhalation exposures"
-            ],
             "contactPoint": {
                 "fn": "Stephen Gavett",
                 "hasEmail": "mailto:gavett.stephen@epa.gov"
             },
+            "description": "The files in the dataset are labeled according to table or figure number as listed in the paper (Gavett et al., Particle and Fibre Toxicology, 13:17, 2016). The paper itself and an online additional file are also included. Data files from the additional file are labeled as Extra File with figures and tables labeled Table S1, Figure S1, etc. The files are all self explanatory with clearly labeled headers and notes explaining the data. Derived data can be traced back to original data by following the formula links in excel files. PDF report titles contain page numbers which reference summary tables used in the paper. \n\nThis dataset is associated with the following publication:\nGavett , S., C. Parkinson, G. Willson, C. Wood , A. Jarabek , K. Roberts, U. Kodavanti , and D. Dodd. Persistent Effects of Libby Amphibole and Amosite Asbestos Following Subchronic Inhalation in Rats.   Particle and Fibre Toxicology. BioMed Central Ltd, London,  UK, 13(1): 17, (2016).",
             "distribution": [
                 {
-                    "title": "Gavett 2016 PartFibToxicol persistent effects LA and AM following subchr inhal.pdf",
                     "downloadURL": "https://pasteur.epa.gov/uploads/228/Gavett%202016%20PartFibToxicol%20persistent%20effects%20LA%20and%20AM%20following%20subchr%20inhal.pdf",
-                    "mediaType": "application/pdf"
+                    "mediaType": "application/pdf",
+                    "title": "Gavett 2016 PartFibToxicol persistent effects LA and AM following subchr inhal.pdf"
                 },
                 {
-                    "title": "Gavett 2016 PartFibToxicol Addtional File 1.docx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/228/Gavett%202016%20PartFibToxicol%20Addtional%20File%201.docx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+                    "title": "Gavett 2016 PartFibToxicol Addtional File 1.docx"
                 },
                 {
-                    "title": "Figure 1 two week exp BALF data Gavett 2016 PFT.xls",
                     "downloadURL": "https://pasteur.epa.gov/uploads/228/Figure%201%20two%20week%20exp%20BALF%20data%20Gavett%202016%20PFT.xls",
-                    "mediaType": "application/vnd.ms-excel"
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Figure 1 two week exp BALF data Gavett 2016 PFT.xls"
                 },
                 {
-                    "title": "Figure 2 two week exp mRNA data Gavett 2016 PFT.xls",
                     "downloadURL": "https://pasteur.epa.gov/uploads/228/Figure%202%20two%20week%20exp%20mRNA%20data%20Gavett%202016%20PFT.xls",
-                    "mediaType": "application/vnd.ms-excel"
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Figure 2 two week exp mRNA data Gavett 2016 PFT.xls"
                 },
                 {
-                    "title": "Figure 3 two week exp BrdU data Gavett 2016 PFT.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/228/Figure%203%20two%20week%20exp%20BrdU%20data%20Gavett%202016%20PFT.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Figure 3 two week exp BrdU data Gavett 2016 PFT.xlsx"
                 },
                 {
-                    "title": "Figure 4 three month exp lung fiber data Gavett 2016 PFT.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/228/Figure%204%20three%20month%20exp%20lung%20fiber%20data%20Gavett%202016%20PFT.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Figure 4 three month exp lung fiber data Gavett 2016 PFT.xlsx"
                 },
                 {
-                    "title": "Figure 5 three month exp BAL data Gavett 2016 PFT.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/228/Figure%205%20three%20month%20exp%20BAL%20data%20Gavett%202016%20PFT.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Figure 5 three month exp BAL data Gavett 2016 PFT.xlsx"
                 },
                 {
-                    "title": "Figure 6 three month exp cytokine and pathway data Gavett 2016 PFT.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/228/Figure%206%20three%20month%20exp%20cytokine%20and%20pathway%20data%20Gavett%202016%20PFT.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Figure 6 three month exp cytokine and pathway data Gavett 2016 PFT.xlsx"
                 },
                 {
-                    "title": "Table 1 two week exp (p 87-94) and pathology (p 103) data Gavett 2016 PFT.pdf",
                     "downloadURL": "https://pasteur.epa.gov/uploads/228/Table%201%20two%20week%20exp%20%28p%2087-94%29%20and%20pathology%20%28p%20103%29%20data%20Gavett%202016%20PFT.pdf",
-                    "mediaType": "application/pdf"
+                    "mediaType": "application/pdf",
+                    "title": "Table 1 two week exp (p 87-94) and pathology (p 103) data Gavett 2016 PFT.pdf"
                 },
                 {
-                    "title": "Table 2 three month exp inhalation report mass conc and APS data Gavett 2016 PFT.docx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/228/Table%202%20three%20month%20exp%20inhalation%20report%20mass%20conc%20and%20APS%20data%20Gavett%202016%20PFT.docx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+                    "title": "Table 2 three month exp inhalation report mass conc and APS data Gavett 2016 PFT.docx"
                 },
                 {
-                    "title": "Table 2 three month exp SEM data Gavett 2016 PFT.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/228/Table%202%20three%20month%20exp%20SEM%20data%20Gavett%202016%20PFT.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Table 2 three month exp SEM data Gavett 2016 PFT.xlsx"
                 },
                 {
-                    "title": "Table 3 1 day to 3 month pathology (p 12-13) data.pdf",
                     "downloadURL": "https://pasteur.epa.gov/uploads/228/Table%203%201%20day%20to%203%20month%20pathology%20%28p%2012-13%29%20data.pdf",
-                    "mediaType": "application/pdf"
+                    "mediaType": "application/pdf",
+                    "title": "Table 3 1 day to 3 month pathology (p 12-13) data.pdf"
                 },
                 {
-                    "title": "Table 3 18 mo pathol (p 13, 16), Table S2 (early death p 11) and S3 (epid and test p 17-18).pdf",
                     "downloadURL": "https://pasteur.epa.gov/uploads/228/Table%203%2018%20mo%20pathol%20%28p%2013%2C%2016%29%2C%20Table%20S2%20%28early%20death%20p%2011%29%20and%20S3%20%28epid%20and%20test%20p%2017-18%29.pdf",
-                    "mediaType": "application/pdf"
+                    "mediaType": "application/pdf",
+                    "title": "Table 3 18 mo pathol (p 13, 16), Table S2 (early death p 11) and S3 (epid and test p 17-18).pdf"
                 },
                 {
-                    "title": "Extra File Table S1 CBC data Gavett 2016 PFT.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/228/Extra%20File%20Table%20S1%20CBC%20data%20Gavett%202016%20PFT.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Extra File Table S1 CBC data Gavett 2016 PFT.xlsx"
                 },
                 {
-                    "title": "Extra File Figure S2 survival curves and cause of death Gavett 2016 PFT.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/228/Extra%20File%20Figure%20S2%20survival%20curves%20and%20cause%20of%20death%20Gavett%202016%20PFT.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Extra File Figure S2 survival curves and cause of death Gavett 2016 PFT.xlsx"
                 }
             ],
+            "identifier": "A-bvqj-228",
+            "keyword": [
+                "asbestos",
+                "Libby amphibole",
+                "amosite",
+                "inflammasome",
+                "inflammation",
+                "Inhalation exposures"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2016-08-23",
-            "references": [
-                "https://doi.org/10.1186/s12989-016-0130-z"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -44898,83 +44892,83 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1186/s12989-016-0130-z"
+            ],
+            "rights": null,
+            "title": "Tables and figures from Gavett 2016 paper in Particle and Fibre Toxicology"
         },
         {
-            "title": "Data for Cyphert, J Toxicol Environ Health A, 2016: Long-Term Toxicity of Naturally Occurring Asbestos in Male Fischer 344 Rats",
-            "description": "The data shown are raw values used in tables and figures published in Cyphert et al., J Toxicol Environ Health A, 2016. Besides the published paper which is included in the dataset, each file is clearly labeled with the table or figure number and 1 to 3 words indicating the subject of the table or figure. All table and figure files are excel spreadsheets which are clearly labeled with the data in columns. One word file has pathology notes used in the composition of figures 4 and 5. \n\nThis dataset is associated with the following publication:\nCyphert, J., M. McGee, A. Nyska, M. Schladweiler , U. Kodavanti , and S. Gavett. Long-Term Toxicity of Naturally Occurring Asbestos in Male Fischer 344 Rats.   JOURNAL OF TOXICOLOGY AND ENVIRONMENTAL HEALTH - PART A:  CURRENT ISSUES. Taylor & Francis, Inc., Philadelphia, PA, USA, 79(2): 49-60, (2016).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "A-vhj8-209",
-            "keyword": [
-                "Libby amphibole",
-                "chrysotile",
-                "tremolite",
-                "ferroactinolite",
-                "fibrosis",
-                "carcinogenesis"
-            ],
             "contactPoint": {
                 "fn": "Stephen Gavett",
                 "hasEmail": "mailto:gavett.stephen@epa.gov"
             },
+            "description": "The data shown are raw values used in tables and figures published in Cyphert et al., J Toxicol Environ Health A, 2016. Besides the published paper which is included in the dataset, each file is clearly labeled with the table or figure number and 1 to 3 words indicating the subject of the table or figure. All table and figure files are excel spreadsheets which are clearly labeled with the data in columns. One word file has pathology notes used in the composition of figures 4 and 5. \n\nThis dataset is associated with the following publication:\nCyphert, J., M. McGee, A. Nyska, M. Schladweiler , U. Kodavanti , and S. Gavett. Long-Term Toxicity of Naturally Occurring Asbestos in Male Fischer 344 Rats.   JOURNAL OF TOXICOLOGY AND ENVIRONMENTAL HEALTH - PART A:  CURRENT ISSUES. Taylor & Francis, Inc., Philadelphia, PA, USA, 79(2): 49-60, (2016).",
             "distribution": [
                 {
-                    "title": "Gavett_A-vhj8_published paper JTEHA 2016.pdf",
                     "downloadURL": "https://pasteur.epa.gov/uploads/209/Gavett_A-vhj8_published%20paper%20JTEHA%202016.pdf",
-                    "mediaType": "application/pdf"
+                    "mediaType": "application/pdf",
+                    "title": "Gavett_A-vhj8_published paper JTEHA 2016.pdf"
                 },
                 {
-                    "title": "Table 1 fiber size data Cyphert 2016 JTEHA.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/209/Table%201%20fiber%20size%20data%20Cyphert%202016%20JTEHA.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Table 1 fiber size data Cyphert 2016 JTEHA.xlsx"
                 },
                 {
-                    "title": "Figure 1 AB buxco data Cyphert 2016 JTEHA.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/209/Figure%201%20AB%20buxco%20data%20Cyphert%202016%20JTEHA.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Figure 1 AB buxco data Cyphert 2016 JTEHA.xlsx"
                 },
                 {
-                    "title": "Figure 1 CD flexivent data Cyphert 2016 JTEHA.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/209/Figure%201%20CD%20flexivent%20data%20Cyphert%202016%20JTEHA.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Figure 1 CD flexivent data Cyphert 2016 JTEHA.xlsx"
                 },
                 {
-                    "title": "Table 2 body weight survival data Cyphert 2016 JTEHA.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/209/Table%202%20body%20weight%20survival%20data%20Cyphert%202016%20JTEHA.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Table 2 body weight survival data Cyphert 2016 JTEHA.xlsx"
                 },
                 {
-                    "title": "Table 2 pathology findings Cyphert 2016 JTEHA.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/209/Table%202%20pathology%20findings%20Cyphert%202016%20JTEHA.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Table 2 pathology findings Cyphert 2016 JTEHA.xlsx"
                 },
                 {
-                    "title": "Figure 2 BAL cells data Cyphert 2016 JTEHA.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/209/Figure%202%20BAL%20cells%20data%20Cyphert%202016%20JTEHA.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Figure 2 BAL cells data Cyphert 2016 JTEHA.xlsx"
                 },
                 {
-                    "title": "Figure 3 BAL biochemistry data Cyphert 2016 JTEHA.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/209/Figure%203%20BAL%20biochemistry%20data%20Cyphert%202016%20JTEHA.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Figure 3 BAL biochemistry data Cyphert 2016 JTEHA.xlsx"
                 },
                 {
-                    "title": "Figures 4 and 5 pathology notes Cyphert 2016 JTEHA.docx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/209/Figures%204%20and%205%20pathology%20notes%20Cyphert%202016%20JTEHA.docx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+                    "title": "Figures 4 and 5 pathology notes Cyphert 2016 JTEHA.docx"
                 }
             ],
+            "identifier": "A-vhj8-209",
+            "keyword": [
+                "Libby amphibole",
+                "chrysotile",
+                "tremolite",
+                "ferroactinolite",
+                "fibrosis",
+                "carcinogenesis"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2016-08-18",
-            "references": [
-                "https://doi.org/10.1080/15287394.2015.1099123"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -44984,57 +44978,59 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1080/15287394.2015.1099123"
+            ],
+            "rights": null,
+            "title": "Data for Cyphert, J Toxicol Environ Health A, 2016: Long-Term Toxicity of Naturally Occurring Asbestos in Male Fischer 344 Rats"
         },
         {
-            "title": "CMAPS source apportionment",
-            "description": "This dataset includes concentrations of trace inorganic elements, ions, and organic/element carbon of PM collected from two sampling sites (GT Craig and Chippewa Lake) in Cleveland as well as PM source profiles/contributions to each sampling sites. \n\nThis dataset is associated with the following publication:\nKim, Y., T. Krantz, J. Mcgee, K. Kovalcik, R. Duvall, R. Willis, A. Kamal, M. Landis, G. Norris, and I. Gilmour. Chemical Composition and Source Apportionment of Size Fractionated Particulate Matter in Cleveland, Ohio, USA.   ENVIRONMENTAL POLLUTION. Elsevier Science Ltd, New York, NY, USA, 218: 1180-1190, (2016).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:094"
-            ],
-            "identifier": "A-ht7m-147",
-            "keyword": [
-                "cleveland",
-                "air pollution",
-                "source apportionment",
-                "urban",
-                "rural"
-            ],
             "contactPoint": {
                 "fn": "Matthew Gilmour",
                 "hasEmail": "mailto:gilmour.ian@epa.gov"
             },
+            "describedBy": "https://pasteur.epa.gov/uploads/147/documents/Dictionary.docx",
+            "describedByType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+            "description": "This dataset includes concentrations of trace inorganic elements, ions, and organic/element carbon of PM collected from two sampling sites (GT Craig and Chippewa Lake) in Cleveland as well as PM source profiles/contributions to each sampling sites. \n\nThis dataset is associated with the following publication:\nKim, Y., T. Krantz, J. Mcgee, K. Kovalcik, R. Duvall, R. Willis, A. Kamal, M. Landis, G. Norris, and I. Gilmour. Chemical Composition and Source Apportionment of Size Fractionated Particulate Matter in Cleveland, Ohio, USA.   ENVIRONMENTAL POLLUTION. Elsevier Science Ltd, New York, NY, USA, 218: 1180-1190, (2016).",
             "distribution": [
                 {
-                    "title": "Description.docx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/147/Description.docx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+                    "title": "Description.docx"
                 },
                 {
-                    "title": "Dictionary.docx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/147/Dictionary.docx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+                    "title": "Dictionary.docx"
                 },
                 {
-                    "title": "Research Data for Science Hub.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/147/Research%20Data%20for%20Science%20Hub.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Research Data for Science Hub.xlsx"
                 },
                 {
-                    "title": "Research Data for Science Hub.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/147/Research%20Data%20for%20Science%20Hub.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Research Data for Science Hub.xlsx"
                 }
             ],
+            "identifier": "A-ht7m-147",
+            "keyword": [
+                "cleveland",
+                "air pollution",
+                "source apportionment",
+                "urban",
+                "rural"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2016-07-27",
-            "references": [
-                "https://doi.org/10.1016/j.envpol.2016.08.073"
+            "programCode": [
+                "020:094"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -45045,43 +45041,43 @@
                     }
                 }
             },
-            "describedBy": "https://pasteur.epa.gov/uploads/147/documents/Dictionary.docx",
-            "describedByType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
+            "references": [
+                "https://doi.org/10.1016/j.envpol.2016.08.073"
+            ],
+            "rights": null,
+            "title": "CMAPS source apportionment"
         },
         {
-            "title": "QSARs for Plasma Protein Binding: Source Data and Predictions",
-            "description": "The dataset has all of the information used to create and evaluate 3 independent QSAR models for the fraction of a chemical unbound by plasma protein (Fub) for environmentally relevant chemicals. In vitro plasma protein values for 1245 pharmaceuticals and 406 ToxCast chemicals were collected from the literature (Obach 2008, Zhu 2013, Wetmore 2012, Wetmore 2015). The 21 descriptors calculated by MOE that were used in the models are included, as is an acid/base/neutral/zwitterions classification based on ionization percentages calculated in ADMET Predictor. Finally, the dataset includes the in silico Fub predictions for each chemical from the constructed k-nearest neighbor, support vector machine, and random forest QSAR models, as well as a consensus (average) prediction. \n\nThis dataset is associated with the following publication:\nIngle, B., R. Tornero-Velez, J. Nichols, and B. Veber. Informing the Human Plasma Protein Binding of Environmental Chemicals by Machine Learning in the Pharmaceutical Space: Applicability Domain and Limits of Predictability.   Journal of Chemical Information and Modeling. American Chemical Society, Washington, DC, USA, 56(11): 2243-2252, (2016).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "A-rbpk-569",
-            "keyword": [
-                "Environmental toxicology",
-                "plasma protein binding",
-                "machine learning",
-                "domain of applicability",
-                "quantitative structure activity relationship (QSAR)"
-            ],
             "contactPoint": {
                 "fn": "Rogelio Tornero-Velez",
                 "hasEmail": "mailto:tornero-velez.rogelio@epa.gov"
             },
+            "describedBy": "https://pasteur.epa.gov/uploads/569/documents/DataDictionary_PPB_JCIM.docx",
+            "describedByType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+            "description": "The dataset has all of the information used to create and evaluate 3 independent QSAR models for the fraction of a chemical unbound by plasma protein (Fub) for environmentally relevant chemicals. In vitro plasma protein values for 1245 pharmaceuticals and 406 ToxCast chemicals were collected from the literature (Obach 2008, Zhu 2013, Wetmore 2012, Wetmore 2015). The 21 descriptors calculated by MOE that were used in the models are included, as is an acid/base/neutral/zwitterions classification based on ionization percentages calculated in ADMET Predictor. Finally, the dataset includes the in silico Fub predictions for each chemical from the constructed k-nearest neighbor, support vector machine, and random forest QSAR models, as well as a consensus (average) prediction. \n\nThis dataset is associated with the following publication:\nIngle, B., R. Tornero-Velez, J. Nichols, and B. Veber. Informing the Human Plasma Protein Binding of Environmental Chemicals by Machine Learning in the Pharmaceutical Space: Applicability Domain and Limits of Predictability.   Journal of Chemical Information and Modeling. American Chemical Society, Washington, DC, USA, 56(11): 2243-2252, (2016).",
             "distribution": [
                 {
-                    "title": "PPB_JChemInfMod_Supp_AllData.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/569/PPB_JChemInfMod_Supp_AllData.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "PPB_JChemInfMod_Supp_AllData.xlsx"
                 }
             ],
+            "identifier": "A-rbpk-569",
+            "keyword": [
+                "Environmental toxicology",
+                "plasma protein binding",
+                "machine learning",
+                "domain of applicability",
+                "quantitative structure activity relationship (QSAR)"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2016-08-26",
-            "references": [
-                "https://doi.org/10.1021/acs.jcim.6b00291"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -45092,43 +45088,41 @@
                     }
                 }
             },
-            "describedBy": "https://pasteur.epa.gov/uploads/569/documents/DataDictionary_PPB_JCIM.docx",
-            "describedByType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
+            "references": [
+                "https://doi.org/10.1021/acs.jcim.6b00291"
+            ],
+            "rights": null,
+            "title": "QSARs for Plasma Protein Binding: Source Data and Predictions"
         },
         {
-            "title": "Multipollutant health effect simulations",
-            "description": "Resulting betas (health effects) from a variety of copollutant epidemiologic models used to analyze the impact of exposure measurement error on health effect estimates. \n\nThis dataset is associated with the following publication:\nDionisio , K., H.H. Chang, and L. Baxter. A simulation study to quantify the impacts of exposure measurement error on air pollution health risk estimates in copollutant time-series models..   ENVIRONMENTAL HEALTH. Academic Press Incorporated, Orlando, FL, USA, 15: 114, (2016).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:094"
-            ],
-            "identifier": "A-9kdf-573",
-            "keyword": [
-                "Exposure modeling",
-                "exposure measurement error",
-                "Exposure Assessment",
-                "bias",
-                "copollutant"
-            ],
             "contactPoint": {
                 "fn": "Kathie Dionisio",
                 "hasEmail": "mailto:dionisio.kathie@epa.gov"
             },
+            "description": "Resulting betas (health effects) from a variety of copollutant epidemiologic models used to analyze the impact of exposure measurement error on health effect estimates. \n\nThis dataset is associated with the following publication:\nDionisio , K., H.H. Chang, and L. Baxter. A simulation study to quantify the impacts of exposure measurement error on air pollution health risk estimates in copollutant time-series models..   ENVIRONMENTAL HEALTH. Academic Press Incorporated, Orlando, FL, USA, 15: 114, (2016).",
             "distribution": [
                 {
-                    "title": "RunSimBatchv2_2016August15.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/573/RunSimBatchv2_2016August15.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "RunSimBatchv2_2016August15.xlsx"
                 }
             ],
+            "identifier": "A-9kdf-573",
+            "keyword": [
+                "Exposure modeling",
+                "exposure measurement error",
+                "Exposure Assessment",
+                "bias",
+                "copollutant"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2016-08-15",
-            "references": [
-                "https://doi.org/10.1186/s12940-016-0186-0"
+            "programCode": [
+                "020:094"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -45138,39 +45132,39 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1186/s12940-016-0186-0"
+            ],
+            "rights": null,
+            "title": "Multipollutant health effect simulations"
         },
         {
-            "title": "Assessing model characterization of single source secondary pollutant impacts using 2013 SENEX field study measurements",
-            "description": "The dataset consists of 4 comma-separated value (csv) text files and 3 netCDF data files. Each csv file contains the observed and CMAQ modeled gas and aerosol concentrations collected during the SENEX field campaign. The netCDF files contain ground layer modeled single source contributions. The headers of each file contain the variable names for each column. An additional data dictionary with variable descriptions and units for the csv files is included with the data along with a file detailing the mapping of files to figures in the manuscript. \n\nThis dataset is associated with the following publication:\nBaker, K., and M. Woody. Assessing Model Characterization of Single Source Secondary Pollutant Impacts Using 2013 SENEX Field Study Measurements.   ENVIRONMENTAL SCIENCE & TECHNOLOGY. American Chemical Society, Washington, DC, USA, 51(7): 3833-3842, (2017).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:094"
-            ],
-            "identifier": "A-mw74-549",
-            "keyword": [
-                "CMAQ",
-                "CMAQ ISAM"
-            ],
             "contactPoint": {
                 "fn": "Matthew Woody",
                 "hasEmail": "mailto:woody.matthew@epa.gov"
             },
+            "description": "The dataset consists of 4 comma-separated value (csv) text files and 3 netCDF data files. Each csv file contains the observed and CMAQ modeled gas and aerosol concentrations collected during the SENEX field campaign. The netCDF files contain ground layer modeled single source contributions. The headers of each file contain the variable names for each column. An additional data dictionary with variable descriptions and units for the csv files is included with the data along with a file detailing the mapping of files to figures in the manuscript. \n\nThis dataset is associated with the following publication:\nBaker, K., and M. Woody. Assessing Model Characterization of Single Source Secondary Pollutant Impacts Using 2013 SENEX Field Study Measurements.   ENVIRONMENTAL SCIENCE & TECHNOLOGY. American Chemical Society, Washington, DC, USA, 51(7): 3833-3842, (2017).",
             "distribution": [
                 {
-                    "title": "data.zip",
                     "downloadURL": "https://pasteur.epa.gov/uploads/549/data.zip",
-                    "mediaType": "application/x-zip-compressed"
+                    "mediaType": "application/x-zip-compressed",
+                    "title": "data.zip"
                 }
             ],
+            "identifier": "A-mw74-549",
+            "keyword": [
+                "CMAQ",
+                "CMAQ ISAM"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2016-09-19",
-            "references": [
-                "https://doi.org/10.1021/acs.est.6b05069"
+            "programCode": [
+                "020:094"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -45180,19 +45174,29 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1021/acs.est.6b05069"
+            ],
+            "rights": null,
+            "title": "Assessing model characterization of single source secondary pollutant impacts using 2013 SENEX field study measurements"
         },
         {
-            "title": "Development of the crop residue and rangeland burning in the 2014 National Emissions Inventory using information from multiple sources",
-            "description": "This workbook contains all the activity data, emission factor data, and ancillary data used to compute crop residue  burning and rangeland emissions for the 2014 NEI as described in the journal article (see citation) in addition to the data associated with Figures 1-5. \n\nThis dataset is associated with the following publication:\nPouliot, G., V. Rao, J. McCarty, and A. Soja. Development of the crop residue and rangeland burning in the 2014 National Emissions Inventory using information from multiple sources.   JOURNAL OF THE AIR & WASTE MANAGEMENT ASSOCIATION. Air & Waste Management Association, Pittsburgh, PA, USA, 67(5): 613-622, (2017).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:094"
+            "contactPoint": {
+                "fn": "George Pouliot",
+                "hasEmail": "mailto:pouliot.george@epa.gov"
+            },
+            "description": "This workbook contains all the activity data, emission factor data, and ancillary data used to compute crop residue  burning and rangeland emissions for the 2014 NEI as described in the journal article (see citation) in addition to the data associated with Figures 1-5. \n\nThis dataset is associated with the following publication:\nPouliot, G., V. Rao, J. McCarty, and A. Soja. Development of the crop residue and rangeland burning in the 2014 National Emissions Inventory using information from multiple sources.   JOURNAL OF THE AIR & WASTE MANAGEMENT ASSOCIATION. Air & Waste Management Association, Pittsburgh, PA, USA, 67(5): 613-622, (2017).",
+            "distribution": [
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/516/Pouliot_A-4b8m_Dataset_20170307.xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Pouliot_A-4b8m_Dataset_20170307.xlsx"
+                }
             ],
             "identifier": "A-4b8m-516",
             "keyword": [
@@ -45203,20 +45207,10 @@
                 "Cropland data Layer",
                 "Hazard Mapping System"
             ],
-            "contactPoint": {
-                "fn": "George Pouliot",
-                "hasEmail": "mailto:pouliot.george@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "Pouliot_A-4b8m_Dataset_20170307.xlsx",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/516/Pouliot_A-4b8m_Dataset_20170307.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2015-08-25",
-            "references": [
-                "https://doi.org/10.1080/10962247.2016.1268982"
+            "programCode": [
+                "020:094"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -45226,19 +45220,29 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1080/10962247.2016.1268982"
+            ],
+            "rights": null,
+            "title": "Development of the crop residue and rangeland burning in the 2014 National Emissions Inventory using information from multiple sources"
         },
         {
-            "title": "Changes in Landscape Greenness and Climatic Factors over 25 Years (1989\u20132013) in the USA",
-            "description": "The asci files are the probability of the NDVI trend (slope) and the direction of the NDVI trend (+/-).  These files can be mapped in ArcMap using ArcToolbox (conversion tools and asci to raster).  The asci files are for maps in Figures 1,2 and 4 in the publication.\n\nFigures.xlsx; Contains 8 Figures, each in a sheet titled same as in the publication. Except for Figure 3, all figures contain information about labeling the axis in publication. \n\nThis dataset is associated with the following publication:\nNash, M., J. Wickham, J. Christensen, and T. Wade. Changes in Landscape Greenness and Climatic Factors over 25 Years (1989\u20132013) in the USA.   Remote Sensing. MDPI AG, Basel,  SWITZERLAND, 9(3): 295, (2017).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
+            "contactPoint": {
+                "fn": "Maliha Nash",
+                "hasEmail": "mailto:nash.maliha@epa.gov"
+            },
+            "description": "The asci files are the probability of the NDVI trend (slope) and the direction of the NDVI trend (+/-).  These files can be mapped in ArcMap using ArcToolbox (conversion tools and asci to raster).  The asci files are for maps in Figures 1,2 and 4 in the publication.\n\nFigures.xlsx; Contains 8 Figures, each in a sheet titled same as in the publication. Except for Figure 3, all figures contain information about labeling the axis in publication. \n\nThis dataset is associated with the following publication:\nNash, M., J. Wickham, J. Christensen, and T. Wade. Changes in Landscape Greenness and Climatic Factors over 25 Years (1989\u20132013) in the USA.   Remote Sensing. MDPI AG, Basel,  SWITZERLAND, 9(3): 295, (2017).",
+            "distribution": [
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/586/Nash_2017_data_ScinceHOP.zip",
+                    "mediaType": "application/octet-stream",
+                    "title": "Nash_2017_data_ScinceHOP.zip"
+                }
             ],
             "identifier": "A-prrq-586",
             "keyword": [
@@ -45249,20 +45253,10 @@
                 "climatic factors",
                 "autoregression model"
             ],
-            "contactPoint": {
-                "fn": "Maliha Nash",
-                "hasEmail": "mailto:nash.maliha@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "Nash_2017_data_ScinceHOP.zip",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/586/Nash_2017_data_ScinceHOP.zip",
-                    "mediaType": "application/octet-stream"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2017-03-21",
-            "references": [
-                "https://doi.org/10.3390/rs9030295"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -45272,19 +45266,35 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.3390/rs9030295"
+            ],
+            "rights": null,
+            "title": "Changes in Landscape Greenness and Climatic Factors over 25 Years (1989\u20132013) in the USA"
         },
         {
-            "title": "An integrated ecological modeling system for assessing impacts of multiple stressors on stream and riverine ecosystem services within river basins",
-            "description": "We demonstrate a novel, spatially explicit assessment of the current condition of aquatic ecosystem services, with limited sensitivity analysis for the atmospheric contaminant mercury. The Integrated Ecological Modeling System (IEMS) forecasts water quality and quantity, habitat suitability for aquatic biota, fish biomasses, population densities, productivities, and contamination by methylmercury across headwater watersheds. We applied this IEMS to the Coal River Basin (CRB), West Virginia (USA), an 8-digit hydrologic unit watershed, by simulating a network of 97 stream segments using the SWAT watershed model, a watershed mercury loading model, the WASP water quality model, the PiSCES fish community estimation model, a fish habitat suitability model, the BASS fish community and bioaccumulation model, and an ecoservices post-processer. Model application was facilitated by automated data retrieval and model setup and updated model wrappers and interfaces for data transfers between these models from a prior study. This companion study evaluates baseline predictions of ecoservices provided for 1990\u20132010 for the population of streams in the CRB and serves as a foundation for future model development. \n\nThis dataset is associated with the following publication:\nJohnston , J., C. Barber , K. Wolfe , M. Galvin , M. Cyterski , and R. Parmar. An integrated ecological modeling system for assessing impacts of multiple stressors on stream and riverine ecosystem services within river basins.   ECOLOGICAL MODELLING. Elsevier Science BV, Amsterdam,  NETHERLANDS, 354: 104-114, (2017).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:097"
+            "contactPoint": {
+                "fn": "John Johnston",
+                "hasEmail": "mailto:johnston.johnm@epa.gov"
+            },
+            "describedBy": "https://pasteur.epa.gov/uploads/555/documents/ESP_Output.txt",
+            "describedByType": "text/plain",
+            "description": "We demonstrate a novel, spatially explicit assessment of the current condition of aquatic ecosystem services, with limited sensitivity analysis for the atmospheric contaminant mercury. The Integrated Ecological Modeling System (IEMS) forecasts water quality and quantity, habitat suitability for aquatic biota, fish biomasses, population densities, productivities, and contamination by methylmercury across headwater watersheds. We applied this IEMS to the Coal River Basin (CRB), West Virginia (USA), an 8-digit hydrologic unit watershed, by simulating a network of 97 stream segments using the SWAT watershed model, a watershed mercury loading model, the WASP water quality model, the PiSCES fish community estimation model, a fish habitat suitability model, the BASS fish community and bioaccumulation model, and an ecoservices post-processer. Model application was facilitated by automated data retrieval and model setup and updated model wrappers and interfaces for data transfers between these models from a prior study. This companion study evaluates baseline predictions of ecoservices provided for 1990\u20132010 for the population of streams in the CRB and serves as a foundation for future model development. \n\nThis dataset is associated with the following publication:\nJohnston , J., C. Barber , K. Wolfe , M. Galvin , M. Cyterski , and R. Parmar. An integrated ecological modeling system for assessing impacts of multiple stressors on stream and riverine ecosystem services within river basins.   ECOLOGICAL MODELLING. Elsevier Science BV, Amsterdam,  NETHERLANDS, 354: 104-114, (2017).",
+            "distribution": [
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/555/Ecological%20Modeling%20Figures%20and%20Tables%20data.xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Ecological Modeling Figures and Tables data.xlsx"
+                },
+                {
+                    "accessURL": "https://www.epa.gov/ceam/3mra",
+                    "title": "https://www.epa.gov/ceam/3mra"
+                }
             ],
             "identifier": "A-612r-555",
             "keyword": [
@@ -45297,24 +45307,10 @@
                 "Freshwater provisioning",
                 "; multiple stressors"
             ],
-            "contactPoint": {
-                "fn": "John Johnston",
-                "hasEmail": "mailto:johnston.johnm@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "Ecological Modeling Figures and Tables data.xlsx",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/555/Ecological%20Modeling%20Figures%20and%20Tables%20data.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
-                },
-                {
-                    "title": "https://www.epa.gov/ceam/3mra",
-                    "accessURL": "https://www.epa.gov/ceam/3mra"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2017-04-11",
-            "references": [
-                "https://doi.org/10.1016/j.ecolmodel.2017.03.021"
+            "programCode": [
+                "020:097"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -45325,20 +45321,27 @@
                     }
                 }
             },
-            "describedBy": "https://pasteur.epa.gov/uploads/555/documents/ESP_Output.txt",
-            "describedByType": "text/plain"
+            "references": [
+                "https://doi.org/10.1016/j.ecolmodel.2017.03.021"
+            ],
+            "rights": null,
+            "title": "An integrated ecological modeling system for assessing impacts of multiple stressors on stream and riverine ecosystem services within river basins"
         },
         {
-            "title": "On the implications of aerosol liquid water and phase separation for organic aerosol mass",
-            "description": "This dataset contains data presented in the figures of the paper \"On the implications of aerosol liquid water and phase separation for organic aerosol mass\" published in Atmospheric Chemistry and Physics. It also links to the data archive of field observations. \n\nThis dataset is associated with the following publication:\nPye, H., B. Murphy, L. Xu, N. Ng, A. Carlton, H. Guo, R. Weber, P. Vasilakos, W. Appel, S. Budisulistiorini, J. Surratt, A. Nenes, W. Hu, J. Jimenez, G. saacman-VanWertz, P. Misztal, and A. Goldstein. On the implications of aerosol liquid water and phase separation for organic aerosol mass.   Atmospheric Chemistry and Physics. Copernicus Publications, Katlenburg-Lindau,  GERMANY, 17: 343-369, (2017).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:094"
+            "contactPoint": {
+                "fn": "Havala Pye",
+                "hasEmail": "mailto:pye.havala@epa.gov"
+            },
+            "description": "This dataset contains data presented in the figures of the paper \"On the implications of aerosol liquid water and phase separation for organic aerosol mass\" published in Atmospheric Chemistry and Physics. It also links to the data archive of field observations. \n\nThis dataset is associated with the following publication:\nPye, H., B. Murphy, L. Xu, N. Ng, A. Carlton, H. Guo, R. Weber, P. Vasilakos, W. Appel, S. Budisulistiorini, J. Surratt, A. Nenes, W. Hu, J. Jimenez, G. saacman-VanWertz, P. Misztal, and A. Goldstein. On the implications of aerosol liquid water and phase separation for organic aerosol mass.   Atmospheric Chemistry and Physics. Copernicus Publications, Katlenburg-Lindau,  GERMANY, 17: 343-369, (2017).",
+            "distribution": [
+                {
+                    "accessURL": "https://www.atmos-chem-phys.net/17/343/2017/acp-17-343-2017-assets.html",
+                    "title": "https://www.atmos-chem-phys.net/17/343/2017/acp-17-343-2017-assets.html"
+                }
             ],
             "identifier": "A-gf28-504",
             "keyword": [
@@ -45352,19 +45355,10 @@
                 "Southeastern USA",
                 "organic aerosol"
             ],
-            "contactPoint": {
-                "fn": "Havala Pye",
-                "hasEmail": "mailto:pye.havala@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "https://www.atmos-chem-phys.net/17/343/2017/acp-17-343-2017-assets.html",
-                    "accessURL": "https://www.atmos-chem-phys.net/17/343/2017/acp-17-343-2017-assets.html"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2017-01-06",
-            "references": [
-                "https://doi.org/10.5194/acp-17-343-2017"
+            "programCode": [
+                "020:094"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -45374,45 +45368,47 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.5194/acp-17-343-2017"
+            ],
+            "rights": null,
+            "title": "On the implications of aerosol liquid water and phase separation for organic aerosol mass"
         },
         {
-            "title": "Measured exposure metrics",
-            "description": "measured air pollution exposure metrics. \n\nThis dataset is associated with the following publication:\nBreen , M., T. Long , B. Schultz, R. Williams , J. Richmond-Bryant , M. Breen, J. Langstaff , R. Devlin , A. Schneider, J. Burke , S.A. Batterman, and Q.Y. Meng. Air Pollution Exposure Model for Individuals (EMI) in Health Studies: Evaluation for Ambient PM2.5 in Central North Carolina.   ENVIRONMENTAL SCIENCE & TECHNOLOGY. American Chemical Society, Washington, DC, USA, 49(24): 14184-14194, (2015).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "A-4f4v-187",
-            "keyword": [
-                "air pollution",
-                "exposure",
-                "human health"
-            ],
             "contactPoint": {
                 "fn": "Michael Breen",
                 "hasEmail": "mailto:breen.michael@epa.gov"
             },
+            "describedBy": "https://pasteur.epa.gov/uploads/187/documents/rtp_pm_data_dictionary.doc",
+            "describedByType": "application/msword",
+            "description": "measured air pollution exposure metrics. \n\nThis dataset is associated with the following publication:\nBreen , M., T. Long , B. Schultz, R. Williams , J. Richmond-Bryant , M. Breen, J. Langstaff , R. Devlin , A. Schneider, J. Burke , S.A. Batterman, and Q.Y. Meng. Air Pollution Exposure Model for Individuals (EMI) in Health Studies: Evaluation for Ambient PM2.5 in Central North Carolina.   ENVIRONMENTAL SCIENCE & TECHNOLOGY. American Chemical Society, Washington, DC, USA, 49(24): 14184-14194, (2015).",
             "distribution": [
                 {
-                    "title": "rtp_tads.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/187/rtp_tads.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "rtp_tads.xlsx"
                 },
                 {
-                    "title": "rtp_pm_data.xls",
                     "downloadURL": "https://pasteur.epa.gov/uploads/187/rtp_pm_data.xls",
-                    "mediaType": "application/vnd.ms-excel"
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "rtp_pm_data.xls"
                 }
             ],
+            "identifier": "A-4f4v-187",
+            "keyword": [
+                "air pollution",
+                "exposure",
+                "human health"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2015-06-05",
-            "references": [
-                "https://doi.org/10.1021/acs.est.5b02765"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -45423,43 +45419,41 @@
                     }
                 }
             },
-            "describedBy": "https://pasteur.epa.gov/uploads/187/documents/rtp_pm_data_dictionary.doc",
-            "describedByType": "application/msword"
+            "references": [
+                "https://doi.org/10.1021/acs.est.5b02765"
+            ],
+            "rights": null,
+            "title": "Measured exposure metrics"
         },
         {
-            "title": "GMAP Phoenix 2013 data",
-            "description": "mobile monitoring data from the 2013 Phoenix study. \n\nThis dataset is associated with the following publication:\nVenkatram, A., V. Isakov , P. Deshmukh, and R. Baldauf. Modeling the impact of solid noise barriers on near road air quality.   ATMOSPHERIC ENVIRONMENT. Elsevier Science Ltd, New York, NY, USA, 141: 462-469, (2016).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:094"
-            ],
-            "identifier": "A-nck9-431",
-            "keyword": [
-                "dispersion modeling",
-                "air quality",
-                "near road",
-                "noise barriers",
-                "traffic"
-            ],
             "contactPoint": {
                 "fn": "Vladilen Isakov",
                 "hasEmail": "mailto:isakov.vlad@epa.gov"
             },
+            "description": "mobile monitoring data from the 2013 Phoenix study. \n\nThis dataset is associated with the following publication:\nVenkatram, A., V. Isakov , P. Deshmukh, and R. Baldauf. Modeling the impact of solid noise barriers on near road air quality.   ATMOSPHERIC ENVIRONMENT. Elsevier Science Ltd, New York, NY, USA, 141: 462-469, (2016).",
             "distribution": [
                 {
-                    "title": "Phoenix2013data.zip",
                     "downloadURL": "https://pasteur.epa.gov/uploads/431/Phoenix2013data.zip",
-                    "mediaType": "application/x-zip-compressed"
+                    "mediaType": "application/x-zip-compressed",
+                    "title": "Phoenix2013data.zip"
                 }
             ],
+            "identifier": "A-nck9-431",
+            "keyword": [
+                "dispersion modeling",
+                "air quality",
+                "near road",
+                "noise barriers",
+                "traffic"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2014-12-22",
-            "references": [
-                "https://doi.org/10.1016/j.atmosenv.2016.07.005"
+            "programCode": [
+                "020:094"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -45469,19 +45463,29 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.atmosenv.2016.07.005"
+            ],
+            "rights": null,
+            "title": "GMAP Phoenix 2013 data"
         },
         {
-            "title": "Chemical Transport Model Simulations of Organic Aerosol in Southern California: Model Evaluation and Gasoline and Diesel Source Contributions",
-            "description": "Gasoline- and diesel-fueled engines are ubiquitous sources of air pollution in urban environments. They emit both primary particulate matter and precursor gases that react to form secondary particulate matter in the atmosphere. In this work, we use experimentally derived inputs and parameterizations to predict concentrations and properties of organic aerosol (OA) from mobile sources in southern California using a three-dimensional chemical transport model, the Community Multiscale Air Quality Model (CMAQ). The updated model includes secondary organic aerosol (SOA) formation from unspeciated intermediate volatility organic compounds (IVOC). Compared to the treatment of OA in the traditional version of CMAQ, which is commonly used for regulatory applications, the updated model did not significantly alter the predicted OA mass concentrations but it did substantially improve predictions of OA sources and composition (e.g., POA-SOA split), and ambient IVOC concentrations. The updated model, despite substantial differences in emissions and chemistry, performs similar to a recently released research version of CMAQ. Mobile sources are predicted to contribute about 30\u201340 % of the OA in southern California (half of which is SOA), making mobile sources the single largest source contributor to OA in southern California. The remainder of the OA is attributed to non-mobile anthropogenic sources (e.g., cooking, biomass burning) with biogenic sources contributing less than 5 % to the total OA. Gasoline sources are predicted to contribute about thirteen times more OA than diesel sources; this difference is driven by differences in SOA production. Model predictions highlight the need to better constrain multi-generational oxidation reactions in chemical transport models. \n\nThis dataset is associated with the following publication:\nJathar, S., M. Woody, H. Pye, K. Baker, and A. Robinson. Chemical transport model simulations of organic aerosol in southern California: model evaluation and gasoline and diesel source contributions.   Atmospheric Chemistry and Physics. Copernicus Publications, Katlenburg-Lindau,  GERMANY, 17: 4305-4318, (2017).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:094"
+            "contactPoint": {
+                "fn": "Havala Pye",
+                "hasEmail": "mailto:pye.havala@epa.gov"
+            },
+            "description": "Gasoline- and diesel-fueled engines are ubiquitous sources of air pollution in urban environments. They emit both primary particulate matter and precursor gases that react to form secondary particulate matter in the atmosphere. In this work, we use experimentally derived inputs and parameterizations to predict concentrations and properties of organic aerosol (OA) from mobile sources in southern California using a three-dimensional chemical transport model, the Community Multiscale Air Quality Model (CMAQ). The updated model includes secondary organic aerosol (SOA) formation from unspeciated intermediate volatility organic compounds (IVOC). Compared to the treatment of OA in the traditional version of CMAQ, which is commonly used for regulatory applications, the updated model did not significantly alter the predicted OA mass concentrations but it did substantially improve predictions of OA sources and composition (e.g., POA-SOA split), and ambient IVOC concentrations. The updated model, despite substantial differences in emissions and chemistry, performs similar to a recently released research version of CMAQ. Mobile sources are predicted to contribute about 30\u201340 % of the OA in southern California (half of which is SOA), making mobile sources the single largest source contributor to OA in southern California. The remainder of the OA is attributed to non-mobile anthropogenic sources (e.g., cooking, biomass burning) with biogenic sources contributing less than 5 % to the total OA. Gasoline sources are predicted to contribute about thirteen times more OA than diesel sources; this difference is driven by differences in SOA production. Model predictions highlight the need to better constrain multi-generational oxidation reactions in chemical transport models. \n\nThis dataset is associated with the following publication:\nJathar, S., M. Woody, H. Pye, K. Baker, and A. Robinson. Chemical transport model simulations of organic aerosol in southern California: model evaluation and gasoline and diesel source contributions.   Atmospheric Chemistry and Physics. Copernicus Publications, Katlenburg-Lindau,  GERMANY, 17: 4305-4318, (2017).",
+            "distribution": [
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/532/calnex_ivoc.zip",
+                    "mediaType": "application/x-zip-compressed",
+                    "title": "calnex_ivoc.zip"
+                }
             ],
             "identifier": "A-tmq4-532",
             "keyword": [
@@ -45495,20 +45499,10 @@
                 "SOA",
                 "Aerosol"
             ],
-            "contactPoint": {
-                "fn": "Havala Pye",
-                "hasEmail": "mailto:pye.havala@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "calnex_ivoc.zip",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/532/calnex_ivoc.zip",
-                    "mediaType": "application/x-zip-compressed"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2017-01-01",
-            "references": [
-                "https://doi.org/10.5194/acp-17-4305-2017"
+            "programCode": [
+                "020:094"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -45518,41 +45512,43 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.5194/acp-17-4305-2017"
+            ],
+            "rights": null,
+            "title": "Chemical Transport Model Simulations of Organic Aerosol in Southern California: Model Evaluation and Gasoline and Diesel Source Contributions"
         },
         {
-            "title": "CMAQv5.1 Base NEIv1 AQS hourly site compare files",
-            "description": "CMAQv5.1 Base NEIv1 AQS hourly sitex files containing hourly paired model/ob data for the AQS network. \n\nThis dataset is associated with the following publication:\nAppel, W., S. Napelenok, K. Foley, H. Pye, C. Hogrefe, D. Luecken, J. Bash, S. Roselle, J. Pleim, H. Foroutan, B. Hutzell, G. Pouliot, G. Sarwar, K. Fahey, B. Gantt, D. Kang, R. Mathur, D. Schwede, T. Spero, D. Wong, J. Young, and N. Heath. Description and evaluation of the Community Multiscale Air Quality (CMAQ) modeling system version 5.1.   Geoscientific Model Development. Copernicus Publications, Katlenburg-Lindau,  GERMANY, 10: 1703-1732, (2017).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:094"
-            ],
-            "identifier": "https://doi.org/10.23719/1500016",
-            "keyword": [
-                "CMAQ",
-                "WRF",
-                "model evaluation",
-                "Air Quality Model"
-            ],
             "contactPoint": {
                 "fn": "Keith Appel",
                 "hasEmail": "mailto:appel.wyat@epa.gov"
             },
+            "describedBy": "https://pasteur.epa.gov/uploads/10.23719/1500016/documents/WyatAppel_A-9zwc_Data_Dictionary.docx",
+            "describedByType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+            "description": "CMAQv5.1 Base NEIv1 AQS hourly sitex files containing hourly paired model/ob data for the AQS network. \n\nThis dataset is associated with the following publication:\nAppel, W., S. Napelenok, K. Foley, H. Pye, C. Hogrefe, D. Luecken, J. Bash, S. Roselle, J. Pleim, H. Foroutan, B. Hutzell, G. Pouliot, G. Sarwar, K. Fahey, B. Gantt, D. Kang, R. Mathur, D. Schwede, T. Spero, D. Wong, J. Young, and N. Heath. Description and evaluation of the Community Multiscale Air Quality (CMAQ) modeling system version 5.1.   Geoscientific Model Development. Copernicus Publications, Katlenburg-Lindau,  GERMANY, 10: 1703-1732, (2017).",
             "distribution": [
                 {
-                    "title": "CMAQv51_Base_NEIv1_AQS_Hourly_sitex.zip",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1500016/CMAQv51_Base_NEIv1_AQS_Hourly_sitex.zip",
-                    "mediaType": "application/x-zip-compressed"
+                    "mediaType": "application/x-zip-compressed",
+                    "title": "CMAQv51_Base_NEIv1_AQS_Hourly_sitex.zip"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1500016",
+            "keyword": [
+                "CMAQ",
+                "WRF",
+                "model evaluation",
+                "Air Quality Model"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2017-05-03",
-            "references": [
-                "https://doi.org/10.5194/gmd-10-1703-2017"
+            "programCode": [
+                "020:094"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -45563,52 +45559,52 @@
                     }
                 }
             },
-            "describedBy": "https://pasteur.epa.gov/uploads/10.23719/1500016/documents/WyatAppel_A-9zwc_Data_Dictionary.docx",
-            "describedByType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
+            "references": [
+                "https://doi.org/10.5194/gmd-10-1703-2017"
+            ],
+            "rights": null,
+            "title": "CMAQv5.1 Base NEIv1 AQS hourly site compare files"
         },
         {
-            "title": "ACONC Files",
-            "description": "ACONC files containing simulated ozone and PM2.5 fields that were used to create the model difference plots shown in the journal article. \n\nThis dataset is associated with the following publication:\nAppel, W., S. Napelenok, K. Foley, H. Pye, C. Hogrefe, D. Luecken, J. Bash, S. Roselle, J. Pleim, H. Foroutan, B. Hutzell, G. Pouliot, G. Sarwar, K. Fahey, B. Gantt, D. Kang, R. Mathur, D. Schwede, T. Spero, D. Wong, J. Young, and N. Heath. Description and evaluation of the Community Multiscale Air Quality (CMAQ) modeling system version 5.1.   Geoscientific Model Development. Copernicus Publications, Katlenburg-Lindau,  GERMANY, 10: 1703-1732, (2017).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:094"
-            ],
-            "identifier": "https://doi.org/10.23719/1500013",
-            "keyword": [
-                "CMAQ",
-                "WRF",
-                "model evaluation",
-                "Air Quality Model"
-            ],
             "contactPoint": {
                 "fn": "Keith Appel",
                 "hasEmail": "mailto:appel.wyat@epa.gov"
             },
+            "describedBy": "https://pasteur.epa.gov/uploads/10.23719/1500013/documents/WyatAppel_A-9zwc_Data_Dictionary.docx",
+            "describedByType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+            "description": "ACONC files containing simulated ozone and PM2.5 fields that were used to create the model difference plots shown in the journal article. \n\nThis dataset is associated with the following publication:\nAppel, W., S. Napelenok, K. Foley, H. Pye, C. Hogrefe, D. Luecken, J. Bash, S. Roselle, J. Pleim, H. Foroutan, B. Hutzell, G. Pouliot, G. Sarwar, K. Fahey, B. Gantt, D. Kang, R. Mathur, D. Schwede, T. Spero, D. Wong, J. Young, and N. Heath. Description and evaluation of the Community Multiscale Air Quality (CMAQ) modeling system version 5.1.   Geoscientific Model Development. Copernicus Publications, Katlenburg-Lindau,  GERMANY, 10: 1703-1732, (2017).",
             "distribution": [
                 {
-                    "title": "CMAQv502_Base_aconc.zip",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1500013/CMAQv502_Base_aconc.zip",
-                    "mediaType": "application/x-zip-compressed"
+                    "mediaType": "application/x-zip-compressed",
+                    "title": "CMAQv502_Base_aconc.zip"
                 },
                 {
-                    "title": "CMAQv51_Base_NEIv1_aconc.zip",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1500013/CMAQv51_Base_NEIv1_aconc.zip",
-                    "mediaType": "application/x-zip-compressed"
+                    "mediaType": "application/x-zip-compressed",
+                    "title": "CMAQv51_Base_NEIv1_aconc.zip"
                 },
                 {
-                    "title": "CMAQv51_Base_NEIv2_aconc.zip",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1500013/CMAQv51_Base_NEIv2_aconc.zip",
-                    "mediaType": "application/x-zip-compressed"
+                    "mediaType": "application/x-zip-compressed",
+                    "title": "CMAQv51_Base_NEIv2_aconc.zip"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1500013",
+            "keyword": [
+                "CMAQ",
+                "WRF",
+                "model evaluation",
+                "Air Quality Model"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2017-05-03",
-            "references": [
-                "https://doi.org/10.5194/gmd-10-1703-2017"
+            "programCode": [
+                "020:094"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -45619,52 +45615,52 @@
                     }
                 }
             },
-            "describedBy": "https://pasteur.epa.gov/uploads/10.23719/1500013/documents/WyatAppel_A-9zwc_Data_Dictionary.docx",
-            "describedByType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
+            "references": [
+                "https://doi.org/10.5194/gmd-10-1703-2017"
+            ],
+            "rights": null,
+            "title": "ACONC Files"
         },
         {
-            "title": "Site compare scripts and output",
-            "description": "Monthly site compare scripts and output used to generate the model/ob plots and statistics in the manuscript. The AQS hourly site compare output files are not included as they were too large to store on ScienceHub. The files contain paired model/ob values for the various air quality networks. \n\nThis dataset is associated with the following publication:\nAppel, W., S. Napelenok, K. Foley, H. Pye, C. Hogrefe, D. Luecken, J. Bash, S. Roselle, J. Pleim, H. Foroutan, B. Hutzell, G. Pouliot, G. Sarwar, K. Fahey, B. Gantt, D. Kang, R. Mathur, D. Schwede, T. Spero, D. Wong, J. Young, and N. Heath. Description and evaluation of the Community Multiscale Air Quality (CMAQ) modeling system version 5.1.   Geoscientific Model Development. Copernicus Publications, Katlenburg-Lindau,  GERMANY, 10: 1703-1732, (2017).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:094"
-            ],
-            "identifier": "https://doi.org/10.23719/1500018",
-            "keyword": [
-                "CMAQ",
-                "WRF",
-                "model evaluation",
-                "Air Quality Model"
-            ],
             "contactPoint": {
                 "fn": "Keith Appel",
                 "hasEmail": "mailto:appel.wyat@epa.gov"
             },
+            "describedBy": "https://pasteur.epa.gov/uploads/10.23719/1500018/documents/WyatAppel_A-9zwc_Data_Dictionary.docx",
+            "describedByType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+            "description": "Monthly site compare scripts and output used to generate the model/ob plots and statistics in the manuscript. The AQS hourly site compare output files are not included as they were too large to store on ScienceHub. The files contain paired model/ob values for the various air quality networks. \n\nThis dataset is associated with the following publication:\nAppel, W., S. Napelenok, K. Foley, H. Pye, C. Hogrefe, D. Luecken, J. Bash, S. Roselle, J. Pleim, H. Foroutan, B. Hutzell, G. Pouliot, G. Sarwar, K. Fahey, B. Gantt, D. Kang, R. Mathur, D. Schwede, T. Spero, D. Wong, J. Young, and N. Heath. Description and evaluation of the Community Multiscale Air Quality (CMAQ) modeling system version 5.1.   Geoscientific Model Development. Copernicus Publications, Katlenburg-Lindau,  GERMANY, 10: 1703-1732, (2017).",
             "distribution": [
                 {
-                    "title": "CMAQ_v502_Base_sitex.zip",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1500018/CMAQ_v502_Base_sitex.zip",
-                    "mediaType": "application/x-zip-compressed"
+                    "mediaType": "application/x-zip-compressed",
+                    "title": "CMAQ_v502_Base_sitex.zip"
                 },
                 {
-                    "title": "CMAQv5.1_Base_NEIv1_sitex.zip",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1500018/CMAQv5.1_Base_NEIv1_sitex.zip",
-                    "mediaType": "application/x-zip-compressed"
+                    "mediaType": "application/x-zip-compressed",
+                    "title": "CMAQv5.1_Base_NEIv1_sitex.zip"
                 },
                 {
-                    "title": "CMAQv5.1_Base_NEIv2_sitex.zip",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1500018/CMAQv5.1_Base_NEIv2_sitex.zip",
-                    "mediaType": "application/x-zip-compressed"
+                    "mediaType": "application/x-zip-compressed",
+                    "title": "CMAQv5.1_Base_NEIv2_sitex.zip"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1500018",
+            "keyword": [
+                "CMAQ",
+                "WRF",
+                "model evaluation",
+                "Air Quality Model"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2017-05-03",
-            "references": [
-                "https://doi.org/10.5194/gmd-10-1703-2017"
+            "programCode": [
+                "020:094"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -45675,42 +45671,42 @@
                     }
                 }
             },
-            "describedBy": "https://pasteur.epa.gov/uploads/10.23719/1500018/documents/WyatAppel_A-9zwc_Data_Dictionary.docx",
-            "describedByType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
+            "references": [
+                "https://doi.org/10.5194/gmd-10-1703-2017"
+            ],
+            "rights": null,
+            "title": "Site compare scripts and output"
         },
         {
-            "title": "CMAQv502 Base AQS Hourly site compare output",
-            "description": "Monthly AQS hourly site compare output files for the CMAQv502 Base simulation. Monthly files contain hourly paired model/ob data for the AQS network. These data were used in some of model/ob plot provided in the manuscript. \n\nThis dataset is associated with the following publication:\nAppel, W., S. Napelenok, K. Foley, H. Pye, C. Hogrefe, D. Luecken, J. Bash, S. Roselle, J. Pleim, H. Foroutan, B. Hutzell, G. Pouliot, G. Sarwar, K. Fahey, B. Gantt, D. Kang, R. Mathur, D. Schwede, T. Spero, D. Wong, J. Young, and N. Heath. Description and evaluation of the Community Multiscale Air Quality (CMAQ) modeling system version 5.1.   Geoscientific Model Development. Copernicus Publications, Katlenburg-Lindau,  GERMANY, 10: 1703-1732, (2017).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:094"
-            ],
-            "identifier": "https://doi.org/10.23719/1500015",
-            "keyword": [
-                "CMAQ",
-                "WRF",
-                "model evaluation",
-                "Air Quality Model"
-            ],
             "contactPoint": {
                 "fn": "Keith Appel",
                 "hasEmail": "mailto:appel.wyat@epa.gov"
             },
+            "describedBy": "https://pasteur.epa.gov/uploads/10.23719/1500015/documents/WyatAppel_A-9zwc_Data_Dictionary.docx",
+            "describedByType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+            "description": "Monthly AQS hourly site compare output files for the CMAQv502 Base simulation. Monthly files contain hourly paired model/ob data for the AQS network. These data were used in some of model/ob plot provided in the manuscript. \n\nThis dataset is associated with the following publication:\nAppel, W., S. Napelenok, K. Foley, H. Pye, C. Hogrefe, D. Luecken, J. Bash, S. Roselle, J. Pleim, H. Foroutan, B. Hutzell, G. Pouliot, G. Sarwar, K. Fahey, B. Gantt, D. Kang, R. Mathur, D. Schwede, T. Spero, D. Wong, J. Young, and N. Heath. Description and evaluation of the Community Multiscale Air Quality (CMAQ) modeling system version 5.1.   Geoscientific Model Development. Copernicus Publications, Katlenburg-Lindau,  GERMANY, 10: 1703-1732, (2017).",
             "distribution": [
                 {
-                    "title": "CMAQv5.0.2_Base_AQS_Hourly_sitex.zip",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1500015/CMAQv5.0.2_Base_AQS_Hourly_sitex.zip",
-                    "mediaType": "application/x-zip-compressed"
+                    "mediaType": "application/x-zip-compressed",
+                    "title": "CMAQv5.0.2_Base_AQS_Hourly_sitex.zip"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1500015",
+            "keyword": [
+                "CMAQ",
+                "WRF",
+                "model evaluation",
+                "Air Quality Model"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2017-05-03",
-            "references": [
-                "https://doi.org/10.5194/gmd-10-1703-2017"
+            "programCode": [
+                "020:094"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -45721,42 +45717,42 @@
                     }
                 }
             },
-            "describedBy": "https://pasteur.epa.gov/uploads/10.23719/1500015/documents/WyatAppel_A-9zwc_Data_Dictionary.docx",
-            "describedByType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
+            "references": [
+                "https://doi.org/10.5194/gmd-10-1703-2017"
+            ],
+            "rights": null,
+            "title": "CMAQv502 Base AQS Hourly site compare output"
         },
         {
-            "title": "CMAQv5.1 Base NEIv2 AQS Hourly site compare output",
-            "description": "CMAQv5.1 Base NEIv2 AQS Hourly site compare output containing paired model/ob values that were used for some of the plots in the manuscript. \n\nThis dataset is associated with the following publication:\nAppel, W., S. Napelenok, K. Foley, H. Pye, C. Hogrefe, D. Luecken, J. Bash, S. Roselle, J. Pleim, H. Foroutan, B. Hutzell, G. Pouliot, G. Sarwar, K. Fahey, B. Gantt, D. Kang, R. Mathur, D. Schwede, T. Spero, D. Wong, J. Young, and N. Heath. Description and evaluation of the Community Multiscale Air Quality (CMAQ) modeling system version 5.1.   Geoscientific Model Development. Copernicus Publications, Katlenburg-Lindau,  GERMANY, 10: 1703-1732, (2017).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:094"
-            ],
-            "identifier": "https://doi.org/10.23719/1500014",
-            "keyword": [
-                "CMAQ",
-                "WRF",
-                "model evaluation",
-                "Air Quality Model"
-            ],
             "contactPoint": {
                 "fn": "Keith Appel",
                 "hasEmail": "mailto:appel.wyat@epa.gov"
             },
+            "describedBy": "https://pasteur.epa.gov/uploads/10.23719/1500014/documents/WyatAppel_A-9zwc_Data_Dictionary.docx",
+            "describedByType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+            "description": "CMAQv5.1 Base NEIv2 AQS Hourly site compare output containing paired model/ob values that were used for some of the plots in the manuscript. \n\nThis dataset is associated with the following publication:\nAppel, W., S. Napelenok, K. Foley, H. Pye, C. Hogrefe, D. Luecken, J. Bash, S. Roselle, J. Pleim, H. Foroutan, B. Hutzell, G. Pouliot, G. Sarwar, K. Fahey, B. Gantt, D. Kang, R. Mathur, D. Schwede, T. Spero, D. Wong, J. Young, and N. Heath. Description and evaluation of the Community Multiscale Air Quality (CMAQ) modeling system version 5.1.   Geoscientific Model Development. Copernicus Publications, Katlenburg-Lindau,  GERMANY, 10: 1703-1732, (2017).",
             "distribution": [
                 {
-                    "title": "CMAQv5.1_Base_NEIv2_AQS_Hourly_sitex.zip",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1500014/CMAQv5.1_Base_NEIv2_AQS_Hourly_sitex.zip",
-                    "mediaType": "application/x-zip-compressed"
+                    "mediaType": "application/x-zip-compressed",
+                    "title": "CMAQv5.1_Base_NEIv2_AQS_Hourly_sitex.zip"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1500014",
+            "keyword": [
+                "CMAQ",
+                "WRF",
+                "model evaluation",
+                "Air Quality Model"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2017-05-03",
-            "references": [
-                "https://doi.org/10.5194/gmd-10-1703-2017"
+            "programCode": [
+                "020:094"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -45767,42 +45763,42 @@
                     }
                 }
             },
-            "describedBy": "https://pasteur.epa.gov/uploads/10.23719/1500014/documents/WyatAppel_A-9zwc_Data_Dictionary.docx",
-            "describedByType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
+            "references": [
+                "https://doi.org/10.5194/gmd-10-1703-2017"
+            ],
+            "rights": null,
+            "title": "CMAQv5.1 Base NEIv2 AQS Hourly site compare output"
         },
         {
-            "title": "CMAQv5.1 TUCL and RetroPhot ACONC files",
-            "description": "January and July monthly average ACONC files for the CMAQv5.1 TUCL and RetroPhot sensitivity runs that were performed and presented in the manuscript. \n\nThis dataset is associated with the following publication:\nAppel, W., S. Napelenok, K. Foley, H. Pye, C. Hogrefe, D. Luecken, J. Bash, S. Roselle, J. Pleim, H. Foroutan, B. Hutzell, G. Pouliot, G. Sarwar, K. Fahey, B. Gantt, D. Kang, R. Mathur, D. Schwede, T. Spero, D. Wong, J. Young, and N. Heath. Description and evaluation of the Community Multiscale Air Quality (CMAQ) modeling system version 5.1.   Geoscientific Model Development. Copernicus Publications, Katlenburg-Lindau,  GERMANY, 10: 1703-1732, (2017).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:094"
-            ],
-            "identifier": "https://doi.org/10.23719/1500017",
-            "keyword": [
-                "CMAQ",
-                "WRF",
-                "model evaluation",
-                "Air Quality Model"
-            ],
             "contactPoint": {
                 "fn": "Keith Appel",
                 "hasEmail": "mailto:appel.wyat@epa.gov"
             },
+            "describedBy": "https://pasteur.epa.gov/uploads/10.23719/1500017/documents/WyatAppel_A-9zwc_Data_Dictionary.docx",
+            "describedByType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+            "description": "January and July monthly average ACONC files for the CMAQv5.1 TUCL and RetroPhot sensitivity runs that were performed and presented in the manuscript. \n\nThis dataset is associated with the following publication:\nAppel, W., S. Napelenok, K. Foley, H. Pye, C. Hogrefe, D. Luecken, J. Bash, S. Roselle, J. Pleim, H. Foroutan, B. Hutzell, G. Pouliot, G. Sarwar, K. Fahey, B. Gantt, D. Kang, R. Mathur, D. Schwede, T. Spero, D. Wong, J. Young, and N. Heath. Description and evaluation of the Community Multiscale Air Quality (CMAQ) modeling system version 5.1.   Geoscientific Model Development. Copernicus Publications, Katlenburg-Lindau,  GERMANY, 10: 1703-1732, (2017).",
             "distribution": [
                 {
-                    "title": "CMAQv51_TUCL_RetroPhot_ACONC.zip",
                     "downloadURL": "https://pasteur.epa.gov/uploads/10.23719/1500017/CMAQv51_TUCL_RetroPhot_ACONC.zip",
-                    "mediaType": "application/x-zip-compressed"
+                    "mediaType": "application/x-zip-compressed",
+                    "title": "CMAQv51_TUCL_RetroPhot_ACONC.zip"
                 }
             ],
+            "identifier": "https://doi.org/10.23719/1500017",
+            "keyword": [
+                "CMAQ",
+                "WRF",
+                "model evaluation",
+                "Air Quality Model"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2017-05-04",
-            "references": [
-                "https://doi.org/10.5194/gmd-10-1703-2017"
+            "programCode": [
+                "020:094"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -45813,35 +45809,35 @@
                     }
                 }
             },
-            "describedBy": "https://pasteur.epa.gov/uploads/10.23719/1500017/documents/WyatAppel_A-9zwc_Data_Dictionary.docx",
-            "describedByType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
+            "references": [
+                "https://doi.org/10.5194/gmd-10-1703-2017"
+            ],
+            "rights": null,
+            "title": "CMAQv5.1 TUCL and RetroPhot ACONC files"
         },
         {
-            "title": "Complex conductivity results to silver nanoparticles in partically saturated laboratory columns",
-            "description": "Laboratory complex conductivity data from partially saturated sand columns with silver nanoparticles. This dataset is not publicly accessible because: It involves two universities and the EPA.  The EPA collaborated in the research; but did not provide funding.  The data are the property of the universities. It can be accessed through the following means: The authors can be contacted individually for the data. Format: The data will be in xlsx format. \n\nThis dataset is associated with the following publication:\nAbdel Aal, G., E. Atekwana, and D. Werkema. Complex conductivity response to silver nanoparticles in partially saturated sand columns.   JOURNAL OF APPLIED GEOPHYSICS. Elsevier Science Ltd, New York, NY, USA, 137: 73-81, (2017).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:095"
-            ],
+            "contactPoint": {
+                "fn": "Douglas Werkema",
+                "hasEmail": "mailto:werkema.d@epa.gov"
+            },
+            "describedBy": "https://pasteur.epa.gov/uploads/580/documents/Abdel%20Aal%20et%20al%20nano%20vadose%20zone%20data%20dictionary.xlsx",
+            "describedByType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+            "description": "Laboratory complex conductivity data from partially saturated sand columns with silver nanoparticles. This dataset is not publicly accessible because: It involves two universities and the EPA.  The EPA collaborated in the research; but did not provide funding.  The data are the property of the universities. It can be accessed through the following means: The authors can be contacted individually for the data. Format: The data will be in xlsx format. \n\nThis dataset is associated with the following publication:\nAbdel Aal, G., E. Atekwana, and D. Werkema. Complex conductivity response to silver nanoparticles in partially saturated sand columns.   JOURNAL OF APPLIED GEOPHYSICS. Elsevier Science Ltd, New York, NY, USA, 137: 73-81, (2017).",
+            "distribution": [],
             "identifier": "A-m0cz-580",
             "keyword": [
                 "nanosilver",
                 "complex conductivity",
                 "Nanoparticles"
             ],
-            "contactPoint": {
-                "fn": "Douglas Werkema",
-                "hasEmail": "mailto:werkema.d@epa.gov"
-            },
-            "distribution": [],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2016-11-14",
-            "references": [
-                "https://doi.org/10.1016/j.jappgeo.2016.12.013"
+            "programCode": [
+                "020:095"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -45852,20 +45848,30 @@
                     }
                 }
             },
-            "describedBy": "https://pasteur.epa.gov/uploads/580/documents/Abdel%20Aal%20et%20al%20nano%20vadose%20zone%20data%20dictionary.xlsx",
-            "describedByType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+            "references": [
+                "https://doi.org/10.1016/j.jappgeo.2016.12.013"
+            ],
+            "rights": null,
+            "title": "Complex conductivity results to silver nanoparticles in partically saturated laboratory columns"
         },
         {
-            "title": "Chemical Alterations of Pb using Flue Gas Desulfurization Gypsum (FGDG) in two contaminated soils",
-            "description": "The data include chemical composition of Pb contaminated soils by adding FGDG as an amendment.  The data shows the changes in Pb speciation to sulfur based minerals. \n\nThis dataset is associated with the following publication:\nKoralegedara, N., S. Al-Abed, S. Rodrigo, R. Karna, K. Scheckel, and D. Dionysiou. Alterations of lead speciation by sulfate from addition of flue gas desulfurization gypsum (FGDG) in two contaminated soils.  D. Barcelo  SCIENCE OF THE TOTAL ENVIRONMENT. Elsevier BV, AMSTERDAM,  NETHERLANDS, 575: 1522-1529, (2017).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:097"
+            "contactPoint": {
+                "fn": "Souhail Al-Abed",
+                "hasEmail": "mailto:al-abed.souhail@epa.gov"
+            },
+            "describedBy": "https://pasteur.epa.gov/uploads/590/documents/data%20dictionary.xlsx",
+            "describedByType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+            "description": "The data include chemical composition of Pb contaminated soils by adding FGDG as an amendment.  The data shows the changes in Pb speciation to sulfur based minerals. \n\nThis dataset is associated with the following publication:\nKoralegedara, N., S. Al-Abed, S. Rodrigo, R. Karna, K. Scheckel, and D. Dionysiou. Alterations of lead speciation by sulfate from addition of flue gas desulfurization gypsum (FGDG) in two contaminated soils.  D. Barcelo  SCIENCE OF THE TOTAL ENVIRONMENT. Elsevier BV, AMSTERDAM,  NETHERLANDS, 575: 1522-1529, (2017).",
+            "distribution": [
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/590/Pb%20manuscript%20Metadata%20data%20tables%20with%20data%20dictionary%202016%20-%20Copy.xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Pb manuscript Metadata data tables with data dictionary 2016 - Copy.xlsx"
+                }
             ],
             "identifier": "A-t775-590",
             "keyword": [
@@ -45876,20 +45882,10 @@
                 "humic acid bound Pb",
                 "leadhillite"
             ],
-            "contactPoint": {
-                "fn": "Souhail Al-Abed",
-                "hasEmail": "mailto:al-abed.souhail@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "Pb manuscript Metadata data tables with data dictionary 2016 - Copy.xlsx",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/590/Pb%20manuscript%20Metadata%20data%20tables%20with%20data%20dictionary%202016%20-%20Copy.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2016-10-06",
-            "references": [
-                "https://doi.org/10.1016/j.scitotenv.2016.10.027"
+            "programCode": [
+                "020:097"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -45900,20 +45896,30 @@
                     }
                 }
             },
-            "describedBy": "https://pasteur.epa.gov/uploads/590/documents/data%20dictionary.xlsx",
-            "describedByType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+            "references": [
+                "https://doi.org/10.1016/j.scitotenv.2016.10.027"
+            ],
+            "rights": null,
+            "title": "Chemical Alterations of Pb using Flue Gas Desulfurization Gypsum (FGDG) in two contaminated soils"
         },
         {
-            "title": "Experimental and fate and transport model simulation results of Se and B released from FGDG, soil and soil-FGDG mixture. ",
-            "description": "The leachate concentrations of Se and B released from FGDG, soil and soil-FGDG mixture obtained from EPA-method 1314 is included in the data set. The non-equilibrium partitioning coefficients calculated based on the experimental data also included along with the predicted NPC values calculated using a regression model based on a power function. Long term environmental release of Se and B in agricultural field and a landfill calculated using fate and transport model simulation also included in the data set. \n\nThis dataset is associated with the following publication:\nKoralegedara, N., S. Al-Abed , M. Arambewela, and D. Dionysiou. Impact of Leaching Conditions on Constituents Release from Flue Gas Desulfurization Gypsum (FGDG) and FGDG-Soil Mixture.  Edith Rene, Robin Gerlach, Peter Galaz, Davide Zannoni and Piet Lens  JOURNAL OF ENVIRONMENTAL MANAGEMENT. Elsevier Science Ltd, New York, NY, USA, 324: 83-93, (2017).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
+            "contactPoint": {
+                "fn": "Souhail Al-Abed",
+                "hasEmail": "mailto:al-abed.souhail@epa.gov"
+            },
+            "describedBy": "https://pasteur.epa.gov/uploads/636/documents/Data%20dictionary-1.xlsx",
+            "describedByType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+            "description": "The leachate concentrations of Se and B released from FGDG, soil and soil-FGDG mixture obtained from EPA-method 1314 is included in the data set. The non-equilibrium partitioning coefficients calculated based on the experimental data also included along with the predicted NPC values calculated using a regression model based on a power function. Long term environmental release of Se and B in agricultural field and a landfill calculated using fate and transport model simulation also included in the data set. \n\nThis dataset is associated with the following publication:\nKoralegedara, N., S. Al-Abed , M. Arambewela, and D. Dionysiou. Impact of Leaching Conditions on Constituents Release from Flue Gas Desulfurization Gypsum (FGDG) and FGDG-Soil Mixture.  Edith Rene, Robin Gerlach, Peter Galaz, Davide Zannoni and Piet Lens  JOURNAL OF ENVIRONMENTAL MANAGEMENT. Elsevier Science Ltd, New York, NY, USA, 324: 83-93, (2017).",
+            "distribution": [
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/636/FGDG%20manuscript%20Metadata%20data%20tables%20with%20data%20dictionary%202016%20-%20Copy.xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "FGDG manuscript Metadata data tables with data dictionary 2016 - Copy.xlsx"
+                }
             ],
             "identifier": "A-g1kb-636",
             "keyword": [
@@ -45924,20 +45930,10 @@
                 "Selenium",
                 "Boron"
             ],
-            "contactPoint": {
-                "fn": "Souhail Al-Abed",
-                "hasEmail": "mailto:al-abed.souhail@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "FGDG manuscript Metadata data tables with data dictionary 2016 - Copy.xlsx",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/636/FGDG%20manuscript%20Metadata%20data%20tables%20with%20data%20dictionary%202016%20-%20Copy.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2015-11-02",
-            "references": [
-                "https://doi.org/10.1016/j.jhazmat.2016.01.019"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -45948,20 +45944,28 @@
                     }
                 }
             },
-            "describedBy": "https://pasteur.epa.gov/uploads/636/documents/Data%20dictionary-1.xlsx",
-            "describedByType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+            "references": [
+                "https://doi.org/10.1016/j.jhazmat.2016.01.019"
+            ],
+            "rights": null,
+            "title": "Experimental and fate and transport model simulation results of Se and B released from FGDG, soil and soil-FGDG mixture. "
         },
         {
-            "title": "Dataset for Probabilistic estimation of residential air exchange rates for population-based exposure modeling",
-            "description": "This dataset provides the city-specific air exchange rate measurements, modeled, literature-based as well as housing characteristics. \n\nThis dataset is associated with the following publication:\nBaxter, L., C. Stallings, L. Smith, and J. Burke. Probabilistic estimation of residential air exchange rates for population-based human exposure modeling.   Journal of Exposure Science and Environmental Epidemiology. Nature Publishing Group, London,  UK, 27: 227-234, (2017).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:094"
+            "contactPoint": {
+                "fn": "Janet Burke-Norris",
+                "hasEmail": "mailto:burke.janet@epa.gov"
+            },
+            "description": "This dataset provides the city-specific air exchange rate measurements, modeled, literature-based as well as housing characteristics. \n\nThis dataset is associated with the following publication:\nBaxter, L., C. Stallings, L. Smith, and J. Burke. Probabilistic estimation of residential air exchange rates for population-based human exposure modeling.   Journal of Exposure Science and Environmental Epidemiology. Nature Publishing Group, London,  UK, 27: 227-234, (2017).",
+            "distribution": [
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/613/Burke%20A-n5tv%20dataset.xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Burke A-n5tv dataset.xlsx"
+                }
             ],
             "identifier": "A-n5tv-613",
             "keyword": [
@@ -45972,20 +45976,10 @@
                 "infiltration",
                 "model evaluation"
             ],
-            "contactPoint": {
-                "fn": "Janet Burke-Norris",
-                "hasEmail": "mailto:burke.janet@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "Burke A-n5tv dataset.xlsx",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/613/Burke%20A-n5tv%20dataset.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2014-11-25",
-            "references": [
-                "https://doi.org/10.1038/jes.2016.49"
+            "programCode": [
+                "020:094"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -45995,19 +45989,31 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1038/jes.2016.49"
+            ],
+            "rights": null,
+            "title": "Dataset for Probabilistic estimation of residential air exchange rates for population-based exposure modeling"
         },
         {
-            "title": "Temperature profiles of three types CNTs (SWCNT, MWCNT and MWCNT-COOH) loaded environmental matrices generated from a microwave induced heating quantification method",
-            "description": "Relationships of temperature and CNT mass (SWCNT, MWCNT, MWCNT-COOH) were developed for three environmental matrices (sand, soil and sludge) spiked with known amounts of different types of CNTs that were then irradiated in a microwave at low energies (70-149 W) for a short time (15-30 sec). Temperature rises data were recorded for CNT loaded environmental samples with excess of inorganic/organic carbon and other carbonaceous nanomaterials (C60, GAC and GO). \n\nThis dataset is associated with the following publication:\nHe, Y., S. Al-Abed, and D. Dionysiou. Quantification of Carbon Nanotubes in Different Environmental Matrices by a Microwave Induced Heating Method.  D. Barcelo, and Jay Gan  SCIENCE OF THE TOTAL ENVIRONMENT. Elsevier BV, AMSTERDAM,  NETHERLANDS, 580: 509-517, (2017).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
+            "contactPoint": {
+                "fn": "Souhail Al-Abed",
+                "hasEmail": "mailto:al-abed.souhail@epa.gov"
+            },
+            "describedBy": "https://pasteur.epa.gov/uploads/639/documents/Data%20Dictionary.xlsx",
+            "describedByType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+            "description": "Relationships of temperature and CNT mass (SWCNT, MWCNT, MWCNT-COOH) were developed for three environmental matrices (sand, soil and sludge) spiked with known amounts of different types of CNTs that were then irradiated in a microwave at low energies (70-149 W) for a short time (15-30 sec). Temperature rises data were recorded for CNT loaded environmental samples with excess of inorganic/organic carbon and other carbonaceous nanomaterials (C60, GAC and GO). \n\nThis dataset is associated with the following publication:\nHe, Y., S. Al-Abed, and D. Dionysiou. Quantification of Carbon Nanotubes in Different Environmental Matrices by a Microwave Induced Heating Method.  D. Barcelo, and Jay Gan  SCIENCE OF THE TOTAL ENVIRONMENT. Elsevier BV, AMSTERDAM,  NETHERLANDS, 580: 509-517, (2017).",
+            "distribution": [
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/639/Microwave_CNTs%20manuscript%20Metadata%20%20data%20tables%20with%20data%20dictionary%202016.xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Microwave_CNTs manuscript Metadata  data tables with data dictionary 2016.xlsx"
+                }
             ],
             "identifier": "A-zpd1-639",
             "keyword": [
@@ -46018,20 +46024,10 @@
                 "soil",
                 "Anaerobic sludge"
             ],
-            "contactPoint": {
-                "fn": "Souhail Al-Abed",
-                "hasEmail": "mailto:al-abed.souhail@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "Microwave_CNTs manuscript Metadata  data tables with data dictionary 2016.xlsx",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/639/Microwave_CNTs%20manuscript%20Metadata%20%20data%20tables%20with%20data%20dictionary%202016.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2016-10-03",
-            "references": [
-                "https://doi.org/10.1016/j.scitotenv.2016.11.205"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -46042,42 +46038,42 @@
                     }
                 }
             },
-            "describedBy": "https://pasteur.epa.gov/uploads/639/documents/Data%20Dictionary.xlsx",
-            "describedByType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+            "references": [
+                "https://doi.org/10.1016/j.scitotenv.2016.11.205"
+            ],
+            "rights": null,
+            "title": "Temperature profiles of three types CNTs (SWCNT, MWCNT and MWCNT-COOH) loaded environmental matrices generated from a microwave induced heating quantification method"
         },
         {
-            "title": "RW1",
-            "description": "Wind tunnel measurements of flow and dispersion from a simulated roadway with near-road solid barriers. \n\nThis dataset is associated with the following publication:\nAhangar, F., D. Heist, S. Perry, and A. Venkatram. Reduction of air pollution levels downwind of a road with an upwind noise barrier.   ATMOSPHERIC ENVIRONMENT. Elsevier Science Ltd, New York, NY, USA, 155: 1-10, (2017).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:094"
-            ],
-            "identifier": "A-dv4c-515",
-            "keyword": [
-                "dispersion modeling",
-                "near road",
-                "noise barriers",
-                "wind tunnel"
-            ],
             "contactPoint": {
                 "fn": "David Heist",
                 "hasEmail": "mailto:heist.david@epa.gov"
             },
+            "describedBy": "https://pasteur.epa.gov/uploads/515/documents/Heist%20A-dv4c-DataDictionaryRW1-20170307.docx",
+            "describedByType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+            "description": "Wind tunnel measurements of flow and dispersion from a simulated roadway with near-road solid barriers. \n\nThis dataset is associated with the following publication:\nAhangar, F., D. Heist, S. Perry, and A. Venkatram. Reduction of air pollution levels downwind of a road with an upwind noise barrier.   ATMOSPHERIC ENVIRONMENT. Elsevier Science Ltd, New York, NY, USA, 155: 1-10, (2017).",
             "distribution": [
                 {
-                    "title": "Heist A-dv4c-DataFiles_RW1-20170307.zip",
                     "downloadURL": "https://pasteur.epa.gov/uploads/515/Heist%20A-dv4c-DataFiles_RW1-20170307.zip",
-                    "mediaType": "application/x-zip-compressed"
+                    "mediaType": "application/x-zip-compressed",
+                    "title": "Heist A-dv4c-DataFiles_RW1-20170307.zip"
                 }
             ],
+            "identifier": "A-dv4c-515",
+            "keyword": [
+                "dispersion modeling",
+                "near road",
+                "noise barriers",
+                "wind tunnel"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2017-03-07",
-            "references": [
-                "https://doi.org/10.1016/j.atmosenv.2017.02.001"
+            "programCode": [
+                "020:094"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -46088,43 +46084,43 @@
                     }
                 }
             },
-            "describedBy": "https://pasteur.epa.gov/uploads/515/documents/Heist%20A-dv4c-DataDictionaryRW1-20170307.docx",
-            "describedByType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
+            "references": [
+                "https://doi.org/10.1016/j.atmosenv.2017.02.001"
+            ],
+            "rights": null,
+            "title": "RW1"
         },
         {
-            "title": "The Acute Toxicity of Major Ion Salts to Ceriodaphnia dubia: I. Influence of background water chemistry.",
-            "description": "This dataset provides concentration-response data and associated general chemistry conditions for 26 experiments consisting of 149 tests regarding the acute toxicity of major ions to Ceriodaphnia dubia in a variety of test waters; it also provides LC50 estimates and the estimated ion mixtures at the LC50 for each toxicity test. \n\nThis dataset is associated with the following publication:\nMount , D., R. Erickson , T. Highland , R. Hockett , D. Hoff , T. Norberg-King , K. Peterson, Z.  Polaske, and S. Wisniewski. The acute toxicity of major ion salts to Ceriodaphnia dubia: I. Influence of background water chemistry.   ENVIRONMENTAL TOXICOLOGY AND CHEMISTRY. Society of Environmental Toxicology and Chemistry, Pensacola, FL, USA, 35(12): 3039-3057, (2016).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:096"
-            ],
-            "identifier": "A-0gb6-45",
-            "keyword": [
-                "Ceriodaphnia dubia",
-                "Acute Toxicity",
-                "Test Water Chemistry Effects",
-                "Major Ion Toxicity",
-                "Freshwater"
-            ],
             "contactPoint": {
                 "fn": "Russell Erickson",
                 "hasEmail": "mailto:erickson.russell@epa.gov"
             },
+            "describedBy": "https://pasteur.epa.gov/uploads/45/documents/MEDIonToxPaper1_DataDictionary.docx",
+            "describedByType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+            "description": "This dataset provides concentration-response data and associated general chemistry conditions for 26 experiments consisting of 149 tests regarding the acute toxicity of major ions to Ceriodaphnia dubia in a variety of test waters; it also provides LC50 estimates and the estimated ion mixtures at the LC50 for each toxicity test. \n\nThis dataset is associated with the following publication:\nMount , D., R. Erickson , T. Highland , R. Hockett , D. Hoff , T. Norberg-King , K. Peterson, Z.  Polaske, and S. Wisniewski. The acute toxicity of major ion salts to Ceriodaphnia dubia: I. Influence of background water chemistry.   ENVIRONMENTAL TOXICOLOGY AND CHEMISTRY. Society of Environmental Toxicology and Chemistry, Pensacola, FL, USA, 35(12): 3039-3057, (2016).",
             "distribution": [
                 {
-                    "title": "MEDIonToxPaper1_Dataset.zip",
                     "downloadURL": "https://pasteur.epa.gov/uploads/45/MEDIonToxPaper1_Dataset.zip",
-                    "mediaType": "application/x-zip-compressed"
+                    "mediaType": "application/x-zip-compressed",
+                    "title": "MEDIonToxPaper1_Dataset.zip"
                 }
             ],
+            "identifier": "A-0gb6-45",
+            "keyword": [
+                "Ceriodaphnia dubia",
+                "Acute Toxicity",
+                "Test Water Chemistry Effects",
+                "Major Ion Toxicity",
+                "Freshwater"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2016-05-05",
-            "references": [
-                "https://doi.org/10.1002/etc.3487"
+            "programCode": [
+                "020:096"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -46135,43 +46131,41 @@
                     }
                 }
             },
-            "describedBy": "https://pasteur.epa.gov/uploads/45/documents/MEDIonToxPaper1_DataDictionary.docx",
-            "describedByType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
+            "references": [
+                "https://doi.org/10.1002/etc.3487"
+            ],
+            "rights": null,
+            "title": "The Acute Toxicity of Major Ion Salts to Ceriodaphnia dubia: I. Influence of background water chemistry."
         },
         {
-            "title": "Box photosynthesis modeling results for WRF/CMAQ LSM",
-            "description": "Box Photosynthesis model simulations for latent heat and ozone at 6 different FLUXNET sites. \n\nThis dataset is associated with the following publication:\nRan, L., J. Pleim, C. Song, L. Band, J. Walker, and F. Binkowski. A photosynthesis-based two-leaf canopy stomatal conductance model for meteorology and air quality modeling with WRF/CMAQ PX LSM.   JOURNAL OF GEOPHYSICAL RESEARCH-ATMOSPHERES. American Geophysical Union, Washington, DC, USA, 122(3): 1930-1952, (2017).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:094"
-            ],
-            "identifier": "A-w9h7-567",
-            "keyword": [
-                "photosynthesis",
-                "PX LSM",
-                "WRF/CMAQ",
-                "ozone deposition",
-                "air quality modeling"
-            ],
             "contactPoint": {
                 "fn": "Limei Ran",
                 "hasEmail": "mailto:ran.limei@epa.gov"
             },
+            "description": "Box Photosynthesis model simulations for latent heat and ozone at 6 different FLUXNET sites. \n\nThis dataset is associated with the following publication:\nRan, L., J. Pleim, C. Song, L. Band, J. Walker, and F. Binkowski. A photosynthesis-based two-leaf canopy stomatal conductance model for meteorology and air quality modeling with WRF/CMAQ PX LSM.   JOURNAL OF GEOPHYSICAL RESEARCH-ATMOSPHERES. American Geophysical Union, Washington, DC, USA, 122(3): 1930-1952, (2017).",
             "distribution": [
                 {
-                    "title": "EPA_science_hub_data.zip",
                     "downloadURL": "https://pasteur.epa.gov/uploads/567/EPA_science_hub_data.zip",
-                    "mediaType": "application/x-zip-compressed"
+                    "mediaType": "application/x-zip-compressed",
+                    "title": "EPA_science_hub_data.zip"
                 }
             ],
+            "identifier": "A-w9h7-567",
+            "keyword": [
+                "photosynthesis",
+                "PX LSM",
+                "WRF/CMAQ",
+                "ozone deposition",
+                "air quality modeling"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2017-04-27",
-            "references": [
-                "https://doi.org/10.1002/2016jd025583"
+            "programCode": [
+                "020:094"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -46181,52 +46175,52 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1002/2016jd025583"
+            ],
+            "rights": null,
+            "title": "Box photosynthesis modeling results for WRF/CMAQ LSM"
         },
         {
-            "title": "Data for manuscript titled \"Historical trends in PM2.5 related premature mortality during 1990-2010 across the northern hemisphere\"",
-            "description": "This manuscript has 6 figures:\r\nFigure 1 shows the modeling domain and includes a map with the different analysis sub-regions. Shapefiles to be used with ArcGIS for re-creating this figure is included. \r\n\r\nThe file named \u201cEHP_data_summary\u201d is and Excel file and includes the data used in creation of Figures 2-6.  \r\n\r\nNote that these data files are a result of extensive data processing of many terra-bytes of model output from the hemispheric WRF-CMAQ model.  The manuscript includes details on how this analysis was conducted, and other data-sets incorporated. \n\nThis dataset is associated with the following publication:\nWang, J., J. Xing , R. Mathur , J. Pleim , S. Wang, C. Hogrefe , M. Gan , D. Wong , and J. Hao. Historical Trends in PM2.5-Related Premature Mortality during 1990-2010 across the Northern Hemisphere.   ENVIRONMENTAL HEALTH PERSPECTIVES. National Institute of Environmental Health Sciences (NIEHS), Research Triangle Park, NC, USA, 125(3): 400\u2013408, (2017).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:094"
-            ],
-            "identifier": "A-t774-221",
-            "keyword": [
-                "Hemispheric CMAQ",
-                "PM2.5 long-term exposure",
-                "emission mitigation efficiency",
-                "Air quality trends",
-                "air pollution exposure"
-            ],
             "contactPoint": {
                 "fn": "Rohit Mathur",
                 "hasEmail": "mailto:mathur.rohit@epa.gov"
             },
+            "description": "This manuscript has 6 figures:\r\nFigure 1 shows the modeling domain and includes a map with the different analysis sub-regions. Shapefiles to be used with ArcGIS for re-creating this figure is included. \r\n\r\nThe file named \u201cEHP_data_summary\u201d is and Excel file and includes the data used in creation of Figures 2-6.  \r\n\r\nNote that these data files are a result of extensive data processing of many terra-bytes of model output from the hemispheric WRF-CMAQ model.  The manuscript includes details on how this analysis was conducted, and other data-sets incorporated. \n\nThis dataset is associated with the following publication:\nWang, J., J. Xing , R. Mathur , J. Pleim , S. Wang, C. Hogrefe , M. Gan , D. Wong , and J. Hao. Historical Trends in PM2.5-Related Premature Mortality during 1990-2010 across the Northern Hemisphere.   ENVIRONMENTAL HEALTH PERSPECTIVES. National Institute of Environmental Health Sciences (NIEHS), Research Triangle Park, NC, USA, 125(3): 400\u2013408, (2017).",
             "distribution": [
                 {
-                    "title": "EHP_data_Readme.docx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/221/EHP_data_Readme.docx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+                    "title": "EHP_data_Readme.docx"
                 },
                 {
-                    "title": "EHP_data_summary.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/221/EHP_data_summary.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "EHP_data_summary.xlsx"
                 },
                 {
-                    "title": "EHP_figure1_shapefile_for_ArcGIS.zip",
                     "downloadURL": "https://pasteur.epa.gov/uploads/221/EHP_figure1_shapefile_for_ArcGIS.zip",
-                    "mediaType": "application/x-zip-compressed"
+                    "mediaType": "application/x-zip-compressed",
+                    "title": "EHP_figure1_shapefile_for_ArcGIS.zip"
                 }
             ],
+            "identifier": "A-t774-221",
+            "keyword": [
+                "Hemispheric CMAQ",
+                "PM2.5 long-term exposure",
+                "emission mitigation efficiency",
+                "Air quality trends",
+                "air pollution exposure"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2015-10-01",
-            "references": [
-                "https://doi.org/10.1289/ehp298"
+            "programCode": [
+                "020:094"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -46236,19 +46230,29 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1289/ehp298"
+            ],
+            "rights": null,
+            "title": "Data for manuscript titled \"Historical trends in PM2.5 related premature mortality during 1990-2010 across the northern hemisphere\""
         },
         {
-            "title": "Data for Arsenic Paper",
-            "description": "Contains data related to Arsenate and Arsenite injections into chlorinated distribution system simulator. Contains data related to model to predict arsenate and arsenite aqueous and wall concentrations within a chlorinated water distribution system. \n\nThis dataset is associated with the following publication:\nBurkhardt, J., J. Szabo, S. Klosterman, J. Hall, and R. Murray. Modeling Fate and Transport of Arsenic in a Chlorinated Distribution System.   ENVIRONMENTAL MODELLING AND SOFTWARE. Elsevier Science Ltd, New York, NY, USA, 93(1): 322-331, (2017).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:060"
+            "contactPoint": {
+                "fn": "Jonathan Burkhardt",
+                "hasEmail": "mailto:burkhardt.jonathan@epa.gov"
+            },
+            "description": "Contains data related to Arsenate and Arsenite injections into chlorinated distribution system simulator. Contains data related to model to predict arsenate and arsenite aqueous and wall concentrations within a chlorinated water distribution system. \n\nThis dataset is associated with the following publication:\nBurkhardt, J., J. Szabo, S. Klosterman, J. Hall, and R. Murray. Modeling Fate and Transport of Arsenic in a Chlorinated Distribution System.   ENVIRONMENTAL MODELLING AND SOFTWARE. Elsevier Science Ltd, New York, NY, USA, 93(1): 322-331, (2017).",
+            "distribution": [
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/432/Burkhardt-Murray_SciHubData_ArsenicModelingPaper_2016.xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Burkhardt-Murray_SciHubData_ArsenicModelingPaper_2016.xlsx"
+                }
             ],
             "identifier": "A-n2zm-432",
             "keyword": [
@@ -46260,20 +46264,10 @@
                 "water distribution",
                 "adsorption"
             ],
-            "contactPoint": {
-                "fn": "Jonathan Burkhardt",
-                "hasEmail": "mailto:burkhardt.jonathan@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "Burkhardt-Murray_SciHubData_ArsenicModelingPaper_2016.xlsx",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/432/Burkhardt-Murray_SciHubData_ArsenicModelingPaper_2016.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2016-10-07",
-            "references": [
-                "https://doi.org/10.1016/j.envsoft.2017.03.016"
+            "programCode": [
+                "020:060"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -46283,49 +46277,51 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.envsoft.2017.03.016"
+            ],
+            "rights": null,
+            "title": "Data for Arsenic Paper"
         },
         {
-            "title": "Chemical Function Predictions for Tox21 Chemicals",
-            "description": "Random forest chemical function predictions for Tox21 chemicals in personal care products uses and \"other\" uses. \n\nThis dataset is associated with the following publication:\nIsaacs , K., M. Goldsmith, P. Egeghy , K. Phillips, R. Brooks, T. Hong, and J. Wambaugh. Characterization and prediction of chemical functions and weight fractions in consumer products.   Toxicology Reports. Elsevier B.V., Amsterdam,  NETHERLANDS, 3: 723-732, (2016).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:095"
-            ],
-            "identifier": "A-mpgn-485",
-            "keyword": [
-                "chemical function",
-                "Exposure modeling",
-                "chemical prioritization",
-                "consumer products",
-                "cosmetics",
-                "ExpoCast",
-                "machine learning"
-            ],
             "contactPoint": {
                 "fn": "Kristin Isaacs",
                 "hasEmail": "mailto:isaacs.kristin@epa.gov"
             },
+            "describedBy": "https://pasteur.epa.gov/uploads/485/documents/read_me_metadata_Tox21preds.docx",
+            "describedByType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+            "description": "Random forest chemical function predictions for Tox21 chemicals in personal care products uses and \"other\" uses. \n\nThis dataset is associated with the following publication:\nIsaacs , K., M. Goldsmith, P. Egeghy , K. Phillips, R. Brooks, T. Hong, and J. Wambaugh. Characterization and prediction of chemical functions and weight fractions in consumer products.   Toxicology Reports. Elsevier B.V., Amsterdam,  NETHERLANDS, 3: 723-732, (2016).",
             "distribution": [
                 {
-                    "title": "ALLPCPPREDS_080516.csv",
                     "downloadURL": "https://pasteur.epa.gov/uploads/485/ALLPCPPREDS_080516.csv",
-                    "mediaType": "application/vnd.ms-excel"
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "ALLPCPPREDS_080516.csv"
                 },
                 {
-                    "title": "ALLOTHERPREDS_080516.csv",
                     "downloadURL": "https://pasteur.epa.gov/uploads/485/ALLOTHERPREDS_080516.csv",
-                    "mediaType": "application/vnd.ms-excel"
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "ALLOTHERPREDS_080516.csv"
                 }
             ],
+            "identifier": "A-mpgn-485",
+            "keyword": [
+                "chemical function",
+                "Exposure modeling",
+                "chemical prioritization",
+                "consumer products",
+                "cosmetics",
+                "ExpoCast",
+                "machine learning"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2016-08-05",
-            "references": [
-                "https://doi.org/10.1016/j.toxrep.2016.08.011"
+            "programCode": [
+                "020:095"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -46336,20 +46332,30 @@
                     }
                 }
             },
-            "describedBy": "https://pasteur.epa.gov/uploads/485/documents/read_me_metadata_Tox21preds.docx",
-            "describedByType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
+            "references": [
+                "https://doi.org/10.1016/j.toxrep.2016.08.011"
+            ],
+            "rights": null,
+            "title": "Chemical Function Predictions for Tox21 Chemicals"
         },
         {
-            "title": "Chemical product and function dataset",
-            "description": "Merged product weight fraction and chemical function data. \n\nThis dataset is associated with the following publication:\nIsaacs , K., M. Goldsmith, P. Egeghy , K. Phillips, R. Brooks, T. Hong, and J. Wambaugh. Characterization and prediction of chemical functions and weight fractions in consumer products.   Toxicology Reports. Elsevier B.V., Amsterdam,  NETHERLANDS, 3: 723-732, (2016).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:095"
+            "contactPoint": {
+                "fn": "Kristin Isaacs",
+                "hasEmail": "mailto:isaacs.kristin@epa.gov"
+            },
+            "describedBy": "https://pasteur.epa.gov/uploads/483/documents/read_me_metadata_MSDSFunction.docx",
+            "describedByType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+            "description": "Merged product weight fraction and chemical function data. \n\nThis dataset is associated with the following publication:\nIsaacs , K., M. Goldsmith, P. Egeghy , K. Phillips, R. Brooks, T. Hong, and J. Wambaugh. Characterization and prediction of chemical functions and weight fractions in consumer products.   Toxicology Reports. Elsevier B.V., Amsterdam,  NETHERLANDS, 3: 723-732, (2016).",
+            "distribution": [
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/483/MSDS_function_data.csv",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "MSDS_function_data.csv"
+                }
             ],
             "identifier": "A-mpgn-483",
             "keyword": [
@@ -46361,20 +46367,10 @@
                 "ExpoCast",
                 "machine learning"
             ],
-            "contactPoint": {
-                "fn": "Kristin Isaacs",
-                "hasEmail": "mailto:isaacs.kristin@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "MSDS_function_data.csv",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/483/MSDS_function_data.csv",
-                    "mediaType": "application/vnd.ms-excel"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2016-08-05",
-            "references": [
-                "https://doi.org/10.1016/j.toxrep.2016.08.011"
+            "programCode": [
+                "020:095"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -46385,20 +46381,30 @@
                     }
                 }
             },
-            "describedBy": "https://pasteur.epa.gov/uploads/483/documents/read_me_metadata_MSDSFunction.docx",
-            "describedByType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
+            "references": [
+                "https://doi.org/10.1016/j.toxrep.2016.08.011"
+            ],
+            "rights": null,
+            "title": "Chemical product and function dataset"
         },
         {
-            "title": "Chemicals and harmonized functions",
-            "description": "Chemicals and harmonized functions -  dataset of chemicals mapped to a harmonized chemical function category. \n\nThis dataset is associated with the following publication:\nIsaacs , K., M. Goldsmith, P. Egeghy , K. Phillips, R. Brooks, T. Hong, and J. Wambaugh. Characterization and prediction of chemical functions and weight fractions in consumer products.   Toxicology Reports. Elsevier B.V., Amsterdam,  NETHERLANDS, 3: 723-732, (2016).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:095"
+            "contactPoint": {
+                "fn": "Kristin Isaacs",
+                "hasEmail": "mailto:isaacs.kristin@epa.gov"
+            },
+            "describedBy": "https://pasteur.epa.gov/uploads/484/documents/read_me_metadata_Function.docx",
+            "describedByType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+            "description": "Chemicals and harmonized functions -  dataset of chemicals mapped to a harmonized chemical function category. \n\nThis dataset is associated with the following publication:\nIsaacs , K., M. Goldsmith, P. Egeghy , K. Phillips, R. Brooks, T. Hong, and J. Wambaugh. Characterization and prediction of chemical functions and weight fractions in consumer products.   Toxicology Reports. Elsevier B.V., Amsterdam,  NETHERLANDS, 3: 723-732, (2016).",
+            "distribution": [
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/484/function_data.csv",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "function_data.csv"
+                }
             ],
             "identifier": "A-mpgn-484",
             "keyword": [
@@ -46410,20 +46416,10 @@
                 "ExpoCast",
                 "machine learning"
             ],
-            "contactPoint": {
-                "fn": "Kristin Isaacs",
-                "hasEmail": "mailto:isaacs.kristin@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "function_data.csv",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/484/function_data.csv",
-                    "mediaType": "application/vnd.ms-excel"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2016-08-08",
-            "references": [
-                "https://doi.org/10.1016/j.toxrep.2016.08.011"
+            "programCode": [
+                "020:095"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -46434,20 +46430,30 @@
                     }
                 }
             },
-            "describedBy": "https://pasteur.epa.gov/uploads/484/documents/read_me_metadata_Function.docx",
-            "describedByType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
+            "references": [
+                "https://doi.org/10.1016/j.toxrep.2016.08.011"
+            ],
+            "rights": null,
+            "title": "Chemicals and harmonized functions"
         },
         {
-            "title": "Importance of predictor variables for models of chemical function",
-            "description": "Importance of random forest predictors for all classification models of chemical function. \n\nThis dataset is associated with the following publication:\nIsaacs , K., M. Goldsmith, P. Egeghy , K. Phillips, R. Brooks, T. Hong, and J. Wambaugh. Characterization and prediction of chemical functions and weight fractions in consumer products.   Toxicology Reports. Elsevier B.V., Amsterdam,  NETHERLANDS, 3: 723-732, (2016).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:095"
+            "contactPoint": {
+                "fn": "Kristin Isaacs",
+                "hasEmail": "mailto:isaacs.kristin@epa.gov"
+            },
+            "describedBy": "https://pasteur.epa.gov/uploads/486/documents/read_me_metadata.docx",
+            "describedByType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+            "description": "Importance of random forest predictors for all classification models of chemical function. \n\nThis dataset is associated with the following publication:\nIsaacs , K., M. Goldsmith, P. Egeghy , K. Phillips, R. Brooks, T. Hong, and J. Wambaugh. Characterization and prediction of chemical functions and weight fractions in consumer products.   Toxicology Reports. Elsevier B.V., Amsterdam,  NETHERLANDS, 3: 723-732, (2016).",
+            "distribution": [
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/486/ranksfunctionimp.csv",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "ranksfunctionimp.csv"
+                }
             ],
             "identifier": "A-mpgn-486",
             "keyword": [
@@ -46459,20 +46465,10 @@
                 "ExpoCast",
                 "machine learning"
             ],
-            "contactPoint": {
-                "fn": "Kristin Isaacs",
-                "hasEmail": "mailto:isaacs.kristin@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "ranksfunctionimp.csv",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/486/ranksfunctionimp.csv",
-                    "mediaType": "application/vnd.ms-excel"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2016-08-05",
-            "references": [
-                "https://doi.org/10.1016/j.toxrep.2016.08.011"
+            "programCode": [
+                "020:095"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -46483,43 +46479,43 @@
                     }
                 }
             },
-            "describedBy": "https://pasteur.epa.gov/uploads/486/documents/read_me_metadata.docx",
-            "describedByType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
+            "references": [
+                "https://doi.org/10.1016/j.toxrep.2016.08.011"
+            ],
+            "rights": null,
+            "title": "Importance of predictor variables for models of chemical function"
         },
         {
-            "title": "Examining the impacts of increased corn production on groundwater quality using a coupled modeling system",
-            "description": "This dataset was used to create graphics associated with manuscript:  Garcia et al., Examining the impacts of increased corn production on groundwater quality using a coupled modeling system, 2017, Science of the Total Environment. \n\nThis dataset is associated with the following publication:\nGarcia, V., E. Cooter, J. Crooks, B. Hinckley, M. Murphy, and X. Xing. Examining the impacts of increased corn production on groundwater quality using a coupled modeling system.   SCIENCE OF THE TOTAL ENVIRONMENT. Elsevier BV, AMSTERDAM,  NETHERLANDS, 586: 16-24, (2017).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:097"
-            ],
-            "identifier": "A-hdrn-492",
-            "keyword": [
-                "irrigated corn",
-                "nitrogen",
-                "groundwater",
-                "EPIC",
-                "nitrate in groundwater"
-            ],
             "contactPoint": {
                 "fn": "Valerie Cover",
                 "hasEmail": "mailto:garcia.val@epa.gov"
             },
+            "describedBy": "https://pasteur.epa.gov/uploads/492/documents/FertilizerScenarioComparison2_data_dic.docx",
+            "describedByType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+            "description": "This dataset was used to create graphics associated with manuscript:  Garcia et al., Examining the impacts of increased corn production on groundwater quality using a coupled modeling system, 2017, Science of the Total Environment. \n\nThis dataset is associated with the following publication:\nGarcia, V., E. Cooter, J. Crooks, B. Hinckley, M. Murphy, and X. Xing. Examining the impacts of increased corn production on groundwater quality using a coupled modeling system.   SCIENCE OF THE TOTAL ENVIRONMENT. Elsevier BV, AMSTERDAM,  NETHERLANDS, 586: 16-24, (2017).",
             "distribution": [
                 {
-                    "title": "FertilizerComparisonScenario2_SciHub.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/492/FertilizerComparisonScenario2_SciHub.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "FertilizerComparisonScenario2_SciHub.xlsx"
                 }
             ],
+            "identifier": "A-hdrn-492",
+            "keyword": [
+                "irrigated corn",
+                "nitrogen",
+                "groundwater",
+                "EPIC",
+                "nitrate in groundwater"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2017-02-07",
-            "references": [
-                "https://doi.org/10.1016/j.scitotenv.2017.02.009"
+            "programCode": [
+                "020:097"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -46530,41 +46526,39 @@
                     }
                 }
             },
-            "describedBy": "https://pasteur.epa.gov/uploads/492/documents/FertilizerScenarioComparison2_data_dic.docx",
-            "describedByType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
+            "references": [
+                "https://doi.org/10.1016/j.scitotenv.2017.02.009"
+            ],
+            "rights": null,
+            "title": "Examining the impacts of increased corn production on groundwater quality using a coupled modeling system"
         },
         {
-            "title": "Figs1,2,3a",
-            "description": "all data is in the netCDF format and zipped. after downloading this data, you need to unzip it first to create original netCDF formatted data. \n\nThis dataset is associated with the following publication:\nHe, J., T. Glotfelty, K. Yahya, K. Alapaty, and S. Yu. Does temperature nudging overwhelm aerosol radiative effects in regional integrated climate models?.   ATMOSPHERIC ENVIRONMENT. Elsevier Science Ltd, New York, NY, USA, 154: 42-52, (2017).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:094"
-            ],
-            "identifier": "A-2z37-499",
-            "keyword": [
-                "aerosol radiative forcing",
-                "nudging",
-                "aerosol effects",
-                "climate"
-            ],
             "contactPoint": {
                 "fn": "Kirankumar Alapaty",
                 "hasEmail": "mailto:alapaty.kiran@epa.gov"
             },
+            "description": "all data is in the netCDF format and zipped. after downloading this data, you need to unzip it first to create original netCDF formatted data. \n\nThis dataset is associated with the following publication:\nHe, J., T. Glotfelty, K. Yahya, K. Alapaty, and S. Yu. Does temperature nudging overwhelm aerosol radiative effects in regional integrated climate models?.   ATMOSPHERIC ENVIRONMENT. Elsevier Science Ltd, New York, NY, USA, 154: 42-52, (2017).",
             "distribution": [
                 {
-                    "title": "https://gaftp.epa.gov/EPADataCommons/ORD/NudgingPRE_AtmosEnvPaperData/",
-                    "accessURL": "https://gaftp.epa.gov/EPADataCommons/ORD/NudgingPRE_AtmosEnvPaperData/"
+                    "accessURL": "https://gaftp.epa.gov/EPADataCommons/ORD/NudgingPRE_AtmosEnvPaperData/",
+                    "title": "https://gaftp.epa.gov/EPADataCommons/ORD/NudgingPRE_AtmosEnvPaperData/"
                 }
             ],
+            "identifier": "A-2z37-499",
+            "keyword": [
+                "aerosol radiative forcing",
+                "nudging",
+                "aerosol effects",
+                "climate"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2017-01-19",
-            "references": [
-                "https://doi.org/10.1016/j.atmosenv.2017.01.040"
+            "programCode": [
+                "020:094"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -46574,41 +46568,41 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.atmosenv.2017.01.040"
+            ],
+            "rights": null,
+            "title": "Figs1,2,3a"
         },
         {
-            "title": "Wind tunnel evaluation of Hi-Vol TSP effectiveness data",
-            "description": "Wind tunnel evaluation of EPA's Hi-Vol TSP sampler for sampling effectiveness with regards to aerodynamic particle diameter (5 to 35 microns), wind speed (2, 8, 24 km/hr), orientation (0, 45, and 90 degrees relative to wind vector), and operational state (ON or OFF). A Coulter Counter analysis of the three Arizona Test Dust mixtures is presented. \n\nThis dataset is associated with the following publication:\nKrug, J., A. Dart, C. Witherspoon, J. Gilberry, Q. Malloy, S. Kaushik, and R. Vanderpool. Review of the of EPA's High-Volume Total Size Selective Performance  (Hi-Vol TSP) Sampler.   AEROSOL SCIENCE AND TECHNOLOGY. Taylor & Francis, Inc., Philadelphia, PA, USA, 0(0): 1-20, (2017).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:094"
-            ],
-            "identifier": "A-fxq2-572",
-            "keyword": [
-                "Hi-Vol TSP",
-                "wind tunnel",
-                "Size selective performance",
-                "total suspended particulate"
-            ],
             "contactPoint": {
                 "fn": "Jonathan Krug",
                 "hasEmail": "mailto:krug.jonathan@epa.gov"
             },
+            "description": "Wind tunnel evaluation of EPA's Hi-Vol TSP sampler for sampling effectiveness with regards to aerodynamic particle diameter (5 to 35 microns), wind speed (2, 8, 24 km/hr), orientation (0, 45, and 90 degrees relative to wind vector), and operational state (ON or OFF). A Coulter Counter analysis of the three Arizona Test Dust mixtures is presented. \n\nThis dataset is associated with the following publication:\nKrug, J., A. Dart, C. Witherspoon, J. Gilberry, Q. Malloy, S. Kaushik, and R. Vanderpool. Review of the of EPA's High-Volume Total Size Selective Performance  (Hi-Vol TSP) Sampler.   AEROSOL SCIENCE AND TECHNOLOGY. Taylor & Francis, Inc., Philadelphia, PA, USA, 0(0): 1-20, (2017).",
             "distribution": [
                 {
-                    "title": "HiVolData_ScienceHub.xlsx",
                     "downloadURL": "https://pasteur.epa.gov/uploads/572/HiVolData_ScienceHub.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "HiVolData_ScienceHub.xlsx"
                 }
             ],
+            "identifier": "A-fxq2-572",
+            "keyword": [
+                "Hi-Vol TSP",
+                "wind tunnel",
+                "Size selective performance",
+                "total suspended particulate"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2017-04-26",
-            "references": [
-                "https://doi.org/10.1080/02786826.2017.1316358"
+            "programCode": [
+                "020:094"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -46618,19 +46612,31 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1080/02786826.2017.1316358"
+            ],
+            "rights": null,
+            "title": "Wind tunnel evaluation of Hi-Vol TSP effectiveness data"
         },
         {
-            "title": "Development and Multi-laboratory Verification of U.S. EPA Method 543 for the Analysis of Drinking Water Contaminants by On-Line Solid Phase Extraction-LC/MS/MS",
-            "description": "A drinking water method for seven pesticides and pesticide degradates was developed that addresses the occurrence monitoring needs of the U.S. Environmental Protection Agency (EPA) for a future Unregulated Contaminant Monitoring Regulation (UCMR).  The method employs on-line solid phase extraction-liquid chromatography/tandem mass spectrometry (SPE-LC/MS/MS).  On-line SPE-LC/MS/MS has the potential to offer cost-effective, faster, more sensitive, and more rugged methods than the traditional off-line SPE approach due to complete automation of the SPE process, as well as seamless integration with the LC/MS/MS system.  Multi-laboratory data are presented that demonstrate method ruggedness and transferability.  The final method meets all of the EPA\u2019s UCMR survey requirements for sample collection and storage, precision, accuracy, and sensitivity. \n\nThis dataset is associated with the following publication:\nShoemaker , J. Development and Multi-laboratory Verification of US EPA Method 543 for the Analysis of Drinking Water Contaminants by Online Solid Phase Extraction-LC\u2013MS-MS.   Journal of Chromatographic Science. Preston Publications Incorporated, Niles, IL, USA, 54(9): 1532-1539, (2016).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:096"
+            "contactPoint": {
+                "fn": "Jody Shoemaker",
+                "hasEmail": "mailto:shoemaker.jody@epa.gov"
+            },
+            "describedBy": "https://pasteur.epa.gov/uploads/611/documents/Definitions_Method%20543%20data.docx",
+            "describedByType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+            "description": "A drinking water method for seven pesticides and pesticide degradates was developed that addresses the occurrence monitoring needs of the U.S. Environmental Protection Agency (EPA) for a future Unregulated Contaminant Monitoring Regulation (UCMR).  The method employs on-line solid phase extraction-liquid chromatography/tandem mass spectrometry (SPE-LC/MS/MS).  On-line SPE-LC/MS/MS has the potential to offer cost-effective, faster, more sensitive, and more rugged methods than the traditional off-line SPE approach due to complete automation of the SPE process, as well as seamless integration with the LC/MS/MS system.  Multi-laboratory data are presented that demonstrate method ruggedness and transferability.  The final method meets all of the EPA\u2019s UCMR survey requirements for sample collection and storage, precision, accuracy, and sensitivity. \n\nThis dataset is associated with the following publication:\nShoemaker , J. Development and Multi-laboratory Verification of US EPA Method 543 for the Analysis of Drinking Water Contaminants by Online Solid Phase Extraction-LC\u2013MS-MS.   Journal of Chromatographic Science. Preston Publications Incorporated, Niles, IL, USA, 54(9): 1532-1539, (2016).",
+            "distribution": [
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/611/ShoemakerJody_Method543_data.xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "ShoemakerJody_Method543_data.xlsx"
+                }
             ],
             "identifier": "A-f1vw-611",
             "keyword": [
@@ -46641,20 +46647,10 @@
                 "Method 543",
                 "contaminant candidate list"
             ],
-            "contactPoint": {
-                "fn": "Jody Shoemaker",
-                "hasEmail": "mailto:shoemaker.jody@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "ShoemakerJody_Method543_data.xlsx",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/611/ShoemakerJody_Method543_data.xlsx",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2017-05-11",
-            "references": [
-                "https://doi.org/10.1093/chromsci/bmw098"
+            "programCode": [
+                "020:096"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -46665,42 +46661,40 @@
                     }
                 }
             },
-            "describedBy": "https://pasteur.epa.gov/uploads/611/documents/Definitions_Method%20543%20data.docx",
-            "describedByType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
+            "references": [
+                "https://doi.org/10.1093/chromsci/bmw098"
+            ],
+            "rights": null,
+            "title": "Development and Multi-laboratory Verification of U.S. EPA Method 543 for the Analysis of Drinking Water Contaminants by On-Line Solid Phase Extraction-LC/MS/MS"
         },
         {
-            "title": "Predicted phototoxicities of carbon nano-material by quantum mechanical calculations",
-            "description": "The data involves a prediction of phototoxicities of nano-materials.  The prediction is based on the calculated triplet excited states of fullerenols and single-walled carbon nanotubes.  The model used is one previously published using actual phototoxicities of polynuclear aromatic hydrocarbons and their calculated triplet excited states. \n\nThis dataset is associated with the following publication:\nBetowski, D. Predicted phototoxicities of carbon nano-material by quantum mechanical calculations.   Journal of Molecular Graphics and Modelling. Elsevier B.V., Amsterdam,  NETHERLANDS, 75: 102-105, (2017).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:000"
-            ],
-            "identifier": "A-m90n-180",
-            "keyword": [
-                "phototoxicity",
-                "fullerenols",
-                "single-walled carbon nanotubes",
-                "ab initio calculations."
-            ],
             "contactPoint": {
                 "fn": "Leon Betowski",
                 "hasEmail": "mailto:betowski.don@epa.gov"
             },
+            "description": "The data involves a prediction of phototoxicities of nano-materials.  The prediction is based on the calculated triplet excited states of fullerenols and single-walled carbon nanotubes.  The model used is one previously published using actual phototoxicities of polynuclear aromatic hydrocarbons and their calculated triplet excited states. \n\nThis dataset is associated with the following publication:\nBetowski, D. Predicted phototoxicities of carbon nano-material by quantum mechanical calculations.   Journal of Molecular Graphics and Modelling. Elsevier B.V., Amsterdam,  NETHERLANDS, 75: 102-105, (2017).",
             "distribution": [
                 {
-                    "title": "Predicted phototoxicities of carbon nano material.pdf",
                     "downloadURL": "https://pasteur.epa.gov/uploads/180/Predicted%20phototoxicities%20of%20carbon%20nano%20material.pdf",
-                    "mediaType": "application/pdf"
+                    "mediaType": "application/pdf",
+                    "title": "Predicted phototoxicities of carbon nano material.pdf"
                 }
             ],
+            "identifier": "A-m90n-180",
+            "keyword": [
+                "phototoxicity",
+                "fullerenols",
+                "single-walled carbon nanotubes",
+                "ab initio calculations."
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2016-08-09",
-            "references": [
-                "https://doi.org/10.1016/j.jmgm.2017.03.017"
+            "programCode": [
+                "020:000"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -46710,92 +46704,94 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.jmgm.2017.03.017"
+            ],
+            "rights": null,
+            "title": "Predicted phototoxicities of carbon nano-material by quantum mechanical calculations"
         },
         {
-            "title": "EPA Contribution to Manuscript \"Evaluation and Error Apportionment of an Ensemble of Atmospheric Chemistry Transport Modelling Systems: Multi-variable Temporal and Spatial Breakdown\"",
-            "description": "This dataset contains the data contributed by EPA/ORD/NERL/CED researchers to the manuscript \"Evaluation and Error Apportionment of an Ensemble of Atmospheric Chemistry Transport Modelling Systems: Multi-variable Temporal and Spatial Breakdown \" led by Dr. Efisio Solazzo of the European Commission's Joint Research Center. \n\nThis dataset is associated with the following publication:\nSolazzo, E., R. Bianconi, C. Hogrefe, G. Curci, P. Tuccella, U. Alyuz, A. Balzarini, R. Baro, R. Bellasio, J. Bieser, J. Brandt, J. Christensen, A. Colette, X. Francis, A. Fraser, M. Garcia Vivanco, P. Jim\u00e9nez-Guerrero, U. Im, A. Manders, U. Nopmongcol, N. Kitwiroon, G. Pirovano, L. Pozzoli, M. Prank, R. Sokhi, A. Unal, G. Yarwood, and S. Galmarini. Evaluation and error apportionment of an ensemble of atmospheric chemistry transport modeling systems: multivariable temporal and spatial breakdown.   Atmospheric Chemistry and Physics. Copernicus Publications, Katlenburg-Lindau,  GERMANY, 17: 3001-3054, (2017).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:094"
-            ],
-            "identifier": "A-z09b-493",
-            "keyword": [
-                "AQMEII",
-                "model evaluation",
-                "scale analysis",
-                "model intercomparision",
-                "ozone persistence"
-            ],
             "contactPoint": {
                 "fn": "Christian Hogrefe",
                 "hasEmail": "mailto:hogrefe.christian@epa.gov"
             },
+            "describedBy": "https://pasteur.epa.gov/uploads/493/documents/DataDictionary.zip",
+            "describedByType": "application/zip",
+            "description": "This dataset contains the data contributed by EPA/ORD/NERL/CED researchers to the manuscript \"Evaluation and Error Apportionment of an Ensemble of Atmospheric Chemistry Transport Modelling Systems: Multi-variable Temporal and Spatial Breakdown \" led by Dr. Efisio Solazzo of the European Commission's Joint Research Center. \n\nThis dataset is associated with the following publication:\nSolazzo, E., R. Bianconi, C. Hogrefe, G. Curci, P. Tuccella, U. Alyuz, A. Balzarini, R. Baro, R. Bellasio, J. Bieser, J. Brandt, J. Christensen, A. Colette, X. Francis, A. Fraser, M. Garcia Vivanco, P. Jim\u00e9nez-Guerrero, U. Im, A. Manders, U. Nopmongcol, N. Kitwiroon, G. Pirovano, L. Pozzoli, M. Prank, R. Sokhi, A. Unal, G. Yarwood, and S. Galmarini. Evaluation and error apportionment of an ensemble of atmospheric chemistry transport modeling systems: multivariable temporal and spatial breakdown.   Atmospheric Chemistry and Physics. Copernicus Publications, Katlenburg-Lindau,  GERMANY, 17: 3001-3054, (2017).",
             "distribution": [
                 {
-                    "title": "data_2010_0236_001_CO.zip",
                     "downloadURL": "https://pasteur.epa.gov/uploads/493/data_2010_0236_001_CO.zip",
-                    "mediaType": "application/x-zip-compressed"
+                    "mediaType": "application/x-zip-compressed",
+                    "title": "data_2010_0236_001_CO.zip"
                 },
                 {
-                    "title": "data_2010_0236_001_NO2.zip",
                     "downloadURL": "https://pasteur.epa.gov/uploads/493/data_2010_0236_001_NO2.zip",
-                    "mediaType": "application/x-zip-compressed"
+                    "mediaType": "application/x-zip-compressed",
+                    "title": "data_2010_0236_001_NO2.zip"
                 },
                 {
-                    "title": "data_2010_0236_001_O3.zip",
                     "downloadURL": "https://pasteur.epa.gov/uploads/493/data_2010_0236_001_O3.zip",
-                    "mediaType": "application/x-zip-compressed"
+                    "mediaType": "application/x-zip-compressed",
+                    "title": "data_2010_0236_001_O3.zip"
                 },
                 {
-                    "title": "data_2010_0236_001_SO2.zip",
                     "downloadURL": "https://pasteur.epa.gov/uploads/493/data_2010_0236_001_SO2.zip",
-                    "mediaType": "application/x-zip-compressed"
+                    "mediaType": "application/x-zip-compressed",
+                    "title": "data_2010_0236_001_SO2.zip"
                 },
                 {
-                    "title": "data_2010_0236_002_PM2_5.zip",
                     "downloadURL": "https://pasteur.epa.gov/uploads/493/data_2010_0236_002_PM2_5.zip",
-                    "mediaType": "application/x-zip-compressed"
+                    "mediaType": "application/x-zip-compressed",
+                    "title": "data_2010_0236_002_PM2_5.zip"
                 },
                 {
-                    "title": "data_2010_0236_002_PM10.zip",
                     "downloadURL": "https://pasteur.epa.gov/uploads/493/data_2010_0236_002_PM10.zip",
-                    "mediaType": "application/x-zip-compressed"
+                    "mediaType": "application/x-zip-compressed",
+                    "title": "data_2010_0236_002_PM10.zip"
                 },
                 {
-                    "title": "data_2010_0236_004_O3.zip",
                     "downloadURL": "https://pasteur.epa.gov/uploads/493/data_2010_0236_004_O3.zip",
-                    "mediaType": "application/x-zip-compressed"
+                    "mediaType": "application/x-zip-compressed",
+                    "title": "data_2010_0236_004_O3.zip"
                 },
                 {
-                    "title": "data_2010_0236_004_TEMP.zip",
                     "downloadURL": "https://pasteur.epa.gov/uploads/493/data_2010_0236_004_TEMP.zip",
-                    "mediaType": "application/x-zip-compressed"
+                    "mediaType": "application/x-zip-compressed",
+                    "title": "data_2010_0236_004_TEMP.zip"
                 },
                 {
-                    "title": "data_2010_0236_004_WS.zip",
                     "downloadURL": "https://pasteur.epa.gov/uploads/493/data_2010_0236_004_WS.zip",
-                    "mediaType": "application/x-zip-compressed"
+                    "mediaType": "application/x-zip-compressed",
+                    "title": "data_2010_0236_004_WS.zip"
                 },
                 {
-                    "title": "data_2010_0236_005_TEMP.zip",
                     "downloadURL": "https://pasteur.epa.gov/uploads/493/data_2010_0236_005_TEMP.zip",
-                    "mediaType": "application/x-zip-compressed"
+                    "mediaType": "application/x-zip-compressed",
+                    "title": "data_2010_0236_005_TEMP.zip"
                 },
                 {
-                    "title": "data_2010_0236_005_WS.zip",
                     "downloadURL": "https://pasteur.epa.gov/uploads/493/data_2010_0236_005_WS.zip",
-                    "mediaType": "application/x-zip-compressed"
+                    "mediaType": "application/x-zip-compressed",
+                    "title": "data_2010_0236_005_WS.zip"
                 }
             ],
+            "identifier": "A-z09b-493",
+            "keyword": [
+                "AQMEII",
+                "model evaluation",
+                "scale analysis",
+                "model intercomparision",
+                "ozone persistence"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2015-12-31",
-            "references": [
-                "https://doi.org/10.5194/acp-17-3001-2017"
+            "programCode": [
+                "020:094"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -46806,42 +46802,42 @@
                     }
                 }
             },
-            "describedBy": "https://pasteur.epa.gov/uploads/493/documents/DataDictionary.zip",
-            "describedByType": "application/zip"
+            "references": [
+                "https://doi.org/10.5194/acp-17-3001-2017"
+            ],
+            "rights": null,
+            "title": "EPA Contribution to Manuscript \"Evaluation and Error Apportionment of an Ensemble of Atmospheric Chemistry Transport Modelling Systems: Multi-variable Temporal and Spatial Breakdown\""
         },
         {
-            "title": "Persistence of Initial Conditions in Continental Scale Air Quality Simulations",
-            "description": "This dataset contains the data used in Figures 1 \u2013 6 and Table 2 of the technical note \"Persistence of Initial Conditions in Continental Scale Air Quality Simulations\". \n\nThis dataset is associated with the following publication:\nHogrefe, C., S. Roselle, and J. Bash. Persistence of initial conditions in continental scale air quality simulations.   ATMOSPHERIC ENVIRONMENT. Elsevier Science Ltd, New York, NY, USA, 160: 36-45, (2017).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:094"
-            ],
-            "identifier": "A-4mwd-521",
-            "keyword": [
-                "Initial conditions",
-                "spin-up period",
-                "soil concentrations",
-                "inert tracers"
-            ],
             "contactPoint": {
                 "fn": "Christian Hogrefe",
                 "hasEmail": "mailto:hogrefe.christian@epa.gov"
             },
+            "describedBy": "https://pasteur.epa.gov/uploads/521/documents/DataDictionary_HogrefeEtAl_A-4mwd.docx",
+            "describedByType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+            "description": "This dataset contains the data used in Figures 1 \u2013 6 and Table 2 of the technical note \"Persistence of Initial Conditions in Continental Scale Air Quality Simulations\". \n\nThis dataset is associated with the following publication:\nHogrefe, C., S. Roselle, and J. Bash. Persistence of initial conditions in continental scale air quality simulations.   ATMOSPHERIC ENVIRONMENT. Elsevier Science Ltd, New York, NY, USA, 160: 36-45, (2017).",
             "distribution": [
                 {
-                    "title": "data_HogrefeChristian_A-4mwd.zip",
                     "downloadURL": "https://pasteur.epa.gov/uploads/521/data_HogrefeChristian_A-4mwd.zip",
-                    "mediaType": "application/x-zip-compressed"
+                    "mediaType": "application/x-zip-compressed",
+                    "title": "data_HogrefeChristian_A-4mwd.zip"
                 }
             ],
+            "identifier": "A-4mwd-521",
+            "keyword": [
+                "Initial conditions",
+                "spin-up period",
+                "soil concentrations",
+                "inert tracers"
+            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2016-10-31",
-            "references": [
-                "https://doi.org/10.1016/j.atmosenv.2017.04.009"
+            "programCode": [
+                "020:094"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -46852,20 +46848,28 @@
                     }
                 }
             },
-            "describedBy": "https://pasteur.epa.gov/uploads/521/documents/DataDictionary_HogrefeEtAl_A-4mwd.docx",
-            "describedByType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
+            "references": [
+                "https://doi.org/10.1016/j.atmosenv.2017.04.009"
+            ],
+            "rights": null,
+            "title": "Persistence of Initial Conditions in Continental Scale Air Quality Simulations"
         },
         {
-            "title": "Simulated Pathogen Concentrations in Locally-Collected Greywater and Wastewater",
-            "description": "This dataset contains simulated pathogen concentrations in locally-collected greywater and wastewater.  Each .zip file includes 21 .csv files, each containing 10,000 years of simulated daily pathogen concentrations in the water type designated by the title (Combined Greywater, Laundry Greywater, Shower Greywater, Sink Greywater, or Onsite Wastewater).  Each .csv file corresponds to one pathogen (Ad Adenovirus, Ca Campylobacter, Cr Cryptosporidium, Gi Giardia, No Norovirus, Ro Rotavirus, or Sa Salmonella) for one population size (5-, 100-, or 1000-person).  For example, ConcAdCombGW100.csv contains concentrations (Conc) of Adenovirus (Ad) in combined greywater (CombGW) for a 100-person population size (100).  Data is structured as 365 rows (days) by 10,000 columns (years), with the first row and column containing year and day indices, respectively.  Units are # pathogens/L water. \n\nThis dataset is associated with the following publication:\nJahne, M., M. Schoen, J. Garland, and N. Ashbolt. Simulation of enteric pathogen concentrations in locally-collected greywater and wastewater for microbial risk assessments.   Microbial Risk Analysis. Elsevier B.V., Amsterdam,  NETHERLANDS, 5: 44-52, (2017).",
             "accessLevel": "public",
-            "rights": null,
-            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "bureauCode": [
                 "020:00"
             ],
-            "programCode": [
-                "020:096"
+            "contactPoint": {
+                "fn": "Michael Jahne",
+                "hasEmail": "mailto:jahne.michael@epa.gov"
+            },
+            "description": "This dataset contains simulated pathogen concentrations in locally-collected greywater and wastewater.  Each .zip file includes 21 .csv files, each containing 10,000 years of simulated daily pathogen concentrations in the water type designated by the title (Combined Greywater, Laundry Greywater, Shower Greywater, Sink Greywater, or Onsite Wastewater).  Each .csv file corresponds to one pathogen (Ad Adenovirus, Ca Campylobacter, Cr Cryptosporidium, Gi Giardia, No Norovirus, Ro Rotavirus, or Sa Salmonella) for one population size (5-, 100-, or 1000-person).  For example, ConcAdCombGW100.csv contains concentrations (Conc) of Adenovirus (Ad) in combined greywater (CombGW) for a 100-person population size (100).  Data is structured as 365 rows (days) by 10,000 columns (years), with the first row and column containing year and day indices, respectively.  Units are # pathogens/L water. \n\nThis dataset is associated with the following publication:\nJahne, M., M. Schoen, J. Garland, and N. Ashbolt. Simulation of enteric pathogen concentrations in locally-collected greywater and wastewater for microbial risk assessments.   Microbial Risk Analysis. Elsevier B.V., Amsterdam,  NETHERLANDS, 5: 44-52, (2017).",
+            "distribution": [
+                {
+                    "downloadURL": "https://pasteur.epa.gov/uploads/196/Simulated%20Pathogen%20Concentrations%20in%20Locally-Collected%20Greywater%20and%20Wastewater.zip",
+                    "mediaType": "application/x-zip-compressed",
+                    "title": "Simulated Pathogen Concentrations in Locally-Collected Greywater and Wastewater.zip"
+                }
             ],
             "identifier": "A-f1vv-196",
             "keyword": [
@@ -46881,20 +46885,10 @@
                 "QMRA",
                 "pathogens"
             ],
-            "contactPoint": {
-                "fn": "Michael Jahne",
-                "hasEmail": "mailto:jahne.michael@epa.gov"
-            },
-            "distribution": [
-                {
-                    "title": "Simulated Pathogen Concentrations in Locally-Collected Greywater and Wastewater.zip",
-                    "downloadURL": "https://pasteur.epa.gov/uploads/196/Simulated%20Pathogen%20Concentrations%20in%20Locally-Collected%20Greywater%20and%20Wastewater.zip",
-                    "mediaType": "application/x-zip-compressed"
-                }
-            ],
+            "license": "https://pasteur.epa.gov/license/sciencehub-license.html",
             "modified": "2016-08-17",
-            "references": [
-                "https://doi.org/10.1016/j.mran.2016.11.001"
+            "programCode": [
+                "020:096"
             ],
             "publisher": {
                 "name": "U.S. EPA Office of Research and Development (ORD)",
@@ -46904,34 +46898,34 @@
                         "name": "U.S. Government"
                     }
                 }
-            }
+            },
+            "references": [
+                "https://doi.org/10.1016/j.mran.2016.11.001"
+            ],
+            "rights": null,
+            "title": "Simulated Pathogen Concentrations in Locally-Collected Greywater and Wastewater"
         },
         {
-            "title": "None",
```

