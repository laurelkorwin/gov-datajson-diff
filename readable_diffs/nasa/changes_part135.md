# Change History for nasa.json (Part 135)

### Changes from 31606f9 to dd2190f (Part 124/162)
**Author:** Automated

**Date:** 2025-02-01 15:02:16+00:00

**Message:** Updated data: Sat Feb  1 15:02:16 UTC 2025

```diff
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://reason.gesdisc.eosdis.nasa.gov/data/Snow_Ice/NHICEM.001/doc/README.NHSNOWICE.pdf",
-                    "description": "README Document",
                     "@type": "dcat:Distribution",
+                    "description": "README Document",
+                    "downloadURL": "https://reason.gesdisc.eosdis.nasa.gov/data/Snow_Ice/NHICEM.001/doc/README.NHSNOWICE.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's read me document"
                 }
             ],
+            "graphic-preview-description": "Sample image of Northern hemisphere monthly ice occurrence frequency (%), Jan 2010",
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/NHICEM_001.gif",
+            "identifier": "C1239898024-GES_DISC",
+            "issue-identification": "NHICEM",
+            "issued": "2009-03-10",
+            "keyword": [
+                "frozen ground",
+                "cryosphere",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/EJ3IACEJDYP8",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2014-11-30",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
+            },
+            "release-place": "NASA GSFC",
+            "series-name": "NHICEM",
             "spatial": "-180.0 0.0 180.0 90.0",
+            "temporal": "2000-01-01T00:00:00Z/2014-11-30T23:59:59.999Z",
             "theme": [
                 "NEESPI NASA",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Northern Hemisphere Ice Cover Monthly Statistics at 1 Degree Resolution V001 (NHICEM) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1760",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Yi, Y., and J.S. Kimball. 2020. ABoVE: Active Layer Thickness from Remote Sensing Permafrost Model, Alaska, 2001-2015. ORNL DAAC, Oak Ridge, Tennessee, USA. https://doi.org/10.3334/ORNLDAAC/1760",
-            "issued": "2020-05-06",
-            "temporal": "2001-01-01T00:00:00Z/2015-12-31T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-17",
-            "keyword": [
-                "frozen ground",
-                "snow/ice",
-                "ngda",
-                "national geospatial data asset",
-                "land surface",
-                "earth science",
-                "cryosphere",
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
-            "identifier": "C2143402571-ORNL_CLOUD",
             "description": "This dataset provides annual estimates of active layer thickness (ALT) at 1 km resolution across Alaska from 2001-2015. The ALT was estimated using a remote sensing-based soil process model incorporating global satellite data from Moderate Resolution Imaging Spectroradiometer (MODIS) land surface temperature (LST) and snow cover extent (SCE), and Soil Moisture Active and Passive (SMAP) satellite soil moisture records. The study area covers the majority land area of Alaska except for areas of perennial ice/snow cover or open water. The ALT was defined as the maximum soil thawing depth throughout the year. The mean ALT and mean uncertainty from 2001 to 2015 are also provided.",
-            "graphic-preview-description": "Model-simulated 1 km mean active layer thickness (ALT) map from 2001 to 2015. Black dots are locations of circumpolar active layer monitoring (CALM) sites used for comparison of observed ALT to modeled ALT. CALM data are not provided. The areas with ALT greater than 300 cm depth are shown in dark gray. (Source: Yi et al. 2018)",
-            "title": "ABoVE: Active Layer Thickness from Remote Sensing Permafrost Model, Alaska, 2001-2015",
-            "graphic-preview-file": "https://daac.ornl.gov/ABOVE/guides/Sat_ActiveLayer_Thickness_Maps_Fig1.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1760",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1760",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/above/Sat_ActiveLayer_Thickness_Maps/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/above/Sat_ActiveLayer_Thickness_Maps/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/ABOVE/guides/Sat_ActiveLayer_Thickness_Maps.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/ABOVE/guides/Sat_ActiveLayer_Thickness_Maps.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1760",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1760",
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
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/Sat_ActiveLayer_Thickness_Maps/comp/Sat_ActiveLayer_Thickness_Maps.pdf",
-                    "description": "ABoVE: Satellite-based Active Layer Thickness Maps, Alaska, 2001-2015: Sat_ActiveLayer_Thickness_Maps.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "ABoVE: Satellite-based Active Layer Thickness Maps, Alaska, 2001-2015: Sat_ActiveLayer_Thickness_Maps.pdf",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/Sat_ActiveLayer_Thickness_Maps/comp/Sat_ActiveLayer_Thickness_Maps.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://daac.ornl.gov/ABOVE/guides/Sat_ActiveLayer_Thickness_Maps_Fig1.png",
-                    "description": "Model-simulated 1 km mean active layer thickness (ALT) map from 2001 to 2015. Black dots are locations of circumpolar active layer monitoring (CALM) sites used for comparison of observed ALT to modeled ALT. CALM data are not provided. The areas with ALT greater than 300 cm depth are shown in dark gray. (Source: Yi et al. 2018)",
                     "@type": "dcat:Distribution",
+                    "description": "Model-simulated 1 km mean active layer thickness (ALT) map from 2001 to 2015. Black dots are locations of circumpolar active layer monitoring (CALM) sites used for comparison of observed ALT to modeled ALT. CALM data are not provided. The areas with ALT greater than 300 cm depth are shown in dark gray. (Source: Yi et al. 2018)",
+                    "downloadURL": "https://daac.ornl.gov/ABOVE/guides/Sat_ActiveLayer_Thickness_Maps_Fig1.png",
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
+            "graphic-preview-description": "Model-simulated 1 km mean active layer thickness (ALT) map from 2001 to 2015. Black dots are locations of circumpolar active layer monitoring (CALM) sites used for comparison of observed ALT to modeled ALT. CALM data are not provided. The areas with ALT greater than 300 cm depth are shown in dark gray. (Source: Yi et al. 2018)",
+            "graphic-preview-file": "https://daac.ornl.gov/ABOVE/guides/Sat_ActiveLayer_Thickness_Maps_Fig1.png",
+            "identifier": "C2143402571-ORNL_CLOUD",
+            "issued": "2020-05-06",
+            "keyword": [
+                "frozen ground",
+                "snow/ice",
+                "ngda",
+                "national geospatial data asset",
+                "land surface",
+                "earth science",
+                "cryosphere",
+                "soils"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1760",
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
             "spatial": "-179.18 55.57 -132.58 70.21",
+            "temporal": "2001-01-01T00:00:00Z/2015-12-31T23:59:59Z",
             "theme": [
                 "ABoVE",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "ABoVE: Active Layer Thickness from Remote Sensing Permafrost Model, Alaska, 2001-2015"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG1-J-PRA-4-SUMM-BROWSE-48SEC-V1.0",
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
+            "description": "This data set consists of edited browse data derived from an original data set obtained from the Voyager 1 Planetary Radio Astronomy (PRA) instrument in the vicinity of Jupiter.  Data are provided for 70 instrument channels covering the range from 1.2 kHz to 1326 kHz in uniform 19.2 kHz steps, each 1 kHz wide. Data are included for the period 1979-01-06 00:00:48 through 1979-04-13 23:58:24.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg1-j-pra-4-summ-browse-48sec-v1.0_reku-jbpk",
+            "issued": "2021-05-21",
+            "keyword": [
+                "jupiter",
+                "voyager"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG1-J-PRA-4-SUMM-BROWSE-48SEC-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg1-j-pra-4-summ-browse-48sec-v1.0_reku-jbpk",
-            "description": "This data set consists of edited browse data derived from an original data set obtained from the Voyager 1 Planetary Radio Astronomy (PRA) instrument in the vicinity of Jupiter.  Data are provided for 70 instrument channels covering the range from 1.2 kHz to 1326 kHz in uniform 19.2 kHz steps, each 1 kHz wide. Data are included for the period 1979-01-06 00:00:48 through 1979-04-13 23:58:24.",
-            "title": "VG1 JUP PRA RESAMPLED SUMMARY BROWSE\n                                         48SEC V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "VG1 JUP PRA RESAMPLED SUMMARY BROWSE\n                                         48SEC V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/LIS/LIS-OTD/DATA306",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Cecil, Daniel J.2003. LIS/OTD 2.5 Degree Low Resolution Annual Climatology Time Series (LRACTS) [indicate subset used]. Dataset available online from the NASA Global Hydrometeorology Resource Center DAAC, Huntsville, Alabama, U.S.A. DOI: http://dx.doi.org/10.5067/LIS/LIS-OTD/DATA306",
-            "issued": "2003-05-14",
-            "temporal": "1995-05-04T00:00:00Z/2015-04-08T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-04-28",
-            "keyword": [
-                "atmosphere",
-                "atmospheric electricity",
-                "weather events",
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
-            "identifier": "C1995863430-GHRC_DAAC",
             "description": "The LIS/OTD 2.5 Degree Low Resolution Annual Climatology Time Series (LRACTS) consists of gridded climatologies of total lightning flash rates seen by the spaceborne Optical Transient Detector (OTD) and Lightning Imaging Sensor (LIS). The long LIS (equatorward of about 38 degree) record makes the merged climatology most robust in the tropics and subtropics, while the high latitude data is entirely from OTD. The LRACTS dataset include annual flash rate time series data in MP4 format.",
-            "graphic-preview-description": "N/A",
-            "title": "LIS/OTD 2.5 Degree Low Resolution Annual Climatology Time Series (LRACTS) V2.3.2015",
-            "graphic-preview-file": "https://ghrc.nsstc.nasa.gov/pub/lis/climatology/LIS-OTD/LRACTS/animations/",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FLIS%2FLIS-OTD%2FDATA306",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FLIS%2FLIS-OTD%2FDATA306",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=lolracts",
-                    "description": "Files may be downloaded directly to your workstation from this link",
                     "@type": "dcat:Distribution",
+                    "description": "Files may be downloaded directly to your workstation from this link",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=lolracts",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/browse_sample/ghrc/lis/lisotd/lolracts/LRACTS_COM_V2.3.2015.jpg",
-                    "description": "Browse Sample",
                     "@type": "dcat:Distribution",
+                    "description": "Browse Sample",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/browse_sample/ghrc/lis/lisotd/lolracts/LRACTS_COM_V2.3.2015.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://ntrs.nasa.gov/archive/nasa/casi.ntrs.nasa.gov/20110015779.pdf",
-                    "description": "The 13 years of TRMM Lightning Imaging Sensor: From individual flash characteristics to decadal tendencies",
                     "@type": "dcat:Distribution",
+                    "description": "The 13 years of TRMM Lightning Imaging Sensor: From individual flash characteristics to decadal tendencies",
+                    "downloadURL": "https://ntrs.nasa.gov/archive/nasa/casi.ntrs.nasa.gov/20110015779.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://dx.doi.org/10.1029/2002JD002347",
-                    "description": "Global frequency and distribution of lightning as observed from space by the Optical Transient Detector",
                     "@type": "dcat:Distribution",
+                    "description": "Global frequency and distribution of lightning as observed from space by the Optical Transient Detector",
+                    "downloadURL": "https://dx.doi.org/10.1029/2002JD002347",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://dx.doi.org/10.5067/LIS/LIS-OTD/DATA311",
-                    "description": "Digital Object Identifier for a collection of related datasets",
                     "@type": "dcat:Distribution",
+                    "description": "Digital Object Identifier for a collection of related datasets",
+                    "downloadURL": "https://dx.doi.org/10.5067/LIS/LIS-OTD/DATA311",
+                    "mediaType": "text/html",
                     "title": "View information related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/doc/lis_climatology/LISOTD_climatology_dataset.pdf",
-                    "description": "LIS/OTD Climatology Dataset Collection User Guide",
                     "@type": "dcat:Distribution",
+                    "description": "LIS/OTD Climatology Dataset Collection User Guide",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/doc/lis_climatology/LISOTD_climatology_dataset.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/msword",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/doc/lis_climatology/LISOTD_Climo_prod_table.doc",
-                    "description": "Products in LIS-OTD gridded climatology files",
                     "@type": "dcat:Distribution",
+                    "description": "Products in LIS-OTD gridded climatology files",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/doc/lis_climatology/LISOTD_Climo_prod_table.doc",
+                    "mediaType": "application/msword",
                     "title": "View the primary investigator's documentation for this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://dx.doi.org/10.1016/j.atmosres.2012.06.028",
-                    "description": "Gridded lightning climatology from TRMM-LIS and OTD: Dataset description",
                     "@type": "dcat:Distribution",
+                    "description": "Gridded lightning climatology from TRMM-LIS and OTD: Dataset description",
+                    "downloadURL": "http://dx.doi.org/10.1016/j.atmosres.2012.06.028",
+                    "mediaType": "text/html",
                     "title": "View the documentation for this dataset's algorithms"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/doc/lis_climatology/getgrid.pro",
-                    "description": "Read SDS Arrays From an A HDF file",
                     "@type": "dcat:Distribution",
+                    "description": "Read SDS Arrays From an A HDF file",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/doc/lis_climatology/getgrid.pro",
+                    "mediaType": "text/html",
                     "title": "Downloadable software applications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/doc/lis_climatology/read_sds.pro",
-                    "description": "Read an SDS grid from the LIS/OTD HDF climatology files",
                     "@type": "dcat:Distribution",
+                    "description": "Read an SDS grid from the LIS/OTD HDF climatology files",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/doc/lis_climatology/read_sds.pro",
+                    "mediaType": "text/html",
                     "title": "Downloadable software applications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/lightning/",
-                    "description": "Lightning Imaging Sensor (LIS) Overview",
                     "@type": "dcat:Distribution",
+                    "description": "Lightning Imaging Sensor (LIS) Overview",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/lightning/",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/lis/climatology/LIS-OTD/LRACTS/animations/",
-                    "description": "N/A",
                     "@type": "dcat:Distribution",
+                    "description": "N/A",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/lis/climatology/LIS-OTD/LRACTS/animations/",
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
+            "graphic-preview-file": "https://ghrc.nsstc.nasa.gov/pub/lis/climatology/LIS-OTD/LRACTS/animations/",
+            "identifier": "C1995863430-GHRC_DAAC",
+            "issued": "2003-05-14",
+            "keyword": [
+                "atmosphere",
+                "atmospheric electricity",
+                "weather events",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/LIS/LIS-OTD/DATA306",
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
             "spatial": "-178.75 -88.75 178.75 88.75",
+            "temporal": "1995-05-04T00:00:00Z/2015-04-08T23:59:59Z",
             "theme": [
                 "LIS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "LIS/OTD 2.5 Degree Low Resolution Annual Climatology Time Series (LRACTS) V2.3.2015"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NEAR-A-GRS-2-EDR-CRUISE3-V1.0",
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
-                "near earth asteroid rendezvous",
-                "solar system"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This data set contains Gamma Ray Spectrometer (GRS) observations made during the third cruise phase of the NEAR mission. The individual observations are combined into a single file per day for each sensor.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.near-a-grs-2-edr-cruise3-v1.0_rend-6q54",
+            "issued": "2021-05-21",
+            "keyword": [
+                "near earth asteroid rendezvous",
+                "solar system"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NEAR-A-GRS-2-EDR-CRUISE3-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.near-a-grs-2-edr-cruise3-v1.0_rend-6q54",
-            "description": "This data set contains Gamma Ray Spectrometer (GRS) observations made during the third cruise phase of the NEAR mission. The individual observations are combined into a single file per day for each sensor.",
-            "title": "NEAR GRS SPECTRA FOR CRUISE 3 PHASE",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "NEAR GRS SPECTRA FOR CRUISE 3 PHASE"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-4-EXT3-67PCHURYUMOV-M31-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This CODMAC level 4 data set contains radiometric calibrated and geometric distortion corrected (resampled) image data in W/m^2/sr/nm acquired by the OSIRIS Narrow Angle Camera during the ROSETTA EXTENSION 3 phase of the Rosetta mission, covering the period from 2016-06-28T23:25:00.000 to 2016-07-26T23:24:59.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-4-ext3-67pchuryumov-m31-v1.0",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2021-05-21",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "16 cyg b",
                 "67p/churyumov-gerasimenko 1 (1969 r1)",
                 "international rosetta mission"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-4-EXT3-67PCHURYUMOV-M31-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-4-ext3-67pchuryumov-m31-v1.0",
-            "description": "This CODMAC level 4 data set contains radiometric calibrated and geometric distortion corrected (resampled) image data in W/m^2/sr/nm acquired by the OSIRIS Narrow Angle Camera during the ROSETTA EXTENSION 3 phase of the Rosetta mission, covering the period from 2016-06-28T23:25:00.000 to 2016-07-26T23:24:59.000.",
-            "title": "ROSETTA-ORBITER 67P OSINAC 4 EXT3-MTP031 RDR V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P OSINAC 4 EXT3-MTP031 RDR V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/AQR50-3RCCE",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "NASA Aquarius project. 2017-12-07. Aquarius Official Release Level 3 Ancillary Reynolds Sea Surface Temperature Standard Mapped Image Mission Cumulative Data. Version 5.0. Aquarius Sea Surface Salinity Products. Goddard Space Flight Center, 8800 Greenbelt Rd.; Greeenbelt, MD., 20771, USA. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/GSFC OBPG. https://doi.org/10.5067/AQR50-3RCCE. http://podaac.jpl.nasa.gov/SeaSurfaceSalinity/Aquarius. NASA Aquarius project, NASA/GSFC OBPG, 2017-12-07, Aquarius Official Release Level 3 Ancillary Reynolds Sea Surface Temperature Standard Mapped Image Mission Cumulative Data V5.0, http://podaac.jpl.nasa.gov/SeaSurfaceSalinity/Aquarius.",
-            "issued": "2017-10-21",
-            "temporal": "2011-08-25T01:45:23Z/2015-06-07T12:45:21Z",
-            "@type": "dcat:Dataset",
-            "modified": "2017-12-07",
-            "keyword": [
-                "earth science",
-                "oceans",
-                "ocean temperature"
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
-            "identifier": "C2491755393-POCLOUD",
-            "description": "Aquarius Level 3 ancillary sea surface temperature (SST) standard mapped image data are the ancillary SST data used in the Aquarius calibration for salinity retrieval.  They are simply the daily SSTs from the Reynolds National Climatic Data Center (NCDC) 0.25 degree dataset, gridded and averaged using the Aquarius processing L2-L3 processing scheme to the same 1 degree spatial resolution and daily, 7 day, monthly, seasonal, and annual time intervals as Aquarius L3 standard salinity and wind speed products.  This particular data set is the mission series mean or cumulative ancillary sea surface temperature product associated with version 5.0 of the Aquarius data set.",
-            "release-place": "Goddard Space Flight Center, 8800 Greenbelt Rd.; Greeenbelt, MD., 20771, USA",
-            "series-name": "Aquarius Official Release Level 3 Ancillary Reynolds Sea Surface Temperature Standard Mapped Image Mission Cumulative Data",
-            "graphic-preview-description": "Thumbnail",
             "creator": "NASA Aquarius project",
-            "title": "Aquarius Official Release Level 3 Ancillary Reynolds Sea Surface Temperature Standard Mapped Image Mission Cumulative Data V5.0",
-            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/AQUARIUS_L3_ANCILLARY_SST_SMI_CUMULATIVE_V5.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "Aquarius Level 3 ancillary sea surface temperature (SST) standard mapped image data are the ancillary SST data used in the Aquarius calibration for salinity retrieval.  They are simply the daily SSTs from the Reynolds National Climatic Data Center (NCDC) 0.25 degree dataset, gridded and averaged using the Aquarius processing L2-L3 processing scheme to the same 1 degree spatial resolution and daily, 7 day, monthly, seasonal, and annual time intervals as Aquarius L3 standard salinity and wind speed products.  This particular data set is the mission series mean or cumulative ancillary sea surface temperature product associated with version 5.0 of the Aquarius data set.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAQR50-3RCCE",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAQR50-3RCCE",
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
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/AQUARIUS_L3_ANCILLARY_SST_SMI_CUMULATIVE_V5.jpg",
-                    "description": "Thumbnail",
                     "@type": "dcat:Distribution",
+                    "description": "Thumbnail",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/AQUARIUS_L3_ANCILLARY_SST_SMI_CUMULATIVE_V5.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
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
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2491755393-POCLOUD",
-                    "description": "HTTPS endpoint for data browse and download",
                     "@type": "dcat:Distribution",
+                    "description": "HTTPS endpoint for data browse and download",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2491755393-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2491755393-POCLOUD",
-                    "description": "Browse granule search results in Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse granule search results in Earthdata Search",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2491755393-POCLOUD",
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
+            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/AQUARIUS_L3_ANCILLARY_SST_SMI_CUMULATIVE_V5.jpg",
+            "identifier": "C2491755393-POCLOUD",
+            "issued": "2017-10-21",
+            "keyword": [
+                "earth science",
+                "oceans",
+                "ocean temperature"
+            ],
+            "landingPage": "https://doi.org/10.5067/AQR50-3RCCE",
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
+            "series-name": "Aquarius Official Release Level 3 Ancillary Reynolds Sea Surface Temperature Standard Mapped Image Mission Cumulative Data",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2011-08-25T01:45:23Z/2015-06-07T12:45:21Z",
             "theme": [
                 "AQUARIUS SAC-D",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Aquarius Official Release Level 3 Ancillary Reynolds Sea Surface Temperature Standard Mapped Image Mission Cumulative Data V5.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "restricted public",
-            "landingPage": "https://pds.jpl.nasa.gov/tools/subscription_service/SS-Release.shtml",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2018-06-26",
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
+                    "downloadURL": "https://pds.jpl.nasa.gov/tools/subscription_service/SS-20110301.shtml",
+                    "mediaType": "application/html"
+                }
             ],
+            "identifier": "NASA-545",
+            "issued": "2018-06-26",
             "keyword": [
                 "ctx",
                 "sharad",
@@ -1301642,306 +1301651,277 @@
                 "spice",
                 "hirise"
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
-            "identifier": "NASA-545",
-            "description": "CRISM, CTX, HiRISE, MARCI, MCS, RSS, SHARAD, SPICE",
-            "title": "PDS Mars Reconnaissance Orbiter Data 16",
-            "programCode": [
-                "026:005"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://pds.jpl.nasa.gov/tools/subscription_service/SS-20110301.shtml",
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
+            "title": "PDS Mars Reconnaissance Orbiter Data 16"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/GOESRPLT/LIP/DATA101",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Blakeslee, Richard J. and Douglas M. Mach.2019. GOES-R PLT Lightning Instrument Package (LIP) [indicate subset used]. Dataset available online from the NASA Global Hydrometeorology Resource Center DAAC, Huntsville, Alabama, U.S.A. DOI: http://dx.doi.org/10.5067/GOESRPLT/LIP/DATA101",
-            "issued": "2019-02-21",
-            "temporal": "2017-03-21T18:30:00Z/2017-05-17T09:58:57Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-04-28",
-            "keyword": [
-                "earth science",
-                "atmosphere",
-                "atmospheric electricity"
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
-            "identifier": "C1979116062-GHRC_DAAC",
             "description": "The GOES-R PLT Lightning Instrument Package (LIP) dataset consists of electrical field measurements of lightning and navigation data collected by the Lightning Instrument Package (LIP) flown aboard a NASA ER-2 high-altitude aircraft during the GOES-R Post Launch Test (PLT) airborne science field campaign. The GOES-R PLT airborne science field campaign took place between March 21 and May 17, 2017 in support of the post-launch product validation of the Advanced Baseline Imager (ABI) and the Geostationary Lightning Mapper (GLM).  These data files are available in ASCII format with browse imagery available in PDF format.",
-            "graphic-preview-description": "N/A",
-            "title": "GOES-R PLT Lightning Instrument Package (LIP) V1",
-            "graphic-preview-file": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/goesrplt/LIP/browse/",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGOESRPLT%2FLIP%2FDATA101",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGOESRPLT%2FLIP%2FDATA101",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=goesrpltlip",
-                    "description": "Files may be downloaded directly to your workstation from this link",
                     "@type": "dcat:Distribution",
+                    "description": "Files may be downloaded directly to your workstation from this link",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=goesrpltlip",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/goesrplt/LIP/browse/goesr_plt_lip_20170321_1930_browsesample.png",
-                    "description": "Sample browse image",
                     "@type": "dcat:Distribution",
+                    "description": "Sample browse image",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/goesrplt/LIP/browse/goesr_plt_lip_20170321_1930_browsesample.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://dx.doi.org/10.5067/GOESRPLT/DATA101",
-                    "description": "GOES-R PLT Field Campaign Collection DOI",
                     "@type": "dcat:Distribution",
+                    "description": "GOES-R PLT Field Campaign Collection DOI",
+                    "downloadURL": "http://dx.doi.org/10.5067/GOESRPLT/DATA101",
+                    "mediaType": "text/html",
                     "title": "View information related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/goesrplt/LIP/doc/goesrpltlip_dataset.pdf",
-                    "description": "The guide document contains detailed information about the dataset",
                     "@type": "dcat:Distribution",
+                    "description": "The guide document contains detailed information about the dataset",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/goesrplt/LIP/doc/goesrpltlip_dataset.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
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
-                    "downloadURL": "https://doi.org/10.1175/JTECH2039.1",
-                    "description": "A low-noise, microprocessor-controlled, internally digitizing rotating-vane electric field mill for airborne platforms",
                     "@type": "dcat:Distribution",
+                    "description": "A low-noise, microprocessor-controlled, internally digitizing rotating-vane electric field mill for airborne platforms",
+                    "downloadURL": "https://doi.org/10.1175/JTECH2039.1",
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
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/goesrplt/LIP/browse/",
-                    "description": "N/A",
                     "@type": "dcat:Distribution",
+                    "description": "N/A",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/goesrplt/LIP/browse/",
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
+            "graphic-preview-file": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/goesrplt/LIP/browse/",
+            "identifier": "C1979116062-GHRC_DAAC",
+            "issued": "2019-02-21",
+            "keyword": [
+                "earth science",
+                "atmosphere",
+                "atmospheric electricity"
+            ],
+            "landingPage": "https://doi.org/10.5067/GOESRPLT/LIP/DATA101",
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
             "spatial": "-124.625 26.449 -72.202 43.573",
+            "temporal": "2017-03-21T18:30:00Z/2017-05-17T09:58:57Z",
             "theme": [
                 "GOES-R PLT",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "GOES-R PLT Lightning Instrument Package (LIP) V1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C3307842625-OMINRT.html",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2024-11-14",
-            "temporal": "2018-01-16T00:00:00Z/2024-12-02T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-14",
-            "keyword": [
-                "earth science",
-                "atmosphere",
-                "aerosols"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "undefined",
                 "hasEmail": "mailto:cmr-support@earthdata.nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Not provided"
-            },
-            "identifier": "C3307842625-OMINRT",
             "description": "The OMPS-N21 L2 NM Aerosol Index swath orbital V2 for Near Real Time. For the standard product see the OMPS_N21_NMUVAI_L2  product in CMR .The aerosol index is derived from normalized radiances using 2 wavelength pairs at 340 and 378.5 nm. Additionally, this data product contains measurements of normalized radiances, reflectivity, cloud fraction, reflectivity, and other ancillary variables.",
-            "title": "OMPS-N21 L2 NM Aerosol Index swath orbital NRT",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://omisips1.omisips.eosdis.nasa.gov/outgoing/OMPS/LANCE/NMUVAI-L2-NRT",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://omisips1.omisips.eosdis.nasa.gov/outgoing/OMPS/LANCE/NMUVAI-L2-NRT",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 }
             ],
+            "identifier": "C3307842625-OMINRT",
+            "issued": "2024-11-14",
+            "keyword": [
+                "earth science",
+                "atmosphere",
+                "aerosols"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C3307842625-OMINRT.html",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2024-11-14",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Not provided"
+            },
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2018-01-16T00:00:00Z/2024-12-02T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "OMPS-N21 L2 NM Aerosol Index swath orbital NRT"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C2331489766-OB_DAAC.html",
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
-                "biosphere",
-                "ecosystems",
-                "earth science",
-                "ngda",
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
-            "identifier": "C2331489766-OB_DAAC",
             "description": "The Ocean Biology DAAC produces near real-time (quicklook) products using the best-available combination of ancillary data from meteorological and ozone data. As such, the inputs and the calibration used are less than optimal. Quicklook products provide a snapshot of the data during a short time period within a single orbit.",
-            "title": "Terra MODIS Global Binned Inherent Optical Properties (IOP) - Near Real-time (NRT) Data, version R2022.0",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://oceandata.sci.gsfc.nasa.gov/directdataaccess/Level-3%20Binned/Terra-MODIS/",
-                    "description": "NASA Ocean Color Web - Data Distribution Site",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Ocean Color Web - Data Distribution Site",
+                    "downloadURL": "https://oceandata.sci.gsfc.nasa.gov/directdataaccess/Level-3%20Binned/Terra-MODIS/",
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
-                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/data/10.5067/TERRA/MODIS/L3B/IOP/2022",
-                    "description": "MODIS-Terra L3B Inherent Optical Properties (IOP) - Near Real-time (NRT) Dataset Landing Page",
                     "@type": "dcat:Distribution",
+                    "description": "MODIS-Terra L3B Inherent Optical Properties (IOP) - Near Real-time (NRT) Dataset Landing Page",
+                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/data/10.5067/TERRA/MODIS/L3B/IOP/2022",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 }
             ],
+            "identifier": "C2331489766-OB_DAAC",
+            "issued": "2019-06-23",
+            "keyword": [
+                "oceans",
+                "national geospatial data asset",
+                "biosphere",
+                "ecosystems",
+                "earth science",
+                "ngda",
+                "ocean optics"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C2331489766-OB_DAAC.html",
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
+            "title": "Terra MODIS Global Binned Inherent Optical Properties (IOP) - Near Real-time (NRT) Data, version R2022.0"
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
-                "dictionary",
-                "pds",
-                "index"
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
-            "identifier": "NASA-640",
             "description": "Data Dictionary and Index Files",
-            "title": "PDS Data Dictionary (1r70)",
-            "programCode": [
-                "026:005"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -1301949,138 +1301929,138 @@
                     "mediaType": "application/html"
                 }
             ],
-            "accrualPeriodicity": "irregular",
+            "identifier": "NASA-640",
+            "issued": "2018-06-25",
+            "keyword": [
+                "dictionary",
+                "pds",
+                "index"
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
+            "title": "PDS Data Dictionary (1r70)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1563",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Numata, I., M.A. Cochrane, J. Kjaersgaard, and S.S. da Silva. 2018. Forest Inventories at Burned and Unburned Tropical Forest Sites, Acre, Brazil, 2014. ORNL DAAC, Oak Ridge, Tennessee, USA. https://doi.org/10.3334/ORNLDAAC/1563",
-            "issued": "2018-02-26",
-            "temporal": "2014-07-01T00:00:00Z/2014-08-31T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-09-11",
-            "keyword": [
-                "vegetation",
-                "natural hazards",
-                "earth science",
-                "ecosystems",
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
-            "identifier": "C2764882625-ORNL_CLOUD",
             "description": "This dataset provides measurements for diameter at breast height (DBH) and species identification of trees for inventories taken at five tropical forest sites in Acre state, Brazil, in the southwestern Amazon region. The sites included one in a forest reserve (Reserva Bonal) and four within forest fragments situated on private property. The inventory sites included forests burned in 2005 and 2010 and also unburned forests. Surveys were conducted in July and August 2014.",
-            "graphic-preview-description": "Photos of recovering burned (left) and unburned (right) sampling sites show vegetation changes due to burning and recovery of aboveground biomass after burning. Photos courtesy of I. Numata.",
-            "title": "Forest Inventories at Burned and Unburned Tropical Forest Sites, Acre, Brazil, 2014",
-            "graphic-preview-file": "https://daac.ornl.gov/VEGETATION/guides/Forest_Inventory_Data_Brazil_Fig1.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1563",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1563",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/global_vegetation/Forest_Inventory_Data_Brazil/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/global_vegetation/Forest_Inventory_Data_Brazil/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/VEGETATION/guides/Forest_Inventory_Data_Brazil.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/VEGETATION/guides/Forest_Inventory_Data_Brazil.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1563",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1563",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/global_vegetation/Forest_Inventory_Data_Brazil/comp/Forest_Inventory_Data_Brazil.pdf",
-                    "description": "Inventory of Burned and Unburned Tropical Forest Sites, Acre, Brazil, 2014: Forest_Inventory_Data_Brazil.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "Inventory of Burned and Unburned Tropical Forest Sites, Acre, Brazil, 2014: Forest_Inventory_Data_Brazil.pdf",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/global_vegetation/Forest_Inventory_Data_Brazil/comp/Forest_Inventory_Data_Brazil.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://daac.ornl.gov/VEGETATION/guides/Forest_Inventory_Data_Brazil_Fig1.png",
-                    "description": "Photos of recovering burned (left) and unburned (right) sampling sites show vegetation changes due to burning and recovery of aboveground biomass after burning. Photos courtesy of I. Numata.",
                     "@type": "dcat:Distribution",
+                    "description": "Photos of recovering burned (left) and unburned (right) sampling sites show vegetation changes due to burning and recovery of aboveground biomass after burning. Photos courtesy of I. Numata.",
+                    "downloadURL": "https://daac.ornl.gov/VEGETATION/guides/Forest_Inventory_Data_Brazil_Fig1.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 }
             ],
+            "graphic-preview-description": "Photos of recovering burned (left) and unburned (right) sampling sites show vegetation changes due to burning and recovery of aboveground biomass after burning. Photos courtesy of I. Numata.",
+            "graphic-preview-file": "https://daac.ornl.gov/VEGETATION/guides/Forest_Inventory_Data_Brazil_Fig1.png",
+            "identifier": "C2764882625-ORNL_CLOUD",
+            "issued": "2018-02-26",
+            "keyword": [
+                "vegetation",
+                "natural hazards",
+                "earth science",
+                "ecosystems",
+                "human dimensions",
+                "biosphere"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1563",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2023-09-11",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "ORNL_DAAC"
+            },
             "spatial": "-67.64 -9.9 -67.02 -9.73",
+            "temporal": "2014-07-01T00:00:00Z/2014-08-31T23:59:59Z",
             "theme": [
                 "Vegetation",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Forest Inventories at Burned and Unburned Tropical Forest Sites, Acre, Brazil, 2014"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/AIRCRAFT/SEAC4RS/RADIANCE/AIRMSPI",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/AIRCRAFT/SEAC4RS/RADIANCE/AIRMSPI. http://eosweb.larc.nasa.gov/project/airmspi/airmspi_table.",
-            "issued": "2013-08-01",
-            "temporal": "2013-08-01T00:00:00Z/2013-09-23T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2013-09-23",
-            "keyword": [
-                "earth science",
-                "spectral/engineering",
-                "ultraviolet wavelengths",
-                "visible wavelengths"
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
-            "identifier": "C1459696669-LARC_ASDC",
             "description": "AirMSPI_SEAC4RS_Terrain-projected_Georegistered_Radiance_Data are AirMSPI terrain-projected georegistered radiance product acquired during the NASA SEAC4RS flight campaign.\nAirMSPI Level 1B2 products contain radiometric and polarimetric images of clouds, aerosols, and the surface of the Earth. In particular, products contain map-projected data at 8 wavelengths: 355, 380, 445, 470, 555, 660, 865, and 935 nm. The data products include radiance, time, solar zenith, solar azimuth, view zenith, and view azimuth for all spectral bands. Wavelengths for which polarization information is available (470, 660, and 865 nm) also include the Stokes parameters Q and U, as well as degree of linear polarization (DOLP) and angle of linear polarization (AOLP). Q, U, and AOLP are reported relative to both the scattering- and view meridian planes. Files are distributed in HDF-EOS-5 format.\nThis release of AirMSPI data contains all targets acquired during the Studies of Emissions and Atmospheric Composition, Clouds and Climate Coupling by Regional Surveys (SEAC4RS) flight campaign. SEAC4RS was primarily based out of Ellington Field in Houston, Texas (initial flights were based out of Armstrong Flight Research Center in Palmdale, CA), and focused on clouds and aerosols in the United States. AirMSPI data were acquired from August 1 through September 23, 2013.",
-            "title": "AirMSPI terrain-projected georegistered radiance product acquired during the NASA SEAC4RS flight campaign August-September 2013, V005",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAIRCRAFT%2FSEAC4RS%2FRADIANCE%2FAIRMSPI",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAIRCRAFT%2FSEAC4RS%2FRADIANCE%2FAIRMSPI",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
@@ -1302150,2072 +1302130,2074 @@
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C1459696669-LARC_ASDC",
+            "issued": "2013-08-01",
+            "keyword": [
+                "earth science",
+                "spectral/engineering",
+                "ultraviolet wavelengths",
+                "visible wavelengths"
+            ],
+            "landingPage": "https://doi.org/10.5067/AIRCRAFT/SEAC4RS/RADIANCE/AIRMSPI",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2013-09-23",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/LARC/SD/ASDC"
+            },
             "spatial": "-125.0 15.0 -74.0 52.0",
+            "temporal": "2013-08-01T00:00:00Z/2013-09-23T23:59:59Z",
             "theme": [
                 "AIRMSPI",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "AirMSPI terrain-projected georegistered radiance product acquired during the NASA SEAC4RS flight campaign August-September 2013, V005"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/VIIRS/VNP13A3.001",
             "citation": "Kamel Didan, Armando Barreto\r\n. 2018-07-19. VNP13A3. Version 001. VIIRS/NPP Vegetation Indices Monthly L3 Global 1km SIN Grid V001\r\n. Sioux Falls, South Dakota, USA. Archived by National Aeronautics and Space Administration, U.S. Government, NASA EOSDIS Land Processes Distributed Active Archive Center. https://doi.org/10.5067/VIIRS/VNP13A3.001. https://doi.org/10.5067/VIIRS/VNP13A3.001. Digital Science Data. This data set was provided by the NASA/NOAA NPP Project. The DOI landing page provides citations in APA and Chicago styles.\r\n.",
-            "issued": "2018-07-19",
-            "temporal": "2012-01-01T00:00:00Z/2024-06-03T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2018-07-19",
-            "keyword": [
-                "earth science",
-                "biosphere",
-                "vegetation"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Kamel Didan",
                 "hasEmail": "mailto:didan@email.arizona.edu"
             },
+            "creator": "Kamel Didan, Armando Barreto",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C1392010615-LPDAAC_ECS",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "LP DAAC"
-            },
             "description": "The NASA/NOAA Suomi National Polar-orbiting Partnership (Suomi NPP) Visible Infrared Imaging Radiometer Suite (VIIRS) Vegetation Indices (VNP13A3) Version 1 data product provides vegetation indices by a process of selecting the best available pixel over a monthly acquisition period at 1 kilometer (km) resolution. The VNP13 data products are designed after the Moderate Resolution Imaging Spectroradiometer (MODIS) Terra and Aqua Vegetation Indices product suite to promote the continuity of the Earth Observation System (EOS) mission.\r\n\r\nThe VNP13 algorithm process produces three vegetation indices: The Normalized Difference Vegetation Index (NDVI), the Enhanced Vegetation Index (EVI), and the Enhanced Vegetation Index-2 (EVI2). NDVI is one of the longest continual remotely sensed time series observations, using both the red and near-infrared (NIR) bands. EVI is a slightly different vegetation index that is more sensitive to canopy cover, while NDVI is more sensitive to chlorophyll. EVI2 is a reformation of the standard 3-band EVI, using the red band and NIR band. This reformation addresses arising issues when comparing VIIRS EVI to other EVI models that do not include a blue band. EVI2 will eventually become the standard EVI. \r\n\r\nAlong with the three Vegetation Indices layers, this product also includes layers for NIR reflectance; three shortwave infrared (SWIR) reflectance; red, blue, and green reflectance; pixel reliability; pixel reliability; relative azimuth, view, and sun angles; and a quality layer. Two low resolution browse images are also available for each VNP13A3 product: EVI and NDVI.",
-            "release-place": "Sioux Falls, South Dakota, USA",
-            "series-name": "VNP13A3",
-            "creator": "Kamel Didan, Armando Barreto",
-            "title": "VIIRS/NPP Vegetation Indices Monthly L3 Global 1km SIN Grid V001",
-            "graphic-preview-description": "Browse image for Earthdata Search",
-            "graphic-preview-file": "https://e4ftl01.cr.usgs.gov/WORKING/BRWS/Browse.001/2019.12.11/BROWSE.VNP13A3.A2019305.h13v09.001.2019345232006.2.jpg?_ga=2.190191019.1452435467.1577973160-2066674673.1574795892",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FVIIRS%2FVNP13A3.001",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FVIIRS%2FVNP13A3.001",
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
-                    "downloadURL": "https://doi.org/10.5067/VIIRS/VNP13A3.001",
-                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
+                    "downloadURL": "https://doi.org/10.5067/VIIRS/VNP13A3.001",
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
-                    "downloadURL": "https://e4ftl01.cr.usgs.gov/VIIRS/VNP13A3.001/",
-                    "description": "LP DAAC Data Pool provides direct access to available products via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "LP DAAC Data Pool provides direct access to available products via HTTPS.",
+                    "downloadURL": "https://e4ftl01.cr.usgs.gov/VIIRS/VNP13A3.001/",
+                    "mediaType": "application/x-hdf",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "application/x-hdf",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=C1392010615-LPDAAC_ECS",
-                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=C1392010615-LPDAAC_ECS",
+                    "mediaType": "application/x-hdf",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://e4ftl01.cr.usgs.gov/WORKING/BRWS/Browse.001/2019.12.11/BROWSE.VNP13A3.A2019305.h13v09.001.2019345232006.2.jpg?_ga=2.190191019.1452435467.1577973160-2066674673.1574795892",
-                    "description": "Browse image for Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse image for Earthdata Search",
+                    "downloadURL": "https://e4ftl01.cr.usgs.gov/WORKING/BRWS/Browse.001/2019.12.11/BROWSE.VNP13A3.A2019305.h13v09.001.2019345232006.2.jpg?_ga=2.190191019.1452435467.1577973160-2066674673.1574795892",
+                    "mediaType": "text/html",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://lpdaac.usgs.gov/documents/184/VNP13_User_Guide_ATBD_V2.1.2.pdf",
-                    "description": "The technical information in the User's Guide enables users to interpret and use the data products.",
                     "@type": "dcat:Distribution",
+                    "description": "The technical information in the User's Guide enables users to interpret and use the data products.",
+                    "downloadURL": "https://lpdaac.usgs.gov/documents/184/VNP13_User_Guide_ATBD_V2.1.2.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://lpdaac.usgs.gov/documents/184/VNP13_User_Guide_ATBD_V2.1.2.pdf",
-                    "description": "The ATBD provides physical theory and mathematical procedures for the calculations used to produce the data products.",
                     "@type": "dcat:Distribution",
+                    "description": "The ATBD provides physical theory and mathematical procedures for the calculations used to produce the data products.",
+                    "downloadURL": "https://lpdaac.usgs.gov/documents/184/VNP13_User_Guide_ATBD_V2.1.2.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's algorithm theoretical basis document"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/filespec/VIIRS/1/VNP13A3",
-                    "description": "The File Specification provides a description of the product file including Scientific Data Sets and their attributes.",
                     "@type": "dcat:Distribution",
+                    "description": "The File Specification provides a description of the product file including Scientific Data Sets and their attributes.",
+                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/filespec/VIIRS/1/VNP13A3",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://opendap.cr.usgs.gov/opendap/hyrax/VNP13A3.001/contents.html",
-                    "description": "Access data via Open-source Project for a Network Data Access Protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access data via Open-source Project for a Network Data Access Protocol.",
+                    "downloadURL": "https://opendap.cr.usgs.gov/opendap/hyrax/VNP13A3.001/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
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
                 }
             ],
+            "graphic-preview-description": "Browse image for Earthdata Search",
+            "graphic-preview-file": "https://e4ftl01.cr.usgs.gov/WORKING/BRWS/Browse.001/2019.12.11/BROWSE.VNP13A3.A2019305.h13v09.001.2019345232006.2.jpg?_ga=2.190191019.1452435467.1577973160-2066674673.1574795892",
+            "identifier": "C1392010615-LPDAAC_ECS",
+            "issued": "2018-07-19",
+            "keyword": [
+                "earth science",
+                "biosphere",
+                "vegetation"
+            ],
+            "landingPage": "https://doi.org/10.5067/VIIRS/VNP13A3.001",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2018-07-19",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "LP DAAC"
+            },
+            "release-place": "Sioux Falls, South Dakota, USA",
+            "series-name": "VNP13A3",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2012-01-01T00:00:00Z/2024-06-03T00:00:00Z",
             "theme": [
                 "NPP-JPSS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "VIIRS/NPP Vegetation Indices Monthly L3 Global 1km SIN Grid V001"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-A-LEISA-2-KEM1-V3.0",
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
-                "vega"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This data set contains Raw data taken by the New Horizons Linear Etalon Imaging Spectral Array instrument during the KEM1 ENCOUNTER mission phase.  This is VERSION 3.0 of this data set. This data set contains LEISA observations taken for functional testing, and Arrokoth [ASTEROID 486958 (2014 MU69)] Encounter operations, including a test of a slow scan rate. Many LEISA Composition and System Scans along with some LEISA Scans as a LORRI Rider. This data set contains data acquired by the spacecraft between 08/14/2018 and 07/31/2019. It only includes data downlinked before 08/01/2019. Future datasets may include more data acquired by the spacecraft after 08/13/2018 but downlinked after 07/31/2019.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-a-leisa-2-kem1-v3.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "new horizons kuiper belt extended mission",
+                "vega"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-A-LEISA-2-KEM1-V3.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-a-leisa-2-kem1-v3.0",
-            "description": "This data set contains Raw data taken by the New Horizons Linear Etalon Imaging Spectral Array instrument during the KEM1 ENCOUNTER mission phase.  This is VERSION 3.0 of this data set. This data set contains LEISA observations taken for functional testing, and Arrokoth [ASTEROID 486958 (2014 MU69)] Encounter operations, including a test of a slow scan rate. Many LEISA Composition and System Scans along with some LEISA Scans as a LORRI Rider. This data set contains data acquired by the spacecraft between 08/14/2018 and 07/31/2019. It only includes data downlinked before 08/01/2019. Future datasets may include more data acquired by the spacecraft after 08/13/2018 but downlinked after 07/31/2019.",
-            "title": "NEW HORIZONS\n      LEISA KEM1\n      RAW V3.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "NEW HORIZONS\n      LEISA KEM1\n      RAW V3.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/MODIS/MOD05_L2.061",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "MODIS Science Team. 2017-11-01. MODIS/Terra Total Precipitable Water Vapor 5-Min L2 Swath 1km and 5km. Version 6.1. MODAPS at NASA/GSFC. Archived by National Aeronautics and Space Administration, U.S. Government, L1 and Atmosphere Archive and Distribution System (LAADS). https://doi.org/10.5067/MODIS/MOD05_L2.061. https://doi.org/10.5067/MODIS/MOD05_L2.061.",
-            "issued": "2017-11-01",
-            "temporal": "2000-02-24T00:00:00Z/2025-01-20T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-17",
-            "keyword": [
-                "national geospatial data asset",
-                "ngda",
-                "atmosphere",
-                "atmospheric water vapor",
-                "earth science"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "ASAD ULLAH",
                 "hasEmail": "mailto:MODAPSUSO@lists.nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Not provided"
-            },
-            "identifier": "C1443531026-LAADS",
-            "description": "The MODIS/Terra Total Precipitable Water Vapor 5-Min L2 Swath 1km and 5km (MOD05_L2) product consists of atmospheric column water-vapor amounts. This product is derived from data collected by the Moderate-Resolution Imaging Spectroradiometer (MODIS) on board the Terra satellite. There are two different algorithms used to derive total precipitable water vapor in this data product: a near-infrared algorithm and an infrared algorithm. The near-infrared algorithm relies on observations of reflected solar radiation in MODIS's near-infrared channels, thus, the near-infrared retrievals are only produced during the daytime over surfaces that reflect near-infrared energy. As a result, the near-infrared algorithm is only applied over clear, cloud free land areas of the globe and above clouds over both the land and ocean. Over clear ocean areas, water-vapor estimates are provided over extended sun glint areas. Data produced by the near-infrared algorithm are generated at a 1-km spatial resolution. \r\n\r\nThe other algorithm is the infrared algorithm which can be used to derive atmospheric precipitable water vapor profiles during both day and night. Data from the infrared algorithm are generated at a 5-km spatial resolution when at least nine field of views (FOVs) are cloud free. The infrared-derived precipitable water vapor is generated as a component of product MOD07, and is simply added to product MOD05 for convenience. There are two MODIS Precipitable Water Vapor products: MOD05_L2, containing data collected from the Terra platform; and MYD05_L2, containing data collected from the Aqua platform. This dataset has a short name of MOD05_L2 and provides data from the Terra platform only. \r\n\r\nThe MODIS Adaptive Processing System (MODAPS) is currently generating an improved version 6.1 (061) for all MODIS Level-1 (L1) and higher-level Level-2 (L2) & Level-3 (L3) Atmosphere Team products. The decision to create a new improved Collection 6.1 (061) was driven by the need to address a number of issues in the current Collection 6 (006) Level-1B (L1B) data, which have a negative impact in varying degrees in downstream products. It should be noted that the near-infrared algorithm refinement for this product is no longer being supported by NASA and as such there has been no update to this algorithm for Collection 6.1.\r\n\r\nFor more information, visit the MODIS Atmosphere website at:\r\nhttps://modis-atmos.gsfc.nasa.gov/products/water-vapor",
-            "release-place": "MODAPS at NASA/GSFC",
             "creator": "MODIS Science Team",
-            "title": "MODIS/Terra Total Precipitable Water Vapor 5-Min L2 Swath 1km and 5km",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The MODIS/Terra Total Precipitable Water Vapor 5-Min L2 Swath 1km and 5km (MOD05_L2) product consists of atmospheric column water-vapor amounts. This product is derived from data collected by the Moderate-Resolution Imaging Spectroradiometer (MODIS) on board the Terra satellite. There are two different algorithms used to derive total precipitable water vapor in this data product: a near-infrared algorithm and an infrared algorithm. The near-infrared algorithm relies on observations of reflected solar radiation in MODIS's near-infrared channels, thus, the near-infrared retrievals are only produced during the daytime over surfaces that reflect near-infrared energy. As a result, the near-infrared algorithm is only applied over clear, cloud free land areas of the globe and above clouds over both the land and ocean. Over clear ocean areas, water-vapor estimates are provided over extended sun glint areas. Data produced by the near-infrared algorithm are generated at a 1-km spatial resolution. \r\n\r\nThe other algorithm is the infrared algorithm which can be used to derive atmospheric precipitable water vapor profiles during both day and night. Data from the infrared algorithm are generated at a 5-km spatial resolution when at least nine field of views (FOVs) are cloud free. The infrared-derived precipitable water vapor is generated as a component of product MOD07, and is simply added to product MOD05 for convenience. There are two MODIS Precipitable Water Vapor products: MOD05_L2, containing data collected from the Terra platform; and MYD05_L2, containing data collected from the Aqua platform. This dataset has a short name of MOD05_L2 and provides data from the Terra platform only. \r\n\r\nThe MODIS Adaptive Processing System (MODAPS) is currently generating an improved version 6.1 (061) for all MODIS Level-1 (L1) and higher-level Level-2 (L2) & Level-3 (L3) Atmosphere Team products. The decision to create a new improved Collection 6.1 (061) was driven by the need to address a number of issues in the current Collection 6 (006) Level-1B (L1B) data, which have a negative impact in varying degrees in downstream products. It should be noted that the near-infrared algorithm refinement for this product is no longer being supported by NASA and as such there has been no update to this algorithm for Collection 6.1.\r\n\r\nFor more information, visit the MODIS Atmosphere website at:\r\nhttps://modis-atmos.gsfc.nasa.gov/products/water-vapor",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMODIS%2FMOD05_L2.061",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMODIS%2FMOD05_L2.061",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://modis-atmos.gsfc.nasa.gov/products/water-vapor",
-                    "description": "Overview of MODIS Water Vapor products.",
                     "@type": "dcat:Distribution",
+                    "description": "Overview of MODIS Water Vapor products.",
+                    "downloadURL": "https://modis-atmos.gsfc.nasa.gov/products/water-vapor",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/MODIS/MOD05_L2.061",
-                    "description": "The product landing page",
                     "@type": "dcat:Distribution",
+                    "description": "The product landing page",
+                    "downloadURL": "https://doi.org/10.5067/MODIS/MOD05_L2.061",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://atmosphere-imager.gsfc.nasa.gov/sites/default/files/ModAtmo/atbd_mod03.pdf",
-                    "description": "Water Vapor product ATBD",
                     "@type": "dcat:Distribution",
+                    "description": "Water Vapor product ATBD",
+                    "downloadURL": "https://atmosphere-imager.gsfc.nasa.gov/sites/default/files/ModAtmo/atbd_mod03.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's algorithm theoretical basis document"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/search/order/2/MOD05_L2--61",
-                    "description": "Search and order products from LAADS website.",
                     "@type": "dcat:Distribution",
+                    "description": "Search and order products from LAADS website.",
+                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/search/order/2/MOD05_L2--61",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through LAADS"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/archive/allData/61/MOD05_L2/",
-                    "description": "Direct access to MOD05_L2 C6.1 data set.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct access to MOD05_L2 C6.1 data set.",
+                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/archive/allData/61/MOD05_L2/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/opendap/RemoteResources/laads/allData/61/MOD05_L2/contents.html",
-                    "description": "Direct access to product's OPeNDAP directory",
                     "@type": "dcat:Distribution",
+                    "description": "Direct access to product's OPeNDAP directory",
+                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/opendap/RemoteResources/laads/allData/61/MOD05_L2/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 }
             ],
+            "identifier": "C1443531026-LAADS",
+            "issued": "2017-11-01",
+            "keyword": [
+                "national geospatial data asset",
+                "ngda",
+                "atmosphere",
+                "atmospheric water vapor",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/MODIS/MOD05_L2.061",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2025-01-17",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Not provided"
+            },
+            "release-place": "MODAPS at NASA/GSFC",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2000-02-24T00:00:00Z/2025-01-20T00:00:00Z",
             "theme": [
                 "Terra",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "MODIS/Terra Total Precipitable Water Vapor 5-Min L2 Swath 1km and 5km"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-5-DDR-ASTERMAG-V10.0",
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
+            "description": "Absolute magnitudes and slopes, mostly IAU-adopted with exceptions noted, for all asteroids numbered as of the 2006 March 14 batch of Minor Planet Circulars.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-5-ddr-astermag-v10.0_rf72-36kp",
+            "issued": "2021-05-21",
+            "keyword": [
+                "asteroid",
+                "support archives"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-5-DDR-ASTERMAG-V10.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-5-ddr-astermag-v10.0_rf72-36kp",
-            "description": "Absolute magnitudes and slopes, mostly IAU-adopted with exceptions noted, for all asteroids numbered as of the 2006 March 14 batch of Minor Planet Circulars.",
-            "title": "ASTEROID ABSOLUTE MAGNITUDES V10.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ASTEROID ABSOLUTE MAGNITUDES V10.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC%2FOSIWAC-5-67P-SHAPE-V1.0",
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
+            "description": "This data set collects shape models and their associated coordinate systems for the Rosetta target 67P/1969 R1 (Churyumov- Gersimenko).  These were produced by the mission teams based on data obtained at the comet.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-osiwac-5-67p-shape-v1.0_rf7m-a6gt",
+            "issued": "2018-06-26",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC%2FOSIWAC-5-67P-SHAPE-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-osiwac-5-67p-shape-v1.0_rf7m-a6gt",
-            "description": "This data set collects shape models and their associated coordinate systems for the Rosetta target 67P/1969 R1 (Churyumov- Gersimenko).  These were produced by the mission teams based on data obtained at the comet.",
-            "title": "ROSETTA OSIRIS SHAPE MODELS OF COMET 67P/C-G",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "ROSETTA OSIRIS SHAPE MODELS OF COMET 67P/C-G"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=SDU-C-NAVCAM-5-WILD2-SHAPE-MODEL-V1.0",
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
+            "description": "Basic tri-axial ellipsoid shape model of comet 81P/Wild 2, as derived from Navcam images obtained around the time of closest approach to the comet.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.sdu-c-navcam-5-wild2-shape-model-v1.0_rf7x-9ypc",
+            "issued": "2021-05-21",
+            "keyword": [
+                "81p/wild 2 (1978 a2)",
+                "stardust"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=SDU-C-NAVCAM-5-WILD2-SHAPE-MODEL-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.sdu-c-navcam-5-wild2-shape-model-v1.0_rf7x-9ypc",
-            "description": "Basic tri-axial ellipsoid shape model of comet 81P/Wild 2, as derived from Navcam images obtained around the time of closest approach to the comet.",
-            "title": "TRI-AXIAL ELLIPSOID MODEL OF COMET WILD 2",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "TRI-AXIAL ELLIPSOID MODEL OF COMET WILD 2"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://techport.nasa.gov/view/14458",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2013-10-01",
-            "temporal": "2013-10-01T00:00:00Z/2014-10-01T00:00:00Z",
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
-                "jet propulsion laboratory"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Michael Hoenk",
                 "hasEmail": "mailto:michael.e.hoenk@jpl.nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Space Technology Mission Directorate"
-            },
-            "identifier": "TECHPORT_14458",
             "description": "&lt;p&gt;The task objective is to develop a gamma ray scintillator technology with subnanosecond temporal resolution and the capability to withstand unprecedented rates and doses of high energy gamma radiation. This is a joint project with Caltech Prof. Dave Hitlin to detect BaF2 fast scintillation (&amp;tau;&amp;nbsp;~&amp;nbsp;0.9ns at &amp;lambda;&amp;nbsp;~&amp;nbsp;220nm) while rejecting slow scintillation (&amp;tau;&amp;nbsp;~&amp;nbsp;650ns at &amp;lambda;&amp;nbsp;~&amp;nbsp;330nm). We will also develop solar blind coatings using ALD technology for DUV bandpass filter.&lt;/p&gt;",
-            "title": "Subnanosecond scintillation detector for high energy cosmic rays Project",
-            "programCode": [
-                "026:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "http://techport.nasa.gov/xml-api/14458",
                     "mediaType": "application/xml"
                 }
-            ]
+            ],
+            "identifier": "TECHPORT_14458",
+            "issued": "2013-10-01",
+            "keyword": [
+                "project",
+                "active",
+                "jet propulsion laboratory"
+            ],
+            "landingPage": "http://techport.nasa.gov/view/14458",
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
+            "temporal": "2013-10-01T00:00:00Z/2014-10-01T00:00:00Z",
+            "title": "Subnanosecond scintillation detector for high energy cosmic rays Project"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/QIANJYJGRWOV",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "SnowEx21 Time Series Snow Pits V001. Version 1. Archived by National Aeronautics and Space Administration, U.S. Government, NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/QIANJYJGRWOV.",
-            "issued": "2020-11-16",
-            "temporal": "1970-01-01T00:00:00Z/2024-06-10T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2021-05-27",
-            "keyword": [
-                "snow/ice",
-                "sea ice",
-                "terrestrial hydrosphere",
-                "cryosphere",
-                "earth science",
-                "glaciers/ice sheets"
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
-            "identifier": "C3046987606-NSIDC_ECS",
             "description": "The data set is a time-series of snow pit measurements obtained by the SnowEx community during the 2021 field campaign. etween November 2020 and May 2021 data from 247 snow pits were collected at 24 unique sites distributed over 4 states (CO, ID, MT, UT) throughout the Western United States. Five of the unique sites had a single visit to establish baseline conditions, while the remaining 19 sites had 3 or more repeat visits throughout the season, with a median visit count of 11.5. On a weekly interval, a snow pit was dug approximately 1 m away from the previous week\u2019s snow pit. Available measured parameters are: snow depth, snow temperature, snow density, stratigraphy, grain size, manual wetness, liquid water content (LWC), and snow water equivalent (SWE). Also available are photos of the field notes and snow pit sites.",
-            "title": "SnowEx21 Time Series Snow Pits V001",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FQIANJYJGRWOV",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FQIANJYJGRWOV",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/SNOWEX/SNEX21_TS_SP.001/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/SNOWEX/SNEX21_TS_SP.001/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=SNEX21_TS_SP+V001",
-                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=SNEX21_TS_SP+V001",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/data/data-access-tool/SNEX21_TS_SP/versions/1/",
-                    "description": "Search and filter data files using a map-based interface",
                     "@type": "dcat:Distribution",
+                    "description": "Search and filter data files using a map-based interface",
+                    "downloadURL": "https://nsidc.org/data/data-access-tool/SNEX21_TS_SP/versions/1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/SNOWEX/SNEX21_TS_SP.001/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/SNOWEX/SNEX21_TS_SP.001/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=SNEX21_TS_SP+V001",
-                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=SNEX21_TS_SP+V001",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/data/data-access-tool/SNEX21_TS_SP/versions/1/",
-                    "description": "Search and filter data files using a map-based interface",
                     "@type": "dcat:Distribution",
+                    "description": "Search and filter data files using a map-based interface",
+                    "downloadURL": "https://nsidc.org/data/data-access-tool/SNEX21_TS_SP/versions/1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/SNOWEX/SNEX21_TS_SP.001/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/SNOWEX/SNEX21_TS_SP.001/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=SNEX21_TS_SP+V001",
-                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=SNEX21_TS_SP+V001",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/data/data-access-tool/SNEX21_TS_SP/versions/1/",
-                    "description": "Search and filter data files using a map-based interface",
                     "@type": "dcat:Distribution",
+                    "description": "Search and filter data files using a map-based interface",
+                    "downloadURL": "https://nsidc.org/data/data-access-tool/SNEX21_TS_SP/versions/1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/QIANJYJGRWOV",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/QIANJYJGRWOV",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/QIANJYJGRWOV",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/QIANJYJGRWOV",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C3046987606-NSIDC_ECS",
+            "issued": "2020-11-16",
+            "keyword": [
+                "snow/ice",
+                "sea ice",
+                "terrestrial hydrosphere",
+                "cryosphere",
+                "earth science",
+                "glaciers/ice sheets"
+            ],
+            "landingPage": "https://doi.org/10.5067/QIANJYJGRWOV",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2021-05-27",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA NSIDC DAAC"
+            },
             "spatial": "-116.12351 37.9071 -105.86093 47.0607",
+            "temporal": "1970-01-01T00:00:00Z/2024-06-10T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "SnowEx21 Time Series Snow Pits V001"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=LCROSS-L-TLP-2-RAW-V1.0",
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
-                "lunar crater observation and sensing satellite"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "Raw, uncalibrated data from the Total Luminance Photometer (TLP) aboard the Lunar Crater Observation and Sensing Satellite (LCROSS).",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.lcross-l-tlp-2-raw-v1.0_rf8w-ryps",
+            "issued": "2021-05-21",
+            "keyword": [
+                "moon",
+                "lunar crater observation and sensing satellite"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=LCROSS-L-TLP-2-RAW-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.lcross-l-tlp-2-raw-v1.0_rf8w-ryps",
-            "description": "Raw, uncalibrated data from the Total Luminance Photometer (TLP) aboard the Lunar Crater Observation and Sensing Satellite (LCROSS).",
-            "title": "LCROSS MOON TOTAL LUMINANCE PHOTOMETER 2 RAW V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "LCROSS MOON TOTAL LUMINANCE PHOTOMETER 2 RAW V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/906",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Cardille, J.A., J.A. Foley, and M.H. Costa. 2008. LBA-ECO LC-04 Satellite/Census-Based 5-Minute Land Use Data, Amazonia: 1980 and 1995. ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/906",
-            "issued": "2023-10-03",
-            "temporal": "1995-01-01T00:00:00Z/1995-01-01T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-10-04",
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
-            "identifier": "C2777285487-ORNL_CLOUD",
             "description": "This data set contains 5-minute land use maps for agricultural activity in Amazonia. The data set was produced by the statistical fusion of agricultural census data from Brazil,Columbia, Bolivia, and Peru with the land cover data product from the Global Land Cover Facility. These land use maps indicate the estimated total amount of cropland and pasture (natural and planted) for the Amazon and Tocantins River basins in 1995 and 1980 and are suitable for use in models or other similar purposes. Data are provided in the netCDF format and the ARC/INFO GRID ASCII format.The 1995 data were generated from a fusion of agricultural census data and a satellite classification, and are described in Cardille, Foley, and Costa (2002).  The fusion technique merges agricultural census data from Brazil, Columbia, Peru, and Bolivia with land cover data from the University of Maryland Global Land Cover Facility 1-km classification. This technique was used to derive an estimate of the mid-1990s total agriculture surface for the region, which was then apportioned according to agriculture census data into cultivated area, natural pasture, and planted pasture.The 1980 maps, including only the Brazilian portion of the Amazon/Tocantins river drainage basins, were created by scaling the mid-1990s snapshots backward in time using the relative increase or decrease in agriculture, as derived from mid-1980s census data and United Nations Food and Agriculture Organization (FAO) data (Cardille and Foley, 2003).",
-            "graphic-preview-description": "Browse Image",
-            "title": "LBA-ECO LC-04 Satellite/Census-Based 5-Minute Land Use Data, Amazonia: 1980 and 1995",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/sdat-tds/906_1_fit.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F906",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F906",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/lba/land_use_land_cover_change/LC04_Land_Use_5min/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/lba/land_use_land_cover_change/LC04_Land_Use_5min/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/LBA/guides/LC04_Land_Use_5min.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/LBA/guides/LC04_Land_Use_5min.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/906",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/906",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC04_Land_Use_5min/comp/Cardille_poster.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC04_Land_Use_5min/comp/Cardille_poster.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC04_Land_Use_5min/comp/LC04_Land_Use_5min.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC04_Land_Use_5min/comp/LC04_Land_Use_5min.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://daac.ornl.gov/graphics/browse/sdat-tds/906_1_fit.png",
-                    "description": "Browse Image",
                     "@type": "dcat:Distribution",
+                    "description": "Browse Image",
+                    "downloadURL": "https://daac.ornl.gov/graphics/browse/sdat-tds/906_1_fit.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://webmap.ornl.gov/wcsdown/dataset.jsp?ds_id=906",
-                    "description": "Web Coverage Service for this collection.",
                     "@type": "dcat:Distribution",
+                    "description": "Web Coverage Service for this collection.",
+                    "downloadURL": "https://webmap.ornl.gov/wcsdown/dataset.jsp?ds_id=906",
+                    "mediaType": "text/html",
                     "title": "Use Web Coverage Service (WCS) to download the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://thredds.daac.ornl.gov/thredds/catalog/ornldaac/906/catalog.html",
-                    "description": "The THREDDS location for this Collection.",
                     "@type": "dcat:Distribution",
+                    "description": "The THREDDS location for this Collection.",
+                    "downloadURL": "https://thredds.daac.ornl.gov/thredds/catalog/ornldaac/906/catalog.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "graphic-preview-description": "Browse Image",
+            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/sdat-tds/906_1_fit.png",
+            "identifier": "C2777285487-ORNL_CLOUD",
+            "issued": "2023-10-03",
+            "keyword": [
+                "land surface",
+                "earth science",
+                "land use/land cover"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/906",
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
             "spatial": "-80.0 -21.0 -45.0 6.0",
+            "temporal": "1995-01-01T00:00:00Z/1995-01-01T23:59:59Z",
             "theme": [
                 "LBA-ECO",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "LBA-ECO LC-04 Satellite/Census-Based 5-Minute Land Use Data, Amazonia: 1980 and 1995"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ASDCDAAC/NARSTO/0060",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2003-04-01. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/ASDCDAAC/NARSTO/0060.",
-            "issued": "2004-01-14",
-            "temporal": "1999-07-30T00:00:00Z/1999-09-03T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2018-04-18",
-            "keyword": [
-                "earth science",
-                "atmospheric water vapor",
-                "atmospheric temperature",
-                "atmospheric chemistry",
-                "atmosphere",
-                "atmospheric pressure",
-                "aerosols",
-                "atmospheric radiation",
-                "atmospheric winds"
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
-            "identifier": "C1000000080-LARC_ASDC",
             "description": "The NARSTO_EPA_SS_ATLANTA_1999_CHEM_PM_MET_DATA is the North American Research Strategy for Tropospheric Ozone (NARSTO) Environmental Protection Agency (EPA) Supersite (SS) Atlanta 1999 Air Chemistry, Particulate Matter (PM), and Meteorological Data product. This data product was obtained from July to September 1999 during the Atlanta Experiment of the U.S. EPA Particulate Matter Supersites Program. \r\n\r\nThe EPS selected Atlanta as one of the first Supersites Programs dedicated to the study of fine particles (or Particulate Matter (PM) 2.5). The Southern Oxidants Study (SOS) in conjunction with the Georgia Institute of Technology, Earth and Atmospheric Sciences Department developed and implemented the scientific research plan for this initial Supersites Program effort. The Atlanta field experiment was a 4-week long campaign aimed at comprehensively addressing issues related to the measurement and characterization of fine particles in the polluted or urban atmosphere. The experiment took place during the August 1999 and deployed a wide array of instrumentation at a measurement site located on Jefferson Street in Midtown Atlanta.\r\n\r\nGoals of the Atlanta Supersite Program were twofold: first, to provide a platform for testing and contrasting some of the newer particle measurement techniques; and second, to provide data to advance our scientific understanding of atmospheric processes regarding atmospheric particles. Specific objectives were: (1) to characterize the performance of emerging and/or state-of-the-science PM Measurements; (2) to compare and contrast similar and dissimilar PM Measurements; (3) to evaluate the precision, accuracy, and completeness of information that can be gained from the planned EPA PM mass and chemical composition networks; (4) to evaluate the scientific information gained by combining various independent and complementary PM Measurements; and (5) to address various scientific issues and their ozone- and PM-related policy implications with this data base.\r\n\r\nThe EPA PM Supersites Program was an ambient air monitoring research program from 1999-2004 designed to provide information of value to the atmospheric sciences, and human health and exposure research communities. Eight geographically diverse projects were chosen to specifically address the following EPA research priorities: (1) to characterize PM, its constituents, precursors, co-pollutants, atmospheric transport, and its source categories that affect the PM in any region; (2) to address the research questions and scientific uncertainties about PM source-receptor and exposure-health effects relationships; and (3) to compare and evaluate different methods of characterizing PM including testing new and emerging measurement methods.\r\n\r\nNARSTO, which has since disbanded, was a public/private partnership, whose membership spanned across government, utilities, industry, and academe throughout Mexico, the United States, and Canada. The primary mission was to coordinate and enhance policy-relevant scientific research and assessment of tropospheric pollution behavior; activities provide input for science-based decision-making and determination of workable, efficient, and effective strategies for local and regional air-pollution management. Data products from local, regional, and international monitoring and research programs are still available.",
-            "title": "NARSTO EPA Supersite (SS) Atlanta 1999 Air Chemistry, Particulate Matter (PM), and Meteorological Data",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDCDAAC%2FNARSTO%2F0060",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDCDAAC%2FNARSTO%2F0060",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/project/NARSTO",
-                    "description": "ASDC Data and Information for NARSTO",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Data and Information for NARSTO",
+                    "downloadURL": "https://asdc.larc.nasa.gov/project/NARSTO",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://cdiac.ess-dive.lbl.gov/programs/NARSTO/",
-                    "description": "NARSTO Quality Systems Program Science Systems Legacy Page",
                     "@type": "dcat:Distribution",
+                    "description": "NARSTO Quality Systems Program Science Systems Legacy Page",
+                    "downloadURL": "https://cdiac.ess-dive.lbl.gov/programs/NARSTO/",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1000000080-LARC_ASDC",
-                    "description": "Earthdata Search for NARSTO_EPA_SS_ATLANTA_1999_CHEM_PM_MET_DATA_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for NARSTO_EPA_SS_ATLANTA_1999_CHEM_PM_MET_DATA_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1000000080-LARC_ASDC",
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
-                    "mediaType": "application/vnd.google-earth.kmz",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/narsto/EPA_Supersites.kmz",
-                    "description": "EPA Supersites - Direct File Download (.kmz)",
                     "@type": "dcat:Distribution",
+                    "description": "EPA Supersites - Direct File Download (.kmz)",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/narsto/EPA_Supersites.kmz",
+                    "mediaType": "application/vnd.google-earth.kmz",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/narsto/guide/narsto_epa_ss_atlanta_1999_chem_pm_met_data.pdf",
-                    "description": "Guide for NARSTO EPA_SS_ATLANTA 1999 Air Chemistry, Particulate Matter, and Met Data",
                     "@type": "dcat:Distribution",
+                    "description": "Guide for NARSTO EPA_SS_ATLANTA 1999 Air Chemistry, Particulate Matter, and Met Data",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/narsto/guide/narsto_epa_ss_atlanta_1999_chem_pm_met_data.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's product usage"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/narsto/readme/readme_narsto_epa_ss_atlanta_1999_chem_pm_met_data_archive.pdf",
-                    "description": "1999 Atlanta Supersite Data in the NARSTO Archive Overview",
                     "@type": "dcat:Distribution",
+                    "description": "1999 Atlanta Supersite Data in the NARSTO Archive Overview",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/narsto/readme/readme_narsto_epa_ss_atlanta_1999_chem_pm_met_data_archive.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/narsto/readme/readme_narsto_epa_ss_atlanta_1999_chem_pm_met_data_qa_plan.pdf",
-                    "description": "Quality Assurance Project Plan for the Southern Oxidant Study Atlanta Supersite Field Experiment",
                     "@type": "dcat:Distribution",
+                    "description": "Quality Assurance Project Plan for the Southern Oxidant Study Atlanta Supersite Field Experiment",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/narsto/readme/readme_narsto_epa_ss_atlanta_1999_chem_pm_met_data_qa_plan.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View the primary investigator's documentation for this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/narsto/readme/readme_narsto_epa_ss_atlanta_1999_chem_pm_met_data_qa_report.pdf",
-                    "description": "Quality Assurance Final Report for the Southern Oxidant Study Atlanta Supersite August 3 - September 1, 1999",
                     "@type": "dcat:Distribution",
+                    "description": "Quality Assurance Final Report for the Southern Oxidant Study Atlanta Supersite August 3 - September 1, 1999",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/narsto/readme/readme_narsto_epa_ss_atlanta_1999_chem_pm_met_data_qa_report.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's data quality document"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/ASDCDAAC/NARSTO/0060",
-                    "description": "DOI data set landing page for NARSTO_EPA_SS_ATLANTA_1999_CHEM_PM_MET_DATA_1",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for NARSTO_EPA_SS_ATLANTA_1999_CHEM_PM_MET_DATA_1",
+                    "downloadURL": "https://doi.org/10.5067/ASDCDAAC/NARSTO/0060",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/narsto/readme/Intro_1_2.pdf",
-                    "description": "Final Report for the Texas PM2.5 Sampling and Analysis Study (March 11, 1997 - March 12, 1998) (Introduction through Section 2)",
                     "@type": "dcat:Distribution",
+                    "description": "Final Report for the Texas PM2.5 Sampling and Analysis Study (March 11, 1997 - March 12, 1998) (Introduction through Section 2)",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/narsto/readme/Intro_1_2.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's science data product validation documentation"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/narsto/readme/Section_3.pdf",
-                    "description": "Final Report for the Texas PM2.5 Sampling and Analysis Study (March 11, 1997 - March 12, 1998) (Section 3)",
                     "@type": "dcat:Distribution",
+                    "description": "Final Report for the Texas PM2.5 Sampling and Analysis Study (March 11, 1997 - March 12, 1998) (Section 3)",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/narsto/readme/Section_3.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's science data product validation documentation"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/narsto/readme/Section_4.pdf",
-                    "description": "Final Report for the Texas PM2.5 Sampling and Analysis Study (March 11, 1997 - March 12, 1998) (Section 4)",
                     "@type": "dcat:Distribution",
+                    "description": "Final Report for the Texas PM2.5 Sampling and Analysis Study (March 11, 1997 - March 12, 1998) (Section 4)",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/narsto/readme/Section_4.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's science data product validation documentation"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/narsto/readme/Sect_5_6.pdf",
-                    "description": "Final Report for the Texas PM2.5 Sampling and Analysis Study (March 11, 1997 - March 12, 1998) (Sections 5-6)",
                     "@type": "dcat:Distribution",
+                    "description": "Final Report for the Texas PM2.5 Sampling and Analysis Study (March 11, 1997 - March 12, 1998) (Sections 5-6)",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/narsto/readme/Sect_5_6.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's science data product validation documentation"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/NARSTO/EPA_SS_ATLANTA_1999_CHEM_PM_MET_DATA_1/",
-                    "description": "ASDC Direct Data Download for NARSTO_EPA_SS_ATLANTA_1999_CHEM_PM_MET_DATA_1",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for NARSTO_EPA_SS_ATLANTA_1999_CHEM_PM_MET_DATA_1",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/NARSTO/EPA_SS_ATLANTA_1999_CHEM_PM_MET_DATA_1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 }
             ],
+            "identifier": "C1000000080-LARC_ASDC",
+            "issued": "2004-01-14",
+            "keyword": [
+                "earth science",
+                "atmospheric water vapor",
+                "atmospheric temperature",
+                "atmospheric chemistry",
+                "atmosphere",
+                "atmospheric pressure",
+                "aerosols",
+                "atmospheric radiation",
+                "atmospheric winds"
+            ],
+            "landingPage": "https://doi.org/10.5067/ASDCDAAC/NARSTO/0060",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2018-04-18",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/LARC/SD/ASDC"
+            },
             "spatial": "33.78 -84.41",
+            "temporal": "1999-07-30T00:00:00Z/1999-09-03T23:59:59.999Z",
             "theme": [
                 "NARSTO",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "NARSTO EPA Supersite (SS) Atlanta 1999 Air Chemistry, Particulate Matter (PM), and Meteorological Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=GP-J-EPI-3-ENTRY-V1.0",
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
-                "galileo"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "The Galileo Probe Energetic Particles Investigation (EPI) Raw Data Set contains two tables of the EPI raw data values sorted by sampling time. The counter table contains the raw counter values as measured and the countrate table contains the countrates as derived from counter values, but without any correction. The tables are split into omnidirectional and sectorized data. The distance to Jupiter is given in Jupiter radii, Rj, and was derived from the Probe trajectory data. The time of probe entry is taken to be 1995-12-07T22:04:44Z when the probe reached an altitude of 450 km above the 1 bar pressure level.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.gp-j-epi-3-entry-v1.0_rfcf-4iyr",
+            "issued": "2018-06-26",
+            "keyword": [
+                "jupiter",
+                "galileo"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=GP-J-EPI-3-ENTRY-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.gp-j-epi-3-entry-v1.0_rfcf-4iyr",
-            "description": "The Galileo Probe Energetic Particles Investigation (EPI) Raw Data Set contains two tables of the EPI raw data values sorted by sampling time. The counter table contains the raw counter values as measured and the countrate table contains the countrates as derived from counter values, but without any correction. The tables are split into omnidirectional and sectorized data. The distance to Jupiter is given in Jupiter radii, Rj, and was derived from the Probe trajectory data. The time of probe entry is taken to be 1995-12-07T22:04:44Z when the probe reached an altitude of 450 km above the 1 bar pressure level.",
-            "title": "GALILEO PROBE EPI RAW DATA SET",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "GALILEO PROBE EPI RAW DATA SET"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-4-EXT3-67P-M35-REFLECT-V1.0",
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
+            "description": "This CODMAC level 4 data set contains radiometric calibrated and geometric distortion corrected (resampled) image data in reflectance units (normalized and thus without unit), acquired by the OSIRIS Narrow Angle Camera on the Rosetta spacecraft during the ROSETTA EXTENSION 3 mission phase, covering the period from 2016-09-26T06:40:00.000 to 2016-10-01T00:00:00.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V1.0 is the first version of this dataset: Lien corrected dataset after October 2018 PSA/PDS external peer review.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-4-ext3-67p-m35-reflect-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-4-EXT3-67P-M35-REFLECT-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-4-ext3-67p-m35-reflect-v1.0",
-            "description": "This CODMAC level 4 data set contains radiometric calibrated and geometric distortion corrected (resampled) image data in reflectance units (normalized and thus without unit), acquired by the OSIRIS Narrow Angle Camera on the Rosetta spacecraft during the ROSETTA EXTENSION 3 mission phase, covering the period from 2016-09-26T06:40:00.000 to 2016-10-01T00:00:00.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V1.0 is the first version of this dataset: Lien corrected dataset after October 2018 PSA/PDS external peer review.",
-            "title": "ROSETTA-ORBITER 67P OSINAC 4 EXT3-MTP035 RDR-REFLECT V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P OSINAC 4 EXT3-MTP035 RDR-REFLECT V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1684",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Williamson, C.J., A. Kupc, K.R. Bilsback, T.P. Bui, P.C. Jost, M. Dollner, K.D. Froyd, A.L. Hodshire, J.L. Jimenez, J.K. Kodros, G. Luo, D.M. Murphy, B.A. Nault, E. Ray, B. Weinzierl, F. Yu, P. Yu, J.R. Pierce, and C.A. Brock. 2019. ATom: In Situ Tropical Aerosol Properties and Comparable Global Model Outputs. ORNL DAAC, Oak Ridge, Tennessee, USA. https://doi.org/10.3334/ORNLDAAC/1684",
-            "issued": "2019-10-15",
-            "temporal": "2016-07-29T00:00:00Z/2017-02-21T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-06-12",
-            "keyword": [
-                "atmosphere",
-                "atmospheric chemistry",
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
-            "identifier": "C2704953786-ORNL_CLOUD",
             "description": "This dataset provides (1) the results of in situ aerosol particle property measurements collected over remote tropical areas of both Pacific and Atlantic Oceans during the NASA airborne Atmospheric Tomography (ATom) campaigns for ATom-1 and ATom-2 and (2) modeled outputs of comparable aerosol properties, atmospheric chemistry and meteorology at 70 m resolution from four chemical-transport models matched to the location and time of the aircraft measurements.",
-            "graphic-preview-description": "The NASA DC-8 aircraft used for the ATom missions.",
-            "title": "ATom: In Situ Tropical Aerosol Properties and Comparable Global Model Outputs",
-            "graphic-preview-file": "https://daac.ornl.gov/ATOM/guides/ATom_Aerosols_Meteorology_Fig1.jpg",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1684",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1684",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/atom/ATom_Aerosols_Meteorology/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/atom/ATom_Aerosols_Meteorology/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/ATOM/guides/ATom_Aerosols_Meteorology.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/ATOM/guides/ATom_Aerosols_Meteorology.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1684",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1684",
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
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/atom/ATom_Aerosols_Meteorology/comp/ATom_Aerosols_Meteorology.pdf",
-                    "description": "ATom: Tropical New Particle Formation Measurements and Global-Model Outputs: ATom_Aerosols_Meteorology.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "ATom: Tropical New Particle Formation Measurements and Global-Model Outputs: ATom_Aerosols_Meteorology.pdf",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/atom/ATom_Aerosols_Meteorology/comp/ATom_Aerosols_Meteorology.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://daac.ornl.gov/ATOM/guides/ATom_Aerosols_Meteorology_Fig1.jpg",
-                    "description": "The NASA DC-8 aircraft used for the ATom missions.",
                     "@type": "dcat:Distribution",
+                    "description": "The NASA DC-8 aircraft used for the ATom missions.",
+                    "downloadURL": "https://daac.ornl.gov/ATOM/guides/ATom_Aerosols_Meteorology_Fig1.jpg",
+                    "mediaType": "image/jpeg",
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
+            "graphic-preview-description": "The NASA DC-8 aircraft used for the ATom missions.",
+            "graphic-preview-file": "https://daac.ornl.gov/ATOM/guides/ATom_Aerosols_Meteorology_Fig1.jpg",
+            "identifier": "C2704953786-ORNL_CLOUD",
+            "issued": "2019-10-15",
+            "keyword": [
+                "atmosphere",
+                "atmospheric chemistry",
+                "aerosols",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1684",
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
+            "title": "ATom: In Situ Tropical Aerosol Properties and Comparable Global Model Outputs"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RL-CAL-SD2-3-PDCS-V1.0",
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
+            "description": "This archive contains calibrated data and telemetry data from the SD2 instrument onboard ROSETTA Lander, acquired during the PDCS mission phase (Pre Delivery Calib Science). It also contains documentation which describes the SD2 experiment. The data archived in this data set conform to the Planetary Data System (PDS) Standards, Version 3.6.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.rl-cal-sd2-3-pdcs-v1.0_rfjv-uts9",
+            "issued": "2021-05-21",
+            "keyword": [
+                "calibration",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RL-CAL-SD2-3-PDCS-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.rl-cal-sd2-3-pdcs-v1.0_rfjv-uts9",
-            "description": "This archive contains calibrated data and telemetry data from the SD2 instrument onboard ROSETTA Lander, acquired during the PDCS mission phase (Pre Delivery Calib Science). It also contains documentation which describes the SD2 experiment. The data archived in this data set conform to the Planetary Data System (PDS) Standards, Version 3.6.",
-            "title": "ROSETTA-LANDER CAL SD2 3 PDCS V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-LANDER CAL SD2 3 PDCS V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC3-1098-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 3 phase 2015-07-01 to 2015-10-21. It is a Global Gravity measurement at the comet 67P and covers the time 2015-10-13T10:17:25.000 to 2015-10-13T17:27:25.500.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc3-1098-v1.0_rfjx-kwup",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC3-1098-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc3-1098-v1.0_rfjx-kwup",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 3 phase 2015-07-01 to 2015-10-21. It is a Global Gravity measurement at the comet 67P and covers the time 2015-10-13T10:17:25.000 to 2015-10-13T17:27:25.500.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 3 1098 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 3 1098 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/SeaBASS/ANT/DATA001",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/GSFC/SED/ESD/GCDC/OB.DAAC. https://doi.org/10.5067/SeaBASS/ANT/DATA001.",
-            "issued": "2000-11-06",
-            "temporal": "2000-11-01T00:00:02Z/2023-04-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-04-06",
-            "keyword": [
-                "salinity/density",
-                "oceans",
-                "ocean temperature",
-                "earth science",
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
-            "identifier": "C1633360103-OB_DAAC",
             "description": "Measurements made along the African Coast by a North Atlantic Transect (ANT) program under the US-funded GEOTRACES program.",
-            "title": "North Atlantic Transect (ANT) program",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSeaBASS%2FANT%2FDATA001",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSeaBASS%2FANT%2FDATA001",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://seabass.gsfc.nasa.gov/experiment/ANT/",
-                    "description": "Detailed information about the SeaBASS Experiment such as cruises, funding, and investigators",
                     "@type": "dcat:Distribution",
+                    "description": "Detailed information about the SeaBASS Experiment such as cruises, funding, and investigators",
+                    "downloadURL": "https://seabass.gsfc.nasa.gov/experiment/ANT/",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 }
             ],
+            "identifier": "C1633360103-OB_DAAC",
+            "issued": "2000-11-06",
+            "keyword": [
+                "salinity/density",
+                "oceans",
+                "ocean temperature",
+                "earth science",
+                "ocean chemistry",
+                "ocean optics"
+            ],
+            "landingPage": "https://doi.org/10.5067/SeaBASS/ANT/DATA001",
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
+            "temporal": "2000-11-01T00:00:02Z/2023-04-17T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "North Atlantic Transect (ANT) program"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-X-RSI-1%2F2%2F3-CR2-0044-V1.0",
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
-                "sun"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This is a Solar Conjunction measurement covering the time 2006-04-27T00:03:06.500 to 2006-04-27T03:14:07.500.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-x-rsi-1-2-3-cr2-0044-v1.0_rfpi-u5h5",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "sun"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-X-RSI-1%2F2%2F3-CR2-0044-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-x-rsi-1-2-3-cr2-0044-v1.0_rfpi-u5h5",
-            "description": "This is a Solar Conjunction measurement covering the time 2006-04-27T00:03:06.500 to 2006-04-27T03:14:07.500.",
-            "title": "ROSETTA-ORBITER SUN RSI 1/2/3 CRUISE 2 0044 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER SUN RSI 1/2/3 CRUISE 2 0044 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/978",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Miller, S.D., M.L. Goulden, and H.R. da Rocha. 2010. LBA-ECO CD-04 CO2 and Heat Flux, km 83 Gap Tower Site, Tapajos National Forest. ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/978",
-            "issued": "2010-07-22",
-            "temporal": "2002-06-03T00:00:00Z/2004-01-30T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-09-18",
-            "keyword": [
-                "atmospheric chemistry",
-                "earth science",
-                "atmospheric winds",
-                "atmosphere",
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
-            "identifier": "C2768934102-ORNL_CLOUD",
             "description": "This data set reports 30-minute values for above-canopy meteorology and fluxes of momentum, heat, and carbon dioxide, and within-canopy carbon dioxide and water vapor concentrations collected at 12 levels between 10 cm and 64 m at the tower located within a logging gap at km 83 Tower Site in the Tapajos National Forest, Para, Brazil. Data were collected over 1.5 years between June 3, 2002 and January 30, 2004. All of the data are contained in one comma separated file.Two towers are located at the km 83 site. The first tower was installed in an intact forest area at this site in June 2000 (the 'intact' tower). In September 2001, the area adjacent to the tower was selectively logged (Bruno et al., 2006). The second tower (the 'gap tower') was installed and operating in June 2002, 400 m east of the intact tower. The gap tower was installed in the middle of a 50 m x 50 m log landing.",
-            "graphic-preview-description": "Browse Image",
-            "title": "LBA-ECO CD-04 CO2 and Heat Flux, km 83 Gap Tower Site, Tapajos National Forest",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/lba_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F978",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F978",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/lba/carbon_dynamics/CD04_Tower_Flux_Gap/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/lba/carbon_dynamics/CD04_Tower_Flux_Gap/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/LBA/guides/CD04_Tower_Flux_Gap.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/LBA/guides/CD04_Tower_Flux_Gap.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/978",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/978",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/carbon_dynamics/CD04_Tower_Flux_Gap/comp/CD04_Tower_Flux_Gap.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/carbon_dynamics/CD04_Tower_Flux_Gap/comp/CD04_Tower_Flux_Gap.pdf",
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
+            "identifier": "C2768934102-ORNL_CLOUD",
+            "issued": "2010-07-22",
+            "keyword": [
+                "atmospheric chemistry",
+                "earth science",
+                "atmospheric winds",
+                "atmosphere",
+                "atmospheric water vapor",
+                "atmospheric temperature"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/978",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2023-09-18",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "ORNL_DAAC"
+            },
             "spatial": "-3.02 -54.97",
+            "temporal": "2002-06-03T00:00:00Z/2004-01-30T23:59:59Z",
             "theme": [
                 "LBA-ECO",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "LBA-ECO CD-04 CO2 and Heat Flux, km 83 Gap Tower Site, Tapajos National Forest"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-4-ESC1-67P-M12-STRLIGHT-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This CODMAC level 4 data set contains solar stray light corrected, radiometric calibrated and geometric distortion corrected (resampled) image data in W/m^2/sr/nm, acquired by the OSIRIS Narrow Angle Camera on the Rosetta spacecraft during the COMET ESCORT 1 mission phase, covering the period from 2015-01-13T23:25:00.000 to 2015-02-10T23:24:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V1.0 is the first version of this dataset: Lien corrected dataset after October 2018 PSA/PDS external peer review.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-4-esc1-67p-m12-strlight-v1.0",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2021-05-21",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "vega",
                 "international rosetta mission",
                 "67p/churyumov-gerasimenko 1 (1969 r1)"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-4-ESC1-67P-M12-STRLIGHT-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-4-esc1-67p-m12-strlight-v1.0",
-            "description": "This CODMAC level 4 data set contains solar stray light corrected, radiometric calibrated and geometric distortion corrected (resampled) image data in W/m^2/sr/nm, acquired by the OSIRIS Narrow Angle Camera on the Rosetta spacecraft during the COMET ESCORT 1 mission phase, covering the period from 2015-01-13T23:25:00.000 to 2015-02-10T23:24:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V1.0 is the first version of this dataset: Lien corrected dataset after October 2018 PSA/PDS external peer review.",
-            "title": "ROSETTA-ORBITER 67P OSINAC 4 ESC1-MTP012 RDR-STRLIGHT V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P OSINAC 4 ESC1-MTP012 RDR-STRLIGHT V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/CAMEX-4/MULTIPLE/DATA102",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Bui, T.P..2002. CAMEX-4 DC-8 METEOROLOGICAL MEASUREMENT SYSTEM (MMS) [indicate subset used]. Dataset available online from the NASA Global Hydrometeorology Resource Center DAAC, Huntsville, Alabama, U.S.A. DOI: http://dx.doi.org/10.5067/CAMEX-4/MULTIPLE/DATA102",
-            "issued": "2002-04-26",
-            "temporal": "2001-08-18T17:40:11Z/2001-09-25T03:08:04Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-05-23",
-            "keyword": [
-                "platform characteristics",
-                "earth science",
-                "atmosphere",
-                "atmospheric pressure",
-                "atmospheric temperature",
-                "spectral/engineering",
-                "sensor characteristics"
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
-            "identifier": "C1979096645-GHRC_DAAC",
             "description": "The CAMEX-4 DC-8 Meteorological Measurement System (MMS) was collected by the MMS, which consists of three major systems: an air-motion sensing system to measure air velocity with respect to the aircraft, an aircraft-motion sensing system to measure the aircraft velocity with respect to the Earth, and a data acquisition system to sample, process, and record the measured quantities. The MMS data was collected during the CAMEX-4 campaign to study physical properties of atmospheric temperature.",
-            "title": "CAMEX-4 DC-8 METEOROLOGICAL MEASUREMENT SYSTEM (MMS) V1",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FCAMEX-4%2FMULTIPLE%2FDATA102",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FCAMEX-4%2FMULTIPLE%2FDATA102",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=c4dmms",
-                    "description": "Files may be downloaded directly to your workstation from this link",
                     "@type": "dcat:Distribution",
+                    "description": "Files may be downloaded directly to your workstation from this link",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=c4dmms",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://ghrc.nsstc.nasa.gov/uso/ds_docs/camex4/c4dmms/c4dmms_dataset.html",
-                    "description": "The guide document contains detailed information about the dataset",
                     "@type": "dcat:Distribution",
+                    "description": "The guide document contains detailed information about the dataset",
+                    "downloadURL": "http://ghrc.nsstc.nasa.gov/uso/ds_docs/camex4/c4dmms/c4dmms_dataset.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/doc/camex4/c4dmms/mms.pdf",
-                    "description": "ER-2 Meteorological Measurement System (MMS)",
                     "@type": "dcat:Distribution",
+                    "description": "ER-2 Meteorological Measurement System (MMS)",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/doc/camex4/c4dmms/mms.pdf",
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
+            "identifier": "C1979096645-GHRC_DAAC",
+            "issued": "2002-04-26",
+            "keyword": [
+                "platform characteristics",
+                "earth science",
+                "atmosphere",
+                "atmospheric pressure",
+                "atmospheric temperature",
+                "spectral/engineering",
+                "sensor characteristics"
+            ],
+            "landingPage": "https://doi.org/10.5067/CAMEX-4/MULTIPLE/DATA102",
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
             "spatial": "-88.215 16.531 -58.635 39.712",
+            "temporal": "2001-08-18T17:40:11Z/2001-09-25T03:08:04Z",
             "theme": [
                 "CAMEX-4",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "CAMEX-4 DC-8 METEOROLOGICAL MEASUREMENT SYSTEM (MMS) V1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/753",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Yokelson, R.J. 2004. SAFARI 2000 Gas Emissions from Biofuel Use and Production, September 2000. ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/753",
-            "issued": "2023-10-18",
-            "temporal": "2000-09-10T00:00:00Z/2000-09-16T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-10-24",
-            "keyword": [
-                "earth science",
-                "atmospheric chemistry",
-                "environmental impacts",
-                "atmosphere",
-                "human dimensions",
-                "economic resources"
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
-            "identifier": "C2789024961-ORNL_CLOUD",
             "description": "Domestic biomass fuels (biofuels) are estimated to be the second largest source of carbon emissions from global biomass burning. Wood and charcoal provide approximately 90% and 10% of domestic energy in tropical Africa, respectively. As part of the Southern Africa Regional Science Initiative (SAFARI 2000), the University of Montana participated in both ground-based and airborne campaigns during the southern African dry season of 2000 to measure trace gas emissions from biofuel production and use and savanna fires, respectively.",
-            "graphic-preview-description": "Browse Image",
-            "title": "SAFARI 2000 Gas Emissions from Biofuel Use and Production, September 2000",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/safari_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F753",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F753",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/safari2k/atmospheric/biofuel_emissions/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/safari2k/atmospheric/biofuel_emissions/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/S2K/guides/biofuel_emissions.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/S2K/guides/biofuel_emissions.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/753",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/753",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/safari2k/atmospheric/biofuel_emissions/comp/biofuel_emissions_readme.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/safari2k/atmospheric/biofuel_emissions/comp/biofuel_emissions_readme.pdf",
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
+            "identifier": "C2789024961-ORNL_CLOUD",
+            "issued": "2023-10-18",
+            "keyword": [
+                "earth science",
+                "atmospheric chemistry",
+                "environmental impacts",
+                "atmosphere",
+                "human dimensions",
+                "economic resources"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/753",
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
             "spatial": "-14.86 24.82",
+            "temporal": "2000-09-10T00:00:00Z/2000-09-16T23:59:59Z",
             "theme": [
                 "SAFARI 2000",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "SAFARI 2000 Gas Emissions from Biofuel Use and Production, September 2000"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-4-PRL-67P-M08-STR-REFL-V1.0",
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
+            "description": "This CODMAC level 4 data set contains solar stray light corrected, radiometric calibrated and geometric distortion corrected (resampled) image data in in reflectance units (normalized and thus without unit), acquired by the OSIRIS Narrow Angle Camera on the Rosetta spacecraft during the PRELANDING mission phase, covering the period from 2014-09-23T10:00:00.000 to 2014-10-24T09:59:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V1.0 is the first version of this dataset: Lien corrected dataset after October 2018 PSA/PDS external peer review.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-4-prl-67p-m08-str-refl-v1.0_rfyt-5wxw",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-4-PRL-67P-M08-STR-REFL-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-4-prl-67p-m08-str-refl-v1.0_rfyt-5wxw",
-            "description": "This CODMAC level 4 data set contains solar stray light corrected, radiometric calibrated and geometric distortion corrected (resampled) image data in in reflectance units (normalized and thus without unit), acquired by the OSIRIS Narrow Angle Camera on the Rosetta spacecraft during the PRELANDING mission phase, covering the period from 2014-09-23T10:00:00.000 to 2014-10-24T09:59:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V1.0 is the first version of this dataset: Lien corrected dataset after October 2018 PSA/PDS external peer review.",
-            "title": "ROSETTA-ORBITER 67P OSINAC 4 PRL-MTP008 RDR-STR-REFL V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P OSINAC 4 PRL-MTP008 RDR-STR-REFL V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/374",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Crill, P.M., and R.K. Varner. 1998. BOREAS TGB-01 CH4 & CO2 Chamber Flux Data: NSA. ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/374",
-            "issued": "2023-11-22",
-            "temporal": "1994-05-16T00:00:00Z/1994-09-13T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-11-28",
-            "keyword": [
-                "earth science",
-                "soils",
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
-            "identifier": "C2808131236-ORNL_CLOUD",
             "description": "Contains TGB-01 carbon chamber flux data for Northern Study Area.",
-            "graphic-preview-description": "Browse Image",
-            "title": "BOREAS TGB-01 CH4 & CO2 Chamber Flux Data: NSA",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/boreas_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F374",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F374",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/boreas/TGB/tgb1ccfd/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/boreas/TGB/tgb1ccfd/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/BOREAS/guides/TGB01_CO2_CH4_Chmbr.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/BOREAS/guides/TGB01_CO2_CH4_Chmbr.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/374",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/374",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/msword",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TGB/tgb1ccfd/comp/TGB01_CO2_CH4_Chmbr.doc",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TGB/tgb1ccfd/comp/TGB01_CO2_CH4_Chmbr.doc",
+                    "mediaType": "application/msword",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TGB/tgb1ccfd/comp/TGB01_CO2_CH4_Chmbr.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TGB/tgb1ccfd/comp/TGB01_CO2_CH4_Chmbr.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TGB/tgb1ccfd/comp/TGB01_CO2_CH4_Chmbr.txt",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TGB/tgb1ccfd/comp/TGB01_CO2_CH4_Chmbr.txt",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TGB/tgb1ccfd/comp/tgb1ccfd.def",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TGB/tgb1ccfd/comp/tgb1ccfd.def",
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
+            "identifier": "C2808131236-ORNL_CLOUD",
+            "issued": "2023-11-22",
+            "keyword": [
+                "earth science",
+                "soils",
+                "land surface"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/374",
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
             "spatial": "-98.62 55.84 -98.03 55.93",
+            "temporal": "1994-05-16T00:00:00Z/1994-09-13T23:59:59Z",
             "theme": [
                 "BOREAS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "BOREAS TGB-01 CH4 & CO2 Chamber Flux Data: NSA"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/VIIRS/VJ101_NRT.002",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "VIIRS Level 1 Processing Group at Ocean SIPS. 2019-04-08. VIIRS/JPSS1 Raw Radiances in Counts 6-Min L1A Swath -NRT. Version 2. MODAPS at NASA/GSFC. Archived by National Aeronautics and Space Administration, U.S. Government, LANCEMODIS. https://doi.org/10.5067/VIIRS/VJ101_NRT.002. http://dx.doi.org/10.5067/VIIRS/VJ101_NRT.002.",
-            "issued": "2019-04-08",
-            "temporal": "2019-04-08T00:00:00Z/2022-01-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2019-04-03",
-            "keyword": [
-                "spectral/engineering",
-                "visible wavelengths",
-                "earth science",
-                "infrared wavelengths"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "LANCEMODIS",
                 "hasEmail": "mailto:support@earthdata.nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Not provided"
-            },
-            "identifier": "C1604377338-LANCEMODIS",
-            "description": "The Near Real Time (NRT) JPSS1/VIIRS Raw Radiances in Counts 6-Min L1A Swath (VJ101_NRT) data product contains the unpacked, raw VIIRS science, calibration and engineering data; the extracted ephemeris and attitude data from the spacecraft diary packets; and the raw ADCS and bus-critical spacecraft telemetry data from those packets, with a few critical fields extracted.\n\nFor more information download VIIRS Level 1 Product User's Guide at:\nhttps://oceancolor.gsfc.nasa.gov/docs/format/VIIRS_Level-1_DataProductUsersGuide.pdf",
-            "release-place": "MODAPS at NASA/GSFC",
             "creator": "VIIRS Level 1 Processing Group at Ocean SIPS",
-            "title": "VIIRS/JPSS1 Raw Radiances in Counts 6-Min L1A Swath -NRT",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The Near Real Time (NRT) JPSS1/VIIRS Raw Radiances in Counts 6-Min L1A Swath (VJ101_NRT) data product contains the unpacked, raw VIIRS science, calibration and engineering data; the extracted ephemeris and attitude data from the spacecraft diary packets; and the raw ADCS and bus-critical spacecraft telemetry data from those packets, with a few critical fields extracted.\n\nFor more information download VIIRS Level 1 Product User's Guide at:\nhttps://oceancolor.gsfc.nasa.gov/docs/format/VIIRS_Level-1_DataProductUsersGuide.pdf",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FVIIRS%2FVJ101_NRT.002",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FVIIRS%2FVJ101_NRT.002",
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
+            "identifier": "C1604377338-LANCEMODIS",
+            "issued": "2019-04-08",
+            "keyword": [
+                "spectral/engineering",
+                "visible wavelengths",
+                "earth science",
+                "infrared wavelengths"
+            ],
+            "landingPage": "https://doi.org/10.5067/VIIRS/VJ101_NRT.002",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2019-04-03",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Not provided"
+            },
+            "release-place": "MODAPS at NASA/GSFC",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2019-04-08T00:00:00Z/2022-01-17T00:00:00Z",
             "theme": [
                 "NPP-JPSS",
                 "LANCE",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "VIIRS/JPSS1 Raw Radiances in Counts 6-Min L1A Swath -NRT"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-PRL-0430-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the PRELANDING phase 2014-01-21 to 2014-11-18. It is a Global Gravity measurement at the comet 67P and covers the time 2014-11-14T03:07:05.000 to 2014-11-14T06:11:49.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-prl-0430-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-PRL-0430-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-prl-0430-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the PRELANDING phase 2014-01-21 to 2014-11-18. It is a Global Gravity measurement at the comet 67P and covers the time 2014-11-14T03:07:05.000 to 2014-11-14T06:11:49.000.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     PRELANDING 0430 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     PRELANDING 0430 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/AQR50-3D7AE",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "NASA Aquarius project. 2017-12-07. Aquarius Official Release Level 3 Sea Surface Density Standard Mapped Image Ascending 7-Day Data. Version 5.0. Aquarius Sea Surface Salinity Products. Goddard Space Flight Center, 8800 Greenbelt Rd.; Greeenbelt, MD., 20771, USA. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/GSFC OBPG. https://doi.org/10.5067/AQR50-3D7AE. http://podaac.jpl.nasa.gov/SeaSurfaceSalinity/Aquarius. NASA Aquarius project, NASA/GSFC OBPG, 2017-12-07, Aquarius Official Release Level 3 Sea Surface Density Standard Mapped Image Ascending 7-Day Data V5.0, http://podaac.jpl.nasa.gov/SeaSurfaceSalinity/Aquarius.",
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
-            "identifier": "C2491755956-POCLOUD",
-            "description": "Aquarius Level 3 sea surface density standard mapped image data contains gridded 1 degree spatial resolution density data averaged over daily, 7 day, monthly, and seasonal time scales. This particular data set is the 7-Day, Ascending sea surface density product\nfor version 5.0 of the Aquarius data set. Only retrieved values for Ascending passes have been used to create this product.  Surface density estimates are based on TEOS-10 and derived using retrieved salinity from Aquarius and collocated ancillary SST (Reynolds OI 0.25 degree product).  The Aquarius instrument is onboard the AQUARIUS/SAC-D satellite, a collaborative effort between NASA and the Argentinian Space Agency Comision Nacional de Actividades Espaciales (CONAE). The instrument consists of three radiometers in push broom alignment at incidence angles of 29, 38, and 46 degrees incidence angles relative to the shadow side of the orbit.  Footprints for the beams are: 76 km (along-track) x 94 km (cross-track), 84 km x 120 km and 96km x 156 km, yielding a total cross-track swath of 370 km. The radiometers measure brightness temperature at 1.413 GHz in their respective horizontal and vertical polarizations (TH and TV). A scatterometer operating at 1.26 GHz measures ocean backscatter in each footprint that is used for surface roughness corrections in the estimation of salinity. The scatterometer has an approximate 390km swath.",
-            "release-place": "Goddard Space Flight Center, 8800 Greenbelt Rd.; Greeenbelt, MD., 20771, USA",
-            "series-name": "Aquarius Official Release Level 3 Sea Surface Density Standard Mapped Image Ascending 7-Day Data",
-            "graphic-preview-description": "Thumbnail",
             "creator": "NASA Aquarius project",
-            "title": "Aquarius Official Release Level 3 Sea Surface Density Standard Mapped Image Ascending 7-Day Data V5.0",
-            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/AQUARIUS_L3_DENSITY_SMIA_7DAY_V5.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "Aquarius Level 3 sea surface density standard mapped image data contains gridded 1 degree spatial resolution density data averaged over daily, 7 day, monthly, and seasonal time scales. This particular data set is the 7-Day, Ascending sea surface density product\nfor version 5.0 of the Aquarius data set. Only retrieved values for Ascending passes have been used to create this product.  Surface density estimates are based on TEOS-10 and derived using retrieved salinity from Aquarius and collocated ancillary SST (Reynolds OI 0.25 degree product).  The Aquarius instrument is onboard the AQUARIUS/SAC-D satellite, a collaborative effort between NASA and the Argentinian Space Agency Comision Nacional de Actividades Espaciales (CONAE). The instrument consists of three radiometers in push broom alignment at incidence angles of 29, 38, and 46 degrees incidence angles relative to the shadow side of the orbit.  Footprints for the beams are: 76 km (along-track) x 94 km (cross-track), 84 km x 120 km and 96km x 156 km, yielding a total cross-track swath of 370 km. The radiometers measure brightness temperature at 1.413 GHz in their respective horizontal and vertical polarizations (TH and TV). A scatterometer operating at 1.26 GHz measures ocean backscatter in each footprint that is used for surface roughness corrections in the estimation of salinity. The scatterometer has an approximate 390km swath.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAQR50-3D7AE",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAQR50-3D7AE",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
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
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/AQUARIUS_L3_DENSITY_SMIA_7DAY_V5.jpg",
-                    "description": "Thumbnail",
                     "@type": "dcat:Distribution",
+                    "description": "Thumbnail",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/AQUARIUS_L3_DENSITY_SMIA_7DAY_V5.jpg",
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
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2491755956-POCLOUD",
-                    "description": "HTTPS endpoint for data browse and download",
                     "@type": "dcat:Distribution",
+                    "description": "HTTPS endpoint for data browse and download",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2491755956-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2491755956-POCLOUD",
-                    "description": "Browse granule search results in Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse granule search results in Earthdata Search",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2491755956-POCLOUD",
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
+            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/AQUARIUS_L3_DENSITY_SMIA_7DAY_V5.jpg",
+            "identifier": "C2491755956-POCLOUD",
+            "issued": "2017-10-21",
+            "keyword": [
+                "oceans",
+                "earth science",
+                "salinity/density"
+            ],
+            "landingPage": "https://doi.org/10.5067/AQR50-3D7AE",
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
+            "series-name": "Aquarius Official Release Level 3 Sea Surface Density Standard Mapped Image Ascending 7-Day Data",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2011-08-25T01:55:23Z/2015-06-07T11:41:38Z",
             "theme": [
                 "AQUARIUS SAC-D",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Aquarius Official Release Level 3 Sea Surface Density Standard Mapped Image Ascending 7-Day Data V5.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.nasa.gov/d/rg5u-t97p",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2021-01-19",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-31",
-            "keyword": [
-                "a",
-                "this",
-                "test",
-                "is"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Taylor Yates",
                 "hasEmail": "mailto:evan.t.yates@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "data.nasa.gov"
-            },
-            "identifier": "https://data.nasa.gov/api/views/rg5u-t97p",
+            "dataQuality": true,
             "description": "A test dataset for Socrata help ticket",
-            "title": "Testing Again Now",
-            "programCode": [
-                "026:004"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -1304223,424 +1304205,417 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.nasa.gov/api/views/rg5u-t97p/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.nasa.gov/api/views/rg5u-t97p/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.nasa.gov/api/views/rg5u-t97p/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.nasa.gov/api/views/rg5u-t97p/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.nasa.gov/api/views/rg5u-t97p/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.nasa.gov/api/views/rg5u-t97p/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.nasa.gov/api/views/rg5u-t97p/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.nasa.gov/api/views/rg5u-t97p/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.nasa.gov/api/views/rg5u-t97p/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "https://data.nasa.gov/api/views/rg5u-t97p",
+            "issued": "2021-01-19",
+            "keyword": [
+                "a",
+                "this",
+                "test",
+                "is"
+            ],
+            "landingPage": "https://data.nasa.gov/d/rg5u-t97p",
+            "modified": "2023-01-31",
+            "programCode": [
+                "026:004"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "data.nasa.gov"
+            },
             "theme": [
                 "Space Science"
-            ]
+            ],
+            "title": "Testing Again Now"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://c3.nasa.gov/dashlink/resources/471/",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2011-09-23",
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
-            "identifier": "DASHLINK_471",
             "description": "These grids were constructed using Centaur software at DLR in Germany. The grids designed for node based (labeled 'cv') and cell-centered solvers (labeled 'cc') are supplied. Grids with mixed elements only are supplied.\r\n\r\nEach mixed elements tar-file contains grid in TAU software native format '.nc','.bmap'.  The grid was converted into '.cgns' format.  In some instances, the grids in TAU native formats were converted into aflr3 format at NASA Langley '.ugrid','.mapbc' which in turn were converted to the 'ugrid.cgns' formats.\r\n\r\n\r\nSome files were too large and had to be split into parts. To combine the parts, use cat filename_part1 filename_part2 > filename.\r\n\r\nGrids are in units of 'mm'.  \r\n\r\nPlease report any issues with these grids to Markus.Ritter@dlr.de and Pawel.Chwalowski@nasa.gov",
-            "title": "HIRENASD Unstructured Grids - Centaur software",
-            "programCode": [
-                "026:029"
-            ],
             "distribution": [
                 {
-                    "mediaType": "application/x-gzip",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/HIRENASD_coarse_cv_Centaur_TAU.tar.gz",
-                    "description": "Coarse Mixed Elements Node Based",
                     "@type": "dcat:Distribution",
+                    "description": "Coarse Mixed Elements Node Based",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/HIRENASD_coarse_cv_Centaur_TAU.tar.gz",
+                    "mediaType": "application/x-gzip",
                     "title": "HIRENASD_coarse_cv_Centaur_TAU.tar.gz"
                 },
                 {
-                    "mediaType": "application/octet-stream",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/HIRENASD_medium_cv_Centaur_TAU.tar.gz_part1",
-                    "description": "Part1: Medium Mixed Elements Node Based",
                     "@type": "dcat:Distribution",
+                    "description": "Part1: Medium Mixed Elements Node Based",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/HIRENASD_medium_cv_Centaur_TAU.tar.gz_part1",
+                    "mediaType": "application/octet-stream",
                     "title": "HIRENASD_medium_cv_Centaur_TAU.tar.gz_part1"
                 },
                 {
-                    "mediaType": "application/octet-stream",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/HIRENASD_medium_cv_Centaur_TAU.tar.gz_part2",
-                    "description": "Part2: Medium Mixed Elements Node Based",
                     "@type": "dcat:Distribution",
+                    "description": "Part2: Medium Mixed Elements Node Based",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/HIRENASD_medium_cv_Centaur_TAU.tar.gz_part2",
+                    "mediaType": "application/octet-stream",
                     "title": "HIRENASD_medium_cv_Centaur_TAU.tar.gz_part2"
                 },
                 {
-                    "mediaType": "application/x-gzip",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/HIRENASD_coarse_cc_Centaur_TAU.tar.gz",
-                    "description": "Coarse Mixed Elements Cell-centered",
                     "@type": "dcat:Distribution",
+                    "description": "Coarse Mixed Elements Cell-centered",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/HIRENASD_coarse_cc_Centaur_TAU.tar.gz",
+                    "mediaType": "application/x-gzip",
                     "title": "HIRENASD_coarse_cc_Centaur_TAU.tar.gz"
                 },
                 {
-                    "mediaType": "application/x-gzip",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/HIRENASD_medium_cc_Centaur_TAU.tar.gz",
-                    "description": "Medium Mixed Elements Cell-Centered",
                     "@type": "dcat:Distribution",
+                    "description": "Medium Mixed Elements Cell-Centered",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/HIRENASD_medium_cc_Centaur_TAU.tar.gz",
+                    "mediaType": "application/x-gzip",
                     "title": "HIRENASD_medium_cc_Centaur_TAU.tar.gz"
                 },
                 {
-                    "mediaType": "application/octet-stream",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/HIRENASD_fine_cv_Centaur_TAU.tar.gz_part1",
-                    "description": "Part1: Fine Mixed Elements Node Based",
                     "@type": "dcat:Distribution",
+                    "description": "Part1: Fine Mixed Elements Node Based",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/HIRENASD_fine_cv_Centaur_TAU.tar.gz_part1",
+                    "mediaType": "application/octet-stream",
                     "title": "HIRENASD_fine_cv_Centaur_TAU.tar.gz_part1"
                 },
                 {
-                    "mediaType": "application/octet-stream",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/HIRENASD_fine_cv_Centaur_TAU.tar.gz_part2",
-                    "description": "Part2: Fine Mixed Elements Node Based",
                     "@type": "dcat:Distribution",
+                    "description": "Part2: Fine Mixed Elements Node Based",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/HIRENASD_fine_cv_Centaur_TAU.tar.gz_part2",
+                    "mediaType": "application/octet-stream",
                     "title": "HIRENASD_fine_cv_Centaur_TAU.tar.gz_part2"
                 },
                 {
-                    "mediaType": "application/octet-stream",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/HIRENASD_fine_cv_Centaur_TAU.tar.gz_part3",
-                    "description": "Part3: Fine Mixed Elements Node Based",
                     "@type": "dcat:Distribution",
+                    "description": "Part3: Fine Mixed Elements Node Based",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/HIRENASD_fine_cv_Centaur_TAU.tar.gz_part3",
+                    "mediaType": "application/octet-stream",
                     "title": "HIRENASD_fine_cv_Centaur_TAU.tar.gz_part3"
                 },
                 {
-                    "mediaType": "application/msword",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/Mesh_statistics_11_2011_final.doc",
-                    "description": "Mesh statistics_11_2011_final.doc",
                     "@type": "dcat:Distribution",
+                    "description": "Mesh statistics_11_2011_final.doc",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/Mesh_statistics_11_2011_final.doc",
+                    "mediaType": "application/msword",
                     "title": "Mesh statistics_11_2011_final.doc"
                 },
                 {
-                    "mediaType": "application/x-gzip",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/HIRENASD_fine_cc_Centaur_TAU.tar.gz",
-                    "description": "Fine Mixed Cell-centered",
                     "@type": "dcat:Distribution",
+                    "description": "Fine Mixed Cell-centered",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/HIRENASD_fine_cc_Centaur_TAU.tar.gz",
+                    "mediaType": "application/x-gzip",
                     "title": "HIRENASD_fine_cc_Centaur_TAU.tar.gz"
                 }
             ],
-            "accrualPeriodicity": "irregular"
+            "identifier": "DASHLINK_471",
+            "issued": "2011-09-23",
+            "keyword": [
+                "ames",
+                "nasa",
+                "dashlink"
+            ],
+            "landingPage": "https://c3.nasa.gov/dashlink/resources/471/",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:029"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Dashlink"
+            },
+            "title": "HIRENASD Unstructured Grids - Centaur software"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/SeaBASS/THAILAND/DATA001",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/GSFC/SED/ESD/GCDC/OB.DAAC. https://doi.org/10.5067/SeaBASS/THAILAND/DATA001.",
-            "issued": "2003-10-09",
-            "temporal": "2003-10-09T00:37:00Z/2023-04-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-04-06",
-            "keyword": [
-                "earth science",
-                "oceans",
-                "ocean optics",
-                "salinity/density",
-                "ocean temperature",
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
-            "identifier": "C1633360682-OB_DAAC",
             "description": "Measurements made in the Gulf of Thailand and the Andaman Sea in 2003.",
-            "title": "Optical measurements in the Gulf of Thailand and the Andaman Sea in 2003",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSeaBASS%2FTHAILAND%2FDATA001",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSeaBASS%2FTHAILAND%2FDATA001",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://seabass.gsfc.nasa.gov/experiment/THAILAND/",
-                    "description": "Detailed information about the SeaBASS Experiment such as cruises, funding, and investigators",
                     "@type": "dcat:Distribution",
+                    "description": "Detailed information about the SeaBASS Experiment such as cruises, funding, and investigators",
+                    "downloadURL": "https://seabass.gsfc.nasa.gov/experiment/THAILAND/",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 }
             ],
+            "identifier": "C1633360682-OB_DAAC",
+            "issued": "2003-10-09",
+            "keyword": [
+                "earth science",
+                "oceans",
+                "ocean optics",
+                "salinity/density",
+                "ocean temperature",
+                "ocean chemistry"
+            ],
+            "landingPage": "https://doi.org/10.5067/SeaBASS/THAILAND/DATA001",
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
+            "temporal": "2003-10-09T00:37:00Z/2023-04-17T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Optical measurements in the Gulf of Thailand and the Andaman Sea in 2003"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/GFOCN-3J634",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Felix Landerer. 2023-02-21. JPL TELLUS GRACE-FO Level-3 Monthly Ocean Bottom Pressure Anomaly. Version RL06.3v04. JPL TELLUS GRACE-FO Level-3 Monthly Ocean Bottom Pressure Anomaly Release 6.3 version 04. JPL. Archived by National Aeronautics and Space Administration, U.S. Government, PO.DAAC. https://doi.org/10.5067/GFOCN-3J634.",
-            "issued": "2021-03-10",
-            "temporal": "2018-05-22T00:00:00Z/2024-09-16T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2021-03-10",
-            "keyword": [
-                "oceans",
-                "earth science",
-                "ocean pressure"
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
-            "identifier": "C3193304376-POCLOUD",
-            "description": "This data set is produced by the Jet Propulsion Laboratory (JPL) as part of the GRACE-FO (Gravity Recovery and Climate Experiment Follow-On) program and derives the ocean bottom pressure (OBP) anomaly given as equivalent water thickness. These monthly grids are derived from GRACE-FO time-variable gravity observations during the specified timespan, and relative to the specified time-mean reference period. This quantity represents sea floor pressure changes due to the integral effect of ocean and atmosphere processes, including global mean ocean bottom pressure changes (mean ocean mass and mean atmosphere mass over the global oceans). A glacial isostatic adjustment (GIA) correction has been applied, and standard corrections for geocenter (degree-1), C20 (degree-20) and C30 (degree-30) are incorporated. Post-processing filters have been applied to reduce correlated errors. Data grids are provided in ASCII/netCDF/GeoTIFF formats. <br><br>\r\n\r\nGRACE-FO was launched on 22 May 2018, and extends the original GRACE mission (2002 \u2013 2017) and expands its legacy of scientific achievements in tracking earth surface mass changes. Version 04 (v04) of the ocean bottom pressure data uses updated and consistent C20 and Geocenter corrections (i.e., Technical Notes TN-14 and TN-13), as well as an ellipsoidal correction to account for the non-spherical shape of the Earth when mapping gravity anomalies to surface mass change. Additionally, this RL06.3 is an updated release of the previous RL06.1. It differs from RL06.1 only in the Level-1B accelerometer transplant data that is used for the GF2 (GRACE-FO 2) satellite; see respective L-2 data descriptions. RL06.3 uses the ACX2-L1B data products. All GRACE-FO RL06.3 Level-3 fields are fully compatible with the GRACE RL06 data.",
-            "release-place": "JPL",
-            "series-name": "JPL TELLUS GRACE-FO Level-3 Monthly Ocean Bottom Pressure Anomaly",
-            "graphic-preview-description": "Thumbnail",
             "creator": "Felix Landerer",
-            "title": "JPL TELLUS GRACE-FO Level-3 Monthly Ocean Bottom Pressure Anomaly Release 6.3 version 04",
-            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/TELLUS_GRFO_L3_JPL_RL06_OCN_v04.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "This data set is produced by the Jet Propulsion Laboratory (JPL) as part of the GRACE-FO (Gravity Recovery and Climate Experiment Follow-On) program and derives the ocean bottom pressure (OBP) anomaly given as equivalent water thickness. These monthly grids are derived from GRACE-FO time-variable gravity observations during the specified timespan, and relative to the specified time-mean reference period. This quantity represents sea floor pressure changes due to the integral effect of ocean and atmosphere processes, including global mean ocean bottom pressure changes (mean ocean mass and mean atmosphere mass over the global oceans). A glacial isostatic adjustment (GIA) correction has been applied, and standard corrections for geocenter (degree-1), C20 (degree-20) and C30 (degree-30) are incorporated. Post-processing filters have been applied to reduce correlated errors. Data grids are provided in ASCII/netCDF/GeoTIFF formats. <br><br>\r\n\r\nGRACE-FO was launched on 22 May 2018, and extends the original GRACE mission (2002 \u2013 2017) and expands its legacy of scientific achievements in tracking earth surface mass changes. Version 04 (v04) of the ocean bottom pressure data uses updated and consistent C20 and Geocenter corrections (i.e., Technical Notes TN-14 and TN-13), as well as an ellipsoidal correction to account for the non-spherical shape of the Earth when mapping gravity anomalies to surface mass change. Additionally, this RL06.3 is an updated release of the previous RL06.1. It differs from RL06.1 only in the Level-1B accelerometer transplant data that is used for the GF2 (GRACE-FO 2) satellite; see respective L-2 data descriptions. RL06.3 uses the ACX2-L1B data products. All GRACE-FO RL06.3 Level-3 fields are fully compatible with the GRACE RL06 data.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGFOCN-3J634",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGFOCN-3J634",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
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
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/gracefo/open/docs/GRACE-FO_L3_Handbook_JPL.pdf",
-                    "description": "User guidance documentation for this dataset",
                     "@type": "dcat:Distribution",
+                    "description": "User guidance documentation for this dataset",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/gracefo/open/docs/GRACE-FO_L3_Handbook_JPL.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/TELLUS_GRFO_L3_JPL_RL06_OCN_v04.jpg",
-                    "description": "Thumbnail",
                     "@type": "dcat:Distribution",
+                    "description": "Thumbnail",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/TELLUS_GRFO_L3_JPL_RL06_OCN_v04.jpg",
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
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C3193304376-POCLOUD",
-                    "description": "HTTPS endpoint for data browse and download",
                     "@type": "dcat:Distribution",
+                    "description": "HTTPS endpoint for data browse and download",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C3193304376-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C3193304376-POCLOUD",
-                    "description": "Browse granule search results in Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse granule search results in Earthdata Search",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C3193304376-POCLOUD",
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
                 }
             ],
+            "graphic-preview-description": "Thumbnail",
+            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/TELLUS_GRFO_L3_JPL_RL06_OCN_v04.jpg",
+            "identifier": "C3193304376-POCLOUD",
+            "issued": "2021-03-10",
+            "keyword": [
+                "oceans",
+                "earth science",
+                "ocean pressure"
+            ],
+            "landingPage": "https://doi.org/10.5067/GFOCN-3J634",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2021-03-10",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/JPL/PODAAC"
+            },
+            "release-place": "JPL",
+            "series-name": "JPL TELLUS GRACE-FO Level-3 Monthly Ocean Bottom Pressure Anomaly",
             "spatial": "-180.0 -89.5 180.0 89.5",
+            "temporal": "2018-05-22T00:00:00Z/2024-09-16T00:00:00Z",
             "theme": [
                 "GRACE-FO",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "JPL TELLUS GRACE-FO Level-3 Monthly Ocean Bottom Pressure Anomaly Release 6.3 version 04"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MER1-M-HAZCAM-5-MESH-OPS-V1.0",
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
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mer1-m-hazcam-5-mesh-ops-v1.0_rg8f-m5ni",
+            "issued": "2018-06-26",
+            "keyword": [
+                "mars",
+                "mars exploration rover"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MER1-M-HAZCAM-5-MESH-OPS-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mer1-m-hazcam-5-mesh-ops-v1.0_rg8f-m5ni",
-            "description": "not applicable",
-            "title": "MER 1 MARS HAZARD AVOID CAMERA TERRAIN MESH RDR OPS V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "MER 1 MARS HAZARD AVOID CAMERA TERRAIN MESH RDR OPS V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/NADIR-2MEC1",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "SWOT. 2022-01-31. SWOT Level-2 Simulated SSH from MITgcm LLC4320 Science Quality Version 1.0. Version 1.0. PO.DAAC. Archived by National Aeronautics and Space Administration, U.S. Government, PO.DAAC. https://doi.org/10.5067/NADIR-2MEC1.",
-            "issued": "2022-01-31",
-            "temporal": "2011-11-13T00:00:00Z/2012-11-12T00:50:15.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2012-11-12",
-            "references": [
-                "https://doi.org/10.1175/JTECH-D-15-0160.1"
-            ],
-            "keyword": [
-                "earth science",
-                "oceans",
-                "sea surface topography"
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
-            "identifier": "C2158344213-POCLOUD",
-            "description": "This dataset provides simulated sea surface height (SSH) in a format similar to the future SWOT Level 2 (L2) altimetry data stream from the Poseidon 3C nadir altimeter. The simulated data were generated by the \"ECCO LLC4320\" global ocean simulation. ECCO, which means \"Estimating the Circulation and Climate of the Ocean\", is a data assimilation and model (and the international consortium of scientists who maintains it) based on the MIT general circulation model (MITgcm) that assimilates and constrains observational data from numerous sources to estimate the ocean state. The model operates on the Lat-Lon-Cap (LLC) grid with a nominal horizontal resolution of 1/48-degrees (when approximated over the entire model domain, corresponding to ~2-km cell size at the equator). SSH data produced by ECCO LLC4320 were rendered from the native output format into the format prescribed in the SWOT L2 SSH PDD to aid ongoing data product development and to benefit future users of data produced during operational phases of the SWOT mission.",
-            "release-place": "PO.DAAC",
-            "graphic-preview-description": "Thumbnail",
             "creator": "SWOT",
-            "title": "SWOT Simulated Level-2 Nadir SSH from MITgcm ECCO LLC4320 for Cal/Val Version 1",
-            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/SWOT_SIMULATED_L2_NADIR_SSH_ECCO_LLC4320_CALVAL_V1.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "This dataset provides simulated sea surface height (SSH) in a format similar to the future SWOT Level 2 (L2) altimetry data stream from the Poseidon 3C nadir altimeter. The simulated data were generated by the \"ECCO LLC4320\" global ocean simulation. ECCO, which means \"Estimating the Circulation and Climate of the Ocean\", is a data assimilation and model (and the international consortium of scientists who maintains it) based on the MIT general circulation model (MITgcm) that assimilates and constrains observational data from numerous sources to estimate the ocean state. The model operates on the Lat-Lon-Cap (LLC) grid with a nominal horizontal resolution of 1/48-degrees (when approximated over the entire model domain, corresponding to ~2-km cell size at the equator). SSH data produced by ECCO LLC4320 were rendered from the native output format into the format prescribed in the SWOT L2 SSH PDD to aid ongoing data product development and to benefit future users of data produced during operational phases of the SWOT mission.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FNADIR-2MEC1",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FNADIR-2MEC1",
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
-                    "downloadURL": "https://podaac.jpl.nasa.gov/SWOT",
-                    "description": "Mission and Instrument Overview",
                     "@type": "dcat:Distribution",
+                    "description": "Mission and Instrument Overview",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/SWOT",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
                     "@type": "dcat:Distribution",
+                    "description": "Generic Data Readers",
                     "downloadURL": "https://github.com/podaac/data-readers",
-                    "mediaType": "text/html",
-                    "description": "Generic Data Readers"
+                    "mediaType": "text/html"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/SWOT_SIMULATED_L2_NADIR_SSH_ECCO_LLC4320_CALVAL_V1.jpg",
-                    "description": "Thumbnail",
                     "@type": "dcat:Distribution",
+                    "description": "Thumbnail",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/SWOT_SIMULATED_L2_NADIR_SSH_ECCO_LLC4320_CALVAL_V1.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2158344213-POCLOUD",
-                    "description": "HTTPS endpoint for data browse and download",
                     "@type": "dcat:Distribution",
+                    "description": "HTTPS endpoint for data browse and download",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2158344213-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2158344213-POCLOUD",
-                    "description": "Browse granule search results in Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse granule search results in Earthdata Search",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2158344213-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
@@ -1304651,277 +1304626,275 @@
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
+            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/SWOT_SIMULATED_L2_NADIR_SSH_ECCO_LLC4320_CALVAL_V1.jpg",
+            "identifier": "C2158344213-POCLOUD",
+            "issued": "2022-01-31",
+            "keyword": [
+                "earth science",
+                "oceans",
+                "sea surface topography"
+            ],
+            "landingPage": "https://doi.org/10.5067/NADIR-2MEC1",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2012-11-12",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/JPL/PODAAC"
+            },
+            "references": [
+                "https://doi.org/10.1175/JTECH-D-15-0160.1"
+            ],
+            "release-place": "PO.DAAC",
             "spatial": "-180.0 -77.6 180.0 77.6",
+            "temporal": "2011-11-13T00:00:00Z/2012-11-12T00:50:15.999Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "SWOT Simulated Level-2 Nadir SSH from MITgcm ECCO LLC4320 for Cal/Val Version 1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-I0037-5-SHAPE8567-V1.0",
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
-                "asteroid 8567"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "We present the three-dimensional shape   and rotation state of near-Earth asteroid (8567) 1996 HW1 based on     radar images and optical lightcurves (Magri et al., 2011). 1996 HW1    was observed in 2008 using the 12.6-cm radar at Arecibo Observatory.   Optical lightcurves were obtained at several observatories and used to further constrain the shape modeling.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-i0037-5-shape8567-v1.0_rgea-4xnw",
+            "issued": "2021-05-21",
+            "keyword": [
+                "support archives",
+                "asteroid 8567"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-I0037-5-SHAPE8567-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-i0037-5-shape8567-v1.0_rgea-4xnw",
-            "description": "We present the three-dimensional shape   and rotation state of near-Earth asteroid (8567) 1996 HW1 based on     radar images and optical lightcurves (Magri et al., 2011). 1996 HW1    was observed in 2008 using the 12.6-cm radar at Arecibo Observatory.   Optical lightcurves were obtained at several observatories and used to further constrain the shape modeling.",
-            "title": "SHAPE AND ROTATION OF (8567) 1996 HW1   \n        V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "SHAPE AND ROTATION OF (8567) 1996 HW1   \n        V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC2-0681-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 2 phase 2015-03-11 to 2015-06-30. It is a Global Gravity measurement at the comet 67P and covers the time 2015-03-29T05:04:40.000 to 2015-03-29T08:43:34.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc2-0681-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC2-0681-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc2-0681-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 2 phase 2015-03-11 to 2015-06-30. It is a Global Gravity measurement at the comet 67P and covers the time 2015-03-29T05:04:40.000 to 2015-03-29T08:43:34.000.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 2 0681 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 2 0681 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=HAY-A-SPICE-6-V1.0",
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
-                "hayabusa",
-                "25143 itokawa"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This data set includes the complete set of Hayabusa SPICE data files (``kernel files'') for the surveying and collection phases of the mission. The SPICE data files, which can be accessed using SPICE software, contain geometric and other ancillary information needed to recover the full value of the science instrument data. In particular SPICE kernels provide spacecraft and planetary ephemerides, instrument mounting alignments, spacecraft orientation, spacecraft sequences of events, and data needed for relevant time conversions.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.hay-a-spice-6-v1.0_rghd-nhf2",
+            "issued": "2018-06-26",
+            "keyword": [
+                "hayabusa",
+                "25143 itokawa"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=HAY-A-SPICE-6-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.hay-a-spice-6-v1.0_rghd-nhf2",
-            "description": "This data set includes the complete set of Hayabusa SPICE data files (``kernel files'') for the surveying and collection phases of the mission. The SPICE data files, which can be accessed using SPICE software, contain geometric and other ancillary information needed to recover the full value of the science instrument data. In particular SPICE kernels provide spacecraft and planetary ephemerides, instrument mounting alignments, spacecraft orientation, spacecraft sequences of events, and data needed for relevant time conversions.",
-            "title": "HAYABUSA SPICE KERNELS V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "HAYABUSA SPICE KERNELS V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ECOSTRESS/ECO_L2T_STARS.002",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Simon Hook, Gregory Halverson, Margaret Johnson, Kerry Cawse-Nicholson. 2023-11-14. ECOSTRESS Tiled Ancillary NDVI and Albedo L2 Global 70 m V002. Version 002. Sioux Falls, South Dakota, USA. Archived by National Aeronautics and Space Administration, U.S. Government, NASA EOSDIS Land Processes Distributed Active Archive Center. https://doi.org/10.5067/ECOSTRESS/ECO_L2T_STARS.002. http://doi.org/10.5067/ECOSTRESS/ECO_L2T_STARS.002. The DOI landing page provides citations in APA and Chicago styles.",
-            "issued": "2023-11-14",
-            "temporal": "2018-07-09T00:00:00Z/2024-06-03T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-11-14",
-            "keyword": [
-                "surface radiative properties",
-                "land surface",
-                "land use/land cover",
-                "earth science",
-                "surface thermal properties"
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
-            "identifier": "C2090073749-LPCLOUD",
-            "description": "The ECOsystem Spaceborne Thermal Radiometer Experiment on Space Station (ECOSTRESS) mission measures the temperature of plants to better understand how much water plants need and how they respond to stress. ECOSTRESS is attached to the International Space Station (ISS) and collects data globally between 52\u00b0 N and 52\u00b0 S latitudes. A map of the acquisition coverage can be found in figure 2 on the ECOSTRESS website(https://ecostress.jpl.nasa.gov/science).\r\n\r\nThe ECOSTRESS Tiled Ancillary NDVI and Albedo Level 2 Global 70 m (ECO_L2T_STARS) Version 2 data product provides Normalized Difference Vegetation Index (NDVI) and albedo aligned with each daytime ECOSTRESS overpass. ECO_L2T_STARS is an ancillary data product derived from Visible Infrared Imaging Radiometer Suite (VIIRS) and Harmonized Landsat Sentinel (HLS) Version 2 data sources with application to the ECOSTRESS mission. This data product fuses fine resolution inputs from HLS surface reflectance products and moderate resolution inputs from the daily NASA/NOAA Suomi National Polar-orbiting Partnership (Suomi NPP) VIIRS surface reflectance (VNP09GA) product. The data fusion is performed using a variant of the Spatial Timeseries for Automated high-Resolution multi-Sensor data fusion (STARS) algorithm to create tiles matching the ECOSTRESS standard resolution of 70 meters (m). STARS is a Bayesian timeseries methodology that provides streaming data fusion and uncertainty quantification through efficient Kalman filtering. Refer to Section 3.1 of the ECOSTRESS Jet Propulsion Laboratory (JPL) EvapoTranspiration (JET) Level-3 Algorithm Theoretical Basis Document (ATBD) for further details of the Bidirectional Reflectance Distribution Function (BRDF) implementation and albedo calculations.\r\n\r\nThe ECO_L2T_STARS Version 2 data product is provided in Cloud Optimized GeoTIFF (COG) format using a modified version of the Military Grid Reference System (MGRS), which divides Universal Transverse Mercator (UTM) zones into square tiles that are 109.8 km by 109.8 km with a 70 m spatial resolution. Each band is distributed as a separate COG. This product contains four layers including NDVI, NDVI uncertainty, albedo, and albedo uncertainty. The ECO_L2T_STARS ancillary NDVI and albedo product is only generated for corresponding daytime ECOSTRESS Tiled Land Surface Temperature and Emissivity Instantaneous Level 2 Global 70 m (ECO_L2T_LSTE) Version 2 tiles.\r\n\r\nThe ECOSTRESS Tiled Ancillary NDVI and Albedo Level 2 Global 70 m (ECO_L2T_STARS) Version 2 data product provides Normalized Difference Vegetation Index (NDVI) and albedo aligned with each daytime ECOSTRESS overpass. ECO_L2T_STARS is an ancillary data product derived from Visible Infrared Imaging Radiometer Suite (VIIRS) ( https://lpdaac.usgs.gov/product_search/?query=viirs&status=Operational&view=list&sort=title) and Harmonized Landsat Sentinel (HLS) ( https://lpdaac.usgs.gov/product_search/?collections=HLS&status=Operational&view=list) Version 2 data sources with application to the ECOSTRESS mission. This data product fuses fine resolution inputs from HLS surface reflectance products and moderate resolution inputs from the daily NASA/NOAA Suomi National Polar-orbiting Partnership (Suomi NPP) VIIRS surface reflectance (VNP09GA) ( https://doi.org/10.5067/VIIRS/VNP09GA.001) product. The data fusion is performed using a variant of the Spatial Timeseries for Automated high-Resolution multi-Sensor data fusion (STARS) algorithm to create tiles matching the ECOSTRESS standard resolution of 70 meters (m). STARS is a Bayesian timeseries methodology that provides streaming data fusion and uncertainty quantification through efficient Kalman filtering. Refer to Section 3.1 of the ECOSTRESS Jet Propulsion Laboratory (JPL) EvapoTranspiration (JET) Level-3 Algorithm Theoretical Basis Document (ATBD) for further details of the Bidirectional Reflectance Distribution Function (BRDF) implementation and albedo calculations.\r\n\r\nThe ECO_L2T_STARS Version 2 data pr",
-            "release-place": "Sioux Falls, South Dakota, USA",
             "creator": "Simon Hook, Gregory Halverson, Margaret Johnson, Kerry Cawse-Nicholson",
-            "title": "ECOSTRESS Tiled Ancillary NDVI and Albedo L2 Global 70 m V002",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The ECOsystem Spaceborne Thermal Radiometer Experiment on Space Station (ECOSTRESS) mission measures the temperature of plants to better understand how much water plants need and how they respond to stress. ECOSTRESS is attached to the International Space Station (ISS) and collects data globally between 52\u00b0 N and 52\u00b0 S latitudes. A map of the acquisition coverage can be found in figure 2 on the ECOSTRESS website(https://ecostress.jpl.nasa.gov/science).\r\n\r\nThe ECOSTRESS Tiled Ancillary NDVI and Albedo Level 2 Global 70 m (ECO_L2T_STARS) Version 2 data product provides Normalized Difference Vegetation Index (NDVI) and albedo aligned with each daytime ECOSTRESS overpass. ECO_L2T_STARS is an ancillary data product derived from Visible Infrared Imaging Radiometer Suite (VIIRS) and Harmonized Landsat Sentinel (HLS) Version 2 data sources with application to the ECOSTRESS mission. This data product fuses fine resolution inputs from HLS surface reflectance products and moderate resolution inputs from the daily NASA/NOAA Suomi National Polar-orbiting Partnership (Suomi NPP) VIIRS surface reflectance (VNP09GA) product. The data fusion is performed using a variant of the Spatial Timeseries for Automated high-Resolution multi-Sensor data fusion (STARS) algorithm to create tiles matching the ECOSTRESS standard resolution of 70 meters (m). STARS is a Bayesian timeseries methodology that provides streaming data fusion and uncertainty quantification through efficient Kalman filtering. Refer to Section 3.1 of the ECOSTRESS Jet Propulsion Laboratory (JPL) EvapoTranspiration (JET) Level-3 Algorithm Theoretical Basis Document (ATBD) for further details of the Bidirectional Reflectance Distribution Function (BRDF) implementation and albedo calculations.\r\n\r\nThe ECO_L2T_STARS Version 2 data product is provided in Cloud Optimized GeoTIFF (COG) format using a modified version of the Military Grid Reference System (MGRS), which divides Universal Transverse Mercator (UTM) zones into square tiles that are 109.8 km by 109.8 km with a 70 m spatial resolution. Each band is distributed as a separate COG. This product contains four layers including NDVI, NDVI uncertainty, albedo, and albedo uncertainty. The ECO_L2T_STARS ancillary NDVI and albedo product is only generated for corresponding daytime ECOSTRESS Tiled Land Surface Temperature and Emissivity Instantaneous Level 2 Global 70 m (ECO_L2T_LSTE) Version 2 tiles.\r\n\r\nThe ECOSTRESS Tiled Ancillary NDVI and Albedo Level 2 Global 70 m (ECO_L2T_STARS) Version 2 data product provides Normalized Difference Vegetation Index (NDVI) and albedo aligned with each daytime ECOSTRESS overpass. ECO_L2T_STARS is an ancillary data product derived from Visible Infrared Imaging Radiometer Suite (VIIRS) ( https://lpdaac.usgs.gov/product_search/?query=viirs&status=Operational&view=list&sort=title) and Harmonized Landsat Sentinel (HLS) ( https://lpdaac.usgs.gov/product_search/?collections=HLS&status=Operational&view=list) Version 2 data sources with application to the ECOSTRESS mission. This data product fuses fine resolution inputs from HLS surface reflectance products and moderate resolution inputs from the daily NASA/NOAA Suomi National Polar-orbiting Partnership (Suomi NPP) VIIRS surface reflectance (VNP09GA) ( https://doi.org/10.5067/VIIRS/VNP09GA.001) product. The data fusion is performed using a variant of the Spatial Timeseries for Automated high-Resolution multi-Sensor data fusion (STARS) algorithm to create tiles matching the ECOSTRESS standard resolution of 70 meters (m). STARS is a Bayesian timeseries methodology that provides streaming data fusion and uncertainty quantification through efficient Kalman filtering. Refer to Section 3.1 of the ECOSTRESS Jet Propulsion Laboratory (JPL) EvapoTranspiration (JET) Level-3 Algorithm Theoretical Basis Document (ATBD) for further details of the Bidirectional Reflectance Distribution Function (BRDF) implementation and albedo calculations.\r\n\r\nThe ECO_L2T_STARS Version 2 data pr",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FECOSTRESS%2FECO_L2T_STARS.002",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FECOSTRESS%2FECO_L2T_STARS.002",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=C2090073749-LPCLOUD",
-                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=C2090073749-LPCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/ECOSTRESS/ECO_L2T_STARS.002",
-                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
+                    "downloadURL": "https://doi.org/10.5067/ECOSTRESS/ECO_L2T_STARS.002",
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
-                    "downloadURL": "https://lpdaac.usgs.gov/documents/1869/ECOSTRESSL3JET_ATBD_V1.pdf",
-                    "description": "The ATBD provides physical theory and mathematical procedures for the calculations used to produce the data products.",
                     "@type": "dcat:Distribution",
+                    "description": "The ATBD provides physical theory and mathematical procedures for the calculations used to produce the data products.",
+                    "downloadURL": "https://lpdaac.usgs.gov/documents/1869/ECOSTRESSL3JET_ATBD_V1.pdf",
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
                     "@type": "dcat:Distribution",
+                    "description": "Browse Image",
                     "downloadURL": "https://cmr.earthdata.nasa.gov/browse-scaler/browse_images/granules/G2788445669-LPCLOUD?h=85&w=85",
-                    "mediaType": "text/html",
-                    "description": "Browse Image"
+                    "mediaType": "text/html"
                 }
             ],
+            "identifier": "C2090073749-LPCLOUD",
+            "issued": "2023-11-14",
+            "keyword": [
+                "surface radiative properties",
+                "land surface",
+                "land use/land cover",
+                "earth science",
+                "surface thermal properties"
+            ],
+            "landingPage": "https://doi.org/10.5067/ECOSTRESS/ECO_L2T_STARS.002",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2023-11-14",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "LP DAAC"
+            },
+            "release-place": "Sioux Falls, South Dakota, USA",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2018-07-09T00:00:00Z/2024-06-03T00:00:00Z",
             "theme": [
                 "ECOSTRESS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "ECOSTRESS Tiled Ancillary NDVI and Albedo L2 Global 70 m V002"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/GPM/DPR/SLH/3A-DAY/07",
             "citation": "GPM Science Team. 2022-05-09. GPM_3HSLH_DAY. GPM DPR Spectral Latent Heating Profiles L3 1 day 0.5 degree x 0.5 degree V07. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/GPM/DPR/SLH/3A-DAY/07. https://disc.gsfc.nasa.gov/datacollection/GPM_3HSLH_DAY_07.html. Digital Science Data.",
-            "issued": "2022-05-09",
-            "temporal": "2014-03-09T00:00:00Z/2023-02-28T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-05-01",
-            "references": [
-                "https://doi.org/10.1175/2009JCLI3110.1",
-                "https://doi.org/10.1175/1520-0469(1973)030%3C0611%3ADOBPOT%3E2.0.CO%3B2"
-            ],
-            "keyword": [
-                "atmospheric water vapor",
-                "atmosphere",
-                "earth science",
-                "precipitation"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Dr. Yukari Takayabu",
                 "hasEmail": "mailto:yukari@ccsr.u-tokyo.ac.jp"
             },
+            "creator": "GPM Science Team",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C2179081641-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "Version 07 is the current version of the data set. Older versions will no longer be available and have been superseded by Version 07.\nThe Gridded  Spectral Latent Heating (3HSLH) products contain latent heating, Q1-QR and Q2 profiles from DPR raindata.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "GPM_3HSLH_DAY",
-            "creator": "GPM Science Team",
-            "title": "GPM DPR Spectral Latent Heating Profiles L3 1 day 0.5 degree x 0.5 degree V07 (GPM_3HSLH_DAY) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/GPM/browse/GPM_3HSLH_DAY_07.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGPM%2FDPR%2FSLH%2F3A-DAY%2F07",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGPM%2FDPR%2FSLH%2F3A-DAY%2F07",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
@@ -1304931,476 +1304904,482 @@
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/GPM_3HSLH_DAY_07.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/GPM_3HSLH_DAY_07.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://gpm1.gesdisc.eosdis.nasa.gov/data/GPM_L3/GPM_3HSLH_DAY.07/",
-                    "description": "Access the data via HTTPS",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS",
+                    "downloadURL": "https://gpm1.gesdisc.eosdis.nasa.gov/data/GPM_L3/GPM_3HSLH_DAY.07/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=GPM_3HSLH_DAY_07",
-                    "description": "Use the Earthdata Search Client to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search Client to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=GPM_3HSLH_DAY_07",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://gpm1.gesdisc.eosdis.nasa.gov/opendap/GPM_L3/GPM_3HSLH_DAY.07/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://gpm1.gesdisc.eosdis.nasa.gov/opendap/GPM_L3/GPM_3HSLH_DAY.07/contents.html",
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
-                    "downloadURL": "https://gpm1.gesdisc.eosdis.nasa.gov/data/GPM_L3/doc/README.GPM.pdf",
-                    "description": "README Document",
                     "@type": "dcat:Distribution",
+                    "description": "README Document",
+                    "downloadURL": "https://gpm1.gesdisc.eosdis.nasa.gov/data/GPM_L3/doc/README.GPM.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's read me document"
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
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://pps.gsfc.nasa.gov/Documents/GPM_SLH_V07A_ReleaseNote_20211117.pdf",
-                    "description": "Release Notes",
                     "@type": "dcat:Distribution",
+                    "description": "Release Notes",
+                    "downloadURL": "https://pps.gsfc.nasa.gov/Documents/GPM_SLH_V07A_ReleaseNote_20211117.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View an important notice for this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://pps.gsfc.nasa.gov/Documents/GPM_SLH_V06B_ATBD_20200706.pdf",
-                    "description": "Algorithm Theoretical Basis Document",
                     "@type": "dcat:Distribution",
+                    "description": "Algorithm Theoretical Basis Document",
+                    "downloadURL": "https://pps.gsfc.nasa.gov/Documents/GPM_SLH_V06B_ATBD_20200706.pdf",
+                    "mediaType": "application/pdf",
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
                 }
             ],
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/GPM/browse/GPM_3HSLH_DAY_07.png",
+            "identifier": "C2179081641-GES_DISC",
+            "issued": "2022-05-09",
+            "keyword": [
+                "atmospheric water vapor",
+                "atmosphere",
+                "earth science",
+                "precipitation"
+            ],
+            "landingPage": "https://doi.org/10.5067/GPM/DPR/SLH/3A-DAY/07",
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
+                "https://doi.org/10.1175/2009JCLI3110.1",
+                "https://doi.org/10.1175/1520-0469(1973)030%3C0611%3ADOBPOT%3E2.0.CO%3B2"
+            ],
+            "release-place": "Greenbelt, MD, USA",
+            "series-name": "GPM_3HSLH_DAY",
             "spatial": "-180.0 -67.0 180.0 67.0",
+            "temporal": "2014-03-09T00:00:00Z/2023-02-28T00:00:00Z",
             "theme": [
                 "GPM",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "GPM DPR Spectral Latent Heating Profiles L3 1 day 0.5 degree x 0.5 degree V07 (GPM_3HSLH_DAY) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VL1%2FVL2-M-MET-4-DAILY-AVG-PRESSURE-V1.0",
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
-                "viking"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This data set contains summary pressure data obtained from the Viking Meteorology Instrument System (VMIS) through the duration of the Viking Lander 1 and 2 missions. The data are derived from the ambient pressure sensor carried onboard the Landers. The data set consists of the daily average pressure values and relevant statistics presented on a sol by sol basis. For further background information on the VMIS and results from this experiment, see CHAMBERLAIN_ETAL1976, HESS_ETAL_1977, TILLMAN_ETAL_1979, HESS_ETAL_1980, and SHARMAN_RYAN_1980. An earlier version of this data set, including descriptive documents and plots on microfiche, is archived at the NSSDC (NSSDC ID 75-075C-07I, 75-075C-07J, 75-083C-07I, and 75-083C-07J).",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vl1-vl2-m-met-4-daily-avg-pressure-v1.0_rgm3-wypp",
+            "issued": "2018-06-26",
+            "keyword": [
+                "mars",
+                "viking"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VL1%2FVL2-M-MET-4-DAILY-AVG-PRESSURE-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vl1-vl2-m-met-4-daily-avg-pressure-v1.0_rgm3-wypp",
-            "description": "This data set contains summary pressure data obtained from the Viking Meteorology Instrument System (VMIS) through the duration of the Viking Lander 1 and 2 missions. The data are derived from the ambient pressure sensor carried onboard the Landers. The data set consists of the daily average pressure values and relevant statistics presented on a sol by sol basis. For further background information on the VMIS and results from this experiment, see CHAMBERLAIN_ETAL1976, HESS_ETAL_1977, TILLMAN_ETAL_1979, HESS_ETAL_1980, and SHARMAN_RYAN_1980. An earlier version of this data set, including descriptive documents and plots on microfiche, is archived at the NSSDC (NSSDC ID 75-075C-07I, 75-075C-07J, 75-083C-07I, and 75-083C-07J).",
-            "title": "VL1/VL2 MARS METEOROLOGY RESAMPLED DAILY AVG PRESSURE V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "VL1/VL2 MARS METEOROLOGY RESAMPLED DAILY AVG PRESSURE V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/GPM/GMI/BASE-RSS/07",
             "citation": "GPM Science Team. 2022-05-09. GPM_BASEGPMGMI_RSS. Version 07. GPM GMI RSS Common Calibrated Brightness Temperatures L1BASE 1.5 hours 13 km V07. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, NASA Goddard Earth Science Data and Information Services Center (GES DISC). https://doi.org/10.5067/GPM/GMI/BASE-RSS/07. https://disc.gsfc.nasa.gov/datacollection/GPM_BASEGPMGMI_RSS_07.html. Digital Science Data.",
-            "issued": "2022-05-09",
-            "temporal": "2014-03-04T00:00:00Z/2023-03-01T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-05-01",
-            "keyword": [
-                "atmosphere",
-                "precipitation",
-                "atmospheric water vapor",
-                "earth science"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "CHRISTOPHER COHOON",
                 "hasEmail": "mailto:helpdesk@pps-mail.nascom.nasa.gov"
             },
+            "creator": "GPM Science Team",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C2259345441-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "Version 07 is the current version of the data set. Older versions are no longer available and have been superseded by the current version.\n\nThis GPM GMI dataset contains  \"GMI Antenna Temperatures\", and is written as a multi-Swath Structure. Swath S1 has channels 1-9: 10V 10H 19V 19H 23V 37V 37H 89V 89H. Swath S2 has channels 10-13: 166V 166H 183+/-3V 183+/-8V. GMIBASERSS is the standard GMI calibration product with full precision of all physical fields. It contains one full orbit plus 200 overlap scans from previous orbit and 200 overlap scans from the post orbit.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "GPM_BASEGPMGMI_RSS",
-            "creator": "GPM Science Team",
-            "title": "GPM GMI RSS Common Calibrated Brightness Temperatures L1BASE 1.5 hours 13 km V07 (GPM_BASEGPMGMI_RSS) at GES DISC",
-            "graphic-preview-description": "Brightness Temperature from GPM GMI (13 km x 13 km) for 06/30/2016 (GPM_BASEGPMGMI_RSS)",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/GPM_BASEGPMGMI_RSS_05.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGPM%2FGMI%2FBASE-RSS%2F07",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGPM%2FGMI%2FBASE-RSS%2F07",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/GPM_BASEGPMGMI_RSS_05.png",
-                    "description": "Brightness Temperature from GPM GMI (13 km x 13 km) for 06/30/2016 (GPM_BASEGPMGMI_RSS)",
                     "@type": "dcat:Distribution",
+                    "description": "Brightness Temperature from GPM GMI (13 km x 13 km) for 06/30/2016 (GPM_BASEGPMGMI_RSS)",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/GPM_BASEGPMGMI_RSS_05.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/GPM_BASEGPMGMI_RSS_07.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/GPM_BASEGPMGMI_RSS_07.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://gpm1.gesdisc.eosdis.nasa.gov/data/GPM_L1BASE/GPM_BASEGPMGMI_RSS.07/",
-                    "description": "Access the data via HTTPS",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS",
+                    "downloadURL": "https://gpm1.gesdisc.eosdis.nasa.gov/data/GPM_L1BASE/GPM_BASEGPMGMI_RSS.07/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=GPM_BASEGPMGMI_RSS_07",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=GPM_BASEGPMGMI_RSS_07",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://gpm1.gesdisc.eosdis.nasa.gov/opendap/hyrax/GPM_L1BASE/GPM_BASEGPMGMI_RSS.07/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol",
+                    "downloadURL": "https://gpm1.gesdisc.eosdis.nasa.gov/opendap/hyrax/GPM_L1BASE/GPM_BASEGPMGMI_RSS.07/contents.html",
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
-                    "downloadURL": "https://gpm1.gesdisc.eosdis.nasa.gov/data/GPM_L1BASE/doc/README.GPM.pdf",
-                    "description": "README Document",
                     "@type": "dcat:Distribution",
+                    "description": "README Document",
+                    "downloadURL": "https://gpm1.gesdisc.eosdis.nasa.gov/data/GPM_L1BASE/doc/README.GPM.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's read me document"
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
+            "graphic-preview-description": "Brightness Temperature from GPM GMI (13 km x 13 km) for 06/30/2016 (GPM_BASEGPMGMI_RSS)",
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/GPM_BASEGPMGMI_RSS_05.png",
+            "identifier": "C2259345441-GES_DISC",
+            "issued": "2022-05-09",
+            "keyword": [
+                "atmosphere",
+                "precipitation",
+                "atmospheric water vapor",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/GPM/GMI/BASE-RSS/07",
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
+            "series-name": "GPM_BASEGPMGMI_RSS",
             "spatial": "-180.0 -70.0 180.0 70.0",
+            "temporal": "2014-03-04T00:00:00Z/2023-03-01T00:00:00Z",
             "theme": [
                 "GPM",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "GPM GMI RSS Common Calibrated Brightness Temperatures L1BASE 1.5 hours 13 km V07 (GPM_BASEGPMGMI_RSS) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/MEASURES/DMSP-F14/SSMI/DATA302",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Wentz, Frank J, Kyle Hilburn and Deborah K Smith.2012. RSS SSM/I OCEAN PRODUCT GRIDS 3-DAY AVERAGE FROM DMSP F14 NETCDF [indicate subset used]. Dataset available online from the NASA Global Hydrometeorology Resource Center DAAC, Huntsville, Alabama, U.S.A. DOI: http://dx.doi.org/10.5067/MEASURES/DMSP-F14/SSMI/DATA302",
-            "issued": "2012-08-08",
-            "temporal": "1997-05-06T00:00:00Z/2008-08-08T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-04-28",
-            "keyword": [
-                "earth science",
-                "clouds",
-                "precipitation",
-                "ocean winds",
-                "atmospheric water vapor",
-                "atmosphere",
-                "atmospheric winds",
-                "oceans"
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
-            "identifier": "C1979928137-GHRC_DAAC",
             "description": "The RSS SSM/I Ocean Product Grids 3-Day Average from DMSP F14 netCDF dataset is part of the collection of Special Sensor Microwave/Imager (SSM/I) and Special Sensor Microwave Imager Sounder (SSMIS) data products produced as part of NASA's MEaSUREs Program. Remote Sensing Systems generates SSM/I and SSMIS binary data products using a unified, physically based algorithm to simultaneously retrieve ocean wind speed, water vapor, cloud water, and rain rate. The SSMIS data have been carefully intercalibrated to the brightness temperature level of the previous SSM/I and therefore extend this important time series of ocean winds, vapor, cloud and rain values. This algorithm is a product of 20 years of refinements, improvements, and verifications. The Global Hydrology Resource Center has reformatted the binary data into a netCDF data product for each temporal group for each satellite. The netCDF SSMI/SSMIS collection will be available for F14 for a 3-day average.",
-            "graphic-preview-description": "N/A",
-            "title": "RSS SSM/I OCEAN PRODUCT GRIDS 3-DAY AVERAGE FROM DMSP F14 NETCDF V7",
-            "graphic-preview-file": "https://ghrc.nsstc.nasa.gov/pub/ssmi/f14/3day/browse/",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMEASURES%2FDMSP-F14%2FSSMI%2FDATA302",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMEASURES%2FDMSP-F14%2FSSMI%2FDATA302",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=rssmif14d3d",
-                    "description": "Files may be downloaded directly to your workstation from this link",
                     "@type": "dcat:Distribution",
+                    "description": "Files may be downloaded directly to your workstation from this link",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=rssmif14d3d",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/ssmi/f14/3day/browse/2000/f14_ssmi_20000302v7_d3d_CW.png",
-                    "description": "Sample browse image",
                     "@type": "dcat:Distribution",
+                    "description": "Sample browse image",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/ssmi/f14/3day/browse/2000/f14_ssmi_20000302v7_d3d_CW.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/ssmi/f14/3day/browse/2000/f14_ssmi_20000302v7_d3d_WV.png",
-                    "description": "Sample browse image",
                     "@type": "dcat:Distribution",
+                    "description": "Sample browse image",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/ssmi/f14/3day/browse/2000/f14_ssmi_20000302v7_d3d_WV.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/ssmi/f14/3day/browse/2000/f14_ssmi_20000302v7_d3d_RR.png",
-                    "description": "Sample browse image",
                     "@type": "dcat:Distribution",
+                    "description": "Sample browse image",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/ssmi/f14/3day/browse/2000/f14_ssmi_20000302v7_d3d_RR.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/ssmi/f14/3day/browse/2000/f14_ssmi_20000302v7_d3d_WS.png",
-                    "description": "Sample browse image",
                     "@type": "dcat:Distribution",
+                    "description": "Sample browse image",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/ssmi/f14/3day/browse/2000/f14_ssmi_20000302v7_d3d_WS.png",
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
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/opendap/ssmi/f14/3day/",
-                    "description": "OPeNDAP server dataset access",
                     "@type": "dcat:Distribution",
+                    "description": "OPeNDAP server dataset access",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/opendap/ssmi/f14/3day/",
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
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/doc/ssmi_netcdf/2012_Wentz_011012_Version-7_SSMI_Calibration.pdf",
-                    "description": "SSM/I Version-7 Calibration Report",
                     "@type": "dcat:Distribution",
+                    "description": "SSM/I Version-7 Calibration Report",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/doc/ssmi_netcdf/2012_Wentz_011012_Version-7_SSMI_Calibration.pdf",
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
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/ssmi/f14/3day/browse/",
-                    "description": "N/A",
                     "@type": "dcat:Distribution",
+                    "description": "N/A",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/ssmi/f14/3day/browse/",
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
+            "graphic-preview-file": "https://ghrc.nsstc.nasa.gov/pub/ssmi/f14/3day/browse/",
+            "identifier": "C1979928137-GHRC_DAAC",
+            "issued": "2012-08-08",
+            "keyword": [
+                "earth science",
+                "clouds",
+                "precipitation",
+                "ocean winds",
+                "atmospheric water vapor",
+                "atmosphere",
+                "atmospheric winds",
+                "oceans"
+            ],
+            "landingPage": "https://doi.org/10.5067/MEASURES/DMSP-F14/SSMI/DATA302",
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
+            "temporal": "1997-05-06T00:00:00Z/2008-08-08T23:59:59Z",
             "theme": [
                 "DISCOVER",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "RSS SSM/I OCEAN PRODUCT GRIDS 3-DAY AVERAGE FROM DMSP F14 NETCDF V7"
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
-                "lunar",
-                "catalog"
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
-            "identifier": "NASA-878",
             "description": "Apollo 16 Surface Sampler Data Package by L. Carrasco",
-            "title": "Apollo 16 Surface Sampler Data Package",
-            "programCode": [
-                "026:008"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -1305408,737 +1305387,741 @@
                     "mediaType": "application/pdf"
                 }
             ],
-            "accrualPeriodicity": "irregular",
+            "identifier": "NASA-878",
+            "issued": "2018-06-25",
+            "keyword": [
+                "apollo",
+                "sample",
+                "lunar",
+                "catalog"
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
+            "title": "Apollo 16 Surface Sampler Data Package"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.7927/H44Q7RWV",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Imhoff, M.L., L. Bounoua, T. Ricketts, C. Loucks, R. Harriss, and W.T. Lawrence. 2004-12-31. HANPP Collection: Global Patterns in Human Appropriation of Net Primary Productivity (HANPP). Version 1.00. Palisades, NY. Archived by National Aeronautics and Space Administration, U.S. Government, NASA Socioeconomic Data and Applications Center (SEDAC). https://doi.org/10.7927/H44Q7RWV. https://doi.org/10.7927/H44Q7RWV.",
-            "issued": "2004-12-31",
-            "temporal": "1995-01-01T00:00:00Z/1995-12-31T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2004-12-31",
-            "references": [
-                "https://doi.org/10.1038/nature02619",
-                "https://doi.org/10.7927/H48G8HMK",
-                "https://doi.org/10.7927/H40Z715X",
-                "https://doi.org/10.7927/H4W66HPJ"
-            ],
-            "keyword": [
-                "earth science",
-                "biosphere",
-                "vegetation"
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
-            "identifier": "C139824016-SEDAC",
-            "description": "The HANPP Collection: Global Patterns in Human Appropriation of Net Primary Productivity (HANPP) represents a digital map of human appropriation of net primary productivity measured in Units of elemental carbon on a one-quarter degree global grid. Net primary productivity (NPP), the net amount of solar energy converted to plant organic matter through photosynthesis, can be measured in Units of elemental carbon and represents the primary food energy source for the world's ecosystems. Humans appropriate net primary productivity through the consumption of food, paper, wood and fiber, which alters the composition of the atmosphere, levels of biodiversity, energy flows within food webs and the provision of important ecosystem services.  The data set is distributed by the Columbia University Center for International Earth Science Information Network (CIESIN).",
-            "release-place": "Palisades, NY",
-            "graphic-preview-description": "Maps Download Page",
             "creator": "Imhoff, M.L., L. Bounoua, T. Ricketts, C. Loucks, R. Harriss, and W.T. Lawrence",
-            "title": "HANPP Collection: Global Patterns in Human Appropriation of Net Primary Productivity (HANPP)",
-            "graphic-preview-file": "https://sedac.ciesin.columbia.edu/data/set/hanpp-human-appropriation-net-primary-productivity/maps",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The HANPP Collection: Global Patterns in Human Appropriation of Net Primary Productivity (HANPP) represents a digital map of human appropriation of net primary productivity measured in Units of elemental carbon on a one-quarter degree global grid. Net primary productivity (NPP), the net amount of solar energy converted to plant organic matter through photosynthesis, can be measured in Units of elemental carbon and represents the primary food energy source for the world's ecosystems. Humans appropriate net primary productivity through the consumption of food, paper, wood and fiber, which alters the composition of the atmosphere, levels of biodiversity, energy flows within food webs and the provision of important ecosystem services.  The data set is distributed by the Columbia University Center for International Earth Science Information Network (CIESIN).",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.7927%2FH44Q7RWV",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.7927%2FH44Q7RWV",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/downloads/maps/hanpp/hanpp-human-appropriation-net-primary-productivity/human-appropriation-net-primary-productivity-thumbnail.jpg",
-                    "description": "Sample browse graphic of the data set.",
                     "@type": "dcat:Distribution",
+                    "description": "Sample browse graphic of the data set.",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/downloads/maps/hanpp/hanpp-human-appropriation-net-primary-productivity/human-appropriation-net-primary-productivity-thumbnail.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/hanpp-human-appropriation-net-primary-productivity/data-download",
-                    "description": "Data Download Page",
                     "@type": "dcat:Distribution",
+                    "description": "Data Download Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/hanpp-human-appropriation-net-primary-productivity/data-download",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/hanpp-human-appropriation-net-primary-productivity/maps",
-                    "description": "Maps Download Page",
                     "@type": "dcat:Distribution",
+                    "description": "Maps Download Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/hanpp-human-appropriation-net-primary-productivity/maps",
+                    "mediaType": "text/html",
                     "title": "Get a related map visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://sedac.ciesin.columbia.edu/data/set/hanpp-human-appropriation-net-primary-productivity/docs",
-                    "description": "Documentation Page",
                     "@type": "dcat:Distribution",
+                    "description": "Documentation Page",
+                    "downloadURL": "http://sedac.ciesin.columbia.edu/data/set/hanpp-human-appropriation-net-primary-productivity/docs",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/hanpp-human-appropriation-net-primary-productivity",
-                    "description": "Data Set\u00a0Overview Page",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set\u00a0Overview Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/hanpp-human-appropriation-net-primary-productivity",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "graphic-preview-description": "Maps Download Page",
+            "graphic-preview-file": "https://sedac.ciesin.columbia.edu/data/set/hanpp-human-appropriation-net-primary-productivity/maps",
+            "identifier": "C139824016-SEDAC",
+            "issued": "2004-12-31",
+            "keyword": [
+                "earth science",
+                "biosphere",
+                "vegetation"
+            ],
+            "landingPage": "https://doi.org/10.7927/H44Q7RWV",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2004-12-31",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "SEDAC"
+            },
+            "references": [
+                "https://doi.org/10.1038/nature02619",
+                "https://doi.org/10.7927/H48G8HMK",
+                "https://doi.org/10.7927/H40Z715X",
+                "https://doi.org/10.7927/H4W66HPJ"
+            ],
+            "release-place": "Palisades, NY",
             "spatial": "-180.0 -55.0 180.0 90.0",
+            "temporal": "1995-01-01T00:00:00Z/1995-12-31T00:00:00Z",
             "theme": [
                 "HANPP",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "HANPP Collection: Global Patterns in Human Appropriation of Net Primary Productivity (HANPP)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/46",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Norman, J. M. 1994. Leaf Photosynthesis Rates (FIFE). Data set. Available on-line [http://www.daac.ornl.gov] from Oak Ridge National Laboratory Distributed Active Archive Center, Oak Ridge, Tennessee, U.S.A. Also published in D. E. Strebel, D. R. Landis, K. F. Huemmrich, and B. W. Meeson (eds.), Collected Data of the First ISLSCP Field Experiment, Vol. 1: Surface Observations and Non-Image Data Sets. CD-ROM. National Aeronautics and Space Administration, Goddard Space Flight Center, Greenbelt, Maryland, U.S.A. (available from http://www.daac.ornl.gov). doi:10.3334/ORNLDAAC/46",
-            "issued": "2024-05-06",
-            "temporal": "1987-06-06T00:00:00Z/1987-08-16T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-07",
-            "keyword": [
-                "vegetation",
-                "atmosphere",
-                "atmospheric temperature",
-                "atmospheric water vapor",
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
-            "identifier": "C2980098728-ORNL_CLOUD",
             "description": "Measurements of leaf photosynthesis rates measured with Li-Cor LI-6200",
-            "graphic-preview-description": "Browse Image",
-            "title": "Leaf Photosynthesis Rates (FIFE)",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/fife_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F46",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F46",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/fife/fife_biology_pho_leaf/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/fife/fife_biology_pho_leaf/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/FIFE/guides/Leaf_Photosynthesis_Rates.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/FIFE/guides/Leaf_Photosynthesis_Rates.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/46",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/46",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/fife/fife_biology_pho_leaf/comp/Leaf_Photosynthesis_Rates.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/fife/fife_biology_pho_leaf/comp/Leaf_Photosynthesis_Rates.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/msword",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/fife/fife_biology_pho_leaf/comp/pho_leaf.doc",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/fife/fife_biology_pho_leaf/comp/pho_leaf.doc",
+                    "mediaType": "application/msword",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/fife/fife_biology_pho_leaf/comp/pho_leaf.tdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/fife/fife_biology_pho_leaf/comp/pho_leaf.tdf",
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
+            "identifier": "C2980098728-ORNL_CLOUD",
+            "issued": "2024-05-06",
+            "keyword": [
+                "vegetation",
+                "atmosphere",
+                "atmospheric temperature",
+                "atmospheric water vapor",
+                "biosphere",
+                "earth science",
+                "ecological dynamics"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/46",
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
             "spatial": "-96.61 39.07 -96.57 39.1",
+            "temporal": "1987-06-06T00:00:00Z/1987-08-16T23:59:59Z",
             "theme": [
                 "FIFE",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Leaf Photosynthesis Rates (FIFE)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1220567929-USGS_LTA.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "U.S. Geological Survey. 2013-01-01. Global Forest Observations Initiative - Zambia. Archived by National Aeronautics and Space Administration, U.S. Government, U.S. Geological Survey. http://lsiexplorer.cr.usgs.gov.",
-            "issued": "1972-01-01",
-            "temporal": "1972-01-01T00:00:00Z/2022-01-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2019-03-25",
-            "keyword": [
-                "forest science",
-                "agriculture",
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
-            "identifier": "C1220567929-USGS_LTA",
-            "description": "The Global Forest Observations Initiative (GFOI) is an initiative of the inter-governmental Group on Earth Observations (GEO) that aims to:\n\nfoster the sustained availability of observations for national forest monitoring systems; support governments that are establishing national systems by providing a platform for coordinating observations, providing assistance and guidance on utilising observations, developing accepted methods and protocols, and promoting ongoing research and development; and work with national governments that report into international forest assessments (such as the global Forest Resources Assessment (FRA) of the Food and Agriculture Organization, FAO) and the national greenhouse gas inventories reported to the UN Framework Convention on Climate Change (UNFCCC) using methods of the Intergovernmental Panel on Climate Change (IPCC).",
             "creator": "U.S. Geological Survey",
-            "title": "USGS Global Forest Observations Initiative (GFOI) Zambia",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The Global Forest Observations Initiative (GFOI) is an initiative of the inter-governmental Group on Earth Observations (GEO) that aims to:\n\nfoster the sustained availability of observations for national forest monitoring systems; support governments that are establishing national systems by providing a platform for coordinating observations, providing assistance and guidance on utilising observations, developing accepted methods and protocols, and promoting ongoing research and development; and work with national governments that report into international forest assessments (such as the global Forest Resources Assessment (FRA) of the Food and Agriculture Organization, FAO) and the national greenhouse gas inventories reported to the UN Framework Convention on Climate Change (UNFCCC) using methods of the Intergovernmental Panel on Climate Change (IPCC).",
             "distribution": [
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
+            "identifier": "C1220567929-USGS_LTA",
+            "issued": "1972-01-01",
+            "keyword": [
+                "forest science",
+                "agriculture",
+                "earth science"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1220567929-USGS_LTA.html",
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
             "spatial": "22.06547 -18.062311 33.57422 -11.178402",
+            "temporal": "1972-01-01T00:00:00Z/2022-01-17T00:00:00Z",
             "theme": [
                 "CWIC",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "USGS Global Forest Observations Initiative (GFOI) Zambia"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://c3.nasa.gov/dashlink/resources/248/",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "RODNEY MARTIN",
+                "hasEmail": "mailto:rodney.martin@nasa.gov"
+            },
+            "description": "Link to Sharepoint website containing a repository of more detailed internal information for authorized users",
+            "identifier": "DASHLINK_248",
             "issued": "2010-11-04",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
             "keyword": [
                 "dashlink",
                 "ames",
                 "nasa"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "RODNEY MARTIN",
-                "hasEmail": "mailto:rodney.martin@nasa.gov"
-            },
+            "landingPage": "https://c3.nasa.gov/dashlink/resources/248/",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:029"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Dashlink"
             },
-            "identifier": "DASHLINK_248",
-            "description": "Link to Sharepoint website containing a repository of more detailed internal information for authorized users",
-            "title": "Sharepoint Link",
-            "programCode": [
-                "026:029"
-            ],
-            "accrualPeriodicity": "irregular"
+            "title": "Sharepoint Link"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VEGA1-C-TNM-2-RDR-HALLEY-V1.0",
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
-                "vega 1"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "TUNDE-M consists of two particle telescopes: T1 is viewing at 55 deg to the east of the Sun, T2 looks at 90 deg to the east of the Sun, both in the ecliptic plane. The telescopes consist of two circular surface barrier semiconductor detectors with an Al layer of 15x10**-6 g/cm** coated on the front detector (A) and an anticoincidence scintillation detector MCP. Low energy electrons (below about 160 keV) were deflected with a magnet. Field of view (half cone): 25 deg. Geometric factor: 0.25 cm**2 sr. Particles stopping in the thin front detector were not identified (they are referred as ion channels), those reaching the thick detector were identified via the dE/E method.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vega1-c-tnm-2-rdr-halley-v1.0_rgsr-fpmq",
+            "issued": "2018-06-26",
+            "keyword": [
+                "halley",
+                "vega 1"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VEGA1-C-TNM-2-RDR-HALLEY-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vega1-c-tnm-2-rdr-halley-v1.0_rgsr-fpmq",
-            "description": "TUNDE-M consists of two particle telescopes: T1 is viewing at 55 deg to the east of the Sun, T2 looks at 90 deg to the east of the Sun, both in the ecliptic plane. The telescopes consist of two circular surface barrier semiconductor detectors with an Al layer of 15x10**-6 g/cm** coated on the front detector (A) and an anticoincidence scintillation detector MCP. Low energy electrons (below about 160 keV) were deflected with a magnet. Field of view (half cone): 25 deg. Geometric factor: 0.25 cm**2 sr. Particles stopping in the thin front detector were not identified (they are referred as ion channels), those reaching the thick detector were identified via the dE/E method.",
-            "title": "VEGA1 TUNDE-M ENERGETIC PARTICLE ANALYSER DATA V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "VEGA1 TUNDE-M ENERGETIC PARTICLE ANALYSER DATA V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1185",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Morton, D.C., R.S. Defries, and Y.E. Shimabukuro. 2013. LBA-ECO LC-22 Land Cover from MODIS Vegetation Indices, Mato Grosso, Brazil. ORNL DAAC, Oak Ridge, Tennessee, USA. https://doi.org/10.3334/ORNLDAAC/1185",
-            "issued": "2023-10-15",
-            "temporal": "2000-09-01T00:00:00Z/2004-12-31T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-10-17",
-            "keyword": [
-                "national geospatial data asset",
-                "ngda",
-                "land surface",
-                "land use/land cover",
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
-            "identifier": "C2784837251-ORNL_CLOUD",
             "description": "This data set, LBA-ECO LC-22 Land Cover from MODIS Vegetation Indices, Mato Grosso, Brazil,  provides land cover classifications for Mato Grosso, Brazil, for the years 2000-2001 and 2003-2004. The classifications were derived from annual vegetation phenology information from a time series of Collection 4, 16-day MODerate Resolution Imaging Spectroradiometer (MODIS) Normalized Difference Vegetation Index (NDVI), and the Enhanced Vegetation Index (EVI) vegetation data, at 250-m resolution. A decision tree classifier was trained using field observations and Landsat TM data of land cover from 2003-2004 to identify seven land-cover classes. The classifier was applied to the 2000-2001 and 2003-2004 MODIS ENVI and EVI data. There are two GeoTIFF (.tif) files with this data set.",
-            "graphic-preview-description": "Browse Image",
-            "title": "LBA-ECO LC-22 Land Cover from MODIS Vegetation Indices, Mato Grosso, Brazil",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/sdat-tds/1185_1_fit.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1185",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1185",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/lba/land_use_land_cover_change/LC22_MODIS_Phenology_Mato_Grosso/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/lba/land_use_land_cover_change/LC22_MODIS_Phenology_Mato_Grosso/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/LBA/guides/LC22_MODIS_Phenology_Mato_Grosso.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/LBA/guides/LC22_MODIS_Phenology_Mato_Grosso.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1185",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1185",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC22_MODIS_Phenology_Mato_Grosso/comp/LC22_MODIS_Phenology_Mato_Grosso.pdf",
-                    "description": "White paper about this data set.",
                     "@type": "dcat:Distribution",
+                    "description": "White paper about this data set.",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC22_MODIS_Phenology_Mato_Grosso/comp/LC22_MODIS_Phenology_Mato_Grosso.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC22_MODIS_Phenology_Mato_Grosso/comp/morton_mato_grosso_land_cover_chapter_lba_archive.pdf",
-                    "description": "Data set documentation PDF.",
                     "@type": "dcat:Distribution",
+                    "description": "Data set documentation PDF.",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC22_MODIS_Phenology_Mato_Grosso/comp/morton_mato_grosso_land_cover_chapter_lba_archive.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://daac.ornl.gov/graphics/browse/sdat-tds/1185_1_fit.png",
-                    "description": "Browse Image",
                     "@type": "dcat:Distribution",
+                    "description": "Browse Image",
+                    "downloadURL": "https://daac.ornl.gov/graphics/browse/sdat-tds/1185_1_fit.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://webmap.ornl.gov/wcsdown/dataset.jsp?ds_id=1185",
-                    "description": "Web Coverage Service for this collection.",
                     "@type": "dcat:Distribution",
+                    "description": "Web Coverage Service for this collection.",
+                    "downloadURL": "https://webmap.ornl.gov/wcsdown/dataset.jsp?ds_id=1185",
+                    "mediaType": "text/html",
                     "title": "Use Web Coverage Service (WCS) to download the dataset's data"
                 }
             ],
+            "graphic-preview-description": "Browse Image",
+            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/sdat-tds/1185_1_fit.png",
+            "identifier": "C2784837251-ORNL_CLOUD",
+            "issued": "2023-10-15",
+            "keyword": [
+                "national geospatial data asset",
+                "ngda",
+                "land surface",
+                "land use/land cover",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1185",
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
             "spatial": "-60.44 -20.0 -52.32 -6.87",
+            "temporal": "2000-09-01T00:00:00Z/2004-12-31T23:59:59Z",
             "theme": [
                 "LBA-ECO",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "LBA-ECO LC-22 Land Cover from MODIS Vegetation Indices, Mato Grosso, Brazil"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-X-SWAP-2-PLUTOCRUISE-V2.0",
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
-                "new horizons"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This data set contains Raw data taken by the New Horizons                Solar Wind Around Pluto                                                instrument during the                                                    pluto cruise                                                           mission phase.  This is VERSION 2.0 of this data set.                    This is Version 2.0 of this data set and supersedes Version 1.0.  It     contains over 2200 additional observations from late 2010 through        late 2014 not included in Version 1.0; it also renamed some of the       observations from Version 1.0.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-x-swap-2-plutocruise-v2.0_rgvu-ud7m",
+            "issued": "2021-05-21",
+            "keyword": [
+                "new horizons"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-X-SWAP-2-PLUTOCRUISE-V2.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-x-swap-2-plutocruise-v2.0_rgvu-ud7m",
-            "description": "This data set contains Raw data taken by the New Horizons                Solar Wind Around Pluto                                                instrument during the                                                    pluto cruise                                                           mission phase.  This is VERSION 2.0 of this data set.                    This is Version 2.0 of this data set and supersedes Version 1.0.  It     contains over 2200 additional observations from late 2010 through        late 2014 not included in Version 1.0; it also renamed some of the       observations from Version 1.0.",
-            "title": "NEW HORIZONS                            \n      SWAP PLUTO CRUISE                                                       \n      RAW V2.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "NEW HORIZONS                            \n      SWAP PLUTO CRUISE                                                       \n      RAW V2.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/GRGIA-1DJ10",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Tellus. 2019-07-25. TELLUS GRACE Level-3 1.0-degree Glacial Isostatic Adjustment datasets produced by JPL. Version 1.0. TELLUS_GIA_1-Deg_v1.0. JPL. Archived by National Aeronautics and Space Administration, U.S. Government, TELLUS. https://doi.org/10.5067/GRGIA-1DJ10. http://grace.jpl.nasa.gov/data/get-data/gia-trends/. Tellus, TELLUS, 2019-07-25, TELLUS GRACE Level-3 1.0-degree Glacial Isostatic Adjustment v1.0 datasets produced by JPL, http://grace.jpl.nasa.gov/data/get-data/gia-trends/.",
-            "issued": "2019-05-02",
-            "temporal": "1900-01-01T00:00:00Z/2100-12-31T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2019-05-02",
-            "keyword": [
-                "glaciers/ice sheets",
-                "cryosphere",
-                "earth science",
-                "solid earth",
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
-            "identifier": "C2689796219-POCLOUD",
-            "description": "Glacial isostatic adjustment (GIA) is an ongoing geophysical process and is measured by gravimetry satellites like GRACE and GRACE-FO. To isolate signals of contemporary surface mass loss in the cumulative satellite gravimetry measurements, contemporary GIA rates are computed and subtracted from the satellite gravimetry observations. The GIA correction models provided here are filtered such that they are compatible with Level-3 post-processing filters applied to GRACE(-FO) data as indicated in the [product_id]. In this way, user can effectively assess the impact of the applied GIA correction, and substitute different GIA models should that be desired. This GIA dataset is mapped into 1.0-degree global grid in netCDF format.",
-            "release-place": "JPL",
-            "series-name": "TELLUS GRACE Level-3 1.0-degree Glacial Isostatic Adjustment datasets produced by JPL",
-            "graphic-preview-description": "Thumbnail",
             "creator": "Tellus",
-            "title": "TELLUS GRACE Level-3 1.0-degree Glacial Isostatic Adjustment v1.0 datasets produced by JPL",
-            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/TELLUS_GIA_L3_1-DEG_V1.0.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "Glacial isostatic adjustment (GIA) is an ongoing geophysical process and is measured by gravimetry satellites like GRACE and GRACE-FO. To isolate signals of contemporary surface mass loss in the cumulative satellite gravimetry measurements, contemporary GIA rates are computed and subtracted from the satellite gravimetry observations. The GIA correction models provided here are filtered such that they are compatible with Level-3 post-processing filters applied to GRACE(-FO) data as indicated in the [product_id]. In this way, user can effectively assess the impact of the applied GIA correction, and substitute different GIA models should that be desired. This GIA dataset is mapped into 1.0-degree global grid in netCDF format.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGRGIA-1DJ10",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGRGIA-1DJ10",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.1002/2017GL076644",
-                    "description": "GIA model statistics for GRACE hydrology",
                     "@type": "dcat:Distribution",
+                    "description": "GIA model statistics for GRACE hydrology",
+                    "downloadURL": "https://doi.org/10.1002/2017GL076644",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.1002/2016JB013844",
-                    "description": "Comment on the paper by Purcell et al. 2016 entitled An assessment of ICE-6G_C (VM5a) glacial isostatic adjustment model",
                     "@type": "dcat:Distribution",
+                    "description": "Comment on the paper by Purcell et al. 2016 entitled An assessment of ICE-6G_C (VM5a) glacial isostatic adjustment model",
+                    "downloadURL": "https://doi.org/10.1002/2016JB013844",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://grace.jpl.nasa.gov/",
-                    "description": "GRACE Project",
                     "@type": "dcat:Distribution",
+                    "description": "GRACE Project",
+                    "downloadURL": "https://grace.jpl.nasa.gov/",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/TELLUS_GIA_L3_1-DEG_V1.0.jpg",
-                    "description": "Thumbnail",
                     "@type": "dcat:Distribution",
+                    "description": "Thumbnail",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/TELLUS_GIA_L3_1-DEG_V1.0.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
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
-                    "downloadURL": "https://podaac.jpl.nasa.gov/GRACE",
-                    "description": "PODAAC GRACE Mission-Page",
                     "@type": "dcat:Distribution",
+                    "description": "PODAAC GRACE Mission-Page",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/GRACE",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://grace.jpl.nasa.gov/data/get-data/gia-trends/",
-                    "description": "Glacial Isostatic Adjustment (GIA)",
                     "@type": "dcat:Distribution",
+                    "description": "Glacial Isostatic Adjustment (GIA)",
+                    "downloadURL": "https://grace.jpl.nasa.gov/data/get-data/gia-trends/",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.1093/gji/ggs030",
-                    "description": "Computations of the viscoelastic response of a 3-D compressible Earth to surface loading: an application to Glacial Isostatic Adjustment in Antarctica and Canada",
                     "@type": "dcat:Distribution",
+                    "description": "Computations of the viscoelastic response of a 3-D compressible Earth to surface loading: an application to Glacial Isostatic Adjustment in Antarctica and Canada",
+                    "downloadURL": "https://doi.org/10.1093/gji/ggs030",
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
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2689796219-POCLOUD",
-                    "description": "HTTPS endpoint for data browse and download",
                     "@type": "dcat:Distribution",
+                    "description": "HTTPS endpoint for data browse and download",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2689796219-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2689796219-POCLOUD",
-                    "description": "Browse granule search results in Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse granule search results in Earthdata Search",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2689796219-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 }
             ],
+            "graphic-preview-description": "Thumbnail",
+            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/TELLUS_GIA_L3_1-DEG_V1.0.jpg",
+            "identifier": "C2689796219-POCLOUD",
+            "issued": "2019-05-02",
+            "keyword": [
+                "glaciers/ice sheets",
+                "cryosphere",
+                "earth science",
+                "solid earth",
+                "gravity/gravitational field"
+            ],
+            "landingPage": "https://doi.org/10.5067/GRGIA-1DJ10",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2019-05-02",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/JPL/PODAAC"
+            },
+            "release-place": "JPL",
+            "series-name": "TELLUS GRACE Level-3 1.0-degree Glacial Isostatic Adjustment datasets produced by JPL",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "1900-01-01T00:00:00Z/2100-12-31T00:00:00Z",
             "theme": [
                 "GRACE",
                 "GRACE-FO",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "TELLUS GRACE Level-3 1.0-degree Glacial Isostatic Adjustment v1.0 datasets produced by JPL"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG2-N-LECP-4-SUMM-SCAN-24SEC-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "Description of the PDS LECP Neptune Scan data.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg2-n-lecp-4-summ-scan-24sec-v1.0_rgx8-87jq",
             "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "voyager",
                 "neptune",
                 "comet sl9/jupiter collision"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG2-N-LECP-4-SUMM-SCAN-24SEC-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg2-n-lecp-4-summ-scan-24sec-v1.0_rgx8-87jq",
-            "description": "Description of the PDS LECP Neptune Scan data.",
-            "title": "VG2 NEP LECP RESAMPLED SUMMARY SCAN AVERAGED 24SEC V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "VG2 NEP LECP RESAMPLED SUMMARY SCAN AVERAGED 24SEC V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=IHW-C-NNSN-3-EDR-HALLEY-ADDENDA-V1.0",
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
+            "description": "The NEAR NUCLEUS STUDIES Network contains 2204 observations of Comet Halley spanning dates from 11982 Oct 16 through 1989 Apr 12.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ihw-c-nnsn-3-edr-halley-addenda-v1.0_rgyz-3r23",
+            "issued": "2018-06-26",
+            "keyword": [
+                "halley",
+                "international halley watch"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=IHW-C-NNSN-3-EDR-HALLEY-ADDENDA-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ihw-c-nnsn-3-edr-halley-addenda-v1.0_rgyz-3r23",
-            "description": "The NEAR NUCLEUS STUDIES Network contains 2204 observations of Comet Halley spanning dates from 11982 Oct 16 through 1989 Apr 12.",
-            "title": "COMET HALLEY ARCHIVE - NEAR NUCLEUS IMAGE DATA",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "COMET HALLEY ARCHIVE - NEAR NUCLEUS IMAGE DATA"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=IHW-C-IRPOL-3-RDR-HALLEY-V1.0",
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
+            "description": "NASA's International Halley Watch (IHW) has created a Comet Halley Archive. The collection of data spans the full wavelength range as submitted by scientists to the IHW. The observations belong to one of the following Disciplines: Amateur, Astrometry, Infrared Studies, Large-Scale Phenomena, Meteor Studies, Near-Nucleus Studies, Photometry and Polarimetry, Radio Studies, and Spectroscopy and Spectrophotometry. The data collected by these nine disciplines were augmented by Spacecraft measurements. The data were submitted to IHW, but the evaluation and selection for the Archive has been the primary responsibility of the Discipline Specialist Teams for each network in cooperation with the Lead Center. The data from the Infrared Polarimetry subnetwork contains 137 observations spanning dates from 1985 September 16 through 1986 June 1.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ihw-c-irpol-3-rdr-halley-v1.0_rgzy-pmdw",
+            "issued": "2021-05-21",
+            "keyword": [
+                "halley",
+                "international halley watch"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=IHW-C-IRPOL-3-RDR-HALLEY-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ihw-c-irpol-3-rdr-halley-v1.0_rgzy-pmdw",
-            "description": "NASA's International Halley Watch (IHW) has created a Comet Halley Archive. The collection of data spans the full wavelength range as submitted by scientists to the IHW. The observations belong to one of the following Disciplines: Amateur, Astrometry, Infrared Studies, Large-Scale Phenomena, Meteor Studies, Near-Nucleus Studies, Photometry and Polarimetry, Radio Studies, and Spectroscopy and Spectrophotometry. The data collected by these nine disciplines were augmented by Spacecraft measurements. The data were submitted to IHW, but the evaluation and selection for the Archive has been the primary responsibility of the Discipline Specialist Teams for each network in cooperation with the Lead Center. The data from the Infrared Polarimetry subnetwork contains 137 observations spanning dates from 1985 September 16 through 1986 June 1.",
-            "title": "IHW COMET HALLEY INFRARED POLARIMETRY V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "IHW COMET HALLEY INFRARED POLARIMETRY V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1000000040-CDDIS.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/GSFC/SED/ESD/GGL/CDDIS.",
-            "issued": "1982-01-01",
-            "temporal": "1982-01-01T00:00:00Z/2022-01-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2012-06-14",
-            "keyword": [
-                "nasa"
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
-            "identifier": "C1000000040-CDDIS",
             "description": "Miscellaneous documentation, information, and ancillary data to be used with GNSS, laser ranging, VLBI and DORIS data and analyzed products available through the CDDIS.",
-            "title": "CDDIS_MISC_information",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -1306147,307 +1306130,301 @@
                     "title": "Download this dataset"
                 }
             ],
-            "theme": [
-                "geospatial"
+            "identifier": "C1000000040-CDDIS",
+            "issued": "1982-01-01",
+            "keyword": [
+                "nasa"
             ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1000000040-CDDIS.html",
             "language": [
                 "en-US"
-            ]
+            ],
+            "modified": "2012-06-14",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GGL/CDDIS"
+            },
+            "temporal": "1982-01-01T00:00:00Z/2022-01-17T00:00:00Z",
+            "theme": [
+                "geospatial"
+            ],
+            "title": "CDDIS_MISC_information"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-PRL-0351-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the PRELANDING phase 2014-01-21 to 2014-11-18. It is a Global Gravity measurement at the comet 67P and covers the time 2014-10-12T03:13:11.000 to 2014-10-12T08:18:56.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-prl-0351-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-PRL-0351-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-prl-0351-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the PRELANDING phase 2014-01-21 to 2014-11-18. It is a Global Gravity measurement at the comet 67P and covers the time 2014-10-12T03:13:11.000 to 2014-10-12T08:18:56.000.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     PRELANDING 0351 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     PRELANDING 0351 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-J-REX-2-JUPITER-V2.0",
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
-                "jupiter"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This data set contains Raw data taken by the New Horizons Radio Science Experiment instrument during the Jupiter encounter mission phase.  This is VERSION 2.0 of this data set. The REX datasets over the mission include calibrations using known radio sources, Jupiter, and cold sky measurements; operational readiness tests (ORTs); internal test pattern calibration; and prime science radiometry and occultation observations during the Pluto Encounter.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-j-rex-2-jupiter-v2.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "new horizons",
+                "jupiter"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-J-REX-2-JUPITER-V2.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-j-rex-2-jupiter-v2.0",
-            "description": "This data set contains Raw data taken by the New Horizons Radio Science Experiment instrument during the Jupiter encounter mission phase.  This is VERSION 2.0 of this data set. The REX datasets over the mission include calibrations using known radio sources, Jupiter, and cold sky measurements; operational readiness tests (ORTs); internal test pattern calibration; and prime science radiometry and occultation observations during the Pluto Encounter.",
-            "title": "NEW HORIZONS\n      REX JUPITER ENCOUNTER\n      RAW V2.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "NEW HORIZONS\n      REX JUPITER ENCOUNTER\n      RAW V2.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MRO-M-ACCEL-5-PROFILE-V1.0",
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
-                "mars reconnaissance orbiter",
-                "mars"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "TBD",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mro-m-accel-5-profile-v1.0_rh5z-e2zk",
+            "issued": "2018-06-26",
+            "keyword": [
+                "mars reconnaissance orbiter",
+                "mars"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MRO-M-ACCEL-5-PROFILE-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mro-m-accel-5-profile-v1.0_rh5z-e2zk",
-            "description": "TBD",
-            "title": "MRO PROFILE DATA RECORDS V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "MRO PROFILE DATA RECORDS V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-2-ESC4-67PCHURYUMOV-M22-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This data set contains images acquired by the OSIRIS Narrow Angle Camera during the COMET ESCORT 4 phase of the Rosetta mission at the comet 67P, covering the period from 2015-10-20T23:25:00.000 to 2015-11-17T23:24:59.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-2-esc4-67pchuryumov-m22-v1.0",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2021-05-21",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "dark",
                 "bias",
                 "international rosetta mission",
                 "67p/churyumov-gerasimenko 1 (1969 r1)"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-2-ESC4-67PCHURYUMOV-M22-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-2-esc4-67pchuryumov-m22-v1.0",
-            "description": "This data set contains images acquired by the OSIRIS Narrow Angle Camera during the COMET ESCORT 4 phase of the Rosetta mission at the comet 67P, covering the period from 2015-10-20T23:25:00.000 to 2015-11-17T23:24:59.000.",
-            "title": "ROSETTA-ORBITER COMET ESCORT 4 OSINAC 2 EDR MTP022 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER COMET ESCORT 4 OSINAC 2 EDR MTP022 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC4-1133-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 4 phase 2015-10-22 to 2015-12-31. It is a Global Gravity measurement at the comet 67P and covers the time 2015-10-27T10:24:15.000 to 2015-10-27T14:11:30.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc4-1133-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC4-1133-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc4-1133-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 4 phase 2015-10-22 to 2015-12-31. It is a Global Gravity measurement at the comet 67P and covers the time 2015-10-27T10:24:15.000 to 2015-10-27T14:11:30.000.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 4 1133 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 4 1133 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewBundle.jsp?identifier=urn%3Anasa%3Apds%3Asystem_bundle&version=1.0",
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
-                "pds"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This Bundle includes all Collections relevant to the PDS4 System Bundle.",
+            "identifier": "urn:nasa:pds:system_bundle",
+            "issued": "2021-05-21",
+            "keyword": [
+                "pds"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewBundle.jsp?identifier=urn%3Anasa%3Apds%3Asystem_bundle&version=1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:system_bundle",
-            "description": "This Bundle includes all Collections relevant to the PDS4 System Bundle.",
-            "title": "PDS4 System Bundle",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "PDS4 System Bundle"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-4-EXT3-67P-M35-INFLDSTR-V1.0",
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
+            "description": "This CODMAC level 4 data set contains solar stray-light corrected, in-field stray-light corrected,  radiometric calibrated and geometric distortion corrected  (resampled) image data in W/m^2/sr/nm,  acquired by the OSIRIS Wide Angle Camera on the Rosetta spacecraft  during the ROSETTA EXTENSION 3 mission phase, covering the period  from 2016-09-26T06:40:00.000 to 2016-10-01T00:00:00.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V1.0 is the first version of this dataset: Lien corrected dataset after September 2019 PSA/PDS external peer review.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-4-ext3-67p-m35-infldstr-v1.0_rh7q-2yb2",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-4-EXT3-67P-M35-INFLDSTR-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-4-ext3-67p-m35-infldstr-v1.0_rh7q-2yb2",
-            "description": "This CODMAC level 4 data set contains solar stray-light corrected, in-field stray-light corrected,  radiometric calibrated and geometric distortion corrected  (resampled) image data in W/m^2/sr/nm,  acquired by the OSIRIS Wide Angle Camera on the Rosetta spacecraft  during the ROSETTA EXTENSION 3 mission phase, covering the period  from 2016-09-26T06:40:00.000 to 2016-10-01T00:00:00.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V1.0 is the first version of this dataset: Lien corrected dataset after September 2019 PSA/PDS external peer review.",
-            "title": "ROSETTA-ORBITER 67P OSIWAC 4 EXT3-MTP035 RDR-INFLDSTR V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P OSIWAC 4 EXT3-MTP035 RDR-INFLDSTR V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://nasa3d.arc.nasa.gov/detail/slic",
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
-                "3d model",
-                "space shuttle",
-                "super lightweight interchangeable",
-                "carrier",
-                "shuttle"
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
-            "identifier": "NASA-408",
             "description": "Polygons: 3867 Vertices: 5444",
-            "title": "NASA 3D Models: Super Lightweight Interchangeable",
-            "programCode": [
-                "026:045",
-                "026:046"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -1306455,464 +1306432,463 @@
                     "mediaType": "image/x-3ds"
                 }
             ],
-            "accrualPeriodicity": "irregular",
+            "identifier": "NASA-408",
+            "issued": "2018-06-25",
+            "keyword": [
+                "3d model",
+                "space shuttle",
+                "super lightweight interchangeable",
+                "carrier",
+                "shuttle"
+            ],
+            "landingPage": "http://nasa3d.arc.nasa.gov/detail/slic",
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
+            "title": "NASA 3D Models: Super Lightweight Interchangeable"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC4-1299-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 4 phase 2015-10-22 to 2015-12-31. It is a Global Gravity measurement at the comet 67P and covers the time 2015-12-30T07:36:40.000 to 2015-12-30T15:08:25.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc4-1299-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC4-1299-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc4-1299-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 4 phase 2015-10-22 to 2015-12-31. It is a Global Gravity measurement at the comet 67P and covers the time 2015-12-30T07:36:40.000 to 2015-12-30T15:08:25.000.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 4 1299 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 4 1299 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/AQR50-3YQCE",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "NASA Aquarius project. 2017-12-07. Aquarius Official Release Level 3 Rain-flagged Sea Surface Salinity Standard Mapped Image 7-Day Running Mean Data. Version 5.0. Aquarius Sea Surface Salinity Products. Goddard Space Flight Center, 8800 Greenbelt Rd.; Greeenbelt, MD., 20771, USA. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/GSFC OBPG. https://doi.org/10.5067/AQR50-3YQCE. http://podaac.jpl.nasa.gov/SeaSurfaceSalinity/Aquarius. NASA Aquarius project, NASA/GSFC OBPG, 2017-12-07, Aquarius Official Release Level 3 Rain-flagged Sea Surface Salinity Standard Mapped Image 7-Day Running Mean Data V5.0, http://podaac.jpl.nasa.gov/SeaSurfaceSalinity/Aquarius.",
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
-            "identifier": "C2491756798-POCLOUD",
-            "description": "Aquarius Level 3 sea surface salinity (SSS) rain-flagged standard mapped image data contains gridded 1 degree spatial resolution SSS averaged\nover daily, 7 day, monthly, and seasonal time scales. This particular data set is the 7-Day running mean rain-flagged rain-flagged sea surface salinity product for version 5.0 of the Aquarius data set. The Aquarius instrument is onboard the AQUARIUS/SAC-D satellite, a collaborative effort between NASA and the Argentinian Space Agency Comision Nacional de Actividades Espaciales (CONAE). The instrument consists of three radiometers in push broom alignment at incidence angles of 29, 38, and 46 degrees incidence angles relative to the shadow side of the orbit.  Footprints for the beams are: 76 km (along-track) x 94 km (cross-track), 84 km x 120 km and 96km x 156 km, yielding a total cross-track swath of 370 km. The radiometers measure brightness temperature at 1.413 GHz in their respective horizontal and vertical polarizations (TH and TV). A scatterometer operating at 1.26 GHz measures ocean backscatter in each footprint that is used for surface roughness corrections in the estimation of salinity. The scatterometer has an approximate 390km swath.",
-            "release-place": "Goddard Space Flight Center, 8800 Greenbelt Rd.; Greeenbelt, MD., 20771, USA",
-            "series-name": "Aquarius Official Release Level 3 Rain-flagged Sea Surface Salinity Standard Mapped Image 7-Day Running Mean Data",
-            "graphic-preview-description": "Thumbnail",
             "creator": "NASA Aquarius project",
-            "title": "Aquarius Official Release Level 3 Rain-flagged Sea Surface Salinity Standard Mapped Image 7-Day Running Mean Data V5.0",
-            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/AQUARIUS_L3_SSS-RainFlagged_SMI_7DAY-RUNNINGMEAN_V5.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "Aquarius Level 3 sea surface salinity (SSS) rain-flagged standard mapped image data contains gridded 1 degree spatial resolution SSS averaged\nover daily, 7 day, monthly, and seasonal time scales. This particular data set is the 7-Day running mean rain-flagged rain-flagged sea surface salinity product for version 5.0 of the Aquarius data set. The Aquarius instrument is onboard the AQUARIUS/SAC-D satellite, a collaborative effort between NASA and the Argentinian Space Agency Comision Nacional de Actividades Espaciales (CONAE). The instrument consists of three radiometers in push broom alignment at incidence angles of 29, 38, and 46 degrees incidence angles relative to the shadow side of the orbit.  Footprints for the beams are: 76 km (along-track) x 94 km (cross-track), 84 km x 120 km and 96km x 156 km, yielding a total cross-track swath of 370 km. The radiometers measure brightness temperature at 1.413 GHz in their respective horizontal and vertical polarizations (TH and TV). A scatterometer operating at 1.26 GHz measures ocean backscatter in each footprint that is used for surface roughness corrections in the estimation of salinity. The scatterometer has an approximate 390km swath.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAQR50-3YQCE",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAQR50-3YQCE",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
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
-                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/AQUARIUS_L3_SSS-RainFlagged_SMI_7DAY-RUNNINGMEAN_V5.jpg",
-                    "description": "Thumbnail",
                     "@type": "dcat:Distribution",
+                    "description": "Thumbnail",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/AQUARIUS_L3_SSS-RainFlagged_SMI_7DAY-RUNNINGMEAN_V5.jpg",
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
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2491756798-POCLOUD",
-                    "description": "HTTPS endpoint for data browse and download",
                     "@type": "dcat:Distribution",
+                    "description": "HTTPS endpoint for data browse and download",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2491756798-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2491756798-POCLOUD",
-                    "description": "Browse granule search results in Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse granule search results in Earthdata Search",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2491756798-POCLOUD",
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
+            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/AQUARIUS_L3_SSS-RainFlagged_SMI_7DAY-RUNNINGMEAN_V5.jpg",
+            "identifier": "C2491756798-POCLOUD",
+            "issued": "2017-10-21",
+            "keyword": [
+                "oceans",
+                "earth science",
+                "salinity/density"
+            ],
+            "landingPage": "https://doi.org/10.5067/AQR50-3YQCE",
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
+            "series-name": "Aquarius Official Release Level 3 Rain-flagged Sea Surface Salinity Standard Mapped Image 7-Day Running Mean Data",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2011-08-25T01:45:23Z/2015-06-07T12:45:21Z",
             "theme": [
                 "AQUARIUS SAC-D",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Aquarius Official Release Level 3 Rain-flagged Sea Surface Salinity Standard Mapped Image 7-Day Running Mean Data V5.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/CAMEX-3/HYGROMETER/DATA201",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "May, Randy D.1999. CAMEX-3 JPL LASER HYGROMETER [indicate subset used]. Dataset available online from the NASA Global Hydrometeorology Resource Center DAAC, Huntsville, Alabama, U.S.A. DOI: http://dx.doi.org/10.5067/CAMEX-3/HYGROMETER/DATA201",
-            "issued": "1999-06-10",
-            "temporal": "1998-08-15T20:19:04Z/1998-09-23T01:24:07Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-05-18",
-            "keyword": [
-                "atmosphere",
-                "earth science",
-                "atmospheric water vapor"
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
-            "identifier": "C1979110870-GHRC_DAAC",
             "description": "The CAMEX-3 Jet Propulsion Laboratory (JPL) Laser Hygrometer datasets consists of timeline measurements of water vapor content colllected during DC-8 flights flown during August and September of 1998. The JPL Laser Hygrometer acquired in situ measurments of the free airstream beyond the boundary layer within the immediate proximity of the aircraft along the flight track.",
-            "title": "CAMEX-3 JPL LASER HYGROMETER V1",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FCAMEX-3%2FHYGROMETER%2FDATA201",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FCAMEX-3%2FHYGROMETER%2FDATA201",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=dc8laserh",
-                    "description": "Files may be downloaded directly to your workstation from this link",
                     "@type": "dcat:Distribution",
+                    "description": "Files may be downloaded directly to your workstation from this link",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=dc8laserh",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://ghrc.nsstc.nasa.gov/uso/ds_docs/camex3/dc8laserh/dc8laserh_dataset.html",
-                    "description": "The guide document contains detailed information about the dataset",
                     "@type": "dcat:Distribution",
+                    "description": "The guide document contains detailed information about the dataset",
+                    "downloadURL": "http://ghrc.nsstc.nasa.gov/uso/ds_docs/camex3/dc8laserh/dc8laserh_dataset.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/home/field-campaigns/CAMEX3",
-                    "description": "The home page for the project or program which sponsored the dataset",
                     "@type": "dcat:Distribution",
+                    "description": "The home page for the project or program which sponsored the dataset",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/home/field-campaigns/CAMEX3",
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
+            "identifier": "C1979110870-GHRC_DAAC",
+            "issued": "1999-06-10",
+            "keyword": [
+                "atmosphere",
+                "earth science",
+                "atmospheric water vapor"
+            ],
+            "landingPage": "https://doi.org/10.5067/CAMEX-3/HYGROMETER/DATA201",
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
             "spatial": "-86.165 14.045 -62.96 39.0333",
+            "temporal": "1998-08-15T20:19:04Z/1998-09-23T01:24:07Z",
             "theme": [
                 "CAMEX-3",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "CAMEX-3 JPL LASER HYGROMETER V1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-3-ESC1-67PCHURYUMOV-M12-V1.0",
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
+            "description": "This data set contains calibrated images acquired by the OSIRIS Wide Angle\nCamera during the escort phase of the Rosetta mission at the comet 67P,\ncovering the period from 2015-01-13 to 2015-02-10.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-3-esc1-67pchuryumov-m12-v1.0_rhct-dfvd",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-3-ESC1-67PCHURYUMOV-M12-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-3-esc1-67pchuryumov-m12-v1.0_rhct-dfvd",
-            "description": "This data set contains calibrated images acquired by the OSIRIS Wide Angle\nCamera during the escort phase of the Rosetta mission at the comet 67P,\ncovering the period from 2015-01-13 to 2015-02-10.",
-            "title": "ROSETTA-ORBITER COMET ESCORT OSIWAC 3 RDR MTP 012 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER COMET ESCORT OSIWAC 3 RDR MTP 012 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C2237419212-GES_DISC.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "OCO-2 Science Team/Michael Gunson, Annmarie Eldering. 2022-03-01. OCO2_L1aIn_Pixel. Version 11. OCO-2 Level 1A collated, parsed, calibration data V11. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://disc.gsfc.nasa.gov/datacollection/OCO2_L1aIn_Pixel_11.html. Digital Science Data.",
-            "issued": "2022-03-01",
-            "temporal": "2019-11-30T00:00:00Z/2023-03-01T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-03-01",
-            "keyword": [
-                "atmosphere",
-                "atmospheric chemistry",
-                "spectral/engineering",
-                "infrared wavelengths",
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
-            "identifier": "C2237419212-GES_DISC",
-            "description": "Version 11 is the current version of the data set. Older versions will no longer be available and are superseded by Version 11.\n\nThe Orbiting Carbon Observatory is the first NASA mission designed to collect space-based measurements of atmospheric carbon dioxide with the precision, resolution, and coverage needed to characterize the processes controlling its buildup in the atmosphere. The OCO-2 project uses the LEOStar-2 spacecraft that carries a single instrument. It incorporates three high-resolution spectrometers that make coincident measurements of reflected sunlight in the near-infrared CO2 near 1.61 and 2.06 micrometers and in molecular oxygen (O2) A-Band at 0.76 micrometers. The three spectrometers have different characteristics and are calibrated independently. Their raw data numbers (DN) are delivered correlated in time to the Level 1B process as Level 1A products. Each band has 1016 spectral elements, although some are masked out in the L2 retrieval.This product is the input to the Level 1B process. It is depacketized raw data formatted into a standard granularity with calibrated engineering data (for both science and calibration observations), in the Single-pixel Mode of operation.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "OCO2_L1aIn_Pixel",
             "creator": "OCO-2 Science Team/Michael Gunson, Annmarie Eldering",
-            "title": "OCO-2 Level 1A collated, parsed, calibration data V11 (OCO2_L1aIn_Pixel) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/OCO/OCO2_logo.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "data-presentation-form": "Digital Science Data",
+            "description": "Version 11 is the current version of the data set. Older versions will no longer be available and are superseded by Version 11.\n\nThe Orbiting Carbon Observatory is the first NASA mission designed to collect space-based measurements of atmospheric carbon dioxide with the precision, resolution, and coverage needed to characterize the processes controlling its buildup in the atmosphere. The OCO-2 project uses the LEOStar-2 spacecraft that carries a single instrument. It incorporates three high-resolution spectrometers that make coincident measurements of reflected sunlight in the near-infrared CO2 near 1.61 and 2.06 micrometers and in molecular oxygen (O2) A-Band at 0.76 micrometers. The three spectrometers have different characteristics and are calibrated independently. Their raw data numbers (DN) are delivered correlated in time to the Level 1B process as Level 1A products. Each band has 1016 spectral elements, although some are masked out in the L2 retrieval.This product is the input to the Level 1B process. It is depacketized raw data formatted into a standard granularity with calibrated engineering data (for both science and calibration observations), in the Single-pixel Mode of operation.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -1306921,646 +1306897,682 @@
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/OCO2_L1aIn_Pixel_11.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/OCO2_L1aIn_Pixel_11.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=OCO2_L1aIn_Pixel",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=OCO2_L1aIn_Pixel",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://oco2.gesdisc.eosdis.nasa.gov/opendap/OCO2_L1aIn_Pixel.11/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://oco2.gesdisc.eosdis.nasa.gov/opendap/OCO2_L1aIn_Pixel.11/contents.html",
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
-                    "downloadURL": "https://oco2.gesdisc.eosdis.nasa.gov/data/OCO2_DATA/OCO2_L1aIn_Pixel.11/",
-                    "description": "Access the data via HTTP.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTP.",
+                    "downloadURL": "https://oco2.gesdisc.eosdis.nasa.gov/data/OCO2_DATA/OCO2_L1aIn_Pixel.11/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/OCO/SDOS_SIS_L1aIn.V7.pdf",
-                    "description": "Level 1A Software Interfase Specification.",
                     "@type": "dcat:Distribution",
+                    "description": "Level 1A Software Interfase Specification.",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/OCO/SDOS_SIS_L1aIn.V7.pdf",
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
-                    "downloadURL": "https://disc.gsfc.nasa.gov/information/howto?title=How+to+download+a+spatial+and+variable+subset+of+Level+1B+data+using+OPeNDAP",
-                    "description": "Subset recipe using OPeNDAP",
                     "@type": "dcat:Distribution",
+                    "description": "Subset recipe using OPeNDAP",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/information/howto?title=How+to+download+a+spatial+and+variable+subset+of+Level+1B+data+using+OPeNDAP",
+                    "mediaType": "text/html",
                     "title": "View this dataset's how-to documentation"
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
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/OCO/OCO2_logo.jpg",
+            "identifier": "C2237419212-GES_DISC",
+            "issued": "2022-03-01",
+            "keyword": [
+                "atmosphere",
+                "atmospheric chemistry",
+                "spectral/engineering",
+                "infrared wavelengths",
+                "earth science"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C2237419212-GES_DISC.html",
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
+            "series-name": "OCO2_L1aIn_Pixel",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2019-11-30T00:00:00Z/2023-03-01T00:00:00Z",
             "theme": [
                 "OCO-2",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "OCO-2 Level 1A collated, parsed, calibration data V11 (OCO2_L1aIn_Pixel) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/2304",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Donatelli, C., L. Cortese, and S. Fagherazzi. 2023. Delta-X: Delft3D Sediment Model, Site 421, Terrebonne Basin, MRD, Louisiana, USA. ORNL DAAC, Oak Ridge, Tennessee, USA. https://doi.org/10.3334/ORNLDAAC/2304",
-            "issued": "2024-02-02",
-            "temporal": "2021-03-25T00:00:00Z/2021-08-28T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-02-08",
-            "keyword": [
-                "surface water",
-                "geomorphic landforms/processes",
-                "solid earth",
-                "water quality/water chemistry",
-                "biosphere",
-                "terrestrial hydrosphere",
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
-            "identifier": "C2857068056-ORNL_CLOUD",
             "description": "This dataset contains the Delft3D model of the intensive site 421 in the Terrebonne Basin along the Mississippi River Delta (MRD) in coastal Louisiana. Simulations cover the Delta-X Spring and Fall deployments in 2021 and include hydrodynamics and sediment transport. All files required to run the simulations are included. The model's output of water velocity and depth-averaged sediment concentrations are provided for both deployments. The dataset includes annual inorganic mass accumulation rates derived through modelling intra-annual variability in water levels and suspended sediment concentrations. The data are provided in netCDF format.",
-            "graphic-preview-description": "Satellite image of Terrebonne Bay, Louisiana, USA with location of Site 421. Inset shows bathymetry of this intensive site.",
-            "title": "Delta-X: Delft3D Sediment Model, Site 421, Terrebonne Basin, MRD, Louisiana, USA",
-            "graphic-preview-file": "https://daac.ornl.gov/DELTAX/guides/DeltaX_Delft3D_421_Terrebonne_Fig1.jpg",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F2304",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F2304",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/deltax/DeltaX_Delft3D_421_Terrebonne/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/deltax/DeltaX_Delft3D_421_Terrebonne/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/DELTAX/guides/DeltaX_Delft3D_421_Terrebonne.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/DELTAX/guides/DeltaX_Delft3D_421_Terrebonne.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/2304",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/2304",
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
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/deltax/DeltaX_Delft3D_421_Terrebonne/comp/DeltaX_Delft3D_421_Terrebonne.pdf",
-                    "description": "Delta-X: Delft3D Sediment Model, Site 421, Terrebonne Basin, MRD, Louisiana, USA: DeltaX_Delft3D_421_Terrebonne.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "Delta-X: Delft3D Sediment Model, Site 421, Terrebonne Basin, MRD, Louisiana, USA: DeltaX_Delft3D_421_Terrebonne.pdf",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/deltax/DeltaX_Delft3D_421_Terrebonne/comp/DeltaX_Delft3D_421_Terrebonne.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://daac.ornl.gov/DELTAX/guides/DeltaX_Delft3D_421_Terrebonne_Fig1.jpg",
-                    "description": "Satellite image of Terrebonne Bay, Louisiana, USA with location of Site 421. Inset shows bathymetry of this intensive site.",
                     "@type": "dcat:Distribution",
+                    "description": "Satellite image of Terrebonne Bay, Louisiana, USA with location of Site 421. Inset shows bathymetry of this intensive site.",
+                    "downloadURL": "https://daac.ornl.gov/DELTAX/guides/DeltaX_Delft3D_421_Terrebonne_Fig1.jpg",
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
+            "graphic-preview-description": "Satellite image of Terrebonne Bay, Louisiana, USA with location of Site 421. Inset shows bathymetry of this intensive site.",
+            "graphic-preview-file": "https://daac.ornl.gov/DELTAX/guides/DeltaX_Delft3D_421_Terrebonne_Fig1.jpg",
+            "identifier": "C2857068056-ORNL_CLOUD",
+            "issued": "2024-02-02",
+            "keyword": [
+                "surface water",
+                "geomorphic landforms/processes",
+                "solid earth",
+                "water quality/water chemistry",
+                "biosphere",
+                "terrestrial hydrosphere",
+                "earth science",
+                "ecosystems"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/2304",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2024-02-08",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "ORNL_DAAC"
+            },
             "spatial": "-90.84 29.15 -90.8 29.2",
+            "temporal": "2021-03-25T00:00:00Z/2021-08-28T23:59:59Z",
             "theme": [
                 "Delta-X",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Delta-X: Delft3D Sediment Model, Site 421, Terrebonne Basin, MRD, Louisiana, USA"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/2194",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Casta\u00f1eda-Moya, E., and E. Solohin. 2023. Delta-X: Foliar Stable Isotopes, MRD, LA, USA, 2021. ORNL DAAC, Oak Ridge, Tennessee, USA. https://doi.org/10.3334/ORNLDAAC/2194",
-            "issued": "2023-09-15",
-            "temporal": "2021-08-19T00:00:00Z/2021-08-27T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-09-19",
-            "keyword": [
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
-            "identifier": "C2769434781-ORNL_CLOUD",
             "description": "This dataset contains foliar tissue C and N bulk isotopic signatures (delta 13C, delta 15N) of dominant wetland herbaceous species collected at six sites in the Atchafalaya (N = 3) and Terrebonne (N = 3) basins in coastal Louisiana. Five of the sites are from the Coastwide Reference Monitoring System (CRMS) and one site is the Mike Island Site in the Wax Lake Delta (WLD). For the herbaceous wetland sites, Aboveground biomass (AGB) was harvested inside duplicate plots (0.25 m2), located 5 m apart at each sampling station. All plant material within each plot was clipped at soil level, stored in plastic bags, and transported to the laboratory for further analyses. In the lab, plant tissue (foliar) C and N bulk isotopic signatures were analyzed for two dominant plant species from each site using a Thermo Scientific Delta V Plus CF-IRMS coupled to a Carlo-Erba 1108 elemental analyzer via a ConFlo IV interface (Thermo Fisher Scientific, Waltham, MA, USA). The data were collected during 2021-08-19 to 2021-08-27 during the Delta-X Fall 2021 deployment.",
-            "graphic-preview-description": "Sampling of aboveground biomass herbaceous vegetation using a 0.25 square meter quadrat.",
-            "title": "Delta-X: Foliar Stable Isotopes, MRD, LA, USA, 2021",
-            "graphic-preview-file": "https://daac.ornl.gov/DELTAX/guides/DeltaX_Foliar_Stable_Isotopes_Fig1.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F2194",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F2194",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/deltax/DeltaX_Foliar_Stable_Isotopes/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/deltax/DeltaX_Foliar_Stable_Isotopes/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/DELTAX/guides/DeltaX_Foliar_Stable_Isotopes.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/DELTAX/guides/DeltaX_Foliar_Stable_Isotopes.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/2194",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/2194",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/deltax/DeltaX_Foliar_Stable_Isotopes/comp/DeltaX_Foliar_Stable_Isotopes.pdf",
-                    "description": "Delta-X: Foliar Stable Isotopes, MRD, LA, USA, 2021: DeltaX_Foliar_Stable_Isotopes.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "Delta-X: Foliar Stable Isotopes, MRD, LA, USA, 2021: DeltaX_Foliar_Stable_Isotopes.pdf",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/deltax/DeltaX_Foliar_Stable_Isotopes/comp/DeltaX_Foliar_Stable_Isotopes.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://daac.ornl.gov/DELTAX/guides/DeltaX_Foliar_Stable_Isotopes_Fig1.png",
-                    "description": "Sampling of aboveground biomass herbaceous vegetation using a 0.25 square meter quadrat.",
                     "@type": "dcat:Distribution",
+                    "description": "Sampling of aboveground biomass herbaceous vegetation using a 0.25 square meter quadrat.",
+                    "downloadURL": "https://daac.ornl.gov/DELTAX/guides/DeltaX_Foliar_Stable_Isotopes_Fig1.png",
+                    "mediaType": "image/png",
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
+            "graphic-preview-description": "Sampling of aboveground biomass herbaceous vegetation using a 0.25 square meter quadrat.",
+            "graphic-preview-file": "https://daac.ornl.gov/DELTAX/guides/DeltaX_Foliar_Stable_Isotopes_Fig1.png",
+            "identifier": "C2769434781-ORNL_CLOUD",
+            "issued": "2023-09-15",
+            "keyword": [
+                "earth science",
+                "biosphere",
+                "vegetation"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/2194",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2023-09-19",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "ORNL_DAAC"
+            },
             "spatial": "-91.89 29.17 -90.82 29.51",
+            "temporal": "2021-08-19T00:00:00Z/2021-08-27T23:59:59Z",
             "theme": [
                 "Delta-X",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Delta-X: Foliar Stable Isotopes, MRD, LA, USA, 2021"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/5X25TK595WAF",
             "citation": "Kevin W. Bowman. 2022-04-04. TRPSYL2HDOCRSFS. Version 1. TROPESS CrIS-SNPP L2 Deuterated Water Vapor for Forward Stream, Summary Product V1. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/5X25TK595WAF. https://disc.gsfc.nasa.gov/datacollection/TRPSYL2HDOCRSFS_1.html. Digital Science Data.",
-            "issued": "2022-04-01",
-            "temporal": "2021-02-01T00:00:00Z/2021-05-21T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-04-01",
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
-                "atmospheric chemistry",
-                "earth science"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "KEVIN BOWMAN",
                 "hasEmail": "mailto:kevin.w.bowman@jpl.nasa.gov"
             },
+            "creator": "Kevin W. Bowman",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C2247040372-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "The TROPESS CrIS-SNPP L2 Deuterated Water Vapor for Forward Stream, Summary Product contains the vertical distribution of the retrieved atmospheric state of semi-heavy water (HDO),  and formal uncertainties measured by the CrIS instrument on the Suomi-NPP satellite. The forward stream standard product is global for the time period from 2021-02-01 to 2021-05-21, when the CrIS-SNPP processing was discontinued. The NASA TRopospheric Ozone and Precursors from Earth System Sounding (TROPESS) project, uses an optimal estimation algorithm, known as the MUlti-SpEctra, MUlti-SpEcies, Multi-SEnsors (MUSES).\n\nThe data files are written in the netCDF version 4 file format, and each file contains one day of data. The data have a spatial resolution of 14 km (CrIS nadir FOV), and are reported at 17 vertical levels from the surface to 0.1 hPa. The principal investigator for the TROPESS project is Kevin W. Bowman.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "TRPSYL2HDOCRSFS",
-            "creator": "Kevin W. Bowman",
-            "graphic-preview-description": "TROPESS CrIS-SNPP HDO (Forward Stream, Summary Product) at 681 hPa on 01 April 2021.",
-            "title": "TROPESS CrIS-SNPP L2 Deuterated Water Vapor for Forward Stream, Summary Product V1 (TRPSYL2HDOCRSFS) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TROPESS/images/TRPSYL2HDOCRSFS_Sample.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2F5X25TK595WAF",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2F5X25TK595WAF",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TROPESS/images/TRPSYL2HDOCRSFS_Sample.png",
-                    "description": "TROPESS CrIS-SNPP HDO (Forward Stream, Summary Product) at 681 hPa on 01 April 2021.",
                     "@type": "dcat:Distribution",
+                    "description": "TROPESS CrIS-SNPP HDO (Forward Stream, Summary Product) at 681 hPa on 01 April 2021.",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TROPESS/images/TRPSYL2HDOCRSFS_Sample.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/TRPSYL2HDOCRSFS_1.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/TRPSYL2HDOCRSFS_1.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/data/TROPESS_Summary/TRPSYL2HDOCRSFS.1/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/data/TROPESS_Summary/TRPSYL2HDOCRSFS.1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=TRPSYL2HDOCRSFS_1",
-                    "description": "Use the Earthdata Search Client to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search Client to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=TRPSYL2HDOCRSFS_1",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/opendap/TROPESS_Summary/TRPSYL2HDOCRSFS.1/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/opendap/TROPESS_Summary/TRPSYL2HDOCRSFS.1/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/data/TROPESS_Summary/TRPSYL2HDOCRSFS.1/doc/TROPESS_Forward_Stream_README.pdf",
-                    "description": "README Document",
                     "@type": "dcat:Distribution",
+                    "description": "README Document",
+                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/data/TROPESS_Summary/TRPSYL2HDOCRSFS.1/doc/TROPESS_Forward_Stream_README.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's read me document"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TROPESS/User_Guides/TROPESS-HDO_L2_Product_Quick_Start_User_Guide_Summary_only.pdf",
-                    "description": "User's Guide",
                     "@type": "dcat:Distribution",
+                    "description": "User's Guide",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TROPESS/User_Guides/TROPESS-HDO_L2_Product_Quick_Start_User_Guide_Summary_only.pdf",
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
+            "graphic-preview-description": "TROPESS CrIS-SNPP HDO (Forward Stream, Summary Product) at 681 hPa on 01 April 2021.",
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TROPESS/images/TRPSYL2HDOCRSFS_Sample.png",
+            "identifier": "C2247040372-GES_DISC",
+            "issued": "2022-04-01",
+            "keyword": [
+                "atmosphere",
+                "atmospheric chemistry",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/5X25TK595WAF",
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
+                "https://doi.org/10.5194/amt-13-1825-2020",
+                "https://doi.org/10.1109/TGRS.2006.871234",
+                "https://doi.org/10.1029/2002JD002299",
+                "https://doi.org/10.5194/amt-5-397-2012",
+                "https://doi.org/10.1029/2005JD006606",
+                "https://doi.org/10.1029/2011JD016621",
+                "https://doi.org/10.1002/wrcr.20312"
+            ],
+            "release-place": "Greenbelt, MD, USA",
+            "series-name": "TRPSYL2HDOCRSFS",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2021-02-01T00:00:00Z/2021-05-21T23:59:59.999Z",
             "theme": [
                 "TROPESS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "TROPESS CrIS-SNPP L2 Deuterated Water Vapor for Forward Stream, Summary Product V1 (TRPSYL2HDOCRSFS) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-MIRO-2-ESC4-67P-V1.0",
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
+            "description": "This data set contains Spectroscopic, Continuum, and Engineering level 2 data, in the form of table files, taken during the COMET ESCORT 4 phase of the Rosetta mission to comet 67P/CHURYUMOV-GERASIMENKO by the MIRO instrument.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-miro-2-esc4-67p-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-MIRO-2-ESC4-67P-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-miro-2-esc4-67p-v1.0",
-            "description": "This data set contains Spectroscopic, Continuum, and Engineering level 2 data, in the form of table files, taken during the COMET ESCORT 4 phase of the Rosetta mission to comet 67P/CHURYUMOV-GERASIMENKO by the MIRO instrument.",
-            "title": "ROSETTA-ORBITER 67P MIRO 2 ESC4 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P MIRO 2 ESC4 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/GRGIA-05J10",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Tellus. 2019-07-24. TELLUS GRACE Level-3 0.5-degree Glacial Isostatic Adjustment datasets produced by JPL. Version 1.0. TELLUS_GIA_0.5-Deg_v1.0. JPL. Archived by National Aeronautics and Space Administration, U.S. Government, TELLUS. https://doi.org/10.5067/GRGIA-05J10. http://grace.jpl.nasa.gov/data/get-data/gia-trends/. Tellus, TELLUS, 2019-07-24, TELLUS GRACE Level-3 0.5-degree Glacial Isostatic Adjustment v1.0 datasets produced by JPL, http://grace.jpl.nasa.gov/data/get-data/gia-trends/.",
-            "issued": "2019-05-02",
-            "temporal": "1900-01-01T00:00:00Z/2100-12-31T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2019-05-02",
-            "keyword": [
-                "gravity/gravitational field",
-                "earth science",
-                "solid earth"
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
-            "identifier": "C2689796236-POCLOUD",
-            "description": "Glacial isostatic adjustment (GIA) is an ongoing geophysical process and is measured by gravimetry satellites like GRACE and GRACE-FO. To isolate signals of contemporary surface mass loss in the cumulative satellite gravimetry measurements, contemporary GIA rates are computed and subtracted from the satellite gravimetry observations. The GIA correction models provided here are filtered such that they are compatible with Level-3 post-processing filters applied to GRACE(-FO) data as indicated in the [product_id]. In this way, user can effectively assess the impact of the applied GIA correction, and substitute different GIA models should that be desired. This GIA dataset is mapped into 0.5-degree global grid compatible with the JPL Mascon solution, provided in netCDF format.",
-            "release-place": "JPL",
-            "series-name": "TELLUS GRACE Level-3 0.5-degree Glacial Isostatic Adjustment datasets produced by JPL",
-            "graphic-preview-description": "Thumbnail",
             "creator": "Tellus",
-            "title": "TELLUS GRACE Level-3 0.5-degree Glacial Isostatic Adjustment v1.0 datasets produced by JPL",
-            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/TELLUS_GIA_L3_0.5-DEG_V1.0.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "Glacial isostatic adjustment (GIA) is an ongoing geophysical process and is measured by gravimetry satellites like GRACE and GRACE-FO. To isolate signals of contemporary surface mass loss in the cumulative satellite gravimetry measurements, contemporary GIA rates are computed and subtracted from the satellite gravimetry observations. The GIA correction models provided here are filtered such that they are compatible with Level-3 post-processing filters applied to GRACE(-FO) data as indicated in the [product_id]. In this way, user can effectively assess the impact of the applied GIA correction, and substitute different GIA models should that be desired. This GIA dataset is mapped into 0.5-degree global grid compatible with the JPL Mascon solution, provided in netCDF format.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGRGIA-05J10",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGRGIA-05J10",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.1002/2016JB013844",
-                    "description": "Comment on the paper by Purcell et al. 2016 entitled An assessment of ICE-6G_C (VM5a) glacial isostatic adjustment model",
                     "@type": "dcat:Distribution",
+                    "description": "Comment on the paper by Purcell et al. 2016 entitled An assessment of ICE-6G_C (VM5a) glacial isostatic adjustment model",
+                    "downloadURL": "https://doi.org/10.1002/2016JB013844",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/TELLUS_GIA_L3_0.5-DEG_V1.0.jpg",
-                    "description": "Thumbnail",
                     "@type": "dcat:Distribution",
+                    "description": "Thumbnail",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/TELLUS_GIA_L3_0.5-DEG_V1.0.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
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
-                    "downloadURL": "https://grace.jpl.nasa.gov/",
-                    "description": "GRACE Project",
                     "@type": "dcat:Distribution",
+                    "description": "GRACE Project",
+                    "downloadURL": "https://grace.jpl.nasa.gov/",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://podaac.jpl.nasa.gov/GRACE",
-                    "description": "PODAAC GRACE Mission-Page",
                     "@type": "dcat:Distribution",
+                    "description": "PODAAC GRACE Mission-Page",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/GRACE",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.1002/2017GL076644",
-                    "description": "GIA model statistics for GRACE hydrology",
                     "@type": "dcat:Distribution",
+                    "description": "GIA model statistics for GRACE hydrology",
+                    "downloadURL": "https://doi.org/10.1002/2017GL076644",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://grace.jpl.nasa.gov/data/get-data/gia-trends/",
-                    "description": "Glacial Isostatic Adjustment (GIA)",
                     "@type": "dcat:Distribution",
+                    "description": "Glacial Isostatic Adjustment (GIA)",
+                    "downloadURL": "http://grace.jpl.nasa.gov/data/get-data/gia-trends/",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.1093/gji/ggs030",
-                    "description": "Computations of the viscoelastic response of a 3-D compressible Earth to surface loading: an application to Glacial Isostatic Adjustment in Antarctica and Canada",
                     "@type": "dcat:Distribution",
+                    "description": "Computations of the viscoelastic response of a 3-D compressible Earth to surface loading: an application to Glacial Isostatic Adjustment in Antarctica and Canada",
+                    "downloadURL": "https://doi.org/10.1093/gji/ggs030",
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
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2689796236-POCLOUD",
-                    "description": "HTTPS endpoint for data browse and download",
                     "@type": "dcat:Distribution",
+                    "description": "HTTPS endpoint for data browse and download",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2689796236-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2689796236-POCLOUD",
-                    "description": "Browse granule search results in Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse granule search results in Earthdata Search",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2689796236-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 }
             ],
+            "graphic-preview-description": "Thumbnail",
+            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/TELLUS_GIA_L3_0.5-DEG_V1.0.jpg",
+            "identifier": "C2689796236-POCLOUD",
+            "issued": "2019-05-02",
+            "keyword": [
+                "gravity/gravitational field",
+                "earth science",
+                "solid earth"
+            ],
+            "landingPage": "https://doi.org/10.5067/GRGIA-05J10",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2019-05-02",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/JPL/PODAAC"
+            },
+            "release-place": "JPL",
+            "series-name": "TELLUS GRACE Level-3 0.5-degree Glacial Isostatic Adjustment datasets produced by JPL",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "1900-01-01T00:00:00Z/2100-12-31T00:00:00Z",
             "theme": [
                 "GRACE",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "TELLUS GRACE Level-3 0.5-degree Glacial Isostatic Adjustment v1.0 datasets produced by JPL"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC3-0913-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 3 phase 2015-07-01 to 2015-10-21. It is a Global Gravity measurement at the comet 67P and covers the time 2015-07-22T21:21:00.000 to 2015-07-23T03:39:08.500.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc3-0913-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC3-0913-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc3-0913-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 3 phase 2015-07-01 to 2015-10-21. It is a Global Gravity measurement at the comet 67P and covers the time 2015-07-22T21:21:00.000 to 2015-07-23T03:39:08.500.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 3 0913 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 3 0913 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://worldwind.arc.nasa.gov/java/",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Patrick Hogan",
+                "hasEmail": "mailto:patrick.j.hogan@nasa.gov"
+            },
+            "description": "World Wind allows any user to zoom from satellite altitude into any place on Earth, leveraging high resolution LandSat imagery and SRTM elevation data to experience Earth in visually rich 3D, just as if you were really there.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://goworldwind.org/mapserver-and-data-installation/",
+                    "mediaType": "text/html"
+                }
+            ],
+            "identifier": "NASA-0000059",
             "issued": "2018-06-25",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
             "keyword": [
                 "nasa",
                 "elevation",
@@ -1307572,144 +1307584,109 @@
                 "wwhgd",
                 "satellite imagery"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Patrick Hogan",
-                "hasEmail": "mailto:patrick.j.hogan@nasa.gov"
-            },
+            "landingPage": "http://worldwind.arc.nasa.gov/java/",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "NASA-0000059",
-            "description": "World Wind allows any user to zoom from satellite altitude into any place on Earth, leveraging high resolution LandSat imagery and SRTM elevation data to experience Earth in visually rich 3D, just as if you were really there.",
-            "title": "World Wind",
-            "programCode": [
-                "026:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://goworldwind.org/mapserver-and-data-installation/",
-                    "mediaType": "text/html"
-                }
-            ],
-            "accrualPeriodicity": "irregular"
+            "title": "World Wind"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/W9FOYWH0EQZ3",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Canadian Meteorological Centre (CMC) Daily Snow Depth Analysis Data, Version 1. Version 1. Archived by National Aeronautics and Space Administration, U.S. Government, NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/W9FOYWH0EQZ3.",
-            "issued": "1998-08-01",
-            "temporal": "1998-08-01T00:00:00Z/2020-12-31T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-12-31",
-            "keyword": [
-                "earth science",
-                "sea ice",
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
-            "identifier": "C1386205170-NSIDCV0",
             "description": "This data set consists of a Northern Hemisphere subset of the Canadian Meteorological Centre (CMC) operational global daily snow depth analysis. Data include daily analyzed snow depths, as well as monthly means and climatologies of snow depth and estimated snow water equivalent (SWE).",
-            "title": "Canadian Meteorological Centre (CMC) Daily Snow Depth Analysis Data, Version 1",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FW9FOYWH0EQZ3",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FW9FOYWH0EQZ3",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/nsidc0447_CMC_snow_depth_v01/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/nsidc0447_CMC_snow_depth_v01/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/nsidc0447_CMC_snow_depth_v01/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/nsidc0447_CMC_snow_depth_v01/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/W9FOYWH0EQZ3",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/W9FOYWH0EQZ3",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/W9FOYWH0EQZ3",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/W9FOYWH0EQZ3",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C1386205170-NSIDCV0",
+            "issued": "1998-08-01",
+            "keyword": [
+                "earth science",
+                "sea ice",
+                "snow/ice",
+                "cryosphere"
+            ],
+            "landingPage": "https://doi.org/10.5067/W9FOYWH0EQZ3",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2020-12-31",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA NSIDC DAAC"
+            },
             "spatial": "-180.0 0.0 180.0 90.0",
+            "temporal": "1998-08-01T00:00:00Z/2020-12-31T23:59:59.999Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Canadian Meteorological Centre (CMC) Daily Snow Depth Analysis Data, Version 1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1237114207-GES_DISC.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "TOMS Science Team. 1996-07-22. TOMSM3L3. Version 008. TOMS Meteor-3 Total Ozone UV-Reflectivity Daily L3 Global 1 deg x 1.25 deg V008. Greenbelt, MD. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://disc.gsfc.nasa.gov/datacollection/TOMSM3L3_008.html. Digital Science Data.",
-            "issued": "2004-04-30",
-            "temporal": "1991-08-22T00:00:00Z/1994-11-24T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2004-04-30",
-            "keyword": [
-                "atmospheric radiation",
-                "atmosphere",
-                "atmospheric chemistry",
-                "earth science"
-            ],
-            "data-presentation-form": "Digital Science Data",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "PAWAN BHARTIA, PH. D",
                 "hasEmail": "mailto:Pawan.K.Bhartia@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
-            "identifier": "C1237114207-GES_DISC",
-            "description": "The Meteor-3 Total Ozone Mapping Spectrometer (TOMS) version 8 daily global gridded data product contains total column ozone, UV aerosol index, Lambertian effective surface reflectivity (Rayleigh corrected), and UV-B erythemal local noon irradiances. The data are mapped to a global grid of size 180 x 288 with a lat-long resolution of 1.00 x 1.25 degrees. These data are stored in the EOS Hierarchical Data Format (HDF-EOS).\n\nThe TOMS data were produced by the Laboratory for Atmospheres at NASA Goddard Space Flight Center (Code 614).",
-            "release-place": "Greenbelt, MD",
-            "series-name": "TOMSM3L3",
             "creator": "TOMS Science Team",
-            "title": "TOMS Meteor-3 Total Ozone UV-Reflectivity Daily L3 Global 1 deg x 1.25 deg V008 (TOMSM3L3) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/TOMSM3L3_008.png",
-            "programCode": [
-                "026:001"
-            ],
+            "data-presentation-form": "Digital Science Data",
+            "description": "The Meteor-3 Total Ozone Mapping Spectrometer (TOMS) version 8 daily global gridded data product contains total column ozone, UV aerosol index, Lambertian effective surface reflectivity (Rayleigh corrected), and UV-B erythemal local noon irradiances. The data are mapped to a global grid of size 180 x 288 with a lat-long resolution of 1.00 x 1.25 degrees. These data are stored in the EOS Hierarchical Data Format (HDF-EOS).\n\nThe TOMS data were produced by the Laboratory for Atmospheres at NASA Goddard Space Flight Center (Code 614).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -1307718,455 +1307695,457 @@
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/TOMSM3L3_008.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/TOMSM3L3_008.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/Meteor3_TOMS_Level3/TOMSM3L3.008/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/Meteor3_TOMS_Level3/TOMSM3L3.008/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=TOMSM3L3",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=TOMSM3L3",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/opendap/Meteor3_TOMS_Level3/TOMSM3L3.008/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/opendap/Meteor3_TOMS_Level3/TOMSM3L3.008/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc1.gesdisc.eosdis.nasa.gov/daac-bin/wms_acp?version=1.1.1&service=WMS&request=GetCapabilities",
-                    "description": "A Web Map Service (WMS) is a standard protocol for generating georeferenced map images which a map server generates using data from a GIS database.",
                     "@type": "dcat:Distribution",
+                    "description": "A Web Map Service (WMS) is a standard protocol for generating georeferenced map images which a map server generates using data from a GIS database.",
+                    "downloadURL": "https://disc1.gesdisc.eosdis.nasa.gov/daac-bin/wms_acp?version=1.1.1&service=WMS&request=GetCapabilities",
+                    "mediaType": "text/html",
                     "title": "Use Web Map Service (WMS) to download the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/daac-bin/wcsACP?service=WCS&version=1.0.0&request=GetCapabilities",
-                    "description": "The Web Coverage Service (WCS) defines Web-based retrieval of coverages \u2013 that is, digital geospatial information representing space/time-varying phenomena.",
                     "@type": "dcat:Distribution",
+                    "description": "The Web Coverage Service (WCS) defines Web-based retrieval of coverages \u2013 that is, digital geospatial information representing space/time-varying phenomena.",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/daac-bin/wcsACP?service=WCS&version=1.0.0&request=GetCapabilities",
+                    "mediaType": "text/html",
                     "title": "Use Web Coverage Service (WCS) to download the dataset's data"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TOMS/METEOR3_USERGUIDE.PDF",
-                    "description": "Meteor-3 TOMS Data Product User's Guide.",
                     "@type": "dcat:Distribution",
+                    "description": "Meteor-3 TOMS Data Product User's Guide.",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TOMS/METEOR3_USERGUIDE.PDF",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TOMS/v8toms_atbd.pdf",
-                    "description": "TOMS V8 ATBD document.",
                     "@type": "dcat:Distribution",
+                    "description": "TOMS V8 ATBD document.",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TOMS/v8toms_atbd.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's algorithm theoretical basis document"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/information/documents?title=TOMS+Mission+Preservation+Documents",
-                    "description": "Documentation related to legacy TOMS mission.",
                     "@type": "dcat:Distribution",
+                    "description": "Documentation related to legacy TOMS mission.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/information/documents?title=TOMS+Mission+Preservation+Documents",
+                    "mediaType": "text/html",
                     "title": "View this dataset's product history"
                 }
             ],
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/TOMSM3L3_008.png",
+            "identifier": "C1237114207-GES_DISC",
+            "issued": "2004-04-30",
+            "keyword": [
+                "atmospheric radiation",
+                "atmosphere",
+                "atmospheric chemistry",
+                "earth science"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1237114207-GES_DISC.html",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2004-04-30",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
+            },
+            "release-place": "Greenbelt, MD",
+            "series-name": "TOMSM3L3",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "1991-08-22T00:00:00Z/1994-11-24T23:59:59.999Z",
             "theme": [
                 "TOMS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "TOMS Meteor-3 Total Ozone UV-Reflectivity Daily L3 Global 1 deg x 1.25 deg V008 (TOMSM3L3) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-X-OSIWAC-4-CR2-CHKOUT-REFLECT-V1.0",
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
-                "9p/tempel 1 (1867 g1)"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This CODMAC level 4 data set contains radiometric calibrated and geometric distortion corrected (resampled)  image data in reflectance units (normalized and thus without unit),  acquired by the OSIRIS Wide Angle Camera on the Rosetta spacecraft  during the CRUISE 2 mission phase, covering the period  from 2005-04-05T00:00:00.000 to 2006-07-28T23:59:59.000. The prime objective was commissioning / calibration. Several targets of opportunity were observed, but none of them is identifiable as prime target. This version V1.0 is the first version of this dataset.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-x-osiwac-4-cr2-chkout-reflect-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "9p/tempel 1 (1867 g1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-X-OSIWAC-4-CR2-CHKOUT-REFLECT-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-x-osiwac-4-cr2-chkout-reflect-v1.0",
-            "description": "This CODMAC level 4 data set contains radiometric calibrated and geometric distortion corrected (resampled)  image data in reflectance units (normalized and thus without unit),  acquired by the OSIRIS Wide Angle Camera on the Rosetta spacecraft  during the CRUISE 2 mission phase, covering the period  from 2005-04-05T00:00:00.000 to 2006-07-28T23:59:59.000. The prime objective was commissioning / calibration. Several targets of opportunity were observed, but none of them is identifiable as prime target. This version V1.0 is the first version of this dataset.",
-            "title": "ROSETTA-ORBITER CHECKOUT OSIWAC 4 CR2 RDR-REFLECT V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER CHECKOUT OSIWAC 4 CR2 RDR-REFLECT V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-E-RPCLAP-3-EAR1-CALIB2-V1.0",
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
-                "earth"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This data set contains\nCALIBRATED data from Rosetta RPC-LAP, acquired during the EARTH SWING-BY\n1 mission phase where the primary target was the planet EARTH. It\ncontains instrument outputs in volts and amperes, calibrated and\ncorrected for instrument offsets.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-e-rpclap-3-ear1-calib2-v1.0_rhpx-w4zu",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "earth"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-E-RPCLAP-3-EAR1-CALIB2-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-e-rpclap-3-ear1-calib2-v1.0_rhpx-w4zu",
-            "description": "This data set contains\nCALIBRATED data from Rosetta RPC-LAP, acquired during the EARTH SWING-BY\n1 mission phase where the primary target was the planet EARTH. It\ncontains instrument outputs in volts and amperes, calibrated and\ncorrected for instrument offsets.",
-            "title": "ROSETTA-ORBITER EARTH RPCLAP\n3 EAR1 CALIB2 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER EARTH RPCLAP\n3 EAR1 CALIB2 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/CALIOP/CALIPSO/CAL_LID_L3_Tropospheric_APro_CloudFree-Standard-V4-20",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2019-09-11. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/CALIOP/CALIPSO/CAL_LID_L3_Tropospheric_APro_CloudFree-Standard-V4-20. https://asdc.larc.nasa.gov/project/CALIPSO.",
-            "issued": "2019-07-18",
-            "temporal": "2006-06-01T00:00:00Z/2022-01-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2019-07-18",
-            "keyword": [
-                "aerosols",
-                "atmosphere",
-                "earth science"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "DAVID WINKER",
                 "hasEmail": "mailto:david.m.winker@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/LARC/SD/ASDC"
-            },
-            "identifier": "C1633036565-LARC_ASDC",
             "description": "CAL_LID_L3_Tropospheric_APro_CloudFree-Standard-V4-20 is the Cloud-Aerosol Lidar and Infrared Pathfinder Satellite Observation (CALIPSO) Lidar Level 3 Tropospheric Aerosol Profiles, Cloud Free Data, Standard Version 4-20 data product. This data product was collected using the Cloud-Aerosol LIdar with Orthogonal Polarization (CALIOP) instrument. Data collection for this product is ongoing.\r\rThe CALIPSO lidar level 3 aerosol data product reports monthly mean profiles of aerosol optical properties on a uniform spatial grid. It is intended to be a tropospheric product and so data are only reported below altitudes of 12 km. All level 3 parameters are derived from the version 4.20 CALIOP level 2 aerosol profile product and have been quality screened prior to averaging. The primary quantities reported are vertical profiles of aerosol extinction coefficient at 532nm and its vertical integral, the aerosol optical depth (AOD). Aerosol type and spatial distribution information are also included. Averaged profile data is reported for all aerosols, regardless of type, and for mineral dust aerosol only. Classification of dust is based on the aerosol type flags in the level 2 profile product. To keep level 3 file sizes manageable, there are four different types of level 3 files produced, depending on the sky condition and the temporal coverage of the data prior to averaging.\r\rDescription of the Four Sky Conditions (Day, Night)\r1) All Sky: All level 2 columns are averaged, regardless of cloud occurrence\r2) Cloud-Free: Only cloud-free level 2 columns are averaged\r3) Cloudy-Sky, Transparent: Only level 2 columns containing transparent clouds are averaged\r4) Cloud-Sky, Opaque: Only level 2 columns containing opaque clouds are averaged\r\rCALIPSO was launched on April 28, 2006 and continues to collect data necessary to study the impact of clouds and aerosols on the Earth's radiation budget and climate . It flies in the international A-Train constellation for coincident Earth observations. The CALIPSO satellite comprises three instruments, CALIOP, Imaging Infrared Radiometer (IIR), and Wide Field Camera (WFC). CALIPSO is a joint satellite mission between NASA and the French Agency, CNES.",
-            "graphic-preview-description": "CALIPSO Lidar Browse Images (Production - Standard - Science Ready)",
-            "title": "CALIPSO Lidar Level 3 Tropospheric Aerosol Profiles, Cloud Free Data, Standard V4-20",
-            "graphic-preview-file": "https://www-calipso.larc.nasa.gov/products/lidar/browse_images/production/",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FCALIOP%2FCALIPSO%2FCAL_LID_L3_Tropospheric_APro_CloudFree-Standard-V4-20",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FCALIOP%2FCALIPSO%2FCAL_LID_L3_Tropospheric_APro_CloudFree-Standard-V4-20",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
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
-                    "downloadURL": "https://doi.org/10.5067/CALIOP/CALIPSO/CAL_LID_L3_Tropospheric_APro_CloudFree-Standard-V4-20",
-                    "description": "DOI data set landing page for CAL_LID_L3_Tropospheric_APro_CloudFree-Standard-V4-20",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for CAL_LID_L3_Tropospheric_APro_CloudFree-Standard-V4-20",
+                    "downloadURL": "https://doi.org/10.5067/CALIOP/CALIPSO/CAL_LID_L3_Tropospheric_APro_CloudFree-Standard-V4-20",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1633036565-LARC_ASDC",
-                    "description": "Earthdata Search for CAL_LID_L3_Tropospheric_APro_CloudFree-Standard-V4-20 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for CAL_LID_L3_Tropospheric_APro_CloudFree-Standard-V4-20 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1633036565-LARC_ASDC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/CALIPSO/LID_L3_Tropospheric_APro_CloudFree-Standard-V4-20/contents.html",
-                    "description": "OPeNDAP data access for CAL_LID_L3_Tropospheric_APro_CloudFree-Standard-V4-20",
                     "@type": "dcat:Distribution",
+                    "description": "OPeNDAP data access for CAL_LID_L3_Tropospheric_APro_CloudFree-Standard-V4-20",
+                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/CALIPSO/LID_L3_Tropospheric_APro_CloudFree-Standard-V4-20/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/CALIPSO/LID_L3_Tropospheric_APro_CloudFree-Standard-V4-20/",
-                    "description": "ASDC Direct Data Download for CAL_LID_L3_Tropospheric_APro_CloudFree-Standard-V4-20_V4-20",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for CAL_LID_L3_Tropospheric_APro_CloudFree-Standard-V4-20_V4-20",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/CALIPSO/LID_L3_Tropospheric_APro_CloudFree-Standard-V4-20/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
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
-                    "downloadURL": "https://www-calipso.larc.nasa.gov/products/lidar/browse_images/production/",
-                    "description": "CALIPSO Lidar Browse Images (Production - Standard - Science Ready)",
                     "@type": "dcat:Distribution",
+                    "description": "CALIPSO Lidar Browse Images (Production - Standard - Science Ready)",
+                    "downloadURL": "https://www-calipso.larc.nasa.gov/products/lidar/browse_images/production/",
+                    "mediaType": "text/html",
                     "title": "Get a related visualization"
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
-                    "downloadURL": "https://www.icare.univ-lille.fr",
-                    "description": "ICARE Data and Services Center Home Page",
                     "@type": "dcat:Distribution",
+                    "description": "ICARE Data and Services Center Home Page",
+                    "downloadURL": "https://www.icare.univ-lille.fr",
+                    "mediaType": "text/html",
                     "title": "The dataset's home page"
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
-                    "downloadURL": "https://www.nasa.gov/mission_pages/calipso/main/index.html",
-                    "description": "NASA Mission Overview of CALIPSO",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Mission Overview of CALIPSO",
+                    "downloadURL": "https://www.nasa.gov/mission_pages/calipso/main/index.html",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
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
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/calipso/TiltModeGeometry.pdf",
-                    "description": "CALIPSO Tilt Mode Geometry Anomaly",
                     "@type": "dcat:Distribution",
+                    "description": "CALIPSO Tilt Mode Geometry Anomaly",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/calipso/TiltModeGeometry.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's documented anomalies"
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
-                    "downloadURL": "https://www.icare.univ-lille.fr/category/icare-news/tools/",
-                    "description": "ICARE Programmers Toolbox",
                     "@type": "dcat:Distribution",
+                    "description": "ICARE Programmers Toolbox",
+                    "downloadURL": "https://www.icare.univ-lille.fr/category/icare-news/tools/",
+                    "mediaType": "text/html",
                     "title": "Use this dataset in a web based map viewerf"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://www-calipso.larc.nasa.gov/products/CALIPSO_DPC_Rev4x92.pdf",
-                    "description": "CALIPSO - Data Management System - Data Products Catalog - Release 2.4",
                     "@type": "dcat:Distribution",
+                    "description": "CALIPSO - Data Management System - Data Products Catalog - Release 2.4",
+                    "downloadURL": "https://www-calipso.larc.nasa.gov/products/CALIPSO_DPC_Rev4x92.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's production history"
                 }
             ],
+            "graphic-preview-description": "CALIPSO Lidar Browse Images (Production - Standard - Science Ready)",
+            "graphic-preview-file": "https://www-calipso.larc.nasa.gov/products/lidar/browse_images/production/",
+            "identifier": "C1633036565-LARC_ASDC",
+            "issued": "2019-07-18",
+            "keyword": [
+                "aerosols",
+                "atmosphere",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/CALIOP/CALIPSO/CAL_LID_L3_Tropospheric_APro_CloudFree-Standard-V4-20",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2019-07-18",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/LARC/SD/ASDC"
+            },
             "spatial": "-180.0 -85.0 180.0 85.0",
+            "temporal": "2006-06-01T00:00:00Z/2022-01-17T00:00:00Z",
             "theme": [
                 "CALIPSO",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "CALIPSO Lidar Level 3 Tropospheric Aerosol Profiles, Cloud Free Data, Standard V4-20"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=ODY-M-GRS-4-DND-V2.0",
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
-                "2001 mars odyssey"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "Prism counting rates,  normalizations, corrections, and thermal, epithermal, and fast neutron counting rates derived from neutron data collected by the Neutron Spectrometer of the Odyssey GRS instrument suite.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ody-m-grs-4-dnd-v2.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "mars",
+                "2001 mars odyssey"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=ODY-M-GRS-4-DND-V2.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ody-m-grs-4-dnd-v2.0",
-            "description": "Prism counting rates,  normalizations, corrections, and thermal, epithermal, and fast neutron counting rates derived from neutron data collected by the Neutron Spectrometer of the Odyssey GRS instrument suite.",
-            "title": "ODY MARS GAMMA RAY\n      SPECTROMETER 4 DND V2.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ODY MARS GAMMA RAY\n      SPECTROMETER 4 DND V2.0"
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
-                "knowledge",
-                "appel",
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
-            "identifier": "NASA-860__41",
             "description": "Academy of Program/Project & Engineering Leadership's ASK Magazine archive.",
-            "title": "Academy of Program/Project & Engineering Leadership ASK Magazine Past Issues",
-            "programCode": [
-                "026:045"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -1308174,692 +1308153,715 @@
                     "mediaType": "application/pdf"
                 }
             ],
-            "accrualPeriodicity": "R/P3M",
+            "identifier": "NASA-860__41",
+            "issued": "2018-06-25",
+            "keyword": [
+                "knowledge",
+                "appel",
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
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC1-0621-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 1 phase 2014-11-20 to 2015-03-10. It is a Global Gravity measurement at the comet 67P and covers the time 2015-03-04T22:15:00.000 to 2015-03-05T04:07:46.500.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc1-0621-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC1-0621-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc1-0621-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 1 phase 2014-11-20 to 2015-03-10. It is a Global Gravity measurement at the comet 67P and covers the time 2015-03-04T22:15:00.000 to 2015-03-05T04:07:46.500.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 1 0621 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 1 0621 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.nasa.gov/d/rhzt-kijt",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "keyword": [
-                "treatment protocol",
-                "library construction",
-                "hindlimb unloading",
-                "ionizing radiation",
-                "nucleic acid sequencing",
-                "nucleic acid extraction"
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
-            "identifier": "nasa_genelab_GLDS-336_rhzt-kijt",
             "description": "Biological risks associated with space radiation and microgravity are major concerns for long-term space travel. Through a Systems Biology approach our previous NASA work has shown both TGF xce xb2 signaling pathways and miRNAs have a critical impact on defining health risks with and without space irradiation. We hypothesize that circulating microRNA (miRNA) signatures are driving microvascular disease and muscle degeneration associated with accelerating aging and will be enhanced by exposure to the space environment (radiation and microgravity). We investigated this hypothesis both in vivo and in vitro and test novel antagonist therapies to these miRNA signatures as countermeasures to reduce space radiation-induced health risks. A comprehensive Systems Biology approach was used to examine the influence by high atomic number by high (H) atomic number (Z) and energy (E) (HZE) irradiation. To simulate low-dose exposure due to galactic cosmic rays (GCR) we used the ions energy and doses determined by a NASA consensus formula of 7 different ions to represent GCR (referred to as GCR sim model). To simulate high-dose radiation exposure due to solar particle events (SPE) we used an acute dose of SPE simulated beam at 1Gy which has energies ranging from 50MeV to 150MeV. C57BL/6 wild-type mice were utilized for irradiation with our established simulated microgravity model (hindlimb suspension model) and an in vitro 3D microvasculature tissue model under simulated microgravity (clinostat) conditions will also be irradiated. To expand on the circulating miRNA signature determined from our preliminary data we determined a group of conserved miRNAs which are commonly being regulated in the majority of the organs and tissues throughout the host using our established techniques. MiRNA-sequencing on serum (before IR and at time of sacrifice) liver heart and muscle tissue for all radiation groups revealed the key circulating miRNA signature (consisting of multiple miRNAs) impacting disease risk. Collectively understanding of how whole body space radiation impacts microvascular and tissue degeneration through circulating miRNAs will greatly enhance health risk prognostication and provide possible new mechanisms for protection against space radiation.",
-            "title": "miRNA signature detection and countermeasures against HZE radiation exposure for tissue degeneration-Plasma",
-            "programCode": [
-                "026:005"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-336",
-                    "description": "GeneLab Study Page",
                     "@type": "dcat:Distribution",
+                    "description": "GeneLab Study Page",
+                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-336",
+                    "mediaType": "text/html",
                     "title": "miRNA signature detection and countermeasures against HZE radiation exposure for tissue degeneration-Plasma"
                 }
             ],
+            "identifier": "nasa_genelab_GLDS-336_rhzt-kijt",
+            "issued": "2021-05-21",
+            "keyword": [
+                "treatment protocol",
+                "library construction",
+                "hindlimb unloading",
+                "ionizing radiation",
+                "nucleic acid sequencing",
+                "nucleic acid extraction"
+            ],
+            "landingPage": "https://data.nasa.gov/d/rhzt-kijt",
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
+            "title": "miRNA signature detection and countermeasures against HZE radiation exposure for tissue degeneration-Plasma"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1109",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Masarie, K.A., F.G. Hall, G.J. Collatz, B.W. Meeson, S.O. Los, E.Brown De Colstoun, and D.R. Landis. 2012. ISLSCP II GlobalView: Atmospheric Methane Concentrations. ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/1109",
-            "issued": "2023-10-15",
-            "temporal": "1984-01-01T00:00:00Z/1998-12-31T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-10-18",
-            "keyword": [
-                "earth science",
-                "atmosphere",
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
-            "identifier": "C2785319804-ORNL_CLOUD",
             "description": "The GlobalView Methane (CH4) data product contains synchronized and smoothed time series of atmospheric CH4 concentrations at selected sites that were created using the data extension and integration techniques described by Masarie and Tans (1995). The information needed to derive this time series is also in this data set, along with extensive documentation. The longest period of coverage is from 1984 to 1998 with some sites having shorter or longer temporal coverage. Note that the GlobalView-CH4 data products are derived from measurements but contain no actual data. To facilitate heterogeneous CH4 data use in carbon cycle modeling studies, the measurements have been processed (smoothed, interpolated, and extrapolated) resulting in extended records that are evenly incremented in time. There are 74 files with this data set which includes 71 *.zip data files. The other three files include 2 files with site information, one comma-delimited ASCII file (.csv), and one .dat file, and one .dat file which is a single reference marine boundary layer matrix file containing CH4 mixing ratios as a function of time and sine of latitude and is a by-product of the data extension procedure.",
-            "graphic-preview-description": "Browse Image",
-            "title": "ISLSCP II GlobalView: Atmospheric Methane Concentrations",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/islscp_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1109",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1109",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/islscp_ii/carbon/globalview_ch4_point/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/islscp_ii/carbon/globalview_ch4_point/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/ISLSCP_II/guides/globalview_ch4_point.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/ISLSCP_II/guides/globalview_ch4_point.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1109",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1109",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/islscp_ii/carbon/globalview_ch4_point/comp/0_globalview_ch4_readme.txt",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/islscp_ii/carbon/globalview_ch4_point/comp/0_globalview_ch4_readme.txt",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/islscp_ii/carbon/globalview_ch4_point/comp/1_globalview_ch4_doc.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/islscp_ii/carbon/globalview_ch4_point/comp/1_globalview_ch4_doc.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/islscp_ii/carbon/globalview_ch4_point/comp/2_gv_ch4_2001_doc.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/islscp_ii/carbon/globalview_ch4_point/comp/2_gv_ch4_2001_doc.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/islscp_ii/carbon/globalview_ch4_point/comp/globalview_ch4_point.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/islscp_ii/carbon/globalview_ch4_point/comp/globalview_ch4_point.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://daac.ornl.gov/graphics/browse/project/square/islscp_logo_square.png",
-                    "description": "Browse Image",
                     "@type": "dcat:Distribution",
+                    "description": "Browse Image",
+                    "downloadURL": "https://daac.ornl.gov/graphics/browse/project/square/islscp_logo_square.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 }
             ],
+            "graphic-preview-description": "Browse Image",
+            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/islscp_logo_square.png",
+            "identifier": "C2785319804-ORNL_CLOUD",
+            "issued": "2023-10-15",
+            "keyword": [
+                "earth science",
+                "atmosphere",
+                "atmospheric chemistry"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1109",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2023-10-18",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "ORNL_DAAC"
+            },
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "1984-01-01T00:00:00Z/1998-12-31T23:59:59Z",
             "theme": [
                 "ISLSCP II",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "ISLSCP II GlobalView: Atmospheric Methane Concentrations"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-X-PEPSSI-2-PLUTOCRUISE-V2.0",
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
-                "new horizons"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This data set contains Raw data taken by the New Horizons                Pluto Energetic Particle Spectrometer Science Investigation            instrument during the                                                    pluto cruise                                                           mission phase.  This is VERSION 2.0 of this data set.                    Per the original mission plan for cruise operations, the PEPSSI            instrument was initially off for Pluto Cruise and only turned on           for functional tests and calibrations during Annual CheckOuts              (ACO); ACOs usually generate engineering data, but there is some           potential for science during those times. After extensive testing          in early 2012, in July of that year the project approved daily             science operations for the SWAP and PEPSSI instruments throughout          the rest of the cruise to Pluto.                                           The changes in Version 2.0 were re-running of the ancillary data         in the data product, updated geometry from newer SPICE kernels,          minor editing of the documentation, catalogs, etc., and resolution       of liens from the December, 2014 review, plus those from the May,        2016 review of the Pluto Encounter data sets.                            New observations added with this version (V2.0) include ongoing          cruise observations from August, 2014 through January, 2015.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-x-pepssi-2-plutocruise-v2.0_ri5k-h9fg",
+            "issued": "2021-05-21",
+            "keyword": [
+                "new horizons"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-X-PEPSSI-2-PLUTOCRUISE-V2.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-x-pepssi-2-plutocruise-v2.0_ri5k-h9fg",
-            "description": "This data set contains Raw data taken by the New Horizons                Pluto Energetic Particle Spectrometer Science Investigation            instrument during the                                                    pluto cruise                                                           mission phase.  This is VERSION 2.0 of this data set.                    Per the original mission plan for cruise operations, the PEPSSI            instrument was initially off for Pluto Cruise and only turned on           for functional tests and calibrations during Annual CheckOuts              (ACO); ACOs usually generate engineering data, but there is some           potential for science during those times. After extensive testing          in early 2012, in July of that year the project approved daily             science operations for the SWAP and PEPSSI instruments throughout          the rest of the cruise to Pluto.                                           The changes in Version 2.0 were re-running of the ancillary data         in the data product, updated geometry from newer SPICE kernels,          minor editing of the documentation, catalogs, etc., and resolution       of liens from the December, 2014 review, plus those from the May,        2016 review of the Pluto Encounter data sets.                            New observations added with this version (V2.0) include ongoing          cruise observations from August, 2014 through January, 2015.",
-            "title": "NEW HORIZONS                            \n      PEPSSI PLUTO CRUISE                                                     \n      RAW V2.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "NEW HORIZONS                            \n      PEPSSI PLUTO CRUISE                                                     \n      RAW V2.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=FEXP-E-DAED-3-RDR-SPECTRUM-V1.0",
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
-                "geologic remote sensing field experiment",
-                "earth"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This data set was acquired during GRSFE with the Daedalus AA440 spectrafax instrument. The data set consists of over 500 data files. The values stored in each data file are raw instrument counts, which are proportional to radiance. The purpose of these measurements was to provide ground calibration for AVIRIS and ASAS data.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.fexp-e-daed-3-rdr-spectrum-v1.0_ri8e-bcef",
+            "issued": "2021-05-21",
+            "keyword": [
+                "geologic remote sensing field experiment",
+                "earth"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=FEXP-E-DAED-3-RDR-SPECTRUM-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.fexp-e-daed-3-rdr-spectrum-v1.0_ri8e-bcef",
-            "description": "This data set was acquired during GRSFE with the Daedalus AA440 spectrafax instrument. The data set consists of over 500 data files. The values stored in each data file are raw instrument counts, which are proportional to radiance. The purpose of these measurements was to provide ground calibration for AVIRIS and ASAS data.",
-            "title": "FIELD EXP E DAEDALUS SPECTROMETER CALIB RDR SPECTRUM V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "FIELD EXP E DAEDALUS SPECTROMETER CALIB RDR SPECTRUM V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-J-REX-3-JUPITER-V1.0",
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
-                "new horizons"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This data set contains Calibrated data taken by the New Horizons Radio Science Experiment instrument during the Jupiter encounter mission phase.  This is VERSION 1.0 of this data set. The REX datasets over the mission include calibrations using known radio sources, Jupiter, and cold sky measurements; operational readiness tests (ORTs); internal test pattern calibration; and prime science radiometry and occultation observations during the Pluto Encounter.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-j-rex-3-jupiter-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "jupiter",
+                "new horizons"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-J-REX-3-JUPITER-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-j-rex-3-jupiter-v1.0",
-            "description": "This data set contains Calibrated data taken by the New Horizons Radio Science Experiment instrument during the Jupiter encounter mission phase.  This is VERSION 1.0 of this data set. The REX datasets over the mission include calibrations using known radio sources, Jupiter, and cold sky measurements; operational readiness tests (ORTs); internal test pattern calibration; and prime science radiometry and occultation observations during the Pluto Encounter.",
-            "title": "NEW HORIZONS\n      REX JUPITER ENCOUNTER\n      CALIBRATED V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "NEW HORIZONS\n      REX JUPITER ENCOUNTER\n      CALIBRATED V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.7927/H46D5QXN",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Center for International Earth Science Information Network - CIESIN - Columbia University. 2006-12-31. Compendium of Environmental Sustainability Indicator Collections: Complete Collection, Version 1.1. Version 1.01. Palisades, NY. Archived by National Aeronautics and Space Administration, U.S. Government, NASA Socioeconomic Data and Applications Center (SEDAC). https://doi.org/10.7927/H46D5QXN. https://doi.org/10.7927/H46D5QXN.",
-            "issued": "2006-12-31",
-            "temporal": "1973-01-01T00:00:00Z/2005-12-31T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2006-12-31",
-            "references": [
-                "https://doi.org/10.7927/H45H7D60",
-                "https://doi.org/10.7927/H4MS3QNT",
-                "https://doi.org/10.7927/H4B56GNC",
-                "https://doi.org/10.7927/H4RF5RZT",
-                "https://doi.org/10.7927/H42N506Q"
-            ],
-            "keyword": [
-                "earth science",
-                "sustainability",
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
-            "identifier": "C1418954625-SEDAC",
-            "description": "The Compendium of Environmental Sustainability Indicator Collections, Version 1.1 contains 426 indicators for 239 countries from five major environmental sustainability indicator efforts: the 2006 Environmental Performance Index (EPI), 2005 Environmental Sustainability Index (ESI), 2004 Environmental Vulnerability Index (EVI), the Rio to Johannesburg Dashboard, the Wellbeing of Nations, and 2006 National Footprint Accounts. It also incorporates 38 ancillary variables such as region name, dummy variables for landlocked countries and small island states, population, GDP, and land area. The collection is compiled and distributed by the Columbia University Center for International Earth Science Information Network (CIESIN).",
-            "release-place": "Palisades, NY",
-            "graphic-preview-description": "Sample browse graphic of the data set.",
             "creator": "Center for International Earth Science Information Network - CIESIN - Columbia University",
-            "title": "Compendium of Environmental Sustainability Indicator Collections: Complete Collection, Version 1.1",
-            "graphic-preview-file": "https://sedac.ciesin.columbia.edu/downloads/maps/cesic/cesic-complete-collection-v1-1/sedac-logo.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The Compendium of Environmental Sustainability Indicator Collections, Version 1.1 contains 426 indicators for 239 countries from five major environmental sustainability indicator efforts: the 2006 Environmental Performance Index (EPI), 2005 Environmental Sustainability Index (ESI), 2004 Environmental Vulnerability Index (EVI), the Rio to Johannesburg Dashboard, the Wellbeing of Nations, and 2006 National Footprint Accounts. It also incorporates 38 ancillary variables such as region name, dummy variables for landlocked countries and small island states, population, GDP, and land area. The collection is compiled and distributed by the Columbia University Center for International Earth Science Information Network (CIESIN).",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.7927%2FH46D5QXN",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.7927%2FH46D5QXN",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/downloads/maps/cesic/cesic-complete-collection-v1-1/sedac-logo.jpg",
-                    "description": "Sample browse graphic of the data set.",
                     "@type": "dcat:Distribution",
+                    "description": "Sample browse graphic of the data set.",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/downloads/maps/cesic/cesic-complete-collection-v1-1/sedac-logo.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/cesic-complete-collection-v1-1/data-download",
-                    "description": "Data Download Page",
                     "@type": "dcat:Distribution",
+                    "description": "Data Download Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/cesic-complete-collection-v1-1/data-download",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://sedac.ciesin.columbia.edu/data/set/cesic-complete-collection-v1-1/docs",
-                    "description": "Documentation Page",
                     "@type": "dcat:Distribution",
+                    "description": "Documentation Page",
+                    "downloadURL": "http://sedac.ciesin.columbia.edu/data/set/cesic-complete-collection-v1-1/docs",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/cesic-complete-collection-v1-1",
-                    "description": "Data Set\u00a0Overview Page",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set\u00a0Overview Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/cesic-complete-collection-v1-1",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "graphic-preview-description": "Sample browse graphic of the data set.",
+            "graphic-preview-file": "https://sedac.ciesin.columbia.edu/downloads/maps/cesic/cesic-complete-collection-v1-1/sedac-logo.jpg",
+            "identifier": "C1418954625-SEDAC",
+            "issued": "2006-12-31",
+            "keyword": [
+                "earth science",
+                "sustainability",
+                "human dimensions"
+            ],
+            "landingPage": "https://doi.org/10.7927/H46D5QXN",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2006-12-31",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "SEDAC"
+            },
+            "references": [
+                "https://doi.org/10.7927/H45H7D60",
+                "https://doi.org/10.7927/H4MS3QNT",
+                "https://doi.org/10.7927/H4B56GNC",
+                "https://doi.org/10.7927/H4RF5RZT",
+                "https://doi.org/10.7927/H42N506Q"
+            ],
+            "release-place": "Palisades, NY",
             "spatial": "-180.0 -55.0 180.0 90.0",
+            "temporal": "1973-01-01T00:00:00Z/2005-12-31T00:00:00Z",
             "theme": [
                 "CESIC",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Compendium of Environmental Sustainability Indicator Collections: Complete Collection, Version 1.1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/GEWEXSRB/Rel4-IP_Shortwave_3hrlymonthly_utc_1",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/GEWEXSRB/Rel4-IP_Shortwave_3hrlymonthly_utc_1.",
-            "issued": "2020-10-05",
-            "temporal": "1983-07-01T00:00:00Z/2017-06-30T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-10-05",
-            "keyword": [
-                "earth science",
-                "clouds",
-                "atmospheric radiation",
-                "atmosphere",
-                "biosphere",
-                "vegetation"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Colleen Mikovitz",
                 "hasEmail": "mailto:j.c.mikovitz@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/LARC/SD/ASDC"
-            },
-            "identifier": "C2058672708-LARC_ASDC",
             "description": "GEWEXSRB_Rel4-IP_Shortwave_3hrlymonthly_utc is the Global Energy and Water Exchanges (GEWEX) Surface Radiation Budget (SRB) Integrated Product (Rel-4) Shortwave 3-Hourly Monthly Average by UTC (also known as diurnal) data product. It contains global fields of 11 shortwave surface and Top of Atmosphere (TOA), radiative parameters derived with the Shortwave algorithm of the NASA World Climate Research Programme/Global Energy and Water-Cycle Experiment (WCRP/GEWEX) Surface Radiation Budget (SRB) Project. This version is known as Release 4-Integrated Product. The fluxes include all-sky, clear-sky and pristine-sky TOA upward fluxes, incoming (downward) TOA flux, and all-sky, clear-sky and pristine-sky upward and downward fluxes at surface. Surface PAR, cloud fraction, average solar zenith angle and a status flag of filled fluxes are also included. Inputs to the shortwave algorithm are cloud and radiance information from International Satellite Cloud Climatology Project (ISCCP) HXS, total column precipitable water from ISCCP nnHIRS, Total Solar Irradiance from SORCE TIM, ozone from ISCCP, and MAC V1 aerosol amounts and radiative properties. The temporal range is July 1983 through June 2017. These data are averaged from UTC 3-hourly values. Data collection for this product is complete.",
-            "title": "GEWEX SRB Integrated Product (Rel-4) Shortwave 3-Hourly Monthly Average by UTC Fluxes",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGEWEXSRB%2FRel4-IP_Shortwave_3hrlymonthly_utc_1",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGEWEXSRB%2FRel4-IP_Shortwave_3hrlymonthly_utc_1",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://gewex-srb.larc.nasa.gov/",
-                    "description": "NASA GEWEX Surface Radiation Budget project page",
                     "@type": "dcat:Distribution",
+                    "description": "NASA GEWEX Surface Radiation Budget project page",
+                    "downloadURL": "https://gewex-srb.larc.nasa.gov/",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/GEWEXSRB/Rel4-IP_Shortwave_3hrlymonthly_utc_1",
-                    "description": "DOI data set landing page for GEWEXSRB_Rel4-IP_Shortwave_3hrlymonthly_utc_1",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for GEWEXSRB_Rel4-IP_Shortwave_3hrlymonthly_utc_1",
+                    "downloadURL": "https://doi.org/10.5067/GEWEXSRB/Rel4-IP_Shortwave_3hrlymonthly_utc_1",
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
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/srb/SRB_Rel4-IP_ATBD.pdf",
-                    "description": "SRB Rel4-IP Algorithm Theoretical Basis Document.",
                     "@type": "dcat:Distribution",
+                    "description": "SRB Rel4-IP Algorithm Theoretical Basis Document.",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/srb/SRB_Rel4-IP_ATBD.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's algorithm theoretical basis document"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/srb/SRB_Rel4-IP_Public_Release_Announcement.pdf",
-                    "description": "SRB Release 4 Announcement",
                     "@type": "dcat:Distribution",
+                    "description": "SRB Release 4 Announcement",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/srb/SRB_Rel4-IP_Public_Release_Announcement.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View an important notice for this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/project/SRB",
-                    "description": "ASDC Data and Information for SRB",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Data and Information for SRB",
+                    "downloadURL": "https://asdc.larc.nasa.gov/project/SRB",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2058672708-LARC_ASDC",
-                    "description": "Earthdata Search for GEWEXSRB_Rel4-IP_Shortwave_3hrlymonthly_utc_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for GEWEXSRB_Rel4-IP_Shortwave_3hrlymonthly_utc_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2058672708-LARC_ASDC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/SRB/GEWEXSRB_Rel4-IP/Shortwave_3hrlymonthly_utc_1/",
-                    "description": "ASDC Direct Data Download for GEWEXSRB_Rel4-IP_Shortwave_3hrlymonthly_utc_1",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for GEWEXSRB_Rel4-IP_Shortwave_3hrlymonthly_utc_1",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/SRB/GEWEXSRB_Rel4-IP/Shortwave_3hrlymonthly_utc_1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/SRB/GEWEXSRB_Rel4-IP/Shortwave_3hrlymonthly_utc_1/contents.html",
-                    "description": "OPeNDAP data access for GEWEXSRB_Rel4-IP_Shortwave_3hrlymonthly_utc_1",
                     "@type": "dcat:Distribution",
+                    "description": "OPeNDAP data access for GEWEXSRB_Rel4-IP_Shortwave_3hrlymonthly_utc_1",
+                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/SRB/GEWEXSRB_Rel4-IP/Shortwave_3hrlymonthly_utc_1/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 }
             ],
+            "identifier": "C2058672708-LARC_ASDC",
+            "issued": "2020-10-05",
+            "keyword": [
+                "earth science",
+                "clouds",
+                "atmospheric radiation",
+                "atmosphere",
+                "biosphere",
+                "vegetation"
+            ],
+            "landingPage": "https://doi.org/10.5067/GEWEXSRB/Rel4-IP_Shortwave_3hrlymonthly_utc_1",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2020-10-05",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/LARC/SD/ASDC"
+            },
             "spatial": "<?xml version=\"1.0\" encoding=\"UTF-8\"?><gml:Polygon xmlns:gml=\"http://www.opengis.net/gml/3.2\" srsName=\"EPSG:9825\"><gml:outerBoundaryIs><gml:LinearRing><gml:posList>-90.0 -180.0 -90.0 180.0 90.0 180.0 90.0 -180.0 -90.0 -180.0</gml:posList></gml:LinearRing></gml:outerBoundaryIs><gml:innerBoundaryIs></gml:innerBoundaryIs></gml:Polygon>",
+            "temporal": "1983-07-01T00:00:00Z/2017-06-30T23:59:59.999Z",
             "theme": [
                 "SRB",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "GEWEX SRB Integrated Product (Rel-4) Shortwave 3-Hourly Monthly Average by UTC Fluxes"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-X-PEPSSI-3-LAUNCH-V1.0",
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
+            "description": "This data set contains Raw data taken by the New Horizons Pluto Energetic Particle Spectrometer Science Investigation instrument during the post-launch checkout mission phase.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-x-pepssi-3-launch-v1.0_riek-hytq",
+            "issued": "2018-06-26",
+            "keyword": [
+                "new horizons",
+                "solar wind"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-X-PEPSSI-3-LAUNCH-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-x-pepssi-3-launch-v1.0_riek-hytq",
-            "description": "This data set contains Raw data taken by the New Horizons Pluto Energetic Particle Spectrometer Science Investigation instrument during the post-launch checkout mission phase.",
-            "title": "NEW HORIZONS PEPSSI POST-LAUNCH CHECKOUT V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "NEW HORIZONS PEPSSI POST-LAUNCH CHECKOUT V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/2021",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Hook, S.J., J.S. Myers, K.J. Thome, M. Fitzgerald, A.B. Kahle,  Airborne Sensor Facility NASA Ames Research Center, G. McFarquhar, S.E. Platnick, and M.D. King. 2022. MASTER: Tropical Composition, Cloud and Climate Coupling Campaign, 2007. ORNL DAAC, Oak Ridge, Tennessee, USA. https://doi.org/10.3334/ORNLDAAC/2021",
-            "issued": "2023-06-29",
-            "temporal": "2007-07-29T12:10:38Z/2007-08-18T19:05:18Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-13",
-            "keyword": [
-                "land surface",
-                "earth science",
-                "infrared wavelengths",
-                "surface thermal properties",
-                "oceans",
-                "ocean temperature",
-                "visible wavelengths",
-                "spectral/engineering",
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
-            "identifier": "C2731721497-ORNL_CLOUD",
             "description": "This dataset includes Level 1B (L1B) and Level 2 (L2) data products from the MODIS/ASTER Airborne Simulator (MASTER) instrument. The spectral data were collected during seven flights aboard a NASA ER-2 aircraft over California, Nevada, Central America, and eastern Pacific Ocean from 2007-07-29 to 2007-08-18. This deployment supported the Tropical Composition, Cloud and Climate Coupling Campaign (TC4), which investigated the atmospheric structure, properties, and processes in the Eastern Pacific Tropics. Data products include L1B georeferenced multispectral imagery of calibrated radiance in 50 bands covering wavelengths of 0.460 to 12.879 micrometers at approximately 50-meter spatial resolution. Derived L2 data products are emissivity in 5 bands in thermal infrared range (8.58 to 12.13 micrometers) and land surface temperature. The L1B file format is HDF-4, and L2 products are provided in ENVI and KMZ formats. In addition, the dataset includes flight paths, spectral band information, instrument configuration, ancillary notes, and summary information for each flight, and browse images derived from each L1B data file.",
-            "graphic-preview-description": "Single-band images and a RGB composite image from flight track 1 acquired on 31 July 2007 over Panama. Source: MASTERL1B_0792500_01_20070731_1317_1321_V03.jpg",
-            "title": "MASTER: Tropical Composition, Cloud and Climate Coupling Campaign, 2007",
-            "graphic-preview-file": "https://daac.ornl.gov/MASTER/guides/MASTER_TC4_2007_Fig1.jpg",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F2021",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F2021",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/master/MASTER_TC4_2007/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/master/MASTER_TC4_2007/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/MASTER/guides/MASTER_TC4_2007.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/MASTER/guides/MASTER_TC4_2007.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/2021",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/2021",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/master/MASTER_TC4_2007/comp/MASTER_TC4_2007.pdf",
-                    "description": "MASTER: Tropical Composition, Cloud and Climate Coupling Campaign, 2007: MASTER_TC4_2007.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "MASTER: Tropical Composition, Cloud and Climate Coupling Campaign, 2007: MASTER_TC4_2007.pdf",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/master/MASTER_TC4_2007/comp/MASTER_TC4_2007.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://daac.ornl.gov/MASTER/guides/MASTER_TC4_2007_Fig1.jpg",
-                    "description": "Single-band images and a RGB composite image from flight track 1 acquired on 31 July 2007 over Panama. Source: MASTERL1B_0792500_01_20070731_1317_1321_V03.jpg",
                     "@type": "dcat:Distribution",
+                    "description": "Single-band images and a RGB composite image from flight track 1 acquired on 31 July 2007 over Panama. Source: MASTERL1B_0792500_01_20070731_1317_1321_V03.jpg",
+                    "downloadURL": "https://daac.ornl.gov/MASTER/guides/MASTER_TC4_2007_Fig1.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 }
             ],
+            "graphic-preview-description": "Single-band images and a RGB composite image from flight track 1 acquired on 31 July 2007 over Panama. Source: MASTERL1B_0792500_01_20070731_1317_1321_V03.jpg",
+            "graphic-preview-file": "https://daac.ornl.gov/MASTER/guides/MASTER_TC4_2007_Fig1.jpg",
+            "identifier": "C2731721497-ORNL_CLOUD",
+            "issued": "2023-06-29",
+            "keyword": [
+                "land surface",
+                "earth science",
+                "infrared wavelengths",
+                "surface thermal properties",
+                "oceans",
+                "ocean temperature",
+                "visible wavelengths",
+                "spectral/engineering",
+                "surface radiative properties"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/2021",
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
             "spatial": "-118.55 -6.5 -78.69 40.98",
+            "temporal": "2007-07-29T12:10:38Z/2007-08-18T19:05:18Z",
             "theme": [
                 "MASTER",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "MASTER: Tropical Composition, Cloud and Climate Coupling Campaign, 2007"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-5-ESC3-67P-M20-GEO-V1.0",
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
+            "description": "This CODMAC level 5 data set contains derived data products that include pixel-precise georeferencing information, acquired by the OSIRIS Wide Angle Camera on the Rosetta spacecraft during the COMET ESCORT 3 mission phase, covering the period from 2015-08-25T23:25:00.000 to 2015-09-22T23:24:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V1.0 is the first version of this dataset: Lien corrected dataset after October 2018 PSA/PDS external peer review.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-5-esc3-67p-m20-geo-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-5-ESC3-67P-M20-GEO-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-5-esc3-67p-m20-geo-v1.0",
-            "description": "This CODMAC level 5 data set contains derived data products that include pixel-precise georeferencing information, acquired by the OSIRIS Wide Angle Camera on the Rosetta spacecraft during the COMET ESCORT 3 mission phase, covering the period from 2015-08-25T23:25:00.000 to 2015-09-22T23:24:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V1.0 is the first version of this dataset: Lien corrected dataset after October 2018 PSA/PDS external peer review.",
-            "title": "ROSETTA-ORBITER 67P OSIWAC 5 ESC3-MTP020 DDR-GEO V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P OSIWAC 5 ESC3-MTP020 DDR-GEO V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-M-OSIWAC-3-MARS-MARSSWINGBY-V1.4",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This data set contains images acquired by the OSIRIS Wide Angle Camera during the MARS SWING-BY mission phase",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-m-osiwac-3-mars-marsswingby-v1.4_rihh-99dz",
             "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "16 cyg b",
                 "vega",
@@ -1308870,448 +1308872,448 @@
                 "jupiter",
                 "international rosetta mission"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-M-OSIWAC-3-MARS-MARSSWINGBY-V1.4",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-m-osiwac-3-mars-marsswingby-v1.4_rihh-99dz",
-            "description": "This data set contains images acquired by the OSIRIS Wide Angle Camera during the MARS SWING-BY mission phase",
-            "title": "ROSETTA-ORBITER MARS SWING-BY OSIWAC 3 RDR V1.4",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "ROSETTA-ORBITER MARS SWING-BY OSIWAC 3 RDR V1.4"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-4-ESC1-67P-M10-REFLECT-V1.0",
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
+            "description": "This CODMAC level 4 data set contains radiometric calibrated and geometric distortion corrected (resampled) image data in reflectance units (normalized and thus without unit), acquired by the OSIRIS Narrow Angle Camera on the Rosetta spacecraft during the COMET ESCORT 1 mission phase, covering the period from 2014-11-21T23:25:00.000 to 2014-12-19T23:24:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V1.0 is the first version of this dataset: Lien corrected dataset after October 2018 PSA/PDS external peer review.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-4-esc1-67p-m10-reflect-v1.0_rik3-vqz9",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-4-ESC1-67P-M10-REFLECT-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-4-esc1-67p-m10-reflect-v1.0_rik3-vqz9",
-            "description": "This CODMAC level 4 data set contains radiometric calibrated and geometric distortion corrected (resampled) image data in reflectance units (normalized and thus without unit), acquired by the OSIRIS Narrow Angle Camera on the Rosetta spacecraft during the COMET ESCORT 1 mission phase, covering the period from 2014-11-21T23:25:00.000 to 2014-12-19T23:24:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V1.0 is the first version of this dataset: Lien corrected dataset after October 2018 PSA/PDS external peer review.",
-            "title": "ROSETTA-ORBITER 67P OSINAC 4 ESC1-MTP010 RDR-REFLECT V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P OSINAC 4 ESC1-MTP010 RDR-REFLECT V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-X-SREM-5-EXT1-MTP027-V1.0",
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
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-x-srem-5-ext1-mtp027-v1.0",
             "description": "This data set contains derived electron and proton flux energies in MeV from the Standard Radiation Environment Monitor (SREM) instrument on the Rosetta spacecraft, which had the primary target of comet 67P/Churyumov-Gerasimenko. These are CODMAC Level 5 derived data, and measure the radiation in the spacecraft environment during the Medium Term Plan 27 period of the EXTENSION 1 mission phase.",
-            "title": "ROSETTA-ORBITER 67P SREM 5 EXTENSION 1\n    MTP027 V1.0",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-x-srem-5-ext1-mtp027-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-X-SREM-5-EXT1-MTP027-V1.0",
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
+            "title": "ROSETTA-ORBITER 67P SREM 5 EXTENSION 1\n    MTP027 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C2792580147-CDDIS.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, CDDIS.",
-            "issued": "1992-01-01",
-            "temporal": "2023-10-01T00:00:00Z/2025-01-13T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-06",
-            "keyword": [
-                "geodetics",
-                "gravity/gravitational field",
-                "solid earth",
-                "tectonics",
-                "earth science"
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
-            "identifier": "C2792580147-CDDIS",
             "description": "This product contains a time series of attitude quaternion components for healthy satellites in the Galileo constellation that are accumulated every minute throughout the day. The product is generated at JPL's Global Differential GPS Operations Centers in real-time. The data in this product can be concatenated with other daily products to provide larger coverage in time.",
-            "title": "Ground-Based Global Navigation Satellite System (GNSS) Galileo real-time POD Attitude Quaternions (30-second sampling, 60-second files) from NASA CDDIS",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/search/concepts/C2792580147-CDDIS.html",
-                    "description": "View this dataset on the CMR (Common Metadata Repository)",
                     "@type": "dcat:Distribution",
+                    "description": "View this dataset on the CMR (Common Metadata Repository)",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/search/concepts/C2792580147-CDDIS.html",
+                    "mediaType": "text/html",
                     "title": "CMR"
                 }
             ],
+            "identifier": "C2792580147-CDDIS",
+            "issued": "1992-01-01",
+            "keyword": [
+                "geodetics",
+                "gravity/gravitational field",
+                "solid earth",
+                "tectonics",
+                "earth science"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C2792580147-CDDIS.html",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2025-01-06",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "CDDIS"
+            },
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2023-10-01T00:00:00Z/2025-01-13T00:00:00Z",
             "theme": [
                 "IGS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Ground-Based Global Navigation Satellite System (GNSS) Galileo real-time POD Attitude Quaternions (30-second sampling, 60-second files) from NASA CDDIS"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1801",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Simard, M., M.W. Denbina, D.J. Jensen, and R. Lane. 2020. Pre-Delta-X: Water Levels across Wax Lake Outlet, Atchafalaya Basin, LA, USA, 2016. ORNL DAAC, Oak Ridge, Tennessee, USA. https://doi.org/10.3334/ORNLDAAC/1801",
-            "issued": "2020-08-25",
-            "temporal": "2016-10-13T00:00:00Z/2016-10-20T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-06-12",
-            "keyword": [
-                "oceans",
-                "atmospheric/ocean indicators",
-                "surface water",
-                "climate indicators",
-                "geomorphic landforms/processes",
-                "ecosystems",
-                "earth science",
-                "terrestrial hydrosphere",
-                "land surface",
-                "coastal processes",
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
-            "identifier": "C2025123345-ORNL_CLOUD",
             "description": "This dataset provides absolute water level elevations derived for 10 locations across the Wax Lake Delta, Atchafalaya Basin, in Southern Louisiana, USA, within the Mississippi River Delta (MRD) floodplain. Field measurements were made during the Pre-Delta-X campaign on October 13-20, 2016. Relative water level measurements were recorded every five minutes during a one-week period using in situ pressure transducers (Solinst) to measure water surface elevation change with millimeter accuracy. The Solinst system combines a total pressure transducer (TPT) and a temperature detector. Once underwater, the TPT measures the sum of the atmosphere and water pressure above the sensor. Atmospheric pressure fluctuations must be accounted for to obtain the height of the water column above the TPT. An absolute elevation correction was applied to the water level data using an iterative approach with the USGS Calumet Station water level height and Airborne Snow Observatory (ASO) lidar water level profiles. These Pre-Delta-X water level measurements served to calibrate and validate the campaign's remote sensing observations and hydrodynamic models.",
-            "graphic-preview-description": "Water level pressure transducer field deployment. a) A total pressure transducer (TPT) to measure water level changes (Solinst; 6.25 in long). b) Installation of a TPT in shallow water within a PVC pipe. The pipe is embedded into the sediment with the TPT 20 cm above the bottom of the channel. c) Installation of a TPT in deep water attached to a concrete block. The TPT is protected inside the small black PVC pipe. The TPT must be above the block once sitting on the bottom of the channel. The rope is attached to a nearby tree or post for later retrieval. Source: Thomas et al. 2019",
-            "title": "Pre-Delta-X: Water Levels across Wax Lake Outlet, Atchafalaya Basin, LA, USA, 2016",
-            "graphic-preview-file": "https://daac.ornl.gov/DELTAX/guides/PreDeltaX_Water_Level_Data_Fig1.PNG",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1801",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1801",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/deltax/PreDeltaX_Water_Level_Data/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/deltax/PreDeltaX_Water_Level_Data/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/DELTAX/guides/PreDeltaX_Water_Level_Data.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/DELTAX/guides/PreDeltaX_Water_Level_Data.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1801",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1801",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/deltax/PreDeltaX_Water_Level_Data/comp/PreDeltaX_Water_Level_Data.pdf",
-                    "description": "Pre-Delta-X: Water Levels across Wax Lake Outlet, Atchafalaya Basin, LA, USA, 2016: PreDeltaX_Water_Level_Data.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "Pre-Delta-X: Water Levels across Wax Lake Outlet, Atchafalaya Basin, LA, USA, 2016: PreDeltaX_Water_Level_Data.pdf",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/deltax/PreDeltaX_Water_Level_Data/comp/PreDeltaX_Water_Level_Data.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://daac.ornl.gov/DELTAX/guides/PreDeltaX_Water_Level_Data_Fig1.PNG",
-                    "description": "Water level pressure transducer field deployment. a) A total pressure transducer (TPT) to measure water level changes (Solinst; 6.25 in long). b) Installation of a TPT in shallow water within a PVC pipe. The pipe is embedded into the sediment with the TPT 20 cm above the bottom of the channel. c) Installation of a TPT in deep water attached to a concrete block. The TPT is protected inside the small black PVC pipe. The TPT must be above the block once sitting on the bottom of the channel. The rope is attached to a nearby tree or post for later retrieval. Source: Thomas et al. 2019",
                     "@type": "dcat:Distribution",
+                    "description": "Water level pressure transducer field deployment. a) A total pressure transducer (TPT) to measure water level changes (Solinst; 6.25 in long). b) Installation of a TPT in shallow water within a PVC pipe. The pipe is embedded into the sediment with the TPT 20 cm above the bottom of the channel. c) Installation of a TPT in deep water attached to a concrete block. The TPT is protected inside the small black PVC pipe. The TPT must be above the block once sitting on the bottom of the channel. The rope is attached to a nearby tree or post for later retrieval. Source: Thomas et al. 2019",
+                    "downloadURL": "https://daac.ornl.gov/DELTAX/guides/PreDeltaX_Water_Level_Data_Fig1.PNG",
+                    "mediaType": "image/png",
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
+            "graphic-preview-description": "Water level pressure transducer field deployment. a) A total pressure transducer (TPT) to measure water level changes (Solinst; 6.25 in long). b) Installation of a TPT in shallow water within a PVC pipe. The pipe is embedded into the sediment with the TPT 20 cm above the bottom of the channel. c) Installation of a TPT in deep water attached to a concrete block. The TPT is protected inside the small black PVC pipe. The TPT must be above the block once sitting on the bottom of the channel. The rope is attached to a nearby tree or post for later retrieval. Source: Thomas et al. 2019",
+            "graphic-preview-file": "https://daac.ornl.gov/DELTAX/guides/PreDeltaX_Water_Level_Data_Fig1.PNG",
+            "identifier": "C2025123345-ORNL_CLOUD",
+            "issued": "2020-08-25",
+            "keyword": [
+                "oceans",
+                "atmospheric/ocean indicators",
+                "surface water",
+                "climate indicators",
+                "geomorphic landforms/processes",
+                "ecosystems",
+                "earth science",
+                "terrestrial hydrosphere",
+                "land surface",
+                "coastal processes",
+                "biosphere"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1801",
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
             "spatial": "-91.45 29.51 -91.36 29.74",
+            "temporal": "2016-10-13T00:00:00Z/2016-10-20T23:59:59Z",
             "theme": [
                 "Delta-X",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Pre-Delta-X: Water Levels across Wax Lake Outlet, Atchafalaya Basin, LA, USA, 2016"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-2-PRL-67PCHURYUMOV-M01-V2.0",
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
+            "description": "This data set contains images acquired by the OSIRIS Narrow Angle Camera during the PRELANDING phase of the Rosetta mission at the comet 67P, covering the period from 2014-01-20T10:00:00.000 to 2014-05-07T12:47:59.000. This version V2.0 supersedes previous deliveries of the same dataset.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-2-prl-67pchuryumov-m01-v2.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-2-PRL-67PCHURYUMOV-M01-V2.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-2-prl-67pchuryumov-m01-v2.0",
-            "description": "This data set contains images acquired by the OSIRIS Narrow Angle Camera during the PRELANDING phase of the Rosetta mission at the comet 67P, covering the period from 2014-01-20T10:00:00.000 to 2014-05-07T12:47:59.000. This version V2.0 supersedes previous deliveries of the same dataset.",
-            "title": "ROSETTA-ORBITER PRELANDING OSINAC 2 EDR MTP001 V2.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER PRELANDING OSINAC 2 EDR MTP001 V2.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=PHX-M-MET-2-L-EDR-V1.0",
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
+            "description": "The PHX Atmospheric Lidar Profiles product contains unprocessed laser scattering atmospheric profiles for photon counting data at 532nm, and analog data at both 532 and 1064nm wavelengths (expressed in Dignal Numbers). The range data is provided as a time series of profiles between 5 and 90 min in total duration, with each profile representing an accumulation or average over 1.28-20.24 sec. Supplemental data of estimated laser power and inter-profile analog background skylight estimates are also provided.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.phx-m-met-2-l-edr-v1.0_rirc-t6kp",
+            "issued": "2018-06-26",
+            "keyword": [
+                "mars",
+                "phoenix"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=PHX-M-MET-2-L-EDR-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.phx-m-met-2-l-edr-v1.0_rirc-t6kp",
-            "description": "The PHX Atmospheric Lidar Profiles product contains unprocessed laser scattering atmospheric profiles for photon counting data at 532nm, and analog data at both 532 and 1064nm wavelengths (expressed in Dignal Numbers). The range data is provided as a time series of profiles between 5 and 90 min in total duration, with each profile representing an accumulation or average over 1.28-20.24 sec. Supplemental data of estimated laser power and inter-profile analog background skylight estimates are also provided.",
-            "title": "PHOENIX MARS MET LIDAR ATMOSPHERIC PROFILES EDR V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "PHOENIX MARS MET LIDAR ATMOSPHERIC PROFILES EDR V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewBundle.jsp?identifier=urn%3Anasa%3Apds%3Aast.shevchenko-tedesco.occultation-albedos&version=1.0",
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
+            "description": "This data set contains albedos for 57    asteroids determined from diameters obtained from stellar              occultations.  These albedos are from Shevchenko and Tedesco (2006).",
+            "identifier": "urn:nasa:pds:ast.shevchenko-tedesco.occultation-albedos",
+            "issued": "2021-05-21",
+            "keyword": [
+                "none",
+                "multiple asteroids"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewBundle.jsp?identifier=urn%3Anasa%3Apds%3Aast.shevchenko-tedesco.occultation-albedos&version=1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:ast.shevchenko-tedesco.occultation-albedos",
-            "description": "This data set contains albedos for 57    asteroids determined from diameters obtained from stellar              occultations.  These albedos are from Shevchenko and Tedesco (2006).",
-            "title": "ASTEROID ALBEDOS FROM STELLAR OCCULTATIONS",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ASTEROID ALBEDOS FROM STELLAR OCCULTATIONS"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-X-SREM-5-PRL-COM-V1.0",
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
+            "description": "This data set contains derived electron and proton flux energies in MeV from the Standard Radiation Environment Monitor (SREM) instrument on the Rosetta spacecraft.  These are CODMAC Level 5 derived data, and measure the radiation in the spacecraft environment during the PRELANDING COMISSIONING mission phase.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-x-srem-5-prl-com-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "calibration"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-X-SREM-5-PRL-COM-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-x-srem-5-prl-com-v1.0",
-            "description": "This data set contains derived electron and proton flux energies in MeV from the Standard Radiation Environment Monitor (SREM) instrument on the Rosetta spacecraft.  These are CODMAC Level 5 derived data, and measure the radiation in the spacecraft environment during the PRELANDING COMISSIONING mission phase.",
-            "title": "ROSETTA-ORBITER X SREM 5 PRELANDING\n    COM V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER X SREM 5 PRELANDING\n    COM V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC3-0940-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 3 phase 2015-07-01 to 2015-10-21. It is a Global Gravity measurement at the comet 67P and covers the time 2015-08-03T21:28:10.000 to 2015-08-04T05:22:56.500.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc3-0940-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC3-0940-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc3-0940-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 3 phase 2015-07-01 to 2015-10-21. It is a Global Gravity measurement at the comet 67P and covers the time 2015-08-03T21:28:10.000 to 2015-08-04T05:22:56.500.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 3 0940 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 3 0940 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=CO-S-UVIS-2-SSB-V1.1",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "Photometric observations of stellar occultations by Saturnian rings, satellites, atmospheres, and Jovian atmosphere.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.co-s-uvis-2-ssb-v1.1_riuy-gehp",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "atlas",
                 "titan",
@@ -1309337,1556 +1309339,1568 @@
                 "cassini-huygens",
                 "calypso"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=CO-S-UVIS-2-SSB-V1.1",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.co-s-uvis-2-ssb-v1.1_riuy-gehp",
-            "description": "Photometric observations of stellar occultations by Saturnian rings, satellites, atmospheres, and Jovian atmosphere.",
-            "title": "CASSINI SATURN UVIS SOLAR STELLAR BRIGHTNESS TIME SERIES 1.1",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "CASSINI SATURN UVIS SOLAR STELLAR BRIGHTNESS TIME SERIES 1.1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-X-RPCMAG-2-CR5-RAW-V3.0",
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
-                "checkout"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This dataset contains EDITED RAW data of the CRUISE 5 phase (CR5).",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-x-rpcmag-2-cr5-raw-v3.0_rizn-9nnw",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "checkout"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-X-RPCMAG-2-CR5-RAW-V3.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-x-rpcmag-2-cr5-raw-v3.0_rizn-9nnw",
-            "description": "This dataset contains EDITED RAW data of the CRUISE 5 phase (CR5).",
-            "title": "ROSETTA-ORBITER CHECK RPCMAG 2 CR5 RAW V3.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER CHECK RPCMAG 2 CR5 RAW V3.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RL-CAL-ROMAP-3-PHC-SPM-V1.0",
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
+            "description": "This archive contains calibrated data (CDMAC level 3) from the ROMAP SPM instrument onboard ROSETTA Lander, acquired during the PHC (Post Hibernation Commissioning) phase. It also contains documentation which describes the ROMAP experiment. The data archived in this data set conform to the Planetary Data System (PDS) Standards, Version 3.6.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.rl-cal-romap-3-phc-spm-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "calibration"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RL-CAL-ROMAP-3-PHC-SPM-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.rl-cal-romap-3-phc-spm-v1.0",
-            "description": "This archive contains calibrated data (CDMAC level 3) from the ROMAP SPM instrument onboard ROSETTA Lander, acquired during the PHC (Post Hibernation Commissioning) phase. It also contains documentation which describes the ROMAP experiment. The data archived in this data set conform to the Planetary Data System (PDS) Standards, Version 3.6.",
-            "title": "ROSETTA-LANDER CAL ROMAP 3 PHC SPM V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-LANDER CAL ROMAP 3 PHC SPM V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-VIRTIS-2-EXT2-MTP029-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This release contains the digital numbers (DN) contained in the telemetry (TM) packages of the VIRTIS instrument on board of the spacecraft Rosetta. This volume contains data at the vicinity of comet 67P, from the EXTENSION 2 MTP029 phase, which occurred from 2016-05-04 to 2016-06-01",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-virtis-2-ext2-mtp029-v1.0",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2021-05-21",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "vega",
                 "international rosetta mission",
                 "67p/churyumov-gerasimenko 1 (1969 r1)"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-VIRTIS-2-EXT2-MTP029-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-virtis-2-ext2-mtp029-v1.0",
-            "description": "This release contains the digital numbers (DN) contained in the telemetry (TM) packages of the VIRTIS instrument on board of the spacecraft Rosetta. This volume contains data at the vicinity of comet 67P, from the EXTENSION 2 MTP029 phase, which occurred from 2016-05-04 to 2016-06-01",
-            "title": "ROSETTA-ORBITER 67P VIRTIS 2 EXTENSION 2 MTP029 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P VIRTIS 2 EXTENSION 2 MTP029 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/SeaBASS/ECOMON/DATA001",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/GSFC/SED/ESD/GCDC/OB.DAAC. https://doi.org/10.5067/SeaBASS/ECOMON/DATA001.",
-            "issued": "2013-02-10",
-            "temporal": "2013-02-10T00:00:02Z/2023-04-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-04-06",
-            "keyword": [
-                "ocean optics",
-                "ocean temperature",
-                "salinity/density",
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
-            "identifier": "C1633360223-OB_DAAC",
             "description": "EcoMon is the NOAA Northeast Fisheries Science Center Ecosystem Monitoring program for the Northeast U.S. continental shelf. EcoMon main objective is hydrography and zooplankton sampling along the Mid-Atlantic and New England coasts . Funding for the project was provided by the NOAA JPSS PGRR program (https://www.nesdis.noaa.gov/current-satellite-missions/currently-flying/joint-polar-satellite-system/proving-grounds). Additional information for this project can be found in Turner et al., 2021 (https://www.sciencedirect.com/science/article/abs/pii/S0034425721004491).",
-            "title": "NOAA Fisheries Ecosystem Monitoring Program",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSeaBASS%2FECOMON%2FDATA001",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSeaBASS%2FECOMON%2FDATA001",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://seabass.gsfc.nasa.gov/experiment/ECOMON/",
-                    "description": "Detailed information about the SeaBASS Experiment such as cruises, funding, and investigators",
                     "@type": "dcat:Distribution",
+                    "description": "Detailed information about the SeaBASS Experiment such as cruises, funding, and investigators",
+                    "downloadURL": "https://seabass.gsfc.nasa.gov/experiment/ECOMON/",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 }
             ],
+            "identifier": "C1633360223-OB_DAAC",
+            "issued": "2013-02-10",
+            "keyword": [
+                "ocean optics",
+                "ocean temperature",
+                "salinity/density",
+                "oceans",
+                "ocean chemistry",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/SeaBASS/ECOMON/DATA001",
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
+            "temporal": "2013-02-10T00:00:02Z/2023-04-17T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "NOAA Fisheries Ecosystem Monitoring Program"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/SDRON-NOPP0",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Saildrone. 2020-05-20. Saildrone Arctic field campaign surface and ADCP measurements for NOPP-MISST project. Version 1.0. Saildrone Arctic NOPP-MISST Field Campaign Products. Saildrone Inc. 1050 W Tower Ave, Alameda, CA 94501. Archived by National Aeronautics and Space Administration, U.S. Government, Saildrone Inc. https://doi.org/10.5067/SDRON-NOPP0. http://podaac.jpl.nasa.gov/saildrone. Saildrone, Saildrone Inc, 2020-05-20, Saildrone Arctic field campaign surface and ADCP measurements for NOPP-MISST project, http://podaac.jpl.nasa.gov/saildrone.",
-            "issued": "2019-05-08",
-            "temporal": "2019-05-14T18:00:00Z/2019-10-11T18:30:01Z",
-            "@type": "dcat:Dataset",
-            "modified": "2019-05-08",
-            "keyword": [
-                "atmosphere",
-                "atmospheric temperature",
-                "salinity/density",
-                "atmospheric pressure",
-                "ocean chemistry",
-                "ocean optics",
-                "atmospheric winds",
-                "oceans",
-                "earth science",
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
-            "identifier": "C2491772160-POCLOUD",
-            "description": "Saildrone is a wind and solar powered unmanned surface vehicle (USV) capable of long distance deployments lasting up to 12 months and providing high quality, near real-time, multivariate surface ocean and atmospheric observations while transiting at typical speeds of 3-5 knots. The drone is autonomous in that it may be guided remotely from land while being completely wind driven. The saildrone Arctic campaign involved the deployment of a fleet of 5 saildrones, jointly funded by NASA and NOAA, from Dutch Harbor, Alaska, within the Bering and Chukchi Seas to the ice edge and back over a 150-day period from 15 May 2019 to 11 October 2019. Scientific objectives include collecting upper ocean temperature profiles with a full suite of ocean measurements, which could lead to significant improvements in modeling of diurnal warming. Additionally, these new data will provide additional Arctic SST observations to benefit SST algorithm development and validation, and collected additional data for studies of air- sea-ice interactions.  For the Arctic cruises, saildrones were equipped with a suite of instruments that included a CTD, IR pyrometer, fluorometer, dissolved oxygen sensor, anemometer, barometer, and Acoustic Doppler Current Profiler (ADCP).  Additionally, four temperature data loggers were positioned vertically along hull to provide further information on thermal variability near the ocean surface. This Saildrone Arctic dataset is comprised of 3 data files for each of the two NASA-funded saildrones deployed.  The one file type contains saildrone platform telemetry and near-surface observational data (air temperature, sea surface skin and bulk temperatures, salinity, oxygen and chlorophyll-a concentrations, barometric pressure, wind speed and direction) spanning the entire cruise at 1 minute temporal resolution. The second file type contains the ADCP current vector data for each of the deployed saildrones that is depth-resolved to 100m at 2m intervals and binned temporally at 1 minute resolution.  The third file type, contains the temperature logger measurement data previously described.  All data files are in netCDF format and CF/ACDD compliant consistent with the NOAA/NCEI specification.",
-            "release-place": "Saildrone Inc. 1050 W Tower Ave, Alameda, CA 94501",
-            "series-name": "Saildrone Arctic field campaign surface and ADCP measurements for NOPP-MISST project",
-            "graphic-preview-description": "Thumbnail",
             "creator": "Saildrone",
-            "title": "Saildrone Arctic field campaign surface and ADCP measurements for NOPP-MISST project",
-            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/SAILDRONE_ARCTIC.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "Saildrone is a wind and solar powered unmanned surface vehicle (USV) capable of long distance deployments lasting up to 12 months and providing high quality, near real-time, multivariate surface ocean and atmospheric observations while transiting at typical speeds of 3-5 knots. The drone is autonomous in that it may be guided remotely from land while being completely wind driven. The saildrone Arctic campaign involved the deployment of a fleet of 5 saildrones, jointly funded by NASA and NOAA, from Dutch Harbor, Alaska, within the Bering and Chukchi Seas to the ice edge and back over a 150-day period from 15 May 2019 to 11 October 2019. Scientific objectives include collecting upper ocean temperature profiles with a full suite of ocean measurements, which could lead to significant improvements in modeling of diurnal warming. Additionally, these new data will provide additional Arctic SST observations to benefit SST algorithm development and validation, and collected additional data for studies of air- sea-ice interactions.  For the Arctic cruises, saildrones were equipped with a suite of instruments that included a CTD, IR pyrometer, fluorometer, dissolved oxygen sensor, anemometer, barometer, and Acoustic Doppler Current Profiler (ADCP).  Additionally, four temperature data loggers were positioned vertically along hull to provide further information on thermal variability near the ocean surface. This Saildrone Arctic dataset is comprised of 3 data files for each of the two NASA-funded saildrones deployed.  The one file type contains saildrone platform telemetry and near-surface observational data (air temperature, sea surface skin and bulk temperatures, salinity, oxygen and chlorophyll-a concentrations, barometric pressure, wind speed and direction) spanning the entire cruise at 1 minute temporal resolution. The second file type contains the ADCP current vector data for each of the deployed saildrones that is depth-resolved to 100m at 2m intervals and binned temporally at 1 minute resolution.  The third file type, contains the temperature logger measurement data previously described.  All data files are in netCDF format and CF/ACDD compliant consistent with the NOAA/NCEI specification.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSDRON-NOPP0",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSDRON-NOPP0",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://podaac.jpl.nasa.gov/saildrone",
-                    "description": "Field Campaign and Instrument Overview",
                     "@type": "dcat:Distribution",
+                    "description": "Field Campaign and Instrument Overview",
+                    "downloadURL": "http://podaac.jpl.nasa.gov/saildrone",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/insitu/open/L2/saildrone/docs/2018_04_Saildrone_Cruise_Report.pdf",
-                    "description": "Cruise Report, Data Submission Report, Instrument Calibration Report",
                     "@type": "dcat:Distribution",
+                    "description": "Cruise Report, Data Submission Report, Instrument Calibration Report",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/insitu/open/L2/saildrone/docs/2018_04_Saildrone_Cruise_Report.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/SAILDRONE_ARCTIC.jpg",
-                    "description": "Thumbnail",
                     "@type": "dcat:Distribution",
+                    "description": "Thumbnail",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/SAILDRONE_ARCTIC.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.saildrone.com/",
-                    "description": "Saildrone Website",
                     "@type": "dcat:Distribution",
+                    "description": "Saildrone Website",
+                    "downloadURL": "https://www.saildrone.com/",
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
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2491772160-POCLOUD",
-                    "description": "HTTPS endpoint for data browse and download",
                     "@type": "dcat:Distribution",
+                    "description": "HTTPS endpoint for data browse and download",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2491772160-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2491772160-POCLOUD",
-                    "description": "Browse granule search results in Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse granule search results in Earthdata Search",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2491772160-POCLOUD",
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
+            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/SAILDRONE_ARCTIC.jpg",
+            "identifier": "C2491772160-POCLOUD",
+            "issued": "2019-05-08",
+            "keyword": [
+                "atmosphere",
+                "atmospheric temperature",
+                "salinity/density",
+                "atmospheric pressure",
+                "ocean chemistry",
+                "ocean optics",
+                "atmospheric winds",
+                "oceans",
+                "earth science",
+                "ocean temperature"
+            ],
+            "landingPage": "https://doi.org/10.5067/SDRON-NOPP0",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2019-05-08",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/JPL/PODAAC"
+            },
+            "release-place": "Saildrone Inc. 1050 W Tower Ave, Alameda, CA 94501",
+            "series-name": "Saildrone Arctic field campaign surface and ADCP measurements for NOPP-MISST project",
             "spatial": "-168.7 53.8 -146.1 75.5",
+            "temporal": "2019-05-14T18:00:00Z/2019-10-11T18:30:01Z",
             "theme": [
                 "NOPP_MISST",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Saildrone Arctic field campaign surface and ADCP measurements for NOPP-MISST project"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/QN80TO7ZHFJZ",
             "citation": "Beaudoing, H. and M. Rodell, NASA/GSFC/HSL. 2019-11-19. GLDAS_NOAH10_M. Version 2.0. GLDAS Noah Land Surface Model L4 monthly 1.0 x 1.0 degree V2.0. Greenbelt, Maryland, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/QN80TO7ZHFJZ. https://disc.gsfc.nasa.gov/datacollection/GLDAS_NOAH10_M_2.0.html. Digital Science Data.",
-            "issued": "2019-11-19",
-            "temporal": "1948-01-01T00:00:00Z/2014-12-31T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2019-11-19",
-            "references": [
-                "https://doi.org/10.1175/BAMS-85-3-381"
-            ],
-            "keyword": [
-                "land surface",
-                "terrestrial hydrosphere",
-                "surface water",
-                "surface thermal properties",
-                "soils",
-                "snow/ice",
-                "precipitation",
-                "atmosphere",
-                "atmospheric pressure",
-                "atmospheric radiation",
-                "atmospheric temperature",
-                "atmospheric water vapor",
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
-            "identifier": "C1233767575-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "NASA Global Land Data Assimilation System Version 2 (GLDAS-2) has three components: GLDAS-2.0, GLDAS-2.1, and GLDAS-2.2. GLDAS-2.0 is forced entirely with the Princeton meteorological forcing input data and provides a temporally consistent series from 1948 through 2014. GLDAS-2.1 is forced with a combination of model and observation data from 2000 to present. GLDAS-2.2 product suites use data assimilation (DA), whereas the GLDAS-2.0 and GLDAS-2.1 products are \"open-loop\" (i.e., no data assimilation). The choice of forcing data, as well as DA observation source, variable, and scheme, vary for different GLDAS-2.2 products.\n\nThis data product, GLDAS-2.0 1.0 degree monthly, was reprocessed and replaced its previous data product on November 19, 2019.  The data product was generated through temporal averaging of the reprocessed 3-hourly data, contains a series of land surface parameters simulated from the Noah Model 3.6, and currently covers from January 1948 to December 2014, but will be extended as the data becomes available.  The GLDAS-2.0 data are archived and distributed in netCDF format.\n\nThe GLDAS-2.0 model simulations were initialized on simulation date January 1, 1948, using soil moisture and other state fields from the LSM climatology for that day of the year. The simulations were forced by the global meteorological forcing data set from Princeton University (Sheffield et al., 2006). Each simulation uses the common GLDAS data sets for land water mask (MOD44W: Carroll et al., 2009) and elevation (GTOPO30) along with the model default land cover and soils datasets. Noah model uses the Modified IGBP MODIS 20-category vegetation classification and the soil texture based on the Hybrid STATSGO/FAO) datasets. The MODIS based land surface parameters are used in the current GLDAS-2.0 and GLDAS-2.1 products while the AVHRR base parameters were used in GLDAS-1 and previous GLDAS-2 products (prior to October 2012).  The land mask was modified to accommodate the river routing scheme included in the simulations in the fall 2019 update.  \n\nIn October 2020, all 3-hourly and monthly GLDAS-2 data were post-processed with the MOD44W MODIS land mask.  Previously, some grid boxes over inland water were considered as over land and, thus, had non-missing values.  The post-processing corrected this issue and masked out all model output data over inland water; the post-processing did not affect the meteorological forcing variables. More information can be found in the GLDAS-2 README.  The MOD44W MODIS land mask is available on the GLDAS Project site.\n\nIf you had downloaded the GLDAS data prior to November 2020, please download the data again to receive the post-processed data.",
-            "release-place": "Greenbelt, Maryland, USA",
-            "series-name": "GLDAS_NOAH10_M",
-            "creator": "Beaudoing, H. and M. Rodell, NASA/GSFC/HSL",
-            "graphic-preview-description": "GLDAS-2.0 Noah monthly 1.0 degree 0 - 10 cm soil moisture content [kg m-2] for Jan. 1948.",
-            "title": "GLDAS Noah Land Surface Model L4 monthly 1.0 x 1.0 degree V2.0 (GLDAS_NOAH10_M) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/GLDAS_NOAH10_M_2.0.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FQN80TO7ZHFJZ",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FQN80TO7ZHFJZ",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/GLDAS_NOAH10_M_2.0.png",
-                    "description": "GLDAS-2.0 Noah monthly 1.0 degree 0 - 10 cm soil moisture content [kg m-2] for Jan. 1948.",
                     "@type": "dcat:Distribution",
+                    "description": "GLDAS-2.0 Noah monthly 1.0 degree 0 - 10 cm soil moisture content [kg m-2] for Jan. 1948.",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/GLDAS_NOAH10_M_2.0.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/GLDAS_NOAH10_M_2.0.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/GLDAS_NOAH10_M_2.0.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://hydro1.gesdisc.eosdis.nasa.gov/data/GLDAS/GLDAS_NOAH10_M.2.0/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://hydro1.gesdisc.eosdis.nasa.gov/data/GLDAS/GLDAS_NOAH10_M.2.0/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=GLDAS_NOAH10_M_2.0",
-                    "description": "Use the Earthdata Search Client (EDSC) to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search Client (EDSC) to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=GLDAS_NOAH10_M_2.0",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://hydro1.gesdisc.eosdis.nasa.gov/opendap/hyrax/GLDAS/GLDAS_NOAH10_M.2.0/",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://hydro1.gesdisc.eosdis.nasa.gov/opendap/hyrax/GLDAS/GLDAS_NOAH10_M.2.0/",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://hydro1.gesdisc.eosdis.nasa.gov/dods/GLDAS_NOAH10_M.2.0/",
-                    "description": "The GrADS Data Server (GDS) is another form of OPeNDAP that provides subsetting and some analysis services across the Internet.",
                     "@type": "dcat:Distribution",
+                    "description": "The GrADS Data Server (GDS) is another form of OPeNDAP that provides subsetting and some analysis services across the Internet.",
+                    "downloadURL": "https://hydro1.gesdisc.eosdis.nasa.gov/dods/GLDAS_NOAH10_M.2.0/",
+                    "mediaType": "text/html",
                     "title": "Use GRADS DATA SERVER (GDS) to access the dataset's data"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://hydro1.gesdisc.eosdis.nasa.gov/data/GLDAS/GLDAS_NOAH10_M.2.0/doc/README_GLDAS2.pdf",
-                    "description": "README Document",
                     "@type": "dcat:Distribution",
+                    "description": "README Document",
+                    "downloadURL": "https://hydro1.gesdisc.eosdis.nasa.gov/data/GLDAS/GLDAS_NOAH10_M.2.0/doc/README_GLDAS2.pdf",
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
-                    "downloadURL": "https://hydro1.gesdisc.eosdis.nasa.gov/thredds/catalog/GLDAS_aggregation/GLDAS_NOAH10_M.2.0/catalog.html",
-                    "description": "Time aggregated THREDDS Data Server (TDS)",
                     "@type": "dcat:Distribution",
+                    "description": "Time aggregated THREDDS Data Server (TDS)",
+                    "downloadURL": "https://hydro1.gesdisc.eosdis.nasa.gov/thredds/catalog/GLDAS_aggregation/GLDAS_NOAH10_M.2.0/catalog.html",
+                    "mediaType": "text/html",
                     "title": "Use THREDDS DATA to download the dataset's data"
                 }
             ],
+            "graphic-preview-description": "GLDAS-2.0 Noah monthly 1.0 degree 0 - 10 cm soil moisture content [kg m-2] for Jan. 1948.",
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/GLDAS_NOAH10_M_2.0.png",
+            "identifier": "C1233767575-GES_DISC",
+            "issued": "2019-11-19",
+            "keyword": [
+                "land surface",
+                "terrestrial hydrosphere",
+                "surface water",
+                "surface thermal properties",
+                "soils",
+                "snow/ice",
+                "precipitation",
+                "atmosphere",
+                "atmospheric pressure",
+                "atmospheric radiation",
+                "atmospheric temperature",
+                "atmospheric water vapor",
+                "atmospheric winds",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/QN80TO7ZHFJZ",
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
+            "series-name": "GLDAS_NOAH10_M",
             "spatial": "-180.0 -60.0 180.0 90.0",
+            "temporal": "1948-01-01T00:00:00Z/2014-12-31T23:59:59.999Z",
             "theme": [
                 "GLDAS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "GLDAS Noah Land Surface Model L4 monthly 1.0 x 1.0 degree V2.0 (GLDAS_NOAH10_M) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-2-ESC2-67PCHURYUMOV-M15-V1.0",
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
+            "description": "This data set contains raw EDR images acquired by the OSIRIS Wide Angle\nCamera during the escort phase of the Rosetta mission at the comet 67P,\ncovering the period from 2015-04-08 to 2015-05-05.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-2-esc2-67pchuryumov-m15-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-2-ESC2-67PCHURYUMOV-M15-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-2-esc2-67pchuryumov-m15-v1.0",
-            "description": "This data set contains raw EDR images acquired by the OSIRIS Wide Angle\nCamera during the escort phase of the Rosetta mission at the comet 67P,\ncovering the period from 2015-04-08 to 2015-05-05.",
-            "title": "ROSETTA-ORBITER COMET ESCORT OSIWAC 2 EDR MTP 015 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER COMET ESCORT OSIWAC 2 EDR MTP 015 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/TRMM/CERES/ES9-PFM_L3.002",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2000-06-30. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/TRMM/CERES/ES9-PFM_L3.002.",
-            "issued": "2014-02-11",
-            "temporal": "1998-01-01T00:00:00Z/2000-03-31T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2015-09-29",
-            "keyword": [
-                "atmospheric radiation",
-                "earth science",
-                "atmosphere"
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
-            "identifier": "C7747951-LARC_ASDC",
             "description": "CER_ES9_TRMM-PFM_Edition2 is the Clouds and the Earth's Radiant Energy System (CERES) Earth Radiation Budget Experiment (ERBE)-like Monthly Regional Averages Tropical Rainfall Measuring Mission (TRMM) protoflight model (PFM) Edition 2 data product. Data for this product was collected by the CERES-PFM on the Tropical Rainfall Measuring Mission (TRMM) platform. Data collection for this product is complete. \r\n\r\nCER_ES9_TRMM-PFM_Edition2 data are CERES instrument Top-of-the-Atmosphere (TOA) fluxes that used algorithms identical to those used by ERBE, regional averages of instantaneous footprint TOA fluxes only for the hours of satellite overpass (from ES-8 Level 2 product). The ERBE-like Monthly Regional Averages (ES-9) product contains a month of space and time averaged CERES data for a single scanner instrument. The ES-9 is also produced for combinations of scanner instruments. All instantaneous shortwave and long-wave (LW) fluxes at the TOA from the CERES ES-8 product for a month are sorted by 2.5-degree spatial regions, by day number, and by the local hour of observation. The mean of the instantaneous fluxes for a given region-day-hour bin is determined and recorded on the ES-9 along with other flux statistics and scene information. For each region, the daily average flux is estimated from an algorithm that uses the available hourly data, scene identification data, and diurnal models. This algorithm is like the algorithm used for the ERBE. The ES-9 also contains hourly average fluxes for the month and an overall monthly average for each region. These average fluxes are given for both clear-sky and total-sky scenes. \r\n\r\nCERES is a key component of the Earth Observing System (EOS) program. The CERES instruments provide radiometric measurements of the Earth's atmosphere from three broadband channels. The CERES missions are a follow-on to the successful ERBE mission. The first CERES instrument, PFM, was launched on November 27, 1997 as part of the TRMM. Two CERES instruments (FM1 and FM2) were launched into polar orbit on board the Earth Observing System (EOS) flagship Terra on December 18, 1999. Two additional CERES instruments (FM3 and FM4) were launched on board Earth Observing System (EOS) Aqua on May 4, 2002. The CERES FM5 instrument was launched on board the Suomi National Polar-orbiting Partnership (NPP) satellite on October 28, 2011. The newest CERES instrument (FM6) was launched on board the Joint Polar-Orbiting Satellite System 1 (JPSS-1) satellite, now called NOAA-20, on November 18, 2017.",
-            "title": "CERES ERBE-like Monthly Regional Averages TRMM PFM Edition2",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FTRMM%2FCERES%2FES9-PFM_L3.002",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FTRMM%2FCERES%2FES9-PFM_L3.002",
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
-                    "downloadURL": "https://doi.org/10.5067/TRMM/CERES/ES9-PFM_L3.002",
-                    "description": "DOI data set landing page for CER_ES9_TRMM-PFM_Edition2",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for CER_ES9_TRMM-PFM_Edition2",
+                    "downloadURL": "https://doi.org/10.5067/TRMM/CERES/ES9-PFM_L3.002",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C7747951-LARC_ASDC",
-                    "description": "Earthdata Search for CER_ES9_TRMM-PFM_Edition2 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for CER_ES9_TRMM-PFM_Edition2 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C7747951-LARC_ASDC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
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
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/ceres/quality_summaries/CER_ES9_TRMM-PFM_Edition2.pdf",
-                    "description": "Quality Summary: CERES ES9 TRMM-PFM Edition 2",
                     "@type": "dcat:Distribution",
+                    "description": "Quality Summary: CERES ES9 TRMM-PFM Edition 2",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/ceres/quality_summaries/CER_ES9_TRMM-PFM_Edition2.pdf",
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
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/CERES/ES9/TRMM-PFM_Edition2/",
-                    "description": "ASDC Direct Data Download for CER_ES9_TRMM-PFM_Edition2",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for CER_ES9_TRMM-PFM_Edition2",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/CERES/ES9/TRMM-PFM_Edition2/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/CERES/ES9/TRMM-PFM_Edition2/contents.html",
-                    "description": "OPeNDAP data access for CER_ES9_TRMM-PFM_Edition2",
                     "@type": "dcat:Distribution",
+                    "description": "OPeNDAP data access for CER_ES9_TRMM-PFM_Edition2",
+                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/CERES/ES9/TRMM-PFM_Edition2/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 }
             ],
+            "identifier": "C7747951-LARC_ASDC",
+            "issued": "2014-02-11",
+            "keyword": [
+                "atmospheric radiation",
+                "earth science",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.5067/TRMM/CERES/ES9-PFM_L3.002",
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
             "spatial": "<?xml version=\"1.0\" encoding=\"UTF-8\"?><gml:Polygon xmlns:gml=\"http://www.opengis.net/gml/3.2\" srsName=\"EPSG:9825\"><gml:outerBoundaryIs><gml:LinearRing><gml:posList>-55.0 -180.0 -55.0 180.0 55.0 180.0 55.0 -180.0 -55.0 -180.0</gml:posList></gml:LinearRing></gml:outerBoundaryIs><gml:innerBoundaryIs></gml:innerBoundaryIs></gml:Polygon>",
+            "temporal": "1998-01-01T00:00:00Z/2000-03-31T23:59:59.999Z",
             "theme": [
                 "CERES",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "CERES ERBE-like Monthly Regional Averages TRMM PFM Edition2"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.7927/H4RF5RZT",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Global Footprint Network - GFN. 2006-12-31. Compendium of Environmental Sustainability Indicator Collections: 2006 National Footprint Accounts (NFA). Version 2006.00. Oakland, CA. Archived by National Aeronautics and Space Administration, U.S. Government, Global Footprint Network (GFN). https://doi.org/10.7927/H4RF5RZT. https://doi.org/10.7927/H4RF5RZT.",
-            "issued": "2006-12-31",
-            "temporal": "2003-01-01T00:00:00Z/2003-12-31T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2006-12-31",
-            "references": [
-                "https://doi.org/10.7927/H45H7D60",
-                "https://doi.org/10.7927/H4MS3QNT",
-                "https://doi.org/10.7927/H4B56GNC",
-                "https://doi.org/10.7927/H46D5QXN",
-                "https://doi.org/10.7927/H42N506Q"
-            ],
-            "keyword": [
-                "earth science",
-                "human dimensions",
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
-            "identifier": "C1418641019-SEDAC",
-            "description": "The 2006 National Footprint Accounts (NFA) portion of the Compendium of Environmental Sustainability Indicator Collections, version 1.1 is a data set that measures how much land and water area a human population requires to produce the resources it consumes and to absorb its wastes under prevailing technology and management. It includes Footprints for cropland, grazing land, carbon, nuclear, forest, built-up and fishing ground for 147 countries. It also identifies countries that are considered to have ecological deficits and reserves. These data are drawn from the National Footprint Accounts, 2006 Edition, produced by the Global Footprint Network and distributed by the Columbia University Center for International Earth Science Information Network (CIESIN).",
-            "release-place": "Oakland, CA",
-            "graphic-preview-description": "Sample browse graphic of the data set.",
             "creator": "Global Footprint Network - GFN",
-            "title": "Compendium of Environmental Sustainability Indicator Collections: 2006 National Footprint Accounts (NFA)",
-            "graphic-preview-file": "https://sedac.ciesin.columbia.edu/downloads/maps/cesic/cesic-national-footprint-accounts-2006/sedac-logo.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The 2006 National Footprint Accounts (NFA) portion of the Compendium of Environmental Sustainability Indicator Collections, version 1.1 is a data set that measures how much land and water area a human population requires to produce the resources it consumes and to absorb its wastes under prevailing technology and management. It includes Footprints for cropland, grazing land, carbon, nuclear, forest, built-up and fishing ground for 147 countries. It also identifies countries that are considered to have ecological deficits and reserves. These data are drawn from the National Footprint Accounts, 2006 Edition, produced by the Global Footprint Network and distributed by the Columbia University Center for International Earth Science Information Network (CIESIN).",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.7927%2FH4RF5RZT",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.7927%2FH4RF5RZT",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/downloads/maps/cesic/cesic-national-footprint-accounts-2006/sedac-logo.jpg",
-                    "description": "Sample browse graphic of the data set.",
                     "@type": "dcat:Distribution",
+                    "description": "Sample browse graphic of the data set.",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/downloads/maps/cesic/cesic-national-footprint-accounts-2006/sedac-logo.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/cesic-national-footprint-accounts-2006/data-download",
-                    "description": "Data Download Page",
                     "@type": "dcat:Distribution",
+                    "description": "Data Download Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/cesic-national-footprint-accounts-2006/data-download",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://sedac.ciesin.columbia.edu/data/set/cesic-national-footprint-accounts-2006/docs",
-                    "description": "Documentation Page",
                     "@type": "dcat:Distribution",
+                    "description": "Documentation Page",
+                    "downloadURL": "http://sedac.ciesin.columbia.edu/data/set/cesic-national-footprint-accounts-2006/docs",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/cesic-national-footprint-accounts-2006",
-                    "description": "Data Set\u00a0Overview Page",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set\u00a0Overview Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/cesic-national-footprint-accounts-2006",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "graphic-preview-description": "Sample browse graphic of the data set.",
+            "graphic-preview-file": "https://sedac.ciesin.columbia.edu/downloads/maps/cesic/cesic-national-footprint-accounts-2006/sedac-logo.jpg",
+            "identifier": "C1418641019-SEDAC",
+            "issued": "2006-12-31",
+            "keyword": [
+                "earth science",
+                "human dimensions",
+                "sustainability"
+            ],
+            "landingPage": "https://doi.org/10.7927/H4RF5RZT",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2006-12-31",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "SEDAC"
+            },
+            "references": [
+                "https://doi.org/10.7927/H45H7D60",
+                "https://doi.org/10.7927/H4MS3QNT",
+                "https://doi.org/10.7927/H4B56GNC",
+                "https://doi.org/10.7927/H46D5QXN",
+                "https://doi.org/10.7927/H42N506Q"
+            ],
+            "release-place": "Oakland, CA",
             "spatial": "-180.0 -55.0 180.0 90.0",
+            "temporal": "2003-01-01T00:00:00Z/2003-12-31T00:00:00Z",
             "theme": [
                 "CESIC",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Compendium of Environmental Sustainability Indicator Collections: 2006 National Footprint Accounts (NFA)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC3-1112-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 3 phase 2015-07-01 to 2015-10-21. It is a Global Gravity measurement at the comet 67P and covers the time 2015-10-19T02:56:30.000 to 2015-10-19T03:49:31.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc3-1112-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC3-1112-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc3-1112-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 3 phase 2015-07-01 to 2015-10-21. It is a Global Gravity measurement at the comet 67P and covers the time 2015-10-19T02:56:30.000 to 2015-10-19T03:49:31.000.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 3 1112 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 3 1112 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VEGA1-C-TNM-2-RDR-HALLEY-V1.0",
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
-                "vega 1"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "TUNDE-M consists of two particle telescopes: T1 is viewing at 55 deg to the east of the Sun, T2 looks at 90 deg to the east of the Sun, both in the ecliptic plane. The telescopes consist of two circular surface barrier semiconductor detectors with an Al layer of 15x10**-6 g/cm** coated on the front detector (A) and an anticoincidence scintillation detector MCP. Low energy electrons (below about 160 keV) were deflected with a magnet. Field of view (half cone): 25 deg. Geometric factor: 0.25 cm**2 sr. Particles stopping in the thin front detector were not identified (they are referred as ion channels), those reaching the thick detector were identified via the dE/E method.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vega1-c-tnm-2-rdr-halley-v1.0_rjdm-esku",
+            "issued": "2021-05-21",
+            "keyword": [
+                "halley",
+                "vega 1"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VEGA1-C-TNM-2-RDR-HALLEY-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vega1-c-tnm-2-rdr-halley-v1.0_rjdm-esku",
-            "description": "TUNDE-M consists of two particle telescopes: T1 is viewing at 55 deg to the east of the Sun, T2 looks at 90 deg to the east of the Sun, both in the ecliptic plane. The telescopes consist of two circular surface barrier semiconductor detectors with an Al layer of 15x10**-6 g/cm** coated on the front detector (A) and an anticoincidence scintillation detector MCP. Low energy electrons (below about 160 keV) were deflected with a magnet. Field of view (half cone): 25 deg. Geometric factor: 0.25 cm**2 sr. Particles stopping in the thin front detector were not identified (they are referred as ion channels), those reaching the thick detector were identified via the dE/E method.",
-            "title": "VEGA1 TUNDE-M ENERGETIC PARTICLE ANALYSER DATA V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "VEGA1 TUNDE-M ENERGETIC PARTICLE ANALYSER DATA V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RPCLAP-2-EXT2-MTP028-V1.0",
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
+            "description": "This data set contains\nEDITED data from Rosetta RPC-LAP, acquired during the ROSETTA\nEXTENSION 2 MTP028 mission phase. Comet C-G/67P was the primary target.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rpclap-2-ext2-mtp028-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RPCLAP-2-EXT2-MTP028-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rpclap-2-ext2-mtp028-v1.0",
-            "description": "This data set contains\nEDITED data from Rosetta RPC-LAP, acquired during the ROSETTA\nEXTENSION 2 MTP028 mission phase. Comet C-G/67P was the primary target.",
-            "title": "ROSETTA-ORBITER 67P RPCLAP 2\nEXT2 MTP028 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RPCLAP 2\nEXT2 MTP028 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/375",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Crill, P.M., and R.K. Varner. 1998. BOREAS TGB-01 CH4 Concentration and Flux Data from NSA Tower Sites. ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/375",
-            "issued": "2023-11-22",
-            "temporal": "1994-05-28T00:00:00Z/1996-10-22T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-11-28",
-            "keyword": [
-                "atmospheric pressure",
-                "atmosphere",
-                "atmospheric temperature",
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
-            "identifier": "C2808131256-ORNL_CLOUD",
             "description": "Contains CH4 tower flux data collected by BOREAS science group TGB01 in the Northern Study Area.",
-            "graphic-preview-description": "Browse Image",
-            "title": "BOREAS TGB-01 CH4 Concentration and Flux Data from NSA Tower Sites",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/boreas_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F375",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F375",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/boreas/TGB/tgb1cfd/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/boreas/TGB/tgb1cfd/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/BOREAS/guides/TGB01_CH4_TOWER.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/BOREAS/guides/TGB01_CH4_TOWER.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/375",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/375",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/msword",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TGB/tgb1cfd/comp/TGB01_CH4_TOWER.doc",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TGB/tgb1cfd/comp/TGB01_CH4_TOWER.doc",
+                    "mediaType": "application/msword",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TGB/tgb1cfd/comp/TGB01_CH4_TOWER.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TGB/tgb1cfd/comp/TGB01_CH4_TOWER.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TGB/tgb1cfd/comp/TGB01_CH4_TOWER.txt",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TGB/tgb1cfd/comp/TGB01_CH4_TOWER.txt",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TGB/tgb1cfd/comp/tgb1cfd.def",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TGB/tgb1cfd/comp/tgb1cfd.def",
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
+            "identifier": "C2808131256-ORNL_CLOUD",
+            "issued": "2023-11-22",
+            "keyword": [
+                "atmospheric pressure",
+                "atmosphere",
+                "atmospheric temperature",
+                "earth science",
+                "atmospheric chemistry"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/375",
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
             "spatial": "-98.63 55.85 -98.04 55.94",
+            "temporal": "1994-05-28T00:00:00Z/1996-10-22T23:59:59Z",
             "theme": [
                 "BOREAS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "BOREAS TGB-01 CH4 Concentration and Flux Data from NSA Tower Sites"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-X-SREM-2-EXT3-MTP034-V1.0",
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
+            "description": "This data set contains count rates (1/s) as measured by the Standard Radiation Environment Monitor (SREM) instrument on the Rosetta spacecraft, along with their standard deviations.  The primary target is comet 67P/Churyumov-Gerasimenko. These are CODMAC Level 2 Experiment Data Record data, and provide a measure of the radiation in the spacecraft environment during the Medium Term Plan 34 period of the EXTENSION 3 mission phase.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-x-srem-2-ext3-mtp034-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-X-SREM-2-EXT3-MTP034-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-x-srem-2-ext3-mtp034-v1.0",
-            "description": "This data set contains count rates (1/s) as measured by the Standard Radiation Environment Monitor (SREM) instrument on the Rosetta spacecraft, along with their standard deviations.  The primary target is comet 67P/Churyumov-Gerasimenko. These are CODMAC Level 2 Experiment Data Record data, and provide a measure of the radiation in the spacecraft environment during the Medium Term Plan 34 period of the EXTENSION 3 mission phase.",
-            "title": "ROSETTA-ORBITER 67P SREM 2 EXTENSION 3\n    MTP034 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P SREM 2 EXTENSION 3\n    MTP034 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=IHW-C-IRFCURV-3-EDR-HALLEY-V2.0",
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
-                "international halley watch"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This data set contains filter curves for all IR filters referenced in any of the data sets archived by the International Halley Watch (IHW) Infrared Studies Network (IRSN).",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ihw-c-irfcurv-3-edr-halley-v2.0_rjkf-4tt2",
+            "issued": "2021-05-21",
+            "keyword": [
+                "calibration",
+                "international halley watch"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=IHW-C-IRFCURV-3-EDR-HALLEY-V2.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ihw-c-irfcurv-3-edr-halley-v2.0_rjkf-4tt2",
-            "description": "This data set contains filter curves for all IR filters referenced in any of the data sets archived by the International Halley Watch (IHW) Infrared Studies Network (IRSN).",
-            "title": "IHW COMET HALLEY INFRARED FILTER MEASUREMENTS, V2.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "IHW COMET HALLEY INFRARED FILTER MEASUREMENTS, V2.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/2303",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Donatelli, C., and S. Fagherazzi. 2023. Delta-X: Delft3D Sediment Model, Site 294, Terrebonne Basin, MRD, Louisiana, USA. ORNL DAAC, Oak Ridge, Tennessee, USA. https://doi.org/10.3334/ORNLDAAC/2303",
-            "issued": "2024-02-02",
-            "temporal": "2021-03-25T00:00:00Z/2021-08-28T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-02-08",
-            "keyword": [
-                "solid earth",
-                "surface water",
-                "ecosystems",
-                "geomorphic landforms/processes",
-                "water quality/water chemistry",
-                "terrestrial hydrosphere",
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
-            "identifier": "C2857067302-ORNL_CLOUD",
             "description": "This dataset contains the Delft3D model of the intensive site 294 in the Terrebonne Basin along the Mississippi River Delta (MRD) in coastal Louisiana. Simulations cover the Delta-X Spring and Fall deployments in 2021 and include hydrodynamics and sediment transport. All files required to run the simulations are included. The model's output of water velocity and depth-averaged sediment concentrations are provided for both deployments. The dataset includes annual inorganic mass accumulation rates derived through modelling intra-annual variability in water levels and suspended sediment concentrations. The data are provided in netCDF format.",
-            "graphic-preview-description": "Satellite image of Terrebonne Bay, Louisiana, USA with location of Site 294. Inset shows bathymetry of this intensive site.",
-            "title": "Delta-X: Delft3D Sediment Model, Site 294, Terrebonne Basin, MRD, Louisiana, USA",
-            "graphic-preview-file": "https://daac.ornl.gov/DELTAX/guides/DeltaX_Delft3D_294_Terrebonne_Fig1.jpg",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F2303",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F2303",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/deltax/DeltaX_Delft3D_294_Terrebonne/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/deltax/DeltaX_Delft3D_294_Terrebonne/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/DELTAX/guides/DeltaX_Delft3D_294_Terrebonne.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/DELTAX/guides/DeltaX_Delft3D_294_Terrebonne.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/2303",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/2303",
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
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/deltax/DeltaX_Delft3D_294_Terrebonne/comp/DeltaX_Delft3D_294_Terrebonne.pdf",
-                    "description": "Delta-X: Delft3D Sediment Model, Site 294, Terrebonne Basin, MRD, Louisiana, USA: DeltaX_Delft3D_294_Terrebonne.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "Delta-X: Delft3D Sediment Model, Site 294, Terrebonne Basin, MRD, Louisiana, USA: DeltaX_Delft3D_294_Terrebonne.pdf",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/deltax/DeltaX_Delft3D_294_Terrebonne/comp/DeltaX_Delft3D_294_Terrebonne.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://daac.ornl.gov/DELTAX/guides/DeltaX_Delft3D_294_Terrebonne_Fig1.jpg",
-                    "description": "Satellite image of Terrebonne Bay, Louisiana, USA with location of Site 294. Inset shows bathymetry of this intensive site.",
                     "@type": "dcat:Distribution",
+                    "description": "Satellite image of Terrebonne Bay, Louisiana, USA with location of Site 294. Inset shows bathymetry of this intensive site.",
+                    "downloadURL": "https://daac.ornl.gov/DELTAX/guides/DeltaX_Delft3D_294_Terrebonne_Fig1.jpg",
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
+            "graphic-preview-description": "Satellite image of Terrebonne Bay, Louisiana, USA with location of Site 294. Inset shows bathymetry of this intensive site.",
+            "graphic-preview-file": "https://daac.ornl.gov/DELTAX/guides/DeltaX_Delft3D_294_Terrebonne_Fig1.jpg",
+            "identifier": "C2857067302-ORNL_CLOUD",
+            "issued": "2024-02-02",
+            "keyword": [
+                "solid earth",
+                "surface water",
+                "ecosystems",
+                "geomorphic landforms/processes",
+                "water quality/water chemistry",
+                "terrestrial hydrosphere",
+                "earth science",
+                "biosphere"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/2303",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2024-02-08",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "ORNL_DAAC"
+            },
             "spatial": "-90.95 29.41 -90.89 29.46",
+            "temporal": "2021-03-25T00:00:00Z/2021-08-28T23:59:59Z",
             "theme": [
                 "Delta-X",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Delta-X: Delft3D Sediment Model, Site 294, Terrebonne Basin, MRD, Louisiana, USA"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/MAPS_SRL1_COSEC_HDF",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "1999-07-19. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/MAPS_SRL1_COSEC_HDF.",
-            "issued": "1999-07-13",
-            "temporal": "1994-04-09T00:00:00Z/1994-04-19T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2018-02-06",
-            "keyword": [
-                "air quality",
-                "earth science",
-                "atmosphere",
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
-            "identifier": "C1536049391-LARC_ASDC",
             "description": "MAPS Overview The MAPS experiment measures the global distribution of carbon monoxide (CO) mixing ratios in the free troposphere. Because of MAPS' previous flights on board the Space Shuttle, Earth system scientists now know that carbon monoxide concentrations in the troposphere are highly variable around the planet, and that widespread burning in the South American Amazon Basin and southern cerrados, the African savannahs, and the Australian grasslands and ranches are major sources of carbon monoxide in the southern hemisphere and tropical troposphere.The 1994 flights of the MAPS experiment provided CO measurements that show seasonal changes in CO emissions, sources, transports, and chemistry.InstrumentThe MAPS instrument is based on a technique called gas filter radiometry. Thermal energy from the Earth passes through the atmosphere and enters the viewport of the downlooking MAPS instrument. Carbon monoxide and nitrous oxide (N2O) in the atmosphere produce unique absorption lines in the transmitted energy. The energy which enters the MAPS instrument is split into three beams. One beam passes through a cell containing CO and falls onto a detector. This CO gas cell acts as a filter for the effects of CO present in the middle troposphere. A second beam falls directly onto a detector without passing through any gas filter. The difference in the voltage of the signals from these two detectors can be used to determine the amount of CO present in the atmosphere at an altitude of 7-8 km. During the dedicated Earth-Observing Space Shuttle mission in 1994, MAPS measured the distribution of carbon monoxide in the middle troposphere to evaluate CO sources and chemistry, and to evaluate the seasonal and interannual variation of this key atmospheric trace gas. Interpretation of these measurements will help us to better understand the atmosphere and the consequences that human activities initiate in global climate change. A third beam of the incident energy passes through a cell containing N2O and falls onto a detector. This N2O gas cell acts as a filter for the effects of N2O present in the atmosphere. The global distribution of N2O is well known, so the N2O signal can be used to detect the presence of clouds in the field of view and to correct the simultaneous CO measurement for systematic errors in the data.SRL-1 Mission GoalsThe MAPS SRL-1 mission took place during Northern Hemisphere Spring when global biomass burning does not typically occur. Some burning may occur for the purpose of clearing the damaged and felled trees in the forests of North America after the rather severe winter. The goals of the MAPS SRL-1 mission are to provide a validated, near-global atlas of the distribution of tropospheric Carbon Monoxide during the mission, and to assess the health status of the MAPS instrument as the mission progresses.SL1 Summary High concentrations of carbon monoxide over the Northern Hemisphere can be seen in measurements made by the Measurement of Air Pollution from Space (MAPS) instrument. These April 1994 measurements, made from the Space Shuttle Endeavour (STS-59), show large sources of air pollution in the lower atmosphere (2 to 10 miles above the surface) over the industrialized Northern Hemisphere.The data that are available from MAPS SRL1 include a 5 by 5 degree gridded box (MAPS_SRL1_5X5_HDF) and a second by second data product (MAPS_SRL1_COSEC_HDF). These data sets are available from the Langley DAAC.",
-            "title": "Measurement of Air Pollution from Satellites (MAPS) Space Radar Laboratory - 1 (SRL1) Carbon Monoxide Second by Second data",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMAPS_SRL1_COSEC_HDF",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMAPS_SRL1_COSEC_HDF",
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
-                    "downloadURL": "https://doi.org/10.5067/MAPS_SRL1_COSEC_HDF",
-                    "description": "DOI data set landing page for MAPS_SRL1_COSEC_HDF_1",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for MAPS_SRL1_COSEC_HDF_1",
+                    "downloadURL": "https://doi.org/10.5067/MAPS_SRL1_COSEC_HDF",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1536049391-LARC_ASDC",
-                    "description": "Earthdata Search for MAPS_SRL1_COSEC_HDF_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for MAPS_SRL1_COSEC_HDF_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1536049391-LARC_ASDC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/maps/guide/base_maps_cosec_dataset.pdf",
-                    "description": "MAPS Second by Second Langley DAAC Data Set Document",
                     "@type": "dcat:Distribution",
+                    "description": "MAPS Second by Second Langley DAAC Data Set Document",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/maps/guide/base_maps_cosec_dataset.pdf",
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
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/maps/readme/readme_maps_srl1_cosec_hdf.txt",
-                    "description": "Readme Information about the MAPS sample read software and data files",
                     "@type": "dcat:Distribution",
+                    "description": "Readme Information about the MAPS sample read software and data files",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/maps/readme/readme_maps_srl1_cosec_hdf.txt",
+                    "mediaType": "text/html",
                     "title": "View this dataset's read me document"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/maps/read_software/compile_read_maps_cosec.txt",
-                    "description": "Script that compiles the C code necessary to read the following MAPS HDF data files: 1) MAPS_OSTA3_COSEC_HDF, 2) MAPS_SRL1_COSEC_HDF, 3) MAPS_SRL2_COSEC_HDF",
                     "@type": "dcat:Distribution",
+                    "description": "Script that compiles the C code necessary to read the following MAPS HDF data files: 1) MAPS_OSTA3_COSEC_HDF, 2) MAPS_SRL1_COSEC_HDF, 3) MAPS_SRL2_COSEC_HDF",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/maps/read_software/compile_read_maps_cosec.txt",
+                    "mediaType": "text/html",
                     "title": "View this dataset's science data product software documentation"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/maps/read_software/maps_cosec_read.c",
-                    "description": "Sample read program for MAPS_SRL1_COSEC_HDF, MAPS_SRL2_COSEC_HDF, and MAPS_OSTA3_COSEC_HDF - Direct File Download (.c)",
                     "@type": "dcat:Distribution",
+                    "description": "Sample read program for MAPS_SRL1_COSEC_HDF, MAPS_SRL2_COSEC_HDF, and MAPS_OSTA3_COSEC_HDF - Direct File Download (.c)",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/maps/read_software/maps_cosec_read.c",
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
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/MAPS/MAPS_SRL1_COSEC_HDF/",
-                    "description": "ASDC Direct Data Download for MAPS_SRL1_COSEC_HDF_1",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for MAPS_SRL1_COSEC_HDF_1",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/MAPS/MAPS_SRL1_COSEC_HDF/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/MAPS/MAPS_SRL1_COSEC_HDF/contents.html",
-                    "description": "OPeNDAP data access for MAPS_SRL1_COSEC_HDF_1",
                     "@type": "dcat:Distribution",
+                    "description": "OPeNDAP data access for MAPS_SRL1_COSEC_HDF_1",
+                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/MAPS/MAPS_SRL1_COSEC_HDF/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 }
             ],
+            "identifier": "C1536049391-LARC_ASDC",
+            "issued": "1999-07-13",
+            "keyword": [
+                "air quality",
+                "earth science",
+                "atmosphere",
+                "atmospheric chemistry"
+            ],
+            "landingPage": "https://doi.org/10.5067/MAPS_SRL1_COSEC_HDF",
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
+            "temporal": "1994-04-09T00:00:00Z/1994-04-19T23:59:59.999Z",
             "theme": [
                 "MAPS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Measurement of Air Pollution from Satellites (MAPS) Space Radar Laboratory - 1 (SRL1) Carbon Monoxide Second by Second data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewBundle.jsp?identifier=urn%3Anasa%3Apds%3Ahot_ion_atmos_escape&version=1.0",
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
-                "hot ion atmospheric escape data",
-                "crossection"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This bundle contains collated hot ion atmospheric escape data from multiple published sources",
+            "identifier": "urn:nasa:pds:hot_ion_atmos_escape",
+            "issued": "2021-05-21",
+            "keyword": [
+                "hot ion atmospheric escape data",
+                "crossection"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewBundle.jsp?identifier=urn%3Anasa%3Apds%3Ahot_ion_atmos_escape&version=1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:hot_ion_atmos_escape",
-            "description": "This bundle contains collated hot ion atmospheric escape data from multiple published sources",
-            "title": "Hot Ion Atmospheric Escape Data",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "Hot Ion Atmospheric Escape Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.nasa.gov/d/rjs4-kkmz",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "GeneLab Outreach",
+                "hasEmail": "mailto:genelab-outreach@lists.nasa.gov"
+            },
+            "description": "Aspergillus fumigatus is a saprophytic filamentous fungus that is ubiquitous outdoors (soil decaying vegetation) and indoors (hospitals simulated closed habitats etc.). A. fumigatus can adapt to various environmental conditions and form airborne conidia that are the inoculum for a variety of diseases (e.g. non- and invasive pulmonary infections allergic bronchopulmonary aspergillosis etc.) in immunocompromised hosts. In an on-going Microbial Observatory Experiments on the International Space Station (ISS) molecular phylogeny of several fungal isolates were characterized. Two strains ISSF 21 and IF1SW-F4 were isolated from the HEPA filter and the surface of the Cupola of the ISS respectively. Using primers targeting the internal transcribed spacers ITS1 and 2 both isolates were identified as A. fumigatus. The whole genome sequence analysis of ISSF 21 revealed increased number of single nucleotide polymorphisms (SNPs) when compared to the reference A. fumigatus 293. Knowing that A. fumigatus is an opportunistic pathogen and microgravity highly influences the antibiotic susceptibility and pathogenicity of microorganisms we examined pathogenicity of both ISS isolates using the zebrafish larval model. The space station isolates (ISSF-021 and IF1SW-F4) were more virulent than two clinical strains (Af293 and CEA10) whose pathogenicity was highly characterized. Here the whole genome sequences of ISSF-021 strain are being deposited.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "GeneLab Study Page",
+                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-68",
+                    "mediaType": "text/html",
+                    "title": "Microbial Observatory (ISS-MO): Draft Genome Sequence of two Aspergillus fumigatus Strains Isolated from the International Space Station"
+                }
+            ],
+            "identifier": "nasa_genelab_GLDS-68_rjs4-kkmz",
             "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
             "keyword": [
                 "sequence assembly",
                 "spaceflight",
@@ -1310900,68 +1310914,33 @@
                 "sample processing",
                 "nucleic acid sequencing"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "GeneLab Outreach",
-                "hasEmail": "mailto:genelab-outreach@lists.nasa.gov"
-            },
+            "landingPage": "https://data.nasa.gov/d/rjs4-kkmz",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "nasa_genelab_GLDS-68_rjs4-kkmz",
-            "description": "Aspergillus fumigatus is a saprophytic filamentous fungus that is ubiquitous outdoors (soil decaying vegetation) and indoors (hospitals simulated closed habitats etc.). A. fumigatus can adapt to various environmental conditions and form airborne conidia that are the inoculum for a variety of diseases (e.g. non- and invasive pulmonary infections allergic bronchopulmonary aspergillosis etc.) in immunocompromised hosts. In an on-going Microbial Observatory Experiments on the International Space Station (ISS) molecular phylogeny of several fungal isolates were characterized. Two strains ISSF 21 and IF1SW-F4 were isolated from the HEPA filter and the surface of the Cupola of the ISS respectively. Using primers targeting the internal transcribed spacers ITS1 and 2 both isolates were identified as A. fumigatus. The whole genome sequence analysis of ISSF 21 revealed increased number of single nucleotide polymorphisms (SNPs) when compared to the reference A. fumigatus 293. Knowing that A. fumigatus is an opportunistic pathogen and microgravity highly influences the antibiotic susceptibility and pathogenicity of microorganisms we examined pathogenicity of both ISS isolates using the zebrafish larval model. The space station isolates (ISSF-021 and IF1SW-F4) were more virulent than two clinical strains (Af293 and CEA10) whose pathogenicity was highly characterized. Here the whole genome sequences of ISSF-021 strain are being deposited.",
-            "title": "Microbial Observatory (ISS-MO): Draft Genome Sequence of two Aspergillus fumigatus Strains Isolated from the International Space Station",
-            "programCode": [
-                "026:005"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-68",
-                    "description": "GeneLab Study Page",
-                    "@type": "dcat:Distribution",
-                    "title": "Microbial Observatory (ISS-MO): Draft Genome Sequence of two Aspergillus fumigatus Strains Isolated from the International Space Station"
-                }
-            ],
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "Microbial Observatory (ISS-MO): Draft Genome Sequence of two Aspergillus fumigatus Strains Isolated from the International Space Station"
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
-                "grs",
-                "spice",
-                "themis",
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
-            "identifier": "NASA-681",
             "description": "GRS, THEMIS, SPICE",
-            "title": "PDS Odyssey Data Release 18",
-            "programCode": [
-                "026:005"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -1310969,56 +1310948,44 @@
                     "mediaType": "application/html"
                 }
             ],
-            "accrualPeriodicity": "irregular",
+            "identifier": "NASA-681",
+            "issued": "2018-06-25",
+            "keyword": [
+                "grs",
+                "spice",
+                "themis",
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
+            "title": "PDS Odyssey Data Release 18"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://www.nasa.gov/centers/kennedy/launchingrockets/archives/2008.html",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2008-01-01",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
-            "references": [
-                "http://www.nasa.gov/centers/kennedy/launchingrockets/archives/elv_archive-index.html"
-            ],
-            "keyword": [
-                "delta",
-                "launch",
-                "landing",
-                "jason",
-                "ostm",
-                "pegasus",
-                "schedule",
-                "support",
-                "ibex",
-                "time",
-                "vehicle",
-                "mission",
-                "history",
-                "glast",
-                "expedition",
-                "earth's bridge to space"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Brian Dunbar",
                 "hasEmail": "mailto:brian.dunbar@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Aeronautics and Space Administration"
-            },
-            "identifier": "NASA-926",
             "description": "A list of launch vehicles launched for NASA missions in 2008.",
-            "title": "NASA Expendable Launch Vehicle Launch Archive 2008",
-            "programCode": [
-                "026:046"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -1311051,179 +1311018,190 @@
                     "mediaType": "application/html"
                 }
             ],
-            "accrualPeriodicity": "irregular",
+            "identifier": "NASA-926",
+            "issued": "2008-01-01",
+            "keyword": [
+                "delta",
+                "launch",
+                "landing",
+                "jason",
+                "ostm",
+                "pegasus",
+                "schedule",
+                "support",
+                "ibex",
+                "time",
+                "vehicle",
+                "mission",
+                "history",
+                "glast",
+                "expedition",
+                "earth's bridge to space"
+            ],
+            "landingPage": "http://www.nasa.gov/centers/kennedy/launchingrockets/archives/2008.html",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:046"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Aeronautics and Space Administration"
+            },
+            "references": [
+                "http://www.nasa.gov/centers/kennedy/launchingrockets/archives/elv_archive-index.html"
+            ],
             "theme": [
                 "Management/Operations"
-            ]
+            ],
+            "title": "NASA Expendable Launch Vehicle Launch Archive 2008"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewBundle.jsp?identifier=urn%3Anasa%3Apds%3Amer1_pancam_sci_derived_iof&version=1.0",
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
+            "description": "This bundle contains derived IOF data from the Panoramic Cameras (Pancam) on Mars Exploration Rover 1 (Opportunity). These data were produced by the science team.",
+            "identifier": "urn:nasa:pds:mer1_pancam_sci_derived_iof",
+            "issued": "2021-05-21",
+            "keyword": [
+                "mars",
+                "mars exploration rover"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewBundle.jsp?identifier=urn%3Anasa%3Apds%3Amer1_pancam_sci_derived_iof&version=1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:mer1_pancam_sci_derived_iof",
-            "description": "This bundle contains derived IOF data from the Panoramic Cameras (Pancam) on Mars Exploration Rover 1 (Opportunity). These data were produced by the science team.",
-            "title": "MER1 Pancam Science Derived IOF Data Bundle",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "MER1 Pancam Science Derived IOF Data Bundle"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.7927/H4BP00QC",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Wildlife Conservation Society - WCS, and Center for International Earth Science Information Network - CIESIN - Columbia University. 2005-12-31. Last of the Wild Project, Version 2, 2005 (LWP-2): Global Human Influence Index (HII) Dataset (Geographic). Version 2.00. Palisades, NY. Archived by National Aeronautics and Space Administration, U.S. Government, Socioeconomic Data and Applications Center (SEDAC), Columbia University. https://doi.org/10.7927/H4BP00QC. https://doi.org/10.7927/H4BP00QC.",
-            "issued": "2005-12-31",
-            "temporal": "1995-01-01T00:00:00Z/2004-12-31T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2005-12-31",
-            "references": [
-                "https://doi.org/10.7927/H4M61H5F",
-                "https://doi.org/10.7927/H4GF0RFQ",
-                "https://doi.org/10.7927/H4348H83",
-                "https://doi.org/10.7927/H4ZC80SS",
-                "https://doi.org/10.7927/H46W980H"
-            ],
-            "keyword": [
-                "land surface",
-                "ecosystems",
-                "earth science",
-                "land use/land cover",
-                "biosphere"
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
-            "identifier": "C179001808-SEDAC",
-            "description": "The Global Human Influence Index Dataset of the Last of the Wild Project, Version 2, 2005 (LWP-2) is a global dataset of 1-kilometer grid cells, created from nine global data layers covering human population pressure (population density), human land use and infrastructure (built-up areas, nighttime lights, land use/land cover), and human access (coastlines, roads, railroads, navigable rivers). The dataset in Clarke 1866 Geographic Coordinate System is produced by the Wildlife Conservation Society (WCS) and the Columbia University Center for International Earth Science Information Network (CIESIN).",
-            "release-place": "Palisades, NY",
-            "graphic-preview-description": "Maps Download Page",
             "creator": "Wildlife Conservation Society - WCS, and Center for International Earth Science Information Network - CIESIN - Columbia University",
-            "title": "Last of the Wild Project, Version 2, 2005 (LWP-2): Global Human Influence Index (HII) Dataset (Geographic)",
-            "graphic-preview-file": "https://sedac.ciesin.columbia.edu/data/set/wildareas-v2-human-influence-index-geographic/maps",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The Global Human Influence Index Dataset of the Last of the Wild Project, Version 2, 2005 (LWP-2) is a global dataset of 1-kilometer grid cells, created from nine global data layers covering human population pressure (population density), human land use and infrastructure (built-up areas, nighttime lights, land use/land cover), and human access (coastlines, roads, railroads, navigable rivers). The dataset in Clarke 1866 Geographic Coordinate System is produced by the Wildlife Conservation Society (WCS) and the Columbia University Center for International Earth Science Information Network (CIESIN).",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.7927%2FH4BP00QC",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.7927%2FH4BP00QC",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/downloads/maps/wildareas-v2/wildareas-v2-human-influence-index-geographic/hii-world-thumbnail.jpg",
-                    "description": "Sample browse graphic of the data set.",
                     "@type": "dcat:Distribution",
+                    "description": "Sample browse graphic of the data set.",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/downloads/maps/wildareas-v2/wildareas-v2-human-influence-index-geographic/hii-world-thumbnail.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 },
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/wildareas-v2-human-influence-index-geographic/data-download",
-                    "description": "Data Download Page",
+                {
                     "@type": "dcat:Distribution",
+                    "description": "Data Download Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/wildareas-v2-human-influence-index-geographic/data-download",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/wildareas-v2-human-influence-index-geographic/maps",
-                    "description": "Maps Download Page",
                     "@type": "dcat:Distribution",
+                    "description": "Maps Download Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/wildareas-v2-human-influence-index-geographic/maps",
+                    "mediaType": "text/html",
                     "title": "Get a related map visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/wildareas-v2-human-influence-index-geographic/maps/services",
-                    "description": "Web Map Service Page",
                     "@type": "dcat:Distribution",
+                    "description": "Web Map Service Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/wildareas-v2-human-influence-index-geographic/maps/services",
+                    "mediaType": "text/html",
                     "title": "Use Web Map Service (WMS) to download the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/wildareas-v2-human-influence-index-geographic",
-                    "description": "Data Set\u00a0Overview Page",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set\u00a0Overview Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/wildareas-v2-human-influence-index-geographic",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "graphic-preview-description": "Maps Download Page",
+            "graphic-preview-file": "https://sedac.ciesin.columbia.edu/data/set/wildareas-v2-human-influence-index-geographic/maps",
+            "identifier": "C179001808-SEDAC",
+            "issued": "2005-12-31",
+            "keyword": [
+                "land surface",
+                "ecosystems",
+                "earth science",
+                "land use/land cover",
+                "biosphere"
+            ],
+            "landingPage": "https://doi.org/10.7927/H4BP00QC",
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
+                "https://doi.org/10.7927/H4M61H5F",
+                "https://doi.org/10.7927/H4GF0RFQ",
+                "https://doi.org/10.7927/H4348H83",
+                "https://doi.org/10.7927/H4ZC80SS",
+                "https://doi.org/10.7927/H46W980H"
+            ],
+            "release-place": "Palisades, NY",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "1995-01-01T00:00:00Z/2004-12-31T00:00:00Z",
             "theme": [
                 "LWP",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Last of the Wild Project, Version 2, 2005 (LWP-2): Global Human Influence Index (HII) Dataset (Geographic)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://planetarynames.wr.usgs.gov/Page/mercuryQuadMap",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "1979-12-31",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
-            "keyword": [
-                "imagery",
-                "images",
-                "working group for planetary system nomenclature",
-                "wgpsn",
-                "mercury",
-                "planets",
-                "asteroids",
-                "usgs"
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
-            "identifier": "OCIO-Fitara-147",
             "description": "The purpose of this set of maps is to provide an up-to-date source showing the locations of Mercury surface feature names approved by the International Astronomical Union (IAU).",
-            "title": "Gazetteer of Planetary Nomenclature: Mercury: 1:5 million-scale",
-            "programCode": [
-                "026:007"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -1311301,718 +1311279,741 @@
                     "mediaType": "application/pdf"
                 }
             ],
-            "accrualPeriodicity": "irregular",
+            "identifier": "OCIO-Fitara-147",
+            "issued": "1979-12-31",
+            "keyword": [
+                "imagery",
+                "images",
+                "working group for planetary system nomenclature",
+                "wgpsn",
+                "mercury",
+                "planets",
+                "asteroids",
+                "usgs"
+            ],
+            "landingPage": "http://planetarynames.wr.usgs.gov/Page/mercuryQuadMap",
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
+            "title": "Gazetteer of Planetary Nomenclature: Mercury: 1:5 million-scale"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/600",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Hall, F.G., G. Rapalee, and D.E. Knapp. 2001. BOREAS Follow-On DSP-10 Regridded NDVI Maps for 1994. ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/600",
-            "issued": "2024-04-27",
-            "temporal": "1994-01-01T00:00:00Z/1995-01-01T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-07",
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
-            "identifier": "C2956559203-ORNL_CLOUD",
             "description": "These images were produced by averaging the 1-km FASIR-NDVI maps by Jing Chen to a 10' (horizontal) by 5' (vertical) pixel size in a straight latitude/longitude grid.  Each pixel represents the average NDVI of the 1-km pixels that fall in each 10' by 5' pixel, where more than 50% of the 1-km pixels in the 10' by 5' area are not cloud and are not missing.  If more than 50% of the 1-km pixels are missing or cloudy, a value of 0 is assigned to the 10' by 5' pixel.",
-            "graphic-preview-description": "Browse Image",
-            "title": "BOREAS Follow-On DSP-10 Regridded NDVI Maps for 1994",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/boreas_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F600",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F600",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/boreas/DSP/BFO_dsp10_ndvi/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/boreas/DSP/BFO_dsp10_ndvi/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/BOREAS/FollowOn/guides/dsp10_ndvi_maps.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/BOREAS/FollowOn/guides/dsp10_ndvi_maps.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/600",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/600",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/DSP/BFO_dsp10_ndvi/comp/0_ndvi_94_10by5min.txt",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/DSP/BFO_dsp10_ndvi/comp/0_ndvi_94_10by5min.txt",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/DSP/BFO_dsp10_ndvi/comp/dsp10_ndvi_maps.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/DSP/BFO_dsp10_ndvi/comp/dsp10_ndvi_maps.pdf",
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
+            "identifier": "C2956559203-ORNL_CLOUD",
+            "issued": "2024-04-27",
+            "keyword": [
+                "biosphere",
+                "earth science",
+                "vegetation"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/600",
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
             "spatial": "-111.0 48.0 -90.0 60.0",
+            "temporal": "1994-01-01T00:00:00Z/1995-01-01T23:59:59Z",
             "theme": [
                 "BOREAS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "BOREAS Follow-On DSP-10 Regridded NDVI Maps for 1994"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=GO-V-PWS-4-SUMM-VSA60S-V1.0",
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
-                "venus"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "Unknown",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.go-v-pws-4-summ-vsa60s-v1.0_rk75-supa",
+            "issued": "2018-06-26",
+            "keyword": [
+                "galileo",
+                "venus"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=GO-V-PWS-4-SUMM-VSA60S-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.go-v-pws-4-summ-vsa60s-v1.0_rk75-supa",
-            "description": "Unknown",
-            "title": "GO V PWS RESAMP SUMMARY VENUS SPECTRUM ANALYZER 60S V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "GO V PWS RESAMP SUMMARY VENUS SPECTRUM ANALYZER 60S V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/GPMGV/OLYMPEX/APU/DATA301",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Petersen, Walter A, Ali  Tokay, Patrick N Gatlin and Matthew T. Wingo.2017. GPM Ground Validation Autonomous Parsivel Unit (APU) OLYMPEX [indicate subset used]. Dataset available online from the NASA Global Hydrometeorology Resource Center DAAC, Huntsville, Alabama, U.S.A. DOI: http://dx.doi.org/10.5067/GPMGV/OLYMPEX/APU/DATA301",
-            "issued": "2017-05-24",
-            "temporal": "2015-01-10T09:24:00Z/2016-01-31T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-04-28",
-            "keyword": [
-                "earth science",
-                "atmosphere",
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
-            "identifier": "C1979128148-GHRC_DAAC",
             "description": "The GPM Ground Validation Autonomous Parsivel Unit (APU) OLYMPEX dataset was collected during the OLYMPEX field campaign held at Washington's Olympic Peninsula during the intense observation period of  November 2015 to the end of January 2016.  The dataset consists of data collected by 16 APUs.  The APU is an optical laser-disdrometer based on single particle extinction that measures particle size and fall velocity.  It consists of the Parsivel2 developed by OTT in Germany and supporting hardware developed by University of Alabama. This APU dataset provides precipitation data including precipitation amount, precipitation rate, reflectivity in Rayleigh regime, liquid water content, drop diameter, and drop concentration. Data are available in ASCII format.",
-            "title": "GPM Ground Validation Autonomous Parsivel Unit (APU) OLYMPEX V1",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGPMGV%2FOLYMPEX%2FAPU%2FDATA301",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGPMGV%2FOLYMPEX%2FAPU%2FDATA301",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=gpmapuolyx",
-                    "description": "Files may be downloaded directly to your workstation from this link",
                     "@type": "dcat:Distribution",
+                    "description": "Files may be downloaded directly to your workstation from this link",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=gpmapuolyx",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
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
-                    "description": "University of Washington OLYMPEX Web Site",
                     "@type": "dcat:Distribution",
+                    "description": "University of Washington OLYMPEX Web Site",
+                    "downloadURL": "http://olympex.atmos.washington.edu/",
+                    "mediaType": "text/html",
                     "title": "View information related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/olympex/disdrometers_and_gauges/parsivel/doc/gpmapuolyx_dataset.pdf",
-                    "description": "The guide document contains detailed information about the dataset",
                     "@type": "dcat:Distribution",
+                    "description": "The guide document contains detailed information about the dataset",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/olympex/disdrometers_and_gauges/parsivel/doc/gpmapuolyx_dataset.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/olympex/disdrometers_and_gauges/parsivel/doc/readme_apu_olympex.pdf",
-                    "description": "Automated Parsivel Unit (APU) data processing Olympic Mountain Experiment (OLYMPEX)",
                     "@type": "dcat:Distribution",
+                    "description": "Automated Parsivel Unit (APU) data processing Olympic Mountain Experiment (OLYMPEX)",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/olympex/disdrometers_and_gauges/parsivel/doc/readme_apu_olympex.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View the primary investigator's documentation for this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.1175/1520-0469(1976)033%3C0851:TVASOC%3E2.0.CO;2",
-                    "description": "Terminal velocity and shape of cloud and precipitation drops aloft",
                     "@type": "dcat:Distribution",
+                    "description": "Terminal velocity and shape of cloud and precipitation drops aloft",
+                    "downloadURL": "https://doi.org/10.1175/1520-0469(1976)033%3C0851:TVASOC%3E2.0.CO;2",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.1175/JTECH-D-12-00254.1",
-                    "description": "Articulating and Stationary PARSIVEL Disdrometer Measurements in Conditions with Strong Winds and Heavy Rainfall",
                     "@type": "dcat:Distribution",
+                    "description": "Articulating and Stationary PARSIVEL Disdrometer Measurements in Conditions with Strong Winds and Heavy Rainfall",
+                    "downloadURL": "https://doi.org/10.1175/JTECH-D-12-00254.1",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.1175/2010JHM1244.1",
-                    "description": "Experimental quantification of the sampling uncertainty associated with measurements from PARSIVEL Disdrometers",
                     "@type": "dcat:Distribution",
+                    "description": "Experimental quantification of the sampling uncertainty associated with measurements from PARSIVEL Disdrometers",
+                    "downloadURL": "https://doi.org/10.1175/2010JHM1244.1",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.1175/1520-0450(2001)040%3C2083:CODSDM%3E2.0.CO;2",
-                    "description": "Comparison of drop size distribution measurements by impact and optical disdrometers",
                     "@type": "dcat:Distribution",
+                    "description": "Comparison of drop size distribution measurements by impact and optical disdrometers",
+                    "downloadURL": "https://doi.org/10.1175/1520-0450(2001)040%3C2083:CODSDM%3E2.0.CO;2",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.1175/JTECH-D-13-00174.1",
-                    "description": "Evaluation of the New Version of the Laser-Optical Disdrometer, OTT Parsivel2",
                     "@type": "dcat:Distribution",
+                    "description": "Evaluation of the New Version of the Laser-Optical Disdrometer, OTT Parsivel2",
+                    "downloadURL": "https://doi.org/10.1175/JTECH-D-13-00174.1",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://dx.doi.org/10.1175/BAMS-D-16-0182.1",
-                    "description": "The Olympic Mountains Experiment (OLYMPEX)",
```

