# Change History for nasa.json (Part 87)

### Changes from 31606f9 to dd2190f (Part 76/162)
**Author:** Automated

**Date:** 2025-02-01 15:02:16+00:00

**Message:** Updated data: Sat Feb  1 15:02:16 UTC 2025

```diff
-            "description": "This CODMAC level 3 data set contains radiometric calibrated image data in W/m^2/sr/nm, acquired by the OSIRIS Narrow Angle Camera on the Rosetta spacecraft during the COMET ESCORT 3 mission phase, covering the period from 2015-09-22T23:25:00.000 to 2015-10-20T23:24:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V3.0 supersedes previous deliveries of the same dataset with the following changes since the last version: Lien corrected dataset after the July and October 2018 PSA/PDS external peer reviews. Updated documentation and ancillary files, added document on bandpass filter. Updated SCIENCE_USER_GUIDE_V03.PDF to include one section about FAQ and one section about image data quality. Added shutter backtravel and readout issues to image quality map. Updated DATA_QUALITY_ID keyword in image header. Improved handling of images with missing packets. Included FITs files. Browse products changed to the same size as the original image.",
-            "title": "ROSETTA-ORBITER 67P OSINAC 3 ESC3-MTP021 RDR V3.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P OSINAC 3 ESC3-MTP021 RDR V3.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/IVA12OZC461E",
             "citation": "NOAA NESDIS. 2022-08-22. VISSRSMS2IMIR. Version 001. VISSR/SMS-2 Infrared Imagery on 70mm Film V001. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/IVA12OZC461E. https://disc.gsfc.nasa.gov/datacollection/VISSRSMS2IMIR_001.html. Digital Science Data.",
-            "issued": "2018-03-13",
-            "temporal": "1975-02-22T00:00:00Z/1980-02-01T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2018-03-13",
-            "keyword": [
-                "earth science",
-                "spectral/engineering",
-                "infrared wavelengths"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "JAMES JOHNSON",
                 "hasEmail": "mailto:James.Johnson@nasa.gov"
             },
+            "creator": "NOAA NESDIS",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C2386956718-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "VISSRSMS2IMIR is the Visible Infrared Spin-Scan Radiometer (VISSR) Infrared Imagery on 70mm Film data product from the second Synchronous Meteorological Satellite (SMS-2). This set of IR imagery (10.5 to 12.5 micrometer) was originally produced on commercial image-generation equipment from digital tapes and was made available on 70-mm film, from which they were later scanned to digital TIFF image files. Each TIFF scan contains 2 or 3 pictures, and there are several hundred scans from an original 70 mm film roll which are combined into a ZIP file. Each picture contains a title on the top boundary and a 33-level gray scale on the right boundary that represents brightness temperatures. It may have a combination of the following options: 1) contrast enhancement, 2) image sectorization, and 3) 1/16-size imagery. The maximum effective size covers 500 sq km, represented by 4000 by 3904 pixels. Each element has a maximum resolution of 3.7 km. The title contains the satellite identification, picture number, picture type, coordinate numbers of the top left pixel relative to the visible sensor, start time of sectorized image, and pixel scaling and sector size identification.\n\nThe SMS-2 satellite was initially parked over the equator at longitude 105W on Feb 22, 1975 viewing the hemisphere below the satellite. It was moved to its final operational position at 135W on Dec 19, 1975. The VISSR experiment was operated by the NOAA National Environmental Satellite Data and Information Service (NESDIS), as well as scientists from NASA Goddard Space Flight Center.\n\nThis product was previously available from the NSSDC with the identifier ESAD-00038 (old ID 75-011A-04C).",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "VISSRSMS2IMIR",
-            "creator": "NOAA NESDIS",
-            "title": "VISSR/SMS-2 Infrared Imagery on 70mm Film V001 (VISSRSMS2IMIR) at GES DISC",
-            "graphic-preview-description": "Typical SMS-2 VISSR visible 70mm film image.",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/VISSRSMS2IMIR_001.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FIVA12OZC461E",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FIVA12OZC461E",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/VISSRSMS2IMIR_001.png",
-                    "description": "Typical SMS-2 VISSR visible 70mm film image.",
                     "@type": "dcat:Distribution",
+                    "description": "Typical SMS-2 VISSR visible 70mm film image.",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/VISSRSMS2IMIR_001.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/VISSRSMS2IMIR_001.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/VISSRSMS2IMIR_001.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/SMS/VISSRSMS2IMIR.001/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/SMS/VISSRSMS2IMIR.001/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=VISSRSMS2IMIR",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=VISSRSMS2IMIR",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/SMS/VISSRSMS2IMIR.001/doc/README.VISSRSMSGOESIM.001.pdf",
-                    "description": "README Document",
                     "@type": "dcat:Distribution",
+                    "description": "README Document",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/SMS/VISSRSMS2IMIR.001/doc/README.VISSRSMSGOESIM.001.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's read me document"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/repository/Mission/Nimbus/3.3_Product_Documentation/3.3.5_Product_Quality/GOES_SMS_Users_Guide.pdf",
-                    "description": "The GOES/SMS User's Guide",
                     "@type": "dcat:Distribution",
+                    "description": "The GOES/SMS User's Guide",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/repository/Mission/Nimbus/3.3_Product_Documentation/3.3.5_Product_Quality/GOES_SMS_Users_Guide.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/repository/Mission/Nimbus/3.3_Product_Documentation/3.3.5_Product_Quality/VISSR_data_processing_plan.pdf",
-                    "description": "VISSR Data Processing Plan for SMS/GOES Satellites",
                     "@type": "dcat:Distribution",
+                    "description": "VISSR Data Processing Plan for SMS/GOES Satellites",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/repository/Mission/Nimbus/3.3_Product_Documentation/3.3.5_Product_Quality/VISSR_data_processing_plan.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "graphic-preview-description": "Typical SMS-2 VISSR visible 70mm film image.",
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/VISSRSMS2IMIR_001.png",
+            "identifier": "C2386956718-GES_DISC",
+            "issued": "2018-03-13",
+            "keyword": [
+                "earth science",
+                "spectral/engineering",
+                "infrared wavelengths"
+            ],
+            "landingPage": "https://doi.org/10.5067/IVA12OZC461E",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2018-03-13",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
+            },
+            "release-place": "Greenbelt, MD, USA",
+            "series-name": "VISSRSMS2IMIR",
             "spatial": "135.0 -90.0 -25.0 90.0",
+            "temporal": "1975-02-22T00:00:00Z/1980-02-01T23:59:59.999Z",
             "theme": [
                 "GOES",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "VISSR/SMS-2 Infrared Imagery on 70mm Film V001 (VISSRSMS2IMIR) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-A%2FCAL-ALICE-3-AST1-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This data set contains CODMAC level 3 data acquired by the Rosetta Orbiter ALICE UV Spectrometer during the fly-by of the asteroid (2867) Steins, which occurred on 2008-09-05.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-a-cal-alice-3-ast1-v1.0_g3nc-nnza",
             "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "2867 steins",
                 "calibration",
                 "international rosetta mission"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-A%2FCAL-ALICE-3-AST1-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-a-cal-alice-3-ast1-v1.0_g3nc-nnza",
-            "description": "This data set contains CODMAC level 3 data acquired by the Rosetta Orbiter ALICE UV Spectrometer during the fly-by of the asteroid (2867) Steins, which occurred on 2008-09-05.",
-            "title": "ROSETTA-ORBITER STEINS/CAL ALICE 3 AST1 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "ROSETTA-ORBITER STEINS/CAL ALICE 3 AST1 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/GPMGV/LPVEX/POSS/DATA101",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Rodriguez, Peter .2019. GPM Ground Validation Precipitation Occurrence Sensor System (POSS) LPVEx [indicate subset used]. Dataset available online from the NASA Global Hydrometeorology Resource Center DAAC, Huntsville, Alabama, U.S.A. DOI: http://dx.doi.org/10.5067/GPMGV/LPVEX/POSS/DATA101",
-            "issued": "2019-07-23",
-            "temporal": "2010-09-17T13:49:00Z/2011-04-20T05:36:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-04-28",
-            "keyword": [
-                "clouds",
-                "earth science",
-                "precipitation",
-                "radar",
-                "atmosphere",
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
-            "identifier": "C1979685546-GHRC_DAAC",
             "description": "The GPM Ground Validation Precipitation Occurrence Sensor System (POSS) LPVEx dataset consists of precipitation and radar parameter estimates for both liquid and solid precipitation. Measurements were collected by the Precipitation Occurrence Sensor System (POSS) during the Global Precipitation Measurement (GPM) mission Light Precipitation Validation Experiment (LPVEx) field campaign.  This field campaign took place around the Gulf of Finland in September and October of 2010. The goal of the campaign was to provide additional high-latitude, light rainfall measurements for the improvement of GPM satellite precipitation algorithms. The POSS dataset files are available from September 18, 2010 through April 20, 2011 for two POSS sites: Emasalo and Jarvenpaa. The data files are in CSV format with browse imagery in PNG format.",
-            "graphic-preview-description": "N/A",
-            "title": "GPM Ground Validation Precipitation Occurrence Sensor System (POSS) LPVEx V1",
-            "graphic-preview-file": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/lpvex/poss/browse/",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGPMGV%2FLPVEX%2FPOSS%2FDATA101",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGPMGV%2FLPVEX%2FPOSS%2FDATA101",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=gpmposslpvex",
-                    "description": "Files may be downloaded directly to your workstation from this link",
                     "@type": "dcat:Distribution",
+                    "description": "Files may be downloaded directly to your workstation from this link",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=gpmposslpvex",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/lpvex/poss/browse/Jarvenpaa/lpvex_poss_PR_20101014_JAR.png",
-                    "description": "Sample Browse Image",
                     "@type": "dcat:Distribution",
+                    "description": "Sample Browse Image",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/lpvex/poss/browse/Jarvenpaa/lpvex_poss_PR_20101014_JAR.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/home/sites/default/files/lpvex_science_plan_June2010.pdf",
-                    "description": "Light Precipitation Validation Experiment (LPVEx) Science Plan",
                     "@type": "dcat:Distribution",
+                    "description": "Light Precipitation Validation Experiment (LPVEx) Science Plan",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/home/sites/default/files/lpvex_science_plan_June2010.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ntrs.nasa.gov/search.jsp?R=20110015768",
-                    "description": "The NASA CloudSat/GPM Light Precipitation Validation Experiment (LPVEx)",
                     "@type": "dcat:Distribution",
+                    "description": "The NASA CloudSat/GPM Light Precipitation Validation Experiment (LPVEx)",
+                    "downloadURL": "https://ntrs.nasa.gov/search.jsp?R=20110015768",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/lpvex/poss/doc/gpmposslpvex_dataset.pdf",
-                    "description": "The guide document contains detailed information about the dataset",
                     "@type": "dcat:Distribution",
+                    "description": "The guide document contains detailed information about the dataset",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/lpvex/poss/doc/gpmposslpvex_dataset.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/lpvex/poss/doc/2013-Feb-11_Documentation_for_New_Gen_PR_files.pdf",
-                    "description": "Description of the POSS post processed \u201cPR\u201d file",
                     "@type": "dcat:Distribution",
+                    "description": "Description of the POSS post processed \u201cPR\u201d file",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/lpvex/poss/doc/2013-Feb-11_Documentation_for_New_Gen_PR_files.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View the primary investigator's documentation for this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.1175/JAMC-D-13-0334.1",
-                    "description": "WRF\u2013 SBM Simulations of Melting-Layer Structure in Mixed-Phase Precipitation Events Observed during LPVEx",
                     "@type": "dcat:Distribution",
+                    "description": "WRF\u2013 SBM Simulations of Melting-Layer Structure in Mixed-Phase Precipitation Events Observed during LPVEx",
+                    "downloadURL": "https://doi.org/10.1175/JAMC-D-13-0334.1",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.1175/JTECH1956.1",
-                    "description": "Sampling Errors in the Measurement of Rainfall Parameters Using the Precipitation Occurrence Sensor System (POSS)",
                     "@type": "dcat:Distribution",
+                    "description": "Sampling Errors in the Measurement of Rainfall Parameters Using the Precipitation Occurrence Sensor System (POSS)",
+                    "downloadURL": "https://doi.org/10.1175/JTECH1956.1",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.1175/2007JTECHA957.1",
-                    "description": "Performance of the Precipitation Occurrence Sensor System as a Precipitation Gauge",
                     "@type": "dcat:Distribution",
+                    "description": "Performance of the Precipitation Occurrence Sensor System as a Precipitation Gauge",
+                    "downloadURL": "https://doi.org/10.1175/2007JTECHA957.1",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/home/field-campaigns/lpvex",
-                    "description": "LPVEx Field Campaign Project Homepage",
                     "@type": "dcat:Distribution",
+                    "description": "LPVEx Field Campaign Project Homepage",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/home/field-campaigns/lpvex",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/lpvex/poss/browse/",
-                    "description": "N/A",
                     "@type": "dcat:Distribution",
+                    "description": "N/A",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/lpvex/poss/browse/",
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
+            "graphic-preview-file": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/lpvex/poss/browse/",
+            "identifier": "C1979685546-GHRC_DAAC",
+            "issued": "2019-07-23",
+            "keyword": [
+                "clouds",
+                "earth science",
+                "precipitation",
+                "radar",
+                "atmosphere",
+                "spectral/engineering"
+            ],
+            "landingPage": "https://doi.org/10.5067/GPMGV/LPVEX/POSS/DATA101",
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
             "spatial": "25.0822 60.2038 25.6248 60.4847",
+            "temporal": "2010-09-17T13:49:00Z/2011-04-20T05:36:00Z",
             "theme": [
                 "LPVEX",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "GPM Ground Validation Precipitation Occurrence Sensor System (POSS) LPVEx V1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ASTER/AST14DEM.003",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "ASA/METI/AIST/Japan Spacesystems and U.S./Japan ASTER Science Team. AST14DEM.003. ASTER DEM Product. Sioux Falls, South Dakota, USA. Archived by National Aeronautics and Space Administration, U.S. Government, NASA EOSDIS Land Processes Distributed Active Archive Center. https://doi.org/10.5067/ASTER/AST14DEM.003. https://doi.org/10.5067/ASTER/AST14DEM.003. The DOI landing page provides citations in APA and Chicago styles..",
-            "issued": "2000-03-06",
-            "temporal": "2000-03-06T00:30:05Z/2024-12-16T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-28",
-            "keyword": [
-                "topography",
-                "earth science",
-                "land surface",
-                "national geospatial data asset",
-                "ngda"
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
-            "identifier": "C1299783579-LPDAAC_ECS",
-            "description": "The ASTER Digital Elevation Model (AST14DEM) product is generated (https://lpdaac.usgs.gov/documents/996/ASTER_Earthdata_Search_Order_Instructions.pdf) using bands 3N (nadir-viewing) and 3B (backward-viewing) of an (ASTER Level 1A) (https://doi.org/10.5067/ASTER/AST_L1A.003) image acquired by the Visible and Near Infrared (VNIR) sensor. The VNIR subsystem includes two independent telescope assemblies that facilitate the generation of stereoscopic data. The band 3 stereo pair is acquired in the spectral range of 0.78 and 0.86 microns with a base-to-height ratio of 0.6 and an intersection angle of 27.7 degrees. There is a time lag of approximately one minute between the acquisition of the nadir and backward images. For a better understanding, refer to this (diagram) (https://lpdaac.usgs.gov/documents/301/ASTER_Along_Track_Imaging_Geometry.png) depicting the along-track imaging geometry of the ASTER VNIR nadir and backward-viewing sensors.\r\n\r\nThe accuracy of the new LP DAAC produced DEMs will meet or exceed accuracy specifications set for the ASTER relative DEMs by the Algorithm Theoretical Basis Document (ATBD) (https://lpdaac.usgs.gov/documents/81/AST14_ATBD.pdf). Users likely will find that the DEMs produced by the new LP DAAC system have accuracies approaching those specified in the ATBD for absolute DEMs. Validation testing has shown that DEMs produced by the new system frequently are more accurate than 25 meters root mean square error (RMSE) in xyz dimensions.\r\n\r\nImprovements/Changes from Previous Versions\r\n\r\nAs of January 2021, the LP DAAC has implemented version 3.0 of the Sensor Information Laboratory Corporation ASTER DEM/Ortho (SILCAST) software, which is used to generate the Level 2 on-demand ASTER Orthorectified and Digital Elevation Model (DEM) products (AST14). The updated software provides digital elevation extraction and orthorectification from ASTER L1B input data without needing to enter ground control points or depending on external global DEMs at 30-arc-second resolution (GTOPO30). It utilizes the ephemeris and attitude data derived from both the ASTER instrument and the Terra spacecraft platform. The outputs are geoid height-corrected and waterbodies are automatically detected in this version. Users will notice differences between AST14DEM, AST14DMO, and AST14OTH products ordered before January 2021 (generated with SILCAST V1) and those generated with the updated version of the production software (version 3.0). Differences may include slight elevation changes over different surface types, including waterbodies. Differences have also been observed over cloudy portions of ASTER scenes. Additional information on SILCAST version 3.0 can be found on the  SILCAST website (http://www.silc.co.jp/en/products.html).\r\n\r\nStarting June 23, 2021, radiometric calibration coefficient Version 5 (RCC V5) will be applied to newly observed ASTER data and archived ASTER data products. Details regarding RCC V5 are described in the following journal article.\r\n\r\nTsuchida, S., Yamamoto, H., Kouyama, T., Obata, K., Sakuma, F., Tachikawa, T., Kamei, A., Arai, K., Czapla-Myers, J.S., Biggar, S.F., and Thome, K.J., 2020, Radiometric Degradation Curves for the ASTER VNIR Processing Using Vicarious and Lunar Calibrations: Remote Sensing, v. 12, no. 3, at https://doi.org/10.3390/rs12030427.",
-            "release-place": "Sioux Falls, South Dakota, USA",
-            "series-name": "AST14DEM.003",
-            "graphic-preview-description": "Browse image for Earthdata Search",
             "creator": "ASA/METI/AIST/Japan Spacesystems and U.S./Japan ASTER Science Team",
-            "title": "ASTER Digital Elevation Model V003",
-            "graphic-preview-file": "https://e4ftl01.cr.usgs.gov/WORKING/BRWS/Browse.001/2021.06.16/pg-BR1A0000-2021061601_029_043.1.VNIR.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The ASTER Digital Elevation Model (AST14DEM) product is generated (https://lpdaac.usgs.gov/documents/996/ASTER_Earthdata_Search_Order_Instructions.pdf) using bands 3N (nadir-viewing) and 3B (backward-viewing) of an (ASTER Level 1A) (https://doi.org/10.5067/ASTER/AST_L1A.003) image acquired by the Visible and Near Infrared (VNIR) sensor. The VNIR subsystem includes two independent telescope assemblies that facilitate the generation of stereoscopic data. The band 3 stereo pair is acquired in the spectral range of 0.78 and 0.86 microns with a base-to-height ratio of 0.6 and an intersection angle of 27.7 degrees. There is a time lag of approximately one minute between the acquisition of the nadir and backward images. For a better understanding, refer to this (diagram) (https://lpdaac.usgs.gov/documents/301/ASTER_Along_Track_Imaging_Geometry.png) depicting the along-track imaging geometry of the ASTER VNIR nadir and backward-viewing sensors.\r\n\r\nThe accuracy of the new LP DAAC produced DEMs will meet or exceed accuracy specifications set for the ASTER relative DEMs by the Algorithm Theoretical Basis Document (ATBD) (https://lpdaac.usgs.gov/documents/81/AST14_ATBD.pdf). Users likely will find that the DEMs produced by the new LP DAAC system have accuracies approaching those specified in the ATBD for absolute DEMs. Validation testing has shown that DEMs produced by the new system frequently are more accurate than 25 meters root mean square error (RMSE) in xyz dimensions.\r\n\r\nImprovements/Changes from Previous Versions\r\n\r\nAs of January 2021, the LP DAAC has implemented version 3.0 of the Sensor Information Laboratory Corporation ASTER DEM/Ortho (SILCAST) software, which is used to generate the Level 2 on-demand ASTER Orthorectified and Digital Elevation Model (DEM) products (AST14). The updated software provides digital elevation extraction and orthorectification from ASTER L1B input data without needing to enter ground control points or depending on external global DEMs at 30-arc-second resolution (GTOPO30). It utilizes the ephemeris and attitude data derived from both the ASTER instrument and the Terra spacecraft platform. The outputs are geoid height-corrected and waterbodies are automatically detected in this version. Users will notice differences between AST14DEM, AST14DMO, and AST14OTH products ordered before January 2021 (generated with SILCAST V1) and those generated with the updated version of the production software (version 3.0). Differences may include slight elevation changes over different surface types, including waterbodies. Differences have also been observed over cloudy portions of ASTER scenes. Additional information on SILCAST version 3.0 can be found on the  SILCAST website (http://www.silc.co.jp/en/products.html).\r\n\r\nStarting June 23, 2021, radiometric calibration coefficient Version 5 (RCC V5) will be applied to newly observed ASTER data and archived ASTER data products. Details regarding RCC V5 are described in the following journal article.\r\n\r\nTsuchida, S., Yamamoto, H., Kouyama, T., Obata, K., Sakuma, F., Tachikawa, T., Kamei, A., Arai, K., Czapla-Myers, J.S., Biggar, S.F., and Thome, K.J., 2020, Radiometric Degradation Curves for the ASTER VNIR Processing Using Vicarious and Lunar Calibrations: Remote Sensing, v. 12, no. 3, at https://doi.org/10.3390/rs12030427.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASTER%2FAST14DEM.003",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASTER%2FAST14DEM.003",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
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
-                    "downloadURL": "https://asterweb.jpl.nasa.gov/",
-                    "description": "The ASTER home page is maintained through NASA's Jet Propulsion Laboratory and documents various aspects of the ASTER mission.",
                     "@type": "dcat:Distribution",
+                    "description": "The ASTER home page is maintained through NASA's Jet Propulsion Laboratory and documents various aspects of the ASTER mission.",
+                    "downloadURL": "https://asterweb.jpl.nasa.gov/",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/ASTER/AST14DEM.003",
-                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
+                    "downloadURL": "https://doi.org/10.5067/ASTER/AST14DEM.003",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=C1299783579-LPDAAC_ECS",
-                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=C1299783579-LPDAAC_ECS",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
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
-                    "downloadURL": "https://lpdaac.usgs.gov/documents/80/AST14_User_Guide_V3.pdf",
-                    "description": "ASTER Higher-Level Product User Guide",
                     "@type": "dcat:Distribution",
+                    "description": "ASTER Higher-Level Product User Guide",
+                    "downloadURL": "https://lpdaac.usgs.gov/documents/80/AST14_User_Guide_V3.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://lpdaac.usgs.gov/documents/81/AST14_ATBD.pdf",
-                    "description": "The ATBD provides physical theory and mathematical procedures for the calculations used to produce the data products.",
                     "@type": "dcat:Distribution",
+                    "description": "The ATBD provides physical theory and mathematical procedures for the calculations used to produce the data products.",
+                    "downloadURL": "https://lpdaac.usgs.gov/documents/81/AST14_ATBD.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's algorithm theoretical basis document"
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
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://lpdaac.usgs.gov/documents/642/DEM_Comparison_Guide.pdf",
-                    "description": "DEM Comparison Guide",
                     "@type": "dcat:Distribution",
+                    "description": "DEM Comparison Guide",
+                    "downloadURL": "https://lpdaac.usgs.gov/documents/642/DEM_Comparison_Guide.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's product usage"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://e4ftl01.cr.usgs.gov/WORKING/BRWS/Browse.001/2021.06.16/pg-BR1A0000-2021061601_029_043.1.VNIR.jpg",
-                    "description": "Browse image for Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse image for Earthdata Search",
+                    "downloadURL": "https://e4ftl01.cr.usgs.gov/WORKING/BRWS/Browse.001/2021.06.16/pg-BR1A0000-2021061601_029_043.1.VNIR.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://lpdaac.usgs.gov/documents/1010/ASTER_User_Handbook_v3.pdf",
-                    "description": "The ASTER User Handbook provides in depth information on ASTER data products.",
                     "@type": "dcat:Distribution",
+                    "description": "The ASTER User Handbook provides in depth information on ASTER data products.",
+                    "downloadURL": "https://lpdaac.usgs.gov/documents/1010/ASTER_User_Handbook_v3.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
                 }
             ],
+            "graphic-preview-description": "Browse image for Earthdata Search",
+            "graphic-preview-file": "https://e4ftl01.cr.usgs.gov/WORKING/BRWS/Browse.001/2021.06.16/pg-BR1A0000-2021061601_029_043.1.VNIR.jpg",
+            "identifier": "C1299783579-LPDAAC_ECS",
+            "issued": "2000-03-06",
+            "keyword": [
+                "topography",
+                "earth science",
+                "land surface",
+                "national geospatial data asset",
+                "ngda"
+            ],
+            "landingPage": "https://doi.org/10.5067/ASTER/AST14DEM.003",
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
+            "series-name": "AST14DEM.003",
             "spatial": "-180.0 -83.0 180.0 83.0",
+            "temporal": "2000-03-06T00:30:05Z/2024-12-16T00:00:00Z",
             "theme": [
                 "Terra",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "ASTER Digital Elevation Model V003"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MR9%2FVO1%2FVO2-M-RSS-5-GRAVITY-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This archive contains maps of the Bouguer anomalies, free-gravity accelerations, and geoid anomalies of Mars, along with spherical harmonic gravity and topography models and occultation data acquired with Mariner 9 and the Viking Orbiter.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mr9-vo1-vo2-m-rss-5-gravity-v1.0_g3st-t4bf",
             "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "viking",
                 "mars",
                 "mariner71"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MR9%2FVO1%2FVO2-M-RSS-5-GRAVITY-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mr9-vo1-vo2-m-rss-5-gravity-v1.0_g3st-t4bf",
-            "description": "This archive contains maps of the Bouguer anomalies, free-gravity accelerations, and geoid anomalies of Mars, along with spherical harmonic gravity and topography models and occultation data acquired with Mariner 9 and the Viking Orbiter.",
-            "title": "unk",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "unk"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-X-RSI-1%2F2%2F3-CR2-0024-V1.0",
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
-                "sun"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This is a Solar Conjunction measurement covering the time 2006-03-31T00:25:41.500 to 2006-03-31T03:38:28.500.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-x-rsi-1-2-3-cr2-0024-v1.0_g3sv-v54z",
+            "issued": "2018-06-26",
+            "keyword": [
+                "international rosetta mission",
+                "sun"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-X-RSI-1%2F2%2F3-CR2-0024-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-x-rsi-1-2-3-cr2-0024-v1.0_g3sv-v54z",
-            "description": "This is a Solar Conjunction measurement covering the time 2006-03-31T00:25:41.500 to 2006-03-31T03:38:28.500.",
-            "title": "ROSETTA-ORBITER SUN RSI 1/2/3 CRUISE 2 0024 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "ROSETTA-ORBITER SUN RSI 1/2/3 CRUISE 2 0024 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/KPUMVXFEQLA1",
             "citation": "Global Modeling and Assimilation Office (GMAO). 2015-06-30. M2TUNXAER. Version 5.12.4. MERRA-2 tavgU_2d_aer_Nx: 2d,diurnal,Time-averaged,Single-Level,Assimilation,Aerosol Diagnostics V5.12.4. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/KPUMVXFEQLA1. https://disc.gsfc.nasa.gov/datacollection/M2TUNXAER_5.12.4.html. Digital Science Data.",
-            "issued": "2007-06-14",
-            "temporal": "1980-01-01T00:00:00Z/2024-03-27T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2015-07-07",
-            "references": [
-                "https://doi.org/10.1175/JCLI-D-16-0758.1",
-                "https://doi.org/10.5194/gmd-8-1339-2015",
-                "https://doi.org/10.1175/JCLI-D-16-0609.1",
-                "https://doi.org/10.1175/JCLI-D-16-0613.1",
-                "https://doi.org/10.1175/JCLI-D-16-0570.1",
-                "https://doi.org/10.1175/JCLI-D-16-0720.1",
-                "https://doi.org/NASA/TM\u20132015-104606/Vol. 43",
-                "https://doi.org/10.1177/1094342005056120"
-            ],
-            "keyword": [
-                "public health",
-                "atmospheric chemistry",
-                "human dimensions",
-                "earth science",
-                "atmosphere",
-                "aerosols",
-                "air quality"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "DANA OSTRENGA",
                 "hasEmail": "mailto:dana.ostrenga@nasa.gov"
             },
+            "creator": "Global Modeling and Assimilation Office (GMAO)",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C1276812869-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "M2TUNXAER (or  tavgU_2d_aer_Nx) is a time-averaged 2-dimensional monthly diurnal means data collection in Modern-Era Retrospective analysis for Research and Applications version 2 (MERRA-2).  This collection consists of assimilated aerosol diagnostics, such as column mass density of aerosol components (black carbon, dust, sea salt, sulfate, and organic carbon), surface mass concentration of aerosol components, and total extinction (and scattering ) aerosol optical thickness (AOT) at 550 nm.   The total PM1.0, PM2.5, and PM10 may be derived with the formula described in the FAQs under the Documentation tab of this page.  This data collection is the monthly mean of data fields for each hour and is time-stamped with the central time of an hour starting from 00:30 UTC, e.g.: 00:30, 01:30, \u2026 , 23:30 UTC.\n\nMERRA-2 is the latest version of global atmospheric reanalysis for the satellite era produced by NASA Global Modeling and Assimilation Office (GMAO) using the Goddard Earth Observing System Model (GEOS) version 5.12.4.  The dataset covers the period of 1980-present with the latency of ~3 weeks after the end of a month. \n\nData Reprocessing:  Please check \u201cRecords of MERRA-2 Data Reprocessing and Service Changes\u201d linked from the \u201cDocumentation\u201d tab on this page.  Note that a reprocessed data filename is different from the original file.\n\nMERRA-2 Mailing List: Sign up to receive information on reprocessing of data, changing of tools and services, as well as data announcements from GMAO. Contact the GES DISC Help Desk (gsfc-dl-help-disc@mail.nasa.gov) to be added to the list.\n\nQuestions: If you have a question, please read \"MERRA-2 File Specification Document\",  \u201cMERRA-2 Data Access \u2013 Quick Start Guide\u201d, and FAQs linked from the \u201dDocumentation\u201d tab on this page.  If that does not answer your question, you may email the question on data access to the GES DISC Help Desk (gsfc-dl-help-disc@mail.nasa.gov), or the question on science to the MERRA-2 science team (merra-questions@lists.nasa.gov).",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "M2TUNXAER",
-            "creator": "Global Modeling and Assimilation Office (GMAO)",
-            "graphic-preview-description": "M2TUNXAER variable",
-            "title": "MERRA-2 tavgU_2d_aer_Nx: 2d,diurnal,Time-averaged,Single-Level,Assimilation,Aerosol Diagnostics 0.625 x 0.5 degree V5.12.4 (M2TUNXAER) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/M2TUNXAER_5.12.4.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FKPUMVXFEQLA1",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FKPUMVXFEQLA1",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/M2TUNXAER_5.12.4.png",
-                    "description": "M2TUNXAER variable",
                     "@type": "dcat:Distribution",
+                    "description": "M2TUNXAER variable",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/M2TUNXAER_5.12.4.png",
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
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/M2TUNXAER_5.12.4.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/M2TUNXAER_5.12.4.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://goldsmr4.gesdisc.eosdis.nasa.gov/data/MERRA2_DIURNAL/M2TUNXAER.5.12.4/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://goldsmr4.gesdisc.eosdis.nasa.gov/data/MERRA2_DIURNAL/M2TUNXAER.5.12.4/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=M2TUNXAER",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=M2TUNXAER",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://goldsmr4.gesdisc.eosdis.nasa.gov/dods/M2TUNXAER.info",
-                    "description": "The GrADS Data Server (GDS) is another form of OPeNDAP that provides subsetting and some analysis services across the Internet.",
                     "@type": "dcat:Distribution",
+                    "description": "The GrADS Data Server (GDS) is another form of OPeNDAP that provides subsetting and some analysis services across the Internet.",
+                    "downloadURL": "https://goldsmr4.gesdisc.eosdis.nasa.gov/dods/M2TUNXAER.info",
+                    "mediaType": "text/html",
                     "title": "Use GRADS DATA SERVER (GDS) to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://goldsmr4.gesdisc.eosdis.nasa.gov/opendap/MERRA2_DIURNAL/M2TUNXAER.5.12.4/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://goldsmr4.gesdisc.eosdis.nasa.gov/opendap/MERRA2_DIURNAL/M2TUNXAER.5.12.4/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://goldsmr4.gesdisc.eosdis.nasa.gov/thredds/catalog/MERRA2_DIURNAL_aggregation/catalog.html?dataset=merra2_diurnal_aggregation%2FM2TUNXAER.5.12.4_Aggregation.ncml",
-                    "description": "Time aggregated THREDDS Data Server (TDS)",
                     "@type": "dcat:Distribution",
+                    "description": "Time aggregated THREDDS Data Server (TDS)",
+                    "downloadURL": "https://goldsmr4.gesdisc.eosdis.nasa.gov/thredds/catalog/MERRA2_DIURNAL_aggregation/catalog.html?dataset=merra2_diurnal_aggregation%2FM2TUNXAER.5.12.4_Aggregation.ncml",
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
-                    "downloadURL": "https://goldsmr4.gesdisc.eosdis.nasa.gov/data/MERRA2_DIURNAL/M2TUNXAER.5.12.4/doc/MERRA2.README.pdf",
-                    "description": "README Document",
                     "@type": "dcat:Distribution",
+                    "description": "README Document",
+                    "downloadURL": "https://goldsmr4.gesdisc.eosdis.nasa.gov/data/MERRA2_DIURNAL/M2TUNXAER.5.12.4/doc/MERRA2.README.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's read me document"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/information/mission-project?title=MERRA-2",
-                    "description": "MERRA-2 Data Access \u2013 Quick Start Guide",
                     "@type": "dcat:Distribution",
+                    "description": "MERRA-2 Data Access \u2013 Quick Start Guide",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/information/mission-project?title=MERRA-2",
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
+            "graphic-preview-description": "M2TUNXAER variable",
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/M2TUNXAER_5.12.4.png",
+            "identifier": "C1276812869-GES_DISC",
+            "issued": "2007-06-14",
+            "keyword": [
+                "public health",
+                "atmospheric chemistry",
+                "human dimensions",
+                "earth science",
+                "atmosphere",
+                "aerosols",
+                "air quality"
+            ],
+            "landingPage": "https://doi.org/10.5067/KPUMVXFEQLA1",
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
+                "https://doi.org/NASA/TM\u20132015-104606/Vol. 43",
+                "https://doi.org/10.1177/1094342005056120"
+            ],
+            "release-place": "Greenbelt, MD, USA",
+            "series-name": "M2TUNXAER",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "1980-01-01T00:00:00Z/2024-03-27T00:00:00Z",
             "theme": [
                 "MERRA-2",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "MERRA-2 tavgU_2d_aer_Nx: 2d,diurnal,Time-averaged,Single-Level,Assimilation,Aerosol Diagnostics 0.625 x 0.5 degree V5.12.4 (M2TUNXAER) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ADEOS-I/OCTS/L3M/CHL/2014",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/GSFC/SED/ESD/GCDC/OB.DAAC. https://doi.org/10.5067/ADEOS-I/OCTS/L3M/CHL/2014.",
-            "issued": "2017-01-11",
-            "temporal": "1996-11-01T00:00:00Z/1997-06-30T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2018-10-10",
-            "keyword": [
-                "ocean chemistry",
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
-            "identifier": "C1200034342-OB_DAAC",
             "description": "On August 17, 1996, the Japanese Space Agency (NASDA - National Space Development Agency)\nlaunched the Advanced Earth Observing Satellite (ADEOS). ADEOS was in a descending, Sun\nsynchronous orbit with a nominal equatorial crossing time of 10:30 a.m. Amoung the\ninstruments carried aboard the ADEOS spacecraft was the Ocean Color and Temperature\nScanner (OCTS). OCTS is an optical radiometer with 12 bands covering the visible, near\ninfrared and thermal infrared regions. (Eight of the bands are in the VIS/NIR. These are\nthe only bands calibrated and processed by the OBPG) OCTS has a swath width of\napproximately 1400 km, and a nominal nadir resolution of 700 m. The instrument operated\nat three tilt states (20 degrees aft, nadir and 20 degrees fore), similar to SeaWiFS.",
-            "title": "ADEOS-I Ocean Color and Temperature Scanner (OCTS) Chlorophyll (CHL) Global Mapped Data",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FADEOS-I%2FOCTS%2FL3M%2FCHL%2F2014",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FADEOS-I%2FOCTS%2FL3M%2FCHL%2F2014",
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
-                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/atbd/chlor_a",
-                    "description": "NASA Ocean Color Web - Algorithm Descriptions",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Ocean Color Web - Algorithm Descriptions",
+                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/atbd/chlor_a",
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
-                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/data/10.5067/ADEOS-I/OCTS/L3M/CHL/2014",
-                    "description": "OB.DAAC OCTS ADEOS-I L3M Chlorophyll (CHL) Landing Page",
                     "@type": "dcat:Distribution",
+                    "description": "OB.DAAC OCTS ADEOS-I L3M Chlorophyll (CHL) Landing Page",
+                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/data/10.5067/ADEOS-I/OCTS/L3M/CHL/2014",
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
+            "identifier": "C1200034342-OB_DAAC",
+            "issued": "2017-01-11",
+            "keyword": [
+                "ocean chemistry",
+                "earth science",
+                "oceans"
+            ],
+            "landingPage": "https://doi.org/10.5067/ADEOS-I/OCTS/L3M/CHL/2014",
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
+            "title": "ADEOS-I Ocean Color and Temperature Scanner (OCTS) Chlorophyll (CHL) Global Mapped Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/MEASURES/WVCC/DATA206",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Eric Fetzer, Brian Wilson, and Gerald Manipon. 2017-05-10. AIRS_MDS_IND. Version 1.0. Aqua AIRS-MODIS Matchup Indexes V1.0. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/MEASURES/WVCC/DATA206. https://disc.gsfc.nasa.gov/datacollection/AIRS_MDS_IND_1.0.html. Digital Science Data.",
-            "issued": "2017-05-01",
-            "temporal": "2003-01-01T00:00:00Z/2022-01-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2017-05-10",
-            "keyword": [
-                "earth science",
-                "clouds",
-                "national geospatial data asset",
-                "ngda",
-                "atmosphere"
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
-            "identifier": "C1385303964-GES_DISC",
-            "description": "This is Aqua AIRS-MODIS collocation indexes, in netCDF-4  format. These data map AIRS profile indexes to those of MODIS.\n\nThe basic task is to bring together retrievals of water vapor and cloud properties from multiple \"A-train\" instruments (AIRS, AMSR-E, MODIS, AMSU, MLS, & CloudSat), classify each \"scene\" (instrument look) using the cloud information, and develop a merged, multi-sensor climatology of atmospheric water vapor as a function of altitude, stratified by the cloud classes. This is a large science analysis project that will require the use of SciFlo technologies to discover and organize all of the datasets, move and cache datasets as required, find space/time \"matchups\" between pairs of instruments, and process years of satellite data to produce the climate data records.\n\nThe short name for this collections is AIRS_MDS_IND",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "AIRS_MDS_IND",
             "creator": "Eric Fetzer, Brian Wilson, and Gerald Manipon",
-            "title": "Aqua AIRS-MODIS Matchup Indexes V1.0 (AIRS_MDS_IND) at GES_DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/MEaSUREs/Fetzer/AIRS_MDS_IND.png",
-            "programCode": [
-                "026:001"
-            ],
+            "data-presentation-form": "Digital Science Data",
+            "description": "This is Aqua AIRS-MODIS collocation indexes, in netCDF-4  format. These data map AIRS profile indexes to those of MODIS.\n\nThe basic task is to bring together retrievals of water vapor and cloud properties from multiple \"A-train\" instruments (AIRS, AMSR-E, MODIS, AMSU, MLS, & CloudSat), classify each \"scene\" (instrument look) using the cloud information, and develop a merged, multi-sensor climatology of atmospheric water vapor as a function of altitude, stratified by the cloud classes. This is a large science analysis project that will require the use of SciFlo technologies to discover and organize all of the datasets, move and cache datasets as required, find space/time \"matchups\" between pairs of instruments, and process years of satellite data to produce the climate data records.\n\nThe short name for this collections is AIRS_MDS_IND",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMEASURES%2FWVCC%2FDATA206",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMEASURES%2FWVCC%2FDATA206",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
@@ -794026,10 +794002,10 @@
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/AIRS_MDS_IND_1.0.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/AIRS_MDS_IND_1.0.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
@@ -794039,10 +794015,10 @@
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=AIRS_MDS_IND",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=AIRS_MDS_IND",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
@@ -794058,208 +794034,208 @@
                     "title": "View this dataset's read me document"
                 }
             ],
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/MEaSUREs/Fetzer/AIRS_MDS_IND.png",
+            "identifier": "C1385303964-GES_DISC",
+            "issued": "2017-05-01",
+            "keyword": [
+                "earth science",
+                "clouds",
+                "national geospatial data asset",
+                "ngda",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.5067/MEASURES/WVCC/DATA206",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2017-05-10",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
+            },
+            "release-place": "Greenbelt, MD, USA",
+            "series-name": "AIRS_MDS_IND",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2003-01-01T00:00:00Z/2022-01-17T00:00:00Z",
             "theme": [
                 "MEaSUREs",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Aqua AIRS-MODIS Matchup Indexes V1.0 (AIRS_MDS_IND) at GES_DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1658475777-OB_DAAC.html",
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
-                "name": "OB.DAAC"
-            },
-            "identifier": "C1658475777-OB_DAAC",
             "description": "The Visible and Infrared Imager/Radiometer Suite (VIIRS) is a multi-disciplinary instrument that is being flown on the Joint Polar Satellite System (JPSS) series of spacecraft, including the Suomi National Polar-orbiting Partnership (S-NPP) that launched in October 2011. JPSS is a multi-platform, multi-agency program that consolidates the polar orbiting spacecraft of NASA and the National Oceanic and Atmospheric Administration (NOAA). S-NPP is the initial spacecraft in this series, and VIIRS is the successor to MODIS for Earth science data product generation. VIIRS has 22 spectral bands ranging from 412 nm to 12 nm. There are 16 moderate-resolution bands (750m at nadir), 5 image-resolution bands (375m), and one day-night band (DNB).",
-            "title": "Suomi-NPP VIIRS Global Mapped 11\u00b5m Daytime Sea Surface Temperature (SST) Data, version 2016.2",
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
-                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/data/10.5067/NPP/VIIRS/L3M/SST/2016.2",
-                    "description": "VIIRS-Suomi-NPP L3M 11\u00b5m Daytime Sea Surface Temperature (SST) Dataset Landing Page",
                     "@type": "dcat:Distribution",
+                    "description": "VIIRS-Suomi-NPP L3M 11\u00b5m Daytime Sea Surface Temperature (SST) Dataset Landing Page",
+                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/data/10.5067/NPP/VIIRS/L3M/SST/2016.2",
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
+            "identifier": "C1658475777-OB_DAAC",
+            "issued": "2019-06-23",
+            "keyword": [
+                "ocean temperature",
+                "oceans",
+                "earth science"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1658475777-OB_DAAC.html",
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
+            "title": "Suomi-NPP VIIRS Global Mapped 11\u00b5m Daytime Sea Surface Temperature (SST) Data, version 2016.2"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MGS-M-MOLA-5-PEDR-SAMPLER-V1.0",
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
+            "description": "The MGS Sampler contains MOLA PEDR altimetry profiles in both binary andASCII formats. These ASCII tables contain calibrated MOLA ranges, energies, and topography for 18 contingency passes, Fall 1997. The tables have 29 columns, delimited by spaces. The tables contain radii, topography, areoid heights, spacecraft location, and instrument data. The information in these files is virtually identical to the binary PEDRs. The binary tables contain additional engineering data.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mgs-m-mola-5-pedr-sampler-v1.0_g448-cenu",
+            "issued": "2018-06-26",
+            "keyword": [
+                "mars global surveyor",
+                "mars"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MGS-M-MOLA-5-PEDR-SAMPLER-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mgs-m-mola-5-pedr-sampler-v1.0_g448-cenu",
-            "description": "The MGS Sampler contains MOLA PEDR altimetry profiles in both binary andASCII formats. These ASCII tables contain calibrated MOLA ranges, energies, and topography for 18 contingency passes, Fall 1997. The tables have 29 columns, delimited by spaces. The tables contain radii, topography, areoid heights, spacecraft location, and instrument data. The information in these files is virtually identical to the binary PEDRs. The binary tables contain additional engineering data.",
-            "title": "MGS SAMPLER MARS ORBITER LASER ALTIMETER PEDR ASCII TABLES",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "MGS SAMPLER MARS ORBITER LASER ALTIMETER PEDR ASCII TABLES"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=DAWN-A-FC2-3-RDR-CERES-IMAGES-V1.0",
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
+            "description": "Abstract                                                                   ========                                                                   Framing Camera 2 is one of two identical units flying on Dawn            spacecraft. This dataset includes the Reduced Data Record (RDR) version  of all available images acquired during the Ceres Encounter (Approach,   Survey, HAMO, and LAMO and the Ceres extended mission phases (XMO1-4).   In addition to the imagery, anciliary information is stored within the   image headers, as well as a detailed account of all the reference files  used for the calibration. Calibration files used during processing are   archived as a separate data set.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.dawn-a-fc2-3-rdr-ceres-images-v1.0_g454-4fxj",
+            "issued": "2021-05-21",
+            "keyword": [
+                "1 ceres",
+                "dawn mission to vesta and ceres"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=DAWN-A-FC2-3-RDR-CERES-IMAGES-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.dawn-a-fc2-3-rdr-ceres-images-v1.0_g454-4fxj",
-            "description": "Abstract                                                                   ========                                                                   Framing Camera 2 is one of two identical units flying on Dawn            spacecraft. This dataset includes the Reduced Data Record (RDR) version  of all available images acquired during the Ceres Encounter (Approach,   Survey, HAMO, and LAMO and the Ceres extended mission phases (XMO1-4).   In addition to the imagery, anciliary information is stored within the   image headers, as well as a detailed account of all the reference files  used for the calibration. Calibration files used during processing are   archived as a separate data set.",
-            "title": "DAWN FC2 CALIBRATED CERES IMAGES V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "DAWN FC2 CALIBRATED CERES IMAGES V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://spotthestation.nasa.gov",
+            "accrualPeriodicity": "R/P1D",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2021-06-10",
-            "temporal": "2021-06-10T00:00:00Z/P1D",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-31",
-            "keyword": [
-                "ephemeris",
-                "trajectory",
-                "topo",
-                "station",
-                "space",
-                "location",
-                "iss",
-                "international",
-                "coords",
-                "coordinates"
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
-            "identifier": "nasa-iss-data_2021-06-10_g458-8baj",
+            "dataQuality": true,
             "description": "This data represents the best estimated real-time trajectory and local sightings opportunities for the International Space Station (ISS) as generated by the Trajectory Operations and Planning (TOPO) flight controllers at Johnson Space Center.",
-            "title": "ISS_COORDS_2021-06-10",
-            "programCode": [
-                "026:004"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -794382,164 +794358,197 @@
                     "title": "XMLsightingData_natparksUSA02"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "nasa-iss-data_2021-06-10_g458-8baj",
+            "issued": "2021-06-10",
+            "keyword": [
+                "ephemeris",
+                "trajectory",
+                "topo",
+                "station",
+                "space",
+                "location",
+                "iss",
+                "international",
+                "coords",
+                "coordinates"
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
+            "temporal": "2021-06-10T00:00:00Z/P1D",
             "theme": [
                 "Space Science"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "ISS_COORDS_2021-06-10"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/GPMGV/WFF/MULTIPLE/DATA101",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Petersen, Walter A.2021. GPM Ground Validation Validation Network (VN) [indicate subset used]. Dataset available online from the NASA Global Hydrometeorology Resource Center DAAC, Huntsville, Alabama, U.S.A. DOI: http://dx.doi.org/10.5067/GPMGV/WFF/MULTIPLE/DATA101",
-            "issued": "2021-09-23",
-            "temporal": "2014-03-09T08:25:43Z/2021-07-31T23:12:32Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-05-23",
-            "keyword": [
-                "earth science",
-                "atmosphere",
-                "radar",
-                "precipitation",
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
-            "identifier": "C1995579435-GHRC_DAAC",
             "description": "The GPM Ground Validation Validation Network (VN) dataset contains reflectivity, hydrometeor identification, rain rate, correlation coefficient, and quality control variables and estimates. This data product was created using the Validation Network (VN), which performs a direct match-up of the Global Precipitation Mission (GPM)\u2019s space-based Dual-frequency Precipitation Radar (DPR) and Microwave Imager (GMI) data with ground radar data from NOAA Weather Surveillance Radar-1988 Doppler (WSR-88D) radars. These data are available from March 9, 2014 through July 31, 2021 in netCDF-3 format, though it should be noted that this dataset will be updated periodically.",
-            "title": "GPM Ground Validation Validation Network (VN) V1",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGPMGV%2FWFF%2FMULTIPLE%2FDATA101",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGPMGV%2FWFF%2FMULTIPLE%2FDATA101",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=gpmvn",
-                    "description": "Files may be downloaded directly to your workstation from this link",
                     "@type": "dcat:Distribution",
+                    "description": "Files may be downloaded directly to your workstation from this link",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=gpmvn",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/relatedProjects/vn/doc/gpmvn_dataset.pdf",
-                    "description": "The guide document contains detailed information about the dataset",
                     "@type": "dcat:Distribution",
+                    "description": "The guide document contains detailed information about the dataset",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/relatedProjects/vn/doc/gpmvn_dataset.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/relatedProjects/vn/doc/Val_Network_Users_Guide_Vol_2.pdf",
-                    "description": "GPM Ground Validation System Validation Network Data Product User's Guide",
                     "@type": "dcat:Distribution",
+                    "description": "GPM Ground Validation System Validation Network Data Product User's Guide",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/relatedProjects/vn/doc/Val_Network_Users_Guide_Vol_2.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View the primary investigator's documentation for this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.1175/1520-0426(2001)018%3C0616:TUOTPR%3E2.0.CO;2",
-                    "description": "The Use of TRMM Precipitation Radar Observations in Determining Ground Radar Calibration Biases",
                     "@type": "dcat:Distribution",
+                    "description": "The Use of TRMM Precipitation Radar Observations in Determining Ground Radar Calibration Biases",
+                    "downloadURL": "https://doi.org/10.1175/1520-0426(2001)018%3C0616:TUOTPR%3E2.0.CO;2",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.1175/1520-0450(2001)040%3C2071:QCVOSB%3E2.0.CO;2",
-                    "description": "Quantitative Cross Validation of Space-Based and Ground-Based Radar Observations",
                     "@type": "dcat:Distribution",
+                    "description": "Quantitative Cross Validation of Space-Based and Ground-Based Radar Observations",
+                    "downloadURL": "https://doi.org/10.1175/1520-0450(2001)040%3C2071:QCVOSB%3E2.0.CO;2",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.1175/2010JTECHA1403.1",
-                    "description": "A Ground Validation Network for the Global Precipitation Measurement Mission",
                     "@type": "dcat:Distribution",
+                    "description": "A Ground Validation Network for the Global Precipitation Measurement Mission",
+                    "downloadURL": "https://doi.org/10.1175/2010JTECHA1403.1",
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
+            "identifier": "C1995579435-GHRC_DAAC",
+            "issued": "2021-09-23",
+            "keyword": [
+                "earth science",
+                "atmosphere",
+                "radar",
+                "precipitation",
+                "spectral/engineering"
+            ],
+            "landingPage": "https://doi.org/10.5067/GPMGV/WFF/MULTIPLE/DATA101",
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
             "spatial": "-169.499 -31.818 169.948 65.634",
+            "temporal": "2014-03-09T08:25:43Z/2021-07-31T23:12:32Z",
             "theme": [
                 "NOT APPLICABLE",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "GPM Ground Validation Validation Network (VN) V1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-2CP-3-RDR-ECAS-MEAN-V1.0",
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
+            "description": "The eight color asteroid survey provides reflection spectra for minor planets using eight filter passbands. This dataset includes mean data averaged for each of 589 minor planets. The primary data for these minor planets, the response curves for the filters, and the values determined for standard stars, are included in other related datasets. The wavelength range covered is .33 to 1.04 micrometers.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-2cp-3-rdr-ecas-mean-v1.0_g49q-s2wb",
+            "issued": "2018-06-26",
+            "keyword": [
+                "support archives",
+                "asteroid"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-2CP-3-RDR-ECAS-MEAN-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-2cp-3-rdr-ecas-mean-v1.0_g49q-s2wb",
-            "description": "The eight color asteroid survey provides reflection spectra for minor planets using eight filter passbands. This dataset includes mean data averaged for each of 589 minor planets. The primary data for these minor planets, the response curves for the filters, and the values determined for standard stars, are included in other related datasets. The wavelength range covered is .33 to 1.04 micrometers.",
-            "title": "EIGHT COLOR ASTEROID SURVEY MEAN DATA V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "EIGHT COLOR ASTEROID SURVEY MEAN DATA V1.0"
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
+            "description": "ISS, RADAR, RPWS, RSS, SPICE, UVIS, VIMS",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://pds.jpl.nasa.gov/tools/subscription_service/SS-20120103.shtml",
+                    "mediaType": "application/html"
+                }
             ],
+            "identifier": "NASA-520",
+            "issued": "2018-06-25",
             "keyword": [
                 "uvis",
                 "radar",
@@ -794550,120 +794559,125 @@
                 "rss",
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
-            "identifier": "NASA-520",
-            "description": "ISS, RADAR, RPWS, RSS, SPICE, UVIS, VIMS",
-            "title": "PDS Cassini Data Release 28",
-            "programCode": [
-                "026:005"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://pds.jpl.nasa.gov/tools/subscription_service/SS-20120103.shtml",
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
+            "title": "PDS Cassini Data Release 28"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-3-RDR-OCCULTATIONS-V12.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This data set is intended to include all reported timings of observed asteroid, planet, and planetary satellite occultation events as well as occultation axes derived from those timings by David W. Dunham and David Herald. This version is complete through January 2014.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-3-rdr-occultations-v12.0_g4e6-v3ey",
             "issued": "2021-05-21",
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
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-3-RDR-OCCULTATIONS-V12.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-3-rdr-occultations-v12.0_g4e6-v3ey",
-            "description": "This data set is intended to include all reported timings of observed asteroid, planet, and planetary satellite occultation events as well as occultation axes derived from those timings by David W. Dunham and David Herald. This version is complete through January 2014.",
-            "title": "ASTEROID OCCULTATIONS V12.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ASTEROID OCCULTATIONS V12.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://c3.nasa.gov/dashlink/resources/805/",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2013-07-23",
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
-            "identifier": "DASHLINK_805",
             "description": "This paper presents a distributed Bayesian fault diagnosis scheme for physical systems. Our diagnoser design is based on a procedure for factoring the global system bond graph (BG) into a set of structurally observable bond graph fac- tors (BG-Fs). Each BG-F is systematically translated into a corresponding DBN Factor (DBN-F), which is then used in its corresponding local diagnoser for quantitative fault detec- tion, isolation, and identification. By construction, the ran- dom variables in each DBN-F are conditionally independent of the random variables in all other DBN-Fs, given a subset of communicated measurements considered as system inputs. Each DBN-F and BG-F pair is used to derive a local diag- noser that generates globally correct diagnosis results by lo- cal analysis. Together, the local diagnosers diagnose all single faults of interest in the system. We demonstrate on an electri- cal system how our distributed diagnosis scheme is compu- tationally more efficient than its centralized counterpart, but without compromising the accuracy of the diagnosis results.",
-            "title": "Distributed Diagnosis in Uncertain Environments Using Dynamic Bayesian Networks",
-            "programCode": [
-                "026:029"
-            ],
             "distribution": [
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/publication/2010_ICBGM_DistrDiagDactoredBGs.pdf",
-                    "description": "2010_ICBGM_DistrDiagDactoredBGs.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "2010_ICBGM_DistrDiagDactoredBGs.pdf",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/publication/2010_ICBGM_DistrDiagDactoredBGs.pdf",
+                    "mediaType": "application/pdf",
                     "title": "2010_ICBGM_DistrDiagDactoredBGs.pdf"
                 }
             ],
-            "accrualPeriodicity": "irregular"
+            "identifier": "DASHLINK_805",
+            "issued": "2013-07-23",
+            "keyword": [
+                "nasa",
+                "dashlink",
+                "ames"
+            ],
+            "landingPage": "https://c3.nasa.gov/dashlink/resources/805/",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:029"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Dashlink"
+            },
+            "title": "Distributed Diagnosis in Uncertain Environments Using Dynamic Bayesian Networks"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.nasa.gov/d/g4gi-jv2m",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "GeneLab Outreach",
+                "hasEmail": "mailto:genelab-outreach@lists.nasa.gov"
+            },
+            "description": "This is a genome-wide approach to identifying genes persistently induced in the mouse mammary gland by acute whole body low dose ionizing radiation (10cGy) 1 and 4 weeks after exposure. Gene expression that is modified under these parameters were compared between Tgfb1 wild type and heterozygote littermates in order to determine which genes induced or repressed by radiation were mediated via Tgfb1 status. Differential gene expression was analyzed in Tgfb1 heterozygote and wild type littermate 4th mammary glands after whole body exposure to an acute dose of 10cGy ionizing radiation. Estrus cycle was normalized in all mice two days prior to irradiation by injection with an estrogen and progesterone mixture. It is widely believed that the carcinogenic action of ionizing radiation is due to targeted DNA damage and resulting mutations but there is also substantial evidence that non-targeted radiation effects alter epithelial phenotype and the stromal microenvironment. Activation of transforming growth factor beta 1 (TGFbeta) is a non-targeted radiation effect that mediates cell fate decisions following DNA damage and regulates microenvironment composition; it could either suppress or promote cancer. Gene expression profiling shown herein demonstrates that low dose radiation (10 cGy) elicits persistent changes in Tgfb1 wild type and heterozygote murine mammary gland that are highly modulated by TGFbeta. We asked if such non-targeted radiation effects contribute to carcinogenesis by using a novel radiation chimera model. Unirradiated Trp53 null mammary epithelium was transplanted to the mammary stroma of mice previously exposed to a single low (10 -100 cGy) radiation dose. By 300 days 100% of transplants in irradiated hosts at either 10 or 100 cGy had developed Trp53 null breast carcinomas compared to 54% in unirradiated hosts. Tumor growth rate was also increased by high but not low dose host irradiation. In contrast irradiation of Tgfb1 heterozygote mice prior to transplantation failed to decrease tumor latency or increase growth rate at any dose. Host irradiation significantly reduced the latency of invasive ductal carcinoma compared to spindle cell carcinoma as well as those tumors negative for smooth muscle actin in wild type but not Tgfb1 heterozygote mice. However irradiation of either host genotype significantly increased the frequency of estrogen receptor negative tumors. These data demonstrate two concepts critical to understanding radiation risks. First non-targeted radiation effects can significantly promote the frequency and alter the features of epithelial cancer. Second radiation-induced TGFbeta activity is a key mechanism of tumor promotion. Keywords: Differential gene expression after low dose irradiation Two genotypes: TGBbeta1 heterozygote and wildtype mouse mammary glands. Two time points post-10cGy-irradiation per genotype (1 week 4 weeks); control time point was 1 week post-sham-irradiation. Two or three replicates per time point.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "GeneLab Study Page",
+                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-153",
+                    "mediaType": "text/html",
+                    "title": "Non-targeted effects of low dose ionizing radiation act via TGF-beta to promote mammary carcinogenesis"
+                }
+            ],
+            "identifier": "nasa_genelab_GLDS-153_g4gi-jv2m",
             "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
             "keyword": [
                 "labeling",
                 "nucleic_acid_extraction",
@@ -794685,846 +794699,811 @@
                 "p-gse18216-7",
                 "p-gse18216-6"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "GeneLab Outreach",
-                "hasEmail": "mailto:genelab-outreach@lists.nasa.gov"
-            },
+            "landingPage": "https://data.nasa.gov/d/g4gi-jv2m",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "nasa_genelab_GLDS-153_g4gi-jv2m",
-            "description": "This is a genome-wide approach to identifying genes persistently induced in the mouse mammary gland by acute whole body low dose ionizing radiation (10cGy) 1 and 4 weeks after exposure. Gene expression that is modified under these parameters were compared between Tgfb1 wild type and heterozygote littermates in order to determine which genes induced or repressed by radiation were mediated via Tgfb1 status. Differential gene expression was analyzed in Tgfb1 heterozygote and wild type littermate 4th mammary glands after whole body exposure to an acute dose of 10cGy ionizing radiation. Estrus cycle was normalized in all mice two days prior to irradiation by injection with an estrogen and progesterone mixture. It is widely believed that the carcinogenic action of ionizing radiation is due to targeted DNA damage and resulting mutations but there is also substantial evidence that non-targeted radiation effects alter epithelial phenotype and the stromal microenvironment. Activation of transforming growth factor beta 1 (TGFbeta) is a non-targeted radiation effect that mediates cell fate decisions following DNA damage and regulates microenvironment composition; it could either suppress or promote cancer. Gene expression profiling shown herein demonstrates that low dose radiation (10 cGy) elicits persistent changes in Tgfb1 wild type and heterozygote murine mammary gland that are highly modulated by TGFbeta. We asked if such non-targeted radiation effects contribute to carcinogenesis by using a novel radiation chimera model. Unirradiated Trp53 null mammary epithelium was transplanted to the mammary stroma of mice previously exposed to a single low (10 -100 cGy) radiation dose. By 300 days 100% of transplants in irradiated hosts at either 10 or 100 cGy had developed Trp53 null breast carcinomas compared to 54% in unirradiated hosts. Tumor growth rate was also increased by high but not low dose host irradiation. In contrast irradiation of Tgfb1 heterozygote mice prior to transplantation failed to decrease tumor latency or increase growth rate at any dose. Host irradiation significantly reduced the latency of invasive ductal carcinoma compared to spindle cell carcinoma as well as those tumors negative for smooth muscle actin in wild type but not Tgfb1 heterozygote mice. However irradiation of either host genotype significantly increased the frequency of estrogen receptor negative tumors. These data demonstrate two concepts critical to understanding radiation risks. First non-targeted radiation effects can significantly promote the frequency and alter the features of epithelial cancer. Second radiation-induced TGFbeta activity is a key mechanism of tumor promotion. Keywords: Differential gene expression after low dose irradiation Two genotypes: TGBbeta1 heterozygote and wildtype mouse mammary glands. Two time points post-10cGy-irradiation per genotype (1 week 4 weeks); control time point was 1 week post-sham-irradiation. Two or three replicates per time point.",
-            "title": "Non-targeted effects of low dose ionizing radiation act via TGF-beta to promote mammary carcinogenesis",
-            "programCode": [
-                "026:005"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-153",
-                    "description": "GeneLab Study Page",
-                    "@type": "dcat:Distribution",
-                    "title": "Non-targeted effects of low dose ionizing radiation act via TGF-beta to promote mammary carcinogenesis"
-                }
-            ],
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "Non-targeted effects of low dose ionizing radiation act via TGF-beta to promote mammary carcinogenesis"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=IHW-C-ASTR-2-EDR-GZ-V1.0",
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
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ihw-c-astr-2-edr-gz-v1.0_g4gt-qzx7",
+            "issued": "2018-06-26",
+            "keyword": [
+                "halley",
+                "international halley watch"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=IHW-C-ASTR-2-EDR-GZ-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ihw-c-astr-2-edr-gz-v1.0_g4gt-qzx7",
-            "description": "In preparation for the concerted international study of Comet Halley, the IHW conducted a trial run with observations of Comet Crommelin, largely during February and March of 1984.",
-            "title": "IHW COMET ASTR EDITED EXPERIMENT DATA RECORD GZ V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "IHW COMET ASTR EDITED EXPERIMENT DATA RECORD GZ V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/GWYQTF307Y9Y",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "SMAP L1B Radiometer Half-Orbit Time-Ordered Brightness Temperatures V006. Version 006. Archived by National Aeronautics and Space Administration, U.S. Government, NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/GWYQTF307Y9Y.",
-            "issued": "2015-03-31",
-            "temporal": "2015-03-31T00:00:00Z/2025-01-13T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-08",
-            "keyword": [
-                "spectral/engineering",
-                "earth science",
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
-            "identifier": "C2938661904-NSIDC_CPRD",
             "description": "This Level-1B (L1B) product provides calibrated estimates of time-ordered geolocated brightness temperatures measured by the Soil Moisture Active Passive (SMAP) passive microwave radiometer. SMAP L-band brightness temperatures are referenced to the Earth's surface with undesired and erroneous radiometric sources removed.",
-            "graphic-preview-description": "This application allows you to interactively browse global satellite imagery within hours of it being acquired. You can also save it, share it, and download the underlying data.",
-            "title": "SMAP L1B Radiometer Half-Orbit Time-Ordered Brightness Temperatures V006",
-            "graphic-preview-file": "https://worldview.earthdata.nasa.gov/?v=-186,-77,170,87&l=SMAP_L1_Passive_Faraday_Rotation_Fore,SMAP_L1_Passive_Faraday_Rotation_Aft,Coastlines_15m,MODIS_Terra_CorrectedReflectance_TrueColor",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGWYQTF307Y9Y",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGWYQTF307Y9Y",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=SPL1BTB+V006",
-                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=SPL1BTB+V006",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2938661904-NSIDC_CPRD",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2938661904-NSIDC_CPRD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://worldview.earthdata.nasa.gov/?v=-186%2C-77%2C170%2C87&l=SMAP_L1_Passive_Faraday_Rotation_Fore%2CSMAP_L1_Passive_Faraday_Rotation_Aft%2CCoastlines_15m%2CMODIS_Terra_CorrectedReflectance_TrueColor",
-                    "description": "This application allows you to interactively browse global satellite imagery within hours of it being acquired. You can also save it, share it, and download the underlying data.",
                     "@type": "dcat:Distribution",
+                    "description": "This application allows you to interactively browse global satellite imagery within hours of it being acquired. You can also save it, share it, and download the underlying data.",
+                    "downloadURL": "https://worldview.earthdata.nasa.gov/?v=-186%2C-77%2C170%2C87&l=SMAP_L1_Passive_Faraday_Rotation_Fore%2CSMAP_L1_Passive_Faraday_Rotation_Aft%2CCoastlines_15m%2CMODIS_Terra_CorrectedReflectance_TrueColor",
+                    "mediaType": "text/html",
                     "title": "Get a related visualization through WORLDVIEW"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/GWYQTF307Y9Y",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/GWYQTF307Y9Y",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/GWYQTF307Y9Y",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/GWYQTF307Y9Y",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "graphic-preview-description": "This application allows you to interactively browse global satellite imagery within hours of it being acquired. You can also save it, share it, and download the underlying data.",
+            "graphic-preview-file": "https://worldview.earthdata.nasa.gov/?v=-186,-77,170,87&l=SMAP_L1_Passive_Faraday_Rotation_Fore,SMAP_L1_Passive_Faraday_Rotation_Aft,Coastlines_15m,MODIS_Terra_CorrectedReflectance_TrueColor",
+            "identifier": "C2938661904-NSIDC_CPRD",
+            "issued": "2015-03-31",
+            "keyword": [
+                "spectral/engineering",
+                "earth science",
+                "microwave"
+            ],
+            "landingPage": "https://doi.org/10.5067/GWYQTF307Y9Y",
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
             "spatial": "-180.0 -86.4 180.0 86.4",
+            "temporal": "2015-03-31T00:00:00Z/2025-01-13T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "SMAP L1B Radiometer Half-Orbit Time-Ordered Brightness Temperatures V006"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RL-A-ROMAP-3-AST1-MAG-V1.0",
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
-                "2867 steins",
-                "international rosetta mission"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This archive contains calibrated data from the ROMAP-MAG instrument onboard ROSETTA Lander, acquired during the AST1 (Steins fly-by) phase. It also contains documentation which describes the ROMAP experiment. The data archived in this data set conform to the Planetary Data System (PDS) Standards, Version 3.6.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.rl-a-romap-3-ast1-mag-v1.0_g4im-e977",
+            "issued": "2021-05-21",
+            "keyword": [
+                "2867 steins",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RL-A-ROMAP-3-AST1-MAG-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.rl-a-romap-3-ast1-mag-v1.0_g4im-e977",
-            "description": "This archive contains calibrated data from the ROMAP-MAG instrument onboard ROSETTA Lander, acquired during the AST1 (Steins fly-by) phase. It also contains documentation which describes the ROMAP experiment. The data archived in this data set conform to the Planetary Data System (PDS) Standards, Version 3.6.",
-            "title": "ROSETTA-LANDER STEINS ROMAP 3 AST1 MAG\n                            V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-LANDER STEINS ROMAP 3 AST1 MAG\n                            V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=P11-J-SW-UV-4-SUMM-1DAY-V1.0",
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
-                "jupiter",
-                "pioneer 11"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "Pioneer 11 ultraviolet photometer 1 day data.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.p11-j-sw-uv-4-summ-1day-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "jupiter",
+                "pioneer 11"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=P11-J-SW-UV-4-SUMM-1DAY-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.p11-j-sw-uv-4-summ-1day-v1.0",
-            "description": "Pioneer 11 ultraviolet photometer 1 day data.",
-            "title": "P11 JUPITER SW UV SUMMARY 1 DAY",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "P11 JUPITER SW UV SUMMARY 1 DAY"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC1-0617-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 1 phase 2014-11-20 to 2015-03-10. It is a Global Gravity measurement at the comet 67P and covers the time 2015-03-02T14:28:35.000 to 2015-03-02T22:01:01.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc1-0617-v1.0_g4rg-nzvt",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC1-0617-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc1-0617-v1.0_g4rg-nzvt",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 1 phase 2014-11-20 to 2015-03-10. It is a Global Gravity measurement at the comet 67P and covers the time 2015-03-02T14:28:35.000 to 2015-03-02T22:01:01.000.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 1 0617 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 1 0617 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-EXT1-1383-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the ROSETTA EXTENSION 1 phase 2016-01-01 to 2016-04-05. It is a Global Gravity measurement at the comet 67P and covers the time 2016-01-30T09:18:20.000 to 2016-01-30T13:08:18.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-ext1-1383-v1.0_g4s5-r3vb",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-EXT1-1383-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-ext1-1383-v1.0_g4s5-r3vb",
-            "description": "This is a Rosetta Radio Science data set, collected during the ROSETTA EXTENSION 1 phase 2016-01-01 to 2016-04-05. It is a Global Gravity measurement at the comet 67P and covers the time 2016-01-30T09:18:20.000 to 2016-01-30T13:08:18.000.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     ROSETTA EXTENSION 1 1383 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     ROSETTA EXTENSION 1 1383 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/NAMMA/PROBES/DATA201",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Heymsfield, Andrew J and Aaron  Bansemer.2006. NAMMA CLOUD MICROPHYSICS (CAPS-PIP) [indicate subset used]. Dataset available online from the NASA Global Hydrometeorology Resource Center DAAC, Huntsville, Alabama, U.S.A. DOI: http://dx.doi.org/10.5067/NAMMA/PROBES/DATA201",
-            "issued": "2006-06-01",
-            "temporal": "2006-08-19T13:32:00Z/2006-09-12T19:47:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-05-19",
-            "keyword": [
-                "precipitation",
-                "atmosphere",
-                "earth science",
-                "clouds",
-                "aerosols"
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
-            "identifier": "C1979885294-GHRC_DAAC",
             "description": "The NAMMA Cloud Microphysics (CAPS-PIP) dataset consists of particle size distributions from the Clouds, Aerosol and Preciptaition Spectrometer (CAPS) and the Precipitaiton Imaging Probe (PIP) from August 19, 2006 to September 12, 2006. These instruments yield precipitation, hydrometeor and aerosol sizes ranging from 0.55 - 100 microns. Data is in the form of images and ascii tables. These data files were generated during support of the NASA African Monsoon Multidisciplinary Analyses (NAMMA) campaign, a field research investigation sponsored by the Science Mission Directorate of the National Aeronautics and Space Administration (NASA). This mission was based in the Cape Verde Islands, 350 miles off the coast of Senegal in west Africa. Commencing in August 2006, NASA scientists employed surface observation networks and aircraft to characterize the evolution and structure of African Easterly Waves (AEWs) and Mesoscale Convective Systems over continental western Africa, and their associated impacts on regional water and energy budgets.",
-            "graphic-preview-description": "N/A",
-            "title": "NAMMA CLOUD MICROPHYSICS (CAPS-PIP) V1",
-            "graphic-preview-file": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/namma/CAPS-PIP/browse/",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FNAMMA%2FPROBES%2FDATA201",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FNAMMA%2FPROBES%2FDATA201",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=namcaps",
-                    "description": "Files may be downloaded directly to your workstation from this link",
                     "@type": "dcat:Distribution",
+                    "description": "Files may be downloaded directly to your workstation from this link",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=namcaps",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/namma/CAPS-PIP/browse/2006-08-19/namma_caps_20060819_165500_CIP10.png",
-                    "description": "Sample browse image",
                     "@type": "dcat:Distribution",
+                    "description": "Sample browse image",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/namma/CAPS-PIP/browse/2006-08-19/namma_caps_20060819_165500_CIP10.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/namma/CAPS-PIP/browse/2006-08-19/namma_caps_20060819_165500_PIP.png",
-                    "description": "Sample browse image",
                     "@type": "dcat:Distribution",
+                    "description": "Sample browse image",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/namma/CAPS-PIP/browse/2006-08-19/namma_caps_20060819_165500_PIP.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://ghrc.nsstc.nasa.gov/uso/ds_docs/namma/namcaps/namcaps_dataset.html",
-                    "description": "The guide document contains detailed information about the dataset",
                     "@type": "dcat:Distribution",
+                    "description": "The guide document contains detailed information about the dataset",
+                    "downloadURL": "http://ghrc.nsstc.nasa.gov/uso/ds_docs/namma/namcaps/namcaps_dataset.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/doc/namma/namcaps/NAMMA_Cloud_Microphysics_readme.txt",
-                    "description": "NAMMA Cloud Microphysics",
                     "@type": "dcat:Distribution",
+                    "description": "NAMMA Cloud Microphysics",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/doc/namma/namcaps/NAMMA_Cloud_Microphysics_readme.txt",
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
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/namma/CAPS-PIP/browse/",
-                    "description": "N/A",
                     "@type": "dcat:Distribution",
+                    "description": "N/A",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/namma/CAPS-PIP/browse/",
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
+            "graphic-preview-file": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/namma/CAPS-PIP/browse/",
+            "identifier": "C1979885294-GHRC_DAAC",
+            "issued": "2006-06-01",
+            "keyword": [
+                "precipitation",
+                "atmosphere",
+                "earth science",
+                "clouds",
+                "aerosols"
+            ],
+            "landingPage": "https://doi.org/10.5067/NAMMA/PROBES/DATA201",
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
             "spatial": "-34.1533 7.03833 -10.5583 21.0483",
+            "temporal": "2006-08-19T13:32:00Z/2006-09-12T19:47:00Z",
             "theme": [
                 "NAMMA",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "NAMMA CLOUD MICROPHYSICS (CAPS-PIP) V1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=PVO-V-ONMS-4-IONMAXCOUNTRATE-12SEC-V1.0",
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
-                "pioneer venus"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This data set represents the maximum count rate per second in a 12 second period beginning with the time of the first data point for a given mass number. Although species other than O+ cannot be reduced to to a flux and direction it is possible to estimate the approximate flux from the maximum count rate per second occurring within one spin period (about 12 seconds). The maximum count rate can be approximately converted to a flux using: [4.E7 (particles/cm**2/sec)]/[1.E4 (counts/sec)]. This sensitivity is for O+. At higher mass numbers the sensitivity is less, being about a factor of 2.5 lower for Ar+.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.pvo-v-onms-4-ionmaxcountrate-12sec-v1.0_g4um-wwmk",
+            "issued": "2021-05-21",
+            "keyword": [
+                "venus",
+                "pioneer venus"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=PVO-V-ONMS-4-IONMAXCOUNTRATE-12SEC-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.pvo-v-onms-4-ionmaxcountrate-12sec-v1.0_g4um-wwmk",
-            "description": "This data set represents the maximum count rate per second in a 12 second period beginning with the time of the first data point for a given mass number. Although species other than O+ cannot be reduced to to a flux and direction it is possible to estimate the approximate flux from the maximum count rate per second occurring within one spin period (about 12 seconds). The maximum count rate can be approximately converted to a flux using: [4.E7 (particles/cm**2/sec)]/[1.E4 (counts/sec)]. This sensitivity is for O+. At higher mass numbers the sensitivity is less, being about a factor of 2.5 lower for Ar+.",
-            "title": "PVO VENUS ONMS BROWSE SUPRTHRML ION MAX COUNT RATE 12S V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "PVO VENUS ONMS BROWSE SUPRTHRML ION MAX COUNT RATE 12S V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/IMPACTS/NEXRAD/DATA112",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Brodzik, Stacy .2022. KENX NEXRAD IMPACTS [indicate subset used]. Dataset available online from the NASA Global Hydrometeorology Resource Center DAAC, Huntsville, Alabama, U.S.A. DOI: http://dx.doi.org/10.5067/IMPACTS/NEXRAD/DATA112",
-            "issued": "2022-03-23",
-            "temporal": "2020-01-01T00:02:13Z/2020-03-01T00:00:32Z",
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
-            "identifier": "C2025220226-GHRC_DAAC",
             "description": "The KENX NEXRAD IMPACTS dataset consists of Next Generation Weather Radar (NEXRAD) Level II surveillance data that were collected at 31 NEXRAD sites from January 1 to March 1, 2020 during the Investigation of Microphysics and Precipitation for Atlantic Coast-Threatening Snowstorms  (IMPACTS) field campaign. IMPACTS was a three-year sequence of winter season deployments conducted to study snowstorms over the U.S Atlantic Coast. The campaign aimed to (1) Provide observations critical to understanding the mechanisms of snowband formation, organization, and evolution; (2) Examine how the microphysical characteristics and likely growth mechanisms of snow particles vary across snowbands; and (3) Improve snowfall remote sensing interpretation and modeling to significantly advance prediction capabilities. There are currently 160 Weather Surveillance Radar-1988 Doppler (WSR-88D) or NEXRAD sites throughout the United States and abroad. These Level II datasets contain meteorological and dual-polarization base data quantities including: radar reflectivity, radial velocity, spectrum width, differential reflectivity, differential phase, and cross correlation ratio. The IMPACTS NEXRAD Level II data files are available in netCDF-4 format. It should be noted that this dataset will be updated in subsequent years of the IMPACTS campaign.",
-            "title": "KENX NEXRAD IMPACTS V1",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FIMPACTS%2FNEXRAD%2FDATA112",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FIMPACTS%2FNEXRAD%2FDATA112",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=kenximpacts",
-                    "description": "Files may be downloaded directly to your workstation from this link",
                     "@type": "dcat:Distribution",
+                    "description": "Files may be downloaded directly to your workstation from this link",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=kenximpacts",
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
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/impacts/NEXRAD/KENX/doc/nexrad_datasets.pdf",
-                    "description": "NEXRAD IMPACTS User Guide",
                     "@type": "dcat:Distribution",
+                    "description": "NEXRAD IMPACTS User Guide",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/impacts/NEXRAD/KENX/doc/nexrad_datasets.pdf",
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
+            "identifier": "C2025220226-GHRC_DAAC",
+            "issued": "2022-03-23",
+            "keyword": [
+                "radar",
+                "spectral/engineering",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/IMPACTS/NEXRAD/DATA112",
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
             "spatial": "-79.677 38.457 -68.451 46.716",
+            "temporal": "2020-01-01T00:02:13Z/2020-03-01T00:00:32Z",
             "theme": [
                 "IMPACTS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "KENX NEXRAD IMPACTS V1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=JNO-E%2FJ%2FSS-WAV-2-EDR-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "The Juno Waves EDR complete data set includes all Waves science and housekeeping data for the entire Juno mission.  This data set consists of reformatted, uncalibrated, spectra and waveforms as well as unaltered housekeeping packets.  The reformatting operation re-assembles measurements which were too long to fit with in a single transmission unit to the Juno flight data system as well as decompressing data that were transmitted in compressed form.  The data for this set were acquired from the Waves Low Frequency Receiver (LFR), High Frequency Receivers (HFR-44, HFR-45), as well as the Digital Signal Processor's housekeeping output.  This data set is intended to preserve the uncalibrated instrument packets and is to be used only as a last resort. Other Waves archived data sets are designed to be complete and more easily used.  Browse images associated with the other data sets provide a graphical search of the data included in this data set.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.jno-e-j-ss-wav-2-edr-v1.0_g526-k7hh",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "solar system",
                 "earth",
                 "jupiter",
                 "juno"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=JNO-E%2FJ%2FSS-WAV-2-EDR-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.jno-e-j-ss-wav-2-edr-v1.0_g526-k7hh",
-            "description": "The Juno Waves EDR complete data set includes all Waves science and housekeeping data for the entire Juno mission.  This data set consists of reformatted, uncalibrated, spectra and waveforms as well as unaltered housekeeping packets.  The reformatting operation re-assembles measurements which were too long to fit with in a single transmission unit to the Juno flight data system as well as decompressing data that were transmitted in compressed form.  The data for this set were acquired from the Waves Low Frequency Receiver (LFR), High Frequency Receivers (HFR-44, HFR-45), as well as the Digital Signal Processor's housekeeping output.  This data set is intended to preserve the uncalibrated instrument packets and is to be used only as a last resort. Other Waves archived data sets are designed to be complete and more easily used.  Browse images associated with the other data sets provide a graphical search of the data included in this data set.",
-            "title": "JUNO E/J/S/SS WAVES EXPERIMENT DATA RECORDS V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "JUNO E/J/S/SS WAVES EXPERIMENT DATA RECORDS V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=PHX-M-RAC-3-RADIOMETRIC-SCI-V1.0",
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
+            "description": "The Robotic Arm Camera (RAC) experiment on the Mars Phoenix Lander consists of one instrument component plus command electronics. This RAC Imaging Science RDR data set contains radiometric data from the Robotic Arm Camera (RAC).",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.phx-m-rac-3-radiometric-sci-v1.0_g52d-dew8",
+            "issued": "2018-06-26",
+            "keyword": [
+                "mars",
+                "phoenix"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=PHX-M-RAC-3-RADIOMETRIC-SCI-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.phx-m-rac-3-radiometric-sci-v1.0_g52d-dew8",
-            "description": "The Robotic Arm Camera (RAC) experiment on the Mars Phoenix Lander consists of one instrument component plus command electronics. This RAC Imaging Science RDR data set contains radiometric data from the Robotic Arm Camera (RAC).",
-            "title": "PHOENIX MARS ROBOTIC ARM CAMERA 3 RADIOMETRIC SCI V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "PHOENIX MARS ROBOTIC ARM CAMERA 3 RADIOMETRIC SCI V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=P10-J-CRT-4-SUMM-FLUX-15MIN-V1.0",
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
-                "pioneer 10"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "Pioneer 10 Cosmic-ray telescope (CRT) data from the Jupiter encounter period, covering 1973-11-26 to 1973-12-15. The data set provides 15.0 minute flux averages from 18 electron, proton, and heavy ion channels.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.p10-j-crt-4-summ-flux-15min-v1.0_g52p-exvs",
+            "issued": "2021-05-21",
+            "keyword": [
+                "jupiter",
+                "pioneer 10"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=P10-J-CRT-4-SUMM-FLUX-15MIN-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.p10-j-crt-4-summ-flux-15min-v1.0_g52p-exvs",
-            "description": "Pioneer 10 Cosmic-ray telescope (CRT) data from the Jupiter encounter period, covering 1973-11-26 to 1973-12-15. The data set provides 15.0 minute flux averages from 18 electron, proton, and heavy ion channels.",
-            "title": "P10 JUPITER CRT ELECTRON/PROTON/ION\n                                      FLUX 15 MIN AVGS V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "P10 JUPITER CRT ELECTRON/PROTON/ION\n                                      FLUX 15 MIN AVGS V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ATLAS/ATL21.003",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "ATLAS/ICESat-2 L3B Daily and Monthly Gridded Polar Sea Surface Height Anomaly V003. Version 003. Archived by National Aeronautics and Space Administration, U.S. Government, NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/ATLAS/ATL21.003.",
-            "issued": "2018-10-14",
-            "temporal": "2018-10-14T00:00:00Z/2024-10-07T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-07-31",
-            "keyword": [
-                "earth science",
-                "oceans",
-                "sea surface topography"
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
-            "identifier": "C2737912334-NSIDC_ECS",
             "description": "ATL21 contains daily and monthly gridded polar sea surface height (SSH) anomalies, derived from the along-track ATLAS/ICESat-2 L3A Sea Ice Height product (ATL10, V6). The ATL10 product identifies leads in sea ice and establishes a reference sea surface used to estimate SSH in 10 km along-track segments. ATL21 aggregates the ATL10 along-track SSH estimates and computes daily and monthly gridded SSH anomaly in NSIDC Polar Stereographic Northern and Southern Hemisphere 25 km grids.",
-            "title": "ATLAS/ICESat-2 L3B Daily and Monthly Gridded Polar Sea Surface Height Anomaly V003",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FATLAS%2FATL21.003",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FATLAS%2FATL21.003",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/ATLAS/ATL21.003/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/ATLAS/ATL21.003/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/data/data-access-tool/ATL21/versions/3/",
-                    "description": "Search and filter data files using a map-based interface",
                     "@type": "dcat:Distribution",
+                    "description": "Search and filter data files using a map-based interface",
+                    "downloadURL": "https://nsidc.org/data/data-access-tool/ATL21/versions/3/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=ATL21+V003",
-                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=ATL21+V003",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/ATLAS/ATL21.003",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/ATLAS/ATL21.003",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/ATLAS/ATL21.003",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/ATLAS/ATL21.003",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C2737912334-NSIDC_ECS",
+            "issued": "2018-10-14",
+            "keyword": [
+                "earth science",
+                "oceans",
+                "sea surface topography"
+            ],
+            "landingPage": "https://doi.org/10.5067/ATLAS/ATL21.003",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2024-07-31",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA NSIDC DAAC"
+            },
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2018-10-14T00:00:00Z/2024-10-07T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "ATLAS/ICESat-2 L3B Daily and Monthly Gridded Polar Sea Surface Height Anomaly V003"
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
-                "themis",
-                "spice",
-                "grs",
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
-            "identifier": "NASA-672",
             "description": "GRS, THEMIS, SPICE",
-            "title": "PDS Odyssey Data Release 27",
-            "programCode": [
-                "026:005"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -795532,485 +795511,517 @@
                     "mediaType": "application/html"
                 }
             ],
-            "accrualPeriodicity": "irregular",
+            "identifier": "NASA-672",
+            "issued": "2018-06-25",
+            "keyword": [
+                "themis",
+                "spice",
+                "grs",
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
+            "title": "PDS Odyssey Data Release 27"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/893",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Asner, G.P., M.M. Keller, R.J.R. Pereira, and J.C. Zweede. 2008. LBA-ECO LC-13 GIS Coverages of Logged Areas, Tapajos Forest, Para, Brazil: 1996, 1998. ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/893",
-            "issued": "2023-10-03",
-            "temporal": "1996-01-01T00:00:00Z/1998-12-31T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-10-04",
-            "keyword": [
-                "biosphere",
-                "earth science",
-                "vegetation",
-                "land surface",
-                "landscape",
-                "human dimensions",
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
-            "identifier": "C2777400780-ORNL_CLOUD",
             "description": "This data set contains GIS coverages constructed from measurements taken of logged areas in the Tapajos National Forest region of Para, Brazil in 1996 and 1998 (Asner et al., 2004). Coverages include log decks (patios), roads, skids trails, tree-fall locations, and block boundary. They are in ArcInfo SHAPE format (*.shp). The Tapajos data are in latitude/longitude using the WGS84 datum.",
-            "graphic-preview-description": "Browse Image",
-            "title": "LBA-ECO LC-13 GIS Coverages of Logged Areas, Tapajos Forest, Para, Brazil: 1996, 1998",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/lba_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F893",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F893",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/lba/land_use_land_cover_change/LC13_GIS_Tapajos/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/lba/land_use_land_cover_change/LC13_GIS_Tapajos/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/LBA/guides/LC13_GIS_Tapajos.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/LBA/guides/LC13_GIS_Tapajos.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/893",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/893",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC13_GIS_Tapajos/comp/LC13_GIS_Tapajos.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC13_GIS_Tapajos/comp/LC13_GIS_Tapajos.pdf",
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
+            "identifier": "C2777400780-ORNL_CLOUD",
+            "issued": "2023-10-03",
+            "keyword": [
+                "biosphere",
+                "earth science",
+                "vegetation",
+                "land surface",
+                "landscape",
+                "human dimensions",
+                "habitat conversion/fragmentation"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/893",
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
             "spatial": "-56.0 -3.5 -54.0 -2.25",
+            "temporal": "1996-01-01T00:00:00Z/1998-12-31T23:59:59Z",
             "theme": [
                 "LBA-ECO",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "LBA-ECO LC-13 GIS Coverages of Logged Areas, Tapajos Forest, Para, Brazil: 1996, 1998"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/TERRA/MISR/RICMIRCM_L1B3.004",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "The data used in this study were produced by the MISR Science Team; processed/stored at the Langley DAAC; MISR L1B3 Radiometric Camera-by-camera Cloud Mask Product subset for the RICO region; See ProductionDateTime for Published date.",
-            "issued": "2017-08-07",
-            "temporal": "2000-11-01T14:36:42Z/2005-01-31T15:19:32Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-04-26",
-            "keyword": [
-                "atmosphere",
-                "clouds",
-                "earth science"
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
-            "identifier": "C1411142650-LARC",
             "description": "This file contains the Radiometric camera-by-camera Cloud Mask dataset over the RICO region. It is used to determine whether a scene is classified as clear or cloudy. A new parameter has been added to indicate dust over ocean. This version of the ESDT is used by MISR PGE 13.",
-            "title": "MISR L1B3 Radiometric Camera-by-camera Cloud Mask Product subset for the RICO region V004",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FTERRA%2FMISR%2FRICMIRCM_L1B3.004",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FTERRA%2FMISR%2FRICMIRCM_L1B3.004",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 }
             ],
+            "identifier": "C1411142650-LARC",
+            "issued": "2017-08-07",
+            "keyword": [
+                "atmosphere",
+                "clouds",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/TERRA/MISR/RICMIRCM_L1B3.004",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2022-04-26",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/LARC/SD/ASDC"
+            },
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2000-11-01T14:36:42Z/2005-01-31T15:19:32Z",
             "theme": [
                 "RICO_2004",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "MISR L1B3 Radiometric Camera-by-camera Cloud Mask Product subset for the RICO region V004"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/182",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Hall, F. G., K. F. Huemmrich, D. E. Strebel, S. J. Goetz, J. E. Nickeson, and K. D. Woods. 1996. SNF Forest Understory Cover Data (Table). [Superior National Forest Forest Understory Cover Data (Table)]. Data set. Available on-line [http://www.daac.ornl.gov] from Oak Ridge National Laboratory Distributed Active Archive Center, Oak Ridge, Tennessee, U.S.A. Based on F. G. Hall, K. F. Huemmrich, D. E. Strebel, S. J. Goetz, J. E. Nickeson, and K. D. Woods, Biophysical, Morphological, Canopy Optical Property, and Productivity Data from the Superior National Forest, NASA Technical Memorandum 104568, National Aeronautics and Space Administration, Goddard Space Flight Center, Greenbelt, Maryland, U.S.A., 1992. doi:10.3334/ORNLDAAC/182",
-            "issued": "2024-03-02",
-            "temporal": "1976-01-01T00:00:00Z/1986-12-31T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-03-04",
-            "keyword": [
-                "vegetation",
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
-            "identifier": "C2884983060-ORNL_CLOUD",
             "description": "SNF study location measurements of percent ground coverage provided by each understory species; percentages are averages of five 2-meter-diameter subsamples in each site (presented in table format)",
-            "graphic-preview-description": "Browse Image",
-            "title": "SNF Forest Understory Cover Data (Table)",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/snf_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F182",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F182",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/snf/SNF_TAB3_3T/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/snf/SNF_TAB3_3T/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/SNF/guides/forest_understory_cover_table.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/SNF/guides/forest_understory_cover_table.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/182",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/182",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/snf/SNF_TAB3_3T/comp/forest_understory_cover_table.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/snf/SNF_TAB3_3T/comp/forest_understory_cover_table.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/snf/SNF_TAB3_3T/comp/forest_understory_cover_table.txt",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/snf/SNF_TAB3_3T/comp/forest_understory_cover_table.txt",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/snf/SNF_TAB3_3T/comp/tab3_3t.def",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/snf/SNF_TAB3_3T/comp/tab3_3t.def",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/snf/SNF_TAB3_3T/comp/tab3_3t.txt",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/snf/SNF_TAB3_3T/comp/tab3_3t.txt",
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
+            "identifier": "C2884983060-ORNL_CLOUD",
+            "issued": "2024-03-02",
+            "keyword": [
+                "vegetation",
+                "earth science",
+                "biosphere"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/182",
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
+            "temporal": "1976-01-01T00:00:00Z/1986-12-31T23:59:59Z",
             "theme": [
                 "SNF",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "SNF Forest Understory Cover Data (Table)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-3-ESC3-67PCHURYUMOV-M19-V2.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This data set contains images acquired by the OSIRIS Wide Angle Camera during the COMET ESCORT 3 phase of the Rosetta mission at the comet 67P, covering the period from 2015-07-28T23:25:00.000 to 2015-08-25T23:24:59.000. This version V2.0 supersedes previous deliveries of the same dataset.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-3-esc3-67pchuryumov-m19-v2.0_g59b-vcxg",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "international rosetta mission",
                 "zeta cas",
                 "67p/churyumov-gerasimenko 1 (1969 r1)"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-3-ESC3-67PCHURYUMOV-M19-V2.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-3-esc3-67pchuryumov-m19-v2.0_g59b-vcxg",
-            "description": "This data set contains images acquired by the OSIRIS Wide Angle Camera during the COMET ESCORT 3 phase of the Rosetta mission at the comet 67P, covering the period from 2015-07-28T23:25:00.000 to 2015-08-25T23:24:59.000. This version V2.0 supersedes previous deliveries of the same dataset.",
-            "title": "ROSETTA-ORBITER COMET ESCORT 3 OSIWAC 3 RDR MTP019 V2.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER COMET ESCORT 3 OSIWAC 3 RDR MTP019 V2.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/TWDAYANXT8UM",
             "citation": "Miyazaki, Kazuyuki. 2024-02-06. TRPSCRAERSO46H3D. Version 1. TROPESS Chemical Reanalysis Aerosol SO4 6-Hourly 3-dimensional Product V1. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/TWDAYANXT8UM. https://disc.gsfc.nasa.gov/datacollection/TRPSCRAERSO46H3D_1.html. Digital Science Data.",
-            "issued": "2023-01-09",
-            "temporal": "2005-01-01T00:00:00Z/2024-02-12T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-09",
-            "references": [
-                "https://doi.org/10.1126/sciadv.abf7460"
-            ],
-            "keyword": [
-                "aerosols",
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
-            "identifier": "C2837624898-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "The TROPESS Chemical Reanalysis Surface Aerosol SO4 6-Hourly 3-dimensional Product contains vertical concentrations of sulfate aerosols. The data are part of the Tropospheric Chemical Reanalysis v2 (TCR-2) for the period 2005-2021. TCR-2 uses JPL's Multi-mOdel Multi-cOnstituent Chemical (MOMO-Chem) data assimilation framework that simultaneously optimizes both concentrations and emissions of multiple species from multiple satellite sensors.\n\nThe data files are written in the netCDF version 4 file format, and each file contains a year of data at 6-hourly resolution, and a spatial resolution of 1.125 x 1.125 degrees at 27 pressure levels between 1000 and 60 hPa. The principal investigator for the TCR-2 data is Miyazaki, Kazuyuki.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "TRPSCRAERSO46H3D",
-            "creator": "Miyazaki, Kazuyuki",
-            "graphic-preview-description": "TROPESS CrIS-SNPP Los Angeles Megacity (Forward Stream, Summary Product) at 681 hPa on 01 April 2021.",
-            "title": "TROPESS Chemical Reanalysis Aerosol SO4 6-Hourly 3-dimensional Product V1 (TRPSCRAERSO46H3D) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TROPESS/images/TRPSCRAERSO46H3D_Sample.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FTWDAYANXT8UM",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FTWDAYANXT8UM",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TROPESS/images/TRPSCRAERSO46H3D_Sample.png",
-                    "description": "TROPESS CrIS-SNPP Los Angeles Megacity (Forward Stream, Summary Product) at 681 hPa on 01 April 2021.",
                     "@type": "dcat:Distribution",
+                    "description": "TROPESS CrIS-SNPP Los Angeles Megacity (Forward Stream, Summary Product) at 681 hPa on 01 April 2021.",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TROPESS/images/TRPSCRAERSO46H3D_Sample.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/TRPSCRAERSO46H3D_1.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/TRPSCRAERSO46H3D_1.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/data/TCR2_6HR_VERTCONCS/TRPSCRAERSO46H3D.1/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/data/TCR2_6HR_VERTCONCS/TRPSCRAERSO46H3D.1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=TRPSCRAERSO46H3D_1",
-                    "description": "Use the Earthdata Search Client to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search Client to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=TRPSCRAERSO46H3D_1",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/opendap/TCR2_6HR_VERTCONCS/TRPSCRAERSO46H3D.1/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/opendap/TCR2_6HR_VERTCONCS/TRPSCRAERSO46H3D.1/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/data/TCR2_6HR_VERTCONCS/TRPSCRAERSO46H3D.1/doc/TROPESS_ChemReanalysis_Forward_Stream_README.pdf",
-                    "description": "README Document",
                     "@type": "dcat:Distribution",
+                    "description": "README Document",
+                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/data/TCR2_6HR_VERTCONCS/TRPSCRAERSO46H3D.1/doc/TROPESS_ChemReanalysis_Forward_Stream_README.pdf",
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
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TROPESS/images/TRPSCRAERSO46H3D_Sample.png",
+            "identifier": "C2837624898-GES_DISC",
+            "issued": "2023-01-09",
+            "keyword": [
+                "aerosols",
+                "atmosphere",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/TWDAYANXT8UM",
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
+            "series-name": "TRPSCRAERSO46H3D",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2005-01-01T00:00:00Z/2024-02-12T00:00:00Z",
             "theme": [
                 "TROPESS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "TROPESS Chemical Reanalysis Aerosol SO4 6-Hourly 3-dimensional Product V1 (TRPSCRAERSO46H3D) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MSL-M-SAM-2-RDR-L0-V1.0",
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
+            "description": "TBD (one or two paragraph summary)",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.msl-m-sam-2-rdr-l0-v1.0_g5ds-2f7s",
+            "issued": "2018-06-26",
+            "keyword": [
+                "mars science laboratory",
+                "mars"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MSL-M-SAM-2-RDR-L0-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.msl-m-sam-2-rdr-l0-v1.0_g5ds-2f7s",
-            "description": "TBD (one or two paragraph summary)",
-            "title": "MSL MARS SAMPLE ANALYSIS AT MARS 2 RDR LEVEL 0 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "MSL MARS SAMPLE ANALYSIS AT MARS 2 RDR LEVEL 0 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=CO-SSA-RADAR-5-BIDR-V1.0",
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
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.co-ssa-radar-5-bidr-v1.0_g5fs-8tka",
+            "issued": "2021-05-21",
+            "keyword": [
+                "cassini-huygens",
+                "titan"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=CO-SSA-RADAR-5-BIDR-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.co-ssa-radar-5-bidr-v1.0_g5fs-8tka",
-            "description": "N/A",
-            "title": "CASSINI ORBITER SSA RADAR 5 BIDR V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "CASSINI ORBITER SSA RADAR 5 BIDR V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.nasa.gov/d/g5hr-j3ar",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "PHIL NEWMAN",
+                "hasEmail": "mailto:panewman@lheapop.gsfc.nasa.gov"
+            },
+            "description": "The High Energy Astrophysics Science Archive Research Center (HEASARC) is the primary archive for NASA missions dealing with extremely energetic phenomena, from black holes to the Big Bang.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://heasarc.gsfc.nasa.gov/xamin/xamin.jsp",
+                    "mediaType": "text/html"
+                }
+            ],
+            "identifier": "NASA-0000053",
             "issued": "2018-06-25",
-            "temporal": "1969-01-01/2006-01-01",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
             "keyword": [
                 "thesaurus",
                 "cosmology",
@@ -796052,220 +796063,187 @@
                 "wmap",
                 "xmm-newton"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "PHIL NEWMAN",
-                "hasEmail": "mailto:panewman@lheapop.gsfc.nasa.gov"
-            },
+            "landingPage": "https://data.nasa.gov/d/g5hr-j3ar",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "NASA-0000053",
-            "description": "The High Energy Astrophysics Science Archive Research Center (HEASARC) is the primary archive for NASA missions dealing with extremely energetic phenomena, from black holes to the Big Bang.",
-            "title": "High Energy Astrophysics Science Archive Research Center",
-            "programCode": [
-                "026:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://heasarc.gsfc.nasa.gov/xamin/xamin.jsp",
-                    "mediaType": "text/html"
-                }
-            ],
-            "accrualPeriodicity": "irregular"
+            "temporal": "1969-01-01/2006-01-01",
+            "title": "High Energy Astrophysics Science Archive Research Center"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-E-RPCMAG-2-EAR3-RAW-V3.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This dataset contains EDITED RAW DATA of the third Earth Swingby (EAR3). The closest approach (CA) took place on November 13, 2009 at 07:45. Additionally data from the Payload Chekcout PC10 are added.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-e-rpcmag-2-ear3-raw-v3.0_g5i5-fzvn",
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
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-E-RPCMAG-2-EAR3-RAW-V3.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-e-rpcmag-2-ear3-raw-v3.0_g5i5-fzvn",
-            "description": "This dataset contains EDITED RAW DATA of the third Earth Swingby (EAR3). The closest approach (CA) took place on November 13, 2009 at 07:45. Additionally data from the Payload Chekcout PC10 are added.",
-            "title": "ROSETTA-ORBITER EARTH RPCMAG 2 EAR3 RAW V3.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "ROSETTA-ORBITER EARTH RPCMAG 2 EAR3 RAW V3.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/GHSEV-3CO01",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "EUMETSAT/OSI SAF. 2015-05-29. SEVIRI Atlantic SST. Version 1. GHRSST Level 3C Atlantic Sea Surface Sub-Skin Temperature from the Spinning Enhanced Visible and Infrared Imager (SEVIRI) on MSG. EUMETSAT Ocean and Sea Ice Satellite Application Facility, Lannion, France. Archived by National Aeronautics and Space Administration, U.S. Government, PO.DAAC. https://doi.org/10.5067/GHSEV-3CO01. https://osi-saf.eumetsat.int/. EUMETSAT/OSI SAF, EUMETSAT Ocean and Sea Ice Satellite Application Facility, Meteo-France/CMS, Lannion, France, 2015-05-29, GHRSST Level 3C Atlantic sub-skin Sea Surface Temperature from the Spinning Enhanced Visible and Infrared Imager (SEVIRI) on MSG at 0 degree longitude (GDS V2) produced by OSI SAF, www.osi-saf.org.",
-            "issued": "2015-03-18",
-            "temporal": "2004-06-01T00:00:00Z/2023-02-28T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2017-04-28",
-            "keyword": [
-                "earth science",
-                "oceans",
-                "ocean temperature"
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
-            "identifier": "C2036878243-POCLOUD",
-            "description": "A Group for High Resolution Sea Surface Temperature (GHRSST) dataset for the Eastern Atlantic Region from the Spinning Enhanced Visible and InfraRed Imager (SEVIRI) on the Meteosat Second Generation (MSG-3) satellites (launched 5 July 2012). \r\n\r\nThe European Organization for the Exploitation of Meteorological Satellites (EUMETSAT),\r\nOcean and Sea Ice Satellite Application Facility (OSI SAF) is producing SST products in near real\r\ntime from MSG/SEVIRI. SEVIRI level 1.5 data are acquired at Meteo-France/Centre de\r\nMeteorologie Spatiale (CMS) through the EUMETSAT/EUMETCAST system. SST is retrieved\r\nfrom the SEVIRI infrared channels (10.8 and 12.0 micrometer) using a multispectral algorithm.\r\nAtmospheric profiles of water vapor and temperature from a numerical weather prediction model,\r\ntogether with a radiatiave transfer model, are used to correct the multispectral algorithm for\r\nregional and seasonal biases due to changing atmospheric conditions. Every 15 minutes slot is\r\nprocessed at full satellite resolution. The operational products are then produced by remapping\r\nover a 0.05 degree regular grid (60S-60N and 60W-60E) SST fields obtained by aggregating all 15\r\nminute SST data available in one hour time, and the priority being given to the value the closest in\r\ntime to the product nominal hour. The product format is compliant with the GHRSST Data\r\nSpecification (GDS) version 2.",
-            "release-place": "EUMETSAT Ocean and Sea Ice Satellite Application Facility, Lannion, France",
-            "series-name": "SEVIRI Atlantic SST",
-            "graphic-preview-description": "Thumbnail",
             "creator": "EUMETSAT/OSI SAF",
-            "title": "GHRSST Level 3C Atlantic sub-skin Sea Surface Temperature from the Spinning Enhanced Visible and Infrared Imager (SEVIRI) on MSG at 0 degree longitude (GDS V2) produced by OSI SAF",
-            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/SEVIRI_SST-OSISAF-L3C-v1.0.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "A Group for High Resolution Sea Surface Temperature (GHRSST) dataset for the Eastern Atlantic Region from the Spinning Enhanced Visible and InfraRed Imager (SEVIRI) on the Meteosat Second Generation (MSG-3) satellites (launched 5 July 2012). \r\n\r\nThe European Organization for the Exploitation of Meteorological Satellites (EUMETSAT),\r\nOcean and Sea Ice Satellite Application Facility (OSI SAF) is producing SST products in near real\r\ntime from MSG/SEVIRI. SEVIRI level 1.5 data are acquired at Meteo-France/Centre de\r\nMeteorologie Spatiale (CMS) through the EUMETSAT/EUMETCAST system. SST is retrieved\r\nfrom the SEVIRI infrared channels (10.8 and 12.0 micrometer) using a multispectral algorithm.\r\nAtmospheric profiles of water vapor and temperature from a numerical weather prediction model,\r\ntogether with a radiatiave transfer model, are used to correct the multispectral algorithm for\r\nregional and seasonal biases due to changing atmospheric conditions. Every 15 minutes slot is\r\nprocessed at full satellite resolution. The operational products are then produced by remapping\r\nover a 0.05 degree regular grid (60S-60N and 60W-60E) SST fields obtained by aggregating all 15\r\nminute SST data available in one hour time, and the priority being given to the value the closest in\r\ntime to the product nominal hour. The product format is compliant with the GHRSST Data\r\nSpecification (GDS) version 2.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGHSEV-3CO01",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGHSEV-3CO01",
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
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/SEVIRI_SST-OSISAF-L3C-v1.0.jpg",
-                    "description": "Thumbnail",
                     "@type": "dcat:Distribution",
+                    "description": "Thumbnail",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/SEVIRI_SST-OSISAF-L3C-v1.0.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://osi-saf.eumetsat.int/lml/doc/osisaf_cdop3_ss1_pum_geo_sst.pdf",
-                    "description": "Product User Manual",
                     "@type": "dcat:Distribution",
+                    "description": "Product User Manual",
+                    "downloadURL": "https://osi-saf.eumetsat.int/lml/doc/osisaf_cdop3_ss1_pum_geo_sst.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View information related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ghrsst.jpl.nasa.gov",
-                    "description": "GHRSST Information",
                     "@type": "dcat:Distribution",
+                    "description": "GHRSST Information",
+                    "downloadURL": "https://ghrsst.jpl.nasa.gov",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.ghrsst.org",
-                    "description": "GHRSST Project",
                     "@type": "dcat:Distribution",
+                    "description": "GHRSST Project",
+                    "downloadURL": "https://www.ghrsst.org",
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
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2036878243-POCLOUD",
-                    "description": "HTTPS endpoint for data browse and download",
                     "@type": "dcat:Distribution",
+                    "description": "HTTPS endpoint for data browse and download",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2036878243-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2036878243-POCLOUD",
-                    "description": "Browse granule search results in Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse granule search results in Earthdata Search",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2036878243-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://osi-saf.eumetsat.int/lml/doc/osisaf_cdop2_ss1_geo_sst_val_rep.pdf",
-                    "description": "Scientific Validation Report",
                     "@type": "dcat:Distribution",
+                    "description": "Scientific Validation Report",
+                    "downloadURL": "https://osi-saf.eumetsat.int/lml/doc/osisaf_cdop2_ss1_geo_sst_val_rep.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's science data product validation documentation"
                 }
             ],
+            "graphic-preview-description": "Thumbnail",
+            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/SEVIRI_SST-OSISAF-L3C-v1.0.jpg",
+            "identifier": "C2036878243-POCLOUD",
+            "issued": "2015-03-18",
+            "keyword": [
+                "earth science",
+                "oceans",
+                "ocean temperature"
+            ],
+            "landingPage": "https://doi.org/10.5067/GHSEV-3CO01",
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
+            "release-place": "EUMETSAT Ocean and Sea Ice Satellite Application Facility, Lannion, France",
+            "series-name": "SEVIRI Atlantic SST",
             "spatial": "-60.0 -60.0 60.0 60.0",
+            "temporal": "2004-06-01T00:00:00Z/2023-02-28T00:00:00Z",
             "theme": [
                 "GHRSST",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "GHRSST Level 3C Atlantic sub-skin Sea Surface Temperature from the Spinning Enhanced Visible and Infrared Imager (SEVIRI) on MSG at 0 degree longitude (GDS V2) produced by OSI SAF"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1273652184-GES_DISC.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Donald F. Heath, et al.. 1977-03-12. BUVN4L1PDB. Version 001. BUV/Nimbus-4 Level 1 Radiance and Housekeeping Data in Telemetry Units V001. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://disc.gsfc.nasa.gov/datacollection/BUVN4L1PDB_001.html. Digital Science Data.",
-            "issued": "2015-12-03",
-            "temporal": "1970-04-10T00:00:00Z/1977-05-06T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2015-12-03",
-            "keyword": [
-                "ultraviolet wavelengths",
-                "earth science",
-                "spectral/engineering"
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
-            "identifier": "C1273652184-GES_DISC",
-            "description": "The Nimbus-4 BUV Level-1 Radiance and Housekeeping Data in Telemetry Units collection contains the raw counts measured by the Backscatter Ultraviolet Spectrometer every 32 seconds at 12 wavelengths between 250 and 340 nm during the daylit orbit portion. The data collection also contains ephemeris data, experiment subsystem status information, and spacecraft housekeeping and orbit data. This data collection was used to create the Level 1 Radiance U-Tape or RUT product.\n\nThe data were originally created on IBM 360 machines and archived on magnetic tapes. The data have been restored from the tapes and are now archived on disk in their original IBM binary file format. Each file contains about one orbit of data. The data files consist of 850 2-byte word records which are blocked in up to ten records. The first record in the file is the header record, followed by a series of data records, and ends with a trailer record. A typical orbit file is about 260 kB in size.\n\nThe BUV instrument was operational from April 10, 1970 until May 6, 1977. In July 1972 the Nimbus-4 solar power array partially failed such that BUV operations were curtailed. Thus data collected in the later years was increasingly sparse, particularly in the equatorial region.\n\nThis product was previously available from the NSSDC with the identifier ESAC-00024 (old ID 70-025A-05E).",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "BUVN4L1PDB",
             "creator": "Donald F. Heath, et al.",
-            "title": "BUV/Nimbus-4 Level 1 Radiance and Housekeeping Data in Telemetry Units V001 (BUVN4L1PDB) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/BUVN4L1PDB_001.png",
-            "programCode": [
-                "026:001"
-            ],
+            "data-presentation-form": "Digital Science Data",
+            "description": "The Nimbus-4 BUV Level-1 Radiance and Housekeeping Data in Telemetry Units collection contains the raw counts measured by the Backscatter Ultraviolet Spectrometer every 32 seconds at 12 wavelengths between 250 and 340 nm during the daylit orbit portion. The data collection also contains ephemeris data, experiment subsystem status information, and spacecraft housekeeping and orbit data. This data collection was used to create the Level 1 Radiance U-Tape or RUT product.\n\nThe data were originally created on IBM 360 machines and archived on magnetic tapes. The data have been restored from the tapes and are now archived on disk in their original IBM binary file format. Each file contains about one orbit of data. The data files consist of 850 2-byte word records which are blocked in up to ten records. The first record in the file is the header record, followed by a series of data records, and ends with a trailer record. A typical orbit file is about 260 kB in size.\n\nThe BUV instrument was operational from April 10, 1970 until May 6, 1977. In July 1972 the Nimbus-4 solar power array partially failed such that BUV operations were curtailed. Thus data collected in the later years was increasingly sparse, particularly in the equatorial region.\n\nThis product was previously available from the NSSDC with the identifier ESAC-00024 (old ID 70-025A-05E).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -796274,351 +796252,375 @@
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/BUVN4L1PDB_001.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/BUVN4L1PDB_001.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/Nimbus4_BUV_Level1/BUVN4L1PDB.001/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/Nimbus4_BUV_Level1/BUVN4L1PDB.001/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=BUVN4L1PDB",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=BUVN4L1PDB",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/Nimbus4_BUV_Level1/BUVN4L1PDB.001/doc/README.BUVN4L1PDB.001.pdf",
-                    "description": "README Document",
                     "@type": "dcat:Distribution",
+                    "description": "README Document",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/Nimbus4_BUV_Level1/BUVN4L1PDB.001/doc/README.BUVN4L1PDB.001.pdf",
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
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/BUVN4L1PDB_001.png",
+            "identifier": "C1273652184-GES_DISC",
+            "issued": "2015-12-03",
+            "keyword": [
+                "ultraviolet wavelengths",
+                "earth science",
+                "spectral/engineering"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1273652184-GES_DISC.html",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2015-12-03",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
+            },
+            "release-place": "Greenbelt, MD, USA",
+            "series-name": "BUVN4L1PDB",
             "spatial": "-180.0 -80.1 180.0 80.1",
+            "temporal": "1970-04-10T00:00:00Z/1977-05-06T23:59:59.999Z",
             "theme": [
                 "Nimbus",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "BUV/Nimbus-4 Level 1 Radiance and Housekeeping Data in Telemetry Units V001 (BUVN4L1PDB) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/MODIS/MCD43D12.061",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Crystal Schaaf, Zhuosen Wang. 2021-02-22. MODIS/Terra+Aqua BRDF/Albedo Parameter3 Band4 Daily L3 Global 30ArcSec CMG V061. Sioux Falls, South Dakota, USA. Archived by National Aeronautics and Space Administration, U.S. Government, NASA EOSDIS Land Processes Distributed Active Archive Center. https://doi.org/10.5067/MODIS/MCD43D12.061. https://doi.org/10.5067/MODIS/MCD43D12.061. The DOI landing page provides citations in APA and Chicago styles..",
-            "issued": "2021-02-22",
-            "temporal": "2000-02-16T00:00:00Z/2024-05-20T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2021-02-22",
-            "keyword": [
-                "earth science",
-                "ngda",
-                "land surface",
-                "surface radiative properties",
-                "national geospatial data asset"
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
-            "identifier": "C2539907890-LPCLOUD",
-            "description": "The MCD43D12 Version 6.1 Bidirectional Reflectance Distribution Function and Albedo (BRDF/Albedo) Model Parameter dataset is produced daily using 16 days of Terra and Aqua Moderate Resolution Imaging Spectroradiometer (MODIS) data at 30 arc second (1,000 meter) resolution. Data are temporally weighted to the ninth day which is reflected in the Julian date in the file name. This Climate Modeling Grid (CMG) product covers the entire globe for use in climate simulation models. Due to the large file size, each MCD43D product contains just one data layer. Each of the three model parameters (isotropic, volumetric, and geometric) for each of the MODIS bands 1 through 7 and the visible, near infrared (NIR), and shortwave bands included in MCD43C1 (https://doi.org/10.5067/MODIS/MCD43C1.061) are stored in a separate file as MCD43D01 through MCD43D30. \r\n\r\nMCD43D12 is the BRDF geometric parameter for MODIS band 4. The geometric parameter, in conjunction with the isotropic and volumetric parameters, is used to derive the BRDF/Albedo values for MODIS band 4. \r\n\r\nImprovements/Changes from Previous Versions\r\n\r\n* The Version 6.1 Level-1B (L1B) products have been improved by undergoing various calibration changes that include: changes to the response-versus-scan angle (RVS) approach that affects reflectance bands for Aqua and Terra MODIS, corrections to adjust for the optical crosstalk in Terra MODIS infrared (IR) bands, and corrections to the Terra MODIS forward look-up table (LUT) update for the period 2012 - 2017.\r\n* A polarization correction has been applied to the L1B Reflective Solar Bands (RSB).",
-            "release-place": "Sioux Falls, South Dakota, USA",
             "creator": "Crystal Schaaf, Zhuosen Wang",
-            "title": "MODIS/Terra+Aqua BRDF/Albedo Parameter3 Band4 Daily L3 Global 30ArcSec CMG V061",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The MCD43D12 Version 6.1 Bidirectional Reflectance Distribution Function and Albedo (BRDF/Albedo) Model Parameter dataset is produced daily using 16 days of Terra and Aqua Moderate Resolution Imaging Spectroradiometer (MODIS) data at 30 arc second (1,000 meter) resolution. Data are temporally weighted to the ninth day which is reflected in the Julian date in the file name. This Climate Modeling Grid (CMG) product covers the entire globe for use in climate simulation models. Due to the large file size, each MCD43D product contains just one data layer. Each of the three model parameters (isotropic, volumetric, and geometric) for each of the MODIS bands 1 through 7 and the visible, near infrared (NIR), and shortwave bands included in MCD43C1 (https://doi.org/10.5067/MODIS/MCD43C1.061) are stored in a separate file as MCD43D01 through MCD43D30. \r\n\r\nMCD43D12 is the BRDF geometric parameter for MODIS band 4. The geometric parameter, in conjunction with the isotropic and volumetric parameters, is used to derive the BRDF/Albedo values for MODIS band 4. \r\n\r\nImprovements/Changes from Previous Versions\r\n\r\n* The Version 6.1 Level-1B (L1B) products have been improved by undergoing various calibration changes that include: changes to the response-versus-scan angle (RVS) approach that affects reflectance bands for Aqua and Terra MODIS, corrections to adjust for the optical crosstalk in Terra MODIS infrared (IR) bands, and corrections to the Terra MODIS forward look-up table (LUT) update for the period 2012 - 2017.\r\n* A polarization correction has been applied to the L1B Reflective Solar Bands (RSB).",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMODIS%2FMCD43D12.061",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMODIS%2FMCD43D12.061",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "application/x-hdf",
-                    "downloadURL": "https://e4ftl01.cr.usgs.gov/MOTA/MCD43D12.061/",
-                    "description": "LP DAAC Data Pool provides direct access to available products via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "LP DAAC Data Pool provides direct access to available products via HTTPS.",
+                    "downloadURL": "https://e4ftl01.cr.usgs.gov/MOTA/MCD43D12.061/",
+                    "mediaType": "application/x-hdf",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "application/x-hdf",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=C2539907890-LPCLOUD",
-                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=C2539907890-LPCLOUD",
+                    "mediaType": "application/x-hdf",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/MODIS/MCD43D12.061",
-                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
+                    "downloadURL": "https://doi.org/10.5067/MODIS/MCD43D12.061",
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
-                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/filespec/MODIS/61/MCD43D12",
-                    "description": "The File Specification provides a description of the product file including Scientific Data Sets and their attributes.",
                     "@type": "dcat:Distribution",
+                    "description": "The File Specification provides a description of the product file including Scientific Data Sets and their attributes.",
+                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/filespec/MODIS/61/MCD43D12",
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
-                    "downloadURL": "https://opendap.cr.usgs.gov/opendap/hyrax/DP137/MOTA/MCD43D12.061/contents.html",
-                    "description": "Access data via Open-source Project for a Network Data Access Protocol",
                     "@type": "dcat:Distribution",
+                    "description": "Access data via Open-source Project for a Network Data Access Protocol",
+                    "downloadURL": "https://opendap.cr.usgs.gov/opendap/hyrax/DP137/MOTA/MCD43D12.061/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 }
             ],
+            "identifier": "C2539907890-LPCLOUD",
+            "issued": "2021-02-22",
+            "keyword": [
+                "earth science",
+                "ngda",
+                "land surface",
+                "surface radiative properties",
+                "national geospatial data asset"
+            ],
+            "landingPage": "https://doi.org/10.5067/MODIS/MCD43D12.061",
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
+            "title": "MODIS/Terra+Aqua BRDF/Albedo Parameter3 Band4 Daily L3 Global 30ArcSec CMG V061"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/443",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Dye, D., and B.N. Holben. 1999. BOREAS RSS-10 TOMS Circumpolar One-Degree PAR Images. ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/443",
-            "issued": "2023-11-22",
-            "temporal": "1979-05-01T00:00:00Z/1989-09-30T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-04-11",
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
-            "identifier": "C2929112031-ORNL_CLOUD",
             "description": "The BOREAS RSS-10 team investigated the magnitude of daily, seasonal, and yearly variations of PAR from ground and satellite observations.  This data set contains satellite estimates of surface-incident photosynthetically active radiation (PAR, 400-700 nm, MJ m-2) at 1 degree spatial resolution. The spatial coverage is circumpolar from latitudes of 41 to 66 degrees N latitude.",
-            "graphic-preview-description": "Browse Image",
-            "title": "BOREAS RSS-10 TOMS Circumpolar One-Degree PAR Images",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/boreas_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F443",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F443",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/boreas/RSS/rss10tom/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/boreas/RSS/rss10tom/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/BOREAS/guides/RSS10_PAR_TOMS.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/BOREAS/guides/RSS10_PAR_TOMS.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/443",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/443",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/RSS/rss10tom/comp/README",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/RSS/rss10tom/comp/README",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/msword",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/RSS/rss10tom/comp/RSS10_PAR_TOMS.doc",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/RSS/rss10tom/comp/RSS10_PAR_TOMS.doc",
+                    "mediaType": "application/msword",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/RSS/rss10tom/comp/RSS10_PAR_TOMS.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/RSS/rss10tom/comp/RSS10_PAR_TOMS.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/RSS/rss10tom/comp/RSS10_PAR_TOMS.txt",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/RSS/rss10tom/comp/RSS10_PAR_TOMS.txt",
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
+            "identifier": "C2929112031-ORNL_CLOUD",
+            "issued": "2023-11-22",
+            "keyword": [
+                "vegetation",
+                "biosphere",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/443",
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
             "spatial": "-180.0 41.5 180.0 65.5",
+            "temporal": "1979-05-01T00:00:00Z/1989-09-30T23:59:59Z",
             "theme": [
                 "BOREAS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "BOREAS RSS-10 TOMS Circumpolar One-Degree PAR Images"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=CO-SS-RSS-1-SCC8-V1.0",
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
-                "solar system"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "The Cassini Radio Science Solar Corona Characterization Experiment (SCC8) Raw Data Archive is a time-ordered collection of radio science raw data acquired from September 27 to September 30, 2011, during the Cassini Extended Mission.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.co-ss-rss-1-scc8-v1.0_g5qn-6gnv",
+            "issued": "2021-05-21",
+            "keyword": [
+                "cassini-huygens",
+                "solar system"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=CO-SS-RSS-1-SCC8-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.co-ss-rss-1-scc8-v1.0_g5qn-6gnv",
-            "description": "The Cassini Radio Science Solar Corona Characterization Experiment (SCC8) Raw Data Archive is a time-ordered collection of radio science raw data acquired from September 27 to September 30, 2011, during the Cassini Extended Mission.",
-            "title": "CASSINI RSS RAW DATA SET - SCC8 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "CASSINI RSS RAW DATA SET - SCC8 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-P-MVIC-3-PLUTO-V2.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This data set contains Calibrated data taken by the New Horizons         Multispectral Visible Imaging Camera                                   instrument during the                                                    Pluto encounter                                                        mission phase.  This is VERSION 2.0 of this data set.                    This data set contains MVIC observations taken during the                the Approach (Jan-Jul, 2015) and Encounter mission sub-phases,           including flyby observations taken on 14 July, 2015.                     This is version 2.0 of this data set. Version 1.0 included data          downlinked between the end of July, 2015 through the end of October      2015. Changes since version 1.0 include additional data downlinked       between October, 2015 and the end of January, 2016. These observations   include Charon, Nix and Hydra observations from the day of encounter,    Pluto and Charon Multi-maps and Multi-longitudes from Approach,          full-frame versions of observations downlinked as sub-framed (windowed)  versions for version 1.0, Kerberos and Styx observations, Pluto          High-phase and Color observations, and departure Ring-search             observations taken in November, 2015.                                    Also, updates were made to the documentation and catalog files,          primarily to resolve liens from the V1.0 peer review.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-p-mvic-3-pluto-v2.0_g5qy-uprx",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "new horizons",
                 "charon",
@@ -796627,72 +796629,45 @@
                 "nix",
                 "pluto"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-P-MVIC-3-PLUTO-V2.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-p-mvic-3-pluto-v2.0_g5qy-uprx",
-            "description": "This data set contains Calibrated data taken by the New Horizons         Multispectral Visible Imaging Camera                                   instrument during the                                                    Pluto encounter                                                        mission phase.  This is VERSION 2.0 of this data set.                    This data set contains MVIC observations taken during the                the Approach (Jan-Jul, 2015) and Encounter mission sub-phases,           including flyby observations taken on 14 July, 2015.                     This is version 2.0 of this data set. Version 1.0 included data          downlinked between the end of July, 2015 through the end of October      2015. Changes since version 1.0 include additional data downlinked       between October, 2015 and the end of January, 2016. These observations   include Charon, Nix and Hydra observations from the day of encounter,    Pluto and Charon Multi-maps and Multi-longitudes from Approach,          full-frame versions of observations downlinked as sub-framed (windowed)  versions for version 1.0, Kerberos and Styx observations, Pluto          High-phase and Color observations, and departure Ring-search             observations taken in November, 2015.                                    Also, updates were made to the documentation and catalog files,          primarily to resolve liens from the V1.0 peer review.",
-            "title": "NEW HORIZONS                            \n      MVIC PLUTO ENCOUNTER                                                    \n      CALIBRATED V2.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "NEW HORIZONS                            \n      MVIC PLUTO ENCOUNTER                                                    \n      CALIBRATED V2.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/GPM/DPR/3A-DES/07",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Toshio Iguchi, Robert Meneghini. 2021-12-10. GPM_3DPR_DES. Version 07. GPM DPR Precipitation Profile 1 Day Descending 0.25 degree x 0.25 degree V07. Greenbelt, MD. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/GPM/DPR/3A-DES/07. https://disc.gsfc.nasa.gov/datacollection/GPM_3DPR_DES_07.html. Digital Science Data.",
-            "issued": "2021-12-06",
-            "temporal": "2014-03-09T00:00:00Z/2023-03-01T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2021-12-06",
-            "keyword": [
-                "earth science",
-                "spectral/engineering",
-                "atmosphere",
-                "precipitation",
-                "atmospheric water vapor",
-                "microwave"
-            ],
-            "data-presentation-form": "Digital Science Data",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "JOYCE CHOU",
                 "hasEmail": "mailto:helpdesk@pps-mail.nascom.nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
-            "identifier": "C2179081663-GES_DISC",
-            "description": "Version 07 is the current version of the data set. Older versions will no longer be available and have been superseded by Version 07.\n. \n\nThe Level 3 DPR algorithm accumulates instantaneous precipitation estimates from the Level 2 retrieval algorithms into grids over a day and month time span. There are two grid resolutions: 5.0 degrees and 25 kms. For each grid box, the core statistics are the number of measurements, mean, and standard deviation. Most variables are also conditioned on surface type and precipitation type with other three-dimensional fields adding the height above the ellipsoid. Unless otherwise specified, the means are conditioned on precipitation being present (rain rate &gt; 0). For the daily product, the mean square statistic is saved rather than the standard deviation. In addition to the daily and monthly products is a simplified joint daily product that contains a subset of the fields from the full daily product. The Level 3 DPR products present the user with summary information over daily and monthly time periods. These gridded products are in a convenient gridded form and can be used easily in comparisons with other satellite and ground data.",
-            "release-place": "Greenbelt, MD",
-            "series-name": "GPM_3DPR_DES",
             "creator": "Toshio Iguchi, Robert Meneghini",
-            "title": "GPM DPR Precipitation Profile 1 Day Descending 0.25 degree x 0.25 degree V07 (GPM_3DPR_DES) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/GPM/browse/GPM_3DPR_DES_07.png",
-            "programCode": [
-                "026:001"
-            ],
+            "data-presentation-form": "Digital Science Data",
+            "description": "Version 07 is the current version of the data set. Older versions will no longer be available and have been superseded by Version 07.\n. \n\nThe Level 3 DPR algorithm accumulates instantaneous precipitation estimates from the Level 2 retrieval algorithms into grids over a day and month time span. There are two grid resolutions: 5.0 degrees and 25 kms. For each grid box, the core statistics are the number of measurements, mean, and standard deviation. Most variables are also conditioned on surface type and precipitation type with other three-dimensional fields adding the height above the ellipsoid. Unless otherwise specified, the means are conditioned on precipitation being present (rain rate &gt; 0). For the daily product, the mean square statistic is saved rather than the standard deviation. In addition to the daily and monthly products is a simplified joint daily product that contains a subset of the fields from the full daily product. The Level 3 DPR products present the user with summary information over daily and monthly time periods. These gridded products are in a convenient gridded form and can be used easily in comparisons with other satellite and ground data.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGPM%2FDPR%2F3A-DES%2F07",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGPM%2FDPR%2F3A-DES%2F07",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
@@ -796702,38 +796677,38 @@
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/GPM_3DPR_DES_07.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/GPM_3DPR_DES_07.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://gpm1.gesdisc.eosdis.nasa.gov/data/GPM_L3/GPM_3DPR_DES.07/",
-                    "description": "Access the data via HTTPS",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS",
+                    "downloadURL": "https://gpm1.gesdisc.eosdis.nasa.gov/data/GPM_L3/GPM_3DPR_DES.07/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=GPM_3DPR_DES_07",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=GPM_3DPR_DES_07",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://gpm1.gesdisc.eosdis.nasa.gov/opendap/GPM_L3/GPM_3DPR_DES.07/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://gpm1.gesdisc.eosdis.nasa.gov/opendap/GPM_L3/GPM_3DPR_DES.07/contents.html",
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
@@ -796743,573 +796718,575 @@
                     "title": "View this dataset's algorithm theoretical basis document"
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
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/GPM/browse/GPM_3DPR_DES_07.png",
+            "identifier": "C2179081663-GES_DISC",
+            "issued": "2021-12-06",
+            "keyword": [
+                "earth science",
+                "spectral/engineering",
+                "atmosphere",
+                "precipitation",
+                "atmospheric water vapor",
+                "microwave"
+            ],
+            "landingPage": "https://doi.org/10.5067/GPM/DPR/3A-DES/07",
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
+            "series-name": "GPM_3DPR_DES",
             "spatial": "-180.0 -67.0 180.0 67.0",
+            "temporal": "2014-03-09T00:00:00Z/2023-03-01T00:00:00Z",
             "theme": [
                 "GPM",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "GPM DPR Precipitation Profile 1 Day Descending 0.25 degree x 0.25 degree V07 (GPM_3DPR_DES) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.7927/H4668B3D",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Center for Hazards and Risk Research - CHRR - Columbia University, and Center for International Earth Science Information Network - CIESIN - Columbia University. 2005-12-31. Global Flood Hazard Frequency and Distribution. Version 1.00. Palisades, NY. Archived by National Aeronautics and Space Administration, U.S. Government, Center for Hazards and Risk Research (CHRR)/Columbia University. https://doi.org/10.7927/H4668B3D. https://doi.org/10.7927/H4668B3D.",
-            "issued": "2005-12-31",
-            "temporal": "1985-01-01T00:00:00Z/2003-12-31T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2005-12-31",
-            "references": [
-                "https://doi.org/10.7927/H4T151KP",
-                "https://doi.org/10.7927/H42F7KCP",
-                "https://doi.org/10.7927/H4XS5S9Q"
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
-            "identifier": "C179001777-SEDAC",
-            "description": "The Global Flood Hazard Frequency and Distribution is a 2.5 minute grid derived from a global listing of extreme flood events between 1985 and 2003 (poor or missing data in the early/mid 1990s) compiled by Dartmouth Flood Observatory and georeferenced to the nearest degree. The resultant flood frequency grid was then classified into 10 classes of approximately equal number of grid cells. The greater the grid cell value in the final data set, the higher the relative frequency of flood occurrence. This data set is the result of collaboration among the Columbia University Center for Hazards and Risk Research (CHRR) and Columbia University Center for International Earth Science Information Network (CIESIN).",
-            "release-place": "Palisades, NY",
-            "graphic-preview-description": "Maps Download Page",
             "creator": "Center for Hazards and Risk Research - CHRR - Columbia University, and Center for International Earth Science Information Network - CIESIN - Columbia University",
-            "title": "Global Flood Hazard Frequency and Distribution",
-            "graphic-preview-file": "https://sedac.ciesin.columbia.edu/data/set/ndh-flood-hazard-frequency-distribution/maps",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The Global Flood Hazard Frequency and Distribution is a 2.5 minute grid derived from a global listing of extreme flood events between 1985 and 2003 (poor or missing data in the early/mid 1990s) compiled by Dartmouth Flood Observatory and georeferenced to the nearest degree. The resultant flood frequency grid was then classified into 10 classes of approximately equal number of grid cells. The greater the grid cell value in the final data set, the higher the relative frequency of flood occurrence. This data set is the result of collaboration among the Columbia University Center for Hazards and Risk Research (CHRR) and Columbia University Center for International Earth Science Information Network (CIESIN).",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.7927%2FH4668B3D",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.7927%2FH4668B3D",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/downloads/maps/ndh/ndh-flood-hazard-frequency-distribution/flood-frequency-distribution-thumbnail.jpg",
-                    "description": "Sample browse graphic of the data set.",
                     "@type": "dcat:Distribution",
+                    "description": "Sample browse graphic of the data set.",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/downloads/maps/ndh/ndh-flood-hazard-frequency-distribution/flood-frequency-distribution-thumbnail.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/ndh-flood-hazard-frequency-distribution/data-download",
-                    "description": "Data Download Page",
                     "@type": "dcat:Distribution",
+                    "description": "Data Download Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/ndh-flood-hazard-frequency-distribution/data-download",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/ndh-flood-hazard-frequency-distribution/maps",
-                    "description": "Maps Download Page",
                     "@type": "dcat:Distribution",
+                    "description": "Maps Download Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/ndh-flood-hazard-frequency-distribution/maps",
+                    "mediaType": "text/html",
                     "title": "Get a related map visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/ndh-flood-hazard-frequency-distribution/maps/services",
-                    "description": "Web Map Service Page",
                     "@type": "dcat:Distribution",
+                    "description": "Web Map Service Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/ndh-flood-hazard-frequency-distribution/maps/services",
+                    "mediaType": "text/html",
                     "title": "Use Web Map Service (WMS) to download the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/ndh-flood-hazard-frequency-distribution",
-                    "description": "Data Set\u00a0Overview Page",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set\u00a0Overview Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/ndh-flood-hazard-frequency-distribution",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "graphic-preview-description": "Maps Download Page",
+            "graphic-preview-file": "https://sedac.ciesin.columbia.edu/data/set/ndh-flood-hazard-frequency-distribution/maps",
+            "identifier": "C179001777-SEDAC",
+            "issued": "2005-12-31",
+            "keyword": [
+                "natural hazards",
+                "earth science",
+                "human dimensions"
+            ],
+            "landingPage": "https://doi.org/10.7927/H4668B3D",
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
+                "https://doi.org/10.7927/H4T151KP",
+                "https://doi.org/10.7927/H42F7KCP",
+                "https://doi.org/10.7927/H4XS5S9Q"
+            ],
+            "release-place": "Palisades, NY",
             "spatial": "-180.0 -58.0 180.0 85.0",
+            "temporal": "1985-01-01T00:00:00Z/2003-12-31T00:00:00Z",
             "theme": [
                 "NDH",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Global Flood Hazard Frequency and Distribution"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-A-NAVCAM-2-AST1-V1.0",
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
-                "2867 steins",
-                "international rosetta mission"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This dataset contains RAW DATA of the STEINS flyby Phase from 4 August 2008 until 5 September 2008. The closest approach (CA) took place on 5 September 2008",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-a-navcam-2-ast1-v1.0_g5u8-juyk",
+            "issued": "2018-06-26",
+            "keyword": [
+                "2867 steins",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-A-NAVCAM-2-AST1-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-a-navcam-2-ast1-v1.0_g5u8-juyk",
-            "description": "This dataset contains RAW DATA of the STEINS flyby Phase from 4 August 2008 until 5 September 2008. The closest approach (CA) took place on 5 September 2008",
-            "title": "ROSETTA-ORBITER-STEINS-NAVCAM-2-AST1-V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "ROSETTA-ORBITER-STEINS-NAVCAM-2-AST1-V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/SWOT-LAKESP-2.0",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Surface Water Ocean Topography (SWOT). 2024-02-01. SWOT Level 2 Lake Single-Pass Vector Prior Data Product. Version 2.0. SWOT Level 2 Lake Single-Pass Vector Prior Data Product, Version 2.0. Jet Propulsion Laboratory. Archived by National Aeronautics and Space Administration, U.S. Government, JPL NASA. https://doi.org/10.5067/SWOT-LAKESP-2.0. https://swot.jpl.nasa.gov/.",
-            "issued": "2022-07-20",
-            "temporal": "2022-12-16T00:00:00Z/2024-03-27T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-07-20",
-            "keyword": [
-                "surface water",
-                "terrestrial hydrosphere",
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
-            "identifier": "C2799438247-POCLOUD",
-            "description": "The SWOT Level 2 Lake Single-Pass Vector Prior Data Product from the Surface Water Ocean Topography (SWOT) mission provides water surface elevation, area, storage change derived from the high rate (HR) data stream from the Ka-band Radar Interferometer (KaRIn). SWOT launched on December 16, 2022 from Vandenberg Air Force Base in California into a 1-day repeat orbit for the \"calibration\" or \"fast-sampling\" phase of the mission, which completed in early July 2023. After the calibration phase, SWOT entered a 21-day repeat orbit in August 2023 to start the \"science\" phase of the mission, which is expected to continue through 2025. <br>\r\nWater surface elevation, area, and storage change are provided in three feature datasets covering the full swath for each continent-pass: 1) an observation-oriented feature dataset of lakes identified in the prior lake database (PLD), 2) a feature dataset of lakes identified in the PLD, and 3) a feature dataset containing unassigned features (i.e., not identified in PLD nor prior river database (PRD)).  These data are generally produced for inland and coastal hydrology surfaces, as controlled by the reloadable KaRIn HR mask. The dataset is distributed in ESRI Shapefile format. <br>\r\nThis collection is a sub-collection of its parent: https://podaac.jpl.nasa.gov/dataset/SWOT_L2_HR_LakeSP_2.0 It contains feature datasets of lakes identified in the PLD.",
-            "release-place": "Jet Propulsion Laboratory",
-            "series-name": "SWOT Level 2 Lake Single-Pass Vector Prior Data Product",
-            "graphic-preview-description": "Thumbnail",
             "creator": "Surface Water Ocean Topography (SWOT)",
-            "title": "SWOT Level 2 Lake Single-Pass Vector Prior Data Product, Version 2.0",
-            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/SWOT_L2_HR_LakeSP_2.0.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The SWOT Level 2 Lake Single-Pass Vector Prior Data Product from the Surface Water Ocean Topography (SWOT) mission provides water surface elevation, area, storage change derived from the high rate (HR) data stream from the Ka-band Radar Interferometer (KaRIn). SWOT launched on December 16, 2022 from Vandenberg Air Force Base in California into a 1-day repeat orbit for the \"calibration\" or \"fast-sampling\" phase of the mission, which completed in early July 2023. After the calibration phase, SWOT entered a 21-day repeat orbit in August 2023 to start the \"science\" phase of the mission, which is expected to continue through 2025. <br>\r\nWater surface elevation, area, and storage change are provided in three feature datasets covering the full swath for each continent-pass: 1) an observation-oriented feature dataset of lakes identified in the prior lake database (PLD), 2) a feature dataset of lakes identified in the PLD, and 3) a feature dataset containing unassigned features (i.e., not identified in PLD nor prior river database (PRD)).  These data are generally produced for inland and coastal hydrology surfaces, as controlled by the reloadable KaRIn HR mask. The dataset is distributed in ESRI Shapefile format. <br>\r\nThis collection is a sub-collection of its parent: https://podaac.jpl.nasa.gov/dataset/SWOT_L2_HR_LakeSP_2.0 It contains feature datasets of lakes identified in the PLD.",
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
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2799438247-POCLOUD",
-                    "description": "HTTPS endpoint for data browse and download",
                     "@type": "dcat:Distribution",
+                    "description": "HTTPS endpoint for data browse and download",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2799438247-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2799438247-POCLOUD",
-                    "description": "Browse granule search results in Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse granule search results in Earthdata Search",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2799438247-POCLOUD",
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
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2799438247-POCLOUD&pg%5B0%5D%5Bid%5D=*PIC0*",
-                    "description": "Search Granules from Forward Processing (PIC0)",
                     "@type": "dcat:Distribution",
+                    "description": "Search Granules from Forward Processing (PIC0)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2799438247-POCLOUD&pg%5B0%5D%5Bid%5D=*PIC0*",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2799438247-POCLOUD&pg%5B0%5D%5Bid%5D=*PGC0*",
-                    "description": "Search Granules from Bulk Reprocessing (PGC0)",
                     "@type": "dcat:Distribution",
+                    "description": "Search Granules from Bulk Reprocessing (PGC0)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2799438247-POCLOUD&pg%5B0%5D%5Bid%5D=*PGC0*",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 }
             ],
+            "graphic-preview-description": "Thumbnail",
+            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/SWOT_L2_HR_LakeSP_2.0.jpg",
+            "identifier": "C2799438247-POCLOUD",
+            "issued": "2022-07-20",
+            "keyword": [
+                "surface water",
+                "terrestrial hydrosphere",
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
+            "series-name": "SWOT Level 2 Lake Single-Pass Vector Prior Data Product",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2022-12-16T00:00:00Z/2024-03-27T00:00:00Z",
             "theme": [
                 "SWOT",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "SWOT Level 2 Lake Single-Pass Vector Prior Data Product, Version 2.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/AURA/TES/TL2CONS_L2.007",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2017-03-07. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/AURA/TES/TL2CONS_L2.007. https://asdc.larc.nasa.gov/project/TES.",
-            "issued": "2015-08-27",
-            "temporal": "2004-09-13T00:00:00Z/2018-01-22T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2019-06-19",
-            "keyword": [
-                "air quality",
-                "atmosphere",
-                "atmospheric temperature",
-                "atmospheric chemistry",
-                "earth science",
-                "clouds"
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
-            "identifier": "C1331182631-LARC",
             "description": "TL2CONS_7 is the Tropospheric Emission Spectrometer (TES)/Aura Level 2 Carbon Monoxide Nadir Special Observation Version 7 data product. TES was an instrument aboard NASA's Aura satellite and was launched from California on July 15, 2004. Data collection for TES is complete. TES Level 2 data contain retrieved species (or temperature) profiles at the observation targets and the estimated errors. The geolocation, quality, and other data (e.g., surface characteristics for nadir observations) were also provided. L2 modeled spectra were evaluated using radiative transfer modeling algorithms. The process, referred to as retrieval, compared observed spectra to the modeled spectra and iteratively updated the atmospheric parameters. L2 standard product files included information for one molecular species (or temperature) for an entire global survey or special observation run. A global survey consisted of a maximum of 16 consecutive orbits.\r\rNadir observations, which point directly to the surface of the Earth, are different from limb observations, which are pointed at various off-nadir angles into the atmosphere. Nadir and limb observations were added to separate L2 files, and a single ancillary file was composed of data that are common to both nadir and limb files. A Nadir sequence within the TES Global Survey was a fixed number of observations within an orbit for a Global Survey. Prior to April 24, 2005, it consisted of two low resolution scans over the same ground locations. After April 24, 2005, Global Survey data consisted of three low resolution scans. The Nadir standard product consists of four files, where each file is composed of the Global Survey Nadir observations from one of four focal planes for a single orbit, i.e. 72 orbit sequences. The Global Survey Nadir observations only used a single set of filter mix. \r\rA Global Survey consisted of observations along 16 consecutive orbits at the start of a two day cycle, over which 4,608 retrievals were performed. Each observation was the input for retrievals of species Volume Mixing Ratios (VMRs), temperature profiles, surface temperature, and other data parameters with associated pressure levels, precision, total error, vertical resolution, total column density, and other diagnostic quantities. Each TES Level 2 standard product reported information in a swath format conforming to the HDF-EOS Aura File Format Guidelines. Each Swath object was bounded by the number of observations in a global survey and a predefined set of pressure levels, representing slices through the atmosphere. Each standard product could have had a variable number of observations depending upon the Global Survey configuration and whether averaging was employed. Also, missing or bad retrievals were not reported. Further, observations were occasionally scheduled on non-global survey days. In general they were measurements made for validation purposes or with highly focused science objectives. Those non-global survey measurements were referred to as \u201cspecial observations.\u201d\r\rA Limb sequence within the TES Global Survey was three high-resolution scans over the same limb locations. The Limb standard product consists of four files, where each file is composed of the Global Survey Limb observations from one of four focal planes for a single orbit, i.e. 72 orbit sequences. The Global Survey Limb observations used a repeating sequence of filter wheel positions. Special Observations could only be scheduled during the 9 or 10 orbit gaps in the Global Surveys, and were conducted in any of three basic modes: stare, transect, step-and-stare. The mode used depended on the science requirement. Each limb observation Limb 1, Limb 2 and Limb 3, were processed independently. Thus, each limb standard product consisted of three sets where each set consisted of 1,152 observations. For TES, the swath object represented one of these sets. Thus, each limb standard product consisted of three swath objects, one for each observation, Limb",
-            "title": "TES/Aura L2 Carbon Monoxide Nadir Special Observation V007",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAURA%2FTES%2FTL2CONS_L2.007",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAURA%2FTES%2FTL2CONS_L2.007",
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
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1331182631-LARC",
-                    "description": "Earthdata Search for TL2CONS_7 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for TL2CONS_7 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1331182631-LARC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/AURA/TES/TL2CONS_L2.007",
-                    "description": "DOI data set landing page for TL2CONS_7",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for TL2CONS_7",
+                    "downloadURL": "https://doi.org/10.5067/AURA/TES/TL2CONS_L2.007",
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
-                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/TES/TL2CONS.007/contents.html",
-                    "description": "OPeNDAP data access for TL2CONS_7",
                     "@type": "dcat:Distribution",
+                    "description": "OPeNDAP data access for TL2CONS_7",
+                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/TES/TL2CONS.007/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/TES/TL2CONS.007/",
-                    "description": "ASDC Direct Data Download for TL2CONS_7",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for TL2CONS_7",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/TES/TL2CONS.007/",
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
-                {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/tes/guide/TESDataUsersGuideV8_0_March_27_2020_FV-8_rh.pdf",
-                    "description": "TES Level 2 (L2) Data User's Guide (Up to & including Version 8 data)",
+                {
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
-                    "downloadURL": "https://subset.larc.nasa.gov/tes/login.php",
-                    "description": "TES Search and Subsetting Web Application",
                     "@type": "dcat:Distribution",
+                    "description": "TES Search and Subsetting Web Application",
+                    "downloadURL": "https://subset.larc.nasa.gov/tes/login.php",
+                    "mediaType": "text/html",
                     "title": "Subset this dataset using a web based subsetter"
                 }
             ],
+            "identifier": "C1331182631-LARC",
+            "issued": "2015-08-27",
+            "keyword": [
+                "air quality",
+                "atmosphere",
+                "atmospheric temperature",
+                "atmospheric chemistry",
+                "earth science",
+                "clouds"
+            ],
+            "landingPage": "https://doi.org/10.5067/AURA/TES/TL2CONS_L2.007",
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
+            "title": "TES/Aura L2 Carbon Monoxide Nadir Special Observation V007"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-ROSINA-3-EXT3-V2.0",
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
+            "description": "This data set contains CODMAC level 3 science data acquired by the DFMS and RTOF ROSINA sensors between 2016-06-28 and 2016-06-30 during the Extension phase 3 of the Rosetta mission to comet 67P/CG. V2.0 : Mass scale has been enhanced for a selection of masses which are now provided with 4 digits after the coma and the offset removal has been improved, corrupted files have been removed in the V2.0",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rosina-3-ext3-v2.0_g5wv-9d6v",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-ROSINA-3-EXT3-V2.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rosina-3-ext3-v2.0_g5wv-9d6v",
-            "description": "This data set contains CODMAC level 3 science data acquired by the DFMS and RTOF ROSINA sensors between 2016-06-28 and 2016-06-30 during the Extension phase 3 of the Rosetta mission to comet 67P/CG. V2.0 : Mass scale has been enhanced for a selection of masses which are now provided with 4 digits after the coma and the offset removal has been improved, corrupted files have been removed in the V2.0",
-            "title": "ROSETTA-ORBITER 67P ROSINA 3\n                                      EXT3 V2.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P ROSINA 3\n                                      EXT3 V2.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/MODIS/MOD00F.NRT.061",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "MODIS Science Team/MODIS Adaptive Processing System (MODAPS). 2017-10-21. MODIS/Terra L0 PDS Data 5-Min Swath - NRT. Version 6.1NRT. MODAPS at NASA/GSFC. Archived by National Aeronautics and Space Administration, U.S. Government, The Land, Atmosphere Near real-time Capability for EOS (LANCE). https://doi.org/10.5067/MODIS/MOD00F.NRT.061.",
-            "issued": "2017-10-11",
-            "temporal": "2017-10-05T00:00:00Z/2023-02-28T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-02-24",
-            "keyword": [
-                "earth science",
-                "visible wavelengths",
-                "ultraviolet wavelengths",
-                "spectral/engineering",
-                "ngda",
-                "national geospatial data asset"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "GANG YE, PH.D",
                 "hasEmail": "mailto:gang.ye-1@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Not provided"
-            },
-            "identifier": "C1426396538-LANCEMODIS",
-            "description": "MODIS/Terra Near Real Time(NRT) L0 PDS Data 5-Min Swath.",
-            "release-place": "MODAPS at NASA/GSFC",
             "creator": "MODIS Science Team/MODIS Adaptive Processing System (MODAPS)",
-            "title": "MODIS/Terra L0 PDS Data 5-Min Swath - NRT",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "MODIS/Terra Near Real Time(NRT) L0 PDS Data 5-Min Swath.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMODIS%2FMOD00F.NRT.061",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMODIS%2FMOD00F.NRT.061",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
@@ -797319,178 +797296,179 @@
                     "title": "Download this dataset through LANCE"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://lance3.modaps.eosdis.nasa.gov/data_products/",
-                    "description": "Access Collection 6.1 data set from the MODAPS LANCE-MODIS page",
                     "@type": "dcat:Distribution",
+                    "description": "Access Collection 6.1 data set from the MODAPS LANCE-MODIS page",
+                    "downloadURL": "https://lance3.modaps.eosdis.nasa.gov/data_products/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through MODAPS"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nrt3.modaps.eosdis.nasa.gov/archive/allData/61/MOD00F/",
-                    "description": "Direct access to the download site and directory hosting the MOD00F C6.1 NRT data set.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct access to the download site and directory hosting the MOD00F C6.1 NRT data set.",
+                    "downloadURL": "https://nrt3.modaps.eosdis.nasa.gov/archive/allData/61/MOD00F/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through MODAPS"
                 }
             ],
+            "identifier": "C1426396538-LANCEMODIS",
+            "issued": "2017-10-11",
+            "keyword": [
+                "earth science",
+                "visible wavelengths",
+                "ultraviolet wavelengths",
+                "spectral/engineering",
+                "ngda",
+                "national geospatial data asset"
+            ],
+            "landingPage": "https://doi.org/10.5067/MODIS/MOD00F.NRT.061",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2023-02-24",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Not provided"
+            },
+            "release-place": "MODAPS at NASA/GSFC",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2017-10-05T00:00:00Z/2023-02-28T00:00:00Z",
             "theme": [
                 "TERRA",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "MODIS/Terra L0 PDS Data 5-Min Swath - NRT"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/GPMGV/IFLOODS/NEXRAD/DATA401",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Unidata  and   NWS Radar Operations Center.2018. GPM Ground Validation NEXRAD Level III KDMX IFloodS [indicate subset used]. Dataset available online from the NASA Global Hydrometeorology Resource Center DAAC, Huntsville, Alabama, U.S.A. DOI: http://dx.doi.org/10.5067/GPMGV/IFLOODS/NEXRAD/DATA401",
-            "issued": "2018-03-05",
-            "temporal": "2013-03-29T21:05:00Z/2013-06-18T16:32:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-05-09",
-            "keyword": [
-                "precipitation",
-                "earth science",
-                "spectral/engineering",
-                "radar",
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
-            "identifier": "C1980844236-GHRC_DAAC",
             "description": "The GPM Ground Validation NEXRAD Level III KDMX IFloodS dataset   contain precipitation products derived from selected NEXt Generation Weather RADar system (NEXRAD) radars in operation during the Iowa Flood Studies (IFloodS) field campaign to help support the ground validation of the Global Precipitation Measurement (GPM). NEXRAD is a network of 160 stationary S-Band radars dispersed throughout the United States and select locations abroad. Data were gathered from four NEXRAD stations in the vicinity of the IFloodS campaign during  March 29, 2013 through June 18, 2013. This dataset contains data files of digital instantaneous precipitation rate (DPR) and storm total accumulation estimates (DTA) in NIDS binary format.",
-            "title": "GPM Ground Validation NEXRAD Level III KDMX IFloodS V1",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGPMGV%2FIFLOODS%2FNEXRAD%2FDATA401",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGPMGV%2FIFLOODS%2FNEXRAD%2FDATA401",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=gpmkdmx3ifld",
-                    "description": "Files may be downloaded directly to your workstation from this link",
                     "@type": "dcat:Distribution",
+                    "description": "Files may be downloaded directly to your workstation from this link",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=gpmkdmx3ifld",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://www.ofcm.gov/publications/fmh/FMH11/fmh11partC.pdf",
-                    "description": "WSR-88D Meteorological Observations: Part C WSR-88D Products and Algorithms",
                     "@type": "dcat:Distribution",
+                    "description": "WSR-88D Meteorological Observations: Part C WSR-88D Products and Algorithms",
+                    "downloadURL": "https://www.ofcm.gov/publications/fmh/FMH11/fmh11partC.pdf",
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
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/ifloods/NEXRAD3/KDMX/doc/gpmnexrad3iflds_dataset.pdf",
-                    "description": "GPM Ground Validation NEXRAD Level III IFloodS User Guide",
                     "@type": "dcat:Distribution",
+                    "description": "GPM Ground Validation NEXRAD Level III IFloodS User Guide",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/ifloods/NEXRAD3/KDMX/doc/gpmnexrad3iflds_dataset.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.1175/JHM-D-14-0148.1",
-                    "description": "NEXRAD NWS Polarimetric Precipitation Product Evaluation for IFloodS",
                     "@type": "dcat:Distribution",
+                    "description": "NEXRAD NWS Polarimetric Precipitation Product Evaluation for IFloodS",
+                    "downloadURL": "https://doi.org/10.1175/JHM-D-14-0148.1",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.1175/2008JAMC1753.1",
-                    "description": "Estimation of Rainfall Based on the Results of Polarimetric Echo Classification",
                     "@type": "dcat:Distribution",
+                    "description": "Estimation of Rainfall Based on the Results of Polarimetric Echo Classification",
+                    "downloadURL": "https://doi.org/10.1175/2008JAMC1753.1",
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
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/home/about-ghrc/citing-ghrc-daac-data",
-                    "description": "Instructions for citing GHRC data",
                     "@type": "dcat:Distribution",
+                    "description": "Instructions for citing GHRC data",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/home/about-ghrc/citing-ghrc-daac-data",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C1980844236-GHRC_DAAC",
+            "issued": "2018-03-05",
+            "keyword": [
+                "precipitation",
+                "earth science",
+                "spectral/engineering",
+                "radar",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.5067/GPMGV/IFLOODS/NEXRAD/DATA401",
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
             "spatial": "-94.1719 41.282 -93.2737 42.1802",
+            "temporal": "2013-03-29T21:05:00Z/2013-06-18T16:32:00Z",
             "theme": [
                 "IFloodS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "GPM Ground Validation NEXRAD Level III KDMX IFloodS V1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/Aura/MLS/DATA2504",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Santee, M., Froidevaux, L., Livesey, N. and Read, W.. 2020-06-11. ML2CH3OH. Version 005. MLS/Aura Level 2 Methanol (CH3OH) Mixing Ratio V005. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/Aura/MLS/DATA2504. https://disc.gsfc.nasa.gov/datacollection/ML2CH3OH_005.html. Digital Science Data.",
-            "issued": "2020-02-04",
-            "temporal": "2004-08-02T00:00:00Z/2022-01-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-02-04",
-            "keyword": [
-                "atmospheric chemistry",
-                "earth science",
-                "atmosphere"
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
-            "identifier": "C1729925104-GES_DISC",
-            "description": "At this time it is recommended that these data not be used pending further validation.ML2CH3OH is the EOS Aura Microwave Limb Sounder (MLS) standard product for methanol derived from radiances measured by the 640 GHz radiometer. The data version is 5.0. Data coverage is from August 8, 2004 to current. Spatial coverage is near-global (-82 degrees to +82 degrees latitude), with each profile spaced 1.5 degrees or ~165 km along the orbit track (roughly 15 orbits per day). The recommended useful vertical range is between 147 and 100 hPa, and the vertical resolution range is about 4-5 km. Users of the ML2CH3OH data product should read section 3.5 of the EOS MLS Level 2 Version 5 Quality Document for more information.\n\nThe data are stored in the version 5 EOS Hierarchical Data Format (HDF-EOS5), which is based on the version 5 Hierarchical Data Format, or HDF-5. Each file contains one swath object (profile data), with a set of data and geolocation fields, swath attributes, and metadata.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "ML2CH3OH",
             "creator": "Santee, M., Froidevaux, L., Livesey, N. and Read, W.",
-            "title": "MLS/Aura Level 2 Methanol (CH3OH) Mixing Ratio V005 (ML2CH3OH) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/ML2CH3OH_005.png",
-            "programCode": [
-                "026:001"
-            ],
+            "data-presentation-form": "Digital Science Data",
+            "description": "At this time it is recommended that these data not be used pending further validation.ML2CH3OH is the EOS Aura Microwave Limb Sounder (MLS) standard product for methanol derived from radiances measured by the 640 GHz radiometer. The data version is 5.0. Data coverage is from August 8, 2004 to current. Spatial coverage is near-global (-82 degrees to +82 degrees latitude), with each profile spaced 1.5 degrees or ~165 km along the orbit track (roughly 15 orbits per day). The recommended useful vertical range is between 147 and 100 hPa, and the vertical resolution range is about 4-5 km. Users of the ML2CH3OH data product should read section 3.5 of the EOS MLS Level 2 Version 5 Quality Document for more information.\n\nThe data are stored in the version 5 EOS Hierarchical Data Format (HDF-EOS5), which is based on the version 5 Hierarchical Data Format, or HDF-5. Each file contains one swath object (profile data), with a set of data and geolocation fields, swath attributes, and metadata.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAura%2FMLS%2FDATA2504",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAura%2FMLS%2FDATA2504",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
@@ -797500,717 +797478,751 @@
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/ML2CH3OH_005.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/ML2CH3OH_005.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/Aura_MLS_Level2/ML2CH3OH.005/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/Aura_MLS_Level2/ML2CH3OH.005/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/opendap/HDF-EOS5/Aura_MLS_Level2/ML2CH3OH.005/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/opendap/HDF-EOS5/Aura_MLS_Level2/ML2CH3OH.005/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=ML2CH3OH_005",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=ML2CH3OH_005",
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
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/ML2CH3OH_005.png",
+            "identifier": "C1729925104-GES_DISC",
+            "issued": "2020-02-04",
+            "keyword": [
+                "atmospheric chemistry",
+                "earth science",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.5067/Aura/MLS/DATA2504",
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
+            "series-name": "ML2CH3OH",
             "spatial": "-180.0 -82.0 180.0 82.0",
+            "temporal": "2004-08-02T00:00:00Z/2022-01-17T00:00:00Z",
             "theme": [
                 "Aura",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "MLS/Aura Level 2 Methanol (CH3OH) Mixing Ratio V005 (ML2CH3OH) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=WIYN-S-WI-2-RPX-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This data set contains images of the Saturn system from the Wisconsin-Indiana-Yale-NOAO(WIYN) using the WIYN Imager in late November 1995. These observations were made during and immediately after the ring plane crossing.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.wiyn-s-wi-2-rpx-v1.0_g62e-dcyy",
             "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "saturn ring plane crossing 1995",
                 "saturn",
                 "flat field"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=WIYN-S-WI-2-RPX-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.wiyn-s-wi-2-rpx-v1.0_g62e-dcyy",
-            "description": "This data set contains images of the Saturn system from the Wisconsin-Indiana-Yale-NOAO(WIYN) using the WIYN Imager in late November 1995. These observations were made during and immediately after the ring plane crossing.",
-            "title": "WIYN S WI RAW RING PLANE CROSSING V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "WIYN S WI RAW RING PLANE CROSSING V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/AURA/TES/TL3O3D.006",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/AURA/TES/TL3O3D.006. https://asdc.larc.nasa.gov/project/TES.",
-            "issued": "2019-02-27",
-            "temporal": "2004-09-03T00:00:00Z/2018-01-22T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2019-06-19",
-            "keyword": [
-                "atmospheric chemistry",
-                "earth science",
-                "atmospheric water vapor",
-                "atmospheric temperature",
-                "atmospheric pressure",
-                "air quality",
-                "atmosphere"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "SCOTT GLUCK",
                 "hasEmail": "mailto:support-asdc@earthdata.nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/LARC/SD/ASDC"
-            },
-            "identifier": "C1630077566-LARC",
             "description": "TL3O3D_6 is the Tropospheric Emission Spectrometer (TES)/Aura L3 Ozone Daily Gridded Version 6 data product. TES was an instrument aboard NASA's Aura satellite and was launched from California on July 15, 2004. Data collection for TES is complete. This data product consists of daily atmospheric temperature and volume mixing ratio (VMR) for the atmospheric species, which were provided at 2 degree latitude by 4 degree longitude spatial grids and at a subset of TES standard pressure levels. The TES Science Data Processing L3 subsystem interpolated the L2 atmospheric profiles collected in a Global Survey onto a global grid uniform in latitude and longitude to provide a 3-D representation of the distribution of atmospheric gasses. Daily and monthly averages of L2 profiles and browse images are available. The L3 standard data products were composed of L3 HDF-EOS grid data. A separate product file is produced for each different atmospheric species. \r\rTES obtains data in two basic observation modes: Limb or Nadir. The product file may have contained, in separate folders, limb data, nadir data, or both folders may be present. Specific to L3 processing are the terms Daily and Monthly representing the approximate time coverage of the L3 products. However, the input data granules to the L3 process are completed Global Surveys; in other words a Global Survey was not split in relation to time when input to the L3 processes even if they exceeded the usual understood meanings of a day or month. More specifically, Daily L3 products represented a single Global Survey (approximately 26 hours) and Monthly L3 products represented Global Surveys that were initiated within that calendar month. The data granules defined for L3 standard products were daily and monthly. Details of the format of this product can be found in the TES Data Products Specifications (DPS).",
-            "title": "TES/Aura L3 Ozone Daily Gridded V006",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAURA%2FTES%2FTL3O3D.006",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAURA%2FTES%2FTL3O3D.006",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://l0dup05.larc.nasa.gov/public/cgi-bin/DUE/tes_L3daily.cgi",
-                    "description": "Report of TES Level 3 Daily Data Products Available from the ASDC",
                     "@type": "dcat:Distribution",
+                    "description": "Report of TES Level 3 Daily Data Products Available from the ASDC",
+                    "downloadURL": "https://l0dup05.larc.nasa.gov/public/cgi-bin/DUE/tes_L3daily.cgi",
+                    "mediaType": "text/html",
                     "title": "View this dataset's production history"
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
-                    "downloadURL": "https://doi.org/10.5067/AURA/TES/TL3O3D.006",
-                    "description": "DOI data set landing page for TL3O3D_6",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for TL3O3D_6",
+                    "downloadURL": "https://doi.org/10.5067/AURA/TES/TL3O3D.006",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
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
-                    "downloadURL": "https://gs614-avdc1-pz.gsfc.nasa.gov/Overview/",
-                    "description": "EOS Aura Science Team Meeting AGENDA, August 27 - August 29, 2019 Pasadena, CA, USA",
                     "@type": "dcat:Distribution",
+                    "description": "EOS Aura Science Team Meeting AGENDA, August 27 - August 29, 2019 Pasadena, CA, USA",
+                    "downloadURL": "https://gs614-avdc1-pz.gsfc.nasa.gov/Overview/",
+                    "mediaType": "text/html",
                     "title": "View the primary investigator's documentation for this dataset"
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
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1630077566-LARC",
-                    "description": "Earthdata Search for TL3O3D_6 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for TL3O3D_6 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1630077566-LARC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/TES/TL3O3D.006/",
-                    "description": "ASDC Direct Data Download for\u00a0TL3O3D_6",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for\u00a0TL3O3D_6",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/TES/TL3O3D.006/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/TES/TL3O3D.006/contents.html",
-                    "description": "OPeNDAP data access for TL3O3D_6",
                     "@type": "dcat:Distribution",
+                    "description": "OPeNDAP data access for TL3O3D_6",
+                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/TES/TL3O3D.006/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/tes/guide/TES_Database_DD_R15.pdf",
-                    "description": "TES Ground Data System Database Definition, Release 15.0 \u2013 R14v147 - March 22, 2019",
                     "@type": "dcat:Distribution",
+                    "description": "TES Ground Data System Database Definition, Release 15.0 \u2013 R14v147 - March 22, 2019",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/tes/guide/TES_Database_DD_R15.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/tes/guide/TES_L3_Products_PGE_Spec_R15.pdf",
-                    "description": "TES L3 Products PGE Specification PGE Definition and Production Rules Release 15 - March 21, 2019",
                     "@type": "dcat:Distribution",
+                    "description": "TES L3 Products PGE Specification PGE Definition and Production Rules Release 15 - March 21, 2019",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/tes/guide/TES_L3_Products_PGE_Spec_R15.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's science data product software documentation"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/tes/guide/TES_L3_Products_RDD_R15.pdf",
-                    "description": "TES L3 Products Release Description Document Release 15",
                     "@type": "dcat:Distribution",
+                    "description": "TES L3 Products Release Description Document Release 15",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/tes/guide/TES_L3_Products_RDD_R15.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/tes/quality_summaries/L3_products_R15.pdf",
-                    "description": "TES L3 R15 Data Quality Summary",
                     "@type": "dcat:Distribution",
+                    "description": "TES L3 R15 Data Quality Summary",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/tes/quality_summaries/L3_products_R15.pdf",
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
                 }
             ],
+            "identifier": "C1630077566-LARC",
+            "issued": "2019-02-27",
+            "keyword": [
+                "atmospheric chemistry",
+                "earth science",
+                "atmospheric water vapor",
+                "atmospheric temperature",
+                "atmospheric pressure",
+                "air quality",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.5067/AURA/TES/TL3O3D.006",
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
+            "temporal": "2004-09-03T00:00:00Z/2018-01-22T23:59:59Z",
             "theme": [
                 "TES",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "TES/Aura L3 Ozone Daily Gridded V006"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/GPMGV/OLYMPEX/MASC/DATA101",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Padmanabhan, Sharmila  and Robert  Stachnik.2018. GPM Ground Validation Microwave Atmospheric Sounder on Cubesat (MASC) OLYMPEX [indicate subset used]. Dataset available online from the NASA Global Hydrometeorology Resource Center DAAC, Huntsville, Alabama, U.S.A. DOI: http://dx.doi.org/10.5067/GPMGV/OLYMPEX/MASC/DATA101",
-            "issued": "2018-06-18",
-            "temporal": "2015-11-10T18:37:59Z/2015-12-13T18:23:57Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-05-18",
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
-            "identifier": "C1979620173-GHRC_DAAC",
             "description": "The GPM Ground Validation Microwave Atmospheric Sounder on Cubesat (MASC) OLYMPEX dataset consists of microwave radiance measurements collected during the GPM Ground Validation Olympic Mountains Experiment (OLYMPEX) field campaign held in the Pacific Northwest. These data were collected by the MASC aboard the NASA DC-8 aircraft, for dates between November 10, 2016 and December 13, 2016.  The data are provided in HDF-EOS5 format.",
-            "title": "GPM Ground Validation Microwave Atmospheric Sounder on Cubesat (MASC) OLYMPEX V1",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGPMGV%2FOLYMPEX%2FMASC%2FDATA101",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGPMGV%2FOLYMPEX%2FMASC%2FDATA101",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=gpmmascolyx",
-                    "description": "Files may be downloaded directly to your workstation from this link",
                     "@type": "dcat:Distribution",
+                    "description": "Files may be downloaded directly to your workstation from this link",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=gpmmascolyx",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "http://www.isac.cnr.it/~ipwg/meetings/bologna-2016/Bologna2016_Orals/4-3_Turk.pdf",
-                    "description": "Multi-Frequency Radar/Passive Microwave Observations and Simulations of Cold Season Precipitation from GPM and OLYMPEX data.",
                     "@type": "dcat:Distribution",
+                    "description": "Multi-Frequency Radar/Passive Microwave Observations and Simulations of Cold Season Precipitation from GPM and OLYMPEX data.",
+                    "downloadURL": "http://www.isac.cnr.it/~ipwg/meetings/bologna-2016/Bologna2016_Orals/4-3_Turk.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://dx.doi.org/10.5067/GPMGV/OLYMPEX/DATA101",
-                    "description": "OLYMPEX Field Campaign DOI",
                     "@type": "dcat:Distribution",
+                    "description": "OLYMPEX Field Campaign DOI",
+                    "downloadURL": "http://dx.doi.org/10.5067/GPMGV/OLYMPEX/DATA101",
+                    "mediaType": "text/html",
                     "title": "View information related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/olympex/MASC/doc/gpmmascolyx_dataset.pdf",
-                    "description": "The guide document contains detailed information about the dataset",
                     "@type": "dcat:Distribution",
+                    "description": "The guide document contains detailed information about the dataset",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/olympex/MASC/doc/gpmmascolyx_dataset.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
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
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/home/about-ghrc/citing-ghrc-daac-data",
-                    "description": "Instructions for citing GHRC data",
                     "@type": "dcat:Distribution",
+                    "description": "Instructions for citing GHRC data",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/home/about-ghrc/citing-ghrc-daac-data",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C1979620173-GHRC_DAAC",
+            "issued": "2018-06-18",
+            "keyword": [
+                "spectral/engineering",
+                "microwave",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/GPMGV/OLYMPEX/MASC/DATA101",
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
             "spatial": "-129.184 39.1659 -119.73 49.4608",
+            "temporal": "2015-11-10T18:37:59Z/2015-12-13T18:23:57Z",
             "theme": [
                 "OLYMPEX",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "GPM Ground Validation Microwave Atmospheric Sounder on Cubesat (MASC) OLYMPEX V1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-4-EXT3-67P-M31-STRLIGHT-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This CODMAC level 4 data set contains solar stray light corrected, radiometric calibrated and geometric distortion corrected (resampled) image data in W/m^2/sr/nm, acquired by the OSIRIS Narrow Angle Camera on the Rosetta spacecraft during the ROSETTA EXTENSION 3 mission phase, covering the period from 2016-06-28T23:25:00.000 to 2016-07-26T23:24:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V1.0 is the first version of this dataset: Lien corrected dataset after October 2018 PSA/PDS external peer review.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-4-ext3-67p-m31-strlight-v1.0",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2021-05-21",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "international rosetta mission",
                 "67p/churyumov-gerasimenko 1 (1969 r1)",
                 "16 cyg b"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-4-EXT3-67P-M31-STRLIGHT-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-4-ext3-67p-m31-strlight-v1.0",
-            "description": "This CODMAC level 4 data set contains solar stray light corrected, radiometric calibrated and geometric distortion corrected (resampled) image data in W/m^2/sr/nm, acquired by the OSIRIS Narrow Angle Camera on the Rosetta spacecraft during the ROSETTA EXTENSION 3 mission phase, covering the period from 2016-06-28T23:25:00.000 to 2016-07-26T23:24:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V1.0 is the first version of this dataset: Lien corrected dataset after October 2018 PSA/PDS external peer review.",
-            "title": "ROSETTA-ORBITER 67P OSINAC 4 EXT3-MTP031 RDR-STRLIGHT V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P OSINAC 4 EXT3-MTP031 RDR-STRLIGHT V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-PRL-0307-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the PRELANDING phase 2014-01-21 to 2014-11-18. It is a Global Gravity measurement at the comet 67P and covers the time 2014-09-21T05:52:05.000 to 2014-09-21T08:17:24.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-prl-0307-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-PRL-0307-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-prl-0307-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the PRELANDING phase 2014-01-21 to 2014-11-18. It is a Global Gravity measurement at the comet 67P and covers the time 2014-09-21T05:52:05.000 to 2014-09-21T08:17:24.000.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     PRELANDING 0307 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     PRELANDING 0307 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-2-PRL-67PCHURYUMOV-M08-V3.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This CODMAC level 2 data set contains uncalibrated image data in DN unit, acquired by the OSIRIS Wide Angle Camera on the Rosetta spacecraft during the PRELANDING mission phase, covering the period from 2014-09-23T10:00:00.000 to 2014-10-24T09:59:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V3.0 supersedes previous deliveries of the same dataset with the following changes since the last version: Lien corrected dataset after the July and October 2018 PSA/PDS external peer reviews. Updated documentation and ancillary files, added document on bandpass filter. Updated SCIENCE_USER_GUIDE_V03.PDF to include one section about FAQ and one section about image data quality. Added shutter backtravel and readout issues to image quality map. Updated DATA_QUALITY_ID keyword in image header. Improved handling of images with missing packets. Included FITs files. Browse products changed to the same size as the original image.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-2-prl-67pchuryumov-m08-v3.0",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2021-05-21",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "international rosetta mission",
                 "67p/churyumov-gerasimenko 1 (1969 r1)",
                 "bias",
                 "dark"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-2-PRL-67PCHURYUMOV-M08-V3.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-2-prl-67pchuryumov-m08-v3.0",
-            "description": "This CODMAC level 2 data set contains uncalibrated image data in DN unit, acquired by the OSIRIS Wide Angle Camera on the Rosetta spacecraft during the PRELANDING mission phase, covering the period from 2014-09-23T10:00:00.000 to 2014-10-24T09:59:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V3.0 supersedes previous deliveries of the same dataset with the following changes since the last version: Lien corrected dataset after the July and October 2018 PSA/PDS external peer reviews. Updated documentation and ancillary files, added document on bandpass filter. Updated SCIENCE_USER_GUIDE_V03.PDF to include one section about FAQ and one section about image data quality. Added shutter backtravel and readout issues to image quality map. Updated DATA_QUALITY_ID keyword in image header. Improved handling of images with missing packets. Included FITs files. Browse products changed to the same size as the original image.",
-            "title": "ROSETTA-ORBITER 67P OSIWAC 2 PRL-MTP008 EDR V3.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P OSIWAC 2 PRL-MTP008 EDR V3.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/65ZEOTLVV7EZ",
             "citation": "Kevin W. Bowman. 2023-06-10. TRPSDL2ALLCRSMGTOK. Version 1. TROPESS CrIS-SNPP L2 for Tokyo Megacity, Standard Product V1. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/65ZEOTLVV7EZ. https://disc.gsfc.nasa.gov/datacollection/TRPSDL2ALLCRSMGTOK_1.html. Digital Science Data.",
-            "issued": "2023-05-05",
-            "temporal": "2016-01-02T00:00:00Z/2023-06-12T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-05-05",
-            "references": [
-                "https://doi.org/10.1126/sciadv.abf7460"
-            ],
-            "keyword": [
-                "atmospheric water vapor",
-                "earth science",
-                "atmosphere",
-                "atmospheric chemistry",
-                "atmospheric temperature"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "KEVIN BOWMAN",
                 "hasEmail": "mailto:kevin.w.bowman@jpl.nasa.gov"
             },
+            "creator": "Kevin W. Bowman",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C2569842902-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "The TROPESS CrIS-SNPP L2 for Tokyo Megacity, Standard Product contains the vertical distribution of seven retrieved atmospheric gases (CH4, CO, H2O, HDO, NH3, O3 and PAN) and temperature, along with formal uncertainties measured by the CrIS instrument on the Suomi-NPP satellite. The forward stream standard product is centered on a 3x3 degree region over Tokyo for the time period from 2021-02-01 to present. The NASA TRopospheric Ozone and Precursors from Earth System Sounding (TROPESS) project, uses an optimal estimation algorithm, known as the MUlti-SpEctra, MUlti-SpEcies, Multi-SEnsors (MUSES).\n\nThe data files are written in the netCDF version 4 file format, and each file contains one day of data. The data have a spatial resolution of 14 km (CrIS nadir FOV), and are reported at 17 vertical levels from the surface to 0.1 hPa. The principal investigator for the TROPESS project is Kevin W. Bowman.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "TRPSDL2ALLCRSMGTOK",
-            "creator": "Kevin W. Bowman",
-            "graphic-preview-description": "TROPESS CrIS-SNPP Tokyo Megacity (Forward Stream, Standard Product) CH4 at 681 hPa on 01 July 2020.",
-            "title": "TROPESS CrIS-SNPP L2 for Tokyo Megacity, Standard Product V1 (TRPSDL2ALLCRSMGTOK) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TROPESS/images/TRPSDL2ALLCRSMGTOK_Sample.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2F65ZEOTLVV7EZ",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2F65ZEOTLVV7EZ",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TROPESS/images/TRPSDL2ALLCRSMGTOK_Sample.png",
-                    "description": "TROPESS CrIS-SNPP Tokyo Megacity (Forward Stream, Standard Product) CH4 at 681 hPa on 01 July 2020.",
                     "@type": "dcat:Distribution",
+                    "description": "TROPESS CrIS-SNPP Tokyo Megacity (Forward Stream, Standard Product) CH4 at 681 hPa on 01 July 2020.",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TROPESS/images/TRPSDL2ALLCRSMGTOK_Sample.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/TRPSDL2ALLCRSMGTOK_1.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/TRPSDL2ALLCRSMGTOK_1.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/data/TROPESS_MegaCities_Standard/TRPSDL2ALLCRSMGTOK.1/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/data/TROPESS_MegaCities_Standard/TRPSDL2ALLCRSMGTOK.1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=TRPSDL2ALLCRSMGTOK_1",
-                    "description": "Use the Earthdata Search Client to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search Client to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=TRPSDL2ALLCRSMGTOK_1",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/opendap/TROPESS_MegaCities_Standard/TRPSDL2ALLCRSMGTOK.1/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/opendap/TROPESS_MegaCities_Standard/TRPSDL2ALLCRSMGTOK.1/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/data/TROPESS_MegaCities_Standard/TRPSDL2ALLCRSMGTOK.1/doc/TROPESS_Forward_Stream_README.pdf",
-                    "description": "README Document",
                     "@type": "dcat:Distribution",
+                    "description": "README Document",
+                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/data/TROPESS_MegaCities_Standard/TRPSDL2ALLCRSMGTOK.1/doc/TROPESS_Forward_Stream_README.pdf",
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
+            "graphic-preview-description": "TROPESS CrIS-SNPP Tokyo Megacity (Forward Stream, Standard Product) CH4 at 681 hPa on 01 July 2020.",
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TROPESS/images/TRPSDL2ALLCRSMGTOK_Sample.png",
+            "identifier": "C2569842902-GES_DISC",
+            "issued": "2023-05-05",
+            "keyword": [
+                "atmospheric water vapor",
+                "earth science",
+                "atmosphere",
+                "atmospheric chemistry",
+                "atmospheric temperature"
+            ],
+            "landingPage": "https://doi.org/10.5067/65ZEOTLVV7EZ",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2023-05-05",
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
+            "series-name": "TRPSDL2ALLCRSMGTOK",
             "spatial": "138.0 34.0 141.0 37.0",
+            "temporal": "2016-01-02T00:00:00Z/2023-06-12T00:00:00Z",
             "theme": [
                 "TROPESS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "TROPESS CrIS-SNPP L2 for Tokyo Megacity, Standard Product V1 (TRPSDL2ALLCRSMGTOK) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1206500991-ASF.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, ASF.",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "undefined",
+                "hasEmail": "mailto:uso@asf.alaska.edu"
+            },
+            "description": "SEASAT Image Level 1",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "Vertex, the ASF search and download interface",
+                    "downloadURL": "https://vertex.daac.asf.alaska.edu/",
+                    "mediaType": "text/html",
+                    "title": "Download this dataset"
+                }
+            ],
+            "identifier": "C1206500991-ASF",
             "issued": "2013-06-27",
-            "temporal": "1978-07-04T12:05:47Z/1978-10-11T01:29:10Z",
-            "@type": "dcat:Dataset",
-            "modified": "2013-09-12",
             "keyword": [
                 "ocean waves",
                 "land surface",
@@ -798224,121 +798236,90 @@
                 "ocean winds",
                 "oceans"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "undefined",
-                "hasEmail": "mailto:uso@asf.alaska.edu"
-            },
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1206500991-ASF.html",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2013-09-12",
+            "programCode": [
+                "026:001"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "ASF"
             },
-            "identifier": "C1206500991-ASF",
-            "description": "SEASAT Image Level 1",
-            "title": "SEASAT_SAR_LEVEL1_HDF5",
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
             "spatial": "<?xml version=\"1.0\" encoding=\"UTF-8\"?><gml:Polygon xmlns:gml=\"http://www.opengis.net/gml/3.2\" srsName=\"EPSG:4326\"><gml:outerBoundaryIs><gml:LinearRing><gml:posList>64.472794 30.9375 74.959392 -15.46875 77.235074 -94.570312 75.497157 -168.398438 72.395706 164.882812 64.472794 156.796875 53.540307 163.125 21.943046 -143.085938 2.811371 -88.242188 3.162456 -72.070312 24.20689 -15.117188 33.72434 14.765625 38.272689 21.445312 64.472794 30.9375</gml:posList></gml:LinearRing></gml:outerBoundaryIs><gml:innerBoundaryIs></gml:innerBoundaryIs></gml:Polygon>",
+            "temporal": "1978-07-04T12:05:47Z/1978-10-11T01:29:10Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "SEASAT_SAR_LEVEL1_HDF5"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=DI%2FEAR-C-I0034-3-UH22M-TMPL1-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This data set includes calibrated images of Deep Impact mission target comet 9P/Tempel 1 taken from November 1997 through July 1999 using the University of Hawaii, 2.24 meter telescope and a Tektronics 2048x2048 CCD. Observations were made using the facility BVRI broadband filters. All data reductions were performed using the Image Reduction and Analysis Facility (IRAF). Data have been flattened, bias subtracted, trimmed, overscan corrected and cleaned for cosmic rays. This data set also includes tables of astrometric measurements of 9P/Tempel 1 as well as calibration frames taken from 1997 and into 2000. This is an ongoing, cumulative data set; reduced images of 9P/Tempel 1 images taken from 2000 through 2005 at the UH2.2m telescope are expected to be added in the future.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.di-ear-c-i0034-3-uh22m-tmpl1-v1.0_g6e5-h7in",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "calibration",
                 "deep impact",
                 "support archives",
                 "9p/tempel 1 (1867 g1)"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=DI%2FEAR-C-I0034-3-UH22M-TMPL1-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.di-ear-c-i0034-3-uh22m-tmpl1-v1.0_g6e5-h7in",
-            "description": "This data set includes calibrated images of Deep Impact mission target comet 9P/Tempel 1 taken from November 1997 through July 1999 using the University of Hawaii, 2.24 meter telescope and a Tektronics 2048x2048 CCD. Observations were made using the facility BVRI broadband filters. All data reductions were performed using the Image Reduction and Analysis Facility (IRAF). Data have been flattened, bias subtracted, trimmed, overscan corrected and cleaned for cosmic rays. This data set also includes tables of astrometric measurements of 9P/Tempel 1 as well as calibration frames taken from 1997 and into 2000. This is an ongoing, cumulative data set; reduced images of 9P/Tempel 1 images taken from 2000 through 2005 at the UH2.2m telescope are expected to be added in the future.",
-            "title": "UH2.2M REDUCED 9P/TEMPEL 1 IMAGES/ASTROMETRY V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "UH2.2M REDUCED 9P/TEMPEL 1 IMAGES/ASTROMETRY V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/VLBI/vlbi_ngs_data_001",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, CDDIS. https://doi.org/10.5067/VLBI/vlbi_ngs_data_001.",
-            "issued": "2005-01-01",
-            "temporal": "2005-01-01T00:00:00Z/2024-12-09T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-12-05",
-            "keyword": [
-                "solid earth",
-                "coordinate reference system",
-                "earth science"
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
-            "identifier": "C2404965297-CDDIS",
             "description": "Very Long Baseline Interferometry (VLBI) ASCII files in the NGS card format. Very Long Baseline Interferometry (VLBI) auxiliary ASCII files provided by the International VLBI Service for Geodesy and Astrometry (IVS) include schedules, notes, and session log files.",
-            "title": "CDDIS VLBI NGS data",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FVLBI%2Fvlbi_ngs_data_001",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FVLBI%2Fvlbi_ngs_data_001",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
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
@@ -798354,466 +798335,497 @@
                     "title": "This dataset's landing page"
                 }
             ],
+            "identifier": "C2404965297-CDDIS",
+            "issued": "2005-01-01",
+            "keyword": [
+                "solid earth",
+                "coordinate reference system",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/VLBI/vlbi_ngs_data_001",
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
+            "temporal": "2005-01-01T00:00:00Z/2024-12-09T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "CDDIS VLBI NGS data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MGS-M-ACCEL-5-PROFILE-V1.1",
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
+            "description": "not applicable",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mgs-m-accel-5-profile-v1.1_g6gu-2ukk",
+            "issued": "2018-06-26",
+            "keyword": [
+                "mars global surveyor",
+                "mars"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MGS-M-ACCEL-5-PROFILE-V1.1",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mgs-m-accel-5-profile-v1.1_g6gu-2ukk",
-            "description": "not applicable",
-            "title": "MGS PROFILE DATA RECORDS V1.1",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "MGS PROFILE DATA RECORDS V1.1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1835",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Joiner, J., and Y. Yoshida. 2021. Global MODIS and FLUXNET-derived Daily Gross Primary Production, V2. ORNL DAAC, Oak Ridge, Tennessee, USA. https://doi.org/10.3334/ORNLDAAC/1835",
-            "issued": "2024-03-11",
-            "temporal": "2000-03-01T00:00:00Z/2020-08-01T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-09-30",
-            "keyword": [
-                "soils",
-                "national geospatial data asset",
-                "land surface",
-                "biosphere",
-                "ngda",
-                "earth science",
-                "vegetation",
-                "ecological dynamics",
-                "surface radiative properties"
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
-            "identifier": "C2764707175-ORNL_CLOUD",
             "description": "This dataset provides global gridded daily estimates of gross primary production (GPP) and uncertainties at 0.05-degree resolution for the period 2000-03-01 to the recent past. The GPP was derived from the MODerate-resolution Imaging Spectroradiometer (MODIS) instruments on the NASA Terra and Aqua satellites using the MCD43C4v006 Nadir Bidirectional Reflectance Distribution Function (BRDF)-Adjusted Reflectances (NBAR) product as input to neural networks that were used to globally upscale GPP estimated from selected FLUXNET 2015 eddy covariance tower sites. Additional data will be added periodically.",
-            "graphic-preview-description": "Gross primary production expressed as carbon (g m-2 d-1) for July 1st, 2019.",
-            "title": "Global MODIS and FLUXNET-derived Daily Gross Primary Production, V2",
-            "graphic-preview-file": "https://daac.ornl.gov/VEGETATION/guides/FluxSat_GPP_FPAR_Fig1.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1835",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1835",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/global_vegetation/FluxSat_GPP_FPAR/data/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/global_vegetation/FluxSat_GPP_FPAR/data/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/VEGETATION/guides/FluxSat_GPP_FPAR.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/VEGETATION/guides/FluxSat_GPP_FPAR.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1835",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1835",
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
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/global_vegetation/FluxSat_GPP_FPAR/comp/FluxSat_GPP_FPAR.pdf",
-                    "description": "Global MODIS and FLUXNET-derived Daily Gross Primary Production, V2: FluxSat_GPP_FPAR.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "Global MODIS and FLUXNET-derived Daily Gross Primary Production, V2: FluxSat_GPP_FPAR.pdf",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/global_vegetation/FluxSat_GPP_FPAR/comp/FluxSat_GPP_FPAR.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://daac.ornl.gov/VEGETATION/guides/FluxSat_GPP_FPAR_Fig1.png",
-                    "description": "Gross primary production expressed as carbon (g m-2 d-1) for July 1st, 2019.",
                     "@type": "dcat:Distribution",
+                    "description": "Gross primary production expressed as carbon (g m-2 d-1) for July 1st, 2019.",
+                    "downloadURL": "https://daac.ornl.gov/VEGETATION/guides/FluxSat_GPP_FPAR_Fig1.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://thredds.daac.ornl.gov/thredds/catalog/ornldaac/1835/catalog.html",
-                    "description": "The THREDDS location for this Collection.",
                     "@type": "dcat:Distribution",
+                    "description": "The THREDDS location for this Collection.",
+                    "downloadURL": "https://thredds.daac.ornl.gov/thredds/catalog/ornldaac/1835/catalog.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "graphic-preview-description": "Gross primary production expressed as carbon (g m-2 d-1) for July 1st, 2019.",
+            "graphic-preview-file": "https://daac.ornl.gov/VEGETATION/guides/FluxSat_GPP_FPAR_Fig1.png",
+            "identifier": "C2764707175-ORNL_CLOUD",
+            "issued": "2024-03-11",
+            "keyword": [
+                "soils",
+                "national geospatial data asset",
+                "land surface",
+                "biosphere",
+                "ngda",
+                "earth science",
+                "vegetation",
+                "ecological dynamics",
+                "surface radiative properties"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1835",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2024-09-30",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "ORNL_DAAC"
+            },
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2000-03-01T00:00:00Z/2020-08-01T23:59:59Z",
             "theme": [
                 "Vegetation",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Global MODIS and FLUXNET-derived Daily Gross Primary Production, V2"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/MODIS/MCD43D19.061",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Crystal Schaaf, Zhuosen Wang. 2021-02-22. MODIS/Terra+Aqua BRDF/Albedo Parameter1 Band7 Daily L3 Global 30ArcSec CMG V061. Sioux Falls, South Dakota, USA. Archived by National Aeronautics and Space Administration, U.S. Government, NASA EOSDIS Land Processes Distributed Active Archive Center. https://doi.org/10.5067/MODIS/MCD43D19.061. https://doi.org/10.5067/MODIS/MCD43D19.061. The DOI landing page provides citations in APA and Chicago styles..",
-            "issued": "2021-02-22",
-            "temporal": "2000-02-16T00:00:00Z/2024-05-20T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2021-02-22",
-            "keyword": [
-                "national geospatial data asset",
-                "surface radiative properties",
-                "earth science",
-                "ngda",
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
-            "identifier": "C2539907958-LPCLOUD",
-            "description": "The MCD43D19 Version 6.1 Bidirectional Reflectance Distribution Function and Albedo (BRDF/Albedo) Model Parameter dataset is produced daily using 16 days of Terra and Aqua Moderate Resolution Imaging Spectroradiometer (MODIS) data at 30 arc second (1,000 meter) resolution. Data are temporally weighted to the ninth day which is reflected in the Julian date in the file name. This Climate Modeling Grid (CMG) product covers the entire globe for use in climate simulation models. Due to the large file size, each MCD43D product contains just one data layer. Each of the three model parameters (isotropic, volumetric, and geometric) for each of the MODIS bands 1 through 7 and the visible, near infrared (NIR), and shortwave bands included in MCD43C1 (https://doi.org/10.5067/MODIS/MCD43C1.061) are stored in a separate file as MCD43D01 through MCD43D30. \r\n\r\nMCD43D19 is the BRDF isotropic parameter for MODIS band 7. The isotropic parameter, in conjunction with the volumetric and geometric parameters, is used to derive the BRDF/Albedo values for MODIS band 7. \r\n\r\nImprovements/Changes from Previous Versions\r\n\r\n* The Version 6.1 Level-1B (L1B) products have been improved by undergoing various calibration changes that include: changes to the response-versus-scan angle (RVS) approach that affects reflectance bands for Aqua and Terra MODIS, corrections to adjust for the optical crosstalk in Terra MODIS infrared (IR) bands, and corrections to the Terra MODIS forward look-up table (LUT) update for the period 2012 - 2017.\r\n* A polarization correction has been applied to the L1B Reflective Solar Bands (RSB).",
-            "release-place": "Sioux Falls, South Dakota, USA",
             "creator": "Crystal Schaaf, Zhuosen Wang",
-            "title": "MODIS/Terra+Aqua BRDF/Albedo Parameter1 Band7 Daily L3 Global 30ArcSec CMG V061",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The MCD43D19 Version 6.1 Bidirectional Reflectance Distribution Function and Albedo (BRDF/Albedo) Model Parameter dataset is produced daily using 16 days of Terra and Aqua Moderate Resolution Imaging Spectroradiometer (MODIS) data at 30 arc second (1,000 meter) resolution. Data are temporally weighted to the ninth day which is reflected in the Julian date in the file name. This Climate Modeling Grid (CMG) product covers the entire globe for use in climate simulation models. Due to the large file size, each MCD43D product contains just one data layer. Each of the three model parameters (isotropic, volumetric, and geometric) for each of the MODIS bands 1 through 7 and the visible, near infrared (NIR), and shortwave bands included in MCD43C1 (https://doi.org/10.5067/MODIS/MCD43C1.061) are stored in a separate file as MCD43D01 through MCD43D30. \r\n\r\nMCD43D19 is the BRDF isotropic parameter for MODIS band 7. The isotropic parameter, in conjunction with the volumetric and geometric parameters, is used to derive the BRDF/Albedo values for MODIS band 7. \r\n\r\nImprovements/Changes from Previous Versions\r\n\r\n* The Version 6.1 Level-1B (L1B) products have been improved by undergoing various calibration changes that include: changes to the response-versus-scan angle (RVS) approach that affects reflectance bands for Aqua and Terra MODIS, corrections to adjust for the optical crosstalk in Terra MODIS infrared (IR) bands, and corrections to the Terra MODIS forward look-up table (LUT) update for the period 2012 - 2017.\r\n* A polarization correction has been applied to the L1B Reflective Solar Bands (RSB).",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMODIS%2FMCD43D19.061",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMODIS%2FMCD43D19.061",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "application/x-hdf",
-                    "downloadURL": "https://e4ftl01.cr.usgs.gov/MOTA/MCD43D19.061/",
-                    "description": "LP DAAC Data Pool provides direct access to available products via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "LP DAAC Data Pool provides direct access to available products via HTTPS.",
+                    "downloadURL": "https://e4ftl01.cr.usgs.gov/MOTA/MCD43D19.061/",
+                    "mediaType": "application/x-hdf",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "application/x-hdf",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=C2539907958-LPCLOUD",
-                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=C2539907958-LPCLOUD",
+                    "mediaType": "application/x-hdf",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/MODIS/MCD43D19.061",
-                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
+                    "downloadURL": "https://doi.org/10.5067/MODIS/MCD43D19.061",
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
-                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/filespec/MODIS/61/MCD43D19",
-                    "description": "The File Specification provides a description of the product file including Scientific Data Sets and their attributes.",
                     "@type": "dcat:Distribution",
+                    "description": "The File Specification provides a description of the product file including Scientific Data Sets and their attributes.",
+                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/filespec/MODIS/61/MCD43D19",
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
-                    "downloadURL": "https://opendap.cr.usgs.gov/opendap/hyrax/DP137/MOTA/MCD43D19.061/contents.html",
-                    "description": "Access data via Open-source Project for a Network Data Access Protocol",
                     "@type": "dcat:Distribution",
+                    "description": "Access data via Open-source Project for a Network Data Access Protocol",
+                    "downloadURL": "https://opendap.cr.usgs.gov/opendap/hyrax/DP137/MOTA/MCD43D19.061/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 }
             ],
+            "identifier": "C2539907958-LPCLOUD",
+            "issued": "2021-02-22",
+            "keyword": [
+                "national geospatial data asset",
+                "surface radiative properties",
+                "earth science",
+                "ngda",
+                "land surface"
+            ],
+            "landingPage": "https://doi.org/10.5067/MODIS/MCD43D19.061",
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
+            "title": "MODIS/Terra+Aqua BRDF/Albedo Parameter1 Band7 Daily L3 Global 30ArcSec CMG V061"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-MIRO-4-ESC3-67P-V1.0",
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
+            "description": "This data set contains Spectroscopic and Continuum level 4 data, in the form of table files, taken during the ROSETTA ESCORT 3 phase of the Rosetta mission to comet 67P/CHURYUMOV-GERASIMENKO by the MIRO instrument.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-miro-4-esc3-67p-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-MIRO-4-ESC3-67P-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-miro-4-esc3-67p-v1.0",
-            "description": "This data set contains Spectroscopic and Continuum level 4 data, in the form of table files, taken during the ROSETTA ESCORT 3 phase of the Rosetta mission to comet 67P/CHURYUMOV-GERASIMENKO by the MIRO instrument.",
-            "title": "ROSETTA-ORBITER 67P MIRO 4 ESC3 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P MIRO 4 ESC3 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ASDC/SUBORBITAL/DISCOVERAQ_Texas_Ground_Pandora_Data_1",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2022-08-22. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/ASDC/SUBORBITAL/DISCOVERAQ_Texas_Ground_Pandora_Data_1.",
-            "issued": "2021-08-19",
-            "temporal": "2012-03-10T00:00:00Z/2013-10-03T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-08-22",
-            "keyword": [
-                "atmosphere",
-                "atmospheric chemistry",
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
-            "identifier": "C2417019649-LARC_ASDC",
             "description": "DISCOVERAQ_Texas_Ground_Pandora_Data contains all of the Pandora instrumentation data collected during the Texas (Houston) deployment of NASA's DISCOVER-AQ field study. Contained in this dataset are column measurements of NO2 and O3. Pandoras were situated at various ground sites across the study area, including Channelview, Conroe, Deer Park, Galveston, Harris County, LaPorte Airport, Manvel Croix, Moody Tower, Seabrook Park, Smith Point, and West Houston. This data product contains only data from the Texas deployment and data collection is complete.\r\n\r\nUnderstanding the factors that contribute to near surface pollution is difficult using only satellite-based observations. The incorporation of surface-level measurements from aircraft and ground-based platforms provides the crucial information necessary to validate and expand upon the use of satellites in understanding near surface pollution. Deriving Information on Surface conditions from Column and Vertically Resolved Observations Relevant to Air Quality (DISCOVER-AQ) was a four-year campaign conducted in collaboration between NASA Langley Research Center, NASA Goddard Space Flight Center, NASA Ames Research Center, and multiple universities to improve the use of satellites to monitor air quality for public health and environmental benefit. Through targeted airborne and ground-based observations, DISCOVER-AQ enabled more effective use of current and future satellites to diagnose ground level conditions influencing air quality.\r\n\r\nDISCOVER-AQ employed two NASA aircraft, the P-3B and King Air, with the P-3B completing in-situ spiral profiling of the atmosphere (aerosol properties, meteorological variables, and trace gas species). The King Air conducted both passive and active remote sensing of the atmospheric column extending below the aircraft to the surface. Data from an existing network of surface air quality monitors, AERONET sun photometers, Pandora UV/vis spectrometers and model simulations were also collected. Further, DISCOVER-AQ employed many surface monitoring sites, with measurements being made on the ground, in conjunction with the aircraft. The B200 and P-3B conducted flights in Baltimore-Washington, D.C. in 2011, Houston, TX in 2013, San Joaquin Valley, CA in 2013, and Denver, CO in 2014. These regions were targeted due to being in violation of the National Ambient Air Quality Standards (NAAQS).\r\n\r\nThe first objective of DISCOVER-AQ was to determine and investigate correlations between surface measurements and satellite column observations for the trace gases ozone (O3), nitrogen dioxide (NO2), and formaldehyde (CH2O) to understand how satellite column observations can diagnose surface conditions. DISCOVER-AQ also had the objective of using surface-level measurements to understand how satellites measure diurnal variability and to understand what factors control diurnal variability. Lastly, DISCOVER-AQ aimed to explore horizontal scales of variability, such as regions with steep gradients and urban plumes.",
-            "title": "DISCOVER-AQ Texas Deployment Pandora Column Observations",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC%2FSUBORBITAL%2FDISCOVERAQ_Texas_Ground_Pandora_Data_1",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC%2FSUBORBITAL%2FDISCOVERAQ_Texas_Ground_Pandora_Data_1",
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
-                    "downloadURL": "https://doi.org/10.5067/ASDC/SUBORBITAL/DISCOVERAQ_Texas_Ground_Pandora_Data_1",
-                    "description": "DOI for DISCOVERAQ_Texas_Ground_Pandora_Data_1",
                     "@type": "dcat:Distribution",
+                    "description": "DOI for DISCOVERAQ_Texas_Ground_Pandora_Data_1",
+                    "downloadURL": "https://doi.org/10.5067/ASDC/SUBORBITAL/DISCOVERAQ_Texas_Ground_Pandora_Data_1",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2417019649-LARC_ASDC",
-                    "description": "Earthdata Search client for DISCOVERAQ_Texas_Ground_Pandora_Data_1",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search client for DISCOVERAQ_Texas_Ground_Pandora_Data_1",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2417019649-LARC_ASDC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/DISCOVER-AQ/Texas_Ground_Pandora_Data_1/",
-                    "description": "ASDC Direct Data Download for DISCOVERAQ_Texas_Ground_Pandora_Data_1",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for DISCOVERAQ_Texas_Ground_Pandora_Data_1",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/DISCOVER-AQ/Texas_Ground_Pandora_Data_1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 }
             ],
+            "identifier": "C2417019649-LARC_ASDC",
+            "issued": "2021-08-19",
+            "keyword": [
+                "atmosphere",
+                "atmospheric chemistry",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/ASDC/SUBORBITAL/DISCOVERAQ_Texas_Ground_Pandora_Data_1",
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
             "spatial": "<?xml version=\"1.0\" encoding=\"UTF-8\"?><gml:Polygon xmlns:gml=\"http://www.opengis.net/gml/3.2\" srsName=\"EPSG:9825\"><gml:outerBoundaryIs><gml:LinearRing><gml:posList>23.0 -120.0 23.0 96.0 43.0 96.0 43.0 -120.0 23.0 -120.0</gml:posList></gml:LinearRing></gml:outerBoundaryIs><gml:innerBoundaryIs></gml:innerBoundaryIs></gml:Polygon>",
+            "temporal": "2012-03-10T00:00:00Z/2013-10-03T23:59:59.999Z",
             "theme": [
                 "DISCOVER-AQ",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "DISCOVER-AQ Texas Deployment Pandora Column Observations"
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
+                    "downloadURL": "http://fermi.gsfc.nasa.gov/ssc/data/access/lat/1FHL/LAT_extended_sources_v12.tar",
+                    "mediaType": "application/x-tar"
+                }
+            ],
+            "identifier": "NASA-0000220__5",
             "issued": "2018-06-25",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
             "keyword": [
                 "acd",
                 "gro",
@@ -798831,63 +798843,32 @@
                 "energy",
                 "compton"
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
-            "identifier": "NASA-0000220__5",
-            "description": "This catalog of LAT sources above 10 GeV reports the locations, spectra, and variability properties of the 514 sources significantly detected in this range during the first three years of the Fermi mission. Many of these sources are already included in the 2FGL catalog, although in that catalog their characterization is dominated by the much larger numbers of gamma rays detected in the energy range 0.1 to 10 GeV.",
-            "title": "First Fermi-LAT Catalog of Sources above 10 GeV (1FHL)",
-            "programCode": [
-                "026:014"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://fermi.gsfc.nasa.gov/ssc/data/access/lat/1FHL/LAT_extended_sources_v12.tar",
-                    "mediaType": "application/x-tar"
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
-            "landingPage": "https://data.nasa.gov/d/g6w2-43cq",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2023-05-09",
-            "@type": "dcat:Dataset",
-            "modified": "2023-09-11",
-            "keyword": [
-                "cloud radiative effect",
-                "modis",
-                "cloud regime",
-                "clouds"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Daeho Jin",
                 "hasEmail": "mailto:Daeho.Jin@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Daeho Jin"
-            },
-            "identifier": "https://data.nasa.gov/api/views/g6w2-43cq",
             "description": "Cloud-only regimes (and 3 sub-regimes of CR15) originally derived from Terra and Aqua observations in 50S-50N, and corresponding \"regime numbers on map\" files assigned to 60S-60N domain are provided (see Jin et al. 2021, doi: 10.1175/JAMC-D-20-0253.1). \nThe zip file also includes sample python codes to calculate regime mean SWCRE/LWCRE for the study of observational CRE feedback (Jin et al. 2023, J. of Climate, submitted).",
-            "title": "Cloud Regime for CRE Feedback Study",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -798895,551 +798876,572 @@
                     "mediaType": "application/zip"
                 }
             ],
+            "identifier": "https://data.nasa.gov/api/views/g6w2-43cq",
+            "issued": "2023-05-09",
+            "keyword": [
+                "cloud radiative effect",
+                "modis",
+                "cloud regime",
+                "clouds"
+            ],
+            "landingPage": "https://data.nasa.gov/d/g6w2-43cq",
+            "modified": "2023-09-11",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Daeho Jin"
+            },
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "Cloud Regime for CRE Feedback Study"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC1-0601-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 1 phase 2014-11-20 to 2015-03-10. It is a Global Gravity measurement at the comet 67P and covers the time 2015-02-24T22:26:50.000 to 2015-02-25T00:19:10.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc1-0601-v1.0_g6wn-yaj4",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC1-0601-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc1-0601-v1.0_g6wn-yaj4",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 1 phase 2014-11-20 to 2015-03-10. It is a Global Gravity measurement at the comet 67P and covers the time 2015-02-24T22:26:50.000 to 2015-02-25T00:19:10.000.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 1 0601 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 1 0601 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/GPMGV/GCPEX/ADMIRARI/DATA201",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Saavedra, Pablo, Alessandro Battaglia and Pablo Saavedra.2014. GPM GROUND VALIDATION ADVANCED MICROWAVE RADIOMETER RAIN IDENTIFICATION (ADMIRARI) GCPEX [indicate subset used]. Dataset available online from the NASA Global Hydrometeorology Resource Center DAAC, Huntsville, Alabama, U.S.A. DOI: http://dx.doi.org/10.5067/GPMGV/GCPEX/ADMIRARI/DATA201",
-            "issued": "2014-06-03",
-            "temporal": "2012-01-14T00:00:00Z/2012-02-29T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-05-20",
-            "keyword": [
-                "earth science",
-                "clouds",
-                "atmosphere",
-                "radar",
-                "spectral/engineering",
-                "lidar",
-                "microwave"
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
-            "identifier": "C1979126099-GHRC_DAAC",
             "description": "The GPM Ground Validation Advanced Microwave Radiometer Rain Identification (ADMIRARI) GCPEx dataset measures brightness temperature at three frequencies (10.7, 21.0 and 36.5 GHz) and at two polarized planes (H & V). The ADMIRIRI retrieval typically provides rain/cloud liquid water path (LWP) and integrated water vapor, and for low water content cases it provides the total LWP and integrated water vapor. The ADMIRARI is a scanning radiometer like its auxiliary active instruments, which include a Micro Rain Radar (MRR) and a cloud lidar, which provide reflectivity profiles and cloud base altitude at the same scanning angle as the ADMIRIRI. This data was collected during the GPM Cold-season Precipitation Experiment (GCPEx) located in Ontario, Canada, January 14, 2012 through February 29, 2012. Reference: http://www2.meteo.uni-bonn.de/admirari.",
-            "graphic-preview-description": "N/A",
-            "title": "GPM GROUND VALIDATION ADVANCED MICROWAVE RADIOMETER RAIN IDENTIFICATION (ADMIRARI) GCPEX V1",
-            "graphic-preview-file": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/gcpex/admirari/browse/",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGPMGV%2FGCPEX%2FADMIRARI%2FDATA201",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGPMGV%2FGCPEX%2FADMIRARI%2FDATA201",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=gpmadmirgcpex",
-                    "description": "Files may be downloaded directly to your workstation from this link",
                     "@type": "dcat:Distribution",
+                    "description": "Files may be downloaded directly to your workstation from this link",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=gpmadmirgcpex",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/gcpex/admirari/browse/gcpex_admirari_20120127_H00_24.png",
-                    "description": "Sample browse image",
                     "@type": "dcat:Distribution",
+                    "description": "Sample browse image",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/gcpex/admirari/browse/gcpex_admirari_20120127_H00_24.png",
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
-                    "downloadURL": "http://ghrc.nsstc.nasa.gov/uso/ds_docs/gpmgv/gcpex/gpmadmirgcpex/gpmadmirgcpex_dataset.html",
-                    "description": "The guide document contains detailed information about the dataset",
                     "@type": "dcat:Distribution",
+                    "description": "The guide document contains detailed information about the dataset",
+                    "downloadURL": "http://ghrc.nsstc.nasa.gov/uso/ds_docs/gpmgv/gcpex/gpmadmirgcpex/gpmadmirgcpex_dataset.html",
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
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/gcpex/admirari/browse/",
-                    "description": "N/A",
                     "@type": "dcat:Distribution",
+                    "description": "N/A",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/gcpex/admirari/browse/",
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
+            "graphic-preview-file": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/gcpex/admirari/browse/",
+            "identifier": "C1979126099-GHRC_DAAC",
+            "issued": "2014-06-03",
+            "keyword": [
+                "earth science",
+                "clouds",
+                "atmosphere",
+                "radar",
+                "spectral/engineering",
+                "lidar",
+                "microwave"
+            ],
+            "landingPage": "https://doi.org/10.5067/GPMGV/GCPEX/ADMIRARI/DATA201",
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
             "spatial": "-79.82 44.18 -79.73 44.29",
+            "temporal": "2012-01-14T00:00:00Z/2012-02-29T23:59:59Z",
             "theme": [
                 "GCPEx",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "GPM GROUND VALIDATION ADVANCED MICROWAVE RADIOMETER RAIN IDENTIFICATION (ADMIRARI) GCPEX V1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-4-ESC3-67P-M21-INFLDSTR-V1.0",
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
+            "description": "This CODMAC level 4 data set contains solar stray-light corrected, in-field stray-light corrected,  radiometric calibrated and geometric distortion corrected  (resampled) image data in W/m^2/sr/nm,  acquired by the OSIRIS Wide Angle Camera on the Rosetta spacecraft  during the COMET ESCORT 3 mission phase, covering the period  from 2015-09-22T23:25:00.000 to 2015-10-20T23:24:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V1.0 is the first version of this dataset: Lien corrected dataset after September 2019 PSA/PDS external peer review.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-4-esc3-67p-m21-infldstr-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-4-ESC3-67P-M21-INFLDSTR-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-4-esc3-67p-m21-infldstr-v1.0",
-            "description": "This CODMAC level 4 data set contains solar stray-light corrected, in-field stray-light corrected,  radiometric calibrated and geometric distortion corrected  (resampled) image data in W/m^2/sr/nm,  acquired by the OSIRIS Wide Angle Camera on the Rosetta spacecraft  during the COMET ESCORT 3 mission phase, covering the period  from 2015-09-22T23:25:00.000 to 2015-10-20T23:24:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V1.0 is the first version of this dataset: Lien corrected dataset after September 2019 PSA/PDS external peer review.",
-            "title": "ROSETTA-ORBITER 67P OSIWAC 4 ESC3-MTP021 RDR-INFLDSTR V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P OSIWAC 4 ESC3-MTP021 RDR-INFLDSTR V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/R3WIYZO7YU82",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "CLPX-Ground: Ground-Based Frequency Modulated Continuous Wave (FMCW) Radar, Version 1. Version 1. Archived by National Aeronautics and Space Administration, U.S. Government, NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/R3WIYZO7YU82.",
-            "issued": "2002-02-19",
-            "temporal": "2002-02-19T00:00:00Z/2003-03-29T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2003-03-29",
-            "keyword": [
-                "cryosphere",
-                "spectral/engineering",
-                "snow/ice",
-                "radar",
-                "earth science"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "undefined",
                 "hasEmail": "mailto:nsidc@nsidc.org"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA NSIDC DAAC"
-            },
-            "identifier": "C1386203912-NSIDCV0",
             "description": "This data set is comprised of FMCW radar measurements, which are sensitive to electromagnetic discontinuities in the snowpack made during the 2002 and 2003 Cold Land Processes Field Experiment (CLPX).",
-            "title": "CLPX-Ground: Ground-Based Frequency Modulated Continuous Wave (FMCW) Radar, Version 1",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FR3WIYZO7YU82",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FR3WIYZO7YU82",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/CLP/data/ground_data/nsidc0164_lsos_fmcw/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/CLP/data/ground_data/nsidc0164_lsos_fmcw/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/CLP/data/ground_data/nsidc0164_lsos_fmcw/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/CLP/data/ground_data/nsidc0164_lsos_fmcw/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/CLP/data/ground_data/nsidc0164_lsos_fmcw/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/CLP/data/ground_data/nsidc0164_lsos_fmcw/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/R3WIYZO7YU82",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/R3WIYZO7YU82",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/R3WIYZO7YU82",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/R3WIYZO7YU82",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C1386203912-NSIDCV0",
+            "issued": "2002-02-19",
+            "keyword": [
+                "cryosphere",
+                "spectral/engineering",
+                "snow/ice",
+                "radar",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/R3WIYZO7YU82",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2003-03-29",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA NSIDC DAAC"
+            },
             "spatial": "-106.6788 39.828 -105.7681 40.6449",
+            "temporal": "2002-02-19T00:00:00Z/2003-03-29T23:59:59.999Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "CLPX-Ground: Ground-Based Frequency Modulated Continuous Wave (FMCW) Radar, Version 1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/GPMGV/OLYMPEX/COSMIR/DATA301",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Kroodsma, Rachael A. and Matthew A. Fritts.2017. GPM Ground Validation Conical Scanning Millimeter-wave Imaging Radiometer (CoSMIR) OLYMPEX [indicate subset used]. Dataset available online from the NASA Global Hydrometeorology Resource Center DAAC, Huntsville, Alabama, U.S.A. DOI: http://dx.doi.org/10.5067/GPMGV/OLYMPEX/COSMIR/DATA301",
-            "issued": "2017-09-15",
-            "temporal": "2015-11-05T00:00:00Z/2015-12-19T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-05-18",
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
-            "identifier": "C1979138680-GHRC_DAAC",
             "description": "The GPM Ground Validation Conical Scanning Millimeter-wave Imaging Radiometer (CoSMIR) OLYMPEX dataset consists of brightness temperatures from 9 channels as measured by CoSMIR when flown on the NASA DC-8 aircraft during the Global Precipitation Mission (GPM) Olympic Mountains Experiment (OLYMPEX) campaign. CoSMIR is a conical and cross-track scanning radiometer with frequencies centered at 50.3, 52.8, 89.0, 165.5, 183.31+/-1, 183.31+/-3, and 183.31+/-7 GHz.  Data files are available from November 5, 2015 thru December 19, 2015 in HDF-5 format, with browse imagery files in PNG format containing brightness temperature time series plots.",
-            "graphic-preview-description": "Sample Browse Image",
-            "title": "GPM Ground Validation Conical Scanning Millimeter-wave Imaging Radiometer (CoSMIR) OLYMPEX V1",
-            "graphic-preview-file": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/olympex/CoSMIR/browse/Conical_20151205.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGPMGV%2FOLYMPEX%2FCOSMIR%2FDATA301",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGPMGV%2FOLYMPEX%2FCOSMIR%2FDATA301",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=gpmcosmirolyx",
-                    "description": "Files may be downloaded directly to your workstation from this link",
                     "@type": "dcat:Distribution",
+                    "description": "Files may be downloaded directly to your workstation from this link",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=gpmcosmirolyx",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/olympex/CoSMIR/browse/Conical_20151205.png",
-                    "description": "Sample Browse Image",
                     "@type": "dcat:Distribution",
+                    "description": "Sample Browse Image",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/olympex/CoSMIR/browse/Conical_20151205.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://dx.doi.org/10.5067/GPMGV/OLYMPEX/DATA101",
-                    "description": "OLYMPEX Field Campaign Collection DOI",
                     "@type": "dcat:Distribution",
+                    "description": "OLYMPEX Field Campaign Collection DOI",
+                    "downloadURL": "http://dx.doi.org/10.5067/GPMGV/OLYMPEX/DATA101",
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
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/olympex/CoSMIR/doc/gpmcosmirolyx_dataset.pdf",
-                    "description": "The guide document contains detailed information about the dataset",
                     "@type": "dcat:Distribution",
+                    "description": "The guide document contains detailed information about the dataset",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/olympex/CoSMIR/doc/gpmcosmirolyx_dataset.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/olympex/CoSMIR/doc/readme_cosmir_olympex.txt",
-                    "description": "OLYMPEX CoSMIR data ReadMe file",
                     "@type": "dcat:Distribution",
+                    "description": "OLYMPEX CoSMIR data ReadMe file",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/olympex/CoSMIR/doc/readme_cosmir_olympex.txt",
+                    "mediaType": "text/html",
                     "title": "View the primary investigator's documentation for this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.1109/TGRS.2012.2200690",
-                    "description": "Observations of Storm Signatures by the Recently Modified Conical Scanning Millimeter-Wave Imaging Radiometer",
                     "@type": "dcat:Distribution",
+                    "description": "Observations of Storm Signatures by the Recently Modified Conical Scanning Millimeter-Wave Imaging Radiometer",
+                    "downloadURL": "https://doi.org/10.1109/TGRS.2012.2200690",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.1109/TGRS.2006.885410",
-                    "description": "Airborne CoSMIR Observations Between 50 and 183 GHz over Snow-Covered Sierra Mountains",
                     "@type": "dcat:Distribution",
+                    "description": "Airborne CoSMIR Observations Between 50 and 183 GHz over Snow-Covered Sierra Mountains",
+                    "downloadURL": "https://doi.org/10.1109/TGRS.2006.885410",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.1109/TGRS.2007.904038",
-                    "description": "A comparison of Near Concurrent Measurements from the SSMIS and CoSMIR for some Selected Channels over the Frequency Range of 50-183 GHz",
                     "@type": "dcat:Distribution",
+                    "description": "A comparison of Near Concurrent Measurements from the SSMIS and CoSMIR for some Selected Channels over the Frequency Range of 50-183 GHz",
+                    "downloadURL": "https://doi.org/10.1109/TGRS.2007.904038",
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
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/home/about-ghrc/citing-ghrc-daac-data",
-                    "description": "Instructions for citing GHRC data",
                     "@type": "dcat:Distribution",
+                    "description": "Instructions for citing GHRC data",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/home/about-ghrc/citing-ghrc-daac-data",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "graphic-preview-description": "Sample Browse Image",
+            "graphic-preview-file": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/olympex/CoSMIR/browse/Conical_20151205.png",
+            "identifier": "C1979138680-GHRC_DAAC",
+            "issued": "2017-09-15",
+            "keyword": [
+                "spectral/engineering",
+                "microwave",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/GPMGV/OLYMPEX/COSMIR/DATA301",
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
             "spatial": "-129.622 29.9313 -117.697 49.7371",
+            "temporal": "2015-11-05T00:00:00Z/2015-12-19T23:59:59Z",
             "theme": [
                 "OLYMPEX",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "GPM Ground Validation Conical Scanning Millimeter-wave Imaging Radiometer (CoSMIR) OLYMPEX V1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MGN-V-RDRS-5-MIDR-C3-V1.0",
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
+            "description": "This data set contains the Magellan Compressed Thrice Mosaicked Image Data Records (C3-MIDRs) which consists of mosaics generated by computing 3x3 pixel arithmetic moving averages from the C2-MIDRs. Each C3-MIDR is in a sinusoidal equal area projection and has an origin at 0 degrees latitude, with the central meridian defined as the longitude bisecting the mosaic. Each C1-MIDR has 7168 lines (aligned with latitudes) and 8192 samples, arranged as 56 1024 x 1024 files on CD-ROM. C3-MIDRs, with their 2.025 km pixel widths, are designed to cover the planet at reasonably high resolution and high signal to noise ratio. The 1024 x 1024 files have a VICAR2 format, with embedded VICAR2 labels. The data have been placed on CD-ROMs with documentation, detached Planetary Data System labels, and summary tabular information.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mgn-v-rdrs-5-midr-c3-v1.0_g756-bpn8",
+            "issued": "2021-05-21",
+            "keyword": [
+                "magellan",
+                "venus"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MGN-V-RDRS-5-MIDR-C3-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mgn-v-rdrs-5-midr-c3-v1.0_g756-bpn8",
-            "description": "This data set contains the Magellan Compressed Thrice Mosaicked Image Data Records (C3-MIDRs) which consists of mosaics generated by computing 3x3 pixel arithmetic moving averages from the C2-MIDRs. Each C3-MIDR is in a sinusoidal equal area projection and has an origin at 0 degrees latitude, with the central meridian defined as the longitude bisecting the mosaic. Each C1-MIDR has 7168 lines (aligned with latitudes) and 8192 samples, arranged as 56 1024 x 1024 files on CD-ROM. C3-MIDRs, with their 2.025 km pixel widths, are designed to cover the planet at reasonably high resolution and high signal to noise ratio. The 1024 x 1024 files have a VICAR2 format, with embedded VICAR2 labels. The data have been placed on CD-ROMs with documentation, detached Planetary Data System labels, and summary tabular information.",
-            "title": "MGN V RADAR SYSTEM DERIVED MIDR COMPRESSED THRICE V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "MGN V RADAR SYSTEM DERIVED MIDR COMPRESSED THRICE V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/803",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Busing, R.T., and T. Fujimori. 2013. NPP Temperate Forest: Humboldt Redwoods State Park, California, USA, 1972-2001, R1. ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/803",
-            "issued": "2023-10-05",
-            "temporal": "1972-01-01T00:00:00Z/2001-12-31T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-10-05",
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
-            "identifier": "C2755668336-ORNL_CLOUD",
             "description": "This data set contains site characteristics, stand descriptors, and measured and calculated above-ground biomass, above-ground net primary production (ANPP), and woody detritus input data for an old Sequoia sempervirens stand at Bull Creek in Humboldt Redwoods State Park, California. There is one data file (.csv format) with this data set. Productivity of the Sequoia stand was studied via tree re-measurement (1972 and 2001) and allometric relationships. Measurements of tree circumference at 1.7 m above ground were made at the beginning and the end of the study. A 1972 stem map of the stand allowed the investigators to identify and re-measure trees >10 cm in diameter. ANPP was estimated using a range of specific gravities and several allometric relationships for tree volume. Estimation procedures were outlined by Busing and Fujimori (2005). Tree loss to mortality over the study interval was included in the analysis. Estimates of total tree ANPP ranged from 600 to 1,400 g/m2/yr. However, ANPP values in the range of 700-1,000 g/m2/yr were considered to be the most reasonable estimate because of the accuracy of the particular equations, specific gravities, and assumptions used to obtain them (Busing and Fujimori, 2005). Above-ground total tree biomass was extremely high (> 300,000 g/m2). Revision Notes: Only the documentation for this data set has been modified. The data files have been checked for accuracy and are identical to those originally published in 2005.",
-            "graphic-preview-description": "Browse Image",
-            "title": "NPP Temperate Forest: Humboldt Redwoods State Park, California, USA, 1972-2001, R1",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/npp_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F803",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F803",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/npp/temperate_forest/NPP_REDWOOD/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/npp/temperate_forest/NPP_REDWOOD/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/NPP/guides/NPP_REDWOOD.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/NPP/guides/NPP_REDWOOD.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/803",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/803",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/npp/temperate_forest/NPP_REDWOOD/comp/NPP_REDWOOD.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/npp/temperate_forest/NPP_REDWOOD/comp/NPP_REDWOOD.pdf",
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
+            "identifier": "C2755668336-ORNL_CLOUD",
+            "issued": "2023-10-05",
+            "keyword": [
+                "biosphere",
+                "vegetation",
+                "ecological dynamics",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/803",
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
             "spatial": "40.35 -123.0",
+            "temporal": "1972-01-01T00:00:00Z/2001-12-31T23:59:59Z",
             "theme": [
                 "NPP",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "NPP Temperate Forest: Humboldt Redwoods State Park, California, USA, 1972-2001, R1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=DAWN-X-FC1-3-RDR-CRUISE-IMAGES-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "Abstract                                                                   ========                                                                   Framing Camera 1 is one of two identical units flying on Dawn            spacecraft. This dataset includes the Reduced Data Record (RDR) version  of all available images acquired during the initial checkout and         pre-Vesta cruise phases (Checkout, Earth to Mars, and Mars to Vesta).    As in the original Raw data sets, in addition to the imagery, ancillary  information is stored within the image headers, as well as a detailed    account of all the reference files used for the calibration. Calibration files needed for further processing are archived as a separate data set.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.dawn-x-fc1-3-rdr-cruise-images-v1.0_g774-n699",
             "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "dawn mission to vesta and ceres",
                 "20 cephei",
@@ -799449,266 +799451,244 @@
                 "epsilon geminorum",
                 "42 pegasi"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=DAWN-X-FC1-3-RDR-CRUISE-IMAGES-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.dawn-x-fc1-3-rdr-cruise-images-v1.0_g774-n699",
-            "description": "Abstract                                                                   ========                                                                   Framing Camera 1 is one of two identical units flying on Dawn            spacecraft. This dataset includes the Reduced Data Record (RDR) version  of all available images acquired during the initial checkout and         pre-Vesta cruise phases (Checkout, Earth to Mars, and Mars to Vesta).    As in the original Raw data sets, in addition to the imagery, ancillary  information is stored within the image headers, as well as a detailed    account of all the reference files used for the calibration. Calibration files needed for further processing are archived as a separate data set.",
-            "title": "DAWN FC1 CALIBRATED CRUISE              \n                                      CHECKOUT/CALIB IMAGES V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "DAWN FC1 CALIBRATED CRUISE              \n                                      CHECKOUT/CALIB IMAGES V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/7L44Z9QVXUNL",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "TOVS Pathfinder Path-P Daily and Monthly Polar Gridded Atmospheric Parameters, Version 1. Version 1. Archived by National Aeronautics and Space Administration, U.S. Government, NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/7L44Z9QVXUNL.",
-            "issued": "1979-01-01",
-            "temporal": "1979-01-01T00:00:00Z/2005-12-31T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2005-12-31",
-            "keyword": [
-                "atmospheric radiation",
-                "earth science",
-                "atmospheric winds",
-                "atmospheric temperature",
-                "clouds",
-                "atmosphere"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Jennifer Francis",
                 "hasEmail": "mailto:francis@apl.washington.edu"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA NSIDC DAAC"
-            },
-            "identifier": "C1386246923-NSIDCV0",
             "description": "The TIROS-N Operational Vertical Sounder (TOVS) Polar Pathfinder (Path-P) data set consists of gridded daily and monthly Arctic and Antarctic atmospheric data derived from various NOAA satellites. TOVS Path-P daily files are available for the Northern and Southern Hemispheres from 60 degrees poleward at 100 km gridded spatial resolution in an Equal-Area Scalable Earth Grid (EASE-Grid). TOVS Path-P monthly files are available for the Northern Hemisphere only from 60 degrees poleward at 100 km gridded spatial resolution in EASE-Grid. Daily and monthly Northern Hemisphere data are available from January 1979 through current processing, and daily Southern Hemisphere data are available from July 1979 through current processing. Data were created from a modified version of the Improved Initialization Inversion Algorithm (3I) (Chedin et al. 1985), a physical-statistical retrieval method improved for use in identifying geophysical variables in snow- and ice-covered areas (Francis 1994).",
-            "title": "TOVS Pathfinder Path-P Daily and Monthly Polar Gridded Atmospheric Parameters, Version 1",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2F7L44Z9QVXUNL",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2F7L44Z9QVXUNL",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/nsidc0027_tovs_pathfinder_atm/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/nsidc0027_tovs_pathfinder_atm/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/7L44Z9QVXUNL",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/7L44Z9QVXUNL",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/7L44Z9QVXUNL",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/7L44Z9QVXUNL",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C1386246923-NSIDCV0",
+            "issued": "1979-01-01",
+            "keyword": [
+                "atmospheric radiation",
+                "earth science",
+                "atmospheric winds",
+                "atmospheric temperature",
+                "clouds",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.5067/7L44Z9QVXUNL",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2005-12-31",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA NSIDC DAAC"
+            },
             "spatial": "-180.0 60.0 180.0 90.0",
+            "temporal": "1979-01-01T00:00:00Z/2005-12-31T23:59:59.999Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "TOVS Pathfinder Path-P Daily and Monthly Polar Gridded Atmospheric Parameters, Version 1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-NAVCAM-3-EXT2-MTP029-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This dataset contains ROSETTA NAVCAM RADIOMETRICALLY CALIBRATED DATA of the ROSETTA EXTENSION 2 MTP029 Phase from 04 May. 2016, 06:04:22 to 31 May. 2016, 23:17:53 when at the vicinity of target 67P/CG.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-navcam-3-ext2-mtp029-v1.0_g7a2-7ms6",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "67p/churyumov-gerasimenko 1 (1969 r1)",
                 "zeta cas",
                 "alpha lyr",
                 "international rosetta mission"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-NAVCAM-3-EXT2-MTP029-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-navcam-3-ext2-mtp029-v1.0_g7a2-7ms6",
-            "description": "This dataset contains ROSETTA NAVCAM RADIOMETRICALLY CALIBRATED DATA of the ROSETTA EXTENSION 2 MTP029 Phase from 04 May. 2016, 06:04:22 to 31 May. 2016, 23:17:53 when at the vicinity of target 67P/CG.",
-            "title": "ROSETTA-ORBITER 67P NAVCAM 3 ROSETTA EXTENSION 2 MTP029 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P NAVCAM 3 ROSETTA EXTENSION 2 MTP029 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/CERES/FLASH_SSF_Terra-FM1-MODIS_Version4A",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/CERES/FLASH_SSF_Terra-FM1-MODIS_Version4A.",
-            "issued": "2020-08-01",
-            "temporal": "2019-01-01T00:00:00Z/2022-01-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-08-01",
-            "keyword": [
-                "atmosphere",
-                "atmospheric radiation",
-                "clouds",
-                "earth science"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Parnchai Sawaengphokhai",
                 "hasEmail": "mailto:parnchai.k.sawaengphokhai@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/LARC/SD/ASDC"
-            },
-            "identifier": "C1719289020-LARC_ASDC",
             "description": "FLASH_SSF_Terra-FM1-MODIS_Version4A is the Fast Longwave And Shortwave Radiative Fluxes (FLASHFlux) Clouds and Radiative Swath (SSF) TERRA-FM1 data in HDF Version 4A data product. This product consist of of Low latency (< 5 days from observation) Top-of-Atmosphere (TOA) fluxes and parameterized surface radiative fluxes at Clouds and the Earth's Radiant Energy Systems (CERES) Single Scanner Footprint (SSF) level for quick-look purposes. \r\n\r\nFLASHFlux data are a product line of the CERES project designed for processing and release of TOA and surface radiative fluxes for applied sciences and educations uses. The FLASHFlux data product is a rapid release product based upon the algorithms developed for and data collected by the CERES project. CERES is currently producing world-class climate data products derived from measurements taken aboard NASA's Terra and Aqua spacecrafts. While of exceptional fidelity, these data products require a considerable amount of processing time to assure quality, verify accuracy, and assess precision. The result is that CERES data are typically released up to six months after acquisition of the initial measurements. For climate studies, such delays are of little consequence especially considering the improved quality of the released data products. Thus, FLASHFlux products are not intended to achieve climate quality. FLASHFlux data products were envisioned as a resource whereby CERES data could be provided to the community within a few days of the initial measurements, with some calibration accuracy requirements relaxed to gain speed. \r\n\r\nThe SSF TOA/Surface Fluxes and Clouds product contains one hour of instantaneous FLASHFlux data for a single CERES scanner instrument. The SSF combines instantaneous CERES data with scene information from a higher-resolution imager such as Moderate-Resolution Imaging Spectroradiometer (MODIS) on the Terra and Aqua satellites and meteorological and ozone information from the GEOS-5 FP-IT Atmospheric Data Assimilation System (GEOS-5 ADAS). Scene identification and cloud properties are defined at the higher imager resolution and these data are averaged over the larger CERES footprint. For each CERES footprint, the SSF contains Top-of-Atmosphere fluxes in SW, LW, and NET, surface fluxes using the Langley parameterized shortwave and longwave algorithms, and clouds information. CERES is a key component of the Earth Observing System (EOS) program. The CERES instruments provide radiometric measurements of the Earth's atmosphere from three broadband channels. The CERES mission is a follow on to the successful Earth Radiation Budget Experiment (ERBE) mission. The first CERES instrument (PFM) was launched on November 27, 1997 as part of the Tropical Rainfall Measuring Mission (TRMM). Two CERES instruments (FM1 and FM2) were launched into polar orbit on board the EOS flagship Terra on December 18, 1999. Two additional CERES instruments (FM3 and FM4) were launched on board EOS Aqua on May 4, 2002. The newest CERES instrument (FM5) was launched on board the Suomi National Polar-orbiting Partnership (NPP) satellite.",
-            "title": "Fast Longwave And SHortwave Fluxes (FLASHflux) Clouds and Radiative Swath (SSF) TERRA-FM1 data in HDF Version 4A",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FCERES%2FFLASH_SSF_Terra-FM1-MODIS_Version4A",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FCERES%2FFLASH_SSF_Terra-FM1-MODIS_Version4A",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/CERES/FLASH_SSF_Terra-FM1-MODIS_Version4A",
-                    "description": "DOI data set landing page for FLASH_SSF_Terra-FM1-MODIS_Version4A",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for FLASH_SSF_Terra-FM1-MODIS_Version4A",
+                    "downloadURL": "https://doi.org/10.5067/CERES/FLASH_SSF_Terra-FM1-MODIS_Version4A",
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
-                    "downloadURL": "https://flashflux.larc.nasa.gov",
-                    "description": "FLASHFlux home page",
                     "@type": "dcat:Distribution",
+                    "description": "FLASHFlux home page",
+                    "downloadURL": "https://flashflux.larc.nasa.gov",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
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
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1719289020-LARC_ASDC",
-                    "description": "Earthdata Search for FLASH_SSF_Terra-FM1-MODIS_Version4A (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for FLASH_SSF_Terra-FM1-MODIS_Version4A (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1719289020-LARC_ASDC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
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
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ceres.larc.nasa.gov/data/#flashflux-ssf-level-2",
-                    "description": "CERES Data Page",
                     "@type": "dcat:Distribution",
+                    "description": "CERES Data Page",
+                    "downloadURL": "https://ceres.larc.nasa.gov/data/#flashflux-ssf-level-2",
+                    "mediaType": "text/html",
                     "title": "Subset this dataset using a web based subsetter"
                 },
                 {
@@ -799724,608 +799704,606 @@
                     "title": "Download this dataset through the CERES Ordering Tool"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/CERES/FLASH/SSF/Terra-FM1-MODIS_Version4A/",
-                    "description": "ASDC Direct Data Download for FLASH_SSF_Terra-FM1-MODIS_Version4A",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for FLASH_SSF_Terra-FM1-MODIS_Version4A",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/CERES/FLASH/SSF/Terra-FM1-MODIS_Version4A/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/CERES/FLASH/SSF/Terra-FM1-MODIS_Version4A/contents.html",
-                    "description": "OPeNDAP data access for FLASH_SSF_Terra-FM1-MODIS_Version4A",
                     "@type": "dcat:Distribution",
+                    "description": "OPeNDAP data access for FLASH_SSF_Terra-FM1-MODIS_Version4A",
+                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/CERES/FLASH/SSF/Terra-FM1-MODIS_Version4A/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 }
             ],
+            "identifier": "C1719289020-LARC_ASDC",
+            "issued": "2020-08-01",
+            "keyword": [
+                "atmosphere",
+                "atmospheric radiation",
+                "clouds",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/CERES/FLASH_SSF_Terra-FM1-MODIS_Version4A",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2020-08-01",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/LARC/SD/ASDC"
+            },
             "spatial": "<?xml version=\"1.0\" encoding=\"UTF-8\"?><gml:Polygon xmlns:gml=\"http://www.opengis.net/gml/3.2\" srsName=\"EPSG:9825\"><gml:outerBoundaryIs><gml:LinearRing><gml:posList>-90.0 -180.0 -90.0 180.0 90.0 180.0 90.0 -180.0 -90.0 -180.0</gml:posList></gml:LinearRing></gml:outerBoundaryIs><gml:innerBoundaryIs></gml:innerBoundaryIs></gml:Polygon>",
+            "temporal": "2019-01-01T00:00:00Z/2022-01-17T00:00:00Z",
             "theme": [
                 "FLASHFLUX",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Fast Longwave And SHortwave Fluxes (FLASHflux) Clouds and Radiative Swath (SSF) TERRA-FM1 data in HDF Version 4A"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/GFL20-MG063",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "GRACE-FO. 2024-06-15. GRACE-FO Level-2 Monthly Geopotential Spherical Harmonics GFZ. Version 6.3. GRACEFO_L2_GFZ_MONTHLY_0063. JPL. Archived by National Aeronautics and Space Administration, U.S. Government, JPL. https://doi.org/10.5067/GFL20-MG063. https://gracefo.jpl.nasa.gov/. GRACE-FO, JPL, 2024-06-15, GRACE-FO Level-2 Monthly Geopotential Spherical Harmonics GFZ Release 6.3 (RL06.3).",
-            "issued": "2022-04-15",
-            "temporal": "2018-05-22T00:00:00Z/2024-10-21T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-04-15",
-            "keyword": [
-                "solid earth",
-                "earth science",
-                "gravity/gravitational field"
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
-            "identifier": "C3059674861-POCLOUD",
-            "description": "FOR EXPERT USE ONLY. This dataset contains estimates of the total month-by-month geopotential of the Earth, derived from the Gravity Recovery and Climate Experiment Follow-On (GRACE-FO) mission measurements, produced by the German Research Centre for Geosciences (GFZ). The data are provided as spherical harmonic coefficients, averaged over approximately a month. These coefficients are derived from the Microwave Instrument (MWI) measured intersatellite range changes between the twin spacecraft of the GRACE-FO mission. Refer to the mission page for more information. \n<br><br>\nThis GRACE-FO RL06.3 data is an updated version of the GRACE-FO RL06.1 Level-2 data products. RL06.3 differs from RL06.1 only in the Level-1B accelerometer transplant data that is used for the GF2 satellite: Level-2 RL06.3 uses ACH1B RL04 that is contained within the ACX2 Level-1 bundle, which replaces ACH1B RL04 contained within the ACX Level-1 bundle that was used for Level-2 RL06.1 (note: ACX2-L1B is only applicable for 01/2023 onwards in wide-deadband operational mode; from 6/2018 through 12/2022, RL06.1 and RL06.3 GRACE-FO data are identical). All GRACE-FO RL06.3 Level-2 products are fully compatible with the GRACE RL06 level-2 fields. Refer to the mission page for more information.",
-            "release-place": "JPL",
-            "series-name": "GRACE-FO Level-2 Monthly Geopotential Spherical Harmonics GFZ",
-            "graphic-preview-description": "Thumbnail",
             "creator": "GRACE-FO",
-            "title": "GRACE-FO Level-2 Monthly Geopotential Spherical Harmonics GFZ Release 6.3 (RL06.3)",
-            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/GRACEFO_L2_GFZ_MONTHLY_0063.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "FOR EXPERT USE ONLY. This dataset contains estimates of the total month-by-month geopotential of the Earth, derived from the Gravity Recovery and Climate Experiment Follow-On (GRACE-FO) mission measurements, produced by the German Research Centre for Geosciences (GFZ). The data are provided as spherical harmonic coefficients, averaged over approximately a month. These coefficients are derived from the Microwave Instrument (MWI) measured intersatellite range changes between the twin spacecraft of the GRACE-FO mission. Refer to the mission page for more information. \n<br><br>\nThis GRACE-FO RL06.3 data is an updated version of the GRACE-FO RL06.1 Level-2 data products. RL06.3 differs from RL06.1 only in the Level-1B accelerometer transplant data that is used for the GF2 satellite: Level-2 RL06.3 uses ACH1B RL04 that is contained within the ACX2 Level-1 bundle, which replaces ACH1B RL04 contained within the ACX Level-1 bundle that was used for Level-2 RL06.1 (note: ACX2-L1B is only applicable for 01/2023 onwards in wide-deadband operational mode; from 6/2018 through 12/2022, RL06.1 and RL06.3 GRACE-FO data are identical). All GRACE-FO RL06.3 Level-2 products are fully compatible with the GRACE RL06 level-2 fields. Refer to the mission page for more information.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGFL20-MG063",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGFL20-MG063",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://podaac.jpl.nasa.gov/GRACE-FO",
-                    "description": "PO.DAAC's Project Page for GRACE-FO",
                     "@type": "dcat:Distribution",
+                    "description": "PO.DAAC's Project Page for GRACE-FO",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/GRACE-FO",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://gracefo.jpl.nasa.gov/",
-                    "description": "GRACE-FO Project Website (external to PO.DAAC)",
                     "@type": "dcat:Distribution",
+                    "description": "GRACE-FO Project Website (external to PO.DAAC)",
+                    "downloadURL": "https://gracefo.jpl.nasa.gov/",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/GRACEFO_L2_GFZ_MONTHLY_0063.jpg",
-                    "description": "Thumbnail",
                     "@type": "dcat:Distribution",
+                    "description": "Thumbnail",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/GRACEFO_L2_GFZ_MONTHLY_0063.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/gracefo/open/docs/GRACE-FO_L2_UserHandbook.pdf",
-                    "description": "Level-2 Gravity Field Product User Handbook",
                     "@type": "dcat:Distribution",
+                    "description": "Level-2 Gravity Field Product User Handbook",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/gracefo/open/docs/GRACE-FO_L2_UserHandbook.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/gracefo/open/docs/GRACE-FO_L2-GFZ_ProcStds_v1.0.pdf",
-                    "description": "GRACE-FO GFZ Level-2 Processing Standards Document",
                     "@type": "dcat:Distribution",
+                    "description": "GRACE-FO GFZ Level-2 Processing Standards Document",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/gracefo/open/docs/GRACE-FO_L2-GFZ_ProcStds_v1.0.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/gracefo/open/docs/GRACE-FO_L2-ReleaseNotes_GFZ_RL06.3.pdf",
-                    "description": "GRACE-FO GFZ Release Notes",
                     "@type": "dcat:Distribution",
+                    "description": "GRACE-FO GFZ Release Notes",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/gracefo/open/docs/GRACE-FO_L2-ReleaseNotes_GFZ_RL06.3.pdf",
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
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C3059674861-POCLOUD",
-                    "description": "HTTPS endpoint for data browse and download",
                     "@type": "dcat:Distribution",
+                    "description": "HTTPS endpoint for data browse and download",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C3059674861-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C3059674861-POCLOUD",
-                    "description": "Browse granule search results in Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse granule search results in Earthdata Search",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C3059674861-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/gracefo/open/docs/TN-13_GEOC_GFZ_RL0603.txt",
-                    "description": "Technical Note (TN) - 13",
                     "@type": "dcat:Distribution",
+                    "description": "Technical Note (TN) - 13",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/gracefo/open/docs/TN-13_GEOC_GFZ_RL0603.txt",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/gracefo/open/docs/TN-14_C30_C20_GSFC_SLR.txt",
-                    "description": "Technical Note (TN) - 14",
                     "@type": "dcat:Distribution",
+                    "description": "Technical Note (TN) - 14",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/gracefo/open/docs/TN-14_C30_C20_GSFC_SLR.txt",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://podaac.jpl.nasa.gov/gravity/gracefo-documentation",
-                    "description": "Page for all GRACE-FO Documentation and Technical Notes",
                     "@type": "dcat:Distribution",
+                    "description": "Page for all GRACE-FO Documentation and Technical Notes",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/gravity/gracefo-documentation",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "graphic-preview-description": "Thumbnail",
+            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/GRACEFO_L2_GFZ_MONTHLY_0063.jpg",
+            "identifier": "C3059674861-POCLOUD",
+            "issued": "2022-04-15",
+            "keyword": [
+                "solid earth",
+                "earth science",
+                "gravity/gravitational field"
+            ],
+            "landingPage": "https://doi.org/10.5067/GFL20-MG063",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2022-04-15",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/JPL/PODAAC"
+            },
+            "release-place": "JPL",
+            "series-name": "GRACE-FO Level-2 Monthly Geopotential Spherical Harmonics GFZ",
             "spatial": "-180.0 -89.0 180.0 89.0",
+            "temporal": "2018-05-22T00:00:00Z/2024-10-21T00:00:00Z",
             "theme": [
                 "GRACE-FO",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "GRACE-FO Level-2 Monthly Geopotential Spherical Harmonics GFZ Release 6.3 (RL06.3)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/79O9UHDQ43CI",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "SMEX03 Site Photographs, Georgia, Version 1. Version 1. Archived by National Aeronautics and Space Administration, U.S. Government, NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/79O9UHDQ43CI.",
-            "issued": "2003-06-23",
-            "temporal": "2003-06-23T00:00:00Z/2003-07-07T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2003-07-07",
-            "keyword": [
-                "land use/land cover",
-                "earth science",
-                "land surface"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Michael Cosh",
                 "hasEmail": "mailto:mcosh@hydrolab.arsusda.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA NSIDC DAAC"
-            },
-            "identifier": "C1386205625-NSIDCV0",
             "description": "The <em>SMEX03 Site Photographs</em> data set includes photographs of the regional study areas of Alabama, Georgia, and Oklahoma, USA as part of the 2003 Soil Moisture Experiment (SMEX03).",
-            "title": "SMEX03 Site Photographs, Georgia, Version 1",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2F79O9UHDQ43CI",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2F79O9UHDQ43CI",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/AVDM/data/soil_moisture/SMEX03/Georgia/ancillary_data/photographs/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/AVDM/data/soil_moisture/SMEX03/Georgia/ancillary_data/photographs/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/AVDM/data/soil_moisture/SMEX03/Georgia/ancillary_data/photographs/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/AVDM/data/soil_moisture/SMEX03/Georgia/ancillary_data/photographs/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/79O9UHDQ43CI",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/79O9UHDQ43CI",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/79O9UHDQ43CI",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/79O9UHDQ43CI",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C1386205625-NSIDCV0",
+            "issued": "2003-06-23",
+            "keyword": [
+                "land use/land cover",
+                "earth science",
+                "land surface"
+            ],
+            "landingPage": "https://doi.org/10.5067/79O9UHDQ43CI",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2003-07-07",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA NSIDC DAAC"
+            },
             "spatial": "-83.8 31.5 -83.5 31.8",
+            "temporal": "2003-06-23T00:00:00Z/2003-07-07T23:59:59.999Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "SMEX03 Site Photographs, Georgia, Version 1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1773",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Jimenez, J.L., P. Campuzano-Jost, D.A. Day, B.A. Nault, and J.C. Schroder. 2020. ATom: L2 Particulate Iodine from High-Resolution Aerosol Mass Spectrometer (HR-AMS). ORNL DAAC, Oak Ridge, Tennessee, USA. https://doi.org/10.3334/ORNLDAAC/1773",
-            "issued": "2020-06-30",
-            "temporal": "2016-07-29T00:00:00Z/2017-02-21T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-06-12",
-            "keyword": [
-                "aerosols",
-                "atmosphere",
-                "earth science",
-                "atmospheric chemistry"
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
-            "identifier": "C2676975101-ORNL_CLOUD",
             "description": "This dataset provides mass concentrations of particulate iodine as measured by the High-Resolution Aerosol Mass Spectrometer (HR-AMS) during the first two deployments of the NASA Atmospheric Tomography airborne missions (ATom-1 and ATom-2) in 2016 and 2017, respectively. The data provided in this dataset result from a reanalysis of the initial HR-AMS data based on post-mission calibrations and are reported at 1-minute resolution. The dataset also includes the fractions of the main ions (I+, HI+, and I2+) that can be used to ascertain the oxidation state of iodine in particles. Each observation includes an air mass classification flag (tropospheric or stratospheric conditions) based on collocated in situ water vapor and ozone measurements and positional data from the HR-AMS data feed.",
-            "graphic-preview-description": "Figure 1: Particulate Iodine measured along flight paths in ATom1 and ATom2. Image courtesy J.L. Jimenez.",
-            "title": "ATom: L2 Particulate Iodine from High-Resolution Aerosol Mass Spectrometer (HR-AMS)",
-            "graphic-preview-file": "https://daac.ornl.gov/ATOM/guides/ATom_Particulate_Iodine_Fig1.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1773",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1773",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/atom/ATom_Particulate_Iodine/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/atom/ATom_Particulate_Iodine/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/ATOM/guides/ATom_Particulate_Iodine.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/ATOM/guides/ATom_Particulate_Iodine.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1773",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1773",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/atom/ATom_Particulate_Iodine/comp/ATom_Particulate_Iodine.pdf",
-                    "description": "ATom: L2 Particulate Iodine from High-Resolution Aerosol Mass Spectrometer (HR-AMS): ATom_Particulate_Iodine.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "ATom: L2 Particulate Iodine from High-Resolution Aerosol Mass Spectrometer (HR-AMS): ATom_Particulate_Iodine.pdf",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/atom/ATom_Particulate_Iodine/comp/ATom_Particulate_Iodine.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://daac.ornl.gov/ATOM/guides/ATom_Particulate_Iodine_Fig1.png",
-                    "description": "Figure 1: Particulate Iodine measured along flight paths in ATom1 and ATom2. Image courtesy J.L. Jimenez.",
                     "@type": "dcat:Distribution",
+                    "description": "Figure 1: Particulate Iodine measured along flight paths in ATom1 and ATom2. Image courtesy J.L. Jimenez.",
+                    "downloadURL": "https://daac.ornl.gov/ATOM/guides/ATom_Particulate_Iodine_Fig1.png",
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
+            "graphic-preview-description": "Figure 1: Particulate Iodine measured along flight paths in ATom1 and ATom2. Image courtesy J.L. Jimenez.",
+            "graphic-preview-file": "https://daac.ornl.gov/ATOM/guides/ATom_Particulate_Iodine_Fig1.png",
+            "identifier": "C2676975101-ORNL_CLOUD",
+            "issued": "2020-06-30",
+            "keyword": [
+                "aerosols",
+                "atmosphere",
+                "earth science",
+                "atmospheric chemistry"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1773",
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
             "spatial": "-180.0 -65.33 180.0 80.52",
+            "temporal": "2016-07-29T00:00:00Z/2017-02-21T23:59:59Z",
             "theme": [
                 "ATom",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "ATom: L2 Particulate Iodine from High-Resolution Aerosol Mass Spectrometer (HR-AMS)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://c3.nasa.gov/dashlink/resources/224/",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2010-10-13",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
-            "keyword": [
-                "dashlink",
-                "ames",
-                "nasa"
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
-            "identifier": "DASHLINK_224",
             "description": "COMPLEX NETWORKS IN CLIMATE SCIENCE:\r\nPROGRESS, OPPORTUNITIES AND CHALLENGES\r\nKARSTEN STEINHAEUSER, NITESH V. CHAWLA, AND AUROOP R. GANGULY\r\n\r\nAbstract. Networks have been used to describe and model a wide range of complex systems,\r\nboth natural as well as man-made. One particularly interesting application in the earth sciences\r\nis the use of complex networks to represent and study the global climate system. In this paper,\r\nwe motivate this general approach, explain the basic methodology, report on the state of the art\r\n(including our contributions), and outline open questions and opportunities for future research.",
-            "title": "COMPLEX NETWORKS IN CLIMATE SCIENCE: PROGRESS, OPPORTUNITIES AND CHALLENGES",
-            "programCode": [
-                "026:029"
-            ],
             "distribution": [
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/publication/Paper_2_.pdf",
-                    "description": "COMPLEX NETWORKS IN CLIMATE SCIENCE: PROGRESS, OPPORTUNITIES AND CHALLENGES",
                     "@type": "dcat:Distribution",
+                    "description": "COMPLEX NETWORKS IN CLIMATE SCIENCE: PROGRESS, OPPORTUNITIES AND CHALLENGES",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/publication/Paper_2_.pdf",
+                    "mediaType": "application/pdf",
                     "title": "Paper 2 .pdf"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/publication/Paper2_presentation.pdf",
-                    "description": "Presentation",
                     "@type": "dcat:Distribution",
+                    "description": "Presentation",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/publication/Paper2_presentation.pdf",
+                    "mediaType": "application/pdf",
                     "title": "Paper2_presentation.pdf"
                 }
             ],
-            "accrualPeriodicity": "irregular"
+            "identifier": "DASHLINK_224",
+            "issued": "2010-10-13",
+            "keyword": [
+                "dashlink",
+                "ames",
+                "nasa"
+            ],
+            "landingPage": "https://c3.nasa.gov/dashlink/resources/224/",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:029"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Dashlink"
+            },
+            "title": "COMPLEX NETWORKS IN CLIMATE SCIENCE: PROGRESS, OPPORTUNITIES AND CHALLENGES"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-3-ESC4-67PCHURYUMOV-M24-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This data set contains images acquired by the OSIRIS Wide Angle Camera during the COMET ESCORT 4 phase of the Rosetta mission at the comet 67P, covering the period from 2015-12-15T23:25:00.000 to 2016-01-12T23:24:59.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-3-esc4-67pchuryumov-m24-v1.0",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2021-05-21",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "zeta cas",
                 "67p/churyumov-gerasimenko 1 (1969 r1)",
                 "vega",
                 "international rosetta mission"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-3-ESC4-67PCHURYUMOV-M24-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-3-esc4-67pchuryumov-m24-v1.0",
-            "description": "This data set contains images acquired by the OSIRIS Wide Angle Camera during the COMET ESCORT 4 phase of the Rosetta mission at the comet 67P, covering the period from 2015-12-15T23:25:00.000 to 2016-01-12T23:24:59.000.",
-            "title": "ROSETTA-ORBITER COMET ESCORT 4 OSIWAC 3 RDR MTP024 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER COMET ESCORT 4 OSIWAC 3 RDR MTP024 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/H9I88X3DQD7S",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "SMEX03 AMSR-E Daily Gridded Soil Moisture and Brightness Temperatures, Georgia, Version 1. Version 1. Archived by National Aeronautics and Space Administration, U.S. Government, NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/H9I88X3DQD7S.",
-            "issued": "2003-04-01",
-            "temporal": "2003-04-01T00:00:00Z/2003-08-31T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2003-08-31",
-            "keyword": [
-                "topography",
-                "earth science",
-                "soils",
-                "microwave",
-                "land surface",
-                "spectral/engineering"
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
-            "identifier": "C1386250713-NSIDCV0",
             "description": "Notice to Data Users: The documentation for this data set was provided solely by the Principal Investigator(s) and was not further developed, thoroughly reviewed, or edited by NSIDC. Thus, support for this data set may be limited.\n\nThis data set contains Advanced Microwave Scanning Radiometer - Earth Observing System (AMSR-E) Level-3 daily measurements of surface soil moisture and vegetation/roughness water content.",
-            "title": "SMEX03 AMSR-E Daily Gridded Soil Moisture and Brightness Temperatures, Georgia, Version 1",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FH9I88X3DQD7S",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FH9I88X3DQD7S",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/AVDM/data/soil_moisture/SMEX03/Georgia/satellite/AMSRE/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/AVDM/data/soil_moisture/SMEX03/Georgia/satellite/AMSRE/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/AVDM/data/soil_moisture/SMEX03/Georgia/satellite/AMSRE/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/AVDM/data/soil_moisture/SMEX03/Georgia/satellite/AMSRE/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/AVDM/data/soil_moisture/SMEX03/Georgia/satellite/AMSRE/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/AVDM/data/soil_moisture/SMEX03/Georgia/satellite/AMSRE/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/AVDM/data/soil_moisture/SMEX03/Georgia/satellite/AMSRE/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/AVDM/data/soil_moisture/SMEX03/Georgia/satellite/AMSRE/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/H9I88X3DQD7S",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/H9I88X3DQD7S",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/H9I88X3DQD7S",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/H9I88X3DQD7S",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C1386250713-NSIDCV0",
+            "issued": "2003-04-01",
+            "keyword": [
+                "topography",
+                "earth science",
+                "soils",
+                "microwave",
+                "land surface",
+                "spectral/engineering"
+            ],
+            "landingPage": "https://doi.org/10.5067/H9I88X3DQD7S",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2003-08-31",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA NSIDC DAAC"
+            },
             "spatial": "-90.0 28.0 -80.0 38.0",
+            "temporal": "2003-04-01T00:00:00Z/2003-08-31T23:59:59.999Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "SMEX03 AMSR-E Daily Gridded Soil Moisture and Brightness Temperatures, Georgia, Version 1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/SeaBASS/MVCO/DATA001",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/GSFC/SED/ESD/GCDC/OB.DAAC. https://doi.org/10.5067/SeaBASS/MVCO/DATA001.",
-            "issued": "2003-05-10",
-            "temporal": "2003-05-10T00:00:02Z/2023-04-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-04-06",
-            "keyword": [
-                "salinity/density",
-                "oceans",
-                "earth science",
-                "ocean chemistry",
-                "ocean optics",
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
-            "identifier": "C1633360510-OB_DAAC",
             "description": "The Martha's Vineyard Coastal Observatory (MVCO) is operated by Woods Hole Oceanographic Institution. These datasets include measurements collected from and around the Martha's Vineyard site.",
-            "title": "Martha's Vineyard Coastal Observatory (MVCO)",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSeaBASS%2FMVCO%2FDATA001",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSeaBASS%2FMVCO%2FDATA001",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://seabass.gsfc.nasa.gov/experiment/MVCO/",
-                    "description": "Detailed information about the SeaBASS Experiment such as cruises, funding, and investigators",
                     "@type": "dcat:Distribution",
+                    "description": "Detailed information about the SeaBASS Experiment such as cruises, funding, and investigators",
+                    "downloadURL": "https://seabass.gsfc.nasa.gov/experiment/MVCO/",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 }
             ],
+            "identifier": "C1633360510-OB_DAAC",
+            "issued": "2003-05-10",
+            "keyword": [
+                "salinity/density",
+                "oceans",
+                "earth science",
+                "ocean chemistry",
+                "ocean optics",
+                "ocean temperature"
+            ],
+            "landingPage": "https://doi.org/10.5067/SeaBASS/MVCO/DATA001",
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
+            "temporal": "2003-05-10T00:00:02Z/2023-04-17T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Martha's Vineyard Coastal Observatory (MVCO)"
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
-                "msc",
-                "lunar",
-                "sample",
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
-            "identifier": "NASA-882",
             "description": "Apollo 16 Lunar Sample Information Catalog; MSC 03210; P. Butler, Jr., M. Anderson, K. Johnston, and W.C. Phinney",
-            "title": "Apollo 16 Lunar Sample Information Catalog",
-            "programCode": [
-                "026:008"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -800333,686 +800311,717 @@
                     "mediaType": "application/pdf"
                 }
             ],
-            "accrualPeriodicity": "irregular",
+            "identifier": "NASA-882",
+            "issued": "2018-06-25",
+            "keyword": [
+                "msc",
+                "lunar",
+                "sample",
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
+            "title": "Apollo 16 Lunar Sample Information Catalog"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/AURA/TES/TL2O3N_L2.007",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2017-04-06. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/AURA/TES/TL2O3N_L2.007. https://asdc.larc.nasa.gov/project/TES.",
-            "issued": "2015-08-27",
-            "temporal": "2004-08-22T00:00:00Z/2018-01-22T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2019-06-19",
-            "keyword": [
-                "atmospheric temperature",
-                "clouds",
-                "earth science",
-                "atmospheric chemistry",
-                "air quality",
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
-            "identifier": "C1331182557-LARC",
             "description": "TL2O3N_7 is the Tropospheric Emission Spectrometer (TES)/Aura Level 2 Ozone Nadir Version 7 data product. It consists of information for one molecular species for an entire Global Survey or Special Observation. TES was an instrument aboard NASA's Aura satellite and was launched from California on July 15, 2004. Data collection for TES is complete. TES Level 2 data contain retrieved species (or temperature) profiles at the observation targets and the estimated errors. The geolocation, quality, and other data (e.g., surface characteristics for nadir observations) were also provided. L2 modeled spectra were evaluated using radiative transfer modeling algorithms. The process, referred to as retrieval, compared observed spectra to the modeled spectra and iteratively updated the atmospheric parameters. L2 standard product files included information for one molecular species (or temperature) for an entire global survey or special observation run. A global survey consisted of a maximum of 16 consecutive orbits. Each TES Level 2 standard product reported information in a swath format conforming to the HDF-EOS Aura File Format Guidelines.\r\rNadir observations, which point directly to the surface of the Earth, are different from limb observations, which are pointed at various off-nadir angles into the atmosphere. Nadir and limb observations were added to separate L2 files, and a single ancillary file was composed of data that are common to both nadir and limb files. A Nadir sequence within the TES Global Survey was a fixed number of observations within an orbit for a Global Survey. Prior to April 24, 2005, it consisted of two low resolution scans over the same ground locations. After April 24, 2005, Global Survey data consisted of three low resolution scans. The Nadir standard product consists of four files, where each file is composed of the Global Survey Nadir observations from one of four focal planes for a single orbit, i.e. 72 orbit sequences. The Global Survey Nadir observations only used a single set of filter mix. \r\rA Global Survey consisted of observations along 16 consecutive orbits at the start of a two day cycle, over which 4,608 retrievals were performed. Each observation was the input for retrievals of species Volume Mixing Ratios (VMRs), temperature profiles, surface temperature, and other data parameters with associated pressure levels, precision, total error, vertical resolution, total column density, and other diagnostic quantities. Each TES Level 2 standard product reported information in a swath format conforming to the HDF-EOS Aura File Format Guidelines. Each Swath object was bounded by the number of observations in a global survey and a predefined set of pressure levels, representing slices through the atmosphere. Each standard product could have had a variable number of observations depending upon the Global Survey configuration and whether averaging was employed. Also, missing or bad retrievals were not reported. Further, observations were occasionally scheduled on non-global survey days. In general they were measurements made for validation purposes or with highly focused science objectives. Those non-global survey measurements were referred to as \u201cspecial observations.\u201d\r\rA Limb sequence within the TES Global Survey was three high-resolution scans over the same limb locations. The Limb standard product consists of four files, where each file is composed of the Global Survey Limb observations from one of four focal planes for a single orbit, i.e. 72 orbit sequences. The Global Survey Limb observations used a repeating sequence of filter wheel positions. Special Observations could only be scheduled during the 9 or 10 orbit gaps in the Global Surveys, and were conducted in any of three basic modes: stare, transect, step-and-stare. The mode used depended on the science requirement. Each limb observation Limb 1, Limb 2 and Limb 3, were processed independently. Thus, each limb standard product consisted of three sets w",
-            "title": "TES/Aura L2 Ozone Nadir V007",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAURA%2FTES%2FTL2O3N_L2.007",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAURA%2FTES%2FTL2O3N_L2.007",
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
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1331182557-LARC",
-                    "description": "Earthdata Search for TL2O3N_7 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for TL2O3N_7 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1331182557-LARC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/AURA/TES/TL2O3N_L2.007",
-                    "description": "DOI data set landing page for TL2O3N_7",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for TL2O3N_7",
+                    "downloadURL": "https://doi.org/10.5067/AURA/TES/TL2O3N_L2.007",
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
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/TES/TL2O3N.007/",
-                    "description": "ASDC Direct Data Download for TL2O3N.007",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for TL2O3N.007",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/TES/TL2O3N.007/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/TES/TL2O3N.007/contents.html",
-                    "description": "OPeNDAP data access for TL2O3N.007",
                     "@type": "dcat:Distribution",
+                    "description": "OPeNDAP data access for TL2O3N.007",
+                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/TES/TL2O3N.007/contents.html",
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
+            "identifier": "C1331182557-LARC",
+            "issued": "2015-08-27",
+            "keyword": [
+                "atmospheric temperature",
+                "clouds",
+                "earth science",
+                "atmospheric chemistry",
+                "air quality",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.5067/AURA/TES/TL2O3N_L2.007",
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
+            "title": "TES/Aura L2 Ozone Nadir V007"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewBundle.jsp?identifier=urn%3Anasa%3Apds%3Amaven.rose.raw&version=1.9",
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
-                "mars atmosphere and volatile evolution mission"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This bundle contains raw data concerning the radio signal transmitted from Earth and the radio signal received at Earth, calibration collections containing a  prediction for the frequency of the radio signal received at Earth and information  on the effects of Earth's ionosphere, troposphere, and weather, and a browse collection contains plots that provide an overview of received data.",
+            "identifier": "urn:nasa:pds:maven.rose.raw",
+            "issued": "2021-05-21",
+            "keyword": [
+                "mars",
+                "mars atmosphere and volatile evolution mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewBundle.jsp?identifier=urn%3Anasa%3Apds%3Amaven.rose.raw&version=1.9",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:maven.rose.raw",
-            "description": "This bundle contains raw data concerning the radio signal transmitted from Earth and the radio signal received at Earth, calibration collections containing a  prediction for the frequency of the radio signal received at Earth and information  on the effects of Earth's ionosphere, troposphere, and weather, and a browse collection contains plots that provide an overview of received data.",
-            "title": "MAVEN ROSE Raw Data Bundle",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "MAVEN ROSE Raw Data Bundle"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/SeaBASS/LAKE_MI_2012_WATERQUAL/DATA001",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/GSFC/SED/ESD/GCDC/OB.DAAC. https://doi.org/10.5067/SeaBASS/LAKE_MI_2012_WATERQUAL/DATA001.",
-            "issued": "2012-06-26",
-            "temporal": "2012-06-26T00:00:02Z/2023-04-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-04-06",
-            "keyword": [
-                "ocean chemistry",
-                "ocean optics",
-                "oceans",
-                "ocean temperature",
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
-            "identifier": "C1633360419-OB_DAAC",
             "description": "Measurements taken in Lake Michigan and Green Bay in 2012 as part of a water quality monitoring program.",
-            "title": "Water quality monitoring program in Lake Michigan and Green Bay",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSeaBASS%2FLAKE_MI_2012_WATERQUAL%2FDATA001",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSeaBASS%2FLAKE_MI_2012_WATERQUAL%2FDATA001",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://seabass.gsfc.nasa.gov/experiment/Lake_MI_2012_WaterQual/",
-                    "description": "Detailed information about the SeaBASS Experiment such as cruises, funding, and investigators",
                     "@type": "dcat:Distribution",
+                    "description": "Detailed information about the SeaBASS Experiment such as cruises, funding, and investigators",
+                    "downloadURL": "https://seabass.gsfc.nasa.gov/experiment/Lake_MI_2012_WaterQual/",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 }
             ],
+            "identifier": "C1633360419-OB_DAAC",
+            "issued": "2012-06-26",
+            "keyword": [
+                "ocean chemistry",
+                "ocean optics",
+                "oceans",
+                "ocean temperature",
+                "salinity/density",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/SeaBASS/LAKE_MI_2012_WATERQUAL/DATA001",
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
+            "temporal": "2012-06-26T00:00:02Z/2023-04-17T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Water quality monitoring program in Lake Michigan and Green Bay"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/SeaBASS/ONR_PENOBSCOTRIVERSYSTEM/DATA001",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/GSFC/SED/ESD/GCDC/OB.DAAC. https://doi.org/10.5067/SeaBASS/ONR_PENOBSCOTRIVERSYSTEM/DATA001.",
-            "issued": "2006-01-09",
-            "temporal": "2006-01-09T10:55:00Z/2023-04-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-04-06",
-            "keyword": [
-                "earth science",
-                "salinity/density",
-                "ocean temperature",
-                "oceans",
-                "ocean chemistry",
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
-            "identifier": "C1633360573-OB_DAAC",
             "description": "Measurements from the Penobscot River System in Maine taken between 2006 and 2009.",
-            "title": "Office of Naval Research (ONR) measurements in the Penobscot River System",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSeaBASS%2FONR_PENOBSCOTRIVERSYSTEM%2FDATA001",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSeaBASS%2FONR_PENOBSCOTRIVERSYSTEM%2FDATA001",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://seabass.gsfc.nasa.gov/experiment/ONR_PenobscotRiverSystem/",
-                    "description": "Detailed information about the SeaBASS Experiment such as cruises, funding, and investigators",
                     "@type": "dcat:Distribution",
+                    "description": "Detailed information about the SeaBASS Experiment such as cruises, funding, and investigators",
+                    "downloadURL": "https://seabass.gsfc.nasa.gov/experiment/ONR_PenobscotRiverSystem/",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 }
             ],
+            "identifier": "C1633360573-OB_DAAC",
+            "issued": "2006-01-09",
+            "keyword": [
+                "earth science",
+                "salinity/density",
+                "ocean temperature",
+                "oceans",
+                "ocean chemistry",
+                "ocean optics"
+            ],
+            "landingPage": "https://doi.org/10.5067/SeaBASS/ONR_PENOBSCOTRIVERSYSTEM/DATA001",
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
+            "temporal": "2006-01-09T10:55:00Z/2023-04-17T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Office of Naval Research (ONR) measurements in the Penobscot River System"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/43NH9LHM9YRK",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "AMSR-E/AMSR2 Unified L3 Global Monthly 25 km EASE-Grid Snow Water Equivalent V001. Version 1. Archived by National Aeronautics and Space Administration, U.S. Government, NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/43NH9LHM9YRK.",
-            "issued": "2012-07-02",
-            "temporal": "2012-07-02T00:00:00Z/2025-01-13T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-12-31",
-            "keyword": [
-                "terrestrial hydrosphere",
-                "cryosphere",
-                "snow/ice",
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
-            "identifier": "C1587883062-NSIDC_ECS",
             "description": "This AMSR-E/AMSR2 Unified Level-3 (L3) data set provides monthly mean estimates of Snow Water Equivalent (SWE). SWE was derived from brightness temperature measurements acquired by the Advanced Microwave Scanning Radiometer 2 (AMSR2) instrument on board the JAXA GCOM-W1 satellite. \n\nThe SWE data is rendered to an azimuthal 25 km Equal-Area Scalable Earth Grid (EASE-Grid) for both the Northern and Southern Hemisphere.\n\nNote: This data set uses JAXA AMSR2 Level-1R (L1R) input brightness temperatures that are calibrated, or unified, across the JAXA AMSR-E and JAXA AMSR2 L1R products.",
-            "graphic-preview-description": "This application allows you to interactively browse global satellite imagery within hours of it being acquired. You can also save it, share it, and download the underlying data.",
-            "title": "AMSR-E/AMSR2 Unified L3 Global Monthly 25 km EASE-Grid Snow Water Equivalent V001",
-            "graphic-preview-file": "https://worldview.earthdata.nasa.gov/?v=-207,-64,134,93&l=AMSRU2_Snow_Water_Equivalent_Monthly,Coastlines_15m,MODIS_Terra_CorrectedReflectance_TrueColor&lg=false&t=2012-08-01",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2F43NH9LHM9YRK",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2F43NH9LHM9YRK",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/AMSA/AU_MoSno.001",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/AMSA/AU_MoSno.001",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=AU_MoSno+V001",
-                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=AU_MoSno+V001",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/data/data-access-tool/AU_MoSno/versions/1/",
-                    "description": "Search and filter data files using a map-based interface",
                     "@type": "dcat:Distribution",
+                    "description": "Search and filter data files using a map-based interface",
+                    "downloadURL": "https://nsidc.org/data/data-access-tool/AU_MoSno/versions/1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://worldview.earthdata.nasa.gov/?v=-207%2C-64%2C134%2C93&l=AMSRU2_Snow_Water_Equivalent_Monthly%2CCoastlines_15m%2CMODIS_Terra_CorrectedReflectance_TrueColor&lg=false&t=2012-08-01",
-                    "description": "This application allows you to interactively browse global satellite imagery within hours of it being acquired. You can also save it, share it, and download the underlying data.",
                     "@type": "dcat:Distribution",
+                    "description": "This application allows you to interactively browse global satellite imagery within hours of it being acquired. You can also save it, share it, and download the underlying data.",
+                    "downloadURL": "https://worldview.earthdata.nasa.gov/?v=-207%2C-64%2C134%2C93&l=AMSRU2_Snow_Water_Equivalent_Monthly%2CCoastlines_15m%2CMODIS_Terra_CorrectedReflectance_TrueColor&lg=false&t=2012-08-01",
+                    "mediaType": "text/html",
                     "title": "Get a related visualization through WORLDVIEW"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/43NH9LHM9YRK",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/43NH9LHM9YRK",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/43NH9LHM9YRK",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/43NH9LHM9YRK",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "graphic-preview-description": "This application allows you to interactively browse global satellite imagery within hours of it being acquired. You can also save it, share it, and download the underlying data.",
+            "graphic-preview-file": "https://worldview.earthdata.nasa.gov/?v=-207,-64,134,93&l=AMSRU2_Snow_Water_Equivalent_Monthly,Coastlines_15m,MODIS_Terra_CorrectedReflectance_TrueColor&lg=false&t=2012-08-01",
+            "identifier": "C1587883062-NSIDC_ECS",
+            "issued": "2012-07-02",
+            "keyword": [
+                "terrestrial hydrosphere",
+                "cryosphere",
+                "snow/ice",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/43NH9LHM9YRK",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2024-12-31",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA NSIDC DAAC"
+            },
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2012-07-02T00:00:00Z/2025-01-13T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "AMSR-E/AMSR2 Unified L3 Global Monthly 25 km EASE-Grid Snow Water Equivalent V001"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ISS/SAGEIII/LUNAR_NetCDF4_L2-V5.2",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/ISS/SAGEIII/LUNAR_NetCDF4_L2-V5.2. https://asdc.larc.nasa.gov/project/SAGE%20III-ISS.",
-            "issued": "2021-10-18",
-            "temporal": "2017-05-31T00:00:00Z/2023-02-28T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2021-10-18",
-            "keyword": [
-                "atmospheric pressure",
-                "aerosols",
-                "atmosphere",
-                "atmospheric chemistry",
-                "atmospheric radiation",
-                "atmospheric water vapor",
-                "earth science"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Dr. David Flittner",
                 "hasEmail": "mailto:david.e.flittner@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/LARC/SD/ASDC"
-            },
-            "identifier": "C2205366222-LARC",
             "description": "g3blmnc_52 is the Stratospheric Aerosol and Gas Experiment III (SAGE III) on the International Space Station (ISS) (SAGE III/ISS) Level 2 Monthly Lunar Event Species Profiles (NetCDF) V052 data product. It contains all the species products for a month of lunar events (the last day of each month is omitted) . SAGE III was Launched on February 19, 2017 on a SpaceX Falcon 9 from Kennedy Space Center, SAGE III-ISS is the second instrument from the SAGE III project, externally mounted on the ISS. This ISS-based instrument uses a technique known as occultation, which involves looking at the light from the Sun or Moon as it passes through Earth's atmosphere at the edge, or limb, of the planet to provide long-term monitoring of ozone vertical profiles of the stratosphere and mesosphere. The data provided by SAGE III-ISS includes key components of atmospheric composition and their long-term variability, focusing on the study of aerosols, chlorine dioxide, clouds, nitrogen dioxide, nitrogen trioxide, pressure and temperature, and water vapor. SAGE data has historically been used by the World Meteorological Organization to inform their periodic assessments of ozone depletion. These new observations from the International Space Station will continue the SAGE team's contributions to ongoing scientific understanding of the Earth's atmosphere.",
-            "title": "SAGE III/ISS L2 Monthly Lunar Event Species Profiles (NetCDF) V052",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FISS%2FSAGEIII%2FLUNAR_NetCDF4_L2-V5.2",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FISS%2FSAGEIII%2FLUNAR_NetCDF4_L2-V5.2",
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
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/ISS/SAGEIII/LUNAR_NetCDF4_L2-V5.2",
-                    "description": "DOI data set landing page for g3blmnc_52",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for g3blmnc_52",
+                    "downloadURL": "https://doi.org/10.5067/ISS/SAGEIII/LUNAR_NetCDF4_L2-V5.2",
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
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2205366222-LARC",
-                    "description": "Earthdata Search for g3blmnc_52 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data).",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for g3blmnc_52 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data).",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2205366222-LARC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 }
             ],
+            "identifier": "C2205366222-LARC",
+            "issued": "2021-10-18",
+            "keyword": [
+                "atmospheric pressure",
+                "aerosols",
+                "atmosphere",
+                "atmospheric chemistry",
+                "atmospheric radiation",
+                "atmospheric water vapor",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/ISS/SAGEIII/LUNAR_NetCDF4_L2-V5.2",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2021-10-18",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/LARC/SD/ASDC"
+            },
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2017-05-31T00:00:00Z/2023-02-28T00:00:00Z",
             "theme": [
                 "SAGE III-ISS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "SAGE III/ISS L2 Monthly Lunar Event Species Profiles (NetCDF) V052"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC3-0966-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 3 phase 2015-07-01 to 2015-10-21. It is a Global Gravity measurement at the comet 67P and covers the time 2015-08-17T03:04:20.000 to 2015-08-17T09:56:21.500.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc3-0966-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC3-0966-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc3-0966-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 3 phase 2015-07-01 to 2015-10-21. It is a Global Gravity measurement at the comet 67P and covers the time 2015-08-17T03:04:20.000 to 2015-08-17T09:56:21.500.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 3 0966 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 3 0966 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC2-0644-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 2 phase 2015-03-11 to 2015-06-30. It is a Global Gravity measurement at the comet 67P and covers the time 2015-03-14T07:28:05.000 to 2015-03-14T09:18:37.500.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc2-0644-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC2-0644-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc2-0644-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 2 phase 2015-03-11 to 2015-06-30. It is a Global Gravity measurement at the comet 67P and covers the time 2015-03-14T07:28:05.000 to 2015-03-14T09:18:37.500.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 2 0644 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 2 0644 V1.0"
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
+                    "downloadURL": "https://pds.jpl.nasa.gov/tools/subscription_service/SS-20120601.shtml",
+                    "mediaType": "application/html"
+                }
             ],
+            "identifier": "NASA-509",
+            "issued": "2018-06-25",
             "keyword": [
                 "marci",
                 "sharad",
@@ -801024,597 +801033,590 @@
                 "crism",
                 "ctx"
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
-            "identifier": "NASA-509",
-            "description": "CRISM, CTX, HiRISE, MARCI, MCS, RSS, SHARAD, SPICE",
-            "title": "PDS Mars Reconnaissance Orbiter Data 21",
-            "programCode": [
-                "026:005"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://pds.jpl.nasa.gov/tools/subscription_service/SS-20120601.shtml",
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
+            "title": "PDS Mars Reconnaissance Orbiter Data 21"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MSL-M-CHEMIN-5-RDR-V1.0",
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
+            "description": "The CheMin instrument determines the mineralogy and elemental composition of powdered samples through the combined application of X-ray diffraction (XRD, producing mineral identification and quantification) and X-ray fluorescence (chemical analysis based on Energy Dispersive Histograms, EDH). This CheMin RDR data set contains mineral identification, abundance, and estimated errors derived from CheMin observations.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.msl-m-chemin-5-rdr-v1.0_g8ap-n4re",
+            "issued": "2018-06-26",
+            "keyword": [
+                "mars science laboratory",
+                "mars"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MSL-M-CHEMIN-5-RDR-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.msl-m-chemin-5-rdr-v1.0_g8ap-n4re",
-            "description": "The CheMin instrument determines the mineralogy and elemental composition of powdered samples through the combined application of X-ray diffraction (XRD, producing mineral identification and quantification) and X-ray fluorescence (chemical analysis based on Energy Dispersive Histograms, EDH). This CheMin RDR data set contains mineral identification, abundance, and estimated errors derived from CheMin observations.",
-            "title": "MSL MARS CHEMISTRY AND MINERALOGY 5 RDR V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "MSL MARS CHEMISTRY AND MINERALOGY 5 RDR V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-EXT1-1424-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the ROSETTA EXTENSION 1 phase 2016-01-01 to 2016-04-05. It is a Global Gravity measurement at the comet 67P and covers the time 2016-02-15T02:44:10.000 to 2016-02-15T11:50:18.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-ext1-1424-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-EXT1-1424-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-ext1-1424-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the ROSETTA EXTENSION 1 phase 2016-01-01 to 2016-04-05. It is a Global Gravity measurement at the comet 67P and covers the time 2016-02-15T02:44:10.000 to 2016-02-15T11:50:18.000.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     ROSETTA EXTENSION 1 1424 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     ROSETTA EXTENSION 1 1424 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-4-PRL-67P-M05-STRLIGHT-V1.0",
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
+            "description": "This CODMAC level 4 data set contains solar stray light corrected, radiometric calibrated and geometric distortion corrected (resampled) image data in W/m^2/sr/nm, acquired by the OSIRIS Wide Angle Camera on the Rosetta spacecraft during the PRELANDING mission phase, covering the period from 2014-07-02T08:35:00.000 to 2014-08-01T09:59:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V1.0 is the first version of this dataset: Lien corrected dataset after October 2018 PSA/PDS external peer review.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-4-prl-67p-m05-strlight-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-4-PRL-67P-M05-STRLIGHT-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-4-prl-67p-m05-strlight-v1.0",
-            "description": "This CODMAC level 4 data set contains solar stray light corrected, radiometric calibrated and geometric distortion corrected (resampled) image data in W/m^2/sr/nm, acquired by the OSIRIS Wide Angle Camera on the Rosetta spacecraft during the PRELANDING mission phase, covering the period from 2014-07-02T08:35:00.000 to 2014-08-01T09:59:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V1.0 is the first version of this dataset: Lien corrected dataset after October 2018 PSA/PDS external peer review.",
-            "title": "ROSETTA-ORBITER 67P OSIWAC 4 PRL-MTP005 RDR-STRLIGHT V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P OSIWAC 4 PRL-MTP005 RDR-STRLIGHT V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.7927/H41834D6",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Center for International Earth Science Information Network - CIESIN - Columbia University. 2015-01-21. Population Exposure Estimates in Proximity to Nuclear Power Plants, Country-Level Aggregates. Version 1.00. Palisades, NY. Archived by National Aeronautics and Space Administration, U.S. Government, NASA Socioeconomic Data and Applications Center (SEDAC). https://doi.org/10.7927/H41834D6. https://doi.org/10.7927/H41834D6.",
-            "issued": "2015-01-21",
-            "temporal": "1990-01-01T00:00:00Z/2010-01-01T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2015-01-21",
-            "references": [
-                "https://doi.org/10.7927/H4WH2MXH"
-            ],
-            "keyword": [
-                "human dimensions",
-                "public health",
-                "population",
-                "environmental impacts",
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
-            "identifier": "C1000000460-SEDAC",
-            "description": "The Population Exposure Estimates in Proximity to Nuclear Power Plants, Country-Level Aggregates data set consists of country-level estimates of total, urban, and rural populations and land area, country-wide, that are in proximity to a nuclear power plant. This data set was created using a global data set of point locations of nuclear power plants, with buffer zones at 30km, 75km, 150km, 300km, 600km, and 1200km, and the Global Population Count Grid Time Series Estimates, Version 1 to estimate the population within each buffer zone for the years 1990, 2000, and 2010. Global Rural-Urban Mapping Project, Version 1 (GRUMPv1) Land and Geographic Unit Area Grids were used to estimate land area within each buffer zone. The GRUMPv1 Urban Extents Grid was used to further delineate population and land area estimates within urban and rural areas. All grids used for population, land area, and urban mask were of 1 km (30 arc-second) resolution.",
-            "release-place": "Palisades, NY",
-            "graphic-preview-description": "Sample browse graphic of the data set.",
             "creator": "Center for International Earth Science Information Network - CIESIN - Columbia University",
-            "title": "Population Exposure Estimates in Proximity to Nuclear Power Plants, Country-Level Aggregates",
-            "graphic-preview-file": "https://sedac.ciesin.columbia.edu/downloads/maps/energy/energy-pop-exposure-nuclear-plants-country/sedac-logo.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The Population Exposure Estimates in Proximity to Nuclear Power Plants, Country-Level Aggregates data set consists of country-level estimates of total, urban, and rural populations and land area, country-wide, that are in proximity to a nuclear power plant. This data set was created using a global data set of point locations of nuclear power plants, with buffer zones at 30km, 75km, 150km, 300km, 600km, and 1200km, and the Global Population Count Grid Time Series Estimates, Version 1 to estimate the population within each buffer zone for the years 1990, 2000, and 2010. Global Rural-Urban Mapping Project, Version 1 (GRUMPv1) Land and Geographic Unit Area Grids were used to estimate land area within each buffer zone. The GRUMPv1 Urban Extents Grid was used to further delineate population and land area estimates within urban and rural areas. All grids used for population, land area, and urban mask were of 1 km (30 arc-second) resolution.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.7927%2FH41834D6",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.7927%2FH41834D6",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/downloads/maps/energy/energy-pop-exposure-nuclear-plants-country/sedac-logo.jpg",
-                    "description": "Sample browse graphic of the data set.",
                     "@type": "dcat:Distribution",
+                    "description": "Sample browse graphic of the data set.",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/downloads/maps/energy/energy-pop-exposure-nuclear-plants-country/sedac-logo.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/energy-pop-exposure-nuclear-plants-country/data-download",
-                    "description": "Data Download Page",
                     "@type": "dcat:Distribution",
+                    "description": "Data Download Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/energy-pop-exposure-nuclear-plants-country/data-download",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://sedac.ciesin.columbia.edu/data/set/energy-pop-exposure-nuclear-plants-country/docs",
-                    "description": "Documentation Page",
                     "@type": "dcat:Distribution",
+                    "description": "Documentation Page",
+                    "downloadURL": "http://sedac.ciesin.columbia.edu/data/set/energy-pop-exposure-nuclear-plants-country/docs",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/energy-pop-exposure-nuclear-plants-country",
-                    "description": "Data Set\u00a0Overview Page",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set\u00a0Overview Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/energy-pop-exposure-nuclear-plants-country",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "graphic-preview-description": "Sample browse graphic of the data set.",
+            "graphic-preview-file": "https://sedac.ciesin.columbia.edu/downloads/maps/energy/energy-pop-exposure-nuclear-plants-country/sedac-logo.jpg",
+            "identifier": "C1000000460-SEDAC",
+            "issued": "2015-01-21",
+            "keyword": [
+                "human dimensions",
+                "public health",
+                "population",
+                "environmental impacts",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.7927/H41834D6",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2015-01-21",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "SEDAC"
+            },
+            "references": [
+                "https://doi.org/10.7927/H4WH2MXH"
+            ],
+            "release-place": "Palisades, NY",
             "spatial": "-180.0 -55.77 180.0 83.63",
+            "temporal": "1990-01-01T00:00:00Z/2010-01-01T00:00:00Z",
             "theme": [
                 "ENERGY",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Population Exposure Estimates in Proximity to Nuclear Power Plants, Country-Level Aggregates"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.nasa.gov/d/g8ge-waq2",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "keyword": [
-                "nucleic acid extraction",
-                "spaceflight",
-                "sequence analysis data transformation",
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
-            "identifier": "nasa_genelab_GLDS-65_g8ge-waq2",
             "description": "The environmental microbiome study was designed to decipher microbial diversity of the International Space Station surfaces in terms of spatial and temporal distributions using 16S and ITS iTag Illumina sequencing. We hypothesized that the microbial population of environmental surfaces changes in time due to astronauts xe2 x80 x99 activity and might be location specific. The environmental samples were collected with the polyester wipes from eight different locations in the ISS during two consecutive sampling sessions (three months apart). The specific objective was to unveil the viable microbial diversity of each location during two separate sessions in terms of abundance and richness of the communities. The International Space Station (ISS) as a closed built environment has its own environmental microbiome which is shaped by microgravity radiation and limited human presence. The microbial diversity associated with ISS environmental surfaces was investigated during this study. Polyester wipes and contact slides were used for sampling of eight various surface locations on the ISS at different time periods. The samples were retrieved and analyzed immediately upon the return to the Earth (via Soyuz TMA-14M or Dragon capsule from SpaceX). After surface sample collection contact slides containing nutrient media for the growth of bacteria and fungi were incubated at 25 xcb x9aC. The polyester wipes were processed to measure microbial burden (R2A Blood Agar and Potato Dextrose Agar) and recover cultivable bacteria as well as fungi. Subsequently viable microbial burden was assessed using Adenosine Triphosphate (ATP) assay and quantitative polymerase chain reaction (PCR) methods after propidium monoazide (PMA) treatment. The 16S-tag and metagenome analyses were used to elucidate viable microbial diversity. The cultivable bacterial population yield from the polyester wipes was very high (5 to 7-logs) when compared with the contact slides (102 to 103 CFU/m2). The PMA-qPCR analysis showed considerable variation of viable bacterial population (105 to 109 16S rDNA gene copies/m2) among locations sampled. Unlike contact slides polyester wipes cover much larger sample surface (~1 m2) and produce much more reliable results of the microbial diversity of the ISS covering both cultivable and non-cultivable species. The cultivable total and viable microbial diversity was determined utilizing state-of-the art molecular techniques. The implementation of the PMA assay before DNA extraction allowed distinguishing viable microorganisms which is crucial for determining their role to the crew health the ISS maintenance and the general knowledge of the closed environmentally controlled built systems.",
-            "title": "Microbial Observatory (ISS-MO): Microbial diversity",
-            "programCode": [
-                "026:005"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-65",
-                    "description": "GeneLab Study Page",
                     "@type": "dcat:Distribution",
+                    "description": "GeneLab Study Page",
+                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-65",
+                    "mediaType": "text/html",
                     "title": "Microbial Observatory (ISS-MO): Microbial diversity"
                 }
             ],
+            "identifier": "nasa_genelab_GLDS-65_g8ge-waq2",
+            "issued": "2021-05-21",
+            "keyword": [
+                "nucleic acid extraction",
+                "spaceflight",
+                "sequence analysis data transformation",
+                "sample collection",
+                "nucleic acid sequencing",
+                "library construction"
+            ],
+            "landingPage": "https://data.nasa.gov/d/g8ge-waq2",
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
+            "title": "Microbial Observatory (ISS-MO): Microbial diversity"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ASDC/SUBORBITAL/STAQS/DATA001/GV/AircraftRemoteSensing/GCAS_1",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2024-08-09. https://doi.org/10.5067/ASDC/SUBORBITAL/STAQS/DATA001/GV/AircraftRemoteSensing/GCAS_1.",
-            "issued": "2023-06-26",
-            "temporal": "2023-06-26T00:00:00Z/2023-08-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-08-16",
-            "keyword": [
-                "atmospheric chemistry",
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
-                "name": "Not provided"
-            },
-            "identifier": "C2862468660-LARC_CLOUD",
             "description": "STAQS_AircraftRemoteSensing_JSC-GV_GCAS_Data is the remotely sensed trace gas data for the JSC Gulfstream V aircraft taken by the GEOstationary Coastal and Air Pollution Events (GEO-CAPE) Airborne Simulator (GCAS) instrument as part of the Synergistic TEMPO Air Quality Science (STAQS) mission. Data collection for this product is complete.\r\n\r\nLaunched in April 2023, NASA\u2019s Tropospheric Emissions: Monitoring of Pollution (TEMPO) satellite monitors major air pollutants across North America every daylight hour at high spatial resolution at a geostationary orbit (GEO). With these measurements, NASA\u2019s STAQS mission seeks to integrate TEMPO satellite observations with traditional air quality monitoring to improve understanding of air quality science and enhance societal benefit. STAQS is being conducted during summer 2023, targeting urban areas, including Los Angeles, New York City, and Chicago. As part of the mission two aircraft will be outfitted with various remote sensing payloads. The Johnson Space Center (JSC) Gulfstream-V (G-V) aircraft will feature the GeoCAPE Airborne Simulator (GCAS) and combined High Spectral Resolution Lidar-2 (HSRL-2) and Ozone Differential Absorption Lidar (DIAL). This payload provides repeated high-resolution mapping of NO2, HCHO, ozone, and aerosols up to 3x per day over targeted cities. NASA Langley Research Center\u2019s (LaRC\u2019s) Gulfstream-III will measure city-scale emissions 2x per day over the targeted cities with the High-Altitude Lidar Observatory (HALO) and Airborne Visible InfraRed Imaging Spectrometer \u2013 Next Generation (AVIRS-NG). STAQS will also incorporate ground-based tropospheric ozone profiles from the NASA Tropospheric Ozone Lidar Network (TOLNet), NO2, HCHO, and ozone measurements from Pandora spectrometers, and will leverage existing networks operated by the EPA and state air quality agencies. The primary goal of STAQS is to improve our current understanding of air quality science under the TEMPO field of regard. Further goals include evaluating TEMPO level 2 data products, interpreting the temporal and spatial evolution of air quality events tracked by TEMPO, improving temporal estimates of anthropogenic, biogenic, and greenhouse gas emissions, assessing the benefit of assimilating TEMPO data into chemical transport models, and linking air quality patterns to socio-demographic data.",
-            "title": "STAQS JSC GV GEOstationary Coastal and Air Pollution Events (GEO-CAPE) Airborne Simulator Data",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC%2FSUBORBITAL%2FSTAQS%2FDATA001%2FGV%2FAircraftRemoteSensing%2FGCAS_1",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC%2FSUBORBITAL%2FSTAQS%2FDATA001%2FGV%2FAircraftRemoteSensing%2FGCAS_1",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www-air.larc.nasa.gov/missions/staqs/",
-                    "description": "STAQS Project Home Page",
                     "@type": "dcat:Distribution",
+                    "description": "STAQS Project Home Page",
+                    "downloadURL": "https://www-air.larc.nasa.gov/missions/staqs/",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://espo.nasa.gov/staqs/content/STAQS",
-                    "description": "STAQS ESPO Home Page",
                     "@type": "dcat:Distribution",
+                    "description": "STAQS ESPO Home Page",
+                    "downloadURL": "https://espo.nasa.gov/staqs/content/STAQS",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://csl.noaa.gov/projects/ages/staqs/",
-                    "description": "NOAA CSL Overview of STAQS",
                     "@type": "dcat:Distribution",
+                    "description": "NOAA CSL Overview of STAQS",
+                    "downloadURL": "https://csl.noaa.gov/projects/ages/staqs/",
+                    "mediaType": "text/html",
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
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2862468660-LARC_CLOUD",
-                    "description": "Earthdata Search for STAQS_AircraftRemoteSensing_JSC-GV_GCAS_Data_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for STAQS_AircraftRemoteSensing_JSC-GV_GCAS_Data_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2862468660-LARC_CLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/ASDC/SUBORBITAL/STAQS/DATA001/GV/AircraftRemoteSensing/GCAS_1",
-                    "description": "DOI data set landing page for STAQS_AircraftRemoteSensing_JSC-GV_GCAS_Data_1",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for STAQS_AircraftRemoteSensing_JSC-GV_GCAS_Data_1",
+                    "downloadURL": "https://doi.org/10.5067/ASDC/SUBORBITAL/STAQS/DATA001/GV/AircraftRemoteSensing/GCAS_1",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 }
             ],
+            "identifier": "C2862468660-LARC_CLOUD",
+            "issued": "2023-06-26",
+            "keyword": [
+                "atmospheric chemistry",
+                "atmosphere",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/ASDC/SUBORBITAL/STAQS/DATA001/GV/AircraftRemoteSensing/GCAS_1",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2023-08-16",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Not provided"
+            },
             "spatial": "-120.3 33.36 -72.0 44.56",
+            "temporal": "2023-06-26T00:00:00Z/2023-08-17T00:00:00Z",
             "theme": [
                 "STAQS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "STAQS JSC GV GEOstationary Coastal and Air Pollution Events (GEO-CAPE) Airborne Simulator Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/VIIRS/WATVP_M3_VIIRS_SNPP.001",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "NASA VIIRS Atmosphere SIPS. 2020-01-15. VIIRS/SNPP Water Vapor Level-3 monthly 0.5 x 0.5 degree grid. Version 1. MODAPS at NASA/GSFC. Archived by National Aeronautics and Space Administration, U.S. Government, L1 and Atmosphere Archive and Distribution System (LAADS). https://doi.org/10.5067/VIIRS/WATVP_M3_VIIRS_SNPP.001. https://doi.org/10.5067/VIIRS/WATVP_M3_VIIRS_SNPP.001.",
-            "issued": "2020-01-06",
-            "temporal": "2012-05-01T00:00:00Z/2024-04-08T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-06",
-            "keyword": [
-                "atmosphere",
-                "earth science",
-                "atmospheric water vapor"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "undefined",
                 "hasEmail": "mailto:sips.support@ssec.wisc.edu"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Not provided"
-            },
-            "identifier": "C1682050863-LAADS",
-            "description": "The VIIRS/SNPP Water Vapor Level-3 monthly 0.5 x 0.5 degree grid Product provide total column water vapor (TPW) properties from merged VIIRS infrared measurements and Cross-track Infrared Sounder (CrIS) plus Advanced Technology Microwave Sounder (ATMS) water vapor soundings to continue the depiction of global moisture at a higher spatial resolution started with MODIS on the Terra and Aqua platforms.  Level-3 global 0.5 degree by 0.5 degree spatial resolution daily mean data products (called WATVP_M3_VIIRS_SNPP) is derived by using a gridding software (called Yori) developed at the University of Wisconsin, Madison, Space Science and Engineering Center (Veglio et al., 2018), and implemented by the NASA VIIRS Atmosphere Science Investigator-led Processing System (SIPS). The Yori has been adapted for the VIIRS TPW products and is processed using the VIIRS Level-2 Water Vapor products (WATVP_L2_VIIRS_SNPP) separated by day and night. The mean and the standard deviation of each Level-2 water vapor product are calculated for each grid cell. The sum, the square of the sum of each product, and the number of pixels in the cells are also stored in the Level-3 (monthly) output files for further aggregation purposes.",
-            "release-place": "MODAPS at NASA/GSFC",
             "creator": "NASA VIIRS Atmosphere SIPS",
-            "title": "VIIRS/SNPP Water Vapor Level-3 monthly 0.5 x 0.5 degree grid",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The VIIRS/SNPP Water Vapor Level-3 monthly 0.5 x 0.5 degree grid Product provide total column water vapor (TPW) properties from merged VIIRS infrared measurements and Cross-track Infrared Sounder (CrIS) plus Advanced Technology Microwave Sounder (ATMS) water vapor soundings to continue the depiction of global moisture at a higher spatial resolution started with MODIS on the Terra and Aqua platforms.  Level-3 global 0.5 degree by 0.5 degree spatial resolution daily mean data products (called WATVP_M3_VIIRS_SNPP) is derived by using a gridding software (called Yori) developed at the University of Wisconsin, Madison, Space Science and Engineering Center (Veglio et al., 2018), and implemented by the NASA VIIRS Atmosphere Science Investigator-led Processing System (SIPS). The Yori has been adapted for the VIIRS TPW products and is processed using the VIIRS Level-2 Water Vapor products (WATVP_L2_VIIRS_SNPP) separated by day and night. The mean and the standard deviation of each Level-2 water vapor product are calculated for each grid cell. The sum, the square of the sum of each product, and the number of pixels in the cells are also stored in the Level-3 (monthly) output files for further aggregation purposes.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FVIIRS%2FWATVP_M3_VIIRS_SNPP.001",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FVIIRS%2FWATVP_M3_VIIRS_SNPP.001",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/search/order/2/WATVP_M3_VIIRS_SNPP--5110",
-                    "description": "Search and order products from LAADS website.",
                     "@type": "dcat:Distribution",
+                    "description": "Search and order products from LAADS website.",
+                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/search/order/2/WATVP_M3_VIIRS_SNPP--5110",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through LAADS"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/archive/allData/5110/WATVP_M3_VIIRS_SNPP/",
-                    "description": "Direct access to WATVP_M3_VIIRS_SNPP data set.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct access to WATVP_M3_VIIRS_SNPP data set.",
+                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/archive/allData/5110/WATVP_M3_VIIRS_SNPP/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/missions-and-measurements/viirs/SNPPVIIRSWATVP001UserGuide2019.pdf",
-                    "description": "Suomi-NPP VIIRS WATVP Products User Guide",
                     "@type": "dcat:Distribution",
+                    "description": "Suomi-NPP VIIRS WATVP Products User Guide",
+                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/missions-and-measurements/viirs/SNPPVIIRSWATVP001UserGuide2019.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/missions-and-measurements/viirs/SNPPVIIRSWATVP001ATBD2019.pdf",
-                    "description": "VIIRS/Suomi-NPP Water Vapor Products Algorithm Theoretical Basis Document",
                     "@type": "dcat:Distribution",
+                    "description": "VIIRS/Suomi-NPP Water Vapor Products Algorithm Theoretical Basis Document",
+                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/missions-and-measurements/viirs/SNPPVIIRSWATVP001ATBD2019.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's algorithm theoretical basis document"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/opendap/allData/5110/WATVP_M3_VIIRS_SNPP/contents.html",
-                    "description": "Direct access to product's OPeNDAP directory",
                     "@type": "dcat:Distribution",
+                    "description": "Direct access to product's OPeNDAP directory",
+                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/opendap/allData/5110/WATVP_M3_VIIRS_SNPP/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 }
             ],
+            "identifier": "C1682050863-LAADS",
+            "issued": "2020-01-06",
+            "keyword": [
+                "atmosphere",
+                "earth science",
+                "atmospheric water vapor"
+            ],
+            "landingPage": "https://doi.org/10.5067/VIIRS/WATVP_M3_VIIRS_SNPP.001",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2020-01-06",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Not provided"
+            },
+            "release-place": "MODAPS at NASA/GSFC",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2012-05-01T00:00:00Z/2024-04-08T00:00:00Z",
             "theme": [
                 "Suomi-NPP",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "VIIRS/SNPP Water Vapor Level-3 monthly 0.5 x 0.5 degree grid"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1597",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Prather, M.J., C.M. Flynn, A. Fiore, G. Correa, S.A. Strode, S.D. Steenrod, L.T. Murray, and J.-F. Lamarque. 2018. ATom: Simulated Data Stream for Modeling ATom-like Measurements. ORNL DAAC, Oak Ridge, Tennessee, USA. https://doi.org/10.3334/ORNLDAAC/1597",
-            "issued": "2018-08-08",
-            "temporal": "1997-08-01T00:00:00Z/2016-08-21T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-06-12",
-            "keyword": [
-                "earth science",
-                "air quality",
-                "atmosphere",
-                "atmospheric chemistry",
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
-            "identifier": "C2675771133-ORNL_CLOUD",
             "description": "This dataset provides a simulated data stream representative of an Atmospheric Tomography mission (ATom) data collection flight and also modeled reactivities for ozone (O3) production and loss and methane (CH4) loss from six global atmospheric chemistry models: CAM, GEOS-Chem, GFDL, GISS-E2.1, GMI, and UCI. The simulated data include concentrations of selected atmospheric trace gases for 14,880 air parcels along a simulated north-south ATom flight path along 180-degrees longitude over the Pacific basin. Each of the six models produced ozone production and loss and methane loss reactivities initialized using the simulated data beginning with five different days in August (8-01, 8-06, 8-11, 8-16, 8-21). Modeled years for each individual model varied from 1997 to 2016.",
-            "graphic-preview-description": "Direct parcel-by-parcel comparisonof modeled reactivities (a, P-O3; b, L-O3; c, L-CH4; all ppb/day) and photolysis rates (d, J-NO2; e, J-O1D; all /sec) calculated for the 14,880 simulated air parcels. Each point is an average over the 5 simulated dates in August (8/01, 8/06, 8/11, 8/16, 8/21). The 1:1 line is shown (black dashed) for each plot. The reference values (X axis) are the average of 3 similar models (GSFC, GC, UCI) selected by examining the rms differences across all the models (see text). Note that the model points are plotted successively on top of one another and thus the earlier-plotted models may appear less frequent: in order, NCAR (black), GFDL (magenta), GISS (cyan), GC (blue), UCI (red), GSFC (green). (from Prather et al. 2018)",
-            "title": "ATom: Simulated Data Stream for Modeling ATom-like Measurements",
-            "graphic-preview-file": "https://daac.ornl.gov/ATOM/guides/ATom_Simulated_Data_Fig1.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1597",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1597",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/atom/ATom_Simulated_Data/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/atom/ATom_Simulated_Data/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/ATOM/guides/ATom_Simulated_Data.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/ATOM/guides/ATom_Simulated_Data.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1597",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1597",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/atom/ATom_Simulated_Data/comp/ATom_Simulated_Data.pdf",
-                    "description": "ATom: Simulated Data Stream for Modeling ATom-like Measurements: ATom_Simulated_Data.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "ATom: Simulated Data Stream for Modeling ATom-like Measurements: ATom_Simulated_Data.pdf",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/atom/ATom_Simulated_Data/comp/ATom_Simulated_Data.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://daac.ornl.gov/ATOM/guides/ATom_Simulated_Data_Fig1.png",
-                    "description": "Direct parcel-by-parcel comparisonof modeled reactivities (a, P-O3; b, L-O3; c, L-CH4; all ppb/day) and photolysis rates (d, J-NO2; e, J-O1D; all /sec) calculated for the 14,880 simulated air parcels. Each point is an average over the 5 simulated dates in August (8/01, 8/06, 8/11, 8/16, 8/21). The 1:1 line is shown (black dashed) for each plot. The reference values (X axis) are the average of 3 similar models (GSFC, GC, UCI) selected by examining the rms differences across all the models (see text). Note that the model points are plotted successively on top of one another and thus the earlier-plotted models may appear less frequent: in order, NCAR (black), GFDL (magenta), GISS (cyan), GC (blue), UCI (red), GSFC (green). (from Prather et al. 2018)",
                     "@type": "dcat:Distribution",
+                    "description": "Direct parcel-by-parcel comparisonof modeled reactivities (a, P-O3; b, L-O3; c, L-CH4; all ppb/day) and photolysis rates (d, J-NO2; e, J-O1D; all /sec) calculated for the 14,880 simulated air parcels. Each point is an average over the 5 simulated dates in August (8/01, 8/06, 8/11, 8/16, 8/21). The 1:1 line is shown (black dashed) for each plot. The reference values (X axis) are the average of 3 similar models (GSFC, GC, UCI) selected by examining the rms differences across all the models (see text). Note that the model points are plotted successively on top of one another and thus the earlier-plotted models may appear less frequent: in order, NCAR (black), GFDL (magenta), GISS (cyan), GC (blue), UCI (red), GSFC (green). (from Prather et al. 2018)",
+                    "downloadURL": "https://daac.ornl.gov/ATOM/guides/ATom_Simulated_Data_Fig1.png",
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
+            "graphic-preview-description": "Direct parcel-by-parcel comparisonof modeled reactivities (a, P-O3; b, L-O3; c, L-CH4; all ppb/day) and photolysis rates (d, J-NO2; e, J-O1D; all /sec) calculated for the 14,880 simulated air parcels. Each point is an average over the 5 simulated dates in August (8/01, 8/06, 8/11, 8/16, 8/21). The 1:1 line is shown (black dashed) for each plot. The reference values (X axis) are the average of 3 similar models (GSFC, GC, UCI) selected by examining the rms differences across all the models (see text). Note that the model points are plotted successively on top of one another and thus the earlier-plotted models may appear less frequent: in order, NCAR (black), GFDL (magenta), GISS (cyan), GC (blue), UCI (red), GSFC (green). (from Prather et al. 2018)",
+            "graphic-preview-file": "https://daac.ornl.gov/ATOM/guides/ATom_Simulated_Data_Fig1.png",
+            "identifier": "C2675771133-ORNL_CLOUD",
+            "issued": "2018-08-08",
+            "keyword": [
+                "earth science",
+                "air quality",
+                "atmosphere",
+                "atmospheric chemistry",
+                "atmospheric water vapor"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1597",
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
             "spatial": "178.9 -59.8 180.0 59.8",
+            "temporal": "1997-08-01T00:00:00Z/2016-08-21T23:59:59Z",
             "theme": [
                 "ATom",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "ATom: Simulated Data Stream for Modeling ATom-like Measurements"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-3-PRL-67PCHURYUMOV-M05-V2.0",
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
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Aeronautics and Space Administration"
-            },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-3-prl-67pchuryumov-m05-v2.0",
             "description": "This data set contains images acquired by the OSIRIS Narrow Angle Camera during the PRELANDING phase of the Rosetta mission at the comet 67P, covering the period from 2014-07-02T08:35:00.000 to 2014-08-01T09:59:59.000. This version V2.0 supersedes previous deliveries of the same dataset.",
-            "title": "ROSETTA-ORBITER PRELANDING OSINAC 3 RDR MTP005 V2.0",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-3-prl-67pchuryumov-m05-v2.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-3-PRL-67PCHURYUMOV-M05-V2.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
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
+            "title": "ROSETTA-ORBITER PRELANDING OSINAC 3 RDR MTP005 V2.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=GO-J-PWS-2-EDR-WAVEFORM-1KHZ-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This data set includes wideband waveform measurements from the Galileo plasma wave receiver obtained during Jupiter orbital operations. These data were obtained during selected observation periods near perijove, satellite encounters and other select times. These measurements are electric waveforms obtained by rapidly sampling the potential at the input to the receiver from the electric dipole antenna.  The sample rates are 201,600/s, 25,200/s, or 3,150/s taken through bandpass filters of 80, 10, or 1 kHz, respectively.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.go-j-pws-2-edr-waveform-1khz-v1.0_g8jz-aiqh",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "europa",
                 "io",
@@ -801625,92 +801627,64 @@
                 "amalthea",
                 "jupiter"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=GO-J-PWS-2-EDR-WAVEFORM-1KHZ-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.go-j-pws-2-edr-waveform-1khz-v1.0_g8jz-aiqh",
-            "description": "This data set includes wideband waveform measurements from the Galileo plasma wave receiver obtained during Jupiter orbital operations. These data were obtained during selected observation periods near perijove, satellite encounters and other select times. These measurements are electric waveforms obtained by rapidly sampling the potential at the input to the receiver from the electric dipole antenna.  The sample rates are 201,600/s, 25,200/s, or 3,150/s taken through bandpass filters of 80, 10, or 1 kHz, respectively.",
-            "title": "GO JUPITER PWS EDITED EDR 1KHZ WAVEFORM RECEIVER V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "GO JUPITER PWS EDITED EDR 1KHZ WAVEFORM RECEIVER V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1528",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Verbyla, D. 2017. ABoVE: Last Day of Spring Snow, Alaska, USA, and Yukon Territory, Canada, 2000-2016. ORNL DAAC, Oak Ridge, Tennessee, USA. https://doi.org/10.3334/ORNLDAAC/1528",
-            "issued": "2017-11-10",
-            "temporal": "2000-04-01T00:00:00Z/2016-07-02T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-06-12",
-            "keyword": [
-                "cryosphere",
-                "ngda",
-                "national geospatial data asset",
-                "earth science",
-                "cryospheric indicators",
-                "climate indicators",
-                "terrestrial hydrosphere",
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
-            "identifier": "C2162119017-ORNL_CLOUD",
             "description": "This dataset provides the last day of spring snow cover for most of Alaska and the Yukon Territory for 2000 through 2016. The data are based on the MODIS daily snow cover fraction product (MODSCAG) and are provided at 500-m resolution. Pixels in the daily snow cover fraction grids from April 1 through July 31 were flagged as \"Snow\" if the snow fraction exceeded 0.15, resulting in a time series of binary daily snow cover grids for each year. The annual last day of spring snow for each pixel was identified by day of the year ranging from 91 (April 1) to 183 (July 2).",
-            "graphic-preview-description": "Browse Image",
-            "title": "ABoVE: Last Day of Spring Snow, Alaska, USA, and Yukon Territory, Canada, 2000-2016",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/sdat-tds/1528_1_fit.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1528",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1528",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/above/Last_Day_Spring_Snow/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/above/Last_Day_Spring_Snow/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/ABOVE/guides/Last_Day_Spring_Snow.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/ABOVE/guides/Last_Day_Spring_Snow.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1528",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1528",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
@@ -801726,200 +801700,204 @@
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://daac.ornl.gov/graphics/browse/sdat-tds/1528_1_fit.png",
-                    "description": "Browse Image",
                     "@type": "dcat:Distribution",
+                    "description": "Browse Image",
+                    "downloadURL": "https://daac.ornl.gov/graphics/browse/sdat-tds/1528_1_fit.png",
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
-                    "downloadURL": "https://webmap.ornl.gov/wcsdown/dataset.jsp?ds_id=1528",
-                    "description": "Web Coverage Service for this collection.",
                     "@type": "dcat:Distribution",
+                    "description": "Web Coverage Service for this collection.",
+                    "downloadURL": "https://webmap.ornl.gov/wcsdown/dataset.jsp?ds_id=1528",
+                    "mediaType": "text/html",
                     "title": "Use Web Coverage Service (WCS) to download the dataset's data"
                 }
             ],
+            "graphic-preview-description": "Browse Image",
+            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/sdat-tds/1528_1_fit.png",
+            "identifier": "C2162119017-ORNL_CLOUD",
+            "issued": "2017-11-10",
+            "keyword": [
+                "cryosphere",
+                "ngda",
+                "national geospatial data asset",
+                "earth science",
+                "cryospheric indicators",
+                "climate indicators",
+                "terrestrial hydrosphere",
+                "snow/ice"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1528",
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
             "spatial": "-175.76 52.17 -97.95 68.97",
+            "temporal": "2000-04-01T00:00:00Z/2016-07-02T23:59:59Z",
             "theme": [
                 "ABoVE",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "ABoVE: Last Day of Spring Snow, Alaska, USA, and Yukon Territory, Canada, 2000-2016"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=ODY-M-THM-5-VISGEO-V1.0",
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
-                "2001 mars odyssey",
-                "mars"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "not applicable",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ody-m-thm-5-visgeo-v1.0_g8md-qrtd",
+            "issued": "2021-05-21",
+            "keyword": [
+                "2001 mars odyssey",
+                "mars"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=ODY-M-THM-5-VISGEO-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ody-m-thm-5-visgeo-v1.0_g8md-qrtd",
-            "description": "not applicable",
-            "title": "ODYSSEY THEMIS VIS GEOMETRIC IMAGES V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ODYSSEY THEMIS VIS GEOMETRIC IMAGES V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C2331490344-OB_DAAC.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/GSFC/SED/ESD/GCDC/OB.DAAC.",
-            "issued": "2019-06-23",
-            "temporal": "2000-02-24T00:00:00Z/2023-02-28T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2019-10-01",
-            "keyword": [
-                "oceans",
-                "national geospatial data asset",
-                "ngda",
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
-            "identifier": "C2331490344-OB_DAAC",
             "description": "The Ocean Biology DAAC produces near real-time (quicklook) products using the best-available combination of ancillary data from meteorological and ozone data. As such, the inputs and the calibration used are less than optimal. Quicklook products provide a snapshot of the data during a short time period within a single orbit.",
-            "title": "Terra MODIS Global Mapped Fluorescence Line Height (FLH) - Near Real Time (NRT) Data, version R2022.0",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://oceandata.sci.gsfc.nasa.gov/directdataaccess/Level-3%20Mapped/Terra-MODIS/",
-                    "description": "NASA Ocean Color Web - Data Distribution Site",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Ocean Color Web - Data Distribution Site",
+                    "downloadURL": "https://oceandata.sci.gsfc.nasa.gov/directdataaccess/Level-3%20Mapped/Terra-MODIS/",
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
-                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/data/10.5067/TERRA/MODIS/L3M/FLH/2022",
-                    "description": "MODIS-Terra L3M Fluorescence Line Height (FLH) - Near Real Time (NRT) Dataset Landing Page",
                     "@type": "dcat:Distribution",
+                    "description": "MODIS-Terra L3M Fluorescence Line Height (FLH) - Near Real Time (NRT) Dataset Landing Page",
+                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/data/10.5067/TERRA/MODIS/L3M/FLH/2022",
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
+            "identifier": "C2331490344-OB_DAAC",
+            "issued": "2019-06-23",
+            "keyword": [
+                "oceans",
+                "national geospatial data asset",
+                "ngda",
+                "earth science",
+                "ocean optics"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C2331490344-OB_DAAC.html",
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
+            "temporal": "2000-02-24T00:00:00Z/2023-02-28T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Terra MODIS Global Mapped Fluorescence Line Height (FLH) - Near Real Time (NRT) Data, version R2022.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ZCRSHBM5HB23",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "UW-Madison Space Science and Engineering Center: Hank Revercomb; UMBC Atmospheric Spectroscopy Laboratory: Larrabee Strow. 2020-12-01. SNPPCrISL1B. Version 3. Suomi NPP CrIS Level 1B Full Spectral Resolution V3. Greenbelt, MD. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/ZCRSHBM5HB23. https://disc.gsfc.nasa.gov/datacollection/SNPPCrISL1B_3.html. Digital Science Data.",
-            "issued": "2015-11-02",
-            "temporal": "2015-11-02T00:00:00Z/2024-11-11T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-02",
-            "keyword": [
-                "spectral/engineering",
-                "infrared wavelengths",
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
-            "identifier": "C1952167468-GES_DISC",
-            "description": "The Cross-track Infrared Sounder (CrIS) Level 1B Full Spectral Resolution (FSR) data files contain radiance measurements along with ancillary spacecraft, instrument, and geolocation data of the CrIS instrument on the Suomi National Polar-orbiting Operational Environmental Satellite System (NPOESS) Preparatory Project (SNPP). In December 2014, the CrIS instrument on the SNPP satellite doubled the spectral resolution of shortwave infrared data being transmitted to the ground.  In November 2015, additional points were included at the ends of the longwave and shortwave interferograms to improve the quality of the calibration.  Prior to November 2, 2015 the data are only available in Normal Spectral Resolution (NSR), after November 2, 2015 at 16:06 UTC, the data are available in both NSR and Full Spectral Resolution. \n\nThe FSR files have 2,223 channels: 637 shortwave channels from 3.9 to 4.7 microns (2555 to 2150 cm-1), 869 midwave channels from 5.7 to 8.05 microns (1752.5 to 1242.5 cm-1), and 717 longwave channels from 9.1 to 15.41 microns (1096.25 to 648.75 cm-1). Each CrIS field-of-regard (FOR) contains 9 field-of-views (FOVs) arranged in a 3X3 array. The Level 1B files contain 30 FORs in the cross track direction and 45 in the along track direction. Data products are constructed on six minute boundaries.\n\nCrIS is designed to be used with the ATMS (Advanced Technology Microwave Sounder) instrument. Processing the data from both of these instruments together is referred to as CrIMSS (Cross-Track Infrared and Microwave Sounder Suite).\n\nIf you were redirected to this page from a DOI from\nan older version, please note this is the current\nversion of the product. Please contact the GES DISC\nuser support if you need information about previous\ndata collections.",
-            "release-place": "Greenbelt, MD",
-            "series-name": "SNPPCrISL1B",
             "creator": "UW-Madison Space Science and Engineering Center: Hank Revercomb; UMBC Atmospheric Spectroscopy Laboratory: Larrabee Strow",
-            "title": "Suomi NPP CrIS Level 1B Full Spectral Resolution V3 (SNPPCrISL1B) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/SNPPCrISL1B_v3.png",
-            "programCode": [
-                "026:001"
-            ],
+            "data-presentation-form": "Digital Science Data",
+            "description": "The Cross-track Infrared Sounder (CrIS) Level 1B Full Spectral Resolution (FSR) data files contain radiance measurements along with ancillary spacecraft, instrument, and geolocation data of the CrIS instrument on the Suomi National Polar-orbiting Operational Environmental Satellite System (NPOESS) Preparatory Project (SNPP). In December 2014, the CrIS instrument on the SNPP satellite doubled the spectral resolution of shortwave infrared data being transmitted to the ground.  In November 2015, additional points were included at the ends of the longwave and shortwave interferograms to improve the quality of the calibration.  Prior to November 2, 2015 the data are only available in Normal Spectral Resolution (NSR), after November 2, 2015 at 16:06 UTC, the data are available in both NSR and Full Spectral Resolution. \n\nThe FSR files have 2,223 channels: 637 shortwave channels from 3.9 to 4.7 microns (2555 to 2150 cm-1), 869 midwave channels from 5.7 to 8.05 microns (1752.5 to 1242.5 cm-1), and 717 longwave channels from 9.1 to 15.41 microns (1096.25 to 648.75 cm-1). Each CrIS field-of-regard (FOR) contains 9 field-of-views (FOVs) arranged in a 3X3 array. The Level 1B files contain 30 FORs in the cross track direction and 45 in the along track direction. Data products are constructed on six minute boundaries.\n\nCrIS is designed to be used with the ATMS (Advanced Technology Microwave Sounder) instrument. Processing the data from both of these instruments together is referred to as CrIMSS (Cross-Track Infrared and Microwave Sounder Suite).\n\nIf you were redirected to this page from a DOI from\nan older version, please note this is the current\nversion of the product. Please contact the GES DISC\nuser support if you need information about previous\ndata collections.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FZCRSHBM5HB23",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FZCRSHBM5HB23",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
@@ -801929,208 +801907,232 @@
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/SNPPCrISL1B_3.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/SNPPCrISL1B_3.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sounder.gesdisc.eosdis.nasa.gov/data/SNPP_Sounder_Level1/SNPPCrISL1B.3/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://sounder.gesdisc.eosdis.nasa.gov/data/SNPP_Sounder_Level1/SNPPCrISL1B.3/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=SNPPCrISL1B+003",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=SNPPCrISL1B+003",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sounder.gesdisc.eosdis.nasa.gov/opendap/SNPP_Sounder_Level1/SNPPCrISL1B.3/",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://sounder.gesdisc.eosdis.nasa.gov/opendap/SNPP_Sounder_Level1/SNPPCrISL1B.3/",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/repository/Mission/SNPP_Sounder/3.3_ScienceDataProductDocumentation/3.3.4_ProductGenerationAlgorithms/D0001-M01-S01-002_JPSS_ATBD_CrIS-SDR_C.pdf",
-                    "description": "Joint Polar Satellite System (JPSS) Cross Track Infrared Sounder (CrIS) Sensor Records (SDR) Algorithm Theoretical Basis Document (ATBD).",
                     "@type": "dcat:Distribution",
+                    "description": "Joint Polar Satellite System (JPSS) Cross Track Infrared Sounder (CrIS) Sensor Records (SDR) Algorithm Theoretical Basis Document (ATBD).",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/repository/Mission/SNPP_Sounder/3.3_ScienceDataProductDocumentation/3.3.4_ProductGenerationAlgorithms/D0001-M01-S01-002_JPSS_ATBD_CrIS-SDR_C.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's algorithm theoretical basis document"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/SNPP/CrIS_L1B_DeltaATBD_V3.0.pdf",
-                    "description": "NASA SNPP Cross Track Infrared Sounder (CrIS) Level 1B Delta Algorithm Theoretical Basis Document (ATBD)",
                     "@type": "dcat:Distribution",
+                    "description": "NASA SNPP Cross Track Infrared Sounder (CrIS) Level 1B Delta Algorithm Theoretical Basis Document (ATBD)",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/SNPP/CrIS_L1B_DeltaATBD_V3.0.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's algorithm theoretical basis document"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Sounder/NASA_CrIS_L1B_Product_Users_Guide_v3RevC.pdf",
-                    "description": "NASA Cross Track Infrared Sounder (CrIS) Level 1B Product Users Guide",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Cross Track Infrared Sounder (CrIS) Level 1B Product Users Guide",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Sounder/NASA_CrIS_L1B_Product_Users_Guide_v3RevC.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Sounder/NASA_CrIS_L1B_Quality_Flags_V3.pdf",
-                    "description": "Cross-track Infrared Sounder (CrIS) Level 1B Quality Flags Description Document",
                     "@type": "dcat:Distribution",
+                    "description": "Cross-track Infrared Sounder (CrIS) Level 1B Quality Flags Description Document",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Sounder/NASA_CrIS_L1B_Quality_Flags_V3.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's data quality document"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Sounder/NASA_CrIS_L1B_Product_Test_Report_v3RevA.pdf",
-                    "description": "CrIS L1B Version 3 Product Test Report",
                     "@type": "dcat:Distribution",
+                    "description": "CrIS L1B Version 3 Product Test Report",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Sounder/NASA_CrIS_L1B_Product_Test_Report_v3RevA.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's product quality assessment"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Sounder/NASA_CrIS_L1B_Radiometric_Uncertainty_v3.pdf",
-                    "description": "CrIS L1B v3 Radiometric Uncertainty document",
                     "@type": "dcat:Distribution",
+                    "description": "CrIS L1B v3 Radiometric Uncertainty document",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Sounder/NASA_CrIS_L1B_Radiometric_Uncertainty_v3.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's product quality assessment"
                 }
             ],
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/SNPPCrISL1B_v3.png",
+            "identifier": "C1952167468-GES_DISC",
+            "issued": "2015-11-02",
+            "keyword": [
+                "spectral/engineering",
+                "infrared wavelengths",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/ZCRSHBM5HB23",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2024-11-02",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
+            },
+            "release-place": "Greenbelt, MD",
+            "series-name": "SNPPCrISL1B",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2015-11-02T00:00:00Z/2024-11-11T00:00:00Z",
             "theme": [
                 "SUOMI-NPP",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Suomi NPP CrIS Level 1B Full Spectral Resolution V3 (SNPPCrISL1B) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=CON-CAL-ALL-6-DOC-SET-V1.0",
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
-                "contour mission",
-                "unknown"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This collection contains documentation created in support and anticipation of the CONTOUR mission, by various contributors. It is provided here 'as is', in the form originally supplied by the authors.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.con-cal-all-6-doc-set-v1.0_g8n6-k3dx",
+            "issued": "2021-05-21",
+            "keyword": [
+                "contour mission",
+                "unknown"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=CON-CAL-ALL-6-DOC-SET-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.con-cal-all-6-doc-set-v1.0_g8n6-k3dx",
-            "description": "This collection contains documentation created in support and anticipation of the CONTOUR mission, by various contributors. It is provided here 'as is', in the form originally supplied by the authors.",
-            "title": "CONTOUR MISSION DOCUMENTATION SET V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "CONTOUR MISSION DOCUMENTATION SET V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC4-1263-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 4 phase 2015-10-22 to 2015-12-31. It is a Global Gravity measurement at the comet 67P and covers the time 2015-12-17T10:06:20.000 to 2015-12-17T15:46:31.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc4-1263-v1.0_g8nm-cfdq",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC4-1263-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc4-1263-v1.0_g8nm-cfdq",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 4 phase 2015-10-22 to 2015-12-31. It is a Global Gravity measurement at the comet 67P and covers the time 2015-12-17T10:06:20.000 to 2015-12-17T15:46:31.000.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 4 1263 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 4 1263 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC1-0531-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 1 phase 2014-11-20 to 2015-03-10. It is a Global Gravity measurement at the comet 67P and covers the time 2015-01-10T04:19:30.000 to 2015-01-10T11:50:52.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc1-0531-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC1-0531-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc1-0531-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 1 phase 2014-11-20 to 2015-03-10. It is a Global Gravity measurement at the comet 67P and covers the time 2015-01-10T04:19:30.000 to 2015-01-10T11:50:52.000.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 1 0531 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 1 0531 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MEX-M-PFS-2-EDR-EXT4-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "The Mars Express PFS data set contains raw (CODMAC Level 2) measurements from the Planetary Fourier Spectrometer collected during the fourth extension Mars orbit phases.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mex-m-pfs-2-edr-ext4-v1.0",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2021-05-21",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "internal source",
                 "deep space",
@@ -802139,560 +802141,536 @@
                 "mars express",
                 "responsivity"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MEX-M-PFS-2-EDR-EXT4-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mex-m-pfs-2-edr-ext4-v1.0",
-            "description": "The Mars Express PFS data set contains raw (CODMAC Level 2) measurements from the Planetary Fourier Spectrometer collected during the fourth extension Mars orbit phases.",
-            "title": "MARS EXPRESS MARS PFS EDR FOURTH\n                                  EXTENSION MISSION DATA V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "MARS EXPRESS MARS PFS EDR FOURTH\n                                  EXTENSION MISSION DATA V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.7265/N5000014",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Reconstructed North American Snow Extent, 1900-1993, Version 1. Version 1. Archived by National Aeronautics and Space Administration, U.S. Government, National Snow and Ice Data Center. https://doi.org/10.7265/N5000014.",
-            "issued": "1900-12-01",
-            "temporal": "1900-12-01T00:00:00Z/1993-03-31T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "1993-03-31",
-            "keyword": [
-                "snow/ice",
-                "earth science",
-                "cryosphere",
-                "terrestrial hydrosphere"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Allan Frei",
                 "hasEmail": "mailto:afrei@geo.hunter.cuny.edu"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NSIDC"
-            },
-            "identifier": "C1386246247-NSIDCV0",
             "description": "This data set contains reconstructed monthly North American snow extent values for November through March, 1900-1993. Investigators used a combination of satellite and station observations and based the reconstruction on linear regressions between the two types of observations. The data also includes standard errors of estimates as well as the observed values upon which the regressions were based.",
-            "title": "Reconstructed North American Snow Extent, 1900-1993, Version 1",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.7265%2FN5000014",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.7265%2FN5000014",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/forms/G02130_or.html?major_version=1",
-                    "description": "Direct download, with optional registration page.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download, with optional registration page.",
+                    "downloadURL": "https://nsidc.org/forms/G02130_or.html?major_version=1",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.7265/N5000014",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.7265/N5000014",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.7265/N5000014",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.7265/N5000014",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C1386246247-NSIDCV0",
+            "issued": "1900-12-01",
+            "keyword": [
+                "snow/ice",
+                "earth science",
+                "cryosphere",
+                "terrestrial hydrosphere"
+            ],
+            "landingPage": "https://doi.org/10.7265/N5000014",
+            "language": [
+                "en-US"
+            ],
+            "modified": "1993-03-31",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NSIDC"
+            },
             "spatial": "-125.0 35.0 -60.0 49.0",
+            "temporal": "1900-12-01T00:00:00Z/1993-03-31T23:59:59.999Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Reconstructed North American Snow Extent, 1900-1993, Version 1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/GRIP/INS/DATA101",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Goodman, Michael .2020. GRIP Hurricane and Tropical Storm Forecasts [indicate subset used]. Dataset available online from the NASA Global Hydrometeorology Resource Center DAAC, Huntsville, Alabama, U.S.A. DOI: http://dx.doi.org/10.5067/GRIP/INS/DATA101",
-            "issued": "2020-02-06",
-            "temporal": "2010-08-12T00:00:00Z/2010-11-14T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-05-31",
-            "keyword": [
-                "weather events",
-                "natural hazards",
-                "human dimensions",
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
-            "identifier": "C1979860341-GHRC_DAAC",
             "description": "The GRIP Hurricane and Tropical Storm Forecasts dataset consists of tropical cyclone model forecast tracks archived during the NASA Genesis and Rapid Intensification Processes (GRIP) field campaign. GRIP was one of three hurricane field campaigns conducted during the 2010 Atlantic/Pacific hurricane season. This tri-agency effort included NASA GRIP, the NSF Pre-Depression Investigation of Cloud-systems in the Tropics (PREDICT) and the NOAA Intensity Forecasting Experiment 2010 (IFEX10). The hurricane and tropical storm forecasts data files are available from August 12 through November 14, 2010 in ASCII text format with browse files in KML format, viewable in Google Earth.  The ASCII text files contain 5-day model \u201cconsensus\u201d forecasts and the KML browse files contain model forecasts ranging from 5-days to 10-days.",
-            "graphic-preview-description": "N/A",
-            "title": "GRIP Hurricane and Tropical Storm Forecasts V1",
-            "graphic-preview-file": "https://search.earthdata.nasa.gov/search?q=gripstorm/browse/",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGRIP%2FINS%2FDATA101",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGRIP%2FINS%2FDATA101",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=gripstorm",
-                    "description": "Files may be downloaded directly to your workstation from this link",
                     "@type": "dcat:Distribution",
+                    "description": "Files may be downloaded directly to your workstation from this link",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=gripstorm",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/browse_sample/fieldCampaigns/grip/gripstorm/gearth_grip1.PNG",
-                    "description": "Sample browse image",
                     "@type": "dcat:Distribution",
+                    "description": "Sample browse image",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/browse_sample/fieldCampaigns/grip/gripstorm/gearth_grip1.PNG",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/home/sites/default/files/6Jun11_200p_Kakar_GRIP_LA.pdf",
-                    "description": "Genesis and Rapid Intensification Processes (GRIP) Field Experiment",
                     "@type": "dcat:Distribution",
+                    "description": "Genesis and Rapid Intensification Processes (GRIP) Field Experiment",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/home/sites/default/files/6Jun11_200p_Kakar_GRIP_LA.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.nhc.noaa.gov/modelsummary.shtml",
-                    "description": "NHC Track and Intensity Models",
                     "@type": "dcat:Distribution",
+                    "description": "NHC Track and Intensity Models",
+                    "downloadURL": "https://www.nhc.noaa.gov/modelsummary.shtml",
+                    "mediaType": "text/html",
                     "title": "View information related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://web.uwm.edu/hurricane-models/models/models.html",
-                    "description": "Hurricane Forecast Model Output",
                     "@type": "dcat:Distribution",
+                    "description": "Hurricane Forecast Model Output",
+                    "downloadURL": "https://web.uwm.edu/hurricane-models/models/models.html",
+                    "mediaType": "text/html",
                     "title": "View information related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/grip/Storm_Forecasts/doc/gripstorm_dataset.pdf",
-                    "description": "The guide document contains detailed information about the dataset",
                     "@type": "dcat:Distribution",
+                    "description": "The guide document contains detailed information about the dataset",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/grip/Storm_Forecasts/doc/gripstorm_dataset.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.1175/BAMS-D-11-00232.1",
-                    "description": "NASA's Genesis and Rapid Intensification Processes (GRIP) Field Experiment",
                     "@type": "dcat:Distribution",
+                    "description": "NASA's Genesis and Rapid Intensification Processes (GRIP) Field Experiment",
+                    "downloadURL": "https://doi.org/10.1175/BAMS-D-11-00232.1",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.1175/WAF-D-13-00008.1",
-                    "description": "An Evaluation of Tropical Cyclone Genesis Forecasts from Global Numerical Models",
                     "@type": "dcat:Distribution",
+                    "description": "An Evaluation of Tropical Cyclone Genesis Forecasts from Global Numerical Models",
+                    "downloadURL": "https://doi.org/10.1175/WAF-D-13-00008.1",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.1175/MWR-D-13-00267.1",
-                    "description": "Characteristics of Tropical Easterly Wave Pouches during Tropical Cyclone Formation",
                     "@type": "dcat:Distribution",
+                    "description": "Characteristics of Tropical Easterly Wave Pouches during Tropical Cyclone Formation",
+                    "downloadURL": "https://doi.org/10.1175/MWR-D-13-00267.1",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.1029/2008GL035586",
-                    "description": "A dynamically\u2010based method for forecasting tropical cyclogenesis location in the Atlantic sector using global model products",
                     "@type": "dcat:Distribution",
+                    "description": "A dynamically\u2010based method for forecasting tropical cyclogenesis location in the Atlantic sector using global model products",
+                    "downloadURL": "https://doi.org/10.1029/2008GL035586",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.1175/MWR-D-10-05063.1",
-                    "description": "A First Look at the Structure of the Wave Pouch during the 2009 PREDICT\u2013GRIP Dry Runs over the Atlantic",
                     "@type": "dcat:Distribution",
+                    "description": "A First Look at the Structure of the Wave Pouch during the 2009 PREDICT\u2013GRIP Dry Runs over the Atlantic",
+                    "downloadURL": "https://doi.org/10.1175/MWR-D-10-05063.1",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/home/field-campaigns/grip",
-                    "description": "GRIP Field Campaign Project Homepage",
                     "@type": "dcat:Distribution",
+                    "description": "GRIP Field Campaign Project Homepage",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/home/field-campaigns/grip",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=gripstorm%2Fbrowse%2F",
-                    "description": "N/A",
                     "@type": "dcat:Distribution",
+                    "description": "N/A",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=gripstorm%2Fbrowse%2F",
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
+            "graphic-preview-file": "https://search.earthdata.nasa.gov/search?q=gripstorm/browse/",
+            "identifier": "C1979860341-GHRC_DAAC",
+            "issued": "2020-02-06",
+            "keyword": [
+                "weather events",
+                "natural hazards",
+                "human dimensions",
+                "earth science",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.5067/GRIP/INS/DATA101",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2022-05-31",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/MSFC/GHRC"
+            },
             "spatial": "-178.5 0.8 0.0 87.6",
+            "temporal": "2010-08-12T00:00:00Z/2010-11-14T00:00:00Z",
             "theme": [
                 "GRIP (HURRICANE)",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "GRIP Hurricane and Tropical Storm Forecasts V1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://c3.nasa.gov/dashlink/resources/215/",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2010-09-22",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
-            "keyword": [
-                "ames",
-                "dashlink",
-                "nasa"
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
-            "identifier": "DASHLINK_215",
             "description": "In this work, we propose a novel approach to perform Dependent Component Analysis (DCA). DCA can be thought as the separation of latent, dependent sources from their observed mixtures which is a more realistic model than Independent Component Analysis (ICA) where the sources are assumed to be independent. In general, the sources can be spatio-temporally dependent and the mixing system may be non-stationary. Here, we propose a DCA algorithm, that combines concepts of particle filters and Markov Chain Monte Carlo (MCMC) methods in order to separate non-stationary mixtures of spatially dependent Gaussian sources.",
-            "title": "Bayesian Separation of Non-Stationary Mixtures of Dependent Gaus",
-            "programCode": [
-                "026:029"
-            ],
             "distribution": [
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/publication/MAXENT_2005.pdf",
-                    "description": "Bayesian Separation of Non-Stationary Mixtures of Dependent Gaussian Sources",
                     "@type": "dcat:Distribution",
+                    "description": "Bayesian Separation of Non-Stationary Mixtures of Dependent Gaussian Sources",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/publication/MAXENT_2005.pdf",
+                    "mediaType": "application/pdf",
                     "title": "MAXENT_2005.pdf"
                 }
             ],
-            "accrualPeriodicity": "irregular"
+            "identifier": "DASHLINK_215",
+            "issued": "2010-09-22",
+            "keyword": [
+                "ames",
+                "dashlink",
+                "nasa"
+            ],
+            "landingPage": "https://c3.nasa.gov/dashlink/resources/215/",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:029"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Dashlink"
+            },
+            "title": "Bayesian Separation of Non-Stationary Mixtures of Dependent Gaus"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ASDC/SUBORBITAL/STRAT_Satellite_Data_1",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2023-11-20. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/ASDC/SUBORBITAL/STRAT_Satellite_Data_1.",
-            "issued": "1995-05-03",
-            "temporal": "1995-05-03T00:00:00Z/1996-12-20T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "1996-12-19",
-            "keyword": [
-                "atmosphere",
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
-                "name": "NASA/LARC/SD/ASDC"
-            },
-            "identifier": "C2770043737-LARC_ASDC",
             "description": "STRAT_Satellite_Data is the supplementary satellite data collected during the Stratospheric Tracers of Atmospheric Transport (STRAT) campaign. Satellite images from the GOES-7 and GOES-9 satellites are featured in this collection. Data collection for this product is complete.\r\n\r\nThe STRAT campaign was a field campaign conducted by NASA from May 1995 to February 1996. The primary goal of STRAT was to collect measurements of the change of long-lived tracers and functions of altitude, latitude, and season. These measurements were taken to aid with determining rates for global-scale transport and future distributions of high-speed civil transport (HSCT) exhaust that was emitted into the lower atmosphere. STRAT had four main objectives:  defining the rate of transport of trace gases from the stratosphere and troposphere (i.e., HSCT exhaust emissions), improving the understanding of dynamical coupling rates for transport of trace gases between tropical regions and higher latitudes and lower altitudes (between tropical regions, higher latitudes, and lower altitudes are where most ozone resides), improving understanding of chemistry in the upper troposphere and lower stratosphere, and finally, providing data sets for testing two-dimensional and three-dimensional models used in assessments of impacts from stratospheric aviation.  \r\n\r\nTo accomplish these objectives, the STRAT Science Team conducted various surface-based remote sensing and in-situ measurements. NASA flew the ER-2 aircraft along with balloons such as ozonesondes and radiosondes just below the tropopause in the Northern Hemisphere to collect data. Along with the ER-2 and balloons, NASA also utilized satellite imagery, theoretical models, and ground sites. The ER-2 collected data on HOx, NOy, CO2, ozone, water vapor, and temperature. The ER-2 also collected in-situ stratospheric measurements of N2O, CH4, CO, HCL, and NO using the Aircraft Laser Infrared Absorption Spectrometer (ALIAS). Ozonesondes and radiosondes were also deployed to collect data on CO2, NO/NOy, air temperature, pressure, and 3D wind. These balloons also took in-situ measurements of N2O, CFC-11, CH4, CO, HCL, and NO2 using the ALIAS. Ground stations were responsible for taking measurements of O3, ozone mixing ratio, pressure, and temperature. Satellites took infrared images of the atmosphere with the goal of aiding in completing STRAT objectives. Pressure and temperature models were created to help plan the mission.",
-            "title": "STRAT Supplementary Satellite Data Products",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC%2FSUBORBITAL%2FSTRAT_Satellite_Data_1",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC%2FSUBORBITAL%2FSTRAT_Satellite_Data_1",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://espo.nasa.gov/strat",
-                    "description": "ESPO Home Page for STRAT",
                     "@type": "dcat:Distribution",
+                    "description": "ESPO Home Page for STRAT",
+                    "downloadURL": "https://espo.nasa.gov/strat",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://espo.nasa.gov/strat/content/STRAT_Science_Overview",
-                    "description": "STRAT Science Overview",
                     "@type": "dcat:Distribution",
+                    "description": "STRAT Science Overview",
+                    "downloadURL": "https://espo.nasa.gov/strat/content/STRAT_Science_Overview",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2770043737-LARC_ASDC",
-                    "description": "Earthdata Search for STRAT_Satellite_Data_1",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for STRAT_Satellite_Data_1",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2770043737-LARC_ASDC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/ASDC/SUBORBITAL/STRAT_Satellite_Data_1",
-                    "description": "DOI for STRAT_Satellite_Data_1",
                     "@type": "dcat:Distribution",
+                    "description": "DOI for STRAT_Satellite_Data_1",
+                    "downloadURL": "https://doi.org/10.5067/ASDC/SUBORBITAL/STRAT_Satellite_Data_1",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/STRAT/Satellite_Data_1/",
-                    "description": "ASDC Direct Data Download for STRAT_Satellite_Data_1",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for STRAT_Satellite_Data_1",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/STRAT/Satellite_Data_1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 }
             ],
+            "identifier": "C2770043737-LARC_ASDC",
+            "issued": "1995-05-03",
+            "keyword": [
+                "atmosphere",
+                "atmospheric water vapor",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/ASDC/SUBORBITAL/STRAT_Satellite_Data_1",
+            "language": [
+                "en-US"
+            ],
+            "modified": "1996-12-19",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/LARC/SD/ASDC"
+            },
             "spatial": "<?xml version=\"1.0\" encoding=\"UTF-8\"?><gml:Polygon xmlns:gml=\"http://www.opengis.net/gml/3.2\" srsName=\"EPSG:9825\"><gml:outerBoundaryIs><gml:LinearRing><gml:posList>-2.14 -180.0 -2.14 180.0 68.23 180.0 68.23 -180.0 -2.14 -180.0</gml:posList></gml:LinearRing></gml:outerBoundaryIs><gml:innerBoundaryIs></gml:innerBoundaryIs></gml:Polygon>",
+            "temporal": "1995-05-03T00:00:00Z/1996-12-20T00:00:00Z",
             "theme": [
                 "STRAT",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "STRAT Supplementary Satellite Data Products"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-5-DDR-DERIVED-LIGHTCURVE-V14.0",
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
+            "description": "This is a compilation of published rotational parameters derived from lightcurve data for asteroids, based on the Warner et al. (2009) Asteroid Lightcurve Database. This is the version as of March 1, 2014. In addition to reported rotational parameters by individual paper, there is a summary file with the values adopted by Harris, Warner, and Pravec as the most likely correct values for each asteroid. The data set also contains files listing known binary asteroids and 'tumbling' asteroids.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-5-ddr-derived-lightcurve-v14.0_g8yy-47a5",
+            "issued": "2021-05-21",
+            "keyword": [
+                "support archives",
+                "asteroid"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-5-DDR-DERIVED-LIGHTCURVE-V14.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-5-ddr-derived-lightcurve-v14.0_g8yy-47a5",
-            "description": "This is a compilation of published rotational parameters derived from lightcurve data for asteroids, based on the Warner et al. (2009) Asteroid Lightcurve Database. This is the version as of March 1, 2014. In addition to reported rotational parameters by individual paper, there is a summary file with the values adopted by Harris, Warner, and Pravec as the most likely correct values for each asteroid. The data set also contains files listing known binary asteroids and 'tumbling' asteroids.",
-            "title": "ASTEROID LIGHTCURVE DERIVED DATA V14.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ASTEROID LIGHTCURVE DERIVED DATA V14.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-X-PEPSSI-2-PLUTOCRUISE-V2.0",
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
-                "new horizons"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This data set contains Raw data taken by the New Horizons                Pluto Energetic Particle Spectrometer Science Investigation            instrument during the                                                    pluto cruise                                                           mission phase.  This is VERSION 2.0 of this data set.                    Per the original mission plan for cruise operations, the PEPSSI            instrument was initially off for Pluto Cruise and only turned on           for functional tests and calibrations during Annual CheckOuts              (ACO); ACOs usually generate engineering data, but there is some           potential for science during those times. After extensive testing          in early 2012, in July of that year the project approved daily             science operations for the SWAP and PEPSSI instruments throughout          the rest of the cruise to Pluto.                                           The changes in Version 2.0 were re-running of the ancillary data         in the data product, updated geometry from newer SPICE kernels,          minor editing of the documentation, catalogs, etc., and resolution       of liens from the December, 2014 review, plus those from the May,        2016 review of the Pluto Encounter data sets.                            New observations added with this version (V2.0) include ongoing          cruise observations from August, 2014 through January, 2015.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-x-pepssi-2-plutocruise-v2.0_g95p-ny39",
+            "issued": "2018-09-05",
+            "keyword": [
+                "new horizons"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-X-PEPSSI-2-PLUTOCRUISE-V2.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-x-pepssi-2-plutocruise-v2.0_g95p-ny39",
-            "description": "This data set contains Raw data taken by the New Horizons                Pluto Energetic Particle Spectrometer Science Investigation            instrument during the                                                    pluto cruise                                                           mission phase.  This is VERSION 2.0 of this data set.                    Per the original mission plan for cruise operations, the PEPSSI            instrument was initially off for Pluto Cruise and only turned on           for functional tests and calibrations during Annual CheckOuts              (ACO); ACOs usually generate engineering data, but there is some           potential for science during those times. After extensive testing          in early 2012, in July of that year the project approved daily             science operations for the SWAP and PEPSSI instruments throughout          the rest of the cruise to Pluto.                                           The changes in Version 2.0 were re-running of the ancillary data         in the data product, updated geometry from newer SPICE kernels,          minor editing of the documentation, catalogs, etc., and resolution       of liens from the December, 2014 review, plus those from the May,        2016 review of the Pluto Encounter data sets.                            New observations added with this version (V2.0) include ongoing          cruise observations from August, 2014 through January, 2015.",
-            "title": "NEW HORIZONS                            \n      PEPSSI PLUTO CRUISE                                                     \n      RAW V2.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "NEW HORIZONS                            \n      PEPSSI PLUTO CRUISE                                                     \n      RAW V2.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-X-ALICE-2-LAUNCH-V1.0",
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
-                "calibration"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This data set contains Raw data taken by the New Horizons Alice UV Imager instrument during the post-launch checkout mission phase.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-x-alice-2-launch-v1.0_g9av-6yra",
+            "issued": "2021-05-21",
+            "keyword": [
+                "new horizons",
+                "calibration"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-X-ALICE-2-LAUNCH-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-x-alice-2-launch-v1.0_g9av-6yra",
-            "description": "This data set contains Raw data taken by the New Horizons Alice UV Imager instrument during the post-launch checkout mission phase.",
-            "title": "NEW HORIZONS ALICE POST-LAUNCH CHECKOUT V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "NEW HORIZONS ALICE POST-LAUNCH CHECKOUT V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=IHW-C-RSOC-3-EDR-HALLEY-V1.0",
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
+            "description": "NASA's International Halley Watch (IHW) has created a Comet Halley Archive. The collection of data spans the full wavelength range as submitted by scientists to the IHW. The observations belong to one of the following Disciplines: Amateur, Astrometry, Infrared Studies, Large-Scale Phenomena, Meteor Studies, Near-Nucleus Studies, Photometry and Polarimetry, Radio Studies, and Spectroscopy and Spectrophotometry. The data collected by these nine disciplines were augmented by Spacecraft measurements. The data were submitted to IHW, but the evaluation and selection for the Archive has been the primary responsibility of the Discipline Specialist Teams for each network in cooperation with the Lead Center. The data from the Radio Occultation Subnetwork contains 6 data files spanning dates 1985 November 23 through 1985 December 10.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ihw-c-rsoc-3-edr-halley-v1.0_g9du-f49p",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international halley watch",
+                "halley"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=IHW-C-RSOC-3-EDR-HALLEY-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ihw-c-rsoc-3-edr-halley-v1.0_g9du-f49p",
-            "description": "NASA's International Halley Watch (IHW) has created a Comet Halley Archive. The collection of data spans the full wavelength range as submitted by scientists to the IHW. The observations belong to one of the following Disciplines: Amateur, Astrometry, Infrared Studies, Large-Scale Phenomena, Meteor Studies, Near-Nucleus Studies, Photometry and Polarimetry, Radio Studies, and Spectroscopy and Spectrophotometry. The data collected by these nine disciplines were augmented by Spacecraft measurements. The data were submitted to IHW, but the evaluation and selection for the Archive has been the primary responsibility of the Discipline Specialist Teams for each network in cooperation with the Lead Center. The data from the Radio Occultation Subnetwork contains 6 data files spanning dates 1985 November 23 through 1985 December 10.",
-            "title": "IHW COMET HALLEY RADIO OCCULTATION GRIDDED DATA V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "IHW COMET HALLEY RADIO OCCULTATION GRIDDED DATA V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/T6IX3V0XGBAN",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Kopp, G.. 2020-12-07. SOR3TSI6. Version 019. SORCE Level 3 Total Solar Irradiance 6-Hour Means V019. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/T6IX3V0XGBAN. https://disc.gsfc.nasa.gov/datacollection/SOR3TSI6_019.html. Digital Science Data.",
-            "issued": "2020-12-02",
-            "temporal": "2003-02-25T00:00:00Z/2020-02-25T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-12-02",
-            "keyword": [
-                "earth science",
-                "sun-earth interactions",
-                "solar activity"
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
-            "identifier": "C1975355700-GES_DISC",
-            "description": "SOR3TSI6 Version 019 is the final version of this data product, and supersedes all previous versions.\n\nThe Total Solar Irradiance (TSI) data set SOR3TSI6 contains the total solar irradiance (a.k.a solar constant) data collected by the Total Irradiance Monitor (TIM) instrument covering the full wavelength spectrum averaged at 6-hour intervals. The data are normalized to one astronomical unit (1 AU).\n\nThe TIM instrument measures the Total Solar Irradiance (TSI), monitoring changes in incident sunlight to the Earth's atmosphere using an ambient temperature active cavity radiometer to a designed absolute accuracy of 100 parts per million (ppm, 1 ppm=0.0001% at 1-sigma) and a precision and long-term relative accuracy of 10 ppm per year. Due to the small size these data and to maximize ease of use to end-users, each delivered TSI product contains science results for the entire mission. Updates to Level 3 TSI data occur monthly in order to reduce repeated delivery of data.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "SOR3TSI6",
             "creator": "Kopp, G.",
-            "title": "SORCE Level 3 Total Solar Irradiance 6-Hour Means V019 (SOR3TSI6) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/SOR3TSI6_019.png",
-            "programCode": [
-                "026:001"
-            ],
+            "data-presentation-form": "Digital Science Data",
+            "description": "SOR3TSI6 Version 019 is the final version of this data product, and supersedes all previous versions.\n\nThe Total Solar Irradiance (TSI) data set SOR3TSI6 contains the total solar irradiance (a.k.a solar constant) data collected by the Total Irradiance Monitor (TIM) instrument covering the full wavelength spectrum averaged at 6-hour intervals. The data are normalized to one astronomical unit (1 AU).\n\nThe TIM instrument measures the Total Solar Irradiance (TSI), monitoring changes in incident sunlight to the Earth's atmosphere using an ambient temperature active cavity radiometer to a designed absolute accuracy of 100 parts per million (ppm, 1 ppm=0.0001% at 1-sigma) and a precision and long-term relative accuracy of 10 ppm per year. Due to the small size these data and to maximize ease of use to end-users, each delivered TSI product contains science results for the entire mission. Updates to Level 3 TSI data occur monthly in order to reduce repeated delivery of data.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FT6IX3V0XGBAN",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FT6IX3V0XGBAN",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
@@ -802702,82 +802680,106 @@
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/SOR3TSI6_019.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/SOR3TSI6_019.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/SORCE_Level3/SOR3TSI6.019/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/SORCE_Level3/SOR3TSI6.019/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=SOR3TSI6_019",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=SOR3TSI6_019",
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
-                    "downloadURL": "http://lasp.colorado.edu/home/sorce/data/tsi-data/tim-tsi-release-notes/",
-                    "description": "TIM Release Notes",
                     "@type": "dcat:Distribution",
+                    "description": "TIM Release Notes",
+                    "downloadURL": "http://lasp.colorado.edu/home/sorce/data/tsi-data/tim-tsi-release-notes/",
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
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/SOR3TSI6_019.png",
+            "identifier": "C1975355700-GES_DISC",
+            "issued": "2020-12-02",
+            "keyword": [
+                "earth science",
+                "sun-earth interactions",
+                "solar activity"
+            ],
+            "landingPage": "https://doi.org/10.5067/T6IX3V0XGBAN",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2020-12-02",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
+            },
+            "release-place": "Greenbelt, MD, USA",
+            "series-name": "SOR3TSI6",
+            "temporal": "2003-02-25T00:00:00Z/2020-02-25T23:59:59.999Z",
             "theme": [
                 "SORCE",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "SORCE Level 3 Total Solar Irradiance 6-Hour Means V019 (SOR3TSI6) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-4-ESC4-67P-M24-STRLIGHT-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This CODMAC level 4 data set contains solar stray light corrected, radiometric calibrated and geometric distortion corrected (resampled) image data in W/m^2/sr/nm, acquired by the OSIRIS Narrow Angle Camera on the Rosetta spacecraft during the COMET ESCORT 4 mission phase, covering the period from 2015-12-15T23:25:00.000 to 2016-01-12T23:24:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V1.0 is the first version of this dataset: Lien corrected dataset after October 2018 PSA/PDS external peer review.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-4-esc4-67p-m24-strlight-v1.0",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2021-05-21",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "67p/churyumov-gerasimenko 1 (1969 r1)",
                 "international rosetta mission",
@@ -802785,60 +802787,37 @@
                 "earth",
                 "vega"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-4-ESC4-67P-M24-STRLIGHT-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-4-esc4-67p-m24-strlight-v1.0",
-            "description": "This CODMAC level 4 data set contains solar stray light corrected, radiometric calibrated and geometric distortion corrected (resampled) image data in W/m^2/sr/nm, acquired by the OSIRIS Narrow Angle Camera on the Rosetta spacecraft during the COMET ESCORT 4 mission phase, covering the period from 2015-12-15T23:25:00.000 to 2016-01-12T23:24:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V1.0 is the first version of this dataset: Lien corrected dataset after October 2018 PSA/PDS external peer review.",
-            "title": "ROSETTA-ORBITER 67P OSINAC 4 ESC4-MTP024 RDR-STRLIGHT V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P OSINAC 4 ESC4-MTP024 RDR-STRLIGHT V1.0"
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
-                "ask the academy",
-                "knowledge",
-                "appel",
-                "sharing"
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
-            "identifier": "NASA-862__46",
             "description": "Academy of Program/Project & Engineering Leadership's Ask the Academy magazine past issues.",
-            "title": "Academy of Program/Project & Engineering Leadership ASK the Academy Past Issues",
-            "programCode": [
-                "026:045"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -802846,223 +802825,226 @@
                     "mediaType": "application/html"
                 }
             ],
-            "accrualPeriodicity": "R/P1M",
+            "identifier": "NASA-862__46",
+            "issued": "2018-06-25",
+            "keyword": [
+                "ask the academy",
+                "knowledge",
+                "appel",
+                "sharing"
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
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=ARCB-V-RTLS-4-12.6CM-V1.0",
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
-                "pre-magellan"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "The Arecibo 12.6 cm radar data set for Venus consists of scaled radar backscatter cross section images generated from data obtained in 1983 and 1988. The images are in raster format (one image per record, with no embedded labels). The original images are in 16-bit, unsigned integer, most-significant-byte-first format. Since the volume of the entire set of 16-bit images would have exceeded the capacity of the CD-ROM, some of the images have been scaled to 8-bit versions. Specifically, the entire set of 1988 images are in the scaled 8-bit format, while all the 1983 images are in the original 16-bit format. Both the 16-bit and the 8-bit images were provided by Don Campbell, Cornell University.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.arcb-v-rtls-4-12.6cm-v1.0_g9jb-993z",
+            "issued": "2018-06-26",
+            "keyword": [
+                "venus",
+                "pre-magellan"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=ARCB-V-RTLS-4-12.6CM-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.arcb-v-rtls-4-12.6cm-v1.0_g9jb-993z",
-            "description": "The Arecibo 12.6 cm radar data set for Venus consists of scaled radar backscatter cross section images generated from data obtained in 1983 and 1988. The images are in raster format (one image per record, with no embedded labels). The original images are in 16-bit, unsigned integer, most-significant-byte-first format. Since the volume of the entire set of 16-bit images would have exceeded the capacity of the CD-ROM, some of the images have been scaled to 8-bit versions. Specifically, the entire set of 1988 images are in the scaled 8-bit format, while all the 1983 images are in the original 16-bit format. Both the 16-bit and the 8-bit images were provided by Don Campbell, Cornell University.",
-            "title": "ARECIBO VENUS RADIO TELESCOPE RESAMPLED 12.6 CM RADAR V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "ARECIBO VENUS RADIO TELESCOPE RESAMPLED 12.6 CM RADAR V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG1-J-LECP-4-BR-15MIN",
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
+            "description": "THIS BROWSE DATA CONSISTS OF RESAMPLED DATA FROM THE LOW ENERGY CHARGED PARTICLE (LECP) EXPERIMENT ON VOYAGER 1 WHILE THE SPACECRAFT WAS IN THE VICINITY OF JUPITER. THIS INSTRUMENT MEASURES THE INTENSITIES OF IN-SITU CHARGED PARTICLES (>26 KEV ELECTRONS AND >30 KEV IONS) WITH VARIOUS LEVELS OF DISCRIMINATION BASED ON ENERGY, MASS SPECIES, AND ANGULAR ARRIVAL DIRECTION. A SUBSET OF ALMOST 100 LECP CHANNELS ARE INCLUDED WITH THIS DATA SET. THE LECP DATA ARE GLOBALLY CALIBRATED TO THE EXTENT POSSIBLE (SEE BELOW) AND THEY ARE TIME AVERAGED TO ABOUT 15 MINUTE TIME INTERVALS WITH THE EXACT BEGINNING AND ENDING TIMES FOR THOSE INTERVALS MATCHING THE LECP INSTRUMENTAL CYCLE PERIODS (THE ANGULAR SCANNING PERIODS). THE LECP INSTUMENT HAS A ROTATING HEAD FOR OBTAINING ANGULAR ANISOTROPY MEASUREMENTS OF THE MEDIUM ENERGY CHARGED PARTICLES THAT IT MEASURES. THE CYCLE TIME FOR THE ROTATION IF VARIABLE, BUT DURING ENCOUNTERS IT IS ALWAYS FASTER THAN 15 MINUTES. FOR THIS BROWSE DATA SET ONLY SCAN AVERAGE DATA IS GIVEN (NO ANGULAR INFORMATION). THE DATA IS IN THE FORM OF 'RATE' DATA WHICH HAS NOT BEEN CONVERTED TO THE USUAL PHYSICAL UNITS. THE REASON IS THAT SUCH A CONVERSION WOULD DEPEND ON UNCERTAIN DETERMINATIONS SUCH AS THE MASS SPECIES OF THE PARTICLES AND THE LEVEL OF BACKGROUND. BOTH MASS SPECIES AND BACKGROUND ARE GENERALLY DETERMINED FROM CONTEXT DURING THE STUDY OF PARTICULAR REGIONS. TO CONVERT 'RATE' TO 'INTENSITY' FOR A PARTICULAR CHANNEL ONE PERFORMS THE FOLLOWING TASKS: 1) DECIDE ON THE LEVEL OF BACKGROUND CONTAMINATION AND SUBTRACT THAT OFF THE GIVEN RATE LEVEL. BACKGROUND IS TO BE DETERMINED FROM CONTEXT AND FROM MAKING USE OF SECTOR 8 RATES (SECTOR 8 HAS A 2 mm AL SHIELD COVERING IT). 2) DIVIDE THE BACKGROUND CORRECTED RATE BY THE CHANNEL GEOMETRIC FACTOR AND BY THE ENERGY BANDPASS OF THE CHANNEL. THE GEOMETRIC FACTOR IS FOUND IN ENTRY 'channel_geometric_ factor' AS ASSOCIATED WITH EACH CHANNEL 'channel_id'. TO DETERMINE THE ENERGY BANDPASS, ONE MUST JUDGE THE MASS SPECIES OF THE OF THE DETECTED PARTICLES (FOR IONS BUT NOT FOR ELECTRONS). THE ENERGY BAND PASSES ARE GIVEN IN ENTRIES 'minimum_instrument_parameter' and 'maximum_instrument_ parameter' IN TABLE 'FPLECPENERGY', AND ARE GIVEN IN THE FORM 'ENERGY/NUCLEON'. FOR CHANNELS THAT BEGIN THEIR NAMES WITH THE DESIGNATIONS 'CH' THESE BANDPASSES CAN BE USED ON MASS SPECIES THAT ARE ACCEPTED INTO THAT CHANNEL (SEE ENTRIES 'minimum_instrument_parameter' and 'maximum_instrument_ parameter' IN TABLE 'FPLECPCHANZ', WHICH GIVE THE MINIMUM AND MAXIMUM 'Z' VALUE ACCEPTED -- THESE ENTRIES ARE BLANK FOR ELECTRON CHANNELS). FOR OTHER CHANNELS THE GIVEN BANDPASS REFERS ONLY TO THE LOWEST 'Z' VALUE ACCEPTED. THE BANDPASSES FOR OTHER 'Z' VALUES ARE NOT ALL KNOWN, BUT SOME ARE GIVEN IN THE LITERATURE (E.G. KRIMIGIS ET AL., 1979). THE FINAL PRODUCT OF THESE INSTRUCTIONS WILL BE THE PARTICLE INTENSITY WITH THE UNITS: COUNTS/(CM**2.STR.SEC.KEV). SOME CHANNELS ARE SUBJECT TO SERIOUS CONTAMINATIONS, AND MANY OF THESE CONTAMINATIONS CANNOT BE REMOVED EXCEPT WITH A REGION-BY-REGION ANALYSIS, WHICH HAS NOT BEEN DONE FOR THIS DATA. THUS, TO USE THIS DATA IT IS ABSOLUTELY VITAL THAT THE CONTAMINATION TYPES ('contamination_id' , 'contamination_desc') AND THE LEVELS OF CONTAMINATION ('data_quality_id' CORRESPONDING TO THE DEFINITIONS 'data_quality_desc') BE CAREFULLY EXAMINED FOR ALL REGIONS OF STUDY. A DEAD TIME CORRECTION PROCEDURE HAS BEEN APPLIED IN AN ATTEMPT TO CORRECT THE LINEAR EFFECTS OF DETECTOR OVERDRIVE (PULSE-PILEUP). THIS PROCEDURE DOES NOT FIX SEVERELY OVERDRIVEN DETECTORS. A PROCEDURE IS AVAILABLE FOR CORRECTING VOYAGER 2 LECP ELECTRON CONTAMINATION OF LOW ENERGY ION CHANNELS, BUT ITS EFFECTIVENESS HAS BEEN EVALUATED ONLY FOR THE URANUS DATA SET. THUS, CORRECTIONS HAVE BEEN APPLIED ONLY TO THE URANUS DATA SET.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg1-j-lecp-4-br-15min_g9kw-wsxf",
+            "issued": "2021-05-21",
+            "keyword": [
+                "jupiter",
+                "voyager"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG1-J-LECP-4-BR-15MIN",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg1-j-lecp-4-br-15min_g9kw-wsxf",
-            "description": "THIS BROWSE DATA CONSISTS OF RESAMPLED DATA FROM THE LOW ENERGY CHARGED PARTICLE (LECP) EXPERIMENT ON VOYAGER 1 WHILE THE SPACECRAFT WAS IN THE VICINITY OF JUPITER. THIS INSTRUMENT MEASURES THE INTENSITIES OF IN-SITU CHARGED PARTICLES (>26 KEV ELECTRONS AND >30 KEV IONS) WITH VARIOUS LEVELS OF DISCRIMINATION BASED ON ENERGY, MASS SPECIES, AND ANGULAR ARRIVAL DIRECTION. A SUBSET OF ALMOST 100 LECP CHANNELS ARE INCLUDED WITH THIS DATA SET. THE LECP DATA ARE GLOBALLY CALIBRATED TO THE EXTENT POSSIBLE (SEE BELOW) AND THEY ARE TIME AVERAGED TO ABOUT 15 MINUTE TIME INTERVALS WITH THE EXACT BEGINNING AND ENDING TIMES FOR THOSE INTERVALS MATCHING THE LECP INSTRUMENTAL CYCLE PERIODS (THE ANGULAR SCANNING PERIODS). THE LECP INSTUMENT HAS A ROTATING HEAD FOR OBTAINING ANGULAR ANISOTROPY MEASUREMENTS OF THE MEDIUM ENERGY CHARGED PARTICLES THAT IT MEASURES. THE CYCLE TIME FOR THE ROTATION IF VARIABLE, BUT DURING ENCOUNTERS IT IS ALWAYS FASTER THAN 15 MINUTES. FOR THIS BROWSE DATA SET ONLY SCAN AVERAGE DATA IS GIVEN (NO ANGULAR INFORMATION). THE DATA IS IN THE FORM OF 'RATE' DATA WHICH HAS NOT BEEN CONVERTED TO THE USUAL PHYSICAL UNITS. THE REASON IS THAT SUCH A CONVERSION WOULD DEPEND ON UNCERTAIN DETERMINATIONS SUCH AS THE MASS SPECIES OF THE PARTICLES AND THE LEVEL OF BACKGROUND. BOTH MASS SPECIES AND BACKGROUND ARE GENERALLY DETERMINED FROM CONTEXT DURING THE STUDY OF PARTICULAR REGIONS. TO CONVERT 'RATE' TO 'INTENSITY' FOR A PARTICULAR CHANNEL ONE PERFORMS THE FOLLOWING TASKS: 1) DECIDE ON THE LEVEL OF BACKGROUND CONTAMINATION AND SUBTRACT THAT OFF THE GIVEN RATE LEVEL. BACKGROUND IS TO BE DETERMINED FROM CONTEXT AND FROM MAKING USE OF SECTOR 8 RATES (SECTOR 8 HAS A 2 mm AL SHIELD COVERING IT). 2) DIVIDE THE BACKGROUND CORRECTED RATE BY THE CHANNEL GEOMETRIC FACTOR AND BY THE ENERGY BANDPASS OF THE CHANNEL. THE GEOMETRIC FACTOR IS FOUND IN ENTRY 'channel_geometric_ factor' AS ASSOCIATED WITH EACH CHANNEL 'channel_id'. TO DETERMINE THE ENERGY BANDPASS, ONE MUST JUDGE THE MASS SPECIES OF THE OF THE DETECTED PARTICLES (FOR IONS BUT NOT FOR ELECTRONS). THE ENERGY BAND PASSES ARE GIVEN IN ENTRIES 'minimum_instrument_parameter' and 'maximum_instrument_ parameter' IN TABLE 'FPLECPENERGY', AND ARE GIVEN IN THE FORM 'ENERGY/NUCLEON'. FOR CHANNELS THAT BEGIN THEIR NAMES WITH THE DESIGNATIONS 'CH' THESE BANDPASSES CAN BE USED ON MASS SPECIES THAT ARE ACCEPTED INTO THAT CHANNEL (SEE ENTRIES 'minimum_instrument_parameter' and 'maximum_instrument_ parameter' IN TABLE 'FPLECPCHANZ', WHICH GIVE THE MINIMUM AND MAXIMUM 'Z' VALUE ACCEPTED -- THESE ENTRIES ARE BLANK FOR ELECTRON CHANNELS). FOR OTHER CHANNELS THE GIVEN BANDPASS REFERS ONLY TO THE LOWEST 'Z' VALUE ACCEPTED. THE BANDPASSES FOR OTHER 'Z' VALUES ARE NOT ALL KNOWN, BUT SOME ARE GIVEN IN THE LITERATURE (E.G. KRIMIGIS ET AL., 1979). THE FINAL PRODUCT OF THESE INSTRUCTIONS WILL BE THE PARTICLE INTENSITY WITH THE UNITS: COUNTS/(CM**2.STR.SEC.KEV). SOME CHANNELS ARE SUBJECT TO SERIOUS CONTAMINATIONS, AND MANY OF THESE CONTAMINATIONS CANNOT BE REMOVED EXCEPT WITH A REGION-BY-REGION ANALYSIS, WHICH HAS NOT BEEN DONE FOR THIS DATA. THUS, TO USE THIS DATA IT IS ABSOLUTELY VITAL THAT THE CONTAMINATION TYPES ('contamination_id' , 'contamination_desc') AND THE LEVELS OF CONTAMINATION ('data_quality_id' CORRESPONDING TO THE DEFINITIONS 'data_quality_desc') BE CAREFULLY EXAMINED FOR ALL REGIONS OF STUDY. A DEAD TIME CORRECTION PROCEDURE HAS BEEN APPLIED IN AN ATTEMPT TO CORRECT THE LINEAR EFFECTS OF DETECTOR OVERDRIVE (PULSE-PILEUP). THIS PROCEDURE DOES NOT FIX SEVERELY OVERDRIVEN DETECTORS. A PROCEDURE IS AVAILABLE FOR CORRECTING VOYAGER 2 LECP ELECTRON CONTAMINATION OF LOW ENERGY ION CHANNELS, BUT ITS EFFECTIVENESS HAS BEEN EVALUATED ONLY FOR THE URANUS DATA SET. THUS, CORRECTIONS HAVE BEEN APPLIED ONLY TO THE URANUS DATA SET.",
-            "title": "VOYAGER 1 JUP LOW ENERGY CHARGED PARTICLE CALIB. BR 15MIN",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "VOYAGER 1 JUP LOW ENERGY CHARGED PARTICLE CALIB. BR 15MIN"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/GNSS/GNSS_HIGHRATE_Q_001",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "International GNSS Service, High-rate QZSS broadcast ephemeris data, Greenbelt, MD, USA:NASA Crustal Dynamics Data Information System (CDDIS), Accessed [[enter user data access date]] at doi:10.5067/GNSS/gnss_highrate_q_001",
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
-            "identifier": "C1422105790-CDDIS",
             "description": "This dataset consists of ground-based Global Navigation Satellite System (GNSS)  Quasi-Zenith Satellite System (QZSS) Broadcast Ephemeris Data (sub-hourly files) from the NASA Crustal Dynamics Data Information System (CDDIS). GNSS provide autonomous geo-spatial positioning with global coverage. GNSS data sets from ground receivers at the CDDIS consist primarily of the data from the U.S. Global Positioning System (GPS) and the Russian GLONASS. Since 2011, the CDDIS GNSS archive includes data from other GNSS (Europe\u2019s Galileo, China\u2019s Beidou, Japan\u2019s Quasi-Zenith Satellite System/QZSS, the Indian Regional Navigation Satellite System/IRNSS, and worldwide Satellite Based Augmentation Systems/SBASs), which are similar to the U.S. GPS in terms of the satellite constellation, orbits, and signal structure. The sub-hourly QZSS broadcast ephemeris files contain 15 minutes of QZSS broadcast navigation data in RINEX format from a global permanent network of ground-based receivers, one file per 15 minutes per site. More information about these data is available on the CDDIS website at https://cddis.nasa.gov/Data_and_Derived_Products/GNSS/high-rate_data.html.",
-            "title": "Ground-Based Global Navigation Satellite System (GNSS) QZSS Broadcast Ephemeris Data (sub-hourly files) from NASA CDDIS",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGNSS%2FGNSS_HIGHRATE_Q_001",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGNSS%2FGNSS_HIGHRATE_Q_001",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://cddis.nasa.gov/archive/gnss/data/highrate",
-                    "description": "URL for retrieval of GNSS sub-hourly data through https",
                     "@type": "dcat:Distribution",
+                    "description": "URL for retrieval of GNSS sub-hourly data through https",
+                    "downloadURL": "https://cddis.nasa.gov/archive/gnss/data/highrate",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://cddis.nasa.gov/Data_and_Derived_Products/GNSS/broadcast_ephemeris_data.html",
-                    "description": "URL for more information about GNSS sub-hourly QZSS broadcast navigation data",
                     "@type": "dcat:Distribution",
+                    "description": "URL for more information about GNSS sub-hourly QZSS broadcast navigation data",
+                    "downloadURL": "https://cddis.nasa.gov/Data_and_Derived_Products/GNSS/broadcast_ephemeris_data.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/GNSS/GNSS_HIGHRATE_Q_001",
-                    "description": "URL for more information about GNSS sub-hourly QZSS broadcast navigation data",
                     "@type": "dcat:Distribution",
+                    "description": "URL for more information about GNSS sub-hourly QZSS broadcast navigation data",
+                    "downloadURL": "https://doi.org/10.5067/GNSS/GNSS_HIGHRATE_Q_001",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 }
             ],
+            "identifier": "C1422105790-CDDIS",
+            "issued": "1992-01-01",
+            "keyword": [
+                "earth science",
+                "solid earth",
+                "geodetics",
+                "gravity/gravitational field",
+                "tectonics"
+            ],
+            "landingPage": "https://doi.org/10.5067/GNSS/GNSS_HIGHRATE_Q_001",
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
+            "title": "Ground-Based Global Navigation Satellite System (GNSS) QZSS Broadcast Ephemeris Data (sub-hourly files) from NASA CDDIS"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=FEXP-E-HSTP-4-RDR-TOPOGRAPHIC-PROF-V1.0",
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
-                "geologic remote sensing field experiment"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "Selected sites, including those areas chosen for calibration and modeling purposes, were photographed via helicopter-borne 70 mm stereophotography using the JPL Hasselblad system. The cameras were flown in August 1990. The images were made with color film (Kodak Aerochrome 2448 color reversal film). Some of the data have been reduced to vertical profiles and arrays at a spacing and accuracy required to meet topography requirements. These data cover approximately 10x20 meter square areas. For GRSFE archive Release V1.0, three profiles are located over or close to the mantled lava flow modeling site and one is located over the playa modeling site.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.fexp-e-hstp-4-rdr-topographic-prof-v1.0_g9rz-u29x",
+            "issued": "2018-06-26",
+            "keyword": [
+                "earth",
+                "geologic remote sensing field experiment"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=FEXP-E-HSTP-4-RDR-TOPOGRAPHIC-PROF-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.fexp-e-hstp-4-rdr-topographic-prof-v1.0_g9rz-u29x",
-            "description": "Selected sites, including those areas chosen for calibration and modeling purposes, were photographed via helicopter-borne 70 mm stereophotography using the JPL Hasselblad system. The cameras were flown in August 1990. The images were made with color film (Kodak Aerochrome 2448 color reversal film). Some of the data have been reduced to vertical profiles and arrays at a spacing and accuracy required to meet topography requirements. These data cover approximately 10x20 meter square areas. For GRSFE archive Release V1.0, three profiles are located over or close to the mantled lava flow modeling site and one is located over the playa modeling site.",
-            "title": "FIELD EXP E HSTP RESAMPLED RDR TOPOGRAPHIC PROFILES V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "FIELD EXP E HSTP RESAMPLED RDR TOPOGRAPHIC PROFILES V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.nasa.gov/d/g9su-ssad",
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
-            "identifier": "NASA-0000037__18",
+            "describedBy": "http://www.lpi.usra.edu/resources/gc/gcreadme.html",
             "description": "Planetary nomenclature, like terrestrial nomenclature, is used to uniquely identify a feature on the surface of a planet or satellite so that the feature can be easily located, described, and discussed. This gazetteer contains detailed information about all names of topographic and albedo features on planets and satellites (and some planetary ring and ring-gap systems) that the International Astronomical Union (IAU) has named and approved from its founding in 1919 through the present time.",
-            "title": "Gateway to Astronaut Photography of Earth",
-            "programCode": [
-                "026:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -803070,282 +803052,314 @@
                     "mediaType": "text/html"
                 }
             ],
-            "describedBy": "http://www.lpi.usra.edu/resources/gc/gcreadme.html",
-            "accrualPeriodicity": "irregular"
+            "identifier": "NASA-0000037__18",
+            "issued": "2018-06-25",
+            "keyword": [
+                "nen",
+                "wise",
+                "space science",
+                "geography"
+            ],
+            "landingPage": "https://data.nasa.gov/d/g9su-ssad",
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
-            "landingPage": "https://doi.org/10.5067/AQR50-3RUDS",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "NASA Aquarius project. 2017-12-07. Aquarius Official Release Level 3 Ancillary Reynolds Sea Surface Temperature Standard Mapped Image Descending Monthly Climatology Data. Version 5.0. Aquarius Sea Surface Salinity Products. Goddard Space Flight Center, 8800 Greenbelt Rd.; Greeenbelt, MD., 20771, USA. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/GSFC OBPG. https://doi.org/10.5067/AQR50-3RUDS. http://podaac.jpl.nasa.gov/SeaSurfaceSalinity/Aquarius. NASA Aquarius project, NASA/GSFC OBPG, 2017-12-07, Aquarius Official Release Level 3 Ancillary Reynolds Sea Surface Temperature Standard Mapped Image Descending Monthly Climatology Data V5.0, http://podaac.jpl.nasa.gov/SeaSurfaceSalinity/Aquarius.",
-            "issued": "2017-10-21",
-            "temporal": "2011-08-25T02:41:02Z/2015-06-07T12:45:21Z",
-            "@type": "dcat:Dataset",
-            "modified": "2017-12-07",
-            "keyword": [
-                "ocean temperature",
-                "earth science",
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
-            "identifier": "C2491755726-POCLOUD",
-            "description": "Aquarius Level 3 ancillary sea surface temperature (SST) standard mapped image data are the ancillary SST data used in the Aquarius calibration for salinity retrieval.  They are simply the daily SSTs from the Reynolds National Climatic Data Center (NCDC) 0.25 degree dataset, gridded and averaged using the Aquarius processing L2-L3 processing scheme to the same 1 degree spatial resolution and daily, 7 day, monthly, seasonal, and annual time intervals as Aquarius L3 standard salinity and wind speed products.  This particular data set is the monthly climatology, descending ancillary sea surface temperature product associated with version 5.0  of the Aquarius data set, which is the official end of mission public data release from the AQUARIUS/SAC-D mission.",
-            "release-place": "Goddard Space Flight Center, 8800 Greenbelt Rd.; Greeenbelt, MD., 20771, USA",
-            "series-name": "Aquarius Official Release Level 3 Ancillary Reynolds Sea Surface Temperature Standard Mapped Image Descending Monthly Climatology Data",
-            "graphic-preview-description": "Thumbnail",
             "creator": "NASA Aquarius project",
-            "title": "Aquarius Official Release Level 3 Ancillary Reynolds Sea Surface Temperature Standard Mapped Image Descending Monthly Climatology Data V5.0",
-            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/AQUARIUS_L3_ANCILLARY_SST_SMID_MONTHLY-CLIMATOLOGY_V5.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "Aquarius Level 3 ancillary sea surface temperature (SST) standard mapped image data are the ancillary SST data used in the Aquarius calibration for salinity retrieval.  They are simply the daily SSTs from the Reynolds National Climatic Data Center (NCDC) 0.25 degree dataset, gridded and averaged using the Aquarius processing L2-L3 processing scheme to the same 1 degree spatial resolution and daily, 7 day, monthly, seasonal, and annual time intervals as Aquarius L3 standard salinity and wind speed products.  This particular data set is the monthly climatology, descending ancillary sea surface temperature product associated with version 5.0  of the Aquarius data set, which is the official end of mission public data release from the AQUARIUS/SAC-D mission.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAQR50-3RUDS",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAQR50-3RUDS",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
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
-                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/AQUARIUS_L3_ANCILLARY_SST_SMID_MONTHLY-CLIMATOLOGY_V5.jpg",
-                    "description": "Thumbnail",
                     "@type": "dcat:Distribution",
+                    "description": "Thumbnail",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/AQUARIUS_L3_ANCILLARY_SST_SMID_MONTHLY-CLIMATOLOGY_V5.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
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
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2491755726-POCLOUD",
-                    "description": "HTTPS endpoint for data browse and download",
                     "@type": "dcat:Distribution",
+                    "description": "HTTPS endpoint for data browse and download",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2491755726-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2491755726-POCLOUD",
-                    "description": "Browse granule search results in Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse granule search results in Earthdata Search",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2491755726-POCLOUD",
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
+            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/AQUARIUS_L3_ANCILLARY_SST_SMID_MONTHLY-CLIMATOLOGY_V5.jpg",
+            "identifier": "C2491755726-POCLOUD",
+            "issued": "2017-10-21",
+            "keyword": [
+                "ocean temperature",
+                "earth science",
+                "oceans"
+            ],
+            "landingPage": "https://doi.org/10.5067/AQR50-3RUDS",
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
+            "series-name": "Aquarius Official Release Level 3 Ancillary Reynolds Sea Surface Temperature Standard Mapped Image Descending Monthly Climatology Data",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2011-08-25T02:41:02Z/2015-06-07T12:45:21Z",
             "theme": [
                 "AQUARIUS SAC-D",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Aquarius Official Release Level 3 Ancillary Reynolds Sea Surface Temperature Standard Mapped Image Descending Monthly Climatology Data V5.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.nasa.gov/d/g9vv-5wxj",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "GeneLab Outreach",
+                "hasEmail": "mailto:genelab-outreach@lists.nasa.gov"
+            },
+            "description": "The environmental microbiome study was designed to decipher microbial diversity of the International Space Station surfaces in terms of spatial and temporal distributions using 16S and ITS iTag Illumina sequencing. We hypothesized that the microbial population of environmental surfaces changes in time due to astronauts xe2 x80 x99 activity and might be location specific. The environmental samples were collected with the polyester wipes from eight different locations in the ISS during two consecutive sampling sessions (three months apart). The specific objective was to unveil the viable microbial diversity of each location during two separate sessions in terms of abundance and richness of the communities. The International Space Station (ISS) as a closed built environment has its own environmental microbiome which is shaped by microgravity radiation and limited human presence. The microbial diversity associated with ISS environmental surfaces was investigated during this study. Polyester wipes and contact slides were used for sampling of eight various surface locations on the ISS at different time periods. The samples were retrieved and analyzed immediately upon the return to the Earth (via Soyuz TMA-14M or Dragon capsule from SpaceX). After surface sample collection contact slides containing nutrient media for the growth of bacteria and fungi were incubated at 25 xcb x9aC. The polyester wipes were processed to measure microbial burden (R2A Blood Agar and Potato Dextrose Agar) and recover cultivable bacteria as well as fungi. Subsequently viable microbial burden was assessed using Adenosine Triphosphate (ATP) assay and quantitative polymerase chain reaction (PCR) methods after propidium monoazide (PMA) treatment. The 16S-tag and metagenome analyses were used to elucidate viable microbial diversity. The cultivable bacterial population yield from the polyester wipes was very high (5 to 7-logs) when compared with the contact slides (102 to 103 CFU/m2). The PMA-qPCR analysis showed considerable variation of viable bacterial population (105 to 109 16S rDNA gene copies/m2) among locations sampled. Unlike contact slides polyester wipes cover much larger sample surface (~1 m2) and produce much more reliable results of the microbial diversity of the ISS covering both cultivable and non-cultivable species. The cultivable total and viable microbial diversity was determined utilizing state-of-the art molecular techniques. The implementation of the PMA assay before DNA extraction allowed distinguishing viable microorganisms which is crucial for determining their role to the crew health the ISS maintenance and the general knowledge of the closed environmentally controlled built systems.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "GeneLab Study Page",
+                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-65",
+                    "mediaType": "text/html",
+                    "title": "Microbial Observatory (ISS-MO): Microbial diversity"
+                }
+            ],
+            "identifier": "nasa_genelab_GLDS-65_g9vv-5wxj",
             "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
             "keyword": [
                 "sequence analysis data transformation",
                 "spaceflight",
@@ -803354,251 +803368,211 @@
                 "nucleic acid extraction",
                 "sample collection"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "GeneLab Outreach",
-                "hasEmail": "mailto:genelab-outreach@lists.nasa.gov"
-            },
+            "landingPage": "https://data.nasa.gov/d/g9vv-5wxj",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "nasa_genelab_GLDS-65_g9vv-5wxj",
-            "description": "The environmental microbiome study was designed to decipher microbial diversity of the International Space Station surfaces in terms of spatial and temporal distributions using 16S and ITS iTag Illumina sequencing. We hypothesized that the microbial population of environmental surfaces changes in time due to astronauts xe2 x80 x99 activity and might be location specific. The environmental samples were collected with the polyester wipes from eight different locations in the ISS during two consecutive sampling sessions (three months apart). The specific objective was to unveil the viable microbial diversity of each location during two separate sessions in terms of abundance and richness of the communities. The International Space Station (ISS) as a closed built environment has its own environmental microbiome which is shaped by microgravity radiation and limited human presence. The microbial diversity associated with ISS environmental surfaces was investigated during this study. Polyester wipes and contact slides were used for sampling of eight various surface locations on the ISS at different time periods. The samples were retrieved and analyzed immediately upon the return to the Earth (via Soyuz TMA-14M or Dragon capsule from SpaceX). After surface sample collection contact slides containing nutrient media for the growth of bacteria and fungi were incubated at 25 xcb x9aC. The polyester wipes were processed to measure microbial burden (R2A Blood Agar and Potato Dextrose Agar) and recover cultivable bacteria as well as fungi. Subsequently viable microbial burden was assessed using Adenosine Triphosphate (ATP) assay and quantitative polymerase chain reaction (PCR) methods after propidium monoazide (PMA) treatment. The 16S-tag and metagenome analyses were used to elucidate viable microbial diversity. The cultivable bacterial population yield from the polyester wipes was very high (5 to 7-logs) when compared with the contact slides (102 to 103 CFU/m2). The PMA-qPCR analysis showed considerable variation of viable bacterial population (105 to 109 16S rDNA gene copies/m2) among locations sampled. Unlike contact slides polyester wipes cover much larger sample surface (~1 m2) and produce much more reliable results of the microbial diversity of the ISS covering both cultivable and non-cultivable species. The cultivable total and viable microbial diversity was determined utilizing state-of-the art molecular techniques. The implementation of the PMA assay before DNA extraction allowed distinguishing viable microorganisms which is crucial for determining their role to the crew health the ISS maintenance and the general knowledge of the closed environmentally controlled built systems.",
-            "title": "Microbial Observatory (ISS-MO): Microbial diversity",
-            "programCode": [
-                "026:005"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-65",
-                    "description": "GeneLab Study Page",
-                    "@type": "dcat:Distribution",
-                    "title": "Microbial Observatory (ISS-MO): Microbial diversity"
-                }
-            ],
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "Microbial Observatory (ISS-MO): Microbial diversity"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/90SYW7APOXKX",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "High Mountain Asia 4-km Dynamically Downscaled Meteorological Data, 2000-2015 V001. Version 1. Archived by National Aeronautics and Space Administration, U.S. Government, NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/90SYW7APOXKX.",
-            "issued": "2000-01-01",
-            "temporal": "2000-01-01T00:00:00Z/2016-01-01T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2016-01-01",
-            "keyword": [
-                "atmosphere",
-                "atmospheric temperature",
-                "earth science",
-                "precipitation"
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
-            "identifier": "C3114262920-NSIDC_ECS",
             "description": "This High Mountain Asia (HMA) data set contains simulated meteorological data for the Indus Basin from 2000 through 2015, at three horizontal resolutions \u2013 36 km, 12 km, and 4 km \u2013 and 9 pressure levels spanning 1000 hPa \u2013 200 hPa. The data were produced by using the Advanced Research Weather Research & Forecasting (ARW-WRF) model to dynamically downscale Climate Forecast System Reanalysis (CFSR) data into three nested domains with increasing horizontal resolution.",
-            "title": "High Mountain Asia 4-km Dynamically Downscaled Meteorological Data, 2000-2015 V001",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2F90SYW7APOXKX",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2F90SYW7APOXKX",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/HMA/HMA2_DDSMET.001/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/HMA/HMA2_DDSMET.001/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/data/data-access-tool/HMA2_DDSMET/versions/1/",
-                    "description": "Search and filter data files using a map-based interface",
                     "@type": "dcat:Distribution",
+                    "description": "Search and filter data files using a map-based interface",
+                    "downloadURL": "https://nsidc.org/data/data-access-tool/HMA2_DDSMET/versions/1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=HMA2_DDSMET+V001",
-                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=HMA2_DDSMET+V001",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/90SYW7APOXKX",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/90SYW7APOXKX",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/90SYW7APOXKX",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/90SYW7APOXKX",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C3114262920-NSIDC_ECS",
+            "issued": "2000-01-01",
+            "keyword": [
+                "atmosphere",
+                "atmospheric temperature",
+                "earth science",
+                "precipitation"
+            ],
+            "landingPage": "https://doi.org/10.5067/90SYW7APOXKX",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2016-01-01",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA NSIDC DAAC"
+            },
             "spatial": "43.179 10.34 108.829 45.569",
+            "temporal": "2000-01-01T00:00:00Z/2016-01-01T23:59:59.999Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "High Mountain Asia 4-km Dynamically Downscaled Meteorological Data, 2000-2015 V001"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-3-PRL-67PCHURYUMOV-M07B-V1.0",
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
+            "description": "This data set contains calibrated images acquired by the OSIRIS Narrow Angle\nCamera during the prelanding phase of the Rosetta mission at the comet 67P,\ncovering the period from 2014-09-16 to 2014-09-23.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-3-prl-67pchuryumov-m07b-v1.0_ga3v-f4zw",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-3-PRL-67PCHURYUMOV-M07B-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-3-prl-67pchuryumov-m07b-v1.0_ga3v-f4zw",
-            "description": "This data set contains calibrated images acquired by the OSIRIS Narrow Angle\nCamera during the prelanding phase of the Rosetta mission at the comet 67P,\ncovering the period from 2014-09-16 to 2014-09-23.",
-            "title": "ROSETTA-ORBITER COMET PRELANDING OSINAC 3 RDR MTP 007B V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER COMET PRELANDING OSINAC 3 RDR MTP 007B V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/GPM/AMSUB/NOAA16/GPROFCLIM/2A/07",
             "citation": "GPM Science Team. 2022-05-09. GPM_2AGPROFNOAA16AMSUB. GPM AMSU-B on NOAA16 (GPROF) Climate-based Radiometer Precipitation Profiling L2 1.5 hours 16 km V07. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/GPM/AMSUB/NOAA16/GPROFCLIM/2A/07. https://disc.gsfc.nasa.gov/datacollection/GPM_2AGPROFNOAA16AMSUB_CLIM_07.html. Digital Science Data.",
-            "issued": "2022-05-09",
-            "temporal": "2000-10-04T00:00:00Z/2010-05-01T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-05-01",
-            "keyword": [
-                "precipitation",
-                "microwave",
-                "atmospheric water vapor",
-                "spectral/engineering",
-                "earth science",
-                "atmosphere"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "GEORGE HUFFMAN",
                 "hasEmail": "mailto:George.J.Huffman@nasa.gov"
             },
+            "creator": "GPM Science Team",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C2264134296-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "Version 07 is the current version of the data set. Older versions will no longer be available and have been superseded by Version 07.\n\n\nThe 'CLIM'  products differ from their 'regular' counterparts (without the 'CLIM' in the name) by the ancillary data they use. They are Climate-Reference products, which requires homogeneous ancillary data over the climate time series.  Hence, the ECMWF-Interim (European Centre for Medium-Range Weather Forecasts, 2-3 months lag behind the regular production) reanalysis is used as ancillary data to derive surface and atmospheric conditions required by the GPROF algorithm for the 'CLIM' output. The GPROF databases are also adjusted accordingly for these climate-referenced retrievals.\n\n\nThe 2AGPROF (Goddard Profiling) algorithm retrieves consistent precipitation and related science fields from the following GMI and partner passive microwave sensors:\n+ TMI (TRMM)\n+ GMI, (GPM)\n+ SSMI (DMSP F11, F13, F14, F15); SSMIS (DMSP F16, F17, F18, F19)\n+ AMSR2 (GCOM-W1)\n+ MHS (NOAA 18,19)\n+ MHS (METOP A,B)\n+ ATMS (NPP)\n+ SAPHIR (MT1)\n\nThis provides the bulk of the 3-hour coverage achieved by GPM. For each sensor, there are nearrealtime (NRT) products, standard products, and climate products. These differ only in the amount of data that are available within 3 hours, 48 hours, and 3 months of collection, as well as the ancillary data used. The NRT product uses GANAL forecast fields. Standard products use the GANAL analysis product, while the climate product uses ECMWF reanalysis in order to allow for consistent data records with earlier missions. These earlier data may be archived separately. The main strength of the product is the large sampling provided.\n\nThe GPM radiometer algorithms are Bayesian-type algorithms. These algorithms search an apriori database of potential rain profiles and retrieve a weighted average of these entries based upon the proximity of the observed brightness temperature (Tb) to the simulated Tb corresponding to each rain profile. By using the same a-priori database of rain profiles, with appropriate simulated Tb for each constellation sensor, the Bayesian method is completely parametric and thus well suited for GPM's constellation approach. The a-priori information will be supplied by the combined algorithm supplied by GPM's core satellite as soon after launch as feasible. Databases for V0 of the algorithm had to be constructed from various sources as described in the ATBD. The solution provides a mean rain rate as well as the vertical structure of cloud and precipitation hydrometeors and their uncertainty",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "GPM_2AGPROFNOAA16AMSUB",
-            "creator": "GPM Science Team",
-            "title": "GPM AMSU-B on NOAA16 (GPROF) Climate-based Radiometer Precipitation Profiling L2 1.5 hours 16 km V07 (GPM_2AGPROFNOAA16AMSUB) at GES DISC",
-            "graphic-preview-description": "GPM AMSU-B on NOAA16 (GPROF) Climate-based Radiometer Precipitation Profiling L2 1.5 hours 16 km (GPM_2AGPROFNOAA16AMSUB)",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/GPM/browse/2A-CLIM-BR.NOAA16.AMSUB.GPROF2017v2.20001004-S121203-E135409.000184.V05A.PNG",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGPM%2FAMSUB%2FNOAA16%2FGPROFCLIM%2F2A%2F07",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGPM%2FAMSUB%2FNOAA16%2FGPROFCLIM%2F2A%2F07",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/GPM/browse/2A-CLIM-BR.NOAA16.AMSUB.GPROF2017v2.20001004-S121203-E135409.000184.V05A.PNG",
-                    "description": "GPM AMSU-B on NOAA16 (GPROF) Climate-based Radiometer Precipitation Profiling L2 1.5 hours 16 km (GPM_2AGPROFNOAA16AMSUB)",
                     "@type": "dcat:Distribution",
+                    "description": "GPM AMSU-B on NOAA16 (GPROF) Climate-based Radiometer Precipitation Profiling L2 1.5 hours 16 km (GPM_2AGPROFNOAA16AMSUB)",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/GPM/browse/2A-CLIM-BR.NOAA16.AMSUB.GPROF2017v2.20001004-S121203-E135409.000184.V05A.PNG",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/GPM_2AGPROFNOAA16AMSUB_CLIM_07.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/GPM_2AGPROFNOAA16AMSUB_CLIM_07.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://gpm1.gesdisc.eosdis.nasa.gov/data/GPM_L2/GPM_2AGPROFNOAA16AMSUB_CLIM.07/",
-                    "description": "Access the data via HTTPS",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS",
+                    "downloadURL": "https://gpm1.gesdisc.eosdis.nasa.gov/data/GPM_L2/GPM_2AGPROFNOAA16AMSUB_CLIM.07/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=GPM_2AGPROFNOAA16AMSUB_07",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=GPM_2AGPROFNOAA16AMSUB_07",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://gpm1.gesdisc.eosdis.nasa.gov/opendap/GPM_L2/GPM_2AGPROFNOAA16AMSUB_CLIM.07/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://gpm1.gesdisc.eosdis.nasa.gov/opendap/GPM_L2/GPM_2AGPROFNOAA16AMSUB_CLIM.07/contents.html",
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
@@ -803608,223 +803582,251 @@
                     "title": "View this dataset's algorithm theoretical basis document"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://arthurhou.pps.eosdis.nasa.gov/Documents/GPROFV07A_releasenotes.pdf",
-                    "description": "Release Notes",
                     "@type": "dcat:Distribution",
+                    "description": "Release Notes",
+                    "downloadURL": "https://arthurhou.pps.eosdis.nasa.gov/Documents/GPROFV07A_releasenotes.pdf",
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
```

