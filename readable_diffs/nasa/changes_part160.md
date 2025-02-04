# Change History for nasa.json (Part 160)

### Changes from 31606f9 to dd2190f (Part 149/162)
**Author:** Automated

**Date:** 2025-02-01 15:02:16+00:00

**Message:** Updated data: Sat Feb  1 15:02:16 UTC 2025

```diff
-                    "downloadURL": "https://tes.jpl.nasa.gov/tropess/",
-                    "description": "TROPESS Project Home Page.",
                     "@type": "dcat:Distribution",
+                    "description": "TROPESS Project Home Page.",
+                    "downloadURL": "https://tes.jpl.nasa.gov/tropess/",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 }
             ],
+            "graphic-preview-description": "TROPESS AIRS-Aqua CO (Reanalysis Stream, Summary Product) at 383 hPa on 01 April 2021.",
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TROPESS/images/TRPSYL2COAIRSORS_Sample.png",
+            "identifier": "C2756757848-GES_DISC",
+            "issued": "2023-10-23",
+            "keyword": [
+                "atmosphere",
+                "atmospheric chemistry",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/WWKSE7JT6HNW",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2023-10-23",
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
+            "series-name": "TRPSYL2COAIRSORS",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2002-09-01T00:00:00Z/2023-11-06T00:00:00Z",
             "theme": [
                 "TROPESS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "TROPESS AIRS-Aqua L2 Carbon Monoxide for Reanalysis Stream, Summary Product V1 (TRPSYL2COAIRSORS) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-NAVCAM-2-ESC1-MTP013-V1.0",
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
+            "description": "This dataset contains ROSETTA NAVCAM RAW DATA of the Escort Phase from 10th Feb 2015 to 10th Mar 2015 when at the vicinity of target 67P/CG.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-navcam-2-esc1-mtp013-v1.0_wfdz-xvrq",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-NAVCAM-2-ESC1-MTP013-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-navcam-2-esc1-mtp013-v1.0_wfdz-xvrq",
-            "description": "This dataset contains ROSETTA NAVCAM RAW DATA of the Escort Phase from 10th Feb 2015 to 10th Mar 2015 when at the vicinity of target 67P/CG.",
-            "title": "ROSETTA-ORBITER 67P NAVCAM 2 COMET ESCORT 1 MTP013 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P NAVCAM 2 COMET ESCORT 1 MTP013 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1220567798-USGS_LTA.html",
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
                 "fn": "LONG TERM ARCHIVE",
                 "hasEmail": "mailto:lta@usgs.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "DOI/USGS/EROS"
-            },
-            "identifier": "C1220567798-USGS_LTA",
             "description": "Global Land Survey 2005 images were acquired from 2003 - 2008 by Landsat 7 ETM+, Landsat 5 Thematic Mapper (TM) and EO-1 ALI.\n\nThe U.S. Geological Survey (USGS) and the National Aeronautics and Space Administration (NASA) collaborated on the creation of the global land datasets using Landsat data from 1972 through 2008. Each of these global datasets was created from the primary Landsat sensor in use at the time: the Multispectral Scanner (MSS) in the 1970s, the Thematic Mapper (TM) in 1990, the Enhanced Thematic Mapper Plus (ETM+) in 2000, and a combination of TM and ETM+, as well as EO-1 ALI data, in 2005.",
-            "title": "Global Land Survey 2005",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://earthexplorer.usgs.gov",
-                    "description": "\n         Query and order satellite images, aerial photographs, and cartographic products through the U.S. Geological Survey. Log in as a guest or as a registered user. Registered users have access to more features than guests do. If you plan on using EarthExplorer frequently, you may wish to register. Please note that this site uses Session Cookies and Java applets.\n         \n         Typically, all data available from USGS/EROS are downloadable at no cost  to the user.  There are some cases when a service fee is required to  convert the analog film record to a digital file. This non-refundable fee  is $30 per scene/frame.\n      ",
                     "@type": "dcat:Distribution",
+                    "description": "\n         Query and order satellite images, aerial photographs, and cartographic products through the U.S. Geological Survey. Log in as a guest or as a registered user. Registered users have access to more features than guests do. If you plan on using EarthExplorer frequently, you may wish to register. Please note that this site uses Session Cookies and Java applets.\n         \n         Typically, all data available from USGS/EROS are downloadable at no cost  to the user.  There are some cases when a service fee is required to  convert the analog film record to a digital file. This non-refundable fee  is $30 per scene/frame.\n      ",
+                    "downloadURL": "http://earthexplorer.usgs.gov",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://landsat.usgs.gov/band_designations_landsat_satellites.php",
-                    "description": "\n         Band designations for the Landsat satellites\n      ",
                     "@type": "dcat:Distribution",
+                    "description": "\n         Band designations for the Landsat satellites\n      ",
+                    "downloadURL": "http://landsat.usgs.gov/band_designations_landsat_satellites.php",
+                    "mediaType": "text/html",
                     "title": "Access to this dataset's extended metadata"
                 }
             ],
+            "identifier": "C1220567798-USGS_LTA",
+            "issued": "2019-09-20",
+            "keyword": [
+                "earth science",
+                "topography",
+                "land surface",
+                "surface radiative properties"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1220567798-USGS_LTA.html",
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
+            "title": "Global Land Survey 2005"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-4-ESC3-67PCHURYUMOV-M18-V2.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This CODMAC level 4 data set contains radiometric calibrated and geometric distortion corrected (resampled) image data in W/m^2/sr/nm, acquired by the OSIRIS Narrow Angle Camera on the Rosetta spacecraft during the COMET ESCORT 3 mission phase, covering the period from 2015-06-30T23:25:00.000 to 2015-07-28T23:24:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V2.0 supersedes previous deliveries of the same dataset with the following changes since the last version: Lien corrected dataset after October 2018 PSA/PDS external peer review. Updated documentation and ancillary files, added document on bandpass filter. Updated SCIENCE_USER_GUIDE_V03.PDF to include one section about FAQ and one section about image data quality. Added shutter backtravel and readout issues to image quality map. Updated DATA_QUALITY_ID keyword in image header. Improved handling of images with missing packets.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-4-esc3-67pchuryumov-m18-v2.0_wfga-9s4p",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "67p/churyumov-gerasimenko 1 (1969 r1)",
                 "pluto",
@@ -1570366,422 +1570368,401 @@
                 "zeta cas",
                 "vega"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-4-ESC3-67PCHURYUMOV-M18-V2.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-4-esc3-67pchuryumov-m18-v2.0_wfga-9s4p",
-            "description": "This CODMAC level 4 data set contains radiometric calibrated and geometric distortion corrected (resampled) image data in W/m^2/sr/nm, acquired by the OSIRIS Narrow Angle Camera on the Rosetta spacecraft during the COMET ESCORT 3 mission phase, covering the period from 2015-06-30T23:25:00.000 to 2015-07-28T23:24:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V2.0 supersedes previous deliveries of the same dataset with the following changes since the last version: Lien corrected dataset after October 2018 PSA/PDS external peer review. Updated documentation and ancillary files, added document on bandpass filter. Updated SCIENCE_USER_GUIDE_V03.PDF to include one section about FAQ and one section about image data quality. Added shutter backtravel and readout issues to image quality map. Updated DATA_QUALITY_ID keyword in image header. Improved handling of images with missing packets.",
-            "title": "ROSETTA-ORBITER 67P OSINAC 4 ESC3-MTP018 RDR V2.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P OSINAC 4 ESC3-MTP018 RDR V2.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/719",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Privette, J.L., M.M. Mukelabai, and C. Pietras. 2004. SAFARI 2000 AOT and Column Water Vapor, Kalahari Transect, Wet Season 2000. ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/719",
-            "issued": "2023-10-18",
-            "temporal": "2000-03-03T00:00:00Z/2000-03-18T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-10-24",
-            "keyword": [
-                "atmosphere",
-                "earth science",
-                "atmospheric water vapor",
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
-            "identifier": "C2788397022-ORNL_CLOUD",
             "description": "The data presented here include the aerosol optical thickness (AOT) and column water vapor measurements taken at sites along the Kalahari Transect using a Microtops sunphotometer. Data were collected every 30 minutes at 4 sites that were visited during the SAFARI 2000 Kalahari Wet Season Campaign between March 3, 2000, and March 18, 2000. AOT values are provided at 340-, 440-, 675-, 870-, and 936-nm wavelengths. An estimate of the Angstrom Coefficient is also provided to allow the estimation of AOT at other wavelengths. The purpose of this data collection was primarily for documentation of the conditions at each site and to aid in the correction of remote sensing data, for validation of Earth Observation System (EOS) products such as MODIS and MISR aerosol products, and for modeling of canopy productivity.",
-            "graphic-preview-description": "Browse Image",
-            "title": "SAFARI 2000 AOT and Column Water Vapor, Kalahari Transect, Wet Season 2000",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/safari_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F719",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F719",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/safari2k/atmospheric/kalahari_aot_h2o_vapor/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/safari2k/atmospheric/kalahari_aot_h2o_vapor/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/S2K/guides/kalahari_aot_h2o_vapor.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/S2K/guides/kalahari_aot_h2o_vapor.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/719",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/719",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/safari2k/atmospheric/kalahari_aot_h2o_vapor/comp/kalahari_aot_h2o_vapor_readme.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/safari2k/atmospheric/kalahari_aot_h2o_vapor/comp/kalahari_aot_h2o_vapor_readme.pdf",
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
+            "identifier": "C2788397022-ORNL_CLOUD",
+            "issued": "2023-10-18",
+            "keyword": [
+                "atmosphere",
+                "earth science",
+                "atmospheric water vapor",
+                "aerosols"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/719",
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
             "spatial": "21.72 -24.17 25.5 -18.65",
+            "temporal": "2000-03-03T00:00:00Z/2000-03-18T23:59:59Z",
             "theme": [
                 "SAFARI 2000",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "SAFARI 2000 AOT and Column Water Vapor, Kalahari Transect, Wet Season 2000"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://c3.nasa.gov/dashlink/resources/832/",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2013-09-06",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
-            "keyword": [
-                "nasa",
-                "dashlink",
-                "ames"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "JENNIFER HEEG",
                 "hasEmail": "mailto:jennifer.heeg@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Dashlink"
-            },
-            "identifier": "DASHLINK_832",
             "description": "Images for the website main pages and all configurations.\r\nThe upload and access points for the other images are:\r\n<center><h1><font color=\"#DF01A5><a href=\"https://c3.nasa.gov/dashlink/resources/836/\" > Website Template </a> </font></h1> </center>\r\n\r\n<center><h1><font color=\"#DF01A5><a href=\"https://c3.nasa.gov/dashlink/resources/837/\" > \r\nRSW images </a> </font></h1> </center>\r\n\r\n<center><h1><font color=\"#DF01A5><a href=\"https://c3.nasa.gov/dashlink/resources/838/\" > BSCW Images </a> </font></h1> </center>\r\n\r\n<center><h1><font color=\"#DF01A5><a href=\"https://c3.nasa.gov/dashlink/resources/839/\" > HIRENASD Images </a> </font></h1> </center>",
-            "title": "Images",
-            "programCode": [
-                "026:029"
-            ],
             "distribution": [
                 {
-                    "mediaType": "image/x-png",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Computational_Teams_button_small.png",
-                    "description": "Computational_Teams_button_small.png",
                     "@type": "dcat:Distribution",
+                    "description": "Computational_Teams_button_small.png",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Computational_Teams_button_small.png",
+                    "mediaType": "image/x-png",
                     "title": "Computational_Teams_button_small.png"
                 },
                 {
-                    "mediaType": "image/x-png",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Organizing_Committee_button_small.png",
-                    "description": "Organizing_Committee_button_small.png",
                     "@type": "dcat:Distribution",
+                    "description": "Organizing_Committee_button_small.png",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Organizing_Committee_button_small.png",
+                    "mediaType": "image/x-png",
                     "title": "Organizing_Committee_button_small.png"
                 },
                 {
-                    "mediaType": "image/x-png",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/RSW_inTDT.png",
-                    "description": "RSW_inTDT.png",
                     "@type": "dcat:Distribution",
+                    "description": "RSW_inTDT.png",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/RSW_inTDT.png",
+                    "mediaType": "image/x-png",
                     "title": "RSW_inTDT.png"
                 },
                 {
-                    "mediaType": "image/pjpeg",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/BSCW_inTDT.jpg",
-                    "description": "BSCW_inTDT.jpg",
                     "@type": "dcat:Distribution",
+                    "description": "BSCW_inTDT.jpg",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/BSCW_inTDT.jpg",
+                    "mediaType": "image/pjpeg",
                     "title": "BSCW_inTDT.jpg"
                 },
                 {
-                    "mediaType": "image/pjpeg",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/HIRENASD_inETW.jpg",
-                    "description": "HIRENASD_inETW.jpg",
                     "@type": "dcat:Distribution",
+                    "description": "HIRENASD_inETW.jpg",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/HIRENASD_inETW.jpg",
+                    "mediaType": "image/pjpeg",
                     "title": "HIRENASD_inETW.jpg"
                 },
                 {
-                    "mediaType": "image/pjpeg",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Montage_Slide_2.jpg",
-                    "description": "Montage_Slide.jpg",
                     "@type": "dcat:Distribution",
+                    "description": "Montage_Slide.jpg",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Montage_Slide_2.jpg",
+                    "mediaType": "image/pjpeg",
                     "title": "Montage_Slide.jpg"
                 },
                 {
-                    "mediaType": "image/pjpeg",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/AeroelastPredictWkshp_Hi.jpg",
-                    "description": "AeroelastPredictWkshp_Hi.jpg",
                     "@type": "dcat:Distribution",
+                    "description": "AeroelastPredictWkshp_Hi.jpg",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/AeroelastPredictWkshp_Hi.jpg",
+                    "mediaType": "image/pjpeg",
                     "title": "AeroelastPredictWkshp_Hi.jpg"
                 },
                 {
-                    "mediaType": "image/pjpeg",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/AePWTimeline.jpg",
-                    "description": "AePWTimeline.jpg",
                     "@type": "dcat:Distribution",
+                    "description": "AePWTimeline.jpg",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/AePWTimeline.jpg",
+                    "mediaType": "image/pjpeg",
                     "title": "AePWTimeline.jpg"
                 },
                 {
-                    "mediaType": "image/x-png",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Agenda_Sat.png",
-                    "description": "Agenda_Sat.png",
                     "@type": "dcat:Distribution",
+                    "description": "Agenda_Sat.png",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Agenda_Sat.png",
+                    "mediaType": "image/x-png",
                     "title": "Agenda_Sat.png"
                 },
                 {
-                    "mediaType": "image/x-png",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Agenda_Sun.png",
-                    "description": "Agenda_Sun.png",
                     "@type": "dcat:Distribution",
+                    "description": "Agenda_Sun.png",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Agenda_Sun.png",
+                    "mediaType": "image/x-png",
                     "title": "Agenda_Sun.png"
                 },
                 {
-                    "mediaType": "image/x-png",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/BSCW_planform_cartoon.png",
-                    "description": "BSCW_planform_cartoon.png",
                     "@type": "dcat:Distribution",
+                    "description": "BSCW_planform_cartoon.png",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/BSCW_planform_cartoon.png",
+                    "mediaType": "image/x-png",
                     "title": "BSCW_planform_cartoon.png"
                 },
                 {
-                    "mediaType": "image/pjpeg",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/HIRENASD_FEM.jpg",
-                    "description": "HIRENASD_FEM.jpg",
                     "@type": "dcat:Distribution",
+                    "description": "HIRENASD_FEM.jpg",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/HIRENASD_FEM.jpg",
+                    "mediaType": "image/pjpeg",
                     "title": "HIRENASD_FEM.jpg"
                 },
                 {
-                    "mediaType": "image/pjpeg",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Hirenasd_model_jh_2.jpg",
-                    "description": "Hirenasd_model_jh_2.jpg",
                     "@type": "dcat:Distribution",
+                    "description": "Hirenasd_model_jh_2.jpg",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Hirenasd_model_jh_2.jpg",
+                    "mediaType": "image/pjpeg",
                     "title": "Hirenasd_model_jh_2.jpg"
                 },
                 {
-                    "mediaType": "image/x-png",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/RSW_onsplitterplate_cartoon.png",
-                    "description": "RSW_onsplitterplate_cartoon.png",
                     "@type": "dcat:Distribution",
+                    "description": "RSW_onsplitterplate_cartoon.png",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/RSW_onsplitterplate_cartoon.png",
+                    "mediaType": "image/x-png",
                     "title": "RSW_onsplitterplate_cartoon.png"
                 },
                 {
-                    "mediaType": "image/x-png",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Submit_data_button_small.png",
-                    "description": "Submit_data_button_small.png",
                     "@type": "dcat:Distribution",
+                    "description": "Submit_data_button_small.png",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Submit_data_button_small.png",
+                    "mediaType": "image/x-png",
                     "title": "Submit_data_button_small.png"
                 },
                 {
-                    "mediaType": "image/x-png",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/templatemo_content_bottom.png",
-                    "description": "templatemo_content_bottom.png",
                     "@type": "dcat:Distribution",
+                    "description": "templatemo_content_bottom.png",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/templatemo_content_bottom.png",
+                    "mediaType": "image/x-png",
                     "title": "templatemo_content_bottom.png"
                 },
                 {
-                    "mediaType": "image/x-png",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Join_AePW_MailingList_button_small.png",
-                    "description": "Join_AePW_MailingList_button_small.png",
                     "@type": "dcat:Distribution",
+                    "description": "Join_AePW_MailingList_button_small.png",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Join_AePW_MailingList_button_small.png",
+                    "mediaType": "image/x-png",
                     "title": "Join_AePW_MailingList_button_small.png"
                 },
                 {
-                    "mediaType": "image/pjpeg",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/RSW_results_image.jpg",
-                    "description": "RSW_results_image.jpg",
                     "@type": "dcat:Distribution",
+                    "description": "RSW_results_image.jpg",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/RSW_results_image.jpg",
+                    "mediaType": "image/pjpeg",
                     "title": "RSW_results_image.jpg"
                 },
                 {
-                    "mediaType": "image/gif",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/RSW_analysis_grid.gif",
-                    "description": "RSW_analysis_grid.gif",
                     "@type": "dcat:Distribution",
+                    "description": "RSW_analysis_grid.gif",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/RSW_analysis_grid.gif",
+                    "mediaType": "image/gif",
                     "title": "RSW_analysis_grid.gif"
                 },
                 {
-                    "mediaType": "image/x-png",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/RSW_analysis_image.png",
-                    "description": "RSW_analysis_image.png",
                     "@type": "dcat:Distribution",
+                    "description": "RSW_analysis_image.png",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/RSW_analysis_image.png",
+                    "mediaType": "image/x-png",
                     "title": "RSW_analysis_image.png"
                 },
                 {
-                    "mediaType": "image/pjpeg",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/RSW_publications_image.jpg",
-                    "description": "RSW_publications_image.jpg",
                     "@type": "dcat:Distribution",
+                    "description": "RSW_publications_image.jpg",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/RSW_publications_image.jpg",
+                    "mediaType": "image/pjpeg",
                     "title": "RSW_publications_image.jpg"
                 },
                 {
-                    "mediaType": "image/x-png",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/RSW_publications_image.png",
-                    "description": "RSW_publications_image.png",
                     "@type": "dcat:Distribution",
+                    "description": "RSW_publications_image.png",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/RSW_publications_image.png",
+                    "mediaType": "image/x-png",
                     "title": "RSW_publications_image.png"
                 },
                 {
-                    "mediaType": "image/pjpeg",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/RSW_results_image_2.jpg",
-                    "description": "RSW_results_image.jpg",
                     "@type": "dcat:Distribution",
+                    "description": "RSW_results_image.jpg",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/RSW_results_image_2.jpg",
+                    "mediaType": "image/pjpeg",
                     "title": "RSW_results_image.jpg"
                 },
                 {
-                    "mediaType": "image/gif",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/RSW_analysis_grid_2.gif",
-                    "description": "RSW_analysis_grid.gif",
                     "@type": "dcat:Distribution",
+                    "description": "RSW_analysis_grid.gif",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/RSW_analysis_grid_2.gif",
+                    "mediaType": "image/gif",
                     "title": "RSW_analysis_grid.gif"
                 },
                 {
-                    "mediaType": "image/x-png",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/RSW_Summary_Information.png",
-                    "description": "RSW Summary Information.png",
                     "@type": "dcat:Distribution",
+                    "description": "RSW Summary Information.png",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/RSW_Summary_Information.png",
+                    "mediaType": "image/x-png",
                     "title": "RSW Summary Information.png"
                 },
                 {
-                    "mediaType": "image/x-png",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/RSW_ReferenceQuantities.png",
-                    "description": "RSW_ReferenceQuantities.png",
                     "@type": "dcat:Distribution",
+                    "description": "RSW_ReferenceQuantities.png",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/RSW_ReferenceQuantities.png",
+                    "mediaType": "image/x-png",
                     "title": "RSW_ReferenceQuantities.png"
                 },
                 {
-                    "mediaType": "image/pjpeg",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/ReferenceQuantities.jpg",
-                    "description": "ReferenceQuantities.jpg",
                     "@type": "dcat:Distribution",
+                    "description": "ReferenceQuantities.jpg",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/ReferenceQuantities.jpg",
+                    "mediaType": "image/pjpeg",
                     "title": "ReferenceQuantities.jpg"
                 },
                 {
-                    "mediaType": "image/pjpeg",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/AnalysisParameters.jpg",
-                    "description": "AnalysisParameters.jpg",
                     "@type": "dcat:Distribution",
+                    "description": "AnalysisParameters.jpg",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/AnalysisParameters.jpg",
+                    "mediaType": "image/pjpeg",
                     "title": "AnalysisParameters.jpg"
                 },
                 {
-                    "mediaType": "image/x-png",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/IFASD_icon.png",
-                    "description": "IFASD_icon.png",
                     "@type": "dcat:Distribution",
+                    "description": "IFASD_icon.png",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/IFASD_icon.png",
+                    "mediaType": "image/x-png",
                     "title": "IFASD_icon.png"
                 },
                 {
-                    "mediaType": "image/x-png",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/SDM_icon.png",
-                    "description": "SDM_icon.png",
                     "@type": "dcat:Distribution",
+                    "description": "SDM_icon.png",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/SDM_icon.png",
+                    "mediaType": "image/x-png",
                     "title": "SDM_icon.png"
                 },
                 {
-                    "mediaType": "image/x-png",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/ASM_icon.png",
-                    "description": "ASM_icon.png",
                     "@type": "dcat:Distribution",
+                    "description": "ASM_icon.png",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/ASM_icon.png",
+                    "mediaType": "image/x-png",
                     "title": "ASM_icon.png"
                 },
                 {
-                    "mediaType": "image/pjpeg",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/MicrosoftWord_icon.jpg",
-                    "description": "MicrosoftWord_icon.jpg",
                     "@type": "dcat:Distribution",
+                    "description": "MicrosoftWord_icon.jpg",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/MicrosoftWord_icon.jpg",
+                    "mediaType": "image/pjpeg",
                     "title": "MicrosoftWord_icon.jpg"
                 },
                 {
-                    "mediaType": "image/pjpeg",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/powerpoint_logo.jpg",
-                    "description": "powerpoint_logo.jpg",
                     "@type": "dcat:Distribution",
+                    "description": "powerpoint_logo.jpg",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/powerpoint_logo.jpg",
+                    "mediaType": "image/pjpeg",
                     "title": "powerpoint_logo.jpg"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/AePW_Kickoff_flyer2.jpg",
-                    "description": "AePW2_KickOff_Flyer",
                     "@type": "dcat:Distribution",
+                    "description": "AePW2_KickOff_Flyer",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/AePW_Kickoff_flyer2.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "AePW Kickoff flyer2.jpg"
                 }
             ],
-            "accrualPeriodicity": "irregular"
+            "identifier": "DASHLINK_832",
+            "issued": "2013-09-06",
+            "keyword": [
+                "nasa",
+                "dashlink",
+                "ames"
+            ],
+            "landingPage": "https://c3.nasa.gov/dashlink/resources/832/",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:029"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Dashlink"
+            },
+            "title": "Images"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ASDC_DAAC/TARFOX/0001",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "1999-10-05. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/ASDC_DAAC/TARFOX/0001. http://eosweb.larc.nasa.gov/project/tarfox/tarfox_table.",
-            "issued": "1999-10-05",
-            "temporal": "1996-07-10T00:00:00Z/1996-07-31T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2018-07-03",
-            "keyword": [
-                "earth science",
-                "aerosols",
-                "atmosphere"
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
-            "identifier": "C1536049396-LARC_ASDC",
             "description": "TARFOX_UWC131A_SUNP Data Set was collected from the 6-channel Sun Photometer flown on the University of Washington C-131A aircraft during the Tropospheric Aerosol Radiative Forcing Observational eXperiment (TARFOX) mission.The TARFOX Intensive Field Campaign was conducted July 10-31, 1996. It included coordinated measurements from four satellites (GOES-8, NOAA-14, ERS-2, LANDSAT), four aircraft (ER-2, C-130, C-131A, and a modified Cessna), land sites, and ships. A variety of aerosol conditions was sampled, ranging from relatively clean behind frontal passages to moderately polluted with aerosol optical depths exceeding 0.5 at mid-visible wavelengths. Gradients of aerosol optical thickness were sampled to aid in isolating aerosol effects from other radiative effects and to more tightly constrain closure tests, including those of satellite retrievals. Early results from TARFOX include demonstration of the unexpected importance of carbonaceous compounds and water condensed on aerosol in the US mid-Atlantic haze plume, chemical apportionment of the aerosol optical depth, measurements of the downward component of aerosol radiative forcing, and agreement between forcing measurements and calculations.",
-            "title": "Tropospheric Aerosol Radiative Forcing Observational eXperiment - Ames Sun Photometer - University of Washington C-131A aircraft",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC_DAAC%2FTARFOX%2F0001",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC_DAAC%2FTARFOX%2F0001",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
@@ -1570857,232 +1570838,265 @@
                     "title": "View this dataset's product usage"
                 }
             ],
+            "identifier": "C1536049396-LARC_ASDC",
+            "issued": "1999-10-05",
+            "keyword": [
+                "earth science",
+                "aerosols",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.5067/ASDC_DAAC/TARFOX/0001",
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
             "spatial": "-76.53 36.01 -72.56 39.78",
+            "temporal": "1996-07-10T00:00:00Z/1996-07-31T23:59:59Z",
             "theme": [
                 "TARFOX",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Tropospheric Aerosol Radiative Forcing Observational eXperiment - Ames Sun Photometer - University of Washington C-131A aircraft"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C2263932520-OB_DAAC.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/GSFC/SED/ESD/GCDC/OB.DAAC.",
-            "issued": "2022-09-13",
-            "temporal": "2018-04-25T00:00:00Z/2024-04-22T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-04-13",
-            "keyword": [
-                "atmospheric radiation",
-                "oceans",
-                "atmosphere",
-                "earth science",
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
-            "identifier": "C2263932520-OB_DAAC",
             "description": "The Ocean Biology DAAC produces near real-time (quicklook) products using the best-available combination of ancillary data from meteorological and ozone data. As such, the inputs and the calibration used are less than optimal. Quicklook products provide a snapshot of the data during a short time period within a single orbit.",
-            "title": "Sentinel-3B OLCI Level-3B Global Binned Earth-observation Reduced Resolution (ERR) Remote-Sensing Reflectance (RRS) - Near Real-time (NRT) Data, version R2022.0",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://oceandata.sci.gsfc.nasa.gov/directdataaccess/Level-3%20Binned/S3B-OLCI",
-                    "description": "NASA Ocean Color Web - Data Distribution Site",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Ocean Color Web - Data Distribution Site",
+                    "downloadURL": "https://oceandata.sci.gsfc.nasa.gov/directdataaccess/Level-3%20Binned/S3B-OLCI",
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
+            "identifier": "C2263932520-OB_DAAC",
+            "issued": "2022-09-13",
+            "keyword": [
+                "atmospheric radiation",
+                "oceans",
+                "atmosphere",
+                "earth science",
+                "ocean optics"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C2263932520-OB_DAAC.html",
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
+            "title": "Sentinel-3B OLCI Level-3B Global Binned Earth-observation Reduced Resolution (ERR) Remote-Sensing Reflectance (RRS) - Near Real-time (NRT) Data, version R2022.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/797",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Holland, E.A., J. Lee-Taylor, C. Nevison, and J.M. Sulzman. 2005. Global N Cycle: Fluxes and N2O Mixing Ratios Originating from Human Activity. ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/797",
-            "issued": "2023-10-02",
-            "temporal": "1756-01-01T00:00:00Z/2004-12-31T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-10-03",
-            "keyword": [
-                "biosphere",
-                "environmental impacts",
-                "human dimensions",
-                "socioeconomics",
-                "agricultural chemicals",
-                "agriculture",
-                "atmosphere",
-                "atmospheric chemistry",
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
-            "identifier": "C2776893351-ORNL_CLOUD",
             "description": "Nitrogen is a major nutrient in terrestrial ecosystems and an important catalyst in tropospheric photochemistry. Over the last century human activities have dramatically increased inputs of reactive nitrogen (Nr, the combination of oxidized, reduced and organically bound nitrogen) to the Earth system. Nitrogen cycle perturbations have compromised air quality and human health, acidified ecosystems, and degraded and eutrophied  lakes and coastal estuaries [Vitousek et al., 1997a, 1997b; Rabalais, 2002; Howarth et al., 2003; Townsend et al., 2003; Galloway et al., 2004]. To begin to quantify the changes to the global N cycle, we have assembled key flux data and N2O mixing ratios from various sources.  The data assembled from different sources includes fertilizer production from 1920-2004;  manure production from 1860-2004; crop N fixation estimated for three time points, 1860, 1900, 1995; tropospheric N2O mixing ratios from ice core and firn measurements, and tropospheric concentrations to cover the time period from 1756-2004.  The changing N2O concentrations provide an independent index of changes to the global N cycle, in much the same way that changing carbon dioxide concentrations provide an important constraint on the global carbon cycle.  The changes to the global N cycle are driven by industrialization, as indicated by fossil fuel NOx emission, and by the intensification of agriculture, as indicted by fertilizer and manure production and crop N2 fixation. The data set and the science it reflects are by nature interdisciplinary.  Making the data set available through the ORNL DAAC is an attempt to make the data set available to the considerable interdisciplinary community studying the N cycle.",
-            "graphic-preview-description": "Browse Image",
-            "title": "Global N Cycle: Fluxes and N2O Mixing Ratios Originating from Human Activity",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/climate_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F797",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F797",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/global_climate/global_N_cycle/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/global_climate/global_N_cycle/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/CLIMATE/guides/N_Emiss.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/CLIMATE/guides/N_Emiss.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/797",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/797",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/global_climate/global_N_cycle/comp/global_N_perturbations.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/global_climate/global_N_cycle/comp/global_N_perturbations.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/global_climate/global_N_cycle/comp/N_Emiss.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/global_climate/global_N_cycle/comp/N_Emiss.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://daac.ornl.gov/graphics/browse/project/square/climate_logo_square.png",
-                    "description": "Browse Image",
                     "@type": "dcat:Distribution",
+                    "description": "Browse Image",
+                    "downloadURL": "https://daac.ornl.gov/graphics/browse/project/square/climate_logo_square.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 }
             ],
+            "graphic-preview-description": "Browse Image",
+            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/climate_logo_square.png",
+            "identifier": "C2776893351-ORNL_CLOUD",
+            "issued": "2023-10-02",
+            "keyword": [
+                "biosphere",
+                "environmental impacts",
+                "human dimensions",
+                "socioeconomics",
+                "agricultural chemicals",
+                "agriculture",
+                "atmosphere",
+                "atmospheric chemistry",
+                "earth science",
+                "ecological dynamics"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/797",
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
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "1756-01-01T00:00:00Z/2004-12-31T23:59:59Z",
             "theme": [
                 "Climate",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Global N Cycle: Fluxes and N2O Mixing Ratios Originating from Human Activity"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MSL-M-SAM-2-EDR-V1.0",
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
+            "description": "N/A",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.msl-m-sam-2-edr-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "mars",
+                "mars science laboratory"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MSL-M-SAM-2-EDR-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.msl-m-sam-2-edr-v1.0",
-            "description": "N/A",
-            "title": "MSL MARS SAMPLE ANALYSIS AT MARS 2 EDR V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "MSL MARS SAMPLE ANALYSIS AT MARS 2 EDR V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.nasa.gov/d/wfqi-8t9c",
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
+            "identifier": "nasa_genelab_GLDS-2_wfqi-8t9c",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
             "keyword": [
                 "p-gse16518-5",
                 "bioassay_data_transformation",
@@ -1571102,227 +1571116,192 @@
                 "p-gse16518-7",
                 "p-gse16518-6"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "GeneLab Outreach",
-                "hasEmail": "mailto:genelab-outreach@lists.nasa.gov"
-            },
+            "landingPage": "https://data.nasa.gov/d/wfqi-8t9c",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "nasa_genelab_GLDS-2_wfqi-8t9c",
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
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
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
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO%2FRL-CAL-CONSERT-2-CVP2-V1.0",
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
-                "international rosetta mission"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This archive contains edited data from the CONSERT instrument onboard ROSETTA Orbiter and Lander, acquired during the Commissioning 2 phase. It also contains documentation which describes the CONSERT experiment. The data archived in this data set conform to the Planetary Data System (PDS) Standards, Version 3.6.  This data set supersedes RO/RL-CAL-CONSERT-2-CVP-V1.0.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-rl-cal-consert-2-cvp2-v1.0_wfqj-wbgc",
+            "issued": "2021-05-21",
+            "keyword": [
+                "calibration",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO%2FRL-CAL-CONSERT-2-CVP2-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-rl-cal-consert-2-cvp2-v1.0_wfqj-wbgc",
-            "description": "This archive contains edited data from the CONSERT instrument onboard ROSETTA Orbiter and Lander, acquired during the Commissioning 2 phase. It also contains documentation which describes the CONSERT experiment. The data archived in this data set conform to the Planetary Data System (PDS) Standards, Version 3.6.  This data set supersedes RO/RL-CAL-CONSERT-2-CVP-V1.0.",
-            "title": "ROSETTA-ORBITER/ROSETTA-LANDER CAL CONSERT\n                            2 CVP2 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER/ROSETTA-LANDER CAL CONSERT\n                            2 CVP2 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1641914526-OB_DAAC.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, OB.DAAC.",
-            "issued": "2019-06-23",
-            "temporal": "2000-02-24T00:00:00Z/2022-01-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2019-10-01",
-            "keyword": [
-                "national geospatial data asset",
-                "ocean temperature",
-                "oceans",
-                "ngda",
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
-            "identifier": "C1641914526-OB_DAAC",
             "description": "The Ocean Biology DAAC produces near real-time (quicklook) products using the best-available combination of ancillary data from meteorological and ozone data. As such, the inputs and the calibration used are less than optimal. Quicklook products provide a snapshot of the data during a short time period within a single orbit.",
-            "title": "Terra MODIS Global Mapped 11\u00b5m Nighttime Sea Surface Temperature (NSST) - Near Real Time (NRT) Data, version R2019.0",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://oceandata.sci.gsfc.nasa.gov/directaccess/MODIS-Terra/L3SMI/",
-                    "description": "NASA Ocean Color Web - Data Distribution Site",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Ocean Color Web - Data Distribution Site",
+                    "downloadURL": "https://oceandata.sci.gsfc.nasa.gov/directaccess/MODIS-Terra/L3SMI/",
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
-                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/data/10.5067/TERRA/MODIS/L3M/NSST/R2019.0",
-                    "description": "MODIS-Terra L3M 11\u00b5m Nighttime Sea Surface Temperature (NSST) - Near Real Time (NRT) Dataset Landing Page",
                     "@type": "dcat:Distribution",
+                    "description": "MODIS-Terra L3M 11\u00b5m Nighttime Sea Surface Temperature (NSST) - Near Real Time (NRT) Dataset Landing Page",
+                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/data/10.5067/TERRA/MODIS/L3M/NSST/R2019.0",
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
+            "identifier": "C1641914526-OB_DAAC",
+            "issued": "2019-06-23",
+            "keyword": [
+                "national geospatial data asset",
+                "ocean temperature",
+                "oceans",
+                "ngda",
+                "earth science"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1641914526-OB_DAAC.html",
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
+            "temporal": "2000-02-24T00:00:00Z/2022-01-17T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Terra MODIS Global Mapped 11\u00b5m Nighttime Sea Surface Temperature (NSST) - Near Real Time (NRT) Data, version R2019.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NEAR-A-MAG-3-RDR-EROS%2FFLY%2FBY-V1.0",
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
+            "description": "NEAR MAG RDR volume sets contain a single data set, from one instrument and one mission phase (defined in the phase table in /AAREADME.TXT).",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.near-a-mag-3-rdr-eros-fly-by-v1.0_wftd-hvbt",
+            "issued": "2018-06-26",
+            "keyword": [
+                "near earth asteroid rendezvous",
+                "eros"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NEAR-A-MAG-3-RDR-EROS%2FFLY%2FBY-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.near-a-mag-3-rdr-eros-fly-by-v1.0_wftd-hvbt",
-            "description": "NEAR MAG RDR volume sets contain a single data set, from one instrument and one mission phase (defined in the phase table in /AAREADME.TXT).",
-            "title": "NEAR MAG DATA FOR EROS/FLY/BY",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "NEAR MAG DATA FOR EROS/FLY/BY"
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
-                "catalog",
-                "lunar"
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
-            "identifier": "NASA-890__3",
             "description": "Apollo 17 Sample Catalog; JSC-26088; G. Ryder",
-            "title": "Apollo 17 Sample Catalog",
-            "programCode": [
-                "026:008"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -1571330,23 +1571309,53 @@
                     "mediaType": "application/pdf"
                 }
             ],
-            "accrualPeriodicity": "irregular",
+            "identifier": "NASA-890__3",
+            "issued": "2018-06-25",
+            "keyword": [
+                "apollo",
+                "sample",
+                "catalog",
+                "lunar"
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
+            "title": "Apollo 17 Sample Catalog"
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
+                    "downloadURL": "https://pds.jpl.nasa.gov/tools/subscription_service/PDS-Subscription-Service-25-Oct-04.shtml",
+                    "mediaType": "application/html"
+                }
             ],
+            "identifier": "NASA-630",
+            "issued": "2018-06-25",
             "keyword": [
                 "mtes",
                 "hazcam",
@@ -1571358,482 +1571367,484 @@
                 "apxs",
                 "mi"
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
-            "identifier": "NASA-630",
-            "description": "APXS, HAZCAM, MB, MI, MTES, NAVCAM, PANCAM, SPICE",
-            "title": "PDS Mars Exploration Rovers Data Release 2 (MER1)",
-            "programCode": [
-                "026:005"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://pds.jpl.nasa.gov/tools/subscription_service/PDS-Subscription-Service-25-Oct-04.shtml",
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
+            "title": "PDS Mars Exploration Rovers Data Release 2 (MER1)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/2359",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Xu, Y., Q. Zhuang, B. Zhao, M. Billmire, C. Cook, J.A. Graham, N.H.F. French, and R. Prinn. 2024. Impacts of Wildfires on Boreal Forest Ecosystem Carbon Dynamics. ORNL DAAC, Oak Ridge, Tennessee, USA. https://doi.org/10.3334/ORNLDAAC/2359",
-            "issued": "2024-09-06",
-            "temporal": "1986-01-01T00:00:00Z/2020-12-31T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-09-11",
-            "keyword": [
-                "vegetation",
-                "soils",
-                "natural hazards",
-                "land surface",
-                "human dimensions",
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
-            "identifier": "C3234724704-ORNL_CLOUD",
             "description": "This dataset contains simulations of net primary production (NPP), heterotrophic respiration (RH), net ecosystem production (NEP), and soil temperature data in North American boreal forests for the period 1986-2020. Data sources included historical fire sources and Landsat data. The delta Normalized Burn Ratio (dNBR), which can be used to represent burn severity for a fire, was calculated for each individual fire over the time period. The interactions between canopy, fire and soil thermal dynamics were modelled using a soil surface energy balance model  incorporated into a previous Terrestrial Ecosystem Model (TEM). Using the revised TEM, two regional simulations were conducted with and without fire disturbance. Fire polygons were dissected into each unit with unique fire history and then intersected with each grid cell to measure fire impacts. The output values for each grid cell are the area-weighted mean of each fire polygon and unburned area within the cell. Two extra simulations without a canopy energy balance scheme were also conducted to quantify the impact of the canopy. Soil temperature was simulated with and without the canopy energy balance scheme in the model in addition to considering fire impacts.",
-            "graphic-preview-description": "Spatial pattern of carbon dynamics during 1986-2020: (a) cumulative net ecosystem productivity (NEP) considering fires; (b) cumulative NEP without considering fires; (c) differences of NEP with and without considering fires (a minus b); (d) time-mean ecosystem carbon storage (vegetation carbon plus soil carbon) considering fires; (e) ecosystem carbon storage without considering fires; (f) differences of carbon storage with and without considering fires (d minus e).",
-            "title": "Impacts of Wildfires on Boreal Forest Ecosystem Carbon Dynamics",
-            "graphic-preview-file": "https://daac.ornl.gov/NACP/guides/Wildfire_Impacts_Boreal_Ecosys_Fig1.jpg",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F2359",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F2359",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/nacp/Wildfire_Impacts_Boreal_Ecosys/data/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/nacp/Wildfire_Impacts_Boreal_Ecosys/data/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "application/zip",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/protected/bundle/Wildfire_Impacts_Boreal_Ecosys_2359.zip",
-                    "description": "Collection bundle",
                     "@type": "dcat:Distribution",
+                    "description": "Collection bundle",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/protected/bundle/Wildfire_Impacts_Boreal_Ecosys_2359.zip",
+                    "mediaType": "application/zip",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/NACP/guides/Wildfire_Impacts_Boreal_Ecosys.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/NACP/guides/Wildfire_Impacts_Boreal_Ecosys.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/2359",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/2359",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/zip",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/protected/bundle/Wildfire_Impacts_Boreal_Ecosys_2359.zip",
-                    "description": "Collection bundle",
                     "@type": "dcat:Distribution",
+                    "description": "Collection bundle",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/protected/bundle/Wildfire_Impacts_Boreal_Ecosys_2359.zip",
+                    "mediaType": "application/zip",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/nacp/Wildfire_Impacts_Boreal_Ecosys/comp/Wildfire_Impacts_Boreal_Ecosys.pdf",
-                    "description": "Impacts of Wildfires on Boreal Forest Ecosystem Carbon Dynamics: Wildfire_Impacts_Boreal_Ecosys.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "Impacts of Wildfires on Boreal Forest Ecosystem Carbon Dynamics: Wildfire_Impacts_Boreal_Ecosys.pdf",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/nacp/Wildfire_Impacts_Boreal_Ecosys/comp/Wildfire_Impacts_Boreal_Ecosys.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://daac.ornl.gov/NACP/guides/Wildfire_Impacts_Boreal_Ecosys_Fig1.jpg",
-                    "description": "Spatial pattern of carbon dynamics during 1986-2020: (a) cumulative net ecosystem productivity (NEP) considering fires; (b) cumulative NEP without considering fires; (c) differences of NEP with and without considering fires (a minus b); (d) time-mean ecosystem carbon storage (vegetation carbon plus soil carbon) considering fires; (e) ecosystem carbon storage without considering fires; (f) differences of carbon storage with and without considering fires (d minus e).",
                     "@type": "dcat:Distribution",
+                    "description": "Spatial pattern of carbon dynamics during 1986-2020: (a) cumulative net ecosystem productivity (NEP) considering fires; (b) cumulative NEP without considering fires; (c) differences of NEP with and without considering fires (a minus b); (d) time-mean ecosystem carbon storage (vegetation carbon plus soil carbon) considering fires; (e) ecosystem carbon storage without considering fires; (f) differences of carbon storage with and without considering fires (d minus e).",
+                    "downloadURL": "https://daac.ornl.gov/NACP/guides/Wildfire_Impacts_Boreal_Ecosys_Fig1.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 }
             ],
+            "graphic-preview-description": "Spatial pattern of carbon dynamics during 1986-2020: (a) cumulative net ecosystem productivity (NEP) considering fires; (b) cumulative NEP without considering fires; (c) differences of NEP with and without considering fires (a minus b); (d) time-mean ecosystem carbon storage (vegetation carbon plus soil carbon) considering fires; (e) ecosystem carbon storage without considering fires; (f) differences of carbon storage with and without considering fires (d minus e).",
+            "graphic-preview-file": "https://daac.ornl.gov/NACP/guides/Wildfire_Impacts_Boreal_Ecosys_Fig1.jpg",
+            "identifier": "C3234724704-ORNL_CLOUD",
+            "issued": "2024-09-06",
+            "keyword": [
+                "vegetation",
+                "soils",
+                "natural hazards",
+                "land surface",
+                "human dimensions",
+                "earth science",
+                "biosphere"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/2359",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2024-09-11",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "ORNL_DAAC"
+            },
             "spatial": "-166.0 43.5 -53.0 70.0",
+            "temporal": "1986-01-01T00:00:00Z/2020-12-31T23:59:59Z",
             "theme": [
                 "NACP",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Impacts of Wildfires on Boreal Forest Ecosystem Carbon Dynamics"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG2-J-LECP-4-SUMM-SECTOR-15MIN-V1.0",
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
-                "jupiter"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "not applicable",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg2-j-lecp-4-summ-sector-15min-v1.0_wfxs-dzuq",
+            "issued": "2018-06-26",
+            "keyword": [
+                "voyager",
+                "jupiter"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG2-J-LECP-4-SUMM-SECTOR-15MIN-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg2-j-lecp-4-summ-sector-15min-v1.0_wfxs-dzuq",
-            "description": "not applicable",
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
-            "landingPage": "https://c3.nasa.gov/dashlink/resources/332/",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2011-04-01",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
-            "keyword": [
-                "nasa",
-                "dashlink",
-                "ames"
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
-            "identifier": "DASHLINK_332",
             "description": "This is a resource where HTML files will be stored for the website",
-            "title": "HTML files",
-            "programCode": [
-                "026:029"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/participate.htm",
-                    "description": "participate.htm",
                     "@type": "dcat:Distribution",
+                    "description": "participate.htm",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/participate.htm",
+                    "mediaType": "text/html",
                     "title": "participate.htm"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/join_aepw_list.htm",
-                    "description": "join_aepw_list.htm",
                     "@type": "dcat:Distribution",
+                    "description": "join_aepw_list.htm",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/join_aepw_list.htm",
+                    "mediaType": "text/html",
                     "title": "join_aepw_list.htm"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/BSCW_base.htm",
-                    "description": "Feb 8, 2012",
                     "@type": "dcat:Distribution",
+                    "description": "Feb 8, 2012",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/BSCW_base.htm",
+                    "mediaType": "text/html",
                     "title": "BSCW_base.htm"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/RSW_base.htm",
-                    "description": "Feb 10, 2012 JH",
                     "@type": "dcat:Distribution",
+                    "description": "Feb 10, 2012 JH",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/RSW_base.htm",
+                    "mediaType": "text/html",
                     "title": "RSW_base.htm"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/AePW_likeAB_main_v2.htm",
-                    "description": "workshop presentations access page (updated Dec 11,2010 JH)",
                     "@type": "dcat:Distribution",
+                    "description": "workshop presentations access page (updated Dec 11,2010 JH)",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/AePW_likeAB_main_v2.htm",
+                    "mediaType": "text/html",
                     "title": "AePW_likeAB_main_v2.htm"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/AePW_likeAB_main_v3.htm",
-                    "description": "workshop presentations access, v3 (updated JHeeg, Dec 11, 2012)",
                     "@type": "dcat:Distribution",
+                    "description": "workshop presentations access, v3 (updated JHeeg, Dec 11, 2012)",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/AePW_likeAB_main_v3.htm",
+                    "mediaType": "text/html",
                     "title": "AePW_likeAB_main_v3.htm"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/HIRENASD_base.htm",
-                    "description": "Feb 21, 2013, pc",
                     "@type": "dcat:Distribution",
+                    "description": "Feb 21, 2013, pc",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/HIRENASD_base.htm",
+                    "mediaType": "text/html",
                     "title": "HIRENASD_base.htm"
                 },
                 {
-                    "mediaType": "application/octet-stream",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/jquery.easing.1.3.js",
-                    "description": "jquery.easing.1.3.js",
                     "@type": "dcat:Distribution",
+                    "description": "jquery.easing.1.3.js",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/jquery.easing.1.3.js",
+                    "mediaType": "application/octet-stream",
                     "title": "jquery.easing.1.3.js"
                 },
                 {
-                    "mediaType": "text/css",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/jquery.ennui.contentslider.css",
-                    "description": "jquery.ennui.contentslider.css",
                     "@type": "dcat:Distribution",
+                    "description": "jquery.ennui.contentslider.css",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/jquery.ennui.contentslider.css",
+                    "mediaType": "text/css",
                     "title": "jquery.ennui.contentslider.css"
                 },
                 {
-                    "mediaType": "application/octet-stream",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/jquery.ennui.contentslider.js",
-                    "description": "jquery.ennui.contentslider.js",
                     "@type": "dcat:Distribution",
+                    "description": "jquery.ennui.contentslider.js",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/jquery.ennui.contentslider.js",
+                    "mediaType": "application/octet-stream",
                     "title": "jquery.ennui.contentslider.js"
                 },
                 {
-                    "mediaType": "application/octet-stream",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/jquery.min.1.3.2.js",
-                    "description": "jquery.min.1.3.2.js",
                     "@type": "dcat:Distribution",
+                    "description": "jquery.min.1.3.2.js",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/jquery.min.1.3.2.js",
+                    "mediaType": "application/octet-stream",
                     "title": "jquery.min.1.3.2.js"
                 },
                 {
-                    "mediaType": "application/octet-stream",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/tabcontent.js",
-                    "description": "tabcontent.js",
                     "@type": "dcat:Distribution",
+                    "description": "tabcontent.js",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/tabcontent.js",
+                    "mediaType": "application/octet-stream",
                     "title": "tabcontent.js"
                 },
                 {
-                    "mediaType": "text/css",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/tabcontent.css",
-                    "description": "tabcontent.css",
                     "@type": "dcat:Distribution",
+                    "description": "tabcontent.css",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/tabcontent.css",
+                    "mediaType": "text/css",
                     "title": "tabcontent.css"
                 },
                 {
-                    "mediaType": "text/css",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/AEPW_style.css",
-                    "description": "AEPW_style.css",
                     "@type": "dcat:Distribution",
+                    "description": "AEPW_style.css",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/AEPW_style.css",
+                    "mediaType": "text/css",
                     "title": "AEPW_style.css"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/BSCW_base_legacy.htm",
-                    "description": "legacy file",
                     "@type": "dcat:Distribution",
+                    "description": "legacy file",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/BSCW_base_legacy.htm",
+                    "mediaType": "text/html",
                     "title": "BSCW_base_legacy.htm"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/RSW_base_legacy.htm",
-                    "description": "legacy file",
                     "@type": "dcat:Distribution",
+                    "description": "legacy file",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/RSW_base_legacy.htm",
+                    "mediaType": "text/html",
                     "title": "RSW_base_legacy.htm"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/HIRENASD_base_legacy.htm",
-                    "description": "legacy file",
                     "@type": "dcat:Distribution",
+                    "description": "legacy file",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/HIRENASD_base_legacy.htm",
+                    "mediaType": "text/html",
                     "title": "HIRENASD_base_legacy.htm"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/AEPW_legacy.htm",
-                    "description": "legacy file",
                     "@type": "dcat:Distribution",
+                    "description": "legacy file",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/AEPW_legacy.htm",
+                    "mediaType": "text/html",
                     "title": "AEPW_legacy.htm"
                 },
                 {
-                    "mediaType": "text/css",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/tabcontent_RSW.css",
-                    "description": "tabcontent_RSW.css",
                     "@type": "dcat:Distribution",
+                    "description": "tabcontent_RSW.css",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/tabcontent_RSW.css",
+                    "mediaType": "text/css",
                     "title": "tabcontent_RSW.css"
                 },
                 {
-                    "mediaType": "text/css",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/style_image_enlarge.css",
-                    "description": "style_image_enlarge.css",
                     "@type": "dcat:Distribution",
+                    "description": "style_image_enlarge.css",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/style_image_enlarge.css",
+                    "mediaType": "text/css",
                     "title": "style_image_enlarge.css"
                 },
                 {
-                    "mediaType": "text/css",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/style_image_enlarge_center.css",
-                    "description": "style_image_enlarge_center.css",
                     "@type": "dcat:Distribution",
+                    "description": "style_image_enlarge_center.css",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/style_image_enlarge_center.css",
+                    "mediaType": "text/css",
                     "title": "style_image_enlarge_center.css"
                 },
                 {
-                    "mediaType": "text/css",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/style_image_enlarge_horizontal.css",
-                    "description": "style_image_enlarge_horizontal.css",
                     "@type": "dcat:Distribution",
+                    "description": "style_image_enlarge_horizontal.css",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/style_image_enlarge_horizontal.css",
+                    "mediaType": "text/css",
                     "title": "style_image_enlarge_horizontal.css"
                 },
                 {
-                    "mediaType": "text/css",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/RSW_style.css",
-                    "description": "RSW_style.css",
                     "@type": "dcat:Distribution",
+                    "description": "RSW_style.css",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/RSW_style.css",
+                    "mediaType": "text/css",
                     "title": "RSW_style.css"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/RSW_osc10.htm",
-                    "description": "RSW_osc10.htm",
                     "@type": "dcat:Distribution",
+                    "description": "RSW_osc10.htm",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/RSW_osc10.htm",
+                    "mediaType": "text/html",
                     "title": "RSW_osc10.htm"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/RSW_osc20.htm",
-                    "description": "RSW_osc20.htm",
                     "@type": "dcat:Distribution",
+                    "description": "RSW_osc20.htm",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/RSW_osc20.htm",
+                    "mediaType": "text/html",
                     "title": "RSW_osc20.htm"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/RSW_steady_4deg.htm",
-                    "description": "RSW_steady_4deg.htm",
                     "@type": "dcat:Distribution",
+                    "description": "RSW_steady_4deg.htm",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/RSW_steady_4deg.htm",
+                    "mediaType": "text/html",
                     "title": "RSW_steady_4deg.htm"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/RSW_steady_2deg.htm",
-                    "description": "RSW_steady_2deg.htm",
                     "@type": "dcat:Distribution",
+                    "description": "RSW_steady_2deg.htm",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/RSW_steady_2deg.htm",
+                    "mediaType": "text/html",
                     "title": "RSW_steady_2deg.htm"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/RSW.htm",
-                    "description": "RSW.htm",
                     "@type": "dcat:Distribution",
+                    "description": "RSW.htm",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/RSW.htm",
+                    "mediaType": "text/html",
                     "title": "RSW.htm"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/RSW_AePWResults.htm",
-                    "description": "RSW_AePWResults.htm",
                     "@type": "dcat:Distribution",
+                    "description": "RSW_AePWResults.htm",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/RSW_AePWResults.htm",
+                    "mediaType": "text/html",
                     "title": "RSW_AePWResults.htm"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/RSW_AnalystPage.htm",
-                    "description": "RSW_AnalystPage.htm",
                     "@type": "dcat:Distribution",
+                    "description": "RSW_AnalystPage.htm",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/RSW_AnalystPage.htm",
+                    "mediaType": "text/html",
                     "title": "RSW_AnalystPage.htm"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/RSW_config.htm",
-                    "description": "RSW_config.htm",
                     "@type": "dcat:Distribution",
+                    "description": "RSW_config.htm",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/RSW_config.htm",
+                    "mediaType": "text/html",
                     "title": "RSW_config.htm"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/RSW_Exp.htm",
-                    "description": "RSW_Exp.htm",
                     "@type": "dcat:Distribution",
+                    "description": "RSW_Exp.htm",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/RSW_Exp.htm",
+                    "mediaType": "text/html",
                     "title": "RSW_Exp.htm"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/Database_repository.htm",
-                    "description": "Database_repository.htm",
                     "@type": "dcat:Distribution",
+                    "description": "Database_repository.htm",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/Database_repository.htm",
+                    "mediaType": "text/html",
                     "title": "Database_repository.htm"
                 },
                 {
-                    "mediaType": "text/css",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/BSCW_style.css",
-                    "description": "BSCW_style.css",
                     "@type": "dcat:Distribution",
+                    "description": "BSCW_style.css",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/BSCW_style.css",
+                    "mediaType": "text/css",
                     "title": "BSCW_style.css"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/BSCW.htm",
-                    "description": "BSCW.htm",
                     "@type": "dcat:Distribution",
+                    "description": "BSCW.htm",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/BSCW.htm",
+                    "mediaType": "text/html",
                     "title": "BSCW.htm"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/BSCW_AnalystPage.htm",
-                    "description": "BSCW_AnalystPage.htm",
                     "@type": "dcat:Distribution",
+                    "description": "BSCW_AnalystPage.htm",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/BSCW_AnalystPage.htm",
+                    "mediaType": "text/html",
                     "title": "BSCW_AnalystPage.htm"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/Publications_AePW.htm",
-                    "description": "Publications_AePW.htm",
                     "@type": "dcat:Distribution",
+                    "description": "Publications_AePW.htm",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/Publications_AePW.htm",
+                    "mediaType": "text/html",
                     "title": "Publications_AePW.htm"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/AEPW.htm",
-                    "description": "Jan 12, 2015, JH",
                     "@type": "dcat:Distribution",
+                    "description": "Jan 12, 2015, JH",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/AEPW.htm",
+                    "mediaType": "text/html",
                     "title": "AEPW.htm"
                 }
             ],
-            "accrualPeriodicity": "irregular"
+            "identifier": "DASHLINK_332",
+            "issued": "2011-04-01",
+            "keyword": [
+                "nasa",
+                "dashlink",
+                "ames"
+            ],
+            "landingPage": "https://c3.nasa.gov/dashlink/resources/332/",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:029"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Dashlink"
+            },
+            "title": "HTML files"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.nasa.gov/d/wg2t-cgjr",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Lorraine Remer",
+                "hasEmail": "mailto:Lorraine.A.Remer@mail.nasa.gov"
+            },
+            "description": "MODIS (or Moderate Resolution Imaging Spectroradiometer) is a key instrument aboard the Terra (EOS AM) and Aqua (EOS PM) satellites. Terra's orbit around the Earth is timed so that it passes from north to south across the equator in the morning, while Aqua passes south to north over the equator in the afternoon. Terra MODIS and Aqua MODIS are viewing the entire Earth's surface every 1 to 2 days, acquiring data in 36 spectral bands, or groups of wavelengths (see MODIS Technical Specifications). This map shows the temperature of Earth's lands during the nighttime.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://modis.gsfc.nasa.gov/data/",
+                    "mediaType": "text/html"
+                }
+            ],
+            "identifier": "NASA-0000060",
             "issued": "2018-06-25",
-            "temporal": "2010-01-01/2014-01-01",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
             "keyword": [
                 "temperature",
                 "modis",
@@ -1571847,826 +1571858,794 @@
                 "solid earth",
                 "raw"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Lorraine Remer",
-                "hasEmail": "mailto:Lorraine.A.Remer@mail.nasa.gov"
-            },
+            "landingPage": "https://data.nasa.gov/d/wg2t-cgjr",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "NASA-0000060",
-            "description": "MODIS (or Moderate Resolution Imaging Spectroradiometer) is a key instrument aboard the Terra (EOS AM) and Aqua (EOS PM) satellites. Terra's orbit around the Earth is timed so that it passes from north to south across the equator in the morning, while Aqua passes south to north over the equator in the afternoon. Terra MODIS and Aqua MODIS are viewing the entire Earth's surface every 1 to 2 days, acquiring data in 36 spectral bands, or groups of wavelengths (see MODIS Technical Specifications). This map shows the temperature of Earth's lands during the nighttime.",
-            "title": "Land Surface Temperature at Night",
-            "programCode": [
-                "026:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://modis.gsfc.nasa.gov/data/",
-                    "mediaType": "text/html"
-                }
-            ],
-            "accrualPeriodicity": "irregular"
+            "temporal": "2010-01-01/2014-01-01",
+            "title": "Land Surface Temperature at Night"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/92",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Betts, A.K. 1994. Site Averaged Flux Data: 1987 (Betts). ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/92",
-            "issued": "2023-11-21",
-            "temporal": "1987-05-27T00:00:00Z/1987-10-16T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-12-02",
-            "keyword": [
-                "soils",
-                "atmosphere",
-                "earth science",
-                "atmospheric radiation",
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
-            "identifier": "C2810660221-ORNL_CLOUD",
             "description": "Site averaged product of the flux data collected by many PIs during the 1987-1989 FIFE experiment. Data are in 30-minute intervals and include data only for 1987.",
-            "graphic-preview-description": "Browse Image",
-            "title": "Site Averaged Flux Data: 1987 (Betts)",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/fife_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F92",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F92",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/fife/ffo_Betts_1987_afd/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/fife/ffo_Betts_1987_afd/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/FIFE/Follow_On/guides/Betts_flux_data_87.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/FIFE/Follow_On/guides/Betts_flux_data_87.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/92",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/92",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/fife/ffo_Betts_1987_afd/comp/Betts_flux_data_87.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/fife/ffo_Betts_1987_afd/comp/Betts_flux_data_87.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/fife/ffo_Beets_1987_afd/comp/Betts_flux_data_87.txt",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/fife/ffo_Beets_1987_afd/comp/Betts_flux_data_87.txt",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/fife/ffo_Betts_1987_afd/comp/ffoflx87.def",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/fife/ffo_Betts_1987_afd/comp/ffoflx87.def",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/fife/ffo_Betts_1987_afd/comp/ffo_flx.txt",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/fife/ffo_Betts_1987_afd/comp/ffo_flx.txt",
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
+            "identifier": "C2810660221-ORNL_CLOUD",
+            "issued": "2023-11-21",
+            "keyword": [
+                "soils",
+                "atmosphere",
+                "earth science",
+                "atmospheric radiation",
+                "land surface"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/92",
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
+            "temporal": "1987-05-27T00:00:00Z/1987-10-16T23:59:59Z",
             "theme": [
                 "FIFE",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Site Averaged Flux Data: 1987 (Betts)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ECG5M-STR44",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "ECCO Consortium, Fukumori, I., Wang, O., Fenty, I., Forget, G., Heimbach, P., & Ponte, R. M.. 2021-04-19. ECCO Ocean and Sea-Ice Surface Stress - Monthly Mean 0.5 Degree (Version 4 Release 4). Version V4r4. PO.DAAC. Archived by National Aeronautics and Space Administration, U.S. Government, PO.DAAC. https://doi.org/10.5067/ECG5M-STR44. ECCO; ECCO Consortium, Fukumori, I., Wang, O., Fenty, I., Forget, G., Heimbach, P., & Ponte, R. M.; 2020; ECCO Ocean and Sea-Ice Surface Stress - Monthly Mean 0.5 Degree (Version 4 Release 4); 10.5067/ECG5M-STR44; https://podaac.jpl.nasa.gov/ECCO.",
-            "issued": "2021-01-01",
-            "temporal": "1992-01-01T00:00:00Z/2018-01-01T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2017-12-31",
-            "references": [
-                "https://doi.org/10.5281/zenodo.3765928"
-            ],
-            "keyword": [
-                "models",
-                "oceans",
-                "earth science services",
-                "ocean winds",
-                "earth science reanalyses/assimilation models",
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
-            "identifier": "C1990404796-POCLOUD",
-            "description": "This dataset contains monthly-averaged ocean and sea-ice surface stress interpolated to a regular 0.5-degree grid from the ECCO Version 4 revision 4 (V4r4) ocean and sea-ice state estimate. Estimating the Circulation and Climate of the Ocean (ECCO) ocean and sea-ice state estimates are dynamically and kinematically-consistent reconstructions of the three-dimensional, time-evolving ocean, sea-ice, and surface atmospheric states. ECCO V4r4 is a free-running solution of the 1-degree global configuration of the MIT general circulation model (MITgcm) that has been fit to observations in a least-squares sense. Observational data constraints used in V4r4 include sea surface height (SSH) from satellite altimeters [ERS-1/2, TOPEX/Poseidon, GFO, ENVISAT, Jason-1,2,3, CryoSat-2, and SARAL/AltiKa]; sea surface temperature (SST) from satellite radiometers [AVHRR], sea surface salinity (SSS) from the Aquarius satellite radiometer/scatterometer, ocean bottom pressure (OBP) from the GRACE satellite gravimeter; sea ice concentration from satellite radiometers [SSM/I and SSMIS], and in-situ ocean temperature and salinity measured with conductivity-temperature-depth (CTD) sensors and expendable bathythermographs (XBTs) from several programs [e.g., WOCE, GO-SHIP, Argo, and others] and platforms [e.g.,research vessels, gliders, moorings, ice-tethered profilers, and instrumented pinnipeds]. V4r4 covers the period 1992-01-01T12:00:00 to 2018-01-01T00:00:00.",
-            "release-place": "PO.DAAC",
-            "graphic-preview-description": "Thumbnail image for Website",
             "creator": "ECCO Consortium, Fukumori, I., Wang, O., Fenty, I., Forget, G., Heimbach, P., & Ponte, R. M.",
-            "title": "ECCO Ocean and Sea-Ice Surface Stress - Monthly Mean 0.5 Degree (Version 4 Release 4)",
-            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/ECCO_L4_STRESS_05DEG_MONTHLY_V4R4.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "This dataset contains monthly-averaged ocean and sea-ice surface stress interpolated to a regular 0.5-degree grid from the ECCO Version 4 revision 4 (V4r4) ocean and sea-ice state estimate. Estimating the Circulation and Climate of the Ocean (ECCO) ocean and sea-ice state estimates are dynamically and kinematically-consistent reconstructions of the three-dimensional, time-evolving ocean, sea-ice, and surface atmospheric states. ECCO V4r4 is a free-running solution of the 1-degree global configuration of the MIT general circulation model (MITgcm) that has been fit to observations in a least-squares sense. Observational data constraints used in V4r4 include sea surface height (SSH) from satellite altimeters [ERS-1/2, TOPEX/Poseidon, GFO, ENVISAT, Jason-1,2,3, CryoSat-2, and SARAL/AltiKa]; sea surface temperature (SST) from satellite radiometers [AVHRR], sea surface salinity (SSS) from the Aquarius satellite radiometer/scatterometer, ocean bottom pressure (OBP) from the GRACE satellite gravimeter; sea ice concentration from satellite radiometers [SSM/I and SSMIS], and in-situ ocean temperature and salinity measured with conductivity-temperature-depth (CTD) sensors and expendable bathythermographs (XBTs) from several programs [e.g., WOCE, GO-SHIP, Argo, and others] and platforms [e.g.,research vessels, gliders, moorings, ice-tethered profilers, and instrumented pinnipeds]. V4r4 covers the period 1992-01-01T12:00:00 to 2018-01-01T00:00:00.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FECG5M-STR44",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FECG5M-STR44",
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
-                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/ECCO_L4_STRESS_05DEG_MONTHLY_V4R4.jpg",
-                    "description": "Thumbnail image for Website",
                     "@type": "dcat:Distribution",
+                    "description": "Thumbnail image for Website",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/ECCO_L4_STRESS_05DEG_MONTHLY_V4R4.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/ECG5M-STR44",
-                    "description": "Access the data set landing page for the collection.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data set landing page for the collection.",
+                    "downloadURL": "https://doi.org/10.5067/ECG5M-STR44",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1990404796-POCLOUD",
-                    "description": "Browse granule search results in Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse granule search results in Earthdata Search",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1990404796-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C1990404796-POCLOUD/temporal",
-                    "description": "Browse and download granules over HTTPS using the virtual directories service",
-                    "@type": "dcat:Distribution",
-                    "title": "Download this dataset through a directory map"
-                }
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "Browse and download granules over HTTPS using the virtual directories service",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C1990404796-POCLOUD/temporal",
+                    "mediaType": "text/html",
+                    "title": "Download this dataset through a directory map"
+                }
+            ],
+            "graphic-preview-description": "Thumbnail image for Website",
+            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/ECCO_L4_STRESS_05DEG_MONTHLY_V4R4.jpg",
+            "identifier": "C1990404796-POCLOUD",
+            "issued": "2021-01-01",
+            "keyword": [
+                "models",
+                "oceans",
+                "earth science services",
+                "ocean winds",
+                "earth science reanalyses/assimilation models",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/ECG5M-STR44",
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
             ],
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
+            "title": "ECCO Ocean and Sea-Ice Surface Stress - Monthly Mean 0.5 Degree (Version 4 Release 4)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/5XSNDT0MX8ZI",
             "citation": "Miyazaki, Kazuyuki. 2024-02-06. TRPSCRTM3D. Version 1. TROPESS Chemical Reanalysis Temperature Monthly 3-dimensional Product V1. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/5XSNDT0MX8ZI. https://disc.gsfc.nasa.gov/datacollection/TRPSCRTM3D_1.html. Digital Science Data.",
-            "issued": "2023-01-09",
-            "temporal": "2005-01-01T00:00:00Z/2024-02-12T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-09",
-            "references": [
-                "https://doi.org/10.1126/sciadv.abf7460"
-            ],
-            "keyword": [
-                "atmosphere",
-                "atmospheric temperature",
-                "earth science"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "KAZUYUKI MIYAZAKI",
                 "hasEmail": "mailto:kazuyuki.miyazaki@jpl.nasa.gov"
             },
+            "creator": "Miyazaki, Kazuyuki",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C2837626762-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "The TROPESS Chemical Reanalysis Temperature Monthly 3-dimensional Product contains vertical temperature values, a meteorological field. The data are part of the Tropospheric Chemical Reanalysis v2 (TCR-2) for the period 2005-2021. TCR-2 uses JPL's Multi-mOdel Multi-cOnstituent Chemical (MOMO-Chem) data assimilation framework that simultaneously optimizes both concentrations and emissions of multiple species from multiple satellite sensors.\n\nThe data files are written in the netCDF version 4 file format, and each file contains a year of data at monthly resolution, and a spatial resolution of 1.125 x 1.125 degrees at 27 pressure levels between 1000 and 60 hPa. The principal investigator for the TCR-2 data is Miyazaki, Kazuyuki.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "TRPSCRTM3D",
-            "creator": "Miyazaki, Kazuyuki",
-            "graphic-preview-description": "TROPESS CrIS-SNPP Los Angeles Megacity (Forward Stream, Summary Product) at 681 hPa on 01 April 2021.",
-            "title": "TROPESS Chemical Reanalysis Temperature Monthly 3-dimensional Product V1 (TRPSCRTM3D) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TROPESS/images/TRPSCRTM3D_Sample.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2F5XSNDT0MX8ZI",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2F5XSNDT0MX8ZI",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TROPESS/images/TRPSCRTM3D_Sample.png",
-                    "description": "TROPESS CrIS-SNPP Los Angeles Megacity (Forward Stream, Summary Product) at 681 hPa on 01 April 2021.",
                     "@type": "dcat:Distribution",
+                    "description": "TROPESS CrIS-SNPP Los Angeles Megacity (Forward Stream, Summary Product) at 681 hPa on 01 April 2021.",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TROPESS/images/TRPSCRTM3D_Sample.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/TRPSCRTM3D_1.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/TRPSCRTM3D_1.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/data/TCR2_MON_VERTCONCS/TRPSCRTM3D.1/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/data/TCR2_MON_VERTCONCS/TRPSCRTM3D.1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=TRPSCRTM3D_1",
-                    "description": "Use the Earthdata Search Client to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search Client to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=TRPSCRTM3D_1",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/opendap/TCR2_MON_METFIELDS/TRPSCRTM3D.1/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/opendap/TCR2_MON_METFIELDS/TRPSCRTM3D.1/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/data/TCR2_MON_METFIELDS/TRPSCRTM3D.1/doc/TROPESS_ChemReanalysis_Forward_Stream_README.pdf",
-                    "description": "README Document",
                     "@type": "dcat:Distribution",
+                    "description": "README Document",
+                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/data/TCR2_MON_METFIELDS/TRPSCRTM3D.1/doc/TROPESS_ChemReanalysis_Forward_Stream_README.pdf",
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
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TROPESS/images/TRPSCRTM3D_Sample.png",
+            "identifier": "C2837626762-GES_DISC",
+            "issued": "2023-01-09",
+            "keyword": [
+                "atmosphere",
+                "atmospheric temperature",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/5XSNDT0MX8ZI",
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
+            "series-name": "TRPSCRTM3D",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2005-01-01T00:00:00Z/2024-02-12T00:00:00Z",
             "theme": [
                 "TROPESS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "TROPESS Chemical Reanalysis Temperature Monthly 3-dimensional Product V1 (TRPSCRTM3D) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1650",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Holmquist, J.R., L. Windham-Myers, B. Bernal, K.B. Byrd, S. Crooks, M.E. Gonneea, N. Herold, S.H. Knox, K. Kroeger, J. Mccombs, P.J. Megonigal, L. Meng, J.T. Morris, A.E. Sutton-grier, T. Troxler, and D. Weller. 2019. Coastal Wetland Elevation and Carbon Flux Inventory with Uncertainty, USA, 2006-2011. ORNL DAAC, Oak Ridge, Tennessee, USA. https://doi.org/10.3334/ORNLDAAC/1650",
-            "issued": "2019-12-17",
-            "temporal": "2006-01-01T00:00:00Z/2011-12-31T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-06-12",
-            "keyword": [
-                "carbon flux",
-                "climate indicators",
-                "ecosystems",
-                "biosphere",
-                "soils",
-                "vegetation",
-                "geomorphic landforms/processes",
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
-            "identifier": "C2389101052-ORNL_CLOUD",
             "description": "This dataset provides maps of coastal wetland carbon and methane fluxes and coastal wetland surface elevation from 2006 to 2011 at 30 m resolution for coastal wetlands of the conterminous United States. Total coastal wetland carbon flux per year per pixel was calculated by combining maps of wetland type and change with soil, biomass, and methane flux data from a literature review. Uncertainty in carbon flux was estimated from 10,000 iterations of a Monte Carlo analysis. In addition to the uncertainty analysis, this dataset also provides a probabilistic map of the extent of tidal elevation, as well as the geospatial files used to create that surface, and a land cover and land cover change map of the coastal zone from 2006 to 2011 with accompanying estimated median soil, biomass, methane, and total CO2 equivalent annual fluxes, each with reported 95% confidence intervals, at 30 m resolution. Land cover was quantified using the Coastal Change Analysis Program (C-CAP), a Landsat-based land cover mapping product.",
-            "graphic-preview-description": "Estimated CO2e fluxes and confidence interval ranges for the Mississippi River outlet in Louisiana, United States. This area contains palustrine and estuarine wetlands, and includes stable wetlands, wetland gains and loss events from 2006 to 2011. A: Total flux from 2006 to 2011. B. Uncertainty, as represented by confidence interval range (0.975 - 0.025 quantile distributions of the results of the Monte Carlo Analysis). C-E. The relative contributions of soil, biomass, and methane to the total flux (A).",
-            "title": "Coastal Wetland Elevation and Carbon Flux Inventory with Uncertainty, USA, 2006-2011",
-            "graphic-preview-file": "https://daac.ornl.gov/CMS/guides/Uncertainty_US_Coastal_GHG_Fig1.jpg",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1650",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1650",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/cms/Uncertainty_US_Coastal_GHG/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/cms/Uncertainty_US_Coastal_GHG/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/CMS/guides/Uncertainty_US_Coastal_GHG.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/CMS/guides/Uncertainty_US_Coastal_GHG.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1650",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1650",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/cms/Uncertainty_US_Coastal_GHG/comp/A1_Supplemental_Information.pdf",
-                    "description": "Coastal Wetland Elevation and Carbon Flux Inventory with Uncertainty, USA, 2006-2011: A1_Supplemental_Information.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "Coastal Wetland Elevation and Carbon Flux Inventory with Uncertainty, USA, 2006-2011: A1_Supplemental_Information.pdf",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/cms/Uncertainty_US_Coastal_GHG/comp/A1_Supplemental_Information.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/cms/Uncertainty_US_Coastal_GHG/comp/A2_Supplemental_Table_1.csv",
-                    "description": "Coastal Wetland Elevation and Carbon Flux Inventory with Uncertainty, USA, 2006-2011: A2_Supplemental_Table_1.csv",
                     "@type": "dcat:Distribution",
+                    "description": "Coastal Wetland Elevation and Carbon Flux Inventory with Uncertainty, USA, 2006-2011: A2_Supplemental_Table_1.csv",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/cms/Uncertainty_US_Coastal_GHG/comp/A2_Supplemental_Table_1.csv",
+                    "mediaType": "text/csv",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/cms/Uncertainty_US_Coastal_GHG/comp/coastal_wetland_downscaled_carbon_fluxes_2006_to_2011.tif.vat.dbf",
-                    "description": "Coastal Wetland Elevation and Carbon Flux Inventory with Uncertainty, USA, 2006-2011: coastal_wetland_downscaled_carbon_fluxes_2006_to_2011.tif.vat.dbf",
                     "@type": "dcat:Distribution",
+                    "description": "Coastal Wetland Elevation and Carbon Flux Inventory with Uncertainty, USA, 2006-2011: coastal_wetland_downscaled_carbon_fluxes_2006_to_2011.tif.vat.dbf",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/cms/Uncertainty_US_Coastal_GHG/comp/coastal_wetland_downscaled_carbon_fluxes_2006_to_2011.tif.vat.dbf",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/vnd.google-earth.kmz",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/cms/Uncertainty_US_Coastal_GHG/comp/MHHWS_MHHW_gauges.kmz",
-                    "description": "Coastal Wetland Elevation and Carbon Flux Inventory with Uncertainty, USA, 2006-2011: MHHWS_MHHW_gauges.kmz",
                     "@type": "dcat:Distribution",
+                    "description": "Coastal Wetland Elevation and Carbon Flux Inventory with Uncertainty, USA, 2006-2011: MHHWS_MHHW_gauges.kmz",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/cms/Uncertainty_US_Coastal_GHG/comp/MHHWS_MHHW_gauges.kmz",
+                    "mediaType": "application/vnd.google-earth.kmz",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/vnd.google-earth.kmz",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/cms/Uncertainty_US_Coastal_GHG/comp/MHHW_NAVD88_gauges.kmz",
-                    "description": "Coastal Wetland Elevation and Carbon Flux Inventory with Uncertainty, USA, 2006-2011: MHHW_NAVD88_gauges.kmz",
                     "@type": "dcat:Distribution",
+                    "description": "Coastal Wetland Elevation and Carbon Flux Inventory with Uncertainty, USA, 2006-2011: MHHW_NAVD88_gauges.kmz",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/cms/Uncertainty_US_Coastal_GHG/comp/MHHW_NAVD88_gauges.kmz",
+                    "mediaType": "application/vnd.google-earth.kmz",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/cms/Uncertainty_US_Coastal_GHG/comp/Uncertainty_US_Coastal_GHG.pdf",
-                    "description": "CMS: Coastal Wetland Greenhouse Gas Inventory Uncertainty, Conterminous US, 2006-2011: Uncertainty_US_Coastal_GHG.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "CMS: Coastal Wetland Greenhouse Gas Inventory Uncertainty, Conterminous US, 2006-2011: Uncertainty_US_Coastal_GHG.pdf",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/cms/Uncertainty_US_Coastal_GHG/comp/Uncertainty_US_Coastal_GHG.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://daac.ornl.gov/CMS/guides/Uncertainty_US_Coastal_GHG_Fig1.jpg",
-                    "description": "Estimated CO2e fluxes and confidence interval ranges for the Mississippi River outlet in Louisiana, United States. This area contains palustrine and estuarine wetlands, and includes stable wetlands, wetland gains and loss events from 2006 to 2011. A: Total flux from 2006 to 2011. B. Uncertainty, as represented by confidence interval range (0.975 - 0.025 quantile distributions of the results of the Monte Carlo Analysis). C-E. The relative contributions of soil, biomass, and methane to the total flux (A).",
                     "@type": "dcat:Distribution",
+                    "description": "Estimated CO2e fluxes and confidence interval ranges for the Mississippi River outlet in Louisiana, United States. This area contains palustrine and estuarine wetlands, and includes stable wetlands, wetland gains and loss events from 2006 to 2011. A: Total flux from 2006 to 2011. B. Uncertainty, as represented by confidence interval range (0.975 - 0.025 quantile distributions of the results of the Monte Carlo Analysis). C-E. The relative contributions of soil, biomass, and methane to the total flux (A).",
+                    "downloadURL": "https://daac.ornl.gov/CMS/guides/Uncertainty_US_Coastal_GHG_Fig1.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 }
             ],
+            "graphic-preview-description": "Estimated CO2e fluxes and confidence interval ranges for the Mississippi River outlet in Louisiana, United States. This area contains palustrine and estuarine wetlands, and includes stable wetlands, wetland gains and loss events from 2006 to 2011. A: Total flux from 2006 to 2011. B. Uncertainty, as represented by confidence interval range (0.975 - 0.025 quantile distributions of the results of the Monte Carlo Analysis). C-E. The relative contributions of soil, biomass, and methane to the total flux (A).",
+            "graphic-preview-file": "https://daac.ornl.gov/CMS/guides/Uncertainty_US_Coastal_GHG_Fig1.jpg",
+            "identifier": "C2389101052-ORNL_CLOUD",
+            "issued": "2019-12-17",
+            "keyword": [
+                "carbon flux",
+                "climate indicators",
+                "ecosystems",
+                "biosphere",
+                "soils",
+                "vegetation",
+                "geomorphic landforms/processes",
+                "earth science",
+                "land surface"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1650",
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
             "spatial": "-135.03 20.38 -56.66 48.99",
+            "temporal": "2006-01-01T00:00:00Z/2011-12-31T23:59:59Z",
             "theme": [
                 "CMS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Coastal Wetland Elevation and Carbon Flux Inventory with Uncertainty, USA, 2006-2011"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/MET10/CERES/GEO_ED4_NH_V01.2",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2018-07-19. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/MET10/CERES/GEO_ED4_NH_V01.2. https://doi.org/10.5067/MET10/CERES/GEO_ED4_NH_V01.2.",
-            "issued": "2018-05-22",
-            "temporal": "2015-07-31T00:00:00Z/2024-03-27T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2018-07-19",
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
-            "identifier": "C1588128371-LARC_ASDC",
             "description": "CER_GEO_Ed4_MET10_NH_V01.2 is the Satellite Cloud and Radiation Property retrieval System (SatCORPS) Clouds and the Earth's Radiant Energy System (CERES) Geostationary Satellite (GEO) Edition 4 Meteosat-10 over the Northern Hemisphere (NH) Version 1.2 data product. Data was collected using the Spinning Enhanced Visible and Infrared Imager (SEVIRI) Instrument on the Meteosat-10 platform. \r\n\r\nNote: Version 1.2 is identical to version 1.0. No changes have been made to the retrieval algorithm.\r\n\r\nThis data set comprises cloud micro-physical and radiation properties derived hourly from Meteosat-1 geostationary satellite imager data using the Langley Research Center (LaRC) SATCORPS algorithms supporting the CERES project. Each active geostationary satellite's cloud microphysical and radiation properties are merged to create hourly global cloud properties that estimate fluxes between CERES instrument measurements to account for the changing diurnal cycle. The data set is arranged as files for each hour and in netCDF-4 format. The observations are at 4 km resolution (at nadir) and are sub-sampled to 8 km.\r\n\r\nCERES is a key Earth Observing System (EOS) program component. The CERES instruments provide radiometric measurements of the Earth's atmosphere from three broadband channels. The CERES missions follow the successful Earth Radiation Budget Experiment (ERBE) mission. The first CERES instrument, the proto flight model (PFM), was launched on November 27, 1997, as part of the Tropical Rainfall Measuring Mission (TRMM). Two CERES instruments (FM1 and FM2) were launched into polar orbit onboard the Earth Observing System (EOS) flagship Terra on December 18, 1999. Two additional CERES instruments (FM3 and FM4) were launched onboard Earth Observing System (EOS) Aqua on May 4, 2002. The CERES FM5 instrument was launched onboard the Suomi National Polar-orbiting Partnership (NPP) satellite on October 28, 2011. The newest CERES instrument (FM6) was launched onboard the Joint Polar-Orbiting Satellite System 1 (JPSS-1) satellite, now called NOAA-20, on November 18, 2017.",
-            "graphic-preview-description": "Mission Logo",
-            "title": "SatCORPS CERES GEO Edition 4 Meteosat-10 Northern Hemisphere Version 1.2",
-            "graphic-preview-file": "https://asdc.larc.nasa.gov/static/images/project_logos/ceres.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMET10%2FCERES%2FGEO_ED4_NH_V01.2",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMET10%2FCERES%2FGEO_ED4_NH_V01.2",
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
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1588128371-LARC_ASDC",
-                    "description": "Earthdata Search for CER_GEO_Ed4_MET10_NH_V01.2 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for CER_GEO_Ed4_MET10_NH_V01.2 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1588128371-LARC_ASDC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/MET10/CERES/GEO_ED4_NH_V01.2",
-                    "description": "DOI data set landing page for CER_GEO_Ed4_MET10_NH_V01.2",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for CER_GEO_Ed4_MET10_NH_V01.2",
+                    "downloadURL": "https://doi.org/10.5067/MET10/CERES/GEO_ED4_NH_V01.2",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
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
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/CERES/GEO/Edition4/MET10_NH_V01.2/",
-                    "description": "ASDC Direct Data Download for CER_GEO_Ed4_MET10_NH_V01.2",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for CER_GEO_Ed4_MET10_NH_V01.2",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/CERES/GEO/Edition4/MET10_NH_V01.2/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/CERES/GEO/Edition4/MET10_NH_V01.2/contents.html",
-                    "description": "OPeNDAP data access for CER_GEO_Ed4_MET10_NH_V01.2",
                     "@type": "dcat:Distribution",
+                    "description": "OPeNDAP data access for CER_GEO_Ed4_MET10_NH_V01.2",
+                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/CERES/GEO/Edition4/MET10_NH_V01.2/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 }
             ],
+            "graphic-preview-description": "Mission Logo",
+            "graphic-preview-file": "https://asdc.larc.nasa.gov/static/images/project_logos/ceres.png",
+            "identifier": "C1588128371-LARC_ASDC",
+            "issued": "2018-05-22",
+            "keyword": [
+                "clouds",
+                "earth science",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.5067/MET10/CERES/GEO_ED4_NH_V01.2",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2018-07-19",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/LARC/SD/ASDC"
+            },
             "spatial": "<?xml version=\"1.0\" encoding=\"UTF-8\"?><gml:Polygon xmlns:gml=\"http://www.opengis.net/gml/3.2\" srsName=\"EPSG:9825\"><gml:outerBoundaryIs><gml:LinearRing><gml:posList>0.0 -50.0 0.0 60.0 60.0 60.0 60.0 -50.0 0.0 -50.0</gml:posList></gml:LinearRing></gml:outerBoundaryIs><gml:innerBoundaryIs></gml:innerBoundaryIs></gml:Polygon>",
+            "temporal": "2015-07-31T00:00:00Z/2024-03-27T00:00:00Z",
             "theme": [
                 "CERES",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "SatCORPS CERES GEO Edition 4 Meteosat-10 Northern Hemisphere Version 1.2"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RL-CAL-ROMAP-3-CR4B-SPM-V1.0",
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
+            "description": "This archive contains level 3 data from the ROMAP SPM instrument onboard ROSETTA Lander, acquired during the CR4B (cruise 4B) phase. It also contains documentation which describes the ROMAP experiment. The data archived in this data set conform to the Planetary Data System (PDS) Standards, Version 3.6.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.rl-cal-romap-3-cr4b-spm-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "calibration"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RL-CAL-ROMAP-3-CR4B-SPM-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.rl-cal-romap-3-cr4b-spm-v1.0",
-            "description": "This archive contains level 3 data from the ROMAP SPM instrument onboard ROSETTA Lander, acquired during the CR4B (cruise 4B) phase. It also contains documentation which describes the ROMAP experiment. The data archived in this data set conform to the Planetary Data System (PDS) Standards, Version 3.6.",
-            "title": "ROSETTA-LANDER CAL ROMAP 3 CR4B SPM V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-LANDER CAL ROMAP 3 CR4B SPM V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://nasa3d.arc.nasa.gov/detail/sat-kit-1000",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2018-06-25",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
-            "references": [
-                "http://www.nasa.gov/mission_pages/shuttle/main/index.html"
-            ],
-            "keyword": [
-                "spacecraft",
-                "satellite",
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
-            "identifier": "NASA-396",
             "description": "A collection of interchangeable satellite parts: bodies, radios, and solar panels.",
-            "title": "NASA 3D Models: Satellite Kit",
-            "programCode": [
-                "026:045",
-                "026:046"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -1572674,311 +1572653,334 @@
                     "mediaType": "application/octet-stream"
                 }
             ],
-            "accrualPeriodicity": "irregular",
+            "identifier": "NASA-396",
+            "issued": "2018-06-25",
+            "keyword": [
+                "spacecraft",
+                "satellite",
+                "3d model"
+            ],
+            "landingPage": "http://nasa3d.arc.nasa.gov/detail/sat-kit-1000",
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
+                "http://www.nasa.gov/mission_pages/shuttle/main/index.html"
+            ],
             "theme": [
                 "Management/Operations"
-            ]
+            ],
+            "title": "NASA 3D Models: Satellite Kit"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MEX-M-ASPERA3-2-EDR-IMA-V1.0",
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
+            "description": "This data set contains Mars Express ASPERA-3 Ion Mass Analyzer (IMA) data from launch (June 2, 2003) to the end of nominal mission (through December 2005). These data are provided in raw units of counts/accumulation.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mex-m-aspera3-2-edr-ima-v1.0_wg9m-r2p7",
+            "issued": "2021-05-21",
+            "keyword": [
+                "mars express",
+                "mars"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MEX-M-ASPERA3-2-EDR-IMA-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mex-m-aspera3-2-edr-ima-v1.0_wg9m-r2p7",
-            "description": "This data set contains Mars Express ASPERA-3 Ion Mass Analyzer (IMA) data from launch (June 2, 2003) to the end of nominal mission (through December 2005). These data are provided in raw units of counts/accumulation.",
-            "title": "MARS EXPRESS ASPERA-3 RAW EDR ION MASS ANALYZER V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "MARS EXPRESS ASPERA-3 RAW EDR ION MASS ANALYZER V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-2-PRL-67PCHURYUMOV-M01-V1.1",
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
+            "description": "This data set contains raw EDR images acquired by the OSIRIS Wide Angle\nCamera during the prelanding phase of the Rosetta mission at the comet 67P,\ncovering the period from 2014-03-18 to 2014-04-06.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-2-prl-67pchuryumov-m01-v1.1_wgac-dvve",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-2-PRL-67PCHURYUMOV-M01-V1.1",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-2-prl-67pchuryumov-m01-v1.1_wgac-dvve",
-            "description": "This data set contains raw EDR images acquired by the OSIRIS Wide Angle\nCamera during the prelanding phase of the Rosetta mission at the comet 67P,\ncovering the period from 2014-03-18 to 2014-04-06.",
-            "title": "ROSETTA-ORBITER COMET PRELANDING OSIWAC 2 EDR DATA MTP 001",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER COMET PRELANDING OSIWAC 2 EDR DATA MTP 001"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://techport.nasa.gov/view/10892",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2011-10-01",
-            "temporal": "2011-10-01T00:00:00Z/2013-09-01T00:00:00Z",
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
-                "wallops flight facility",
-                "project",
-                "active"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Mark Conde",
                 "hasEmail": "mailto:mark.conde@gi.alaska.edu"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Science Mission Directorate"
-            },
-            "identifier": "TECHPORT_10892",
             "description": "&lt;p&gt;\r\n\tThe methodology developed under this grant is primarily an effort to develop new sub-payload technologies and an inexpensive method of testing them. The three technical goals are: (1) to improve and test the existing spring sub-payload ejection system and rocket propelled ejection system, (2) to test the performance of ampule-deployed radar chaff (rather than TMA) to track high altitude winds, and (3) to develop and test sensor and telemetry packages to monitor the attitude stability and position of deployed sub-payloads.&amp;nbsp; The proposed effort will also demonstrate very low cost, low altitude rockets as an inexpensive flight test of payloads prior to expensive sounding rocket deployments. The payloads tested on 5 to 7 low-cost rockets will be (1) foil chaff designed for radar tracking of mesospheric winds, (2) plasma instruments composed of GPS monitors, magnetometers, and accelerometers, and (3) android phones for the investigation of off-the-shell instrumentation and telemetry.&amp;nbsp; Finally, a campaign of 2 to 4 sounding rocket deployments on &amp;lsquo;as-available&amp;rsquo; flights from Poker Flats will be used to test spring ejection without spin up, spring ejection with spin up for sub-payload attitude control, and rocket ejection&lt;/p&gt;",
-            "title": "Sounding rocket payload systems for in-situ measurements of ionosphere-thermosphere structure at small spatial scales Project",
-            "programCode": [
-                "026:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "http://techport.nasa.gov/xml-api/10892",
                     "mediaType": "application/xml"
                 }
-            ]
+            ],
+            "identifier": "TECHPORT_10892",
+            "issued": "2011-10-01",
+            "keyword": [
+                "wallops flight facility",
+                "project",
+                "active"
+            ],
+            "landingPage": "http://techport.nasa.gov/view/10892",
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
+            "temporal": "2011-10-01T00:00:00Z/2013-09-01T00:00:00Z",
+            "title": "Sounding rocket payload systems for in-situ measurements of ionosphere-thermosphere structure at small spatial scales Project"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG1%2FVG2-SR%2FUR-RSS-4-OCC-V1.0",
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
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg1-vg2-sr-ur-rss-4-occ-v1.0_wgah-5iu7",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "s rings",
                 "voyager",
                 "u rings"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG1%2FVG2-SR%2FUR-RSS-4-OCC-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg1-vg2-sr-ur-rss-4-occ-v1.0_wgah-5iu7",
-            "description": "not applicable",
-            "title": "VG1/VG2 SR/UR RSS RESAMPLED RING OCCULTATION V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "VG1/VG2 SR/UR RSS RESAMPLED RING OCCULTATION V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewBundle.jsp?identifier=urn%3Anasa%3Apds%3Aa15_17_hfe_concatenated&version=1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This bundle contains ASCII tables containing corrected, reduced, and concatenated versions of all available calibrated data from the Apollo 15 and 17 Heat Flow Experiment, along with supporting documentation and source data. These tables are based on other data in the PDS and the published literature, specifically (1) transcriptions of data sent by the original instrument team to the NSSDC and (2) data not archived by the instrument team and recovered much later from ARCSAV tapes. The data here correct several errors in (1), and furthermore place (1) and (2) into a standardized format for ease of use.",
+            "identifier": "urn:nasa:pds:a15_17_hfe_concatenated",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2021-05-21",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "moon",
                 "apollo 15",
                 "apollo 17"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewBundle.jsp?identifier=urn%3Anasa%3Apds%3Aa15_17_hfe_concatenated&version=1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:a15_17_hfe_concatenated",
-            "description": "This bundle contains ASCII tables containing corrected, reduced, and concatenated versions of all available calibrated data from the Apollo 15 and 17 Heat Flow Experiment, along with supporting documentation and source data. These tables are based on other data in the PDS and the published literature, specifically (1) transcriptions of data sent by the original instrument team to the NSSDC and (2) data not archived by the instrument team and recovered much later from ARCSAV tapes. The data here correct several errors in (1), and furthermore place (1) and (2) into a standardized format for ease of use.",
-            "title": "Apollo 15 and 17 Heat Flow Experiment Concatenated Data Sets Bundle",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "Apollo 15 and 17 Heat Flow Experiment Concatenated Data Sets Bundle"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/2064",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Hook, S.J., J.S. Myers, K.J. Thome, M. Fitzgerald, A.B. Kahle,  Airborne Sensor Facility NASA Ames Research Center, and T.H. Mace. 2022. MASTER: Airborne Science, Southwestern US, September, 2002. ORNL DAAC, Oak Ridge, Tennessee, USA. https://doi.org/10.3334/ORNLDAAC/2064",
-            "issued": "2023-07-09",
-            "temporal": "2002-09-10T21:18:37Z/2002-09-26T19:15:38Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-13",
-            "keyword": [
-                "land surface",
-                "visible wavelengths",
-                "surface thermal properties",
-                "surface radiative properties",
-                "spectral/engineering",
-                "infrared wavelengths",
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
-            "identifier": "C2731761299-ORNL_CLOUD",
             "description": "This dataset includes Level 1B (L1B) and Level 2 (L2) data products from the MODIS/ASTER Airborne Simulator (MASTER) instrument. The spectral data were collected during 11 flights aboard a NASA ER-2 aircraft over southwestern U.S. from 2002-09-10 to 2002-09-26. This deployment was coordinated by NASA's Dryden Flight Research Center (DRFC), renamed Armstrong Flight Research Center in 2014, located in Edwards, California. Data products include L1B georeferenced multispectral imagery of calibrated radiance in 50 bands covering wavelengths of 0.460 to 12.879 micrometers at approximately 50-meter spatial resolution. Derived L2 data products are emissivity in 5 bands in thermal infrared range (8.58 to 12.13 micrometers) and land surface temperature. The L1B file format is HDF-4, and L2 products are provided in ENVI and KMZ formats. In addition, the dataset includes flight paths, spectral band information, instrument configuration, ancillary notes, and summary information for each flight, and browse images derived from each L1B data file.",
-            "graphic-preview-description": "Single-band images and a RGB composite image from flight track 4 as acquired on 10 September 2002 over Mono Lake, California, U.S. Source: MASTERL1B_0297100_04_20020910_2151_2157_V01.jpg",
-            "title": "MASTER: Airborne Science, Southwestern US, September, 2002",
-            "graphic-preview-file": "https://daac.ornl.gov/MASTER/guides/MASTER_DFRC_September_2002_Fig1.jpg",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F2064",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F2064",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/master/MASTER_DFRC_September_2002/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/master/MASTER_DFRC_September_2002/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/MASTER/guides/MASTER_DFRC_September_2002.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/MASTER/guides/MASTER_DFRC_September_2002.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/2064",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/2064",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/master/MASTER_DFRC_September_2002/comp/MASTER_DFRC_September_2002.pdf",
-                    "description": "MASTER: Airborne Science, Southwestern US, September, 2002: MASTER_DFRC_September_2002.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "MASTER: Airborne Science, Southwestern US, September, 2002: MASTER_DFRC_September_2002.pdf",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/master/MASTER_DFRC_September_2002/comp/MASTER_DFRC_September_2002.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://daac.ornl.gov/MASTER/guides/MASTER_DFRC_September_2002_Fig1.jpg",
-                    "description": "Single-band images and a RGB composite image from flight track 4 as acquired on 10 September 2002 over Mono Lake, California, U.S. Source: MASTERL1B_0297100_04_20020910_2151_2157_V01.jpg",
                     "@type": "dcat:Distribution",
+                    "description": "Single-band images and a RGB composite image from flight track 4 as acquired on 10 September 2002 over Mono Lake, California, U.S. Source: MASTERL1B_0297100_04_20020910_2151_2157_V01.jpg",
+                    "downloadURL": "https://daac.ornl.gov/MASTER/guides/MASTER_DFRC_September_2002_Fig1.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 }
             ],
+            "graphic-preview-description": "Single-band images and a RGB composite image from flight track 4 as acquired on 10 September 2002 over Mono Lake, California, U.S. Source: MASTERL1B_0297100_04_20020910_2151_2157_V01.jpg",
+            "graphic-preview-file": "https://daac.ornl.gov/MASTER/guides/MASTER_DFRC_September_2002_Fig1.jpg",
+            "identifier": "C2731761299-ORNL_CLOUD",
+            "issued": "2023-07-09",
+            "keyword": [
+                "land surface",
+                "visible wavelengths",
+                "surface thermal properties",
+                "surface radiative properties",
+                "spectral/engineering",
+                "infrared wavelengths",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/2064",
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
             "spatial": "-123.75 28.97 -95.85 40.98",
+            "temporal": "2002-09-10T21:18:37Z/2002-09-26T19:15:38Z",
             "theme": [
                 "MASTER",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "MASTER: Airborne Science, Southwestern US, September, 2002"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-2-PRL-67PCHURYUMOV-M03-V2.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This data set contains images acquired by the OSIRIS Wide Angle Camera during the PRELANDING phase of the Rosetta mission at the comet 67P, covering the period from 2014-05-07T12:48:00.000 to 2014-06-04T10:49:59.000. This version V2.0 supersedes previous deliveries of the same dataset.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-2-prl-67pchuryumov-m03-v2.0",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2021-05-21",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "dark",
                 "zeta cas",
@@ -1572989,68 +1572991,67 @@
                 "67p/churyumov-gerasimenko 1 (1969 r1)",
                 "16 cyg b"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-2-PRL-67PCHURYUMOV-M03-V2.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-2-prl-67pchuryumov-m03-v2.0",
-            "description": "This data set contains images acquired by the OSIRIS Wide Angle Camera during the PRELANDING phase of the Rosetta mission at the comet 67P, covering the period from 2014-05-07T12:48:00.000 to 2014-06-04T10:49:59.000. This version V2.0 supersedes previous deliveries of the same dataset.",
-            "title": "ROSETTA-ORBITER PRELANDING OSIWAC 2 EDR MTP003 V2.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER PRELANDING OSIWAC 2 EDR MTP003 V2.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1214353754-ASF.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, ASF.",
-            "issued": "2014-02-21",
-            "temporal": "2008-07-24T21:06:27Z/2024-11-11T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-07",
-            "keyword": [
-                "earth science",
-                "solid earth",
-                "tectonics"
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
-            "identifier": "C1214353754-ASF",
             "description": "UAVSAR PolSAR Scene Incidence Angle",
-            "title": "UAVSAR_POLSAR_INCIDENCE",
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
+            "identifier": "C1214353754-ASF",
+            "issued": "2014-02-21",
+            "keyword": [
+                "earth science",
+                "solid earth",
+                "tectonics"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1214353754-ASF.html",
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
@@ -1573516,642 +1573517,650 @@
                 "Peace River and I17 Corridor, FL",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "UAVSAR_POLSAR_INCIDENCE"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/IS-40e/TEMPO/IRR_L1.003",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/IS-40e/TEMPO/IRR_L1.003.",
-            "issued": "2024-04-03",
-            "temporal": "2023-08-01T00:00:00Z/2025-01-13T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-09",
-            "keyword": [
-                "atmosphere",
-                "earth science",
-                "atmospheric radiation"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Raid Suleiman",
                 "hasEmail": "mailto:rsuleiman@cfa.harvard.edu"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/LARC/SD/ASDC"
-            },
-            "identifier": "C2930757598-LARC_CLOUD",
             "description": "Level 1 irradiance files provide solar irradiance measured using the working solar diffuser. Each file includes the measured solar irradiance for all the North-South cross-track pixels. The files are provided in netCDF4 format, and contain information on radiometrically and wavelength calibrated solar irradiance for the UV and visible bands, corresponding noise, parameterized wavelength grid, solar viewing geometry, quality flags and other ancillary information. The product is produced using the L0-1b processor which includes multiple steps: (1) Image processing to produce radiometrically calibrated radiance, and (2) Additional wavelength calibration to improve wavelength registration. These data reached provisional validation on December 9, 2024.",
-            "graphic-preview-description": "TEMPO Logo",
-            "title": "TEMPO solar irradiance V03 (PROVISIONAL)",
-            "graphic-preview-file": "https://asdc.larc.nasa.gov/static/images/project_logos/tempo.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FIS-40e%2FTEMPO%2FIRR_L1.003",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FIS-40e%2FTEMPO%2FIRR_L1.003",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://tempo.si.edu",
-                    "description": "TEMPO project page",
                     "@type": "dcat:Distribution",
+                    "description": "TEMPO project page",
+                    "downloadURL": "http://tempo.si.edu",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/IS-40e/TEMPO/IRR_L1.003",
-                    "description": "DOI data set landing page for TEMPO_IRR_L1_V03",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for TEMPO_IRR_L1_V03",
+                    "downloadURL": "https://doi.org/10.5067/IS-40e/TEMPO/IRR_L1.003",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://asdc.larc.nasa.gov/static/images/project_logos/tempo.png",
-                    "description": "TEMPO Logo",
                     "@type": "dcat:Distribution",
+                    "description": "TEMPO Logo",
+                    "downloadURL": "https://asdc.larc.nasa.gov/static/images/project_logos/tempo.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization through WORLDVIEW"
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
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2930757598-LARC_CLOUD",
-                    "description": "Earthdata Search for TEMPO_IRR_L1_V03 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for TEMPO_IRR_L1_V03 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2930757598-LARC_CLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/project/TEMPO",
-                    "description": "ASDC Data and Information for TEMPO",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Data and Information for TEMPO",
+                    "downloadURL": "https://asdc.larc.nasa.gov/project/TEMPO",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/tempo/guide/TEMPO_Level-1_user_guide_V1.2_20241204.pdf",
-                    "description": "Tropospheric Emissions: Monitoring Pollution (TEMPO) Project Level 1 Data Products: User Guide",
                     "@type": "dcat:Distribution",
+                    "description": "Tropospheric Emissions: Monitoring Pollution (TEMPO) Project Level 1 Data Products: User Guide",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/tempo/guide/TEMPO_Level-1_user_guide_V1.2_20241204.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
                 }
             ],
+            "graphic-preview-description": "TEMPO Logo",
+            "graphic-preview-file": "https://asdc.larc.nasa.gov/static/images/project_logos/tempo.png",
+            "identifier": "C2930757598-LARC_CLOUD",
+            "issued": "2024-04-03",
+            "keyword": [
+                "atmosphere",
+                "earth science",
+                "atmospheric radiation"
+            ],
+            "landingPage": "https://doi.org/10.5067/IS-40e/TEMPO/IRR_L1.003",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2025-01-09",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/LARC/SD/ASDC"
+            },
             "spatial": "<?xml version=\"1.0\" encoding=\"UTF-8\"?><gml:Polygon xmlns:gml=\"http://www.opengis.net/gml/3.2\" srsName=\"EPSG:9825\"><gml:outerBoundaryIs><gml:LinearRing><gml:posList>10.0 -170.0 10.0 -10.0 80.0 -10.0 80.0 -170.0 10.0 -170.0</gml:posList></gml:LinearRing></gml:outerBoundaryIs><gml:innerBoundaryIs></gml:innerBoundaryIs></gml:Polygon>",
+            "temporal": "2023-08-01T00:00:00Z/2025-01-13T00:00:00Z",
             "theme": [
                 "TEMPO",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "TEMPO solar irradiance V03 (PROVISIONAL)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-C-CFCCD-5-RDR-CTIO-BORR-PHOTOM-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This data set contains images of the Deep Space 1 target, comet 19P/Borrelly, and derived photometry from five consecutive nights of observing over 28 July - 1 August 2000. The observations were made using the 1.5m telescope of the Cerro Tololo Interamerican Observatory using the CFCCD camera mounted at the f/7.5 focus. The detector used was a Tek2K, yielding a plate scale of 0.4334 arcseconds/pixel. The photometric and lightcurve results were presented in Mueller and Samarasinha (2002).",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-c-cfccd-5-rdr-ctio-borr-photom-v1.0_wgmf-7e4b",
             "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "support archives",
                 "19p/borrelly 1 (1904 y2)",
                 "calibration field"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-C-CFCCD-5-RDR-CTIO-BORR-PHOTOM-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-c-cfccd-5-rdr-ctio-borr-photom-v1.0_wgmf-7e4b",
-            "description": "This data set contains images of the Deep Space 1 target, comet 19P/Borrelly, and derived photometry from five consecutive nights of observing over 28 July - 1 August 2000. The observations were made using the 1.5m telescope of the Cerro Tololo Interamerican Observatory using the CFCCD camera mounted at the f/7.5 focus. The detector used was a Tek2K, yielding a plate scale of 0.4334 arcseconds/pixel. The photometric and lightcurve results were presented in Mueller and Samarasinha (2002).",
-            "title": "CTIO IMAGES OF 19P/BORRELLY WITH PHOTOMETRY",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "CTIO IMAGES OF 19P/BORRELLY WITH PHOTOMETRY"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG2-N-MAG-4-RDR-HGCOORDS-9.6SEC-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This data set includes data from the Low Field Magnetometer (LFM) during the inbound Neptune encounter beginning in the solar wind and continuing until the first magnetopause crossing. The magnetometer are given in Heliographic coordinates and the data have been averaged from the 1.92 second averages to a 9.6 second resampled rate. The dataset consists of the following columns: 1) ctime (decimal seconds since 1966-01-01T00:00:00.000), 2) pdstime (ISO standard time format), 3-5) spacecraft clock (m65536,m60,fds-line), 6) magnetometer id (1 = LFM, 2 = HFM), 7), Br (radial component), 8) Bt (tangential component), 9) Bn (normal component), 10) Bmag (magnitude of the average components), 11) avg_Bmag (average of the magnitude of the raw components), 12) Lambda (longitude = tan^-1(Bt/Br)), 13) Delta (latitude = sin^-1(Bn/avg_Bmag) ), 14-16) rms vector (pythagorean root mean square deviation of the component averages), 17) npts (number of points in average), 18) flag a character string which indicates software or s/c hardware intervention which reduces confidence in the data (NULL flags represent 'good' data).",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg2-n-mag-4-rdr-hgcoords-9.6sec-v1.0_wgqe-9b6q",
             "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "comet sl9/jupiter collision",
                 "voyager",
                 "neptune"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG2-N-MAG-4-RDR-HGCOORDS-9.6SEC-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg2-n-mag-4-rdr-hgcoords-9.6sec-v1.0_wgqe-9b6q",
-            "description": "This data set includes data from the Low Field Magnetometer (LFM) during the inbound Neptune encounter beginning in the solar wind and continuing until the first magnetopause crossing. The magnetometer are given in Heliographic coordinates and the data have been averaged from the 1.92 second averages to a 9.6 second resampled rate. The dataset consists of the following columns: 1) ctime (decimal seconds since 1966-01-01T00:00:00.000), 2) pdstime (ISO standard time format), 3-5) spacecraft clock (m65536,m60,fds-line), 6) magnetometer id (1 = LFM, 2 = HFM), 7), Br (radial component), 8) Bt (tangential component), 9) Bn (normal component), 10) Bmag (magnitude of the average components), 11) avg_Bmag (average of the magnitude of the raw components), 12) Lambda (longitude = tan^-1(Bt/Br)), 13) Delta (latitude = sin^-1(Bn/avg_Bmag) ), 14-16) rms vector (pythagorean root mean square deviation of the component averages), 17) npts (number of points in average), 18) flag a character string which indicates software or s/c hardware intervention which reduces confidence in the data (NULL flags represent 'good' data).",
-            "title": "VG2 NEP MAG RESAMP RDR HELIOGRAPHIC COORDINATES 9.6SEC V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "VG2 NEP MAG RESAMP RDR HELIOGRAPHIC COORDINATES 9.6SEC V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ASDC_DAAC/FIRE/0059",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "1999-11-15. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/ASDC_DAAC/FIRE/0059.",
-            "issued": "1999-11-02",
-            "temporal": "1992-05-29T00:00:00Z/1992-06-19T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2018-07-06",
-            "keyword": [
-                "ocean temperature",
-                "oceans",
-                "earth science"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "ALAIN WEILL",
                 "hasEmail": "mailto:alain.weill@cetp.ipsl.fr"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/LARC/SD/ASDC"
-            },
-            "identifier": "C1000001043-LARC_ASDC",
             "description": "The First ISCCP Regional Experiments have been designed to improve data products and cloud/radiation parameterizations used in general circulation models (GCMs). Specifically, the goals of FIRE are (1) to improve basic understanding of the interaction of physical processes in determining life cycles of cirrus and marine stratocumulus systems and the radiative properties of these clouds during their life cycles and (2) to investigate the interrelationships between the ISCCP data, GCM parameterizations, and higher space and time resolution cloud data.To-date, four intensive field-observation periods were planned and executed: a cirrus IFO (October 13-November 2, 1986); a marine stratocumulus IFO off the southwestern coast of California (June 29-July 20, 1987); a second cirrus IFO in southeastern Kansas (November 13-December 7, 1991); and a second marine stratocumulus IFO in the eastern North Atlantic Ocean (June 1-June 28, 1992). Each mission combined coordinated satellite, airborne, and surface observations with modeling studies to investigate the cloud properties and physical processes of the cloud systems.SOFIA (Surface of the Ocean, Fluxes and Interaction with the Atmosphere) is a research program carried out by French groups from the Centre de Recherches en Physique de l'Environnement (CRPE), Laboratoire l'Aerologie (LA)-Toulouse, Centre de Meteorologie Marine (CMM)-Brest, Institut Francais de Rechercher sur la Mer (IFREMER)-Brest, Service d'Aeronomie-Paris, and Laboratoire de Meteorologie Dynamique (LMD)-Palaiseau with cooperation from Centre National de Recherche Meteorologique (CNRM)-Toulouse.The scientific objective of SOFIA during ASTEX was the study of energy transfer (heat, humidity and momentum fluxes) between the sea surface and the atmospheric boundary layer at scales ranging from the local scale to the mesoscale (50 km). The general concept of the program was to develop a measurement strategy based on nested boxes in which instrumentation would be used to estimate and quantify fluxes. These instruments, from which flux estimates at different scales would be measured, were used in connection with satellite measurements to understand and, hence, to validate the satellite integration of fluxes, particularly in the presence of mesoscale oceanic andatmospheric structures responsible for spatial inhomogeneity of fluxes.The data provided were collected via a trailing thermistor with bucketmeasurements. The thermistor data have been calibrated but not quality controlled.",
-            "title": "First ISCCP Regional Experiment (FIRE) Atlantic Stratocumulus Transition Experiment (ASTEX) SOFIA Le Suroit Bucket Data",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC_DAAC%2FFIRE%2F0059",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC_DAAC%2FFIRE%2F0059",
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
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1000001043-LARC_ASDC",
-                    "description": "Earthdata Search for FIRE_AX_SOF_SUR_BUCK_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for FIRE_AX_SOF_SUR_BUCK_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1000001043-LARC_ASDC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/read_software/fax_sof_sur_buck_read.c",
-                    "description": "Read Software - How to use the Program for RD_AX_SURBUCK.c - Direct File Download (.c)",
                     "@type": "dcat:Distribution",
+                    "description": "Read Software - How to use the Program for RD_AX_SURBUCK.c - Direct File Download (.c)",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/read_software/fax_sof_sur_buck_read.c",
+                    "mediaType": "text/html",
                     "title": "View this dataset's science data product software documentation"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/read_software/fax_sof_sur_nav_dat_read.c",
-                    "description": "Readme to read the SOFIA-SUROIT_NAV FIRE_ASTEX_NAT data file - Direct File Download (.c)",
                     "@type": "dcat:Distribution",
+                    "description": "Readme to read the SOFIA-SUROIT_NAV FIRE_ASTEX_NAT data file - Direct File Download (.c)",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/read_software/fax_sof_sur_nav_dat_read.c",
+                    "mediaType": "text/html",
                     "title": "View this dataset's science data product software documentation"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/readme/readme_fire_ax_sof_sur_buck_info1",
-                    "description": "Note for FIRE_AX_SOF_SUR_BUCK",
                     "@type": "dcat:Distribution",
+                    "description": "Note for FIRE_AX_SOF_SUR_BUCK",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/readme/readme_fire_ax_sof_sur_buck_info1",
+                    "mediaType": "text/html",
                     "title": "View this dataset's documented anomalies"
                 },
                 {
-                    "mediaType": "application/postscript",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/readme/readme_fire_ax_sof_sur_buck.ps",
-                    "description": "FIRE ASTEX Readme - Direct File Download (.ps)",
                     "@type": "dcat:Distribution",
+                    "description": "FIRE ASTEX Readme - Direct File Download (.ps)",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/readme/readme_fire_ax_sof_sur_buck.ps",
+                    "mediaType": "application/postscript",
                     "title": "View this dataset's read me document"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/ASDC_DAAC/FIRE/0059",
-                    "description": "DOI data set landing page for FIRE_AX_SOF_SUR_BUCK_1",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for FIRE_AX_SOF_SUR_BUCK_1",
+                    "downloadURL": "https://doi.org/10.5067/ASDC_DAAC/FIRE/0059",
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
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/guide/base_fire_ax_sofia_dataset.pdf",
-                    "description": "FIRE ASTEX Surface of the Ocean, Fluxes and Interaction with the Atmosphere (SOFIA) Langley DAAC Data Set Document",
                     "@type": "dcat:Distribution",
+                    "description": "FIRE ASTEX Surface of the Ocean, Fluxes and Interaction with the Atmosphere (SOFIA) Langley DAAC Data Set Document",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/guide/base_fire_ax_sofia_dataset.pdf",
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
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/FIRE/FIRE_AX_SOF_SUR_BUCK/",
-                    "description": "ASDC Direct Data Download for FIRE_AX_SOF_SUR_BUCK_1",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for FIRE_AX_SOF_SUR_BUCK_1",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/FIRE/FIRE_AX_SOF_SUR_BUCK/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/FIRE/FIRE_AX_SOF_SUR_BUCK/contents.html",
-                    "description": "OPeNDAP data access for FIRE_AX_SOF_SUR_BUCK_1",
                     "@type": "dcat:Distribution",
+                    "description": "OPeNDAP data access for FIRE_AX_SOF_SUR_BUCK_1",
+                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/FIRE/FIRE_AX_SOF_SUR_BUCK/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 }
             ],
+            "identifier": "C1000001043-LARC_ASDC",
+            "issued": "1999-11-02",
+            "keyword": [
+                "ocean temperature",
+                "oceans",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/ASDC_DAAC/FIRE/0059",
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
             "spatial": "<?xml version=\"1.0\" encoding=\"UTF-8\"?><gml:Polygon xmlns:gml=\"http://www.opengis.net/gml/3.2\" srsName=\"EPSG:4326\"><gml:outerBoundaryIs><gml:LinearRing><gml:posList>34.5 -26.8 34.5 -23.1 37.8 -23.1 37.8 -26.8 34.5 -26.8</gml:posList></gml:LinearRing></gml:outerBoundaryIs><gml:innerBoundaryIs></gml:innerBoundaryIs></gml:Polygon>",
+            "temporal": "1992-05-29T00:00:00Z/1992-06-19T23:59:59.999Z",
             "theme": [
                 "FIRE",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "First ISCCP Regional Experiment (FIRE) Atlantic Stratocumulus Transition Experiment (ASTEX) SOFIA Le Suroit Bucket Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/AURA/TES/TL2TNS_L2.007",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2017-03-07. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/AURA/TES/TL2TNS_L2.007. https://asdc.larc.nasa.gov/project/TES.",
-            "issued": "2015-08-27",
-            "temporal": "2004-09-13T00:00:00Z/2018-01-22T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2019-06-19",
-            "keyword": [
-                "earth science",
-                "atmospheric temperature",
-                "atmosphere"
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
-            "identifier": "C1331182617-LARC",
             "description": "TL2TNS_7 is the Tropospheric Emission Spectrometer (TES)/Aura Level 2 Atmospheric Temperatures Nadir Special Observation Version 7 data product. TES was an instrument aboard NASA's Aura satellite and was launched from California on July 15, 2004. Data collection for TES is complete. This product contains atmospheric vertical profile estimates and associated errors (diagonals and covariance matrices), along with retrieved surface temperature, cloud effective optical depth, column estimates, quality flags, averaging kernels and priori constraint vectors. TES Level 2 data contain retrieved species (or temperature) profiles at the observation targets and the estimated errors. The geolocation, quality, and other data (e.g., surface characteristics for nadir observations) were also provided. L2 modeled spectra were evaluated using radiative transfer modeling algorithms. The process, referred to as retrieval, compared observed spectra to the modeled spectra and iteratively updated the atmospheric parameters. L2 standard product files included information for one molecular species (or temperature) for an entire global survey or special observation run. A global survey consisted of a maximum of 16 consecutive orbits.\r\rNadir observations, which point directly to the surface of the Earth, are different from limb observations, which are pointed at various off-nadir angles into the atmosphere. Nadir and limb observations were added to separate L2 files, and a single ancillary file was composed of data that are common to both nadir and limb files. A Nadir sequence within the TES Global Survey was a fixed number of observations within an orbit for a Global Survey. Prior to April 24, 2005, it consisted of two low resolution scans over the same ground locations. After April 24, 2005, Global Survey data consisted of three low resolution scans. The Nadir standard product consists of four files, where each file is composed of the Global Survey Nadir observations from one of four focal planes for a single orbit, i.e. 72 orbit sequences. The Global Survey Nadir observations only used a single set of filter mix. \r\rA Global Survey consisted of observations along 16 consecutive orbits at the start of a two day cycle, over which 3,200 retrievals were performed. Each observation was the input for retrievals of species Volume Mixing Ratios (VMRs), temperature profiles, surface temperature, and other data parameters with associated pressure levels, precision, total error, vertical resolution, total column density, and other diagnostic quantities. Each TES Level 2 standard product reported information in a swath format conforming to the HDF-EOS Aura File Format Guidelines. Each Swath object was bounded by the number of observations in a global survey and a predefined set of pressure levels, representing slices through the atmosphere. Each standard product could have had a variable number of observations depending upon the Global Survey configuration and whether averaging was employed. Also, missing or bad retrievals were not reported. Further, observations were occasionally scheduled on non-global survey days. In general they were measurements made for validation purposes or with highly focused science objectives. Those non-global survey measurements were referred to as \u201cspecial observations\u201d\r\rThe organization of data within the Swath object was based on a superset of the Upper Atmosphere Research Satellite (UARS) pressure levels used to report concentrations of trace atmospheric gases. The reporting grid was the same pressure grid used for modeling. There were 67 reporting levels from 1211.53 hPa, which allowed for very high surface pressure conditions, to 0.1 hPa, about 65 km. In addition, the products reported values directly at the surface when possible or at the observed cloud top level. Thus in the Standard Product files, each observation could potentially contain estimates for the concentration of a particular molecule at 67 different pressure level",
-            "title": "TES/Aura L2 Atmospheric Temperatures Nadir Special Observation V007",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAURA%2FTES%2FTL2TNS_L2.007",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAURA%2FTES%2FTL2TNS_L2.007",
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
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1331182617-LARC",
-                    "description": "Earthdata Search for TL2TNS_7 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for TL2TNS_7 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1331182617-LARC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/AURA/TES/TL2TNS_L2.007",
-                    "description": "DOI data set landing page for TL2TNS_7",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for TL2TNS_7",
+                    "downloadURL": "https://doi.org/10.5067/AURA/TES/TL2TNS_L2.007",
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
-                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/TES/TL2TNS.007/contents.html",
-                    "description": "OPeNDAP data access for TL2TNS_7",
                     "@type": "dcat:Distribution",
+                    "description": "OPeNDAP data access for TL2TNS_7",
+                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/TES/TL2TNS.007/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/TES/TL2TNS.007/",
-                    "description": "ASDC Direct Data Download for TL2TNS_7",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for TL2TNS_7",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/TES/TL2TNS.007/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
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
+            "identifier": "C1331182617-LARC",
+            "issued": "2015-08-27",
+            "keyword": [
+                "earth science",
+                "atmospheric temperature",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.5067/AURA/TES/TL2TNS_L2.007",
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
+            "title": "TES/Aura L2 Atmospheric Temperatures Nadir Special Observation V007"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/ITM51B0FIBDV",
             "citation": "Kevin W. Bowman. 2022-04-04. TRPSYL2PANCRSFS. Version 1. TROPESS CrIS-SNPP L2 Peroxyacetyl Nitrate for Forward Stream, Summary Product V1. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/ITM51B0FIBDV. https://disc.gsfc.nasa.gov/datacollection/TRPSYL2PANCRSFS_1.html. Digital Science Data.",
-            "issued": "2022-04-01",
-            "temporal": "2021-02-01T00:00:00Z/2023-02-28T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-04-01",
-            "references": [
-                "https://doi.org/10.1126/sciadv.abf7460",
-                "https://doi.org/10.5194/amt-7-3737-2014",
-                "https://doi.org/10.1109/TGRS.2006.871234",
-                "https://doi.org/10.1029/2002JD002299"
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
-            "identifier": "C2247040984-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "The TROPESS CrIS-SNPP L2 Peroxyacetyl Nitrate for Forward Stream, Summary Product contains the vertical distribution of the retrieved atmospheric state of peroxyacetyl nitrate (PAN),  and formal uncertainties measured by the CrIS instrument on the Suomi-NPP satellite. The forward stream standard product is global for the time period from 2021-02-01 to 2021-05-21, when the CrIS-SNPP processing was discontinued. The NASA TRopospheric Ozone and Precursors from Earth System Sounding (TROPESS) project, uses an optimal estimation algorithm, known as the MUlti-SpEctra, MUlti-SpEcies, Multi-SEnsors (MUSES).\n\nThe data files are written in the netCDF version 4 file format, and each file contains one day of data. The data have a spatial resolution of 14 km (CrIS nadir FOV), and are reported at 16 vertical levels from the surface to 0.1 hPa. The principal investigator for the TROPESS project is Kevin W. Bowman.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "TRPSYL2PANCRSFS",
-            "creator": "Kevin W. Bowman",
-            "graphic-preview-description": "TROPESS CrIS-SNPP PAN (Forward Stream, Summary Product) at 383 hPa on 01 April 2021.",
-            "title": "TROPESS CrIS-SNPP L2 Peroxyacetyl Nitrate for Forward Stream, Summary Product V1 (TRPSYL2PANCRSFS) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TROPESS/images/TRPSYL2PANCRSFS_Sample.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FITM51B0FIBDV",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FITM51B0FIBDV",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TROPESS/images/TRPSYL2PANCRSFS_Sample.png",
-                    "description": "TROPESS CrIS-SNPP PAN (Forward Stream, Summary Product) at 383 hPa on 01 April 2021.",
                     "@type": "dcat:Distribution",
+                    "description": "TROPESS CrIS-SNPP PAN (Forward Stream, Summary Product) at 383 hPa on 01 April 2021.",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TROPESS/images/TRPSYL2PANCRSFS_Sample.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/TRPSYL2PANCRSFS_1.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/TRPSYL2PANCRSFS_1.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/data/TROPESS_Summary/TRPSYL2PANCRSFS.1/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/data/TROPESS_Summary/TRPSYL2PANCRSFS.1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=TRPSYL2PANCRSFS_1",
-                    "description": "Use the Earthdata Search Client to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search Client to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=TRPSYL2PANCRSFS_1",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/opendap/TROPESS_Summary/TRPSYL2PANCRSFS.1/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/opendap/TROPESS_Summary/TRPSYL2PANCRSFS.1/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/data/TROPESS_Summary/TRPSYL2PANCRSFS.1/doc/TROPESS_Forward_Stream_README.pdf",
-                    "description": "README Document",
                     "@type": "dcat:Distribution",
+                    "description": "README Document",
+                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/data/TROPESS_Summary/TRPSYL2PANCRSFS.1/doc/TROPESS_Forward_Stream_README.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's read me document"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TROPESS/User_Guides/TROPESS-PAN_L2_Product_Quick_Start_User_Guide_Summary_only.pdf",
-                    "description": "User's Guide",
                     "@type": "dcat:Distribution",
+                    "description": "User's Guide",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TROPESS/User_Guides/TROPESS-PAN_L2_Product_Quick_Start_User_Guide_Summary_only.pdf",
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
+            "graphic-preview-description": "TROPESS CrIS-SNPP PAN (Forward Stream, Summary Product) at 383 hPa on 01 April 2021.",
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TROPESS/images/TRPSYL2PANCRSFS_Sample.png",
+            "identifier": "C2247040984-GES_DISC",
+            "issued": "2022-04-01",
+            "keyword": [
+                "atmosphere",
+                "earth science",
+                "atmospheric chemistry"
+            ],
+            "landingPage": "https://doi.org/10.5067/ITM51B0FIBDV",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2022-04-01",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
+            },
+            "references": [
+                "https://doi.org/10.1126/sciadv.abf7460",
+                "https://doi.org/10.5194/amt-7-3737-2014",
+                "https://doi.org/10.1109/TGRS.2006.871234",
+                "https://doi.org/10.1029/2002JD002299"
+            ],
+            "release-place": "Greenbelt, MD, USA",
+            "series-name": "TRPSYL2PANCRSFS",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2021-02-01T00:00:00Z/2023-02-28T00:00:00Z",
             "theme": [
                 "TROPESS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "TROPESS CrIS-SNPP L2 Peroxyacetyl Nitrate for Forward Stream, Summary Product V1 (TRPSYL2PANCRSFS) at GES DISC"
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
+            "description": "Shock Wave / Turbulent Boundary Layer Flows at High Mach Numbers. This web page provides data from experiments that may be useful for the validation of turbulence models. This resource is expected to grow gradually over time. All data herein arepublicly available.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://www.cubrc.org/_iassets/docs/LENS2-hollowcylinderflare.xlsx",
+                    "mediaType": "application/xlsx"
+                }
             ],
+            "identifier": "NASA-850__4",
+            "issued": "2018-06-25",
             "keyword": [
                 "turbulence",
                 "shockwave",
@@ -1574162,891 +1574171,896 @@
                 "models",
                 "validation"
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
-            "identifier": "NASA-850__4",
-            "description": "Shock Wave / Turbulent Boundary Layer Flows at High Mach Numbers. This web page provides data from experiments that may be useful for the validation of turbulence models. This resource is expected to grow gradually over time. All data herein arepublicly available.",
-            "title": "Turbulence Models: Data from Other Experiments:  Shock Wave / Turbulent Boundary Layer Flows at High Mach Numbers",
-            "programCode": [
-                "026:023"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.cubrc.org/_iassets/docs/LENS2-hollowcylinderflare.xlsx",
-                    "mediaType": "application/xlsx"
-                }
+            "references": [
+                "http://turbmodels.larc.nasa.gov/index.html"
             ],
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Aerospace"
-            ]
+            ],
+            "title": "Turbulence Models: Data from Other Experiments:  Shock Wave / Turbulent Boundary Layer Flows at High Mach Numbers"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-5-DDR-ASTNAMES-DISCOVERY-V8.0",
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
+            "description": "This data set includes names, designations, and discovery circumstances for the asteroids numbered as of April 18, 2004.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-5-ddr-astnames-discovery-v8.0_wgu4-yq5u",
+            "issued": "2021-05-21",
+            "keyword": [
+                "asteroid",
+                "support archives"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-5-DDR-ASTNAMES-DISCOVERY-V8.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-5-ddr-astnames-discovery-v8.0_wgu4-yq5u",
-            "description": "This data set includes names, designations, and discovery circumstances for the asteroids numbered as of April 18, 2004.",
-            "title": "ASTEROID NAMES AND DISCOVERY V8.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ASTEROID NAMES AND DISCOVERY V8.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC1-0588-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 1 phase 2014-11-20 to 2015-03-10. It is a Global Gravity measurement at the comet 67P and covers the time 2015-02-18T10:53:00.000 to 2015-02-18T13:11:58.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc1-0588-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC1-0588-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc1-0588-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 1 phase 2014-11-20 to 2015-03-10. It is a Global Gravity measurement at the comet 67P and covers the time 2015-02-18T10:53:00.000 to 2015-02-18T13:11:58.000.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 1 0588 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 1 0588 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=CO-SSA-RADAR-3-ABDR-SUMMARY-V1.0",
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
+            "description": "N/A",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.co-ssa-radar-3-abdr-summary-v1.0_wgwv-g73p",
+            "issued": "2018-06-26",
+            "keyword": [
+                "titan",
+                "cassini-huygens"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=CO-SSA-RADAR-3-ABDR-SUMMARY-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.co-ssa-radar-3-abdr-summary-v1.0_wgwv-g73p",
-            "description": "N/A",
-            "title": "CASSINI ORBITER RADAR ALTIMETER BURST DATA RECORD SUMMARY",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "CASSINI ORBITER RADAR ALTIMETER BURST DATA RECORD SUMMARY"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=PHB2-M-VSK-2-EDR-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This data set consists of the set of images obtained by the VSK-Fregat experiment on the Phobos 2 spacecraft. This data set is saved for historical reasons, but is not considered to be of archival quality.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.phb2-m-vsk-2-edr-v1.0_wgxm-jfvp",
             "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "jupiter",
                 "phobos 2",
                 "phobos",
                 "mars"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=PHB2-M-VSK-2-EDR-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.phb2-m-vsk-2-edr-v1.0_wgxm-jfvp",
-            "description": "This data set consists of the set of images obtained by the VSK-Fregat experiment on the Phobos 2 spacecraft. This data set is saved for historical reasons, but is not considered to be of archival quality.",
-            "title": "PHOBOS 2 MARS VSK-FREGAT EDR V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "PHOBOS 2 MARS VSK-FREGAT EDR V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ADEOS-I/OCTS/L3M/KD/2014",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/GSFC/SED/ESD/GCDC/OB.DAAC. https://doi.org/10.5067/ADEOS-I/OCTS/L3M/KD/2014.",
-            "issued": "2017-01-11",
-            "temporal": "1996-11-01T00:00:00Z/1997-06-30T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2018-10-10",
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
-            "identifier": "C1200034383-OB_DAAC",
             "description": "On August 17, 1996, the Japanese Space Agency (NASDA - National Space Development Agency)\nlaunched the Advanced Earth Observing Satellite (ADEOS). ADEOS was in a descending, Sun\nsynchronous orbit with a nominal equatorial crossing time of 10:30 a.m. Amoung the\ninstruments carried aboard the ADEOS spacecraft was the Ocean Color and Temperature\nScanner (OCTS). OCTS is an optical radiometer with 12 bands covering the visible, near\ninfrared and thermal infrared regions. (Eight of the bands are in the VIS/NIR. These are\nthe only bands calibrated and processed by the OBPG) OCTS has a swath width of\napproximately 1400 km, and a nominal nadir resolution of 700 m. The instrument operated\nat three tilt states (20 degrees aft, nadir and 20 degrees fore), similar to SeaWiFS.",
-            "title": "ADEOS-I Ocean Color and Temperature Scanner (OCTS) Diffuse Attenuation Coefficient for Downwelling Irradiance (KD) Global Mapped Data",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FADEOS-I%2FOCTS%2FL3M%2FKD%2F2014",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FADEOS-I%2FOCTS%2FL3M%2FKD%2F2014",
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
-                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/atbd/kd_490",
-                    "description": "NASA Ocean Color Web - Algorithm Descriptions",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Ocean Color Web - Algorithm Descriptions",
+                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/atbd/kd_490",
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
-                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/data/10.5067/ADEOS-I/OCTS/L3M/KD/2014",
-                    "description": "OB.DAAC OCTS ADEOS-I L3M Diffuse Attenuation Coefficient for Downwelling Irradiance (KD) Landing Page",
                     "@type": "dcat:Distribution",
+                    "description": "OB.DAAC OCTS ADEOS-I L3M Diffuse Attenuation Coefficient for Downwelling Irradiance (KD) Landing Page",
+                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/data/10.5067/ADEOS-I/OCTS/L3M/KD/2014",
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
+            "identifier": "C1200034383-OB_DAAC",
+            "issued": "2017-01-11",
+            "keyword": [
+                "oceans",
+                "ocean optics",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/ADEOS-I/OCTS/L3M/KD/2014",
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
+            "title": "ADEOS-I Ocean Color and Temperature Scanner (OCTS) Diffuse Attenuation Coefficient for Downwelling Irradiance (KD) Global Mapped Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewBundle.jsp?identifier=urn%3Anasa%3Apds%3Amer2_pancam_sci_derived_color&version=1.0",
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
-                "mars exploration rover"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This bundle contains color mosaics from the Panoramic Cameras (Pancam) on Mars Exploration Rover 2 (Spirit). These data were produced by the science team.",
+            "identifier": "urn:nasa:pds:mer2_pancam_sci_derived_color",
+            "issued": "2021-05-21",
+            "keyword": [
+                "mars",
+                "mars exploration rover"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewBundle.jsp?identifier=urn%3Anasa%3Apds%3Amer2_pancam_sci_derived_color&version=1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:mer2_pancam_sci_derived_color",
-            "description": "This bundle contains color mosaics from the Panoramic Cameras (Pancam) on Mars Exploration Rover 2 (Spirit). These data were produced by the science team.",
-            "title": "MER2 Pancam Derived Color Mosaic Data Bundle",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "MER2 Pancam Derived Color Mosaic Data Bundle"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1953",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Hook, S.J., J.S. Myers, K.J. Thome, M. Fitzgerald, A.B. Kahle,  Airborne Sensor Facility NASA Ames Research Center, and R.O. Green. 2022. MASTER: Western Diversity Time Series Campaign, WDTS, California, USA, Spring 2021. ORNL DAAC, Oak Ridge, Tennessee, USA. https://doi.org/10.3334/ORNLDAAC/1953",
-            "issued": "2023-06-19",
-            "temporal": "2021-02-09T19:37:32Z/2021-04-02T23:11:06Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-13",
-            "keyword": [
-                "spectral/engineering",
-                "visible wavelengths",
-                "earth science",
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
-            "identifier": "C2731669314-ORNL_CLOUD",
             "description": "This dataset includes Level 1B (L1B) and Level 2 (L2) data products from the MODIS/ASTER Airborne Simulator (MASTER) instrument. The spectral data were collected as part of the Western Diversity Time Series (WDTS, formerly HyspIRI) airborne campaign during nine flights aboard a NASA ER-2 aircraft over selected areas of California and Nevada, U.S., from 2021-02-09 to 2021-04-02. The WDTS campaign will observe California's ecosystems and provide critical information on natural disasters such as volcanoes, wildfires, and drought. MASTER products can identify vegetation type and health and provide a benchmark for the state of the ecosystems against which future changes can be assessed. Data products include L1B georeferenced multispectral imagery of calibrated radiance in 50 bands covering wavelengths of 0.460 to 12.879 micrometers at approximately 50-meter spatial resolution. Derived L2 data products are emissivity in 5 bands in thermal infrared range (8.58 to 12.13 micrometers) and land surface temperature. The L1B file format is HDF-4, and L2 products are provided in ENVI and KMZ formats. In addition, the dataset includes the flight path, spectral band information, instrument configuration, ancillary notes, and summary information for each flight, and browse images derived from each L1B data file.",
-            "graphic-preview-description": "Single band images and an RGB composite image from flight track 03 acquired on 24 February 2021 near Ivanpah Lake, California, U.S. Source: MASTERL1B_2193000_03_20210224_1925_1928_V01.jpg",
-            "title": "MASTER: Western Diversity Time Series Campaign, WDTS, California, USA, Spring 2021",
-            "graphic-preview-file": "https://daac.ornl.gov/MASTER/guides/MASTER_WDTS_Spring_2021_Fig1.jpg",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1953",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1953",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/master/MASTER_WDTS_Spring_2021/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/master/MASTER_WDTS_Spring_2021/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/MASTER/guides/MASTER_WDTS_Spring_2021.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/MASTER/guides/MASTER_WDTS_Spring_2021.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1953",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1953",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/master/MASTER_WDTS_Spring_2021/comp/MASTER_WDTS_Spring_2021.pdf",
-                    "description": "MASTER: Western Diversity Time Series Campaign, WDTS, California, USA, Spring 2021: MASTER_WDTS_Spring_2021.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "MASTER: Western Diversity Time Series Campaign, WDTS, California, USA, Spring 2021: MASTER_WDTS_Spring_2021.pdf",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/master/MASTER_WDTS_Spring_2021/comp/MASTER_WDTS_Spring_2021.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://daac.ornl.gov/MASTER/guides/MASTER_WDTS_Spring_2021_Fig1.jpg",
-                    "description": "Single band images and an RGB composite image from flight track 03 acquired on 24 February 2021 near Ivanpah Lake, California, U.S. Source: MASTERL1B_2193000_03_20210224_1925_1928_V01.jpg",
                     "@type": "dcat:Distribution",
+                    "description": "Single band images and an RGB composite image from flight track 03 acquired on 24 February 2021 near Ivanpah Lake, California, U.S. Source: MASTERL1B_2193000_03_20210224_1925_1928_V01.jpg",
+                    "downloadURL": "https://daac.ornl.gov/MASTER/guides/MASTER_WDTS_Spring_2021_Fig1.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 }
             ],
+            "graphic-preview-description": "Single band images and an RGB composite image from flight track 03 acquired on 24 February 2021 near Ivanpah Lake, California, U.S. Source: MASTERL1B_2193000_03_20210224_1925_1928_V01.jpg",
+            "graphic-preview-file": "https://daac.ornl.gov/MASTER/guides/MASTER_WDTS_Spring_2021_Fig1.jpg",
+            "identifier": "C2731669314-ORNL_CLOUD",
+            "issued": "2023-06-19",
+            "keyword": [
+                "spectral/engineering",
+                "visible wavelengths",
+                "earth science",
+                "infrared wavelengths"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1953",
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
             "spatial": "-123.82 31.95 -112.49 40.98",
+            "temporal": "2021-02-09T19:37:32Z/2021-04-02T23:11:06Z",
             "theme": [
                 "MASTER",
                 "WDTS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "MASTER: Western Diversity Time Series Campaign, WDTS, California, USA, Spring 2021"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C%2FCAL-ALICE-4-ESC1-V2.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This data set contains CODMAC Level 4 data acquired by the Rosetta Orbiter ALICE UV Spectrometer during the comet 67P/Churyumov-Gerasimenko Comet Escort 1 mission phase, which took place between 2014-11-20 and 2015-03-10.  The current V2.0 data set supersedes the previous V1.0 data set.  Pixel list data files have had corrections applied to their FITS formatting, and browse images have been supplied.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-cal-alice-4-esc1-v2.0_wh2a-b4cb",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
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
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C%2FCAL-ALICE-4-ESC1-V2.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-cal-alice-4-esc1-v2.0_wh2a-b4cb",
-            "description": "This data set contains CODMAC Level 4 data acquired by the Rosetta Orbiter ALICE UV Spectrometer during the comet 67P/Churyumov-Gerasimenko Comet Escort 1 mission phase, which took place between 2014-11-20 and 2015-03-10.  The current V2.0 data set supersedes the previous V1.0 data set.  Pixel list data files have had corrections applied to their FITS formatting, and browse images have been supplied.",
-            "title": "ROSETTA-ORBITER 67P/CAL ALICE 4 ESC1 V2.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P/CAL ALICE 4 ESC1 V2.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=PVO-V-OEFD-3--EFIELD-HIRES-V1.0",
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
+            "description": "not applicable",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.pvo-v-oefd-3--efield-hires-v1.0_wh33-m9xn",
+            "issued": "2018-06-26",
+            "keyword": [
+                "venus",
+                "pioneer venus"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=PVO-V-OEFD-3--EFIELD-HIRES-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.pvo-v-oefd-3--efield-hires-v1.0_wh33-m9xn",
-            "description": "not applicable",
-            "title": "PVO VENUS SC POSITION DERIVED VSO COORDS 12 SECOND VER1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "PVO VENUS SC POSITION DERIVED VSO COORDS 12 SECOND VER1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C2340494639-OB_DAAC.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/GSFC/SED/ESD/GCDC/OB.DAAC.",
-            "issued": "2022-09-14",
-            "temporal": "2017-11-29T00:00:00Z/2023-03-01T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-09-14",
-            "keyword": [
-                "earth science",
-                "atmosphere",
-                "aerosols",
-                "oceans",
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
-            "identifier": "C2340494639-OB_DAAC",
             "description": "The Ocean Biology DAAC produces near real-time (quicklook) products using the best-available combination of ancillary data from meteorological and ozone data. As such, the inputs and the calibration used are less than optimal. Quicklook products provide a snapshot of the data during a short time period within a single orbit.",
-            "title": "NOAA-20 VIIRS Global Mapped Remote-Sensing Reflectance (RRS) - NRT Data, version R2022.0",
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
-                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/data/10.5067/NOAA20/VIIRS/L3M/RRS/2022",
-                    "description": "VIIRS-NOAA-20 L3M Remote-Sensing Reflectance (RRS) - NRT Dataset Landing Page",
                     "@type": "dcat:Distribution",
+                    "description": "VIIRS-NOAA-20 L3M Remote-Sensing Reflectance (RRS) - NRT Dataset Landing Page",
+                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/data/10.5067/NOAA20/VIIRS/L3M/RRS/2022",
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
+            "identifier": "C2340494639-OB_DAAC",
+            "issued": "2022-09-14",
+            "keyword": [
+                "earth science",
+                "atmosphere",
+                "aerosols",
+                "oceans",
+                "ocean optics"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C2340494639-OB_DAAC.html",
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
+            "temporal": "2017-11-29T00:00:00Z/2023-03-01T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "NOAA-20 VIIRS Global Mapped Remote-Sensing Reflectance (RRS) - NRT Data, version R2022.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=DAWN-A-VIR-3-RDR-VIS-VESTA-SPECTRA-V2.0",
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
+            "description": "This data set contains the spectral      radiance (W/(m**2*sr*micron)) data from the Dawn VIR instrument         visible channel for all Vesta encounter mission phases. The data in    this version of the data set have been produced using an updated        calibration. The data cover the time period between 2011-05-03 and      2012-07-18.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.dawn-a-vir-3-rdr-vis-vesta-spectra-v2.0_wh7t-tktv",
+            "issued": "2018-06-26",
+            "keyword": [
+                "4 vesta",
+                "dawn mission to vesta and ceres"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=DAWN-A-VIR-3-RDR-VIS-VESTA-SPECTRA-V2.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.dawn-a-vir-3-rdr-vis-vesta-spectra-v2.0_wh7t-tktv",
-            "description": "This data set contains the spectral      radiance (W/(m**2*sr*micron)) data from the Dawn VIR instrument         visible channel for all Vesta encounter mission phases. The data in    this version of the data set have been produced using an updated        calibration. The data cover the time period between 2011-05-03 and      2012-07-18.",
-            "title": "DAWN VIR CAL (RDR) VESTA VISIBLE SPECTRA V2.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "DAWN VIR CAL (RDR) VESTA VISIBLE SPECTRA V2.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/NIMBUS/NmTHIR115-3G",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Nimbus Temperature-Humidity Infrared Radiometer 11.5 \u00b5m Remapped Digital Data Daily L3, GeoTIFF V001. Version 1. Archived by National Aeronautics and Space Administration, U.S. Government, NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/NIMBUS/NmTHIR115-3G.",
-            "issued": "1970-04-13",
-            "temporal": "1970-04-13T00:00:00Z/1971-04-01T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "1971-04-01",
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
-            "identifier": "C1690291112-NSIDC_ECS",
             "description": "This data set (NmTHIR115-3G) consists of daily, global composites of radiative temperatures obtained in the 11.5 \u00b5m window (10.5 \u00b5m - 12.5 \u00b5m) by the Temperature-Humidity Infrared Radiometer (THIR) on board the Nimbus 4 satellite. This window was used to measure cloud top or surface temperatures. Data files are GeoTIFF versions of the HDF-formatted equatorial projection file <em>only</em> from the Nimbus Temperature-Humidity Infrared Radiometer 11.5 \u00b5m Remapped Digital Data Daily L3, HDF5 (<a href=\"http://dx.doi.org/10.5067/NIMBUS/NmTHIR115-3H\">NmTHIR115-3H</a>) data set.",
-            "title": "Nimbus Temperature-Humidity Infrared Radiometer 11.5 \u00b5m Remapped Digital Data Daily L3, GeoTIFF V001",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FNIMBUS%2FNmTHIR115-3G",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FNIMBUS%2FNmTHIR115-3G",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/NIMBUS/NmTHIR115-3G.001/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/NIMBUS/NmTHIR115-3G.001/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1242109290-NSIDC_ECS&m=-54.703125%2118%211%211%210%210%2C2&q=NmTHIR115-3G",
-                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1242109290-NSIDC_ECS&m=-54.703125%2118%211%211%210%210%2C2&q=NmTHIR115-3G",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/data/data-access-tool/NmTHIR115-3G/versions/1/",
-                    "description": "Data Access link for ITSD project",
                     "@type": "dcat:Distribution",
+                    "description": "Data Access link for ITSD project",
+                    "downloadURL": "https://nsidc.org/data/data-access-tool/NmTHIR115-3G/versions/1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/NIMBUS/NmTHIR115-3G",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/NIMBUS/NmTHIR115-3G",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/NIMBUS/NmTHIR115-3G",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/NIMBUS/NmTHIR115-3G",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C1690291112-NSIDC_ECS",
+            "issued": "1970-04-13",
+            "keyword": [
+                "spectral/engineering",
+                "infrared wavelengths",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/NIMBUS/NmTHIR115-3G",
+            "language": [
+                "en-US"
+            ],
+            "modified": "1971-04-01",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA NSIDC DAAC"
+            },
             "spatial": "-180.0 -60.0 180.0 60.0",
+            "temporal": "1970-04-13T00:00:00Z/1971-04-01T23:59:59.999Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Nimbus Temperature-Humidity Infrared Radiometer 11.5 \u00b5m Remapped Digital Data Daily L3, GeoTIFF V001"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MER1-M-HAZCAM-5-SLOPE-OPS-V1.0",
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
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mer1-m-hazcam-5-slope-ops-v1.0_wh8p-sfkg",
+            "issued": "2021-05-21",
+            "keyword": [
+                "mars",
+                "mars exploration rover"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MER1-M-HAZCAM-5-SLOPE-OPS-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mer1-m-hazcam-5-slope-ops-v1.0_wh8p-sfkg",
-            "description": "NULL",
-            "title": "MER 1 MARS HAZARD AVOID CAMERA SLOPE RDR \n                                      OPS V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "MER 1 MARS HAZARD AVOID CAMERA SLOPE RDR \n                                      OPS V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/MODIS/MOD21.061",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Glynn Hulley, Simon Hook. 2021-02-08. MODIS/Terra Land Surface Temperature/3-Band Emissivity 5-Min L2 1km V061. Sioux Falls, South Dakota, USA. Archived by National Aeronautics and Space Administration, U.S. Government, NASA EOSDIS Land Processes Distributed Active Archive Center. https://doi.org/10.5067/MODIS/MOD21.061. https://doi.org/10.5067/MODIS/MOD21.061. The DOI landing page provides citations in APA and Chicago styles..",
-            "issued": "2021-02-08",
-            "temporal": "2000-02-24T00:00:00Z/2024-05-27T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2021-02-08",
-            "keyword": [
-                "national geospatial data asset",
-                "surface radiative properties",
-                "land surface",
-                "ngda",
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
-            "identifier": "C2565791036-LPCLOUD",
-            "description": "The MOD21 Land Surface Temperature and Emissivity (LST&E) swath data product is produced daily in five minute temporal increments of satellite acquisition. The swath is approximately 2,030 pixels along track and 1,354 pixels per line, at a nadir resolution of 1,000 meters. The MOD21 Land Surface Temperature (LST) algorithm differs from the MOD11 (https://doi.org/10.5067/modis/mod11_l2.061) algorithm in that the MOD21 LST algorithm is based on the ASTER Temperature/Emissivity Separation (TES) technique, whereas the MOD11 uses the split-window technique. The MOD21 TES algorithm uses a physics-based algorithm to dynamically retrieve both LST and spectral emissivity simultaneously from the MODIS thermal infrared bands 29, 31, and 32. The TES algorithm is combined with an improved Water Vapor Scaling (WVS) atmospheric correction scheme to stabilize the retrieval during very warm and humid conditions. Additional details regarding the method used to create this Level 2 (L2) product are available in the Algorithm Theoretical Basis Document (ATBD (https://lpdaac.usgs.gov/documents/1399/MOD21_ATBD.pdf)).  \r\n\r\nValidation at stage 1 (https://modis-land.gsfc.nasa.gov/MODLAND_val.html) has been achieved for the MODIS Land Surface Temperature and Emissivity data products. Further details regarding MODIS land product validation for the MOD21 data products are available from the MODIS Land Team Validation site (https://modis-land.gsfc.nasa.gov/ValStatus.php?ProductID=MOD21).\r\n\r\nImprovements/Changes from Previous Versions\r\n\r\n* The Version 6.1 Level-1B (L1B) products have been improved by undergoing various calibration changes that include: changes to the response-versus-scan angle (RVS) approach that affects reflectance bands for Aqua and Terra MODIS, corrections to adjust for the optical crosstalk in Terra MODIS infrared (IR) bands, and corrections to the Terra MODIS forward look-up table (LUT) update for the period 2012 - 2017.\r\n* A polarization correction has been applied to the L1B Reflective Solar Bands (RSB).\r\n* The product utilizes GEOS data replacing MERRA2. \r\n* Three new CMG products are available in the MxD21 suite (MxD21C1/C2/C3).",
-            "release-place": "Sioux Falls, South Dakota, USA",
-            "graphic-preview-description": "Browse image for Earthdata Search",
             "creator": "Glynn Hulley, Simon Hook",
-            "title": "MODIS/Terra Land Surface Temperature/3-Band Emissivity 5-Min L2 1km V061",
-            "graphic-preview-file": "https://cmr.earthdata.nasa.gov/browse-scaler/browse_images/granules/G2631454963-LPCLOUD?h=85&w=85",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The MOD21 Land Surface Temperature and Emissivity (LST&E) swath data product is produced daily in five minute temporal increments of satellite acquisition. The swath is approximately 2,030 pixels along track and 1,354 pixels per line, at a nadir resolution of 1,000 meters. The MOD21 Land Surface Temperature (LST) algorithm differs from the MOD11 (https://doi.org/10.5067/modis/mod11_l2.061) algorithm in that the MOD21 LST algorithm is based on the ASTER Temperature/Emissivity Separation (TES) technique, whereas the MOD11 uses the split-window technique. The MOD21 TES algorithm uses a physics-based algorithm to dynamically retrieve both LST and spectral emissivity simultaneously from the MODIS thermal infrared bands 29, 31, and 32. The TES algorithm is combined with an improved Water Vapor Scaling (WVS) atmospheric correction scheme to stabilize the retrieval during very warm and humid conditions. Additional details regarding the method used to create this Level 2 (L2) product are available in the Algorithm Theoretical Basis Document (ATBD (https://lpdaac.usgs.gov/documents/1399/MOD21_ATBD.pdf)).  \r\n\r\nValidation at stage 1 (https://modis-land.gsfc.nasa.gov/MODLAND_val.html) has been achieved for the MODIS Land Surface Temperature and Emissivity data products. Further details regarding MODIS land product validation for the MOD21 data products are available from the MODIS Land Team Validation site (https://modis-land.gsfc.nasa.gov/ValStatus.php?ProductID=MOD21).\r\n\r\nImprovements/Changes from Previous Versions\r\n\r\n* The Version 6.1 Level-1B (L1B) products have been improved by undergoing various calibration changes that include: changes to the response-versus-scan angle (RVS) approach that affects reflectance bands for Aqua and Terra MODIS, corrections to adjust for the optical crosstalk in Terra MODIS infrared (IR) bands, and corrections to the Terra MODIS forward look-up table (LUT) update for the period 2012 - 2017.\r\n* A polarization correction has been applied to the L1B Reflective Solar Bands (RSB).\r\n* The product utilizes GEOS data replacing MERRA2. \r\n* Three new CMG products are available in the MxD21 suite (MxD21C1/C2/C3).",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMODIS%2FMOD21.061",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMODIS%2FMOD21.061",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "application/x-hdf",
-                    "downloadURL": "https://e4ftl01.cr.usgs.gov/MOLT/MOD21.061/",
-                    "description": "LP DAAC Data Pool provides direct access to available products via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "LP DAAC Data Pool provides direct access to available products via HTTPS.",
+                    "downloadURL": "https://e4ftl01.cr.usgs.gov/MOLT/MOD21.061/",
+                    "mediaType": "application/x-hdf",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "application/x-hdf",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=C2565791036-LPCLOUD",
-                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=C2565791036-LPCLOUD",
+                    "mediaType": "application/x-hdf",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/MODIS/MOD21.061",
-                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
+                    "downloadURL": "https://doi.org/10.5067/MODIS/MOD21.061",
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
-                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/filespec/MODIS/6/MOD21",
-                    "description": "The File Specification provides a description of the product file including Scientific Data Sets and their attributes.",
                     "@type": "dcat:Distribution",
+                    "description": "The File Specification provides a description of the product file including Scientific Data Sets and their attributes.",
+                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/filespec/MODIS/6/MOD21",
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
-                    "description": "Further details regarding MODIS land product validation for the MOD21 data products are available from the MODIS Land Team Validation site.",
                     "@type": "dcat:Distribution",
+                    "description": "Further details regarding MODIS land product validation for the MOD21 data products are available from the MODIS Land Team Validation site.",
+                    "downloadURL": "https://modis-land.gsfc.nasa.gov/ValStatus.php?ProductID=MOD21",
+                    "mediaType": "text/html",
                     "title": "View this dataset's science data product validation documentation"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://opendap.cr.usgs.gov/opendap/hyrax/DP131/MOLT/MOD21.061/contents.html",
-                    "description": "Access data via Open-source Project for a Network Data Access Protocol",
                     "@type": "dcat:Distribution",
+                    "description": "Access data via Open-source Project for a Network Data Access Protocol",
+                    "downloadURL": "https://opendap.cr.usgs.gov/opendap/hyrax/DP131/MOLT/MOD21.061/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/browse-scaler/browse_images/granules/G2631454963-LPCLOUD?h=85&w=85",
-                    "description": "Browse image for Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse image for Earthdata Search",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/browse-scaler/browse_images/granules/G2631454963-LPCLOUD?h=85&w=85",
+                    "mediaType": "text/html",
                     "title": "Get a related visualization"
                 }
             ],
+            "graphic-preview-description": "Browse image for Earthdata Search",
+            "graphic-preview-file": "https://cmr.earthdata.nasa.gov/browse-scaler/browse_images/granules/G2631454963-LPCLOUD?h=85&w=85",
+            "identifier": "C2565791036-LPCLOUD",
+            "issued": "2021-02-08",
+            "keyword": [
+                "national geospatial data asset",
+                "surface radiative properties",
+                "land surface",
+                "ngda",
+                "earth science",
+                "surface thermal properties"
+            ],
+            "landingPage": "https://doi.org/10.5067/MODIS/MOD21.061",
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
+            "temporal": "2000-02-24T00:00:00Z/2024-05-27T00:00:00Z",
             "theme": [
                 "Terra",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "MODIS/Terra Land Surface Temperature/3-Band Emissivity 5-Min L2 1km V061"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C%2FCAL-ALICE-4-PRL-V2.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This data set contains CODMAC Level 4 data acquired by the Rosetta Orbiter ALICE UV Spectrometer during the comet 67P/Churyumov-Gerasimenko Prelanding mission phase, which took place between 2014-01-21 and 2014-11-19.  The current V2.0 data set supersedes the previous V1.0 data set.  Pixel list data files have had corrections applied to their FITS formatting, and browse images have been supplied.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-cal-alice-4-prl-v2.0",
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
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C%2FCAL-ALICE-4-PRL-V2.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-cal-alice-4-prl-v2.0",
-            "description": "This data set contains CODMAC Level 4 data acquired by the Rosetta Orbiter ALICE UV Spectrometer during the comet 67P/Churyumov-Gerasimenko Prelanding mission phase, which took place between 2014-01-21 and 2014-11-19.  The current V2.0 data set supersedes the previous V1.0 data set.  Pixel list data files have had corrections applied to their FITS formatting, and browse images have been supplied.",
-            "title": "ROSETTA-ORBITER 67P/CAL ALICE 4 PRL V2.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P/CAL ALICE 4 PRL V2.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.nasa.gov/d/whbe-gfq7",
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
+            "identifier": "nasa_genelab_GLDS-16_whbe-gfq7",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
             "keyword": [
                 "spaceflight",
                 "labeling",
@@ -1575057,48 +1575071,43 @@
                 "sample collection",
                 "organism part"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "GeneLab Outreach",
-                "hasEmail": "mailto:genelab-outreach@lists.nasa.gov"
-            },
+            "landingPage": "https://data.nasa.gov/d/whbe-gfq7",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "nasa_genelab_GLDS-16_whbe-gfq7",
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
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
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
+                    "downloadURL": "http://turbmodels.larc.nasa.gov/Other_exp_Data/Coanda/ldv_lower_xc_0.8_cm_0.047.dat",
+                    "mediaType": "application/dat"
+                }
             ],
+            "identifier": "NASA-851__5",
+            "issued": "2018-06-25",
             "keyword": [
                 "coanda",
                 "experiment",
@@ -1575110,620 +1575119,591 @@
                 "synthetic",
                 "jets"
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
-            "identifier": "NASA-851__5",
-            "description": "2-D Coanda Airfoil with Tangential Wall Jet. This web page provides data from experiments that may be useful for the validation of turbulence models. This resource is expected to grow gradually over time. All data herein arepublicly available.",
-            "title": "Turbulence Models: Data from Other Experiments: 2-D Coanda Airfoil with Tangential Wall Jet",
-            "programCode": [
-                "026:023"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://turbmodels.larc.nasa.gov/Other_exp_Data/Coanda/ldv_lower_xc_0.8_cm_0.047.dat",
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
-            "landingPage": "https://doi.org/10.5067/SeaBASS/NES-LTER/DATA001",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/GSFC/SED/ESD/GCDC/OB.DAAC. https://doi.org/10.5067/SeaBASS/NES-LTER/DATA001.",
-            "issued": "2018-01-31",
-            "temporal": "2018-01-31T00:00:02Z/2023-04-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-04-06",
-            "keyword": [
-                "ocean chemistry",
-                "oceans",
-                "ocean temperature",
-                "salinity/density",
-                "earth science",
-                "ocean optics"
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
-            "identifier": "C2208430341-OB_DAAC",
             "description": "The Northeast U.S. Shelf (NES) Long-Term Ecological Research (LTER) project integrates observations, experiments, and models to understand and predict how planktonic food webs are changing, and how those changes impact the productivity of higher trophic levels. The NES-LTER is co-located with the Northeast U.S. Continental Shelf Large Marine Ecosystem, spanning the Middle Atlantic Bight and Gulf of Maine. Our focal cross-shelf transect extends about 150 km southward from Martha&#39s Vineyard, MA, to just beyond the shelf break.",
-            "title": "Northeast U.S. Shelf (NES), Long-Term Ecological Research (LTER)",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSeaBASS%2FNES-LTER%2FDATA001",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSeaBASS%2FNES-LTER%2FDATA001",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://seabass.gsfc.nasa.gov/experiment/NES-LTER/",
-                    "description": "Detailed information about the SeaBASS Experiment such as cruises, funding, and investigators",
                     "@type": "dcat:Distribution",
+                    "description": "Detailed information about the SeaBASS Experiment such as cruises, funding, and investigators",
+                    "downloadURL": "https://seabass.gsfc.nasa.gov/experiment/NES-LTER/",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 }
             ],
+            "identifier": "C2208430341-OB_DAAC",
+            "issued": "2018-01-31",
+            "keyword": [
+                "ocean chemistry",
+                "oceans",
+                "ocean temperature",
+                "salinity/density",
+                "earth science",
+                "ocean optics"
+            ],
+            "landingPage": "https://doi.org/10.5067/SeaBASS/NES-LTER/DATA001",
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
+            "temporal": "2018-01-31T00:00:02Z/2023-04-17T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Northeast U.S. Shelf (NES), Long-Term Ecological Research (LTER)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-MIRO-3-EXT1-67P-V1.0",
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
+            "description": "This data set contains Spectroscopic and Continuum, calibrated data, in the form of table files, taken during the ROSETTA EXTENSION 1 phase of the Rosetta mission to comet 67P/CHURYUMOV-GERASIMENKO by the MIRO instrument.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-miro-3-ext1-67p-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-MIRO-3-EXT1-67P-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-miro-3-ext1-67p-v1.0",
-            "description": "This data set contains Spectroscopic and Continuum, calibrated data, in the form of table files, taken during the ROSETTA EXTENSION 1 phase of the Rosetta mission to comet 67P/CHURYUMOV-GERASIMENKO by the MIRO instrument.",
-            "title": "ROSETTA-ORBITER 67P MIRO 3 EXT1 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P MIRO 3 EXT1 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1386206769-NSIDCV0.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Rock glaciers, Austria, Version 1. Version 1. Archived by National Aeronautics and Space Administration, U.S. Government, National Snow and Ice Data Center.",
-            "issued": "1980-01-01",
-            "temporal": "1980-01-01T00:00:00Z/1990-12-31T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "1990-12-31",
-            "keyword": [
-                "earth science",
-                "frozen ground",
-                "land surface",
-                "cryosphere"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "undefined",
                 "hasEmail": "mailto:nsidc@nsidc.org"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NSIDC"
-            },
-            "identifier": "C1386206769-NSIDCV0",
             "description": "The Austrian Alps are part of the Eastern Alps which consist of three main mountain ranges. The Northern Alps as well as the Southern Alps are predominantly built of limestone and have poor glaciation in spite of high amounts of precipitation (2000-3000 mm/a) due to the fact that they reach elevations of not more than 3000 m. In contrast the Central Alps consist of metamorphic rocks and receive less precipitation, but are glaciated on large areas (highest mountain of Austria: Groglockner, 3797 m). Recent permafrost and rock glaciers are best developed in the Central Alps, where discontinuous mountain permafrost occurs above a mean altitude of 2500 m.\n\nRock glaciers were mapped from aerial photographs (different years, most of them 1980-1990) completely covering the area described above. The inventory comprises 1451 rock glaciers with data on their horizontal and vertical position, activity, and morphometric characteristics of each rock glacier. The distinction between active and inactive rock glaciers within the activity class 'intact' was not possible due to the quality of the photographs. Only 19 % of the rock glaciers were classified as intact, while 81 % are relict ones and in most cases of Late Glacial age (a great part of the investigated is situated below present day lower limit of permafrost). In detail the inventory contains information of the following parameters:\n1: River basin\n2: Number of rock glacier according to river basins\n3: Topographic name out of the official map 1:50.000\n4: Mountain group\n5: Number of official map 1:50.000\n6: Number of official aerial photograph map\n7: Exposure (8 classes)\n8: Lower limit of rock glacier (m above sea level)\n9: Maximum length (m, in estimated flow direction)\n10: Maximum width (m)\n11: Activity (2 classes: intact, relict=fossil)\n12: Highest point of the catchment area of the rock glacier\n(m above sea level)\n13: Difference between 12 and 8 (m)\n\nGeographic coordinates of coverage as listed in the GGD inventory are approximate. These data are presented on the CAPS Version 1.0 CD-ROM, June 1998. The inventory does not include measurements on dynamics of rock glacier permafrost.",
-            "title": "Rock glaciers, Austria, Version 1",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/forms/GGD310_or.html?major_version=1",
-                    "description": "Direct download, with optional registration page.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download, with optional registration page.",
+                    "downloadURL": "https://nsidc.org/forms/GGD310_or.html?major_version=1",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/data/GGD310/versions/1",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://nsidc.org/data/GGD310/versions/1",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/data/GGD310/versions/1",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://nsidc.org/data/GGD310/versions/1",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C1386206769-NSIDCV0",
+            "issued": "1980-01-01",
+            "keyword": [
+                "earth science",
+                "frozen ground",
+                "land surface",
+                "cryosphere"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1386206769-NSIDCV0.html",
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
             "spatial": "12.0 47.0 17.0 49.0",
+            "temporal": "1980-01-01T00:00:00Z/1990-12-31T23:59:59.999Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Rock glaciers, Austria, Version 1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC2-0733-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 2 phase 2015-03-11 to 2015-06-30. It is a Global Gravity measurement at the comet 67P and covers the time 2015-04-26T23:42:05.000 to 2015-04-27T03:17:06.500.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc2-0733-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC2-0733-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc2-0733-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 2 phase 2015-03-11 to 2015-06-30. It is a Global Gravity measurement at the comet 67P and covers the time 2015-04-26T23:42:05.000 to 2015-04-27T03:17:06.500.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 2 0733 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 2 0733 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1238",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "West, T.O. 2014. Soil Carbon Estimates in 20-cm Layers to 1-meter Depth, Conterminous US, 1970-1993. ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/1238",
-            "issued": "2022-02-12",
-            "temporal": "1970-01-01T00:00:00Z/1993-12-30T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-06-12",
-            "keyword": [
-                "soils",
-                "earth science",
-                "agriculture",
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
-            "identifier": "C2216863502-ORNL_CLOUD",
             "description": "This data set provides a soil map with estimates of soil carbon (C) in g C/m2 for 20-cm layers from the surface to one meter depth for the conterminous United States.STATSGO v.1 (State Soil Geographic Database, Soil Survey Staff, 1994) data were used to estimate by 20-cm intervals to a 1-m depth the mean soil carbon for each of the STATSGO-delineated soil map units. These map units are the polygons represented in the provided Shapefile data product.",
-            "graphic-preview-description": "Soil carbon in g C/m2 for the 0-20 cm layer for central Florida.",
-            "title": "Soil Carbon Estimates in 20-cm Layers to 1-meter Depth, Conterminous US, 1970-1993",
-            "graphic-preview-file": "https://daac.ornl.gov/SOILS/guides/Fig2_west-soil_map_florida.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1238",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1238",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/global_soil/West_Soil_Carbon/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/global_soil/West_Soil_Carbon/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/SOILS/guides/West_Soil_Carbon.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/SOILS/guides/West_Soil_Carbon.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1238",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1238",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/global_soil/West_Soil_Carbon/comp/West_Soil_Carbon.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/global_soil/West_Soil_Carbon/comp/West_Soil_Carbon.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://daac.ornl.gov/SOILS/guides/Fig2_west-soil_map_florida.png",
-                    "description": "Soil carbon in g C/m2 for the 0-20 cm layer for central Florida.",
                     "@type": "dcat:Distribution",
+                    "description": "Soil carbon in g C/m2 for the 0-20 cm layer for central Florida.",
+                    "downloadURL": "https://daac.ornl.gov/SOILS/guides/Fig2_west-soil_map_florida.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 }
             ],
+            "graphic-preview-description": "Soil carbon in g C/m2 for the 0-20 cm layer for central Florida.",
+            "graphic-preview-file": "https://daac.ornl.gov/SOILS/guides/Fig2_west-soil_map_florida.png",
+            "identifier": "C2216863502-ORNL_CLOUD",
+            "issued": "2022-02-12",
+            "keyword": [
+                "soils",
+                "earth science",
+                "agriculture",
+                "land surface"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1238",
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
             "spatial": "-135.68 22.27 -54.82 53.54",
+            "temporal": "1970-01-01T00:00:00Z/1993-12-30T23:59:59Z",
             "theme": [
                 "Soil",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Soil Carbon Estimates in 20-cm Layers to 1-meter Depth, Conterminous US, 1970-1993"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ECOSTRESS/ECO_L2T_LSTE.002",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Simon Hook, Glynn Hulley. 2022-11-14. ECOSTRESS Tiled Land Surface Temperature and Emissivity Instantaneous L2 Global 70 m v002. Sioux Falls, South Dakota, USA. Archived by National Aeronautics and Space Administration, U.S. Government, NASA EOSDIS Land Processes Distributed Active Archive Center. https://doi.org/10.5067/ECOSTRESS/ECO_L2T_LSTE.002. https://doi.org/10.5067/ECOSTRESS/ECO_L2T_LSTE.002. The DOI landing page provides citations in APA and Chicago styles..",
-            "issued": "2022-11-14",
-            "temporal": "2018-07-09T00:00:00Z/2024-06-03T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-11-14",
-            "keyword": [
-                "earth science",
-                "surface thermal properties",
-                "surface radiative properties",
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
-            "identifier": "C2076090826-LPCLOUD",
-            "description": "The ECOsystem Spaceborne Thermal Radiometer Experiment on Space Station (ECOSTRESS) mission measures the temperature of plants to better understand how much water plants need and how they respond to stress. ECOSTRESS is attached to the International Space Station (ISS) and collects data globally between 52\u00b0 N and 52\u00b0 S latitudes. A map of the acquisition coverage can be found in Figure 2 on the ECOSTRESS website(https://ecostress.jpl.nasa.gov/science).\r\nThe ECOSTRESS Tiled Land Surface Temperature and Emissivity Instantaneous Level 2 Global 70 m (ECO_L2T_LSTE) Version 2 data product provides atmospherically corrected land surface temperature and emissivity (LST&E) values derived from five thermal infrared (TIR) bands. The ECO_L2T_LSTE data product was derived using a physics-based Temperature/Emissivity Separation (TES) algorithm. This tiled data product is subset from the ECO_L2G_LSTE data product using a modified version of the Military Grid Reference System (MGRS) which divides Universal Transverse Mercator (UTM) zones into square tiles that are 109.8 km by 109.8 km with a 70 meter (m) spatial resolution.\r\nThe ECO_L2T_LSTE Version 2 data product is provided in Cloud Optimized GeoTIFF (COG) format, and each band is distributed as a separate COG. This product contains seven layers including LST, LST error, wideband emissivity, quality flags, height, and cloud and water masks.\r\n\r\nKnown Issues: *Data acquisition gap: ECOSTRESS was launched on June 29, 2018, and moved to autonomous science operations on August 20, 2018, following a successful in-orbit checkout period. On September 29, 2018, ECOSTRESS experienced an anomaly with its primary mass storage unit (MSU). ECOSTRESS has a primary and secondary MSU (A and B). On December 5, 2018, the instrument was switched to the secondary MSU and science operations resumed. On March 14, 2019, the secondary MSU experienced a similar anomaly, temporarily halting science acquisitions. On May 15, 2019, a new data acquisition approach was implemented, and science acquisitions resumed. To optimize the new acquisition approach TIR bands 2, 4, and 5 are being downloaded. The data products are as previously, except the bands not downloaded contain fill values (L1 radiance and L2 emissivity). This approach was implemented from May 15, 2019, through April 28, 2023.\r\n*Data acquisition gap: From February 8 to February 16, 2020, an ECOSTRESS instrument issue resulted in a data anomaly that created striping in band 4 (10.5 micron). These data products have been reprocessed and are available for download. No ECOSTRESS data were acquired on February 17, 2020, due to the instrument being in SAFEHOLD. Data acquired following the anomaly have not been affected.\r\n*Data acquisition: ECOSTRESS has now successfully returned to 5-band mode after being in 3-band mode since 2019. This feature was successfully enabled following a Data Processing Unit firmware update (version 4.1) to the payload on April 28, 2023. To better balance contiguous science data scene variables, 3-band collection is currently being interleaved with 5-band acquisitions over the orbital day/night periods.",
-            "release-place": "Sioux Falls, South Dakota, USA",
-            "graphic-preview-description": "Browse image for Earthdata Search",
             "creator": "Simon Hook, Glynn Hulley",
-            "title": "ECOSTRESS Tiled Land Surface Temperature and Emissivity Instantaneous L2 Global 70 m V002",
-            "graphic-preview-file": "https://data.lpdaac.earthdatacloud.nasa.gov/lp-prod-public/ECO_L2T_LSTE.002/ECOv002_L2T_LSTE_21247_032_19MCN_20220405T135253_0700_01/ECOv002_L2T_LSTE_21247_032_19MCN_20220405T135253_0700_01.png",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The ECOsystem Spaceborne Thermal Radiometer Experiment on Space Station (ECOSTRESS) mission measures the temperature of plants to better understand how much water plants need and how they respond to stress. ECOSTRESS is attached to the International Space Station (ISS) and collects data globally between 52\u00b0 N and 52\u00b0 S latitudes. A map of the acquisition coverage can be found in Figure 2 on the ECOSTRESS website(https://ecostress.jpl.nasa.gov/science).\r\nThe ECOSTRESS Tiled Land Surface Temperature and Emissivity Instantaneous Level 2 Global 70 m (ECO_L2T_LSTE) Version 2 data product provides atmospherically corrected land surface temperature and emissivity (LST&E) values derived from five thermal infrared (TIR) bands. The ECO_L2T_LSTE data product was derived using a physics-based Temperature/Emissivity Separation (TES) algorithm. This tiled data product is subset from the ECO_L2G_LSTE data product using a modified version of the Military Grid Reference System (MGRS) which divides Universal Transverse Mercator (UTM) zones into square tiles that are 109.8 km by 109.8 km with a 70 meter (m) spatial resolution.\r\nThe ECO_L2T_LSTE Version 2 data product is provided in Cloud Optimized GeoTIFF (COG) format, and each band is distributed as a separate COG. This product contains seven layers including LST, LST error, wideband emissivity, quality flags, height, and cloud and water masks.\r\n\r\nKnown Issues: *Data acquisition gap: ECOSTRESS was launched on June 29, 2018, and moved to autonomous science operations on August 20, 2018, following a successful in-orbit checkout period. On September 29, 2018, ECOSTRESS experienced an anomaly with its primary mass storage unit (MSU). ECOSTRESS has a primary and secondary MSU (A and B). On December 5, 2018, the instrument was switched to the secondary MSU and science operations resumed. On March 14, 2019, the secondary MSU experienced a similar anomaly, temporarily halting science acquisitions. On May 15, 2019, a new data acquisition approach was implemented, and science acquisitions resumed. To optimize the new acquisition approach TIR bands 2, 4, and 5 are being downloaded. The data products are as previously, except the bands not downloaded contain fill values (L1 radiance and L2 emissivity). This approach was implemented from May 15, 2019, through April 28, 2023.\r\n*Data acquisition gap: From February 8 to February 16, 2020, an ECOSTRESS instrument issue resulted in a data anomaly that created striping in band 4 (10.5 micron). These data products have been reprocessed and are available for download. No ECOSTRESS data were acquired on February 17, 2020, due to the instrument being in SAFEHOLD. Data acquired following the anomaly have not been affected.\r\n*Data acquisition: ECOSTRESS has now successfully returned to 5-band mode after being in 3-band mode since 2019. This feature was successfully enabled following a Data Processing Unit firmware update (version 4.1) to the payload on April 28, 2023. To better balance contiguous science data scene variables, 3-band collection is currently being interleaved with 5-band acquisitions over the orbital day/night periods.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FECOSTRESS%2FECO_L2T_LSTE.002",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FECOSTRESS%2FECO_L2T_LSTE.002",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=C2076090826-LPCLOUD",
-                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=C2076090826-LPCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/ECOSTRESS/ECO_L2T_LSTE.002",
-                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
+                    "downloadURL": "https://doi.org/10.5067/ECOSTRESS/ECO_L2T_LSTE.002",
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
-                    "downloadURL": "https://lpdaac.usgs.gov/documents/1324/ECO2_LSTE_ATBD_V1.pdf",
-                    "description": "The ATBD provides physical theory and mathematical procedures for the calculations used to produce the data products.",
                     "@type": "dcat:Distribution",
+                    "description": "The ATBD provides physical theory and mathematical procedures for the calculations used to produce the data products.",
+                    "downloadURL": "https://lpdaac.usgs.gov/documents/1324/ECO2_LSTE_ATBD_V1.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's algorithm theoretical basis document"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://data.lpdaac.earthdatacloud.nasa.gov/lp-prod-public/ECO_L2T_LSTE.002/ECOv002_L2T_LSTE_21247_032_19MCN_20220405T135253_0700_01/ECOv002_L2T_LSTE_21247_032_19MCN_20220405T135253_0700_01.png",
-                    "description": "Browse image for Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse image for Earthdata Search",
+                    "downloadURL": "https://data.lpdaac.earthdatacloud.nasa.gov/lp-prod-public/ECO_L2T_LSTE.002/ECOv002_L2T_LSTE_21247_032_19MCN_20220405T135253_0700_01/ECOv002_L2T_LSTE_21247_032_19MCN_20220405T135253_0700_01.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://lpdaac.usgs.gov/documents/380/ECO2_PSD_V1.pdf",
-                    "description": "The Product Specification Document (PSD) describes the format and contents of the ECOSTRESS product.",
                     "@type": "dcat:Distribution",
+                    "description": "The Product Specification Document (PSD) describes the format and contents of the ECOSTRESS product.",
+                    "downloadURL": "https://lpdaac.usgs.gov/documents/380/ECO2_PSD_V1.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://lpdaac.usgs.gov/documents/299/ECO2_ASD_V1.pdf",
-                    "description": "The Algorithm Specification Document (ASD) describes the computer processing used to generate the ECOSTRESS products.",
                     "@type": "dcat:Distribution",
+                    "description": "The Algorithm Specification Document (ASD) describes the computer processing used to generate the ECOSTRESS products.",
+                    "downloadURL": "https://lpdaac.usgs.gov/documents/299/ECO2_ASD_V1.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View the documentation for this dataset's algorithms"
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
-                    "downloadURL": "https://lpdaac-ops.cr.usgs.gov/documents/1574/ECOL2_User_Guide_V2.pdf",
-                    "description": "The quality information in the ECO_L2_LSTE User's Guide enables users to interpret and use the data products.",
                     "@type": "dcat:Distribution",
+                    "description": "The quality information in the ECO_L2_LSTE User's Guide enables users to interpret and use the data products.",
+                    "downloadURL": "https://lpdaac-ops.cr.usgs.gov/documents/1574/ECOL2_User_Guide_V2.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
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
-                    "downloadURL": "https://ecostress.jpl.nasa.gov/science",
-                    "description": "The ECOSTRESS website provides detailed information on the mission, instruments, products, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "The ECOSTRESS website provides detailed information on the mission, instruments, products, etc.",
+                    "downloadURL": "https://ecostress.jpl.nasa.gov/science",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 }
             ],
+            "graphic-preview-description": "Browse image for Earthdata Search",
+            "graphic-preview-file": "https://data.lpdaac.earthdatacloud.nasa.gov/lp-prod-public/ECO_L2T_LSTE.002/ECOv002_L2T_LSTE_21247_032_19MCN_20220405T135253_0700_01/ECOv002_L2T_LSTE_21247_032_19MCN_20220405T135253_0700_01.png",
+            "identifier": "C2076090826-LPCLOUD",
+            "issued": "2022-11-14",
+            "keyword": [
+                "earth science",
+                "surface thermal properties",
+                "surface radiative properties",
+                "land surface"
+            ],
+            "landingPage": "https://doi.org/10.5067/ECOSTRESS/ECO_L2T_LSTE.002",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2022-11-14",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "LP DAAC"
+            },
+            "release-place": "Sioux Falls, South Dakota, USA",
             "spatial": "-180.0 -54.0 180.0 54.0",
+            "temporal": "2018-07-09T00:00:00Z/2024-06-03T00:00:00Z",
             "theme": [
                 "ECOSTRESS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "ECOSTRESS Tiled Land Surface Temperature and Emissivity Instantaneous L2 Global 70 m V002"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/S3B/OLCI/L2/ILW/4",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/GSFC/SED/ESD/GCDC/OB.DAAC. https://doi.org/10.5067/S3B/OLCI/L2/ILW/4.",
-            "issued": "2022-09-13",
-            "temporal": "2018-04-25T00:00:00Z/2024-05-06T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-04-26",
-            "keyword": [
-                "bacteria/archaea",
-                "terrestrial hydrosphere",
-                "earth science services",
-                "surface water",
-                "oceans",
-                "ocean optics",
-                "water quality/water chemistry",
-                "marine environment monitoring",
-                "aquatic sciences",
-                "biological classification",
-                "biosphere",
-                "hydrological advisories",
-                "human dimensions",
-                "environmental governance/management",
-                "environmental advisories",
-                "ecosystems",
-                "coastal processes",
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
-            "identifier": "C2954424200-OB_DAAC",
             "description": "The Inland Waters dataset (ILW) provides data for lakes and other water bodies  across the contiguous United States (CONUS) and Alaska. ILW significantly  reduces the processing effort required by end users and is a standardized  community resource for lake and reservoir algorithm development and  performance assessment. The data is provided for 15,450 CONUS waterbodies with  a size of at least one 300 m pixel and over 2,300 resolvable lakes with sizes  greater than three 300 m pixels. Alaska has 5,874 lakes resolvable lakes. ILW  was developed in collaboration with the Cyanobacteria Assessment Network (CyAN).  Additional inland water details and resources, including maps of resolvable lakes  and additional inland water products, such as true color imagery, are available  at the CyAN site.",
-            "title": "Sentinel-3B OLCI Inland Waters (ILW) Data, version 4",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FS3B%2FOLCI%2FL2%2FILW%2F4",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FS3B%2FOLCI%2FL2%2FILW%2F4",
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
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/data/10.5067/S3B/OLCI/L2/ILW/4",
-                    "description": "OLCI-Sentinel-3B 2 Inland Waters (ILW) Dataset Landing Page",
                     "@type": "dcat:Distribution",
+                    "description": "OLCI-Sentinel-3B 2 Inland Waters (ILW) Dataset Landing Page",
+                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/data/10.5067/S3B/OLCI/L2/ILW/4",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 }
             ],
+            "identifier": "C2954424200-OB_DAAC",
+            "issued": "2022-09-13",
+            "keyword": [
+                "bacteria/archaea",
+                "terrestrial hydrosphere",
+                "earth science services",
+                "surface water",
+                "oceans",
+                "ocean optics",
+                "water quality/water chemistry",
+                "marine environment monitoring",
+                "aquatic sciences",
+                "biological classification",
+                "biosphere",
+                "hydrological advisories",
+                "human dimensions",
+                "environmental governance/management",
+                "environmental advisories",
+                "ecosystems",
+                "coastal processes",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/S3B/OLCI/L2/ILW/4",
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
+            "temporal": "2018-04-25T00:00:00Z/2024-05-06T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Sentinel-3B OLCI Inland Waters (ILW) Data, version 4"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-A%2FCAL-ALICE-4-AST1-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This data set contains CODMAC level 4 data acquired by the Rosetta Orbiter ALICE UV Spectrometer during the fly-by of the asteroid (2867) Steins, which occurred on 2008-09-05.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-a-cal-alice-4-ast1-v1.0_whns-7vje",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "calibration",
                 "2867 steins",
                 "international rosetta mission"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-A%2FCAL-ALICE-4-AST1-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-a-cal-alice-4-ast1-v1.0_whns-7vje",
-            "description": "This data set contains CODMAC level 4 data acquired by the Rosetta Orbiter ALICE UV Spectrometer during the fly-by of the asteroid (2867) Steins, which occurred on 2008-09-05.",
-            "title": "ROSETTA-ORBITER STEINS/CAL ALICE 4 AST1 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER STEINS/CAL ALICE 4 AST1 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ASDC_DAAC/LASE/0001",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "1999-10-15. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/ASDC_DAAC/LASE/0001. http://eosweb.larc.nasa.gov/project/lase/lase_table.",
-            "issued": "1999-10-15",
-            "temporal": "1996-07-14T00:00:00Z/1996-07-26T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2018-07-03",
-            "keyword": [
-                "atmospheric water vapor",
-                "earth science",
-                "aerosols",
-                "atmosphere"
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
-            "identifier": "C1535871073-LARC_ASDC",
             "description": "The Lidar Atmospheric Sensing Experiment (LASE) Tropospheric Aerosol Radiative Forcing Observational Experiment (TARFOX) data set was collected over the Western Atlantic Ocean in July 1996. The overall goal of TARFOX was to reduce uncertainties in the effects of aerosols on climate by determining the direct radiative impacts, as well as the chemical, physical, and optical properties, of the aerosols carried over the western Atlantic Ocean from the United States.LASE is an airborne autonomous DIAL system which produces measurements of aerosols and water vapor vertical profiles from the aircraft altitude down to the surface. Such profiles show the vertical context in which the TARFOX in situ and radiometric measurements are made, thus supporting the vertical extension of the in situ measurements and detecting any unsampled layers or inhomogeneities, which would impact the airborne and satellite radiative flux measurements.Note that the LASE_TARFOX data set is also available under the TARFOX project as the TARFOX_LASE data set. The data files included in these two data sets are identical.",
-            "title": "Lidar Atmospheric Sensing Experiment (LASE) Data Obtained During the Tropospheric Aerosol Radiative Forcing Observational Experiment (TARFOX)",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC_DAAC%2FLASE%2F0001",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC_DAAC%2FLASE%2F0001",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
@@ -1575805,509 +1575785,504 @@
                     "title": "View this dataset's product usage"
                 }
             ],
+            "identifier": "C1535871073-LARC_ASDC",
+            "issued": "1999-10-15",
+            "keyword": [
+                "atmospheric water vapor",
+                "earth science",
+                "aerosols",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.5067/ASDC_DAAC/LASE/0001",
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
             "spatial": "-77.4 32.1 -64.5 39.4",
+            "temporal": "1996-07-14T00:00:00Z/1996-07-26T23:59:59Z",
             "theme": [
                 "LASE",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Lidar Atmospheric Sensing Experiment (LASE) Data Obtained During the Tropospheric Aerosol Radiative Forcing Observational Experiment (TARFOX)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/CYGNS-L3C11",
             "citation": "CYGNSS. 2021-02-05. CYGNSS Level 3 Climate Data Record. Version 1.1. CYGNSS Level 3 Climate Data Record Version 1.1. PO.DAAC. Archived by National Aeronautics and Space Administration, U.S. Government, PO.DAAC. https://doi.org/10.5067/CYGNS-L3C11. https://cygnss.engin.umich.edu/. CYGNSS, PO.DAAC, 2021-02-05, CYGNSS Level 3 Climate Data Record Version 1.1, https://cygnss.engin.umich.edu/.",
-            "issued": "2020-12-16",
-            "temporal": "2018-08-01T00:00:00Z/2023-03-01T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-12-16",
-            "references": [
-                "https://doi.org/10.1038/s41598-018-27127-4"
-            ],
-            "keyword": [
-                "oceans",
-                "ocean winds",
-                "earth science"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "undefined",
                 "hasEmail": "mailto:podaac@podaac.jpl.nasa.gov"
             },
-            "identifier": "C2205121540-POCLOUD",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/JPL/PODAAC"
-            },
-            "description": "This dataset contains the Version 1.1 CYGNSS Level 3 Climate Data Record which provides the average wind speed and mean square slope (MSS) on a 0.2x0.2 degree latitude by longitude equirectangular grid obtained from the Delay Doppler Mapping Instrument aboard the CYGNSS satellite constellation. The Level 2 Delay Doppler Map (DDM) data are used in the direct processing of the average wind speed and MSS data that are binned on the Level 3 grid. A subset of DDM data used in the direct processing of the average wind speed and MSS is co-located inside of the Level 2 data files. A single netCDF-4 data file is produced for each day of operation with an approximate 1 to 2 month latency. The reported sample locations are determined by the specular points corresponding to the Delay Doppler Maps (DDMs). The Version 1.1 CDR is a collection of reanalysis products derived from the SDR v3.0 Level 1 data (https://doi.org/10.5067/CYGNS-L1X30 ). Calibration accuracy and long term stability are improved relative to SDR v3.0 (https://doi.org/10.5067/CYGNS-L3X30 ) using the same trackwise correction algorithm as was used by CDR v1.0 (https://doi.org/10.5067/CYGNS-L3C10 ), which was derived from SDR v2.1 Level 1 data (https://doi.org/10.5067/CYGNS-L1X21 ). Details of the algorithm are provided in the Trackwise Corrected CDR Algorithm Theoretical Basis Document. CDR Level 2 and 3 products (ocean surface wind speed, mean square slope, and latent and sensible heat flux) are generated from the CDR L1 data using the v3.0 SDR data processing algorithms. These products also exhibit improved calibration accuracy and stability over SDR v3.0. Trackwise correction is applied to the two primary CYGNSS L1 science data products, the normalized bistatic radar cross section (NBRCS) and the leading edge slope of the Doppler-integrated delay waveform (LES). The correction compensates for small errors in the Level 1 calibration, due e.g. to uncertainties in the GPS transmitting antenna gain patterns and the CYGNSS receiving antenna gain patterns. CDR v1.1 does not include a Young Seas with Limited Fetch (YSLF) wind speed product and investigators requiring wind speed measurements in and near the inner core of tropical cyclones should use the SDR v3.0 YSLF wind speed product. A YSLF wind speed product is omitted because the trackwise correction algorithm, which constrains the average value of the L1 data using MERRA-2 reanalysis wind speeds, is inherently biased toward fully developed sea state conditions. The constraint improves wind speed retrieval performance in fully developed seas but produces underestimates in YSLF conditions. It should also be noted that the trackwise correction algorithm cannot be successfully applied to all SDR v3.0 L1 data so there is also some loss of samples that were present in SDR v3.0.",
-            "release-place": "PO.DAAC",
-            "series-name": "CYGNSS Level 3 Climate Data Record",
             "creator": "CYGNSS",
-            "title": "CYGNSS Level 3 Climate Data Record Version 1.1",
-            "graphic-preview-description": "Thumbnail",
-            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/CYGNSS_L3_CDR_V1.1.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "This dataset contains the Version 1.1 CYGNSS Level 3 Climate Data Record which provides the average wind speed and mean square slope (MSS) on a 0.2x0.2 degree latitude by longitude equirectangular grid obtained from the Delay Doppler Mapping Instrument aboard the CYGNSS satellite constellation. The Level 2 Delay Doppler Map (DDM) data are used in the direct processing of the average wind speed and MSS data that are binned on the Level 3 grid. A subset of DDM data used in the direct processing of the average wind speed and MSS is co-located inside of the Level 2 data files. A single netCDF-4 data file is produced for each day of operation with an approximate 1 to 2 month latency. The reported sample locations are determined by the specular points corresponding to the Delay Doppler Maps (DDMs). The Version 1.1 CDR is a collection of reanalysis products derived from the SDR v3.0 Level 1 data (https://doi.org/10.5067/CYGNS-L1X30 ). Calibration accuracy and long term stability are improved relative to SDR v3.0 (https://doi.org/10.5067/CYGNS-L3X30 ) using the same trackwise correction algorithm as was used by CDR v1.0 (https://doi.org/10.5067/CYGNS-L3C10 ), which was derived from SDR v2.1 Level 1 data (https://doi.org/10.5067/CYGNS-L1X21 ). Details of the algorithm are provided in the Trackwise Corrected CDR Algorithm Theoretical Basis Document. CDR Level 2 and 3 products (ocean surface wind speed, mean square slope, and latent and sensible heat flux) are generated from the CDR L1 data using the v3.0 SDR data processing algorithms. These products also exhibit improved calibration accuracy and stability over SDR v3.0. Trackwise correction is applied to the two primary CYGNSS L1 science data products, the normalized bistatic radar cross section (NBRCS) and the leading edge slope of the Doppler-integrated delay waveform (LES). The correction compensates for small errors in the Level 1 calibration, due e.g. to uncertainties in the GPS transmitting antenna gain patterns and the CYGNSS receiving antenna gain patterns. CDR v1.1 does not include a Young Seas with Limited Fetch (YSLF) wind speed product and investigators requiring wind speed measurements in and near the inner core of tropical cyclones should use the SDR v3.0 YSLF wind speed product. A YSLF wind speed product is omitted because the trackwise correction algorithm, which constrains the average value of the L1 data using MERRA-2 reanalysis wind speeds, is inherently biased toward fully developed sea state conditions. The constraint improves wind speed retrieval performance in fully developed seas but produces underestimates in YSLF conditions. It should also be noted that the trackwise correction algorithm cannot be successfully applied to all SDR v3.0 L1 data so there is also some loss of samples that were present in SDR v3.0.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FCYGNS-L3C11",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FCYGNS-L3C11",
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
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/cygnss/open/L3/docs/148-0390-2_L3_v1.1_CDR_netCDF_Data_Dictionary.xlsx",
-                    "description": "Look-up table to define the Level 3 data variables",
                     "@type": "dcat:Distribution",
+                    "description": "Look-up table to define the Level 3 data variables",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/cygnss/open/L3/docs/148-0390-2_L3_v1.1_CDR_netCDF_Data_Dictionary.xlsx",
+                    "mediaType": "text/html",
                     "title": "View this dataset's user's guide"
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
-                    "downloadURL": "https://doi.org/10.1175/BAMS-D-18-0337.1",
-                    "description": "Ruf, C., S. Asharaf, R. Balasubramaniam, S. Gleason, T. Lang, D. McKague, D. Twigg, and D. Waliser. (2019). In-Orbit Performance of the Constellation of CYGNSS Hurricane Satellites. Bull. Amer. Meteor. Soc., 100, 2009 - 2023, https://doi.org/10.1175/BAMS-D-18-0337.1.",
                     "@type": "dcat:Distribution",
+                    "description": "Ruf, C., S. Asharaf, R. Balasubramaniam, S. Gleason, T. Lang, D. McKague, D. Twigg, and D. Waliser. (2019). In-Orbit Performance of the Constellation of CYGNSS Hurricane Satellites. Bull. Amer. Meteor. Soc., 100, 2009 - 2023, https://doi.org/10.1175/BAMS-D-18-0337.1.",
+                    "downloadURL": "https://doi.org/10.1175/BAMS-D-18-0337.1",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/cygnss/open/L3/docs/148-0319_ATBD_L3_Gridded_Wind_Speed_Rev1_Aug2018_release.pdf",
-                    "description": "Level 3 Gridded Wind Speed Algorithm Theoretical Basis Document, C. Ruf, CYGNSS Project Document 148-0319, Rev 1, 20 Aug. 2018.",
                     "@type": "dcat:Distribution",
+                    "description": "Level 3 Gridded Wind Speed Algorithm Theoretical Basis Document, C. Ruf, CYGNSS Project Document 148-0319, Rev 1, 20 Aug. 2018.",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/cygnss/open/L3/docs/148-0319_ATBD_L3_Gridded_Wind_Speed_Rev1_Aug2018_release.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's algorithm theoretical basis document"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://cygnss.engin.umich.edu/",
-                    "description": "CYGNSS Mission Page at University of Michigan",
                     "@type": "dcat:Distribution",
+                    "description": "CYGNSS Mission Page at University of Michigan",
+                    "downloadURL": "https://cygnss.engin.umich.edu/",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/cygnss/open/L3/docs/148-0389-1_ATBD_Trackwise_Corrected_CDR.pdf",
-                    "description": "Algorithm Theoretical Basis Document (ATBD) for the CYGNSS Climate Data Record (CDR)",
                     "@type": "dcat:Distribution",
+                    "description": "Algorithm Theoretical Basis Document (ATBD) for the CYGNSS Climate Data Record (CDR)",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/cygnss/open/L3/docs/148-0389-1_ATBD_Trackwise_Corrected_CDR.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's algorithm theoretical basis document"
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
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/CYGNSS_L3_CDR_V1.1.jpg",
-                    "description": "Thumbnail",
                     "@type": "dcat:Distribution",
+                    "description": "Thumbnail",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/CYGNSS_L3_CDR_V1.1.jpg",
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
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2205121540-POCLOUD",
-                    "description": "HTTPS endpoint for data browse and download",
                     "@type": "dcat:Distribution",
+                    "description": "HTTPS endpoint for data browse and download",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2205121540-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2205121540-POCLOUD",
-                    "description": "Browse granule search results in Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse granule search results in Earthdata Search",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2205121540-POCLOUD",
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
-                    "mediaType": "text/html",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/cygnss/open/L1/docs/att_tables/Attitude_Table_FM_1.txt",
-                    "description": "Updated Monthly",
                     "@type": "dcat:Distribution",
+                    "description": "Updated Monthly",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/cygnss/open/L1/docs/att_tables/Attitude_Table_FM_1.txt",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/cygnss/open/L1/docs/att_tables/Attitude_Table_FM_2.txt",
-                    "description": "Updated Monthly",
                     "@type": "dcat:Distribution",
+                    "description": "Updated Monthly",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/cygnss/open/L1/docs/att_tables/Attitude_Table_FM_2.txt",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/cygnss/open/L1/docs/att_tables/Attitude_Table_FM_3.txt",
-                    "description": "Updated Monthly",
                     "@type": "dcat:Distribution",
+                    "description": "Updated Monthly",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/cygnss/open/L1/docs/att_tables/Attitude_Table_FM_3.txt",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/cygnss/open/L1/docs/att_tables/Attitude_Table_FM_4.txt",
-                    "description": "Updated Monthly",
                     "@type": "dcat:Distribution",
+                    "description": "Updated Monthly",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/cygnss/open/L1/docs/att_tables/Attitude_Table_FM_4.txt",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/cygnss/open/L1/docs/att_tables/Attitude_Table_FM_5.txt",
-                    "description": "Updated Monthly",
                     "@type": "dcat:Distribution",
+                    "description": "Updated Monthly",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/cygnss/open/L1/docs/att_tables/Attitude_Table_FM_5.txt",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/cygnss/open/L1/docs/att_tables/Attitude_Table_FM_6.txt",
-                    "description": "Updated Monthly",
                     "@type": "dcat:Distribution",
+                    "description": "Updated Monthly",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/cygnss/open/L1/docs/att_tables/Attitude_Table_FM_6.txt",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/cygnss/open/L1/docs/att_tables/Attitude_Table_FM_7.txt",
-                    "description": "Updated Monthly",
                     "@type": "dcat:Distribution",
+                    "description": "Updated Monthly",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/cygnss/open/L1/docs/att_tables/Attitude_Table_FM_7.txt",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/cygnss/open/L1/docs/att_tables/Attitude_Table_FM_8.txt",
-                    "description": "Updated Monthly",
                     "@type": "dcat:Distribution",
+                    "description": "Updated Monthly",
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
+            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/CYGNSS_L3_CDR_V1.1.jpg",
+            "identifier": "C2205121540-POCLOUD",
+            "issued": "2020-12-16",
+            "keyword": [
+                "oceans",
+                "ocean winds",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/CYGNS-L3C11",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2020-12-16",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/JPL/PODAAC"
+            },
+            "references": [
+                "https://doi.org/10.1038/s41598-018-27127-4"
+            ],
+            "release-place": "PO.DAAC",
+            "series-name": "CYGNSS Level 3 Climate Data Record",
             "spatial": "-180.0 -40.0 180.0 40.0",
+            "temporal": "2018-08-01T00:00:00Z/2023-03-01T00:00:00Z",
             "theme": [
                 "CYGNSS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "CYGNSS Level 3 Climate Data Record Version 1.1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=JNO-J-JIRAM-3-RDR-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This dataset contains the                scientific telemetry produced by the JIRAM                 instrument , together with geometric                       information computed on ground to locate                   observations in space and time.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.jno-j-jiram-3-rdr-v1.0_whs6-4skc",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "juno",
                 "jupiter",
                 "io"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=JNO-J-JIRAM-3-RDR-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.jno-j-jiram-3-rdr-v1.0_whs6-4skc",
-            "description": "This dataset contains the                scientific telemetry produced by the JIRAM                 instrument , together with geometric                       information computed on ground to locate                   observations in space and time.",
-            "title": "JUNO JUPITER JIRAM REDUCED DATA         \n                                      RECORD V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "JUNO JUPITER JIRAM REDUCED DATA         \n                                      RECORD V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/SMP60-2SNRT",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Remote Sensing Systems (RSS). 2024-02-29. RSS SMAP Level 2C Sea Surface Validated Dataset. Version 6.0. SMAP Sea Surface Salinity Products. Remote Sensing Systems, 444 Tenth Street, Suite 200, Santa Rosa, CA 95401, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Remote Sensing Systems (RSS). https://doi.org/10.5067/SMP60-2SNRT. http://podaac.jpl.nasa.gov/smap. Remote Sensing Systems (RSS), Remote Sensing Systems (RSS), 2022-02-25, RSS SMAP Level 2C Sea Surface Salinity V5.0 Validated Dataset, http://podaac.jpl.nasa.gov/smap.",
-            "issued": "2021-01-13",
-            "temporal": "2022-07-28T00:00:00Z/2024-03-27T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2021-01-13",
-            "keyword": [
-                "oceans",
-                "earth science",
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
-            "identifier": "C2832224417-POCLOUD",
-            "description": "The SMAP-SSS level 2C near real-time (NRT) V6.0 dataset produced by the Remote Sensing Systems (RSS) and sponsored by the NASA Ocean Salinity Science Team, is a validated product that provides near real-time orbital/swath data on sea surface salinity (SSS) derived from the NASA's Soil Moisture Active Passive (SMAP) mission. SMAP, launched on January 31, 2015, was initially designed to measure and map Earth's soil moisture and freeze/thaw state to better understand terrestrial water, carbon and energy cycles, and has been adapted to measure ocean SSS and ocean wind speed using its passive microwave instrument.  The SMAP instrument is in a near polar orbiting,  sun synchronous orbit with a nominal 8 day repeat cycle. \r\n<br><br>\r\nThe dataset includes derived SMAP SSS, SSS uncertainty using the NRT SMAP Salinity Retrieval Algorithm, top of atmosphere brightness temperature (TB), wind speed and direction data for extreme winds, and other all necessary ancillary data and the results of all intermediate steps. The observations are global, provided on a 0.25&deg; fixed Earth grid with an approximate spatial resolution of 70 km. The major changes in Version 6.0 from Version 5.0 are: (1) Removal of biases during the first few months of the SMAP mission that are related to the operation of the SMAP radar during that time. (2) Mitigation of biases that depend on the SMAP look angle. (3) Mitigation of salty biases at high Northern latitudes. (4) Revised sun-glint flag. Each data file covers one 98-minute orbit (15 files per day), is available in netCDF-4 file format with about 5 hours l\r\natency.\r\n<br><br>\r\nThis RSS SMAP-SSS V6.0 NRT dataset holds tremendous potential for scientific research and various applications. Given the SMAP satellite's near-polar orbit and sun-synchronous nature with its 1000km swath, it achieves global coverage in approximately three days, enabling researchers to monitor and model global oceanic and climatic phenomena with unprecedented detail and timeliness. These data can inform and enhance understanding of global weather patterns, the Earth\u2019s hydrological cycle, ocean circulation, and climate change.",
-            "release-place": "Remote Sensing Systems, 444 Tenth Street, Suite 200, Santa Rosa, CA 95401, USA",
-            "series-name": "RSS SMAP Level 2C Sea Surface Validated Dataset",
-            "graphic-preview-description": "Thumbnail",
             "creator": "Remote Sensing Systems (RSS)",
-            "title": "RSS SMAP Level 2C Sea Surface Salinity NRT V6.0 Validated Dataset",
-            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/SMAP_RSS_L2_SSS_NRT_V6.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The SMAP-SSS level 2C near real-time (NRT) V6.0 dataset produced by the Remote Sensing Systems (RSS) and sponsored by the NASA Ocean Salinity Science Team, is a validated product that provides near real-time orbital/swath data on sea surface salinity (SSS) derived from the NASA's Soil Moisture Active Passive (SMAP) mission. SMAP, launched on January 31, 2015, was initially designed to measure and map Earth's soil moisture and freeze/thaw state to better understand terrestrial water, carbon and energy cycles, and has been adapted to measure ocean SSS and ocean wind speed using its passive microwave instrument.  The SMAP instrument is in a near polar orbiting,  sun synchronous orbit with a nominal 8 day repeat cycle. \r\n<br><br>\r\nThe dataset includes derived SMAP SSS, SSS uncertainty using the NRT SMAP Salinity Retrieval Algorithm, top of atmosphere brightness temperature (TB), wind speed and direction data for extreme winds, and other all necessary ancillary data and the results of all intermediate steps. The observations are global, provided on a 0.25&deg; fixed Earth grid with an approximate spatial resolution of 70 km. The major changes in Version 6.0 from Version 5.0 are: (1) Removal of biases during the first few months of the SMAP mission that are related to the operation of the SMAP radar during that time. (2) Mitigation of biases that depend on the SMAP look angle. (3) Mitigation of salty biases at high Northern latitudes. (4) Revised sun-glint flag. Each data file covers one 98-minute orbit (15 files per day), is available in netCDF-4 file format with about 5 hours l\r\natency.\r\n<br><br>\r\nThis RSS SMAP-SSS V6.0 NRT dataset holds tremendous potential for scientific research and various applications. Given the SMAP satellite's near-polar orbit and sun-synchronous nature with its 1000km swath, it achieves global coverage in approximately three days, enabling researchers to monitor and model global oceanic and climatic phenomena with unprecedented detail and timeliness. These data can inform and enhance understanding of global weather patterns, the Earth\u2019s hydrological cycle, ocean circulation, and climate change.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSMP60-2SNRT",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSMP60-2SNRT",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/smap/open/docs/V6/ATBD_EOM_final.pdf",
-                    "description": "SMAP-SSS V6.0 Technical Guide (ATBD, Validation Analysis, Product Format Specification)",
                     "@type": "dcat:Distribution",
+                    "description": "SMAP-SSS V6.0 Technical Guide (ATBD, Validation Analysis, Product Format Specification)",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/smap/open/docs/V6/ATBD_EOM_final.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://images.remss.com/figures/missions/smap/bad_orbits.txt",
-                    "description": "Dynamically updated RSS webpage listing L2 files with Bad Orbits",
                     "@type": "dcat:Distribution",
+                    "description": "Dynamically updated RSS webpage listing L2 files with Bad Orbits",
+                    "downloadURL": "http://images.remss.com/figures/missions/smap/bad_orbits.txt",
+                    "mediaType": "text/html",
                     "title": "View this dataset's documented anomalies"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://smap.jpl.nasa.gov/",
-                    "description": "NASA SMAP Mission Website",
                     "@type": "dcat:Distribution",
+                    "description": "NASA SMAP Mission Website",
+                    "downloadURL": "https://smap.jpl.nasa.gov/",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/aquarius/open/README.KnownIssues.txt",
-                    "description": "Information on Data Outages & Known Issues",
                     "@type": "dcat:Distribution",
+                    "description": "Information on Data Outages & Known Issues",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/aquarius/open/README.KnownIssues.txt",
+                    "mediaType": "text/html",
                     "title": "View this dataset's documented anomalies"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://www.remss.com/missions/smap",
-                    "description": "Remote Sensing Systems SMAP Sea Surface Salinity Website",
                     "@type": "dcat:Distribution",
+                    "description": "Remote Sensing Systems SMAP Sea Surface Salinity Website",
+                    "downloadURL": "http://www.remss.com/missions/smap",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/SMAP_RSS_L2_SSS_NRT_V6.jpg",
-                    "description": "Thumbnail",
                     "@type": "dcat:Distribution",
+                    "description": "Thumbnail",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/SMAP_RSS_L2_SSS_NRT_V6.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/smap/open/docs/V6/Release_V6.0.pdf",
-                    "description": "ATBD, Validation Analysis, Product Specifications, etc",
                     "@type": "dcat:Distribution",
+                    "description": "ATBD, Validation Analysis, Product Specifications, etc",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/smap/open/docs/V6/Release_V6.0.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://images.remss.com/figures/missions/smap/bad_ancillaries.txt",
-                    "description": "Dynamically updated RSS webpage listing L2 files with missing ancillary inputs",
                     "@type": "dcat:Distribution",
+                    "description": "Dynamically updated RSS webpage listing L2 files with missing ancillary inputs",
+                    "downloadURL": "http://images.remss.com/figures/missions/smap/bad_ancillaries.txt",
+                    "mediaType": "text/html",
                     "title": "View this dataset's documented anomalies"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://podaac.jpl.nasa.gov/smap",
-                    "description": "SMAP-SSS Project and Instrument Overview",
                     "@type": "dcat:Distribution",
+                    "description": "SMAP-SSS Project and Instrument Overview",
+                    "downloadURL": "http://podaac.jpl.nasa.gov/smap",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/smap/open/L2/RSS/README.txt",
-                    "description": "Known issues README",
                     "@type": "dcat:Distribution",
+                    "description": "Known issues README",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/smap/open/L2/RSS/README.txt",
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
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2832224417-POCLOUD",
-                    "description": "HTTPS endpoint for data browse and download",
                     "@type": "dcat:Distribution",
+                    "description": "HTTPS endpoint for data browse and download",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2832224417-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2832224417-POCLOUD",
-                    "description": "Browse granule search results in Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse granule search results in Earthdata Search",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2832224417-POCLOUD",
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
                     "@type": "dcat:Distribution",
+                    "description": "Data Subscriber",
                     "downloadURL": "https://github.com/podaac/data-subscriber",
-                    "mediaType": "text/html",
-                    "description": "Data Subscriber"
+                    "mediaType": "text/html"
                 }
             ],
+            "graphic-preview-description": "Thumbnail",
+            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/SMAP_RSS_L2_SSS_NRT_V6.jpg",
+            "identifier": "C2832224417-POCLOUD",
+            "issued": "2021-01-13",
+            "keyword": [
+                "oceans",
+                "earth science",
+                "salinity/density"
+            ],
+            "landingPage": "https://doi.org/10.5067/SMP60-2SNRT",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2021-01-13",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/JPL/PODAAC"
+            },
+            "release-place": "Remote Sensing Systems, 444 Tenth Street, Suite 200, Santa Rosa, CA 95401, USA",
+            "series-name": "RSS SMAP Level 2C Sea Surface Validated Dataset",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2022-07-28T00:00:00Z/2024-03-27T00:00:00Z",
             "theme": [
                 "SMAP",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "RSS SMAP Level 2C Sea Surface Salinity NRT V6.0 Validated Dataset"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-3-RDR-NEO-LIGHTCURVES-V1.0",
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
+            "description": "This data set contains photometric lightcurves of near-earth asteroids obtained by Petr Pravec and his collaborators at Ondrejov Observatory. Lightcurves for 42 asteroids are included. These asteroids were included based on a slightly wider criterion for a NEA: q < 1.33 AU (rather than the standard definition of q < 1.3 AU). As a result, some asteroids may be included which other researchers would classify as Mars-crossers.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-3-rdr-neo-lightcurves-v1.0_whyz-6jfp",
+            "issued": "2018-06-26",
+            "keyword": [
+                "asteroid",
+                "support archives"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-3-RDR-NEO-LIGHTCURVES-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-3-rdr-neo-lightcurves-v1.0_whyz-6jfp",
-            "description": "This data set contains photometric lightcurves of near-earth asteroids obtained by Petr Pravec and his collaborators at Ondrejov Observatory. Lightcurves for 42 asteroids are included. These asteroids were included based on a slightly wider criterion for a NEA: q < 1.33 AU (rather than the standard definition of q < 1.3 AU). As a result, some asteroids may be included which other researchers would classify as Mars-crossers.",
-            "title": "NEAR EARTH ASTEROID LIGHTCURVES V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "NEAR EARTH ASTEROID LIGHTCURVES V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/6K2DW26DXETZ",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Jianxiong Sheng & Daniel Jacob. 2016-06-26. CMS_CH4_FLX_CA. Version 1. Methane (CH4) Flux for Canadian Oil/Gas Systems L4 V1. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/6K2DW26DXETZ. https://disc.gsfc.nasa.gov/datacollection/CMS_CH4_FLX_CA_1.html.",
-            "issued": "2013-01-01",
-            "temporal": "2013-01-01T00:00:00Z/2014-01-01T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2014-01-01",
-            "references": [
-                "https://doi.org/10.1016/j.atmosenv.2017.02.036"
-            ],
-            "keyword": [
-                "atmosphere",
-                "earth science",
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
-            "identifier": "C1405716389-GES_DISC",
-            "description": "This data set (CMS_CH4_FLX_CA) contains the yearly average methane (CH4) flux for Canada's oil and gas systems based on a bottom up calculation of oil/gas emissions reported by ICF International in 2013.  A related data set (CMS_CH4_FLX_MX) contains the yearly average methane (CH4) flux for Mexico's oil and gas systems based on a bottom up calculation of oil/gas emissions reported by the Mexican Petrolium Institute in 2010.  The Canadian emissions are concentrated in Alberta (gas production and processing) and the Mexican emissions are concentrated along the east coast (oil production).  More details about the observations, algorithm, and scientific findings are described in Sheng et al. 2017.\n\nThe NASA Carbon Monitoring System (CMS) is designed to make significant contributions in characterizing, quantifying, understanding, and predicting the evolution of global carbon sources and sinks through improved monitoring of carbon stocks and fluxes. The System will use the full range of NASA satellite observations and modeling/analysis capabilities to establish the accuracy, quantitative uncertainties, and utility of products for supporting national and international policy, regulatory, and management activities. CMS will maintain a global emphasis while providing finer scale regional information, utilizing space-based and surface-based data and will rapidly initiate generation and distribution of products both for user evaluation and to inform near-term policy development and planning.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "CMS_CH4_FLX_CA",
             "creator": "Jianxiong Sheng & Daniel Jacob",
-            "title": "Methane (CH4) Flux for Canadian Oil/Gas Systems L4 V1 (CMS_CH4_FLX_CA) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/CMS/CMS_CH4_FLX_CA.png",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "This data set (CMS_CH4_FLX_CA) contains the yearly average methane (CH4) flux for Canada's oil and gas systems based on a bottom up calculation of oil/gas emissions reported by ICF International in 2013.  A related data set (CMS_CH4_FLX_MX) contains the yearly average methane (CH4) flux for Mexico's oil and gas systems based on a bottom up calculation of oil/gas emissions reported by the Mexican Petrolium Institute in 2010.  The Canadian emissions are concentrated in Alberta (gas production and processing) and the Mexican emissions are concentrated along the east coast (oil production).  More details about the observations, algorithm, and scientific findings are described in Sheng et al. 2017.\n\nThe NASA Carbon Monitoring System (CMS) is designed to make significant contributions in characterizing, quantifying, understanding, and predicting the evolution of global carbon sources and sinks through improved monitoring of carbon stocks and fluxes. The System will use the full range of NASA satellite observations and modeling/analysis capabilities to establish the accuracy, quantitative uncertainties, and utility of products for supporting national and international policy, regulatory, and management activities. CMS will maintain a global emphasis while providing finer scale regional information, utilizing space-based and surface-based data and will rapidly initiate generation and distribution of products both for user evaluation and to inform near-term policy development and planning.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2F6K2DW26DXETZ",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2F6K2DW26DXETZ",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
@@ -1576317,319 +1576292,320 @@
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/CMS_CH4_FLX_CA_1.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/CMS_CH4_FLX_CA_1.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://acdisc.gsfc.nasa.gov/data/CMS/CMS_CH4_FLX_CA.1/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://acdisc.gsfc.nasa.gov/data/CMS/CMS_CH4_FLX_CA.1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://acdisc.gsfc.nasa.gov/opendap/CMS/CMS_CH4_FLX_CA.1/",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://acdisc.gsfc.nasa.gov/opendap/CMS/CMS_CH4_FLX_CA.1/",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://acdisc.gsfc.nasa.gov/data/CMS/CMS_CH4_FLX_CA.1/doc/README.CMS_CH4_FLX_CAMX_V1.pdf",
-                    "description": "README Document",
                     "@type": "dcat:Distribution",
+                    "description": "README Document",
+                    "downloadURL": "https://acdisc.gsfc.nasa.gov/data/CMS/CMS_CH4_FLX_CA.1/doc/README.CMS_CH4_FLX_CAMX_V1.pdf",
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
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=CMS_CH4_FLX_CA",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=CMS_CH4_FLX_CA",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 }
             ],
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/CMS/CMS_CH4_FLX_CA.png",
+            "identifier": "C1405716389-GES_DISC",
+            "issued": "2013-01-01",
+            "keyword": [
+                "atmosphere",
+                "earth science",
+                "atmospheric chemistry"
+            ],
+            "landingPage": "https://doi.org/10.5067/6K2DW26DXETZ",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2014-01-01",
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
+            "series-name": "CMS_CH4_FLX_CA",
             "spatial": "-142.05 40.05 -47.05 69.95",
+            "temporal": "2013-01-01T00:00:00Z/2014-01-01T23:59:59.999Z",
             "theme": [
                 "CMS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Methane (CH4) Flux for Canadian Oil/Gas Systems L4 V1 (CMS_CH4_FLX_CA) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/IMPACTS/NEXRAD/DATA103",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Brodzik, Stacy .2022. KBOX NEXRAD IMPACTS [indicate subset used]. Dataset available online from the NASA Global Hydrometeorology Resource Center DAAC, Huntsville, Alabama, U.S.A. DOI: http://dx.doi.org/10.5067/IMPACTS/NEXRAD/DATA103",
-            "issued": "2022-03-23",
-            "temporal": "2020-01-01T00:05:13Z/2020-03-01T00:00:16Z",
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
-            "identifier": "C1995581487-GHRC_DAAC",
             "description": "The KBOX NEXRAD IMPACTS dataset consists of Next Generation Weather Radar (NEXRAD) Level II surveillance data that were collected from January 1 to March 1, 2020 during the Investigation of Microphysics and Precipitation for Atlantic Coast-Threatening Snowstorms  (IMPACTS) field campaign. IMPACTS was a three-year sequence of winter season deployments conducted to study snowstorms over the U.S Atlantic Coast. The campaign aimed to (1) Provide observations critical to understanding the mechanisms of snowband formation, organization, and evolution; (2) Examine how the microphysical characteristics and likely growth mechanisms of snow particles vary across snowbands; and (3) Improve snowfall remote sensing interpretation and modeling to significantly advance prediction capabilities. There are currently 160 Weather Surveillance Radar-1988 Doppler (WSR-88D) or NEXRAD sites throughout the United States and abroad. These Level II datasets contain meteorological and dual-polarization base data quantities including: radar reflectivity, radial velocity, spectrum width, differential reflectivity, differential phase, and cross correlation ratio. The IMPACTS NEXRAD Level II data files are available in netCDF-4 format. It should be noted that this dataset will be updated in subsequent years of the IMPACTS campaign.",
-            "title": "KBOX NEXRAD IMPACTS V1",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FIMPACTS%2FNEXRAD%2FDATA103",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FIMPACTS%2FNEXRAD%2FDATA103",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=kboximpacts",
-                    "description": "Files may be downloaded directly to your workstation from this link",
                     "@type": "dcat:Distribution",
+                    "description": "Files may be downloaded directly to your workstation from this link",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=kboximpacts",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://espo.nasa.gov/impacts",
-                    "description": "IMPACTS Information",
                     "@type": "dcat:Distribution",
+                    "description": "IMPACTS Information",
+                    "downloadURL": "https://espo.nasa.gov/impacts",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.ncdc.noaa.gov/data-access/radar-data/nexrad",
-                    "description": "NEXRAD Radar Information",
                     "@type": "dcat:Distribution",
+                    "description": "NEXRAD Radar Information",
+                    "downloadURL": "https://www.ncdc.noaa.gov/data-access/radar-data/nexrad",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://catalog.data.gov/dataset/noaa-next-generation-radar-nexrad-products",
-                    "description": "NOAA NEXt-Generation RADar (NEXRAD) Products",
                     "@type": "dcat:Distribution",
+                    "description": "NOAA NEXt-Generation RADar (NEXRAD) Products",
+                    "downloadURL": "https://catalog.data.gov/dataset/noaa-next-generation-radar-nexrad-products",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
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
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/impacts/NEXRAD/KBOX/doc/nexrad_datasets.pdf",
-                    "description": "NEXRAD IMPACTS Datasets User Guide",
                     "@type": "dcat:Distribution",
+                    "description": "NEXRAD IMPACTS Datasets User Guide",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/impacts/NEXRAD/KBOX/doc/nexrad_datasets.pdf",
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
+            "identifier": "C1995581487-GHRC_DAAC",
+            "issued": "2022-03-23",
+            "keyword": [
+                "spectral/engineering",
+                "earth science",
+                "radar"
+            ],
+            "landingPage": "https://doi.org/10.5067/IMPACTS/NEXRAD/DATA103",
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
             "spatial": "-76.6945 37.8256 -65.5792 46.086",
+            "temporal": "2020-01-01T00:05:13Z/2020-03-01T00:00:16Z",
             "theme": [
                 "IMPACTS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "KBOX NEXRAD IMPACTS V1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/SENTINEL-3A/OLCI/L3M/ERR/RRS/2022",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/GSFC/SED/ESD/GCDC/OB.DAAC. https://doi.org/10.5067/SENTINEL-3A/OLCI/L3M/ERR/RRS/2022.",
-            "issued": "2022-09-13",
-            "temporal": "2016-04-25T00:00:00Z/2024-04-22T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-04-13",
-            "keyword": [
-                "atmosphere",
-                "ocean optics",
-                "earth science",
-                "atmospheric radiation",
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
-            "identifier": "C2264534426-OB_DAAC",
             "description": "The Ocean and Land Colour Instrument (OLCI) is the successor to ENVISAT's Medium Resolution Imaging Spectrometer (MERIS) having additional spectral channels, different camera arrangements and simplified on-board processing. The OLCI is a push-broom instrument with five camera modules sharing the field of view. The field of view of the five cameras is arranged in a fan-shaped configuration in the vertical plane, perpendicular to the platform velocity. Each camera has an individual field of view of 14.2\u00b0 and a 0.6\u00b0 overlap with its neighbors. The whole field of view is shifted across track by 12.6\u00b0 away from the sun to minimize the impact of sun glint. OLCI is equipped with on-board calibration hardware based on sun diffusers. There are three sun diffusers--two 'white' diffusers dedicated to radiometric calibration and one dedicated to spectral calibration, with spectral reflectance features. The native resolution is approximately 300m, refered to as Full Resolution (FR). A Reduced Resolution (RR) processing mode provides Level-1B data at sampling rates decreased by a factor of four in both spatial dimensions resulting to resolution of approximately 1.2 km.",
-            "title": "Sentinel-3A OLCI Level-3M Global Mapped Earth-observation Reduced Resolution (ERR) Remote-Sensing Reflectance (RRS) Data, version R2022.0",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSENTINEL-3A%2FOLCI%2FL3M%2FERR%2FRRS%2F2022",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSENTINEL-3A%2FOLCI%2FL3M%2FERR%2FRRS%2F2022",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://oceandata.sci.gsfc.nasa.gov/opendap/S3OLCI/",
-                    "description": "OB.DAAC OPeNDAP Site for Sentinel-3A OLCI Standard Mapped Image (SMI) Product",
                     "@type": "dcat:Distribution",
+                    "description": "OB.DAAC OPeNDAP Site for Sentinel-3A OLCI Standard Mapped Image (SMI) Product",
+                    "downloadURL": "https://oceandata.sci.gsfc.nasa.gov/opendap/S3OLCI/",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 }
             ],
+            "identifier": "C2264534426-OB_DAAC",
+            "issued": "2022-09-13",
+            "keyword": [
+                "atmosphere",
+                "ocean optics",
+                "earth science",
+                "atmospheric radiation",
+                "oceans"
+            ],
+            "landingPage": "https://doi.org/10.5067/SENTINEL-3A/OLCI/L3M/ERR/RRS/2022",
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
+            "temporal": "2016-04-25T00:00:00Z/2024-04-22T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Sentinel-3A OLCI Level-3M Global Mapped Earth-observation Reduced Resolution (ERR) Remote-Sensing Reflectance (RRS) Data, version R2022.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://spotthestation.nasa.gov",
+            "accrualPeriodicity": "R/P1D",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2021-07-20",
-            "temporal": "2021-07-20T00:00:00Z/P1D",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-31",
-            "keyword": [
-                "trajectory",
-                "space",
-                "location",
-                "coordinates",
-                "iss",
-                "ephemeris",
-                "coords",
-                "international",
-                "topo",
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
-            "identifier": "nasa-iss-data_2021-07-20_wi7k-iwtn",
+            "dataQuality": true,
             "description": "This data represents the best estimated real-time trajectory and local sightings opportunities for the International Space Station (ISS) as generated by the Trajectory Operations and Planning (TOPO) flight controllers at Johnson Space Center.",
-            "title": "ISS_COORDS_2021-07-20",
-            "programCode": [
-                "026:004"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -1576752,25 +1576728,63 @@
                     "title": "XMLsightingData_natparksUSA02"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "nasa-iss-data_2021-07-20_wi7k-iwtn",
+            "issued": "2021-07-20",
+            "keyword": [
+                "trajectory",
+                "space",
+                "location",
+                "coordinates",
+                "iss",
+                "ephemeris",
+                "coords",
+                "international",
+                "topo",
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
+            "temporal": "2021-07-20T00:00:00Z/P1D",
             "theme": [
                 "Space Science"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "ISS_COORDS_2021-07-20"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.nasa.gov/d/wi9w-yrvp",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "GeneLab Outreach",
+                "hasEmail": "mailto:genelab-outreach@lists.nasa.gov"
+            },
+            "description": "We examined molecular responses using transcriptome profiling in isolated left ventricular murine cardiomyocytes to 90 cGy 1 GeV proton (1H) and 15 cGy 1 GeV/nucleon (n) proton (56Fe) particles 1 3 7 14 and 28 days after exposure. Unsupervised clustering analysis of gene expression segregated samples according to the radiation (IR) response and time after exposure with 56Fe-IR showing the greatest level of gene modulation. 1H-IR exposures showed little differential transcript modulation. Network analysis categorized the major differentially expressed genes into cell cycle oxidative responses and transcriptional regulation functional groups. Transcriptional networks identified key nodes regulating expression. Individual transcription factors were inferred to be active at 1 3 7 14 and 28 days after exposure. Validation of the signal transduction network by protein analysis showed that particle IR clearly regulates a long lived signaling mechanism for p38 MAPK signaling and NFATc4 activation. Electrophoresis mobility shift assays supported the role of additional key transcription factors GATA-4 STAT-3 and NF-kB as regulators of the response at specific time points. These data suggest that the molecular response to 56Fe-IR is unique and shows long-lasting gene expression in cardiomyocytes up to 28 days after exposure. Additionally proteins involved in signal transduction and transcriptional activation via DNA binding play a role in the response to high charge (Z) and energy (E) particles (HZE). Our study may have implications for NASA  s efforts to develop heart disease risk estimates for astronauts safety via identification of specific HZE-IR molecular markers and for patients receiving conventional and particle radiotherapy. Transcriptome profiling in isolated left ventricular murine cardiomyocytes to 90 cGy 1 GeV proton (1H) and 15 cGy 1 GeV/nucleon (n) proton (56Fe) particles 1 3 7 14 and 28 days after exposure.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "GeneLab Study Page",
+                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-117",
+                    "mediaType": "text/html",
+                    "title": "Delayed Cardiomyocyte Response to Total Body Particle Radiation Exposure - Identification of Regulatory Gene Network [proton]"
+                }
+            ],
+            "identifier": "nasa_genelab_GLDS-117_wi9w-yrvp",
             "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
             "keyword": [
                 "p-gse68875-2",
                 "time",
@@ -1576788,1287 +1576802,1250 @@
                 "p-gse68875-1",
                 "p-gse68875-3"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "GeneLab Outreach",
-                "hasEmail": "mailto:genelab-outreach@lists.nasa.gov"
-            },
+            "landingPage": "https://data.nasa.gov/d/wi9w-yrvp",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "nasa_genelab_GLDS-117_wi9w-yrvp",
-            "description": "We examined molecular responses using transcriptome profiling in isolated left ventricular murine cardiomyocytes to 90 cGy 1 GeV proton (1H) and 15 cGy 1 GeV/nucleon (n) proton (56Fe) particles 1 3 7 14 and 28 days after exposure. Unsupervised clustering analysis of gene expression segregated samples according to the radiation (IR) response and time after exposure with 56Fe-IR showing the greatest level of gene modulation. 1H-IR exposures showed little differential transcript modulation. Network analysis categorized the major differentially expressed genes into cell cycle oxidative responses and transcriptional regulation functional groups. Transcriptional networks identified key nodes regulating expression. Individual transcription factors were inferred to be active at 1 3 7 14 and 28 days after exposure. Validation of the signal transduction network by protein analysis showed that particle IR clearly regulates a long lived signaling mechanism for p38 MAPK signaling and NFATc4 activation. Electrophoresis mobility shift assays supported the role of additional key transcription factors GATA-4 STAT-3 and NF-kB as regulators of the response at specific time points. These data suggest that the molecular response to 56Fe-IR is unique and shows long-lasting gene expression in cardiomyocytes up to 28 days after exposure. Additionally proteins involved in signal transduction and transcriptional activation via DNA binding play a role in the response to high charge (Z) and energy (E) particles (HZE). Our study may have implications for NASA  s efforts to develop heart disease risk estimates for astronauts safety via identification of specific HZE-IR molecular markers and for patients receiving conventional and particle radiotherapy. Transcriptome profiling in isolated left ventricular murine cardiomyocytes to 90 cGy 1 GeV proton (1H) and 15 cGy 1 GeV/nucleon (n) proton (56Fe) particles 1 3 7 14 and 28 days after exposure.",
-            "title": "Delayed Cardiomyocyte Response to Total Body Particle Radiation Exposure - Identification of Regulatory Gene Network [proton]",
-            "programCode": [
-                "026:005"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-117",
-                    "description": "GeneLab Study Page",
-                    "@type": "dcat:Distribution",
-                    "title": "Delayed Cardiomyocyte Response to Total Body Particle Radiation Exposure - Identification of Regulatory Gene Network [proton]"
-                }
-            ],
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "Delayed Cardiomyocyte Response to Total Body Particle Radiation Exposure - Identification of Regulatory Gene Network [proton]"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/PP7T2GBI52I2",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Western United States UCLA Daily Snow Reanalysis V001. Version 1. Archived by National Aeronautics and Space Administration, U.S. Government, NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/PP7T2GBI52I2.",
-            "issued": "1984-10-01",
-            "temporal": "1984-10-01T00:00:00Z/2021-09-30T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2021-09-30",
-            "keyword": [
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
-                "name": "NASA NSIDC DAAC"
-            },
-            "identifier": "C2253727823-NSIDC_ECS",
             "description": "This Western United States snow reanalysis data set contains daily estimates of posterior snow water equivalent (SWE), fractional snow-covered area (fSCA) and snow depth (SD) at 16 arc-second (~500 m) resolution from water years 1985 to 2021. This data set was developed to be compared to SnowEx data sets but its utility reaches beyond that since its spatial and temporal bounds extend over the entire Western U.S. and over several decades.",
-            "title": "Western United States UCLA Daily Snow Reanalysis V001",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FPP7T2GBI52I2",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FPP7T2GBI52I2",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/SNOWEX/WUS_UCLA_SR.001/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/SNOWEX/WUS_UCLA_SR.001/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/data/data-access-tool/WUS_UCLA_SR/versions/1/",
-                    "description": "Search and filter data files using a map-based interface",
                     "@type": "dcat:Distribution",
+                    "description": "Search and filter data files using a map-based interface",
+                    "downloadURL": "https://nsidc.org/data/data-access-tool/WUS_UCLA_SR/versions/1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=WUS_UCLA_SR+V001",
-                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=WUS_UCLA_SR+V001",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/SNOWEX/WUS_UCLA_SR.001/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/SNOWEX/WUS_UCLA_SR.001/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/data/data-access-tool/WUS_UCLA_SR/versions/1/",
-                    "description": "Search and filter data files using a map-based interface",
                     "@type": "dcat:Distribution",
+                    "description": "Search and filter data files using a map-based interface",
+                    "downloadURL": "https://nsidc.org/data/data-access-tool/WUS_UCLA_SR/versions/1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=WUS_UCLA_SR+V001",
-                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=WUS_UCLA_SR+V001",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/PP7T2GBI52I2",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/PP7T2GBI52I2",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/PP7T2GBI52I2",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/PP7T2GBI52I2",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C2253727823-NSIDC_ECS",
+            "issued": "1984-10-01",
+            "keyword": [
+                "snow/ice",
+                "earth science",
+                "cryosphere"
+            ],
+            "landingPage": "https://doi.org/10.5067/PP7T2GBI52I2",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2021-09-30",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA NSIDC DAAC"
+            },
             "spatial": "-125.0 31.0 -102.0 49.0",
+            "temporal": "1984-10-01T00:00:00Z/2021-09-30T23:59:59.999Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Western United States UCLA Daily Snow Reanalysis V001"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C2340494006-OB_DAAC.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/GSFC/SED/ESD/GCDC/OB.DAAC.",
-            "issued": "2022-09-14",
-            "temporal": "2012-01-02T00:00:00Z/2023-02-28T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-09-14",
-            "keyword": [
-                "ecosystems",
-                "earth science",
-                "oceans",
-                "ocean optics",
-                "biosphere"
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
-            "identifier": "C2340494006-OB_DAAC",
             "description": "The Ocean Biology DAAC produces near real-time (quicklook) products using the best-available combination of ancillary data from meteorological and ozone data. As such, the inputs and the calibration used are less than optimal. Quicklook products provide a snapshot of the data during a short time period within a single orbit.",
-            "title": "Suomi-NPP VIIRS Regional Inherent Optical Properties (IOP) - Near Real-time (NRT) Data, version R2022.0",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://oceandata.sci.gsfc.nasa.gov/directdataaccess/Level-2/SNPP-VIIRS/",
-                    "description": "NASA Ocean Color Web - Data Distribution Site",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Ocean Color Web - Data Distribution Site",
+                    "downloadURL": "https://oceandata.sci.gsfc.nasa.gov/directdataaccess/Level-2/SNPP-VIIRS/",
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
-                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/data/10.5067/SNPP/VIIRS/L2/IOP/2022",
-                    "description": "VIIRS-Suomi-NPP L2 Inherent Optical Properties (IOP) - Near Real-time (NRT) Dataset Landing Page",
                     "@type": "dcat:Distribution",
+                    "description": "VIIRS-Suomi-NPP L2 Inherent Optical Properties (IOP) - Near Real-time (NRT) Dataset Landing Page",
+                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/data/10.5067/SNPP/VIIRS/L2/IOP/2022",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 }
             ],
+            "identifier": "C2340494006-OB_DAAC",
+            "issued": "2022-09-14",
+            "keyword": [
+                "ecosystems",
+                "earth science",
+                "oceans",
+                "ocean optics",
+                "biosphere"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C2340494006-OB_DAAC.html",
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
+            "title": "Suomi-NPP VIIRS Regional Inherent Optical Properties (IOP) - Near Real-time (NRT) Data, version R2022.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/GHH09-2P290",
             "citation": "NOAA/NESDIS/STAR. 2023-08-08. GHRSST NOAA Himawari/AHI L2P Pacific Ocean Region SST dataset. Version 2.90. GHRSST L2P NOAA/ACSPO Himawari-09 AHI Pacific Ocean Region Sea Surface Temperature v2.90 dataset\r\n. 5200 Auth Rd, Camp Springs, MD, 20746 USA. Archived by National Aeronautics and Space Administration, U.S. Government, PO.DAAC. https://doi.org/10.5067/GHH09-2P290\r\n. https://www.star.nesdis.noaa.gov/star/index.php.",
-            "issued": "2023-08-14",
-            "temporal": "2022-10-22T00:00:00Z/2023-09-04T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-08-14",
-            "references": [
-                "https://doi.org/10.3390/rs8010079"
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
-            "identifier": "C2744808497-POCLOUD",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/JPL/PODAAC"
-            },
-            "description": "The H09-AHI-L2P-ACSPO-v2.90 dataset contains the Subskin Sea Surface Temperature (SST) produced by the NOAA ACSPO system from the Advanced Himawari Imager (AHI; largely identical to GOES-R/ABI) onboard the Himawari-9 (H09) satellite. The H09 is a Japanese weather satellite, the 9th of the Himawari geostationary weather satellite operated by the Japan Meteorological Agency. It was launched on November 2, 2016 into its nominal position at 140.7-deg E, and declared operational on December 13, 2022, replacing the Himawari-8. The AHI is the primary instrument on the Himawari Series for imaging Earth\u2019s weather, oceans, and environment with high temporal and spatial resolutions.  <br><br>\r\nThe H08/AHI maps SST in a Full Disk (FD) area from 80E-160W and 60S-60N, with spatial resolution 2km at nadir to 15km/VZA (view zenith angle) 67-deg, and 10-min temporal sampling. The 10-min FD data are subsequently collated in time, to produce the 1-hr product, with improved coverage and reduced cloud leakages and image noise. The L2P data is produced in GHRSST compliant netCDF4 GDS2 format, with 24 granules per day, and a total data volume 1.2 GB/day. The near-real time (NRT) data are updated hourly, with several hours latency. The NRT files are replaced with Delayed Mode (DM) files, with a latency of approximately 2-months. File names remain unchanged, and DM vs NRT can be identified by different time stamps and global attributes inside the files (MERRA instead of GFS for atmospheric profiles, and same day CMC L4 analyses in DM instead of one-day delayed in NRT processing).  <br><br>\r\nPixel earth locations are not reported in the granules, as they remain unchanged from granule to granule. Pixel locations  can be obtained using a flat lat/lon file or a Python script available via Documents tab from the dataset landing page. Climate and Forecast (CF) metadata aware software (e.g., Panoply, xarray) can detect and map the data as is via the granule CF projection attributes and variables. The ACSPO H09 HAI SSTs are validated against quality controlled in situ data from the NOAA iQuam system (Xu and Ignatov, 2014) and continuously monitored in the NOAA SQUAM system (Dash et al, 2010). A 0.02-deg equal-angle gridded L3C product 0.7GB/day) is available at https://podaac.jpl.nasa.gov/dataset/H09-AHI-L3C-ACSPO-v2.90",
-            "release-place": "5200 Auth Rd, Camp Springs, MD, 20746 USA",
-            "series-name": "GHRSST NOAA Himawari/AHI L2P Pacific Ocean Region SST dataset",
             "creator": "NOAA/NESDIS/STAR",
-            "title": "GHRSST L2P NOAA/ACSPO Himawari-09 AHI Pacific Ocean Region Sea Surface Temperature v2.90 dataset",
-            "graphic-preview-description": "Thumbnail",
-            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/AHI_H08-STAR-L2P-v2.70.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The H09-AHI-L2P-ACSPO-v2.90 dataset contains the Subskin Sea Surface Temperature (SST) produced by the NOAA ACSPO system from the Advanced Himawari Imager (AHI; largely identical to GOES-R/ABI) onboard the Himawari-9 (H09) satellite. The H09 is a Japanese weather satellite, the 9th of the Himawari geostationary weather satellite operated by the Japan Meteorological Agency. It was launched on November 2, 2016 into its nominal position at 140.7-deg E, and declared operational on December 13, 2022, replacing the Himawari-8. The AHI is the primary instrument on the Himawari Series for imaging Earth\u2019s weather, oceans, and environment with high temporal and spatial resolutions.  <br><br>\r\nThe H08/AHI maps SST in a Full Disk (FD) area from 80E-160W and 60S-60N, with spatial resolution 2km at nadir to 15km/VZA (view zenith angle) 67-deg, and 10-min temporal sampling. The 10-min FD data are subsequently collated in time, to produce the 1-hr product, with improved coverage and reduced cloud leakages and image noise. The L2P data is produced in GHRSST compliant netCDF4 GDS2 format, with 24 granules per day, and a total data volume 1.2 GB/day. The near-real time (NRT) data are updated hourly, with several hours latency. The NRT files are replaced with Delayed Mode (DM) files, with a latency of approximately 2-months. File names remain unchanged, and DM vs NRT can be identified by different time stamps and global attributes inside the files (MERRA instead of GFS for atmospheric profiles, and same day CMC L4 analyses in DM instead of one-day delayed in NRT processing).  <br><br>\r\nPixel earth locations are not reported in the granules, as they remain unchanged from granule to granule. Pixel locations  can be obtained using a flat lat/lon file or a Python script available via Documents tab from the dataset landing page. Climate and Forecast (CF) metadata aware software (e.g., Panoply, xarray) can detect and map the data as is via the granule CF projection attributes and variables. The ACSPO H09 HAI SSTs are validated against quality controlled in situ data from the NOAA iQuam system (Xu and Ignatov, 2014) and continuously monitored in the NOAA SQUAM system (Dash et al, 2010). A 0.02-deg equal-angle gridded L3C product 0.7GB/day) is available at https://podaac.jpl.nasa.gov/dataset/H09-AHI-L3C-ACSPO-v2.90",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGHH09-2P290%0D%0A",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGHH09-2P290%0D%0A",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.star.nesdis.noaa.gov/sod/sst/iquam/",
-                    "description": "In situ SST Quality Monitor v2.10",
                     "@type": "dcat:Distribution",
+                    "description": "In situ SST Quality Monitor v2.10",
+                    "downloadURL": "https://www.star.nesdis.noaa.gov/sod/sst/iquam/",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://www.ghrsst.org",
-                    "description": "GHRSST Project",
                     "@type": "dcat:Distribution",
+                    "description": "GHRSST Project",
+                    "downloadURL": "http://www.ghrsst.org",
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
-                    "downloadURL": "https://www.star.nesdis.noaa.gov/sod/sst/squam/",
-                    "description": "SST Quality Monitor 2.1",
                     "@type": "dcat:Distribution",
+                    "description": "SST Quality Monitor 2.1",
+                    "downloadURL": "https://www.star.nesdis.noaa.gov/sod/sst/squam/",
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
-                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/AHI_H08-STAR-L2P-v2.70.jpg",
-                    "description": "Thumbnail",
                     "@type": "dcat:Distribution",
+                    "description": "Thumbnail",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/AHI_H08-STAR-L2P-v2.70.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/ghrsst/open/data/GDS2/L2P/H09/STAR/docs/geo_nav.py",
-                    "description": "Example input file for python geolocation script",
                     "@type": "dcat:Distribution",
+                    "description": "Example input file for python geolocation script",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/ghrsst/open/data/GDS2/L2P/H09/STAR/docs/geo_nav.py",
+                    "mediaType": "text/html",
                     "title": "View this dataset's how-to documentation"
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
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2744808497-POCLOUD",
-                    "description": "HTTPS endpoint for data browse and download",
                     "@type": "dcat:Distribution",
+                    "description": "HTTPS endpoint for data browse and download",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2744808497-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2744808497-POCLOUD",
-                    "description": "Browse granule search results in Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse granule search results in Earthdata Search",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2744808497-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "application/x-netcdf",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/ghrsst/open/data/GDS2/L2P/H09/STAR/docs/H09_140_7_E.nc",
-                    "description": "Geolocation file in netCDF",
                     "@type": "dcat:Distribution",
+                    "description": "Geolocation file in netCDF",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/ghrsst/open/data/GDS2/L2P/H09/STAR/docs/H09_140_7_E.nc",
+                    "mediaType": "application/x-netcdf",
                     "title": "View this dataset's how-to documentation"
                 }
             ],
+            "graphic-preview-description": "Thumbnail",
+            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/AHI_H08-STAR-L2P-v2.70.jpg",
+            "identifier": "C2744808497-POCLOUD",
+            "issued": "2023-08-14",
+            "keyword": [
+                "ocean temperature",
+                "oceans",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/GHH09-2P290",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2023-08-14",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/JPL/PODAAC"
+            },
+            "references": [
+                "https://doi.org/10.3390/rs8010079"
+            ],
+            "release-place": "5200 Auth Rd, Camp Springs, MD, 20746 USA",
+            "series-name": "GHRSST NOAA Himawari/AHI L2P Pacific Ocean Region SST dataset",
             "spatial": "80.0 -60.0 -160.0 60.0",
+            "temporal": "2022-10-22T00:00:00Z/2023-09-04T00:00:00Z",
             "theme": [
                 "GHRSST",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "GHRSST L2P NOAA/ACSPO Himawari-09 AHI Pacific Ocean Region Sea Surface Temperature v2.90 dataset"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/IIG8FHR17DA9",
             "citation": "Beaudoing, H. and M. Rodell, NASA/GSFC/HSL. 2020-01-30. GLDAS_NOAH10_3H. Version 2.1. GLDAS Noah Land Surface Model L4 3 hourly 1.0 x 1.0 degree V2.1. Greenbelt, Maryland, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/IIG8FHR17DA9. https://disc.gsfc.nasa.gov/datacollection/GLDAS_NOAH10_3H_2.1.html. Digital Science Data.",
-            "issued": "2020-01-30",
-            "temporal": "2000-01-01T00:00:00Z/2022-01-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-30",
-            "references": [
-                "https://doi.org/10.1175/BAMS-85-3-381"
-            ],
-            "keyword": [
-                "land surface",
-                "atmospheric water vapor",
-                "atmospheric temperature",
-                "precipitation",
-                "atmospheric radiation",
-                "atmospheric pressure",
-                "atmosphere",
-                "snow/ice",
-                "soils",
-                "surface thermal properties",
-                "surface water",
-                "terrestrial hydrosphere",
-                "atmospheric winds",
-                "earth science"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "HUALAN RUI",
                 "hasEmail": "mailto:Hualan.Rui@nasa.gov"
             },
+            "creator": "Beaudoing, H. and M. Rodell, NASA/GSFC/HSL",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C1288937556-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "NASA Global Land Data Assimilation System Version 2 (GLDAS-2) has three components: GLDAS-2.0, GLDAS-2.1, and GLDAS-2.2.  GLDAS-2.0 is forced entirely with the Princeton meteorological forcing input data and provides a temporally consistent series from 1948 through 2014.  GLDAS-2.1 is forced with a combination of model and observation data from 2000 to present.  GLDAS-2.2 product suites use data assimilation (DA), whereas the GLDAS-2.0 and GLDAS-2.1 products are \"open-loop\" (i.e., no data assimilation).  The choice of forcing data, as well as DA observation source, variable, and scheme, vary for different GLDAS-2.2 products.\n\nGLDAS-2.1 data products are now available in two production streams: one stream is forced with combined forcing data including GPCP version 1.3 (the main production stream), and the other stream is processed without this forcing data (the early production stream). Since the GPCP Version 1.3 data have a 3-4 month latency, the GLDAS-2.1 data products are first created without it, and are designated as Early Products (EPs), with about 1.5 month latency. Once the GPCP Version 1.3 data become available, the GLDAS-2.1 data products are processed in the main production stream and are removed from the Early Products archive. \n\nThis data product, reprocessed in January 2020, is for GLDAS-2.1 Noah 3-hourly 1.0 degree data from the main production stream and it is a replacement to its previous version.\n\nThe 3-hourly data product was simulated with the Noah Model 3.6 in Land Information System (LIS) Version 7.  The data product contains 36 land surface fields from January 2000 to present. The GLDAS-2.1 data are archived and distributed in NetCDF format. The GLDAS-2.1 products supersede their corresponding GLDAS-1 products.\n\nThe GLDAS-2.1 simulation started on January 1, 2000 using the conditions from the GLDAS-2.0 simulation. This simulation was forced with National Oceanic and Atmospheric Administration (NOAA)/Global Data Assimilation System (GDAS) atmospheric analysis fields (Derber et al., 1991), the disaggregated Global Precipitation Climatology Project (GPCP) V1.3 Daily Analysis precipitation fields (Adler et al., 2003; Huffman et al., 2001), and the Air Force Weather Agency's AGRicultural METeorological modeling system (AGRMET) radiation fields.  The simulation used with GDAS and GPCP only from 2000 to February 2001, followed by addition of AGRMET for March 1, 2001 onwards.\n\nIn October 2020, all 3-hourly and monthly GLDAS-2 data were post-processed with the MOD44W MODIS land mask.  Previously, some grid boxes over inland water were considered as over land and, thus, had non-missing values.  The post-processing corrected this issue and masked out all model output data over inland water; the post-processing did not affect the meteorological forcing variables. More information can be found in the GLDAS-2 README.  The MOD44W MODIS land mask is available on the GLDAS Project site.\n\nIf you had downloaded the GLDAS data prior to November 2020, please download the data again to receive the post-processed data.",
-            "release-place": "Greenbelt, Maryland, USA",
-            "series-name": "GLDAS_NOAH10_3H",
-            "creator": "Beaudoing, H. and M. Rodell, NASA/GSFC/HSL",
-            "graphic-preview-description": "GLDAS-2.1 Noah 3-ourly 1.0 Degree 0-10 cm Soil Moisture [kg m-2] for 00Z March 01, 2001.",
-            "title": "GLDAS Noah Land Surface Model L4 3 hourly 1.0 x 1.0 degree V2.1 (GLDAS_NOAH10_3H) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/GLDAS_NOAH10_3H_2.1.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FIIG8FHR17DA9",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FIIG8FHR17DA9",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/GLDAS_NOAH10_3H_2.1.png",
-                    "description": "GLDAS-2.1 Noah 3-ourly 1.0 Degree 0-10 cm Soil Moisture [kg m-2] for 00Z March 01, 2001.",
                     "@type": "dcat:Distribution",
+                    "description": "GLDAS-2.1 Noah 3-ourly 1.0 Degree 0-10 cm Soil Moisture [kg m-2] for 00Z March 01, 2001.",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/GLDAS_NOAH10_3H_2.1.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/GLDAS_NOAH10_3H_2.1.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/GLDAS_NOAH10_3H_2.1.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://hydro1.gesdisc.eosdis.nasa.gov/data/GLDAS/GLDAS_NOAH10_3H.2.1/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://hydro1.gesdisc.eosdis.nasa.gov/data/GLDAS/GLDAS_NOAH10_3H.2.1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=GLDAS_NOAH10_3H_2.1",
-                    "description": "Use the Earthdata Search Client (EDSC) to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search Client (EDSC) to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=GLDAS_NOAH10_3H_2.1",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://hydro1.gesdisc.eosdis.nasa.gov/opendap/GLDAS/GLDAS_NOAH10_M.2.1/",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://hydro1.gesdisc.eosdis.nasa.gov/opendap/GLDAS/GLDAS_NOAH10_M.2.1/",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://hydro1.gesdisc.eosdis.nasa.gov/dods/GLDAS_NOAH10_3H.2.1/",
-                    "description": "The GrADS Data Server (GDS) is another form of OPeNDAP that provides subsetting and some analysis services across the Internet.",
                     "@type": "dcat:Distribution",
+                    "description": "The GrADS Data Server (GDS) is another form of OPeNDAP that provides subsetting and some analysis services across the Internet.",
+                    "downloadURL": "https://hydro1.gesdisc.eosdis.nasa.gov/dods/GLDAS_NOAH10_3H.2.1/",
+                    "mediaType": "text/html",
                     "title": "Use GRADS DATA SERVER (GDS) to access the dataset's data"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://hydro1.gesdisc.eosdis.nasa.gov/data/GLDAS/GLDAS_NOAH10_3H.2.1/doc/README_GLDAS2.pdf",
-                    "description": "README Document",
                     "@type": "dcat:Distribution",
+                    "description": "README Document",
+                    "downloadURL": "https://hydro1.gesdisc.eosdis.nasa.gov/data/GLDAS/GLDAS_NOAH10_3H.2.1/doc/README_GLDAS2.pdf",
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
-                    "downloadURL": "https://hydro1.gesdisc.eosdis.nasa.gov/thredds/catalog/GLDAS_aggregation/GLDAS_NOAH10_3H.2.1/catalog.html",
-                    "description": "Time aggregated THREDDS Data Server (TDS)",
                     "@type": "dcat:Distribution",
+                    "description": "Time aggregated THREDDS Data Server (TDS)",
+                    "downloadURL": "https://hydro1.gesdisc.eosdis.nasa.gov/thredds/catalog/GLDAS_aggregation/GLDAS_NOAH10_3H.2.1/catalog.html",
+                    "mediaType": "text/html",
                     "title": "Use THREDDS DATA to download the dataset's data"
                 }
             ],
+            "graphic-preview-description": "GLDAS-2.1 Noah 3-ourly 1.0 Degree 0-10 cm Soil Moisture [kg m-2] for 00Z March 01, 2001.",
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/GLDAS_NOAH10_3H_2.1.png",
+            "identifier": "C1288937556-GES_DISC",
+            "issued": "2020-01-30",
+            "keyword": [
+                "land surface",
+                "atmospheric water vapor",
+                "atmospheric temperature",
+                "precipitation",
+                "atmospheric radiation",
+                "atmospheric pressure",
+                "atmosphere",
+                "snow/ice",
+                "soils",
+                "surface thermal properties",
+                "surface water",
+                "terrestrial hydrosphere",
+                "atmospheric winds",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/IIG8FHR17DA9",
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
+            "series-name": "GLDAS_NOAH10_3H",
             "spatial": "-180.0 -60.0 180.0 90.0",
+            "temporal": "2000-01-01T00:00:00Z/2022-01-17T00:00:00Z",
             "theme": [
                 "GLDAS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "GLDAS Noah Land Surface Model L4 3 hourly 1.0 x 1.0 degree V2.1 (GLDAS_NOAH10_3H) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/WUKWENW76N5P",
             "citation": "Kevin W. Bowman. 2021-07-09. TRPSDL2O3CRS1FS. Version 1. TROPESS CrIS-JPSS1 L2 Ozone for Forward Stream, Standard Product V1. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/WUKWENW76N5P. https://disc.gsfc.nasa.gov/datacollection/TRPSDL2O3CRS1FS_1.html. Digital Science Data.",
-            "issued": "2021-05-18",
-            "temporal": "2021-04-01T00:00:00Z/2023-02-28T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2021-05-18",
-            "references": [
-                "https://doi.org/10.1126/sciadv.abf7460",
-                "https://doi.org/10.1029/2006JD007258",
-                "https://doi.org/10.5194/acp-10-9901-2010",
-                "https://doi.org/10.1029/2007JD008819",
-                "https://doi.org/10.5194/amt-6-1413-2013",
-                "https://doi.org/10.5194/amt-11-5587-2018"
-            ],
-            "keyword": [
-                "atmospheric chemistry",
-                "atmosphere",
-                "earth science"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "KEVIN BOWMAN",
                 "hasEmail": "mailto:kevin.w.bowman@jpl.nasa.gov"
             },
+            "creator": "Kevin W. Bowman",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C2088007562-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "The TROPESS CrIS-JPSS1 L2 Ozone for Forward Stream, Standard Product contains the vertical distribution of the retrieved atmospheric state of ozone (O3), formal uncertainties, and diagnostic information measured by the CrIS instrument on the JPSS-1 (NOAA-20) satellite. The forward stream standard product is global for the time period from 2021-04-01 to present. The NASA TRopospheric Ozone and Precursors from Earth System Sounding (TROPESS) project, uses an optimal estimation algorithm, known as the MUlti-SpEctra, MUlti-SpEcies, Multi-SEnsors (MUSES).\n\nThe data files are written in the netCDF version 4 file format, and each file contains one day of data. The data have a spatial resolution of 14 km (CrIS nadir FOV), and are reported at 26 vertical levels from the surface to 0.1 hPa. The principal investigator for the TROPESS project is Kevin W. Bowman.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "TRPSDL2O3CRS1FS",
-            "creator": "Kevin W. Bowman",
-            "graphic-preview-description": "TROPESS CrIS-JPSS1 O3 (Forward Stream, Standard Product) at 261 hPa on 01 April 2021.",
-            "title": "TROPESS CrIS-JPSS1 L2 Ozone for Forward Stream, Standard Product V1 (TRPSDL2O3CRS1FS) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TROPESS/images/TRPSDL2O3CRS1FS_Sample.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FWUKWENW76N5P",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FWUKWENW76N5P",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TROPESS/images/TRPSDL2O3CRS1FS_Sample.png",
-                    "description": "TROPESS CrIS-JPSS1 O3 (Forward Stream, Standard Product) at 261 hPa on 01 April 2021.",
                     "@type": "dcat:Distribution",
+                    "description": "TROPESS CrIS-JPSS1 O3 (Forward Stream, Standard Product) at 261 hPa on 01 April 2021.",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TROPESS/images/TRPSDL2O3CRS1FS_Sample.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/TRPSDL2O3CRS1FS_1.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/TRPSDL2O3CRS1FS_1.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/data/TROPESS_Standard/TRPSDL2O3CRS1FS.1/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/data/TROPESS_Standard/TRPSDL2O3CRS1FS.1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=TRPSDL2O3CRS1FS_1",
-                    "description": "Use the Earthdata Search Client to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search Client to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=TRPSDL2O3CRS1FS_1",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/opendap/TROPESS_Standard/TRPSDL2O3CRS1FS.1/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/opendap/TROPESS_Standard/TRPSDL2O3CRS1FS.1/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/data/TROPESS_Standard/TRPSDL2O3CRS1FS.1/doc/TROPESS_Forward_Stream_README.pdf",
-                    "description": "README Document",
                     "@type": "dcat:Distribution",
+                    "description": "README Document",
+                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/data/TROPESS_Standard/TRPSDL2O3CRS1FS.1/doc/TROPESS_Forward_Stream_README.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's read me document"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TROPESS/User_Guides/TROPESS-CRIS-O3_L2_Product_Quick_Start_User_Guide_Standard_only_2-22-21.pdf",
-                    "description": "User's Guide",
                     "@type": "dcat:Distribution",
+                    "description": "User's Guide",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TROPESS/User_Guides/TROPESS-CRIS-O3_L2_Product_Quick_Start_User_Guide_Standard_only_2-22-21.pdf",
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
+            "graphic-preview-description": "TROPESS CrIS-JPSS1 O3 (Forward Stream, Standard Product) at 261 hPa on 01 April 2021.",
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TROPESS/images/TRPSDL2O3CRS1FS_Sample.png",
+            "identifier": "C2088007562-GES_DISC",
+            "issued": "2021-05-18",
+            "keyword": [
+                "atmospheric chemistry",
+                "atmosphere",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/WUKWENW76N5P",
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
+                "https://doi.org/10.1029/2006JD007258",
+                "https://doi.org/10.5194/acp-10-9901-2010",
+                "https://doi.org/10.1029/2007JD008819",
+                "https://doi.org/10.5194/amt-6-1413-2013",
+                "https://doi.org/10.5194/amt-11-5587-2018"
+            ],
+            "release-place": "Greenbelt, MD, USA",
+            "series-name": "TRPSDL2O3CRS1FS",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2021-04-01T00:00:00Z/2023-02-28T00:00:00Z",
             "theme": [
                 "TROPESS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "TROPESS CrIS-JPSS1 L2 Ozone for Forward Stream, Standard Product V1 (TRPSDL2O3CRS1FS) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1658475738-OB_DAAC.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, OB.DAAC.",
-            "issued": "2019-06-23",
-            "temporal": "2012-01-02T00:00:00Z/2022-01-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2019-08-08",
-            "keyword": [
-                "oceans",
-                "earth science",
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
-            "identifier": "C1658475738-OB_DAAC",
             "description": "The Visible and Infrared Imager/Radiometer Suite (VIIRS) is a multi-disciplinary instrument that is being flown on the Joint Polar Satellite System (JPSS) series of spacecraft, including the Suomi National Polar-orbiting Partnership (S-NPP) that launched in October 2011. JPSS is a multi-platform, multi-agency program that consolidates the polar orbiting spacecraft of NASA and the National Oceanic and Atmospheric Administration (NOAA). S-NPP is the initial spacecraft in this series, and VIIRS is the successor to MODIS for Earth science data product generation. VIIRS has 22 spectral bands ranging from 412 nm to 12 nm. There are 16 moderate-resolution bands (750m at nadir), 5 image-resolution bands (375m), and one day-night band (DNB).",
-            "title": "Suomi-NPP VIIRS Regional Triple-window Sea Surface Temperature (SST3) Data, version 2016.2",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://oceandata.sci.gsfc.nasa.gov/directaccess/VIIRS-SNPP/L2",
-                    "description": "NASA Ocean Color Web - Data Distribution Site",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Ocean Color Web - Data Distribution Site",
+                    "downloadURL": "https://oceandata.sci.gsfc.nasa.gov/directaccess/VIIRS-SNPP/L2",
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
-                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/data/10.5067/SNPP/VIIRS/L2/SST3/2016.2",
-                    "description": "VIIRS-Suomi-NPP L2 Triple-window Sea Surface Temperature (SST3) Dataset Landing Page",
                     "@type": "dcat:Distribution",
+                    "description": "VIIRS-Suomi-NPP L2 Triple-window Sea Surface Temperature (SST3) Dataset Landing Page",
+                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/data/10.5067/SNPP/VIIRS/L2/SST3/2016.2",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 }
             ],
+            "identifier": "C1658475738-OB_DAAC",
+            "issued": "2019-06-23",
+            "keyword": [
+                "oceans",
+                "earth science",
+                "ocean temperature"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1658475738-OB_DAAC.html",
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
+            "title": "Suomi-NPP VIIRS Regional Triple-window Sea Surface Temperature (SST3) Data, version 2016.2"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC4-1295-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 4 phase 2015-10-22 to 2015-12-31. It is a Global Gravity measurement at the comet 67P and covers the time 2015-12-29T01:24:05.000 to 2015-12-29T04:12:45.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc4-1295-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC4-1295-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc4-1295-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 4 phase 2015-10-22 to 2015-12-31. It is a Global Gravity measurement at the comet 67P and covers the time 2015-12-29T01:24:05.000 to 2015-12-29T04:12:45.000.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 4 1295 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 4 1295 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/Y3MAIEUNDTBX",
             "citation": "Kevin W. Bowman. 2021-05-18. TRPSDL2COCRSWCFHI. Version 1. TROPESS CrIS-SNPP L2 Carbon Monoxide for West Coast Fires HiRes, Standard Product V1. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/Y3MAIEUNDTBX. https://disc.gsfc.nasa.gov/datacollection/TRPSDL2COCRSWCFHI_1.html. Digital Science Data.",
-            "issued": "2021-05-18",
-            "temporal": "2020-08-02T00:00:00Z/2020-10-26T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2021-05-18",
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
-            "identifier": "C2054599696-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "The TROPESS CrIS-SNPP L2 Carbon Monoxide for West Coast Fires HiRes, Standard Product contains the vertical distribution of the retrieved atmospheric state of carbon monoxide (CO), formal uncertainties, and diagnostic information measured by the CrIS instrument on the Suomi-NPP satellite. This product focuses on the CONUS region (20N-60N; 150W-40W) for the time period from 2020-08-01 to 2020-10-31, during the outbreak of U.S. West Coast wildfires. The NASA TRopospheric Ozone and Precursors from Earth System Sounding (TROPESS) project, uses an optimal estimation algorithm, known as the MUlti-SpEctra, MUlti-SpEcies, Multi-SEnsors (MUSES).\n\nThe data files are written in the netCDF version 4 file format, and each file contains one day of data. The data have a spatial resolution of 14 km (CrIS nadir FOV), and are reported at 14 vertical levels from the surface to 0.1 hPa. The principal investigator for the TROPESS project is Kevin W. Bowman.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "TRPSDL2COCRSWCFHI",
-            "creator": "Kevin W. Bowman",
-            "graphic-preview-description": "TROPESS CrIS/SNPP CO (West Coast Fires, Special Product) at 383 hPa on 12 September 2020.",
-            "title": "TROPESS CrIS-SNPP L2 Carbon Monoxide for West Coast Fires HiRes, Standard Product V1 (TRPSDL2COCRSWCFHI) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TROPESS/images/TRPSDL2COCRSWCFHI_Sample.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FY3MAIEUNDTBX",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FY3MAIEUNDTBX",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TROPESS/images/TRPSDL2COCRSWCFHI_Sample.png",
-                    "description": "TROPESS CrIS/SNPP CO (West Coast Fires, Special Product) at 383 hPa on 12 September 2020.",
                     "@type": "dcat:Distribution",
+                    "description": "TROPESS CrIS/SNPP CO (West Coast Fires, Special Product) at 383 hPa on 12 September 2020.",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TROPESS/images/TRPSDL2COCRSWCFHI_Sample.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/TRPSDL2COCRSWCFHI_1.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/TRPSDL2COCRSWCFHI_1.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/data/TROPESS_Special/TRPSDL2COCRSWCFHI.1/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/data/TROPESS_Special/TRPSDL2COCRSWCFHI.1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=TRPSDL2COCRSWCFHI_1",
-                    "description": "Use the Earthdata Search Client to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search Client to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=TRPSDL2COCRSWCFHI_1",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/opendap/TROPESS_Special/TRPSDL2COCRSWCFHI.1/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/opendap/TROPESS_Special/TRPSDL2COCRSWCFHI.1/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/data/TROPESS_Special/TRPSDL2COCRSWCFHI.1/doc/TROPESS_West_Coast_Fires_README_2-23-21.pdf",
-                    "description": "README Document",
                     "@type": "dcat:Distribution",
+                    "description": "README Document",
+                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/data/TROPESS_Special/TRPSDL2COCRSWCFHI.1/doc/TROPESS_West_Coast_Fires_README_2-23-21.pdf",
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
+            "graphic-preview-description": "TROPESS CrIS/SNPP CO (West Coast Fires, Special Product) at 383 hPa on 12 September 2020.",
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TROPESS/images/TRPSDL2COCRSWCFHI_Sample.png",
+            "identifier": "C2054599696-GES_DISC",
+            "issued": "2021-05-18",
+            "keyword": [
+                "atmosphere",
+                "earth science",
+                "atmospheric chemistry"
+            ],
+            "landingPage": "https://doi.org/10.5067/Y3MAIEUNDTBX",
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
+                "https://doi.org/10.1029/2006JD007663",
+                "https://doi.org/10.1029/2007JD008803",
+                "https://doi.org/10.5194/amt-9-2567-2016",
+                "https://doi.org/10.1016/j.rse.2020.112275",
+                "https://doi.org/10.5194/acp-13-837-2013"
+            ],
+            "release-place": "Greenbelt, MD, USA",
+            "series-name": "TRPSDL2COCRSWCFHI",
             "spatial": "-150.0 20.0 -40.0 60.0",
+            "temporal": "2020-08-02T00:00:00Z/2020-10-26T23:59:59.999Z",
             "theme": [
                 "TROPESS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "TROPESS CrIS-SNPP L2 Carbon Monoxide for West Coast Fires HiRes, Standard Product V1 (TRPSDL2COCRSWCFHI) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/FQPTQ4OJ22TL",
             "citation": "Global Modeling and Assimilation Office (GMAO). 2015-06-30. M2TMNXINT. Version 5.12.4. MERRA-2 tavgM_2d_int_Nx: 2d,Monthly mean,Time-Averaged,Single-Level,Assimilation,Vertically Integrated Diagnostics V5.12.4. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/FQPTQ4OJ22TL. https://disc.gsfc.nasa.gov/datacollection/M2TMNXINT_5.12.4.html. Digital Science Data.",
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
-                "atmospheric radiation",
-                "atmosphere",
-                "sea ice",
-                "terrestrial hydrosphere",
-                "precipitation",
-                "clouds",
-                "atmospheric water vapor",
-                "cryosphere",
-                "oceans",
-                "ocean heat budget",
-                "earth science",
-                "snow/ice"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "DANA OSTRENGA",
                 "hasEmail": "mailto:dana.ostrenga@nasa.gov"
             },
+            "creator": "Global Modeling and Assimilation Office (GMAO)",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C1276812854-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "M2TMNXINT (or  tavgM_2d_int_Nx) is a time-averaged 2-dimensional monthly mean data collection in Modern-Era Retrospective analysis for Research and Applications version 2 (MERRA-2).  This collection consists of  water and energy related vertically Integrated diagnostics, such as autoconversion loss of cloud water,  convective source of cloud ice (water),  eastward (nothward) flux of atmospheric ice (liquid, vapor),  total potential energy tendency, vertically integrated potential energy tendency, and vertically integrated kinetic energy tendency.  The collection also includes variance of certain parameters. \n\nMERRA-2 is the latest version of global atmospheric reanalysis for the satellite era produced by NASA Global Modeling and Assimilation Office (GMAO) using the Goddard Earth Observing System Model (GEOS) version 5.12.4.  The dataset covers the period of 1980-present with the latency of ~3 weeks after the end of a month. \n\nData Reprocessing:  Please check \u201cRecords of MERRA-2 Data Reprocessing and Service Changes\u201d linked from the \u201cDocumentation\u201d tab on this page.  Note that a reprocessed data filename is different from the original file.\n\nMERRA-2 Mailing List: Sign up to receive information on reprocessing of data, changing of tools and services, as well as data announcements from GMAO. Contact the GES DISC Help Desk (gsfc-dl-help-disc@mail.nasa.gov) to be added to the list.\n\nQuestions: If you have a question, please read \"MERRA-2 File Specification Document\",  \u201cMERRA-2 Data Access \u2013 Quick Start Guide\u201d, and FAQs linked from the \u201dDocumentation\u201d tab on this page.  If that does not answer your question, you may email the question on data access to the GES DISC Help Desk (gsfc-dl-help-disc@mail.nasa.gov), or the question on science to the MERRA-2 science team (merra-questions@lists.nasa.gov).",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "M2TMNXINT",
-            "creator": "Global Modeling and Assimilation Office (GMAO)",
-            "graphic-preview-description": "The GES-DISC Interactive Online Visualization ANd aNalysis Interface (Giovanni) is a web-based tool that allows users to interactively visualize and analyze data.",
-            "title": "MERRA-2 tavgM_2d_int_Nx: 2d,Monthly mean,Time-Averaged,Single-Level,Assimilation,Vertically Integrated Diagnostics 0.625 x 0.5 degree V5.12.4 (M2TMNXINT) at GES DISC",
-            "graphic-preview-file": "https://giovanni.gsfc.nasa.gov/giovanni/#dataKeyword=M2TMNXINT",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FFQPTQ4OJ22TL",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FFQPTQ4OJ22TL",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/M2TMNXINT_5.12.4.png",
-                    "description": "M2TMNXINT variable",
                     "@type": "dcat:Distribution",
+                    "description": "M2TMNXINT variable",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/M2TMNXINT_5.12.4.png",
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
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/M2TMNXINT_5.12.4.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/M2TMNXINT_5.12.4.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://goldsmr4.gesdisc.eosdis.nasa.gov/data/MERRA2_MONTHLY/M2TMNXINT.5.12.4/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://goldsmr4.gesdisc.eosdis.nasa.gov/data/MERRA2_MONTHLY/M2TMNXINT.5.12.4/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://giovanni.gsfc.nasa.gov/giovanni/#dataKeyword=M2TMNXINT",
-                    "description": "The GES-DISC Interactive Online Visualization ANd aNalysis Interface (Giovanni) is a web-based tool that allows users to interactively visualize and analyze data.",
                     "@type": "dcat:Distribution",
+                    "description": "The GES-DISC Interactive Online Visualization ANd aNalysis Interface (Giovanni) is a web-based tool that allows users to interactively visualize and analyze data.",
+                    "downloadURL": "https://giovanni.gsfc.nasa.gov/giovanni/#dataKeyword=M2TMNXINT",
+                    "mediaType": "text/html",
                     "title": "Get a related visualization through GIOVANNI"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=M2TMNXINT",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=M2TMNXINT",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://goldsmr4.gesdisc.eosdis.nasa.gov/dods/M2TMNXINT.info",
-                    "description": "The GrADS Data Server (GDS) is another form of OPeNDAP that provides subsetting and some analysis services across the Internet.",
                     "@type": "dcat:Distribution",
+                    "description": "The GrADS Data Server (GDS) is another form of OPeNDAP that provides subsetting and some analysis services across the Internet.",
+                    "downloadURL": "https://goldsmr4.gesdisc.eosdis.nasa.gov/dods/M2TMNXINT.info",
+                    "mediaType": "text/html",
                     "title": "Use GRADS DATA SERVER (GDS) to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://goldsmr4.gesdisc.eosdis.nasa.gov/opendap/MERRA2_MONTHLY/M2TMNXINT.5.12.4/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://goldsmr4.gesdisc.eosdis.nasa.gov/opendap/MERRA2_MONTHLY/M2TMNXINT.5.12.4/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://goldsmr4.gesdisc.eosdis.nasa.gov/thredds/catalog/MERRA2_MONTHLY_aggregation/catalog.html?dataset=merra2_monthly_aggregation%2FM2TMNXINT.5.12.4_Aggregation.ncml",
-                    "description": "Time aggregated THREDDS Data Server (TDS) ",
                     "@type": "dcat:Distribution",
+                    "description": "Time aggregated THREDDS Data Server (TDS) ",
+                    "downloadURL": "https://goldsmr4.gesdisc.eosdis.nasa.gov/thredds/catalog/MERRA2_MONTHLY_aggregation/catalog.html?dataset=merra2_monthly_aggregation%2FM2TMNXINT.5.12.4_Aggregation.ncml",
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
-                    "downloadURL": "https://goldsmr4.gesdisc.eosdis.nasa.gov/data/MERRA2_MONTHLY/M2TMNXINT.5.12.4/doc/MERRA2.README.pdf",
-                    "description": "README Document",
                     "@type": "dcat:Distribution",
+                    "description": "README Document",
+                    "downloadURL": "https://goldsmr4.gesdisc.eosdis.nasa.gov/data/MERRA2_MONTHLY/M2TMNXINT.5.12.4/doc/MERRA2.README.pdf",
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
+            "graphic-preview-file": "https://giovanni.gsfc.nasa.gov/giovanni/#dataKeyword=M2TMNXINT",
+            "identifier": "C1276812854-GES_DISC",
+            "issued": "2007-06-14",
+            "keyword": [
+                "atmospheric radiation",
+                "atmosphere",
+                "sea ice",
+                "terrestrial hydrosphere",
+                "precipitation",
+                "clouds",
+                "atmospheric water vapor",
+                "cryosphere",
+                "oceans",
+                "ocean heat budget",
+                "earth science",
+                "snow/ice"
+            ],
+            "landingPage": "https://doi.org/10.5067/FQPTQ4OJ22TL",
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
+            "series-name": "M2TMNXINT",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "1980-01-01T00:00:00Z/2022-01-17T00:00:00Z",
             "theme": [
                 "MERRA-2",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "MERRA-2 tavgM_2d_int_Nx: 2d,Monthly mean,Time-Averaged,Single-Level,Assimilation,Vertically Integrated Diagnostics 0.625 x 0.5 degree V5.12.4 (M2TMNXINT) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-E%2FCAL-NAVCAM-2-EAR3-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This dataset contains RAW DATA of the EARTH 3 Swingby Phase from 13 November 2009 until 30 November 2009. The closest approach (CA) took place on 13 November 2009",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-e-cal-navcam-2-ear3-v1.0_wigu-rhxr",
             "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "earth",
                 "moon",
                 "calibration",
                 "international rosetta mission"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-E%2FCAL-NAVCAM-2-EAR3-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-e-cal-navcam-2-ear3-v1.0_wigu-rhxr",
-            "description": "This dataset contains RAW DATA of the EARTH 3 Swingby Phase from 13 November 2009 until 30 November 2009. The closest approach (CA) took place on 13 November 2009",
-            "title": "ROSETTA-ORBITER-EARTH/CAL-NAVCAM-2-EAR3-V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "ROSETTA-ORBITER-EARTH/CAL-NAVCAM-2-EAR3-V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/SeaBASS/AMLR/DATA001",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/GSFC/SED/ESD/GCDC/OB.DAAC. https://doi.org/10.5067/SeaBASS/AMLR/DATA001.",
-            "issued": "1997-01-26",
-            "temporal": "1997-01-26T00:00:02Z/2023-04-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-04-06",
-            "keyword": [
-                "ocean chemistry",
-                "earth science",
-                "ocean optics",
-                "salinity/density",
-                "ocean temperature",
-                "oceans"
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
-            "identifier": "C1633360097-OB_DAAC",
             "description": "Measurements taken under the U.S. Antarctic Marine Living Resources (AMLR) program spanning 1997 to 2008.",
-            "title": "Antarctic Marine Living Resources (AMLR) program",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSeaBASS%2FAMLR%2FDATA001",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSeaBASS%2FAMLR%2FDATA001",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://seabass.gsfc.nasa.gov/experiment/AMLR/",
-                    "description": "Detailed information about the SeaBASS Experiment such as cruises, funding, and investigators",
                     "@type": "dcat:Distribution",
+                    "description": "Detailed information about the SeaBASS Experiment such as cruises, funding, and investigators",
+                    "downloadURL": "https://seabass.gsfc.nasa.gov/experiment/AMLR/",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 }
             ],
+            "identifier": "C1633360097-OB_DAAC",
+            "issued": "1997-01-26",
+            "keyword": [
+                "ocean chemistry",
+                "earth science",
+                "ocean optics",
+                "salinity/density",
+                "ocean temperature",
+                "oceans"
+            ],
+            "landingPage": "https://doi.org/10.5067/SeaBASS/AMLR/DATA001",
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
+            "temporal": "1997-01-26T00:00:02Z/2023-04-17T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Antarctic Marine Living Resources (AMLR) program"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/351",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Arkebauer, T.J. 1998. BOREAS TE-12 Leaf Gas Exchange Data. ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/351",
-            "issued": "2023-11-22",
-            "temporal": "1994-05-29T00:00:00Z/1995-08-07T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-11-28",
-            "keyword": [
-                "biosphere",
-                "vegetation",
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
-            "identifier": "C2808129981-ORNL_CLOUD",
             "description": "Contains data collected by TE-12 of single leaf gas exchange properties of dominant vascular plant species in the SSA in 1994 and 1995.",
-            "graphic-preview-description": "Browse Image",
-            "title": "BOREAS TE-12 Leaf Gas Exchange Data",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/boreas_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F351",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F351",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/boreas/TE/te12lgex/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/boreas/TE/te12lgex/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/BOREAS/guides/TE12_Leaf_Gas_Exch.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/BOREAS/guides/TE12_Leaf_Gas_Exch.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/351",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/351",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TE/te12lgex/comp/te12lgex.def",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TE/te12lgex/comp/te12lgex.def",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/msword",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TE/te12lgex/comp/TE12_Leaf_Gas_Exch.doc",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TE/te12lgex/comp/TE12_Leaf_Gas_Exch.doc",
+                    "mediaType": "application/msword",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TE/te12lgex/comp/TE12_Leaf_Gas_Exch.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TE/te12lgex/comp/TE12_Leaf_Gas_Exch.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TE/te12lgex/comp/TE12_Leaf_Gas_Exch.txt",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TE/te12lgex/comp/TE12_Leaf_Gas_Exch.txt",
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
+            "identifier": "C2808129981-ORNL_CLOUD",
+            "issued": "2023-11-22",
+            "keyword": [
+                "biosphere",
+                "vegetation",
+                "ecological dynamics",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/351",
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
+            "temporal": "1994-05-29T00:00:00Z/1995-08-07T23:59:59Z",
             "theme": [
                 "BOREAS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "BOREAS TE-12 Leaf Gas Exchange Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://planetarynames.wr.usgs.gov/Page/Images",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "1979-12-31",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
-            "keyword": [
-                "boundaries",
-                "usgs",
-                "regional",
-                "mola",
-                "mars",
-                "imagery",
-                "images",
-                "maps",
-                "working group for planetary system nomenclature"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Michael Kelly",
                 "hasEmail": "mailto:Michael.S.Kelley@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "International Astronomical Union (IAU) Working Group for Planetary System Nomenclature (WGPSN)"
-            },
-            "identifier": "OCIO-Fitara-163",
             "description": "These maps display regional feature names and boundaries of regional features of Mars approved by the International Astronomical Union (IAU).",
-            "title": "Gazetteer of Planetary Nomenclature: Mars: MOLA global images",
-            "programCode": [
-                "026:007"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -1578081,57 +1578058,54 @@
                     "mediaType": "application/pdf"
                 }
             ],
-            "accrualPeriodicity": "irregular",
+            "identifier": "OCIO-Fitara-163",
+            "issued": "1979-12-31",
+            "keyword": [
+                "boundaries",
+                "usgs",
+                "regional",
+                "mola",
+                "mars",
+                "imagery",
+                "images",
+                "maps",
+                "working group for planetary system nomenclature"
+            ],
+            "landingPage": "http://planetarynames.wr.usgs.gov/Page/Images",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:007"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "International Astronomical Union (IAU) Working Group for Planetary System Nomenclature (WGPSN)"
+            },
             "theme": [
                 "Space Science"
-            ]
+            ],
+            "title": "Gazetteer of Planetary Nomenclature: Mars: MOLA global images"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/TRMM/TMPA/MONTH/7",
             "citation": "Tropical Rainfall Measuring Mission (TRMM). 2011-07-01. TRMM_3B43. TRMM (TMPA/3B43) Rainfall Estimate L3 1 month 0.25 degree x 0.25 degree V7. Greenbelt, MD. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/TRMM/TMPA/MONTH/7. https://disc.gsfc.nasa.gov/datacollection/TRMM_3B43_7.html. Digital Science Data.",
-            "issued": "2011-07-01",
-            "temporal": "1998-01-01T00:00:00Z/2019-12-31T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2016-04-20",
-            "references": [
-                "https://doi.org/10.1007/978-90-481-2915-7"
-            ],
-            "keyword": [
-                "precipitation",
-                "earth science",
-                "atmosphere"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "ANDREY SAVTCHENKO",
                 "hasEmail": "mailto:Andrey.Savtchenko@nasa.gov"
             },
+            "creator": "Tropical Rainfall Measuring Mission (TRMM)",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C1282032631-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "TMPA (3B43) dataset have been discontinued as of Dec. 31, 2019, and users are strongly encouraged to shift to the successor IMERG dataset (doi: 10.5067/GPM/IMERG/3B-MONTH/06).\n\nThe 3B43 dataset is the monthly version of the 3B42 dataset.\n\nThis product was created using TRMM-adjusted merged microwave-infrared precipitation rate (in mm/hr) and root-mean-square (RMS) precipitation-error estimates.\nIt provides a \"best\" precipitation estimate in a latitude band covering 50o N to 50o S, an expansion of the TRMM region, from all global data sources, namely high-quality microwave data, infrared data, and analyses of rain gauges. The granule size is one month.",
-            "release-place": "Greenbelt, MD",
-            "series-name": "TRMM_3B43",
-            "creator": "Tropical Rainfall Measuring Mission (TRMM)",
-            "graphic-preview-description": "The GES-DISC Interactive Online Visualization ANd aNalysis Interface (Giovanni) is a web-based tool that allows users to interactively visualize and analyze data.",
-            "title": "TRMM (TMPA/3B43) Rainfall Estimate L3 1 month 0.25 degree x 0.25 degree V7 (TRMM_3B43) at GES DISC",
-            "graphic-preview-file": "https://giovanni.gsfc.nasa.gov/giovanni/#dataKeyword=TRMM_3B43",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FTRMM%2FTMPA%2FMONTH%2F7",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FTRMM%2FTMPA%2FMONTH%2F7",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
@@ -1578141,59 +1578115,59 @@
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/TRMM_3B43_7.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/TRMM_3B43_7.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc2.gesdisc.eosdis.nasa.gov/data/TRMM_L3/TRMM_3B43.7",
-                    "description": "Access the data via HTTPS",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS",
+                    "downloadURL": "https://disc2.gesdisc.eosdis.nasa.gov/data/TRMM_L3/TRMM_3B43.7",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc2.gesdisc.eosdis.nasa.gov/opendap/TRMM_L3/TRMM_3B43.7/",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://disc2.gesdisc.eosdis.nasa.gov/opendap/TRMM_L3/TRMM_3B43.7/",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://giovanni.gsfc.nasa.gov/giovanni/#dataKeyword=TRMM_3B43",
-                    "description": "The GES-DISC Interactive Online Visualization ANd aNalysis Interface (Giovanni) is a web-based tool that allows users to interactively visualize and analyze data.",
                     "@type": "dcat:Distribution",
+                    "description": "The GES-DISC Interactive Online Visualization ANd aNalysis Interface (Giovanni) is a web-based tool that allows users to interactively visualize and analyze data.",
+                    "downloadURL": "https://giovanni.gsfc.nasa.gov/giovanni/#dataKeyword=TRMM_3B43",
+                    "mediaType": "text/html",
                     "title": "Get a related visualization through GIOVANNI"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc2.gesdisc.eosdis.nasa.gov/thredds/catalog/aggregation/TRMM_3B43.7/catalog.html",
-                    "description": "Access the data via the THREDDS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the THREDDS.",
+                    "downloadURL": "https://disc2.gesdisc.eosdis.nasa.gov/thredds/catalog/aggregation/TRMM_3B43.7/catalog.html",
+                    "mediaType": "text/html",
                     "title": "Use THREDDS DATA to download the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc2.gesdisc.eosdis.nasa.gov/dods/TRMM_3B43_7.info",
-                    "description": "The GrADS Data Server (GDS) is another form of OPeNDAP that provides subsetting and some analysis services across the Internet.",
                     "@type": "dcat:Distribution",
+                    "description": "The GrADS Data Server (GDS) is another form of OPeNDAP that provides subsetting and some analysis services across the Internet.",
+                    "downloadURL": "https://disc2.gesdisc.eosdis.nasa.gov/dods/TRMM_3B43_7.info",
+                    "mediaType": "text/html",
                     "title": "Use GRADS DATA SERVER (GDS) to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=TRMM_3B43",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=TRMM_3B43",
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
@@ -1578203,870 +1578177,905 @@
                     "title": "View the primary investigator's documentation for this dataset"
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
-                    "downloadURL": "https://disc2.gesdisc.eosdis.nasa.gov/data/TRMM_L3/TRMM_3B43/doc/README.TRMM_V7.pdf",
-                    "description": "README Document",
                     "@type": "dcat:Distribution",
+                    "description": "README Document",
+                    "downloadURL": "https://disc2.gesdisc.eosdis.nasa.gov/data/TRMM_L3/TRMM_3B43/doc/README.TRMM_V7.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's read me document"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://pmm.nasa.gov/sites/default/files/imce/3B42_3B43_TMPA_restart.pdf",
-                    "description": "Details of the TMPA algorithm used in this product.",
                     "@type": "dcat:Distribution",
+                    "description": "Details of the TMPA algorithm used in this product.",
+                    "downloadURL": "https://pmm.nasa.gov/sites/default/files/imce/3B42_3B43_TMPA_restart.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
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
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/GPM/TMPA-to-IMERG_transition.pdf",
-                    "description": "Transition from TMPA to IMERG",
                     "@type": "dcat:Distribution",
+                    "description": "Transition from TMPA to IMERG",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/GPM/TMPA-to-IMERG_transition.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "graphic-preview-description": "The GES-DISC Interactive Online Visualization ANd aNalysis Interface (Giovanni) is a web-based tool that allows users to interactively visualize and analyze data.",
+            "graphic-preview-file": "https://giovanni.gsfc.nasa.gov/giovanni/#dataKeyword=TRMM_3B43",
+            "identifier": "C1282032631-GES_DISC",
+            "issued": "2011-07-01",
+            "keyword": [
+                "precipitation",
+                "earth science",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.5067/TRMM/TMPA/MONTH/7",
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
+                "https://doi.org/10.1007/978-90-481-2915-7"
+            ],
+            "release-place": "Greenbelt, MD",
+            "series-name": "TRMM_3B43",
             "spatial": "-180.0 -50.0 180.0 50.0",
+            "temporal": "1998-01-01T00:00:00Z/2019-12-31T23:59:59.999Z",
             "theme": [
                 "TRMM",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "TRMM (TMPA/3B43) Rainfall Estimate L3 1 month 0.25 degree x 0.25 degree V7 (TRMM_3B43) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "http://techport.nasa.gov/view/18915",
-            "issued": "2015-01-01",
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
-                "learn",
-                "ames research center",
-                "active"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Douglas Rohn",
                 "hasEmail": "mailto:douglas.a.rohn@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Aeronautics Research Mission Directorate"
-            },
-            "identifier": "TECHPORT_18915",
             "description": "&lt;p&gt;The LEARN Project explores the creation of novel concepts and processes with the potential to create new capabilities in aeronautics research through awards to the external community including university and industry teams. The LEARN Project incorporates a competitive review process of the external teams&amp;rsquo; proposals to develop integrated solutions for complex technical problems captured in the ARMD strategic thrusts, followed by short duration activities for feasibility assessment. Follow-on phases of the most promising ideas are also funded. LEARN also utilizes challenges and prizes to the external community.&amp;nbsp; With these processes, NASA funds also help catalyze investments from the aerospace and non-aerospace communities toward solving problems aligned with NASA interests.&lt;/p&gt;&lt;p&gt;The NASA Aeronautics Research Institute (NARI) has been established to achieve the LEARN Project&amp;rsquo;s goals.&amp;nbsp; NARI will complement other ARMD efforts in seeking early-stage innovative concepts applicable to a broad spectrum of aeronautical challenges in the nation&amp;rsquo;s air transportation system by sponsoring research solicitations and by hosting future competitive challenges. The Institute will coordinate these efforts and communicate the outcome of the research conducted to interested parties both internal and external to NASA. ARMD&amp;rsquo;s goal is to mature the new concepts in order to infuse them into current ARMD research programs, to enable new avenues of aeronautics research that are not currently supported by ARMD program and project funds, or to achieve practical application by the aeronautics community.&lt;/p&gt;",
-            "title": "Leading Edge Aeronautics Research for NASA Project",
-            "programCode": [
-                "026:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "http://techport.nasa.gov/xml-api/18915",
                     "mediaType": "application/xml"
                 }
-            ]
+            ],
+            "identifier": "TECHPORT_18915",
+            "issued": "2015-01-01",
+            "keyword": [
+                "project",
+                "learn",
+                "ames research center",
+                "active"
+            ],
+            "landingPage": "http://techport.nasa.gov/view/18915",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Aeronautics Research Mission Directorate"
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
+            "title": "Leading Edge Aeronautics Research for NASA Project"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1237207620-LARC_ASDC.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2016-04-25. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://asdc.larc.nasa.gov/project/CERES/CER_GEO_Ed4_MET10_SH_V01.",
-            "issued": "2016-03-18",
-            "temporal": "2013-01-21T00:00:00Z/2017-02-28T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2016-03-18",
-            "keyword": [
-                "earth science",
-                "clouds",
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
-            "identifier": "C1237207620-LARC_ASDC",
             "description": "CER_GEO_Ed4_MET10_SH_V01 is the Satellite Cloud and Radiation Property retrieval System (SatCORPS) Clouds and the Earth's Radiant Energy System (CERES) Geostationary Satellite (GEO) Edition 4 Meteosat-10 over the Southern Hemisphere (SH) Version 1.0 data product. Data was collected using the Spinning Enhanced Visible and Infrared Imager (SEVIRI) Instrument on the Meteosat-10 platform. Data collection for this product is complete.\r\n\r\nThis data set comprises cloud micro-physical and radiation properties derived hourly from Meteosat-10 geostationary satellite imager data using the Langley Research Center (LARC) SATCORPS algorithms supporting the CERES project. Each active geostationary satellite's cloud micro-physical and radiation properties are merged to create hourly global cloud properties that estimate fluxes between CERES instrument measurements to account for the changing diurnal cycle. The data set is arranged as files for each hour and in netCDF-4 format. The observations are at 3 km resolution (at nadir) and are sub-sampled to 9 km.\r\n\r\nCERES is a key Earth Observing System (EOS) program component. The CERES instruments provide radiometric measurements of the Earth's atmosphere from three broadband channels. The CERES missions follow the successful Earth Radiation Budget Experiment (ERBE) mission. The first CERES instrument, the protoflight model (PFM), was launched on November 27, 1997, as part of the Tropical Rainfall Measuring Mission (TRMM). Two CERES instruments (FM1 and FM2) were launched into polar orbit on board the Earth Observing System (EOS) flagship Terra on December 18, 1999. Two additional CERES instruments (FM3 and FM4) were launched on board Earth Observing System (EOS) Aqua on May 4, 2002. The CERES FM5 instrument was launched on board the Suomi National Polar-orbiting Partnership (NPP) satellite on October 28, 2011. The newest CERES instrument (FM6) was launched on board the Joint Polar-Orbiting Satellite System 1 (JPSS-1) satellite, now called NOAA-20, on November 18, 2017.",
-            "graphic-preview-description": "Mission Logo",
-            "title": "SatCORPS CERES GEO Edition 4 Meteosat-10 Southern Hemisphere Version 1.0",
-            "graphic-preview-file": "https://asdc.larc.nasa.gov/static/images/project_logos/ceres.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
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
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1237207620-LARC_ASDC",
-                    "description": "Earthdata Search for CER_GEO_Ed4_MET10_SH_V01 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for CER_GEO_Ed4_MET10_SH_V01 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1237207620-LARC_ASDC",
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
-                    "downloadURL": "https://asdc.larc.nasa.gov/citing-data",
-                    "description": "ASDC's data citation policy",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC's data citation policy",
+                    "downloadURL": "https://asdc.larc.nasa.gov/citing-data",
+                    "mediaType": "text/html",
                     "title": "View information related to this dataset"
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
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/CERES/GEO/Edition4/MET10_SH_V01/",
-                    "description": "ASDC Direct Data Download for CER_GEO_Ed4_MET10_SH_V01",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for CER_GEO_Ed4_MET10_SH_V01",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/CERES/GEO/Edition4/MET10_SH_V01/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/CERES/GEO/Edition4/MET10_SH_V01/contents.html",
-                    "description": "OPeNDAP data access for CER_GEO_Ed4_MET10_SH_V01",
                     "@type": "dcat:Distribution",
+                    "description": "OPeNDAP data access for CER_GEO_Ed4_MET10_SH_V01",
+                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/CERES/GEO/Edition4/MET10_SH_V01/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 }
             ],
+            "graphic-preview-description": "Mission Logo",
+            "graphic-preview-file": "https://asdc.larc.nasa.gov/static/images/project_logos/ceres.png",
+            "identifier": "C1237207620-LARC_ASDC",
+            "issued": "2016-03-18",
+            "keyword": [
+                "earth science",
+                "clouds",
+                "atmosphere"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1237207620-LARC_ASDC.html",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2016-03-18",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/LARC/SD/ASDC"
+            },
             "spatial": "<?xml version=\"1.0\" encoding=\"UTF-8\"?><gml:Polygon xmlns:gml=\"http://www.opengis.net/gml/3.2\" srsName=\"EPSG:9825\"><gml:outerBoundaryIs><gml:LinearRing><gml:posList>-60.0 -50.0 -60.0 60.0 0.0 60.0 0.0 -50.0 -60.0 -50.0</gml:posList></gml:LinearRing></gml:outerBoundaryIs><gml:innerBoundaryIs></gml:innerBoundaryIs></gml:Polygon>",
+            "temporal": "2013-01-21T00:00:00Z/2017-02-28T23:59:59.999Z",
             "theme": [
                 "CERES",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "SatCORPS CERES GEO Edition 4 Meteosat-10 Southern Hemisphere Version 1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RPCIES-5-ESC2-V1.0",
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
+            "description": "This dataset contains DERIVED DATA of the Rosetta RPCIES instrument taken during the comet escort 2 phase (ESC2). The target of this phase was comet 67P/CHURYUMOV-GERASIMENKO 1 (1969 R1). Included are the data taken between 11 Mar 2015 and 30 Jun 2015.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rpcies-5-esc2-v1.0_wiyc-kaea",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RPCIES-5-ESC2-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rpcies-5-esc2-v1.0_wiyc-kaea",
-            "description": "This dataset contains DERIVED DATA of the Rosetta RPCIES instrument taken during the comet escort 2 phase (ESC2). The target of this phase was comet 67P/CHURYUMOV-GERASIMENKO 1 (1969 R1). Included are the data taken between 11 Mar 2015 and 30 Jun 2015.",
-            "title": "ROSETTA-ORBITER 67P RPCIES 5 ESC2 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RPCIES 5 ESC2 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=GIO-C-MAG-4-RDR-HALLEY-8SEC-V1.0",
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
-                "giotto",
-                "halley"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "The main objective of the Giotto Magnetometer Experiment is the investigation of the interaction between Comet Halley and the solar wind at a distance of 0.9 AU from the Sun, to within 500 km of the cometary nucleus. A second objective is the study of the interplanetary magnetic field. The instrumentation consists of a triaxial and a separate biaxial system of fluxgate sensors of the ring-core type, the associated analogue electronics and a digital processor. The measuring ranges of +/- 16 nT, +/- 64 nT, etc., up to +/- 65536 nT are digitis- ed by a 12-bit analogue-to-digital converter, allowing a sampling rate of 28.24 vectors per second at encounter. Memory modes allow the bridging of gaps in telemetry coverage of up to ten days. The total mass of the instrument is 1360 g and its power consumption 820 mW.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.gio-c-mag-4-rdr-halley-8sec-v1.0_wj5d-fhsw",
+            "issued": "2021-05-21",
+            "keyword": [
+                "giotto",
+                "halley"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=GIO-C-MAG-4-RDR-HALLEY-8SEC-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.gio-c-mag-4-rdr-halley-8sec-v1.0_wj5d-fhsw",
-            "description": "The main objective of the Giotto Magnetometer Experiment is the investigation of the interaction between Comet Halley and the solar wind at a distance of 0.9 AU from the Sun, to within 500 km of the cometary nucleus. A second objective is the study of the interplanetary magnetic field. The instrumentation consists of a triaxial and a separate biaxial system of fluxgate sensors of the ring-core type, the associated analogue electronics and a digital processor. The measuring ranges of +/- 16 nT, +/- 64 nT, etc., up to +/- 65536 nT are digitis- ed by a 12-bit analogue-to-digital converter, allowing a sampling rate of 28.24 vectors per second at encounter. Memory modes allow the bridging of gaps in telemetry coverage of up to ten days. The total mass of the instrument is 1360 g and its power consumption 820 mW.",
-            "title": "GIOTTO MAGNETOMETER 8 SECOND DATA V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "GIOTTO MAGNETOMETER 8 SECOND DATA V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1658475772-OB_DAAC.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, OB.DAAC.",
-            "issued": "2019-06-23",
-            "temporal": "2012-01-02T00:00:00Z/2022-01-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2019-08-08",
-            "keyword": [
-                "ocean temperature",
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
-                "name": "OB.DAAC"
-            },
-            "identifier": "C1658475772-OB_DAAC",
             "description": "The Visible and Infrared Imager/Radiometer Suite (VIIRS) is a multi-disciplinary instrument that is being flown on the Joint Polar Satellite System (JPSS) series of spacecraft, including the Suomi National Polar-orbiting Partnership (S-NPP) that launched in October 2011. JPSS is a multi-platform, multi-agency program that consolidates the polar orbiting spacecraft of NASA and the National Oceanic and Atmospheric Administration (NOAA). S-NPP is the initial spacecraft in this series, and VIIRS is the successor to MODIS for Earth science data product generation. VIIRS has 22 spectral bands ranging from 412 nm to 12 nm. There are 16 moderate-resolution bands (750m at nadir), 5 image-resolution bands (375m), and one day-night band (DNB).",
-            "title": "Suomi-NPP VIIRS Global Mapped Triple-window Sea Surface Temperature (SST3) Data, version 2016.2",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://oceandata.sci.gsfc.nasa.gov/directaccess/VIIRS-SNPP/L3SMI",
-                    "description": "NASA Ocean Color Web - Data Distribution Site",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Ocean Color Web - Data Distribution Site",
+                    "downloadURL": "https://oceandata.sci.gsfc.nasa.gov/directaccess/VIIRS-SNPP/L3SMI",
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
-                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/data/10.5067/NPP/VIIRS/L3M/SST3/2016.2",
-                    "description": "VIIRS-Suomi-NPP L3M Triple-window Sea Surface Temperature (SST3) Dataset Landing Page",
                     "@type": "dcat:Distribution",
+                    "description": "VIIRS-Suomi-NPP L3M Triple-window Sea Surface Temperature (SST3) Dataset Landing Page",
+                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/data/10.5067/NPP/VIIRS/L3M/SST3/2016.2",
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
+            "identifier": "C1658475772-OB_DAAC",
+            "issued": "2019-06-23",
+            "keyword": [
+                "ocean temperature",
+                "earth science",
+                "oceans"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1658475772-OB_DAAC.html",
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
+            "title": "Suomi-NPP VIIRS Global Mapped Triple-window Sea Surface Temperature (SST3) Data, version 2016.2"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ASDC/SUBORBITAL/DISCOVERAQ_California_Ground_Pandora_Data_1",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2022-07-26. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/ASDC/SUBORBITAL/DISCOVERAQ_California_Ground_Pandora_Data_1.",
-            "issued": "2021-08-19",
-            "temporal": "2012-12-02T00:00:00Z/2013-02-13T23:59:59.999Z",
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
-            "identifier": "C2404262905-LARC_ASDC",
             "description": "DISCOVERAQ_California_Pandora_Data contains all of the Pandora instrumentation data collected during the DISCOVER-AQ field study. Contained in this dataset are column measurements of NO2 and O3. Pandoras were situated at various ground sites across the study area, including Arvin-DiGiorgio, Bakersfield, Corcoran, Fresno, Hanford, Huron, Madera, Parlier, Porterville, Shafter, Tranquility and Visalia Airport. This data product contains only data from the California deployment and data collection is complete.\r\n\r\nUnderstanding the factors that contribute to near surface pollution is difficult using only satellite-based observations. The incorporation of surface-level measurements from aircraft and ground-based platforms provides the crucial information necessary to validate and expand upon the use of satellites in understanding near surface pollution. Deriving Information on Surface conditions from Column and Vertically Resolved Observations Relevant to Air Quality (DISCOVER-AQ) was a four-year campaign conducted in collaboration between NASA Langley Research Center, NASA Goddard Space Flight Center, NASA Ames Research Center, and multiple universities to improve the use of satellites to monitor air quality for public health and environmental benefit. Through targeted airborne and ground-based observations, DISCOVER-AQ enabled more effective use of current and future satellites to diagnose ground level conditions influencing air quality.\r\n\r\nDISCOVER-AQ employed two NASA aircraft, the P-3B and King Air, with the P-3B completing in-situ spiral profiling of the atmosphere (aerosol properties, meteorological variables, and trace gas species). The King Air conducted both passive and active remote sensing of the atmospheric column extending below the aircraft to the surface. Data from an existing network of surface air quality monitors, AERONET sun photometers, Pandora UV/vis spectrometers and model simulations were also collected. Further, DISCOVER-AQ employed many surface monitoring sites, with measurements being made on the ground, in conjunction with the aircraft. The B200 and P-3B conducted flights in Baltimore-Washington, D.C. in 2011, Houston, TX in 2013, San Joaquin Valley, CA in 2013, and Denver, CO in 2014. These regions were targeted due to being in violation of the National Ambient Air Quality Standards (NAAQS).\r\n\r\nThe first objective of DISCOVER-AQ was to determine and investigate correlations between surface measurements and satellite column observations for the trace gases ozone (O3), nitrogen dioxide (NO2), and formaldehyde (CH2O) to understand how satellite column observations can diagnose surface conditions. DISCOVER-AQ also had the objective of using surface-level measurements to understand how satellites measure diurnal variability and to understand what factors control diurnal variability. Lastly, DISCOVER-AQ aimed to explore horizontal scales of variability, such as regions with steep gradients and urban plumes.",
-            "title": "DISCOVER-AQ California Deployment Pandora Column Observations",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC%2FSUBORBITAL%2FDISCOVERAQ_California_Ground_Pandora_Data_1",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC%2FSUBORBITAL%2FDISCOVERAQ_California_Ground_Pandora_Data_1",
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
-                    "downloadURL": "https://pandora.gsfc.nasa.gov/",
-                    "description": "NASA Pandora Project Website",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Pandora Project Website",
+                    "downloadURL": "https://pandora.gsfc.nasa.gov/",
+                    "mediaType": "text/html",
                     "title": "View this dataset's calibration documentation"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/ASDC/SUBORBITAL/DISCOVERAQ_California_Ground_Pandora_Data_1",
-                    "description": "DOI for DISCOVERAQ_California_Ground_Pandora_Data_1",
                     "@type": "dcat:Distribution",
+                    "description": "DOI for DISCOVERAQ_California_Ground_Pandora_Data_1",
+                    "downloadURL": "https://doi.org/10.5067/ASDC/SUBORBITAL/DISCOVERAQ_California_Ground_Pandora_Data_1",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2404262905-LARC_ASDC",
-                    "description": "Earthdata Search client for DISCOVERAQ_California_Ground_Pandora_Data_1",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search client for DISCOVERAQ_California_Ground_Pandora_Data_1",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2404262905-LARC_ASDC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/DISCOVER-AQ/California_Ground_Pandora_Data_1/",
-                    "description": "ASDC Direct Data Download for DISCOVERAQ_California_Ground_Pandora_Data_1",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for DISCOVERAQ_California_Ground_Pandora_Data_1",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/DISCOVER-AQ/California_Ground_Pandora_Data_1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 }
             ],
+            "identifier": "C2404262905-LARC_ASDC",
+            "issued": "2021-08-19",
+            "keyword": [
+                "atmospheric chemistry",
+                "atmosphere",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/ASDC/SUBORBITAL/DISCOVERAQ_California_Ground_Pandora_Data_1",
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
             "spatial": "<?xml version=\"1.0\" encoding=\"UTF-8\"?><gml:Polygon xmlns:gml=\"http://www.opengis.net/gml/3.2\" srsName=\"EPSG:9825\"><gml:outerBoundaryIs><gml:LinearRing><gml:posList>25.0 -130.0 25.0 121.0 45.0 121.0 45.0 -130.0 25.0 -130.0</gml:posList></gml:LinearRing></gml:outerBoundaryIs><gml:innerBoundaryIs></gml:innerBoundaryIs></gml:Polygon>",
+            "temporal": "2012-12-02T00:00:00Z/2013-02-13T23:59:59.999Z",
             "theme": [
                 "DISCOVER-AQ",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "DISCOVER-AQ California Deployment Pandora Column Observations"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-PRL-0336-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the PRELANDING phase 2014-01-21 to 2014-11-18. It is a Global Gravity measurement at the comet 67P and covers the time 2014-10-05T05:07:05.000 to 2014-10-05T08:18:25.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-prl-0336-v1.0_wj73-ji38",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-PRL-0336-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-prl-0336-v1.0_wj73-ji38",
-            "description": "This is a Rosetta Radio Science data set, collected during the PRELANDING phase 2014-01-21 to 2014-11-18. It is a Global Gravity measurement at the comet 67P and covers the time 2014-10-05T05:07:05.000 to 2014-10-05T08:18:25.000.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     PRELANDING 0336 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     PRELANDING 0336 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=GIO-C-OPE-3-RDR-GRIGG-SKJELL-V1.0",
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
-                "26p/grigg-skjellerup 1 (1922 k1)",
-                "giotto extended mission"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This dataset includes raw and calibrated results from the Optical Probe Experiment (OPE) aboard the Giotto spacecraft during its extended mission to comet 26P/Grigg-Skjellerup, as well as the data used in the calibration.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.gio-c-ope-3-rdr-grigg-skjell-v1.0_wjae-dnta",
+            "issued": "2021-05-21",
+            "keyword": [
+                "26p/grigg-skjellerup 1 (1922 k1)",
+                "giotto extended mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=GIO-C-OPE-3-RDR-GRIGG-SKJELL-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.gio-c-ope-3-rdr-grigg-skjell-v1.0_wjae-dnta",
-            "description": "This dataset includes raw and calibrated results from the Optical Probe Experiment (OPE) aboard the Giotto spacecraft during its extended mission to comet 26P/Grigg-Skjellerup, as well as the data used in the calibration.",
-            "title": "GIOTTO EXTENDED MISSION, OPE, V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "GIOTTO EXTENDED MISSION, OPE, V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/NOAA-21/VIIRS/L3B/POC/2022",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/GSFC/SED/ESD/GCDC/OB.DAAC. https://doi.org/10.5067/NOAA-21/VIIRS/L3B/POC/2022.",
-            "issued": "2023-04-04",
-            "temporal": "2022-11-10T00:00:00Z/2023-04-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-04-04",
-            "keyword": [
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
-            "identifier": "C2652675332-OB_DAAC",
             "description": "The Visible and Infrared Imager/Radiometer Suite (VIIRS) is a multi-disciplinary instrument that is being flown on the Joint Polar Satellite System (JPSS) series of spacecraft, including the Suomi National Polar-orbiting Partnership (S-NPP) that launched in October 2011. JPSS is a multi-platform, multi-agency program that consolidates the polar orbiting spacecraft of NASA and the National Oceanic and Atmospheric Administration (NOAA). S-NPP is the initial spacecraft in this series, and VIIRS is the successor to MODIS for Earth science data product generation. VIIRS has 22 spectral bands ranging from 412 nm to 12 nm. There are 16 moderate-resolution bands (750m at nadir), 5 image-resolution bands (375m), and one day-night band (DNB).",
-            "title": "NOAA-21 VIIRS Global Binned Particulate Organic Carbon (POC) Data, version R2022.0",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FNOAA-21%2FVIIRS%2FL3B%2FPOC%2F2022",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FNOAA-21%2FVIIRS%2FL3B%2FPOC%2F2022",
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
-                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/data/10.5067/NOAA-21/VIIRS/L3B/POC/2022",
-                    "description": "VIIRS-NOAA-21 L3B Particulate Organic Carbon (POC) Dataset Landing Page",
                     "@type": "dcat:Distribution",
+                    "description": "VIIRS-NOAA-21 L3B Particulate Organic Carbon (POC) Dataset Landing Page",
+                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/data/10.5067/NOAA-21/VIIRS/L3B/POC/2022",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 }
             ],
+            "identifier": "C2652675332-OB_DAAC",
+            "issued": "2023-04-04",
+            "keyword": [
+                "earth science",
+                "ocean chemistry",
+                "oceans"
+            ],
+            "landingPage": "https://doi.org/10.5067/NOAA-21/VIIRS/L3B/POC/2022",
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
+            "title": "NOAA-21 VIIRS Global Binned Particulate Organic Carbon (POC) Data, version R2022.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.7927/H4862DC5",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Center for Hazards and Risk Research - CHRR - Columbia University, Center for International Earth Science Information Network - CIESIN - Columbia University, and International Bank for Reconstruction and Development - The World Bank. 2005-12-31. Global Cyclone Mortality Risks and Distribution. Version 1.00. Palisades, NY. Archived by National Aeronautics and Space Administration, U.S. Government, Center for Hazards and Risk Research (CHRR)/Columbia University. https://doi.org/10.7927/H4862DC5. https://doi.org/10.7927/H4862DC5.",
-            "issued": "2005-12-31",
-            "temporal": "2000-01-01T00:00:00Z/2000-12-31T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2005-12-31",
-            "references": [
-                "https://doi.org/10.7927/H4CZ353K",
-                "https://doi.org/10.7927/H40P0WXQ",
-                "https://doi.org/10.7927/H44F1NNF"
-            ],
-            "keyword": [
-                "natural hazards",
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
-            "identifier": "C179001768-SEDAC",
-            "description": "The Global Cyclone Mortality Risks and Distribution is a 2.5 minute grid of global cyclone mortality risks. Gridded Population of the World, Version 3 (GPWv3) data provide a baseline estimation of population per grid cell from which to estimate potential mortality loss. Mortality loss estimates per hazard event are calculated using regional, hazard-specific mortality records of the Emergency Events Database (EM-DAT) that span the 20 years between 1981 and 2000. Data regarding the frequency and distribution of cyclone hazard are obtained from the Global Cyclone Hazard Frequency and Distribution data set. In order to more accurately reflect the confidence associated with the data and procedures, the potential mortality estimate range is classified into deciles, 10 classes of an approximately equal number of grid cells, providing a relative estimate of cyclone-based mortality risks. This data set is the result of collaboration among the Columbia University Center for Hazards and Risk Research (CHRR), International Bank for Reconstruction and Development/The World Bank, and Columbia University Center for International Earth Science Information Network (CIESIN).",
-            "release-place": "Palisades, NY",
-            "graphic-preview-description": "Maps Download Page",
             "creator": "Center for Hazards and Risk Research - CHRR - Columbia University, Center for International Earth Science Information Network - CIESIN - Columbia University, and International Bank for Reconstruction and Development - The World Bank",
-            "title": "Global Cyclone Mortality Risks and Distribution",
-            "graphic-preview-file": "https://sedac.ciesin.columbia.edu/data/set/ndh-cyclone-mortality-risks-distribution/maps",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The Global Cyclone Mortality Risks and Distribution is a 2.5 minute grid of global cyclone mortality risks. Gridded Population of the World, Version 3 (GPWv3) data provide a baseline estimation of population per grid cell from which to estimate potential mortality loss. Mortality loss estimates per hazard event are calculated using regional, hazard-specific mortality records of the Emergency Events Database (EM-DAT) that span the 20 years between 1981 and 2000. Data regarding the frequency and distribution of cyclone hazard are obtained from the Global Cyclone Hazard Frequency and Distribution data set. In order to more accurately reflect the confidence associated with the data and procedures, the potential mortality estimate range is classified into deciles, 10 classes of an approximately equal number of grid cells, providing a relative estimate of cyclone-based mortality risks. This data set is the result of collaboration among the Columbia University Center for Hazards and Risk Research (CHRR), International Bank for Reconstruction and Development/The World Bank, and Columbia University Center for International Earth Science Information Network (CIESIN).",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.7927%2FH4862DC5",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.7927%2FH4862DC5",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/downloads/maps/ndh/ndh-cyclone-mortality-risks-distribution/cyclone-mortality-thumbnail.jpg",
-                    "description": "Sample browse graphic of the data set.",
                     "@type": "dcat:Distribution",
+                    "description": "Sample browse graphic of the data set.",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/downloads/maps/ndh/ndh-cyclone-mortality-risks-distribution/cyclone-mortality-thumbnail.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/ndh-cyclone-mortality-risks-distribution/data-download",
-                    "description": "Data Download Page",
                     "@type": "dcat:Distribution",
+                    "description": "Data Download Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/ndh-cyclone-mortality-risks-distribution/data-download",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/ndh-cyclone-mortality-risks-distribution/maps",
-                    "description": "Maps Download Page",
                     "@type": "dcat:Distribution",
+                    "description": "Maps Download Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/ndh-cyclone-mortality-risks-distribution/maps",
+                    "mediaType": "text/html",
                     "title": "Get a related map visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/ndh-cyclone-mortality-risks-distribution/maps/services",
-                    "description": "Web Map Service Page",
                     "@type": "dcat:Distribution",
+                    "description": "Web Map Service Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/ndh-cyclone-mortality-risks-distribution/maps/services",
+                    "mediaType": "text/html",
                     "title": "Use Web Map Service (WMS) to download the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/ndh-cyclone-mortality-risks-distribution",
-                    "description": "Data Set\u00a0Overview Page",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set\u00a0Overview Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/ndh-cyclone-mortality-risks-distribution",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "graphic-preview-description": "Maps Download Page",
+            "graphic-preview-file": "https://sedac.ciesin.columbia.edu/data/set/ndh-cyclone-mortality-risks-distribution/maps",
+            "identifier": "C179001768-SEDAC",
+            "issued": "2005-12-31",
+            "keyword": [
+                "natural hazards",
+                "human dimensions",
+                "population",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.7927/H4862DC5",
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
+                "https://doi.org/10.7927/H4CZ353K",
+                "https://doi.org/10.7927/H40P0WXQ",
+                "https://doi.org/10.7927/H44F1NNF"
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
+            "title": "Global Cyclone Mortality Risks and Distribution"
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
+                    "downloadURL": "http://turbmodels.larc.nasa.gov/Other_exp_Data/Coanda/Cmu_0.150_Spanwise_Pressures.dat",
+                    "mediaType": "application/dat"
+                }
             ],
+            "identifier": "NASA-851__14",
+            "issued": "2018-06-25",
             "keyword": [
                 "experiment",
                 "validation",
@@ -1579078,45 +1579087,38 @@
                 "models",
                 "turbulence"
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
-            "identifier": "NASA-851__14",
-            "description": "2-D Coanda Airfoil with Tangential Wall Jet. This web page provides data from experiments that may be useful for the validation of turbulence models. This resource is expected to grow gradually over time. All data herein arepublicly available.",
-            "title": "Turbulence Models: Data from Other Experiments: 2-D Coanda Airfoil with Tangential Wall Jet",
-            "programCode": [
-                "026:023"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://turbmodels.larc.nasa.gov/Other_exp_Data/Coanda/Cmu_0.150_Spanwise_Pressures.dat",
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
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=GO-A%2FC-SSI-2-REDR-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This data set has been generated by NASA's Galileo Project in order to distribute the images acquired by the Solid State Imaging (SSI) camera to the scientists and later to the Planetary Data System (PDS). The collection resides on volume GO_0016 and consists of all images acquired by the Galileo spacecraft during the period from the flyby of Ida through the Shoemaker-Levy 9 (SL9) comet impact on Jupiter. This includes data from SCLK 197327200 through 249221800 and contains the following targets: stars, Ida and Jupiter.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.go-a-c-ssi-2-redr-v1.0_wjfy-hbm3",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "non science",
                 "jupiter",
@@ -1579124,417 +1579126,429 @@
                 "galileo",
                 "comet sl9/jupiter collision"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=GO-A%2FC-SSI-2-REDR-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.go-a-c-ssi-2-redr-v1.0_wjfy-hbm3",
-            "description": "This data set has been generated by NASA's Galileo Project in order to distribute the images acquired by the Solid State Imaging (SSI) camera to the scientists and later to the Planetary Data System (PDS). The collection resides on volume GO_0016 and consists of all images acquired by the Galileo spacecraft during the period from the flyby of Ida through the Shoemaker-Levy 9 (SL9) comet impact on Jupiter. This includes data from SCLK 197327200 through 249221800 and contains the following targets: stars, Ida and Jupiter.",
-            "title": "GALILEO ORBITER ASTEROID AND COMET SL9 SOLID STATE IMAGING 2",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "GALILEO ORBITER ASTEROID AND COMET SL9 SOLID STATE IMAGING 2"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-3-RDR-OCCULTATIONS-V10.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This data set is intended to include all reported timings of observed asteroid, planet, and planetary satellite occultation events as well as occultation axes derived from those timings by David W. Dunham and David Herald. This version is complete through February 2012.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-3-rdr-occultations-v10.0_wjjx-xxbz",
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
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-3-RDR-OCCULTATIONS-V10.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-3-rdr-occultations-v10.0_wjjx-xxbz",
-            "description": "This data set is intended to include all reported timings of observed asteroid, planet, and planetary satellite occultation events as well as occultation axes derived from those timings by David W. Dunham and David Herald. This version is complete through February 2012.",
-            "title": "ASTEROID OCCULTATIONS V10.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "ASTEROID OCCULTATIONS V10.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=DAWN-A-GRAND-5-VESTA-ABSORPTION-V1.0",
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
-                "4 vesta"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "A global map of a unitless\ncompositional parameter, delta-C_perpendicular (DCP), and propagated\n1-sigma uncertainties is provided.  DCP varies linearly with the\nmacroscopic thermal neutron absorption cross section of Vesta's\nregolith.  An equation for converting tabulated DCP values to\nabsorption units is provided in this document. DCP was determined from\nthermal and epithermal neutron counting rates measured by the NASA\nDawn mission's Gamma Ray and Neutron Detector (GRaND) while in low\naltitude mapping orbit, about 210 km from Vesta's surface.  The\nmeasurements are representative of Vesta's bulk regolith composition\nto depths of a few decimeters with a spatial resolution of about\n300-km full-width-at-half-maximum of arc length on the surface.  The\nmethods used to determine neutron absorption are described by\nPRETTYMANETAL2013.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.dawn-a-grand-5-vesta-absorption-v1.0_wjmz-kg6q",
+            "issued": "2021-05-21",
+            "keyword": [
+                "dawn mission to vesta and ceres",
+                "4 vesta"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=DAWN-A-GRAND-5-VESTA-ABSORPTION-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.dawn-a-grand-5-vesta-absorption-v1.0_wjmz-kg6q",
-            "description": "A global map of a unitless\ncompositional parameter, delta-C_perpendicular (DCP), and propagated\n1-sigma uncertainties is provided.  DCP varies linearly with the\nmacroscopic thermal neutron absorption cross section of Vesta's\nregolith.  An equation for converting tabulated DCP values to\nabsorption units is provided in this document. DCP was determined from\nthermal and epithermal neutron counting rates measured by the NASA\nDawn mission's Gamma Ray and Neutron Detector (GRaND) while in low\naltitude mapping orbit, about 210 km from Vesta's surface.  The\nmeasurements are representative of Vesta's bulk regolith composition\nto depths of a few decimeters with a spatial resolution of about\n300-km full-width-at-half-maximum of arc length on the surface.  The\nmethods used to determine neutron absorption are described by\nPRETTYMANETAL2013.",
-            "title": "DAWN GRAND MAP VESTA NEUTRON ABSORPTION\n                                      V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "DAWN GRAND MAP VESTA NEUTRON ABSORPTION\n                                      V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/KE2LG72Z89LN",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "High Mountain Asia Glacier Thickness Change Mosaics from Multi-Sensor DEMs V001. Version 1. Archived by National Aeronautics and Space Administration, U.S. Government, NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/KE2LG72Z89LN.",
-            "issued": "1974-01-01",
-            "temporal": "1974-01-01T00:00:00Z/2017-12-31T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2017-12-31",
-            "keyword": [
-                "earth science",
-                "ngda",
-                "national geospatial data asset",
-                "glaciers/ice sheets",
-                "cryosphere"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Joshua Maurer",
                 "hasEmail": "mailto:jmaurer@ldeo.columbia.edu"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA NSIDC DAAC"
-            },
-            "identifier": "C1591209290-NSIDC_ECS",
             "description": "This data set contains thickness change mosaics that include approximately 650 Himalayan glaciers between 1975 and 2000, and 1040 Himalayan glaciers between 2000 and 2016. The data were derived from HEXAGON KH-9 and ASTER digital elevation models (DEMs), by fitting robust linear trends to time series of elevation pixels over the glacier surfaces.",
-            "title": "High Mountain Asia Glacier Thickness Change Mosaics from Multi-Sensor DEMs V001",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FKE2LG72Z89LN",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FKE2LG72Z89LN",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/HMA/HMA_Glacier_dH_Mosaics.001/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/HMA/HMA_Glacier_dH_Mosaics.001/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1591209290-NSIDC_ECS&m=16.592379857766502%2183.7652587890625%213%211%210%210%2C2&tl=1541002257%214%21%21&q=hma&ok=hma",
-                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1591209290-NSIDC_ECS&m=16.592379857766502%2183.7652587890625%213%211%210%210%2C2&tl=1541002257%214%21%21&q=hma&ok=hma",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/data/data-access-tool/HMA_Glacier_dH_Mosaics/versions/1/",
-                    "description": "Data Access link for ITSD project",
                     "@type": "dcat:Distribution",
+                    "description": "Data Access link for ITSD project",
+                    "downloadURL": "https://nsidc.org/data/data-access-tool/HMA_Glacier_dH_Mosaics/versions/1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/HMA/HMA_Glacier_dH_Mosaics.001/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/HMA/HMA_Glacier_dH_Mosaics.001/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1591209290-NSIDC_ECS&m=16.592379857766502%2183.7652587890625%213%211%210%210%2C2&tl=1541002257%214%21%21&q=hma&ok=hma",
-                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1591209290-NSIDC_ECS&m=16.592379857766502%2183.7652587890625%213%211%210%210%2C2&tl=1541002257%214%21%21&q=hma&ok=hma",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/data/data-access-tool/HMA_Glacier_dH_Mosaics/versions/1/",
-                    "description": "Data Access link for ITSD project",
                     "@type": "dcat:Distribution",
+                    "description": "Data Access link for ITSD project",
+                    "downloadURL": "https://nsidc.org/data/data-access-tool/HMA_Glacier_dH_Mosaics/versions/1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/KE2LG72Z89LN",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/KE2LG72Z89LN",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/KE2LG72Z89LN",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/KE2LG72Z89LN",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C1591209290-NSIDC_ECS",
+            "issued": "1974-01-01",
+            "keyword": [
+                "earth science",
+                "ngda",
+                "national geospatial data asset",
+                "glaciers/ice sheets",
+                "cryosphere"
+            ],
+            "landingPage": "https://doi.org/10.5067/KE2LG72Z89LN",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2017-12-31",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA NSIDC DAAC"
+            },
             "spatial": "75.4 27.4 92.9 34.4",
+            "temporal": "1974-01-01T00:00:00Z/2017-12-31T23:59:59.999Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "High Mountain Asia Glacier Thickness Change Mosaics from Multi-Sensor DEMs V001"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG2-N-PWS-2-RDR-SA-4SEC-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This data set consists of 4-second edited, wave electric field intensities from the Voyager 2 Plasma Wave Receiver (PWS) spectrum analyzer obtained in the vicinity of the Neptunian magnetosphere. For each 4-second interval, a field strength is determined for each of the 16 spectrum analyzer channels whose center frequencies range from 10 Hertz to 56.2 kiloHertz and which are logarithmically spaced in frequency, four channels per decade. The time associated with each set of intensities (16 channels) is the time of the beginning of the scan. During data gaps where complete 4-second spectra are missing, no entries exist in the file, that is, the gaps are not zero-filled or tagged in any other way. When one or more channels are missing within a scan, the missing measurements are zero-filled. Data are edited but not calibrated. The data numbers in this data set can be plotted in raw form for event searches and simple trend analysis since they are roughly proportional to the log of the electric field strength. Calibration procedures and tables are provided for use with this data set",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg2-n-pws-2-rdr-sa-4sec-v1.0_wjph-akju",
             "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "neptune",
                 "voyager",
                 "comet sl9/jupiter collision"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG2-N-PWS-2-RDR-SA-4SEC-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg2-n-pws-2-rdr-sa-4sec-v1.0_wjph-akju",
-            "description": "This data set consists of 4-second edited, wave electric field intensities from the Voyager 2 Plasma Wave Receiver (PWS) spectrum analyzer obtained in the vicinity of the Neptunian magnetosphere. For each 4-second interval, a field strength is determined for each of the 16 spectrum analyzer channels whose center frequencies range from 10 Hertz to 56.2 kiloHertz and which are logarithmically spaced in frequency, four channels per decade. The time associated with each set of intensities (16 channels) is the time of the beginning of the scan. During data gaps where complete 4-second spectra are missing, no entries exist in the file, that is, the gaps are not zero-filled or tagged in any other way. When one or more channels are missing within a scan, the missing measurements are zero-filled. Data are edited but not calibrated. The data numbers in this data set can be plotted in raw form for event searches and simple trend analysis since they are roughly proportional to the log of the electric field strength. Calibration procedures and tables are provided for use with this data set",
-            "title": "VG2 NEP PWS EDITED RDR UNCALIB SPECTRUM ANALYZER 4SEC V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "VG2 NEP PWS EDITED RDR UNCALIB SPECTRUM ANALYZER 4SEC V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=IHW-C-PPOL-3-RDR-GZ-V1.0",
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
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ihw-c-ppol-3-rdr-gz-v1.0_wjqm-ipf7",
+            "issued": "2018-06-26",
+            "keyword": [
+                "international halley watch",
+                "halley"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=IHW-C-PPOL-3-RDR-GZ-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ihw-c-ppol-3-rdr-gz-v1.0_wjqm-ipf7",
-            "description": "In preparation for the concerted international study of Comet Halley, the IHW conducted a trial run with observations of Comet Crommelin, largely during February and March of 1984.",
-            "title": "IHW COMET PPOL CALIBRATED REDUCED DATA RECORD GZ V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "IHW COMET PPOL CALIBRATED REDUCED DATA RECORD GZ V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RPCICA-2-EXT1-RAW-V1.0",
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
+            "description": "This dataset contains RAW DATA from the RPCICA instrument on\nmission ROSETTA during Rosetta extension 1.\nData contains measurements of solar wind interaction\nwith the atmosphere of target comet 67P.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rpcica-2-ext1-raw-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RPCICA-2-EXT1-RAW-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rpcica-2-ext1-raw-v1.0",
-            "description": "This dataset contains RAW DATA from the RPCICA instrument on\nmission ROSETTA during Rosetta extension 1.\nData contains measurements of solar wind interaction\nwith the atmosphere of target comet 67P.",
-            "title": "ROSETTA-ORBITER 67P RPCICA 2 EXT1 UNCALIBRATED V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RPCICA 2 EXT1 UNCALIBRATED V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ASDC_DAAC/ATTREX/0002",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2015-05-28. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/ASDC_DAAC/ATTREX/0002. https://asdc.larc.nasa.gov/project/ATTREX.",
-            "issued": "2015-01-30",
-            "temporal": "2011-10-01T00:00:00Z/2013-03-01T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2018-07-23",
-            "keyword": [
-                "earth science",
-                "clouds",
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
-            "identifier": "C1536056461-LARC_ASDC",
             "description": "ATTREX-Aircraft_insitu_Cloud_property_Measurements are in-situ cloud measurements collected onboard the Global Hawk Unihabited Aerial System (UAS) during the Airborne Tropical TRopopause EXperiment (ATTREX) campaign. This collection consists of in-situ cloud properties collected by the Hawkeye-FCDP (Hawkeye-Fast Cloud Droplet Probe) during the 2011 and 2013 deployments over California, and 2014 deployment over Guam. Data collection is complete.\nEven though it is typically found in low concentrations, stratospheric water vapor has large impacts on the Earth\u2019s climate and energy budget. Studies have suggested that even relatively small changes in stratospheric humidity may have significant climate impacts and future changes in stratospheric humidity and ozone concentration in response to a changing climate are significant climate feedback. Tropospheric water vapor climate feedback is typically well represented in global models. However, predictions of future changes in stratospheric humidity are highly uncertain due to gaps in our understanding of physical processes occurring in the region of the atmosphere that controls the composition of the stratosphere, the Tropical Tropopause Layer (TTL, ~13-18 km). The ability to predict future changes in stratospheric ozone are also limited due to uncertainties in the chemical composition of the TTL. In order to address these uncertainties, the Airborne Tropical Tropopause Experiment (ATTREX) was completed. Instruments during ATTREX provided measurements to trace the movement of reactive halogen-containing compounds and other important chemical species, the size and shape of cirrus cloud particles, water vapor, and winds in three dimensions through the TTL. Bromine-containing gases were measured to improve understanding of stratospheric ozone. ATTREX consisted of four NASA Global Hawk Uninhabited Aerial System (UAS) campaigns deployed from NASA\u2019s Armstrong Flight Research Center (formally Dryden Flight Research Center). Campaigns were deployed over Edwards, CA, Guam, Hawaii, and Darwin, Australia in Boreal summer, winter, fall, and summer, respectively.",
-            "title": "ATTREX-Aircraft_insitu_Cloud_property_Measurements",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC_DAAC%2FATTREX%2F0002",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC_DAAC%2FATTREX%2F0002",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/project/ATTREX",
-                    "description": "ASDC Data and Information for ATTREX",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Data and Information for ATTREX",
+                    "downloadURL": "https://asdc.larc.nasa.gov/project/ATTREX",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/ASDC_DAAC/ATTREX/0002",
-                    "description": "DOI data set landing page for ATTREX-Aircraft_insitu_Cloud_property_Measurements_1",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for ATTREX-Aircraft_insitu_Cloud_property_Measurements_1",
+                    "downloadURL": "https://doi.org/10.5067/ASDC_DAAC/ATTREX/0002",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1536056461-LARC_ASDC",
-                    "description": "Earthdata Search for ATTREX-Aircraft_insitu_Cloud_property_Measurements_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for ATTREX-Aircraft_insitu_Cloud_property_Measurements_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1536056461-LARC_ASDC",
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
-                    "downloadURL": "https://espoarchive.nasa.gov/archive/browse/attrex",
-                    "description": "ESPO Data Archive for ATTREX",
                     "@type": "dcat:Distribution",
+                    "description": "ESPO Data Archive for ATTREX",
+                    "downloadURL": "https://espoarchive.nasa.gov/archive/browse/attrex",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/ATTREX/Aircraft_insitu_Cloud_property_Measurements_1/",
-                    "description": "ASDC Direct Data Download for ATTREX-Aircraft_insitu_Cloud_property_Measurements_1",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for ATTREX-Aircraft_insitu_Cloud_property_Measurements_1",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/ATTREX/Aircraft_insitu_Cloud_property_Measurements_1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 }
             ],
+            "identifier": "C1536056461-LARC_ASDC",
+            "issued": "2015-01-30",
+            "keyword": [
+                "earth science",
+                "clouds",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.5067/ASDC_DAAC/ATTREX/0002",
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
             "spatial": "-135.6 -12.3 -113.2 36.1",
+            "temporal": "2011-10-01T00:00:00Z/2013-03-01T23:59:59Z",
             "theme": [
                 "ATTREX",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "ATTREX-Aircraft_insitu_Cloud_property_Measurements"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.nasa.gov/d/wjun-bf9r",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "GeneLab Outreach",
+                "hasEmail": "mailto:genelab-outreach@lists.nasa.gov"
+            },
+            "description": "Analysis of human peripheral blood 48 hours after irradiation ex vivo with graded doses of gamma rays. Results have been used in building and testing classifiers to predict exposure dose for use in radiological triage and also provide insight into immune cell responses. Results were compared with those from earlier times and from patients exposed in vivo. Peripheral blood from 5 healthy donors was exposed ex vivo to 0. 0.5 2 5 or 8 Gy gamma-rays and gene expression was analyzed up to 48 hours after exposure.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "GeneLab Study Page",
+                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-157",
+                    "mediaType": "text/html",
+                    "title": "Gene expression in human peripheral blood 48 hours after exposure to ionizing radiation"
+                }
+            ],
+            "identifier": "nasa_genelab_GLDS-157_wjun-bf9r",
             "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
             "keyword": [
                 "p-gse44201-3",
                 "p-gse44201-1",
@@ -1579556,514 +1579570,502 @@
                 "p-gse44201-2",
                 "nucleic acid extraction protocol"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "GeneLab Outreach",
-                "hasEmail": "mailto:genelab-outreach@lists.nasa.gov"
-            },
+            "landingPage": "https://data.nasa.gov/d/wjun-bf9r",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "nasa_genelab_GLDS-157_wjun-bf9r",
-            "description": "Analysis of human peripheral blood 48 hours after irradiation ex vivo with graded doses of gamma rays. Results have been used in building and testing classifiers to predict exposure dose for use in radiological triage and also provide insight into immune cell responses. Results were compared with those from earlier times and from patients exposed in vivo. Peripheral blood from 5 healthy donors was exposed ex vivo to 0. 0.5 2 5 or 8 Gy gamma-rays and gene expression was analyzed up to 48 hours after exposure.",
-            "title": "Gene expression in human peripheral blood 48 hours after exposure to ionizing radiation",
-            "programCode": [
-                "026:005"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-157",
-                    "description": "GeneLab Study Page",
-                    "@type": "dcat:Distribution",
-                    "title": "Gene expression in human peripheral blood 48 hours after exposure to ionizing radiation"
-                }
-            ],
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "Gene expression in human peripheral blood 48 hours after exposure to ionizing radiation"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/CYGNS-L2H32",
             "citation": "CYGNSS. 2024-06-28. CYGNSS Level 2 Ocean Surface Heat Flux Science Data Record. Version 3.2. CYGNSS Level 2 Ocean Surface Heat Flux Science Data Record Version 3.2. PO.DAAC. Archived by National Aeronautics and Space Administration, U.S. Government, PO.DAAC. https://doi.org/10.5067/CYGNS-L2H32. https://cygnss.engin.umich.edu/. CYGNSS, PO.DAAC, 2019-08-11, CYGNSS Level 2 Ocean Surface Heat Flux Science Data Record Version 1.0, https://cygnss.engin.umich.edu/.",
-            "issued": "2022-04-16",
-            "temporal": "2018-08-01T00:00:00Z/2024-06-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-04-29",
-            "references": [
-                "https://doi.org/10.3390/rs11192294"
-            ],
-            "keyword": [
-                "oceans",
-                "ocean temperature",
-                "earth science",
-                "ocean heat budget"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "undefined",
                 "hasEmail": "mailto:podaac@podaac.jpl.nasa.gov"
             },
-            "identifier": "C2927907727-POCLOUD",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/JPL/PODAAC"
-            },
-            "description": "The CYGNSS level 2 ocean surface heat flux science data record version 3.2 dataset is provided as a service to the oceanographic and meteorological research communities on behalf of a NASA ROSES funded project within CYGNSS Science Team in direct collaboration with the Cyclone Global Navigation Satellite System (CYGNSS) Mission. CYGNSS was launched on 15 December 2016, it is a NASA Earth System Science Pathfinder Mission that was launched with the purpose of collecting the first frequent space\u2010based measurements of surface wind speeds in the inner core of tropical cyclones. Originally made up of a constellation of eight micro-satellites, the observatories provide nearly gap-free Earth coverage using an orbital inclination of approximately 35\u00b0 from the equator, with a mean (i.e., average) revisit time of seven hours and a median revisit time of three hours. \r\n<br><br>\r\nThis dataset provides time-tagged and geolocated ocean surface heat flux parameters with 25x25 kilometer footprint resolution from the Delay Doppler Mapping Instrument (DDMI) aboard the CYGNSS satellite constellation. The reported sample locations are determined by the specular points corresponding to the Delay Doppler Maps (DDMs). Version 3.2 uses CYGNSS Level 2 (L2) Science Data Record (SDR) Version 3.2 surface wind speeds and ECMWF Reanalysis, Version 5 (ERA5). The Coupled Ocean-Atmosphere Response Experiment (COARE) algorithm is what is used in this dataset to estimate the latent and sensible heat fluxes and their respective transfer coefficients. While COARE's initial intentions were for low to moderate wind speeds, the version used for this product, COARE 3.5, has been verified with direct in situ flux measurements for wind speeds up to 25 m/s. As CYGNSS does not provide air/sea temperature, humidity, surface pressure or density, the producer of this dataset obtains these values from this dataset obtains these values from ERA5. This dataset is made available from 1 August 2018 to present with an approximate 1 week latency in the netCDF-4 formatted data files, where each file contains data within a 24-hour UTC period from a combination of up to 8 unique CYGNSS spacecraft. More information on CYGNSS can be found on the CYGNSS mission page.",
-            "release-place": "PO.DAAC",
-            "series-name": "CYGNSS Level 2 Ocean Surface Heat Flux Science Data Record",
             "creator": "CYGNSS",
-            "title": "CYGNSS Level 2 Ocean Surface Heat Flux Science Data Record Version 3.2",
-            "graphic-preview-description": "Thumbnail",
-            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/CYGNSS_L2_SURFACE_FLUX_V2.0.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The CYGNSS level 2 ocean surface heat flux science data record version 3.2 dataset is provided as a service to the oceanographic and meteorological research communities on behalf of a NASA ROSES funded project within CYGNSS Science Team in direct collaboration with the Cyclone Global Navigation Satellite System (CYGNSS) Mission. CYGNSS was launched on 15 December 2016, it is a NASA Earth System Science Pathfinder Mission that was launched with the purpose of collecting the first frequent space\u2010based measurements of surface wind speeds in the inner core of tropical cyclones. Originally made up of a constellation of eight micro-satellites, the observatories provide nearly gap-free Earth coverage using an orbital inclination of approximately 35\u00b0 from the equator, with a mean (i.e., average) revisit time of seven hours and a median revisit time of three hours. \r\n<br><br>\r\nThis dataset provides time-tagged and geolocated ocean surface heat flux parameters with 25x25 kilometer footprint resolution from the Delay Doppler Mapping Instrument (DDMI) aboard the CYGNSS satellite constellation. The reported sample locations are determined by the specular points corresponding to the Delay Doppler Maps (DDMs). Version 3.2 uses CYGNSS Level 2 (L2) Science Data Record (SDR) Version 3.2 surface wind speeds and ECMWF Reanalysis, Version 5 (ERA5). The Coupled Ocean-Atmosphere Response Experiment (COARE) algorithm is what is used in this dataset to estimate the latent and sensible heat fluxes and their respective transfer coefficients. While COARE's initial intentions were for low to moderate wind speeds, the version used for this product, COARE 3.5, has been verified with direct in situ flux measurements for wind speeds up to 25 m/s. As CYGNSS does not provide air/sea temperature, humidity, surface pressure or density, the producer of this dataset obtains these values from this dataset obtains these values from ERA5. This dataset is made available from 1 August 2018 to present with an approximate 1 week latency in the netCDF-4 formatted data files, where each file contains data within a 24-hour UTC period from a combination of up to 8 unique CYGNSS spacecraft. More information on CYGNSS can be found on the CYGNSS mission page.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FCYGNS-L2H32",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FCYGNS-L2H32",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/cygnss/open/L2/docs/148-0138_ATBD_L2_Wind_Speed_Retrieval_Rev5_Aug2018_release.pdf",
-                    "description": "Level 2 Wind Speed Retrieval Algorithm Theoretical Basis Document, M. P. Clarizia, V. Zavarotny, C. Ruf, CYGNSS Project Document 148-0138, Rev 5, 17 Aug. 2018.",
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
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/cygnss/open/L2/docs/148-0382-6_Level_2_Surface_Flux_netCDF_Data_Dictionary.xlsx",
-                    "description": "Data Variable Dictionary",
                     "@type": "dcat:Distribution",
+                    "description": "Data Variable Dictionary",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/cygnss/open/L2/docs/148-0382-6_Level_2_Surface_Flux_netCDF_Data_Dictionary.xlsx",
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
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2927907727-POCLOUD",
-                    "description": "HTTPS endpoint for data browse and download",
                     "@type": "dcat:Distribution",
+                    "description": "HTTPS endpoint for data browse and download",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2927907727-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2927907727-POCLOUD",
-                    "description": "Browse granule search results in Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse granule search results in Earthdata Search",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2927907727-POCLOUD",
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
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://podaac.github.io/tutorials/",
-                    "description": "PO.DAAC Cookbook",
                     "@type": "dcat:Distribution",
+                    "description": "PO.DAAC Cookbook",
+                    "downloadURL": "https://podaac.github.io/tutorials/",
+                    "mediaType": "text/html",
                     "title": "View this dataset's data recipes"
                 }
             ],
+            "graphic-preview-description": "Thumbnail",
+            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/CYGNSS_L2_SURFACE_FLUX_V2.0.jpg",
+            "identifier": "C2927907727-POCLOUD",
+            "issued": "2022-04-16",
+            "keyword": [
+                "oceans",
+                "ocean temperature",
+                "earth science",
+                "ocean heat budget"
+            ],
+            "landingPage": "https://doi.org/10.5067/CYGNS-L2H32",
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
+            "temporal": "2018-08-01T00:00:00Z/2024-06-17T00:00:00Z",
             "theme": [
                 "CYGNSS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "CYGNSS Level 2 Ocean Surface Heat Flux Science Data Record Version 3.2"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1339",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Moghaddam, M., A.R. Silva, D. Clewley, R. Akbar, S.A. Hussaini, J. Whitcomb, R. Devarakonda, R. Shrestha, R.B. Cook, G. Prakash, S.K. Santhana Vannan, and A.G. Boyer. 2017. Soil Moisture Profiles and Temperature Data from SoilSCAPE Sites, USA. ORNL DAAC, Oak Ridge, Tennessee, USA. https://doi.org/10.3334/ORNLDAAC/1339",
-            "issued": "2024-02-19",
-            "temporal": "2011-08-03T00:00:00Z/2019-12-14T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-03-04",
-            "keyword": [
-                "soils",
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
-            "identifier": "C2736724942-ORNL_CLOUD",
             "description": "This data set contains in-situ soil moisture profile and soil temperature data collected at 20-minute intervals at SoilSCAPE (Soil moisture Sensing Controller and oPtimal Estimator) project sites in four states (California, Arizona, Oklahoma, and Michigan) in the United States. SoilSCAPE used wireless sensor technology to acquire high temporal resolution soil moisture and temperature data at up to 12 sites over varying durations since August 2011. At its maximum, the network consisted of over 200 wireless sensor installations (nodes), with a range of 6 to 27 nodes per site. The soil moisture sensors (EC-5 and 5-TM from Decagon Devices) were installed at three to four depths, nominally at 5, 20, and 50 cm below the surface. Soil conditions (e.g., hard soil or rocks) may have limited sensor placement. Temperature sensors were installed at 5 cm depth at six of the sites. Data collection started in August 2011 and continues at eight sites through the present. The data enables estimation of local-scale soil moisture at high temporal resolution and validation of remote sensing estimates of soil moisture at regional (airborne, e.g. NASA's Airborne Microwave Observation of Subcanopy and Subsurface Mission - AirMOSS) and national (spaceborne, e.g. NASA's Soil Moisture Active Passive - SMAP) scales.",
-            "graphic-preview-description": "Browse Image",
-            "title": "Soil Moisture Profiles and Temperature Data from SoilSCAPE Sites, USA",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/sdat-tds/1339_1_fit.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1339",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1339",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/eos_land_val/SoilSCAPE/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/eos_land_val/SoilSCAPE/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/LAND_VAL/guides/SoilSCAPE.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/LAND_VAL/guides/SoilSCAPE.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1339",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1339",
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
-                    "mediaType": "application/zip",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/eos_land_val/SoilSCAPE/comp/NodePhotos.zip",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/eos_land_val/SoilSCAPE/comp/NodePhotos.zip",
+                    "mediaType": "application/zip",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/eos_land_val/SoilSCAPE/comp/SoilSCAPE.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/eos_land_val/SoilSCAPE/comp/SoilSCAPE.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/eos_land_val/SoilSCAPE/comp/SoilScape_BLMLand3NTonzi_CA.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/eos_land_val/SoilSCAPE/comp/SoilScape_BLMLand3NTonzi_CA.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/eos_land_val/SoilSCAPE/comp/SoilScape_BLM_Land_STonzi_CA.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/eos_land_val/SoilSCAPE/comp/SoilScape_BLM_Land_STonzi_CA.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/eos_land_val/SoilSCAPE/comp/SoilScape_CantonOK.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/eos_land_val/SoilSCAPE/comp/SoilScape_CantonOK.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/eos_land_val/SoilSCAPE/comp/SoilScape_KendallAZ.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/eos_land_val/SoilSCAPE/comp/SoilScape_KendallAZ.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/eos_land_val/SoilSCAPE/comp/SoilScape_LuckyHillsAZ.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/eos_land_val/SoilSCAPE/comp/SoilScape_LuckyHillsAZ.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/eos_land_val/SoilSCAPE/comp/SoilScape_MatthaeiGardensMI.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/eos_land_val/SoilSCAPE/comp/SoilScape_MatthaeiGardensMI.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/eos_land_val/SoilSCAPE/comp/SoilScape_NewHoganLakeCA.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/eos_land_val/SoilSCAPE/comp/SoilScape_NewHoganLakeCA.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/eos_land_val/SoilSCAPE/comp/SoilScape_Terra_dOro_VineyardCA.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/eos_land_val/SoilSCAPE/comp/SoilScape_Terra_dOro_VineyardCA.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/eos_land_val/SoilSCAPE/comp/SoilScape_TonziCA.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/eos_land_val/SoilSCAPE/comp/SoilScape_TonziCA.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/eos_land_val/SoilSCAPE/comp/SoilScape_VairaCA.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/eos_land_val/SoilSCAPE/comp/SoilScape_VairaCA.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://daac.ornl.gov/graphics/browse/sdat-tds/1339_1_fit.png",
-                    "description": "Browse Image",
                     "@type": "dcat:Distribution",
+                    "description": "Browse Image",
+                    "downloadURL": "https://daac.ornl.gov/graphics/browse/sdat-tds/1339_1_fit.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://thredds.daac.ornl.gov/thredds/catalog/ornldaac/1339/catalog.html",
-                    "description": "The THREDDS location for this Collection.",
                     "@type": "dcat:Distribution",
+                    "description": "The THREDDS location for this Collection.",
+                    "downloadURL": "https://thredds.daac.ornl.gov/thredds/catalog/ornldaac/1339/catalog.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "graphic-preview-description": "Browse Image",
+            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/sdat-tds/1339_1_fit.png",
+            "identifier": "C2736724942-ORNL_CLOUD",
+            "issued": "2024-02-19",
+            "keyword": [
+                "soils",
+                "earth science",
+                "land surface"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1339",
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
             "spatial": "-120.99 31.74 -83.66 42.3",
+            "temporal": "2011-08-03T00:00:00Z/2019-12-14T23:59:59Z",
             "theme": [
                 "EOS LAND VAL",
                 "AirMOSS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Soil Moisture Profiles and Temperature Data from SoilSCAPE Sites, USA"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewBundle.jsp?identifier=urn%3Anasa%3Apds%3Aladee_nms&version=1.0",
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
-                "ladee"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This bundle contains the data collected by the Neutral Mass Spectrometer (NMS) instrument aboard the Lunar Atmosphere and Dust Environment Explorer (LADEE) satellite, along with the documents and other information necessary for the interpretation of that data.",
+            "identifier": "urn:nasa:pds:ladee_nms_wk2p-jh6t",
+            "issued": "2018-06-26",
+            "keyword": [
+                "moon",
+                "ladee"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewBundle.jsp?identifier=urn%3Anasa%3Apds%3Aladee_nms&version=1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:ladee_nms_wk2p-jh6t",
-            "description": "This bundle contains the data collected by the Neutral Mass Spectrometer (NMS) instrument aboard the Lunar Atmosphere and Dust Environment Explorer (LADEE) satellite, along with the documents and other information necessary for the interpretation of that data.",
-            "title": "LADEE Neutral Mass Spectrometer Data",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "LADEE Neutral Mass Spectrometer Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=CO-S-UVIS-2-CALIB-V1.1",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "Observations of solar or stellar targets for the purpose of calibrating detector wavelength scale, photometric sensitivity and flat fields.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.co-s-uvis-2-calib-v1.1_wk3j-usfp",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "hyperion",
                 "janus",
@@ -1580089,125 +1580091,101 @@
                 "iapetus",
                 "helene"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=CO-S-UVIS-2-CALIB-V1.1",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.co-s-uvis-2-calib-v1.1_wk3j-usfp",
-            "description": "Observations of solar or stellar targets for the purpose of calibrating detector wavelength scale, photometric sensitivity and flat fields.",
-            "title": "CASSINI ORBITER SATURN UVIS CALIBRATION DATA 1.1",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "CASSINI ORBITER SATURN UVIS CALIBRATION DATA 1.1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1386206552-NSIDCV0.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Active-Layer and Permafrost Temperatures, Sisimiut (Holsteinsborg), Greenland, Version 1. Version 1. Archived by National Aeronautics and Space Administration, U.S. Government, Greenlandic Geological Survey, GEUS.",
-            "issued": "1967-09-01",
-            "temporal": "1967-09-01T00:00:00Z/1982-08-31T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "1982-08-31",
-            "keyword": [
-                "cryosphere",
-                "frozen ground",
-                "soils",
-                "land surface",
-                "earth science"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Niels Foged",
                 "hasEmail": "mailto:nf@byg.dtu.dk"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NSIDC"
-            },
-            "identifier": "C1386206552-NSIDCV0",
             "description": "This data set contains active-layer and permafrost temperatures from Sisimiut, west Greenland, recorded from 18 sensors at depths of 0.25 m, 0.5 m, 0.75 m, 1 m, 1.25 m, 1.5 m, 1.75 m, 2 m, 2.5 m, 3 m, 3.5 m, 4 m, 4.5 m, 5 m, 6 m, 7 m, 8 m, and 9 m below the surface. Snow depth, snow extent, and surface air temperature were also recorded. Thermometers recorded temperatures once a day from September 1967 to August 1982; however, this data set only contains bi-weekly averages. Data are in tab-delimited ASCII text format and are available via FTP.",
-            "title": "Active-Layer and Permafrost Temperatures, Sisimiut (Holsteinsborg), Greenland, Version 1",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/forms/GGD23_or.html?major_version=1",
-                    "description": "Direct download, with optional registration page.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download, with optional registration page.",
+                    "downloadURL": "https://nsidc.org/forms/GGD23_or.html?major_version=1",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/data/GGD23/versions/1",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://nsidc.org/data/GGD23/versions/1",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/data/GGD23/versions/1",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://nsidc.org/data/GGD23/versions/1",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C1386206552-NSIDCV0",
+            "issued": "1967-09-01",
+            "keyword": [
+                "cryosphere",
+                "frozen ground",
+                "soils",
+                "land surface",
+                "earth science"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1386206552-NSIDCV0.html",
+            "language": [
+                "en-US"
+            ],
+            "modified": "1982-08-31",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NSIDC"
+            },
             "spatial": "-53.64 66.94 -53.64 66.94",
+            "temporal": "1967-09-01T00:00:00Z/1982-08-31T23:59:59.999Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Active-Layer and Permafrost Temperatures, Sisimiut (Holsteinsborg), Greenland, Version 1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://nasa3d.arc.nasa.gov/detail/ostm-jason-2",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2018-06-25",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
-            "references": [
-                "http://www.nasa.gov/mission_pages/ostm/main/index.html"
-            ],
-            "keyword": [
-                "spacecraft",
-                "eyes on the solar system",
-                "satellite",
-                "3d model",
-                "ostm/jason-2"
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
-            "identifier": "NASA-391",
             "description": "OSTM/Jason-2's primary payload includes five instruments similar to those aboard Jason-1, along with three experimental instruments. Its main instrument is an altimeter that precisely measures the distance from the satellite to the ocean surface. Its radiometer measures the amount of water vapor in the atmosphere, which can distort the altimeter measurements. Three location systems combine to measure the satellite's precise position in orbit.",
-            "title": "NASA 3D Models: OSTM/Jason-2",
-            "programCode": [
-                "026:007"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -1580215,96 +1580193,129 @@
                     "mediaType": "application/octet-stream"
                 }
             ],
-            "accrualPeriodicity": "irregular",
+            "identifier": "NASA-391",
+            "issued": "2018-06-25",
+            "keyword": [
+                "spacecraft",
+                "eyes on the solar system",
+                "satellite",
+                "3d model",
+                "ostm/jason-2"
+            ],
+            "landingPage": "http://nasa3d.arc.nasa.gov/detail/ostm-jason-2",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:007"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Aeronautics and Space Administration"
+            },
+            "references": [
+                "http://www.nasa.gov/mission_pages/ostm/main/index.html"
+            ],
             "theme": [
                 "Space Science"
-            ]
+            ],
+            "title": "NASA 3D Models: OSTM/Jason-2"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-A-OSINAC-3-AST2-LUTETIAFLYBY-V1.1",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This data set contains images acquired by the OSIRIS Narrow Angle Camera during the LUTETIA FLY-BY mission phase",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-a-osinac-3-ast2-lutetiaflyby-v1.1_wk7w-g5c3",
             "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "vega",
                 "16 cyg b",
                 "international rosetta mission",
                 "21 lutetia"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-A-OSINAC-3-AST2-LUTETIAFLYBY-V1.1",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-a-osinac-3-ast2-lutetiaflyby-v1.1_wk7w-g5c3",
-            "description": "This data set contains images acquired by the OSIRIS Narrow Angle Camera during the LUTETIA FLY-BY mission phase",
-            "title": "ROSETTA-ORBITER LUTETIA FLY-BY OSINAC 3 RDR V1.1",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "ROSETTA-ORBITER LUTETIA FLY-BY OSINAC 3 RDR V1.1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC2-0645-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 2 phase 2015-03-11 to 2015-06-30. It is a Global Gravity measurement at the comet 67P and covers the time 2015-03-14T23:48:05.000 to 2015-03-15T09:16:07.500.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc2-0645-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC2-0645-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc2-0645-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 2 phase 2015-03-11 to 2015-06-30. It is a Global Gravity measurement at the comet 67P and covers the time 2015-03-14T23:48:05.000 to 2015-03-15T09:16:07.500.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 2 0645 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 2 0645 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.nasa.gov/d/wk9u-ab4f",
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
+                    "downloadURL": "http://prime.jsc.nasa.gov/earthplus/data.htm",
+                    "mediaType": "text/html"
+                }
+            ],
+            "identifier": "NASA-0000033",
             "issued": "2018-06-25",
-            "temporal": "2004-01-01/2005-01-01",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
             "keyword": [
                 "education outreach",
                 "atmospheric science data center",
@@ -1580314,614 +1580325,576 @@
                 "hdf5",
                 "earth science"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Robert O. Shelton",
-                "hasEmail": "mailto:Robert.o.Shelton@nasa.gov"
-            },
+            "landingPage": "https://data.nasa.gov/d/wk9u-ab4f",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "NASA-0000033",
-            "description": "Earth+ makes NASA satellite photos and data accessible to blind students.",
-            "title": "Earth+",
-            "programCode": [
-                "026:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://prime.jsc.nasa.gov/earthplus/data.htm",
-                    "mediaType": "text/html"
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
-            "landingPage": "https://doi.org/10.5067/ASDC_DAAC/FIRE/0033",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2000-04-07. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/ASDC_DAAC/FIRE/0033.",
-            "issued": "2000-03-16",
-            "temporal": "1992-06-01T00:00:00Z/1992-06-29T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2018-07-06",
-            "keyword": [
-                "atmospheric winds",
-                "atmosphere",
-                "ocean winds",
-                "oceans",
-                "earth science"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "LAURENCE EYMARD",
                 "hasEmail": "mailto:laurence.eymard@cetp.ipsl.fr"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/LARC/SD/ASDC"
-            },
-            "identifier": "C1000000998-LARC_ASDC",
             "description": "The First ISCCP Regional Experiments have been designed to improve data products and cloud/radiation parameterizations used in general circulation models (GCMs). Specifically, the goals of FIRE are (1) to improve the basic understanding of the interaction of physical processes in determining life cycles of cirrus and marine stratocumulus systems and the radiative properties of these clouds during their life cycles and (2) to investigate the interrelationships between the ISCCP data, GCM parameterizations, and higher space and time resolution cloud data. To-date, four intensive field-observation periods were planned and executed: a cirrus IFO (October 13 - November 2, 1986); a marine stratocumulus IFO off the southwestern coast of California (June 29 - July 20, 1987); a second cirrus IFO in southeastern Kansas (November 13 - December 7, 1991); and a second marine stratocumulus IFO in the eastern North Atlantic Ocean (June 1 - June 28, 1992). Each mission combined coordinated satellite, airborne, and surface observations with modeling studies to investigate the cloud properties and physical processes of the cloud systems.The wind scatterometer aboard ERS-1 scans a 300km wide zone, situated 300km right of the satellite track. Orbital data are given for each orbit (number 1 to 501), starting from the orbit node (10:30 solar time for the descending orbit at the equator). The complete cycle duration is 35 days. Data from the ASTEX domain have been extracted for June, 1992 from the fast delivery product tapes provided by ESA. The raw data have been processed by ESA, using an algorithm (CMOD2) which has has revealed to fail in a number of cases. Itresults in particular in erroneous wind direction (180deg ambiguit\\ y). These data thus cannot be used without a careful examination of their coherence.",
-            "title": "First ISCCP Regional Experiment (FIRE) Atlantic Stratocumulus Transition Experiment (ASTEX) ERS-1 Wind Scatterometer Data",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC_DAAC%2FFIRE%2F0033",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC_DAAC%2FFIRE%2F0033",
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
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1000000998-LARC_ASDC",
-                    "description": "Earthdata Search for FIRE_AX_ERS1_SCTRMTR_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for FIRE_AX_ERS1_SCTRMTR_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1000000998-LARC_ASDC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/ASDC_DAAC/FIRE/0033",
-                    "description": "DOI data set landing page for FIRE_AX_ERS1_SCTRMTR_1",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for FIRE_AX_ERS1_SCTRMTR_1",
+                    "downloadURL": "https://doi.org/10.5067/ASDC_DAAC/FIRE/0033",
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
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/guide/base_fire_ax_ers1_dataset.pdf",
-                    "description": "FIRE ASTEX ERS-1 Langley DAAC Data Set Document",
                     "@type": "dcat:Distribution",
+                    "description": "FIRE ASTEX ERS-1 Langley DAAC Data Set Document",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/guide/base_fire_ax_ers1_dataset.pdf",
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
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/FIRE/FIRE_AX_ERS1_SCTRMTR/",
-                    "description": "ASDC Direct Data Download for FIRE_AX_ERS1_SCTRMTR_1",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for FIRE_AX_ERS1_SCTRMTR_1",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/FIRE/FIRE_AX_ERS1_SCTRMTR/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/FIRE/FIRE_AX_ERS1_SCTRMTR/contents.html",
-                    "description": "OPeNDAP data access for FIRE_AX_ERS1_SCTRMTR_1",
                     "@type": "dcat:Distribution",
+                    "description": "OPeNDAP data access for FIRE_AX_ERS1_SCTRMTR_1",
+                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/FIRE/FIRE_AX_ERS1_SCTRMTR/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 }
             ],
+            "identifier": "C1000000998-LARC_ASDC",
+            "issued": "2000-03-16",
+            "keyword": [
+                "atmospheric winds",
+                "atmosphere",
+                "ocean winds",
+                "oceans",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/ASDC_DAAC/FIRE/0033",
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
             "spatial": "<?xml version=\"1.0\" encoding=\"UTF-8\"?><gml:Polygon xmlns:gml=\"http://www.opengis.net/gml/3.2\" srsName=\"EPSG:4326\"><gml:outerBoundaryIs><gml:LinearRing><gml:posList>22.2 -34.83 22.2 -10.15 42.94 -10.15 42.94 -34.83 22.2 -34.83</gml:posList></gml:LinearRing></gml:outerBoundaryIs><gml:innerBoundaryIs></gml:innerBoundaryIs></gml:Polygon>",
+            "temporal": "1992-06-01T00:00:00Z/1992-06-29T23:59:59.999Z",
             "theme": [
                 "FIRE",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "First ISCCP Regional Experiment (FIRE) Atlantic Stratocumulus Transition Experiment (ASTEX) ERS-1 Wind Scatterometer Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MEX-M-MARSIS-3-RDR-SS-EXT3-V1.0",
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
+            "description": "This dataset contains subsurface sounding data from the MARS EXPRESS MARS MARSIS EXPERIMENT DATA RECORD V2.0 Data Set that have been uncompressed, corrected for Automated Gain Control, aligned to a reference altitude and, except for data acquired using the SS2 mode, range processed after correcting for the distortion of the transmitted signal caused by the ionosphere.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mex-m-marsis-3-rdr-ss-ext3-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "mars",
+                "mars express"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MEX-M-MARSIS-3-RDR-SS-EXT3-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mex-m-marsis-3-rdr-ss-ext3-v1.0",
-            "description": "This dataset contains subsurface sounding data from the MARS EXPRESS MARS MARSIS EXPERIMENT DATA RECORD V2.0 Data Set that have been uncompressed, corrected for Automated Gain Control, aligned to a reference altitude and, except for data acquired using the SS2 mode, range processed after correcting for the distortion of the transmitted signal caused by the ionosphere.",
-            "title": "MARS EXPRESS MARSIS REDUCED DATA SUBSURFACE EXT 3 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "MARS EXPRESS MARSIS REDUCED DATA SUBSURFACE EXT 3 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ASDC/SUBORBITAL/SOLVE2_Sondes_Data_1",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/ASDC/SUBORBITAL/SOLVE2_Sondes_Data_1.",
-            "issued": "2022-09-12",
-            "temporal": "2002-12-03T00:00:00Z/2004-01-11T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-12-13",
-            "keyword": [
-                "clouds",
-                "earth science",
-                "aerosols",
-                "atmospheric chemistry",
-                "atmospheric pressure",
-                "atmospheric water vapor",
-                "atmospheric temperature",
-                "atmosphere"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Geoffrey Toon",
                 "hasEmail": "mailto:geoffrey.c.toon@jpl.caltech.edu"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/LARC/SD/ASDC"
-            },
-            "identifier": "C2569836986-LARC_ASDC",
             "description": "SOLVE2_Sondes_Data is the balloonsonde and ozonesonde data collected during the SAGE III Ozone Loss and Validation Experiment II (SOLVE II). Data were collected by frost-point hygrometer, ozonesondes, condensation nuclei counters, Optical Particle Counters (OPC), and the JPL MkIV Balloon Interferometer (MkIV). Data collection for this product is complete. \r\n\r\nThe SOLVE campaign was a NASA multi-program effort of the Upper Atmosphere Research Program (UARP), Atmospheric Effects of Aviation Project (AEAP), Atmospheric Chemistry Modeling and Analysis Program (ACMAP) and Earth Observing System (EOS) of NASA\u2019s Earth Science Enterprise (ESE). SOLVE\u2019s primary objective was for calibrating and validating the Stratospheric Aerosol and Gas Experiment (SAGE) III satellite measurements, while examining the processes that controlled ozone levels at a mid- to high-latitude range. The major goal of SAGE III was to quantitatively assess ozone loss at high latitudes. SOLVE was a two-phase experiment, the first phase, SOLVE, occurred during the fall of 1999 through the spring of 2000. The second phase, SOLVE II, occurred during the winter of 2003.\r\n\r\nSOLVE took place in the Arctic high-latitude region during the winter. The polar ozone depletion processes cause by human-produced chlorine and bromine are most active in mid-to-late winter and early spring in the high Arctic. In order to conduct this validation experiment, NASA deployed the NASA ER-2 aircraft and NASA DC-8 aircraft. The ER-2 measured a variety of atmospheric data, including ozone (O3), H2O, CO2, ClONO2, HCl, ClO/BrO, and Cl2O2. The DC-8 aircraft measured ozone, ClO/BrO, and aerosol, among other atmospheric data. SOLVE also utilized balloon platforms, ground-based instruments, and collaborations with the German Aerospace Center\u2019s (DLR) FALCON aircraft equipped with the OLEX Lidar to achieve the mission objectives. Overall, the campaign had 28 flights, with SOLVE featuring 17 total flights among the different aircrafts and SOLVE II featuring 11 flights.",
-            "title": "SOLVE II Balloonsondes and Ozonesondes Data",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC%2FSUBORBITAL%2FSOLVE2_Sondes_Data_1",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC%2FSUBORBITAL%2FSOLVE2_Sondes_Data_1",
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
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/SOLVE_II/Sondes_Data_1/",
-                    "description": "ASDC Direct Data Download for SOLVE2_Sondes_Data_1",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for SOLVE2_Sondes_Data_1",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/SOLVE_II/Sondes_Data_1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 }
             ],
+            "identifier": "C2569836986-LARC_ASDC",
+            "issued": "2022-09-12",
+            "keyword": [
+                "clouds",
+                "earth science",
+                "aerosols",
+                "atmospheric chemistry",
+                "atmospheric pressure",
+                "atmospheric water vapor",
+                "atmospheric temperature",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.5067/ASDC/SUBORBITAL/SOLVE2_Sondes_Data_1",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2022-12-13",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/LARC/SD/ASDC"
+            },
             "spatial": "<?xml version=\"1.0\" encoding=\"UTF-8\"?><gml:Polygon xmlns:gml=\"http://www.opengis.net/gml/3.2\" srsName=\"EPSG:9825\"><gml:outerBoundaryIs><gml:LinearRing><gml:posList>-45.1 -105.7 -45.1 170.5 69.3 170.5 69.3 -105.7 -45.1 -105.7</gml:posList></gml:LinearRing></gml:outerBoundaryIs><gml:innerBoundaryIs></gml:innerBoundaryIs></gml:Polygon>",
+            "temporal": "2002-12-03T00:00:00Z/2004-01-11T23:59:59.999Z",
             "theme": [
                 "SOLVE",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "SOLVE II Balloonsondes and Ozonesondes Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://c3.nasa.gov/dashlink/resources/294/",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2011-01-28",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
-            "keyword": [
-                "dashlink",
-                "nasa",
-                "ames"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Nikunj Oza",
                 "hasEmail": "mailto:Nikunj.C.Oza@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Dashlink"
-            },
-            "identifier": "DASHLINK_294",
             "description": "This data set is a simulated data set based on the flight simulator \"FLTz\" used by the Intelligent Flight Control (IFC) group at NASA ARC. Flights were preprogrammed to fly through randomly generated circular flight paths starting from San Francisco International Airport (SFO) and ending at approximately the same location. No known anomalous flights were simulated.",
-            "title": "FLTz",
-            "programCode": [
-                "026:029"
-            ],
             "distribution": [
                 {
-                    "mediaType": "application/zip",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/FLTz_2.zip",
-                    "description": "FLTz.zip",
                     "@type": "dcat:Distribution",
+                    "description": "FLTz.zip",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/FLTz_2.zip",
+                    "mediaType": "application/zip",
                     "title": "FLTz.zip"
                 },
                 {
-                    "mediaType": "application/zip",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/matfiles.zip",
-                    "description": "Large FLTz dataset",
                     "@type": "dcat:Distribution",
+                    "description": "Large FLTz dataset",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/matfiles.zip",
+                    "mediaType": "application/zip",
                     "title": "matfiles.zip"
                 },
                 {
-                    "mediaType": "application/x-pdf",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/table_report.pdf",
-                    "description": "Meta-data for Large FLTz dataset",
                     "@type": "dcat:Distribution",
+                    "description": "Meta-data for Large FLTz dataset",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/table_report.pdf",
+                    "mediaType": "application/x-pdf",
                     "title": "table_report.pdf"
                 }
             ],
-            "accrualPeriodicity": "irregular"
+            "identifier": "DASHLINK_294",
+            "issued": "2011-01-28",
+            "keyword": [
+                "dashlink",
+                "nasa",
+                "ames"
+            ],
+            "landingPage": "https://c3.nasa.gov/dashlink/resources/294/",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:029"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Dashlink"
+            },
+            "title": "FLTz"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.nasa.gov/d/wkm8-fkaj",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "keyword": [
-                "strain",
-                "sequence assembly",
-                "nucleic acid extraction",
-                "sample collection",
-                "nucleic acid sequencing",
-                "library construction"
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
-            "identifier": "nasa_genelab_GLDS-291_wkm8-fkaj",
             "description": "Rubinsicoccus jplei genome a novel genus isolated from JPL spacecraft environment where Mars 2020 subsystems are assembled.",
-            "title": "Kineosporiaceae bacterium B12 whole genome shotgun sequencing project",
-            "programCode": [
-                "026:005"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-291",
-                    "description": "GeneLab Study Page",
                     "@type": "dcat:Distribution",
+                    "description": "GeneLab Study Page",
+                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-291",
+                    "mediaType": "text/html",
                     "title": "Kineosporiaceae bacterium B12 whole genome shotgun sequencing project"
                 }
             ],
+            "identifier": "nasa_genelab_GLDS-291_wkm8-fkaj",
+            "issued": "2021-05-21",
+            "keyword": [
+                "strain",
+                "sequence assembly",
+                "nucleic acid extraction",
+                "sample collection",
+                "nucleic acid sequencing",
+                "library construction"
+            ],
+            "landingPage": "https://data.nasa.gov/d/wkm8-fkaj",
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
+            "title": "Kineosporiaceae bacterium B12 whole genome shotgun sequencing project"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/I9AJNY3T70UC",
             "citation": "Chris Barnet. 2019-01-15. SNDRAQIML3SMCCP. Version 2. Sounder SIPS: AQUA AIRS IR + MW Level 3 CLIMCAPS: Specific Quality Control Gridded Monthly V2. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/I9AJNY3T70UC. https://disc.gsfc.nasa.gov/datacollection/SNDRAQIML3SMCCP_2.html. Digital Science Data.",
-            "issued": "2002-09-01",
-            "temporal": "2002-08-31T00:00:00Z/2023-02-28T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2016-10-01",
-            "references": [
-                "https://doi.org/10.3390/rs11101227",
-                "https://doi.org/10.1109/TGRS.2012.2220369",
-                "https://doi.org/Sounder%20SIPS%3A%20Suomi%20NPP%20CrIMSS%20Level%203%20Comprehensive%20Quality%20Control%20Gridded%20Daily%20CLIMCAPS%20Normal%20Spectral%20Resolution%20V1",
-                "https://doi.org/10.1109/TGRS.2002.808236",
-                "https://doi.org/10.1029/2005/JD007020",
-                "https://doi.org/10.5194/amt-13-4437-2020"
-            ],
-            "keyword": [
-                "clouds",
-                "air quality",
-                "surface thermal properties",
-                "surface radiative properties",
-                "precipitation",
-                "ocean temperature",
-                "oceans",
-                "land surface",
-                "earth science",
-                "atmospheric water vapor",
-                "atmospheric temperature",
-                "atmospheric radiation",
-                "atmospheric pressure",
-                "atmospheric chemistry",
-                "atmosphere",
-                "altitude"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Lena Iredell",
                 "hasEmail": "mailto:lena.iredell@nasa.gov"
             },
+            "creator": "Chris Barnet",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C1693440838-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Not provided"
-            },
             "description": "WARNING: To users of the derived product \u201cco_mmr_midtrop\u201d (carbon monoxide mass mixing ratio to dry air [kg/kg] at ~500 hPa). This variable has a significant bias due to a conversion error: the molecular weight of carbon dioxide (CO2, 44.01 g/mol) was used instead of carbon monoxide (CO, 28.01 g/mol). To correct, simply multiply \u201cco_mmr_midtrop\u201d by 28.01/44.01. Alternatively, derive a profile of mass mixing ratio from scratch using the retrieved column density values (\u201cmol_lay/co_mol_lay\u201d) in the Level 2 files. For further questions or concerns please contact the Sounder SIPS at: sounder.sips@jpl.nasa.gov\n\nThe CLIMCAPS (Community Long-term Infrared Microwave Coupled Product System) algorithm is used to analyze data from the AIRS (Atmospheric Infrared Sounder) and AMSU (Advanced Microwave Sounding Unit). The AIRS instrument is a grating spectrometer (R = 1200) aboard the second Earth Observing System (EOS) polar-orbiting platform, EOS Aqua. The AIRS in combination with the AMSU constitutes an innovative atmospheric sounding group of infrared and microwave sensors. The AIRS Standard Retrieval Product consists of retrieved estimates of cloud and surface properties, plus profiles of retrieved temperature, water vapor, ozone, carbon monoxide and methane. The temperature profile vertical resolution is 100 levels total between 1100 mb and 0.1 mb, while moisture profile is reported at atmospheric layers between 1100 mb and 300 mb. The horizontal resolution is 50 km.\n \nThe CLIMCAPS algorithm uses an Optimal Estimation methodology and uses an a-priori first guess to start the process. A CLIMCAPS sounding is comprised of a set of parameters that characterizes the full atmospheric state and includes a variety of geophysical parameters derived from the CrIMSS data. These include surface temperature and infrared emissivity; full atmosphere profiles of temperature, water vapor and ozone; infrared effective cloud top characteristics; carbon monoxide, methane, carbon dioxide, sulfur dioxide, nitrous oxide, and nitric acid.\n \nThis monthly one degree latitude by one degree longitude level-3 product starts with level-2 retrieval products applying the specific quality control (QC) methodology. Specific QC accepts profile level from the top of the atmosphere down to the level where the QC determines that it is still good. Below this level, the data is rejected.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "SNDRAQIML3SMCCP",
-            "creator": "Chris Barnet",
-            "graphic-preview-description": "Sample plot of AIRS/AMSU Level 3 Retrieval.",
-            "title": "Sounder SIPS: AQUA AIRS IR + MW Level 3 CLIMCAPS: Specific Quality Control Gridded Monthly V2 at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/SNDRAQIML3SMCCP_2.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FI9AJNY3T70UC",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FI9AJNY3T70UC",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/SNDRAQIML3SMCCP_2.png",
-                    "description": "Sample plot of AIRS/AMSU Level 3 Retrieval.",
                     "@type": "dcat:Distribution",
+                    "description": "Sample plot of AIRS/AMSU Level 3 Retrieval.",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/SNDRAQIML3SMCCP_2.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sounder.gesdisc.eosdis.nasa.gov/data/Aqua_Sounder_Level3/SNDRAQIML3SMCCP.2",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://sounder.gesdisc.eosdis.nasa.gov/data/Aqua_Sounder_Level3/SNDRAQIML3SMCCP.2",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sounder.gesdisc.eosdis.nasa.gov/opendap/Aqua_Sounder_Level3/SNDRAQIML3SMCCP.2/",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://sounder.gesdisc.eosdis.nasa.gov/opendap/Aqua_Sounder_Level3/SNDRAQIML3SMCCP.2/",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=SSNDRAQIML3SMCCP+2",
-                    "description": "Search the Earthdata website",
                     "@type": "dcat:Distribution",
+                    "description": "Search the Earthdata website",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=SSNDRAQIML3SMCCP+2",
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
                 }
             ],
+            "graphic-preview-description": "Sample plot of AIRS/AMSU Level 3 Retrieval.",
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/SNDRAQIML3SMCCP_2.png",
+            "identifier": "C1693440838-GES_DISC",
+            "issued": "2002-09-01",
+            "keyword": [
+                "clouds",
+                "air quality",
+                "surface thermal properties",
+                "surface radiative properties",
+                "precipitation",
+                "ocean temperature",
+                "oceans",
+                "land surface",
+                "earth science",
+                "atmospheric water vapor",
+                "atmospheric temperature",
+                "atmospheric radiation",
+                "atmospheric pressure",
+                "atmospheric chemistry",
+                "atmosphere",
+                "altitude"
+            ],
+            "landingPage": "https://doi.org/10.5067/I9AJNY3T70UC",
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
+                "https://doi.org/Sounder%20SIPS%3A%20Suomi%20NPP%20CrIMSS%20Level%203%20Comprehensive%20Quality%20Control%20Gridded%20Daily%20CLIMCAPS%20Normal%20Spectral%20Resolution%20V1",
+                "https://doi.org/10.1109/TGRS.2002.808236",
+                "https://doi.org/10.1029/2005/JD007020",
+                "https://doi.org/10.5194/amt-13-4437-2020"
+            ],
+            "release-place": "Greenbelt, MD, USA",
+            "series-name": "SNDRAQIML3SMCCP",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2002-08-31T00:00:00Z/2023-02-28T00:00:00Z",
             "theme": [
                 "Aqua",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Sounder SIPS: AQUA AIRS IR + MW Level 3 CLIMCAPS: Specific Quality Control Gridded Monthly V2 at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/MEASURES/OZONE/DATA207",
             "citation": "P.K. Bhartia, et al.. 2012-09-06. SBUV2N17L2. Version 1. SBUV2/NOAA-17 Ozone (O3) Nadir Profile and Total Column 1 Day L2 V1. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/MEASURES/OZONE/DATA207. https://disc.gsfc.nasa.gov/datacollection/SBUV2N17L2_1.html. Digital Science Data.",
-            "issued": "2013-08-28",
-            "temporal": "2002-07-11T00:00:00Z/2013-04-10T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2013-08-28",
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
-            "identifier": "C1251051640-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "The Solar Backscattered Ultraviolet (SBUV) from NOAA-17 Level-2 daily product (SBUV2N17L2) contains ozone nadir profile and total column data from retrievals generated from the v8.6 SBUV algorithm. The v8.6 SBUV algorithm estimates the ozone nadir profile and total column from SBUV measurements using 1) the Brion-Daumont-Malicet ozone cross sections, 2) an OMI-derived cloud-height climatology, 3) a revised a priori ozone climatology, and 4) inter-instrument calibration based on comparisons with no local time difference.\n\nThe SBUV2N17L2 product is written as daily files using the HDF5 format, with file sizes ranging from about 1 to 5 Mbytes. Data are available from July 2002 through April 2013. The SBUV2N17L2 data product was used as input in creating the SBUV2N17L3zm monthly zonal mean data product.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "SBUV2N17L2",
-            "creator": "P.K. Bhartia, et al.",
-            "title": "SBUV2/NOAA-17 Ozone (O3) Nadir Profile and Total Column 1 Day L2 V1 (SBUV2N17L2) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/SBUV2N17L2_1.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMEASURES%2FOZONE%2FDATA207",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMEASURES%2FOZONE%2FDATA207",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
@@ -1580931,169 +1580904,210 @@
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/SBUV2N17L2_1.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/SBUV2N17L2_1.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://measures.gesdisc.eosdis.nasa.gov/data/Ozone/SBUV2N17L2.1/",
-                    "description": "Access the data via HTTP.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTP.",
+                    "downloadURL": "https://measures.gesdisc.eosdis.nasa.gov/data/Ozone/SBUV2N17L2.1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://measures.gesdisc.eosdis.nasa.gov/opendap/Ozone/SBUV2N17L2.1/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://measures.gesdisc.eosdis.nasa.gov/opendap/Ozone/SBUV2N17L2.1/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://measures.gesdisc.eosdis.nasa.gov/opendap/Ozone/SBUV2N17L2.1/catalog.xml",
-                    "description": "Access the data using the THREDDS Catalog.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data using the THREDDS Catalog.",
+                    "downloadURL": "https://measures.gesdisc.eosdis.nasa.gov/opendap/Ozone/SBUV2N17L2.1/catalog.xml",
+                    "mediaType": "text/html",
                     "title": "Use THREDDS DATA to download the dataset's data"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://measures.gesdisc.eosdis.nasa.gov/data/Ozone/SBUV2N17L2.1/doc/README.SBUVL2.pdf",
-                    "description": "README Document",
                     "@type": "dcat:Distribution",
+                    "description": "README Document",
+                    "downloadURL": "https://measures.gesdisc.eosdis.nasa.gov/data/Ozone/SBUV2N17L2.1/doc/README.SBUVL2.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's read me document"
                 }
             ],
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/SBUV2N17L2_1.png",
+            "identifier": "C1251051640-GES_DISC",
+            "issued": "2013-08-28",
+            "keyword": [
+                "atmosphere",
+                "atmospheric chemistry",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/MEASURES/OZONE/DATA207",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2013-08-28",
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
+            "series-name": "SBUV2N17L2",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2002-07-11T00:00:00Z/2013-04-10T23:59:59.999Z",
             "theme": [
                 "MEaSUREs",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "SBUV2/NOAA-17 Ozone (O3) Nadir Profile and Total Column 1 Day L2 V1 (SBUV2N17L2) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=DAWN-M-GRAND-3-RDR-MARS-COUNTS-V1.0",
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
-                "dawn mission to vesta and ceres"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "The GRaND RDR are a time-ordered collection of\ncorrected gamma ray and neutron counting data and calibrated pulse\nheight spectra acquired by GRaND during all phases of the Dawn mission.\nThis data set is specific to Mars Gravity Assist (MGA), and includes\ndata acquired during Mars approach and flyby.  The RDR is a calibrated\ndata set derived from the Experiment Data Records (EDR), consisting of\ntime-series counting rates from which elemental abundances can be\ndetermined.  Ancillary ephemeris and pointing data needed for analysis\nand mapping of the time series data are included in the data set.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.dawn-m-grand-3-rdr-mars-counts-v1.0_wku7-kmsk",
+            "issued": "2021-05-21",
+            "keyword": [
+                "dawn mission to vesta and ceres"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=DAWN-M-GRAND-3-RDR-MARS-COUNTS-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.dawn-m-grand-3-rdr-mars-counts-v1.0_wku7-kmsk",
-            "description": "The GRaND RDR are a time-ordered collection of\ncorrected gamma ray and neutron counting data and calibrated pulse\nheight spectra acquired by GRaND during all phases of the Dawn mission.\nThis data set is specific to Mars Gravity Assist (MGA), and includes\ndata acquired during Mars approach and flyby.  The RDR is a calibrated\ndata set derived from the Experiment Data Records (EDR), consisting of\ntime-series counting rates from which elemental abundances can be\ndetermined.  Ancillary ephemeris and pointing data needed for analysis\nand mapping of the time series data are included in the data set.",
-            "title": "DAWN GRAND CALIBRATED MARS FLYBY COUNTS\n                                      V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "DAWN GRAND CALIBRATED MARS FLYBY COUNTS\n                                      V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-PRL-0426-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the PRELANDING phase 2014-01-21 to 2014-11-18. It is a Global Gravity measurement at the comet 67P and covers the time 2014-11-12T14:07:05.000 to 2014-11-13T02:42:38.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-prl-0426-v1.0_wkub-x8re",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-PRL-0426-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-prl-0426-v1.0_wkub-x8re",
-            "description": "This is a Rosetta Radio Science data set, collected during the PRELANDING phase 2014-01-21 to 2014-11-18. It is a Global Gravity measurement at the comet 67P and covers the time 2014-11-12T14:07:05.000 to 2014-11-13T02:42:38.000.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     PRELANDING 0426 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     PRELANDING 0426 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-4-ESC1-67P-M11-REFLECT-V1.0",
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
+            "description": "This CODMAC level 4 data set contains radiometric calibrated and geometric distortion corrected (resampled) image data in reflectance units (normalized and thus without unit), acquired by the OSIRIS Narrow Angle Camera on the Rosetta spacecraft during the COMET ESCORT 1 mission phase, covering the period from 2014-12-19T23:25:00.000 to 2015-01-13T23:24:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V1.0 is the first version of this dataset: Lien corrected dataset after October 2018 PSA/PDS external peer review.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-4-esc1-67p-m11-reflect-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-4-ESC1-67P-M11-REFLECT-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-4-esc1-67p-m11-reflect-v1.0",
-            "description": "This CODMAC level 4 data set contains radiometric calibrated and geometric distortion corrected (resampled) image data in reflectance units (normalized and thus without unit), acquired by the OSIRIS Narrow Angle Camera on the Rosetta spacecraft during the COMET ESCORT 1 mission phase, covering the period from 2014-12-19T23:25:00.000 to 2015-01-13T23:24:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V1.0 is the first version of this dataset: Lien corrected dataset after October 2018 PSA/PDS external peer review.",
-            "title": "ROSETTA-ORBITER 67P OSINAC 4 ESC1-MTP011 RDR-REFLECT V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P OSINAC 4 ESC1-MTP011 RDR-REFLECT V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.nasa.gov/d/wkwg-a6gy",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "GeneLab Outreach",
+                "hasEmail": "mailto:genelab-outreach@lists.nasa.gov"
+            },
+            "description": "Controlled hypobaria presents biology with an environment that is never encountered in terrestrial ecology yet the apparent components of hypobaria are stresses typical of terrestrial ecosystems. High altitude for example presents terrestrial hypobaria always with hypoxia as a component stress since the relative partial pressure of O2 is constant in the atmosphere. Laboratory-controlled hypobaria however allows the dissection of pressure effects away from the effects typically associated with altitude in particular hypoxia as the partial pressure of O2 can be varied. In this study whole transcriptomes of plants grown in ambient (97 kPa/pO2 = 21 kPa) atmospheric conditions were compared to those of plants transferred to five different atmospheres of varying pressure and oxygen composition for 24 h: 50 kPa/pO2 = 10 kPa 25 kPa/pO2 = 5 kPa 50 kPa/pO2 = 21 kPa 25 kPa/pO2 = 21 kPa or 97 kPa/pO2 = 5 kPa. The plants exposed to these environments were 10 day old Arabidopsis seedlings grown vertically on hydrated nutrient plates. In addition 5 day old plants were also exposed for 24 h to the 50 kPa and ambient environments to evaluate age-dependent responses. The gene expression profiles from roots and shoots showed that the hypobaric response contained more complex gene regulation than simple hypoxia and that adding back oxygen to normoxic conditions did not completely alleviate gene expression changes in hypobaric responses.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "GeneLab Study Page",
+                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-134",
+                    "mediaType": "text/html",
+                    "title": "Dissecting Low Atmospheric Pressure Stress: Transcriptome Responses to the Components of Hypobaria in Arabidopsis [Experiment 1]"
+                }
+            ],
+            "identifier": "nasa_genelab_GLDS-134_wkwg-a6gy",
             "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
             "keyword": [
                 "mesh:atmospheric pressure",
                 "treatment",
@@ -1581105,1422 +1581119,1410 @@
                 "normalization data transformation",
                 "labeling"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "GeneLab Outreach",
-                "hasEmail": "mailto:genelab-outreach@lists.nasa.gov"
-            },
+            "landingPage": "https://data.nasa.gov/d/wkwg-a6gy",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "nasa_genelab_GLDS-134_wkwg-a6gy",
-            "description": "Controlled hypobaria presents biology with an environment that is never encountered in terrestrial ecology yet the apparent components of hypobaria are stresses typical of terrestrial ecosystems. High altitude for example presents terrestrial hypobaria always with hypoxia as a component stress since the relative partial pressure of O2 is constant in the atmosphere. Laboratory-controlled hypobaria however allows the dissection of pressure effects away from the effects typically associated with altitude in particular hypoxia as the partial pressure of O2 can be varied. In this study whole transcriptomes of plants grown in ambient (97 kPa/pO2 = 21 kPa) atmospheric conditions were compared to those of plants transferred to five different atmospheres of varying pressure and oxygen composition for 24 h: 50 kPa/pO2 = 10 kPa 25 kPa/pO2 = 5 kPa 50 kPa/pO2 = 21 kPa 25 kPa/pO2 = 21 kPa or 97 kPa/pO2 = 5 kPa. The plants exposed to these environments were 10 day old Arabidopsis seedlings grown vertically on hydrated nutrient plates. In addition 5 day old plants were also exposed for 24 h to the 50 kPa and ambient environments to evaluate age-dependent responses. The gene expression profiles from roots and shoots showed that the hypobaric response contained more complex gene regulation than simple hypoxia and that adding back oxygen to normoxic conditions did not completely alleviate gene expression changes in hypobaric responses.",
-            "title": "Dissecting Low Atmospheric Pressure Stress: Transcriptome Responses to the Components of Hypobaria in Arabidopsis [Experiment 1]",
-            "programCode": [
-                "026:005"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-134",
-                    "description": "GeneLab Study Page",
-                    "@type": "dcat:Distribution",
-                    "title": "Dissecting Low Atmospheric Pressure Stress: Transcriptome Responses to the Components of Hypobaria in Arabidopsis [Experiment 1]"
-                }
-            ],
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "Dissecting Low Atmospheric Pressure Stress: Transcriptome Responses to the Components of Hypobaria in Arabidopsis [Experiment 1]"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/981",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Armstrong, R.L., K. Knowles, F.G. Hall, G.J. Collatz, B.W. Meeson, S.O. Los, E.Brown De Colstoun, and D.R. Landis. 2010. ISLSCP II Global Sea Ice Concentration. ORNL DAAC, Oak Ridge, Tennessee, USA. https://doi.org/10.3334/ORNLDAAC/981",
-            "issued": "2023-10-15",
-            "temporal": "1986-01-01T00:00:00Z/1995-12-31T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-10-17",
-            "keyword": [
-                "oceans",
-                "climate indicators",
-                "earth science",
-                "sea ice",
-                "cryospheric indicators",
-                "cryosphere"
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
-            "identifier": "C2784896705-ORNL_CLOUD",
             "description": "This International Satellite Land Surface Climatology Project (ISLSCP) Initiative II data set, ISLSCP II Global Sea Ice Concentration, is based on the Goddard Space Flight Center (GSFC) Sea Ice Concentrations from Nimbus-7 Scanning Multichannel Microwave Radiometer (SMMR) and the Defense Meteorological Satellites Program (DMSP) Special Sensor Microwave/Imager (SSM/I) Passive Microwave Data. This data set contains four zip files which includes sea ice concentration (in percentage of ocean area covered by sea ice), table data and map data.  These original data were re-gridded by the National Snow and Ice Data Center (NSIDC) from their original 25-km spatial resolution and EASE-Grid into equal angle Earth grids with quarter, half and one degree spatial resolutions in latitude/longitude. The ISLSCP II staff have taken the one degree resolution original data provided by the Principal Investigator and created global maps of monthly sea ice concentration on a global one degree grid using the latitude and longitude coordinates that were provided. Individual monthly files were created and written to the ASCII format. The re-gridded one degree original data were also adjusted to match the one degree ISLSCP II land/water mask.",
-            "graphic-preview-description": "Browse Image",
-            "title": "ISLSCP II Global Sea Ice Concentration",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/sdat-tds/981_1_fit.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F981",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F981",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/islscp_ii/snow_sea-ice_oceans/sea_ice_extent_xdeg/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/islscp_ii/snow_sea-ice_oceans/sea_ice_extent_xdeg/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/ISLSCP_II/guides/sea_ice_extent_xdeg.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/ISLSCP_II/guides/sea_ice_extent_xdeg.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/981",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/981",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/islscp_ii/snow_sea-ice_oceans/sea_ice_extent_xdeg/comp/0_sea_ice_extent_readme.txt",
-                    "description": "Data set text file containing the file naming convention and data formats of the granules in this collection.",
                     "@type": "dcat:Distribution",
+                    "description": "Data set text file containing the file naming convention and data formats of the granules in this collection.",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/islscp_ii/snow_sea-ice_oceans/sea_ice_extent_xdeg/comp/0_sea_ice_extent_readme.txt",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/islscp_ii/snow_sea-ice_oceans/sea_ice_extent_xdeg/comp/1_sea_ice_extent_doc.pdf",
-                    "description": "Data set documentation PDF.",
                     "@type": "dcat:Distribution",
+                    "description": "Data set documentation PDF.",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/islscp_ii/snow_sea-ice_oceans/sea_ice_extent_xdeg/comp/1_sea_ice_extent_doc.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://daac.ornl.gov/graphics/browse/sdat-tds/981_1_fit.png",
-                    "description": "Browse Image",
                     "@type": "dcat:Distribution",
+                    "description": "Browse Image",
+                    "downloadURL": "https://daac.ornl.gov/graphics/browse/sdat-tds/981_1_fit.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://webmap.ornl.gov/wcsdown/dataset.jsp?ds_id=981",
-                    "description": "Web Coverage Service for this collection.",
                     "@type": "dcat:Distribution",
+                    "description": "Web Coverage Service for this collection.",
+                    "downloadURL": "https://webmap.ornl.gov/wcsdown/dataset.jsp?ds_id=981",
+                    "mediaType": "text/html",
                     "title": "Use Web Coverage Service (WCS) to download the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://thredds.daac.ornl.gov/thredds/catalog/ornldaac/981/catalog.html",
-                    "description": "The THREDDS location for this Collection.",
                     "@type": "dcat:Distribution",
+                    "description": "The THREDDS location for this Collection.",
+                    "downloadURL": "https://thredds.daac.ornl.gov/thredds/catalog/ornldaac/981/catalog.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "graphic-preview-description": "Browse Image",
+            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/sdat-tds/981_1_fit.png",
+            "identifier": "C2784896705-ORNL_CLOUD",
+            "issued": "2023-10-15",
+            "keyword": [
+                "oceans",
+                "climate indicators",
+                "earth science",
+                "sea ice",
+                "cryospheric indicators",
+                "cryosphere"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/981",
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
+            "temporal": "1986-01-01T00:00:00Z/1995-12-31T23:59:59Z",
             "theme": [
                 "ISLSCP II",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "ISLSCP II Global Sea Ice Concentration"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1422",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Zhang, K., A.A. Ali, A. Antonarakis, and P.R. Moorcroft. 2016. AirMOSS: L4 Daily Modeled Net Ecosystem Exchange (NEE), AirMOSS sites, 2012-2014. ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/1422",
-            "issued": "2016-11-22",
-            "temporal": "2012-01-01T00:00:00Z/2014-10-30T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-17",
-            "keyword": [
-                "land surface",
-                "soils",
-                "biosphere",
-                "ecosystems",
-                "ecological dynamics",
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
-            "identifier": "C2262413649-ORNL_CLOUD",
             "description": "This data set provides Level 4 daily estimates of Net Ecosystem Exchange (NEE) of CO2 at a spatial resolution of 30 arc-seconds (~1 km) for seven of the sites covered by the Airborne Microwave Observatory of Subcanopy and Subsurface (AirMOSS) flights, each site spanning ~2500 km2. The daily NEE estimates are generally available from October 2012 through October 2014, although the exact time ranges vary by site. The AirMOSS L4 daily NEE were produced by the Ecosystem Demography Biosphere Model (ED2) augmented by the AirMOSS-derived L2/3 root zone soil moisture data as an additional input. The AirMOSS soil moisture data were used to estimate the sensitivity of carbon fluxes to soil moisture and to diagnose and improve estimation and prediction of NEE by constraining the model's predictions of soil moisture and its impact on above- and below-ground fluxes.",
-            "graphic-preview-description": "Browse Image",
-            "title": "AirMOSS: L4 Daily Modeled Net Ecosystem Exchange (NEE), AirMOSS sites, 2012-2014",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/sdat-tds/1422_1_fit.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1422",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1422",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/airmoss/campaign/AirMOSS_L4_Daily_NEE/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/airmoss/campaign/AirMOSS_L4_Daily_NEE/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/AIRMOSS/guides/AirMOSS_L4_Daily_NEE.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/AIRMOSS/guides/AirMOSS_L4_Daily_NEE.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1422",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1422",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
```

