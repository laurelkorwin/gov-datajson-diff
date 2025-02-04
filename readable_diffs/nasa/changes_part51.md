# Change History for nasa.json (Part 51)

### Changes from 31606f9 to dd2190f (Part 40/162)
**Author:** Automated

**Date:** 2025-02-01 15:02:16+00:00

**Message:** Updated data: Sat Feb  1 15:02:16 UTC 2025

```diff
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
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/ML2HNO3_004.png",
+            "identifier": "C1251101497-GES_DISC",
+            "issued": "2015-02-19",
+            "keyword": [
+                "earth science",
+                "atmospheric chemistry",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.5067/Aura/MLS/DATA2012",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2015-02-19",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
+            },
+            "release-place": "Greenbelt, MD, USA",
+            "series-name": "ML2HNO3",
             "spatial": "-180.0 -82.0 180.0 82.0",
+            "temporal": "2004-08-02T00:00:00Z/2022-01-17T00:00:00Z",
             "theme": [
                 "Aura",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "MLS/Aura Level 2 Nitric Acid (HNO3) Mixing Ratio V004 (ML2HNO3) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/AQR50-3R3DS",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "NASA Aquarius project. 2017-12-07. Aquarius Official Release Level 3 Ancillary Reynolds Sea Surface Temperature Standard Mapped Image Descending Seasonal Data. Version 5.0. Aquarius Sea Surface Salinity Products. Goddard Space Flight Center, 8800 Greenbelt Rd.; Greeenbelt, MD., 20771, USA. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/GSFC OBPG. https://doi.org/10.5067/AQR50-3R3DS. http://podaac.jpl.nasa.gov/SeaSurfaceSalinity/Aquarius. NASA Aquarius project, NASA/GSFC OBPG, 2017-12-07, Aquarius Official Release Level 3 Ancillary Reynolds Sea Surface Temperature Standard Mapped Image Descending Seasonal Data V5.0, http://podaac.jpl.nasa.gov/SeaSurfaceSalinity/Aquarius.",
-            "issued": "2017-10-21",
-            "temporal": "2011-08-25T02:41:02Z/2015-06-07T12:45:21Z",
-            "@type": "dcat:Dataset",
-            "modified": "2017-12-07",
-            "keyword": [
-                "oceans",
-                "ocean temperature",
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
-            "identifier": "C2491755612-POCLOUD",
-            "description": "Aquarius Level 3 ancillary sea surface temperature (SST) standard mapped image data are the ancillary SST data used in the Aquarius calibration for salinity retrieval.  They are simply the daily SSTs from the Reynolds National Climatic Data Center (NCDC) 0.25 degree dataset, gridded and averaged using the Aquarius processing L2-L3 processing scheme to the same 1 degree spatial resolution and daily, 7 day, monthly, seasonal, and annual time intervals as Aquarius L3 standard salinity and wind speed products.  This particular data set is the Seasonal, descending ancillary sea surface temperature product associated with version 5.0  of the Aquarius data set, which is the official end of mission public data release from the AQUARIUS/SAC-D mission.",
-            "release-place": "Goddard Space Flight Center, 8800 Greenbelt Rd.; Greeenbelt, MD., 20771, USA",
-            "series-name": "Aquarius Official Release Level 3 Ancillary Reynolds Sea Surface Temperature Standard Mapped Image Descending Seasonal Data",
-            "graphic-preview-description": "Thumbnail",
             "creator": "NASA Aquarius project",
-            "title": "Aquarius Official Release Level 3 Ancillary Reynolds Sea Surface Temperature Standard Mapped Image Descending Seasonal Data V5.0",
-            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/AQUARIUS_L3_ANCILLARY_SST_SMID_3MONTH_V5.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "Aquarius Level 3 ancillary sea surface temperature (SST) standard mapped image data are the ancillary SST data used in the Aquarius calibration for salinity retrieval.  They are simply the daily SSTs from the Reynolds National Climatic Data Center (NCDC) 0.25 degree dataset, gridded and averaged using the Aquarius processing L2-L3 processing scheme to the same 1 degree spatial resolution and daily, 7 day, monthly, seasonal, and annual time intervals as Aquarius L3 standard salinity and wind speed products.  This particular data set is the Seasonal, descending ancillary sea surface temperature product associated with version 5.0  of the Aquarius data set, which is the official end of mission public data release from the AQUARIUS/SAC-D mission.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAQR50-3R3DS",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAQR50-3R3DS",
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
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/AQUARIUS_L3_ANCILLARY_SST_SMID_3MONTH_V5.jpg",
-                    "description": "Thumbnail",
                     "@type": "dcat:Distribution",
+                    "description": "Thumbnail",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/AQUARIUS_L3_ANCILLARY_SST_SMID_3MONTH_V5.jpg",
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
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2491755612-POCLOUD",
-                    "description": "HTTPS endpoint for data browse and download",
                     "@type": "dcat:Distribution",
+                    "description": "HTTPS endpoint for data browse and download",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2491755612-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2491755612-POCLOUD",
-                    "description": "Browse granule search results in Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse granule search results in Earthdata Search",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2491755612-POCLOUD",
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
+            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/AQUARIUS_L3_ANCILLARY_SST_SMID_3MONTH_V5.jpg",
+            "identifier": "C2491755612-POCLOUD",
+            "issued": "2017-10-21",
+            "keyword": [
+                "oceans",
+                "ocean temperature",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/AQR50-3R3DS",
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
+            "series-name": "Aquarius Official Release Level 3 Ancillary Reynolds Sea Surface Temperature Standard Mapped Image Descending Seasonal Data",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2011-08-25T02:41:02Z/2015-06-07T12:45:21Z",
             "theme": [
                 "AQUARIUS SAC-D",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Aquarius Official Release Level 3 Ancillary Reynolds Sea Surface Temperature Standard Mapped Image Descending Seasonal Data V5.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://techport.nasa.gov/view/10895",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2009-01-01",
-            "temporal": "2009-01-01T00:00:00Z/2014-01-01T00:00:00Z",
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
-                "goddard space flight center"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Caroline Kilbourne",
                 "hasEmail": "mailto:caroline.a.kilbourne@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Science Mission Directorate"
-            },
-            "identifier": "TECHPORT_10895",
             "description": "\"We propose to continue our successful research program in developing x-ray microcalorimeter arrays for astrophysics.  This development will directly benefit not only the International X-ray Observatory (IXO), but also other possible mission concepts.  We will investigate various array and pixel optimizations such as would be needed for large arrays for surveys, or arrays of fast pixels optimized for neutron star burst spectroscopy.\n\n\n\nThe main emphasis of our research will be the further development of arrays of superconducting transition-edge sensors (TES) for imaging x-ray spectroscopy.   We have developed a TES pixel that achieves better than 2.5-eV resolution at 6 keV, and arrays of such pixels that are sufficiently uniform in characteristics  as to permit common biasing without significant compromises in the operation of any pixel.   We are also making arrays of position sensitive TES pixels that show promise for use on IXO.  We propose to advance both the single-pixel and position-sensitive arrays so that we can produce arrays suitable for subsystem-level read-out demonstrations of the IXO X-ray Microcalorimeter Spectrometer focal plane.\n\n\n\nAdditionally, we propose to re-evaluate out successful pixel design which, while certainly suitable for use in developing the architecture of arrays and addressing detector systems issues, is not necessarily the final optimization. The performance of a TES depends on the functional form of the current, temperature, and magnetic-field dependence of the resistive transition, and also on the noise at each point on this transition surface.  The parameters that describe this transition surface occupy a large phase space, and we have only probed a small portion of it. We propose to fabricate a series of test devices to explore other parts of the phase space and to learn how to engineer the superconducting transition. Recently, our understanding of the physical effects governing the observed resistive transitions has improved, th",
-            "title": "Advancement and New Optimizations of Microcalorimeter Arrays for High-Resolution Imaging X-ray Spectroscopy Project",
-            "programCode": [
-                "026:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "http://techport.nasa.gov/xml-api/10895",
                     "mediaType": "application/xml"
                 }
-            ]
+            ],
+            "identifier": "TECHPORT_10895",
+            "issued": "2009-01-01",
+            "keyword": [
+                "active",
+                "project",
+                "goddard space flight center"
+            ],
+            "landingPage": "http://techport.nasa.gov/view/10895",
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
+            "temporal": "2009-01-01T00:00:00Z/2014-01-01T00:00:00Z",
+            "title": "Advancement and New Optimizations of Microcalorimeter Arrays for High-Resolution Imaging X-ray Spectroscopy Project"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ASDCDAAC/NARSTO/0050",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2008-01-04. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/ASDCDAAC/NARSTO/0050.",
-            "issued": "2011-08-31",
-            "temporal": "2000-05-24T00:00:00Z/2007-01-01T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2018-04-26",
-            "keyword": [
-                "atmosphere",
-                "atmospheric pressure",
-                "atmospheric water vapor",
-                "atmospheric radiation",
-                "atmospheric winds",
-                "earth science"
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
-            "identifier": "C2241871216-LARC_ASDC",
             "description": "NARSTO_EPA_SS_FRESNO_MET_DATA is North American Research Strategy for Tropospheric Ozone (NARSTO) Environmental Protection Agency (EPA) Supersite (SS) Fresno, Beta Attenuation Monitors (BAM) Meteorological Data. This data set contains measurements taken from six meteorological instruments operated at the Fresno supersite from May 24, 2000 to December 31, 2006. The ambient temperature was measured by a Met One Instruments aspirated thermistor, Model 060A-2. The barometric pressure was measured by a Met One pressure transducer, Model 090D. The relative humidity was measured by a Met One aspirated thin film capacitor, Model 083V. The solar radiation was measured by a LI-COR Inc. pyranometer, Model LI-200SA. The wind speed was measured by a Met One Instruments 3-cup anemometer, Model 010-SC. The wind direction was measured by a Met One Instruments High-Sensitivity wind vane, Model 025-5C. All six instruments reported 5 minute samples.\r\n\r\nThe Fresno Supersite is one of several Supersites established in urban areas within the United States by the EPA to better understand the measurement, sources, and health effects of suspended particulate matter (PM). The site is located at 3425 First Street, approximately 1 km north of the downtown commercial district. First Street was a four-lane artery with moderate traffic levels. Commercial establishments, office buildings, churches, and schools were located north and south of the monitor. Medium-density single-family homes and some apartments were located in the blocks to the east and west of First Street. The Fresno Supersite began operation in May of 1999.The EPA PM Supersites Program was an ambient air monitoring research program designed to provide information of value to the atmospheric sciences, and human health and exposure research communities. \r\n\r\nEight geographically diverse projects were chosen to specifically address the following EPA research priorities: (1) to characterize PM, its constituents, precursors, co-pollutants, atmospheric transport, and its source categories that affect the PM in any region; (2) to address the research questions and scientific uncertainties about PM source-receptor and exposure-health effects relationships; and (3) to compare and evaluate different methods of characterizing PM including testing new and emerging measurement methods.\r\n\r\nNARSTO, which has since disbanded, was a public/private partnership, whose membership spanned across government, utilities, industry, and academe throughout Mexico, the United States, and Canada. The primary mission was to coordinate and enhance policy-relevant scientific research and assessment of tropospheric pollution behavior; activities provide input for science-based decision-making and determination of workable, efficient, and effective strategies for local and regional air-pollution management. Data products from local, regional, and international monitoring and research programs are still available.",
-            "title": "NARSTO EPA Supersite (SS) Fresno, Beta Attenuation Monitors (BAM) Meteorological Data",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDCDAAC%2FNARSTO%2F0050",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDCDAAC%2FNARSTO%2F0050",
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
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2241871216-LARC_ASDC",
-                    "description": "Earthdata Search for NARSTO_EPA_SS_FRESNO_MET_DATA_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for NARSTO_EPA_SS_FRESNO_MET_DATA_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2241871216-LARC_ASDC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/ASDCDAAC/NARSTO/0050",
-                    "description": "DOI data set landing page for NARSTO_EPA_SS_FRESNO_MET_DATA_1",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for NARSTO_EPA_SS_FRESNO_MET_DATA_1",
+                    "downloadURL": "https://doi.org/10.5067/ASDCDAAC/NARSTO/0050",
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
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/narsto/guide/narsto_epa_ss_fresno_met_data.pdf",
-                    "description": "Guide for NARSTO EPA_SS_FRESNO Meteorological Data",
                     "@type": "dcat:Distribution",
+                    "description": "Guide for NARSTO EPA_SS_FRESNO Meteorological Data",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/narsto/guide/narsto_epa_ss_fresno_met_data.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's product usage"
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
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/NARSTO/EPA_SS_FRESNO_MET_DATA_1/",
-                    "description": "ASDC Direct Data Download for NARSTO_EPA_SS_FRESNO_MET_DATA_1",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for NARSTO_EPA_SS_FRESNO_MET_DATA_1",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/NARSTO/EPA_SS_FRESNO_MET_DATA_1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 }
             ],
+            "identifier": "C2241871216-LARC_ASDC",
+            "issued": "2011-08-31",
+            "keyword": [
+                "atmosphere",
+                "atmospheric pressure",
+                "atmospheric water vapor",
+                "atmospheric radiation",
+                "atmospheric winds",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/ASDCDAAC/NARSTO/0050",
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
             "spatial": "36.79 -119.78",
+            "temporal": "2000-05-24T00:00:00Z/2007-01-01T23:59:59.999Z",
             "theme": [
                 "NARSTO",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "NARSTO EPA Supersite (SS) Fresno, Beta Attenuation Monitors (BAM) Meteorological Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=PHX-M-RAC-2-EDR-V1.0",
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
+            "description": "The Robotic Arm Camera (RAC) experiment on the Mars Phoenix Lander consists of one instrument component plus command electronics. This RAC Imaging Operations EDR data set contains raw data from the Robotic Arm Camera (RAC).",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.phx-m-rac-2-edr-v1.0_99xj-38uh",
+            "issued": "2018-06-26",
+            "keyword": [
+                "mars",
+                "phoenix"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=PHX-M-RAC-2-EDR-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.phx-m-rac-2-edr-v1.0_99xj-38uh",
-            "description": "The Robotic Arm Camera (RAC) experiment on the Mars Phoenix Lander consists of one instrument component plus command electronics. This RAC Imaging Operations EDR data set contains raw data from the Robotic Arm Camera (RAC).",
-            "title": "PHOENIX MARS ROBOTIC ARM CAMERA 2 EDR VERSION 1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "PHOENIX MARS ROBOTIC ARM CAMERA 2 EDR VERSION 1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC2-0662-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 2 phase 2015-03-11 to 2015-06-30. It is a Global Gravity measurement at the comet 67P and covers the time 2015-03-21T01:58:50.000 to 2015-03-21T09:02:02.500.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc2-0662-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC2-0662-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc2-0662-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 2 phase 2015-03-11 to 2015-06-30. It is a Global Gravity measurement at the comet 67P and covers the time 2015-03-21T01:58:50.000 to 2015-03-21T09:02:02.500.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 2 0662 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 2 0662 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-A-MIRO-3-AST1-STEINS-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This data set contains radiometrically calibrated Spectroscopic and Continuum data, in the form of table files, taken during the Steins Fly-by phase of the Rosetta mission by the MIRO instrument.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-a-miro-3-ast1-steins-v1.0_9a2v-zz6c",
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
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-A-MIRO-3-AST1-STEINS-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-a-miro-3-ast1-steins-v1.0_9a2v-zz6c",
-            "description": "This data set contains radiometrically calibrated Spectroscopic and Continuum data, in the form of table files, taken during the Steins Fly-by phase of the Rosetta mission by the MIRO instrument.",
-            "title": "ROSETTA-ORBITER STEINS MIRO 3 AST1 STEINS V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "ROSETTA-ORBITER STEINS MIRO 3 AST1 STEINS V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/GPMGV/IPHEX/NAV/DATA/001",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Poellot, Michael R, Andrew J Heymsfield and David  Delene.2015. GPM GROUND VALIDATION UND CITATION NAVIGATION DATA IPHEx [indicate subset used]. Dataset available online from the NASA Global Hydrometeorology Resource Center DAAC, Huntsville, Alabama, U.S.A. DOI: http://dx.doi.org/10.5067/GPMGV/IPHEX/NAV/DATA/001",
-            "issued": "2015-04-30",
-            "temporal": "2014-03-06T17:45:38Z/2014-06-13T23:39:40Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-05-09",
-            "keyword": [
-                "atmospheric temperature",
-                "atmosphere",
-                "spectral/engineering",
-                "platform characteristics",
-                "earth science",
-                "atmospheric winds",
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
-            "identifier": "C1979635316-GHRC_DAAC",
             "description": "The GPM Ground Validation UND Citation Navigation Data IPHEx dataset supplies navigation data collected by the Cessna Citation II aircraft for flights that occurred during March 6, 2014 through June 13, 2014 for the Global Precipitation Measurement Ground Validation Integrated Precipitation and Hydrology Experiment (IPHEx) field campaign in North Carolina. The goal of IPHEx was to evaluate the accuracy of satellite precipitation measurements and use the collected data for hydrology models in the region. The Cessna Citation II Research aircraft, owned and operated by the University of North Dakota (UND), participated in the IPHEx field campaign by serving as an in situ microphysics sampling platform. This navigation dataset consists of final processed files containing records that include flight time, aircraft location (latitude, longitude, and altitude), air temperature, wind speed, and other relevant aircraft parameters in ASCII format.",
-            "title": "GPM GROUND VALIDATION UND CITATION NAVIGATION DATA IPHEx V1",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGPMGV%2FIPHEX%2FNAV%2FDATA%2F001",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGPMGV%2FIPHEX%2FNAV%2FDATA%2F001",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=gpmnavcitiphx",
-                    "description": "Files may be downloaded directly to your workstation from this link",
                     "@type": "dcat:Distribution",
+                    "description": "Files may be downloaded directly to your workstation from this link",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=gpmnavcitiphx",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://dx.doi.org/10.5067/GPMGV/IPHEX/DATA101",
-                    "description": "IPHEx Field Campaign Collection DOI",
                     "@type": "dcat:Distribution",
+                    "description": "IPHEx Field Campaign Collection DOI",
+                    "downloadURL": "http://dx.doi.org/10.5067/GPMGV/IPHEX/DATA101",
+                    "mediaType": "text/html",
                     "title": "View information related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://airborneresearch.atmos.und.edu/",
-                    "description": "Cessna Citation II Research Aircraft",
                     "@type": "dcat:Distribution",
+                    "description": "Cessna Citation II Research Aircraft",
+                    "downloadURL": "http://airborneresearch.atmos.und.edu/",
+                    "mediaType": "text/html",
                     "title": "View information related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://airborneresearch.atmos.und.edu/dataformat.aspx",
-                    "description": "Citation Research Aircraft Data File Format",
                     "@type": "dcat:Distribution",
+                    "description": "Citation Research Aircraft Data File Format",
+                    "downloadURL": "http://airborneresearch.atmos.und.edu/dataformat.aspx",
+                    "mediaType": "text/html",
                     "title": "View information related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/iphex/nav_citation/doc/gpmnavcitiphx_dataset.pdf",
-                    "description": "The guide document contains detailed information about the dataset",
                     "@type": "dcat:Distribution",
+                    "description": "The guide document contains detailed information about the dataset",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/iphex/nav_citation/doc/gpmnavcitiphx_dataset.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "http://ghrc.nsstc.nasa.gov/uso/ds_docs/gpmgv/iphex/citation_mission/Citation_IPHEX_MissionSummary.pdf",
-                    "description": "IPHEx Citation Mission Summary",
                     "@type": "dcat:Distribution",
+                    "description": "IPHEx Citation Mission Summary",
+                    "downloadURL": "http://ghrc.nsstc.nasa.gov/uso/ds_docs/gpmgv/iphex/citation_mission/Citation_IPHEX_MissionSummary.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View the primary investigator's documentation for this dataset"
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
-                    "downloadURL": "http://dx.doi.org/10.1007/s12145-010-0061-4",
-                    "description": "Airborne data processing and analysis software package",
                     "@type": "dcat:Distribution",
+                    "description": "Airborne data processing and analysis software package",
+                    "downloadURL": "http://dx.doi.org/10.1007/s12145-010-0061-4",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/home/field-campaigns/iphex",
-                    "description": "IPHEx Field Campaign Project Homepage",
                     "@type": "dcat:Distribution",
+                    "description": "IPHEx Field Campaign Project Homepage",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/home/field-campaigns/iphex",
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
+            "identifier": "C1979635316-GHRC_DAAC",
+            "issued": "2015-04-30",
+            "keyword": [
+                "atmospheric temperature",
+                "atmosphere",
+                "spectral/engineering",
+                "platform characteristics",
+                "earth science",
+                "atmospheric winds",
+                "atmospheric pressure"
+            ],
+            "landingPage": "https://doi.org/10.5067/GPMGV/IPHEX/NAV/DATA/001",
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
             "spatial": "-81.0 43.5 -78.0 46.5",
+            "temporal": "2014-03-06T17:45:38Z/2014-06-13T23:39:40Z",
             "theme": [
                 "IPHEx",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "GPM GROUND VALIDATION UND CITATION NAVIGATION DATA IPHEx V1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=CLEM1-L-RSS-1-BSR-V1.0",
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
-                "deep space program science experiment",
-                "moon"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "The Clementine Bistatic Radar Raw Data Archive (BSR-RDA) is a time-ordered collection of raw and partially processed data from bistatic radar scattering experiments conducted using the Clementine spacecraft while it orbited the Moon.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.clem1-l-rss-1-bsr-v1.0_9a3p-j9q2",
+            "issued": "2021-05-21",
+            "keyword": [
+                "deep space program science experiment",
+                "moon"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=CLEM1-L-RSS-1-BSR-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.clem1-l-rss-1-bsr-v1.0_9a3p-j9q2",
-            "description": "The Clementine Bistatic Radar Raw Data Archive (BSR-RDA) is a time-ordered collection of raw and partially processed data from bistatic radar scattering experiments conducted using the Clementine spacecraft while it orbited the Moon.",
-            "title": "CLEM1 LUNAR RADIO SCIENCE RAW BISTATIC RADAR V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "CLEM1 LUNAR RADIO SCIENCE RAW BISTATIC RADAR V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=IHW-C-IRSPEC-3-EDR-GZ-V1.0",
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
+            "description": "In preparation for the concerted international study of Comet Halley, the IHW conducted a trial run with observations of Comet Crommelin, largely during February and March of 1984.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ihw-c-irspec-3-edr-gz-v1.0_9a4j-zwq3",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international halley watch",
+                "halley"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=IHW-C-IRSPEC-3-EDR-GZ-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ihw-c-irspec-3-edr-gz-v1.0_9a4j-zwq3",
-            "description": "In preparation for the concerted international study of Comet Halley, the IHW conducted a trial run with observations of Comet Crommelin, largely during February and March of 1984.",
-            "title": "IHW COMET IRSPEC CALIBRATED EXPERIMENT DATA RECORD GZ V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "IHW COMET IRSPEC CALIBRATED EXPERIMENT DATA RECORD GZ V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/SWTPR-GPS01",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "SWOT pre-launch field campaign. 2022-05-31. GPS sea surface height, Conductivity, Temperature and Depth (CTD) data from the 2019-2020 SWOT pre-launch field campaign. Version 1.0. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/JPL/PODAAC. https://doi.org/10.5067/SWTPR-GPS01. https://podaac-tools.jpl.nasa.gov/drive/files/misc/web/misc/SWOT/SWOT_Prelaunch_2019_2020/User_Guide_SWOT_Prelaunch_2019_2020.pdf .",
-            "issued": "2022-03-02",
-            "temporal": "2019-09-05T00:00:00Z/2020-01-19T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-19",
-            "references": [
-                "https://doi.org/10.1175/jtech-d-21-0039.1"
-            ],
-            "keyword": [
-                "earth science",
-                "oceans",
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
-            "identifier": "C2229635778-POCLOUD",
-            "description": "This dataset provides the 1Hz time series of the sea surface height measured by a surface buoy equipped with a Global Position System (GPS). The GPS-mooring was deployed by the SWOT prelaunch field campaign conducted near the SWOT CalVal crossover location, about 300 kilometers west of Monterey, California between September, 2019 and January, 2020. The GPS measurements represent the total sea surface height including the Inverted barometer component. The same mooring also carries fixed-depth CTD sensors https://doi.org/10.5067/SWTPR-CTD11. They were used together with atmospheric pressure and bottom pressure measurements to close the sea surface equation (Wang et al., 2022). The campaign also deployed another two CTD moorings, a slocum glider, and a Pressure Inverted Echo Sounder (PIES). Details can be found in the user guide and the journal reference given in the documentation section.",
-            "graphic-preview-description": "Thumbnail",
             "creator": "SWOT pre-launch field campaign",
-            "title": "SWOT 2019-2020 Prelaunch Oceanography Field Campaign JPL Global Positioning Systems (GPS)",
-            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/SWOT_PRELAUNCH_L2_GPS_V1.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "This dataset provides the 1Hz time series of the sea surface height measured by a surface buoy equipped with a Global Position System (GPS). The GPS-mooring was deployed by the SWOT prelaunch field campaign conducted near the SWOT CalVal crossover location, about 300 kilometers west of Monterey, California between September, 2019 and January, 2020. The GPS measurements represent the total sea surface height including the Inverted barometer component. The same mooring also carries fixed-depth CTD sensors https://doi.org/10.5067/SWTPR-CTD11. They were used together with atmospheric pressure and bottom pressure measurements to close the sea surface equation (Wang et al., 2022). The campaign also deployed another two CTD moorings, a slocum glider, and a Pressure Inverted Echo Sounder (PIES). Details can be found in the user guide and the journal reference given in the documentation section.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSWTPR-GPS01",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSWTPR-GPS01",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/web-misc/SWOT/SWOT_Prelaunch_2019_2020/User_Guide_SWOT_Prelaunch_2019_2020.pdf",
-                    "description": "User's Guide",
                     "@type": "dcat:Distribution",
+                    "description": "User's Guide",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/web-misc/SWOT/SWOT_Prelaunch_2019_2020/User_Guide_SWOT_Prelaunch_2019_2020.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://podaac.jpl.nasa.gov/swot",
-                    "description": "Field Campaign and Instrument Overview for SWOT",
                     "@type": "dcat:Distribution",
+                    "description": "Field Campaign and Instrument Overview for SWOT",
+                    "downloadURL": "http://podaac.jpl.nasa.gov/swot",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/SWOT_PRELAUNCH_L2_GPS_V1.jpg",
-                    "description": "Thumbnail",
                     "@type": "dcat:Distribution",
+                    "description": "Thumbnail",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/SWOT_PRELAUNCH_L2_GPS_V1.jpg",
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
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2229635778-POCLOUD",
-                    "description": "HTTPS endpoint for data browse and download",
                     "@type": "dcat:Distribution",
+                    "description": "HTTPS endpoint for data browse and download",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2229635778-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2229635778-POCLOUD",
-                    "description": "Browse granule search results in Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse granule search results in Earthdata Search",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2229635778-POCLOUD",
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
+            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/SWOT_PRELAUNCH_L2_GPS_V1.jpg",
+            "identifier": "C2229635778-POCLOUD",
+            "issued": "2022-03-02",
+            "keyword": [
+                "earth science",
+                "oceans",
+                "sea surface topography"
+            ],
+            "landingPage": "https://doi.org/10.5067/SWTPR-GPS01",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2020-01-19",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/JPL/PODAAC"
+            },
+            "references": [
+                "https://doi.org/10.1175/jtech-d-21-0039.1"
+            ],
             "spatial": "-125.2 35.8 -125.0 36.2",
+            "temporal": "2019-09-05T00:00:00Z/2020-01-19T23:59:59.999Z",
             "theme": [
                 "SWOT",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "SWOT 2019-2020 Prelaunch Oceanography Field Campaign JPL Global Positioning Systems (GPS)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=IHW-C-IRSPEC-N-NDR-HALLEY-V1.0",
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
+            "description": "NASA's International Halley Watch (IHW) has created a Comet Halley Archive. The collection of data spans the full wavelength range as submitted by scientists to the IHW. The observations belong to one of the following Disciplines: Amateur, Astrometry, Infrared Studies, Large-Scale Phenomena, Meteor Studies, Near-Nucleus Studies, Photometry and Polarimetry, Radio Studies, and Spectroscopy and Spectrophotometry. The data collected by these nine disciplines were augmented by Spacecraft measurements. The data were submitted to IHW, but the evaluation and selection for the Archive has been the primary responsibility of the Discipline Specialist Teams for each network in cooperation with the Lead Center. The data from the Infrared Spectroscopy Subnetwork contains 24 citations of recorded Halley spectra in logs or publications. The data covers dates from 1985 December 21 through 1986 April 29.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ihw-c-irspec-n-ndr-halley-v1.0_9a7k-b7mv",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international halley watch",
+                "halley"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=IHW-C-IRSPEC-N-NDR-HALLEY-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ihw-c-irspec-n-ndr-halley-v1.0_9a7k-b7mv",
-            "description": "NASA's International Halley Watch (IHW) has created a Comet Halley Archive. The collection of data spans the full wavelength range as submitted by scientists to the IHW. The observations belong to one of the following Disciplines: Amateur, Astrometry, Infrared Studies, Large-Scale Phenomena, Meteor Studies, Near-Nucleus Studies, Photometry and Polarimetry, Radio Studies, and Spectroscopy and Spectrophotometry. The data collected by these nine disciplines were augmented by Spacecraft measurements. The data were submitted to IHW, but the evaluation and selection for the Archive has been the primary responsibility of the Discipline Specialist Teams for each network in cooperation with the Lead Center. The data from the Infrared Spectroscopy Subnetwork contains 24 citations of recorded Halley spectra in logs or publications. The data covers dates from 1985 December 21 through 1986 April 29.",
-            "title": "IHW COMET HALLEY INFRARED SPECTRA REFERENCES V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "IHW COMET HALLEY INFRARED SPECTRA REFERENCES V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=DAWN-A-VIR-2-EDR-IR-VESTA-SPECTRA-V2.0",
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
+            "description": "This data set contains the raw           infrared channel digital numbers (DN) contained in the telemetry         packages taken by the Dawn VIR spectrometer for all Vesta encounter      mission phaes. The data in this version of the data set include          minor updates to the data files and labels. The data cover the time      period between 2011-05-03 and 2012-07-18.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.dawn-a-vir-2-edr-ir-vesta-spectra-v2.0_9abx-px4j",
+            "issued": "2018-06-26",
+            "keyword": [
+                "4 vesta",
+                "dawn mission to vesta and ceres"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=DAWN-A-VIR-2-EDR-IR-VESTA-SPECTRA-V2.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.dawn-a-vir-2-edr-ir-vesta-spectra-v2.0_9abx-px4j",
-            "description": "This data set contains the raw           infrared channel digital numbers (DN) contained in the telemetry         packages taken by the Dawn VIR spectrometer for all Vesta encounter      mission phaes. The data in this version of the data set include          minor updates to the data files and labels. The data cover the time      period between 2011-05-03 and 2012-07-18.",
-            "title": "DAWN VIR RAW (EDR) VESTA INFRARED SPECTRA V2.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "DAWN VIR RAW (EDR) VESTA INFRARED SPECTRA V2.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1883",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Kyzivat, E.D., L.C. Smith, C. Huang, C. Wang, T. Langhorst, J.V. Fayne, M.E. Harlan, Y. Ishitsuka, D. Feng, L.H. Pitcher, and T.M. Pavelsky. 2021. ABoVE: Lake and Wetland Classification from L-band SAR, Alaska and Canada, 2017-2019. ORNL DAAC, Oak Ridge, Tennessee, USA. https://doi.org/10.3334/ORNLDAAC/1883",
-            "issued": "2021-12-21",
-            "temporal": "2017-01-01T00:00:00Z/2019-09-19T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-06-12",
-            "keyword": [
-                "land use/land cover",
-                "surface water",
-                "terrestrial hydrosphere",
-                "biosphere",
-                "ecosystems",
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
-            "identifier": "C2192619280-ORNL_CLOUD",
             "description": "This dataset contains a high-resolution land cover classification focused on water and wetland vegetation classes over three NASA ABoVE Campaign regions: Yukon Flats, Alaska, USA; the Peace-Athabasca Delta, Alberta; and the Canadian Shield, Northwest Territories (NWT), Canada. The product was derived from L-band synthetic aperture radar (SAR) acquisitions from the airborne NASA UAVSAR instrument in 2017-2019. The classification was trained and validated from field visits, UAV images, satellite imagery as well as other ABoVE datasets. Classifications in all regions are provided as both preliminary 13-class versions and final, simplified 5-class versions. Training and test data used for the classifier are also included as well as characteristics of lakes in the study area. This land cover classification was developed to support a project focusing on potential methane emissions from the shallow near-shore, or littoral, regions of lakes. The emergent aquatic vegetation classes can be used as a proxy for these littoral zones. Wetland vegetation classifications are provided as gridded raster files with an approximately 5-meter spatial resolution and aligned with the original UAVSAR footprints. Composite mosaics that aggregate these UAVSAR scenes by region and day of acquisition, if applicable, are also provided. Classifications in all regions are provided as both preliminary 13-class versions and final 5-class versions.",
-            "graphic-preview-description": "A preliminary wetland classification for Canadian Shield lakes north of Yellowknife, NWT, Canada. Missing data in some lakes appear as white spots. Source: bakerc_16008_19059_012_190904_L090_CX_01_Freeman-inc_cls.tif",
-            "title": "ABoVE: Lake and Wetland Classification from L-band SAR, Alaska and Canada, 2017-2019",
-            "graphic-preview-file": "https://daac.ornl.gov/ABOVE/guides/Lake_Wetland_Classes_UAVSAR_Fig1.jpg",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1883",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1883",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/above/Lake_Wetland_Classes_UAVSAR/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/above/Lake_Wetland_Classes_UAVSAR/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/ABOVE/guides/Lake_Wetland_Classes_UAVSAR.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/ABOVE/guides/Lake_Wetland_Classes_UAVSAR.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1883",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1883",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/Lake_Wetland_Classes_UAVSAR/comp/13-classes-arcgis.lyr",
-                    "description": "ABoVE: Lake and Wetland Classification from L-band SAR, Alaska and Canada, 2017-2019: 13-classes-arcgis.lyr",
                     "@type": "dcat:Distribution",
+                    "description": "ABoVE: Lake and Wetland Classification from L-band SAR, Alaska and Canada, 2017-2019: 13-classes-arcgis.lyr",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/Lake_Wetland_Classes_UAVSAR/comp/13-classes-arcgis.lyr",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/Lake_Wetland_Classes_UAVSAR/comp/13-classes-qgis.qml",
-                    "description": "ABoVE: Lake and Wetland Classification from L-band SAR, Alaska and Canada, 2017-2019: 13-classes-qgis.qml",
                     "@type": "dcat:Distribution",
+                    "description": "ABoVE: Lake and Wetland Classification from L-band SAR, Alaska and Canada, 2017-2019: 13-classes-qgis.qml",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/Lake_Wetland_Classes_UAVSAR/comp/13-classes-qgis.qml",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/Lake_Wetland_Classes_UAVSAR/comp/5-classes-arcgis.lyr",
-                    "description": "ABoVE: Lake and Wetland Classification from L-band SAR, Alaska and Canada, 2017-2019: 5-classes-arcgis.lyr",
                     "@type": "dcat:Distribution",
+                    "description": "ABoVE: Lake and Wetland Classification from L-band SAR, Alaska and Canada, 2017-2019: 5-classes-arcgis.lyr",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/Lake_Wetland_Classes_UAVSAR/comp/5-classes-arcgis.lyr",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/Lake_Wetland_Classes_UAVSAR/comp/5-classes-qgis.qml",
-                    "description": "ABoVE: Lake and Wetland Classification from L-band SAR, Alaska and Canada, 2017-2019: 5-classes-qgis.qml",
                     "@type": "dcat:Distribution",
+                    "description": "ABoVE: Lake and Wetland Classification from L-band SAR, Alaska and Canada, 2017-2019: 5-classes-qgis.qml",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/Lake_Wetland_Classes_UAVSAR/comp/5-classes-qgis.qml",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/Lake_Wetland_Classes_UAVSAR/comp/Lake_Wetland_Classes_UAVSAR.pdf",
-                    "description": "ABoVE: Lake and Wetland Classification from L-band SAR, Alaska and Canada, 2017-2019: Lake_Wetland_Classes_UAVSAR.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "ABoVE: Lake and Wetland Classification from L-band SAR, Alaska and Canada, 2017-2019: Lake_Wetland_Classes_UAVSAR.pdf",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/Lake_Wetland_Classes_UAVSAR/comp/Lake_Wetland_Classes_UAVSAR.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/vnd.google-earth.kml+xml",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/Lake_Wetland_Classes_UAVSAR/comp/Study-areas.kml",
-                    "description": "ABoVE: Lake and Wetland Classification from L-band SAR, Alaska and Canada, 2017-2019: Study-areas.kml",
                     "@type": "dcat:Distribution",
+                    "description": "ABoVE: Lake and Wetland Classification from L-band SAR, Alaska and Canada, 2017-2019: Study-areas.kml",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/Lake_Wetland_Classes_UAVSAR/comp/Study-areas.kml",
+                    "mediaType": "application/vnd.google-earth.kml+xml",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/vnd.google-earth.kml+xml",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/Lake_Wetland_Classes_UAVSAR/comp/UAVSAR_classification_footprints.kml",
-                    "description": "ABoVE: Lake and Wetland Classification from L-band SAR, Alaska and Canada, 2017-2019: UAVSAR_classification_footprints.kml",
                     "@type": "dcat:Distribution",
+                    "description": "ABoVE: Lake and Wetland Classification from L-band SAR, Alaska and Canada, 2017-2019: UAVSAR_classification_footprints.kml",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/Lake_Wetland_Classes_UAVSAR/comp/UAVSAR_classification_footprints.kml",
+                    "mediaType": "application/vnd.google-earth.kml+xml",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://daac.ornl.gov/ABOVE/guides/Lake_Wetland_Classes_UAVSAR_Fig1.jpg",
-                    "description": "A preliminary wetland classification for Canadian Shield lakes north of Yellowknife, NWT, Canada. Missing data in some lakes appear as white spots. Source: bakerc_16008_19059_012_190904_L090_CX_01_Freeman-inc_cls.tif",
                     "@type": "dcat:Distribution",
+                    "description": "A preliminary wetland classification for Canadian Shield lakes north of Yellowknife, NWT, Canada. Missing data in some lakes appear as white spots. Source: bakerc_16008_19059_012_190904_L090_CX_01_Freeman-inc_cls.tif",
+                    "downloadURL": "https://daac.ornl.gov/ABOVE/guides/Lake_Wetland_Classes_UAVSAR_Fig1.jpg",
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
+            "graphic-preview-description": "A preliminary wetland classification for Canadian Shield lakes north of Yellowknife, NWT, Canada. Missing data in some lakes appear as white spots. Source: bakerc_16008_19059_012_190904_L090_CX_01_Freeman-inc_cls.tif",
+            "graphic-preview-file": "https://daac.ornl.gov/ABOVE/guides/Lake_Wetland_Classes_UAVSAR_Fig1.jpg",
+            "identifier": "C2192619280-ORNL_CLOUD",
+            "issued": "2021-12-21",
+            "keyword": [
+                "land use/land cover",
+                "surface water",
+                "terrestrial hydrosphere",
+                "biosphere",
+                "ecosystems",
+                "land surface",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1883",
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
             "spatial": "-149.16 53.71 -107.86 67.91",
+            "temporal": "2017-01-01T00:00:00Z/2019-09-19T23:59:59Z",
             "theme": [
                 "ABoVE",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "ABoVE: Lake and Wetland Classification from L-band SAR, Alaska and Canada, 2017-2019"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC2-0840-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 2 phase 2015-03-11 to 2015-06-30. It is a Global Gravity measurement at the comet 67P and covers the time 2015-06-12T20:59:20.000 to 2015-06-13T06:09:14.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc2-0840-v1.0_9ag3-tyez",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC2-0840-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc2-0840-v1.0_9ag3-tyez",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 2 phase 2015-03-11 to 2015-06-30. It is a Global Gravity measurement at the comet 67P and covers the time 2015-06-12T20:59:20.000 to 2015-06-13T06:09:14.000.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 2 0840 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 2 0840 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/SWOT-RIVERSP-2.0",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Surface Water Ocean Topography (SWOT). 2024-02-01. SWOT Level 2 River Single-Pass Vector Node Data Product. Version 2.0. SWOT Level 2 River Single-Pass Vector Node Data Product, Version 2.0. Jet Propulsion Laboratory. Archived by National Aeronautics and Space Administration, U.S. Government, JPL NASA. https://doi.org/10.5067/SWOT-RIVERSP-2.0. https://swot.jpl.nasa.gov/.",
-            "issued": "2022-07-20",
-            "temporal": "2022-12-16T00:00:00Z/2024-03-27T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-07-20",
-            "keyword": [
-                "terrestrial hydrosphere",
-                "surface water",
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
-            "identifier": "C2799438301-POCLOUD",
-            "description": "The SWOT Level 2 River Single-Pass Vector Node Data Product from the Surface Water Ocean Topography (SWOT) mission provides water surface elevation, slope, width, and discharge derived from the high rate (HR) data stream from the Ka-band Radar Interferometer (KaRIn). SWOT launched on December 16, 2022 from Vandenberg Air Force Base in California into a 1-day repeat orbit for the \"calibration\" or \"fast-sampling\" phase of the mission, which completed in early July 2023. After the calibration phase, SWOT entered a 21-day repeat orbit in August 2023 to start the \"science\" phase of the mission, which is expected to continue through 2025. <br>\r\nWater surface elevation, slope, width, and discharge are provided for river reaches (approximately 10 km long) and nodes (approximately 200 m spacing) identified in the prior river database, and distributed as feature datasets covering the full swath for each continent-pass. These data are generally produced for inland and coastal hydrology surfaces, as controlled by the reloadable KaRIn HR mask. The dataset is distributed in ESRI Shapefile format. <br>\r\nThis collection is a sub-collection of its parent: https://podaac.jpl.nasa.gov/dataset/SWOT_L2_HR_RiverSP_2.0 It contains only river nodes.",
-            "release-place": "Jet Propulsion Laboratory",
-            "series-name": "SWOT Level 2 River Single-Pass Vector Node Data Product",
-            "graphic-preview-description": "Thumbnail",
             "creator": "Surface Water Ocean Topography (SWOT)",
-            "title": "SWOT Level 2 River Single-Pass Vector Node Data Product, Version 2.0",
-            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/SWOT_L2_HR_RiverSP_2.0.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The SWOT Level 2 River Single-Pass Vector Node Data Product from the Surface Water Ocean Topography (SWOT) mission provides water surface elevation, slope, width, and discharge derived from the high rate (HR) data stream from the Ka-band Radar Interferometer (KaRIn). SWOT launched on December 16, 2022 from Vandenberg Air Force Base in California into a 1-day repeat orbit for the \"calibration\" or \"fast-sampling\" phase of the mission, which completed in early July 2023. After the calibration phase, SWOT entered a 21-day repeat orbit in August 2023 to start the \"science\" phase of the mission, which is expected to continue through 2025. <br>\r\nWater surface elevation, slope, width, and discharge are provided for river reaches (approximately 10 km long) and nodes (approximately 200 m spacing) identified in the prior river database, and distributed as feature datasets covering the full swath for each continent-pass. These data are generally produced for inland and coastal hydrology surfaces, as controlled by the reloadable KaRIn HR mask. The dataset is distributed in ESRI Shapefile format. <br>\r\nThis collection is a sub-collection of its parent: https://podaac.jpl.nasa.gov/dataset/SWOT_L2_HR_RiverSP_2.0 It contains only river nodes.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSWOT-RIVERSP-2.0",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSWOT-RIVERSP-2.0",
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
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2799438301-POCLOUD",
-                    "description": "HTTPS endpoint for data browse and download",
                     "@type": "dcat:Distribution",
+                    "description": "HTTPS endpoint for data browse and download",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2799438301-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2799438301-POCLOUD",
-                    "description": "Browse granule search results in Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse granule search results in Earthdata Search",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2799438301-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/SWOT_L2_HR_RiverSP_2.0.jpg",
-                    "description": "Thumbnail",
                     "@type": "dcat:Distribution",
+                    "description": "Thumbnail",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/SWOT_L2_HR_RiverSP_2.0.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/web-misc/swot_mission_docs/pdd/D-105505_SWOT_ATBD_L2_HR_RiverSP_20230713_cite.pdf",
-                    "description": "Product Description Document (PDD)",
                     "@type": "dcat:Distribution",
+                    "description": "Product Description Document (PDD)",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/web-misc/swot_mission_docs/pdd/D-105505_SWOT_ATBD_L2_HR_RiverSP_20230713_cite.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/web-misc/swot_mission_docs/atbd/D-56413_SWOT_Product_Description_L2_HR_RiverSP_20231026_RevBcite.pdf",
-                    "description": "Algorithm Theoretical Basis Document (ATBD)",
                     "@type": "dcat:Distribution",
+                    "description": "Algorithm Theoretical Basis Document (ATBD)",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/web-misc/swot_mission_docs/atbd/D-56413_SWOT_Product_Description_L2_HR_RiverSP_20231026_RevBcite.pdf",
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
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2799438301-POCLOUD&pg%5B0%5D%5Bid%5D=*PIC0*",
-                    "description": "Search Granules from Forward Processing (PIC0)",
                     "@type": "dcat:Distribution",
+                    "description": "Search Granules from Forward Processing (PIC0)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2799438301-POCLOUD&pg%5B0%5D%5Bid%5D=*PIC0*",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2799438301-POCLOUD&pg%5B0%5D%5Bid%5D=*PGC0*",
-                    "description": "Search Granules from Bulk Reprocessing (PGC0)",
                     "@type": "dcat:Distribution",
+                    "description": "Search Granules from Bulk Reprocessing (PGC0)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2799438301-POCLOUD&pg%5B0%5D%5Bid%5D=*PGC0*",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 }
             ],
+            "graphic-preview-description": "Thumbnail",
+            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/SWOT_L2_HR_RiverSP_2.0.jpg",
+            "identifier": "C2799438301-POCLOUD",
+            "issued": "2022-07-20",
+            "keyword": [
+                "terrestrial hydrosphere",
+                "surface water",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/SWOT-RIVERSP-2.0",
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
+            "series-name": "SWOT Level 2 River Single-Pass Vector Node Data Product",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2022-12-16T00:00:00Z/2024-03-27T00:00:00Z",
             "theme": [
                 "SWOT",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "SWOT Level 2 River Single-Pass Vector Node Data Product, Version 2.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=LP-L-6-EPHEMERIS-V1.0",
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
-                "lunar prospector",
-                "moon"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "The Lunar Prospector ephemeris data set consists of spacecraft position and velocity determinations as a function of time in Moon-centered, Earth equator, mean of J2000 coordinates. Tracking data collected by ground stations are used by the Goddard Flight Dynamics Analysis Branch (FDAB) to compute the Lunar Prospector orbit ephemeris. The Level 0 Data archive contains the ephemeris type known as the 'definitive ephemeris', which is based on an updated lunar gravity model [FDAB1997].",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.lp-l-6-ephemeris-v1.0_9aj6-rbku",
+            "issued": "2021-05-21",
+            "keyword": [
+                "lunar prospector",
+                "moon"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=LP-L-6-EPHEMERIS-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.lp-l-6-ephemeris-v1.0_9aj6-rbku",
-            "description": "The Lunar Prospector ephemeris data set consists of spacecraft position and velocity determinations as a function of time in Moon-centered, Earth equator, mean of J2000 coordinates. Tracking data collected by ground stations are used by the Goddard Flight Dynamics Analysis Branch (FDAB) to compute the Lunar Prospector orbit ephemeris. The Level 0 Data archive contains the ephemeris type known as the 'definitive ephemeris', which is based on an updated lunar gravity model [FDAB1997].",
-            "title": "LP MOON SPACECRAFT EPHEMERIS V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "LP MOON SPACECRAFT EPHEMERIS V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-MIRO-3-PRL-67P-V3.0",
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
+            "description": "This data set contains Spectroscopic and Continuum, level 3 data, in the form of table files, taken during the ROSETTA COMET Prelanding phase of the Rosetta mission to comet 67P/CHURYUMOV-GERASIMENKO by the MIRO instrument.  It supercedes dataset RO-C-MIRO-3-PRL-67P-V2.0. The updates include a new calibration algorithm and modified documentation.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-miro-3-prl-67p-v3.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-MIRO-3-PRL-67P-V3.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-miro-3-prl-67p-v3.0",
-            "description": "This data set contains Spectroscopic and Continuum, level 3 data, in the form of table files, taken during the ROSETTA COMET Prelanding phase of the Rosetta mission to comet 67P/CHURYUMOV-GERASIMENKO by the MIRO instrument.  It supercedes dataset RO-C-MIRO-3-PRL-67P-V2.0. The updates include a new calibration algorithm and modified documentation.",
-            "title": "ROSETTA-ORBITER 67P MIRO 3 PRL V3.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P MIRO 3 PRL V3.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/960",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Moody, E.G., M.D. King, C. Schaaf,  F. Gao, F.G. Hall, G.J. Collatz, B.W. Meeson, S.O. Los, E.Brown De Colstoun, and D.R. Landis. 2009. ISLSCP II Snow-Free, Spatially Complete, 16 Day Albedo, 2002. ORNL DAAC, Oak Ridge, Tennessee, USA. https://doi.org/10.3334/ORNLDAAC/960",
-            "issued": "2023-10-15",
-            "temporal": "2002-01-01T00:00:00Z/2002-12-31T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-10-17",
-            "keyword": [
-                "ngda",
-                "national geospatial data asset",
-                "earth science",
-                "land surface",
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
-            "identifier": "C2784886599-ORNL_CLOUD",
             "description": "This data set, ISLSCP II Snow-Free, Spatially Complete, 16 Day Albedo, 2002, contains 9 files for snow-free, spatially complete 16-day global black-sky albedos at local solar noon, white-sky albedos and quality information based on MODerate Resolution Imaging Spectroradiometer (MODIS) Collection 4 Albedo Products (MOD43B3). Data are provided for 7 spectral bands and 3 broad bands for a full year of MODIS data (2002). An ecosystem-dependent temporal interpolation technique was developed to fill any missing or seasonally snow-covered data in the official MOD43B3 albedo product. The resulting data set maintains the original resolution and data of the MOD43B3 product while replacing fill values to provide snow-free spatially complete maps.",
-            "graphic-preview-description": "Browse Image",
-            "title": "ISLSCP II Snow-Free, Spatially Complete, 16 Day Albedo, 2002",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/sdat-tds/960_1_fit.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F960",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F960",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/islscp_ii/vegetation/modis_albedo_2002_filled_xdeg/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/islscp_ii/vegetation/modis_albedo_2002_filled_xdeg/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/ISLSCP_II/guides/islscp_ii_monthly_snowfree_albedo_16day.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/ISLSCP_II/guides/islscp_ii_monthly_snowfree_albedo_16day.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/960",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/960",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/islscp_ii/vegetation/modis_albedo_2002_filled_xdeg/comp/0_modis_fill_alb_readme.txt",
-                    "description": "Data set text file containing the file naming convention and data formats of the granules in this collection.",
                     "@type": "dcat:Distribution",
+                    "description": "Data set text file containing the file naming convention and data formats of the granules in this collection.",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/islscp_ii/vegetation/modis_albedo_2002_filled_xdeg/comp/0_modis_fill_alb_readme.txt",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/islscp_ii/vegetation/modis_albedo_2002_filled_xdeg/comp/1_modis_fill_alb_2002_doc.pdf",
-                    "description": "Data set documentation PDF.",
                     "@type": "dcat:Distribution",
+                    "description": "Data set documentation PDF.",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/islscp_ii/vegetation/modis_albedo_2002_filled_xdeg/comp/1_modis_fill_alb_2002_doc.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://daac.ornl.gov/graphics/browse/sdat-tds/960_1_fit.png",
-                    "description": "Browse Image",
                     "@type": "dcat:Distribution",
+                    "description": "Browse Image",
+                    "downloadURL": "https://daac.ornl.gov/graphics/browse/sdat-tds/960_1_fit.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://webmap.ornl.gov/wcsdown/dataset.jsp?ds_id=960",
-                    "description": "Web Coverage Service for this collection.",
                     "@type": "dcat:Distribution",
+                    "description": "Web Coverage Service for this collection.",
+                    "downloadURL": "https://webmap.ornl.gov/wcsdown/dataset.jsp?ds_id=960",
+                    "mediaType": "text/html",
                     "title": "Use Web Coverage Service (WCS) to download the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://thredds.daac.ornl.gov/thredds/catalog/ornldaac/960/catalog.html",
-                    "description": "The THREDDS location for this Collection.",
                     "@type": "dcat:Distribution",
+                    "description": "The THREDDS location for this Collection.",
+                    "downloadURL": "https://thredds.daac.ornl.gov/thredds/catalog/ornldaac/960/catalog.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "graphic-preview-description": "Browse Image",
+            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/sdat-tds/960_1_fit.png",
+            "identifier": "C2784886599-ORNL_CLOUD",
+            "issued": "2023-10-15",
+            "keyword": [
+                "ngda",
+                "national geospatial data asset",
+                "earth science",
+                "land surface",
+                "surface radiative properties"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/960",
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
+            "temporal": "2002-01-01T00:00:00Z/2002-12-31T23:59:59Z",
             "theme": [
                 "ISLSCP II",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "ISLSCP II Snow-Free, Spatially Complete, 16 Day Albedo, 2002"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-P-ALICE-3-PLUTO-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This data set contains Calibrated data taken by the New Horizons         Alice Ultraviolet Imaging Spectrograph                                 instrument during the                                                    Pluto encounter                                                        mission phase.  This is VERSION 1.0 of this data set.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-p-alice-3-pluto-v1.0_9ask-q7fv",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "pluto",
                 "sun",
                 "new horizons"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-P-ALICE-3-PLUTO-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-p-alice-3-pluto-v1.0_9ask-q7fv",
-            "description": "This data set contains Calibrated data taken by the New Horizons         Alice Ultraviolet Imaging Spectrograph                                 instrument during the                                                    Pluto encounter                                                        mission phase.  This is VERSION 1.0 of this data set.",
-            "title": "NEW HORIZONS                            \n      ALICE PLUTO ENCOUNTER                                                   \n      CALIBRATED V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "NEW HORIZONS                            \n      ALICE PLUTO ENCOUNTER                                                   \n      CALIBRATED V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MER2-M-PANCAM-5-ROUGHNESS-OPS-V1.0",
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
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mer2-m-pancam-5-roughness-ops-v1.0_9ati-j7hi",
+            "issued": "2018-06-26",
+            "keyword": [
+                "mars exploration rover",
+                "mars"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MER2-M-PANCAM-5-ROUGHNESS-OPS-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mer2-m-pancam-5-roughness-ops-v1.0_9ati-j7hi",
-            "description": "not applicable",
-            "title": "MER 2 MARS PANORAMIC CAMERA SURFACE ROUGH RDR OPS V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "MER 2 MARS PANORAMIC CAMERA SURFACE ROUGH RDR OPS V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/667",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Hyman, A., W. Lucht, and A. Strahler. 2003. PROVE Surface albedo of Jornada Experimental Range, New Mexico, 1997. ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/667",
-            "issued": "2023-11-19",
-            "temporal": "1997-05-22T00:00:00Z/1997-05-27T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-11-20",
-            "keyword": [
-                "visible wavelengths",
-                "surface radiative properties",
-                "spectral/engineering",
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
-            "identifier": "C2804796522-ORNL_CLOUD",
             "description": "The objective of this study was to determine the spatial variations in field measurements of broadband albedo as related to the ground cover and under a range of solar conditions during the Prototype Validation Exercise (PROVE) at the Jornada Experimental Range in New Mexico on May 20-30, 1997.",
-            "graphic-preview-description": "Browse Image",
-            "title": "PROVE Surface albedo of Jornada Experimental Range, New Mexico, 1997",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/prove_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F667",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F667",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/prove/jornada_albedo/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/prove/jornada_albedo/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/PROVE/guides/prove_albedo_guide.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/PROVE/guides/prove_albedo_guide.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/667",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/667",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/prove/jornada_albedo/comp/albedo_new_readme.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/prove/jornada_albedo/comp/albedo_new_readme.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/prove/jornada_albedo/comp/albedo_new_readme.txt",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/prove/jornada_albedo/comp/albedo_new_readme.txt",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/prove/jornada_albedo/comp/albedo_original_readme.txt",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/prove/jornada_albedo/comp/albedo_original_readme.txt",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/prove/jornada_albedo/comp/east_site1_classified.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/prove/jornada_albedo/comp/east_site1_classified.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/prove/jornada_albedo/comp/east_site1_photo.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/prove/jornada_albedo/comp/east_site1_photo.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/prove/jornada_albedo/comp/Hyman_Jornada_albedo_thesis.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/prove/jornada_albedo/comp/Hyman_Jornada_albedo_thesis.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/prove/jornada_albedo/comp/longeast48.5_classified.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/prove/jornada_albedo/comp/longeast48.5_classified.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/prove/jornada_albedo/comp/longeast48.5_photo.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/prove/jornada_albedo/comp/longeast48.5_photo.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/prove/jornada_albedo/comp/prove_albedo_guide.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/prove/jornada_albedo/comp/prove_albedo_guide.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/prove/jornada_albedo/comp/west_site9_classified.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/prove/jornada_albedo/comp/west_site9_classified.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/prove/jornada_albedo/comp/west_site9_photo.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/prove/jornada_albedo/comp/west_site9_photo.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://daac.ornl.gov/graphics/browse/project/square/prove_logo_square.png",
-                    "description": "Browse Image",
                     "@type": "dcat:Distribution",
+                    "description": "Browse Image",
+                    "downloadURL": "https://daac.ornl.gov/graphics/browse/project/square/prove_logo_square.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 }
             ],
+            "graphic-preview-description": "Browse Image",
+            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/prove_logo_square.png",
+            "identifier": "C2804796522-ORNL_CLOUD",
+            "issued": "2023-11-19",
+            "keyword": [
+                "visible wavelengths",
+                "surface radiative properties",
+                "spectral/engineering",
+                "land use/land cover",
+                "land surface",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/667",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2023-11-20",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "ORNL_DAAC"
+            },
             "spatial": "32.5 -106.75",
+            "temporal": "1997-05-22T00:00:00Z/1997-05-27T23:59:59Z",
             "theme": [
                 "PROVE",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "PROVE Surface albedo of Jornada Experimental Range, New Mexico, 1997"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/L4Y1YYH4CI4R",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "OCO Science Team/Michael Gunson, Annmarie Eldering. 2024-04-10. OCO3_L2_Standard. Version 11r. OCO-3 Level 2 geolocated XCO2 retrievals results, physical model, Retrospective Processing V11r. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/L4Y1YYH4CI4R. https://disc.gsfc.nasa.gov/datacollection/OCO3_L2_Standard_11r.html. Digital Science Data.",
-            "issued": "2021-05-31",
-            "temporal": "2019-08-06T00:00:00Z/2024-10-07T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2021-05-31",
-            "keyword": [
-                "earth science",
-                "atmosphere",
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
-            "identifier": "C2910086890-GES_DISC",
-            "description": "Version 11r is the current version of the data set. Older versions will no longer be available and are superseded by Version 11r.\n\nThe Orbiting Carbon Observatory -3 (OCO-3) was deployed to the International Space Station in May, 2019. It is technically a single instrument, almost identical to OCO-2.\n\nThe Orbiting Carbon Observatory is the first NASA mission designed to collect space-based measurements of atmospheric carbon dioxide with the precision, resolution, and coverage needed to characterize the processes controlling its buildup in the atmosphere.\n\nOCO-3 incorporates three high-resolution spectrometers that make coincident measurements of reflected sunlight in the near-infrared CO2 near 1.61 and 2.06 micrometers and in molecular oxygen (O2) A-Band at 0.76 micrometers. The three spectrometers have different characteristics and are calibrated independently. \n\nOxygen-A Band cloud screening algorithm is one of the primary cloud screening tools implemented in the operational OCO processing pipeline. The algorithm was introduced and applied to early GOSAT data  with further analysis performed on OCO-2 simulations.\n\nThe OCO ABO2 algorithm employs a fast Bayesian retrieval to estimate surface pressure and surface albedo from high resolution spectra of the molecular oxygen (O2) A-band, near 0.765 \u00b5m. The radiative transfer forward model (FM) assumes a clear-sky condition, i.e. Rayleigh scattering only, such that differences between the modeled and measured radiances are apparent when the measurement scene contains cloud or aerosol.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "OCO3_L2_Standard",
             "creator": "OCO Science Team/Michael Gunson, Annmarie Eldering",
-            "title": "OCO-3 Level 2 geolocated XCO2 retrievals results, physical model, Retrospective Processing V11r (OCO3_L2_Standard) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/OCO/OCO3_logo.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "data-presentation-form": "Digital Science Data",
+            "description": "Version 11r is the current version of the data set. Older versions will no longer be available and are superseded by Version 11r.\n\nThe Orbiting Carbon Observatory -3 (OCO-3) was deployed to the International Space Station in May, 2019. It is technically a single instrument, almost identical to OCO-2.\n\nThe Orbiting Carbon Observatory is the first NASA mission designed to collect space-based measurements of atmospheric carbon dioxide with the precision, resolution, and coverage needed to characterize the processes controlling its buildup in the atmosphere.\n\nOCO-3 incorporates three high-resolution spectrometers that make coincident measurements of reflected sunlight in the near-infrared CO2 near 1.61 and 2.06 micrometers and in molecular oxygen (O2) A-Band at 0.76 micrometers. The three spectrometers have different characteristics and are calibrated independently. \n\nOxygen-A Band cloud screening algorithm is one of the primary cloud screening tools implemented in the operational OCO processing pipeline. The algorithm was introduced and applied to early GOSAT data  with further analysis performed on OCO-2 simulations.\n\nThe OCO ABO2 algorithm employs a fast Bayesian retrieval to estimate surface pressure and surface albedo from high resolution spectra of the molecular oxygen (O2) A-band, near 0.765 \u00b5m. The radiative transfer forward model (FM) assumes a clear-sky condition, i.e. Rayleigh scattering only, such that differences between the modeled and measured radiances are apparent when the measurement scene contains cloud or aerosol.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FL4Y1YYH4CI4R",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FL4Y1YYH4CI4R",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
@@ -411889,59 +411867,59 @@
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/OCO3_L2_Standard_11r.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/OCO3_L2_Standard_11r.html",
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
-                    "downloadURL": "https://oco2.gesdisc.eosdis.nasa.gov/data/OCO3_DATA/OCO3_L2_Standard.11r/",
-                    "description": "Access the data via HTTP",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTP",
+                    "downloadURL": "https://oco2.gesdisc.eosdis.nasa.gov/data/OCO3_DATA/OCO3_L2_Standard.11r/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=OCO3_L2_Standard",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=OCO3_L2_Standard",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://oco2.gesdisc.eosdis.nasa.gov/opendap/OCO3_L2_Standard.10r/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://oco2.gesdisc.eosdis.nasa.gov/opendap/OCO3_L2_Standard.10r/contents.html",
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
@@ -411951,169 +411929,169 @@
                     "title": "View this dataset's algorithm theoretical basis document"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/OCO/SDOS_SIS_L2Standard.V7.pdf",
-                    "description": "Software Interface Specification",
                     "@type": "dcat:Distribution",
+                    "description": "Software Interface Specification",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/OCO/SDOS_SIS_L2Standard.V7.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View the primary investigator's documentation for this dataset"
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
+            "identifier": "C2910086890-GES_DISC",
+            "issued": "2021-05-31",
+            "keyword": [
+                "earth science",
+                "atmosphere",
+                "atmospheric chemistry"
+            ],
+            "landingPage": "https://doi.org/10.5067/L4Y1YYH4CI4R",
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
+            "series-name": "OCO3_L2_Standard",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2019-08-06T00:00:00Z/2024-10-07T00:00:00Z",
             "theme": [
                 "OCO-3",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "OCO-3 Level 2 geolocated XCO2 retrievals results, physical model, Retrospective Processing V11r (OCO3_L2_Standard) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-CAL%2FE-ALICE-3-EAR3-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This data set contains CODMAC level 3 data acquired by the Rosetta Orbiter ALICE UV Spectrometer during the third earth flyby mission phase, which took place between 2009-09-14 and 2009-12-13.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-cal-e-alice-3-ear3-v1.0_9axn-ppmz",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "calibration",
                 "moon",
                 "international rosetta mission",
                 "earth"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-CAL%2FE-ALICE-3-EAR3-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-cal-e-alice-3-ear3-v1.0_9axn-ppmz",
-            "description": "This data set contains CODMAC level 3 data acquired by the Rosetta Orbiter ALICE UV Spectrometer during the third earth flyby mission phase, which took place between 2009-09-14 and 2009-12-13.",
-            "title": "ROSETTA-ORBITER CAL/EARTH ALICE 3 EAR3 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER CAL/EARTH ALICE 3 EAR3 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1000000483-LARC_ASDC.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC.",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "undefined",
+                "hasEmail": "mailto:support-asdc@earthdata.nasa.gov"
+            },
+            "description": "INTEX-B King Air Be200 Aircraft data.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "View this dataset on the CMR (Common Metadata Repository)",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/search/concepts/C1000000483-LARC_ASDC.html",
+                    "mediaType": "text/html",
+                    "title": "CMR"
+                }
+            ],
+            "identifier": "C1000000483-LARC_ASDC",
             "issued": "2009-03-03",
-            "temporal": "2006-03-01T00:00:00Z/2006-03-31T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2018-04-25",
             "keyword": [
                 "nasa"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "undefined",
-                "hasEmail": "mailto:support-asdc@earthdata.nasa.gov"
-            },
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1000000483-LARC_ASDC.html",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2018-04-25",
+            "programCode": [
+                "026:001"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "NASA/LARC/SD/ASDC"
             },
-            "identifier": "C1000000483-LARC_ASDC",
-            "description": "INTEX-B King Air Be200 Aircraft data.",
-            "title": "INTEXB_Be200_AIRCRAFT",
-            "programCode": [
-                "026:001"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/search/concepts/C1000000483-LARC_ASDC.html",
-                    "description": "View this dataset on the CMR (Common Metadata Repository)",
-                    "@type": "dcat:Distribution",
-                    "title": "CMR"
-                }
-            ],
+            "temporal": "2006-03-01T00:00:00Z/2006-03-31T23:59:59Z",
             "theme": [
                 "INTEXB",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "INTEXB_Be200_AIRCRAFT"
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
-                "radio science",
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
-            "identifier": "NASA-499",
             "description": "GRS, RADIO SCIENCE (Releases 121-123), SPICE, THEMIS",
-            "title": "PDS Odyssey Data Release 41",
-            "programCode": [
-                "026:005"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -412121,94 +412099,90 @@
                     "mediaType": "application/html"
                 }
             ],
-            "accrualPeriodicity": "irregular",
+            "identifier": "NASA-499",
+            "issued": "2018-06-25",
+            "keyword": [
+                "grs",
+                "spice",
+                "themis",
+                "radio science",
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
+            "title": "PDS Odyssey Data Release 41"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC2-0731-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 2 phase 2015-03-11 to 2015-06-30. It is a Global Gravity measurement at the comet 67P and covers the time 2015-04-26T05:43:05.000 to 2015-04-26T07:40:44.500.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc2-0731-v1.0_9b43-7jx9",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC2-0731-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc2-0731-v1.0_9b43-7jx9",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 2 phase 2015-03-11 to 2015-06-30. It is a Global Gravity measurement at the comet 67P and covers the time 2015-04-26T05:43:05.000 to 2015-04-26T07:40:44.500.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 2 0731 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 2 0731 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/J07I81P6G1XS",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "AIRS project. 2007-06-30. AIRXBCAL. Version 005. AIRS/Aqua L1B Calibration subset V005. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/J07I81P6G1XS. https://disc.gsfc.nasa.gov/datacollection/AIRXBCAL_005.html. Digital Science Data.",
-            "issued": "2002-08-31",
-            "temporal": "2002-08-31T00:00:00Z/2024-12-23T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-12-20",
-            "keyword": [
-                "oceans",
-                "spectral/engineering",
-                "ocean heat budget",
-                "infrared wavelengths",
-                "earth science",
-                "atmospheric radiation",
-                "atmosphere"
-            ],
-            "data-presentation-form": "Digital Science Data",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "ED ESFANDIARI",
                 "hasEmail": "mailto:asghar.e.esfandiari@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
-            "identifier": "C1243477315-GES_DISC",
-            "description": "The Atmospheric Infrared Sounder (AIRS) is a grating spectrometer (R = 1200) aboard the second Earth Observing System (EOS) polar-orbiting platform, EOS Aqua. In combination with the Advanced Microwave Sounding Unit (AMSU) and the Humidity Sounder for Brazil (HSB), AIRS constitutes an innovative atmospheric sounding group of visible, infrared, and microwave sensors. AIRS/Aqua Level-1B calibration subset including clear cases, special calibration sites, random nadir spots, and high clouds. The AIRS Visible/Near Infrared (VIS/NIR) level 1B data set contains AIRS visible and near-infrared calibrated and geolocated radiances in W/m^2/micron/steradian. This data set is generated from AIRS level 1A digital numbers (DN), including 4 channels in the 0.4 to 1.0 um region of the spectrum.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "AIRXBCAL",
             "creator": "AIRS project",
-            "title": "AIRS/Aqua L1B Calibration subset V005 (AIRXBCAL) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/AIRXBCAL_005.gif",
-            "programCode": [
-                "026:001"
-            ],
+            "data-presentation-form": "Digital Science Data",
+            "description": "The Atmospheric Infrared Sounder (AIRS) is a grating spectrometer (R = 1200) aboard the second Earth Observing System (EOS) polar-orbiting platform, EOS Aqua. In combination with the Advanced Microwave Sounding Unit (AMSU) and the Humidity Sounder for Brazil (HSB), AIRS constitutes an innovative atmospheric sounding group of visible, infrared, and microwave sensors. AIRS/Aqua Level-1B calibration subset including clear cases, special calibration sites, random nadir spots, and high clouds. The AIRS Visible/Near Infrared (VIS/NIR) level 1B data set contains AIRS visible and near-infrared calibrated and geolocated radiances in W/m^2/micron/steradian. This data set is generated from AIRS level 1A digital numbers (DN), including 4 channels in the 0.4 to 1.0 um region of the spectrum.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FJ07I81P6G1XS",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FJ07I81P6G1XS",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
@@ -412218,112 +412192,122 @@
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/AIRXBCAL_005.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/AIRXBCAL_005.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://airsl2.gesdisc.eosdis.nasa.gov/data/Aqua_AIRS_Level2/AIRXBCAL.005/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://airsl2.gesdisc.eosdis.nasa.gov/data/Aqua_AIRS_Level2/AIRXBCAL.005/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://airsl2.gesdisc.eosdis.nasa.gov/opendap/Aqua_AIRS_Level2/AIRXBCAL.005/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://airsl2.gesdisc.eosdis.nasa.gov/opendap/Aqua_AIRS_Level2/AIRXBCAL.005/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=AIRXBCAL+005",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=AIRXBCAL+005",
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
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/AIRXBCAL_005.html",
-                    "description": "AIRS AIRXBCAL documentation page at the GES DISC.",
                     "@type": "dcat:Distribution",
+                    "description": "AIRS AIRXBCAL documentation page at the GES DISC.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/AIRXBCAL_005.html",
+                    "mediaType": "text/html",
                     "title": "View information related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/repository/Mission/AIRS/3.3_ScienceDataProductDocumentation/3.3.4_ProductGenerationAlgorithms/README.AIRXBCAL.pdf",
-                    "description": "README Document",
                     "@type": "dcat:Distribution",
+                    "description": "README Document",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/repository/Mission/AIRS/3.3_ScienceDataProductDocumentation/3.3.4_ProductGenerationAlgorithms/README.AIRXBCAL.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's read me document"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/repository/Mission/AIRS/3.7_ScienceDataProductValidation/V5_CalVal_Status_Summary.pdf",
-                    "description": "Summary of validation status of products",
                     "@type": "dcat:Distribution",
+                    "description": "Summary of validation status of products",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/repository/Mission/AIRS/3.7_ScienceDataProductValidation/V5_CalVal_Status_Summary.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://eospso.gsfc.nasa.gov/sites/default/files/atbd/AIRS_L1B_ATBD_Part_1.pdf",
-                    "description": "ATBD documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ATBD documentation",
+                    "downloadURL": "https://eospso.gsfc.nasa.gov/sites/default/files/atbd/AIRS_L1B_ATBD_Part_1.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's algorithm theoretical basis document"
                 }
             ],
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/AIRXBCAL_005.gif",
+            "identifier": "C1243477315-GES_DISC",
+            "issued": "2002-08-31",
+            "keyword": [
+                "oceans",
+                "spectral/engineering",
+                "ocean heat budget",
+                "infrared wavelengths",
+                "earth science",
+                "atmospheric radiation",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.5067/J07I81P6G1XS",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2024-12-20",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
+            },
+            "release-place": "Greenbelt, MD, USA",
+            "series-name": "AIRXBCAL",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2002-08-31T00:00:00Z/2024-12-23T00:00:00Z",
             "theme": [
                 "Aqua",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "AIRS/Aqua L1B Calibration subset V005 (AIRXBCAL) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "restricted public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://psi.nasa.gov/",
-            "issued": "2020-03-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-31",
-            "keyword": [
-                "nasa"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Teresa Y Miller",
                 "hasEmail": "mailto:teresa.y.miller@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "PSI"
-            },
-            "identifier": "https://data.nasa.gov/api/views/9b7s-v6d2",
             "description": "NASA\u2019s Physical Sciences Research Program, along with its predecessors, has conducted significant fundamental and applied research in the physical sciences.  The International Space Station (ISS) is an orbiting laboratory that provides an ideal facility to conduct long-duration experiments in reduced gravity and allows continuous and interactive research similar to Earth-based laboratories.  This enables scientists to pursue innovations and discoveries not currently achievable by other means.  NASA\u2019s Physical Sciences Research Program also benefits from collaborations with several of the ISS International Partners\u2014Europe, Russia, Japan, and Canada\u2014foreign governments with space programs, such as France, Germany, and Italy.",
-            "title": "Physical Sciences Informatics (PSI) System data repository- International Space Station (ISS)",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -412331,215 +412315,207 @@
                     "mediaType": "text/html",
                     "title": "Homepage"
                 }
-            ]
+            ],
+            "identifier": "https://data.nasa.gov/api/views/9b7s-v6d2",
+            "issued": "2020-03-26",
+            "keyword": [
+                "nasa"
+            ],
+            "landingPage": "https://psi.nasa.gov/",
+            "modified": "2023-01-31",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "PSI"
+            },
+            "title": "Physical Sciences Informatics (PSI) System data repository- International Space Station (ISS)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ISS/CATS/L2O_D-M7.1-V3-01_05kmPro",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2018-10-31. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/ISS/CATS/L2O_D-M7.1-V3-01_05kmPro. https://asdc.larc.nasa.gov/project/CATS-ISS.",
-            "issued": "2018-08-13",
-            "temporal": "2015-02-10T00:00:00Z/2015-03-21T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2018-08-13",
-            "keyword": [
-                "atmosphere",
-                "earth science",
-                "clouds",
-                "aerosols"
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
-            "identifier": "C1621697868-LARC_ASDC",
             "description": "CATS-ISS_L2O_D-M7.1-V3-01_05kmPro is the Cloud-Aerosol Transport System (CATS) International Space Station (ISS) Level 2 Operational Day Mode 7.1 Version 3-01 5 km Profile data product. This collection spans from February 10, 2015 to March 21, 2015. CATS, which was launched on January 10, 2015, was a lidar remote sensing instrument that provided range-resolved profile measurements of atmospheric aerosols and clouds from the ISS. CATS was intended to operate on-orbit for up to three years. CATS provides vertical profiles at three wavelengths, orbiting between ~230 and ~270 miles above the Earth's surface at a 51-degree inclination with nearly a three-day repeat cycle. For the first time, scientists were able to study diurnal (day-to-night) changes in cloud and aerosol effects from space by observing the same spot on Earth at different times each day. CATS Level 2 Layer data products contain geophysical parameters and are derived from Level 1 data, at 60m vertical and 5km horizontal resolution.",
-            "graphic-preview-description": "CATS Browse and Granule Availability",
-            "title": "CATS-ISS Level 2 Operational Day Mode 7.1 Version 3-01 5 km Profile",
-            "graphic-preview-file": "https://cats.gsfc.nasa.gov/data/browse/",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FISS%2FCATS%2FL2O_D-M7.1-V3-01_05kmPro",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FISS%2FCATS%2FL2O_D-M7.1-V3-01_05kmPro",
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
-                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/CATS/L2O_D-M7.1-V3-01_05kmPro/contents.html",
-                    "description": "OPeNDAP data access for CATS-ISS_L2O_D-M7.1-V3-01_05kmPro_V3-01",
                     "@type": "dcat:Distribution",
+                    "description": "OPeNDAP data access for CATS-ISS_L2O_D-M7.1-V3-01_05kmPro_V3-01",
+                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/CATS/L2O_D-M7.1-V3-01_05kmPro/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1621697868-LARC_ASDC",
-                    "description": "Earthdata Search for CATS-ISS_L2O_D-M7.1-V3-01_05kmPro_V3-01 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for CATS-ISS_L2O_D-M7.1-V3-01_05kmPro_V3-01 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1621697868-LARC_ASDC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/CATS/L2O_D-M7.1-V3-01_05kmPro/",
-                    "description": "ASDC Direct Data Download for CATS-ISS_L2O_D-M7.1-V3-01_05kmPro_V3-01",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for CATS-ISS_L2O_D-M7.1-V3-01_05kmPro_V3-01",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/CATS/L2O_D-M7.1-V3-01_05kmPro/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/ISS/CATS/L2O_D-M7.1-V3-01_05kmPro",
-                    "description": "DOI data set landing page for CATS-ISS_L2O_D-M7.1-V3-01_05kmPro_V3-01",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for CATS-ISS_L2O_D-M7.1-V3-01_05kmPro_V3-01",
+                    "downloadURL": "https://doi.org/10.5067/ISS/CATS/L2O_D-M7.1-V3-01_05kmPro",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
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
+            "identifier": "C1621697868-LARC_ASDC",
+            "issued": "2018-08-13",
+            "keyword": [
+                "atmosphere",
+                "earth science",
+                "clouds",
+                "aerosols"
+            ],
+            "landingPage": "https://doi.org/10.5067/ISS/CATS/L2O_D-M7.1-V3-01_05kmPro",
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
+            "temporal": "2015-02-10T00:00:00Z/2015-03-21T23:59:59Z",
             "theme": [
                 "CATS-ISS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "CATS-ISS Level 2 Operational Day Mode 7.1 Version 3-01 5 km Profile"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/HO07ZJEQBMHE",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Kevin Bowman. 2020-09-28. CMSFluxFire. Version 2. Carbon Monitoring System Carbon Flux for Fire L4 V2. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/HO07ZJEQBMHE. https://disc.gsfc.nasa.gov/datacollection/CMSFluxFire_2.html.",
-            "issued": "2017-04-26",
-            "temporal": "2010-01-01T00:00:00Z/2017-01-01T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2017-08-18",
-            "keyword": [
-                "oceans",
-                "atmosphere",
-                "earth science",
-                "ocean chemistry",
-                "atmospheric chemistry"
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
-            "identifier": "C1945851681-GES_DISC",
-            "description": "This dataset provides the Carbon Flux for Fires.\n\nThe NASA Carbon Monitoring System (CMS) is designed to make significant contributions in characterizing, quantifying, understanding, and predicting the evolution of global carbon sources and sinks through improved monitoring of carbon stocks and fluxes. The System will use the full range of NASA satellite observations and modeling/analysis capabilities to establish the accuracy, quantitative uncertainties, and utility of products for supporting national and international policy, regulatory, and management activities. CMS will maintain a global emphasis while providing finer scale regional information, utilizing space-based and surface-based data and will rapidly initiate generation and distribution of products both for user evaluation and to inform near-term policy development and planning.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "CMSFluxFire",
             "creator": "Kevin Bowman",
-            "title": "Carbon Monitoring System Carbon Flux for Fire L4 V2 (CMSFluxFire) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/CMS/CMSFluxFire_2.png",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "This dataset provides the Carbon Flux for Fires.\n\nThe NASA Carbon Monitoring System (CMS) is designed to make significant contributions in characterizing, quantifying, understanding, and predicting the evolution of global carbon sources and sinks through improved monitoring of carbon stocks and fluxes. The System will use the full range of NASA satellite observations and modeling/analysis capabilities to establish the accuracy, quantitative uncertainties, and utility of products for supporting national and international policy, regulatory, and management activities. CMS will maintain a global emphasis while providing finer scale regional information, utilizing space-based and surface-based data and will rapidly initiate generation and distribution of products both for user evaluation and to inform near-term policy development and planning.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FHO07ZJEQBMHE",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FHO07ZJEQBMHE",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
@@ -412549,178 +412525,174 @@
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/CMSFluxFire_2.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/CMSFluxFire_2.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://acdisc.gsfc.nasa.gov/data/CMS/CMSFluxFire.2/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://acdisc.gsfc.nasa.gov/data/CMS/CMSFluxFire.2/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://acdisc.gsfc.nasa.gov/opendap/CMS/CMSFluxFire.2/",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://acdisc.gsfc.nasa.gov/opendap/CMS/CMSFluxFire.2/",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://acdisc.gsfc.nasa.gov/data/CMS/CMSFluxFire.2/doc/README.CMS_Flux_V2.pdf",
-                    "description": "README Document",
                     "@type": "dcat:Distribution",
+                    "description": "README Document",
+                    "downloadURL": "https://acdisc.gsfc.nasa.gov/data/CMS/CMSFluxFire.2/doc/README.CMS_Flux_V2.pdf",
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
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/CMS/CMSFluxFire_2.png",
+            "identifier": "C1945851681-GES_DISC",
+            "issued": "2017-04-26",
+            "keyword": [
+                "oceans",
+                "atmosphere",
+                "earth science",
+                "ocean chemistry",
+                "atmospheric chemistry"
+            ],
+            "landingPage": "https://doi.org/10.5067/HO07ZJEQBMHE",
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
+            "temporal": "2010-01-01T00:00:00Z/2017-01-01T23:59:59.999Z",
             "theme": [
                 "CMS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Carbon Monitoring System Carbon Flux for Fire L4 V2 (CMSFluxFire) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-E-MIRO-3-EAR1-EARTH1-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This data set contains Spectroscopic and Continuum data, in the form of table files, taken during the first Earth swing-by phase of the Rosetta mission by the MIRO instrument. These data have been calibrated to antenna temperatures.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-e-miro-3-ear1-earth1-v1.0_9b9c-2u2h",
             "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "earth",
                 "international rosetta mission",
                 "moon"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-E-MIRO-3-EAR1-EARTH1-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-e-miro-3-ear1-earth1-v1.0_9b9c-2u2h",
-            "description": "This data set contains Spectroscopic and Continuum data, in the form of table files, taken during the first Earth swing-by phase of the Rosetta mission by the MIRO instrument. These data have been calibrated to antenna temperatures.",
-            "title": "ROSETTA-ORBITER EARTH MIRO 3 EAR1 EARTH1 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "ROSETTA-ORBITER EARTH MIRO 3 EAR1 EARTH1 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewBundle.jsp?identifier=urn%3Anasa%3Apds%3Acarbonate_refractive_indices&version=1.0",
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
-                "investigation of complex refractive indices of carbonates"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "Visible to Mid-Infrared (VMIR, ~0.3-6 micrometer) Complex Refractive Indices of Carbonates.",
+            "identifier": "urn:nasa:pds:carbonate_refractive_indices",
+            "issued": "2021-05-21",
+            "keyword": [
+                "investigation of complex refractive indices of carbonates"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewBundle.jsp?identifier=urn%3Anasa%3Apds%3Acarbonate_refractive_indices&version=1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:carbonate_refractive_indices",
-            "description": "Visible to Mid-Infrared (VMIR, ~0.3-6 micrometer) Complex Refractive Indices of Carbonates.",
-            "title": "Visible to Mid-Infrared (VMIR, ~0.3-6 micrometer) Complex Refractive Indices of Carbonates Bundle",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "Visible to Mid-Infrared (VMIR, ~0.3-6 micrometer) Complex Refractive Indices of Carbonates Bundle"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/AURA/OMI/DATA2032",
             "citation": "Joanna J. Joiner, Wenhan Qin, Zachary Fasnacht, Alexander Vasilkov, David P. Haffner, Bradford Fisher, Nickolay Krotkov, Lok N. Lamsal and Robert Spurr. 2019-12-20. OMGLER. Version 003. OMI/Aura Global Geometry-Dependent Surface LER 1-Orbit L2 Swath 13x24km V3. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/AURA/OMI/DATA2032. https://disc.gsfc.nasa.gov/datacollection/OMGLER_003.html. Digital Science Data.",
-            "issued": "2019-05-10",
-            "temporal": "2004-10-01T00:00:00Z/2022-01-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2019-05-10",
-            "references": [
-                "https://doi.org/10.1029/2007JD008665",
-                "https://doi.org/10.5194/amt-12-6749-2019",
-                "https://doi.org/10.5194/amt-12-3997-2019",
-                "https://doi.org/10.5194/amt-10-333-2017"
-            ],
-            "keyword": [
-                "earth science",
-                "atmospheric radiation",
-                "atmosphere"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "JOANNA JOINER, PH. D",
                 "hasEmail": "mailto:Joanna.Joiner@nasa.gov"
             },
+            "creator": "Joanna J. Joiner, Wenhan Qin, Zachary Fasnacht, Alexander Vasilkov, David P. Haffner, Bradford Fisher, Nickolay Krotkov, Lok N. Lamsal and Robert Spurr",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C1611899353-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "The OMI/Aura Global Geometry-Dependent Surface LER 1-Orbit L2 Swath 13x24km product, or OMGLER, provides GLER, and the computed top-of-atmosphere (TOA) radiance from which GLER is derived, for the OMI field of view. The OMGLER data also contain a number of ancillary/input parameters for each OMI pixel used to compute TOA radiance. The primary intended use of the product is to provide surface reflectance information for OMI cloud, aerosol and trace gas algorithms. GLER is designed to easily replace commonly used LER climatologies within existing OMI algorithms. The product lead is Joanna J. Joiner (OMI US science team leader). The algorithm developer is Wenhan Qin.\n\nThe OMGLER product file is produced in the version 5 Hierarchical Data Format (HDF-EOS5). Each file contains GLER data for the daylit portion of an orbit (~53 minutes). There are approximately 14 orbits per day. Files are roughly 9 MB in size.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "OMGLER",
-            "creator": "Joanna J. Joiner, Wenhan Qin, Zachary Fasnacht, Alexander Vasilkov, David P. Haffner, Bradford Fisher, Nickolay Krotkov, Lok N. Lamsal and Robert Spurr",
-            "title": "OMI/Aura Global Geometry-Dependent Surface LER 1-Orbit L2 Swath 13x24km V3 (OMGLER) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/OMGLER_003.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAURA%2FOMI%2FDATA2032",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAURA%2FOMI%2FDATA2032",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
@@ -412730,73 +412702,73 @@
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/OMGLER_003.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/OMGLER_003.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://aura.gesdisc.eosdis.nasa.gov/data/Aura_OMI_Level2/OMGLER.003/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://aura.gesdisc.eosdis.nasa.gov/data/Aura_OMI_Level2/OMGLER.003/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=OMGLER_003",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=OMGLER_003",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://aura.gesdisc.eosdis.nasa.gov/opendap/Aura_OMI_Level2/OMGLER.003/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://aura.gesdisc.eosdis.nasa.gov/opendap/Aura_OMI_Level2/OMGLER.003/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://aura.gesdisc.eosdis.nasa.gov/data/Aura_OMI_Level2/OMGLER.003/doc/OMGLER_README.pdf",
-                    "description": "README Document",
                     "@type": "dcat:Distribution",
+                    "description": "README Document",
+                    "downloadURL": "https://aura.gesdisc.eosdis.nasa.gov/data/Aura_OMI_Level2/OMGLER.003/doc/OMGLER_README.pdf",
+                    "mediaType": "application/pdf",
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
-                    "mediaType": "text/html",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/OMI/OMGLER.fs",
-                    "description": "File Specification Document",
                     "@type": "dcat:Distribution",
+                    "description": "File Specification Document",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/OMI/OMGLER.fs",
+                    "mediaType": "text/html",
                     "title": "View the primary investigator's documentation for this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/repository/Mission/OMI/3.3_ScienceDataProductDocumentation/3.3.4_ProductGenerationAlgorithm/ATBD-OMI-04.pdf",
-                    "description": "OMI Algorithm Theoretical Basis Documents",
                     "@type": "dcat:Distribution",
+                    "description": "OMI Algorithm Theoretical Basis Documents",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/repository/Mission/OMI/3.3_ScienceDataProductDocumentation/3.3.4_ProductGenerationAlgorithm/ATBD-OMI-04.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's algorithm theoretical basis document"
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
@@ -412806,985 +412778,993 @@
                     "title": "View this dataset's publications"
                 }
             ],
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/OMGLER_003.png",
+            "identifier": "C1611899353-GES_DISC",
+            "issued": "2019-05-10",
+            "keyword": [
+                "earth science",
+                "atmospheric radiation",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.5067/AURA/OMI/DATA2032",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2019-05-10",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
+            },
+            "references": [
+                "https://doi.org/10.1029/2007JD008665",
+                "https://doi.org/10.5194/amt-12-6749-2019",
+                "https://doi.org/10.5194/amt-12-3997-2019",
+                "https://doi.org/10.5194/amt-10-333-2017"
+            ],
+            "release-place": "Greenbelt, MD, USA",
+            "series-name": "OMGLER",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2004-10-01T00:00:00Z/2022-01-17T00:00:00Z",
             "theme": [
                 "Aura",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "OMI/Aura Global Geometry-Dependent Surface LER 1-Orbit L2 Swath 13x24km V3 (OMGLER) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/346",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Middleton, E.M., and J. Sullivan. 1998. BOREAS TE-10 Leaf Gas Exchange Data. ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/346",
-            "issued": "2023-11-22",
-            "temporal": "1994-05-25T00:00:00Z/1994-09-15T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-11-28",
-            "keyword": [
-                "vegetation",
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
-            "identifier": "C2808129626-ORNL_CLOUD",
             "description": "Contains gas exchange data collected by TE-10 during the BOREAS project.",
-            "graphic-preview-description": "Browse Image",
-            "title": "BOREAS TE-10 Leaf Gas Exchange Data",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/boreas_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F346",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F346",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/boreas/TE/te10lgxd/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/boreas/TE/te10lgxd/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/BOREAS/guides/TE10_Leaf_Gas_Exchange.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/BOREAS/guides/TE10_Leaf_Gas_Exchange.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/346",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/346",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TE/te10lgxd/comp/te10lgxd.def",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TE/te10lgxd/comp/te10lgxd.def",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/msword",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TE/te10lgxd/comp/TE10_Leaf_Gas_Exchange.doc",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TE/te10lgxd/comp/TE10_Leaf_Gas_Exchange.doc",
+                    "mediaType": "application/msword",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TE/te10lgxd/comp/TE10_Leaf_Gas_Exchange.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TE/te10lgxd/comp/TE10_Leaf_Gas_Exchange.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TE/te10lgxd/comp/TE10_Leaf_Gas_Exchange.txt",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TE/te10lgxd/comp/TE10_Leaf_Gas_Exchange.txt",
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
+            "identifier": "C2808129626-ORNL_CLOUD",
+            "issued": "2023-11-22",
+            "keyword": [
+                "vegetation",
+                "biosphere",
+                "earth science",
+                "ecological dynamics"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/346",
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
+            "temporal": "1994-05-25T00:00:00Z/1994-09-15T23:59:59Z",
             "theme": [
                 "BOREAS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "BOREAS TE-10 Leaf Gas Exchange Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/AURA/TES/TL2N2ON.008",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/AURA/TES/TL2N2ON.008. https://asdc.larc.nasa.gov/project/TES.",
-            "issued": "2017-01-10",
-            "temporal": "2004-08-22T00:00:00Z/2018-01-22T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2018-09-08",
-            "keyword": [
-                "earth science",
-                "atmosphere",
-                "atmospheric chemistry",
-                "atmospheric temperature",
-                "air quality",
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
-            "identifier": "C1616452212-LARC",
             "description": "TL2N2ON_8 is the Tropospheric Emission Spectrometer (TES)/Aura Level 2 Nitrous Oxide Nadir Version 8 data product. It consists of information for one molecular species, Nitrous Oxide, for an entire Global Survey or Special Observation. TES was an instrument aboard NASA's Aura satellite and was launched from California on July 15, 2004. Data collection for TES is complete. TES Level 2 data contain retrieved species (or temperature) profiles at the observation targets and the estimated errors. The geolocation, quality, and other data (e.g., surface characteristics for nadir observations) were also provided. L2 modeled spectra were evaluated using radiative transfer modeling algorithms. The process, referred to as retrieval, compared observed spectra to the modeled spectra and iteratively updated the atmospheric parameters. L2 standard product files included information for one molecular species (or temperature) for an entire global survey or special observation run. A global survey consisted of a maximum of 16 consecutive orbits.\r\rNadir observations, which point directly to the surface of the Earth, are different from limb observations, which are pointed at various off-nadir angles into the atmosphere. Nadir and limb observations were added to separate L2 files, and a single ancillary file was composed of data that are common to both nadir and limb files. A Nadir sequence within the TES Global Survey was a fixed number of observations within an orbit for a Global Survey. Prior to April 24, 2005, it consisted of two low resolution scans over the same ground locations. After April 24, 2005, Global Survey data consisted of three low resolution scans. The Nadir standard product consists of four files, where each file is composed of the Global Survey Nadir observations from one of four focal planes for a single orbit, i.e. 72 orbit sequences. The Global Survey Nadir observations only used a single set of filter mix. \r\rA Global Survey consisted of observations along 16 consecutive orbits at the start of a two day cycle, over which 3,200 retrievals were performed. Each observation was the input for retrievals of species Volume Mixing Ratios (VMRs), temperature profiles, surface temperature, and other data parameters with associated pressure levels, precision, total error, vertical resolution, total column density, and other diagnostic quantities. Each TES Level 2 standard product reported information in a swath format conforming to the HDF-EOS Aura File Format Guidelines. Each Swath object was bounded by the number of observations in a global survey and a predefined set of pressure levels, representing slices through the atmosphere. Each standard product could have had a variable number of observations depending upon the Global Survey configuration and whether averaging was employed. Also, missing or bad retrievals were not reported. Further, observations were occasionally scheduled on non-global survey days. In general they were measurements made for validation purposes or with highly focused science objectives. Those non-global survey measurements were referred to as \u201cspecial observations.\u201d\r\rA Limb sequence within the TES Global Survey was three high-resolution scans over the same limb locations. The Limb standard product consists of four files, where each file is composed of the Global Survey Limb observations from one of four focal planes for a single orbit, i.e. 72 orbit sequences. The Global Survey Limb observations used a repeating sequence of filter wheel positions. Special Observations could only be scheduled during the 9 or 10 orbit gaps in the Global Surveys, and were conducted in any of three basic modes: stare, transect, step-and-stare. The mode used depended on the science requirement. Each limb observation Limb 1, Limb 2 and Limb 3, were processed independently. Thus, each limb standard product consisted of three sets where each set consisted of 1,152 observations. For TES, the swath object represented one of these sets.",
-            "title": "TES/Aura L2 Nitrous Oxide Nadir V008",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAURA%2FTES%2FTL2N2ON.008",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAURA%2FTES%2FTL2N2ON.008",
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
-                    "downloadURL": "https://doi.org/10.5067/AURA/TES/TL2N2ON.008",
-                    "description": "DOI data set landing page for TL2N2ON_8",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for TL2N2ON_8",
+                    "downloadURL": "https://doi.org/10.5067/AURA/TES/TL2N2ON.008",
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
-                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/TES/TL2N2ON.008/contents.html",
-                    "description": "OPeNDAP data access for TL2N2ON_8",
                     "@type": "dcat:Distribution",
+                    "description": "OPeNDAP data access for TL2N2ON_8",
+                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/TES/TL2N2ON.008/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1616452212-LARC",
-                    "description": "Earthdata Search for TL2N2ON_8 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for TL2N2ON_8 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1616452212-LARC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/TES/TL2N2ON.008/",
-                    "description": "ASDC Direct Data Download for TL2N2ON_8",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for TL2N2ON_8",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/TES/TL2N2ON.008/",
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
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/tes/quality_summaries/L2_Products_Data_Quality_V008.pdf",
-                    "description": "Aura-TES L2 Products: Version 8 Data Quality Description",
                     "@type": "dcat:Distribution",
+                    "description": "Aura-TES L2 Products: Version 8 Data Quality Description",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/tes/quality_summaries/L2_Products_Data_Quality_V008.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's data quality document"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/tes/readme/TES_Validation_Report_v8_Final.pdf",
-                    "description": "Earth Observing System (EOS) Tropospheric Emission Spectrometer (TES) Data Validation Report (Version F08_12 data) - Version 8.0",
                     "@type": "dcat:Distribution",
+                    "description": "Earth Observing System (EOS) Tropospheric Emission Spectrometer (TES) Data Validation Report (Version F08_12 data) - Version 8.0",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/tes/readme/TES_Validation_Report_v8_Final.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's science data product validation documentation"
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
+            "identifier": "C1616452212-LARC",
+            "issued": "2017-01-10",
+            "keyword": [
+                "earth science",
+                "atmosphere",
+                "atmospheric chemistry",
+                "atmospheric temperature",
+                "air quality",
+                "clouds"
+            ],
+            "landingPage": "https://doi.org/10.5067/AURA/TES/TL2N2ON.008",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2018-09-08",
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
+            "title": "TES/Aura L2 Nitrous Oxide Nadir V008"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1119",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Biggs, T.W., T. Dunne, T.F. Domingues, and L.A. Martinelli. 2012. LBA-ECO ND-01 Streamwater and Watershed Characteristics, Rondonia, Brazil: 1998-1999. ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/1119",
-            "issued": "2023-10-03",
-            "temporal": "1998-08-02T00:00:00Z/1999-01-28T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-10-11",
-            "keyword": [
-                "land surface",
-                "surface water",
-                "terrestrial hydrosphere",
-                "water quality/water chemistry",
-                "atmospheric chemistry",
-                "solid earth",
-                "geochemistry",
-                "atmosphere",
-                "erosion/sedimentation",
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
-            "identifier": "C2780920003-ORNL_CLOUD",
             "description": "This data set provides the results of (1) synoptic streamwater sampling and analyses from numerous sites across Rondonia and (2) corresponding watershed characteristics derived from remote sensing and historical/available data sources. Sixty streams, in both forested and non-forested sites, were sampled once during the dry season in August of 1998 and 49 of the same streams were sampled again during the wet season in January-February of 1999. Analyses included sodium (Na), calcium (Ca), magnesium (Mg), potassium (K), silica (Si), chloride (Cl), sulfate, pH, and acid neutralizing capacity. Watershed characteristics, including soil cation content, pH, watershed lithology, area, percent deforested, and urban watershed population density, were derived and calculated from digitized soil maps and available soil profile analyses, digitized topographic maps, land use mosaics from Landsat Thematic Mapper (TM) images, and Brazilian census data. The objective of the study was to determine the relative influence of watershed soil exchangeable cation content, rock type, deforestation, and urban population density on stream concentrations of base cations, dissolved silicon, chloride and sulfate in both the dry and wet seasons in a humid tropical region undergoing regional land use transformation. There are three comma-delimited data files with this data set.",
-            "graphic-preview-description": "Browse Image",
-            "title": "LBA-ECO ND-01 Streamwater and Watershed Characteristics, Rondonia, Brazil: 1998-1999",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/lba_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1119",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1119",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/lba/nutrient_dynamics/ND01_Stream_Chemistry/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/lba/nutrient_dynamics/ND01_Stream_Chemistry/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/LBA/guides/ND01_Stream_Chemistry.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/LBA/guides/ND01_Stream_Chemistry.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1119",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1119",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/nutrient_dynamics/ND01_Stream_Chemistry/comp/ND01_Stream_Chemistry.PDF",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/nutrient_dynamics/ND01_Stream_Chemistry/comp/ND01_Stream_Chemistry.PDF",
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
+            "identifier": "C2780920003-ORNL_CLOUD",
+            "issued": "2023-10-03",
+            "keyword": [
+                "land surface",
+                "surface water",
+                "terrestrial hydrosphere",
+                "water quality/water chemistry",
+                "atmospheric chemistry",
+                "solid earth",
+                "geochemistry",
+                "atmosphere",
+                "erosion/sedimentation",
+                "earth science",
+                "soils"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1119",
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
             "spatial": "-64.43 -12.63 -60.7 -8.0",
+            "temporal": "1998-08-02T00:00:00Z/1999-01-28T23:59:59Z",
             "theme": [
                 "LBA-ECO",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "LBA-ECO ND-01 Streamwater and Watershed Characteristics, Rondonia, Brazil: 1998-1999"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MER1-M-PANCAM-3-RADCAL-RDR-V2.0",
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
+            "description": "Mars Exploration Rover 1 Pancam Radiometrically Calibrated Reduced Data Record",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mer1-m-pancam-3-radcal-rdr-v2.0_9bez-ygb6",
+            "issued": "2021-05-21",
+            "keyword": [
+                "mars exploration rover",
+                "mars"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MER1-M-PANCAM-3-RADCAL-RDR-V2.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mer1-m-pancam-3-radcal-rdr-v2.0_9bez-ygb6",
-            "description": "Mars Exploration Rover 1 Pancam Radiometrically Calibrated Reduced Data Record",
-            "title": "MER 1 MARS PANCAM RADIOMETRICALLY\n                                  CALIBRATED RDR V2.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "MER 1 MARS PANCAM RADIOMETRICALLY\n                                  CALIBRATED RDR V2.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C2254304452-OB_DAAC.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/GSFC/SED/ESD/GCDC/OB.DAAC.",
-            "issued": "2022-09-13",
-            "temporal": "2018-04-25T00:00:00Z/2024-11-04T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-04-13",
-            "keyword": [
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
-            "identifier": "C2254304452-OB_DAAC",
             "description": "The Ocean Biology DAAC produces near real-time (quicklook) products using the best-available combination of ancillary data from meteorological and ozone data. As such, the inputs and the calibration used are less than optimal. Quicklook products provide a snapshot of the data during a short time period within a single orbit.",
-            "title": "Sentinel-3B OLCI Level-2 Regional Earth-observation Full Resolution (EFR) Inherent Optical Properties (IOP) - Near Real-time (NRT) Data, version R2022.0",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
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
+            "identifier": "C2254304452-OB_DAAC",
+            "issued": "2022-09-13",
+            "keyword": [
+                "ocean optics",
+                "earth science",
+                "oceans"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C2254304452-OB_DAAC.html",
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
+            "temporal": "2018-04-25T00:00:00Z/2024-11-04T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Sentinel-3B OLCI Level-2 Regional Earth-observation Full Resolution (EFR) Inherent Optical Properties (IOP) - Near Real-time (NRT) Data, version R2022.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.7927/H4SJ1HHX",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Center for International Earth Science Information Network - CIESIN - Columbia University. 2018-12-06. West Africa Coastal Vulnerability Mapping: Deforestation, 2000-2012. Version 1.00. Palisades, NY. Archived by National Aeronautics and Space Administration, U.S. Government, Socioeconomic Data and Applications Center (SEDAC). https://doi.org/10.7927/H4SJ1HHX. https://doi.org/10.7927/H4SJ1HHX.",
-            "issued": "2018-12-06",
-            "temporal": "2000-01-01T00:00:00Z/2012-12-31T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2018-12-06",
-            "references": [
-                "https://doi.org/10.1126/science.1244693",
-                "https://doi.org/10.7927/H4F769H4",
-                "https://doi.org/10.7927/H45T3HFZ",
-                "https://doi.org/10.7927/H4222RQJ",
-                "https://doi.org/10.7927/H4X9287N",
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
-                "http://doi.org/10.3390/ijgi4042561"
-            ],
-            "keyword": [
-                "habitat conversion/fragmentation",
-                "human dimensions",
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
-            "identifier": "C1577516995-SEDAC",
-            "description": "The West Africa Coastal Vulnerability Mapping: Deforestation, 2000-2012, layer was created from the Global Forest Change data set which represents global tree cover extent, loss, and gain mapped for the period from 2000 to 2012 at a spatial resolution of 30m, with loss allocated annually. The Global Forest Change data set defines trees as all vegetation taller than 5m in height. Forest loss (deforestation) is defined as a stand-replacement disturbance, or a change from a forest to non-forest state. The data on forest loss were aggregated to a one kilometer resolution and subsetted to 200 kilometers from the coast to produce this data set. Raster values represent the percentage of the grid cell area that experienced forest cover loss from 2000 to 2012.",
-            "release-place": "Palisades, NY",
-            "graphic-preview-description": "Sample browse graphic of the data set.",
             "creator": "Center for International Earth Science Information Network - CIESIN - Columbia University",
-            "title": "West Africa Coastal Vulnerability Mapping: Deforestation, 2000-2012",
-            "graphic-preview-file": "https://sedac.ciesin.columbia.edu/downloads/maps/wacvm/wacvm-deforestation-2000-2012/sedac-logo.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The West Africa Coastal Vulnerability Mapping: Deforestation, 2000-2012, layer was created from the Global Forest Change data set which represents global tree cover extent, loss, and gain mapped for the period from 2000 to 2012 at a spatial resolution of 30m, with loss allocated annually. The Global Forest Change data set defines trees as all vegetation taller than 5m in height. Forest loss (deforestation) is defined as a stand-replacement disturbance, or a change from a forest to non-forest state. The data on forest loss were aggregated to a one kilometer resolution and subsetted to 200 kilometers from the coast to produce this data set. Raster values represent the percentage of the grid cell area that experienced forest cover loss from 2000 to 2012.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.7927%2FH4SJ1HHX",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.7927%2FH4SJ1HHX",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/downloads/maps/wacvm/wacvm-deforestation-2000-2012/sedac-logo.jpg",
-                    "description": "Sample browse graphic of the data set.",
                     "@type": "dcat:Distribution",
+                    "description": "Sample browse graphic of the data set.",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/downloads/maps/wacvm/wacvm-deforestation-2000-2012/sedac-logo.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/wacvm-deforestation-2000-2012/data-download",
-                    "description": "Data Download Page",
                     "@type": "dcat:Distribution",
+                    "description": "Data Download Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/wacvm-deforestation-2000-2012/data-download",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://sedac.ciesin.columbia.edu/data/set/wacvm-deforestation-2000-2012/docs",
-                    "description": "Documentation Page",
                     "@type": "dcat:Distribution",
+                    "description": "Documentation Page",
+                    "downloadURL": "http://sedac.ciesin.columbia.edu/data/set/wacvm-deforestation-2000-2012/docs",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/wacvm-deforestation-2000-2012",
-                    "description": "Data Set\u00a0Overview Page",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set\u00a0Overview Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/wacvm-deforestation-2000-2012",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "graphic-preview-description": "Sample browse graphic of the data set.",
+            "graphic-preview-file": "https://sedac.ciesin.columbia.edu/downloads/maps/wacvm/wacvm-deforestation-2000-2012/sedac-logo.jpg",
+            "identifier": "C1577516995-SEDAC",
+            "issued": "2018-12-06",
+            "keyword": [
+                "habitat conversion/fragmentation",
+                "human dimensions",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.7927/H4SJ1HHX",
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
+                "https://doi.org/10.1126/science.1244693",
+                "https://doi.org/10.7927/H4F769H4",
+                "https://doi.org/10.7927/H45T3HFZ",
+                "https://doi.org/10.7927/H4222RQJ",
+                "https://doi.org/10.7927/H4X9287N",
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
+                "http://doi.org/10.3390/ijgi4042561"
+            ],
+            "release-place": "Palisades, NY",
             "spatial": "-16.71 1.65 13.566667 13.9",
+            "temporal": "2000-01-01T00:00:00Z/2012-12-31T00:00:00Z",
             "theme": [
                 "WACVM",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "West Africa Coastal Vulnerability Mapping: Deforestation, 2000-2012"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/AURA/TES/TL2FORLN_L2.006",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "The data used in this study were produced by the TES Science Team at the TES SIPS and archived at the Langley DAAC. See ProductionDateTime for Published date.",
-            "issued": "2014-08-20",
-            "temporal": "2004-07-15T00:00:00Z/2022-01-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2015-10-28",
-            "keyword": [
-                "atmospheric chemistry/carbon and hydrocarbon compounds",
-                "earth science",
-                "air quality",
-                "atmosphere"
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
-            "identifier": "C1000000362-LARC",
             "description": "Atmospheric vertical profile estimates and associated errors including the mapping matrix to relate the reduced-size retrieval vectors, covariances, and averaging kernels back to the TES forward model pressure grid.",
-            "title": "TES/Aura L2 Formic Acid Lite Nadir V006",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAURA%2FTES%2FTL2FORLN_L2.006",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAURA%2FTES%2FTL2FORLN_L2.006",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 }
             ],
+            "identifier": "C1000000362-LARC",
+            "issued": "2014-08-20",
+            "keyword": [
+                "atmospheric chemistry/carbon and hydrocarbon compounds",
+                "earth science",
+                "air quality",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.5067/AURA/TES/TL2FORLN_L2.006",
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
+            "title": "TES/Aura L2 Formic Acid Lite Nadir V006"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1790",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Engram, M.J., K.W. Anthony, and F.J. Meyer. 2020. ABoVE: SAR-based Methane Ebullition Flux from Lakes, Five Regions, Alaska, 2007-2010. ORNL DAAC, Oak Ridge, Tennessee, USA. https://doi.org/10.3334/ORNLDAAC/1790",
-            "issued": "2020-07-15",
-            "temporal": "2007-11-13T00:00:00Z/2010-11-11T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-06-12",
-            "keyword": [
-                "snow/ice",
-                "earth science",
-                "terrestrial hydrosphere",
-                "surface water",
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
-            "identifier": "C2143401901-ORNL_CLOUD",
             "description": "This dataset provides Synthetic Aperture Radar (SAR) estimates of lake-source methane ebullition flux in mg CH4/m2/d for thousands of lakes in five regions across Alaska. The study regions include the Atqasuk, Barrow Peninsula, Fairbanks, northern Seward Peninsula, and Toolik. L-band SAR backscatter values for early winter lake ice scenes were collected from 2007 to 2010 over 5,143 lakes using the Phased Array type L-band Synthetic Aperture Radar (PALSAR) instrument on the Advanced Land Observing Satellite (ALOS-1) satellite. The backscatter data were combined with field measurements of methane ebullition from 48 study lakes across the five regions to obtain a volumetric flux estimate for each lake. Mean methane gas-fractions from each region were applied to the SAR-based volumetric fluxes to obtain an estimate of methane ebullition mass flux per lake. The data files contain lake perimeters and the lake-specific attributes of lake area, SAR backscatter values and standard errors, volumetric flux with standard errors, mean percent of methane from gas samples, and methane ebullition mass flux.",
-            "graphic-preview-description": "SAR-based lake ebullition maps. Panel A shows Alaska study regions with SAR footprints outlined in yellow. Subsequent panels show SAR-based CH4 ebullition maps for B) Barrow Peninsula, C) Atqasuk, D) Toolik, E) northern Seward Peninsula, and F) Fairbanks. Study lakes with field-based measurements are outlined (B,C) or boxed (D,E,F) in white. Orange boxes in panel F indicate anthropogenic study lakes. Source: Engram et al. (2020).",
-            "title": "ABoVE: SAR-based Methane Ebullition Flux from Lakes, Five Regions, Alaska, 2007-2010",
-            "graphic-preview-file": "https://daac.ornl.gov/ABOVE/guides/SAR_Methane_Ebullition_AK_Fig1.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1790",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1790",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/above/SAR_Methane_Ebullition_AK/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/above/SAR_Methane_Ebullition_AK/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/ABOVE/guides/SAR_Methane_Ebullition_AK.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/ABOVE/guides/SAR_Methane_Ebullition_AK.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1790",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1790",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/vnd.google-earth.kml+xml",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/SAR_Methane_Ebullition_AK/comp/atqasuk.kml",
-                    "description": "ABoVE: SAR-based Methane Ebullition Flux from Lakes, Five Regions, Alaska, 2007-2010: atqasuk.kml",
                     "@type": "dcat:Distribution",
+                    "description": "ABoVE: SAR-based Methane Ebullition Flux from Lakes, Five Regions, Alaska, 2007-2010: atqasuk.kml",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/SAR_Methane_Ebullition_AK/comp/atqasuk.kml",
+                    "mediaType": "application/vnd.google-earth.kml+xml",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/vnd.google-earth.kml+xml",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/SAR_Methane_Ebullition_AK/comp/barrow_peninsula.kml",
-                    "description": "ABoVE: SAR-based Methane Ebullition Flux from Lakes, Five Regions, Alaska, 2007-2010: barrow_peninsula.kml",
                     "@type": "dcat:Distribution",
+                    "description": "ABoVE: SAR-based Methane Ebullition Flux from Lakes, Five Regions, Alaska, 2007-2010: barrow_peninsula.kml",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/SAR_Methane_Ebullition_AK/comp/barrow_peninsula.kml",
+                    "mediaType": "application/vnd.google-earth.kml+xml",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/vnd.google-earth.kml+xml",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/SAR_Methane_Ebullition_AK/comp/fairbanks.kml",
-                    "description": "ABoVE: SAR-based Methane Ebullition Flux from Lakes, Five Regions, Alaska, 2007-2010: fairbanks.kml",
                     "@type": "dcat:Distribution",
+                    "description": "ABoVE: SAR-based Methane Ebullition Flux from Lakes, Five Regions, Alaska, 2007-2010: fairbanks.kml",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/SAR_Methane_Ebullition_AK/comp/fairbanks.kml",
+                    "mediaType": "application/vnd.google-earth.kml+xml",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/vnd.google-earth.kml+xml",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/SAR_Methane_Ebullition_AK/comp/northern_seward_peninsula.kml",
-                    "description": "ABoVE: SAR-based Methane Ebullition Flux from Lakes, Five Regions, Alaska, 2007-2010: northern_seward_peninsula.kml",
                     "@type": "dcat:Distribution",
+                    "description": "ABoVE: SAR-based Methane Ebullition Flux from Lakes, Five Regions, Alaska, 2007-2010: northern_seward_peninsula.kml",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/SAR_Methane_Ebullition_AK/comp/northern_seward_peninsula.kml",
+                    "mediaType": "application/vnd.google-earth.kml+xml",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/SAR_Methane_Ebullition_AK/comp/SAR_Methane_Ebullition_AK.pdf",
-                    "description": "ABoVE: SAR-based Methane Ebullition Flux from Lakes, Five Regions, Alaska, 2007-2010: SAR_Methane_Ebullition_AK.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "ABoVE: SAR-based Methane Ebullition Flux from Lakes, Five Regions, Alaska, 2007-2010: SAR_Methane_Ebullition_AK.pdf",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/SAR_Methane_Ebullition_AK/comp/SAR_Methane_Ebullition_AK.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/vnd.google-earth.kml+xml",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/SAR_Methane_Ebullition_AK/comp/toolik.kml",
-                    "description": "ABoVE: SAR-based Methane Ebullition Flux from Lakes, Five Regions, Alaska, 2007-2010: toolik.kml",
                     "@type": "dcat:Distribution",
+                    "description": "ABoVE: SAR-based Methane Ebullition Flux from Lakes, Five Regions, Alaska, 2007-2010: toolik.kml",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/SAR_Methane_Ebullition_AK/comp/toolik.kml",
+                    "mediaType": "application/vnd.google-earth.kml+xml",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://daac.ornl.gov/ABOVE/guides/SAR_Methane_Ebullition_AK_Fig1.png",
-                    "description": "SAR-based lake ebullition maps. Panel A shows Alaska study regions with SAR footprints outlined in yellow. Subsequent panels show SAR-based CH4 ebullition maps for B) Barrow Peninsula, C) Atqasuk, D) Toolik, E) northern Seward Peninsula, and F) Fairbanks. Study lakes with field-based measurements are outlined (B,C) or boxed (D,E,F) in white. Orange boxes in panel F indicate anthropogenic study lakes. Source: Engram et al. (2020).",
                     "@type": "dcat:Distribution",
+                    "description": "SAR-based lake ebullition maps. Panel A shows Alaska study regions with SAR footprints outlined in yellow. Subsequent panels show SAR-based CH4 ebullition maps for B) Barrow Peninsula, C) Atqasuk, D) Toolik, E) northern Seward Peninsula, and F) Fairbanks. Study lakes with field-based measurements are outlined (B,C) or boxed (D,E,F) in white. Orange boxes in panel F indicate anthropogenic study lakes. Source: Engram et al. (2020).",
+                    "downloadURL": "https://daac.ornl.gov/ABOVE/guides/SAR_Methane_Ebullition_AK_Fig1.png",
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
+            "graphic-preview-description": "SAR-based lake ebullition maps. Panel A shows Alaska study regions with SAR footprints outlined in yellow. Subsequent panels show SAR-based CH4 ebullition maps for B) Barrow Peninsula, C) Atqasuk, D) Toolik, E) northern Seward Peninsula, and F) Fairbanks. Study lakes with field-based measurements are outlined (B,C) or boxed (D,E,F) in white. Orange boxes in panel F indicate anthropogenic study lakes. Source: Engram et al. (2020).",
+            "graphic-preview-file": "https://daac.ornl.gov/ABOVE/guides/SAR_Methane_Ebullition_AK_Fig1.png",
+            "identifier": "C2143401901-ORNL_CLOUD",
+            "issued": "2020-07-15",
+            "keyword": [
+                "snow/ice",
+                "earth science",
+                "terrestrial hydrosphere",
+                "surface water",
+                "atmosphere",
+                "atmospheric chemistry"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1790",
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
             "spatial": "-165.17 64.44 -147.37 71.35",
+            "temporal": "2007-11-13T00:00:00Z/2010-11-11T23:59:59Z",
             "theme": [
                 "ABoVE",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "ABoVE: SAR-based Methane Ebullition Flux from Lakes, Five Regions, Alaska, 2007-2010"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/903",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Shimabukuro, Y.E., and E.M.L.M. Novo. 2007. Pre-LBA FLOODAMA Project Data. ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/903",
-            "issued": "2023-10-03",
-            "temporal": "1986-08-04T00:00:00Z/1995-09-19T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-10-04",
-            "keyword": [
-                "earth science",
-                "biosphere",
-                "surface water",
-                "geomorphic landforms/processes",
-                "terrestrial hydrosphere",
-                "land surface",
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
-            "identifier": "C2777404781-ORNL_CLOUD",
             "description": "This data set provides a digital mosaic of the Amazon River floodplain that was compiled using Landsat TM images. This mosaic was planned in July 1995 as an activity of the EOS-IDS Project that was developed with cooperation among INPE, CENA, University of Washington in Seattle (UW), University of California in Santa Barbara (UCSB), and NASA. The mosaic is composed by 29 Landsat TM images covering a period from 1986 to 1995 that were selected with minimum cloud cover and within the July to September high water season of the Amazon River. These images were geometrically corrected using ground control points extracted from topographic charts and image charts at the 1:250,000 scale. In addition, these images were radiometrically rectified to 231/062 (Manaus region) TM image using the method developed by Hall et al. (1991). The radiometric rectification applied had a good performance for bands 3, 5, and 7, for most of the scenes. For bands 1 and 2 the radiometric rectification was limited, especially for scenes with intense haze. Nevertheless, the overall performance of radiometric normalization allowed the production of a uniform data set for the entire Brazilian Amazon River mainstem floodplain. The mosaic was then built using the best bands (rectified or non-rectified) of the TM images with 90 meter spatial resolution. The mosaic data are provided in geoTIFF-formatted files, rectified and geocoded, for six TM bands (1 to 5 and 7) with 90-meter spatial resolution. The mosaic is divided in two parts: Part 1, from the mouth of the Amazon river in Brazil to the Brazil/Peru boundary and Part 2, from the Brazil/Peru boundary to its spring.There is also a 500-meter resolution mosaic covering all the Amazon river (from spring to the mouth) with geoTIFF-formatted data files for TM bands 3, 4, and 5. The processed, quality controlled and integrated data in the documented Pre-LBA Data sets were originally published as a set of three CD_ROMs (Marengo and Victoria, 1998) but are now archived individually.",
-            "graphic-preview-description": "Browse Image",
-            "title": "Pre-LBA FLOODAMA Project Data",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/lba_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F903",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F903",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/lba/land_use_land_cover_change/FLOODAMA/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/lba/land_use_land_cover_change/FLOODAMA/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/LBA/guides/Pre_LBA_FLOODAMA.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/LBA/guides/Pre_LBA_FLOODAMA.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/903",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/903",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/FLOODAMA/comp/Pre_LBA_FLOODAMA.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/FLOODAMA/comp/Pre_LBA_FLOODAMA.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/FLOODAMA/comp/TM_mosaic_readme.txt",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/FLOODAMA/comp/TM_mosaic_readme.txt",
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
+            "identifier": "C2777404781-ORNL_CLOUD",
+            "issued": "2023-10-03",
+            "keyword": [
+                "earth science",
+                "biosphere",
+                "surface water",
+                "geomorphic landforms/processes",
+                "terrestrial hydrosphere",
+                "land surface",
+                "vegetation"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/903",
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
             "spatial": "-78.19 -18.2 -46.28 1.29",
+            "temporal": "1986-08-04T00:00:00Z/1995-09-19T23:59:59Z",
             "theme": [
                 "LBA-ECO",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Pre-LBA FLOODAMA Project Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/307",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Atkinson, G.B., and B. Funk. 1999. BOREAS Saskatchewan Forest Fire Control Centre Surface Meteorological Data. ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/307",
-            "issued": "2023-11-22",
-            "temporal": "1995-05-05T00:00:00Z/1995-10-01T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-11-27",
-            "keyword": [
-                "precipitation",
-                "atmospheric water vapor",
-                "atmospheric temperature",
-                "atmospheric winds",
-                "atmosphere",
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
-            "identifier": "C2807645802-ORNL_CLOUD",
             "description": "Contains 1994 and 1995 hourly data from various forestry meteorology stations.",
-            "graphic-preview-description": "Browse Image",
-            "title": "BOREAS Saskatchewan Forest Fire Control Centre Surface Meteorological Data",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/boreas_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F307",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F307",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/boreas/STAFF/saskffcc/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/boreas/STAFF/saskffcc/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/BOREAS/guides/Sask_Forestry_Met.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/BOREAS/guides/Sask_Forestry_Met.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/307",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/307",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/STAFF/saskffcc/comp/saskffcc.def",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/STAFF/saskffcc/comp/saskffcc.def",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/msword",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/STAFF/saskffcc/comp/Sask_Forestry_Met.doc",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/STAFF/saskffcc/comp/Sask_Forestry_Met.doc",
+                    "mediaType": "application/msword",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/STAFF/saskffcc/comp/Sask_Forestry_Met.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/STAFF/saskffcc/comp/Sask_Forestry_Met.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/STAFF/saskffcc/comp/Sask_Forestry_Met.txt",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/STAFF/saskffcc/comp/Sask_Forestry_Met.txt",
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
+            "identifier": "C2807645802-ORNL_CLOUD",
+            "issued": "2023-11-22",
+            "keyword": [
+                "precipitation",
+                "atmospheric water vapor",
+                "atmospheric temperature",
+                "atmospheric winds",
+                "atmosphere",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/307",
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
             "spatial": "-108.42 53.33 -102.48 55.38",
+            "temporal": "1995-05-05T00:00:00Z/1995-10-01T23:59:59Z",
             "theme": [
                 "BOREAS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "BOREAS Saskatchewan Forest Fire Control Centre Surface Meteorological Data"
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
-                "pds",
-                "tool",
-                "product"
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
-            "identifier": "NASA-451",
             "description": "PDS Software Release Validation Tool (2.5.0)",
-            "title": "PDS Software Release Validation Tool (2.5.0)",
-            "programCode": [
-                "026:005"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -413792,23 +413772,45 @@
                     "mediaType": "application/html"
                 }
             ],
-            "accrualPeriodicity": "irregular",
+            "identifier": "NASA-451",
+            "issued": "2018-06-25",
+            "keyword": [
+                "pds",
+                "tool",
+                "product"
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
+            "title": "PDS Software Release Validation Tool (2.5.0)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-P-LORRI-3-PLUTO-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This data set contains Calibrated data taken by the New Horizons         Long Range Reconnaissance Imager                                       instrument during the                                                    Pluto encounter                                                        mission phase.  This is VERSION 1.0 of this data set.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-p-lorri-3-pluto-v1.0_9bqk-28i2",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "pluto",
                 "nix",
@@ -413816,331 +413818,331 @@
                 "charon",
                 "hydra"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-P-LORRI-3-PLUTO-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-p-lorri-3-pluto-v1.0_9bqk-28i2",
-            "description": "This data set contains Calibrated data taken by the New Horizons         Long Range Reconnaissance Imager                                       instrument during the                                                    Pluto encounter                                                        mission phase.  This is VERSION 1.0 of this data set.",
-            "title": "NEW HORIZONS                            \n      LORRI PLUTO ENCOUNTER                                                   \n      CALIBRATED V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "NEW HORIZONS                            \n      LORRI PLUTO ENCOUNTER                                                   \n      CALIBRATED V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/AURA/TES/TL2HDON_L2.007",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2017-04-06. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/AURA/TES/TL2HDON_L2.007. https://asdc.larc.nasa.gov/project/TES.",
-            "issued": "2015-08-27",
-            "temporal": "2004-08-22T00:00:00Z/2018-01-22T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2019-06-19",
-            "keyword": [
-                "atmosphere",
-                "atmospheric water vapor",
-                "atmospheric chemistry",
-                "earth science",
-                "atmospheric temperature",
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
-            "identifier": "C1331182625-LARC",
             "description": "TL2HDON_7 is the Tropospheric Emission Spectrometer (TES)/Aura Level 2 Deuterium Oxide Nadir Version 7 data product. It consists of information for one molecular species for an entire Global Survey or Special Observation. TES was an instrument aboard NASA's Aura satellite and was launched from California on July 15, 2004. Data collection for TES is complete. TES Level 2 data contain retrieved species (or temperature) profiles at the observation targets and the estimated errors. The geolocation, quality, and other data (e.g., surface characteristics for nadir observations) were also provided. L2 modeled spectra were evaluated using radiative transfer modeling algorithms. The process, referred to as retrieval, compared observed spectra to the modeled spectra and iteratively updated the atmospheric parameters. L2 standard product files included information for one molecular species (or temperature) for an entire global survey or special observation run. A global survey consisted of a maximum of 16 consecutive orbits.\r\rNadir observations, which point directly to the surface of the Earth, are different from limb observations, which are pointed at various off-nadir angles into the atmosphere. Nadir and limb observations were added to separate L2 files, and a single ancillary file was composed of data that are common to both nadir and limb files. A Nadir sequence within the TES Global Survey was a fixed number of observations within an orbit for a Global Survey. Prior to April 24, 2005, it consisted of two low resolution scans over the same ground locations. After April 24, 2005, Global Survey data consisted of three low resolution scans. The Nadir standard product consists of four files, where each file is composed of the Global Survey Nadir observations from one of four focal planes for a single orbit, i.e. 72 orbit sequences. The Global Survey Nadir observations only used a single set of filter mix. \r\rA Global Survey consisted of observations along 16 consecutive orbits at the start of a two day cycle, over which 4,608 retrievals were performed. Each observation was the input for retrievals of species Volume Mixing Ratios (VMRs), temperature profiles, surface temperature, and other data parameters with associated pressure levels, precision, total error, vertical resolution, total column density, and other diagnostic quantities. Each TES Level 2 standard product reported information in a swath format conforming to the HDF-EOS Aura File Format Guidelines. Each Swath object was bounded by the number of observations in a global survey and a predefined set of pressure levels, representing slices through the atmosphere. Each standard product could have had a variable number of observations depending upon the Global Survey configuration and whether averaging was employed. Also, missing or bad retrievals were not reported. Further, observations were occasionally scheduled on non-global survey days. In general they were measurements made for validation purposes or with highly focused science objectives. Those non-global survey measurements were referred to as \u201cspecial observations.\u201d\r\rA Limb sequence within the TES Global Survey was three high-resolution scans over the same limb locations. The Limb standard product consists of four files, where each file is composed of the Global Survey Limb observations from one of four focal planes for a single orbit, i.e. 72 orbit sequences. The Global Survey Limb observations used a repeating sequence of filter wheel positions. Special Observations could only be scheduled during the 9 or 10 orbit gaps in the Global Surveys, and were conducted in any of three basic modes: stare, transect, step-and-stare. The mode used depended on the science requirement. Each limb observation Limb 1, Limb 2 and Limb 3, were processed independently. Thus, each limb standard product consisted of three sets where each set consisted of 1,152 observations. For TES, the swath object represented one of these sets. Thus, each li",
-            "title": "TES/Aura L2 Deuterium Oxide Nadir V007",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAURA%2FTES%2FTL2HDON_L2.007",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAURA%2FTES%2FTL2HDON_L2.007",
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
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1331182625-LARC",
-                    "description": "Earthdata Search for TL2HDON_7 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for TL2HDON_7 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1331182625-LARC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/AURA/TES/TL2HDON_L2.007",
-                    "description": "DOI data set landing page for TL2HDON_7",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for TL2HDON_7",
+                    "downloadURL": "https://doi.org/10.5067/AURA/TES/TL2HDON_L2.007",
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
-                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/TES/TL2HDON.007/contents.html",
-                    "description": "OPeNDAP data access for TL2HDON_7",
                     "@type": "dcat:Distribution",
+                    "description": "OPeNDAP data access for TL2HDON_7",
+                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/TES/TL2HDON.007/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/TES/TL2HDON.007/",
-                    "description": "ASDC Direct Data Download for TL2HDON_7",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for TL2HDON_7",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/TES/TL2HDON.007/",
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
+            "identifier": "C1331182625-LARC",
+            "issued": "2015-08-27",
+            "keyword": [
+                "atmosphere",
+                "atmospheric water vapor",
+                "atmospheric chemistry",
+                "earth science",
+                "atmospheric temperature",
+                "clouds"
+            ],
+            "landingPage": "https://doi.org/10.5067/AURA/TES/TL2HDON_L2.007",
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
+            "title": "TES/Aura L2 Deuterium Oxide Nadir V007"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ZX0GA2TYWNX4",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "SMEX04 Aircraft Polarimetric Scanning Radiometer (PSR) Data, Sonora, Version 1. Version 1. Archived by National Aeronautics and Space Administration, U.S. Government, NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/ZX0GA2TYWNX4.",
-            "issued": "2004-08-05",
-            "temporal": "2004-08-05T00:00:00Z/2004-08-26T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2004-08-26",
-            "keyword": [
-                "soils",
-                "land surface",
-                "spectral/engineering",
-                "earth science",
-                "microwave"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Jackson",
                 "hasEmail": "mailto:tom.jackson@ars.usda.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA NSIDC DAAC"
-            },
-            "identifier": "C1386205588-NSIDCV0",
             "description": "Notice to Data Users: The documentation for this data set was provided solely by the Principal Investigator(s) and was not further developed, thoroughly reviewed, or edited by NSIDC. Thus, support for this data set may be limited.\n\nThis data set includes brightness temperature and soil moisture data acquired with the Polarimetric Scanning Radiometer (PSR) instrument, an airborne microwave imaging radiometer developed and operated by the National Oceanic and Atmospheric Administration (NOAA) Environmental Technology Laboratory.",
-            "title": "SMEX04 Aircraft Polarimetric Scanning Radiometer (PSR) Data, Sonora, Version 1",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FZX0GA2TYWNX4",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FZX0GA2TYWNX4",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/AVDM/data/soil_moisture/SMEX04/Sonora/aircraft/PSR/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/AVDM/data/soil_moisture/SMEX04/Sonora/aircraft/PSR/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/AVDM/data/soil_moisture/SMEX04/Sonora/aircraft/PSR/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/AVDM/data/soil_moisture/SMEX04/Sonora/aircraft/PSR/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/ZX0GA2TYWNX4",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/ZX0GA2TYWNX4",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/ZX0GA2TYWNX4",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/ZX0GA2TYWNX4",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C1386205588-NSIDCV0",
+            "issued": "2004-08-05",
+            "keyword": [
+                "soils",
+                "land surface",
+                "spectral/engineering",
+                "earth science",
+                "microwave"
+            ],
+            "landingPage": "https://doi.org/10.5067/ZX0GA2TYWNX4",
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
             "spatial": "-110.77258 29.69284 -110.22005 30.56124",
+            "temporal": "2004-08-05T00:00:00Z/2004-08-26T23:59:59.999Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "SMEX04 Aircraft Polarimetric Scanning Radiometer (PSR) Data, Sonora, Version 1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/YR21Q0Q8IPR6",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "EASE-Grid Land-Ocean-Coastline-Ice Masks Derived from Boston University MODIS/Terra Land Cover Data, Version 1. Version 1. Archived by National Aeronautics and Space Administration, U.S. Government, NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/YR21Q0Q8IPR6.",
-            "issued": "2000-07-01",
-            "temporal": "2000-07-01T00:00:00Z/2000-12-31T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2000-12-31",
-            "keyword": [
-                "national geospatial data asset",
-                "land surface",
-                "earth science",
-                "ngda",
-                "land use/land cover"
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
-            "identifier": "C1386205661-NSIDCV0",
             "description": "These Land-Ocean-Coastline-Ice (LOCI) files provide land classification masks derived from the Boston University MOD12Q1 V004 MODIS/Terra 1 km Land Cover Product (Friedl et al. 2002). The masks are available in various EASE-Grid azimuthal and global projections, at 12.5 km and 25 km spatial resolutions. The masks are in flat binary, 1 byte files stored by row. Quick-look browse images of the masks are also available in PNG (.png) format.",
-            "title": "EASE-Grid Land-Ocean-Coastline-Ice Masks Derived from Boston University MODIS/Terra Land Cover Data, Version 1",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FYR21Q0Q8IPR6",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FYR21Q0Q8IPR6",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/nsidc0607_loci_ease/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/nsidc0607_loci_ease/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/YR21Q0Q8IPR6",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/YR21Q0Q8IPR6",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/YR21Q0Q8IPR6",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/YR21Q0Q8IPR6",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C1386205661-NSIDCV0",
+            "issued": "2000-07-01",
+            "keyword": [
+                "national geospatial data asset",
+                "land surface",
+                "earth science",
+                "ngda",
+                "land use/land cover"
+            ],
+            "landingPage": "https://doi.org/10.5067/YR21Q0Q8IPR6",
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
             "spatial": "-180.0 -90.0 180.0 0.0",
+            "temporal": "2000-07-01T00:00:00Z/2000-12-31T23:59:59.999Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "EASE-Grid Land-Ocean-Coastline-Ice Masks Derived from Boston University MODIS/Terra Land Cover Data, Version 1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-X-OSIWAC-2-CVP-COMMISSIONING-V1.4",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This data set contains images acquired by the OSIRIS Wide Angle Camera\nduring the COMMISSIONING mission phase",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-x-osiwac-2-cvp-commissioning-v1.4_9bwh-ek9b",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "area 98",
                 "international rosetta mission",
@@ -414149,483 +414151,492 @@
                 "m42",
                 "eps aqr"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-X-OSIWAC-2-CVP-COMMISSIONING-V1.4",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-x-osiwac-2-cvp-commissioning-v1.4_9bwh-ek9b",
-            "description": "This data set contains images acquired by the OSIRIS Wide Angle Camera\nduring the COMMISSIONING mission phase",
-            "title": "ROSETTA-ORBITER COMMISSIONING OSIWAC 2\n                                      EDR V1.4",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER COMMISSIONING OSIWAC 2\n                                      EDR V1.4"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=CO-SSA-RSS-1-DIGR1-V1.0",
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
-                "dione"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "The Cassini Radio Science Dione Gravity Experiment (DIGR1) Raw Data Archive is a time-ordered collection of radio science raw data acquired on October 10, 11, 12, 2005 during the Tour subphase of the Cassini mission. DATA_SET_DESC =",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.co-ssa-rss-1-digr1-v1.0_9bxk-gsaq",
+            "issued": "2018-06-26",
+            "keyword": [
+                "cassini-huygens",
+                "dione"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=CO-SSA-RSS-1-DIGR1-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.co-ssa-rss-1-digr1-v1.0_9bxk-gsaq",
-            "description": "The Cassini Radio Science Dione Gravity Experiment (DIGR1) Raw Data Archive is a time-ordered collection of radio science raw data acquired on October 10, 11, 12, 2005 during the Tour subphase of the Cassini mission. DATA_SET_DESC =",
-            "title": "CASSINI RSS RAW DATA SET - DIGR1 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
-        },
-        {
-            "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/GOES-18/CERES/GEO_Ed4_GOE18_NH_V01.2",
-            "bureauCode": [
-                "026:00"
-            ],
-            "citation": "2018-08-08. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/GOES-18/CERES/GEO_Ed4_GOE18_NH_V01.2.",
-            "issued": "2023-04-06",
-            "temporal": "2023-01-04T00:00:00Z/2023-08-21T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-04-06",
-            "keyword": [
-                "earth science",
-                "clouds",
-                "atmosphere"
+            "title": "CASSINI RSS RAW DATA SET - DIGR1 V1.0"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "026:00"
             ],
+            "citation": "2018-08-08. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/GOES-18/CERES/GEO_Ed4_GOE18_NH_V01.2.",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Data Manager",
                 "hasEmail": "mailto:larc@eos.nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/LARC/SD/ASDC"
-            },
-            "identifier": "C2736710133-LARC_ASDC",
             "description": "CER_GEO_Ed4_GOE18_NH_V01.2 is the Satellite ClOud and Radiation Property retrieval System (SatCORPS) Clouds and the Earth's Radiant Energy System (CERES) Geostationary Satellite (GEO) Edition 4 Geostationary Operational Environmental Satellite 18 (GOES-18) over the Northern Hemisphere (NH) Version 1.2 data product. Data was collected using the GOES-18 Imager on the GOES-18 Platform. Data collection for this product is in progress. \r\n\r\nThis data set is comprised of cloud micro-physical and radiation properties derived hourly from GOES-18 geostationary satellite imager data using the Langley Research Center (LaRC) SATCORPS algorithms in support of the CERES project. The cloud microphysical and radiation properties from each active geostationary satellite are merged together to create hourly global cloud properties that are used to estimate fluxes between CERES instrument measurements to account for the changing diurnal cycle. The data set is arranged as files for each hour and in netCDF-4 format. The observations are at 4-km resolution (at nadir) and are sub-sampled to 8 km.\r\n\r\nCERES is a key component of the Earth Observing System (EOS) program. The CERES instruments provide radiometric measurements of the Earth's atmosphere from three broadband channels. The CERES missions are a follow-on to the successful Earth Radiation Budget Experiment (ERBE) mission. The first CERES instrument, the proto flight model (PFM), was launched on November 27, 1997, as part of the Tropical Rainfall Measuring Mission (TRMM). Two CERES instruments (FM1 and FM2) were launched into polar orbit onboard the Earth Observing System (EOS) flagship Terra on December 18, 1999. Two additional CERES instruments (FM3 and FM4) were launched onboard Earth Observing System (EOS) Aqua on May 4, 2002. The CERES FM5 instrument was launched onboard the Suomi National Polar-orbiting Partnership (NPP) satellite on October 28, 2011. The newest CERES instrument (FM6) was launched onboard the Joint Polar-Orbiting Satellite System 1 (JPSS-1) satellite, now called NOAA-20, on November 18, 2017.",
-            "title": "SatCORPS CERES GEO Edition 4 GOES-18 Northern Hemisphere Version 1.2",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGOES-18%2FCERES%2FGEO_Ed4_GOE18_NH_V01.2",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGOES-18%2FCERES%2FGEO_Ed4_GOE18_NH_V01.2",
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
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2736710133-LARC_ASDC",
-                    "description": "Earthdata Search for CER_GEO_Ed4_GOE18_NH_V01.2 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for CER_GEO_Ed4_GOE18_NH_V01.2 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2736710133-LARC_ASDC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/GOES-18/CERES/GEO_Ed4_GOE18_NH_V01.2",
-                    "description": "DOI data set landing page for CER_GEO_Ed4_GOE18_NH_V01.2",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for CER_GEO_Ed4_GOE18_NH_V01.2",
+                    "downloadURL": "https://doi.org/10.5067/GOES-18/CERES/GEO_Ed4_GOE18_NH_V01.2",
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
-                    "downloadURL": "https://eospso.gsfc.nasa.gov/atbd-category/40",
-                    "description": "CERES ATBD",
                     "@type": "dcat:Distribution",
+                    "description": "CERES ATBD",
+                    "downloadURL": "https://eospso.gsfc.nasa.gov/atbd-category/40",
+                    "mediaType": "text/html",
                     "title": "View this dataset's algorithm theoretical basis document"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/CERES/GEO/Edition4/GOE18_NH_V01.2/",
-                    "description": "ASDC Direct Data Download for CER_GEO_Ed4_GOE18_NH_V01.2",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for CER_GEO_Ed4_GOE18_NH_V01.2",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/CERES/GEO/Edition4/GOE18_NH_V01.2/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/CERES/GEO/Edition4/GOE18_NH_V01.2/contents.html",
-                    "description": "OPeNDAP data access for CER_GEO_Ed4_GOE18_NH_V01.2",
                     "@type": "dcat:Distribution",
+                    "description": "OPeNDAP data access for CER_GEO_Ed4_GOE18_NH_V01.2",
+                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/CERES/GEO/Edition4/GOE18_NH_V01.2/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 }
             ],
+            "identifier": "C2736710133-LARC_ASDC",
+            "issued": "2023-04-06",
+            "keyword": [
+                "earth science",
+                "clouds",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.5067/GOES-18/CERES/GEO_Ed4_GOE18_NH_V01.2",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2023-04-06",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/LARC/SD/ASDC"
+            },
             "spatial": "<?xml version=\"1.0\" encoding=\"UTF-8\"?><gml:Polygon xmlns:gml=\"http://www.opengis.net/gml/3.2\" srsName=\"EPSG:9825\"><gml:outerBoundaryIs><gml:LinearRing><gml:posList>0.0 -180.0 0.0 -90.0 60.0 -90.0 60.0 -180.0 0.0 -180.0</gml:posList></gml:LinearRing></gml:outerBoundaryIs><gml:innerBoundaryIs></gml:innerBoundaryIs></gml:Polygon>",
+            "temporal": "2023-01-04T00:00:00Z/2023-08-21T00:00:00Z",
             "theme": [
                 "CERES",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "SatCORPS CERES GEO Edition 4 GOES-18 Northern Hemisphere Version 1.2"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-X-SREM-5-ESC1-MTP010-V1.0",
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
+            "description": "This data set contains derived electron and proton flux energies in MeV from the Standard Radiation Environment Monitor (SREM) instrument on the Rosetta spacecraft, which had the primary target of comet 67P/Churyumov-Gerasimenko. These are CODMAC Level 5 derived data, and measure the radiation in the spacecraft environment during the Medium Term Plan 10 period of the ESCORT 1 mission phase.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-x-srem-5-esc1-mtp010-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-X-SREM-5-ESC1-MTP010-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-x-srem-5-esc1-mtp010-v1.0",
-            "description": "This data set contains derived electron and proton flux energies in MeV from the Standard Radiation Environment Monitor (SREM) instrument on the Rosetta spacecraft, which had the primary target of comet 67P/Churyumov-Gerasimenko. These are CODMAC Level 5 derived data, and measure the radiation in the spacecraft environment during the Medium Term Plan 10 period of the ESCORT 1 mission phase.",
-            "title": "ROSETTA-ORBITER 67P SREM 5 ESCORT 1\n    MTP010 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P SREM 5 ESCORT 1\n    MTP010 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/EPIC/DSCOVR/L2_CLOUD_03",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2018-01-12. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/EPIC/DSCOVR/L2_CLOUD_03.",
-            "issued": "2017-11-05",
-            "temporal": "2015-06-13T00:00:00Z/2022-01-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2018-05-29",
-            "keyword": [
-                "atmosphere",
-                "earth science",
-                "clouds"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Yuekui Yang",
                 "hasEmail": "mailto:yuekui.yang-1@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/LARC/SD/ASDC"
-            },
-            "identifier": "C1982417666-LARC_ASDC",
             "description": "DSCOVR_EPIC_L2_CLOUD_03 is the Deep Space Climate Observatory (DSCOVR) Earth Polychromatic Imaging Camera (EPIC) Level 2 Cloud version 03 data product. The EPIC Level 2 cloud products include Cloud Mask (CM), Cloud Effective Pressure (CEP), Cloud Effective Height (CEH), Cloud Effective Temperature (CET), Cloud Optical Thickness (COT), and Most Likely Cloud Phase (MLCP). All the products are provided at the EPIC original temporal and special resolutions. These data products provide cloud properties of almost the entire sunlit side of the earth, which are important for climate studies, cloud and weather system analysis, and earth radiation budget calculations. Data collection for this product is ongoing.\r\n\r\nDetails about the algorithms for generating the operational EPIC L2 Cloud Products can be found in Yang et al., 2019, Meyer et al., 2016, and Zhou et al., 2020. A brief description is provided below: \r\n(1) The EPIC CM is based on the threshold method; surface is classified into three categories: land, deep water and snow/ice; CM with confidence level is determined independently for each surface type. \r\n(2) For the CEP/CEH, the Mixed Lambertian-Equivalent Reflectivity (MLER) model is adopted, which assumes that an EPIC pixel contains two Lambertian reflectors, the surface and the cloud. This assumption simplifies the radiative transfer equation and cloud pressure can be retrieved using the oxygen A- and B-band pairs. Since the MLER model does not take into account the effect of photon penetration into clouds, the retrieved cloud pressure is an effective pressure. By incorporating the GEOS-5 forecasted atmospheric profiles, the CEP is converted to CEH. \r\n(3) The EPIC COT product is produced using the operational MODIS cloud retrieval infrastructure. Since EPIC does not have particle size sensitive channels, a single channel retrieval algorithm was developed assuming fixed values for cloud effective radius (CER). In addition, cloud phase determination capability for EPIC is limited; hence the EPIC COT product provides two retrievals for each cloudy pixel, one assuming liquid phase and the other ice phase. A likely cloud phase is also provided based on the CEH.",
-            "title": "DSCOVR EPIC Level 2 Cloud Version 03",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FEPIC%2FDSCOVR%2FL2_CLOUD_03",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FEPIC%2FDSCOVR%2FL2_CLOUD_03",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://epic.gsfc.nasa.gov/science/products/cloud",
-                    "description": "DSCOVR EPIC Cloud Product Overview",
                     "@type": "dcat:Distribution",
+                    "description": "DSCOVR EPIC Cloud Product Overview",
+                    "downloadURL": "https://epic.gsfc.nasa.gov/science/products/cloud",
+                    "mediaType": "text/html",
                     "title": "The dataset's home page"
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
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/dscovr/EPIC_Data_Format_Control_Book_2016-07-01.pdf",
-                    "description": "EPIC Data Format Control Book Specification July 1, 2016",
                     "@type": "dcat:Distribution",
+                    "description": "EPIC Data Format Control Book Specification July 1, 2016",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/dscovr/EPIC_Data_Format_Control_Book_2016-07-01.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's processing history"
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
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/dscovr/EPICCloudProductDescription_Nov2017_1.pdf",
-                    "description": "EPIC Cloud Product Description",
                     "@type": "dcat:Distribution",
+                    "description": "EPIC Cloud Product Description",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/dscovr/EPICCloudProductDescription_Nov2017_1.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.nasa.gov/image-feature/nasa-captures-epic-earth-image",
-                    "description": "NASA Captures \"EPIC\" Earth Image Article from July 20, 2015",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Captures \"EPIC\" Earth Image Article from July 20, 2015",
+                    "downloadURL": "https://www.nasa.gov/image-feature/nasa-captures-epic-earth-image",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
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
-                    "downloadURL": "https://doi.org/10.5067/EPIC/DSCOVR/L2_CLOUD_03",
-                    "description": "DOI data set landing page for DSCOVR_EPIC_L2_CLOUD_03",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for DSCOVR_EPIC_L2_CLOUD_03",
+                    "downloadURL": "https://doi.org/10.5067/EPIC/DSCOVR/L2_CLOUD_03",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1982417666-LARC_ASDC",
-                    "description": "Earthdata Search for DSCOVR_EPIC_L2_CLOUD_03 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for DSCOVR_EPIC_L2_CLOUD_03 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1982417666-LARC_ASDC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/DSCOVR/EPIC/L2_CLOUD_03/",
-                    "description": "ASDC Direct Data Download for DSCOVR_EPIC_L2_CLOUD_03",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for DSCOVR_EPIC_L2_CLOUD_03",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/DSCOVR/EPIC/L2_CLOUD_03/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 }
             ],
+            "identifier": "C1982417666-LARC_ASDC",
+            "issued": "2017-11-05",
+            "keyword": [
+                "atmosphere",
+                "earth science",
+                "clouds"
+            ],
+            "landingPage": "https://doi.org/10.5067/EPIC/DSCOVR/L2_CLOUD_03",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2018-05-29",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/LARC/SD/ASDC"
+            },
             "spatial": "<?xml version=\"1.0\" encoding=\"UTF-8\"?><gml:Polygon xmlns:gml=\"http://www.opengis.net/gml/3.2\" srsName=\"EPSG:9825\"><gml:outerBoundaryIs><gml:LinearRing><gml:posList>-90.0 -180.0 -90.0 180.0 90.0 180.0 90.0 -180.0 -90.0 -180.0</gml:posList></gml:LinearRing></gml:outerBoundaryIs><gml:innerBoundaryIs></gml:innerBoundaryIs></gml:Polygon>",
+            "temporal": "2015-06-13T00:00:00Z/2022-01-17T00:00:00Z",
             "theme": [
                 "DSCOVR",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "DSCOVR EPIC Level 2 Cloud Version 03"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://podaac.jpl.nasa.gov/ws/metadata/dataset/index.html",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2015-11-30",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
-            "references": [
-                "https://data.nasa.gov/developer"
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Jason Duley",
+                "hasEmail": "mailto:jason.duley@nasa.gov"
+            },
+            "description": "PO.DAAC provides several ways to discover and access physical oceanography data, from the PO.DAAC Web Portal to FTP access to front-end user interfaces (see http://podaac.jpl.nasa.gov).  That same data can also be discovered and accessed through PO.DAAC Web Services, enabling efficient machine-to-machine communication and data transfers.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "PO.DAAC provides several ways to discover and access physical oceanography data, from the PO.DAAC Web Portal to FTP access to front-end user interfaces (see http://podaac.jpl.nasa.gov).  That same data can also be discovered and accessed through PO.DAAC Web Services, enabling efficient machine-to-machine communication and data transfers.",
+                    "downloadURL": "http://podaac.jpl.nasa.gov/ws/metadata/dataset/index.html",
+                    "mediaType": "text/html",
+                    "title": "JPL Physical Oceanography Distributed Active Archive Center (PODAAC) Dataset Metadata API"
+                }
             ],
+            "identifier": "API-25",
+            "issued": "2015-11-30",
             "keyword": [
                 "api",
                 "oceanography",
@@ -414633,1513 +414644,1481 @@
                 "earth science research",
                 "granule"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Jason Duley",
-                "hasEmail": "mailto:jason.duley@nasa.gov"
-            },
+            "landingPage": "http://podaac.jpl.nasa.gov/ws/metadata/dataset/index.html",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:001"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "API-25",
-            "description": "PO.DAAC provides several ways to discover and access physical oceanography data, from the PO.DAAC Web Portal to FTP access to front-end user interfaces (see http://podaac.jpl.nasa.gov).  That same data can also be discovered and accessed through PO.DAAC Web Services, enabling efficient machine-to-machine communication and data transfers.",
-            "title": "JPL Physical Oceanography Distributed Active Archive Center (PODAAC) Dataset Metadata API",
-            "programCode": [
-                "026:001"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://podaac.jpl.nasa.gov/ws/metadata/dataset/index.html",
-                    "description": "PO.DAAC provides several ways to discover and access physical oceanography data, from the PO.DAAC Web Portal to FTP access to front-end user interfaces (see http://podaac.jpl.nasa.gov).  That same data can also be discovered and accessed through PO.DAAC Web Services, enabling efficient machine-to-machine communication and data transfers.",
-                    "@type": "dcat:Distribution",
-                    "title": "JPL Physical Oceanography Distributed Active Archive Center (PODAAC) Dataset Metadata API"
-                }
+            "references": [
+                "https://data.nasa.gov/developer"
             ],
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "JPL Physical Oceanography Distributed Active Archive Center (PODAAC) Dataset Metadata API"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-I0046-3-REDDYVESTA-V1.0",
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
-                "support archives"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This data set contains low-resolution near-infrared (~0.7-2.5 microns) spectra of main belt asteroid (4) Vesta observed with the SpeX instrument on NASA Infrared Telescope Facility (IRTF) on Mauna Kea, Hawai'i, and reported in Reddy et al. (2011). This data set archives reduced, calibrated spectra that were obtained as part of ground-based characterization of Vesta prior to the arrival of Dawn spacecraft. They have been used for detailed rotationally-resolved mineralogical/compositional analysis.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-i0046-3-reddyvesta-v1.0_9c6g-ejzf",
+            "issued": "2021-05-21",
+            "keyword": [
+                "4 vesta",
+                "support archives"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-I0046-3-REDDYVESTA-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-i0046-3-reddyvesta-v1.0_9c6g-ejzf",
-            "description": "This data set contains low-resolution near-infrared (~0.7-2.5 microns) spectra of main belt asteroid (4) Vesta observed with the SpeX instrument on NASA Infrared Telescope Facility (IRTF) on Mauna Kea, Hawai'i, and reported in Reddy et al. (2011). This data set archives reduced, calibrated spectra that were obtained as part of ground-based characterization of Vesta prior to the arrival of Dawn spacecraft. They have been used for detailed rotationally-resolved mineralogical/compositional analysis.",
-            "title": "REDDY VESTA ROTATIONALLY RESOLVED NEAR-INFRARED SPECTRA V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "REDDY VESTA ROTATIONALLY RESOLVED NEAR-INFRARED SPECTRA V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG2-S-PLS-5-ION-MOM-96.0SEC",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "THIS DATA SET CONTAINS ESTIMATES OF THE ION MOMENT DENSITY IN THE PLS VOLTAGE RANGE (10-5950 EV/Q) AT SATURN DURING THE VOYAGER 2 ENCOUNTER. RIGID COROTATION IS ASSUMED, WHICH LEADS TO AN UNDERESTIMATE OF THE DENSITY IN SOME REGIONS, AS DOES THE USE OF AN ACCEPTANCE AREA RELEVANT FOR A COLD BEAM FOR PLASMA WHICH IS TRANSONIC IS SOME REGIONS. DENSITIES MAY BE UNDERESTIMATED BY A FACTOR OF 2-3 IN THE INNER MAGNETOSPHERE, SO THIS DATA SET SHOULD BE USED PRIMARILY FOR STUDIES USING VARIATIONS IN PLASMA DENSITY. THE FIT DENSITIES GIVE A BETTER ESTIMATE OF THE ABSOLUTE DENSITY. THIS IS THE DATA SHOWN AND DESCRIBED IN DETAIL IN LAZARUS AND MCNUTT (1983). DATA FORMAT: COLUMNS 1-5 ARE TIME (YEAR, DAY, HOUR, MIN, SEC) AND COLUMN 6 IS THE MOMENT DENSITY IN CM-3. EACH ROW HAS FORMAT (I5,I4,2I3,I4,F8.3). ADDITIONAL INFORMATION ABOUT THIS DATASET AND THE INSTRUMENT WHICH PRODUCED IT CAN BE FOUND ELSEWHERE IN THIS CATALOG. AN OVERVIEW OF THE DATA IN THIS DATA SET CAN BE FOUND IN LAZARUS AND MCNUTT (1983) AND A COMPLETE INSTRUMENT DESCRIPTION CAN BE FOUND IN BRIDGE (1977).",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg2-s-pls-5-ion-mom-96.0sec_9c74-9ubb",
             "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "saturn",
                 "comet sl9/jupiter collision",
                 "voyager"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG2-S-PLS-5-ION-MOM-96.0SEC",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg2-s-pls-5-ion-mom-96.0sec_9c74-9ubb",
-            "description": "THIS DATA SET CONTAINS ESTIMATES OF THE ION MOMENT DENSITY IN THE PLS VOLTAGE RANGE (10-5950 EV/Q) AT SATURN DURING THE VOYAGER 2 ENCOUNTER. RIGID COROTATION IS ASSUMED, WHICH LEADS TO AN UNDERESTIMATE OF THE DENSITY IN SOME REGIONS, AS DOES THE USE OF AN ACCEPTANCE AREA RELEVANT FOR A COLD BEAM FOR PLASMA WHICH IS TRANSONIC IS SOME REGIONS. DENSITIES MAY BE UNDERESTIMATED BY A FACTOR OF 2-3 IN THE INNER MAGNETOSPHERE, SO THIS DATA SET SHOULD BE USED PRIMARILY FOR STUDIES USING VARIATIONS IN PLASMA DENSITY. THE FIT DENSITIES GIVE A BETTER ESTIMATE OF THE ABSOLUTE DENSITY. THIS IS THE DATA SHOWN AND DESCRIBED IN DETAIL IN LAZARUS AND MCNUTT (1983). DATA FORMAT: COLUMNS 1-5 ARE TIME (YEAR, DAY, HOUR, MIN, SEC) AND COLUMN 6 IS THE MOMENT DENSITY IN CM-3. EACH ROW HAS FORMAT (I5,I4,2I3,I4,F8.3). ADDITIONAL INFORMATION ABOUT THIS DATASET AND THE INSTRUMENT WHICH PRODUCED IT CAN BE FOUND ELSEWHERE IN THIS CATALOG. AN OVERVIEW OF THE DATA IN THIS DATA SET CAN BE FOUND IN LAZARUS AND MCNUTT (1983) AND A COMPLETE INSTRUMENT DESCRIPTION CAN BE FOUND IN BRIDGE (1977).",
-            "title": "VOYAGER 2 SATURN PLASMA DERIVED ION MOMENTS 96 SEC",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "VOYAGER 2 SATURN PLASMA DERIVED ION MOMENTS 96 SEC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=HST-M-WFPC2-3-V1.0",
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
-                "mars"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "The Hubble Space Telescope Wide Field Planetary Camera 2 data archive contains calibrated data of Mars observed between April 27, 1999 and September 4, 2001. These are full-disk images of Mars obtained primarily through narrowband filters and in the wavelength interval of 255 to 1042 nm. The data have been calibrated to radiance factor, or I/F.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.hst-m-wfpc2-3-v1.0_9c8g-3gwv",
+            "issued": "2018-06-26",
+            "keyword": [
+                "mars"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=HST-M-WFPC2-3-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.hst-m-wfpc2-3-v1.0_9c8g-3gwv",
-            "description": "The Hubble Space Telescope Wide Field Planetary Camera 2 data archive contains calibrated data of Mars observed between April 27, 1999 and September 4, 2001. These are full-disk images of Mars obtained primarily through narrowband filters and in the wavelength interval of 255 to 1042 nm. The data have been calibrated to radiance factor, or I/F.",
-            "title": "HST WIDE FIELD PLANETARY CAMERA 2 OBSERVATIONS OF MARS",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "HST WIDE FIELD PLANETARY CAMERA 2 OBSERVATIONS OF MARS"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/VIIRS/VNP43D18.001",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Crystal Schaaf, Zhuosen Wang, Xiaoyang Zhang, Alan Strahler\r\n. 2019-11-07. VNP43D18. Version 001. VIIRS/NPP BRDF/Albedo Parameter 3 Band M7 Daily L3 Global 30 ArcSec CMG V001\r\n. Sioux Falls, South Dakota, USA. Archived by National Aeronautics and Space Administration, U.S. Government, NASA EOSDIS Land Processes Distributed Active Archive Center. https://doi.org/10.5067/VIIRS/VNP43D18.001. https://doi.org/10.5067/VIIRS/VNP43D18.001. Digital Science Data. The DOI landing page provides citations in APA and Chicago styles.\r\n.",
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
-            "identifier": "C1607318934-LPDAAC_ECS",
-            "description": "The NASA/NOAA Suomi National Polar-orbiting Partnership (Suomi NPP) Visible Infrared Imaging Radiometer Suite (VIIRS) Bidirectional Reflectance Distribution Function (BRDF) and Albedo Model Parameter 3 Band M7 product (VNP43D18) is produced daily using 16 days of data at 30 arc second (1,000 meter) resolution. Data are temporally weighted to the ninth day, which is reflected in the file name. The VNP43D product suite is provided in a Climate Modeling Grid (CMG), which covers the entire globe for use in climate simulation models. Due to the large file size, each VNP43D product contains just one data layer. Each of the three model parameters (isotropic, volumetric, and geometric) for each of the nine VIIRS moderate resolution bands along with the visible, near-infrared (NIR), and shortwave bands included in the VNP43MA1 (https://doi.org/10.5067/VIIRS/VNP43MA1.001) product is stored in a separate file as VNP43D01 through VNP43D36. In addition to the bands included in VNP43MA1, this product suite includes model parameters for the VIIRS Day/Night Band (DNB) as VNP43D37 through VNP43D39. Details regarding methodology are available on the VNP43MA1 product page and in the Algorithm Theoretical Basis Document (ATBD).\r\n\r\nVNP43D18 is the BRDF geometric parameter for VIIRS band M7 (0.865 \u03bcm). The geometric parameter, in conjunction with the isotropic and volumetric parameters, is used to derive the BRDF/Albedo values for VIIRS band M7.",
-            "release-place": "Sioux Falls, South Dakota, USA",
-            "series-name": "VNP43D18",
             "creator": "Crystal Schaaf, Zhuosen Wang, Xiaoyang Zhang, Alan Strahler",
-            "title": "VIIRS/NPP BRDF/Albedo Parameter 3 Band M7 Daily L3 Global 30 ArcSec CMG V001",
-            "programCode": [
-                "026:001"
-            ],
+            "data-presentation-form": "Digital Science Data",
+            "description": "The NASA/NOAA Suomi National Polar-orbiting Partnership (Suomi NPP) Visible Infrared Imaging Radiometer Suite (VIIRS) Bidirectional Reflectance Distribution Function (BRDF) and Albedo Model Parameter 3 Band M7 product (VNP43D18) is produced daily using 16 days of data at 30 arc second (1,000 meter) resolution. Data are temporally weighted to the ninth day, which is reflected in the file name. The VNP43D product suite is provided in a Climate Modeling Grid (CMG), which covers the entire globe for use in climate simulation models. Due to the large file size, each VNP43D product contains just one data layer. Each of the three model parameters (isotropic, volumetric, and geometric) for each of the nine VIIRS moderate resolution bands along with the visible, near-infrared (NIR), and shortwave bands included in the VNP43MA1 (https://doi.org/10.5067/VIIRS/VNP43MA1.001) product is stored in a separate file as VNP43D01 through VNP43D36. In addition to the bands included in VNP43MA1, this product suite includes model parameters for the VIIRS Day/Night Band (DNB) as VNP43D37 through VNP43D39. Details regarding methodology are available on the VNP43MA1 product page and in the Algorithm Theoretical Basis Document (ATBD).\r\n\r\nVNP43D18 is the BRDF geometric parameter for VIIRS band M7 (0.865 \u03bcm). The geometric parameter, in conjunction with the isotropic and volumetric parameters, is used to derive the BRDF/Albedo values for VIIRS band M7.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FVIIRS%2FVNP43D18.001",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FVIIRS%2FVNP43D18.001",
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
-                    "downloadURL": "https://doi.org/10.5067/VIIRS/VNP43D18.001",
-                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
+                    "downloadURL": "https://doi.org/10.5067/VIIRS/VNP43D18.001",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/xhdf5",
-                    "downloadURL": "https://e4ftl01.cr.usgs.gov/VIIRS/VNP43D18.001/",
-                    "description": "LP DAAC Data Pool provides direct access to available products via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "LP DAAC Data Pool provides direct access to available products via HTTPS.",
+                    "downloadURL": "https://e4ftl01.cr.usgs.gov/VIIRS/VNP43D18.001/",
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
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=C1607318934-LPDAAC_ECS",
-                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=C1607318934-LPDAAC_ECS",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://opendap.cr.usgs.gov/opendap/hyrax/VNP43D18.001/contents.html",
-                    "description": "Access data via Open-source Project for a Network Data Access Protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access data via Open-source Project for a Network Data Access Protocol.",
+                    "downloadURL": "https://opendap.cr.usgs.gov/opendap/hyrax/VNP43D18.001/contents.html",
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
-                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/filespec/VIIRS/1/VNP43D18",
-                    "description": "The File Specification provides a description of the product file including Scientific Data Sets and their attributes.",
                     "@type": "dcat:Distribution",
+                    "description": "The File Specification provides a description of the product file including Scientific Data Sets and their attributes.",
+                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/filespec/VIIRS/1/VNP43D18",
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
+            "identifier": "C1607318934-LPDAAC_ECS",
+            "issued": "2019-11-07",
+            "keyword": [
+                "surface radiative properties",
+                "earth science",
+                "land surface"
+            ],
+            "landingPage": "https://doi.org/10.5067/VIIRS/VNP43D18.001",
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
+            "series-name": "VNP43D18",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2012-01-19T00:00:00Z/2024-05-20T00:00:00Z",
             "theme": [
                 "NPP-JPSS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "VIIRS/NPP BRDF/Albedo Parameter 3 Band M7 Daily L3 Global 30 ArcSec CMG V001"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/MODIS/CLDPROPCOSP_M3_VIIRS_NOAA20.011",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "MODIS Atmosphere Science Team. 2024-05-10. VIIRS/SNPP Cloud Properties COSP Level 3 monthly, 1x1 degree grid. Version 1.1. MODAPS at NASA/GSFC. Archived by National Aeronautics and Space Administration, U.S. Government, L1 and Atmosphere Archive and Distribution System (LAADS). https://doi.org/10.5067/MODIS/CLDPROPCOSP_M3_VIIRS_NOAA20.011. https://doi.org/10.5067/MODIS/CLDPROPCOSP_M3_VIIRS_NOAA20.011.",
-            "issued": "2024-01-10",
-            "temporal": "2018-03-01T00:00:00Z/2025-01-13T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-01",
-            "keyword": [
-                "earth science",
-                "atmospheric radiation",
-                "atmosphere",
-                "clouds"
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
-            "identifier": "C2946981699-LAADS",
-            "description": "The VIIRS/NOAA20 Cloud Properties COSP Level 3 monthly, 1x1 degree grid product is a new L3 CLDPROP COSP Cloud product with short-name CLDPROPCOSP_M3_VIIRS_NOAA20.  It contains VIIRS SNPP cloud mask, cloud top, and cloud optical retrieval data over monthly timeframe. It provides a set of custom cloud-related parameters for better comparison with climate model output. The \u201cCOSP\u201d acronym in the short-name stands for  Cloud Feedback Model Intercomparison Project (CFMIP) Observation Simulator Package. \nProvided in netCDF4 format, it contains 32 aggregated science data sets (SDS/parameters).\n\nConsult the CLDPROPCOSP User Guide for details regarding how the L3 monthly statistics are computed, and to learn more about the gridding and sampling protocols specific to this product and a number of other topics germane to the user community.  The collection of this product starts from March 1, 2018 and includes 12 granules each calendar year.",
-            "release-place": "MODAPS at NASA/GSFC",
             "creator": "MODIS Atmosphere Science Team",
-            "title": "VIIRS/NOAA20 Cloud Properties COSP Level 3 monthly, 1x1 deg. grid",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The VIIRS/NOAA20 Cloud Properties COSP Level 3 monthly, 1x1 degree grid product is a new L3 CLDPROP COSP Cloud product with short-name CLDPROPCOSP_M3_VIIRS_NOAA20.  It contains VIIRS SNPP cloud mask, cloud top, and cloud optical retrieval data over monthly timeframe. It provides a set of custom cloud-related parameters for better comparison with climate model output. The \u201cCOSP\u201d acronym in the short-name stands for  Cloud Feedback Model Intercomparison Project (CFMIP) Observation Simulator Package. \nProvided in netCDF4 format, it contains 32 aggregated science data sets (SDS/parameters).\n\nConsult the CLDPROPCOSP User Guide for details regarding how the L3 monthly statistics are computed, and to learn more about the gridding and sampling protocols specific to this product and a number of other topics germane to the user community.  The collection of this product starts from March 1, 2018 and includes 12 granules each calendar year.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMODIS%2FCLDPROPCOSP_M3_VIIRS_NOAA20.011",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMODIS%2FCLDPROPCOSP_M3_VIIRS_NOAA20.011",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/MODIS/CLDPROPCOSP_M3_VIIRS_NOAA20.011",
-                    "description": "The product landing page",
                     "@type": "dcat:Distribution",
+                    "description": "The product landing page",
+                    "downloadURL": "https://doi.org/10.5067/MODIS/CLDPROPCOSP_M3_VIIRS_NOAA20.011",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://atmosphere-imager.gsfc.nasa.gov/sites/default/files/ModAtmo/documents/L3_MCD06COSP_UserGuide_v1.5.pdf",
-                    "description": "Daily MCD06COSP product User Guide",
                     "@type": "dcat:Distribution",
+                    "description": "Daily MCD06COSP product User Guide",
+                    "downloadURL": "https://atmosphere-imager.gsfc.nasa.gov/sites/default/files/ModAtmo/documents/L3_MCD06COSP_UserGuide_v1.5.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/search/order/2/CLDPROPCOSP_M3_VIIRS_NOAA20--5111",
-                    "description": "Search and order products from LAADS website.",
                     "@type": "dcat:Distribution",
+                    "description": "Search and order products from LAADS website.",
+                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/search/order/2/CLDPROPCOSP_M3_VIIRS_NOAA20--5111",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through LAADS"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/archive/allData/5111/CLDPROPCOSP_M3_VIIRS_NOAA20/",
-                    "description": "Direct access to CLDPROPCOSP_M3_VIIRS_NOAA20 data set.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct access to CLDPROPCOSP_M3_VIIRS_NOAA20 data set.",
+                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/archive/allData/5111/CLDPROPCOSP_M3_VIIRS_NOAA20/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/opendap/RemoteResources/laads/allData/5111/CLDPROPCOSP_M3_VIIRS_NOAA20/contents.html",
-                    "description": "Direct access to product's OPeNDAP directory",
                     "@type": "dcat:Distribution",
+                    "description": "Direct access to product's OPeNDAP directory",
+                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/opendap/RemoteResources/laads/allData/5111/CLDPROPCOSP_M3_VIIRS_NOAA20/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 }
             ],
+            "identifier": "C2946981699-LAADS",
+            "issued": "2024-01-10",
+            "keyword": [
+                "earth science",
+                "atmospheric radiation",
+                "atmosphere",
+                "clouds"
+            ],
+            "landingPage": "https://doi.org/10.5067/MODIS/CLDPROPCOSP_M3_VIIRS_NOAA20.011",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2025-01-01",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Not provided"
+            },
+            "release-place": "MODAPS at NASA/GSFC",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2018-03-01T00:00:00Z/2025-01-13T00:00:00Z",
             "theme": [
                 "NOAA - SPACE WEATHER PROGRAM",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "VIIRS/NOAA20 Cloud Properties COSP Level 3 monthly, 1x1 deg. grid"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MER1-M-PANCAM-2-EDR-SCI-V1.0",
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
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mer1-m-pancam-2-edr-sci-v1.0_9cdm-t4jx",
+            "issued": "2021-05-21",
+            "keyword": [
+                "mars",
+                "mars exploration rover"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MER1-M-PANCAM-2-EDR-SCI-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mer1-m-pancam-2-edr-sci-v1.0_9cdm-t4jx",
-            "description": "NULL",
-            "title": "MER 1 MARS PANORAMIC CAMERA SCIENCE EDR\n                                      VERSION 1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "MER 1 MARS PANORAMIC CAMERA SCIENCE EDR\n                                      VERSION 1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C3166805868-OB_DAAC.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/GSFC/SED/ESD/GCDC/OB.DAAC.",
-            "issued": "2024-07-19",
-            "temporal": "2017-11-29T00:00:00Z/2024-08-12T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-07-19",
-            "keyword": [
-                "oceans",
-                "ocean temperature",
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
-            "identifier": "C3166805868-OB_DAAC",
             "description": "The Ocean Biology DAAC produces near real-time (quicklook) products using the best-available combination of ancillary data from meteorological and ozone data. As such, the inputs and the calibration used are less than optimal. Quicklook products provide a snapshot of the data during a short time period within a single orbit.",
-            "title": "NOAA-20 VIIRS Level-3 Global Mapped 11\u00b5m Day/Night Sea Surface Temperature (SST) - Near Real Time (NRT) Data, version 2024.0",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
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
-                    "downloadURL": "https://oceandata.sci.gsfc.nasa.gov/opendap/VIIRSJ1/L3SMI/",
-                    "description": "OB.DAAC OPeNDAP Site for NOAA-20 VIIRS Standard Mapped Image (SMI) Product",
                     "@type": "dcat:Distribution",
+                    "description": "OB.DAAC OPeNDAP Site for NOAA-20 VIIRS Standard Mapped Image (SMI) Product",
+                    "downloadURL": "https://oceandata.sci.gsfc.nasa.gov/opendap/VIIRSJ1/L3SMI/",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 }
             ],
+            "identifier": "C3166805868-OB_DAAC",
+            "issued": "2024-07-19",
+            "keyword": [
+                "oceans",
+                "ocean temperature",
+                "earth science"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C3166805868-OB_DAAC.html",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2024-07-19",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GCDC/OB.DAAC"
+            },
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2017-11-29T00:00:00Z/2024-08-12T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "NOAA-20 VIIRS Level-3 Global Mapped 11\u00b5m Day/Night Sea Surface Temperature (SST) - Near Real Time (NRT) Data, version 2024.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://c3.nasa.gov/dashlink/resources/315/",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2011-02-18",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
-            "keyword": [
-                "ames",
-                "dashlink",
-                "nasa"
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
-            "identifier": "DASHLINK_315",
             "description": "On line detection techniques to monitor the health of rotating engine components are becoming increasingly attractive options to aircraft engine companies in order to increase safety of operation and lower maintenance costs. Health monitoring remains a challenging feature to easily implement, especially, in the presence of scattered loading conditions, crack size, component geometry and materials properties. The current trend, however, is to utilize noninvasive types of health monitoring or nondestructive techniques to detect hidden flaws and mini cracks before any catastrophic event occurs. These techniques go further to evaluate materials' discontinuities and other anomalies that have grown to the level of critical defects which can lead to failure. Generally, health monitoring is highly dependent on sensor systems that are capable of performing in various engine environmental conditions and able to transmit a signal upon a predetermined crack length, while acting in a neutral form upon the overall performance of the engine system. Efforts are under way at NASA Glenn Research Center through support of the Intelligent Vehicle Health Management Project (IVHM) to develop and implement such sensor technology for a wide variety of applications [1-5]. These efforts are focused on developing high temperature, wireless, low cost and durable products.Therefore, in an effort to address the technical issues concerning health monitoring of a rotor disk, this paper considers data collected from an experimental study using high frequency capacitive sensor technology to capture blade tip clearance and tip timing measurements in a rotating engine-like-disk-to predict the disk faults and assess its structural integrity. The experimental results collected at a range of rotational speeds from tests conducted at the NASA Glenn Research Center's Rotordynamics Laboratory will be evaluated using multiple data-driven anomaly detection techniques [6-9] to identify anomalies in the disk. This study is expected to present a select evaluation of online health monitoring of a rotating disk using these high caliber sensors and test the capability of the in-house spin system.",
-            "title": "Propulsion Health Monitoring of a Turbine Engine Disk using Spin Test Data",
-            "programCode": [
-                "026:029"
-            ],
             "distribution": [
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/publication/abwo10.pdf",
-                    "description": "abwo10.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "abwo10.pdf",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/publication/abwo10.pdf",
+                    "mediaType": "application/pdf",
                     "title": "abwo10.pdf"
                 }
             ],
-            "accrualPeriodicity": "irregular"
+            "identifier": "DASHLINK_315",
+            "issued": "2011-02-18",
+            "keyword": [
+                "ames",
+                "dashlink",
+                "nasa"
+            ],
+            "landingPage": "https://c3.nasa.gov/dashlink/resources/315/",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:029"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Dashlink"
+            },
+            "title": "Propulsion Health Monitoring of a Turbine Engine Disk using Spin Test Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RPCLAP-2-ESC3-MTP018-V2.0",
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
+            "description": "This data set contains\nEDITED data from Rosetta RPC-LAP, acquired during the COMET ESCORT 3\nMTP018 mission phase. Comet C-G/67P was the primary target.\nThis data set supersedes RO-C-RPCLAP-2-ESC3-MTP018-V1.0.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rpclap-2-esc3-mtp018-v2.0_9cgf-zkid",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RPCLAP-2-ESC3-MTP018-V2.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rpclap-2-esc3-mtp018-v2.0_9cgf-zkid",
-            "description": "This data set contains\nEDITED data from Rosetta RPC-LAP, acquired during the COMET ESCORT 3\nMTP018 mission phase. Comet C-G/67P was the primary target.\nThis data set supersedes RO-C-RPCLAP-2-ESC3-MTP018-V1.0.",
-            "title": "ROSETTA-ORBITER 67P RPCLAP 2\nESC3 MTP018 V2.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RPCLAP 2\nESC3 MTP018 V2.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1615934250-OB_DAAC.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, OB.DAAC.",
-            "issued": "2019-06-23",
-            "temporal": "2000-02-24T00:00:00Z/2022-01-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2019-08-08",
-            "keyword": [
-                "ngda",
-                "earth science",
-                "oceans",
-                "national geospatial data asset",
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
-            "identifier": "C1615934250-OB_DAAC",
             "description": "MODIS (or Moderate Resolution Imaging Spectroradiometer) is a key instrument aboard the Terra (EOS AM) and Aqua (EOS PM) satellites. Terra's orbit around the Earth is timed so that it passes from north to south across the equator in the morning, while Aqua passes south to north over the equator in the afternoon. Terra MODIS and Aqua MODIS are viewing the entire Earth's surface every 1 to 2 days, acquiring data in 36 spectral bands, or groups of wavelengths (see MODIS Technical Specifications). These data will improve our understanding of global dynamics and processes occurring on the land, in the oceans, and in the lower atmosphere. MODIS is playing a vital role in the development of validated, global, interactive Earth system models able to predict global change accurately enough to assist policy makers in making sound decisions concerning the protection of our environment.",
-            "title": "Terra MODIS Regional 11\u00b5m Day/Night Sea Surface Temperature (SST) Data, version R2019.0",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://oceandata.sci.gsfc.nasa.gov/directaccess/MODIS-Terra/L2/",
-                    "description": "NASA Ocean Color Web - Data Distribution Site",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Ocean Color Web - Data Distribution Site",
+                    "downloadURL": "https://oceandata.sci.gsfc.nasa.gov/directaccess/MODIS-Terra/L2/",
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
-                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/data/10.5067/TERRA/MODIS/L2/SST/R2019.0",
-                    "description": "MODIS-Terra L2 11\u00b5m Daytime Sea Surface Temperature (SST) Dataset Landing Page",
                     "@type": "dcat:Distribution",
+                    "description": "MODIS-Terra L2 11\u00b5m Daytime Sea Surface Temperature (SST) Dataset Landing Page",
+                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/data/10.5067/TERRA/MODIS/L2/SST/R2019.0",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 }
             ],
+            "identifier": "C1615934250-OB_DAAC",
+            "issued": "2019-06-23",
+            "keyword": [
+                "ngda",
+                "earth science",
+                "oceans",
+                "national geospatial data asset",
+                "ocean temperature"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1615934250-OB_DAAC.html",
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
+            "temporal": "2000-02-24T00:00:00Z/2022-01-17T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Terra MODIS Regional 11\u00b5m Day/Night Sea Surface Temperature (SST) Data, version R2019.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C2263929279-OB_DAAC.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/GSFC/SED/ESD/GCDC/OB.DAAC.",
-            "issued": "2022-09-13",
-            "temporal": "2016-04-25T00:00:00Z/2024-04-22T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-04-13",
-            "keyword": [
-                "atmosphere",
-                "earth science",
-                "oceans",
-                "atmospheric radiation",
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
-            "identifier": "C2263929279-OB_DAAC",
             "description": "The Ocean Biology DAAC produces near real-time (quicklook) products using the best-available combination of ancillary data from meteorological and ozone data. As such, the inputs and the calibration used are less than optimal. Quicklook products provide a snapshot of the data during a short time period within a single orbit.",
-            "title": "Sentinel-3A OLCI Level-3M Global Mapped Earth-observation Reduced Resolution (ERR) Chlorophyll (CHL) - Near Real-time (NRT) Data, version R2022.0",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://oceandata.sci.gsfc.nasa.gov/directdataaccess/Level-3%20Mapped/S3A-OLCI",
-                    "description": "NASA Ocean Color Web - Data Distribution Site",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Ocean Color Web - Data Distribution Site",
+                    "downloadURL": "https://oceandata.sci.gsfc.nasa.gov/directdataaccess/Level-3%20Mapped/S3A-OLCI",
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
-                    "downloadURL": "https://oceandata.sci.gsfc.nasa.gov/opendap/S3OLCI/",
-                    "description": "OB.DAAC OPeNDAP Site for Sentinel-3A OLCI Standard Mapped Image (SMI) Product",
                     "@type": "dcat:Distribution",
+                    "description": "OB.DAAC OPeNDAP Site for Sentinel-3A OLCI Standard Mapped Image (SMI) Product",
+                    "downloadURL": "https://oceandata.sci.gsfc.nasa.gov/opendap/S3OLCI/",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 }
             ],
+            "identifier": "C2263929279-OB_DAAC",
+            "issued": "2022-09-13",
+            "keyword": [
+                "atmosphere",
+                "earth science",
+                "oceans",
+                "atmospheric radiation",
+                "ocean optics"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C2263929279-OB_DAAC.html",
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
+            "title": "Sentinel-3A OLCI Level-3M Global Mapped Earth-observation Reduced Resolution (ERR) Chlorophyll (CHL) - Near Real-time (NRT) Data, version R2022.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/GHVRS-2PN30",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Naval Oceanographic Office. 2018-04-15. GHRSST Level 2P 1 m Depth Global Sea Surface Temperature version 3.0 from the Visible Infrared Imaging Radiometer Suite (VIIRS) on the Suomi NPP satellite (GDS2). Version 3.0. Stennis Space Center, MS, USA. Archived by National Aeronautics and Space Administration, U.S. Government, PO.DAAC. https://doi.org/10.5067/GHVRS-2PN30.",
-            "issued": "2018-02-01",
-            "temporal": "2018-01-30T17:51:49Z/2023-03-01T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2018-02-01",
-            "references": [
-                "https://doi.org/10.1117/12.2017965",
-                "https://doi.org/10.1117/12.2053430"
-            ],
-            "keyword": [
-                "earth science",
-                "oceans",
-                "ocean temperature"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Bruce McKenzie",
                 "hasEmail": "mailto:bruce.mckenzie@navy.mil"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/JPL/PODAAC"
-            },
-            "identifier": "C1996881636-POCLOUD",
-            "description": "A global Group for High Resolution Sea Surface Temperature (GHRSST) Level 2P dataset based on retrievals from the Visible Infrared Imaging Radiometer Suite (VIIRS). This sensor resides on the Suomi National Polar-orbiting Partnership (Suomi_NPP) satellite launched on 28 October 2011. VIIRS is a whiskbroom scanning radiometer which takes measurements in the cross-track direction within a field of regard of 112.56 degrees using 16 detectors and a double-sided mirror assembly. At a nominal altitude of 829 km, the swath width is 3060 km, providing full daily coverage both on the day and night side of the Earth.\nThe VIIRS instrument is a 22-band, multi-spectral scanning radiometer that builds on the heritage of the MODIS , AVHRR and SeaWIFS sensors for sea surface temperature (SST) and ocean color. For the infrared bands for SST the effective pixel size is 750 meters at nadir and the pixel size variation across the swath is constrained to no more than 1600 meters at the edge of the swath.  This L2P SST v3.0 is upgraded from the v2.0 with several significant improvements in processing algorithms, including contamination detection, cloud detection, and data format upgrades.  It contains the global near daily-coverage Sea Surface Temperature at 1-meter depth with 750 m (along) x 750 m (cross) spatial resolution in swath coordinates.  Each netCDF file has 768 x 3200 pixels in size, in compliance with the GHRSST Data Processing Specification (GDS) version 2 format specifications.",
-            "release-place": "Stennis Space Center, MS, USA",
-            "graphic-preview-description": "Thumbnail",
             "creator": "Naval Oceanographic Office",
-            "title": "GHRSST Level 2P 1 m Depth Global Sea Surface Temperature version 3.0 from the Visible Infrared Imaging Radiometer Suite (VIIRS) on the Suomi NPP satellite (GDS2)",
-            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/VIIRS_NPP-NAVO-L2P-v3.0.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "A global Group for High Resolution Sea Surface Temperature (GHRSST) Level 2P dataset based on retrievals from the Visible Infrared Imaging Radiometer Suite (VIIRS). This sensor resides on the Suomi National Polar-orbiting Partnership (Suomi_NPP) satellite launched on 28 October 2011. VIIRS is a whiskbroom scanning radiometer which takes measurements in the cross-track direction within a field of regard of 112.56 degrees using 16 detectors and a double-sided mirror assembly. At a nominal altitude of 829 km, the swath width is 3060 km, providing full daily coverage both on the day and night side of the Earth.\nThe VIIRS instrument is a 22-band, multi-spectral scanning radiometer that builds on the heritage of the MODIS , AVHRR and SeaWIFS sensors for sea surface temperature (SST) and ocean color. For the infrared bands for SST the effective pixel size is 750 meters at nadir and the pixel size variation across the swath is constrained to no more than 1600 meters at the edge of the swath.  This L2P SST v3.0 is upgraded from the v2.0 with several significant improvements in processing algorithms, including contamination detection, cloud detection, and data format upgrades.  It contains the global near daily-coverage Sea Surface Temperature at 1-meter depth with 750 m (along) x 750 m (cross) spatial resolution in swath coordinates.  Each netCDF file has 768 x 3200 pixels in size, in compliance with the GHRSST Data Processing Specification (GDS) version 2 format specifications.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGHVRS-2PN30",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGHVRS-2PN30",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3390/rs71215881",
-                    "description": "Validation of S-NPP VIIRS Sea Surface Temperature Retrieved from NAVO",
                     "@type": "dcat:Distribution",
+                    "description": "Validation of S-NPP VIIRS Sea Surface Temperature Retrieved from NAVO",
+                    "downloadURL": "https://doi.org/10.3390/rs71215881",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ghrsst.jpl.nasa.gov",
-                    "description": "GHRSST Project Page",
                     "@type": "dcat:Distribution",
+                    "description": "GHRSST Project Page",
+                    "downloadURL": "https://ghrsst.jpl.nasa.gov",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
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
-                    "downloadURL": "https://podaac.jpl.nasa.gov/forum",
-                    "description": "PO.DAAC Forum Page",
                     "@type": "dcat:Distribution",
+                    "description": "PO.DAAC Forum Page",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/forum",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/VIIRS_NPP-NAVO-L2P-v3.0.jpg",
-                    "description": "Thumbnail",
                     "@type": "dcat:Distribution",
+                    "description": "Thumbnail",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/VIIRS_NPP-NAVO-L2P-v3.0.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/ghrsst/open/docs/GDS20r5.pdf",
-                    "description": "GHRSST Data User Guide",
                     "@type": "dcat:Distribution",
+                    "description": "GHRSST Data User Guide",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/ghrsst/open/docs/GDS20r5.pdf",
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
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C1996881636-POCLOUD",
-                    "description": "HTTPS endpoint for data browse and download",
                     "@type": "dcat:Distribution",
+                    "description": "HTTPS endpoint for data browse and download",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C1996881636-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1996881636-POCLOUD",
-                    "description": "Browse granule search results in Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse granule search results in Earthdata Search",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1996881636-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 }
             ],
+            "graphic-preview-description": "Thumbnail",
+            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/VIIRS_NPP-NAVO-L2P-v3.0.jpg",
+            "identifier": "C1996881636-POCLOUD",
+            "issued": "2018-02-01",
+            "keyword": [
+                "earth science",
+                "oceans",
+                "ocean temperature"
+            ],
+            "landingPage": "https://doi.org/10.5067/GHVRS-2PN30",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2018-02-01",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/JPL/PODAAC"
+            },
+            "references": [
+                "https://doi.org/10.1117/12.2017965",
+                "https://doi.org/10.1117/12.2053430"
+            ],
+            "release-place": "Stennis Space Center, MS, USA",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2018-01-30T17:51:49Z/2023-03-01T00:00:00Z",
             "theme": [
                 "GHRSST",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "GHRSST Level 2P 1 m Depth Global Sea Surface Temperature version 3.0 from the Visible Infrared Imaging Radiometer Suite (VIIRS) on the Suomi NPP satellite (GDS2)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-A-LORRI-3-KEM1-V1.0",
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
-                "new horizons kuiper belt extended mission"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This data set contains Calibrated data taken by the New Horizons Long Range Reconnaissance Imager instrument during the KEM1 ENCOUNTER mission phase. This is VERSION 1.0 of this data set. This data set contains data acquired by the spacecraft between 08/14/2018 and 12/31/2018. It only includes data downlinked before 01/01/2019. Future datasets may include more data acquired by the spacecraft after 08/13/2018 but downlinked after 12/31/2018. It includes a number of distant Kuiper Belt Objects (DKBOs). It also includes images of the approach field where MU69 was expected to reside during the MU69 encounter on Jan. 1, 2019.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-a-lorri-3-kem1-v1.0_9cky-prwz",
+            "issued": "2021-05-21",
+            "keyword": [
+                "new horizons kuiper belt extended mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-A-LORRI-3-KEM1-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-a-lorri-3-kem1-v1.0_9cky-prwz",
-            "description": "This data set contains Calibrated data taken by the New Horizons Long Range Reconnaissance Imager instrument during the KEM1 ENCOUNTER mission phase. This is VERSION 1.0 of this data set. This data set contains data acquired by the spacecraft between 08/14/2018 and 12/31/2018. It only includes data downlinked before 01/01/2019. Future datasets may include more data acquired by the spacecraft after 08/13/2018 but downlinked after 12/31/2018. It includes a number of distant Kuiper Belt Objects (DKBOs). It also includes images of the approach field where MU69 was expected to reside during the MU69 encounter on Jan. 1, 2019.",
-            "title": "NEW HORIZONS\n      LORRI KEM1\n      CALIBRATED V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "NEW HORIZONS\n      LORRI KEM1\n      CALIBRATED V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-C-5-DDR-PCC-V1.0",
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
-                "comet"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "Physical characteristics of comets observed from -466 to 1975, compiled by S. K. Vsekhsvyatskii.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-c-5-ddr-pcc-v1.0_9cm8-b33v",
+            "issued": "2021-05-21",
+            "keyword": [
+                "comet"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-C-5-DDR-PCC-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-c-5-ddr-pcc-v1.0_9cm8-b33v",
-            "description": "Physical characteristics of comets observed from -466 to 1975, compiled by S. K. Vsekhsvyatskii.",
-            "title": "PHYSICAL CHARACTERISTICS OF COMETS",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "PHYSICAL CHARACTERISTICS OF COMETS"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1432636975-GES_DISC.html",
             "citation": "Oxford University AOPP. 2017-10-31. SAMSN7L1RAD_CDROM. Version 001. SAMS/Nimbus-7 Level 1 Radiance Data from CD-ROM V001. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://disc.gsfc.nasa.gov/datacollection/SAMSN7L1RAD_CDROM_001.html. Digital Science Data.",
-            "issued": "1998-04-20",
-            "temporal": "1978-10-22T00:00:00Z/1984-04-16T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "1998-04-20",
-            "references": [
-                "https://doi.org/10.1098/rsta.1980.0166"
-            ],
-            "keyword": [
-                "spectral/engineering",
-                "infrared wavelengths",
-                "earth science",
-                "atmospheric temperature",
-                "atmosphere"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "JAMES JOHNSON",
                 "hasEmail": "mailto:James.Johnson@nasa.gov"
             },
+            "creator": "Oxford University AOPP",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C1432636975-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "SAMSN7L1RAD_CDROM is the gridded Nimbus-7 Stratospheric and Mesospheric Sounder (SAMS) Level 1 Radiance Data Product. The radiances were selected to derive gas concentrations at the wavelength bands 15 (CO2), 25-100 (H2O) 4-5 (CO and NO), and 7.7 (N2O and CH4) microns in the stratosphere and mesosphere, with a resolution of 100 km in the horizontal by 10 km in the vertical at the limb. This product contains radiances in a daily 2.5 degree latitude x 10 degree longitude grid format, gridded temperature profiles at 100, 30, 10, 3, 1, 0.3, 0.1, 0.03, 0.01 and 0.003 hPa, as well as the calibration, apriori and reformatted copies of the original tapes. The data for this product are available from 22 October 1978 through June 9 1983, with a few additional raw radiances to 16 April 1984. The principal investigators for the SAMS experiment were Prof. John T. Houghton and Dr. Fredric W. Taylor from Oxford University.\n\nThis product was created by the Oxford University's Atmospheric, Oceanic and Planetary Physics (AOPP) group. The data are stored on a set of 53 CD-ROMs in ASCII files of hexadecimal characters, and are available in gzipped Unix tar archive files. The first CD-ROM contains the a-priori temperature profile, monthly mean retrieved temperature profile, pre-launch calibration, housekeeping and instrument subsystem status files. CD-ROMs 2-5 contain the gridded temperature data. CD-ROMs 6-22 contain the radiances from the C-series and G-series tapes, and CD-ROMs 34-53 contain the raw radiance values from the R-series tape. The byte-ordering in the data files follows the DEC convention for 16-bit integers of less significant byte first. Normal 2's complement integer storage is assumed.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "SAMSN7L1RAD_CDROM",
-            "creator": "Oxford University AOPP",
-            "graphic-preview-description": "Nimbus-7 SAMS zonal mean temperature cross section for 6 November 1978.",
-            "title": "SAMS/Nimbus-7 Level 1 Radiance Data from CD-ROM V001 (SAMSN7L1RAD_CDROM) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Nimbus/images/N7SAMS_sample.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Nimbus/images/N7SAMS_sample.png",
-                    "description": "Nimbus-7 SAMS zonal mean temperature cross section for 6 November 1978.",
                     "@type": "dcat:Distribution",
+                    "description": "Nimbus-7 SAMS zonal mean temperature cross section for 6 November 1978.",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Nimbus/images/N7SAMS_sample.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/SAMSN7L1RAD_CDROM_001.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/SAMSN7L1RAD_CDROM_001.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/Nimbus7_SAMS_Level1/SAMSN7L1RAD_CDROM.001/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/Nimbus7_SAMS_Level1/SAMSN7L1RAD_CDROM.001/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=SAMSN7L1RAD_CDROM",
-                    "description": "Use the Earthdata Search Client to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search Client to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=SAMSN7L1RAD_CDROM",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/Nimbus7_SAMS_Level1/SAMSN7L1RAD_CDROM.001/doc/README.SAMSN7L1RAD_CDROM_001.txt",
-                    "description": "README Document",
                     "@type": "dcat:Distribution",
+                    "description": "README Document",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/Nimbus7_SAMS_Level1/SAMSN7L1RAD_CDROM.001/doc/README.SAMSN7L1RAD_CDROM_001.txt",
+                    "mediaType": "text/html",
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
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/repository/Mission/Nimbus/3.3_Product_Documentation/3.3.5_Product_Quality/N7_SAMS_DataUserGuide_19890016933.pdf",
-                    "description": "Nimbus 7 SAMS User's Guide",
                     "@type": "dcat:Distribution",
+                    "description": "Nimbus 7 SAMS User's Guide",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/repository/Mission/Nimbus/3.3_Product_Documentation/3.3.5_Product_Quality/N7_SAMS_DataUserGuide_19890016933.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
                 }
             ],
+            "graphic-preview-description": "Nimbus-7 SAMS zonal mean temperature cross section for 6 November 1978.",
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Nimbus/images/N7SAMS_sample.png",
+            "identifier": "C1432636975-GES_DISC",
+            "issued": "1998-04-20",
+            "keyword": [
+                "spectral/engineering",
+                "infrared wavelengths",
+                "earth science",
+                "atmospheric temperature",
+                "atmosphere"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1432636975-GES_DISC.html",
+            "language": [
+                "en-US"
+            ],
+            "modified": "1998-04-20",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
+            },
+            "references": [
+                "https://doi.org/10.1098/rsta.1980.0166"
+            ],
+            "release-place": "Greenbelt, MD, USA",
+            "series-name": "SAMSN7L1RAD_CDROM",
             "spatial": "-180.0 -50.0 180.0 67.5",
+            "temporal": "1978-10-22T00:00:00Z/1984-04-16T23:59:59.999Z",
             "theme": [
                 "Nimbus",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "SAMS/Nimbus-7 Level 1 Radiance Data from CD-ROM V001 (SAMSN7L1RAD_CDROM) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/VIIRS/VNP43D04.001",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Crystal Schaaf, Zhuosen Wang, Xiaoyang Zhang, Alan Strahler\r\n. 2019-11-07. VNP43D04. Version 001. VIIRS/NPP BRDF/Albedo Parameter 1 Band M2 Daily L3 Global 30 ArcSec CMG V001\r\n. Sioux Falls, South Dakota, USA. Archived by National Aeronautics and Space Administration, U.S. Government, NASA EOSDIS Land Processes Distributed Active Archive Center. https://doi.org/10.5067/VIIRS/VNP43D04.001. https://doi.org/10.5067/VIIRS/VNP43D04.001. Digital Science Data. The DOI landing page provides citations in APA and Chicago styles.\r\n.",
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
-            "identifier": "C1607315263-LPDAAC_ECS",
-            "description": "The NASA/NOAA Suomi National Polar-orbiting Partnership (Suomi NPP) Visible Infrared Imaging Radiometer Suite (VIIRS) Bidirectional Reflectance Distribution Function (BRDF) and Albedo Model Parameter 1 Band M2 product (VNP43D04) is produced daily using 16 days of data at 30 arc second (1,000 meter) resolution. Data are temporally weighted to the ninth day, which is reflected in the file name. The VNP43D product suite is provided in a Climate Modeling Grid (CMG), which covers the entire globe for use in climate simulation models. Due to the large file size, each VNP43D product contains just one data layer. Each of the three model parameters (isotropic, volumetric, and geometric) for each of the nine VIIRS moderate resolution bands along with the visible, near-infrared (NIR), and shortwave bands included in the VNP43MA1 (https://doi.org/10.5067/VIIRS/VNP43MA1.001) product is stored in a separate file as VNP43D01 through VNP43D36. In addition to the bands included in VNP43MA1, this product suite includes model parameters for the VIIRS Day/Night Band (DNB) as VNP43D37 through VNP43D39. Details regarding methodology are available on the VNP43MA1 product page and in the Algorithm Theoretical Basis Document (ATBD).\r\n\r\nVNP43D04 is the BRDF isotropic parameter for VIIRS band M2 (0.445 \u03bcm). The isotropic parameter, in conjunction with the volumetric and geometric parameters, is used to derive the BRDF/Albedo values for VIIRS band M2.",
-            "release-place": "Sioux Falls, South Dakota, USA",
-            "series-name": "VNP43D04",
             "creator": "Crystal Schaaf, Zhuosen Wang, Xiaoyang Zhang, Alan Strahler",
-            "title": "VIIRS/NPP BRDF/Albedo Parameter 1 Band M2 Daily L3 Global 30 ArcSec CMG V001",
-            "programCode": [
-                "026:001"
-            ],
+            "data-presentation-form": "Digital Science Data",
+            "description": "The NASA/NOAA Suomi National Polar-orbiting Partnership (Suomi NPP) Visible Infrared Imaging Radiometer Suite (VIIRS) Bidirectional Reflectance Distribution Function (BRDF) and Albedo Model Parameter 1 Band M2 product (VNP43D04) is produced daily using 16 days of data at 30 arc second (1,000 meter) resolution. Data are temporally weighted to the ninth day, which is reflected in the file name. The VNP43D product suite is provided in a Climate Modeling Grid (CMG), which covers the entire globe for use in climate simulation models. Due to the large file size, each VNP43D product contains just one data layer. Each of the three model parameters (isotropic, volumetric, and geometric) for each of the nine VIIRS moderate resolution bands along with the visible, near-infrared (NIR), and shortwave bands included in the VNP43MA1 (https://doi.org/10.5067/VIIRS/VNP43MA1.001) product is stored in a separate file as VNP43D01 through VNP43D36. In addition to the bands included in VNP43MA1, this product suite includes model parameters for the VIIRS Day/Night Band (DNB) as VNP43D37 through VNP43D39. Details regarding methodology are available on the VNP43MA1 product page and in the Algorithm Theoretical Basis Document (ATBD).\r\n\r\nVNP43D04 is the BRDF isotropic parameter for VIIRS band M2 (0.445 \u03bcm). The isotropic parameter, in conjunction with the volumetric and geometric parameters, is used to derive the BRDF/Albedo values for VIIRS band M2.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FVIIRS%2FVNP43D04.001",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FVIIRS%2FVNP43D04.001",
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
-                    "downloadURL": "https://doi.org/10.5067/VIIRS/VNP43D04.001",
-                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
+                    "downloadURL": "https://doi.org/10.5067/VIIRS/VNP43D04.001",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/xhdf5",
-                    "downloadURL": "https://e4ftl01.cr.usgs.gov/VIIRS/VNP43D04.001/",
-                    "description": "LP DAAC Data Pool provides direct access to available products via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "LP DAAC Data Pool provides direct access to available products via HTTPS.",
+                    "downloadURL": "https://e4ftl01.cr.usgs.gov/VIIRS/VNP43D04.001/",
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
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=C1607315263-LPDAAC_ECS",
-                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=C1607315263-LPDAAC_ECS",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://opendap.cr.usgs.gov/opendap/hyrax/VNP43D04.001/contents.html",
-                    "description": "Access data via Open-source Project for a Network Data Access Protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access data via Open-source Project for a Network Data Access Protocol.",
+                    "downloadURL": "https://opendap.cr.usgs.gov/opendap/hyrax/VNP43D04.001/contents.html",
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
-                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/filespec/VIIRS/1/VNP43D04",
-                    "description": "The File Specification provides a description of the product file including Scientific Data Sets and their attributes.",
                     "@type": "dcat:Distribution",
+                    "description": "The File Specification provides a description of the product file including Scientific Data Sets and their attributes.",
+                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/filespec/VIIRS/1/VNP43D04",
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
+            "identifier": "C1607315263-LPDAAC_ECS",
+            "issued": "2019-11-07",
+            "keyword": [
+                "surface radiative properties",
+                "earth science",
+                "land surface"
+            ],
+            "landingPage": "https://doi.org/10.5067/VIIRS/VNP43D04.001",
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
+            "series-name": "VNP43D04",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2012-01-19T00:00:00Z/2024-05-20T00:00:00Z",
             "theme": [
                 "NPP-JPSS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "VIIRS/NPP BRDF/Albedo Parameter 1 Band M2 Daily L3 Global 30 ArcSec CMG V001"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ASDC/SUBORBITAL/STRAT_Model_Data_1",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2023-11-20. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/ASDC/SUBORBITAL/STRAT_Model_Data_1.",
-            "issued": "1995-05-03",
-            "temporal": "1995-05-03T00:00:00Z/1996-02-16T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "1996-02-15",
-            "keyword": [
-                "earth science",
-                "atmospheric winds",
-                "atmosphere",
-                "atmospheric temperature"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Leslie Lait",
                 "hasEmail": "mailto:leslie.r.lait@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/LARC/SD/ASDC"
-            },
-            "identifier": "C2770047658-LARC_ASDC",
             "description": "STRAT_Model_Data is the model data collected during the Stratospheric Tracers of Atmospheric Transport (STRAT) campaign. Data collection for this product is complete.\r\n\r\nThe STRAT campaign was a field campaign conducted by NASA from May 1995 to February 1996. The primary goal of STRAT was to collect measurements of the change of long-lived tracers and functions of altitude, latitude, and season. These measurements were taken to aid with determining rates for global-scale transport and future distributions of high-speed civil transport (HSCT) exhaust that was emitted into the lower atmosphere. STRAT had four main objectives:  defining the rate of transport of trace gases from the stratosphere and troposphere (i.e., HSCT exhaust emissions), improving the understanding of dynamical coupling rates for transport of trace gases between tropical regions and higher latitudes and lower altitudes (between tropical regions, higher latitudes, and lower altitudes are where most ozone resides), improving understanding of chemistry in the upper troposphere and lower stratosphere, and finally, providing data sets for testing two-dimensional and three-dimensional models used in assessments of impacts from stratospheric aviation.  \r\n\r\nTo accomplish these objectives, the STRAT Science Team conducted various surface-based remote sensing and in-situ measurements. NASA flew the ER-2 aircraft along with balloons such as ozonesondes and radiosondes just below the tropopause in the Northern Hemisphere to collect data. Along with the ER-2 and balloons, NASA also utilized satellite imagery, theoretical models, and ground sites. The ER-2 collected data on HOx, NOy, CO2, ozone, water vapor, and temperature. The ER-2 also collected in-situ stratospheric measurements of N2O, CH4, CO, HCL, and NO using the Aircraft Laser Infrared Absorption Spectrometer (ALIAS). Ozonesondes and radiosondes were also deployed to collect data on CO2, NO/NOy, air temperature, pressure, and 3D wind. These balloons also took in-situ measurements of N2O, CFC-11, CH4, CO, HCL, and NO2 using the ALIAS. Ground stations were responsible for taking measurements of O3, ozone mixing ratio, pressure, and temperature. Satellites took infrared images of the atmosphere with the goal of aiding in completing STRAT objectives. Pressure and temperature models were created to help plan the mission.",
-            "title": "STRAT Model Data",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC%2FSUBORBITAL%2FSTRAT_Model_Data_1",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC%2FSUBORBITAL%2FSTRAT_Model_Data_1",
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
                     "title": "The dataset's home page"
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
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2770047658-LARC_ASDC",
-                    "description": "Earthdata Search for STRAT_Model_Data_1",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for STRAT_Model_Data_1",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2770047658-LARC_ASDC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/ASDC/SUBORBITAL/STRAT_Model_Data_1",
-                    "description": "DOI for STRAT_Model_Data_1",
                     "@type": "dcat:Distribution",
+                    "description": "DOI for STRAT_Model_Data_1",
+                    "downloadURL": "https://doi.org/10.5067/ASDC/SUBORBITAL/STRAT_Model_Data_1",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/STRAT/Model_Data_1/",
-                    "description": "ASDC Direct Data Download for STRAT_Model_Data_1",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for STRAT_Model_Data_1",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/STRAT/Model_Data_1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 }
             ],
+            "identifier": "C2770047658-LARC_ASDC",
+            "issued": "1995-05-03",
+            "keyword": [
+                "earth science",
+                "atmospheric winds",
+                "atmosphere",
+                "atmospheric temperature"
+            ],
+            "landingPage": "https://doi.org/10.5067/ASDC/SUBORBITAL/STRAT_Model_Data_1",
+            "language": [
+                "en-US"
+            ],
+            "modified": "1996-02-15",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/LARC/SD/ASDC"
+            },
             "spatial": "<?xml version=\"1.0\" encoding=\"UTF-8\"?><gml:Polygon xmlns:gml=\"http://www.opengis.net/gml/3.2\" srsName=\"EPSG:9825\"><gml:outerBoundaryIs><gml:LinearRing><gml:posList>-2.14 -180.0 -2.14 180.0 68.23 180.0 68.23 -180.0 -2.14 -180.0</gml:posList></gml:LinearRing></gml:outerBoundaryIs><gml:innerBoundaryIs></gml:innerBoundaryIs></gml:Polygon>",
+            "temporal": "1995-05-03T00:00:00Z/1996-02-16T00:00:00Z",
             "theme": [
                 "STRAT",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "STRAT Model Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC2-0654-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 2 phase 2015-03-11 to 2015-06-30. It is a Global Gravity measurement at the comet 67P and covers the time 2015-03-18T01:58:35.000 to 2015-03-18T09:09:03.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc2-0654-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC2-0654-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc2-0654-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 2 phase 2015-03-11 to 2015-06-30. It is a Global Gravity measurement at the comet 67P and covers the time 2015-03-18T01:58:35.000 to 2015-03-18T09:09:03.000.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 2 0654 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 2 0654 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO%2FRL-C-CONSERT-3-SDL-V1.1",
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
+            "description": "This archive contains CALIBRATED data (CODMAC level 3) that refers to target 67P/CHURYUMOV-GERASIMENKO 1 (1969 R1) from the CONSERT instrument onboard ROSETTA Orbiter and Lander, acquired during the SDL phase. In addition to the scientific signal of interest, it contains all the values applied to the signal for calibration. It also contains documentation which describes the CONSERT experiment. The data archived in this data set conform to the Planetary Data System (PDS) Standards, Version 3.6. V1.1 of this dataset includes corrections on the data and label files (add missing keywords, correct files name into .txt files, add missing inteference parameters for FSS_RANGING).",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-rl-c-consert-3-sdl-v1.1",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO%2FRL-C-CONSERT-3-SDL-V1.1",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-rl-c-consert-3-sdl-v1.1",
-            "description": "This archive contains CALIBRATED data (CODMAC level 3) that refers to target 67P/CHURYUMOV-GERASIMENKO 1 (1969 R1) from the CONSERT instrument onboard ROSETTA Orbiter and Lander, acquired during the SDL phase. In addition to the scientific signal of interest, it contains all the values applied to the signal for calibration. It also contains documentation which describes the CONSERT experiment. The data archived in this data set conform to the Planetary Data System (PDS) Standards, Version 3.6. V1.1 of this dataset includes corrections on the data and label files (add missing keywords, correct files name into .txt files, add missing inteference parameters for FSS_RANGING).",
-            "title": "ROSETTA-ORBITER/ROSETTA-LANDER 67P CONSERT 3 SDL V1.1",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER/ROSETTA-LANDER 67P CONSERT 3 SDL V1.1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/310",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Anderson, Darwin. 1999. BOREAS TE-01 CH4 Flux Data over the SSA-OA. ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/310",
-            "issued": "2023-11-22",
-            "temporal": "1994-05-29T00:00:00Z/1994-09-17T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-11-27",
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
-            "identifier": "C2807648526-ORNL_CLOUD",
             "description": "Contains the TE-01 CH4 flux data for the southern study area old aspen site.",
-            "graphic-preview-description": "Browse Image",
-            "title": "BOREAS TE-01 CH4 Flux Data over the SSA-OA",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/boreas_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F310",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F310",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/boreas/TE/te1ch4fx/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/boreas/TE/te1ch4fx/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/BOREAS/guides/TE01_CH4_FLUX.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/BOREAS/guides/TE01_CH4_FLUX.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/310",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/310",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/msword",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TE/te1ch4fx/comp/TE01_CH4_FLUX.doc",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TE/te1ch4fx/comp/TE01_CH4_FLUX.doc",
+                    "mediaType": "application/msword",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TE/te1ch4fx/comp/TE01_CH4_FLUX.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TE/te1ch4fx/comp/TE01_CH4_FLUX.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TE/te1ch4fx/comp/TE01_CH4_FLUX.txt",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TE/te1ch4fx/comp/TE01_CH4_FLUX.txt",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TE/te1ch4fx/comp/te1ch4fx.def",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TE/te1ch4fx/comp/te1ch4fx.def",
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
+            "identifier": "C2807648526-ORNL_CLOUD",
+            "issued": "2023-11-22",
+            "keyword": [
+                "earth science",
+                "land surface",
+                "soils"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/310",
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
             "spatial": "53.63 -106.2",
+            "temporal": "1994-05-29T00:00:00Z/1994-09-17T23:59:59Z",
             "theme": [
                 "BOREAS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "BOREAS TE-01 CH4 Flux Data over the SSA-OA"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ADEOS-I/OCTS/L3B/PAR/2014",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/GSFC/SED/ESD/GCDC/OB.DAAC. https://doi.org/10.5067/ADEOS-I/OCTS/L3B/PAR/2014.",
-            "issued": "2017-01-11",
-            "temporal": "1996-11-01T00:00:00Z/1997-06-30T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2018-10-10",
-            "keyword": [
-                "oceans",
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
-            "identifier": "C1200034341-OB_DAAC",
             "description": "On August 17, 1996, the Japanese Space Agency (NASDA - National Space Development Agency)\nlaunched the Advanced Earth Observing Satellite (ADEOS). ADEOS was in a descending, Sun\nsynchronous orbit with a nominal equatorial crossing time of 10:30 a.m. Amoung the\ninstruments carried aboard the ADEOS spacecraft was the Ocean Color and Temperature\nScanner (OCTS). OCTS is an optical radiometer with 12 bands covering the visible, near\ninfrared and thermal infrared regions. (Eight of the bands are in the VIS/NIR. These are\nthe only bands calibrated and processed by the OBPG) OCTS has a swath width of\napproximately 1400 km, and a nominal nadir resolution of 700 m. The instrument operated\nat three tilt states (20 degrees aft, nadir and 20 degrees fore), similar to SeaWiFS.",
-            "title": "ADEOS-I Ocean Color and Temperature Scanner (OCTS) Photosynthetically Available Radiation (PAR) Global Binned Data",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FADEOS-I%2FOCTS%2FL3B%2FPAR%2F2014",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FADEOS-I%2FOCTS%2FL3B%2FPAR%2F2014",
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
-                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/atbd/par",
-                    "description": "NASA Ocean Color Web - Algorithm Descriptions",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Ocean Color Web - Algorithm Descriptions",
+                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/atbd/par",
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
-                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/data/10.5067/ADEOS-I/OCTS/L3B/PAR/2014",
-                    "description": "OB.DAAC OCTS ADEOS-I L3B Photosynthetically Available Radiation (PAR) Landing Page",
                     "@type": "dcat:Distribution",
+                    "description": "OB.DAAC OCTS ADEOS-I L3B Photosynthetically Available Radiation (PAR) Landing Page",
+                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/data/10.5067/ADEOS-I/OCTS/L3B/PAR/2014",
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
+            "identifier": "C1200034341-OB_DAAC",
+            "issued": "2017-01-11",
+            "keyword": [
+                "oceans",
+                "earth science",
+                "ocean optics"
+            ],
+            "landingPage": "https://doi.org/10.5067/ADEOS-I/OCTS/L3B/PAR/2014",
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
+            "title": "ADEOS-I Ocean Color and Temperature Scanner (OCTS) Photosynthetically Available Radiation (PAR) Global Binned Data"
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
-            "identifier": "NASA-862__39",
             "description": "Academy of Program/Project & Engineering Leadership's Ask the Academy magazine past issues.",
-            "title": "Academy of Program/Project & Engineering Leadership ASK the Academy Past Issues",
-            "programCode": [
-                "026:045"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -416147,297 +416126,332 @@
                     "mediaType": "application/html"
                 }
             ],
-            "accrualPeriodicity": "R/P1M",
+            "identifier": "NASA-862__39",
+            "issued": "2018-06-25",
+            "keyword": [
+                "knowledge",
+                "ask the academy",
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
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-4-ESC3-67P-M20-STR-REFL-V1.0",
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
+            "description": "This CODMAC level 4 data set contains solar stray light corrected, radiometric calibrated and geometric distortion corrected (resampled) image data in in reflectance units (normalized and thus without unit), acquired by the OSIRIS Narrow Angle Camera on the Rosetta spacecraft during the COMET ESCORT 3 mission phase, covering the period from 2015-08-25T23:25:00.000 to 2015-09-22T23:24:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V1.0 is the first version of this dataset: Lien corrected dataset after October 2018 PSA/PDS external peer review.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-4-esc3-67p-m20-str-refl-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-4-ESC3-67P-M20-STR-REFL-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-4-esc3-67p-m20-str-refl-v1.0",
-            "description": "This CODMAC level 4 data set contains solar stray light corrected, radiometric calibrated and geometric distortion corrected (resampled) image data in in reflectance units (normalized and thus without unit), acquired by the OSIRIS Narrow Angle Camera on the Rosetta spacecraft during the COMET ESCORT 3 mission phase, covering the period from 2015-08-25T23:25:00.000 to 2015-09-22T23:24:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V1.0 is the first version of this dataset: Lien corrected dataset after October 2018 PSA/PDS external peer review.",
-            "title": "ROSETTA-ORBITER 67P OSINAC 4 ESC3-MTP020 RDR-STR-REFL V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P OSINAC 4 ESC3-MTP020 RDR-STR-REFL V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/609",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Betts, A.K., S.R. Shewchuk, H. Osborne, K. Young, and V. Wittrock. 2001. BOREAS Follow-On HMet-04 1996-1998 NSA Meteorological Data. ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/609",
-            "issued": "2024-04-27",
-            "temporal": "1994-01-01T00:00:00Z/1999-01-01T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-04-28",
-            "keyword": [
-                "atmospheric temperature",
-                "soils",
-                "biosphere",
-                "snow/ice",
-                "atmospheric water vapor",
-                "surface thermal properties",
-                "atmospheric winds",
-                "terrestrial hydrosphere",
-                "earth science",
-                "land surface",
-                "vegetation",
-                "precipitation",
-                "atmospheric radiation",
-                "atmosphere",
-                "atmospheric pressure"
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
-            "identifier": "C2956536978-ORNL_CLOUD",
             "description": "As part of the BOREAS Follow-on, an extended period of data collection was supported in the NSA because of the continued efforts at the NSA-OBS site.  This data set contains near-surface meteorological data collected and averaged over 15 minute intervals from two sites in the NSA, the SRC tower at the Thompson airport (YTH) and a temporary walkup wooden tower at the Old Black Spruce (OBS) tower site.",
-            "graphic-preview-description": "Browse Image",
-            "title": "BOREAS Follow-On HMet-04 1996-1998 NSA Meteorological Data",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/boreas_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F609",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F609",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/boreas/HMET/BFO_hmet04_src_nsa_96-98/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/boreas/HMET/BFO_hmet04_src_nsa_96-98/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/BOREAS/FollowOn/guides/hmet04_src_nsa_met_doc.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/BOREAS/FollowOn/guides/hmet04_src_nsa_met_doc.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/609",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/609",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/HMET/BFO_hmet04_src_nsa_96-98/comp/0_readme.txt",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/HMET/BFO_hmet04_src_nsa_96-98/comp/0_readme.txt",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/HMET/BFO_hmet04_src_nsa_96-98/comp/0_site_list.txt",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/HMET/BFO_hmet04_src_nsa_96-98/comp/0_site_list.txt",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/HMET/BFO_hmet04_src_nsa_96-98/comp/hmet04_src_nsa_met_doc.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/HMET/BFO_hmet04_src_nsa_96-98/comp/hmet04_src_nsa_met_doc.pdf",
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
+            "identifier": "C2956536978-ORNL_CLOUD",
+            "issued": "2024-04-27",
+            "keyword": [
+                "atmospheric temperature",
+                "soils",
+                "biosphere",
+                "snow/ice",
+                "atmospheric water vapor",
+                "surface thermal properties",
+                "atmospheric winds",
+                "terrestrial hydrosphere",
+                "earth science",
+                "land surface",
+                "vegetation",
+                "precipitation",
+                "atmospheric radiation",
+                "atmosphere",
+                "atmospheric pressure"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/609",
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
             "spatial": "-111.0 48.0 -90.0 60.0",
+            "temporal": "1994-01-01T00:00:00Z/1999-01-01T23:59:59Z",
             "theme": [
                 "BOREAS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "BOREAS Follow-On HMet-04 1996-1998 NSA Meteorological Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/Aqua/AIRS/DATA304",
             "citation": "AIRS Science Team/Joao Teixeira. 2013-03-12. AIRX3SPD. Version 006. AIRS/Aqua L3 Daily Support Product (AIRS+AMSU) 1 degree x 1 degree V006. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/Aqua/AIRS/DATA304. https://disc.gsfc.nasa.gov/datacollection/AIRX3SPD_006.html. Digital Science Data.",
-            "issued": "2002-08-31",
-            "temporal": "2002-08-31T00:00:00Z/2016-09-25T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2016-09-25",
-            "references": [
-                "https://doi.org/10.1117/1.JRS.8.084994",
-                "https://doi.org/10.5194/acp-14-399-2014"
-            ],
-            "keyword": [
-                "surface thermal properties",
-                "ocean temperature",
-                "earth science",
-                "precipitation",
-                "oceans",
-                "clouds",
-                "atmospheric water vapor",
-                "atmospheric temperature",
-                "air quality",
-                "altitude",
-                "atmosphere",
-                "atmospheric radiation",
-                "atmospheric chemistry",
-                "land surface",
-                "atmospheric pressure",
-                "surface radiative properties"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "ED ESFANDIARI",
                 "hasEmail": "mailto:asghar.e.esfandiari@nasa.gov"
             },
+            "creator": "AIRS Science Team/Joao Teixeira",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C1238517317-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "The Atmospheric Infrared Sounder (AIRS) is a grating spectrometer (R = 1200) aboard the second Earth Observing System (EOS) polar-orbiting platform, EOS Aqua. In combination with the Advanced Microwave Sounding Unit (AMSU) and the Humidity Sounder for Brazil (HSB), AIRS constitutes an innovative atmospheric sounding group of visible, infrared, and microwave sensors. The L3 support products are similar to the L3 standard products but contain fields which are not fully validated, or are inputs or intermediary values. Because no quality control information is available for some of these fields, values from failed retrievals may be included.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "AIRX3SPD",
-            "creator": "AIRS Science Team/Joao Teixeira",
-            "graphic-preview-description": "Sample data of the \"AIRS/Aqua Level 3 daily standard physical retrieval product (Without HSB)\".",
-            "title": "AIRS/Aqua L3 Daily Support Product (AIRS+AMSU) 1 degree x 1 degree V006 (AIRX3SPD) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/AIRX3SPD_006.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAqua%2FAIRS%2FDATA304",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAqua%2FAIRS%2FDATA304",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/AIRX3SPD_006.png",
-                    "description": "Sample data of the \"AIRS/Aqua Level 3 daily standard physical retrieval product (Without HSB)\".",
                     "@type": "dcat:Distribution",
+                    "description": "Sample data of the \"AIRS/Aqua Level 3 daily standard physical retrieval product (Without HSB)\".",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/AIRX3SPD_006.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/AIRX3SPD_006.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/AIRX3SPD_006.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/Aqua_AIRS_Level3/AIRX3SPD.006/",
-                    "description": "Access the data via HTTP.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTP.",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/Aqua_AIRS_Level3/AIRX3SPD.006/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/opendap/Aqua_AIRS_Level3/AIRX3SPD.006/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
-                    "title": "Use OPeNDAP to access the dataset's data"
-                },
-                {
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/opendap/Aqua_AIRS_Level3/AIRX3SPD.006/contents.html",
                     "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=AIRX3SPD+006",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "title": "Use OPeNDAP to access the dataset's data"
+                },
+                {
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=AIRX3SPD+006",
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
+            "graphic-preview-description": "Sample data of the \"AIRS/Aqua Level 3 daily standard physical retrieval product (Without HSB)\".",
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/AIRX3SPD_006.png",
+            "identifier": "C1238517317-GES_DISC",
+            "issued": "2002-08-31",
+            "keyword": [
+                "surface thermal properties",
+                "ocean temperature",
+                "earth science",
+                "precipitation",
+                "oceans",
+                "clouds",
+                "atmospheric water vapor",
+                "atmospheric temperature",
+                "air quality",
+                "altitude",
+                "atmosphere",
+                "atmospheric radiation",
+                "atmospheric chemistry",
+                "land surface",
+                "atmospheric pressure",
+                "surface radiative properties"
+            ],
+            "landingPage": "https://doi.org/10.5067/Aqua/AIRS/DATA304",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2016-09-25",
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
+            "series-name": "AIRX3SPD",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2002-08-31T00:00:00Z/2016-09-25T23:59:59.999Z",
             "theme": [
                 "Aqua",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "AIRS/Aqua L3 Daily Support Product (AIRS+AMSU) 1 degree x 1 degree V006 (AIRX3SPD) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.nasa.gov/d/9d67-y8yu",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "GeneLab Outreach",
+                "hasEmail": "mailto:genelab-outreach@lists.nasa.gov"
+            },
+            "description": "We report how high and low linear energy transfer (LET) radiation microgravity and elevated dietary iron affect colon microbiota (determined by 16S rDNA pyrosequencing) and colon function. Three independent experiments were conducted: 1) fractionated low LET gamma radiation (137Cs 3 Gy RAD) high Fe diet (IRON) (650 mg/kg diet) and a combination of low LET gamma radiation and high Fe diet (IRON+RAD) in male Sprague-Dawley rats; 2) high LET 38Si particle exposure (0.050 Gy) 1/6 G partial weight bearing (PWB) and a combination of high LET38Si particle exposure and PWB in female BalbC/ByJ mice; and 3) 13 d spaceflight in female C57BL/6 mice. For each experiment the colon was resected and feces removed for microbial sequencing analysis on a Roche 454 Genome Sequencer FLX Titanium instrument (Microbiome Core Facility Chapel Hill NC) using the GS FLX Titanium XLR70 sequencing reagents and protocols. Analysis of amplicon sequencing data was carried out using the QIIME pipeline. Low LET radiation high iron diet and spaceflight increased Bacteroidetes and decreased Firmicutes. Low LET radiation high Fe diet and spaceflight did not significantly affect diversity or richness or elevate pathogenic genera. Spaceflight increased Clostridiales and decreased Lactobacillales and similar trends were observed in the experiment using a ground-based model of microgravity suggesting altered gravity may affect colonic microbiota. Microbiota characteriztion in these models is a first step in understanding the impact of the space environment on intestinal health.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "GeneLab Study Page",
+                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-72",
+                    "mediaType": "text/html",
+                    "title": "Space environmental factor impacts upon murine colon microbiota and mucosal homeostasis"
+                }
+            ],
+            "identifier": "nasa_genelab_GLDS-72_9d67-y8yu",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
             "keyword": [
                 "diet",
                 "radiation",
@@ -416450,65 +416464,34 @@
                 "sequence assembly",
                 "sample collection"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "GeneLab Outreach",
-                "hasEmail": "mailto:genelab-outreach@lists.nasa.gov"
-            },
+            "landingPage": "https://data.nasa.gov/d/9d67-y8yu",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "nasa_genelab_GLDS-72_9d67-y8yu",
-            "description": "We report how high and low linear energy transfer (LET) radiation microgravity and elevated dietary iron affect colon microbiota (determined by 16S rDNA pyrosequencing) and colon function. Three independent experiments were conducted: 1) fractionated low LET gamma radiation (137Cs 3 Gy RAD) high Fe diet (IRON) (650 mg/kg diet) and a combination of low LET gamma radiation and high Fe diet (IRON+RAD) in male Sprague-Dawley rats; 2) high LET 38Si particle exposure (0.050 Gy) 1/6 G partial weight bearing (PWB) and a combination of high LET38Si particle exposure and PWB in female BalbC/ByJ mice; and 3) 13 d spaceflight in female C57BL/6 mice. For each experiment the colon was resected and feces removed for microbial sequencing analysis on a Roche 454 Genome Sequencer FLX Titanium instrument (Microbiome Core Facility Chapel Hill NC) using the GS FLX Titanium XLR70 sequencing reagents and protocols. Analysis of amplicon sequencing data was carried out using the QIIME pipeline. Low LET radiation high iron diet and spaceflight increased Bacteroidetes and decreased Firmicutes. Low LET radiation high Fe diet and spaceflight did not significantly affect diversity or richness or elevate pathogenic genera. Spaceflight increased Clostridiales and decreased Lactobacillales and similar trends were observed in the experiment using a ground-based model of microgravity suggesting altered gravity may affect colonic microbiota. Microbiota characteriztion in these models is a first step in understanding the impact of the space environment on intestinal health.",
-            "title": "Space environmental factor impacts upon murine colon microbiota and mucosal homeostasis",
-            "programCode": [
-                "026:005"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-72",
-                    "description": "GeneLab Study Page",
-                    "@type": "dcat:Distribution",
-                    "title": "Space environmental factor impacts upon murine colon microbiota and mucosal homeostasis"
-                }
-            ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "Space environmental factor impacts upon murine colon microbiota and mucosal homeostasis"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1000000019-CDDIS.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/GSFC/SED/ESD/GGL/CDDIS.",
-            "issued": "1982-01-01",
-            "temporal": "1969-01-01T00:00:00Z/2022-01-17T00:00:00Z",
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
-            "identifier": "C1000000019-CDDIS",
             "description": "Lunar Laser Ranging (LLR) measures the distance between the Earth and the Moon using laser ranging. A short pulse of coherent light generated by a laser (Light Amplification by Stimulated Emission of Radiation) is transmitted in a narrow beam to illuminate corner cube retroreflectors on the moon. The return signal, typically a few photons, is collected by a telescope and the time-of-flight is measured. Apollo astronauts and Russian rovers deployed laser ranging retroreflector arrays on the lunar surface which continue to yield fundamental scientific data. Analysis of Lunar Laser Ranging (LLR) data provides information on the lunar orbit, rotation, solid-body tides, and retroreflector locations.",
-            "title": "CDDIS_LLR_data",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -416517,1376 +416500,1365 @@
                     "title": "Download this dataset"
                 }
             ],
+            "identifier": "C1000000019-CDDIS",
+            "issued": "1982-01-01",
+            "keyword": [
+                "nasa"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1000000019-CDDIS.html",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2012-06-14",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GGL/CDDIS"
+            },
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "1969-01-01T00:00:00Z/2022-01-17T00:00:00Z",
             "theme": [
                 "ILRS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "CDDIS_LLR_data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=GO-E-MAG-4-SUMM-EARTH1-SUMMARY-V1.0",
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
-                "galileo",
-                "earth"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "Galileo Orbiter Magnetometer (MAG) calibrated 20 second averaged data from the Earth-1 flyby in spacecraft, GSE, and GSM coordinates. These data cover the interval 1990-11-05 to 1990-12-31.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.go-e-mag-4-summ-earth1-summary-v1.0_9d7k-5syf",
+            "issued": "2021-05-21",
+            "keyword": [
+                "galileo",
+                "earth"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=GO-E-MAG-4-SUMM-EARTH1-SUMMARY-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.go-e-mag-4-summ-earth1-summary-v1.0_9d7k-5syf",
-            "description": "Galileo Orbiter Magnetometer (MAG) calibrated 20 second averaged data from the Earth-1 flyby in spacecraft, GSE, and GSM coordinates. These data cover the interval 1990-11-05 to 1990-12-31.",
-            "title": "GALILEO ORBITER EARTH MAG SUMM EARTH1 SUMMARY V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "GALILEO ORBITER EARTH MAG SUMM EARTH1 SUMMARY V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ASDC/SUBORBITAL/DISCOVERAQ_Colorado_MetNav_AircraftInSitu_B200_Data_1",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2022-08-29. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/ASDC/SUBORBITAL/DISCOVERAQ_Colorado_MetNav_AircraftInSitu_B200_Data_1.",
-            "issued": "2021-08-20",
-            "temporal": "2014-07-06T00:00:00Z/2014-08-14T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-08-29",
-            "keyword": [
-                "altitude",
-                "earth science",
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
-            "identifier": "C2430068044-LARC_ASDC",
             "description": "DISCOVERAQ_Colorado_MetNav_AircraftInSitu_B200_Data contains in situ meteorological and navigational data collected onboard NASA's B-200 aircraft during the Colorado (Denver) deployment of NASA's DISCOVER-AQ field study. This product contains the B-200 navigational data collected via the APPLANIX. This data product contains data for only the Colorado deployment and data collection is complete.\r\n\r\nUnderstanding the factors that contribute to near surface pollution is difficult using only satellite-based observations. The incorporation of surface-level measurements from aircraft and ground-based platforms provides the crucial information necessary to validate and expand upon the use of satellites in understanding near surface pollution. Deriving Information on Surface conditions from Column and Vertically Resolved Observations Relevant to Air Quality (DISCOVER-AQ) was a four-year campaign conducted in collaboration between NASA Langley Research Center, NASA Goddard Space Flight Center, NASA Ames Research Center, and multiple universities to improve the use of satellites to monitor air quality for public health and environmental benefit. Through targeted airborne and ground-based observations, DISCOVER-AQ enabled more effective use of current and future satellites to diagnose ground level conditions influencing air quality.\r\n\r\nDISCOVER-AQ employed two NASA aircraft, the P-3B and King Air, with the P-3B completing in-situ spiral profiling of the atmosphere (aerosol properties, meteorological variables, and trace gas species). The King Air conducted both passive and active remote sensing of the atmospheric column extending below the aircraft to the surface. Data from an existing network of surface air quality monitors, AERONET sun photometers, Pandora UV/vis spectrometers and model simulations were also collected. Further, DISCOVER-AQ employed many surface monitoring sites, with measurements being made on the ground, in conjunction with the aircraft. The B200 and P-3B conducted flights in Baltimore-Washington, D.C. in 2011, Houston, TX in 2013, San Joaquin Valley, CA in 2013, and Denver, CO in 2014. These regions were targeted due to being in violation of the National Ambient Air Quality Standards (NAAQS).\r\n\r\nThe first objective of DISCOVER-AQ was to determine and investigate correlations between surface measurements and satellite column observations for the trace gases ozone (O3), nitrogen dioxide (NO2), and formaldehyde (CH2O) to understand how satellite column observations can diagnose surface conditions. DISCOVER-AQ also had the objective of using surface-level measurements to understand how satellites measure diurnal variability and to understand what factors control diurnal variability. Lastly, DISCOVER-AQ aimed to explore horizontal scales of variability, such as regions with steep gradients and urban plumes.",
-            "title": "DISCOVER-AQ Colorado Deployment B-200 Aircraft In Situ Meteorological and Navigational Data",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC%2FSUBORBITAL%2FDISCOVERAQ_Colorado_MetNav_AircraftInSitu_B200_Data_1",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC%2FSUBORBITAL%2FDISCOVERAQ_Colorado_MetNav_AircraftInSitu_B200_Data_1",
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
-                    "downloadURL": "https://doi.org/10.5067/ASDC/SUBORBITAL/DISCOVERAQ_Colorado_MetNav_AircraftInSitu_B200_Data_1",
-                    "description": "DOI for DISCOVERAQ_Colorado_MetNav_AircraftInSitu_B200_Data_1",
                     "@type": "dcat:Distribution",
+                    "description": "DOI for DISCOVERAQ_Colorado_MetNav_AircraftInSitu_B200_Data_1",
+                    "downloadURL": "https://doi.org/10.5067/ASDC/SUBORBITAL/DISCOVERAQ_Colorado_MetNav_AircraftInSitu_B200_Data_1",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2430068044-LARC_ASDC",
-                    "description": "Earthdata search client for DISCOVERAQ_Colorado_MetNav_AircraftInSitu_B200_Data_1",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata search client for DISCOVERAQ_Colorado_MetNav_AircraftInSitu_B200_Data_1",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2430068044-LARC_ASDC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/DISCOVER-AQ/Colorado_MetNav_AircraftInSitu_B200_Data_1/",
-                    "description": "ASDC Direct Data Download for DISCOVERAQ_Colorado_MetNav_AircraftInSitu_B200_Data_1",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for DISCOVERAQ_Colorado_MetNav_AircraftInSitu_B200_Data_1",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/DISCOVER-AQ/Colorado_MetNav_AircraftInSitu_B200_Data_1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 }
             ],
+            "identifier": "C2430068044-LARC_ASDC",
+            "issued": "2021-08-20",
+            "keyword": [
+                "altitude",
+                "earth science",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.5067/ASDC/SUBORBITAL/DISCOVERAQ_Colorado_MetNav_AircraftInSitu_B200_Data_1",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2022-08-29",
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
+            "title": "DISCOVER-AQ Colorado Deployment B-200 Aircraft In Situ Meteorological and Navigational Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.7265/N53N21BT",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Sea-ice Thickness and Draft Statistics from Submarine ULS, Moored ULS, and a Coupled Model, Version 1. Version 1. Archived by National Aeronautics and Space Administration, U.S. Government, National Snow and Ice Data Center. https://doi.org/10.7265/N53N21BT.",
-            "issued": "1979-01-01",
-            "temporal": "1979-01-01T00:00:00Z/2004-12-31T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2004-12-31",
-            "keyword": [
-                "earth science",
-                "cryosphere",
-                "sea ice"
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
-            "identifier": "C1386246283-NSIDCV0",
             "description": "This data set consists of estimates of mean values of sea-ice thickness and sea-ice draft in meters computed from three different input data sets: sea ice draft from Upward Looking Sonar (ULS) mounted on submarines, sea ice draft from ULS mounted on bottom-anchored moorings, and a simulated ice-thickness model. The data span from 1979 to 2004 and cover two regions centered around the North Pole.",
-            "title": "Sea-ice Thickness and Draft Statistics from Submarine ULS, Moored ULS, and a Coupled Model, Version 1",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.7265%2FN53N21BT",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.7265%2FN53N21BT",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/forms/G02194_or.html?major_version=1",
-                    "description": "Direct download, with optional registration page.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download, with optional registration page.",
+                    "downloadURL": "https://nsidc.org/forms/G02194_or.html?major_version=1",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.7265/N53N21BT",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.7265/N53N21BT",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.7265/N53N21BT",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.7265/N53N21BT",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C1386246283-NSIDCV0",
+            "issued": "1979-01-01",
+            "keyword": [
+                "earth science",
+                "cryosphere",
+                "sea ice"
+            ],
+            "landingPage": "https://doi.org/10.7265/N53N21BT",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2004-12-31",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NSIDC"
+            },
             "spatial": "-180.0 87.0 180.0 90.0",
+            "temporal": "1979-01-01T00:00:00Z/2004-12-31T23:59:59.999Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Sea-ice Thickness and Draft Statistics from Submarine ULS, Moored ULS, and a Coupled Model, Version 1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/CHQTHBBT42QL",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Nimbus Temperature-Humidity Infrared Radiometer 11.5 \u00b5m Grayscale Swath Data L1, TIFF V001. Version 1. Archived by National Aeronautics and Space Administration, U.S. Government, NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/CHQTHBBT42QL.",
-            "issued": "1970-04-08",
-            "temporal": "1970-04-08T00:00:00Z/1975-11-11T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "1975-11-11",
-            "keyword": [
-                "earth science",
-                "infrared wavelengths",
-                "spectral/engineering"
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
-            "identifier": "C1703456255-NSIDC_ECS",
             "description": "This data set consists of daily, global grayscale TIFF images derived from radiative temperatures measured in the 11.5 \u00b5m window (10.5 \u00b5m - 12.5 \u00b5m). These data were detected by the Temperature-Humidity Infrared Radiometer (THIR) on board the Nimbus 4, Nimbus 5, and Nimbus 6 satellites, respectively, during 1970-1971, 1973-1975 and 1975. The Nimbus satellites used the THIR 11.5 \u00b5m window to measure cloud top or surface temperatures. Note: This data set is not georeferenced and contains some gaps in temporal coverage because of missing data.",
-            "title": "Nimbus Temperature-Humidity Infrared Radiometer 11.5 \u00b5m Grayscale Swath Data L1, TIFF V001",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FCHQTHBBT42QL",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FCHQTHBBT42QL",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/NIMBUS/NmTHIR115-1T.001/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/NIMBUS/NmTHIR115-1T.001/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1703456255-NSIDC_ECS&q=NmTHIR115-1T&m=-58.10675108287023%21-1.6864013671875%211%211%210%210%2C2&tl=1568750791%214%21%21",
-                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1703456255-NSIDC_ECS&q=NmTHIR115-1T&m=-58.10675108287023%21-1.6864013671875%211%211%210%210%2C2&tl=1568750791%214%21%21",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/data/data-access-tool/NmTHIR115-1T/versions/1/",
-                    "description": "Data Access link for ITSD project",
                     "@type": "dcat:Distribution",
+                    "description": "Data Access link for ITSD project",
+                    "downloadURL": "https://nsidc.org/data/data-access-tool/NmTHIR115-1T/versions/1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/CHQTHBBT42QL",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/CHQTHBBT42QL",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/CHQTHBBT42QL",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/CHQTHBBT42QL",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C1703456255-NSIDC_ECS",
+            "issued": "1970-04-08",
+            "keyword": [
+                "earth science",
+                "infrared wavelengths",
+                "spectral/engineering"
+            ],
+            "landingPage": "https://doi.org/10.5067/CHQTHBBT42QL",
+            "language": [
+                "en-US"
+            ],
+            "modified": "1975-11-11",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NSIDC"
+            },
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "1970-04-08T00:00:00Z/1975-11-11T23:59:59.999Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Nimbus Temperature-Humidity Infrared Radiometer 11.5 \u00b5m Grayscale Swath Data L1, TIFF V001"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C156141689-LARC.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "The data used in this study were produced by the MISR Science Team;processed/stored at the Langley DAAC;Product is the MISR Level 3 FIRSTLOOK Component Global Aerosol Product covering a month's products;See ProductionDateTime for Published date.",
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
-            "identifier": "C156141689-LARC",
             "description": "This file contains the MISR Level 3 FIRSTLOOK Component Global Aerosol Product covering a month",
-            "graphic-preview-description": "ASDC List of MISR Imagery and Articles",
-            "title": "MISR Level 3 FIRSTLOOK Component Global Aerosol Product covering a month V002",
-            "graphic-preview-file": "https://asdc.larc.nasa.gov/documents/misr/imagery.html",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/search/concepts/C156141689-LARC.html",
-                    "description": "View this dataset on the CMR (Common Metadata Repository)",
                     "@type": "dcat:Distribution",
+                    "description": "View this dataset on the CMR (Common Metadata Repository)",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/search/concepts/C156141689-LARC.html",
+                    "mediaType": "text/html",
                     "title": "CMR"
                 }
             ],
+            "graphic-preview-description": "ASDC List of MISR Imagery and Articles",
+            "graphic-preview-file": "https://asdc.larc.nasa.gov/documents/misr/imagery.html",
+            "identifier": "C156141689-LARC",
+            "issued": "2007-07-30",
+            "keyword": [
+                "nasa"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C156141689-LARC.html",
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
+            "title": "MISR Level 3 FIRSTLOOK Component Global Aerosol Product covering a month V002"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ASDC/SUBORBITAL/DISCOVERAQ_Colorado_Aerosol_AircraftInSitu_P3B_Data_1",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2022-04-18. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/ASDC/SUBORBITAL/DISCOVERAQ_Colorado_Aerosol_AircraftInSitu_P3B_Data_1.",
-            "issued": "2021-08-20",
-            "temporal": "2014-07-06T00:00:00Z/2014-08-14T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-04-18",
-            "keyword": [
-                "aerosols",
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
-            "identifier": "C2254457471-LARC_ASDC",
             "description": "DISCOVERAQ_Colorado_Aerosol_AircraftInSitu_P3B_Data contains in situ aerosol data collected onboard NASA's P-3B aircraft during the Colorado (Denver) deployment of NASA's DISCOVER-AQ field study. Instruments utilized to collect data found in this data product include the 3-Wavelength Particle Soot Absorption Photometer Manufactured by Radiance Research (PSAP), Aerodynamic Particle Sizer (APS), Condensation Particle Counter (CPC), Nephelometer, Launch Abort System (LAS), Particle-Into-Liquid Sampler (PILS), Scanning Mobility Particle Sizer (SMPS), Single Particle Soot Photometer (SP2), Ultra-High Sensitivity Aerosol Spectrometer (UHSAS), Cloud and Aerosol Spectrometer (CAS), Cloud Imaging Probe (CIP), and Theory of change (TOC). This data product contains data for only the Colorado deployment, and data collection is complete.\r\n\r\nUnderstanding the factors that contribute to near surface pollution is difficult using only satellite-based observations. The incorporation of surface-level measurements from aircraft and ground-based platforms provides the crucial information necessary to validate and expand upon the use of satellites in understanding near surface pollution. Deriving Information on Surface conditions from Column and Vertically Resolved Observations Relevant to Air Quality (DISCOVER-AQ) was a four-year campaign conducted in collaboration between NASA Langley Research Center, NASA Goddard Space Flight Center, NASA Ames Research Center, and multiple universities to improve the use of satellites to monitor air quality for public health and environmental benefit. Through targeted airborne and ground-based observations, DISCOVER-AQ enabled more effective use of current and future satellites to diagnose ground level conditions influencing air quality.\r\n\r\nDISCOVER-AQ employed two NASA aircraft, the P-3B and King Air, with the P-3B completing in-situ spiral profiling of the atmosphere (aerosol properties, meteorological variables, and trace gas species). The King Air conducted both passive and active remote sensing of the atmospheric column extending below the aircraft to the surface. Data from an existing network of surface air quality monitors, AERONET sun photometers, Pandora UV/vis spectrometers and model simulations were also collected. Further, DISCOVER-AQ employed many surface monitoring sites, with measurements being made on the ground, in conjunction with the aircraft. The B200 and P-3B conducted flights in Baltimore-Washington, D.C. in 2011, Houston, TX in 2013, San Joaquin Valley, CA in 2013, and Denver, CO in 2014. These regions were targeted due to being in violation of the National Ambient Air Quality Standards (NAAQS).\r\n\r\nThe first objective of DISCOVER-AQ was to determine and investigate correlations between surface measurements and satellite column observations for the trace gases ozone (O3), nitrogen dioxide (NO2), and formaldehyde (CH2O) to understand how satellite column observations can diagnose surface conditions. DISCOVER-AQ also had the objective of using surface-level measurements to understand how satellites measure diurnal variability and to understand what factors control diurnal variability. Lastly, DISCOVER-AQ aimed to explore horizontal scales of variability, such as regions with steep gradients and urban plumes.",
-            "title": "DISCOVER-AQ Colorado Deployment P-3B Aircraft In Situ Aerosol Data",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC%2FSUBORBITAL%2FDISCOVERAQ_Colorado_Aerosol_AircraftInSitu_P3B_Data_1",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC%2FSUBORBITAL%2FDISCOVERAQ_Colorado_Aerosol_AircraftInSitu_P3B_Data_1",
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
-                    "downloadURL": "https://doi.org/10.5067/ASDC/SUBORBITAL/DISCOVERAQ_Colorado_Aerosol_AircraftInSitu_P3B_Data_1",
-                    "description": "DOI Data Set Landing Page for DISCOVERAQ_Colorado_Aerosol_AircraftInSitu_P3B_Data_1",
                     "@type": "dcat:Distribution",
+                    "description": "DOI Data Set Landing Page for DISCOVERAQ_Colorado_Aerosol_AircraftInSitu_P3B_Data_1",
+                    "downloadURL": "https://doi.org/10.5067/ASDC/SUBORBITAL/DISCOVERAQ_Colorado_Aerosol_AircraftInSitu_P3B_Data_1",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2254457471-LARC_ASDC",
-                    "description": "Earthdata Search Client for DISCOVER-AQ_Colorado_Aerosol_AircraftInSitu_P3B_Data_1",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search Client for DISCOVER-AQ_Colorado_Aerosol_AircraftInSitu_P3B_Data_1",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2254457471-LARC_ASDC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/DISCOVER-AQ/Colorado_Aerosol_AircraftInSitu_P3B_Data_1/",
-                    "description": "ASDC Direct Data Download for DISCOVERAQ_Colorado_Aerosol_AircraftInSitu_P3B_Data_1",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for DISCOVERAQ_Colorado_Aerosol_AircraftInSitu_P3B_Data_1",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/DISCOVER-AQ/Colorado_Aerosol_AircraftInSitu_P3B_Data_1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 }
             ],
+            "identifier": "C2254457471-LARC_ASDC",
+            "issued": "2021-08-20",
+            "keyword": [
+                "aerosols",
+                "atmosphere",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/ASDC/SUBORBITAL/DISCOVERAQ_Colorado_Aerosol_AircraftInSitu_P3B_Data_1",
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
             "spatial": "<?xml version=\"1.0\" encoding=\"UTF-8\"?><gml:Polygon xmlns:gml=\"http://www.opengis.net/gml/3.2\" srsName=\"EPSG:9825\"><gml:outerBoundaryIs><gml:LinearRing><gml:posList>0.0 -130.0 0.0 0.0 48.0 0.0 48.0 -130.0 0.0 -130.0</gml:posList></gml:LinearRing></gml:outerBoundaryIs><gml:innerBoundaryIs></gml:innerBoundaryIs></gml:Polygon>",
+            "temporal": "2014-07-06T00:00:00Z/2014-08-14T23:59:59.999Z",
             "theme": [
                 "DISCOVER-AQ",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "DISCOVER-AQ Colorado Deployment P-3B Aircraft In Situ Aerosol Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/AQR50-3YUDE",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "NASA Aquarius project. 2017-12-07. Aquarius Official Release Level 3 Rain-flagged Sea Surface Salinity Standard Mapped Image Descending Monthly Climatology Data. Version 5.0. Aquarius Sea Surface Salinity Products. Goddard Space Flight Center, 8800 Greenbelt Rd.; Greeenbelt, MD., 20771, USA. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/GSFC OBPG. https://doi.org/10.5067/AQR50-3YUDE. http://podaac.jpl.nasa.gov/SeaSurfaceSalinity/Aquarius. NASA Aquarius project, NASA/GSFC OBPG, 2017-12-07, Aquarius Official Release Level 3 Rain-flagged Sea Surface Salinity Standard Mapped Image Descending Monthly Climatology Data V5.0, http://podaac.jpl.nasa.gov/SeaSurfaceSalinity/Aquarius.",
-            "issued": "2017-10-21",
-            "temporal": "2011-08-25T02:41:02Z/2015-06-07T12:45:21Z",
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
-            "identifier": "C2491757158-POCLOUD",
-            "description": "Aquarius Level 3 sea surface salinity (SSS) rain-flagged standard mapped image data contains gridded 1 degree spatial resolution SSS averaged over daily, 7 day, monthly, and\nseasonal time scales. This particular data set is the monthly climatology, Descending rain-flagged sea surface salinity product for version 5.0 of the Aquarius data set. Only retrieved values for Descending passes have been used to create this product.  The Aquarius instrument is onbard the AQUARIUS/SAC-D satellite, a collaborative effort between NASA and the Argentinian Space Agency Comision Nacional de Actividades Espaciales (CONAE). The instrument consists of three radiometers in push broom alignment at incidence angles of 29, 38, and 46 degrees incidence angles relative to the shadow side of the orbit.  Footprints for the beams are: 76 km (along-track) x 94 km (cross-track), 84 km x 120 km and 96km x 156 km, yielding a total cross-track swath of 370 km. The radiometers measure brightness temperature at 1.413 GHz in their respective horizontal and vertical polarizations (TH and TV). A scatterometer operating at 1.26 GHz measures ocean backscatter in each footprint that is used for surface roughness corrections in the estimation of salinity. The scatterometer has an approximate 390km swath.",
-            "release-place": "Goddard Space Flight Center, 8800 Greenbelt Rd.; Greeenbelt, MD., 20771, USA",
-            "series-name": "Aquarius Official Release Level 3 Rain-flagged Sea Surface Salinity Standard Mapped Image Descending Monthly Climatology Data",
-            "graphic-preview-description": "Thumbnail",
             "creator": "NASA Aquarius project",
-            "title": "Aquarius Official Release Level 3 Rain-flagged Sea Surface Salinity Standard Mapped Image Descending Monthly Climatology Data V5.0",
-            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/AQUARIUS_L3_SSS-RainFlagged_SMID_MONTHLY-CLIMATOLOGY_V5.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "Aquarius Level 3 sea surface salinity (SSS) rain-flagged standard mapped image data contains gridded 1 degree spatial resolution SSS averaged over daily, 7 day, monthly, and\nseasonal time scales. This particular data set is the monthly climatology, Descending rain-flagged sea surface salinity product for version 5.0 of the Aquarius data set. Only retrieved values for Descending passes have been used to create this product.  The Aquarius instrument is onbard the AQUARIUS/SAC-D satellite, a collaborative effort between NASA and the Argentinian Space Agency Comision Nacional de Actividades Espaciales (CONAE). The instrument consists of three radiometers in push broom alignment at incidence angles of 29, 38, and 46 degrees incidence angles relative to the shadow side of the orbit.  Footprints for the beams are: 76 km (along-track) x 94 km (cross-track), 84 km x 120 km and 96km x 156 km, yielding a total cross-track swath of 370 km. The radiometers measure brightness temperature at 1.413 GHz in their respective horizontal and vertical polarizations (TH and TV). A scatterometer operating at 1.26 GHz measures ocean backscatter in each footprint that is used for surface roughness corrections in the estimation of salinity. The scatterometer has an approximate 390km swath.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAQR50-3YUDE",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAQR50-3YUDE",
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
-                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/AQUARIUS_L3_SSS-RainFlagged_SMID_MONTHLY-CLIMATOLOGY_V5.jpg",
-                    "description": "Thumbnail",
                     "@type": "dcat:Distribution",
+                    "description": "Thumbnail",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/AQUARIUS_L3_SSS-RainFlagged_SMID_MONTHLY-CLIMATOLOGY_V5.jpg",
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
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2491757158-POCLOUD",
-                    "description": "HTTPS endpoint for data browse and download",
                     "@type": "dcat:Distribution",
+                    "description": "HTTPS endpoint for data browse and download",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2491757158-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2491757158-POCLOUD",
-                    "description": "Browse granule search results in Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse granule search results in Earthdata Search",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2491757158-POCLOUD",
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
+            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/AQUARIUS_L3_SSS-RainFlagged_SMID_MONTHLY-CLIMATOLOGY_V5.jpg",
+            "identifier": "C2491757158-POCLOUD",
+            "issued": "2017-10-21",
+            "keyword": [
+                "oceans",
+                "earth science",
+                "salinity/density"
+            ],
+            "landingPage": "https://doi.org/10.5067/AQR50-3YUDE",
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
+            "series-name": "Aquarius Official Release Level 3 Rain-flagged Sea Surface Salinity Standard Mapped Image Descending Monthly Climatology Data",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2011-08-25T02:41:02Z/2015-06-07T12:45:21Z",
             "theme": [
                 "AQUARIUS SAC-D",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Aquarius Official Release Level 3 Rain-flagged Sea Surface Salinity Standard Mapped Image Descending Monthly Climatology Data V5.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-2-PRL-67PCHURYUMOV-M02-V1.1",
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
+            "description": "This data set contains raw EDR images acquired by the OSIRIS Wide Angle\nCamera during the prelanding phase of the Rosetta mission at the comet 67P,\ncovering the period from 2014-04-06 to 2014-05-07.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-2-prl-67pchuryumov-m02-v1.1_9djg-nczu",
+            "issued": "2018-06-26",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-2-PRL-67PCHURYUMOV-M02-V1.1",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-2-prl-67pchuryumov-m02-v1.1_9djg-nczu",
-            "description": "This data set contains raw EDR images acquired by the OSIRIS Wide Angle\nCamera during the prelanding phase of the Rosetta mission at the comet 67P,\ncovering the period from 2014-04-06 to 2014-05-07.",
-            "title": "ROSETTA-ORBITER COMET PRELANDING OSIWAC 2 EDR DATA MTP 002",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "ROSETTA-ORBITER COMET PRELANDING OSIWAC 2 EDR DATA MTP 002"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/CALIOP/CALIPSO/CAL_LID_L2_05kmCLay-Standard-V4-21",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2018-10-17. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/CALIOP/CALIPSO/CAL_LID_L2_05kmCLay-Standard-V4-21.",
-            "issued": "2018-09-06",
-            "temporal": "2020-07-01T00:00:00Z/2022-01-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2018-09-06",
-            "keyword": [
-                "clouds",
-                "earth science",
-                "atmosphere",
-                "lidar",
-                "spectral/engineering"
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
-            "identifier": "C1978623400-LARC_ASDC",
             "description": "CAL_LID_L2_05kmCLay-Standard-V4-21 is the Cloud-Aerosol Lidar and Infrared Pathfinder Satellite Observations (CALIPSO) Lidar Level 2 5 km Cloud Layer, Version 4-21 data product. Data for this product was collected using the CALIPSO Cloud-Aerosol Lidar with Orthogonal Polarization (CALIOP) instrument. The version of this product was changed from 4-20 to 4-21 to account for a change in the operating system of the CALIPSO production cluster. Data collection for this product is ongoing.\r\n\r\nCALIPSO was launched on April 28, 2006 to study the impact of clouds and aerosols on the Earth's radiation budget and climate. It flies in the international A-Train constellation for coincident Earth observations. The CALIPSO satellite comprises three instruments, CALIOP, Imaging Infrared Radiometer (IIR), and Wide Field Camera (WFC). CALIPSO is a joint satellite mission between NASA and the French Agency, CNES.",
-            "title": "CALIPSO Lidar Level 2 5 km Cloud Layer, V4-21",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FCALIOP%2FCALIPSO%2FCAL_LID_L2_05kmCLay-Standard-V4-21",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FCALIOP%2FCALIPSO%2FCAL_LID_L2_05kmCLay-Standard-V4-21",
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
-                    "downloadURL": "https://www-calipso.larc.nasa.gov/resources/calipso_users_guide/qs/cal_lid_l2_all_v4-20.php",
-                    "description": "Data Quality Summary for the CALIPSO Version 4.20 and V4.21 Lidar Level 2 Data Products",
                     "@type": "dcat:Distribution",
+                    "description": "Data Quality Summary for the CALIPSO Version 4.20 and V4.21 Lidar Level 2 Data Products",
+                    "downloadURL": "https://www-calipso.larc.nasa.gov/resources/calipso_users_guide/qs/cal_lid_l2_all_v4-20.php",
+                    "mediaType": "text/html",
                     "title": "View this dataset's product quality assessment"
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
-                    "downloadURL": "https://doi.org/10.5067/CALIOP/CALIPSO/CAL_LID_L2_05kmCLay-Standard-V4-21",
-                    "description": "DOI data set landing page for CAL_LID_L2_05kmCLay-Standard-V4-21",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for CAL_LID_L2_05kmCLay-Standard-V4-21",
+                    "downloadURL": "https://doi.org/10.5067/CALIOP/CALIPSO/CAL_LID_L2_05kmCLay-Standard-V4-21",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1978623400-LARC_ASDC",
-                    "description": "Earthdata Search for CAL_LID_L2_05kmCLay-Standard-V4-21 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for CAL_LID_L2_05kmCLay-Standard-V4-21 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1978623400-LARC_ASDC",
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
-                    "downloadURL": "https://www-calipso.larc.nasa.gov/resources/calipso_users_guide/",
-                    "description": "CALIPSO Data User\u2019s Guide",
                     "@type": "dcat:Distribution",
+                    "description": "CALIPSO Data User\u2019s Guide",
+                    "downloadURL": "https://www-calipso.larc.nasa.gov/resources/calipso_users_guide/",
+                    "mediaType": "text/html",
                     "title": "View this dataset's user's guide"
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
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/CALIPSO/LID_L2_05kmCLay-Standard-V4-21/",
-                    "description": "ASDC Direct Data Download for CAL_LID_L2_05kmCLay-Standard-V4-21_V4-21",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for CAL_LID_L2_05kmCLay-Standard-V4-21_V4-21",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/CALIPSO/LID_L2_05kmCLay-Standard-V4-21/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/CALIPSO/LID_L2_05kmCLay-Standard-V4-21/contents.html",
-                    "description": "OPeNDAP data access for CAL_LID_L2_05kmCLay-Standard-V4-21_V4-21",
                     "@type": "dcat:Distribution",
+                    "description": "OPeNDAP data access for CAL_LID_L2_05kmCLay-Standard-V4-21_V4-21",
+                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/CALIPSO/LID_L2_05kmCLay-Standard-V4-21/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 }
             ],
+            "identifier": "C1978623400-LARC_ASDC",
+            "issued": "2018-09-06",
+            "keyword": [
+                "clouds",
+                "earth science",
+                "atmosphere",
+                "lidar",
+                "spectral/engineering"
+            ],
+            "landingPage": "https://doi.org/10.5067/CALIOP/CALIPSO/CAL_LID_L2_05kmCLay-Standard-V4-21",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2018-09-06",
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
+            "title": "CALIPSO Lidar Level 2 5 km Cloud Layer, V4-21"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/CAMEX-4/PROFILER/DATA102",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Mahoney, Michael J.2002. CAMEX-4 ER-2 MICROWAVE TEMPERATURE PROFILER [indicate subset used]. Dataset available online from the NASA Global Hydrometeorology Resource Center DAAC, Huntsville, Alabama, U.S.A. DOI: http://dx.doi.org/10.5067/CAMEX-4/PROFILER/DATA102",
-            "issued": "2002-10-16",
-            "temporal": "2001-08-26T16:52:18Z/2001-09-25T01:09:29Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-04-28",
-            "keyword": [
-                "earth science",
-                "atmospheric temperature",
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
-            "identifier": "C1979099369-GHRC_DAAC",
             "description": "The CAMEX-4 ER-2 Microwave Temperature Profiler dataset was collected by the Microwave Temperature Profiler (MTP), which is a passive microwave radiometer which measures the thermal emission from oxygen molecules in the atmosphere for a selection of elevation angles. Current observing frequencies are 56.6 and 58.8 GHz. Measured brightness temperature versus elevation angle is converted to air temperature versus altitude using a statistical retrieval procedure. An altitude temperature profile is produced every three km along the flight path. Data were collected from the Jacksonville Naval Air Station, Florida during the CAMEX-4 campaign spanning from August 26 - September 26. 2001.",
-            "graphic-preview-description": "N/A",
-            "title": "CAMEX-4 ER-2 MICROWAVE TEMPERATURE PROFILER V1",
-            "graphic-preview-file": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/camex4/MTP_ER-2/browse/",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FCAMEX-4%2FPROFILER%2FDATA102",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FCAMEX-4%2FPROFILER%2FDATA102",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=c4emtp",
-                    "description": "Files may be downloaded directly to your workstation from this link",
                     "@type": "dcat:Distribution",
+                    "description": "Files may be downloaded directly to your workstation from this link",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=c4emtp",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/camex4/MTP_ER-2/browse/c4emtp_20010922.png",
-                    "description": "Sample browse image",
                     "@type": "dcat:Distribution",
+                    "description": "Sample browse image",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/camex4/MTP_ER-2/browse/c4emtp_20010922.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://ghrc.nsstc.nasa.gov/uso/ds_docs/camex4/c4emtp/c4emtp_dataset.html",
-                    "description": "The guide document contains detailed information about the dataset",
                     "@type": "dcat:Distribution",
+                    "description": "The guide document contains detailed information about the dataset",
+                    "downloadURL": "http://ghrc.nsstc.nasa.gov/uso/ds_docs/camex4/c4emtp/c4emtp_dataset.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/doc/camex4/c4emtp/mtp_er2.pdf",
-                    "description": "ER2 Microwave Temperature Profiler (MTP/ER2)",
                     "@type": "dcat:Distribution",
+                    "description": "ER2 Microwave Temperature Profiler (MTP/ER2)",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/doc/camex4/c4emtp/mtp_er2.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View the primary investigator's documentation for this dataset"
                 },
                 {
-                    "mediaType": "application/rtf",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/doc/camex4/c4emtp/MTP_ER2_Readme.rtf",
-                    "description": "URL Text",
                     "@type": "dcat:Distribution",
+                    "description": "URL Text",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/doc/camex4/c4emtp/MTP_ER2_Readme.rtf",
+                    "mediaType": "application/rtf",
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
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/camex4/MTP_ER-2/browse/",
-                    "description": "N/A",
                     "@type": "dcat:Distribution",
+                    "description": "N/A",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/camex4/MTP_ER-2/browse/",
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
+            "graphic-preview-file": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/camex4/MTP_ER-2/browse/",
+            "identifier": "C1979099369-GHRC_DAAC",
+            "issued": "2002-10-16",
+            "keyword": [
+                "earth science",
+                "atmospheric temperature",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.5067/CAMEX-4/PROFILER/DATA102",
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
             "spatial": "-85.744 24.19 -61.98 39.458",
+            "temporal": "2001-08-26T16:52:18Z/2001-09-25T01:09:29Z",
             "theme": [
                 "CAMEX-4",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "CAMEX-4 ER-2 MICROWAVE TEMPERATURE PROFILER V1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-VARGBDET-5-WISAST-V1.0",
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
+            "description": "Photometric observations of 125 asteroids, including absolute magnitudes, reported in Wisniewski et al. 1997.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-vargbdet-5-wisast-v1.0_9dr4-93sx",
+            "issued": "2018-06-26",
+            "keyword": [
+                "asteroid",
+                "support archives"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-VARGBDET-5-WISAST-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-vargbdet-5-wisast-v1.0_9dr4-93sx",
-            "description": "Photometric observations of 125 asteroids, including absolute magnitudes, reported in Wisniewski et al. 1997.",
-            "title": "WISNIEWSKI ASTEROID ABSOLUTE MAGNITUDES V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "WISNIEWSKI ASTEROID ABSOLUTE MAGNITUDES V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-I0066-5-TORINOPOL-V1.0",
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
+            "description": "This data set contains asteroid polarimetric observations made during 1995-2005 with the Torino photopolarimeter at the 2.15-m telescope at El Leoncito Observatory in Argentina. These observations are reported in Cellino et al. (2005).",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-i0066-5-torinopol-v1.0_9drt-2asn",
+            "issued": "2018-06-26",
+            "keyword": [
+                "asteroid",
+                "support archives"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-I0066-5-TORINOPOL-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-i0066-5-torinopol-v1.0_9drt-2asn",
-            "description": "This data set contains asteroid polarimetric observations made during 1995-2005 with the Torino photopolarimeter at the 2.15-m telescope at El Leoncito Observatory in Argentina. These observations are reported in Cellino et al. (2005).",
-            "title": "TORINO ASTEROID POLARIMETRY V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "TORINO ASTEROID POLARIMETRY V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/IR85TKB5BLM3",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "AMSR-E/Aqua L2B Global Swath Surface Precipitation GSFC Profiling Algorithm V004. Version 4. Archived by National Aeronautics and Space Administration, U.S. Government, NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/IR85TKB5BLM3.",
-            "issued": "2002-06-01",
-            "temporal": "2002-06-01T00:00:00Z/2011-10-04T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2011-10-04",
-            "keyword": [
-                "atmosphere",
-                "clouds",
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
-            "identifier": "C1997893797-NSIDC_ECS",
             "description": "The AMSR-E/Aqua Level-2B precipitation product includes instantaneous surface precipitation rate and type over ice-free/snow-free land and ocean between 89.24 degrees north and south latitudes at at 10 km spatial resolution along the track and 5 km spatial resolution along the scan. The data are generated by the GPROF 2017 algorithm using Version 4 of the AMSR-E Level-2A Brightness Temperatures.",
-            "title": "AMSR-E/Aqua L2B Global Swath Surface Precipitation GSFC Profiling Algorithm V004",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FIR85TKB5BLM3",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FIR85TKB5BLM3",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/AMSA/AE_Rain.004",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/AMSA/AE_Rain.004",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=AE_Rain+V004",
-                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=AE_Rain+V004",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/IR85TKB5BLM3",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/IR85TKB5BLM3",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/IR85TKB5BLM3",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/IR85TKB5BLM3",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C1997893797-NSIDC_ECS",
+            "issued": "2002-06-01",
+            "keyword": [
+                "atmosphere",
+                "clouds",
+                "earth science",
+                "precipitation"
+            ],
+            "landingPage": "https://doi.org/10.5067/IR85TKB5BLM3",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2011-10-04",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA NSIDC DAAC"
+            },
             "spatial": "-180.0 -89.24 180.0 89.24",
+            "temporal": "2002-06-01T00:00:00Z/2011-10-04T23:59:59.999Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "AMSR-E/Aqua L2B Global Swath Surface Precipitation GSFC Profiling Algorithm V004"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG2-S-PRA-3-RDR-LOWBAND-6SEC-V1.0",
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
-                "saturn",
-                "voyager"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "not applicable",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg2-s-pra-3-rdr-lowband-6sec-v1.0_9e2p-5h6x",
+            "issued": "2018-06-26",
+            "keyword": [
+                "saturn",
+                "voyager"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG2-S-PRA-3-RDR-LOWBAND-6SEC-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg2-s-pra-3-rdr-lowband-6sec-v1.0_9e2p-5h6x",
-            "description": "not applicable",
-            "title": "VG2 SAT PRA CALIBRATED HI-RES LOW FREQ. REC. BAND DATA V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "VG2 SAT PRA CALIBRATED HI-RES LOW FREQ. REC. BAND DATA V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://www.lpi.usra.edu/resources/cla/",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2018-06-25",
-            "temporal": "1967-01-01/1972-01-01",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
-            "references": [
-                "http://www.lpi.usra.edu/resources/apollopanoramas/",
-                "http://www.lpi.usra.edu/resources/cla/",
-                "http://www.lpi.usra.edu/resources/lunarorbiter/",
-                "http://www.lpi.usra.edu/resources/lunar_orbiter/",
-                "http://www.lpi.usra.edu/resources/ranger/",
-                "http://planetarynames.wr.usgs.gov/"
-            ],
-            "keyword": [
-                "imagery",
-                "lunar science",
-                "space science",
-                "circulation",
-                "modeling"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Paul Schenk",
                 "hasEmail": "mailto:rpif@lpi.usra.edu"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Aeronautics and Space Administration"
-            },
-            "identifier": "NASA-0000030",
             "description": "The Consolidated Lunar Atlas is a collection of the best photographic images of the moon, including low-oblique photography, full-moon photography, and tabular and positional plates.",
-            "title": "Consolidated Lunar Atlas",
-            "programCode": [
-                "026:009"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -417894,595 +417866,636 @@
                     "mediaType": "text/html"
                 }
             ],
+            "identifier": "NASA-0000030",
+            "issued": "2018-06-25",
+            "keyword": [
+                "imagery",
+                "lunar science",
+                "space science",
+                "circulation",
+                "modeling"
+            ],
+            "landingPage": "http://www.lpi.usra.edu/resources/cla/",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:009"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Aeronautics and Space Administration"
+            },
+            "references": [
+                "http://www.lpi.usra.edu/resources/apollopanoramas/",
+                "http://www.lpi.usra.edu/resources/cla/",
+                "http://www.lpi.usra.edu/resources/lunarorbiter/",
+                "http://www.lpi.usra.edu/resources/lunar_orbiter/",
+                "http://www.lpi.usra.edu/resources/ranger/",
+                "http://planetarynames.wr.usgs.gov/"
+            ],
             "spatial": "Lunar",
-            "accrualPeriodicity": "irregular",
+            "temporal": "1967-01-01/1972-01-01",
             "theme": [
                 "Space Science"
-            ]
+            ],
+            "title": "Consolidated Lunar Atlas"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MEX-M-MRS-1%2F2%2F3-EXT5-3806-V1.0",
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
+            "description": "This is a Mars Express Radio Science data set, collected during the extended mission phase 2015-01-01 to 2016-12-31. It is a Occultation measurement and covers the time 2015-09-01T14:10:09 to 2015-09-02T06:48:38.999.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mex-m-mrs-1-2-3-ext5-3806-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "mars express",
+                "mars"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MEX-M-MRS-1%2F2%2F3-EXT5-3806-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mex-m-mrs-1-2-3-ext5-3806-v1.0",
-            "description": "This is a Mars Express Radio Science data set, collected during the extended mission phase 2015-01-01 to 2016-12-31. It is a Occultation measurement and covers the time 2015-09-01T14:10:09 to 2015-09-02T06:48:38.999.",
-            "title": "MARS EXPRESS MARS MRS 1/2/3\n                                     EXTENDED MISSION 5 3806 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "MARS EXPRESS MARS MRS 1/2/3\n                                     EXTENDED MISSION 5 3806 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/NIMBUS/NmTHIR115-1H",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Nimbus Temperature-Humidity Infrared Radiometer 11.5 \u00b5m Swath L1, HDF5 V001. Version 1. Archived by National Aeronautics and Space Administration, U.S. Government, NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/NIMBUS/NmTHIR115-1H.",
-            "issued": "1970-04-13",
-            "temporal": "1970-04-13T00:00:00Z/1971-04-01T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "1971-04-01",
-            "keyword": [
-                "infrared wavelengths",
-                "earth science",
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
-            "identifier": "C1701043553-NSIDC_ECS",
             "description": "This data set (NmTHIR115-1H) consists of daily, global radiative temperatures measured in the 11.5 \u00b5m window (10.5 \u00b5m - 12.5 \u00b5m) by the Temperature-Humidity Infrared Radiometer (THIR) on board the Nimbus 4 satellite. This window was used to measure cloud top or surface temperatures.",
-            "title": "Nimbus Temperature-Humidity Infrared Radiometer 11.5 \u00b5m Swath L1, HDF5 V001",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FNIMBUS%2FNmTHIR115-1H",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FNIMBUS%2FNmTHIR115-1H",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/NIMBUS/NmTHIR115-1H.001/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/NIMBUS/NmTHIR115-1H.001/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1000001341-NSIDC_ECS&m=-31.078125%21-0.5625%211%211%210%210%2C2&q=NmTHIR115-1H",
-                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1000001341-NSIDC_ECS&m=-31.078125%21-0.5625%211%211%210%210%2C2&q=NmTHIR115-1H",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/data/data-access-tool/NmTHIR115-1H/versions/1/",
-                    "description": "Data Access link for ITSD project",
                     "@type": "dcat:Distribution",
+                    "description": "Data Access link for ITSD project",
+                    "downloadURL": "https://nsidc.org/data/data-access-tool/NmTHIR115-1H/versions/1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/NIMBUS/NmTHIR115-1H",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/NIMBUS/NmTHIR115-1H",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/NIMBUS/NmTHIR115-1H",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/NIMBUS/NmTHIR115-1H",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C1701043553-NSIDC_ECS",
+            "issued": "1970-04-13",
+            "keyword": [
+                "infrared wavelengths",
+                "earth science",
+                "spectral/engineering"
+            ],
+            "landingPage": "https://doi.org/10.5067/NIMBUS/NmTHIR115-1H",
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
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "1970-04-13T00:00:00Z/1971-04-01T23:59:59.999Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Nimbus Temperature-Humidity Infrared Radiometer 11.5 \u00b5m Swath L1, HDF5 V001"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/232",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Kouwen, N., R. Soulis, W. Jenkinson, A. Graham, and T. Neff. 1998. BOREAS 1995 HYD-09 Tipping Bucket Rain Data. ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/232",
-            "issued": "2023-11-22",
-            "temporal": "1995-01-01T00:00:00Z/1995-12-31T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-11-27",
-            "keyword": [
-                "atmosphere",
-                "earth science",
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
-            "identifier": "C2807610223-ORNL_CLOUD",
             "description": "Contains the Tipping Bucket rain gauge data that was collected by the HYD09 group at various locations.",
-            "graphic-preview-description": "Browse Image",
-            "title": "BOREAS 1995 HYD-09 Tipping Bucket Rain Data",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/boreas_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F232",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F232",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/boreas/HYD/h9rgtb95/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/boreas/HYD/h9rgtb95/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/BOREAS/guides/HYD09_TPBK_RG.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/BOREAS/guides/HYD09_TPBK_RG.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/232",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/232",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/HYD/h9rgtb95/comp/h9rgtb95.def",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/HYD/h9rgtb95/comp/h9rgtb95.def",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/msword",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/HYD/h9rgtb95/comp/HYD09_TPBK_RG.doc",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/HYD/h9rgtb95/comp/HYD09_TPBK_RG.doc",
+                    "mediaType": "application/msword",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/HYD/h9rgtb95/comp/HYD09_TPBK_RG.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/HYD/h9rgtb95/comp/HYD09_TPBK_RG.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/HYD/h9rgtb95/comp/HYD09_TPBK_RG.txt",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/HYD/h9rgtb95/comp/HYD09_TPBK_RG.txt",
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
+            "identifier": "C2807610223-ORNL_CLOUD",
+            "issued": "2023-11-22",
+            "keyword": [
+                "atmosphere",
+                "earth science",
+                "precipitation"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/232",
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
             "spatial": "-105.14 53.9 -98.34 55.93",
+            "temporal": "1995-01-01T00:00:00Z/1995-12-31T23:59:59Z",
             "theme": [
                 "BOREAS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "BOREAS 1995 HYD-09 Tipping Bucket Rain Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/214",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Esser, G. 2013. NPP Multi-Biome: Global Osnabruck Data, 1937-1981, R1. ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/214",
-            "issued": "2023-08-17",
-            "temporal": "1937-01-01T00:00:00Z/1981-12-31T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-08-17",
-            "keyword": [
-                "vegetation",
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
-            "identifier": "C2752605983-ORNL_CLOUD",
             "description": "This data set contains three files. The first file provides net primary productivity (NPP) estimates, vegetation characteristics, and summary climate data for 720 globally-distributed terrestrial sites. Each site is geographically referenced (latitude/longitude) and classified according to biome (i.e., cropland, desert, forest, grassland, Mediterranean, pasture, plantation, savanna, tundra, and wetlands), where known. The data were extracted and synthesized from scientific literature dating from 1869 to 1982. The majority of references were published in the 1960s and 1970s. The second file provides a summary of climate, vegetation type, species, and type for the 720 records. The third file provides the bibliography of 858 original-source references of data on NPP from Esser et al. (1997). Literature that is not directly cross-referenced to the NPP data set records is marked with an asterisk (*). Of the 720 unique NPP records, about two-thirds have above-ground net primary production (ANPP) estimates that range between 1 and 8,530 g/m2/year dry matter, one-fourth of the sites have estimates for below-ground NPP that range between 0 and 5,828 g/m2/year, and more than half of the sites have total NPP estimates that range from 3 to 9,320 g/m2/year dry matter. The high-range estimates are lower when doubtful values, wetlands estimates, and estimates for crops/pastures and other managed systems are excluded from calculations. Revision Notes: Only the documentation for this data set has been modified. The data files have been checked for accuracy and are identical to those originally published in 1998.",
-            "graphic-preview-description": "Browse Image",
-            "title": "NPP Multi-Biome: Global Osnabruck Data, 1937-1981, R1",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/npp_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F214",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F214",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/npp/multi_biome/NPP_ODS/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/npp/multi_biome/NPP_ODS/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/NPP/guides/NPP_ODS.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/NPP/guides/NPP_ODS.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/214",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/214",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/npp/multi_biome/NPP_ODS/comp/NPP_ODS.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/npp/multi_biome/NPP_ODS/comp/NPP_ODS.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/npp/multi_biome/NPP_ODS/comp/ORNL_TM_13485_Esser.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/npp/multi_biome/NPP_ODS/comp/ORNL_TM_13485_Esser.pdf",
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
+            "identifier": "C2752605983-ORNL_CLOUD",
+            "issued": "2023-08-17",
+            "keyword": [
+                "vegetation",
+                "biosphere",
+                "earth science",
+                "ecological dynamics"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/214",
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
             "spatial": "-165.0 -65.25 177.0 75.67",
+            "temporal": "1937-01-01T00:00:00Z/1981-12-31T23:59:59Z",
             "theme": [
                 "NPP",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "NPP Multi-Biome: Global Osnabruck Data, 1937-1981, R1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/SSAT2-DAX01",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "GSFC. 1996-07-19. SEASAT SCATTEROMETER DEALIASED OCEAN WIND VECTORS (Atlas). Version 1. SEASAT SCATTEROMETER DEALIASED OCEAN WIND VECTORS (Atlas). PO.DAAC. Archived by National Aeronautics and Space Administration, U.S. Government, PO.DAAC. https://doi.org/10.5067/SSAT2-DAX01. https://podaac-tools.jpl.nasa.gov/drive/files/pub/ocean_wind/seasat/wind/swath_Atlas/doc/Readme_002.html. GSFC, PO.DAAC, 1996-07-19, SEASAT SCATTEROMETER DEALIASED OCEAN WIND VECTORS (Atlas), https://podaac-tools.jpl.nasa.gov/drive/files/pub/ocean_wind/seasat/wind/swath_Atlas/doc/Readme_002.html.",
-            "issued": "2009-06-15",
-            "temporal": "1978-07-07T00:00:00Z/1978-10-10T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2011-01-21",
-            "keyword": [
-                "ocean winds",
-                "oceans",
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
-            "identifier": "C2617197627-POCLOUD",
-            "description": "Contains wind speeds and directions derived from the Seasat-A Scatterometer (SASS), presented chronologically by swath for the period between 7 July 1978 and 10 October 1978. Robert Atlas et al. (1987) produced this product using an objective ambiguity removal scheme to dealias the wind vector data binned at 100 km cells, which were calculated by Frank Wentz.",
-            "release-place": "PO.DAAC",
-            "series-name": "SEASAT SCATTEROMETER DEALIASED OCEAN WIND VECTORS (Atlas)",
-            "graphic-preview-description": "Thumbnail",
             "creator": "GSFC",
-            "title": "SEASAT SCATTEROMETER DEALIASED OCEAN WIND VECTORS (Atlas)",
-            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/ATLAS_DEALIASED_SASS_L2.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "Contains wind speeds and directions derived from the Seasat-A Scatterometer (SASS), presented chronologically by swath for the period between 7 July 1978 and 10 October 1978. Robert Atlas et al. (1987) produced this product using an objective ambiguity removal scheme to dealias the wind vector data binned at 100 km cells, which were calculated by Frank Wentz.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSSAT2-DAX01",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSSAT2-DAX01",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/ATLAS_DEALIASED_SASS_L2.jpg",
-                    "description": "Thumbnail",
                     "@type": "dcat:Distribution",
+                    "description": "Thumbnail",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/ATLAS_DEALIASED_SASS_L2.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://podaac-tools.jpl.nasa.gov/drive/files/pub/ocean_wind/seasat/wind/swath_Atlas/doc/Readme_002.html",
-                    "description": "Dataset User Guide",
                     "@type": "dcat:Distribution",
+                    "description": "Dataset User Guide",
+                    "downloadURL": "https://podaac-tools.jpl.nasa.gov/drive/files/pub/ocean_wind/seasat/wind/swath_Atlas/doc/Readme_002.html",
+                    "mediaType": "text/html",
                     "title": "View this dataset's user's guide"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/seasat/open/L2/atlas/docs/Readme_002.html",
-                    "description": "PO.DAAC Drive",
                     "@type": "dcat:Distribution",
+                    "description": "PO.DAAC Drive",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/seasat/open/L2/atlas/docs/Readme_002.html",
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
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2617197627-POCLOUD",
-                    "description": "HTTPS endpoint for data browse and download",
                     "@type": "dcat:Distribution",
+                    "description": "HTTPS endpoint for data browse and download",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2617197627-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2617197627-POCLOUD",
-                    "description": "Browse granule search results in Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse granule search results in Earthdata Search",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2617197627-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 }
             ],
+            "graphic-preview-description": "Thumbnail",
+            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/ATLAS_DEALIASED_SASS_L2.jpg",
+            "identifier": "C2617197627-POCLOUD",
+            "issued": "2009-06-15",
+            "keyword": [
+                "ocean winds",
+                "oceans",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/SSAT2-DAX01",
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
+            "series-name": "SEASAT SCATTEROMETER DEALIASED OCEAN WIND VECTORS (Atlas)",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "1978-07-07T00:00:00Z/1978-10-10T23:59:59.999Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "SEASAT SCATTEROMETER DEALIASED OCEAN WIND VECTORS (Atlas)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=ULY-J-HISCALE-4-SUMM-WARTD-V1.0",
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
+            "description": "This data set consists of HISCALE Composition Aperture (WARTD) ion counts. These measurements were taken during the Ulysses Jupiter encounter 1991-12-31 to 1992-02-16, and include 1 hour averaged inbound cruise data (1991-12-31 to 1992-02-01), and 15 minute averaged encounter data (1992-02-02 to 1992-02-16).",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.uly-j-hiscale-4-summ-wartd-v1.0_9eia-4q5x",
+            "issued": "2021-05-21",
+            "keyword": [
+                "jupiter",
+                "ulysses"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=ULY-J-HISCALE-4-SUMM-WARTD-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.uly-j-hiscale-4-summ-wartd-v1.0_9eia-4q5x",
-            "description": "This data set consists of HISCALE Composition Aperture (WARTD) ion counts. These measurements were taken during the Ulysses Jupiter encounter 1991-12-31 to 1992-02-16, and include 1 hour averaged inbound cruise data (1991-12-31 to 1992-02-01), and 15 minute averaged encounter data (1992-02-02 to 1992-02-16).",
-            "title": "ULYSSES JUPITER HISCALE COMPOSITION\n                                        APERTURE ION COUNTS",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ULYSSES JUPITER HISCALE COMPOSITION\n                                        APERTURE ION COUNTS"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=LRO-L-LAMP-2-EDR-V1.0",
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
-                "lunar reconnaissance orbiter"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "The Lunar Reconnaissance Orbiter (LRO) Lyman Alpha Mapping Project (LAMP) CODMAC Level 2 Experiment Data Record is a collection of the far ultraviolet photon detections obtained by the LAMP instrument, in raw form. As such, it constitutes the permanent record of the raw LAMP data. These data include both the instrument science and housekeeping data, organized into extensions within files formatted according to the Flexible Image Transport System (FITS) standard, version 2.1b. The LAMP EDR archive enables reprocessing of the raw science data as radiometric and geometric calibration processing routines improve. Investigators interested in applying advanced calibration methods or needing to understand the properties of the raw data will find the EDR products useful. Most investigators, however, will be interested in using either the LAMP data products contained in the CODMAC Level 3 Reduced Data Record, as radiometric and geometric calibration processing has already been done for these products, or the LAMP CODMAC Level 5 far ultraviolet map products.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.lro-l-lamp-2-edr-v1.0_9eii-ukhj",
+            "issued": "2021-05-21",
+            "keyword": [
+                "moon",
+                "lunar reconnaissance orbiter"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=LRO-L-LAMP-2-EDR-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.lro-l-lamp-2-edr-v1.0_9eii-ukhj",
-            "description": "The Lunar Reconnaissance Orbiter (LRO) Lyman Alpha Mapping Project (LAMP) CODMAC Level 2 Experiment Data Record is a collection of the far ultraviolet photon detections obtained by the LAMP instrument, in raw form. As such, it constitutes the permanent record of the raw LAMP data. These data include both the instrument science and housekeeping data, organized into extensions within files formatted according to the Flexible Image Transport System (FITS) standard, version 2.1b. The LAMP EDR archive enables reprocessing of the raw science data as radiometric and geometric calibration processing routines improve. Investigators interested in applying advanced calibration methods or needing to understand the properties of the raw data will find the EDR products useful. Most investigators, however, will be interested in using either the LAMP data products contained in the CODMAC Level 3 Reduced Data Record, as radiometric and geometric calibration processing has already been done for these products, or the LAMP CODMAC Level 5 far ultraviolet map products.",
-            "title": "LRO MOON LAMP 2 EXPERIMENT DATA RECORD V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "LRO MOON LAMP 2 EXPERIMENT DATA RECORD V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/FRAMQ2JFF6J9",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "SnowEx23 Snow Water Equivalent V001. Version 1. Archived by National Aeronautics and Space Administration, U.S. Government, NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/FRAMQ2JFF6J9.",
-            "issued": "2023-03-13",
-            "temporal": "2023-03-13T00:00:00Z/2023-03-16T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-03-16",
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
-            "identifier": "C3041011983-NSIDC_ECS",
             "description": "This data set presents snow depth, snow water equivalent (SWE), and bulk snow density data collected during the NASA SnowEx 2023 field campaign between March 13-16 2023. Samples were collected using an Adirondack snow sampler (SWE tube) from two study sites: Upper Kuparuk and Toolik (UKT), an arctic tundra environment in Northern Alaska, and Farmers Loop Creamers Field (FLCF), a boreal forest near Fairbanks, Alaska.",
-            "title": "SnowEx23 Snow Water Equivalent V001",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FFRAMQ2JFF6J9",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FFRAMQ2JFF6J9",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/SNOWEX/SNEX23_SWE.001/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/SNOWEX/SNEX23_SWE.001/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=SNEX23_SWE+V001",
-                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=SNEX23_SWE+V001",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/data/data-access-tool/SNEX23_SWE/versions/1/",
-                    "description": "Search and filter data files using a map-based interface",
                     "@type": "dcat:Distribution",
+                    "description": "Search and filter data files using a map-based interface",
+                    "downloadURL": "https://nsidc.org/data/data-access-tool/SNEX23_SWE/versions/1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/FRAMQ2JFF6J9",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/FRAMQ2JFF6J9",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/FRAMQ2JFF6J9",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/FRAMQ2JFF6J9",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C3041011983-NSIDC_ECS",
+            "issued": "2023-03-13",
+            "keyword": [
+                "cryosphere",
+                "snow/ice",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/FRAMQ2JFF6J9",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2023-03-16",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA NSIDC DAAC"
+            },
             "spatial": "-149.494 64.8677 -147.6745 68.615",
+            "temporal": "2023-03-13T00:00:00Z/2023-03-16T23:59:59.999Z",
             "theme": [
                 "SnowEx",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "SnowEx23 Snow Water Equivalent V001"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.nasa.gov/d/9epu-76zj",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Becky McCauley Rench",
+                "hasEmail": "mailto:rebecca.l.mccauleyrench@nasa.gov"
+            },
+            "describedBy": "https://pds.jpl.nasa.gov/pds4/about/portal.shtml",
+            "description": "The Planetary Data System (PDS) is an archive of data products from NASA planetary missions, which is sponsored by NASA's Science Mission Directorate. We actively manage the archive to maximize its usefulness, and it has become a basic resource for scientists around the world.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://pds.jpl.nasa.gov/tools/data-search/",
+                    "mediaType": "text/html"
+                }
+            ],
+            "identifier": "NASA-0000104",
             "issued": "2018-06-25",
-            "@type": "dcat:Dataset",
-            "modified": "2021-07-02",
             "keyword": [
                 "laboratory",
                 "images",
@@ -418497,46 +418510,35 @@
                 "proposals",
                 "space science"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Becky McCauley Rench",
-                "hasEmail": "mailto:rebecca.l.mccauleyrench@nasa.gov"
-            },
+            "landingPage": "https://data.nasa.gov/d/9epu-76zj",
+            "modified": "2021-07-02",
+            "programCode": [
+                "026:007"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "NASA-0000104",
-            "description": "The Planetary Data System (PDS) is an archive of data products from NASA planetary missions, which is sponsored by NASA's Science Mission Directorate. We actively manage the archive to maximize its usefulness, and it has become a basic resource for scientists around the world.",
-            "title": "Planetary Data System (PDS)",
-            "programCode": [
-                "026:007"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://pds.jpl.nasa.gov/tools/data-search/",
-                    "mediaType": "text/html"
-                }
-            ],
-            "describedBy": "https://pds.jpl.nasa.gov/pds4/about/portal.shtml",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Space Science"
-            ]
+            ],
+            "title": "Planetary Data System (PDS)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-RDR-3-52COLOR-V2.1",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This data set contains 52-color IR data of asteroids, taken using a double circularly variable filter. The short wavelength portion of the CVF covered the octave from 0.8 to 1.6 microns with 3 percent resolution, while the long wavelength portion covered 1.5 to 2.6 microns with 5 percent resolution. Most of the data are unpublished other than in this PDS data set.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-rdr-3-52color-v2.1_9eqs-fp8f",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "1866 sisyphus",
                 "532 herculina",
@@ -418660,69 +418662,45 @@
                 "3551 verenia",
                 "674 rachele"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-RDR-3-52COLOR-V2.1",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-rdr-3-52color-v2.1_9eqs-fp8f",
-            "description": "This data set contains 52-color IR data of asteroids, taken using a double circularly variable filter. The short wavelength portion of the CVF covered the octave from 0.8 to 1.6 microns with 3 percent resolution, while the long wavelength portion covered 1.5 to 2.6 microns with 5 percent resolution. Most of the data are unpublished other than in this PDS data set.",
-            "title": "52-COLOR ASTEROID SURVEY",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "52-COLOR ASTEROID SURVEY"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/Aura/MLS/DATA/3104",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Santee, M., Livesey, N., Read, W., and Fuller, R.. 2020-04-20. ML3DBCLO. Version 004. MLS/Aura Level 3 Daily Binned Chlorine Monoxide (ClO) Mixing Ratio on Assorted Grids V004. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/Aura/MLS/DATA/3104. https://disc.gsfc.nasa.gov/datacollection/ML3DBCLO_004.html. Digital Science Data.",
-            "issued": "2020-03-06",
-            "temporal": "2004-08-02T00:00:00Z/2022-01-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-03-06",
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
-            "identifier": "C1725331414-GES_DISC",
-            "description": "ML3DBCLO is the EOS Aura Microwave Limb Sounder (MLS) daily binned on various vertical grids product for chlorine monoxide (ClO) derived from radiances measured primarily by the 640 GHz radiometer. The data version is 4.2. Data coverage is from August 2, 2004 to current. Spatial coverage is near-global (-82 to +82 degrees latitude) at a spatial resolution of 4 degrees latitude by 5 degrees longitude. The recommended useful vertical range is between 147 and 1.0 hPa, and the vertical resolution varies between 3 and 4.5 km. Users of the ML3DBCLO data product should read chapter 4 and section 3.6 of the EOS MLS Level 2 Version 4 Quality Document for more information.\n\nThe data files are archived in the netCDF4 format, which is also compatible with HDF5 readers and tools. Each file contains six group objects: lat-lon map vs pressure, lat vs pressure zonal mean, lat-lon map vs \"potential temperature\", lat vs \"potential temperature\" zonal mean, \"equivalent latitude\" vs \"potential temperature\" zonal mean, and vortex average vs \"potential temperature\". These are further subdivided into groups with all valid, ascending orbit, descending orbit, daytime (SZA < 90), and nighttime (SZA > 110) profiles. Each group has a set of data (average, min, max, std dev, rms) and geolocation fields, grid attributes, and metadata.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "ML3DBCLO",
             "creator": "Santee, M., Livesey, N., Read, W., and Fuller, R.",
-            "title": "MLS/Aura Level 3 Daily Binned Chlorine Monoxide (ClO) Mixing Ratio on Assorted Grids V004 (ML3DBCLO) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/ML3DBCLO_004.png",
-            "programCode": [
-                "026:001"
-            ],
+            "data-presentation-form": "Digital Science Data",
+            "description": "ML3DBCLO is the EOS Aura Microwave Limb Sounder (MLS) daily binned on various vertical grids product for chlorine monoxide (ClO) derived from radiances measured primarily by the 640 GHz radiometer. The data version is 4.2. Data coverage is from August 2, 2004 to current. Spatial coverage is near-global (-82 to +82 degrees latitude) at a spatial resolution of 4 degrees latitude by 5 degrees longitude. The recommended useful vertical range is between 147 and 1.0 hPa, and the vertical resolution varies between 3 and 4.5 km. Users of the ML3DBCLO data product should read chapter 4 and section 3.6 of the EOS MLS Level 2 Version 4 Quality Document for more information.\n\nThe data files are archived in the netCDF4 format, which is also compatible with HDF5 readers and tools. Each file contains six group objects: lat-lon map vs pressure, lat vs pressure zonal mean, lat-lon map vs \"potential temperature\", lat vs \"potential temperature\" zonal mean, \"equivalent latitude\" vs \"potential temperature\" zonal mean, and vortex average vs \"potential temperature\". These are further subdivided into groups with all valid, ascending orbit, descending orbit, daytime (SZA < 90), and nighttime (SZA > 110) profiles. Each group has a set of data (average, min, max, std dev, rms) and geolocation fields, grid attributes, and metadata.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAura%2FMLS%2FDATA%2F3104",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAura%2FMLS%2FDATA%2F3104",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
@@ -418732,285 +418710,319 @@
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/ML3DBCLO_004.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/ML3DBCLO_004.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/Aura_MLS_Level3/ML3DBCLO.004/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/Aura_MLS_Level3/ML3DBCLO.004/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/opendap/HDF-EOS5/Aura_MLS_Level3/ML3DBCLO.004/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/opendap/HDF-EOS5/Aura_MLS_Level3/ML3DBCLO.004/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=ML3DBCLO_004",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=ML3DBCLO_004",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://mls.jpl.nasa.gov/data/v4-2_data_quality_document.pdf",
-                    "description": "Data Quality and Description Document",
                     "@type": "dcat:Distribution",
+                    "description": "Data Quality and Description Document",
+                    "downloadURL": "https://mls.jpl.nasa.gov/data/v4-2_data_quality_document.pdf",
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
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/ML3DBCLO_004.png",
+            "identifier": "C1725331414-GES_DISC",
+            "issued": "2020-03-06",
+            "keyword": [
+                "atmospheric chemistry",
+                "earth science",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.5067/Aura/MLS/DATA/3104",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2020-03-06",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
+            },
+            "release-place": "Greenbelt, MD, USA",
+            "series-name": "ML3DBCLO",
             "spatial": "-180.0 -82.0 180.0 82.0",
+            "temporal": "2004-08-02T00:00:00Z/2022-01-17T00:00:00Z",
             "theme": [
                 "Aura",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "MLS/Aura Level 3 Daily Binned Chlorine Monoxide (ClO) Mixing Ratio on Assorted Grids V004 (ML3DBCLO) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NEAR-A-GRS-2-EDR-EROS%2FORBIT-V1.0",
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
+            "description": "This data set contains Gamma Ray Spectrometer (GRS) observations made during the Eros orbit phase of the NEAR mission. The individual observations are combined into a single file per day for each sensor.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.near-a-grs-2-edr-eros-orbit-v1.0_9eu9-3dsd",
+            "issued": "2021-05-21",
+            "keyword": [
+                "eros",
+                "near earth asteroid rendezvous"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NEAR-A-GRS-2-EDR-EROS%2FORBIT-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.near-a-grs-2-edr-eros-orbit-v1.0_9eu9-3dsd",
-            "description": "This data set contains Gamma Ray Spectrometer (GRS) observations made during the Eros orbit phase of the NEAR mission. The individual observations are combined into a single file per day for each sensor.",
-            "title": "NEAR GRS SPECTRA FOR EROS ORBIT PHASE",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "NEAR GRS SPECTRA FOR EROS ORBIT PHASE"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=P10-J-HVM-4-SUMM-S3COORDS-1MIN-V1.0",
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
-                "pioneer 10",
-                "jupiter"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "Pioneer 10 HVM data near Jupiter (covering 1973-11-03 to 1973-12-29) in System III [1965] coordinates.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.p10-j-hvm-4-summ-s3coords-1min-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "pioneer 10",
+                "jupiter"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=P10-J-HVM-4-SUMM-S3COORDS-1MIN-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.p10-j-hvm-4-summ-s3coords-1min-v1.0",
-            "description": "Pioneer 10 HVM data near Jupiter (covering 1973-11-03 to 1973-12-29) in System III [1965] coordinates.",
-            "title": "P10 JUPITER HVM SUMM S3 COORDS 1 MINUTE",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "P10 JUPITER HVM SUMM S3 COORDS 1 MINUTE"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://c3.nasa.gov/dashlink/resources/483/",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2011-11-02",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
-            "keyword": [
-                "ames",
-                "dashlink",
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
-            "identifier": "DASHLINK_483",
             "description": "The HIRENASD data produced by analyzing the experimental data is repeated on this website, for those who can not download the information in the zip format found on the primary Experimental Data page, or who wish to examine the plots of the data online.",
-            "title": "HIRENASD Experimental Data, Individual Plots",
-            "programCode": [
-                "026:029"
-            ],
             "distribution": [
                 {
-                    "mediaType": "image/pjpeg",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Magnitude_Mach7_Re7M.jpg",
-                    "description": "Magnitude_Mach7_Re7M.jpg",
                     "@type": "dcat:Distribution",
+                    "description": "Magnitude_Mach7_Re7M.jpg",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Magnitude_Mach7_Re7M.jpg",
+                    "mediaType": "image/pjpeg",
                     "title": "Magnitude_Mach7_Re7M.jpg"
                 },
                 {
-                    "mediaType": "image/pjpeg",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Magnitude_Mach8_Re7M.jpg",
-                    "description": "Magnitude_Mach8_Re7M.jpg",
                     "@type": "dcat:Distribution",
+                    "description": "Magnitude_Mach8_Re7M.jpg",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Magnitude_Mach8_Re7M.jpg",
+                    "mediaType": "image/pjpeg",
                     "title": "Magnitude_Mach8_Re7M.jpg"
                 },
                 {
-                    "mediaType": "image/pjpeg",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Magnitude_Mach8_Re23p5.jpg",
-                    "description": "Magnitude_Mach8_Re23p5.jpg",
                     "@type": "dcat:Distribution",
+                    "description": "Magnitude_Mach8_Re23p5.jpg",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Magnitude_Mach8_Re23p5.jpg",
+                    "mediaType": "image/pjpeg",
                     "title": "Magnitude_Mach8_Re23p5.jpg"
                 },
                 {
-                    "mediaType": "image/pjpeg",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Magnitude_Mach8_Re23p5_rescaled.jpg",
-                    "description": "Magnitude_Mach8_Re23p5_rescaled.jpg",
                     "@type": "dcat:Distribution",
+                    "description": "Magnitude_Mach8_Re23p5_rescaled.jpg",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Magnitude_Mach8_Re23p5_rescaled.jpg",
+                    "mediaType": "image/pjpeg",
                     "title": "Magnitude_Mach8_Re23p5_rescaled.jpg"
                 },
                 {
-                    "mediaType": "image/pjpeg",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Phase_Mach7_Re7M.jpg",
-                    "description": "Phase_Mach7_Re7M.jpg",
                     "@type": "dcat:Distribution",
+                    "description": "Phase_Mach7_Re7M.jpg",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Phase_Mach7_Re7M.jpg",
+                    "mediaType": "image/pjpeg",
                     "title": "Phase_Mach7_Re7M.jpg"
                 },
                 {
-                    "mediaType": "image/pjpeg",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Phase_Mach8_Re7M.jpg",
-                    "description": "Phase_Mach8_Re7M.jpg",
                     "@type": "dcat:Distribution",
+                    "description": "Phase_Mach8_Re7M.jpg",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Phase_Mach8_Re7M.jpg",
+                    "mediaType": "image/pjpeg",
                     "title": "Phase_Mach8_Re7M.jpg"
                 },
                 {
-                    "mediaType": "image/pjpeg",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Phase_Mach8_Re23p5M.jpg",
-                    "description": "Phase_Mach8_Re23p5M.jpg",
                     "@type": "dcat:Distribution",
+                    "description": "Phase_Mach8_Re23p5M.jpg",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Phase_Mach8_Re23p5M.jpg",
+                    "mediaType": "image/pjpeg",
                     "title": "Phase_Mach8_Re23p5M.jpg"
                 },
                 {
-                    "mediaType": "image/pjpeg",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Static_Cp_Mach7_fromDynamic.jpg",
-                    "description": "Static_Cp_Mach7_fromDynamic.jpg",
                     "@type": "dcat:Distribution",
+                    "description": "Static_Cp_Mach7_fromDynamic.jpg",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Static_Cp_Mach7_fromDynamic.jpg",
+                    "mediaType": "image/pjpeg",
                     "title": "Static_Cp_Mach7_fromDynamic.jpg"
                 },
                 {
-                    "mediaType": "image/pjpeg",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Static_Cp_Mach7_fromDynamicANDstatic.jpg",
-                    "description": "Static_Cp_Mach7_fromDynamicANDstatic.jpg",
                     "@type": "dcat:Distribution",
+                    "description": "Static_Cp_Mach7_fromDynamicANDstatic.jpg",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Static_Cp_Mach7_fromDynamicANDstatic.jpg",
+                    "mediaType": "image/pjpeg",
                     "title": "Static_Cp_Mach7_fromDynamicANDstatic.jpg"
                 },
                 {
-                    "mediaType": "image/pjpeg",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Static_Cp_Mp7_Re7M.jpg",
-                    "description": "Static_Cp_Mp7_Re7M.jpg",
                     "@type": "dcat:Distribution",
+                    "description": "Static_Cp_Mp7_Re7M.jpg",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Static_Cp_Mp7_Re7M.jpg",
+                    "mediaType": "image/pjpeg",
                     "title": "Static_Cp_Mp7_Re7M.jpg"
                 },
                 {
-                    "mediaType": "image/pjpeg",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Static_Cp_Mp8_Re7M_v2.jpg",
-                    "description": "Static_Cp_Mp8_Re7M_v2.jpg",
                     "@type": "dcat:Distribution",
+                    "description": "Static_Cp_Mp8_Re7M_v2.jpg",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Static_Cp_Mp8_Re7M_v2.jpg",
+                    "mediaType": "image/pjpeg",
                     "title": "Static_Cp_Mp8_Re7M_v2.jpg"
                 },
                 {
-                    "mediaType": "image/pjpeg",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Static_Cp_Mp8_Re23p5M.jpg",
-                    "description": "Static_Cp_Mp8_Re23p5M.jpg",
                     "@type": "dcat:Distribution",
+                    "description": "Static_Cp_Mp8_Re23p5M.jpg",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Static_Cp_Mp8_Re23p5M.jpg",
+                    "mediaType": "image/pjpeg",
                     "title": "Static_Cp_Mp8_Re23p5M.jpg"
                 },
                 {
-                    "mediaType": "image/pjpeg",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Static_Cp_Mp8_Re23p5M_v2.jpg",
-                    "description": "Static_Cp_Mp8_Re23p5M_v2.jpg",
                     "@type": "dcat:Distribution",
+                    "description": "Static_Cp_Mp8_Re23p5M_v2.jpg",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Static_Cp_Mp8_Re23p5M_v2.jpg",
+                    "mediaType": "image/pjpeg",
                     "title": "Static_Cp_Mp8_Re23p5M_v2.jpg"
                 }
             ],
-            "accrualPeriodicity": "irregular"
+            "identifier": "DASHLINK_483",
+            "issued": "2011-11-02",
+            "keyword": [
+                "ames",
+                "dashlink",
+                "nasa"
+            ],
+            "landingPage": "https://c3.nasa.gov/dashlink/resources/483/",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:029"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Dashlink"
+            },
+            "title": "HIRENASD Experimental Data, Individual Plots"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://neo.sci.gsfc.nasa.gov/",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Charles Ichoku",
+                "hasEmail": "mailto:Charles.Ichoku@nasa.gov"
+            },
+            "description": "Our mission is to help you picture climate change and environmental changes happening on our home planet. Here you can search for and retrieve satellite images of Earth. Download them; export them to GoogleEarth; perform basic analysis. Tracking regional and global changes around the world just got easier.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "ftp://neoftp.sci.gsfc.nasa.gov/rgb/",
+                    "mediaType": "image/png"
+                }
+            ],
+            "identifier": "NASA-0000087__1",
             "issued": "2018-06-25",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
             "keyword": [
                 "atmosphere",
                 "web mapping",
@@ -419022,175 +419034,172 @@
                 "energy",
                 "earth science"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Charles Ichoku",
-                "hasEmail": "mailto:Charles.Ichoku@nasa.gov"
-            },
+            "landingPage": "http://neo.sci.gsfc.nasa.gov/",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:001"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "NASA-0000087__1",
-            "description": "Our mission is to help you picture climate change and environmental changes happening on our home planet. Here you can search for and retrieve satellite images of Earth. Download them; export them to GoogleEarth; perform basic analysis. Tracking regional and global changes around the world just got easier.",
-            "title": "NASA Earth Observations (NEO)",
-            "programCode": [
-                "026:001"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "ftp://neoftp.sci.gsfc.nasa.gov/rgb/",
-                    "mediaType": "image/png"
-                }
-            ],
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "NASA Earth Observations (NEO)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/VIIRS/VNP43D84.001",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Crystal Schaaf, Zhuosen Wang, Xiaoyang Zhang, Alan Strahler\r\n. 2019-11-07. VNP43D84. Version 001. VIIRS/NPP BRDF/Albedo NBAR at Solar Noon Band M5 Daily L3 Global 30ArcSec CMG V001\r\n. Sioux Falls, South Dakota, USA. Archived by National Aeronautics and Space Administration, U.S. Government, NASA EOSDIS Land Processes Distributed Active Archive Center. https://doi.org/10.5067/VIIRS/VNP43D84.001. https://doi.org/10.5067/VIIRS/VNP43D84.001. Digital Science Data. The DOI landing page provides citations in APA and Chicago styles.\r\n.",
-            "issued": "2019-11-07",
-            "temporal": "2012-01-19T00:00:00Z/2024-05-27T00:00:00Z",
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
-            "identifier": "C1607357171-LPDAAC_ECS",
-            "description": "The NASA/ NOAA Suomi National Polar-orbiting Partnership (Suomi NPP) Visible Infrared Imaging Radiometer Suite (VIIRS) Bidirectional Reflectance Distribution Function (BRDF) and Albedo Nadir BRDF-Adjusted Reflectance (NBAR) for Band M5 (VNP43D84) is produced daily using 16 days of data at 30 arc second (1,000 meter) resolution. Data are temporally weighted to the ninth day, which is reflected in the file name. The VNP43D product suite is provided in a Climate Modeling Grid (CMG), which covers the entire globe for use in climate simulation models. Due to the large file size, each VNP43D product contains just one data layer. \r\n\r\nVNP43D80 through VNP43D89 are the NBAR products of the VNP43D BRDF/Albedo product suite. NBAR values are provided for the nine VIIRS moderate resolution bands (M1 through M5, M7, M8, M10, and M11) included in the VNP43MA4 (https://doi.org/10.5067/VIIRS/VNP43MA4.001) product. In addition to the bands included in VNP43MA4, this product suite includes NBAR values for the VIIRS Day/Night Band (DNB). The NBAR algorithm removes view angle effects from directional reflectances to model the values as if they were collected from a nadir view at local solar noon. Details regarding methodology are available on the VNP43MA4 product page and in the Algorithm Theoretical Basis Document (ATBD).\r\n\r\nVNP43D84 is the NBAR for VIIRS band M5 (0.672 \u03bcm).",
-            "release-place": "Sioux Falls, South Dakota, USA",
-            "series-name": "VNP43D84",
             "creator": "Crystal Schaaf, Zhuosen Wang, Xiaoyang Zhang, Alan Strahler",
-            "title": "VIIRS/NPP BRDF/Albedo NBAR at Solar Noon Band M5 Daily L3 Global 30ArcSec CMG V001",
-            "programCode": [
-                "026:001"
-            ],
+            "data-presentation-form": "Digital Science Data",
+            "description": "The NASA/ NOAA Suomi National Polar-orbiting Partnership (Suomi NPP) Visible Infrared Imaging Radiometer Suite (VIIRS) Bidirectional Reflectance Distribution Function (BRDF) and Albedo Nadir BRDF-Adjusted Reflectance (NBAR) for Band M5 (VNP43D84) is produced daily using 16 days of data at 30 arc second (1,000 meter) resolution. Data are temporally weighted to the ninth day, which is reflected in the file name. The VNP43D product suite is provided in a Climate Modeling Grid (CMG), which covers the entire globe for use in climate simulation models. Due to the large file size, each VNP43D product contains just one data layer. \r\n\r\nVNP43D80 through VNP43D89 are the NBAR products of the VNP43D BRDF/Albedo product suite. NBAR values are provided for the nine VIIRS moderate resolution bands (M1 through M5, M7, M8, M10, and M11) included in the VNP43MA4 (https://doi.org/10.5067/VIIRS/VNP43MA4.001) product. In addition to the bands included in VNP43MA4, this product suite includes NBAR values for the VIIRS Day/Night Band (DNB). The NBAR algorithm removes view angle effects from directional reflectances to model the values as if they were collected from a nadir view at local solar noon. Details regarding methodology are available on the VNP43MA4 product page and in the Algorithm Theoretical Basis Document (ATBD).\r\n\r\nVNP43D84 is the NBAR for VIIRS band M5 (0.672 \u03bcm).",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FVIIRS%2FVNP43D84.001",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FVIIRS%2FVNP43D84.001",
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
-                    "downloadURL": "https://doi.org/10.5067/VIIRS/VNP43D84.001",
-                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
+                    "downloadURL": "https://doi.org/10.5067/VIIRS/VNP43D84.001",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/xhdf5",
-                    "downloadURL": "https://e4ftl01.cr.usgs.gov/VIIRS/VNP43D84.001/",
-                    "description": "LP DAAC Data Pool provides direct access to available products via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "LP DAAC Data Pool provides direct access to available products via HTTPS.",
+                    "downloadURL": "https://e4ftl01.cr.usgs.gov/VIIRS/VNP43D84.001/",
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
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=C1607357171-LPDAAC_ECS",
-                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=C1607357171-LPDAAC_ECS",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://opendap.cr.usgs.gov/opendap/hyrax/VNP43D84.001/contents.html",
-                    "description": "Access data via Open-source Project for a Network Data Access Protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access data via Open-source Project for a Network Data Access Protocol.",
+                    "downloadURL": "https://opendap.cr.usgs.gov/opendap/hyrax/VNP43D84.001/contents.html",
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
-                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/filespec/VIIRS/1/VNP43D84",
-                    "description": "The File Specification provides a description of the product file including Scientific Data Sets and their attributes.",
                     "@type": "dcat:Distribution",
+                    "description": "The File Specification provides a description of the product file including Scientific Data Sets and their attributes.",
+                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/filespec/VIIRS/1/VNP43D84",
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
+            "identifier": "C1607357171-LPDAAC_ECS",
+            "issued": "2019-11-07",
+            "keyword": [
+                "surface radiative properties",
+                "earth science",
+                "land surface"
+            ],
+            "landingPage": "https://doi.org/10.5067/VIIRS/VNP43D84.001",
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
+            "series-name": "VNP43D84",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2012-01-19T00:00:00Z/2024-05-27T00:00:00Z",
             "theme": [
                 "NPP-JPSS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "VIIRS/NPP BRDF/Albedo NBAR at Solar Noon Band M5 Daily L3 Global 30ArcSec CMG V001"
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
+                    "downloadURL": "http://appel.nasa.gov/wp-content/uploads/sites/2/2013/04/384151main_Viking_GCMS_case_study.pdf",
+                    "mediaType": "application/pdf"
+                }
             ],
+            "identifier": "NASA-865__12",
+            "issued": "2018-06-25",
             "keyword": [
                 "sharing",
                 "case studies",
@@ -419199,489 +419208,482 @@
                 "management",
                 "knowledge"
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
-            "identifier": "NASA-865__12",
-            "description": "Case studies illustrate the kinds of decisions and dilemmas managers face every day, and as such provide an effective learning tool for project management. Due to the dynamic and complex environment of projects, a great deal of project management knowledge is tacit and hard to formalize. A case study captures the complex nature of a project and identifies key decision points, allowing the reader an inside look at the project from a practitioner\u2019s point of view.",
-            "title": "Academy of Program/Project & Engineering Leadership: APPEL Case Studies",
-            "programCode": [
-                "026:045"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://appel.nasa.gov/wp-content/uploads/sites/2/2013/04/384151main_Viking_GCMS_case_study.pdf",
-                    "mediaType": "application/pdf"
-                }
+            "references": [
+                "http://km.nasa.gov/knowledge-map/"
             ],
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Management/Operations"
-            ]
+            ],
+            "title": "Academy of Program/Project & Engineering Leadership: APPEL Case Studies"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=GO-L-NIMS-3-TUBE-V1.0",
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
-                "galileo"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "Unknown",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.go-l-nims-3-tube-v1.0_9f87-p6qx",
+            "issued": "2018-06-26",
+            "keyword": [
+                "moon",
+                "galileo"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=GO-L-NIMS-3-TUBE-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.go-l-nims-3-tube-v1.0_9f87-p6qx",
-            "description": "Unknown",
-            "title": "NIMS SPECTRAL IMAGE TUBES OF THE MOON: E1 & E2 ENCOUNTERS",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "NIMS SPECTRAL IMAGE TUBES OF THE MOON: E1 & E2 ENCOUNTERS"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-3-RDR-TRIAD-POLARIMETRY-V2.1",
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
+            "description": "Asteroid polarimatetry from the TRIAD database.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-3-rdr-triad-polarimetry-v2.1_9fds-r6zq",
+            "issued": "2021-05-21",
+            "keyword": [
+                "support archives",
+                "asteroid"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-3-RDR-TRIAD-POLARIMETRY-V2.1",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-3-rdr-triad-polarimetry-v2.1_9fds-r6zq",
-            "description": "Asteroid polarimatetry from the TRIAD database.",
-            "title": "TRIAD ASTEROID POLARIMETRY V2.1",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "TRIAD ASTEROID POLARIMETRY V2.1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/SeaBASS/SFP/DATA001",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/GSFC/SED/ESD/GCDC/OB.DAAC. https://doi.org/10.5067/SeaBASS/SFP/DATA001.",
-            "issued": "2012-02-27",
-            "temporal": "2012-02-27T16:09:00Z/2023-04-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-04-06",
-            "keyword": [
-                "oceans",
-                "ocean temperature",
-                "salinity/density",
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
-            "identifier": "C1633360659-OB_DAAC",
             "description": "South Florida Program (SFP)",
-            "title": "South Florida Program (SFP)",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSeaBASS%2FSFP%2FDATA001",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSeaBASS%2FSFP%2FDATA001",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://seabass.gsfc.nasa.gov/experiment/SFP/",
-                    "description": "Detailed information about the SeaBASS Experiment such as cruises, funding, and investigators",
                     "@type": "dcat:Distribution",
+                    "description": "Detailed information about the SeaBASS Experiment such as cruises, funding, and investigators",
+                    "downloadURL": "https://seabass.gsfc.nasa.gov/experiment/SFP/",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 }
             ],
+            "identifier": "C1633360659-OB_DAAC",
+            "issued": "2012-02-27",
+            "keyword": [
+                "oceans",
+                "ocean temperature",
+                "salinity/density",
+                "earth science",
+                "ocean chemistry",
+                "ocean optics"
+            ],
+            "landingPage": "https://doi.org/10.5067/SeaBASS/SFP/DATA001",
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
+            "temporal": "2012-02-27T16:09:00Z/2023-04-17T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "South Florida Program (SFP)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1432636966-GES_DISC.html",
             "citation": "Oxford University AOPP. 2017-10-31. SCRN5L1RAD_CDROM. Version 001. SCR/Nimbus-5 Level 1 Radiance Data from CD-ROM V001. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://disc.gsfc.nasa.gov/datacollection/SCRN5L1RAD_CDROM_001.html. Digital Science Data.",
-            "issued": "1998-03-02",
-            "temporal": "1974-12-12T00:00:00Z/1978-04-20T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "1998-03-02",
-            "references": [
-                "https://doi.org/10.1098/rspa.1973.0085"
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
-            "identifier": "C1432636966-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "SCRN5L1RAD_CDROM is the gridded Nimbus-5 Selective Chopper Radiometer (SCR) Level 1 Radiance Data Product. The radiances are measured by 16 channels at 2.3 to 15 micrometers with a ground resolution of 25 km. This product contains corrected and uncorrected radiances in a daily 4 degree latitude x 10 degree longitude grid format, as well as the original orbit format and reformatted copies of the original tapes. This was the follow-on to the SCR experiment flown on Nimbus-4. The data for this product are available from 13 December 1972 to 20 April 1978. The principal investigator for the SCR experiment was Dr. John T. Houghton from Oxford University.\n\nThis product was created by the Oxford University's Atmospheric, Oceanic and Planetary Physics (AOPP) group. The data are stored on a set of 28 CD-ROMs in ASCII files of hexadecimal characters, and are available in gzipped Unix tar archive files. The first CD-ROM contains the gridded radiance data and a few original tape data files, the subsequent CD-ROMs contain the remaining compressed copies of the original data tapes. The byte-ordering in the data files follows the DEC convention for 16-bit integers of less significant byte first. Normal 2's complement integer storage is assumed.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "SCRN5L1RAD_CDROM",
-            "creator": "Oxford University AOPP",
-            "graphic-preview-description": "Northern hemisphere radiance field (in ergs) for January 1973 derived from SCR channel B1B2 data (about 1.6 mb or 45 km).",
-            "title": "SCR/Nimbus-5 Level 1 Radiance Data from CD-ROM V001 (SCRN5L1RAD_CDROM) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Nimbus/images/N5SCR_sample.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Nimbus/images/N5SCR_sample.png",
-                    "description": "Northern hemisphere radiance field (in ergs) for January 1973 derived from SCR channel B1B2 data (about 1.6 mb or 45 km).",
                     "@type": "dcat:Distribution",
+                    "description": "Northern hemisphere radiance field (in ergs) for January 1973 derived from SCR channel B1B2 data (about 1.6 mb or 45 km).",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Nimbus/images/N5SCR_sample.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/SCRN5L1RAD_CDROM_001.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/SCRN5L1RAD_CDROM_001.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/Nimbus5_SCR_Level1/SCRN5L1RAD_CDROM.001/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/Nimbus5_SCR_Level1/SCRN5L1RAD_CDROM.001/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=SCRN5L1RAD_CDROM",
-                    "description": "Use the Earthdata Search Client to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search Client to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=SCRN5L1RAD_CDROM",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/Nimbus5_SCR_Level1/SCRN5L1RAD_CDROM.001/doc/README.SCRN5L1RAD_CDROM_001.txt",
-                    "description": "README Document",
                     "@type": "dcat:Distribution",
+                    "description": "README Document",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/Nimbus5_SCR_Level1/SCRN5L1RAD_CDROM.001/doc/README.SCRN5L1RAD_CDROM_001.txt",
+                    "mediaType": "text/html",
                     "title": "View this dataset's read me document"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/repository/Mission/Nimbus/3.3_Product_Documentation/3.3.5_Product_Quality/N5_Users_Guide.pdf",
-                    "description": "Nimbus 5 User's Guide",
                     "@type": "dcat:Distribution",
+                    "description": "Nimbus 5 User's Guide",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/repository/Mission/Nimbus/3.3_Product_Documentation/3.3.5_Product_Quality/N5_Users_Guide.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
                 },
                 {
-                    "mediaType": "application/gzip",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/repository/Mission/Nimbus/3.3_Product_Documentation/3.3.5_Product_Quality/DataCatalogNimbus5.tar.gz",
-                    "description": "Nimbus 5 Data Catalog",
                     "@type": "dcat:Distribution",
+                    "description": "Nimbus 5 Data Catalog",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/repository/Mission/Nimbus/3.3_Product_Documentation/3.3.5_Product_Quality/DataCatalogNimbus5.tar.gz",
+                    "mediaType": "application/gzip",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "graphic-preview-description": "Northern hemisphere radiance field (in ergs) for January 1973 derived from SCR channel B1B2 data (about 1.6 mb or 45 km).",
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Nimbus/images/N5SCR_sample.png",
+            "identifier": "C1432636966-GES_DISC",
+            "issued": "1998-03-02",
+            "keyword": [
+                "infrared wavelengths",
+                "spectral/engineering",
+                "earth science"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1432636966-GES_DISC.html",
+            "language": [
+                "en-US"
+            ],
+            "modified": "1998-03-02",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
+            },
+            "references": [
+                "https://doi.org/10.1098/rspa.1973.0085"
+            ],
+            "release-place": "Greenbelt, MD, USA",
+            "series-name": "SCRN5L1RAD_CDROM",
             "spatial": "-180.0 -80.0 180.0 80.0",
+            "temporal": "1974-12-12T00:00:00Z/1978-04-20T23:59:59.999Z",
             "theme": [
                 "Nimbus",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "SCR/Nimbus-5 Level 1 Radiance Data from CD-ROM V001 (SCRN5L1RAD_CDROM) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/GPMGV/GCPEX/GOES-IM/DATA301",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Hall, John .2014. GPM GROUND VALIDATION GOES 13 VISIBLE AND INFRARED IMAGES GCPEX [indicate subset used]. Dataset available online from the NASA Global Hydrometeorology Resource Center DAAC, Huntsville, Alabama, U.S.A. DOI: http://dx.doi.org/10.5067/GPMGV/GCPEX/GOES-IM/DATA301",
-            "issued": "2014-01-14",
-            "temporal": "2012-01-01T00:15:00Z/2012-03-14T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-05-23",
-            "keyword": [
-                "infrared wavelengths",
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
-            "identifier": "C1981574739-GHRC_DAAC",
             "description": "The GPM Ground Validation GOES 13 Visible and Infrared Images GCPEx dataset was produced and archived in near real time at the Global Hydrology Resource Center throughout the GPM Cold-Season Precipitation Experiment (GCPEx). These image files were created for use with the Real Time Mission Monitor (RTMM). Generally, GOES-13 images are available for all dates between January 1, 2012 and March 13, 2012 at 15 minute intervals. The GPM Ground Validation GOES-13 Visible and Infrared Images dataset files are available in PNG format and contain images over the MC3E campaign area.",
-            "title": "GPM GROUND VALIDATION GOES 13 VISIBLE AND INFRARED IMAGES GCPEX V1",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGPMGV%2FGCPEX%2FGOES-IM%2FDATA301",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGPMGV%2FGCPEX%2FGOES-IM%2FDATA301",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=gpmgoes13gcpexB",
-                    "description": "Files may be downloaded directly to your workstation from this link",
                     "@type": "dcat:Distribution",
+                    "description": "Files may be downloaded directly to your workstation from this link",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=gpmgoes13gcpexB",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://ghrc.nsstc.nasa.gov/uso/ds_docs/gpmgv/goes/gpmgoes13_dataset.html",
-                    "description": "The guide document contains detailed information about the dataset",
                     "@type": "dcat:Distribution",
+                    "description": "The guide document contains detailed information about the dataset",
+                    "downloadURL": "http://ghrc.nsstc.nasa.gov/uso/ds_docs/gpmgv/goes/gpmgoes13_dataset.html",
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
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/home/about-ghrc/citing-ghrc-daac-data",
-                    "description": "Instructions for citing GHRC data",
                     "@type": "dcat:Distribution",
+                    "description": "Instructions for citing GHRC data",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/home/about-ghrc/citing-ghrc-daac-data",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C1981574739-GHRC_DAAC",
+            "issued": "2014-01-14",
+            "keyword": [
+                "infrared wavelengths",
+                "earth science",
+                "visible wavelengths",
+                "spectral/engineering"
+            ],
+            "landingPage": "https://doi.org/10.5067/GPMGV/GCPEX/GOES-IM/DATA301",
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
             "spatial": "-120.0 -90.0 -20.0 90.0",
+            "temporal": "2012-01-01T00:15:00Z/2012-03-14T00:00:00Z",
             "theme": [
                 "GCPEx",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "GPM GROUND VALIDATION GOES 13 VISIBLE AND INFRARED IMAGES GCPEX V1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.7927/hvgh-g750",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Center for International Earth Science Information Network - CIESIN - Columbia University. 2023-12-31. Natural Resource Protection and Child Health Indicators, 2023 Release. Version 2023.00. Palisades, NY. Archived by National Aeronautics and Space Administration, U.S. Government, NASA Socioeconomic Data and Applications Center (SEDAC). https://doi.org/10.7927/hvgh-g750. https://doi.org/10.7927/hvgh-g750.",
-            "issued": "2023-12-31",
-            "temporal": "2010-01-01T00:00:00Z/2022-12-31T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-12-31",
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
-                "https://doi.org/10.7927/7ppx-6m60",
-                "https://doi.org/10.7927/5bbs-e174",
-                "https://doi.org/10.7927/70tj-g487",
-                "https://doi.org/10.7927/ddww-mp73"
-            ],
-            "keyword": [
-                "public health",
-                "human dimensions",
-                "earth science",
-                "environmental impacts",
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
-            "identifier": "C2905539824-SEDAC",
-            "description": "The Natural Resource Protection and Child Health Indicators, 2023 Release, is produced in support of the U.S. Millennium Challenge Corporation as selection criteria for funding eligibility. The Natural Resource Protection Indicator (NRPI) and Child Health Indicator (CHI) are based on proximity-to-target scores ranging from 0 to 100 (at target). The NRPI covers 76 countries which are eligible for MCC funding and is using the 2022 Environmental Performance Index. The CHI is a composite index for 198 countries derived from the average of three proximity-to-target scores for at least basic access to water, at least basic access to sanitation, and child mortality rates. The 2023 release includes a consistent time series of NRPI scores for 2019 to 2022 and CHI scores for 2010 to 2022.",
-            "release-place": "Palisades, NY",
-            "graphic-preview-description": "Sample browse graphic of the data set.",
             "creator": "Center for International Earth Science Information Network - CIESIN - Columbia University",
-            "title": "Natural Resource Protection and Child Health Indicators, 2023 Release",
-            "graphic-preview-file": "https://sedac.ciesin.columbia.edu/downloads/maps/nrmi/nrmi-natural-resource-protection-child-health-indicators-2023/sedac-logo.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The Natural Resource Protection and Child Health Indicators, 2023 Release, is produced in support of the U.S. Millennium Challenge Corporation as selection criteria for funding eligibility. The Natural Resource Protection Indicator (NRPI) and Child Health Indicator (CHI) are based on proximity-to-target scores ranging from 0 to 100 (at target). The NRPI covers 76 countries which are eligible for MCC funding and is using the 2022 Environmental Performance Index. The CHI is a composite index for 198 countries derived from the average of three proximity-to-target scores for at least basic access to water, at least basic access to sanitation, and child mortality rates. The 2023 release includes a consistent time series of NRPI scores for 2019 to 2022 and CHI scores for 2010 to 2022.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.7927%2Fhvgh-g750",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.7927%2Fhvgh-g750",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/downloads/maps/nrmi/nrmi-natural-resource-protection-child-health-indicators-2023/sedac-logo.jpg",
-                    "description": "Sample browse graphic of the data set.",
                     "@type": "dcat:Distribution",
+                    "description": "Sample browse graphic of the data set.",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/downloads/maps/nrmi/nrmi-natural-resource-protection-child-health-indicators-2023/sedac-logo.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/nrmi-natural-resource-protection-child-health-indicators-2023/data-download",
-                    "description": "Data Download Page",
                     "@type": "dcat:Distribution",
+                    "description": "Data Download Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/nrmi-natural-resource-protection-child-health-indicators-2023/data-download",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://sedac.ciesin.columbia.edu/data/set/nrmi-natural-resource-protection-child-health-indicators-2023/docs",
-                    "description": "Documentation Page",
                     "@type": "dcat:Distribution",
+                    "description": "Documentation Page",
+                    "downloadURL": "http://sedac.ciesin.columbia.edu/data/set/nrmi-natural-resource-protection-child-health-indicators-2023/docs",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/nrmi-natural-resource-protection-child-health-indicators-2023",
-                    "description": "Data Set\u00a0Overview Page",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set\u00a0Overview Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/nrmi-natural-resource-protection-child-health-indicators-2023",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "graphic-preview-description": "Sample browse graphic of the data set.",
+            "graphic-preview-file": "https://sedac.ciesin.columbia.edu/downloads/maps/nrmi/nrmi-natural-resource-protection-child-health-indicators-2023/sedac-logo.jpg",
+            "identifier": "C2905539824-SEDAC",
+            "issued": "2023-12-31",
+            "keyword": [
+                "public health",
+                "human dimensions",
+                "earth science",
+                "environmental impacts",
+                "sustainability"
+            ],
+            "landingPage": "https://doi.org/10.7927/hvgh-g750",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2023-12-31",
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
+                "https://doi.org/10.7927/7ppx-6m60",
+                "https://doi.org/10.7927/5bbs-e174",
+                "https://doi.org/10.7927/70tj-g487",
+                "https://doi.org/10.7927/ddww-mp73"
+            ],
+            "release-place": "Palisades, NY",
             "spatial": "-180.0 -55.0 180.0 90.0",
+            "temporal": "2010-01-01T00:00:00Z/2022-12-31T00:00:00Z",
             "theme": [
                 "NRMI",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Natural Resource Protection and Child Health Indicators, 2023 Release"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-J-SDC-2-JUPITER-V1.0",
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
-                "new horizons"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This data set contains Raw data taken by the New Horizons Student Dust Counter instrument during the Jupiter encounter mission phase.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-j-sdc-2-jupiter-v1.0_9fkj-vtmi",
+            "issued": "2018-06-26",
+            "keyword": [
+                "dust",
+                "new horizons"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-J-SDC-2-JUPITER-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-j-sdc-2-jupiter-v1.0_9fkj-vtmi",
-            "description": "This data set contains Raw data taken by the New Horizons Student Dust Counter instrument during the Jupiter encounter mission phase.",
-            "title": "NEW HORIZONS SDC JUPITER ENCOUNTER V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "NEW HORIZONS SDC JUPITER ENCOUNTER V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=CO-S-CIRS-5-CUBES-V2.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This data set comprises uncalibrated\nand calibrated data from the Cassini Composite Infrared Spectrometer\n(CIRS) instrument. The basic data is comprised of uncalibrated raw spectra,\nalong with along with pointing and geometry information, and\nhousekeeping information. Also included are calibrated power spectra,\nand documentation.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.co-s-cirs-5-cubes-v2.0_9fme-qz4j",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "phoebe",
                 "prometheus",
@@ -419705,586 +419707,586 @@
                 "titan",
                 "pan"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=CO-S-CIRS-5-CUBES-V2.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.co-s-cirs-5-cubes-v2.0_9fme-qz4j",
-            "description": "This data set comprises uncalibrated\nand calibrated data from the Cassini Composite Infrared Spectrometer\n(CIRS) instrument. The basic data is comprised of uncalibrated raw spectra,\nalong with along with pointing and geometry information, and\nhousekeeping information. Also included are calibrated power spectra,\nand documentation.",
-            "title": "CASSINI SATURN CIRS CUBES\n                                      RECORDS V2.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "CASSINI SATURN CIRS CUBES\n                                      RECORDS V2.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-COMPIL-5-BINMP-V7.0",
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
+            "description": "The data set lists orbital and physical properties for well-observed or suspected binary/multiple minor planets including the Pluto system, compiled from the published literature as inspired by Richardson and Walsh (2006) and similar reviews (Merline et al., 2003; Noll, 2006; Pravec et al., 2006; Pravec and Harris, 2007; Descamps and Marchis, 2008; Noll et al., 2008; Walsh, 2009). In total 256 companions in 242 systems are included. Data are presented in three tables: one for orbital and physical properties; one for companion designations, discovery information, and reference codes for data values; and one giving full references for each reference code. This data set is complete for binary/multiple components reported through 31 March 2014.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-compil-5-binmp-v7.0_9fpq-pabw",
+            "issued": "2021-05-21",
+            "keyword": [
+                "support archives",
+                "asteroid"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-COMPIL-5-BINMP-V7.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-compil-5-binmp-v7.0_9fpq-pabw",
-            "description": "The data set lists orbital and physical properties for well-observed or suspected binary/multiple minor planets including the Pluto system, compiled from the published literature as inspired by Richardson and Walsh (2006) and similar reviews (Merline et al., 2003; Noll, 2006; Pravec et al., 2006; Pravec and Harris, 2007; Descamps and Marchis, 2008; Noll et al., 2008; Walsh, 2009). In total 256 companions in 242 systems are included. Data are presented in three tables: one for orbital and physical properties; one for companion designations, discovery information, and reference codes for data values; and one giving full references for each reference code. This data set is complete for binary/multiple components reported through 31 March 2014.",
-            "title": "BINARY MINOR PLANETS V7.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "BINARY MINOR PLANETS V7.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/A1E1EWIHPHAO",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "SMEX03 Vegetation Data: Oklahoma, Version 1. Version 1. Archived by National Aeronautics and Space Administration, U.S. Government, NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/A1E1EWIHPHAO.",
-            "issued": "2003-07-01",
-            "temporal": "2003-07-01T00:00:00Z/2003-07-18T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2003-07-18",
-            "keyword": [
-                "biosphere",
-                "earth science",
-                "vegetation"
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
-            "identifier": "C1386204215-NSIDCV0",
             "description": "This data set contains various vegetation parameters for several locations from Oklahoma North (ON) and Oklahoma South (OS).",
-            "title": "SMEX03 Vegetation Data: Oklahoma, Version 1",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FA1E1EWIHPHAO",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FA1E1EWIHPHAO",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/AVDM/data/soil_moisture/SMEX03/Oklahoma/vegetation/regional_watershed/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/AVDM/data/soil_moisture/SMEX03/Oklahoma/vegetation/regional_watershed/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/AVDM/data/soil_moisture/SMEX03/Oklahoma/vegetation/regional_watershed/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/AVDM/data/soil_moisture/SMEX03/Oklahoma/vegetation/regional_watershed/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/A1E1EWIHPHAO",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/A1E1EWIHPHAO",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/A1E1EWIHPHAO",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/A1E1EWIHPHAO",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C1386204215-NSIDCV0",
+            "issued": "2003-07-01",
+            "keyword": [
+                "biosphere",
+                "earth science",
+                "vegetation"
+            ],
+            "landingPage": "https://doi.org/10.5067/A1E1EWIHPHAO",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2003-07-18",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA NSIDC DAAC"
+            },
             "spatial": "-98.3 34.8 -97.6 35.9",
+            "temporal": "2003-07-01T00:00:00Z/2003-07-18T23:59:59.999Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "SMEX03 Vegetation Data: Oklahoma, Version 1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC1-0634-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 1 phase 2014-11-20 to 2015-03-10. It is a Global Gravity measurement at the comet 67P and covers the time 2015-03-10T13:46:00.000 to 2015-03-10T15:57:40.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc1-0634-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC1-0634-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc1-0634-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 1 phase 2014-11-20 to 2015-03-10. It is a Global Gravity measurement at the comet 67P and covers the time 2015-03-10T13:46:00.000 to 2015-03-10T15:57:40.000.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 1 0634 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 1 0634 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/Terra/MISR/MIL3DCFA_L3.001",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "The data used in this study were produced by the MISR Science Team;processed/stored at the Langley DAAC;Product is the MISR Level 3 Cloud Fraction by Altitude Product for a day;See ProductionDateTime for Published date.",
-            "issued": "2010-04-27",
-            "temporal": "1999-12-18T00:00:00Z/2022-01-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2017-10-26",
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
-            "identifier": "C188637668-LARC",
             "description": "This file contains the public MISR Level 3 Cloud Fraction by Altitude Product covering a day",
-            "graphic-preview-description": "ASDC List of MISR Imagery and Articles",
-            "title": "MISR Level 3 Cloud Fraction by Altitude Product covering a day V001",
-            "graphic-preview-file": "https://asdc.larc.nasa.gov/documents/misr/imagery.html",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FTerra%2FMISR%2FMIL3DCFA_L3.001",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FTerra%2FMISR%2FMIL3DCFA_L3.001",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 }
             ],
+            "graphic-preview-description": "ASDC List of MISR Imagery and Articles",
+            "graphic-preview-file": "https://asdc.larc.nasa.gov/documents/misr/imagery.html",
+            "identifier": "C188637668-LARC",
+            "issued": "2010-04-27",
+            "keyword": [
+                "nasa"
+            ],
+            "landingPage": "https://doi.org/10.5067/Terra/MISR/MIL3DCFA_L3.001",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2017-10-26",
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
+            "title": "MISR Level 3 Cloud Fraction by Altitude Product covering a day V001"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/Terra/MISR/MI3DLSR_L3.002",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2006-03-13. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/Terra/MISR/MI3DLSR_L3.002. https://asdc.larc.nasa.gov/project/MISR.",
-            "issued": "2006-02-13",
-            "temporal": "2002-03-29T00:00:00Z/2007-08-30T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2019-06-19",
-            "keyword": [
-                "land surface",
-                "atmosphere",
-                "atmospheric radiation",
-                "biosphere",
-                "earth science",
-                "land use/land cover",
-                "vegetation"
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
-            "identifier": "C179031511-LARC",
             "description": "MI3DLSR_2 is the Multi-angle Imaging SpectroRadiometer (MISR) Level 3 Component Global Land Regional public Product covering a dayversion 2. It contains a daily statistical summary of directional hemispherical reflectance (DHR), photosynthetically active spectral region (DHR-PAR), DHR for near-infrared band (DHR-NIR), fractional absorbed photosynthetically active radiation (FPAR), DHR-based normalized difference vegetation index (NDVI) and land surface bidirectional reflectance factor (BRF) model parameters. It is classified into six vegetated and one non-vegetated types. This data product is a global summary of the Level 2 land/surface parameters of interest averaged over a day and reported on a geographic grid, with resolution of 0.5 degree by 0.5 degree. Data collection for this product is complete. The data are for distinct regions associated with associated field campaigns. The MISR instrument consists of nine pushbroom cameras which measure radiance in four spectral bands. Global coverage is achieved in nine days. The cameras are arranged with one camera pointing toward the nadir, four cameras pointing forward, and four cameras pointing aftward. It takes seven minutes for all nine cameras to view the same surface location. The view angles relative to the surface reference ellipsoid, are 0, 26.1, 45.6, 60.0, and 70.5 degrees. The spectral band shapes are nominally Gaussian, centered at 443, 555, 670, and 865 nm.",
-            "graphic-preview-description": "ASDC List of MISR Imagery and Articles",
-            "title": "MISR Level 3 Component Global Land Regional public Product covering a day V002",
-            "graphic-preview-file": "https://asdc.larc.nasa.gov/documents/misr/imagery.html",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FTerra%2FMISR%2FMI3DLSR_L3.002",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FTerra%2FMISR%2FMI3DLSR_L3.002",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
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
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C179031511-LARC",
-                    "description": "Earthdata Search for MI3DLSR_2 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for MI3DLSR_2 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C179031511-LARC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/MISR/MI3DLSR.002/contents.html",
-                    "description": "OPeNDAP data access for MI3DLSR_2",
                     "@type": "dcat:Distribution",
+                    "description": "OPeNDAP data access for MI3DLSR_2",
+                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/MISR/MI3DLSR.002/contents.html",
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
-                    "downloadURL": "https://doi.org/10.5067/Terra/MISR/MI3DLSR_L3.002",
-                    "description": "DOI data set landing page for MI3DLSR_2",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for MI3DLSR_2",
+                    "downloadURL": "https://doi.org/10.5067/Terra/MISR/MI3DLSR_L3.002",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
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
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/MISR/MI3DLSR.002/",
-                    "description": "ASDC Direct Data Download for MI3DLSR_2",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for MI3DLSR_2",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/MISR/MI3DLSR.002/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/misr/DPS_CGLS_V032.20180125.pdf",
-                    "description": "Data Product Specification for the MISR Level 3 Component Global Land Surface Product - Incorporating the Science Data Processing Interface Control Document",
                     "@type": "dcat:Distribution",
+                    "description": "Data Product Specification for the MISR Level 3 Component Global Land Surface Product - Incorporating the Science Data Processing Interface Control Document",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/misr/DPS_CGLS_V032.20180125.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's product usage"
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
+            "identifier": "C179031511-LARC",
+            "issued": "2006-02-13",
+            "keyword": [
+                "land surface",
+                "atmosphere",
+                "atmospheric radiation",
+                "biosphere",
+                "earth science",
+                "land use/land cover",
+                "vegetation"
+            ],
+            "landingPage": "https://doi.org/10.5067/Terra/MISR/MI3DLSR_L3.002",
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
+            "temporal": "2002-03-29T00:00:00Z/2007-08-30T23:59:59Z",
             "theme": [
                 "MISR",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "MISR Level 3 Component Global Land Regional public Product covering a day V002"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-X-MVIC-2-PLUTOCRUISE-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This data set contains Raw data taken by the New Horizons                Multispectral Visible Imaging Camera                                   instrument during the                                                    pluto cruise                                                           mission phase.  This is VERSION 1.0 of this data set.                    The spacecraft was in hibernation for much of the Pluto Cruise             mission phase, and the focus for RALPH (MVIC and LEISA) during             Annual CheckOuts one through four (ACO1-4) was preparation for the         Pluto Encounter in 2015, including functional tests, and calibrations.     Science observations performed during this phase included Uranus and       Neptune at phase angles (44 degrees and 34 degrees, respectively) not      available from Earth (MVIC), calibrations with Neptune as a navigation     test target (MVIC), Sun in the Solar Illumination Assembly (SIA) (MVIC     and LEISA), the M6 and M7 clusters (MVIC), and other                       calibrations (stray light, dark, interference with other instruments).",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-x-mvic-2-plutocruise-v1.0_9fu2-6tba",
             "issued": "2018-09-05",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "neptune",
                 "uranus",
@@ -420294,38 +420296,38 @@
                 "sun",
                 "calibration"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-X-MVIC-2-PLUTOCRUISE-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-x-mvic-2-plutocruise-v1.0_9fu2-6tba",
-            "description": "This data set contains Raw data taken by the New Horizons                Multispectral Visible Imaging Camera                                   instrument during the                                                    pluto cruise                                                           mission phase.  This is VERSION 1.0 of this data set.                    The spacecraft was in hibernation for much of the Pluto Cruise             mission phase, and the focus for RALPH (MVIC and LEISA) during             Annual CheckOuts one through four (ACO1-4) was preparation for the         Pluto Encounter in 2015, including functional tests, and calibrations.     Science observations performed during this phase included Uranus and       Neptune at phase angles (44 degrees and 34 degrees, respectively) not      available from Earth (MVIC), calibrations with Neptune as a navigation     test target (MVIC), Sun in the Solar Illumination Assembly (SIA) (MVIC     and LEISA), the M6 and M7 clusters (MVIC), and other                       calibrations (stray light, dark, interference with other instruments).",
-            "title": "NEW HORIZONS                            \n      MVIC PLUTO CRUISE                                                       \n      RAW V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "NEW HORIZONS                            \n      MVIC PLUTO CRUISE                                                       \n      RAW V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-J-LORRI-3-JUPITER-V1.1",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This data set contains Calibrated data taken by the New Horizons Long Range Reconnaissance Imager instrument during the Jupiter encounter mission phase.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-j-lorri-3-jupiter-v1.1_9fw5-et8x",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "calibration",
                 "callisto",
@@ -420339,273 +420341,243 @@
                 "j7 elara",
                 "j6 himalia"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-J-LORRI-3-JUPITER-V1.1",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-j-lorri-3-jupiter-v1.1_9fw5-et8x",
-            "description": "This data set contains Calibrated data taken by the New Horizons Long Range Reconnaissance Imager instrument during the Jupiter encounter mission phase.",
-            "title": "NEW HORIZONS LORRI JUPITER ENCOUNTER V1.1",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "NEW HORIZONS LORRI JUPITER ENCOUNTER V1.1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-A-SDC-2-KEM1-V1.0",
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
-                "dust",
-                "new horizons kuiper belt extended mission"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This data set contains Raw data taken by the New Horizons Student Dust Counter instrument during the KEM1 ENCOUNTER mission phase. This is VERSION 1.0 of this data set. This data set contains data acquired by the spacecraft between 08/14/2018 and 12/31/2018. It only includes data downlinked before 01/01/2019. Future datasets may include more data acquired by the spacecraft after 08/13/2018 but downlinked after 12/31/2018.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-a-sdc-2-kem1-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "dust",
+                "new horizons kuiper belt extended mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-A-SDC-2-KEM1-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-a-sdc-2-kem1-v1.0",
-            "description": "This data set contains Raw data taken by the New Horizons Student Dust Counter instrument during the KEM1 ENCOUNTER mission phase. This is VERSION 1.0 of this data set. This data set contains data acquired by the spacecraft between 08/14/2018 and 12/31/2018. It only includes data downlinked before 01/01/2019. Future datasets may include more data acquired by the spacecraft after 08/13/2018 but downlinked after 12/31/2018.",
-            "title": "NEW HORIZONS\n      SDC KEM1\n      RAW V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "NEW HORIZONS\n      SDC KEM1\n      RAW V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG2-U-UVS-3-RDR-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This data set contains reformatted records derived from data returned by the Voyager Ultraviolet Spectrometer Subsystem on board Voyager 2 during the Uranus encounter phase of the Voyager mission. Original instrument data were merged with ancillary data from footprint SEDR files provided by the Voyager Project at the Jet Propulsion Laboratory. The final product files are formatted as PDS binary tables.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg2-u-uvs-3-rdr-v1.0_9g2f-4ydx",
             "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "comet sl9/jupiter collision",
                 "voyager",
                 "uranus"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG2-U-UVS-3-RDR-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg2-u-uvs-3-rdr-v1.0_9g2f-4ydx",
-            "description": "This data set contains reformatted records derived from data returned by the Voyager Ultraviolet Spectrometer Subsystem on board Voyager 2 during the Uranus encounter phase of the Voyager mission. Original instrument data were merged with ancillary data from footprint SEDR files provided by the Voyager Project at the Jet Propulsion Laboratory. The final product files are formatted as PDS binary tables.",
-            "title": "VG2 URANUS ULTRAVIOLET SPECTROMETER SUBSYSTEM 3 RDR V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "VG2 URANUS ULTRAVIOLET SPECTROMETER SUBSYSTEM 3 RDR V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-4-PRL-67PCHURYUMOV-M05-V1.0",
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
+            "description": "This CODMAC level 4 data set contains radiometric calibrated and geometric distortion corrected (resampled) image data in W/m^2/sr/nm acquired by the OSIRIS Wide Angle Camera during the PRELANDING phase of the Rosetta mission, covering the period from 2014-07-02T08:35:00.000 to 2014-08-01T09:59:59.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-4-prl-67pchuryumov-m05-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-4-PRL-67PCHURYUMOV-M05-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-4-prl-67pchuryumov-m05-v1.0",
-            "description": "This CODMAC level 4 data set contains radiometric calibrated and geometric distortion corrected (resampled) image data in W/m^2/sr/nm acquired by the OSIRIS Wide Angle Camera during the PRELANDING phase of the Rosetta mission, covering the period from 2014-07-02T08:35:00.000 to 2014-08-01T09:59:59.000.",
-            "title": "ROSETTA-ORBITER 67P OSIWAC 4 PRL-MTP005 RDR V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P OSIWAC 4 PRL-MTP005 RDR V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/2336",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Byrne, B.K., J. Liu, K.W. Bowman, Y. Yin, J. Yun, G. Ferreira, S.M. Ogle, L. Baskaran, L. He, X. Li, J. Xiao, and K.J. Davis. 2024. CMS-Flux-NA Fluxes and Aircraft CO2 Co-samples for 2018-2019. ORNL DAAC, Oak Ridge, Tennessee, USA. https://doi.org/10.3334/ORNLDAAC/2336",
-            "issued": "2024-04-24",
-            "temporal": "2018-01-01T01:36:55Z/2019-12-31T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-04-26",
-            "keyword": [
-                "climate indicators",
-                "atmosphere",
-                "atmospheric chemistry",
-                "earth science",
-                "carbon flux"
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
-            "identifier": "C2954648832-ORNL_CLOUD",
             "description": "This dataset provides gridded surface-atmosphere CO2 fluxes over North America from April 8 to November 18 during 2018 and 2019. Net ecosystem exchange (NEE) was estimated  by the CMS-Flux-NA CO2 inversion system by assimilating in situ CO2 measurements and/or Orbiting Carbon Observatory (OCO-2) column-averaged CO2 retrievals. These data, along with imposed diurnal NEE variations, fossil fuel emissions, biomass burning, and biofuel emissions, are provided at 3-hour temporal resolution. The modeled co-samples of CO2 observed for aircraft flights are included for model evaluation. The data are provided in NetCDF version 4 format.",
-            "graphic-preview-description": "Bottom-up (LNLGOGIS) spatial patterns of June-July mean change in net ecosystem exchange  (NEE_2019-NEE_2018) at 4 x 5-degrees spatial resolution.",
-            "title": "CMS-Flux-NA Fluxes and Aircraft CO2 Co-samples for 2018-2019",
-            "graphic-preview-file": "https://daac.ornl.gov/CMS/guides/CMS_FluxEstimates_Aircraft_CO2_Fig1.jpg",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F2336",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F2336",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/cms/CMS_FluxEstimates_Aircraft_CO2/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/cms/CMS_FluxEstimates_Aircraft_CO2/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/CMS/guides/CMS_FluxEstimates_Aircraft_CO2.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/CMS/guides/CMS_FluxEstimates_Aircraft_CO2.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/2336",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/2336",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/cms/CMS_FluxEstimates_Aircraft_CO2/comp/CMS_FluxEstimates_Aircraft_CO2.pdf",
-                    "description": "CMS-Flux-NA Fluxes and Aircraft CO2 Co-samples for 2018-2019: CMS_FluxEstimates_Aircraft_CO2.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "CMS-Flux-NA Fluxes and Aircraft CO2 Co-samples for 2018-2019: CMS_FluxEstimates_Aircraft_CO2.pdf",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/cms/CMS_FluxEstimates_Aircraft_CO2/comp/CMS_FluxEstimates_Aircraft_CO2.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://daac.ornl.gov/CMS/guides/CMS_FluxEstimates_Aircraft_CO2_Fig1.jpg",
-                    "description": "Bottom-up (LNLGOGIS) spatial patterns of June-July mean change in net ecosystem exchange  (NEE_2019-NEE_2018) at 4 x 5-degrees spatial resolution.",
                     "@type": "dcat:Distribution",
+                    "description": "Bottom-up (LNLGOGIS) spatial patterns of June-July mean change in net ecosystem exchange  (NEE_2019-NEE_2018) at 4 x 5-degrees spatial resolution.",
+                    "downloadURL": "https://daac.ornl.gov/CMS/guides/CMS_FluxEstimates_Aircraft_CO2_Fig1.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 }
             ],
+            "graphic-preview-description": "Bottom-up (LNLGOGIS) spatial patterns of June-July mean change in net ecosystem exchange  (NEE_2019-NEE_2018) at 4 x 5-degrees spatial resolution.",
+            "graphic-preview-file": "https://daac.ornl.gov/CMS/guides/CMS_FluxEstimates_Aircraft_CO2_Fig1.jpg",
+            "identifier": "C2954648832-ORNL_CLOUD",
+            "issued": "2024-04-24",
+            "keyword": [
+                "climate indicators",
+                "atmosphere",
+                "atmospheric chemistry",
+                "earth science",
+                "carbon flux"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/2336",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2024-04-26",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "ORNL_DAAC"
+            },
             "spatial": "-167.81 13.75 -39.69 76.25",
+            "temporal": "2018-01-01T01:36:55Z/2019-12-31T23:59:59Z",
             "theme": [
                 "CMS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "CMS-Flux-NA Fluxes and Aircraft CO2 Co-samples for 2018-2019"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/CAR/DATA113",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Charles Gatebe; Michael King; Rajesh Poudyal. 2018-01-10. CAR_ARMCAS_L1C. Version 1. CAR ARMCAS Arctic Cloud Radiation Measurements L1 V1. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/CAR/DATA113. https://disc.gsfc.nasa.gov/datacollection/CAR_ARMCAS_L1C_1.html.",
-            "issued": "2017-11-29",
-            "temporal": "1995-06-03T00:00:00Z/1995-06-14T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2017-11-29",
-            "keyword": [
-                "land surface",
-                "surface radiative properties",
-                "atmosphere",
-                "aerosols",
-                "atmospheric radiation",
-                "earth science",
-                "clouds",
-                "oceans",
-                "ocean optics"
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
-            "identifier": "C1442068286-GES_DISC",
-            "description": "The Arctic Radiation Measurement in Column Atmosphere-surface System (ARMCAS) was a collaborative research effort between the Cloud and Aerosol Research (CAR) Group, Department of Atmospheric Sciences, University of Washington (led by Professor Peter V. Hobbs) and Drs. Michael King and Si-Chee Tsay of NASA/Goddard. The field portion of ARMCAS was based out of Deadhorse, Alaska, from June 3-15, 1995. Flights of the University of Washington's Convair C-131A research aircraft and NASA's ER-2 aircraft took place over the tundra of the North Slope and over the partially ice-covered Beaufort Sea. Several of these flights were closely coordinated in order to provide simultaneous in situ and remote sensing measurements of arctic clouds.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "CAR_ARMCAS_L1C",
             "creator": "Charles Gatebe; Michael King; Rajesh Poudyal",
-            "title": "CAR ARMCAS Arctic Cloud Radiation Measurements L1 V1 (CAR_ARMCAS_L1C) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/CAR_ARMCAS_L1C_1.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The Arctic Radiation Measurement in Column Atmosphere-surface System (ARMCAS) was a collaborative research effort between the Cloud and Aerosol Research (CAR) Group, Department of Atmospheric Sciences, University of Washington (led by Professor Peter V. Hobbs) and Drs. Michael King and Si-Chee Tsay of NASA/Goddard. The field portion of ARMCAS was based out of Deadhorse, Alaska, from June 3-15, 1995. Flights of the University of Washington's Convair C-131A research aircraft and NASA's ER-2 aircraft took place over the tundra of the North Slope and over the partially ice-covered Beaufort Sea. Several of these flights were closely coordinated in order to provide simultaneous in situ and remote sensing measurements of arctic clouds.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FCAR%2FDATA113",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
```

