# Change History for nasa.json (Part 137)

### Changes from 31606f9 to dd2190f (Part 126/162)
**Author:** Automated

**Date:** 2025-02-01 15:02:16+00:00

**Message:** Updated data: Sat Feb  1 15:02:16 UTC 2025

```diff
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://data.nasa.gov/api/views/dd9e-wu2v/rows.csv?accessType=DOWNLOAD",
-                    "description": "Landslide data as a CSV file",
                     "@type": "dcat:Distribution",
+                    "description": "Landslide data as a CSV file",
+                    "downloadURL": "https://data.nasa.gov/api/views/dd9e-wu2v/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv",
                     "title": "rows.csv"
                 }
             ],
-            "accrualPeriodicity": "irregular",
+            "identifier": "Global-Landslide-Catalog-Export",
+            "issued": "2018-04-02",
+            "keyword": [
+                "hazards",
+                "citizen science",
+                "landslide",
+                "mudslide",
+                "earth"
+            ],
+            "landingPage": "https://landslides.nasa.gov",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Aeronautics and Space Administration"
+            },
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "Global Landslide Catalog Export"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/AQR50-3WUDS",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "NASA Aquarius project. 2017-12-07. Aquarius Official Release Level 3 Wind Speed Standard Mapped Image Descending Monthly Climatology Data. Version 5.0. Aquarius Sea Surface Salinity Products. Goddard Space Flight Center, 8800 Greenbelt Rd.; Greeenbelt, MD., 20771, USA. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/GSFC OBPG. https://doi.org/10.5067/AQR50-3WUDS. http://podaac.jpl.nasa.gov/SeaSurfaceSalinity/Aquarius. NASA Aquarius project, NASA/GSFC OBPG, 2017-12-07, Aquarius Official Release Level 3 Wind Speed Standard Mapped Image Descending Monthly Climatology Data V5.0, http://podaac.jpl.nasa.gov/SeaSurfaceSalinity/Aquarius.",
-            "issued": "2017-10-21",
-            "temporal": "2011-08-25T02:41:02Z/2015-06-07T12:45:21Z",
-            "@type": "dcat:Dataset",
-            "modified": "2017-12-07",
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
-            "identifier": "C2491757228-POCLOUD",
-            "description": "Aquarius Level 3 ocean surface wind speed standard mapped image data contains gridded 1 degree spatial resolution wind speed data averaged over daily, 7 day, monthly, and seasonal time scales. This particular data set is the\nmonthly climatology, Descending wind speed product for version 5.0 of the Aquarius data set, which is the official end of mission public data release from the AQUARIUS/SAC-D mission. Only retrieved values for Descending passes have been used to create this product.  The Aquarius instrument is onboard the AQUARIUS/SAC-D satellite, a collaborative effort between NASA and the Argentinian Space Agency Comision Nacional de Actividades Espaciales (CONAE). The instrument consists of three radiometers in push broom alignment at incidence angles of 29, 38, and 46 degrees incidence angles relative to the shadow side of the orbit.  Footprints for the beams are: 76 km (along-track) x 94 km (cross-track), 84 km x 120 km and 96km x 156 km, yielding a total cross-track swath of 370 km. The radiometers measure brightness temperature at 1.413 GHz in their respective horizontal and vertical polarizations (TH and TV). A scatterometer operating at 1.26 GHz measures ocean backscatter in each footprint that is used for surface roughness corrections in the estimation of salinity. The scatterometer has an approximate 390km swath.",
-            "release-place": "Goddard Space Flight Center, 8800 Greenbelt Rd.; Greeenbelt, MD., 20771, USA",
-            "series-name": "Aquarius Official Release Level 3 Wind Speed Standard Mapped Image Descending Monthly Climatology Data",
-            "graphic-preview-description": "Thumbnail",
             "creator": "NASA Aquarius project",
-            "title": "Aquarius Official Release Level 3 Wind Speed Standard Mapped Image Descending Monthly Climatology Data V5.0",
-            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/AQUARIUS_L3_WIND_SPEED_SMID_MONTHLY-CLIMATOLOGY_V5.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "Aquarius Level 3 ocean surface wind speed standard mapped image data contains gridded 1 degree spatial resolution wind speed data averaged over daily, 7 day, monthly, and seasonal time scales. This particular data set is the\nmonthly climatology, Descending wind speed product for version 5.0 of the Aquarius data set, which is the official end of mission public data release from the AQUARIUS/SAC-D mission. Only retrieved values for Descending passes have been used to create this product.  The Aquarius instrument is onboard the AQUARIUS/SAC-D satellite, a collaborative effort between NASA and the Argentinian Space Agency Comision Nacional de Actividades Espaciales (CONAE). The instrument consists of three radiometers in push broom alignment at incidence angles of 29, 38, and 46 degrees incidence angles relative to the shadow side of the orbit.  Footprints for the beams are: 76 km (along-track) x 94 km (cross-track), 84 km x 120 km and 96km x 156 km, yielding a total cross-track swath of 370 km. The radiometers measure brightness temperature at 1.413 GHz in their respective horizontal and vertical polarizations (TH and TV). A scatterometer operating at 1.26 GHz measures ocean backscatter in each footprint that is used for surface roughness corrections in the estimation of salinity. The scatterometer has an approximate 390km swath.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAQR50-3WUDS",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAQR50-3WUDS",
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
-                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/AQUARIUS_L3_WIND_SPEED_SMID_MONTHLY-CLIMATOLOGY_V5.jpg",
-                    "description": "Thumbnail",
                     "@type": "dcat:Distribution",
+                    "description": "Thumbnail",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/AQUARIUS_L3_WIND_SPEED_SMID_MONTHLY-CLIMATOLOGY_V5.jpg",
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
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2491757228-POCLOUD",
-                    "description": "HTTPS endpoint for data browse and download",
                     "@type": "dcat:Distribution",
+                    "description": "HTTPS endpoint for data browse and download",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2491757228-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2491757228-POCLOUD",
-                    "description": "Browse granule search results in Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse granule search results in Earthdata Search",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2491757228-POCLOUD",
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
+            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/AQUARIUS_L3_WIND_SPEED_SMID_MONTHLY-CLIMATOLOGY_V5.jpg",
+            "identifier": "C2491757228-POCLOUD",
+            "issued": "2017-10-21",
+            "keyword": [
+                "earth science",
+                "ocean winds",
+                "oceans"
+            ],
+            "landingPage": "https://doi.org/10.5067/AQR50-3WUDS",
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
+            "series-name": "Aquarius Official Release Level 3 Wind Speed Standard Mapped Image Descending Monthly Climatology Data",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2011-08-25T02:41:02Z/2015-06-07T12:45:21Z",
             "theme": [
                 "AQUARIUS SAC-D",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Aquarius Official Release Level 3 Wind Speed Standard Mapped Image Descending Monthly Climatology Data V5.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/322",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Ehleringer, J.R. 1999. BOREAS TE-05 Diurnal CO2 Canopy Profile Data. ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/322",
-            "issued": "2023-11-22",
-            "temporal": "1994-05-24T00:00:00Z/1994-09-08T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-11-28",
-            "keyword": [
-                "atmospheric chemistry",
-                "soils",
-                "biosphere",
-                "earth science",
-                "atmosphere",
-                "ecosystems",
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
-            "identifier": "C2808128013-ORNL_CLOUD",
             "description": "Contains the CO2 profile concentration measurements made by the TE-05 BOREAS team in the NSA and SSA.",
-            "graphic-preview-description": "Browse Image",
-            "title": "BOREAS TE-05 Diurnal CO2 Canopy Profile Data",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/boreas_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F322",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F322",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/boreas/TE/te5co2pd/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/boreas/TE/te5co2pd/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/BOREAS/guides/TE05_CO2_Profile.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/BOREAS/guides/TE05_CO2_Profile.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/322",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/322",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/msword",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TE/te5co2pd/comp/TE05_CO2_Profile.doc",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TE/te5co2pd/comp/TE05_CO2_Profile.doc",
+                    "mediaType": "application/msword",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TE/te5co2pd/comp/TE05_CO2_Profile.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TE/te5co2pd/comp/TE05_CO2_Profile.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TE/te5co2pd/comp/TE05_CO2_Profile.txt",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TE/te5co2pd/comp/TE05_CO2_Profile.txt",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TE/te5co2pd/comp/te5co2pd.def",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TE/te5co2pd/comp/te5co2pd.def",
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
+            "identifier": "C2808128013-ORNL_CLOUD",
+            "issued": "2023-11-22",
+            "keyword": [
+                "atmospheric chemistry",
+                "soils",
+                "biosphere",
+                "earth science",
+                "atmosphere",
+                "ecosystems",
+                "land surface"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/322",
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
             "spatial": "-106.19 53.62 -98.51 55.93",
+            "temporal": "1994-05-24T00:00:00Z/1994-09-08T23:59:59Z",
             "theme": [
                 "BOREAS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "BOREAS TE-05 Diurnal CO2 Canopy Profile Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/716",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Nelkin, E.J., G.J. Huffman, and C.D. Kummerow. 2004. SAFARI 2000 SSM/I GPROF 6.0 Precipitation Data, 0.5-Deg, 1999-2001. ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/716",
-            "issued": "2023-10-18",
-            "temporal": "1999-01-01T00:00:00Z/2001-12-31T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-10-24",
-            "keyword": [
-                "earth science",
-                "precipitation",
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
-            "identifier": "C2788392368-ORNL_CLOUD",
             "description": "The GPROF 6.0 Pentads data set contains 5-day (pentad) averages of the GPROF 6.0 Gridded Orbits. The GPROF(Goddard Profiling Algorithm) data set contains a suite of 9 products providing instantaneous, gridded values of precipitation totals for each granule of the SSM/I (Special Sensor Microwave/Imager) data over the roughly 14-year period July 1987 through the present. Even though there have been at least two satellites for the entire period, sampling is sufficiently sparse that the data are averaged for pentads, then the pentads are smoothed with a 1-2-3-2-1 time-weighting. The last two pentads are unevenly weighted since the last (or last two) pentads in the average are not yet available. Consequently, the last two pentads must be recomputed when the next pentad becomes available.The data set prepared for SAFARI cover the years 1999, 2000, and 2001.The main refereed citations for the data set are Kummerow et al. (1996)and Olson et al. (1999)",
-            "graphic-preview-description": "Browse Image",
-            "title": "SAFARI 2000 SSM/I GPROF 6.0 Precipitation Data, 0.5-Deg, 1999-2001",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/safari_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F716",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F716",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/safari2k/climate_meteorology/GPROF_precip/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/safari2k/climate_meteorology/GPROF_precip/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/S2K/guides/s2k_GPROF.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/S2K/guides/s2k_GPROF.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/716",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/716",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/safari2k/climate_meteorology/GPROF_precip/comp/S2K_precip_gprofv6.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/safari2k/climate_meteorology/GPROF_precip/comp/S2K_precip_gprofv6.pdf",
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
+            "identifier": "C2788392368-ORNL_CLOUD",
+            "issued": "2023-10-18",
+            "keyword": [
+                "earth science",
+                "precipitation",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/716",
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
             "spatial": "5.0 -35.0 60.0 5.0",
+            "temporal": "1999-01-01T00:00:00Z/2001-12-31T23:59:59Z",
             "theme": [
                 "SAFARI 2000",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "SAFARI 2000 SSM/I GPROF 6.0 Precipitation Data, 0.5-Deg, 1999-2001"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewBundle.jsp?identifier=urn%3Anasa%3Apds%3Agbo.ast.smass2.spectra&version=1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This data set contains visible-wavelength (0.435-0.925 micron) spectra for 1341\nmain-belt asteroids observed during the second phase of the Small Main-belt  Asteroid\nSpectroscopic Survey (SMASSII) between August 1993 and March 1999.  The purpose of\nthe SMASSII survey was to provide a new basis for studying the compositional\ndiversity and structure of the asteroid belt.  Based on experiences gained from the\nearlier SMASS survey, SMASSII focused on producing an even larger, internally\nconsistent set of CCD spectra for small (D < 20 km) main-belt asteroids.  The\nobserving strategies and procedures used during SMASSII roughly parallel those used\nin the first survey (Xu et al. Icarus 115 1-35, 1995), though several minor changes\nwere made in instrumentation and in portions of the data reduction process.",
+            "identifier": "urn:nasa:pds:gbo.ast.smass2.spectra",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2021-05-21",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "(3406) omsk",
                 "(100480) 1996 uk",
@@ -1324251,895 +1324253,901 @@
                 "multiple asteroids",
                 "none"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewBundle.jsp?identifier=urn%3Anasa%3Apds%3Agbo.ast.smass2.spectra&version=1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:gbo.ast.smass2.spectra",
-            "description": "This data set contains visible-wavelength (0.435-0.925 micron) spectra for 1341\nmain-belt asteroids observed during the second phase of the Small Main-belt  Asteroid\nSpectroscopic Survey (SMASSII) between August 1993 and March 1999.  The purpose of\nthe SMASSII survey was to provide a new basis for studying the compositional\ndiversity and structure of the asteroid belt.  Based on experiences gained from the\nearlier SMASS survey, SMASSII focused on producing an even larger, internally\nconsistent set of CCD spectra for small (D < 20 km) main-belt asteroids.  The\nobserving strategies and procedures used during SMASSII roughly parallel those used\nin the first survey (Xu et al. Icarus 115 1-35, 1995), though several minor changes\nwere made in instrumentation and in portions of the data reduction process.",
-            "title": "Small Main-Belt Asteroid Spectroscopic Survey, Phase II V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "Small Main-Belt Asteroid Spectroscopic Survey, Phase II V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C2340494496-OB_DAAC.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/GSFC/SED/ESD/GCDC/OB.DAAC.",
-            "issued": "2022-09-14",
-            "temporal": "2017-11-29T00:00:00Z/2023-02-28T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-09-14",
-            "keyword": [
-                "oceans",
-                "ocean optics",
-                "aerosols",
-                "atmosphere",
-                "earth science",
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
-            "identifier": "C2340494496-OB_DAAC",
             "description": "The Ocean Biology DAAC produces near real-time (quicklook) products using the best-available combination of ancillary data from meteorological and ozone data. As such, the inputs and the calibration used are less than optimal. Quicklook products provide a snapshot of the data during a short time period within a single orbit.",
-            "title": "NOAA-20 VIIRS Regional Ocean Color (OC) - Near Real Time (NRT) Data, version R2022.0",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://oceandata.sci.gsfc.nasa.gov/directdataaccess/Level-2/NOAA20-VIIRS/",
-                    "description": "NASA Ocean Color Web - Data Distribution Site",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Ocean Color Web - Data Distribution Site",
+                    "downloadURL": "https://oceandata.sci.gsfc.nasa.gov/directdataaccess/Level-2/NOAA20-VIIRS/",
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
-                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/data/10.5067/NOAA20/VIIRS/L2/OC/2022",
-                    "description": "VIIRS-NOAA-20 L2 Ocean Color (OC) - Near Real Time (NRT) Dataset Landing Page",
                     "@type": "dcat:Distribution",
+                    "description": "VIIRS-NOAA-20 L2 Ocean Color (OC) - Near Real Time (NRT) Dataset Landing Page",
+                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/data/10.5067/NOAA20/VIIRS/L2/OC/2022",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 }
             ],
+            "identifier": "C2340494496-OB_DAAC",
+            "issued": "2022-09-14",
+            "keyword": [
+                "oceans",
+                "ocean optics",
+                "aerosols",
+                "atmosphere",
+                "earth science",
+                "ocean chemistry"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C2340494496-OB_DAAC.html",
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
+            "temporal": "2017-11-29T00:00:00Z/2023-02-28T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "NOAA-20 VIIRS Regional Ocean Color (OC) - Near Real Time (NRT) Data, version R2022.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/S6AP4-2LRNTR-F08",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Ocean Surface Topography Science Team. 2023-07-31. Sentinel-6A MF Jason-CS L2 P4 Altimeter Low Resolution (LR) NTC Reduced Ocean Surface Topography F08. Version F08. PO.DAAC. Archived by National Aeronautics and Space Administration, U.S. Government, PO.DAAC. https://doi.org/10.5067/S6AP4-2LRNTR-F08.",
-            "issued": "2023-02-18",
-            "temporal": "2020-11-30T00:00:00Z/2024-12-09T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-04",
-            "references": [
-                "https://doi.org/10.1016/j.rse.2021.112395"
-            ],
-            "keyword": [
-                "ocean waves",
-                "oceans",
-                "earth science",
-                "sea surface topography"
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
-            "identifier": "C2619443998-POCLOUD",
-            "description": "Provides low resolution (LR) non-time critical (NTC; 60-day latency) measurements of sea surface height anomaly (SSHA), Significant Wave Height (SWH), and Wind Speed. The NTC product is analogous to the Jason-3 GDR product.",
-            "release-place": "PO.DAAC",
-            "graphic-preview-description": "Thumbnail image for Website",
             "creator": "Ocean Surface Topography Science Team",
-            "title": "Sentinel-6A MF Jason-CS L2 P4 Altimeter Low Resolution (LR) NTC Reduced Ocean Surface Topography F08",
-            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/JASON_CS_S6A_L2_ALT_HR_RED_OST_NTC_F08.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "Provides low resolution (LR) non-time critical (NTC; 60-day latency) measurements of sea surface height anomaly (SSHA), Significant Wave Height (SWH), and Wind Speed. The NTC product is analogous to the Jason-3 GDR product.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FS6AP4-2LRNTR-F08",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FS6AP4-2LRNTR-F08",
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
-                    "downloadURL": "https://podaac.jpl.nasa.gov/dataset/JASON_CS_S6A_L2_ALT_LR_RED_OST_NTC_F08",
-                    "description": "Data Set Landing Page",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Landing Page",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/dataset/JASON_CS_S6A_L2_ALT_LR_RED_OST_NTC_F08",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/JASON_CS_S6A_L2_ALT_HR_RED_OST_NTC_F08.jpg",
-                    "description": "Thumbnail image for Website",
                     "@type": "dcat:Distribution",
+                    "description": "Thumbnail image for Website",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/JASON_CS_S6A_L2_ALT_HR_RED_OST_NTC_F08.jpg",
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
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2619443998-POCLOUD",
-                    "description": "HTTPS endpoint for data browse and download",
                     "@type": "dcat:Distribution",
+                    "description": "HTTPS endpoint for data browse and download",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2619443998-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2619443998-POCLOUD",
-                    "description": "Browse granule search results in Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse granule search results in Earthdata Search",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2619443998-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 }
             ],
+            "graphic-preview-description": "Thumbnail image for Website",
+            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/JASON_CS_S6A_L2_ALT_HR_RED_OST_NTC_F08.jpg",
+            "identifier": "C2619443998-POCLOUD",
+            "issued": "2023-02-18",
+            "keyword": [
+                "ocean waves",
+                "oceans",
+                "earth science",
+                "sea surface topography"
+            ],
+            "landingPage": "https://doi.org/10.5067/S6AP4-2LRNTR-F08",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2024-11-04",
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
+            "temporal": "2020-11-30T00:00:00Z/2024-12-09T00:00:00Z",
             "theme": [
                 "Sentinel-6",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Sentinel-6A MF Jason-CS L2 P4 Altimeter Low Resolution (LR) NTC Reduced Ocean Surface Topography F08"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/GEDI/GEDI01_B.002",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Ralph Dubayah, Scott Luthcke, James Blair, Michelle Hofton, John Armston, Hao Tang. 2021-04-16. GEDI L1B Geolocated Waveform Data Global Footprint Level V002. Sioux Falls, South Dakota, USA. Archived by National Aeronautics and Space Administration, U.S. Government, NASA EOSDIS Land Processes Distributed Active Archive Center. https://doi.org/10.5067/GEDI/GEDI01_B.002. https://doi.org/10.5067/GEDI/GEDI01_B.002. The DOI landing page provides citations in APA and Chicago..",
-            "issued": "2021-04-16",
-            "temporal": "2019-04-04T00:00:00Z/2023-03-16T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-03-01",
-            "keyword": [
-                "topography",
-                "vegetation",
-                "spectral/engineering",
-                "lidar",
-                "land surface",
-                "earth science",
-                "biosphere"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ralph Dubayah",
                 "hasEmail": "mailto:dubayah@umd.edu"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "LP DAAC"
-            },
-            "identifier": "C2142749196-LPCLOUD",
-            "description": "The Global Ecosystem Dynamics Investigation (GEDI) mission aims to characterize ecosystem structure and dynamics to enable radically improved quantification and understanding of the Earth\u2019s carbon cycle and biodiversity. The GEDI instrument produces high resolution laser ranging observations of the 3-dimensional structure of the Earth. GEDI is attached to the International Space Station (ISS) and collects data globally between 51.6\u00b0 N and 51.6\u00b0 S latitudes at the highest resolution and densest sampling of any light detection and ranging (lidar) instrument in orbit to date. Each GEDI Version 2 granule encompasses one-fourth of an ISS orbit and includes georeferenced metadata to allow for spatial querying and subsetting.\r\n\r\nThe GEDI Level 1B Geolocated Waveforms product (GEDI01_B) provides geolocated corrected and smoothed waveforms, geolocation parameters, and geophysical corrections for each laser shot for all eight GEDI beams. GEDI01_B data are created by geolocating the GEDI01_A raw waveform data. The GEDI01_B product is provided in HDF5 format and has a spatial resolution (average footprint) of 25 meters.\r\n\r\nThe GEDI01_B data product contains 85 layers for each of the eight beams including the geolocated corrected and smoothed waveform datasets and parameters and the accompanying ancillary, geolocation, and geophysical correction. Additional information can be found in the GEDI L1B Product Data Dictionary.",
-            "release-place": "Sioux Falls, South Dakota, USA",
-            "graphic-preview-description": "Browse image for Earthdata Search",
             "creator": "Ralph Dubayah, Scott Luthcke, James Blair, Michelle Hofton, John Armston, Hao Tang",
-            "title": "GEDI L1B Geolocated Waveform Data Global Footprint Level V002",
-            "graphic-preview-file": "https://data.lpdaac.earthdatacloud.nasa.gov/lp-prod-public/GEDI01_B.002/GEDI01_B_2023075170425_O24113_02_T00409_02_005_02_V002/GEDI01_B_2023075170425_O24113_02_T00409_02_005_02_V002.png",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The Global Ecosystem Dynamics Investigation (GEDI) mission aims to characterize ecosystem structure and dynamics to enable radically improved quantification and understanding of the Earth\u2019s carbon cycle and biodiversity. The GEDI instrument produces high resolution laser ranging observations of the 3-dimensional structure of the Earth. GEDI is attached to the International Space Station (ISS) and collects data globally between 51.6\u00b0 N and 51.6\u00b0 S latitudes at the highest resolution and densest sampling of any light detection and ranging (lidar) instrument in orbit to date. Each GEDI Version 2 granule encompasses one-fourth of an ISS orbit and includes georeferenced metadata to allow for spatial querying and subsetting.\r\n\r\nThe GEDI Level 1B Geolocated Waveforms product (GEDI01_B) provides geolocated corrected and smoothed waveforms, geolocation parameters, and geophysical corrections for each laser shot for all eight GEDI beams. GEDI01_B data are created by geolocating the GEDI01_A raw waveform data. The GEDI01_B product is provided in HDF5 format and has a spatial resolution (average footprint) of 25 meters.\r\n\r\nThe GEDI01_B data product contains 85 layers for each of the eight beams including the geolocated corrected and smoothed waveform datasets and parameters and the accompanying ancillary, geolocation, and geophysical correction. Additional information can be found in the GEDI L1B Product Data Dictionary.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGEDI%2FGEDI01_B.002",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGEDI%2FGEDI01_B.002",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=C2142749196-LPCLOUD",
-                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=C2142749196-LPCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
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
-                    "downloadURL": "https://doi.org/10.5067/GEDI/GEDI01_B.002",
-                    "description": "The product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "The product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
+                    "downloadURL": "https://doi.org/10.5067/GEDI/GEDI01_B.002",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://lpdaac.usgs.gov/documents/981/gedi_l1b_dictionary_P003_v2.html",
-                    "description": "The data dictionary provides additional information on the Science Dataset (SDS) layers.",
                     "@type": "dcat:Distribution",
+                    "description": "The data dictionary provides additional information on the Science Dataset (SDS) layers.",
+                    "downloadURL": "https://lpdaac.usgs.gov/documents/981/gedi_l1b_dictionary_P003_v2.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/DOC/GEDI/GEDI_WF_ATBD.001",
-                    "description": "The Waveform Processing ATBD provides physical theory and mathematical procedures for the calculations used to produce the data products.",
                     "@type": "dcat:Distribution",
+                    "description": "The Waveform Processing ATBD provides physical theory and mathematical procedures for the calculations used to produce the data products.",
+                    "downloadURL": "https://doi.org/10.5067/DOC/GEDI/GEDI_WF_ATBD.001",
+                    "mediaType": "text/html",
                     "title": "View this dataset's algorithm theoretical basis document"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/DOC/GEDI/GEDI_WFGEO_ATBD.001",
-                    "description": "The Geolocation ATBD provides physical theory and mathematical procedures for the calculations used to produce the data products.",
                     "@type": "dcat:Distribution",
+                    "description": "The Geolocation ATBD provides physical theory and mathematical procedures for the calculations used to produce the data products.",
+                    "downloadURL": "https://doi.org/10.5067/DOC/GEDI/GEDI_WFGEO_ATBD.001",
+                    "mediaType": "text/html",
                     "title": "View this dataset's algorithm theoretical basis document"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://gedi.umd.edu/",
-                    "description": "The GEDI website provides detailed information on the GEDI mission, instrument, science, applications, and data.",
                     "@type": "dcat:Distribution",
+                    "description": "The GEDI website provides detailed information on the GEDI mission, instrument, science, applications, and data.",
+                    "downloadURL": "https://gedi.umd.edu/",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://lpdaac.usgs.gov/documents/997/GEDI01B_User_Guide_V21.pdf",
-                    "description": "The technical information in the User's Guide enables users to interpret and use the data products.",
                     "@type": "dcat:Distribution",
+                    "description": "The technical information in the User's Guide enables users to interpret and use the data products.",
+                    "downloadURL": "https://lpdaac.usgs.gov/documents/997/GEDI01B_User_Guide_V21.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://lpdaac.usgs.gov/resources/e-learning/accessing-and-analyzing-gedi-lidar-data-for-vegetation-studies/",
-                    "description": "GEDI L1-L2 Data Resources, Access, and Visualization Demonstration",
                     "@type": "dcat:Distribution",
+                    "description": "GEDI L1-L2 Data Resources, Access, and Visualization Demonstration",
+                    "downloadURL": "https://lpdaac.usgs.gov/resources/e-learning/accessing-and-analyzing-gedi-lidar-data-for-vegetation-studies/",
+                    "mediaType": "text/html",
                     "title": "View this dataset's how-to documentation"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://git.earthdata.nasa.gov/projects/LPDUR/repos/gedi-subsetter/browse",
-                    "description": "GEDI Spatial and Band/Layer Subsetting and Export to GeoJSON Script",
                     "@type": "dcat:Distribution",
+                    "description": "GEDI Spatial and Band/Layer Subsetting and Export to GeoJSON Script",
+                    "downloadURL": "https://git.earthdata.nasa.gov/projects/LPDUR/repos/gedi-subsetter/browse",
+                    "mediaType": "text/html",
                     "title": "View this dataset's how-to documentation"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://lpdaac.usgs.gov/documents/989/GEDI_Quick_Guide_V2.pdf",
-                    "description": "GEDI Spatial Querying and Subsetting Quick Guide",
                     "@type": "dcat:Distribution",
+                    "description": "GEDI Spatial Querying and Subsetting Quick Guide",
+                    "downloadURL": "https://lpdaac.usgs.gov/documents/989/GEDI_Quick_Guide_V2.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's how-to documentation"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://data.lpdaac.earthdatacloud.nasa.gov/lp-prod-public/GEDI01_B.002/GEDI01_B_2023075170425_O24113_02_T00409_02_005_02_V002/GEDI01_B_2023075170425_O24113_02_T00409_02_005_02_V002.png",
-                    "description": "Browse image for Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse image for Earthdata Search",
+                    "downloadURL": "https://data.lpdaac.earthdatacloud.nasa.gov/lp-prod-public/GEDI01_B.002/GEDI01_B_2023075170425_O24113_02_T00409_02_005_02_V002/GEDI01_B_2023075170425_O24113_02_T00409_02_005_02_V002.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://github.com/nasa/GEDI-Data-Resources",
-                    "description": "The GEDI Data Resources repository provides guides, short how-tos, and tutorials to help users access and work with data from the GEDI mission.",
                     "@type": "dcat:Distribution",
+                    "description": "The GEDI Data Resources repository provides guides, short how-tos, and tutorials to help users access and work with data from the GEDI mission.",
+                    "downloadURL": "https://github.com/nasa/GEDI-Data-Resources",
+                    "mediaType": "text/html",
                     "title": "View this dataset's how-to documentation"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://git.earthdata.nasa.gov/projects/LPDUR/repos/gedi-finder-tutorial-python/browse",
-                    "description": "Spatial Querying of GEDI Version 2 Data in Python",
                     "@type": "dcat:Distribution",
+                    "description": "Spatial Querying of GEDI Version 2 Data in Python",
+                    "downloadURL": "https://git.earthdata.nasa.gov/projects/LPDUR/repos/gedi-finder-tutorial-python/browse",
+                    "mediaType": "text/html",
                     "title": "View this dataset's how-to documentation"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://git.earthdata.nasa.gov/projects/LPDUR/repos/gedi-finder-tutorial-r/browse",
-                    "description": "Spatial Querying of GEDI Version 2 Data in R",
                     "@type": "dcat:Distribution",
+                    "description": "Spatial Querying of GEDI Version 2 Data in R",
+                    "downloadURL": "https://git.earthdata.nasa.gov/projects/LPDUR/repos/gedi-finder-tutorial-r/browse",
+                    "mediaType": "text/html",
                     "title": "View this dataset's how-to documentation"
                 }
             ],
+            "graphic-preview-description": "Browse image for Earthdata Search",
+            "graphic-preview-file": "https://data.lpdaac.earthdatacloud.nasa.gov/lp-prod-public/GEDI01_B.002/GEDI01_B_2023075170425_O24113_02_T00409_02_005_02_V002/GEDI01_B_2023075170425_O24113_02_T00409_02_005_02_V002.png",
+            "identifier": "C2142749196-LPCLOUD",
+            "issued": "2021-04-16",
+            "keyword": [
+                "topography",
+                "vegetation",
+                "spectral/engineering",
+                "lidar",
+                "land surface",
+                "earth science",
+                "biosphere"
+            ],
+            "landingPage": "https://doi.org/10.5067/GEDI/GEDI01_B.002",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2024-03-01",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "LP DAAC"
+            },
+            "release-place": "Sioux Falls, South Dakota, USA",
             "spatial": "-180.0 -54.0 180.0 54.0",
+            "temporal": "2019-04-04T00:00:00Z/2023-03-16T23:59:59.999Z",
             "theme": [
                 "GEDI",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "GEDI L1B Geolocated Waveform Data Global Footprint Level V002"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/MODIS/MYD21A1D.061",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Glynn Hulley. 2021-02-08. MODIS/Aqua Land Surface Temperature/3-Band Emissivity Daily L3 Global 1km SIN Grid Day V061. Sioux Falls, South Dakota, USA. Archived by National Aeronautics and Space Administration, U.S. Government, NASA EOSDIS Land Processes Distributed Active Archive Center. https://doi.org/10.5067/MODIS/MYD21A1D.061. https://doi.org/10.5067/MODIS/MYD21A1D.061. The DOI landing page provides citations in APA and Chicago styles..",
-            "issued": "2021-02-08",
-            "temporal": "2002-07-04T00:00:00Z/2024-06-03T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2021-02-08",
-            "keyword": [
-                "surface thermal properties",
-                "earth science",
-                "land surface",
-                "ngda",
-                "surface radiative properties",
-                "national geospatial data asset"
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
-            "identifier": "C2565805783-LPCLOUD",
-            "description": "A suite of MODIS Land Surface Temperature and Emissivity  (LST&E) products are available in Collection 6.1. The MYD21 LST algorithm differs from the algorithm of the MYD11 (https://doi.org/10.5067/modis/myd11_l2.061) LST products, in that the MYD21 algorithm is based on the ASTER Temperature/Emissivity Separation (TES) technique, whereas the MYD11 uses the split-window technique. The MYD21 TES algorithm uses a physics-based algorithm to retrieve dynamically both the LST and spectral emissivity simultaneously from the three MODIS thermal infrared bands 29, 31, and 32. The TES algorithm is combined with an improved Water Vapor Scaling (WVS) atmospheric correction scheme to stabilize the retrieval during very warm and humid conditions. \r\n\r\nThe MYD21A1D dataset is produced daily from daytime Level 2 Gridded (L2G) intermediate LST products. The L2G process maps the daily MYD21 (https://doi.org/10.5067/MODIS/MYD21.061) swath granules onto a sinusoidal MODIS grid and stores all observations falling over a gridded cell for a given day. The MOD21A1 algorithm sorts through all these observations for each cell and estimates the final LST value as an average from all observations that are cloud free and have good LST&E accuracies. The daytime average is weighted by the observation coverage for that cell. Only observations having observation coverage more than a certain threshold (15%) are considered for this averaging. The MYD21A1D product contains seven Science Datasets (SDS), which include the calculated LST as well as quality control, the three emissivity bands, view zenith angle, and time of observation. Additional details regarding the methodology used to create this Level 3 (L3) product are available in the Algorithm Theoretical Basis Document (ATBD (https://lpdaac.usgs.gov/documents/1399/MOD21_ATBD.pdf)).\r\n\r\nValidation at stage 1 (https://modis-land.gsfc.nasa.gov/MODLAND_val.html) has been achieved for the MODIS Land Surface Temperature and Emissivity data products. Further details regarding MODIS land product validation for the MYD21 data products are available from the MODIS Land Team Validation site (https://modis-land.gsfc.nasa.gov/ValStatus.php?ProductID=MOD21).\r\n\r\nImprovements/Changes from Previous Versions\r\n* The Version 6.1 Level-1B (L1B) products have been improved by undergoing various calibration changes that include: changes to the response-versus-scan angle (RVS) approach that affects reflectance bands for Aqua and Terra MODIS, corrections to adjust for the optical crosstalk in Terra MODIS infrared (IR) bands, and corrections to the Terra MODIS forward look-up table (LUT) update for the period 2012 - 2017.\r\n* A polarization correction has been applied to the L1B Reflective Solar Bands (RSB).\r\n* The product utilizes GEOS data replacing MERRA2.\r\n* Three new CMG products are available in the MxD21 suite (MxD21C1/C2/C3).",
-            "release-place": "Sioux Falls, South Dakota, USA",
-            "graphic-preview-description": "Browse image for Earthdata Search",
             "creator": "Glynn Hulley",
-            "title": "MODIS/Aqua Land Surface Temperature/3-Band Emissivity Daily L3 Global 1km SIN Grid Day V061",
-            "graphic-preview-file": "https://cmr.earthdata.nasa.gov/browse-scaler/browse_images/granules/G2689275133-LPCLOUD?h=85&w=85",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "A suite of MODIS Land Surface Temperature and Emissivity  (LST&E) products are available in Collection 6.1. The MYD21 LST algorithm differs from the algorithm of the MYD11 (https://doi.org/10.5067/modis/myd11_l2.061) LST products, in that the MYD21 algorithm is based on the ASTER Temperature/Emissivity Separation (TES) technique, whereas the MYD11 uses the split-window technique. The MYD21 TES algorithm uses a physics-based algorithm to retrieve dynamically both the LST and spectral emissivity simultaneously from the three MODIS thermal infrared bands 29, 31, and 32. The TES algorithm is combined with an improved Water Vapor Scaling (WVS) atmospheric correction scheme to stabilize the retrieval during very warm and humid conditions. \r\n\r\nThe MYD21A1D dataset is produced daily from daytime Level 2 Gridded (L2G) intermediate LST products. The L2G process maps the daily MYD21 (https://doi.org/10.5067/MODIS/MYD21.061) swath granules onto a sinusoidal MODIS grid and stores all observations falling over a gridded cell for a given day. The MOD21A1 algorithm sorts through all these observations for each cell and estimates the final LST value as an average from all observations that are cloud free and have good LST&E accuracies. The daytime average is weighted by the observation coverage for that cell. Only observations having observation coverage more than a certain threshold (15%) are considered for this averaging. The MYD21A1D product contains seven Science Datasets (SDS), which include the calculated LST as well as quality control, the three emissivity bands, view zenith angle, and time of observation. Additional details regarding the methodology used to create this Level 3 (L3) product are available in the Algorithm Theoretical Basis Document (ATBD (https://lpdaac.usgs.gov/documents/1399/MOD21_ATBD.pdf)).\r\n\r\nValidation at stage 1 (https://modis-land.gsfc.nasa.gov/MODLAND_val.html) has been achieved for the MODIS Land Surface Temperature and Emissivity data products. Further details regarding MODIS land product validation for the MYD21 data products are available from the MODIS Land Team Validation site (https://modis-land.gsfc.nasa.gov/ValStatus.php?ProductID=MOD21).\r\n\r\nImprovements/Changes from Previous Versions\r\n* The Version 6.1 Level-1B (L1B) products have been improved by undergoing various calibration changes that include: changes to the response-versus-scan angle (RVS) approach that affects reflectance bands for Aqua and Terra MODIS, corrections to adjust for the optical crosstalk in Terra MODIS infrared (IR) bands, and corrections to the Terra MODIS forward look-up table (LUT) update for the period 2012 - 2017.\r\n* A polarization correction has been applied to the L1B Reflective Solar Bands (RSB).\r\n* The product utilizes GEOS data replacing MERRA2.\r\n* Three new CMG products are available in the MxD21 suite (MxD21C1/C2/C3).",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMODIS%2FMYD21A1D.061",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMODIS%2FMYD21A1D.061",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "application/x-hdf",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=C2565805783-LPCLOUD",
-                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=C2565805783-LPCLOUD",
+                    "mediaType": "application/x-hdf",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "application/x-hdf",
-                    "downloadURL": "https://e4ftl01.cr.usgs.gov/MOLA/MYD21A1D.061/",
-                    "description": "LP DAAC Data Pool provides direct access to available products via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "LP DAAC Data Pool provides direct access to available products via HTTPS.",
+                    "downloadURL": "https://e4ftl01.cr.usgs.gov/MOLA/MYD21A1D.061/",
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
-                    "downloadURL": "https://doi.org/10.5067/MODIS/MYD21A1D.061",
-                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
+                    "downloadURL": "https://doi.org/10.5067/MODIS/MYD21A1D.061",
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
-                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/filespec/MODIS/6/MYD21A1D",
-                    "description": "The File Specification provides a description of the product file including Scientific Data Sets and their attributes.",
                     "@type": "dcat:Distribution",
+                    "description": "The File Specification provides a description of the product file including Scientific Data Sets and their attributes.",
+                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/filespec/MODIS/6/MYD21A1D",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://opendap.cr.usgs.gov/opendap/hyrax/DP130/MOLA/MYD21A1D.061/contents.html",
-                    "description": "OPeNDAP provides direct access to data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "OPeNDAP provides direct access to data via HTTPS.",
+                    "downloadURL": "https://opendap.cr.usgs.gov/opendap/hyrax/DP130/MOLA/MYD21A1D.061/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
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
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/browse-scaler/browse_images/granules/G2689275133-LPCLOUD?h=85&w=85",
-                    "description": "Browse image for Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse image for Earthdata Search",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/browse-scaler/browse_images/granules/G2689275133-LPCLOUD?h=85&w=85",
+                    "mediaType": "text/html",
                     "title": "Get a related visualization"
                 }
             ],
+            "graphic-preview-description": "Browse image for Earthdata Search",
+            "graphic-preview-file": "https://cmr.earthdata.nasa.gov/browse-scaler/browse_images/granules/G2689275133-LPCLOUD?h=85&w=85",
+            "identifier": "C2565805783-LPCLOUD",
+            "issued": "2021-02-08",
+            "keyword": [
+                "surface thermal properties",
+                "earth science",
+                "land surface",
+                "ngda",
+                "surface radiative properties",
+                "national geospatial data asset"
+            ],
+            "landingPage": "https://doi.org/10.5067/MODIS/MYD21A1D.061",
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
+            "title": "MODIS/Aqua Land Surface Temperature/3-Band Emissivity Daily L3 Global 1km SIN Grid Day V061"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://techport.nasa.gov/view/10876",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2010-01-01",
-            "temporal": "2010-01-01T00:00:00Z/2014-01-01T00:00:00Z",
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
                 "fn": "Simon Bandler",
                 "hasEmail": "mailto:simon.r.bandler@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Science Mission Directorate"
-            },
-            "identifier": "TECHPORT_10876",
             "description": "\"We propose to develop a revolutionary x-ray camera for astrophysical imaging spectroscopy. High-resolution x-ray spectroscopy is a powerful tool for studying the evolving universe. Emission line ratios (e.g. within the He-like triplet) provide density and temperature diagnostics. Emission and absorption line energies identify ions and determine their velocities, and the shape of the lines can be used to study turbulence or the relativistic effects of a supermassive black hole. The grating spectrometers on the XMM and Chandra satellites demonstrated the power of high-resolution x-ray spectroscopy for astrophysics, but there remains a need for instrumentation that can provide higher spectral resolution with high throughput in the Fe-K band and that can enable spatial/spectral investigations of extended sources, such as supernova remnants and galaxy clusters. The instrumentation needed is a broad-band imaging spectrometer - basically an x-ray camera that can precisely resolve x-ray energies and fluxes over a large field-of-view.\n\n\n\n While we do not claim that in 3 years we will have developed such detectors, we advocate developing the technology that has the greatest potential for achieving this. Theoretically, magnetically-coupled microcalorimeters are best equipped to achieve sub-eV energy resolution in very large formats. We propose to build upon the work carried out by our group on metallic magnetic calorimeters (MMC) in the antecedent program. The great promise of MMCs for sub-eV energy resolution has been recognized for years. During our current research program, an accident in detector fabrication produced devices that derived their sensitivity from a different operating principle - the temperature dependence of a superconduc",
-            "title": "Magnetically-coupled microcalorimeter arrays for x-ray astrophysics with sub-eV spectral resolution and large format capability Project",
-            "programCode": [
-                "026:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "http://techport.nasa.gov/xml-api/10876",
                     "mediaType": "application/xml"
                 }
-            ]
+            ],
+            "identifier": "TECHPORT_10876",
+            "issued": "2010-01-01",
+            "keyword": [
+                "project",
+                "active"
+            ],
+            "landingPage": "http://techport.nasa.gov/view/10876",
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
+            "temporal": "2010-01-01T00:00:00Z/2014-01-01T00:00:00Z",
+            "title": "Magnetically-coupled microcalorimeter arrays for x-ray astrophysics with sub-eV spectral resolution and large format capability Project"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ASDC/SUBORBITAL/ARCTAS_Trajectory_Data_1",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2022-09-06. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/ASDC/SUBORBITAL/ARCTAS_Trajectory_Data_1.",
-            "issued": "2022-01-06",
-            "temporal": "2008-03-28T00:00:00Z/2008-07-15T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-09-06",
-            "keyword": [
-                "altitude",
-                "atmospheric pressure",
-                "earth science",
-                "atmosphere",
-                "atmospheric winds",
-                "atmospheric temperature"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Henry Fuelberg",
                 "hasEmail": "mailto:fuelberg@huey.met.fsu.edu"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/LARC/SD/ASDC"
-            },
-            "identifier": "C2449573919-LARC_ASDC",
             "description": "ARCTAS_Trajectory_Data is the Kinematic Backward and Forward Trajectories derived for the Arctic Research of the Composition of the Troposphere from Aircraft & Satellites sub-orbital campaign. The kinematic trajectories are driven by hourly FSU-WRF winds and initialized at a variety of pressure levels (flight level, 850 HPa, 700 HPa, 500 HPa, and 300 HPa). Data collection for this product is complete. \r\n\r\nThe Arctic is a critical region in understanding climate change. The responses of the Arctic to environmental perturbations such as warming, pollution, and emissions from forest fires in boreal Eurasia and North America include key processes such as the melting of ice sheets and permafrost, a decrease in snow albedo, and the deposition of halogen radical chemistry from sea salt aerosols to ice. Arctic Research of the Composition of the Troposphere from Aircraft and Satellites (ARCTAS) was a field campaign that explored environmental processes related to the high degree of climate sensitivity in the Arctic. ARCTAS was part of NASA\u2019s contribution to the International Global Atmospheric Chemistry (IGAC) Polar Study using Aircraft, Remote Sensing, Surface Measurements, and Models of Climate, Chemistry, Aerosols, and Transport (POLARCAT) Experiment for the International Polar Year 2007-2008.\r\n\r\nARCTAS had four primary objectives. The first was to understand long-range transport of pollution to the Arctic. Pollution brought to the Arctic from northern mid-latitude continents has environmental consequences, such as modifying regional and global climate and affecting the ozone budget. Prior to ARCTAS, these pathways remained largely uncertain. The second objective was to understand the atmospheric composition and climate implications of boreal forest fires; the smoke emissions from which act as an atmospheric perturbation to the Arctic by impacting the radiation budget and cloud processes and contributing to the production of tropospheric ozone. The third objective was to understand aerosol radiative forcing from climate perturbations, as the Arctic is an important place for understanding radiative forcing due to the rapid pace of climate change in the region and its unique radiative environment. The fourth objective of ARCTAS was to understand chemical processes with a focus on ozone, aerosols, mercury, and halogens. Additionally, ARCTAS sought to develop capabilities for incorporating data from aircraft and satellites related to pollution and related environmental perturbations in the Arctic into earth science models, expanding the potential for those models to predict future environmental change.\r\n\r\nARCTAS consisted of two, three-week aircraft deployments conducted in April and July 2008. The spring deployment sought to explore arctic haze, stratosphere-troposphere exchange, and sunrise photochemistry. April was chosen for the deployment phase due to historically being the peak in the seasonal accumulation of pollution from northern mid-latitude continents in the Arctic. The summer deployment sought to understand boreal forest fires at their most active seasonal phase in addition to stratosphere-troposphere exchange and summertime photochemistry.\r\n\r\nDuring ARCTAS, three NASA aircrafts, the DC-8, P-3B, and BE-200, conducted measurements and were equipped with suites of in-situ and remote sensing instrumentation. Airborne data was used in conjunction with satellite observations from AURA, AQUA, CloudSat, PARASOL, CALIPSO, and MISR.\r\n\r\nThe ASDC houses ARCTAS aircraft data, along with data related to MISR, a satellite instrument aboard the Terra satellite which provides measurements that provide information about the Earth\u2019s environment and climate.",
-            "title": "ARCTAS Kinematic Trajectories",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC%2FSUBORBITAL%2FARCTAS_Trajectory_Data_1",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC%2FSUBORBITAL%2FARCTAS_Trajectory_Data_1",
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
-                    "downloadURL": "https://espo.nasa.gov/arctas/",
-                    "description": "ESPO Home Page for ARCTAS",
                     "@type": "dcat:Distribution",
+                    "description": "ESPO Home Page for ARCTAS",
+                    "downloadURL": "https://espo.nasa.gov/arctas/",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
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
-                    "downloadURL": "https://doi.org/10.5067/ASDC/SUBORBITAL/ARCTAS_Trajectory_Data_1",
-                    "description": "DOI for ARCTAS_Trajectory_Data_1",
                     "@type": "dcat:Distribution",
+                    "description": "DOI for ARCTAS_Trajectory_Data_1",
+                    "downloadURL": "https://doi.org/10.5067/ASDC/SUBORBITAL/ARCTAS_Trajectory_Data_1",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2449573919-LARC_ASDC",
-                    "description": "Earthdata Search client for ARCTAS_Trajectory_Data_1",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search client for ARCTAS_Trajectory_Data_1",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2449573919-LARC_ASDC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/ARCTAS/Trajectory_Data_1/",
-                    "description": "ASDC Direct Data Download for ARCTAS_Trajectory_Data_1",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for ARCTAS_Trajectory_Data_1",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/ARCTAS/Trajectory_Data_1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 }
             ],
+            "identifier": "C2449573919-LARC_ASDC",
+            "issued": "2022-01-06",
+            "keyword": [
+                "altitude",
+                "atmospheric pressure",
+                "earth science",
+                "atmosphere",
+                "atmospheric winds",
+                "atmospheric temperature"
+            ],
+            "landingPage": "https://doi.org/10.5067/ASDC/SUBORBITAL/ARCTAS_Trajectory_Data_1",
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
             "spatial": "<?xml version=\"1.0\" encoding=\"UTF-8\"?><gml:Polygon xmlns:gml=\"http://www.opengis.net/gml/3.2\" srsName=\"EPSG:9825\"><gml:outerBoundaryIs><gml:LinearRing><gml:posList>7.5 -180.0 7.5 180.0 90.0 180.0 90.0 -180.0 7.5 -180.0</gml:posList></gml:LinearRing></gml:outerBoundaryIs><gml:innerBoundaryIs></gml:innerBoundaryIs></gml:Polygon>",
+            "temporal": "2008-03-28T00:00:00Z/2008-07-15T23:59:59.999Z",
             "theme": [
                 "ARCTAS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "ARCTAS Kinematic Trajectories"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MEX-M-MRS-1%2F2%2F3-EXT3-3342-V1.0",
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
+            "description": "This is a Mars Express Radio Science data set, collected during the extended mission phase 2010-01-01 to 2012-12-31. It is a Global Gravity measurement and covers the time 2012-07-08T10:41:23.000 to 2012-07-08T13:35:44.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mex-m-mrs-1-2-3-ext3-3342-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "mars express",
+                "mars"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MEX-M-MRS-1%2F2%2F3-EXT3-3342-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mex-m-mrs-1-2-3-ext3-3342-v1.0",
-            "description": "This is a Mars Express Radio Science data set, collected during the extended mission phase 2010-01-01 to 2012-12-31. It is a Global Gravity measurement and covers the time 2012-07-08T10:41:23.000 to 2012-07-08T13:35:44.000.",
-            "title": "MARS EXPRESS MARS MRS 1/2/3\n                                     EXTENDED MISSION 3 3342 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "MARS EXPRESS MARS MRS 1/2/3\n                                     EXTENDED MISSION 3 3342 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/MODIS/MOD09CMA.NRT.061",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "LANCEMODIS. 2021-02-07. MODIS/Terra Aerosol Optical Thickness Daily L3 Global 0.05Deg CMA NRT. Version 6.1NRT. MODAPS at NASA/GSFC. Archived by National Aeronautics and Space Administration, U.S. Government, The Land, Atmosphere Near real-time Capability for EOS (LANCE). https://doi.org/10.5067/MODIS/MOD09CMA.NRT.061.",
-            "issued": "2021-02-07",
-            "temporal": "2021-02-07T00:00:00Z/2023-07-24T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-20",
-            "keyword": [
-                "atmosphere",
-                "national geospatial data asset",
-                "earth science",
-                "ngda",
-                "aerosols"
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
-            "identifier": "C2007660084-LANCEMODIS",
-            "description": "The MODIS/Terra Aerosol Optical Thickness Daily L3 Global 0.05Deg CMA Neal Real Time (NRT) Product (MOD09CMA) is a daily level 3 and global product. It is in linear latitude and longitude (Plate Carre) projection with a 0.05Deg spatial resolution. This product is derived from MOD09IDN, MOD09IDT and MOD09IDS for each orbit by compositing the data on the basis of minimum band 3 (459 - 479 nm band) values (after excluding pixels flagged for clouds and high solar zenith angles).",
-            "release-place": "MODAPS at NASA/GSFC",
             "creator": "LANCEMODIS",
-            "title": "MODIS/Terra Aerosol Optical Thickness Daily L3 Global 0.05Deg CMA NRT",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The MODIS/Terra Aerosol Optical Thickness Daily L3 Global 0.05Deg CMA Neal Real Time (NRT) Product (MOD09CMA) is a daily level 3 and global product. It is in linear latitude and longitude (Plate Carre) projection with a 0.05Deg spatial resolution. This product is derived from MOD09IDN, MOD09IDT and MOD09IDS for each orbit by compositing the data on the basis of minimum band 3 (459 - 479 nm band) values (after excluding pixels flagged for clouds and high solar zenith angles).",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMODIS%2FMOD09CMA.NRT.061",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMODIS%2FMOD09CMA.NRT.061",
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
-                    "downloadURL": "https://nrt3.modaps.eosdis.nasa.gov/archive/allData/61/MOD09CMA",
-                    "description": "Direct access to the download site and directory hosting the MOD09CMA 6.1NRT data set.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct access to the download site and directory hosting the MOD09CMA 6.1NRT data set.",
+                    "downloadURL": "https://nrt3.modaps.eosdis.nasa.gov/archive/allData/61/MOD09CMA",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 }
             ],
+            "identifier": "C2007660084-LANCEMODIS",
+            "issued": "2021-02-07",
+            "keyword": [
+                "atmosphere",
+                "national geospatial data asset",
+                "earth science",
+                "ngda",
+                "aerosols"
+            ],
+            "landingPage": "https://doi.org/10.5067/MODIS/MOD09CMA.NRT.061",
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
             "spatial": "-180.0 -81.0 180.0 81.0",
+            "temporal": "2021-02-07T00:00:00Z/2023-07-24T00:00:00Z",
             "theme": [
                 "Terra",
                 "CWIC",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "MODIS/Terra Aerosol Optical Thickness Daily L3 Global 0.05Deg CMA NRT"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RPCLAP-2-PRL-MTP004-V2.0",
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
+            "description": "This data set contains\nEDITED data from Rosetta RPC-LAP, acquired during the PRELANDING\nMTP004 mission phase. Comet C-G/67P was the primary target.\nThis data set supersedes RO-C-RPCLAP-2-PRL-EDITED-V1.0 and is only\nthe MTP004 part of it.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rpclap-2-prl-mtp004-v2.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RPCLAP-2-PRL-MTP004-V2.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rpclap-2-prl-mtp004-v2.0",
-            "description": "This data set contains\nEDITED data from Rosetta RPC-LAP, acquired during the PRELANDING\nMTP004 mission phase. Comet C-G/67P was the primary target.\nThis data set supersedes RO-C-RPCLAP-2-PRL-EDITED-V1.0 and is only\nthe MTP004 part of it.",
-            "title": "ROSETTA-ORBITER 67P RPCLAP 2\nPRL MTP004 V2.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RPCLAP 2\nPRL MTP004 V2.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://aeronet.gsfc.nasa.gov/new_web/ocean_color.html",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2018-06-25",
-            "temporal": "2002-01-01/2014-01-01",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
-            "references": [
-                "http://aeronet.gsfc.nasa.gov/new_web/Documents/Feb232011.zip",
-                "http://aeronet.gsfc.nasa.gov/new_web/Documents/Feb242011.zip"
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Brent Holben",
+                "hasEmail": "mailto:Brent.N.Holben@nasa.gov"
+            },
+            "describedBy": "http://aeronet.gsfc.nasa.gov/new_web/units-ocean.html",
+            "description": "The Aerosol Robotic Network (AERONET), developed to sustain atmospheric studies at various scales with measurements from worldwide distributed autonomous sun-photometers has  been extended to support marine applications. This new network component called AERONET \u2013 Ocean Color (AERONET-OC), provides the additional capability of measuring the radiance emerging from the sea  (i.e., water-leaving radiance) with modified sun-photometers installed on offshore platforms like lighthouses, oceanographic and oil towers. AERONET-OC is instrumental in satellite ocean color validation activities through standardized measurements a) performed at different sites with a single measuring system and protocol, b) calibrated with an identical reference source and method, and c) processed with the same code.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://aeronet.gsfc.nasa.gov/cgi-bin/type_piece_of_map_seaprism_new?long1=-180&long2=180&lat1=-90&lat2=90&multiplier=2&what_map=4&nachal=1&formatter=0&level=2",
+                    "mediaType": "text/html"
+                }
             ],
+            "identifier": "NASA-0000007__1",
+            "issued": "2018-06-25",
             "keyword": [
                 "radiation",
                 "precipitable water",
@@ -1325149,220 +1325157,214 @@
                 "earth science",
                 "satellite"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Brent Holben",
-                "hasEmail": "mailto:Brent.N.Holben@nasa.gov"
-            },
+            "landingPage": "http://aeronet.gsfc.nasa.gov/new_web/ocean_color.html",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:001"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "NASA-0000007__1",
-            "description": "The Aerosol Robotic Network (AERONET), developed to sustain atmospheric studies at various scales with measurements from worldwide distributed autonomous sun-photometers has  been extended to support marine applications. This new network component called AERONET \u2013 Ocean Color (AERONET-OC), provides the additional capability of measuring the radiance emerging from the sea  (i.e., water-leaving radiance) with modified sun-photometers installed on offshore platforms like lighthouses, oceanographic and oil towers. AERONET-OC is instrumental in satellite ocean color validation activities through standardized measurements a) performed at different sites with a single measuring system and protocol, b) calibrated with an identical reference source and method, and c) processed with the same code.",
-            "title": "AERONET-OCEAN COLOR",
-            "programCode": [
-                "026:001"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://aeronet.gsfc.nasa.gov/cgi-bin/type_piece_of_map_seaprism_new?long1=-180&long2=180&lat1=-90&lat2=90&multiplier=2&what_map=4&nachal=1&formatter=0&level=2",
-                    "mediaType": "text/html"
-                }
+            "references": [
+                "http://aeronet.gsfc.nasa.gov/new_web/Documents/Feb232011.zip",
+                "http://aeronet.gsfc.nasa.gov/new_web/Documents/Feb242011.zip"
             ],
             "spatial": "Global",
-            "describedBy": "http://aeronet.gsfc.nasa.gov/new_web/units-ocean.html",
-            "accrualPeriodicity": "irregular",
+            "temporal": "2002-01-01/2014-01-01",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "AERONET-OCEAN COLOR"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ERS2B-SNEN0",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "BYU/SCP. 2011-11-29. ERS-2 Gridded Level 3 Enhanced Resolution Sigma-0 from BYU. Version 1. ERS-2 Gridded Level 3 Enhanced Resolution Sigma-0 from BYU. PO.DAAC. Archived by National Aeronautics and Space Administration, U.S. Government, PO.DAAC. https://doi.org/10.5067/ERS2B-SNEN0. https://podaac-tools.jpl.nasa.gov/drive/files/allData/ers2/L3/byu_scp/sigma0enhanced/docs/dLongERS2.html. BYU/SCP, PO.DAAC, 2011-11-29, ERS-2 Gridded Level 3 Enhanced Resolution Sigma-0 from BYU, https://podaac-tools.jpl.nasa.gov/drive/files/allData/ers2/L3/byu_scp/sigma0enhanced/docs/dLongERS2.html.",
-            "issued": "2011-11-21",
-            "temporal": "1996-06-03T00:00:00Z/2001-12-30T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2011-11-21",
-            "keyword": [
-                "radar",
-                "earth science",
-                "cryosphere",
-                "sea ice",
-                "spectral/engineering"
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
-            "identifier": "C2617226211-POCLOUD",
-            "description": "This European Remote Sensing (ERS) Sigma-0 dataset is generated by the Scatterometer Climate Record Pathfinder (SCP) project at Brigham Young University (BYU) and is generated using a Scatterometer Image Reconstruction (SIR) technique developed by Dr. David Long at BYU. The dataset provides SIR processed Sigma-0 data from the ERS-2 C-band scatterometer, which is also known as the Active Microwave Instrument (AMI). AMI is a multimode radar operating at a frequency of 5.3 GHz (C-band), using vertically polarized antennas for both transmission and reception. The SIR technique results in an enhanced resolution image reconstruction and gridded on an equal-area grid (for non-polar regions) at 8.9 km pixel resolution stored in SIR files; polar regions are gridded at the same resolution using a polar-stereographic technique. A non-enhanced version is provided at 44.5 km pixel resolution in a format known as GRD (i.e., gridded) files. All files are produced in IEEE formatted binary. All data files are separated and organized by region, parameter, and sampling technique (i.e., SIR vs. GRD). The regions of China and Japan are combined into a single region. In addition to Sigma-0, various statistical parameters are provided for added guidance, including but not limited to: standard deviation, measurement counts, pixel time, Sigma-0 error, and average incidence angle. This dataset was once distributed on tape, but has been made available on FTP thanks to the BYU SCP. For more information, please visit: http://www.scp.byu.edu/docs/ERS_user_notes.html",
-            "release-place": "PO.DAAC",
-            "series-name": "ERS-2 Gridded Level 3 Enhanced Resolution Sigma-0 from BYU",
-            "graphic-preview-description": "Thumbnail",
             "creator": "BYU/SCP",
-            "title": "ERS-2 Gridded Level 3 Enhanced Resolution Sigma-0 from BYU",
-            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/ERS-2_BYU_L3_OW_SIGMA0_ENHANCED.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "This European Remote Sensing (ERS) Sigma-0 dataset is generated by the Scatterometer Climate Record Pathfinder (SCP) project at Brigham Young University (BYU) and is generated using a Scatterometer Image Reconstruction (SIR) technique developed by Dr. David Long at BYU. The dataset provides SIR processed Sigma-0 data from the ERS-2 C-band scatterometer, which is also known as the Active Microwave Instrument (AMI). AMI is a multimode radar operating at a frequency of 5.3 GHz (C-band), using vertically polarized antennas for both transmission and reception. The SIR technique results in an enhanced resolution image reconstruction and gridded on an equal-area grid (for non-polar regions) at 8.9 km pixel resolution stored in SIR files; polar regions are gridded at the same resolution using a polar-stereographic technique. A non-enhanced version is provided at 44.5 km pixel resolution in a format known as GRD (i.e., gridded) files. All files are produced in IEEE formatted binary. All data files are separated and organized by region, parameter, and sampling technique (i.e., SIR vs. GRD). The regions of China and Japan are combined into a single region. In addition to Sigma-0, various statistical parameters are provided for added guidance, including but not limited to: standard deviation, measurement counts, pixel time, Sigma-0 error, and average incidence angle. This dataset was once distributed on tape, but has been made available on FTP thanks to the BYU SCP. For more information, please visit: http://www.scp.byu.edu/docs/ERS_user_notes.html",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FERS2B-SNEN0",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FERS2B-SNEN0",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/ERS-2_BYU_L3_OW_SIGMA0_ENHANCED.jpg",
-                    "description": "Thumbnail",
                     "@type": "dcat:Distribution",
+                    "description": "Thumbnail",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/ERS-2_BYU_L3_OW_SIGMA0_ENHANCED.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/ers2/open/L3/byu_scp/sigma0enhanced/docs/dLongERS2.html",
-                    "description": "Dataset User Guide",
                     "@type": "dcat:Distribution",
+                    "description": "Dataset User Guide",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/ers2/open/L3/byu_scp/sigma0enhanced/docs/dLongERS2.html",
+                    "mediaType": "text/html",
                     "title": "View this dataset's user's guide"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/ers1/open/L3/byu_scp/sigma0enhanced/docs/dLongERS1.html",
-                    "description": "PO.DAAC Drive",
                     "@type": "dcat:Distribution",
+                    "description": "PO.DAAC Drive",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/ers1/open/L3/byu_scp/sigma0enhanced/docs/dLongERS1.html",
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
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2617226211-POCLOUD",
-                    "description": "HTTPS endpoint for data browse and download",
                     "@type": "dcat:Distribution",
+                    "description": "HTTPS endpoint for data browse and download",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2617226211-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2617226211-POCLOUD",
-                    "description": "Browse granule search results in Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse granule search results in Earthdata Search",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2617226211-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 }
             ],
+            "graphic-preview-description": "Thumbnail",
+            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/ERS-2_BYU_L3_OW_SIGMA0_ENHANCED.jpg",
+            "identifier": "C2617226211-POCLOUD",
+            "issued": "2011-11-21",
+            "keyword": [
+                "radar",
+                "earth science",
+                "cryosphere",
+                "sea ice",
+                "spectral/engineering"
+            ],
+            "landingPage": "https://doi.org/10.5067/ERS2B-SNEN0",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2011-11-21",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/JPL/PODAAC"
+            },
+            "release-place": "PO.DAAC",
+            "series-name": "ERS-2 Gridded Level 3 Enhanced Resolution Sigma-0 from BYU",
             "spatial": "-180.0 -79.7 180.0 88.2",
+            "temporal": "1996-06-03T00:00:00Z/2001-12-30T23:59:59Z",
             "theme": [
                 "SCP",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "ERS-2 Gridded Level 3 Enhanced Resolution Sigma-0 from BYU"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=A14A-L-CCIG-3-ATMOS-DENSITY-PLOTS-V1.0",
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
-                "apollo 14",
-                "moon"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This data set contains digitized plots of the density of the lunar atmosphere as measured by the Apollo 14 Cold Cathode Ion Gage from 09 February 1971 through 31 December 1973.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.a14a-l-ccig-3-atmos-density-plots-v1.0_ru3i-psrn",
+            "issued": "2018-06-26",
+            "keyword": [
+                "apollo 14",
+                "moon"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=A14A-L-CCIG-3-ATMOS-DENSITY-PLOTS-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.a14a-l-ccig-3-atmos-density-plots-v1.0_ru3i-psrn",
-            "description": "This data set contains digitized plots of the density of the lunar atmosphere as measured by the Apollo 14 Cold Cathode Ion Gage from 09 February 1971 through 31 December 1973.",
-            "title": "APOLLO 14 ALSEP/CCIG REDUCED ATMOSPHERIC DENSITY PLOTS V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "APOLLO 14 ALSEP/CCIG REDUCED ATMOSPHERIC DENSITY PLOTS V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-4-ESC4-67P-M23-STRLIGHT-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This CODMAC level 4 data set contains solar stray light corrected, radiometric calibrated and geometric distortion corrected (resampled) image data in W/m^2/sr/nm, acquired by the OSIRIS Wide Angle Camera on the Rosetta spacecraft during the COMET ESCORT 4 mission phase, covering the period from 2015-11-17T23:25:00.000 to 2015-12-15T23:24:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V1.0 is the first version of this dataset: Lien corrected dataset after October 2018 PSA/PDS external peer review.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-4-esc4-67p-m23-strlight-v1.0_ru6m-kd8s",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "international rosetta mission",
                 "zeta cas",
                 "67p/churyumov-gerasimenko 1 (1969 r1)",
                 "vega"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-4-ESC4-67P-M23-STRLIGHT-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-4-esc4-67p-m23-strlight-v1.0_ru6m-kd8s",
-            "description": "This CODMAC level 4 data set contains solar stray light corrected, radiometric calibrated and geometric distortion corrected (resampled) image data in W/m^2/sr/nm, acquired by the OSIRIS Wide Angle Camera on the Rosetta spacecraft during the COMET ESCORT 4 mission phase, covering the period from 2015-11-17T23:25:00.000 to 2015-12-15T23:24:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V1.0 is the first version of this dataset: Lien corrected dataset after October 2018 PSA/PDS external peer review.",
-            "title": "ROSETTA-ORBITER 67P OSIWAC 4 ESC4-MTP023 RDR-STRLIGHT V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P OSIWAC 4 ESC4-MTP023 RDR-STRLIGHT V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-NAVCAM-3-EXT1-MTP026-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This dataset contains ROSETTA NAVCAM RADIOMETRICALLY CALIBRATED DATA of the ROSETTA EXTENSION 1 MTP026 Phase from 10 Feb. 2016, 06:04:22 to 08 Mar. 2016, 23:17:57 when at the vicinity of target 67P/CG.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-navcam-3-ext1-mtp026-v1.0",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2021-05-21",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "bias",
                 "67p/churyumov-gerasimenko 1 (1969 r1)",
@@ -1325370,109 +1325372,121 @@
                 "alpha lyr",
                 "international rosetta mission"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-NAVCAM-3-EXT1-MTP026-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-navcam-3-ext1-mtp026-v1.0",
-            "description": "This dataset contains ROSETTA NAVCAM RADIOMETRICALLY CALIBRATED DATA of the ROSETTA EXTENSION 1 MTP026 Phase from 10 Feb. 2016, 06:04:22 to 08 Mar. 2016, 23:17:57 when at the vicinity of target 67P/CG.",
-            "title": "ROSETTA-ORBITER 67P NAVCAM 3 ROSETTA EXTENSION 1 MTP026 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P NAVCAM 3 ROSETTA EXTENSION 1 MTP026 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=GP-J-EPI-3-ENTRY-V1.0",
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
-                "galileo"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "The Galileo Probe Energetic Particles Investigation (EPI) Raw Data Set contains two tables of the EPI raw data values sorted by sampling time. The counter table contains the raw counter values as measured and the countrate table contains the countrates as derived from counter values, but without any correction. The tables are split into omnidirectional and sectorized data. The distance to Jupiter is given in Jupiter radii, Rj, and was derived from the Probe trajectory data. The time of probe entry is taken to be 1995-12-07T22:04:44Z when the probe reached an altitude of 450 km above the 1 bar pressure level.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.gp-j-epi-3-entry-v1.0_ru89-qgm5",
+            "issued": "2021-05-21",
+            "keyword": [
+                "jupiter",
+                "galileo"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=GP-J-EPI-3-ENTRY-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.gp-j-epi-3-entry-v1.0_ru89-qgm5",
-            "description": "The Galileo Probe Energetic Particles Investigation (EPI) Raw Data Set contains two tables of the EPI raw data values sorted by sampling time. The counter table contains the raw counter values as measured and the countrate table contains the countrates as derived from counter values, but without any correction. The tables are split into omnidirectional and sectorized data. The distance to Jupiter is given in Jupiter radii, Rj, and was derived from the Probe trajectory data. The time of probe entry is taken to be 1995-12-07T22:04:44Z when the probe reached an altitude of 450 km above the 1 bar pressure level.",
-            "title": "GALILEO PROBE EPI RAW DATA SET",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "GALILEO PROBE EPI RAW DATA SET"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VEGA2-C-PM1-2-RDR-HALLEY-V1.0",
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
-                "vega 2",
-                "halley"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "The PLASMAG-1 instument package included six different sensors: A0 plasma impact detector for measuring neutral particle flux, (manufactured by R. Grard, ESA/ESTEC, Noordwijk, The Netherlands) A1 Faraday cup for measuring integral ion flux from solar direction, A2 Faraday cup for measuring integral ion flux and neutral particles from ram direction, A3 spherical electrostatic analyzer for measuring ions from ram direction in the energy range of 15 eV - 3.6 keV in 120 logarithmically spaced channels, A4 spherical electrostatic analyzer for measuring ions from solar direction in the energy range of 60 eV - 30 keV in 60 logarithmically spaced channels, A5 cylindrical electrostatic analyzer for measuring ions perpendicular to the ecliptic plane in the energy range of 2 eV - 10 keV in 30 logarithmically spaced channels.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vega2-c-pm1-2-rdr-halley-v1.0_ru8r-yhri",
+            "issued": "2018-06-26",
+            "keyword": [
+                "vega 2",
+                "halley"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VEGA2-C-PM1-2-RDR-HALLEY-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vega2-c-pm1-2-rdr-halley-v1.0_ru8r-yhri",
-            "description": "The PLASMAG-1 instument package included six different sensors: A0 plasma impact detector for measuring neutral particle flux, (manufactured by R. Grard, ESA/ESTEC, Noordwijk, The Netherlands) A1 Faraday cup for measuring integral ion flux from solar direction, A2 Faraday cup for measuring integral ion flux and neutral particles from ram direction, A3 spherical electrostatic analyzer for measuring ions from ram direction in the energy range of 15 eV - 3.6 keV in 120 logarithmically spaced channels, A4 spherical electrostatic analyzer for measuring ions from solar direction in the energy range of 60 eV - 30 keV in 60 logarithmically spaced channels, A5 cylindrical electrostatic analyzer for measuring ions perpendicular to the ecliptic plane in the energy range of 2 eV - 10 keV in 30 logarithmically spaced channels.",
-            "title": "VEGA2 PLASMAG-1 PLASMA ENERGY ANALYSER DATA V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "VEGA2 PLASMAG-1 PLASMA ENERGY ANALYSER DATA V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.nasa.gov/d/ruau-afxq",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "GeneLab Outreach",
+                "hasEmail": "mailto:genelab-outreach@lists.nasa.gov"
+            },
+            "description": "Transcriptional crosstalk between mammary gland liver and adipose tissue Experiment Overall Design: Pregnant and Lactating rats exposed to 3 gravity conditions",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "GeneLab Study Page",
+                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-63",
+                    "mediaType": "text/html",
+                    "title": "Transcription profiling of rat response to changes in developmental stage - 3 types of tissue 3 gravity conditions 2 developmental conditions"
+                }
+            ],
+            "identifier": "nasa_genelab_GLDS-63_ruau-afxq",
             "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
             "keyword": [
                 "p-g12132-1",
                 "microgravity",
@@ -1325487,336 +1325501,301 @@
                 "radiation dosimetry",
                 "nucleic_acid_extraction"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "GeneLab Outreach",
-                "hasEmail": "mailto:genelab-outreach@lists.nasa.gov"
-            },
+            "landingPage": "https://data.nasa.gov/d/ruau-afxq",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "nasa_genelab_GLDS-63_ruau-afxq",
-            "description": "Transcriptional crosstalk between mammary gland liver and adipose tissue Experiment Overall Design: Pregnant and Lactating rats exposed to 3 gravity conditions",
-            "title": "Transcription profiling of rat response to changes in developmental stage - 3 types of tissue 3 gravity conditions 2 developmental conditions",
-            "programCode": [
-                "026:005"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-63",
-                    "description": "GeneLab Study Page",
-                    "@type": "dcat:Distribution",
-                    "title": "Transcription profiling of rat response to changes in developmental stage - 3 types of tissue 3 gravity conditions 2 developmental conditions"
-                }
-            ],
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "Transcription profiling of rat response to changes in developmental stage - 3 types of tissue 3 gravity conditions 2 developmental conditions"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RPCIES-5-ESC4-V1.0",
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
+            "description": "This dataset contains DERIVED DATA of the Rosetta RPCIES instrument taken during the comet escort 4 phase (ESC4). The target of this phase was comet 67P/CHURYUMOV-GERASIMENKO 1 (1969 R1). Included are the data taken between 22 Oct 2015 and 31 Dec 2015.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rpcies-5-esc4-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RPCIES-5-ESC4-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rpcies-5-esc4-v1.0",
-            "description": "This dataset contains DERIVED DATA of the Rosetta RPCIES instrument taken during the comet escort 4 phase (ESC4). The target of this phase was comet 67P/CHURYUMOV-GERASIMENKO 1 (1969 R1). Included are the data taken between 22 Oct 2015 and 31 Dec 2015.",
-            "title": "ROSETTA-ORBITER 67P RPCIES 5 ESC4 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RPCIES 5 ESC4 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/938",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Brondizio, E.S., and E.F. Moran. 2009. LBA-ECO LC-09 Soil Composition and Structure in the Brazilian Amazon: 1992-1995. ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/938",
-            "issued": "2023-10-03",
-            "temporal": "1992-01-01T00:00:00Z/1993-12-31T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-10-05",
-            "keyword": [
-                "soils",
-                "land use/land cover",
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
-            "identifier": "C2777751083-ORNL_CLOUD",
             "description": "This data set reports basic soil structure and composition information for five Amazonian research sites: Altamira, Bragantina, Tome-Acu, and Ponta de Pedras, all four in the state of Para, Brazil; and one site in Yapu, Colombia. Soil characteristics reported for all five study sites include cation information (e.g., H, Al, Mg, K, Na, S), percent of soil C, N, and organic matter, soil texture/composition and color, pH, and land use history. Soil bulk density and tons of carbon/ha are reported for only three of the study sites: Altamira, Bragantina, and Tome-Acu. All of the data are provided in one comma-separated data file.The five study areas represent characteristic differences in soil fertility and a range of land uses typical of the Amazon region. One of these areas, Altamira, is characterized by above average pH, nutrients, and texture. The other four areas are more typical of the 75 percent of the Amazon that is characterized by Oxisols and Ultisols, with well-drained but low pH and low levels of nutrients. Ponta de Pedras in Marajo Island, located in the estuary, is composed of upland Oxisols and floodplain alluvial soils. Igarape-Acu in the Bragantina region is characterized by both nutrient-poor Spodosols and Oxisols. Tome-Acu, south of Igarape-Acu, represents a mosaic of Oxisols and Ultisols. Yapu, in the Colombian Vaupes, is composed of patches of Spodosols and Oxisols. Three of the areas are colonization regions at various degrees of development: Altamira is a colonization front that opened up in 1971, whereas Tome-Acu was settled by a Japanese population in the 1930s, and Bragantina was settled in the early part of the twentieth century. Marajo (Ponta de Pedras) is the home of caboclos, whereas Yapu is home to Tukanoan Native American populations. In these study areas  slash-and-burn cultivation as well as plantation agriculture and mechanized agriculture are employed. Length of fallows vary in these communities. The two indigenous areas leave their land in longer fallow than do the three colonization areas, and the proportion of land prepared from secondary forests increases with length of settlement as the stock of mature forest declines over time.",
-            "graphic-preview-description": "Browse Image",
-            "title": "LBA-ECO LC-09 Soil Composition and Structure in the Brazilian Amazon: 1992-1995",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/lba_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F938",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F938",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/lba/land_use_land_cover_change/LC09_Soil_Composition/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/lba/land_use_land_cover_change/LC09_Soil_Composition/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/LBA/guides/LC09_Soil_Composition.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/LBA/guides/LC09_Soil_Composition.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/938",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/938",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC09_Soil_Composition/comp/LC09_Soil_Composition.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC09_Soil_Composition/comp/LC09_Soil_Composition.pdf",
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
+            "identifier": "C2777751083-ORNL_CLOUD",
+            "issued": "2023-10-03",
+            "keyword": [
+                "soils",
+                "land use/land cover",
+                "land surface",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/938",
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
             "spatial": "-54.0 -4.0 -51.0 -2.5",
+            "temporal": "1992-01-01T00:00:00Z/1993-12-31T23:59:59Z",
             "theme": [
                 "LBA-ECO",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "LBA-ECO LC-09 Soil Composition and Structure in the Brazilian Amazon: 1992-1995"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-EXT1-1344-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the ROSETTA EXTENSION 1 phase 2016-01-01 to 2016-04-05. It is a Global Gravity measurement at the comet 67P and covers the time 2016-01-15T05:18:00.000 to 2016-01-15T14:11:50.999.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-ext1-1344-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-EXT1-1344-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-ext1-1344-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the ROSETTA EXTENSION 1 phase 2016-01-01 to 2016-04-05. It is a Global Gravity measurement at the comet 67P and covers the time 2016-01-15T05:18:00.000 to 2016-01-15T14:11:50.999.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     ROSETTA EXTENSION 1 1344 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     ROSETTA EXTENSION 1 1344 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/FXX5S2VP2FVI",
             "citation": "Natalya Kramarova. 2024-07-11. OMPS_NPP_NPBUVO3_L2. Version 2.9. OMPS-NPP L2 NP Ozone (O3) Vertical Profile swath orbital V2.9. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/FXX5S2VP2FVI. https://disc.gsfc.nasa.gov/datacollection/OMPS_NPP_NPBUVO3_L2_2.9.html. Digital Science Data.",
-            "issued": "2023-11-14",
-            "temporal": "2011-11-13T00:00:00Z/2024-07-15T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-11-14",
-            "references": [
-                "https://doi.org/10.5194/amt-6-2533-2013"
-            ],
-            "keyword": [
-                "atmosphere",
-                "atmospheric chemistry",
-                "earth science"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "NATALYA KRAMAROVA",
                 "hasEmail": "mailto:Natalya.Kramarova@nasa.gov"
             },
+            "creator": "Natalya Kramarova",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C2821060582-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "The OMPS-NPP L2 NP Ozone (O3) Total Column swath orbital product provides ozone profile retrievals from the Ozone Mapping and Profiling Suite (OMPS) Nadir-Profiler (NP) instrument on the Suomi-NPP satellite. The V8 ozone profile algorithm relies on nadir profiler measurements made in the 250 to 310 nm range, as well as from measurements from the nadir mapper in the 300 to 380 nm range. Ozone mixing ratios are reported at 15 pressure levels between 50 and 0.5 hPa. Additionally, this data product contains measurements of total ozone, UV aerosol index and reflectivities at 331 and 380 nm.\n\nEach granule contains data from the daylight portion of each orbit measured for a full day. Spatial coverage is global (-82 to +82 degrees latitude), and there are about 14.5 orbits per day, each has typically 80 profiles. The NP footprint size is 250 km x 250 km. The files are written using the Hierarchical Data Format Version 5 or HDF5.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "OMPS_NPP_NPBUVO3_L2",
-            "creator": "Natalya Kramarova",
-            "graphic-preview-description": "OMPS Logo",
-            "title": "OMPS-NPP L2 NP Ozone (O3) Vertical Profile swath orbital V2.9 (OMPS_NPP_NPBUVO3_L2) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/OMPS_NPP_NPBUVO3_L2_2.9.jpeg",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FFXX5S2VP2FVI",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FFXX5S2VP2FVI",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/OMPS_NPP_NPBUVO3_L2_2.9.jpeg",
-                    "description": "OMPS Logo",
                     "@type": "dcat:Distribution",
+                    "description": "OMPS Logo",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/OMPS_NPP_NPBUVO3_L2_2.9.jpeg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/OMPS_NPP_NPBUVO3_L2_2.9.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/OMPS_NPP_NPBUVO3_L2_2.9.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://omps.gesdisc.eosdis.nasa.gov/data/SNPP_OMPS_Level2/OMPS_NPP_NPBUVO3_L2.2.9/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://omps.gesdisc.eosdis.nasa.gov/data/SNPP_OMPS_Level2/OMPS_NPP_NPBUVO3_L2.2.9/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://omps.gesdisc.eosdis.nasa.gov/opendap/SNPP_OMPS_Level2/OMPS_NPP_NPBUVO3_L2.2.9/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://omps.gesdisc.eosdis.nasa.gov/opendap/SNPP_OMPS_Level2/OMPS_NPP_NPBUVO3_L2.2.9/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=OMPS_NPP_NPBUVO3_L2_2.9",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=OMPS_NPP_NPBUVO3_L2_2.9",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://omps.gesdisc.eosdis.nasa.gov/data/SNPP_OMPS_Level2/OMPS_NPP_NPBUVO3_L2.2.9/doc/README.OMPS_NPP_NPBUVO3_L2_v2.9.pdf",
-                    "description": "README Document",
                     "@type": "dcat:Distribution",
+                    "description": "README Document",
+                    "downloadURL": "https://omps.gesdisc.eosdis.nasa.gov/data/SNPP_OMPS_Level2/OMPS_NPP_NPBUVO3_L2.2.9/doc/README.OMPS_NPP_NPBUVO3_L2_v2.9.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's read me document"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.nesdis.noaa.gov/our-satellites/currently-flying/joint-polar-satellite-system",
-                    "description": "Joint Polar Satellite System (JPSS) mission home page",
                     "@type": "dcat:Distribution",
+                    "description": "Joint Polar Satellite System (JPSS) mission home page",
+                    "downloadURL": "https://www.nesdis.noaa.gov/our-satellites/currently-flying/joint-polar-satellite-system",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 }
             ],
+            "graphic-preview-description": "OMPS Logo",
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/OMPS_NPP_NPBUVO3_L2_2.9.jpeg",
+            "identifier": "C2821060582-GES_DISC",
+            "issued": "2023-11-14",
+            "keyword": [
+                "atmosphere",
+                "atmospheric chemistry",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/FXX5S2VP2FVI",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2023-11-14",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
+            },
+            "references": [
+                "https://doi.org/10.5194/amt-6-2533-2013"
+            ],
+            "release-place": "Greenbelt, MD, USA",
+            "series-name": "OMPS_NPP_NPBUVO3_L2",
             "spatial": "-180.0 -82.0 180.0 82.0",
+            "temporal": "2011-11-13T00:00:00Z/2024-07-15T00:00:00Z",
             "theme": [
                 "NPP-JPSS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "OMPS-NPP L2 NP Ozone (O3) Vertical Profile swath orbital V2.9 (OMPS_NPP_NPBUVO3_L2) at GES DISC"
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
-                "index",
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
-            "identifier": "NASA-565",
             "description": "Data Dictionary and Index Files",
-            "title": "PDS Data Dictionary (1r80)",
-            "programCode": [
-                "026:005"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -1325824,273 +1325803,296 @@
                     "mediaType": "application/html"
                 }
             ],
-            "accrualPeriodicity": "irregular",
+            "identifier": "NASA-565",
+            "issued": "2018-06-25",
+            "keyword": [
+                "dictionary",
+                "pds",
+                "index",
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
+            "title": "PDS Data Dictionary (1r80)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/S6AP4-1AHST",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Ocean Surface Topography Science Team. 2021-06-22. Sentinel-6A MF Jason-CS L1A P4 Altimeter High Resolution (HR) STC Intermediate Outputs with Instrument Calibrations. Version F. PO.DAAC. Archived by National Aeronautics and Space Administration, U.S. Government, PO.DAAC. https://doi.org/10.5067/S6AP4-1AHST.",
-            "issued": "2020-12-07",
-            "temporal": "2020-12-07T01:15:01.314Z/2023-04-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-04-13",
-            "references": [
-                "https://doi.org/10.1016/j.rse.2021.112395"
-            ],
-            "keyword": [
-                "oceans",
-                "sea surface topography",
-                "earth science",
-                "ocean waves"
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
-            "identifier": "C1968979558-POCLOUD",
-            "description": "Provides L1A high resolution (HR) short time critical (STC; 36-hour latency) altimetry intermediate outputs from the Poseidon-4 SAR altimeter on the Sentinel-6A Michael Freilich spacecraft, which are geo-located bursts of Ku-band echoes (at ~140 Hz) with all instrument calibrations applied and full rate complex waveforms for delay/Doppler or HR processing. The S6A STC product is analogous to the Jason-3 IGDR product.",
-            "release-place": "PO.DAAC",
-            "graphic-preview-description": "Thumbnail image for Website",
             "creator": "Ocean Surface Topography Science Team",
-            "title": "Sentinel-6A MF Jason-CS L1A P4 Altimeter High Resolution (HR) STC Intermediate Outputs with Instrument Calibrations",
-            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/JASON_CS_S6A_L1A_ALT_HR_STC_F.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "Provides L1A high resolution (HR) short time critical (STC; 36-hour latency) altimetry intermediate outputs from the Poseidon-4 SAR altimeter on the Sentinel-6A Michael Freilich spacecraft, which are geo-located bursts of Ku-band echoes (at ~140 Hz) with all instrument calibrations applied and full rate complex waveforms for delay/Doppler or HR processing. The S6A STC product is analogous to the Jason-3 IGDR product.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FS6AP4-1AHST",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FS6AP4-1AHST",
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
-                    "downloadURL": "https://podaac.jpl.nasa.gov/dataset/JASON_CS_S6A_L1A_ALT_HR_STC_F",
-                    "description": "Data Set Landing Page",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Landing Page",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/dataset/JASON_CS_S6A_L1A_ALT_HR_STC_F",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/JASON_CS_S6A_L1A_ALT_HR_STC_F.jpg",
-                    "description": "Thumbnail image for Website",
                     "@type": "dcat:Distribution",
+                    "description": "Thumbnail image for Website",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/JASON_CS_S6A_L1A_ALT_HR_STC_F.jpg",
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
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C1968979558-POCLOUD",
-                    "description": "HTTPS endpoint for data browse and download",
                     "@type": "dcat:Distribution",
+                    "description": "HTTPS endpoint for data browse and download",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C1968979558-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1968979558-POCLOUD",
-                    "description": "Browse granule search results in Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse granule search results in Earthdata Search",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1968979558-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 }
             ],
+            "graphic-preview-description": "Thumbnail image for Website",
+            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/JASON_CS_S6A_L1A_ALT_HR_STC_F.jpg",
+            "identifier": "C1968979558-POCLOUD",
+            "issued": "2020-12-07",
+            "keyword": [
+                "oceans",
+                "sea surface topography",
+                "earth science",
+                "ocean waves"
+            ],
+            "landingPage": "https://doi.org/10.5067/S6AP4-1AHST",
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
+            "temporal": "2020-12-07T01:15:01.314Z/2023-04-17T00:00:00Z",
             "theme": [
                 "Sentinel-6",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Sentinel-6A MF Jason-CS L1A P4 Altimeter High Resolution (HR) STC Intermediate Outputs with Instrument Calibrations"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-E-RPCICA-2-EAR1-RAW-V2.0",
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
-                "earth",
-                "international rosetta mission"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This dataset contains RAW DATA from the RPCICA instrument on mission\nROSETTA during Earth the first Earth swingby. Due to an overheating event\nRPC-ICA only obtained data from the deep tail at about 200 RE tailward\ndistance. Protons at about 10 KeV energy were observed throughout the\nobservation period. Magnetosheath like populations of protons and alpha particles were observed during most of the observation period.\nData set version 2 replaces a previously delivered data set.\nImportant changes are the ordering of the energy levels which now\ngo from low to high and that the quality flag in the labels is\nupdated.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-e-rpcica-2-ear1-raw-v2.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "earth",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-E-RPCICA-2-EAR1-RAW-V2.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-e-rpcica-2-ear1-raw-v2.0",
-            "description": "This dataset contains RAW DATA from the RPCICA instrument on mission\nROSETTA during Earth the first Earth swingby. Due to an overheating event\nRPC-ICA only obtained data from the deep tail at about 200 RE tailward\ndistance. Protons at about 10 KeV energy were observed throughout the\nobservation period. Magnetosheath like populations of protons and alpha particles were observed during most of the observation period.\nData set version 2 replaces a previously delivered data set.\nImportant changes are the ordering of the energy levels which now\ngo from low to high and that the quality flag in the labels is\nupdated.",
-            "title": "ROSETTA-ORBITER EARTH RPCICA 2 EAR1 UNCALIBRATED V2.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER EARTH RPCICA 2 EAR1 UNCALIBRATED V2.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/SeaBASS/HYCODE_LEO-15/DATA001",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/GSFC/SED/ESD/GCDC/OB.DAAC. https://doi.org/10.5067/SeaBASS/HYCODE_LEO-15/DATA001.",
-            "issued": "2000-07-20",
-            "temporal": "2000-07-20T00:00:00Z/2023-04-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-04-06",
-            "keyword": [
-                "ocean chemistry",
-                "ocean temperature",
-                "earth science",
-                "ocean optics",
-                "salinity/density",
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
-            "identifier": "C1633360372-OB_DAAC",
             "description": "Measurements from the Hyperspectral Coastal Ocean Dynamics Experiment (HyCoDE) LEO-15 station off the Atlantic Coast of New Jersey.",
-            "title": "Hyperspectral Coastal Ocean Dynamics Experiment (HyCoDE) measurements at Long-term Ecosystem Observatory 15 (LEO-15) oceanographic and meteorological station",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSeaBASS%2FHYCODE_LEO-15%2FDATA001",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSeaBASS%2FHYCODE_LEO-15%2FDATA001",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://seabass.gsfc.nasa.gov/experiment/HYCODE_LEO-15/",
-                    "description": "Detailed information about the SeaBASS Experiment such as cruises, funding, and investigators",
                     "@type": "dcat:Distribution",
+                    "description": "Detailed information about the SeaBASS Experiment such as cruises, funding, and investigators",
+                    "downloadURL": "https://seabass.gsfc.nasa.gov/experiment/HYCODE_LEO-15/",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 }
             ],
+            "identifier": "C1633360372-OB_DAAC",
+            "issued": "2000-07-20",
+            "keyword": [
+                "ocean chemistry",
+                "ocean temperature",
+                "earth science",
+                "ocean optics",
+                "salinity/density",
+                "oceans"
+            ],
+            "landingPage": "https://doi.org/10.5067/SeaBASS/HYCODE_LEO-15/DATA001",
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
+            "temporal": "2000-07-20T00:00:00Z/2023-04-17T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Hyperspectral Coastal Ocean Dynamics Experiment (HyCoDE) measurements at Long-term Ecosystem Observatory 15 (LEO-15) oceanographic and meteorological station"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=SOHO-C-LASCO-5-KREUTZPHOTOM-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This data set contains aperture photometry of Kreutz sungrazing comets that were observed by the LASCO instrument on SOHO from 1996-2005. Apparent magnitude and the error in the magnitude due to photon statistics are given for circular apertures ranging from 1,2,3...10 pixels in radius. All images were taken either with the C2 telescope (11.9 arcsec/pixel) or the C3 telescope (56 arcsec/pixel). The reduced subimages from which this photometry was calculated are archived with PDS (Knight 2008) [KNIGHT2008] and scientific analysis is in (Knight et al. 2010) [KNIGHTETAL2010].",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.soho-c-lasco-5-kreutzphotom-v1.0_rupp-5mgy",
             "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "c/soho (2002 w17)",
                 "solar and heliospheric observatory",
@@ -1327007,773 +1327009,749 @@
                 "c/soho (2002 w15)",
                 "c/soho (2002 w16)"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=SOHO-C-LASCO-5-KREUTZPHOTOM-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.soho-c-lasco-5-kreutzphotom-v1.0_rupp-5mgy",
-            "description": "This data set contains aperture photometry of Kreutz sungrazing comets that were observed by the LASCO instrument on SOHO from 1996-2005. Apparent magnitude and the error in the magnitude due to photon statistics are given for circular apertures ranging from 1,2,3...10 pixels in radius. All images were taken either with the C2 telescope (11.9 arcsec/pixel) or the C3 telescope (56 arcsec/pixel). The reduced subimages from which this photometry was calculated are archived with PDS (Knight 2008) [KNIGHT2008] and scientific analysis is in (Knight et al. 2010) [KNIGHTETAL2010].",
-            "title": "SOHO LASCO COMET PHOTOMETRY V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "SOHO LASCO COMET PHOTOMETRY V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ASDC/SUBORBITAL/STAQS/DATA001/Ground_1",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2024-08-09. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/ASDC/SUBORBITAL/STAQS/DATA001/Ground_1.",
-            "issued": "2023-07-01",
-            "temporal": "2023-07-01T00:00:00Z/2023-08-31T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-08-31",
-            "keyword": [
-                "atmospheric winds",
-                "atmospheric temperature",
-                "atmosphere",
-                "atmospheric pressure",
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
-            "identifier": "C3094428881-LARC_CLOUD",
             "description": "STAQS_Ground_Data is the ground site data collected during the Synergistic TEMPO Air Quality Science (STAQS) mission. Data collection for this product is complete.\r\n\r\nLaunched in April 2023, NASA\u2019s Tropospheric Emissions: Monitoring of Pollution (TEMPO) satellite monitors major air pollutants across North America every daylight hour at high spatial resolution at a geostationary orbit (GEO). With these measurements, NASA\u2019s STAQS mission seeks to integrate TEMPO satellite observations with traditional air quality monitoring to improve understanding of air quality science and enhance societal benefit. STAQS is being conducted during summer 2023, targeting urban areas, including Los Angeles, New York City, and Chicago. As part of the mission two aircraft will be outfitted with various remote sensing payloads. The Johnson Space Center (JSC) Gulfstream-V (G-V) aircraft will feature the GeoCAPE Airborne Simulator (GCAS) and combined High Spectral Resolution Lidar-2 (HSRL-2) and Ozone Differential Absorption Lidar (DIAL). This payload provides repeated high-resolution mapping of NO2, HCHO, ozone, and aerosols up to 3x per day over targeted cities. NASA Langley Research Center\u2019s (LaRC\u2019s) Gulfstream-III will measure city-scale emissions 2x per day over the targeted cities with the High-Altitude Lidar Observatory (HALO) and Airborne Visible InfraRed Imaging Spectrometer \u2013 Next Generation (AVIRS-NG). STAQS will also incorporate ground-based tropospheric ozone profiles from the NASA Tropospheric Ozone Lidar Network (TOLNet), NO2, HCHO, and ozone measurements from Pandora spectrometers, and will leverage existing networks operated by the EPA and state air quality agencies. The primary goal of STAQS is to improve our current understanding of air quality science under the TEMPO field of regard. Further goals include evaluating TEMPO level 2 data products, interpreting the temporal and spatial evolution of air quality events tracked by TEMPO, improving temporal estimates of anthropogenic, biogenic, and greenhouse gas emissions, assessing the benefit of assimilating TEMPO data into chemical transport models, and linking air quality patterns to socio-demographic data.",
-            "title": "STAQS Ground Data",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC%2FSUBORBITAL%2FSTAQS%2FDATA001%2FGround_1",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC%2FSUBORBITAL%2FSTAQS%2FDATA001%2FGround_1",
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
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C3094428881-LARC_CLOUD",
-                    "description": "Earthdata Search for STAQS_Ground_Data_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for STAQS_Ground_Data_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C3094428881-LARC_CLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/ASDC/SUBORBITAL/STAQS/DATA001/Ground_1",
-                    "description": "DOI data set landing page for STAQS_Ground_Data_1",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for STAQS_Ground_Data_1",
+                    "downloadURL": "https://doi.org/10.5067/ASDC/SUBORBITAL/STAQS/DATA001/Ground_1",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 }
             ],
+            "identifier": "C3094428881-LARC_CLOUD",
+            "issued": "2023-07-01",
+            "keyword": [
+                "atmospheric winds",
+                "atmospheric temperature",
+                "atmosphere",
+                "atmospheric pressure",
+                "atmospheric chemistry",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/ASDC/SUBORBITAL/STAQS/DATA001/Ground_1",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2023-08-31",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/LARC/SD/ASDC"
+            },
             "spatial": "-87.83 42.58 -87.808 42.59",
+            "temporal": "2023-07-01T00:00:00Z/2023-08-31T23:59:59Z",
             "theme": [
                 "STAQS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "STAQS Ground Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-A-OSINAC-3-AST1-STEINSFLYBY-V1.4",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This data set contains images acquired by the OSIRIS Narrow Angle Camera during the STEINS_FLY-BY mission phase",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-a-osinac-3-ast1-steinsflyby-v1.4_ruvf-embm",
             "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "2867 steins",
                 "international rosetta mission",
                 "16 cyg b",
                 "vega"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-A-OSINAC-3-AST1-STEINSFLYBY-V1.4",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-a-osinac-3-ast1-steinsflyby-v1.4_ruvf-embm",
-            "description": "This data set contains images acquired by the OSIRIS Narrow Angle Camera during the STEINS_FLY-BY mission phase",
-            "title": "ROSETTA-ORBITER STEINS_FLY-BY OSINAC 3 RDR V1.4",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "ROSETTA-ORBITER STEINS_FLY-BY OSINAC 3 RDR V1.4"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/GNSS/GLONASS_DAILY_M_001",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "International GNSS Service, Daily 30-second GLONASS meteorological data, Greenbelt, MD, USA:NASA Crustal Dynamics Data Information System (CDDIS), Accessed [[enter user data access date]] at doi:10.5067/GNSS/glonass_daily_m_001",
-            "issued": "1998-01-01",
-            "temporal": "1998-01-01T00:00:00Z/2025-01-20T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-17",
-            "keyword": [
-                "gravity/gravitational field",
-                "earth science",
-                "solid earth",
-                "tectonics",
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
-            "identifier": "C1423569055-CDDIS",
             "description": "This dataset consists of ground-based Meteorological Data (daily, 24 hour files) from instruments co-located with Global Navigation Satellite System (GNSS) GLONASS receivers from the NASA Crustal Dynamics Data Information System (CDDIS). GNSS provide autonomous geo-spatial positioning with global coverage. The GLONASS data sets from ground receivers at the CDDIS consist of observations from the Russian GLObal NAvigation Satellite System (GLONASS); Russia's GLONASS is similar to the U.S. GPS in terms of the satellite constellation, orbits, and signal structure. The daily meteorological data files contain one day of meteorological data (temperature, pressure, humidity, etc.) in RINEX format from a global permanent network of ground-based receivers, one file per site. More information about these data is available on the CDDIS website at https://cddis.nasa.gov/Data_and_Derived_Products/GNSS/daily_30second_data.html.",
-            "title": "Ground-Based Meteorological Data (daily, 24 hour files) from Co-Located Ground-Based Global Navigation Satellite System GLONASS (GLObal NAvigation Satellite System) Receivers from NASA CDDIS",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGNSS%2FGLONASS_DAILY_M_001",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGNSS%2FGLONASS_DAILY_M_001",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://cddis.nasa.gov/archive/glonass/data/daily",
-                    "description": "URL for retrieval of GLONASS daily meteorological data through https",
                     "@type": "dcat:Distribution",
+                    "description": "URL for retrieval of GLONASS daily meteorological data through https",
+                    "downloadURL": "https://cddis.nasa.gov/archive/glonass/data/daily",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://cddis.nasa.gov/Data_and_Derived_Products/GNSS/daily_30second_data.html",
-                    "description": "URL for more information about GLONASS daily meteorological data",
                     "@type": "dcat:Distribution",
+                    "description": "URL for more information about GLONASS daily meteorological data",
+                    "downloadURL": "https://cddis.nasa.gov/Data_and_Derived_Products/GNSS/daily_30second_data.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/GNSS/GLONASS_DAILY_M_001",
-                    "description": "URL for more information about GLONASS daily meteorological data",
                     "@type": "dcat:Distribution",
+                    "description": "URL for more information about GLONASS daily meteorological data",
+                    "downloadURL": "https://doi.org/10.5067/GNSS/GLONASS_DAILY_M_001",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 }
             ],
+            "identifier": "C1423569055-CDDIS",
+            "issued": "1998-01-01",
+            "keyword": [
+                "gravity/gravitational field",
+                "earth science",
+                "solid earth",
+                "tectonics",
+                "geodetics"
+            ],
+            "landingPage": "https://doi.org/10.5067/GNSS/GLONASS_DAILY_M_001",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2025-01-17",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "CDDIS"
+            },
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "1998-01-01T00:00:00Z/2025-01-20T00:00:00Z",
             "theme": [
                 "IGS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Ground-Based Meteorological Data (daily, 24 hour files) from Co-Located Ground-Based Global Navigation Satellite System GLONASS (GLObal NAvigation Satellite System) Receivers from NASA CDDIS"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.7927/10.7927/f8eh-5864",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Di, Q., Y. Wei, A. Shtein, C. Hultquist, X. Xing, H. Amini, L. Shi, I. Kloog, R. Silvern, J. T. Kelly, M. B. Sabath, C. Choirat, P. Koutrakis, A. Lyapustin, Y. Wang, L. J. Mickley, and J. Schwartz. 2022-06-21. Daily and Annual NO2 Concentrations for the Contiguous United States, 1-km Grids, v1 (2000 - 2016). Version 1.00. Palisades, NY. Archived by National Aeronautics and Space Administration, U.S. Government, NASA Socioeconomic Data and Applications Center (SEDAC). https://doi.org/10.7927/10.7927/f8eh-5864. https://doi.org/10.7927/f8eh-5864.",
-            "issued": "2022-06-21",
-            "temporal": "2000-01-01T00:00:00Z/2016-12-31T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-06-21",
-            "keyword": [
-                "atmospheric chemistry",
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
-            "identifier": "C2302636732-SEDAC",
-            "description": "The Daily and Annual NO2 Concentrations for the Contiguous United States, 1-km Grids, v1 (2000-2016) data set contains daily predictions of Nitrogen Dioxide (NO2) concentrations at a high resolution (1 km x 1 km grid cells) for the years 2000 to 2016. An ensemble modeling framework was used to assess NO2 levels with high accuracy, which combined estimates from three machine learning models (neural network, random forest, and gradient boosting), with a generalized additive model. Predictor variables included NO2 column concentrations from satellites, land-use variables, meteorological variables, predictions from two chemical transport models, GEOS-Chem and the U.S. Environmental Protection Agency (EPA) CommUnity Multiscale Air Quality Modeling System (CMAQ), along with other ancillary variables. The annual predictions were calculated by averaging the daily predictions for each year in each grid cell. The ensemble produced a cross-validated R-squared value of 0.79 overall, a spatial R-squared value of 0.84, and a temporal R-squared value of 0.73.",
-            "release-place": "Palisades, NY",
-            "graphic-preview-description": "Sample browse graphic of the data set.",
             "creator": "Di, Q., Y. Wei, A. Shtein, C. Hultquist, X. Xing, H. Amini, L. Shi, I. Kloog, R. Silvern, J. T. Kelly, M. B. Sabath, C. Choirat, P. Koutrakis, A. Lyapustin, Y. Wang, L. J. Mickley, and J. Schwartz",
-            "title": "Daily and Annual NO2 Concentrations for the Contiguous United States, 1-km Grids, v1 (2000 - 2016)",
-            "graphic-preview-file": "https://sedac.ciesin.columbia.edu/downloads/maps/aqdh/aqdh-no2-concentrations-contiguous-us-1-km-2000-2016/sedac-logo.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The Daily and Annual NO2 Concentrations for the Contiguous United States, 1-km Grids, v1 (2000-2016) data set contains daily predictions of Nitrogen Dioxide (NO2) concentrations at a high resolution (1 km x 1 km grid cells) for the years 2000 to 2016. An ensemble modeling framework was used to assess NO2 levels with high accuracy, which combined estimates from three machine learning models (neural network, random forest, and gradient boosting), with a generalized additive model. Predictor variables included NO2 column concentrations from satellites, land-use variables, meteorological variables, predictions from two chemical transport models, GEOS-Chem and the U.S. Environmental Protection Agency (EPA) CommUnity Multiscale Air Quality Modeling System (CMAQ), along with other ancillary variables. The annual predictions were calculated by averaging the daily predictions for each year in each grid cell. The ensemble produced a cross-validated R-squared value of 0.79 overall, a spatial R-squared value of 0.84, and a temporal R-squared value of 0.73.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.7927%2F10.7927%2Ff8eh-5864",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.7927%2F10.7927%2Ff8eh-5864",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/downloads/maps/aqdh/aqdh-no2-concentrations-contiguous-us-1-km-2000-2016/sedac-logo.jpg",
-                    "description": "Sample browse graphic of the data set.",
                     "@type": "dcat:Distribution",
+                    "description": "Sample browse graphic of the data set.",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/downloads/maps/aqdh/aqdh-no2-concentrations-contiguous-us-1-km-2000-2016/sedac-logo.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/aqdh-no2-concentrations-contiguous-us-1-km-2000-2016/data-download",
-                    "description": "Data Download Page",
                     "@type": "dcat:Distribution",
+                    "description": "Data Download Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/aqdh-no2-concentrations-contiguous-us-1-km-2000-2016/data-download",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/aqdh-no2-concentrations-contiguous-us-1-km-2000-2016/docs",
-                    "description": "Documentation Page",
                     "@type": "dcat:Distribution",
+                    "description": "Documentation Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/aqdh-no2-concentrations-contiguous-us-1-km-2000-2016/docs",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/aqdh-no2-concentrations-contiguous-us-1-km-2000-2016",
-                    "description": "Data Set\u00a0Overview Page",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set\u00a0Overview Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/aqdh-no2-concentrations-contiguous-us-1-km-2000-2016",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "graphic-preview-description": "Sample browse graphic of the data set.",
+            "graphic-preview-file": "https://sedac.ciesin.columbia.edu/downloads/maps/aqdh/aqdh-no2-concentrations-contiguous-us-1-km-2000-2016/sedac-logo.jpg",
+            "identifier": "C2302636732-SEDAC",
+            "issued": "2022-06-21",
+            "keyword": [
+                "atmospheric chemistry",
+                "earth science",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.7927/10.7927/f8eh-5864",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2022-06-21",
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
+            "title": "Daily and Annual NO2 Concentrations for the Contiguous United States, 1-km Grids, v1 (2000 - 2016)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/IIR/CALIPSO/CAL_IIR_L2_Swath-Standard-V4-21",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2019-05-29. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/IIR/CALIPSO/CAL_IIR_L2_Swath-Standard-V4-21.",
-            "issued": "2019-05-08",
-            "temporal": "2020-07-01T00:00:00Z/2022-01-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2019-05-08",
-            "keyword": [
-                "clouds",
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
-            "identifier": "C1969999387-LARC_ASDC",
             "description": "CAL_IIR_L2_Swath-Standard-V4-20 is the Cloud-Aerosol Lidar and Infrared Pathfinder Satellite Observations (CALIPSO) Infrared Imaging Radiometer (IIR) Level 2 Swath, Version 4-21 data product. Data for this product was collected using the CALIPSO IIR instrument. Data collection for this product is ongoing. This product contains emissivity and cloud particle data assigned to IIR pixels on a 1 km grid centered on the lidar track. The version of this product was changed from 4-20 to 4-21 to account for a change in the operating system of the CALIPSO production cluster.\r\n\r\nCALIPSO was launched on April 28, 2006 to study the impact of clouds and aerosols on the Earth's radiation budget and climate. It flies in the international A-Train constellation for coincident Earth observations. The CALIPSO satellite comprises three instruments, Cloud-Aerosol LIdar with Orthogonal Polarization (CALIOP), IIR, and Wide Field Camera (WFC). CALIPSO is a joint satellite mission between NASA and the French Agency, CNES.",
-            "title": "CALIPSO Infrared Imaging Radiometer (IIR) Level 2 Swath, V4-21",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FIIR%2FCALIPSO%2FCAL_IIR_L2_Swath-Standard-V4-21",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FIIR%2FCALIPSO%2FCAL_IIR_L2_Swath-Standard-V4-21",
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
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://www-calipso.larc.nasa.gov/products/CALIPSO_DPC_Rev4x92.pdf",
-                    "description": "CALIPSO - Data Management System - Data Products Catalog - Release 2.4",
                     "@type": "dcat:Distribution",
+                    "description": "CALIPSO - Data Management System - Data Products Catalog - Release 2.4",
+                    "downloadURL": "https://www-calipso.larc.nasa.gov/products/CALIPSO_DPC_Rev4x92.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's production history"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www-calipso.larc.nasa.gov/resources/calipso_users_guide/qs/cal_iir_l2_trackswath_v4-20.php",
-                    "description": "Detailed quality summary of the V4.20 IIR Level 2 data product",
                     "@type": "dcat:Distribution",
+                    "description": "Detailed quality summary of the V4.20 IIR Level 2 data product",
+                    "downloadURL": "https://www-calipso.larc.nasa.gov/resources/calipso_users_guide/qs/cal_iir_l2_trackswath_v4-20.php",
+                    "mediaType": "text/html",
                     "title": "View this dataset's data quality document"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www-calipso.larc.nasa.gov/resources/calipso_users_guide/data_summaries/iir/cal_iir_l2_swath_v4-20_desc.php",
-                    "description": "User's guide description document of the V4.20 IIR Level 2 Swath data product",
                     "@type": "dcat:Distribution",
+                    "description": "User's guide description document of the V4.20 IIR Level 2 Swath data product",
+                    "downloadURL": "https://www-calipso.larc.nasa.gov/resources/calipso_users_guide/data_summaries/iir/cal_iir_l2_swath_v4-20_desc.php",
+                    "mediaType": "text/html",
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
                     "title": "View this dataset's data citation policy"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www-calipso.larc.nasa.gov/resources/publications.php",
-                    "description": "CALIPSO - List of publications",
                     "@type": "dcat:Distribution",
+                    "description": "CALIPSO - List of publications",
+                    "downloadURL": "https://www-calipso.larc.nasa.gov/resources/publications.php",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
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
-                    "description": "CALIPSO Tilt Mode Geometry Anomaly",
                     "@type": "dcat:Distribution",
+                    "description": "CALIPSO Tilt Mode Geometry Anomaly",
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
-                    "downloadURL": "https://doi.org/10.5067/IIR/CALIPSO/CAL_IIR_L2_Swath-Standard-V4-21",
-                    "description": "DOI data set landing page for CAL_IIR_L2_Swath-Standard-V4-21_V4-21",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for CAL_IIR_L2_Swath-Standard-V4-21_V4-21",
+                    "downloadURL": "https://doi.org/10.5067/IIR/CALIPSO/CAL_IIR_L2_Swath-Standard-V4-21",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1969999387-LARC_ASDC",
-                    "description": "Earthdata Search for CAL_IIR_L2_Swath-Standard-V4-21_V4-21 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for CAL_IIR_L2_Swath-Standard-V4-21_V4-21 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1969999387-LARC_ASDC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
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
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/CALIPSO/IIR_L2_Swath-Standard-V4-21/",
-                    "description": "ASDC Direct Data Download for CAL_IIR_L2_Swath-Standard-V4-21_V4-21",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for CAL_IIR_L2_Swath-Standard-V4-21_V4-21",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/CALIPSO/IIR_L2_Swath-Standard-V4-21/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/CALIPSO/IIR_L2_Swath-Standard-V4-21/contents.html",
-                    "description": "OPeNDAP data access for CAL_IIR_L2_Swath-Standard-V4-21_V4-21",
                     "@type": "dcat:Distribution",
+                    "description": "OPeNDAP data access for CAL_IIR_L2_Swath-Standard-V4-21_V4-21",
+                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/CALIPSO/IIR_L2_Swath-Standard-V4-21/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 }
             ],
+            "identifier": "C1969999387-LARC_ASDC",
+            "issued": "2019-05-08",
+            "keyword": [
+                "clouds",
+                "atmosphere",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/IIR/CALIPSO/CAL_IIR_L2_Swath-Standard-V4-21",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2019-05-08",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/LARC/SD/ASDC"
+            },
             "spatial": "<?xml version=\"1.0\" encoding=\"UTF-8\"?><gml:Polygon xmlns:gml=\"http://www.opengis.net/gml/3.2\" srsName=\"EPSG:9825\"><gml:outerBoundaryIs><gml:LinearRing><gml:posList>-90.0 -180.0 -90.0 180.0 90.0 180.0 90.0 -180.0 -90.0 -180.0</gml:posList></gml:LinearRing></gml:outerBoundaryIs><gml:innerBoundaryIs></gml:innerBoundaryIs></gml:Polygon>",
+            "temporal": "2020-07-01T00:00:00Z/2022-01-17T00:00:00Z",
             "theme": [
                 "CALIPSO",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "CALIPSO Infrared Imaging Radiometer (IIR) Level 2 Swath, V4-21"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-3-ESC4-67PCHURYUMOV-M23-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This data set contains images acquired by the OSIRIS Wide Angle Camera during the COMET ESCORT 4 phase of the Rosetta mission at the comet 67P, covering the period from 2015-11-17T23:25:00.000 to 2015-12-15T23:24:59.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-3-esc4-67pchuryumov-m23-v1.0",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2021-05-21",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "international rosetta mission",
                 "67p/churyumov-gerasimenko 1 (1969 r1)",
                 "zeta cas",
                 "vega"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-3-ESC4-67PCHURYUMOV-M23-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-3-esc4-67pchuryumov-m23-v1.0",
-            "description": "This data set contains images acquired by the OSIRIS Wide Angle Camera during the COMET ESCORT 4 phase of the Rosetta mission at the comet 67P, covering the period from 2015-11-17T23:25:00.000 to 2015-12-15T23:24:59.000.",
-            "title": "ROSETTA-ORBITER COMET ESCORT 4 OSIWAC 3 RDR MTP023 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER COMET ESCORT 4 OSIWAC 3 RDR MTP023 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG1-S-PLS-5-SUMM-IONFIT-96SEC-V1.0",
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
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg1-s-pls-5-summ-ionfit-96sec-v1.0_rv3i-uk87",
+            "issued": "2018-06-26",
+            "keyword": [
+                "voyager",
+                "saturn"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG1-S-PLS-5-SUMM-IONFIT-96SEC-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg1-s-pls-5-summ-ionfit-96sec-v1.0_rv3i-uk87",
-            "description": "not applicable",
-            "title": "VOYAGER 1 SATURN PLASMA DERIVED ION FITS 96 SEC V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "VOYAGER 1 SATURN PLASMA DERIVED ION FITS 96 SEC V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1641945804-OB_DAAC.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, OB.DAAC.",
-            "issued": "2019-06-23",
-            "temporal": "2002-07-04T00:00:00Z/2022-01-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2019-10-01",
-            "keyword": [
-                "oceans",
-                "national geospatial data asset",
-                "earth science",
-                "ngda",
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
-            "identifier": "C1641945804-OB_DAAC",
             "description": "The Ocean Biology DAAC produces near real-time (quicklook) products using the best-available combination of ancillary data from meteorological and ozone data. As such, the inputs and the calibration used are less than optimal. Quicklook products provide a snapshot of the data during a short time period within a single orbit.",
-            "title": "Aqua MODIS Global Binned 11\u00b5m Day/Night Sea Surface Temperature (SST) - Near Real Time (NRT) Data, version R2019.0",
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
-                    "description": "MODIS-Aqua L3B 11\u00b5m Day/Night Sea Surface Temperature (SST) - Near Real Time (NRT) Dataset Landing Page",
                     "@type": "dcat:Distribution",
+                    "description": "MODIS-Aqua L3B 11\u00b5m Day/Night Sea Surface Temperature (SST) - Near Real Time (NRT) Dataset Landing Page",
+                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/data/10.5067/AQUA/MODIS/L3B/SST/R2019.0",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 }
             ],
+            "identifier": "C1641945804-OB_DAAC",
+            "issued": "2019-06-23",
+            "keyword": [
+                "oceans",
+                "national geospatial data asset",
+                "earth science",
+                "ngda",
+                "ocean temperature"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1641945804-OB_DAAC.html",
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
+            "title": "Aqua MODIS Global Binned 11\u00b5m Day/Night Sea Surface Temperature (SST) - Near Real Time (NRT) Data, version R2019.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=PVO-V-ONMS-4-THERMALION-12SEC-V1.0",
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
+            "description": "Thermal ions can be measured with the filament off and the ion repeller set at 0 V. Species observed include He+, N+, O+, CO+ and/or N2+, NO+, O2+ and CO2+. H+ is not measurable with the current instrument configuration. One component of the ion drift in the ecliptic plane can also be determined. Thermal ion measurements have been taken sporadically at the end of neutral density passes and on alternate orbits when superthermal ions are not being measured.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.pvo-v-onms-4-thermalion-12sec-v1.0_rv87-n8e5",
+            "issued": "2021-05-21",
+            "keyword": [
+                "venus",
+                "pioneer venus"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=PVO-V-ONMS-4-THERMALION-12SEC-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.pvo-v-onms-4-thermalion-12sec-v1.0_rv87-n8e5",
-            "description": "Thermal ions can be measured with the filament off and the ion repeller set at 0 V. Species observed include He+, N+, O+, CO+ and/or N2+, NO+, O2+ and CO2+. H+ is not measurable with the current instrument configuration. One component of the ion drift in the ecliptic plane can also be determined. Thermal ion measurements have been taken sporadically at the end of neutral density passes and on alternate orbits when superthermal ions are not being measured.",
-            "title": "PVO VENUS ONMS BROWSE THERMAL ION 12 SECOND V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "PVO VENUS ONMS BROWSE THERMAL ION 12 SECOND V1.0"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "http://turbmodels.larc.nasa.gov/bradshaw.html",
-            "bureauCode": [
-                "026:00"
-            ],
-            "issued": "2018-06-25",
             "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
-            "references": [
-                "http://turbmodels.larc.nasa.gov/index.html"
-            ],
-            "keyword": [
-                "turbulence",
-                "cases",
-                "models",
-                "incompressible",
-                "flow"
+            "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "026:00"
             ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Christopher Rumsey",
                 "hasEmail": "mailto:c.l.rumsey@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Aeronautics and Space Administration"
-            },
-            "identifier": "NASA-842__11",
             "description": "This grouping contains the incompressible-flow cases from the 1980-81 Data Library.",
-            "title": "Collaborative Testing of Turbulence Models: Incompressible Flow Cases from 1980-81 Data Library",
-            "programCode": [
-                "026:023"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -1327781,464 +1327759,488 @@
                     "mediaType": "application/txt"
                 }
             ],
-            "accrualPeriodicity": "irregular",
+            "identifier": "NASA-842__11",
+            "issued": "2018-06-25",
+            "keyword": [
+                "turbulence",
+                "cases",
+                "models",
+                "incompressible",
+                "flow"
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
-            "landingPage": "https://doi.org/10.5067/GOES13/CERES/GEO_ED4_SH_V01.2",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2018-07-19. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/GOES13/CERES/GEO_ED4_SH_V01.2.",
-            "issued": "2018-05-22",
-            "temporal": "2015-07-01T00:00:00Z/2022-01-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2018-07-19",
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
-            "identifier": "C1587405101-LARC_ASDC",
             "description": "CER_GEO_Ed4_GOE13_SH_V01.2 is the Satellite ClOud and Radiation Property retrieval System (SatCORPS) Clouds and the Earth's Radiant Energy System (CERES) Geostationary Satellite (GEO) Edition 4 Geostationary Operational Environmental Satellite 13 (GOES-13) over the Southern Hemisphere (SH) Version 1.2 data product. Data was collected using the GOES-13 Imager on the GOES-13 Platform. Data collection for this product is in progress.\r\n\r\nNote : Version 1.2 is identical to version 1.0. No changes in retrieval algorithm.\r\n\r\nThis data set is comprised of cloud micro-physical and radiation properties derived hourly from GOES-13 geostationary satellite imager data using the Langley Research Center (LARC) SATCORPS algorithms in support of the CERES project. The cloud micro-physical and radiation properties from each active geostationary satellite are merged together to create hourly global cloud properties that are used to estimate fluxes between CERES instrument measurements to account for the changing diurnal cycle. The data set is arranged as files for each hour and in netCDF-4 format. The observations are at 4-km resolution (at nadir) and are sub-sampled to 8 km.\r\n\r\nCERES is a key component of the Earth Observing System (EOS) program. The CERES instruments provide radiometric measurements of the Earth's atmosphere from three broadband channels. The CERES missions are a follow-on to the successful Earth Radiation Budget Experiment (ERBE) mission. The first CERES instrument, protoflight model (PFM), was launched on November 27, 1997 as part of the Tropical Rainfall Measuring Mission (TRMM). Two CERES instruments (FM1 and FM2) were launched into polar orbit on board the Earth Observing System (EOS) flagship Terra on December 18, 1999. Two additional CERES instruments (FM3 and FM4) were launched on board Earth Observing System (EOS) Aqua on May 4, 2002. The CERES FM5 instrument was launched on board the Suomi National Polar-orbiting Partnership (NPP) satellite on October 28, 2011. The newest CERES instrument (FM6) was launched on board the Joint Polar-Orbiting Satellite System 1 (JPSS-1) satellite, now called NOAA-20, on November 18, 2017.",
-            "title": "SatCORPS CERES GEO Edition 4 GOES-13 Southern Hemisphere Version 1.2",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGOES13%2FCERES%2FGEO_ED4_SH_V01.2",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGOES13%2FCERES%2FGEO_ED4_SH_V01.2",
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
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1587405101-LARC_ASDC",
-                    "description": "Earthdata Search for CER_GEO_Ed4_GOE13_SH_V01.2 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for CER_GEO_Ed4_GOE13_SH_V01.2 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1587405101-LARC_ASDC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/GOES13/CERES/GEO_ED4_SH_V01.2",
-                    "description": "DOI data set landing page for CER_GEO_Ed4_GOE13_SH_V01.2",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for CER_GEO_Ed4_GOE13_SH_V01.2",
+                    "downloadURL": "https://doi.org/10.5067/GOES13/CERES/GEO_ED4_SH_V01.2",
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
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/CERES/GEO/Edition4/GOE13_SH_V01.2/",
-                    "description": "ASDC Direct Data Download for CER_GEO_Ed4_GOE13_SH_V01.2",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for CER_GEO_Ed4_GOE13_SH_V01.2",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/CERES/GEO/Edition4/GOE13_SH_V01.2/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/CERES/GEO/Edition4/GOE13_SH_V01.2/contents.html",
-                    "description": "OPeNDAP data access for CER_GEO_Ed4_GOE13_SH_V01.2",
                     "@type": "dcat:Distribution",
+                    "description": "OPeNDAP data access for CER_GEO_Ed4_GOE13_SH_V01.2",
+                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/CERES/GEO/Edition4/GOE13_SH_V01.2/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 }
             ],
+            "identifier": "C1587405101-LARC_ASDC",
+            "issued": "2018-05-22",
+            "keyword": [
+                "atmosphere",
+                "earth science",
+                "clouds"
+            ],
+            "landingPage": "https://doi.org/10.5067/GOES13/CERES/GEO_ED4_SH_V01.2",
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
             "spatial": "<?xml version=\"1.0\" encoding=\"UTF-8\"?><gml:Polygon xmlns:gml=\"http://www.opengis.net/gml/3.2\" srsName=\"EPSG:9825\"><gml:outerBoundaryIs><gml:LinearRing><gml:posList>-60.0 -120.0 -60.0 -30.0 0.0 -30.0 0.0 -120.0 -60.0 -120.0</gml:posList></gml:LinearRing></gml:outerBoundaryIs><gml:innerBoundaryIs></gml:innerBoundaryIs></gml:Polygon>",
+            "temporal": "2015-07-01T00:00:00Z/2022-01-17T00:00:00Z",
             "theme": [
                 "CERES",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "SatCORPS CERES GEO Edition 4 GOES-13 Southern Hemisphere Version 1.2"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MER2-M-MTES-4-EMR-V1.0",
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
+            "description": "This archive contains Mars Exploration Rover Miniature Thermal Emission Spectrometer (Mini-TES) Emissivity Reduced Data Record (EMR) products and ancillary files. The Mini-TES EMR products archived on this volume are the original products used during mission operations by the Mars Exploration Rover project.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mer2-m-mtes-4-emr-v1.0_rva4-bjy4",
+            "issued": "2018-06-26",
+            "keyword": [
+                "mars",
+                "mars exploration rover"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MER2-M-MTES-4-EMR-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mer2-m-mtes-4-emr-v1.0_rva4-bjy4",
-            "description": "This archive contains Mars Exploration Rover Miniature Thermal Emission Spectrometer (Mini-TES) Emissivity Reduced Data Record (EMR) products and ancillary files. The Mini-TES EMR products archived on this volume are the original products used during mission operations by the Mars Exploration Rover project.",
-            "title": "MER2 MARS MINIATURE THERMAL EMISSION SPECTROMETER EMR V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "MER2 MARS MINIATURE THERMAL EMISSION SPECTROMETER EMR V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MSL-M-HAZCAM-5-RDR-V1.0",
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
+            "description": "Unknown",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.msl-m-hazcam-5-rdr-v1.0_rvbp-4viq",
+            "issued": "2018-06-26",
+            "keyword": [
+                "mars science laboratory",
+                "mars"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MSL-M-HAZCAM-5-RDR-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.msl-m-hazcam-5-rdr-v1.0_rvbp-4viq",
-            "description": "Unknown",
-            "title": "MSL MARS HAZARD AVOIDANCE CAMERA 5 RDR V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "MSL MARS HAZARD AVOIDANCE CAMERA 5 RDR V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=ULY-J-COSPIN-KET-3-RDR-RAW-HIRES-V1.0",
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
+            "description": "Raw data including single counter rates for the Semiconductor Detector D1 and the Anticoincidence A.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.uly-j-cospin-ket-3-rdr-raw-hires-v1.0_rvcp-jsd9",
+            "issued": "2021-05-21",
+            "keyword": [
+                "jupiter",
+                "ulysses"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=ULY-J-COSPIN-KET-3-RDR-RAW-HIRES-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.uly-j-cospin-ket-3-rdr-raw-hires-v1.0_rvcp-jsd9",
-            "description": "Raw data including single counter rates for the Semiconductor Detector D1 and the Anticoincidence A.",
-            "title": "ULY JUP COSPIN KIEL ELE TEL HIRES RAW\n                                        PARTICLE COUNT RATES",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ULY JUP COSPIN KIEL ELE TEL HIRES RAW\n                                        PARTICLE COUNT RATES"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/MEASURES/LANDMET/DATA001",
             "citation": "William B. Rossow. 2016-12-15. LANDMET. Version 1. Land Surface Atmospheric Boundary Interaction Product L3 V1. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/MEASURES/LANDMET/DATA001. https://disc.gsfc.nasa.gov/datacollection/LANDMET_1.html. Digital Science Data.",
-            "issued": "2016-11-22",
-            "temporal": "1998-01-01T00:00:00Z/2007-12-31T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2016-11-22",
-            "keyword": [
-                "precipitation",
-                "land surface",
-                "topography",
-                "atmospheric temperature",
-                "atmospheric radiation",
-                "atmospheric water vapor",
-                "atmospheric winds",
-                "land use/land cover",
-                "natural hazards",
-                "soils",
-                "surface thermal properties",
-                "earth science",
-                "human dimensions",
-                "atmosphere"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "SUHUNG SHEN",
                 "hasEmail": "mailto:suhung.shen@nasa.gov"
             },
+            "creator": "William B. Rossow",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C1374187813-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "This product is a multi-variate data compilation that reconciles the variation scales of these multiple measurements from varies resources, merges and maps them into a comprehensive description of the near-surface atmospheric properties together with the land surface property variations on diurnal-to-decadal time scales.   Many of these data products, especially those based on surface measurements, are spatially and/or temporally sparse or incomplete in coverage, so procedures were developed to fill missing values. \nThe data product is comprised of a sequence of daily global files, where quantities are mapped into 1.0-degree equivalent equal-area grid, with time sampling is reported at daily or 3-hourly intervals. The time period overlap among the products covers 10 years from 1998 to 2007.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "LANDMET",
-            "creator": "William B. Rossow",
-            "title": "Land Surface Atmospheric Boundary Interaction Product L3 V1(LANDMET) at GES DISC",
-            "graphic-preview-description": "This is a sample image of Near-surface air temperature at 2-meter from the product, LANDMET_L3_v1, on Jan 1 1998 at 00:00Z",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/LANDMET_1.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMEASURES%2FLANDMET%2FDATA001",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMEASURES%2FLANDMET%2FDATA001",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/LANDMET_1.png",
-                    "description": "This is a sample image of Near-surface air temperature at 2-meter from the product, LANDMET_L3_v1, on Jan 1 1998 at 00:00Z",
                     "@type": "dcat:Distribution",
+                    "description": "This is a sample image of Near-surface air temperature at 2-meter from the product, LANDMET_L3_v1, on Jan 1 1998 at 00:00Z",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/LANDMET_1.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/LANDMET_1.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/LANDMET_1.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://measures.gesdisc.eosdis.nasa.gov/data/LANDMET/LANDMET.1",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://measures.gesdisc.eosdis.nasa.gov/data/LANDMET/LANDMET.1",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=LANDMET",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=LANDMET",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://measures.gesdisc.eosdis.nasa.gov/opendap/LANDMET/LANDMET.1/contents.html",
-                    "description": "Access to the data via OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access to the data via OPeNDAP protocol.",
+                    "downloadURL": "https://measures.gesdisc.eosdis.nasa.gov/opendap/LANDMET/LANDMET.1/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://measures.gesdisc.eosdis.nasa.gov/data/LANDMET/LANDMET.1/doc/README.LANDMET_V1.pdf",
-                    "description": "README Document",
                     "@type": "dcat:Distribution",
+                    "description": "README Document",
+                    "downloadURL": "https://measures.gesdisc.eosdis.nasa.gov/data/LANDMET/LANDMET.1/doc/README.LANDMET_V1.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's read me document"
                 }
             ],
+            "graphic-preview-description": "This is a sample image of Near-surface air temperature at 2-meter from the product, LANDMET_L3_v1, on Jan 1 1998 at 00:00Z",
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/LANDMET_1.png",
+            "identifier": "C1374187813-GES_DISC",
+            "issued": "2016-11-22",
+            "keyword": [
+                "precipitation",
+                "land surface",
+                "topography",
+                "atmospheric temperature",
+                "atmospheric radiation",
+                "atmospheric water vapor",
+                "atmospheric winds",
+                "land use/land cover",
+                "natural hazards",
+                "soils",
+                "surface thermal properties",
+                "earth science",
+                "human dimensions",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.5067/MEASURES/LANDMET/DATA001",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2016-11-22",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
+            },
+            "release-place": "Greenbelt, MD, USA",
+            "series-name": "LANDMET",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "1998-01-01T00:00:00Z/2007-12-31T23:59:59Z",
             "theme": [
                 "MEaSUREs",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Land Surface Atmospheric Boundary Interaction Product L3 V1(LANDMET) at GES DISC"
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
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.go-a-c-ssi-2-redr-v1.0_rvg6-wy6c",
             "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "ida",
                 "non science",
@@ -1328246,294 +1328248,294 @@
                 "jupiter",
                 "comet sl9/jupiter collision"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=GO-A%2FC-SSI-2-REDR-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.go-a-c-ssi-2-redr-v1.0_rvg6-wy6c",
-            "description": "This data set has been generated by NASA's Galileo Project in order to distribute the images acquired by the Solid State Imaging (SSI) camera to the scientists and later to the Planetary Data System (PDS). The collection resides on volume GO_0016 and consists of all images acquired by the Galileo spacecraft during the period from the flyby of Ida through the Shoemaker-Levy 9 (SL9) comet impact on Jupiter. This includes data from SCLK 197327200 through 249221800 and contains the following targets: stars, Ida and Jupiter.",
-            "title": "GALILEO ORBITER ASTEROID AND COMET SL9 SOLID STATE IMAGING 2",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "GALILEO ORBITER ASTEROID AND COMET SL9 SOLID STATE IMAGING 2"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.7927/H4WW7FKN",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Center for International Earth Science Information Network - CIESIN. 1994-12-31. Georeferenced Population Datasets of Mexico (GEO-MEX): Urban Place GIS Coverage of Mexico. Version 1.00. Saginaw, MI. Archived by National Aeronautics and Space Administration, U.S. Government, NASA Socioeconomic Data and Applications Center (SEDAC). https://doi.org/10.7927/H4WW7FKN. https://doi.org/10.7927/H4WW7FKN.",
-            "issued": "1994-12-31",
-            "temporal": "1921-01-01T00:00:00Z/1990-12-31T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "1994-12-31",
-            "references": [
-                "https://doi.org/10.7927/H45D8PS8",
-                "https://doi.org/10.7927/H4S46PV7",
-                "https://doi.org/10.7927/H4959FH0",
-                "https://doi.org/10.7927/H41N7Z2Z"
-            ],
-            "keyword": [
-                "boundaries",
-                "human dimensions",
-                "earth science",
-                "population"
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
-            "identifier": "C179001923-SEDAC",
-            "description": "The Urban Place GIS Coverage of Mexico is a vector based point Geographic Information System (GIS) coverage of 696 urban places in Mexico. Each Urban Place is geographically referenced down to one tenth of a minute. The attribute data include time-series population and selected census/geographic data items for Mexican urban places from from 1921 to 1990. The cartographic data include urban place point locations on a state boundary file of Mexico. This data set is  produced by the Columbia University Center for International Earth Science Information Network (CIESIN) in collaboration with the Instituto Nacional de Estadistica Geografia e Informatica (INEGI) and the Environmental Research Institute (ERI) of Michigan.",
-            "release-place": "Saginaw, MI",
-            "graphic-preview-description": "Sample browse graphic of the data set.",
             "creator": "Center for International Earth Science Information Network - CIESIN",
-            "title": "Georeferenced Population Datasets of Mexico (GEO-MEX): Urban Place GIS Coverage of Mexico",
-            "graphic-preview-file": "https://sedac.ciesin.columbia.edu/downloads/maps/geo-mex/geo-mex-mexico-urban-place-gis/sedac-logo.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The Urban Place GIS Coverage of Mexico is a vector based point Geographic Information System (GIS) coverage of 696 urban places in Mexico. Each Urban Place is geographically referenced down to one tenth of a minute. The attribute data include time-series population and selected census/geographic data items for Mexican urban places from from 1921 to 1990. The cartographic data include urban place point locations on a state boundary file of Mexico. This data set is  produced by the Columbia University Center for International Earth Science Information Network (CIESIN) in collaboration with the Instituto Nacional de Estadistica Geografia e Informatica (INEGI) and the Environmental Research Institute (ERI) of Michigan.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.7927%2FH4WW7FKN",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.7927%2FH4WW7FKN",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/downloads/maps/geo-mex/geo-mex-mexico-urban-place-gis/sedac-logo.jpg",
-                    "description": "Sample browse graphic of the data set.",
                     "@type": "dcat:Distribution",
+                    "description": "Sample browse graphic of the data set.",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/downloads/maps/geo-mex/geo-mex-mexico-urban-place-gis/sedac-logo.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/geo-mex-mexico-urban-place-gis/data-download",
-                    "description": "Data Download Page",
                     "@type": "dcat:Distribution",
+                    "description": "Data Download Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/geo-mex-mexico-urban-place-gis/data-download",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://sedac.ciesin.columbia.edu/data/set/geo-mex-mexico-urban-place-gis/docs",
-                    "description": "Documentation Page",
                     "@type": "dcat:Distribution",
+                    "description": "Documentation Page",
+                    "downloadURL": "http://sedac.ciesin.columbia.edu/data/set/geo-mex-mexico-urban-place-gis/docs",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/geo-mex-mexico-urban-place-gis",
-                    "description": "Data Set\u00a0Overview Page",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set\u00a0Overview Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/geo-mex-mexico-urban-place-gis",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "graphic-preview-description": "Sample browse graphic of the data set.",
+            "graphic-preview-file": "https://sedac.ciesin.columbia.edu/downloads/maps/geo-mex/geo-mex-mexico-urban-place-gis/sedac-logo.jpg",
+            "identifier": "C179001923-SEDAC",
+            "issued": "1994-12-31",
+            "keyword": [
+                "boundaries",
+                "human dimensions",
+                "earth science",
+                "population"
+            ],
+            "landingPage": "https://doi.org/10.7927/H4WW7FKN",
+            "language": [
+                "en-US"
+            ],
+            "modified": "1994-12-31",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "SEDAC"
+            },
+            "references": [
+                "https://doi.org/10.7927/H45D8PS8",
+                "https://doi.org/10.7927/H4S46PV7",
+                "https://doi.org/10.7927/H4959FH0",
+                "https://doi.org/10.7927/H41N7Z2Z"
+            ],
+            "release-place": "Saginaw, MI",
             "spatial": "-117.0 14.0 -86.0 33.0",
+            "temporal": "1921-01-01T00:00:00Z/1990-12-31T00:00:00Z",
             "theme": [
                 "GEO-MEX",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Georeferenced Population Datasets of Mexico (GEO-MEX): Urban Place GIS Coverage of Mexico"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ASDC/SUBORBITAL/SONEX_Merge_DC8_Data_1",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2023-08-21. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/ASDC/SUBORBITAL/SONEX_Merge_DC8_Data_1.",
-            "issued": "1997-10-07",
-            "temporal": "1997-10-07T00:00:00Z/1997-11-12T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "1997-11-12",
-            "keyword": [
-                "atmosphere",
-                "platform characteristics",
-                "air quality",
-                "aerosols",
-                "atmospheric winds",
-                "atmospheric chemistry",
-                "atmospheric pressure",
-                "atmospheric temperature",
-                "spectral/engineering",
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
-            "identifier": "C2662407660-LARC_ASDC",
             "description": "SONEX_Merge_DC8_Data_1 is all of the project generated merge files for the SONEX suborbital campaign. Types of merges include 1- and 5-minute, aerosol composition-based, H2O2-based, HNO3-based, hydrocarbon-based, NO-based, and PAN-based merges. Data collection for this product is complete.\r\nThe SASS (Subsonics Assessment) Ozone and NOx Experiment (SONEX) was an international, multi-organizational mission that took place in October-November 1997. NASA was the US sponsor of SONEX that partnered with POLINAT-2 (Pollution from Aircraft Emissions in the North Atlantic Flight Corridor) funded by the German DLR (Deutsches Zentrum f\u00fcr Luft- und Raumfahrt) or German Aerospace Agency. NASA flew the DC-8 aircraft out of NASA/Ames Research Center. DLR operated an instrumented Falcon 20 aircraft. The staging locations for NAFC sampling were primarily Bangor, Maine (US), and Shannon, Ireland. Subsonic aircraft emissions impact several aspects of atmospheric composition: nitrogen oxides (NOx), CO, and hydrocarbons from emissions can perturb upper tropospheric/lower stratospheric (UT/LS) ozone; water vapor, soot, and sulfur oxides (SOx) emitted by aircraft may perturb clouds and aerosols, changing UT/LS radiative forcing and global temperature.\r\nIn SONEX and POLINAT, flights were conducted in the vicinity of the North Atlantic Flight Coordinator (NAFC) to observe the impact of aircraft emissions on NOx and ozone (O3). The DC-8 aircraft payload (Singh et al., 1999) primarily measured in-situ CO, CO2, hydrocarbons/halocarbons, O3, aerosols (Dibb et al., 2000), OH/HO2, water vapor, nitric acid (Talbot et al., 1999), photolysis rates, temperature, pressure, winds, NOx, and NOy.\r\nThree sampling approaches were implemented during SONEX. First, special meteorological (Fuelberg et al., 2000) were developed to allow targeted sampling for air parcels affected by aircraft emissions and various meteorological events, e.g., convection, lightning (Jeker et al., 2000), stratospheric intrusions (Cho et al., 2000). Second, because the NAFC had not been extensively sampled in the past, it was important for SONEX to characterize the climatology of trace species like CN (Wang et al., 2000), NOx and NOy (Koike et al., 2000). Third, tracers (Simpson et al., 2000; Thompson et al., 1999) and model sensitivity studies (Meijer et al., 2000) were employed for Air Mass Identification. This sampling strategy answered the following questions: Where and when are air masses found with the greatest aircraft influence? When and where was stratospheric air sampled? SONEX showed a substantial impact of aircraft emissions on UT/LS NOx and CN in the vicinity of fresh aircraft emissions. However, during October-November 1997 over the NAFC, UT/LS NOx was dominated by surface emissions redistributed by convection and augmented by lightning.",
-            "title": "SASS (Subsonics Assessment) Ozone and NOx Experiment (SONEX) Merge Data Files",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC%2FSUBORBITAL%2FSONEX_Merge_DC8_Data_1",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC%2FSUBORBITAL%2FSONEX_Merge_DC8_Data_1",
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
-                    "downloadURL": "https://doi.org/10.1029/1999GL900588",
-                    "description": "SONEX airborne mission and coordinated POLINAT-2 activity: Overview and accomplishments",
                     "@type": "dcat:Distribution",
+                    "description": "SONEX airborne mission and coordinated POLINAT-2 activity: Overview and accomplishments",
+                    "downloadURL": "https://doi.org/10.1029/1999GL900588",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.1029/1999JD900424",
-                    "description": "Composition and distribution of aerosols over the North Atlantic during the Subsonic Assessment Ozone and Nitrogen Oxide Experiment (SONEX)",
                     "@type": "dcat:Distribution",
+                    "description": "Composition and distribution of aerosols over the North Atlantic during the Subsonic Assessment Ozone and Nitrogen Oxide Experiment (SONEX)",
+                    "downloadURL": "https://doi.org/10.1029/1999JD900424",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.1029/1999GL900589",
-                    "description": "Reactive nitrogen budget during the NASA SONEX Mission",
                     "@type": "dcat:Distribution",
+                    "description": "Reactive nitrogen budget during the NASA SONEX Mission",
+                    "downloadURL": "https://doi.org/10.1029/1999GL900589",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.1029/1999JD900917",
-                    "description": "A meteorological overview of the Subsonic Assessment Ozone and Nitrogen Oxide Experiment (SONEX) period",
                     "@type": "dcat:Distribution",
+                    "description": "A meteorological overview of the Subsonic Assessment Ozone and Nitrogen Oxide Experiment (SONEX) period",
+                    "downloadURL": "https://doi.org/10.1029/1999JD900917",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.1029/1999JD901053",
-                    "description": "Measurements of nitrogen oxides at the tropopause: Attribution to convection and correlation with lightning",
                     "@type": "dcat:Distribution",
+                    "description": "Measurements of nitrogen oxides at the tropopause: Attribution to convection and correlation with lightning",
+                    "downloadURL": "https://doi.org/10.1029/1999JD901053",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.1029/1999JD900430",
-                    "description": "Observations of convective and dynamical instabilities in tropopause folds and their contribution to stratosphere-troposphere exchange",
                     "@type": "dcat:Distribution",
+                    "description": "Observations of convective and dynamical instabilities in tropopause folds and their contribution to stratosphere-troposphere exchange",
+                    "downloadURL": "https://doi.org/10.1029/1999JD900430",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.1029/1999GL010930",
-                    "description": "Evidence of convection as a major source of condensation nuclei in the northern midlatitude upper troposphere",
                     "@type": "dcat:Distribution",
+                    "description": "Evidence of convection as a major source of condensation nuclei in the northern midlatitude upper troposphere",
+                    "downloadURL": "https://doi.org/10.1029/1999GL010930",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.1029/1999JD901013",
-                    "description": "Impact of aircraft emissions on reactive nitrogen over the North Atlantic Flight Corridor region",
                     "@type": "dcat:Distribution",
+                    "description": "Impact of aircraft emissions on reactive nitrogen over the North Atlantic Flight Corridor region",
+                    "downloadURL": "https://doi.org/10.1029/1999JD901013",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.1029/1999JD900750",
-                    "description": "Nonmethane hydrocarbon measurements in the North Atlantic Flight Corridor during the Subsonic Assessment Ozone and Nitrogen Oxide Experiment",
                     "@type": "dcat:Distribution",
+                    "description": "Nonmethane hydrocarbon measurements in the North Atlantic Flight Corridor during the Subsonic Assessment Ozone and Nitrogen Oxide Experiment",
+                    "downloadURL": "https://doi.org/10.1029/1999JD900750",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.1029/1999GL900581",
-                    "description": "Perspectives on NO, NOy, and fine aerosol sources and variability during SONEX",
                     "@type": "dcat:Distribution",
+                    "description": "Perspectives on NO, NOy, and fine aerosol sources and variability during SONEX",
+                    "downloadURL": "https://doi.org/10.1029/1999GL900581",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.1029/1999JD901052",
-                    "description": "Model calculations of the impact of NOx from air traffic, lightning, and surface emissions, compared with measurements",
                     "@type": "dcat:Distribution",
+                    "description": "Model calculations of the impact of NOx from air traffic, lightning, and surface emissions, compared with measurements",
+                    "downloadURL": "https://doi.org/10.1029/1999JD901052",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://espo.nasa.gov/content/Ames_Format_Overview",
-                    "description": "Ames File Format",
                     "@type": "dcat:Distribution",
+                    "description": "Ames File Format",
+                    "downloadURL": "https://espo.nasa.gov/content/Ames_Format_Overview",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2662407660-LARC_ASDC",
-                    "description": "Earthdata Search client for SONEX_Merge_DC8_Data_1",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search client for SONEX_Merge_DC8_Data_1",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2662407660-LARC_ASDC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/ASDC/SUBORBITAL/SONEX_Merge_DC8_Data_1",
-                    "description": "DOI for SONEX_Merge_DC8_Data_1",
                     "@type": "dcat:Distribution",
+                    "description": "DOI for SONEX_Merge_DC8_Data_1",
+                    "downloadURL": "https://doi.org/10.5067/ASDC/SUBORBITAL/SONEX_Merge_DC8_Data_1",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/SONEX/Merge_DC8_Data_1/",
-                    "description": "ASDC Direct Data Download for SONEX_Merge_DC8_Data_1",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for SONEX_Merge_DC8_Data_1",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/SONEX/Merge_DC8_Data_1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 }
             ],
+            "identifier": "C2662407660-LARC_ASDC",
+            "issued": "1997-10-07",
+            "keyword": [
+                "atmosphere",
+                "platform characteristics",
+                "air quality",
+                "aerosols",
+                "atmospheric winds",
+                "atmospheric chemistry",
+                "atmospheric pressure",
+                "atmospheric temperature",
+                "spectral/engineering",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/ASDC/SUBORBITAL/SONEX_Merge_DC8_Data_1",
+            "language": [
+                "en-US"
+            ],
+            "modified": "1997-11-12",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/LARC/SD/ASDC"
+            },
             "spatial": "<?xml version=\"1.0\" encoding=\"UTF-8\"?><gml:Polygon xmlns:gml=\"http://www.opengis.net/gml/3.2\" srsName=\"EPSG:9825\"><gml:outerBoundaryIs><gml:LinearRing><gml:posList>19.89 -178.2 19.89 148.2 84.32 148.2 84.32 -178.2 19.89 -178.2</gml:posList></gml:LinearRing></gml:outerBoundaryIs><gml:innerBoundaryIs></gml:innerBoundaryIs></gml:Polygon>",
+            "temporal": "1997-10-07T00:00:00Z/1997-11-12T23:59:59.999Z",
             "theme": [
                 "SONEX",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "SASS (Subsonics Assessment) Ozone and NOx Experiment (SONEX) Merge Data Files"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=GO-J-PLS-3-RDR-FULLRES-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This data set contains raw data from the Plasma Science instrument (PLS) on the Galileo spacecraft for all Jupiter orbits. These data have been reformatted into ASCII tables to facilitate data processing and analysis.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.go-j-pls-3-rdr-fullres-v1.0_rvka-ad8v",
             "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "ganymede",
                 "jupiter",
@@ -1328542,58 +1328544,36 @@
                 "galileo",
                 "europa"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=GO-J-PLS-3-RDR-FULLRES-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.go-j-pls-3-rdr-fullres-v1.0_rvka-ad8v",
-            "description": "This data set contains raw data from the Plasma Science instrument (PLS) on the Galileo spacecraft for all Jupiter orbits. These data have been reformatted into ASCII tables to facilitate data processing and analysis.",
-            "title": "GALILEO JUPITER RDR FULL RESOLUTION PLASMA DATA V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "GALILEO JUPITER RDR FULL RESOLUTION PLASMA DATA V1.0"
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
-            "identifier": "NASA-637",
             "description": "Data Dictionary and Index Files",
-            "title": "PDS Data Dictionary (1r73)",
-            "programCode": [
-                "026:005"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -1328601,151 +1328581,150 @@
                     "mediaType": "application/html"
                 }
             ],
-            "accrualPeriodicity": "irregular",
+            "identifier": "NASA-637",
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
+            "title": "PDS Data Dictionary (1r73)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1171",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Asner, G.P., A.R. Townsend, and M.M.C. Bustamante. 2013. LBA-ECO ND-10 Soil Properties of Pasture Chronosequences, Para, Brazil: 1997. ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/1171",
-            "issued": "2023-10-03",
-            "temporal": "1997-08-01T00:00:00Z/1997-08-31T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-10-12",
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
-            "identifier": "C2781558603-ORNL_CLOUD",
             "description": "This data set provides the results of soil physical property and chemical measurements of samples collected from two pasture chronosequences (years since conversion from primary forest) located on two ranches south of Santarem, Para, Brazil, and east of the Tapajos River. Soil data includes soil classification, bulk density, texture, and mean concentrations of total nitrogen (N), carbon (C), phosphorus (P), and P fractions. The soils were high clay oxisols and highly sandy entisols.One chronosequence of sites was established on oxisol soils dating 2, 7, and 15 years since conversion from primary forest. A second set of sites, 1, 7, and 15 years old was established on the sandy entisols. Five of the six pasture sites were on a single ranch; the 2-year-old oxisol pasture was the exception. Ten soil samples per site were collected from 0-10 cm depth along random intervals within 100-m transects in August 1997.There are two comma-delimited (.csv) data files with this data set.",
-            "graphic-preview-description": "Browse Image",
-            "title": "LBA-ECO ND-10 Soil Properties of Pasture Chronosequences, Para, Brazil: 1997",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/lba_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1171",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1171",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/lba/nutrient_dynamics/ND10_Soil_Chemistry/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/lba/nutrient_dynamics/ND10_Soil_Chemistry/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/LBA/guides/ND10_Soil_Chemistry.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/LBA/guides/ND10_Soil_Chemistry.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1171",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1171",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/nutrient_dynamics/ND10_Soil_Chemistry/comp/ND10_Soil_Chemistry.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/nutrient_dynamics/ND10_Soil_Chemistry/comp/ND10_Soil_Chemistry.pdf",
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
+            "identifier": "C2781558603-ORNL_CLOUD",
+            "issued": "2023-10-03",
+            "keyword": [
+                "soils",
+                "land surface",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1171",
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
             "spatial": "-54.93 -3.27 -54.67 -3.13",
+            "temporal": "1997-08-01T00:00:00Z/1997-08-31T23:59:59Z",
             "theme": [
                 "LBA-ECO",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "LBA-ECO ND-10 Soil Properties of Pasture Chronosequences, Para, Brazil: 1997"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/VIIRS/VJ109_NRT.002",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "LANCEMODIS. 2023-10-10. VIIRS/JPSS1 Atmospherically Corrected Surface Reflectance 6-Min L2 Swath IP 375m, 750m NRT. Version 2. NASA GSFC LANCE. Archived by National Aeronautics and Space Administration, U.S. Government, LANCEMODIS. https://doi.org/10.5067/VIIRS/VJ109_NRT.002. https://earthdata.nasa.gov/earth-observation-data/near-real-time/download-nrt-data/viirs-nrt.",
-            "issued": "2023-10-10",
-            "temporal": "2023-10-10T00:00:00Z/2023-10-16T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-10-11",
-            "keyword": [
-                "earth science",
-                "surface thermal properties",
-                "surface radiative properties",
-                "land surface"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "LANCEMODIS",
                 "hasEmail": "mailto:support@earthdata.nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/EOS/ESDIS/LANCE MODIS"
-            },
-            "identifier": "C2780802523-LANCEMODIS",
-            "description": "The VJ109_NRT is a Near Real Time (NRT) Visible Infrared Imager Radiometer Suite (VIIRS) 375 m, 750 m Atmospherically Corrected Surface Reflectance product. The VIIRS surface reflectance products are estimates of surface reflectance in each of the VIIRS reflective bands I1-I3, M1-M5, M7, M8, M10, and M11. The VNP09 Level-2 surface reflectance product contains approximately 6 minutes' worth of data. Surface reflectance for each moderate-resolution (750m) or imagery-resolution (375m) pixel is retrieved separately for the Level-2 products. \r\n\r\n\r\nSurface reflectance is obtained by adjusting top-of-atmosphere reflectance to compensate for atmospheric effects. Corrections are made for the effects of molecular gases, including ozone and water vapor, and for the effects of atmospheric aerosols. The inputs to the surface reflectance algorithm include top-of-atmosphere reflectance for the VIIRS visible bands (VJ102MOD, VJ102IMG), the VIIRS cloud mask and aerosol product, aerosol optical thickness, and atmospheric data obtained from a reanalysis (surface pressure, atmospheric precipitable water, and ozone concentration).\r\n\r\n\r\nAll surface reflectance products are produced for daytime conditions only. The product is produced under all atmospheric conditions except for night and oceans. Pixels when not produced are replaced by fill values in the Level-2 and Level-2G products.\r\n\r\n\r\nFor more information read Suomi-NPP VIIRS Surface Reflectance User's Guide at https://viirsland.gsfc.nasa.gov/PDF/VIIRS_Surf_Refl_UserGuide_v2.0.pdf\r\n\r\nor \r\n\r\nvisit VIIRS Land website at https://viirsland.gsfc.nasa.gov/index.html",
-            "release-place": "NASA GSFC LANCE",
             "creator": "LANCEMODIS",
-            "title": "VIIRS/JPSS1 Atmospherically Corrected Surface Reflectance 6-Min L2 Swath IP 375m, 750m NRT",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The VJ109_NRT is a Near Real Time (NRT) Visible Infrared Imager Radiometer Suite (VIIRS) 375 m, 750 m Atmospherically Corrected Surface Reflectance product. The VIIRS surface reflectance products are estimates of surface reflectance in each of the VIIRS reflective bands I1-I3, M1-M5, M7, M8, M10, and M11. The VNP09 Level-2 surface reflectance product contains approximately 6 minutes' worth of data. Surface reflectance for each moderate-resolution (750m) or imagery-resolution (375m) pixel is retrieved separately for the Level-2 products. \r\n\r\n\r\nSurface reflectance is obtained by adjusting top-of-atmosphere reflectance to compensate for atmospheric effects. Corrections are made for the effects of molecular gases, including ozone and water vapor, and for the effects of atmospheric aerosols. The inputs to the surface reflectance algorithm include top-of-atmosphere reflectance for the VIIRS visible bands (VJ102MOD, VJ102IMG), the VIIRS cloud mask and aerosol product, aerosol optical thickness, and atmospheric data obtained from a reanalysis (surface pressure, atmospheric precipitable water, and ozone concentration).\r\n\r\n\r\nAll surface reflectance products are produced for daytime conditions only. The product is produced under all atmospheric conditions except for night and oceans. Pixels when not produced are replaced by fill values in the Level-2 and Level-2G products.\r\n\r\n\r\nFor more information read Suomi-NPP VIIRS Surface Reflectance User's Guide at https://viirsland.gsfc.nasa.gov/PDF/VIIRS_Surf_Refl_UserGuide_v2.0.pdf\r\n\r\nor \r\n\r\nvisit VIIRS Land website at https://viirsland.gsfc.nasa.gov/index.html",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FVIIRS%2FVJ109_NRT.002",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FVIIRS%2FVJ109_NRT.002",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nrt3.modaps.eosdis.nasa.gov/archive/allData/5200/VJ109_NRT",
-                    "description": "Direct access to the download site and directory hosting the VJ109_NRT data set.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct access to the download site and directory hosting the VJ109_NRT data set.",
+                    "downloadURL": "https://nrt3.modaps.eosdis.nasa.gov/archive/allData/5200/VJ109_NRT",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
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
@@ -1328755,832 +1328734,829 @@
                     "title": "View this dataset's user's guide"
                 }
             ],
+            "identifier": "C2780802523-LANCEMODIS",
+            "issued": "2023-10-10",
+            "keyword": [
+                "earth science",
+                "surface thermal properties",
+                "surface radiative properties",
+                "land surface"
+            ],
+            "landingPage": "https://doi.org/10.5067/VIIRS/VJ109_NRT.002",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2023-10-11",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/EOS/ESDIS/LANCE MODIS"
+            },
+            "release-place": "NASA GSFC LANCE",
             "spatial": "-180.0 -80.0 180.0 80.0",
+            "temporal": "2023-10-10T00:00:00Z/2023-10-16T00:00:00Z",
             "theme": [
                 "LANCE",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "VIIRS/JPSS1 Atmospherically Corrected Surface Reflectance 6-Min L2 Swath IP 375m, 750m NRT"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-COMPIL-5-TNOCENALB-V2.0",
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
+            "description": "This data set is a compilation of published diameters, albedos, and densities for Transneptunian Objects (TNOs) and Centaurs. A total of 167 objects are listed, many with more than one entry. This version covers published values through 31 March 2014.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-compil-5-tnocenalb-v2.0_rvru-qmdk",
+            "issued": "2021-05-21",
+            "keyword": [
+                "support archives",
+                "asteroid"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-COMPIL-5-TNOCENALB-V2.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-compil-5-tnocenalb-v2.0_rvru-qmdk",
-            "description": "This data set is a compilation of published diameters, albedos, and densities for Transneptunian Objects (TNOs) and Centaurs. A total of 167 objects are listed, many with more than one entry. This version covers published values through 31 March 2014.",
-            "title": "TNO AND CENTAUR DIAMETERS, ALBEDOS, AND DENSITIES V2.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "TNO AND CENTAUR DIAMETERS, ALBEDOS, AND DENSITIES V2.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-4-PRL-67P-M08-INF-REFL-V1.0",
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
+            "description": "This CODMAC level 4 data set contains solar stray-light corrected, in-field stray-light corrected,  radiometric calibrated and geometric distortion corrected  (resampled) image data in reflectance units (normalized  and thus without unit),  acquired by the OSIRIS Wide Angle Camera on the Rosetta spacecraft  during the PRELANDING mission phase, covering the period  from 2014-09-23T10:00:00.000 to 2014-10-24T09:59:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V1.0 is the first version of this dataset: Lien corrected dataset after September 2019 PSA/PDS external peer review.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-4-prl-67p-m08-inf-refl-v1.0_rvta-umfh",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-4-PRL-67P-M08-INF-REFL-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-4-prl-67p-m08-inf-refl-v1.0_rvta-umfh",
-            "description": "This CODMAC level 4 data set contains solar stray-light corrected, in-field stray-light corrected,  radiometric calibrated and geometric distortion corrected  (resampled) image data in reflectance units (normalized  and thus without unit),  acquired by the OSIRIS Wide Angle Camera on the Rosetta spacecraft  during the PRELANDING mission phase, covering the period  from 2014-09-23T10:00:00.000 to 2014-10-24T09:59:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V1.0 is the first version of this dataset: Lien corrected dataset after September 2019 PSA/PDS external peer review.",
-            "title": "ROSETTA-ORBITER 67P OSIWAC 4 PRL-MTP008 RDR-INF-REFL V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P OSIWAC 4 PRL-MTP008 RDR-INF-REFL V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/Aqua/AIRS/DATA315",
             "citation": "AIRS Science Team/Joao Teixeira. 2013-03-12. AIRS3SP8. Version 006. AIRS/Aqua L3 8-day Support Product (AIRS-only) 1 degree X 1 degree V006. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/Aqua/AIRS/DATA315. https://disc.gsfc.nasa.gov/datacollection/AIRS3SP8_006.html. Digital Science Data.",
-            "issued": "2002-09-01",
-            "temporal": "2002-09-01T00:00:00Z/2025-01-13T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-12-26",
-            "references": [
-                "https://doi.org/10.1117/1.JRS.8.084994",
-                "https://doi.org/10.5194/acp-14-399-2014"
-            ],
-            "keyword": [
-                "ocean temperature",
-                "precipitation",
-                "surface radiative properties",
-                "atmosphere",
-                "altitude",
-                "oceans",
-                "land surface",
-                "earth science",
-                "air quality",
-                "clouds",
-                "atmospheric water vapor",
-                "surface thermal properties",
-                "atmospheric temperature",
-                "atmospheric radiation",
-                "atmospheric pressure",
-                "atmospheric chemistry"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "ED ESFANDIARI",
                 "hasEmail": "mailto:asghar.e.esfandiari@nasa.gov"
             },
+            "creator": "AIRS Science Team/Joao Teixeira",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C1238517268-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "The Atmospheric Infrared Sounder (AIRS) is a grating spectrometer (R = 1200) aboard the second Earth Observing System (EOS) polar-orbiting platform, EOS Aqua. In combination with the Advanced Microwave Sounding Unit (AMSU) and the Humidity Sounder for Brazil (HSB), AIRS constitutes an innovative atmospheric sounding group of visible, infrared, and microwave sensors. The L3 support products are similar to the L3 standard products but contain fields which are not fully validated, or are inputs or intermediary values. Because no quality control information is available for some of these fields, values from failed retrievals may be included.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "AIRS3SP8",
-            "creator": "AIRS Science Team/Joao Teixeira",
-            "graphic-preview-description": "Sample data of the \"AIRS/Aqua Level 3 multi-day standard physical retrieval product (AIRS only)\".",
-            "title": "AIRS/Aqua L3 8-day Support Product (AIRS-only) 1 degree X 1 degree V006 (AIRS3SP8) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/AIRS3SP8_006.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAqua%2FAIRS%2FDATA315",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAqua%2FAIRS%2FDATA315",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/AIRS3SP8_006.png",
-                    "description": "Sample data of the \"AIRS/Aqua Level 3 multi-day standard physical retrieval product (AIRS only)\".",
                     "@type": "dcat:Distribution",
+                    "description": "Sample data of the \"AIRS/Aqua Level 3 multi-day standard physical retrieval product (AIRS only)\".",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/AIRS3SP8_006.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/AIRS3SP8_006.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/AIRS3SP8_006.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/Aqua_AIRS_Level3/AIRS3SP8.006/",
-                    "description": "Access the data via HTTP.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTP.",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/Aqua_AIRS_Level3/AIRS3SP8.006/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/opendap/Aqua_AIRS_Level3/AIRS3SP8.006/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/opendap/Aqua_AIRS_Level3/AIRS3SP8.006/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=AIRS3SP8+006",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=AIRS3SP8+006",
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
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/repository/Mission/AIRS/3.3_ScienceDataProductDocumentation/3.3.4_ProductGenerationAlgorithms/README.AIRS_V6.pdf",
-                    "description": "README Document",
                     "@type": "dcat:Distribution",
+                    "description": "README Document",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/repository/Mission/AIRS/3.3_ScienceDataProductDocumentation/3.3.4_ProductGenerationAlgorithms/README.AIRS_V6.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's read me document"
                 }
             ],
+            "graphic-preview-description": "Sample data of the \"AIRS/Aqua Level 3 multi-day standard physical retrieval product (AIRS only)\".",
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/AIRS3SP8_006.png",
+            "identifier": "C1238517268-GES_DISC",
+            "issued": "2002-09-01",
+            "keyword": [
+                "ocean temperature",
+                "precipitation",
+                "surface radiative properties",
+                "atmosphere",
+                "altitude",
+                "oceans",
+                "land surface",
+                "earth science",
+                "air quality",
+                "clouds",
+                "atmospheric water vapor",
+                "surface thermal properties",
+                "atmospheric temperature",
+                "atmospheric radiation",
+                "atmospheric pressure",
+                "atmospheric chemistry"
+            ],
+            "landingPage": "https://doi.org/10.5067/Aqua/AIRS/DATA315",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2024-12-26",
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
+            "series-name": "AIRS3SP8",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2002-09-01T00:00:00Z/2025-01-13T00:00:00Z",
             "theme": [
                 "Aqua",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "AIRS/Aqua L3 8-day Support Product (AIRS-only) 1 degree X 1 degree V006 (AIRS3SP8) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/2UUZUX6GJ49C",
             "citation": "Nadia Smith. 2019-01-15. SNDRAQIL2PLEVCPS. Version 2.1. Sounder SIPS: AQUA AIRS IR-only Level 2: Atmospheric state at Standard Pressure Levels derived from CLIMCAPS V2.1. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/2UUZUX6GJ49C. https://disc.gsfc.nasa.gov/datacollection/SNDRAQIL2PLEVCPS_2.1.html. Digital Science Data.",
-            "issued": "2002-08-31",
-            "temporal": "2002-08-31T00:00:00Z/2024-12-30T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-12-01",
-            "references": [
-                "https://doi.org/DOI  10.3390/rs11101227",
-                "https://doi.org/10.1109/TGRS.2012.2220369",
-                "https://doi.org/10.1016/S0022-4073(97)00169-6",
-                "https://doi.org/10.1109/TGRS.2002.808236",
-                "https://doi.org/10.1029/2005/JD007020",
-                "https://doi.org/10.5194/amt-13-4437-2020"
-            ],
-            "keyword": [
-                "air quality",
-                "atmospheric chemistry",
-                "atmospheric temperature",
-                "atmospheric water vapor",
-                "atmosphere",
-                "altitude",
-                "clouds",
-                "earth science"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Lena Iredell",
                 "hasEmail": "mailto:lena.iredell@nasa.gov"
             },
+            "creator": "Nadia Smith",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C2791411861-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Not provided"
-            },
             "description": "The CLIMCAPS (Community Long-term Infrared Microwave Coupled Product System) algorithm is used to analyze data from the AIRS (Atmospheric Infrared Sounder) instrument aboard the Earth Observing System (EOS) polar-orbiting platform, EOS Aqua. This file contains the fixed Pressure Level product (PLEV) variables derived from the CLIMCAPS algorithm using data. They include including gas mixing ratio profiles, column totals, surface values, tropopause properties, and relative humidity, together with per-field quality flagging. The profiles are specified at the surface and layer boundaries and are estimated from layer amounts using the L2 algorithm\n\nAn AIRS granule has been set as 6 minutes of data, 30 footprints cross track by 45 lines along track. There are 240 granules per day, with an orbit repeat cycle of approximately 16 day.\n\nThe CLIMCAPS algorithm uses data from the second Modern-Era Retrospective analysis for Research and Applications (MERRA-2) as a first-guess for the atmospheric state.  Because MERRA-2 products typically have a latency from 3 to 7 weeks, so too do the CLIMCAPS products.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "SNDRAQIL2PLEVCPS",
-            "creator": "Nadia Smith",
-            "graphic-preview-description": "Sample plot of CLIMCAPS Level 2 Pressure Level product.",
-            "title": "Sounder SIPS: AQUA AIRS IR-only Level 2: Atmospheric state at Standard Pressure Levels derived from CLIMCAPS V2.1 (SNDRAQIL2PLEVCPS) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/SNDRAQIL2PLEVCPS_2.1.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2F2UUZUX6GJ49C",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2F2UUZUX6GJ49C",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/SNDRAQIL2PLEVCPS_2.1.png",
-                    "description": "Sample plot of CLIMCAPS Level 2 Pressure Level product.",
                     "@type": "dcat:Distribution",
+                    "description": "Sample plot of CLIMCAPS Level 2 Pressure Level product.",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/SNDRAQIL2PLEVCPS_2.1.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/SNDRAQIL2PLEVCPS_2.1.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/SNDRAQIL2PLEVCPS_2.1.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sounder.gesdisc.eosdis.nasa.gov/data/Aqua_Sounder_Level2/SNDRAQIL2PLEVCPS.2.1/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://sounder.gesdisc.eosdis.nasa.gov/data/Aqua_Sounder_Level2/SNDRAQIL2PLEVCPS.2.1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sounder.gesdisc.eosdis.nasa.gov/opendap/Aqua_Sounder_Level2/SNDRAQIL2PLEVCPS.2.1/",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://sounder.gesdisc.eosdis.nasa.gov/opendap/Aqua_Sounder_Level2/SNDRAQIL2PLEVCPS.2.1/",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=SNDRAQIL2PLEVCPS+2.1",
-                    "description": "Search the Earthdata website",
                     "@type": "dcat:Distribution",
+                    "description": "Search the Earthdata website",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=SNDRAQIL2PLEVCPS+2.1",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Sounder/CLIMCAPS.PLEV.CPS.L2.V2.1.README.pdf",
-                    "description": "CLIMCAPS L2 Product User Guide:File Format and Definition",
                     "@type": "dcat:Distribution",
+                    "description": "CLIMCAPS L2 Product User Guide:File Format and Definition",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Sounder/CLIMCAPS.PLEV.CPS.L2.V2.1.README.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's read me document"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Sounder/L2_CLIMCAPS_V2.to.V2.1_Mapping.pdf",
-                    "description": "Mapping of data variables from v2 CLIMCAPS to V2.1 CLIMCAPS PLEV_CPS",
                     "@type": "dcat:Distribution",
+                    "description": "Mapping of data variables from v2 CLIMCAPS to V2.1 CLIMCAPS PLEV_CPS",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Sounder/L2_CLIMCAPS_V2.to.V2.1_Mapping.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's product usage"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Sounder/CLIMCAPS.PLEV.CPS.V2.1.ATBD.pdf",
-                    "description": "CLIMCAPS ATBD",
                     "@type": "dcat:Distribution",
+                    "description": "CLIMCAPS ATBD",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Sounder/CLIMCAPS.PLEV.CPS.V2.1.ATBD.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's algorithm theoretical basis document"
                 }
             ],
+            "graphic-preview-description": "Sample plot of CLIMCAPS Level 2 Pressure Level product.",
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/SNDRAQIL2PLEVCPS_2.1.png",
+            "identifier": "C2791411861-GES_DISC",
+            "issued": "2002-08-31",
+            "keyword": [
+                "air quality",
+                "atmospheric chemistry",
+                "atmospheric temperature",
+                "atmospheric water vapor",
+                "atmosphere",
+                "altitude",
+                "clouds",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/2UUZUX6GJ49C",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2024-12-01",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Not provided"
+            },
+            "references": [
+                "https://doi.org/DOI  10.3390/rs11101227",
+                "https://doi.org/10.1109/TGRS.2012.2220369",
+                "https://doi.org/10.1016/S0022-4073(97)00169-6",
+                "https://doi.org/10.1109/TGRS.2002.808236",
+                "https://doi.org/10.1029/2005/JD007020",
+                "https://doi.org/10.5194/amt-13-4437-2020"
+            ],
+            "release-place": "Greenbelt, MD, USA",
+            "series-name": "SNDRAQIL2PLEVCPS",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2002-08-31T00:00:00Z/2024-12-30T00:00:00Z",
             "theme": [
                 "Aqua",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Sounder SIPS: AQUA AIRS IR-only Level 2: Atmospheric state at Standard Pressure Levels derived from CLIMCAPS V2.1 (SNDRAQIL2PLEVCPS) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ASDCDAAC/NARSTO/0051",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2003-10-09. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/ASDCDAAC/NARSTO/0051.",
-            "issued": "2011-09-07",
-            "temporal": "1999-12-17T00:00:00Z/2007-01-01T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2018-04-26",
-            "keyword": [
-                "atmosphere",
-                "earth science",
-                "aerosols"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "JUDITH, DR. CHOW",
                 "hasEmail": "mailto:judyc@dri.edu"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/LARC/SD/ASDC"
-            },
-            "identifier": "C1000000200-LARC_ASDC",
             "description": "NARSTO_EPA_SS_FRESNO_EC_PM25_FRACTION is the North American Research Strategy for Tropospheric Ozone (NARSTO) Environmental Protection Agency (EPA) Supersite (SS) Fresno, Elemental Carbon in 2.5 um Aerosol Fraction Data product. This data set contains the measurements taken with a single and dual wavelength aethalometer. The single wavelength aethalometer (model AE14) was operated at the Fresno supersite from December 17, 1999 to September 27, 2002. This instrument used a broad spectrum incandescent lamp to illuminate the collected aerosol. Aerosol samples were collected for five minute periods. The air sample was collected through a sharp cut size-selective cyclone to limit the size of particles to aerodynamic diameters of 2.5 m or less. A single concentration of black carbon was determined for each five minute period. A dual-wavelength aethalometer (model AE21) operated at the Fresno supersite from February 25, 2003 to December 31, 2006. The collected aerosol sample is illuminated with light from two light emitting diodes at wavelengths of 370 and 880 nm. Aerosol samples are collected for five minute periods. The air sample is collected through a sharp cut size-selective cyclone to limit the size of particles to aerodynamic diameters of 2.5 m or less. The concentration of black carbon corresponds to the 880 nm measurement. The black carbon equivalent at the ultraviolet wavelength was also determined.\r\n\r\nThe Fresno Supersite is one of several Supersites established in urban areas within the United States by the EPA to better understand the measurement, sources, and health effects of suspended particulate matter (PM). The site is located at 3425 First Street, approximately 1 km north of the downtown commercial district. First Street was a four-lane artery with moderate traffic levels. Commercial establishments, office buildings, churches, and schools were located north and south of the monitor. Medium-density single-family homes and some apartments were located in the blocks to the east and west of First Street. The Fresno Supersite began operation in May of 1999.The EPA PM Supersites Program was an ambient air monitoring research program designed to provide information of value to the atmospheric sciences, and human health and exposure research communities. \r\n\r\nEight geographically diverse projects were chosen to specifically address the following EPA research priorities: (1) to characterize PM, its constituents, precursors, co-pollutants, atmospheric transport, and its source categories that affect the PM in any region; (2) to address the research questions and scientific uncertainties about PM source-receptor and exposure-health effects relationships; and (3) to compare and evaluate different methods of characterizing PM including testing new and emerging measurement methods.\r\n\r\nNARSTO, which has since disbanded, was a public/private partnership, whose membership spanned across government, utilities, industry, and academe throughout Mexico, the United States, and Canada. The primary mission was to coordinate and enhance policy-relevant scientific research and assessment of tropospheric pollution behavior; activities provide input for science-based decision-making and determination of workable, efficient, and effective strategies for local and regional air-pollution management. Data products from local, regional, and international monitoring and research programs are still available.",
-            "title": "NARSTO EPA Supersite (SS) Fresno, Elemental Carbon in 2.5 um Aerosol Fraction Data",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDCDAAC%2FNARSTO%2F0051",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDCDAAC%2FNARSTO%2F0051",
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
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1000000200-LARC_ASDC",
-                    "description": "Earthdata Search for NARSTO_EPA_SS_FRESNO_EC_PM25_FRACTION_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for NARSTO_EPA_SS_FRESNO_EC_PM25_FRACTION_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1000000200-LARC_ASDC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/ASDCDAAC/NARSTO/0051",
-                    "description": "DOI data set landing page for NARSTO_EPA_SS_FRESNO_EC_PM25_FRACTION_1",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for NARSTO_EPA_SS_FRESNO_EC_PM25_FRACTION_1",
+                    "downloadURL": "https://doi.org/10.5067/ASDCDAAC/NARSTO/0051",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/narsto/guide/narsto_epa_ss_fresno_ec_pm25_fraction.pdf",
-                    "description": "Guide for NARSTO EPA_SS_FRESNO Elemental Carbon in 2.5 um Aerosol Fraction",
                     "@type": "dcat:Distribution",
+                    "description": "Guide for NARSTO EPA_SS_FRESNO Elemental Carbon in 2.5 um Aerosol Fraction",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/narsto/guide/narsto_epa_ss_fresno_ec_pm25_fraction.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/narsto/readme/EPA_SS_Fresno_Final_Report.pdf",
-                    "description": "Fresno Supersite Final Report - March 31, 2005",
                     "@type": "dcat:Distribution",
+                    "description": "Fresno Supersite Final Report - March 31, 2005",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/narsto/readme/EPA_SS_Fresno_Final_Report.pdf",
+                    "mediaType": "application/pdf",
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
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/NARSTO/EPA_SS_FRESNO_EC_PM25_FRACTION_1/",
-                    "description": "ASDC Direct Data Download for NARSTO_EPA_SS_FRESNO_EC_PM25_FRACTION_1",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for NARSTO_EPA_SS_FRESNO_EC_PM25_FRACTION_1",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/NARSTO/EPA_SS_FRESNO_EC_PM25_FRACTION_1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 }
             ],
+            "identifier": "C1000000200-LARC_ASDC",
+            "issued": "2011-09-07",
+            "keyword": [
+                "atmosphere",
+                "earth science",
+                "aerosols"
+            ],
+            "landingPage": "https://doi.org/10.5067/ASDCDAAC/NARSTO/0051",
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
             "spatial": "36.78 -119.77",
+            "temporal": "1999-12-17T00:00:00Z/2007-01-01T23:59:59.999Z",
             "theme": [
                 "NARSTO",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "NARSTO EPA Supersite (SS) Fresno, Elemental Carbon in 2.5 um Aerosol Fraction Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-5-DDR-DERIVED-LIGHTCURVE-V3.0",
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
+            "description": "This is a compilation of published lightcurve results up through 20 October, 1997. This compilation is maintained by Alan Harris, JPL.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-5-ddr-derived-lightcurve-v3.0_rvxa-ugap",
+            "issued": "2018-06-26",
+            "keyword": [
+                "support archives",
+                "asteroid"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-5-DDR-DERIVED-LIGHTCURVE-V3.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-5-ddr-derived-lightcurve-v3.0_rvxa-ugap",
-            "description": "This is a compilation of published lightcurve results up through 20 October, 1997. This compilation is maintained by Alan Harris, JPL.",
-            "title": "ASTEROID LIGHTCURVE DERIVED DATA V3.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "ASTEROID LIGHTCURVE DERIVED DATA V3.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/758",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Korontzi, S., D.P. Roy, and C.O. Justice. 2004. SAFARI 2000 Emissions Estimates, MODIS Burned Area Product, Dry Season 2000. ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/758",
-            "issued": "2023-10-18",
-            "temporal": "2000-08-31T00:00:00Z/2000-09-30T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-10-24",
-            "keyword": [
-                "ecosystems",
-                "ecological dynamics",
-                "earth science",
-                "national geospatial data asset",
-                "biosphere",
-                "atmospheric chemistry",
-                "atmosphere",
-                "natural hazards",
-                "ngda",
-                "surface radiative properties",
-                "vegetation",
-                "land surface",
-                "human dimensions",
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
-            "identifier": "C2789036254-ORNL_CLOUD",
             "description": "The recently generated MODIS burned area product over southern Africa for the month of September 2000 was used to calculate regional biomass burning emissions from grassland and woodland fires for a number of trace gases and particulates at 1 km spatial resolution. A dynamic regional fuel load model developed for southern Africa in support of SAFARI 2000 fire emissions modeling is used to compute spatially explicit southern Africa fuel load data.",
-            "graphic-preview-description": "Browse Image",
-            "title": "SAFARI 2000 Emissions Estimates, MODIS Burned Area Product, Dry Season 2000",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/safari_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F758",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F758",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/safari2k/remote_sensing/MODIS_emissions/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/safari2k/remote_sensing/MODIS_emissions/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/S2K/guides/modis_emissions.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/S2K/guides/modis_emissions.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/758",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/758",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/safari2k/remote_sensing/MODIS_emissions/comp/modis_emissions_readme.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/safari2k/remote_sensing/MODIS_emissions/comp/modis_emissions_readme.pdf",
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
+            "identifier": "C2789036254-ORNL_CLOUD",
+            "issued": "2023-10-18",
+            "keyword": [
+                "ecosystems",
+                "ecological dynamics",
+                "earth science",
+                "national geospatial data asset",
+                "biosphere",
+                "atmospheric chemistry",
+                "atmosphere",
+                "natural hazards",
+                "ngda",
+                "surface radiative properties",
+                "vegetation",
+                "land surface",
+                "human dimensions",
+                "environmental impacts"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/758",
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
             "spatial": "9.67 -34.14 46.65 0.34",
+            "temporal": "2000-08-31T00:00:00Z/2000-09-30T23:59:59Z",
             "theme": [
                 "SAFARI 2000",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "SAFARI 2000 Emissions Estimates, MODIS Burned Area Product, Dry Season 2000"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C2652675386-OB_DAAC.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/GSFC/SED/ESD/GCDC/OB.DAAC.",
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
-            "identifier": "C2652675386-OB_DAAC",
             "description": "The Ocean Biology DAAC produces near real-time (quicklook) products using the best-available combination of ancillary data from meteorological and ozone data. As such, the inputs and the calibration used are less than optimal. Quicklook products provide a snapshot of the data during a short time period within a single orbit.",
-            "title": "NOAA-21 VIIRS Global Mapped Particulate Organic Carbon (POC) - Near Real Time (NRT) Data, version R2022.0",
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
-                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/data/10.5067/NOAA21/VIIRS/L3M/POC/2022",
-                    "description": "VIIRS-NOAA-21 L3M Particulate Organic Carbon (POC) - Near Real Time (NRT) Dataset Landing Page",
                     "@type": "dcat:Distribution",
+                    "description": "VIIRS-NOAA-21 L3M Particulate Organic Carbon (POC) - Near Real Time (NRT) Dataset Landing Page",
+                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/data/10.5067/NOAA21/VIIRS/L3M/POC/2022",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://oceandata.sci.gsfc.nasa.gov/opendap/VIIRSJ2/L3SMI/",
-                    "description": "OB.DAAC OPeNDAP Site for NOAA-21 VIIRS Standard Mapped Image (SMI) Product",
                     "@type": "dcat:Distribution",
+                    "description": "OB.DAAC OPeNDAP Site for NOAA-21 VIIRS Standard Mapped Image (SMI) Product",
+                    "downloadURL": "https://oceandata.sci.gsfc.nasa.gov/opendap/VIIRSJ2/L3SMI/",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 }
             ],
+            "identifier": "C2652675386-OB_DAAC",
+            "issued": "2023-04-04",
+            "keyword": [
+                "earth science",
+                "ocean chemistry",
+                "oceans"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C2652675386-OB_DAAC.html",
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
+            "title": "NOAA-21 VIIRS Global Mapped Particulate Organic Carbon (POC) - Near Real Time (NRT) Data, version R2022.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=CH1-ORB-L-MRFFR-5-CDR-MOSAIC-V1.0",
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
-                "chandrayaan-1",
-                "moon"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This data set contains lunar polar mosaics composed of calibrated data acquired from the Mini-RF (Mini-SAR) Forerunner instrument during the Chandrayaan-1 mission. The mosaics are made from data collected during multiple orbits.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ch1-orb-l-mrffr-5-cdr-mosaic-v1.0_rw3m-dc8i",
+            "issued": "2018-06-26",
+            "keyword": [
+                "chandrayaan-1",
+                "moon"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=CH1-ORB-L-MRFFR-5-CDR-MOSAIC-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ch1-orb-l-mrffr-5-cdr-mosaic-v1.0_rw3m-dc8i",
-            "description": "This data set contains lunar polar mosaics composed of calibrated data acquired from the Mini-RF (Mini-SAR) Forerunner instrument during the Chandrayaan-1 mission. The mosaics are made from data collected during multiple orbits.",
-            "title": "CH1-ORB MOON MINI-RF 5 POLAR MOSAIC CALIBRATED DATA REC V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "CH1-ORB MOON MINI-RF 5 POLAR MOSAIC CALIBRATED DATA REC V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.7265/N58C9T60",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Former Soviet Union Hydrological Snow Surveys, 1966-1996, Version 1. Version 1. Archived by National Aeronautics and Space Administration, U.S. Government, National Snow and Ice Data Center. https://doi.org/10.7265/N58C9T60.",
-            "issued": "1966-01-10",
-            "temporal": "1966-01-10T00:00:00Z/1996-12-31T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "1996-12-31",
-            "keyword": [
-                "terrestrial hydrosphere",
-                "cryosphere",
-                "earth science",
-                "snow/ice"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Richard Armstrong",
                 "hasEmail": "mailto:rlax@nsidc.org"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NSIDC"
-            },
-            "identifier": "C1386246234-NSIDCV0",
             "description": "The Former Soviet Union Hydrological Snow Surveys are based on observations made by personnel at 1,345 sites throughout the Former Soviet Union between 1966 and 1990, and over 200 of those sites between 1991 and 1996. These observations include snow depths at World Meteorological Organization (WMO) stations and snow depth and snow water equivalent measured over a nearby snow course transect. The station snow depth measurements are a ten-day average of individual snow depth measurements. The transect snow depth data are the spatial average of 100 to 200 individual measuring points. The transect snow water equivalent is the spatial average of 20 individual measuring points. Data were acquired from the Institute of Geography, Russian Academy of Sciences Moscow, and data were digitized in Russia under the supervision of Professor Alexander Krenke.",
-            "title": "Former Soviet Union Hydrological Snow Surveys, 1966-1996, Version 1",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.7265%2FN58C9T60",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.7265%2FN58C9T60",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/forms/G01170_or.html?major_version=1",
-                    "description": "Direct download, with optional registration page.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download, with optional registration page.",
+                    "downloadURL": "https://nsidc.org/forms/G01170_or.html?major_version=1",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.7265/N58C9T60",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.7265/N58C9T60",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.7265/N58C9T60",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.7265/N58C9T60",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C1386246234-NSIDCV0",
+            "issued": "1966-01-10",
+            "keyword": [
+                "terrestrial hydrosphere",
+                "cryosphere",
+                "earth science",
+                "snow/ice"
+            ],
+            "landingPage": "https://doi.org/10.7265/N58C9T60",
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
             "spatial": "30.0 35.0 180.0 80.0",
+            "temporal": "1966-01-10T00:00:00Z/1996-12-31T23:59:59.999Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Former Soviet Union Hydrological Snow Surveys, 1966-1996, Version 1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/3C1Y3EJB1E7Q",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Kevin Bowman. 2017-09-01. CMSFluxFire. Version 1. Carbon Monitoring System Carbon Flux for Fire L4 V1. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/3C1Y3EJB1E7Q. https://disc.gsfc.nasa.gov/datacollection/CMSFluxFire_1.html.",
-            "issued": "2017-04-26",
-            "temporal": "2010-01-01T00:00:00Z/2013-01-01T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2017-08-18",
-            "keyword": [
-                "oceans",
-                "ocean chemistry",
-                "earth science",
-                "atmospheric chemistry",
-                "atmosphere"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Kevin Bowman",
                 "hasEmail": "mailto:kevin.w.bowman@jpl.nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
-            "identifier": "C1424798922-GES_DISC",
-            "description": "This dataset provides the Carbon Flux for Fires.\n\nThe NASA Carbon Monitoring System (CMS) is designed to make significant contributions in characterizing, quantifying, understanding, and predicting the evolution of global carbon sources and sinks through improved monitoring of carbon stocks and fluxes. The System will use the full range of NASA satellite observations and modeling/analysis capabilities to establish the accuracy, quantitative uncertainties, and utility of products for supporting national and international policy, regulatory, and management activities. CMS will maintain a global emphasis while providing finer scale regional information, utilizing space-based and surface-based data and will rapidly initiate generation and distribution of products both for user evaluation and to inform near-term policy development and planning.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "CMSFluxFire",
             "creator": "Kevin Bowman",
-            "title": "Carbon Monitoring System Carbon Flux for Fire L4 V1 (CMSFluxFire) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/CMS/CMSFluxFire.png",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "This dataset provides the Carbon Flux for Fires.\n\nThe NASA Carbon Monitoring System (CMS) is designed to make significant contributions in characterizing, quantifying, understanding, and predicting the evolution of global carbon sources and sinks through improved monitoring of carbon stocks and fluxes. The System will use the full range of NASA satellite observations and modeling/analysis capabilities to establish the accuracy, quantitative uncertainties, and utility of products for supporting national and international policy, regulatory, and management activities. CMS will maintain a global emphasis while providing finer scale regional information, utilizing space-based and surface-based data and will rapidly initiate generation and distribution of products both for user evaluation and to inform near-term policy development and planning.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2F3C1Y3EJB1E7Q",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2F3C1Y3EJB1E7Q",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
@@ -1329590,91 +1329566,93 @@
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/CMSFluxFire_1.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/CMSFluxFire_1.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://acdisc.gsfc.nasa.gov/data/CMS/CMSFluxFire.1/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://acdisc.gsfc.nasa.gov/data/CMS/CMSFluxFire.1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://acdisc.gsfc.nasa.gov/opendap/CMS/CMSFluxFire.1/",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://acdisc.gsfc.nasa.gov/opendap/CMS/CMSFluxFire.1/",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://acdisc.gsfc.nasa.gov/data/CMS/CMSFluxFire.1/doc/README.CMS_Flux_V1.pdf",
-                    "description": "README Document",
                     "@type": "dcat:Distribution",
+                    "description": "README Document",
+                    "downloadURL": "https://acdisc.gsfc.nasa.gov/data/CMS/CMSFluxFire.1/doc/README.CMS_Flux_V1.pdf",
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
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=CMSFluxFire",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=CMSFluxFire",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 }
             ],
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/CMS/CMSFluxFire.png",
+            "identifier": "C1424798922-GES_DISC",
+            "issued": "2017-04-26",
+            "keyword": [
+                "oceans",
+                "ocean chemistry",
+                "earth science",
+                "atmospheric chemistry",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.5067/3C1Y3EJB1E7Q",
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
+            "series-name": "CMSFluxFire",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2010-01-01T00:00:00Z/2013-01-01T23:59:59.999Z",
             "theme": [
                 "CMS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Carbon Monitoring System Carbon Flux for Fire L4 V1 (CMSFluxFire) at GES DISC"
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
-                "models",
-                "incompressible",
-                "cases",
-                "turbulence",
-                "flow"
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
-            "identifier": "NASA-842__26",
             "description": "This grouping contains the incompressible-flow cases from the 1980-81 Data Library.",
-            "title": "Collaborative Testing of Turbulence Models: Incompressible Flow Cases from 1980-81 Data Library",
-            "programCode": [
-                "026:023"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -1329682,258 +1329660,260 @@
                     "mediaType": "application/x-compressed"
                 }
             ],
-            "accrualPeriodicity": "irregular",
+            "identifier": "NASA-842__26",
+            "issued": "2018-06-25",
+            "keyword": [
+                "models",
+                "incompressible",
+                "cases",
+                "turbulence",
+                "flow"
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
-            "landingPage": "https://doi.org/10.5067/MODIS/N11_AVH02C1.006",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "The Long-Term Data Record (LTDR) project. 2023-07-25. NOAA-11 AVHRR Top-of-Atmosphere Reflectance Daily L3 Global 0.05 Deg. CMG. Version 6. MODAPS at NASA/GSFC. Archived by National Aeronautics and Space Administration, U.S. Government, L1 and Atmosphere Archive and Distribution System (LAADS). https://doi.org/10.5067/MODIS/N11_AVH02C1.006.",
-            "issued": "2022-07-21",
-            "temporal": "1988-11-08T00:00:00Z/1995-01-01T23:59:59.900Z",
-            "@type": "dcat:Dataset",
-            "modified": "1995-01-01",
-            "keyword": [
-                "infrared wavelengths",
-                "earth science",
-                "atmospheric radiation",
-                "atmosphere",
-                "surface radiative properties",
-                "spectral/engineering",
-                "land surface"
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
-            "identifier": "C2738327749-LAADS",
-            "description": "The Long-Term Data Record (LTDR) produces, validates, and distributes a global land surface climate data record (CDR) that uses both mature and well-tested algorithms in concert with the best-available polar-orbiting satellite data from past to the present.   The CDR is critically important to studying global climate change.  The LTDR project is unique in that it serves as a bridge that connects data derived from the NOAA Advanced Very High Resolution Radiometer (AVHRR), the EOS Moderate resolution Imaging Spectroradiometer (MODIS), the Suomi National Polar-orbiting Partnership (SNPP) Visible Infrared Imaging Radiometer Suite (VIIRS), and Joint Polar Satellite System (JPSS) VIIRS missions.  The LTDR draws from the following eight AVHRR missions: \r\nNOAA-7, NOAA-9, NOAA-11, NOAA-14, NOAA-16, NOAA-18, NOAA-19, and MetOp-B.\r\nCurrently, the project generates a daily surface reflectance product as the fundamental climate data record (FCDR) and derives daily Normalized Differential Vegetation Index (NDVI) and Leaf-Area Index/fraction of absorbed Photosynthetically Active Radiation (LAI/fPAR) as two thematic CDRs (TCDR).  LAI/fPAR was developed as an experimental product.\r\n\r\nThe  NOAA-11 AVHRR Top-of-Atmosphere Reflectance Daily L3 Global 0.05 Deg. CMG, short-name N11_AVH02C1 is generated from GIMMS Advanced Processing System (GAPS) BRDF-corrected Surface Reflectance product (AVH01C1). The N11_AVH02C1 consist of Top-of-atmosphere reflectance for bands 1 and 2, data Quality flags, angles (solar zenith, view zenith, and relative azimuth), thermal data (thermal bands 3, 4 and 5), and additional data (scan time).",
-            "release-place": "MODAPS at NASA/GSFC",
             "creator": "The Long-Term Data Record (LTDR) project",
-            "title": "NOAA-11 AVHRR Top-of-Atmosphere Reflectance Daily L3 Global 0.05 Deg. CMG",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The Long-Term Data Record (LTDR) produces, validates, and distributes a global land surface climate data record (CDR) that uses both mature and well-tested algorithms in concert with the best-available polar-orbiting satellite data from past to the present.   The CDR is critically important to studying global climate change.  The LTDR project is unique in that it serves as a bridge that connects data derived from the NOAA Advanced Very High Resolution Radiometer (AVHRR), the EOS Moderate resolution Imaging Spectroradiometer (MODIS), the Suomi National Polar-orbiting Partnership (SNPP) Visible Infrared Imaging Radiometer Suite (VIIRS), and Joint Polar Satellite System (JPSS) VIIRS missions.  The LTDR draws from the following eight AVHRR missions: \r\nNOAA-7, NOAA-9, NOAA-11, NOAA-14, NOAA-16, NOAA-18, NOAA-19, and MetOp-B.\r\nCurrently, the project generates a daily surface reflectance product as the fundamental climate data record (FCDR) and derives daily Normalized Differential Vegetation Index (NDVI) and Leaf-Area Index/fraction of absorbed Photosynthetically Active Radiation (LAI/fPAR) as two thematic CDRs (TCDR).  LAI/fPAR was developed as an experimental product.\r\n\r\nThe  NOAA-11 AVHRR Top-of-Atmosphere Reflectance Daily L3 Global 0.05 Deg. CMG, short-name N11_AVH02C1 is generated from GIMMS Advanced Processing System (GAPS) BRDF-corrected Surface Reflectance product (AVH01C1). The N11_AVH02C1 consist of Top-of-atmosphere reflectance for bands 1 and 2, data Quality flags, angles (solar zenith, view zenith, and relative azimuth), thermal data (thermal bands 3, 4 and 5), and additional data (scan time).",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMODIS%2FN11_AVH02C1.006",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMODIS%2FN11_AVH02C1.006",
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
-                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/search/order/1/N11_AVH02C1--466",
-                    "description": "Search and order products from LAADS website.",
                     "@type": "dcat:Distribution",
+                    "description": "Search and order products from LAADS website.",
+                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/search/order/1/N11_AVH02C1--466",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through LAADS"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/archive/allData/466/N11_AVH02C1/",
-                    "description": "Direct access to C6 N11_AVH02C1 data set.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct access to C6 N11_AVH02C1 data set.",
+                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/archive/allData/466/N11_AVH02C1/",
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
+            "identifier": "C2738327749-LAADS",
+            "issued": "2022-07-21",
+            "keyword": [
+                "infrared wavelengths",
+                "earth science",
+                "atmospheric radiation",
+                "atmosphere",
+                "surface radiative properties",
+                "spectral/engineering",
+                "land surface"
+            ],
+            "landingPage": "https://doi.org/10.5067/MODIS/N11_AVH02C1.006",
+            "language": [
+                "en-US"
+            ],
+            "modified": "1995-01-01",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Not provided"
+            },
+            "release-place": "MODAPS at NASA/GSFC",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "1988-11-08T00:00:00Z/1995-01-01T23:59:59.900Z",
             "theme": [
                 "NOAA - SPACE WEATHER PROGRAM",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "NOAA-11 AVHRR Top-of-Atmosphere Reflectance Daily L3 Global 0.05 Deg. CMG"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewBundle.jsp?identifier=urn%3Anasa%3Apds%3Acompil.ast.magnitude-slope&version=1.0",
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
+            "description": "Absolute magnitudes and slopes, mostly   IAU-adopted with exceptions noted, for all asteroids numbered as of    the 2008 April 20 batch of Minor Planet Circulars.",
+            "identifier": "urn:nasa:pds:compil.ast.magnitude-slope",
+            "issued": "2021-05-21",
+            "keyword": [
+                "none",
+                "multiple asteroids"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewBundle.jsp?identifier=urn%3Anasa%3Apds%3Acompil.ast.magnitude-slope&version=1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:compil.ast.magnitude-slope",
-            "description": "Absolute magnitudes and slopes, mostly   IAU-adopted with exceptions noted, for all asteroids numbered as of    the 2008 April 20 batch of Minor Planet Circulars.",
-            "title": "ASTEROID ABSOLUTE MAGNITUDES",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ASTEROID ABSOLUTE MAGNITUDES"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/SeaBASS/NSF-BWZ/DATA001",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/GSFC/SED/ESD/GCDC/OB.DAAC. https://doi.org/10.5067/SeaBASS/NSF-BWZ/DATA001.",
-            "issued": "2004-02-15",
-            "temporal": "2004-02-15T00:00:02Z/2023-04-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-04-06",
-            "keyword": [
-                "ocean chemistry",
-                "earth science",
-                "ocean temperature",
-                "oceans",
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
-            "identifier": "C1633360531-OB_DAAC",
             "description": "Measurements taken in the Blue Water Zone (BWZ) under NSF funding near Antarctica and Drakes Passage in 2004 to 2006.",
-            "title": "National Science Foundation (NSF)-Blue Water Zone (BWZ) measurements",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSeaBASS%2FNSF-BWZ%2FDATA001",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSeaBASS%2FNSF-BWZ%2FDATA001",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://seabass.gsfc.nasa.gov/experiment/NSF-BWZ/",
-                    "description": "Detailed information about the SeaBASS Experiment such as cruises, funding, and investigators",
                     "@type": "dcat:Distribution",
+                    "description": "Detailed information about the SeaBASS Experiment such as cruises, funding, and investigators",
+                    "downloadURL": "https://seabass.gsfc.nasa.gov/experiment/NSF-BWZ/",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 }
             ],
+            "identifier": "C1633360531-OB_DAAC",
+            "issued": "2004-02-15",
+            "keyword": [
+                "ocean chemistry",
+                "earth science",
+                "ocean temperature",
+                "oceans",
+                "ocean optics",
+                "salinity/density"
+            ],
+            "landingPage": "https://doi.org/10.5067/SeaBASS/NSF-BWZ/DATA001",
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
+            "temporal": "2004-02-15T00:00:02Z/2023-04-17T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "National Science Foundation (NSF)-Blue Water Zone (BWZ) measurements"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-4-ESC3-67PCHURYUMOV-M20-V2.0",
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
+            "description": "This CODMAC level 4 data set contains radiometric calibrated and geometric distortion corrected (resampled) image data in W/m^2/sr/nm, acquired by the OSIRIS Wide Angle Camera on the Rosetta spacecraft during the COMET ESCORT 3 mission phase, covering the period from 2015-08-25T23:25:00.000 to 2015-09-22T23:24:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V2.0 supersedes previous deliveries of the same dataset with the following changes since the last version: Lien corrected dataset after October 2018 PSA/PDS external peer review. Updated documentation and ancillary files, added document on bandpass filter. Updated SCIENCE_USER_GUIDE_V03.PDF to include one section about FAQ and one section about image data quality. Added shutter backtravel and readout issues to image quality map. Updated DATA_QUALITY_ID keyword in image header. Improved handling of images with missing packets.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-4-esc3-67pchuryumov-m20-v2.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-4-ESC3-67PCHURYUMOV-M20-V2.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-4-esc3-67pchuryumov-m20-v2.0",
-            "description": "This CODMAC level 4 data set contains radiometric calibrated and geometric distortion corrected (resampled) image data in W/m^2/sr/nm, acquired by the OSIRIS Wide Angle Camera on the Rosetta spacecraft during the COMET ESCORT 3 mission phase, covering the period from 2015-08-25T23:25:00.000 to 2015-09-22T23:24:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V2.0 supersedes previous deliveries of the same dataset with the following changes since the last version: Lien corrected dataset after October 2018 PSA/PDS external peer review. Updated documentation and ancillary files, added document on bandpass filter. Updated SCIENCE_USER_GUIDE_V03.PDF to include one section about FAQ and one section about image data quality. Added shutter backtravel and readout issues to image quality map. Updated DATA_QUALITY_ID keyword in image header. Improved handling of images with missing packets.",
-            "title": "ROSETTA-ORBITER 67P OSIWAC 4 ESC3-MTP020 RDR V2.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P OSIWAC 4 ESC3-MTP020 RDR V2.0"
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
-                "data",
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
-            "identifier": "NASA-456",
             "description": "Data dictionary and index files version 1r91.",
-            "title": "PDS Data Dictionary (1r91)",
-            "programCode": [
-                "026:005"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -1329941,1124 +1329921,1146 @@
                     "mediaType": "application/html"
                 }
             ],
-            "accrualPeriodicity": "irregular",
+            "identifier": "NASA-456",
+            "issued": "2018-06-25",
+            "keyword": [
+                "data",
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
+            "title": "PDS Data Dictionary (1r91)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=LCROSS-X-NSP2-3-CAL-V1.0",
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
-                "lunar crater observation and sensing satellite",
-                "sun"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "Calibrated spectra from the Near Infrared Spectrometer 2 (NSP2) aboard the Lunar Crater Observation and Sensing Satellite (LCROSS).",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.lcross-x-nsp2-3-cal-v1.0_rwgi-xbmj",
+            "issued": "2021-05-21",
+            "keyword": [
+                "lunar crater observation and sensing satellite",
+                "sun"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=LCROSS-X-NSP2-3-CAL-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.lcross-x-nsp2-3-cal-v1.0_rwgi-xbmj",
-            "description": "Calibrated spectra from the Near Infrared Spectrometer 2 (NSP2) aboard the Lunar Crater Observation and Sensing Satellite (LCROSS).",
-            "title": "LCROSS SUN 2ND NEAR IR SPECTROMETER 3 CAL V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "LCROSS SUN 2ND NEAR IR SPECTROMETER 3 CAL V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MER1-M-NAVCAM-5-SOLAR-OPS-V1.0",
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
+            "description": "not applicable",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mer1-m-navcam-5-solar-ops-v1.0_rwhu-x248",
+            "issued": "2021-05-21",
+            "keyword": [
+                "mars",
+                "mars exploration rover"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MER1-M-NAVCAM-5-SOLAR-OPS-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mer1-m-navcam-5-solar-ops-v1.0_rwhu-x248",
-            "description": "not applicable",
-            "title": "MER 1 MARS NAVIGATION CAMERA SOLAR RDR OPS V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "MER 1 MARS NAVIGATION CAMERA SOLAR RDR OPS V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://c3.nasa.gov/dashlink/resources/262/",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2010-11-17",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
-            "keyword": [
-                "nasa",
-                "dashlink",
-                "ames"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Kanishka Bhaduri",
                 "hasEmail": "mailto:kanishka.bhaduri-1@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Dashlink"
-            },
-            "identifier": "DASHLINK_262",
             "description": "This paper proposes a scalable, local privacy preserving algorithm for distributed Peer-to-Peer (P2P) data aggregation useful for many advanced data mining/analysis tasks such as average/sum computation, decision tree induction, feature selection, and more.\r\nUnlike most multi-party privacy-preserving data mining algorithms, this approach works in an asynchronous manner through local interactions and it is highly scalable. It particularly deals with the distributed computation of the sum of a set of numbers stored at different peers in a P2P network in the context of a P2P web mining application. The proposed optimization based privacy-preserving technique for computing the sum allows different peers to specify different privacy requirements without having to adhere to a global set of parameters for the chosen privacy model. Since distributed sum computation is a frequently used primitive,\r\nthe proposed approach is likely to have significant impact on many data mining tasks such as multi-party privacy-preserving clustering, frequent itemset mining, and statistical aggregate computation.",
-            "title": "Multi-objective optimization based privacy preserving distributed data mining in Peer-to-Peer networks",
-            "programCode": [
-                "026:029"
-            ],
             "distribution": [
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/publication/Multi-objective_optimization.pdf",
-                    "description": "Multi-objective optimization.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "Multi-objective optimization.pdf",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/publication/Multi-objective_optimization.pdf",
+                    "mediaType": "application/pdf",
                     "title": "Multi-objective optimization.pdf"
                 }
             ],
-            "accrualPeriodicity": "irregular"
+            "identifier": "DASHLINK_262",
+            "issued": "2010-11-17",
+            "keyword": [
+                "nasa",
+                "dashlink",
+                "ames"
+            ],
+            "landingPage": "https://c3.nasa.gov/dashlink/resources/262/",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:029"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Dashlink"
+            },
+            "title": "Multi-objective optimization based privacy preserving distributed data mining in Peer-to-Peer networks"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-X-RSI-1%2F2%2F3-CR2-0041-V1.0",
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
-                "sun",
-                "international rosetta mission"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This is a Solar Conjunction measurement covering the time 2006-04-24T00:05:04.500 to 2006-04-24T03:16:20.500.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-x-rsi-1-2-3-cr2-0041-v1.0_rwip-ykvw",
+            "issued": "2021-05-21",
+            "keyword": [
+                "sun",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-X-RSI-1%2F2%2F3-CR2-0041-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-x-rsi-1-2-3-cr2-0041-v1.0_rwip-ykvw",
-            "description": "This is a Solar Conjunction measurement covering the time 2006-04-24T00:05:04.500 to 2006-04-24T03:16:20.500.",
-            "title": "ROSETTA-ORBITER SUN RSI 1/2/3 CRUISE 2 0041 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER SUN RSI 1/2/3 CRUISE 2 0041 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MEX-M-MRS-1%2F2%2F3-EXT3-3408-V1.0",
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
+            "description": "This is a Mars Express Radio Science data set, collected during the extended mission phase 2010-01-01 to 2012-12-31. It is a Global Gravity measurement and covers the time 2012-09-23T08:35:15.000 to 2012-09-23T11:20:46.500.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mex-m-mrs-1-2-3-ext3-3408-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "mars",
+                "mars express"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MEX-M-MRS-1%2F2%2F3-EXT3-3408-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mex-m-mrs-1-2-3-ext3-3408-v1.0",
-            "description": "This is a Mars Express Radio Science data set, collected during the extended mission phase 2010-01-01 to 2012-12-31. It is a Global Gravity measurement and covers the time 2012-09-23T08:35:15.000 to 2012-09-23T11:20:46.500.",
-            "title": "MARS EXPRESS MARS MRS 1/2/3\n                                     EXTENDED MISSION 3 3408 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "MARS EXPRESS MARS MRS 1/2/3\n                                     EXTENDED MISSION 3 3408 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ASTER/AST_09XT.003",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "NASA/METI/AIST/Japan Spacesystems and U.S./Japan ASTER Science Team. 2006-10-13. AST_09XT.003.  ASTER On-Demand L2 Surface Radiance VNIR and SWIR Crosstalk-Corrected. Sioux Falls, South Dakota, USA. Archived by National Aeronautics and Space Administration, U.S. Government, NASA EOSDIS Land Processes Distributed Active Archive Center. https://doi.org/10.5067/ASTER/AST_09XT.003. https://doi.org/10.5067/ASTER/AST_09XT.003. The DOI landing page provides citations in APA and Chicago styles..",
-            "issued": "2006-10-13",
-            "temporal": "2000-03-06T00:30:05Z/2024-12-16T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-28",
-            "keyword": [
-                "infrared wavelengths",
-                "national geospatial data asset",
-                "ngda",
-                "spectral/engineering",
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
-                "name": "LP DAAC"
-            },
-            "identifier": "C1299783631-LPDAAC_ECS",
-            "description": "The ASTER Surface Radiance VNIR and Crosstalk Corrected SWIR (AST_09XT) is a multi-file product (https://lpdaac.usgs.gov/documents/996/ASTER_Earthdata_Search_Order_Instructions.pdf) that contains atmospherically corrected data for both the Visible and Near Infrared (VNIR) and Shortwave Infrared (SWIR) sensors. The crosstalk phenomenon was discovered during the nascent stage of the Terra Mission. It is whereby the incident light with band 4 caused multiple reflections for the SWIR bands, which resulted in blurred images. This has been corrected with the ASTER L2 Surface Radiance VNIR and Crosstalk Corrected SWIR data product. Each product delivery includes two Hierarchical Data Format - Earth Observing System (HDF-EOS) files: one for the VNIR, and the other for the SWIR. Both the VNIR and the SWIR data are atmospherically corrected using the corresponding bands from an (ASTER Level 1B) (https://doi.org/10.5067/ASTER/AST_L1B.003) image.\r\n\r\nASTER Level 2 data requests for observations that occurred after May 27, 2020 will resort back to using the climatology ozone input. Additional information can be found in the ASTER L2 Processing Options Update (https://lpdaac.usgs.gov/news/aster-l2-processing-options-update/).\r\n\r\nStarting June 23, 2021, radiometric calibration coefficient Version 5 (RCC V5) will be applied to newly observed ASTER data and archived ASTER data products. Details regarding RCC V5 are described in the following journal article.\r\n\r\nTsuchida, S., Yamamoto, H., Kouyama, T., Obata, K., Sakuma, F., Tachikawa, T., Kamei, A., Arai, K., Czapla-Myers, J.S., Biggar, S.F., and Thome, K.J., 2020, Radiometric Degradation Curves for the ASTER VNIR Processing Using Vicarious and Lunar Calibrations: Remote Sensing, v. 12, no. 3, at https://doi.org/10.3390/rs12030427.\r\n\r\nAs of December 15, 2021, the LP DAAC has implemented changes to ASTER PGE Version 3.4, which will affect all ASTER Level 2 on-demand products.  Changes include:\r\n\u2022\tAura Ozone Monitoring Instrument (OMI) has been added as one of the ancillary ozone inputs for any observations made after May 27, 2020.  The sequence of fallbacks for ozone will remain the same.\r\n\u2022\tToolkit has been updated from Version 5.2.17 to 5.2.20.  Users may notice minor differences between the two versions.  Differences may include minuscule changes in digital numbers around the peripheral of the granule and boundaries of a cloud for Surface Reflectance and Surface Radiance (AST07 and AST09) QA Data Plane depending on the Operating System and libraries being used by the user to process the data.\r\n\r\nAdditionally, Climatology, which is one of the inputs for Ozone and Moisture, Temperature and Pressures (MTP) will be removed from the Earthdata Order Form.  It has been observed that PGEs generated with Climatology as an input yield noticeable differences statistically during image and spectral analysis.  Climatology will continue to be used as the final default if neither of the first two selectable options are available for Ozone and MTP.  Users can check the OPERATIONALQUALITYFLAGEXPLANATION field in the metadata or the output file for atmospheric parameters that were applied.\r\n\r\nAura OMI data are no longer available as an input for ASTER Level 2 data acquisitions after October 6, 2023. For data acquired after this date, ozone inputs will automatically fall back to climatology ozone inputs when Aura OMI is selected as an input. For more details, please refer to the Discontinuation of Aura OMI as an Input news announcement (https://lpdaac.usgs.gov/news/discontinuation-of-aura-omi-as-an-ancillary-ozone-input-for-aster-products/).",
-            "release-place": "Sioux Falls, South Dakota, USA",
-            "series-name": "AST_09XT.003",
-            "graphic-preview-description": "Browse image for Earthdata Search",
             "creator": "NASA/METI/AIST/Japan Spacesystems and U.S./Japan ASTER Science Team",
-            "title": "ASTER L2 Surface Radiance - VNIR and Crosstalk Corrected SWIR V003",
-            "graphic-preview-file": "https://e4ftl01.cr.usgs.gov/WORKING/BRWS/Browse.001/2020.11.18/pg-BR1A0000-2020111801_006_012.1.VNIR.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The ASTER Surface Radiance VNIR and Crosstalk Corrected SWIR (AST_09XT) is a multi-file product (https://lpdaac.usgs.gov/documents/996/ASTER_Earthdata_Search_Order_Instructions.pdf) that contains atmospherically corrected data for both the Visible and Near Infrared (VNIR) and Shortwave Infrared (SWIR) sensors. The crosstalk phenomenon was discovered during the nascent stage of the Terra Mission. It is whereby the incident light with band 4 caused multiple reflections for the SWIR bands, which resulted in blurred images. This has been corrected with the ASTER L2 Surface Radiance VNIR and Crosstalk Corrected SWIR data product. Each product delivery includes two Hierarchical Data Format - Earth Observing System (HDF-EOS) files: one for the VNIR, and the other for the SWIR. Both the VNIR and the SWIR data are atmospherically corrected using the corresponding bands from an (ASTER Level 1B) (https://doi.org/10.5067/ASTER/AST_L1B.003) image.\r\n\r\nASTER Level 2 data requests for observations that occurred after May 27, 2020 will resort back to using the climatology ozone input. Additional information can be found in the ASTER L2 Processing Options Update (https://lpdaac.usgs.gov/news/aster-l2-processing-options-update/).\r\n\r\nStarting June 23, 2021, radiometric calibration coefficient Version 5 (RCC V5) will be applied to newly observed ASTER data and archived ASTER data products. Details regarding RCC V5 are described in the following journal article.\r\n\r\nTsuchida, S., Yamamoto, H., Kouyama, T., Obata, K., Sakuma, F., Tachikawa, T., Kamei, A., Arai, K., Czapla-Myers, J.S., Biggar, S.F., and Thome, K.J., 2020, Radiometric Degradation Curves for the ASTER VNIR Processing Using Vicarious and Lunar Calibrations: Remote Sensing, v. 12, no. 3, at https://doi.org/10.3390/rs12030427.\r\n\r\nAs of December 15, 2021, the LP DAAC has implemented changes to ASTER PGE Version 3.4, which will affect all ASTER Level 2 on-demand products.  Changes include:\r\n\u2022\tAura Ozone Monitoring Instrument (OMI) has been added as one of the ancillary ozone inputs for any observations made after May 27, 2020.  The sequence of fallbacks for ozone will remain the same.\r\n\u2022\tToolkit has been updated from Version 5.2.17 to 5.2.20.  Users may notice minor differences between the two versions.  Differences may include minuscule changes in digital numbers around the peripheral of the granule and boundaries of a cloud for Surface Reflectance and Surface Radiance (AST07 and AST09) QA Data Plane depending on the Operating System and libraries being used by the user to process the data.\r\n\r\nAdditionally, Climatology, which is one of the inputs for Ozone and Moisture, Temperature and Pressures (MTP) will be removed from the Earthdata Order Form.  It has been observed that PGEs generated with Climatology as an input yield noticeable differences statistically during image and spectral analysis.  Climatology will continue to be used as the final default if neither of the first two selectable options are available for Ozone and MTP.  Users can check the OPERATIONALQUALITYFLAGEXPLANATION field in the metadata or the output file for atmospheric parameters that were applied.\r\n\r\nAura OMI data are no longer available as an input for ASTER Level 2 data acquisitions after October 6, 2023. For data acquired after this date, ozone inputs will automatically fall back to climatology ozone inputs when Aura OMI is selected as an input. For more details, please refer to the Discontinuation of Aura OMI as an Input news announcement (https://lpdaac.usgs.gov/news/discontinuation-of-aura-omi-as-an-ancillary-ozone-input-for-aster-products/).",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASTER%2FAST_09XT.003",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASTER%2FAST_09XT.003",
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
-                    "downloadURL": "https://doi.org/10.5067/ASTER/AST_09XT.003",
-                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
+                    "downloadURL": "https://doi.org/10.5067/ASTER/AST_09XT.003",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/x-hdf",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=C1299783631-LPDAAC_ECS",
-                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=C1299783631-LPDAAC_ECS",
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
                     "title": "View documentation related to this dataset"
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
-                    "downloadURL": "https://e4ftl01.cr.usgs.gov/WORKING/BRWS/Browse.001/2020.11.18/pg-BR1A0000-2020111801_006_012.1.VNIR.jpg",
-                    "description": "Browse image for Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse image for Earthdata Search",
+                    "downloadURL": "https://e4ftl01.cr.usgs.gov/WORKING/BRWS/Browse.001/2020.11.18/pg-BR1A0000-2020111801_006_012.1.VNIR.jpg",
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
+            "graphic-preview-file": "https://e4ftl01.cr.usgs.gov/WORKING/BRWS/Browse.001/2020.11.18/pg-BR1A0000-2020111801_006_012.1.VNIR.jpg",
+            "identifier": "C1299783631-LPDAAC_ECS",
+            "issued": "2006-10-13",
+            "keyword": [
+                "infrared wavelengths",
+                "national geospatial data asset",
+                "ngda",
+                "spectral/engineering",
+                "earth science",
+                "visible wavelengths"
+            ],
+            "landingPage": "https://doi.org/10.5067/ASTER/AST_09XT.003",
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
+            "series-name": "AST_09XT.003",
             "spatial": "-180.0 -83.0 180.0 83.0",
+            "temporal": "2000-03-06T00:30:05Z/2024-12-16T00:00:00Z",
             "theme": [
                 "Terra",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "ASTER L2 Surface Radiance - VNIR and Crosstalk Corrected SWIR V003"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/ZRRJPGWL8AVL",
             "citation": "Global Modeling and Assimilation Office (GMAO). 2015-06-30. M2T3NPTRB. Version 5.12.4. MERRA-2 tavg3_3d_trb_Np: 3d,3-Hourly,Time-Averaged,Pressure-Level,Assimilation,Turbulence Diagnostics V5.12.4. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/ZRRJPGWL8AVL. https://disc.gsfc.nasa.gov/datacollection/M2T3NPTRB_5.12.4.html. Digital Science Data.",
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
-                "atmospheric winds",
-                "earth science",
-                "atmosphere"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "DANA OSTRENGA",
                 "hasEmail": "mailto:dana.ostrenga@nasa.gov"
             },
+            "creator": "Global Modeling and Assimilation Office (GMAO)",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C1276812691-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "M2T3NPTRB (or  tavg3_3d_trb_Np) is a 3-dimensional 3-hourly time averaged data collection in Modern-Era Retrospective analysis for Research and Applications version 2 (MERRA-2).  This collection consists of assimilations of turbulence diagnostics on 42 pressure levels, such as total scalar diffusivity, total momentum diffusivity, momentum diffusivity from Louis, and Richardson number from Louis. The data field is available every three hour starting from 01:30 UTC, e.g.: 01:30, 04:30, \u2026 , 22:30 UTC. The information on the pressure levels can be found in the section 4.2 of the MERRA-2 File Specification document. \n\nMERRA-2 is the latest version of global atmospheric reanalysis for the satellite era produced by NASA Global Modeling and Assimilation Office (GMAO) using the Goddard Earth Observing System Model (GEOS) version 5.12.4.  The dataset covers the period of 1980-present with the latency of ~3 weeks after the end of a month. \n\nData Reprocessing:  Please check \u201cRecords of MERRA-2 Data Reprocessing and Service Changes\u201d linked from the \u201cDocumentation\u201d tab on this page.  Note that a reprocessed data filename is different from the original file.\n\nMERRA-2 Mailing List: Sign up to receive information on reprocessing of data, changing of tools and services, as well as data announcements from GMAO. Contact the GES DISC Help Desk (gsfc-dl-help-disc@mail.nasa.gov) to be added to the list.\n\nQuestions: If you have a question, please read \"MERRA-2 File Specification Document\",  \u201cMERRA-2 Data Access \u2013 Quick Start Guide\u201d, and FAQs linked from the \u201dDocumentation\u201d tab on this page.  If that does not answer your question, you may email the question on data access to the GES DISC Help Desk (gsfc-dl-help-disc@mail.nasa.gov), or the question on science to the MERRA-2 science team (merra-questions@lists.nasa.gov).",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "M2T3NPTRB",
-            "creator": "Global Modeling and Assimilation Office (GMAO)",
-            "graphic-preview-description": "M2T3NPTRB variable",
-            "title": "MERRA-2 tavg3_3d_trb_Np: 3d,3-Hourly,Time-Averaged,Pressure-Level,Assimilation,Turbulence Diagnostics 0.625 x 0.5 degree V5.12.4 (M2T3NPTRB) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/M2T3NPTRB_5.12.4.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FZRRJPGWL8AVL",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FZRRJPGWL8AVL",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/M2T3NPTRB_5.12.4.png",
-                    "description": "M2T3NPTRB variable",
                     "@type": "dcat:Distribution",
+                    "description": "M2T3NPTRB variable",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/M2T3NPTRB_5.12.4.png",
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
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/M2T3NPTRB_5.12.4.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/M2T3NPTRB_5.12.4.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://goldsmr5.gesdisc.eosdis.nasa.gov/data/MERRA2/M2T3NPTRB.5.12.4/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://goldsmr5.gesdisc.eosdis.nasa.gov/data/MERRA2/M2T3NPTRB.5.12.4/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=M2T3NPTRB",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=M2T3NPTRB",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://goldsmr5.gesdisc.eosdis.nasa.gov/dods/M2T3NPTRB.info",
-                    "description": "The GrADS Data Server (GDS) is another form of OPeNDAP that provides subsetting and some analysis services across the Internet.",
                     "@type": "dcat:Distribution",
+                    "description": "The GrADS Data Server (GDS) is another form of OPeNDAP that provides subsetting and some analysis services across the Internet.",
+                    "downloadURL": "https://goldsmr5.gesdisc.eosdis.nasa.gov/dods/M2T3NPTRB.info",
+                    "mediaType": "text/html",
                     "title": "Use GRADS DATA SERVER (GDS) to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://goldsmr5.gesdisc.eosdis.nasa.gov/opendap/MERRA2/M2T3NPTRB.5.12.4/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://goldsmr5.gesdisc.eosdis.nasa.gov/opendap/MERRA2/M2T3NPTRB.5.12.4/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://goldsmr5.gesdisc.eosdis.nasa.gov/thredds/catalog/MERRA2_aggregation/M2T3NPTRB.5.12.4/catalog.html",
-                    "description": "Time aggregated THREDDS Data Server (TDS)",
                     "@type": "dcat:Distribution",
+                    "description": "Time aggregated THREDDS Data Server (TDS)",
+                    "downloadURL": "https://goldsmr5.gesdisc.eosdis.nasa.gov/thredds/catalog/MERRA2_aggregation/M2T3NPTRB.5.12.4/catalog.html",
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
-                    "downloadURL": "https://goldsmr5.gesdisc.eosdis.nasa.gov/data/MERRA2/M2T3NPTRB.5.12.4/doc/MERRA2.README.pdf",
-                    "description": "README Document",
                     "@type": "dcat:Distribution",
+                    "description": "README Document",
+                    "downloadURL": "https://goldsmr5.gesdisc.eosdis.nasa.gov/data/MERRA2/M2T3NPTRB.5.12.4/doc/MERRA2.README.pdf",
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
+            "graphic-preview-description": "M2T3NPTRB variable",
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/M2T3NPTRB_5.12.4.png",
+            "identifier": "C1276812691-GES_DISC",
+            "issued": "2007-06-14",
+            "keyword": [
+                "atmospheric winds",
+                "earth science",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.5067/ZRRJPGWL8AVL",
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
+            "series-name": "M2T3NPTRB",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "1980-01-01T00:00:00Z/2024-03-27T00:00:00Z",
             "theme": [
                 "MERRA-2",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "MERRA-2 tavg3_3d_trb_Np: 3d,3-Hourly,Time-Averaged,Pressure-Level,Assimilation,Turbulence Diagnostics 0.625 x 0.5 degree V5.12.4 (M2T3NPTRB) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewBundle.jsp?identifier=urn%3Anasa%3Apds%3Amer1_mtes_derived_emissivity&version=1.0",
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
+            "description": "This bundle contains derived emissivity data from the Mini-TES instrument on Mars Exploration Rover 1 (Opportunity).",
+            "identifier": "urn:nasa:pds:mer1_mtes_derived_emissivity",
+            "issued": "2021-05-21",
+            "keyword": [
+                "mars exploration rover",
+                "mars"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewBundle.jsp?identifier=urn%3Anasa%3Apds%3Amer1_mtes_derived_emissivity&version=1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:mer1_mtes_derived_emissivity",
-            "description": "This bundle contains derived emissivity data from the Mini-TES instrument on Mars Exploration Rover 1 (Opportunity).",
-            "title": "MER1 Mini-TES Derived Emissivity Data Bundle",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "MER1 Mini-TES Derived Emissivity Data Bundle"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC2-0637-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 2 phase 2015-03-11 to 2015-06-30. It is a Global Gravity measurement at the comet 67P and covers the time 2015-03-11T10:24:05.000 to 2015-03-11T12:24:01.500.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc2-0637-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC2-0637-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc2-0637-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 2 phase 2015-03-11 to 2015-06-30. It is a Global Gravity measurement at the comet 67P and covers the time 2015-03-11T10:24:05.000 to 2015-03-11T12:24:01.500.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 2 0637 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 2 0637 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/649",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Post, W.M. 2002. SAFARI 2000 Soil Types, 0.5-Deg Grid (Modified Zobler). ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/649",
-            "issued": "2023-10-18",
-            "temporal": "1974-01-01T00:00:00Z/1981-12-31T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-10-24",
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
-            "identifier": "C2788353687-ORNL_CLOUD",
             "description": "A SAFARI 2000 data set of soil types is available at 0.5-degree latitude by 0.5-degree longitude resolution. There are 106 soil units, based on Zobler's (1986) assessment of the FAO/UNESCO Soil Map of the World. This data set is a conversion of the Zobler 1-degree resolution version to a 0.5-degree resolution. The resolution of the data set was not actually increased. Rather, the 1-degree squares were divided into four 0.5-degree squares with the necessary adjustment of continental boundaries and islands.",
-            "graphic-preview-description": "Browse Image",
-            "title": "SAFARI 2000 Soil Types, 0.5-Deg Grid (Modified Zobler)",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/safari_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F649",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F649",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/safari2k/soils/Zobler_Soil/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/safari2k/soils/Zobler_Soil/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/S2K/guides/zoblersoilderived1.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/S2K/guides/zoblersoilderived1.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/649",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/649",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/safari2k/soils/Zobler_Soil/comp/readme.txt",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/safari2k/soils/Zobler_Soil/comp/readme.txt",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/safari2k/soils/Zobler_Soil/comp/zobler.legend",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/safari2k/soils/Zobler_Soil/comp/zobler.legend",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/safari2k/soils/Zobler_Soil/comp/zobler_readme.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/safari2k/soils/Zobler_Soil/comp/zobler_readme.pdf",
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
+            "identifier": "C2788353687-ORNL_CLOUD",
+            "issued": "2023-10-18",
+            "keyword": [
+                "soils",
+                "earth science",
+                "land surface"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/649",
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
             "spatial": "5.0 -35.0 60.0 5.0",
+            "temporal": "1974-01-01T00:00:00Z/1981-12-31T23:59:59Z",
             "theme": [
                 "SAFARI 2000",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "SAFARI 2000 Soil Types, 0.5-Deg Grid (Modified Zobler)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=GO-V-EPD-4-SUMM-5.0MIN-V1.0",
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
-                "venus",
-                "galileo"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This data set contains 5 minute averages\nfor the energetic particle detector rate data obtained from the LEMMS\ntelescope during the time the detector was operated during the Venus\nencounter.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.go-v-epd-4-summ-5.0min-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "venus",
+                "galileo"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=GO-V-EPD-4-SUMM-5.0MIN-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.go-v-epd-4-summ-5.0min-v1.0",
-            "description": "This data set contains 5 minute averages\nfor the energetic particle detector rate data obtained from the LEMMS\ntelescope during the time the detector was operated during the Venus\nencounter.",
-            "title": "GO VEN EPD RESAMPLED SUMMARY 5.0 MIN V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "GO VEN EPD RESAMPLED SUMMARY 5.0 MIN V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=CH1-ORB-L-MRFFR-5-CDR-MAP-V1.0",
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
-                "chandrayaan-1"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This data set contains archival map-projected calibrated data acquired from the Mini-RF (Mini-SAR) Forerunner instrument during the Chandrayaan-1 mission and associated ancillary data.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ch1-orb-l-mrffr-5-cdr-map-v1.0_rwxy-q3e9",
+            "issued": "2018-06-26",
+            "keyword": [
+                "moon",
+                "chandrayaan-1"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=CH1-ORB-L-MRFFR-5-CDR-MAP-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ch1-orb-l-mrffr-5-cdr-map-v1.0_rwxy-q3e9",
-            "description": "This data set contains archival map-projected calibrated data acquired from the Mini-RF (Mini-SAR) Forerunner instrument during the Chandrayaan-1 mission and associated ancillary data.",
-            "title": "CH1-ORB MOON MINI-RF 5 MAP-PROJ CALIBRATED DATA REC V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "CH1-ORB MOON MINI-RF 5 MAP-PROJ CALIBRATED DATA REC V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ASTER/ASTWBD_ATTNC.001",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "NASA/METI/AIST/Japan Spacesystems and U.S./Japan ASTER Science Team. 2019-08-05. ASTWBD_ATTNC.001. ASTER Global Water Bodies Database Attributes NetCDF V001. Sioux Falls, South Dakota, USA. Archived by National Aeronautics and Space Administration, U.S. Government, NASA EOSDIS Land Processes Distributed Active Archive Center. https://doi.org/10.5067/ASTER/ASTWBD_ATTNC.001. https://doi.org/10.5067/ASTER/ASTWBD_ATTNC.001.",
-            "issued": "2019-08-05",
-            "temporal": "2000-03-01T00:00:00Z/2013-11-30T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2019-08-05",
-            "keyword": [
-                "surface water",
-                "terrestrial hydrosphere",
-                "ngda",
-                "national geospatial data asset",
-                "earth science",
-                "topography",
-                "land surface"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "undefined",
                 "hasEmail": "mailto:mjabrams@jpl.nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "LP DAAC"
-            },
-            "identifier": "C1575734760-LPDAAC_ECS",
-            "description": "The ASTER Global Water Bodies Database (ASTWBD) Version 1 data product provides global coverage of water bodies larger than 0.2 square kilometers at a spatial resolution of 1 arc second (approximately 30 meters) at the equator, along with associated elevation information. \r\n\r\nThe ASTWBD data product was created in conjunction with the ASTER Global Digital Elevation Model (ASTER GDEM) Version 3 data product by the Sensor Information Laboratory Corporation (SILC) in Tokyo. The ASTER GDEM Version 3 data product was generated using ASTER Level 1A (https://doi.org/10.5067/ASTER/AST_L1A.003) scenes acquired between March 1, 2000, and November 30, 2013. The ASTWBD data product was then generated to correct elevation values of water body surfaces.\r\n\r\nTo generate the ASTWBD data product, water bodies were separated from land areas and then classified into three categories: ocean, river, or lake. Oceans and lakes have a flattened, constant elevation value. The effects of sea ice were manually removed from areas classified as oceans to better delineate ocean shorelines in high latitude areas. For lake waterbodies, the elevation for each lake was calculated from the perimeter elevation data using the mosaic image that covers the entire area of the lake. Rivers presented a unique challenge given that their elevations gradually step down from upstream to downstream; therefore, visual inspection and other manual detection methods were required. \r\n\r\nThe geographic coverage of the ASTWBD extends from 83\u00b0N to 83\u00b0S. Each tile is distributed in NetCDF format and referenced to the 1984 World Geodetic System (WGS84)/1996 Earth Gravitational Model (EGM96) geoid. Each ASTWBD_ATTNC file contains an attribute file with the water body classification information. The corresponding  ASTWBD_NC data product DEM file, which provides elevation information in meters.",
-            "release-place": "Sioux Falls, South Dakota, USA",
-            "series-name": "ASTWBD_ATTNC.001",
-            "graphic-preview-description": "Browse image for Earthdata Search",
             "creator": "NASA/METI/AIST/Japan Spacesystems and U.S./Japan ASTER Science Team",
-            "title": "ASTER Global Water Bodies Database Attributes NetCDF V001",
-            "graphic-preview-file": "https://e4ftl01.cr.usgs.gov/WORKING/BRWS/Browse.001/2019.07.01/ASTWBDV001_N06E004_att.1.jpg?_ga=2.93072671.344140723.1565008229-1371303444.1563801461",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The ASTER Global Water Bodies Database (ASTWBD) Version 1 data product provides global coverage of water bodies larger than 0.2 square kilometers at a spatial resolution of 1 arc second (approximately 30 meters) at the equator, along with associated elevation information. \r\n\r\nThe ASTWBD data product was created in conjunction with the ASTER Global Digital Elevation Model (ASTER GDEM) Version 3 data product by the Sensor Information Laboratory Corporation (SILC) in Tokyo. The ASTER GDEM Version 3 data product was generated using ASTER Level 1A (https://doi.org/10.5067/ASTER/AST_L1A.003) scenes acquired between March 1, 2000, and November 30, 2013. The ASTWBD data product was then generated to correct elevation values of water body surfaces.\r\n\r\nTo generate the ASTWBD data product, water bodies were separated from land areas and then classified into three categories: ocean, river, or lake. Oceans and lakes have a flattened, constant elevation value. The effects of sea ice were manually removed from areas classified as oceans to better delineate ocean shorelines in high latitude areas. For lake waterbodies, the elevation for each lake was calculated from the perimeter elevation data using the mosaic image that covers the entire area of the lake. Rivers presented a unique challenge given that their elevations gradually step down from upstream to downstream; therefore, visual inspection and other manual detection methods were required. \r\n\r\nThe geographic coverage of the ASTWBD extends from 83\u00b0N to 83\u00b0S. Each tile is distributed in NetCDF format and referenced to the 1984 World Geodetic System (WGS84)/1996 Earth Gravitational Model (EGM96) geoid. Each ASTWBD_ATTNC file contains an attribute file with the water body classification information. The corresponding  ASTWBD_NC data product DEM file, which provides elevation information in meters.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASTER%2FASTWBD_ATTNC.001",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASTER%2FASTWBD_ATTNC.001",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/ASTER/ASTWBD_ATTNC.001",
-                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
+                    "downloadURL": "https://doi.org/10.5067/ASTER/ASTWBD_ATTNC.001",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
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
-                    "downloadURL": "https://asterweb.jpl.nasa.gov/",
-                    "description": "The ASTER home page is maintained through NASA's Jet Propulsion Laboratory and documents various aspects of the ASTER mission.",
                     "@type": "dcat:Distribution",
+                    "description": "The ASTER home page is maintained through NASA's Jet Propulsion Laboratory and documents various aspects of the ASTER mission.",
+                    "downloadURL": "https://asterweb.jpl.nasa.gov/",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "application/x-netcdf",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=C1575734760-LPDAAC_ECS",
-                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=C1575734760-LPDAAC_ECS",
+                    "mediaType": "application/x-netcdf",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "application/x-netcdf",
-                    "downloadURL": "https://e4ftl01.cr.usgs.gov/ASTT/ASTWBD_ATTNC.001/",
-                    "description": "LP DAAC Data Pool provides direct access to available products via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "LP DAAC Data Pool provides direct access to available products via HTTPS.",
+                    "downloadURL": "https://e4ftl01.cr.usgs.gov/ASTT/ASTWBD_ATTNC.001/",
+                    "mediaType": "application/x-netcdf",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://lpdaac.usgs.gov/documents/436/ASTWBD_User_Guide_V1.pdf",
-                    "description": "The technical information in the User's Guide enables users to interpret and use the data products.",
                     "@type": "dcat:Distribution",
+                    "description": "The technical information in the User's Guide enables users to interpret and use the data products.",
+                    "downloadURL": "https://lpdaac.usgs.gov/documents/436/ASTWBD_User_Guide_V1.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://e4ftl01.cr.usgs.gov/WORKING/BRWS/Browse.001/2019.07.01/ASTWBDV001_N06E004_att.1.jpg?_ga=2.93072671.344140723.1565008229-1371303444.1563801461",
-                    "description": "Browse image for Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse image for Earthdata Search",
+                    "downloadURL": "https://e4ftl01.cr.usgs.gov/WORKING/BRWS/Browse.001/2019.07.01/ASTWBDV001_N06E004_att.1.jpg?_ga=2.93072671.344140723.1565008229-1371303444.1563801461",
+                    "mediaType": "text/html",
                     "title": "Get a related visualization"
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
-                    "downloadURL": "https://opendap.cr.usgs.gov/opendap/hyrax/ASTWBD_ATTNC.001/contents.html",
-                    "description": "OPeNDAP provides direct access to data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "OPeNDAP provides direct access to data via HTTPS.",
+                    "downloadURL": "https://opendap.cr.usgs.gov/opendap/hyrax/ASTWBD_ATTNC.001/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 }
             ],
+            "graphic-preview-description": "Browse image for Earthdata Search",
+            "graphic-preview-file": "https://e4ftl01.cr.usgs.gov/WORKING/BRWS/Browse.001/2019.07.01/ASTWBDV001_N06E004_att.1.jpg?_ga=2.93072671.344140723.1565008229-1371303444.1563801461",
+            "identifier": "C1575734760-LPDAAC_ECS",
+            "issued": "2019-08-05",
+            "keyword": [
+                "surface water",
+                "terrestrial hydrosphere",
+                "ngda",
+                "national geospatial data asset",
+                "earth science",
+                "topography",
+                "land surface"
+            ],
+            "landingPage": "https://doi.org/10.5067/ASTER/ASTWBD_ATTNC.001",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2019-08-05",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "LP DAAC"
+            },
+            "release-place": "Sioux Falls, South Dakota, USA",
+            "series-name": "ASTWBD_ATTNC.001",
             "spatial": "-180.0 -83.0 180.0 82.0",
+            "temporal": "2000-03-01T00:00:00Z/2013-11-30T23:59:59.999Z",
             "theme": [
                 "Terra",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "ASTER Global Water Bodies Database Attributes NetCDF V001"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC4-1207-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 4 phase 2015-10-22 to 2015-12-31. It is a Global Gravity measurement at the comet 67P and covers the time 2015-11-23T19:04:55.000 to 2015-11-24T02:25:05.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc4-1207-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC4-1207-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc4-1207-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 4 phase 2015-10-22 to 2015-12-31. It is a Global Gravity measurement at the comet 67P and covers the time 2015-11-23T19:04:55.000 to 2015-11-24T02:25:05.000.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 4 1207 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 4 1207 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ASDC/SUBORBITAL/SOLVE2_Satellite_Data_1",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/ASDC/SUBORBITAL/SOLVE2_Satellite_Data_1.",
-            "issued": "2022-09-12",
-            "temporal": "2002-12-01T00:00:00Z/2003-03-02T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-12-13",
-            "keyword": [
-                "atmospheric water vapor",
-                "atmospheric chemistry",
-                "earth science",
-                "atmospheric temperature",
-                "atmospheric pressure",
-                "atmospheric winds",
-                "atmosphere",
-                "aerosols"
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
-            "identifier": "C2569836981-LARC_ASDC",
             "description": "SOLVE2_Satellite_Data is the supplementary satellite data for the SAGE III Ozone Loss and Validation Experiment II (SOLVE II). Data were collected by the Polar Ozone and Aerosol Measurement III (POAM III) satellite. Data collection for this product is complete.\r\n\r\nThe SOLVE campaign was a NASA multi-program effort of the Upper Atmosphere Research Program (UARP), Atmospheric Effects of Aviation Project (AEAP), Atmospheric Chemistry Modeling and Analysis Program (ACMAP) and Earth Observing System (EOS) of NASA\u2019s Earth Science Enterprise (ESE). SOLVE\u2019s primary objective was for calibrating and validating the Stratospheric Aerosol and Gas Experiment (SAGE) III satellite measurements, while examining the processes that controlled ozone levels at a mid- to high-latitude range. The major goal of SAGE III was to quantitatively assess ozone loss at high latitudes. SOLVE was a two-phase experiment, the first phase, SOLVE, occurred during the fall of 1999 through the spring of 2000. The second phase, SOLVE II, occurred during the winter of 2003.\r\n\r\nSOLVE took place in the Arctic high-latitude region during the winter. The polar ozone depletion processes cause by human-produced chlorine and bromine are most active in mid-to-late winter and early spring in the high Arctic. In order to conduct this validation experiment, NASA deployed the NASA ER-2 aircraft and NASA DC-8 aircraft. The ER-2 measured a variety of atmospheric data, including ozone (O3), H2O, CO2, ClONO2, HCl, ClO/BrO, and Cl2O2. The DC-8 aircraft measured ozone, ClO/BrO, and aerosol, among other atmospheric data. SOLVE also utilized balloon platforms, ground-based instruments, and collaborations with the German Aerospace Center\u2019s (DLR) FALCON aircraft equipped with the OLEX Lidar to achieve the mission objectives. Overall, the campaign had 28 flights, with SOLVE featuring 17 total flights among the different aircrafts and SOLVE II featuring 11 flights.",
-            "title": "SOLVE II Supplementary Satellite Data Products",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC%2FSUBORBITAL%2FSOLVE2_Satellite_Data_1",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC%2FSUBORBITAL%2FSOLVE2_Satellite_Data_1",
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
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/SOLVE_II/Satellite_Data_1/",
-                    "description": "ASDC Direct Data Download for SOLVE2_Satellite_Data_1",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for SOLVE2_Satellite_Data_1",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/SOLVE_II/Satellite_Data_1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 }
             ],
+            "identifier": "C2569836981-LARC_ASDC",
+            "issued": "2022-09-12",
+            "keyword": [
+                "atmospheric water vapor",
+                "atmospheric chemistry",
+                "earth science",
+                "atmospheric temperature",
+                "atmospheric pressure",
+                "atmospheric winds",
+                "atmosphere",
+                "aerosols"
+            ],
+            "landingPage": "https://doi.org/10.5067/ASDC/SUBORBITAL/SOLVE2_Satellite_Data_1",
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
             "spatial": "<?xml version=\"1.0\" encoding=\"UTF-8\"?><gml:Polygon xmlns:gml=\"http://www.opengis.net/gml/3.2\" srsName=\"EPSG:9825\"><gml:outerBoundaryIs><gml:LinearRing><gml:posList>63.4 -180.0 63.4 180.0 67.6 180.0 67.6 -180.0 63.4 -180.0</gml:posList></gml:LinearRing></gml:outerBoundaryIs><gml:innerBoundaryIs></gml:innerBoundaryIs></gml:Polygon>",
+            "temporal": "2002-12-01T00:00:00Z/2003-03-02T23:59:59.999Z",
             "theme": [
                 "SOLVE",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "SOLVE II Supplementary Satellite Data Products"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/AQUA/MODIS/L3M/RRS/2022",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/GSFC/SED/ESD/GCDC/OB.DAAC. https://doi.org/10.5067/AQUA/MODIS/L3M/RRS/2022.",
-            "issued": "2019-06-23",
-            "temporal": "2002-07-04T00:00:00Z/2023-02-28T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2019-10-01",
-            "keyword": [
-                "oceans",
-                "ocean optics",
-                "earth science",
-                "atmosphere",
-                "ngda",
-                "aerosols",
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
-            "identifier": "C2330512571-OB_DAAC",
             "description": "MODIS (or Moderate-Resolution Imaging Spectroradiometer) is a key instrument aboard the Terra (EOS AM) and Aqua (EOS PM) satellites. Terra's orbit around the Earth is timed so that it passes from north to south across the equator in the morning, while Aqua passes south to north over the equator in the afternoon. Terra MODIS and Aqua MODIS are viewing the entire Earth's surface every 1 to 2 days, acquiring data in 36 spectral bands, or groups of wavelengths (see MODIS Technical Specifications). These data will improve our understanding of global dynamics and processes occurring on the land, in the oceans, and in the lower atmosphere. MODIS is playing a vital role in the development of validated, global, interactive Earth system models able to predict global change accurately enough to assist policy makers in making sound decisions concerning the protection of our environment.",
-            "title": "Aqua MODIS Global Mapped Remote-Sensing Reflectance (RRS) Data, version R2022.0",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAQUA%2FMODIS%2FL3M%2FRRS%2F2022",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAQUA%2FMODIS%2FL3M%2FRRS%2F2022",
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
-                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/data/10.5067/AQUA/MODIS/L3M/RRS/2022",
-                    "description": "MODIS-Aqua L3M Remote-Sensing Reflectance (RRS) Dataset Landing Page",
                     "@type": "dcat:Distribution",
+                    "description": "MODIS-Aqua L3M Remote-Sensing Reflectance (RRS) Dataset Landing Page",
+                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/data/10.5067/AQUA/MODIS/L3M/RRS/2022",
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
+            "identifier": "C2330512571-OB_DAAC",
+            "issued": "2019-06-23",
+            "keyword": [
+                "oceans",
+                "ocean optics",
+                "earth science",
+                "atmosphere",
+                "ngda",
+                "aerosols",
+                "national geospatial data asset"
+            ],
+            "landingPage": "https://doi.org/10.5067/AQUA/MODIS/L3M/RRS/2022",
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
+            "title": "Aqua MODIS Global Mapped Remote-Sensing Reflectance (RRS) Data, version R2022.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=LCROSS-E%2FL-NIR1-2-RAW-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "Raw, uncalibrated image data from the Near Infrared Camera 1 (NIR1) aboard the Lunar Crater Observation and Sensing Satellite (LCROSS).",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.lcross-e-l-nir1-2-raw-v1.0_rxcm-8iw5",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "test image",
                 "calibration",
@@ -1331066,69 +1331068,45 @@
                 "lunar crater observation and sensing satellite",
                 "moon"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=LCROSS-E%2FL-NIR1-2-RAW-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.lcross-e-l-nir1-2-raw-v1.0_rxcm-8iw5",
-            "description": "Raw, uncalibrated image data from the Near Infrared Camera 1 (NIR1) aboard the Lunar Crater Observation and Sensing Satellite (LCROSS).",
-            "title": "LCROSS EARTH/MOON 1ST NEAR IR CAMERA 2 RAW V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "LCROSS EARTH/MOON 1ST NEAR IR CAMERA 2 RAW V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/8U0VGVQC7HZG",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "OCO Science Team/Michael Gunson, Annmarie Eldering. 2024-04-10. OCO3_L2_Lite_FP. Version 11r. OCO-3 Level 2 bias-corrected XCO2 and other select fields from the full-physics retrieval aggregated as daily files, Retrospective processing V11r. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/8U0VGVQC7HZG. https://disc.gsfc.nasa.gov/datacollection/OCO3_L2_Lite_FP_11r.html. Digital Science Data.",
-            "issued": "2021-05-31",
-            "temporal": "2019-08-06T00:00:00Z/2024-10-07T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2021-05-31",
-            "keyword": [
-                "earth science",
-                "atmospheric chemistry",
-                "atmosphere"
-            ],
-            "data-presentation-form": "Digital Science Data",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "ANDREY SAVTCHENKO",
                 "hasEmail": "mailto:Andrey.Savtchenko@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
-            "identifier": "C2910086168-GES_DISC",
-            "description": "Version 11r is the current version of the data set. Older versions will no longer be available and are superseded by Version 11r.\n\nThe Orbiting Carbon Observatory -3 (OCO-3) was deployed to the International Space Station in May, 2019. It is technically a single instrument, almost identical to OCO-2.\n\nThe Orbiting Carbon Observatory is the first NASA mission designed to collect space-based measurements of atmospheric carbon dioxide with the precision, resolution, and coverage needed to characterize the processes controlling its buildup in the atmosphere.\n\nOCO-3 incorporates three high-resolution spectrometers that make coincident measurements of reflected sunlight in the near-infrared CO2 near 1.61 and 2.06 micrometers and in molecular oxygen (O2) A-Band at 0.76 micrometers. The three spectrometers have different characteristics and are calibrated independently. \n\nOxygen-A Band cloud screening algorithm is one of the primary cloud screening tools implemented in the operational OCO processing pipeline. The algorithm was introduced and applied to early GOSAT data  with further analysis performed on OCO-2 simulations.\n\nThe OCO ABO2 algorithm employs a fast Bayesian retrieval to estimate surface pressure and surface albedo from high resolution spectra of the molecular oxygen (O2) A-band, near 0.765 \u00b5m. The radiative transfer forward model (FM) assumes a clear-sky condition, i.e. Rayleigh scattering only, such that differences between the modeled and measured radiances are apparent when the measurement scene contains cloud or aerosol.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "OCO3_L2_Lite_FP",
             "creator": "OCO Science Team/Michael Gunson, Annmarie Eldering",
-            "title": "OCO-3 Level 2 bias-corrected XCO2 and other select fields from the full-physics retrieval aggregated as daily files, Retrospective processing V11r (OCO3_L2_Lite_FP) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/OCO/OCO3_L2_Lite_FP_10r.png",
-            "programCode": [
-                "026:001"
-            ],
+            "data-presentation-form": "Digital Science Data",
+            "description": "Version 11r is the current version of the data set. Older versions will no longer be available and are superseded by Version 11r.\n\nThe Orbiting Carbon Observatory -3 (OCO-3) was deployed to the International Space Station in May, 2019. It is technically a single instrument, almost identical to OCO-2.\n\nThe Orbiting Carbon Observatory is the first NASA mission designed to collect space-based measurements of atmospheric carbon dioxide with the precision, resolution, and coverage needed to characterize the processes controlling its buildup in the atmosphere.\n\nOCO-3 incorporates three high-resolution spectrometers that make coincident measurements of reflected sunlight in the near-infrared CO2 near 1.61 and 2.06 micrometers and in molecular oxygen (O2) A-Band at 0.76 micrometers. The three spectrometers have different characteristics and are calibrated independently. \n\nOxygen-A Band cloud screening algorithm is one of the primary cloud screening tools implemented in the operational OCO processing pipeline. The algorithm was introduced and applied to early GOSAT data  with further analysis performed on OCO-2 simulations.\n\nThe OCO ABO2 algorithm employs a fast Bayesian retrieval to estimate surface pressure and surface albedo from high resolution spectra of the molecular oxygen (O2) A-band, near 0.765 \u00b5m. The radiative transfer forward model (FM) assumes a clear-sky condition, i.e. Rayleigh scattering only, such that differences between the modeled and measured radiances are apparent when the measurement scene contains cloud or aerosol.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2F8U0VGVQC7HZG",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2F8U0VGVQC7HZG",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
@@ -1331138,59 +1331116,59 @@
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/OCO3_L2_Lite_FP_11r.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/OCO3_L2_Lite_FP_11r.html",
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
-                    "downloadURL": "https://oco2.gesdisc.eosdis.nasa.gov/data/OCO3_DATA/OCO3_L2_Lite_FP.11r/",
-                    "description": "Access the data via HTTP",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTP",
+                    "downloadURL": "https://oco2.gesdisc.eosdis.nasa.gov/data/OCO3_DATA/OCO3_L2_Lite_FP.11r/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://oco2.gesdisc.eosdis.nasa.gov/opendap/OCO3_L2_Lite_FP.11r/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://oco2.gesdisc.eosdis.nasa.gov/opendap/OCO3_L2_Lite_FP.11r/contents.html",
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
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=OCO3_L2_Lite_FP",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=OCO3_L2_Lite_FP",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
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
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/OCO/OCO3_L2_DQ_Statement_v10_v104.pdf",
-                    "description": "User's Guide",
                     "@type": "dcat:Distribution",
+                    "description": "User's Guide",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/OCO/OCO3_L2_DQ_Statement_v10_v104.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
                 },
                 {
@@ -1331200,374 +1331178,410 @@
                     "title": "View this dataset's algorithm theoretical basis document"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/OCO/OCO2_XCO2_Lite_Files_and_Bias_Correction.pdf",
-                    "description": "Bias Correction and Warn Levels",
                     "@type": "dcat:Distribution",
+                    "description": "Bias Correction and Warn Levels",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/OCO/OCO2_XCO2_Lite_Files_and_Bias_Correction.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
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
                 }
             ],
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/OCO/OCO3_L2_Lite_FP_10r.png",
+            "identifier": "C2910086168-GES_DISC",
+            "issued": "2021-05-31",
+            "keyword": [
+                "earth science",
+                "atmospheric chemistry",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.5067/8U0VGVQC7HZG",
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
+            "series-name": "OCO3_L2_Lite_FP",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2019-08-06T00:00:00Z/2024-10-07T00:00:00Z",
             "theme": [
                 "OCO-3",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "OCO-3 Level 2 bias-corrected XCO2 and other select fields from the full-physics retrieval aggregated as daily files, Retrospective processing V11r (OCO3_L2_Lite_FP) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/SeaBASS/Arctic_RSWQ/DATA001",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/GSFC/SED/ESD/GCDC/OB.DAAC. https://doi.org/10.5067/SeaBASS/Arctic_RSWQ/DATA001.",
-            "issued": "2018-08-27",
-            "temporal": "2018-08-27T00:00:02Z/2019-09-30T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-04-06",
-            "keyword": [
-                "oceans",
-                "salinity/density",
-                "ocean temperature",
-                "ocean chemistry",
-                "ocean optics",
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
-            "identifier": "C2077034346-OB_DAAC",
             "description": "This research project seeks to jumpstart Arctic-COLORS while filling major gaps in our knowledge about the transformation of riverine water quality constituents from the ABoVE domain through estuaries to the near coastal environment. The project conducted field sampling in the Yukon River, delta and plume waters for three transects in spring, early and late summer, and acquisition of additional transect samples during similar flow regimes through our collaborators on the north slope of Alaska and Mackenzie River. Field measurements included a number of water quality parameters relevant to Arctic biogeochemical function and NASA products, including dissolved organic matter (DOM), particulate organic matter (POM), suspended particulate matter (SPM), chlorophyll-a, radiometry, in situ inherent optical properties, discrete dissolved and particle absorption, fluorescent DOM (FDOM), lignin phenols, HPLC pigments, bioavailability of dissolved organic carbon (DOC).  Combined, our field sampling, algorithm development, hindcasting, and synthesis efforts will provide a foundation for a successful Arctic-COLORS campaign while providing critical new knowledge of transformations in estuarine systems.",
-            "title": "Impacts of estuarine processes on delivery of Arctic riverine materials to the near coastal environment: Implications for water quality and biogeochemical cycling in preparation for Arctic-COLORS",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSeaBASS%2FArctic_RSWQ%2FDATA001",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSeaBASS%2FArctic_RSWQ%2FDATA001",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://seabass.gsfc.nasa.gov/experiment/Arctic_RSWQ/",
-                    "description": "Detailed information about the SeaBASS Experiment such as cruises, funding, and investigators",
                     "@type": "dcat:Distribution",
+                    "description": "Detailed information about the SeaBASS Experiment such as cruises, funding, and investigators",
+                    "downloadURL": "https://seabass.gsfc.nasa.gov/experiment/Arctic_RSWQ/",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 }
             ],
+            "identifier": "C2077034346-OB_DAAC",
+            "issued": "2018-08-27",
+            "keyword": [
+                "oceans",
+                "salinity/density",
+                "ocean temperature",
+                "ocean chemistry",
+                "ocean optics",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/SeaBASS/Arctic_RSWQ/DATA001",
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
+            "temporal": "2018-08-27T00:00:02Z/2019-09-30T23:59:59Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Impacts of estuarine processes on delivery of Arctic riverine materials to the near coastal environment: Implications for water quality and biogeochemical cycling in preparation for Arctic-COLORS"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/RA1MIJOYPK3P",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "AMSR-E/AMSR2 Unified L3 Daily 12.5 km Brightness Temperatures, Sea Ice Concentration, Motion & Snow Depth Polar Grids V001. Version 1. Archived by National Aeronautics and Space Administration, U.S. Government, NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/RA1MIJOYPK3P.",
-            "issued": "2012-07-02",
-            "temporal": "2012-07-02T00:00:00Z/2024-12-16T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-12-09",
-            "keyword": [
-                "spectral/engineering",
-                "cryosphere",
-                "earth science",
-                "microwave",
-                "sea ice"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Walter Meier",
                 "hasEmail": "mailto:walt@nsidc.org"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA NSIDC DAAC"
-            },
-            "identifier": "C1542606326-NSIDC_ECS",
             "description": "The AMSR-E/AMSR2 Unified Level-3 12.5 km product provides brightness temperatures, sea ice concentration, and snow depth over sea ice for the Northern and Southern Hemisphere, as well as sea ice motion for the Arctic. This data set includes daily brightness temperature fields for channels ranging from 18.7 GHz through 89.0 GHz, daily sea ice concentration fields, and daily sea ice concentration difference fields for ascending orbits, descending orbits, and full orbit daily averages. Snow depth over sea ice is provided as a five-day running average for the Arctic and Antarctic. Sea Ice motion is provided daily for tracking ice movement over consecutive days in the Arctic.\n\n<b>Note:</b> This product uses the Japan Aerospace Exploration Agency (JAXA) AMSR2 Level-1R input brightness temperatures that are calibrated, or unified, across the JAXA AMSR-E and JAXA AMSR2 Level-1R products.",
-            "graphic-preview-description": "This application allows you to interactively browse global satellite imagery within hours of it being acquired. You can also save it, share it, and download the underlying data.",
-            "title": "AMSR-E/AMSR2 Unified L3 Daily 12.5 km Brightness Temperatures, Sea Ice Concentration, Motion & Snow Depth Polar Grids V001",
-            "graphic-preview-file": "https://worldview.earthdata.nasa.gov/?p=arctic&l=BlueMarble_NextGeneration,AMSRU2_Sea_Ice_Concentration_12km,Coastlines",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FRA1MIJOYPK3P",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FRA1MIJOYPK3P",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/AMSA/AU_SI12.001",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/AMSA/AU_SI12.001",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=AU_SI12+V001",
-                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=AU_SI12+V001",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/data/data-access-tool/AU_SI12/versions/1/",
-                    "description": "Search and filter data files using a map-based interface",
                     "@type": "dcat:Distribution",
+                    "description": "Search and filter data files using a map-based interface",
+                    "downloadURL": "https://nsidc.org/data/data-access-tool/AU_SI12/versions/1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://worldview.earthdata.nasa.gov/?p=arctic&l=BlueMarble_NextGeneration%2CAMSRU2_Sea_Ice_Concentration_12km%2CCoastlines",
-                    "description": "This application allows you to interactively browse global satellite imagery within hours of it being acquired. You can also save it, share it, and download the underlying data.",
                     "@type": "dcat:Distribution",
+                    "description": "This application allows you to interactively browse global satellite imagery within hours of it being acquired. You can also save it, share it, and download the underlying data.",
+                    "downloadURL": "https://worldview.earthdata.nasa.gov/?p=arctic&l=BlueMarble_NextGeneration%2CAMSRU2_Sea_Ice_Concentration_12km%2CCoastlines",
+                    "mediaType": "text/html",
                     "title": "Get a related visualization through WORLDVIEW"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/RA1MIJOYPK3P",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/RA1MIJOYPK3P",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/RA1MIJOYPK3P",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/RA1MIJOYPK3P",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "graphic-preview-description": "This application allows you to interactively browse global satellite imagery within hours of it being acquired. You can also save it, share it, and download the underlying data.",
+            "graphic-preview-file": "https://worldview.earthdata.nasa.gov/?p=arctic&l=BlueMarble_NextGeneration,AMSRU2_Sea_Ice_Concentration_12km,Coastlines",
+            "identifier": "C1542606326-NSIDC_ECS",
+            "issued": "2012-07-02",
+            "keyword": [
+                "spectral/engineering",
+                "cryosphere",
+                "earth science",
+                "microwave",
+                "sea ice"
+            ],
+            "landingPage": "https://doi.org/10.5067/RA1MIJOYPK3P",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2024-12-09",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA NSIDC DAAC"
+            },
             "spatial": "-180.0 -89.24 180.0 -39.23",
+            "temporal": "2012-07-02T00:00:00Z/2024-12-16T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "AMSR-E/AMSR2 Unified L3 Daily 12.5 km Brightness Temperatures, Sea Ice Concentration, Motion & Snow Depth Polar Grids V001"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/JWGEFX2FALQR",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "CLPX-Ground: Ground-based L and Ku band polarimetric scatterometry, Version 1. Version 1. Archived by National Aeronautics and Space Administration, U.S. Government, NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/JWGEFX2FALQR.",
-            "issued": "2003-02-17",
-            "temporal": "2003-02-17T00:00:00Z/2003-03-30T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2003-03-30",
-            "keyword": [
-                "precipitation",
-                "radar",
-                "sea ice",
-                "snow/ice",
-                "spectral/engineering",
-                "terrestrial hydrosphere",
-                "atmosphere",
-                "cryosphere",
-                "earth science",
-                "microwave"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Kamal Sarabandi",
                 "hasEmail": "mailto:saraband@eecs.umich.edu"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA NSIDC DAAC"
-            },
-            "identifier": "C1386203934-NSIDCV0",
             "description": "This data set includes ground-based radar observations carried out at the Fraser Experimental Forest Headquarters, Colorado, USA.",
-            "title": "CLPX-Ground: Ground-based L and Ku band polarimetric scatterometry, Version 1",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FJWGEFX2FALQR",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FJWGEFX2FALQR",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/CLP/data/ground_data/nsidc0166_lsos_scatterometer/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/CLP/data/ground_data/nsidc0166_lsos_scatterometer/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/CLP/data/ground_data/nsidc0166_lsos_scatterometer/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/CLP/data/ground_data/nsidc0166_lsos_scatterometer/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/JWGEFX2FALQR",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/JWGEFX2FALQR",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/JWGEFX2FALQR",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/JWGEFX2FALQR",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C1386203934-NSIDCV0",
+            "issued": "2003-02-17",
+            "keyword": [
+                "precipitation",
+                "radar",
+                "sea ice",
+                "snow/ice",
+                "spectral/engineering",
+                "terrestrial hydrosphere",
+                "atmosphere",
+                "cryosphere",
+                "earth science",
+                "microwave"
+            ],
+            "landingPage": "https://doi.org/10.5067/JWGEFX2FALQR",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2003-03-30",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA NSIDC DAAC"
+            },
             "spatial": "-105.9 39.95 -105.9 39.95",
+            "temporal": "2003-02-17T00:00:00Z/2003-03-30T23:59:59.999Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "CLPX-Ground: Ground-based L and Ku band polarimetric scatterometry, Version 1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/472",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Waring, R.H., B.E. Law, and B. Bond. 2013. NPP Temperate Forest: OTTER Project Sites, Oregon, USA, 1989-1991, R1. ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/472",
-            "issued": "2023-08-20",
-            "temporal": "1989-01-01T00:00:00Z/1991-12-31T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-08-23",
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
-            "identifier": "C2751945080-ORNL_CLOUD",
             "description": "This data set provides net primary productivity (NPP) estimates and associated field measurements for six sites located along the 250-km, west-east transect of the Oregon Transect Ecosystem Research Project (OTTER) in the Pacific Northwest. Leaf area indices, biomass, and NPP vary about 10-fold across the OTTER transect. Leaf area index (LAI) ranges from 0.4 m2/m2 at the Juniper/Sisters site to 8.6 m2/m2 at the Scio western Cascade site. Total NPP follows a similar trend with the Juniper/Sisters site having the lowest NPP value (300 g/m2/yr) and the Scio site having the highest (2,250-2,570 g/m2/yr). Total tree biomass across the transect ranges from to 1,080 g/m2 at Juniper/Sisters to 71,080 g/m2 at Cascade Head. Vegetation intercepts 22% to 99.5% of incident photosynthetically active radiation along the transect.There is one data file (.csv format) with this data set. Revision Notes: Only the documentation for this data set has been modified. The data files have been checked for accuracy and are identical to those originally published in 1999.",
-            "graphic-preview-description": "Browse Image",
-            "title": "NPP Temperate Forest: OTTER Project Sites, Oregon, USA, 1989-1991, R1",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/npp_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F472",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F472",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/npp/temperate_forest/NPP_OTTER/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/npp/temperate_forest/NPP_OTTER/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/NPP/guides/NPP_OTTER.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/NPP/guides/NPP_OTTER.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/472",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/472",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/npp/temperate_forest/NPP_OTTER/comp/NPP_OTTER.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/npp/temperate_forest/NPP_OTTER/comp/NPP_OTTER.pdf",
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
+            "identifier": "C2751945080-ORNL_CLOUD",
+            "issued": "2023-08-20",
+            "keyword": [
+                "biosphere",
+                "vegetation",
+                "ecological dynamics",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/472",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2023-08-23",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "ORNL_DAAC"
+            },
             "spatial": "-124.02 44.27 -121.17 44.95",
+            "temporal": "1989-01-01T00:00:00Z/1991-12-31T23:59:59Z",
             "theme": [
                 "NPP",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "NPP Temperate Forest: OTTER Project Sites, Oregon, USA, 1989-1991, R1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://www.nasa.gov/content/it-policies-and-standards/#.VZFTzuuxEwB",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Lori Parker",
+                "hasEmail": "mailto:lori.parker-1@nasa.gov"
+            },
+            "description": "The documents contained in this dataset reflect NASA's comprehensive IT policy in compliance with Federal Government laws and regulations.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "NASA Information Technology and Institutional Infrastructure Program and Project Management Requirements",
+                    "downloadURL": "http://nodis3.gsfc.nasa.gov/npg_img/N_PR_7120_0007_/N_PR_7120_0007_.pdf",
+                    "mediaType": "application/pdf",
+                    "title": "NPR7120.7.pdf"
+                }
+            ],
+            "identifier": "OCIO-Fitara-12",
             "issued": "2008-11-03",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
             "keyword": [
                 "it policy",
                 "institutional infrastructure",
@@ -1331577,555 +1331591,543 @@
                 "chief information officer",
                 "nasa it policy"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Lori Parker",
-                "hasEmail": "mailto:lori.parker-1@nasa.gov"
-            },
+            "landingPage": "http://www.nasa.gov/content/it-policies-and-standards/#.VZFTzuuxEwB",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:046"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "OCIO-Fitara-12",
-            "description": "The documents contained in this dataset reflect NASA's comprehensive IT policy in compliance with Federal Government laws and regulations.",
-            "title": "IT Policies and Standards - NASA Information Technology and Institutional Infrastructure Program and Project Management Requirements",
-            "programCode": [
-                "026:046"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "http://nodis3.gsfc.nasa.gov/npg_img/N_PR_7120_0007_/N_PR_7120_0007_.pdf",
-                    "description": "NASA Information Technology and Institutional Infrastructure Program and Project Management Requirements",
-                    "@type": "dcat:Distribution",
-                    "title": "NPR7120.7.pdf"
-                }
-            ],
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Management/Operations"
-            ]
+            ],
+            "title": "IT Policies and Standards - NASA Information Technology and Institutional Infrastructure Program and Project Management Requirements"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NEAR-A-MSI-3-EDR-EROS%2FORBIT-V1.0",
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
+            "description": "This data set contains calibrated images of Eros taken in orbit by the NEAR Multi-Spectral Imager.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.near-a-msi-3-edr-eros-orbit-v1.0_rxgc-hpk9",
+            "issued": "2021-05-21",
+            "keyword": [
+                "eros",
+                "near earth asteroid rendezvous"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NEAR-A-MSI-3-EDR-EROS%2FORBIT-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.near-a-msi-3-edr-eros-orbit-v1.0_rxgc-hpk9",
-            "description": "This data set contains calibrated images of Eros taken in orbit by the NEAR Multi-Spectral Imager.",
-            "title": "NEAR MSI IMAGES FOR EROS/ORBIT",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "NEAR MSI IMAGES FOR EROS/ORBIT"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=CLEM1-L-RSS-1-BSR-V1.0",
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
-                "deep space program science experiment"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "The Clementine Bistatic Radar Raw Data Archive (BSR-RDA) is a time-ordered collection of raw and partially processed data from bistatic radar scattering experiments conducted using the Clementine spacecraft while it orbited the Moon.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.clem1-l-rss-1-bsr-v1.0_rxgr-6rf2",
+            "issued": "2018-06-26",
+            "keyword": [
+                "moon",
+                "deep space program science experiment"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=CLEM1-L-RSS-1-BSR-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.clem1-l-rss-1-bsr-v1.0_rxgr-6rf2",
-            "description": "The Clementine Bistatic Radar Raw Data Archive (BSR-RDA) is a time-ordered collection of raw and partially processed data from bistatic radar scattering experiments conducted using the Clementine spacecraft while it orbited the Moon.",
-            "title": "CLEM1 LUNAR RADIO SCIENCE RAW BISTATIC RADAR V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "CLEM1 LUNAR RADIO SCIENCE RAW BISTATIC RADAR V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/EA7RCFXYB29L",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "SMEX03 Soil Moisture, Meteorological, and Vegetation Data: Brazil, Version 1. Version 1. Archived by National Aeronautics and Space Administration, U.S. Government, NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/EA7RCFXYB29L.",
-            "issued": "2003-12-01",
-            "temporal": "2003-12-01T00:00:00Z/2003-12-31T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2003-12-31",
-            "keyword": [
-                "soils",
-                "precipitation",
-                "land surface",
-                "atmospheric water vapor",
-                "biosphere",
-                "earth science",
-                "agriculture",
-                "vegetation",
-                "atmospheric temperature",
-                "atmosphere"
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
-            "identifier": "C1386205028-NSIDCV0",
             "description": "Notice to Data Users: The documentation for this data set was provided solely by the Principal Investigator(s) and was not further developed, thoroughly reviewed, or edited by NSIDC. Thus, support for this data set may be limited.\n\nThis data set contains soil moisture, vegetation, and meteorological data. An extensive collection of photographs documenting the regional study areas is also included.",
-            "title": "SMEX03 Soil Moisture, Meteorological, and Vegetation Data: Brazil, Version 1",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FEA7RCFXYB29L",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FEA7RCFXYB29L",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/AVDM/data/soil_moisture/SMEX03/Brazil/ground/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/AVDM/data/soil_moisture/SMEX03/Brazil/ground/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/AVDM/data/soil_moisture/SMEX03/Brazil/ground/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/AVDM/data/soil_moisture/SMEX03/Brazil/ground/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/AVDM/data/soil_moisture/SMEX03/Brazil/ground/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/AVDM/data/soil_moisture/SMEX03/Brazil/ground/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/AVDM/data/soil_moisture/SMEX03/Brazil/ground/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/AVDM/data/soil_moisture/SMEX03/Brazil/ground/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/EA7RCFXYB29L",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/EA7RCFXYB29L",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/EA7RCFXYB29L",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/EA7RCFXYB29L",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C1386205028-NSIDCV0",
+            "issued": "2003-12-01",
+            "keyword": [
+                "soils",
+                "precipitation",
+                "land surface",
+                "atmospheric water vapor",
+                "biosphere",
+                "earth science",
+                "agriculture",
+                "vegetation",
+                "atmospheric temperature",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.5067/EA7RCFXYB29L",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2003-12-31",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA NSIDC DAAC"
+            },
             "spatial": "-50.0 -17.0 -40.0 -7.0",
+            "temporal": "2003-12-01T00:00:00Z/2003-12-31T23:59:59.999Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "SMEX03 Soil Moisture, Meteorological, and Vegetation Data: Brazil, Version 1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C2131771775-GES_DISC.html",
             "citation": "EOS MLS Science Team. 2022-01-11. ML2N2O_NRT. Version 005. MLS/Aura Near-Real-Time L2 Nitrous Oxide (N2O) Mixing Ratio V005. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://disc.gsfc.nasa.gov/datacollection/ML2N2O_NRT_005.html. Digital Science Data.",
-            "issued": "2021-09-21",
-            "temporal": "2021-09-21T00:00:00Z/2023-02-28T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2021-09-21",
-            "keyword": [
-                "atmosphere",
-                "atmospheric chemistry",
-                "earth science"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "NATHANIEL LIVESEY",
                 "hasEmail": "mailto:livesey@mls.jpl.nasa.gov"
             },
+            "creator": "EOS MLS Science Team",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C2131771775-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "ML2N2O_NRT is the EOS Aura Microwave Limb Sounder (MLS) Near-Real-Time (NRT) product for nitrous oxide (N2O). This product contains N2O profiles derived from the 190 GHz region. The NRT data are typically available within 3 hours of observation and are broken into files containing about 15 minutes of data. The most recent 7 days of data are available online. Spatial coverage is near-global (-82 degrees to +82 degrees latitude), with each profile spaced 1.5 degrees or ~165 km along the orbit track (roughly 15 orbits per day). The vertical coverage is from 100 to 1 hPa.\n\nThe MLS NRT algorithm uses a simplified fast forward model to meet Near Real Time data latency requirements and are therefore not as accurate as the retrievals that constitute the standard MLS products. Nevertheless the results are scientifically useful in selected regions of the Earth's atmosphere provided that the data are screened according to the recommendations in the MLS NRT User Guide and the MLS L2 Data Quality Document for Standard Products.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "ML2N2O_NRT",
-            "creator": "EOS MLS Science Team",
-            "title": "MLS/Aura Near-Real-Time L2 Nitrous Oxide (N2O) Mixing Ratio V005 (ML2N2O_NRT) at GES DISC",
-            "graphic-preview-description": "Aura MLS logo",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/ML2N2O_NRT_003.jpeg",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/ML2N2O_NRT_003.jpeg",
-                    "description": "Aura MLS logo",
                     "@type": "dcat:Distribution",
+                    "description": "Aura MLS logo",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/ML2N2O_NRT_003.jpeg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/ML2N2O_NRT_005.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/ML2N2O_NRT_005.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://discnrt1.gesdisc.eosdis.nasa.gov/data/Aura_MLS_NRT/ML2N2O_NRT.005",
-                    "description": "Access the data via HTTPS. User registration is required. Register for a username and password at https://urs.eosdis.nasa.gov/users/new.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS. User registration is required. Register for a username and password at https://urs.eosdis.nasa.gov/users/new.",
+                    "downloadURL": "https://discnrt1.gesdisc.eosdis.nasa.gov/data/Aura_MLS_NRT/ML2N2O_NRT.005",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://discnrt1.gesdisc.eosdis.nasa.gov/opendap/Aura_MLS_NRT/ML2N2O_NRT.005/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://discnrt1.gesdisc.eosdis.nasa.gov/opendap/Aura_MLS_NRT/ML2N2O_NRT.005/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://discnrt1.gesdisc.eosdis.nasa.gov/datacasting/ML2N2O_NRT.005.datacast-feed.xml",
-                    "description": "Access the data via datacasting.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via datacasting.",
+                    "downloadURL": "https://discnrt1.gesdisc.eosdis.nasa.gov/datacasting/ML2N2O_NRT.005.datacast-feed.xml",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a datacast URL."
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=ML2N2O_NRT_005",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=ML2N2O_NRT_005",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://mls.jpl.nasa.gov/data/NRT-user-guide-v5.pdf",
-                    "description": "Aura MLS Version 5 Level 2 Near-Real-Time Data User Guide",
                     "@type": "dcat:Distribution",
+                    "description": "Aura MLS Version 5 Level 2 Near-Real-Time Data User Guide",
+                    "downloadURL": "https://mls.jpl.nasa.gov/data/NRT-user-guide-v5.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://mls.jpl.nasa.gov/data/v5-0_data_quality_document.pdf",
-                    "description": "Aura MLS Version 5 Level 2 Data Quality and Description Document",
                     "@type": "dcat:Distribution",
+                    "description": "Aura MLS Version 5 Level 2 Data Quality and Description Document",
+                    "downloadURL": "https://mls.jpl.nasa.gov/data/v5-0_data_quality_document.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://mls.jpl.nasa.gov/",
-                    "description": "MLS Science Team home page",
                     "@type": "dcat:Distribution",
+                    "description": "MLS Science Team home page",
+                    "downloadURL": "https://mls.jpl.nasa.gov/",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 }
             ],
+            "graphic-preview-description": "Aura MLS logo",
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/ML2N2O_NRT_003.jpeg",
+            "identifier": "C2131771775-GES_DISC",
+            "issued": "2021-09-21",
+            "keyword": [
+                "atmosphere",
+                "atmospheric chemistry",
+                "earth science"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C2131771775-GES_DISC.html",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2021-09-21",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
+            },
+            "release-place": "Greenbelt, MD, USA",
+            "series-name": "ML2N2O_NRT",
             "spatial": "-180.0 -82.0 180.0 82.0",
+            "temporal": "2021-09-21T00:00:00Z/2023-02-28T00:00:00Z",
             "theme": [
                 "Aura",
                 "LANCE",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "MLS/Aura Near-Real-Time L2 Nitrous Oxide (N2O) Mixing Ratio V005 (ML2N2O_NRT) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=ESO1M-SR-APPH-4-OCC-V1.0",
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
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.eso1m-sr-apph-4-occ-v1.0_rxpz-3xn8",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "saturn",
                 "s rings",
                 "saturn occultation of 28 sagittarius 1989"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=ESO1M-SR-APPH-4-OCC-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.eso1m-sr-apph-4-occ-v1.0_rxpz-3xn8",
-            "description": "TBD",
-            "title": "ESO1M SR AP-PHOTOMETER RESAMPLED RING OCCULTATION V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ESO1M SR AP-PHOTOMETER RESAMPLED RING OCCULTATION V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/Suborbital/LISTOS/Ground_BronxPfizer_Data_1",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2020-12-16. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/Suborbital/LISTOS/Ground_BronxPfizer_Data_1.",
-            "issued": "2020-09-08",
-            "temporal": "2018-01-01T00:00:00Z/2018-11-13T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-04-18",
-            "keyword": [
-                "atmosphere",
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
-            "identifier": "C1981386910-LARC_ASDC",
             "description": "LISTOS_Ground_BronxPfizer_Data is the Long Island Sound Tropospheric Ozone Study (LISTOS) ground site data collected at the Bronx Pfizer ground site during the LISTOS field campaign. This product is a result of a joint effort across multiple agencies, including NASA, NOAA, the EPA Northeast States for Coordinated Air Use Management (NESCAUM), Maine Department of Environmental Protection, New Jersey Department of Environmental Protection, New York State Department of Environmental Conservation and several research groups at universities. Data collection is complete.\r\n\r\nThe New York City (NYC) metropolitan area (comprised of portions of New Jersey, New York, and Connecticut in and around NYC) is home to over 20 million people, but also millions of people living downwind in neighboring states. This area continues to persistently have challenges meeting past and recently revised federal health-based air quality standards for ground-level ozone, which impacts the health and well-being of residents living in the area. A unique feature of this chronic ozone problem is the pollution transported in a northeast direction out of NYC over Long Island Sound. The relatively cool waters of Long Island Sound confine the pollutants in a shallow and stable marine boundary layer. Afternoon heating over coastal land creates a sea breeze that carries the air pollution inland from the confined marine layer, resulting in high ozone concentrations in Connecticut and, at times, farther east into Rhode Island and Massachusetts. To investigate the evolving nature of ozone formation and transport in the NYC region and downwind, Northeast States for Coordinated Air Use Management (NESCAUM) launched the Long Island Sound Tropospheric Ozone Study (LISTOS). LISTOS was a multi-agency collaborative study focusing on Long Island Sound and the surrounding coastlines that continually suffer from poor air quality exacerbated by land/water circulation. The primary measurement observations took place between June-September 2018 and include in-situ and remote sensing instrumentation that were integrated aboard three aircraft, a network of ground sites, mobile vehicles, boat measurements, and ozonesondes. The goal of LISTOS was to improve the understanding of ozone chemistry and sea breeze transported pollution over Long Island Sound and its coastlines. LISTOS also provided NASA the opportunity to test air quality remote sensing retrievals with the use of its airborne simulators (GEOstationary Coastal and Air Pollution Events (GEO-CAPE) Airborne Simulator (GCAS), and Geostationary Trace gas and Aerosol Sensory Optimization (GeoTASO)) for the preparation of the Tropospheric Emissions; Monitoring of Pollution (TEMPO) observations for monitoring air quality from space. LISTOS also helped collaborators in the validation of Tropospheric Monitoring Instrument (TROPOMI) science products, with use of airborne- and ground-based measurements of ozone, NO2, and HCHO.",
-            "title": "LISTOS Bronx Pfizer Ground Site Data",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSuborbital%2FLISTOS%2FGround_BronxPfizer_Data_1",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSuborbital%2FLISTOS%2FGround_BronxPfizer_Data_1",
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
-                    "downloadURL": "https://doi.org/10.5067/Suborbital/LISTOS/Ground_BronxPfizer_Data_1",
-                    "description": "DOI data set landing page for LISTOS_Ground_BronxPfizer_Data_1",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for LISTOS_Ground_BronxPfizer_Data_1",
+                    "downloadURL": "https://doi.org/10.5067/Suborbital/LISTOS/Ground_BronxPfizer_Data_1",
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
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1981386910-LARC_ASDC",
-                    "description": "Earthdata Search for LISTOS_Ground_BronxPfizer_Data_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for LISTOS_Ground_BronxPfizer_Data_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1981386910-LARC_ASDC",
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
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/LISTOS/Ground_BronxPfizer_Data_1/",
-                    "description": "ASDC Direct Data Download for LISTOS_Ground_BronxPfizer_Data_1",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for LISTOS_Ground_BronxPfizer_Data_1",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/LISTOS/Ground_BronxPfizer_Data_1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 }
             ],
+            "identifier": "C1981386910-LARC_ASDC",
+            "issued": "2020-09-08",
+            "keyword": [
+                "atmosphere",
+                "atmospheric chemistry",
+                "earth science",
+                "air quality"
+            ],
+            "landingPage": "https://doi.org/10.5067/Suborbital/LISTOS/Ground_BronxPfizer_Data_1",
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
+            "temporal": "2018-01-01T00:00:00Z/2018-11-13T23:59:59.999Z",
             "theme": [
                 "LISTOS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "LISTOS Bronx Pfizer Ground Site Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://techport.nasa.gov/view/10864",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2010-01-01",
-            "temporal": "2010-01-01T00:00:00Z/2014-01-01T00:00:00Z",
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
-                "project"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Goutam Chattopadhyay",
                 "hasEmail": "mailto:goutam.chattopadhyay@jpl.nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Science Mission Directorate"
-            },
-            "identifier": "TECHPORT_10864",
             "description": "\"We are proposing a new concept of integrated component development technology at submillimeter wavelengths that will dramatically simplify the fabrication, assembly, and integration of large focal plane arrays and imagers. This technology has the potential to significantly increase the pixel count of detector arrays and reduce the mass, volume, and complexity of array receivers for a broad range of applications in astrophysics and earth sciences. \n\n\n\nWe will develop and demonstrate a highly integrated silicon-micromachined array receiver at  1.9 THz based on advanced dual-polarized, sideband-separating, balanced heterodyne mixers. The receiver front-end will be integrated with a novel micro-lens antenna array. We will design full-waveguide-band 90-degree quadrature hybrids, orthomode transducers (OMT), polarization twists, in-phase power splitters, and directional couplers at 1.9 THz; fabricate them using deep reactive ion etching (DRIE) based silicon micromachining, integrate them with existing HEB mixers at 1.9 THz; and test and fully characterize them in our laboratory.\n\n\n\nThe scientific importance of high-resolution spectroscopic observations at submillimeter wavelengths is underscored by the key role of heterodyne spectrometers in the ESA cornerstone Herschel Space Observatory as well as the ground-based ALMA and airborne SOFIA.  Star formation and key phases of galaxy evolution occur in region enshrouded by dust that obscures them at infrared and optical wavelengths, while the temperature range of the interstellar medium of ten to a few thousand Kelvin in these regions excites a wealth of submillimeter-wave spectral lines. With high-resolution spectroscopy, resolved line profiles reveal the dynamics of star formation, directly revealing details of turbulence, outflows, and core collapse.  Observations of emission from ionized species such as C+ at 1900.53690 GHz (158 um), allow one to directly measure the cooling of the diffuse component of the interstellar m",
-            "title": "Silicon Micromachined Heterodyne Array Receiver at 1.9 THz Project",
-            "programCode": [
-                "026:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "http://techport.nasa.gov/xml-api/10864",
                     "mediaType": "application/xml"
                 }
-            ]
+            ],
+            "identifier": "TECHPORT_10864",
+            "issued": "2010-01-01",
+            "keyword": [
+                "active",
+                "project"
+            ],
+            "landingPage": "http://techport.nasa.gov/view/10864",
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
+            "temporal": "2010-01-01T00:00:00Z/2014-01-01T00:00:00Z",
+            "title": "Silicon Micromachined Heterodyne Array Receiver at 1.9 THz Project"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-M-OSIWAC-2-MARS-MARSSWINGBY-V2.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This CODMAC level 2 data set contains uncalibrated image data in DN unit,  acquired by the OSIRIS Wide Angle Camera on the Rosetta spacecraft  during the MARS SWING-BY mission phase, covering the period  from 2006-07-29T00:00:00.000 to 2007-05-28T23:59:59.000. The prime target is planet Mars. This version V2.0 supersedes previous deliveries of the same dataset with the following changes since the last version: Reprocessed dataset after October 2018 PSA/PDS external peer review.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-m-osiwac-2-mars-marsswingby-v2.0",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2021-05-21",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "deimos",
                 "jupiter",
@@ -1332140,257 +1332142,264 @@
                 "dark",
                 "international rosetta mission"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-M-OSIWAC-2-MARS-MARSSWINGBY-V2.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-m-osiwac-2-mars-marsswingby-v2.0",
-            "description": "This CODMAC level 2 data set contains uncalibrated image data in DN unit,  acquired by the OSIRIS Wide Angle Camera on the Rosetta spacecraft  during the MARS SWING-BY mission phase, covering the period  from 2006-07-29T00:00:00.000 to 2007-05-28T23:59:59.000. The prime target is planet Mars. This version V2.0 supersedes previous deliveries of the same dataset with the following changes since the last version: Reprocessed dataset after October 2018 PSA/PDS external peer review.",
-            "title": "ROSETTA-ORBITER MARS OSIWAC 2 MARS EDR V2.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER MARS OSIWAC 2 MARS EDR V2.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/2139",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Thompson, D.R., D.J. Jensen, J.W. Chapman, M. Simard, and E. Greenberg. 2023. Delta-X: AVIRIS-NG L2B BRDF-Adjusted Surface Reflectance, MRD, LA, 2021, V2. ORNL DAAC, Oak Ridge, Tennessee, USA. https://doi.org/10.3334/ORNLDAAC/2139",
-            "issued": "2024-01-12",
-            "temporal": "2021-03-27T00:00:00Z/2021-09-25T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-01-16",
-            "keyword": [
-                "geomorphic landforms/processes",
-                "surface radiative properties",
-                "earth science",
-                "erosion/sedimentation",
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
-            "identifier": "C2707162636-ORNL_CLOUD",
             "description": "This data provides AVIRIS-NG Bidirectional Reflectance Distribution Function (BRDF) and sunglint-corrected surface spectral reflectance images over the Atchafalaya and Terrebonne basins of the Mississippi River Delta (MRD) of coastal Louisiana, USA. Flights were acquired during the Spring and Fall 2021 deployments of the Delta-X campaign. The imagery was acquired by the Airborne Visible/Infrared Imaging Spectrometer - Next Generation (AVIRIS-NG) from 2021-03-27 to 2021-04-06 and 2021-08-18 to 2021-09-25. Reflectance data are provided as file sets for each flight line. In addition, ten files of mosaicked flight lines, by time period and over four locations (labeled Terre, Atcha, TerreEast, and Bara), are included. Files are presented as compressed (*.zip) files, containing binary ENVI image and header files. Only land pixels were corrected and mask files for the mosaic file coverage showing presence/absence of water are also included. For the Delta-X mission, these data serve to better understand rates of soil erosion, accretion, and creation in the delta system, with the goal of building better models of how river deltas will behave under relative sea level rise.",
-            "graphic-preview-description": "Figure 1: A BRDF and sunglint-corrected image of the Atchafalaya basin.",
-            "title": "Delta-X: AVIRIS-NG L2B BRDF-Adjusted Surface Reflectance, MRD, LA, 2021, V2",
-            "graphic-preview-file": "https://daac.ornl.gov/DELTAX/guides/DeltaX_L2A_AVIRIS-NG_BRDF_V2_Fig1.jpg",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F2139",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F2139",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/deltax/DeltaX_L2A_AVIRIS-NG_BRDF_V2/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/deltax/DeltaX_L2A_AVIRIS-NG_BRDF_V2/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/DELTAX/guides/DeltaX_L2A_AVIRIS-NG_BRDF_V2.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/DELTAX/guides/DeltaX_L2A_AVIRIS-NG_BRDF_V2.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/2139",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/2139",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/deltax/DeltaX_L2A_AVIRIS-NG_BRDF_V2/comp/DeltaX_L2A_AVIRIS-NG_BRDF_V2.pdf",
-                    "description": "Delta-X: AVIRIS-NG L2B BRDF-Adjusted Surface Reflectance, MRD, LA, 2021, V2: DeltaX_L2A_AVIRIS-NG_BRDF_V2.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "Delta-X: AVIRIS-NG L2B BRDF-Adjusted Surface Reflectance, MRD, LA, 2021, V2: DeltaX_L2A_AVIRIS-NG_BRDF_V2.pdf",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/deltax/DeltaX_L2A_AVIRIS-NG_BRDF_V2/comp/DeltaX_L2A_AVIRIS-NG_BRDF_V2.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://daac.ornl.gov/DELTAX/guides/DeltaX_L2A_AVIRIS-NG_BRDF_V2_Fig1.jpg",
-                    "description": "Figure 1: A BRDF and sunglint-corrected image of the Atchafalaya basin.",
                     "@type": "dcat:Distribution",
+                    "description": "Figure 1: A BRDF and sunglint-corrected image of the Atchafalaya basin.",
+                    "downloadURL": "https://daac.ornl.gov/DELTAX/guides/DeltaX_L2A_AVIRIS-NG_BRDF_V2_Fig1.jpg",
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
+            "graphic-preview-description": "Figure 1: A BRDF and sunglint-corrected image of the Atchafalaya basin.",
+            "graphic-preview-file": "https://daac.ornl.gov/DELTAX/guides/DeltaX_L2A_AVIRIS-NG_BRDF_V2_Fig1.jpg",
+            "identifier": "C2707162636-ORNL_CLOUD",
+            "issued": "2024-01-12",
+            "keyword": [
+                "geomorphic landforms/processes",
+                "surface radiative properties",
+                "earth science",
+                "erosion/sedimentation",
+                "land surface"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/2139",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2024-01-16",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "ORNL_DAAC"
+            },
             "spatial": "-91.59 29.05 -89.67 29.85",
+            "temporal": "2021-03-27T00:00:00Z/2021-09-25T23:59:59Z",
             "theme": [
                 "Delta-X",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Delta-X: AVIRIS-NG L2B BRDF-Adjusted Surface Reflectance, MRD, LA, 2021, V2"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewBundle.jsp?identifier=urn%3Anasa%3Apds%3Ainsight_documents&version=2.0",
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
-                "insight mars lander mission"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "The Mars InSight Lander document bundle includes a collection of documents for each of the InSight science experiments and a collection of documents pertaining to the mission as a  whole.",
+            "identifier": "urn:nasa:pds:insight_documents",
+            "issued": "2021-05-21",
+            "keyword": [
+                "mars",
+                "insight mars lander mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewBundle.jsp?identifier=urn%3Anasa%3Apds%3Ainsight_documents&version=2.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:insight_documents",
-            "description": "The Mars InSight Lander document bundle includes a collection of documents for each of the InSight science experiments and a collection of documents pertaining to the mission as a  whole.",
-            "title": "Mars InSight Lander Document Archive",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "Mars InSight Lander Document Archive"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1086",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Mayorga, E., M.G. Logsdon, M.V.R. Ballester, and J.E. Richey. 2012. LBA-ECO CD-06 Amazon River Basin Land and Stream Drainage Direction Maps. ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/1086",
-            "issued": "2023-10-03",
-            "temporal": "1940-01-01T00:00:00Z/1960-01-01T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-10-10",
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
-            "identifier": "C2780118467-ORNL_CLOUD",
             "description": "This data set provides high-resolution (~500 m) gridded land and stream drainage direction maps for the Amazon River basin, excluding the Rio Tocantins basin. These maps are the result of a new topography-independent analysis method (Mayorga et al., 2005) using the vector river network from the Digital Chart of the World (DCW, Danko, 1992) to create a high-resolution flow direction map. The data products include (1) a stream network coverage with stream order assigned to each reach; (2) the basin boundaries of the major tributaries to the Amazon mainstem; (3) the mouths; and (4) the source points of these tributaries.There are 7 ESRI ArcGIS shapefiles provided in compressed *.zip format and 4 GeoTiff image files with this data set.",
-            "graphic-preview-description": "Browse Image",
-            "title": "LBA-ECO CD-06 Amazon River Basin Land and Stream Drainage Direction Maps",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/lba_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1086",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1086",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/lba/carbon_dynamics/CD06_Camrex/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/lba/carbon_dynamics/CD06_Camrex/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/LBA/guides/CD06_CAMREX.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/LBA/guides/CD06_CAMREX.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1086",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1086",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/carbon_dynamics/CD06_Camrex/comp/CD06_Camrex.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/carbon_dynamics/CD06_Camrex/comp/CD06_Camrex.pdf",
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
+            "identifier": "C2780118467-ORNL_CLOUD",
+            "issued": "2023-10-03",
+            "keyword": [
+                "surface water",
+                "earth science",
+                "terrestrial hydrosphere"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1086",
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
             "spatial": "-80.5 -20.5 -48.5 6.0",
+            "temporal": "1940-01-01T00:00:00Z/1960-01-01T23:59:59Z",
             "theme": [
                 "LBA-ECO",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "LBA-ECO CD-06 Amazon River Basin Land and Stream Drainage Direction Maps"
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
+                    "downloadURL": "https://pds.jpl.nasa.gov/tools/subscription_service/SS-20070815.shtml",
+                    "mediaType": "application/html"
+                }
             ],
+            "identifier": "NASA-706",
+            "issued": "2018-06-25",
             "keyword": [
                 "radar",
                 "uvis",
@@ -1332402,173 +1332411,166 @@
                 "spice",
                 "cda"
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
-            "identifier": "NASA-706",
-            "description": "CDA, CIRS, ISS, RADAR, RSS, UVIS, VIMS, SPICE",
-            "title": "PDS Cassini Data Release 9",
-            "programCode": [
-                "026:005"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://pds.jpl.nasa.gov/tools/subscription_service/SS-20070815.shtml",
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
+            "title": "PDS Cassini Data Release 9"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=SDU-C%2FCAL-NAVCAM-3-NEXT-TEMPEL1-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This data set contains RDR pre- and post-encounter and encounter images taken by the Stardust Navigation Camera during the encounter with comet 9P/Tempel 1 (1867 G1), plus calibration images taken throughout the Stardust-NExT mission.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.sdu-c-cal-navcam-3-next-tempel1-v1.0_rxvq-znjm",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "next",
                 "9p/tempel 1 (1867 g1)",
                 "calibration"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=SDU-C%2FCAL-NAVCAM-3-NEXT-TEMPEL1-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.sdu-c-cal-navcam-3-next-tempel1-v1.0_rxvq-znjm",
-            "description": "This data set contains RDR pre- and post-encounter and encounter images taken by the Stardust Navigation Camera during the encounter with comet 9P/Tempel 1 (1867 G1), plus calibration images taken throughout the Stardust-NExT mission.",
-            "title": "STARDUST 9P/TEMPEL 1 NAVCAM 3 NEXT V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "STARDUST 9P/TEMPEL 1 NAVCAM 3 NEXT V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ADEOS-I/OCTS/L3B/CHL/2014",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/GSFC/SED/ESD/GCDC/OB.DAAC. https://doi.org/10.5067/ADEOS-I/OCTS/L3B/CHL/2014.",
-            "issued": "2017-01-11",
-            "temporal": "1996-11-01T00:00:00Z/1997-06-30T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2018-10-10",
-            "keyword": [
-                "oceans",
-                "earth science",
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
-            "identifier": "C1200034361-OB_DAAC",
             "description": "On August 17, 1996, the Japanese Space Agency (NASDA - National Space Development Agency)\nlaunched the Advanced Earth Observing Satellite (ADEOS). ADEOS was in a descending, Sun\nsynchronous orbit with a nominal equatorial crossing time of 10:30 a.m. Amoung the\ninstruments carried aboard the ADEOS spacecraft was the Ocean Color and Temperature\nScanner (OCTS). OCTS is an optical radiometer with 12 bands covering the visible, near\ninfrared and thermal infrared regions. (Eight of the bands are in the VIS/NIR. These are\nthe only bands calibrated and processed by the OBPG) OCTS has a swath width of\napproximately 1400 km, and a nominal nadir resolution of 700 m. The instrument operated\nat three tilt states (20 degrees aft, nadir and 20 degrees fore), similar to SeaWiFS.",
-            "title": "ADEOS-I Ocean Color and Temperature Scanner (OCTS) Chlorophyll (CHL) Global Binned Data",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FADEOS-I%2FOCTS%2FL3B%2FCHL%2F2014",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FADEOS-I%2FOCTS%2FL3B%2FCHL%2F2014",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://oceandata.sci.gsfc.nasa.gov/OCTS/L3BIN/",
-                    "description": "NASA Ocean Color Web - Data Distribution Site",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Ocean Color Web - Data Distribution Site",
+                    "downloadURL": "https://oceandata.sci.gsfc.nasa.gov/OCTS/L3BIN/",
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
-                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/data/10.5067/ADEOS-I/OCTS/L3B/CHL/2014",
-                    "description": "OB.DAAC OCTS ADEOS-I L3B Chlorophyll (CHL) Landing Page",
                     "@type": "dcat:Distribution",
+                    "description": "OB.DAAC OCTS ADEOS-I L3B Chlorophyll (CHL) Landing Page",
+                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/data/10.5067/ADEOS-I/OCTS/L3B/CHL/2014",
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
+            "identifier": "C1200034361-OB_DAAC",
+            "issued": "2017-01-11",
+            "keyword": [
+                "oceans",
+                "earth science",
+                "ocean chemistry"
+            ],
+            "landingPage": "https://doi.org/10.5067/ADEOS-I/OCTS/L3B/CHL/2014",
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
+            "title": "ADEOS-I Ocean Color and Temperature Scanner (OCTS) Chlorophyll (CHL) Global Binned Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-X-OSINAC-4-CR2-CHECKOUT-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This CODMAC level 4 data set contains radiometric calibrated and geometric distortion corrected (resampled) image data in W/m^2/sr/nm,  acquired by the OSIRIS Narrow Angle Camera on the Rosetta spacecraft  during the CRUISE 2 mission phase, covering the period  from 2005-04-05T00:00:00.000 to 2006-07-28T23:59:59.000. The prime objective was commissioning / calibration. Several targets of opportunity were observed, but none of them is identifiable as prime target. This version V1.0 is the first version of this dataset.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-x-osinac-4-cr2-checkout-v1.0",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2021-05-21",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "16 cyg b",
                 "starfield",
@@ -1332576,411 +1332578,389 @@
                 "9p/tempel 1 (1867 g1)",
                 "international rosetta mission"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-X-OSINAC-4-CR2-CHECKOUT-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-x-osinac-4-cr2-checkout-v1.0",
-            "description": "This CODMAC level 4 data set contains radiometric calibrated and geometric distortion corrected (resampled) image data in W/m^2/sr/nm,  acquired by the OSIRIS Narrow Angle Camera on the Rosetta spacecraft  during the CRUISE 2 mission phase, covering the period  from 2005-04-05T00:00:00.000 to 2006-07-28T23:59:59.000. The prime objective was commissioning / calibration. Several targets of opportunity were observed, but none of them is identifiable as prime target. This version V1.0 is the first version of this dataset.",
-            "title": "ROSETTA-ORBITER CHECKOUT OSINAC 4 CR2 RDR V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER CHECKOUT OSINAC 4 CR2 RDR V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/HRSFWSRE4IWV",
             "citation": "Chris Barnet. 2019-12-15. SNDRSNIML3SDCCPN. Version 2. Sounder SIPS: Suomi NPP CrIMSS Level 3 Specific Quality Control Gridded Daily CLIMCAPS Normal Spectral Resolution V2. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/HRSFWSRE4IWV. https://disc.gsfc.nasa.gov/datacollection/SNDRSNIML3SDCCPN_2.html. Digital Science Data.",
-            "issued": "2012-04-19",
-            "temporal": "2012-04-19T00:00:00Z/2024-05-20T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2021-05-22",
-            "references": [
-                "https://doi.org/10.3390/rs11101227",
-                "https://doi.org/10.1109/TGRS.2012.2220369",
-                "https://doi.org/10.1016/S0022-4073(97)00169-6",
-                "https://doi.org/10.1109/TGRS.2002.808236",
-                "https://doi.org/10.1029/2005/JD007020",
-                "https://doi.org/10.5194/amt-13-4437-2020"
-            ],
-            "keyword": [
-                "atmosphere",
-                "land surface",
-                "earth science",
-                "ocean temperature",
-                "atmospheric pressure",
-                "atmospheric chemistry",
-                "surface thermal properties",
-                "precipitation",
-                "atmospheric water vapor",
-                "atmospheric temperature",
-                "atmospheric radiation",
-                "altitude",
-                "oceans",
-                "clouds",
-                "surface radiative properties",
-                "air quality"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Lena Iredell",
                 "hasEmail": "mailto:lena.iredell@nasa.gov"
             },
+            "creator": "Chris Barnet",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C1692982081-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Not provided"
-            },
             "description": "The CLIMCAPS (Community Long-term Infrared Microwave Coupled Product System) algorithm is used to analyze data from the Cross-track Infrared Sounder/Advanced Technology Microwave Sounder (CrIS/ATMS) instruments, also known as CrIMSS (Cross-track Infrared and Microwave Sounding Suite). The CrIS/ATMS instruments used for this product are on board the Suomi National Polar-orbiting Partnership (SNPP) platform and use the Normal Spectral Resolution (NSR) data. The CrIS instrument is a Fourier transform spectrometer with a total of 1305 NSR infrared sounding channels covering the longwave (655-1095 cm-1), midwave (1210-1750 cm-1), and shortwave (2155-2550 cm-1) spectral regions. The ATMS instrument  is a cross-track scanner with 22 channels in spectral bands from 23 GHz through 183 GHz.\n \nThe CLIMCAPS algorithm uses an Optimal Estimation methodology and uses an a-priori first guess to start the process. A CLIMCAPS sounding is comprised of a set of parameters that characterizes the full atmospheric state and includes a variety of geophysical parameters derived from the CrIMSS data. These include surface temperature and infrared emissivity; full atmosphere profiles of temperature, water vapor and ozone; infrared effective cloud top characteristics; carbon monoxide, methane, carbon dioxide, sulfur dioxide, nitrous oxide, and nitric acid.\n\nThis daily one degree latitude by one degree longitude level-3 product starts with level-2 retrieval products with QC values of 0 (best), 1 (good), and 2 (don't use) which are provided for each variable and applying specific QC methodology. Specific QC accepts profile level from the top of the atmosphere down to the level where the QC determines that it is still good. Below this level, the data is rejected.\n\nWARNING: To users of the derived product \u201cco_mmr_midtrop\u201d (carbon monoxide mass mixing ratio to dry air [kg/kg] at ~500 hPa). This variable has a significant bias due to a conversion error: the molecular weight of carbon dioxide (CO2, 48.01 g/mol) was used instead of carbon monoxide (CO, 28.01 g/mol). To correct, simply multiply \u201cco_mmr_midtrop\u201d by 28.01/48.01. Alternatively, derive a profile of mass mixing ratio from scratch using the retrieved column density values (\u201cmol_lay/co_mol_lay\u201d) in the Level 2 files. For further questions or concerns please contact the Sounder SIPS at: sounder.sips@jpl.nasa.gov",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "SNDRSNIML3SDCCPN",
-            "creator": "Chris Barnet",
-            "graphic-preview-description": "Sample plot of CrIS/ATMS Level 3 daily surface skin temperature (K).",
-            "title": "Sounder SIPS: Suomi NPP CrIMSS Level 3 Specific Quality Control Gridded Daily CLIMCAPS Normal Spectral Resolution V2 (SNDRSNIML3SDCCPN) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/SNDRSNIML3SDCCPN_2.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FHRSFWSRE4IWV",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FHRSFWSRE4IWV",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/SNDRSNIML3SDCCPN_2.png",
-                    "description": "Sample plot of CrIS/ATMS Level 3 daily surface skin temperature (K).",
                     "@type": "dcat:Distribution",
+                    "description": "Sample plot of CrIS/ATMS Level 3 daily surface skin temperature (K).",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/SNDRSNIML3SDCCPN_2.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/SNDRSNIML3SDCCPN_2.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/SNDRSNIML3SDCCPN_2.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sounder.gesdisc.eosdis.nasa.gov/data/SNPP_Sounder_Level3/SNDRSNIML3SDCCPN.2",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://sounder.gesdisc.eosdis.nasa.gov/data/SNPP_Sounder_Level3/SNDRSNIML3SDCCPN.2",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sounder.gesdisc.eosdis.nasa.gov/opendap/SNPP_Sounder_Level3/SNDRSNIML3SDCCPN.2/",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://sounder.gesdisc.eosdis.nasa.gov/opendap/SNPP_Sounder_Level3/SNDRSNIML3SDCCPN.2/",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=SNDRSNIML3SDCCPN+2",
-                    "description": "Search the Earthdata website",
                     "@type": "dcat:Distribution",
+                    "description": "Search the Earthdata website",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=SNDRSNIML3SDCCPN+2",
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
                 }
             ],
+            "graphic-preview-description": "Sample plot of CrIS/ATMS Level 3 daily surface skin temperature (K).",
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/SNDRSNIML3SDCCPN_2.png",
+            "identifier": "C1692982081-GES_DISC",
+            "issued": "2012-04-19",
+            "keyword": [
+                "atmosphere",
+                "land surface",
+                "earth science",
+                "ocean temperature",
+                "atmospheric pressure",
+                "atmospheric chemistry",
+                "surface thermal properties",
+                "precipitation",
+                "atmospheric water vapor",
+                "atmospheric temperature",
+                "atmospheric radiation",
+                "altitude",
+                "oceans",
+                "clouds",
+                "surface radiative properties",
+                "air quality"
+            ],
+            "landingPage": "https://doi.org/10.5067/HRSFWSRE4IWV",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2021-05-22",
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
+                "https://doi.org/10.1016/S0022-4073(97)00169-6",
+                "https://doi.org/10.1109/TGRS.2002.808236",
+                "https://doi.org/10.1029/2005/JD007020",
+                "https://doi.org/10.5194/amt-13-4437-2020"
+            ],
+            "release-place": "Greenbelt, MD, USA",
+            "series-name": "SNDRSNIML3SDCCPN",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2012-04-19T00:00:00Z/2024-05-20T00:00:00Z",
             "theme": [
                 "SUOMI-NPP",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Sounder SIPS: Suomi NPP CrIMSS Level 3 Specific Quality Control Gridded Daily CLIMCAPS Normal Spectral Resolution V2 (SNDRSNIML3SDCCPN) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.7927/H4Z60M4Z",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Center for International Earth Science Information Network - CIESIN - Columbia University. 2018-12-31. Gridded Population of the World, Version 4 (GPWv4): Land and Water Area, Revision 11. Version 4.11. Palisades, NY. Archived by National Aeronautics and Space Administration, U.S. Government, NASA Socioeconomic Data and Applications Center (SEDAC). https://doi.org/10.7927/H4Z60M4Z. https://doi.org/10.7927/H4Z60M4Z.",
-            "issued": "2018-12-31",
-            "temporal": "2010-07-01T00:00:00Z/2010-07-01T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2018-12-31",
-            "references": [
-                "https://doi.org/10.7927/H45M63M9",
-                "https://doi.org/10.1080/23754931.2015.1014272",
-                "https://doi.org/10.7927/H4Z03642",
-                "https://doi.org/10.7927/H4BC3WMT",
-                "https://doi.org/10.7927/H42Z13KG",
-                "https://doi.org/10.7927/H4TD9VDP",
-                "https://doi.org/10.7927/H4JW8BX5",
-                "https://doi.org/10.7927/H49C6VHW",
-                "https://doi.org/10.7927/H45Q4T5F",
-                "https://doi.org/10.7927/H46M34XX",
-                "https://doi.org/10.7927/H4PN93PB",
-                "https://doi.org/10.7927/H4F47M65"
-            ],
-            "keyword": [
-                "land use/land cover",
-                "earth science",
-                "surface water",
-                "terrestrial hydrosphere",
-                "land surface"
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
-            "identifier": "C1597156945-SEDAC",
-            "description": "The Gridded Population of the World, Version 4 (GPWv4): Land and Water Area, Revision 11 consists of two rasters that measure surface areas of land and water in square kilometers per pixel. The Land Area raster provides estimates of the land area, excluding permanent ice and water, within each pixel, and was used to calculate the population density rasters. The Water Area raster provides estimates of the water area (permanent ice and water) within each pixel. The sum of land area and water area of a pixel equals the total surface area of that pixel. The data files were produced as global rasters at 30 arc-second (~1 km at the equator) resolution. To enable faster global processing, and in support of research commUnities, the 30 arc-second data were aggregated to 2.5 arc-minute, 15 arc-minute, 30 arc-minute and 1 degree resolutions.",
-            "release-place": "Palisades, NY",
-            "graphic-preview-description": "Maps Download Page",
             "creator": "Center for International Earth Science Information Network - CIESIN - Columbia University",
-            "title": "Gridded Population of the World, Version 4 (GPWv4): Land and Water Area, Revision 11",
-            "graphic-preview-file": "https://sedac.ciesin.columbia.edu/data/set/gpw-v4-land-water-area-rev11/maps",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The Gridded Population of the World, Version 4 (GPWv4): Land and Water Area, Revision 11 consists of two rasters that measure surface areas of land and water in square kilometers per pixel. The Land Area raster provides estimates of the land area, excluding permanent ice and water, within each pixel, and was used to calculate the population density rasters. The Water Area raster provides estimates of the water area (permanent ice and water) within each pixel. The sum of land area and water area of a pixel equals the total surface area of that pixel. The data files were produced as global rasters at 30 arc-second (~1 km at the equator) resolution. To enable faster global processing, and in support of research commUnities, the 30 arc-second data were aggregated to 2.5 arc-minute, 15 arc-minute, 30 arc-minute and 1 degree resolutions.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.7927%2FH4Z60M4Z",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.7927%2FH4Z60M4Z",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/downloads/maps/gpw-v4/gpw-v4-land-water-area-rev11/gpw-v4-land-water-area-rev11-land-thumbnail.jpg",
-                    "description": "Sample browse graphic of the data set.",
                     "@type": "dcat:Distribution",
+                    "description": "Sample browse graphic of the data set.",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/downloads/maps/gpw-v4/gpw-v4-land-water-area-rev11/gpw-v4-land-water-area-rev11-land-thumbnail.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/gpw-v4-land-water-area-rev11/data-download",
-                    "description": "Data Download Page",
                     "@type": "dcat:Distribution",
+                    "description": "Data Download Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/gpw-v4-land-water-area-rev11/data-download",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/gpw-v4-land-water-area-rev11/maps",
-                    "description": "Maps Download Page",
                     "@type": "dcat:Distribution",
+                    "description": "Maps Download Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/gpw-v4-land-water-area-rev11/maps",
+                    "mediaType": "text/html",
                     "title": "Get a related map visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://sedac.ciesin.columbia.edu/data/set/gpw-v4-land-water-area-rev11/docs",
-                    "description": "Documentation Page",
                     "@type": "dcat:Distribution",
+                    "description": "Documentation Page",
+                    "downloadURL": "http://sedac.ciesin.columbia.edu/data/set/gpw-v4-land-water-area-rev11/docs",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/gpw-v4-land-water-area-rev11/maps/services",
-                    "description": "Web Map Service Page",
                     "@type": "dcat:Distribution",
+                    "description": "Web Map Service Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/gpw-v4-land-water-area-rev11/maps/services",
+                    "mediaType": "text/html",
                     "title": "Use Web Map Service (WMS) to download the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/gpw-v4-land-water-area-rev11",
-                    "description": "Data Set\u00a0Overview Page",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set\u00a0Overview Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/gpw-v4-land-water-area-rev11",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "graphic-preview-description": "Maps Download Page",
+            "graphic-preview-file": "https://sedac.ciesin.columbia.edu/data/set/gpw-v4-land-water-area-rev11/maps",
+            "identifier": "C1597156945-SEDAC",
+            "issued": "2018-12-31",
+            "keyword": [
+                "land use/land cover",
+                "earth science",
+                "surface water",
+                "terrestrial hydrosphere",
+                "land surface"
+            ],
+            "landingPage": "https://doi.org/10.7927/H4Z60M4Z",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2018-12-31",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "SEDAC"
+            },
+            "references": [
+                "https://doi.org/10.7927/H45M63M9",
+                "https://doi.org/10.1080/23754931.2015.1014272",
+                "https://doi.org/10.7927/H4Z03642",
+                "https://doi.org/10.7927/H4BC3WMT",
+                "https://doi.org/10.7927/H42Z13KG",
+                "https://doi.org/10.7927/H4TD9VDP",
+                "https://doi.org/10.7927/H4JW8BX5",
+                "https://doi.org/10.7927/H49C6VHW",
+                "https://doi.org/10.7927/H45Q4T5F",
+                "https://doi.org/10.7927/H46M34XX",
+                "https://doi.org/10.7927/H4PN93PB",
+                "https://doi.org/10.7927/H4F47M65"
+            ],
+            "release-place": "Palisades, NY",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2010-07-01T00:00:00Z/2010-07-01T00:00:00Z",
             "theme": [
                 "GPW",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Gridded Population of the World, Version 4 (GPWv4): Land and Water Area, Revision 11"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC1-0567-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 1 phase 2014-11-20 to 2015-03-10. It is a Global Gravity measurement at the comet 67P and covers the time 2015-02-07T03:35:40.000 to 2015-02-07T08:54:12.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc1-0567-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC1-0567-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc1-0567-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 1 phase 2014-11-20 to 2015-03-10. It is a Global Gravity measurement at the comet 67P and covers the time 2015-02-07T03:35:40.000 to 2015-02-07T08:54:12.000.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 1 0567 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 1 0567 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=P11-J-CRT-4-SUMM-FLUX-15MIN-V1.0",
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
-                "pioneer 11"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "not applicable",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.p11-j-crt-4-summ-flux-15min-v1.0_ry57-593e",
+            "issued": "2018-06-26",
+            "keyword": [
+                "jupiter",
+                "pioneer 11"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=P11-J-CRT-4-SUMM-FLUX-15MIN-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.p11-j-crt-4-summ-flux-15min-v1.0_ry57-593e",
-            "description": "not applicable",
-            "title": "P11 JUPITER CRT ELECTRON/PROTON/ION FLUX 15 MIN AVGS V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "P11 JUPITER CRT ELECTRON/PROTON/ION FLUX 15 MIN AVGS V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=GO-V-EPD-2-SAMP-PAD-V1.0",
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
-                "venus",
-                "galileo"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This data set contains sixteen sector\nrate data for the energetic particle detector obtained from the LEMMS\ntelescope during the time of significant activity during the Venus\nencounter.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.go-v-epd-2-samp-pad-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "venus",
+                "galileo"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=GO-V-EPD-2-SAMP-PAD-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.go-v-epd-2-samp-pad-v1.0",
-            "description": "This data set contains sixteen sector\nrate data for the energetic particle detector obtained from the LEMMS\ntelescope during the time of significant activity during the Venus\nencounter.",
-            "title": "GO VEN EPD EDITED SAMPLE PITCH ANGLE DISTRIBUTIONS V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "GO VEN EPD EDITED SAMPLE PITCH ANGLE DISTRIBUTIONS V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/AIRCRAFT/AIRMSPI/IMPACT-PM/RADIANCE/TERRAIN_v006",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2018-05-04. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/AIRCRAFT/AIRMSPI/IMPACT-PM/RADIANCE/TERRAIN_v006. http://eosweb.larc.nasa.gov/project/airmspi/airmspi_table.",
-            "issued": "2017-10-12",
-            "temporal": "2016-07-05T00:00:00Z/2016-07-08T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2018-06-25",
-            "keyword": [
-                "visible wavelengths",
-                "earth science",
-                "ultraviolet wavelengths",
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
-            "identifier": "C1517289469-LARC_ASDC",
             "description": "AirMSPI_ImPACT-PM_Terrain-projected_Georegistered_Radiance_Data is an AirMSPI terrain-projected georegistered radiance product acquired during the JPL and Caltech Imaging Polarimetric Assessment and Characterization of Tropospheric Particulate Matter (ImPACT-PM) flight campaign.\nAirMSPI Level 1B2 products contain radiometric and polarimetric images of clouds, aerosols, and the surface of the Earth. In particular, products contain map-projected data at 8 wavelengths: 355, 380, 445, 470, 555, 660, 865, and 935 nm. The data products include radiance, time, solar zenith, solar azimuth, view zenith, and view azimuth for all spectral bands. Wavelengths for which polarization information is available (470, 660, and 865 nm) and include the Stokes parameters Q and U, as well as degree of linear polarization (DOLP) and angle of linear polarization (AOLP). Q, U, and AOLP are reported relative to both the scattering- and view meridian planes. Files are distributed in HDF-EOS-5 format.\nThis release of AirMSPI data contains all targets acquired during the Imaging Polarimetric Assessment and Characterization of Tropospheric Particulate Matter (ImPACT-PM) flight campaign, which involved the ER-2 based out of Armstrong Flight Research Center in Palmdale, CA and a Navy Twin Otter flying the Caltech CIRPAS suite of instruments based out of Monterey, CA. The campaign was conducted to test a strategy to use multi-angle, spectro-polarimetric remote sensing to retrieve information on the distributions of atmospheric particle types, with emphasis on carbon-containing compounds, as a precursor to NASA\u2019s Multi-Angle Imager for Aerosols, an Earth Venture-Instrument currently in formulation. AirMSPI data were acquired from July 5 through July 8, 2016.",
-            "title": "AirMSPI verison 6 terrain-projected georegistered radiance product acquired during the ImPACT-PM flight campaign",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAIRCRAFT%2FAIRMSPI%2FIMPACT-PM%2FRADIANCE%2FTERRAIN_v006",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAIRCRAFT%2FAIRMSPI%2FIMPACT-PM%2FRADIANCE%2FTERRAIN_v006",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
@@ -1333044,108 +1333024,140 @@
                     "title": "Use OPeNDAP to access the dataset's data"
                 }
             ],
+            "identifier": "C1517289469-LARC_ASDC",
+            "issued": "2017-10-12",
+            "keyword": [
+                "visible wavelengths",
+                "earth science",
+                "ultraviolet wavelengths",
+                "spectral/engineering"
+            ],
+            "landingPage": "https://doi.org/10.5067/AIRCRAFT/AIRMSPI/IMPACT-PM/RADIANCE/TERRAIN_v006",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2018-06-25",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/LARC/SD/ASDC"
+            },
             "spatial": "-122.0 32.0 -117.0 39.0",
+            "temporal": "2016-07-05T00:00:00Z/2016-07-08T23:59:59Z",
             "theme": [
                 "AIRMSPI",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "AirMSPI verison 6 terrain-projected georegistered radiance product acquired during the ImPACT-PM flight campaign"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MEX-M-MRS-1%2F2%2F3-EXT3-3295-V1.0",
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
+            "description": "This is a Mars Express Radio Science data set, collected during the extended mission phase 2010-01-01 to 2012-12-31. It is a Global Gravity measurement and covers the time 2012-05-23T09:57:48.000 to 2012-05-23T13:55:40.500.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mex-m-mrs-1-2-3-ext3-3295-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "mars express",
+                "mars"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MEX-M-MRS-1%2F2%2F3-EXT3-3295-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mex-m-mrs-1-2-3-ext3-3295-v1.0",
-            "description": "This is a Mars Express Radio Science data set, collected during the extended mission phase 2010-01-01 to 2012-12-31. It is a Global Gravity measurement and covers the time 2012-05-23T09:57:48.000 to 2012-05-23T13:55:40.500.",
-            "title": "MARS EXPRESS MARS MRS 1/2/3\n                                     EXTENDED MISSION 3 3295 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "MARS EXPRESS MARS MRS 1/2/3\n                                     EXTENDED MISSION 3 3295 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1627523801-LARC.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "MISR Science Team (2004), Terra/MISR Level 1B, Radiometric camera-by-camera Cloud Mask subset for the UAE region, version 4, Hampton, VA, USA: NASA Atmospheric Science Data Center (ASDC), Accessed <author citing data inserts date here> at doi: TBD",
-            "issued": "2019-07-31",
-            "temporal": "2004-07-01T06:34:28.582Z/2006-10-05T08:15:37.747Z",
-            "@type": "dcat:Dataset",
-            "modified": "2019-08-01",
-            "keyword": [
-                "nasa"
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
-            "identifier": "C1627523801-LARC",
             "description": "Multi-angle Imaging SpectroRadiometer (MISR) is an instrument designed to view Earth with cameras pointed in 9 different directions. As the instrument flies overhead, each piece of Earth's surface below is successively imaged by all 9 cameras, in each of 4 wavelengths (blue, green, red, and near-infrared). The goal of MISR is to improve our understanding of the fate of sunlight in Earth environment, as well as distinguish different types of clouds, particles and surfaces. Specifically, MISR monitors the monthly, seasonal, and long-term trends in three areas: 1) amount and type of atmospheric particles (aerosols), including those formed by natural sources and by human activities; 2) amounts, types, and heights of clouds, and 3) distribution of land surface cover, including vegetation canopy structure. MISR radiometric camera-by-camera Cloud Mask subset for the UAE region V004 contains the Radiometric camera-by-camera Cloud Mask dataset. It is used to determine whether a scene is classified as clear or cloudy. A new parameter has been added to indicate dust over ocean. This version of the ESDT is used by MISR PGE 13.",
-            "title": "MISR radiometric camera-by-camera Cloud Mask subset for the UAE region V004",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/search/concepts/C1627523801-LARC.html",
-                    "description": "View this dataset on the CMR (Common Metadata Repository)",
                     "@type": "dcat:Distribution",
+                    "description": "View this dataset on the CMR (Common Metadata Repository)",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/search/concepts/C1627523801-LARC.html",
+                    "mediaType": "text/html",
                     "title": "CMR"
                 }
             ],
+            "identifier": "C1627523801-LARC",
+            "issued": "2019-07-31",
+            "keyword": [
+                "nasa"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1627523801-LARC.html",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2019-08-01",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/LARC/SD/ASDC"
+            },
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2004-07-01T06:34:28.582Z/2006-10-05T08:15:37.747Z",
             "theme": [
                 "UAE_2004",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "MISR radiometric camera-by-camera Cloud Mask subset for the UAE region V004"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://eros.usgs.gov/imagegallery/earth-art-2",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Charles Ichoku",
+                "hasEmail": "mailto:james.r.irons@nasa.gov"
+            },
+            "description": "The Earth Resources Observation and Science (EROS) Center manages this collection of forty-five new scenes developed for their aesthetic beauty, rather than for scientific value. The artists of this collection come from three sensors aboard satellites orbiting the Earth - Landsat 7, ASTER, and MODIS.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://eros.usgs.gov/imagegallery/earth-art-2",
+                    "mediaType": "application/html"
+                }
+            ],
+            "identifier": "NASA-910",
             "issued": "2014-04-29",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
             "keyword": [
                 "aster",
                 "images",
@@ -1333156,78 +1333168,41 @@
                 "earth as art",
                 "earth science"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Charles Ichoku",
-                "hasEmail": "mailto:james.r.irons@nasa.gov"
-            },
+            "landingPage": "http://eros.usgs.gov/imagegallery/earth-art-2",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "NASA-910",
-            "description": "The Earth Resources Observation and Science (EROS) Center manages this collection of forty-five new scenes developed for their aesthetic beauty, rather than for scientific value. The artists of this collection come from three sensors aboard satellites orbiting the Earth - Landsat 7, ASTER, and MODIS.",
-            "title": "Earth Resources Observation and Science (EROS) Center's Earth as Art Image Gallery 2",
-            "programCode": [
-                "026:005"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://eros.usgs.gov/imagegallery/earth-art-2",
-                    "mediaType": "application/html"
-                }
-            ],
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "Earth Resources Observation and Science (EROS) Center's Earth as Art Image Gallery 2"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/TRMM/TMPA/DAY/7",
             "citation": "Huffman, G.J., D.T. Bolvin, E.J. Nelkin, and R.F. Adler. Andrey Savtchenko. 2016-05-15. TRMM_3B42_Daily. Version 7. TRMM (TMPA) Precipitation L3 1 day 0.25 degree x 0.25 degree V7. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/TRMM/TMPA/DAY/7. https://disc.gsfc.nasa.gov/datacollection/TRMM_3B42_Daily_7.html. Digital Science Data.",
-            "issued": "2016-04-19",
-            "temporal": "1998-01-01T00:00:00Z/2022-01-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2016-04-29",
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
                 "fn": "GEORGE HUFFMAN",
                 "hasEmail": "mailto:George.J.Huffman@nasa.gov"
             },
+            "creator": "Huffman, G.J., D.T. Bolvin, E.J. Nelkin, and R.F. Adler",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C1239536905-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "TMPA (3B42_Daily) dataset have been discontinued as of Dec. 31, 2019, and users are strongly encouraged to shift to the successor IMERG dataset (doi: 10.5067/GPM/IMERGDF/DAY/06).\n\nThis daily accumulated precipitation product is generated from the research-quality 3-hourly TRMM Multi-Satellite Precipitation Analysis TMPA (3B42). It is produced at the NASA GES DISC, as a value added product.  Simple summation of valid retrievals in a grid cell is applied for the data day. The result is given in (mm). The beginning and ending time for every daily granule are listed in the file global attributes, and are taken correspondingly from the first and the last 3-hourly granules participating in the aggregation. Thus the time period covered by one daily granule amounts to 24 hours, which can be inspected in the file global attributes. \n\nCounts of valid retrievals for the day are provided for every variable, making it possible to compute conditional and unconditional mean precipitation for grid cells where less than 8 retrievals for the day are available.\n\nEfforts have been made to make the format of this  derived product as similar as possible to the new Global Precipitation Measurement CF-compliant file format.\n\nThe information provided here on the TRMM mission, and on the original 3-hr 3B42 product, remain relevant for this derived product. Note, however, this product is in netCDF-4 format.\n\n\n\nThe following describes the derivation in more details.\n\nThe daily accumulation is derived by summing *valid* retrievals in a grid cell for the data day. Since the 3-hourly source data are in mm/hr, a factor of 3 is applied to the sum. Thus, for every grid cell we have                \n\nPdaily     = 3 * SUM{Pi * 1[Pi valid]}, i=[1,Nf]\nPdaily_cnt = SUM{1[Pi valid]}\n\nwhere:\nPdaily          - Daily accumulation (mm)\nPi              - 3-hourly input, in (mm/hr)\nNf              - Number of 3-hourly files per day, Nf=8\n1[.]            - Indicator function; 1 when Pi is valid, 0 otherwise\nPdaily_cnt      - Number of valid retrievals in a grid cell per day.\n\nGrid cells for which Pdaily_cnt=0, are set to fill value in the Daily files.\nNote that Pi=0 is a valid value.\n\n\nOn occasion, the 3-hourly source data have fill values for Pi in a very few grid cells. The total accumulation for such grid cells is still issued, inspite of the likelihood that thus resulting accumulation has a larger uncertainty in representing the \"true\" daily total. These events are easily detectable using \"counts\" variables that contain Pdaily_cnt, whereby users can screen out any grid cells for which\n Pdaily_cnt less than Nf.\n\n\nThere are various ways the accumulated daily error could be estimated from the source 3-hourly error. In this release, the daily error provided in the data files is calculated as follows. First, squared 3-hourly errors are summed, and then square root of the sum is taken. Similarly to the precipitation, a factor of 3 is finally applied:\n\nPerr_daily = 3 * { SUM[ (Perr_i * 1[Perr_i valid])^2 ] }^0.5 , i=[1,Nf]\nNcnt_err   = SUM( 1[Perr_i valid] )\n\nwhere:\nPerr_daily\t- Magnitude of the daily accumulated error power, (mm)\nNcnt_err\t- The counts for the error variable\n\nThus computed Perr_daily represents the worst case scenario that assumes the error in the 3-hourly source data, which is given in mm/hr, accumulates first within the 3-hour period of the source data, and then continues to accumulate during the day. These values, however, can easily be converted to root mean square error estimate of the rainfall rate:\n\nrms_err =   { (Perr_daily/3) ^2 / Ncnt_err }^0.5\t(mm/hr)\n\n\nThis estimate assumes that the error given in the 3-hourly files is representative of the error of the rainfall rate (mm/hr) within the 3-hour window of the files, and it is random throughout the day. Note, this should be interpreted as the error of the rainfall rate (mm/hr) for the day, not the daily accumulation.",
-            "editor": "Andrey Savtchenko",
-            "series-name": "TRMM_3B42_Daily",
-            "creator": "Huffman, G.J., D.T. Bolvin, E.J. Nelkin, and R.F. Adler",
-            "title": "TRMM (TMPA) Precipitation L3 1 day 0.25 degree x 0.25 degree V7 (TRMM_3B42_Daily) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/GPM/browse/TRMM_3B42_Daily.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FTRMM%2FTMPA%2FDAY%2F7",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FTRMM%2FTMPA%2FDAY%2F7",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
@@ -1333237,129 +1333212,135 @@
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/TRMM_3B42_Daily_7.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/TRMM_3B42_Daily_7.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc2.gesdisc.eosdis.nasa.gov/data/TRMM_L3/TRMM_3B42_Daily.7",
-                    "description": "Access the data via HTTPS",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS",
+                    "downloadURL": "https://disc2.gesdisc.eosdis.nasa.gov/data/TRMM_L3/TRMM_3B42_Daily.7",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=TRMM_3B42_Daily",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=TRMM_3B42_Daily",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc2.gesdisc.eosdis.nasa.gov/dods/TRMM_3B42_Daily_7.info",
-                    "description": "The GrADS Data Server (GDS) is another form of OPeNDAP that provides subsetting and some analysis services across the Internet.",
                     "@type": "dcat:Distribution",
+                    "description": "The GrADS Data Server (GDS) is another form of OPeNDAP that provides subsetting and some analysis services across the Internet.",
+                    "downloadURL": "https://disc2.gesdisc.eosdis.nasa.gov/dods/TRMM_3B42_Daily_7.info",
+                    "mediaType": "text/html",
                     "title": "Use GRADS DATA SERVER (GDS) to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc2.gesdisc.eosdis.nasa.gov/opendap/TRMM_L3/TRMM_3B42_Daily.7/",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://disc2.gesdisc.eosdis.nasa.gov/opendap/TRMM_L3/TRMM_3B42_Daily.7/",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc2.gesdisc.eosdis.nasa.gov/thredds/catalog/aggregation/TRMM_3B42_Daily.7/catalog.html",
-                    "description": "Access the data via the THREDDS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the THREDDS.",
+                    "downloadURL": "https://disc2.gesdisc.eosdis.nasa.gov/thredds/catalog/aggregation/TRMM_3B42_Daily.7/catalog.html",
+                    "mediaType": "text/html",
                     "title": "Use THREDDS DATA to download the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/information/faqs?groups=Precipitation",
-                    "description": "View frequently asked questions about TRMM.",
                     "@type": "dcat:Distribution",
+                    "description": "View frequently asked questions about TRMM.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/information/faqs?groups=Precipitation",
+                    "mediaType": "text/html",
                     "title": "View information related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/GPM/3B42_3B43_doc_V7.pdf",
-                    "description": "README Document",
                     "@type": "dcat:Distribution",
+                    "description": "README Document",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/GPM/3B42_3B43_doc_V7.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's read me document"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://pmm.nasa.gov/sites/default/files/document_files/3B42_3B43_TMPA_restart.pdf",
-                    "description": "Transition from Monthly TMPA to Climatological Calibration/Adjustment",
                     "@type": "dcat:Distribution",
+                    "description": "Transition from Monthly TMPA to Climatological Calibration/Adjustment",
+                    "downloadURL": "https://pmm.nasa.gov/sites/default/files/document_files/3B42_3B43_TMPA_restart.pdf",
+                    "mediaType": "application/pdf",
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
+            "editor": "Andrey Savtchenko",
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/GPM/browse/TRMM_3B42_Daily.png",
+            "identifier": "C1239536905-GES_DISC",
+            "issued": "2016-04-19",
+            "keyword": [
+                "precipitation",
+                "earth science",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.5067/TRMM/TMPA/DAY/7",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2016-04-29",
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
+            "series-name": "TRMM_3B42_Daily",
             "spatial": "-180.0 -50.0 180.0 50.0",
+            "temporal": "1998-01-01T00:00:00Z/2022-01-17T00:00:00Z",
             "theme": [
                 "TRMM",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "TRMM (TMPA) Precipitation L3 1 day 0.25 degree x 0.25 degree V7 (TRMM_3B42_Daily) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/VLBI/VLBI_session_eops_001",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, CDDIS. https://doi.org/10.5067/VLBI/VLBI_session_eops_001.",
-            "issued": "2002-02-13",
-            "temporal": "2002-02-13T00:00:00Z/2023-12-11T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-12-11",
-            "keyword": [
-                "solid earth",
-                "geodetics",
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
-            "identifier": "C3242579905-CDDIS",
             "description": "The Session Series EOP product is a series of EOP results, one for each geodetic session. Data are irregularly spaced and there are multiple results for days on which there were simultaneous sessions. Each series includes a minimum of one year of results. The operational EOP-S product is available on the IVS Data Centers 24 hours after availability of each new session data base.",
-            "title": "CDDIS VLBI Session Earth Orientation Parameter Series (EOP-S) Product from NASA CDDIS",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FVLBI%2FVLBI_session_eops_001",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FVLBI%2FVLBI_session_eops_001",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
@@ -1333375,694 +1333356,715 @@
                     "title": "This dataset's landing page"
                 }
             ],
+            "identifier": "C3242579905-CDDIS",
+            "issued": "2002-02-13",
+            "keyword": [
+                "solid earth",
+                "geodetics",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/VLBI/VLBI_session_eops_001",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2023-12-11",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "CDDIS"
+            },
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2002-02-13T00:00:00Z/2023-12-11T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "CDDIS VLBI Session Earth Orientation Parameter Series (EOP-S) Product from NASA CDDIS"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/AURA/TES/TL2CON_L2.007",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2017-10-17. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/AURA/TES/TL2CON_L2.007. https://asdc.larc.nasa.gov/project/TES.",
-            "issued": "2015-08-27",
-            "temporal": "2004-08-22T00:00:00Z/2017-10-24T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2019-06-19",
-            "keyword": [
-                "clouds",
-                "atmosphere",
-                "atmospheric temperature",
-                "air quality",
-                "earth science",
-                "atmospheric chemistry"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "SCOTT Gluck",
                 "hasEmail": "mailto:scott.gluck@jpl.nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/LARC/SD/ASDC"
-            },
-            "identifier": "C1331182556-LARC",
             "description": "TL2CON_7 is the Tropospheric Emission Spectrometer (TES)/Aura Level 2 Carbon Monoxide Nadir Version 7 data product. TES was an instrument aboard NASA's Aura satellite and was launched from California on July 15, 2004. Data collection for TES is complete. TES Level 2 data contain retrieved species (or temperature) profiles at the observation targets and the estimated errors. The geolocation, quality, and other data (e.g., surface characteristics for nadir observations) were also provided. L2 modeled spectra were evaluated using radiative transfer modeling algorithms. The process, referred to as retrieval, compared observed spectra to the modeled spectra and iteratively updated the atmospheric parameters. L2 standard product files included information for one molecular species (or temperature) for an entire global survey or special observation run. A global survey consisted of a maximum of 16 consecutive orbits.\r\rNadir observations, which point directly to the surface of the Earth, are different from limb observations, which are pointed at various off-nadir angles into the atmosphere. Nadir and limb observations were added to separate L2 files, and a single ancillary file was composed of data that are common to both nadir and limb files. A Nadir sequence within the TES Global Survey was a fixed number of observations within an orbit for a Global Survey. Prior to April 24, 2005, it consisted of two low resolution scans over the same ground locations. After April 24, 2005, Global Survey data consisted of three low resolution scans. The Nadir standard product consists of four files, where each file is composed of the Global Survey Nadir observations from one of four focal planes for a single orbit, i.e. 72 orbit sequences. The Global Survey Nadir observations only used a single set of filter mix. \r\rA Global Survey consisted of observations along 16 consecutive orbits at the start of a two day cycle, over which 4,608 retrievals were performed. Each observation was the input for retrievals of species Volume Mixing Ratios (VMRs), temperature profiles, surface temperature, and other data parameters with associated pressure levels, precision, total error, vertical resolution, total column density, and other diagnostic quantities. Each TES Level 2 standard product reported information in a swath format conforming to the HDF-EOS Aura File Format Guidelines. Each Swath object was bounded by the number of observations in a global survey and a predefined set of pressure levels, representing slices through the atmosphere. Each standard product could have had a variable number of observations depending upon the Global Survey configuration and whether averaging was employed. Also, missing or bad retrievals were not reported. Further, observations were occasionally scheduled on non-global survey days. In general they were measurements made for validation purposes or with highly focused science objectives. Those non-global survey measurements were referred to as \u201cspecial observations.\u201d\r\rA Limb sequence within the TES Global Survey was three high-resolution scans over the same limb locations. The Limb standard product consists of four files, where each file is composed of the Global Survey Limb observations from one of four focal planes for a single orbit, i.e. 72 orbit sequences. The Global Survey Limb observations used a repeating sequence of filter wheel positions. Special Observations could only be scheduled during the 9 or 10 orbit gaps in the Global Surveys, and were conducted in any of three basic modes: stare, transect, step-and-stare. The mode used depended on the science requirement. Each limb observation Limb 1, Limb 2 and Limb 3, were processed independently. Thus, each limb standard product consisted of three sets where each set consisted of 1,152 observations. For TES, the swath object represented one of these sets. Thus, each limb standard product consisted of three swath objects, one for each observation, Limb 1, Limb 2, and Limb 3",
-            "title": "TES/Aura L2 Carbon Monoxide Nadir V007",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAURA%2FTES%2FTL2CON_L2.007",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAURA%2FTES%2FTL2CON_L2.007",
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
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1331182556-LARC",
-                    "description": "Earthdata Search for TL2CON_7 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for TL2CON_7 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1331182556-LARC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/AURA/TES/TL2CON_L2.007",
-                    "description": "DOI data set landing page for TL2CON_7",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for TL2CON_7",
+                    "downloadURL": "https://doi.org/10.5067/AURA/TES/TL2CON_L2.007",
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
-                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/TES/TL2CON.007/contents.html",
-                    "description": "OPeNDAP data access for TL2CON_7",
                     "@type": "dcat:Distribution",
+                    "description": "OPeNDAP data access for TL2CON_7",
+                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/TES/TL2CON.007/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/TES/TL2CON.007/",
-                    "description": "ASDC Direct Data Download for TL2CON_7",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for TL2CON_7",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/TES/TL2CON.007/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
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
+            "identifier": "C1331182556-LARC",
+            "issued": "2015-08-27",
+            "keyword": [
+                "clouds",
+                "atmosphere",
+                "atmospheric temperature",
+                "air quality",
+                "earth science",
+                "atmospheric chemistry"
+            ],
+            "landingPage": "https://doi.org/10.5067/AURA/TES/TL2CON_L2.007",
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
+            "temporal": "2004-08-22T00:00:00Z/2017-10-24T23:59:59Z",
             "theme": [
                 "TES",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "TES/Aura L2 Carbon Monoxide Nadir V007"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/AURA/TES/TESO3L_L2.006",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "The data used in this study were produced by the TES Science Team at the TES SIPS and archived at the Langley DAAC. See ProductionDateTime for Published date.",
-            "issued": "2013-03-29",
-            "temporal": "2004-07-15T00:00:00Z/2022-01-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2015-10-28",
-            "keyword": [
-                "atmospheric chemistry/oxygen compounds",
-                "air quality",
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
-                "name": "LaRC"
-            },
-            "identifier": "C191856329-LARC",
             "description": "Atmospheric vertical profile estimates and associated errors (diagonals and covariance matrices), along with retrieved surface temperature, cloud effective optical depth, column estimates, quality flags, averaging kernels and a priori constraint vectors.",
-            "title": "TES/Aura L2 O3 Limb V006",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAURA%2FTES%2FTESO3L_L2.006",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAURA%2FTES%2FTESO3L_L2.006",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 }
             ],
+            "identifier": "C191856329-LARC",
+            "issued": "2013-03-29",
+            "keyword": [
+                "atmospheric chemistry/oxygen compounds",
+                "air quality",
+                "atmosphere",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/AURA/TES/TESO3L_L2.006",
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
+            "title": "TES/Aura L2 O3 Limb V006"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/557",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Hall, F. G. 2000. BOREAS TE-18, 30-m, Radiometrically Rectified Landsat TM Imagery. ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/557",
-            "issued": "2023-11-22",
-            "temporal": "1984-06-22T00:00:00Z/1994-09-19T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-04-11",
-            "keyword": [
-                "earth science",
-                "land use/land cover",
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
-            "identifier": "C2929169150-ORNL_CLOUD",
             "description": "The BOREAS TE-18 team used a radiometric rectification process to produce standardized DN values for a series of Landsat TM images of the BOREAS SSA and NSA in order to compare images that were collected under different atmospheric conditions. The images for each study area were referenced to an image that had very clear atmospheric qualities. Each of the reference scenes had coincident atmospheric optical thickness measurements made by RSS-11.",
-            "graphic-preview-description": "Browse Image",
-            "title": "BOREAS TE-18, 30-m, Radiometrically Rectified Landsat TM Imagery",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/boreas_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F557",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F557",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/boreas/TE/te18ls30/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/boreas/TE/te18ls30/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/BOREAS/guides/TE18_Rad_Rectif_30m.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/BOREAS/guides/TE18_Rad_Rectif_30m.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/557",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/557",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TE/te18ls30/comp/ltm_rad_rect_30m_inv.lis",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TE/te18ls30/comp/ltm_rad_rect_30m_inv.lis",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TE/te18ls30/comp/README",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TE/te18ls30/comp/README",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TE/te18ls30/comp/restricted_readme",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TE/te18ls30/comp/restricted_readme",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TE/te18ls30/comp/te18ls30.def",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TE/te18ls30/comp/te18ls30.def",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/msword",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TE/te18ls30/comp/TE18_Rad_Rectif_30m.doc",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TE/te18ls30/comp/TE18_Rad_Rectif_30m.doc",
+                    "mediaType": "application/msword",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TE/te18ls30/comp/TE18_Rad_Rectif_30m.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TE/te18ls30/comp/TE18_Rad_Rectif_30m.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TE/te18ls30/comp/TE18_Rad_Rectif_30m.txt",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TE/te18ls30/comp/TE18_Rad_Rectif_30m.txt",
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
+            "identifier": "C2929169150-ORNL_CLOUD",
+            "issued": "2023-11-22",
+            "keyword": [
+                "earth science",
+                "land use/land cover",
+                "land surface"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/557",
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
             "spatial": "-106.32 53.42 -97.23 56.25",
+            "temporal": "1984-06-22T00:00:00Z/1994-09-19T23:59:59Z",
             "theme": [
                 "BOREAS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "BOREAS TE-18, 30-m, Radiometrically Rectified Landsat TM Imagery"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/WFC/CALIPSO/CAL_WFC_L1_1KM-VALSTAGE1-V3-02_L1B-003.02",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2011-12-13. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/WFC/CALIPSO/CAL_WFC_L1_1KM-VALSTAGE1-V3-02_L1B-003.02. https://asdc.larc.nasa.gov/project/CALIPSO.",
-            "issued": "2014-04-22",
-            "temporal": "2007-04-15T00:00:00Z/2022-01-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2018-03-11",
-            "keyword": [
-                "visible wavelengths",
-                "atmosphere",
-                "spectral/engineering",
-                "atmospheric radiation",
-                "earth science",
-                "infrared wavelengths",
-                "aerosols"
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
-            "identifier": "C7427596-LARC_ASDC",
             "description": "CAL_WFC_L1_1Km-ValStage1-V3-02 data are Cloud-Aerosol Lidar and Infrared Pathfinder Satellite Observation (CALIPSO) Wide Field Camera (WFC), Level 1B 1 km Native Science data, Validated Stage 1 Version 3-02. Data collection for this product is ongoing. Version 3.02 represents a transition of the Lidar, Imaging Infrared Radiometer (IIR), and WFC processing and browse code to a new cluster computing system. No algorithm changes were introduced, and very minor changes were observed between V3.01 and V3.02 as a result of the compiler and computer architecture differences. The primary WFC Level 1B data products are calibrated radiance and bidirectional reflectance registered to an Earth-based grid centered on the Lidar ground track. During the normal operation, the WFC acquires science data only during the daylight portions of the CALIPSO orbits. The WFC Level 1B 1 km Native Science grid covers the full 61 km swath centered on the Lidar track. CALIPSO was launched on April 28, 2006 to study the impact of clouds and aerosols on the Earth's radiation budget and climate. It flies in the international A-Train constellation for coincident Earth observations. The CALIPSO satellite is comprised of three instruments, the Cloud-Aerosol LIdar with Orthogonal Polarization (CALIOP), IIR, and WFC. CALIPSO is a joint satellite mission between NASA and the French Agency, CNES.",
-            "title": "CALIPSO Wide Field Camera Level 1B 1 km Native Science data, Validated Stage 1 V3-02",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FWFC%2FCALIPSO%2FCAL_WFC_L1_1KM-VALSTAGE1-V3-02_L1B-003.02",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FWFC%2FCALIPSO%2FCAL_WFC_L1_1KM-VALSTAGE1-V3-02_L1B-003.02",
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
-                    "downloadURL": "https://doi.org/10.5067/WFC/CALIPSO/CAL_WFC_L1_1KM-VALSTAGE1-V3-02_L1B-003.02",
-                    "description": "DOI data set landing page for CAL_WFC_L1_1Km-ValStage1-V3-02_V3-02",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for CAL_WFC_L1_1Km-ValStage1-V3-02_V3-02",
+                    "downloadURL": "https://doi.org/10.5067/WFC/CALIPSO/CAL_WFC_L1_1KM-VALSTAGE1-V3-02_L1B-003.02",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C7427596-LARC_ASDC",
-                    "description": "Earthdata Search for CAL_WFC_L1_1Km-ValStage1-V3-02_V3-02 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for CAL_WFC_L1_1Km-ValStage1-V3-02_V3-02 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C7427596-LARC_ASDC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/CALIPSO/WFC_L1_1Km-ValStage1-V3-02/contents.html",
-                    "description": "OPeNDAP data access for CAL_WFC_L1_1Km-ValStage1-V3-02_V3-02",
                     "@type": "dcat:Distribution",
+                    "description": "OPeNDAP data access for CAL_WFC_L1_1Km-ValStage1-V3-02_V3-02",
+                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/CALIPSO/WFC_L1_1Km-ValStage1-V3-02/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
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
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/calipso/quality_summaries/WFC_L1BScansProducts_3-01_v02.pdf",
-                    "description": "CALIPSO Quality Statement: Wide Field Camera Level 1B Scans Data Release Versions: 3.01, 3.02",
                     "@type": "dcat:Distribution",
+                    "description": "CALIPSO Quality Statement: Wide Field Camera Level 1B Scans Data Release Versions: 3.01, 3.02",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/calipso/quality_summaries/WFC_L1BScansProducts_3-01_v02.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's product quality assessment"
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
-                    "downloadURL": "https://www-calipso.larc.nasa.gov/resources/publications.php",
-                    "description": "CALIPSO - List of publications",
                     "@type": "dcat:Distribution",
+                    "description": "CALIPSO - List of publications",
+                    "downloadURL": "https://www-calipso.larc.nasa.gov/resources/publications.php",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
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
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/CALIPSO/WFC_L1_1Km-ValStage1-V3-02/",
-                    "description": "ASDC Direct Data Download for CAL_WFC_L1_1Km-ValStage1-V3-02_V3-02",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for CAL_WFC_L1_1Km-ValStage1-V3-02_V3-02",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/CALIPSO/WFC_L1_1Km-ValStage1-V3-02/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
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
                 }
             ],
+            "identifier": "C7427596-LARC_ASDC",
+            "issued": "2014-04-22",
+            "keyword": [
+                "visible wavelengths",
+                "atmosphere",
+                "spectral/engineering",
+                "atmospheric radiation",
+                "earth science",
+                "infrared wavelengths",
+                "aerosols"
+            ],
+            "landingPage": "https://doi.org/10.5067/WFC/CALIPSO/CAL_WFC_L1_1KM-VALSTAGE1-V3-02_L1B-003.02",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2018-03-11",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/LARC/SD/ASDC"
+            },
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2007-04-15T00:00:00Z/2022-01-17T00:00:00Z",
             "theme": [
                 "CALIPSO",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "CALIPSO Wide Field Camera Level 1B 1 km Native Science data, Validated Stage 1 V3-02"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-GST-3-RDR-GEOGRAPHOS-RADAR-V1.0",
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
-                "geographos",
-                "support archives"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "Goldstone radar observations of 1620 Geographos from August 28 through Sept. 2, 1994 yield delay-Doppler images whose linear spatial resolutions range from ~75 to ~151 meters, and 138 pairs of dual-polarization (OC/SC) (opposite circular/same circular) spectra with one-dimensional resolution of 103 m. These data are presented in Ostro, et al. 1996, Icarus 121, 46 [OSTROETAL1996], and are included in this data set. A full description of the observations and the reduction process is provided in the paper.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-gst-3-rdr-geographos-radar-v1.0_ryhj-umvw",
+            "issued": "2018-06-26",
+            "keyword": [
+                "geographos",
+                "support archives"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-GST-3-RDR-GEOGRAPHOS-RADAR-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-gst-3-rdr-geographos-radar-v1.0_ryhj-umvw",
-            "description": "Goldstone radar observations of 1620 Geographos from August 28 through Sept. 2, 1994 yield delay-Doppler images whose linear spatial resolutions range from ~75 to ~151 meters, and 138 pairs of dual-polarization (OC/SC) (opposite circular/same circular) spectra with one-dimensional resolution of 103 m. These data are presented in Ostro, et al. 1996, Icarus 121, 46 [OSTROETAL1996], and are included in this data set. A full description of the observations and the reduction process is provided in the paper.",
-            "title": "GEOGRAPHOS RADAR V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "GEOGRAPHOS RADAR V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-3-ESC2-67PCHURYUMOV-M14-V2.0",
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
+            "description": "This data set contains images acquired by the OSIRIS Narrow Angle Camera during the COMET ESCORT 2 phase of the Rosetta mission at the comet 67P, covering the period from 2015-03-10T23:25:00.000 to 2015-04-08T11:24:59.000. This version V2.0 supersedes previous deliveries of the same dataset.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-3-esc2-67pchuryumov-m14-v2.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-3-ESC2-67PCHURYUMOV-M14-V2.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-3-esc2-67pchuryumov-m14-v2.0",
-            "description": "This data set contains images acquired by the OSIRIS Narrow Angle Camera during the COMET ESCORT 2 phase of the Rosetta mission at the comet 67P, covering the period from 2015-03-10T23:25:00.000 to 2015-04-08T11:24:59.000. This version V2.0 supersedes previous deliveries of the same dataset.",
-            "title": "ROSETTA-ORBITER COMET ESCORT 2 OSINAC 3 RDR MTP014 V2.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER COMET ESCORT 2 OSINAC 3 RDR MTP014 V2.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://c3.nasa.gov/dashlink/resources/893/",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2014-01-11",
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
-            "identifier": "DASHLINK_893",
             "description": "This paper introduces a novel Prognostics-enhanced Automated Contingency Management (or ACM+P) paradigm based on both current health state (diagnosis) and future health state estimates (prognosis) for advanced autonomous systems. Including prognostics in ACM system allows not only fault accommodation, but also fault mitigation via proper control actions based on short term prognosis, and moreover, the establishment of a long term operational plan that optimizes the\r\nutility of the entire system based on long term prognostics. Technical challenges are identified and addressed by a hierarchical ACM+P architecture that allows fault accommodation and mitigation at various levels in the system ranging from component level control reconfiguration, system level control reconfiguration, to high level mission re-planning and resource redistribution. The ACM+P paradigm was developed and evaluated in a high fidelity Unmanned Aerial Vehicle (UAV) simulation environment with flight-proven baseline flight controller and simulated diagnostics and prognostics of flight control actuators. Simulation results are presented. The ACM+P concept, architecture and the generic methodologies presented in this paper are applicable to many advanced autonomous systems such as deep space probes, unmanned autonomous vehicles, and military and commercial aircraft.",
-            "title": "Simulation-based Design and Validation of Automated Contingency Management for Propulsion Systems",
-            "programCode": [
-                "026:029"
-            ],
             "distribution": [
                 {
-                    "mediaType": "application/download",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/publication/25_Prognsotics_Enhanced_ACM_for_Advanced_Autonomous.pdf",
-                    "description": "25 Prognsotics Enhanced ACM for Advanced Autonomous.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "25 Prognsotics Enhanced ACM for Advanced Autonomous.pdf",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/publication/25_Prognsotics_Enhanced_ACM_for_Advanced_Autonomous.pdf",
+                    "mediaType": "application/download",
                     "title": "25 Prognsotics Enhanced ACM for Advanced Autonomous.pdf"
                 }
             ],
-            "accrualPeriodicity": "irregular"
+            "identifier": "DASHLINK_893",
+            "issued": "2014-01-11",
+            "keyword": [
+                "nasa",
+                "ames",
+                "dashlink"
+            ],
+            "landingPage": "https://c3.nasa.gov/dashlink/resources/893/",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:029"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Dashlink"
+            },
+            "title": "Simulation-based Design and Validation of Automated Contingency Management for Propulsion Systems"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=CO-S-UVIS-2-SPEC-V1.1",
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
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.co-s-uvis-2-spec-v1.1_ryiz-3w85",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "epimetheus",
                 "titan",
@@ -1334089,78 +1334091,85 @@
                 "calypso",
                 "atlas"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=CO-S-UVIS-2-SPEC-V1.1",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.co-s-uvis-2-spec-v1.1_ryiz-3w85",
-            "description": "Spectroscopy of Jupiter, Saturnian rings, atmospheres and satellites for determining chemical abundance, compositional albedo, aerosol profiling, ring reflected spectra and diffraction patterns.",
-            "title": "CASSINI ORBITER SATURN UVIS EDITED SPECTRA 1.1",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "CASSINI ORBITER SATURN UVIS EDITED SPECTRA 1.1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-A-OSIWAC-3-AST1-STEINSFLYBY-V1.4",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This data set contains images acquired by the OSIRIS Wide Angle Camera\nduring the STEINS_FLY-BY mission phase",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-a-osiwac-3-ast1-steinsflyby-v1.4_ryq3-7drp",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "16 cyg b",
                 "international rosetta mission",
                 "vega",
                 "2867 steins"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-A-OSIWAC-3-AST1-STEINSFLYBY-V1.4",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-a-osiwac-3-ast1-steinsflyby-v1.4_ryq3-7drp",
-            "description": "This data set contains images acquired by the OSIRIS Wide Angle Camera\nduring the STEINS_FLY-BY mission phase",
-            "title": "ROSETTA-ORBITER STEINS_FLY-BY OSIWAC 3\n                                      RDR V1.4",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER STEINS_FLY-BY OSIWAC 3\n                                      RDR V1.4"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://nasa3d.arc.nasa.gov/detail/aura-eoe3d",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2018-06-25",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
-            "references": [
-                "http://www.nasa.gov/mission_pages/aura/main/index.html"
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Brian Kumanchik",
+                "hasEmail": "mailto:brian.kumanchik@jpl.nasa.gov"
+            },
+            "description": "Aura observes the chemical content of the atmosphere to track the state of the ozone layer and the dispersion of airborne pollution.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://nasa3d.arc.nasa.gov/shared_assets/models/aura-eoe3d/Aura-v002.fbx.zip",
+                    "mediaType": "application/octet-stream"
+                }
             ],
+            "identifier": "NASA-319",
+            "issued": "2018-06-25",
             "keyword": [
                 "eyes on the earth 3d",
                 "eyes on the solar system",
@@ -1334171,1017 +1334180,986 @@
                 "spacecraft",
                 "a-train"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Brian Kumanchik",
-                "hasEmail": "mailto:brian.kumanchik@jpl.nasa.gov"
-            },
+            "landingPage": "http://nasa3d.arc.nasa.gov/detail/aura-eoe3d",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:007"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "NASA-319",
-            "description": "Aura observes the chemical content of the atmosphere to track the state of the ozone layer and the dispersion of airborne pollution.",
-            "title": "NASA 3D Models: Aura",
-            "programCode": [
-                "026:007"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://nasa3d.arc.nasa.gov/shared_assets/models/aura-eoe3d/Aura-v002.fbx.zip",
-                    "mediaType": "application/octet-stream"
-                }
+            "references": [
+                "http://www.nasa.gov/mission_pages/aura/main/index.html"
             ],
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Space Science"
-            ]
+            ],
+            "title": "NASA 3D Models: Aura"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-X-HK-3-IMP-V1.0",
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
+            "description": "This CODMAC level 3 data set contains the key parameters of the Inertial Measurement Package.                                                     In particular, it provides information on the gyroscope attitude         measurements on a global scale and individual.                           It covers the period from launch in 2004, through the 3 Earth and        1 Mars flyby, plus the hibernation phases, plus the asteroid flybys      and finally covers the Prelanding, comet escort & Extension phases       of the prime target of the mission.                                      The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1).         This version V1.0 is the first version of this dataset.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-x-hk-3-imp-v1.0_ryra-g46z",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-X-HK-3-IMP-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-x-hk-3-imp-v1.0_ryra-g46z",
-            "description": "This CODMAC level 3 data set contains the key parameters of the Inertial Measurement Package.                                                     In particular, it provides information on the gyroscope attitude         measurements on a global scale and individual.                           It covers the period from launch in 2004, through the 3 Earth and        1 Mars flyby, plus the hibernation phases, plus the asteroid flybys      and finally covers the Prelanding, comet escort & Extension phases       of the prime target of the mission.                                      The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1).         This version V1.0 is the first version of this dataset.",
-            "title": "ROSETTA INERTIAL MEASUREMENT PACKAGE                  \n                        ENGINEERING DATA",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA INERTIAL MEASUREMENT PACKAGE                  \n                        ENGINEERING DATA"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.7927/H47M05W2",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Center for International Earth Science Information Network - CIESIN - Columbia University. 2017-10-13. Global Population Count Grid Time Series Estimates. Version 1.00. Palisades, NY. Archived by National Aeronautics and Space Administration, U.S. Government, NASA Socioeconomic Data and Applications Center (SEDAC). https://doi.org/10.7927/H47M05W2. https://doi.org/10.7927/H4CC0XNV.",
-            "issued": "2017-10-13",
-            "temporal": "1970-01-01T00:00:00Z/2000-12-31T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2017-10-13",
-            "references": [
-                "https://doi.org/10.1111/j.1466-8238.2010.00587.x",
-                "https://doi.org/10.1177/0959683609356587",
-                "https://doi.org/10.7927/H47M05W2",
-                "https://doi.org/10.7927/H40R9MBW"
-            ],
-            "keyword": [
-                "earth science",
-                "human dimensions",
-                "population"
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
-            "identifier": "C1427515664-SEDAC",
-            "description": "The Global Population Count Grid Time Series Estimates provide a back-cast time series of population grids based on the year 2000 population grid from SEDAC's Global Rural-Urban Mapping Project, Version 1 (GRUMPv1) data set. The grids were created by using rates of population change between decades from the coarser resolution History Database of the Global Environment (HYDE) database to back-cast the GRUMPv1 population count grids. Mismatches between the spatial extent of the HYDE calculated rates and GRUMPv1 population data were resolved via infilling rate cells based on a focal mean of values. Finally, the grids were adjusted so that the population totals for each country equaled the UN World Population Prospects (2008 Revision) estimates for that country for the respective year (1970, 1980, 1990, and 2000). These data do not represent census observations for the years prior to 2000, and therefore can at best be thought of as estimations of the populations in given locations. The population grids are consistent internally within the time series, but are not recommended for use in creating longer time series with any other population grids, including GRUMPv1, Gridded Population of the World, Version 4 (GPWv4), or non-SEDAC developed population grids. These population grids served as an input to SEDAC's Global Estimated Net Migration Grids by Decade: 1970-2000 data set.",
-            "release-place": "Palisades, NY",
-            "graphic-preview-description": "Maps Download Page",
             "creator": "Center for International Earth Science Information Network - CIESIN - Columbia University",
-            "title": "Global Population Count Grid Time Series Estimates",
-            "graphic-preview-file": "https://sedac.ciesin.columbia.edu/data/set/popdynamics-global-pop-count-time-series-estimates/maps",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The Global Population Count Grid Time Series Estimates provide a back-cast time series of population grids based on the year 2000 population grid from SEDAC's Global Rural-Urban Mapping Project, Version 1 (GRUMPv1) data set. The grids were created by using rates of population change between decades from the coarser resolution History Database of the Global Environment (HYDE) database to back-cast the GRUMPv1 population count grids. Mismatches between the spatial extent of the HYDE calculated rates and GRUMPv1 population data were resolved via infilling rate cells based on a focal mean of values. Finally, the grids were adjusted so that the population totals for each country equaled the UN World Population Prospects (2008 Revision) estimates for that country for the respective year (1970, 1980, 1990, and 2000). These data do not represent census observations for the years prior to 2000, and therefore can at best be thought of as estimations of the populations in given locations. The population grids are consistent internally within the time series, but are not recommended for use in creating longer time series with any other population grids, including GRUMPv1, Gridded Population of the World, Version 4 (GPWv4), or non-SEDAC developed population grids. These population grids served as an input to SEDAC's Global Estimated Net Migration Grids by Decade: 1970-2000 data set.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.7927%2FH47M05W2",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.7927%2FH47M05W2",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/downloads/maps/popdynamics/popdynamics-global-pop-count-time-series-estimates/popdynamics-global-pop-count-time-series-estimates-1990-thumbnail.jpg",
-                    "description": "Sample browse graphic of the data set.",
                     "@type": "dcat:Distribution",
+                    "description": "Sample browse graphic of the data set.",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/downloads/maps/popdynamics/popdynamics-global-pop-count-time-series-estimates/popdynamics-global-pop-count-time-series-estimates-1990-thumbnail.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/popdynamics-global-pop-count-time-series-estimates/data-download",
-                    "description": "Data Download Page",
                     "@type": "dcat:Distribution",
+                    "description": "Data Download Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/popdynamics-global-pop-count-time-series-estimates/data-download",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/popdynamics-global-pop-count-time-series-estimates/maps",
-                    "description": "Maps Download Page",
+                {
                     "@type": "dcat:Distribution",
+                    "description": "Maps Download Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/popdynamics-global-pop-count-time-series-estimates/maps",
+                    "mediaType": "text/html",
                     "title": "Get a related map visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://sedac.ciesin.columbia.edu/data/set/popdynamics-global-pop-count-time-series-estimates/docs",
-                    "description": "Documentation Page",
                     "@type": "dcat:Distribution",
+                    "description": "Documentation Page",
+                    "downloadURL": "http://sedac.ciesin.columbia.edu/data/set/popdynamics-global-pop-count-time-series-estimates/docs",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/popdynamics-global-pop-count-time-series-estimates/maps/services",
-                    "description": "Web Map Service Page",
                     "@type": "dcat:Distribution",
+                    "description": "Web Map Service Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/popdynamics-global-pop-count-time-series-estimates/maps/services",
+                    "mediaType": "text/html",
                     "title": "Use Web Map Service (WMS) to download the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/popdynamics-global-pop-count-time-series-estimates",
-                    "description": "Data Set\u00a0Overview Page",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set\u00a0Overview Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/popdynamics-global-pop-count-time-series-estimates",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "graphic-preview-description": "Maps Download Page",
+            "graphic-preview-file": "https://sedac.ciesin.columbia.edu/data/set/popdynamics-global-pop-count-time-series-estimates/maps",
+            "identifier": "C1427515664-SEDAC",
+            "issued": "2017-10-13",
+            "keyword": [
+                "earth science",
+                "human dimensions",
+                "population"
+            ],
+            "landingPage": "https://doi.org/10.7927/H47M05W2",
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
+                "https://doi.org/10.1111/j.1466-8238.2010.00587.x",
+                "https://doi.org/10.1177/0959683609356587",
+                "https://doi.org/10.7927/H47M05W2",
+                "https://doi.org/10.7927/H40R9MBW"
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
+            "title": "Global Population Count Grid Time Series Estimates"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewBundle.jsp?identifier=urn%3Anasa%3Apds%3Airtf_io_photometry&version=1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "IRTF Photometry of Io",
+            "identifier": "urn:nasa:pds:irtf_io_photometry",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2021-05-21",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "irtf photometry of io",
                 "io",
                 "irtf photometry io"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewBundle.jsp?identifier=urn%3Anasa%3Apds%3Airtf_io_photometry&version=1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:irtf_io_photometry",
-            "description": "IRTF Photometry of Io",
-            "title": "InfraRed Telescope Facility Io Photometry Bundle",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "InfraRed Telescope Facility Io Photometry Bundle"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1432636971-GES_DISC.html",
             "citation": "Oxford University AOPP. 2017-10-31. PMRN6L1RAD_CDROM. Version 001. PMR/Nimbus-6 Level 1 Radiance Data from CD-ROM V001. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://disc.gsfc.nasa.gov/datacollection/PMRN6L1RAD_CDROM_001.html. Digital Science Data.",
-            "issued": "1998-02-25",
-            "temporal": "1975-06-16T00:00:00Z/1978-06-24T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "1998-02-25",
-            "references": [
-                "https://doi.org/10.1098/rspa.1974.0042"
-            ],
-            "keyword": [
-                "infrared wavelengths",
-                "spectral/engineering",
-                "earth science"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "JAMES JOHNSON",
                 "hasEmail": "mailto:James.Johnson@nasa.gov"
             },
+            "creator": "Oxford University AOPP",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C1432636971-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "PMRN6L1RAD_CDROM is the gridded Nimbus-6 Pressure Modulated Radiometer (PMR) Level 1 Radiance Data Product. The radiances are measured at CO2 lines in the 15 micron band. The purpose of the PMR experiment is to measure the temperature of the upper stratosphere and mesosphere from 40 to 90 km with a vertical resolution of about 10 km, and 500 km horizontal resolution. This product contains radiances in a daily 4 degree latitude x 10 degree longitude grid format, as well as copies of the original tapes. The data for this product are available from 16 June 1975 to 24 June 1978. The principal investigator for the PMR experiment was Dr. John T. Houghton from Oxford University.\n\nThis product was created by the Oxford University's Atmospheric, Oceanic and Planetary Physics (AOPP) group. The data are stored on two CD-ROMs in ASCII files of hexadecimal characters, and are available in gzipped Unix tar archive files. The first CD-ROM contains the gridded radiance data and a few original tape data files, the second CD-ROM contains the remaining compressed copies of the original data tapes. The byte-ordering in the data files follows the DEC convention for 16-bit integers of less significant byte first. Normal 2's complement integer storage is assumed.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "PMRN6L1RAD_CDROM",
-            "creator": "Oxford University AOPP",
-            "graphic-preview-description": "Nimbus-6 PMR Radiance emitted from the 47-73 km layer on 31 July 1975",
-            "title": "PMR/Nimbus-6 Level 1 Radiance Data from CD-ROM V001 (PMRN6L1RAD_CDROM) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Nimbus/images/N6PMR_sample.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Nimbus/images/N6PMR_sample.png",
-                    "description": "Nimbus-6 PMR Radiance emitted from the 47-73 km layer on 31 July 1975",
                     "@type": "dcat:Distribution",
+                    "description": "Nimbus-6 PMR Radiance emitted from the 47-73 km layer on 31 July 1975",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Nimbus/images/N6PMR_sample.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/PMRN6L1RAD_CDROM_001.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/PMRN6L1RAD_CDROM_001.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/Nimbus6_PMR_Level1/PMRN6L1RAD_CDROM.001/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/Nimbus6_PMR_Level1/PMRN6L1RAD_CDROM.001/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=PMRN6L1RAD_CDROM",
-                    "description": "Use the Earthdata Search Client to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search Client to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=PMRN6L1RAD_CDROM",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/Nimbus6_PMR_Level1/PMRN6L1RAD_CDROM.001/doc/README.PMRN6L1RAD_CDROM_001.txt",
-                    "description": "README Document",
                     "@type": "dcat:Distribution",
+                    "description": "README Document",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/Nimbus6_PMR_Level1/PMRN6L1RAD_CDROM.001/doc/README.PMRN6L1RAD_CDROM_001.txt",
+                    "mediaType": "text/html",
                     "title": "View this dataset's read me document"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/repository/Mission/Nimbus/3.3_Product_Documentation/3.3.5_Product_Quality/NimbusVIUG.pdf",
-                    "description": "Nimbus 6 User's Guide",
                     "@type": "dcat:Distribution",
+                    "description": "Nimbus 6 User's Guide",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/repository/Mission/Nimbus/3.3_Product_Documentation/3.3.5_Product_Quality/NimbusVIUG.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
                 },
                 {
-                    "mediaType": "application/gzip",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/repository/Mission/Nimbus/3.3_Product_Documentation/3.3.5_Product_Quality/DataCatalogNimbus6.tar.gz",
-                    "description": "Nimbus 6 Data Catalog",
                     "@type": "dcat:Distribution",
+                    "description": "Nimbus 6 Data Catalog",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/repository/Mission/Nimbus/3.3_Product_Documentation/3.3.5_Product_Quality/DataCatalogNimbus6.tar.gz",
+                    "mediaType": "application/gzip",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "graphic-preview-description": "Nimbus-6 PMR Radiance emitted from the 47-73 km layer on 31 July 1975",
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Nimbus/images/N6PMR_sample.png",
+            "identifier": "C1432636971-GES_DISC",
+            "issued": "1998-02-25",
+            "keyword": [
+                "infrared wavelengths",
+                "spectral/engineering",
+                "earth science"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1432636971-GES_DISC.html",
+            "language": [
+                "en-US"
+            ],
+            "modified": "1998-02-25",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
+            },
+            "references": [
+                "https://doi.org/10.1098/rspa.1974.0042"
+            ],
+            "release-place": "Greenbelt, MD, USA",
+            "series-name": "PMRN6L1RAD_CDROM",
             "spatial": "-180.0 -80.0 180.0 80.0",
+            "temporal": "1975-06-16T00:00:00Z/1978-06-24T23:59:59.999Z",
             "theme": [
                 "Nimbus",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "PMR/Nimbus-6 Level 1 Radiance Data from CD-ROM V001 (PMRN6L1RAD_CDROM) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/TERRA/MOPITT/MOP03TM_L3.109",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/TERRA/MOPITT/MOP03TM_L3.109. https://asdc.larc.nasa.gov/project/MOPITT.",
-            "issued": "2020-12-23",
-            "temporal": "2018-03-01T00:00:00Z/2023-03-01T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-12-23",
-            "keyword": [
-                "air quality",
-                "atmospheric chemistry",
-                "earth science",
-                "atmosphere"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Helen Worden",
                 "hasEmail": "mailto:hmw@ucar.edu"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/LARC/SD/ASDC"
-            },
-            "identifier": "C2103889025-LARC",
             "description": "MOP03TM_109 is the Measurements Of Pollution In The Troposphere (MOPITT) Beta CO gridded monthly means (Thermal Infrared Radiances) version 109 product. It is an unvalidated beta product subject to recalibration, contains monthly mean gridded versions of the daily Level 2 CO profile and total column retrievals. The averaging kernels associated with each retrieval are also gridded and included in the Level 3 files. Version 109 products are beta versions for version 9 products, they are unvalidated beta products subject to recalibration. Data collection for this product is ongoing.\r\rFor a description of the file contents, refer to the File Spec Document. The MOPITT Level 2 Data Quality Statement contains additional information about the quality and the limitations of the retrievals. [From the MOPITT version 3 Level 3 Data Quality Summary] MOPITT was successfully launched into sun-synchronous polar orbit aboard Terra, NASA's first Earth Observing System spacecraft on December 18, 1999. The MOPITT instrument was constructed by a consortium of Canadian companies and funded by the Space Science Division of the Canadian Space Agency.",
-            "graphic-preview-description": "NASA Worldview",
-            "title": "MOPITT Beta CO gridded monthly means (Thermal Infrared Radiances) V109",
-            "graphic-preview-file": "https://worldview.earthdata.nasa.gov/",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FTERRA%2FMOPITT%2FMOP03TM_L3.109",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FTERRA%2FMOPITT%2FMOP03TM_L3.109",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://mopitt.physics.utoronto.ca/",
-                    "description": "University of Toronto MOPITT Overview",
                     "@type": "dcat:Distribution",
+                    "description": "University of Toronto MOPITT Overview",
+                    "downloadURL": "https://mopitt.physics.utoronto.ca/",
+                    "mediaType": "text/html",
                     "title": "The dataset's home page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www2.acom.ucar.edu/mopitt",
-                    "description": "U.S. MOPITT project home page",
                     "@type": "dcat:Distribution",
+                    "description": "U.S. MOPITT project home page",
+                    "downloadURL": "https://www2.acom.ucar.edu/mopitt",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.atmosp.physics.utoronto.ca/MOPITT/home.html",
-                    "description": "Canadian MOPITT project home page",
                     "@type": "dcat:Distribution",
+                    "description": "Canadian MOPITT project home page",
+                    "downloadURL": "https://www.atmosp.physics.utoronto.ca/MOPITT/home.html",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://eospso.gsfc.nasa.gov/atbd-category/48",
-                    "description": "NASA EOS ATB Documents: MOPITT",
                     "@type": "dcat:Distribution",
+                    "description": "NASA EOS ATB Documents: MOPITT",
+                    "downloadURL": "https://eospso.gsfc.nasa.gov/atbd-category/48",
+                    "mediaType": "text/html",
                     "title": "View this dataset's algorithm theoretical basis document"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/mopitt/guide/ASDC_MOPITT_Overview_2015.pdf",
-                    "description": "Overview of MOPITT Data at the ASDC",
                     "@type": "dcat:Distribution",
+                    "description": "Overview of MOPITT Data at the ASDC",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/mopitt/guide/ASDC_MOPITT_Overview_2015.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://terra.nasa.gov/",
-                    "description": "Terra Instrument home page",
                     "@type": "dcat:Distribution",
+                    "description": "Terra Instrument home page",
+                    "downloadURL": "https://terra.nasa.gov/",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/mopitt/mopitt_quality_statements.html",
-                    "description": "ASDC List of MOPITT Quality Statements",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC List of MOPITT Quality Statements",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/mopitt/mopitt_quality_statements.html",
+                    "mediaType": "text/html",
                     "title": "View this dataset's data quality document"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/project/MOPITT",
-                    "description": "ASDC Data and Information for MOPITT",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Data and Information for MOPITT",
+                    "downloadURL": "https://asdc.larc.nasa.gov/project/MOPITT",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://earthdata.nasa.gov/learn/sensing-our-planet/on-the-trail-of-global-pollution-drift",
-                    "description": "Earth Observing System Data and InformationSystem (EOSDIS) Article: On The Trail of Global Pollution Drift",
                     "@type": "dcat:Distribution",
+                    "description": "Earth Observing System Data and InformationSystem (EOSDIS) Article: On The Trail of Global Pollution Drift",
+                    "downloadURL": "https://earthdata.nasa.gov/learn/sensing-our-planet/on-the-trail-of-global-pollution-drift",
+                    "mediaType": "text/html",
                     "title": "View a micro article on this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://giovanni.gsfc.nasa.gov/giovanni/",
-                    "description": "Goddard Earth Sciences Data and Information Services Center (GES DISC): Giovanni - Interactive Visualization and Analysis software",
                     "@type": "dcat:Distribution",
+                    "description": "Goddard Earth Sciences Data and Information Services Center (GES DISC): Giovanni - Interactive Visualization and Analysis software",
+                    "downloadURL": "https://giovanni.gsfc.nasa.gov/giovanni/",
+                    "mediaType": "text/html",
                     "title": "Subset this dataset using a web based subsetter"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www2.acom.ucar.edu/mopitt/visualization",
-                    "description": "MOPITT Visualizations",
                     "@type": "dcat:Distribution",
+                    "description": "MOPITT Visualizations",
+                    "downloadURL": "https://www2.acom.ucar.edu/mopitt/visualization",
+                    "mediaType": "text/html",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://earthobservatory.nasa.gov/images/10775/bushfires-raging-in-southeast-australia",
-                    "description": "NASA Earth Observatory Article: Bushfires Raging in Southeast Australia : Natural Hazards\u00a0- Data taken by the Measurements Of Pollution In The Troposphere (MOPITT) instrument aboard NASA's Terra satellite have been combined for 6 days from January 15-20, 2003",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Earth Observatory Article: Bushfires Raging in Southeast Australia : Natural Hazards\u00a0- Data taken by the Measurements Of Pollution In The Troposphere (MOPITT) instrument aboard NASA's Terra satellite have been combined for 6 days from January 15-20, 2003",
+                    "downloadURL": "https://earthobservatory.nasa.gov/images/10775/bushfires-raging-in-southeast-australia",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://earthobservatory.nasa.gov/images/13721/carbon-monoxide-from-tropical-fires",
-                    "description": "NASA Earth Observatory Article: Carbon Monoxide from Tropical Fires : Natural Hazards\u00a0-\u00a0The Terra MOPITT sensor observed large plumes of carbon monoxide produced by biomass burning in South America and Africa in early August 2004.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Earth Observatory Article: Carbon Monoxide from Tropical Fires : Natural Hazards\u00a0-\u00a0The Terra MOPITT sensor observed large plumes of carbon monoxide produced by biomass burning in South America and Africa in early August 2004.",
+                    "downloadURL": "https://earthobservatory.nasa.gov/images/13721/carbon-monoxide-from-tropical-fires",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://earthobservatory.nasa.gov/images/19011/fires-and-thick-smoke-over-south-america",
-                    "description": "NASA Earth Observatory Article: Fires and Thick Smoke over South America : Natural Hazards\u00a0-\u00a0Places where MOPITT could not collect enough data to make an estimate of carbon monoxide (probably due to clouds) are gray.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Earth Observatory Article: Fires and Thick Smoke over South America : Natural Hazards\u00a0-\u00a0Places where MOPITT could not collect enough data to make an estimate of carbon monoxide (probably due to clouds) are gray.",
+                    "downloadURL": "https://earthobservatory.nasa.gov/images/19011/fires-and-thick-smoke-over-south-america",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://earthobservatory.nasa.gov/images/533/mopitt-first-light-image",
-                    "description": "NASA Earth Observatory Article: MOPITT First Light Image : Image of the Day\u00a0-\u00a0MOPITT measures radiances in several channels to determine the amount of carbon monoxide (CO) and methane in the atmosphere.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Earth Observatory Article: MOPITT First Light Image : Image of the Day\u00a0-\u00a0MOPITT measures radiances in several channels to determine the amount of carbon monoxide (CO) and methane in the atmosphere.",
+                    "downloadURL": "https://earthobservatory.nasa.gov/images/533/mopitt-first-light-image",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://earthobservatory.nasa.gov/images/852/mopitt-views-carbon-monoxide-concentration",
-                    "description": "NASA Earth Observatory Article: MOPITT Views Carbon Monoxide Concentration, there were widespread wildfires across Montana and Idaho.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Earth Observatory Article: MOPITT Views Carbon Monoxide Concentration, there were widespread wildfires across Montana and Idaho.",
+                    "downloadURL": "https://earthobservatory.nasa.gov/images/852/mopitt-views-carbon-monoxide-concentration",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://earthobservatory.nasa.gov/images/559/mopitt-views-north-america",
-                    "description": "NASA Earth Observatory Article: MOPITT Views North America : Image of the Day\u00a0-\u00a0Measurement of Pollution in the Troposphere, MOPITT, measures two important pollutants in the Earth's atmosphere\u2014carbon monoxide (CO) and methane.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Earth Observatory Article: MOPITT Views North America : Image of the Day\u00a0-\u00a0Measurement of Pollution in the Troposphere, MOPITT, measures two important pollutants in the Earth's atmosphere\u2014carbon monoxide (CO) and methane.",
+                    "downloadURL": "https://earthobservatory.nasa.gov/images/559/mopitt-views-north-america",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://earthdata.nasa.gov/learn/sensing-our-planet/nature-s-contribution",
-                    "description": "NASA Earthdata Article: Nature's contribution: Researchers investigate how much wildfires contribute to pollution, and how far this pollution can travel - By Jane Beitler",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Earthdata Article: Nature's contribution: Researchers investigate how much wildfires contribute to pollution, and how far this pollution can travel - By Jane Beitler",
+                    "downloadURL": "https://earthdata.nasa.gov/learn/sensing-our-planet/nature-s-contribution",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://forum.earthdata.nasa.gov/app.php/tag/MOPITT",
-                    "description": "NASA Earthdata Forum - MOPITT Project Specific Forum",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Earthdata Forum - MOPITT Project Specific Forum",
+                    "downloadURL": "https://forum.earthdata.nasa.gov/app.php/tag/MOPITT",
+                    "mediaType": "text/html",
                     "title": "Access this dataset's users feedback page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.nasa.gov/feature/langley/longstanding-carbon-monoxide-measuring-instrument-mopitt-celebrated/",
-                    "description": "NASA Langley Article: Fourteen Years of Carbon Monoxide from MOPITT, which has truly unlocked a pathway for groundbreaking studies of air pollution transport and atmospheric chemical processes.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Langley Article: Fourteen Years of Carbon Monoxide from MOPITT, which has truly unlocked a pathway for groundbreaking studies of air pollution transport and atmospheric chemical processes.",
+                    "downloadURL": "https://www.nasa.gov/feature/langley/longstanding-carbon-monoxide-measuring-instrument-mopitt-celebrated/",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://worldview.earthdata.nasa.gov/",
-                    "description": "NASA Worldview",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Worldview",
+                    "downloadURL": "https://worldview.earthdata.nasa.gov/",
+                    "mediaType": "text/html",
                     "title": "Get a related visualization through WORLDVIEW"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.pnas.org/content/115/20/5099",
-                    "description": "Proceedings of the National Academy of Sciences (PNAS) Article: Unexpected slowdown of US pollutant emission reduction in the past decade\u00a0(Ground and satellite observations show that air pollution regulations in the United States (US) have resulted in substantial reductions in emissions and corresponding improvements in air quality over the last several decades)",
                     "@type": "dcat:Distribution",
+                    "description": "Proceedings of the National Academy of Sciences (PNAS) Article: Unexpected slowdown of US pollutant emission reduction in the past decade\u00a0(Ground and satellite observations show that air pollution regulations in the United States (US) have resulted in substantial reductions in emissions and corresponding improvements in air quality over the last several decades)",
+                    "downloadURL": "https://www.pnas.org/content/115/20/5099",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
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
-                    "downloadURL": "https://hdfeos.org/zoo/",
-                    "description": "Examples on how to access and visualize various NASA HDF/HDF-EOS files using Python (pyhdf/h5py), NCL, MATLAB\u00ae, and IDL\u00ae, NCL, MATLAB\u00ae, and IDL\u00ae",
                     "@type": "dcat:Distribution",
+                    "description": "Examples on how to access and visualize various NASA HDF/HDF-EOS files using Python (pyhdf/h5py), NCL, MATLAB\u00ae, and IDL\u00ae, NCL, MATLAB\u00ae, and IDL\u00ae",
+                    "downloadURL": "https://hdfeos.org/zoo/",
+                    "mediaType": "text/html",
                     "title": "View this dataset's how-to documentation"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2103889025-LARC",
-                    "description": "Earthdata Search for MOP03TM_109 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for MOP03TM_109 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2103889025-LARC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/TERRA/MOPITT/MOP03TM_L3.109",
-                    "description": "DOI data set landing page for MOP03TM_109",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for MOP03TM_109",
+                    "downloadURL": "https://doi.org/10.5067/TERRA/MOPITT/MOP03TM_L3.109",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 }
             ],
+            "graphic-preview-description": "NASA Worldview",
+            "graphic-preview-file": "https://worldview.earthdata.nasa.gov/",
+            "identifier": "C2103889025-LARC",
+            "issued": "2020-12-23",
+            "keyword": [
+                "air quality",
+                "atmospheric chemistry",
+                "earth science",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.5067/TERRA/MOPITT/MOP03TM_L3.109",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2020-12-23",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/LARC/SD/ASDC"
+            },
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2018-03-01T00:00:00Z/2023-03-01T00:00:00Z",
             "theme": [
                 "MOPITT",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "MOPITT Beta CO gridded monthly means (Thermal Infrared Radiances) V109"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/GPMGV/IFLOODS/D3R/DATA101",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Chandrasekar, V. .2014. GPM GROUND VALIDATION DUAL-FREQUENCY DUAL-POLARIZED DOPPLER RADAR (D3R) IFLOODS [indicate subset used]. Dataset available online from the NASA Global Hydrometeorology Resource Center DAAC, Huntsville, Alabama, U.S.A. DOI: http://dx.doi.org/10.5067/GPMGV/IFLOODS/D3R/DATA101",
-            "issued": "2014-02-17",
-            "temporal": "2013-05-09T02:59:31Z/2013-06-13T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-05-09",
-            "keyword": [
-                "atmosphere",
-                "clouds",
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
-            "identifier": "C1981441257-GHRC_DAAC",
             "description": "The GPM Ground Validation Dual-frequency Dual-polarized Doppler Radar (D3R) IFloodS dataset contains radar reflectivity and doppler velocity measurements from the Iowa Flood Studies (IFloodS) campaign. This campaign aimed to improve satellite precipitation measurements for flood prediction by using ground measurements to improve satellite retrieval algorithms. The D3R was developed by a government-industry-academic consortium with funding from NASA's Global Precipitation Measurement (GPM) Project. It operates at the ku (13.91 GHz \u00b1 25 MHz) and ka (35.56 GHz \u00b1 25 MHz) frequencies covering a fixed range from 450 m to 39.75 km. The D3R IFloodS dataset is available from May 9, 2013 through June 13, 2013 in netCDF-3 format with corresponding browse imagery available in PNG format.",
-            "graphic-preview-description": "Browse images illustrate the nature and coverage of the data",
-            "title": "GPM GROUND VALIDATION DUAL-FREQUENCY DUAL-POLARIZED DOPPLER RADAR (D3R) IFLOODS V1",
-            "graphic-preview-file": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/ifloods/D3R/browse/",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGPMGV%2FIFLOODS%2FD3R%2FDATA101",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGPMGV%2FIFLOODS%2FD3R%2FDATA101",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=gpmd3rifld",
-                    "description": "Files may be downloaded directly to your workstation from this link",
                     "@type": "dcat:Distribution",
+                    "description": "Files may be downloaded directly to your workstation from this link",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=gpmd3rifld",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/ifloods/D3R/browse/2013-06-04/ku_clutterfilter_off/ifloods_d3r_ku_20130604_124423_01_RHI_az_130.5_zdb.png",
-                    "description": "Sample browse image",
                     "@type": "dcat:Distribution",
+                    "description": "Sample browse image",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/ifloods/D3R/browse/2013-06-04/ku_clutterfilter_off/ifloods_d3r_ku_20130604_124423_01_RHI_az_130.5_zdb.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
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
-                    "mediaType": "text/html",
-                    "downloadURL": "http://pmm.nasa.gov/science/ground-validation/D3R",
-                    "description": "D3R Instrument Information Page",
                     "@type": "dcat:Distribution",
+                    "description": "D3R Instrument Information Page",
+                    "downloadURL": "http://pmm.nasa.gov/science/ground-validation/D3R",
+                    "mediaType": "text/html",
                     "title": "View information related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/ifloods/D3R/doc/gpmd3rifld_dataset.pdf",
-                    "description": "The guide document contains detailed information about the dataset",
                     "@type": "dcat:Distribution",
+                    "description": "The guide document contains detailed information about the dataset",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/ifloods/D3R/doc/gpmd3rifld_dataset.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.1109/IGARSS.2010.5653929",
-                    "description": "Realization of the NASA Dual-Frequency Dual-Polarized Doppler Radar (D3R)",
                     "@type": "dcat:Distribution",
+                    "description": "Realization of the NASA Dual-Frequency Dual-Polarized Doppler Radar (D3R)",
+                    "downloadURL": "https://doi.org/10.1109/IGARSS.2010.5653929",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.1109/IGARSS.2010.5649440",
-                    "description": "Scientific and engineering overview of the NASA Dual-Frequency Dual-Polarized Doppler Radar (D3R) system for GPM Ground Validation",
                     "@type": "dcat:Distribution",
+                    "description": "Scientific and engineering overview of the NASA Dual-Frequency Dual-Polarized Doppler Radar (D3R) system for GPM Ground Validation",
+                    "downloadURL": "https://doi.org/10.1109/IGARSS.2010.5649440",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.1175/JTECH-D-14-00097.1",
-                    "description": "A Semisupervised Robust Hydrometeor Classification Method for Dual-Polarization Radar Applications",
                     "@type": "dcat:Distribution",
+                    "description": "A Semisupervised Robust Hydrometeor Classification Method for Dual-Polarization Radar Applications",
+                    "downloadURL": "https://doi.org/10.1175/JTECH-D-14-00097.1",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/home/field-campaigns/ifloods",
-                    "description": "IFloodS Field Campaign Project Homepage",
                     "@type": "dcat:Distribution",
+                    "description": "IFloodS Field Campaign Project Homepage",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/home/field-campaigns/ifloods",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/ifloods/D3R/browse/",
-                    "description": "Browse images illustrate the nature and coverage of the data",
                     "@type": "dcat:Distribution",
+                    "description": "Browse images illustrate the nature and coverage of the data",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/ifloods/D3R/browse/",
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
+            "graphic-preview-file": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/ifloods/D3R/browse/",
+            "identifier": "C1981441257-GHRC_DAAC",
+            "issued": "2014-02-17",
+            "keyword": [
+                "atmosphere",
+                "clouds",
+                "radar",
+                "earth science",
+                "spectral/engineering"
+            ],
+            "landingPage": "https://doi.org/10.5067/GPMGV/IFLOODS/D3R/DATA101",
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
             "spatial": "-92.9 42.0 -90.1 42.5",
+            "temporal": "2013-05-09T02:59:31Z/2013-06-13T23:59:59Z",
             "theme": [
                 "IFloodS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "GPM GROUND VALIDATION DUAL-FREQUENCY DUAL-POLARIZED DOPPLER RADAR (D3R) IFLOODS V1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-4-ESC1-67PCHURYUMOV-M12-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This CODMAC level 4 data set contains radiometric calibrated and geometric distortion corrected (resampled) image data in W/m^2/sr/nm acquired by the OSIRIS Narrow Angle Camera during the COMET ESCORT 1 phase of the Rosetta mission, covering the period from 2015-01-13T23:25:00.000 to 2015-02-10T23:24:59.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-4-esc1-67pchuryumov-m12-v1.0",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2021-05-21",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "67p/churyumov-gerasimenko 1 (1969 r1)",
                 "vega",
                 "international rosetta mission"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-4-ESC1-67PCHURYUMOV-M12-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-4-esc1-67pchuryumov-m12-v1.0",
-            "description": "This CODMAC level 4 data set contains radiometric calibrated and geometric distortion corrected (resampled) image data in W/m^2/sr/nm acquired by the OSIRIS Narrow Angle Camera during the COMET ESCORT 1 phase of the Rosetta mission, covering the period from 2015-01-13T23:25:00.000 to 2015-02-10T23:24:59.000.",
-            "title": "ROSETTA-ORBITER 67P OSINAC 4 ESC1-MTP012 RDR V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P OSINAC 4 ESC1-MTP012 RDR V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/AQR50-3DCAE",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "NASA Aquarius project. 2017-12-07. Aquarius Official Release Level 3 Sea Surface Density Standard Mapped Image Ascending Mission Cumulative Data. Version 5.0. Aquarius Sea Surface Salinity Products. Goddard Space Flight Center, 8800 Greenbelt Rd.; Greeenbelt, MD., 20771, USA. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/GSFC OBPG. https://doi.org/10.5067/AQR50-3DCAE. http://podaac.jpl.nasa.gov/SeaSurfaceSalinity/Aquarius. NASA Aquarius project, NASA/GSFC OBPG, 2017-12-07, Aquarius Official Release Level 3 Sea Surface Density Standard Mapped Image Ascending Mission Cumulative Data V5.0, http://podaac.jpl.nasa.gov/SeaSurfaceSalinity/Aquarius.",
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
-            "identifier": "C2491755981-POCLOUD",
-            "description": "Aquarius Level 3 sea surface density standard mapped image data contains gridded 1 degree spatial resolution density data averaged over daily, 7 day, monthly, and seasonal time scales. This particular data set is the mission series mean or cumulative, Ascending sea\nsurface density product for version 5.0 of the Aquarius data set. Only retrieved values for Ascending passes have been used to create this product.  Surface density estimates are based on TEOS-10 and derived using retrieved salinity from Aquarius and collocated ancillary SST (Reynolds OI 0.25 degree product).  The Aquarius instrument is onboard the AQUARIUS/SAC-D satellite, a collaborative effort between NASA and the Argentinian Space Agency Comision Nacional de Actividades Espaciales (CONAE). The instrument consists of three radiometers in push broom alignment at incidence angles of 29, 38, and 46 degrees incidence angles relative to the shadow side of the orbit.  Footprints for the beams are: 76 km (along-track) x 94 km (cross-track), 84 km x 120 km and 96km x 156 km, yielding a total cross-track swath of 370 km. The radiometers measure brightness temperature at 1.413 GHz in their respective horizontal and vertical polarizations (TH and TV). A scatterometer operating at 1.26 GHz measures ocean backscatter in each footprint that is used for surface roughness corrections in the estimation of salinity. The scatterometer has an approximate 390km swath.",
-            "release-place": "Goddard Space Flight Center, 8800 Greenbelt Rd.; Greeenbelt, MD., 20771, USA",
-            "series-name": "Aquarius Official Release Level 3 Sea Surface Density Standard Mapped Image Ascending Mission Cumulative Data",
-            "graphic-preview-description": "Thumbnail",
             "creator": "NASA Aquarius project",
-            "title": "Aquarius Official Release Level 3 Sea Surface Density Standard Mapped Image Ascending Mission Cumulative Data V5.0",
-            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/AQUARIUS_L3_DENSITY_SMIA_CUMULATIVE_V5.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "Aquarius Level 3 sea surface density standard mapped image data contains gridded 1 degree spatial resolution density data averaged over daily, 7 day, monthly, and seasonal time scales. This particular data set is the mission series mean or cumulative, Ascending sea\nsurface density product for version 5.0 of the Aquarius data set. Only retrieved values for Ascending passes have been used to create this product.  Surface density estimates are based on TEOS-10 and derived using retrieved salinity from Aquarius and collocated ancillary SST (Reynolds OI 0.25 degree product).  The Aquarius instrument is onboard the AQUARIUS/SAC-D satellite, a collaborative effort between NASA and the Argentinian Space Agency Comision Nacional de Actividades Espaciales (CONAE). The instrument consists of three radiometers in push broom alignment at incidence angles of 29, 38, and 46 degrees incidence angles relative to the shadow side of the orbit.  Footprints for the beams are: 76 km (along-track) x 94 km (cross-track), 84 km x 120 km and 96km x 156 km, yielding a total cross-track swath of 370 km. The radiometers measure brightness temperature at 1.413 GHz in their respective horizontal and vertical polarizations (TH and TV). A scatterometer operating at 1.26 GHz measures ocean backscatter in each footprint that is used for surface roughness corrections in the estimation of salinity. The scatterometer has an approximate 390km swath.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAQR50-3DCAE",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAQR50-3DCAE",
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
-                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/AQUARIUS_L3_DENSITY_SMIA_CUMULATIVE_V5.jpg",
-                    "description": "Thumbnail",
                     "@type": "dcat:Distribution",
+                    "description": "Thumbnail",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/AQUARIUS_L3_DENSITY_SMIA_CUMULATIVE_V5.jpg",
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
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2491755981-POCLOUD",
-                    "description": "HTTPS endpoint for data browse and download",
                     "@type": "dcat:Distribution",
+                    "description": "HTTPS endpoint for data browse and download",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2491755981-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2491755981-POCLOUD",
-                    "description": "Browse granule search results in Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse granule search results in Earthdata Search",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2491755981-POCLOUD",
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
```

