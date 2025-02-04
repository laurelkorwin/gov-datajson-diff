# Change History for nasa.json (Part 110)

### Changes from 31606f9 to dd2190f (Part 99/162)
**Author:** Automated

**Date:** 2025-02-01 15:02:16+00:00

**Message:** Updated data: Sat Feb  1 15:02:16 UTC 2025

```diff
                 "026:00"
             ],
-            "issued": "2010-09-22",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
-            "keyword": [
-                "dashlink",
-                "ames",
-                "nasa"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "MARK SCHWABACHER",
                 "hasEmail": "mailto:mark.a.schwabacher@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Dashlink"
-            },
-            "identifier": "DASHLINK_191",
             "description": "Full title: Mining Distance-Based Outliers in Near Linear Time with Randomization and a Simple Pruning Rule\r\n\r\nAbstract: Defining outliers by their distance to neighboring examples is a popular approach to finding unusual examples in a data set. Recently, much work has been conducted with the goal of finding fast algorithms for this task. We show that a simple nested loop algorithm that in the worst case is quadratic can give near linear time performance when the data is in random order and a simple pruning rule is used. We test our algorithm on real high-dimensional data sets with millions of examples and show that the near linear scaling holds over several orders of magnitude. Our average case analysis suggests that much of the efficiency is because the time to process non-outliers, which are the majority of examples, does not depend on the size of the data set.",
-            "title": "Mining Distance-Based Outliers in Near Linear Time",
-            "programCode": [
-                "026:029"
-            ],
             "distribution": [
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/publication/BaySchwabacherKDD2003.pdf",
-                    "description": "Mining Distance-Based Outliers in Near Linear Time with Randomization and a Simple Pruning Rule",
                     "@type": "dcat:Distribution",
+                    "description": "Mining Distance-Based Outliers in Near Linear Time with Randomization and a Simple Pruning Rule",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/publication/BaySchwabacherKDD2003.pdf",
+                    "mediaType": "application/pdf",
                     "title": "BaySchwabacherKDD2003.pdf"
                 }
             ],
-            "accrualPeriodicity": "irregular"
+            "identifier": "DASHLINK_191",
+            "issued": "2010-09-22",
+            "keyword": [
+                "dashlink",
+                "ames",
+                "nasa"
+            ],
+            "landingPage": "https://c3.nasa.gov/dashlink/resources/191/",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:029"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Dashlink"
+            },
+            "title": "Mining Distance-Based Outliers in Near Linear Time"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.nasa.gov/d/kkjx-tji2",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2018-06-25",
-            "temporal": "1977-01-01/2014-01-01",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
-            "keyword": [
-                "geography",
-                "wise",
-                "space science",
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
-            "identifier": "NASA-0000038__51",
+            "describedBy": "http://planetarynames.wr.usgs.gov/Page/Website",
             "description": "Planetary nomenclature, like terrestrial nomenclature, is used to uniquely identify a feature on the surface of a planet or satellite so that the feature can be easily located, described, and discussed. This gazetteer contains detailed information about all names of topographic and albedo features on planets and satellites (and some planetary ring and ring-gap systems) that the International Astronomical Union (IAU) has named and approved from its founding in 1919 through the present time.",
-            "title": "Gazetteer of Planetary Nomenclature",
-            "programCode": [
-                "026:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -1037051,186 +1037033,205 @@
                     "mediaType": "application/zip"
                 }
             ],
-            "describedBy": "http://planetarynames.wr.usgs.gov/Page/Website",
-            "accrualPeriodicity": "irregular"
+            "identifier": "NASA-0000038__51",
+            "issued": "2018-06-25",
+            "keyword": [
+                "geography",
+                "wise",
+                "space science",
+                "nen"
+            ],
+            "landingPage": "https://data.nasa.gov/d/kkjx-tji2",
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
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/601",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Hall, F.G., G. Rapalee, and D.E. Knapp. 2001. BOREAS Follow-On DSP-10 Regridded Peatland Maps. ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/601",
-            "issued": "2024-04-27",
-            "temporal": "1994-01-01T00:00:00Z/1995-01-01T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-04-28",
-            "keyword": [
-                "earth science",
-                "biosphere",
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
-            "identifier": "C2766089604-ORNL_CLOUD",
             "description": "These images were produced by aggregating 1' gridded data layers derived from the polygon-based Peatlands of Canada Database (Tarnocai et al., 2000) to 10' (horizontal) by 5' (vertical) and to 0.5 degree by 0.5 degree (or 30' by 30') pixel sizes in straight latitude/longitude grids.",
-            "graphic-preview-description": "Browse Image",
-            "title": "BOREAS Follow-On DSP-10 Regridded Peatland Maps",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/boreas_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F601",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F601",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/boreas/DSP/BFO_dsp10_peatlands/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/boreas/DSP/BFO_dsp10_peatlands/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/BOREAS/FollowOn/guides/dsp10_peatlands_maps.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/BOREAS/FollowOn/guides/dsp10_peatlands_maps.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/601",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/601",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/DSP/BFO_dsp10_peatlands/comp/0_peatlands_10by5min.txt",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/DSP/BFO_dsp10_peatlands/comp/0_peatlands_10by5min.txt",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/DSP/BFO_dsp10_peatlands/comp/0_peatlands_30min.txt",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/DSP/BFO_dsp10_peatlands/comp/0_peatlands_30min.txt",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/DSP/BFO_dsp10_peatlands/comp/0_pixel_area_10by5min.txt",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/DSP/BFO_dsp10_peatlands/comp/0_pixel_area_10by5min.txt",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/DSP/BFO_dsp10_peatlands/comp/dsp10_peatlands_maps.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/DSP/BFO_dsp10_peatlands/comp/dsp10_peatlands_maps.pdf",
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
+            "identifier": "C2766089604-ORNL_CLOUD",
+            "issued": "2024-04-27",
+            "keyword": [
+                "earth science",
+                "biosphere",
+                "ecosystems"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/601",
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
+            "temporal": "1994-01-01T00:00:00Z/1995-01-01T23:59:59Z",
             "theme": [
                 "BOREAS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "BOREAS Follow-On DSP-10 Regridded Peatland Maps"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/MODIS/MYDAODHD.NRT.061",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "LANCEMODIS. 2017-10-20. MODIS/Aqua value-added Aerosol Optical Depth Product. Version 6.1NRT. MODAPS at NASA/GSFC. Archived by National Aeronautics and Space Administration, U.S. Government, The Land, Atmosphere Near real-time Capability for EOS (LANCE). https://doi.org/10.5067/MODIS/MYDAODHD.NRT.061. https://earthdata.nasa.gov/earth-observation-data/near-real-time/download-nrt-data/modis-nrt.",
-            "issued": "2017-10-11",
-            "temporal": "2017-10-20T00:00:00Z/2023-07-24T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-20",
-            "references": [
-                "https://doi.org/10.5194/amt-4-379-2011"
-            ],
-            "keyword": [
-                "aerosols",
-                "ngda",
-                "earth science",
-                "atmospheric radiation",
-                "atmosphere",
-                "national geospatial data asset"
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
-            "identifier": "C1427010664-LANCEMODIS",
-            "description": "MODIS was launched aboard the Terra satellite on December 18, 1999 (10:30 am equator crossing time) as part of NASA's Earth Observing System (EOS) mission. MODIS with its 2330 km viewing swath width provides almost daily global coverage. It acquires data in 36 high spectral resolution bands between 0.415 to 14.235 micron with spatial resolutions of 250m(2 bands), 500m(5 bands),and 1000m (29 bands). MODIS sensor counts, calibrated radiances, geolocation products and all derived geophysical atmospheric and ocean products are archived at various DAACs and has been made available to public since April 2000.\n\nThe shortname for this level-3 MODIS aerosol product is MYDAODHD. The Naval Research Laboratory and the University of North Dakota developed this value-added aerosol optical depth dataset based on MODIS Level 2 aerosol products. The MYDAODHD is a gridded product and is specifically designed for quantitative applications including data assimilation and model validation. It is available through LANCE-MODIS. It offers several enhancements over the MODIS Level 2 data on which it is based. These enhancements include stringent filtering to reduce outliers, eliminate cloud contamination, and exclude conditions where aerosol detection is likely to be inaccurate; reduction of systematic biases over land and ocean by empirical corrections; reduction of random variation in AOD values by spatial averaging; quantitative estimation of uncertainty for each AOD data point.\n\nThe MxDAODHD granules are produced every six hours, and time-stamped 00:00, 06:00, 12:00, and 18:00 (all times UTC). Each granule includes MODIS observations from +/-3 hours from the timestamp (e.g. 12:00 product includes MODIS data from 09:00-15:00 UTC). Production is initiated as soon as the Level 2 inputs become available in the LANCE system.\n\nSee the LANCE-MODIS page for more dataset information: \n\nhttps://earthdata.nasa.gov/earth-observation-data/near-real-time/download-nrt-data/modis-nrt",
-            "release-place": "MODAPS at NASA/GSFC",
             "creator": "LANCEMODIS",
-            "title": "MODIS/Aqua L3 Value-added Aerosol Optical Depth - NRT",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "MODIS was launched aboard the Terra satellite on December 18, 1999 (10:30 am equator crossing time) as part of NASA's Earth Observing System (EOS) mission. MODIS with its 2330 km viewing swath width provides almost daily global coverage. It acquires data in 36 high spectral resolution bands between 0.415 to 14.235 micron with spatial resolutions of 250m(2 bands), 500m(5 bands),and 1000m (29 bands). MODIS sensor counts, calibrated radiances, geolocation products and all derived geophysical atmospheric and ocean products are archived at various DAACs and has been made available to public since April 2000.\n\nThe shortname for this level-3 MODIS aerosol product is MYDAODHD. The Naval Research Laboratory and the University of North Dakota developed this value-added aerosol optical depth dataset based on MODIS Level 2 aerosol products. The MYDAODHD is a gridded product and is specifically designed for quantitative applications including data assimilation and model validation. It is available through LANCE-MODIS. It offers several enhancements over the MODIS Level 2 data on which it is based. These enhancements include stringent filtering to reduce outliers, eliminate cloud contamination, and exclude conditions where aerosol detection is likely to be inaccurate; reduction of systematic biases over land and ocean by empirical corrections; reduction of random variation in AOD values by spatial averaging; quantitative estimation of uncertainty for each AOD data point.\n\nThe MxDAODHD granules are produced every six hours, and time-stamped 00:00, 06:00, 12:00, and 18:00 (all times UTC). Each granule includes MODIS observations from +/-3 hours from the timestamp (e.g. 12:00 product includes MODIS data from 09:00-15:00 UTC). Production is initiated as soon as the Level 2 inputs become available in the LANCE system.\n\nSee the LANCE-MODIS page for more dataset information: \n\nhttps://earthdata.nasa.gov/earth-observation-data/near-real-time/download-nrt-data/modis-nrt",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMODIS%2FMYDAODHD.NRT.061",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMODIS%2FMYDAODHD.NRT.061",
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
-                    "description": "Access Collection 6.1 data set from the MODAPS LANCE-MODIS page(DOWNLOAD server).",
                     "@type": "dcat:Distribution",
+                    "description": "Access Collection 6.1 data set from the MODAPS LANCE-MODIS page(DOWNLOAD server).",
+                    "downloadURL": "https://lance3.modaps.eosdis.nasa.gov/data_products/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through MODAPS"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nrt3.modaps.eosdis.nasa.gov/allData/61/MYDAODHD/",
-                    "description": "Direct access to the directory hosting the MYDAODHD Collection 6.1 NRT data set.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct access to the directory hosting the MYDAODHD Collection 6.1 NRT data set.",
+                    "downloadURL": "https://nrt3.modaps.eosdis.nasa.gov/allData/61/MYDAODHD/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through MODAPS"
                 }
             ],
+            "identifier": "C1427010664-LANCEMODIS",
+            "issued": "2017-10-11",
+            "keyword": [
+                "aerosols",
+                "ngda",
+                "earth science",
+                "atmospheric radiation",
+                "atmosphere",
+                "national geospatial data asset"
+            ],
+            "landingPage": "https://doi.org/10.5067/MODIS/MYDAODHD.NRT.061",
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
+            "references": [
+                "https://doi.org/10.5194/amt-4-379-2011"
+            ],
+            "release-place": "MODAPS at NASA/GSFC",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2017-10-20T00:00:00Z/2023-07-24T00:00:00Z",
             "theme": [
                 "DODS",
                 "EOSDIS",
@@ -1037238,1237 +1037239,1211 @@
                 "AQUA",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "MODIS/Aqua L3 Value-added Aerosol Optical Depth - NRT"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewBundle.jsp?identifier=urn%3Anasa%3Apds%3Aphx_mission_bundle&version=1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This version of the Phoenix bundle was created by the PDS Atmospheres node in 2014",
+            "identifier": "urn:nasa:pds:phx_mission_bundle_kkqw-yu3e",
             "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "phoenix mars mission",
                 "phoenix",
                 "mars"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewBundle.jsp?identifier=urn%3Anasa%3Apds%3Aphx_mission_bundle&version=1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:phx_mission_bundle_kkqw-yu3e",
-            "description": "This version of the Phoenix bundle was created by the PDS Atmospheres node in 2014",
-            "title": "Phoenix Mission Bundle",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "Phoenix Mission Bundle"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/GEWEXSRB/Rel4-IP_Longwave_3hrlymonthly_oceanonly_utc_1",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/GEWEXSRB/Rel4-IP_Longwave_3hrlymonthly_oceanonly_utc_1.",
-            "issued": "2020-10-05",
-            "temporal": "2010-01-01T00:00:00Z/2017-06-30T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-10-05",
-            "keyword": [
-                "earth science",
-                "clouds",
-                "atmospheric radiation",
-                "atmosphere"
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
-            "identifier": "C2062180056-LARC_ASDC",
             "description": "GEWEXSRB_Rel4-GEWEXSRB_Rel4-IP_Longwave_3hrlymonthly_oceanonly_utc is the Global Energy and Water Exchanges (GEWEX) Surface Radiation Budget (SRB) Integrated Product (Release-4) Longwave 3-Hourly Monthly Average by UTC (also known as \"diurnal\"). This product contains ocean-only global fields of 26 longwave surface, Top of Atmosphere (TOA), and atmospheric profile radiative parameters derived with the Longwave algorithm of the NASA World Climate Research Programme/Global Energy and Water-Cycle Experiment (WCRP/GEWEX) Surface Radiation Budget (SRB) Project. This version is an extension of Release 4- Integrated Product with ocean-only fluxes due to a missing key input from the main data set . The fluxes include all-sky, clear-sky and pristine-sky TOA upward fluxes (outgoing longwave radiation, OLR), all-sky, clear-sky and pristine-sky upward and downward fluxes at: tropopause, 200hPa, 500hPa and surface. A status flag of filled cloud properties is also included. Inputs to the longwave algorithm are cloud information based on ISCCP HXS, meteorology from ISCCP nnHIRS, SeaFlux SST and surface, and MERRA-2 conditionally. The temporal range is January 2010 through June 2017. These data are averaged by UTC from 3-hourly values.",
-            "title": "GEWEX SRB Integrated Product (Rel-4) Longwave 3-Hourly Monthly Average by UTC Ocean-only Fluxes",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGEWEXSRB%2FRel4-IP_Longwave_3hrlymonthly_oceanonly_utc_1",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGEWEXSRB%2FRel4-IP_Longwave_3hrlymonthly_oceanonly_utc_1",
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
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2062180056-LARC_ASDC",
-                    "description": "Earthdata Search for GEWEXSRB_Rel4-IP_Longwave_3hrlymonthly_oceanonly_utc_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for GEWEXSRB_Rel4-IP_Longwave_3hrlymonthly_oceanonly_utc_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2062180056-LARC_ASDC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/GEWEXSRB/Rel4-IP_Longwave_3hrlymonthly_oceanonly_utc_1",
-                    "description": "DOI data set landing page for GEWEXSRB_Rel4-IP_Longwave_3hrlymonthly_oceanonly_utc_1",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for GEWEXSRB_Rel4-IP_Longwave_3hrlymonthly_oceanonly_utc_1",
+                    "downloadURL": "https://doi.org/10.5067/GEWEXSRB/Rel4-IP_Longwave_3hrlymonthly_oceanonly_utc_1",
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
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/SRB/GEWEXSRB_Rel4-IP/Longwave_3hrlymonthly_oceanonly_utc_1/",
-                    "description": "ASDC Direct Data Download for GEWEXSRB_Rel4-IP_Longwave_3hrlymonthly_oceanonly_utc_1",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for GEWEXSRB_Rel4-IP_Longwave_3hrlymonthly_oceanonly_utc_1",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/SRB/GEWEXSRB_Rel4-IP/Longwave_3hrlymonthly_oceanonly_utc_1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/SRB/GEWEXSRB_Rel4-IP/Longwave_3hrlymonthly_oceanonly_utc_1/contents.html",
-                    "description": "OPeNDAP data access for GEWEXSRB_Rel4-IP_Longwave_3hrlymonthly_oceanonly_utc_1",
                     "@type": "dcat:Distribution",
+                    "description": "OPeNDAP data access for GEWEXSRB_Rel4-IP_Longwave_3hrlymonthly_oceanonly_utc_1",
+                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/SRB/GEWEXSRB_Rel4-IP/Longwave_3hrlymonthly_oceanonly_utc_1/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 }
             ],
+            "identifier": "C2062180056-LARC_ASDC",
+            "issued": "2020-10-05",
+            "keyword": [
+                "earth science",
+                "clouds",
+                "atmospheric radiation",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.5067/GEWEXSRB/Rel4-IP_Longwave_3hrlymonthly_oceanonly_utc_1",
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
+            "temporal": "2010-01-01T00:00:00Z/2017-06-30T23:59:59.999Z",
             "theme": [
                 "SRB",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "GEWEX SRB Integrated Product (Rel-4) Longwave 3-Hourly Monthly Average by UTC Ocean-only Fluxes"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/2013",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Hook, S.J., J.S. Myers, K.J. Thome, M. Fitzgerald, A.B. Kahle,  Airborne Sensor Facility NASA Ames Research Center, and A.N. French. 2022. MASTER: Jornada Experiment, Nevada-New Mexico, October 2007. ORNL DAAC, Oak Ridge, Tennessee, USA. https://doi.org/10.3334/ORNLDAAC/2013",
-            "issued": "2023-06-29",
-            "temporal": "2007-10-01T18:22:35Z/2007-10-04T18:46:01Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-13",
-            "keyword": [
-                "infrared wavelengths",
-                "spectral/engineering",
-                "visible wavelengths",
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
-            "identifier": "C2731711949-ORNL_CLOUD",
             "description": "This dataset includes Level 1B (L1B) data products from the MODIS/ASTER Airborne Simulator (MASTER) instrument. The spectral data were collected during four flights aboard a DOE B-200 aircraft over Nevada, Arizona, and New Mexico, U.S., from 2007-10-01 to 2007-10-04. A focus of this data collection was the USDA Jornada Experimental Range (Jornada) in southern New Mexico. To complement the programs of ground measurements, JORNEX (JORNada EXperiment) began in 1995 to collect remotely sensed data from aircraft and satellite platforms to provide spatial and temporal data on physical and biological states of the Jornada rangeland. JORNEX uses remote sensing techniques to study arid rangeland and the responses of vegetation to changing hydrologic fluxes and atmospheric driving forces. This deployment was coordinated by the U.S. Department of Energy's Remote Sensing Laboratory (RSL) located at Nellis Air Force Base near Las Vegas, Nevada. Data products include L1B georeferenced multispectral imagery of calibrated radiance in 50 bands covering wavelengths of 0.460 to 12.879 micrometers at approximately 10-meter spatial resolution. The L1B file format is HDF-4. In addition, the dataset includes flight paths, spectral band information, instrument configuration, ancillary notes, and summary information for each flight, and browse images derived from each L1B data file.",
-            "graphic-preview-description": "Single-band images and a RGB composite image from flight track 2 as acquired on 01 October 2007 over Valley of Fire, west of Lake Mead, Nevada, California, U.S. Source: MASTERL1B_0800101_02_20071001_1828_1829_V02.jpg",
-            "title": "MASTER: Jornada Experiment, Nevada-New Mexico, October 2007",
-            "graphic-preview-file": "https://daac.ornl.gov/MASTER/guides/MASTER_RSL_October_2007_Fig1.jpg",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F2013",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F2013",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/master/MASTER_RSL_October_2007/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/master/MASTER_RSL_October_2007/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/MASTER/guides/MASTER_RSL_October_2007.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/MASTER/guides/MASTER_RSL_October_2007.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/2013",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/2013",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/master/MASTER_RSL_October_2007/comp/MASTER_RSL_October_2007.pdf",
-                    "description": "MASTER: Jornada Experiment, Nevada-New Mexico, October 2007: MASTER_RSL_October_2007.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "MASTER: Jornada Experiment, Nevada-New Mexico, October 2007: MASTER_RSL_October_2007.pdf",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/master/MASTER_RSL_October_2007/comp/MASTER_RSL_October_2007.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://daac.ornl.gov/MASTER/guides/MASTER_RSL_October_2007_Fig1.jpg",
-                    "description": "Single-band images and a RGB composite image from flight track 2 as acquired on 01 October 2007 over Valley of Fire, west of Lake Mead, Nevada, California, U.S. Source: MASTERL1B_0800101_02_20071001_1828_1829_V02.jpg",
                     "@type": "dcat:Distribution",
+                    "description": "Single-band images and a RGB composite image from flight track 2 as acquired on 01 October 2007 over Valley of Fire, west of Lake Mead, Nevada, California, U.S. Source: MASTERL1B_0800101_02_20071001_1828_1829_V02.jpg",
+                    "downloadURL": "https://daac.ornl.gov/MASTER/guides/MASTER_RSL_October_2007_Fig1.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 }
             ],
+            "graphic-preview-description": "Single-band images and a RGB composite image from flight track 2 as acquired on 01 October 2007 over Valley of Fire, west of Lake Mead, Nevada, California, U.S. Source: MASTERL1B_0800101_02_20071001_1828_1829_V02.jpg",
+            "graphic-preview-file": "https://daac.ornl.gov/MASTER/guides/MASTER_RSL_October_2007_Fig1.jpg",
+            "identifier": "C2731711949-ORNL_CLOUD",
+            "issued": "2023-06-29",
+            "keyword": [
+                "infrared wavelengths",
+                "spectral/engineering",
+                "visible wavelengths",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/2013",
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
             "spatial": "-114.53 32.43 -106.59 36.52",
+            "temporal": "2007-10-01T18:22:35Z/2007-10-04T18:46:01Z",
             "theme": [
                 "MASTER",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "MASTER: Jornada Experiment, Nevada-New Mexico, October 2007"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://c3.nasa.gov/dashlink/resources/522/",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2012-02-07",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
-            "keyword": [
-                "ames",
-                "dashlink",
-                "nasa"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Matthew Daigle",
                 "hasEmail": "mailto:matthew.j.daigle@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Dashlink"
-            },
-            "identifier": "DASHLINK_522",
             "description": "Within the area of systems health management, the task of prognostics centers on predicting when components will fail. Model-based prognostics exploits domain knowledge of the system, its components, and how they fail by casting the underlying physical phenomena in a physics-based model that is derived from first principles. Uncertainty cannot be avoided in prediction, therefore, algorithms are employed that help in managing these uncertainties. The particle filtering algorithm has become a popular choice for model-based prognostics due to its wide applicability, ease of implementation, and support for uncertainty management. We develop a general model-based prognostics methodology within a robust probabilistic framework using particle filters. As a case study, we consider a pneumatic valve from the Space Shuttle cryogenic refueling system. We develop a detailed physics-based model of the pneumatic valve, and perform comprehensive simulation experiments to illustrate our prognostics approach and evaluate its effectiveness and robustness. The approach is demonstrated using historical pneumatic valve data from the refueling system.",
-            "title": "A Model-based Prognostics Approach Applied to Pneumatic Valves",
-            "programCode": [
-                "026:029"
-            ],
             "distribution": [
                 {
-                    "mediaType": "application/x-pdf",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/publication/DaigleEtAl-IJPHM-Valves.pdf",
-                    "description": "DaigleEtAl-IJPHM-Valves.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "DaigleEtAl-IJPHM-Valves.pdf",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/publication/DaigleEtAl-IJPHM-Valves.pdf",
+                    "mediaType": "application/x-pdf",
                     "title": "DaigleEtAl-IJPHM-Valves.pdf"
                 }
             ],
-            "accrualPeriodicity": "irregular"
+            "identifier": "DASHLINK_522",
+            "issued": "2012-02-07",
+            "keyword": [
+                "ames",
+                "dashlink",
+                "nasa"
+            ],
+            "landingPage": "https://c3.nasa.gov/dashlink/resources/522/",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:029"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Dashlink"
+            },
+            "title": "A Model-based Prognostics Approach Applied to Pneumatic Valves"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/GZT3YJIL1HUV",
             "citation": "AIRS project. 2019-12-15. AIRX3SPM. Version 7.0. Aqua/AIRS L3 Monthly Support Product (AIRS+AMSU) 1 degree x 1 degree V7.0. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/GZT3YJIL1HUV. https://disc.gsfc.nasa.gov/datacollection/AIRX3SPM_7.0.html. Digital Science Data.",
-            "issued": "2002-09-01",
-            "temporal": "2002-09-01T00:00:00Z/2022-01-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2016-10-01",
-            "references": [
-                "https://doi.org/10.1117/1.JRS.8.084994",
-                "https://doi.org/10.5194/acp-14-399-2014"
-            ],
-            "keyword": [
-                "air quality",
-                "surface thermal properties",
-                "surface radiative properties",
-                "precipitation",
-                "ocean temperature",
-                "oceans",
-                "land surface",
-                "earth science",
-                "clouds",
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
                 "fn": "LENA IREDELL",
                 "hasEmail": "mailto:lena.iredell@nasa.gov"
             },
+            "creator": "AIRS project",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C1701805687-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "The Atmospheric Infrared Sounder (AIRS) is a grating spectrometer (R = 1200) aboard the second Earth Observing System (EOS) polar-orbiting platform, EOS Aqua. In combination with the Advanced Microwave Sounding Unit (AMSU) AIRS constitutes an innovative atmospheric sounding group of infrared and microwave sensors. The L3 support products are similar to the L3 standard products but contain fields which are not fully validated, or are inputs or intermediary values. Because no quality control information is available for some of these fields, values from failed retrievals may be included.\n\n\nThe value for each grid box is the sum of the values that fall within the 1x1 area divided by the number of points in the\nbox.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "AIRX3SPM",
-            "creator": "AIRS project",
-            "graphic-preview-description": "Sample data of the \"AIRS/Aqua Level 3 monthly standard physical retrieval product (Without HSB)\".",
-            "title": "Aqua/AIRS L3 Monthly Support Product (AIRS+AMSU) 1 degree x 1 degree V7.0 at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/AIRX3SPM_7.0.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGZT3YJIL1HUV",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGZT3YJIL1HUV",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/AIRX3SPM_7.0.png",
-                    "description": "Sample data of the \"AIRS/Aqua Level 3 monthly standard physical retrieval product (Without HSB)\".",
                     "@type": "dcat:Distribution",
+                    "description": "Sample data of the \"AIRS/Aqua Level 3 monthly standard physical retrieval product (Without HSB)\".",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/AIRX3SPM_7.0.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/AIRX3SPM_7.0.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/AIRX3SPM_7.0.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/Aqua_AIRS_Level3/AIRX3SPM.7.0/",
-                    "description": "Access the data via HTTP.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTP.",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/Aqua_AIRS_Level3/AIRX3SPM.7.0/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/opendap/Aqua_AIRS_Level3/AIRX3SPM.7.0",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/opendap/Aqua_AIRS_Level3/AIRX3SPM.7.0",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=AIRX3SPM+7.0",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=AIRX3SPM+7.0",
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
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/AIRS/Overview_of_AIRS_Products_and_Documentation.pdf",
-                    "description": "Overview of the AIRS Mission: Instruments, Processing Algorithms, Products, and Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Overview of the AIRS Mission: Instruments, Processing Algorithms, Products, and Documentation",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/AIRS/Overview_of_AIRS_Products_and_Documentation.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's read me document"
                 },
-                {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/AIRS/V7_L3_User_Guide.pdf",
-                    "description": "AIRS Version 7 Level 3 Product User Guide",
-                    "@type": "dcat:Distribution",
-                    "title": "View this dataset's user's guide"
-                }
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "AIRS Version 7 Level 3 Product User Guide",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/AIRS/V7_L3_User_Guide.pdf",
+                    "mediaType": "application/pdf",
+                    "title": "View this dataset's user's guide"
+                }
+            ],
+            "graphic-preview-description": "Sample data of the \"AIRS/Aqua Level 3 monthly standard physical retrieval product (Without HSB)\".",
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/AIRX3SPM_7.0.png",
+            "identifier": "C1701805687-GES_DISC",
+            "issued": "2002-09-01",
+            "keyword": [
+                "air quality",
+                "surface thermal properties",
+                "surface radiative properties",
+                "precipitation",
+                "ocean temperature",
+                "oceans",
+                "land surface",
+                "earth science",
+                "clouds",
+                "atmospheric water vapor",
+                "atmospheric temperature",
+                "atmospheric radiation",
+                "atmospheric pressure",
+                "atmospheric chemistry",
+                "atmosphere",
+                "altitude"
+            ],
+            "landingPage": "https://doi.org/10.5067/GZT3YJIL1HUV",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2016-10-01",
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
             ],
+            "release-place": "Greenbelt, MD, USA",
+            "series-name": "AIRX3SPM",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2002-09-01T00:00:00Z/2022-01-17T00:00:00Z",
             "theme": [
                 "Aqua",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Aqua/AIRS L3 Monthly Support Product (AIRS+AMSU) 1 degree x 1 degree V7.0 at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/GNKZZBAYDF4W",
             "citation": "Amy McNally NASA/GSFC/HSL. 2018-11-15. FLDAS_NOAH01_C_GL_MA. Version 001. FLDAS Noah Land Surface Model L4 Global Monthly Anomaly 0.1 x 0.1 degree (MERRA-2 and CHIRPS). Greenbelt, Maryland, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/GNKZZBAYDF4W. https://disc.gsfc.nasa.gov/datacollection/FLDAS_NOAH01_C_GL_MA_001.html. Digital Science Data.",
-            "issued": "2018-10-15",
-            "temporal": "1982-01-01T00:00:00Z/2022-01-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2018-10-15",
-            "references": [
-                "https://doi.org/10.1038/sdata.2017.12",
-                "https://doi.org/10.3390/w11101968"
-            ],
-            "keyword": [
-                "atmospheric water vapor",
-                "earth science",
-                "surface water",
-                "terrestrial hydrosphere",
-                "atmospheric temperature",
-                "atmosphere",
-                "land surface",
-                "soils",
-                "precipitation"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Carlee Loeser",
                 "hasEmail": "mailto:carlee.loeser@nasa.gov"
             },
+            "creator": "Amy McNally NASA/GSFC/HSL",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C1563092281-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "The monthly anomaly data set contains a series of land surface parameters simulated from the Noah 3.6.1 model in the Famine Early Warning Systems Network (FEWS NET) Land Data Assimilation System (FLDAS). The dataset comprises of monthly files, each representing how the month compares to the 35-year monthly climatology from 1982 to 2016, based on the FLDAS Noah Land Surface Model L4 Global Monthly 0.1 x 0.1 degree (MERRA-2 and CHIRPS) V001 (FLDAS_NOAH01_C_GL_M_001) monthly data. The data are in 0.10 degree resolution and the spatial coverage is global (60S, 180W, 90N, 180E). The FLDAS regional monthly anomaly datasets will no longer be available and have been superseded by the global monthly anomaly dataset. \n\nMore information about the monthly FLDAS can be found from the dataset landing page for FLDAS_NOAH01_C_GL_M_001 and the FLDAS README document.\n\nIn November 2020, all FLDAS data were\u00a0post-processed with the MOD44W MODIS land mask. \u00a0Previously, some grid boxes over inland water were considered as over land and, thus, had non-missing values.\u00a0 The post-processing corrected this issue and masked out all model output data over inland water; the post-processing did not affect\u00a0the meteorological forcing variables. More information on this can be found in the FLDAS README document, and the MOD44W MODIS land mask is available on the FLDAS Project site.  If you had downloaded any FLDAS data prior to November 2020, please download the data again to receive the post-processed data.",
-            "release-place": "Greenbelt, Maryland, USA",
-            "series-name": "FLDAS_NOAH01_C_GL_MA",
-            "creator": "Amy McNally NASA/GSFC/HSL",
-            "graphic-preview-description": "The GES-DISC Interactive Online Visualization ANd aNalysis Interface (Giovanni) is a web-based tool that allows users to interactively visualize and analyze data.",
-            "title": "FLDAS Noah Land Surface Model L4 Global Monthly Anomaly 0.1 x 0.1 degree (MERRA-2 and CHIRPS) V001 (FLDAS_NOAH01_C_GL_MA) at GES DISC",
-            "graphic-preview-file": "https://giovanni.gsfc.nasa.gov/giovanni/#dataKeyword=FLDAS_NOAH01_C_GL_MA",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGNKZZBAYDF4W",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGNKZZBAYDF4W",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/FLDAS_NOAH01_C_GL_MA_001.png",
-                    "description": "FLDAS Noah Land Surface Model L4 Global Monthly Anomaly 0.1 x 0.1 degree (MERRA-2 and CHIRPS) V001 - Monthly anomaly of soil moisture content for 0 - 10 cm underground (m^3 m-3) for January 1982, based on 35-year monthly climatology (1982-2016)",
                     "@type": "dcat:Distribution",
+                    "description": "FLDAS Noah Land Surface Model L4 Global Monthly Anomaly 0.1 x 0.1 degree (MERRA-2 and CHIRPS) V001 - Monthly anomaly of soil moisture content for 0 - 10 cm underground (m^3 m-3) for January 1982, based on 35-year monthly climatology (1982-2016)",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/FLDAS_NOAH01_C_GL_MA_001.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/FLDAS_NOAH01_C_GL_MA_001.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/FLDAS_NOAH01_C_GL_MA_001.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://hydro1.gesdisc.eosdis.nasa.gov/data/FLDAS/FLDAS_NOAH01_C_GL_MA.001/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://hydro1.gesdisc.eosdis.nasa.gov/data/FLDAS/FLDAS_NOAH01_C_GL_MA.001/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=FLDAS_NOAH01_C_GL_MA",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=FLDAS_NOAH01_C_GL_MA",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://giovanni.gsfc.nasa.gov/giovanni/#dataKeyword=FLDAS_NOAH01_C_GL_MA",
-                    "description": "The GES-DISC Interactive Online Visualization ANd aNalysis Interface (Giovanni) is a web-based tool that allows users to interactively visualize and analyze data.",
                     "@type": "dcat:Distribution",
+                    "description": "The GES-DISC Interactive Online Visualization ANd aNalysis Interface (Giovanni) is a web-based tool that allows users to interactively visualize and analyze data.",
+                    "downloadURL": "https://giovanni.gsfc.nasa.gov/giovanni/#dataKeyword=FLDAS_NOAH01_C_GL_MA",
+                    "mediaType": "text/html",
                     "title": "Get a related visualization through GIOVANNI"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://hydro1.gesdisc.eosdis.nasa.gov/opendap/FLDAS/FLDAS_NOAH01_C_GL_MA.001/",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://hydro1.gesdisc.eosdis.nasa.gov/opendap/FLDAS/FLDAS_NOAH01_C_GL_MA.001/",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://hydro1.gesdisc.eosdis.nasa.gov/data/FLDAS/FLDAS_NOAH01_C_GL_MA.001/doc/README_FLDAS.pdf",
-                    "description": "README Document",
                     "@type": "dcat:Distribution",
+                    "description": "README Document",
+                    "downloadURL": "https://hydro1.gesdisc.eosdis.nasa.gov/data/FLDAS/FLDAS_NOAH01_C_GL_MA.001/doc/README_FLDAS.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's read me document"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ldas.gsfc.nasa.gov/FLDAS/",
-                    "description": "FLDAS Project Website",
                     "@type": "dcat:Distribution",
+                    "description": "FLDAS Project Website",
+                    "downloadURL": "https://ldas.gsfc.nasa.gov/FLDAS/",
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
-                    "downloadURL": "https://ldas.gsfc.nasa.gov/fldas/vegetation-class",
-                    "description": "The MOD44W MODIS Water Mask is the standard land/sea mask for FLDAS, and is available for download.",
                     "@type": "dcat:Distribution",
+                    "description": "The MOD44W MODIS Water Mask is the standard land/sea mask for FLDAS, and is available for download.",
+                    "downloadURL": "https://ldas.gsfc.nasa.gov/fldas/vegetation-class",
+                    "mediaType": "text/html",
                     "title": "View this dataset's product usage"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://hydro1.gesdisc.eosdis.nasa.gov/thredds/catalog/FLDAS_aggregation/FLDAS_NOAH01_C_GL_MA.001/catalog.html",
-                    "description": "Allows users to access the data aggregated by year and month.",
                     "@type": "dcat:Distribution",
+                    "description": "Allows users to access the data aggregated by year and month.",
+                    "downloadURL": "https://hydro1.gesdisc.eosdis.nasa.gov/thredds/catalog/FLDAS_aggregation/FLDAS_NOAH01_C_GL_MA.001/catalog.html",
+                    "mediaType": "text/html",
                     "title": "Use THREDDS DATA to download the dataset's data"
                 }
             ],
+            "graphic-preview-description": "The GES-DISC Interactive Online Visualization ANd aNalysis Interface (Giovanni) is a web-based tool that allows users to interactively visualize and analyze data.",
+            "graphic-preview-file": "https://giovanni.gsfc.nasa.gov/giovanni/#dataKeyword=FLDAS_NOAH01_C_GL_MA",
+            "identifier": "C1563092281-GES_DISC",
+            "issued": "2018-10-15",
+            "keyword": [
+                "atmospheric water vapor",
+                "earth science",
+                "surface water",
+                "terrestrial hydrosphere",
+                "atmospheric temperature",
+                "atmosphere",
+                "land surface",
+                "soils",
+                "precipitation"
+            ],
+            "landingPage": "https://doi.org/10.5067/GNKZZBAYDF4W",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2018-10-15",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
+            },
+            "references": [
+                "https://doi.org/10.1038/sdata.2017.12",
+                "https://doi.org/10.3390/w11101968"
+            ],
+            "release-place": "Greenbelt, Maryland, USA",
+            "series-name": "FLDAS_NOAH01_C_GL_MA",
             "spatial": "-180.0 -60.0 180.0 90.0",
+            "temporal": "1982-01-01T00:00:00Z/2022-01-17T00:00:00Z",
             "theme": [
                 "FLDAS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "FLDAS Noah Land Surface Model L4 Global Monthly Anomaly 0.1 x 0.1 degree (MERRA-2 and CHIRPS) V001 (FLDAS_NOAH01_C_GL_MA) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ASDC/SUBORBITAL/TRACE-P/TraceGas_InSitu_P3B_Data_1",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2024-09-06. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/ASDC/SUBORBITAL/TRACE-P/TraceGas_InSitu_P3B_Data_1.",
-            "issued": "2001-02-01",
-            "temporal": "1999-01-07T00:00:00Z/2002-03-01T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2001-04-30",
-            "keyword": [
-                "atmosphere",
-                "earth science",
-                "air quality",
-                "aerosols",
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
-            "identifier": "C2812956769-LARC_CLOUD",
             "description": "TRACE-P_TraceGas_AircraftInSitu_P3B_Data is the in-situ trace gas data collected onboard the P-3B aircraft during the Transport and Chemical Evolution over the Pacific (TRACE-P) suborbital campaign. Data from the Chemical Ionization Mass Spectrometer (CIMS) and the Differential Absorption of CO, CH4, N2O Measurements (DACOM) instruments are featured in this collection. Data collection for this product is complete.\r\n\r\nThe NASA TRACE-P mission was a part of NASA\u2019s Global Tropospheric Experiment (GTE) \u2013 an assemblage of missions conducted from 1983-2001 with various research goals and objectives.\u202fTRACE-P was a multi-organizational campaign with NASA, the National Center for Atmospheric Research (NCAR), and several US universities.\u202fTRACE-P deployed\u202fits payloads in the Pacific between the months of March and April 2001 with the goal of studying the air chemistry emerging\u202ffrom Asia\u202fto the western Pacific.\u202fAlong with this, TRACE-P had the objective\u202fstudying\u202fthe chemical evolution of the air as it moved away from Asia.\u202f \r\n\r\nIn order to accomplish its goals, the NASA DC-8 aircraft and NASA P-3B aircraft were deployed, each equipped with various instrumentation.\u202fTRACE-P also relied on ground sites,\u202fand\u202fsatellites\u202fto collect data. The DC-8 aircraft was equipped with 19 instruments in total\u202fwhile the P-3B\u202fboasted\u202f21 total instruments.\u202fSome instruments on the DC-8 include the Nephelometer, the GCMS, the Nitric Oxide Chemiluminescence, the Differential Absorption Lidar (DIAL), and the Dual Channel Collectors and Fluorometers, HPLC. The Nephelometer was utilized to gather data on various\u202fwavelengths\u202fincluding\u202faerosol\u202fscattering\u202f(450, 550, 700nm), aerosol absorption (565nm), equivalent BC mass, and air density ratio. The GCMS was responsible for capturing a multitude of compounds in the atmosphere, some of which include CH4, CH3CHO, CH3Br, CH3Cl, CHBr3, and C2H6O.\u202fDIAL was used for a variety of measurements, some of which include aerosol wavelength dependence (1064/587nm), IR aerosol scattering ratio (1064nm),\u202ftropopause heights and ozone columns, visible aerosol scattering ratio, composite tropospheric ozone cross-sections, and visible aerosol depolarization. Finally, the Dual Channel Collectors and Fluorometers, HPLC collected data on H2O2, CH3OOH, and CH2O in the atmosphere.\u202fThe P-3B aircraft was equipped with various instruments for TRACE-P, some of which include\u202fthe MSA/CIMS, the Non-dispersive IR Spectrometer, the PILS-Ion Chromatograph, and the\u202fCondensation particle counter and Pulse Height Analysis (PHA). The\u202fMSA/CIMS measured OH, H2SO4, MSA, and HNO3. The Non-dispersive IR Spectrometer took measurements on CO2 in the atmosphere. The PILS-Ion Chromatograph recorded measurements of compounds and elements in the atmosphere, including sodium, calcium, potassium, magnesium, chloride, NH4, NO3, and SO4. Finally, the Condensation particle counter and PHA was used to gather data on total UCN, UCN 3-8nm, and UCN 3-4nm. Along with the aircrafts, ground stations measured air quality from China along with C2H2, C2H6, CO, and HCN.\u202fFinally, satellites imagery was used to collect a multitude of data, some of the uses were to observe the history of lightning flashes,\u202fSeaWiFS\u202fcloud imagery, 8-day exposure to TOMS aerosols, and\u202fSeaWiFS\u202faerosol optical thickness. The imagery was used to best aid in planning for the aircraft deployment.",
-            "title": "TRACE-P P-3B In-Situ Trace Gas Data",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC%2FSUBORBITAL%2FTRACE-P%2FTraceGas_InSitu_P3B_Data_1",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC%2FSUBORBITAL%2FTRACE-P%2FTraceGas_InSitu_P3B_Data_1",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www-air.larc.nasa.gov/missions/tracep/tracep.htm",
-                    "description": "TRACE-P Home Page",
                     "@type": "dcat:Distribution",
+                    "description": "TRACE-P Home Page",
+                    "downloadURL": "https://www-air.larc.nasa.gov/missions/tracep/tracep.htm",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www-air.larc.nasa.gov/missions/tracep/WhitePaper.htm",
-                    "description": "TRACE-P White Paper",
                     "@type": "dcat:Distribution",
+                    "description": "TRACE-P White Paper",
+                    "downloadURL": "https://www-air.larc.nasa.gov/missions/tracep/WhitePaper.htm",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://agupubs.onlinelibrary.wiley.com/doi/epdf/10.1029/2002JD003276",
-                    "description": "Transport and Chemical Evolution over the Pacific (TRACE-P)aircraft mission: Design, execution, and first results",
                     "@type": "dcat:Distribution",
+                    "description": "Transport and Chemical Evolution over the Pacific (TRACE-P)aircraft mission: Design, execution, and first results",
+                    "downloadURL": "https://agupubs.onlinelibrary.wiley.com/doi/epdf/10.1029/2002JD003276",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www-gte.larc.nasa.gov/gte_hmpg.htm#table",
-                    "description": "GTE Home Page",
                     "@type": "dcat:Distribution",
+                    "description": "GTE Home Page",
+                    "downloadURL": "https://www-gte.larc.nasa.gov/gte_hmpg.htm#table",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/gte/guide/gte_fmt.pdf",
-                    "description": "GTE Data Format",
                     "@type": "dcat:Distribution",
+                    "description": "GTE Data Format",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/gte/guide/gte_fmt.pdf",
+                    "mediaType": "application/pdf",
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
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2812956769-LARC_CLOUD",
-                    "description": "Earthdata Search for TRACE-P_TraceGas_InSitu_P3B_Data_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for TRACE-P_TraceGas_InSitu_P3B_Data_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2812956769-LARC_CLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/ASDC/SUBORBITAL/TRACE-P/TraceGas_InSitu_P3B_Data_1",
-                    "description": "DOI data set landing page for TRACE-P_TraceGas_InSitu_P3B_Data_1",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for TRACE-P_TraceGas_InSitu_P3B_Data_1",
+                    "downloadURL": "https://doi.org/10.5067/ASDC/SUBORBITAL/TRACE-P/TraceGas_InSitu_P3B_Data_1",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 }
             ],
+            "identifier": "C2812956769-LARC_CLOUD",
+            "issued": "2001-02-01",
+            "keyword": [
+                "atmosphere",
+                "earth science",
+                "air quality",
+                "aerosols",
+                "atmospheric chemistry"
+            ],
+            "landingPage": "https://doi.org/10.5067/ASDC/SUBORBITAL/TRACE-P/TraceGas_InSitu_P3B_Data_1",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2001-04-30",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/LARC/SD/ASDC"
+            },
             "spatial": "-180.0 6.89 180.0 45.7",
+            "temporal": "1999-01-07T00:00:00Z/2002-03-01T00:00:00Z",
             "theme": [
                 "TRACE-P",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "TRACE-P P-3B In-Situ Trace Gas Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/IMPACTS/NEXRAD/DATA125",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Brodzik, Stacy .2022. KMKX NEXRAD IMPACTS [indicate subset used]. Dataset available online from the NASA Global Hydrometeorology Resource Center DAAC, Huntsville, Alabama, U.S.A. DOI: http://dx.doi.org/10.5067/IMPACTS/NEXRAD/DATA125",
-            "issued": "2022-03-23",
-            "temporal": "2020-01-01T00:04:41Z/2020-03-01T00:03:39Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-31",
-            "keyword": [
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
-            "identifier": "C2012934799-GHRC_DAAC",
             "description": "The KMKX NEXRAD IMPACTS dataset consists of Next Generation Weather Radar (NEXRAD) Level II surveillance data that were collected at 31 NEXRAD sites from January 1 to March 1, 2020 during the Investigation of Microphysics and Precipitation for Atlantic Coast-Threatening Snowstorms  (IMPACTS) field campaign. IMPACTS was a three-year sequence of winter season deployments conducted to study snowstorms over the U.S Atlantic Coast. The campaign aimed to (1) Provide observations critical to understanding the mechanisms of snowband formation, organization, and evolution; (2) Examine how the microphysical characteristics and likely growth mechanisms of snow particles vary across snowbands; and (3) Improve snowfall remote sensing interpretation and modeling to significantly advance prediction capabilities. There are currently 160 Weather Surveillance Radar-1988 Doppler (WSR-88D) or NEXRAD sites throughout the United States and abroad. This Level II dataset contains meteorological and dual-polarization base data quantities including: radar reflectivity, radial velocity, spectrum width, differential reflectivity, differential phase, and cross correlation ratio. The IMPACTS NEXRAD Level II data files are available in netCDF-4 format. It should be noted that this dataset will be updated in subsequent years of the IMPACTS campaign.",
-            "title": "KMKX NEXRAD IMPACTS V1",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FIMPACTS%2FNEXRAD%2FDATA125",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FIMPACTS%2FNEXRAD%2FDATA125",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=kmkximpacts",
-                    "description": "Files may be downloaded directly to your workstation from this link",
                     "@type": "dcat:Distribution",
+                    "description": "Files may be downloaded directly to your workstation from this link",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=kmkximpacts",
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
-                    "downloadURL": "http://www.ofcm.gov/publications/fmh/FMH11/2016FMH11PTA.pdf",
-                    "description": "Federal Meteorological Handbook No. 11 Part A: System Concepts, Responsibilities, and Procedures",
                     "@type": "dcat:Distribution",
+                    "description": "Federal Meteorological Handbook No. 11 Part A: System Concepts, Responsibilities, and Procedures",
+                    "downloadURL": "http://www.ofcm.gov/publications/fmh/FMH11/2016FMH11PTA.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View information related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "http://www.ofcm.gov/publications/fmh/FMH11/fmh11partC.pdf",
-                    "description": "Federal Meteorological Handbook No. 11 Part C: WSR-88D Products and Algorithms",
                     "@type": "dcat:Distribution",
+                    "description": "Federal Meteorological Handbook No. 11 Part C: WSR-88D Products and Algorithms",
+                    "downloadURL": "http://www.ofcm.gov/publications/fmh/FMH11/fmh11partC.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View information related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/impacts/NEXRAD/KMKX/doc/nexrad_datasets.pdf",
-                    "description": "NEXRAD IMPACTS User Guide",
                     "@type": "dcat:Distribution",
+                    "description": "NEXRAD IMPACTS User Guide",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/impacts/NEXRAD/KMKX/doc/nexrad_datasets.pdf",
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
+            "identifier": "C2012934799-GHRC_DAAC",
+            "issued": "2022-03-23",
+            "keyword": [
+                "radar",
+                "earth science",
+                "spectral/engineering"
+            ],
+            "landingPage": "https://doi.org/10.5067/IMPACTS/NEXRAD/DATA125",
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
             "spatial": "-94.199 38.838 -82.902 47.098",
+            "temporal": "2020-01-01T00:04:41Z/2020-03-01T00:03:39Z",
             "theme": [
                 "IMPACTS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "KMKX NEXRAD IMPACTS V1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://c3.nasa.gov/dashlink/resources/808/",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2013-07-23",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
-            "keyword": [
-                "ames",
-                "nasa",
-                "dashlink"
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
-            "identifier": "DASHLINK_808",
             "description": "This paper introduces a novel reasoning methodology, in combination with appropriate models and measurements (data) to perform accurately and expeditiously expert troubleshooting for complex military and industrial processes. This automated troubleshooting tool is designed to support the maintainer/ repairman by identifying and locating faulty system components. The enabling technologies build upon a Model Based Reasoning paradigm and a Dynamic Case Based Reasoning method acting as the intelligent database. A case study employs a helicopter Intermediate Gearbox as the application domain to illustrate the efficacy of the approach.",
-            "title": "A Reasoning Architecture for Expert Troubleshooting of Complex Processes",
-            "programCode": [
-                "026:029"
-            ],
             "distribution": [
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/publication/2012_PHM_Troubleshooting.pdf",
-                    "description": "2012_PHM_Troubleshooting.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "2012_PHM_Troubleshooting.pdf",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/publication/2012_PHM_Troubleshooting.pdf",
+                    "mediaType": "application/pdf",
                     "title": "2012_PHM_Troubleshooting.pdf"
                 }
             ],
-            "accrualPeriodicity": "irregular"
+            "identifier": "DASHLINK_808",
+            "issued": "2013-07-23",
+            "keyword": [
+                "ames",
+                "nasa",
+                "dashlink"
+            ],
+            "landingPage": "https://c3.nasa.gov/dashlink/resources/808/",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:029"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Dashlink"
+            },
+            "title": "A Reasoning Architecture for Expert Troubleshooting of Complex Processes"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-EXT1-1410-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the ROSETTA EXTENSION 1 phase 2016-01-01 to 2016-04-05. It is a Global Gravity measurement at the comet 67P and covers the time 2016-02-08T11:42:10.000 to 2016-02-08T12:25:32.500.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-ext1-1410-v1.0_km8p-62zq",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-EXT1-1410-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-ext1-1410-v1.0_km8p-62zq",
-            "description": "This is a Rosetta Radio Science data set, collected during the ROSETTA EXTENSION 1 phase 2016-01-01 to 2016-04-05. It is a Global Gravity measurement at the comet 67P and covers the time 2016-02-08T11:42:10.000 to 2016-02-08T12:25:32.500.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     ROSETTA EXTENSION 1 1410 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     ROSETTA EXTENSION 1 1410 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.7265/N56Q1V5R",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "International Ice Patrol (IIP) Iceberg Sightings Database, Version 1. Version 1. Archived by National Aeronautics and Space Administration, U.S. Government, National Snow and Ice Data Center. https://doi.org/10.7265/N56Q1V5R.",
-            "issued": "1960-01-01",
-            "temporal": "1960-01-01T00:00:00Z/2021-09-29T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2021-09-29",
-            "keyword": [
-                "sea ice",
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
-            "identifier": "C1386246225-NSIDCV0",
             "description": "The International Ice Patrol (IIP) has been collecting information on iceberg activity in the North Atlantic since 1913. This database contains the data from these sightings from 1960 through most current processing. The IIP data files include latitude and longitude of sighted icebergs, coded iceberg size and shape class, and date and time of the sighting. The IIP area of responsibility is 40\u00b0 N to 65\u00b0 N and 39\u00b0 W to 57\u00b0 W. Note, the IIP area of responsibility prior to 2006 was 40\u00b0 N to 52\u00b0 N and 39\u00b0 W to 57\u00b0 W. Data are in space-delimited ASCII text files and are available via FTP.",
-            "title": "International Ice Patrol (IIP) Iceberg Sightings Database, Version 1",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.7265%2FN56Q1V5R",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.7265%2FN56Q1V5R",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/forms/G00807_or.html?major_version=1",
-                    "description": "Direct download, with optional registration page.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download, with optional registration page.",
+                    "downloadURL": "https://nsidc.org/forms/G00807_or.html?major_version=1",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.7265/N56Q1V5R",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.7265/N56Q1V5R",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.7265/N56Q1V5R",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.7265/N56Q1V5R",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C1386246225-NSIDCV0",
+            "issued": "1960-01-01",
+            "keyword": [
+                "sea ice",
+                "earth science",
+                "cryosphere"
+            ],
+            "landingPage": "https://doi.org/10.7265/N56Q1V5R",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2021-09-29",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NSIDC"
+            },
             "spatial": "-60.0 40.0 -40.0 60.0",
+            "temporal": "1960-01-01T00:00:00Z/2021-09-29T23:59:59.999Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "International Ice Patrol (IIP) Iceberg Sightings Database, Version 1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1615934284-OB_DAAC.html",
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
-                "oceans",
-                "earth science",
-                "ocean temperature",
-                "national geospatial data asset"
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
-            "identifier": "C1615934284-OB_DAAC",
             "description": "MODIS (or Moderate Resolution Imaging Spectroradiometer) is a key instrument aboard the Terra (EOS AM) and Aqua (EOS PM) satellites. Terra's orbit around the Earth is timed so that it passes from north to south across the equator in the morning, while Aqua passes south to north over the equator in the afternoon. Terra MODIS and Aqua MODIS are viewing the entire Earth's surface every 1 to 2 days, acquiring data in 36 spectral bands, or groups of wavelengths (see MODIS Technical Specifications). These data will improve our understanding of global dynamics and processes occurring on the land, in the oceans, and in the lower atmosphere. MODIS is playing a vital role in the development of validated, global, interactive Earth system models able to predict global change accurately enough to assist policy makers in making sound decisions concerning the protection of our environment.",
-            "title": "Terra MODIS Global Mapped 4\u00b5m Nighttime Sea Surface Temperature (SST4) Data, version R2019.0",
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
-                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/data/10.5067/TERRA/MODIS/L3M/SST4/R2019.0",
-                    "description": "MODIS-Terra L3M 4\u00b5m Nighttime Sea Surface Temperature (SST4) Dataset Landing Page",
                     "@type": "dcat:Distribution",
+                    "description": "MODIS-Terra L3M 4\u00b5m Nighttime Sea Surface Temperature (SST4) Dataset Landing Page",
+                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/data/10.5067/TERRA/MODIS/L3M/SST4/R2019.0",
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
+            "identifier": "C1615934284-OB_DAAC",
+            "issued": "2019-06-23",
+            "keyword": [
+                "ngda",
+                "oceans",
+                "earth science",
+                "ocean temperature",
+                "national geospatial data asset"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1615934284-OB_DAAC.html",
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
+            "title": "Terra MODIS Global Mapped 4\u00b5m Nighttime Sea Surface Temperature (SST4) Data, version R2019.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/451",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Anderson, Dean, R. Striegl, and K.P. Wickland. 1999. BOREAS TF-04 SSA-YJP Tower Flux, Meteorological, and Canopy Condition Data, R1. ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/451",
-            "issued": "2023-11-22",
-            "temporal": "1993-09-02T00:00:00Z/1994-09-20T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-11-28",
-            "keyword": [
-                "atmospheric radiation",
-                "biosphere",
-                "earth science",
-                "precipitation",
-                "atmospheric water vapor",
-                "atmospheric temperature",
-                "atmospheric winds",
-                "atmospheric pressure",
-                "atmospheric chemistry",
-                "atmosphere",
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
-            "identifier": "C2808090511-ORNL_CLOUD",
             "description": "The flux and ancillary data collected at the SSA-YJP towerflux site by the TF-04 group.",
-            "graphic-preview-description": "Browse Image",
-            "title": "BOREAS TF-04 SSA-YJP Tower Flux, Meteorological, and Canopy Condition Data, R1",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/boreas_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F451",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F451",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/boreas/TF/tf04flux/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/boreas/TF/tf04flux/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/BOREAS/guides/TF04_Flux_Met.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/BOREAS/guides/TF04_Flux_Met.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/451",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/451",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TF/tf04flux/comp/tf04flux.def",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TF/tf04flux/comp/tf04flux.def",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/msword",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TF/tf04flux/comp/TF04_Flux_Met.doc",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TF/tf04flux/comp/TF04_Flux_Met.doc",
+                    "mediaType": "application/msword",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TF/tf04flux/comp/TF04_Flux_Met.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TF/tf04flux/comp/TF04_Flux_Met.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TF/tf04flux/comp/TF04_Flux_Met.txt",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TF/tf04flux/comp/TF04_Flux_Met.txt",
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
+            "identifier": "C2808090511-ORNL_CLOUD",
+            "issued": "2023-11-22",
+            "keyword": [
+                "atmospheric radiation",
+                "biosphere",
+                "earth science",
+                "precipitation",
+                "atmospheric water vapor",
+                "atmospheric temperature",
+                "atmospheric winds",
+                "atmospheric pressure",
+                "atmospheric chemistry",
+                "atmosphere",
+                "vegetation"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/451",
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
             "spatial": "53.88 -104.65",
+            "temporal": "1993-09-02T00:00:00Z/1994-09-20T23:59:59Z",
             "theme": [
                 "BOREAS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "BOREAS TF-04 SSA-YJP Tower Flux, Meteorological, and Canopy Condition Data, R1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/GPM/PR/TRMM/SLH/3A-MONTH/07",
             "citation": "Tropical Rainfall Measuring Mission (TRMM). 2021-07-29. GPM_3HSLH_TRMM. GPM PR on TRMM Spectral Latent Heating L3 1 month 0.5 degree x 0.5 degree V07. Greenbelt, MD. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/GPM/PR/TRMM/SLH/3A-MONTH/07. https://disc.gsfc.nasa.gov/datacollection/GPM_3HSLH_TRMM_07.html. Digital Science Data.",
-            "issued": "2021-07-21",
-            "temporal": "1997-12-01T00:00:00Z/2015-04-30T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2021-07-21",
-            "references": [
-                "https://doi.org/10.1175/AMSMONOGRAPHS-D-15-0013.1"
-            ],
-            "keyword": [
-                "clouds",
-                "atmosphere",
-                "earth science"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "ANDREY SAVTCHENKO",
                 "hasEmail": "mailto:Andrey.Savtchenko@nasa.gov"
             },
+            "creator": "Tropical Rainfall Measuring Mission (TRMM)",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C2264132394-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "This is the new (GPM-formated) TRMM product. It replaces the old TRMM_3H25\n\nVersion 07 is the current version of the data set. Older versions will no longer be available and have been superseded by Version 07.\n\nEstimating vertical profiles of latent heating released by precipitating cloud systems is one of the key objectives of TRMM, together with accurately measuring the horizontal distribution of tropical rainfall.\n\nThe method uses TRMM PR information [precipitation-top height (PTH), precipitation rates at the surface and melting level, and rain type] to select heating profiles from lookup tables. Heating-profile lookup tables for the three rain types\u2014convective, shallow stratiform, and anvil rain (deep stratiform with a melting level)\u2014were derived from numerical simulations of tropical cloud systems from the Tropical Ocean and Global Atmosphere Coupled Ocean\u2013Atmosphere Response Experiment (TOGA COARE) utilizing a cloud-resolving model (CRM). The SLH algorithm is severely limited by the inherent sensitivity of the TRMM PR. For latent heating, the quantity required is actually cloud top, but the PR can detect only precipitation-sized particles.\n\nBecause observed information on precipitation depth is used in addition to precipitation type and intensity, differences between shallow and deep convection are more distinct in the SLH algorithm in comparison with the CSH algorithm.\n\nMonthly Spectral Latent Heating produces 0.5 degree x 0.5 degree grid of latent heating profiles from the TRMM PR rain. The grids are in the Planetary Grid 2 structure matching the Dual-frequency PR on the core GPM observatory that covers 67S to 67N degrees of latitudes.  Areas beyond the \u00b140 degrees of latitudes are padded with empty grid cells.",
-            "release-place": "Greenbelt, MD",
-            "series-name": "GPM_3HSLH_TRMM",
-            "creator": "Tropical Rainfall Measuring Mission (TRMM)",
-            "title": "GPM PR on TRMM Spectral Latent Heating L3 1 month 0.5 degree x 0.5 degree V07 (GPM_3HSLH_TRMM) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/GPM/browse/GPM_3HSLH_TRMM.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGPM%2FPR%2FTRMM%2FSLH%2F3A-MONTH%2F07",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGPM%2FPR%2FTRMM%2FSLH%2F3A-MONTH%2F07",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
@@ -1038478,731 +1038453,769 @@
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/GPM_3HSLH_TRMM_07.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/GPM_3HSLH_TRMM_07.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc2.gesdisc.eosdis.nasa.gov/data/TRMM_L3/GPM_3HSLH_TRMM.07",
-                    "description": "Access the data via HTTPS",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS",
+                    "downloadURL": "https://disc2.gesdisc.eosdis.nasa.gov/data/TRMM_L3/GPM_3HSLH_TRMM.07",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc2.gesdisc.eosdis.nasa.gov/opendap/TRMM_L3/GPM_3HSLH_TRMM.07/",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://disc2.gesdisc.eosdis.nasa.gov/opendap/TRMM_L3/GPM_3HSLH_TRMM.07/",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=GPM_3HSLH_TRMM",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=GPM_3HSLH_TRMM",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://gpm.nasa.gov",
-                    "description": "TRMM Project Home Page",
                     "@type": "dcat:Distribution",
+                    "description": "TRMM Project Home Page",
+                    "downloadURL": "https://gpm.nasa.gov",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
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
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/GPM/README.TRMM.pdf",
-                    "description": "README Document",
                     "@type": "dcat:Distribution",
+                    "description": "README Document",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/GPM/README.TRMM.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's read me document"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://pps.gsfc.nasa.gov/Documents/CSH_ATBD.pdf",
-                    "description": "Details of the caveats to consider in this product.",
                     "@type": "dcat:Distribution",
+                    "description": "Details of the caveats to consider in this product.",
+                    "downloadURL": "https://pps.gsfc.nasa.gov/Documents/CSH_ATBD.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://pps.gsfc.nasa.gov/Documents/V7A_SLH_caveats.pdf",
-                    "description": "Details of the caveats to consider in this product.",
                     "@type": "dcat:Distribution",
+                    "description": "Details of the caveats to consider in this product.",
+                    "downloadURL": "https://pps.gsfc.nasa.gov/Documents/V7A_SLH_caveats.pdf",
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
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/GPM/browse/GPM_3HSLH_TRMM.png",
+            "identifier": "C2264132394-GES_DISC",
+            "issued": "2021-07-21",
+            "keyword": [
+                "clouds",
+                "atmosphere",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/GPM/PR/TRMM/SLH/3A-MONTH/07",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2021-07-21",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
+            },
+            "references": [
+                "https://doi.org/10.1175/AMSMONOGRAPHS-D-15-0013.1"
+            ],
+            "release-place": "Greenbelt, MD",
+            "series-name": "GPM_3HSLH_TRMM",
             "spatial": "-180.0 -67.0 180.0 67.0",
+            "temporal": "1997-12-01T00:00:00Z/2015-04-30T23:59:59.999Z",
             "theme": [
                 "TRMM",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "GPM PR on TRMM Spectral Latent Heating L3 1 month 0.5 degree x 0.5 degree V07 (GPM_3HSLH_TRMM) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/SMODE-SEAGL2",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "S-MODE Team. 2023-10-01. S-MODE Seaglider Observations Version 1. Version 1. S-MODE Seaglider Observations Version 1. Archived by National Aeronautics and Space Administration, U.S. Government, S-MODE Project Data Manager, Frederick Bingham. https://doi.org/10.5067/SMODE-SEAGL2. http://podaac.jpl.nasa.gov/S-MODE.",
-            "issued": "2022-08-23",
-            "temporal": "2022-08-23T00:00:00Z/2023-07-07T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-06",
-            "keyword": [
-                "ocean circulation",
-                "ocean chemistry",
-                "salinity/density",
-                "oceans",
-                "ocean optics",
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
-            "identifier": "C2766303078-POCLOUD",
-            "description": "This dataset contains profiles of temperature, dissolved oxygen, salinity, and other observations collected by Seagliders during the Sub-Mesoscale Ocean Dynamics Experiment (S-MODE) field campaign. The experiment was conducted approximately 300 km offshore of San Francisco, during two intensive operating periods in Fall 2022 and Spring 2023. S-MODE aims to understand how ocean dynamics acting on short spatial scales influence the vertical exchange of physical and biological variables in the ocean. Seagliders are autonomous underwater vehicles (AUVs) designed to glide from the ocean surface to as deep as 1000 m and back while\r\ncollecting profiles of oceanic variables. Data are available in netCDF format.",
-            "series-name": "S-MODE Seaglider Observations Version 1",
-            "graphic-preview-description": "Thumbnail",
             "creator": "S-MODE Team",
-            "title": "S-MODE Seaglider Observations Version 1",
-            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/SMODE_L2_SEAGLIDER_V1.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "This dataset contains profiles of temperature, dissolved oxygen, salinity, and other observations collected by Seagliders during the Sub-Mesoscale Ocean Dynamics Experiment (S-MODE) field campaign. The experiment was conducted approximately 300 km offshore of San Francisco, during two intensive operating periods in Fall 2022 and Spring 2023. S-MODE aims to understand how ocean dynamics acting on short spatial scales influence the vertical exchange of physical and biological variables in the ocean. Seagliders are autonomous underwater vehicles (AUVs) designed to glide from the ocean surface to as deep as 1000 m and back while\r\ncollecting profiles of oceanic variables. Data are available in netCDF format.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSMODE-SEAGL2",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSMODE-SEAGL2",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://smode.whoi.edu/",
-                    "description": "Project Website for S-MODE hosted by Woods Hole Oceanographic Institute (WHOI)",
                     "@type": "dcat:Distribution",
+                    "description": "Project Website for S-MODE hosted by Woods Hole Oceanographic Institute (WHOI)",
+                    "downloadURL": "http://smode.whoi.edu/",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://podaac.jpl.nasa.gov/s-mode",
-                    "description": "Project Landing Page for S-MODE on the PO.DAAC Website",
                     "@type": "dcat:Distribution",
+                    "description": "Project Landing Page for S-MODE on the PO.DAAC Website",
+                    "downloadURL": "http://podaac.jpl.nasa.gov/s-mode",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/SMODE_L2_SEAGLIDER_V1.jpg",
-                    "description": "Thumbnail",
                     "@type": "dcat:Distribution",
+                    "description": "Thumbnail",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/SMODE_L2_SEAGLIDER_V1.jpg",
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
-                    "downloadURL": "https://github.com/NASA-SMODE",
-                    "description": "S-MODE GitHub Organization",
                     "@type": "dcat:Distribution",
+                    "description": "S-MODE GitHub Organization",
+                    "downloadURL": "https://github.com/NASA-SMODE",
+                    "mediaType": "text/html",
                     "title": "View information related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2766303078-POCLOUD",
-                    "description": "Browse and download granules over HTTPS using the virtual directories",
                     "@type": "dcat:Distribution",
+                    "description": "Browse and download granules over HTTPS using the virtual directories",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2766303078-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2766303078-POCLOUD",
-                    "description": "Browse granule search results in Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse granule search results in Earthdata Search",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2766303078-POCLOUD",
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
-                    "mediaType": "text/html",
-                    "downloadURL": "https://espo.nasa.gov/s-mode/content/S-MODE_2022_Open_Data_Workshop",
-                    "description": "2022 S-MODE Open Data Workshop Information",
                     "@type": "dcat:Distribution",
+                    "description": "2022 S-MODE Open Data Workshop Information",
+                    "downloadURL": "https://espo.nasa.gov/s-mode/content/S-MODE_2022_Open_Data_Workshop",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://espo.nasa.gov/s-mode/content/S-MODE_2022_ODW_Recording_and_Presentations",
-                    "description": "2022 S-MODE Open Data Workshop Presentations and Recordings",
                     "@type": "dcat:Distribution",
+                    "description": "2022 S-MODE Open Data Workshop Presentations and Recordings",
+                    "downloadURL": "https://espo.nasa.gov/s-mode/content/S-MODE_2022_ODW_Recording_and_Presentations",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://github.com/podaac/2022-SMODE-Open-Data-Workshop",
-                    "description": "2022 S-MODE Open Data Workshop Code and Tutorials",
                     "@type": "dcat:Distribution",
+                    "description": "2022 S-MODE Open Data Workshop Code and Tutorials",
+                    "downloadURL": "https://github.com/podaac/2022-SMODE-Open-Data-Workshop",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "graphic-preview-description": "Thumbnail",
+            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/SMODE_L2_SEAGLIDER_V1.jpg",
+            "identifier": "C2766303078-POCLOUD",
+            "issued": "2022-08-23",
+            "keyword": [
+                "ocean circulation",
+                "ocean chemistry",
+                "salinity/density",
+                "oceans",
+                "ocean optics",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/SMODE-SEAGL2",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2023-07-06",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/JPL/PODAAC"
+            },
+            "series-name": "S-MODE Seaglider Observations Version 1",
             "spatial": "-125.4 36.3 -122.9 38.1",
+            "temporal": "2022-08-23T00:00:00Z/2023-07-07T00:00:00Z",
             "theme": [
                 "S-MODE",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "S-MODE Seaglider Observations Version 1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/MEASURES/DMSP-F10/SSMI/DATA304",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Wentz, Frank J, Kyle Hilburn and Deborah K Smith.2012. RSS SSM/I OCEAN PRODUCT GRIDS MONTHLY AVERAGE FROM DMSP F10 NETCDF [indicate subset used]. Dataset available online from the NASA Global Hydrometeorology Resource Center DAAC, Huntsville, Alabama, U.S.A. DOI: http://dx.doi.org/10.5067/MEASURES/DMSP-F10/SSMI/DATA304",
-            "issued": "2012-08-08",
-            "temporal": "1990-12-01T00:00:00Z/1997-11-30T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-04-28",
-            "keyword": [
-                "atmospheric winds",
-                "atmosphere",
-                "atmospheric water vapor",
-                "clouds",
-                "earth science",
-                "oceans",
-                "ocean winds",
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
-            "identifier": "C1979902952-GHRC_DAAC",
             "description": "The RSS SSM/I Ocean Product Grids Monthly Average from DMSP F10 netCDF dataset is part of the collection of Special Sensor Microwave/Imager (SSM/I) and Special Sensor Microwave Imager Sounder (SSMIS) data products produced as part of NASA's MEaSUREs Program. Remote Sensing Systems generates SSM/I and SSMIS binary data products using a unified, physically based algorithm to simultaneously retrieve ocean wind speed, water vapor, cloud water, and rain rate. The SSMIS data have been carefully intercalibrated to the brightness temperature level of the previous SSM/I and therefore extend this important time series of ocean winds, vapor, cloud and rain values. This algorithm is a product of 20 years of refinements, improvements, and verifications. The Global Hydrology Resource Center has reformatted the binary data into a netCDF data product for each temporal group for each satellite. The netCDF SSMI/SSMIS collection will be available for F10 for monthly averages.",
-            "graphic-preview-description": "N/A",
-            "title": "RSS SSM/I OCEAN PRODUCT GRIDS MONTHLY AVERAGE FROM DMSP F10 NETCDF V7",
-            "graphic-preview-file": "https://ghrc.nsstc.nasa.gov/pub/ssmi/f10/monthly/browse/",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMEASURES%2FDMSP-F10%2FSSMI%2FDATA304",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMEASURES%2FDMSP-F10%2FSSMI%2FDATA304",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=rssmif10m",
-                    "description": "Files may be downloaded directly to your workstation from this link",
                     "@type": "dcat:Distribution",
+                    "description": "Files may be downloaded directly to your workstation from this link",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=rssmif10m",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/ssmi/f10/monthly/browse/1996/f10_ssmi_199607v7_WV.png",
-                    "description": "Sample browse image",
                     "@type": "dcat:Distribution",
+                    "description": "Sample browse image",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/ssmi/f10/monthly/browse/1996/f10_ssmi_199607v7_WV.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/ssmi/f10/monthly/browse/1996/f10_ssmi_199607v7_WS.png",
-                    "description": "Sample browse image",
                     "@type": "dcat:Distribution",
+                    "description": "Sample browse image",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/ssmi/f10/monthly/browse/1996/f10_ssmi_199607v7_WS.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/ssmi/f10/monthly/browse/1996/f10_ssmi_199607v7_RR.png",
-                    "description": "Sample browse image",
                     "@type": "dcat:Distribution",
+                    "description": "Sample browse image",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/ssmi/f10/monthly/browse/1996/f10_ssmi_199607v7_RR.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/ssmi/f10/monthly/browse/1996/f10_ssmi_199607v7_CW.png",
-                    "description": "Sample browse image",
                     "@type": "dcat:Distribution",
+                    "description": "Sample browse image",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/ssmi/f10/monthly/browse/1996/f10_ssmi_199607v7_CW.png",
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
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/opendap/ssmi/f10/monthly/",
-                    "description": "OPeNDAP server dataset access",
                     "@type": "dcat:Distribution",
+                    "description": "OPeNDAP server dataset access",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/opendap/ssmi/f10/monthly/",
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
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/ssmi/f10/monthly/browse/",
-                    "description": "N/A",
                     "@type": "dcat:Distribution",
+                    "description": "N/A",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/ssmi/f10/monthly/browse/",
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
+            "graphic-preview-file": "https://ghrc.nsstc.nasa.gov/pub/ssmi/f10/monthly/browse/",
+            "identifier": "C1979902952-GHRC_DAAC",
+            "issued": "2012-08-08",
+            "keyword": [
+                "atmospheric winds",
+                "atmosphere",
+                "atmospheric water vapor",
+                "clouds",
+                "earth science",
+                "oceans",
+                "ocean winds",
+                "precipitation"
+            ],
+            "landingPage": "https://doi.org/10.5067/MEASURES/DMSP-F10/SSMI/DATA304",
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
+            "temporal": "1990-12-01T00:00:00Z/1997-11-30T23:59:59Z",
             "theme": [
                 "DISCOVER",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "RSS SSM/I OCEAN PRODUCT GRIDS MONTHLY AVERAGE FROM DMSP F10 NETCDF V7"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MSL-M-NAVCAM-5-RDR-MOSAIC-V1.0",
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
-                "mars science laboratory"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "Unknown",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.msl-m-navcam-5-rdr-mosaic-v1.0_kmmx-myk3",
+            "issued": "2021-05-21",
+            "keyword": [
+                "mars",
+                "mars science laboratory"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MSL-M-NAVCAM-5-RDR-MOSAIC-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.msl-m-navcam-5-rdr-mosaic-v1.0_kmmx-myk3",
-            "description": "Unknown",
-            "title": "MSL MARS NAVIGATION CAMERA 5 RDR MOSAIC V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "MSL MARS NAVIGATION CAMERA 5 RDR MOSAIC V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/SUBORBITAL/ACEPOL2017/AircraftRemoteSensing_HSRL2_Data_1",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2020-05-27. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/SUBORBITAL/ACEPOL2017/AircraftRemoteSensing_HSRL2_Data_1.",
-            "issued": "2020-03-27",
-            "temporal": "2017-10-23T00:00:00Z/2017-11-09T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-04-08",
-            "keyword": [
-                "atmosphere",
-                "clouds",
-                "earth science",
-                "aerosols"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Kirk  Knobelspiesse",
                 "hasEmail": "mailto:kirk.d.knobelspiesse@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/LARC/SD/ASDC"
-            },
-            "identifier": "C1758588330-LARC_ASDC",
             "description": "ACEPOL High Spectral Resolution Lidar 2 (HSRL-2) Remotely Sensed Data (ACEPOL_AircraftRemoteSensing_HSRL2_Data) are remotely sensed measurements collected by the High-Spectral Resolution Lidar (HSRL-2) onboard the ER-2 during ACEPOL. In order to improve our understanding of the effect of aerosols on climate and air quality, measurements of aerosol chemical composition, size distribution, height profile, and optical properties are of crucial importance. In terms of remotely sensed instrumentation, the most extensive set of aerosol properties can be obtained by combining passive multi-angle, multi-spectral measurements of intensity and polarization with active measurements performed by a High Spectral Resolution Lidar. During Fall 2017, the Aerosol Characterization from Polarimeter and Lidar (ACEPOL) campaign, jointly sponsored by NASA and the Netherlands Institute for Space Research (SRON), performed aerosol and cloud measurements over the United States from the NASA high altitude ER-2 aircraft. Six instruments were deployed on the aircraft. Four of these instruments were multi-angle polarimeters: the Airborne Hyper Angular Rainbow Polarimeter (AirHARP), the Airborne Multiangle SpectroPolarimetric Imager (AirMSPI), the Airborne Spectrometer for Planetary Exploration (SPEX Airborne) and the Research Scanning Polarimeter (RSP). The other two instruments were lidars: the High Spectral Resolution Lidar 2 (HSRL-2) and the Cloud Physics Lidar (CPL). The ACEPOL operation was based at NASA\u2019s Armstrong Flight Research Center in Palmdale California, which enabled observations of a wide variety of scene types, including urban, desert, forest, coastal ocean and agricultural areas, with clear, cloudy, polluted and pristine atmospheric conditions. The primary goal of ACEPOL was to assess the capabilities of the different polarimeters for retrieval of aerosol and cloud microphysical and optical parameters, as well as their capabilities to derive aerosol layer height (near-UV polarimetry, O2 A-band). ACEPOL also focused on the development and evaluation of aerosol retrieval algorithms that combine data from both active (lidar) and passive (polarimeter) instruments. ACEPOL data are appropriate for algorithm development and testing, instrument intercomparison, and investigations of active and passive instrument data fusion, which make them valuable resources for remote sensing communities as they prepare for the next generation of spaceborne MAP and lidar missions.",
-            "title": "ACEPOL High Spectral Resolution Lidar 2 (HSRL-2) Remotely Sensed Data",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSUBORBITAL%2FACEPOL2017%2FAircraftRemoteSensing_HSRL2_Data_1",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSUBORBITAL%2FACEPOL2017%2FAircraftRemoteSensing_HSRL2_Data_1",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://airbornescience.nasa.gov/acepwg/content/ACE_Polarimeter_Working_Group_ACEPWG_ACEPOL_field_campaign",
-                    "description": "NASA Airborne Science Program Overview of ACEPWG ACEPOL/LIREX field campaign",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Airborne Science Program Overview of ACEPWG ACEPOL/LIREX field campaign",
+                    "downloadURL": "https://airbornescience.nasa.gov/acepwg/content/ACE_Polarimeter_Working_Group_ACEPWG_ACEPOL_field_campaign",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/SUBORBITAL/ACEPOL2017/AircraftRemoteSensing_HSRL2_Data_1",
-                    "description": "DOI data set landing page for ACEPOL_AircraftRemoteSensing_HSRL2_Data_1",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for ACEPOL_AircraftRemoteSensing_HSRL2_Data_1",
+                    "downloadURL": "https://doi.org/10.5067/SUBORBITAL/ACEPOL2017/AircraftRemoteSensing_HSRL2_Data_1",
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
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1758588330-LARC_ASDC",
-                    "description": "Earthdata Search for ACEPOL_AircraftRemoteSensing_HSRL2_Data_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for ACEPOL_AircraftRemoteSensing_HSRL2_Data_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1758588330-LARC_ASDC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www-air.larc.nasa.gov/missions/acepol/index.html/",
-                    "description": "NASA LaRC Airborne Science Data for Atmospheric Composition ACEPOL Home Page",
                     "@type": "dcat:Distribution",
+                    "description": "NASA LaRC Airborne Science Data for Atmospheric Composition ACEPOL Home Page",
+                    "downloadURL": "https://www-air.larc.nasa.gov/missions/acepol/index.html/",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.nwo.nl/en/projects/alw-go16-09/",
-                    "description": "Netherlands Organization for Scientific Research (NWO) ACEPOL Home Page",
                     "@type": "dcat:Distribution",
+                    "description": "Netherlands Organization for Scientific Research (NWO) ACEPOL Home Page",
+                    "downloadURL": "https://www.nwo.nl/en/projects/alw-go16-09/",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://gmao.gsfc.nasa.gov/field_campaigns/ACEPOL/",
-                    "description": "Global Modeling and Assimilation Office (GMAO) ACEPOL Support Website",
                     "@type": "dcat:Distribution",
+                    "description": "Global Modeling and Assimilation Office (GMAO) ACEPOL Support Website",
+                    "downloadURL": "https://gmao.gsfc.nasa.gov/field_campaigns/ACEPOL/",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/soot/power-user/ACEPOL/2017",
-                    "description": "ACEPOL Data on the Sub-Orbital Order Tool (SOOT) Power User Interface (UI)",
                     "@type": "dcat:Distribution",
+                    "description": "ACEPOL Data on the Sub-Orbital Order Tool (SOOT) Power User Interface (UI)",
+                    "downloadURL": "https://asdc.larc.nasa.gov/soot/power-user/ACEPOL/2017",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through the Sub-Orbital Order Tool"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/ACEPOL/AircraftRemoteSensing_HSRL2_Data_1/",
-                    "description": "ASDC Direct Data Download for ACEPOL_AircraftRemoteSensing_HSRL2_Data_1",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for ACEPOL_AircraftRemoteSensing_HSRL2_Data_1",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/ACEPOL/AircraftRemoteSensing_HSRL2_Data_1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/ACEPOL/AircraftRemoteSensing_HSRL2_Data_1/contents.html",
-                    "description": "OPeNDAP data access for ACEPOL_AircraftRemoteSensing_HSRL2_Data_1",
                     "@type": "dcat:Distribution",
+                    "description": "OPeNDAP data access for ACEPOL_AircraftRemoteSensing_HSRL2_Data_1",
+                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/ACEPOL/AircraftRemoteSensing_HSRL2_Data_1/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 }
             ],
+            "identifier": "C1758588330-LARC_ASDC",
+            "issued": "2020-03-27",
+            "keyword": [
+                "atmosphere",
+                "clouds",
+                "earth science",
+                "aerosols"
+            ],
+            "landingPage": "https://doi.org/10.5067/SUBORBITAL/ACEPOL2017/AircraftRemoteSensing_HSRL2_Data_1",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2022-04-08",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/LARC/SD/ASDC"
+            },
             "spatial": "<?xml version=\"1.0\" encoding=\"UTF-8\"?><gml:Polygon xmlns:gml=\"http://www.opengis.net/gml/3.2\" srsName=\"EPSG:9825\"><gml:outerBoundaryIs><gml:LinearRing><gml:posList>25.0 -130.0 25.0 -100.0 45.0 -100.0 45.0 -130.0 25.0 -130.0</gml:posList></gml:LinearRing></gml:outerBoundaryIs><gml:innerBoundaryIs></gml:innerBoundaryIs></gml:Polygon>",
+            "temporal": "2017-10-23T00:00:00Z/2017-11-09T23:59:59.999Z",
             "theme": [
                 "ACEPOL",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "ACEPOL High Spectral Resolution Lidar 2 (HSRL-2) Remotely Sensed Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-X-REX-2-PLUTOCRUISE-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This data set contains Raw data taken by the New Horizons Radio Science Experiment instrument during the pluto cruise mission phase.  This is VERSION 1.0 of this data set.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-x-rex-2-plutocruise-v1.0_kmnn-zzfp",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "new horizons",
                 "earth",
                 "sun",
                 "calibration"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-X-REX-2-PLUTOCRUISE-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-x-rex-2-plutocruise-v1.0_kmnn-zzfp",
-            "description": "This data set contains Raw data taken by the New Horizons Radio Science Experiment instrument during the pluto cruise mission phase.  This is VERSION 1.0 of this data set.",
-            "title": "NEW HORIZONS\n      REX PLUTO CRUISE\n      RAW V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "NEW HORIZONS\n      REX PLUTO CRUISE\n      RAW V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-4-ESC3-67PCHURYUMOV-M19-V2.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This CODMAC level 4 data set contains radiometric calibrated and geometric distortion corrected (resampled) image data in W/m^2/sr/nm, acquired by the OSIRIS Wide Angle Camera on the Rosetta spacecraft during the COMET ESCORT 3 mission phase, covering the period from 2015-07-28T23:25:00.000 to 2015-08-25T23:24:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V2.0 supersedes previous deliveries of the same dataset with the following changes since the last version: Lien corrected dataset after October 2018 PSA/PDS external peer review. Updated documentation and ancillary files, added document on bandpass filter. Updated SCIENCE_USER_GUIDE_V03.PDF to include one section about FAQ and one section about image data quality. Added shutter backtravel and readout issues to image quality map. Updated DATA_QUALITY_ID keyword in image header. Improved handling of images with missing packets.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-4-esc3-67pchuryumov-m19-v2.0",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2021-05-21",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "vega",
                 "zeta cas",
                 "international rosetta mission",
                 "67p/churyumov-gerasimenko 1 (1969 r1)"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-4-ESC3-67PCHURYUMOV-M19-V2.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-4-esc3-67pchuryumov-m19-v2.0",
-            "description": "This CODMAC level 4 data set contains radiometric calibrated and geometric distortion corrected (resampled) image data in W/m^2/sr/nm, acquired by the OSIRIS Wide Angle Camera on the Rosetta spacecraft during the COMET ESCORT 3 mission phase, covering the period from 2015-07-28T23:25:00.000 to 2015-08-25T23:24:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V2.0 supersedes previous deliveries of the same dataset with the following changes since the last version: Lien corrected dataset after October 2018 PSA/PDS external peer review. Updated documentation and ancillary files, added document on bandpass filter. Updated SCIENCE_USER_GUIDE_V03.PDF to include one section about FAQ and one section about image data quality. Added shutter backtravel and readout issues to image quality map. Updated DATA_QUALITY_ID keyword in image header. Improved handling of images with missing packets.",
-            "title": "ROSETTA-ORBITER 67P OSIWAC 4 ESC3-MTP019 RDR V2.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P OSIWAC 4 ESC3-MTP019 RDR V2.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/788",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Trouet, V. 2005. SAFARI 2000 Tree Ring Data, Mongu, Zambia, Dry Season 2000. ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/788",
-            "issued": "2023-10-18",
-            "temporal": "1953-01-01T00:00:00Z/2000-08-31T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-10-25",
-            "keyword": [
-                "earth science",
-                "biosphere",
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
-            "identifier": "C2789727146-ORNL_CLOUD",
             "description": "This data set contains tree ring data from three sites located about 25 km of the meteorological station at Mongu, Zambia. Data from about 50 individual trees are reported. In addition, chronologies (or site mean curves) that better represent common influences (e.g., in this study, the climatic signal) were developed for each site based on the individual data (Trouet, 2004; Trouet et al., 2001). The series covers a maximum of 46 years, although most series do not extend longer than 30 years. The data were collected during the SAFARI 2000 Dry Season Field Campaign of August 2000.Ten to 23 samples were taken at each site. Brachystegia bakeriana was sampled at site 1, and Brachystegia spiciformis at sites 2 and 3. The vegetation at all sites underwent primitive harvesting for subsistence earlier the same year, thus samples could be taken from freshly cut trees and no living trees were cut. At all sites, samples consisted of full stem discs. Where possible, samples were taken at breast height (1.3 m) or slightly lower. Growth ring widths were measured to the nearest 0.01 mm using LINTAB equipment and TSAP software (Rinn and Jakel, 1997). Four radii per sample disc were measured. Cross-dating and response function analyses were performed by routine dendrochronological techniques. There are two files for each site, one containing integer values representing tree ring widths (raw data), and the other containing standardized values (chronologies), for each year. The data are stored as ASCII table files in comma-separated-value (.csv) format, with column headers.",
-            "graphic-preview-description": "Browse Image",
-            "title": "SAFARI 2000 Tree Ring Data, Mongu, Zambia, Dry Season 2000",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/safari_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F788",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F788",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/safari2k/field_campaign/mongu_tree_rings/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/safari2k/field_campaign/mongu_tree_rings/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/S2K/guides/mongu_tree_rings.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/S2K/guides/mongu_tree_rings.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/788",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/788",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/safari2k/field_campaign/mongu_tree_rings/comp/mongu_tree_rings_readme.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/safari2k/field_campaign/mongu_tree_rings/comp/mongu_tree_rings_readme.pdf",
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
+            "identifier": "C2789727146-ORNL_CLOUD",
+            "issued": "2023-10-18",
+            "keyword": [
+                "earth science",
+                "biosphere",
+                "ecosystems",
+                "vegetation"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/788",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2023-10-25",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "ORNL_DAAC"
+            },
             "spatial": "23.26 -15.45 23.32 -15.19",
+            "temporal": "1953-01-01T00:00:00Z/2000-08-31T23:59:59Z",
             "theme": [
                 "SAFARI 2000",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "SAFARI 2000 Tree Ring Data, Mongu, Zambia, Dry Season 2000"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://pmm.nasa.gov/data-access",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Dr. Gail Skofronick-Jackson",
+                "hasEmail": "mailto:gail.s.jackson@nasa.gov"
+            },
+            "describedBy": "http://pmm.nasa.gov/data-access/data-sources/",
+            "description": "Tropical Rainfall Measuring Mission (TRMM) data products are currently available from 1998 to the present. Global Precipitation Measurement (GPM) mission data products are currently available from March 2014 to the present. TRMM and GPM are joint missions between NASA and the Japan Aerospace Exploration Agency (JAXA) designed to monitor and study global precipitation. Here we outline the types of products currently available for TRMM and GPM and the various ways to query, view and download these precipitation products.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://pmm.nasa.gov/data-access/downloads/gpm",
+                    "mediaType": "text/html"
+                }
+            ],
+            "identifier": "NASA-0000105__1",
             "issued": "2018-06-25",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
             "keyword": [
                 "radiance",
                 "earth science",
@@ -1039217,806 +1039230,770 @@
                 "precipitation",
                 "nasa"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Dr. Gail Skofronick-Jackson",
-                "hasEmail": "mailto:gail.s.jackson@nasa.gov"
-            },
+            "landingPage": "http://pmm.nasa.gov/data-access",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "NASA-0000105__1",
-            "description": "Tropical Rainfall Measuring Mission (TRMM) data products are currently available from 1998 to the present. Global Precipitation Measurement (GPM) mission data products are currently available from March 2014 to the present. TRMM and GPM are joint missions between NASA and the Japan Aerospace Exploration Agency (JAXA) designed to monitor and study global precipitation. Here we outline the types of products currently available for TRMM and GPM and the various ways to query, view and download these precipitation products.",
-            "title": "Precipitation Measurement Missions Data Access",
-            "programCode": [
-                "026:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://pmm.nasa.gov/data-access/downloads/gpm",
-                    "mediaType": "text/html"
-                }
-            ],
-            "describedBy": "http://pmm.nasa.gov/data-access/data-sources/",
-            "accrualPeriodicity": "irregular"
+            "title": "Precipitation Measurement Missions Data Access"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC4-1205-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 4 phase 2015-10-22 to 2015-12-31. It is a Global Gravity measurement at the comet 67P and covers the time 2015-11-23T08:16:50.000 to 2015-11-23T10:09:12.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc4-1205-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC4-1205-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc4-1205-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 4 phase 2015-10-22 to 2015-12-31. It is a Global Gravity measurement at the comet 67P and covers the time 2015-11-23T08:16:50.000 to 2015-11-23T10:09:12.000.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 4 1205 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 4 1205 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-PRL-0300-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the PRELANDING phase 2014-01-21 to 2014-11-18. It is a Global Gravity measurement at the comet 67P and covers the time 2014-09-17T17:01:03.000 to 2014-09-18T03:42:45.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-prl-0300-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-PRL-0300-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-prl-0300-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the PRELANDING phase 2014-01-21 to 2014-11-18. It is a Global Gravity measurement at the comet 67P and covers the time 2014-09-17T17:01:03.000 to 2014-09-18T03:42:45.000.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     PRELANDING 0300 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     PRELANDING 0300 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG1-J-PLS-5-ION-MOM-96.0SEC",
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
-                "voyager"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "THIS DATA SET CONTAINS THE BEST ESTIMATES OF THE TOTAL ION DENSITY AT JUPITER DURING THE VOYAGER 1 ENCOUNTER IN THE PLS VOLTAGE RANGE (10-5950 EV/Q). IT IS CALCULATED USING THE METHOD OF MCNUTT ET AL. (1981) WHICH TO FIRST ORDER CONSISTS OF TAKING THE TOTAL MEASURED CURRENT AND DIVIDING BY THE COLLECTOR AREA AND PLASMA BULK VELOCITY. THIS METHOD IS ONLY ACCURATE FOR HIGH MACH NUMBER FLOWS DIRECTLY INTO THE DETECTOR, AND MAY RESULT IN UNDERESTIMATES OF THE TOTAL DENSITY OF A FACTOR OF 2 IN THE OUTER MAGNETOSPHERE. THUS ABSOLUTE DENSITIES SHOULD BE TREATED WITH CAUTION, BUT DENSITY VARIATIONS IN THE DATA SET CAN BE TRUSTED. THE LOW RESOLUTION MODE DENSITY IS USED BEFORE 1979 63 1300, AFTER THIS THE LARGER OF THE HIGH AND LOW RESOLUTION MODE DENSITIES IN A 96 SEC PERIOD IS USED SINCE THE L-MODE SPECTRA OFTEN ARE SATURATED. COROTATION IS ASSUMED INSIDE L=17.5, AND A CONSTANT VELOCITY COMPONENT OF 200 KM/S INTO THE D CUP IS USED OUTSIDE OF THIS. THESE ARE THE DENSITIES GIVEN IN THE MCNUTT ET AL. (1981) PAPER CORRECTED BY A FACTOR OF 1.209 (.9617) FOR DENSITIES OBTAINED FROM THE SIDE (MAIN) SENSOR. THIS CORRECTION IS DUE TO A BETTER CALCULATION OF THE EFFECTIVE AREA OF THE SENSORS. DATA FORMAT: COLUMNS 1-6 ARE TIME (YEAR, DAY, HOUR, MIN, SEC, MSEC) COLUMN 7 IS THE MOMENT DENSITY IN CM-3. EACH ROW HAS FORMAT (6I4, E12.3). VALUES OF 1.E32 INDICATE THAT THE PARAMETER COULD NOT BE OBTAINED FROM THE DATA USING THE STANDARD ANALYSIS TECHNIQUE. ADDITIONAL INFORMATION ABOUT THIS DATASET AND THE INSTRUMENT WHICH PRODUCED IT CAN BE FOUND ELSEWHERE IN THIS CATALOG. AN OVERVIEW OF THE DATA IN THIS DATA SET CAN BE FOUND IN MCNUTT ET AL. (1981) AND A COMPLETE INSTRUMENT DESCRIPTION CAN BE FOUND IN BRIDGE (1977).",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg1-j-pls-5-ion-mom-96.0sec_kmx8-mqrr",
+            "issued": "2018-06-26",
+            "keyword": [
+                "jupiter",
+                "voyager"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG1-J-PLS-5-ION-MOM-96.0SEC",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg1-j-pls-5-ion-mom-96.0sec_kmx8-mqrr",
-            "description": "THIS DATA SET CONTAINS THE BEST ESTIMATES OF THE TOTAL ION DENSITY AT JUPITER DURING THE VOYAGER 1 ENCOUNTER IN THE PLS VOLTAGE RANGE (10-5950 EV/Q). IT IS CALCULATED USING THE METHOD OF MCNUTT ET AL. (1981) WHICH TO FIRST ORDER CONSISTS OF TAKING THE TOTAL MEASURED CURRENT AND DIVIDING BY THE COLLECTOR AREA AND PLASMA BULK VELOCITY. THIS METHOD IS ONLY ACCURATE FOR HIGH MACH NUMBER FLOWS DIRECTLY INTO THE DETECTOR, AND MAY RESULT IN UNDERESTIMATES OF THE TOTAL DENSITY OF A FACTOR OF 2 IN THE OUTER MAGNETOSPHERE. THUS ABSOLUTE DENSITIES SHOULD BE TREATED WITH CAUTION, BUT DENSITY VARIATIONS IN THE DATA SET CAN BE TRUSTED. THE LOW RESOLUTION MODE DENSITY IS USED BEFORE 1979 63 1300, AFTER THIS THE LARGER OF THE HIGH AND LOW RESOLUTION MODE DENSITIES IN A 96 SEC PERIOD IS USED SINCE THE L-MODE SPECTRA OFTEN ARE SATURATED. COROTATION IS ASSUMED INSIDE L=17.5, AND A CONSTANT VELOCITY COMPONENT OF 200 KM/S INTO THE D CUP IS USED OUTSIDE OF THIS. THESE ARE THE DENSITIES GIVEN IN THE MCNUTT ET AL. (1981) PAPER CORRECTED BY A FACTOR OF 1.209 (.9617) FOR DENSITIES OBTAINED FROM THE SIDE (MAIN) SENSOR. THIS CORRECTION IS DUE TO A BETTER CALCULATION OF THE EFFECTIVE AREA OF THE SENSORS. DATA FORMAT: COLUMNS 1-6 ARE TIME (YEAR, DAY, HOUR, MIN, SEC, MSEC) COLUMN 7 IS THE MOMENT DENSITY IN CM-3. EACH ROW HAS FORMAT (6I4, E12.3). VALUES OF 1.E32 INDICATE THAT THE PARAMETER COULD NOT BE OBTAINED FROM THE DATA USING THE STANDARD ANALYSIS TECHNIQUE. ADDITIONAL INFORMATION ABOUT THIS DATASET AND THE INSTRUMENT WHICH PRODUCED IT CAN BE FOUND ELSEWHERE IN THIS CATALOG. AN OVERVIEW OF THE DATA IN THIS DATA SET CAN BE FOUND IN MCNUTT ET AL. (1981) AND A COMPLETE INSTRUMENT DESCRIPTION CAN BE FOUND IN BRIDGE (1977).",
-            "title": "VOYAGER 1 JUPITER PLASMA DERIVED ION MOMENTS 96 SEC",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "VOYAGER 1 JUPITER PLASMA DERIVED ION MOMENTS 96 SEC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MSL-M-REMS-4-ENVRDR-V1.0",
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
-                "mars science laboratory",
-                "mars"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "Data taken by the sensors of the Rover Environmental Monitoring Station (REMS) aboard the  Mars Science Laboratory, in physical units.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.msl-m-rems-4-envrdr-v1.0_kmxa-xa59",
+            "issued": "2021-05-21",
+            "keyword": [
+                "mars science laboratory",
+                "mars"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MSL-M-REMS-4-ENVRDR-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.msl-m-rems-4-envrdr-v1.0_kmxa-xa59",
-            "description": "Data taken by the sensors of the Rover Environmental Monitoring Station (REMS) aboard the  Mars Science Laboratory, in physical units.",
-            "title": "MSL MARS ROVER ENV MONITORING STATION \n                                      4 ENVRDR V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "MSL MARS ROVER ENV MONITORING STATION \n                                      4 ENVRDR V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-2-ESC3-67PCHURYUMOV-M19-V1.0",
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
+            "description": "This data set contains raw EDR images acquired by the OSIRIS Wide Angle\nCamera during the escort phase of the Rosetta mission at the comet 67P,\ncovering the period from 2015-07-28 to 2015-08-25.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-2-esc3-67pchuryumov-m19-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-2-ESC3-67PCHURYUMOV-M19-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-2-esc3-67pchuryumov-m19-v1.0",
-            "description": "This data set contains raw EDR images acquired by the OSIRIS Wide Angle\nCamera during the escort phase of the Rosetta mission at the comet 67P,\ncovering the period from 2015-07-28 to 2015-08-25.",
-            "title": "ROSETTA-ORBITER COMET ESCORT OSIWAC 2 EDR MTP 019 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER COMET ESCORT OSIWAC 2 EDR MTP 019 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-PRL-0224-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the PRELANDING phase 2014-01-21 to 2014-11-18. It is a Global Gravity measurement at the comet 67P and covers the time 2014-08-20T10:00:35.000 to 2014-08-20T13:04:58.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-prl-0224-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-PRL-0224-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-prl-0224-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the PRELANDING phase 2014-01-21 to 2014-11-18. It is a Global Gravity measurement at the comet 67P and covers the time 2014-08-20T10:00:35.000 to 2014-08-20T13:04:58.000.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     PRELANDING 0224 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     PRELANDING 0224 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://c3.nasa.gov/dashlink/resources/756/",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2013-06-19",
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
-            "identifier": "DASHLINK_756",
             "description": "Requirements for system availability for ultra-high reliability electronic systems such as airborne and space electronic systems are driving the need for advanced heath monitoring techniques for early detection of the onset of damage. Aerospace-electronic systems usually face a very harsh environment, requiring them to survive the high strain rates, e.g. during launch and re-entry and thermal environments including extreme low and high temperatures. Traditional health monitoring methodologies have relied on reactive methods of failure detection often providing little or no insight into the remaining useful life of the system. In this paper, a mathematical approach for interrogation of system state under cyclic thermo- mechanical stresses has been developed for 6-different leadfree solder alloy systems. Data has been collected for leading indicators of failure for alloy systems including, Sn3Ag0.5Cu, Sn3Ag0.7Cu, Sn1Ag0.5Cu, Sn0.3Ag0.5Cu0.1Bi, Sn0.2Ag0.5Cu0.1Bi0.1Ni, 96.5Sn3.5Ag second-level interconnects under the application of cyclic thermo-mechanical loads. Methodology presented resides in the pre-failure space of the system in which no macro-indicators such as cracks or delamination exist. Systems subjected to thermo-mechanical damage have been interrogated for system state and the computed damage state correlated with known imposed damage. The approach involves the use of condition monitoring devices which can be interrogated for damage proxies at finite time- intervals. Interrogation techniques are based on derivation of damage proxies, and system prior damage based non-linear least- squares methods including the Levenberg-Marquardt Algorithm. The system\u2019s residual life is computed based on residual-life computation algorithms.",
-            "title": "Prognostication of Residual Life and Latent Damage Assessment in Lead-free Electronics Under Thermo-Mechanical Loads",
-            "programCode": [
-                "026:029"
-            ],
             "distribution": [
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/publication/2010_IEEE_TIE_ThermoMechanicalLoad.pdf",
-                    "description": "2010_IEEE_TIE_ThermoMechanicalLoad.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "2010_IEEE_TIE_ThermoMechanicalLoad.pdf",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/publication/2010_IEEE_TIE_ThermoMechanicalLoad.pdf",
+                    "mediaType": "application/pdf",
                     "title": "2010_IEEE_TIE_ThermoMechanicalLoad.pdf"
                 }
             ],
-            "accrualPeriodicity": "irregular"
+            "identifier": "DASHLINK_756",
+            "issued": "2013-06-19",
+            "keyword": [
+                "nasa",
+                "dashlink",
+                "ames"
+            ],
+            "landingPage": "https://c3.nasa.gov/dashlink/resources/756/",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:029"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Dashlink"
+            },
+            "title": "Prognostication of Residual Life and Latent Damage Assessment in Lead-free Electronics Under Thermo-Mechanical Loads"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=ODY-M-GRS-5-AND-V2.0",
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
+            "description": "Averaged neutron data from the Neutron Spectrometer in the Odyssey GRS Instrument suite.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ody-m-grs-5-and-v2.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "mars",
+                "2001 mars odyssey"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=ODY-M-GRS-5-AND-V2.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ody-m-grs-5-and-v2.0",
-            "description": "Averaged neutron data from the Neutron Spectrometer in the Odyssey GRS Instrument suite.",
-            "title": "ODY MARS GAMMA RAY\n                                   SPECTROMETER 5 AND V2.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ODY MARS GAMMA RAY\n                                   SPECTROMETER 5 AND V2.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/GPM/SAPHIR/MT1/PRPSCLIM/3A-MONTH/06",
             "citation": "Christopher Kidd. 2019-03-20. GPM_3PRPSMT1SAPHIR_CLIM. Version 06. GPM SAPHIR on MT1 (PRPS) Climate-based Radiometer Precipitation Profiling L3 1 month 0.25 x 0.25 degree V06. Greenbelt, MD. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/GPM/SAPHIR/MT1/PRPSCLIM/3A-MONTH/06. https://disc.gsfc.nasa.gov/datacollection/GPM_3PRPSMT1SAPHIR_CLIM_06.html. Digital Science Data.",
-            "issued": "2019-03-20",
-            "temporal": "2011-10-01T00:00:00Z/2021-12-31T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2019-03-20",
-            "keyword": [
-                "earth science",
-                "atmosphere",
-                "precipitation",
-                "atmospheric water vapor"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "CHRIS KIDD",
                 "hasEmail": "mailto:chris.kidd@nasa.gov"
             },
+            "creator": "Christopher Kidd",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C1596594717-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "The \"CLIM\"  products differ from their \"regular\" counterparts (without the \"CLIM\" in the name) by the ancillary data they use. They are Climate-Reference products, which requires homogeneous ancillary data over the climate time series.  Hence, the ECMWF-Interim (European Centre for Medium-Range Weather Forecasts, 2-3 months lag behind the regular production) reanalysis is used as ancillary data to derive surface and atmospheric conditions required by the GPROF algorithm for the \"CLIM\" output. \n\n\nThe Precipitation Retrieval and Profiling Scheme (PRPS)is designed to provide a best estimate of precipitation based upon matched SAPHIR-DPR observations. This fulfils in part the essence of GPM (and its predecessor, TRMM) in which the core observatory acts as a calibrator of precipitation retrievals for the international constellation of passive microwave instruments. In doing so the retrievals from the partner constellation sensors are able to provide greater temporal sampling and great spatial coverage than is possible from the DPR instrument alone. However, the limitations of the DPR instrument are transferred through the retrieval scheme to the resulting precipitation products.\n\nFundamental to the design of the PRPS is the independence from any dynamic ancillary data sets: the retrieval is based solely upon the satellite radiances, a static a priori radiance-rainrate database (and index), and (static) topographical data. Critically, the technique is independent of any model information, unlike the retrievals generated through the Goddard PROFiling (GPROF) scheme: this independence is advantageous when generating products across time scales from near real-time (inaccessibility to model\ndata) to climatological scales (circumventing trends in model data).\n\nThe algorithm is designed to generate instantaneous estimates of precipitation at a constant resolution (regardless of scan position), for all scan positions and scan lines. In addition to the actual precipitation estimate, an assessment of the error is made, and a measure of the \u2018fit\u2019 of the observations to the database provided. A quality flag is also provided, with any bad data generating a \u2018missing flag\u2019 in the retrieval.",
-            "release-place": "Greenbelt, MD",
-            "series-name": "GPM_3PRPSMT1SAPHIR_CLIM",
-            "creator": "Christopher Kidd",
-            "title": "GPM SAPHIR on MT1 (PRPS) Climate-based Radiometer Precipitation Profiling L3 1 month 0.25 x 0.25 degree V06 (GPM_3PRPSMT1SAPHIR_CLIM) at GES DISC",
-            "graphic-preview-description": "GPM SAPHIR on MT1 (PRPS) Radiometer Precipitation Profiling L3 1 month 0.25 x 0.25 degree (GPM_3PRPSMT1SAPHIR)",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/GPM/browse/GPM_3PRPSMT1SAPHIR.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGPM%2FSAPHIR%2FMT1%2FPRPSCLIM%2F3A-MONTH%2F06",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGPM%2FSAPHIR%2FMT1%2FPRPSCLIM%2F3A-MONTH%2F06",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/GPM/browse/GPM_3PRPSMT1SAPHIR.png",
-                    "description": "GPM SAPHIR on MT1 (PRPS) Radiometer Precipitation Profiling L3 1 month 0.25 x 0.25 degree (GPM_3PRPSMT1SAPHIR)",
                     "@type": "dcat:Distribution",
+                    "description": "GPM SAPHIR on MT1 (PRPS) Radiometer Precipitation Profiling L3 1 month 0.25 x 0.25 degree (GPM_3PRPSMT1SAPHIR)",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/GPM/browse/GPM_3PRPSMT1SAPHIR.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/GPM_3PRPSMT1SAPHIR_CLIM_06.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/GPM_3PRPSMT1SAPHIR_CLIM_06.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://gpm1.gesdisc.eosdis.nasa.gov/data/s4pa/GPM_L3/GPM_3PRPSMT1SAPHIR_CLIM.06/",
-                    "description": "Access the data via HTTPS",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS",
+                    "downloadURL": "https://gpm1.gesdisc.eosdis.nasa.gov/data/s4pa/GPM_L3/GPM_3PRPSMT1SAPHIR_CLIM.06/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://gpm1.gesdisc.eosdis.nasa.gov/opendap/GPM_L3/GPM_3PRPSMT1SAPHIR_CLIM.06/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://gpm1.gesdisc.eosdis.nasa.gov/opendap/GPM_L3/GPM_3PRPSMT1SAPHIR_CLIM.06/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=GPM_3PRPSMT1SAPHIR_CLIM_06",
-                    "description": "Use the Earthdata Search Client to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search Client to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=GPM_3PRPSMT1SAPHIR_CLIM_06",
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
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://pps.gsfc.nasa.gov/Documents/20180203_SAPHIR-ATBD.pdf",
-                    "description": "The PRPS Algorithm Theoretical Base Document",
                     "@type": "dcat:Distribution",
+                    "description": "The PRPS Algorithm Theoretical Base Document",
+                    "downloadURL": "https://pps.gsfc.nasa.gov/Documents/20180203_SAPHIR-ATBD.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's algorithm theoretical basis document"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://pps.gsfc.nasa.gov/atbd.html",
-                    "description": "All available GPM Algorithm Theoretical Base Documents",
                     "@type": "dcat:Distribution",
+                    "description": "All available GPM Algorithm Theoretical Base Documents",
+                    "downloadURL": "https://pps.gsfc.nasa.gov/atbd.html",
+                    "mediaType": "text/html",
                     "title": "View this dataset's algorithm theoretical basis document"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.star.nesdis.noaa.gov/mirs/saphir.php",
-                    "description": "Instrument Description",
                     "@type": "dcat:Distribution",
+                    "description": "Instrument Description",
+                    "downloadURL": "https://www.star.nesdis.noaa.gov/mirs/saphir.php",
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
+            "graphic-preview-description": "GPM SAPHIR on MT1 (PRPS) Radiometer Precipitation Profiling L3 1 month 0.25 x 0.25 degree (GPM_3PRPSMT1SAPHIR)",
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/GPM/browse/GPM_3PRPSMT1SAPHIR.png",
+            "identifier": "C1596594717-GES_DISC",
+            "issued": "2019-03-20",
+            "keyword": [
+                "earth science",
+                "atmosphere",
+                "precipitation",
+                "atmospheric water vapor"
+            ],
+            "landingPage": "https://doi.org/10.5067/GPM/SAPHIR/MT1/PRPSCLIM/3A-MONTH/06",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2019-03-20",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
+            },
+            "release-place": "Greenbelt, MD",
+            "series-name": "GPM_3PRPSMT1SAPHIR_CLIM",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2011-10-01T00:00:00Z/2021-12-31T23:59:59.999Z",
             "theme": [
                 "GPM",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "GPM SAPHIR on MT1 (PRPS) Climate-based Radiometer Precipitation Profiling L3 1 month 0.25 x 0.25 degree V06 (GPM_3PRPSMT1SAPHIR_CLIM) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/AQR50-3DQCS",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "NASA Aquarius project. 2017-12-07. Aquarius Official Release Level 3 Sea Surface Density Standard Mapped Image 7-Day Running Mean Data. Version 5.0. Aquarius Sea Surface Salinity Products. Goddard Space Flight Center, 8800 Greenbelt Rd.; Greeenbelt, MD., 20771, USA. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/GSFC OBPG. https://doi.org/10.5067/AQR50-3DQCS. http://podaac.jpl.nasa.gov/SeaSurfaceSalinity/Aquarius. NASA Aquarius project, NASA/GSFC OBPG, 2017-12-07, Aquarius Official Release Level 3 Sea Surface Density Standard Mapped Image 7-Day Running Mean Data V5.0, http://podaac.jpl.nasa.gov/SeaSurfaceSalinity/Aquarius.",
-            "issued": "2017-10-21",
-            "temporal": "2011-08-25T01:45:23Z/2015-06-07T12:45:21Z",
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
-            "identifier": "C2491755802-POCLOUD",
-            "description": "Aquarius Level 3 sea surface density standard mapped image data contains gridded 1 degree spatial resolution derived density averaged over daily, 7 day, monthly, and seasonal time scales. This particular data set is the 7-Day running mean, sea surface density\nproduct for version 5.0 of the Aquarius data set, which is the official end of mission public data release from the AQUARIUS/SAC-D mission.  Surface density estimates are based on TEOS-10 and derived using retrieved salinity from Aquarius and collocated ancillary SST (Reynolds OI 0.25 degree product). The Aquarius instrument is onboard the AQUARIUS/SAC-D satellite, a collaborative effort between NASA and the Argentinian Space Agency Comision Nacional de Actividades Espaciales (CONAE). The instrument consists of three radiometers in push broom alignment at incidence angles of 29, 38, and 46 degrees incidence angles relative to the shadow side of the orbit.  Footprints for the beams are: 76 km (along-track) x 94 km (cross-track), 84 km x 120 km and 96km x 156 km, yielding a total cross-track swath of 370 km. The radiometers measure brightness temperature at 1.413 GHz in their respective horizontal and vertical polarizations (TH and TV). A scatterometer operating at 1.26 GHz measures ocean backscatter in each footprint that is used for surface roughness corrections in the estimation of salinity. The scatterometer has an approximate 390km swath.",
-            "release-place": "Goddard Space Flight Center, 8800 Greenbelt Rd.; Greeenbelt, MD., 20771, USA",
-            "series-name": "Aquarius Official Release Level 3 Sea Surface Density Standard Mapped Image 7-Day Running Mean Data",
-            "graphic-preview-description": "Thumbnail",
             "creator": "NASA Aquarius project",
-            "title": "Aquarius Official Release Level 3 Sea Surface Density Standard Mapped Image 7-Day Running Mean Data V5.0",
-            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/AQUARIUS_L3_DENSITY_SMI_7DAY-RUNNINGMEAN_V5.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "Aquarius Level 3 sea surface density standard mapped image data contains gridded 1 degree spatial resolution derived density averaged over daily, 7 day, monthly, and seasonal time scales. This particular data set is the 7-Day running mean, sea surface density\nproduct for version 5.0 of the Aquarius data set, which is the official end of mission public data release from the AQUARIUS/SAC-D mission.  Surface density estimates are based on TEOS-10 and derived using retrieved salinity from Aquarius and collocated ancillary SST (Reynolds OI 0.25 degree product). The Aquarius instrument is onboard the AQUARIUS/SAC-D satellite, a collaborative effort between NASA and the Argentinian Space Agency Comision Nacional de Actividades Espaciales (CONAE). The instrument consists of three radiometers in push broom alignment at incidence angles of 29, 38, and 46 degrees incidence angles relative to the shadow side of the orbit.  Footprints for the beams are: 76 km (along-track) x 94 km (cross-track), 84 km x 120 km and 96km x 156 km, yielding a total cross-track swath of 370 km. The radiometers measure brightness temperature at 1.413 GHz in their respective horizontal and vertical polarizations (TH and TV). A scatterometer operating at 1.26 GHz measures ocean backscatter in each footprint that is used for surface roughness corrections in the estimation of salinity. The scatterometer has an approximate 390km swath.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAQR50-3DQCS",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAQR50-3DQCS",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
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
-                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/AQUARIUS_L3_DENSITY_SMI_7DAY-RUNNINGMEAN_V5.jpg",
-                    "description": "Thumbnail",
                     "@type": "dcat:Distribution",
+                    "description": "Thumbnail",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/AQUARIUS_L3_DENSITY_SMI_7DAY-RUNNINGMEAN_V5.jpg",
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
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2491755802-POCLOUD",
-                    "description": "HTTPS endpoint for data browse and download",
                     "@type": "dcat:Distribution",
+                    "description": "HTTPS endpoint for data browse and download",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2491755802-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2491755802-POCLOUD",
-                    "description": "Browse granule search results in Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse granule search results in Earthdata Search",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2491755802-POCLOUD",
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
-                {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/aquarius/open/docs/v5/AQ-014-PS-0017_Aquarius_ATBD-EndOfMission.pdf",
-                    "description": "ATBD, Validation Analysis, Product Specifications, etc",
+                {
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
+            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/AQUARIUS_L3_DENSITY_SMI_7DAY-RUNNINGMEAN_V5.jpg",
+            "identifier": "C2491755802-POCLOUD",
+            "issued": "2017-10-21",
+            "keyword": [
+                "oceans",
+                "salinity/density",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/AQR50-3DQCS",
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
+            "series-name": "Aquarius Official Release Level 3 Sea Surface Density Standard Mapped Image 7-Day Running Mean Data",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2011-08-25T01:45:23Z/2015-06-07T12:45:21Z",
             "theme": [
                 "AQUARIUS SAC-D",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Aquarius Official Release Level 3 Sea Surface Density Standard Mapped Image 7-Day Running Mean Data V5.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=GO-A-SSI-2-REDR-IDA%2FGASPRA-V1.0",
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
-                "asteroid"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "Galileo Magnetometer observations of the asteroid Gaspra, extracted from the Galileo archive",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.go-a-ssi-2-redr-ida-gaspra-v1.0_kncb-h6kw",
+            "issued": "2021-05-21",
+            "keyword": [
+                "galileo",
+                "asteroid"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=GO-A-SSI-2-REDR-IDA%2FGASPRA-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.go-a-ssi-2-redr-ida-gaspra-v1.0_kncb-h6kw",
-            "description": "Galileo Magnetometer observations of the asteroid Gaspra, extracted from the Galileo archive",
-            "title": "GALILEO SSI IDA/GASPRA IMAGES V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "GALILEO SSI IDA/GASPRA IMAGES V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/MEASURES/AER/DATA202",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Omar Torres et al.. 2018-10-01. TOMSEPAER. Version 2. TOMS/EP Near UV Aerosol Index and LER 1-Orbit L2 40x40km. Goddard Space Flight Center. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/MEASURES/AER/DATA202. https://disc.gsfc.nasa.gov/datacollection/TOMSEPAER_2.html. Digital Science Data.",
-            "issued": "2017-12-12",
-            "temporal": "1996-07-16T18:21:21Z/2002-01-01T00:20:26Z",
-            "@type": "dcat:Dataset",
-            "modified": "2018-09-06",
-            "keyword": [
-                "earth science",
-                "clouds",
-                "atmosphere",
-                "aerosols"
-            ],
-            "data-presentation-form": "Digital Science Data",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "OMAR TORRES, PH. D",
                 "hasEmail": "mailto:omar.o.torres@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
-            "identifier": "C1452994122-GES_DISC",
-            "description": "As part of the NASA's Making Earth System Data Records for Use in Research Environments (MEaSUREs) program, this projects describes a multi-decadal Fundamental Climate Data Record (FCDR) of calibrated radiances as well as an Earth System Data Record (ESDR) of aerosol properties over the continents derived from a 32-year record of satellite near-UV observations by three sensors.  \n\nThe TOMS Earth Probe version 2 Level-2 orbital data product consists of cloud fraction, cloud optical depth, normalized radiance, reflectivity, residue, and UV aerosol index at approximately 40x40 km resolution (at nadir). This product also contains ancillary variables for ocean corrected surface albedo and terrain pressure.\n\nTotal Ozone Mapping Spectrometer (TOMS) instruments have been successfully flown in orbit aboard the Nimbus-7(Nov. 1978 - May 1993), Meteor-3 (Aug. 1991 - Dec. 1994), Earth Probe (June 1996 - December 2005), and ADEOS (Sep. 1996 - June 1997) satellites.\n\nThese Level-2 data are stored in the Hierarchical Data Format 5 (HDF5) and are available from the Goddard Earth Sciences (GES) Data and Information Services Center (DISC).",
-            "release-place": "Goddard Space Flight Center",
-            "series-name": "TOMSEPAER",
             "creator": "Omar Torres et al.",
-            "title": "TOMS/EP Near UV Aerosol Index and LER 1-Orbit L2 40x40km at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/TOMSEPAER_002.png",
-            "programCode": [
-                "026:001"
-            ],
+            "data-presentation-form": "Digital Science Data",
+            "description": "As part of the NASA's Making Earth System Data Records for Use in Research Environments (MEaSUREs) program, this projects describes a multi-decadal Fundamental Climate Data Record (FCDR) of calibrated radiances as well as an Earth System Data Record (ESDR) of aerosol properties over the continents derived from a 32-year record of satellite near-UV observations by three sensors.  \n\nThe TOMS Earth Probe version 2 Level-2 orbital data product consists of cloud fraction, cloud optical depth, normalized radiance, reflectivity, residue, and UV aerosol index at approximately 40x40 km resolution (at nadir). This product also contains ancillary variables for ocean corrected surface albedo and terrain pressure.\n\nTotal Ozone Mapping Spectrometer (TOMS) instruments have been successfully flown in orbit aboard the Nimbus-7(Nov. 1978 - May 1993), Meteor-3 (Aug. 1991 - Dec. 1994), Earth Probe (June 1996 - December 2005), and ADEOS (Sep. 1996 - June 1997) satellites.\n\nThese Level-2 data are stored in the Hierarchical Data Format 5 (HDF5) and are available from the Goddard Earth Sciences (GES) Data and Information Services Center (DISC).",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMEASURES%2FAER%2FDATA202",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMEASURES%2FAER%2FDATA202",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
@@ -1040026,91 +1040003,92 @@
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/TOMSEPAER_2.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/TOMSEPAER_2.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://measures.gesdisc.eosdis.nasa.gov/data/AER/TOMSEPAER.2/",
-                    "description": "Access the data via HTTPS",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS",
+                    "downloadURL": "https://measures.gesdisc.eosdis.nasa.gov/data/AER/TOMSEPAER.2/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://measures.gesdisc.eosdis.nasa.gov/data/AER/TOMSEPAER.2/doc/README.MEaSUREs_Aerosols.pdf",
-                    "description": "README Document",
                     "@type": "dcat:Distribution",
+                    "description": "README Document",
+                    "downloadURL": "https://measures.gesdisc.eosdis.nasa.gov/data/AER/TOMSEPAER.2/doc/README.MEaSUREs_Aerosols.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's read me document"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://earthdata.nasa.gov/community/community-data-system-programs/measures-projects",
-                    "description": "MEaSUREs Project Homepage",
                     "@type": "dcat:Distribution",
+                    "description": "MEaSUREs Project Homepage",
+                    "downloadURL": "https://earthdata.nasa.gov/community/community-data-system-programs/measures-projects",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=TOMSEPAER_2",
-                    "description": "Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=TOMSEPAER_2",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://measures.gesdisc.eosdis.nasa.gov/opendap/AER/TOMSEPAER.2",
-                    "description": "OPeNDAP Service",
                     "@type": "dcat:Distribution",
+                    "description": "OPeNDAP Service",
+                    "downloadURL": "https://measures.gesdisc.eosdis.nasa.gov/opendap/AER/TOMSEPAER.2",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 }
             ],
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/TOMSEPAER_002.png",
+            "identifier": "C1452994122-GES_DISC",
+            "issued": "2017-12-12",
+            "keyword": [
+                "earth science",
+                "clouds",
+                "atmosphere",
+                "aerosols"
+            ],
+            "landingPage": "https://doi.org/10.5067/MEASURES/AER/DATA202",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2018-09-06",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
+            },
+            "release-place": "Goddard Space Flight Center",
+            "series-name": "TOMSEPAER",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "1996-07-16T18:21:21Z/2002-01-01T00:20:26Z",
             "theme": [
                 "MEaSUREs",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "TOMS/EP Near UV Aerosol Index and LER 1-Orbit L2 40x40km at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://nasa3d.arc.nasa.gov/detail/headquarters",
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
-                "headquarters",
-                "tools",
-                "building"
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
-            "identifier": "NASA-357",
             "description": "Headquarters building model.",
-            "title": "NASA 3D Models: Headquarters Building",
-            "programCode": [
-                "026:045",
-                "026:046"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -1040118,210 +1040096,210 @@
                     "mediaType": "application/octet-stream"
                 }
             ],
-            "accrualPeriodicity": "irregular",
+            "identifier": "NASA-357",
+            "issued": "2018-06-25",
+            "keyword": [
+                "3d model",
+                "headquarters",
+                "tools",
+                "building"
+            ],
+            "landingPage": "http://nasa3d.arc.nasa.gov/detail/headquarters",
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
+            "title": "NASA 3D Models: Headquarters Building"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=DAWN-A-FC2-5-MOSAIC-V1.0",
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
+            "description": "Abstract                                                                   ========                                                                   This data set includes various Vesta global mosaics derived from images  acquired by the Framing Camera 2 (FC2) on the NASA Dawn spacecraft at    the high and low altitude mapping orbits (HAMO and LAMO). Data are       provided in cylindrical and polar stereographic projections. In addition to the mosaics, the flatfield and stray light used during the processing of the raw images are provided.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.dawn-a-fc2-5-mosaic-v1.0_knfj-2c5v",
+            "issued": "2018-06-26",
+            "keyword": [
+                "4 vesta",
+                "dawn mission to vesta and ceres"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=DAWN-A-FC2-5-MOSAIC-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.dawn-a-fc2-5-mosaic-v1.0_knfj-2c5v",
-            "description": "Abstract                                                                   ========                                                                   This data set includes various Vesta global mosaics derived from images  acquired by the Framing Camera 2 (FC2) on the NASA Dawn spacecraft at    the high and low altitude mapping orbits (HAMO and LAMO). Data are       provided in cylindrical and polar stereographic projections. In addition to the mosaics, the flatfield and stray light used during the processing of the raw images are provided.",
-            "title": "DAWN FC2 DERIVED VESTA GLOBAL MOSAICS V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "DAWN FC2 DERIVED VESTA GLOBAL MOSAICS V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://techport.nasa.gov/view/13680",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2012-10-01",
-            "temporal": "2012-10-01T00:00:00Z/2014-09-01T00:00:00Z",
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
-                "element",
-                "johnson space center",
-                "active"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Stephen Gaddis",
                 "hasEmail": "mailto:stephen.w.gaddis@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Space Technology Mission Directorate"
-            },
-            "identifier": "TECHPORT_13680",
             "description": "&lt;p&gt;During 2014, the &lt;em&gt;Robotic ISRU Resource Acquisition &lt;/em&gt;project element will develop two technologies:&lt;/p&gt;&lt;ul&gt;&lt;li&gt;Exploration Ground Data Systems (xGDS)&lt;/li&gt;&lt;li&gt;Sample Acquisition on Asteroids, Mars, Moons of Mars, and Lunar Cold Traps&lt;/li&gt;&lt;/ul&gt;&lt;p&gt;A primary technology of this element is development of HRS&amp;rsquo;s Exploration Ground Data Systems (xGDS) software, a set of planning, monitoring, archiving, and search tools for dealing with data sent to or received from robotic spacecraft or crew systems.&amp;nbsp; xGDS is being matured through technology development under HRS (with STMD funds) and field-tested with funds from the Human Exploration and Operations Mission Directorate (HEOMD) and Science Mission Directorate (SMD).&amp;nbsp; The outcome of this development will be that the desired parts of the xGDS system (likely the traverse planner, real time plotting, and raster mapping tools) will be ready to be infused into the lunar Resource Prospector Mission (RPM).&amp;nbsp; The scope of FY14 xGDS work includes maturing time delayed image and video processing and archiving tools and adding support for mobile devices.&amp;nbsp; During 2014, xGDS will support the AES-funded Regolith and Environment Science and Oxygen and Lunar Volatile Extraction (RESOLVE) payload thermal vacuum chamber testing the SMD-funded Mojave Volatiles Prospector (MVP) project.&amp;nbsp;&lt;/p&gt;&lt;p&gt;Another technology under this element will develop regolith sampling and excavation for reduced and low gravity environments.&amp;nbsp; The objective for this work in FY14 is to acquire representative samples of target bodies in order to characterize the regolith for ISRU prospecting purposes which would also benefit science objectives and other relevant Strategic Knowledge Gaps (SKG&amp;rsquo;s). The requirements of the Advanced Exploration Systems (AES) lunar Resource Prospector (RP) are focused on a lunar South pole mission near the impact site of the recent Lunar CRater Observation and Sensing Satellite (LCROSS) mission in order to obtain ground truth on the lunar surface.&amp;nbsp; Orbital data from neutron spectrometers shows that most of the detected hydrogen on the moon is in these crater floor cold traps. The goal is to confirm the existence of volatiles such as water, hydrogen and helium in the regolith at the lunar poles.&amp;nbsp; Other target bodies such as asteroids and Mars&amp;rsquo; moons will also need prospecting and characterization. One of the primary potential uses of the returned asteroid in the Asteroid Initiative is for ISRU demonstrations in lunar orbit.&amp;nbsp; Sampling devices will be needed to prospect the asteroid for useful resources, such as water on a carbonaceous condrite. The Mars&amp;rsquo; moons and Mars itself are also of interest for ISRU purposes and can be sampled with robotic devices or by human crews to determine the ISRU value of their regolith.&lt;/p&gt;&lt;p&gt;Regolith excavation and sample acquisition in low gravity environments ( micro-G, 1/3 G, 1/6th G) is difficult due to the lack of reaction force from the weight of the excavation robot.&amp;nbsp; On Earth, excavators are typically large and heavy to take advantage of this large reaction force to counter-act the digging forces. In space, new methods of digging and sampling must be found, due to their light weight in low gravity environments.&amp;nbsp; Percussive excavation is one method for reducing digging forces, and in FY14, the HRS project will test interfaces for a large percussive excavation end effector: the Vibratory Implement for Percussive Excavation of Regolith (VIPER) which is designed to be mounted on the All-Terrain Hex-Limbed Extra-Terrestrial Explorer (ATHLETE) robot from JPL. The VIPER was designed and fabricated by HRS. A smaller percussive excavation implement called Badger, will be operated on the Centaur 2 mobility robot with a positioning mechanism. Firs",
-            "title": "Human Robotic Systems (HRS): Robotic ISRU Acquisition Element",
-            "programCode": [
-                "026:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "http://techport.nasa.gov/xml-api/13680",
                     "mediaType": "application/xml"
                 }
-            ]
+            ],
+            "identifier": "TECHPORT_13680",
+            "issued": "2012-10-01",
+            "keyword": [
+                "element",
+                "johnson space center",
+                "active"
+            ],
+            "landingPage": "http://techport.nasa.gov/view/13680",
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
+            "temporal": "2012-10-01T00:00:00Z/2014-09-01T00:00:00Z",
+            "title": "Human Robotic Systems (HRS): Robotic ISRU Acquisition Element"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=CO-SSA-RSS-1-ENGR2-V1.0",
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
-                "enceladus",
-                "cassini-huygens"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "The Cassini Radio Science Enceladus Gravity Science Experiment (ENGR2) Raw Data Archive is a time-ordered collection of radio science raw data acquired on March 11 and March 13, 2008, during the Tour subphase of the Cassini mission.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.co-ssa-rss-1-engr2-v1.0_kniu-cjfg",
+            "issued": "2018-06-26",
+            "keyword": [
+                "enceladus",
+                "cassini-huygens"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=CO-SSA-RSS-1-ENGR2-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.co-ssa-rss-1-engr2-v1.0_kniu-cjfg",
-            "description": "The Cassini Radio Science Enceladus Gravity Science Experiment (ENGR2) Raw Data Archive is a time-ordered collection of radio science raw data acquired on March 11 and March 13, 2008, during the Tour subphase of the Cassini mission.",
-            "title": "CASSINI RSS RAW DATA SET - ENGR2 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "CASSINI RSS RAW DATA SET - ENGR2 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC3-1081-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 3 phase 2015-07-01 to 2015-10-21. It is a Global Gravity measurement at the comet 67P and covers the time 2015-10-05T21:05:30.000 to 2015-10-06T05:22:04.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc3-1081-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC3-1081-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc3-1081-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 3 phase 2015-07-01 to 2015-10-21. It is a Global Gravity measurement at the comet 67P and covers the time 2015-10-05T21:05:30.000 to 2015-10-06T05:22:04.000.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 3 1081 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 3 1081 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/Aura/MLS/DATA/3547",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Wang, S., Livesey, N., Read, W., and Fuller, R.. 2021-04-29. ML3MBOH. Version 005. MLS/Aura Level 3 Monthly Binned Hydroxyl (OH) Mixing Ratio on Assorted Grids V005. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/Aura/MLS/DATA/3547. https://disc.gsfc.nasa.gov/datacollection/ML3MBOH_005.html. Digital Science Data.",
-            "issued": "2021-04-29",
-            "temporal": "2004-08-02T00:00:00Z/2014-10-01T23:59:59.999Z",
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
-            "identifier": "C2042568937-GES_DISC",
-            "description": "ML3MBOH is the EOS Aura Microwave Limb Sounder (MLS) monthly binned on various vertical grids product for hydroxyl (OH) derived from radiances measured by the THz radiometer. The data version is 5.1. Data coverage is continuous from August 2005 to December 12, 2009 when the THz radiometer was placed in standby mode. After this date OH data were collected for about 30 days in August/September of 2011, 2012, 2013 and 2014. Spatial coverage is near-global (-82 to +82 degrees latitude), with a spatial resolution of 4 degrees latitude by 5 degrees longitude. The recommended useful vertical range is from 31.6 to 0.00316 hPa, and the vertical resolution is about 3. Users of the ML3MBOH data product should read chapter 4 and section 3.19 of the EOS MLS Level 2 Version 5 Quality Document for more information.\n\nThe data files are archived in the netCDF4 format, which is also compatible with HDF5 readers and tools. Each file contains two grid objects (profile and column data), each with a set of data and geolocation fields, grid attributes, and metadata.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "ML3MBOH",
             "creator": "Wang, S., Livesey, N., Read, W., and Fuller, R.",
-            "title": "MLS/Aura Level 3 Monthly Binned Hydroxyl (OH) Mixing Ratio on Assorted Grids V005 (ML3MBOH) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/ML3MBOH_005.png",
-            "programCode": [
-                "026:001"
-            ],
+            "data-presentation-form": "Digital Science Data",
+            "description": "ML3MBOH is the EOS Aura Microwave Limb Sounder (MLS) monthly binned on various vertical grids product for hydroxyl (OH) derived from radiances measured by the THz radiometer. The data version is 5.1. Data coverage is continuous from August 2005 to December 12, 2009 when the THz radiometer was placed in standby mode. After this date OH data were collected for about 30 days in August/September of 2011, 2012, 2013 and 2014. Spatial coverage is near-global (-82 to +82 degrees latitude), with a spatial resolution of 4 degrees latitude by 5 degrees longitude. The recommended useful vertical range is from 31.6 to 0.00316 hPa, and the vertical resolution is about 3. Users of the ML3MBOH data product should read chapter 4 and section 3.19 of the EOS MLS Level 2 Version 5 Quality Document for more information.\n\nThe data files are archived in the netCDF4 format, which is also compatible with HDF5 readers and tools. Each file contains two grid objects (profile and column data), each with a set of data and geolocation fields, grid attributes, and metadata.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAura%2FMLS%2FDATA%2F3547",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAura%2FMLS%2FDATA%2F3547",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
@@ -1040331,312 +1040309,306 @@
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/ML3MBOH_005.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/ML3MBOH_005.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/Aura_MLS_Level3/ML3MBOH.005/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/Aura_MLS_Level3/ML3MBOH.005/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/opendap/HDF-EOS5/Aura_MLS_Level3/ML3MBOH.005/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/opendap/HDF-EOS5/Aura_MLS_Level3/ML3MBOH.005/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=ML3MBOH_005",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=ML3MBOH_005",
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
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/ML3MBOH_005.png",
+            "identifier": "C2042568937-GES_DISC",
+            "issued": "2021-04-29",
+            "keyword": [
+                "earth science",
+                "atmosphere",
+                "atmospheric chemistry"
+            ],
+            "landingPage": "https://doi.org/10.5067/Aura/MLS/DATA/3547",
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
+            "series-name": "ML3MBOH",
             "spatial": "-180.0 -82.0 180.0 82.0",
+            "temporal": "2004-08-02T00:00:00Z/2014-10-01T23:59:59.999Z",
             "theme": [
                 "Aura",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "MLS/Aura Level 3 Monthly Binned Hydroxyl (OH) Mixing Ratio on Assorted Grids V005 (ML3MBOH) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C2801713712-LAADS.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "National Aeronautics and Space Administration (NASA),. 2023-11-01.  MODIS Airborne Simulator (MAS) L2 Cloud Data Products. Version 1. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Level 1 and Atmosphere Archive and Distribution System (LAADS).",
-            "issued": "2007-07-06",
-            "temporal": "2007-07-07T00:00:00Z/2007-08-10T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2007-08-09",
-            "keyword": [
-                "earth science",
-                "infrared wavelengths",
-                "clouds",
-                "atmosphere",
-                "visible wavelengths",
-                "spectral/engineering"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "LAADS USER SUPPORT TEAM",
                 "hasEmail": "mailto:MODAPSUSO@lists.nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/HBSL/BISB/LAADS"
-            },
-            "identifier": "C2801713712-LAADS",
-            "description": "The MODIS Airborne Simulator (MAS) Level-2 Cloud Data product (MASL2CLD) consists of cloud optical and physical parameters. These parameters are derived using remotely sensed infrared and near infrared solar reflected radiances. Multispectral images of the reflectance and brightness temperature at 10 wavelengths between 0.66 and 13.98nm were used to derive the probability of clear sky (or cloud), cloud thermodynamic phase, and the optical thickness and effective radius of liquid water and ice clouds.\r\n\r\nMASL2CLD product files are stored in Hierarchical Data Format (HDF-EOS). All gridded cloud parameters are stored as Scientific Data Sets (SDS) within the file.\r\n\r\nFor more information and for a list of MAS campaign flights  visit ladsweb at:\r\n\r\nhttps://ladsweb.modaps.eosdis.nasa.gov/missions-and-measurements/mas/",
-            "release-place": "Greenbelt, MD, USA",
             "creator": "National Aeronautics and Space Administration (NASA),",
-            "title": "MODIS Airborne Simulator (MAS) L2 Cloud Data",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The MODIS Airborne Simulator (MAS) Level-2 Cloud Data product (MASL2CLD) consists of cloud optical and physical parameters. These parameters are derived using remotely sensed infrared and near infrared solar reflected radiances. Multispectral images of the reflectance and brightness temperature at 10 wavelengths between 0.66 and 13.98nm were used to derive the probability of clear sky (or cloud), cloud thermodynamic phase, and the optical thickness and effective radius of liquid water and ice clouds.\r\n\r\nMASL2CLD product files are stored in Hierarchical Data Format (HDF-EOS). All gridded cloud parameters are stored as Scientific Data Sets (SDS) within the file.\r\n\r\nFor more information and for a list of MAS campaign flights  visit ladsweb at:\r\n\r\nhttps://ladsweb.modaps.eosdis.nasa.gov/missions-and-measurements/mas/",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/archive/allData/440/MASL2CLD/",
-                    "description": "Direct access to MAS data from LAADS.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct access to MAS data from LAADS.",
+                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/archive/allData/440/MASL2CLD/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through LAADS"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asapdata.arc.nasa.gov/",
-                    "description": "The Airborne Sensor Facility (ASF) at NASA Ames Research Center.",
                     "@type": "dcat:Distribution",
+                    "description": "The Airborne Sensor Facility (ASF) at NASA Ames Research Center.",
+                    "downloadURL": "https://asapdata.arc.nasa.gov/",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 }
             ],
+            "identifier": "C2801713712-LAADS",
+            "issued": "2007-07-06",
+            "keyword": [
+                "earth science",
+                "infrared wavelengths",
+                "clouds",
+                "atmosphere",
+                "visible wavelengths",
+                "spectral/engineering"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C2801713712-LAADS.html",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2007-08-09",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/HBSL/BISB/LAADS"
+            },
+            "release-place": "Greenbelt, MD, USA",
             "spatial": "-180.0 -35.0 180.0 80.0",
+            "temporal": "2007-07-07T00:00:00Z/2007-08-10T00:00:00Z",
             "theme": [
                 "MAS_eMAS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "MODIS Airborne Simulator (MAS) L2 Cloud Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/NOAA-20/VIIRS/L3B/PIC/2022",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/GSFC/SED/ESD/GCDC/OB.DAAC. https://doi.org/10.5067/NOAA-20/VIIRS/L3B/PIC/2022.",
-            "issued": "2022-09-14",
-            "temporal": "2017-11-29T00:00:00Z/2023-02-28T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-09-14",
-            "keyword": [
-                "oceans",
-                "ocean chemistry",
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
-            "identifier": "C2340494513-OB_DAAC",
             "description": "The Visible and Infrared Imager/Radiometer Suite (VIIRS) is a multi-disciplinary instrument that is being flown on the Joint Polar Satellite System (JPSS) series of spacecraft, including the Suomi National Polar-orbiting Partnership (S-NPP) that launched in October 2011.  JPSS is a multi-platform, multi-agency program that consolidates the polar orbiting spacecraft of NASA and the National Oceanic and Atmospheric Administration (NOAA).  S-NPP is the initial spacecraft in this series, and VIIRS is the successor to MODIS for Earth science data product generation.  VIIRS has 22 spectral bands ranging from 412 nm to 12 nm.  There are 16 moderate-resolution bands (750m at nadir), 5 image-resolution bands (375m), and one day-night band (DNB).",
-            "title": "NOAA-20 VIIRS Global Binned Particulate Inorganic Carbon (PIC) Data, version R2022.0",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FNOAA-20%2FVIIRS%2FL3B%2FPIC%2F2022",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FNOAA-20%2FVIIRS%2FL3B%2FPIC%2F2022",
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
-                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/data/10.5067/NOAA-20/VIIRS/L3B/PIC/2022",
-                    "description": "VIIRS-NOAA-20 L3B Particulate Inorganic Carbon (PIC) Dataset Landing Page",
                     "@type": "dcat:Distribution",
+                    "description": "VIIRS-NOAA-20 L3B Particulate Inorganic Carbon (PIC) Dataset Landing Page",
+                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/data/10.5067/NOAA-20/VIIRS/L3B/PIC/2022",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 }
             ],
+            "identifier": "C2340494513-OB_DAAC",
+            "issued": "2022-09-14",
+            "keyword": [
+                "oceans",
+                "ocean chemistry",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/NOAA-20/VIIRS/L3B/PIC/2022",
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
+            "title": "NOAA-20 VIIRS Global Binned Particulate Inorganic Carbon (PIC) Data, version R2022.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/GPM/ATMS/NPP/1C/07",
             "citation": "Wesley Berg. 2022-05-09. GPM_1CNPPATMS. GPM ATMS on SUOMI-NPP Common Calibrated Brightness Temperature L1C 1.5 hours 16 km V07. Greenbelt, MD. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/GPM/ATMS/NPP/1C/07. https://disc.gsfc.nasa.gov/datacollection/GPM_1CNPPATMS_07.html. Digital Science Data.",
-            "issued": "2022-05-01",
-            "temporal": "2011-11-08T00:00:00Z/2023-02-28T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-05-01",
-            "references": [
-                "https://doi.org/10.1175/JTECH-D-16-0100.1",
-                "https://doi.org/10.3390/rs10081306"
-            ],
-            "keyword": [
-                "atmospheric water vapor",
-                "precipitation",
-                "atmosphere",
-                "earth science"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "WESLEY BERG",
                 "hasEmail": "mailto:berg@atmos.colostate.edu"
             },
+            "creator": "Wesley Berg",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C2264133568-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "Version 07 is the current version of the data set. Older versions will no longer be available and have been superseded by Version 07. All 1C products have a common L1C data structure, simple and generic. Each L1C swath includes scan time, latitude and longitude, scan status, quality, incidence angle, Sun glint angle, and the intercalibrated brightness temperature (Tc). One or more swaths are included in a product. The radiometer data are recalibrated to a common basis so that precipitation products derived from them are consistent. 1CATMS contains common calibrated brightness temperature from the ATMS passive microwave instrument flown on the Suomi NPP satellite and JPSS satellites. ATMS is approximately a combination of the AMSU-A channels and the MHS channels. ATMS rotates 3 scans per 8 seconds. ATMS has the following 22 channels: Ch GHz Pol 1 23.8 QV 2 31.4 QV 3 50.3 QH 4 51.76 QH 5 52.8 QH 6 53.596+-0.115 QH 7 54.4 QH 8 54.94 QH 9 55.5 QH 10 fo = 57.29 QH 11 fo+-0.3222+-0.217 QH 12 fo+-0.3222+-0.048 QH 13 fo+-0.3222+-0.022 QH 14 fo+-0.3222+-0.010 QH 15 fo+-0.3222+-0.0045 QH 16 88.2 QV 17 165.5 QH 18 183.31+-7 QH 19 183.31+-4.5 QH 20 183.31+-3 QH 21 183.31+-1.8 QH 22 183.31+-1 QH\n\nQV means quasi-vertical; the polarization vector is parallel to the scan plane at nadir. QH meansquasi-horizontal polarization. Note on geolocation and 1C swaths: The BeamLatitude and BeamLongitude in ATMSBASE have a band dimension of 5. Lat and lon is for channels 1,2,3,16,17. Each 1C swath will contain one band: 1C swath Band IEEE GHz Ch geo Chs in band 1 K 18-26.5 1 1 2 A(Ka) 26.5-40 2 2 3 W 75-110 16 16 4 G 110-300 17 17-22 Note that channels 3-15 are NOT included in the 1C product. 1C ATMS contains 4 swaths, one for each band K, A(Ka), W, and G.",
-            "release-place": "Greenbelt, MD",
-            "series-name": "GPM_1CNPPATMS",
-            "creator": "Wesley Berg",
-            "graphic-preview-description": "Common Calibrated Brightness Temperature from GPM ATMS on SUOMI-NPP (GPM_1CNPPATMS)",
-            "title": "GPM ATMS on SUOMI-NPP Common Calibrated Brightness Temperature L1C 1.5 hours 16 km V07 (GPM_1CNPPATMS) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/GPM/browse/GPM_1CNPPATMS.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGPM%2FATMS%2FNPP%2F1C%2F07",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGPM%2FATMS%2FNPP%2F1C%2F07",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/GPM/browse/GPM_1CNPPATMS.png",
-                    "description": "Common Calibrated Brightness Temperature from GPM ATMS on SUOMI-NPP (GPM_1CNPPATMS)",
                     "@type": "dcat:Distribution",
+                    "description": "Common Calibrated Brightness Temperature from GPM ATMS on SUOMI-NPP (GPM_1CNPPATMS)",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/GPM/browse/GPM_1CNPPATMS.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/GPM_1CNPPATMS_07.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/GPM_1CNPPATMS_07.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://gpm1.gesdisc.eosdis.nasa.gov/data/GPM_L1C/GPM_1CNPPATMS.07/",
-                    "description": "Access the data via HTTPS",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS",
+                    "downloadURL": "https://gpm1.gesdisc.eosdis.nasa.gov/data/GPM_L1C/GPM_1CNPPATMS.07/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://gpm1.gesdisc.eosdis.nasa.gov/opendap/GPM_L1C/GPM_1CNPPATMS.07/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://gpm1.gesdisc.eosdis.nasa.gov/opendap/GPM_L1C/GPM_1CNPPATMS.07/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=GPM_1CNPPATMS_07",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=GPM_1CNPPATMS_07",
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
@@ -1040646,615 +1040618,645 @@
                     "title": "View this dataset's algorithm theoretical basis document"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://arthurhou.pps.eosdis.nasa.gov/Documents/V07_L1C_Release_Notes.pdf",
-                    "description": "Release Notes",
                     "@type": "dcat:Distribution",
+                    "description": "Release Notes",
+                    "downloadURL": "https://arthurhou.pps.eosdis.nasa.gov/Documents/V07_L1C_Release_Notes.pdf",
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
-                    "downloadURL": "https://www.star.nesdis.noaa.gov/mirs/snppatms.php",
-                    "description": "Instrument Description",
                     "@type": "dcat:Distribution",
+                    "description": "Instrument Description",
+                    "downloadURL": "https://www.star.nesdis.noaa.gov/mirs/snppatms.php",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "graphic-preview-description": "Common Calibrated Brightness Temperature from GPM ATMS on SUOMI-NPP (GPM_1CNPPATMS)",
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/GPM/browse/GPM_1CNPPATMS.png",
+            "identifier": "C2264133568-GES_DISC",
+            "issued": "2022-05-01",
+            "keyword": [
+                "atmospheric water vapor",
+                "precipitation",
+                "atmosphere",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/GPM/ATMS/NPP/1C/07",
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
+                "https://doi.org/10.1175/JTECH-D-16-0100.1",
+                "https://doi.org/10.3390/rs10081306"
+            ],
+            "release-place": "Greenbelt, MD",
+            "series-name": "GPM_1CNPPATMS",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2011-11-08T00:00:00Z/2023-02-28T00:00:00Z",
             "theme": [
                 "GPM",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "GPM ATMS on SUOMI-NPP Common Calibrated Brightness Temperature L1C 1.5 hours 16 km V07 (GPM_1CNPPATMS) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MER2-M-PANCAM-5-WEDGE-OPS-V1.0",
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
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mer2-m-pancam-5-wedge-ops-v1.0_knq3-di4g",
+            "issued": "2021-05-21",
+            "keyword": [
+                "mars",
+                "mars exploration rover"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MER2-M-PANCAM-5-WEDGE-OPS-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mer2-m-pancam-5-wedge-ops-v1.0_knq3-di4g",
-            "description": "NULL",
-            "title": "MER 2 MARS PANORAMIC CAMERA TERRAIN\n                                      WEDGE RDR OPS V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "MER 2 MARS PANORAMIC CAMERA TERRAIN\n                                      WEDGE RDR OPS V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=A12A-L-SWS-3-SOLAR-WIND-28S-RES-V1.0",
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
-                "apollo 12",
-                "moon"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This data set contains daily tables of time ordered, 28-second-resolution plasma parameters, mainly of the solar wind, as observed on the Moon at the Apollo 12 ALSEP site by the Apollo 12 Solar Wind Spectrometer from 19 November 1969 through 25 March 1976.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.a12a-l-sws-3-solar-wind-28s-res-v1.0_knt4-q4jh",
+            "issued": "2018-06-26",
+            "keyword": [
+                "apollo 12",
+                "moon"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=A12A-L-SWS-3-SOLAR-WIND-28S-RES-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.a12a-l-sws-3-solar-wind-28s-res-v1.0_knt4-q4jh",
-            "description": "This data set contains daily tables of time ordered, 28-second-resolution plasma parameters, mainly of the solar wind, as observed on the Moon at the Apollo 12 ALSEP site by the Apollo 12 Solar Wind Spectrometer from 19 November 1969 through 25 March 1976.",
-            "title": "APOLLO 12 ALSEP/SWS SOLAR WIND 28-SEC RESOLUTION TABLES V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "APOLLO 12 ALSEP/SWS SOLAR WIND 28-SEC RESOLUTION TABLES V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/2321",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Armston, J., R.O. Dubayah, S.P. Healey, Z. Yang, P.L. Patterson, S. Saarela, G. Stahl, L. Duncanson, J.R. Kellner, A. Pascual, and J. Bruening. 2023. GEDI L4B Country-level Summaries of Aboveground Biomass. ORNL DAAC, Oak Ridge, Tennessee, USA. https://doi.org/10.3334/ORNLDAAC/2321",
-            "issued": "2023-12-06",
-            "temporal": "2019-04-18T00:00:00Z/2023-03-16T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-12-07",
-            "keyword": [
-                "biosphere",
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
-            "identifier": "C2813390180-ORNL_CLOUD",
             "description": "This dataset provides country-level estimates of land surface mean aboveground biomass density (AGBD), total aboveground biomass (AGB) stocks, and the associated standard errors of the mean calculated using different versions of the Global Ecosystem Dynamics Investigation (GEDI) Level-4B (L4B) product. The GEDI L4B product provides gridded (1 km x 1 km) estimates of AGBD within the GEDI orbital extent (between 51.6 degrees N and 51.6 degrees S). For comparison purposes, this dataset also includes national-scale National Forest Inventory (NFI) estimates of AGBD from the 2020 Global Forest Resources Assessment (FRA) published by the Food and Agriculture Organization (FAO, 2020) of the United Nations.The GEDI instrument produces high-resolution laser ranging observations of the 3-dimensional structure of the Earth's surface. GEDI was launched on December 5, 2018, and is attached to the International Space Station (ISS). The GEDI instrument consists of three lasers producing a total of eight beam ground transects, which consist of ~25 m footprint samples spaced approximately every 60 m along-track. The GEDI beam transects are spaced approximately 600 m apart on the Earth's surface in the cross-track direction, for an across-track width of ~4.2 km. The data are provided in comma-separated value (CSV) format.",
-            "graphic-preview-description": "Country-wide estimates of total aboveground biomass (GEDI_L4B_AGB) in peta grams (Pg) using GEDI L4B Version 2.1 dataset.",
-            "title": "GEDI L4B Country-level Summaries of Aboveground Biomass",
-            "graphic-preview-file": "https://daac.ornl.gov/GEDI/guides/GEDI_L4B_Country_Biomass_Fig1.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F2321",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F2321",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/gedi/GEDI_L4B_Country_Biomass/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/gedi/GEDI_L4B_Country_Biomass/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/GEDI/guides/GEDI_L4B_Country_Biomass.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/GEDI/guides/GEDI_L4B_Country_Biomass.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/2321",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/2321",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/gedi/GEDI_L4B_Country_Biomass/comp/GEDI_L4B_Country_Biomass.pdf",
-                    "description": "GEDI L4B Country-level Summaries of Aboveground Biomass: GEDI_L4B_Country_Biomass.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "GEDI L4B Country-level Summaries of Aboveground Biomass: GEDI_L4B_Country_Biomass.pdf",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/gedi/GEDI_L4B_Country_Biomass/comp/GEDI_L4B_Country_Biomass.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/gedi/GEDI_L4B_Country_Biomass/comp/summary_country_estimates_agbd.pdf",
-                    "description": "GEDI L4B Country-level Summaries of Aboveground Biomass: summary_country_estimates_agbd.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "GEDI L4B Country-level Summaries of Aboveground Biomass: summary_country_estimates_agbd.pdf",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/gedi/GEDI_L4B_Country_Biomass/comp/summary_country_estimates_agbd.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://daac.ornl.gov/GEDI/guides/GEDI_L4B_Country_Biomass_Fig1.png",
-                    "description": "Country-wide estimates of total aboveground biomass (GEDI_L4B_AGB) in peta grams (Pg) using GEDI L4B Version 2.1 dataset.",
                     "@type": "dcat:Distribution",
+                    "description": "Country-wide estimates of total aboveground biomass (GEDI_L4B_AGB) in peta grams (Pg) using GEDI L4B Version 2.1 dataset.",
+                    "downloadURL": "https://daac.ornl.gov/GEDI/guides/GEDI_L4B_Country_Biomass_Fig1.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://gedi.umd.edu",
-                    "description": "GEDI Project Site",
                     "@type": "dcat:Distribution",
+                    "description": "GEDI Project Site",
+                    "downloadURL": "https://gedi.umd.edu",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 }
             ],
+            "graphic-preview-description": "Country-wide estimates of total aboveground biomass (GEDI_L4B_AGB) in peta grams (Pg) using GEDI L4B Version 2.1 dataset.",
+            "graphic-preview-file": "https://daac.ornl.gov/GEDI/guides/GEDI_L4B_Country_Biomass_Fig1.png",
+            "identifier": "C2813390180-ORNL_CLOUD",
+            "issued": "2023-12-06",
+            "keyword": [
+                "biosphere",
+                "vegetation",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/2321",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2023-12-07",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "ORNL_DAAC"
+            },
             "spatial": "-180.0 -52.0 180.0 52.0",
+            "temporal": "2019-04-18T00:00:00Z/2023-03-16T23:59:59Z",
             "theme": [
                 "GEDI",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "GEDI L4B Country-level Summaries of Aboveground Biomass"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1301",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "dos-Santos, M.N., and M.M. Keller. 2016. CMS: Forest Inventory and Biophysical Measurements, Para, Brazil, 2012-2014. ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/1301",
-            "issued": "2016-01-06",
-            "temporal": "2012-01-27T00:00:00Z/2014-04-25T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-06-12",
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
-            "identifier": "C2343139758-ORNL_CLOUD",
             "description": "This data set provides measurements for diameter at breast height (DBH), commercial tree height, and total tree height for forest inventories taken at the Fazenda Cauaxi and the Fazenda Nova Neonita, Paragominas municipality, Para, Brazil. Also included for each tree are the common, family, and scientific name, coordinates, canopy position, crown radius, and for dead trees the decomposition status. These biophysical measurements were made at Fazenda Cauaxi during 2012 and 2014 and at the Fazenda Nova Neonita during 2013.",
-            "graphic-preview-description": "Browse Image",
-            "title": "CMS: Forest Inventory and Biophysical Measurements, Para, Brazil, 2012-2014",
-            "graphic-preview-file": "https://daac.ornl.gov/CMS/guides/CMS_Para_Brazil_Inventory_Map_BROWSE_Image.jpg",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1301",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1301",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/cms/CMS_Landscapes_Brazil_Forests/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/cms/CMS_Landscapes_Brazil_Forests/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/CMS/guides/CMS_Landscapes_Brazil_Forests.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/CMS/guides/CMS_Landscapes_Brazil_Forests.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1301",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1301",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/cms/CMS_Landscapes_Brazil_Forests/comp/CMS_Landscapes_Brazil_Forests.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/cms/CMS_Landscapes_Brazil_Forests/comp/CMS_Landscapes_Brazil_Forests.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://daac.ornl.gov/CMS/guides/CMS_Para_Brazil_Inventory_Map_BROWSE_Image.jpg",
-                    "description": "Browse Image",
                     "@type": "dcat:Distribution",
+                    "description": "Browse Image",
+                    "downloadURL": "https://daac.ornl.gov/CMS/guides/CMS_Para_Brazil_Inventory_Map_BROWSE_Image.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 }
             ],
+            "graphic-preview-description": "Browse Image",
+            "graphic-preview-file": "https://daac.ornl.gov/CMS/guides/CMS_Para_Brazil_Inventory_Map_BROWSE_Image.jpg",
+            "identifier": "C2343139758-ORNL_CLOUD",
+            "issued": "2016-01-06",
+            "keyword": [
+                "earth science",
+                "biosphere",
+                "vegetation"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1301",
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
             "spatial": "-48.5 -3.76 -47.51 -3.31",
+            "temporal": "2012-01-27T00:00:00Z/2014-04-25T23:59:59Z",
             "theme": [
                 "CMS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "CMS: Forest Inventory and Biophysical Measurements, Para, Brazil, 2012-2014"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/4DISDZEYDMGT",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "High Mountain Asia MAR V3.5 Regional Climate Model Output V001. Version 1. Archived by National Aeronautics and Space Administration, U.S. Government, NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/4DISDZEYDMGT.",
-            "issued": "2000-01-01",
-            "temporal": "2000-01-01T00:00:00Z/2015-12-31T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2015-12-31",
-            "keyword": [
-                "atmospheric winds",
-                "land surface",
-                "earth science",
-                "snow/ice",
-                "surface thermal properties",
-                "terrestrial hydrosphere",
-                "atmospheric radiation",
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
-            "identifier": "C1618449579-NSIDC_ECS",
             "description": "This data set provides modeled surface and atmospheric fields from the Mod\u00e8le Atmosph\u00e9rique R\u00e9gionale (MAR) regional climate model (version 3.5) over the Himalayan region at 10 km spatial resolution. Modeled parameters include surface mass and energy balance components, near-surface atmospheric properties, and snowpack properties.",
-            "title": "High Mountain Asia MAR V3.5 Regional Climate Model Output V001",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2F4DISDZEYDMGT",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2F4DISDZEYDMGT",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/HMA/HMA_MAR3_5.001/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/HMA/HMA_MAR3_5.001/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1618449579-NSIDC_ECS&m=9.993988037109377%2183.95504760742188%213%211%210%210%2C2&q=HMA_MAR3_5&ok=HMA_MAR3_5",
-                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1618449579-NSIDC_ECS&m=9.993988037109377%2183.95504760742188%213%211%210%210%2C2&q=HMA_MAR3_5&ok=HMA_MAR3_5",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/data/data-access-tool/HMA_MAR3_5/versions/1/",
-                    "description": "Data Access link for ITSD project",
                     "@type": "dcat:Distribution",
+                    "description": "Data Access link for ITSD project",
+                    "downloadURL": "https://nsidc.org/data/data-access-tool/HMA_MAR3_5/versions/1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/4DISDZEYDMGT",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/4DISDZEYDMGT",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/4DISDZEYDMGT",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/4DISDZEYDMGT",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C1618449579-NSIDC_ECS",
+            "issued": "2000-01-01",
+            "keyword": [
+                "atmospheric winds",
+                "land surface",
+                "earth science",
+                "snow/ice",
+                "surface thermal properties",
+                "terrestrial hydrosphere",
+                "atmospheric radiation",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.5067/4DISDZEYDMGT",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2015-12-31",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA NSIDC DAAC"
+            },
             "spatial": "65.2 22.41 87.92 38.84",
+            "temporal": "2000-01-01T00:00:00Z/2015-12-31T23:59:59.999Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "High Mountain Asia MAR V3.5 Regional Climate Model Output V001"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/GNSS/GNSS_IGSTROPZPDV1_001",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/GSFC/SED/ESD/GGL/CDDIS. https://doi.org/10.5067/GNSS/GNSS_IGSTROPZPDV1_001.",
-            "issued": "2000-01-01",
-            "temporal": "1997-01-01T00:00:00Z/2023-03-27T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-03-18",
-            "keyword": [
-                "earth science",
-                "solid earth",
-                "gravity/gravitational field",
-                "geodetics",
-                "tectonics"
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
-            "identifier": "C1708941255-CDDIS",
             "description": "This derived product set consists of version 1 of the Global Navigation Satellite System Final Troposphere Zenith Path Delay (ZPD) Product (daily files by station) from the NASA Crustal Dynamics Data Information System (CDDIS). GNSS provide autonomous geo-spatial positioning with global coverage. GNSS data sets from ground receivers at the CDDIS consist primarily of the data from the U.S. Global Positioning System (GPS) and the Russian GLObal NAvigation Satellite System (GLONASS). Analysis Centers (ACs) of the International GNSS Service (IGS) retrieve GNSS data on regular schedules to produce troposphere ZPD estimates for stations of the IGS network. The primary\u00a0troposphere products\u00a0generated from ground-based GNSS data are estimates of total zenith path delay and north/east troposphere gradient. Ancillary measurements of surface pressure and temperature allow the extraction of precipitable water vapor from the total zenith path delay. The IGS Troposphere Analysis Center Coordinator (ACC) used these individual AC solutions to generate the official version 1 of the IGS troposphere ZPD estimates for many of the stations in the IGS network. The final products consisted of daily files containing data from each observing station. All ZPD solution files utilize the Solution INdependent EXchange format for combination of TROpospheric estimates (SINEX_TRO) and span 24 hours from 00:00 to 23:45 UTC. In late 2006, a new version of the troposphere combination has been generated by the IGS Troposphere Analysis Center Coordinator. More information about the new version can be found under collection CDDIS_GNSS_IGSTroposphereZPD_product.",
-            "title": "Global Navigation Satellite System (GNSS) Troposphere Zenith Path Delay (ZPD) product (Version 1) from NASA CDDIS",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGNSS%2FGNSS_IGSTROPZPDV1_001",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGNSS%2FGNSS_IGSTROPZPDV1_001",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "ftp://cddis.nasa.gov/gnss/products",
-                    "description": "URL for retrieval of GNSS derived products through ftp",
                     "@type": "dcat:Distribution",
+                    "description": "URL for retrieval of GNSS derived products through ftp",
+                    "downloadURL": "ftp://cddis.nasa.gov/gnss/products",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://cddis.nasa.gov/Data_and_Derived_Products/GNSS/GNSS_product_holdings.html",
-                    "description": "URL for more information about GNSS derived products",
                     "@type": "dcat:Distribution",
+                    "description": "URL for more information about GNSS derived products",
+                    "downloadURL": "https://cddis.nasa.gov/Data_and_Derived_Products/GNSS/GNSS_product_holdings.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://dx.doi.org/10.5067/GNSS/GNSS_IGSTROPZPDV1_001",
-                    "description": "URL for more information about GNSS derived products",
                     "@type": "dcat:Distribution",
+                    "description": "URL for more information about GNSS derived products",
+                    "downloadURL": "http://dx.doi.org/10.5067/GNSS/GNSS_IGSTROPZPDV1_001",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 }
             ],
+            "identifier": "C1708941255-CDDIS",
+            "issued": "2000-01-01",
+            "keyword": [
+                "earth science",
+                "solid earth",
+                "gravity/gravitational field",
+                "geodetics",
+                "tectonics"
+            ],
+            "landingPage": "https://doi.org/10.5067/GNSS/GNSS_IGSTROPZPDV1_001",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2023-03-18",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GGL/CDDIS"
+            },
+            "temporal": "1997-01-01T00:00:00Z/2023-03-27T00:00:00Z",
             "theme": [
                 "IGS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Global Navigation Satellite System (GNSS) Troposphere Zenith Path Delay (ZPD) product (Version 1) from NASA CDDIS"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/B8A796JV7GGZ",
             "citation": "Natalya Kramarova. 2017-10-03. OMPS_NPP_NPBUVO3_L2. Version 2. OMPS-NPP L2 NP Ozone (O3) Vertical Profile swath orbital V2. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/B8A796JV7GGZ. https://disc.gsfc.nasa.gov/datacollection/OMPS_NPP_NPBUVO3_L2_2.html.",
-            "issued": "2017-09-27",
-            "temporal": "2011-11-13T00:00:00Z/2022-01-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2021-05-28",
-            "references": [
-                "https://doi.org/10.5194/amt-6-2533-2013"
-            ],
-            "keyword": [
-                "earth science",
-                "atmosphere",
-                "atmospheric chemistry"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "NATALYA KRAMAROVA",
                 "hasEmail": "mailto:Natalya.Kramarova@nasa.gov"
             },
-            "identifier": "C1412974465-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
-            "description": "The OMPS-NPP L2 NP Ozone (O3) Total Column swath orbital product provides ozone profile retrievals from the Ozone Mapping and Profiling Suite (OMPS) Nadir-Profiler (NP) instrument on the Suomi-NPP satellite. The V8 ozone profile algorithm relies on nadir profiler measurements made in the 250 to 310 nm range, as well as from measurements from the nadir mapper in the 300 to 380 nm range. Ozone mixing ratios are reported at 15 pressure levels between 50 and 0.5 hPa. Additionally, this data product contains measurements of total ozone, UV aerosol index and reflectivities at 331 and 380 nm.\n\nEach granule contains data from the daylight portion of each orbit measured for a full day. Spatial coverage is global (-82 to +82 degrees latitude), and there are about 14.5 orbits per day, each has typically 80 profiles. The NP footprint size is 250 km x 250 km. The files are written using the Hierarchical Data Format Version 5 or HDF5.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "OMPS_NPP_NPBUVO3_L2",
             "creator": "Natalya Kramarova",
-            "title": "OMPS-NPP L2 NP Ozone (O3) Vertical Profile swath orbital",
-            "graphic-preview-description": "OMPS Logo",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/OMPS_NPP_NPBUVO3_L2_2.jpeg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The OMPS-NPP L2 NP Ozone (O3) Total Column swath orbital product provides ozone profile retrievals from the Ozone Mapping and Profiling Suite (OMPS) Nadir-Profiler (NP) instrument on the Suomi-NPP satellite. The V8 ozone profile algorithm relies on nadir profiler measurements made in the 250 to 310 nm range, as well as from measurements from the nadir mapper in the 300 to 380 nm range. Ozone mixing ratios are reported at 15 pressure levels between 50 and 0.5 hPa. Additionally, this data product contains measurements of total ozone, UV aerosol index and reflectivities at 331 and 380 nm.\n\nEach granule contains data from the daylight portion of each orbit measured for a full day. Spatial coverage is global (-82 to +82 degrees latitude), and there are about 14.5 orbits per day, each has typically 80 profiles. The NP footprint size is 250 km x 250 km. The files are written using the Hierarchical Data Format Version 5 or HDF5.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FB8A796JV7GGZ",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FB8A796JV7GGZ",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/OMPS_NPP_NPBUVO3_L2_2.jpeg",
-                    "description": "OMPS Logo",
                     "@type": "dcat:Distribution",
+                    "description": "OMPS Logo",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/OMPS_NPP_NPBUVO3_L2_2.jpeg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/OMPS_NPP_NPBUVO3_L2_2.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/OMPS_NPP_NPBUVO3_L2_2.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://snpp-omps.gesdisc.eosdis.nasa.gov/data/SNPP_OMPS_Level2/OMPS_NPP_NPBUVO3_L2.2/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://snpp-omps.gesdisc.eosdis.nasa.gov/data/SNPP_OMPS_Level2/OMPS_NPP_NPBUVO3_L2.2/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://snpp-omps.gesdisc.eosdis.nasa.gov/opendap/SNPP_OMPS_Level2/OMPS_NPP_NPBUVO3_L2.2/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://snpp-omps.gesdisc.eosdis.nasa.gov/opendap/SNPP_OMPS_Level2/OMPS_NPP_NPBUVO3_L2.2/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=OMPS_NPP_NPBUVO3_L2_2",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=OMPS_NPP_NPBUVO3_L2_2",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://snpp-omps.gesdisc.eosdis.nasa.gov/data/SNPP_OMPS_Level2/OMPS_NPP_NPBUVO3_L2.2/doc/README.OMPS_NPP_NPBUVO3_L2_v87.pdf",
-                    "description": "README Document",
                     "@type": "dcat:Distribution",
+                    "description": "README Document",
+                    "downloadURL": "https://snpp-omps.gesdisc.eosdis.nasa.gov/data/SNPP_OMPS_Level2/OMPS_NPP_NPBUVO3_L2.2/doc/README.OMPS_NPP_NPBUVO3_L2_v87.pdf",
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
+            "graphic-preview-description": "OMPS Logo",
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/OMPS_NPP_NPBUVO3_L2_2.jpeg",
+            "identifier": "C1412974465-GES_DISC",
+            "issued": "2017-09-27",
+            "keyword": [
+                "earth science",
+                "atmosphere",
+                "atmospheric chemistry"
+            ],
+            "landingPage": "https://doi.org/10.5067/B8A796JV7GGZ",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2021-05-28",
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
+            "temporal": "2011-11-13T00:00:00Z/2022-01-17T00:00:00Z",
             "theme": [
                 "NPP-JPSS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "OMPS-NPP L2 NP Ozone (O3) Vertical Profile swath orbital"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG1-J-MAG-4-1.92SEC",
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
+            "description": "This data set includes Voyager 1 Jupiter encounter magnetometer data that have been resampled at a 1.92 second sample rate. The data set is composed of 6 columns: 1) ctime - this column contains the data acquisition time. The time is always output in the ISO standard spacecraft event time format (yyyy-mm-dd-Thh:mm:ss.sss) but is stored internally in Cline time which is measured in seconds after 00:00:00.000 Jan 01, 1966, 2) br - this column contains the radial component of the magnetic field, 3) bphi - this column contains the phi component of the magnetic field, 4) btheta - this column contains the theta component of the magnetic field, 5) bmag - this column contains the magnitude of the magnetic field, 6) flag - a flag value that indicates either software error or spacecraft hardware interference reduced confidence in this record (flag value of 1 is bad , 0 is good or unchecked). All magnetic field observations are measured in nanoTeslas. The coordinate system for this dataset is Minus System III. All of the magnetic field data are calibrated (see the instrument calibration description for more details). The Jupiter System III coordinate system is defined in Dessler 1983 and the reference documents for this dataset are: Ness et al, 1979 Lepping et al, 1981 Connerney,Acuna,Ness, 1981 Behannon,Burlaga,Ness, 1981",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg1-j-mag-4-1.92sec_knzb-8j4w",
+            "issued": "2018-06-26",
+            "keyword": [
+                "voyager",
+                "jupiter"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG1-J-MAG-4-1.92SEC",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg1-j-mag-4-1.92sec_knzb-8j4w",
-            "description": "This data set includes Voyager 1 Jupiter encounter magnetometer data that have been resampled at a 1.92 second sample rate. The data set is composed of 6 columns: 1) ctime - this column contains the data acquisition time. The time is always output in the ISO standard spacecraft event time format (yyyy-mm-dd-Thh:mm:ss.sss) but is stored internally in Cline time which is measured in seconds after 00:00:00.000 Jan 01, 1966, 2) br - this column contains the radial component of the magnetic field, 3) bphi - this column contains the phi component of the magnetic field, 4) btheta - this column contains the theta component of the magnetic field, 5) bmag - this column contains the magnitude of the magnetic field, 6) flag - a flag value that indicates either software error or spacecraft hardware interference reduced confidence in this record (flag value of 1 is bad , 0 is good or unchecked). All magnetic field observations are measured in nanoTeslas. The coordinate system for this dataset is Minus System III. All of the magnetic field data are calibrated (see the instrument calibration description for more details). The Jupiter System III coordinate system is defined in Dessler 1983 and the reference documents for this dataset are: Ness et al, 1979 Lepping et al, 1981 Connerney,Acuna,Ness, 1981 Behannon,Burlaga,Ness, 1981",
-            "title": "VOYAGER 1 JUPITER MAGNETOMETER RESAMPLED DATA 1.92 SEC",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "VOYAGER 1 JUPITER MAGNETOMETER RESAMPLED DATA 1.92 SEC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=CO-E%2FSW%2FJ%2FS-MAG-3-RDR-CALIB-SHM-V2.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This data set contains magnetic-field data acquired during the cruise and tour phases of the Cassini mission to Saturn. Data collection began on 16 August (day 228), 1999. On this date, two days before the spacecraft commenced Earth swingby, the magnetometer boom was unfurled into its extended position; a configuration it maintained for the remainder of the mission. This dataset contains the data collected from the helium magnetometer while in scalar mode (SHM). The SHM mode is used only when high fields are expected, this means that SHM data is only collected infrequently and ceased being collected after 17 November (day 321), 2005 due to an instrument failure.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.co-e-sw-j-s-mag-3-rdr-calib-shm-v2.0",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2021-05-21",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "titan",
                 "venus",
@@ -1041263,405 +1041265,386 @@
                 "cassini-huygens",
                 "saturn"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=CO-E%2FSW%2FJ%2FS-MAG-3-RDR-CALIB-SHM-V2.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.co-e-sw-j-s-mag-3-rdr-calib-shm-v2.0",
-            "description": "This data set contains magnetic-field data acquired during the cruise and tour phases of the Cassini mission to Saturn. Data collection began on 16 August (day 228), 1999. On this date, two days before the spacecraft commenced Earth swingby, the magnetometer boom was unfurled into its extended position; a configuration it maintained for the remainder of the mission. This dataset contains the data collected from the helium magnetometer while in scalar mode (SHM). The SHM mode is used only when high fields are expected, this means that SHM data is only collected infrequently and ceased being collected after 17 November (day 321), 2005 due to an instrument failure.",
-            "title": "CASSINI SCALAR MAGNETOMETER CALIB DATA V2.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "CASSINI SCALAR MAGNETOMETER CALIB DATA V2.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1626189758-LARC.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "MISR Science Team (2007), Terra/MISR Level 2, TOA/Cloud Aerosol Product subset for the VBBE region, version 2, Hampton, VA, USA: NASA Atmospheric Science Data Center (ASDC), Accessed <author citing data inserts date here> at doi: TBD",
-            "issued": "2019-07-25",
-            "temporal": "2007-08-01T02:41:24Z/2007-11-30T03:43:32Z",
-            "@type": "dcat:Dataset",
-            "modified": "2019-07-25",
-            "keyword": [
-                "air quality",
-                "earth science",
-                "atmosphere",
-                "aerosols"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Earl Hansen",
                 "hasEmail": "mailto:earl.g.hansen@jpl.nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/LARC/SD/ASDC"
-            },
-            "identifier": "C1626189758-LARC",
             "description": "Multi-angle Imaging SpectroRadiometer (MISR) is an instrument designed to view Earth with cameras pointed in 9 different directions. As the instrument flies overhead, each piece of Earth's surface below is successively imaged by all 9 cameras, in each of 4 wavelengths (blue, green, red, and near-infrared). The goal of MISR is to improve our understanding of the fate of sunlight in Earth environment, as well as distinguish different types of clouds, particles and surfaces. Specifically, MISR monitors the monthly, seasonal, and long-term trends in three areas: 1) amount and type of atmospheric particles (aerosols), including those formed by natural sources and by human activities; 2) amounts, types, and heights of clouds, and 3) distribution of land surface cover, including vegetation canopy structure. MISR Level 2 TOA/Cloud Aerosol Product subset for the VBBE region V002 contains Aerosol optical depth and particle type, with associated atmospheric data.",
-            "title": "MISR Level 2 TOA/Cloud Aerosol Product subset for the VBBE region V002",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/search/concepts/C1626189758-LARC.html",
-                    "description": "View this dataset on the CMR (Common Metadata Repository)",
                     "@type": "dcat:Distribution",
+                    "description": "View this dataset on the CMR (Common Metadata Repository)",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/search/concepts/C1626189758-LARC.html",
+                    "mediaType": "text/html",
                     "title": "CMR"
                 }
             ],
+            "identifier": "C1626189758-LARC",
+            "issued": "2019-07-25",
+            "keyword": [
+                "air quality",
+                "earth science",
+                "atmosphere",
+                "aerosols"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1626189758-LARC.html",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2019-07-25",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/LARC/SD/ASDC"
+            },
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2007-08-01T02:41:24Z/2007-11-30T03:43:32Z",
             "theme": [
                 "VBBE_2007",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "MISR Level 2 TOA/Cloud Aerosol Product subset for the VBBE region V002"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG2-S-PWS-4-SA-48.0SEC",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This data set consists of 48-second calibrated, averaged wave electric field intensities from the Voyager 2 Plasma Wave Receiver spectrum analyzer obtained in the vicinity of the Saturnian magnetosphere. For each 48-second interval, a geometric average field strength is determined for each of the 16 spectrum analyzer channels whose center frequencies range from 10 Hertz to 56.2 kilo- Hertz and which are logarithmically spaced in frequency, four channels per decade. The time associated with each set of averages is the beginning of the averating interval. Averages are stored in units of volt/meter. During data gaps where complete 48-second intervals are missing, no entries exist in the file, that is, the gaps are not zero-filled or tagged in any other way. Additional information about this dataset and the instrument which produced it can be found elsewhere in this catalog. An overview of the data in this data set can be found in Scarf et al. [1982] and a complete instrument description can be found in Scarf and Gurnett [1977].",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg2-s-pws-4-sa-48.0sec_kpae-pgz4",
             "issued": "2021-05-21",
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
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG2-S-PWS-4-SA-48.0SEC",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg2-s-pws-4-sa-48.0sec_kpae-pgz4",
-            "description": "This data set consists of 48-second calibrated, averaged wave electric field intensities from the Voyager 2 Plasma Wave Receiver spectrum analyzer obtained in the vicinity of the Saturnian magnetosphere. For each 48-second interval, a geometric average field strength is determined for each of the 16 spectrum analyzer channels whose center frequencies range from 10 Hertz to 56.2 kilo- Hertz and which are logarithmically spaced in frequency, four channels per decade. The time associated with each set of averages is the beginning of the averating interval. Averages are stored in units of volt/meter. During data gaps where complete 48-second intervals are missing, no entries exist in the file, that is, the gaps are not zero-filled or tagged in any other way. Additional information about this dataset and the instrument which produced it can be found elsewhere in this catalog. An overview of the data in this data set can be found in Scarf et al. [1982] and a complete instrument description can be found in Scarf and Gurnett [1977].",
-            "title": "VOYAGER 2 SAT PLASMA WAVE SPECTROMETER RESAMP SPEC 48.0SEC",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "VOYAGER 2 SAT PLASMA WAVE SPECTROMETER RESAMP SPEC 48.0SEC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/AMSR-E/AE_MOOCN.002",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "AMSR-E/Aqua Monthly L3 Global Ascending/Descending .25x.25 deg Ocean Grids V002. Version 2. Archived by National Aeronautics and Space Administration, U.S. Government, NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/AMSR-E/AE_MOOCN.002.",
-            "issued": "2002-06-19",
-            "temporal": "2002-06-19T00:00:00Z/2011-10-01T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2011-10-01",
-            "keyword": [
-                "ocean winds",
-                "atmospheric winds",
-                "atmospheric water vapor",
-                "clouds",
-                "earth science",
-                "ocean temperature",
-                "oceans",
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
-            "identifier": "C179014697-NSIDC_ECS",
             "description": "The Level-3 daily product (AE_DyOcn), weekly product (AE_WkOcn), and monthly product (AE_MoOcn) include SST, near-surface wind speed, columnar water vapor, and columnar cloud liquid water over oceans in a 0.25 degree by 0.25 degree grid, generated from AE_Ocean.",
-            "title": "AMSR-E/Aqua Monthly L3 Global Ascending/Descending .25x.25 deg Ocean Grids V002",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAMSR-E%2FAE_MOOCN.002",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAMSR-E%2FAE_MOOCN.002",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/AMSA/AE_MoOcn.002",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/AMSA/AE_MoOcn.002",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C179014697-NSIDC_ECS&m=-31.078125%210.28125%211%211%210%210%2C2&q=AE_MoOcn",
-                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C179014697-NSIDC_ECS&m=-31.078125%210.28125%211%211%210%210%2C2&q=AE_MoOcn",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/data/data-access-tool/AE_MoOcn/versions/2/",
-                    "description": "Data Access link for ITSD project",
                     "@type": "dcat:Distribution",
+                    "description": "Data Access link for ITSD project",
+                    "downloadURL": "https://nsidc.org/data/data-access-tool/AE_MoOcn/versions/2/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/AMSR-E/AE_MOOCN.002",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/AMSR-E/AE_MOOCN.002",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/AMSR-E/AE_MOOCN.002",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/AMSR-E/AE_MOOCN.002",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C179014697-NSIDC_ECS",
+            "issued": "2002-06-19",
+            "keyword": [
+                "ocean winds",
+                "atmospheric winds",
+                "atmospheric water vapor",
+                "clouds",
+                "earth science",
+                "ocean temperature",
+                "oceans",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.5067/AMSR-E/AE_MOOCN.002",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2011-10-01",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA NSIDC DAAC"
+            },
             "spatial": "-180.0 -89.24 180.0 89.24",
+            "temporal": "2002-06-19T00:00:00Z/2011-10-01T23:59:59.999Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "AMSR-E/Aqua Monthly L3 Global Ascending/Descending .25x.25 deg Ocean Grids V002"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/120",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Wang, J. R. 1994. Stream Flow Storm Data (FIFE). Data set. Available on-line [http://www.daac.ornl.gov] from Oak Ridge National Laboratory Distributed Active Archive Center, Oak Ridge, Tennessee, U.S.A. Also published in D. E. Strebel, D. R. Landis, K. F. Huemmrich, and B. W. Meeson (eds.), Collected Data of the First ISLSCP Field Experiment, Vol. 1: Surface Observations and Non-Image Data Sets. CD-ROM. National Aeronautics and Space Administration, Goddard Space Flight Center, Greenbelt, Maryland, U.S.A. (available from http://www.daac.ornl.gov). doi:10.3334/ORNLDAAC/120",
-            "issued": "2024-05-04",
-            "temporal": "1987-01-01T00:00:00Z/1988-01-01T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-07",
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
-            "identifier": "C2980689463-ORNL_CLOUD",
             "description": "USGS stream flow during storm events around Kings Creek on the Konza Prairie",
-            "graphic-preview-description": "Browse Image",
-            "title": "Stream Flow Storm Data (FIFE)",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/fife_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F120",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F120",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/fife/fife_hydrology_strm_st/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/fife/fife_hydrology_strm_st/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/FIFE/guides/stream_flow_storm.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/FIFE/guides/stream_flow_storm.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/120",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/120",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/fife/fife_hydrology_strm_st/comp/stream_flow_storm.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/fife/fife_hydrology_strm_st/comp/stream_flow_storm.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/msword",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/fife/fife_hydrology_strm_st/comp/strm_st.doc",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/fife/fife_hydrology_strm_st/comp/strm_st.doc",
+                    "mediaType": "application/msword",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/fife/fife_hydrology_strm_st/comp/strm_st.tdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/fife/fife_hydrology_strm_st/comp/strm_st.tdf",
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
+            "identifier": "C2980689463-ORNL_CLOUD",
+            "issued": "2024-05-04",
+            "keyword": [
+                "surface water",
+                "earth science",
+                "terrestrial hydrosphere"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/120",
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
             "spatial": "-96.58 39.07 -96.56 39.09",
+            "temporal": "1987-01-01T00:00:00Z/1988-01-01T23:59:59Z",
             "theme": [
                 "FIFE",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Stream Flow Storm Data (FIFE)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewBundle.jsp?identifier=urn%3Anasa%3Apds%3Amer2_mtes_derived_emissivity&version=1.0",
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
+            "description": "This bundle contains emissivity data from the Mini-TES instrument on Mars Exploration Rover 2 (Spirit).",
+            "identifier": "urn:nasa:pds:mer2_mtes_derived_emissivity",
+            "issued": "2021-05-21",
+            "keyword": [
+                "mars",
+                "mars exploration rover"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewBundle.jsp?identifier=urn%3Anasa%3Apds%3Amer2_mtes_derived_emissivity&version=1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:mer2_mtes_derived_emissivity",
-            "description": "This bundle contains emissivity data from the Mini-TES instrument on Mars Exploration Rover 2 (Spirit).",
-            "title": "MER2 Mini-TES Derived Emissivity Data Bundle",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "MER2 Mini-TES Derived Emissivity Data Bundle"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=CO-SS-RSS-1-SCC7-V1.0",
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
-                "solar system",
-                "cassini-huygens"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "The Cassini Radio Science Solar Corona Characterization Experiment (SCC7) Raw Data Archive is a time-ordered collection of radio science raw data acquired from October 1 to October 13, 2010, during the Cassini Extended Mission.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.co-ss-rss-1-scc7-v1.0_kpgc-2iqn",
+            "issued": "2018-06-26",
+            "keyword": [
+                "solar system",
+                "cassini-huygens"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=CO-SS-RSS-1-SCC7-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.co-ss-rss-1-scc7-v1.0_kpgc-2iqn",
-            "description": "The Cassini Radio Science Solar Corona Characterization Experiment (SCC7) Raw Data Archive is a time-ordered collection of radio science raw data acquired from October 1 to October 13, 2010, during the Cassini Extended Mission.",
-            "title": "CASSINI RSS RAW DATA SET - SCC7 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "CASSINI RSS RAW DATA SET - SCC7 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1000000014-CDDIS.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/GSFC/SED/ESD/GGL/CDDIS.",
-            "issued": "1994-01-01",
-            "temporal": "1994-01-01T00:00:00Z/2022-01-17T00:00:00Z",
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
-            "identifier": "C1000000014-CDDIS",
             "description": "Precise satellite orbits derived from analysis of Global Navigation Satellite System (GNSS) data. Analysis Centers (ACs) of the International GNSS Service (IGS) retrieve GNSS data on regular schedules to produce precise orbits identifying the position and velocity of the GNSS satellites. These orbits are determined sub-daily (ultra-rapid generation), daily (rapid generation), and weekly (final IGS product). The IGS Analysis Center Coordinator retrieves these individual solutions and generates the official IGS combined orbit products. The orbits generated by the individual ACs and the combination products generated by the ACCs are available at the CDDIS. These orbits can be used to determine precise coordinates of the observing stations, gravity field parameters, and Earth orientation parameters.",
-            "title": "CDDIS_GNSS_products_orbit_rapid",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -1041670,163 +1041653,151 @@
                     "title": "Download this dataset"
                 }
             ],
+            "identifier": "C1000000014-CDDIS",
+            "issued": "1994-01-01",
+            "keyword": [
+                "nasa"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1000000014-CDDIS.html",
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
+            "temporal": "1994-01-01T00:00:00Z/2022-01-17T00:00:00Z",
             "theme": [
                 "IGS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "CDDIS_GNSS_products_orbit_rapid"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1734",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Ryerson, T.B., C.R. Thompson, J. Peischl, and I. Bourgeois. 2019. ATom: L2 In Situ Measurements from NOAA Nitrogen Oxides and Ozone (NOyO3) Instrument. ORNL DAAC, Oak Ridge, Tennessee, USA. https://doi.org/10.3334/ORNLDAAC/1734",
-            "issued": "2019-09-30",
-            "temporal": "2016-07-29T14:33:18Z/2018-05-21T23:37:58Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-06-12",
-            "keyword": [
-                "atmospheric chemistry",
-                "atmosphere",
-                "air quality",
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
-            "identifier": "C2676921722-ORNL_CLOUD",
             "description": "This dataset provides in situ concentrations of nitric oxide (NO), nitrogen dioxide (NO2), total reactive nitrogen oxides (NOy), and ozone (O3) measured by the NOAA Nitrogen Oxides and Ozone (NOyO3) 4-channel chemiluminescence (CL) instrument during airborne campaigns conducted by NASA's Atmospheric Tomography (ATom) mission. NOyO3 provides fast-response, specific, high precision, and calibrated measurements of nitrogen oxides and ozone at a spatial resolution of better than 100 m. ATom deploys an extensive gas and aerosol payload on the NASA DC-8 aircraft for systematic, global-scale sampling of the atmosphere, profiling continuously from 0.2 to 12 km altitude. Flights occurred in each of 4 seasons from 2016 to 2018. Flights originate from the Armstrong Flight Research Center in Palmdale, California, fly north to the western Arctic, south to the South Pacific, east to the Atlantic, north to Greenland, and return to California across central North America. ATom establishes a single, contiguous, global-scale dataset. This comprehensive dataset will be used to improve the representation of chemically reactive gases and short-lived climate forcers in global models of atmospheric chemistry and climate.",
-            "graphic-preview-description": "The  NOAA NOyO3 4-channel chemiluminescence (CL) instrument.",
-            "title": "ATom: L2 In Situ Measurements from NOAA Nitrogen Oxides and Ozone (NOyO3) Instrument",
-            "graphic-preview-file": "https://daac.ornl.gov/ATOM/guides/ATom_NOyO3_Instrument_Data_Fig1.jpg",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1734",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1734",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/atom/ATom_NOyO3_Instrument_Data/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/atom/ATom_NOyO3_Instrument_Data/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/ATOM/guides/ATom_NOyO3_Instrument_Data.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/ATOM/guides/ATom_NOyO3_Instrument_Data.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1734",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1734",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/atom/ATom_NOyO3_Instrument_Data/comp/ATom_NOyO3_Instrument_Data.pdf",
-                    "description": "ATom: L2 Measurements from NOAA Nitrogen Oxides and Ozone (NOyO3): ATom_NOyO3_Instrument_Data.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "ATom: L2 Measurements from NOAA Nitrogen Oxides and Ozone (NOyO3): ATom_NOyO3_Instrument_Data.pdf",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/atom/ATom_NOyO3_Instrument_Data/comp/ATom_NOyO3_Instrument_Data.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://daac.ornl.gov/ATOM/guides/ATom_NOyO3_Instrument_Data_Fig1.jpg",
-                    "description": "The  NOAA NOyO3 4-channel chemiluminescence (CL) instrument.",
                     "@type": "dcat:Distribution",
+                    "description": "The  NOAA NOyO3 4-channel chemiluminescence (CL) instrument.",
+                    "downloadURL": "https://daac.ornl.gov/ATOM/guides/ATom_NOyO3_Instrument_Data_Fig1.jpg",
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
+            "graphic-preview-description": "The  NOAA NOyO3 4-channel chemiluminescence (CL) instrument.",
+            "graphic-preview-file": "https://daac.ornl.gov/ATOM/guides/ATom_NOyO3_Instrument_Data_Fig1.jpg",
+            "identifier": "C2676921722-ORNL_CLOUD",
+            "issued": "2019-09-30",
+            "keyword": [
+                "atmospheric chemistry",
+                "atmosphere",
+                "air quality",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1734",
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
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2016-07-29T14:33:18Z/2018-05-21T23:37:58Z",
             "theme": [
                 "ATom",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "ATom: L2 In Situ Measurements from NOAA Nitrogen Oxides and Ozone (NOyO3) Instrument"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/GEWEXSRB/Rel4-IP_Ancillary_3hrly_1",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/GEWEXSRB/Rel4-IP_Ancillary_3hrly_1.",
-            "issued": "2020-10-05",
-            "temporal": "1988-01-01T00:00:00Z/2009-12-31T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-10-05",
-            "keyword": [
-                "surface thermal properties",
-                "snow/ice",
-                "land surface",
-                "earth science",
-                "terrestrial hydrosphere",
-                "cryosphere",
-                "clouds",
-                "atmospheric water vapor",
-                "atmosphere",
-                "atmospheric chemistry",
-                "atmospheric temperature",
-                "atmospheric radiation",
-                "atmospheric pressure"
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
-            "identifier": "C2062227429-LARC_ASDC",
             "description": "GEWEX SRB Integrated Product (Rel-4) Ancillary 3-Hourly contains the global fields of meteorology, clouds and other ancillary data that serves as the inputs to the GEWEX SRB Integrated Product (Rel-4) Longwave algorithm, although some are applicable to the Shortwave product as well. Included are surface skin temperature, near-surface meteorology, Fu-Liou longwave algorithm based bands of surface emissivity, snow and ice amount, total column precipitable water, total column ozone, total cloud properties, and three-level water and ice cloud properties. The temporal range is January 1988 through December 2009, with the ends bound by input constraints. These data are available in NetCDF-4.",
-            "title": "GEWEX SRB Integrated Product (Rel-4) Ancillary 3-Hourly",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGEWEXSRB%2FRel4-IP_Ancillary_3hrly_1",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGEWEXSRB%2FRel4-IP_Ancillary_3hrly_1",
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
@@ -1041842,10 +1041813,10 @@
                     "title": "View this dataset's algorithm theoretical basis document"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/GEWEXSRB/Rel4-IP_Ancillary_3hrly_1",
-                    "description": "Data set landing page for GEWEXSRB_Rel4-IP_Ancillary_3hrly",
                     "@type": "dcat:Distribution",
+                    "description": "Data set landing page for GEWEXSRB_Rel4-IP_Ancillary_3hrly",
+                    "downloadURL": "https://doi.org/10.5067/GEWEXSRB/Rel4-IP_Ancillary_3hrly_1",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
@@ -1041855,305 +1041826,316 @@
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/SRB/GEWEXSRB_Rel4-IP/Ancillary_3hrly_1/",
-                    "description": "ASDC Direct Data Download for GEWEXSRB_Rel4-IP_Ancillary_3hrly_1",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for GEWEXSRB_Rel4-IP_Ancillary_3hrly_1",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/SRB/GEWEXSRB_Rel4-IP/Ancillary_3hrly_1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/SRB/GEWEXSRB_Rel4-IP/Ancillary_3hrly_1/contents.html",
-                    "description": "OPeNDAP data access for GEWEXSRB_Rel4-IP_Ancillary_3hrly_1",
                     "@type": "dcat:Distribution",
+                    "description": "OPeNDAP data access for GEWEXSRB_Rel4-IP_Ancillary_3hrly_1",
+                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/SRB/GEWEXSRB_Rel4-IP/Ancillary_3hrly_1/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 }
             ],
+            "identifier": "C2062227429-LARC_ASDC",
+            "issued": "2020-10-05",
+            "keyword": [
+                "surface thermal properties",
+                "snow/ice",
+                "land surface",
+                "earth science",
+                "terrestrial hydrosphere",
+                "cryosphere",
+                "clouds",
+                "atmospheric water vapor",
+                "atmosphere",
+                "atmospheric chemistry",
+                "atmospheric temperature",
+                "atmospheric radiation",
+                "atmospheric pressure"
+            ],
+            "landingPage": "https://doi.org/10.5067/GEWEXSRB/Rel4-IP_Ancillary_3hrly_1",
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
+            "temporal": "1988-01-01T00:00:00Z/2009-12-31T23:59:59.999Z",
             "theme": [
                 "SRB",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "GEWEX SRB Integrated Product (Rel-4) Ancillary 3-Hourly"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-4-PRL-67P-M01-REFLECT-V1.0",
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
+            "description": "This CODMAC level 4 data set contains radiometric calibrated and geometric distortion corrected (resampled) image data in reflectance units (normalized and thus without unit), acquired by the OSIRIS Wide Angle Camera on the Rosetta spacecraft during the PRELANDING mission phase, covering the period from 2014-01-20T10:00:00.000 to 2014-05-07T12:47:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V1.0 is the first version of this dataset: Lien corrected dataset after October 2018 PSA/PDS external peer review.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-4-prl-67p-m01-reflect-v1.0_kpmz-xpc8",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-4-PRL-67P-M01-REFLECT-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-4-prl-67p-m01-reflect-v1.0_kpmz-xpc8",
-            "description": "This CODMAC level 4 data set contains radiometric calibrated and geometric distortion corrected (resampled) image data in reflectance units (normalized and thus without unit), acquired by the OSIRIS Wide Angle Camera on the Rosetta spacecraft during the PRELANDING mission phase, covering the period from 2014-01-20T10:00:00.000 to 2014-05-07T12:47:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V1.0 is the first version of this dataset: Lien corrected dataset after October 2018 PSA/PDS external peer review.",
-            "title": "ROSETTA-ORBITER 67P OSIWAC 4 PRL-MTP001 RDR-REFLECT V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P OSIWAC 4 PRL-MTP001 RDR-REFLECT V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-EXT1-1394-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the ROSETTA EXTENSION 1 phase 2016-01-01 to 2016-04-05. It is a Global Gravity measurement at the comet 67P and covers the time 2016-02-03T05:01:05.000 to 2016-02-03T08:50:46.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-ext1-1394-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-EXT1-1394-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-ext1-1394-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the ROSETTA EXTENSION 1 phase 2016-01-01 to 2016-04-05. It is a Global Gravity measurement at the comet 67P and covers the time 2016-02-03T05:01:05.000 to 2016-02-03T08:50:46.000.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     ROSETTA EXTENSION 1 1394 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     ROSETTA EXTENSION 1 1394 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1386206906-NSIDCV0.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Northern Hemisphere EASE-Grid Annual Freezing and Thawing  Indices, 1901 - 2002, Version 1. Version 1. Archived by National Aeronautics and Space Administration, U.S. Government, National Snow and Ice Data Center.",
-            "issued": "1901-01-01",
-            "temporal": "1901-01-01T00:00:00Z/2002-12-31T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2002-12-31",
-            "keyword": [
-                "atmospheric temperature",
-                "atmosphere",
-                "earth science"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Tingjun Zhang",
                 "hasEmail": "mailto:nsidc@nsidc.org"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NSIDC"
-            },
-            "identifier": "C1386206906-NSIDCV0",
             "description": "This data set contains annual freezing and thawing indices for each year from 1901 to 2002 on the 25 km resolution Equal-Area Scalable Earth Grid (EASE-Grid). Annual freezing and thawing indices are defined as the cumulative number of degree-days when air temperatures are below and above 0 degrees C. The values were calculated based upon the monthly mean air temperature from the 1901-2002, 0.5 deg. global land temperatures from the University of East Anglia Climate Research Unit (Mitchell and Jones, 2005).\n\nTwo ASCII files are available for each year for the freezing and thawing indices, respectively. Each file is approximately 5.5 MB in size. In addition, there is one 10.4 MB ASCII file defining the latitude and longitude coordinates for each grid point. The data set is available in compressed form via FTP.",
-            "title": "Northern Hemisphere EASE-Grid Annual Freezing and Thawing  Indices, 1901 - 2002, Version 1",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/forms/GGD649_or.html?major_version=1",
-                    "description": "Direct download, with optional registration page.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download, with optional registration page.",
+                    "downloadURL": "https://nsidc.org/forms/GGD649_or.html?major_version=1",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/data/GGD649/versions/1",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://nsidc.org/data/GGD649/versions/1",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/data/GGD649/versions/1",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                {
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://nsidc.org/data/GGD649/versions/1",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C1386206906-NSIDCV0",
+            "issued": "1901-01-01",
+            "keyword": [
+                "atmospheric temperature",
+                "atmosphere",
+                "earth science"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1386206906-NSIDCV0.html",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2002-12-31",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NSIDC"
+            },
             "spatial": "-180.0 0.0 180.0 90.0",
+            "temporal": "1901-01-01T00:00:00Z/2002-12-31T23:59:59.999Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Northern Hemisphere EASE-Grid Annual Freezing and Thawing  Indices, 1901 - 2002, Version 1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RPCLAP-3-ESC4-CALIB2-V1.0",
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
+            "description": "This data set contains\nCALIBRATED data from Rosetta RPC-LAP, acquired during the COMET ESCORT 4\nmission phase where the primary target was the comet\n67P/CHURYUMOV-GERASIMENKO 1 (1969 R1). It contains instrument outputs in\nvolts and amperes, calibrated and corrected for instrument offsets.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rpclap-3-esc4-calib2-v1.0_kpsn-r74q",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RPCLAP-3-ESC4-CALIB2-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rpclap-3-esc4-calib2-v1.0_kpsn-r74q",
-            "description": "This data set contains\nCALIBRATED data from Rosetta RPC-LAP, acquired during the COMET ESCORT 4\nmission phase where the primary target was the comet\n67P/CHURYUMOV-GERASIMENKO 1 (1969 R1). It contains instrument outputs in\nvolts and amperes, calibrated and corrected for instrument offsets.",
-            "title": "ROSETTA-ORBITER 67P RPCLAP 3\nESC4 CALIB2 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RPCLAP 3\nESC4 CALIB2 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewBundle.jsp?identifier=urn%3Anasa%3Apds%3Amess_rs_derived&version=3.0",
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
-                "messenger",
-                "mercury"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "The bundle contains derived models of Mercury gravity and topography from radio science  tracking and from the MLA instrument on MESSENGER. There are three product types: the Occultation Summary (OCC), the Spherical Harmonics ASCII Data Records (SHADR), and the Spherical Harmonics Binary Data Records (SHBDR).",
+            "identifier": "urn:nasa:pds:mess_rs_derived",
+            "issued": "2021-05-21",
+            "keyword": [
+                "messenger",
+                "mercury"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewBundle.jsp?identifier=urn%3Anasa%3Apds%3Amess_rs_derived&version=3.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:mess_rs_derived",
-            "description": "The bundle contains derived models of Mercury gravity and topography from radio science  tracking and from the MLA instrument on MESSENGER. There are three product types: the Occultation Summary (OCC), the Spherical Harmonics ASCII Data Records (SHADR), and the Spherical Harmonics Binary Data Records (SHBDR).",
-            "title": "MESSENGER gravity and topography spherical harmonics model bundle",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "MESSENGER gravity and topography spherical harmonics model bundle"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC4-1174-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 4 phase 2015-10-22 to 2015-12-31. It is a Global Gravity measurement at the comet 67P and covers the time 2015-11-12T02:30:10.000 to 2015-11-12T07:27:23.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc4-1174-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC4-1174-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc4-1174-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 4 phase 2015-10-22 to 2015-12-31. It is a Global Gravity measurement at the comet 67P and covers the time 2015-11-12T02:30:10.000 to 2015-11-12T07:27:23.000.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 4 1174 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 4 1174 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.nasa.gov/d/kpxj-46ib",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2021-04-13",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-31",
-            "keyword": [
-                "jets",
-                "acoustic",
-                "nozzle"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Brenda Henderson",
                 "hasEmail": "mailto:brenda.s.henderson@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA"
-            },
-            "identifier": "https://data.nasa.gov/api/views/kpxj-46ib",
             "description": "A series of nozzle chevrons were designed to create a parametric family with varying length, penetration and width, with the objective of demonstrating noise reduction for supersonic nozzles. Eight sets of chevrons were fabricated and tested on the High-Flow Jet Exit Rig in the Aero-Acoustic Propulsion Lab at the NASA Glenn Research Center in 2009. Details of the test are given in the paper \"An MDOE Investigation of Chevrons for Supersonic Jet Noise Reduction\" by Henderson and Bridges (DOI: 10.2514/6.2010-3926). This data repository contains a test requirements document with configuration and flow definitions, a spreadsheet with measured jet flow conditions from the test, chevron geometry files in CAD format, and a set of files containing spectral directivity measurements of the acoustic far-field at the ~350 test points. Details about the data files are contained in a README document.",
-            "title": "SERDP09 MDOE chevron nozzle noise database",
-            "programCode": [
-                "026:021"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -1042161,818 +1042143,814 @@
                     "mediaType": "application/zip"
                 }
             ],
+            "identifier": "https://data.nasa.gov/api/views/kpxj-46ib",
+            "issued": "2021-04-13",
+            "keyword": [
+                "jets",
+                "acoustic",
+                "nozzle"
+            ],
+            "landingPage": "https://data.nasa.gov/d/kpxj-46ib",
             "license": "https://www.usa.gov/government-works",
+            "modified": "2023-01-31",
+            "programCode": [
+                "026:021"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA"
+            },
             "theme": [
                 "Aerospace"
-            ]
+            ],
+            "title": "SERDP09 MDOE chevron nozzle noise database"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=CO-SSA-RSS-1-TIGR14-V1.0",
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
+            "description": "The Cassini Radio Science Titan Gravity Science Experiment (TIGR14) Raw Data Archive is a time-ordered collection of radio science raw data acquired on April 3, 5, June 21 and 23, 2009, during he Cassini Extended Mission.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.co-ssa-rss-1-tigr14-v1.0_kpza-j5gp",
+            "issued": "2018-06-26",
+            "keyword": [
+                "cassini-huygens",
+                "titan"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=CO-SSA-RSS-1-TIGR14-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.co-ssa-rss-1-tigr14-v1.0_kpza-j5gp",
-            "description": "The Cassini Radio Science Titan Gravity Science Experiment (TIGR14) Raw Data Archive is a time-ordered collection of radio science raw data acquired on April 3, 5, June 21 and 23, 2009, during he Cassini Extended Mission.",
-            "title": "CASSINI RSS RAW DATA SET - TIGR14 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "CASSINI RSS RAW DATA SET - TIGR14 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/GEWEXSRB/Rel4_1-IP_Longwave_3hrly_oceanonly_1",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/GEWEXSRB/Rel4_1-IP_Longwave_3hrly_oceanonly_1. https://doi.org/10.5067/GEWEXSRB/Rel4_1-IP_Longwave_3hrly_oceanonly_1.",
-            "issued": "2023-10-27",
-            "temporal": "2010-01-01T00:00:00Z/2017-06-30T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2017-06-30",
-            "keyword": [
-                "earth science",
-                "clouds",
-                "atmosphere",
-                "atmospheric radiation"
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
-            "identifier": "C2791459985-LARC_ASDC",
             "description": "GEWEXSRB_Rel4_1-IP_Longwave_3hrly_oceanonly is the Global Energy and Water Exchanges (GEWEX) Surface Radiation Budget (SRB) Integrated Product (Rel-4) Longwave 3-Hourly data product. It contains ocean-only global fields of 26 longwave surface, Top of Atmosphere (TOA), and atmospheric profile radiative parameters derived with the Longwave algorithm of the NASA World Climate Research Programme/Global Energy and Water-Cycle Experiment (WCRP/GEWEX) Surface Radiation Budget (SRB) Project. This version is an extension of Release 4-Integrated Product with ocean-only fluxes due to a missing key input from the main data set. The fluxes include all-sky, clear-sky, and pristine-sky TOA upward fluxes (outgoing longwave radiation, OLR), all-sky, clear-sky, and pristine-sky upward and downward fluxes at the tropopause, 200hPa, 500hPa, and surface. In addition to the fluxes, a day/night flag and a status flag of filled cloud properties are also included. Inputs to the longwave algorithm are cloud information based on ISCCP HXS, meteorology from ISCCP nnHIRS, SeaFlux SST and surface, and MERRA-2 conditionally. The temporal range is January 2010 through June 2017. Data collection for this product is complete.",
-            "graphic-preview-description": "Mission Logo",
-            "title": "GEWEX SRB Integrated Product (Rel-4_1) Longwave 3-Hourly Ocean-only Fluxes",
-            "graphic-preview-file": "https://asdc.larc.nasa.gov/static/images/project_logos/gewex-rfa.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGEWEXSRB%2FRel4_1-IP_Longwave_3hrly_oceanonly_1",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGEWEXSRB%2FRel4_1-IP_Longwave_3hrly_oceanonly_1",
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
-                    "downloadURL": "https://doi.org/10.5067/GEWEXSRB/Rel4_1-IP_Longwave_3hrly_oceanonly_1",
-                    "description": "DOI data set landing page for GEWEXSRB_Rel4-IP_Longwave_3hrly_oceanonly_1",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for GEWEXSRB_Rel4-IP_Longwave_3hrly_oceanonly_1",
+                    "downloadURL": "https://doi.org/10.5067/GEWEXSRB/Rel4_1-IP_Longwave_3hrly_oceanonly_1",
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
-                    "description": "SRB Rel4-IP ATBD",
                     "@type": "dcat:Distribution",
+                    "description": "SRB Rel4-IP ATBD",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/srb/SRB_Rel4-IP_ATBD.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's algorithm theoretical basis document"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/srb/SRB_Rel4-IP_Public_Release_Announcement.pdf",
-                    "description": "SRB Rel4-IP Public Release Announcement",
                     "@type": "dcat:Distribution",
+                    "description": "SRB Rel4-IP Public Release Announcement",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/srb/SRB_Rel4-IP_Public_Release_Announcement.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View an important notice for this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2791459985-LARC_ASDC",
-                    "description": "Earthdata Search for GEWEXSRB_Rel4_1-IP_Longwave_3hrly_oceanonly_1",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for GEWEXSRB_Rel4_1-IP_Longwave_3hrly_oceanonly_1",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2791459985-LARC_ASDC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://asdc.larc.nasa.gov/static/images/project_logos/gewex-rfa.png",
-                    "description": "Mission Logo",
                     "@type": "dcat:Distribution",
+                    "description": "Mission Logo",
+                    "downloadURL": "https://asdc.larc.nasa.gov/static/images/project_logos/gewex-rfa.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization through WORLDVIEW"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/SRB/GEWEXSRB_Rel4_1-IP/Longwave_3hrly_oceanonly_1/",
-                    "description": "ASDC Direct Data Download for GEWEXSRB_Rel4_1-IP_Longwave_3hrly_oceanonly_1",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for GEWEXSRB_Rel4_1-IP_Longwave_3hrly_oceanonly_1",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/SRB/GEWEXSRB_Rel4_1-IP/Longwave_3hrly_oceanonly_1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/SRB/GEWEXSRB_Rel4_1-IP/Longwave_3hrly_oceanonly_1/contents.html",
-                    "description": "OPeNDAP data access for GEWEXSRB_Rel4_1-IP_Longwave_3hrly_oceanonly_1",
                     "@type": "dcat:Distribution",
+                    "description": "OPeNDAP data access for GEWEXSRB_Rel4_1-IP_Longwave_3hrly_oceanonly_1",
+                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/SRB/GEWEXSRB_Rel4_1-IP/Longwave_3hrly_oceanonly_1/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 }
             ],
+            "graphic-preview-description": "Mission Logo",
+            "graphic-preview-file": "https://asdc.larc.nasa.gov/static/images/project_logos/gewex-rfa.png",
+            "identifier": "C2791459985-LARC_ASDC",
+            "issued": "2023-10-27",
+            "keyword": [
+                "earth science",
+                "clouds",
+                "atmosphere",
+                "atmospheric radiation"
+            ],
+            "landingPage": "https://doi.org/10.5067/GEWEXSRB/Rel4_1-IP_Longwave_3hrly_oceanonly_1",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2017-06-30",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/LARC/SD/ASDC"
+            },
             "spatial": "<?xml version=\"1.0\" encoding=\"UTF-8\"?><gml:Polygon xmlns:gml=\"http://www.opengis.net/gml/3.2\" srsName=\"EPSG:9825\"><gml:outerBoundaryIs><gml:LinearRing><gml:posList>-90.0 -180.0 -90.0 180.0 90.0 180.0 90.0 -180.0 -90.0 -180.0</gml:posList></gml:LinearRing></gml:outerBoundaryIs><gml:innerBoundaryIs></gml:innerBoundaryIs></gml:Polygon>",
+            "temporal": "2010-01-01T00:00:00Z/2017-06-30T23:59:59.999Z",
             "theme": [
                 "SRB",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "GEWEX SRB Integrated Product (Rel-4_1) Longwave 3-Hourly Ocean-only Fluxes"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=ULY-J-EPAC-4-SUMM-PSTL3-FLUX-1HR-V1.0",
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
+            "description": "This data set contains Ulysses Energetic Particle Composition Experiment (EPAC) 1 hour averaged sectored proton flux data from the Ulysses Jupiter encounter 1992-Jan-25 to 1992-Feb-28. These data were recorded by Proton Spectral Telescope 3 (PSTL3).",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.uly-j-epac-4-summ-pstl3-flux-1hr-v1.0_kq57-4b7h",
+            "issued": "2018-06-26",
+            "keyword": [
+                "jupiter",
+                "ulysses"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=ULY-J-EPAC-4-SUMM-PSTL3-FLUX-1HR-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.uly-j-epac-4-summ-pstl3-flux-1hr-v1.0_kq57-4b7h",
-            "description": "This data set contains Ulysses Energetic Particle Composition Experiment (EPAC) 1 hour averaged sectored proton flux data from the Ulysses Jupiter encounter 1992-Jan-25 to 1992-Feb-28. These data were recorded by Proton Spectral Telescope 3 (PSTL3).",
-            "title": "ULYSSES JUPITER EPAC PROTON SPECTRAL DATA 1 HR V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "ULYSSES JUPITER EPAC PROTON SPECTRAL DATA 1 HR V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/IMPACTS/PARSIVEL/DATA201",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Potter, Erin , Justin R. Minder and Massey  Bartolini.2022. UAlbany Parsivel IMPACTS [indicate subset used]. Dataset available online from the NASA Global Hydrometeorology Resource Center DAAC, Huntsville, Alabama, U.S.A. DOI: http://dx.doi.org/10.5067/IMPACTS/PARSIVEL/DATA201",
-            "issued": "2022-07-13",
-            "temporal": "2020-01-30T00:00:00Z/2022-02-28T23:59:50Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "keyword": [
-                "radar",
-                "spectral/engineering",
-                "atmosphere",
-                "atmospheric water vapor",
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
-            "identifier": "C2102858144-GHRC_DAAC",
             "description": "The UAlbany Parsivel IMPACTS dataset consists of precipitation data collected by a Parsivel2 disdrometer in support of the Investigation of Microphysics and Precipitation for Atlantic Coast-Threatening Snowstorms (IMPACTS) field campaign. IMPACTS was a three-year sequence of winter season deployments conducted to study snowstorms over the U.S Atlantic Coast (2020-2023). The campaign aimed to (1) Provide observations critical to understanding the mechanisms of snowband formation, organization, and evolution; (2) Examine how the microphysical characteristics and likely growth mechanisms of snow particles vary across snowbands; and (3) Improve snowfall remote sensing interpretation and modeling to significantly advance prediction capabilities. The Parsivel disdrometer data include particle size distribution, fall speed, radar reflectivity and precipitation rate. The dataset files are available in netCDF-4 format from 30 January 2020 through 28 February 2022.",
-            "title": "UAlbany Parsivel IMPACTS V1",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FIMPACTS%2FPARSIVEL%2FDATA201",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FIMPACTS%2FPARSIVEL%2FDATA201",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/portal/ghrc/search?q=ualbparsimpacts&ghrccloud%2Fdata%2F=",
-                    "description": "Files may be downloaded directly to your workstation from this link",
                     "@type": "dcat:Distribution",
+                    "description": "Files may be downloaded directly to your workstation from this link",
+                    "downloadURL": "https://search.earthdata.nasa.gov/portal/ghrc/search?q=ualbparsimpacts&ghrccloud%2Fdata%2F=",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.ott.com/download/ott-parsivel-white-paper/",
-                    "description": "OTT Parsivel - Enhanced precipitation identifier and new generation of present weather sensor by OTT Messtechnik, Germany",
                     "@type": "dcat:Distribution",
+                    "description": "OTT Parsivel - Enhanced precipitation identifier and new generation of present weather sensor by OTT Messtechnik, Germany",
+                    "downloadURL": "https://www.ott.com/download/ott-parsivel-white-paper/",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://gpm.nasa.gov/resources/documents/parsivel-laser-optical-disdrometer",
-                    "description": "Parsivel (Laser Optical) Disdrometer",
                     "@type": "dcat:Distribution",
+                    "description": "Parsivel (Laser Optical) Disdrometer",
+                    "downloadURL": "https://gpm.nasa.gov/resources/documents/parsivel-laser-optical-disdrometer",
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
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/impacts/UALB_Parsivel/doc/ualbparsimpacts_dataset.pdf",
-                    "description": "The guide document contains detailed information about the dataset",
                     "@type": "dcat:Distribution",
+                    "description": "The guide document contains detailed information about the dataset",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/impacts/UALB_Parsivel/doc/ualbparsimpacts_dataset.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
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
+            "identifier": "C2102858144-GHRC_DAAC",
+            "issued": "2022-07-13",
+            "keyword": [
+                "radar",
+                "spectral/engineering",
+                "atmosphere",
+                "atmospheric water vapor",
+                "clouds",
+                "earth science",
+                "precipitation"
+            ],
+            "landingPage": "https://doi.org/10.5067/IMPACTS/PARSIVEL/DATA201",
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
             "spatial": "-73.8419 42.6709 -73.8044 42.6957",
+            "temporal": "2020-01-30T00:00:00Z/2022-02-28T23:59:50Z",
             "theme": [
                 "IMPACTS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "UAlbany Parsivel IMPACTS V1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/MODIS/MCD43D22.061",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Crystal Schaaf, Zhuosen Wang. 2021-02-22. MODIS/Terra+Aqua BRDF/Albedo Parameter1 VIS Daily L3 Global 30ArcSec CMG V061. Sioux Falls, South Dakota, USA. Archived by National Aeronautics and Space Administration, U.S. Government, NASA EOSDIS Land Processes Distributed Active Archive Center. https://doi.org/10.5067/MODIS/MCD43D22.061. https://doi.org/10.5067/MODIS/MCD43D22.061. The DOI landing page provides citations in APA and Chicago styles..",
-            "issued": "2021-02-22",
-            "temporal": "2000-02-16T00:00:00Z/2024-05-20T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2021-02-22",
-            "keyword": [
-                "land surface",
-                "earth science",
-                "national geospatial data asset",
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
-            "identifier": "C2540268550-LPCLOUD",
-            "description": "The MCD43D22 Version 6.1 Bidirectional Reflectance Distribution Function and Albedo (BRDF/Albedo) Model Parameter dataset is produced daily using 16 days of Terra and Aqua Moderate Resolution Imaging Spectroradiometer (MODIS) data at 30 arc second (1,000 meter) resolution. Data are temporally weighted to the ninth day which is reflected in the Julian date in the file name. This Climate Modeling Grid (CMG) product covers the entire globe for use in climate simulation models. Due to the large file size, each MCD43D product contains just one data layer. Each of the three model parameters (isotropic, volumetric, and geometric) for each of the MODIS bands 1 through 7 and the visible, near infrared (NIR), and shortwave bands included in  MCD43C1 (https://doi.org/10.5067/MODIS/MCD43C1.061) are stored in a separate file as MCD43D01 through MCD43D30. \r\n\r\nMCD43D22 is the BRDF isotropic parameter for the MODIS visible broadband. The isotropic parameter, in conjunction with the volumetric and geometric parameters, is used to derive the BRDF/Albedo values for the MODIS visible broadband. \r\n\r\nImprovements/Changes from Previous Versions\r\n\r\n* The Version 6.1 Level-1B (L1B) products have been improved by undergoing various calibration changes that include: changes to the response-versus-scan angle (RVS) approach that affects reflectance bands for Aqua and Terra MODIS, corrections to adjust for the optical crosstalk in Terra MODIS infrared (IR) bands, and corrections to the Terra MODIS forward look-up table (LUT) update for the period 2012 - 2017.\r\n* A polarization correction has been applied to the L1B Reflective Solar Bands (RSB).",
-            "release-place": "Sioux Falls, South Dakota, USA",
             "creator": "Crystal Schaaf, Zhuosen Wang",
-            "title": "MODIS/Terra+Aqua BRDF/Albedo Parameter1 VIS Daily L3 Global 30ArcSec CMG V061",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The MCD43D22 Version 6.1 Bidirectional Reflectance Distribution Function and Albedo (BRDF/Albedo) Model Parameter dataset is produced daily using 16 days of Terra and Aqua Moderate Resolution Imaging Spectroradiometer (MODIS) data at 30 arc second (1,000 meter) resolution. Data are temporally weighted to the ninth day which is reflected in the Julian date in the file name. This Climate Modeling Grid (CMG) product covers the entire globe for use in climate simulation models. Due to the large file size, each MCD43D product contains just one data layer. Each of the three model parameters (isotropic, volumetric, and geometric) for each of the MODIS bands 1 through 7 and the visible, near infrared (NIR), and shortwave bands included in  MCD43C1 (https://doi.org/10.5067/MODIS/MCD43C1.061) are stored in a separate file as MCD43D01 through MCD43D30. \r\n\r\nMCD43D22 is the BRDF isotropic parameter for the MODIS visible broadband. The isotropic parameter, in conjunction with the volumetric and geometric parameters, is used to derive the BRDF/Albedo values for the MODIS visible broadband. \r\n\r\nImprovements/Changes from Previous Versions\r\n\r\n* The Version 6.1 Level-1B (L1B) products have been improved by undergoing various calibration changes that include: changes to the response-versus-scan angle (RVS) approach that affects reflectance bands for Aqua and Terra MODIS, corrections to adjust for the optical crosstalk in Terra MODIS infrared (IR) bands, and corrections to the Terra MODIS forward look-up table (LUT) update for the period 2012 - 2017.\r\n* A polarization correction has been applied to the L1B Reflective Solar Bands (RSB).",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMODIS%2FMCD43D22.061",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMODIS%2FMCD43D22.061",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "application/x-hdf",
-                    "downloadURL": "https://e4ftl01.cr.usgs.gov/MOTA/MCD43D22.061/",
-                    "description": "LP DAAC Data Pool provides direct access to available products via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "LP DAAC Data Pool provides direct access to available products via HTTPS.",
+                    "downloadURL": "https://e4ftl01.cr.usgs.gov/MOTA/MCD43D22.061/",
+                    "mediaType": "application/x-hdf",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "application/x-hdf",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=C2540268550-LPCLOUD",
-                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=C2540268550-LPCLOUD",
+                    "mediaType": "application/x-hdf",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/MODIS/MCD43D22.061",
-                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
+                    "downloadURL": "https://doi.org/10.5067/MODIS/MCD43D22.061",
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
-                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/filespec/MODIS/61/MCD43D22",
-                    "description": "The File Specification provides a description of the product file including Scientific Data Sets and their attributes.",
                     "@type": "dcat:Distribution",
+                    "description": "The File Specification provides a description of the product file including Scientific Data Sets and their attributes.",
+                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/filespec/MODIS/61/MCD43D22",
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
-                    "downloadURL": "https://opendap.cr.usgs.gov/opendap/hyrax/DP137/MOTA/MCD43D22.061/contents.html",
-                    "description": "Access data via Open-source Project for a Network Data Access Protocol",
                     "@type": "dcat:Distribution",
+                    "description": "Access data via Open-source Project for a Network Data Access Protocol",
+                    "downloadURL": "https://opendap.cr.usgs.gov/opendap/hyrax/DP137/MOTA/MCD43D22.061/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 }
             ],
+            "identifier": "C2540268550-LPCLOUD",
+            "issued": "2021-02-22",
+            "keyword": [
+                "land surface",
+                "earth science",
+                "national geospatial data asset",
+                "ngda",
+                "surface radiative properties"
+            ],
+            "landingPage": "https://doi.org/10.5067/MODIS/MCD43D22.061",
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
+            "title": "MODIS/Terra+Aqua BRDF/Albedo Parameter1 VIS Daily L3 Global 30ArcSec CMG V061"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-X-RSI-1%2F2%2F3-CR2-0022-V1.0",
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
-                "international rosetta mission"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This is a Solar Conjunction measurement covering the time 2006-03-29T00:27:38.500 to 2006-03-29T03:38:13.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-x-rsi-1-2-3-cr2-0022-v1.0_kqar-295c",
+            "issued": "2018-06-26",
+            "keyword": [
+                "sun",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-X-RSI-1%2F2%2F3-CR2-0022-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-x-rsi-1-2-3-cr2-0022-v1.0_kqar-295c",
-            "description": "This is a Solar Conjunction measurement covering the time 2006-03-29T00:27:38.500 to 2006-03-29T03:38:13.000.",
-            "title": "ROSETTA-ORBITER SUN RSI 1/2/3 CRUISE 2 0022 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "ROSETTA-ORBITER SUN RSI 1/2/3 CRUISE 2 0022 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-4-PRL-67P-M08-STRLIGHT-V1.0",
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
+            "description": "This CODMAC level 4 data set contains solar stray light corrected, radiometric calibrated and geometric distortion corrected (resampled) image data in W/m^2/sr/nm, acquired by the OSIRIS Wide Angle Camera on the Rosetta spacecraft during the PRELANDING mission phase, covering the period from 2014-09-23T10:00:00.000 to 2014-10-24T09:59:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V1.0 is the first version of this dataset: Lien corrected dataset after October 2018 PSA/PDS external peer review.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-4-prl-67p-m08-strlight-v1.0_kqjq-dpua",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-4-PRL-67P-M08-STRLIGHT-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-4-prl-67p-m08-strlight-v1.0_kqjq-dpua",
-            "description": "This CODMAC level 4 data set contains solar stray light corrected, radiometric calibrated and geometric distortion corrected (resampled) image data in W/m^2/sr/nm, acquired by the OSIRIS Wide Angle Camera on the Rosetta spacecraft during the PRELANDING mission phase, covering the period from 2014-09-23T10:00:00.000 to 2014-10-24T09:59:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V1.0 is the first version of this dataset: Lien corrected dataset after October 2018 PSA/PDS external peer review.",
-            "title": "ROSETTA-ORBITER 67P OSIWAC 4 PRL-MTP008 RDR-STRLIGHT V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P OSIWAC 4 PRL-MTP008 RDR-STRLIGHT V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC1-0633-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 1 phase 2014-11-20 to 2015-03-10. It is a Global Gravity measurement at the comet 67P and covers the time 2015-03-10T07:33:05.000 to 2015-03-10T09:28:00.500.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc1-0633-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC1-0633-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc1-0633-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 1 phase 2014-11-20 to 2015-03-10. It is a Global Gravity measurement at the comet 67P and covers the time 2015-03-10T07:33:05.000 to 2015-03-10T09:28:00.500.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 1 0633 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 1 0633 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/171",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Hall, F. G., K. F. Huemmrich, D. E. Strebel, S. J. Goetz, J. E. Nickeson, and K. D. Woods. 1996. NWS Daily Climatology Data: 1984 (SNF). [National Weather Service Daily Climatology Data: 1984 (Superior National Forest)]. Data set. Available on-line [http://www.daac.ornl.gov] from Oak Ridge National Laboratory Distributed Active Archive Center, Oak Ridge, Tennessee, U.S.A. Based on F. G. Hall, K. F. Huemmrich, D. E. Strebel, S. J. Goetz, J. E. Nickeson, and K. D. Woods, Biophysical, Morphological, Canopy Optical Property, and Productivity Data from the Superior National Forest, NASA Technical Memorandum 104568, National Aeronautics and Space Administration, Goddard Space Flight Center, Greenbelt, Maryland, U.S.A., 1992. doi:10.3334/ORNLDAAC/171",
-            "issued": "2024-03-01",
-            "temporal": "1984-01-01T00:00:00Z/1984-12-31T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-03-04",
-            "keyword": [
-                "atmospheric radiation",
-                "precipitation",
-                "atmospheric water vapor",
-                "earth science",
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
-            "identifier": "C2884978272-ORNL_CLOUD",
             "description": "Daily min, max, average temperature (F), precipitation (water equivalent in inches), and daily insolation (Langleys) for the Superior National Forest area as collected by NWS and U. of Minnesota",
-            "graphic-preview-description": "Browse Image",
-            "title": "NWS Daily Climatology Data: 1984 (SNF)",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/snf_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F171",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F171",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/snf/SNF_MET_1984/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/snf/SNF_MET_1984/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/SNF/guides/nws_daily_climate_1984.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/SNF/guides/nws_daily_climate_1984.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/171",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/171",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/snf/SNF_MET_1984/comp/met_1984.def",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/snf/SNF_MET_1984/comp/met_1984.def",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/snf/SNF_MET_1984/comp/met_1984.txt",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/snf/SNF_MET_1984/comp/met_1984.txt",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/snf/SNF_MET_1984/comp/nws_daily_climate_1984.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/snf/SNF_MET_1984/comp/nws_daily_climate_1984.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/snf/SNF_MET_1984/comp/nws_daily_climate_1984.txt",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/snf/SNF_MET_1984/comp/nws_daily_climate_1984.txt",
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
+            "identifier": "C2884978272-ORNL_CLOUD",
+            "issued": "2024-03-01",
+            "keyword": [
+                "atmospheric radiation",
+                "precipitation",
+                "atmospheric water vapor",
+                "earth science",
+                "atmospheric temperature",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/171",
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
+            "temporal": "1984-01-01T00:00:00Z/1984-12-31T23:59:59Z",
             "theme": [
                 "SNF",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "NWS Daily Climatology Data: 1984 (SNF)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.7927/H47W694W",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Wildlife Conservation Society - WCS, and Center for International Earth Science Information Network - CIESIN - Columbia University. 2002-12-31. Last of the Wild Project, Version 1, 2002 (LWP-1): Global Human Footprint Dataset (IGHP). Version 1.00. Palisades, NY. Archived by National Aeronautics and Space Administration, U.S. Government, NASA Socioeconomic Data and Applications Center (SEDAC). https://doi.org/10.7927/H47W694W. https://doi.org/10.7927/H47W694W. Sanderson, E. W., M. Jaiteh, M. A. Levy, K. H. Redford, A. V. Wannebo, and G. Woolmer. 2002. The Human Footprint and the Last of the Wild. BioScience 52 (10): 891-904. https://doi.org/10.1641/0006-3568(2002)052[0891:THFATL]2.0.CO;2.",
-            "issued": "2002-12-31",
-            "temporal": "1992-01-01T00:00:00Z/1995-12-31T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-10-12",
-            "references": [
-                "https://doi.org/10.7927/H4CN71V6",
-                "https://doi.org/10.7927/H4VM496V",
-                "https://doi.org/10.7927/H4QV3JG4",
-                "https://doi.org/10.7927/H4445JDG",
-                "https://doi.org/10.7927/H40C4SPR"
-            ],
-            "keyword": [
-                "earth science",
-                "biosphere",
-                "land use/land cover",
-                "land surface",
-                "ecosystems"
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
-            "identifier": "C179001935-SEDAC",
-            "description": "The Global Human Footprint Dataset of the Last of the Wild Project, Version 1, 2002 (LWP-1) is the Human Influence Index (HII) normalized by biome and realm. The HII is a global dataset of 1-kilometer grid cells, created from nine global data layers covering human population pressure (population density, population settlements), human land use and infrastructure (built up areas, nighttime lights, land use/land cover), and human access (coastlines, roads, railroads, navigable rivers). The dataset  in Interrupted Goode Homolosine Projection (IGHP) is produced by the Wildlife Conservation Society (WCS) and Columbia University Center for International Earth Science Information Network (CIESIN).",
-            "release-place": "Palisades, NY",
-            "graphic-preview-description": "Sample browse graphic of the data set.",
             "creator": "Wildlife Conservation Society - WCS, and Center for International Earth Science Information Network - CIESIN - Columbia University",
-            "title": "Last of the Wild Project, Version 1, 2002 (LWP-1): Global Human Footprint Dataset (IGHP)",
-            "graphic-preview-file": "https://sedac.ciesin.columbia.edu/downloads/maps/wildareas-v1/wildareas-v1-human-footprint-ighp/sedac-logo.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The Global Human Footprint Dataset of the Last of the Wild Project, Version 1, 2002 (LWP-1) is the Human Influence Index (HII) normalized by biome and realm. The HII is a global dataset of 1-kilometer grid cells, created from nine global data layers covering human population pressure (population density, population settlements), human land use and infrastructure (built up areas, nighttime lights, land use/land cover), and human access (coastlines, roads, railroads, navigable rivers). The dataset  in Interrupted Goode Homolosine Projection (IGHP) is produced by the Wildlife Conservation Society (WCS) and Columbia University Center for International Earth Science Information Network (CIESIN).",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.7927%2FH47W694W",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.7927%2FH47W694W",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/downloads/maps/wildareas-v1/wildareas-v1-human-footprint-ighp/sedac-logo.jpg",
-                    "description": "Sample browse graphic of the data set.",
                     "@type": "dcat:Distribution",
+                    "description": "Sample browse graphic of the data set.",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/downloads/maps/wildareas-v1/wildareas-v1-human-footprint-ighp/sedac-logo.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C179001935-SEDAC",
-                    "description": "Data Download Page",
                     "@type": "dcat:Distribution",
+                    "description": "Data Download Page",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C179001935-SEDAC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/downloads/docs-repo/wildareas-v1-human-footprint-ighp-readme.txt",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/downloads/docs-repo/wildareas-v1-human-footprint-ighp-readme.txt",
+                    "mediaType": "text/html",
                     "title": "View this dataset's read me document"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/downloads/docs-repo/wildareas-v1-human-footprint-ighp-citation2.txt",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/downloads/docs-repo/wildareas-v1-human-footprint-ighp-citation2.txt",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "graphic-preview-description": "Sample browse graphic of the data set.",
+            "graphic-preview-file": "https://sedac.ciesin.columbia.edu/downloads/maps/wildareas-v1/wildareas-v1-human-footprint-ighp/sedac-logo.jpg",
+            "identifier": "C179001935-SEDAC",
+            "issued": "2002-12-31",
+            "keyword": [
+                "earth science",
+                "biosphere",
+                "land use/land cover",
+                "land surface",
+                "ecosystems"
+            ],
+            "landingPage": "https://doi.org/10.7927/H47W694W",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2024-10-12",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "SEDAC"
+            },
+            "references": [
+                "https://doi.org/10.7927/H4CN71V6",
+                "https://doi.org/10.7927/H4VM496V",
+                "https://doi.org/10.7927/H4QV3JG4",
+                "https://doi.org/10.7927/H4445JDG",
+                "https://doi.org/10.7927/H40C4SPR"
+            ],
+            "release-place": "Palisades, NY",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "1992-01-01T00:00:00Z/1995-12-31T00:00:00Z",
             "theme": [
                 "LWP",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Last of the Wild Project, Version 1, 2002 (LWP-1): Global Human Footprint Dataset (IGHP)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5270/S5P-s4ljg54",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Copernicus Sentinel data processed by ESA, Koninklijk Nederlands Meteorologisch Instituut (KNMI). 2018-08-23. S5P_L2__NO2___. Version 1. Sentinel-5P TROPOMI Tropospheric NO2 1-Orbit L2 7km x 3.5km. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5270/S5P-s4ljg54. https://disc.gsfc.nasa.gov/datacollection/S5P_L2__NO2____1.html. Digital Science Data.",
-            "issued": "2017-05-05",
-            "temporal": "2018-04-30T00:41:24Z/2022-01-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2017-05-05",
-            "keyword": [
-                "atmosphere",
-                "atmospheric chemistry",
-                "earth science"
-            ],
-            "data-presentation-form": "Digital Science Data",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Pepijn Veefkind",
                 "hasEmail": "mailto:pepijn.veefkind@knmi.nl"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
-            "identifier": "C1442068511-GES_DISC",
-            "description": "Starting from August 6th in 2019, Sentinel-5P TROPOMI along-track high spatial resolution (~5.5km at nadir) has been implemented.\nFor data after August 6th of 2019, please check S5P_L2__NO2___ data collection.\n\nThe Copernicus Sentinel-5 Precursor (Sentinel-5P or S5P) satellite mission is one of the European Space Agency's (ESA) new mission family - Sentinels, and it is a joint initiative between the Kingdom of the Netherlands and the ESA. The sole payload on Sentinel-5P is the TROPOspheric Monitoring Instrument (TROPOMI), which is a nadir-viewing 108 degree Field-of-View push-broom grating hyperspectral spectrometer, covering the wavelength of ultraviolet-visible (UV-VIS, 270nm to 495nm), near infrared (NIR, 675nm to 775nm), and shortwave infrared (SWIR, 2305nm-2385nm). Sentinel-5P is the first of the Atmospheric Composition Sentinels and is expected to provide measurements of ozone, NO2, SO2, CH4, CO, formaldehyde, aerosols and cloud at high spatial, temporal and spectral resolutions.\n\nThe TROPOMI retrieval of total and tropospheric NO2, is based on the DOMINO approach, a DOAS retrieval, a pre-calculated air-mass factor (AMF) look-up table, and a data assimilation/chemistry transport model for the separation of the stratospheric and tropospheric contributions to the NO2 column. It also include many retrieval developments of the European Quality Assurance for Essential Climate Variables (QA4ECV) project.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "S5P_L2__NO2___",
             "creator": "Copernicus Sentinel data processed by ESA, Koninklijk Nederlands Meteorologisch Instituut (KNMI)",
-            "title": "Sentinel-5P TROPOMI Tropospheric NO2 1-Orbit L2 7km x 3.5km V1 (S5P_L2__NO2___) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/S5P_OFFL_L2__NO2____1.png",
-            "programCode": [
-                "026:001"
-            ],
+            "data-presentation-form": "Digital Science Data",
+            "description": "Starting from August 6th in 2019, Sentinel-5P TROPOMI along-track high spatial resolution (~5.5km at nadir) has been implemented.\nFor data after August 6th of 2019, please check S5P_L2__NO2___ data collection.\n\nThe Copernicus Sentinel-5 Precursor (Sentinel-5P or S5P) satellite mission is one of the European Space Agency's (ESA) new mission family - Sentinels, and it is a joint initiative between the Kingdom of the Netherlands and the ESA. The sole payload on Sentinel-5P is the TROPOspheric Monitoring Instrument (TROPOMI), which is a nadir-viewing 108 degree Field-of-View push-broom grating hyperspectral spectrometer, covering the wavelength of ultraviolet-visible (UV-VIS, 270nm to 495nm), near infrared (NIR, 675nm to 775nm), and shortwave infrared (SWIR, 2305nm-2385nm). Sentinel-5P is the first of the Atmospheric Composition Sentinels and is expected to provide measurements of ozone, NO2, SO2, CH4, CO, formaldehyde, aerosols and cloud at high spatial, temporal and spectral resolutions.\n\nThe TROPOMI retrieval of total and tropospheric NO2, is based on the DOMINO approach, a DOAS retrieval, a pre-calculated air-mass factor (AMF) look-up table, and a data assimilation/chemistry transport model for the separation of the stratospheric and tropospheric contributions to the NO2 column. It also include many retrieval developments of the European Quality Assurance for Essential Climate Variables (QA4ECV) project.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5270%2FS5P-s4ljg54",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5270%2FS5P-s4ljg54",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
@@ -1042982,772 +1042960,770 @@
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/S5P_L2__NO2____1.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/S5P_L2__NO2____1.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://tropomi.gesdisc.eosdis.nasa.gov/opendap/S5P_TROPOMI_Level2/S5P_L2__NO2___.1/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://tropomi.gesdisc.eosdis.nasa.gov/opendap/S5P_TROPOMI_Level2/S5P_L2__NO2___.1/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://tropomi.gesdisc.eosdis.nasa.gov/data/S5P_TROPOMI_Level2/S5P_L2__NO2___.1",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://tropomi.gesdisc.eosdis.nasa.gov/data/S5P_TROPOMI_Level2/S5P_L2__NO2___.1",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sentinel.esa.int/documents/247904/3541451/Sentinel-5P-Nitrogen-Dioxide-Level-2-Product-Readme-File",
-                    "description": "README Document",
                     "@type": "dcat:Distribution",
+                    "description": "README Document",
+                    "downloadURL": "https://sentinel.esa.int/documents/247904/3541451/Sentinel-5P-Nitrogen-Dioxide-Level-2-Product-Readme-File",
+                    "mediaType": "text/html",
                     "title": "View this dataset's read me document"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=S5P_L2__NO2____1",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=S5P_L2__NO2____1",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sentinel.esa.int/documents/247904/2476257/Sentinel-5P-TROPOMI-ATBD-NO2-data-products",
-                    "description": "Algorithm Theoretical Basis Document",
                     "@type": "dcat:Distribution",
+                    "description": "Algorithm Theoretical Basis Document",
+                    "downloadURL": "https://sentinel.esa.int/documents/247904/2476257/Sentinel-5P-TROPOMI-ATBD-NO2-data-products",
+                    "mediaType": "text/html",
                     "title": "View this dataset's algorithm theoretical basis document"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sentinel.esa.int/documents/247904/2474726/Sentinel-5P-Level-2-Product-User-Manual-Nitrogen-Dioxide",
-                    "description": "Product User Manual Document",
                     "@type": "dcat:Distribution",
+                    "description": "Product User Manual Document",
+                    "downloadURL": "https://sentinel.esa.int/documents/247904/2474726/Sentinel-5P-Level-2-Product-User-Manual-Nitrogen-Dioxide",
+                    "mediaType": "text/html",
                     "title": "View this dataset's user's guide"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sentinel.esa.int/web/sentinel/missions/sentinel-5p",
-                    "description": "ESA Copernicus Sentinal 5P Home Page",
                     "@type": "dcat:Distribution",
+                    "description": "ESA Copernicus Sentinal 5P Home Page",
+                    "downloadURL": "https://sentinel.esa.int/web/sentinel/missions/sentinel-5p",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/information/glossary?title=Sentinel-5P",
-                    "description": "S5P TROPOMI Data Collection Summary",
                     "@type": "dcat:Distribution",
+                    "description": "S5P TROPOMI Data Collection Summary",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/information/glossary?title=Sentinel-5P",
+                    "mediaType": "text/html",
                     "title": "View this dataset's product history"
                 }
             ],
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/S5P_OFFL_L2__NO2____1.png",
+            "identifier": "C1442068511-GES_DISC",
+            "issued": "2017-05-05",
+            "keyword": [
+                "atmosphere",
+                "atmospheric chemistry",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5270/S5P-s4ljg54",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2017-05-05",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
+            },
+            "release-place": "Greenbelt, MD, USA",
+            "series-name": "S5P_L2__NO2___",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2018-04-30T00:41:24Z/2022-01-17T00:00:00Z",
             "theme": [
                 "Sentinel-5P",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Sentinel-5P TROPOMI Tropospheric NO2 1-Orbit L2 7km x 3.5km V1 (S5P_L2__NO2___) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/SUOMI-NPP/VIIRS/L3M/PIC/2022",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/GSFC/SED/ESD/GCDC/OB.DAAC. https://doi.org/10.5067/SUOMI-NPP/VIIRS/L3M/PIC/2022.",
-            "issued": "2022-09-14",
-            "temporal": "2012-01-02T00:00:00Z/2023-02-28T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-09-14",
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
-            "identifier": "C2340494409-OB_DAAC",
             "description": "The Visible and Infrared Imager/Radiometer Suite (VIIRS) is a multi-disciplinary instrument that is being flown on the Joint Polar Satellite System (JPSS) series of spacecraft, including the Suomi National Polar-orbiting Partnership (S-NPP) that launched in October 2011.  JPSS is a multi-platform, multi-agency program that consolidates the polar orbiting spacecraft of NASA and the National Oceanic and Atmospheric Administration (NOAA).  S-NPP is the initial spacecraft in this series, and VIIRS is the successor to MODIS for Earth science data product generation.  VIIRS has 22 spectral bands ranging from 412 nm to 12 nm.  There are 16 moderate-resolution bands (750m at nadir), 5 image-resolution bands (375m), and one day-night band (DNB).",
-            "title": "Suomi-NPP VIIRS Global Mapped Particulate Inorganic Carbon (PIC) Data, version R2022.0",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSUOMI-NPP%2FVIIRS%2FL3M%2FPIC%2F2022",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSUOMI-NPP%2FVIIRS%2FL3M%2FPIC%2F2022",
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
-                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/data/10.5067/SUOMI-NPP/VIIRS/L3M/PIC/2022",
-                    "description": "VIIRS-Suomi-NPP L3M Particulate Inorganic Carbon (PIC) Dataset Landing Page",
                     "@type": "dcat:Distribution",
+                    "description": "VIIRS-Suomi-NPP L3M Particulate Inorganic Carbon (PIC) Dataset Landing Page",
+                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/data/10.5067/SUOMI-NPP/VIIRS/L3M/PIC/2022",
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
+            "identifier": "C2340494409-OB_DAAC",
+            "issued": "2022-09-14",
+            "keyword": [
+                "ocean chemistry",
+                "earth science",
+                "oceans"
+            ],
+            "landingPage": "https://doi.org/10.5067/SUOMI-NPP/VIIRS/L3M/PIC/2022",
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
+            "title": "Suomi-NPP VIIRS Global Mapped Particulate Inorganic Carbon (PIC) Data, version R2022.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC2-0677-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 2 phase 2015-03-11 to 2015-06-30. It is a Global Gravity measurement at the comet 67P and covers the time 2015-03-28T01:59:30.000 to 2015-03-28T06:39:10.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc2-0677-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC2-0677-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc2-0677-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 2 phase 2015-03-11 to 2015-06-30. It is a Global Gravity measurement at the comet 67P and covers the time 2015-03-28T01:59:30.000 to 2015-03-28T06:39:10.000.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 2 0677 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 2 0677 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-3-RDR-OCCULTATIONS-V4.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This data set is intended to include all reported timings of observed asteroid occultation events through Apr. 11, 2006, as well as asteroid occultation axes derived from those timings by David W. Dunham and David Herald. Some occultations by planetary satellites are also included.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-3-rdr-occultations-v4.0_kqwe-9rjx",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "asteroid",
                 "support archives",
                 "satellite",
                 "neptune"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-3-RDR-OCCULTATIONS-V4.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-3-rdr-occultations-v4.0_kqwe-9rjx",
-            "description": "This data set is intended to include all reported timings of observed asteroid occultation events through Apr. 11, 2006, as well as asteroid occultation axes derived from those timings by David W. Dunham and David Herald. Some occultations by planetary satellites are also included.",
-            "title": "ASTEROID OCCULTATIONS V4.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ASTEROID OCCULTATIONS V4.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.7927/H4R78C4K",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Center for International Earth Science Information Network - CIESIN - Columbia University and University of Puerto Rico - UPR - Rio Piedras. 2020-02-14. Latin America and the Caribbean Population Time Series. Version 1.00. Palisades, NY. Archived by National Aeronautics and Space Administration, U.S. Government, NASA Socioeconomic Data and Applications Center (SEDAC). https://doi.org/10.7927/H4R78C4K. https://doi.org/10.7927/H4R78C4K.",
-            "issued": "2020-02-14",
-            "temporal": "1990-01-01T00:00:00Z/2000-01-01T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-02-14",
-            "references": [
-                "https://doi.org/10.7927/H4MG7MF9"
-            ],
-            "keyword": [
-                "population",
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
-            "identifier": "C1701593248-SEDAC",
-            "description": "The Latin America and the Caribbean Population Time Series data set provides total population estimates using spatially consistent and comparable Units for Latin American municipalities or equivalent administrative Units for the years 1990 and 2000. The data set consists of two vector polygon layers: one layer displays population estimates for subnational administrative Units in 1990 and 2000, including population counts, density, and percent change, at the municipality level or equivalent (level 2); a second layer summarizes this information at the country level (level 0).",
-            "release-place": "Palisades, NY",
-            "graphic-preview-description": "Sample browse graphic of the data set.",
             "creator": "Center for International Earth Science Information Network - CIESIN - Columbia University and University of Puerto Rico - UPR - Rio Piedras",
-            "title": "Latin America and the Caribbean Population Time Series",
-            "graphic-preview-file": "https://sedac.ciesin.columbia.edu/downloads/maps/popdynamics/popdynamics-lac-pop-1990-2000/sedac-logo.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The Latin America and the Caribbean Population Time Series data set provides total population estimates using spatially consistent and comparable Units for Latin American municipalities or equivalent administrative Units for the years 1990 and 2000. The data set consists of two vector polygon layers: one layer displays population estimates for subnational administrative Units in 1990 and 2000, including population counts, density, and percent change, at the municipality level or equivalent (level 2); a second layer summarizes this information at the country level (level 0).",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.7927%2FH4R78C4K",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.7927%2FH4R78C4K",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/downloads/maps/popdynamics/popdynamics-lac-pop-1990-2000/sedac-logo.jpg",
-                    "description": "Sample browse graphic of the data set.",
                     "@type": "dcat:Distribution",
+                    "description": "Sample browse graphic of the data set.",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/downloads/maps/popdynamics/popdynamics-lac-pop-1990-2000/sedac-logo.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/popdynamics-lac-pop-1990-2000/data-download",
-                    "description": "Data Download Page",
                     "@type": "dcat:Distribution",
+                    "description": "Data Download Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/popdynamics-lac-pop-1990-2000/data-download",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://sedac.ciesin.columbia.edu/data/set/popdynamics-lac-pop-1990-2000/docs",
-                    "description": "Documentation Page",
                     "@type": "dcat:Distribution",
+                    "description": "Documentation Page",
+                    "downloadURL": "http://sedac.ciesin.columbia.edu/data/set/popdynamics-lac-pop-1990-2000/docs",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/popdynamics-lac-pop-1990-2000",
-                    "description": "Data Set\u00a0Overview Page",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set\u00a0Overview Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/popdynamics-lac-pop-1990-2000",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "graphic-preview-description": "Sample browse graphic of the data set.",
+            "graphic-preview-file": "https://sedac.ciesin.columbia.edu/downloads/maps/popdynamics/popdynamics-lac-pop-1990-2000/sedac-logo.jpg",
+            "identifier": "C1701593248-SEDAC",
+            "issued": "2020-02-14",
+            "keyword": [
+                "population",
+                "human dimensions",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.7927/H4R78C4K",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2020-02-14",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "SEDAC"
+            },
+            "references": [
+                "https://doi.org/10.7927/H4MG7MF9"
+            ],
+            "release-place": "Palisades, NY",
             "spatial": "-167.470568 -70.224737 25.441213 54.180542",
+            "temporal": "1990-01-01T00:00:00Z/2000-01-01T00:00:00Z",
             "theme": [
                 "POPDYNAMICS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Latin America and the Caribbean Population Time Series"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://c3.nasa.gov/dashlink/resources/159/",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2010-09-22",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
-            "keyword": [
-                "dashlink",
-                "nasa",
-                "ames"
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
-            "identifier": "DASHLINK_159",
             "description": "This paper describes the results of a significant research and development effort conducted at NASA Ames Research Center to develop new text mining algorithms to discover anomalies in free-text reports regarding system health and safety of two aerospace systems. We discuss two problems of significant import in the aviation industry. The first problem is that of automatic anomaly discovery concerning an aerospace system through the analysis of tens of thousands of free-text problem reports that are written about the system. The second problem that we address is that of automatic discovery of recurring anomalies, i.e., anomalies that may be described in different ways by different authors, at varying times and under varying conditions, but that are truly about the same part of the system. The intent of recurring anomaly identification is to determine project or system weakness or high-risk issues. The discovery of recurring anomalies is a key goal in building safe, reliable, and cost-effective aerospace systems.",
-            "title": "Discovery of Recurring Anomalies in Text Reports",
-            "programCode": [
-                "026:029"
-            ],
             "distribution": [
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/publication/IEEE_TextMiningPaper_vrs4_2.pdf",
-                    "description": "Paper",
                     "@type": "dcat:Distribution",
+                    "description": "Paper",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/publication/IEEE_TextMiningPaper_vrs4_2.pdf",
+                    "mediaType": "application/pdf",
                     "title": "IEEE_TextMiningPaper_vrs4.pdf"
                 }
             ],
-            "accrualPeriodicity": "irregular"
+            "identifier": "DASHLINK_159",
+            "issued": "2010-09-22",
+            "keyword": [
+                "dashlink",
+                "nasa",
+                "ames"
+            ],
+            "landingPage": "https://c3.nasa.gov/dashlink/resources/159/",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:029"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Dashlink"
+            },
+            "title": "Discovery of Recurring Anomalies in Text Reports"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=CO-S-RSS-1-SROC25-V1.0",
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
-                "saturn",
-                "cassini-huygens"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "The Cassini Radio Science Saturn Ring and Atmospheric Occultation experiments (SROC25) Raw Data Archive is a time-ordered collection of radio science raw data acquired on April 6, 20, and on May 28, 2017, during the Cassini Extended Extended Mission.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.co-s-rss-1-sroc25-v1.0_kqyz-8g2i",
+            "issued": "2018-09-05",
+            "keyword": [
+                "saturn",
+                "cassini-huygens"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=CO-S-RSS-1-SROC25-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.co-s-rss-1-sroc25-v1.0_kqyz-8g2i",
-            "description": "The Cassini Radio Science Saturn Ring and Atmospheric Occultation experiments (SROC25) Raw Data Archive is a time-ordered collection of radio science raw data acquired on April 6, 20, and on May 28, 2017, during the Cassini Extended Extended Mission.",
-            "title": "CASSINI RSS RAW DATA SET - SROC25 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "CASSINI RSS RAW DATA SET - SROC25 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC4-1199-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 4 phase 2015-10-22 to 2015-12-31. It is a Global Gravity measurement at the comet 67P and covers the time 2015-11-22T07:44:00.000 to 2015-11-22T16:41:41.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc4-1199-v1.0_kqzf-42dj",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC4-1199-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc4-1199-v1.0_kqzf-42dj",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 4 phase 2015-10-22 to 2015-12-31. It is a Global Gravity measurement at the comet 67P and covers the time 2015-11-22T07:44:00.000 to 2015-11-22T16:41:41.000.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 4 1199 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 4 1199 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=SDU-C-NAVCAM-2-EDR-WILD2-V2.0",
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
+            "description": "This data set contains raw pre-encounter and encounter images taken by the Stardust Navigation Camera during the encounter with comet Wild 2.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.sdu-c-navcam-2-edr-wild2-v2.0_kqzw-kt7b",
+            "issued": "2021-05-21",
+            "keyword": [
+                "81p/wild 2 (1978 a2)",
+                "stardust"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=SDU-C-NAVCAM-2-EDR-WILD2-V2.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.sdu-c-navcam-2-edr-wild2-v2.0_kqzw-kt7b",
-            "description": "This data set contains raw pre-encounter and encounter images taken by the Stardust Navigation Camera during the encounter with comet Wild 2.",
-            "title": "STARDUST NAVCAM IMAGES OF WILD 2 - VERSION 2.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "STARDUST NAVCAM IMAGES OF WILD 2 - VERSION 2.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/TERRA/MOPITT/MOP03J_L3.008",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2000-03-03. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/TERRA/MOPITT/MOP03J_L3.008. https://asdc.larc.nasa.gov/project/MOPITT.",
-            "issued": "2018-10-26",
-            "temporal": "2000-03-03T00:00:00Z/2022-01-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2019-06-19",
-            "keyword": [
-                "atmospheric chemistry",
-                "air quality",
-                "atmosphere",
-                "earth science",
-                "atmospheric water vapor",
-                "atmospheric temperature",
-                "atmospheric pressure"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "DALLAS MASTERS",
                 "hasEmail": "mailto:mastersd@ucar.edu"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/LARC/SD/ASDC"
-            },
-            "identifier": "C1575974131-LARC",
             "description": "MOP03J_8 is the Measurements Of Pollution In The Troposphere (MOPITT) Carbon Monoxide (CO) gridded daily means (Near and Thermal Infrared Radiances) version 8 data product. It contains daily mean gridded versions of the daily Level 2 CO profile and total column retrievals. For this data product, the averaging kernels associated with each retrieval are also gridded and included in the Level 3 files. For a description of the file contents, refer to the File Spec Document. The MOPITT Level 2 Data Quality Statement contains additional information about the quality and the limitations of the retrievals. MOPITT was successfully launched into sun-synchronous polar orbit aboard Terra, NASA's first Earth Observing System spacecraft, on December 18, 1999. The MOPITT instrument was constructed by a consortium of Canadian companies and funded by the Space Science Division of the Canadian Space Agency. Data collection for this product was completed in March of 2020.",
-            "title": "MOPITT CO gridded daily means (Near and Thermal Infrared Radiances) V008",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FTERRA%2FMOPITT%2FMOP03J_L3.008",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FTERRA%2FMOPITT%2FMOP03J_L3.008",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1575974131-LARC",
-                    "description": "Earthdata Search for MOP03J_8 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for MOP03J_8 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1575974131-LARC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
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
-                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/MOPITT/MOP03J.008/contents.html",
-                    "description": "OPeNDAP data access for MOP03J_8",
                     "@type": "dcat:Distribution",
+                    "description": "OPeNDAP data access for MOP03J_8",
+                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/MOPITT/MOP03J.008/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://www2.acom.ucar.edu/sites/default/files/mopitt/v8_users_guide_201812.pdf",
-                    "description": "MOPITT Version 8 Product User's Guide - December 2018",
                     "@type": "dcat:Distribution",
+                    "description": "MOPITT Version 8 Product User's Guide - December 2018",
+                    "downloadURL": "https://www2.acom.ucar.edu/sites/default/files/mopitt/v8_users_guide_201812.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/TERRA/MOPITT/MOP03J_L3.008",
-                    "description": "DOI data set landing page for MOP03J_8",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for MOP03J_8",
+                    "downloadURL": "https://doi.org/10.5067/TERRA/MOPITT/MOP03J_L3.008",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
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
-                    "downloadURL": "https://subset.larc.nasa.gov/mopitt/",
-                    "description": "MOPITT Search and Subsetting Web Application",
                     "@type": "dcat:Distribution",
+                    "description": "MOPITT Search and Subsetting Web Application",
+                    "downloadURL": "https://subset.larc.nasa.gov/mopitt/",
+                    "mediaType": "text/html",
                     "title": "Subset this dataset using a web based subsetter"
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
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/MOPITT/MOP03J.008/",
-                    "description": "ASDC Direct Data Download for MOP03J_8",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for MOP03J_8",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/MOPITT/MOP03J.008/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
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
-                    "downloadURL": "https://www.pnas.org/content/115/20/5099",
-                    "description": "Proceedings of the National Academy of Sciences (PNAS) Article: Unexpected slowdown of US pollutant emission reduction in the past decade\u00a0(Ground and satellite observations show that air pollution regulations in the United States (US) have resulted in substantial reductions in emissions and corresponding improvements in air quality over the last several decades)",
                     "@type": "dcat:Distribution",
+                    "description": "Proceedings of the National Academy of Sciences (PNAS) Article: Unexpected slowdown of US pollutant emission reduction in the past decade\u00a0(Ground and satellite observations show that air pollution regulations in the United States (US) have resulted in substantial reductions in emissions and corresponding improvements in air quality over the last several decades)",
+                    "downloadURL": "https://www.pnas.org/content/115/20/5099",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/mopitt/quality_summaries/MOPV8_L3_DQ_statement.pdf",
-                    "description": "Quality Summary: MOPITT Level 3, Version 8 (V8; L3V5.6.x), first released December, 2018",
                     "@type": "dcat:Distribution",
+                    "description": "Quality Summary: MOPITT Level 3, Version 8 (V8; L3V5.6.x), first released December, 2018",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/mopitt/quality_summaries/MOPV8_L3_DQ_statement.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's data quality document"
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
                 }
             ],
+            "identifier": "C1575974131-LARC",
+            "issued": "2018-10-26",
+            "keyword": [
+                "atmospheric chemistry",
+                "air quality",
+                "atmosphere",
+                "earth science",
+                "atmospheric water vapor",
+                "atmospheric temperature",
+                "atmospheric pressure"
+            ],
+            "landingPage": "https://doi.org/10.5067/TERRA/MOPITT/MOP03J_L3.008",
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
+            "temporal": "2000-03-03T00:00:00Z/2022-01-17T00:00:00Z",
             "theme": [
                 "MOPITT",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "MOPITT CO gridded daily means (Near and Thermal Infrared Radiances) V008"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1237114211-GES_DISC.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "TOMS Science Team. TOMSN7L2. Version 008. TOMS Nimbus-7 Ozone (O3) Total Column 1-Orbit L2 Swath 50 km x 50 km V008. Greenbelt, MD. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://disc.gsfc.nasa.gov/datacollection/TOMSN7L2_008.html. Digital Science Data.",
-            "issued": "2004-04-30",
-            "temporal": "1978-11-01T00:00:00Z/1993-05-06T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2004-04-30",
-            "keyword": [
-                "aerosols",
-                "earth science",
-                "atmospheric radiation",
-                "atmospheric chemistry",
-                "atmosphere"
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
-            "identifier": "C1237114211-GES_DISC",
-            "description": "The Nimbus-7 Total Ozone Mapping Spectrometer (TOMS) version 8 orbital swath data product contains total column ozone, UV aerosol index, and Lambertian effective surface reflectivity (Rayleigh corrected) at approximately 50x50 km2 resolution (at nadir). This product also contains some auxiliary derived and ancillary parameters including N-values, SO2 index, cloud fraction, cloud pressure, ozone below clouds, terrain height, geolocation, solar and satellite viewing angles, and data quality flags. These data are stored in the version 5 EOS Hierarchical Data Format (HDF-EOS5).\n\nThe TOMS data were produced by the Laboratory for Atmospheres at NASA Goddard Space Flight Center (Code 614).",
-            "release-place": "Greenbelt, MD",
-            "series-name": "TOMSN7L2",
             "creator": "TOMS Science Team",
-            "title": "TOMS Nimbus-7 Ozone (O3) Total Column 1-Orbit L2 Swath 50 km x 50 km V008 (TOMSN7L2) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/TOMSN7L2_008.png",
-            "programCode": [
-                "026:001"
-            ],
+            "data-presentation-form": "Digital Science Data",
+            "description": "The Nimbus-7 Total Ozone Mapping Spectrometer (TOMS) version 8 orbital swath data product contains total column ozone, UV aerosol index, and Lambertian effective surface reflectivity (Rayleigh corrected) at approximately 50x50 km2 resolution (at nadir). This product also contains some auxiliary derived and ancillary parameters including N-values, SO2 index, cloud fraction, cloud pressure, ozone below clouds, terrain height, geolocation, solar and satellite viewing angles, and data quality flags. These data are stored in the version 5 EOS Hierarchical Data Format (HDF-EOS5).\n\nThe TOMS data were produced by the Laboratory for Atmospheres at NASA Goddard Space Flight Center (Code 614).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -1043756,195 +1043732,231 @@
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/TOMSN7L2_008.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/TOMSN7L2_008.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/Nimbus_7_TOMS_Level2/TOMSN7L2/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/Nimbus_7_TOMS_Level2/TOMSN7L2/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=TOMSN7L2",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=TOMSN7L2",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TOMS/NIMBUS7_USERGUIDE.PDF",
-                    "description": "Nimbus-7 TOMS Data Product User's Guide.",
                     "@type": "dcat:Distribution",
+                    "description": "Nimbus-7 TOMS Data Product User's Guide.",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TOMS/NIMBUS7_USERGUIDE.PDF",
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
                 }
             ],
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/TOMSN7L2_008.png",
+            "identifier": "C1237114211-GES_DISC",
+            "issued": "2004-04-30",
+            "keyword": [
+                "aerosols",
+                "earth science",
+                "atmospheric radiation",
+                "atmospheric chemistry",
+                "atmosphere"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1237114211-GES_DISC.html",
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
+            "series-name": "TOMSN7L2",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "1978-11-01T00:00:00Z/1993-05-06T23:59:59.999Z",
             "theme": [
                 "TOMS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "TOMS Nimbus-7 Ozone (O3) Total Column 1-Orbit L2 Swath 50 km x 50 km V008 (TOMSN7L2) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1386206873-NSIDCV0.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Ground temperatures in ice-cemented ground at Linnaeus Terrace, Dry Valleys, Antarctica, Version 1. Version 1. Archived by National Aeronautics and Space Administration, U.S. Government, National Snow and Ice Data Center.",
-            "issued": "1994-01-01",
-            "temporal": "1994-01-01T00:00:00Z/1994-12-31T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "1994-12-31",
-            "keyword": [
-                "cryosphere",
-                "earth science",
-                "frozen ground",
-                "land surface"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Christopher McKay",
                 "hasEmail": "mailto:chris.mckay@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NSIDC"
-            },
-            "identifier": "C1386206873-NSIDCV0",
             "description": "Soil temperatures were measured with Campbell 107 soil thermistors. Thermistors were placed at 0, 17, 23 (just above the ice-cemented permafrost) and 40 cm depth. To emplace the sensors, first a soil pit was dug to the level of ice-cemented permafrost. Then a hammer drill was used to make a narrow, 15 cm deep hole into the ice-cemented ground. The thermistor was placed into the drill hole. This procedure caused minimal disturbance to the ice-cemented ground. Air temperature and humidity were measured with a Campbell 207 air probe. The temperature on the surface of an outcrop of Beacon sandstone was measured with a T-type thermocouple. Sunlight was measured with a LiCor 200 pyranometer. The sensors were deployed during Jan 1993 but (due to equipment failure) data storage began only on 6 Jan 1994 and was continued until 16 Jan 1995. All temperature sensors were removed after the data collection interval and calibrated in the laboratory. Calibrations were applied using the Steinhart and Hart (1968) representations for the temperature dependence of the thermistor resistance. This was necessary since the instrumental calibration for the 107 thermistor provided by Campbell did not extend below -40C. After correction, the error in the temperature measurement is estimated to be less than 0.2 C and error in the humidity measurement was Campbell 207 RH sensor has high errors for relative humidity values below 15% --- tending to systematically overestimate values by more than 10% humidity. The error in the averaged light measurement is less than 10 W/m2.  All sensors were sampled once every 10 minutes and averages of three measurements were written to final memory every 30 minutes corresponding to 48 recordings each day.   \n\nData are stored in columns of ASCII data; entries are \n1. Digital day of year in 1994 \n 2. Air temperature \n3. Air relative humidity \n4. Sunlight, W/m2 \n5. Soil surface temperature \n4. Sunlight, W/m2 \n5. Soil surface temperature \n6. Temperature at 17 cm depth \n7. Temperature at 23 cm depth \n8. Temperature at 40 cm depth \n9. Temperature on surface of rock \n\nData are presented on the CAPS Version 1.0 CD-ROM, June 1998.",
-            "title": "Ground temperatures in ice-cemented ground at Linnaeus Terrace, Dry Valleys, Antarctica, Version 1",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/forms/GGD6_or.html?major_version=1",
-                    "description": "Direct download, with optional registration page.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download, with optional registration page.",
+                    "downloadURL": "https://nsidc.org/forms/GGD6_or.html?major_version=1",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/data/GGD6/versions/1",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://nsidc.org/data/GGD6/versions/1",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/data/GGD6/versions/1",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://nsidc.org/data/GGD6/versions/1",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C1386206873-NSIDCV0",
+            "issued": "1994-01-01",
+            "keyword": [
+                "cryosphere",
+                "earth science",
+                "frozen ground",
+                "land surface"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1386206873-NSIDCV0.html",
+            "language": [
+                "en-US"
+            ],
+            "modified": "1994-12-31",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NSIDC"
+            },
             "spatial": "161.083 -77.6 161.083 -77.6",
+            "temporal": "1994-01-01T00:00:00Z/1994-12-31T23:59:59.999Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Ground temperatures in ice-cemented ground at Linnaeus Terrace, Dry Valleys, Antarctica, Version 1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/SENTINEL-3A/OLCI/L3M/ERR/CHL/2022",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/GSFC/SED/ESD/GCDC/OB.DAAC. https://doi.org/10.5067/SENTINEL-3A/OLCI/L3M/ERR/CHL/2022.",
-            "issued": "2022-09-13",
-            "temporal": "2016-04-25T00:00:00Z/2024-04-22T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-04-13",
-            "keyword": [
-                "ocean optics",
-                "atmospheric radiation",
-                "earth science",
-                "oceans",
-                "atmosphere"
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
-            "identifier": "C2264534423-OB_DAAC",
             "description": "The Ocean and Land Colour Instrument (OLCI) is the successor to ENVISAT's Medium Resolution Imaging Spectrometer (MERIS) having additional spectral channels, different camera arrangements and simplified on-board processing. The OLCI is a push-broom instrument with five camera modules sharing the field of view. The field of view of the five cameras is arranged in a fan-shaped configuration in the vertical plane, perpendicular to the platform velocity. Each camera has an individual field of view of 14.2\u00b0 and a 0.6\u00b0 overlap with its neighbors. The whole field of view is shifted across track by 12.6\u00b0 away from the sun to minimize the impact of sun glint. OLCI is equipped with on-board calibration hardware based on sun diffusers. There are three sun diffusers--two 'white' diffusers dedicated to radiometric calibration and one dedicated to spectral calibration, with spectral reflectance features. The native resolution is approximately 300m, refered to as Full Resolution (FR). A Reduced Resolution (RR) processing mode provides Level-1B data at sampling rates decreased by a factor of four in both spatial dimensions resulting to resolution of approximately 1.2 km.",
-            "title": "Sentinel-3A OLCI Level-3M Global Mapped Earth-observation Reduced Resolution (ERR) Chlorophyll (CHL) Data, version R2022.0",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSENTINEL-3A%2FOLCI%2FL3M%2FERR%2FCHL%2F2022",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSENTINEL-3A%2FOLCI%2FL3M%2FERR%2FCHL%2F2022",
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
+            "identifier": "C2264534423-OB_DAAC",
+            "issued": "2022-09-13",
+            "keyword": [
+                "ocean optics",
+                "atmospheric radiation",
+                "earth science",
+                "oceans",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.5067/SENTINEL-3A/OLCI/L3M/ERR/CHL/2022",
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
+            "title": "Sentinel-3A OLCI Level-3M Global Mapped Earth-observation Reduced Resolution (ERR) Chlorophyll (CHL) Data, version R2022.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1243129847-ASF.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, ASF.",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "undefined",
+                "hasEmail": "mailto:uso@asf.alaska.edu"
+            },
+            "description": "SMAP Level 1B Sigma Naught Low Res Data Quality Info Version 3",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "Vertex, the ASF search and download interface",
+                    "downloadURL": "https://vertex.daac.asf.alaska.edu/",
+                    "mediaType": "text/html",
+                    "title": "Download this dataset"
+                }
+            ],
+            "identifier": "C1243129847-ASF",
             "issued": "2015-07-31",
-            "temporal": "2015-02-12T16:02:58Z/2022-01-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2016-05-07",
             "keyword": [
                 "platform characteristics",
                 "smap",
@@ -1043957,638 +1043969,635 @@
                 "imaging radars",
                 "nasa decadal survey"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "undefined",
-                "hasEmail": "mailto:uso@asf.alaska.edu"
-            },
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1243129847-ASF.html",
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
-            "identifier": "C1243129847-ASF",
-            "description": "SMAP Level 1B Sigma Naught Low Res Data Quality Info Version 3",
-            "title": "SMAP_L1B_SIGMA_NAUGHT_LOW_RES_QA_V003",
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
+            "title": "SMAP_L1B_SIGMA_NAUGHT_LOW_RES_QA_V003"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RPCLAP-5-PRL-DERIV2-V1.0",
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
+            "description": "This data set contains DERIVED\ndata from Rosetta RPC-LAP, acquired during the PRELANDING mission phase\nwhere the primary target was the comet 67P/CHURYUMOV-GERASIMENKO 1 (1969\nR1). It contains high-level data products in physical units, such as\nelectron density, electron temperature, spacecraft potential, and\ndownsampled time series of current and voltage measurements.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rpclap-5-prl-deriv2-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RPCLAP-5-PRL-DERIV2-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rpclap-5-prl-deriv2-v1.0",
-            "description": "This data set contains DERIVED\ndata from Rosetta RPC-LAP, acquired during the PRELANDING mission phase\nwhere the primary target was the comet 67P/CHURYUMOV-GERASIMENKO 1 (1969\nR1). It contains high-level data products in physical units, such as\nelectron density, electron temperature, spacecraft potential, and\ndownsampled time series of current and voltage measurements.",
-            "title": "ROSETTA-ORBITER 67P RPCLAP 5\nPRL DERIV2 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RPCLAP 5\nPRL DERIV2 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MSL-M-DAN-3%2F4-RDR-V1.0",
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
-                "mars science laboratory"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "Reduced housekeeping and scientific data collected from the Dynamic Albedo of Neutron Detector (DAN) aboard the Mars Science Laboratory.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.msl-m-dan-3-4-rdr-v1.0_krbu-rt64",
+            "issued": "2018-06-26",
+            "keyword": [
+                "mars",
+                "mars science laboratory"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MSL-M-DAN-3%2F4-RDR-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.msl-m-dan-3-4-rdr-v1.0_krbu-rt64",
-            "description": "Reduced housekeeping and scientific data collected from the Dynamic Albedo of Neutron Detector (DAN) aboard the Mars Science Laboratory.",
-            "title": "MSL DYNAMIC ALBEDO OF NEUTRONS LEVEL 3/4 RDR V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "MSL DYNAMIC ALBEDO OF NEUTRONS LEVEL 3/4 RDR V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=GO-CAL-PPR-2-EDR-VENUS-CALIBRATION-V1.0",
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
-                "galileo"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "added ARCHIVE_STATUS, ,This data set contains the R_EDR data for the Galileo Orbiter PPR instrument for the period corresponding to the Venus encounter observations in February 1990.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.go-cal-ppr-2-edr-venus-calibration-v1.0_krbx-i6rm",
+            "issued": "2018-06-26",
+            "keyword": [
+                "venus",
+                "galileo"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=GO-CAL-PPR-2-EDR-VENUS-CALIBRATION-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.go-cal-ppr-2-edr-venus-calibration-v1.0_krbx-i6rm",
-            "description": "added ARCHIVE_STATUS, ,This data set contains the R_EDR data for the Galileo Orbiter PPR instrument for the period corresponding to the Venus encounter observations in February 1990.",
-            "title": "GLL PPR VENUS ENCOUNTER EDR",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "GLL PPR VENUS ENCOUNTER EDR"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/VIIRS/VJ102DNB_NRT.021",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "VCST Team. 2022-01-27. VIIRS/JPSS1 Day/Night Band 6-Min L1B Swath 750m NRT. Version 2.1. MODAPS at NASA/GSFC. Archived by National Aeronautics and Space Administration, U.S. Government, LANCEMODIS. https://doi.org/10.5067/VIIRS/VJ102DNB_NRT.021. https://doi.org/10.5067/VIIRS/VJ102DNB_NRT.021.",
-            "issued": "2022-01-01",
-            "temporal": "2022-01-01T00:00:00Z/2023-03-01T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-01-28",
-            "keyword": [
-                "visible wavelengths",
-                "infrared wavelengths",
-                "earth science",
-                "spectral/engineering"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Vincent Chiang",
                 "hasEmail": "mailto:kwo-fu.chiang@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Not provided"
-            },
-            "identifier": "C2208780589-LANCEMODIS",
-            "description": "The VIIRS/JPSS1 Day/Night Band 6-Min L1B Swath 750m Near Real Time (NRT) product, short-name VJ102DNB_NRT is one of the VIIRS Level 1 and Level 2 swath products that are generated from the processing of 6 minutes of VIIRS data acquired during the Joint Polar Satellite System - 1 (JPSS1) satellite overpass. The Day/Night band (DNB) is a panchromatic channel covering the wavelengths from 500 nm to 900 nm, and sensitive to visible and near-infrared from daylight down to the low-level radiation observed at night.\r\n\r\nThe VIIRS DNB is much improved from previous products due in large part to its complicated continuous on-board calibration. In addition, new-moon Earth observations are used to estimate and remove stray light. These corrections are a first of its kind to provide on-orbit radiometric calibration. The corrections made to the DNB data are provided by the NASA VIIRS Characterization Support Team and are likely to continue to evolve given this new methodology.\r\n\r\nThe spatial resolution of the instrument at viewing nadir is approximately 750 m for the DNB and the Moderate-resolution Bands and and 375m for the Imagery bands. The DNB is aggregated to maintain nearly constant horizontal spatial resolution across the swath.\r\n\r\nAs the DNB is sensitive to nighttime radiation over the full lunar cycle, the incoming solar and lunar radiation must be properly modeled to calculate the reflectance. However, the DNB is sensitive to more sources of radiation than just the sun and moon.",
-            "release-place": "MODAPS at NASA/GSFC",
             "creator": "VCST Team",
-            "title": "VIIRS/JPSS1 Day/Night Band 6 Min L1B Swath 750m NRT",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The VIIRS/JPSS1 Day/Night Band 6-Min L1B Swath 750m Near Real Time (NRT) product, short-name VJ102DNB_NRT is one of the VIIRS Level 1 and Level 2 swath products that are generated from the processing of 6 minutes of VIIRS data acquired during the Joint Polar Satellite System - 1 (JPSS1) satellite overpass. The Day/Night band (DNB) is a panchromatic channel covering the wavelengths from 500 nm to 900 nm, and sensitive to visible and near-infrared from daylight down to the low-level radiation observed at night.\r\n\r\nThe VIIRS DNB is much improved from previous products due in large part to its complicated continuous on-board calibration. In addition, new-moon Earth observations are used to estimate and remove stray light. These corrections are a first of its kind to provide on-orbit radiometric calibration. The corrections made to the DNB data are provided by the NASA VIIRS Characterization Support Team and are likely to continue to evolve given this new methodology.\r\n\r\nThe spatial resolution of the instrument at viewing nadir is approximately 750 m for the DNB and the Moderate-resolution Bands and and 375m for the Imagery bands. The DNB is aggregated to maintain nearly constant horizontal spatial resolution across the swath.\r\n\r\nAs the DNB is sensitive to nighttime radiation over the full lunar cycle, the incoming solar and lunar radiation must be properly modeled to calculate the reflectance. However, the DNB is sensitive to more sources of radiation than just the sun and moon.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FVIIRS%2FVJ102DNB_NRT.021",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FVIIRS%2FVJ102DNB_NRT.021",
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
-                    "downloadURL": "https://nrt3.modaps.eosdis.nasa.gov/archive/allData/5200/VJ102DNB_NRT/",
-                    "description": "Direct access to data from MODAPS public site.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct access to data from MODAPS public site.",
+                    "downloadURL": "https://nrt3.modaps.eosdis.nasa.gov/archive/allData/5200/VJ102DNB_NRT/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 }
             ],
+            "identifier": "C2208780589-LANCEMODIS",
+            "issued": "2022-01-01",
+            "keyword": [
+                "visible wavelengths",
+                "infrared wavelengths",
+                "earth science",
+                "spectral/engineering"
+            ],
+            "landingPage": "https://doi.org/10.5067/VIIRS/VJ102DNB_NRT.021",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2022-01-28",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Not provided"
+            },
+            "release-place": "MODAPS at NASA/GSFC",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2022-01-01T00:00:00Z/2023-03-01T00:00:00Z",
             "theme": [
                 "JPSS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "VIIRS/JPSS1 Day/Night Band 6 Min L1B Swath 750m NRT"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC1-0468-V1.0",
-            "bureauCode": [
-                "026:00"
-            ],
-            "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2021-05-21",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
-            "keyword": [
-                "international rosetta mission",
-                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "026:00"
             ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 1 phase 2014-11-20 to 2015-03-10. It is a Global Gravity measurement at the comet 67P and covers the time 2014-12-01T02:33:05.000 to 2014-12-01T13:04:03.500.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc1-0468-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC1-0468-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc1-0468-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 1 phase 2014-11-20 to 2015-03-10. It is a Global Gravity measurement at the comet 67P and covers the time 2014-12-01T02:33:05.000 to 2014-12-01T13:04:03.500.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 1 0468 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 1 0468 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MER2-M-HAZCAM-5-XYZ-OPS-V1.0",
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
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mer2-m-hazcam-5-xyz-ops-v1.0_krfq-ywj9",
+            "issued": "2018-06-26",
+            "keyword": [
+                "mars",
+                "mars exploration rover"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MER2-M-HAZCAM-5-XYZ-OPS-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mer2-m-hazcam-5-xyz-ops-v1.0_krfq-ywj9",
-            "description": "not applicable",
-            "title": "MER 2 MARS HAZARD AVOID CAMERA XYZ RDR OPS V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "MER 2 MARS HAZARD AVOID CAMERA XYZ RDR OPS V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/GNSS/GNSS_HOURLY_I_001",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "International GNSS Service, Hourly 30-second IRNSS broadcast ephemeris data, Greenbelt, MD, USA:NASA Crustal Dynamics Data Information System (CDDIS), Accessed [[enter user data access date]] at doi:10.5067/GNSS/gnss_hourly_i_001",
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
-            "identifier": "C1605632902-CDDIS",
             "description": "This dataset consists of ground-based Global Navigation Satellite System (GNSS) Indian Regional Navigation Satellite System (IRNSS) Broadcast Ephemeris Data (hourly files) from the NASA Crustal Dynamics Data Information System (CDDIS). GNSS provide autonomous geo-spatial positioning with global coverage. GNSS data sets from ground receivers at the CDDIS consist primarily of the data from the U.S. Global Positioning System (GPS) and the Russian GLONASS. Since 2011, the CDDIS GNSS archive includes data from other GNSS (Europe\u2019s Galileo, China\u2019s Beidou, Japan\u2019s Quasi-Zenith Satellite System/QZSS, the Indian Regional Navigation Satellite System/IRNSS, and worldwide Satellite Based Augmentation Systems/SBASs), which are similar to the U.S. GPS in terms of the satellite constellation, orbits, and signal structure. The hourly IRNSS broadcast ephemeris files contain one hour of IRNSS broadcast navigation data in RINEX format from a global permanent network of ground-based receivers, one file per site.",
-            "title": "Ground-Based Global Navigation Satellite System (GNSS) IRNSS Broadcast Ephemeris Data (hourly files) from NASA CDDIS",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGNSS%2FGNSS_HOURLY_I_001",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGNSS%2FGNSS_HOURLY_I_001",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://cddis.nasa.gov/archive/gnss/data/hourly",
-                    "description": "URL for retrieval of GNSS hourly data through https",
                     "@type": "dcat:Distribution",
+                    "description": "URL for retrieval of GNSS hourly data through https",
+                    "downloadURL": "https://cddis.nasa.gov/archive/gnss/data/hourly",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://cddis.nasa.gov/Data_and_Derived_Products/GNSS/broadcast_ephemeris_data.html",
-                    "description": "URL for more information about GNSS hourly IRNSS broadcast navigation data",
                     "@type": "dcat:Distribution",
+                    "description": "URL for more information about GNSS hourly IRNSS broadcast navigation data",
+                    "downloadURL": "https://cddis.nasa.gov/Data_and_Derived_Products/GNSS/broadcast_ephemeris_data.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/GNSS/GNSS_HOURLY_I_001",
-                    "description": "URL for more information about GNSS hourly IRNSS broadcast navigation data",
                     "@type": "dcat:Distribution",
+                    "description": "URL for more information about GNSS hourly IRNSS broadcast navigation data",
+                    "downloadURL": "https://doi.org/10.5067/GNSS/GNSS_HOURLY_I_001",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 }
             ],
+            "identifier": "C1605632902-CDDIS",
+            "issued": "1992-01-01",
+            "keyword": [
+                "earth science",
+                "solid earth",
+                "geodetics",
+                "gravity/gravitational field",
+                "tectonics"
+            ],
+            "landingPage": "https://doi.org/10.5067/GNSS/GNSS_HOURLY_I_001",
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
+            "title": "Ground-Based Global Navigation Satellite System (GNSS) IRNSS Broadcast Ephemeris Data (hourly files) from NASA CDDIS"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1267",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Liu, L., K. Schaefer, A. Chen, A. Gusmeroli, E. Jafarov, S. Panda, A. Parsekian, T. Schaefer, H. A. Zebker, T. Zhang. 2015. Pre-ABoVE: Remotely Sensed Active Layer Thickness, Prudhoe Bay, Alaska, 1992-2000. ORNL DAAC, Oak Ridge National Laboratory Distributed Active Archive Center, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/1267",
-            "issued": "2015-01-23",
-            "temporal": "1992-01-01T00:00:00Z/2000-12-31T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-12",
-            "keyword": [
-                "frozen ground",
-                "topography",
-                "earth science",
-                "land surface",
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
-            "identifier": "C2170968546-ORNL_CLOUD",
             "description": "Active layer thickness (ALT) is a critical parameter for monitoring the status of permafrost that is typically measured at specific locations using probing, in situ temperature sensors, or other ground-based observations. The thickness of the active layer is the average annual thaw depth, in permafrost areas, due to solar heating of the surface. This data set includes the mean Remotely Sensed Active Layer Thickness (ReSALT) over years 1992 to 2000 for an area near Prudhoe Bay, Alaska. The data were produced by an Interferometric Synthetic Aperture Radar (InSAR) technique that measures seasonal surface subsidence and infers ALT. ReSALT estimates were validated by comparison with ground-based ALT measurements at multiple sites. These results indicate remote sensing techniques based on InSAR could be an effective way to measure and monitor ALT over large areas on the Arctic coastal plain.These data provide gridded (100-m) estimates of active layer thickness (cm; ALT), seasonal subsidence (cm) and subsidence trend (mm/yr), as well as calculated uncertainty in each of these parameters. This data set was developed in support  of NASA's Arctic-Boreal Vulnerability Experiment (ABoVE) field campaign.The data are presented in one netCDF (*.nc) file.",
-            "graphic-preview-description": "Browse Image",
-            "title": "Pre-ABoVE: Remotely Sensed Active Layer Thickness, Prudhoe Bay, Alaska, 1992-2000",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/sdat-tds/1267_1_fit.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1267",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1267",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/above/InSAR_Prudhoe_Bay/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/above/InSAR_Prudhoe_Bay/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/ABOVE/guides/InSAR_Prudhoe_Bay.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/ABOVE/guides/InSAR_Prudhoe_Bay.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1267",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1267",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/InSAR_Prudhoe_Bay/comp/InSAR_Prudhoe_Bay.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/InSAR_Prudhoe_Bay/comp/InSAR_Prudhoe_Bay.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/InSAR_Prudhoe_Bay/comp/ReSALT_prudhoe.txt",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/InSAR_Prudhoe_Bay/comp/ReSALT_prudhoe.txt",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://daac.ornl.gov/graphics/browse/sdat-tds/1267_1_fit.png",
-                    "description": "Browse Image",
                     "@type": "dcat:Distribution",
+                    "description": "Browse Image",
+                    "downloadURL": "https://daac.ornl.gov/graphics/browse/sdat-tds/1267_1_fit.png",
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
-                    "downloadURL": "https://thredds.daac.ornl.gov/thredds/catalog/ornldaac/1267/catalog.html",
-                    "description": "The THREDDS location for this Collection.",
                     "@type": "dcat:Distribution",
+                    "description": "The THREDDS location for this Collection.",
+                    "downloadURL": "https://thredds.daac.ornl.gov/thredds/catalog/ornldaac/1267/catalog.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "graphic-preview-description": "Browse Image",
+            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/sdat-tds/1267_1_fit.png",
+            "identifier": "C2170968546-ORNL_CLOUD",
+            "issued": "2015-01-23",
+            "keyword": [
+                "frozen ground",
+                "topography",
+                "earth science",
+                "land surface",
+                "cryosphere"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1267",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2023-07-12",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "ORNL_DAAC"
+            },
             "spatial": "-149.5 69.95 -146.99 70.45",
+            "temporal": "1992-01-01T00:00:00Z/2000-12-31T23:59:59Z",
             "theme": [
                 "ABoVE",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Pre-ABoVE: Remotely Sensed Active Layer Thickness, Prudhoe Bay, Alaska, 1992-2000"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=CLEM1-L-LWIR-3-RDR-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This volume contains the archive of Lunar brightness temperature data derived from images acquired by the Clementine Long Wavelength Infrared (LWIR) camera. The LWIR camera acquired approximately 220,000 thermal-infrared images of the lunar surface that were used to generate the brightness temperature images within this archive. The procedure for generating brightness temperature values can be summarized as follows: 1) original LWIR digital numbers were converted to radiance; 2) the dark current signal was subtracted from the radiance values; 3) a flat field correction was applied; 4) bad pixels were identified and smoothed over; and 5) calibrated radiance values were converted to brightness temperatures using the Planck function.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.clem1-l-lwir-3-rdr-v1.0_krhz-mw2p",
             "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "moon",
                 "sky",
                 "deep space program science experiment"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=CLEM1-L-LWIR-3-RDR-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.clem1-l-lwir-3-rdr-v1.0_krhz-mw2p",
-            "description": "This volume contains the archive of Lunar brightness temperature data derived from images acquired by the Clementine Long Wavelength Infrared (LWIR) camera. The LWIR camera acquired approximately 220,000 thermal-infrared images of the lunar surface that were used to generate the brightness temperature images within this archive. The procedure for generating brightness temperature values can be summarized as follows: 1) original LWIR digital numbers were converted to radiance; 2) the dark current signal was subtracted from the radiance values; 3) a flat field correction was applied; 4) bad pixels were identified and smoothed over; and 5) calibrated radiance values were converted to brightness temperatures using the Planck function.",
-            "title": "CLEMENTINE LWIR BRIGHTNESS TEMPERATURE V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "CLEMENTINE LWIR BRIGHTNESS TEMPERATURE V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/3LXL78PSKVXQ",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "SMAPVEX19-22 Massachusetts Temporary Soil Moisture Network V001. Version 001. Archived by National Aeronautics and Space Administration, U.S. Government, NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/3LXL78PSKVXQ.",
-            "issued": "2019-05-01",
-            "temporal": "2019-05-01T00:00:00Z/2021-10-31T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2021-10-31",
-            "keyword": [
-                "soils",
-                "earth science",
-                "atmospheric temperature",
-                "land surface",
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
-            "identifier": "C2654469973-NSIDC_ECS",
             "description": "These data consist of ground-based, soil moisture, soil temperature, and air temperature measurements recorded by twenty-five temporary stations located in the vicinity of Petersham, MA during the SMAPVEX19-22 campaign. The stations were installed across an area of approximately 23 km by 36 km in May 2019 and operated through 2022. Note that the product is named SMAPVEX19-22 because, although the current coverage is through 2021, it is projected to include 2022 data in the future.",
-            "title": "SMAPVEX19-22 Massachusetts Temporary Soil Moisture Network V001",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2F3LXL78PSKVXQ",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2F3LXL78PSKVXQ",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/SMAP_VAL/SV19MA_TNET.001/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/SMAP_VAL/SV19MA_TNET.001/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=SV19MA_TNET+V001",
-                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=SV19MA_TNET+V001",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/data/data-access-tool/SV19MA_TNET/versions/1/",
-                    "description": "Search and filter data files using a map-based interface",
                     "@type": "dcat:Distribution",
+                    "description": "Search and filter data files using a map-based interface",
+                    "downloadURL": "https://nsidc.org/data/data-access-tool/SV19MA_TNET/versions/1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/3LXL78PSKVXQ",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/3LXL78PSKVXQ",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/3LXL78PSKVXQ",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/3LXL78PSKVXQ",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C2654469973-NSIDC_ECS",
+            "issued": "2019-05-01",
+            "keyword": [
+                "soils",
+                "earth science",
+                "atmospheric temperature",
+                "land surface",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.5067/3LXL78PSKVXQ",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2021-10-31",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA NSIDC DAAC"
+            },
             "spatial": "-72.29 42.34 -71.95 42.69",
+            "temporal": "2019-05-01T00:00:00Z/2021-10-31T23:59:59.999Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "SMAPVEX19-22 Massachusetts Temporary Soil Moisture Network V001"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RPCLAP-5-EXT3-NEL-V1.0",
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
+            "description": "This data set contains DERIVED\ndata from Rosetta RPC-LAP, acquired during the ROSETTA EXTENSION 3\nmission phase where the primary target was the comet\n67P/CHURYUMOV-GERASIMENKO 1 (1969 R1). It contains electron density at\nhigher time resolution than in the DERIV2 data sets.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rpclap-5-ext3-nel-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RPCLAP-5-EXT3-NEL-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rpclap-5-ext3-nel-v1.0",
-            "description": "This data set contains DERIVED\ndata from Rosetta RPC-LAP, acquired during the ROSETTA EXTENSION 3\nmission phase where the primary target was the comet\n67P/CHURYUMOV-GERASIMENKO 1 (1969 R1). It contains electron density at\nhigher time resolution than in the DERIV2 data sets.",
-            "title": "ROSETTA-ORBITER 67P RPCLAP 5\nEXT3 NEL V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RPCLAP 5\nEXT3 NEL V1.0"
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
+            "description": "APXS, ENG, HAZCAM, NAVCAM, MI, PANCAM, RAT, SPICE",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://pds.jpl.nasa.gov/tools/subscription_service/SS-20131206.shtml",
+                    "mediaType": "application/html"
+                }
             ],
+            "identifier": "NASA-461",
+            "issued": "2018-06-25",
             "keyword": [
                 "hazcam",
                 "pds",
@@ -1044600,226 +1044609,231 @@
                 "eng",
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
-            "identifier": "NASA-461",
-            "description": "APXS, ENG, HAZCAM, NAVCAM, MI, PANCAM, RAT, SPICE",
-            "title": "PDS Mars Exploration Rovers Data Release 38",
-            "programCode": [
-                "026:005"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://pds.jpl.nasa.gov/tools/subscription_service/SS-20131206.shtml",
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
+            "title": "PDS Mars Exploration Rovers Data Release 38"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/YP1PVPR72IHG",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "IceBridge MCoRDS L3 Gridded Ice Thickness, Surface, and Bottom V002. Version 2. Archived by National Aeronautics and Space Administration, U.S. Government, NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/YP1PVPR72IHG.",
-            "issued": "2006-01-01",
-            "temporal": "2006-01-01T00:00:00Z/2012-12-31T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2012-12-31",
-            "keyword": [
-                "earth science",
-                "glaciers/ice sheets",
-                "cryosphere"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "John Paden",
                 "hasEmail": "mailto:paden@ku.edu"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA NSIDC DAAC"
-            },
-            "identifier": "C1426298063-NSIDC_ECS",
             "description": "This data set contains products from depth sounder measurements over Greenland and Antarctica taken from the Multichannel Coherent Radar Depth Sounder (MCoRDS). The data were collected as part of NASA Operation IceBridge funded campaigns. Browse files for this data set are duplicates for the thickness PNG files.",
-            "title": "IceBridge MCoRDS L3 Gridded Ice Thickness, Surface, and Bottom V002",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FYP1PVPR72IHG",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FYP1PVPR72IHG",
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
-                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/ICEBRIDGE/IRMCR3.002/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/ICEBRIDGE/IRMCR3.002/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/data/data-access-tool/IRMCR3/versions/2/",
-                    "description": "Data Access link for ITSD project",
                     "@type": "dcat:Distribution",
+                    "description": "Data Access link for ITSD project",
+                    "downloadURL": "https://nsidc.org/data/data-access-tool/IRMCR3/versions/2/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
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
-                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/ICEBRIDGE/IRMCR3.002/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/ICEBRIDGE/IRMCR3.002/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/data/data-access-tool/IRMCR3/versions/2/",
-                    "description": "Data Access link for ITSD project",
                     "@type": "dcat:Distribution",
+                    "description": "Data Access link for ITSD project",
+                    "downloadURL": "https://nsidc.org/data/data-access-tool/IRMCR3/versions/2/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
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
-                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/ICEBRIDGE/IRMCR3.002/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/ICEBRIDGE/IRMCR3.002/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/data/data-access-tool/IRMCR3/versions/2/",
-                    "description": "Data Access link for ITSD project",
                     "@type": "dcat:Distribution",
+                    "description": "Data Access link for ITSD project",
+                    "downloadURL": "https://nsidc.org/data/data-access-tool/IRMCR3/versions/2/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
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
-                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/ICEBRIDGE/IRMCR3.002/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/ICEBRIDGE/IRMCR3.002/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/data/data-access-tool/IRMCR3/versions/2/",
-                    "description": "Data Access link for ITSD project",
                     "@type": "dcat:Distribution",
+                    "description": "Data Access link for ITSD project",
+                    "downloadURL": "https://nsidc.org/data/data-access-tool/IRMCR3/versions/2/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/YP1PVPR72IHG",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/YP1PVPR72IHG",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/YP1PVPR72IHG",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/YP1PVPR72IHG",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C1426298063-NSIDC_ECS",
+            "issued": "2006-01-01",
+            "keyword": [
+                "earth science",
+                "glaciers/ice sheets",
+                "cryosphere"
+            ],
+            "landingPage": "https://doi.org/10.5067/YP1PVPR72IHG",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2012-12-31",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA NSIDC DAAC"
+            },
             "spatial": "-180.0 -90.0 180.0 -53.0",
+            "temporal": "2006-01-01T00:00:00Z/2012-12-31T23:59:59.999Z",
             "theme": [
                 "MULTI_NASA",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "IceBridge MCoRDS L3 Gridded Ice Thickness, Surface, and Bottom V002"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MER2-M-MB-2-EDR-OPS-V1.0",
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
+            "description": "This archive contains Mars Exploration Rover Operations (Ops)\nMoessbauer Experiment Data Record (EDR) products and ancillary files.\nThe Moessbauer Operations EDR products archived on this volume\nare the original products used during mission operations by the Mars\nExploration Rover project.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mer2-m-mb-2-edr-ops-v1.0_krtd-cmkk",
+            "issued": "2021-05-21",
+            "keyword": [
+                "mars exploration rover",
+                "mars"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MER2-M-MB-2-EDR-OPS-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mer2-m-mb-2-edr-ops-v1.0_krtd-cmkk",
-            "description": "This archive contains Mars Exploration Rover Operations (Ops)\nMoessbauer Experiment Data Record (EDR) products and ancillary files.\nThe Moessbauer Operations EDR products archived on this volume\nare the original products used during mission operations by the Mars\nExploration Rover project.",
-            "title": "MER 2 MARS MOESSBAUER SPECTROMETER EDR\n                                      OPS VERSION 1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "MER 2 MARS MOESSBAUER SPECTROMETER EDR\n                                      OPS VERSION 1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.nasa.gov/d/krvn-94zk",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "GeneLab Outreach",
+                "hasEmail": "mailto:genelab-outreach@lists.nasa.gov"
+            },
+            "description": "BACKGROUND: Ionizing radiation (IR) can be extremely harmful for human cells since an improper DNA-damage response (DDR) to IR can contribute to carcinogenesis initiation. Perturbations in DDR pathway can originate from alteration in the functionality of the microRNA-mediated gene regulation being microRNAs (miRNAs) small noncoding RNA that act as post-transcriptional regulators of gene expression. In this study we gained insight into the role of miRNAs in the regulation of DDR to IR under microgravity a condition of weightlessness experienced by astronauts during space missions which could have a synergistic action on cells increasing the risk of radiation exposure. METHODOLOGY/PRINCIPAL FINDINGS: We analyzed miRNA expression profile of human peripheral blood lymphocytes (PBL) incubated for 4 and 24 h in normal gravity (1 g) and in modeled microgravity (MMG) during the repair time after irradiation with 0.2 and 2Gy of gamma-rays. Our results show that MMG alters miRNA expression signature of irradiated PBL by decreasing the number of radio-responsive miRNAs. Moreover let-7i* miR-7 miR-7-1* miR-27a miR-144 miR-200a miR-598 miR-650 are deregulated by the combined action of radiation and MMG. Integrated analyses of miRNA and mRNA expression profiles carried out on PBL of the same donors identified significant miRNA-mRNA anti-correlations of DDR pathway. Gene Ontology analysis reports that the biological category of Response to DNA damage is enriched when PBL are incubated in 1 g but not in MMG. Moreover some anti-correlated genes of p53-pathway show a different expression level between 1 g and MMG. Functional validation assays using luciferase reporter constructs confirmed miRNA-mRNA interactions derived from target prediction analyses. CONCLUSIONS/SIGNIFICANCE: On the whole by integrating the transcriptome and microRNome we provide evidence that modeled microgravity can affects the DNA-damage response to IR in human PBL.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "GeneLab Study Page",
+                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-128",
+                    "mediaType": "text/html",
+                    "title": "Identification of miRNAs involved in cell response to ionising radiation and modeled microgravity"
+                }
+            ],
+            "identifier": "nasa_genelab_GLDS-128_krvn-94zk",
             "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
             "keyword": [
                 "ionizing radiation",
                 "simulated microgravity",
@@ -1044831,85 +1044845,73 @@
                 "labeling",
                 "data collection"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "GeneLab Outreach",
-                "hasEmail": "mailto:genelab-outreach@lists.nasa.gov"
-            },
+            "landingPage": "https://data.nasa.gov/d/krvn-94zk",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "nasa_genelab_GLDS-128_krvn-94zk",
-            "description": "BACKGROUND: Ionizing radiation (IR) can be extremely harmful for human cells since an improper DNA-damage response (DDR) to IR can contribute to carcinogenesis initiation. Perturbations in DDR pathway can originate from alteration in the functionality of the microRNA-mediated gene regulation being microRNAs (miRNAs) small noncoding RNA that act as post-transcriptional regulators of gene expression. In this study we gained insight into the role of miRNAs in the regulation of DDR to IR under microgravity a condition of weightlessness experienced by astronauts during space missions which could have a synergistic action on cells increasing the risk of radiation exposure. METHODOLOGY/PRINCIPAL FINDINGS: We analyzed miRNA expression profile of human peripheral blood lymphocytes (PBL) incubated for 4 and 24 h in normal gravity (1 g) and in modeled microgravity (MMG) during the repair time after irradiation with 0.2 and 2Gy of gamma-rays. Our results show that MMG alters miRNA expression signature of irradiated PBL by decreasing the number of radio-responsive miRNAs. Moreover let-7i* miR-7 miR-7-1* miR-27a miR-144 miR-200a miR-598 miR-650 are deregulated by the combined action of radiation and MMG. Integrated analyses of miRNA and mRNA expression profiles carried out on PBL of the same donors identified significant miRNA-mRNA anti-correlations of DDR pathway. Gene Ontology analysis reports that the biological category of Response to DNA damage is enriched when PBL are incubated in 1 g but not in MMG. Moreover some anti-correlated genes of p53-pathway show a different expression level between 1 g and MMG. Functional validation assays using luciferase reporter constructs confirmed miRNA-mRNA interactions derived from target prediction analyses. CONCLUSIONS/SIGNIFICANCE: On the whole by integrating the transcriptome and microRNome we provide evidence that modeled microgravity can affects the DNA-damage response to IR in human PBL.",
-            "title": "Identification of miRNAs involved in cell response to ionising radiation and modeled microgravity",
-            "programCode": [
-                "026:005"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-128",
-                    "description": "GeneLab Study Page",
-                    "@type": "dcat:Distribution",
-                    "title": "Identification of miRNAs involved in cell response to ionising radiation and modeled microgravity"
-                }
-            ],
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "Identification of miRNAs involved in cell response to ionising radiation and modeled microgravity"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-X-OSIWAC-3-CVP1-CHECKOUT-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This CODMAC level 3 data set contains radiometric calibrated image data in W/m^2/sr/nm,  acquired by the OSIRIS Wide Angle Camera on the Rosetta spacecraft  during the COMMISSIONING 1 mission phase, covering the period  from 2004-03-05T00:00:00.000 to 2004-06-06T23:59:59.000. The prime objective was commissioning / calibration. Several targets of opportunity were observed, but none of them is identifiable as prime target. After the October 2018 PSA/PDS external peer review, the COMMISSIONING  data set was reprocessed and split into multiple data sets.  This  version V1.0 is one part and supersedes the previous delivery.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-x-osiwac-3-cvp1-checkout-v1.0",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2021-05-21",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "international rosetta mission",
                 "c/linear (2002 t7)",
                 "eps aqr"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-X-OSIWAC-3-CVP1-CHECKOUT-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-x-osiwac-3-cvp1-checkout-v1.0",
-            "description": "This CODMAC level 3 data set contains radiometric calibrated image data in W/m^2/sr/nm,  acquired by the OSIRIS Wide Angle Camera on the Rosetta spacecraft  during the COMMISSIONING 1 mission phase, covering the period  from 2004-03-05T00:00:00.000 to 2004-06-06T23:59:59.000. The prime objective was commissioning / calibration. Several targets of opportunity were observed, but none of them is identifiable as prime target. After the October 2018 PSA/PDS external peer review, the COMMISSIONING  data set was reprocessed and split into multiple data sets.  This  version V1.0 is one part and supersedes the previous delivery.",
-            "title": "ROSETTA-ORBITER CHECKOUT OSIWAC 3 CVP1 RDR V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER CHECKOUT OSIWAC 3 CVP1 RDR V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-J-MVIC-2-JUPITER-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This data set contains Raw data taken by the New Horizons Multispectral Visible Imaging Camera instrument during the Jupiter encounter mission phase.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-j-mvic-2-jupiter-v1.0_krwy-9krx",
             "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "new horizons",
                 "earth",
@@ -1044919,575 +1044921,585 @@
                 "j2 europa",
                 "callisto"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-J-MVIC-2-JUPITER-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-j-mvic-2-jupiter-v1.0_krwy-9krx",
-            "description": "This data set contains Raw data taken by the New Horizons Multispectral Visible Imaging Camera instrument during the Jupiter encounter mission phase.",
-            "title": "NEW HORIZONS MVIC JUPITER ENCOUNTER V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "NEW HORIZONS MVIC JUPITER ENCOUNTER V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/3X4CIKKSYQRU",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "IceBridge CMG GT-1A Gravimeter L2 Geolocated Free Air Gravity Disturbances V001. Version 1. Archived by National Aeronautics and Space Administration, U.S. Government, NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/3X4CIKKSYQRU.",
-            "issued": "2012-11-22",
-            "temporal": "2012-11-22T00:00:00Z/2012-12-04T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2012-12-04",
-            "keyword": [
-                "solid earth",
-                "earth science",
-                "gravity/gravitational field"
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
-            "identifier": "C1000000380-NSIDC_ECS",
             "description": "This data set contains geolocated free air gravity disturbances derived from measurements taken over Antarctica using the GT-1A gravity meter S-019. The data were collected by scientists working on the Investigating the Cryospheric Evolution of the Central Antarctic Plate (ICECAP) project, which is funded by the National Science Foundation (NSF) and the Natural Environment Research Council (NERC) with additional support from NASA Operation IceBridge.",
-            "title": "IceBridge CMG GT-1A Gravimeter L2 Geolocated Free Air Gravity Disturbances V001",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2F3X4CIKKSYQRU",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2F3X4CIKKSYQRU",
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
-                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/ICEBRIDGE/IGCMG2.001/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/ICEBRIDGE/IGCMG2.001/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1000000380-NSIDC_ECS&m=-58.827500141439664%21140.22040945893772%210%212%210%210%2C2&q=IGCMG2",
-                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1000000380-NSIDC_ECS&m=-58.827500141439664%21140.22040945893772%210%212%210%210%2C2&q=IGCMG2",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/data/data-access-tool/IGCMG2/versions/1/",
-                    "description": "Data Access link for ITSD project",
                     "@type": "dcat:Distribution",
+                    "description": "Data Access link for ITSD project",
+                    "downloadURL": "https://nsidc.org/data/data-access-tool/IGCMG2/versions/1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
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
-                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/ICEBRIDGE/IGCMG2.001/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/ICEBRIDGE/IGCMG2.001/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1000000380-NSIDC_ECS&m=-58.827500141439664%21140.22040945893772%210%212%210%210%2C2&q=IGCMG2",
-                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1000000380-NSIDC_ECS&m=-58.827500141439664%21140.22040945893772%210%212%210%210%2C2&q=IGCMG2",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/data/data-access-tool/IGCMG2/versions/1/",
-                    "description": "Data Access link for ITSD project",
                     "@type": "dcat:Distribution",
+                    "description": "Data Access link for ITSD project",
+                    "downloadURL": "https://nsidc.org/data/data-access-tool/IGCMG2/versions/1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/3X4CIKKSYQRU",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/3X4CIKKSYQRU",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/3X4CIKKSYQRU",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/3X4CIKKSYQRU",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C1000000380-NSIDC_ECS",
+            "issued": "2012-11-22",
+            "keyword": [
+                "solid earth",
+                "earth science",
+                "gravity/gravitational field"
+            ],
+            "landingPage": "https://doi.org/10.5067/3X4CIKKSYQRU",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2012-12-04",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA NSIDC DAAC"
+            },
             "spatial": "-180.0 -90.0 180.0 -53.0",
+            "temporal": "2012-11-22T00:00:00Z/2012-12-04T23:59:59.999Z",
             "theme": [
                 "2012_AN_UTIG",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "IceBridge CMG GT-1A Gravimeter L2 Geolocated Free Air Gravity Disturbances V001"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/IMPACTS/NEXRAD/DATA201",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Brodzik, Stacy .2022. NEXRAD Mosaic East IMPACTS [indicate subset used]. Dataset available online from the NASA Global Hydrometeorology Resource Center DAAC, Huntsville, Alabama, U.S.A. DOI: http://dx.doi.org/10.5067/IMPACTS/NEXRAD/DATA201",
-            "issued": "2022-03-23",
-            "temporal": "2019-12-31T23:50:34Z/2020-02-29T23:58:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-31",
-            "keyword": [
-                "earth science",
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
-            "identifier": "C1995866059-GHRC_DAAC",
             "description": "The NEXRAD Mosaic East IMPACTS dataset consists of Next Generation Weather Radar (NEXRAD) 3D mosaic files created from Level II surveillance data gathered  during the Investigation of Microphysics and Precipitation for Atlantic Coast-Threatening Snowstorms (IMPACTS) field campaign. IMPACTS was a three-year sequence of winter season deployments conducted to study snowstorms over the U.S. Atlantic Coast (2020-2022). The campaign aimed to (1) Provide observations critical to understanding the mechanisms of snowband formation, organization, and evolution; (2) Examine how the microphysical characteristics and likely growth mechanisms of snow particles vary across snowbands; and (3) Improve snowfall remote sensing interpretation and modeling to significantly advance prediction capabilities. The Mosaic East dataset is composed of Level II data from 19 NEXRAD sites in the eastern U.S.. These data files are available in netCDF-4 format and contain meteorological and dual-polarization base data quantities including radar reflectivity, radial velocity, spectrum width, differential reflectivity, differential phase, and cross correlation ratio from January 1 through February 29, 2020. It should be noted that this dataset will be updated in subsequent years of the IMPACTS campaign.",
-            "title": "NEXRAD Mosaic East IMPACTS V1",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FIMPACTS%2FNEXRAD%2FDATA201",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FIMPACTS%2FNEXRAD%2FDATA201",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=nexeastimpacts",
-                    "description": "Files may be downloaded directly to your workstation from this link",
                     "@type": "dcat:Distribution",
+                    "description": "Files may be downloaded directly to your workstation from this link",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=nexeastimpacts",
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
-                    "downloadURL": "https://ral.ucar.edu/projects/titan/docs/TitanDataFlow.pdf",
-                    "description": "TITANS User Guide",
                     "@type": "dcat:Distribution",
+                    "description": "TITANS User Guide",
+                    "downloadURL": "https://ral.ucar.edu/projects/titan/docs/TitanDataFlow.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View information related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://espo.nasa.gov/impacts",
-                    "description": "IMPACTS Field Campaign",
                     "@type": "dcat:Distribution",
+                    "description": "IMPACTS Field Campaign",
+                    "downloadURL": "https://espo.nasa.gov/impacts",
+                    "mediaType": "text/html",
                     "title": "View information related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.ncdc.noaa.gov/data-access/radar-data/nexrad",
-                    "description": "NEXRAD Instrument Information",
                     "@type": "dcat:Distribution",
+                    "description": "NEXRAD Instrument Information",
+                    "downloadURL": "https://www.ncdc.noaa.gov/data-access/radar-data/nexrad",
+                    "mediaType": "text/html",
                     "title": "View information related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://catalog.data.gov/dataset/noaa-next-generation-radar-nexrad-products",
-                    "description": "NEXRAD Radar Data Products",
                     "@type": "dcat:Distribution",
+                    "description": "NEXRAD Radar Data Products",
+                    "downloadURL": "https://catalog.data.gov/dataset/noaa-next-generation-radar-nexrad-products",
+                    "mediaType": "text/html",
                     "title": "View information related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "http://www.ofcm.gov/publications/fmh/FMH11/fmh-11B-2005.pdf",
-                    "description": "Federal Meteorological Handbook No. 11 Part B: Doppler Radar Theory and Meteorology.",
                     "@type": "dcat:Distribution",
+                    "description": "Federal Meteorological Handbook No. 11 Part B: Doppler Radar Theory and Meteorology.",
+                    "downloadURL": "http://www.ofcm.gov/publications/fmh/FMH11/fmh-11B-2005.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View information related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "http://www.ofcm.gov/publications/fmh/FMH11/FMH11D-2006.pdf",
-                    "description": "Federal Meteorological Handbook No. 11 Part D: WSR-88D Unit Description and Operational Applications",
                     "@type": "dcat:Distribution",
+                    "description": "Federal Meteorological Handbook No. 11 Part D: WSR-88D Unit Description and Operational Applications",
+                    "downloadURL": "http://www.ofcm.gov/publications/fmh/FMH11/FMH11D-2006.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View information related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "http://www.ofcm.gov/publications/fmh/FMH11/2016FMH11PTA.pdf",
-                    "description": "Federal Meteorological Handbook No. 11 Part A: System Concepts, Responsibilities, and Procedures",
                     "@type": "dcat:Distribution",
+                    "description": "Federal Meteorological Handbook No. 11 Part A: System Concepts, Responsibilities, and Procedures",
+                    "downloadURL": "http://www.ofcm.gov/publications/fmh/FMH11/2016FMH11PTA.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View information related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "http://www.ofcm.gov/publications/fmh/FMH11/fmh11partC.pdf",
-                    "description": "Federal Meteorological Handbook No. 11 Part C: WSR-88D Products and Algorithms",
                     "@type": "dcat:Distribution",
+                    "description": "Federal Meteorological Handbook No. 11 Part C: WSR-88D Products and Algorithms",
+                    "downloadURL": "http://www.ofcm.gov/publications/fmh/FMH11/fmh11partC.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View information related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/impacts/NEXRAD/Mosaic_East/doc/nexmosaicimpacts_datasets.pdf",
-                    "description": "Mosaic NEXRAD IMPACTS Datasets User Guide",
                     "@type": "dcat:Distribution",
+                    "description": "Mosaic NEXRAD IMPACTS Datasets User Guide",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/impacts/NEXRAD/Mosaic_East/doc/nexmosaicimpacts_datasets.pdf",
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
+            "identifier": "C1995866059-GHRC_DAAC",
+            "issued": "2022-03-23",
+            "keyword": [
+                "earth science",
+                "radar",
+                "spectral/engineering"
+            ],
+            "landingPage": "https://doi.org/10.5067/IMPACTS/NEXRAD/DATA201",
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
             "spatial": "-85.0 32.5 -67.525 46.475",
+            "temporal": "2019-12-31T23:50:34Z/2020-02-29T23:58:00Z",
             "theme": [
                 "IMPACTS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "NEXRAD Mosaic East IMPACTS V1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/994",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Fekete, B.M., C.J. Vorosmarty, F.G. Hall, G.J. Collatz, B.W. Meeson, S.O. Los, E.Brown De Colstoun, and D.R. Landis. 2011. ISLSCP II UNH/GRDC Composite Monthly Runoff. ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/994",
-            "issued": "2023-10-15",
-            "temporal": "1986-01-01T00:00:00Z/1995-12-31T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-10-17",
-            "keyword": [
-                "earth science",
-                "ecosystems",
-                "topography",
-                "biosphere",
-                "ecological dynamics",
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
-            "identifier": "C2784897571-ORNL_CLOUD",
             "description": "The University of New Hampshire (UNH)/Global Runoff Data Centre (GRDC) composite runoff data combines simulated water balance model runoff estimates derived from climate forcing with monitored river discharge. It can be viewed as a data assimilation applied in a water balance model context (conceptually similar to the commonly used 4DDA techniques used in meteorological modeling). Such a data assimilation scheme preserves the spatial specificity of the water balance calculations while constrained by the more accurate discharge measurement. There are 11 data files in this data set and 1 changemap file which shows the differences between the ISLSCP II land/water mask and the original data set.",
-            "graphic-preview-description": "Browse Image",
-            "title": "ISLSCP II UNH/GRDC Composite Monthly Runoff",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/sdat-tds/994_1_fit.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F994",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F994",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/islscp_ii/hydrology_soils/comp_runoff_monthly_xdeg/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/islscp_ii/hydrology_soils/comp_runoff_monthly_xdeg/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/ISLSCP_II/guides/comp_runoff_monthly_xdeg.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/ISLSCP_II/guides/comp_runoff_monthly_xdeg.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/994",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/994",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/islscp_ii/hydrology_soils/comp_runoff_monthly_xdeg/comp/0_comp_runoff_month_readme.txt",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/islscp_ii/hydrology_soils/comp_runoff_monthly_xdeg/comp/0_comp_runoff_month_readme.txt",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/islscp_ii/hydrology_soils/comp_runoff_monthly_xdeg/comp/1_comp_runoff_month_doc.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/islscp_ii/hydrology_soils/comp_runoff_monthly_xdeg/comp/1_comp_runoff_month_doc.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://daac.ornl.gov/graphics/browse/sdat-tds/994_1_fit.png",
-                    "description": "Browse Image",
                     "@type": "dcat:Distribution",
+                    "description": "Browse Image",
+                    "downloadURL": "https://daac.ornl.gov/graphics/browse/sdat-tds/994_1_fit.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://webmap.ornl.gov/wcsdown/dataset.jsp?ds_id=994",
-                    "description": "Web Coverage Service for this collection.",
                     "@type": "dcat:Distribution",
+                    "description": "Web Coverage Service for this collection.",
+                    "downloadURL": "https://webmap.ornl.gov/wcsdown/dataset.jsp?ds_id=994",
+                    "mediaType": "text/html",
                     "title": "Use Web Coverage Service (WCS) to download the dataset's data"
                 }
             ],
+            "graphic-preview-description": "Browse Image",
+            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/sdat-tds/994_1_fit.png",
+            "identifier": "C2784897571-ORNL_CLOUD",
+            "issued": "2023-10-15",
+            "keyword": [
+                "earth science",
+                "ecosystems",
+                "topography",
+                "biosphere",
+                "ecological dynamics",
+                "land surface"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/994",
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
+            "title": "ISLSCP II UNH/GRDC Composite Monthly Runoff"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-2-ESC1-67PCHURYUMOV-M10-V1.0",
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
+            "description": "This data set contains raw EDR images acquired by the OSIRIS Narrow Angle\nCamera during the escort phase of the Rosetta mission at the comet 67P,\ncovering the period from 2014-11-21 to 2014-12-19.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-2-esc1-67pchuryumov-m10-v1.0_ks2s-et3f",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-2-ESC1-67PCHURYUMOV-M10-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-2-esc1-67pchuryumov-m10-v1.0_ks2s-et3f",
-            "description": "This data set contains raw EDR images acquired by the OSIRIS Narrow Angle\nCamera during the escort phase of the Rosetta mission at the comet 67P,\ncovering the period from 2014-11-21 to 2014-12-19.",
-            "title": "ROSETTA-ORBITER COMET ESCORT1 OSINAC 2 EDR MTP 010 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER COMET ESCORT1 OSINAC 2 EDR MTP 010 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=IRTF-SR-URAC-4-OCC-V1.0",
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
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.irtf-sr-urac-4-occ-v1.0_ks2t-5yp2",
             "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "saturn",
                 "saturn occultation of 28 sagittarius 1989",
                 "s rings"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=IRTF-SR-URAC-4-OCC-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.irtf-sr-urac-4-occ-v1.0_ks2t-5yp2",
-            "description": "not applicable",
-            "title": "IRTF SR U-ROCHESTER-ARRY-CAM RESAMPLED RING OCCULTATION V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "IRTF SR U-ROCHESTER-ARRY-CAM RESAMPLED RING OCCULTATION V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/XIMNXRTQVMOX",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "AMSR-E/Aqua Daily EASE-Grid Brightness Temperatures, Version 1. Version 1. Archived by National Aeronautics and Space Administration, U.S. Government, NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/XIMNXRTQVMOX.",
-            "issued": "2002-06-19",
-            "temporal": "2002-06-19T00:00:00Z/2011-09-27T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2011-09-27",
-            "keyword": [
-                "earth science",
-                "microwave",
-                "spectral/engineering"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Matthew Savoie",
                 "hasEmail": "mailto:savoie@nsidc.org"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA NSIDC DAAC"
-            },
-            "identifier": "C1386204218-NSIDCV0",
             "description": "The Advanced Microwave Scanning Radiometer - Earth Observing System (AMSR-E) instrument on the NASA EOS Aqua satellite provides global passive microwave measurements of the Earth. NSIDC produces AMSR-E gridded brightness temperature data by interpolating AMSR-E data (6.9 GHz, 10.7 GHz, 18.7 GHz, 23.8 GHz, 36.5 GHz, and 89.0 GHz) to the output grids from swath space using an Inverse Distance Squared (ID2) method. AMSR-E/Aqua L2A Global Swath Spatially-Resampled Brightness Temperatures (AE_L2A) input source data are used.\n\nThese data are provided in three EASE-Grid projections (north and south Lambert azimuthal and global cylindrical) at 25 km resolution, and in one global cylindrical, equidistant latitude-longitude projection at 0.25 degree (quarter-degree) resolution.",
-            "title": "AMSR-E/Aqua Daily EASE-Grid Brightness Temperatures, Version 1",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FXIMNXRTQVMOX",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FXIMNXRTQVMOX",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/nsidc0301_amsre_ease_grid_tbs/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/nsidc0301_amsre_ease_grid_tbs/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/XIMNXRTQVMOX",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/XIMNXRTQVMOX",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/XIMNXRTQVMOX",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/XIMNXRTQVMOX",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C1386204218-NSIDCV0",
+            "issued": "2002-06-19",
+            "keyword": [
+                "earth science",
+                "microwave",
+                "spectral/engineering"
+            ],
+            "landingPage": "https://doi.org/10.5067/XIMNXRTQVMOX",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2011-09-27",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA NSIDC DAAC"
+            },
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2002-06-19T00:00:00Z/2011-09-27T23:59:59.999Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "AMSR-E/Aqua Daily EASE-Grid Brightness Temperatures, Version 1"
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
+                    "downloadURL": "http://arxiv.org/abs/1306.6772",
+                    "mediaType": "text/html"
+                }
+            ],
+            "identifier": "NASA-0000220",
             "issued": "2018-06-25",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
             "keyword": [
                 "gamma-ray",
                 "high-energy",
@@ -1045505,262 +1045517,224 @@
                 "balloon",
                 "acd"
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
-            "identifier": "NASA-0000220",
-            "description": "This catalog of LAT sources above 10 GeV reports the locations, spectra, and variability properties of the 514 sources significantly detected in this range during the first three years of the Fermi mission. Many of these sources are already included in the 2FGL catalog, although in that catalog their characterization is dominated by the much larger numbers of gamma rays detected in the energy range 0.1 to 10 GeV.",
-            "title": "First Fermi-LAT Catalog of Sources above 10 GeV (1FHL)",
-            "programCode": [
-                "026:014"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://arxiv.org/abs/1306.6772",
-                    "mediaType": "text/html"
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
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/EGCSHHHVLJKT",
             "citation": "NASA/GSFC. 2021-11-18. TIROS4L1ORT. Version 001. TIROS-4 Low-Resolution Omnidirectional Radiometer Level 1 Temperature Data V001. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/EGCSHHHVLJKT. https://disc.gsfc.nasa.gov/datacollection/TIROS4L1ORT_001.html. Digital Science Data.",
-            "issued": "2021-08-13",
-            "temporal": "1962-02-08T00:00:00Z/1962-06-28T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2021-08-13",
-            "keyword": [
-                "earth science",
-                "atmosphere",
-                "atmospheric radiation"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "JAMES JOHNSON",
                 "hasEmail": "mailto:James.Johnson@nasa.gov"
             },
+            "creator": "NASA/GSFC",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C2152905392-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "The TIROS-4 Low-Resolution Omnidirectional Radiometer Level 1 Temperature Data product contains the black and white sensor temperature values in degrees Celsius. The experiment consisted of two sets of bolometers in the form of hollow aluminum hemispheres, mounted on opposite sides of the spacecraft, and whose optical axes were parallel to the spin axis. The bolometers were thermally isolated from but in close proximity to reflecting mirrors so that the hemispheres behaved like isolated spheres in space. The experiment was designed to measure the amount of solar energy absorbed, reflected, and emitted by the earth and its atmosphere in order to calculate the Earth's radiation budget. The data were originally written on IBM 7094 machines, and these have been recovered from magnetic tapes, referred to as the Omnidirectional Radiometer Temperature (ORT) tapes. The data are archived in their text format.\n\nThe TIROS-4 satellite was successfully launched on February 8, 1962. The Low-Resolution Omnidirectional Radiometer experiment returned data for about five months. A previous instrument flew on TIROS-3 and a follow-on instrument was flown on TIROS-7, while a similar instrument flew on Explorer-7.\n\nThe Principal Investigator for these data was Verner E. Suomi from the University of Wisconsin. This product was previously available from the NSSDC with the identifier ESAD-00252 (old id 62-002A-01A).",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "TIROS4L1ORT",
-            "creator": "NASA/GSFC",
-            "title": "TIROS-4 Low-Resolution Omnidirectional Radiometer Level 1 Temperature Data V001 (TIROS4L1ORT) at GES DISC",
-            "graphic-preview-description": "TIROS-4 L1 ORT data showing data coverage and sensor temperatures from the omnidirectional radiometer for orbit 30 on February 10, 1962.",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/TIROS4L1ORT_Sample.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FEGCSHHHVLJKT",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FEGCSHHHVLJKT",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/TIROS4L1ORT_Sample.png",
-                    "description": "TIROS-4 L1 ORT data showing data coverage and sensor temperatures from the omnidirectional radiometer for orbit 30 on February 10, 1962.",
                     "@type": "dcat:Distribution",
+                    "description": "TIROS-4 L1 ORT data showing data coverage and sensor temperatures from the omnidirectional radiometer for orbit 30 on February 10, 1962.",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/TIROS4L1ORT_Sample.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/TIROS/TIROS4L1ORT.001/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/TIROS/TIROS4L1ORT.001/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=TIROS4L1ORT",
-                    "description": "Use the Earthdata Search Client to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search Client to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=TIROS4L1ORT",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/TIROS/TIROS4L1ORT.001/doc/README.TIROSORT.001.pdf",
-                    "description": "README Document",
                     "@type": "dcat:Distribution",
+                    "description": "README Document",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/TIROS/TIROS4L1ORT.001/doc/README.TIROSORT.001.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's read me document"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TIROS/Tiros_Inventory.xlsx",
-                    "description": "TIROS Inventory",
                     "@type": "dcat:Distribution",
+                    "description": "TIROS Inventory",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TIROS/Tiros_Inventory.xlsx",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "graphic-preview-description": "TIROS-4 L1 ORT data showing data coverage and sensor temperatures from the omnidirectional radiometer for orbit 30 on February 10, 1962.",
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/TIROS4L1ORT_Sample.png",
+            "identifier": "C2152905392-GES_DISC",
+            "issued": "2021-08-13",
+            "keyword": [
+                "earth science",
+                "atmosphere",
+                "atmospheric radiation"
+            ],
+            "landingPage": "https://doi.org/10.5067/EGCSHHHVLJKT",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2021-08-13",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
+            },
+            "release-place": "Greenbelt, MD, USA",
+            "series-name": "TIROS4L1ORT",
             "spatial": "-180.0 -82.0 180.0 82.0",
+            "temporal": "1962-02-08T00:00:00Z/1962-06-28T23:59:59.999Z",
             "theme": [
                 "TIROS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "TIROS-4 Low-Resolution Omnidirectional Radiometer Level 1 Temperature Data V001 (TIROS4L1ORT) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/SeaBASS/TAO_MOORINGS/DATA001",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/GSFC/SED/ESD/GCDC/OB.DAAC. https://doi.org/10.5067/SeaBASS/TAO_MOORINGS/DATA001.",
-            "issued": "1992-03-01",
-            "temporal": "1992-03-01T00:00:00Z/2023-04-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-04-06",
-            "keyword": [
-                "ocean chemistry",
-                "oceans",
-                "ocean optics",
-                "earth science",
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
-            "identifier": "C1633360673-OB_DAAC",
             "description": "Mooring data from the TAO buoy array between 1992 and 2002.",
-            "title": "Tropical Atmosphere Ocean (TAO) Moored Buoy Array",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSeaBASS%2FTAO_MOORINGS%2FDATA001",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSeaBASS%2FTAO_MOORINGS%2FDATA001",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://seabass.gsfc.nasa.gov/experiment/TAO_Moorings/",
-                    "description": "Detailed information about the SeaBASS Experiment such as cruises, funding, and investigators",
                     "@type": "dcat:Distribution",
+                    "description": "Detailed information about the SeaBASS Experiment such as cruises, funding, and investigators",
+                    "downloadURL": "https://seabass.gsfc.nasa.gov/experiment/TAO_Moorings/",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 }
             ],
+            "identifier": "C1633360673-OB_DAAC",
+            "issued": "1992-03-01",
+            "keyword": [
+                "ocean chemistry",
+                "oceans",
+                "ocean optics",
+                "earth science",
+                "salinity/density",
+                "ocean temperature"
+            ],
+            "landingPage": "https://doi.org/10.5067/SeaBASS/TAO_MOORINGS/DATA001",
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
+            "temporal": "1992-03-01T00:00:00Z/2023-04-17T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Tropical Atmosphere Ocean (TAO) Moored Buoy Array"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/P4HZB9N27EKU",
             "citation": "John Janowiak, Bob Joyce, Pingping Xie. Andrey Savtchenko. 2017-12-30. GPM_MERGIR. Version 1. NCEP/CPC L3 Half Hourly 4km Global (60S - 60N) Merged IR V1. Greenbelt, MD. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/P4HZB9N27EKU. https://disc.gsfc.nasa.gov/datacollection/GPM_MERGIR_1.html. Digital Science Data.",
-            "issued": "2017-10-10",
-            "temporal": "1998-01-01T00:00:00Z/2022-01-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2017-10-10",
-            "keyword": [
-                "spectral/engineering",
-                "earth science",
-                "atmosphere",
-                "infrared wavelengths",
-                "precipitation"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "PINGPING XIE",
                 "hasEmail": "mailto:Pingping.Xie@noaa.gov"
             },
+            "creator": "John Janowiak, Bob Joyce, Pingping Xie",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C1432254058-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "These data originate from NOAA/NCEP.\n\nThe NOAA Climate Prediction Center/NCEP/NWS is making the data available originally in binary format, in a weekly rotating archive. The NASA GES DISC is acquiring the binary files as they become available, converts them into CF (Climate and Forecast) -convention compliant netCDF-4 format, and stores the product in a permanent archive. It has been the intention to extend the record back to TRMM epoch, and some data are available from 1998. However, currently, the continuous record starts from February, 2000.\n\nThe leading edge of data availability is delayed by about 24 hours from real-time to abide by international data exchange agreements between NOAA and EUMETSAT (the METEOSAT data providers).\n\nThe data contain  globally-merged (60S-60N) 4-km pixel-resolution IR brightness temperature data (equivalent blackbody temps), merged from the European, Japanese, and U.S. geostationary satellites over the period of record (GOES-8/9/10/11/12/13/14/15/16, METEOSAT-5/7/8/9/10, and GMS-5/MTSat-1R/2/Himawari-8).\n\nThe data have been corrected for \"zenith angle dependence\", i.e. IR temperatures for locations far from satellite nadir are erroneously cold due to a combination of geometric effects and radiometric path extinction effects.  This correction allows for the merging of the IR data from the various geostationary satellites with greatly reduced discontinuities at their boundaries.  Some residual differences among the data exist since the IR channels aboard the various spacecraft have slightly different characteristics and no intercalibration among the sensors has been performed. NOAA are in the process of performing such an intercalibration, although this effect is considerably smaller than the zenith angle effects.\n\n\nThe NASA GES DISC is curating these data in a self-documenting, CF-compliant, netCDF-4 format, which allows a broad range of applications to access the data directly, without the need to cope with the original binary data format. In addition to the direct download of netCDF-4 data, the GES DISC provides data download in binary, ASCII, and netCDF-3 formats using the OPeNDAP interface. \n\n\nSimilarities with the original\n-----------------------------\nAs in the original binaries, every netCDF-4 file covers one hour, and contains two half-hourly grids, at 4-km grid cell resolution. \n\n\nDifferences from the original\n-----------------------------\n1. The data in the netCDF-4 files are already converted to real (float) values of Brightness Temperatures in Kelvin. There is no need to further scale these data. The netCDF-4 format is machine-independent and users need not worry about the endian-ness of their machines. \n\n2. To meet the requirements of collection spatial metadata, the grid is re-ordered from the original and now goes from -180 (West) to 180 (East). It is also starting from -60 (South).\n\nThe data and time units are reflected in the corresponding \"units\" attributes, and grid dimensions are described by longitude (\"lon\"), latitude (\"lat\") and \"time\" vectors. Thus, any CF-compliant tool should automatically understand the setup in the data files and the starting time for each half-hourly grid. Even without such tools, simple \"ncdump\" or \"h5dump\" command line tools will easily disclose the netCDF-4 files configuration.\n\n\nAcknowledgements\n------------------\nThe creation of the original data at NOAA/NCEP is supported by funding from the NOAA Office of Global Programs for the Global Precipitation Climatology Project (GPCP) and by NASA via the Tropical Rainfall Measuring Mission (TRMM). \n\nThe permanent archive at GES DISC is supported by NASA's HQ Earth Science Data Systems (ESDS) Program.",
-            "editor": "Andrey Savtchenko",
-            "release-place": "Greenbelt, MD",
-            "series-name": "GPM_MERGIR",
-            "creator": "John Janowiak, Bob Joyce, Pingping Xie",
-            "graphic-preview-description": "Panoply screenshot of Half-Hourly 4-km Merged IR Brightness Temperatures served from GES DISC OPeNDAP",
-            "title": "NCEP/CPC L3 Half Hourly 4km Global (60S - 60N) Merged IR V1 (GPM_MERGIR) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/GPM/browse/GPM_MERGIR.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FP4HZB9N27EKU",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FP4HZB9N27EKU",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/GPM/browse/GPM_MERGIR.png",
-                    "description": "Panoply screenshot of Half-Hourly 4-km Merged IR Brightness Temperatures served from GES DISC OPeNDAP",
                     "@type": "dcat:Distribution",
+                    "description": "Panoply screenshot of Half-Hourly 4-km Merged IR Brightness Temperatures served from GES DISC OPeNDAP",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/GPM/browse/GPM_MERGIR.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/GPM_MERGIR_1.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/GPM_MERGIR_1.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc2.gesdisc.eosdis.nasa.gov/data/MERGED_IR/GPM_MERGIR.1/",
-                    "description": "Access the data via HTTP",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTP",
+                    "downloadURL": "https://disc2.gesdisc.eosdis.nasa.gov/data/MERGED_IR/GPM_MERGIR.1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc2.gesdisc.eosdis.nasa.gov/opendap/MERGED_IR/GPM_MERGIR.1/",
-                    "description": "Access the data via the OPeNDAP protocol",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol",
+                    "downloadURL": "https://disc2.gesdisc.eosdis.nasa.gov/opendap/MERGED_IR/GPM_MERGIR.1/",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=GPM_MERGIR",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=GPM_MERGIR",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
@@ -1045770,1150 +1045744,1178 @@
                     "title": "View this dataset's read me document"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/GPM/CPC-4kmIR-Sats.pdf",
-                    "description": "Geo-IR satellites contained in the Merged 4-km IR Tb dataset provided by NOAA/NWS/CPC ",
                     "@type": "dcat:Distribution",
+                    "description": "Geo-IR satellites contained in the Merged 4-km IR Tb dataset provided by NOAA/NWS/CPC ",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/GPM/CPC-4kmIR-Sats.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "editor": "Andrey Savtchenko",
+            "graphic-preview-description": "Panoply screenshot of Half-Hourly 4-km Merged IR Brightness Temperatures served from GES DISC OPeNDAP",
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/GPM/browse/GPM_MERGIR.png",
+            "identifier": "C1432254058-GES_DISC",
+            "issued": "2017-10-10",
+            "keyword": [
+                "spectral/engineering",
+                "earth science",
+                "atmosphere",
+                "infrared wavelengths",
+                "precipitation"
+            ],
+            "landingPage": "https://doi.org/10.5067/P4HZB9N27EKU",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2017-10-10",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
+            },
+            "release-place": "Greenbelt, MD",
+            "series-name": "GPM_MERGIR",
             "spatial": "-180.0 -60.0 180.0 60.0",
+            "temporal": "1998-01-01T00:00:00Z/2022-01-17T00:00:00Z",
             "theme": [
                 "GPM",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "NCEP/CPC L3 Half Hourly 4km Global (60S - 60N) Merged IR V1 (GPM_MERGIR) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/MRTPR45H95EC",
             "citation": "Kevin W. Bowman. 2021-05-27. TRPSDL2CH4CRSFS. Version 1. TROPESS CrIS-SNPP L2 Methane for Forward Stream, Standard Product V1. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/MRTPR45H95EC. https://disc.gsfc.nasa.gov/datacollection/TRPSDL2CH4CRSFS_1.html. Digital Science Data.",
-            "issued": "2021-05-18",
-            "temporal": "2021-02-01T00:00:00Z/2021-05-21T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2021-05-18",
-            "references": [
-                "https://doi.org/10.1126/sciadv.abf7460",
-                "https://doi.org/10.5194/amt-14-335-2021"
-            ],
-            "keyword": [
-                "earth science",
-                "atmospheric chemistry",
-                "atmosphere"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "KEVIN BOWMAN",
                 "hasEmail": "mailto:kevin.w.bowman@jpl.nasa.gov"
             },
+            "creator": "Kevin W. Bowman",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C2041963510-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "The TROPESS CrIS-SNPP L2 Methane for Forward Stream, Standard Product contains the vertical distribution of the retrieved atmospheric state of methane (CH4), formal uncertainties, and diagnostic information measured by the CrIS instrument on the Suomi-NPP satellite. The forward stream standard product is global for the time period from 2021-02-01 to 2021-05-21, when the CrIS-SNPP processing was discontinued. The NASA TRopospheric Ozone and Precursors from Earth System Sounding (TROPESS) project, uses an optimal estimation algorithm, known as the MUlti-SpEctra, MUlti-SpEcies, Multi-SEnsors (MUSES).\n\nThe data files are written in the netCDF version 4 file format, and each file contains one day of data. The data have a spatial resolution of 14 km (CrIS nadir FOV), and are reported at 26 vertical levels from the surface to 0.1 hPa. The principal investigator for the TROPESS project is Kevin W. Bowman.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "TRPSDL2CH4CRSFS",
-            "creator": "Kevin W. Bowman",
-            "graphic-preview-description": "TROPESS CrIS-SNPP CH4 (Forward Stream, Standard Product) at 383 hPa on 01 April 2021.",
-            "title": "TROPESS CrIS-SNPP L2 Methane for Forward Stream, Standard Product V1 (TRPSDL2CH4CRSFS) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TROPESS/images/TRPSDL2CH4CRSFS_Sample.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMRTPR45H95EC",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMRTPR45H95EC",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TROPESS/images/TRPSDL2CH4CRSFS_Sample.png",
-                    "description": "TROPESS CrIS-SNPP CH4 (Forward Stream, Standard Product) at 383 hPa on 01 April 2021.",
                     "@type": "dcat:Distribution",
+                    "description": "TROPESS CrIS-SNPP CH4 (Forward Stream, Standard Product) at 383 hPa on 01 April 2021.",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TROPESS/images/TRPSDL2CH4CRSFS_Sample.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/TRPSDL2CH4CRSFS_1.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/TRPSDL2CH4CRSFS_1.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/data/TROPESS_Standard/TRPSDL2CH4CRSFS.1/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/data/TROPESS_Standard/TRPSDL2CH4CRSFS.1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=TRPSDL2CH4CRSFS_1",
-                    "description": "Use the Earthdata Search Client to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search Client to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=TRPSDL2CH4CRSFS_1",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/opendap/TROPESS_Standard/TRPSDL2CH4CRSFS.1/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/opendap/TROPESS_Standard/TRPSDL2CH4CRSFS.1/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/data/TROPESS_Standard/TRPSDL2CH4CRSFS.1/doc/TROPESS_Forward_Stream_README.pdf",
-                    "description": "README Document",
                     "@type": "dcat:Distribution",
+                    "description": "README Document",
+                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/data/TROPESS_Standard/TRPSDL2CH4CRSFS.1/doc/TROPESS_Forward_Stream_README.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's read me document"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TROPESS/User_Guides/TROPESS-AIRS-CH4_L2_Product_Quick_Start_User_Guide_20210402.pdf",
-                    "description": "User's Guide",
                     "@type": "dcat:Distribution",
+                    "description": "User's Guide",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TROPESS/User_Guides/TROPESS-AIRS-CH4_L2_Product_Quick_Start_User_Guide_20210402.pdf",
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
+            "graphic-preview-description": "TROPESS CrIS-SNPP CH4 (Forward Stream, Standard Product) at 383 hPa on 01 April 2021.",
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TROPESS/images/TRPSDL2CH4CRSFS_Sample.png",
+            "identifier": "C2041963510-GES_DISC",
+            "issued": "2021-05-18",
+            "keyword": [
+                "earth science",
+                "atmospheric chemistry",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.5067/MRTPR45H95EC",
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
+                "https://doi.org/10.5194/amt-14-335-2021"
+            ],
+            "release-place": "Greenbelt, MD, USA",
+            "series-name": "TRPSDL2CH4CRSFS",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2021-02-01T00:00:00Z/2021-05-21T23:59:59.999Z",
             "theme": [
                 "TROPESS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "TROPESS CrIS-SNPP L2 Methane for Forward Stream, Standard Product V1 (TRPSDL2CH4CRSFS) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=LRO-L-LROC-5-RDR-V1.0",
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
+            "description": "This data set comprises calibrated data from the LROC NAC and WAC cameras. The science data is comprised of calibrated raw images, along with pointing data and housekeeping information.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.lro-l-lroc-5-rdr-v1.0_ksdr-nni8",
+            "issued": "2018-06-26",
+            "keyword": [
+                "lunar reconnaissance orbiter",
+                "moon"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=LRO-L-LROC-5-RDR-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.lro-l-lroc-5-rdr-v1.0_ksdr-nni8",
-            "description": "This data set comprises calibrated data from the LROC NAC and WAC cameras. The science data is comprised of calibrated raw images, along with pointing data and housekeeping information.",
-            "title": "LRO MOON LROC 5 RDR V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "LRO MOON LROC 5 RDR V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-P-SWAP-5-DERIVED-SOLARWIND-V1.0",
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
-                "new horizons"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This data set presents characteristics of the solar wind derived from data taken by the New Horizons Solar Wind Around Pluto (SWAP) instrument during the Pluto encounter. This archive contains two data products. Each product compiles the CODMAC level 2 source data used, the solar wind speed, proton density, proton speed, proton temerature, proton dynamic pressure, proton thermal pressure, spacecraft position and speed. The two product files differ in that one is in Heliographic Inertial (HGI) coordinates and the other is in Pluto centric J2000 and IAU J2000 coordinates.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-p-swap-5-derived-solarwind-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "new horizons"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-P-SWAP-5-DERIVED-SOLARWIND-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-p-swap-5-derived-solarwind-v1.0",
-            "description": "This data set presents characteristics of the solar wind derived from data taken by the New Horizons Solar Wind Around Pluto (SWAP) instrument during the Pluto encounter. This archive contains two data products. Each product compiles the CODMAC level 2 source data used, the solar wind speed, proton density, proton speed, proton temerature, proton dynamic pressure, proton thermal pressure, spacecraft position and speed. The two product files differ in that one is in Heliographic Inertial (HGI) coordinates and the other is in Pluto centric J2000 and IAU J2000 coordinates.",
-            "title": "NEW HORIZONS SWAP DERIVED SOLAR WIND AT PLUTO V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "NEW HORIZONS SWAP DERIVED SOLAR WIND AT PLUTO V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG2-J-PLS-5-SUMM-ION-INBNDSWIND-96S-V1.0",
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
-                "jupiter"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This data set contains solar wind plasma data upstream of Jupiter before the Voyager 2 encounter. Fit and moment parameters are given; the fit parameters assume a convected isotropic proton Maxwellian distribution. Use of fit parameters is recommended as these are normally more accurate. Since only the first 72 or last 72 energy/charge channels are telemetered to Earth from each M-mode spectra, derived parameters change significantly only every other set of spectra so the effective time resolution is 196 s.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg2-j-pls-5-summ-ion-inbndswind-96s-v1.0_ksiv-4tc4",
+            "issued": "2021-05-21",
+            "keyword": [
+                "voyager",
+                "jupiter"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG2-J-PLS-5-SUMM-ION-INBNDSWIND-96S-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg2-j-pls-5-summ-ion-inbndswind-96s-v1.0_ksiv-4tc4",
-            "description": "This data set contains solar wind plasma data upstream of Jupiter before the Voyager 2 encounter. Fit and moment parameters are given; the fit parameters assume a convected isotropic proton Maxwellian distribution. Use of fit parameters is recommended as these are normally more accurate. Since only the first 72 or last 72 energy/charge channels are telemetered to Earth from each M-mode spectra, derived parameters change significantly only every other set of spectra so the effective time resolution is 196 s.",
-            "title": "VG2 JUP PLS DERIVED ION INBOUND SOLAR\nWIND 96SEC V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "VG2 JUP PLS DERIVED ION INBOUND SOLAR\nWIND 96SEC V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/MEASURES/DMSP-F16/SSMIS/DATA301",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Wentz, Frank J, Kyle Hilburn and Deborah K Smith.2012. RSS SSMIS OCEAN PRODUCT GRIDS DAILY FROM DMSP F16 NETCDF [indicate subset used]. Dataset available online from the NASA Global Hydrometeorology Resource Center DAAC, Huntsville, Alabama, U.S.A. DOI: http://dx.doi.org/10.5067/MEASURES/DMSP-F16/SSMIS/DATA301",
-            "issued": "2012-10-01",
-            "temporal": "2003-10-26T00:00:00Z/2022-05-03T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-04-28",
-            "keyword": [
-                "oceans",
-                "precipitation",
-                "earth science",
-                "ocean winds",
-                "clouds",
-                "atmospheric winds",
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
-            "identifier": "C1996546500-GHRC_DAAC",
             "description": "The RSS SSMIS Ocean Product Grids Daily from DMSP F16 netCDF dataset is part of the collection of Special Sensor Microwave/Imager (SSM/I) and Special Sensor Microwave Imager Sounder (SSMIS) data products produced as part of NASA's MEaSUREs Program. Remote Sensing Systems generates SSM/I and SSMIS binary data products using a unified, physically based algorithm to simultaneously retrieve ocean wind speed, water vapor, cloud water, and rain rate. The SSMIS data have been carefully intercalibrated to the brightness temperature level of the previous SSM/I and therefore extend this important time series of ocean winds, vapor, cloud and rain values. This algorithm is a product of 20 years of refinements, improvements, and verifications. The Global Hydrology Resource Center has reformatted the binary data into a netCDF data product for each temporal group for each satellite. The netCDF SSMI/SSMIS collection will be available for F16 daily.",
-            "graphic-preview-description": "N/A",
-            "title": "RSS SSMIS OCEAN PRODUCT GRIDS DAILY FROM DMSP F16 NETCDF V7",
-            "graphic-preview-file": "https://ghrc.nsstc.nasa.gov/pub/ssmis/f16/daily/browse/",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMEASURES%2FDMSP-F16%2FSSMIS%2FDATA301",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMEASURES%2FDMSP-F16%2FSSMIS%2FDATA301",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=rssmif16d",
-                    "description": "Files may be downloaded directly to your workstation from this link",
                     "@type": "dcat:Distribution",
+                    "description": "Files may be downloaded directly to your workstation from this link",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=rssmif16d",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/ssmis/f16/daily/browse/2008/f16_ssmis_20080101v7_A_CW.png",
-                    "description": "Sample browse image",
                     "@type": "dcat:Distribution",
+                    "description": "Sample browse image",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/ssmis/f16/daily/browse/2008/f16_ssmis_20080101v7_A_CW.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/ssmis/f16/daily/browse/2008/f16_ssmis_20080101v7_A_WS.png",
-                    "description": "Sample browse image",
                     "@type": "dcat:Distribution",
+                    "description": "Sample browse image",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/ssmis/f16/daily/browse/2008/f16_ssmis_20080101v7_A_WS.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/ssmis/f16/daily/browse/2008/f16_ssmis_20080101v7_A_WV.png",
-                    "description": "Sample browse image",
                     "@type": "dcat:Distribution",
+                    "description": "Sample browse image",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/ssmis/f16/daily/browse/2008/f16_ssmis_20080101v7_A_WV.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/ssmis/f16/daily/browse/2008/f16_ssmis_20080101v7_A_RR.png",
-                    "description": "Sample browse image",
                     "@type": "dcat:Distribution",
+                    "description": "Sample browse image",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/ssmis/f16/daily/browse/2008/f16_ssmis_20080101v7_A_RR.png",
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
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/doc/ssmi_netcdf/ssmi.pdf",
-                    "description": "A Well Calibrated Ocean Algorithm for SSM/I",
                     "@type": "dcat:Distribution",
+                    "description": "A Well Calibrated Ocean Algorithm for SSM/I",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/doc/ssmi_netcdf/ssmi.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View the primary investigator's documentation for this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/opendap/ssmis/f16/daily/data/",
-                    "description": "OPeNDAP server dataset access",
                     "@type": "dcat:Distribution",
+                    "description": "OPeNDAP server dataset access",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/opendap/ssmis/f16/daily/data/",
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
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/ssmis/f16/daily/browse/",
-                    "description": "N/A",
                     "@type": "dcat:Distribution",
+                    "description": "N/A",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/ssmis/f16/daily/browse/",
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
+            "graphic-preview-file": "https://ghrc.nsstc.nasa.gov/pub/ssmis/f16/daily/browse/",
+            "identifier": "C1996546500-GHRC_DAAC",
+            "issued": "2012-10-01",
+            "keyword": [
+                "oceans",
+                "precipitation",
+                "earth science",
+                "ocean winds",
+                "clouds",
+                "atmospheric winds",
+                "atmospheric water vapor",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.5067/MEASURES/DMSP-F16/SSMIS/DATA301",
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
+            "temporal": "2003-10-26T00:00:00Z/2022-05-03T00:00:00Z",
             "theme": [
                 "DISCOVER",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "RSS SSMIS OCEAN PRODUCT GRIDS DAILY FROM DMSP F16 NETCDF V7"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-PRL-0222-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the PRELANDING phase 2014-01-21 to 2014-11-18. It is a Global Gravity measurement at the comet 67P and covers the time 2014-08-19T13:24:05.000 to 2014-08-19T18:43:26.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-prl-0222-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-PRL-0222-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-prl-0222-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the PRELANDING phase 2014-01-21 to 2014-11-18. It is a Global Gravity measurement at the comet 67P and covers the time 2014-08-19T13:24:05.000 to 2014-08-19T18:43:26.000.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     PRELANDING 0222 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     PRELANDING 0222 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/SWOT-NALT-GDR-2.0",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Surface Water Ocean Topography (SWOT). 2023-06-01. SWOT Level 2 Nadir Altimeter Geophysical Data Record with Waveforms - GDR. Version 2.0. SWOT Level 2 Nadir Altimeter Geophysical Data Record with Waveforms - GDR, Version 2.0. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/JPL/PODAAC. https://doi.org/10.5067/SWOT-NALT-GDR-2.0.",
-            "issued": "2022-06-28",
-            "temporal": "2022-12-16T00:00:00Z/2024-03-27T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-06-28",
-            "keyword": [
-                "earth science",
-                "oceans",
-                "ocean waves",
-                "sea surface topography"
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
-            "identifier": "C2799465509-POCLOUD",
-            "description": "The SWOT Level 2 Nadir Altimeter Geophysical Data Record (GDR) with Waveforms dataset produced by the Surface Water and Ocean Topography (SWOT) mission provides sea surface height, significant wave height and wind speed measurements from the Poseidon-3C nadir altimeter, a Jason-class dual frequency (Ku/C) altimeter. SWOT is a joint mission between NASA and CNES that launched on December 16, 2022. It aims to measure ocean surface topography with unprecedented resolution and accuracy, as well as map inland water bodies globally. The GDR dataset consists of discrete measurements for each half orbit along the ground track with sampling resolutions of approximately 6-km and 300-m at 1Hz and 20Hz, respectively. The data were processed using restituted auxiliary data and the Precise Orbit Ephemeris (POE). The data are available with latency of < 90 days and distributed in netCDF-4 file format.\r\n<br>This collection is a sub-collection of its parent: https://podaac.jpl.nasa.gov/dataset/SWOT_L2_NALT_GDR_2.0",
-            "series-name": "SWOT Level 2 Nadir Altimeter Geophysical Data Record with Waveforms - GDR",
-            "graphic-preview-description": "Thumbnail",
             "creator": "Surface Water Ocean Topography (SWOT)",
-            "title": "SWOT Level 2 Nadir Altimeter Geophysical Data Record with Waveforms - GDR",
-            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/SWOT_L2_NALT_GDR_2.0.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The SWOT Level 2 Nadir Altimeter Geophysical Data Record (GDR) with Waveforms dataset produced by the Surface Water and Ocean Topography (SWOT) mission provides sea surface height, significant wave height and wind speed measurements from the Poseidon-3C nadir altimeter, a Jason-class dual frequency (Ku/C) altimeter. SWOT is a joint mission between NASA and CNES that launched on December 16, 2022. It aims to measure ocean surface topography with unprecedented resolution and accuracy, as well as map inland water bodies globally. The GDR dataset consists of discrete measurements for each half orbit along the ground track with sampling resolutions of approximately 6-km and 300-m at 1Hz and 20Hz, respectively. The data were processed using restituted auxiliary data and the Precise Orbit Ephemeris (POE). The data are available with latency of < 90 days and distributed in netCDF-4 file format.\r\n<br>This collection is a sub-collection of its parent: https://podaac.jpl.nasa.gov/dataset/SWOT_L2_NALT_GDR_2.0",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSWOT-NALT-GDR-2.0",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSWOT-NALT-GDR-2.0",
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
-                    "downloadURL": "https://swot.jpl.nasa.gov",
-                    "description": "SWOT Mission Page",
                     "@type": "dcat:Distribution",
+                    "description": "SWOT Mission Page",
+                    "downloadURL": "https://swot.jpl.nasa.gov",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
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
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2799465509-POCLOUD",
-                    "description": "HTTPS endpoint for data browse and download",
                     "@type": "dcat:Distribution",
+                    "description": "HTTPS endpoint for data browse and download",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2799465509-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2799465509-POCLOUD",
-                    "description": "Browse granule search results in Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse granule search results in Earthdata Search",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2799465509-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/SWOT_L2_NALT_GDR_2.0.jpg",
-                    "description": "Thumbnail",
                     "@type": "dcat:Distribution",
+                    "description": "Thumbnail",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/SWOT_L2_NALT_GDR_2.0.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/web-misc/swot_mission_docs/pdd/SALP-ST-M-EA-17043-CN_0103_20220411_Rev1.3.pdf",
-                    "description": "Product Description Document (PDD)",
                     "@type": "dcat:Distribution",
+                    "description": "Product Description Document (PDD)",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/web-misc/swot_mission_docs/pdd/SALP-ST-M-EA-17043-CN_0103_20220411_Rev1.3.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
                 }
             ],
-            "spatial": "-180.0 -77.6 180.0 77.6",
-            "theme": [
-                "SWOT",
-                "geospatial"
+            "graphic-preview-description": "Thumbnail",
+            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/SWOT_L2_NALT_GDR_2.0.jpg",
+            "identifier": "C2799465509-POCLOUD",
+            "issued": "2022-06-28",
+            "keyword": [
+                "earth science",
+                "oceans",
+                "ocean waves",
+                "sea surface topography"
             ],
+            "landingPage": "https://doi.org/10.5067/SWOT-NALT-GDR-2.0",
             "language": [
                 "en-US"
-            ]
-        },
-        {
-            "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/NPP/CERES/SSF_NPP-FM5_L2.002A",
-            "bureauCode": [
-                "026:00"
             ],
-            "citation": "2020-09-15. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/NPP/CERES/SSF_NPP-FM5_L2.002A.",
-            "issued": "2023-01-15",
-            "temporal": "2012-01-27T00:00:00Z/2023-03-01T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-02-08",
-            "keyword": [
-                "aerosols",
-                "atmosphere",
-                "atmospheric radiation",
-                "clouds",
-                "lidar",
-                "earth science",
-                "infrared wavelengths",
-                "land surface",
-                "surface radiative properties",
-                "spectral/engineering"
+            "modified": "2022-06-28",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/JPL/PODAAC"
+            },
+            "series-name": "SWOT Level 2 Nadir Altimeter Geophysical Data Record with Waveforms - GDR",
+            "spatial": "-180.0 -77.6 180.0 77.6",
+            "temporal": "2022-12-16T00:00:00Z/2024-03-27T00:00:00Z",
+            "theme": [
+                "SWOT",
+                "geospatial"
+            ],
+            "title": "SWOT Level 2 Nadir Altimeter Geophysical Data Record with Waveforms - GDR"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "026:00"
             ],
+            "citation": "2020-09-15. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/NPP/CERES/SSF_NPP-FM5_L2.002A.",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "DAVID, DR. KRATZ",
                 "hasEmail": "mailto:david.p.kratz@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/LARC/SD/ASDC"
-            },
-            "identifier": "C2246001739-LARC_ASDC",
             "description": "CER_SSF_NPP-FM5_Edition2A data are CERES observed TOA fluxes, MODIS clouds and aerosols, and parameterized surface fluxes.The Single Scanner Footprint TOA/Surface Fluxes and Clouds (SSF) product contains one hour of instantaneous Clouds and the Earth's Radiant Energy System (CERES) data for a single scanner instrument. The SSF combines instantaneous CERES data with scene information from a higher-resolution imager such as Visible/Infrared Scanner (VIRS) on TRMM, Moderate-Resolution Imaging Spectroradiometer (MODIS) on Terra and Aqua, or Visible Infrare Imaging Radiometer Suite (VIIRS) on S-NPP and NOAA-20. Scene identification and cloud properties are defined at the higher imager resolution and these data are averaged over the larger CERES footprint. For each CERES footprint, the SSF contains the number of cloud layers and for each layer the cloud amount, height, temperature, pressure, optical depth, emissivity, ice and liquid water path, and water particle size. The SSF also contains the CERES filtered radiances for the total, shortwave (SW), and window (WN) channels and the unfiltered SW, longwave (LW), and WN radiances. The SW, LW, and WN radiances at spacecraft altitude are converted to Top-of-the-Atmosphere (TOA) fluxes based on the imager defined scene. These TOA fluxes are used to estimate surface fluxes. Only footprints with adequate imager coverage are included on CER_SSF_TRMM-PFM-VIRS_Subset_Edition1 the SSF which is much less than the full set of footprints on the CERES ES-8 product. CERES is a key component of the Earth Observing System (EOS) program. The CERES instruments provide radiometric measurements of the Earth's atmosphere from three broadband channels. The CERES missions are a follow-on to the successful Earth Radiation Budget Experiment (ERBE) mission. The first CERES instrument (PFM) was launched on November 27, 1997 as part of the Tropical Rainfall Measuring Mission (TRMM). Two CERES instruments (FM1 and FM2) were launched into polar orbit on board the EOS flagship Terra on December 18, 1999. Two additional CERES instruments (FM3 and FM4) were launched on board EOS Aqua on May 4, 2002. The CERES instrument (FM5) was launched on board the Suomi National Polar-orbiting Partnership (NPP) satellite on October 28, 2011. The newest CERES instrument (FM6) was launched on board the Joint Polar-Orbiting Satellite System 1 (JPSS-1) satellite on November 18, 2017.",
-            "title": "CERES Single Scanner Footprint (SSF) TOA/Surface Fluxes, Clouds and Aerosols NPP-FM5 Edition2A",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FNPP%2FCERES%2FSSF_NPP-FM5_L2.002A",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FNPP%2FCERES%2FSSF_NPP-FM5_L2.002A",
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
-                    "downloadURL": "https://doi.org/10.5067/NPP/CERES/SSF_NPP-FM5_L2.002A",
-                    "description": "DOI data set landing page for CER_SSF_NPP-FM5-VIIRS_Edition2A",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for CER_SSF_NPP-FM5-VIIRS_Edition2A",
+                    "downloadURL": "https://doi.org/10.5067/NPP/CERES/SSF_NPP-FM5_L2.002A",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/ceres/readme/DPC_SSF-Ed4_R5V1.pdf",
-                    "description": "CERES Data Products Catalog for Edition4-1 Single Scanner Footprint TOA/Surface Fluxes and Clouds (SSF)",
                     "@type": "dcat:Distribution",
+                    "description": "CERES Data Products Catalog for Edition4-1 Single Scanner Footprint TOA/Surface Fluxes and Clouds (SSF)",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/ceres/readme/DPC_SSF-Ed4_R5V1.pdf",
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
-                    "downloadURL": "https://ceres.larc.nasa.gov/documents/collect_guide/pdf/SSF_CG_R2V1.pdf",
-                    "description": "Single Satellite Footprint TOA/Surface Fluxes and Clouds (SSF) Collection Document Release 2 Version 1",
                     "@type": "dcat:Distribution",
+                    "description": "Single Satellite Footprint TOA/Surface Fluxes and Clouds (SSF) Collection Document Release 2 Version 1",
+                    "downloadURL": "https://ceres.larc.nasa.gov/documents/collect_guide/pdf/SSF_CG_R2V1.pdf",
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
-                    "downloadURL": "https://ceres.larc.nasa.gov/documents/DQ_summaries/CER_SSF_NPP_Edition2A.pdf",
-                    "description": "Quality Summary: CERES_SSF_NPP Edition 2A (3/17/2022)",
                     "@type": "dcat:Distribution",
+                    "description": "Quality Summary: CERES_SSF_NPP Edition 2A (3/17/2022)",
+                    "downloadURL": "https://ceres.larc.nasa.gov/documents/DQ_summaries/CER_SSF_NPP_Edition2A.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's product quality assessment"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/ceres/guide/cer_ssf.pdf",
-                    "description": "CERES Single Scanner Footprint TOA/Surface Fluxes and Clouds (SSF) Data Set Abstract",
                     "@type": "dcat:Distribution",
+                    "description": "CERES Single Scanner Footprint TOA/Surface Fluxes and Clouds (SSF) Data Set Abstract",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/ceres/guide/cer_ssf.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
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
-                    "downloadURL": "https://subset.larc.nasa.gov/ceres/",
-                    "description": "CERES\u00a0Search and Subsetting Web Application",
                     "@type": "dcat:Distribution",
+                    "description": "CERES\u00a0Search and Subsetting Web Application",
+                    "downloadURL": "https://subset.larc.nasa.gov/ceres/",
+                    "mediaType": "text/html",
                     "title": "Subset this dataset using a web based subsetter"
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
-                    "downloadURL": "https://ceres.larc.nasa.gov/instruments/satellite-missions/#npp",
-                    "description": "CERES Overview of NPP",
                     "@type": "dcat:Distribution",
+                    "description": "CERES Overview of NPP",
+                    "downloadURL": "https://ceres.larc.nasa.gov/instruments/satellite-missions/#npp",
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
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/ceres/readme/readme_cer_ssf_SampleRead_R3-358.txt",
-                    "description": "Sample read software for CERES SSF Data Products",
                     "@type": "dcat:Distribution",
+                    "description": "Sample read software for CERES SSF Data Products",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/ceres/readme/readme_cer_ssf_SampleRead_R3-358.txt",
+                    "mediaType": "text/html",
                     "title": "View this dataset's read me document"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/ceres/readme/readme_flash_ssf_SampleRead_R4-555.txt",
-                    "description": "Readme Information on FLASH SSF Terra and Aqua",
                     "@type": "dcat:Distribution",
+                    "description": "Readme Information on FLASH SSF Terra and Aqua",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/ceres/readme/readme_flash_ssf_SampleRead_R4-555.txt",
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
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2246001739-LARC_ASDC",
-                    "description": "Earthdata Search for CER_SSF_NPP-FM5-VIIRS_Edition2A (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for CER_SSF_NPP-FM5-VIIRS_Edition2A (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2246001739-LARC_ASDC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/CERES/SSF/NPP-FM5-VIIRS_Edition2A/",
-                    "description": "ASDC Direct Data Download for CER_SSF_NPP-FM5-VIIRS_Edition2A",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for CER_SSF_NPP-FM5-VIIRS_Edition2A",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/CERES/SSF/NPP-FM5-VIIRS_Edition2A/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/CERES/SSF/NPP-FM5-VIIRS_Edition2A/contents.html",
-                    "description": "OPeNDAP data access for CER_SSF_NPP-FM5-VIIRS_Edition2A",
                     "@type": "dcat:Distribution",
+                    "description": "OPeNDAP data access for CER_SSF_NPP-FM5-VIIRS_Edition2A",
+                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/CERES/SSF/NPP-FM5-VIIRS_Edition2A/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 }
             ],
+            "identifier": "C2246001739-LARC_ASDC",
+            "issued": "2023-01-15",
+            "keyword": [
+                "aerosols",
+                "atmosphere",
+                "atmospheric radiation",
+                "clouds",
+                "lidar",
+                "earth science",
+                "infrared wavelengths",
+                "land surface",
+                "surface radiative properties",
+                "spectral/engineering"
+            ],
+            "landingPage": "https://doi.org/10.5067/NPP/CERES/SSF_NPP-FM5_L2.002A",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2023-02-08",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/LARC/SD/ASDC"
+            },
             "spatial": "<?xml version=\"1.0\" encoding=\"UTF-8\"?><gml:Polygon xmlns:gml=\"http://www.opengis.net/gml/3.2\" srsName=\"EPSG:9825\"><gml:outerBoundaryIs><gml:LinearRing><gml:posList>-90.0 -180.0 -90.0 180.0 90.0 180.0 90.0 -180.0 -90.0 -180.0</gml:posList></gml:LinearRing></gml:outerBoundaryIs><gml:innerBoundaryIs></gml:innerBoundaryIs></gml:Polygon>",
+            "temporal": "2012-01-27T00:00:00Z/2023-03-01T00:00:00Z",
             "theme": [
                 "CERES",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "CERES Single Scanner Footprint (SSF) TOA/Surface Fluxes, Clouds and Aerosols NPP-FM5 Edition2A"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/GFLND-3J634",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Felix Landerer. 2023-02-21. JPL TELLUS GRACE-FO Level-3 Monthly Land Water-Equivalent-Thickness. Version RL06.3v04. JPL TELLUS GRACE-FO Level-3 Monthly Land Water-Equivalent-Thickness Surface Mass Anomaly Release 6.3 version 04. JPL. Archived by National Aeronautics and Space Administration, U.S. Government, PO.DAAC. https://doi.org/10.5067/GFLND-3J634.",
-            "issued": "2021-03-10",
-            "temporal": "2018-05-22T00:00:00Z/2024-09-16T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2021-03-10",
-            "keyword": [
-                "water budget",
-                "earth science",
-                "terrestrial hydrosphere"
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
-            "identifier": "C3193302127-POCLOUD",
-            "description": "This data set is produced by the Jet Propulsion Laboratory (JPL) as part of the GRACE-FO (Gravity Recovery and Climate Experiment Follow-On) program and derives the terrestrial water storage anomaly given as equivalent water thickness. These monthly grids are derived from GRACE-FO time-variable gravity observations during the specified timespan, and relative to the specified time-mean reference period. This quantity represents the total terrestrial water storage anomalies from soil moisture, snow, surface water (incl. rivers, lakes, reservoirs etc.), as well as groundwater and aquifers. A glacial isostatic adjustment (GIA) correction has been applied, and standard corrections for geocenter (degree-1), C20 (degree-20) and C30 (degree-30) are incorporated. Post-processing filters have been applied to reduce correlated errors. Data grids are provided in ASCII/netCDF/GeoTIFF formats. <br><br>\r\n\r\nGRACE-FO was launched on 22 May 2018, and extends the original GRACE mission (2002 \u2013 2017) and expands its legacy of scientific achievements in tracking earth surface mass changes. Version 04 (v04) of the terrestrial water storage data uses updated and consistent C20 and Geocenter corrections (i.e., Technical Notes TN-14 and TN-13), as well as an ellipsoidal correction to account for the non-spherical shape of the Earth when mapping gravity anomalies to surface mass change. Additionally, this RL06.3 is an updated release of the previous RL06.1. It differs from RL06.1 only in the Level-1B accelerometer transplant data that is used for the GF2 (GRACE-FO 2) satellite; see respective L-2 data descriptions. RL06.3 uses the ACX2-L1B data products. All GRACE-FO RL06.3 Level-3 fields are fully compatible with the GRACE RL06 data.",
-            "release-place": "JPL",
-            "series-name": "JPL TELLUS GRACE-FO Level-3 Monthly Land Water-Equivalent-Thickness",
-            "graphic-preview-description": "Thumbnail",
             "creator": "Felix Landerer",
-            "title": "JPL TELLUS GRACE-FO Level-3 Monthly Land Water-Equivalent-Thickness Surface Mass Anomaly Release 6.3 version 04",
-            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/TELLUS_GRFO_L3_JPL_RL06_LND_v04.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "This data set is produced by the Jet Propulsion Laboratory (JPL) as part of the GRACE-FO (Gravity Recovery and Climate Experiment Follow-On) program and derives the terrestrial water storage anomaly given as equivalent water thickness. These monthly grids are derived from GRACE-FO time-variable gravity observations during the specified timespan, and relative to the specified time-mean reference period. This quantity represents the total terrestrial water storage anomalies from soil moisture, snow, surface water (incl. rivers, lakes, reservoirs etc.), as well as groundwater and aquifers. A glacial isostatic adjustment (GIA) correction has been applied, and standard corrections for geocenter (degree-1), C20 (degree-20) and C30 (degree-30) are incorporated. Post-processing filters have been applied to reduce correlated errors. Data grids are provided in ASCII/netCDF/GeoTIFF formats. <br><br>\r\n\r\nGRACE-FO was launched on 22 May 2018, and extends the original GRACE mission (2002 \u2013 2017) and expands its legacy of scientific achievements in tracking earth surface mass changes. Version 04 (v04) of the terrestrial water storage data uses updated and consistent C20 and Geocenter corrections (i.e., Technical Notes TN-14 and TN-13), as well as an ellipsoidal correction to account for the non-spherical shape of the Earth when mapping gravity anomalies to surface mass change. Additionally, this RL06.3 is an updated release of the previous RL06.1. It differs from RL06.1 only in the Level-1B accelerometer transplant data that is used for the GF2 (GRACE-FO 2) satellite; see respective L-2 data descriptions. RL06.3 uses the ACX2-L1B data products. All GRACE-FO RL06.3 Level-3 fields are fully compatible with the GRACE RL06 data.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGFLND-3J634",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGFLND-3J634",
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
-                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/TELLUS_GRFO_L3_JPL_RL06_LND_v04.jpg",
-                    "description": "Thumbnail",
                     "@type": "dcat:Distribution",
+                    "description": "Thumbnail",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/TELLUS_GRFO_L3_JPL_RL06_LND_v04.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
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
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C3193302127-POCLOUD",
-                    "description": "HTTPS endpoint for data browse and download",
                     "@type": "dcat:Distribution",
+                    "description": "HTTPS endpoint for data browse and download",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C3193302127-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C3193302127-POCLOUD",
-                    "description": "Browse granule search results in Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse granule search results in Earthdata Search",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C3193302127-POCLOUD",
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
+            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/TELLUS_GRFO_L3_JPL_RL06_LND_v04.jpg",
+            "identifier": "C3193302127-POCLOUD",
+            "issued": "2021-03-10",
+            "keyword": [
+                "water budget",
+                "earth science",
+                "terrestrial hydrosphere"
+            ],
+            "landingPage": "https://doi.org/10.5067/GFLND-3J634",
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
+            "series-name": "JPL TELLUS GRACE-FO Level-3 Monthly Land Water-Equivalent-Thickness",
             "spatial": "-180.0 -89.5 180.0 89.5",
+            "temporal": "2018-05-22T00:00:00Z/2024-09-16T00:00:00Z",
             "theme": [
                 "GRACE-FO",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "JPL TELLUS GRACE-FO Level-3 Monthly Land Water-Equivalent-Thickness Surface Mass Anomaly Release 6.3 version 04"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-4-PRL-67PCHURYUMOV-M02-V2.0",
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
+            "description": "This CODMAC level 4 data set contains radiometric calibrated and geometric distortion corrected (resampled) image data in W/m^2/sr/nm, acquired by the OSIRIS Wide Angle Camera on the Rosetta spacecraft during the PRELANDING mission phase, covering the period from 2014-01-20T10:00:00.000 to 2014-05-07T12:47:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V2.0 supersedes previous deliveries of the same dataset with the following changes since the last version: Lien corrected dataset after October 2018 PSA/PDS external peer review. Updated documentation and ancillary files, added document on bandpass filter. Updated SCIENCE_USER_GUIDE_V03.PDF to include one section about FAQ and one section about image data quality. Added shutter backtravel and readout issues to image quality map. Updated DATA_QUALITY_ID keyword in image header. Improved handling of images with missing packets.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-4-prl-67pchuryumov-m02-v2.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-4-PRL-67PCHURYUMOV-M02-V2.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-4-prl-67pchuryumov-m02-v2.0",
-            "description": "This CODMAC level 4 data set contains radiometric calibrated and geometric distortion corrected (resampled) image data in W/m^2/sr/nm, acquired by the OSIRIS Wide Angle Camera on the Rosetta spacecraft during the PRELANDING mission phase, covering the period from 2014-01-20T10:00:00.000 to 2014-05-07T12:47:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V2.0 supersedes previous deliveries of the same dataset with the following changes since the last version: Lien corrected dataset after October 2018 PSA/PDS external peer review. Updated documentation and ancillary files, added document on bandpass filter. Updated SCIENCE_USER_GUIDE_V03.PDF to include one section about FAQ and one section about image data quality. Added shutter backtravel and readout issues to image quality map. Updated DATA_QUALITY_ID keyword in image header. Improved handling of images with missing packets.",
-            "title": "ROSETTA-ORBITER 67P OSIWAC 4 PRL-MTP002 RDR V2.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P OSIWAC 4 PRL-MTP002 RDR V2.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-PRL-0350-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the PRELANDING phase 2014-01-21 to 2014-11-18. It is a Global Gravity measurement at the comet 67P and covers the time 2014-10-11T15:39:20.000 to 2014-10-11T22:16:02.500.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-prl-0350-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-PRL-0350-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-prl-0350-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the PRELANDING phase 2014-01-21 to 2014-11-18. It is a Global Gravity measurement at the comet 67P and covers the time 2014-10-11T15:39:20.000 to 2014-10-11T22:16:02.500.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     PRELANDING 0350 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     PRELANDING 0350 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/Lidar/Ozone/TOLNet/NASA-JPL",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2022-12-13. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/Lidar/Ozone/TOLNet/NASA-JPL\r\n.",
-            "issued": "2022-09-21",
-            "temporal": "2011-01-27T00:00:00Z/2023-02-28T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-12-13",
-            "keyword": [
-                "earth science",
-                "atmospheric temperature",
-                "atmospheric pressure",
-                "atmosphere",
-                "atmospheric chemistry"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Leblanc Thierry",
                 "hasEmail": "mailto:thierry.leblanc@jpl.nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/LARC/SD/ASDC"
-            },
-            "identifier": "C2565841261-LARC_ASDC",
             "description": "TOLNet_JPL_Data is the lidar data collected by the Table Mountain Facility (TMF) tropospheric ozone lidar system at the NASA Jet Propulsion Laboratory (JPL) as part of the Tropospheric Ozone Lidar Network (TOLNet). Data collection for this product is ongoing.\r\n\r\nIn the troposphere, ozone is considered a pollutant and is important to understand due to its harmful effects on human health and vegetation. Tropospheric ozone is also significant for its impact on climate as a greenhouse gas. Operating since 2011, TOLNet is an interagency collaboration between NASA, NOAA, and the EPA designed to perform studies of air quality and atmospheric modeling as well as validation and interpretation of satellite observations. TOLNet is currently comprised of six Differential Absorption Lidars (DIAL). Each of the lidars are unique, and some have had a long history of ozone observations prior to joining the network. Five lidars are mobile systems that can be deployed at remote locations to support field campaigns. This includes the Langley Mobile Ozone Lidar (LMOL) at NASA Langley Research Center (LaRC), the Tropospheric Ozone (TROPOZ) lidar at the Goddard Space Flight Center (GSFC), the Tunable Optical Profile for Aerosol and oZone (TOPAZ) lidar at the NOAA Chemical Sciences Laboratory (CSL) in Boulder, Colorado, the Autonomous Mobile Ozone LIDAR instrument for Tropospheric Experiments (AMOLITE) lidar at Environment and Climate Change Canada (ECCC) in Toronto, Canada, and the Rocket-city O3 Quality Evaluation in the Troposphere (RO3QET) lidar at the University of Alabama in Huntsville, Alabama. The remaining lidar, the Table Mountain Facility (TMF) tropospheric ozone lidar system located at the NASA Jet Propulsion Laboratory (JPL), is a fixed system.\r\n\r\nTOLNet seeks to address three science objectives. The primary objective of the network is to provide high spatio-temporal measurements of ozone from near the surface to the top of the troposphere. Detailed observations of ozone structure allow science teams and the modeling community to better understand ozone in the lower-atmosphere and to assess the accuracy and vertical resolution with which geosynchronous instruments could retrieve the observed laminar ozone structures. Another objective of TOLNet is to identify an ozone lidar instrument design that would be suitable to address the needs of NASA, NOAA, and EPA air quality scientists who express a desire for these ozone profiles. The third objective of TOLNET is to perform basic scientific research into the processes create and destroy the ubiquitously observed ozone laminae and other ozone features in the troposphere. To help fulfill these objectives, lidars that are a part of TOLNet have been deployed to support nearly ten campaigns thus far. This includes campaigns such as the Deriving Information on Surface conditions from Column and Vertically Resolved Observations Relevant to Air Quality (DISCOVER-AQ) mission, the Korea United States Air Quality Study (KORUS-AQ), the Tracking Aerosol Convection ExpeRiment \u2013 Air Quality (TRACER-AQ) campaign, the Front Range Air Pollution and Photochemistry \u00c9xperiment (FRAPP\u00c9), the Long Island Sound Tropospheric Ozone Study (LISTOS), and the Ozone Water\u2013Land Environmental Transition Study (OWLETS).",
-            "title": "TOLNet NASA Jet Propulsion Laboratory Data",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FLidar%2FOzone%2FTOLNet%2FNASA-JPL%0D%0A",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FLidar%2FOzone%2FTOLNet%2FNASA-JPL%0D%0A",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www-air.larc.nasa.gov/missions/TOLNet/",
-                    "description": "TOLNet Project Home Page",
                     "@type": "dcat:Distribution",
+                    "description": "TOLNet Project Home Page",
+                    "downloadURL": "https://www-air.larc.nasa.gov/missions/TOLNet/",
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
-                    "downloadURL": "http://dx.doi.org/10.1364/AO.52.003557",
-                    "description": "Ground-based lidar for atmospheric boundary layer ozone measurements",
                     "@type": "dcat:Distribution",
+                    "description": "Ground-based lidar for atmospheric boundary layer ozone measurements",
+                    "downloadURL": "http://dx.doi.org/10.1364/AO.52.003557",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://www-air.larc.nasa.gov/missions/TOLNet/docs/meeting/June2016/Wednesday/Berkoff_TolnetSTMmeetingV3_Final.pdf",
-                    "description": "Capabilities & example data from the Langley Mobile Ozone Lidar (LMOL)",
                     "@type": "dcat:Distribution",
+                    "description": "Capabilities & example data from the Langley Mobile Ozone Lidar (LMOL)",
+                    "downloadURL": "https://www-air.larc.nasa.gov/missions/TOLNet/docs/meeting/June2016/Wednesday/Berkoff_TolnetSTMmeetingV3_Final.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5194/amt-7-3529-2014",
-                    "description": "A mobile differential absorption lidar to measure sub-hourly fluctuation of tropospheric ozone profiles in the Baltimore\u2013Washington, D.C. region",
                     "@type": "dcat:Distribution",
+                    "description": "A mobile differential absorption lidar to measure sub-hourly fluctuation of tropospheric ozone profiles in the Baltimore\u2013Washington, D.C. region",
+                    "downloadURL": "https://doi.org/10.5194/amt-7-3529-2014",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.1364/AO.41.007550",
-                    "description": "Redesign and improved performance of the tropospheric ozone lidar at the Jet Propulsion Laboratory Table Mountain Facility",
                     "@type": "dcat:Distribution",
+                    "description": "Redesign and improved performance of the tropospheric ozone lidar at the Jet Propulsion Laboratory Table Mountain Facility",
+                    "downloadURL": "https://doi.org/10.1364/AO.41.007550",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.1175/JTECH-D-10-05044.1",
-                    "description": "Development and Application of a Compact, Tunable, Solid-State Airborne Ozone Lidar System for Boundary Layer Profiling",
                     "@type": "dcat:Distribution",
+                    "description": "Development and Application of a Compact, Tunable, Solid-State Airborne Ozone Lidar System for Boundary Layer Profiling",
+                    "downloadURL": "https://doi.org/10.1175/JTECH-D-10-05044.1",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://doi.org/10.1175/JTECH-D-10-05043.1",
-                    "description": "Comparison between the TOPAZ Airborne Ozone Lidar and In Situ Measurements during TexAQS 2006",
                     "@type": "dcat:Distribution",
+                    "description": "Comparison between the TOPAZ Airborne Ozone Lidar and In Situ Measurements during TexAQS 2006",
+                    "downloadURL": "http://doi.org/10.1175/JTECH-D-10-05043.1",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5194/amt-6-801-2013",
-                    "description": "Developing a portable, autonomous aerosol backscatter lidar for network or remote operations",
                     "@type": "dcat:Distribution",
+                    "description": "Developing a portable, autonomous aerosol backscatter lidar for network or remote operations",
+                    "downloadURL": "https://doi.org/10.5194/amt-6-801-2013",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5194/amt-10-3865-2017",
-                    "description": "Quantifying TOLNet ozone lidar accuracy during the 2014 DISCOVER-AQ and FRAPP\u00c9 campaigns",
                     "@type": "dcat:Distribution",
+                    "description": "Quantifying TOLNet ozone lidar accuracy during the 2014 DISCOVER-AQ and FRAPP\u00c9 campaigns",
+                    "downloadURL": "https://doi.org/10.5194/amt-10-3865-2017",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2565841261-LARC_ASDC",
-                    "description": "Earthdata Search access for TOLNet_JPL_Data_1",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search access for TOLNet_JPL_Data_1",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2565841261-LARC_ASDC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/Lidar/Ozone/TOLNet/NASA-JPL",
-                    "description": "DOI Data Set Landing Page",
                     "@type": "dcat:Distribution",
+                    "description": "DOI Data Set Landing Page",
+                    "downloadURL": "https://doi.org/10.5067/Lidar/Ozone/TOLNet/NASA-JPL",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/TOLNet/JPL_Data_1/",
-                    "description": "ASDC Direct Data Download for TOLNet_JPL_Data_1",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for TOLNet_JPL_Data_1",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/TOLNet/JPL_Data_1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/TOLNet/JPL_Data_1/contents.html",
-                    "description": "OPeNDAP data access for TOLNet_JPL_Data_1",
                     "@type": "dcat:Distribution",
+                    "description": "OPeNDAP data access for TOLNet_JPL_Data_1",
+                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/TOLNet/JPL_Data_1/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 }
             ],
+            "identifier": "C2565841261-LARC_ASDC",
+            "issued": "2022-09-21",
+            "keyword": [
+                "earth science",
+                "atmospheric temperature",
+                "atmospheric pressure",
+                "atmosphere",
+                "atmospheric chemistry"
+            ],
+            "landingPage": "https://doi.org/10.5067/Lidar/Ozone/TOLNet/NASA-JPL",
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
             "spatial": "<?xml version=\"1.0\" encoding=\"UTF-8\"?><gml:Polygon xmlns:gml=\"http://www.opengis.net/gml/3.2\" srsName=\"EPSG:9825\"><gml:outerBoundaryIs><gml:LinearRing><gml:posList>34.3 -117.75 34.3 -117.65 34.6 -117.65 34.6 -117.75 34.3 -117.75</gml:posList></gml:LinearRing></gml:outerBoundaryIs><gml:innerBoundaryIs></gml:innerBoundaryIs></gml:Polygon>",
+            "temporal": "2011-01-27T00:00:00Z/2023-02-28T00:00:00Z",
             "theme": [
                 "TOLNet",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "TOLNet NASA Jet Propulsion Laboratory Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-2-ESC3-67PCHURYUMOV-M19-V3.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This CODMAC level 2 data set contains uncalibrated image data in DN unit, acquired by the OSIRIS Narrow Angle Camera on the Rosetta spacecraft during the COMET ESCORT 3 mission phase, covering the period from 2015-07-28T23:25:00.000 to 2015-08-25T23:24:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V3.0 supersedes previous deliveries of the same dataset with the following changes since the last version: Lien corrected dataset after the July and October 2018 PSA/PDS external peer reviews. Updated documentation and ancillary files, added document on bandpass filter. Updated SCIENCE_USER_GUIDE_V03.PDF to include one section about FAQ and one section about image data quality. Added shutter backtravel and readout issues to image quality map. Updated DATA_QUALITY_ID keyword in image header. Improved handling of images with missing packets. Included FITs files. Browse products changed to the same size as the original image.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-2-esc3-67pchuryumov-m19-v3.0",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2021-05-21",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "67p/churyumov-gerasimenko 1 (1969 r1)",
                 "vega",
@@ -1046922,72 +1046924,44 @@
                 "dark",
                 "bias"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-2-ESC3-67PCHURYUMOV-M19-V3.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-2-esc3-67pchuryumov-m19-v3.0",
-            "description": "This CODMAC level 2 data set contains uncalibrated image data in DN unit, acquired by the OSIRIS Narrow Angle Camera on the Rosetta spacecraft during the COMET ESCORT 3 mission phase, covering the period from 2015-07-28T23:25:00.000 to 2015-08-25T23:24:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V3.0 supersedes previous deliveries of the same dataset with the following changes since the last version: Lien corrected dataset after the July and October 2018 PSA/PDS external peer reviews. Updated documentation and ancillary files, added document on bandpass filter. Updated SCIENCE_USER_GUIDE_V03.PDF to include one section about FAQ and one section about image data quality. Added shutter backtravel and readout issues to image quality map. Updated DATA_QUALITY_ID keyword in image header. Improved handling of images with missing packets. Included FITs files. Browse products changed to the same size as the original image.",
-            "title": "ROSETTA-ORBITER 67P OSINAC 2 ESC3-MTP019 EDR V3.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P OSINAC 2 ESC3-MTP019 EDR V3.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/W92WIC96B2CZ",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Charles Gatebe; Michael King; Rajesh Poudyal. 2019-03-06. CAR_INTEXB_BRDF. Version 2. CAR INTEXB BRDF Measurements L1 V2. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/W92WIC96B2CZ. https://disc.gsfc.nasa.gov/datacollection/CAR_INTEXB_BRDF_2.html.",
-            "issued": "2019-01-27",
-            "temporal": "2006-03-03T00:00:00Z/2006-03-19T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2019-01-27",
-            "keyword": [
-                "surface radiative properties",
-                "earth science",
-                "atmospheric radiation",
-                "oceans",
-                "land surface",
-                "atmosphere",
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
-            "identifier": "C1617621688-GES_DISC",
-            "description": "INTEX-B (Intercontinental Chemical Transport Experiment-Phase B) focuses on the long-range transport of pollution, global atmospheric photochemistry, and the effects of aerosols and clouds on radiation and climate. It has two phases: phase 1 of the study was performed in Mexico from March 1-20, 2006, and phase 2 was performed in April and May and focused on Asian City pollution outflow over the western Pacific.\n\nThis data set consists of observations made with the CAR instrument and includes values for bidirectional reflectance factor at varying spectral bands.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "CAR_INTEXB_BRDF",
             "creator": "Charles Gatebe; Michael King; Rajesh Poudyal",
-            "title": "CAR INTEXB BRDF Measurements L1 V2 (CAR_INTEXB_BRDF) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/CAR_INTEXB_L1C_1.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "INTEX-B (Intercontinental Chemical Transport Experiment-Phase B) focuses on the long-range transport of pollution, global atmospheric photochemistry, and the effects of aerosols and clouds on radiation and climate. It has two phases: phase 1 of the study was performed in Mexico from March 1-20, 2006, and phase 2 was performed in April and May and focused on Asian City pollution outflow over the western Pacific.\n\nThis data set consists of observations made with the CAR instrument and includes values for bidirectional reflectance factor at varying spectral bands.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FW92WIC96B2CZ",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FW92WIC96B2CZ",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
@@ -1046997,792 +1046971,796 @@
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/CAR_INTEXB_BRDF_2.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/CAR_INTEXB_BRDF_2.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://car.gsfc.nasa.gov/",
-                    "description": "CAR Project Home Page",
                     "@type": "dcat:Distribution",
+                    "description": "CAR Project Home Page",
+                    "downloadURL": "https://car.gsfc.nasa.gov/",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/opendap/CAR/CAR_INTEXB_BRDF.2/",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/opendap/CAR/CAR_INTEXB_BRDF.2/",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/CAR/CAR_INTEXB_BRDF.2/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/CAR/CAR_INTEXB_BRDF.2/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/CAR/CAR_BRDF_README-v2.pdf",
-                    "description": "README Document",
                     "@type": "dcat:Distribution",
+                    "description": "README Document",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/CAR/CAR_BRDF_README-v2.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's read me document"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=CAR_INTEXB_BRDF",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=CAR_INTEXB_BRDF",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 }
             ],
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/CAR_INTEXB_L1C_1.jpg",
+            "identifier": "C1617621688-GES_DISC",
+            "issued": "2019-01-27",
+            "keyword": [
+                "surface radiative properties",
+                "earth science",
+                "atmospheric radiation",
+                "oceans",
+                "land surface",
+                "atmosphere",
+                "ocean optics"
+            ],
+            "landingPage": "https://doi.org/10.5067/W92WIC96B2CZ",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2019-01-27",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
+            },
+            "release-place": "Greenbelt, MD, USA",
+            "series-name": "CAR_INTEXB_BRDF",
             "spatial": "-99.451 19.1145 -93.9624 22.1784",
+            "temporal": "2006-03-03T00:00:00Z/2006-03-19T23:59:59.999Z",
             "theme": [
                 "CAR",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "CAR INTEXB BRDF Measurements L1 V2 (CAR_INTEXB_BRDF) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ASDC/SUBORBITAL/KORUSAQ_Pandora_Data_1",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2022-03-01. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/ASDC/SUBORBITAL/KORUSAQ_Pandora_Data_1.",
-            "issued": "2021-06-09",
-            "temporal": "2015-04-30T00:00:00Z/2016-10-18T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-04-18",
-            "keyword": [
-                "atmospheric chemistry",
-                "earth science",
-                "atmosphere",
-                "air quality"
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
-            "identifier": "C2226947399-LARC_ASDC",
             "description": "KORUSAQ_Ground_Pandora_Data contains all of the Pandora instrumentation data collected during the KORUS-AQ field study. Contained in this dataset are column measurements of NO2, O3, and HCHO. Pandoras were situated at various ground sites across the study area, including, NIER-Taehwa, NIER-Olympic Park, NIER-Gwangju, NIER-Anmyeon, Busan, Yonsei University, Songchon, and Yeoju. Data collection for this product is complete.\r\n\r\nThe KORUS-AQ field study was conducted in South Korea during May-June, 2016. The study was jointly sponsored by NASA and Korea\u2019s National Institute of Environmental Research (NIER). The primary objectives were to investigate the factors controlling air quality in Korea (e.g., local emissions, chemical processes, and transboundary transport) and to assess future air quality observing strategies incorporating geostationary satellite observations. To achieve these science objectives, KORUS-AQ adopted a highly coordinated sampling strategy involved surface and airborne measurements including both in-situ and remote sensing instruments.\r\n\r\nSurface observations provided details on ground-level air quality conditions while airborne sampling provided an assessment of conditions aloft relevant to satellite observations and necessary to understand the role of emissions, chemistry, and dynamics in determining air quality outcomes. The sampling region covers the South Korean peninsula and surrounding waters with a primary focus on the Seoul Metropolitan Area. Airborne sampling was primarily conducted from near surface to about 8 km with extensive profiling to characterize the vertical distribution of pollutants and their precursors. The airborne observational data were collected from three aircraft platforms: the NASA DC-8, NASA B-200, and Hanseo King Air. Surface measurements were conducted from 16 ground sites and 2 ships: R/V Onnuri and R/V Jang Mok.\r\n\r\nThe major data products collected from both the ground and air include in-situ measurements of trace gases (e.g., ozone, reactive nitrogen species, carbon monoxide and dioxide, methane, non-methane and oxygenated hydrocarbon species), aerosols (e.g., microphysical and optical properties and chemical composition), active remote sensing of ozone and aerosols, and passive remote sensing of NO2, CH2O, and O3 column densities. These data products support research focused on examining the impact of photochemistry and transport on ozone and aerosols, evaluating emissions inventories, and assessing the potential use of satellite observations in air quality studies.",
-            "title": "KORUS-AQ Pandora Column Observations",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC%2FSUBORBITAL%2FKORUSAQ_Pandora_Data_1",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC%2FSUBORBITAL%2FKORUSAQ_Pandora_Data_1",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://espo.nasa.gov/korus-aq",
-                    "description": "KORUS-AQ Earth Science Project Office (ESPO) Home Page",
                     "@type": "dcat:Distribution",
+                    "description": "KORUS-AQ Earth Science Project Office (ESPO) Home Page",
+                    "downloadURL": "https://espo.nasa.gov/korus-aq",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.nier.go.kr/NIER/eng/index.do",
-                    "description": "KORUS-AQ Earth Science Project Office (ESPO) Home Page",
                     "@type": "dcat:Distribution",
+                    "description": "KORUS-AQ Earth Science Project Office (ESPO) Home Page",
+                    "downloadURL": "https://www.nier.go.kr/NIER/eng/index.do",
+                    "mediaType": "text/html",
                     "title": "The dataset's home page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.nasa.gov/feature/langley/the-future-of-monitoring-air-quality-from-space",
-                    "description": "Article, The Future of Monitoring Air Quality from Space",
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
-                    "downloadURL": "https://doi.org/10.5067/ASDC/SUBORBITAL/KORUSAQ_Pandora_Data_1",
-                    "description": "DOI Data Set Landing Page for KORUSAQ_Pandora_Data_1",
                     "@type": "dcat:Distribution",
+                    "description": "DOI Data Set Landing Page for KORUSAQ_Pandora_Data_1",
+                    "downloadURL": "https://doi.org/10.5067/ASDC/SUBORBITAL/KORUSAQ_Pandora_Data_1",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2226947399-LARC_ASDC",
-                    "description": "Earthdata Search Client for KORUSAQ_Pandora_Data_1",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search Client for KORUSAQ_Pandora_Data_1",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2226947399-LARC_ASDC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/KORUS-AQ/Pandora_Data_1/",
-                    "description": "ASDC Direct Data Download for KORUSAQ_Pandora_Data_1",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for KORUSAQ_Pandora_Data_1",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/KORUS-AQ/Pandora_Data_1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 }
             ],
+            "identifier": "C2226947399-LARC_ASDC",
+            "issued": "2021-06-09",
+            "keyword": [
+                "atmospheric chemistry",
+                "earth science",
+                "atmosphere",
+                "air quality"
+            ],
+            "landingPage": "https://doi.org/10.5067/ASDC/SUBORBITAL/KORUSAQ_Pandora_Data_1",
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
+            "temporal": "2015-04-30T00:00:00Z/2016-10-18T23:59:59.999Z",
             "theme": [
                 "KORUS-AQ",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "KORUS-AQ Pandora Column Observations"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=DAWN-A-GRAND-5-VESTA-FAST-RESIDUAL-V1.0",
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
-                "dawn mission to vesta and ceres"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "These data are maps of fast neutron\nresidual count rates from the GRaND plus Z boron loaded sensor.  The\nnominal fast neutron count rates were detrended using the GRaND\nepithermal neutron map to produced this residual map.  The residual map\nis related to the average atomic mass on Vesta.  Details of the map and\ndata reduction are described in LAWRENCEETAL2013B.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.dawn-a-grand-5-vesta-fast-residual-v1.0_ktau-u4u5",
+            "issued": "2021-05-21",
+            "keyword": [
+                "4 vesta",
+                "dawn mission to vesta and ceres"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=DAWN-A-GRAND-5-VESTA-FAST-RESIDUAL-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.dawn-a-grand-5-vesta-fast-residual-v1.0_ktau-u4u5",
-            "description": "These data are maps of fast neutron\nresidual count rates from the GRaND plus Z boron loaded sensor.  The\nnominal fast neutron count rates were detrended using the GRaND\nepithermal neutron map to produced this residual map.  The residual map\nis related to the average atomic mass on Vesta.  Details of the map and\ndata reduction are described in LAWRENCEETAL2013B.",
-            "title": "DAWN GRAND MAP VESTA FAST NEUTRON\n                                      RESIDUAL V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "DAWN GRAND MAP VESTA FAST NEUTRON\n                                      RESIDUAL V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/MC3E/NEXRAD/DATA202",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "National Weather Service .2014. GPM GROUND VALIDATION KVNX NEXRAD MC3E [indicate subset used]. Dataset available online from the NASA Global Hydrometeorology Resource Center DAAC, Huntsville, Alabama, U.S.A. DOI: http://dx.doi.org/10.5067/MC3E/NEXRAD/DATA202",
-            "issued": "2014-10-03",
-            "temporal": "2011-04-22T00:01:35Z/2011-06-06T23:52:18Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-05-10",
-            "keyword": [
-                "spectral/engineering",
-                "radar",
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
-            "identifier": "C1979618519-GHRC_DAAC",
             "description": "The GPM Ground Validation KVNX NEXRAD MC3E dataset was collected from April 22, 2011 to June 6, 2011 for the Midlatitude Continental Convective Clouds Experiment (MC3E). The overarching goal of MC3E was to provide the most complete characterization of convective cloud systems, precipitation, and the environment that has ever been obtained, providing constraints for model cumulus parameterizations and space-based rainfall retrieval algorithms over land that had never before been available. The Next Generation Weather Radar system (NEXRAD) is comprised of 160 Weather Surveillance Radar-1988 Doppler (WSR-88D) sites throughout the United States and select overseas locations. The GPM Ground Validation NEXRAD MC3E data files are available as compressed binary files.",
-            "graphic-preview-description": "N/A",
-            "title": "GPM GROUND VALIDATION KVNX NEXRAD MC3E V1",
-            "graphic-preview-file": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/mc3e/NEXRAD/KVNX/browse/",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMC3E%2FNEXRAD%2FDATA202",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMC3E%2FNEXRAD%2FDATA202",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=gpmkvnxmc3e",
-                    "description": "Files may be downloaded directly to your workstation from this link",
                     "@type": "dcat:Distribution",
+                    "description": "Files may be downloaded directly to your workstation from this link",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=gpmkvnxmc3e",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/browse_sample/fieldCampaigns/gpmValidation/mc3e/gpmkvnxmc3e/2011-05-11_23-04-05_KVNX_COMPOSITE.png",
-                    "description": "Sample browse image",
                     "@type": "dcat:Distribution",
+                    "description": "Sample browse image",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/browse_sample/fieldCampaigns/gpmValidation/mc3e/gpmkvnxmc3e/2011-05-11_23-04-05_KVNX_COMPOSITE.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/browse_sample/fieldCampaigns/gpmValidation/mc3e/gpmkvnxmc3e/2011-05-11_23-04-05_KVNX_CAPPI_05.0.png",
-                    "description": "Sample browse image",
                     "@type": "dcat:Distribution",
+                    "description": "Sample browse image",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/browse_sample/fieldCampaigns/gpmValidation/mc3e/gpmkvnxmc3e/2011-05-11_23-04-05_KVNX_CAPPI_05.0.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/browse_sample/fieldCampaigns/gpmValidation/mc3e/gpmkvnxmc3e/2011-05-11_23-04-05_KVNX_ELEV_05.png",
-                    "description": "Sample browse image",
                     "@type": "dcat:Distribution",
+                    "description": "Sample browse image",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/browse_sample/fieldCampaigns/gpmValidation/mc3e/gpmkvnxmc3e/2011-05-11_23-04-05_KVNX_ELEV_05.png",
+                    "mediaType": "image/png",
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
-                    "downloadURL": "http://ghrc.nsstc.nasa.gov/uso/ds_docs/gpmgv/mc3e/gpmnexradmc3e/gpmnexradmc3e_dataset.html",
-                    "description": "The guide document contains detailed information about the dataset",
                     "@type": "dcat:Distribution",
+                    "description": "The guide document contains detailed information about the dataset",
+                    "downloadURL": "http://ghrc.nsstc.nasa.gov/uso/ds_docs/gpmgv/mc3e/gpmnexradmc3e/gpmnexradmc3e_dataset.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
```

