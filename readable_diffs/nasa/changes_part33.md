# Change History for nasa.json (Part 33)

### Changes from 31606f9 to dd2190f (Part 22/162)
**Author:** Automated

**Date:** 2025-02-01 15:02:16+00:00

**Message:** Updated data: Sat Feb  1 15:02:16 UTC 2025

```diff
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/zip",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/sageiii-iss/read_software/readers_G3B_v05.30.zip",
-                    "description": "SAGE III/ISS Data Read Software Package - Direct File Download (.zip)",
                     "@type": "dcat:Distribution",
+                    "description": "SAGE III/ISS Data Read Software Package - Direct File Download (.zip)",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/sageiii-iss/read_software/readers_G3B_v05.30.zip",
+                    "mediaType": "application/zip",
                     "title": "Downloadable software applications"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/sageiii-iss/guide/DPUG_G3B_v05.30.pdf",
-                    "description": "SAGE III/ISS Version 5.30 DPUG (Data Product User's Guide)",
                     "@type": "dcat:Distribution",
+                    "description": "SAGE III/ISS Version 5.30 DPUG (Data Product User's Guide)",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/sageiii-iss/guide/DPUG_G3B_v05.30.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/citing-data",
-                    "description": "How to cite ASDC data",
                     "@type": "dcat:Distribution",
+                    "description": "How to cite ASDC data",
+                    "downloadURL": "https://asdc.larc.nasa.gov/citing-data",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/sageiii-iss/read_software/19529_SAGE_III_NOSA_1.3_License.pdf",
-                    "description": "NASA Open Source Agreement for Computer Software",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Open Source Agreement for Computer Software",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/sageiii-iss/read_software/19529_SAGE_III_NOSA_1.3_License.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/sageiii-iss/guide/ReleaseNotes_G3B_v05.30.pdf",
-                    "description": "SAGE III/ISS Version 5.30 Release Notes",
                     "@type": "dcat:Distribution",
+                    "description": "SAGE III/ISS Version 5.30 Release Notes",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/sageiii-iss/guide/ReleaseNotes_G3B_v05.30.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2626885220-LARC",
-                    "description": "Earthdata Search for g3btb_53 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for g3btb_53 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2626885220-LARC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 }
             ],
+            "identifier": "C2626885220-LARC",
+            "issued": "2022-11-10",
+            "keyword": [
+                "atmospheric radiation",
+                "atmosphere",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/ISS/SAGEIII/SOLAR_BINARY_L1B-V5.3",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2022-11-17",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/LARC/SD/ASDC"
+            },
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2017-06-07T00:00:00Z/2023-04-10T00:00:00Z",
             "theme": [
                 "SAGE III-ISS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "SAGE III/ISS L1B Solar Event Transmission Data (Native) V053"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewBundle.jsp?identifier=urn%3Anasa%3Apds%3Aast.mrc.families&version=1.0",
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
+            "description": "This bundle contains an updated         compilation of asteroid families and clusters, resulting from the      application of the Hierarchical Clustering Method (HCM) on a set of    around 120,000 asteroids with available proper elements. Whenever      available, the classification in the Bus taxonomy is provided for      family members, based on spectra from the SMASS, SMASS2 and S3OS2      spectroscopic surveys.",
+            "identifier": "urn:nasa:pds:ast.mrc.families",
+            "issued": "2021-05-21",
+            "keyword": [
+                "multiple asteroids",
+                "none"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewBundle.jsp?identifier=urn%3Anasa%3Apds%3Aast.mrc.families&version=1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:ast.mrc.families",
-            "description": "This bundle contains an updated         compilation of asteroid families and clusters, resulting from the      application of the Hierarchical Clustering Method (HCM) on a set of    around 120,000 asteroids with available proper elements. Whenever      available, the classification in the Bus taxonomy is provided for      family members, based on spectra from the SMASS, SMASS2 and S3OS2      spectroscopic surveys.",
-            "title": "MOTHE-DINIZ ASTEROID DYNAMICAL FAMILIES",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "MOTHE-DINIZ ASTEROID DYNAMICAL FAMILIES"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/2370",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Hook, S.J., J.S. Myers, K.J. Thome, M. Fitzgerald, A.B. Kahle,  Airborne Sensor Facility NASA Ames Research Center, and R.F. Kokaly. 2024. MASTER: Geological Earth Mapping Experiment (GEMx), Spring 2024. ORNL DAAC, Oak Ridge, Tennessee, USA. https://doi.org/10.3334/ORNLDAAC/2370",
-            "issued": "2024-10-14",
-            "temporal": "2024-04-02T00:00:01Z/2024-06-24T23:23:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-10-17",
-            "keyword": [
-                "earth science",
-                "infrared wavelengths",
-                "spectral/engineering",
-                "visible wavelengths"
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
-            "identifier": "C3255928163-ORNL_CLOUD",
             "description": "This dataset includes Level 1B (L1B) data products from the MODIS/ASTER Airborne Simulator (MASTER) instrument. The spectral data were collected during 26 flights aboard a NASA ER-2 aircraft over California, Oregon, Nevada, and Arizona, US, from 2024-04-02 to 2024-06-24. The Geological Earth Mapping Experiment (GEMx) research project used NASA's Airborne Visible/Infrared Imaging Spectrometer (AVIRIS), Hyperspectral Thermal Emission Spectrometer (HyTES), and MODIS/ASTER Airborne Simulator (MASTER) instruments to collect the measurements over the country's arid and semi-arid regions, including parts of California, Nevada, Arizona, and New Mexico, to map portions of southwest US for critical minerals. Data products include L1B georeferenced multispectral imagery of calibrated radiance in 50 bands covering wavelengths of 0.460 to 12.879 micrometers at approximately 50-meter spatial resolution. The L1B file format is HDF-4. In addition, the dataset includes the flight path, spectral band information, instrument configuration, ancillary notes, and summary information for each flight, and browse images derived from each L1B data file. Level 2 products from these GEMx flights will be added to this dataset when they become available.",
-            "graphic-preview-description": "Single band images and an RGB composite image from flight track 1 acquired on 02 April 2024 over Primm, Nevada, US (approx. 35.60 lat, -115.40 lon). Source: MASTERL1B_2493400_01_20240402_1859_1902_V01.jpg",
-            "title": "MASTER: Geological Earth Mapping Experiment (GEMx), Spring 2024",
-            "graphic-preview-file": "https://daac.ornl.gov/MASTER/guides/MASTER_GEMx_Spring_2024_Fig1.jpg",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F2370",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F2370",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/master/MASTER_GEMx_Spring_2024/data/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/master/MASTER_GEMx_Spring_2024/data/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/MASTER/guides/MASTER_GEMx_Spring_2024.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/MASTER/guides/MASTER_GEMx_Spring_2024.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/2370",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/2370",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/master/MASTER_GEMx_Spring_2024/comp/MASTER_GEMx_Spring_2024.pdf",
-                    "description": "MASTER: Geological Earth Mapping Experiment (GEMx), Spring 2024: MASTER_GEMx_Spring_2024.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "MASTER: Geological Earth Mapping Experiment (GEMx), Spring 2024: MASTER_GEMx_Spring_2024.pdf",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/master/MASTER_GEMx_Spring_2024/comp/MASTER_GEMx_Spring_2024.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://daac.ornl.gov/MASTER/guides/MASTER_GEMx_Spring_2024_Fig1.jpg",
-                    "description": "Single band images and an RGB composite image from flight track 1 acquired on 02 April 2024 over Primm, Nevada, US (approx. 35.60 lat, -115.40 lon). Source: MASTERL1B_2493400_01_20240402_1859_1902_V01.jpg",
                     "@type": "dcat:Distribution",
+                    "description": "Single band images and an RGB composite image from flight track 1 acquired on 02 April 2024 over Primm, Nevada, US (approx. 35.60 lat, -115.40 lon). Source: MASTERL1B_2493400_01_20240402_1859_1902_V01.jpg",
+                    "downloadURL": "https://daac.ornl.gov/MASTER/guides/MASTER_GEMx_Spring_2024_Fig1.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 }
             ],
+            "graphic-preview-description": "Single band images and an RGB composite image from flight track 1 acquired on 02 April 2024 over Primm, Nevada, US (approx. 35.60 lat, -115.40 lon). Source: MASTERL1B_2493400_01_20240402_1859_1902_V01.jpg",
+            "graphic-preview-file": "https://daac.ornl.gov/MASTER/guides/MASTER_GEMx_Spring_2024_Fig1.jpg",
+            "identifier": "C3255928163-ORNL_CLOUD",
+            "issued": "2024-10-14",
+            "keyword": [
+                "earth science",
+                "infrared wavelengths",
+                "spectral/engineering",
+                "visible wavelengths"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/2370",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2024-10-17",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "ORNL_DAAC"
+            },
             "spatial": "-124.26 31.14 -108.08 43.2",
+            "temporal": "2024-04-02T00:00:01Z/2024-06-24T23:23:59Z",
             "theme": [
                 "MASTER",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "MASTER: Geological Earth Mapping Experiment (GEMx), Spring 2024"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/3K9PK956EIQ9",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Kevin Bowman. 2020-09-28. CMSFluxOceanPrior. Version 3. Carbon Monitoring System Carbon Flux Ocean Prior L4 V3. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/3K9PK956EIQ9. https://disc.gsfc.nasa.gov/datacollection/CMSFluxOceanPrior_3.html. Digital Science Data.",
-            "issued": "2017-04-26",
-            "temporal": "2010-01-01T00:00:00Z/2022-12-31T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2017-08-18",
-            "keyword": [
-                "earth science",
-                "atmosphere",
-                "atmospheric chemistry",
-                "oceans",
-                "ocean chemistry"
-            ],
-            "data-presentation-form": "Digital Science Data",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Kevin Bowman",
                 "hasEmail": "mailto:kevin.w.bowman@jpl.nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
-            "identifier": "C3005726600-GES_DISC",
-            "description": "This dataset provides the Prior for the Carbon Flux for Ocean.\n\nThe NASA Carbon Monitoring System (CMS) is designed to make significant contributions in characterizing, quantifying, understanding, and predicting the evolution of global carbon sources and sinks through improved monitoring of carbon stocks and fluxes. The System will use the full range of NASA satellite observations and modeling/analysis capabilities to establish the accuracy, quantitative uncertainties, and utility of products for supporting national and international policy, regulatory, and management activities. CMS will maintain a global emphasis while providing finer scale regional information, utilizing space-based and surface-based data and will rapidly initiate generation and distribution of products both for user evaluation and to inform near-term policy development and planning.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "CMSFluxOceanPrior",
             "creator": "Kevin Bowman",
-            "title": "Carbon Monitoring System Carbon Flux Ocean Prior L4 V3 (CMSFluxOceanPrior)",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/CMS/CMSFluxOceanPrior_3.png",
-            "programCode": [
-                "026:001"
-            ],
+            "data-presentation-form": "Digital Science Data",
+            "description": "This dataset provides the Prior for the Carbon Flux for Ocean.\n\nThe NASA Carbon Monitoring System (CMS) is designed to make significant contributions in characterizing, quantifying, understanding, and predicting the evolution of global carbon sources and sinks through improved monitoring of carbon stocks and fluxes. The System will use the full range of NASA satellite observations and modeling/analysis capabilities to establish the accuracy, quantitative uncertainties, and utility of products for supporting national and international policy, regulatory, and management activities. CMS will maintain a global emphasis while providing finer scale regional information, utilizing space-based and surface-based data and will rapidly initiate generation and distribution of products both for user evaluation and to inform near-term policy development and planning.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2F3K9PK956EIQ9",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2F3K9PK956EIQ9",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
@@ -219778,69 +219754,95 @@
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/CMSFluxOceanPrior_3.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/CMSFluxOceanPrior_3.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://acdisc.gsfc.nasa.gov/data/CMS/CMSFluxOceanPrior.3/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://acdisc.gsfc.nasa.gov/data/CMS/CMSFluxOceanPrior.3/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://acdisc.gsfc.nasa.gov/opendap/CMS/CMSFluxOceanPrior.3/",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://acdisc.gsfc.nasa.gov/opendap/CMS/CMSFluxOceanPrior.3/",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/CMS/README.CMS_Flux_V3.pdf",
-                    "description": "README Document",
                     "@type": "dcat:Distribution",
+                    "description": "README Document",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/CMS/README.CMS_Flux_V3.pdf",
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
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=CMSFluxOceanPrior",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=CMSFluxOceanPrior",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 }
             ],
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/CMS/CMSFluxOceanPrior_3.png",
+            "identifier": "C3005726600-GES_DISC",
+            "issued": "2017-04-26",
+            "keyword": [
+                "earth science",
+                "atmosphere",
+                "atmospheric chemistry",
+                "oceans",
+                "ocean chemistry"
+            ],
+            "landingPage": "https://doi.org/10.5067/3K9PK956EIQ9",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2017-08-18",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
+            },
+            "release-place": "Greenbelt, MD, USA",
+            "series-name": "CMSFluxOceanPrior",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2010-01-01T00:00:00Z/2022-12-31T23:59:59.999Z",
             "theme": [
                 "CMS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Carbon Monitoring System Carbon Flux Ocean Prior L4 V3 (CMSFluxOceanPrior)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-3-PRL-67PCHURYUMOV-M03-V2.0",
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
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-3-prl-67pchuryumov-m03-v2.0",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2021-05-21",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "calibration",
                 "16 cyg b",
@@ -219849,1078 +219851,1078 @@
                 "vega",
                 "zeta cas"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-3-PRL-67PCHURYUMOV-M03-V2.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-3-prl-67pchuryumov-m03-v2.0",
-            "description": "This data set contains images acquired by the OSIRIS Wide Angle Camera during the PRELANDING phase of the Rosetta mission at the comet 67P, covering the period from 2014-05-07T12:48:00.000 to 2014-06-04T10:49:59.000. This version V2.0 supersedes previous deliveries of the same dataset.",
-            "title": "ROSETTA-ORBITER PRELANDING OSIWAC 3 RDR MTP003 V2.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER PRELANDING OSIWAC 3 RDR MTP003 V2.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewBundle.jsp?identifier=urn%3Anasa%3Apds%3Aa16oms&version=1.0",
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
-                "apollo 16",
-                "moon"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This bundle contains microfilm scans of formatted outputs of all data acquired by the Apollo 16 Orbital Mass Spectrometer from lunar orbit during 20-24 April 1972, along with relevant documentation.",
+            "identifier": "urn:nasa:pds:a16oms",
+            "issued": "2021-05-21",
+            "keyword": [
+                "apollo 16",
+                "moon"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewBundle.jsp?identifier=urn%3Anasa%3Apds%3Aa16oms&version=1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:a16oms",
-            "description": "This bundle contains microfilm scans of formatted outputs of all data acquired by the Apollo 16 Orbital Mass Spectrometer from lunar orbit during 20-24 April 1972, along with relevant documentation.",
-            "title": "Apollo 16 Orbital Mass Spectrometer Data Output Scans Bundle",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "Apollo 16 Orbital Mass Spectrometer Data Output Scans Bundle"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=DIF-C-HRII-3%2F4-EPOXI-HARTLEY2-V3.0",
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
-                "epoxi",
-                "103p/hartley 2 (1986 e2)"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This dataset contains calibrated, 1.05- to 4.8-micron spectral images of comet 103/P Hartley 2 acquired by the High Resolution Infrared Spectrometer (HRII) from 01 October through 26 November 2010 during the Hartley 2 encounter phase of the EPOXI mission. Version 3.0 includes the application of scaled master dark subtraction for DOY 307 and in scene dark subtraction for DOY 311-313, as well as the use of an average per scan optical bench temperature in the pipeline processing. Version 3 also includes the calibration enhancements implemented in Version 2 of this dataset: a new per-pixel linearity correction treatment and its propagation through the calibration steps (i.e., bad-pixel maps, flat-field file update, revised spectral calibration curve), new mode-dependent master darks, an optimized scaling factor for the master dark, and a refinement in the absolute spectral calibration curve.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.dif-c-hrii-3-4-epoxi-hartley2-v3.0_5ze8-2zhg",
+            "issued": "2018-06-26",
+            "keyword": [
+                "epoxi",
+                "103p/hartley 2 (1986 e2)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=DIF-C-HRII-3%2F4-EPOXI-HARTLEY2-V3.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.dif-c-hrii-3-4-epoxi-hartley2-v3.0_5ze8-2zhg",
-            "description": "This dataset contains calibrated, 1.05- to 4.8-micron spectral images of comet 103/P Hartley 2 acquired by the High Resolution Infrared Spectrometer (HRII) from 01 October through 26 November 2010 during the Hartley 2 encounter phase of the EPOXI mission. Version 3.0 includes the application of scaled master dark subtraction for DOY 307 and in scene dark subtraction for DOY 311-313, as well as the use of an average per scan optical bench temperature in the pipeline processing. Version 3 also includes the calibration enhancements implemented in Version 2 of this dataset: a new per-pixel linearity correction treatment and its propagation through the calibration steps (i.e., bad-pixel maps, flat-field file update, revised spectral calibration curve), new mode-dependent master darks, an optimized scaling factor for the master dark, and a refinement in the absolute spectral calibration curve.",
-            "title": "EPOXI 103P/HARTLEY2 ENCOUNTER - HRII CALIBRATED SPECTRA V3.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "EPOXI 103P/HARTLEY2 ENCOUNTER - HRII CALIBRATED SPECTRA V3.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RPCLAP-3-EXT1-CALIB2-V1.0",
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
+            "description": "This data set contains\nCALIBRATED data from Rosetta RPC-LAP, acquired during the ROSETTA\nEXTENSION 1 mission phase where the primary target was the comet\n67P/CHURYUMOV-GERASIMENKO 1 (1969 R1). It contains instrument outputs in\nvolts and amperes, calibrated and corrected for instrument offsets.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rpclap-3-ext1-calib2-v1.0_5zg4-83yq",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RPCLAP-3-EXT1-CALIB2-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rpclap-3-ext1-calib2-v1.0_5zg4-83yq",
-            "description": "This data set contains\nCALIBRATED data from Rosetta RPC-LAP, acquired during the ROSETTA\nEXTENSION 1 mission phase where the primary target was the comet\n67P/CHURYUMOV-GERASIMENKO 1 (1969 R1). It contains instrument outputs in\nvolts and amperes, calibrated and corrected for instrument offsets.",
-            "title": "ROSETTA-ORBITER 67P RPCLAP 3\nEXT1 CALIB2 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RPCLAP 3\nEXT1 CALIB2 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://c3.nasa.gov/dashlink/resources/533/",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2012-02-13",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
-            "keyword": [
-                "dashlink",
-                "ames",
-                "nasa"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "DAVID SCHUSTER",
                 "hasEmail": "mailto:david.m.schuster@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Dashlink"
-            },
-            "identifier": "DASHLINK_533",
             "description": "RSW Wing Grid.  Structured single-block grid with viscous tunnel wall.  PLOT3D Format",
-            "title": "RSW-CFL3D-Schuster-Coarse Grid",
-            "programCode": [
-                "026:029"
-            ],
             "distribution": [
                 {
-                    "mediaType": "application/octet-stream",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/RSW-CFL3D-Coarse.g",
-                    "description": "RSW-CFL3D-Coarse.g",
                     "@type": "dcat:Distribution",
+                    "description": "RSW-CFL3D-Coarse.g",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/RSW-CFL3D-Coarse.g",
+                    "mediaType": "application/octet-stream",
                     "title": "RSW-CFL3D-Coarse.g"
                 }
             ],
-            "accrualPeriodicity": "irregular"
+            "identifier": "DASHLINK_533",
+            "issued": "2012-02-13",
+            "keyword": [
+                "dashlink",
+                "ames",
+                "nasa"
+            ],
+            "landingPage": "https://c3.nasa.gov/dashlink/resources/533/",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:029"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Dashlink"
+            },
+            "title": "RSW-CFL3D-Schuster-Coarse Grid"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/NE8CLN3ES5XQ",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "SnowEx Mores Creek Summit (MCS) Airborne LiDAR Survey V001. Version 1. Archived by National Aeronautics and Space Administration, U.S. Government, NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/NE8CLN3ES5XQ.",
-            "issued": "2022-02-17",
-            "temporal": "2021-03-10T00:00:00Z/2024-04-18T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-04-18",
-            "keyword": [
-                "land surface",
-                "snow/ice",
-                "earth science",
-                "vegetation",
-                "cryosphere",
-                "biosphere",
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
-            "identifier": "C3242734666-NSIDC_ECS",
             "description": "The data set provides digital terrain models (DTM), digital surface models (DSM) snow depth models, and canopy height models (CHM), derived from point cloud data (available as  <a href=\"https://nsidc.org/data/SNEX_MCS_Lidar_Raw\">SnowEx Mores Creek Summit (MCS) Airborne LiDAR Survey Raw, Version 1</a>) acquired by airborne lidar scanning. Data were collected as part of a multi-year effort to monitor monthly snow distribution over a 35 km\u00b2 region of the Mores Creek Headwaters in the Boise Mountains of central Idaho between 2021 and 2024. Data acquisition in 2021 overlapped temporally with the NASA SnowEx 2021 field campaign.",
-            "title": "SnowEx Mores Creek Summit (MCS) Airborne LiDAR Survey V001",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FNE8CLN3ES5XQ",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FNE8CLN3ES5XQ",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/SNOWEX/SNEX_MCS_Lidar.001/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/SNOWEX/SNEX_MCS_Lidar.001/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=SNEX_MCS_Lidar+V001",
-                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=SNEX_MCS_Lidar+V001",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/data/data-access-tool/SNEX_MCS_Lidar/versions/1/",
-                    "description": "Search and filter data files using a map-based interface",
                     "@type": "dcat:Distribution",
+                    "description": "Search and filter data files using a map-based interface",
+                    "downloadURL": "https://nsidc.org/data/data-access-tool/SNEX_MCS_Lidar/versions/1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/SNOWEX/SNEX_MCS_Lidar.001/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/SNOWEX/SNEX_MCS_Lidar.001/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=SNEX_MCS_Lidar+V001",
-                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=SNEX_MCS_Lidar+V001",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/data/data-access-tool/SNEX_MCS_Lidar/versions/1/",
-                    "description": "Search and filter data files using a map-based interface",
                     "@type": "dcat:Distribution",
+                    "description": "Search and filter data files using a map-based interface",
+                    "downloadURL": "https://nsidc.org/data/data-access-tool/SNEX_MCS_Lidar/versions/1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/NE8CLN3ES5XQ",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/NE8CLN3ES5XQ",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/NE8CLN3ES5XQ",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/NE8CLN3ES5XQ",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C3242734666-NSIDC_ECS",
+            "issued": "2022-02-17",
+            "keyword": [
+                "land surface",
+                "snow/ice",
+                "earth science",
+                "vegetation",
+                "cryosphere",
+                "biosphere",
+                "topography"
+            ],
+            "landingPage": "https://doi.org/10.5067/NE8CLN3ES5XQ",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2024-04-18",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA NSIDC DAAC"
+            },
             "spatial": "-115.7304987 43.9136453 -115.6424377 43.9748021",
+            "temporal": "2021-03-10T00:00:00Z/2024-04-18T23:59:59.999Z",
             "theme": [
                 "SnowEx",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "SnowEx Mores Creek Summit (MCS) Airborne LiDAR Survey V001"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1078",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Kim, D.-G., R. Vargas, B.P. Bond-Lamberty, and M.R. Turetsky. 2012. A Global Database of Gas Fluxes from Soils after Rewetting or Thawing, Version 1.0. ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/1078",
-            "issued": "2022-02-12",
-            "temporal": "1956-01-01T00:00:00Z/2009-12-31T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-06-12",
-            "keyword": [
-                "soils",
-                "atmospheric chemistry",
-                "biosphere",
-                "atmosphere",
-                "earth science",
-                "agriculture",
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
-            "identifier": "C2216863284-ORNL_CLOUD",
             "description": "This database contains information compiled from published studies on gas flux from soil following rewetting or thawing. The resulting database includes 222 field and laboratory observations focused on rewetting of dry soils, and 116 field laboratory observations focused on thawing of frozen soils studies conducted from 1956 to 2010. Fluxes of carbon dioxide, methane, nitrous oxide, nitrogen oxide, and ammonia (CO2, CH4, N2O, NO and NH3) were compiled from the literature and the flux rates were normalized for ease of comparison. Field observations of gas flux following rewetting of dry soils include events caused by natural rainfall, simulated rainfall in natural ecosystems, and irrigation in agricultural lands. Similarly, thawing of frozen soils include field observations of natural thawing, simulated freezing-thawing events (i.e., thawing of simulated frozen soil by snow removal), and thawing of seasonal ice in temperate and high latitude regions (Kim et al., 2012). Reported parameters include experiment type, location, site type, vegetation, climate, soil properties, rainfall, soil moisture, soil gas flux after wetting and thawing, peak soil gas flux properties, and the corresponding study references. There is one comma-delimited data file.",
-            "graphic-preview-description": "Location of 215 out of 338 cited database observations.",
-            "title": "A Global Database of Gas Fluxes from Soils after Rewetting or Thawing, Version 1.0",
-            "graphic-preview-file": "https://daac.ornl.gov/SOILS/guides/global_rtsg_flux_v1_figure1.jpg",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1078",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1078",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/global_soil/Global_RTSG_Flux/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/global_soil/Global_RTSG_Flux/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/SOILS/guides/Global_RTSG_Flux.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/SOILS/guides/Global_RTSG_Flux.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1078",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1078",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/global_soil/Global_RTSG_Flux/comp/Global_RTSG_Flux.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/global_soil/Global_RTSG_Flux/comp/Global_RTSG_Flux.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/global_soil/Global_RTSG_Flux/comp/unit_conversion_table_v1.csv",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/global_soil/Global_RTSG_Flux/comp/unit_conversion_table_v1.csv",
+                    "mediaType": "text/csv",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://daac.ornl.gov/SOILS/guides/global_rtsg_flux_v1_figure1.jpg",
-                    "description": "Location of 215 out of 338 cited database observations.",
                     "@type": "dcat:Distribution",
+                    "description": "Location of 215 out of 338 cited database observations.",
+                    "downloadURL": "https://daac.ornl.gov/SOILS/guides/global_rtsg_flux_v1_figure1.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 }
             ],
+            "graphic-preview-description": "Location of 215 out of 338 cited database observations.",
+            "graphic-preview-file": "https://daac.ornl.gov/SOILS/guides/global_rtsg_flux_v1_figure1.jpg",
+            "identifier": "C2216863284-ORNL_CLOUD",
+            "issued": "2022-02-12",
+            "keyword": [
+                "soils",
+                "atmospheric chemistry",
+                "biosphere",
+                "atmosphere",
+                "earth science",
+                "agriculture",
+                "land surface",
+                "ecological dynamics"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1078",
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
             "spatial": "-149.63 -36.45 160.52 74.5",
+            "temporal": "1956-01-01T00:00:00Z/2009-12-31T23:59:59Z",
             "theme": [
                 "Soil",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "A Global Database of Gas Fluxes from Soils after Rewetting or Thawing, Version 1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ISS/SAGEIII/LUNAR_NetCDF4_L2-V5.3",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "SAGE III/ISS Science Team (2022), SAGE III/ISS L2 Monthly Lunar Event Species Profiles (NetCDF), version 5.3, Hampton, VA, USA: NASA Atmospheric Science Data Center (ASDC), Accessed <author citing data inserts date here>",
-            "issued": "2022-11-10",
-            "temporal": "2017-06-07T00:00:00Z/2023-04-10T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-11-17",
-            "keyword": [
-                "aerosols",
-                "earth science",
-                "atmospheric radiation",
-                "atmospheric pressure",
-                "atmospheric chemistry",
-                "atmospheric water vapor",
-                "atmosphere"
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
-            "identifier": "C2626885268-LARC",
             "description": "g3blmnc_53 is the Stratospheric Aerosol and Gas Experiment III (SAGE III) on the International Space Station (ISS) (SAGE III/ISS) Level 2 Monthly Lunar Event Species Profiles (NetCDF) V053 data product. It contains all the species products for a month of lunar events (the last day of each month is omitted) . SAGE III was Launched on February 19, 2017 on a SpaceX Falcon 9 from Kennedy Space Center, SAGE III-ISS is the second instrument from the SAGE III project, externally mounted on the ISS. This ISS-based instrument uses a technique known as occultation, which involves looking at the light from the Sun or Moon as it passes through Earth's atmosphere at the edge, or limb, of the planet to provide long-term monitoring of ozone vertical profiles of the stratosphere and mesosphere. The data provided by SAGE III-ISS includes key components of atmospheric composition and their long-term variability, focusing on the study of aerosols, chlorine dioxide, clouds, nitrogen dioxide, nitrogen trioxide, pressure and temperature, and water vapor. SAGE data has historically been used by the World Meteorological Organization to inform their periodic assessments of ozone depletion. These new observations from the International Space Station will continue the SAGE team's contributions to ongoing scientific understanding of the Earth's atmosphere.",
-            "title": "SAGE III/ISS L2 Monthly Lunar Event Species Profiles (NetCDF) V053",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FISS%2FSAGEIII%2FLUNAR_NetCDF4_L2-V5.3",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FISS%2FSAGEIII%2FLUNAR_NetCDF4_L2-V5.3",
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
-                    "downloadURL": "https://doi.org/10.5067/ISS/SAGEIII/LUNAR_NetCDF4_L2-V5.3",
-                    "description": "DOI data set landing page for g3blmnc_53",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for g3blmnc_53",
+                    "downloadURL": "https://doi.org/10.5067/ISS/SAGEIII/LUNAR_NetCDF4_L2-V5.3",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/sageiii-iss/guide/ReleaseNotes_G3B_v05.30.pdf",
-                    "description": "SAGE III/ISS Version 5.30 Release Notes",
                     "@type": "dcat:Distribution",
+                    "description": "SAGE III/ISS Version 5.30 Release Notes",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/sageiii-iss/guide/ReleaseNotes_G3B_v05.30.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/sageiii-iss/guide/DPUG_G3B_v05.30.pdf",
-                    "description": "SAGE III/ISS Version 5.30 DPUG (Data Product User's Guide)",
                     "@type": "dcat:Distribution",
+                    "description": "SAGE III/ISS Version 5.30 DPUG (Data Product User's Guide)",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/sageiii-iss/guide/DPUG_G3B_v05.30.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
                 },
                 {
-                    "mediaType": "application/zip",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/sageiii-iss/read_software/readers_G3B_v05.30.zip",
-                    "description": "SAGE III/ISS Data Read Software Package - Direct File Download (.zip)",
                     "@type": "dcat:Distribution",
+                    "description": "SAGE III/ISS Data Read Software Package - Direct File Download (.zip)",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/sageiii-iss/read_software/readers_G3B_v05.30.zip",
+                    "mediaType": "application/zip",
                     "title": "Downloadable software applications"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/sageiii-iss/read_software/19529_SAGE_III_NOSA_1.3_License.pdf",
-                    "description": "NASA Open Source Agreement for Computer Software",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Open Source Agreement for Computer Software",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/sageiii-iss/read_software/19529_SAGE_III_NOSA_1.3_License.pdf",
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
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2626885268-LARC",
-                    "description": "Earthdata Search for g3blmnc_53 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for g3blmnc_53 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2626885268-LARC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 }
             ],
+            "identifier": "C2626885268-LARC",
+            "issued": "2022-11-10",
+            "keyword": [
+                "aerosols",
+                "earth science",
+                "atmospheric radiation",
+                "atmospheric pressure",
+                "atmospheric chemistry",
+                "atmospheric water vapor",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.5067/ISS/SAGEIII/LUNAR_NetCDF4_L2-V5.3",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2022-11-17",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/LARC/SD/ASDC"
+            },
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2017-06-07T00:00:00Z/2023-04-10T00:00:00Z",
             "theme": [
                 "SAGE III-ISS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "SAGE III/ISS L2 Monthly Lunar Event Species Profiles (NetCDF) V053"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewBundle.jsp?identifier=urn%3Anasa%3Apds%3Acorss_saturn_ionosphere&version=1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "Cassini radio occultations of the Saturn ionosphere",
+            "identifier": "urn:nasa:pds:corss_saturn_ionosphere",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2021-05-21",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "cassini",
                 "cassini orbiter rss saturn",
                 "saturn"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewBundle.jsp?identifier=urn%3Anasa%3Apds%3Acorss_saturn_ionosphere&version=1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:corss_saturn_ionosphere",
-            "description": "Cassini radio occultations of the Saturn ionosphere",
-            "title": "Saturn Ionosphere Bundle",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "Saturn Ionosphere Bundle"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=DIF-C-HRIV-2-EPOXI-HARTLEY2-V1.0",
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
-                "103p/hartley 2 (1986 e2)",
-                "epoxi"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This dataset contains raw clear-filter images of comet 103/P Hartley 2 acquired by the High Resolution Visible CCD (HRIV) from 05 September through 26 November 2010 during the Hartley 2 encounter phase of the EPOXI mission. Four color-filter sets (350-950 nm) were acquired during the hour about closest approach.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.dif-c-hriv-2-epoxi-hartley2-v1.0_5zrc-rdtz",
+            "issued": "2018-06-26",
+            "keyword": [
+                "103p/hartley 2 (1986 e2)",
+                "epoxi"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=DIF-C-HRIV-2-EPOXI-HARTLEY2-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.dif-c-hriv-2-epoxi-hartley2-v1.0_5zrc-rdtz",
-            "description": "This dataset contains raw clear-filter images of comet 103/P Hartley 2 acquired by the High Resolution Visible CCD (HRIV) from 05 September through 26 November 2010 during the Hartley 2 encounter phase of the EPOXI mission. Four color-filter sets (350-950 nm) were acquired during the hour about closest approach.",
-            "title": "EPOXI 103P/HARTLEY2 ENCOUNTER - HRIV RAW IMAGES V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "EPOXI 103P/HARTLEY2 ENCOUNTER - HRIV RAW IMAGES V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/CPEX/APR3/DATA101",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Durden, Stephen L. and Simone  Tanelli.2022. Airborne Precipitation Radar 3rd Generation (APR-3) CPEX [indicate subset used]. Dataset available online from the NASA Global Hydrometeorology Resource Center DAAC, Huntsville, Alabama, U.S.A. DOI: http://dx.doi.org/10.5067/CPEX/APR3/DATA101",
-            "issued": "2022-08-03",
-            "temporal": "2017-05-27T19:06:52Z/2017-06-24T21:55:10Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-02-03",
-            "keyword": [
-                "atmosphere",
-                "earth science",
-                "spectral/engineering",
-                "radar",
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
-            "identifier": "C2409563129-GHRC_DAAC",
             "description": "The Airborne Precipitation Radar 3rd Generation (APR-3) CPEX dataset consists of radar reflectivity, Doppler velocity for all bands, linear depolarization ratio Ku-band, and normalized radar cross section measurements at Ka- and Ku- bands data collected by the APR-3 onboard the NASA DC-8 aircraft. These data were gathered during the Convective Processes Experiment (CPEX) aircraft field campaign. CPEX collected data to help answer questions about convective storm initiation, organization, growth, and dissipation in the North Atlantic-Gulf of Mexico-Caribbean Oceanic region during the early summer of 2017. These data files are available from May 27, 2017 through June 24, 2017 in a HDF-5 file, with associated browse imagery in JPG format.",
-            "title": "Airborne Precipitation Radar 3rd Generation (APR-3) CPEX V1",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FCPEX%2FAPR3%2FDATA101",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FCPEX%2FAPR3%2FDATA101",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=apr3cpex&ghrccloud%2Fdata%2F=",
-                    "description": "Files may be downloaded directly to your workstation from this link",
                     "@type": "dcat:Distribution",
+                    "description": "Files may be downloaded directly to your workstation from this link",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=apr3cpex&ghrccloud%2Fdata%2F=",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://dx.doi.org/10.5067/CPEX/DATA101",
-                    "description": "CPEX Field Campaign Collection DOI",
                     "@type": "dcat:Distribution",
+                    "description": "CPEX Field Campaign Collection DOI",
+                    "downloadURL": "http://dx.doi.org/10.5067/CPEX/DATA101",
+                    "mediaType": "text/html",
                     "title": "View information related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/cpex/apr3/doc/apr3cpex_dataset.pdf",
-                    "description": "Airborne Precipitation Radar 3rd Generation (APR-3) CPEX User Guide",
                     "@type": "dcat:Distribution",
+                    "description": "Airborne Precipitation Radar 3rd Generation (APR-3) CPEX User Guide",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/cpex/apr3/doc/apr3cpex_dataset.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://airbornescience.nasa.gov/sites/default/files/documents/pr2-mwj.pdf",
-                    "description": "Development of an advanced airborne precipitation radar.(Technical Feature)",
                     "@type": "dcat:Distribution",
+                    "description": "Development of an advanced airborne precipitation radar.(Technical Feature)",
+                    "downloadURL": "https://airbornescience.nasa.gov/sites/default/files/documents/pr2-mwj.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.1109/LGRS.2006.872929",
-                    "description": "Simultaneous Measurements of Ku- and Ka-band Sea Surface Cross-Sections by an Airborne Radar",
                     "@type": "dcat:Distribution",
+                    "description": "Simultaneous Measurements of Ku- and Ka-band Sea Surface Cross-Sections by an Airborne Radar",
+                    "downloadURL": "https://doi.org/10.1109/LGRS.2006.872929",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/home/field-campaigns/cpex",
-                    "description": "CPEX Field Campaign Project Homepage",
                     "@type": "dcat:Distribution",
+                    "description": "CPEX Field Campaign Project Homepage",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/home/field-campaigns/cpex",
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
+            "identifier": "C2409563129-GHRC_DAAC",
+            "issued": "2022-08-03",
+            "keyword": [
+                "atmosphere",
+                "earth science",
+                "spectral/engineering",
+                "radar",
+                "precipitation"
+            ],
+            "landingPage": "https://doi.org/10.5067/CPEX/APR3/DATA101",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2023-02-03",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/MSFC/GHRC"
+            },
             "spatial": "-96.0262 16.8091 -69.2994 28.9042",
+            "temporal": "2017-05-27T19:06:52Z/2017-06-24T21:55:10Z",
             "theme": [
                 "CPEX",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Airborne Precipitation Radar 3rd Generation (APR-3) CPEX V1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/270",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Peck, E.L., and T.R. Carroll. 1998. BOREAS HYD-06 Aircraft Gamma Ray Soil Moisture. ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/270",
-            "issued": "2023-11-22",
-            "temporal": "1993-08-01T00:00:00Z/1994-09-10T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-12-05",
-            "keyword": [
-                "land surface",
-                "earth science",
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
-            "identifier": "C2812442887-ORNL_CLOUD",
             "description": "Contains the aircraft estimates of soil moisture measured by the gamma ray instrument from HYD06.",
-            "graphic-preview-description": "Browse Image",
-            "title": "BOREAS HYD-06 Aircraft Gamma Ray Soil Moisture",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/boreas_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F270",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F270",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/boreas/HYD/h6acgsmd/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/boreas/HYD/h6acgsmd/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/BOREAS/guides/HYD06_AIRSM.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
-                    "title": "View documentation related to this dataset"
-                },
-                {
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/BOREAS/guides/HYD06_AIRSM.html",
                     "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/270",
-                    "description": "Data set Landing Page DOI URL",
+                    "title": "View documentation related to this dataset"
+                },
+                {
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/270",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/HYD/h6acgsmd/comp/h6acgsmd.def",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/HYD/h6acgsmd/comp/h6acgsmd.def",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/msword",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/HYD/h6acgsmd/comp/HYD06_AIRSM.doc",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/HYD/h6acgsmd/comp/HYD06_AIRSM.doc",
+                    "mediaType": "application/msword",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/HYD/h6acgsmd/comp/HYD06_AIRSM.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/HYD/h6acgsmd/comp/HYD06_AIRSM.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/HYD/h6acgsmd/comp/HYD06_AIRSM.txt",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/HYD/h6acgsmd/comp/HYD06_AIRSM.txt",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/gif",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/HYD/h6acgsmd/comp/HYD06_AIRSM_1.gif",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/HYD/h6acgsmd/comp/HYD06_AIRSM_1.gif",
+                    "mediaType": "image/gif",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/gif",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/HYD/h6acgsmd/comp/HYD06_AIRSM_2.gif",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/HYD/h6acgsmd/comp/HYD06_AIRSM_2.gif",
+                    "mediaType": "image/gif",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/msword",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/HYD/h6acgsmd/comp/HYD06_Cosmic.doc",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/HYD/h6acgsmd/comp/HYD06_Cosmic.doc",
+                    "mediaType": "application/msword",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/HYD/h6acgsmd/comp/HYD06_Cosmic.txt",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/HYD/h6acgsmd/comp/HYD06_Cosmic.txt",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/HYD/h6acgsmd/comp/hyd06_transect_ref.dat",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/HYD/h6acgsmd/comp/hyd06_transect_ref.dat",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/HYD/h6acgsmd/comp/hyd06_transect_ref.def",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/HYD/h6acgsmd/comp/hyd06_transect_ref.def",
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
+            "identifier": "C2812442887-ORNL_CLOUD",
+            "issued": "2023-11-22",
+            "keyword": [
+                "land surface",
+                "earth science",
+                "soils"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/270",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2023-12-05",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "ORNL_DAAC"
+            },
             "spatial": "-106.29 53.37 -98.26 55.94",
+            "temporal": "1993-08-01T00:00:00Z/1994-09-10T23:59:59Z",
             "theme": [
                 "BOREAS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "BOREAS HYD-06 Aircraft Gamma Ray Soil Moisture"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/OMGEV-ALMO1",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "OMG. 2022-02-28. OMG Ocean Water Properties Data from Alamo Floats. Version 1. OMG Ocean Water Properties Data from Alamo Floats Version 1. NASA/JPL/PODAAC. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/JPL/PODAAC. https://doi.org/10.5067/OMGEV-ALMO1. OMG, NASA/JPL/PODAAC, 2022-02-28, OMG Ocean Water Properties Data from Alamo Floats Version 1, .",
-            "issued": "2021-12-06",
-            "temporal": "2017-08-30T14:39:13Z/2022-08-31T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2021-12-06",
-            "keyword": [
-                "salinity/density",
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
-            "identifier": "C2491772150-POCLOUD",
-            "description": "This dataset contains level 1 in situ measurements of temperature and salinity from several autonomous, profiling Alamo floats. These floats change their buoyancy by inflating an external bladder with oil, allowing them to dive and surface regularly. Conductivity, Temperature and Depth sensors (CTDs) allow them to collect vertical profiles of temperature and salinity. This provided measurements of the ocean's physical characteristics around Greenland. The floats wer deployed as part of the Oceans Melting Greenland (OMG) project. The goal of the project is to find out what contributions the ocean has on Greenland's melting glaciers.",
-            "release-place": "NASA/JPL/PODAAC",
-            "series-name": "OMG Ocean Water Properties Data from Alamo Floats",
-            "graphic-preview-description": "Thumbnail",
             "creator": "OMG",
-            "title": "OMG Ocean Water Properties Data from Alamo Floats Version 1",
-            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/OMG_L1_FLOAT_ALAMO.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "This dataset contains level 1 in situ measurements of temperature and salinity from several autonomous, profiling Alamo floats. These floats change their buoyancy by inflating an external bladder with oil, allowing them to dive and surface regularly. Conductivity, Temperature and Depth sensors (CTDs) allow them to collect vertical profiles of temperature and salinity. This provided measurements of the ocean's physical characteristics around Greenland. The floats wer deployed as part of the Oceans Melting Greenland (OMG) project. The goal of the project is to find out what contributions the ocean has on Greenland's melting glaciers.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FOMGEV-ALMO1",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FOMGEV-ALMO1",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/omg/open/L1/docs/ALAMO/.gitkeep",
-                    "description": "Alamo Floats Supporting Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Alamo Floats Supporting Documentation",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/omg/open/L1/docs/ALAMO/.gitkeep",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/omg/open/L1/docs/omg-ocean-alamo-users-guide.pdf",
-                    "description": "User guide documentation for this dataset",
                     "@type": "dcat:Distribution",
+                    "description": "User guide documentation for this dataset",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/omg/open/L1/docs/omg-ocean-alamo-users-guide.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://omg.jpl.nasa.gov/",
-                    "description": "OMG Mission Page",
                     "@type": "dcat:Distribution",
+                    "description": "OMG Mission Page",
+                    "downloadURL": "https://omg.jpl.nasa.gov/",
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
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/OMG_L1_FLOAT_ALAMO.jpg",
-                    "description": "Thumbnail",
                     "@type": "dcat:Distribution",
+                    "description": "Thumbnail",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/OMG_L1_FLOAT_ALAMO.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2491772150-POCLOUD",
-                    "description": "HTTPS endpoint for data browse and download",
                     "@type": "dcat:Distribution",
+                    "description": "HTTPS endpoint for data browse and download",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2491772150-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2491772150-POCLOUD",
-                    "description": "Browse granule search results in Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse granule search results in Earthdata Search",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2491772150-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 }
             ],
+            "graphic-preview-description": "Thumbnail",
+            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/OMG_L1_FLOAT_ALAMO.jpg",
+            "identifier": "C2491772150-POCLOUD",
+            "issued": "2021-12-06",
+            "keyword": [
+                "salinity/density",
+                "earth science",
+                "oceans",
+                "ocean temperature"
+            ],
+            "landingPage": "https://doi.org/10.5067/OMGEV-ALMO1",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2021-12-06",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/JPL/PODAAC"
+            },
+            "release-place": "NASA/JPL/PODAAC",
+            "series-name": "OMG Ocean Water Properties Data from Alamo Floats",
             "spatial": "-74.576 60.351 53.406 79.841",
+            "temporal": "2017-08-30T14:39:13Z/2022-08-31T23:59:59.999Z",
             "theme": [
                 "OMG",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "OMG Ocean Water Properties Data from Alamo Floats Version 1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RPCMAG-3-ESC3-CALIBRATED-V6.0",
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
+            "description": "This dataset contains CALIBRATED (CODMAC LEVEL 3) DATA of the COMET\nESCORT 3 Phase (ESC3) from  July 1 until October 20, 2015 of the\nROSETTA orbiter magnetometer RPCMAG. Observations are done in the\nvicinity of comet 67P/CHURYUMOV-GERASIMENKO 1 (1969 R1).\nThe current version of the dataset is V6.0, the first one\nbeing archived.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rpcmag-3-esc3-calibrated-v6.0_5zzz-e2np",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RPCMAG-3-ESC3-CALIBRATED-V6.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rpcmag-3-esc3-calibrated-v6.0_5zzz-e2np",
-            "description": "This dataset contains CALIBRATED (CODMAC LEVEL 3) DATA of the COMET\nESCORT 3 Phase (ESC3) from  July 1 until October 20, 2015 of the\nROSETTA orbiter magnetometer RPCMAG. Observations are done in the\nvicinity of comet 67P/CHURYUMOV-GERASIMENKO 1 (1969 R1).\nThe current version of the dataset is V6.0, the first one\nbeing archived.",
-            "title": "ROSETTA-ORBITER 67P RPCMAG 3 ESC3 CALIBRATED V6.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RPCMAG 3 ESC3 CALIBRATED V6.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-4-EXT3-67P-M33-REFLECT-V1.0",
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
+            "description": "This CODMAC level 4 data set contains radiometric calibrated and geometric distortion corrected (resampled) image data in reflectance units (normalized and thus without unit), acquired by the OSIRIS Narrow Angle Camera on the Rosetta spacecraft during the ROSETTA EXTENSION 3 mission phase, covering the period from 2016-08-09T23:25:00.000 to 2016-09-02T06:39:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V1.0 is the first version of this dataset: Lien corrected dataset after October 2018 PSA/PDS external peer review.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-4-ext3-67p-m33-reflect-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-4-EXT3-67P-M33-REFLECT-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-4-ext3-67p-m33-reflect-v1.0",
-            "description": "This CODMAC level 4 data set contains radiometric calibrated and geometric distortion corrected (resampled) image data in reflectance units (normalized and thus without unit), acquired by the OSIRIS Narrow Angle Camera on the Rosetta spacecraft during the ROSETTA EXTENSION 3 mission phase, covering the period from 2016-08-09T23:25:00.000 to 2016-09-02T06:39:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V1.0 is the first version of this dataset: Lien corrected dataset after October 2018 PSA/PDS external peer review.",
-            "title": "ROSETTA-ORBITER 67P OSINAC 4 EXT3-MTP033 RDR-REFLECT V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P OSINAC 4 EXT3-MTP033 RDR-REFLECT V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/SLR/SLR_DAILY_NPT_001",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, CDDIS. https://doi.org/10.5067/SLR/SLR_DAILY_NPT_001.",
-            "issued": "1976-01-01",
-            "temporal": "2016-01-01T00:00:00Z/2024-11-18T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-15",
-            "keyword": [
-                "geodetics",
-                "earth science",
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
-            "identifier": "C1537476328-CDDIS",
             "description": "This dataset consists of ground-based Satellite Laser Ranging observation data (normal points, daily 24 hour files) from the NASA Crustal Dynamics Data Information System (CDDIS). SLR provides unambiguous range measurements to mm precision that can be aggregated over the global network to provide very accurate satellite orbits, time histories of station position and motion, and many other geophysical parameters. SLR operates in the optical region and is the only space geodetic technique that measures unambiguous range directly. Analysis of SLR data contributes to the terrestrial reference frame, modeling of the spatial and temporal variations of the Earth's gravitational field, and monitoring of millimeter-level variations in the location of the center of mass of the total Earth system (solid Earth-atmosphere-oceans). In addition, SLR provides precise orbit determination for spaceborne radar altimeter missions. It provides a means for sub-nanosecond global time transfer, and a basis for special tests of the Theory of General Relativity. Analysis Centers (ACs) of the International Laser Ranging Service (ILRS) retrieve SLR data on regular schedules to produce precise station positions and velocities for stations in the ILRS network. The daily SLR normal point observation files contain data received in the previous 24-hour period from a global network of stations ranging to satellites equipped with retroreflectors. Data are available in ILRS data format (older data sets) and/or the Consolidated Ranging Data (CRD) format. More information about these data is available on the CDDIS website at https://cddis.nasa.gov/Data_and_Derived_Products/SLR/Normal_point_data.html.",
-            "title": "Ground-Based Satellite Laser Ranging (SLR) Observation Data (normal points, daily, 24 hour files) from NASA CDDIS",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSLR%2FSLR_DAILY_NPT_001",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSLR%2FSLR_DAILY_NPT_001",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://cddis.nasa.gov/archive/slr/data",
-                    "description": "URL for retrieval of SLR derived products through https",
                     "@type": "dcat:Distribution",
+                    "description": "URL for retrieval of SLR derived products through https",
+                    "downloadURL": "https://cddis.nasa.gov/archive/slr/data",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://cddis.nasa.gov/Data_and_Derived_Products/SLR/Normal_point_data.html",
-                    "description": "URL for more information about SLR data",
                     "@type": "dcat:Distribution",
+                    "description": "URL for more information about SLR data",
+                    "downloadURL": "https://cddis.nasa.gov/Data_and_Derived_Products/SLR/Normal_point_data.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/SLR/slr_data_daily_npt_001",
-                    "description": "URL for more information about SLR data",
                     "@type": "dcat:Distribution",
+                    "description": "URL for more information about SLR data",
+                    "downloadURL": "https://doi.org/10.5067/SLR/slr_data_daily_npt_001",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 }
             ],
+            "identifier": "C1537476328-CDDIS",
+            "issued": "1976-01-01",
+            "keyword": [
+                "geodetics",
+                "earth science",
+                "solid earth",
+                "gravity/gravitational field",
+                "tectonics"
+            ],
+            "landingPage": "https://doi.org/10.5067/SLR/SLR_DAILY_NPT_001",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2024-11-15",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "CDDIS"
+            },
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2016-01-01T00:00:00Z/2024-11-18T00:00:00Z",
             "theme": [
                 "ILRS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Ground-Based Satellite Laser Ranging (SLR) Observation Data (normal points, daily, 24 hour files) from NASA CDDIS"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MESS-E%2FV%2FH-GRNS-5-GRS-DAP-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "Abstract ======== The GRS experiment is a gamma-ray spectrometer designed to observe spectra of gamma rays emitted from Mercury's surface in the energy range from 0.1 to 10 MeV. This data set consists of the MESSENGER GRS advanced data products (DAPs), which are jpeg2000 maps of gamma-ray count rates or elemental abundances derived from summed GRS data, each with a corresponding one standard deviation error map.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mess-e-v-h-grns-5-grs-dap-v1.0_625g-ua4a",
             "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "venus",
                 "messenger",
@@ -220928,88 +220930,63 @@
                 "earth",
                 "calibration"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MESS-E%2FV%2FH-GRNS-5-GRS-DAP-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mess-e-v-h-grns-5-grs-dap-v1.0_625g-ua4a",
-            "description": "Abstract ======== The GRS experiment is a gamma-ray spectrometer designed to observe spectra of gamma rays emitted from Mercury's surface in the energy range from 0.1 to 10 MeV. This data set consists of the MESSENGER GRS advanced data products (DAPs), which are jpeg2000 maps of gamma-ray count rates or elemental abundances derived from summed GRS data, each with a corresponding one standard deviation error map.",
-            "title": "MESSENGER E/V/H GRNS 5 GAMMA RAY SPECTROMETER DAP V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "MESSENGER E/V/H GRNS 5 GAMMA RAY SPECTROMETER DAP V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1513",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Bourgeau-Chavez, L.L., S. Endres, M. Battaglia, and E. Banda. 2017. NACP Peatland Land Cover Map of Upper Peninsula, Michigan, 2007-2011. ORNL DAAC, Oak Ridge, Tennessee, USA. https://doi.org/10.3334/ORNLDAAC/1513",
-            "issued": "2017-09-27",
-            "temporal": "2007-03-01T00:00:00Z/2011-10-01T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-06-12",
-            "keyword": [
-                "biosphere",
-                "land use/land cover",
-                "land surface",
-                "ecosystems",
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
-            "identifier": "C2517704644-ORNL_CLOUD",
             "description": "This dataset provides a land cover map focused on peatland ecosystems in the upper peninsula of Michigan. The map was produced at 12.5-m resolution using a multi-sensor fusion (optical and L-band SAR) approach with imagery from Landsat-5 TM and ALOS PALSAR collected between 2007 and 2011. A random forest classifier trained with polygons delineated from field data and aerial photography was used to determine pixel classes. Accuracy assessment based on field-sampled sites show high overall map accuracy (92%).",
-            "graphic-preview-description": "Browse Image",
-            "title": "NACP Peatland Land Cover Map of Upper Peninsula, Michigan, 2007-2011",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/sdat-tds/1513_1_fit.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1513",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1513",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/nacp/NACP_Peatland_Land_Cover_MI/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/nacp/NACP_Peatland_Land_Cover_MI/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/NACP/guides/NACP_Peatland_Land_Cover_MI.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/NACP/guides/NACP_Peatland_Land_Cover_MI.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1513",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1513",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
@@ -221037,841 +221014,876 @@
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://daac.ornl.gov/graphics/browse/sdat-tds/1513_1_fit.png",
-                    "description": "Browse Image",
                     "@type": "dcat:Distribution",
+                    "description": "Browse Image",
+                    "downloadURL": "https://daac.ornl.gov/graphics/browse/sdat-tds/1513_1_fit.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://webmap.ornl.gov/wcsdown/dataset.jsp?ds_id=1513",
-                    "description": "Web Coverage Service for this collection.",
                     "@type": "dcat:Distribution",
+                    "description": "Web Coverage Service for this collection.",
+                    "downloadURL": "https://webmap.ornl.gov/wcsdown/dataset.jsp?ds_id=1513",
+                    "mediaType": "text/html",
                     "title": "Use Web Coverage Service (WCS) to download the dataset's data"
                 }
             ],
+            "graphic-preview-description": "Browse Image",
+            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/sdat-tds/1513_1_fit.png",
+            "identifier": "C2517704644-ORNL_CLOUD",
+            "issued": "2017-09-27",
+            "keyword": [
+                "biosphere",
+                "land use/land cover",
+                "land surface",
+                "ecosystems",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1513",
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
             "spatial": "-91.08 44.54 -82.29 48.75",
+            "temporal": "2007-03-01T00:00:00Z/2011-10-01T23:59:59Z",
             "theme": [
                 "NACP",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "NACP Peatland Land Cover Map of Upper Peninsula, Michigan, 2007-2011"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-COMPIL-5-ASTMASS-V2.0",
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
+            "description": "This collection of asteroid masses and densities was compiled from the published literature by Jim Baer, Steve Chesley, and Dan Britt. Size and shape information are included as well as masses and densities. This is the version of the compilation as of Dec. 15, 2010.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-compil-5-astmass-v2.0_625v-ain8",
+            "issued": "2018-06-26",
+            "keyword": [
+                "support archives",
+                "asteroid"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-COMPIL-5-ASTMASS-V2.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-compil-5-astmass-v2.0_625v-ain8",
-            "description": "This collection of asteroid masses and densities was compiled from the published literature by Jim Baer, Steve Chesley, and Dan Britt. Size and shape information are included as well as masses and densities. This is the version of the compilation as of Dec. 15, 2010.",
-            "title": "ASTEROID MASSES V2.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "ASTEROID MASSES V2.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/627",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Hansen, M.C., R.S. Defries, J.R.G. Townshend, and R.A. Sohlberg. 2002. SAFARI 2000 Land Cover from AVHRR, 1-km, 1992-1993 (Hansen et al.). ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/627",
-            "issued": "2023-10-18",
-            "temporal": "1992-01-01T00:00:00Z/1993-12-31T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-12-19",
-            "keyword": [
-                "land surface",
-                "land use/land cover",
-                "biosphere",
-                "vegetation",
-                "earth science",
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
-            "identifier": "C2788343294-ORNL_CLOUD",
             "description": "This data set consists of a southern African subset of the 1-km Global Land Cover Data Set Derived from AVHRR developed at the Laboratory for Global Remote Sensing Studies (LGRSS) at the University of Maryland. Both ASCII data and binary image files are available.",
-            "graphic-preview-description": "Browse Image",
-            "title": "SAFARI 2000 Land Cover from AVHRR, 1-km, 1992-1993 (Hansen et al.)",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/safari_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F627",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F627",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/safari2k/vegetation_wetlands/land_cover_data-1km/data/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/safari2k/vegetation_wetlands/land_cover_data-1km/data/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "application/zip",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/protected/bundle/land_cover_data-1km_627.zip",
-                    "description": "Collection bundle",
                     "@type": "dcat:Distribution",
+                    "description": "Collection bundle",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/protected/bundle/land_cover_data-1km_627.zip",
+                    "mediaType": "application/zip",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/S2K/guides/glcf1km.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/S2K/guides/glcf1km.html",
+                    "mediaType": "text/html",
                     "title": "View this dataset's user's guide"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/627",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/627",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/zip",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/protected/bundle/land_cover_data-1km_627.zip",
-                    "description": "Collection bundle",
                     "@type": "dcat:Distribution",
+                    "description": "Collection bundle",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/protected/bundle/land_cover_data-1km_627.zip",
+                    "mediaType": "application/zip",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/safari2k/vegetation_wetlands/land_cover_data-1km/comp/0_readme.txt",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/safari2k/vegetation_wetlands/land_cover_data-1km/comp/0_readme.txt",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/safari2k/vegetation_wetlands/land_cover_data-1km/comp/glcf1km_readme.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/safari2k/vegetation_wetlands/land_cover_data-1km/comp/glcf1km_readme.pdf",
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
+            "identifier": "C2788343294-ORNL_CLOUD",
+            "issued": "2023-10-18",
+            "keyword": [
+                "land surface",
+                "land use/land cover",
+                "biosphere",
+                "vegetation",
+                "earth science",
+                "ecosystems"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/627",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2024-12-19",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "ORNL_DAAC"
+            },
             "spatial": "5.0 -35.0 60.0 5.0",
+            "temporal": "1992-01-01T00:00:00Z/1993-12-31T23:59:59Z",
             "theme": [
                 "SAFARI 2000",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "SAFARI 2000 Land Cover from AVHRR, 1-km, 1992-1993 (Hansen et al.)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ASDC_DAAC/FIRE/0019",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "1999-10-15. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/ASDC_DAAC/FIRE/0019.",
-            "issued": "1999-10-14",
-            "temporal": "1992-05-31T00:00:00Z/1992-06-29T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2018-07-06",
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
-            "identifier": "C1000000984-LARC_ASDC",
             "description": "The First ISCCP Regional Experiments have been designed to improve data products and cloud/radiation parameterizations used in general circulation models (GCMs). Specifically, the goals of FIRE are (1) to seek the basic understanding of the interaction of physical processes in determining life cycles of cirrus and marine stratocumulus systems and the radiative properties of these clouds during their life cycles and (2) to investigate the interrelationships between the ISCCP data, GCM parameterizations, and higher space and time resolution cloud data.To-date, four intensive field-observation periods were planned and executed: a cirrus IFO (October 13 - November 2, 1986); a marine stratocumulus IFO off the southwestern coast of California (June 29 - July 20, 1987) a second cirrus IFO in southeastern Kansas (November 13 - December 7, 1991); and a second marine stratocumulus IFO in the eastern North Atlantic Ocean (June 1 - June 28, 1992). Each mission combined coordinated satellite, airborne, and surface observationswith modeling studies to investigate the cloud properties and physical processes of the cloud system.The Belfort Laser Ceilometer was operated during FIRE ASTEX on Porto Santo, Madeira. It utilized a 20 watt near-infrared Gallium-Arsenide laser operating at a wavelength of 0.91 microns to detect cloud base height. It employed 1024 range gates which yield a vertical resolution of 25 feet up to a maximum range of 25,600 feet. The fields of view of the transmitter and receiver are approximately 1 degree.The ceilometer used a measured noise level to determine a count (-1,0,1) which is then summed for each gate. This histogram is the basic output from which the cloud base height is estimated.",
-            "title": "First ISCCP Regional Experiment (FIRE) Atlantic Stratocumulus Transition Experiment (ASTEX) Colorado State University (CSU) Ceilometer Data (FIRE_AX_CSU_CEILOM)",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC_DAAC%2FFIRE%2F0019",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC_DAAC%2FFIRE%2F0019",
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
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1000000984-LARC_ASDC",
-                    "description": "Earthdata Search for FIRE_AX_CSU_CEILOM_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for FIRE_AX_CSU_CEILOM_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1000000984-LARC_ASDC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/read_software/fax_csu_ceilom_read.c",
-                    "description": "Project Level/Data Set Level Read Software for SUN, HP, SGI, and Dec Alpha Platforms - Direct File Download (.c), HP, SGI, and Dec Alpha Platforms - Direct File Download (.c)",
                     "@type": "dcat:Distribution",
+                    "description": "Project Level/Data Set Level Read Software for SUN, HP, SGI, and Dec Alpha Platforms - Direct File Download (.c), HP, SGI, and Dec Alpha Platforms - Direct File Download (.c)",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/read_software/fax_csu_ceilom_read.c",
+                    "mediaType": "text/html",
                     "title": "View this dataset's science data product software documentation"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/guide/base_fire_ax_csu_dataset.pdf",
-                    "description": "FIRE ASTEX Colorado State University (CSU) Langley DAAC Data Set Document",
                     "@type": "dcat:Distribution",
+                    "description": "FIRE ASTEX Colorado State University (CSU) Langley DAAC Data Set Document",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/guide/base_fire_ax_csu_dataset.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/postscript",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/readme/readme_fire_ax_csu_ceilom.ps",
-                    "description": "FIRE ASTEX sample read software and data files - Direct File Download (.ps)",
                     "@type": "dcat:Distribution",
+                    "description": "FIRE ASTEX sample read software and data files - Direct File Download (.ps)",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/readme/readme_fire_ax_csu_ceilom.ps",
+                    "mediaType": "application/postscript",
                     "title": "View this dataset's science data product software documentation"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/ASDC_DAAC/FIRE/0019",
-                    "description": "DOI data set landing page for FIRE_AX_CSU_CEILOM_1",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for FIRE_AX_CSU_CEILOM_1",
+                    "downloadURL": "https://doi.org/10.5067/ASDC_DAAC/FIRE/0019",
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
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/FIRE/FIRE_AX_CSU_CEILOM/",
-                    "description": "ASDC Direct Data Download for FIRE_AX_CSU_CEILOM_1",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for FIRE_AX_CSU_CEILOM_1",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/FIRE/FIRE_AX_CSU_CEILOM/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/FIRE/FIRE_AX_CSU_CEILOM/contents.html",
-                    "description": "OPeNDAP data access for FIRE_AX_CSU_CEILOM_1",
                     "@type": "dcat:Distribution",
+                    "description": "OPeNDAP data access for FIRE_AX_CSU_CEILOM_1",
+                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/FIRE/FIRE_AX_CSU_CEILOM/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 }
             ],
+            "identifier": "C1000000984-LARC_ASDC",
+            "issued": "1999-10-14",
+            "keyword": [
+                "earth science",
+                "clouds",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.5067/ASDC_DAAC/FIRE/0019",
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
             "spatial": "33.08 -16.35",
+            "temporal": "1992-05-31T00:00:00Z/1992-06-29T23:59:59.999Z",
             "theme": [
                 "FIRE",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "First ISCCP Regional Experiment (FIRE) Atlantic Stratocumulus Transition Experiment (ASTEX) Colorado State University (CSU) Ceilometer Data (FIRE_AX_CSU_CEILOM)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-4-ESC1-67P-M13-INFLDSTR-V1.0",
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
+            "description": "This CODMAC level 4 data set contains solar stray-light corrected, in-field stray-light corrected,  radiometric calibrated and geometric distortion corrected  (resampled) image data in W/m^2/sr/nm,  acquired by the OSIRIS Narrow Angle Camera on the Rosetta spacecraft  during the COMET ESCORT 1 mission phase, covering the period  from 2015-02-10T23:25:00.000 to 2015-03-10T23:24:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V1.0 is the first version of this dataset: Lien corrected dataset after September 2019 PSA/PDS external peer review.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-4-esc1-67p-m13-infldstr-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-4-ESC1-67P-M13-INFLDSTR-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-4-esc1-67p-m13-infldstr-v1.0",
-            "description": "This CODMAC level 4 data set contains solar stray-light corrected, in-field stray-light corrected,  radiometric calibrated and geometric distortion corrected  (resampled) image data in W/m^2/sr/nm,  acquired by the OSIRIS Narrow Angle Camera on the Rosetta spacecraft  during the COMET ESCORT 1 mission phase, covering the period  from 2015-02-10T23:25:00.000 to 2015-03-10T23:24:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V1.0 is the first version of this dataset: Lien corrected dataset after September 2019 PSA/PDS external peer review.",
-            "title": "ROSETTA-ORBITER 67P OSINAC 4 ESC1-MTP013 RDR-INFLDSTR V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P OSINAC 4 ESC1-MTP013 RDR-INFLDSTR V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-VIRTIS-2-ESC3-MTP019-V1.0",
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
+            "description": "This release contains the digital numbers (DN) contained in the telemetry (TM) packages of the VIRTIS instrument on board of the spacecraft Rosetta. This volume contains data at the vicinity of comet 67P, from the ESCORT 3 MTP019 phase, which occurred from 2015-07-29 to 2015-08-26",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-virtis-2-esc3-mtp019-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-VIRTIS-2-ESC3-MTP019-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-virtis-2-esc3-mtp019-v1.0",
-            "description": "This release contains the digital numbers (DN) contained in the telemetry (TM) packages of the VIRTIS instrument on board of the spacecraft Rosetta. This volume contains data at the vicinity of comet 67P, from the ESCORT 3 MTP019 phase, which occurred from 2015-07-29 to 2015-08-26",
-            "title": "ROSETTA-ORBITER 67P VIRTIS 2 ESCORT 3 MTP019 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P VIRTIS 2 ESCORT 3 MTP019 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-4-PRL-67P-M05-INFLDSTR-V1.0",
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
+            "description": "This CODMAC level 4 data set contains solar stray-light corrected, in-field stray-light corrected,  radiometric calibrated and geometric distortion corrected  (resampled) image data in W/m^2/sr/nm,  acquired by the OSIRIS Wide Angle Camera on the Rosetta spacecraft  during the PRELANDING mission phase, covering the period  from 2014-07-02T08:35:00.000 to 2014-08-01T09:59:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V1.0 is the first version of this dataset: Lien corrected dataset after September 2019 PSA/PDS external peer review.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-4-prl-67p-m05-infldstr-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-4-PRL-67P-M05-INFLDSTR-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-4-prl-67p-m05-infldstr-v1.0",
-            "description": "This CODMAC level 4 data set contains solar stray-light corrected, in-field stray-light corrected,  radiometric calibrated and geometric distortion corrected  (resampled) image data in W/m^2/sr/nm,  acquired by the OSIRIS Wide Angle Camera on the Rosetta spacecraft  during the PRELANDING mission phase, covering the period  from 2014-07-02T08:35:00.000 to 2014-08-01T09:59:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V1.0 is the first version of this dataset: Lien corrected dataset after September 2019 PSA/PDS external peer review.",
-            "title": "ROSETTA-ORBITER 67P OSIWAC 4 PRL-MTP005 RDR-INFLDSTR V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P OSIWAC 4 PRL-MTP005 RDR-INFLDSTR V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=GO-J-PPR-3-EDR-SL9-G%2FH%2FL%2FQ1-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This is a selected portion of the Galileo PPR data set acquired for the Shoemaker-Levy 9 fragment impacts with Jupiter in July 1994. These data focus on the time periods in which the major events were detected. Times given are equivalent UTC times for Earth-based observers.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.go-j-ppr-3-edr-sl9-g-h-l-q1-v1.0_62h4-8vqj",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "galileo",
                 "comet sl9/jupiter collision",
                 "sl9",
                 "jupiter"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=GO-J-PPR-3-EDR-SL9-G%2FH%2FL%2FQ1-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.go-j-ppr-3-edr-sl9-g-h-l-q1-v1.0_62h4-8vqj",
-            "description": "This is a selected portion of the Galileo PPR data set acquired for the Shoemaker-Levy 9 fragment impacts with Jupiter in July 1994. These data focus on the time periods in which the major events were detected. Times given are equivalent UTC times for Earth-based observers.",
-            "title": "GO JUPITER/SHOEMAKER-LEVY 9 PPR CALIB FRAG G/H/L/Q1 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "GO JUPITER/SHOEMAKER-LEVY 9 PPR CALIB FRAG G/H/L/Q1 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NEAR-A-SPICE-6-CRUISE4-V1.0",
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
+            "description": "This data set includes the complete set of SPICE data for one NEAR mission phase in the form of SPICE kernels, which can be accessed using SPICE software available to read these files.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.near-a-spice-6-cruise4-v1.0_62h6-zi43",
+            "issued": "2018-06-26",
+            "keyword": [
+                "near earth asteroid rendezvous",
+                "eros"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NEAR-A-SPICE-6-CRUISE4-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.near-a-spice-6-cruise4-v1.0_62h6-zi43",
-            "description": "This data set includes the complete set of SPICE data for one NEAR mission phase in the form of SPICE kernels, which can be accessed using SPICE software available to read these files.",
-            "title": "NEAR SPICE KERNELS CRUISE4",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "NEAR SPICE KERNELS CRUISE4"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://c3.nasa.gov/dashlink/resources/479/",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2011-10-26",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
-            "keyword": [
-                "dashlink",
-                "nasa",
-                "ames"
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
-            "identifier": "DASHLINK_479",
             "description": "These grids were constructed using VGRID software from NASA Langley. The grids designed for node based (labeled 'nc') and cell-centered solvers are supplied. Grids with mixed elements (labeled 'mixed') and tetrahedral elements (labeled 'tets') are supplied.\r\n\r\nEach mixed elements tar-file contains grid in aflr3 .ugrid format and the corresponding .cgns file. Each tetrahedral elements tar-file contains grid in native VGRID format (.cogsg, .bs, .mapbc) and the corresponding .cgns file.\r\n\r\nSome files were too large and had to be split into parts. To combine the parts, use cat filename_part1 filename_part2 > filename.\r\n\r\nGrids are in units of 'inch'. Information about grids, that is number of nodes, elements, etc., is provided in AePW_BSCW_Grid_Statistics_VGRID_Final.docx\r\n\r\nPlease report any issues with these grids to Pawel.Chwalowski@nasa.gov",
-            "title": "BSCW Unstructured Grids - VGRID software FINAL",
-            "programCode": [
-                "026:029"
-            ],
             "distribution": [
                 {
-                    "mediaType": "application/x-gzip",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/bscw_coarse_tets_nc.tar_2.gz",
-                    "description": "Coarse tetrahedral node based",
                     "@type": "dcat:Distribution",
+                    "description": "Coarse tetrahedral node based",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/bscw_coarse_tets_nc.tar_2.gz",
+                    "mediaType": "application/x-gzip",
                     "title": "bscw_coarse_tets_nc.tar.gz"
                 },
                 {
-                    "mediaType": "application/x-gzip",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/bscw_coarse_mixed_nc.tar_2.gz",
-                    "description": "Coarse Mixed node based",
                     "@type": "dcat:Distribution",
+                    "description": "Coarse Mixed node based",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/bscw_coarse_mixed_nc.tar_2.gz",
+                    "mediaType": "application/x-gzip",
                     "title": "bscw_coarse_mixed_nc.tar.gz"
                 },
                 {
-                    "mediaType": "application/x-gzip",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/bscw_coarse_tets_cc.tar_2.gz",
-                    "description": "Coarse tetrahedral cell-centered",
                     "@type": "dcat:Distribution",
+                    "description": "Coarse tetrahedral cell-centered",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/bscw_coarse_tets_cc.tar_2.gz",
+                    "mediaType": "application/x-gzip",
                     "title": "bscw_coarse_tets_cc.tar.gz"
                 },
                 {
-                    "mediaType": "application/x-gzip",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/bscw_coarse_mixed_cc.tar_2.gz",
-                    "description": "Coarse Mixed cell-centered ",
                     "@type": "dcat:Distribution",
+                    "description": "Coarse Mixed cell-centered ",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/bscw_coarse_mixed_cc.tar_2.gz",
+                    "mediaType": "application/x-gzip",
                     "title": "bscw_coarse_mixed_cc.tar.gz"
                 },
                 {
-                    "mediaType": "application/x-gzip",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/bscw_medium_tets_nc.tar_2.gz",
-                    "description": "Medium tetrahedral node based",
                     "@type": "dcat:Distribution",
+                    "description": "Medium tetrahedral node based",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/bscw_medium_tets_nc.tar_2.gz",
+                    "mediaType": "application/x-gzip",
                     "title": "bscw_medium_tets_nc.tar.gz"
                 },
                 {
-                    "mediaType": "application/x-gzip",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/bscw_medium_mixed_nc.tar_2.gz",
-                    "description": "Medium Mixed node based",
                     "@type": "dcat:Distribution",
+                    "description": "Medium Mixed node based",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/bscw_medium_mixed_nc.tar_2.gz",
+                    "mediaType": "application/x-gzip",
                     "title": "bscw_medium_mixed_nc.tar.gz"
                 },
                 {
-                    "mediaType": "application/x-gzip",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/bscw_medium_tets_cc.tar_2.gz",
-                    "description": "Medium tetrahedral cell-centered",
                     "@type": "dcat:Distribution",
+                    "description": "Medium tetrahedral cell-centered",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/bscw_medium_tets_cc.tar_2.gz",
+                    "mediaType": "application/x-gzip",
                     "title": "bscw_medium_tets_cc.tar.gz"
                 },
                 {
-                    "mediaType": "application/x-gzip",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/bscw_medium_mixed_cc.tar_2.gz",
-                    "description": "Medium Mixed cell-centered",
                     "@type": "dcat:Distribution",
+                    "description": "Medium Mixed cell-centered",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/bscw_medium_mixed_cc.tar_2.gz",
+                    "mediaType": "application/x-gzip",
                     "title": "bscw_medium_mixed_cc.tar.gz"
                 },
                 {
-                    "mediaType": "application/octet-stream",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/bscw_fine_tets_nc.tar_2.gz_part1",
-                    "description": "Part1: Fine tetradedral node based",
                     "@type": "dcat:Distribution",
+                    "description": "Part1: Fine tetradedral node based",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/bscw_fine_tets_nc.tar_2.gz_part1",
+                    "mediaType": "application/octet-stream",
                     "title": "bscw_fine_tets_nc.tar.gz_part1"
                 },
                 {
-                    "mediaType": "application/octet-stream",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/bscw_fine_tets_nc.tar_2.gz_part2",
-                    "description": "Part2: Fine tetradedral node based",
                     "@type": "dcat:Distribution",
+                    "description": "Part2: Fine tetradedral node based",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/bscw_fine_tets_nc.tar_2.gz_part2",
+                    "mediaType": "application/octet-stream",
                     "title": "bscw_fine_tets_nc.tar.gz_part2"
                 },
                 {
-                    "mediaType": "application/octet-stream",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/bscw_fine_mixed_nc.tar_2.gz_part1",
-                    "description": "Part1: Fine Mixed node based",
                     "@type": "dcat:Distribution",
+                    "description": "Part1: Fine Mixed node based",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/bscw_fine_mixed_nc.tar_2.gz_part1",
+                    "mediaType": "application/octet-stream",
                     "title": "bscw_fine_mixed_nc.tar.gz_part1"
                 },
                 {
-                    "mediaType": "application/octet-stream",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/bscw_fine_mixed_nc.tar_2.gz_part2",
-                    "description": "Part2: Fine Mixed node based",
                     "@type": "dcat:Distribution",
+                    "description": "Part2: Fine Mixed node based",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/bscw_fine_mixed_nc.tar_2.gz_part2",
+                    "mediaType": "application/octet-stream",
                     "title": "bscw_fine_mixed_nc.tar.gz_part2"
                 },
                 {
-                    "mediaType": "application/x-gzip",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/bscw_fine_tets_cc.tar_2.gz",
-                    "description": "Fine tetrahedral cell-centered",
                     "@type": "dcat:Distribution",
+                    "description": "Fine tetrahedral cell-centered",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/bscw_fine_tets_cc.tar_2.gz",
+                    "mediaType": "application/x-gzip",
                     "title": "bscw_fine_tets_cc.tar.gz"
                 },
                 {
-                    "mediaType": "application/x-gzip",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/bscw_fine_mixed_cc.tar_2.gz",
-                    "description": "Fine Mixed cell-centered",
                     "@type": "dcat:Distribution",
+                    "description": "Fine Mixed cell-centered",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/bscw_fine_mixed_cc.tar_2.gz",
+                    "mediaType": "application/x-gzip",
                     "title": "bscw_fine_mixed_cc.tar.gz"
                 },
                 {
-                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.d",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/AePW_BSCW_Grid_Statistics_VGRID_Final.docx",
-                    "description": "Grid Information",
                     "@type": "dcat:Distribution",
+                    "description": "Grid Information",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/AePW_BSCW_Grid_Statistics_VGRID_Final.docx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.d",
                     "title": "AePW_BSCW_Grid_Statistics_VGRID_Final.docx"
                 }
             ],
-            "accrualPeriodicity": "irregular"
+            "identifier": "DASHLINK_479",
+            "issued": "2011-10-26",
+            "keyword": [
+                "dashlink",
+                "nasa",
+                "ames"
+            ],
+            "landingPage": "https://c3.nasa.gov/dashlink/resources/479/",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:029"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Dashlink"
+            },
+            "title": "BSCW Unstructured Grids - VGRID software FINAL"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/AQUA/MODIS/L3M/KD/2022",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/GSFC/SED/ESD/GCDC/OB.DAAC. https://doi.org/10.5067/AQUA/MODIS/L3M/KD/2022.",
-            "issued": "2019-06-23",
-            "temporal": "2002-07-04T00:00:00Z/2023-02-28T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2019-10-01",
-            "keyword": [
-                "ngda",
-                "earth science",
-                "oceans",
-                "ocean optics",
-                "national geospatial data asset"
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
-            "identifier": "C2330512183-OB_DAAC",
             "description": "MODIS (or Moderate-Resolution Imaging Spectroradiometer) is a key instrument aboard the Terra (EOS AM) and Aqua (EOS PM) satellites. Terra's orbit around the Earth is timed so that it passes from north to south across the equator in the morning, while Aqua passes south to north over the equator in the afternoon. Terra MODIS and Aqua MODIS are viewing the entire Earth's surface every 1 to 2 days, acquiring data in 36 spectral bands, or groups of wavelengths (see MODIS Technical Specifications). These data will improve our understanding of global dynamics and processes occurring on the land, in the oceans, and in the lower atmosphere. MODIS is playing a vital role in the development of validated, global, interactive Earth system models able to predict global change accurately enough to assist policy makers in making sound decisions concerning the protection of our environment.",
-            "title": "Aqua MODIS Global Mapped Diffuse Attenuation Coefficient for Downwelling Irradiance (KD) Data, version R2022.0",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAQUA%2FMODIS%2FL3M%2FKD%2F2022",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAQUA%2FMODIS%2FL3M%2FKD%2F2022",
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
-                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/data/10.5067/AQUA/MODIS/L3M/KD/2022",
-                    "description": "MODIS-Aqua L3M Diffuse Attenuation Coefficient for Downwelling Irradiance (KD) Dataset Landing Page",
                     "@type": "dcat:Distribution",
+                    "description": "MODIS-Aqua L3M Diffuse Attenuation Coefficient for Downwelling Irradiance (KD) Dataset Landing Page",
+                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/data/10.5067/AQUA/MODIS/L3M/KD/2022",
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
+            "identifier": "C2330512183-OB_DAAC",
+            "issued": "2019-06-23",
+            "keyword": [
+                "ngda",
+                "earth science",
+                "oceans",
+                "ocean optics",
+                "national geospatial data asset"
+            ],
+            "landingPage": "https://doi.org/10.5067/AQUA/MODIS/L3M/KD/2022",
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
+            "title": "Aqua MODIS Global Mapped Diffuse Attenuation Coefficient for Downwelling Irradiance (KD) Data, version R2022.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/SeaBASS/ECS/DATA001",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/GSFC/SED/ESD/GCDC/OB.DAAC. https://doi.org/10.5067/SeaBASS/ECS/DATA001.",
-            "issued": "1997-12-19",
-            "temporal": "1997-12-19T00:00:02Z/2023-04-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-04-06",
-            "keyword": [
-                "ocean chemistry",
-                "salinity/density",
-                "ocean optics",
-                "oceans",
-                "ocean temperature",
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
-            "identifier": "C1633360224-OB_DAAC",
             "description": "East China Sea (ECS) measurements spanning 1997 and 1998.",
-            "title": "East China Sea (ECS) measurements",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSeaBASS%2FECS%2FDATA001",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSeaBASS%2FECS%2FDATA001",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://seabass.gsfc.nasa.gov/experiment/ECS/",
-                    "description": "Detailed information about the SeaBASS Experiment such as cruises, funding, and investigators",
                     "@type": "dcat:Distribution",
+                    "description": "Detailed information about the SeaBASS Experiment such as cruises, funding, and investigators",
+                    "downloadURL": "https://seabass.gsfc.nasa.gov/experiment/ECS/",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 }
             ],
+            "identifier": "C1633360224-OB_DAAC",
+            "issued": "1997-12-19",
+            "keyword": [
+                "ocean chemistry",
+                "salinity/density",
+                "ocean optics",
+                "oceans",
+                "ocean temperature",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/SeaBASS/ECS/DATA001",
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
+            "temporal": "1997-12-19T00:00:02Z/2023-04-17T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "East China Sea (ECS) measurements"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-A-LORRI-2-KEM1-V3.0",
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
+            "description": "This data set contains Raw data taken by the New Horizons Long Range Reconnaissance Imager instrument during the KEM1 ENCOUNTER mission phase. This is VERSION 3.0 of this data set. This data set contains data acquired by the spacecraft between 08/14/2018 and 07/31/2019. It only includes data downlinked before 08/01/2019. Future datasets may include more data acquired by the spacecraft after 08/13/2018 but downlinked after 07/31/2019. It includes a number of distant Kuiper Belt Objects (DKBOs). It also includes images of the approach and departure field around MU69 (Arrokoth). The data also cover the actual MU69 encounter.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-a-lorri-2-kem1-v3.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "new horizons kuiper belt extended mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-A-LORRI-2-KEM1-V3.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-a-lorri-2-kem1-v3.0",
-            "description": "This data set contains Raw data taken by the New Horizons Long Range Reconnaissance Imager instrument during the KEM1 ENCOUNTER mission phase. This is VERSION 3.0 of this data set. This data set contains data acquired by the spacecraft between 08/14/2018 and 07/31/2019. It only includes data downlinked before 08/01/2019. Future datasets may include more data acquired by the spacecraft after 08/13/2018 but downlinked after 07/31/2019. It includes a number of distant Kuiper Belt Objects (DKBOs). It also includes images of the approach and departure field around MU69 (Arrokoth). The data also cover the actual MU69 encounter.",
-            "title": "NEW HORIZONS\n      LORRI KEM1\n      RAW V3.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "NEW HORIZONS\n      LORRI KEM1\n      RAW V3.0"
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
+            "description": "These images display several of Jupiter's moons approved by the International Astronomical Union (IAU).",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://planetarynames.wr.usgs.gov/images/gany_15ppi.pdf",
+                    "mediaType": "application/pdf"
+                }
+            ],
+            "identifier": "OCIO-Fitara-181",
             "issued": "1979-12-31",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
             "keyword": [
                 "thebe",
                 "io",
@@ -221887,128 +221899,118 @@
                 "amalthea",
                 "europa"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Michael Kelly",
-                "hasEmail": "mailto:Michael.S.Kelley@nasa.gov"
-            },
+            "landingPage": "http://planetarynames.wr.usgs.gov/Page/Images",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:007"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "International Astronomical Union (IAU) Working Group for Planetary System Nomenclature (WGPSN)"
             },
-            "identifier": "OCIO-Fitara-181",
-            "description": "These images display several of Jupiter's moons approved by the International Astronomical Union (IAU).",
-            "title": "Gazetteer of Planetary Nomenclature: Jovian System: Ganymede",
-            "programCode": [
-                "026:007"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://planetarynames.wr.usgs.gov/images/gany_15ppi.pdf",
-                    "mediaType": "application/pdf"
-                }
-            ],
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Space Science"
-            ]
+            ],
+            "title": "Gazetteer of Planetary Nomenclature: Jovian System: Ganymede"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/PUXL0HHMHVP8",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "VIIRS/NPP Ice Surface Temperature Daily L3 Global 750m EASE-Grid 2.0 Day V002. Version 2. Archived by National Aeronautics and Space Administration, U.S. Government, NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/PUXL0HHMHVP8.",
-            "issued": "2012-01-19",
-            "temporal": "2012-01-19T00:00:00Z/2025-01-27T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-23",
-            "keyword": [
-                "cryosphere",
-                "earth science",
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
-            "identifier": "C2317045292-NSIDC_ECS",
             "description": "This data set estimates of sea ice surface temperature (IST) derived from radiance data acquired by the Visible Infrared Imager Radiometer Suite (VIIRS). Following the approach used by MODIS, the algorithm converts VIIRS calibrated radiances into brightness temperature and computes IST using a split-window technique.\n\nVIIRS flies on board the Suomi National Polar-orbiting Partnership (NPP) satellite.",
-            "title": "VIIRS/NPP Ice Surface Temperature Daily L3 Global 750m EASE-Grid 2.0 Day V002",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FPUXL0HHMHVP8",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FPUXL0HHMHVP8",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/VIIRS/VNP30P1D.002",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/VIIRS/VNP30P1D.002",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=VNP30P1D+V002",
-                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=VNP30P1D+V002",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/data/data-access-tool/VNP30P1D/versions/2/",
-                    "description": "Search and filter data files using a map-based interface",
                     "@type": "dcat:Distribution",
+                    "description": "Search and filter data files using a map-based interface",
+                    "downloadURL": "https://nsidc.org/data/data-access-tool/VNP30P1D/versions/2/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/PUXL0HHMHVP8",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/PUXL0HHMHVP8",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/PUXL0HHMHVP8",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/PUXL0HHMHVP8",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C2317045292-NSIDC_ECS",
+            "issued": "2012-01-19",
+            "keyword": [
+                "cryosphere",
+                "earth science",
+                "sea ice"
+            ],
+            "landingPage": "https://doi.org/10.5067/PUXL0HHMHVP8",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2025-01-23",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA NSIDC DAAC"
+            },
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2012-01-19T00:00:00Z/2025-01-27T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "VIIRS/NPP Ice Surface Temperature Daily L3 Global 750m EASE-Grid 2.0 Day V002"
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
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-a-rosina-2-ast1-v1.0_62s2-rtq2",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "unknown",
                 "67p/churyumov-gerasimenko 1 (1969 r1)",
@@ -222017,39 +222019,46 @@
                 "earth",
                 "international rosetta mission"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-A-ROSINA-2-AST1-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-a-rosina-2-ast1-v1.0_62s2-rtq2",
-            "description": "This data set present engineering data of the COPS and DFMS ROSINA sensors during the Steins flyby phase. There were no RTOF measurements",
-            "title": "ROSETTA-ORBITER STEINS ROSINA 2 ENGINEERING V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER STEINS ROSINA 2 ENGINEERING V1.0"
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
+            "description": "Exp: FAITH Hill 3-D Separated Flow. This web page provides data from experiments that may be useful for the validation of turbulence models. This resource is expected to grow gradually over time. All data herein arepublicly available.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://turbmodels.larc.nasa.gov/Other_exp_Data/FAITH_Hill/PSP_data.tar.gz",
+                    "mediaType": "application/x-gzip"
+                }
             ],
+            "identifier": "NASA-853__3",
+            "issued": "2018-06-25",
             "keyword": [
                 "separation",
                 "models",
@@ -222060,620 +222069,625 @@
                 "faith",
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
-            "identifier": "NASA-853__3",
-            "description": "Exp: FAITH Hill 3-D Separated Flow. This web page provides data from experiments that may be useful for the validation of turbulence models. This resource is expected to grow gradually over time. All data herein arepublicly available.",
-            "title": "Turbulence Models: Data from Other Experiments: FAITH Hill 3-D Separated Flow",
-            "programCode": [
-                "026:023"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://turbmodels.larc.nasa.gov/Other_exp_Data/FAITH_Hill/PSP_data.tar.gz",
-                    "mediaType": "application/x-gzip"
-                }
+            "references": [
+                "http://turbmodels.larc.nasa.gov/index.html"
             ],
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Aerospace"
-            ]
+            ],
+            "title": "Turbulence Models: Data from Other Experiments: FAITH Hill 3-D Separated Flow"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-E-NAVCAM-2-EAR1-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This dataset contains RAW DATA of the EARTH 1 Swingby Phase from 4 March 2005 until 5 March 2005. The closest approach (CA) took place on 4 March 2005",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-e-navcam-2-ear1-v1.0_62vx-f5ah",
             "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "earth",
                 "moon",
                 "international rosetta mission"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-E-NAVCAM-2-EAR1-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-e-navcam-2-ear1-v1.0_62vx-f5ah",
-            "description": "This dataset contains RAW DATA of the EARTH 1 Swingby Phase from 4 March 2005 until 5 March 2005. The closest approach (CA) took place on 4 March 2005",
-            "title": "ROSETTA-ORBITER-EARTH-NAVCAM-2-EAR1-V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "ROSETTA-ORBITER-EARTH-NAVCAM-2-EAR1-V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://c3.nasa.gov/dashlink/resources/829/",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2013-07-29",
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
-            "identifier": "DASHLINK_829",
             "description": "Prognostics and Health Management (PHM) principles have considerable promise to change the game of lifecycle cost of engineering systems at high safety levels by providing a reliable estimate of future system states. This estimate is a key for planning and decision making in an operational setting. While technology solutions have made considerable advances, the tie-in into the systems engineering process is lagging behind, which delays fielding of PHM-enabled systems. The derivation of specifications from high level requirements for algorithm performance to ensure quality predictions is not well developed. From an engineering perspective some key parameters driving the requirements for prognostics performance include: (1) maximum allowable Probability of Failure (PoF) of the prognostic system to bound the risk of losing an asset, (2) tolerable limits on proactive maintenance to minimize missed opportunity of asset usage, (3) lead time to specify the amount of advanced warning needed for actionable decisions, and (4) required confidence to specify when prognosis is sufficiently good to be used. This paper takes a systems engineering view towards the requirements specification process and presents a method for the flowdown process. A case study based on an electric Unmanned Aerial Vehicle (e-UAV) scenario demonstrates how top level requirements for performance, cost, and safety flow down to the health management level and specify quantitative requirements for prognostic algorithm performance.",
-            "title": "Requirements Flowdown for Prognostics and Health Management",
-            "programCode": [
-                "026:029"
-            ],
             "distribution": [
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/publication/2012_AIAA_Requirements_2.pdf",
-                    "description": "2012_AIAA_Requirements.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "2012_AIAA_Requirements.pdf",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/publication/2012_AIAA_Requirements_2.pdf",
+                    "mediaType": "application/pdf",
                     "title": "2012_AIAA_Requirements.pdf"
                 }
             ],
-            "accrualPeriodicity": "irregular"
+            "identifier": "DASHLINK_829",
+            "issued": "2013-07-29",
+            "keyword": [
+                "nasa",
+                "dashlink",
+                "ames"
+            ],
+            "landingPage": "https://c3.nasa.gov/dashlink/resources/829/",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:029"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Dashlink"
+            },
+            "title": "Requirements Flowdown for Prognostics and Health Management"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-C-CCD-3-EDR-HALLEY-OUTBURST-ESO-V1.0",
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
-                "halley"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "Charged Coupled Device (CCD) cameras from ESO were used by groups to observe the outburst of comet Halley using a variety of telescopes and chip sets.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-c-ccd-3-edr-halley-outburst-eso-v1.0_633c-i9z4",
+            "issued": "2018-06-26",
+            "keyword": [
+                "support archives",
+                "halley"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-C-CCD-3-EDR-HALLEY-OUTBURST-ESO-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-c-ccd-3-edr-halley-outburst-eso-v1.0_633c-i9z4",
-            "description": "Charged Coupled Device (CCD) cameras from ESO were used by groups to observe the outburst of comet Halley using a variety of telescopes and chip sets.",
-            "title": "CCD OBSERVATIONS V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "CCD OBSERVATIONS V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/AURA/TES/TESH2OL_L2.006",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "The data used in this study were produced by the TES Science Team at the TES SIPS and archived at the Langley DAAC. See ProductionDateTime for Published date.",
-            "issued": "2013-03-29",
-            "temporal": "2004-07-15T00:00:00Z/2022-01-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2015-10-28",
-            "keyword": [
-                "earth science",
-                "atmospheric water vapor",
-                "atmosphere",
-                "atmospheric temperature"
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
-            "identifier": "C191856311-LARC",
             "description": "Atmospheric vertical profile estimates and associated errors (diagonals and covariance matrices), along with retrieved surface temperature, cloud effective optical depth, column estimates, quality flags, averaging kernels and a priori constraint vectors.",
-            "title": "TES/Aura L2 H2O Limb V006",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAURA%2FTES%2FTESH2OL_L2.006",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAURA%2FTES%2FTESH2OL_L2.006",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 }
             ],
+            "identifier": "C191856311-LARC",
+            "issued": "2013-03-29",
+            "keyword": [
+                "earth science",
+                "atmospheric water vapor",
+                "atmosphere",
+                "atmospheric temperature"
+            ],
+            "landingPage": "https://doi.org/10.5067/AURA/TES/TESH2OL_L2.006",
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
+            "title": "TES/Aura L2 H2O Limb V006"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ASDC_DAAC/AIRMISR_CLAMS_2001_1",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2002-08-01. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/ASDC_DAAC/AIRMISR_CLAMS_2001_1.",
-            "issued": "2004-03-24",
-            "temporal": "2001-07-12T00:00:00Z/2001-08-02T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2018-04-26",
-            "keyword": [
-                "infrared wavelengths",
-                "visible wavelengths",
-                "earth science",
-                "spectral/engineering"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "CAROL BRUEGGE",
                 "hasEmail": "mailto:carol.j.bruegge@jpl.nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/LARC/SD/ASDC"
-            },
-            "identifier": "C1000000702-LARC_ASDC",
             "description": "The AIRMISR_CLAMS_2001 data were acquired during the CLAMS campaign on July 12, July 17, August 1, and August 2 of 2001. The Jet Propulsion Laboratory (JPL) in Pasadena, California provided the data. The Chesapeake Lighthouse and Aircraft Measurements for Satellites (CLAMS) field campaign was held in the summer of 2001 at the CERES Ocean Validation Experiment (COVE) site in the Chesapeake Bay, 20 km east of Virginia Beach. CLAMS is a clear-sky, shortwave closure campaign in conjunction with MISR, CERES, MODIS-Atmospheres and the Global Aerosol Climatology Project (GACP). Its goals were to obtain more accurate broadband fluxes at sea surface and within the atmosphere, space-time variability of spectral BRDF of the sea surface, and aerosol retrievals. The Airborne Multi-angle Imaging SpectroRadiometer (AirMISR) is an airborne instrument for obtaining multi-angle imagery similar to that of the satellite-borne Multi-angle Imaging SpectroRadiometer (MISR) instrument, which is designed to contribute to studies of the Earth's ecology and climate. AirMISR flies on the NASA ER-2 aircraft. The Jet Propulsion Laboratory in Pasadena, California built the instrument for NASA. Unlike the satellite-borne MISR instrument, which has nine cameras oriented at various angles, AirMISR uses a single camera in a pivoting gimbal mount. A data run by the ER-2 aircraft is divided into nine segments, each with the camera positioned to a MISR look angle. The gimbal rotates between successive segments, such that each segment acquires data over the same area on the ground as the previous segment. This process is repeated until all nine angles of the target area are collected. The swath width, which varies from 11 km in the nadir to 32 km at the most oblique angle, is governed by the camera's instantaneous field-of-view of 7 meters cross-track x 6 meters along-track in the nadir view and 21 meters x 55 meters at the most oblique angle. The along-track image length at each angle is dictated by the timing required to obtain overlap imagery at all angles, and varies from about 9 km in the nadir to 26 km at the most oblique angle. Thus, the nadir image dictates the area of overlap that is obtained from all nine angles. A complete flight run takes approximately 13 minutes. The 9 camera viewing angles are: 0 degrees or nadir 26.1 degrees, fore and aft 45.6 degrees, fore and aft 60.0 degrees, fore and aft 70.5 degrees, fore and aft. For each of the camera angles, images are obtained at 4 spectral bands. The spectral bands can be used to identify vegetation and aerosols, estimate surface reflectance and ocean color studies. The center wavelengths of the 4 spectral bands are: 443 nanometers, blue 555 nanometers, green 670 nanometers, red 865 nanometers, near-infrared two types of AirMISR data products are available - the Level 1 Radiometric product (L1B1) and the Level 1 Georectified radiance product (L1B2).",
-            "graphic-preview-description": "AirMISR Campaign Imagery: AirMISR Red Band Browse Images from the CLAMS_2001 Field Campaign July 12, 2001",
-            "title": "Airborne Multi-angle Imaging SpectroRadiometer (AirMISR) Data from the CLAMS 2001 Campaign",
-            "graphic-preview-file": "https://asdc.larc.nasa.gov/documents/airmisr/airmisr_CLAMS_images.html",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC_DAAC%2FAIRMISR_CLAMS_2001_1",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC_DAAC%2FAIRMISR_CLAMS_2001_1",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/project/AIRMISR",
-                    "description": "ASDC Data and Information for AirMISR",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Data and Information for AirMISR",
+                    "downloadURL": "https://asdc.larc.nasa.gov/project/AIRMISR",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://misr.jpl.nasa.gov/Mission/airMISR/",
-                    "description": "AirMISR project home page",
                     "@type": "dcat:Distribution",
+                    "description": "AirMISR project home page",
+                    "downloadURL": "https://misr.jpl.nasa.gov/Mission/airMISR/",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/project/CLAMS",
-                    "description": "ASDC Data and Information for CLAMS",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Data and Information for CLAMS",
+                    "downloadURL": "https://asdc.larc.nasa.gov/project/CLAMS",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1000000702-LARC_ASDC",
-                    "description": "Earthdata Search for AIRMISR_CLAMS_2001_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for AIRMISR_CLAMS_2001_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1000000702-LARC_ASDC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/airmisr/airmisr_read_software.pdf",
-                    "description": "AirMISR Read Software Document Readme",
                     "@type": "dcat:Distribution",
+                    "description": "AirMISR Read Software Document Readme",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/airmisr/airmisr_read_software.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's read me document"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/airmisr/readme/readme_airmisr_clams_2001",
-                    "description": "Readme Information about the AirMISR Data During a Flight overChesapeake Lighthouse & Aircraft Measurements for Satellites (CLAMS) site on July 12, 2001",
                     "@type": "dcat:Distribution",
+                    "description": "Readme Information about the AirMISR Data During a Flight overChesapeake Lighthouse & Aircraft Measurements for Satellites (CLAMS) site on July 12, 2001",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/airmisr/readme/readme_airmisr_clams_2001",
+                    "mediaType": "text/html",
                     "title": "View this dataset's read me document"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/airmisr/read_software/read_airmisr.pro",
-                    "description": "Readme to open and read AIRMISR L1B2 GP (Georectified Radiance Product) HDF-EOS data files",
                     "@type": "dcat:Distribution",
+                    "description": "Readme to open and read AIRMISR L1B2 GP (Georectified Radiance Product) HDF-EOS data files",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/airmisr/read_software/read_airmisr.pro",
+                    "mediaType": "text/html",
                     "title": "View this dataset's how-to documentation"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www-angler.larc.nasa.gov/clams/er2.shtml",
-                    "description": "CLAMS ER-2 Flight Track Overlay by Flight Day",
                     "@type": "dcat:Distribution",
+                    "description": "CLAMS ER-2 Flight Track Overlay by Flight Day",
+                    "downloadURL": "https://www-angler.larc.nasa.gov/clams/er2.shtml",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/ASDC_DAAC/AIRMISR_CLAMS_2001_1",
-                    "description": "DOI data set landing page for AIRMISR_CLAMS_2001_1",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for AIRMISR_CLAMS_2001_1",
+                    "downloadURL": "https://doi.org/10.5067/ASDC_DAAC/AIRMISR_CLAMS_2001_1",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/airmisr/readme/AirMISR_DPS_F01.pdf",
-                    "description": "AirMISR Data Products Specifications, December 21, 2000",
                     "@type": "dcat:Distribution",
+                    "description": "AirMISR Data Products Specifications, December 21, 2000",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/airmisr/readme/AirMISR_DPS_F01.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's product usage"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/airmisr/readme/AirMISR_DPS.pdf",
-                    "description": "AirMISR Data Products Specifications, Rev. A, December 21,2000",
                     "@type": "dcat:Distribution",
+                    "description": "AirMISR Data Products Specifications, Rev. A, December 21,2000",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/airmisr/readme/AirMISR_DPS.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's product usage"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/airmisr/readme/AirMISR_DPS_RevC.pdf",
-                    "description": "AirMISR Data Products Specifications, Rev. C, December 21,2000",
                     "@type": "dcat:Distribution",
+                    "description": "AirMISR Data Products Specifications, Rev. C, December 21,2000",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/airmisr/readme/AirMISR_DPS_RevC.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's product usage"
                 },
                 {
-                    "mediaType": "application/x-tar",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/airmisr/tools/coregister_L1B2_L2AS.tar",
-                    "description": "AirMISR L1B2/L2AS Coregistration Tool - Direct File Download (.tar)",
                     "@type": "dcat:Distribution",
+                    "description": "AirMISR L1B2/L2AS Coregistration Tool - Direct File Download (.tar)",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/airmisr/tools/coregister_L1B2_L2AS.tar",
+                    "mediaType": "application/x-tar",
                     "title": "Downloadable software applications"
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
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/airmisr/using_airmisr_data.pdf",
-                    "description": "ASDC Documents for Using AirMISR Data",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Documents for Using AirMISR Data",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/airmisr/using_airmisr_data.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's how-to documentation"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/misr/DPS_v50_RevS.pdf",
-                    "description": "Data Product Specification for MISR - Revision S, April 15, 2011   ",
                     "@type": "dcat:Distribution",
+                    "description": "Data Product Specification for MISR - Revision S, April 15, 2011   ",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/misr/DPS_v50_RevS.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's product usage"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://earthobservatory.nasa.gov/features/FieryTemperament",
-                    "description": "NASA Earth ObservatoryArticle: \"Fiery Temperament\" By Michon Scott, May 14, 2002",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Earth ObservatoryArticle: \"Fiery Temperament\" By Michon Scott, May 14, 2002",
+                    "downloadURL": "https://earthobservatory.nasa.gov/features/FieryTemperament",
+                    "mediaType": "text/html",
                     "title": "View a micro article on this dataset"
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
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/airmisr/readme/MultiangleAerosolMonterey.pdf",
-                    "description": "Journal of Geophysical Research Article: \"Aerosol properties derived from aircraft multiangle imagingover Monterey Bay\" by Ralph Kahn, Pranab Banerjee, Duncan McDonald, and John Martonchik, June 16, 2001",
                     "@type": "dcat:Distribution",
+                    "description": "Journal of Geophysical Research Article: \"Aerosol properties derived from aircraft multiangle imagingover Monterey Bay\" by Ralph Kahn, Pranab Banerjee, Duncan McDonald, and John Martonchik, June 16, 2001",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/airmisr/readme/MultiangleAerosolMonterey.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/airmisr/readme/MultiangleAerosolRetrieval.pdf",
-                    "description": "Journal of Geophysical Research Article: \"Sensitivity of multiangle imaging to natural mixturesof aerosols over ocean\" by Ralph Kahn, Pranab Banerjee, and Duncan McDonald, August 27, 2001",
                     "@type": "dcat:Distribution",
+                    "description": "Journal of Geophysical Research Article: \"Sensitivity of multiangle imaging to natural mixturesof aerosols over ocean\" by Ralph Kahn, Pranab Banerjee, and Duncan McDonald, August 27, 2001",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/airmisr/readme/MultiangleAerosolRetrieval.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's publications"
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
-                    "downloadURL": "https://misr.jpl.nasa.gov/",
-                    "description": "MISR project home page",
                     "@type": "dcat:Distribution",
+                    "description": "MISR project home page",
+                    "downloadURL": "https://misr.jpl.nasa.gov/",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
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
-                    "downloadURL": "https://www.fs.usda.gov/rmrs/groups/larse",
-                    "description": "USDA Overview of Laboratory for Applications of Remote Sensing in Ecology (LARSE)",
                     "@type": "dcat:Distribution",
+                    "description": "USDA Overview of Laboratory for Applications of Remote Sensing in Ecology (LARSE)",
+                    "downloadURL": "https://www.fs.usda.gov/rmrs/groups/larse",
+                    "mediaType": "text/html",
                     "title": "The dataset's home page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/airmisr/tools/coregister_L1B2_L2AS.pro",
-                    "description": "AirMISR L1B2/L2AS Coregistration Tool IDL source code - Direct File Download (.pro)",
                     "@type": "dcat:Distribution",
+                    "description": "AirMISR L1B2/L2AS Coregistration Tool IDL source code - Direct File Download (.pro)",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/airmisr/tools/coregister_L1B2_L2AS.pro",
+                    "mediaType": "text/html",
                     "title": "Downloadable software applications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/airmisr/tools/coregister_L1B2_L2AS.sav",
-                    "description": "AirMISR L1B2/L2AS Coregistration Tool  IDL executable save file (use with the IDL Virtual Machine) - Direct File Download (.sav)",
                     "@type": "dcat:Distribution",
+                    "description": "AirMISR L1B2/L2AS Coregistration Tool  IDL executable save file (use with the IDL Virtual Machine) - Direct File Download (.sav)",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/airmisr/tools/coregister_L1B2_L2AS.sav",
+                    "mediaType": "text/html",
                     "title": "Downloadable software applications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/airmisr/tools/readme_L1B2_L2AS_coregistration_tool.txt",
-                    "description": "AirMISR L1B2/L2AS Coregistration Tool Readme",
                     "@type": "dcat:Distribution",
+                    "description": "AirMISR L1B2/L2AS Coregistration Tool Readme",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/airmisr/tools/readme_L1B2_L2AS_coregistration_tool.txt",
+                    "mediaType": "text/html",
                     "title": "View this dataset's read me document"
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
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/airmisr/airmisr_CLAMS_images.html",
-                    "description": "AirMISR Campaign Imagery: AirMISR Red Band Browse Images from the CLAMS_2001 Field Campaign July 12, 2001",
                     "@type": "dcat:Distribution",
+                    "description": "AirMISR Campaign Imagery: AirMISR Red Band Browse Images from the CLAMS_2001 Field Campaign July 12, 2001",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/airmisr/airmisr_CLAMS_images.html",
+                    "mediaType": "text/html",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/AirMISR/AIRMISR_CLAMS_2001/",
-                    "description": "ASDC Direct Data Download for AIRMISR_CLAMS_2001_1",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for AIRMISR_CLAMS_2001_1",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/AirMISR/AIRMISR_CLAMS_2001/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/AirMISR/AIRMISR_CLAMS_2001/contents.html",
-                    "description": "OPeNDAP data access for AIRMISR_CLAMS_2001_1",
                     "@type": "dcat:Distribution",
+                    "description": "OPeNDAP data access for AIRMISR_CLAMS_2001_1",
+                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/AirMISR/AIRMISR_CLAMS_2001/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 }
             ],
+            "graphic-preview-description": "AirMISR Campaign Imagery: AirMISR Red Band Browse Images from the CLAMS_2001 Field Campaign July 12, 2001",
+            "graphic-preview-file": "https://asdc.larc.nasa.gov/documents/airmisr/airmisr_CLAMS_images.html",
+            "identifier": "C1000000702-LARC_ASDC",
+            "issued": "2004-03-24",
+            "keyword": [
+                "infrared wavelengths",
+                "visible wavelengths",
+                "earth science",
+                "spectral/engineering"
+            ],
+            "landingPage": "https://doi.org/10.5067/ASDC_DAAC/AIRMISR_CLAMS_2001_1",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2018-04-26",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/LARC/SD/ASDC"
+            },
             "spatial": "<?xml version=\"1.0\" encoding=\"UTF-8\"?><gml:Polygon xmlns:gml=\"http://www.opengis.net/gml/3.2\" srsName=\"EPSG:4326\"><gml:outerBoundaryIs><gml:LinearRing><gml:posList>35.64 -78.82 35.64 -74.01 39.99 -74.01 39.99 -78.82 35.64 -78.82</gml:posList></gml:LinearRing></gml:outerBoundaryIs><gml:innerBoundaryIs></gml:innerBoundaryIs></gml:Polygon>",
+            "temporal": "2001-07-12T00:00:00Z/2001-08-02T23:59:59.999Z",
             "theme": [
                 "AIRMISR",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Airborne Multi-angle Imaging SpectroRadiometer (AirMISR) Data from the CLAMS 2001 Campaign"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.nasa.gov/d/63bx-knk2",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "GeneLab Outreach",
+                "hasEmail": "mailto:genelab-outreach@lists.nasa.gov"
+            },
+            "description": "The present study concerns the effects of 21 days of sustained recumbence (bedrest) and hypoxia alone and in combination on skeletal muscle microRNA expression. 14 male subjects participated in 3 experimental campaigns in a counterbalanced fashion: normoxic bedrest (NBR) hypoxic bedrest (HBR) and hypoxic ambulatory confinement (HAMB) both hypoxic conditions with FO2 = 0.141 and PIO2 = 90  xc2 xb1 0.4 mmHg equivalent to an altitude of  xe2 x89 x88 4000 m). Each intervention (bedrest or ambulatory confinement) lasted 21 days and the interventions were separated by a 4-month wash-out/recovery period. The order in which each subject undertook the interventions is denoted   Intervention_order   Throughout both bedrest interventions each subject remained in a horizontal position at all times. He was allowed one pillow for the head and to occasionally lean on an elbow while eating or being transferred to a gurney. Muscular exercise was prohibited. During the HAMB confinement each subject was allowed to move freely within the hypoxic area. To mimic a normal level of physical activity subjects performed 30 minutes of low-to-moderate-intensity exercise twice daily. Muscle samples from Vastus lateralis.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "GeneLab Study Page",
+                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-198",
+                    "mediaType": "text/html",
+                    "title": "Effects of bedrest and hypoxia on human skeletal muscle miRNA expression"
+                }
+            ],
+            "identifier": "nasa_genelab_GLDS-198_63bx-knk2",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
             "keyword": [
                 "treatment",
                 "treatment protocol",
@@ -222688,206 +222702,194 @@
                 "bed rest",
                 "experimental campaign"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "GeneLab Outreach",
-                "hasEmail": "mailto:genelab-outreach@lists.nasa.gov"
-            },
+            "landingPage": "https://data.nasa.gov/d/63bx-knk2",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "nasa_genelab_GLDS-198_63bx-knk2",
-            "description": "The present study concerns the effects of 21 days of sustained recumbence (bedrest) and hypoxia alone and in combination on skeletal muscle microRNA expression. 14 male subjects participated in 3 experimental campaigns in a counterbalanced fashion: normoxic bedrest (NBR) hypoxic bedrest (HBR) and hypoxic ambulatory confinement (HAMB) both hypoxic conditions with FO2 = 0.141 and PIO2 = 90  xc2 xb1 0.4 mmHg equivalent to an altitude of  xe2 x89 x88 4000 m). Each intervention (bedrest or ambulatory confinement) lasted 21 days and the interventions were separated by a 4-month wash-out/recovery period. The order in which each subject undertook the interventions is denoted   Intervention_order   Throughout both bedrest interventions each subject remained in a horizontal position at all times. He was allowed one pillow for the head and to occasionally lean on an elbow while eating or being transferred to a gurney. Muscular exercise was prohibited. During the HAMB confinement each subject was allowed to move freely within the hypoxic area. To mimic a normal level of physical activity subjects performed 30 minutes of low-to-moderate-intensity exercise twice daily. Muscle samples from Vastus lateralis.",
-            "title": "Effects of bedrest and hypoxia on human skeletal muscle miRNA expression",
-            "programCode": [
-                "026:005"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-198",
-                    "description": "GeneLab Study Page",
-                    "@type": "dcat:Distribution",
-                    "title": "Effects of bedrest and hypoxia on human skeletal muscle miRNA expression"
-                }
-            ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "Effects of bedrest and hypoxia on human skeletal muscle miRNA expression"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-2-PRL-67PCHURYUMOV-M02-V1.1",
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
+            "description": "This data set contains raw EDR images acquired by the OSIRIS Narrow Angle\nCamera during the prelanding phase of the Rosetta mission at the comet 67P,\ncovering the period from 2014-04-06 to 2014-05-07.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-2-prl-67pchuryumov-m02-v1.1_63dg-jays",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-2-PRL-67PCHURYUMOV-M02-V1.1",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-2-prl-67pchuryumov-m02-v1.1_63dg-jays",
-            "description": "This data set contains raw EDR images acquired by the OSIRIS Narrow Angle\nCamera during the prelanding phase of the Rosetta mission at the comet 67P,\ncovering the period from 2014-04-06 to 2014-05-07.",
-            "title": "ROSETTA-ORBITER COMET PRELANDING OSINAC 2 EDR DATA MTP 002",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER COMET PRELANDING OSINAC 2 EDR DATA MTP 002"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-PRL-0374-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the PRELANDING phase 2014-01-21 to 2014-11-18. It is a Global Gravity measurement at the comet 67P and covers the time 2014-10-21T04:17:05.000 to 2014-10-21T14:51:46.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-prl-0374-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-PRL-0374-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-prl-0374-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the PRELANDING phase 2014-01-21 to 2014-11-18. It is a Global Gravity measurement at the comet 67P and covers the time 2014-10-21T04:17:05.000 to 2014-10-21T14:51:46.000.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     PRELANDING 0374 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     PRELANDING 0374 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-A-REX-2-KEM1-V2.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This data set contains Raw data taken by the New Horizons Radio Science Experiment instrument during the KEM1 ENCOUNTER mission phase. This is VERSION 2.0 of this data set. This data set contains data acquired by the spacecraft between 08/14/2018 and 07/31/2019. It only includes data downlinked before 08/01/2019. Future datasets may include more data acquired by the spacecraft after 08/13/2018 but downlinked after 07/31/2019. The REX datasets over the mission include calibrations using known radio sources, Jupiter, and cold sky measurements; operational readiness tests (ORTs); internal test pattern calibration; and prime science radiometry and occultation observations during the Arrokoth Encounter.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-a-rex-2-kem1-v2.0",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2021-05-21",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "new horizons kuiper belt extended mission"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-A-REX-2-KEM1-V2.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-a-rex-2-kem1-v2.0",
-            "description": "This data set contains Raw data taken by the New Horizons Radio Science Experiment instrument during the KEM1 ENCOUNTER mission phase. This is VERSION 2.0 of this data set. This data set contains data acquired by the spacecraft between 08/14/2018 and 07/31/2019. It only includes data downlinked before 08/01/2019. Future datasets may include more data acquired by the spacecraft after 08/13/2018 but downlinked after 07/31/2019. The REX datasets over the mission include calibrations using known radio sources, Jupiter, and cold sky measurements; operational readiness tests (ORTs); internal test pattern calibration; and prime science radiometry and occultation observations during the Arrokoth Encounter.",
-            "title": "NEW HORIZONS\n      REX KEM1\n      RAW V2.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "NEW HORIZONS\n      REX KEM1\n      RAW V2.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/Terra/MISR/MI3QCLDN_L3.002",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "The data used in this study were produced by the MISR Science Team;processed/stored at the Langley DAAC;Product is the MISR Level 3 Global Cloud public Product in netCDF format covering a quarter;See ProductionDateTime for Published date.",
-            "issued": "2006-03-01",
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
-            "identifier": "C108919910-LARC",
             "description": "This file contains the MISR Level 3 Global Cloud public Product in netCDF format covering a quarter (seasonal)",
-            "graphic-preview-description": "ASDC List of MISR Imagery and Articles",
-            "title": "MISR Level 3 Global Cloud public Product in netCDF format covering a quarter V002",
-            "graphic-preview-file": "https://asdc.larc.nasa.gov/documents/misr/imagery.html",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FTerra%2FMISR%2FMI3QCLDN_L3.002",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FTerra%2FMISR%2FMI3QCLDN_L3.002",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 }
             ],
+            "graphic-preview-description": "ASDC List of MISR Imagery and Articles",
+            "graphic-preview-file": "https://asdc.larc.nasa.gov/documents/misr/imagery.html",
+            "identifier": "C108919910-LARC",
+            "issued": "2006-03-01",
+            "keyword": [
+                "nasa"
+            ],
+            "landingPage": "https://doi.org/10.5067/Terra/MISR/MI3QCLDN_L3.002",
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
+            "title": "MISR Level 3 Global Cloud public Product in netCDF format covering a quarter V002"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-C-I0065-2-IMGBORRELLYKPNO-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "The data set consists of ground-based images of comet 19P/Borrelly in the R filter taken at the Kitt Peak 2.1m for three nights from September 21-23, 2001, bracketing the Deep Space 1 encounter. Raw, as well as reduced images are included.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-c-i0065-2-imgborrellykpno-v1.0_63ta-854t",
             "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "support archives",
                 "19p/borrelly 1 (1904 y2)",
@@ -222895,710 +222897,688 @@
                 "pg 0231+051",
                 "pg 2213-006"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-C-I0065-2-IMGBORRELLYKPNO-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-c-i0065-2-imgborrellykpno-v1.0_63ta-854t",
-            "description": "The data set consists of ground-based images of comet 19P/Borrelly in the R filter taken at the Kitt Peak 2.1m for three nights from September 21-23, 2001, bracketing the Deep Space 1 encounter. Raw, as well as reduced images are included.",
-            "title": "IMAGES OF COMET 19P/BORRELLY FROM 9/21-23, 2001 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "IMAGES OF COMET 19P/BORRELLY FROM 9/21-23, 2001 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/IA5WAX7K3YGY",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "ABoVE LVIS L2 Geolocated Surface Elevation Product V001. Version 1. Archived by National Aeronautics and Space Administration, U.S. Government, NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/IA5WAX7K3YGY.",
-            "issued": "2017-06-29",
-            "temporal": "2017-06-29T00:00:00Z/2017-07-17T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2017-07-17",
-            "keyword": [
-                "topography",
-                "land surface",
-                "earth science"
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
-            "identifier": "C1513105984-NSIDC_ECS",
             "description": "This data set contains surface elevation data over Alaska and Western Canada measured by the NASA Land, Vegetation, and Ice Sensor (LVIS), an airborne lidar scanning laser altimeter. The data were collected as part of NASA's Terrestrial Ecology Program campaign, the Arctic-Boreal Vulnerability Experiment (ABoVE).",
-            "title": "ABoVE LVIS L2 Geolocated Surface Elevation Product V001",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FIA5WAX7K3YGY",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FIA5WAX7K3YGY",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/ICEBRIDGE/ABLVIS2.001/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/ICEBRIDGE/ABLVIS2.001/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1513105984-NSIDC_ECS&m=46.72265625%21-112.5703125%213%211%210%210%2C2&tl=1513803658%214%21%21&q=ABLVIS2",
-                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1513105984-NSIDC_ECS&m=46.72265625%21-112.5703125%213%211%210%210%2C2&tl=1513803658%214%21%21&q=ABLVIS2",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/icebridge/portal/map",
-                    "description": "Tool to visualize, search, and download IceBridge data.",
                     "@type": "dcat:Distribution",
+                    "description": "Tool to visualize, search, and download IceBridge data.",
+                    "downloadURL": "https://nsidc.org/icebridge/portal/map",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/data/data-access-tool/ABLVIS2/versions/1/",
-                    "description": "Data Access link for ITSD project",
                     "@type": "dcat:Distribution",
+                    "description": "Data Access link for ITSD project",
+                    "downloadURL": "https://nsidc.org/data/data-access-tool/ABLVIS2/versions/1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/IA5WAX7K3YGY",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/IA5WAX7K3YGY",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/IA5WAX7K3YGY",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/IA5WAX7K3YGY",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C1513105984-NSIDC_ECS",
+            "issued": "2017-06-29",
+            "keyword": [
+                "topography",
+                "land surface",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/IA5WAX7K3YGY",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2017-07-17",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA NSIDC DAAC"
+            },
             "spatial": "-158.0 48.0 -104.0 72.0",
+            "temporal": "2017-06-29T00:00:00Z/2017-07-17T23:59:59.999Z",
             "theme": [
                 "ABoVE",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "ABoVE LVIS L2 Geolocated Surface Elevation Product V001"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/08X5YUIZERS9",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "SMEX04 Airborne Visible/Infrared Imaging Spectrometer (AVIRIS) Data: Arizona, Version 1. Version 1. Archived by National Aeronautics and Space Administration, U.S. Government, NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/08X5YUIZERS9.",
-            "issued": "2004-08-25",
-            "temporal": "2004-08-25T00:00:00Z/2004-08-25T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2004-08-25",
-            "keyword": [
-                "spectral/engineering",
-                "infrared wavelengths",
-                "earth science",
-                "biosphere",
-                "land surface",
-                "visible wavelengths",
-                "vegetation",
-                "surface radiative properties"
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
-            "identifier": "C1386205104-NSIDCV0",
             "description": "Notice to Data Users: The documentation for this data set was provided solely by the Principal Investigator(s) and was not further developed, thoroughly reviewed, or edited by NSIDC. Thus, support for this data set may be limited.\n\nThis data set contains surface reflectance measurements acquired over the Soil Moisture Experiment 2004 (SMEX04) regional study area in Arizona, USA.",
-            "title": "SMEX04 Airborne Visible/Infrared Imaging Spectrometer (AVIRIS) Data: Arizona, Version 1",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2F08X5YUIZERS9",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2F08X5YUIZERS9",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/AVDM/data/soil_moisture/SMEX04/Arizona/aircraft/AVIRIS/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/AVDM/data/soil_moisture/SMEX04/Arizona/aircraft/AVIRIS/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/AVDM/data/soil_moisture/SMEX04/Arizona/aircraft/AVIRIS/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/AVDM/data/soil_moisture/SMEX04/Arizona/aircraft/AVIRIS/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/AVDM/data/soil_moisture/SMEX04/Arizona/aircraft/AVIRIS/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/AVDM/data/soil_moisture/SMEX04/Arizona/aircraft/AVIRIS/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/AVDM/data/soil_moisture/SMEX04/Arizona/aircraft/AVIRIS/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/AVDM/data/soil_moisture/SMEX04/Arizona/aircraft/AVIRIS/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/08X5YUIZERS9",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/08X5YUIZERS9",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/08X5YUIZERS9",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/08X5YUIZERS9",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C1386205104-NSIDCV0",
+            "issued": "2004-08-25",
+            "keyword": [
+                "spectral/engineering",
+                "infrared wavelengths",
+                "earth science",
+                "biosphere",
+                "land surface",
+                "visible wavelengths",
+                "vegetation",
+                "surface radiative properties"
+            ],
+            "landingPage": "https://doi.org/10.5067/08X5YUIZERS9",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2004-08-25",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA NSIDC DAAC"
+            },
             "spatial": "-111.42 29.36 -108.63 32.69",
+            "temporal": "2004-08-25T00:00:00Z/2004-08-25T23:59:59.999Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "SMEX04 Airborne Visible/Infrared Imaging Spectrometer (AVIRIS) Data: Arizona, Version 1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/1WJ3UHP5YT3L",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "SMEX03 ALMNet and SCAN Soil Moisture Data: Alabama, Version 1. Version 1. Archived by National Aeronautics and Space Administration, U.S. Government, NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/1WJ3UHP5YT3L.",
-            "issued": "2003-06-01",
-            "temporal": "2003-06-01T00:00:00Z/2003-07-15T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2003-07-15",
-            "keyword": [
-                "soils",
-                "agriculture",
-                "atmosphere",
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
-            "identifier": "C1386205053-NSIDCV0",
             "description": "Notice to Data Users: The documentation for this data set was provided solely by the Principal Investigator(s) and was not further developed, thoroughly reviewed, or edited by NSIDC. Thus, support for this data set may be limited.\n\nThis data set includes soil moisture data collected at crop, pasture, and forested sites located within the Alabama MesoNet (ALMNet) network.",
-            "title": "SMEX03 ALMNet and SCAN Soil Moisture Data: Alabama, Version 1",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2F1WJ3UHP5YT3L",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2F1WJ3UHP5YT3L",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/AVDM/data/soil_moisture/SMEX03/Alabama/ground_soil_moisture/soil_moisture_network/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/AVDM/data/soil_moisture/SMEX03/Alabama/ground_soil_moisture/soil_moisture_network/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/AVDM/data/soil_moisture/SMEX03/Alabama/ground_soil_moisture/soil_moisture_network/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/AVDM/data/soil_moisture/SMEX03/Alabama/ground_soil_moisture/soil_moisture_network/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/AVDM/data/soil_moisture/SMEX03/Alabama/ground_soil_moisture/soil_moisture_network/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/AVDM/data/soil_moisture/SMEX03/Alabama/ground_soil_moisture/soil_moisture_network/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/AVDM/data/soil_moisture/SMEX03/Alabama/ground_soil_moisture/soil_moisture_network/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/AVDM/data/soil_moisture/SMEX03/Alabama/ground_soil_moisture/soil_moisture_network/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/1WJ3UHP5YT3L",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/1WJ3UHP5YT3L",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/1WJ3UHP5YT3L",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/1WJ3UHP5YT3L",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C1386205053-NSIDCV0",
+            "issued": "2003-06-01",
+            "keyword": [
+                "soils",
+                "agriculture",
+                "atmosphere",
+                "earth science",
+                "precipitation"
+            ],
+            "landingPage": "https://doi.org/10.5067/1WJ3UHP5YT3L",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2003-07-15",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA NSIDC DAAC"
+            },
             "spatial": "-87.08 34.68 -85.78 35.16",
+            "temporal": "2003-06-01T00:00:00Z/2003-07-15T23:59:59.999Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "SMEX03 ALMNet and SCAN Soil Moisture Data: Alabama, Version 1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/AQR50-3Y1AE",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "NASA Aquarius project. 2017-12-07. Aquarius Official Release Level 3 Rain-flagged Sea Surface Salinity Standard Mapped Image Ascending Daily Data. Version 5.0. Aquarius Sea Surface Salinity Products. Goddard Space Flight Center, 8800 Greenbelt Rd.; Greeenbelt, MD., 20771, USA. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/GSFC OBPG. https://doi.org/10.5067/AQR50-3Y1AE. http://podaac.jpl.nasa.gov/SeaSurfaceSalinity/Aquarius. NASA Aquarius project, NASA/GSFC OBPG, 2017-12-07, Aquarius Official Release Level 3 Rain-flagged Sea Surface Salinity Standard Mapped Image Ascending Daily Data V5.0, http://podaac.jpl.nasa.gov/SeaSurfaceSalinity/Aquarius.",
-            "issued": "2017-10-21",
-            "temporal": "2011-08-25T01:45:23Z/2015-06-07T11:41:38Z",
-            "@type": "dcat:Dataset",
-            "modified": "2017-12-07",
-            "keyword": [
-                "oceans",
-                "salinity/density",
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
-            "identifier": "C2491757061-POCLOUD",
-            "description": "Aquarius Level 3 sea surface salinity (SSS) rain-flagged standard mapped image data contains gridded 1 degree spatial resolution SSS averaged over daily, 7 day, monthly, and seasonal time\nscales. This particular data set is the Daily, Ascending rain-flagged rain-flagged sea surface salinity product for version 5.0 of the Aquarius data set. Only retrieved values for Ascending passes have been used to create this product. The Aquarius instrument is onboard the AQUARIUS/SAC-D satellite, a collaborative effort between NASA and the Argentinian Space Agency Comision Nacional de Actividades Espaciales (CONAE). The instrument consists of three radiometers in push broom alignment at incidence angles of 29, 38, and 46 degrees incidence angles relative to the shadow side of the orbit.  Footprints for the beams are: 76 km (along-track) x 94 km (cross-track), 84 km x 120 km and 96km x 156 km, yielding a total cross-track swath of 370 km. The radiometers measure brightness temperature at 1.413 GHz in their respective horizontal and vertical polarizations (TH and TV). A scatterometer operating at 1.26 GHz measures ocean backscatter in each footprint that is used for surface roughness corrections in the estimation of salinity. The scatterometer has an approximate 390km swath.",
-            "release-place": "Goddard Space Flight Center, 8800 Greenbelt Rd.; Greeenbelt, MD., 20771, USA",
-            "series-name": "Aquarius Official Release Level 3 Rain-flagged Sea Surface Salinity Standard Mapped Image Ascending Daily Data",
-            "graphic-preview-description": "Thumbnail",
             "creator": "NASA Aquarius project",
-            "title": "Aquarius Official Release Level 3 Rain-flagged Sea Surface Salinity Standard Mapped Image Ascending Daily Data V5.0",
-            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/AQUARIUS_L3_SSS-RainFlagged_SMIA_DAILY_V5.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "Aquarius Level 3 sea surface salinity (SSS) rain-flagged standard mapped image data contains gridded 1 degree spatial resolution SSS averaged over daily, 7 day, monthly, and seasonal time\nscales. This particular data set is the Daily, Ascending rain-flagged rain-flagged sea surface salinity product for version 5.0 of the Aquarius data set. Only retrieved values for Ascending passes have been used to create this product. The Aquarius instrument is onboard the AQUARIUS/SAC-D satellite, a collaborative effort between NASA and the Argentinian Space Agency Comision Nacional de Actividades Espaciales (CONAE). The instrument consists of three radiometers in push broom alignment at incidence angles of 29, 38, and 46 degrees incidence angles relative to the shadow side of the orbit.  Footprints for the beams are: 76 km (along-track) x 94 km (cross-track), 84 km x 120 km and 96km x 156 km, yielding a total cross-track swath of 370 km. The radiometers measure brightness temperature at 1.413 GHz in their respective horizontal and vertical polarizations (TH and TV). A scatterometer operating at 1.26 GHz measures ocean backscatter in each footprint that is used for surface roughness corrections in the estimation of salinity. The scatterometer has an approximate 390km swath.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAQR50-3Y1AE",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAQR50-3Y1AE",
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
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/AQUARIUS_L3_SSS-RainFlagged_SMIA_DAILY_V5.jpg",
-                    "description": "Thumbnail",
                     "@type": "dcat:Distribution",
+                    "description": "Thumbnail",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/AQUARIUS_L3_SSS-RainFlagged_SMIA_DAILY_V5.jpg",
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
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2491757061-POCLOUD",
-                    "description": "HTTPS endpoint for data browse and download",
                     "@type": "dcat:Distribution",
+                    "description": "HTTPS endpoint for data browse and download",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2491757061-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2491757061-POCLOUD",
-                    "description": "Browse granule search results in Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse granule search results in Earthdata Search",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2491757061-POCLOUD",
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
+            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/AQUARIUS_L3_SSS-RainFlagged_SMIA_DAILY_V5.jpg",
+            "identifier": "C2491757061-POCLOUD",
+            "issued": "2017-10-21",
+            "keyword": [
+                "oceans",
+                "salinity/density",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/AQR50-3Y1AE",
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
+            "series-name": "Aquarius Official Release Level 3 Rain-flagged Sea Surface Salinity Standard Mapped Image Ascending Daily Data",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2011-08-25T01:45:23Z/2015-06-07T11:41:38Z",
             "theme": [
                 "AQUARIUS SAC-D",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Aquarius Official Release Level 3 Rain-flagged Sea Surface Salinity Standard Mapped Image Ascending Daily Data V5.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-X-SREM-2-EAR3-V1.0",
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
-                "international rosetta mission"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This data set contains count rates (1/s) as measured by the Standard Radiation Environment Monitor (SREM) instrument on the Rosetta spacecraft, along with their standard deviations.  These are CODMAC Level 2 Experiment Data Record data, and provide a measure of the radiation in the spacecraft environment during the EARTH 3 mission phase.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-x-srem-2-ear3-v1.0_644a-kxng",
+            "issued": "2021-05-21",
+            "keyword": [
+                "earth",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-X-SREM-2-EAR3-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-x-srem-2-ear3-v1.0_644a-kxng",
-            "description": "This data set contains count rates (1/s) as measured by the Standard Radiation Environment Monitor (SREM) instrument on the Rosetta spacecraft, along with their standard deviations.  These are CODMAC Level 2 Experiment Data Record data, and provide a measure of the radiation in the spacecraft environment during the EARTH 3 mission phase.",
-            "title": "ROSETTA-ORBITER X SREM 2 EARTH 3 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER X SREM 2 EARTH 3 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MER2-M-HAZCAM-5-ANAGLYPH-OPS-V1.0",
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
-                "mars exploration rover"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "not applicable",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mer2-m-hazcam-5-anaglyph-ops-v1.0_644k-jd3n",
+            "issued": "2018-06-26",
+            "keyword": [
+                "mars",
+                "mars exploration rover"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MER2-M-HAZCAM-5-ANAGLYPH-OPS-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mer2-m-hazcam-5-anaglyph-ops-v1.0_644k-jd3n",
-            "description": "not applicable",
-            "title": "MER 2 MARS HAZARD AVOID CAMERA ANAGLYPH RDR OPS V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "MER 2 MARS HAZARD AVOID CAMERA ANAGLYPH RDR OPS V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=DAWN-A-RSS-1-VEGR-V1.0",
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
+            "description": "This data set contains archival raw, partially processed, and\nancillary/supporting gravity science data acquired during the Dawn\nmission while the spacecraft was in orbit around the asteroid Vesta.\nThe radio observations were carried out using the Dawn spacecraft and\nEarth-based receiving stations of the NASA Deep Space Network (DSN).\nThe data set was designed primarily to support generation of\nhigh-resolution gravity field models for Vesta. Of most interest are\nlikely to be the Orbit Data Files in the ODF directory, which provided\nthe raw input to gravity investigations, as well as the ionospheric and\ntropospheric media calibration files in the ION and TRO directories,\nrespectively.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.dawn-a-rss-1-vegr-v1.0_646a-jpkx",
+            "issued": "2021-05-21",
+            "keyword": [
+                "dawn mission to vesta and ceres",
+                "4 vesta"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=DAWN-A-RSS-1-VEGR-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.dawn-a-rss-1-vegr-v1.0_646a-jpkx",
-            "description": "This data set contains archival raw, partially processed, and\nancillary/supporting gravity science data acquired during the Dawn\nmission while the spacecraft was in orbit around the asteroid Vesta.\nThe radio observations were carried out using the Dawn spacecraft and\nEarth-based receiving stations of the NASA Deep Space Network (DSN).\nThe data set was designed primarily to support generation of\nhigh-resolution gravity field models for Vesta. Of most interest are\nlikely to be the Orbit Data Files in the ODF directory, which provided\nthe raw input to gravity investigations, as well as the ionospheric and\ntropospheric media calibration files in the ION and TRO directories,\nrespectively.",
-            "title": "DAWN VESTA RAW GRAVITY SCIENCE V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "DAWN VESTA RAW GRAVITY SCIENCE V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://eros.usgs.gov/imagegallery/image-week-2",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2014-04-29",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
-            "keyword": [
-                "images",
-                "usgs",
-                "earth as art",
-                "earth science",
-                "imagery",
-                "landsat"
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
-            "identifier": "NASA-912",
             "description": "The Earth Resources Observation and Science (EROS) Center manages the this image of the week gallery.",
-            "title": "Earth Resources Observation and Science (EROS) Center's Image of the Week Gallery",
-            "programCode": [
-                "026:005"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -223606,472 +223586,470 @@
                     "mediaType": "application/html"
                 }
             ],
-            "accrualPeriodicity": "irregular",
+            "identifier": "NASA-912",
+            "issued": "2014-04-29",
+            "keyword": [
+                "images",
+                "usgs",
+                "earth as art",
+                "earth science",
+                "imagery",
+                "landsat"
+            ],
+            "landingPage": "http://eros.usgs.gov/imagegallery/image-week-2",
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
+            "title": "Earth Resources Observation and Science (EROS) Center's Image of the Week Gallery"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ASDC/SUBORBITAL/DISCOVERAQ_Colorado_MetNav_AircraftInSitu_P3B_Data_1",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2022-04-18. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/ASDC/SUBORBITAL/DISCOVERAQ_Colorado_MetNav_AircraftInSitu_P3B_Data_1.",
-            "issued": "2021-08-20",
-            "temporal": "2014-07-06T00:00:00Z/2014-08-14T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-04-18",
-            "keyword": [
-                "atmospheric temperature",
-                "atmospheric pressure",
-                "atmosphere",
-                "earth science",
-                "atmospheric winds",
-                "atmospheric water vapor"
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
-            "identifier": "C2254457674-LARC_ASDC",
             "description": "DISCOVERAQ_Colorado_MetNav_AircraftInSitu_P3B_Data contains in situ meteorological and navigational data collected onboard NASA's P-3B aircraft during the Colorado (Denver) deployment of NASA's DISCOVER-AQ field study. This product features navigational data for the P-3B aircraft, along with data from the DLH. This data product contains data for only the Maryland deployment and data collection is complete.\r\n\r\nUnderstanding the factors that contribute to near surface pollution is difficult using only satellite-based observations. The incorporation of surface-level measurements from aircraft and ground-based platforms provides the crucial information necessary to validate and expand upon the use of satellites in understanding near surface pollution. Deriving Information on Surface conditions from Column and Vertically Resolved Observations Relevant to Air Quality (DISCOVER-AQ) was a four-year campaign conducted in collaboration between NASA Langley Research Center, NASA Goddard Space Flight Center, NASA Ames Research Center, and multiple universities to improve the use of satellites to monitor air quality for public health and environmental benefit. Through targeted airborne and ground-based observations, DISCOVER-AQ enabled more effective use of current and future satellites to diagnose ground level conditions influencing air quality.\r\n\r\nDISCOVER-AQ employed two NASA aircraft, the P-3B and King Air, with the P-3B completing in-situ spiral profiling of the atmosphere (aerosol properties, meteorological variables, and trace gas species). The King Air conducted both passive and active remote sensing of the atmospheric column extending below the aircraft to the surface. Data from an existing network of surface air quality monitors, AERONET sun photometers, Pandora UV/vis spectrometers and model simulations were also collected. Further, DISCOVER-AQ employed many surface monitoring sites, with measurements being made on the ground, in conjunction with the aircraft. The B200 and P-3B conducted flights in Baltimore-Washington, D.C. in 2011, Houston, TX in 2013, San Joaquin Valley, CA in 2013, and Denver, CO in 2014. These regions were targeted due to being in violation of the National Ambient Air Quality Standards (NAAQS).\r\n\r\nThe first objective of DISCOVER-AQ was to determine and investigate correlations between surface measurements and satellite column observations for the trace gases ozone (O3), nitrogen dioxide (NO2), and formaldehyde (CH2O) to understand how satellite column observations can diagnose surface conditions. DISCOVER-AQ also had the objective of using surface-level measurements to understand how satellites measure diurnal variability and to understand what factors control diurnal variability. Lastly, DISCOVER-AQ aimed to explore horizontal scales of variability, such as regions with steep gradients and urban plumes.",
-            "title": "DISCOVER-AQ Colorado Deployment P-3B Aircraft In Situ Meteorological and Navigational Data",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC%2FSUBORBITAL%2FDISCOVERAQ_Colorado_MetNav_AircraftInSitu_P3B_Data_1",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC%2FSUBORBITAL%2FDISCOVERAQ_Colorado_MetNav_AircraftInSitu_P3B_Data_1",
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
-                    "downloadURL": "https://doi.org/10.5067/ASDC/SUBORBITAL/DISCOVERAQ_Colorado_MetNav_AircraftInSitu_P3B_Data_1",
-                    "description": "Doi for DISCOVERAQ_COLORADO_METNAV_AIRCRAFTINSITU_P3B_DATA_1",
                     "@type": "dcat:Distribution",
+                    "description": "Doi for DISCOVERAQ_COLORADO_METNAV_AIRCRAFTINSITU_P3B_DATA_1",
+                    "downloadURL": "https://doi.org/10.5067/ASDC/SUBORBITAL/DISCOVERAQ_Colorado_MetNav_AircraftInSitu_P3B_Data_1",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2254457674-LARC_ASDC",
-                    "description": "Earthdata Search Client for DISCOVERAQ_COLORADO_METNAV_AIRCRAFTINSITU_P3B_DATA_1",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search Client for DISCOVERAQ_COLORADO_METNAV_AIRCRAFTINSITU_P3B_DATA_1",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2254457674-LARC_ASDC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/DISCOVER-AQ/Colorado_MetNav_AircraftInSitu_P3B_Data_1/",
-                    "description": "ASDC Direct Data Download for DISCOVERAQ_Colorado_MetNav_AircraftInSitu_P3B_Data_1",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for DISCOVERAQ_Colorado_MetNav_AircraftInSitu_P3B_Data_1",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/DISCOVER-AQ/Colorado_MetNav_AircraftInSitu_P3B_Data_1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 }
             ],
+            "identifier": "C2254457674-LARC_ASDC",
+            "issued": "2021-08-20",
+            "keyword": [
+                "atmospheric temperature",
+                "atmospheric pressure",
+                "atmosphere",
+                "earth science",
+                "atmospheric winds",
+                "atmospheric water vapor"
+            ],
+            "landingPage": "https://doi.org/10.5067/ASDC/SUBORBITAL/DISCOVERAQ_Colorado_MetNav_AircraftInSitu_P3B_Data_1",
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
+            "temporal": "2014-07-06T00:00:00Z/2014-08-14T23:59:59.999Z",
             "theme": [
                 "DISCOVER-AQ",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "DISCOVER-AQ Colorado Deployment P-3B Aircraft In Situ Meteorological and Navigational Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-2-ESC1-67PCHURYUMOV-M13-V1.0",
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
+            "description": "This data set contains raw EDR images acquired by the OSIRIS Narrow Angle\nCamera during the escort phase of the Rosetta mission at the comet 67P,\ncovering the period from 2015-02-10 to 2015-03-10.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-2-esc1-67pchuryumov-m13-v1.0_64es-43yc",
+            "issued": "2018-06-26",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-2-ESC1-67PCHURYUMOV-M13-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-2-esc1-67pchuryumov-m13-v1.0_64es-43yc",
-            "description": "This data set contains raw EDR images acquired by the OSIRIS Narrow Angle\nCamera during the escort phase of the Rosetta mission at the comet 67P,\ncovering the period from 2015-02-10 to 2015-03-10.",
-            "title": "ROSETTA-ORBITER COMET ESCORT OSINAC 2 EDR MTP 013 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "ROSETTA-ORBITER COMET ESCORT OSINAC 2 EDR MTP 013 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-ROSINA-2-EXT2-V2.0",
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
+            "description": "This data set contains CODMAC level 2 science data acquired by the COPS, DFMS and RTOF ROSINA sensors between 2016-04-06 and 2016-06-29 during the Extension phase 2 of the Rosetta mission at the comet 67P/CG. V2.0 : Some missing DFMS PDS files were added and corrupted files have been removed.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rosina-2-ext2-v2.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-ROSINA-2-EXT2-V2.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rosina-2-ext2-v2.0",
-            "description": "This data set contains CODMAC level 2 science data acquired by the COPS, DFMS and RTOF ROSINA sensors between 2016-04-06 and 2016-06-29 during the Extension phase 2 of the Rosetta mission at the comet 67P/CG. V2.0 : Some missing DFMS PDS files were added and corrupted files have been removed.",
-            "title": "ROSETTA-ORBITER 67P ROSINA 2\n                                      EXT2 V2.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P ROSINA 2\n                                      EXT2 V2.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/1KQLWP4ESGXB",
             "citation": "Miyazaki, Kazuyuki. 2024-01-08. TRPSCRPS2H2D. Version 1. TROPESS Chemical Reanalysis Surface Pressure 2-Hourly 2-dimensional Product V1. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/1KQLWP4ESGXB. https://disc.gsfc.nasa.gov/datacollection/TRPSCRPS2H2D_1.html. Digital Science Data.",
-            "issued": "2023-01-09",
-            "temporal": "2005-01-01T00:00:00Z/2021-12-31T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-02-17",
-            "references": [
-                "https://doi.org/10.5194/essd-12-2223-2020"
-            ],
-            "keyword": [
-                "earth science",
-                "atmosphere",
-                "atmospheric pressure"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "KAZUYUKI MIYAZAKI",
                 "hasEmail": "mailto:kazuyuki.miyazaki@jpl.nasa.gov"
             },
+            "creator": "Miyazaki, Kazuyuki",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C2816184432-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "The TROPESS Chemical Reanalysis Surface Pressure 2-Hourly 2-dimensional Product contains surface pressure values, a meteorological field. The data are part of the Tropospheric Chemical Reanalysis v2 (TCR-2) for the period 2005-2021. TCR-2 uses JPL's Multi-mOdel Multi-cOnstituent Chemical (MOMO-Chem) data assimilation framework that simultaneously optimizes both concentrations and emissions of multiple species from multiple satellite sensors.\n\nThe data files are written in the netCDF version 4 file format, and each file contains a year of data at 2-hourly resolution, and a spatial resolution of 1.125 x 1.125 degrees. The principal investigator for the TCR-2 data is Miyazaki, Kazuyuki.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "TRPSCRPS2H2D",
-            "creator": "Miyazaki, Kazuyuki",
-            "graphic-preview-description": "TCR-2 01 April 2005.",
-            "title": "TROPESS Chemical Reanalysis Surface Pressure 2-Hourly 2-dimensional Product V1 (TRPSCRPS2H2D) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TROPESS/images/TRPSCRPS2H2D_Sample.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2F1KQLWP4ESGXB",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2F1KQLWP4ESGXB",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TROPESS/images/TRPSCRPS2H2D_Sample.png",
-                    "description": "TCR-2 01 April 2005.",
                     "@type": "dcat:Distribution",
+                    "description": "TCR-2 01 April 2005.",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TROPESS/images/TRPSCRPS2H2D_Sample.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/TRPSCRPS2H2D_1.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/TRPSCRPS2H2D_1.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/data/TCR2_2HR_METFIELDS/TRPSCRPS2H2D.1/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/data/TCR2_2HR_METFIELDS/TRPSCRPS2H2D.1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=TRPSCRPS2H2D_1",
-                    "description": "Use the Earthdata Search Client to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search Client to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=TRPSCRPS2H2D_1",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/opendap/TCR2_2HR_METFIELDS/TRPSCRPS2H2D.1/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/opendap/TCR2_2HR_METFIELDS/TRPSCRPS2H2D.1/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/data/TCR2_2HR_METFIELDS/TRPSCRPS2H2D.1/doc/TROPESS_ChemReanalysis_Forward_Stream_README.pdf",
-                    "description": "README Document",
                     "@type": "dcat:Distribution",
+                    "description": "README Document",
+                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/data/TCR2_2HR_METFIELDS/TRPSCRPS2H2D.1/doc/TROPESS_ChemReanalysis_Forward_Stream_README.pdf",
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
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TROPESS/images/TRPSCRPS2H2D_Sample.png",
+            "identifier": "C2816184432-GES_DISC",
+            "issued": "2023-01-09",
+            "keyword": [
+                "earth science",
+                "atmosphere",
+                "atmospheric pressure"
+            ],
+            "landingPage": "https://doi.org/10.5067/1KQLWP4ESGXB",
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
+            "series-name": "TRPSCRPS2H2D",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2005-01-01T00:00:00Z/2021-12-31T23:59:59.999Z",
             "theme": [
                 "TROPESS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "TROPESS Chemical Reanalysis Surface Pressure 2-Hourly 2-dimensional Product V1 (TRPSCRPS2H2D) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/AMSR-E/AE_WKOCN.002",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "AMSR-E/Aqua Weekly L3 Global Ascending/Descending .25x.25 deg Ocean Grids V002. Version 2. Archived by National Aeronautics and Space Administration, U.S. Government, NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/AMSR-E/AE_WKOCN.002.",
-            "issued": "2002-06-19",
-            "temporal": "2002-06-19T00:00:00Z/2011-10-02T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2011-10-02",
-            "keyword": [
-                "atmospheric water vapor",
-                "ocean temperature",
-                "oceans",
-                "atmospheric winds",
-                "atmospheric/ocean indicators",
-                "atmosphere",
-                "climate indicators",
-                "clouds",
-                "earth science"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Frank Wentz",
                 "hasEmail": "mailto:wentz@remss.com"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA NSIDC DAAC"
-            },
-            "identifier": "C179014694-NSIDC_ECS",
             "description": "The Level-3 daily product (AE_DyOcn), weekly product (AE_WkOcn), and monthly product (AE_MoOcn) include SST, near-surface wind speed, columnar water vapor, and columnar cloud liquid water over oceans in a 0.25 degree by 0.25 degree grid, generated from AE_Ocean.",
-            "title": "AMSR-E/Aqua Weekly L3 Global Ascending/Descending .25x.25 deg Ocean Grids V002",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAMSR-E%2FAE_WKOCN.002",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAMSR-E%2FAE_WKOCN.002",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/AMSA/AE_WkOcn.002",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/AMSA/AE_WkOcn.002",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C179014694-NSIDC_ECS&m=-30.796875%21-0.84375%211%211%210%210%2C2&q=AE_WkOcn",
-                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C179014694-NSIDC_ECS&m=-30.796875%21-0.84375%211%211%210%210%2C2&q=AE_WkOcn",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/data/data-access-tool/AE_WkOcn/versions/2/",
-                    "description": "Data Access link for ITSD project",
                     "@type": "dcat:Distribution",
+                    "description": "Data Access link for ITSD project",
+                    "downloadURL": "https://nsidc.org/data/data-access-tool/AE_WkOcn/versions/2/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/AMSR-E/AE_WKOCN.002",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/AMSR-E/AE_WKOCN.002",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/AMSR-E/AE_WKOCN.002",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/AMSR-E/AE_WKOCN.002",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C179014694-NSIDC_ECS",
+            "issued": "2002-06-19",
+            "keyword": [
+                "atmospheric water vapor",
+                "ocean temperature",
+                "oceans",
+                "atmospheric winds",
+                "atmospheric/ocean indicators",
+                "atmosphere",
+                "climate indicators",
+                "clouds",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/AMSR-E/AE_WKOCN.002",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2011-10-02",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA NSIDC DAAC"
+            },
             "spatial": "-180.0 -89.24 180.0 89.24",
+            "temporal": "2002-06-19T00:00:00Z/2011-10-02T23:59:59.999Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "AMSR-E/Aqua Weekly L3 Global Ascending/Descending .25x.25 deg Ocean Grids V002"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/RALZNTOKG6PD",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "JPL Science Team. 2022-08-10. SNDRSNATMSMAP. Version 1. Sounder SIPS: Suomi-NPP ATMS Level 1 Daily Polygon Granule Map. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/RALZNTOKG6PD. https://disc.gsfc.nasa.gov/datacollection/SNDRSNATMSMAP_1.html. Digital Science Data.",
-            "issued": "2011-12-10",
-            "temporal": "2011-12-10T00:00:00Z/2024-11-25T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-19",
-            "keyword": [
-                "earth science",
-                "microwave",
-                "spectral/engineering"
-            ],
-            "data-presentation-form": "Digital Science Data",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Lena Iredell",
                 "hasEmail": "mailto:lena.f.iredell@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
-            "identifier": "C2373912793-GES_DISC",
-            "description": "The Advanced Technology Microwave Sounder (ATMS) Level 1B data files contain brightness temperature measurements along with ancillary spacecraft, instrument, and geolocation data of the ATMS instrument on the Suomi National Polar-orbiting Partnership Project (S-NPP).\n\nThe ATMS instrument is a cross-track scanner with 22 microwave channels in the range 23.8-183.31 Gigahertz (GHz). The beam width is 1.1 degrees for the channels in the 160-183 GHz range, 2.2 degrees for the 80 GHz and 50-60 GHz channels, and 5.2 degrees for the 23.8 and 31.4 GHz channels. Since the SNPP satellite is orbiting at an altitude of about 830 km, the instantaneous spatial resolution on the ground at nadir is about 16 km, 32 km, or 75 km depending upon the channel. The brightness temperature data are contained in an array with 135 rows in the along-track direction, 96 columns in the cross-track direction, and a 3rd dimension for each of the 22 channels. The ATMS cross-track scan interval is 0.018 seconds and the along-track scan period is 8.3 seconds.\n \nData products are constructed on six minute boundaries. The Granule Map Product consists of daily images of granule coverage in PDF format.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "SNDRSNATMSMAP",
             "creator": "JPL Science Team",
-            "title": "Sounder SIPS: Suomi-NPP ATMS Level 1 Daily Polygon Granule Map at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/SNPP.Granule.map.png",
-            "programCode": [
-                "026:001"
-            ],
+            "data-presentation-form": "Digital Science Data",
+            "description": "The Advanced Technology Microwave Sounder (ATMS) Level 1B data files contain brightness temperature measurements along with ancillary spacecraft, instrument, and geolocation data of the ATMS instrument on the Suomi National Polar-orbiting Partnership Project (S-NPP).\n\nThe ATMS instrument is a cross-track scanner with 22 microwave channels in the range 23.8-183.31 Gigahertz (GHz). The beam width is 1.1 degrees for the channels in the 160-183 GHz range, 2.2 degrees for the 80 GHz and 50-60 GHz channels, and 5.2 degrees for the 23.8 and 31.4 GHz channels. Since the SNPP satellite is orbiting at an altitude of about 830 km, the instantaneous spatial resolution on the ground at nadir is about 16 km, 32 km, or 75 km depending upon the channel. The brightness temperature data are contained in an array with 135 rows in the along-track direction, 96 columns in the cross-track direction, and a 3rd dimension for each of the 22 channels. The ATMS cross-track scan interval is 0.018 seconds and the along-track scan period is 8.3 seconds.\n \nData products are constructed on six minute boundaries. The Granule Map Product consists of daily images of granule coverage in PDF format.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FRALZNTOKG6PD",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FRALZNTOKG6PD",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
@@ -224081,250 +224059,250 @@
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/SNDRSNATMSMAP_1.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/SNDRSNATMSMAP_1.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sounder.gesdisc.eosdis.nasa.gov/data/Granule_Maps/SNDRSNATMSMAP.1/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://sounder.gesdisc.eosdis.nasa.gov/data/Granule_Maps/SNDRSNATMSMAP.1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=SNDRSNATMSMAP+1",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=SNDRSNATMSMAP+1",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://airs.jpl.nasa.gov/index.html",
-                    "description": "Sounder home page at NASA/JPL. General information on instrument, algorithms, and other AIRS and Sounder related activities can be found.",
                     "@type": "dcat:Distribution",
+                    "description": "Sounder home page at NASA/JPL. General information on instrument, algorithms, and other AIRS and Sounder related activities can be found.",
+                    "downloadURL": "https://airs.jpl.nasa.gov/index.html",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/information/documents?title=AIRS+Documentation",
-                    "description": "AIRS/Sounder Documentation Page",
                     "@type": "dcat:Distribution",
+                    "description": "AIRS/Sounder Documentation Page",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/information/documents?title=AIRS+Documentation",
+                    "mediaType": "text/html",
                     "title": "View information related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Sounder/Readme.ATMS.GranuleMap.pdf",
-                    "description": "README Document",
                     "@type": "dcat:Distribution",
+                    "description": "README Document",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Sounder/Readme.ATMS.GranuleMap.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's read me document"
                 }
             ],
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/SNPP.Granule.map.png",
+            "identifier": "C2373912793-GES_DISC",
+            "issued": "2011-12-10",
+            "keyword": [
+                "earth science",
+                "microwave",
+                "spectral/engineering"
+            ],
+            "landingPage": "https://doi.org/10.5067/RALZNTOKG6PD",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2024-11-19",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
+            },
+            "release-place": "Greenbelt, MD, USA",
+            "series-name": "SNDRSNATMSMAP",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2011-12-10T00:00:00Z/2024-11-25T00:00:00Z",
             "theme": [
                 "SUOMI-NPP",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Sounder SIPS: Suomi-NPP ATMS Level 1 Daily Polygon Granule Map at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/ZOF1X5E4L5QW",
             "citation": "Miyazaki, Kazuyuki. 2024-01-08. TRPSCRPAN2H2D. Version 1. TROPESS Chemical Reanalysis Surface PAN 2-Hourly 2-dimensional Product V1. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/ZOF1X5E4L5QW. https://disc.gsfc.nasa.gov/datacollection/TRPSCRPAN2H2D_1.html. Digital Science Data.",
-            "issued": "2023-01-09",
-            "temporal": "2005-01-01T00:00:00Z/2021-12-31T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-02-17",
-            "references": [
-                "https://doi.org/10.5194/essd-12-2223-2020"
-            ],
-            "keyword": [
-                "atmospheric chemistry",
-                "earth science",
-                "atmosphere"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "KAZUYUKI MIYAZAKI",
                 "hasEmail": "mailto:kazuyuki.miyazaki@jpl.nasa.gov"
             },
+            "creator": "Miyazaki, Kazuyuki",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C2816184431-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "The TROPESS Chemical Reanalysis PAN 2-Hourly 2-dimensional Product contains the surface concentrations of peryoxyacetyl nitrate. The data are part of the Tropospheric Chemical Reanalysis v2 (TCR-2) for the period 2005-2021. TCR-2 uses JPL's Multi-mOdel Multi-cOnstituent Chemical (MOMO-Chem) data assimilation framework that simultaneously optimizes both concentrations and emissions of multiple species from multiple satellite sensors.\n\nThe data files are written in the netCDF version 4 file format, and each file contains a year of data at 2-hourly resolution, and a spatial resolution of 1.125 x 1.125 degrees. The principal investigator for the TCR-2 data is Miyazaki, Kazuyuki.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "TRPSCRPAN2H2D",
-            "creator": "Miyazaki, Kazuyuki",
-            "graphic-preview-description": "TCR-2 01 April 2005.",
-            "title": "TROPESS Chemical Reanalysis Surface PAN 2-Hourly 2-dimensional Product V1 (TRPSCRPAN2H2D) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TROPESS/images/TRPSCRPAN2H2D_Sample.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FZOF1X5E4L5QW",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FZOF1X5E4L5QW",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TROPESS/images/TRPSCRPAN2H2D_Sample.png",
-                    "description": "TCR-2 01 April 2005.",
                     "@type": "dcat:Distribution",
+                    "description": "TCR-2 01 April 2005.",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TROPESS/images/TRPSCRPAN2H2D_Sample.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/TRPSCRPAN2H2D_1.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/TRPSCRPAN2H2D_1.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/data/TCR2_2HR_SURFCONCS/TRPSCRPAN2H2D.1/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/data/TCR2_2HR_SURFCONCS/TRPSCRPAN2H2D.1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=TRPSCRPAN2H2D_1",
-                    "description": "Use the Earthdata Search Client to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search Client to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=TRPSCRPAN2H2D_1",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/opendap/TCR2_2HR_SURFCONCS/TRPSCRPAN2H2D.1/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/opendap/TCR2_2HR_SURFCONCS/TRPSCRPAN2H2D.1/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/data/TCR2_2HR_SURFCONCS/TRPSCRPAN2H2D.1/doc/TROPESS_ChemReanalysis_Forward_Stream_README.pdf",
-                    "description": "README Document",
                     "@type": "dcat:Distribution",
+                    "description": "README Document",
+                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/data/TCR2_2HR_SURFCONCS/TRPSCRPAN2H2D.1/doc/TROPESS_ChemReanalysis_Forward_Stream_README.pdf",
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
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TROPESS/images/TRPSCRPAN2H2D_Sample.png",
+            "identifier": "C2816184431-GES_DISC",
+            "issued": "2023-01-09",
+            "keyword": [
+                "atmospheric chemistry",
+                "earth science",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.5067/ZOF1X5E4L5QW",
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
+            "series-name": "TRPSCRPAN2H2D",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2005-01-01T00:00:00Z/2021-12-31T23:59:59.999Z",
             "theme": [
                 "TROPESS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "TROPESS Chemical Reanalysis Surface PAN 2-Hourly 2-dimensional Product V1 (TRPSCRPAN2H2D) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-3-RDR-OCCULTATIONS-V1.0",
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
+            "description": "This data set is a collection of reported timings of observed asteroid occultations though 1998, and reliable occultation diameters published through the given STOP TIME. The timing data are previously unpublished; the diameters are reproduced from Millis and Dunham (1989) and Dunham, et al. (2002).",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-3-rdr-occultations-v1.0_64zz-vgae",
+            "issued": "2018-06-26",
+            "keyword": [
+                "asteroid",
+                "support archives"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-3-RDR-OCCULTATIONS-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-3-rdr-occultations-v1.0_64zz-vgae",
-            "description": "This data set is a collection of reported timings of observed asteroid occultations though 1998, and reliable occultation diameters published through the given STOP TIME. The timing data are previously unpublished; the diameters are reproduced from Millis and Dunham (1989) and Dunham, et al. (2002).",
-            "title": "ASTEROID OCCULTATIONS V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "ASTEROID OCCULTATIONS V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1273652204-GES_DISC.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "NASA Goddard Space Flight Center (GSFC). 2015-05-20. THIRN7L1CLDT. Version 001. THIR/Nimbus-7 Level 1 Calibrated Located Radiation Data at 6.7 and 11.5 microns V001. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://disc.gsfc.nasa.gov/datacollection/THIRN7L1CLDT_001.html. Digital Science Data.",
-            "issued": "2011-06-27",
-            "temporal": "1978-10-30T00:00:00Z/1985-05-13T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2011-06-27",
-            "keyword": [
-                "earth science",
-                "infrared wavelengths",
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
-            "identifier": "C1273652204-GES_DISC",
-            "description": "THIRN7L1CLDT is the Nimbus-7 Temperature-Humidity Infrared Radiometer (THIR) Level 1 Calibrated Located Radiation Data (CLDT) at 6.7 and 11.5 microns product and contains radiances expressed in units of W/m2/sr measured in the 10.5 - 12.5 (11.5) micron and 6.5 - 7.0 (6.7) micron channels. The data, originally written on IBM 360 machines, were recovered from magnetic 9-track tapes. The data are archived in their original proprietary format.\n\nThe Nimbus-7 satellite was successfully launched on October 28, 1978. The Temperature-Humidity Infrared Radiometer (THIR) experiment on Nimbus-7 is basically identical to its predecessors flown on Nimbus-4, -5 and -6, except that the data were digitized on board. The THIR instrument is a two channel high resolution scanning radiometer designed to perform two major functions:* The 11.5 micron channel provides both day and night cloud top or surface temperatures. The ground resolution at the sub-point is 6.7 km and operates day and night.* The 6.7 micron channel gives information on the moisture content of the upper troposphere and stratosphere and the location of jet streams and frontal systems. The water vapor channel has a resolution of the sub-point is 20 km and operates mostly at night.\n\nThe THIR Principal Investigator was Dr. Larry L. Stowe from NOAA NESDIS. The Nimbus-7 THIR data are available from October 30, 1979 (day of year 303) through May 13, 1985 (day of year 133).\n\nThis product was previously available from the NSSDC with the identifier ESAD-00107 (old ID 78-098A-10C).",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "THIRN7L1CLDT",
             "creator": "NASA Goddard Space Flight Center (GSFC)",
-            "title": "THIR/Nimbus-7 Level 1 Calibrated Located Radiation Data at 6.7 and 11.5 microns V001 (THIRN7L1CLDT) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/THIRN7L1CLDT_001.png",
-            "programCode": [
-                "026:001"
-            ],
+            "data-presentation-form": "Digital Science Data",
+            "description": "THIRN7L1CLDT is the Nimbus-7 Temperature-Humidity Infrared Radiometer (THIR) Level 1 Calibrated Located Radiation Data (CLDT) at 6.7 and 11.5 microns product and contains radiances expressed in units of W/m2/sr measured in the 10.5 - 12.5 (11.5) micron and 6.5 - 7.0 (6.7) micron channels. The data, originally written on IBM 360 machines, were recovered from magnetic 9-track tapes. The data are archived in their original proprietary format.\n\nThe Nimbus-7 satellite was successfully launched on October 28, 1978. The Temperature-Humidity Infrared Radiometer (THIR) experiment on Nimbus-7 is basically identical to its predecessors flown on Nimbus-4, -5 and -6, except that the data were digitized on board. The THIR instrument is a two channel high resolution scanning radiometer designed to perform two major functions:* The 11.5 micron channel provides both day and night cloud top or surface temperatures. The ground resolution at the sub-point is 6.7 km and operates day and night.* The 6.7 micron channel gives information on the moisture content of the upper troposphere and stratosphere and the location of jet streams and frontal systems. The water vapor channel has a resolution of the sub-point is 20 km and operates mostly at night.\n\nThe THIR Principal Investigator was Dr. Larry L. Stowe from NOAA NESDIS. The Nimbus-7 THIR data are available from October 30, 1979 (day of year 303) through May 13, 1985 (day of year 133).\n\nThis product was previously available from the NSSDC with the identifier ESAD-00107 (old ID 78-098A-10C).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -224333,1096 +224311,1119 @@
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/THIRN7L1CLDT_001.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/THIRN7L1CLDT_001.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/Nimbus7_THIR_Level1/THIRN7L1CLDT.001/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/Nimbus7_THIR_Level1/THIRN7L1CLDT.001/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=THIRN7L1CLDT",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=THIRN7L1CLDT",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/Nimbus7_THIR_Level1/THIRN7L1CLDT.001/doc/README.THIRN7L1CLDT.001.pdf",
-                    "description": "README Document",
                     "@type": "dcat:Distribution",
+                    "description": "README Document",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/Nimbus7_THIR_Level1/THIRN7L1CLDT.001/doc/README.THIRN7L1CLDT.001.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's read me document"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/repository/Mission/Nimbus/3.3_Product_Documentation/3.3.5_Product_Quality/N7_Users_Guide.pdf",
-                    "description": "Nimbus 7 User's Guide",
                     "@type": "dcat:Distribution",
+                    "description": "Nimbus 7 User's Guide",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/repository/Mission/Nimbus/3.3_Product_Documentation/3.3.5_Product_Quality/N7_Users_Guide.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/repository/Mission/Nimbus/3.3_Product_Documentation/3.3.5_Product_Quality/N7THIRDataUserGuide_0582.pdf",
-                    "description": "Nimbus 7 THIR Data User's Guide",
                     "@type": "dcat:Distribution",
+                    "description": "Nimbus 7 THIR Data User's Guide",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/repository/Mission/Nimbus/3.3_Product_Documentation/3.3.5_Product_Quality/N7THIRDataUserGuide_0582.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/repository/Mission/Nimbus/3.3_Product_Documentation/3.3.2_Product_Rqmts_Design/THIR_TST344011_CLDT.pdf",
-                    "description": "Nimbus 7 THIR Tape Specification Document",
                     "@type": "dcat:Distribution",
+                    "description": "Nimbus 7 THIR Tape Specification Document",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/repository/Mission/Nimbus/3.3_Product_Documentation/3.3.2_Product_Rqmts_Design/THIR_TST344011_CLDT.pdf",
+                    "mediaType": "application/pdf",
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
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Nimbus/N7_THIR_Inventory.xlsx",
-                    "description": "N7 THIR Inventory",
                     "@type": "dcat:Distribution",
+                    "description": "N7 THIR Inventory",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Nimbus/N7_THIR_Inventory.xlsx",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/THIRN7L1CLDT_001.png",
+            "identifier": "C1273652204-GES_DISC",
+            "issued": "2011-06-27",
+            "keyword": [
+                "earth science",
+                "infrared wavelengths",
+                "spectral/engineering"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1273652204-GES_DISC.html",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2011-06-27",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
+            },
+            "release-place": "Greenbelt, MD, USA",
+            "series-name": "THIRN7L1CLDT",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "1978-10-30T00:00:00Z/1985-05-13T23:59:59.999Z",
             "theme": [
                 "Nimbus",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "THIR/Nimbus-7 Level 1 Calibrated Located Radiation Data at 6.7 and 11.5 microns V001 (THIRN7L1CLDT) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/E9PAQOER1YQA",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "CLPX-Satellite: MODIS Radiances, Reflectances, Snow Cover and Related Grids, Version 1. Version 1. Archived by National Aeronautics and Space Administration, U.S. Government, NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/E9PAQOER1YQA.",
-            "issued": "2002-02-15",
-            "temporal": "2002-02-15T00:00:00Z/2003-05-15T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2003-05-15",
-            "keyword": [
-                "biosphere",
-                "land surface",
-                "national geospatial data asset",
-                "ngda",
-                "snow/ice",
-                "spectral/engineering",
-                "terrestrial hydrosphere",
-                "surface radiative properties",
-                "surface thermal properties",
-                "vegetation",
-                "visible wavelengths",
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
-            "identifier": "C1386250201-NSIDCV0",
             "description": "This data set provides Moderate Resolution Imaging Spectroradiometer (MODIS) data as part of the Cold Land Processes Field Experiment (CLPX). Parameters include radiances, surface reflectance, snow cover, land surface temperature/emissivity, and vegetation indices.",
-            "title": "CLPX-Satellite: MODIS Radiances, Reflectances, Snow Cover and Related Grids, Version 1",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FE9PAQOER1YQA",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FE9PAQOER1YQA",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/CLP/data/satellite/nsidc0151_modis/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/CLP/data/satellite/nsidc0151_modis/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/CLP/data/satellite/nsidc0151_modis/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/CLP/data/satellite/nsidc0151_modis/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/E9PAQOER1YQA",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/E9PAQOER1YQA",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/E9PAQOER1YQA",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/E9PAQOER1YQA",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C1386250201-NSIDCV0",
+            "issued": "2002-02-15",
+            "keyword": [
+                "biosphere",
+                "land surface",
+                "national geospatial data asset",
+                "ngda",
+                "snow/ice",
+                "spectral/engineering",
+                "terrestrial hydrosphere",
+                "surface radiative properties",
+                "surface thermal properties",
+                "vegetation",
+                "visible wavelengths",
+                "cryosphere",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/E9PAQOER1YQA",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2003-05-15",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA NSIDC DAAC"
+            },
             "spatial": "-108.5 38.5 -104.0 42.0",
+            "temporal": "2002-02-15T00:00:00Z/2003-05-15T23:59:59.999Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "CLPX-Satellite: MODIS Radiances, Reflectances, Snow Cover and Related Grids, Version 1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/743PMYFA8F8J",
             "citation": "William E. Shenk. 2024-10-25. GVHRRATS6IMVIS. Version 001. GVHRR/ATS-6 Black and White Visible Images on Film V001. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/743PMYFA8F8J. https://disc.gsfc.nasa.gov/datacollection/GVHRRATS6IMVIS_001.html. Digital Science Data.",
-            "issued": "2019-03-08",
-            "temporal": "1974-06-07T00:00:00Z/1974-08-15T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2019-03-08",
-            "keyword": [
-                "spectral/engineering",
-                "earth science",
-                "visible wavelengths"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "JAMES JOHNSON",
                 "hasEmail": "mailto:James.Johnson@nasa.gov"
             },
+            "creator": "William E. Shenk",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C3275628923-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "GVHRRATS6IMVIS is the Geosynchronous Very High Resolution Radiometer (GVHRR) Black and White Visible Images on Film data product from the sixth Applications Technology Satellite (ATS-6). This set of visible imagery (0.55 to 0.75 micrometer, with a 5.5 km footprint at the sub-satellite point) was originally produced on commercial image-generation equipment from digital tapes and was made available on 70-mm film, from which they were later scanned to digital TIFF image files. Each TIFF scan contains 2 or 3 pictures, and there are several hundred scans from an original 70 mm film roll which are combined into a ZIP file. Each picture contains a title at the bottom of the image and a gray scale on the right boundary that represents brightness temperatures. The title contains the satellite identification, receiving station, spectral band, picture number, picture type, pixel scale, sector number, and date.\n\nThe ATS-6 satellite was in a geosynchronous orbit parked at 95W viewing the hemisphere below the satellite. The GVHRR experiment returned data from launch until August 15, 1974 when it became inoperable, The PI was William E. Shenk from NASA Goddard Space Flight Center.\n\nThis product was previously available from the NSSDC with the identifier ESAD-00047 (old ID 74-039A-08A).",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "GVHRRATS6IMVIS",
-            "creator": "William E. Shenk",
-            "title": "GVHRR/ATS-6 Black and White Visible Images on Film V001 (GVHRRATS6IMVIS) at GES DISC",
-            "graphic-preview-description": "Typical GVHRR/ATS-6 visible film image.",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/GVHRRATS6IMVIS_001.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2F743PMYFA8F8J",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2F743PMYFA8F8J",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/GVHRRATS6IMVIS_001.png",
-                    "description": "Typical GVHRR/ATS-6 visible film image.",
                     "@type": "dcat:Distribution",
+                    "description": "Typical GVHRR/ATS-6 visible film image.",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/GVHRRATS6IMVIS_001.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/GVHRRATS6IMVIS_001.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/GVHRRATS6IMVIS_001.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/GOES/GVHRRATS6IMVIS.001/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/GOES/GVHRRATS6IMVIS.001/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=GVHRRATS6IMVIS",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=GVHRRATS6IMVIS",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/GOES/GVHRRATS6IMVIS.001/doc/README.GVHRRATS6IM.001.pdf",
-                    "description": "README Document",
                     "@type": "dcat:Distribution",
+                    "description": "README Document",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/GOES/GVHRRATS6IMVIS.001/doc/README.GVHRRATS6IM.001.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's read me document"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/ATS6/ATS6_Inventory.xlsx",
-                    "description": "ATS-6 Inventory",
                     "@type": "dcat:Distribution",
+                    "description": "ATS-6 Inventory",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/ATS6/ATS6_Inventory.xlsx",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "graphic-preview-description": "Typical GVHRR/ATS-6 visible film image.",
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/GVHRRATS6IMVIS_001.png",
+            "identifier": "C3275628923-GES_DISC",
+            "issued": "2019-03-08",
+            "keyword": [
+                "spectral/engineering",
+                "earth science",
+                "visible wavelengths"
+            ],
+            "landingPage": "https://doi.org/10.5067/743PMYFA8F8J",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2019-03-08",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
+            },
+            "release-place": "Greenbelt, MD, USA",
+            "series-name": "GVHRRATS6IMVIS",
             "spatial": "175.0 -90.0 -5.0 90.0",
+            "temporal": "1974-06-07T00:00:00Z/1974-08-15T23:59:59.999Z",
             "theme": [
                 "EOSDIS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "GVHRR/ATS-6 Black and White Visible Images on Film V001 (GVHRRATS6IMVIS) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/164",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Hall, F. G., K. F. Huemmrich, D. E. Strebel, S. J. Goetz, J. E. Nickeson, and K. D. Woods. 1996. NWS Daily Climatology Data: 1977 (SNF). [National Weather Service Daily Climatology Data: 1977 (Superior National Forest)]. Data set. Available on-line [http://www.daac.ornl.gov] from Oak Ridge National Laboratory Distributed Active Archive Center, Oak Ridge, Tennessee, U.S.A. Based on F. G. Hall, K. F. Huemmrich, D. E. Strebel, S. J. Goetz, J. E. Nickeson, and K. D. Woods, Biophysical, Morphological, Canopy Optical Property, and Productivity Data from the Superior National Forest, NASA Technical Memorandum 104568, National Aeronautics and Space Administration, Goddard Space Flight Center, Greenbelt, Maryland, U.S.A., 1992. doi:10.3334/ORNLDAAC/164",
-            "issued": "2024-03-01",
-            "temporal": "1977-01-01T00:00:00Z/1977-12-31T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-03-04",
-            "keyword": [
-                "precipitation",
-                "earth science",
-                "atmospheric water vapor",
-                "atmospheric radiation",
-                "atmospheric temperature",
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
-            "identifier": "C2884974331-ORNL_CLOUD",
             "description": "Daily min, max, average temperature (F), precipitation (water equivalent in inches), and daily insolation (Langleys) for the Superior National Forest area as collected by NWS and U. of Minnesota",
-            "graphic-preview-description": "Browse Image",
-            "title": "NWS Daily Climatology Data: 1977 (SNF)",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/snf_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F164",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F164",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/snf/SNF_MET_1977/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/snf/SNF_MET_1977/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/SNF/guides//nws_daily_climate_1977.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/SNF/guides//nws_daily_climate_1977.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/164",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/164",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/snf/SNF_MET_1977/comp/met_1977.def",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/snf/SNF_MET_1977/comp/met_1977.def",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/snf/SNF_MET_1977/comp/met_1977.txt",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/snf/SNF_MET_1977/comp/met_1977.txt",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/snf/SNF_MET_1977/comp/nws_daily_climate_1977.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/snf/SNF_MET_1977/comp/nws_daily_climate_1977.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/snf/SNF_MET_1977/comp/nws_daily_climate_1977.txt",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/snf/SNF_MET_1977/comp/nws_daily_climate_1977.txt",
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
+            "identifier": "C2884974331-ORNL_CLOUD",
+            "issued": "2024-03-01",
+            "keyword": [
+                "precipitation",
+                "earth science",
+                "atmospheric water vapor",
+                "atmospheric radiation",
+                "atmospheric temperature",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/164",
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
+            "temporal": "1977-01-01T00:00:00Z/1977-12-31T23:59:59Z",
             "theme": [
                 "SNF",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "NWS Daily Climatology Data: 1977 (SNF)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=CO-D-HRD-3-COHRD-V15.0",
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
-                "cassini-huygens"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "The High Rate Detector (HRD) from the University of Chicago is an independent part of the CDA instrument on the Cassini Orbiter that measures the dust flux and particle mass distribution of dust particles hitting the HRD detectors.  This data set includes all data from the HRD through December 31, 2014.  Please refer to Srama et al. (2004) for a detailed HRD description.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.co-d-hrd-3-cohrd-v15.0_6583-bpi9",
+            "issued": "2018-06-26",
+            "keyword": [
+                "dust",
+                "cassini-huygens"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=CO-D-HRD-3-COHRD-V15.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.co-d-hrd-3-cohrd-v15.0_6583-bpi9",
-            "description": "The High Rate Detector (HRD) from the University of Chicago is an independent part of the CDA instrument on the Cassini Orbiter that measures the dust flux and particle mass distribution of dust particles hitting the HRD detectors.  This data set includes all data from the HRD through December 31, 2014.  Please refer to Srama et al. (2004) for a detailed HRD description.",
-            "title": "CASSINI HIGH RATE DETECTOR V15.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "CASSINI HIGH RATE DETECTOR V15.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=PHX-M-TEGA-2-MSGEDR-V1.0",
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
+            "description": "Raw, uncalibrated engineering, housekeeping and scientific data collected from the Thermal Evolved Gas Analyzer (TEGA) aboard the 2007 Mars Phoenix Lander.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.phx-m-tega-2-msgedr-v1.0_658u-syg7",
+            "issued": "2018-06-26",
+            "keyword": [
+                "phoenix",
+                "mars"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=PHX-M-TEGA-2-MSGEDR-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.phx-m-tega-2-msgedr-v1.0_658u-syg7",
-            "description": "Raw, uncalibrated engineering, housekeeping and scientific data collected from the Thermal Evolved Gas Analyzer (TEGA) aboard the 2007 Mars Phoenix Lander.",
-            "title": "PHX MARS THERMAL EVOLVED GAS ANALYZER 2 MSGEDR V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "PHX MARS THERMAL EVOLVED GAS ANALYZER 2 MSGEDR V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=LCROSS-X-NSP2-2-RAW-V1.0",
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
-                "sun",
-                "lunar crater observation and sensing satellite"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "Raw, uncalibrated spectra from the Near Infrared Spectrometer 2 (NSP2) aboard the Lunar Crater Observation and Sensing Satellite (LCROSS).",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.lcross-x-nsp2-2-raw-v1.0_65ak-ybch",
+            "issued": "2018-06-26",
+            "keyword": [
+                "sun",
+                "lunar crater observation and sensing satellite"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=LCROSS-X-NSP2-2-RAW-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.lcross-x-nsp2-2-raw-v1.0_65ak-ybch",
-            "description": "Raw, uncalibrated spectra from the Near Infrared Spectrometer 2 (NSP2) aboard the Lunar Crater Observation and Sensing Satellite (LCROSS).",
-            "title": "LCROSS SUN 2ND NEAR IR SPECTROMETER 2 RAW V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "LCROSS SUN 2ND NEAR IR SPECTROMETER 2 RAW V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VEGA2-C-TVS-2-RDR-HALLEY-V1.0",
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
-                "vega 2"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "For the TV SYSTEM, 39 images were sent as a 7-d FITS file with little information in the FITS headers. In addition, to the size of the image (NAXIS1 and NAXIS2), the values for NAXIS3 and NAXIS4 were labeled 'TIME' time in seconds. The following procedure was used to convert NAXIS3 information:",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vega2-c-tvs-2-rdr-halley-v1.0_65as-ce76",
+            "issued": "2018-06-26",
+            "keyword": [
+                "halley",
+                "vega 2"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VEGA2-C-TVS-2-RDR-HALLEY-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vega2-c-tvs-2-rdr-halley-v1.0_65as-ce76",
-            "description": "For the TV SYSTEM, 39 images were sent as a 7-d FITS file with little information in the FITS headers. In addition, to the size of the image (NAXIS1 and NAXIS2), the values for NAXIS3 and NAXIS4 were labeled 'TIME' time in seconds. The following procedure was used to convert NAXIS3 information:",
-            "title": "VEGA2 TV SYSTEM IMAGES V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "VEGA2 TV SYSTEM IMAGES V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC2-0684-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 2 phase 2015-03-11 to 2015-06-30. It is a Global Gravity measurement at the comet 67P and covers the time 2015-03-30T21:41:00.000 to 2015-03-31T08:38:56.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc2-0684-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC2-0684-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc2-0684-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 2 phase 2015-03-11 to 2015-06-30. It is a Global Gravity measurement at the comet 67P and covers the time 2015-03-30T21:41:00.000 to 2015-03-31T08:38:56.000.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 2 0684 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 2 0684 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=GO-X-PPR-2-EDR-CHECKOUT-V1.0",
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
+            "description": "This data set contains the R_EDR data for the Galileo Orbiter PPR instrument for the period corresponding to the initial turn-on and checkout of the PPR in December 1989.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.go-x-ppr-2-edr-checkout-v1.0_65bp-h2gz",
+            "issued": "2021-05-21",
+            "keyword": [
+                "galileo"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=GO-X-PPR-2-EDR-CHECKOUT-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.go-x-ppr-2-edr-checkout-v1.0_65bp-h2gz",
-            "description": "This data set contains the R_EDR data for the Galileo Orbiter PPR instrument for the period corresponding to the initial turn-on and checkout of the PPR in December 1989.",
-            "title": "GLL PPR INITIAL CHECKOUT R_EDR",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "GLL PPR INITIAL CHECKOUT R_EDR"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/VIIRS/VNP43D40.001",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Crystal Schaaf, Zhuosen Wang, Xiaoyang Zhang, Alan Strahler\r\n. 2019-11-07. VNP43D40. Version 001. VIIRS/NPP BRDF/Albedo Quality Daily L3 Global 30ArcSec CMG V001\r\n. Sioux Falls, South Dakota, USA. Archived by National Aeronautics and Space Administration, U.S. Government, NASA EOSDIS Land Processes Distributed Active Archive Center. https://doi.org/10.5067/VIIRS/VNP43D40.001. https://doi.org/10.5067/VIIRS/VNP43D40.001. Digital Science Data. The DOI landing page provides citations in APA and Chicago styles.\r\n.",
-            "issued": "2019-11-07",
-            "temporal": "2012-01-19T00:00:00Z/2024-05-20T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2019-11-07",
-            "keyword": [
-                "earth science",
-                "land surface",
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
-            "identifier": "C1607328149-LPDAAC_ECS",
-            "description": "The NASA/NOAA Suomi National Polar-orbiting Partnership (Suomi NPP) Visible Infrared Imaging Radiometer Suite (VIIRS) Bidirectional Reflectance Distribution Function (BRDF) and Albedo Quality product (VNP43D40) is produced daily using 16 days of data at 30 arc second (1,000 meter) resolution. Data are temporally weighted to the ninth day, which is reflected in the file name. The VNP43D product suite is provided in a Climate Modeling Grid (CMG), which covers the entire globe for use in climate simulation models. Due to the large file size, each VNP43D product contains just one data layer for each of the parameters included in the VNP43MA2 (https://doi.org/10.5067/VIIRS/VNP43MA2.001)  product. VNP43D40 through VNP43D53 are the 30 arc second BRDF/Albedo Quality values, the Local Solar Noon values, the Valid Observations of the moderate resolution bands (M1 through M5, M7, M8, M10, and M11) plus the Day/Night Band (DNB), the Snow Status, and the Uncertainty. Details regarding methodology are available on the VNP43MA2 product page and in the Algorithm Theoretical Basis Document (ATBD).\r\n\r\nVNP43D40 consists of BRDF/Albedo quality information representing the overall quality of each pixel for VIIRS moderate resolution bands M1 through M5, M7, M8, M10, M11, and DNB.",
-            "release-place": "Sioux Falls, South Dakota, USA",
-            "series-name": "VNP43D40",
             "creator": "Crystal Schaaf, Zhuosen Wang, Xiaoyang Zhang, Alan Strahler",
-            "title": "VIIRS/NPP BRDF/Albedo Quality Daily L3 Global 30ArcSec CMG V001",
-            "programCode": [
-                "026:001"
-            ],
+            "data-presentation-form": "Digital Science Data",
+            "description": "The NASA/NOAA Suomi National Polar-orbiting Partnership (Suomi NPP) Visible Infrared Imaging Radiometer Suite (VIIRS) Bidirectional Reflectance Distribution Function (BRDF) and Albedo Quality product (VNP43D40) is produced daily using 16 days of data at 30 arc second (1,000 meter) resolution. Data are temporally weighted to the ninth day, which is reflected in the file name. The VNP43D product suite is provided in a Climate Modeling Grid (CMG), which covers the entire globe for use in climate simulation models. Due to the large file size, each VNP43D product contains just one data layer for each of the parameters included in the VNP43MA2 (https://doi.org/10.5067/VIIRS/VNP43MA2.001)  product. VNP43D40 through VNP43D53 are the 30 arc second BRDF/Albedo Quality values, the Local Solar Noon values, the Valid Observations of the moderate resolution bands (M1 through M5, M7, M8, M10, and M11) plus the Day/Night Band (DNB), the Snow Status, and the Uncertainty. Details regarding methodology are available on the VNP43MA2 product page and in the Algorithm Theoretical Basis Document (ATBD).\r\n\r\nVNP43D40 consists of BRDF/Albedo quality information representing the overall quality of each pixel for VIIRS moderate resolution bands M1 through M5, M7, M8, M10, M11, and DNB.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FVIIRS%2FVNP43D40.001",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FVIIRS%2FVNP43D40.001",
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
-                    "downloadURL": "https://doi.org/10.5067/VIIRS/VNP43D40.001",
-                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
+                    "downloadURL": "https://doi.org/10.5067/VIIRS/VNP43D40.001",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/xhdf5",
-                    "downloadURL": "https://e4ftl01.cr.usgs.gov/VIIRS/VNP43D40.001/",
-                    "description": "LP DAAC Data Pool provides direct access to available products via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "LP DAAC Data Pool provides direct access to available products via HTTPS.",
+                    "downloadURL": "https://e4ftl01.cr.usgs.gov/VIIRS/VNP43D40.001/",
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
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=C1607328149-LPDAAC_ECS",
-                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=C1607328149-LPDAAC_ECS",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://opendap.cr.usgs.gov/opendap/hyrax/VNP43D40.001/contents.html",
-                    "description": "Access data via Open-source Project for a Network Data Access Protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access data via Open-source Project for a Network Data Access Protocol.",
+                    "downloadURL": "https://opendap.cr.usgs.gov/opendap/hyrax/VNP43D40.001/contents.html",
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
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/filespec/VIIRS/1/VNP43D40",
-                    "description": "The File Specification provides a description of the product file including Scientific Data Sets and their attributes.",
+                {
                     "@type": "dcat:Distribution",
+                    "description": "The File Specification provides a description of the product file including Scientific Data Sets and their attributes.",
+                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/filespec/VIIRS/1/VNP43D40",
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
+            "identifier": "C1607328149-LPDAAC_ECS",
+            "issued": "2019-11-07",
+            "keyword": [
+                "earth science",
+                "land surface",
+                "surface radiative properties"
+            ],
+            "landingPage": "https://doi.org/10.5067/VIIRS/VNP43D40.001",
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
+            "series-name": "VNP43D40",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2012-01-19T00:00:00Z/2024-05-20T00:00:00Z",
             "theme": [
                 "NPP-JPSS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "VIIRS/NPP BRDF/Albedo Quality Daily L3 Global 30ArcSec CMG V001"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-NAVCAM-2-EXT3-MTP032-V1.1",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This dataset contains ROSETTA NAVCAM RAW DATA of the Extension 3 Phase from 26th June 2016 to 9th Aug 2016 when at the vicinity of target 67P/CG. This data set V1.1 supersedes the V1.0. It includes updates of the Browse images, clarification of calibration target, document updates and resolve other minor outstanding errata.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-navcam-2-ext3-mtp032-v1.1",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2021-05-21",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "alpha lyr",
                 "67p/churyumov-gerasimenko 1 (1969 r1)",
                 "international rosetta mission",
                 "zeta cas"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-NAVCAM-2-EXT3-MTP032-V1.1",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-navcam-2-ext3-mtp032-v1.1",
-            "description": "This dataset contains ROSETTA NAVCAM RAW DATA of the Extension 3 Phase from 26th June 2016 to 9th Aug 2016 when at the vicinity of target 67P/CG. This data set V1.1 supersedes the V1.0. It includes updates of the Browse images, clarification of calibration target, document updates and resolve other minor outstanding errata.",
-            "title": "ROSETTA-ORBITER 67P NAVCAM 2 ROSETTA EXTENSION 3 MTP032 V1.1",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P NAVCAM 2 ROSETTA EXTENSION 3 MTP032 V1.1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewBundle.jsp?identifier=urn%3Anasa%3Apds%3Amer1_apxs_raw&version=1.0",
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
+            "description": "This bundle contains raw data from the Alpha Particle X-ray Spectrometer on Mars Exploration Rover 1 (Opportunity).",
+            "identifier": "urn:nasa:pds:mer1_apxs_raw",
+            "issued": "2021-05-21",
+            "keyword": [
+                "mars",
+                "mars exploration rover"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewBundle.jsp?identifier=urn%3Anasa%3Apds%3Amer1_apxs_raw&version=1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:mer1_apxs_raw",
-            "description": "This bundle contains raw data from the Alpha Particle X-ray Spectrometer on Mars Exploration Rover 1 (Opportunity).",
-            "title": "MER1 APXS Raw Data Bundle",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "MER1 APXS Raw Data Bundle"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/MEASURES/DMSP-F15/SSMI/DATA303",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Wentz, Frank J, Kyle Hilburn and Deborah K Smith.2012. RSS SSM/I OCEAN PRODUCT GRIDS WEEKLY AVERAGE FROM DMSP F15 NETCDF [indicate subset used]. Dataset available online from the NASA Global Hydrometeorology Resource Center DAAC, Huntsville, Alabama, U.S.A. DOI: http://dx.doi.org/10.5067/MEASURES/DMSP-F15/SSMI/DATA303",
-            "issued": "2012-08-08",
-            "temporal": "1999-12-12T00:00:00Z/2011-12-31T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-04-28",
-            "keyword": [
-                "precipitation",
-                "atmospheric winds",
-                "ocean winds",
-                "oceans",
-                "earth science",
-                "clouds",
-                "atmospheric water vapor",
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
-            "identifier": "C1979943320-GHRC_DAAC",
             "description": "The RSS SSM/I Ocean Product Grids Weekly Average from DMSP F15 netCDF dataset is part of the collection of Special Sensor Microwave/Imager (SSM/I) and Special Sensor Microwave Imager Sounder (SSMIS) data products produced as part of NASA's MEaSUREs Program. Remote Sensing Systems generates SSM/I and SSMIS binary data products using a unified, physically based algorithm to simultaneously retrieve ocean wind speed, water vapor, cloud water, and rain rate. The SSMIS data have been carefully intercalibrated to the brightness temperature level of the previous SSM/I and therefore extend this important time series of ocean winds, vapor, cloud and rain values. This algorithm is a product of 20 years of refinements, improvements, and verifications. The Global Hydrology Resource Center has reformatted the binary data into a netCDF data product for each temporal group for each satellite. The netCDF SSMI/SSMIS collection will be available for F15 for a weekly average.",
-            "graphic-preview-description": "N/A",
-            "title": "RSS SSM/I OCEAN PRODUCT GRIDS WEEKLY AVERAGE FROM DMSP F15 NETCDF V7",
-            "graphic-preview-file": "https://ghrc.nsstc.nasa.gov/pub/ssmi/f15/weekly/browse/",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMEASURES%2FDMSP-F15%2FSSMI%2FDATA303",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMEASURES%2FDMSP-F15%2FSSMI%2FDATA303",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=rssmif15w",
-                    "description": "Files may be downloaded directly to your workstation from this link",
                     "@type": "dcat:Distribution",
+                    "description": "Files may be downloaded directly to your workstation from this link",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=rssmif15w",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/ssmi/f15/weekly/browse/2010/f15_ssmi_20100925v7_wk_WV.png",
-                    "description": "Sample browse image",
                     "@type": "dcat:Distribution",
+                    "description": "Sample browse image",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/ssmi/f15/weekly/browse/2010/f15_ssmi_20100925v7_wk_WV.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/ssmi/f15/weekly/browse/2010/f15_ssmi_20100925v7_wk_CW.png",
-                    "description": "Sample browse image",
                     "@type": "dcat:Distribution",
+                    "description": "Sample browse image",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/ssmi/f15/weekly/browse/2010/f15_ssmi_20100925v7_wk_CW.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/ssmi/f15/weekly/browse/2010/f15_ssmi_20100925v7_wk_RR.png",
-                    "description": "Sample browse image",
                     "@type": "dcat:Distribution",
+                    "description": "Sample browse image",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/ssmi/f15/weekly/browse/2010/f15_ssmi_20100925v7_wk_RR.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/ssmi/f15/weekly/browse/2010/f15_ssmi_20100925v7_wk_WS.png",
-                    "description": "Sample browse image",
                     "@type": "dcat:Distribution",
+                    "description": "Sample browse image",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/ssmi/f15/weekly/browse/2010/f15_ssmi_20100925v7_wk_WS.png",
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
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/doc/ssmi_netcdf/rain.pdf",
-                    "description": "SSM/I Rain Retrievals Within an Unified All-Weather Ocean Algorithm",
                     "@type": "dcat:Distribution",
+                    "description": "SSM/I Rain Retrievals Within an Unified All-Weather Ocean Algorithm",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/doc/ssmi_netcdf/rain.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View the primary investigator's documentation for this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/opendap/ssmi/f15/weekly/",
-                    "description": "OPeNDAP server dataset access",
                     "@type": "dcat:Distribution",
+                    "description": "OPeNDAP server dataset access",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/opendap/ssmi/f15/weekly/",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
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
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/ssmi/f15/weekly/browse/",
-                    "description": "N/A",
                     "@type": "dcat:Distribution",
+                    "description": "N/A",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/ssmi/f15/weekly/browse/",
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
+            "graphic-preview-file": "https://ghrc.nsstc.nasa.gov/pub/ssmi/f15/weekly/browse/",
+            "identifier": "C1979943320-GHRC_DAAC",
+            "issued": "2012-08-08",
+            "keyword": [
+                "precipitation",
+                "atmospheric winds",
+                "ocean winds",
+                "oceans",
+                "earth science",
+                "clouds",
+                "atmospheric water vapor",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.5067/MEASURES/DMSP-F15/SSMI/DATA303",
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
+            "temporal": "1999-12-12T00:00:00Z/2011-12-31T23:59:59Z",
             "theme": [
                 "DISCOVER",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "RSS SSM/I OCEAN PRODUCT GRIDS WEEKLY AVERAGE FROM DMSP F15 NETCDF V7"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC3-0919-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 3 phase 2015-07-01 to 2015-10-21. It is a Global Gravity measurement at the comet 67P and covers the time 2015-07-25T15:57:30.000 to 2015-07-25T17:35:47.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc3-0919-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC3-0919-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc3-0919-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 3 phase 2015-07-01 to 2015-10-21. It is a Global Gravity measurement at the comet 67P and covers the time 2015-07-25T15:57:30.000 to 2015-07-25T17:35:47.000.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 3 0919 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 3 0919 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/0ZBRL3GY720R",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "IceBridge WISE L2 Ice Thickness and Surface Elevation V001. Version 1. Archived by National Aeronautics and Space Administration, U.S. Government, NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/0ZBRL3GY720R.",
-            "issued": "2012-03-16",
-            "temporal": "2012-03-16T00:00:00Z/2012-03-26T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2012-03-26",
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
-            "identifier": "C1000000080-NSIDC_ECS",
             "description": "This data set contains depth sounder measurements of elevation, surface, bottom, and thickness for Alaska taken from the Warm Ice Sounding Explorer (WISE). The data were collected as part of Operation IceBridge funded aircraft survey campaigns.",
-            "title": "IceBridge WISE L2 Ice Thickness and Surface Elevation V001",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2F0ZBRL3GY720R",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2F0ZBRL3GY720R",
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
-                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/ICEBRIDGE/IRWIS2.001/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/ICEBRIDGE/IRWIS2.001/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1000000080-NSIDC_ECS&m=55.494140625%21-139.9921875%214%211%210%210%2C2&tl=1513802572%214%21%21&q=IRWIS2",
-                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1000000080-NSIDC_ECS&m=55.494140625%21-139.9921875%214%211%210%210%2C2&tl=1513802572%214%21%21&q=IRWIS2",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/data/data-access-tool/IRWIS2/versions/1/",
-                    "description": "Data Access link for ITSD project",
                     "@type": "dcat:Distribution",
+                    "description": "Data Access link for ITSD project",
+                    "downloadURL": "https://nsidc.org/data/data-access-tool/IRWIS2/versions/1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/0ZBRL3GY720R",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/0ZBRL3GY720R",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/0ZBRL3GY720R",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/0ZBRL3GY720R",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C1000000080-NSIDC_ECS",
+            "issued": "2012-03-16",
+            "keyword": [
+                "snow/ice",
+                "earth science",
+                "cryosphere"
+            ],
+            "landingPage": "https://doi.org/10.5067/0ZBRL3GY720R",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2012-03-26",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA NSIDC DAAC"
+            },
             "spatial": "-148.6 58.7 -137.1 61.7",
+            "temporal": "2012-03-16T00:00:00Z/2012-03-26T23:59:59.999Z",
             "theme": [
                 "2009_AK_NASA",
                 "2009_AK_UAF",
@@ -225438,250 +225439,229 @@
                 "2015_AK_NASA",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "IceBridge WISE L2 Ice Thickness and Surface Elevation V001"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://c3.nasa.gov/dashlink/resources/836/",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2013-09-23",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
-            "keyword": [
-                "dashlink",
-                "ames",
-                "nasa"
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
-            "identifier": "DASHLINK_836",
             "description": "Images for the website template go here.  It will not change their names or locations, but will hopefully help to organize them.  Oh, but for a directory structure...",
-            "title": "images_template",
-            "programCode": [
-                "026:029"
-            ],
             "distribution": [
                 {
-                    "mediaType": "image/x-png",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/template_site_title_bg.png",
-                    "description": "template_site_title_bg.png",
                     "@type": "dcat:Distribution",
+                    "description": "template_site_title_bg.png",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/template_site_title_bg.png",
+                    "mediaType": "image/x-png",
                     "title": "template_site_title_bg.png"
                 },
                 {
-                    "mediaType": "image/x-png",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/template_site_title_wrapper.png",
-                    "description": "template_site_title_wrapper.png",
                     "@type": "dcat:Distribution",
+                    "description": "template_site_title_wrapper.png",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/template_site_title_wrapper.png",
+                    "mediaType": "image/x-png",
                     "title": "template_site_title_wrapper.png"
                 },
                 {
-                    "mediaType": "image/pjpeg",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/template_site_title_wrapper.jpg",
-                    "description": "template_site_title_wrapper.jpg",
                     "@type": "dcat:Distribution",
+                    "description": "template_site_title_wrapper.jpg",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/template_site_title_wrapper.jpg",
+                    "mediaType": "image/pjpeg",
                     "title": "template_site_title_wrapper.jpg"
                 },
                 {
-                    "mediaType": "image/pjpeg",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/template_site_title_bg.jpg",
-                    "description": "template_site_title_bg.jpg",
                     "@type": "dcat:Distribution",
+                    "description": "template_site_title_bg.jpg",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/template_site_title_bg.jpg",
+                    "mediaType": "image/pjpeg",
                     "title": "template_site_title_bg.jpg"
                 },
                 {
-                    "mediaType": "image/x-png",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/templatemo_more_button_long.png",
-                    "description": "templatemo_more_button_long.png",
                     "@type": "dcat:Distribution",
+                    "description": "templatemo_more_button_long.png",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/templatemo_more_button_long.png",
+                    "mediaType": "image/x-png",
                     "title": "templatemo_more_button_long.png"
                 },
                 {
-                    "mediaType": "image/pjpeg",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/templatemo_more_button_long.jpg",
-                    "description": "templatemo_more_button_long.jpg",
                     "@type": "dcat:Distribution",
+                    "description": "templatemo_more_button_long.jpg",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/templatemo_more_button_long.jpg",
+                    "mediaType": "image/pjpeg",
                     "title": "templatemo_more_button_long.jpg"
                 },
                 {
-                    "mediaType": "image/x-png",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/templatemo_more_button.png",
-                    "description": "templatemo_more_button.png",
                     "@type": "dcat:Distribution",
+                    "description": "templatemo_more_button.png",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/templatemo_more_button.png",
+                    "mediaType": "image/x-png",
                     "title": "templatemo_more_button.png"
                 },
                 {
-                    "mediaType": "image/pjpeg",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/templatemo_main_bg_top_skinny.jpg",
-                    "description": "templatemo_main_bg_top_skinny.jpg",
                     "@type": "dcat:Distribution",
+                    "description": "templatemo_main_bg_top_skinny.jpg",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/templatemo_main_bg_top_skinny.jpg",
+                    "mediaType": "image/pjpeg",
                     "title": "templatemo_main_bg_top_skinny.jpg"
                 },
                 {
-                    "mediaType": "image/x-png",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/cs_leftImg.png",
-                    "description": "cs_leftImg.png",
                     "@type": "dcat:Distribution",
+                    "description": "cs_leftImg.png",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/cs_leftImg.png",
+                    "mediaType": "image/x-png",
                     "title": "cs_leftImg.png"
                 },
                 {
-                    "mediaType": "image/x-png",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/cs_rightImg.png",
-                    "description": "cs_rightImg.png",
                     "@type": "dcat:Distribution",
+                    "description": "cs_rightImg.png",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/cs_rightImg.png",
+                    "mediaType": "image/x-png",
                     "title": "cs_rightImg.png"
                 },
                 {
-                    "mediaType": "image/pjpeg",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/temlatemo_menu_hover.jpg",
-                    "description": "temlatemo_menu_hover.jpg",
                     "@type": "dcat:Distribution",
+                    "description": "temlatemo_menu_hover.jpg",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/temlatemo_menu_hover.jpg",
+                    "mediaType": "image/pjpeg",
                     "title": "temlatemo_menu_hover.jpg"
                 },
                 {
-                    "mediaType": "image/pjpeg",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/templatemo_125_125_banner.jpg",
-                    "description": "templatemo_125_125_banner.jpg",
                     "@type": "dcat:Distribution",
+                    "description": "templatemo_125_125_banner.jpg",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/templatemo_125_125_banner.jpg",
+                    "mediaType": "image/pjpeg",
                     "title": "templatemo_125_125_banner.jpg"
                 },
                 {
-                    "mediaType": "image/x-png",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/templatemo_content_bottom_2.png",
-                    "description": "templatemo_content_bottom.png",
                     "@type": "dcat:Distribution",
+                    "description": "templatemo_content_bottom.png",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/templatemo_content_bottom_2.png",
+                    "mediaType": "image/x-png",
                     "title": "templatemo_content_bottom.png"
                 },
                 {
-                    "mediaType": "image/x-png",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/templatemo_content_middle.png",
-                    "description": "templatemo_content_middle.png",
                     "@type": "dcat:Distribution",
+                    "description": "templatemo_content_middle.png",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/templatemo_content_middle.png",
+                    "mediaType": "image/x-png",
                     "title": "templatemo_content_middle.png"
                 },
                 {
-                    "mediaType": "image/x-png",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/templatemo_content_top.png",
-                    "description": "templatemo_content_top.png",
                     "@type": "dcat:Distribution",
+                    "description": "templatemo_content_top.png",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/templatemo_content_top.png",
+                    "mediaType": "image/x-png",
                     "title": "templatemo_content_top.png"
                 },
                 {
-                    "mediaType": "image/pjpeg",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/templatemo_main_bg.jpg",
-                    "description": "templatemo_main_bg.jpg",
                     "@type": "dcat:Distribution",
+                    "description": "templatemo_main_bg.jpg",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/templatemo_main_bg.jpg",
+                    "mediaType": "image/pjpeg",
                     "title": "templatemo_main_bg.jpg"
                 },
                 {
-                    "mediaType": "image/pjpeg",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/templatemo_main_bg_bottom.jpg",
-                    "description": "templatemo_main_bg_bottom.jpg",
                     "@type": "dcat:Distribution",
+                    "description": "templatemo_main_bg_bottom.jpg",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/templatemo_main_bg_bottom.jpg",
+                    "mediaType": "image/pjpeg",
                     "title": "templatemo_main_bg_bottom.jpg"
                 },
                 {
-                    "mediaType": "image/pjpeg",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/templatemo_main_bg_bottom_wrapper.jpg",
-                    "description": "templatemo_main_bg_bottom_wrapper.jpg",
                     "@type": "dcat:Distribution",
+                    "description": "templatemo_main_bg_bottom_wrapper.jpg",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/templatemo_main_bg_bottom_wrapper.jpg",
+                    "mediaType": "image/pjpeg",
                     "title": "templatemo_main_bg_bottom_wrapper.jpg"
                 },
                 {
-                    "mediaType": "image/pjpeg",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/templatemo_main_bg_top.jpg",
-                    "description": "templatemo_main_bg_top.jpg",
                     "@type": "dcat:Distribution",
+                    "description": "templatemo_main_bg_top.jpg",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/templatemo_main_bg_top.jpg",
+                    "mediaType": "image/pjpeg",
                     "title": "templatemo_main_bg_top.jpg"
                 },
                 {
-                    "mediaType": "image/pjpeg",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/templatemo_main_bg_top_wrapper.jpg",
-                    "description": "templatemo_main_bg_top_wrapper.jpg",
                     "@type": "dcat:Distribution",
+                    "description": "templatemo_main_bg_top_wrapper.jpg",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/templatemo_main_bg_top_wrapper.jpg",
+                    "mediaType": "image/pjpeg",
                     "title": "templatemo_main_bg_top_wrapper.jpg"
                 },
                 {
-                    "mediaType": "image/x-png",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/templatemo_menu_bg.png",
-                    "description": "templatemo_menu_bg.png",
                     "@type": "dcat:Distribution",
+                    "description": "templatemo_menu_bg.png",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/templatemo_menu_bg.png",
+                    "mediaType": "image/x-png",
                     "title": "templatemo_menu_bg.png"
                 },
                 {
-                    "mediaType": "image/pjpeg",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/templatemo_menu_divider.jpg",
-                    "description": "templatemo_menu_divider.jpg",
                     "@type": "dcat:Distribution",
+                    "description": "templatemo_menu_divider.jpg",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/templatemo_menu_divider.jpg",
+                    "mediaType": "image/pjpeg",
                     "title": "templatemo_menu_divider.jpg"
                 },
                 {
-                    "mediaType": "image/pjpeg",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/templatemo_menu_hover.jpg",
-                    "description": "templatemo_menu_hover.jpg",
                     "@type": "dcat:Distribution",
+                    "description": "templatemo_menu_hover.jpg",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/templatemo_menu_hover.jpg",
+                    "mediaType": "image/pjpeg",
                     "title": "templatemo_menu_hover.jpg"
                 },
                 {
-                    "mediaType": "image/pjpeg",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/templatemo_more_button.jpg",
-                    "description": "templatemo_more_button.jpg",
                     "@type": "dcat:Distribution",
+                    "description": "templatemo_more_button.jpg",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/templatemo_more_button.jpg",
+                    "mediaType": "image/pjpeg",
                     "title": "templatemo_more_button.jpg"
                 },
                 {
-                    "mediaType": "image/pjpeg",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/templatemo_post_title_bg.jpg",
-                    "description": "templatemo_post_title_bg.jpg",
                     "@type": "dcat:Distribution",
+                    "description": "templatemo_post_title_bg.jpg",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/templatemo_post_title_bg.jpg",
+                    "mediaType": "image/pjpeg",
                     "title": "templatemo_post_title_bg.jpg"
                 }
             ],
-            "accrualPeriodicity": "irregular"
+            "identifier": "DASHLINK_836",
+            "issued": "2013-09-23",
+            "keyword": [
+                "dashlink",
+                "ames",
+                "nasa"
+            ],
+            "landingPage": "https://c3.nasa.gov/dashlink/resources/836/",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:029"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Dashlink"
+            },
+            "title": "images_template"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://ti.arc.nasa.gov/opensource/projects/mkad/",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2015-01-07",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
-            "keyword": [
-                "ocsvm",
-                "mkad",
-                "foqa",
-                "one class support vector machine",
-                "algorithm",
-                "multiple kernel anomaly detection"
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
-            "identifier": "OCIO-Fitara-129",
             "description": "The Multiple Kernel Anomaly Detection (MKAD) algorithm is designed for anomaly detection over a set of files.",
-            "title": "ARC Code TI: Multiple Kernel Anomaly Detection (MKAD) Algorithm",
-            "programCode": [
-                "026:046"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -225689,23 +225669,45 @@
                     "mediaType": "application/x-tar"
                 }
             ],
-            "accrualPeriodicity": "irregular",
+            "identifier": "OCIO-Fitara-129",
+            "issued": "2015-01-07",
+            "keyword": [
+                "ocsvm",
+                "mkad",
+                "foqa",
+                "one class support vector machine",
+                "algorithm",
+                "multiple kernel anomaly detection"
+            ],
+            "landingPage": "http://ti.arc.nasa.gov/opensource/projects/mkad/",
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
+            "title": "ARC Code TI: Multiple Kernel Anomaly Detection (MKAD) Algorithm"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewBundle.jsp?identifier=urn%3Anasa%3Apds%3Agbo.olivines.pitman.lab-spectra&version=1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "Laboratory measurements quantifying the  effect of Fe substituting for Mg in olivine are necessary to           distinguish compositional from temperature, grain size and grain shape effects in observational data. This bundle presents room temperature  (18-19 degrees Celsius) diamond anvil cell thin film absorption        spectra of a large suite of olivines evenly spaced across Mg and Fe    compositions at infrared wavelengths.  In each file, the left column   is the frequency in wave numbers (units: cm**-1).  The right column is the chemical absorbance (common logarithm based).",
+            "identifier": "urn:nasa:pds:gbo.olivines.pitman.lab-spectra",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2021-05-21",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "natural fo93",
                 "synthetic fo50",
@@ -225727,243 +225729,220 @@
                 "synthetic fo75",
                 "natural fo31"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewBundle.jsp?identifier=urn%3Anasa%3Apds%3Agbo.olivines.pitman.lab-spectra&version=1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:gbo.olivines.pitman.lab-spectra",
-            "description": "Laboratory measurements quantifying the  effect of Fe substituting for Mg in olivine are necessary to           distinguish compositional from temperature, grain size and grain shape effects in observational data. This bundle presents room temperature  (18-19 degrees Celsius) diamond anvil cell thin film absorption        spectra of a large suite of olivines evenly spaced across Mg and Fe    compositions at infrared wavelengths.  In each file, the left column   is the frequency in wave numbers (units: cm**-1).  The right column is the chemical absorbance (common logarithm based).",
-            "title": "OLIVINE LABORATORY INFRARED ABSORBANCE SPECTRA",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "OLIVINE LABORATORY INFRARED ABSORBANCE SPECTRA"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ASDC/NAAMES_MetNav_AircraftInSitu_Data_1",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2020-02-04. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/ASDC/NAAMES_MetNav_AircraftInSitu_Data_1.",
-            "issued": "2019-11-06",
-            "temporal": "2015-11-04T00:00:00Z/2018-03-24T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-04-11",
-            "keyword": [
-                "atmospheric temperature",
-                "atmosphere",
-                "atmospheric water vapor",
-                "earth science"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Michael Behrenfeld",
                 "hasEmail": "mailto:behrenfm@science.oregonstate.edu"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/LARC/SD/ASDC"
-            },
-            "identifier": "C1688111692-LARC_ASDC",
             "description": "NAAMES_MetNav_AircraftInSitu_Data are in situ meteorological and navigational measurements collected onboard the C-130 aircraft during the North Atlantic Aerosols and Marine Ecosystems Study (NAAMES). These measurements were collected from November 4, 2015 \u2013 November 29, 2015, May 11, 2016 \u2013 June 5, 2016 and August 30, 2017-September 22, 2017 over the North Atlantic Ocean. The primary objective of NAAMES was to resolve key processes controlling ocean system function, their influences on atmospheric aerosols and clouds and their implications for climate. The airborne products link local-scale processes and properties to the larger scale continuous satellite record. Data collection for this product is complete.\r\n\r\nThe NASA North Atlantic Aerosols and Marine Ecosystems Study (NAAMES) project was the first NASA Earth Venture \u2013 Suborbital mission focused on studying the coupled ocean ecosystem and atmosphere. NAAMES utilizes a combination of ship-based, airborne, autonomous sensor, and remote sensing measurements that directly link ocean ecosystem processes, emissions of ocean-generated aerosols and precursor gases, and subsequent atmospheric evolution and processing. Four deployments coincide with the seasonal cycle of phytoplankton in the North Atlantic Ocean: the Winter Transition (November 5 \u2013 December 2, 2015), the Bloom Climax (May 11 \u2013 June 5, 2016), the Deceleration Phase (August 30 \u2013 September 24, 2017), and the Acceleration Phase (March 20 \u2013 April 13, 2018). Ship-based measurements were conducted from the Woods Hole Oceanographic Institution Research Vessel Atlantis in the middle of the North Atlantic Ocean, while airborne measurements were conducted on a NASA Wallops Flight Facility C-130 Hercules that was based at St. John's International Airport, Newfoundland, Canada. Data products in the ASDC archive focus on the NAAMES atmospheric aerosol, cloud, and trace gas data from the ship and aircraft, as well as related satellite and model data subsets. While a few ocean-remote sensing data products (e.g., from the high-spectral resolution lidar) are also included in the ASDC archive, most ocean data products reside in a companion archive at SeaBass.",
-            "title": "NAAMES C-130 Navigational and Meteorological Data, Version 1",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC%2FNAAMES_MetNav_AircraftInSitu_Data_1",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC%2FNAAMES_MetNav_AircraftInSitu_Data_1",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/project/NAAMES",
-                    "description": "ASDC Data and Information for NAAMES",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Data and Information for NAAMES",
+                    "downloadURL": "https://asdc.larc.nasa.gov/project/NAAMES",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://naames.larc.nasa.gov/",
-                    "description": "NAAMES project home page",
                     "@type": "dcat:Distribution",
+                    "description": "NAAMES project home page",
+                    "downloadURL": "https://naames.larc.nasa.gov/",
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
-                    "downloadURL": "https://doi.org/10.5067/ASDC/NAAMES_MetNav_AircraftInSitu_Data_1",
-                    "description": "DOI data set landing page for NAAMES_MetNav_AircraftInSitu_Data_1",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for NAAMES_MetNav_AircraftInSitu_Data_1",
+                    "downloadURL": "https://doi.org/10.5067/ASDC/NAAMES_MetNav_AircraftInSitu_Data_1",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1688111692-LARC_ASDC",
-                    "description": "Earthdata Search for NAAMES_MetNav_AircraftInSitu_Data_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for NAAMES_MetNav_AircraftInSitu_Data_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1688111692-LARC_ASDC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/naames/naames-project-documents.html",
-                    "description": "ASDC NAAMES Project Documentation Page",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC NAAMES Project Documentation Page",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/naames/naames-project-documents.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://seabass.gsfc.nasa.gov/naames",
-                    "description": "NAAMES SeaBASS Data",
                     "@type": "dcat:Distribution",
+                    "description": "NAAMES SeaBASS Data",
+                    "downloadURL": "https://seabass.gsfc.nasa.gov/naames",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.frontiersin.org/articles/10.3389/fmars.2019.00122/full",
-                    "description": "NAAMES Science Motive and Mission Overview",
                     "@type": "dcat:Distribution",
+                    "description": "NAAMES Science Motive and Mission Overview",
+                    "downloadURL": "https://www.frontiersin.org/articles/10.3389/fmars.2019.00122/full",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://earthobservatory.nasa.gov/blogs/fromthefield/category/naames/",
-                    "description": "NASA Earth Observatory NAAMES Posts",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Earth Observatory NAAMES Posts",
+                    "downloadURL": "https://earthobservatory.nasa.gov/blogs/fromthefield/category/naames/",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://blogs.nasa.gov/earthexpeditions/tag/naames/",
-                    "description": "NASA Earth Expeditions NAAMES Posts",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Earth Expeditions NAAMES Posts",
+                    "downloadURL": "https://blogs.nasa.gov/earthexpeditions/tag/naames/",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.nasa.gov/feature/five-year-nasa-study-to-look-at-the-immense-influence-of-petite-plankton",
-                    "description": "NASA.gov Article \u201cFive-Year NASA Study to Look at the Immense Influence of Petite Plankton\u201d",
                     "@type": "dcat:Distribution",
+                    "description": "NASA.gov Article \u201cFive-Year NASA Study to Look at the Immense Influence of Petite Plankton\u201d",
+                    "downloadURL": "https://www.nasa.gov/feature/five-year-nasa-study-to-look-at-the-immense-influence-of-petite-plankton",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.nasa.gov/feature/all-in-the-naames-of-ocean-ecosystems-and-climate",
-                    "description": "NASA.gov Article \u201cAll in the NAAMES of Ocean Ecosystems and Climate\u201d",
                     "@type": "dcat:Distribution",
+                    "description": "NASA.gov Article \u201cAll in the NAAMES of Ocean Ecosystems and Climate\u201d",
+                    "downloadURL": "https://www.nasa.gov/feature/all-in-the-naames-of-ocean-ecosystems-and-climate",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.nasa.gov/feature/langley/naames-returns-to-air-and-sea-to-study-plankton-s-annual-cycle",
-                    "description": "NASA.gov Article \u201cNAAMES Returns to Air and Sea to Study Plankton\u2019s Annual Cycle\u201d",
                     "@type": "dcat:Distribution",
+                    "description": "NASA.gov Article \u201cNAAMES Returns to Air and Sea to Study Plankton\u2019s Annual Cycle\u201d",
+                    "downloadURL": "https://www.nasa.gov/feature/langley/naames-returns-to-air-and-sea-to-study-plankton-s-annual-cycle",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/outreach-materials#name-exploring-the-connection-between-plankton-and-clouds-naames-storymap",
-                    "description": "ASDC StoryMap \u201cExploring the Connection Between Plankton and Clouds \u2013 NAAMES\u201d",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC StoryMap \u201cExploring the Connection Between Plankton and Clouds \u2013 NAAMES\u201d",
+                    "downloadURL": "https://asdc.larc.nasa.gov/outreach-materials#name-exploring-the-connection-between-plankton-and-clouds-naames-storymap",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/micro-article/a-look-into-the-north-atlantic-aerosols-and-marine-ecosystems-study-naames",
-                    "description": "ASDC Microarticle \u201cA Look into the North Atlantic Aerosols and Marine Ecosystems Study (NAAMES)\u201d",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Microarticle \u201cA Look into the North Atlantic Aerosols and Marine Ecosystems Study (NAAMES)\u201d",
+                    "downloadURL": "https://asdc.larc.nasa.gov/micro-article/a-look-into-the-north-atlantic-aerosols-and-marine-ecosystems-study-naames",
+                    "mediaType": "text/html",
                     "title": "View a micro article on this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/micro-article/observing-sea-to-air-aerosol-gas-fluxes-under-extreme-weather-conditions",
-                    "description": "ASDC Microarticle \u201cObserving Sea-to-Air Aerosol Gas Fluxes Under Extreme Weather Conditions\u201d",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Microarticle \u201cObserving Sea-to-Air Aerosol Gas Fluxes Under Extreme Weather Conditions\u201d",
+                    "downloadURL": "https://asdc.larc.nasa.gov/micro-article/observing-sea-to-air-aerosol-gas-fluxes-under-extreme-weather-conditions",
+                    "mediaType": "text/html",
                     "title": "View a micro article on this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/soot/power-user/NAAMES/2015",
-                    "description": "NAAMES Data on the Sub-Orbital Order Tool (SOOT) Power User Interface (UI)",
                     "@type": "dcat:Distribution",
+                    "description": "NAAMES Data on the Sub-Orbital Order Tool (SOOT) Power User Interface (UI)",
+                    "downloadURL": "https://asdc.larc.nasa.gov/soot/power-user/NAAMES/2015",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through the Sub-Orbital Order Tool"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.frontiersin.org/research-topics/8451/unraveling-mechanisms-underlying-annual-plankton-blooms-in-the-north-atlantic-and-their-implications",
-                    "description": "Frontiers E-Book: Unraveling Mechanisms Underlying Annual Plankton Blooms in the North Atlantic and their Implications for Biogenic Aerosol Properties and Cloud Formation",
                     "@type": "dcat:Distribution",
+                    "description": "Frontiers E-Book: Unraveling Mechanisms Underlying Annual Plankton Blooms in the North Atlantic and their Implications for Biogenic Aerosol Properties and Cloud Formation",
+                    "downloadURL": "https://www.frontiersin.org/research-topics/8451/unraveling-mechanisms-underlying-annual-plankton-blooms-in-the-north-atlantic-and-their-implications",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/NAAMES/MetNav_AircraftInSitu_Data_1/",
-                    "description": "ASDC Direct Data Download for NAAMES_MetNav_AircraftInSitu_Data_1",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for NAAMES_MetNav_AircraftInSitu_Data_1",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/NAAMES/MetNav_AircraftInSitu_Data_1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 }
             ],
+            "identifier": "C1688111692-LARC_ASDC",
+            "issued": "2019-11-06",
+            "keyword": [
+                "atmospheric temperature",
+                "atmosphere",
+                "atmospheric water vapor",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/ASDC/NAAMES_MetNav_AircraftInSitu_Data_1",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2022-04-11",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/LARC/SD/ASDC"
+            },
             "spatial": "<?xml version=\"1.0\" encoding=\"UTF-8\"?><gml:Polygon xmlns:gml=\"http://www.opengis.net/gml/3.2\" srsName=\"EPSG:9825\"><gml:outerBoundaryIs><gml:LinearRing><gml:posList>30.0 -80.0 30.0 -30.0 65.0 -30.0 65.0 -80.0 30.0 -80.0</gml:posList></gml:LinearRing></gml:outerBoundaryIs><gml:innerBoundaryIs></gml:innerBoundaryIs></gml:Polygon>",
+            "temporal": "2015-11-04T00:00:00Z/2018-03-24T23:59:59.999Z",
             "theme": [
                 "NAAMES",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "NAAMES C-130 Navigational and Meteorological Data, Version 1"
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
-                "knowledge",
-                "sharing",
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
-            "identifier": "NASA-860__17",
             "description": "Academy of Program/Project & Engineering Leadership's ASK Magazine archive.",
-            "title": "Academy of Program/Project & Engineering Leadership ASK Magazine Past Issues",
-            "programCode": [
-                "026:045"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -225971,131 +225950,154 @@
                     "mediaType": "application/pdf"
                 }
             ],
-            "accrualPeriodicity": "R/P3M",
+            "identifier": "NASA-860__17",
+            "issued": "2018-06-25",
+            "keyword": [
+                "appel",
+                "knowledge",
+                "sharing",
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
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/4",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Kelly, R. D. 1994. Aircraft Flux - Detrended: U of Wy. (FIFE). Data set. Available on-line [http://www.daac.ornl.gov] from Oak Ridge National Laboratory Distributed Active Archive Center, Oak Ridge, Tennessee, U.S.A. Also published in D. E. Strebel, D. R. Landis, K. F. Huemmrich, and B. W. Meeson (eds.), Collected Data of the First ISLSCP Field Experiment, Vol. 1: Surface Observations and Non-Image Data Sets. CD-ROM. National Aeronautics and Space Administration, Goddard Space Flight Center, Greenbelt, Maryland, U.S.A. (available from http://www.daac.ornl.gov). doi:10.3334/ORNLDAAC/4",
-            "issued": "2024-05-02",
-            "temporal": "1987-08-11T00:00:00Z/1989-10-31T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-03",
-            "keyword": [
-                "atmosphere",
-                "atmospheric temperature",
-                "atmospheric water vapor",
-                "atmospheric radiation",
-                "atmospheric pressure",
-                "atmospheric chemistry",
-                "atmospheric winds",
-                "altitude",
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
-            "identifier": "C2968504925-ORNL_CLOUD",
             "description": "Detrended boundary layer fluxes recorded on aircraft flights over the Konza",
-            "graphic-preview-description": "Browse Image",
-            "title": "Aircraft Flux-Detrended: U of Wy. (FIFE)",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/fife_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F4",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F4",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/fife/fife_AF_dtrnd_wyo/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/fife/fife_AF_dtrnd_wyo/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/FIFE/guides/air_flux_det_wy.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/FIFE/guides/air_flux_det_wy.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/4",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/4",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/msword",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/fife/fife_AF_dtrnd_wyo/comp/aflux_kl.doc",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/fife/fife_AF_dtrnd_wyo/comp/aflux_kl.doc",
+                    "mediaType": "application/msword",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/fife/fife_AF_dtrnd_wyo/comp/af_dtrnd.tdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/fife/fife_AF_dtrnd_wyo/comp/af_dtrnd.tdf",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/fife/fife_AF_dtrnd_wyo/comp/air_flux_det_wy.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/fife/fife_AF_dtrnd_wyo/comp/air_flux_det_wy.pdf",
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
+            "identifier": "C2968504925-ORNL_CLOUD",
+            "issued": "2024-05-02",
+            "keyword": [
+                "atmosphere",
+                "atmospheric temperature",
+                "atmospheric water vapor",
+                "atmospheric radiation",
+                "atmospheric pressure",
+                "atmospheric chemistry",
+                "atmospheric winds",
+                "altitude",
+                "biosphere",
+                "earth science",
+                "vegetation"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/4",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2024-05-03",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "ORNL_DAAC"
+            },
             "spatial": "-102.0 37.0 -95.0 40.0",
+            "temporal": "1987-08-11T00:00:00Z/1989-10-31T23:59:59Z",
             "theme": [
                 "FIFE",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Aircraft Flux-Detrended: U of Wy. (FIFE)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MESS-E%2FV%2FH%2FSW-EPPS-2-EPS-RAWDATA-V2.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "Abstract ======== This data set consists of the MESSENGER Energetic Particle and Plasma Spectrometer (EPPS) uncalibrated observations, also known as EDRs. The system encompasses 2 instrument subsystems - the Energetic Particle Spectrometer (EPS) and the Fast Imaging Plasma Spectrometer (FIPS). EPS covers the energy range of 25 to > 500 keV for electrons, and 10 keV/nucleon to ~3 MeV total energy for ions. FIPS covers the energy/ charge range of < 50 eV/q to 20 keV/q. There are nine EDR data products, four of science and ancillary data for the EPS and the FIPS, and one of engineering and status for the total EPPS instrument.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mess-e-v-h-sw-epps-2-eps-rawdata-v2.0_65up-b397",
             "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "calibration",
                 "mercury",
@@ -226103,1519 +226105,1495 @@
                 "earth",
                 "venus"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MESS-E%2FV%2FH%2FSW-EPPS-2-EPS-RAWDATA-V2.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mess-e-v-h-sw-epps-2-eps-rawdata-v2.0_65up-b397",
-            "description": "Abstract ======== This data set consists of the MESSENGER Energetic Particle and Plasma Spectrometer (EPPS) uncalibrated observations, also known as EDRs. The system encompasses 2 instrument subsystems - the Energetic Particle Spectrometer (EPS) and the Fast Imaging Plasma Spectrometer (FIPS). EPS covers the energy range of 25 to > 500 keV for electrons, and 10 keV/nucleon to ~3 MeV total energy for ions. FIPS covers the energy/ charge range of < 50 eV/q to 20 keV/q. There are nine EDR data products, four of science and ancillary data for the EPS and the FIPS, and one of engineering and status for the total EPPS instrument.",
-            "title": "EPPS UNCALIBRATED (EDR) DATA E/V/H V2.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "EPPS UNCALIBRATED (EDR) DATA E/V/H V2.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.7927/H4DN4300",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Goddard Space Flight Center - GSFC, and Center for International Earth Science Information Network - CIESIN - Columbia University. 2009-12-31. Indicators of Coastal Water Quality: Annual Chlorophyll-a Concentration 1998-2007. Version 1.00. Palisades, NY. Archived by National Aeronautics and Space Administration, U.S. Government, NASA Socioeconomic Data and Applications Center (SEDAC). https://doi.org/10.7927/H4DN4300. https://doi.org/10.7927/H4DN4300.",
-            "issued": "2009-12-31",
-            "temporal": "1998-01-01T00:00:00Z/2007-12-31T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2009-12-31",
-            "references": [
-                "https://doi.org/10.7927/H48W3B88",
-                "https://doi.org/10.7927/H4J96490"
-            ],
-            "keyword": [
-                "ocean chemistry",
-                "oceans",
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
-            "identifier": "C179002069-SEDAC",
-            "description": "The Annual Chlorophyll-a Concentrations component of the Indicators of Coastal Water Quality Collection consists of gridded satellite measurements of chlorophyll-a concentrations (in nanogram/cubic meter) in a band extending between 10 and 100 km from the shoreline. Chlorophyll-a concentrations are derived from NASA's Sea-viewing Wide Field-of-view Sensor (SeaWiFS). The grids are based on annual composites of SeaWiFS satellite data provided by the SeaWiFS Project, NASA/Goddard Space Flight Center and GeoEye in the form of HDF files at a resolution of 5 arc-minutes (approximately 9 x 9 km at the equator). The source files are true-color images generated from sub-sampled, calibrated, Rayleigh-corrected level-2 data, which are derived from raw radiance counts by applying sensor calibration, atmospheric corrections, and bio-optical algorithms. To arrive at chlorophyll-a concentrations, radiance counts were converted using the conversion formula provided as part of the original data files. The gridding is done by the Columbia University Center for International Earth Science Information Network (CIESIN).",
-            "release-place": "Palisades, NY",
-            "graphic-preview-description": "Sample browse graphic of the data set.",
             "creator": "Goddard Space Flight Center - GSFC, and Center for International Earth Science Information Network - CIESIN - Columbia University",
-            "title": "Indicators of Coastal Water Quality: Annual Chlorophyll-a Concentration 1998-2007",
-            "graphic-preview-file": "https://sedac.ciesin.columbia.edu/downloads/maps/icwq/icwq-annual-chlorophyll-a-concentration-1998-2007/sedac-logo.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The Annual Chlorophyll-a Concentrations component of the Indicators of Coastal Water Quality Collection consists of gridded satellite measurements of chlorophyll-a concentrations (in nanogram/cubic meter) in a band extending between 10 and 100 km from the shoreline. Chlorophyll-a concentrations are derived from NASA's Sea-viewing Wide Field-of-view Sensor (SeaWiFS). The grids are based on annual composites of SeaWiFS satellite data provided by the SeaWiFS Project, NASA/Goddard Space Flight Center and GeoEye in the form of HDF files at a resolution of 5 arc-minutes (approximately 9 x 9 km at the equator). The source files are true-color images generated from sub-sampled, calibrated, Rayleigh-corrected level-2 data, which are derived from raw radiance counts by applying sensor calibration, atmospheric corrections, and bio-optical algorithms. To arrive at chlorophyll-a concentrations, radiance counts were converted using the conversion formula provided as part of the original data files. The gridding is done by the Columbia University Center for International Earth Science Information Network (CIESIN).",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.7927%2FH4DN4300",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.7927%2FH4DN4300",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/downloads/maps/icwq/icwq-annual-chlorophyll-a-concentration-1998-2007/sedac-logo.jpg",
-                    "description": "Sample browse graphic of the data set.",
                     "@type": "dcat:Distribution",
+                    "description": "Sample browse graphic of the data set.",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/downloads/maps/icwq/icwq-annual-chlorophyll-a-concentration-1998-2007/sedac-logo.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/icwq-annual-chlorophyll-a-concentration-1998-2007/data-download",
-                    "description": "Data Download Page",
                     "@type": "dcat:Distribution",
+                    "description": "Data Download Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/icwq-annual-chlorophyll-a-concentration-1998-2007/data-download",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/icwq-annual-chlorophyll-a-concentration-1998-2007",
-                    "description": "Data Set\u00a0Overview Page",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set\u00a0Overview Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/icwq-annual-chlorophyll-a-concentration-1998-2007",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "graphic-preview-description": "Sample browse graphic of the data set.",
+            "graphic-preview-file": "https://sedac.ciesin.columbia.edu/downloads/maps/icwq/icwq-annual-chlorophyll-a-concentration-1998-2007/sedac-logo.jpg",
+            "identifier": "C179002069-SEDAC",
+            "issued": "2009-12-31",
+            "keyword": [
+                "ocean chemistry",
+                "oceans",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.7927/H4DN4300",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2009-12-31",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "SEDAC"
+            },
+            "references": [
+                "https://doi.org/10.7927/H48W3B88",
+                "https://doi.org/10.7927/H4J96490"
+            ],
+            "release-place": "Palisades, NY",
             "spatial": "-180.0 -90.0 179.99856 89.99928",
+            "temporal": "1998-01-01T00:00:00Z/2007-12-31T00:00:00Z",
             "theme": [
                 "ICWQ",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Indicators of Coastal Water Quality: Annual Chlorophyll-a Concentration 1998-2007"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/SO0GIXLAK2SG",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "SnowEx20 Grand Mesa IOP Computed Tomography Snow Microstructure V001. Version 1. Archived by National Aeronautics and Space Administration, U.S. Government, NASA NSIDC DAAC. https://doi.org/10.5067/SO0GIXLAK2SG.",
-            "issued": "2020-02-03",
-            "temporal": "2020-02-03T00:00:00Z/2020-02-08T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-02-08",
-            "keyword": [
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
-            "identifier": "C2695623073-NSIDC_ECS",
             "description": "This data set characterizes snow microstructure for 6 snow pits from the SnowEx 2020 Grand Mesa Intensive Observation Period (February 2020) using microcomputed tomography (micro-CT). Included with this data set are two- and three-dimensional microstructural analysis of DMP/DEP casted and un-casted snow samples, available as .xlsx and .txt file, and visual representations of the three-dimensional snow structure, available is .bmp image files. Containers of snow were collected at 6 snow pits in approximately 17 cm intervals. There were approximately 5-8 discrete containers per pit and each container had an ~2 cm overlap with the sample below. A 6-cm section of snow was dissected from each container of snow, which were analyzed in ~2 cm sub-sections. Each sub-section was scanned in three intervals using a micro-CT instrument. The three interval scans comprise multiple slices, and were combined into the reconstructed final scan used for calculating the snow microstructural data.",
-            "title": "SnowEx20 Grand Mesa IOP Computed Tomography Snow Microstructure V001",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSO0GIXLAK2SG",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSO0GIXLAK2SG",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/SNOWEX/SNEX20_GM_CTSM.001/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/SNOWEX/SNEX20_GM_CTSM.001/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/data/data-access-tool/SNEX20_GM_CTSM/versions/1",
-                    "description": "Search and filter data files using a map-based interface",
                     "@type": "dcat:Distribution",
+                    "description": "Search and filter data files using a map-based interface",
+                    "downloadURL": "https://nsidc.org/data/data-access-tool/SNEX20_GM_CTSM/versions/1",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=SNEX20_GM_CTSM+V001",
-                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=SNEX20_GM_CTSM+V001",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/SNOWEX/SNEX20_GM_CTSM.001/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/SNOWEX/SNEX20_GM_CTSM.001/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/data/data-access-tool/SNEX20_GM_CTSM/versions/1",
-                    "description": "Search and filter data files using a map-based interface",
                     "@type": "dcat:Distribution",
+                    "description": "Search and filter data files using a map-based interface",
+                    "downloadURL": "https://nsidc.org/data/data-access-tool/SNEX20_GM_CTSM/versions/1",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=SNEX20_GM_CTSM+V001",
-                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=SNEX20_GM_CTSM+V001",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/SNOWEX/SNEX20_GM_CTSM.001/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/SNOWEX/SNEX20_GM_CTSM.001/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/data/data-access-tool/SNEX20_GM_CTSM/versions/1",
-                    "description": "Search and filter data files using a map-based interface",
                     "@type": "dcat:Distribution",
+                    "description": "Search and filter data files using a map-based interface",
+                    "downloadURL": "https://nsidc.org/data/data-access-tool/SNEX20_GM_CTSM/versions/1",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=SNEX20_GM_CTSM+V001",
-                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=SNEX20_GM_CTSM+V001",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/SO0GIXLAK2SG",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/SO0GIXLAK2SG",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/SO0GIXLAK2SG",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/SO0GIXLAK2SG",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C2695623073-NSIDC_ECS",
+            "issued": "2020-02-03",
+            "keyword": [
+                "cryosphere",
+                "snow/ice",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/SO0GIXLAK2SG",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2020-02-08",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA NSIDC DAAC"
+            },
             "spatial": "-108.228389 39.005111 -108.110485 39.065321",
+            "temporal": "2020-02-03T00:00:00Z/2020-02-08T23:59:59.999Z",
             "theme": [
                 "SnowEx",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "SnowEx20 Grand Mesa IOP Computed Tomography Snow Microstructure V001"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=CO-SA-ISSNA-5-MIMASSHAPE-V2.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "The shape model of Mimas derived by Robert Gaskell from Cassini ISSNA and ISSWA images and Voyager 1 ISSN images. The model is provided in the implicitly connected quadrilateral (ICQ) format. This version of the model was prepared on June 26, 2012. Vertex-facet versions of the models are also provided.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.co-sa-issna-5-mimasshape-v2.0_65zu-9xyb",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "voyager",
                 "cassini-huygens",
                 "s1 mimas"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=CO-SA-ISSNA-5-MIMASSHAPE-V2.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.co-sa-issna-5-mimasshape-v2.0_65zu-9xyb",
-            "description": "The shape model of Mimas derived by Robert Gaskell from Cassini ISSNA and ISSWA images and Voyager 1 ISSN images. The model is provided in the implicitly connected quadrilateral (ICQ) format. This version of the model was prepared on June 26, 2012. Vertex-facet versions of the models are also provided.",
-            "title": "GASKELL MIMAS SHAPE MODEL V2.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "GASKELL MIMAS SHAPE MODEL V2.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG2-J-PLS-5-SUMM-ELE-MOM-96.0SEC-V1.0",
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
+            "description": "This data set contains derived values of the electron density and moment temperature at Jupiter during the Voyager 2 encounter in the PLS voltage range (10-5950 eV/q). Adjacent low and high energy electron measurements are combined to form a composite spectra which is used for the moment calculation. These assume isotropic distributions and correct for positive spacecraft charge when applicable and interpolate electron spectra below the 10 eV instrument threshold before performing the integration over velocity. Data format: column 1 is time (yyyy-mm-ddThh:mm:ss.sssZ), column 2 is the moment density in cm^-3, column 3 the temperature in eV. Each row has format (a24, 2(1x,1pe9.2)). Values of -9.99e+10 indicate that the parameter could not be obtained from the data using the standard analysis technique. Additional information about this data set and the instrument which produced it can be found elsewhere in this catalog.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg2-j-pls-5-summ-ele-mom-96.0sec-v1.0_6624-weh8",
+            "issued": "2021-05-21",
+            "keyword": [
+                "jupiter",
+                "voyager"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG2-J-PLS-5-SUMM-ELE-MOM-96.0SEC-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg2-j-pls-5-summ-ele-mom-96.0sec-v1.0_6624-weh8",
-            "description": "This data set contains derived values of the electron density and moment temperature at Jupiter during the Voyager 2 encounter in the PLS voltage range (10-5950 eV/q). Adjacent low and high energy electron measurements are combined to form a composite spectra which is used for the moment calculation. These assume isotropic distributions and correct for positive spacecraft charge when applicable and interpolate electron spectra below the 10 eV instrument threshold before performing the integration over velocity. Data format: column 1 is time (yyyy-mm-ddThh:mm:ss.sssZ), column 2 is the moment density in cm^-3, column 3 the temperature in eV. Each row has format (a24, 2(1x,1pe9.2)). Values of -9.99e+10 indicate that the parameter could not be obtained from the data using the standard analysis technique. Additional information about this data set and the instrument which produced it can be found elsewhere in this catalog.",
-            "title": "VG2 JUP PLASMA DERIVED ELECTRON MOMENTS\n96.0 SEC V1.1",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "VG2 JUP PLASMA DERIVED ELECTRON MOMENTS\n96.0 SEC V1.1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1545",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Pu, R., Z. Li, P. Gong, I.A. Csiszar, R. Fraser, W.M. Hao, S. Kondragunta, T.V. Loboda, J.V. Hall, and V.S. Shevade. 2018. ABoVE: AVHRR-Derived Forest Fire Burned Area-Hot Spots, Alaska and Canada, 1989-2000. ORNL DAAC, Oak Ridge, Tennessee, USA. https://doi.org/10.3334/ORNLDAAC/1545",
-            "issued": "2019-01-25",
-            "temporal": "1989-05-01T00:00:00Z/2000-10-31T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-06-12",
-            "keyword": [
-                "natural hazards",
-                "earth science",
-                "ecological dynamics",
-                "human dimensions",
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
-            "identifier": "C2170970978-ORNL_CLOUD",
             "description": "This dataset provides annual forest fire burned area and daily hotspot products developed using data acquired from the Advanced Very-High-Resolution Radiometer (AVHRR) instruments carried aboard two NOAA polar-orbiting satellites (NOAA-11 and NOAA-14). The fire products were generated over 12 fire seasons (1st May - 31st October) from 1989-2000 across North America  at 1-km resolution and subset to the ABoVE spatial domain of Alaska and Canada.",
-            "graphic-preview-description": "Figure 1: The ABoVE study domain showing cumulative annual burned areas derived from AVHRR for 1989 - 2000.",
-            "title": "ABoVE: AVHRR-Derived Forest Fire Burned Area-Hot Spots, Alaska and Canada, 1989-2000",
-            "graphic-preview-file": "https://daac.ornl.gov/ABOVE/guides/AVHRR_Fire_Products_Fig1.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1545",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1545",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/above/AVHRR_Fire_Products/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/above/AVHRR_Fire_Products/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/ABOVE/guides/AVHRR_Fire_Products.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/ABOVE/guides/AVHRR_Fire_Products.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1545",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1545",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/AVHRR_Fire_Products/comp/AVHRR_Fire_Products.pdf",
-                    "description": "ABoVE Forest Fire AVHRR Derived Burned Area and Hot Spots for 1989 - 2000: AVHRR_Fire_Products.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "ABoVE Forest Fire AVHRR Derived Burned Area and Hot Spots for 1989 - 2000: AVHRR_Fire_Products.pdf",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/AVHRR_Fire_Products/comp/AVHRR_Fire_Products.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/AVHRR_Fire_Products/comp/AVHRR_Fire_Product_User_Guide.pdf",
-                    "description": "ABoVE Forest Fire AVHRR Derived Burned Area and Hot Spots for 1989 - 2000: AVHRR_Fire_Product_User_Guide.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "ABoVE Forest Fire AVHRR Derived Burned Area and Hot Spots for 1989 - 2000: AVHRR_Fire_Product_User_Guide.pdf",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/AVHRR_Fire_Products/comp/AVHRR_Fire_Product_User_Guide.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://daac.ornl.gov/ABOVE/guides/AVHRR_Fire_Products_Fig1.png",
-                    "description": "Figure 1: The ABoVE study domain showing cumulative annual burned areas derived from AVHRR for 1989 - 2000.",
                     "@type": "dcat:Distribution",
+                    "description": "Figure 1: The ABoVE study domain showing cumulative annual burned areas derived from AVHRR for 1989 - 2000.",
+                    "downloadURL": "https://daac.ornl.gov/ABOVE/guides/AVHRR_Fire_Products_Fig1.png",
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
+            "graphic-preview-description": "Figure 1: The ABoVE study domain showing cumulative annual burned areas derived from AVHRR for 1989 - 2000.",
+            "graphic-preview-file": "https://daac.ornl.gov/ABOVE/guides/AVHRR_Fire_Products_Fig1.png",
+            "identifier": "C2170970978-ORNL_CLOUD",
+            "issued": "2019-01-25",
+            "keyword": [
+                "natural hazards",
+                "earth science",
+                "ecological dynamics",
+                "human dimensions",
+                "biosphere"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1545",
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
             "spatial": "-165.19 41.72 -53.17 69.01",
+            "temporal": "1989-05-01T00:00:00Z/2000-10-31T23:59:59Z",
             "theme": [
                 "ABoVE",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "ABoVE: AVHRR-Derived Forest Fire Burned Area-Hot Spots, Alaska and Canada, 1989-2000"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/9HYQMFZP4ALB",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "SnowEx20 Raw Near Surface Snow Temperature Profile Time Series V001. Version 1. Archived by National Aeronautics and Space Administration, U.S. Government, NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/9HYQMFZP4ALB.",
-            "issued": "2020-02-05",
-            "temporal": "2020-02-05T00:00:00Z/2020-02-12T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-02-12",
-            "keyword": [
-                "snow/ice",
-                "earth science",
-                "terrestrial hydrosphere"
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
-            "identifier": "C1997892310-NSIDC_ECS",
             "description": "This data set contains an eight-day time series of vertical temperature profile measurements. Measurements were collected using a thermoprobe to a depth of 30 cm at two site locations. These data were collected as part of the SnowEx 2020 Intensive Observation Period in Grand Mesa, Colorado. Alongside temperature profiles, this data set contains snow depth measurements, manual temperature measurements, and thermal infrared camera images. These data are published without QA/QC or calibration with manual measurements.",
-            "title": "SnowEx20 Raw Near Surface Snow Temperature Profile Time Series V001",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2F9HYQMFZP4ALB",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2F9HYQMFZP4ALB",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1997892310-NSIDC_ECS&pg%5B0%5D%5Bgsk%5D=-start_date&q=SNEX20_VPTS_Raw&m=38.35552775499695%21-113.57226562500001%215%211%210%210%2C2&tl=1596643552%214%21%21",
-                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1997892310-NSIDC_ECS&pg%5B0%5D%5Bgsk%5D=-start_date&q=SNEX20_VPTS_Raw&m=38.35552775499695%21-113.57226562500001%215%211%210%210%2C2&tl=1596643552%214%21%21",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/SNOWEX/SNEX20_VPTS_Raw.001/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/SNOWEX/SNEX20_VPTS_Raw.001/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/data/data-access-tool/SNEX20_VPTS_Raw/versions/1/",
-                    "description": "Data Access link for ITSD project",
                     "@type": "dcat:Distribution",
+                    "description": "Data Access link for ITSD project",
+                    "downloadURL": "https://nsidc.org/data/data-access-tool/SNEX20_VPTS_Raw/versions/1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1997892310-NSIDC_ECS&pg%5B0%5D%5Bgsk%5D=-start_date&q=SNEX20_VPTS_Raw&m=38.35552775499695%21-113.57226562500001%215%211%210%210%2C2&tl=1596643552%214%21%21",
-                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1997892310-NSIDC_ECS&pg%5B0%5D%5Bgsk%5D=-start_date&q=SNEX20_VPTS_Raw&m=38.35552775499695%21-113.57226562500001%215%211%210%210%2C2&tl=1596643552%214%21%21",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/SNOWEX/SNEX20_VPTS_Raw.001/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/SNOWEX/SNEX20_VPTS_Raw.001/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/data/data-access-tool/SNEX20_VPTS_Raw/versions/1/",
-                    "description": "Data Access link for ITSD project",
                     "@type": "dcat:Distribution",
+                    "description": "Data Access link for ITSD project",
+                    "downloadURL": "https://nsidc.org/data/data-access-tool/SNEX20_VPTS_Raw/versions/1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1997892310-NSIDC_ECS&pg%5B0%5D%5Bgsk%5D=-start_date&q=SNEX20_VPTS_Raw&m=38.35552775499695%21-113.57226562500001%215%211%210%210%2C2&tl=1596643552%214%21%21",
-                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1997892310-NSIDC_ECS&pg%5B0%5D%5Bgsk%5D=-start_date&q=SNEX20_VPTS_Raw&m=38.35552775499695%21-113.57226562500001%215%211%210%210%2C2&tl=1596643552%214%21%21",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/SNOWEX/SNEX20_VPTS_Raw.001/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/SNOWEX/SNEX20_VPTS_Raw.001/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/data/data-access-tool/SNEX20_VPTS_Raw/versions/1/",
-                    "description": "Data Access link for ITSD project",
                     "@type": "dcat:Distribution",
+                    "description": "Data Access link for ITSD project",
+                    "downloadURL": "https://nsidc.org/data/data-access-tool/SNEX20_VPTS_Raw/versions/1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1997892310-NSIDC_ECS&pg%5B0%5D%5Bgsk%5D=-start_date&q=SNEX20_VPTS_Raw&m=38.35552775499695%21-113.57226562500001%215%211%210%210%2C2&tl=1596643552%214%21%21",
-                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1997892310-NSIDC_ECS&pg%5B0%5D%5Bgsk%5D=-start_date&q=SNEX20_VPTS_Raw&m=38.35552775499695%21-113.57226562500001%215%211%210%210%2C2&tl=1596643552%214%21%21",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/SNOWEX/SNEX20_VPTS_Raw.001/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/SNOWEX/SNEX20_VPTS_Raw.001/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/data/data-access-tool/SNEX20_VPTS_Raw/versions/1/",
-                    "description": "Data Access link for ITSD project",
                     "@type": "dcat:Distribution",
+                    "description": "Data Access link for ITSD project",
+                    "downloadURL": "https://nsidc.org/data/data-access-tool/SNEX20_VPTS_Raw/versions/1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/9HYQMFZP4ALB",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/9HYQMFZP4ALB",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/9HYQMFZP4ALB",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/9HYQMFZP4ALB",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C1997892310-NSIDC_ECS",
+            "issued": "2020-02-05",
+            "keyword": [
+                "snow/ice",
+                "earth science",
+                "terrestrial hydrosphere"
+            ],
+            "landingPage": "https://doi.org/10.5067/9HYQMFZP4ALB",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2020-02-12",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA NSIDC DAAC"
+            },
             "spatial": "-108.215629 39.006 -108.17523 39.036349",
+            "temporal": "2020-02-05T00:00:00Z/2020-02-12T23:59:59.999Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "SnowEx20 Raw Near Surface Snow Temperature Profile Time Series V001"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://c3.nasa.gov/dashlink/resources/781/",
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
-            "identifier": "DASHLINK_781",
             "description": "A remaining useful life prediction algorithm and degradation model for electrolytic capacitors is presented. Electrolytic capacitors are used in several applications ranging from power supplies on critical avionics equipment to power drivers for electro-mechanical actuators. These devices are known for their low reliability and given their criticality in electronics subsystems they are a good candidate for component level prognostics and health management research. Prognostics provides a way to assess remaining useful life of a capacitor based on its current state of health and its anticipated future usage and operational conditions. In particular, experimental results of an accelerated aging test under electrical stresses are presented. The capacitors used in this test form the basis for a remaining life prediction algorithm where a model of the degradation process is suggested. This preliminary remaining life prediction algorithm serves as a demonstration of how prognostics methodologies could be used for electrolytic capacitors.",
-            "title": "Towards Prognostics of Electrolytic Capacitors",
-            "programCode": [
-                "026:029"
-            ],
             "distribution": [
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/publication/2011_AIAATowardsCapacitors.pdf",
-                    "description": "2011_AIAATowardsCapacitors.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "2011_AIAATowardsCapacitors.pdf",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/publication/2011_AIAATowardsCapacitors.pdf",
+                    "mediaType": "application/pdf",
                     "title": "2011_AIAATowardsCapacitors.pdf"
                 }
             ],
-            "accrualPeriodicity": "irregular"
+            "identifier": "DASHLINK_781",
+            "issued": "2013-06-19",
+            "keyword": [
+                "ames",
+                "dashlink",
+                "nasa"
+            ],
+            "landingPage": "https://c3.nasa.gov/dashlink/resources/781/",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:029"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Dashlink"
+            },
+            "title": "Towards Prognostics of Electrolytic Capacitors"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-3-RDR-RIVKIN-THREE-MICRON-V1.0",
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
+            "description": "This data set includes 3-micron spectra of asteroids taken by Andy Rivkin (1995) [RIVKINETAL1995]. The spectra include both measured reflectance and error bars at six points in the range 1.25-3.35 microns. 17 spectra of 16 different asteroids are included.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-3-rdr-rivkin-three-micron-v1.0_667i-4gu9",
+            "issued": "2018-06-26",
+            "keyword": [
+                "asteroid",
+                "support archives"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-3-RDR-RIVKIN-THREE-MICRON-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-3-rdr-rivkin-three-micron-v1.0_667i-4gu9",
-            "description": "This data set includes 3-micron spectra of asteroids taken by Andy Rivkin (1995) [RIVKINETAL1995]. The spectra include both measured reflectance and error bars at six points in the range 1.25-3.35 microns. 17 spectra of 16 different asteroids are included.",
-            "title": "RIVKIN THREE MICRON ASTEROID DATA V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "RIVKIN THREE MICRON ASTEROID DATA V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://c3.nasa.gov/dashlink/resources/39/",
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
                 "fn": "Elizabeth Foughty",
                 "hasEmail": "mailto:elizabeth.a.foughty@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Dashlink"
-            },
-            "identifier": "DASHLINK_39",
             "description": "The land remote sensing community has a long history of using supervised and unsupervised methods to help interpret and analyze remote sensing data sets. Until relatively recently, most remote sensing studies have used fairly conventional image processing and pattern recognition methodologies. In the past decade, NASA has launched a series of remote sensing missions known as the Earth Observing System (EOS). The data sets acquired by EOS instruments provide an extremely rich source of information related to the properties and dynamics of the Earth\u2019s terrestrial ecosystems. However, these data are also characterized by large volumes and complex spectral, spatial and temporal attributes. Because of the volume and complexity of EOS data sets, efficient and effective analysis of them presents significant challenges that are difficult to address using conventional remote sensing approaches. In this paper we discuss results from applying a variety of different data mining approaches to global remote sensing data sets. Specifically, we describe three main problem domains and sets of analyses: (1) supervised classification of global land cover from using data from NASA\u2019s Moderate Resolution Imaging Spectroradiometer; (2) the use of linear and non-linear cluster and dimensionality reduction methods to examine coupled climate-vegetation dynamics using a twenty year time series of data from the Advanced Very High Resolution Radiometer; and (3) the use of functional models, non-parametric clustering, and mixture models to help interpret and understand the feature space and class structure of high dimensional remote sensing data sets. The paper will not focus on specific details of algorithms. Instead we describe key results, successes, and lessons learned from ten years of research focusing on the use of data mining and machine learning methods for remote sensing and Earth science problems.",
-            "title": "Friedl presentation at CIDU",
-            "programCode": [
-                "026:029"
-            ],
             "distribution": [
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/CIDU_08_friedl.pdf",
-                    "description": "CIDU_08_friedl.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "CIDU_08_friedl.pdf",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/CIDU_08_friedl.pdf",
+                    "mediaType": "application/pdf",
                     "title": "CIDU_08_friedl.pdf"
                 }
             ],
-            "accrualPeriodicity": "irregular"
+            "identifier": "DASHLINK_39",
+            "issued": "2010-09-10",
+            "keyword": [
+                "nasa",
+                "ames",
+                "dashlink"
+            ],
+            "landingPage": "https://c3.nasa.gov/dashlink/resources/39/",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:029"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Dashlink"
+            },
+            "title": "Friedl presentation at CIDU"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/EPIC/DSCOVR/L2_TO3_03",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2017-09-12. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/EPIC/DSCOVR/L2_TO3_03.",
-            "issued": "2017-06-06",
-            "temporal": "2015-06-16T00:00:00Z/2022-01-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2017-06-06",
-            "keyword": [
-                "atmosphere",
-                "earth science",
-                "atmospheric radiation",
-                "atmospheric chemistry"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Natalya Kramarova",
                 "hasEmail": "mailto:natalya.a.kramarova@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/LARC/SD/ASDC"
-            },
-            "identifier": "C1990753071-LARC_ASDC",
             "description": "DSCOVR_EPIC_L2_TO3_v03 is Level2 Total Ozone derived from the Deep Space Climate Observatory (DSCOVR) Earth Polychromatic Imaging Camera (EPIC) using Level 1b version 3 inputs and version 3 ozone retrieval algorithm. The measurements from four EPIC UV channels are used to derive the global distributions of total ozone over the entire sunlit portion of the Earth. A new soft calibration technique developed based on scene matching with OMPS gives calibrated EPIC radiances. The calibrated EPIC radiances are used to derive science-quality total ozone products from EPIC that are consistent with those from other UV instruments. The retrieval algorithm uses wavelength triplets and assumes that the scene reflectivity changes linearly with wavelength. Version 3 algorithm includes several key modifications aimed to improve total ozone retrievals: a) switch to Version 3 Level 1b product with improved geolocation registration, flat field and dark counts corrections; b) replace OMI based cloud height climatology with the simultaneous EPIC A-Band cloud height; c) update absolute calibrations using polar orbiting SNPP OMPS; d) add corrections for ozone profile shape and temperature; e) update algorithm and error flags to filter data; f) add column weighting functions for each observation to facilitate error analysis. EPIC ozone retrievals accurately capture short term synoptic changes in total column ozone. With EPIC measurements from DSCOVR's vantage point synoptic ozone maps can be derived every 1-2 hours. Scene Reflectivity (clouds, aerosols, and surface) is derived as part of the ozone retrieval. The scene reflectivity in conjunction with ozone has been used to derive the amount of UV solar radiation reaching the ground, and surface UV Erythemal is also reported in these files.",
-            "title": "DSCOVR EPIC Level 2 Total Ozone, Version 3",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FEPIC%2FDSCOVR%2FL2_TO3_03",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FEPIC%2FDSCOVR%2FL2_TO3_03",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://epic.gsfc.nasa.gov/science/products/o3",
-                    "description": "EPIC O3 Product Overview",
                     "@type": "dcat:Distribution",
+                    "description": "EPIC O3 Product Overview",
+                    "downloadURL": "https://epic.gsfc.nasa.gov/science/products/o3",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/EPIC/DSCOVR/L2_TO3_03",
-                    "description": "DOI data set landing page for DSCOVR_EPIC_L2_TO3_03",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for DSCOVR_EPIC_L2_TO3_03",
+                    "downloadURL": "https://doi.org/10.5067/EPIC/DSCOVR/L2_TO3_03",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
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
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1990753071-LARC_ASDC",
-                    "description": "Earthdata Search for DSCOVR_EPIC_L2_TO3_03 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for DSCOVR_EPIC_L2_TO3_03 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1990753071-LARC_ASDC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/DSCOVR/EPIC/L2_TO3_03/",
-                    "description": "ASDC Direct Data Download for DSCOVR_EPIC_L2_TO3_03",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for DSCOVR_EPIC_L2_TO3_03",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/DSCOVR/EPIC/L2_TO3_03/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/DSCOVR/EPIC/L2_TO3_03/contents.html",
-                    "description": "OPeNDAP data access for DSCOVR_EPIC_L2_TO3_03",
                     "@type": "dcat:Distribution",
+                    "description": "OPeNDAP data access for DSCOVR_EPIC_L2_TO3_03",
+                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/DSCOVR/EPIC/L2_TO3_03/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 }
             ],
+            "identifier": "C1990753071-LARC_ASDC",
+            "issued": "2017-06-06",
+            "keyword": [
+                "atmosphere",
+                "earth science",
+                "atmospheric radiation",
+                "atmospheric chemistry"
+            ],
+            "landingPage": "https://doi.org/10.5067/EPIC/DSCOVR/L2_TO3_03",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2017-06-06",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/LARC/SD/ASDC"
+            },
             "spatial": "<?xml version=\"1.0\" encoding=\"UTF-8\"?><gml:Polygon xmlns:gml=\"http://www.opengis.net/gml/3.2\" srsName=\"EPSG:9825\"><gml:outerBoundaryIs><gml:LinearRing><gml:posList>-90.0 -180.0 -90.0 180.0 90.0 180.0 90.0 -180.0 -90.0 -180.0</gml:posList></gml:LinearRing></gml:outerBoundaryIs><gml:innerBoundaryIs></gml:innerBoundaryIs></gml:Polygon>",
+            "temporal": "2015-06-16T00:00:00Z/2022-01-17T00:00:00Z",
             "theme": [
                 "DSCOVR",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "DSCOVR EPIC Level 2 Total Ozone, Version 3"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-3-ESC1-67PCHURYUMOV-M12-V2.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This data set contains images acquired by the OSIRIS Narrow Angle Camera during the COMET ESCORT 1 phase of the Rosetta mission at the comet 67P, covering the period from 2015-01-13T23:25:00.000 to 2015-02-10T23:24:59.000. This version V2.0 supersedes previous deliveries of the same dataset.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-3-esc1-67pchuryumov-m12-v2.0",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2021-05-21",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "67p/churyumov-gerasimenko 1 (1969 r1)",
                 "international rosetta mission",
                 "vega"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-3-ESC1-67PCHURYUMOV-M12-V2.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-3-esc1-67pchuryumov-m12-v2.0",
-            "description": "This data set contains images acquired by the OSIRIS Narrow Angle Camera during the COMET ESCORT 1 phase of the Rosetta mission at the comet 67P, covering the period from 2015-01-13T23:25:00.000 to 2015-02-10T23:24:59.000. This version V2.0 supersedes previous deliveries of the same dataset.",
-            "title": "ROSETTA-ORBITER COMET ESCORT 1 OSINAC 3 RDR MTP012 V2.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER COMET ESCORT 1 OSINAC 3 RDR MTP012 V2.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/VIIRS/VJ143MA4.002",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Crystal Schaaf, Zhuosen Wang, Angela Erb, Ian Paynter\r\n. 2024-10-31. VIIRS/JPSS1 BRDF/Albedo Nadir BRDF-Adjusted Ref Daily L3 Global 1km SIN Grid V002. Version 002. Sioux Falls, South Dakota, USA. Archived by National Aeronautics and Space Administration, U.S. Government, NASA EOSDIS Land Processes Distributed Active Archive Center. https://doi.org/10.5067/VIIRS/VJ143MA4.002. https://doi.org/10.5067/VIIRS/VJ143MA4.002. This data set was provided by the NASA/NOAA NPP Project. The DOI landing page provides citations in APA and Chicago styles.\r\n.",
-            "issued": "2024-10-31",
-            "temporal": "2018-01-01T00:00:00Z/2024-11-04T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-10-31",
-            "keyword": [
-                "land surface",
-                "surface radiative properties",
-                "earth science"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Zhuosen Wang",
                 "hasEmail": "mailto:zhuosen.wang@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "LP DAAC"
-            },
-            "identifier": "C2545310943-LPCLOUD",
-            "description": "The NOAA-20 Visible Infrared Imaging Radiometer Suite (VIIRS) Nadir Bidirectional Reflectance Distribution Function (BRDF) Adjusted Reflectance (NBAR) Version 2 product provides NBAR estimates at 1 kilometer (km) resolution. The VJ143IA4 product is produced daily using 16-day VIIRS data and is weighted temporally to the 9th day, which is reflected in the file name. The view angle effects are removed from the directional reflectances resulting in a stable and consistent NBAR product. The VJ143 data products are designed after the Moderate Resolution Imaging Spectroradiometer (MODIS) BRDF/Albedo product suite to promote the continuity of the Earth Observation System (EOS) mission. The VJ143 data products are designed to promote the continuity of NASA\u2019s Moderate Resolution Imaging Spectroradiometer (MODIS) BRDF/Albedo data product suite.\r\n\r\nThe VJ143 algorithm uses the RossThick/Li-Sparse-Reciprocal (RTLSR) semi-empirical kernel-driven BRDF model, with the three kernel weights from VJ143MA1 to reconstruct surface anisotropic effects, correcting the directional reflectance to a common view geometry (VJ143MA4), while also computing integrated black-sky albedo (BSA) at local solar noon and white-sky albedo (WSA) (VJ143MA3). Researchers can use the BRDF model parameters with a simple polynomial, to obtain black-sky albedo at any solar illumination angle. Likewise, both the BSA and WSA Science Dataset (SDS) layers can be used with a simple polynomial, to manually estimate instantaneous actual albedo (blue-sky albedo). Additional details regarding the methodology are available in the Algorithm Theoretical Basis Document (ATBD).\r\n\r\nThe VJ143MA4 product includes 18 SDS layers for BRDF/Albedo mandatory quality and nadir reflectance for VIIRS nine moderate bands M1-M5, M7-M8, and M10-M11. A low-resolution browse image is also available showing NBAR bands M5, M7, and M5 as an RGB image in JPEG format.",
-            "release-place": "Sioux Falls, South Dakota, USA",
-            "graphic-preview-description": "Browse image for Earthdata Search",
             "creator": "Crystal Schaaf, Zhuosen Wang, Angela Erb, Ian Paynter",
-            "title": "VIIRS/JPSS1 BRDF/Albedo Nadir BRDF-Adjusted Ref Daily L3 Global 1km SIN Grid V002",
-            "graphic-preview-file": "https://data.lpdaac.earthdatacloud.nasa.gov/lp-prod-public/VJ143MA4.002/VJ143MA4.A2024294.h11v05.002.2024302063644/BROWSE.VJ143MA4.A2024294.h11v05.002.2024302063644.1.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The NOAA-20 Visible Infrared Imaging Radiometer Suite (VIIRS) Nadir Bidirectional Reflectance Distribution Function (BRDF) Adjusted Reflectance (NBAR) Version 2 product provides NBAR estimates at 1 kilometer (km) resolution. The VJ143IA4 product is produced daily using 16-day VIIRS data and is weighted temporally to the 9th day, which is reflected in the file name. The view angle effects are removed from the directional reflectances resulting in a stable and consistent NBAR product. The VJ143 data products are designed after the Moderate Resolution Imaging Spectroradiometer (MODIS) BRDF/Albedo product suite to promote the continuity of the Earth Observation System (EOS) mission. The VJ143 data products are designed to promote the continuity of NASA\u2019s Moderate Resolution Imaging Spectroradiometer (MODIS) BRDF/Albedo data product suite.\r\n\r\nThe VJ143 algorithm uses the RossThick/Li-Sparse-Reciprocal (RTLSR) semi-empirical kernel-driven BRDF model, with the three kernel weights from VJ143MA1 to reconstruct surface anisotropic effects, correcting the directional reflectance to a common view geometry (VJ143MA4), while also computing integrated black-sky albedo (BSA) at local solar noon and white-sky albedo (WSA) (VJ143MA3). Researchers can use the BRDF model parameters with a simple polynomial, to obtain black-sky albedo at any solar illumination angle. Likewise, both the BSA and WSA Science Dataset (SDS) layers can be used with a simple polynomial, to manually estimate instantaneous actual albedo (blue-sky albedo). Additional details regarding the methodology are available in the Algorithm Theoretical Basis Document (ATBD).\r\n\r\nThe VJ143MA4 product includes 18 SDS layers for BRDF/Albedo mandatory quality and nadir reflectance for VIIRS nine moderate bands M1-M5, M7-M8, and M10-M11. A low-resolution browse image is also available showing NBAR bands M5, M7, and M5 as an RGB image in JPEG format.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FVIIRS%2FVJ143MA4.002",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FVIIRS%2FVJ143MA4.002",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "application/x-hdf5",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=C2545310943-LPCLOUD",
-                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=C2545310943-LPCLOUD",
+                    "mediaType": "application/x-hdf5",
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
-                    "downloadURL": "https://doi.org/10.5067/VIIRS/VJ143MA4.002",
-                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
+                    "downloadURL": "https://doi.org/10.5067/VIIRS/VJ143MA4.002",
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
-                    "downloadURL": "https://www.umb.edu/spectralmass/viirs-user-guides-c1-and-c2/vnp43ia4-and-vnpma4-nbar-products/",
-                    "description": "The technical information in the User's Guide enables users to interpret and use the data products.",
                     "@type": "dcat:Distribution",
+                    "description": "The technical information in the User's Guide enables users to interpret and use the data products.",
+                    "downloadURL": "https://www.umb.edu/spectralmass/viirs-user-guides-c1-and-c2/vnp43ia4-and-vnpma4-nbar-products/",
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
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://data.lpdaac.earthdatacloud.nasa.gov/lp-prod-public/VJ143MA4.002/VJ143MA4.A2024294.h11v05.002.2024302063644/BROWSE.VJ143MA4.A2024294.h11v05.002.2024302063644.1.jpg",
-                    "description": "Browse image for Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse image for Earthdata Search",
+                    "downloadURL": "https://data.lpdaac.earthdatacloud.nasa.gov/lp-prod-public/VJ143MA4.002/VJ143MA4.A2024294.h11v05.002.2024302063644/BROWSE.VJ143MA4.A2024294.h11v05.002.2024302063644.1.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://viirsland.gsfc.nasa.gov/Val/Albedo_Val.html",
-                    "description": "Validation at stage 3 has been achieved for the VIIRS BRDF/Albedo product suite.",
                     "@type": "dcat:Distribution",
+                    "description": "Validation at stage 3 has been achieved for the VIIRS BRDF/Albedo product suite.",
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
+            "graphic-preview-description": "Browse image for Earthdata Search",
+            "graphic-preview-file": "https://data.lpdaac.earthdatacloud.nasa.gov/lp-prod-public/VJ143MA4.002/VJ143MA4.A2024294.h11v05.002.2024302063644/BROWSE.VJ143MA4.A2024294.h11v05.002.2024302063644.1.jpg",
+            "identifier": "C2545310943-LPCLOUD",
+            "issued": "2024-10-31",
+            "keyword": [
+                "land surface",
+                "surface radiative properties",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/VIIRS/VJ143MA4.002",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2024-10-31",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "LP DAAC"
+            },
+            "release-place": "Sioux Falls, South Dakota, USA",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2018-01-01T00:00:00Z/2024-11-04T00:00:00Z",
             "theme": [
                 "JPSS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "VIIRS/JPSS1 BRDF/Albedo Nadir BRDF-Adjusted Ref Daily L3 Global 1km SIN Grid V002"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/GPMGV/MC3E/PROFILER/DATA101",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Williams, Christopher.2012. GPM GROUND VALIDATION NOAA UHF 449 PROFILER MC3E [indicate subset used]. Dataset available online from the NASA Global Hydrometeorology Resource Center DAAC, Huntsville, Alabama, U.S.A. DOI: http://dx.doi.org/10.5067/GPMGV/MC3E/PROFILER/DATA101",
-            "issued": "2012-09-11",
-            "temporal": "2011-04-08T16:00:11Z/2011-06-07T13:50:51Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-05-24",
-            "keyword": [
-                "radar",
-                "atmospheric winds",
-                "earth science",
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
-            "identifier": "C1979827921-GHRC_DAAC",
             "description": "The GPM Ground Validation NOAA UHF 449 Profiler MC3E dataset was collected during the NASA supported Midlatitude Continental Convective Clouds Experiment (MC3E). The overarching goal was to provide the most complete characterization of convective cloud systems, precipitation, and the environment that has ever been obtained, providing constraints for model cumulus parameterizations and space-based rainfall retrieval algorithms over land that had never before been available. The Ultra High Frequency 449 MHz profiler was one of three NOAA deployed instruments which also included a Parsivel and a 2.8 GHz profiler (S-Band). The 449 MHz profiler raw data files provide estimates of the vertical air motion during precipitation from near the surface to just below the freezing level. Used together with the S-band profiler, vertical profiles of raindrop size distributions can be retrieved. The raw 449MGx profiler data consists of uncalibrated Doppler velocity spectra data in units of relative power return.",
-            "graphic-preview-description": "N/A",
-            "title": "GPM GROUND VALIDATION NOAA UHF 449 PROFILER MC3E V1",
-            "graphic-preview-file": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/mc3e/profiler/uhf449/browse/",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGPMGV%2FMC3E%2FPROFILER%2FDATA101",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGPMGV%2FMC3E%2FPROFILER%2FDATA101",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=gpmuhfnoaamc3e",
-                    "description": "Files may be downloaded directly to your workstation from this link",
                     "@type": "dcat:Distribution",
+                    "description": "Files may be downloaded directly to your workstation from this link",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=gpmuhfnoaamc3e",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/browse_sample/fieldCampaigns/gpmValidation/mc3e/gpmuhfnoaamc3e/MC3E_449MHzSpectra_2.8GHzSpectra_20110520_061023.jpg",
-                    "description": "Sample browse image",
                     "@type": "dcat:Distribution",
+                    "description": "Sample browse image",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/browse_sample/fieldCampaigns/gpmValidation/mc3e/gpmuhfnoaamc3e/MC3E_449MHzSpectra_2.8GHzSpectra_20110520_061023.jpg",
+                    "mediaType": "image/jpeg",
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
-                    "downloadURL": "http://ghrc.nsstc.nasa.gov/uso/ds_docs/gpmgv/mc3e/gpmuhf449mc3e/gpm_noaa_uhf449_mc3e.html",
-                    "description": "The guide document contains detailed information about the dataset",
                     "@type": "dcat:Distribution",
+                    "description": "The guide document contains detailed information about the dataset",
+                    "downloadURL": "http://ghrc.nsstc.nasa.gov/uso/ds_docs/gpmgv/mc3e/gpmuhf449mc3e/gpm_noaa_uhf449_mc3e.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "http://ghrc.nsstc.nasa.gov/uso/ds_docs/gpmgv/mc3e/gpmuhf449mc3e/Profiler_MC3E_Data_Description_2012_08_29v2.pdf",
-                    "description": "Description of Data Collected by the NOAA 449-MHz and 2.8-GHz Profilers during the Mid-latitude Continental Convective Cloud Experiment (MC3E) 22 April \u00bf\u00bf\u00bf 6 June 2011 (TEXT)",
                     "@type": "dcat:Distribution",
+                    "description": "Description of Data Collected by the NOAA 449-MHz and 2.8-GHz Profilers during the Mid-latitude Continental Convective Cloud Experiment (MC3E) 22 April \u00bf\u00bf\u00bf 6 June 2011 (TEXT)",
+                    "downloadURL": "http://ghrc.nsstc.nasa.gov/uso/ds_docs/gpmgv/mc3e/gpmuhf449mc3e/Profiler_MC3E_Data_Description_2012_08_29v2.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View the primary investigator's documentation for this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://ghrc.nsstc.nasa.gov/uso/ds_docs/gpmgv/mc3e/gpmuhf449mc3e/Profiler_MC3E_Data_Description_2012_08_29v2.docx",
-                    "description": "Description of Data Collected by the NOAA 449-MHz and 2.8-GHz Profilers during the Mid-latitude Continental Convective Cloud Experiment (MC3E) 22 April-6 June 2011 (DOCUMENT)",
                     "@type": "dcat:Distribution",
+                    "description": "Description of Data Collected by the NOAA 449-MHz and 2.8-GHz Profilers during the Mid-latitude Continental Convective Cloud Experiment (MC3E) 22 April-6 June 2011 (DOCUMENT)",
+                    "downloadURL": "http://ghrc.nsstc.nasa.gov/uso/ds_docs/gpmgv/mc3e/gpmuhf449mc3e/Profiler_MC3E_Data_Description_2012_08_29v2.docx",
+                    "mediaType": "text/html",
                     "title": "View the primary investigator's documentation for this dataset"
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
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/mc3e/profiler/uhf449/browse/",
-                    "description": "N/A",
                     "@type": "dcat:Distribution",
+                    "description": "N/A",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/mc3e/profiler/uhf449/browse/",
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
+            "graphic-preview-file": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/mc3e/profiler/uhf449/browse/",
+            "identifier": "C1979827921-GHRC_DAAC",
+            "issued": "2012-09-11",
+            "keyword": [
+                "radar",
+                "atmospheric winds",
+                "earth science",
+                "atmosphere",
+                "spectral/engineering"
+            ],
+            "landingPage": "https://doi.org/10.5067/GPMGV/MC3E/PROFILER/DATA101",
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
             "spatial": "-97.491 36.599 -97.489 36.601",
+            "temporal": "2011-04-08T16:00:11Z/2011-06-07T13:50:51Z",
             "theme": [
                 "MC3E",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "GPM GROUND VALIDATION NOAA UHF 449 PROFILER MC3E V1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=DIF-M-MRI-3%2F4-EPOXI-MARS-V1.0",
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
-                "epoxi",
-                "mars"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This data set contains calibrated 750-nm filter images of Mars acquired by the Deep Impact Medium Resolution Visible CCD (MRI) for the EPOCh project during the second cruise phase of the EPOXI mission. One set of observations was acquired on 20-21 November 2009 to characterize Mars as an analog for extrasolar planets. The observing period lasted approximately 24 hours, and one MRI image was taken simultaneously with the first north/south scan of the HRI IR spectrometer at half-hour intervals to provide context for the spectral scans.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.dif-m-mri-3-4-epoxi-mars-v1.0_66cz-59ca",
+            "issued": "2018-06-26",
+            "keyword": [
+                "epoxi",
+                "mars"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=DIF-M-MRI-3%2F4-EPOXI-MARS-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.dif-m-mri-3-4-epoxi-mars-v1.0_66cz-59ca",
-            "description": "This data set contains calibrated 750-nm filter images of Mars acquired by the Deep Impact Medium Resolution Visible CCD (MRI) for the EPOCh project during the second cruise phase of the EPOXI mission. One set of observations was acquired on 20-21 November 2009 to characterize Mars as an analog for extrasolar planets. The observing period lasted approximately 24 hours, and one MRI image was taken simultaneously with the first north/south scan of the HRI IR spectrometer at half-hour intervals to provide context for the spectral scans.",
-            "title": "EPOXI MARS OBS - MRI CALIBRATED IMAGES V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "EPOXI MARS OBS - MRI CALIBRATED IMAGES V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/DORIS/DORIS_IDSGLOBALSNX_001",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/GSFC/SED/ESD/GGL/CDDIS. https://doi.org/10.5067/DORIS/DORIS_IDSGLOBALSNX_001.",
-            "issued": "1993-01-01",
-            "temporal": "1992-01-01T00:00:00Z/2022-06-20T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2021-09-14",
-            "keyword": [
-                "solid earth",
-                "tectonics",
-                "geodetics",
-                "gravity/gravitational field",
-                "earth science"
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
-            "identifier": "C1544926300-CDDIS",
             "description": "Doppler Orbitography and Radiopositioning Integrated by Satellite (DORIS) Cumulative Station Position Product from the NASA Crustal Dynamics Data Information System (CDDIS). DORIS is a dual-frequency Doppler system consisting of a receiver flying aboard a satellite and a globally distributed network of ground beacons. The DORIS receiver on-board the orbiting satellite tracks the dual-frequency radio signals transmitted by the network of ground beacons and generates the DORIS data. A measurement is made of either the Doppler shift or absolute phase as the satellite\u2019s orbit moves over the ground-based beacon. DORIS data records contain a time-tagged range-rate measurement with associated ancillary information. DORIS observations from a global network can be utilized for a variety of products. Analysis Centers (ACs) of the International DORIS Service (IDS) retrieve DORIS data on a regular basis to compute station position solutions for the DORIS beacons supporting the IDS network. The IDS Analysis Center Coordinator combines these individual AC solutions to generate a long-term DORIS position and velocity cumulative solution through a piecewise linear (position+velocity) model to describe the station motions. The cumulative position and velocity solution is obtained from the stacking of the weekly solution files and is then aligned to the current ITRF. The residuals of this stacking are of particular interest since they depict non-linear station motions.",
-            "title": "Ground-Based Doppler Orbitography and Radiopositioning Integrated by Satellite (DORIS) Cumulative Station Position Product from NASA CDDIS",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FDORIS%2FDORIS_IDSGLOBALSNX_001",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FDORIS%2FDORIS_IDSGLOBALSNX_001",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://cddis.nasa.gov/archive/doris/products/sinex_global/",
-                    "description": "URL for retrieval of DORIS products through https",
                     "@type": "dcat:Distribution",
+                    "description": "URL for retrieval of DORIS products through https",
+                    "downloadURL": "https://cddis.nasa.gov/archive/doris/products/sinex_global/",
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
-                    "downloadURL": "http://dx.doi.org/10.5067/DORIS/DORIS_IDSGLOBALSNX_001",
-                    "description": "URL for more information about DORIS products",
                     "@type": "dcat:Distribution",
+                    "description": "URL for more information about DORIS products",
+                    "downloadURL": "http://dx.doi.org/10.5067/DORIS/DORIS_IDSGLOBALSNX_001",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 }
             ],
+            "identifier": "C1544926300-CDDIS",
+            "issued": "1993-01-01",
+            "keyword": [
+                "solid earth",
+                "tectonics",
+                "geodetics",
+                "gravity/gravitational field",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/DORIS/DORIS_IDSGLOBALSNX_001",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2021-09-14",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GGL/CDDIS"
+            },
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "1992-01-01T00:00:00Z/2022-06-20T00:00:00Z",
             "theme": [
                 "IDS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Ground-Based Doppler Orbitography and Radiopositioning Integrated by Satellite (DORIS) Cumulative Station Position Product from NASA CDDIS"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RPCLAP-2-ESC4-MTP022-V2.0",
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
+            "description": "This data set contains\nEDITED data from Rosetta RPC-LAP, acquired during the COMET ESCORT 4\nMTP022 mission phase. Comet C-G/67P was the primary target.\nThis data set supersedes RO-C-RPCLAP-2-ESC4-MTP022-V1.0.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rpclap-2-esc4-mtp022-v2.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RPCLAP-2-ESC4-MTP022-V2.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rpclap-2-esc4-mtp022-v2.0",
-            "description": "This data set contains\nEDITED data from Rosetta RPC-LAP, acquired during the COMET ESCORT 4\nMTP022 mission phase. Comet C-G/67P was the primary target.\nThis data set supersedes RO-C-RPCLAP-2-ESC4-MTP022-V1.0.",
-            "title": "ROSETTA-ORBITER 67P RPCLAP 2\nESC4 MTP022 V2.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RPCLAP 2\nESC4 MTP022 V2.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/PT6TXZKSHBW9",
             "citation": "Watson Gregg and Cecile Rousseaux. Watson Gregg and Cecile Rousseaux. 2017-07-31. NOBM_DAY. Version R2017. NASA Ocean Biogeochemical Model assimilating satellite chlorophyll data global daily VR2017. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/PT6TXZKSHBW9. https://disc.gsfc.nasa.gov/datacollection/NOBM_DAY_R2017.html. Digital Science Data.",
-            "issued": "2017-07-08",
-            "temporal": "1998-01-01T00:00:00Z/2015-12-31T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2017-07-08",
-            "references": [
-                "https://doi.org/10.3390/rs6010001"
-            ],
-            "keyword": [
-                "protists",
-                "ocean temperature",
-                "oceans",
-                "ocean chemistry",
-                "ocean optics",
-                "earth science",
-                "biological classification"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Suhung Shen",
                 "hasEmail": "mailto:suhung.shen@nasa.gov"
             },
+            "creator": "Watson Gregg and Cecile Rousseaux",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C1404080675-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "This is the assimilated daily data from NASA Ocean Biogeochemical Model (NOBM).  The NOBM is a comprehensive, interactive ocean biogeochemical model coupled with a circulation and radiative model in the global oceans (Gregg and Casey, 2007). It spans the domain from -84 to 72 degree latitude in increments of 1.25 degree longitude by 2/3 degree latitude, including only open ocean areas where bottom depth > 200m. NOBM contains 4 phytoplankton groups, 4 nutrient groups, a single herbivore group, and 3 detrital pools, and the major ocean carbon components, dissolved organic and inorganic carbon (DOC and DIC).",
-            "editor": "Watson Gregg and Cecile Rousseaux",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "NOBM_DAY",
-            "creator": "Watson Gregg and Cecile Rousseaux",
-            "graphic-preview-description": "The GES-DISC Interactive Online Visualization ANd aNalysis Interface (Giovanni) is a web-based tool that allows users to interactively visualize and analyze data.",
-            "title": "NASA Ocean Biogeochemical Model assimilating satellite chlorophyll data global daily VR2017 (NOBM_DAY) at GES DISC",
-            "graphic-preview-file": "https://giovanni.gsfc.nasa.gov/giovanni/#dataKeyword=NOBM_DAY",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FPT6TXZKSHBW9",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FPT6TXZKSHBW9",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/NOBM/NOBM_DAY.R2017.sample.20150101.png",
-                    "description": "Sample image of daily assimilated total chlorophyll [mg m-3] from the NASA Ocean Biogeochemical Model  (NOBM_DAY.R2017), Jan 1 2015",
                     "@type": "dcat:Distribution",
+                    "description": "Sample image of daily assimilated total chlorophyll [mg m-3] from the NASA Ocean Biogeochemical Model  (NOBM_DAY.R2017), Jan 1 2015",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/NOBM/NOBM_DAY.R2017.sample.20150101.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/NOBM_DAY_R2017.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/NOBM_DAY_R2017.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://reason.gesdisc.eosdis.nasa.gov/data/nobm/NOBM_DAY.R2017",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://reason.gesdisc.eosdis.nasa.gov/data/nobm/NOBM_DAY.R2017",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=NOBM_DAY",
-                    "description": "Use the Earthdata Search Client to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search Client to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=NOBM_DAY",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://reason.gesdisc.eosdis.nasa.gov/opendap/nobm/NOBM_DAY.R2017/contents.html",
-                    "description": "Access to the data via OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access to the data via OPeNDAP protocol.",
+                    "downloadURL": "https://reason.gesdisc.eosdis.nasa.gov/opendap/nobm/NOBM_DAY.R2017/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://giovanni.gsfc.nasa.gov/giovanni/#dataKeyword=NOBM_DAY",
-                    "description": "The GES-DISC Interactive Online Visualization ANd aNalysis Interface (Giovanni) is a web-based tool that allows users to interactively visualize and analyze data.",
                     "@type": "dcat:Distribution",
+                    "description": "The GES-DISC Interactive Online Visualization ANd aNalysis Interface (Giovanni) is a web-based tool that allows users to interactively visualize and analyze data.",
+                    "downloadURL": "https://giovanni.gsfc.nasa.gov/giovanni/#dataKeyword=NOBM_DAY",
+                    "mediaType": "text/html",
                     "title": "Get a related visualization through GIOVANNI"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://reason.gesdisc.eosdis.nasa.gov/data/nobm/NOBM_MON.R2017/doc/README_NOBM_R2017.pdf",
-                    "description": "README Document",
                     "@type": "dcat:Distribution",
+                    "description": "README Document",
+                    "downloadURL": "https://reason.gesdisc.eosdis.nasa.gov/data/nobm/NOBM_MON.R2017/doc/README_NOBM_R2017.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's read me document"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://gmao.gsfc.nasa.gov/research/oceanbiology/references.php",
-                    "description": "NASA GMAO NOBM Project documentation page",
                     "@type": "dcat:Distribution",
+                    "description": "NASA GMAO NOBM Project documentation page",
+                    "downloadURL": "https://gmao.gsfc.nasa.gov/research/oceanbiology/references.php",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/information/howto",
-                    "description": "Data recipes for accessing and using data",
                     "@type": "dcat:Distribution",
+                    "description": "Data recipes for accessing and using data",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/information/howto",
+                    "mediaType": "text/html",
                     "title": "View this dataset's how-to documentation"
                 }
             ],
+            "editor": "Watson Gregg and Cecile Rousseaux",
+            "graphic-preview-description": "The GES-DISC Interactive Online Visualization ANd aNalysis Interface (Giovanni) is a web-based tool that allows users to interactively visualize and analyze data.",
+            "graphic-preview-file": "https://giovanni.gsfc.nasa.gov/giovanni/#dataKeyword=NOBM_DAY",
+            "identifier": "C1404080675-GES_DISC",
+            "issued": "2017-07-08",
+            "keyword": [
+                "protists",
+                "ocean temperature",
+                "oceans",
+                "ocean chemistry",
+                "ocean optics",
+                "earth science",
+                "biological classification"
+            ],
+            "landingPage": "https://doi.org/10.5067/PT6TXZKSHBW9",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2017-07-08",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
+            },
+            "references": [
+                "https://doi.org/10.3390/rs6010001"
+            ],
+            "release-place": "Greenbelt, MD, USA",
+            "series-name": "NOBM_DAY",
             "spatial": "-180.0 -84.0 180.0 72.0",
+            "temporal": "1998-01-01T00:00:00Z/2015-12-31T23:59:59.999Z",
             "theme": [
                 "NOBM",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "NASA Ocean Biogeochemical Model assimilating satellite chlorophyll data global daily VR2017 (NOBM_DAY) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/Aura/MLS/DATA/3574",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Lambert, A., Livesey, N., Read, W., and Fuller, R.. 2021-04-29. ML3DZIWC. Version 005. MLS/Aura Level 3 Daily Binned Cloud Ice (IWC) on Zonal and Similar Grids V005. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/Aura/MLS/DATA/3574. https://disc.gsfc.nasa.gov/datacollection/ML3DZIWC_005.html. Digital Science Data.",
-            "issued": "2021-04-29",
-            "temporal": "2004-08-02T00:00:00Z/2022-01-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2021-04-29",
-            "keyword": [
-                "earth science",
-                "atmosphere",
-                "clouds"
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
-            "identifier": "C2042566860-GES_DISC",
-            "description": "ML3DZIWC is the EOS Aura Microwave Limb Sounder (MLS) daily binned on zonal and assorted vertical grids product for cloud ice water content (IWC) derived from radiances measured by the 240 GHz radiometer. The data version is 5.1. Spatial coverage is near-global (-82 to +82 degrees latitude) at 4 degree latitude zonal increments. The recommended useful vertical range is from 215 to 82.5 hPa, and the vertical resolution is about 3 km. Users of the ML3DZIWC data product should read chapter 4 and sections 3.15 and 3.16 of the EOS MLS Level 2 Version 5 Quality Document for more information.\n\nThe data files contain one year of data and are archived in the netCDF4 format, which is also compatible with HDF5 readers and tools. Each file contains four group objects: lat vs pressure zonal mean, lat vs \"potential temperature\" zonal mean, \"equivalent latitude\" vs \"potential temperature\" zonal mean, and vortex average vs \"potential temperature\". Each group has a set of data (average, min, max, std dev, rms) and geolocation fields, grid attributes, and metadata.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "ML3DZIWC",
             "creator": "Lambert, A., Livesey, N., Read, W., and Fuller, R.",
-            "title": "MLS/Aura Level 3 Daily Binned Cloud Ice (IWC) on Zonal and Similar Grids V005 (ML3DZIWC) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/ML3DZIWC_005.png",
-            "programCode": [
-                "026:001"
-            ],
+            "data-presentation-form": "Digital Science Data",
+            "description": "ML3DZIWC is the EOS Aura Microwave Limb Sounder (MLS) daily binned on zonal and assorted vertical grids product for cloud ice water content (IWC) derived from radiances measured by the 240 GHz radiometer. The data version is 5.1. Spatial coverage is near-global (-82 to +82 degrees latitude) at 4 degree latitude zonal increments. The recommended useful vertical range is from 215 to 82.5 hPa, and the vertical resolution is about 3 km. Users of the ML3DZIWC data product should read chapter 4 and sections 3.15 and 3.16 of the EOS MLS Level 2 Version 5 Quality Document for more information.\n\nThe data files contain one year of data and are archived in the netCDF4 format, which is also compatible with HDF5 readers and tools. Each file contains four group objects: lat vs pressure zonal mean, lat vs \"potential temperature\" zonal mean, \"equivalent latitude\" vs \"potential temperature\" zonal mean, and vortex average vs \"potential temperature\". Each group has a set of data (average, min, max, std dev, rms) and geolocation fields, grid attributes, and metadata.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAura%2FMLS%2FDATA%2F3574",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAura%2FMLS%2FDATA%2F3574",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
@@ -227625,116 +227603,118 @@
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/ML3DZIWC_005.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/ML3DZIWC_005.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/Aura_MLS_Level3/ML3DZIWC.005/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/Aura_MLS_Level3/ML3DZIWC.005/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/opendap/HDF-EOS5/Aura_MLS_Level3/ML3DZIWC.005/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/opendap/HDF-EOS5/Aura_MLS_Level3/ML3DZIWC.005/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=ML3DZIWC_005",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=ML3DZIWC_005",
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
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/ML3DZIWC_005.png",
+            "identifier": "C2042566860-GES_DISC",
+            "issued": "2021-04-29",
+            "keyword": [
+                "earth science",
+                "atmosphere",
+                "clouds"
+            ],
+            "landingPage": "https://doi.org/10.5067/Aura/MLS/DATA/3574",
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
+            "series-name": "ML3DZIWC",
             "spatial": "-180.0 -82.0 180.0 82.0",
+            "temporal": "2004-08-02T00:00:00Z/2022-01-17T00:00:00Z",
             "theme": [
                 "Aura",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "MLS/Aura Level 3 Daily Binned Cloud Ice (IWC) on Zonal and Similar Grids V005 (ML3DZIWC) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/AURA/TES/TESTL3CO2LM_L3",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2013-01-01. Archived by National Aeronautics and Space Administration, U.S. Government, ASDC. https://doi.org/10.5067/AURA/TES/TESTL3CO2LM_L3. http://eosweb.larc.nasa.gov/project/tes/tes_table.",
-            "issued": "2004-08-22",
-            "temporal": "2004-08-22T00:00:00Z/2024-12-23T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-12-18",
-            "keyword": [
-                "atmospheric chemistry",
-                "air quality",
-                "atmosphere",
-                "earth science"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "SCOTT GLUCK",
                 "hasEmail": "mailto:Scott.Gluck@jpl.nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "ASDC"
-            },
-            "identifier": "C189920635-LARC",
             "description": "The TES Aura L3 CO2 data consist of daily atmospheric temperature and VMR for the atmospheric species. Data are provided at 2 degree latitude X 4 degree longitude spatial grids and at a subset of TES standard pressure levels. The TES Science Data Processing L3 subsystem interpolates the L2 atmospheric profiles collected in a Global Survey onto a global grid uniform in latitude and longitude to provide a 3-D representation of the distribution of atmospheric gasses. Daily and monthly averages of L2 profiles and browse images are available. The L3 standard data products are composed of L3 HDF - EOS-EOS grid data. A separate product file is produced for each different atmospheric species. TES obtains data in two basic observation modes: Limb or Nadir. The product file may contain, in separate folders, limb data, nadir data, or both folders may be present. Specific to L3 processing are the terms Daily and Monthly representing the approximate time coverage of the L3 products. However, the input data granules to the L3 process are complete Global Surveys; in other words a Global Survey will not be split in relation to time when input to the L3 processes even if they exceed the usual understood meanings of a day or month. More specifically, Daily L3 products represent a single Global Survey (approximately 26 hours) and Monthly L3 products represent Global Surveys that are initiated within that calendar month. The data granules defined for L3 standard products are daily and monthly. Details of the format of this product can be found in the TES Data Products Specifications (DPS) which is available from the LaRC ASDC site: http://eosweb.larc.nasa.gov/project/tes/DPS",
-            "title": "TES/Aura L3 CO2 Lite Monthly Gridded V003",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAURA%2FTES%2FTESTL3CO2LM_L3",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAURA%2FTES%2FTESTL3CO2LM_L3",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
@@ -227774,34 +227754,56 @@
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/AURA/TES/TESTL3CO2LM_L3",
-                    "description": "DOI data set landing page for TL3CO2LM_3",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for TL3CO2LM_3",
+                    "downloadURL": "https://doi.org/10.5067/AURA/TES/TESTL3CO2LM_L3",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 }
             ],
+            "identifier": "C189920635-LARC",
+            "issued": "2004-08-22",
+            "keyword": [
+                "atmospheric chemistry",
+                "air quality",
+                "atmosphere",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/AURA/TES/TESTL3CO2LM_L3",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2024-12-18",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "ASDC"
+            },
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2004-08-22T00:00:00Z/2024-12-23T00:00:00Z",
             "theme": [
                 "TES",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "TES/Aura L3 CO2 Lite Monthly Gridded V003"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-P-LORRI-3-PLUTO-V3.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This data set contains Calibrated data taken by the New Horizons         Long Range Reconnaissance Imager                                       instrument during the                                                    Pluto encounter                                                        mission phase.  This is VERSION 3.0 of this data set.                    This data set contains LORRI observations taken during the               the Approach (Jan-Jul, 2015), Encounter, Departure, and                  Transition mission sub-phases, including flyby observations              taken on 14 July, 2015, and departure and calibration data               through late October, 2016. Departure observations include               a ring search of the Pluto system and 1994 JR1 observations.             This data set completes the Pluto mission phase deliveries for           LORRI.                                                                   This is version 3.0 of this dataset. Changes since version 2.0 include   the addition of data downlinked between the end of January, 2016 and the end of October, 2016, completing the delivery of all data covering the   Pluto Encounter and subsequent Calibration Campaign. It includes multi-  map observations from the Approach phase, observations of the moons, hi- res, full-frame observations from Pluto Encounter and Departure, sliver  maps, and ring search observations.  There may be some overlap between   prior datasets and this dataset, due to only partial, windowed, or lossy data in prior datasets.  Observations at closest approach to Pluto are   marked with _CA in the Request ID. This dataset also includes functional tests from the Calibration Campaign, including a regular observation of  NGC3532. Finally it includes the first set of distant KBO observations.  Also, updates were made to the calibration files, documentation, and     catalog files.                                                           There were minor changes to the level 2 LORRI calibration process, as    well as to the LORRI calibration constants for the final Pluto P3 PDS    delivery.                                                                The process change involves gap removal during calibration.  Files       with gaps come in many flavors, depending on where the gap lies within   the image. This update recognizes some additional possiblities, mainly   that the gap might be close to the bottom or top of the image (and       therefore the previous algorithm would fail because it filled the gap    with median pixel info from both above and below the gap). The new       algorithm will take the info from one side of the gap exclusively,       when appropriate.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-p-lorri-3-pluto-v3.0_66ks-cr8i",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "styx",
                 "calibration",
@@ -227812,131 +227814,108 @@
                 "hydra",
                 "charon"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-P-LORRI-3-PLUTO-V3.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-p-lorri-3-pluto-v3.0_66ks-cr8i",
-            "description": "This data set contains Calibrated data taken by the New Horizons         Long Range Reconnaissance Imager                                       instrument during the                                                    Pluto encounter                                                        mission phase.  This is VERSION 3.0 of this data set.                    This data set contains LORRI observations taken during the               the Approach (Jan-Jul, 2015), Encounter, Departure, and                  Transition mission sub-phases, including flyby observations              taken on 14 July, 2015, and departure and calibration data               through late October, 2016. Departure observations include               a ring search of the Pluto system and 1994 JR1 observations.             This data set completes the Pluto mission phase deliveries for           LORRI.                                                                   This is version 3.0 of this dataset. Changes since version 2.0 include   the addition of data downlinked between the end of January, 2016 and the end of October, 2016, completing the delivery of all data covering the   Pluto Encounter and subsequent Calibration Campaign. It includes multi-  map observations from the Approach phase, observations of the moons, hi- res, full-frame observations from Pluto Encounter and Departure, sliver  maps, and ring search observations.  There may be some overlap between   prior datasets and this dataset, due to only partial, windowed, or lossy data in prior datasets.  Observations at closest approach to Pluto are   marked with _CA in the Request ID. This dataset also includes functional tests from the Calibration Campaign, including a regular observation of  NGC3532. Finally it includes the first set of distant KBO observations.  Also, updates were made to the calibration files, documentation, and     catalog files.                                                           There were minor changes to the level 2 LORRI calibration process, as    well as to the LORRI calibration constants for the final Pluto P3 PDS    delivery.                                                                The process change involves gap removal during calibration.  Files       with gaps come in many flavors, depending on where the gap lies within   the image. This update recognizes some additional possiblities, mainly   that the gap might be close to the bottom or top of the image (and       therefore the previous algorithm would fail because it filled the gap    with median pixel info from both above and below the gap). The new       algorithm will take the info from one side of the gap exclusively,       when appropriate.",
-            "title": "NEW HORIZONS                            \n      LORRI PLUTO ENCOUNTER                                                   \n      CALIBRATED V3.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "NEW HORIZONS                            \n      LORRI PLUTO ENCOUNTER                                                   \n      CALIBRATED V3.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-J-SDC-2-JUPITER-V4.0",
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
+            "description": "This data set contains Raw data taken by the New Horizons                Student Dust Counter                                                   instrument during the                                                    Jupiter encounter                                                      mission phase.  This is VERSION 4.0 of this data set.                    For the Jupiter encounter mission phase, SDC collected no science        data during the Jupiter flyby, as the requisite spacecraft               configuration prevented SDC from operating.  There were some very        sparse data taken from December, 2006 through April, 2007, and           some of very short (or zero) duration after the Jupiter flyby from       April, 2007 through June, 2007.                                          The changes in Version 4.0 were re-running of the ancillary data         in the data product, updated geometry from newer SPICE kernels,          minor editing of the documentation, catalogs, etc., and resolution       of liens from the December, 2014 review, plus those from the May,        2016 review of the Pluto Encounter data sets.  No new observations       were added with Version 4.0.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-j-sdc-2-jupiter-v4.0_66mk-xvef",
+            "issued": "2021-05-21",
+            "keyword": [
+                "new horizons",
+                "dust"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-J-SDC-2-JUPITER-V4.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-j-sdc-2-jupiter-v4.0_66mk-xvef",
-            "description": "This data set contains Raw data taken by the New Horizons                Student Dust Counter                                                   instrument during the                                                    Jupiter encounter                                                      mission phase.  This is VERSION 4.0 of this data set.                    For the Jupiter encounter mission phase, SDC collected no science        data during the Jupiter flyby, as the requisite spacecraft               configuration prevented SDC from operating.  There were some very        sparse data taken from December, 2006 through April, 2007, and           some of very short (or zero) duration after the Jupiter flyby from       April, 2007 through June, 2007.                                          The changes in Version 4.0 were re-running of the ancillary data         in the data product, updated geometry from newer SPICE kernels,          minor editing of the documentation, catalogs, etc., and resolution       of liens from the December, 2014 review, plus those from the May,        2016 review of the Pluto Encounter data sets.  No new observations       were added with Version 4.0.",
-            "title": "NEW HORIZONS                            \n      SDC JUPITER ENCOUNTER                                                   \n      RAW V4.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "NEW HORIZONS                            \n      SDC JUPITER ENCOUNTER                                                   \n      RAW V4.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1410",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Chapin, E., S. Flores, L. Harcke, B.P. Hawkins, S. Hensley, T.R. Michel, R.J. Muellerschoen, J.G. Shimada, W.W. Tung, and C. Veeramachaneni. 2018. AirMOSS: L1 S-0 Polarimetric Data from AirMOSS P-band SAR, Howland Forest, 2012-2015. ORNL DAAC, Oak Ridge, Tennessee, USA. https://doi.org/10.3334/ORNLDAAC/1410",
-            "issued": "2018-04-25",
-            "temporal": "2012-10-15T00:00:00Z/2015-09-09T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-17",
-            "keyword": [
-                "spectral/engineering",
-                "radar",
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
-            "identifier": "C2274853415-ORNL_CLOUD",
             "description": "This data set provides level 1 (L1) polarimetric radar backscattering coefficient (sigma-0), multilook complex, polarimetrically calibrated, and georeferenced data products from the Airborne Microwave Observatory of Subcanopy and Subsurface (AirMOSS) radar instrument collected over the Howland Forest site in Maine. The AirMOSS radar is a P-band (UHF) fully polarimetric synthetic aperture radar (SAR) currently operating in the 420-440 MHz band designed to measure root-zone soil moisture (RZSM) and is flown on a NASA Gulfstream-III aircraft. Flight campaigns took place at least biannually from 2012 to 2015 at 10 study sites across North America. The acquired L1 P-band radar backscatter data will be used to retrieve the RZSM at the study sites. Subsequent analyses will investigate both seasonal and inter-annual variability in soil moisture and the relationships to carbon fluxes and their associated uncertainties on a continental scale.",
-            "graphic-preview-description": "Browse Image",
-            "title": "AirMOSS: L1 S-0 Polarimetric Data from AirMOSS P-band SAR, Howland Forest, 2012-2015",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/sdat-tds/1410_1_fit.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1410",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1410",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/airmoss/campaign/AirMOSS_L1_Sigma0_Howlnd/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/airmoss/campaign/AirMOSS_L1_Sigma0_Howlnd/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/AIRMOSS/guides/AirMOSS_L1_Sigma0_Howlnd.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/AIRMOSS/guides/AirMOSS_L1_Sigma0_Howlnd.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1410",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1410",
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
@@ -227946,73 +227925,70 @@
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://daac.ornl.gov/graphics/browse/sdat-tds/1410_1_fit.png",
-                    "description": "Browse Image",
                     "@type": "dcat:Distribution",
+                    "description": "Browse Image",
+                    "downloadURL": "https://daac.ornl.gov/graphics/browse/sdat-tds/1410_1_fit.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://airmoss.ornl.gov",
-                    "description": "AirMOSS campaign site",
                     "@type": "dcat:Distribution",
+                    "description": "AirMOSS campaign site",
+                    "downloadURL": "https://airmoss.ornl.gov",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://thredds.daac.ornl.gov/thredds/catalog/ornldaac/1410/catalog.html",
-                    "description": "The THREDDS location for this Collection.",
                     "@type": "dcat:Distribution",
+                    "description": "The THREDDS location for this Collection.",
+                    "downloadURL": "https://thredds.daac.ornl.gov/thredds/catalog/ornldaac/1410/catalog.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "graphic-preview-description": "Browse Image",
+            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/sdat-tds/1410_1_fit.png",
+            "identifier": "C2274853415-ORNL_CLOUD",
+            "issued": "2018-04-25",
+            "keyword": [
+                "spectral/engineering",
+                "radar",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1410",
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
             "spatial": "-69.11 44.5 -68.25 46.02",
+            "temporal": "2012-10-15T00:00:00Z/2015-09-09T23:59:59Z",
             "theme": [
                 "AirMOSS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "AirMOSS: L1 S-0 Polarimetric Data from AirMOSS P-band SAR, Howland Forest, 2012-2015"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://spotthestation.nasa.gov",
+            "accrualPeriodicity": "R/P1D",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2021-07-27",
-            "temporal": "2021-07-27T00:00:00Z/P1D",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-31",
-            "keyword": [
-                "coordinates",
-                "ephemeris",
-                "space",
-                "station",
-                "iss",
-                "international",
-                "trajectory",
-                "coords",
-                "topo",
-                "location"
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
-            "identifier": "nasa-iss-data_2021-07-27_66nk-z96w",
+            "dataQuality": true,
             "description": "This data represents the best estimated real-time trajectory and local sightings opportunities for the International Space Station (ISS) as generated by the Trajectory Operations and Planning (TOPO) flight controllers at Johnson Space Center.",
-            "title": "ISS_COORDS_2021-07-27",
-            "programCode": [
-                "026:004"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -228135,133 +228111,171 @@
                     "title": "XMLsightingData_natparksUSA02"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "nasa-iss-data_2021-07-27_66nk-z96w",
+            "issued": "2021-07-27",
+            "keyword": [
+                "coordinates",
+                "ephemeris",
+                "space",
+                "station",
+                "iss",
+                "international",
+                "trajectory",
+                "coords",
+                "topo",
+                "location"
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
+            "temporal": "2021-07-27T00:00:00Z/P1D",
             "theme": [
                 "Space Science"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "ISS_COORDS_2021-07-27"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/693",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Stone, T.A., P. Schlesinger, and V.A. Alexeyev. 2003. RLC Forest Cover of the Krasnoyarsk Region, Russia, 1973. ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/693",
-            "issued": "2023-11-21",
-            "temporal": "1973-01-01T00:00:00Z/1973-12-31T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-12-02",
-            "keyword": [
-                "ecosystems",
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
-            "identifier": "C2810671459-ORNL_CLOUD",
             "description": "This dataset is a 1:2 million scale forest cover map for the land area of the Krasnoyarsk Region, Russia. Thirty-two land cover classes are distinguished. These data were digitized from maps of the Atlas of Forests of the USSR (Anon. 1973). This map should not be strictly viewed as a map of actual forest cover, but rather as a map of dominant tree species. Very few tree species are defined, and generally, each polygon and color has only one tree species assigned to it.",
-            "graphic-preview-description": "Browse Image",
-            "title": "RLC Forest Cover of the Krasnoyarsk Region, Russia, 1973",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/vegetation_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F693",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F693",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/global_vegetation/rlc_forest_map_krasnoyarsk/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/global_vegetation/rlc_forest_map_krasnoyarsk/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/RLC/guides/RLC_forest_krasnoyarsk_73.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/RLC/guides/RLC_forest_krasnoyarsk_73.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/693",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/693",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/global_vegetation/rlc_forest_map_krasnoyarsk/comp/fmap73_kr.jpg",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/global_vegetation/rlc_forest_map_krasnoyarsk/comp/fmap73_kr.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/global_vegetation/rlc_forest_map_krasnoyarsk/comp/fmap73_kr_projection.txt",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/global_vegetation/rlc_forest_map_krasnoyarsk/comp/fmap73_kr_projection.txt",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/global_vegetation/rlc_forest_map_krasnoyarsk/comp/fmap73_kr_readme.txt",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/global_vegetation/rlc_forest_map_krasnoyarsk/comp/fmap73_kr_readme.txt",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/global_vegetation/rlc_forest_map_krasnoyarsk/comp/RLC_forest_krasnoyarsk_73.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/global_vegetation/rlc_forest_map_krasnoyarsk/comp/RLC_forest_krasnoyarsk_73.pdf",
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
+            "identifier": "C2810671459-ORNL_CLOUD",
+            "issued": "2023-11-21",
+            "keyword": [
+                "ecosystems",
+                "vegetation",
+                "biosphere",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/693",
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
             "spatial": "56.5 104.5",
+            "temporal": "1973-01-01T00:00:00Z/1973-12-31T23:59:59Z",
             "theme": [
                 "Vegetation",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "RLC Forest Cover of the Krasnoyarsk Region, Russia, 1973"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.nasa.gov/d/66tz-kdn7",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "GeneLab Outreach",
+                "hasEmail": "mailto:genelab-outreach@lists.nasa.gov"
+            },
+            "description": "Microgravity effect on C. elegans gene expression was analysed by whole genome microarray. The worms were cultivated under microgravity for 4 days in the Japanese Module of the International Space Station. C. elegans N2 was exposed microgravity for 4 days. The worms synchronously were cultivated from L1 larvae to adult. There are two control groups onboard 1G and ground 1G control.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "GeneLab Study Page",
+                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-112",
+                    "mediaType": "text/html",
+                    "title": "Microgravity effect on C. elegans N2/VC (CERISE 4 days)"
+                }
+            ],
+            "identifier": "nasa_genelab_GLDS-112_66tz-kdn7",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
             "keyword": [
                 "rna extraction",
                 "sample collection",
@@ -228271,189 +228285,189 @@
                 "microgravity",
                 "nucleic acid hybridization"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "GeneLab Outreach",
-                "hasEmail": "mailto:genelab-outreach@lists.nasa.gov"
-            },
+            "landingPage": "https://data.nasa.gov/d/66tz-kdn7",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "nasa_genelab_GLDS-112_66tz-kdn7",
-            "description": "Microgravity effect on C. elegans gene expression was analysed by whole genome microarray. The worms were cultivated under microgravity for 4 days in the Japanese Module of the International Space Station. C. elegans N2 was exposed microgravity for 4 days. The worms synchronously were cultivated from L1 larvae to adult. There are two control groups onboard 1G and ground 1G control.",
-            "title": "Microgravity effect on C. elegans N2/VC (CERISE 4 days)",
-            "programCode": [
-                "026:005"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-112",
-                    "description": "GeneLab Study Page",
-                    "@type": "dcat:Distribution",
-                    "title": "Microgravity effect on C. elegans N2/VC (CERISE 4 days)"
-                }
-            ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "Microgravity effect on C. elegans N2/VC (CERISE 4 days)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/184",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Hall, F. G., K. F. Huemmrich, D. E. Strebel, S. J. Goetz, J. E. Nickeson, and K. D. Woods. 1996. SNF Leaf Optical Properties: TMS. [Superior National Forest Leaf Optical Properties: Thematic Mapper Simulator]. Data set. Available on-line [http://www.daac.ornl.gov] from Oak Ridge National Laboratory Distributed Active Archive Center, Oak Ridge, Tennessee, U.S.A. Based on F. G. Hall, K. F. Huemmrich, D. E. Strebel, S. J. Goetz, J. E. Nickeson, and K. D. Woods, Biophysical, Morphological, Canopy Optical Property, and Productivity Data from the Superior National Forest, NASA Technical Memorandum 104568, National Aeronautics and Space Administration, Goddard Space Flight Center, Greenbelt, Maryland, U.S.A., 1992. doi:10.3334/ORNLDAAC/184",
-            "issued": "2024-03-02",
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
-            "identifier": "C2884983354-ORNL_CLOUD",
             "description": "Reflectance and transmittance properties of canopy components, measured by Cary-14 spectrometer and averaged (weighted average) to Thematic Mapper Simulator (TMS) wavelength bands; see SNF_CAN_SPEC",
-            "graphic-preview-description": "Browse Image",
-            "title": "SNF Leaf Optical Properties: TMS",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/snf_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F184",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F184",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/snf/SNF_LEAF_TMS/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/snf/SNF_LEAF_TMS/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/SNF/guides/leaf_optical_tms.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/SNF/guides/leaf_optical_tms.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/184",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/184",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/snf/SNF_LEAF_TMS/comp/leaf_optical_tms.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/snf/SNF_LEAF_TMS/comp/leaf_optical_tms.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/snf/SNF_LEAF_TMS/comp/leaf_optical_tms.txt",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/snf/SNF_LEAF_TMS/comp/leaf_optical_tms.txt",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/snf/SNF_LEAF_TMS/comp/leaf_tms.def",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/snf/SNF_LEAF_TMS/comp/leaf_tms.def",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/snf/SNF_LEAF_TMS/comp/leaf_tms.txt",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/snf/SNF_LEAF_TMS/comp/leaf_tms.txt",
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
+            "identifier": "C2884983354-ORNL_CLOUD",
+            "issued": "2024-03-02",
+            "keyword": [
+                "earth science",
+                "vegetation",
+                "biosphere"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/184",
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
+            "title": "SNF Leaf Optical Properties: TMS"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewBundle.jsp?identifier=urn%3Anasa%3Apds%3Amaven.lpw.raw&version=3.7",
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
-                "mars atmosphere and volatile evolution mission",
-                "mars"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This bundle raw contains uncompressed, uncalibrated data from the individual LPW telemetry packets.",
+            "identifier": "urn:nasa:pds:maven.lpw.raw_66wv-isiz",
+            "issued": "2021-05-21",
+            "keyword": [
+                "mars atmosphere and volatile evolution mission",
+                "mars"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewBundle.jsp?identifier=urn%3Anasa%3Apds%3Amaven.lpw.raw&version=3.7",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:maven.lpw.raw_66wv-isiz",
-            "description": "This bundle raw contains uncompressed, uncalibrated data from the individual LPW telemetry packets.",
-            "title": "MAVEN LPW Raw Data Bundle",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "MAVEN LPW Raw Data Bundle"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.nasa.gov/d/66yt-65wn",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "GeneLab Outreach",
+                "hasEmail": "mailto:genelab-outreach@lists.nasa.gov"
+            },
+            "description": "The goal of this study was to assess whether low shear-modeled microgravity (LSMMG) effects yeast ,genomic expression patterns using the powerful tool of whole genome microarray hybridization. We determined ,changes in the yeast model organism Saccharomyces cerevisisae when grown in LSMMG using the rotating High ,Aspect Ratio Vessel (HARV). A significant number of genes were up- or down-regulated by at least two fold in cells ,that were grown for 5 generations or 25 generations in HARVs. We identified genes in cell wall integrity signaling ,pathways containing MAP kinase cascades that may provide clues to novel physiological responses of eukaryotic ,cells to the external stress of a low-shear modeled microgravity environment. A comparison of the microgravity ,response to other environmental stress response (ESR) genes showed that 26% of the genes that respond ,significantly to LSMMG are involved in a general environmental stress response while 74% of the genes may ,represent a unique transcriptional response to microgravity. In addition we found changes in genes involved in ,budding cell polarity establishment and cell separation that confirm our hypothesis that exposure to LSMMG ,causes changes in gene transcription resulting in a phenotypic response. The results of the study provide interesting ,clues to potential mechanisms involved in the response to adaptation to and survival of eukaryotic cells in a ,microgravity environment and our findings may have important health implications for human spaceflight. Experiment Overall Design: Four conditions are compared with three replicates each: yeast grown in low-shear modeled microgravity (HARV bioreactor) for 5 and 25 generations; yeast grown in a horizontal (non-LSMMG) HARV bioreactor for 5 and 25 generations.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "GeneLab Study Page",
+                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-12",
+                    "mediaType": "text/html",
+                    "title": "Transcription profiling of S. cerevisiae cultures grown under low shear-modeled microgravity"
+                }
+            ],
+            "identifier": "nasa_genelab_GLDS-12_66yt-65wn",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
             "keyword": [
                 "p-g4136-2",
                 "p-g4136-3",
@@ -228464,513 +228478,475 @@
                 "nucleic_acid_extraction",
                 "environmentalstress"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "GeneLab Outreach",
-                "hasEmail": "mailto:genelab-outreach@lists.nasa.gov"
-            },
+            "landingPage": "https://data.nasa.gov/d/66yt-65wn",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "nasa_genelab_GLDS-12_66yt-65wn",
-            "description": "The goal of this study was to assess whether low shear-modeled microgravity (LSMMG) effects yeast ,genomic expression patterns using the powerful tool of whole genome microarray hybridization. We determined ,changes in the yeast model organism Saccharomyces cerevisisae when grown in LSMMG using the rotating High ,Aspect Ratio Vessel (HARV). A significant number of genes were up- or down-regulated by at least two fold in cells ,that were grown for 5 generations or 25 generations in HARVs. We identified genes in cell wall integrity signaling ,pathways containing MAP kinase cascades that may provide clues to novel physiological responses of eukaryotic ,cells to the external stress of a low-shear modeled microgravity environment. A comparison of the microgravity ,response to other environmental stress response (ESR) genes showed that 26% of the genes that respond ,significantly to LSMMG are involved in a general environmental stress response while 74% of the genes may ,represent a unique transcriptional response to microgravity. In addition we found changes in genes involved in ,budding cell polarity establishment and cell separation that confirm our hypothesis that exposure to LSMMG ,causes changes in gene transcription resulting in a phenotypic response. The results of the study provide interesting ,clues to potential mechanisms involved in the response to adaptation to and survival of eukaryotic cells in a ,microgravity environment and our findings may have important health implications for human spaceflight. Experiment Overall Design: Four conditions are compared with three replicates each: yeast grown in low-shear modeled microgravity (HARV bioreactor) for 5 and 25 generations; yeast grown in a horizontal (non-LSMMG) HARV bioreactor for 5 and 25 generations.",
-            "title": "Transcription profiling of S. cerevisiae cultures grown under low shear-modeled microgravity",
-            "programCode": [
-                "026:005"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-12",
-                    "description": "GeneLab Study Page",
-                    "@type": "dcat:Distribution",
-                    "title": "Transcription profiling of S. cerevisiae cultures grown under low shear-modeled microgravity"
-                }
-            ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "Transcription profiling of S. cerevisiae cultures grown under low shear-modeled microgravity"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-M-RPCMAG-2-MARS-RAW-V3.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This dataset contains EDITED RAW DATA of the MARS Flyby (MSB). Included are the data of the very Flyby from February 23 until February 27,2007 and the data of the Passive Checkouts PC3 ( August 29, 2006), PC4 (November 23 - December 21,2006) and PC5 (May 22, 2007)",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-m-rpcmag-2-mars-raw-v3.0_673w-isim",
             "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "mars",
                 "international rosetta mission",
                 "unknown"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-M-RPCMAG-2-MARS-RAW-V3.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-m-rpcmag-2-mars-raw-v3.0_673w-isim",
-            "description": "This dataset contains EDITED RAW DATA of the MARS Flyby (MSB). Included are the data of the very Flyby from February 23 until February 27,2007 and the data of the Passive Checkouts PC3 ( August 29, 2006), PC4 (November 23 - December 21,2006) and PC5 (May 22, 2007)",
-            "title": "ROSETTA-ORBITER MARS RPCMAG 2 MARS RAW V3.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "ROSETTA-ORBITER MARS RPCMAG 2 MARS RAW V3.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/AQUA/CERES/ISCCP-D2LIKE-MERG00_L3.003A",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2013-11-26. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/AQUA/CERES/ISCCP-D2LIKE-MERG00_L3.003A. https://doi.org/10.5067/AQUA/CERES/ISCCP-D2LIKE-MERG00_L3.003A.",
-            "issued": "2013-12-18",
-            "temporal": "2000-03-01T00:00:00Z/2017-02-28T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2018-04-19",
-            "keyword": [
-                "ngda",
-                "national geospatial data asset",
-                "earth science",
-                "clouds",
-                "atmosphere"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "DAVID DOELLING",
                 "hasEmail": "mailto:david.r.doelling@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/LARC/SD/ASDC"
-            },
-            "identifier": "C7019527-LARC_ASDC",
             "description": "CER_ISCCP-D2like-Mrg_GEO-MODIS-DAY_Edition3A is the Clouds and the Earth's Radiant Energy System (CERES) Moderate Resolution Imaging Spectroradiometer (MODIS) and Geostationary Satellite (GEO) Cloud Retrievals in International Satellite Cloud Climatology Project (ISCCP) \u2013 Day 2like Format Daytime Edition3A data product. This product is a merge of data from the following platforms and instruments: Spinning Enhanced Visible and Infrared Imager (SEVIRI) on Meteosat Operational Programme 10 (METEOSAT-10); Japanese Advanced Meteorological Imager (JAMI) on The Multi-functional Transport Satellite 2 (MTSAT-2); SEVIRI on METEOSAT-9; Visible and Infrared Spin Scan Radiometer (GMS Series) on (VISSR-GMS) on Geostationary Meteorological Satellite-5 (GMS-5); SEVIRI on METEOSAT-8; Geostationary Operational Environmental Satellite (GOES) I-M IMAGER on Geostationary Operational Environmental Satellite 9 (GOES-9); GOES-11 IMAGER on GOES-11; GOES N-P IMAGER on GOES-13; GOES-8 IMAGER on GOES-8; GOES I-M IMAGER on GOES-10; SEVIRI on METEOSAT-7; MODIS on Terra; GOES N-P IMAGER on GOES-14; MVIRI on METEOSAT-5; GOES-12 IMAGER on GOES-12; GOES-15 IMAGER on GOES-15; MODIS on Aqua; JAMI on Multi-functional Transport Satellite 1 Replacement (MTSAT-1R). Data collection for this product is complete.\r\n\r\nThe Monthly Gridded Cloud Averages (ISCCP-D2like-Mrg) data products contain monthly and monthly 3-hourly (GMT-based) gridded regional mean cloud properties as a function of 18 cloud types, similar to the ISCCP D2 product, where the cloud properties are stratified by pressure, optical depth, and phase. The merged (Mrg) product combines daytime cloud properties from Terra-MODIS (10:30 AM local equator crossing time LECT), Aqua-MODIS (1:30 PM LECT), and geostationary satellites (GEO) to provide the most diurnally complete daytime ISCCP-D2like product. The GEO cloud properties have been normalized with MODIS for diurnal consistency. The CERES MODIS-derived cloud properties are not the official NASA MODIS cloud retrievals but are based on the CERES cloud working group retrievals that are also available in other CERES products. The CERES MODIS-derived cloud properties provide coverage from pole to pole. The 3-hourly GMT-based GEO cloud properties come from five satellites at 8 km nominal resolution with limited coverage. The GEO daytime cloud retrievals incorporate only a visible and IR channel common to all geostationary satellites for spatial consistency. The geostationary calibration is normalized to Terra-MODIS. Each ISCCP-D2like file covers a single month.\r\n\r\nCERES is a key Earth Observing System (EOS) program component. The CERES instruments provide radiometric measurements of the Earth's atmosphere from three broadband channels. The CERES missions follow the successful Earth Radiation Budget Experiment (ERBE) mission. The first CERES instrument, the protoflight model (PFM), was launched on November 27, 1997, as part of the Tropical Rainfall Measuring Mission (TRMM). Two CERES instruments (FM1 and FM2) were launched into polar orbit on board the Earth Observing System (EOS) flagship Terra on December 18, 1999. Two additional CERES instruments (FM3 and FM4) were launched on board Earth Observing System (EOS) Aqua on May 4, 2002. The CERES FM5 instrument was launched on board the Suomi National Polar-orbiting Partnership (NPP) satellite on October 28, 2011. The newest CERES instrument (FM6) was launched on board the Joint Polar-Orbiting Satellite System 1 (JPSS-1) satellite, now called NOAA-20, on November 18, 2017.",
-            "graphic-preview-description": "Mission Logo",
-            "title": "CERES MODIS and GEO Cloud Retrievals in ISCCP-D2like Format Daytime Edition3A",
-            "graphic-preview-file": "https://asdc.larc.nasa.gov/static/images/project_logos/ceres.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAQUA%2FCERES%2FISCCP-D2LIKE-MERG00_L3.003A",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAQUA%2FCERES%2FISCCP-D2LIKE-MERG00_L3.003A",
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
-                    "downloadURL": "https://doi.org/10.5067/AQUA/CERES/ISCCP-D2LIKE-MERG00_L3.003A",
-                    "description": "DOI data set landing page for CER_ISCCP-D2like-Mrg_GEO-MODIS-DAY_Edition3A",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for CER_ISCCP-D2like-Mrg_GEO-MODIS-DAY_Edition3A",
+                    "downloadURL": "https://doi.org/10.5067/AQUA/CERES/ISCCP-D2LIKE-MERG00_L3.003A",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C7019527-LARC_ASDC",
-                    "description": "Earthdata Search for CER_ISCCP-D2like-Mrg_GEO-MODIS-DAY_Edition3A (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for CER_ISCCP-D2like-Mrg_GEO-MODIS-DAY_Edition3A (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C7019527-LARC_ASDC",
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
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/ceres/guide/cer_isccp-d2like-mrg.pdf",
-                    "description": "CERES Monthly Gridded Cloud Averages (ISCCP-D2like-Mrg) Data Set Abstract",
                     "@type": "dcat:Distribution",
+                    "description": "CERES Monthly Gridded Cloud Averages (ISCCP-D2like-Mrg) Data Set Abstract",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/ceres/guide/cer_isccp-d2like-mrg.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/ceres/quality_summaries/CER_ISCCP-D2like_Edition3A.pdf",
-                    "description": "Quality Summary: CERES_ISCCP-D2like_Ed3A (11/14/2013)",
                     "@type": "dcat:Distribution",
+                    "description": "Quality Summary: CERES_ISCCP-D2like_Ed3A (11/14/2013)",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/ceres/quality_summaries/CER_ISCCP-D2like_Edition3A.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's product quality assessment"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/ceres/readme/DPC_ISCCP-D2like-Mrg_R5V2.pdf",
-                    "description": "CERES Data Products Catalog R5V2 11/27/2013 Monthly Cloud Averages (ISCCP-D2like-Mrg)",
                     "@type": "dcat:Distribution",
+                    "description": "CERES Data Products Catalog R5V2 11/27/2013 Monthly Cloud Averages (ISCCP-D2like-Mrg)",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/ceres/readme/DPC_ISCCP-D2like-Mrg_R5V2.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's production history"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/ceres/readme/TISAgrid_SampleRead_ISCCP-D2like-Mrg_R5-988.txt",
-                    "description": "Readme Information on the CER_ISCCP-D2like-Mrg_GEO-MODIS-DAY_Edition3A Data Set",
                     "@type": "dcat:Distribution",
+                    "description": "Readme Information on the CER_ISCCP-D2like-Mrg_GEO-MODIS-DAY_Edition3A Data Set",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/ceres/readme/TISAgrid_SampleRead_ISCCP-D2like-Mrg_R5-988.txt",
+                    "mediaType": "text/html",
                     "title": "View this dataset's read me document"
                 },
                 {
-                    "mediaType": "application/zip",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/ceres/read_software/TISAgrid_SampleRead_ISCCP-D2like-Mrg_R5-988.zip",
-                    "description": "Read Software Package - ISCCP-D2like-Mrg_R5-988 - Direct File Download (.zip)",
                     "@type": "dcat:Distribution",
+                    "description": "Read Software Package - ISCCP-D2like-Mrg_R5-988 - Direct File Download (.zip)",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/ceres/read_software/TISAgrid_SampleRead_ISCCP-D2like-Mrg_R5-988.zip",
+                    "mediaType": "application/zip",
                     "title": "View this dataset's science data product software documentation"
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
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/ceres/readme/input_datasets_for_Edition3A.pdf",
-                    "description": "CERES Input Data Sets (2000-2010)",
                     "@type": "dcat:Distribution",
+                    "description": "CERES Input Data Sets (2000-2010)",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/ceres/readme/input_datasets_for_Edition3A.pdf",
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
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/CERES/ISCCP-D2like-Mrg/GEO-MODIS-DAY_Edition3A/",
-                    "description": "ASDC Direct Data Download for CER_ISCCP-D2like-Mrg_GEO-MODIS-DAY_Edition3A",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for CER_ISCCP-D2like-Mrg_GEO-MODIS-DAY_Edition3A",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/CERES/ISCCP-D2like-Mrg/GEO-MODIS-DAY_Edition3A/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/CERES/ISCCP-D2like-Mrg/GEO-MODIS-DAY_Edition3A/contents.html",
-                    "description": "OPeNDAP data access for CER_ISCCP-D2like-Mrg_GEO-MODIS-DAY_Edition3A",
                     "@type": "dcat:Distribution",
+                    "description": "OPeNDAP data access for CER_ISCCP-D2like-Mrg_GEO-MODIS-DAY_Edition3A",
+                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/CERES/ISCCP-D2like-Mrg/GEO-MODIS-DAY_Edition3A/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 }
             ],
+            "graphic-preview-description": "Mission Logo",
+            "graphic-preview-file": "https://asdc.larc.nasa.gov/static/images/project_logos/ceres.png",
+            "identifier": "C7019527-LARC_ASDC",
+            "issued": "2013-12-18",
+            "keyword": [
+                "ngda",
+                "national geospatial data asset",
+                "earth science",
+                "clouds",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.5067/AQUA/CERES/ISCCP-D2LIKE-MERG00_L3.003A",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2018-04-19",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/LARC/SD/ASDC"
+            },
             "spatial": "<?xml version=\"1.0\" encoding=\"UTF-8\"?><gml:Polygon xmlns:gml=\"http://www.opengis.net/gml/3.2\" srsName=\"EPSG:9825\"><gml:outerBoundaryIs><gml:LinearRing><gml:posList>-90.0 -180.0 -90.0 180.0 90.0 180.0 90.0 -180.0 -90.0 -180.0</gml:posList></gml:LinearRing></gml:outerBoundaryIs><gml:innerBoundaryIs></gml:innerBoundaryIs></gml:Polygon>",
+            "temporal": "2000-03-01T00:00:00Z/2017-02-28T23:59:59.999Z",
             "theme": [
                 "CERES",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "CERES MODIS and GEO Cloud Retrievals in ISCCP-D2like Format Daytime Edition3A"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://spotthestation.nasa.gov",
+            "accrualPeriodicity": "R/P1D",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2021-02-27",
-            "temporal": "2021-02-27T00:00:00Z/P1D",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-31",
-            "keyword": [
-                "iss",
-                "trajectory",
-                "topo",
-                "station",
-                "space",
-                "location",
-                "international",
-                "ephemeris",
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
-            "identifier": "nasa-iss-data_2021-02-27",
+            "dataQuality": true,
             "description": "This data represents the best estimated real-time trajectory and local sightings opportunities for the International Space Station (ISS) as generated by the Trajectory Operations and Planning (TOPO) flight controllers at Johnson Space Center.",
-            "title": "ISS_COORDS_2021-02-27",
-            "programCode": [
-                "026:004"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -229093,209 +229069,235 @@
                     "title": "XMLsightingData_natparksUSA02"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "nasa-iss-data_2021-02-27",
+            "issued": "2021-02-27",
+            "keyword": [
+                "iss",
+                "trajectory",
+                "topo",
+                "station",
+                "space",
+                "location",
+                "international",
+                "ephemeris",
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
+            "temporal": "2021-02-27T00:00:00Z/P1D",
             "theme": [
                 "Space Science"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "ISS_COORDS_2021-02-27"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/GPMGV/MRMS/DATA101",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Kirstetter, Pierre , Walter A Petersen and Jonathan J Gourley.2018. GPM Ground Validation Multi-Radar/Multi-Sensor (MRMS) Precipitation Reanalysis for Satellite Validation Product [indicate subset used]. Dataset available online from the NASA Global Hydrometeorology Resource Center DAAC, Huntsville, Alabama, U.S.A. DOI: http://dx.doi.org/10.5067/GPMGV/MRMS/DATA101",
-            "issued": "2018-12-21",
-            "temporal": "2014-03-02T00:14:00Z/2018-10-30T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-05-23",
-            "keyword": [
-                "radar",
-                "spectral/engineering",
-                "atmosphere",
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
-            "identifier": "C1980955793-GHRC_DAAC",
             "description": "The GPM Ground Validation Multi-Radar/Multi-Sensor (MRMS) Precipitation Reanalysis for Satellite Validation Product dataset contains precipitation rate and type estimates, quality control products, and precipitation corrective factors products. These data products were created using the NOAA MRMS System which ingests Weather Surveillance Radar 88 Doppler (WSR-88D) radar data, Rapid Update Cycle (RAP) model analysis fields, and gauge data. It should be noted that these data products are not standard MRMS. Significant post-processing is applied to MRMS to generate products specifically adapted to satellite purposes and needs over North America. These data are available from March 2, 2014 through October 30, 2018 in ASCII format.",
-            "title": "GPM Ground Validation Multi-Radar/Multi-Sensor (MRMS) Precipitation Reanalysis for Satellite Validation Product V1",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGPMGV%2FMRMS%2FDATA101",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGPMGV%2FMRMS%2FDATA101",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=gpmmrms",
-                    "description": "Files may be downloaded directly to your workstation from this link",
                     "@type": "dcat:Distribution",
+                    "description": "Files may be downloaded directly to your workstation from this link",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=gpmmrms",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://www.nssl.noaa.gov/news/factsheets/MRMS_2015.March.16.pdf",
-                    "description": "MRMS Fact Sheet",
                     "@type": "dcat:Distribution",
+                    "description": "MRMS Fact Sheet",
+                    "downloadURL": "https://www.nssl.noaa.gov/news/factsheets/MRMS_2015.March.16.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://wallops-prf.gsfc.nasa.gov/NMQ/Docs/DailyProducts.pdf",
-                    "description": "MRMS Product Descriptions",
                     "@type": "dcat:Distribution",
+                    "description": "MRMS Product Descriptions",
+                    "downloadURL": "https://wallops-prf.gsfc.nasa.gov/NMQ/Docs/DailyProducts.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.nssl.noaa.gov/projects/mrms/",
-                    "description": "NSSL MRMS Webpage",
                     "@type": "dcat:Distribution",
+                    "description": "NSSL MRMS Webpage",
+                    "downloadURL": "https://www.nssl.noaa.gov/projects/mrms/",
+                    "mediaType": "text/html",
                     "title": "View information related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/relatedProjects/mrms/doc/gpmmrms_dataset.pdf",
-                    "description": "The guide document contains detailed information about the dataset",
                     "@type": "dcat:Distribution",
+                    "description": "The guide document contains detailed information about the dataset",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/relatedProjects/mrms/doc/gpmmrms_dataset.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.1175/JHM-D-11-0139.1",
-                    "description": "Toward a Framework for Systematic Error modeling of Spaceborne Precipitation Radar with NOAA/NSSL Ground Radar-Based National Mosaic QPE",
                     "@type": "dcat:Distribution",
+                    "description": "Toward a Framework for Systematic Error modeling of Spaceborne Precipitation Radar with NOAA/NSSL Ground Radar-Based National Mosaic QPE",
+                    "downloadURL": "https://doi.org/10.1175/JHM-D-11-0139.1",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.1175/BAMS-D-14-00174.1",
-                    "description": "Multi-Radar Multi-Sensor (MRMS) Quantitative Precipitation Estimation: Initial Operating Capabilities",
                     "@type": "dcat:Distribution",
+                    "description": "Multi-Radar Multi-Sensor (MRMS) Quantitative Precipitation Estimation: Initial Operating Capabilities",
+                    "downloadURL": "https://doi.org/10.1175/BAMS-D-14-00174.1",
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
+            "identifier": "C1980955793-GHRC_DAAC",
+            "issued": "2018-12-21",
+            "keyword": [
+                "radar",
+                "spectral/engineering",
+                "atmosphere",
+                "earth science",
+                "precipitation"
+            ],
+            "landingPage": "https://doi.org/10.5067/GPMGV/MRMS/DATA101",
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
             "spatial": "-130.0 20.0 -60.0 55.0",
+            "temporal": "2014-03-02T00:14:00Z/2018-10-30T00:00:00Z",
             "theme": [
                 "NOT APPLICABLE",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "GPM Ground Validation Multi-Radar/Multi-Sensor (MRMS) Precipitation Reanalysis for Satellite Validation Product V1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO%2FRL-C-CONSERT-2-FSS-V1.0",
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
+            "description": "This archive contains edited data (CODMAC level 2) from the CONSERT instrument onboard ROSETTA Orbiter and Lander, acquired during FSS mission phase (First Science Sequence). The primary target is the comet 67P/CHURYUMOV-GERASIMENKO. It also contains documentation which describes the CONSERT experiment. The data archived in this data set conform to the Planetary Data System (PDS) Standards, Version 3.6.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-rl-c-consert-2-fss-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO%2FRL-C-CONSERT-2-FSS-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-rl-c-consert-2-fss-v1.0",
-            "description": "This archive contains edited data (CODMAC level 2) from the CONSERT instrument onboard ROSETTA Orbiter and Lander, acquired during FSS mission phase (First Science Sequence). The primary target is the comet 67P/CHURYUMOV-GERASIMENKO. It also contains documentation which describes the CONSERT experiment. The data archived in this data set conform to the Planetary Data System (PDS) Standards, Version 3.6.",
-            "title": "ROSETTA-ORBITER/ROSETTA-LANDER 67P CONSERT\n                           2 FSS V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER/ROSETTA-LANDER 67P CONSERT\n                           2 FSS V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MER1-M-PANCAM-3-IOFCAL-SCI-V1.0",
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
-                "mars exploration rover",
-                "mars"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "NULL",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mer1-m-pancam-3-iofcal-sci-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "mars exploration rover",
+                "mars"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MER1-M-PANCAM-3-IOFCAL-SCI-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mer1-m-pancam-3-iofcal-sci-v1.0",
-            "description": "NULL",
-            "title": "MER 1 MARS PANCAM IOF SCIENCE V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "MER 1 MARS PANCAM IOF SCIENCE V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-I0046-3-FBIRTFSPEC-V2.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "The data set contains observations obtained with the NASA IRTF SpeX instrument covering the 0.7 to 2.5 micron near-infrared portion of the spectrum. The data set archives reduced, calibrated spectra which were obtained and used in Sherry Fieber-Beyer's Ph.D. dissertation at the University of North Dakota and archives reduced, calibrated spectra subsequent 2010. The research focused on asteroids in a zone centered on the 3:1 resonance. These spectra were used to mineralogically characterize asteroids in this zone in an attempt to identify their meteorite analogs.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-i0046-3-fbirtfspec-v2.0_67dh-4nii",
             "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "292 ludovica",
                 "2089 cetacea",
@@ -229338,99 +229340,78 @@
                 "908 buda",
                 "897 lysistrata"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-I0046-3-FBIRTFSPEC-V2.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-i0046-3-fbirtfspec-v2.0_67dh-4nii",
-            "description": "The data set contains observations obtained with the NASA IRTF SpeX instrument covering the 0.7 to 2.5 micron near-infrared portion of the spectrum. The data set archives reduced, calibrated spectra which were obtained and used in Sherry Fieber-Beyer's Ph.D. dissertation at the University of North Dakota and archives reduced, calibrated spectra subsequent 2010. The research focused on asteroids in a zone centered on the 3:1 resonance. These spectra were used to mineralogically characterize asteroids in this zone in an attempt to identify their meteorite analogs.",
-            "title": "FIEBER-BEYER IRTF MAINBELT ASTEROID SPECTRA V2.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "FIEBER-BEYER IRTF MAINBELT ASTEROID SPECTRA V2.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-P-SDC-3-PLUTO-V2.0",
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
+            "description": "This data set contains Calibrated data taken by the New Horizons         Student Dust Counter                                                   instrument during the                                                    Pluto encounter                                                        mission phase.  This is VERSION 2.0 of this data set.                    This data set contains SDC observations taken during the                 the Approach (Jan-Jul, 2015), Encounter and Departure mission            sub-phases, including flyby observations taken on 14.July, 2015,         and including data through 2015 and into January, 2016; the data are     limited to those downlinked from the spacecraft as of the end of         January, 2016.  The rest of the downlinked data for this mission         phase will be delivered in a future data set.                            This is version 2.0 of this data set.  Changes since version 1.0         include data downlinked between the end of July, 2015 and the end of     January, 2016.  Also, updates were made to the documentation and         catalog files, primarily to resolve liens from the V1.0 peer review.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-p-sdc-3-pluto-v2.0_67dw-56f2",
+            "issued": "2018-09-05",
+            "keyword": [
+                "new horizons",
+                "dust"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-P-SDC-3-PLUTO-V2.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-p-sdc-3-pluto-v2.0_67dw-56f2",
-            "description": "This data set contains Calibrated data taken by the New Horizons         Student Dust Counter                                                   instrument during the                                                    Pluto encounter                                                        mission phase.  This is VERSION 2.0 of this data set.                    This data set contains SDC observations taken during the                 the Approach (Jan-Jul, 2015), Encounter and Departure mission            sub-phases, including flyby observations taken on 14.July, 2015,         and including data through 2015 and into January, 2016; the data are     limited to those downlinked from the spacecraft as of the end of         January, 2016.  The rest of the downlinked data for this mission         phase will be delivered in a future data set.                            This is version 2.0 of this data set.  Changes since version 1.0         include data downlinked between the end of July, 2015 and the end of     January, 2016.  Also, updates were made to the documentation and         catalog files, primarily to resolve liens from the V1.0 peer review.",
-            "title": "NEW HORIZONS                            \n      SDC PLUTO ENCOUNTER                                                     \n      CALIBRATED V2.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "NEW HORIZONS                            \n      SDC PLUTO ENCOUNTER                                                     \n      CALIBRATED V2.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/EPIC/DSCOVR/DSCOVR_EPIC_L3_PAR-image_L3.01",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/EPIC/DSCOVR/DSCOVR_EPIC_L3_PAR-image_L3.01.",
-            "issued": "2021-02-17",
-            "temporal": "2015-06-13T00:00:00Z/2023-03-01T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2021-02-17",
-            "keyword": [
-                "ocean optics",
-                "oceans",
-                "earth science"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Robert Frouin",
                 "hasEmail": "mailto:rfrouin@ucsd.edu"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/LARC/SD/ASDC"
-            },
-            "identifier": "C2150640573-LARC_ASDC",
             "description": "DSCOVR_EPIC_L3_PAR-image_01 is a view image showing data from DSCOVR_EPIC_L3_PAR, which is the Deep Space Climate Observatory (DSCOVR) Earth Polychromatic Imaging Camera (EPIC) Level 3 photosynthetically available radiation (PAR) version 1 data product. The EPIC observations of the Earth\u2019s surface lit by the Sun made 13 times during the day in spectral bands centered on 443, 551, and 680 nm are used to estimate daily mean PAR at the ice-free ocean surface. PAR is defined as the quantum energy flux from the Sun in the 400-700 nm range. Daily mean PAR is the 24-hour averaged planar flux in that spectral range reaching the surface. It is expressed in E.m-2.d-1 (Einstein per meter squared per day). The factor required to convert E.m-2 d-1 units to mW.cm-2.\u00b5m-1 units is equal to 0.838 to an inaccuracy of a few percent regardless of meteorological conditions. The EPIC daily mean PAR product is generated on Plate Carr\u00e9e (equal-angle) grid with 18.4 km resolution at the equator and on 18.4 km equal-area grid, i.e., the product is compatible with Ocean Biology Processing Group ocean color products.\r\nThe EPIC PAR algorithm uses a budget approach, in which the solar irradiance reaching the surface is obtained by subtracting from the irradiance arriving at the top of the atmosphere (known), the irradiance reflected to space (estimated from the EPIC Level 1b radiance data), taking into account atmospheric transmission (modeled). Clear and cloudy regions within a pixel do not need to be distinguished, which dismisses the need for often-arbitrary assumptions about cloudiness distribution and is therefore adapted to the relatively large EPIC pixels. A daily mean PAR is estimated on the source grid for each EPIC instantaneous daytime observation, assuming no cloudiness change during the day, and the individual estimates are remapped and weight-averaged using the cosine of the Sun zenith angle. In the computations, wind speed, surface pressure, and water vapor amount are extracted from NCEP (National Centers for Environmental Prediction) Reanalysis 2 data, aerosol optical thickness and angstrom coefficient from MERRA-2 (Modern-Era Retrospective analysis for Research and Applications, Version 2) data, and ozone amount from EPIC Level 2 data. Areas contaminated by sun glint are excluded using a threshold on sun glint reflectance calculated using wind data. Ice masking is based on NSIDC (National Snow and Ice Data Center) near real time ice fraction data. \r\nAdditional information about the EPIC ocean surface PAR products can be found at the NASA DSCOVR: EPIC website: https://epic.gsfc.nasa.gov/, under \u201cScience -> Products -> Ocean Surface\u201d (https://epic.gsfc.nasa.gov/science/products/ocean).",
-            "title": "DSCOVR EPIC Level 3 PAR Image",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FEPIC%2FDSCOVR%2FDSCOVR_EPIC_L3_PAR-image_L3.01",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FEPIC%2FDSCOVR%2FDSCOVR_EPIC_L3_PAR-image_L3.01",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
@@ -229440,440 +229421,439 @@
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/EPIC/DSCOVR/DSCOVR_EPIC_L3_PAR-image_L3.01",
-                    "description": "DOI data set landing page for DSCOVR_EPIC_L3_PAR-IMAGE_01",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for DSCOVR_EPIC_L3_PAR-IMAGE_01",
+                    "downloadURL": "https://doi.org/10.5067/EPIC/DSCOVR/DSCOVR_EPIC_L3_PAR-image_L3.01",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2150640573-LARC_ASDC",
-                    "description": "Earthdata Search for DSCOVR_EPIC_L3_PAR-image_01 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for DSCOVR_EPIC_L3_PAR-image_01 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2150640573-LARC_ASDC",
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
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/DSCOVR/EPIC/L3_PAR-IMAGE_01/",
-                    "description": "ASDC Direct Data Download for DSCOVR_EPIC_L3_PAR-IMAGE_01",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for DSCOVR_EPIC_L3_PAR-IMAGE_01",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/DSCOVR/EPIC/L3_PAR-IMAGE_01/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 }
             ],
+            "identifier": "C2150640573-LARC_ASDC",
+            "issued": "2021-02-17",
+            "keyword": [
+                "ocean optics",
+                "oceans",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/EPIC/DSCOVR/DSCOVR_EPIC_L3_PAR-image_L3.01",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2021-02-17",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/LARC/SD/ASDC"
+            },
             "spatial": "<?xml version=\"1.0\" encoding=\"UTF-8\"?><gml:Polygon xmlns:gml=\"http://www.opengis.net/gml/3.2\" srsName=\"EPSG:9825\"><gml:outerBoundaryIs><gml:LinearRing><gml:posList>-90.0 -180.0 -90.0 180.0 90.0 180.0 90.0 -180.0 -90.0 -180.0</gml:posList></gml:LinearRing></gml:outerBoundaryIs><gml:innerBoundaryIs></gml:innerBoundaryIs></gml:Polygon>",
+            "temporal": "2015-06-13T00:00:00Z/2023-03-01T00:00:00Z",
             "theme": [
                 "DSCOVR",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "DSCOVR EPIC Level 3 PAR Image"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1863",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Yu, L., J. Wen, C.Y. Chang, C. Frankenberg, and Y. Sun. 2021. High Resolution Global Contiguous SIF Estimates from OCO-2 SIF and MODIS, Version 2. ORNL DAAC, Oak Ridge, Tennessee, USA. https://doi.org/10.3334/ORNLDAAC/1863",
-            "issued": "2022-01-09",
-            "temporal": "2014-09-01T00:00:00Z/2020-07-31T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-17",
-            "keyword": [
-                "ecological dynamics",
-                "vegetation",
-                "ngda",
-                "national geospatial data asset",
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
-            "identifier": "C2207986708-ORNL_CLOUD",
             "description": "This dataset provides spatially-contiguous global mean daily solar-induced chlorophyll fluorescence (SIF) estimates at 0.05 degree (approximately 5 km at the equator) spatial and 16-day temporal resolution from September 2014 through July 2020. This product was derived from Orbiting Carbon Observatory-2 (OCO-2) SIF observations and produced by training an artificial neural network (ANN) on the native OCO-2 SIF observations and MODIS BRDF-corrected seven-band surface reflectance along OCO-2's orbits. The trained ANN model was then applied to predict mean daily SIF (mW/m2/nm/sr) in OCO-2's gap regions based on MODIS reflectance and landcover. This framework was stratified by biomes and 16-day time steps. This dataset's high resolution and global contiguous coverage will greatly enhance the synergy between satellite SIF and photosynthesis measured on the ground at consistent spatial scales. Potential applications of this dataset include advancing dynamic drought monitoring and mitigation, informing agricultural planning and yield estimation, and providing a benchmark for upcoming satellite missions with SIF capabilities at higher spatial resolutions.",
-            "graphic-preview-description": "Predicted spatially contiguous SIF in the first half of August 2015. The highest SIF values during this time period were observed in agricultural sectors in the Northern Hemisphere. Source: Data file sif_ann_201508a.nc",
-            "title": "High Resolution Global Contiguous SIF Estimates from OCO-2 SIF and MODIS, Version 2",
-            "graphic-preview-file": "https://daac.ornl.gov/SIF-ESDR/guides/Global_SIF_OCO2_MODIS_Fig1.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1863",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1863",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/sif-esdr/17-MEASURES-0032/Global_SIF_OCO2_MODIS/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/sif-esdr/17-MEASURES-0032/Global_SIF_OCO2_MODIS/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/SIF-ESDR/guides/Global_SIF_OCO2_MODIS.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/SIF-ESDR/guides/Global_SIF_OCO2_MODIS.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1863",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1863",
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
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/sif-esdr/17-MEASURES-0032/Global_SIF_OCO2_MODIS/comp/Global_SIF_OCO2_MODIS.pdf",
-                    "description": "High Resolution Global Contiguous SIF Estimates from OCO-2 SIF and MODIS, Version 2: Global_SIF_OCO2_MODIS.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "High Resolution Global Contiguous SIF Estimates from OCO-2 SIF and MODIS, Version 2: Global_SIF_OCO2_MODIS.pdf",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/sif-esdr/17-MEASURES-0032/Global_SIF_OCO2_MODIS/comp/Global_SIF_OCO2_MODIS.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://daac.ornl.gov/SIF-ESDR/guides/Global_SIF_OCO2_MODIS_Fig1.png",
-                    "description": "Predicted spatially contiguous SIF in the first half of August 2015. The highest SIF values during this time period were observed in agricultural sectors in the Northern Hemisphere. Source: Data file sif_ann_201508a.nc",
                     "@type": "dcat:Distribution",
+                    "description": "Predicted spatially contiguous SIF in the first half of August 2015. The highest SIF values during this time period were observed in agricultural sectors in the Northern Hemisphere. Source: Data file sif_ann_201508a.nc",
+                    "downloadURL": "https://daac.ornl.gov/SIF-ESDR/guides/Global_SIF_OCO2_MODIS_Fig1.png",
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
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://thredds.daac.ornl.gov/thredds/catalog/ornldaac/1863/catalog.html",
-                    "description": "The THREDDS location for this Collection.",
                     "@type": "dcat:Distribution",
+                    "description": "The THREDDS location for this Collection.",
+                    "downloadURL": "https://thredds.daac.ornl.gov/thredds/catalog/ornldaac/1863/catalog.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "graphic-preview-description": "Predicted spatially contiguous SIF in the first half of August 2015. The highest SIF values during this time period were observed in agricultural sectors in the Northern Hemisphere. Source: Data file sif_ann_201508a.nc",
+            "graphic-preview-file": "https://daac.ornl.gov/SIF-ESDR/guides/Global_SIF_OCO2_MODIS_Fig1.png",
+            "identifier": "C2207986708-ORNL_CLOUD",
+            "issued": "2022-01-09",
+            "keyword": [
+                "ecological dynamics",
+                "vegetation",
+                "ngda",
+                "national geospatial data asset",
+                "earth science",
+                "biosphere"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1863",
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
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2014-09-01T00:00:00Z/2020-07-31T23:59:59Z",
             "theme": [
                 "SIF-ESDR",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "High Resolution Global Contiguous SIF Estimates from OCO-2 SIF and MODIS, Version 2"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=CO-X-RSS-1-GWE2-V1.0",
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
-                "cassini-huygens"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "not applicable",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.co-x-rss-1-gwe2-v1.0_67gf-txb7",
+            "issued": "2021-05-21",
+            "keyword": [
+                "cassini-huygens"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=CO-X-RSS-1-GWE2-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.co-x-rss-1-gwe2-v1.0_67gf-txb7",
-            "description": "not applicable",
-            "title": "CASSINI RSS RAW DATA SET - GWE2 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "CASSINI RSS RAW DATA SET - GWE2 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/MODIS/MOD10_L2.061",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "MODIS/Terra Snow Cover 5-Min L2 Swath 500m V061. Version 61. Archived by National Aeronautics and Space Administration, U.S. Government, NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/MODIS/MOD10_L2.061.",
-            "issued": "2000-02-24",
-            "temporal": "2000-02-24T00:00:00Z/2024-11-11T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-08",
-            "keyword": [
-                "earth science",
-                "cryosphere",
-                "snow/ice",
-                "ngda",
-                "national geospatial data asset"
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
-            "identifier": "C1646610394-NSIDC_ECS",
             "description": "This global Level-2 (L2) data set provides daily snow cover detected using the Normalized Difference Snow Index (NDSI) and a series of screens designed to alleviate errors and flag uncertain snow cover detections. The NDSI is derived from radiance data acquired by the Moderate Resolution Imaging Spectroradiometer (MODIS) on board the Terra satellite: DOI:10.5067/MODIS/MOD02HKM.061 and DOI:10.5067/MODIS/MOD021KM.061. Each data granule contains 5 minutes of swath data observed at a resolution of 500 m.\n\nThe terms \"Version 61\" and \"Collection 6.1\" are used interchangeably in reference to this release of MODIS data.",
-            "graphic-preview-description": "This application allows you to interactively browse global satellite imagery within hours of it being acquired. You can also save it, share it, and download the underlying data.",
-            "title": "MODIS/Terra Snow Cover 5-Min L2 Swath 500m V061",
-            "graphic-preview-file": "https://worldview.earthdata.nasa.gov/?v=-189,-80,151,77&l=MODIS_Terra_NDSI_Snow_Cover,Coastlines_15m,MODIS_Terra_CorrectedReflectance_TrueColor",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMODIS%2FMOD10_L2.061",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMODIS%2FMOD10_L2.061",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/daac/subscriptions.html",
-                    "description": "Subscribe to have new data automatically sent when the data become available.",
                     "@type": "dcat:Distribution",
+                    "description": "Subscribe to have new data automatically sent when the data become available.",
+                    "downloadURL": "https://nsidc.org/daac/subscriptions.html",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/MOST/MOD10_L2.061/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/MOST/MOD10_L2.061/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=MOD10_L2+V061",
-                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=MOD10_L2+V061",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/data/data-access-tool/MOD10_L2/versions/61/",
-                    "description": "Search and filter data files using a map-based interface",
                     "@type": "dcat:Distribution",
+                    "description": "Search and filter data files using a map-based interface",
+                    "downloadURL": "https://nsidc.org/data/data-access-tool/MOD10_L2/versions/61/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://worldview.earthdata.nasa.gov/?v=-189%2C-80%2C151%2C77&l=MODIS_Terra_NDSI_Snow_Cover%2CCoastlines_15m%2CMODIS_Terra_CorrectedReflectance_TrueColor",
-                    "description": "This application allows you to interactively browse global satellite imagery within hours of it being acquired. You can also save it, share it, and download the underlying data.",
                     "@type": "dcat:Distribution",
+                    "description": "This application allows you to interactively browse global satellite imagery within hours of it being acquired. You can also save it, share it, and download the underlying data.",
+                    "downloadURL": "https://worldview.earthdata.nasa.gov/?v=-189%2C-80%2C151%2C77&l=MODIS_Terra_NDSI_Snow_Cover%2CCoastlines_15m%2CMODIS_Terra_CorrectedReflectance_TrueColor",
+                    "mediaType": "text/html",
                     "title": "Get a related visualization through WORLDVIEW"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/MODIS/MOD10_L2.061",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/MODIS/MOD10_L2.061",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/MODIS/MOD10_L2.061",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/MODIS/MOD10_L2.061",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "graphic-preview-description": "This application allows you to interactively browse global satellite imagery within hours of it being acquired. You can also save it, share it, and download the underlying data.",
+            "graphic-preview-file": "https://worldview.earthdata.nasa.gov/?v=-189,-80,151,77&l=MODIS_Terra_NDSI_Snow_Cover,Coastlines_15m,MODIS_Terra_CorrectedReflectance_TrueColor",
+            "identifier": "C1646610394-NSIDC_ECS",
+            "issued": "2000-02-24",
+            "keyword": [
+                "earth science",
+                "cryosphere",
+                "snow/ice",
+                "ngda",
+                "national geospatial data asset"
+            ],
+            "landingPage": "https://doi.org/10.5067/MODIS/MOD10_L2.061",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2024-11-08",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA NSIDC DAAC"
+            },
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2000-02-24T00:00:00Z/2024-11-11T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "MODIS/Terra Snow Cover 5-Min L2 Swath 500m V061"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MEX-M-MRS-1%2F2%2F3-EXT3-3899-V1.0",
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
+            "description": "This is a Mars Express Radio Science data set, collected during the extended mission phase 2010-01-01 to 2012-12-31. It is a Global Gravity measurement and covers the time 2012-08-20T05:39:30.000 to 2012-08-20T08:22:55.500.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mex-m-mrs-1-2-3-ext3-3899-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "mars",
+                "mars express"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MEX-M-MRS-1%2F2%2F3-EXT3-3899-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mex-m-mrs-1-2-3-ext3-3899-v1.0",
-            "description": "This is a Mars Express Radio Science data set, collected during the extended mission phase 2010-01-01 to 2012-12-31. It is a Global Gravity measurement and covers the time 2012-08-20T05:39:30.000 to 2012-08-20T08:22:55.500.",
-            "title": "MARS EXPRESS MARS MRS 1/2/3\n                                     EXTENDED MISSION 3 3899 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "MARS EXPRESS MARS MRS 1/2/3\n                                     EXTENDED MISSION 3 3899 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-5-DDR-FAMILY-V4.1",
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
+            "description": "Dynamical family classification of asteroids by Zappala, et al., based on the hierarchical clustering method.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-5-ddr-family-v4.1_67iy-q4t7",
+            "issued": "2021-05-21",
+            "keyword": [
+                "support archives",
+                "asteroid"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-5-DDR-FAMILY-V4.1",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-5-ddr-family-v4.1_67iy-q4t7",
-            "description": "Dynamical family classification of asteroids by Zappala, et al., based on the hierarchical clustering method.",
-            "title": "ASTEROID DYNAMICAL FAMILIES V4.1",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ASTEROID DYNAMICAL FAMILIES V4.1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-X-ALICE-3-PLUTOCRUISE-V2.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This data set contains Calibrated data taken by the New Horizons         Alice Ultraviolet Imaging Spectrograph                                 instrument during the                                                    pluto cruise                                                           mission phase.  This is VERSION 2.0 of this data set.                    ALICE Activities Overview at Annual CheckOuts (ACOs) during the          Pluto Cruise mission phase started with the standard WakeUp              sequence (memory/code checks, aperture door performance test,            pixelhack issue verification, 24 hours of decontamination and            three one hour dark observations) and finished with the standard         Button-Up sequence (code and parameter refresh).  Other activities       (with targets as noted) were calibrations for flux (Spica,               rho-Leo, gamma-Grus, HD93521, Sun in Solar OCcultation Channel,          SOCC), flatfield (rho-Leo), airglow scattered light and SOCC             pointing calibrations (Spica, zeta-Pup), SOCC flat (Sun), dark sky       stares, spinning dark observations (in some cases the Sun strobes        through the slit), pointing and short wavelength calibration             (HD93521), InterPlanetary Medium (IPM) histograms and pixellist          observations, dual target tests (HD214680 = 8 Lac, HD214168 = 10         Lac), MEV Solar Wind (HEET) baseine observation, Pluto encounter         rehearsals, and instrument interference tests.                           The changes in Version 2.0 were re-running of the ancillary data         in the data product, updated geometry from newer SPICE kernels,          minor editing of the documentation, catalogs, etc., and resolution       of liens from the December, 2014 review, plus those from the May,        2016 review of the Pluto Encounter data sets.                            New observations added with this version (V2.0) include IPM              histogram scans in December, 2014, which failed.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-x-alice-3-plutocruise-v2.0_67jp-x882",
             "issued": "2018-09-05",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "new horizons",
                 "sun",
                 "calibration"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-X-ALICE-3-PLUTOCRUISE-V2.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-x-alice-3-plutocruise-v2.0_67jp-x882",
-            "description": "This data set contains Calibrated data taken by the New Horizons         Alice Ultraviolet Imaging Spectrograph                                 instrument during the                                                    pluto cruise                                                           mission phase.  This is VERSION 2.0 of this data set.                    ALICE Activities Overview at Annual CheckOuts (ACOs) during the          Pluto Cruise mission phase started with the standard WakeUp              sequence (memory/code checks, aperture door performance test,            pixelhack issue verification, 24 hours of decontamination and            three one hour dark observations) and finished with the standard         Button-Up sequence (code and parameter refresh).  Other activities       (with targets as noted) were calibrations for flux (Spica,               rho-Leo, gamma-Grus, HD93521, Sun in Solar OCcultation Channel,          SOCC), flatfield (rho-Leo), airglow scattered light and SOCC             pointing calibrations (Spica, zeta-Pup), SOCC flat (Sun), dark sky       stares, spinning dark observations (in some cases the Sun strobes        through the slit), pointing and short wavelength calibration             (HD93521), InterPlanetary Medium (IPM) histograms and pixellist          observations, dual target tests (HD214680 = 8 Lac, HD214168 = 10         Lac), MEV Solar Wind (HEET) baseine observation, Pluto encounter         rehearsals, and instrument interference tests.                           The changes in Version 2.0 were re-running of the ancillary data         in the data product, updated geometry from newer SPICE kernels,          minor editing of the documentation, catalogs, etc., and resolution       of liens from the December, 2014 review, plus those from the May,        2016 review of the Pluto Encounter data sets.                            New observations added with this version (V2.0) include IPM              histogram scans in December, 2014, which failed.",
-            "title": "NEW HORIZONS                            \n      ALICE PLUTO CRUISE                                                      \n      CALIBRATED V2.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "NEW HORIZONS                            \n      ALICE PLUTO CRUISE                                                      \n      CALIBRATED V2.0"
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
-                "index",
-                "pds",
-                "dictionary"
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
-            "identifier": "NASA-643",
             "description": "Data Dictionary and Index Files",
-            "title": "PDS Data Dictionary (1r67)",
-            "programCode": [
-                "026:005"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -229881,1134 +229861,1132 @@
                     "mediaType": "application/html"
                 }
             ],
-            "accrualPeriodicity": "irregular",
+            "identifier": "NASA-643",
+            "issued": "2018-06-25",
+            "keyword": [
+                "index",
+                "pds",
+                "dictionary"
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
+            "title": "PDS Data Dictionary (1r67)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RPCIES-2-ESC2-V2.0",
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
+            "description": "This dataset contains EDITED DATA of the Rosetta RPCIES instrument taken during the comet escort 2 phase (ESC2). The target of this phase was comet 67P/CHURYUMOV-GERASIMENKO 1 (1969 R1). Included are the data taken between 11 Mar 2015 and 30 Jun 2015. This dataset supersedes the previous RO-C-RPCIES-2-ESC2-V1.0 dataset. The primary change is the addition of the cycle duration field to the data products.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rpcies-2-esc2-v2.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RPCIES-2-ESC2-V2.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rpcies-2-esc2-v2.0",
-            "description": "This dataset contains EDITED DATA of the Rosetta RPCIES instrument taken during the comet escort 2 phase (ESC2). The target of this phase was comet 67P/CHURYUMOV-GERASIMENKO 1 (1969 R1). Included are the data taken between 11 Mar 2015 and 30 Jun 2015. This dataset supersedes the previous RO-C-RPCIES-2-ESC2-V1.0 dataset. The primary change is the addition of the cycle duration field to the data products.",
-            "title": "ROSETTA-ORBITER 67P RPCIES 2 ESC2 V2.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RPCIES 2 ESC2 V2.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MEX-M-MRS-1%2F2%2F3-EXT3-3334-V1.0",
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
+            "description": "This is a Mars Express Radio Science data set, collected during the extended mission phase 2010-01-01 to 2012-12-31. It is a Global Gravity measurement and covers the time 2012-07-02T08:18:11.000 to 2012-07-02T09:56:20.500.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mex-m-mrs-1-2-3-ext3-3334-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "mars express",
+                "mars"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MEX-M-MRS-1%2F2%2F3-EXT3-3334-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mex-m-mrs-1-2-3-ext3-3334-v1.0",
-            "description": "This is a Mars Express Radio Science data set, collected during the extended mission phase 2010-01-01 to 2012-12-31. It is a Global Gravity measurement and covers the time 2012-07-02T08:18:11.000 to 2012-07-02T09:56:20.500.",
-            "title": "MARS EXPRESS MARS MRS 1/2/3\n                                     EXTENDED MISSION 3 3334 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "MARS EXPRESS MARS MRS 1/2/3\n                                     EXTENDED MISSION 3 3334 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG2-N-PRA-2-RDR-HIGHRATE-60MS-V1.0",
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
-                "neptune",
-                "voyager"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This data set (VG2-N-PRA-2-RDR-HIGHRATE-60MS-V1.0) contains data\nacquired by the Voyager-2 Planetary Radio Astronomy (PRA) instrument\nduring the Neptune encounter.  Since the PRA instrument is able to\nobserve planetary phenomenon at much larger ranges than other fields\nand particles experiments, thus the PRA data cover a variable and\nlonger encounter period. PRA lowband data provided here cover the\nentire Neptune Encounter Phase (1989-05-25 to 1989-09-27).",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg2-n-pra-2-rdr-highrate-60ms-v1.0_67rf-mg8g",
+            "issued": "2021-05-21",
+            "keyword": [
+                "neptune",
+                "voyager"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG2-N-PRA-2-RDR-HIGHRATE-60MS-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg2-n-pra-2-rdr-highrate-60ms-v1.0_67rf-mg8g",
-            "description": "This data set (VG2-N-PRA-2-RDR-HIGHRATE-60MS-V1.0) contains data\nacquired by the Voyager-2 Planetary Radio Astronomy (PRA) instrument\nduring the Neptune encounter.  Since the PRA instrument is able to\nobserve planetary phenomenon at much larger ranges than other fields\nand particles experiments, thus the PRA data cover a variable and\nlonger encounter period. PRA lowband data provided here cover the\nentire Neptune Encounter Phase (1989-05-25 to 1989-09-27).",
-            "title": "VG2 NEP PRA EDITED RDR HIGH RATE\n                                      60MS V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "VG2 NEP PRA EDITED RDR HIGH RATE\n                                      60MS V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/366",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Rayment, M.B. 1998. BOREAS TF-09 SSA-OBS Branch Level Flux Data. ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/366",
-            "issued": "2023-11-22",
-            "temporal": "1996-04-07T00:00:00Z/1996-11-23T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-11-28",
-            "keyword": [
-                "earth science",
-                "vegetation",
-                "atmospheric chemistry",
-                "atmosphere",
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
-            "identifier": "C2808130816-ORNL_CLOUD",
             "description": "CO2 and H2O vapor exchange and ancillary data collected from enclosures around the black spruce branches.  Data collected by the TF-09 group at the SSA-OBS site.",
-            "graphic-preview-description": "Browse Image",
-            "title": "BOREAS TF-09 SSA-OBS Branch Level Flux Data",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/boreas_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F366",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F366",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/boreas/TF/tf9brflx/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/boreas/TF/tf9brflx/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/BOREAS/guides/TF09_BranchBag.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/BOREAS/guides/TF09_BranchBag.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/366",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/366",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/msword",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TF/tf9brflx/comp/TF09_BranchBag.doc",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TF/tf9brflx/comp/TF09_BranchBag.doc",
+                    "mediaType": "application/msword",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TF/tf9brflx/comp/TF09_BranchBag.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TF/tf9brflx/comp/TF09_BranchBag.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TF/tf9brflx/comp/TF09_BranchBag.txt",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TF/tf9brflx/comp/TF09_BranchBag.txt",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TF/tf9brflx/comp/tf9brflx.def",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TF/tf9brflx/comp/tf9brflx.def",
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
+            "identifier": "C2808130816-ORNL_CLOUD",
+            "issued": "2023-11-22",
+            "keyword": [
+                "earth science",
+                "vegetation",
+                "atmospheric chemistry",
+                "atmosphere",
+                "biosphere"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/366",
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
             "spatial": "53.99 -105.12",
+            "temporal": "1996-04-07T00:00:00Z/1996-11-23T23:59:59Z",
             "theme": [
                 "BOREAS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "BOREAS TF-09 SSA-OBS Branch Level Flux Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/SeaBASS/OCEAN_COLOR_CAL_VAL/DATA001",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/GSFC/SED/ESD/GCDC/OB.DAAC. https://doi.org/10.5067/SeaBASS/OCEAN_COLOR_CAL_VAL/DATA001.",
-            "issued": "2005-03-30",
-            "temporal": "2005-03-30T00:00:00Z/2023-04-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-04-06",
-            "keyword": [
-                "ocean temperature",
-                "salinity/density",
-                "ocean optics",
-                "oceans",
-                "ocean chemistry",
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
-            "identifier": "C1633360535-OB_DAAC",
             "description": "Measurements made off the New Jersey and New York coasts between 2005 and 2009.",
-            "title": "Ocean color calibration and validation measurements off the New Jersey and New York coasts",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSeaBASS%2FOCEAN_COLOR_CAL_VAL%2FDATA001",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSeaBASS%2FOCEAN_COLOR_CAL_VAL%2FDATA001",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://seabass.gsfc.nasa.gov/experiment/Ocean_Color_Cal_Val/",
-                    "description": "Detailed information about the SeaBASS Experiment such as cruises, funding, and investigators",
                     "@type": "dcat:Distribution",
+                    "description": "Detailed information about the SeaBASS Experiment such as cruises, funding, and investigators",
+                    "downloadURL": "https://seabass.gsfc.nasa.gov/experiment/Ocean_Color_Cal_Val/",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 }
             ],
+            "identifier": "C1633360535-OB_DAAC",
+            "issued": "2005-03-30",
+            "keyword": [
+                "ocean temperature",
+                "salinity/density",
+                "ocean optics",
+                "oceans",
+                "ocean chemistry",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/SeaBASS/OCEAN_COLOR_CAL_VAL/DATA001",
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
+            "title": "Ocean color calibration and validation measurements off the New Jersey and New York coasts"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/749",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Turner, D.P., W.D. Ritts, and M.J. Gregory. 2006. BigFoot GPP Surfaces for North and South American Sites, 2000-2004. ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/749",
-            "issued": "2023-07-26",
-            "temporal": "2000-01-01T00:00:00Z/2004-12-31T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-10-01",
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
-            "identifier": "C2751481399-ORNL_CLOUD",
             "description": "The BigFoot project gathered Gross Primary Production (GPP) data for nine EOS Land Validation Sites located from Alaska to Brazil from 2000 to 2004.  Each site is representative of one or two distinct biomes, including the Arctic tundra; boreal evergreen needleleaf forest; temperate cropland, grassland, evergreen needleleaf forest, and deciduous broadleaf forest; desert grassland and shrubland; and tropical evergreen broadleaf forest. BigFoot was funded by NASA's Terrestrial Ecology Program.For more details on the BigFoot Project, please visit the website: http://www.fsl.orst.edu/larse/bigfoot/index.html.",
-            "graphic-preview-description": "Browse Image",
-            "title": "BigFoot GPP Surfaces for North and South American Sites, 2000-2004",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/bigfoot_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F749",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F749",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/bigfoot_val/GPP_surfaces/data/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/bigfoot_val/GPP_surfaces/data/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "application/zip",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/protected/bundle/GPP_surfaces_749.zip",
-                    "description": "Collection bundle",
                     "@type": "dcat:Distribution",
+                    "description": "Collection bundle",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/protected/bundle/GPP_surfaces_749.zip",
+                    "mediaType": "application/zip",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/BIGFOOT_VAL/guides/bf_gpp_surf_guide.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/BIGFOOT_VAL/guides/bf_gpp_surf_guide.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/749",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/749",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/zip",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/protected/bundle/GPP_surfaces_749.zip",
-                    "description": "Collection bundle",
                     "@type": "dcat:Distribution",
+                    "description": "Collection bundle",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/protected/bundle/GPP_surfaces_749.zip",
+                    "mediaType": "application/zip",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/bigfoot_val/LAI_surfaces/comp/bf_gpp_surf_guide.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/bigfoot_val/LAI_surfaces/comp/bf_gpp_surf_guide.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/bigfoot_val/LAI_surfaces/comp/BigFoot_readme.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/bigfoot_val/LAI_surfaces/comp/BigFoot_readme.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://daac.ornl.gov/graphics/browse/project/square/bigfoot_logo_square.png",
-                    "description": "Browse Image",
                     "@type": "dcat:Distribution",
+                    "description": "Browse Image",
+                    "downloadURL": "https://daac.ornl.gov/graphics/browse/project/square/bigfoot_logo_square.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 }
             ],
+            "graphic-preview-description": "Browse Image",
+            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/bigfoot_logo_square.png",
+            "identifier": "C2751481399-ORNL_CLOUD",
+            "issued": "2023-07-26",
+            "keyword": [
+                "earth science",
+                "biosphere",
+                "ecological dynamics"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/749",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2024-10-01",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "ORNL_DAAC"
+            },
             "spatial": "-156.61 -2.86 -54.96 71.27",
+            "temporal": "2000-01-01T00:00:00Z/2004-12-31T23:59:59Z",
             "theme": [
                 "BigFoot",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "BigFoot GPP Surfaces for North and South American Sites, 2000-2004"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/AURA/TES/TL3HNOM_L3.004",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2015-06-01. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/AURA/TES/TL3HNOM_L3.004. https://asdc.larc.nasa.gov/project/TES.",
-            "issued": "2013-01-18",
-            "temporal": "2004-08-22T00:00:00Z/2005-03-31T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2019-06-19",
-            "keyword": [
-                "atmospheric chemistry",
-                "atmosphere",
-                "air quality",
-                "earth science"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Reinhard Beer",
                 "hasEmail": "mailto:reinhard.beer@jpl.nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/LARC/SD/ASDC"
-            },
-            "identifier": "C1000000600-LARC",
             "description": "TL3HNOM_4 is the Tropospheric Emission Spectrometer (TES)/Aura Level 2 Atmospheric Temperatures Limb Version 4 data product. It consists of monthly averages of atmospheric temperature and VMR for atmospheric species are provided at 2 deg. lat. X 4 deg. long. spatial grids and at a subset of TES standard pressure levels. Algorithms for deriving TES L3 data will be provided in the data files.",
-            "title": "TES/Aura L3 HNO3 Monthly Gridded V004",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAURA%2FTES%2FTL3HNOM_L3.004",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAURA%2FTES%2FTL3HNOM_L3.004",
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
-                    "downloadURL": "https://asdc.larc.nasa.gov/project/TES",
-                    "description": "ASDC Data and Information for TES",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Data and Information for TES",
+                    "downloadURL": "https://asdc.larc.nasa.gov/project/TES",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
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
-                    "downloadURL": "https://l0dup05.larc.nasa.gov/cgi-bin/DUE/tes_L3monthly.cgi",
-                    "description": "Report of TES Level 3 Monthly Data Products Available from the ASDC",
                     "@type": "dcat:Distribution",
+                    "description": "Report of TES Level 3 Monthly Data Products Available from the ASDC",
+                    "downloadURL": "https://l0dup05.larc.nasa.gov/cgi-bin/DUE/tes_L3monthly.cgi",
+                    "mediaType": "text/html",
                     "title": "View this dataset's production history"
                 },
                 {
-                    "mediaType": "application/pdf",
```

