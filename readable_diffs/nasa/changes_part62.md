# Change History for nasa.json (Part 62)

### Changes from 31606f9 to dd2190f (Part 51/162)
**Author:** Automated

**Date:** 2025-02-01 15:02:16+00:00

**Message:** Updated data: Sat Feb  1 15:02:16 UTC 2025

```diff
+                "en-US"
+            ],
+            "modified": "2024-11-26",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "ORNL_DAAC"
+            },
             "spatial": "-169.0 50.0 -120.0 74.5",
+            "temporal": "2012-01-01T00:00:00Z/2014-12-31T23:59:59Z",
             "theme": [
                 "CARVE",
                 "ABoVE",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "CARVE: Net Ecosystem CO2 Exchange and Regional Carbon Budgets for Alaska, 2012-2014"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MEX-M-MRS-1%2F2%2F3-EXT5-3812-V1.0",
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
-                "mars express"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This is a Mars Express Radio Science data set, collected during the extended mission phase 2015-01-01 to 2016-12-31. It is a Occultation measurement and covers the time 2015-09-07T05:18:09.500 to 2015-09-07T05:42:03.949.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mex-m-mrs-1-2-3-ext5-3812-v1.0_bdxr-3rnp",
+            "issued": "2021-05-21",
+            "keyword": [
+                "mars",
+                "mars express"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MEX-M-MRS-1%2F2%2F3-EXT5-3812-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mex-m-mrs-1-2-3-ext5-3812-v1.0_bdxr-3rnp",
-            "description": "This is a Mars Express Radio Science data set, collected during the extended mission phase 2015-01-01 to 2016-12-31. It is a Occultation measurement and covers the time 2015-09-07T05:18:09.500 to 2015-09-07T05:42:03.949.",
-            "title": "MARS EXPRESS MARS MRS 1/2/3\n                                     EXTENDED MISSION 5 3812 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "MARS EXPRESS MARS MRS 1/2/3\n                                     EXTENDED MISSION 5 3812 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://c3.nasa.gov/dashlink/resources/307/",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Vlad Popescu",
+                "hasEmail": "mailto:vmpopescu@gmail.com"
+            },
+            "description": "This paper discusses the effect of sequential conflict resolution maneuvers of an infinite aircraft flow through a finite control volume. Aircraft flow models are utilized to simulate traffic flows and determine stability. Pseudo-random flow geometry is considered to determine airspace stability in a more random airspace, where aircraft flows are spread over a given positive width. The use of this aircraft flow model generates a more realistic flow geometry. A set of upper bounds on the maximal aircraft deviation during conflict resolution is derived. Also with this flow geometry it is proven that these bounds are not symmetric, unlike the symmetric bounds derived in previous papers for simpler flow configurations. Stability is preserved under sequential conflict resolution algorithms for all flow geometries discussed in this paper.",
+            "identifier": "DASHLINK_307",
             "issued": "2011-02-07",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
             "keyword": [
                 "dashlink",
                 "nasa",
                 "ames"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Vlad Popescu",
-                "hasEmail": "mailto:vmpopescu@gmail.com"
-            },
+            "landingPage": "https://c3.nasa.gov/dashlink/resources/307/",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:029"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Dashlink"
             },
-            "identifier": "DASHLINK_307",
-            "description": "This paper discusses the effect of sequential conflict resolution maneuvers of an infinite aircraft flow through a finite control volume. Aircraft flow models are utilized to simulate traffic flows and determine stability. Pseudo-random flow geometry is considered to determine airspace stability in a more random airspace, where aircraft flows are spread over a given positive width. The use of this aircraft flow model generates a more realistic flow geometry. A set of upper bounds on the maximal aircraft deviation during conflict resolution is derived. Also with this flow geometry it is proven that these bounds are not symmetric, unlike the symmetric bounds derived in previous papers for simpler flow configurations. Stability is preserved under sequential conflict resolution algorithms for all flow geometries discussed in this paper.",
-            "title": "Stability of Spatially Distributed, Intersecting Aircraft Flows Under Sequential Conflict Resolution Schemes",
-            "programCode": [
-                "026:029"
-            ],
-            "accrualPeriodicity": "irregular"
+            "title": "Stability of Spatially Distributed, Intersecting Aircraft Flows Under Sequential Conflict Resolution Schemes"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/KZ43HVLZV6G4",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "SnowEx20 Time Series Snow Pit Measurements V002. Version 2. Archived by National Aeronautics and Space Administration, U.S. Government, NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/KZ43HVLZV6G4.",
-            "issued": "2019-10-24",
-            "temporal": "2019-10-24T00:00:00Z/2020-05-20T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-20",
-            "keyword": [
-                "earth science",
-                "terrestrial hydrosphere",
-                "glaciers/ice sheets",
-                "snow/ice"
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
-            "identifier": "C2929469669-NSIDC_ECS",
             "description": "The data set is a time-series of snow pit measurements obtained by the SnowEx community during the 2020 campaign. Between October 2019 and May 2020, data were collected from 454 snow pits at 12 regional locations throughout California, Colorado, Idaho, New Mexico, and Utah, USA. At each of the locations, between 1 and 11 sites covering a range of conditions (terrains, snow depths, etc.) were chosen for weekly snow pit observations.  Also available are photos of the field notes and snow pit sites.",
-            "title": "SnowEx20 Time Series Snow Pit Measurements V002",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FKZ43HVLZV6G4",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FKZ43HVLZV6G4",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/SNOWEX/SNEX20_TS_SP.002/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/SNOWEX/SNEX20_TS_SP.002/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/data/data-access-tool/SNEX20_TS_SP/versions/2/",
-                    "description": "Search and filter data files using a map-based interface",
                     "@type": "dcat:Distribution",
+                    "description": "Search and filter data files using a map-based interface",
+                    "downloadURL": "https://nsidc.org/data/data-access-tool/SNEX20_TS_SP/versions/2/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=SNEX20_TS_SP+V002",
-                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=SNEX20_TS_SP+V002",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/SNOWEX/SNEX20_TS_SP.002/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/SNOWEX/SNEX20_TS_SP.002/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/data/data-access-tool/SNEX20_TS_SP/versions/2/",
-                    "description": "Search and filter data files using a map-based interface",
                     "@type": "dcat:Distribution",
+                    "description": "Search and filter data files using a map-based interface",
+                    "downloadURL": "https://nsidc.org/data/data-access-tool/SNEX20_TS_SP/versions/2/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=SNEX20_TS_SP+V002",
-                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=SNEX20_TS_SP+V002",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/SNOWEX/SNEX20_TS_SP.002/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/SNOWEX/SNEX20_TS_SP.002/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/data/data-access-tool/SNEX20_TS_SP/versions/2/",
-                    "description": "Search and filter data files using a map-based interface",
                     "@type": "dcat:Distribution",
+                    "description": "Search and filter data files using a map-based interface",
+                    "downloadURL": "https://nsidc.org/data/data-access-tool/SNEX20_TS_SP/versions/2/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=SNEX20_TS_SP+V002",
-                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=SNEX20_TS_SP+V002",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/SNOWEX/SNEX20_TS_SP.002/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/SNOWEX/SNEX20_TS_SP.002/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/data/data-access-tool/SNEX20_TS_SP/versions/2/",
-                    "description": "Search and filter data files using a map-based interface",
                     "@type": "dcat:Distribution",
+                    "description": "Search and filter data files using a map-based interface",
+                    "downloadURL": "https://nsidc.org/data/data-access-tool/SNEX20_TS_SP/versions/2/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=SNEX20_TS_SP+V002",
-                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=SNEX20_TS_SP+V002",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/KZ43HVLZV6G4",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/KZ43HVLZV6G4",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/KZ43HVLZV6G4",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/KZ43HVLZV6G4",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C2929469669-NSIDC_ECS",
+            "issued": "2019-10-24",
+            "keyword": [
+                "earth science",
+                "terrestrial hydrosphere",
+                "glaciers/ice sheets",
+                "snow/ice"
+            ],
+            "landingPage": "https://doi.org/10.5067/KZ43HVLZV6G4",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2020-05-20",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA NSIDC DAAC"
+            },
             "spatial": "-120.29897 35.85794 -105.54616 44.30455",
+            "temporal": "2019-10-24T00:00:00Z/2020-05-20T23:59:59.999Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "SnowEx20 Time Series Snow Pit Measurements V002"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RL-C-ROMAP-2-SDL-MAG-V1.0",
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
+            "description": "This archive contains edited data refering to target 67P (CODMAC level 2) from the ROMAP-MAG instrument onboard ROSETTA Lander, acquired during the SDL (Separation Descent Landing) phase. It also contains documentation which describes the ROMAP experiment. The data archived in this data set conform to the Planetary Data System (PDS) Standards, Version 3.6.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.rl-c-romap-2-sdl-mag-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RL-C-ROMAP-2-SDL-MAG-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.rl-c-romap-2-sdl-mag-v1.0",
-            "description": "This archive contains edited data refering to target 67P (CODMAC level 2) from the ROMAP-MAG instrument onboard ROSETTA Lander, acquired during the SDL (Separation Descent Landing) phase. It also contains documentation which describes the ROMAP experiment. The data archived in this data set conform to the Planetary Data System (PDS) Standards, Version 3.6.",
-            "title": "ROSETTA-LANDER 67P ROMAP 2 SDL MAG\n                            V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-LANDER 67P ROMAP 2 SDL MAG\n                            V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/SPUR2-GLID3",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Ben Hodges. 2019-08-15. SPURS-2 Waveglider data for the E. Tropical Pacific field campaign. Version 1.0. SPURS-2 Field Campaign Waveglider Data Products. ASL, Physical Oceanography Department, Woods Hole Oceanographic Institution, Woods Hole, MA 02543 USA. Archived by National Aeronautics and Space Administration, U.S. Government, SPURS Data Management PI, Fred Bingham. https://doi.org/10.5067/SPUR2-GLID3. http://podaac.jpl.nasa.gov/SPURS. Ben Hodges, SPURS Data Management PI, Fred Bingham, 2019-08-15, SPURS-2 Waveglider data for the  E. Tropical Pacific field campaign, http://podaac.jpl.nasa.gov/SPURS.",
-            "issued": "2019-07-23",
-            "temporal": "2016-08-24T00:00:00Z/2017-11-10T21:30:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2019-07-23",
-            "keyword": [
-                "salinity/density",
-                "earth science",
-                "ocean pressure",
-                "oceans",
-                "ocean circulation",
-                "ocean temperature",
-                "ocean winds"
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
-            "identifier": "C2491772363-POCLOUD",
-            "description": "The SPURS (Salinity Processes in the Upper Ocean Regional Study) project is a NASA-funded oceanographic process study and associated field program that aim to elucidate key mechanisms responsible for near-surface salinity variations in the oceans. The project is comprised of two field campaigns and a series of cruises in regions of the Atlantic and Pacific Oceans exhibiting salinity extremes. SPURS employs a suite of state-of-the-art in-situ sampling technologies that, combined with remotely sensed salinity fields from the Aquarius/SAC-D, SMAP and SMOS satellites, provide a detailed characterization of salinity structure over a continuum of spatio-temporal scales. The SPURS-2 campaign involved two month-long cruises by the R/V Revelle in August 2016 and October 2017 combined with complementary sampling on a more continuous basis over this period by the schooner Lady Amber. Focused around a central mooring located near 10N,125W, the objective of SPURS-2 was to study the dynamics of the rainfall-dominated surface ocean at the western edge of the eastern Pacific fresh pool subject to high seasonal variability and strong zonal flows associated with the North Equatorial Current and Countercurrent. A Waveglider is an autonomous platform propelled by the conversion of ocean wave energy into forward thrust and employing solar panels to power instrumentation. For SPURS-2, sensors included a CTD at the near-surface and another at 6 m depth, providing continuous salinity and temperature observations plus air temperature and wind measurements.  Three wavegliders (ASL22, 32, 42) were deployed from the Revelle in August 2016 and again in November 2017 before final retrieval at the conclusion on the second cruise. Waveglider trajectories followed a 20x20km square loop around the moorings and a butterfly pattern around the neutrally-buoyant float. NetCDF waveglider data files here (one per platform) contain hour averaged, georeferenced  trajectory data for those parameters and depths.",
-            "release-place": "ASL, Physical Oceanography Department, Woods Hole Oceanographic Institution, Woods Hole, MA 02543 USA",
-            "series-name": "SPURS-2 Waveglider data for the E. Tropical Pacific field campaign",
-            "graphic-preview-description": "Thumbnail",
             "creator": "Ben Hodges",
-            "title": "SPURS-2 Waveglider data for the  E. Tropical Pacific field campaign",
-            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/SPURS2_WAVEGLIDER.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The SPURS (Salinity Processes in the Upper Ocean Regional Study) project is a NASA-funded oceanographic process study and associated field program that aim to elucidate key mechanisms responsible for near-surface salinity variations in the oceans. The project is comprised of two field campaigns and a series of cruises in regions of the Atlantic and Pacific Oceans exhibiting salinity extremes. SPURS employs a suite of state-of-the-art in-situ sampling technologies that, combined with remotely sensed salinity fields from the Aquarius/SAC-D, SMAP and SMOS satellites, provide a detailed characterization of salinity structure over a continuum of spatio-temporal scales. The SPURS-2 campaign involved two month-long cruises by the R/V Revelle in August 2016 and October 2017 combined with complementary sampling on a more continuous basis over this period by the schooner Lady Amber. Focused around a central mooring located near 10N,125W, the objective of SPURS-2 was to study the dynamics of the rainfall-dominated surface ocean at the western edge of the eastern Pacific fresh pool subject to high seasonal variability and strong zonal flows associated with the North Equatorial Current and Countercurrent. A Waveglider is an autonomous platform propelled by the conversion of ocean wave energy into forward thrust and employing solar panels to power instrumentation. For SPURS-2, sensors included a CTD at the near-surface and another at 6 m depth, providing continuous salinity and temperature observations plus air temperature and wind measurements.  Three wavegliders (ASL22, 32, 42) were deployed from the Revelle in August 2016 and again in November 2017 before final retrieval at the conclusion on the second cruise. Waveglider trajectories followed a 20x20km square loop around the moorings and a butterfly pattern around the neutrally-buoyant float. NetCDF waveglider data files here (one per platform) contain hour averaged, georeferenced  trajectory data for those parameters and depths.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSPUR2-GLID3",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSPUR2-GLID3",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/insitu/open/L2/spurs2/docs/DataDocumentation/ReadmeCFT_2016.pdf",
-                    "description": "Data Submission Report, Instrument Calibration Report, etc",
                     "@type": "dcat:Distribution",
+                    "description": "Data Submission Report, Instrument Calibration Report, etc",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/insitu/open/L2/spurs2/docs/DataDocumentation/ReadmeCFT_2016.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://spurs.jpl.nasa.gov/",
-                    "description": "Project Website for SPURS",
                     "@type": "dcat:Distribution",
+                    "description": "Project Website for SPURS",
+                    "downloadURL": "http://spurs.jpl.nasa.gov/",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://podaac.jpl.nasa.gov/spurs",
-                    "description": "Field Campaign and Instrument Overview",
                     "@type": "dcat:Distribution",
+                    "description": "Field Campaign and Instrument Overview",
+                    "downloadURL": "http://podaac.jpl.nasa.gov/spurs",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/insitu/open/L2/spurs2/docs/CruiseReports/SPURS2-2016-Cruise-Report.pdf",
-                    "description": "Cruise Reports",
                     "@type": "dcat:Distribution",
+                    "description": "Cruise Reports",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/insitu/open/L2/spurs2/docs/CruiseReports/SPURS2-2016-Cruise-Report.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/SPURS2_WAVEGLIDER.jpg",
-                    "description": "Thumbnail",
                     "@type": "dcat:Distribution",
+                    "description": "Thumbnail",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/SPURS2_WAVEGLIDER.jpg",
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
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2491772363-POCLOUD",
-                    "description": "HTTPS endpoint for data browse and download",
                     "@type": "dcat:Distribution",
+                    "description": "HTTPS endpoint for data browse and download",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2491772363-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2491772363-POCLOUD",
-                    "description": "Browse granule search results in Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse granule search results in Earthdata Search",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2491772363-POCLOUD",
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
+            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/SPURS2_WAVEGLIDER.jpg",
+            "identifier": "C2491772363-POCLOUD",
+            "issued": "2019-07-23",
+            "keyword": [
+                "salinity/density",
+                "earth science",
+                "ocean pressure",
+                "oceans",
+                "ocean circulation",
+                "ocean temperature",
+                "ocean winds"
+            ],
+            "landingPage": "https://doi.org/10.5067/SPUR2-GLID3",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2019-07-23",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/JPL/PODAAC"
+            },
+            "release-place": "ASL, Physical Oceanography Department, Woods Hole Oceanographic Institution, Woods Hole, MA 02543 USA",
+            "series-name": "SPURS-2 Waveglider data for the E. Tropical Pacific field campaign",
             "spatial": "-126.4 6.1 -108.8 13.8",
+            "temporal": "2016-08-24T00:00:00Z/2017-11-10T21:30:00Z",
             "theme": [
                 "SPURS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "SPURS-2 Waveglider data for the  E. Tropical Pacific field campaign"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=DAWN-CAL-FC2-2-EDR-CALIB-IMAGES-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "Abstract ======== Framing Camera 2 is one of two identical units flying on Dawn spacecraft. This dataset includes the image files to be used in the calibration of the raw data throughout the mission. These files represent the behaviour of each individual pixel with respect to dark current generation and pixel-to-pixel non-uniformity as a function of the filter. As these are elaborated image products, not obtained from a specific image acquisition, they do not have any ancillary data.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.dawn-cal-fc2-2-edr-calib-images-v1.0_be4b-r3qe",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "mars",
                 "dawn mission to vesta and ceres",
                 "1 ceres",
                 "4 vesta"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=DAWN-CAL-FC2-2-EDR-CALIB-IMAGES-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.dawn-cal-fc2-2-edr-calib-images-v1.0_be4b-r3qe",
-            "description": "Abstract ======== Framing Camera 2 is one of two identical units flying on Dawn spacecraft. This dataset includes the image files to be used in the calibration of the raw data throughout the mission. These files represent the behaviour of each individual pixel with respect to dark current generation and pixel-to-pixel non-uniformity as a function of the filter. As these are elaborated image products, not obtained from a specific image acquisition, they do not have any ancillary data.",
-            "title": "DAWN FC2 CALIBRATION IMAGES V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "DAWN FC2 CALIBRATION IMAGES V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C2789636167-LARC_ASDC.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://asdc.larc.nasa.gov/project/CERES/FLASH_SSF_NOAA20-FM6-VIIRS_Version1B.",
-            "issued": "2023-10-01",
-            "temporal": "2023-10-01T00:00:00Z/2025-01-06T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-12-31",
-            "keyword": [
-                "clouds",
-                "atmospheric water vapor",
-                "atmospheric temperature",
-                "surface radiative properties",
-                "atmosphere",
-                "land surface",
-                "atmospheric radiation",
-                "earth science"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "DR. PAUL STACKHOUSE",
                 "hasEmail": "mailto:paul.w.stackhouse@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/LARC/SD/ASDC"
-            },
-            "identifier": "C2789636167-LARC_ASDC",
             "description": "FLASH_SSF_NOAA20-FM6-VIIRS_Version1B data are near real-time CERES observed TOA fluxes, clouds, and parameterized surface fluxes, not officially calibrated. The Fast Longwave and SHortwave Flux (FLASHFlux) data are a product line of the Clouds and the Earth's Radiant Energy Systems (CERES) project designed for processing and release of top-of-atmosphere (TOA) and surface radiative fluxes within one week of CERES instrument measurement. The FLASHFlux data product is a rapid-release product based on the algorithms developed for and data collected by the CERES project. CERES is currently producing world-class climate data products derived from measurements taken aboard NASA's Terra and Aqua spacecraft. While of exceptional fidelity, these data products require considerable processing time to assure quality, verify accuracy, and assess precision. The result is that CERES data are typically released up to six months after acquiring the initial measurements. Such delays are of little consequence for climate studies, especially considering the improved quality of the released data products. Thus, FLASHFlux products are not intended to achieve climate quality.FLASHFlux data products were envisioned as a resource whereby CERES data could be provided to the community within a week of the initial measurements, with some calibration accuracy requirements relaxed to gain speed. The Single Scanner Footprint TOA/Surface Fluxes and Clouds (SSF) product contains one hour of instantaneous Fast Longwave And SHortwave Fluxes (FLASHFlux) data for a single Clouds and the Earth's Radiant Energy Systems (CERES) scanner instrument. The SSF combines instantaneous CERES data with scene information from a higher-resolution imager such as the Visible Infrared Imaging Radiometer Suite (VIIRS) on the NOAA-20 satellite and meteorological and ozone information from The Goddard Earth Observing System (GEOS) GEOS-IT Atmospheric Data Assimilation System (GEOS-5 ADAS). Scene identification and cloud properties are defined at the higher image resolution, and these data are averaged over the larger CERES footprint. For each CERES footprint, the SSF contains Top-of-Atmosphere fluxes in SW, LW, and incoming NET, surface fluxes using the Langley parameterized shortwave and longwave algorithms, and cloud information. CERES is a key component of the Earth Observing System (EOS) program. The CERES instruments provide radiometric measurements of the Earth's atmosphere from three broadband channels. The CERES mission is a follow-up to the successful Earth Radiation Budget Experiment (ERBE) mission. The first CERES instrument (PFM) was launched on November 27, 1997, as part of the Tropical Rainfall Measuring Mission (TRMM). Two CERES instruments (FM1 and FM2) were launched into polar orbit on board the EOS flagship Terra on December 18, 1999. Two additional CERES instruments (FM3 and FM4) were launched on board EOS Aqua on May 4, 2002. CERES instrument Flight Model 5 (FM5) was launched on board the Suomi National Polar-orbiting Partnership (NPP) satellite on October 28, 2011. The latest CERES instrument (FM6) was launched on board NOAA-20 on November 18, 2017.",
-            "graphic-preview-description": "Mission Logo",
-            "title": "Fast Longwave And SHortwave Fluxes (FLASHflux) NOAA-20 Clouds and Radiative Swath (SSF) Version1B",
-            "graphic-preview-file": "https://asdc.larc.nasa.gov/static/images/project_logos/ceres.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ceres.larc.nasa.gov/data/#fast-longwave-and-shortwave-flux-flashflux",
-                    "description": "CERES Data Page",
                     "@type": "dcat:Distribution",
+                    "description": "CERES Data Page",
+                    "downloadURL": "https://ceres.larc.nasa.gov/data/#fast-longwave-and-shortwave-flux-flashflux",
+                    "mediaType": "text/html",
                     "title": "Subset this dataset using a web based subsetter"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2789636167-LARC_ASDC",
-                    "description": "Earthdata Search for FLASH_SSF_NOAA20-FM6-VIIRS_Version1B (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for FLASH_SSF_NOAA20-FM6-VIIRS_Version1B (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2789636167-LARC_ASDC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ceres.larc.nasa.gov/",
-                    "description": "CERES Project Landing Page",
                     "@type": "dcat:Distribution",
+                    "description": "CERES Project Landing Page",
+                    "downloadURL": "https://ceres.larc.nasa.gov/",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
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
-                    "downloadURL": "https://asdc.larc.nasa.gov/project/CERES",
-                    "description": "ASDC Data and Information for CERES",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Data and Information for CERES",
+                    "downloadURL": "https://asdc.larc.nasa.gov/project/CERES",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/ceres/readme/DPC_SSF_R4V1.pdf",
-                    "description": "CERES Data Products Catalog R4V110/1/2004 Single Scanner Footprint TOA/Surface Fluxes and Clouds (SSF)",
                     "@type": "dcat:Distribution",
+                    "description": "CERES Data Products Catalog R4V110/1/2004 Single Scanner Footprint TOA/Surface Fluxes and Clouds (SSF)",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/ceres/readme/DPC_SSF_R4V1.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's processing history"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ceres-tool.larc.nasa.gov/ord-tool/products?CERESProducts=FLASH_SSF",
-                    "description": "CERES Tool Products Browse, Subset, and Order: Fast Longwave and Shortwave Flux (FLASHFlux)",
                     "@type": "dcat:Distribution",
+                    "description": "CERES Tool Products Browse, Subset, and Order: Fast Longwave and Shortwave Flux (FLASHFlux)",
+                    "downloadURL": "https://ceres-tool.larc.nasa.gov/ord-tool/products?CERESProducts=FLASH_SSF",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through the CERES Ordering Tool"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://ceres.larc.nasa.gov/documents/DQ_summaries/Versioned/CER_FLASHFlux_SSF_Terra-Aqua_Ver4A_DQS_V01.pdf",
-                    "description": "Data Quality: FLASH_SSF",
                     "@type": "dcat:Distribution",
+                    "description": "Data Quality: FLASH_SSF",
+                    "downloadURL": "https://ceres.larc.nasa.gov/documents/DQ_summaries/Versioned/CER_FLASHFlux_SSF_Terra-Aqua_Ver4A_DQS_V01.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's data quality document"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/FLASH/SSF/NOAA20-FM6-VIIRS_Version1B/",
-                    "description": "ASDC Direct Data Download for FLASH_SSF_NOAA20-FM6-VIIRS_Version1B",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for FLASH_SSF_NOAA20-FM6-VIIRS_Version1B",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/FLASH/SSF/NOAA20-FM6-VIIRS_Version1B/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/FLASH/SSF/NOAA20-FM6-VIIRS_Version1B/contents.html",
-                    "description": "OPeNDAP data access for FLASH_SSF_NOAA20-FM6-VIIRS_Version1B",
                     "@type": "dcat:Distribution",
+                    "description": "OPeNDAP data access for FLASH_SSF_NOAA20-FM6-VIIRS_Version1B",
+                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/FLASH/SSF/NOAA20-FM6-VIIRS_Version1B/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 }
             ],
+            "graphic-preview-description": "Mission Logo",
+            "graphic-preview-file": "https://asdc.larc.nasa.gov/static/images/project_logos/ceres.png",
+            "identifier": "C2789636167-LARC_ASDC",
+            "issued": "2023-10-01",
+            "keyword": [
+                "clouds",
+                "atmospheric water vapor",
+                "atmospheric temperature",
+                "surface radiative properties",
+                "atmosphere",
+                "land surface",
+                "atmospheric radiation",
+                "earth science"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C2789636167-LARC_ASDC.html",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2024-12-31",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/LARC/SD/ASDC"
+            },
             "spatial": "<?xml version=\"1.0\" encoding=\"UTF-8\"?><gml:Polygon xmlns:gml=\"http://www.opengis.net/gml/3.2\" srsName=\"EPSG:9825\"><gml:outerBoundaryIs><gml:LinearRing><gml:posList>-90.0 -180.0 -90.0 180.0 90.0 180.0 90.0 -180.0 -90.0 -180.0</gml:posList></gml:LinearRing></gml:outerBoundaryIs><gml:innerBoundaryIs></gml:innerBoundaryIs></gml:Polygon>",
+            "temporal": "2023-10-01T00:00:00Z/2025-01-06T00:00:00Z",
             "theme": [
                 "FLASHFLUX",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Fast Longwave And SHortwave Fluxes (FLASHflux) NOAA-20 Clouds and Radiative Swath (SSF) Version1B"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://c3.nasa.gov/dashlink/resources/886/",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2014-01-07",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
-            "keyword": [
-                "ames",
-                "nasa",
-                "dashlink"
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
-            "identifier": "DASHLINK_886",
             "description": "Diagnosability is an important issue in the design of diagnostic systems, because it helps identify whether sufficient information is available to distinguish all the faults. Diagnosability of hybrid systems, however, is challenging, because mode transitions may occur during fault isolation. We present an event-based framework for hybrid systems diagnosis based on a qualitative abstraction of measurement deviations from nominal behavior. We derive event-based fault models that describe the possible measurement deviations sequences due to faults, which, coupled with the mode transition structure of the system, are used to automatically synthesize an event-based diagnoser for hybrid systems. We introduce notions of diagnosability for hybrid systems and show how the event-based diagnoser can be used to verify the diagnosability of the system. We apply our diagnosability analysis scheme to a real-world electrical power distribution system.",
-            "title": "An Event-based Approach to Hybrid Systems Diagnosability",
-            "programCode": [
-                "026:029"
-            ],
             "distribution": [
                 {
-                    "mediaType": "application/x-download",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/publication/DaigleEtAl-EventBasedHybridDiagnosability.pdf",
-                    "description": "DaigleEtAl-EventBasedHybridDiagnosability.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "DaigleEtAl-EventBasedHybridDiagnosability.pdf",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/publication/DaigleEtAl-EventBasedHybridDiagnosability.pdf",
+                    "mediaType": "application/x-download",
                     "title": "DaigleEtAl-EventBasedHybridDiagnosability.pdf"
                 }
             ],
-            "accrualPeriodicity": "irregular"
+            "identifier": "DASHLINK_886",
+            "issued": "2014-01-07",
+            "keyword": [
+                "ames",
+                "nasa",
+                "dashlink"
+            ],
+            "landingPage": "https://c3.nasa.gov/dashlink/resources/886/",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:029"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Dashlink"
+            },
+            "title": "An Event-based Approach to Hybrid Systems Diagnosability"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewBundle.jsp?identifier=urn%3Anasa%3Apds%3Acompil.satellite.polarimetry&version=1.0",
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
-                "multiple satellites"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This compilation of polarimetry of       planetary satellites has been compiled from the published literature   and from unpublished results by Zaitsev, Rosenbush, and Kiselev.       Geometric observational circumstances, calculated using the JPL        Horizons ephemeris system, are also included.  This version of the     compilation is dated April 15, 2012.",
+            "identifier": "urn:nasa:pds:compil.satellite.polarimetry",
+            "issued": "2021-05-21",
+            "keyword": [
+                "none",
+                "multiple satellites"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewBundle.jsp?identifier=urn%3Anasa%3Apds%3Acompil.satellite.polarimetry&version=1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:compil.satellite.polarimetry",
-            "description": "This compilation of polarimetry of       planetary satellites has been compiled from the published literature   and from unpublished results by Zaitsev, Rosenbush, and Kiselev.       Geometric observational circumstances, calculated using the JPL        Horizons ephemeris system, are also included.  This version of the     compilation is dated April 15, 2012.",
-            "title": "POLARIMETRY OF PLANETARY SATELLITES",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
-        },
-        {
-            "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/VIIRS/VNP43D08.001",
-            "bureauCode": [
-                "026:00"
-            ],
-            "citation": "Crystal Schaaf, Zhuosen Wang, Xiaoyang Zhang, Alan Strahler\r\n. 2019-11-07. VNP43d08. Version 001. VIIRS/NPP BRDF/Albedo Parameter 2 Band M3 Daily L3 Global 30 ArcSec CMG V001\r\n. Sioux Falls, South Dakota, USA. Archived by National Aeronautics and Space Administration, U.S. Government, NASA EOSDIS Land Processes Distributed Active Archive Center. https://doi.org/10.5067/VIIRS/VNP43D08.001. https://doi.org/10.5067/VIIRS/VNP43D08.001. Digital Science Data. The DOI landing page provides citations in APA and Chicago styles.\r\n.",
-            "issued": "2019-11-07",
-            "temporal": "2012-01-19T00:00:00Z/2024-05-20T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2019-11-07",
-            "keyword": [
-                "land surface",
-                "surface radiative properties",
-                "earth science"
             ],
-            "data-presentation-form": "Digital Science Data",
+            "title": "POLARIMETRY OF PLANETARY SATELLITES"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "026:00"
+            ],
+            "citation": "Crystal Schaaf, Zhuosen Wang, Xiaoyang Zhang, Alan Strahler\r\n. 2019-11-07. VNP43d08. Version 001. VIIRS/NPP BRDF/Albedo Parameter 2 Band M3 Daily L3 Global 30 ArcSec CMG V001\r\n. Sioux Falls, South Dakota, USA. Archived by National Aeronautics and Space Administration, U.S. Government, NASA EOSDIS Land Processes Distributed Active Archive Center. https://doi.org/10.5067/VIIRS/VNP43D08.001. https://doi.org/10.5067/VIIRS/VNP43D08.001. Digital Science Data. The DOI landing page provides citations in APA and Chicago styles.\r\n.",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "undefined",
                 "hasEmail": "mailto:lpdaac@usgs.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "LP DAAC"
-            },
-            "identifier": "C1607315592-LPDAAC_ECS",
-            "description": "The NASA/NOAA Suomi National Polar-orbiting Partnership (Suomi NPP) Visible Infrared Imaging Radiometer Suite (VIIRS) Bidirectional Reflectance Distribution Function (BRDF) and Albedo Model Parameter 2 Band M3 product (VNP43D08) is produced daily using 16 days of data at 30 arc second (1,000 meter) resolution. Data are temporally weighted to the ninth day, which is reflected in the file name. The VNP43D product suite is provided in a Climate Modeling Grid (CMG), which covers the entire globe for use in climate simulation models. Due to the large file size, each VNP43D product contains just one data layer. Each of the three model parameters (isotropic, volumetric, and geometric) for each of the nine VIIRS moderate resolution bands along with the visible, near-infrared (NIR), and shortwave bands included in the VNP43MA1 (https://doi.org/10.5067/VIIRS/VNP43MA1.001) product is stored in a separate file as VNP43D01 through VNP43D36. In addition to the bands included in VNP43MA1, this product suite includes model parameters for the VIIRS Day/Night Band (DNB) as VNP43D37 through VNP43D39. Details regarding methodology are available on the VNP43MA1 product page and in the Algorithm Theoretical Basis Document [ATBD).\r\n\r\nVNP43D08 is the BRDF volumetric parameter for VIIRS band M3 (0.488 \u03bcm). The volumetric parameter, in conjunction with the isotropic and geometric parameters, is used to derive the BRDF/Albedo values for VIIRS band M3.",
-            "release-place": "Sioux Falls, South Dakota, USA",
-            "series-name": "VNP43d08",
             "creator": "Crystal Schaaf, Zhuosen Wang, Xiaoyang Zhang, Alan Strahler",
-            "title": "VIIRS/NPP BRDF/Albedo Parameter 2 Band M3 Daily L3 Global 30 ArcSec CMG V001",
-            "programCode": [
-                "026:001"
-            ],
+            "data-presentation-form": "Digital Science Data",
+            "description": "The NASA/NOAA Suomi National Polar-orbiting Partnership (Suomi NPP) Visible Infrared Imaging Radiometer Suite (VIIRS) Bidirectional Reflectance Distribution Function (BRDF) and Albedo Model Parameter 2 Band M3 product (VNP43D08) is produced daily using 16 days of data at 30 arc second (1,000 meter) resolution. Data are temporally weighted to the ninth day, which is reflected in the file name. The VNP43D product suite is provided in a Climate Modeling Grid (CMG), which covers the entire globe for use in climate simulation models. Due to the large file size, each VNP43D product contains just one data layer. Each of the three model parameters (isotropic, volumetric, and geometric) for each of the nine VIIRS moderate resolution bands along with the visible, near-infrared (NIR), and shortwave bands included in the VNP43MA1 (https://doi.org/10.5067/VIIRS/VNP43MA1.001) product is stored in a separate file as VNP43D01 through VNP43D36. In addition to the bands included in VNP43MA1, this product suite includes model parameters for the VIIRS Day/Night Band (DNB) as VNP43D37 through VNP43D39. Details regarding methodology are available on the VNP43MA1 product page and in the Algorithm Theoretical Basis Document [ATBD).\r\n\r\nVNP43D08 is the BRDF volumetric parameter for VIIRS band M3 (0.488 \u03bcm). The volumetric parameter, in conjunction with the isotropic and geometric parameters, is used to derive the BRDF/Albedo values for VIIRS band M3.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FVIIRS%2FVNP43D08.001",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FVIIRS%2FVNP43D08.001",
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
-                    "downloadURL": "https://doi.org/10.5067/VIIRS/VNP43D08.001",
-                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
+                    "downloadURL": "https://doi.org/10.5067/VIIRS/VNP43D08.001",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/xhdf5",
-                    "downloadURL": "https://e4ftl01.cr.usgs.gov/VIIRS/VNP43D08.001/",
-                    "description": "LP DAAC Data Pool provides direct access to available products via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "LP DAAC Data Pool provides direct access to available products via HTTPS.",
+                    "downloadURL": "https://e4ftl01.cr.usgs.gov/VIIRS/VNP43D08.001/",
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
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=C1607315592-LPDAAC_ECS",
-                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=C1607315592-LPDAAC_ECS",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://opendap.cr.usgs.gov/opendap/hyrax/VNP43D08.001/contents.html",
-                    "description": "Access data via Open-source Project for a Network Data Access Protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access data via Open-source Project for a Network Data Access Protocol.",
+                    "downloadURL": "https://opendap.cr.usgs.gov/opendap/hyrax/VNP43D08.001/contents.html",
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
-                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/filespec/VIIRS/1/VNP43D08",
-                    "description": "The File Specification provides a description of the product file including Scientific Data Sets and their attributes.",
                     "@type": "dcat:Distribution",
+                    "description": "The File Specification provides a description of the product file including Scientific Data Sets and their attributes.",
+                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/filespec/VIIRS/1/VNP43D08",
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
+            "identifier": "C1607315592-LPDAAC_ECS",
+            "issued": "2019-11-07",
+            "keyword": [
+                "land surface",
+                "surface radiative properties",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/VIIRS/VNP43D08.001",
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
+            "series-name": "VNP43d08",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2012-01-19T00:00:00Z/2024-05-20T00:00:00Z",
             "theme": [
                 "NPP-JPSS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "VIIRS/NPP BRDF/Albedo Parameter 2 Band M3 Daily L3 Global 30 ArcSec CMG V001"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=DIF-M-HRII-2-EPOXI-MARS-V1.0",
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
-                "epoxi",
-                "mars"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This data set contains raw, 1.05- to 4.8-micron spectra of Mars acquired by the High Resolution Infrared Spectrometer (HRII) for the EPOCh project during the second cruise phase of the EPOXI mission. One set of observations was acquired on 20-21 November 2009 to characterize Mars as an analog for extrasolar planets. The observing period lasted approximately 24 hours, and spectra were acquired twice per hour.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.dif-m-hrii-2-epoxi-mars-v1.0_bed7-ejd9",
+            "issued": "2021-05-21",
+            "keyword": [
+                "epoxi",
+                "mars"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=DIF-M-HRII-2-EPOXI-MARS-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.dif-m-hrii-2-epoxi-mars-v1.0_bed7-ejd9",
-            "description": "This data set contains raw, 1.05- to 4.8-micron spectra of Mars acquired by the High Resolution Infrared Spectrometer (HRII) for the EPOCh project during the second cruise phase of the EPOXI mission. One set of observations was acquired on 20-21 November 2009 to characterize Mars as an analog for extrasolar planets. The observing period lasted approximately 24 hours, and spectra were acquired twice per hour.",
-            "title": "EPOXI MARS OBS - HRII RAW SPECTRA V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "EPOXI MARS OBS - HRII RAW SPECTRA V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MEX-X-MRS-1%2F2%2F3-EXT3-2758-V1.0",
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
-                "mars express"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This is a Mars Express Radio Science data set, collected during the extended mission phase 2010-01-01 to 2012-12-31. It is a Solar Conjunction measurement and covers the time 2011-02-05T17:00:12 to 2011-02-05T20:55:59.500.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mex-x-mrs-1-2-3-ext3-2758-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "mars express"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MEX-X-MRS-1%2F2%2F3-EXT3-2758-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mex-x-mrs-1-2-3-ext3-2758-v1.0",
-            "description": "This is a Mars Express Radio Science data set, collected during the extended mission phase 2010-01-01 to 2012-12-31. It is a Solar Conjunction measurement and covers the time 2011-02-05T17:00:12 to 2011-02-05T20:55:59.500.",
-            "title": "MARS EXPRESS SUN MRS 1/2/3\n                                     EXTENDED MISSION 3 2758 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "MARS EXPRESS SUN MRS 1/2/3\n                                     EXTENDED MISSION 3 2758 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1000000443-LARC.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "The data used in this study were produced by the MISR Science Team;processed/stored at the Langley DAAC;Product is the MISR Level 2 TOA/Cloud Stereo parameters for the SAMUM region;See ProductionDateTime for published Date.",
-            "issued": "2015-07-23",
-            "temporal": "2006-05-12T00:00:00Z/2006-06-15T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2015-07-23",
-            "keyword": [
-                "atmosphere",
-                "earth science",
-                "clouds"
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
-            "identifier": "C1000000443-LARC",
             "description": "This is the Level 2 TOA/Cloud Stereo Product. It contains the Stereoscopically Derived Cloud Mask (SDCM), cloud winds, Reflecting Level Reference Altitude (RLRA), with associated data for the SAMUM_2006 theme.",
-            "title": "MISR L2 TOA/Cloud Stereo Product subset for the SAMUM region V002",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/search/concepts/C1000000443-LARC.html",
-                    "description": "View this dataset on the CMR (Common Metadata Repository)",
                     "@type": "dcat:Distribution",
+                    "description": "View this dataset on the CMR (Common Metadata Repository)",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/search/concepts/C1000000443-LARC.html",
+                    "mediaType": "text/html",
                     "title": "CMR"
                 }
             ],
+            "identifier": "C1000000443-LARC",
+            "issued": "2015-07-23",
+            "keyword": [
+                "atmosphere",
+                "earth science",
+                "clouds"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1000000443-LARC.html",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2015-07-23",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "LaRC"
+            },
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2006-05-12T00:00:00Z/2006-06-15T23:59:59Z",
             "theme": [
                 "SAMUM_2006",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "MISR L2 TOA/Cloud Stereo Product subset for the SAMUM region V002"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://c3.nasa.gov/dashlink/resources/265/",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2010-11-22",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
-            "keyword": [
-                "ames",
-                "nasa",
-                "dashlink"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "SCOTT POLL",
                 "hasEmail": "mailto:scott.d.poll@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Dashlink"
-            },
-            "identifier": "DASHLINK_265",
             "description": "Sample data for the DXC'09 Synthetic Track.",
-            "title": "DXC'09 Synthetic Track Sample Data",
-            "programCode": [
-                "026:029"
-            ],
             "distribution": [
                 {
-                    "mediaType": "application/x-gzip",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/DXC09_Synthetic_SampleData_1.1.tar.gz",
-                    "description": "Synthetic Track Sample Data",
                     "@type": "dcat:Distribution",
+                    "description": "Synthetic Track Sample Data",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/DXC09_Synthetic_SampleData_1.1.tar.gz",
+                    "mediaType": "application/x-gzip",
                     "title": "DXC09_Synthetic_SampleData_1.1.tar.gz"
                 },
                 {
-                    "mediaType": "application/x-gzip",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/DXC09_SyntheticTrackSystems_1.2.tar.gz",
-                    "description": "Synthetic Track System Descriptions",
                     "@type": "dcat:Distribution",
+                    "description": "Synthetic Track System Descriptions",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/DXC09_SyntheticTrackSystems_1.2.tar.gz",
+                    "mediaType": "application/x-gzip",
                     "title": "DXC09_SyntheticTrackSystems_1.2.tar.gz"
                 }
             ],
-            "accrualPeriodicity": "irregular"
+            "identifier": "DASHLINK_265",
+            "issued": "2010-11-22",
+            "keyword": [
+                "ames",
+                "nasa",
+                "dashlink"
+            ],
+            "landingPage": "https://c3.nasa.gov/dashlink/resources/265/",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:029"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Dashlink"
+            },
+            "title": "DXC'09 Synthetic Track Sample Data"
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
-                "rss"
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
-            "identifier": "NASA-757",
             "description": "RSS",
-            "title": "PDS Odyssey Radio Science Data (44)",
-            "programCode": [
-                "026:005"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -529613,112 +529594,140 @@
                     "mediaType": "application/html"
                 }
             ],
-            "accrualPeriodicity": "irregular",
+            "identifier": "NASA-757",
+            "issued": "2018-06-25",
+            "keyword": [
+                "pds",
+                "rss"
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
+            "title": "PDS Odyssey Radio Science Data (44)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://c3.nasa.gov/dashlink/resources/843/",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Kai Goebel",
+                "hasEmail": "mailto:kai.goebel@nasa.gov"
+            },
+            "description": "This data set deals with Maintenance Action Recommendations",
+            "identifier": "DASHLINK_843",
             "issued": "2013-10-30",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
             "keyword": [
                 "ames",
                 "dashlink",
                 "nasa"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Kai Goebel",
-                "hasEmail": "mailto:kai.goebel@nasa.gov"
-            },
+            "landingPage": "https://c3.nasa.gov/dashlink/resources/843/",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:029"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Dashlink"
             },
-            "identifier": "DASHLINK_843",
-            "description": "This data set deals with Maintenance Action Recommendations",
-            "title": "Maintenance Action Recommendation",
-            "programCode": [
-                "026:029"
-            ],
-            "accrualPeriodicity": "irregular"
+            "title": "Maintenance Action Recommendation"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/SeaBASS/SOUTHERN_OCEAN_DRIFTER/DATA001",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/GSFC/SED/ESD/GCDC/OB.DAAC. https://doi.org/10.5067/SeaBASS/SOUTHERN_OCEAN_DRIFTER/DATA001.",
-            "issued": "1996-09-05",
-            "temporal": "1996-09-05T00:00:00Z/2023-04-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-04-06",
-            "keyword": [
-                "oceans",
-                "salinity/density",
-                "ocean temperature",
-                "ocean optics",
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
-            "identifier": "C1633360666-OB_DAAC",
             "description": "Measurements taken by a drifter in the Southern Pacific Ocean in 1996.",
-            "title": "Southern Pacific Ocean drifter measurements in 1996",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSeaBASS%2FSOUTHERN_OCEAN_DRIFTER%2FDATA001",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSeaBASS%2FSOUTHERN_OCEAN_DRIFTER%2FDATA001",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://seabass.gsfc.nasa.gov/experiment/Southern_Ocean_Drifter/",
-                    "description": "Detailed information about the SeaBASS Experiment such as cruises, funding, and investigators",
                     "@type": "dcat:Distribution",
+                    "description": "Detailed information about the SeaBASS Experiment such as cruises, funding, and investigators",
+                    "downloadURL": "https://seabass.gsfc.nasa.gov/experiment/Southern_Ocean_Drifter/",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 }
             ],
+            "identifier": "C1633360666-OB_DAAC",
+            "issued": "1996-09-05",
+            "keyword": [
+                "oceans",
+                "salinity/density",
+                "ocean temperature",
+                "ocean optics",
+                "ocean chemistry",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/SeaBASS/SOUTHERN_OCEAN_DRIFTER/DATA001",
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
+            "temporal": "1996-09-05T00:00:00Z/2023-04-17T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Southern Pacific Ocean drifter measurements in 1996"
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
+                    "downloadURL": "http://turbmodels.larc.nasa.gov/Other_exp_Data/Coanda/ldv_lower_xc_0.9_cm_0.047.dat",
+                    "mediaType": "application/dat"
+                }
             ],
+            "identifier": "NASA-851__6",
+            "issued": "2018-06-25",
             "keyword": [
                 "coanda",
                 "jets",
@@ -529730,305 +529739,275 @@
                 "synthetic",
                 "models"
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
-            "identifier": "NASA-851__6",
-            "description": "2-D Coanda Airfoil with Tangential Wall Jet. This web page provides data from experiments that may be useful for the validation of turbulence models. This resource is expected to grow gradually over time. All data herein arepublicly available.",
-            "title": "Turbulence Models: Data from Other Experiments: 2-D Coanda Airfoil with Tangential Wall Jet",
-            "programCode": [
-                "026:023"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://turbmodels.larc.nasa.gov/Other_exp_Data/Coanda/ldv_lower_xc_0.9_cm_0.047.dat",
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
-            "landingPage": "https://doi.org/10.5067/ASDC/SUBORBITAL/KORUSAQ_MetNav_AircraftInSitu_B200_Data_1",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2022-02-27. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/ASDC/SUBORBITAL/KORUSAQ_MetNav_AircraftInSitu_B200_Data_1.",
-            "issued": "2021-05-14",
-            "temporal": "2016-04-27T00:00:00Z/2016-06-12T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-04-18",
-            "keyword": [
-                "atmosphere",
-                "earth science",
-                "altitude",
-                "atmospheric pressure"
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
-            "identifier": "C2225485398-LARC_ASDC",
             "description": "KORUSAQ_MetNav_AircraftInSitu_B200_Data are in-situ meteorological and navigational data collected onboard the B200 aircraft during the KORUS-AQ field campaign. This dataset contains the navigational data for the B200 aircraft. Data collection for this product is complete.\r\n\r\nThe KORUS-AQ field study was conducted in South Korea during May-June, 2016. The study was jointly sponsored by NASA and Korea\u2019s National Institute of Environmental Research (NIER). The primary objectives were to investigate the factors controlling air quality in Korea (e.g., local emissions, chemical processes, and transboundary transport) and to assess future air quality observing strategies incorporating geostationary satellite observations. To achieve these science objectives, KORUS-AQ adopted a highly coordinated sampling strategy involved surface and airborne measurements including both in-situ and remote sensing instruments.\r\n\r\nSurface observations provided details on ground-level air quality conditions while airborne sampling provided an assessment of conditions aloft relevant to satellite observations and necessary to understand the role of emissions, chemistry, and dynamics in determining air quality outcomes. The sampling region covers the South Korean peninsula and surrounding waters with a primary focus on the Seoul Metropolitan Area. Airborne sampling was primarily conducted from near surface to about 8 km with extensive profiling to characterize the vertical distribution of pollutants and their precursors. The airborne observational data were collected from three aircraft platforms: the NASA DC-8, NASA B-200, and Hanseo King Air. Surface measurements were conducted from 16 ground sites and 2 ships: R/V Onnuri and R/V Jang Mok.\r\n\r\nThe major data products collected from both the ground and air include in-situ measurements of trace gases (e.g., ozone, reactive nitrogen species, carbon monoxide and dioxide, methane, non-methane and oxygenated hydrocarbon species), aerosols (e.g., microphysical and optical properties and chemical composition), active remote sensing of ozone and aerosols, and passive remote sensing of NO2, CH2O, and O3 column densities. These data products support research focused on examining the impact of photochemistry and transport on ozone and aerosols, evaluating emissions inventories, and assessing the potential use of satellite observations in air quality studies.",
-            "title": "KORUS-AQ B200 Aircraft In Situ Meteorological and Navigational Data",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC%2FSUBORBITAL%2FKORUSAQ_MetNav_AircraftInSitu_B200_Data_1",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC%2FSUBORBITAL%2FKORUSAQ_MetNav_AircraftInSitu_B200_Data_1",
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
-                    "description": "Article, The Future of Monitoring Air Quality from Space",
                     "@type": "dcat:Distribution",
+                    "description": "Article, The Future of Monitoring Air Quality from Space",
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
-                    "description": "KORUS-AQ White Paper Outlining NASA\u2019s contribution",
                     "@type": "dcat:Distribution",
+                    "description": "KORUS-AQ White Paper Outlining NASA\u2019s contribution",
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
-                    "downloadURL": "https://doi.org/10.5067/ASDC/SUBORBITAL/KORUSAQ_MetNav_AircraftInSitu_B200_Data_1",
-                    "description": "DOI Data Set Landing Page for KORUSAQ_MetNav_AircraftInSitu_B200_Data_1",
                     "@type": "dcat:Distribution",
+                    "description": "DOI Data Set Landing Page for KORUSAQ_MetNav_AircraftInSitu_B200_Data_1",
+                    "downloadURL": "https://doi.org/10.5067/ASDC/SUBORBITAL/KORUSAQ_MetNav_AircraftInSitu_B200_Data_1",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2225485398-LARC_ASDC",
-                    "description": "Earthdata Search Client for KORUSAQ_MetNav_AircraftInSitu_B200_Data_1",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search Client for KORUSAQ_MetNav_AircraftInSitu_B200_Data_1",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2225485398-LARC_ASDC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/KORUS-AQ/MetNav_AircraftInSitu_B200_Data_1/",
-                    "description": "ASDC Direct Data Download for KORUSAQ_MetNav_AircraftInSitu_B200_Data_1",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for KORUSAQ_MetNav_AircraftInSitu_B200_Data_1",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/KORUS-AQ/MetNav_AircraftInSitu_B200_Data_1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 }
             ],
+            "identifier": "C2225485398-LARC_ASDC",
+            "issued": "2021-05-14",
+            "keyword": [
+                "atmosphere",
+                "earth science",
+                "altitude",
+                "atmospheric pressure"
+            ],
+            "landingPage": "https://doi.org/10.5067/ASDC/SUBORBITAL/KORUSAQ_MetNav_AircraftInSitu_B200_Data_1",
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
             "spatial": "<?xml version=\"1.0\" encoding=\"UTF-8\"?><gml:Polygon xmlns:gml=\"http://www.opengis.net/gml/3.2\" srsName=\"EPSG:9825\"><gml:outerBoundaryIs><gml:LinearRing><gml:posList>27.0 -180.0 27.0 180.0 87.0 180.0 87.0 -180.0 27.0 -180.0</gml:posList></gml:LinearRing></gml:outerBoundaryIs><gml:innerBoundaryIs></gml:innerBoundaryIs></gml:Polygon>",
+            "temporal": "2016-04-27T00:00:00Z/2016-06-12T23:59:59.999Z",
             "theme": [
                 "KORUS-AQ",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "KORUS-AQ B200 Aircraft In Situ Meteorological and Navigational Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.7927/H4VD6WCT",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Center for International Earth Science Information Network - CIESIN - Columbia University, and Information Technology Outreach Services - ITOS - University of Georgia. 2013-05-16. Global Roads Open Access Data Set, Version 1 (gROADSv1). Version 1.00. Palisades, NY. Archived by National Aeronautics and Space Administration, U.S. Government, NASA Socioeconomic Data and Applications Center (SEDAC). https://doi.org/10.7927/H4VD6WCT. https://doi.org/10.7927/H4VD6WCT.",
-            "issued": "2013-05-16",
-            "temporal": "1980-01-01T00:00:00Z/2010-12-31T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2013-05-16",
-            "references": [
-                "https://doi.org/10.7927/H4X63JTX"
-            ],
-            "keyword": [
-                "infrastructure",
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
-            "identifier": "C1000000202-SEDAC",
-            "description": "The Global Roads Open Access Data Set, Version 1 (gROADSv1) was developed under the auspices of the CODATA Global Roads Data Development Task Group. The data set combines the best available roads data by country into a global roads coverage, using the UN Spatial Data Infrastructure Transport (UNSDI-T) version 2 as a common data model. All country road networks have been joined topologically at the borders, and many countries have been edited for internal topology. Source data for each country are provided in the documentation, and users are encouraged to refer to the readme file for use constraints that apply to a small number of countries. Because the data are compiled from multiple sources, the date range for road network representations ranges from the 1980s to 2010 depending on the country (most countries have no confirmed date), and spatial accuracy varies. The baseline global data set was compiled by the Information Technology Outreach Services (ITOS) of the University of Georgia. Updated data for 27 countries and 6 smaller geographic entities were assembled by Columbia University's Center for International Earth Science Information Network (CIESIN), with a focus largely on developing countries with the poorest data coverage.",
-            "release-place": "Palisades, NY",
-            "graphic-preview-description": "Maps Download Page",
             "creator": "Center for International Earth Science Information Network - CIESIN - Columbia University, and Information Technology Outreach Services - ITOS - University of Georgia",
-            "title": "Global Roads Open Access Data Set, Version 1 (gROADSv1)",
-            "graphic-preview-file": "https://sedac.ciesin.columbia.edu/data/set/groads-global-roads-open-access-v1/maps",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The Global Roads Open Access Data Set, Version 1 (gROADSv1) was developed under the auspices of the CODATA Global Roads Data Development Task Group. The data set combines the best available roads data by country into a global roads coverage, using the UN Spatial Data Infrastructure Transport (UNSDI-T) version 2 as a common data model. All country road networks have been joined topologically at the borders, and many countries have been edited for internal topology. Source data for each country are provided in the documentation, and users are encouraged to refer to the readme file for use constraints that apply to a small number of countries. Because the data are compiled from multiple sources, the date range for road network representations ranges from the 1980s to 2010 depending on the country (most countries have no confirmed date), and spatial accuracy varies. The baseline global data set was compiled by the Information Technology Outreach Services (ITOS) of the University of Georgia. Updated data for 27 countries and 6 smaller geographic entities were assembled by Columbia University's Center for International Earth Science Information Network (CIESIN), with a focus largely on developing countries with the poorest data coverage.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.7927%2FH4VD6WCT",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.7927%2FH4VD6WCT",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/downloads/maps/groads/groads-global-roads-open-access-v1/groads-v1-global-thumbnail.jpg",
-                    "description": "Sample browse graphic of the data set.",
                     "@type": "dcat:Distribution",
+                    "description": "Sample browse graphic of the data set.",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/downloads/maps/groads/groads-global-roads-open-access-v1/groads-v1-global-thumbnail.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/groads-global-roads-open-access-v1/data-download",
-                    "description": "Data Download Page",
                     "@type": "dcat:Distribution",
+                    "description": "Data Download Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/groads-global-roads-open-access-v1/data-download",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/groads-global-roads-open-access-v1/maps",
-                    "description": "Maps Download Page",
                     "@type": "dcat:Distribution",
+                    "description": "Maps Download Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/groads-global-roads-open-access-v1/maps",
+                    "mediaType": "text/html",
                     "title": "Get a related map visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://sedac.ciesin.columbia.edu/data/set/groads-global-roads-open-access-v1/docs",
-                    "description": "Documentation Page",
                     "@type": "dcat:Distribution",
+                    "description": "Documentation Page",
+                    "downloadURL": "http://sedac.ciesin.columbia.edu/data/set/groads-global-roads-open-access-v1/docs",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/groads-global-roads-open-access-v1",
-                    "description": "Data Set\u00a0Overview Page",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set\u00a0Overview Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/groads-global-roads-open-access-v1",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "graphic-preview-description": "Maps Download Page",
+            "graphic-preview-file": "https://sedac.ciesin.columbia.edu/data/set/groads-global-roads-open-access-v1/maps",
+            "identifier": "C1000000202-SEDAC",
+            "issued": "2013-05-16",
+            "keyword": [
+                "infrastructure",
+                "human dimensions",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.7927/H4VD6WCT",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2013-05-16",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "SEDAC"
+            },
+            "references": [
+                "https://doi.org/10.7927/H4X63JTX"
+            ],
+            "release-place": "Palisades, NY",
             "spatial": "-180.0 -55.0 180.0 90.0",
+            "temporal": "1980-01-01T00:00:00Z/2010-12-31T00:00:00Z",
             "theme": [
                 "GROADS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Global Roads Open Access Data Set, Version 1 (gROADSv1)"
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
-                "sharing",
-                "appel",
-                "ask magazine",
-                "knowledge"
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
-            "identifier": "NASA-860__40",
             "description": "Academy of Program/Project & Engineering Leadership's ASK Magazine archive.",
-            "title": "Academy of Program/Project & Engineering Leadership ASK Magazine Past Issues",
-            "programCode": [
-                "026:045"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -530036,56 +530015,89 @@
                     "mediaType": "application/pdf"
                 }
             ],
-            "accrualPeriodicity": "R/P3M",
+            "identifier": "NASA-860__40",
+            "issued": "2018-06-25",
+            "keyword": [
+                "sharing",
+                "appel",
+                "ask magazine",
+                "knowledge"
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
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=GSSR-M-RTLS-5-ALT-V1.0",
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
-                "pre-magellan",
-                "mars"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This data set consists of Martian radii and elevations (relative to the 6 millibar reference surface) measured relative to JPL ephemeris DE_118. The data were obtained by the Goldstone Solar System Radar during the oppositions of 1971-1982. Present form of table generated by R. Mehlman, UCLA/IGPP.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.gssr-m-rtls-5-alt-v1.0_bf25-fd4w",
+            "issued": "2018-06-26",
+            "keyword": [
+                "pre-magellan",
+                "mars"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=GSSR-M-RTLS-5-ALT-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.gssr-m-rtls-5-alt-v1.0_bf25-fd4w",
-            "description": "This data set consists of Martian radii and elevations (relative to the 6 millibar reference surface) measured relative to JPL ephemeris DE_118. The data were obtained by the Goldstone Solar System Radar during the oppositions of 1971-1982. Present form of table generated by R. Mehlman, UCLA/IGPP.",
-            "title": "GOLDSTONE MARS RADIO TELESCOPE DERIVED ALTIMETRY V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "GOLDSTONE MARS RADIO TELESCOPE DERIVED ALTIMETRY V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.nasa.gov/d/bf5v-ajgz",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Site Admin",
+                "hasEmail": "mailto:podaac@podaac.jpl.nasa.gov"
+            },
+            "description": "PO.DAAC is an element of the Earth Observing System Data Information System (EOSDIS). PO.DAAC's primary responsibility is to provide distribution and archive support for NASA's physical oceanography missions such as TOPEX/Poseidon and SeaWinds on QuikSCAT. However, PO.DAAC additionally collaborates with other institutes to acquire complementary data products and value-added services.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://podaac.jpl.nasa.gov/dataaccess",
+                    "mediaType": "text/html"
+                }
+            ],
+            "identifier": "NASA-0000102",
             "issued": "2018-06-25",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
             "keyword": [
                 "opendap",
                 "apps",
@@ -530106,82 +530118,72 @@
                 "wind",
                 "wist"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Site Admin",
-                "hasEmail": "mailto:podaac@podaac.jpl.nasa.gov"
-            },
+            "landingPage": "https://data.nasa.gov/d/bf5v-ajgz",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:046"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "NASA-0000102",
-            "description": "PO.DAAC is an element of the Earth Observing System Data Information System (EOSDIS). PO.DAAC's primary responsibility is to provide distribution and archive support for NASA's physical oceanography missions such as TOPEX/Poseidon and SeaWinds on QuikSCAT. However, PO.DAAC additionally collaborates with other institutes to acquire complementary data products and value-added services.",
-            "title": "Physical Oceanography Distributed Active Archive Center (PO.DAAC)",
-            "programCode": [
-                "026:046"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://podaac.jpl.nasa.gov/dataaccess",
-                    "mediaType": "text/html"
-                }
-            ],
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Management/Operations"
-            ]
+            ],
+            "title": "Physical Oceanography Distributed Active Archive Center (PO.DAAC)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=ER2-E-AVIR-3-RDR-IMAGE-V1.0",
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
+            "description": "The Airborne Visible and Infared Imaging Spectrometer (AVIRIS) data are divided into 10x10 square kilometer scenes for purposes of standard product generation. More than 40 scenes were generated during GRSFE, more than 20 of which are included on the CD-ROMs, covering a variety of surfaces. Lunar Crater was covered several times in one day (under clear atmospheric conditions) in order to evaluate atmospheric scattering and absorption removal algorithms and to explore extraction of roughness information using variable incidence angle AVIRIS data. The AVIRIS multi-temporal data were acquired at the same time that ground-based, multi-spectral measurements of atmospheric optical depth, and sky radiance at varying scattering angles were acquired, along with surface bidirectional reflectance data. Accurate wavelength calibration of AVIRIS was performed by JPL using laboratory measurements acquired before and after the AVIRIS flights. An additional check on the wavelength calibration can be made by comparing the positions of known atmospheric absorption features to their locations in actual AVIRIS data.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.er2-e-avir-3-rdr-image-v1.0_bf5x-5vi9",
+            "issued": "2021-05-21",
+            "keyword": [
+                "geologic remote sensing field experiment",
+                "earth"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=ER2-E-AVIR-3-RDR-IMAGE-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.er2-e-avir-3-rdr-image-v1.0_bf5x-5vi9",
-            "description": "The Airborne Visible and Infared Imaging Spectrometer (AVIRIS) data are divided into 10x10 square kilometer scenes for purposes of standard product generation. More than 40 scenes were generated during GRSFE, more than 20 of which are included on the CD-ROMs, covering a variety of surfaces. Lunar Crater was covered several times in one day (under clear atmospheric conditions) in order to evaluate atmospheric scattering and absorption removal algorithms and to explore extraction of roughness information using variable incidence angle AVIRIS data. The AVIRIS multi-temporal data were acquired at the same time that ground-based, multi-spectral measurements of atmospheric optical depth, and sky radiance at varying scattering angles were acquired, along with surface bidirectional reflectance data. Accurate wavelength calibration of AVIRIS was performed by JPL using laboratory measurements acquired before and after the AVIRIS flights. An additional check on the wavelength calibration can be made by comparing the positions of known atmospheric absorption features to their locations in actual AVIRIS data.",
-            "title": "ER2 EARTH AVIRIS CALIBRATED REDUCED DATA RECORD IMAGE V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ER2 EARTH AVIRIS CALIBRATED REDUCED DATA RECORD IMAGE V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MEX-M-SPI-2-UVRDR-CLEANED-EXT1-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "The Mars Express SPICAM level 1A UV dataset contains measurements from the ultra violet SPICAM spectrometer collected during MARS phase with some corrections and processing",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mex-m-spi-2-uvrdr-cleaned-ext1-v1.0",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2021-05-21",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "sun",
                 "earth",
@@ -530194,251 +530196,258 @@
                 "mars express",
                 "comet"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MEX-M-SPI-2-UVRDR-CLEANED-EXT1-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mex-m-spi-2-uvrdr-cleaned-ext1-v1.0",
-            "description": "The Mars Express SPICAM level 1A UV dataset contains measurements from the ultra violet SPICAM spectrometer collected during MARS phase with some corrections and processing",
-            "title": "MEX_EXT1_SPICAM_MARS_CLEANED_UV_RDR_V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "MEX_EXT1_SPICAM_MARS_CLEANED_UV_RDR_V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/GPMGV/IPHEX/WBAND/DATA101",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Tsay, Si-Chee , Adrian  Loftus and Peter  Pantina.2016. GPM GROUND VALIDATION ACHIEVE W-BAND CLOUD RADAR IPHEX [indicate subset used]. Dataset available online from the NASA Global Hydrometeorology Resource Center DAAC, Huntsville, Alabama, U.S.A. DOI: http://dx.doi.org/10.5067/GPMGV/IPHEX/WBAND/DATA101",
-            "issued": "2016-11-28",
-            "temporal": "2014-05-09T12:54:13Z/2014-06-14T18:35:39Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-05-25",
-            "keyword": [
-                "earth science",
-                "spectral/engineering",
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
-            "identifier": "C1979831259-GHRC_DAAC",
             "description": "The GPM Ground Validation ACHIEVE W-band Cloud Radar IPHEx dataset consists of cloud and light precipitation radar observations gathered during the Global Precipitation Measurement (GPM) mission Ground Validation Integrated Precipitation and Hydrology Experiment (IPHEx) Intensive Observing Period (IOP) in North Carolina from May 1 through June 15, 2014. The goal of IPHEx was to evaluate the accuracy of satellite precipitation measurements and use the collected data for hydrology models in the region. The dataset includes data from the ProSensing 95 GHz W-band cloud radar, which is part of the NASA Goddard Space Flight Center (GSFC) Aerosol, Cloud, Humidity, Interactions Exploring and Validating Enterprise (ACHIEVE) ground-based mobile laboratory. The W-band cloud radar is a scanning 95 GHz dual-polarization (horizontal transmission and co- and cross-polar receiving) Doppler radar used for observing liquid and ice clouds and light precipitation. The instrument measures co- and cross-polar reflectivity, radial velocity, Doppler spectrum width, and signal-to-noise ratio. Linear depolarization ratio was derived from the measured parameters. During the IPHEx campaign, the W-Band radar was used exclusively in vertical-pointing mode. The dataset files are available from May 9 through June 14, 2014 in netCDF-3 data format.",
-            "title": "GPM GROUND VALIDATION ACHIEVE W-BAND CLOUD RADAR IPHEX V1",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGPMGV%2FIPHEX%2FWBAND%2FDATA101",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGPMGV%2FIPHEX%2FWBAND%2FDATA101",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=gpmwbandiphx",
-                    "description": "Files may be downloaded directly to your workstation from this link",
                     "@type": "dcat:Distribution",
+                    "description": "Files may be downloaded directly to your workstation from this link",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=gpmwbandiphx",
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
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/iphex/Wband/doc/gpmwbandiphx_dataset.pdf",
-                    "description": "The guide document contains detailed information about the dataset",
                     "@type": "dcat:Distribution",
+                    "description": "The guide document contains detailed information about the dataset",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/iphex/Wband/doc/gpmwbandiphx_dataset.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/opendap/fieldCampaigns/gpmValidation/iphex/Wband/",
-                    "description": "OPeNDAP",
                     "@type": "dcat:Distribution",
+                    "description": "OPeNDAP",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/opendap/fieldCampaigns/gpmValidation/iphex/Wband/",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://dx.doi.org/10.1175/1520-0426%281997%29014%3C0003%3ADOIHAU%3E2.0.CO%3B2",
-                    "description": "Detection of Ice Hydrometer Alignment Using an Airborne W-band Polarimetric Radar",
                     "@type": "dcat:Distribution",
+                    "description": "Detection of Ice Hydrometer Alignment Using an Airborne W-band Polarimetric Radar",
+                    "downloadURL": "http://dx.doi.org/10.1175/1520-0426%281997%29014%3C0003%3ADOIHAU%3E2.0.CO%3B2",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://dx.doi.org/10.1109/36.298002",
-                    "description": "An airborne 95 GHz dual-polarized radar for cloud studies",
                     "@type": "dcat:Distribution",
+                    "description": "An airborne 95 GHz dual-polarized radar for cloud studies",
+                    "downloadURL": "http://dx.doi.org/10.1109/36.298002",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/home/field-campaigns/iphex",
-                    "description": "Project Home Page",
                     "@type": "dcat:Distribution",
+                    "description": "Project Home Page",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/home/field-campaigns/iphex",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/home/micro-articles/investigation-microphysics-and-precipitation-atlantic-coast-threatening-snowstorms",
-                    "description": "Investigation of Microphysics and Precipitation for Atlantic Coast-Threatening Snowstorms (IMPACTS) Field Campaign",
                     "@type": "dcat:Distribution",
+                    "description": "Investigation of Microphysics and Precipitation for Atlantic Coast-Threatening Snowstorms (IMPACTS) Field Campaign",
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
+            "identifier": "C1979831259-GHRC_DAAC",
+            "issued": "2016-11-28",
+            "keyword": [
+                "earth science",
+                "spectral/engineering",
+                "radar"
+            ],
+            "landingPage": "https://doi.org/10.5067/GPMGV/IPHEX/WBAND/DATA101",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2022-05-25",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/MSFC/GHRC"
+            },
             "spatial": "-83.0947 35.5198 -83.0947 35.5198",
+            "temporal": "2014-05-09T12:54:13Z/2014-06-14T18:35:39Z",
             "theme": [
                 "IPHEx",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "GPM GROUND VALIDATION ACHIEVE W-BAND CLOUD RADAR IPHEX V1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/MC3E/NEXRAD/DATA205",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "National Weather Service .2014. GPM GROUND VALIDATION KTWX NEXRAD MC3E [indicate subset used]. Dataset available online from the NASA Global Hydrometeorology Resource Center DAAC, Huntsville, Alabama, U.S.A. DOI: http://dx.doi.org/10.5067/MC3E/NEXRAD/DATA205",
-            "issued": "2014-10-03",
-            "temporal": "2011-06-01T00:08:23Z/2011-06-01T23:59:09Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-05-10",
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
-            "identifier": "C1979618378-GHRC_DAAC",
             "description": "The GPM Ground Validation KTWX NEXRAD MC3E dataset was collected from April 22, 2011 to June 6, 2011 for the Midlatitude Continental Convective Clouds Experiment (MC3E) which took place in central Oklahoma. The overarching goal of MC3E was to provide the most complete characterization of convective cloud systems, precipitation, and the environment that has ever been obtained, providing constraints for model cumulus parameterizations and space-based rainfall retrieval algorithms over land that had never before been available. The Next Generation Weather Radar system (NEXRAD) is comprised of 160 Weather Surveillance Radar-1988 Doppler (WSR-88D) sites throughout the United States and select overseas locations. The GPM Ground Validation NEXRAD MC3E data files are available as compressed binary files.",
-            "graphic-preview-description": "N/A",
-            "title": "GPM GROUND VALIDATION KTWX NEXRAD MC3E V1",
-            "graphic-preview-file": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/mc3e/NEXRAD/KTWX/browse/",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMC3E%2FNEXRAD%2FDATA205",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMC3E%2FNEXRAD%2FDATA205",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=gpmktwxmc3e",
-                    "description": "Files may be downloaded directly to your workstation from this link",
                     "@type": "dcat:Distribution",
+                    "description": "Files may be downloaded directly to your workstation from this link",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=gpmktwxmc3e",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/browse_sample/fieldCampaigns/gpmValidation/mc3e/gpmktwxmc3e/2011-06-01_22-04-23_KTWX_COMPOSITE.png",
-                    "description": "Sample browse image",
                     "@type": "dcat:Distribution",
+                    "description": "Sample browse image",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/browse_sample/fieldCampaigns/gpmValidation/mc3e/gpmktwxmc3e/2011-06-01_22-04-23_KTWX_COMPOSITE.png",
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
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/mc3e/NEXRAD/KTWX/browse/",
-                    "description": "N/A",
                     "@type": "dcat:Distribution",
+                    "description": "N/A",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/mc3e/NEXRAD/KTWX/browse/",
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
+            "graphic-preview-file": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/mc3e/NEXRAD/KTWX/browse/",
+            "identifier": "C1979618378-GHRC_DAAC",
+            "issued": "2014-10-03",
+            "keyword": [
+                "earth science",
+                "radar",
+                "spectral/engineering"
+            ],
+            "landingPage": "https://doi.org/10.5067/MC3E/NEXRAD/DATA205",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2022-05-10",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/MSFC/GHRC"
+            },
             "spatial": "-101.55 34.86 -90.9161 43.1339",
+            "temporal": "2011-06-01T00:08:23Z/2011-06-01T23:59:09Z",
             "theme": [
                 "MC3E",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "GPM GROUND VALIDATION KTWX NEXRAD MC3E V1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://appel.nasa.gov/knowledge-sharing/publications/appel-releases-ibook-html/",
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
+            "description": "The NASA Academy of Program/Project & Engineering Leadership (APPEL) is excited to announce the public release of Orbital Debris Management and Risk Mitigation, its first publication of NASA training materials using the iBook format.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://itunes.apple.com/us/course/orbital-debris-management/id566557528?i=307466871&mt=2",
+                    "mediaType": "application/x-itunes-itlp"
+                }
             ],
+            "identifier": "NASA-863__2",
+            "issued": "2018-06-25",
             "keyword": [
                 "appel",
                 "management",
@@ -530449,45 +530458,38 @@
                 "ibook",
                 "knowledge"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Ed Hoffman",
-                "hasEmail": "mailto:ehoffman@nasa.gov"
-            },
+            "landingPage": "http://appel.nasa.gov/knowledge-sharing/publications/appel-releases-ibook-html/",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:045"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "NASA-863__2",
-            "description": "The NASA Academy of Program/Project & Engineering Leadership (APPEL) is excited to announce the public release of Orbital Debris Management and Risk Mitigation, its first publication of NASA training materials using the iBook format.",
-            "title": "Academy of Program/Project & Engineering Leadership Orbital Debris Management and Risk Mitigation",
-            "programCode": [
-                "026:045"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://itunes.apple.com/us/course/orbital-debris-management/id566557528?i=307466871&mt=2",
-                    "mediaType": "application/x-itunes-itlp"
-                }
+            "references": [
+                "http://km.nasa.gov/knowledge-map/"
             ],
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Management/Operations"
-            ]
+            ],
+            "title": "Academy of Program/Project & Engineering Leadership Orbital Debris Management and Risk Mitigation"
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
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.iue-c-lwp-3-edr-iuecdb-v1.0_bfdj-95ct",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "p/levy 1 (1991 l3)",
                 "support archives",
@@ -530531,39 +530533,39 @@
                 "10p/tempel 2 (1873 n1)",
                 "p/mcnaught-russell 1 (1994 x1)"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=IUE-C-LWP-3-EDR-IUECDB-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.iue-c-lwp-3-edr-iuecdb-v1.0_bfdj-95ct",
-            "description": "IUE Long-Wavelength Prime (LWP) observations of comets",
-            "title": "IUE LWP DATA OF COMETS",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "IUE LWP DATA OF COMETS"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-2-ESC2-67PCHURYUMOV-M16-V3.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This CODMAC level 2 data set contains uncalibrated image data in DN unit, acquired by the OSIRIS Wide Angle Camera on the Rosetta spacecraft during the COMET ESCORT 2 mission phase, covering the period from 2015-05-05T23:25:00.000 to 2015-06-02T23:24:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V3.0 supersedes previous deliveries of the same dataset with the following changes since the last version: Lien corrected dataset after the July and October 2018 PSA/PDS external peer reviews. Updated documentation and ancillary files, added document on bandpass filter. Updated SCIENCE_USER_GUIDE_V03.PDF to include one section about FAQ and one section about image data quality. Added shutter backtravel and readout issues to image quality map. Updated DATA_QUALITY_ID keyword in image header. Improved handling of images with missing packets. Included FITs files. Browse products changed to the same size as the original image.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-2-esc2-67pchuryumov-m16-v3.0_bfdk-ysi3",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "67p/churyumov-gerasimenko 1 (1969 r1)",
                 "vega",
@@ -530571,66 +530573,43 @@
                 "dark",
                 "bias"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-2-ESC2-67PCHURYUMOV-M16-V3.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-2-esc2-67pchuryumov-m16-v3.0_bfdk-ysi3",
-            "description": "This CODMAC level 2 data set contains uncalibrated image data in DN unit, acquired by the OSIRIS Wide Angle Camera on the Rosetta spacecraft during the COMET ESCORT 2 mission phase, covering the period from 2015-05-05T23:25:00.000 to 2015-06-02T23:24:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V3.0 supersedes previous deliveries of the same dataset with the following changes since the last version: Lien corrected dataset after the July and October 2018 PSA/PDS external peer reviews. Updated documentation and ancillary files, added document on bandpass filter. Updated SCIENCE_USER_GUIDE_V03.PDF to include one section about FAQ and one section about image data quality. Added shutter backtravel and readout issues to image quality map. Updated DATA_QUALITY_ID keyword in image header. Improved handling of images with missing packets. Included FITs files. Browse products changed to the same size as the original image.",
-            "title": "ROSETTA-ORBITER 67P OSIWAC 2 ESC2-MTP016 EDR V3.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P OSIWAC 2 ESC2-MTP016 EDR V3.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/GNSS/GDGPS_daily_acc_POD_clk_corr_gal_001",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, CDDIS. https://doi.org/10.5067/GNSS/GDGPS_daily_acc_POD_clk_corr_gal_001\r\n.",
-            "issued": "1992-01-01",
-            "temporal": "2023-10-01T00:00:00Z/2024-12-02T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-26",
-            "keyword": [
-                "geodetics",
-                "earth science",
-                "gravity/gravitational field",
-                "solid earth",
-                "tectonics"
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
-            "identifier": "C2792578374-CDDIS",
             "description": "This product contains a time series of clock biases for healthy satellites in the Galileo constellation that are accumulated every minute throughout the day. In addition, formal 1-sigma uncertainties for the corrections are provided. The product is generated at JPL's Global Differential GPS Operations Centers in real-time. The data in this product can be concatenated with other daily products to provide larger coverage in time.",
-            "title": "Ground-Based Global Navigation Satellite System (GNSS) Guardian Galileo daily accumulated real-time POD Clock Corrections (60-second sampling, 24-hour files) from NASA CDDIS",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGNSS%2FGDGPS_daily_acc_POD_clk_corr_gal_001%0D%0A",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGNSS%2FGDGPS_daily_acc_POD_clk_corr_gal_001%0D%0A",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
@@ -530646,61 +530625,96 @@
                     "title": "Download this dataset"
                 }
             ],
+            "identifier": "C2792578374-CDDIS",
+            "issued": "1992-01-01",
+            "keyword": [
+                "geodetics",
+                "earth science",
+                "gravity/gravitational field",
+                "solid earth",
+                "tectonics"
+            ],
+            "landingPage": "https://doi.org/10.5067/GNSS/GDGPS_daily_acc_POD_clk_corr_gal_001",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2024-11-26",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "CDDIS"
+            },
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2023-10-01T00:00:00Z/2024-12-02T00:00:00Z",
             "theme": [
                 "IGS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Ground-Based Global Navigation Satellite System (GNSS) Guardian Galileo daily accumulated real-time POD Clock Corrections (60-second sampling, 24-hour files) from NASA CDDIS"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-MIDAS-3-ESC4-SAMPLES-V2.0",
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
+            "description": "The Micro-Imaging Dust Analysis System (MIDAS) is an instrument on the\nROSETTA Orbiter that will provide 3D images and statistical parameters\nof pristine cometary particles, collected in the vicinity of comet\n67P/Churyumov-Gerasimenko. This data set includes all data from the\nCOMET ESCORT 4 mission phase. The current release is based on the results of the Comet Science\nReviews held in Feb 2016 and Oct 2017 and supersedes version 1.0.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-midas-3-esc4-samples-v2.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-MIDAS-3-ESC4-SAMPLES-V2.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-midas-3-esc4-samples-v2.0",
-            "description": "The Micro-Imaging Dust Analysis System (MIDAS) is an instrument on the\nROSETTA Orbiter that will provide 3D images and statistical parameters\nof pristine cometary particles, collected in the vicinity of comet\n67P/Churyumov-Gerasimenko. This data set includes all data from the\nCOMET ESCORT 4 mission phase. The current release is based on the results of the Comet Science\nReviews held in Feb 2016 and Oct 2017 and supersedes version 1.0.",
-            "title": "ROSETTA-ORBITER 67P MIDAS 3 ESC4 SAMPLES V2.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P MIDAS 3 ESC4 SAMPLES V2.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.nasa.gov/d/bfim-tktm",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "GeneLab Outreach",
+                "hasEmail": "mailto:genelab-outreach@lists.nasa.gov"
+            },
+            "description": "We investigated differentially regulated genes in human Jurkat T lymphocytic cells in 20s and 5min microgravity and in hypergravity and compared expression profiles to identify potential gravity-regulated genes and adaptation processes.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "GeneLab Study Page",
+                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-172",
+                    "mediaType": "text/html",
+                    "title": "Dynamic gene expression response to altered gravity in human T cells (parabolic flight)"
+                }
+            ],
+            "identifier": "nasa_genelab_GLDS-172_bfim-tktm",
             "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
             "keyword": [
                 "nucleic acid hybridization",
                 "growth protocol",
@@ -530713,69 +530727,33 @@
                 "labeling",
                 "hypergravity"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "GeneLab Outreach",
-                "hasEmail": "mailto:genelab-outreach@lists.nasa.gov"
-            },
+            "landingPage": "https://data.nasa.gov/d/bfim-tktm",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "nasa_genelab_GLDS-172_bfim-tktm",
-            "description": "We investigated differentially regulated genes in human Jurkat T lymphocytic cells in 20s and 5min microgravity and in hypergravity and compared expression profiles to identify potential gravity-regulated genes and adaptation processes.",
-            "title": "Dynamic gene expression response to altered gravity in human T cells (parabolic flight)",
-            "programCode": [
-                "026:005"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-172",
-                    "description": "GeneLab Study Page",
-                    "@type": "dcat:Distribution",
-                    "title": "Dynamic gene expression response to altered gravity in human T cells (parabolic flight)"
-                }
-            ],
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "Dynamic gene expression response to altered gravity in human T cells (parabolic flight)"
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
-                "turbulence",
-                "incompressible",
-                "flow",
-                "cases"
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
-            "identifier": "NASA-845",
             "description": "This grouping contains more recent incompressible-flow cases.",
-            "title": "Collaborative Testing of Turbulence Models: More Recent Incompressible Flow Cases",
-            "programCode": [
-                "026:023"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -530783,200 +530761,224 @@
                     "mediaType": "application/dat"
                 }
             ],
-            "accrualPeriodicity": "irregular",
+            "identifier": "NASA-845",
+            "issued": "2018-06-25",
+            "keyword": [
+                "models",
+                "turbulence",
+                "incompressible",
+                "flow",
+                "cases"
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
+            "title": "Collaborative Testing of Turbulence Models: More Recent Incompressible Flow Cases"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/NAMMA/APR2/DATA201",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Im, Eastwood.2006. NAMMA SECOND GENERATION AIRBORNE PRECIPITATION RADAR (APR-2) [indicate subset used]. Dataset available online from the NASA Global Hydrometeorology Resource Center DAAC, Huntsville, Alabama, U.S.A. DOI: http://dx.doi.org/10.5067/NAMMA/APR2/DATA201",
-            "issued": "2006-06-01",
-            "temporal": "2006-08-19T15:19:15Z/2006-09-12T18:28:40Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-05-19",
-            "keyword": [
-                "atmosphere",
-                "earth science",
-                "spectral/engineering",
-                "precipitation",
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
-            "identifier": "C1979884964-GHRC_DAAC",
             "description": "The NAMMA Second Generation Airborne Precipitation Radar (APR-2) dataset was collected by using the Second Generation Airborne Precipitation Radar (APR-2), which is a dual-frequency (14 GHz and 35 GHz), Doppler, dual-polarization radar system that includes digital, real-time pulse compression, extremely compact RF electronics, and a large deployable dual-frequency cylindrical parabolic antenna subsystem. This system measures radar reflectivity and doppler velocity at both the Ku- and Ka-band. These data files were generated during support of the NASA African Monsoon Multidisciplinary Analyses (NAMMA) campaign, a field research investigation sponsored by the Science Mission Directorate of the National Aeronautics and Space Administration (NASA). This mission was based in the Cape Verde Islands, 350 miles off the coast of Senegal in west Africa. Commencing in August 2006, NASA scientists employed surface observation networks and aircraft to characterize the evolution and structure of African Easterly Waves (AEWs) and Mesoscale Convective Systems over continental western Africa, and their associated impacts on regional water and energy budgets.",
-            "graphic-preview-description": "N/A",
-            "title": "NAMMA SECOND GENERATION AIRBORNE PRECIPITATION RADAR (APR-2) V1",
-            "graphic-preview-file": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/namma/APR2/browse/",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FNAMMA%2FAPR2%2FDATA201",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FNAMMA%2FAPR2%2FDATA201",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=namapr2",
-                    "description": "Files may be downloaded directly to your workstation from this link",
                     "@type": "dcat:Distribution",
+                    "description": "Files may be downloaded directly to your workstation from this link",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=namapr2",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/namma/APR2/browse/namma_apr2_20060819_165354_41.hdf.jpg",
-                    "description": "Sample browse image",
                     "@type": "dcat:Distribution",
+                    "description": "Sample browse image",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/namma/APR2/browse/namma_apr2_20060819_165354_41.hdf.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://ghrc.nsstc.nasa.gov/uso/ds_docs/namma/namapr2/namapr2_dataset.html",
-                    "description": "The guide document contains detailed information about the dataset",
                     "@type": "dcat:Distribution",
+                    "description": "The guide document contains detailed information about the dataset",
+                    "downloadURL": "http://ghrc.nsstc.nasa.gov/uso/ds_docs/namma/namapr2/namapr2_dataset.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/msword",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/doc/namma/namapr2/NAMMA06_APR2_Format_HDFv41.doc",
-                    "description": "Content of \u00bf\u00bf\u00bfnamma_apr2_yymmdd_hhmmss_41.hdf\u00bf\u00bf\u00bf Data Format (version 4.1)",
                     "@type": "dcat:Distribution",
+                    "description": "Content of \u00bf\u00bf\u00bfnamma_apr2_yymmdd_hhmmss_41.hdf\u00bf\u00bf\u00bf Data Format (version 4.1)",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/doc/namma/namapr2/NAMMA06_APR2_Format_HDFv41.doc",
+                    "mediaType": "application/msword",
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
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/namma/APR2/browse/",
-                    "description": "N/A",
                     "@type": "dcat:Distribution",
+                    "description": "N/A",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/namma/APR2/browse/",
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
+            "graphic-preview-file": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/namma/APR2/browse/",
+            "identifier": "C1979884964-GHRC_DAAC",
+            "issued": "2006-06-01",
+            "keyword": [
+                "atmosphere",
+                "earth science",
+                "spectral/engineering",
+                "precipitation",
+                "radar"
+            ],
+            "landingPage": "https://doi.org/10.5067/NAMMA/APR2/DATA201",
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
             "spatial": "-34.1533 7.03833 -13.4683 21.4717",
+            "temporal": "2006-08-19T15:19:15Z/2006-09-12T18:28:40Z",
             "theme": [
                 "NAMMA",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "NAMMA SECOND GENERATION AIRBORNE PRECIPITATION RADAR (APR-2) V1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-COMPIL-3-TNO-CEN-COLOR-V10.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This data set is intended to include published broadband colors of centaurs and Transneptunian Objects (TNOs) published through March 2014. It includes some comets with Centaur orbits. It supersedes all versions of the TNO colors data set EAR-A-3-RDR-TNO-PHOT.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-compil-3-tno-cen-color-v10.0_bfje-pse9",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "support archives",
                 "asteroid",
                 "comet"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-COMPIL-3-TNO-CEN-COLOR-V10.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-compil-3-tno-cen-color-v10.0_bfje-pse9",
-            "description": "This data set is intended to include published broadband colors of centaurs and Transneptunian Objects (TNOs) published through March 2014. It includes some comets with Centaur orbits. It supersedes all versions of the TNO colors data set EAR-A-3-RDR-TNO-PHOT.",
-            "title": "TNO AND CENTAUR COLORS V10.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "TNO AND CENTAUR COLORS V10.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RL-CAL-ROMAP-2-CR2-MAG-V1.0",
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
+            "description": "This archive contains level 2 data from the ROMAP-MAG instrument onboard ROSETTA Lander, acquired during the CR2 (cruise 2) phase. It also contains documentation which describes the ROMAP experiment. The data archived in this data set conform to the Planetary Data System (PDS) Standards, Version 3.6.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.rl-cal-romap-2-cr2-mag-v1.0_bfji-zc2b",
+            "issued": "2021-05-21",
+            "keyword": [
+                "calibration",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RL-CAL-ROMAP-2-CR2-MAG-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.rl-cal-romap-2-cr2-mag-v1.0_bfji-zc2b",
-            "description": "This archive contains level 2 data from the ROMAP-MAG instrument onboard ROSETTA Lander, acquired during the CR2 (cruise 2) phase. It also contains documentation which describes the ROMAP experiment. The data archived in this data set conform to the Planetary Data System (PDS) Standards, Version 3.6.",
-            "title": "ROSETTA-LANDER CAL ROMAP 2 CR2 MAG\n                            V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-LANDER CAL ROMAP 2 CR2 MAG\n                            V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-CAL%2FJ%2FM-ALICE-2-MARS-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This data set contains CODMAC level 2 instrument checkout data acquired by the Rosetta Orbiter ALICE UV Spectrometer during the Mars Swing-by phase of the Rosetta mission, which occurred 2006-07-29 to 2007-05-28. Data include the calibration observations of payload checkout (PC) 4, observations of Mars, and observations of Jupiter and the Io plasma torus.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-cal-j-m-alice-2-mars-v1.0_bfnp-epee",
             "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "international rosetta mission",
                 "saturn",
@@ -530985,35 +530987,47 @@
                 "unknown",
                 "jupiter"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-CAL%2FJ%2FM-ALICE-2-MARS-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-cal-j-m-alice-2-mars-v1.0_bfnp-epee",
-            "description": "This data set contains CODMAC level 2 instrument checkout data acquired by the Rosetta Orbiter ALICE UV Spectrometer during the Mars Swing-by phase of the Rosetta mission, which occurred 2006-07-29 to 2007-05-28. Data include the calibration observations of payload checkout (PC) 4, observations of Mars, and observations of Jupiter and the Io plasma torus.",
-            "title": "ROSETTA-ORBITER CAL/JUPITER/MARS ALICE 2 MARS V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "ROSETTA-ORBITER CAL/JUPITER/MARS ALICE 2 MARS V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.nasa.gov/d/bfsh-zase",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "GeneLab Outreach",
+                "hasEmail": "mailto:genelab-outreach@lists.nasa.gov"
+            },
+            "description": "The general objective of the study was to determine modulation of gene expression by environmental factors with a special emphasis on bone formation. For this reason the specific period of treatment was chosen between 5-6 days post-fertilization (dpf) when bone formation and calcification are taking place. Zebrafish larvae were placed at 5 dpf into a Large Diameter Centrifuge and brought to a gravitational force of 3g or 5g for 24 hours. We show that this treatment causes a clear increase of bone formation as illustrated by cranial skeleton staining of the bone matrix by Alizarin Red by morphometric analysis of the resulting images and by gene expression studies of selected genes. Thus a whole genome micro-array experiment was conducted to identify genes that may be involved in the observed effect on bone formation.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "GeneLab Study Page",
+                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-123",
+                    "mediaType": "text/html",
+                    "title": "Exposure of zebrafish larvae to 3g and 5g hyper gravity between 5-6 days post-fertilization."
+                }
+            ],
+            "identifier": "nasa_genelab_GLDS-123_bfsh-zase",
             "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
             "keyword": [
                 "p-mtab-43162",
                 "p-mtab-43161",
@@ -531032,146 +531046,104 @@
                 "nucleic acid extraction protocol",
                 "normalization data transformation protocol"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "GeneLab Outreach",
-                "hasEmail": "mailto:genelab-outreach@lists.nasa.gov"
-            },
+            "landingPage": "https://data.nasa.gov/d/bfsh-zase",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "nasa_genelab_GLDS-123_bfsh-zase",
-            "description": "The general objective of the study was to determine modulation of gene expression by environmental factors with a special emphasis on bone formation. For this reason the specific period of treatment was chosen between 5-6 days post-fertilization (dpf) when bone formation and calcification are taking place. Zebrafish larvae were placed at 5 dpf into a Large Diameter Centrifuge and brought to a gravitational force of 3g or 5g for 24 hours. We show that this treatment causes a clear increase of bone formation as illustrated by cranial skeleton staining of the bone matrix by Alizarin Red by morphometric analysis of the resulting images and by gene expression studies of selected genes. Thus a whole genome micro-array experiment was conducted to identify genes that may be involved in the observed effect on bone formation.",
-            "title": "Exposure of zebrafish larvae to 3g and 5g hyper gravity between 5-6 days post-fertilization.",
-            "programCode": [
-                "026:005"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-123",
-                    "description": "GeneLab Study Page",
-                    "@type": "dcat:Distribution",
-                    "title": "Exposure of zebrafish larvae to 3g and 5g hyper gravity between 5-6 days post-fertilization."
-                }
-            ],
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "Exposure of zebrafish larvae to 3g and 5g hyper gravity between 5-6 days post-fertilization."
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1278770864-GES_DISC.html",
             "citation": "Joanna Joiner. 2017-01-11. OMMYDAGEO. Version 003. OMI/Aura and MODIS/Aqua Merged Aerosol Geo-colocation Product 1-Orbit L2 Swath 13x24 km V003. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://disc.gsfc.nasa.gov/datacollection/OMMYDAGEO_003.html. Digital Science Data.",
-            "issued": "2017-01-03",
-            "temporal": "2004-10-01T00:00:00Z/2022-01-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2017-01-03",
-            "references": [
-                "https://doi.org/10.1029/2007JD008689"
-            ],
-            "keyword": [
-                "ngda",
-                "aerosols",
-                "atmosphere",
-                "national geospatial data asset",
-                "earth science"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "JOANNA JOINER, PH. D",
                 "hasEmail": "mailto:Joanna.Joiner@nasa.gov"
             },
+            "creator": "Joanna Joiner",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C1278770864-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "The OMI/Aura and MODIS/Aqua Aerosol Geo-colocation Product 1-Orbit L2 Swath 13x24 km (OMMYDAGEO) is a Level-2 orbital data product that links the MODIS/Aqua aerosol geo-coordinates at 3 and 10 km with the OMI indices along the OMI orbital track. This product allows users to match up MODIS granules with the OMI orbit for analysis and validation. It co-locates MODIS and OMI cloud and radiance information onto the OMI pixel.\n\nThe OMMYDAGEO data files are stored in the version 5 EOS Hierarchical Data Format (HDF-EOS5) using the swath model, and follows the same conventions used by the other OMI Level-2 data products. Each file contains data for 5 minutes, corresponding to the MODIS granule from the daylit side of the orbit. There are on the order of about 140 swath files per day. The file size for the OMMYDAGEO data product is about 12 Megabytes.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "OMMYDAGEO",
-            "creator": "Joanna Joiner",
-            "graphic-preview-description": "OMMYDAGEO Sample Image",
-            "title": "OMI/Aura and MODIS/Aqua Aerosol Geo-colocation Product 1-Orbit L2 Swath 13x24 km V003 (OMMYDAGEO) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/OMMYDAGEO_003.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/OMMYDAGEO_003.png",
-                    "description": "OMMYDAGEO Sample Image",
                     "@type": "dcat:Distribution",
+                    "description": "OMMYDAGEO Sample Image",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/OMMYDAGEO_003.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/OMMYDAGEO_003.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/OMMYDAGEO_003.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://aura.gesdisc.eosdis.nasa.gov/data/Aura_OMI_Level2/OMMYDAGEO.003/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://aura.gesdisc.eosdis.nasa.gov/data/Aura_OMI_Level2/OMMYDAGEO.003/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=OMMYDAGEO_003",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=OMMYDAGEO_003",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://aura.gesdisc.eosdis.nasa.gov/opendap/Aura_OMI_Level2/OMMYDAGEO.003/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://aura.gesdisc.eosdis.nasa.gov/opendap/Aura_OMI_Level2/OMMYDAGEO.003/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://aura.gesdisc.eosdis.nasa.gov/data/Aura_OMI_Level2/OMMYDAGEO.003/doc/README.OMMYDAGEO.pdf",
-                    "description": "README Document",
                     "@type": "dcat:Distribution",
+                    "description": "README Document",
+                    "downloadURL": "https://aura.gesdisc.eosdis.nasa.gov/data/Aura_OMI_Level2/OMMYDAGEO.003/doc/README.OMMYDAGEO.pdf",
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
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/repository/Mission/OMI/3.3_ScienceDataProductDocumentation/3.3.2_ProductRequirements_Designs/OMMYDAGEO_v5.fs",
-                    "description": "File Specification Document",
                     "@type": "dcat:Distribution",
+                    "description": "File Specification Document",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/repository/Mission/OMI/3.3_ScienceDataProductDocumentation/3.3.2_ProductRequirements_Designs/OMMYDAGEO_v5.fs",
+                    "mediaType": "text/html",
                     "title": "View the primary investigator's documentation for this dataset"
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
@@ -531181,64 +531153,94 @@
                     "title": "View this dataset's publications"
                 }
             ],
+            "graphic-preview-description": "OMMYDAGEO Sample Image",
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/OMMYDAGEO_003.png",
+            "identifier": "C1278770864-GES_DISC",
+            "issued": "2017-01-03",
+            "keyword": [
+                "ngda",
+                "aerosols",
+                "atmosphere",
+                "national geospatial data asset",
+                "earth science"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1278770864-GES_DISC.html",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2017-01-03",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
+            },
+            "references": [
+                "https://doi.org/10.1029/2007JD008689"
+            ],
+            "release-place": "Greenbelt, MD, USA",
+            "series-name": "OMMYDAGEO",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2004-10-01T00:00:00Z/2022-01-17T00:00:00Z",
             "theme": [
                 "Aura",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "OMI/Aura and MODIS/Aqua Aerosol Geo-colocation Product 1-Orbit L2 Swath 13x24 km V003 (OMMYDAGEO) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-X-SREM-2-CR5-V1.0",
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
+            "description": "This data set contains count rates (1/s) as measured by the Standard Radiation Environment Monitor (SREM) instrument on the Rosetta spacecraft, along with their standard deviations.  These are CODMAC Level 2 Experiment Data Record data, and provide a measure of the radiation in the spacecraft environment during the CRUISE 5 mission phase.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-x-srem-2-cr5-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "calibration",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-X-SREM-2-CR5-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-x-srem-2-cr5-v1.0",
-            "description": "This data set contains count rates (1/s) as measured by the Standard Radiation Environment Monitor (SREM) instrument on the Rosetta spacecraft, along with their standard deviations.  These are CODMAC Level 2 Experiment Data Record data, and provide a measure of the radiation in the spacecraft environment during the CRUISE 5 mission phase.",
-            "title": "ROSETTA-ORBITER X SREM 2 CRUISE 5\n    V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER X SREM 2 CRUISE 5\n    V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-J-LORRI-3-JUPITER-V2.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This data set contains Calibrated data taken by the New Horizons Long Range Reconnaissance Imager instrument during the Jupiter encounter mission phase.  This is VERSION 2.0 of this data set.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-j-lorri-3-jupiter-v2.0_bfv2-nbuz",
             "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "earth",
                 "callisto",
@@ -531252,38 +531254,38 @@
                 "calibration",
                 "ganymede"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-J-LORRI-3-JUPITER-V2.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-j-lorri-3-jupiter-v2.0_bfv2-nbuz",
-            "description": "This data set contains Calibrated data taken by the New Horizons Long Range Reconnaissance Imager instrument during the Jupiter encounter mission phase.  This is VERSION 2.0 of this data set.",
-            "title": "NEW HORIZONS\n      LORRI JUPITER ENCOUNTER\n      CALIBRATED V2.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "NEW HORIZONS\n      LORRI JUPITER ENCOUNTER\n      CALIBRATED V2.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=CFHT-S-QUIRC-1%2F3-RPX-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This data set contains images of the Saturn system from the CANADA-FRANCE-HAWAII telescope with the Quick Infrared Camera in early August 1995.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.cfht-s-quirc-1-3-rpx-v1.0_bfv3-n3bf",
             "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "tethys",
                 "titan",
@@ -531292,583 +531294,583 @@
                 "s rings",
                 "saturn ring plane crossing 1995"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=CFHT-S-QUIRC-1%2F3-RPX-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.cfht-s-quirc-1-3-rpx-v1.0_bfv3-n3bf",
-            "description": "This data set contains images of the Saturn system from the CANADA-FRANCE-HAWAII telescope with the Quick Infrared Camera in early August 1995.",
-            "title": "CFHT SR QUIRC RAW AND CALIBRATED RING PLANE CROSSING 1.O",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "CFHT SR QUIRC RAW AND CALIBRATED RING PLANE CROSSING 1.O"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C2331490179-OB_DAAC.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/GSFC/SED/ESD/GCDC/OB.DAAC.",
-            "issued": "2019-06-23",
-            "temporal": "2000-02-24T00:00:00Z/2023-02-28T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2019-10-01",
-            "keyword": [
-                "ngda",
-                "national geospatial data asset",
-                "ocean optics",
-                "oceans",
-                "earth science",
-                "atmosphere",
-                "aerosols"
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
-            "identifier": "C2331490179-OB_DAAC",
             "description": "The Ocean Biology DAAC produces near real-time (quicklook) products using the best-available combination of ancillary data from meteorological and ozone data. As such, the inputs and the calibration used are less than optimal. Quicklook products provide a snapshot of the data during a short time period within a single orbit.",
-            "title": "Terra MODIS Global Binned Remote-Sensing Reflectance (RRS) - NRT Data, version R2022.0",
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
-                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/data/10.5067/TERRA/MODIS/L3B/RRS/2022",
-                    "description": "MODIS-Terra L3B Remote-Sensing Reflectance (RRS) - NRT Dataset Landing Page",
                     "@type": "dcat:Distribution",
+                    "description": "MODIS-Terra L3B Remote-Sensing Reflectance (RRS) - NRT Dataset Landing Page",
+                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/data/10.5067/TERRA/MODIS/L3B/RRS/2022",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 }
             ],
+            "identifier": "C2331490179-OB_DAAC",
+            "issued": "2019-06-23",
+            "keyword": [
+                "ngda",
+                "national geospatial data asset",
+                "ocean optics",
+                "oceans",
+                "earth science",
+                "atmosphere",
+                "aerosols"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C2331490179-OB_DAAC.html",
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
+            "title": "Terra MODIS Global Binned Remote-Sensing Reflectance (RRS) - NRT Data, version R2022.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/PECEC1AZ5R1J",
             "citation": "Kevin W. Bowman. 2023-02-13. TRPSDL2ALLCRSMGMEX. Version 1. TROPESS CrIS-SNPP L2 for Mexico City Megacity, Standard Product V1. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/PECEC1AZ5R1J. https://disc.gsfc.nasa.gov/datacollection/TRPSDL2ALLCRSMGMEX_1.html. Digital Science Data.",
-            "issued": "2023-01-12",
-            "temporal": "2016-01-02T00:00:00Z/2023-03-06T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-12",
-            "references": [
-                "https://doi.org/10.1126/sciadv.abf7460"
-            ],
-            "keyword": [
-                "earth science",
-                "atmospheric chemistry",
-                "atmosphere",
-                "atmospheric water vapor",
-                "atmospheric temperature"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "KEVIN BOWMAN",
                 "hasEmail": "mailto:kevin.w.bowman@jpl.nasa.gov"
             },
+            "creator": "Kevin W. Bowman",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C2569840361-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "The TROPESS CrIS-SNPP L2 for Mexico City Megacity, Standard Product contains the vertical distribution of seven retrieved atmospheric gases (CH4, CO, H2O, HDO, NH3, O3 and PAN) and temperature, along with formal uncertainties measured by the CrIS instrument on the Suomi-NPP satellite. The forward stream standard product is centered on a 3x3 degree region over Mexico City for the time period from 2016-01-02 to present. The NASA TRopospheric Ozone and Precursors from Earth System Sounding (TROPESS) project, uses an optimal estimation algorithm, known as the MUlti-SpEctra, MUlti-SpEcies, Multi-SEnsors (MUSES).\n\nThe data files are written in the netCDF version 4 file format, and each file contains one day of data. The data have a spatial resolution of 14 km (CrIS nadir FOV), and are reported at 17 vertical levels from the surface to 0.1 hPa. The principal investigator for the TROPESS project is Kevin W. Bowman.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "TRPSDL2ALLCRSMGMEX",
-            "creator": "Kevin W. Bowman",
-            "graphic-preview-description": "TROPESS CrIS-SNPP Mexico City Megacity (Forward Stream, Standard Product) at 681 hPa on 01 April 2021.",
-            "title": "TROPESS CrIS-SNPP L2 for Mexico City Megacity, Standard Product V1 (TRPSDL2ALLCRSMGMEX) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TROPESS/images/TRPSDL2ALLCRSMGMEX_Sample.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FPECEC1AZ5R1J",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FPECEC1AZ5R1J",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TROPESS/images/TRPSDL2ALLCRSMGMEX_Sample.png",
-                    "description": "TROPESS CrIS-SNPP Mexico City Megacity (Forward Stream, Standard Product) at 681 hPa on 01 April 2021.",
                     "@type": "dcat:Distribution",
+                    "description": "TROPESS CrIS-SNPP Mexico City Megacity (Forward Stream, Standard Product) at 681 hPa on 01 April 2021.",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TROPESS/images/TRPSDL2ALLCRSMGMEX_Sample.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/TRPSDL2ALLCRSMGMEX_1.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/TRPSDL2ALLCRSMGMEX_1.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/data/TROPESS_MegaCities_Standard/TRPSDL2ALLCRSMGMEX.1/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/data/TROPESS_MegaCities_Standard/TRPSDL2ALLCRSMGMEX.1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=TRPSDL2ALLCRSMGMEX_1",
-                    "description": "Use the Earthdata Search Client to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search Client to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=TRPSDL2ALLCRSMGMEX_1",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/opendap/TROPESS_MegaCities_Standard/TRPSDL2ALLCRSMGMEX.1/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/opendap/TROPESS_MegaCities_Standard/TRPSDL2ALLCRSMGMEX.1/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/data/TROPESS_MegaCities_Standard/TRPSDL2ALLCRSMGMEX.1/doc/TROPESS_Forward_Stream_README.pdf",
-                    "description": "README Document",
                     "@type": "dcat:Distribution",
+                    "description": "README Document",
+                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/data/TROPESS_MegaCities_Standard/TRPSDL2ALLCRSMGMEX.1/doc/TROPESS_Forward_Stream_README.pdf",
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
+            "graphic-preview-description": "TROPESS CrIS-SNPP Mexico City Megacity (Forward Stream, Standard Product) at 681 hPa on 01 April 2021.",
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TROPESS/images/TRPSDL2ALLCRSMGMEX_Sample.png",
+            "identifier": "C2569840361-GES_DISC",
+            "issued": "2023-01-12",
+            "keyword": [
+                "earth science",
+                "atmospheric chemistry",
+                "atmosphere",
+                "atmospheric water vapor",
+                "atmospheric temperature"
+            ],
+            "landingPage": "https://doi.org/10.5067/PECEC1AZ5R1J",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2023-01-12",
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
+            "series-name": "TRPSDL2ALLCRSMGMEX",
             "spatial": "-101.0 18.0 -98.0 21.0",
+            "temporal": "2016-01-02T00:00:00Z/2023-03-06T00:00:00Z",
             "theme": [
                 "TROPESS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "TROPESS CrIS-SNPP L2 for Mexico City Megacity, Standard Product V1 (TRPSDL2ALLCRSMGMEX) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.7927/H4HQ3WTH",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Yetman, G., S.R. Gaffin, and  X. Xing. 2004-04-30. Global 15 x 15 Minute Grids of the Downscaled Population Based on the SRES B2 Scenario, 1990 and 2025. Version 1.00. Palisades, NY. Archived by National Aeronautics and Space Administration, U.S. Government, NASA Socioeconomic Data and Applications Center (SEDAC). https://doi.org/10.7927/H4HQ3WTH. https://doi.org/10.7927/H4HQ3WTH.",
-            "issued": "2004-04-30",
-            "temporal": "1990-01-01T00:00:00Z/2025-12-31T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2004-04-30",
-            "references": [
-                "https://doi.org/10.7927/H4XW4GQ1",
-                "https://doi.org/10.7927/H4T43R01",
-                "https://doi.org/10.7927/H4PC308P",
-                "https://doi.org/10.7927/H4NC5Z4X"
-            ],
-            "keyword": [
-                "population",
-                "atmosphere",
-                "human dimensions",
-                "earth science",
-                "air quality"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
-                "fn": "undefined",
-                "hasEmail": "mailto:metadata@ciesin.columbia.edu"
-            },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "SEDAC"
+                "fn": "undefined",
+                "hasEmail": "mailto:metadata@ciesin.columbia.edu"
             },
-            "identifier": "C179001925-SEDAC",
-            "description": "The Global 15x15 Minute Grids of the Downscaled Population Based on the Special Report on Emissions Scenarios (SRES) B2 Scenario, 1990 and 2025, are geospatial distributions of the downscaled population per Unit area (population densities). These global grids were generated using the Country-level Population and Downscaled Projections Based on the SRES B2 Scenario, 1990-2100 data set, and CIESIN's Gridded Population of World, Version 2 (GPWv2) data set as the base map. The 1990 GPW was used as the base distribution and the country-level downscaled projections were used to replace population estimates of 1990 in GPW and 2025. The fractional distribution of the population at each grid cell is the same as the 1990 GPW, sub-nationally. This data set is produced  and distributed by the Columbia University Center for International Earth Science Information Network (CIESIN).",
-            "release-place": "Palisades, NY",
-            "graphic-preview-description": "Maps Download Page",
             "creator": "Yetman, G., S.R. Gaffin, and  X. Xing",
-            "title": "Global 15 x 15 Minute Grids of the Downscaled Population Based on the SRES B2 Scenario, 1990 and 2025",
-            "graphic-preview-file": "https://sedac.ciesin.columbia.edu/data/set/sdp-downscaled-population-grid-b2-1990-2025/maps",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The Global 15x15 Minute Grids of the Downscaled Population Based on the Special Report on Emissions Scenarios (SRES) B2 Scenario, 1990 and 2025, are geospatial distributions of the downscaled population per Unit area (population densities). These global grids were generated using the Country-level Population and Downscaled Projections Based on the SRES B2 Scenario, 1990-2100 data set, and CIESIN's Gridded Population of World, Version 2 (GPWv2) data set as the base map. The 1990 GPW was used as the base distribution and the country-level downscaled projections were used to replace population estimates of 1990 in GPW and 2025. The fractional distribution of the population at each grid cell is the same as the 1990 GPW, sub-nationally. This data set is produced  and distributed by the Columbia University Center for International Earth Science Information Network (CIESIN).",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.7927%2FH4HQ3WTH",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.7927%2FH4HQ3WTH",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/downloads/maps/sdp/sdp-downscaled-gdp-grid-b2-1990-2025/gridded-gdp-1990-2025-global-thumbnail.jpg",
-                    "description": "Sample browse graphic of the data set.",
                     "@type": "dcat:Distribution",
+                    "description": "Sample browse graphic of the data set.",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/downloads/maps/sdp/sdp-downscaled-gdp-grid-b2-1990-2025/gridded-gdp-1990-2025-global-thumbnail.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/sdp-downscaled-population-grid-b2-1990-2025/data-download",
-                    "description": "Data Download Page",
                     "@type": "dcat:Distribution",
+                    "description": "Data Download Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/sdp-downscaled-population-grid-b2-1990-2025/data-download",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/sdp-downscaled-population-grid-b2-1990-2025/maps",
-                    "description": "Maps Download Page",
                     "@type": "dcat:Distribution",
+                    "description": "Maps Download Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/sdp-downscaled-population-grid-b2-1990-2025/maps",
+                    "mediaType": "text/html",
                     "title": "Get a related map visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/sdp-downscaled-population-grid-b2-1990-2025",
-                    "description": "Data Set\u00a0Overview Page",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set\u00a0Overview Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/sdp-downscaled-population-grid-b2-1990-2025",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "graphic-preview-description": "Maps Download Page",
+            "graphic-preview-file": "https://sedac.ciesin.columbia.edu/data/set/sdp-downscaled-population-grid-b2-1990-2025/maps",
+            "identifier": "C179001925-SEDAC",
+            "issued": "2004-04-30",
+            "keyword": [
+                "population",
+                "atmosphere",
+                "human dimensions",
+                "earth science",
+                "air quality"
+            ],
+            "landingPage": "https://doi.org/10.7927/H4HQ3WTH",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2004-04-30",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "SEDAC"
+            },
+            "references": [
+                "https://doi.org/10.7927/H4XW4GQ1",
+                "https://doi.org/10.7927/H4T43R01",
+                "https://doi.org/10.7927/H4PC308P",
+                "https://doi.org/10.7927/H4NC5Z4X"
+            ],
+            "release-place": "Palisades, NY",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "1990-01-01T00:00:00Z/2025-12-31T00:00:00Z",
             "theme": [
                 "SDP",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Global 15 x 15 Minute Grids of the Downscaled Population Based on the SRES B2 Scenario, 1990 and 2025"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1800",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Shimada, J.G., Y. Lou, S. Hensley, B.P. Hawkins, L. Harcke, D.M. Lagoy, T.R. Michel, R.J. Muellerschoen, S. Flores, N. Pinto, C. Rains, W.W. Tung, and Y. Zheng. 2021. ABoVE: L1 S-0 Polarimetric Data from UAVSAR P-band SAR, Alaska and Canada, 2017. ORNL DAAC, Oak Ridge, Tennessee, USA. https://doi.org/10.3334/ORNLDAAC/1800",
-            "issued": "2021-04-03",
-            "temporal": "2017-05-22T20:26:00Z/2017-08-18T22:38:48Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-17",
-            "keyword": [
-                "spectral/engineering",
-                "earth science",
-                "radar"
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
-            "identifier": "C2143401773-ORNL_CLOUD",
             "description": "This dataset provides Level 1 (L1) polarimetric radar backscattering coefficient (Sigma-0 or S-0), multi-look complex, polarimetrically calibrated, and georeferenced data products from the UAVSAR P-band SAR radar instrument collected over 74 study sites across Alaska, USA, and western Canada. The radar instrument is a fully polarimetric P-band (ultra-high frequency) SAR operating in the 420-440 MHz band. The flight campaigns took place periodically in May-August 2017 onboard a NASA Gulfstream-III aircraft. Each set of products was produced from a data take (i.e., acquisition) of the UAVSAR P-band SAR radar instrument, where one data take is equivalent to one flight line over a site. Two to four data takes were sought for each site, although for some sites as few as one or as many as six are provided. There were a total of 139 data takes over the 74 sites.",
-            "graphic-preview-description": "UAVSAR P-band SAR radar swaths over study sites across Alaska, USA, and western Canada for the 2017 ABoVE campaign.",
-            "title": "ABoVE: L1 S-0 Polarimetric Data from UAVSAR P-band SAR, Alaska and Canada, 2017",
-            "graphic-preview-file": "https://daac.ornl.gov/ABOVE/guides/ABoVE_L1_P_SAR_Fig1.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1800",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1800",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/above/ABoVE_L1_P_SAR/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/above/ABoVE_L1_P_SAR/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/ABOVE/guides/ABoVE_L1_P_SAR.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/ABOVE/guides/ABoVE_L1_P_SAR.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1800",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1800",
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
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/ABoVE_L1_P_SAR/comp/ABoVE_L1_P_SAR.pdf",
-                    "description": "ABoVE: L1 S-0 Polarimetric Data from UAVSAR P-band SAR, Alaska and Canada, 2017: ABoVE_L1_P_SAR.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "ABoVE: L1 S-0 Polarimetric Data from UAVSAR P-band SAR, Alaska and Canada, 2017: ABoVE_L1_P_SAR.pdf",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/ABoVE_L1_P_SAR/comp/ABoVE_L1_P_SAR.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://daac.ornl.gov/ABOVE/guides/ABoVE_L1_P_SAR_Fig1.png",
-                    "description": "UAVSAR P-band SAR radar swaths over study sites across Alaska, USA, and western Canada for the 2017 ABoVE campaign.",
                     "@type": "dcat:Distribution",
+                    "description": "UAVSAR P-band SAR radar swaths over study sites across Alaska, USA, and western Canada for the 2017 ABoVE campaign.",
+                    "downloadURL": "https://daac.ornl.gov/ABOVE/guides/ABoVE_L1_P_SAR_Fig1.png",
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
+            "graphic-preview-description": "UAVSAR P-band SAR radar swaths over study sites across Alaska, USA, and western Canada for the 2017 ABoVE campaign.",
+            "graphic-preview-file": "https://daac.ornl.gov/ABOVE/guides/ABoVE_L1_P_SAR_Fig1.png",
+            "identifier": "C2143401773-ORNL_CLOUD",
+            "issued": "2021-04-03",
+            "keyword": [
+                "spectral/engineering",
+                "earth science",
+                "radar"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1800",
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
             "spatial": "-166.61 52.08 -104.18 71.46",
+            "temporal": "2017-05-22T20:26:00Z/2017-08-18T22:38:48Z",
             "theme": [
                 "ABoVE",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "ABoVE: L1 S-0 Polarimetric Data from UAVSAR P-band SAR, Alaska and Canada, 2017"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/512",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Black, T.A. 2000. BOREAS TF-01 SSA-OA Tower Flux, Meteorological, and Soil Temperature Data. ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/512",
-            "issued": "2023-11-22",
-            "temporal": "1996-02-02T00:00:00Z/1996-12-31T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-11-28",
-            "keyword": [
-                "atmosphere",
-                "vegetation",
-                "soils",
-                "precipitation",
-                "land surface",
-                "earth science",
-                "biosphere",
-                "atmospheric winds",
-                "atmospheric water vapor",
-                "atmospheric temperature",
-                "atmospheric radiation",
-                "atmospheric chemistry",
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
-            "identifier": "C2808092747-ORNL_CLOUD",
             "description": "Energy, cargon dioxide, and momentum flux data collected above the canopy along with meteorological and soils data at the BOREAS SSA-OA site",
-            "graphic-preview-description": "Browse Image",
-            "title": "BOREAS TF-01 SSA-OA Tower Flux, Meteorological, and Soil Temperature Data",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/boreas_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F512",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F512",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/boreas/TF/tf01tflx/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/boreas/TF/tf01tflx/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/BOREAS/guides/TF01_Tower_Flux.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/BOREAS/guides/TF01_Tower_Flux.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/512",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/512",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TF/tf01tflx/comp/tf01tflx.def",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TF/tf01tflx/comp/tf01tflx.def",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/msword",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TF/tf01tflx/comp/TF01_Tower_Flux.doc",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TF/tf01tflx/comp/TF01_Tower_Flux.doc",
+                    "mediaType": "application/msword",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TF/tf01tflx/comp/TF01_Tower_Flux.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TF/tf01tflx/comp/TF01_Tower_Flux.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TF/tf01tflx/comp/TF01_Tower_Flux.txt",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TF/tf01tflx/comp/TF01_Tower_Flux.txt",
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
+            "identifier": "C2808092747-ORNL_CLOUD",
+            "issued": "2023-11-22",
+            "keyword": [
+                "atmosphere",
+                "vegetation",
+                "soils",
+                "precipitation",
+                "land surface",
+                "earth science",
+                "biosphere",
+                "atmospheric winds",
+                "atmospheric water vapor",
+                "atmospheric temperature",
+                "atmospheric radiation",
+                "atmospheric chemistry",
+                "atmospheric pressure"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/512",
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
             "spatial": "53.63 -106.2",
+            "temporal": "1996-02-02T00:00:00Z/1996-12-31T23:59:59Z",
             "theme": [
                 "BOREAS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "BOREAS TF-01 SSA-OA Tower Flux, Meteorological, and Soil Temperature Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=CO-X-UVIS-2-SPEC-V1.0",
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
+            "description": "Spectroscopy of Jupiter, Saturnian rings, atmospheres and satellites for determining chemical abundance, compositional albedo, aerosol profiling, ring reflected spectra and diffraction patterns.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.co-x-uvis-2-spec-v1.0_bg4y-bdek",
+            "issued": "2021-05-21",
+            "keyword": [
+                "cassini-huygens"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=CO-X-UVIS-2-SPEC-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.co-x-uvis-2-spec-v1.0_bg4y-bdek",
-            "description": "Spectroscopy of Jupiter, Saturnian rings, atmospheres and satellites for determining chemical abundance, compositional albedo, aerosol profiling, ring reflected spectra and diffraction patterns.",
-            "title": "CASSINI ORBITER N/A UVIS EDITED SPECTRA 1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "CASSINI ORBITER N/A UVIS EDITED SPECTRA 1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-J-MVIC-3-JUPITER-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This data set contains Calibrated data taken by the New Horizons Multispectral Visible Imaging Camera instrument during the Jupiter encounter mission phase.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-j-mvic-3-jupiter-v1.0_bg52-xkqy",
             "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "earth",
                 "j1 io",
@@ -531878,76 +531880,85 @@
                 "ganymede",
                 "callisto"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-J-MVIC-3-JUPITER-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-j-mvic-3-jupiter-v1.0_bg52-xkqy",
-            "description": "This data set contains Calibrated data taken by the New Horizons Multispectral Visible Imaging Camera instrument during the Jupiter encounter mission phase.",
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
-            "landingPage": "https://c3.nasa.gov/dashlink/resources/680/",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2013-03-28",
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
-            "identifier": "DASHLINK_680",
             "description": "In this paper we propose an innovative learning algorithm - a variation of One-class \u0017 Support Vector Machines (SVMs) learning algorithm to produce sparser solutions with much reduced computational complexities. The proposed technique returns an approximate solution, nearly as good as the solution set obtained by the classical approach, by minimizing the original risk function along with a regularization term. We introduce a bi-criterion optimization that helps guide the search towards the optimal set in much reduced\r\ntime. The outcome of the proposed learning technique was compared with the benchmark one-class Support Vector machines algorithm which more often leads to solutions with\r\nredundant support vectors. Through out the analysis, the problem size for both optimization routines was kept consistent.\r\nWe have tested the proposed algorithm on a variety of data sources under different conditions to demonstrate the effectiveness. In all cases the proposed algorithm closely preserves the accuracy of standard one-class \u0017 SVMs while reducing both training time and test time by several factors.",
-            "title": "Sparse Solutions for Single Class SVMs: A Bi-Criterion Approach",
-            "programCode": [
-                "026:029"
-            ],
             "distribution": [
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/publication/daoz11.pdf",
-                    "description": "daoz11.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "daoz11.pdf",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/publication/daoz11.pdf",
+                    "mediaType": "application/pdf",
                     "title": "daoz11.pdf"
                 }
             ],
-            "accrualPeriodicity": "irregular"
+            "identifier": "DASHLINK_680",
+            "issued": "2013-03-28",
+            "keyword": [
+                "dashlink",
+                "nasa",
+                "ames"
+            ],
+            "landingPage": "https://c3.nasa.gov/dashlink/resources/680/",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:029"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Dashlink"
+            },
+            "title": "Sparse Solutions for Single Class SVMs: A Bi-Criterion Approach"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.nasa.gov/d/bg6s-kh9m",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Randal Jackson",
+                "hasEmail": "mailto:randal.k.jackson@jpl.nasa.gov"
+            },
+            "description": "Carbon dioxide (CO2) is an important greenhouse gas released through natural processes such as respiration and volcano eruptions and through huma activities such as deforestation and burning fossil fuels. AIRS is the Atmospheric InfraRed Sounder, AIRS, was launched aboard the Aqua Spacecraft in 2002 as part of NASA\u2019s Earth Observing System Afternoon Constellation of satellites known as the \u2018A-Train\u2019.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://climate.nasa.gov/key_indicators",
+                    "mediaType": "text/html"
+                }
+            ],
+            "identifier": "NASA-0000044",
             "issued": "2018-06-25",
-            "temporal": "2002-01-01/2012-01-01",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
             "keyword": [
                 "carbon dioxide",
                 "waves",
@@ -531961,698 +531972,696 @@
                 "climate",
                 "arctic sea ice"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Randal Jackson",
-                "hasEmail": "mailto:randal.k.jackson@jpl.nasa.gov"
-            },
+            "landingPage": "https://data.nasa.gov/d/bg6s-kh9m",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:001"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "NASA-0000044",
-            "description": "Carbon dioxide (CO2) is an important greenhouse gas released through natural processes such as respiration and volcano eruptions and through huma activities such as deforestation and burning fossil fuels. AIRS is the Atmospheric InfraRed Sounder, AIRS, was launched aboard the Aqua Spacecraft in 2002 as part of NASA\u2019s Earth Observing System Afternoon Constellation of satellites known as the \u2018A-Train\u2019.",
-            "title": "Monthly Carbon Dioxide in Troposphere (AIRS on AQUA)",
-            "programCode": [
-                "026:001"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://climate.nasa.gov/key_indicators",
-                    "mediaType": "text/html"
-                }
-            ],
             "spatial": "global",
-            "accrualPeriodicity": "irregular",
+            "temporal": "2002-01-01/2012-01-01",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "Monthly Carbon Dioxide in Troposphere (AIRS on AQUA)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MGS-M-RSS-5-SDP-V1.0",
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
+            "description": "This data set contains archival results from radio science investigations conducted during the Mars Global Surveyor (MGS) mission. Radio measurements were made using the MGS spacecraft and Earth-based stations of the NASA Deep Space Network (DSN). The data set includes high-resolution spherical harmonic models of Mars' gravity field generated by groups at the Jet Propulsion Laboratory and Goddard Space Flight Center, covariance matrices for some models, and maps for some models; these results were derived from raw radio tracking data. Also included are profiles of atmospheric temperature and pressure and ionospheric electron density, derived from phase measurements collected during radio occultations. The data set also includes analyses of transient surface echoes observed close to occultations during the first few years of MGS operations. The atmospheric and surface investigations were conducted by Radio Science Team members at Stanford University. The data set also includes 93 line-of-sight acceleration profiles derived at JPL from radio tracking data collected near periapsis while Mars Global Surveyor was in its Science Phasing Orbit and below its nominal Mapping altitude of 400 km. The data were delivered to PDS in approximately chronological order at the rate of one CD-WO volume (typically 100 MB) every three months.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mgs-m-rss-5-sdp-v1.0_bga6-qwbr",
+            "issued": "2018-06-26",
+            "keyword": [
+                "mars global surveyor",
+                "mars"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MGS-M-RSS-5-SDP-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mgs-m-rss-5-sdp-v1.0_bga6-qwbr",
-            "description": "This data set contains archival results from radio science investigations conducted during the Mars Global Surveyor (MGS) mission. Radio measurements were made using the MGS spacecraft and Earth-based stations of the NASA Deep Space Network (DSN). The data set includes high-resolution spherical harmonic models of Mars' gravity field generated by groups at the Jet Propulsion Laboratory and Goddard Space Flight Center, covariance matrices for some models, and maps for some models; these results were derived from raw radio tracking data. Also included are profiles of atmospheric temperature and pressure and ionospheric electron density, derived from phase measurements collected during radio occultations. The data set also includes analyses of transient surface echoes observed close to occultations during the first few years of MGS operations. The atmospheric and surface investigations were conducted by Radio Science Team members at Stanford University. The data set also includes 93 line-of-sight acceleration profiles derived at JPL from radio tracking data collected near periapsis while Mars Global Surveyor was in its Science Phasing Orbit and below its nominal Mapping altitude of 400 km. The data were delivered to PDS in approximately chronological order at the rate of one CD-WO volume (typically 100 MB) every three months.",
-            "title": "MGS RADIO SCIENCE -- SCIENCE DATA PRODUCTS V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "MGS RADIO SCIENCE -- SCIENCE DATA PRODUCTS V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/HO9OVZWF3KW2",
             "citation": "Global Modeling and Assimilation Office (GMAO). 2015-06-30. M2I3NVCHM. Version 5.12.4. MERRA-2 inst3_3d_chm_Nv: 3d,3-Hourly,Instantaneous,Model-Level,Assimilation,Carbon Monoxide and Ozone Mixing Ratio V5.12.4. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/HO9OVZWF3KW2. https://disc.gsfc.nasa.gov/datacollection/M2I3NVCHM_5.12.4.html. Digital Science Data.",
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
-                "atmospheric pressure",
-                "air quality",
-                "earth science",
-                "atmospheric chemistry",
-                "atmosphere"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "DANA OSTRENGA",
                 "hasEmail": "mailto:dana.ostrenga@nasa.gov"
             },
+            "creator": "Global Modeling and Assimilation Office (GMAO)",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C1276812901-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "M2I3NVCHM (or  inst3_3d_chm_Nv) is an instantaneous 3-dimensional 3-hourly data collection in Modern-Era Retrospective analysis for Research and Applications version 2 (MERRA-2).  This collection consists of assimilations of carbon monoxide and ozone mixing ratio at 72 model layers.  The data is available every three hour starting from 00:00 UTC, e.g.:  00:00, 03:00, \u2026 , 21:00 UTC. Section 4.2 of the MERRA-2 File Specification document provides pressure values nominal for a 1000 hPa surface pressure and refers to the top edge of the layer. The lev=1 is for the top layer, and lev=72 is for the bottom (or surface) model layer. \n\nMERRA-2 is the latest version of global atmospheric reanalysis for the satellite era produced by NASA Global Modeling and Assimilation Office (GMAO) using the Goddard Earth Observing System Model (GEOS) version 5.12.4.  The dataset covers the period of 1980-present with the latency of ~3 weeks after the end of a month. \n\nData Reprocessing:  Please check \u201cRecords of MERRA-2 Data Reprocessing and Service Changes\u201d linked from the \u201cDocumentation\u201d tab on this page.  Note that a reprocessed data filename is different from the original file.\n\nMERRA-2 Mailing List: Sign up to receive information on reprocessing of data, changing of tools and services, as well as data announcements from GMAO. Contact the GES DISC Help Desk (gsfc-dl-help-disc@mail.nasa.gov) to be added to the list.\n\nQuestions: If you have a question, please read \"MERRA-2 File Specification Document\",  \u201cMERRA-2 Data Access \u2013 Quick Start Guide\u201d, and FAQs linked from the \u201dDocumentation\u201d tab on this page.  If that does not answer your question, you may email the question on data access to the GES DISC Help Desk (gsfc-dl-help-disc@mail.nasa.gov), or the question on science to the MERRA-2 science team (merra-questions@lists.nasa.gov).",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "M2I3NVCHM",
-            "creator": "Global Modeling and Assimilation Office (GMAO)",
-            "graphic-preview-description": "M2I3NVCHM variable",
-            "title": "MERRA-2 inst3_3d_chm_Nv: 3d,3-Hourly,Instantaneous,Model-Level,Assimilation,Carbon Monoxide and Ozone Mixing Ratio 0.625 x 0.5 degree V5.12.4 (M2I3NVCHM) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/M2I3NVCHM_5.12.4.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FHO9OVZWF3KW2",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FHO9OVZWF3KW2",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/M2I3NVCHM_5.12.4.png",
-                    "description": "M2I3NVCHM variable",
                     "@type": "dcat:Distribution",
+                    "description": "M2I3NVCHM variable",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/M2I3NVCHM_5.12.4.png",
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
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/M2I3NVCHM_5.12.4.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/M2I3NVCHM_5.12.4.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://goldsmr5.gesdisc.eosdis.nasa.gov/data/MERRA2/M2I3NVCHM.5.12.4/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://goldsmr5.gesdisc.eosdis.nasa.gov/data/MERRA2/M2I3NVCHM.5.12.4/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=M2I3NVCHM",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=M2I3NVCHM",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://goldsmr5.gesdisc.eosdis.nasa.gov/dods/M2I3NVCHM.info",
-                    "description": "The GrADS Data Server (GDS) is another form of OPeNDAP that provides subsetting and some analysis services across the Internet.",
                     "@type": "dcat:Distribution",
+                    "description": "The GrADS Data Server (GDS) is another form of OPeNDAP that provides subsetting and some analysis services across the Internet.",
+                    "downloadURL": "https://goldsmr5.gesdisc.eosdis.nasa.gov/dods/M2I3NVCHM.info",
+                    "mediaType": "text/html",
                     "title": "Use GRADS DATA SERVER (GDS) to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://goldsmr5.gesdisc.eosdis.nasa.gov/opendap/MERRA2/M2I3NVCHM.5.12.4/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://goldsmr5.gesdisc.eosdis.nasa.gov/opendap/MERRA2/M2I3NVCHM.5.12.4/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://goldsmr5.gesdisc.eosdis.nasa.gov/thredds/catalog/MERRA2_aggregation/M2I3NVCHM.5.12.4/catalog.html",
-                    "description": "Time aggregated THREDDS Data Server (TDS) ",
                     "@type": "dcat:Distribution",
+                    "description": "Time aggregated THREDDS Data Server (TDS) ",
+                    "downloadURL": "https://goldsmr5.gesdisc.eosdis.nasa.gov/thredds/catalog/MERRA2_aggregation/M2I3NVCHM.5.12.4/catalog.html",
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
-                    "downloadURL": "https://goldsmr5.gesdisc.eosdis.nasa.gov/data/MERRA2/M2I3NVCHM.5.12.4/doc/MERRA2.README.pdf",
-                    "description": "README Document",
                     "@type": "dcat:Distribution",
+                    "description": "README Document",
+                    "downloadURL": "https://goldsmr5.gesdisc.eosdis.nasa.gov/data/MERRA2/M2I3NVCHM.5.12.4/doc/MERRA2.README.pdf",
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
+            "graphic-preview-description": "M2I3NVCHM variable",
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/M2I3NVCHM_5.12.4.png",
+            "identifier": "C1276812901-GES_DISC",
+            "issued": "2007-06-14",
+            "keyword": [
+                "atmospheric pressure",
+                "air quality",
+                "earth science",
+                "atmospheric chemistry",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.5067/HO9OVZWF3KW2",
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
+            "series-name": "M2I3NVCHM",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "1980-01-01T00:00:00Z/2022-01-17T00:00:00Z",
             "theme": [
                 "MERRA-2",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "MERRA-2 inst3_3d_chm_Nv: 3d,3-Hourly,Instantaneous,Model-Level,Assimilation,Carbon Monoxide and Ozone Mixing Ratio 0.625 x 0.5 degree V5.12.4 (M2I3NVCHM) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=DIF-C-MRI-3%2F4-EPOXI-HARTLEY2-V1.0",
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
-                "epoxi",
-                "103p/hartley 2 (1986 e2)"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This dataset contains calibrated images of comet 103/P Hartley 2 acquired by the Medium Resolution Visible CCD (MRI) from 05 September through 26 November 2010 during the Hartley 2 encounter phase of the EPOXI mission. Clear-filter and CN images of the comet were acquired throughout this phase; OH, C2, and dust continuum images were only acquired for several days spanning closest approach.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.dif-c-mri-3-4-epoxi-hartley2-v1.0_bgan-w9bf",
+            "issued": "2021-05-21",
+            "keyword": [
+                "epoxi",
+                "103p/hartley 2 (1986 e2)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=DIF-C-MRI-3%2F4-EPOXI-HARTLEY2-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.dif-c-mri-3-4-epoxi-hartley2-v1.0_bgan-w9bf",
-            "description": "This dataset contains calibrated images of comet 103/P Hartley 2 acquired by the Medium Resolution Visible CCD (MRI) from 05 September through 26 November 2010 during the Hartley 2 encounter phase of the EPOXI mission. Clear-filter and CN images of the comet were acquired throughout this phase; OH, C2, and dust continuum images were only acquired for several days spanning closest approach.",
-            "title": "EPOXI 103P/HARTLEY2 ENCOUNTER - MRI CALIBRATED IMAGES V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "EPOXI 103P/HARTLEY2 ENCOUNTER - MRI CALIBRATED IMAGES V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=ULY-J-HISCALE-4-SUMM-LEMS30-V1.0",
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
+            "description": "This data set consists of HISCALE Low-Energy Magnetic Spectrometer (LEFS) ion counts at 30 degrees from the spacecraft spin axis. These measurements were taken during the Ulysses Jupiter encounter 1991-12-31 to 1992-02-16, and include 1 hour averaged inbound cruise data (1991-12-31 to 1992-02-01), and 15 minute averaged encounter data (1992-02-02 to 1992-02-16).",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.uly-j-hiscale-4-summ-lems30-v1.0_bgb6-sxgw",
+            "issued": "2018-06-26",
+            "keyword": [
+                "jupiter",
+                "ulysses"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=ULY-J-HISCALE-4-SUMM-LEMS30-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.uly-j-hiscale-4-summ-lems30-v1.0_bgb6-sxgw",
-            "description": "This data set consists of HISCALE Low-Energy Magnetic Spectrometer (LEFS) ion counts at 30 degrees from the spacecraft spin axis. These measurements were taken during the Ulysses Jupiter encounter 1991-12-31 to 1992-02-16, and include 1 hour averaged inbound cruise data (1991-12-31 to 1992-02-01), and 15 minute averaged encounter data (1992-02-02 to 1992-02-16).",
-            "title": "ULYSSES JUPITER HISCALE LEMS 30 ION COUNTS",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "ULYSSES JUPITER HISCALE LEMS 30 ION COUNTS"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-EXT1-1367-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the ROSETTA EXTENSION 1 phase 2016-01-01 to 2016-04-05. It is a Global Gravity measurement at the comet 67P and covers the time 2016-01-24T19:24:45.000 to 2016-01-24T21:42:51.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-ext1-1367-v1.0_bgbe-uzwv",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-EXT1-1367-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-ext1-1367-v1.0_bgbe-uzwv",
-            "description": "This is a Rosetta Radio Science data set, collected during the ROSETTA EXTENSION 1 phase 2016-01-01 to 2016-04-05. It is a Global Gravity measurement at the comet 67P and covers the time 2016-01-24T19:24:45.000 to 2016-01-24T21:42:51.000.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     ROSETTA EXTENSION 1 1367 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     ROSETTA EXTENSION 1 1367 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ESASB-L2W11",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "MEaSUREs/OSWV. 2022-09-27. MetOp-B ASCAT Scatterometer Inter-Calibrated ESDR Level 2 Ocean Surface Equivalent Neutral Wind Vectors and Wind Stress Vectors. Version 1.1. MetOp-B ASCAT Scatterometer Inter-Calibrated ESDR Level 2 Ocean Surface Equivalent Neutral Wind Vectors and Wind Stress Vectors Version 1.1. PO.DAAC. Archived by National Aeronautics and Space Administration, U.S. Government, PO.DAAC. https://doi.org/10.5067/ESASB-L2W11.",
-            "issued": "2022-04-27",
-            "temporal": "2013-08-01T00:00:00Z/2022-05-31T01:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-10-08",
-            "keyword": [
-                "earth science",
-                "oceans",
-                "ocean winds"
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
-            "identifier": "C2706513160-POCLOUD",
-            "description": "This dataset contains ocean surface wind vectors (equivalent neutral and true 10m) and wind stress vectors derived from satellite-based scatterometer observations (the MetOp-B ASCAT scatterometer), representing the first science quality release of these data (post-provisional after v1.0) funded under the MEaAUREs program. This product from MetOp-B ASCAT has been intercalibrated with similar scatterometer measurements from instruments on the MetOp-A, ScatSat-1, and QuikScat satellites. The wind vector and stress retrievals are provided on a non-uniform grid within the swath (Level 2 (L2) products) at 12.5 km pixel resolution. Each L2 file corresponds to a specific orbital revolution number, which begins at the southernmost point of the ascending orbit.\r\n<br><br>\r\nThe dataset represents the first science quality release funded under the MEaSUREs (Making Earth System Data Records for Use in Research Environments) program. Version 1.1 provides a set of updates and improvements from version 1.0, including: 1) increased data coverage, 2) improved quality control, and 3) new global metadata attributes featuring revolution number, equator crossing longitude, and equator crossing time (UTC). The primary purpose of this release is for science evaluation by the NASA International Ocean Vector Winds Science Team (IOVWST).",
-            "release-place": "PO.DAAC",
-            "series-name": "MetOp-B ASCAT Scatterometer Inter-Calibrated ESDR Level 2 Ocean Surface Equivalent Neutral Wind Vectors and Wind Stress Vectors",
-            "graphic-preview-description": "Thumbnail",
             "creator": "MEaSUREs/OSWV",
-            "title": "MetOp-B ASCAT Scatterometer Inter-Calibrated ESDR Level 2 Ocean Surface Equivalent Neutral Wind Vectors and Wind Stress Vectors Version 1.1",
-            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/ASCATB_ESDR_L2_WIND_STRESS_V1.1.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "This dataset contains ocean surface wind vectors (equivalent neutral and true 10m) and wind stress vectors derived from satellite-based scatterometer observations (the MetOp-B ASCAT scatterometer), representing the first science quality release of these data (post-provisional after v1.0) funded under the MEaAUREs program. This product from MetOp-B ASCAT has been intercalibrated with similar scatterometer measurements from instruments on the MetOp-A, ScatSat-1, and QuikScat satellites. The wind vector and stress retrievals are provided on a non-uniform grid within the swath (Level 2 (L2) products) at 12.5 km pixel resolution. Each L2 file corresponds to a specific orbital revolution number, which begins at the southernmost point of the ascending orbit.\r\n<br><br>\r\nThe dataset represents the first science quality release funded under the MEaSUREs (Making Earth System Data Records for Use in Research Environments) program. Version 1.1 provides a set of updates and improvements from version 1.0, including: 1) increased data coverage, 2) improved quality control, and 3) new global metadata attributes featuring revolution number, equator crossing longitude, and equator crossing time (UTC). The primary purpose of this release is for science evaluation by the NASA International Ocean Vector Winds Science Team (IOVWST).",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FESASB-L2W11",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FESASB-L2W11",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/ASCATB_ESDR_L2_WIND_STRESS_V1.1.jpg",
-                    "description": "Thumbnail",
                     "@type": "dcat:Distribution",
+                    "description": "Thumbnail",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/ASCATB_ESDR_L2_WIND_STRESS_V1.1.jpg",
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
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2706513160-POCLOUD",
-                    "description": "HTTPS endpoint for data browse and download",
                     "@type": "dcat:Distribution",
+                    "description": "HTTPS endpoint for data browse and download",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2706513160-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2706513160-POCLOUD",
-                    "description": "Browse granule search results in Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse granule search results in Earthdata Search",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2706513160-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 }
             ],
+            "graphic-preview-description": "Thumbnail",
+            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/ASCATB_ESDR_L2_WIND_STRESS_V1.1.jpg",
+            "identifier": "C2706513160-POCLOUD",
+            "issued": "2022-04-27",
+            "keyword": [
+                "earth science",
+                "oceans",
+                "ocean winds"
+            ],
+            "landingPage": "https://doi.org/10.5067/ESASB-L2W11",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2022-10-08",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/JPL/PODAAC"
+            },
+            "release-place": "PO.DAAC",
+            "series-name": "MetOp-B ASCAT Scatterometer Inter-Calibrated ESDR Level 2 Ocean Surface Equivalent Neutral Wind Vectors and Wind Stress Vectors",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2013-08-01T00:00:00Z/2022-05-31T01:00:00Z",
             "theme": [
                 "MEaSUREs/OSWV",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "MetOp-B ASCAT Scatterometer Inter-Calibrated ESDR Level 2 Ocean Surface Equivalent Neutral Wind Vectors and Wind Stress Vectors Version 1.1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MER1-M-NAVCAM-2-EDR-OPS-V1.0",
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
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mer1-m-navcam-2-edr-ops-v1.0_bgce-3m8c",
+            "issued": "2018-06-26",
+            "keyword": [
+                "mars",
+                "mars exploration rover"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MER1-M-NAVCAM-2-EDR-OPS-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mer1-m-navcam-2-edr-ops-v1.0_bgce-3m8c",
-            "description": "not applicable",
-            "title": "MER 1 MARS NAVIGATION CAMERA EDR OPS VERSION 1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "MER 1 MARS NAVIGATION CAMERA EDR OPS VERSION 1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=CO-D-HRD-3-COHRD-V5.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "The High Rate Detector (HRD) from the University of Chicago is an independent part of the CDA instrument on the Cassini Orbiter that measures the dust flux and particle mass distribution of dust particles hitting the HRD detectors. This data set includes all data from the HRD through the end of 2008. Please refer to Srama et al. (2004) for a detailed HRD description.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.co-d-hrd-3-cohrd-v5.0_bgdd-qmac",
             "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "cassini-huygens",
                 "dust",
                 "calibration"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=CO-D-HRD-3-COHRD-V5.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.co-d-hrd-3-cohrd-v5.0_bgdd-qmac",
-            "description": "The High Rate Detector (HRD) from the University of Chicago is an independent part of the CDA instrument on the Cassini Orbiter that measures the dust flux and particle mass distribution of dust particles hitting the HRD detectors. This data set includes all data from the HRD through the end of 2008. Please refer to Srama et al. (2004) for a detailed HRD description.",
-            "title": "CASSINI HIGH RATE DETECTOR V5.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "CASSINI HIGH RATE DETECTOR V5.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C2652675358-OB_DAAC.html",
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
-            "identifier": "C2652675358-OB_DAAC",
             "description": "The Ocean Biology DAAC produces near real-time (quicklook) products using the best-available combination of ancillary data from meteorological and ozone data. As such, the inputs and the calibration used are less than optimal. Quicklook products provide a snapshot of the data during a short time period within a single orbit.",
-            "title": "NOAA-21 VIIRS Global Mapped Photosynthetically Available Radiation (PAR) - Near Real Time (NRT) Data, version R2022.0",
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
-                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/data/10.5067/NOAA21/VIIRS/L3M/PAR/2022",
-                    "description": "VIIRS-NOAA-21 L3M Photosynthetically Available Radiation (PAR) - Near Real Time (NRT) Dataset Landing Page",
                     "@type": "dcat:Distribution",
+                    "description": "VIIRS-NOAA-21 L3M Photosynthetically Available Radiation (PAR) - Near Real Time (NRT) Dataset Landing Page",
+                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/data/10.5067/NOAA21/VIIRS/L3M/PAR/2022",
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
+            "identifier": "C2652675358-OB_DAAC",
+            "issued": "2023-04-04",
+            "keyword": [
+                "earth science",
+                "ocean optics",
+                "oceans"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C2652675358-OB_DAAC.html",
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
+            "title": "NOAA-21 VIIRS Global Mapped Photosynthetically Available Radiation (PAR) - Near Real Time (NRT) Data, version R2022.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/301",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Way, J., K. McDonald, and R. Zimmermann. 1998. BOREAS RSS-17 Dielectric Constant Profile Measurements. ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/301",
-            "issued": "2023-11-22",
-            "temporal": "1994-04-19T00:00:00Z/1994-04-28T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-11-27",
-            "keyword": [
-                "spectral/engineering",
-                "ecosystems",
-                "biosphere",
-                "vegetation",
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
-            "identifier": "C2807645232-ORNL_CLOUD",
             "description": "Contains dielectric profile  measurements taken by RSS-17 at NSA and SSA treed tower sites.",
-            "graphic-preview-description": "Browse Image",
-            "title": "BOREAS RSS-17 Dielectric Constant Profile Measurements",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/boreas_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F301",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F301",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/boreas/RSS/rs17diel/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/boreas/RSS/rs17diel/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/BOREAS/guides/RSS17_Dielectric_Prof.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/BOREAS/guides/RSS17_Dielectric_Prof.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/301",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/301",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/RSS/rs17diel/comp/rs17diel.def",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/RSS/rs17diel/comp/rs17diel.def",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/msword",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/RSS/rs17diel/comp/RSS17_Dielectric_Prof.doc",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/RSS/rs17diel/comp/RSS17_Dielectric_Prof.doc",
+                    "mediaType": "application/msword",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/RSS/rs17diel/comp/RSS17_Dielectric_Prof.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/RSS/rs17diel/comp/RSS17_Dielectric_Prof.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/RSS/rs17diel/comp/RSS17_Dielectric_Prof.txt",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/RSS/rs17diel/comp/RSS17_Dielectric_Prof.txt",
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
+            "identifier": "C2807645232-ORNL_CLOUD",
+            "issued": "2023-11-22",
+            "keyword": [
+                "spectral/engineering",
+                "ecosystems",
+                "biosphere",
+                "vegetation",
+                "radar",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/301",
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
             "spatial": "-106.2 53.63 -98.29 55.93",
+            "temporal": "1994-04-19T00:00:00Z/1994-04-28T23:59:59Z",
             "theme": [
                 "BOREAS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "BOREAS RSS-17 Dielectric Constant Profile Measurements"
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
+            "description": "CFD Validation of Synthetic Jets and Turbulent Separation Control. This web page provides data from experiments that may be useful for the validation of turbulence models. This resource is expected to grow gradually over time. All data herein arepublicly available.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://cfdval2004.larc.nasa.gov/FinalReports/nasacp-2007-214874cfdval.pdf",
+                    "mediaType": "application/pdf"
+                }
             ],
+            "identifier": "NASA-848",
+            "issued": "2018-06-25",
             "keyword": [
                 "models",
                 "separation",
@@ -532663,1106 +532672,1109 @@
                 "validation",
                 "synthetic"
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
-            "identifier": "NASA-848",
-            "description": "CFD Validation of Synthetic Jets and Turbulent Separation Control. This web page provides data from experiments that may be useful for the validation of turbulence models. This resource is expected to grow gradually over time. All data herein arepublicly available.",
-            "title": "Turbulence Models: Data from Other Experiments: CFD Validation of Synthetic Jets and Turbulent Separation Control",
-            "programCode": [
-                "026:023"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://cfdval2004.larc.nasa.gov/FinalReports/nasacp-2007-214874cfdval.pdf",
-                    "mediaType": "application/pdf"
-                }
+            "references": [
+                "http://turbmodels.larc.nasa.gov/index.html"
             ],
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Aerospace"
-            ]
+            ],
+            "title": "Turbulence Models: Data from Other Experiments: CFD Validation of Synthetic Jets and Turbulent Separation Control"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-VARGBDET-5-MOTHEFAM-V1.1",
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
+            "description": "This dataset contains an updated compilation of asteroid families and clusters, resulting from the application of the Hierarchical Clustering Method (HCM) on a set of around 120,000 asteroids with available proper elements. Whenever available, the classification in the Bus taxonomy is provided for family members, based on spectra from the SMASS, SMASS2 and S3OS2 spectroscopic surveys.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-vargbdet-5-mothefam-v1.1_bgg5-yf2u",
+            "issued": "2021-05-21",
+            "keyword": [
+                "support archives",
+                "asteroid"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-VARGBDET-5-MOTHEFAM-V1.1",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-vargbdet-5-mothefam-v1.1_bgg5-yf2u",
-            "description": "This dataset contains an updated compilation of asteroid families and clusters, resulting from the application of the Hierarchical Clustering Method (HCM) on a set of around 120,000 asteroids with available proper elements. Whenever available, the classification in the Bus taxonomy is provided for family members, based on spectra from the SMASS, SMASS2 and S3OS2 spectroscopic surveys.",
-            "title": "MOTHE-DINIZ ASTEROID DYNAMICAL FAMILIES V1.1",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "MOTHE-DINIZ ASTEROID DYNAMICAL FAMILIES V1.1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1157",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Wei, Y., W.M. Post, R.B. Cook, D.N. Huntzinger, P.E. Thornton, A.R. Jacobson, I.T. Baker, J.M. Chen, F. Chevallier, F.M. Hoffman, A.K. Jain, Shuguang Liu, R. Lokupitiya, D.A. McGuire, A.M. Michalak, G.G. Moisen, R.P. Neilson, P. Peylin, C.S. Potter, B. Poulter, D. Price, J.T. Randerson, C. Rodenbeck, H. Tian, E. Tomelleri, G.R. van der Werf, N. Viovy, T.O. West, J. Xiao, N. Zeng, and M. Zhao. 2013. NACP Regional: Gridded 1-deg Observation Data and Biosphere and Inverse Model Outputs. ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/1157",
-            "issued": "2022-11-28",
-            "temporal": "1990-01-01T00:00:00Z/2007-12-31T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-06-12",
-            "keyword": [
-                "atmospheric water vapor",
-                "ngda",
-                "atmosphere",
-                "biosphere",
-                "natural hazards",
-                "earth science",
-                "ecological dynamics",
-                "ecosystems",
-                "vegetation",
-                "human dimensions",
-                "land surface",
-                "national geospatial data asset",
-                "soils",
-                "agriculture"
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
-            "identifier": "C2555119330-ORNL_CLOUD",
             "description": "This data set contains standardized gridded observation data, terrestrial biosphere model output data, and inverse model simulations of carbon flux parameters that were used in the North American Carbon Program (NACP) Regional Synthesis activities. The data set provides five observation data files (MODIS GPP, MODIS NPP, FIA forest biomass/forest area, NASS crop NPP, and NASS agricultural land fraction) and simulation results from 18 terrestrial biosphere models (TBM) (28 variables; 114 files) and seven inverse models (IM) (two variables; 8 files). To produce this data set, the NACP Modeling and Synthesis Thematic Data Center (MAST-DC) resampled original model simulation results and observation measurement data to 1-degree spatial resolution for North American region, interpolated into monthly or yearly temporal resolution, and reformatted into Climate and Forecast (CF) convention compatible netCDF format.",
-            "graphic-preview-description": "Browse Image",
-            "title": "NACP Regional: Gridded 1-deg Observation Data and Biosphere and Inverse Model Outputs",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/nacp_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1157",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1157",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/nacp/NACP_Regional_Obs_Model_Grid/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/nacp/NACP_Regional_Obs_Model_Grid/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/NACP/guides/NACP_Regional_Obs_Model_Grid.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/NACP/guides/NACP_Regional_Obs_Model_Grid.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1157",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1157",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/nacp/NACP_Regional_Obs_Model_Grid/comp/NACP_Model_Characteristics.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/nacp/NACP_Regional_Obs_Model_Grid/comp/NACP_Model_Characteristics.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/nacp/NACP_Regional_Obs_Model_Grid/comp/NACP_Model_Metadata_Survey_Results.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/nacp/NACP_Regional_Obs_Model_Grid/comp/NACP_Model_Metadata_Survey_Results.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/nacp/NACP_Regional_Obs_Model_Grid/comp/NACP_Regional_Obs_Model_Grid.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/nacp/NACP_Regional_Obs_Model_Grid/comp/NACP_Regional_Obs_Model_Grid.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/nacp/NACP_Regional_Obs_Model_Grid/comp/Regional-Description_of_Observations_and_Models.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/nacp/NACP_Regional_Obs_Model_Grid/comp/Regional-Description_of_Observations_and_Models.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://daac.ornl.gov/graphics/browse/project/square/nacp_logo_square.png",
-                    "description": "Browse Image",
                     "@type": "dcat:Distribution",
+                    "description": "Browse Image",
+                    "downloadURL": "https://daac.ornl.gov/graphics/browse/project/square/nacp_logo_square.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 }
             ],
+            "graphic-preview-description": "Browse Image",
+            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/nacp_logo_square.png",
+            "identifier": "C2555119330-ORNL_CLOUD",
+            "issued": "2022-11-28",
+            "keyword": [
+                "atmospheric water vapor",
+                "ngda",
+                "atmosphere",
+                "biosphere",
+                "natural hazards",
+                "earth science",
+                "ecological dynamics",
+                "ecosystems",
+                "vegetation",
+                "human dimensions",
+                "land surface",
+                "national geospatial data asset",
+                "soils",
+                "agriculture"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1157",
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
             "spatial": "-170.0 10.0 -50.0 84.0",
+            "temporal": "1990-01-01T00:00:00Z/2007-12-31T23:59:59Z",
             "theme": [
                 "NACP",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "NACP Regional: Gridded 1-deg Observation Data and Biosphere and Inverse Model Outputs"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/FCHUV8F5Z8OD",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "High Mountain Asia Daily 0.05 x 0.05 deg Noah-MP Land Surface Model Reanalysis V001. Version 1. Archived by National Aeronautics and Space Administration, U.S. Government, NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/FCHUV8F5Z8OD.",
-            "issued": "2003-01-01",
-            "temporal": "2003-01-01T00:00:00Z/2020-12-31T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-12-31",
-            "keyword": [
-                "water budget",
-                "terrestrial hydrosphere",
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
-            "identifier": "C2808112558-NSIDC_ECS",
             "description": "This data set consists of a water budget reanalysis for the High Mountain Asia (HMA) region spanning the years 2003 through 2020. Estimates are provided for more than 30 parameters, including storages; fluxes; snow depth, extent, and snow water equivalent; temperature (land surface, soil, snow, and ice); surface albedo; soil moisture; evapotranspiration; and streamflow.\n\nThe data were generated using the Noah Multi-Parameterization (Noah-MP) land surface model (Version 4.0.1), driven by precipitation estimates and hydrological inputs developed specifically for HMA.",
-            "title": "High Mountain Asia Daily 0.05 x 0.05 deg Noah-MP Land Surface Model Reanalysis V001",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FFCHUV8F5Z8OD",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FFCHUV8F5Z8OD",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/HMA/HMA2_NLSMR.001/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/HMA/HMA2_NLSMR.001/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/data/data-access-tool/HMA2_NLSMR/versions/1/",
-                    "description": "Search and filter data files using a map-based interface",
                     "@type": "dcat:Distribution",
+                    "description": "Search and filter data files using a map-based interface",
+                    "downloadURL": "https://nsidc.org/data/data-access-tool/HMA2_NLSMR/versions/1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=HMA2_NLSMR+V001",
-                    "description": "Search and filter data files using a map-based interface",
                     "@type": "dcat:Distribution",
+                    "description": "Search and filter data files using a map-based interface",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=HMA2_NLSMR+V001",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/FCHUV8F5Z8OD",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/FCHUV8F5Z8OD",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/FCHUV8F5Z8OD",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/FCHUV8F5Z8OD",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C2808112558-NSIDC_ECS",
+            "issued": "2003-01-01",
+            "keyword": [
+                "water budget",
+                "terrestrial hydrosphere",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/FCHUV8F5Z8OD",
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
             "spatial": "60.0 20.0 111.0 46.0",
+            "temporal": "2003-01-01T00:00:00Z/2020-12-31T23:59:59.999Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "High Mountain Asia Daily 0.05 x 0.05 deg Noah-MP Land Surface Model Reanalysis V001"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/IMPACTS/NEXRAD/DATA111",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Brodzik, Stacy .2022. KDVN NEXRAD IMPACTS [indicate subset used]. Dataset available online from the NASA Global Hydrometeorology Resource Center DAAC, Huntsville, Alabama, U.S.A. DOI: http://dx.doi.org/10.5067/IMPACTS/NEXRAD/DATA111",
-            "issued": "2022-03-23",
-            "temporal": "2020-01-01T00:04:54Z/2020-03-01T00:07:49Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-31",
-            "keyword": [
-                "earth science",
-                "spectral/engineering",
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
-            "identifier": "C2025219690-GHRC_DAAC",
             "description": "The KDVN NEXRAD IMPACTS dataset consists of Next Generation Weather Radar (NEXRAD) Level II surveillance data that were collected at 31 NEXRAD sites from January 1 to March 1, 2020 during the Investigation of Microphysics and Precipitation for Atlantic Coast-Threatening Snowstorms  (IMPACTS) field campaign. IMPACTS was a three-year sequence of winter season deployments conducted to study snowstorms over the U.S Atlantic Coast. The campaign aimed to (1) Provide observations critical to understanding the mechanisms of snowband formation, organization, and evolution; (2) Examine how the microphysical characteristics and likely growth mechanisms of snow particles vary across snowbands; and (3) Improve snowfall remote sensing interpretation and modeling to significantly advance prediction capabilities. There are currently 160 Weather Surveillance Radar-1988 Doppler (WSR-88D) or NEXRAD sites throughout the United States and abroad. These Level II datasets contain meteorological and dual-polarization base data quantities including: radar reflectivity, radial velocity, spectrum width, differential reflectivity, differential phase, and cross correlation ratio. The IMPACTS NEXRAD Level II data files are available in netCDF-4 format. It should be noted that this dataset will be updated in subsequent years of the IMPACTS campaign.",
-            "title": "KDVN NEXRAD IMPACTS V1",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FIMPACTS%2FNEXRAD%2FDATA111",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FIMPACTS%2FNEXRAD%2FDATA111",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=kdvnimpacts",
-                    "description": "Files may be downloaded directly to your workstation from this link",
                     "@type": "dcat:Distribution",
+                    "description": "Files may be downloaded directly to your workstation from this link",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=kdvnimpacts",
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
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/impacts/NEXRAD/KDVN/doc/nexrad_datasets.pdf",
-                    "description": "NEXRAD IMPACTS User Guide",
                     "@type": "dcat:Distribution",
+                    "description": "NEXRAD IMPACTS User Guide",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/impacts/NEXRAD/KDVN/doc/nexrad_datasets.pdf",
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
+            "identifier": "C2025219690-GHRC_DAAC",
+            "issued": "2022-03-23",
+            "keyword": [
+                "earth science",
+                "spectral/engineering",
+                "radar"
+            ],
+            "landingPage": "https://doi.org/10.5067/IMPACTS/NEXRAD/DATA111",
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
             "spatial": "-96.109 37.482 -85.053 45.742",
+            "temporal": "2020-01-01T00:04:54Z/2020-03-01T00:07:49Z",
             "theme": [
                 "IMPACTS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "KDVN NEXRAD IMPACTS V1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.7927/H4JS9NC2",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Seirup, L., G. Yetman, and L. Razafindrazay. 2013-05-17. U.S. Census Grids (Summary File 3), 1990. Version 1.00. Palisades, NY. Archived by National Aeronautics and Space Administration, U.S. Government, NASA Socioeconomic Data and Applications Center (SEDAC). https://doi.org/10.7927/H4JS9NC2. https://doi.org/10.7927/H4JS9NC2.",
-            "issued": "2013-05-17",
-            "temporal": "1990-04-01T00:00:00Z/1990-04-01T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2013-05-17",
-            "references": [
-                "https://doi.org/10.7927/H42R3PMN"
-            ],
-            "keyword": [
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
-            "identifier": "C1000000181-SEDAC",
-            "description": "The U.S. Census Grids (Summary File 3), 1990 data set contains grids of demographic and socioeconomic data from the year 1990 U.S. census in ASCII and GeoTIFF formats. The grids have a resolution of 30 arc-seconds (0.0083 decimal degrees), or approximately 1 square km. The gridded variables are based on census block geography from Census 1990 TIGER/Line Files and census variables (population, households, and housing variables). This data set is produced by the Columbia University Center for International Earth Science Information Network (CIESIN).",
-            "release-place": "Palisades, NY",
-            "graphic-preview-description": "Sample browse graphic of the data set.",
             "creator": "Seirup, L., G. Yetman, and L. Razafindrazay",
-            "title": "U.S. Census Grids (Summary File 3), 1990",
-            "graphic-preview-file": "https://sedac.ciesin.columbia.edu/downloads/maps/usgrid/usgrid-summary-file3-1990/sedac-logo.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The U.S. Census Grids (Summary File 3), 1990 data set contains grids of demographic and socioeconomic data from the year 1990 U.S. census in ASCII and GeoTIFF formats. The grids have a resolution of 30 arc-seconds (0.0083 decimal degrees), or approximately 1 square km. The gridded variables are based on census block geography from Census 1990 TIGER/Line Files and census variables (population, households, and housing variables). This data set is produced by the Columbia University Center for International Earth Science Information Network (CIESIN).",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.7927%2FH4JS9NC2",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.7927%2FH4JS9NC2",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/downloads/maps/usgrid/usgrid-summary-file3-1990/sedac-logo.jpg",
-                    "description": "Sample browse graphic of the data set.",
                     "@type": "dcat:Distribution",
+                    "description": "Sample browse graphic of the data set.",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/downloads/maps/usgrid/usgrid-summary-file3-1990/sedac-logo.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/usgrid-summary-file3-1990/data-download",
-                    "description": "Data Download Page",
                     "@type": "dcat:Distribution",
+                    "description": "Data Download Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/usgrid-summary-file3-1990/data-download",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://sedac.ciesin.columbia.edu/data/set/usgrid-summary-file3-1990/docs",
-                    "description": "Documentation Page",
                     "@type": "dcat:Distribution",
+                    "description": "Documentation Page",
+                    "downloadURL": "http://sedac.ciesin.columbia.edu/data/set/usgrid-summary-file3-1990/docs",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/usgrid-summary-file3-1990",
-                    "description": "Data Set\u00a0Overview Page",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set\u00a0Overview Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/usgrid-summary-file3-1990",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "graphic-preview-description": "Sample browse graphic of the data set.",
+            "graphic-preview-file": "https://sedac.ciesin.columbia.edu/downloads/maps/usgrid/usgrid-summary-file3-1990/sedac-logo.jpg",
+            "identifier": "C1000000181-SEDAC",
+            "issued": "2013-05-17",
+            "keyword": [
+                "human dimensions",
+                "earth science",
+                "population"
+            ],
+            "landingPage": "https://doi.org/10.7927/H4JS9NC2",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2013-05-17",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "SEDAC"
+            },
+            "references": [
+                "https://doi.org/10.7927/H42R3PMN"
+            ],
+            "release-place": "Palisades, NY",
             "spatial": "-180.0 17.0 -65.0 72.0",
+            "temporal": "1990-04-01T00:00:00Z/1990-04-01T00:00:00Z",
             "theme": [
                 "USCG",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "U.S. Census Grids (Summary File 3), 1990"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-4-ESC2-67PCHURYUMOV-M14-V1.0",
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
+            "description": "This CODMAC level 4 data set contains radiometric calibrated and geometric distortion corrected (resampled) image data in W/m^2/sr/nm acquired by the OSIRIS Narrow Angle Camera during the COMET ESCORT 2 phase of the Rosetta mission, covering the period from 2015-03-10T23:25:00.000 to 2015-04-08T11:24:59.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-4-esc2-67pchuryumov-m14-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-4-ESC2-67PCHURYUMOV-M14-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-4-esc2-67pchuryumov-m14-v1.0",
-            "description": "This CODMAC level 4 data set contains radiometric calibrated and geometric distortion corrected (resampled) image data in W/m^2/sr/nm acquired by the OSIRIS Narrow Angle Camera during the COMET ESCORT 2 phase of the Rosetta mission, covering the period from 2015-03-10T23:25:00.000 to 2015-04-08T11:24:59.000.",
-            "title": "ROSETTA-ORBITER 67P OSINAC 4 ESC2-MTP014 RDR V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P OSINAC 4 ESC2-MTP014 RDR V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ASDC/SUBORBITAL/ARCTAS_Satellite_Data_1",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2022-09-06. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/ASDC/SUBORBITAL/ARCTAS_Satellite_Data_1.",
-            "issued": "2022-01-07",
-            "temporal": "2008-02-28T00:00:00Z/2008-08-02T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-09-06",
-            "keyword": [
-                "air quality",
-                "atmosphere",
-                "atmospheric chemistry",
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
-            "identifier": "C2449529636-LARC_ASDC",
             "description": "ARCTAS_Satellite_Data is the supplementary satellite data for the Arctic Research of the Composition of the Troposphere from Aircraft & Satellites sub-orbital campaign. Data from TES, MOPITT and OMI are featured in this data product and data collection is complete.\r\n\r\nThe Arctic is a critical region in understanding climate change. The responses of the Arctic to environmental perturbations such as warming, pollution, and emissions from forest fires in boreal Eurasia and North America include key processes such as the melting of ice sheets and permafrost, a decrease in snow albedo, and the deposition of halogen radical chemistry from sea salt aerosols to ice. Arctic Research of the Composition of the Troposphere from Aircraft and Satellites (ARCTAS) was a field campaign that explored environmental processes related to the high degree of climate sensitivity in the Arctic. ARCTAS was part of NASA\u2019s contribution to the International Global Atmospheric Chemistry (IGAC) Polar Study using Aircraft, Remote Sensing, Surface Measurements, and Models of Climate, Chemistry, Aerosols, and Transport (POLARCAT) Experiment for the International Polar Year 2007-2008.\r\n\r\nARCTAS had four primary objectives. The first was to understand long-range transport of pollution to the Arctic. Pollution brought to the Arctic from northern mid-latitude continents has environmental consequences, such as modifying regional and global climate and affecting the ozone budget. Prior to ARCTAS, these pathways remained largely uncertain. The second objective was to understand the atmospheric composition and climate implications of boreal forest fires; the smoke emissions from which act as an atmospheric perturbation to the Arctic by impacting the radiation budget and cloud processes and contributing to the production of tropospheric ozone. The third objective was to understand aerosol radiative forcing from climate perturbations, as the Arctic is an important place for understanding radiative forcing due to the rapid pace of climate change in the region and its unique radiative environment. The fourth objective of ARCTAS was to understand chemical processes with a focus on ozone, aerosols, mercury, and halogens. Additionally, ARCTAS sought to develop capabilities for incorporating data from aircraft and satellites related to pollution and related environmental perturbations in the Arctic into earth science models, expanding the potential for those models to predict future environmental change.\r\n\r\nARCTAS consisted of two, three-week aircraft deployments conducted in April and July 2008. The spring deployment sought to explore arctic haze, stratosphere-troposphere exchange, and sunrise photochemistry. April was chosen for the deployment phase due to historically being the peak in the seasonal accumulation of pollution from northern mid-latitude continents in the Arctic. The summer deployment sought to understand boreal forest fires at their most active seasonal phase in addition to stratosphere-troposphere exchange and summertime photochemistry.\r\n\r\nDuring ARCTAS, three NASA aircrafts, the DC-8, P-3B, and BE-200, conducted measurements and were equipped with suites of in-situ and remote sensing instrumentation. Airborne data was used in conjunction with satellite observations from AURA, AQUA, CloudSat, PARASOL, CALIPSO, and MISR.\r\n\r\nThe ASDC houses ARCTAS aircraft data, along with data related to MISR, a satellite instrument aboard the Terra satellite which provides measurements that provide information about the Earth\u2019s environment and climate.",
-            "title": "ARCTAS Supplementary Satellite Data Products",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC%2FSUBORBITAL%2FARCTAS_Satellite_Data_1",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC%2FSUBORBITAL%2FARCTAS_Satellite_Data_1",
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
-                    "downloadURL": "https://doi.org/10.5067/ASDC/SUBORBITAL/ARCTAS_Satellite_Data_1",
-                    "description": "DOI for ARCTAS_Satellite_Data_1",
                     "@type": "dcat:Distribution",
+                    "description": "DOI for ARCTAS_Satellite_Data_1",
+                    "downloadURL": "https://doi.org/10.5067/ASDC/SUBORBITAL/ARCTAS_Satellite_Data_1",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2449529636-LARC_ASDC",
-                    "description": "Earthdata search client for ARCTAS_Satellite_Data_1",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata search client for ARCTAS_Satellite_Data_1",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2449529636-LARC_ASDC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/ARCTAS/Satellite_Data_1/",
-                    "description": "ASDC Direct Data Download for ARCTAS_Satellite_Data_1",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for ARCTAS_Satellite_Data_1",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/ARCTAS/Satellite_Data_1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/ARCTAS/Satellite_Data_1/contents.html",
-                    "description": "OPeNDAP data access for ARCTAS_Satellite_Data_1",
                     "@type": "dcat:Distribution",
+                    "description": "OPeNDAP data access for ARCTAS_Satellite_Data_1",
+                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/ARCTAS/Satellite_Data_1/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 }
             ],
+            "identifier": "C2449529636-LARC_ASDC",
+            "issued": "2022-01-07",
+            "keyword": [
+                "air quality",
+                "atmosphere",
+                "atmospheric chemistry",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/ASDC/SUBORBITAL/ARCTAS_Satellite_Data_1",
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
             "spatial": "<?xml version=\"1.0\" encoding=\"UTF-8\"?><gml:Polygon xmlns:gml=\"http://www.opengis.net/gml/3.2\" srsName=\"EPSG:9825\"><gml:outerBoundaryIs><gml:LinearRing><gml:posList>-90.0 -180.0 -90.0 180.0 90.0 180.0 90.0 -180.0 -90.0 -180.0</gml:posList></gml:LinearRing></gml:outerBoundaryIs><gml:innerBoundaryIs></gml:innerBoundaryIs></gml:Polygon>",
+            "temporal": "2008-02-28T00:00:00Z/2008-08-02T23:59:59.999Z",
             "theme": [
                 "ARCTAS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "ARCTAS Supplementary Satellite Data Products"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.7927/H4W66HPJ",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Imhoff, M.L., L. Bounoua, T. Ricketts, C. Loucks, R. Harriss, and W.T. Lawrence. 2004-12-31. HANPP Collection: Human Appropriation of Net Primary Productivity as a Percentage of Net Primary Productivity. Version 1.00. Palisades, NY. Archived by National Aeronautics and Space Administration, U.S. Government, NASA Socioeconomic Data and Applications Center (SEDAC). https://doi.org/10.7927/H4W66HPJ. https://doi.org/10.7927/H4W66HPJ.",
-            "issued": "2004-12-31",
-            "temporal": "1995-01-01T00:00:00Z/1995-12-31T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2004-12-31",
-            "references": [
-                "https://doi.org/10.1038/nature02619",
-                "https://doi.org/10.7927/H48G8HMK",
-                "https://doi.org/10.7927/H44Q7RWV",
-                "https://doi.org/10.7927/H40Z715X"
-            ],
-            "keyword": [
-                "biosphere",
-                "earth science",
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
-            "identifier": "C139824018-SEDAC",
-            "description": "The HANPP Collection: Human Appropriation of Net Primary Productivity as a Percentage of Net Primary Productivity represents a map identifying regions in which human consumption of NPP is greatly in excess of production by local ecosystems.  Humans appropriate net primary productivity through the consumption of food, paper, wood and fiber, which alters the composition of the atmosphere, levels of biodiversity, energy flows within food webs and the provision of important ecosystem services. Net primary productivity (NPP), the net amount of solar energy converted to plant organic matter through photosynthesis, can be measured in Units of elemental carbon and represents the primary food energy source for the world's ecosystems.",
-            "release-place": "Palisades, NY",
-            "graphic-preview-description": "Maps Download Page",
             "creator": "Imhoff, M.L., L. Bounoua, T. Ricketts, C. Loucks, R. Harriss, and W.T. Lawrence",
-            "title": "HANPP Collection: Human Appropriation of Net Primary Productivity as a Percentage of Net Primary Productivity",
-            "graphic-preview-file": "https://sedac.ciesin.columbia.edu/data/set/hanpp-percentage-net-primary-productivity/maps",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The HANPP Collection: Human Appropriation of Net Primary Productivity as a Percentage of Net Primary Productivity represents a map identifying regions in which human consumption of NPP is greatly in excess of production by local ecosystems.  Humans appropriate net primary productivity through the consumption of food, paper, wood and fiber, which alters the composition of the atmosphere, levels of biodiversity, energy flows within food webs and the provision of important ecosystem services. Net primary productivity (NPP), the net amount of solar energy converted to plant organic matter through photosynthesis, can be measured in Units of elemental carbon and represents the primary food energy source for the world's ecosystems.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.7927%2FH4W66HPJ",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.7927%2FH4W66HPJ",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/downloads/maps/hanpp/hanpp-percentage-net-primary-productivity/hanpp-percentage-npp-thumbnail.jpg",
-                    "description": "Sample browse graphic of the data set.",
                     "@type": "dcat:Distribution",
+                    "description": "Sample browse graphic of the data set.",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/downloads/maps/hanpp/hanpp-percentage-net-primary-productivity/hanpp-percentage-npp-thumbnail.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/hanpp-percentage-net-primary-productivity/data-download",
-                    "description": "Data Download Page",
                     "@type": "dcat:Distribution",
+                    "description": "Data Download Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/hanpp-percentage-net-primary-productivity/data-download",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/hanpp-percentage-net-primary-productivity/maps",
-                    "description": "Maps Download Page",
                     "@type": "dcat:Distribution",
+                    "description": "Maps Download Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/hanpp-percentage-net-primary-productivity/maps",
+                    "mediaType": "text/html",
                     "title": "Get a related map visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://sedac.ciesin.columbia.edu/data/set/hanpp-percentage-net-primary-productivity/docs",
-                    "description": "Documentation Page",
                     "@type": "dcat:Distribution",
+                    "description": "Documentation Page",
+                    "downloadURL": "http://sedac.ciesin.columbia.edu/data/set/hanpp-percentage-net-primary-productivity/docs",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/hanpp-percentage-net-primary-productivity",
-                    "description": "Data Set\u00a0Overview Page",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set\u00a0Overview Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/hanpp-percentage-net-primary-productivity",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "graphic-preview-description": "Maps Download Page",
+            "graphic-preview-file": "https://sedac.ciesin.columbia.edu/data/set/hanpp-percentage-net-primary-productivity/maps",
+            "identifier": "C139824018-SEDAC",
+            "issued": "2004-12-31",
+            "keyword": [
+                "biosphere",
+                "earth science",
+                "vegetation"
+            ],
+            "landingPage": "https://doi.org/10.7927/H4W66HPJ",
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
+                "https://doi.org/10.7927/H44Q7RWV",
+                "https://doi.org/10.7927/H40Z715X"
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
+            "title": "HANPP Collection: Human Appropriation of Net Primary Productivity as a Percentage of Net Primary Productivity"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/5W8Q3I9WUFGX",
             "citation": "Global Modeling and Assimilation Office (GMAO). 2015-06-30. M2TMNXGLC. Version 5.12.4. MERRA-2 tavgM_2d_glc_Nx: 2d,Monthly mean,Time-Averaged,Single-Level,Assimilation,Land Ice Surface Diagnostics V5.12.4. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/5W8Q3I9WUFGX. https://disc.gsfc.nasa.gov/datacollection/M2TMNXGLC_5.12.4.html. Digital Science Data.",
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
-                "terrestrial hydrosphere",
-                "snow/ice",
-                "glaciers/ice sheets",
-                "sea ice",
-                "cryosphere"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "DANA OSTRENGA",
                 "hasEmail": "mailto:dana.ostrenga@nasa.gov"
             },
+            "creator": "Global Modeling and Assimilation Office (GMAO)",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C1276812853-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "M2TMNXGLC (or  tavgM_2d_glc_Nx) is a 2-dimensional monthly mean data collection in Modern-Era Retrospective analysis for Research and Applications version 2 (MERRA-2).  This collection consists of assimilated land ice surface diagnostics at the single levels, such as  fractional area of glaciated surface snow cover, snow mass over glaciated surface, snow depth over glaciated surface, and total snow mass residual due to densification. The collection also includes variance of certain parameters.\n\nMERRA-2 is the latest version of global atmospheric reanalysis for the satellite era produced by NASA Global Modeling and Assimilation Office (GMAO) using the Goddard Earth Observing System Model (GEOS) version 5.12.4.  The dataset covers the period of 1980-present with the latency of ~3 weeks after the end of a month. \n\nData Reprocessing:  Please check \u201cRecords of MERRA-2 Data Reprocessing and Service Changes\u201d linked from the \u201cDocumentation\u201d tab on this page.  Note that a reprocessed data filename is different from the original file.\n\nMERRA-2 Mailing List: Sign up to receive information on reprocessing of data, changing of tools and services, as well as data announcements from GMAO. Contact the GES DISC Help Desk (gsfc-dl-help-disc@mail.nasa.gov) to be added to the list.\n\nQuestions: If you have a question, please read \"MERRA-2 File Specification Document\",  \u201cMERRA-2 Data Access \u2013 Quick Start Guide\u201d, and FAQs linked from the \u201dDocumentation\u201d tab on this page.  If that does not answer your question, you may email the question on data access to the GES DISC Help Desk (gsfc-dl-help-disc@mail.nasa.gov), or the question on science to the MERRA-2 science team (merra-questions@lists.nasa.gov).",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "M2TMNXGLC",
-            "creator": "Global Modeling and Assimilation Office (GMAO)",
-            "graphic-preview-description": "The GES-DISC Interactive Online Visualization ANd aNalysis Interface (Giovanni) is a web-based tool that allows users to interactively visualize and analyze data.",
-            "title": "MERRA-2 tavgM_2d_glc_Nx: 2d,Monthly mean,Time-Averaged,Single-Level,Assimilation,Land Ice Surface Diagnostics 0.625 x 0.5 degree V5.12.4 (M2TMNXGLC) at GES DISC",
-            "graphic-preview-file": "https://giovanni.gsfc.nasa.gov/giovanni/#dataKeyword=M2TMNXGLC",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2F5W8Q3I9WUFGX",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2F5W8Q3I9WUFGX",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/M2TMNXGLC_5.12.4.png",
-                    "description": "M2TMNXGLC variable",
                     "@type": "dcat:Distribution",
+                    "description": "M2TMNXGLC variable",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/M2TMNXGLC_5.12.4.png",
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
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/M2TMNXGLC_5.12.4.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/M2TMNXGLC_5.12.4.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://goldsmr4.gesdisc.eosdis.nasa.gov/data/MERRA2_MONTHLY/M2TMNXGLC.5.12.4/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://goldsmr4.gesdisc.eosdis.nasa.gov/data/MERRA2_MONTHLY/M2TMNXGLC.5.12.4/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://giovanni.gsfc.nasa.gov/giovanni/#dataKeyword=M2TMNXGLC",
-                    "description": "The GES-DISC Interactive Online Visualization ANd aNalysis Interface (Giovanni) is a web-based tool that allows users to interactively visualize and analyze data.",
                     "@type": "dcat:Distribution",
+                    "description": "The GES-DISC Interactive Online Visualization ANd aNalysis Interface (Giovanni) is a web-based tool that allows users to interactively visualize and analyze data.",
+                    "downloadURL": "https://giovanni.gsfc.nasa.gov/giovanni/#dataKeyword=M2TMNXGLC",
+                    "mediaType": "text/html",
                     "title": "Get a related visualization through GIOVANNI"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=M2TMNXGLC",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=M2TMNXGLC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://goldsmr4.gesdisc.eosdis.nasa.gov/dods/M2TMNXGLC.info",
-                    "description": "The GrADS Data Server (GDS) is another form of OPeNDAP that provides subsetting and some analysis services across the Internet.",
                     "@type": "dcat:Distribution",
+                    "description": "The GrADS Data Server (GDS) is another form of OPeNDAP that provides subsetting and some analysis services across the Internet.",
+                    "downloadURL": "https://goldsmr4.gesdisc.eosdis.nasa.gov/dods/M2TMNXGLC.info",
+                    "mediaType": "text/html",
                     "title": "Use GRADS DATA SERVER (GDS) to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://goldsmr4.gesdisc.eosdis.nasa.gov/opendap/MERRA2_MONTHLY/M2TMNXGLC.5.12.4/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://goldsmr4.gesdisc.eosdis.nasa.gov/opendap/MERRA2_MONTHLY/M2TMNXGLC.5.12.4/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://goldsmr4.gesdisc.eosdis.nasa.gov/thredds/catalog/MERRA2_MONTHLY_aggregation/catalog.html?dataset=merra2_monthly_aggregation%2FM2TMNXGLC.5.12.4_Aggregation.ncml",
-                    "description": "Time aggregated THREDDS Data Server (TDS) ",
                     "@type": "dcat:Distribution",
+                    "description": "Time aggregated THREDDS Data Server (TDS) ",
+                    "downloadURL": "https://goldsmr4.gesdisc.eosdis.nasa.gov/thredds/catalog/MERRA2_MONTHLY_aggregation/catalog.html?dataset=merra2_monthly_aggregation%2FM2TMNXGLC.5.12.4_Aggregation.ncml",
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
-                    "downloadURL": "https://goldsmr4.gesdisc.eosdis.nasa.gov/data/MERRA2_MONTHLY/M2TMNXGLC.5.12.4/doc/MERRA2.README.pdf",
-                    "description": "README Document",
                     "@type": "dcat:Distribution",
+                    "description": "README Document",
+                    "downloadURL": "https://goldsmr4.gesdisc.eosdis.nasa.gov/data/MERRA2_MONTHLY/M2TMNXGLC.5.12.4/doc/MERRA2.README.pdf",
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
+            "graphic-preview-file": "https://giovanni.gsfc.nasa.gov/giovanni/#dataKeyword=M2TMNXGLC",
+            "identifier": "C1276812853-GES_DISC",
+            "issued": "2007-06-14",
+            "keyword": [
+                "earth science",
+                "terrestrial hydrosphere",
+                "snow/ice",
+                "glaciers/ice sheets",
+                "sea ice",
+                "cryosphere"
+            ],
+            "landingPage": "https://doi.org/10.5067/5W8Q3I9WUFGX",
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
+            "series-name": "M2TMNXGLC",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "1980-01-01T00:00:00Z/2022-01-17T00:00:00Z",
             "theme": [
                 "MERRA-2",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "MERRA-2 tavgM_2d_glc_Nx: 2d,Monthly mean,Time-Averaged,Single-Level,Assimilation,Land Ice Surface Diagnostics 0.625 x 0.5 degree V5.12.4 (M2TMNXGLC) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1413",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Chapin, E., S. Flores, L. Harcke, B.P. Hawkins, S. Hensley, T.R. Michel, R.J. Muellerschoen, J.G. Shimada, W.W. Tung, and C. Veeramachaneni. 2018. AirMOSS: L1 S-0 Polarimetric Data from AirMOSS P-band SAR, MOISST, 2012-2015. ORNL DAAC, Oak Ridge, Tennessee, USA. https://doi.org/10.3334/ORNLDAAC/1413",
-            "issued": "2018-05-01",
-            "temporal": "2012-10-24T00:00:00Z/2015-08-14T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-17",
-            "keyword": [
-                "earth science",
-                "radar",
-                "spectral/engineering"
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
-            "identifier": "C2274886681-ORNL_CLOUD",
             "description": "This data set provides level 1 (L1) polarimetric radar backscattering coefficient (sigma-0), multilook complex, polarimetrically calibrated, and georeferenced data products from the Airborne Microwave Observatory of Subcanopy and Subsurface (AirMOSS) radar instrument collected over the MOISST site in Oklahoma. The AirMOSS radar is a P-band (UHF) fully polarimetric synthetic aperture radar (SAR) currently operating in the 420-440 MHz band designed to measure root-zone soil moisture (RZSM) and is flown on a NASA Gulfstream-III aircraft. Flight campaigns took place at least biannually from 2012 to 2015 at 10 study sites across North America. The acquired L1 P-band radar backscatter data will be used to retrieve the RZSM at the study sites. Subsequent analyses will investigate both seasonal and inter-annual variability in soil moisture and the relationships to carbon fluxes and their associated uncertainties on a continental scale.",
-            "graphic-preview-description": "Browse Image",
-            "title": "AirMOSS: L1 S-0 Polarimetric Data from AirMOSS P-band SAR, MOISST, 2012-2015",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/sdat-tds/1413_1_fit.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1413",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1413",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/airmoss/campaign/AirMOSS_L1_Sigma0_Moisst/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/airmoss/campaign/AirMOSS_L1_Sigma0_Moisst/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/AIRMOSS/guides/AirMOSS_L1_Sigma0_Moisst.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/AIRMOSS/guides/AirMOSS_L1_Sigma0_Moisst.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1413",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1413",
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
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/airmoss/campaign/AirMOSS_L1_Sigma0_Moisst/comp/AirMOSS_L1_Sigma0_Moisst.pdf",
-                    "description": "AirMOSS: L1 S-0 Polarimetric Data from AirMOSS P-band SAR, MOISST, 2012-2015: AirMOSS_L1_Sigma0_Moisst.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "AirMOSS: L1 S-0 Polarimetric Data from AirMOSS P-band SAR, MOISST, 2012-2015: AirMOSS_L1_Sigma0_Moisst.pdf",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/airmoss/campaign/AirMOSS_L1_Sigma0_Moisst/comp/AirMOSS_L1_Sigma0_Moisst.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
-                },
-                {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://daac.ornl.gov/graphics/browse/sdat-tds/1413_1_fit.png",
-                    "description": "Browse Image",
+                },
+                {
                     "@type": "dcat:Distribution",
+                    "description": "Browse Image",
+                    "downloadURL": "https://daac.ornl.gov/graphics/browse/sdat-tds/1413_1_fit.png",
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
-                    "downloadURL": "https://thredds.daac.ornl.gov/thredds/catalog/ornldaac/1413/catalog.html",
-                    "description": "The THREDDS location for this Collection.",
                     "@type": "dcat:Distribution",
+                    "description": "The THREDDS location for this Collection.",
+                    "downloadURL": "https://thredds.daac.ornl.gov/thredds/catalog/ornldaac/1413/catalog.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "graphic-preview-description": "Browse Image",
+            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/sdat-tds/1413_1_fit.png",
+            "identifier": "C2274886681-ORNL_CLOUD",
+            "issued": "2018-05-01",
+            "keyword": [
+                "earth science",
+                "radar",
+                "spectral/engineering"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1413",
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
             "spatial": "-99.0 35.78 -96.82 36.89",
+            "temporal": "2012-10-24T00:00:00Z/2015-08-14T23:59:59Z",
             "theme": [
                 "AirMOSS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "AirMOSS: L1 S-0 Polarimetric Data from AirMOSS P-band SAR, MOISST, 2012-2015"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=IHW-C-IRPHOT-3-RDR-HALLEY-V1.0",
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
+            "description": "NASA's International Halley Watch (IHW) has created a Comet Halley Archive. The collection of data spans the full wavelength range as submitted by scientists to the IHW. The observations belong to one of the following Disciplines: Amateur, Astrometry, Infrared Studies, Large-Scale Phenomena, Meteor Studies, Near-Nucleus Studies, Photometry and Polarimetry, Radio Studies, and Spectroscopy and Spectrophotometry. The data collected by these nine disciplines were augmented by Spacecraft measurements. The data were submitted to IHW, but the evaluation and selection for the Archive has been the primary responsibility of the Discipline Specialist Teams for each network in cooperation with the Lead Center. The data from the Infrared Photometry subnetwork contains 2204 observations spanning dates from 1984 September 14 through 1988 April 08.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ihw-c-irphot-3-rdr-halley-v1.0_bgty-2ycd",
+            "issued": "2018-06-26",
+            "keyword": [
+                "international halley watch",
+                "halley"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=IHW-C-IRPHOT-3-RDR-HALLEY-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ihw-c-irphot-3-rdr-halley-v1.0_bgty-2ycd",
-            "description": "NASA's International Halley Watch (IHW) has created a Comet Halley Archive. The collection of data spans the full wavelength range as submitted by scientists to the IHW. The observations belong to one of the following Disciplines: Amateur, Astrometry, Infrared Studies, Large-Scale Phenomena, Meteor Studies, Near-Nucleus Studies, Photometry and Polarimetry, Radio Studies, and Spectroscopy and Spectrophotometry. The data collected by these nine disciplines were augmented by Spacecraft measurements. The data were submitted to IHW, but the evaluation and selection for the Archive has been the primary responsibility of the Discipline Specialist Teams for each network in cooperation with the Lead Center. The data from the Infrared Photometry subnetwork contains 2204 observations spanning dates from 1984 September 14 through 1988 April 08.",
-            "title": "IHW COMET HALLEY INFRARED PHOTOMETRY V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "IHW COMET HALLEY INFRARED PHOTOMETRY V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.nasa.gov/d/bgui-7jtm",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Steve Kempler",
+                "hasEmail": "mailto:Steven.J.Kempler@nasa.gov"
+            },
+            "description": "The NASA Goddard Earth Sciences (GES) Data and Information Services Center (DISC) is the home (archive) of Precipitation, Atmospheric Chemistry and Dynamics, and information, as well as data and information from other related disciplines.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://disc.sci.gsfc.nasa.gov/",
+                    "mediaType": "text/html"
+                }
+            ],
+            "identifier": "NASA-0000049",
             "issued": "2018-06-25",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
             "keyword": [
                 "earth science",
                 "airs",
@@ -533780,501 +533792,470 @@
                 "mirador",
                 "precipitation"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Steve Kempler",
-                "hasEmail": "mailto:Steven.J.Kempler@nasa.gov"
-            },
+            "landingPage": "https://data.nasa.gov/d/bgui-7jtm",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "NASA-0000049",
-            "description": "The NASA Goddard Earth Sciences (GES) Data and Information Services Center (DISC) is the home (archive) of Precipitation, Atmospheric Chemistry and Dynamics, and information, as well as data and information from other related disciplines.",
-            "title": "Goddard Earth Sciences Data and Information Services Center (GES DISC)",
-            "programCode": [
-                "026:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://disc.sci.gsfc.nasa.gov/",
-                    "mediaType": "text/html"
-                }
-            ],
-            "accrualPeriodicity": "irregular"
+            "title": "Goddard Earth Sciences Data and Information Services Center (GES DISC)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1996",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Denbina, M.W., M. Simard, and E. Rodriguez. 2021. Delta-X: AirSWOT Level 1B Interferogram Products in Radar Coordinates, 2021. ORNL DAAC, Oak Ridge, Tennessee, USA. https://doi.org/10.3334/ORNLDAAC/1996",
-            "issued": "2022-08-29",
-            "temporal": "2021-03-26T00:00:00Z/2021-09-12T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-06-12",
-            "keyword": [
-                "terrestrial hydrosphere",
-                "biosphere",
-                "earth science",
-                "surface water",
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
-            "identifier": "C2428617287-ORNL_CLOUD",
             "description": "This dataset contains AirSWOT interferogram products collected during the 2021 Delta-X Campaign over the Atchafalaya and Terrebonne Basins of the Mississippi River Delta, Louisiana, USA from 2021-03-26 to 2021-04-18 (Spring) and 2021-08-21 to 2021-09-12 (Fall). AirSWOT uses near-nadir wide-swath Ka-band radar interferometry to measure water-surface elevation and produce continuous gridded elevation data. AirSWOT elevation data is useful for calibrating elevation and slopes along the main channels, as well as tying observations to open ocean tidal conditions. The AirSWOT Level 1B (L1B) data products represent interferogram data in the radar coordinate system, not in georeferenced map coordinates. This is an earlier stage of data processing which is used to generate the later Level 2 and Level 3 data products which will contain georeferenced water heights and water height profiles for river channels in each basin. The data are provided in binary and text file formats.",
-            "graphic-preview-description": "AirSWOT L1B noise-subtracted reference power (left image) and complex interferogram (right image) collected on April 1, 2021 (Flight Line ID: 124406).  In the complex interferogram image, the brightness of each pixel corresponds to the interferogram coherence magnitude, while the color of each pixel corresponds to the interferogram phase (as shown in the colorbar).",
-            "title": "Delta-X: AirSWOT Level 1B Interferogram Products in Radar Coordinates, 2021",
-            "graphic-preview-file": "https://daac.ornl.gov/DELTAX/guides/DeltaX_L1b_AirSWOT_Fig1.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1996",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1996",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/deltax/DeltaX_L1b_AirSWOT/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/deltax/DeltaX_L1b_AirSWOT/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/DELTAX/guides/DeltaX_L1b_AirSWOT.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/DELTAX/guides/DeltaX_L1b_AirSWOT.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1996",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1996",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/deltax/DeltaX_L1b_AirSWOT/comp/DeltaX_L1b_AirSWOT.pdf",
-                    "description": "Delta-X: AirSWOT Level 1B Interferogram Products in Radar Coordinates, 2021: DeltaX_L1b_AirSWOT.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "Delta-X: AirSWOT Level 1B Interferogram Products in Radar Coordinates, 2021: DeltaX_L1b_AirSWOT.pdf",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/deltax/DeltaX_L1b_AirSWOT/comp/DeltaX_L1b_AirSWOT.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://daac.ornl.gov/DELTAX/guides/DeltaX_L1b_AirSWOT_Fig1.png",
-                    "description": "AirSWOT L1B noise-subtracted reference power (left image) and complex interferogram (right image) collected on April 1, 2021 (Flight Line ID: 124406).  In the complex interferogram image, the brightness of each pixel corresponds to the interferogram coherence magnitude, while the color of each pixel corresponds to the interferogram phase (as shown in the colorbar).",
                     "@type": "dcat:Distribution",
+                    "description": "AirSWOT L1B noise-subtracted reference power (left image) and complex interferogram (right image) collected on April 1, 2021 (Flight Line ID: 124406).  In the complex interferogram image, the brightness of each pixel corresponds to the interferogram coherence magnitude, while the color of each pixel corresponds to the interferogram phase (as shown in the colorbar).",
+                    "downloadURL": "https://daac.ornl.gov/DELTAX/guides/DeltaX_L1b_AirSWOT_Fig1.png",
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
+            "graphic-preview-description": "AirSWOT L1B noise-subtracted reference power (left image) and complex interferogram (right image) collected on April 1, 2021 (Flight Line ID: 124406).  In the complex interferogram image, the brightness of each pixel corresponds to the interferogram coherence magnitude, while the color of each pixel corresponds to the interferogram phase (as shown in the colorbar).",
+            "graphic-preview-file": "https://daac.ornl.gov/DELTAX/guides/DeltaX_L1b_AirSWOT_Fig1.png",
+            "identifier": "C2428617287-ORNL_CLOUD",
+            "issued": "2022-08-29",
+            "keyword": [
+                "terrestrial hydrosphere",
+                "biosphere",
+                "earth science",
+                "surface water",
+                "ecosystems"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1996",
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
             "spatial": "-91.54 29.07 -90.58 29.8",
+            "temporal": "2021-03-26T00:00:00Z/2021-09-12T23:59:59Z",
             "theme": [
                 "Delta-X",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Delta-X: AirSWOT Level 1B Interferogram Products in Radar Coordinates, 2021"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=P12-V-ORAD-4-ALT%2FRAD-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This data set consists of groups of measurements made by the Radar Mapper experiment on the Pioneer Venus Orbiter spacecraft. The measurements were made during each approximately 12-second spacecraft rotation period for a period of 32 minutes on either side of periapsis, when the range to the surface was less than about 4500 kilometers. During those 12 seconds, up to 8 measurements were made: (a) cold-sky received calibration when the antenna pointed to the zenith, (b) 'early' imaging, when the antenna pointer at an angle of between 10 and 40 degrees from nadir, (c) planetary thermal noise temperature when the antenna pointed to the nadir (d) one altimetry measurement, or (d-g) four altimetry measurements, and (h) 'late' imaging, when the antenna again pointed at an angle of between 10 and 40 degrees from nadir, but on the other side from 'early' imaging.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.p12-v-orad-4-alt-rad-v1.0_bgv4-xn9r",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "pioneer",
                 "pre-magellan",
                 "venus"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=P12-V-ORAD-4-ALT%2FRAD-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.p12-v-orad-4-alt-rad-v1.0_bgv4-xn9r",
-            "description": "This data set consists of groups of measurements made by the Radar Mapper experiment on the Pioneer Venus Orbiter spacecraft. The measurements were made during each approximately 12-second spacecraft rotation period for a period of 32 minutes on either side of periapsis, when the range to the surface was less than about 4500 kilometers. During those 12 seconds, up to 8 measurements were made: (a) cold-sky received calibration when the antenna pointed to the zenith, (b) 'early' imaging, when the antenna pointer at an angle of between 10 and 40 degrees from nadir, (c) planetary thermal noise temperature when the antenna pointed to the nadir (d) one altimetry measurement, or (d-g) four altimetry measurements, and (h) 'late' imaging, when the antenna again pointed at an angle of between 10 and 40 degrees from nadir, but on the other side from 'early' imaging.",
-            "title": "P12 V ORBITING RADAR RESAMPLED ALTIMETER/RADIOMETER V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "P12 V ORBITING RADAR RESAMPLED ALTIMETER/RADIOMETER V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-5-DDR-ASTEROID-DENSITIES-V1.1",
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
+            "description": "This data set contains a tabulation of asteroid masses, diameters, and bulk densities compiled by D. T. Britt and published in Table 1 of Britt, et al. (2002) [BRITTETAL2002] in the 'Asteroids III' volume.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-5-ddr-asteroid-densities-v1.1_bgxa-b7p2",
+            "issued": "2018-06-26",
+            "keyword": [
+                "asteroid",
+                "support archives"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-5-DDR-ASTEROID-DENSITIES-V1.1",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-5-ddr-asteroid-densities-v1.1_bgxa-b7p2",
-            "description": "This data set contains a tabulation of asteroid masses, diameters, and bulk densities compiled by D. T. Britt and published in Table 1 of Britt, et al. (2002) [BRITTETAL2002] in the 'Asteroids III' volume.",
-            "title": "ASTEROID DENSITIES",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "ASTEROID DENSITIES"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1024",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Saatchi, S.S., B. Nelson, E. Podest, and J. Holt. 2011. LBA-ECO LC-15 JERS-1 Synthetic Aperture Radar, 1- km Mosaic, Amazon Basin: 1995-1996. ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/1024",
-            "issued": "2023-10-03",
-            "temporal": "1995-08-01T00:00:00Z/1996-06-30T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-10-05",
-            "keyword": [
-                "spectral/engineering",
-                "earth science",
-                "land surface",
-                "radar",
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
-            "identifier": "C2777844591-ORNL_CLOUD",
             "description": "This data set contains two image mosaics of L-band radar backscatter and two image mosaics of first order texture. The two backscatter images are mosaics of L-band Radar Backscatter at Horizontal-Horizontal (HH) Polarization created from 1,500 images collected by the Japanese Earth Resources Satellite-1 (JERS-1) Synthetic Aperture Radar (SAR) over the Amazon River Basin as part of the Global Rainforest Mapping Project (GRMP). These backscatter image mosaics were developed using data collected over 62 days from August to November of 1995 for the peak of the dry season and for 62 days from May to June of 1996 during the peak of the wet season. The two image mosaics are at 3 arc-sec resolution. Data provided under this project are resampled images at 30 arc-sec resolution (or about 1 km resolution). For each radar backscatter image, first order texture statistical information was derived and is distributed along with the image mosaic.This data set contains four images each in both geotiff and ENVI formats, provided in eight zip files.  The four files in ENVI file format contain o_envi? in their file name and when extrapolated contain an envi image (*_envi.dat) and an envi image header file (_envi.hdr). The four files in geotiff format contain o_geotiff?  in their file name and when extrapolated contain *.tif and *.tfw file pairs. See Section 2 for more information about the characteristics of these data files.",
-            "graphic-preview-description": "Browse Image",
-            "title": "LBA-ECO LC-15 JERS-1 Synthetic Aperture Radar, 1- km Mosaic, Amazon Basin: 1995-1996",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/sdat-tds/1024_1_fit.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1024",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1024",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/lba/land_use_land_cover_change/LC15_GRFM_JERS1_Mosaic/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/lba/land_use_land_cover_change/LC15_GRFM_JERS1_Mosaic/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/LBA/guides/LC15_GRFM_JERS1_Mosaic.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/LBA/guides/LC15_GRFM_JERS1_Mosaic.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1024",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1024",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC15_GRFM_JERS1_Mosaic/comp/LC15_GRFM_JERS1_Mosaic.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC15_GRFM_JERS1_Mosaic/comp/LC15_GRFM_JERS1_Mosaic.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://daac.ornl.gov/graphics/browse/sdat-tds/1024_1_fit.png",
-                    "description": "Browse Image",
                     "@type": "dcat:Distribution",
+                    "description": "Browse Image",
+                    "downloadURL": "https://daac.ornl.gov/graphics/browse/sdat-tds/1024_1_fit.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://webmap.ornl.gov/wcsdown/dataset.jsp?ds_id=1024",
-                    "description": "Web Coverage Service for this collection.",
                     "@type": "dcat:Distribution",
+                    "description": "Web Coverage Service for this collection.",
+                    "downloadURL": "https://webmap.ornl.gov/wcsdown/dataset.jsp?ds_id=1024",
+                    "mediaType": "text/html",
                     "title": "Use Web Coverage Service (WCS) to download the dataset's data"
                 }
             ],
+            "graphic-preview-description": "Browse Image",
+            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/sdat-tds/1024_1_fit.png",
+            "identifier": "C2777844591-ORNL_CLOUD",
+            "issued": "2023-10-03",
+            "keyword": [
+                "spectral/engineering",
+                "earth science",
+                "land surface",
+                "radar",
+                "land use/land cover"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1024",
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
             "spatial": "-82.72 -23.43 -47.02 13.86",
+            "temporal": "1995-08-01T00:00:00Z/1996-06-30T23:59:59Z",
             "theme": [
                 "LBA-ECO",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "LBA-ECO LC-15 JERS-1 Synthetic Aperture Radar, 1- km Mosaic, Amazon Basin: 1995-1996"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-4-ESC2-67P-M16-REFLECT-V1.0",
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
+            "description": "This CODMAC level 4 data set contains radiometric calibrated and geometric distortion corrected (resampled) image data in reflectance units (normalized and thus without unit), acquired by the OSIRIS Wide Angle Camera on the Rosetta spacecraft during the COMET ESCORT 2 mission phase, covering the period from 2015-05-05T23:25:00.000 to 2015-06-02T23:24:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V1.0 is the first version of this dataset: Lien corrected dataset after October 2018 PSA/PDS external peer review.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-4-esc2-67p-m16-reflect-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-4-ESC2-67P-M16-REFLECT-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-4-esc2-67p-m16-reflect-v1.0",
-            "description": "This CODMAC level 4 data set contains radiometric calibrated and geometric distortion corrected (resampled) image data in reflectance units (normalized and thus without unit), acquired by the OSIRIS Wide Angle Camera on the Rosetta spacecraft during the COMET ESCORT 2 mission phase, covering the period from 2015-05-05T23:25:00.000 to 2015-06-02T23:24:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V1.0 is the first version of this dataset: Lien corrected dataset after October 2018 PSA/PDS external peer review.",
-            "title": "ROSETTA-ORBITER 67P OSIWAC 4 ESC2-MTP016 RDR-REFLECT V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P OSIWAC 4 ESC2-MTP016 RDR-REFLECT V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/226",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Kittel, T.G.F., N.A. Rosenbloom, T.H. Painter, D.S. Schimel, H.H. Fisher, A. Grimsdell, VEMAP Participants, C. Daly, and E.R. Hunt. 1998. VEMAP 1: U.S. Site Files . ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/226",
-            "issued": "2024-04-26",
-            "temporal": "1961-01-01T00:00:00Z/1990-12-31T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-04-26",
-            "keyword": [
-                "atmospheric water vapor",
-                "atmospheric winds",
-                "atmosphere",
-                "earth science",
-                "precipitation",
-                "atmospheric temperature",
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
-            "identifier": "C2954622639-ORNL_CLOUD",
             "description": "An integrated input data set for ecosystem and vegetation modeling for the conterminous United States: Site Files",
-            "graphic-preview-description": "Browse Image",
-            "title": "VEMAP 1: U.S. Site Files",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/vemap_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F226",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F226",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/vemap/vemap-1_siteFile/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/vemap/vemap-1_siteFile/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/VEMAP/guides/site.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/VEMAP/guides/site.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/226",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/226",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/vemap/vemap-1_siteFile/comp/CORRECT.txt",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/vemap/vemap-1_siteFile/comp/CORRECT.txt",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/vemap/vemap-1_siteFile/comp/FORMAT.SIT",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/vemap/vemap-1_siteFile/comp/FORMAT.SIT",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/vemap/vemap-1_siteFile/comp/Phase_1_User_Guide.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/vemap/vemap-1_siteFile/comp/Phase_1_User_Guide.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/vemap/vemap-1_siteFile/comp/README.SIT",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/vemap/vemap-1_siteFile/comp/README.SIT",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/vemap/vemap-1_siteFile/comp/README.vem",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/vemap/vemap-1_siteFile/comp/README.vem",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/vemap/vemap-1_siteFile/comp/site.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/vemap/vemap-1_siteFile/comp/site.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/vemap/vemap-1_siteFile/comp/SVF_FORMAT.txt",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/vemap/vemap-1_siteFile/comp/SVF_FORMAT.txt",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/vemap/vemap-1_siteFile/comp/VEMAPDOC.txt",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/vemap/vemap-1_siteFile/comp/VEMAPDOC.txt",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://daac.ornl.gov/graphics/browse/project/square/vemap_logo_square.png",
-                    "description": "Browse Image",
                     "@type": "dcat:Distribution",
+                    "description": "Browse Image",
+                    "downloadURL": "https://daac.ornl.gov/graphics/browse/project/square/vemap_logo_square.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 }
             ],
+            "graphic-preview-description": "Browse Image",
+            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/vemap_logo_square.png",
+            "identifier": "C2954622639-ORNL_CLOUD",
+            "issued": "2024-04-26",
+            "keyword": [
+                "atmospheric water vapor",
+                "atmospheric winds",
+                "atmosphere",
+                "earth science",
+                "precipitation",
+                "atmospheric temperature",
+                "atmospheric radiation"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/226",
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
             "spatial": "-124.5 25.0 -67.0 49.0",
+            "temporal": "1961-01-01T00:00:00Z/1990-12-31T23:59:59Z",
             "theme": [
                 "VEMAP",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "VEMAP 1: U.S. Site Files"
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
-                "grs"
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
-            "identifier": "NASA-670",
             "description": "GRS",
-            "title": "PDS Odyssey Data Release 28-GRS",
-            "programCode": [
-                "026:005"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -534282,127 +534263,124 @@
                     "mediaType": "application/html"
                 }
             ],
-            "accrualPeriodicity": "irregular",
+            "identifier": "NASA-670",
+            "issued": "2018-06-25",
+            "keyword": [
+                "pds",
+                "grs"
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
+            "title": "PDS Odyssey Data Release 28-GRS"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-E-OSIWAC-4-EAR3-EARTH-REFLECT-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This CODMAC level 4 data set contains radiometric calibrated and geometric distortion corrected (resampled)  image data in reflectance units (normalized and thus without unit),  acquired by the OSIRIS Wide Angle Camera on the Rosetta spacecraft  during the EARTH SWING-BY 3 mission phase, covering the period  from 2009-09-14T00:00:00.000 to 2009-12-13T23:59:59.000. The prime target is planet Earth. This version V1.0 is the first version of this dataset.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-e-osiwac-4-ear3-earth-reflect-v1.0",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2021-05-21",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "international rosetta mission",
                 "earth",
                 "moon"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-E-OSIWAC-4-EAR3-EARTH-REFLECT-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-e-osiwac-4-ear3-earth-reflect-v1.0",
-            "description": "This CODMAC level 4 data set contains radiometric calibrated and geometric distortion corrected (resampled)  image data in reflectance units (normalized and thus without unit),  acquired by the OSIRIS Wide Angle Camera on the Rosetta spacecraft  during the EARTH SWING-BY 3 mission phase, covering the period  from 2009-09-14T00:00:00.000 to 2009-12-13T23:59:59.000. The prime target is planet Earth. This version V1.0 is the first version of this dataset.",
-            "title": "ROSETTA-ORBITER EARTH OSIWAC 4 EAR3 RDR-REFLECT V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER EARTH OSIWAC 4 EAR3 RDR-REFLECT V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=C130-E-ASAS-3-RDR-IMAGE-V1.0",
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
+            "description": "Most of the ASAS data acquired for GRSFE were taken during flights over Lunar Lake, Nevada, at a nominal altitude of 5000 m above ground level. Flights over Lunar Lake were repeated to acquire data for a range of solar zenith angles and to obtain data for several view azimuth angles (i.e., for several flight headings relative to the solar principal plane). On most flights, the sensor field of view was initially pointed forward 45 degrees as the aircraft approached the site. The sensor then imaged the site through a sequence of seven fore-to-aft view directions ranging from 45 degrees forward to 45 degrees aft in 15 degree increments as the aircraft flew over the site. The primary target of interest was the Lunar Lake playa, but the digital images also include data for the lava flow and cobble areas within and around the playa. Data were acquired in a similar manner on one flight over the Ubehebe Crater. One flight over Lunar Lake was also flown approximately along the solar principal plane with the ASAS view zenith angle fixed at the solar zenith angle. The purpose of this flight was to observe the opposition effect.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.c130-e-asas-3-rdr-image-v1.0_bh8t-x8pb",
+            "issued": "2018-06-26",
+            "keyword": [
+                "earth",
+                "geologic remote sensing field experiment"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=C130-E-ASAS-3-RDR-IMAGE-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.c130-e-asas-3-rdr-image-v1.0_bh8t-x8pb",
-            "description": "Most of the ASAS data acquired for GRSFE were taken during flights over Lunar Lake, Nevada, at a nominal altitude of 5000 m above ground level. Flights over Lunar Lake were repeated to acquire data for a range of solar zenith angles and to obtain data for several view azimuth angles (i.e., for several flight headings relative to the solar principal plane). On most flights, the sensor field of view was initially pointed forward 45 degrees as the aircraft approached the site. The sensor then imaged the site through a sequence of seven fore-to-aft view directions ranging from 45 degrees forward to 45 degrees aft in 15 degree increments as the aircraft flew over the site. The primary target of interest was the Lunar Lake playa, but the digital images also include data for the lava flow and cobble areas within and around the playa. Data were acquired in a similar manner on one flight over the Ubehebe Crater. One flight over Lunar Lake was also flown approximately along the solar principal plane with the ASAS view zenith angle fixed at the solar zenith angle. The purpose of this flight was to observe the opposition effect.",
-            "title": "C130 EARTH ASAS CALIBRATED REDUCED DATA RECORD IMAGE V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "C130 EARTH ASAS CALIBRATED REDUCED DATA RECORD IMAGE V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/MEASURES/NIMBUS7/SMMR/DATA201",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Chris Kidd. PRECIP_SMMR_NIMBUS7. Version 1. NASA MEASURES Precipitation Ensemble based on SMMR Nimbus-7 NSIDC L1B Tbs. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/MEASURES/NIMBUS7/SMMR/DATA201. https://measures.gsfc.nasa.gov/datacollection/PRECIP_SMMR_NIMBUS7_1.html. Digital Science Data.",
-            "issued": "2021-06-10",
-            "temporal": "1979-01-02T01:08:00Z/1987-08-20T14:02:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2021-06-10",
-            "keyword": [
-                "earth science",
-                "precipitation",
-                "atmosphere"
-            ],
-            "data-presentation-form": "Digital Science Data",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Chris Kidd",
                 "hasEmail": "mailto:chris.kidd@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
-            "identifier": "C2368307664-GES_DISC",
-            "description": "The data presented in this level 2 orbital product are rain rate estimates expressed as mm/hour determined from brightness temperatures (Tbs) obtained from the Scanning Multichannel Microwave Radiometer (SMMR) flown on the Nimbus-7 satellite. Most of the products generated in this data set are based upon the algorithms developed for the 3rd Algorithm Intercomparison Project (AIP-3) of the Global Precipitation Climatology Project (GPCP).  Details of these 15 algorithms and development of a quality score which is a measure of confidence in the estimate, along with processing and algorithmic flags, can be found in the Algorithm Theoretical Basis Document  (ATBD).  The data in this product cover the period from 1979 to 1987 with one file per orbit.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "PRECIP_SMMR_NIMBUS7",
             "creator": "Chris Kidd",
-            "title": "NASA MEASURES Precipitation Ensemble based on SMMR Nimbus-7 NSIDC L1B Tbs 1-orbit L2 Swath 25x25km V1 (PRECIP_SMMR_NIMBUS7) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/PRECIP_SMMR_NIMBUS7.png",
-            "programCode": [
-                "026:001"
-            ],
+            "data-presentation-form": "Digital Science Data",
+            "description": "The data presented in this level 2 orbital product are rain rate estimates expressed as mm/hour determined from brightness temperatures (Tbs) obtained from the Scanning Multichannel Microwave Radiometer (SMMR) flown on the Nimbus-7 satellite. Most of the products generated in this data set are based upon the algorithms developed for the 3rd Algorithm Intercomparison Project (AIP-3) of the Global Precipitation Climatology Project (GPCP).  Details of these 15 algorithms and development of a quality score which is a measure of confidence in the estimate, along with processing and algorithmic flags, can be found in the Algorithm Theoretical Basis Document  (ATBD).  The data in this product cover the period from 1979 to 1987 with one file per orbit.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMEASURES%2FNIMBUS7%2FSMMR%2FDATA201",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMEASURES%2FNIMBUS7%2FSMMR%2FDATA201",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
@@ -534442,31 +534420,67 @@
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://measures.gesdisc.eosdis.nasa.gov/opendap/Precipitation/PRECIP_SMMR_NIMBUS7.1/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://measures.gesdisc.eosdis.nasa.gov/opendap/Precipitation/PRECIP_SMMR_NIMBUS7.1/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 }
             ],
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/PRECIP_SMMR_NIMBUS7.png",
+            "identifier": "C2368307664-GES_DISC",
+            "issued": "2021-06-10",
+            "keyword": [
+                "earth science",
+                "precipitation",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.5067/MEASURES/NIMBUS7/SMMR/DATA201",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2021-06-10",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
+            },
+            "release-place": "Greenbelt, MD, USA",
+            "series-name": "PRECIP_SMMR_NIMBUS7",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "1979-01-02T01:08:00Z/1987-08-20T14:02:00Z",
             "theme": [
                 "MEaSUREs",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "NASA MEASURES Precipitation Ensemble based on SMMR Nimbus-7 NSIDC L1B Tbs 1-orbit L2 Swath 25x25km V1 (PRECIP_SMMR_NIMBUS7) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.nasa.gov/d/bhd4-cidu",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "GeneLab Outreach",
+                "hasEmail": "mailto:genelab-outreach@lists.nasa.gov"
+            },
+            "description": "Astronauts have been previously shown to exhibit decreased salivary lysozyme and increased dental calculus and gingival inflammation in response to space flight host factors that could contribute to oral diseases such as caries and periodontitis. However the specific physiological response of caries-causing bacteria such as Streptococcus mutans to space flight and/or ground-based simulated microgravity has not been extensively investigated. In this study High Aspect Ratio Vessel (HARV) S. mutans simulated microgravity and normal gravity cultures were assessed for changes in metabolite and transcriptome profiles H2O2 resistance and competence in sucrose-containing biofilm media. Stationary phase S. mutans simulated microgravity cultures displayed increased killing by H2O2 compared to normal gravity control cultures but competence was not affected. RNA-seq analysis revealed that expression of 153 genes was up-regulated >= 2-fold and 94 genes down-regulated >= 2-fold during simulated microgravity HARV growth. These included a number of genes located on extrachromosomal elements as well as genes involved in carbohydrate metabolism translation and stress responses. Collectively these results suggest that growth under microgravity analog conditions promotes changes in S. mutans gene expression and physiology that may translate to an altered cariogenic potential of this organism during space flight missions. Overall design: Differential gene expression was compared between RNA from S. mutans grown in normal gravity HARVs (n=3 independent cultures) and RNA from S. mutans grown in simulated microgravity HARVs (n=3 independent cultures)",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "GeneLab Study Page",
+                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-106",
+                    "mediaType": "text/html",
+                    "title": "Streptococcus mutans differential gene expression in response to simulated microgravity"
+                }
+            ],
+            "identifier": "nasa_genelab_GLDS-106_bhd4-cidu",
             "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
             "keyword": [
                 "weightlessness simulation",
                 "sequence analysis data transformation",
@@ -534475,547 +534489,513 @@
                 "nucleic acid sequencing",
                 "nucleic acid extraction"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "GeneLab Outreach",
-                "hasEmail": "mailto:genelab-outreach@lists.nasa.gov"
-            },
+            "landingPage": "https://data.nasa.gov/d/bhd4-cidu",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "nasa_genelab_GLDS-106_bhd4-cidu",
-            "description": "Astronauts have been previously shown to exhibit decreased salivary lysozyme and increased dental calculus and gingival inflammation in response to space flight host factors that could contribute to oral diseases such as caries and periodontitis. However the specific physiological response of caries-causing bacteria such as Streptococcus mutans to space flight and/or ground-based simulated microgravity has not been extensively investigated. In this study High Aspect Ratio Vessel (HARV) S. mutans simulated microgravity and normal gravity cultures were assessed for changes in metabolite and transcriptome profiles H2O2 resistance and competence in sucrose-containing biofilm media. Stationary phase S. mutans simulated microgravity cultures displayed increased killing by H2O2 compared to normal gravity control cultures but competence was not affected. RNA-seq analysis revealed that expression of 153 genes was up-regulated >= 2-fold and 94 genes down-regulated >= 2-fold during simulated microgravity HARV growth. These included a number of genes located on extrachromosomal elements as well as genes involved in carbohydrate metabolism translation and stress responses. Collectively these results suggest that growth under microgravity analog conditions promotes changes in S. mutans gene expression and physiology that may translate to an altered cariogenic potential of this organism during space flight missions. Overall design: Differential gene expression was compared between RNA from S. mutans grown in normal gravity HARVs (n=3 independent cultures) and RNA from S. mutans grown in simulated microgravity HARVs (n=3 independent cultures)",
-            "title": "Streptococcus mutans differential gene expression in response to simulated microgravity",
-            "programCode": [
-                "026:005"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-106",
-                    "description": "GeneLab Study Page",
-                    "@type": "dcat:Distribution",
-                    "title": "Streptococcus mutans differential gene expression in response to simulated microgravity"
-                }
-            ],
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "Streptococcus mutans differential gene expression in response to simulated microgravity"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ECTSS-MAP4B",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "ECCO Consortium, Fukumori, I., Wang, O., Fenty, I., Forget, G., Heimbach, P., & Ponte, R. M.. 2021-10-01. ECCO Global Mean Atmospheric Pressure - Snapshot (Version 4 Release 4). Version V4r4. PO.DAAC. Archived by National Aeronautics and Space Administration, U.S. Government, PO.DAAC. https://doi.org/10.5067/ECTSS-MAP4B.",
-            "issued": "1992-01-01",
-            "temporal": "1992-01-01T00:00:00Z/2018-01-01T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2018-01-01",
-            "references": [
-                "https://doi.org/10.5281/zenodo.3765928"
-            ],
-            "keyword": [
-                "atmospheric pressure",
-                "atmosphere",
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
-            "identifier": "C2133160276-POCLOUD",
-            "description": "This dataset provides instantaneous hourly global mean atmospheric pressure from the ECCO Version 4 Release 4b (V4r4b) ocean and sea-ice state estimate. V4r4b is an errata for ECCO Version 4, Release 4 (V4r4). Estimating the Circulation and Climate of the Ocean (ECCO) ocean and sea-ice state estimates are dynamically and kinematically-consistent reconstructions of the three-dimensional time-evolving ocean, sea-ice, and surface atmospheric states. ECCO V4r4b is a free-running solution of the 1-degree global configuration of the MIT general circulation model (MITgcm) that has been fit to observations in a least-squares sense. Observational data constraints used in V4r4b include sea surface height and model sea level anomaly (SSH) from satellite altimeters [ERS-1/2, TOPEX/Poseidon, GFO, ENVISAT, Jason-1,2,3, CryoSat-2, and SARAL/AltiKa]; sea surface temperature (SST) from satellite radiometers [AVHRR], sea surface salinity (SSS) from the Aquarius satellite radiometer/scatterometer, ocean bottom pressure (OBP) from the GRACE satellite gravimeter; sea ice concentration from satellite radiometers [SSM/I and SSMIS], and in-situ ocean temperature and salinity measured with conductivity-temperature-depth (CTD) sensors and expendable bathythermographs (XBTs) from several programs [e.g., WOCE, GO-SHIP, Argo, and others] and platforms [e.g., research vessels, gliders, moorings, ice-tethered profilers, and instrumented pinnipeds]. V4r4b covers the period 1992-01-01T12:00:00 to 2018-01-01T00:00:00.",
-            "release-place": "PO.DAAC",
-            "graphic-preview-description": "Thumbnail",
             "creator": "ECCO Consortium, Fukumori, I., Wang, O., Fenty, I., Forget, G., Heimbach, P., & Ponte, R. M.",
-            "title": "ECCO Global Mean Atmospheric Pressure - Snapshot (Version 4 Release 4b)",
-            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/ECCO_L4_GMAP_TIME_SERIES_SNAPSHOT_V4R4.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "This dataset provides instantaneous hourly global mean atmospheric pressure from the ECCO Version 4 Release 4b (V4r4b) ocean and sea-ice state estimate. V4r4b is an errata for ECCO Version 4, Release 4 (V4r4). Estimating the Circulation and Climate of the Ocean (ECCO) ocean and sea-ice state estimates are dynamically and kinematically-consistent reconstructions of the three-dimensional time-evolving ocean, sea-ice, and surface atmospheric states. ECCO V4r4b is a free-running solution of the 1-degree global configuration of the MIT general circulation model (MITgcm) that has been fit to observations in a least-squares sense. Observational data constraints used in V4r4b include sea surface height and model sea level anomaly (SSH) from satellite altimeters [ERS-1/2, TOPEX/Poseidon, GFO, ENVISAT, Jason-1,2,3, CryoSat-2, and SARAL/AltiKa]; sea surface temperature (SST) from satellite radiometers [AVHRR], sea surface salinity (SSS) from the Aquarius satellite radiometer/scatterometer, ocean bottom pressure (OBP) from the GRACE satellite gravimeter; sea ice concentration from satellite radiometers [SSM/I and SSMIS], and in-situ ocean temperature and salinity measured with conductivity-temperature-depth (CTD) sensors and expendable bathythermographs (XBTs) from several programs [e.g., WOCE, GO-SHIP, Argo, and others] and platforms [e.g., research vessels, gliders, moorings, ice-tethered profilers, and instrumented pinnipeds]. V4r4b covers the period 1992-01-01T12:00:00 to 2018-01-01T00:00:00.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FECTSS-MAP4B",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FECTSS-MAP4B",
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
-                    "description": "The project website for the ECCO Consortium",
                     "@type": "dcat:Distribution",
+                    "description": "The project website for the ECCO Consortium",
+                    "downloadURL": "https://www.ecco-group.org",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://github.com/ECCO-GROUP/",
-                    "description": "Software maintained by ECCO Consortium on GitHub",
                     "@type": "dcat:Distribution",
+                    "description": "Software maintained by ECCO Consortium on GitHub",
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
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/web-misc/ecco/docs/v4r4_reproduction_howto.pdf",
-                    "description": "Instructions for reproducing ECCO Version 4 Release 4",
                     "@type": "dcat:Distribution",
+                    "description": "Instructions for reproducing ECCO Version 4 Release 4",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/web-misc/ecco/docs/v4r4_reproduction_howto.pdf",
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
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/web-misc/ecco/docs/v4r4_user_guide.pdf",
-                    "description": "ECCO Version 4 Release 4 User Guide",
                     "@type": "dcat:Distribution",
+                    "description": "ECCO Version 4 Release 4 User Guide",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/web-misc/ecco/docs/v4r4_user_guide.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/web-misc/ecco/docs/v4r4_synopsis.pdf",
-                    "description": "Synopsis of ECCO Version 4 Release 4",
                     "@type": "dcat:Distribution",
+                    "description": "Synopsis of ECCO Version 4 Release 4",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/web-misc/ecco/docs/v4r4_synopsis.pdf",
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
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/web-misc/ecco/docs/v4r4_overview_plots.pdf",
-                    "description": "Sample Plots -- gcmfaces analysis of ECCO V4, Release 4 (1992-2017)",
                     "@type": "dcat:Distribution",
+                    "description": "Sample Plots -- gcmfaces analysis of ECCO V4, Release 4 (1992-2017)",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/web-misc/ecco/docs/v4r4_overview_plots.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's product usage"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/ECCO_L4_GMAP_TIME_SERIES_SNAPSHOT_V4R4.jpg",
-                    "description": "Thumbnail",
                     "@type": "dcat:Distribution",
+                    "description": "Thumbnail",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/ECCO_L4_GMAP_TIME_SERIES_SNAPSHOT_V4R4.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/ECTSS-MAP4B",
-                    "description": "Access the data set landing page for the collection",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data set landing page for the collection",
+                    "downloadURL": "https://doi.org/10.5067/ECTSS-MAP4B",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2133160276-POCLOUD",
-                    "description": "Browse granule search results in Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse granule search results in Earthdata Search",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2133160276-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2133160276-POCLOUD",
-                    "description": "HTTPS endpoint for data browse and download",
                     "@type": "dcat:Distribution",
+                    "description": "HTTPS endpoint for data browse and download",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2133160276-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://ecco-group.org/docs/ECCO_V4r4_errata.pdf",
-                    "description": "ECCO V4r4b (V4r4 Errata) Document",
                     "@type": "dcat:Distribution",
+                    "description": "ECCO V4r4b (V4r4 Errata) Document",
+                    "downloadURL": "https://ecco-group.org/docs/ECCO_V4r4_errata.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View an important notice for this dataset"
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
+            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/ECCO_L4_GMAP_TIME_SERIES_SNAPSHOT_V4R4.jpg",
+            "identifier": "C2133160276-POCLOUD",
+            "issued": "1992-01-01",
+            "keyword": [
+                "atmospheric pressure",
+                "atmosphere",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/ECTSS-MAP4B",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2018-01-01",
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
+            "title": "ECCO Global Mean Atmospheric Pressure - Snapshot (Version 4 Release 4b)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-3-ESC3-67PCHURYUMOV-M20-V1.0",
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
+            "description": "This data set contains images acquired by the OSIRIS Narrow Angle Camera during the COMET ESCORT 3 phase of the Rosetta mission at the comet 67P, covering the period from 2015-08-25T23:25:00.000 to 2015-09-22T23:24:59.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-3-esc3-67pchuryumov-m20-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-3-ESC3-67PCHURYUMOV-M20-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-3-esc3-67pchuryumov-m20-v1.0",
-            "description": "This data set contains images acquired by the OSIRIS Narrow Angle Camera during the COMET ESCORT 3 phase of the Rosetta mission at the comet 67P, covering the period from 2015-08-25T23:25:00.000 to 2015-09-22T23:24:59.000.",
-            "title": "ROSETTA-ORBITER COMET ESCORT 3 OSINAC 3 RDR MTP020 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER COMET ESCORT 3 OSINAC 3 RDR MTP020 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/SSCH3-01XM1",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "GSFC/JPL. 1996-04-18. SEASAT SCATTEROMETER DERIVED GLOBAL GRIDDED MONTHLY OCEAN WIND STRESS (Chelton). Version 1. SEASAT SCATTEROMETER DERIVED GLOBAL GRIDDED MONTHLY OCEAN WIND STRESS (Chelton). PO.DAAC. Archived by National Aeronautics and Space Administration, U.S. Government, PO.DAAC. https://doi.org/10.5067/SSCH3-01XM1. https://podaac-tools.jpl.nasa.gov/drive/files/pub/documents/dataset_docs/seasat_chelton.html. GSFC/JPL, PO.DAAC, 1996-04-18, SEASAT SCATTEROMETER DERIVED GLOBAL GRIDDED MONTHLY OCEAN WIND STRESS (Chelton), https://podaac-tools.jpl.nasa.gov/drive/files/pub/documents/dataset_docs/seasat_chelton.html.",
-            "issued": "2009-06-15",
-            "temporal": "1978-07-07T00:00:00Z/1978-10-10T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2011-01-21",
-            "keyword": [
-                "ocean winds",
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
-            "identifier": "C2617197622-POCLOUD",
-            "description": "Contains monthly averaged ocean surface wind stress derived from Seasat-A Scatterometer (SASS) wind retrievals, from July 1978 until October 1978, gridded on a 2.5-degree by 2.5 degree global grid. The vector average wind stress is stored in units of dynes per centimeter squared (dyn/cm^2). Data is provided in formatted ASCII text. The primary data set used to construct these wind stress fields consists of 96 days of SASS vector winds supplied by Robert Atlas at GSFC. The directional ambiguities in the raw SASS data had been objectively removed using the GSFC Laboratory for Atmospheric Sciences atmospheric general circulation model.",
-            "release-place": "PO.DAAC",
-            "series-name": "SEASAT SCATTEROMETER DERIVED GLOBAL GRIDDED MONTHLY OCEAN WIND STRESS (Chelton)",
-            "graphic-preview-description": "Thumbnail",
             "creator": "GSFC/JPL",
-            "title": "SEASAT SCATTEROMETER DERIVED GLOBAL GRIDDED MONTHLY OCEAN WIND STRESS (Chelton)",
-            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/CHELTON_SEASAT_SASS_L3.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "Contains monthly averaged ocean surface wind stress derived from Seasat-A Scatterometer (SASS) wind retrievals, from July 1978 until October 1978, gridded on a 2.5-degree by 2.5 degree global grid. The vector average wind stress is stored in units of dynes per centimeter squared (dyn/cm^2). Data is provided in formatted ASCII text. The primary data set used to construct these wind stress fields consists of 96 days of SASS vector winds supplied by Robert Atlas at GSFC. The directional ambiguities in the raw SASS data had been objectively removed using the GSFC Laboratory for Atmospheric Sciences atmospheric general circulation model.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSSCH3-01XM1",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSSCH3-01XM1",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/CHELTON_SEASAT_SASS_L3.jpg",
-                    "description": "Thumbnail",
                     "@type": "dcat:Distribution",
+                    "description": "Thumbnail",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/CHELTON_SEASAT_SASS_L3.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://podaac-tools.jpl.nasa.gov/drive/files/pub/documents/dataset_docs/seasat_chelton.html",
-                    "description": "Dataset User Guide",
                     "@type": "dcat:Distribution",
+                    "description": "Dataset User Guide",
+                    "downloadURL": "https://podaac-tools.jpl.nasa.gov/drive/files/pub/documents/dataset_docs/seasat_chelton.html",
+                    "mediaType": "text/html",
                     "title": "View this dataset's user's guide"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/seasat/open/L3/sass_monthly_Chelton/docs/README",
-                    "description": "PO.DAAC Drive",
                     "@type": "dcat:Distribution",
+                    "description": "PO.DAAC Drive",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/seasat/open/L3/sass_monthly_Chelton/docs/README",
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
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2617197622-POCLOUD",
-                    "description": "HTTPS endpoint for data browse and download",
                     "@type": "dcat:Distribution",
+                    "description": "HTTPS endpoint for data browse and download",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2617197622-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2617197622-POCLOUD",
-                    "description": "Browse granule search results in Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse granule search results in Earthdata Search",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2617197622-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 }
             ],
+            "graphic-preview-description": "Thumbnail",
+            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/CHELTON_SEASAT_SASS_L3.jpg",
+            "identifier": "C2617197622-POCLOUD",
+            "issued": "2009-06-15",
+            "keyword": [
+                "ocean winds",
+                "earth science",
+                "oceans"
+            ],
+            "landingPage": "https://doi.org/10.5067/SSCH3-01XM1",
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
+            "series-name": "SEASAT SCATTEROMETER DERIVED GLOBAL GRIDDED MONTHLY OCEAN WIND STRESS (Chelton)",
             "spatial": "-180.0 -70.0 180.0 70.0",
+            "temporal": "1978-07-07T00:00:00Z/1978-10-10T23:59:59.999Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "SEASAT SCATTEROMETER DERIVED GLOBAL GRIDDED MONTHLY OCEAN WIND STRESS (Chelton)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://c3.nasa.gov/dashlink/resources/870/",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2013-12-19",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
-            "keyword": [
-                "dashlink",
-                "nasa",
-                "ames"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "SCOTT POLL",
                 "hasEmail": "mailto:scott.d.poll@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Dashlink"
-            },
-            "identifier": "DASHLINK_870",
             "description": "This paper presents a new sensing application\r\nto diagnose power semiconductor aging in power drive\r\nsystems. It has been shown previously that device\r\nparasitic characteristics change during the aging process\r\nwhich results in detectable changes in their frequency\r\nresponse. This change is manifested in the current signal\r\nat very high frequencies. Therefore, using a wideband\r\nAC current sensor, high frequency components of the\r\ncurrent can be acquired, providing a way to detect\r\ndevice aging.",
-            "title": "New Sensing Application to Diagnose Power Semiconductor Aging in Actuator Power Drive Systems",
-            "programCode": [
-                "026:029"
-            ],
             "distribution": [
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/publication/2012IEEE_Ali_NewSensingPowerSemiconductor.pdf",
-                    "description": "2012IEEE_Ali_NewSensingPowerSemiconductor.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "2012IEEE_Ali_NewSensingPowerSemiconductor.pdf",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/publication/2012IEEE_Ali_NewSensingPowerSemiconductor.pdf",
+                    "mediaType": "application/pdf",
                     "title": "2012IEEE_Ali_NewSensingPowerSemiconductor.pdf"
                 }
             ],
-            "accrualPeriodicity": "irregular"
+            "identifier": "DASHLINK_870",
+            "issued": "2013-12-19",
+            "keyword": [
+                "dashlink",
+                "nasa",
+                "ames"
+            ],
+            "landingPage": "https://c3.nasa.gov/dashlink/resources/870/",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:029"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Dashlink"
+            },
+            "title": "New Sensing Application to Diagnose Power Semiconductor Aging in Actuator Power Drive Systems"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/MODIS/MYD21A1N.061",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Glynn Hulley. 2021-02-08. MODIS/Aqua Land Surface Temperature/3-Band Emissivity Daily L3 Global 1km SIN Grid Night V061. Sioux Falls, South Dakota, USA. Archived by National Aeronautics and Space Administration, U.S. Government, NASA EOSDIS Land Processes Distributed Active Archive Center. https://doi.org/10.5067/MODIS/MYD21A1N.061. https://doi.org/10.5067/MODIS/MYD21A1N.061. The DOI landing page provides citations in APA and Chicago styles..",
-            "issued": "2021-02-08",
-            "temporal": "2002-07-04T00:00:00Z/2024-06-03T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2021-02-08",
-            "keyword": [
-                "national geospatial data asset",
-                "land surface",
-                "surface thermal properties",
-                "surface radiative properties",
-                "ngda",
-                "earth science"
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
-            "identifier": "C2565805789-LPCLOUD",
-            "description": "A suite of Moderate Resolution Imaging Spectroradiometer (MODIS) Land Surface Temperature and Emissivity (LST&E) products are available in Collection 6.1. The MYD21 Land Surface Temperature (LST) algorithm differs from the algorithm of the MYD11 (https://doi.org/10.5067/modis/myd11_l2.061) LST products, in that the MYD21 algorithm is based on the ASTER Temperature/Emissivity Separation (TES) technique, whereas the MYD11 uses the split-window technique. The MYD21 TES algorithm uses a physics-based algorithm to dynamically retrieve both the LST and spectral emissivity simultaneously from the MODIS thermal infrared bands 29, 31, and 32. The TES algorithm is combined with an improved Water Vapor Scaling (WVS) atmospheric correction scheme to stabilize the retrieval during very warm and humid conditions. \n\nThe MYD21A1N dataset is produced daily from nighttime Level 2 Gridded (L2G) intermediate LST products. The L2G process maps the daily MYD21 (https://doi.org/10.5067/MODIS/MYD21.061) swath granules onto a sinusoidal MODIS grid and stores all observations falling over a gridded cell for a given day. The MOD21A1 algorithm sorts through all these observations for each cell and estimates the final LST value as an average from all observations that are cloud free and have good LST&E accuracies. The nighttime average is weighted by the observation coverage for that cell. Only observations having an observation coverage greater than a 15% threshold are considered. The MYD21A1N product contains seven Science Datasets (SDS), which include the calculated LST as well as quality control, the three emissivity bands, view zenith angle, and time of observation. Additional details regarding the methodology used to create this Level 3 (L3) product are available in the Algorithm Theoretical Basis Document (ATBD (https://lpdaac.usgs.gov/documents/1399/MOD21_ATBD.pdf)).\n\nValidation at stage 1 (https://modis-land.gsfc.nasa.gov/MODLAND_val.html) has been achieved for the MODIS Land Surface Temperature and Emissivity data products. Further details regarding MODIS land product validation for the MYD21 data products are available from the MODIS Land Team Validation site (https://modis-land.gsfc.nasa.gov/ValStatus.php?ProductID=MOD21).\n\nImprovements/Changes from Previous Versions\n* The Version 6.1 Level-1B (L1B) products have been improved by undergoing various calibration changes that include: changes to the response-versus-scan angle (RVS) approach that affects reflectance bands for Aqua and Terra MODIS, corrections to adjust for the optical crosstalk in Terra MODIS infrared (IR) bands, and corrections to the Terra MODIS forward look-up table (LUT) update for the period 2012 - 2017.\n* A polarization correction has been applied to the L1B Reflective Solar Bands (RSB).\n* The product utilizes GEOS data replacing MERRA2.\n* Three new CMG products are available in the MxD21 suite (MxD21C1/C2/C3).",
-            "release-place": "Sioux Falls, South Dakota, USA",
-            "graphic-preview-description": "Browse image for Earthdata Search",
             "creator": "Glynn Hulley",
-            "title": "MODIS/Aqua Land Surface Temperature/3-Band Emissivity Daily L3 Global 1km SIN Grid Night V061",
-            "graphic-preview-file": "https://cmr.earthdata.nasa.gov/browse-scaler/browse_images/granules/G2681480198-LPCLOUD?h=85&w=85",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "A suite of Moderate Resolution Imaging Spectroradiometer (MODIS) Land Surface Temperature and Emissivity (LST&E) products are available in Collection 6.1. The MYD21 Land Surface Temperature (LST) algorithm differs from the algorithm of the MYD11 (https://doi.org/10.5067/modis/myd11_l2.061) LST products, in that the MYD21 algorithm is based on the ASTER Temperature/Emissivity Separation (TES) technique, whereas the MYD11 uses the split-window technique. The MYD21 TES algorithm uses a physics-based algorithm to dynamically retrieve both the LST and spectral emissivity simultaneously from the MODIS thermal infrared bands 29, 31, and 32. The TES algorithm is combined with an improved Water Vapor Scaling (WVS) atmospheric correction scheme to stabilize the retrieval during very warm and humid conditions. \n\nThe MYD21A1N dataset is produced daily from nighttime Level 2 Gridded (L2G) intermediate LST products. The L2G process maps the daily MYD21 (https://doi.org/10.5067/MODIS/MYD21.061) swath granules onto a sinusoidal MODIS grid and stores all observations falling over a gridded cell for a given day. The MOD21A1 algorithm sorts through all these observations for each cell and estimates the final LST value as an average from all observations that are cloud free and have good LST&E accuracies. The nighttime average is weighted by the observation coverage for that cell. Only observations having an observation coverage greater than a 15% threshold are considered. The MYD21A1N product contains seven Science Datasets (SDS), which include the calculated LST as well as quality control, the three emissivity bands, view zenith angle, and time of observation. Additional details regarding the methodology used to create this Level 3 (L3) product are available in the Algorithm Theoretical Basis Document (ATBD (https://lpdaac.usgs.gov/documents/1399/MOD21_ATBD.pdf)).\n\nValidation at stage 1 (https://modis-land.gsfc.nasa.gov/MODLAND_val.html) has been achieved for the MODIS Land Surface Temperature and Emissivity data products. Further details regarding MODIS land product validation for the MYD21 data products are available from the MODIS Land Team Validation site (https://modis-land.gsfc.nasa.gov/ValStatus.php?ProductID=MOD21).\n\nImprovements/Changes from Previous Versions\n* The Version 6.1 Level-1B (L1B) products have been improved by undergoing various calibration changes that include: changes to the response-versus-scan angle (RVS) approach that affects reflectance bands for Aqua and Terra MODIS, corrections to adjust for the optical crosstalk in Terra MODIS infrared (IR) bands, and corrections to the Terra MODIS forward look-up table (LUT) update for the period 2012 - 2017.\n* A polarization correction has been applied to the L1B Reflective Solar Bands (RSB).\n* The product utilizes GEOS data replacing MERRA2.\n* Three new CMG products are available in the MxD21 suite (MxD21C1/C2/C3).",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMODIS%2FMYD21A1N.061",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMODIS%2FMYD21A1N.061",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "application/x-hdf",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=C2565805789-LPCLOUD",
-                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=C2565805789-LPCLOUD",
+                    "mediaType": "application/x-hdf",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "application/x-hdf",
-                    "downloadURL": "https://e4ftl01.cr.usgs.gov/MOLA/MYD21A1N.061/",
-                    "description": "LP DAAC Data Pool provides direct access to available products via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "LP DAAC Data Pool provides direct access to available products via HTTPS.",
+                    "downloadURL": "https://e4ftl01.cr.usgs.gov/MOLA/MYD21A1N.061/",
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
-                    "downloadURL": "https://doi.org/10.5067/MODIS/MYD21A1N.061",
-                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
+                    "downloadURL": "https://doi.org/10.5067/MODIS/MYD21A1N.061",
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
-                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/filespec/MODIS/6/MYD21A1N",
-                    "description": "The File Specification provides a description of the product file including Scientific Data Sets and their attributes.",
                     "@type": "dcat:Distribution",
+                    "description": "The File Specification provides a description of the product file including Scientific Data Sets and their attributes.",
+                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/filespec/MODIS/6/MYD21A1N",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://opendap.cr.usgs.gov/opendap/hyrax/DP130/MOLA/MYD21A1N.061/contents.html",
-                    "description": "OPeNDAP provides direct access to data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "OPeNDAP provides direct access to data via HTTPS.",
+                    "downloadURL": "https://opendap.cr.usgs.gov/opendap/hyrax/DP130/MOLA/MYD21A1N.061/contents.html",
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
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/browse-scaler/browse_images/granules/G2681480198-LPCLOUD?h=85&w=85",
-                    "description": "Browse image for Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse image for Earthdata Search",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/browse-scaler/browse_images/granules/G2681480198-LPCLOUD?h=85&w=85",
+                    "mediaType": "text/html",
                     "title": "Get a related visualization"
                 }
             ],
+            "graphic-preview-description": "Browse image for Earthdata Search",
+            "graphic-preview-file": "https://cmr.earthdata.nasa.gov/browse-scaler/browse_images/granules/G2681480198-LPCLOUD?h=85&w=85",
+            "identifier": "C2565805789-LPCLOUD",
+            "issued": "2021-02-08",
+            "keyword": [
+                "national geospatial data asset",
+                "land surface",
+                "surface thermal properties",
+                "surface radiative properties",
+                "ngda",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/MODIS/MYD21A1N.061",
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
+            "title": "MODIS/Aqua Land Surface Temperature/3-Band Emissivity Daily L3 Global 1km SIN Grid Night V061"
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
-            "identifier": "NASA-657",
             "description": "Data Dictionary and Index Files",
-            "title": "PDS Data Dictionary (1r54)",
-            "programCode": [
-                "026:005"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -535023,645 +535003,640 @@
                     "mediaType": "application/html"
                 }
             ],
-            "accrualPeriodicity": "irregular",
+            "identifier": "NASA-657",
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
+            "title": "PDS Data Dictionary (1r54)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/843",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Schroeder, W., J.T. Morisette, I.A. Csiszar, L. Giglio, D.C. Morton, and C.O. Justice. 2006. LBA-ECO LC-23 Characterization of Vegetation Fire Dynamics for Brazil: 2001-2003. ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/843",
-            "issued": "2023-10-15",
-            "temporal": "2001-01-01T00:00:00Z/2003-12-31T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-10-17",
-            "keyword": [
-                "surface radiative properties",
-                "human dimensions",
-                "earth science",
-                "natural hazards",
-                "ngda",
-                "biosphere",
-                "ecological dynamics",
-                "land surface",
-                "national geospatial data asset"
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
-            "identifier": "C2784831948-ORNL_CLOUD",
             "description": "Satellite fire detection was determined from two sensors, the Advanced Very High Resolution Radiometer (AVHRR) on NOAA-12 and the Moderate Resolution Imaging Spectroradiometer (MODIS) on both the Terra and Aqua platforms, for 2001- 2003 to characterize fire activity in Brazil, giving special emphasis to the Amazon region. Active fire data for AVHRR/NOAA-12 was produced using a fixed threshold fire detection technique based on the algorithm developed by the Centro de Previsao do Tempo e Estudos Climaticos (CPTEC/INPE) (Setzer and Pereira, 1991; Setzer et al., 1994; Setzer and Malingreau, 1996). Active fire data for MODIS/Terra and MODIS/Aqua was produced using a contextual fire detection technique based on NASA-University of Maryland algorithm (Justice et al., 2003; Giglio et al.2003).Resulting fire counts were compared for major biomes of Brazil (Figure 1), the nine states of the Legal Amazon (e.g., Tocantins, Figure 2), and two important road corridors in the Amazon region (Figure 3). In evaluating the daily fire counts, there is a dependence on variations in satellite viewing geometry, overpass time, atmospheric conditions, and fire characteristics (Schroeder et al., 2005). The data provided are the coordinates of daily active vegetation fires in Brazil for 2001 through 2003 at 1km resolution for both AVHRR and MODIS sensors.  Data are provided in both Arcview (shape file format) and ASCII comma separated file formats. Vector files for the major biomes of Brazil, the nine states of the Legal Amazon, and two important road corridors in the Amazon region are also included.",
-            "graphic-preview-description": "Browse Image",
-            "title": "LBA-ECO LC-23 Characterization of Vegetation Fire Dynamics for Brazil: 2001-2003",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/lba_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F843",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F843",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/lba/land_use_land_cover_change/LC23_Vegetation_Fire_Dynamics/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/lba/land_use_land_cover_change/LC23_Vegetation_Fire_Dynamics/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/LBA/guides/LC23_Vegetation_Fire_Dynamics.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/LBA/guides/LC23_Vegetation_Fire_Dynamics.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/843",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/843",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC23_Vegetation_Fire_Dynamics/comp/LC23_Vegetation_Fire_Dynamics.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC23_Vegetation_Fire_Dynamics/comp/LC23_Vegetation_Fire_Dynamics.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC23_Vegetation_Fire_Dynamics/comp/LC23_Veg_Biomes_Brazil.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC23_Vegetation_Fire_Dynamics/comp/LC23_Veg_Biomes_Brazil.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC23_Vegetation_Fire_Dynamics/comp/readme_aqua.txt",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC23_Vegetation_Fire_Dynamics/comp/readme_aqua.txt",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC23_Vegetation_Fire_Dynamics/comp/readme_noaa.txt",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC23_Vegetation_Fire_Dynamics/comp/readme_noaa.txt",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC23_Vegetation_Fire_Dynamics/comp/readme_terra.txt",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC23_Vegetation_Fire_Dynamics/comp/readme_terra.txt",
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
+            "identifier": "C2784831948-ORNL_CLOUD",
+            "issued": "2023-10-15",
+            "keyword": [
+                "surface radiative properties",
+                "human dimensions",
+                "earth science",
+                "natural hazards",
+                "ngda",
+                "biosphere",
+                "ecological dynamics",
+                "land surface",
+                "national geospatial data asset"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/843",
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
             "spatial": "-74.0 -33.75 -34.8 5.3",
+            "temporal": "2001-01-01T00:00:00Z/2003-12-31T23:59:59Z",
             "theme": [
                 "LBA-ECO",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "LBA-ECO LC-23 Characterization of Vegetation Fire Dynamics for Brazil: 2001-2003"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=GO-J-UVS-3-RDR-SL9-G-FRAGMENT-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "The UltraViolet Spectrometer (UVS) on the Galileo spacecraft took unique data of Comet Shoemaker-Levy/9's impact with Jupiter. A preliminary analysis of this data is presented in this submission to the Planetary Data System (PDS). It consists of four small tables with detached labels and documentation.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.go-j-uvs-3-rdr-sl9-g-fragment-v1.0_bhj5-mqx7",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "jupiter",
                 "sl9",
                 "galileo",
                 "comet sl9/jupiter collision"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=GO-J-UVS-3-RDR-SL9-G-FRAGMENT-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.go-j-uvs-3-rdr-sl9-g-fragment-v1.0_bhj5-mqx7",
-            "description": "The UltraViolet Spectrometer (UVS) on the Galileo spacecraft took unique data of Comet Shoemaker-Levy/9's impact with Jupiter. A preliminary analysis of this data is presented in this submission to the Planetary Data System (PDS). It consists of four small tables with detached labels and documentation.",
-            "title": "GO UVS TABULAR DATA FROM THE SL9-G IMPACT WITH JUPITER V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "GO UVS TABULAR DATA FROM THE SL9-G IMPACT WITH JUPITER V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/2096",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Hook, S.J., J.S. Myers, K.J. Thome, M. Fitzgerald, A.B. Kahle,  Airborne Sensor Facility NASA Ames Research Center, F.D. Palluconi, E.A. Abbott, A. Gillespie, J.P. Schieldge, P.R. Christensen, T.J. Schmugge, and J.C. Ritchie. 2022. MASTER: Airborne Science, southwestern US, June, 2000. ORNL DAAC, Oak Ridge, Tennessee, USA. https://doi.org/10.3334/ORNLDAAC/2096",
-            "issued": "2023-06-29",
-            "temporal": "2000-06-01T23:02:10Z/2000-06-17T22:26:31Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-13",
-            "keyword": [
-                "infrared wavelengths",
-                "visible wavelengths",
-                "spectral/engineering",
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
-            "identifier": "C2731772359-ORNL_CLOUD",
             "description": "This dataset includes Level 1B (L1B) data products from the MODIS/ASTER Airborne Simulator (MASTER) instrument. The spectral data were collected during 12 flights aboard a DOE B-200 aircraft over California, Nevada, Arizona, and New Mexico, U.S., on 2000-06-01 to 2000-06-17. This deployment was coordinated by the U.S. Department of Energy's Remote Sensing Laboratory (RSL) located at Nellis Air Force Base near Las Vegas, Nevada. Data products include L1B georeferenced multispectral imagery of calibrated radiance in 50 bands covering wavelengths of 0.460 to 12.879 micrometers at approximately 20-meter spatial resolution. The L1B file format is HDF-4. In addition, the dataset includes flight paths, spectral band information, instrument configuration, ancillary notes, and summary information for each flight, and browse images derived from each L1B data file.",
-            "graphic-preview-description": "Single-band images and a RGB composite image from flight track 4 acquired on 02 June 2000 over Mono Lake near Lee Vining, California, U.S. Source: MASTERL1B_0000202_04_20000602_1929_1931_V01.jpg",
-            "title": "MASTER: Airborne Science, southwestern US, June, 2000",
-            "graphic-preview-file": "https://daac.ornl.gov/MASTER/guides/MASTER_RSL_June_2000_Fig1.jpg",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F2096",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F2096",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/master/MASTER_RSL_June_2000/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/master/MASTER_RSL_June_2000/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/MASTER/guides/MASTER_RSL_June_2000.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/MASTER/guides/MASTER_RSL_June_2000.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/2096",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/2096",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/master/MASTER_RSL_June_2000/comp/MASTER_RSL_June_2000.pdf",
-                    "description": "MASTER: Airborne Science, southwestern US, June, 2000: MASTER_RSL_June_2000.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "MASTER: Airborne Science, southwestern US, June, 2000: MASTER_RSL_June_2000.pdf",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/master/MASTER_RSL_June_2000/comp/MASTER_RSL_June_2000.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://daac.ornl.gov/MASTER/guides/MASTER_RSL_June_2000_Fig1.jpg",
-                    "description": "Single-band images and a RGB composite image from flight track 4 acquired on 02 June 2000 over Mono Lake near Lee Vining, California, U.S. Source: MASTERL1B_0000202_04_20000602_1929_1931_V01.jpg",
                     "@type": "dcat:Distribution",
+                    "description": "Single-band images and a RGB composite image from flight track 4 acquired on 02 June 2000 over Mono Lake near Lee Vining, California, U.S. Source: MASTERL1B_0000202_04_20000602_1929_1931_V01.jpg",
+                    "downloadURL": "https://daac.ornl.gov/MASTER/guides/MASTER_RSL_June_2000_Fig1.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 }
             ],
+            "graphic-preview-description": "Single-band images and a RGB composite image from flight track 4 acquired on 02 June 2000 over Mono Lake near Lee Vining, California, U.S. Source: MASTERL1B_0000202_04_20000602_1929_1931_V01.jpg",
+            "graphic-preview-file": "https://daac.ornl.gov/MASTER/guides/MASTER_RSL_June_2000_Fig1.jpg",
+            "identifier": "C2731772359-ORNL_CLOUD",
+            "issued": "2023-06-29",
+            "keyword": [
+                "infrared wavelengths",
+                "visible wavelengths",
+                "spectral/engineering",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/2096",
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
             "spatial": "-120.31 31.28 -106.01 39.43",
+            "temporal": "2000-06-01T23:02:10Z/2000-06-17T22:26:31Z",
             "theme": [
                 "MASTER",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "MASTER: Airborne Science, southwestern US, June, 2000"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ASDC_DAAC/FIRE/0119",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2000-04-07. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/ASDC_DAAC/FIRE/0119.",
-            "issued": "2000-03-17",
-            "temporal": "1991-11-21T00:00:00Z/1991-12-06T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2018-07-12",
-            "keyword": [
-                "atmosphere",
-                "aerosols",
-                "earth science"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "KENNETH SASSEN",
                 "hasEmail": "mailto:ksassen@gi.alaska.edu"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/LARC/SD/ASDC"
-            },
-            "identifier": "C1000001172-LARC_ASDC",
             "description": "The First ISCCP Regional Experiments have been designed to improve data products and cloud/radiation parameterizations used in general circulation models (GCMs). Specifically, the goals of FIRE are (1) to seek the basic understanding of the interaction of physical processes in determining life cycles of cirrus and marine stratocumulus systems and the radiative properties of these clouds during their life cycles and (2) to investigate the interrelationships between ISCCP data, GCM parameterizations, and higher space and time resolution cloud data. To-date, four intensive field-observation periods were planned and executed: a cirrus IFO (October 13 - November 2, 1986); a marine stratocumulus IFO off the southwestern coast of California (June 29 - July 20, 1987); a second cirrus IFO in southeastern Kansas (November 13 - December 7, 1991); and a second marine stratocumulus IFO in the eastern North Atlantic Ocean (June 1 - June 28, 1992). Each mission combined coordinated satellite, airborne, and surface observations with modeling studies to investigate the cloud properties and physical processes of the cloud systems.Lidar returned signal in arbitrary units, raw data, background subtracted, Minimum value = 0, Maximum value = 25600, Scaling Factor = 100 A description of the lidar is given in the following paper: Sassen, K., 1994: Advances in polarization diversity lidar for cloud remote sensing, Proc. IEEE, 82, 1907-1914",
-            "title": "First ISCCP Regional Experiment (FIRE) Cirrus Phase II University of Utah Polar Diversification LIDAR",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC_DAAC%2FFIRE%2F0119",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC_DAAC%2FFIRE%2F0119",
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
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1000001172-LARC_ASDC",
-                    "description": "Earthdata Search for FIRE_CI2_UTAH_PDL_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for FIRE_CI2_UTAH_PDL_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1000001172-LARC_ASDC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/readme/readme_fire_ci2_utah_pdl_data_log.txt",
-                    "description": "FIRE CI2 Utah PDL Data Log Table",
                     "@type": "dcat:Distribution",
+                    "description": "FIRE CI2 Utah PDL Data Log Table",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/readme/readme_fire_ci2_utah_pdl_data_log.txt",
+                    "mediaType": "text/html",
                     "title": "Access to this dataset's extended metadata"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/ASDC_DAAC/FIRE/0119",
-                    "description": "DOI data set landing page for FIRE_CI2_UTAH_PDL_1",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for FIRE_CI2_UTAH_PDL_1",
+                    "downloadURL": "https://doi.org/10.5067/ASDC_DAAC/FIRE/0119",
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
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/fire3_ace/ACEDOCS/index.pdf",
-                    "description": "FIRE Arctic Cloud Experiment (FIRE.ACE) Home Page Document",
                     "@type": "dcat:Distribution",
+                    "description": "FIRE Arctic Cloud Experiment (FIRE.ACE) Home Page Document",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/fire3_ace/ACEDOCS/index.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
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
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/FIRE_III.tar",
-                    "description": "FIRE III Read Software Package - Direct File Download (.tar)",
                     "@type": "dcat:Distribution",
+                    "description": "FIRE III Read Software Package - Direct File Download (.tar)",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/FIRE_III.tar",
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
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/FIRE/FIRE_CI2_UTAH_PDL/",
-                    "description": "ASDC Direct Data Download for FIRE_CI2_UTAH_PDL_1",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for FIRE_CI2_UTAH_PDL_1",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/FIRE/FIRE_CI2_UTAH_PDL/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/FIRE/FIRE_CI2_UTAH_PDL/contents.html",
-                    "description": "OPeNDAP data access for FIRE_CI2_UTAH_PDL_1",
                     "@type": "dcat:Distribution",
+                    "description": "OPeNDAP data access for FIRE_CI2_UTAH_PDL_1",
+                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/FIRE/FIRE_CI2_UTAH_PDL/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 }
             ],
+            "identifier": "C1000001172-LARC_ASDC",
+            "issued": "2000-03-17",
+            "keyword": [
+                "atmosphere",
+                "aerosols",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/ASDC_DAAC/FIRE/0119",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2018-07-12",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/LARC/SD/ASDC"
+            },
             "spatial": "37.06 -95.24",
+            "temporal": "1991-11-21T00:00:00Z/1991-12-06T23:59:59.999Z",
             "theme": [
                 "FIRE",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "First ISCCP Regional Experiment (FIRE) Cirrus Phase II University of Utah Polar Diversification LIDAR"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC4-1260-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 4 phase 2015-10-22 to 2015-12-31. It is a Global Gravity measurement at the comet 67P and covers the time 2015-12-15T10:11:00.000 to 2015-12-15T15:51:40.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc4-1260-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC4-1260-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc4-1260-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 4 phase 2015-10-22 to 2015-12-31. It is a Global Gravity measurement at the comet 67P and covers the time 2015-12-15T10:11:00.000 to 2015-12-15T15:51:40.000.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 4 1260 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 4 1260 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/GFOCN-3G634",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Felix Landerer. 2023-02-21. GFZTELLUS GRACE-FO Level-3 Monthly Ocean Bottom Pressure Anomaly. Version RL06.3v04. GFZ TELLUS GRACE-FO Level-3 Monthly Ocean Bottom Pressure Anomaly Release 6.3 version 04. JPL. Archived by National Aeronautics and Space Administration, U.S. Government, PO.DAAC. https://doi.org/10.5067/GFOCN-3G634.",
-            "issued": "2021-03-10",
-            "temporal": "2018-05-22T00:00:00Z/2024-10-21T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2021-03-10",
-            "keyword": [
-                "ocean pressure",
-                "earth science",
-                "oceans"
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
-            "identifier": "C3193298027-POCLOUD",
-            "description": "This data set is produced by the German Research Centre for Geosciences (GFZ) as part of the GRACE-FO (Gravity Recovery and Climate Experiment Follow-On) program and derives the ocean bottom pressure (OBP) anomaly given as equivalent water thickness. These monthly grids are derived from GRACE-FO time-variable gravity observations during the specified timespan, and relative to the specified time-mean reference period. This quantity represents sea floor pressure changes due to the integral effect of ocean and atmosphere processes, including global mean ocean bottom pressure changes (mean ocean mass and mean atmosphere mass over the global oceans). A glacial isostatic adjustment (GIA) correction has been applied, and standard corrections for geocenter (degree-1), C20 (degree-20) and C30 (degree-30) are incorporated. Post-processing filters have been applied to reduce correlated errors. Data grids are provided in ASCII/netCDF/GeoTIFF formats. \n<br><br>\nGRACE-FO was launched on 22 May 2018, and extends the original GRACE mission (2002 \u2013 2017) and expands its legacy of scientific achievements in tracking earth surface mass changes. Version 04 (v04) of the ocean bottom pressure data uses updated and consistent C20 and Geocenter corrections (i.e., Technical Notes TN-14 and TN-13), as well as an ellipsoidal correction to account for the non-spherical shape of the Earth when mapping gravity anomalies to surface mass change. Additionally, this release 06.3 is an updated version of the Level 3 products in coordination with the release of the analogous Level 2 products used to generate them. It differs from RL06.1 only in the Level-1B accelerometer transplant data that is used for the GF2 (GRACE-FO 2) satellite; see respective L-2 data descriptions. RL06.3 uses the ACX2-L1B data products. All GRACE-FO RL06.3 Level-3 fields are fully compatible with the GRACE RL06 data.",
-            "release-place": "JPL",
-            "series-name": "GFZTELLUS GRACE-FO Level-3 Monthly Ocean Bottom Pressure Anomaly",
-            "graphic-preview-description": "Thumbnail",
             "creator": "Felix Landerer",
-            "title": "GFZ TELLUS GRACE-FO Level-3 Monthly Ocean Bottom Pressure Anomaly Release 6.3 version 04",
-            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/TELLUS_GRFO_L3_GFZ_RL063_OCN_v04.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "This data set is produced by the German Research Centre for Geosciences (GFZ) as part of the GRACE-FO (Gravity Recovery and Climate Experiment Follow-On) program and derives the ocean bottom pressure (OBP) anomaly given as equivalent water thickness. These monthly grids are derived from GRACE-FO time-variable gravity observations during the specified timespan, and relative to the specified time-mean reference period. This quantity represents sea floor pressure changes due to the integral effect of ocean and atmosphere processes, including global mean ocean bottom pressure changes (mean ocean mass and mean atmosphere mass over the global oceans). A glacial isostatic adjustment (GIA) correction has been applied, and standard corrections for geocenter (degree-1), C20 (degree-20) and C30 (degree-30) are incorporated. Post-processing filters have been applied to reduce correlated errors. Data grids are provided in ASCII/netCDF/GeoTIFF formats. \n<br><br>\nGRACE-FO was launched on 22 May 2018, and extends the original GRACE mission (2002 \u2013 2017) and expands its legacy of scientific achievements in tracking earth surface mass changes. Version 04 (v04) of the ocean bottom pressure data uses updated and consistent C20 and Geocenter corrections (i.e., Technical Notes TN-14 and TN-13), as well as an ellipsoidal correction to account for the non-spherical shape of the Earth when mapping gravity anomalies to surface mass change. Additionally, this release 06.3 is an updated version of the Level 3 products in coordination with the release of the analogous Level 2 products used to generate them. It differs from RL06.1 only in the Level-1B accelerometer transplant data that is used for the GF2 (GRACE-FO 2) satellite; see respective L-2 data descriptions. RL06.3 uses the ACX2-L1B data products. All GRACE-FO RL06.3 Level-3 fields are fully compatible with the GRACE RL06 data.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGFOCN-3G634",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGFOCN-3G634",
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
-                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/TELLUS_GRFO_L3_GFZ_RL063_OCN_v04.jpg",
-                    "description": "Thumbnail",
                     "@type": "dcat:Distribution",
+                    "description": "Thumbnail",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/TELLUS_GRFO_L3_GFZ_RL063_OCN_v04.jpg",
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
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C3193298027-POCLOUD",
-                    "description": "HTTPS endpoint for data browse and download",
                     "@type": "dcat:Distribution",
+                    "description": "HTTPS endpoint for data browse and download",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C3193298027-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C3193298027-POCLOUD",
-                    "description": "Browse granule search results in Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse granule search results in Earthdata Search",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C3193298027-POCLOUD",
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
+            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/TELLUS_GRFO_L3_GFZ_RL063_OCN_v04.jpg",
+            "identifier": "C3193298027-POCLOUD",
+            "issued": "2021-03-10",
+            "keyword": [
+                "ocean pressure",
+                "earth science",
+                "oceans"
+            ],
+            "landingPage": "https://doi.org/10.5067/GFOCN-3G634",
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
+            "series-name": "GFZTELLUS GRACE-FO Level-3 Monthly Ocean Bottom Pressure Anomaly",
             "spatial": "-180.0 -89.5 180.0 89.5",
+            "temporal": "2018-05-22T00:00:00Z/2024-10-21T00:00:00Z",
             "theme": [
                 "GRACE-FO",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "GFZ TELLUS GRACE-FO Level-3 Monthly Ocean Bottom Pressure Anomaly Release 6.3 version 04"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/XO2LBBNPO010",
             "citation": "OCO-2 Science Team/Michael Gunson, Annmarie Eldering. 2020-08-10. OCO2_L2_Lite_SIF. Version 10r. OCO-2 Level 2 bias-corrected solar-induced fluorescence and other select fields from the IMAP-DOAS algorithm aggregated as daily files, Retrospective processing V10r. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/XO2LBBNPO010. https://disc.gsfc.nasa.gov/datacollection/OCO2_L2_Lite_SIF_10r.html. Digital Science Data.",
-            "issued": "2020-08-01",
-            "temporal": "2014-09-06T00:00:00Z/2022-01-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-08-10",
-            "keyword": [
-                "biosphere",
-                "atmosphere",
-                "atmospheric chemistry",
-                "earth science",
-                "vegetation"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "THOMAS HEARTY",
                 "hasEmail": "mailto:Thomas.J.Hearty@nasa.gov"
             },
+            "creator": "OCO-2 Science Team/Michael Gunson, Annmarie Eldering",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C1685783920-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "Version 10r is the current version of the data set. Older versions will no longer be available and are superseded by Version 10r.\n The OCO-2 SIF Lite files contain bias-corrected solar induced chlorophyll fluorescence along with other select fields aggregated as daily files. \n\nIn early 2021, the OCO Team identified an issue with OCO-2 level 2 products processed since January 28, 2020. The Ancillary Geometric Product (AGAP) file, a static file used in OCO-2 Geolocation processing, was inadvertently replaced with an obsolete version. This AGAP file included a ~300 m pointing error. As a result, all OCO-2 Level 2, version 10r, data files for the period January 28 - December 31, 2020, were corrected and replaced. The replacement process was completed by the end of June, 2021. The significance of this error has been described in Kiel et al. (2019; doi:10.5194/amt-12-2241-2019).\n\nThe Orbiting Carbon Observatory is the first NASA mission designed to collect space-based measurements of atmospheric carbon dioxide with the precision, resolution, and coverage needed to characterize the processes controlling its buildup in the atmosphere. The OCO-2 project uses the LEOStar-2 spacecraft that carries a single instrument. It incorporates three high-resolution spectrometers that make coincident measurements of reflected sunlight in the near-infrared CO2 near 1.61 and 2.06 micrometers and in molecular oxygen (O2) A-Band at 0.76 micrometers.\n This collection encompass the output from the IMAP-DOAS preprocessor, which is used for both screening of the official XCO2 product as well as for the retrieval of Solar-Induced Fluorescence from the 0.76 micrometer O2 A-band. The IMAP-DOAS preprocessor, just as the ABO2 cloud screen, is implemented in the operational OCO-2 processing pipeline.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "OCO2_L2_Lite_SIF",
-            "creator": "OCO-2 Science Team/Michael Gunson, Annmarie Eldering",
-            "title": "OCO-2 Level 2 bias-corrected solar-induced fluorescence and other select fields from the IMAP-DOAS algorithm aggregated as daily files, Retrospective processing V10r (OCO2_L2_Lite_SIF) at GES DISC",
-            "graphic-preview-description": "OCO-2 L2 Lite Product , Solar-Induced Chlorophyll Fluorescence, (SIF) at 771nm, one day (June/01/2021), variable \"Daily_SIF_771nm\", in W/m^2/sr/micron units. Note that, although the data range is truncated at 0, small negatives values are retained in the data to avoid positive biases in SIF distributions.",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/OCO/OCO2_L2Lite_SIF_10r__20210601.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FXO2LBBNPO010",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FXO2LBBNPO010",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/OCO/OCO2_L2Lite_SIF_10r__20210601.png",
-                    "description": "OCO-2 L2 Lite Product , Solar-Induced Chlorophyll Fluorescence, (SIF) at 771nm, one day (June/01/2021), variable \"Daily_SIF_771nm\", in W/m^2/sr/micron units. Note that, although the data range is truncated at 0, small negatives values are retained in the data to avoid positive biases in SIF distributions.",
                     "@type": "dcat:Distribution",
+                    "description": "OCO-2 L2 Lite Product , Solar-Induced Chlorophyll Fluorescence, (SIF) at 771nm, one day (June/01/2021), variable \"Daily_SIF_771nm\", in W/m^2/sr/micron units. Note that, although the data range is truncated at 0, small negatives values are retained in the data to avoid positive biases in SIF distributions.",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/OCO/OCO2_L2Lite_SIF_10r__20210601.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/OCO2_L2_Lite_SIF_10r.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/OCO2_L2_Lite_SIF_10r.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://oco2.gesdisc.eosdis.nasa.gov/data/OCO2_DATA/OCO2_L2_Lite_SIF.10r/",
-                    "description": "Access the data via HTTP",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTP",
+                    "downloadURL": "https://oco2.gesdisc.eosdis.nasa.gov/data/OCO2_DATA/OCO2_L2_Lite_SIF.10r/",
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
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/OCO/OCO2_OCO3_SIF_DUG.pdf",
-                    "description": "User's Guide",
                     "@type": "dcat:Distribution",
+                    "description": "User's Guide",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/OCO/OCO2_OCO3_SIF_DUG.pdf",
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
@@ -535671,989 +535646,1026 @@
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
-                    "downloadURL": "https://oco2.gesdisc.eosdis.nasa.gov/opendap/OCO2_L2_Lite_SIF.10r/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://oco2.gesdisc.eosdis.nasa.gov/opendap/OCO2_L2_Lite_SIF.10r/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 }
             ],
+            "graphic-preview-description": "OCO-2 L2 Lite Product , Solar-Induced Chlorophyll Fluorescence, (SIF) at 771nm, one day (June/01/2021), variable \"Daily_SIF_771nm\", in W/m^2/sr/micron units. Note that, although the data range is truncated at 0, small negatives values are retained in the data to avoid positive biases in SIF distributions.",
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/OCO/OCO2_L2Lite_SIF_10r__20210601.png",
+            "identifier": "C1685783920-GES_DISC",
+            "issued": "2020-08-01",
+            "keyword": [
+                "biosphere",
+                "atmosphere",
+                "atmospheric chemistry",
+                "earth science",
+                "vegetation"
+            ],
+            "landingPage": "https://doi.org/10.5067/XO2LBBNPO010",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2020-08-10",
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
+            "temporal": "2014-09-06T00:00:00Z/2022-01-17T00:00:00Z",
             "theme": [
                 "OCO-2",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "OCO-2 Level 2 bias-corrected solar-induced fluorescence and other select fields from the IMAP-DOAS algorithm aggregated as daily files, Retrospective processing V10r (OCO2_L2_Lite_SIF) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/9UYH1Z35DOC8",
             "citation": "Chris Barnet. 2019-01-15. SNDRAQIL3SMCCP. Version 2. Sounder SIPS: AQUA AIRS IR-only Level 3 CLIMCAPS: Specific Quality Control Gridded Monthly V2. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/9UYH1Z35DOC8. https://disc.gsfc.nasa.gov/datacollection/SNDRAQIL3SMCCP_2.html. Digital Science Data.",
-            "issued": "2002-09-01",
-            "temporal": "2002-08-31T00:00:00Z/2024-12-30T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-01",
-            "references": [
-                "https://doi.org/10.3390/rs11101227",
-                "https://doi.org/10.1109/TGRS.2012.2220369",
-                "https://doi.org/Sounder SIPS: Suomi NPP CrIMSS Level 3 Comprehensive Quality Control Gridded Daily CLIMCAPS Normal Spectral Resolution V1",
-                "https://doi.org/10.1109/TGRS.2002.808236",
-                "https://doi.org/10.1029/2005/JD007020",
-                "https://doi.org/10.5194/amt-13-4437-2020"
-            ],
-            "keyword": [
-                "earth science",
-                "air quality",
-                "altitude",
-                "atmosphere",
-                "atmospheric chemistry",
-                "atmospheric pressure",
-                "surface thermal properties",
-                "atmospheric radiation",
-                "atmospheric temperature",
-                "atmospheric water vapor",
-                "clouds",
-                "land surface",
-                "oceans",
-                "ocean temperature",
-                "precipitation",
-                "surface radiative properties"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Lena Iredell",
                 "hasEmail": "mailto:lena.iredell@nasa.gov"
             },
+            "creator": "Chris Barnet",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C1693440803-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Not provided"
-            },
             "description": "WARNING: Users of the derived product \u201cco_mmr_midtrop\u201d (carbon monoxide mass mixing ratio to dry air [kg/kg] at ~500 hPa). This variable has a significant bias due to a conversion error: the molecular weight of carbon dioxide (CO2, 44.01 g/mol) was used instead of carbon monoxide (CO, 28.01 g/mol). To correct, simply multiply \u201cco_mmr_midtrop\u201d by 28.01/44.01. Alternatively, derive a profile of mass mixing ratio from scratch using the retrieved column density values (\u201cmol_lay/co_mol_lay\u201d) in the Level 2 files. For further questions or concerns please contact the Sounder SIPS at: sounder.sips@jpl.nasa.gov\n\nThe CLIMCAPS (Community Long-term Infrared Microwave Coupled Product System) algorithm is used to analyze data from the AIRS (Atmospheric Infrared Sounder). The AIRS instrument is a grating spectrometer (R = 1200) aboard the second Earth Observing System (EOS) polar-orbiting platform, EOS Aqua. The AIRS Standard Retrieval Product consists of retrieved estimates of cloud and surface properties, plus profiles of retrieved temperature, water vapor, ozone, carbon monoxide and methane. The temperature profile vertical resolution is 100 levels total between 1100 mb and 0.1 mb, while moisture profile is reported at atmospheric layers between 1100 mb and 300 mb. The horizontal resolution is 50 km.\n \nThe CLIMCAPS algorithm uses an Optimal Estimation methodology and uses an a-priori first guess to start the process. A CLIMCAPS sounding is comprised of a set of parameters that characterizes the full atmospheric state and includes a variety of geophysical parameters derived from the CrIMSS data. These include surface temperature and infrared emissivity; full atmosphere profiles of temperature, water vapor and ozone; infrared effective cloud top characteristics; carbon monoxide, methane, carbon dioxide, sulfur dioxide, nitrous oxide, and nitric acid.\n\nThis daily one degree latitude by one degree longitude level-3 product starts with level-2 retrieval products applying the specific quality control (QC) methodology. Specific QC accepts profile level from the top of the atmosphere down to the level where the QC determines that it is still good. Below this level, the data is rejected.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "SNDRAQIL3SMCCP",
-            "creator": "Chris Barnet",
-            "graphic-preview-description": "Sample plot of AIRS Level 3 Monthly Retrieval.",
-            "title": "Sounder SIPS: AQUA AIRS IR-only Level 3 CLIMCAPS: Specific Quality Control Gridded Monthly V2 (SNDRAQIL3SMCCP) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/SNDRAQIL3SMCCP_2.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2F9UYH1Z35DOC8",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2F9UYH1Z35DOC8",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/SNDRAQIL3SMCCP_2.png",
-                    "description": "Sample plot of AIRS Level 3 Monthly Retrieval.",
                     "@type": "dcat:Distribution",
+                    "description": "Sample plot of AIRS Level 3 Monthly Retrieval.",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/SNDRAQIL3SMCCP_2.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/SNDRAQIL3SMCCP_2.html",
-                    "description": "Dataset Landing Page",
                     "@type": "dcat:Distribution",
+                    "description": "Dataset Landing Page",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/SNDRAQIL3SMCCP_2.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sounder.gesdisc.eosdis.nasa.gov/data/Aqua_Sounder_Level3/SNDRAQIL3SMCCP.2/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://sounder.gesdisc.eosdis.nasa.gov/data/Aqua_Sounder_Level3/SNDRAQIL3SMCCP.2/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sounder.gesdisc.eosdis.nasa.gov/opendap/Aqua_Sounder_Level3/SNDRAQIL3SMCCP.2/",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://sounder.gesdisc.eosdis.nasa.gov/opendap/Aqua_Sounder_Level3/SNDRAQIL3SMCCP.2/",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=SNDRAQIL3SMCCP+2",
-                    "description": "Search the Earthdata website",
                     "@type": "dcat:Distribution",
+                    "description": "Search the Earthdata website",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=SNDRAQIL3SMCCP+2",
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
                 }
             ],
-            "spatial": "-180.0 -90.0 180.0 90.0",
-            "theme": [
-                "Aqua",
-                "geospatial"
+            "graphic-preview-description": "Sample plot of AIRS Level 3 Monthly Retrieval.",
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/SNDRAQIL3SMCCP_2.png",
+            "identifier": "C1693440803-GES_DISC",
+            "issued": "2002-09-01",
+            "keyword": [
+                "earth science",
+                "air quality",
+                "altitude",
+                "atmosphere",
+                "atmospheric chemistry",
+                "atmospheric pressure",
+                "surface thermal properties",
+                "atmospheric radiation",
+                "atmospheric temperature",
+                "atmospheric water vapor",
+                "clouds",
+                "land surface",
+                "oceans",
+                "ocean temperature",
+                "precipitation",
+                "surface radiative properties"
             ],
+            "landingPage": "https://doi.org/10.5067/9UYH1Z35DOC8",
             "language": [
                 "en-US"
-            ]
+            ],
+            "modified": "2024-11-01",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Not provided"
             },
-        {
-            "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/Airborne/Aeolus-CalVal-Dropsondes_DC8_1",
-            "bureauCode": [
-                "026:00"
+            "references": [
+                "https://doi.org/10.3390/rs11101227",
+                "https://doi.org/10.1109/TGRS.2012.2220369",
+                "https://doi.org/Sounder SIPS: Suomi NPP CrIMSS Level 3 Comprehensive Quality Control Gridded Daily CLIMCAPS Normal Spectral Resolution V1",
+                "https://doi.org/10.1109/TGRS.2002.808236",
+                "https://doi.org/10.1029/2005/JD007020",
+                "https://doi.org/10.5194/amt-13-4437-2020"
             ],
-            "citation": "2020-07-29. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/Airborne/Aeolus-CalVal-Dropsondes_DC8_1.",
-            "issued": "2020-07-07",
-            "temporal": "2019-04-18T00:00:00Z/2019-04-30T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-04-11",
-            "keyword": [
-                "atmospheric winds",
-                "atmosphere",
-                "atmospheric temperature",
-                "earth science"
+            "release-place": "Greenbelt, MD, USA",
+            "series-name": "SNDRAQIL3SMCCP",
+            "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2002-08-31T00:00:00Z/2024-12-30T00:00:00Z",
+            "theme": [
+                "Aqua",
+                "geospatial"
+            ],
+            "title": "Sounder SIPS: AQUA AIRS IR-only Level 3 CLIMCAPS: Specific Quality Control Gridded Monthly V2 (SNDRAQIL3SMCCP) at GES DISC"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "026:00"
             ],
+            "citation": "2020-07-29. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/Airborne/Aeolus-CalVal-Dropsondes_DC8_1.",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Kristopher Bedka",
                 "hasEmail": "mailto:kristopher.m.bedka@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/LARC/SD/ASDC"
-            },
-            "identifier": "C1918229595-LARC_ASDC",
             "description": "Aeolus-CalVal-Dropsondes_DC8_1 is the Aeolus CalVal Dropsonde Profiles data product. Data was collected using Dropsondes from the Douglas (DC-8) Aircraft. Data collection for this product is complete. \r\n\r\nNASA conducted an airborne campaign from 17 April to 30 April 2019 to: 1) demonstrate the performance of the Doppler Aerosol WiNd Lidar (DAWN) and High Altitude Lidar Observatory (HALO) instruments across a range of aerosol, cloud, and weather conditions; 2) compare these measurements with the European Space Agency Aeolus mission to gain an initial perspective of Aeolus performance in preparation for a future international Aeolus Cal/Val airborne campaign; and 3) demonstrate how weather processes can be resolved and better understood through simultaneous airborne wind, water vapor (WV), and aerosol profile observations, coupled with numerical model and other remote sensing observations. Five NASA DC-8 aircraft flights, comprising 46 flight hours, were conducted over the Eastern Pacific and Southwest U.S., based out of NASA Armstrong Flight Research Center in Palmdale, CA and Kona, HI. Yankee Environmental Systems, Inc High Definition Sounding System (HDSS) eXpendable Digitial Dropsondes (XDD) were used to validate the DAWN and Aeolus wind observations. The LaRC Diode Laser Hygrometer instrument, which was integrated on the DC-8 in preparation for another NASA airborne campaign, provided in-situ WV measurements used during one flight to validate HALO and dropsonde WV profile products.",
-            "title": "Aeolus CalVal Dropsonde Profiles",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAirborne%2FAeolus-CalVal-Dropsondes_DC8_1",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAirborne%2FAeolus-CalVal-Dropsondes_DC8_1",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.nasa.gov/feature/goddard/2019/illuminating-gases-in-the-sky-nasa-technology-pinpoints-potent-greenhouse-gases",
-                    "description": "NASA.gov Article \"Illuminating Gases in the Sky: NASA Technology Pinpoints Potent Greenhouse Gases\" (April 19, 2019)",
                     "@type": "dcat:Distribution",
+                    "description": "NASA.gov Article \"Illuminating Gases in the Sky: NASA Technology Pinpoints Potent Greenhouse Gases\" (April 19, 2019)",
+                    "downloadURL": "https://www.nasa.gov/feature/goddard/2019/illuminating-gases-in-the-sky-nasa-technology-pinpoints-potent-greenhouse-gases",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.nasa.gov/feature/langley/nasa-testing-airborne-lasers-to-touch-the-wind",
-                    "description": "NASA Langley Article: NASA Testing Airborne Lasers to Touch the Wind (April 18, 2019)",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Langley Article: NASA Testing Airborne Lasers to Touch the Wind (April 18, 2019)",
+                    "downloadURL": "https://www.nasa.gov/feature/langley/nasa-testing-airborne-lasers-to-touch-the-wind",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://eoportal.org/web/eoportal/airborne-sensors/halo",
-                    "description": "Earth Observatory Overview of the HALO (High Altitude Lidar Observatory) Instrument",
                     "@type": "dcat:Distribution",
+                    "description": "Earth Observatory Overview of the HALO (High Altitude Lidar Observatory) Instrument",
+                    "downloadURL": "https://eoportal.org/web/eoportal/airborne-sensors/halo",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1918229595-LARC_ASDC",
-                    "description": "Earthdata Search for Aeolus-CalVal-Dropsondes_DC8_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for Aeolus-CalVal-Dropsondes_DC8_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1918229595-LARC_ASDC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/Airborne/Aeolus-CalVal-Dropsondes_DC8_1",
-                    "description": "DOI data set landing page for Aeolus-CalVal-Dropsondes_DC8_1",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for Aeolus-CalVal-Dropsondes_DC8_1",
+                    "downloadURL": "https://doi.org/10.5067/Airborne/Aeolus-CalVal-Dropsondes_DC8_1",
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
-                    "downloadURL": "https://www.nasa.gov/image-feature/langley/going-where-the-wind-takes-it",
-                    "description": "NASA.gov Article \"Going Where the Wind Takes It\" (March 18, 2019)",
                     "@type": "dcat:Distribution",
+                    "description": "NASA.gov Article \"Going Where the Wind Takes It\" (March 18, 2019)",
+                    "downloadURL": "https://www.nasa.gov/image-feature/langley/going-where-the-wind-takes-it",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/soot/power-user/AEOLUS/2019",
-                    "description": "Aeolus Data on the Sub-Orbital Order Tool",
                     "@type": "dcat:Distribution",
+                    "description": "Aeolus Data on the Sub-Orbital Order Tool",
+                    "downloadURL": "https://asdc.larc.nasa.gov/soot/power-user/AEOLUS/2019",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through the Sub-Orbital Order Tool"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/Aeolus/CalVal-Dropsondes_DC8_1/",
-                    "description": "ASDC Direct Data Download for Aeolus-CalVal-Dropsondes_DC8_1",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for Aeolus-CalVal-Dropsondes_DC8_1",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/Aeolus/CalVal-Dropsondes_DC8_1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 }
             ],
+            "identifier": "C1918229595-LARC_ASDC",
+            "issued": "2020-07-07",
+            "keyword": [
+                "atmospheric winds",
+                "atmosphere",
+                "atmospheric temperature",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/Airborne/Aeolus-CalVal-Dropsondes_DC8_1",
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
             "spatial": "<?xml version=\"1.0\" encoding=\"UTF-8\"?><gml:Polygon xmlns:gml=\"http://www.opengis.net/gml/3.2\" srsName=\"EPSG:9825\"><gml:outerBoundaryIs><gml:LinearRing><gml:posList>5.0 -159.0 5.0 -113.0 52.0 -113.0 52.0 -159.0 5.0 -159.0</gml:posList></gml:LinearRing></gml:outerBoundaryIs><gml:innerBoundaryIs></gml:innerBoundaryIs></gml:Polygon>",
+            "temporal": "2019-04-18T00:00:00Z/2019-04-30T23:59:59.999Z",
             "theme": [
                 "Aeolus",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Aeolus CalVal Dropsonde Profiles"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://techport.nasa.gov/view/14683",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2014-04-01",
-            "temporal": "2014-04-01T00:00:00Z/2014-09-01T00:00:00Z",
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
-                "glenn research center",
-                "completed",
-                "project"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Michael Meador",
                 "hasEmail": "mailto:michael.a.meador@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Space Technology Mission Directorate"
-            },
-            "identifier": "TECHPORT_14683",
             "description": "&lt;p&gt;Tensegrity robots have attracted considerable attention for use in planetary exploration missions because they can be stowed into relatively small volumes before launch and are readily deployable upon landing. Because of their design and structure they can absorb significant impact shocks, such as those experienced during landing, and are well suited for use on extremely rough planetary terrains.&lt;/p&gt;",
-            "title": "Carbon Nanotube Multifunctional Tendons for Tensegrity Robots Project",
-            "programCode": [
-                "026:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "http://techport.nasa.gov/xml-api/14683",
                     "mediaType": "application/xml"
                 }
-            ]
+            ],
+            "identifier": "TECHPORT_14683",
+            "issued": "2014-04-01",
+            "keyword": [
+                "glenn research center",
+                "completed",
+                "project"
+            ],
+            "landingPage": "http://techport.nasa.gov/view/14683",
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
+            "temporal": "2014-04-01T00:00:00Z/2014-09-01T00:00:00Z",
+            "title": "Carbon Nanotube Multifunctional Tendons for Tensegrity Robots Project"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/NILL9KD1K78G",
             "citation": "Kevin W. Bowman. 2023-07-10. TRPSDL2ALLCRSMGDEL. Version 1. TROPESS CrIS-SNPP L2 for Delhi Megacity, Standard Product V1. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/NILL9KD1K78G. https://disc.gsfc.nasa.gov/datacollection/TRPSDL2ALLCRSMGDEL_1.html. Digital Science Data.",
-            "issued": "2023-06-14",
-            "temporal": "2016-01-02T00:00:00Z/2023-08-14T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-06-14",
-            "references": [
-                "https://doi.org/10.1126/sciadv.abf7460"
-            ],
-            "keyword": [
-                "atmospheric temperature",
-                "atmosphere",
-                "earth science",
-                "atmospheric water vapor",
-                "atmospheric chemistry"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "KEVIN BOWMAN",
                 "hasEmail": "mailto:kevin.w.bowman@jpl.nasa.gov"
             },
+            "creator": "Kevin W. Bowman",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C2569835155-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "The TROPESS CrIS-SNPP L2 for Delhi Megacity, Standard Product contains the vertical distribution of seven retrieved atmospheric gases (CH4, CO, H2O, HDO, NH3, O3 and PAN) and temperature, along with formal uncertainties measured by the CrIS instrument on the Suomi-NPP satellite. This standard product is one of the TROPESS Special Collections, centered on a 3x3 degree region over Delhi for the time period from 2016-01-02 to 2021-05-21. The NASA TRopospheric Ozone and Precursors from Earth System Sounding (TROPESS) project, uses an optimal estimation algorithm, known as the MUlti-SpEctra, MUlti-SpEcies, Multi-SEnsors (MUSES).\n\nThe data files are written in the netCDF version 4 file format, and each file contains one day of data. The data have a spatial resolution of 14 km (CrIS nadir FOV), and are reported at 17 vertical levels from the surface to 0.1 hPa. The principal investigator for the TROPESS project is Kevin W. Bowman.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "TRPSDL2ALLCRSMGDEL",
-            "creator": "Kevin W. Bowman",
-            "graphic-preview-description": "TROPESS CrIS-SNPP Delhi Megacity (Forward Stream, Standard Product) at 681 hPa on 01 April 2021.",
-            "title": "TROPESS CrIS-SNPP L2 for Delhi Megacity, Standard Product V1 (TRPSDL2ALLCRSMGDEL) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TROPESS/images/TRPSDL2ALLCRSMGDEL_Sample.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FNILL9KD1K78G",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FNILL9KD1K78G",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TROPESS/images/TRPSDL2ALLCRSMGDEL_Sample.png",
-                    "description": "TROPESS CrIS-SNPP Delhi Megacity (Forward Stream, Standard Product) at 681 hPa on 01 April 2021.",
                     "@type": "dcat:Distribution",
+                    "description": "TROPESS CrIS-SNPP Delhi Megacity (Forward Stream, Standard Product) at 681 hPa on 01 April 2021.",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TROPESS/images/TRPSDL2ALLCRSMGDEL_Sample.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/TRPSDL2ALLCRSMGDEL_1.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/TRPSDL2ALLCRSMGDEL_1.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/data/TROPESS_Standard/TRPSDL2ALLCRSMGDEL.1/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/data/TROPESS_Standard/TRPSDL2ALLCRSMGDEL.1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=TRPSDL2ALLCRSMGDEL_1",
-                    "description": "Use the Earthdata Search Client to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search Client to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=TRPSDL2ALLCRSMGDEL_1",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/opendap/TROPESS_Standard/TRPSDL2ALLCRSMGDEL.1/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/opendap/TROPESS_Standard/TRPSDL2ALLCRSMGDEL.1/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/data/TROPESS_Standard/TRPSDL2ALLCRSMGDEL.1/doc/TROPESS_Forward_Stream_README.pdf",
-                    "description": "README Document",
                     "@type": "dcat:Distribution",
+                    "description": "README Document",
+                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/data/TROPESS_Standard/TRPSDL2ALLCRSMGDEL.1/doc/TROPESS_Forward_Stream_README.pdf",
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
+            "graphic-preview-description": "TROPESS CrIS-SNPP Delhi Megacity (Forward Stream, Standard Product) at 681 hPa on 01 April 2021.",
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TROPESS/images/TRPSDL2ALLCRSMGDEL_Sample.png",
+            "identifier": "C2569835155-GES_DISC",
+            "issued": "2023-06-14",
+            "keyword": [
+                "atmospheric temperature",
+                "atmosphere",
+                "earth science",
+                "atmospheric water vapor",
+                "atmospheric chemistry"
+            ],
+            "landingPage": "https://doi.org/10.5067/NILL9KD1K78G",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2023-06-14",
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
+            "series-name": "TRPSDL2ALLCRSMGDEL",
             "spatial": "76.0 28.0 79.0 31.0",
+            "temporal": "2016-01-02T00:00:00Z/2023-08-14T00:00:00Z",
             "theme": [
                 "TROPESS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "TROPESS CrIS-SNPP L2 for Delhi Megacity, Standard Product V1 (TRPSDL2ALLCRSMGDEL) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/Aura/MLS/DATA1504",
             "citation": "Jarnot, R. and Perun, V.. 2020-06-11. ML1RADT. Version 005. MLS/Aura L1 Radiances from Filter Banks for THz V005. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/Aura/MLS/DATA1504. https://disc.gsfc.nasa.gov/datacollection/ML1RADT_005.html. Digital Science Data.",
-            "issued": "2020-02-06",
-            "temporal": "2004-08-01T00:00:00Z/2022-01-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-02-06",
-            "keyword": [
-                "spectral/engineering",
-                "microwave",
-                "earth science"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "NATHANIEL LIVESEY",
                 "hasEmail": "mailto:livesey@mls.jpl.nasa.gov"
             },
+            "creator": "Jarnot, R. and Perun, V.",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C1729925082-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "ML1RADT is the EOS Aura Microwave Limb Sounder (MLS) product containing the level 1 radiances from the filter banks for the GHz radiometers. The data version is 5.0. Data coverage is from August 8, 2004 to current. Spatial coverage is near-global (-82 degrees to +82 degrees latitude), and files contain a full days worth of data (15 orbits). Users of the ML1RADG data product should read the 'A Short Guide to the Use and Interpretation of v4.2x Level 1 Data' document for additional information.\n\nThe data are stored in the version 5 Hierarchical Data Format, or HDF-5. Each file contains radiances and ancillary information written as HDF-5 dataset objects (n-dimensional arrays), along with file attributes and metadata.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "ML1RADT",
-            "creator": "Jarnot, R. and Perun, V.",
-            "title": "MLS/Aura L1 Radiances from Filter Banks for THz V005 (ML1RADT) at GES DISC",
-            "graphic-preview-description": "Aura MLS logo",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/ML1RADT_005.jpeg",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAura%2FMLS%2FDATA1504",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAura%2FMLS%2FDATA1504",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/ML1RADT_005.jpeg",
-                    "description": "Aura MLS logo",
                     "@type": "dcat:Distribution",
+                    "description": "Aura MLS logo",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/ML1RADT_005.jpeg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/ML1RADT_005.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/ML1RADT_005.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://aura.gesdisc.eosdis.nasa.gov/data/Aura_MLS_Level1/ML1RADT.005/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://aura.gesdisc.eosdis.nasa.gov/data/Aura_MLS_Level1/ML1RADT.005/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=ML1RADT_005",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=ML1RADT_005",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://mls.jpl.nasa.gov/data/Level_1_ReadMe_v4.pdf",
-                    "description": "README Document",
                     "@type": "dcat:Distribution",
+                    "description": "README Document",
+                    "downloadURL": "https://mls.jpl.nasa.gov/data/Level_1_ReadMe_v4.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's read me document"
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
+            "graphic-preview-description": "Aura MLS logo",
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/ML1RADT_005.jpeg",
+            "identifier": "C1729925082-GES_DISC",
+            "issued": "2020-02-06",
+            "keyword": [
+                "spectral/engineering",
+                "microwave",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/Aura/MLS/DATA1504",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2020-02-06",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
+            },
+            "release-place": "Greenbelt, MD, USA",
+            "series-name": "ML1RADT",
             "spatial": "-180.0 -82.0 180.0 82.0",
+            "temporal": "2004-08-01T00:00:00Z/2022-01-17T00:00:00Z",
             "theme": [
                 "Aura",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "MLS/Aura L1 Radiances from Filter Banks for THz V005 (ML1RADT) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://c3.nasa.gov/dashlink/resources/875/",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2013-12-24",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
-            "keyword": [
-                "nasa",
-                "ames",
-                "dashlink"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Brian Bole",
                 "hasEmail": "mailto:brian.bole@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Dashlink"
-            },
-            "identifier": "DASHLINK_875",
             "description": "Validation of prognostic technologies through ground and flight tests is an important step in maturing these novel technologies and deploying them on real-world systems. To this end, a series of flight tests have been conducted using an unmanned electric vehicle during which the motor system batteries were monitored by a prognostic algorithm. The research presented here endeavors to produce and validate a technology for predicting the remaining time until end-ofdischarge of the batteries on an electric aircraft as a function of an expected future flight and online estimates of the charge contained in the batteries. Flight data and flight experiment results are presented along with an assessment of model and algorithm performance",
-            "title": "Battery Charge Depletion Prediction on an Electric Aircraft",
-            "programCode": [
-                "026:029"
-            ],
             "distribution": [
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/publication/phmc_13_066.pdf",
-                    "description": "phmc_13_066.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "phmc_13_066.pdf",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/publication/phmc_13_066.pdf",
+                    "mediaType": "application/pdf",
                     "title": "phmc_13_066.pdf"
                 }
             ],
-            "accrualPeriodicity": "irregular"
+            "identifier": "DASHLINK_875",
+            "issued": "2013-12-24",
+            "keyword": [
+                "nasa",
+                "ames",
+                "dashlink"
+            ],
+            "landingPage": "https://c3.nasa.gov/dashlink/resources/875/",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:029"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Dashlink"
+            },
+            "title": "Battery Charge Depletion Prediction on an Electric Aircraft"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-X-OSIWAC-4-CR5-CHKOUT-STR-REFL-V1.0",
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
-                "4 vesta"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This CODMAC level 4 data set contains solar stray light corrected, radiometric calibrated and geometric distortion corrected (resampled) image data in in reflectance units  (normalized and thus without unit),  acquired by the OSIRIS Wide Angle Camera on the Rosetta spacecraft  during the CRUISE 5 mission phase, covering the period  from 2009-12-14T00:00:00.000 to 2010-05-16T23:59:59.000. The prime objective was commissioning / calibration. Several targets of opportunity were observed, but none of them is identifiable as prime target. This version V1.0 is the first version of this dataset.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-x-osiwac-4-cr5-chkout-str-refl-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "4 vesta"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-X-OSIWAC-4-CR5-CHKOUT-STR-REFL-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-x-osiwac-4-cr5-chkout-str-refl-v1.0",
-            "description": "This CODMAC level 4 data set contains solar stray light corrected, radiometric calibrated and geometric distortion corrected (resampled) image data in in reflectance units  (normalized and thus without unit),  acquired by the OSIRIS Wide Angle Camera on the Rosetta spacecraft  during the CRUISE 5 mission phase, covering the period  from 2009-12-14T00:00:00.000 to 2010-05-16T23:59:59.000. The prime objective was commissioning / calibration. Several targets of opportunity were observed, but none of them is identifiable as prime target. This version V1.0 is the first version of this dataset.",
-            "title": "ROSETTA-ORBITER CHECKOUT OSIWAC 4 CR5 RDR-STR-REFL V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER CHECKOUT OSIWAC 4 CR5 RDR-STR-REFL V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=JNO-J-JED-3-CDR-V1.0",
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
-                "juno"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "Abstract ======== This data set consists of the JUNO JEDI (Jupiter Energetic-Particle Detector) calibrated observations, also known as CDRs. The system is made up of 3 instrument subsystems (pucks) aligned in three directions on the spinning JUNO spacecraft. The pucks each have 6 look directions (telescopes) with a time of flight (TOF) and a deposited energy detection (SSD) system.  In addition, the pulse height of the signal in the TOF system can be used for energy measurement. The instruments can be operated in a variety of modes, differing in the way they use and combine these measurements. More details are available in the INSTRUMENT.CAT file and the JEDI SIS. The CDRs are organized in files covering one day of spacecraft event time (SCET). There are potentially 10 different files per puck, corresponding to the available data gathering modes: HIERSESP, HIERSISP, HIERSTOFXER, HIERSTOFXPHR, LOERSESP, LOERSISP, LOERSTOFXER, LOERSTOFXPHR, NONPTOFXER, NONPTOFXPHR. Depending on how the pucks are operated, not all data types will be available for all pucks for any particular time range. All the measured quantities present in the uncalibrated data files (EDRs) are present here in three forms: counts per accumulation (the same numbers as in the EDRs), counts per second (this number may be corrected for instrument saturation and background), intensity (counts per second per steradian per cm2 per keV). Additional support quantities are also included for the convenience or enlightenment of the end user.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.jno-j-jed-3-cdr-v1.0_bi47-a83c",
+            "issued": "2021-05-21",
+            "keyword": [
+                "jupiter",
+                "juno"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=JNO-J-JED-3-CDR-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.jno-j-jed-3-cdr-v1.0_bi47-a83c",
-            "description": "Abstract ======== This data set consists of the JUNO JEDI (Jupiter Energetic-Particle Detector) calibrated observations, also known as CDRs. The system is made up of 3 instrument subsystems (pucks) aligned in three directions on the spinning JUNO spacecraft. The pucks each have 6 look directions (telescopes) with a time of flight (TOF) and a deposited energy detection (SSD) system.  In addition, the pulse height of the signal in the TOF system can be used for energy measurement. The instruments can be operated in a variety of modes, differing in the way they use and combine these measurements. More details are available in the INSTRUMENT.CAT file and the JEDI SIS. The CDRs are organized in files covering one day of spacecraft event time (SCET). There are potentially 10 different files per puck, corresponding to the available data gathering modes: HIERSESP, HIERSISP, HIERSTOFXER, HIERSTOFXPHR, LOERSESP, LOERSISP, LOERSTOFXER, LOERSTOFXPHR, NONPTOFXER, NONPTOFXPHR. Depending on how the pucks are operated, not all data types will be available for all pucks for any particular time range. All the measured quantities present in the uncalibrated data files (EDRs) are present here in three forms: counts per accumulation (the same numbers as in the EDRs), counts per second (this number may be corrected for instrument saturation and background), intensity (counts per second per steradian per cm2 per keV). Additional support quantities are also included for the convenience or enlightenment of the end user.",
-            "title": "JNO J JED 3 CDR V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "JNO J JED 3 CDR V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/MODIS/MCD43D56.061",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Crystal Schaaf, Zhuosen Wang. 2021-02-22. MODIS/Terra+Aqua BRDF/Albedo White Sky Albedo Band5 Daily L3 Global 30ArcSec CMG V061. Sioux Falls, South Dakota, USA. Archived by National Aeronautics and Space Administration, U.S. Government, NASA EOSDIS Land Processes Distributed Active Archive Center. https://doi.org/10.5067/MODIS/MCD43D56.061. https://doi.org/10.5067/MODIS/MCD43D56.061. The DOI landing page provides citations in APA and Chicago styles..",
-            "issued": "2021-02-22",
-            "temporal": "2000-02-16T00:00:00Z/2024-05-20T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2021-02-22",
-            "keyword": [
-                "surface radiative properties",
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
-            "identifier": "C2540273121-LPCLOUD",
-            "description": "The MCD43D56 Version 6.1 Bidirectional Reflectance Distribution Function and Albedo (BRDF/Albedo) White-Sky Albedo dataset is produced daily using 16 days of Terra and Aqua Moderate Resolution Imaging Spectroradiometer (MODIS) data at 30 arc second (1,000 meter (m)) resolution. Data are temporally weighted to the ninth day which is reflected in the Julian date in the file name. This Climate Modeling Grid (CMG) product covers the entire globe for use in climate simulation models. Due to the large file size, each MCD43D product contains just one data layer. \r\n\r\nMCD43D42 through MCD43D61 are the albedo products of the MCD43D BRDF/Albedo product suite. There are 10 black-sky albedo and 10 white-sky albedo layers representing MODIS bands 1 through 7 and the visible, near infrared (NIR), and shortwave bands. The black-sky albedo (directional hemispherical reflectance) is defined as albedo in the absence of a diffuse component and is a function of solar zenith angle. White-sky albedo (bihemispherical reflectance) is defined as albedo in the absence of a direct component when the diffuse component is isotropic. \r\n\r\nMCD43D56 is the white-sky albedo for MODIS band 5. \r\n\r\nImprovements/Changes from Previous Versions\r\n\r\n* The Version 6.1 Level-1B (L1B) products have been improved by undergoing various calibration changes that include: changes to the response-versus-scan angle (RVS) approach that affects reflectance bands for Aqua and Terra MODIS, corrections to adjust for the optical crosstalk in Terra MODIS infrared (IR) bands, and corrections to the Terra MODIS forward look-up table (LUT) update for the period 2012 - 2017.\r\n* A polarization correction has been applied to the L1B Reflective Solar Bands (RSB).",
-            "release-place": "Sioux Falls, South Dakota, USA",
             "creator": "Crystal Schaaf, Zhuosen Wang",
-            "title": "MODIS/Terra+Aqua BRDF/Albedo White Sky Albedo Band5 Daily L3 Global 30ArcSec CMG V061",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The MCD43D56 Version 6.1 Bidirectional Reflectance Distribution Function and Albedo (BRDF/Albedo) White-Sky Albedo dataset is produced daily using 16 days of Terra and Aqua Moderate Resolution Imaging Spectroradiometer (MODIS) data at 30 arc second (1,000 meter (m)) resolution. Data are temporally weighted to the ninth day which is reflected in the Julian date in the file name. This Climate Modeling Grid (CMG) product covers the entire globe for use in climate simulation models. Due to the large file size, each MCD43D product contains just one data layer. \r\n\r\nMCD43D42 through MCD43D61 are the albedo products of the MCD43D BRDF/Albedo product suite. There are 10 black-sky albedo and 10 white-sky albedo layers representing MODIS bands 1 through 7 and the visible, near infrared (NIR), and shortwave bands. The black-sky albedo (directional hemispherical reflectance) is defined as albedo in the absence of a diffuse component and is a function of solar zenith angle. White-sky albedo (bihemispherical reflectance) is defined as albedo in the absence of a direct component when the diffuse component is isotropic. \r\n\r\nMCD43D56 is the white-sky albedo for MODIS band 5. \r\n\r\nImprovements/Changes from Previous Versions\r\n\r\n* The Version 6.1 Level-1B (L1B) products have been improved by undergoing various calibration changes that include: changes to the response-versus-scan angle (RVS) approach that affects reflectance bands for Aqua and Terra MODIS, corrections to adjust for the optical crosstalk in Terra MODIS infrared (IR) bands, and corrections to the Terra MODIS forward look-up table (LUT) update for the period 2012 - 2017.\r\n* A polarization correction has been applied to the L1B Reflective Solar Bands (RSB).",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMODIS%2FMCD43D56.061",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMODIS%2FMCD43D56.061",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "application/x-hdf",
-                    "downloadURL": "https://e4ftl01.cr.usgs.gov/MOTA/MCD43D56.061/",
-                    "description": "LP DAAC Data Pool provides direct access to available products via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "LP DAAC Data Pool provides direct access to available products via HTTPS.",
+                    "downloadURL": "https://e4ftl01.cr.usgs.gov/MOTA/MCD43D56.061/",
+                    "mediaType": "application/x-hdf",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "application/x-hdf",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=C2540273121-LPCLOUD",
-                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=C2540273121-LPCLOUD",
+                    "mediaType": "application/x-hdf",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/MODIS/MCD43D56.061",
-                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
+                    "downloadURL": "https://doi.org/10.5067/MODIS/MCD43D56.061",
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
-                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/filespec/MODIS/6/MCD43D56",
-                    "description": "The File Specification provides a description of the product file including Scientific Data Sets and their attributes.",
                     "@type": "dcat:Distribution",
+                    "description": "The File Specification provides a description of the product file including Scientific Data Sets and their attributes.",
+                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/filespec/MODIS/6/MCD43D56",
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
-                    "downloadURL": "https://opendap.cr.usgs.gov/opendap/hyrax/DP137/MOTA/MCD43D56.061/contents.html",
-                    "description": "Access data via Open-source Project for a Network Data Access Protocol",
                     "@type": "dcat:Distribution",
+                    "description": "Access data via Open-source Project for a Network Data Access Protocol",
+                    "downloadURL": "https://opendap.cr.usgs.gov/opendap/hyrax/DP137/MOTA/MCD43D56.061/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 }
             ],
+            "identifier": "C2540273121-LPCLOUD",
+            "issued": "2021-02-22",
+            "keyword": [
+                "surface radiative properties",
+                "earth science",
+                "land surface",
+                "national geospatial data asset",
+                "ngda"
+            ],
+            "landingPage": "https://doi.org/10.5067/MODIS/MCD43D56.061",
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
+            "title": "MODIS/Terra+Aqua BRDF/Albedo White Sky Albedo Band5 Daily L3 Global 30ArcSec CMG V061"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ASDC_DAAC/FIRE/0076",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "1999-11-15. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/ASDC_DAAC/FIRE/0076.",
-            "issued": "1999-11-08",
-            "temporal": "1986-10-14T00:00:00Z/1986-11-02T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2018-07-13",
-            "keyword": [
-                "atmospheric radiation",
-                "atmosphere",
-                "earth science",
-                "atmospheric water vapor",
-                "clouds",
-                "atmospheric temperature",
-                "atmospheric winds"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "ANDREW HEYMSFIELD",
                 "hasEmail": "mailto:heyms1@ucar.edu"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/LARC/SD/ASDC"
-            },
-            "identifier": "C1000001082-LARC_ASDC",
             "description": "The First ISCCP Regional Experiments have been designed to improve data products and cloud/radiation parameterizations used in general circulation models (GCMs). Specifically, the goals of FIRE are (1) to improve basic understanding of the interaction of physical processes in determining life cycles of cirrus and marine stratocumulus systems and the radiative properties of these clouds during their life cycles and (2) to investigate the interrelationships between the ISCCP data, GCM parameterizations, and higher space and time resolution cloud data.To-date, four intensive field-observation periods were planned and executed: a cirrus IFO (October 13-November 2, 1986); a marine stratocumulus IFO off the southwestern coast of California (June 29-July 20, 1987); a second cirrus IFO in southeastern Kansas (November 13-December 7, 1991); and a second marine stratocumulus IFO in the eastern North Atlantic Ocean (June 1-June 28, 1992). Each mission combined coordinated satellite, airborne, and surface observations with modeling studies to investigate the cloud properties and physical processes of the cloud systems. Cirrus IFO-I was conducted from October 13 to November 2, 1986 in central Wisconsin. The NCAR King Air aircraft measured radiation andmicrophysical properties of the cloud layers, in addition to temperature, moisture, and air motions.",
-            "title": "First ISCCP Regional Experiment (FIRE) Cirrus Phase I National Center for Atmospheric Research (NCAR) Kingair Aircraft Data",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC_DAAC%2FFIRE%2F0076",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC_DAAC%2FFIRE%2F0076",
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
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1000001082-LARC_ASDC",
-                    "description": "Earthdata Search for FIRE_CI1_KINGAIR_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for FIRE_CI1_KINGAIR_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1000001082-LARC_ASDC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/guide/base_fire_kingair_dataset.pdf",
-                    "description": "FIRE NCAR Kingair Aircraft Langley DAAC Data Set Document",
                     "@type": "dcat:Distribution",
+                    "description": "FIRE NCAR Kingair Aircraft Langley DAAC Data Set Document",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/guide/base_fire_kingair_dataset.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/read_software/fire_lib.c",
-                    "description": "fsdf_lib Program for reading FIRE Cirrus I, Cirrus II, and MS data sets - Direct File Download (.c)",
                     "@type": "dcat:Distribution",
+                    "description": "fsdf_lib Program for reading FIRE Cirrus I, Cirrus II, and MS data sets - Direct File Download (.c)",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/read_software/fire_lib.c",
+                    "mediaType": "text/html",
                     "title": "View this dataset's science data product software documentation"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/read_software/genpro.c",
-                    "description": "Program to read GENPRO Formatted Files - Direct File Download (.c)",
                     "@type": "dcat:Distribution",
+                    "description": "Program to read GENPRO Formatted Files - Direct File Download (.c)",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/read_software/genpro.c",
+                    "mediaType": "text/html",
                     "title": "View this dataset's how-to documentation"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/read_software/Makefile.fci1",
-                    "description": "Makefile.fci1 Release: 1.1 Date: 7/29/94",
                     "@type": "dcat:Distribution",
+                    "description": "Makefile.fci1 Release: 1.1 Date: 7/29/94",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/read_software/Makefile.fci1",
+                    "mediaType": "text/html",
                     "title": "View this dataset's science data product software documentation"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/ASDC_DAAC/FIRE/0076",
-                    "description": "DOI data set landing page for FIRE_CI1_KINGAIR_1",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for FIRE_CI1_KINGAIR_1",
+                    "downloadURL": "https://doi.org/10.5067/ASDC_DAAC/FIRE/0076",
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
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/FIRE/FIRE_CI1_KINGAIR/",
-                    "description": "ASDC Direct Data Download for FIRE_CI1_KINGAIR_1",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for FIRE_CI1_KINGAIR_1",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/FIRE/FIRE_CI1_KINGAIR/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/FIRE/FIRE_CI1_KINGAIR/contents.html",
-                    "description": "OPeNDAP data access for FIRE_CI1_KINGAIR_1",
                     "@type": "dcat:Distribution",
+                    "description": "OPeNDAP data access for FIRE_CI1_KINGAIR_1",
+                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/FIRE/FIRE_CI1_KINGAIR/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 }
             ],
+            "identifier": "C1000001082-LARC_ASDC",
+            "issued": "1999-11-08",
+            "keyword": [
+                "atmospheric radiation",
+                "atmosphere",
+                "earth science",
+                "atmospheric water vapor",
+                "clouds",
+                "atmospheric temperature",
+                "atmospheric winds"
+            ],
+            "landingPage": "https://doi.org/10.5067/ASDC_DAAC/FIRE/0076",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2018-07-13",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/LARC/SD/ASDC"
+            },
             "spatial": "<?xml version=\"1.0\" encoding=\"UTF-8\"?><gml:Polygon xmlns:gml=\"http://www.opengis.net/gml/3.2\" srsName=\"EPSG:4326\"><gml:outerBoundaryIs><gml:LinearRing><gml:posList>40.36 -96.92 40.36 -87.0 46.82 -87.0 46.82 -96.92 40.36 -96.92</gml:posList></gml:LinearRing></gml:outerBoundaryIs><gml:innerBoundaryIs></gml:innerBoundaryIs></gml:Polygon>",
+            "temporal": "1986-10-14T00:00:00Z/1986-11-02T23:59:59.999Z",
             "theme": [
                 "FIRE",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "First ISCCP Regional Experiment (FIRE) Cirrus Phase I National Center for Atmospheric Research (NCAR) Kingair Aircraft Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://mirador.gsfc.nasa.gov/cgi-bin/mirador/presentNavigation.pl?tree=scienceArea&scienceArea=Weather",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Steven Kempler",
+                "hasEmail": "mailto:Steven.J.Kempler@nasa.gov"
+            },
+            "description": "Earth Science data access made simple. Our weather system includes the dynamics of the atmosphere and its interaction with the oceans and land. The improvement of our understanding of weather processes and phenomena is crucial in gaining an understanding of the Earth system.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://mirador.gsfc.nasa.gov/cgi-bin/mirador/servcoll.pl?helpmenuclass=inventory&CGISESSID=eb339eab3ab73f9cc2e88005a366822d&CURRENT_CONTEXT=KeywordSearch&SearchButton=Search%20GES-DISC",
+                    "mediaType": "text/html"
+                }
+            ],
+            "identifier": "NASA-0000083",
             "issued": "2018-06-25",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
             "keyword": [
                 "ice",
                 "pressure",
@@ -536671,112 +536683,78 @@
                 "terrestrial water",
                 "atmospheric height"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Steven Kempler",
-                "hasEmail": "mailto:Steven.J.Kempler@nasa.gov"
-            },
+            "landingPage": "http://mirador.gsfc.nasa.gov/cgi-bin/mirador/presentNavigation.pl?tree=scienceArea&scienceArea=Weather",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:001"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "NASA-0000083",
-            "description": "Earth Science data access made simple. Our weather system includes the dynamics of the atmosphere and its interaction with the oceans and land. The improvement of our understanding of weather processes and phenomena is crucial in gaining an understanding of the Earth system.",
-            "title": "Mirador - Weather",
-            "programCode": [
-                "026:001"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://mirador.gsfc.nasa.gov/cgi-bin/mirador/servcoll.pl?helpmenuclass=inventory&CGISESSID=eb339eab3ab73f9cc2e88005a366822d&CURRENT_CONTEXT=KeywordSearch&SearchButton=Search%20GES-DISC",
-                    "mediaType": "text/html"
-                }
-            ],
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "Mirador - Weather"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=IHW-C-PPMAG-3-RDR-HALLEY-V2.0",
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
-                "1p/halley 1 (1682 q1)",
-                "international halley watch"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This data set presents the photometric magnitude measurements of 1P/Halley submitted to the International Halley Watch (IHW) Photometry and Polarimetry Network (PPN). Both broadband and narrowband magnitudes are included, with filter parameters for each measurement. In this second version, the FITS tables have been converted to flat ASCII, the PDS labels rewritten, a table combing all the measurements into a single, chronological set has been added, and known errata have been corrected.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ihw-c-ppmag-3-rdr-halley-v2.0_bi9m-bb7p",
+            "issued": "2021-05-21",
+            "keyword": [
+                "1p/halley 1 (1682 q1)",
+                "international halley watch"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=IHW-C-PPMAG-3-RDR-HALLEY-V2.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ihw-c-ppmag-3-rdr-halley-v2.0_bi9m-bb7p",
-            "description": "This data set presents the photometric magnitude measurements of 1P/Halley submitted to the International Halley Watch (IHW) Photometry and Polarimetry Network (PPN). Both broadband and narrowband magnitudes are included, with filter parameters for each measurement. In this second version, the FITS tables have been converted to flat ASCII, the PDS labels rewritten, a table combing all the measurements into a single, chronological set has been added, and known errata have been corrected.",
-            "title": "IHW COMET HALLEY PHOTOMETRIC MAGNITUDES, V2.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "IHW COMET HALLEY PHOTOMETRIC MAGNITUDES, V2.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/Aura/HIRDLS-MLS/DATA301",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Massie, S. T. and Jiang, J. H.. 2013-08-19. HIRMLS3IWC. Version 002. HIRDLS-MLS/Aura Level 3 Monthly 10 x 20 deg Ice Water Content V002. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/Aura/HIRDLS-MLS/DATA301. https://disc.gsfc.nasa.gov/datacollection/HIRMLS3IWC_002.html. Digital Science Data.",
-            "issued": "2013-03-13",
-            "temporal": "2005-02-01T00:00:00Z/2007-12-31T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2013-03-13",
-            "keyword": [
-                "clouds",
-                "atmosphere",
-                "earth science"
-            ],
-            "data-presentation-form": "Digital Science Data",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "JOHN GILLE",
                 "hasEmail": "mailto:gille@ucar.edu"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
-            "identifier": "C1251101078-GES_DISC",
-            "description": "HIRMLS3IWC is the Joint EOS High Resolution Dynamics Limb Sounder (HIRDLS) and Microwave Limb Sounder (MLS) monthly 10 degreee lat x 20 degreee lon gridded product for ice water content (IWC) data. This is version 2 released to the public, with the original input coming from v3.3 MLS and v7 HIRDLS. The grid spatial coverage is near-global (-80 to +90 degrees latitude). The product contains HIRDLS and MLS IWC data for the time of the HIRDLS mission from February 1, 2005 through December 31, 2007. The useful vertical range of the data is from 215 to 82 hPa for both HIRDLS and MLS, and the vertical resolution is about 1.5 km for HIRDLS and 3 km for MLS. Users of the HIRMLS3IWC data product should read the Version 2 HIRDLS-MLS Level 3 IWC Data Description and Quality document for more information.\n\nThe data are stored in the version 5 EOS Hierarchical Data Format (HDF-EOS5), which is based on the version 5 Hierarchical Data Format, or HDF5. The data file contains two grid objects (one with HIRDLS data, the other with MLS data), each with a set of data fields, attributes, and metadata. Each grid contains data fields with IWC values, and the HIRDLS grid includes data fields with volume density, cloud top pressure and frequency of clouds. Time, latitude and vertical pressure information are also included in each grid.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "HIRMLS3IWC",
             "creator": "Massie, S. T. and Jiang, J. H.",
-            "title": "HIRDLS-MLS/Aura Level 3 Monthly 10 x 20 deg Ice Water Content V002 (HIRMLS3IWC) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/HIRMLS3IWC_002.png",
-            "programCode": [
-                "026:001"
-            ],
+            "data-presentation-form": "Digital Science Data",
+            "description": "HIRMLS3IWC is the Joint EOS High Resolution Dynamics Limb Sounder (HIRDLS) and Microwave Limb Sounder (MLS) monthly 10 degreee lat x 20 degreee lon gridded product for ice water content (IWC) data. This is version 2 released to the public, with the original input coming from v3.3 MLS and v7 HIRDLS. The grid spatial coverage is near-global (-80 to +90 degrees latitude). The product contains HIRDLS and MLS IWC data for the time of the HIRDLS mission from February 1, 2005 through December 31, 2007. The useful vertical range of the data is from 215 to 82 hPa for both HIRDLS and MLS, and the vertical resolution is about 1.5 km for HIRDLS and 3 km for MLS. Users of the HIRMLS3IWC data product should read the Version 2 HIRDLS-MLS Level 3 IWC Data Description and Quality document for more information.\n\nThe data are stored in the version 5 EOS Hierarchical Data Format (HDF-EOS5), which is based on the version 5 Hierarchical Data Format, or HDF5. The data file contains two grid objects (one with HIRDLS data, the other with MLS data), each with a set of data fields, attributes, and metadata. Each grid contains data fields with IWC values, and the HIRDLS grid includes data fields with volume density, cloud top pressure and frequency of clouds. Time, latitude and vertical pressure information are also included in each grid.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAura%2FHIRDLS-MLS%2FDATA301",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAura%2FHIRDLS-MLS%2FDATA301",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
@@ -536786,236 +536764,241 @@
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/HIRMLS3IWC_002.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/HIRMLS3IWC_002.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/Aura_HIRDLS_MLS_Level3/HIRMLS3IWC.002/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/Aura_HIRDLS_MLS_Level3/HIRMLS3IWC.002/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/opendap/HDF-EOS5/Aura_HIRDLS_MLS_Level3/HIRMLS3IWC.002/HIRDLS-MLS-Aura_L3IWC_v02-00-00-c01_2005m02-2007m12.he5.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/opendap/HDF-EOS5/Aura_HIRDLS_MLS_Level3/HIRMLS3IWC.002/HIRDLS-MLS-Aura_L3IWC_v02-00-00-c01_2005m02-2007m12.he5.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=HIRMLS3IWC_002",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=HIRMLS3IWC_002",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "application/msword",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/HIRDLS/SC-HIR-1849B.doc",
-                    "description": "README and Data Quality document",
                     "@type": "dcat:Distribution",
+                    "description": "README and Data Quality document",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/HIRDLS/SC-HIR-1849B.doc",
+                    "mediaType": "application/msword",
                     "title": "View this dataset's read me document"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/repository/Mission/HIRDLS/3.3_Product_Documentation/3.3.6_Product_Application/All_HIRDLS_Papers_26June2013.pdf",
-                    "description": "List of publications.",
                     "@type": "dcat:Distribution",
+                    "description": "List of publications.",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/repository/Mission/HIRDLS/3.3_Product_Documentation/3.3.6_Product_Application/All_HIRDLS_Papers_26June2013.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's publications"
                 }
             ],
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/HIRMLS3IWC_002.png",
+            "identifier": "C1251101078-GES_DISC",
+            "issued": "2013-03-13",
+            "keyword": [
+                "clouds",
+                "atmosphere",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/Aura/HIRDLS-MLS/DATA301",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2013-03-13",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
+            },
+            "release-place": "Greenbelt, MD, USA",
+            "series-name": "HIRMLS3IWC",
             "spatial": "-180.0 -80.0 180.0 90.0",
+            "temporal": "2005-02-01T00:00:00Z/2007-12-31T23:59:59.999Z",
             "theme": [
                 "Aura",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "HIRDLS-MLS/Aura Level 3 Monthly 10 x 20 deg Ice Water Content V002 (HIRMLS3IWC) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-X-SREM-5-EXT3-MTP034-V1.0",
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
+            "description": "This data set contains derived electron and proton flux energies in MeV from the Standard Radiation Environment Monitor (SREM) instrument on the Rosetta spacecraft, which had the primary target of comet 67P/Churyumov-Gerasimenko. These are CODMAC Level 5 derived data, and measure the radiation in the spacecraft environment during the Medium Term Plan 34 period of the EXTENSION 3 mission phase.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-x-srem-5-ext3-mtp034-v1.0_biaw-d8yz",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-X-SREM-5-EXT3-MTP034-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-x-srem-5-ext3-mtp034-v1.0_biaw-d8yz",
-            "description": "This data set contains derived electron and proton flux energies in MeV from the Standard Radiation Environment Monitor (SREM) instrument on the Rosetta spacecraft, which had the primary target of comet 67P/Churyumov-Gerasimenko. These are CODMAC Level 5 derived data, and measure the radiation in the spacecraft environment during the Medium Term Plan 34 period of the EXTENSION 3 mission phase.",
-            "title": "ROSETTA-ORBITER 67P SREM 5 EXTENSION 3\n    MTP034 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P SREM 5 EXTENSION 3\n    MTP034 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://c3.nasa.gov/dashlink/resources/212/",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
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
                 "fn": "Deniz Gencaga",
                 "hasEmail": "mailto:dgencaga@gmail.com"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Dashlink"
-            },
-            "identifier": "DASHLINK_212",
             "description": "In this paper, we propose a novel approach to reduce the noise in Synthetic Aperture Radar (SAR) images using particle filters. Interpretation of SAR images is a difficult problem, since they are contaminated with a multiplicative noise, which is known as the \u201cSpeckle Noise\u201d. In literature, the general approach  for removing\r\nthe speckle is to use the local statistics, which are computed in a square window. Here, we propose to use particle filters, which is a sequential Bayesian technique. The proposed method also uses the local statistics to denoise the images. Since this is a Bayesian\r\napproach, the computed statistics of the window can be exploited as a priori information. Moreover, particle filters are sequential methods, which are more appropriate to handle the heterogeneous structure of the image. Computer simulations show that the proposed method provides better edge-preserving results with\r\nsatisfactory speckle removal, when compared to the results obtained by Gamma Maximum a posteriori (MAP) filter.",
-            "title": "SAR Image Enhancement using Particle Filters",
-            "programCode": [
-                "026:029"
-            ],
             "distribution": [
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/publication/ESA_EUSC_conference_GENCAGA_etal.pdf",
-                    "description": "SAR image enhancement using particle filtering",
                     "@type": "dcat:Distribution",
+                    "description": "SAR image enhancement using particle filtering",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/publication/ESA_EUSC_conference_GENCAGA_etal.pdf",
+                    "mediaType": "application/pdf",
                     "title": "ESA_EUSC_conference_GENCAGA_etal.pdf"
                 }
             ],
-            "accrualPeriodicity": "irregular"
+            "identifier": "DASHLINK_212",
+            "issued": "2010-09-22",
+            "keyword": [
+                "dashlink",
+                "ames",
+                "nasa"
+            ],
+            "landingPage": "https://c3.nasa.gov/dashlink/resources/212/",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:029"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Dashlink"
+            },
+            "title": "SAR Image Enhancement using Particle Filters"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=LRO-L-MRFLRO-1-PDR-V1.0",
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
+            "description": "This data set contains archival raw data acquired from the Mini-RF instrument during the LRO mission.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.lro-l-mrflro-1-pdr-v1.0_bic5-3egh",
+            "issued": "2018-06-26",
+            "keyword": [
+                "lunar reconnaissance orbiter",
+                "moon"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=LRO-L-MRFLRO-1-PDR-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.lro-l-mrflro-1-pdr-v1.0_bic5-3egh",
-            "description": "This data set contains archival raw data acquired from the Mini-RF instrument during the LRO mission.",
-            "title": "LRO MOON MINI-RF 1 PACKETIZED DATA RECORD V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "LRO MOON MINI-RF 1 PACKETIZED DATA RECORD V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG2-N-UVS-3-RDR-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This data set contains reformatted records derived from data returned by the Voyager Ultraviolet Spectrometer Subsystem on board Voyager 2 during the Neptune encounter phase of the Voyager mission. Original instrument data were merged with ancillary data from footprint SEDR files provided by the Voyager Project at the Jet Propulsion Laboratory. The final product files are formatted as PDS binary tables.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg2-n-uvs-3-rdr-v1.0_bic7-yaxr",
             "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "comet sl9/jupiter collision",
                 "neptune",
                 "voyager"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG2-N-UVS-3-RDR-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg2-n-uvs-3-rdr-v1.0_bic7-yaxr",
-            "description": "This data set contains reformatted records derived from data returned by the Voyager Ultraviolet Spectrometer Subsystem on board Voyager 2 during the Neptune encounter phase of the Voyager mission. Original instrument data were merged with ancillary data from footprint SEDR files provided by the Voyager Project at the Jet Propulsion Laboratory. The final product files are formatted as PDS binary tables.",
-            "title": "VG2 NEPTUNE ULTRAVIOLET SPECTROMETER SUBSYSTEM 3 RDR V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "VG2 NEPTUNE ULTRAVIOLET SPECTROMETER SUBSYSTEM 3 RDR V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1000000006-CDDIS.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/GSFC/SED/ESD/GGL/CDDIS.",
-            "issued": "1998-05-01",
-            "temporal": "2008-10-05T00:00:00Z/2022-01-17T00:00:00Z",
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
-            "identifier": "C1000000006-CDDIS",
             "description": "Satellite and receiver clock products derived from analysis of Global Navigation Satellite System (GNSS) data. These products are the generated by analysis centers in support of the International GNSS Service (IGS) and combined by the IGS analysis coordinator to form the official IGS real-time clock product (daily). This product is used for comparison purposes.",
-            "title": "CDDIS_GNSS_products_ionosphere_final",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -537024,142 +537007,134 @@
                     "title": "Download this dataset"
                 }
             ],
+            "identifier": "C1000000006-CDDIS",
+            "issued": "1998-05-01",
+            "keyword": [
+                "nasa"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1000000006-CDDIS.html",
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
+            "temporal": "2008-10-05T00:00:00Z/2022-01-17T00:00:00Z",
             "theme": [
                 "IGS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "CDDIS_GNSS_products_ionosphere_final"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.7265/N5BC3WGR",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Snowchange Oral History - Work Among the Kolyma River Indigenous Societies in Siberia, Russia, Version 1. Version 1. Archived by National Aeronautics and Space Administration, U.S. Government, National Snow and Ice Data Center. https://doi.org/10.7265/N5BC3WGR.",
-            "issued": "1930-01-01",
-            "temporal": "1930-01-01T00:00:00Z/2009-12-31T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2009-12-31",
-            "keyword": [
-                "animal science",
-                "boundaries",
-                "cryosphere",
-                "earth science",
-                "biological classification",
-                "human dimensions",
-                "economic resources",
-                "environmental impacts",
-                "infrastructure",
-                "land surface",
-                "land use/land cover",
-                "agriculture",
-                "animal commodities",
-                "frozen ground",
-                "animals/vertebrates"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Tero Mustonen",
                 "hasEmail": "mailto:tero@snowchange.org"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NSIDC"
-            },
-            "identifier": "C1386206314-NSIDCV0",
             "description": "This data set includes oral history accounts from Indigenous people participating in the Snowchange project in Siberia, Russia. It provides geographic and environmental information from residents of two Indigenous Chukchi communities practicing seasonal nomadic reindeer herding and other subsistence activities that are being affected by climate change in Republic of Sakha-Yakutia, Siberia, in the Russian Federation.",
-            "title": "Snowchange Oral History - Work Among the Kolyma River Indigenous Societies in Siberia, Russia, Version 1",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.7265%2FN5BC3WGR",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.7265%2FN5BC3WGR",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://eloka-arctic.org/communities/russia/index.html",
-                    "description": "Product website where you can access the data.",
                     "@type": "dcat:Distribution",
+                    "description": "Product website where you can access the data.",
+                    "downloadURL": "http://eloka-arctic.org/communities/russia/index.html",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://eloka-arctic.org/communities/russia/index.html",
-                    "description": "Product website where you can access the data.",
                     "@type": "dcat:Distribution",
+                    "description": "Product website where you can access the data.",
+                    "downloadURL": "http://eloka-arctic.org/communities/russia/index.html",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.7265/N5BC3WGR",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.7265/N5BC3WGR",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.7265/N5BC3WGR",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.7265/N5BC3WGR",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C1386206314-NSIDCV0",
+            "issued": "1930-01-01",
+            "keyword": [
+                "animal science",
+                "boundaries",
+                "cryosphere",
+                "earth science",
+                "biological classification",
+                "human dimensions",
+                "economic resources",
+                "environmental impacts",
+                "infrastructure",
+                "land surface",
+                "land use/land cover",
+                "agriculture",
+                "animal commodities",
+                "frozen ground",
+                "animals/vertebrates"
+            ],
+            "landingPage": "https://doi.org/10.7265/N5BC3WGR",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2009-12-31",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NSIDC"
+            },
             "spatial": "153.38806 66.85056 164.74167 71.24028",
+            "temporal": "1930-01-01T00:00:00Z/2009-12-31T23:59:59.999Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Snowchange Oral History - Work Among the Kolyma River Indigenous Societies in Siberia, Russia, Version 1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "issue-identification": "MAM06S0",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1236350974-GES_DISC.html",
             "citation": "MODIS Science Team; Dr. Bo-Cai Gao, Dr. Paul Menzel, Dr. Michael King. 2006-10-01. MAM06S0. Version 002. MODIS/Aqua Clouds 1km and 5km 5-Min L2 Swath Subset along MLS. Greenbelt, MD, USA. MAM06S0. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://disc.gsfc.nasa.gov/datacollection/MAM06S0_002.html. Digital Science Data.",
-            "issued": "2004-08-08",
-            "temporal": "2004-08-08T00:00:00Z/2008-01-11T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2008-01-11",
-            "keyword": [
-                "ngda",
-                "national geospatial data asset",
-                "earth science",
-                "clouds",
-                "atmosphere"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "ANDREY SAVTCHENKO",
                 "hasEmail": "mailto:Andrey.Savtchenko@nasa.gov"
             },
+            "creator": "MODIS Science Team; Dr. Bo-Cai Gao, Dr. Paul Menzel, Dr. Michael King",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C1236350974-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "This is the MODIS/Aqua subset along MLS field of view track. The goal of the subset is to select and return MODIS data that are within +-100 km across the MLS track. I.e. the resultant MODIS subset swath is sought to be about 200 km cross-track. However, the original MYD06_L2 has data of 5- and 1-km pixels. Thus, MAM06S0 cross-track width is 41- and 201-pixels, depending on the parameter. Along-track, all MODIS pixels from the original product are preserved.\n      \nIn the standard product, the level-2 MODIS cloud product consists of cloud optical and physical parameters. These parameters are derived using remotely sensed infrared, visible and near infrared solar reflected radiances. MODIS infrared channel radiances are used to derive cloud top temperature, cloud top height, effective emissivity, cloud phase (ice vs. water, opaque vs. non-opaque), and cloud fraction under both daytime and  nighttime conditions. MODIS visible radiances are used to derive cloud optical thickness and effective particle radius and cloud shadow effects. Near infrared solar reflected radiance provides additional information in the retrieval of cloud particle phase (ice vs. water, clouds vs. snow).\n      \n(The shortname for this product is MAM06S0).",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "MAM06S0",
-            "creator": "MODIS Science Team; Dr. Bo-Cai Gao, Dr. Paul Menzel, Dr. Michael King",
-            "title": "MODIS/Aqua Clouds 1km and 5km 5-Min L2 Swath Subset along MLS V002 (MAM06S0) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/MAM06S0_002.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -537168,73 +537143,112 @@
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/MAM06S0_002.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/MAM06S0_002.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://atrain.gesdisc.eosdis.nasa.gov/data/MAM/MAM06S0.002/",
-                    "description": "Access the data via HTTPS",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS",
+                    "downloadURL": "https://atrain.gesdisc.eosdis.nasa.gov/data/MAM/MAM06S0.002/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ladsweb.nascom.nasa.gov",
-                    "description": "View standard full-sized MODIS data availability.",
                     "@type": "dcat:Distribution",
+                    "description": "View standard full-sized MODIS data availability.",
+                    "downloadURL": "https://ladsweb.nascom.nasa.gov",
+                    "mediaType": "text/html",
                     "title": "View information related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://modis.gsfc.nasa.gov/",
-                    "description": "MODIS Science Team",
                     "@type": "dcat:Distribution",
+                    "description": "MODIS Science Team",
+                    "downloadURL": "https://modis.gsfc.nasa.gov/",
+                    "mediaType": "text/html",
                     "title": "View information related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://mcst.gsfc.nasa.gov/",
-                    "description": "MODIS Characterization Support Team (MCST)",
                     "@type": "dcat:Distribution",
+                    "description": "MODIS Characterization Support Team (MCST)",
+                    "downloadURL": "https://mcst.gsfc.nasa.gov/",
+                    "mediaType": "text/html",
                     "title": "View information related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://www.cloudsat.cira.colostate.edu/",
-                    "description": "CloudSat Data Processing Center",
                     "@type": "dcat:Distribution",
+                    "description": "CloudSat Data Processing Center",
+                    "downloadURL": "http://www.cloudsat.cira.colostate.edu/",
+                    "mediaType": "text/html",
                     "title": "View information related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://modis-atmos.gsfc.nasa.gov/data-issues/cloud",
-                    "description": "Quality Assurance for the original product.",
                     "@type": "dcat:Distribution",
+                    "description": "Quality Assurance for the original product.",
+                    "downloadURL": "https://modis-atmos.gsfc.nasa.gov/data-issues/cloud",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/MAM06S0_002.png",
+            "identifier": "C1236350974-GES_DISC",
+            "issue-identification": "MAM06S0",
+            "issued": "2004-08-08",
+            "keyword": [
+                "ngda",
+                "national geospatial data asset",
+                "earth science",
+                "clouds",
+                "atmosphere"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1236350974-GES_DISC.html",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2008-01-11",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
+            },
+            "release-place": "Greenbelt, MD, USA",
+            "series-name": "MAM06S0",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2004-08-08T00:00:00Z/2008-01-11T23:59:59.999Z",
             "theme": [
                 "ATDD",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "MODIS/Aqua Clouds 1km and 5km 5-Min L2 Swath Subset along MLS V002 (MAM06S0) at GES DISC"
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
+            "description": "NASA Financial Budget Documents, Strategic Plans and Performance Reports for fiscal year 2001.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "FY01 NASA Budget Package",
+                    "downloadURL": "ftp://ftp.hq.nasa.gov/pub/pao/budget/2001/lg_budget_pkg.pdf",
+                    "mediaType": "application/pdf",
+                    "title": "FY01 NASA Budget Package"
+                }
+            ],
+            "identifier": "OCIO-Fitara-99",
             "issued": "2001-05-01",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
             "keyword": [
                 "strategic",
                 "finance",
@@ -537243,105 +537257,70 @@
                 "financial",
                 "budget"
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
-            "identifier": "OCIO-Fitara-99",
-            "description": "NASA Financial Budget Documents, Strategic Plans and Performance Reports for fiscal year 2001.",
-            "title": "NASA Financial Budget Documents, Strategic Plans and Performance Reports 2001: NASA Budget Package",
-            "programCode": [
-                "026:046"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "ftp://ftp.hq.nasa.gov/pub/pao/budget/2001/lg_budget_pkg.pdf",
-                    "description": "FY01 NASA Budget Package",
-                    "@type": "dcat:Distribution",
-                    "title": "FY01 NASA Budget Package"
-                }
-            ],
-            "accrualPeriodicity": "R/P1Y",
             "theme": [
                 "Management/Operations"
-            ]
+            ],
+            "title": "NASA Financial Budget Documents, Strategic Plans and Performance Reports 2001: NASA Budget Package"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-5-DDR-TAXONOMY-V1.0",
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
+            "description": "This dataset provides asteroid taxonomic classifications of the Tholen, Barucci, and Tedesco classification systems.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-5-ddr-taxonomy-v1.0_bike-94fb",
+            "issued": "2021-05-21",
+            "keyword": [
+                "asteroid",
+                "support archives"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-5-DDR-TAXONOMY-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-5-ddr-taxonomy-v1.0_bike-94fb",
-            "description": "This dataset provides asteroid taxonomic classifications of the Tholen, Barucci, and Tedesco classification systems.",
-            "title": "ASTEROID TAXONOMY V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ASTEROID TAXONOMY V1.0"
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
-            ],
-            "keyword": [
-                "ingest",
-                "catalog",
-                "pds",
-                "tool"
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
-            "identifier": "NASA-591",
             "description": "Software Release Catalog Ingest Tool (1.0.0)",
-            "title": "PDS Catalog Ingest Tool Software Release Catalog Ingest Tool (1.0.0)",
-            "programCode": [
-                "026:005"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -537349,259 +537328,289 @@
                     "mediaType": "application/html"
                 }
             ],
-            "accrualPeriodicity": "irregular",
+            "identifier": "NASA-591",
+            "issued": "2018-06-26",
+            "keyword": [
+                "ingest",
+                "catalog",
+                "pds",
+                "tool"
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
+            "title": "PDS Catalog Ingest Tool Software Release Catalog Ingest Tool (1.0.0)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ASDC/SUBORBITAL/TOTE-VOTE_TraceGas_AircraftInSitu_DC8_Data_1",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2023-10-17. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/ASDC/SUBORBITAL/TOTE-VOTE_TraceGas_AircraftInSitu_DC8_Data_1.",
-            "issued": "1995-12-06",
-            "temporal": "1995-12-03T00:00:00Z/1996-02-20T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "1996-02-19",
-            "keyword": [
-                "earth science",
-                "atmospheric chemistry",
-                "atmosphere"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Andrew Weinheimer",
                 "hasEmail": "mailto:wein@ucar.edu"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/LARC/SD/ASDC"
-            },
-            "identifier": "C2736766511-LARC_ASDC",
             "description": "TOTE-VOTE_TraceGas_AircraftInSitu_DC8_Data_1 is the in situ trace gas data collected onboard the DC-8 aircraft as part of the Tropical Ozone Transport Experiment \u2013 Vortex Ozone Transport Experiment (TOTE-VOTE) campaign. Data collected by the DACOM, LICOR, and chemiluminescence are featured in this product. Data collection is completed.\r\nThe Tropical Ozone Transport Experiment \u2013 Vortex Ozone Transport Experiment (TOTE-VOTE) campaign was conducted by NASA from December 1995 to February 1996. TOTE-VOTE took place in the Pacific region with the goal of gaining a better understanding of background transport processes from tropical/polar regions to midlatitudes. Nineteen flights were conducted using the NASA DC-8 aircraft and balloon sondes with the purpose of measuring the transport of filaments of air moved in or out of the arctic polar vortex and the tropical stratospheric reservoir. TOTE-VOTE also utilized ground-based instruments along with aircrafts.\r\n\r\nVarious instrumentation was used during TOTE-VOTE in order to achieve the mission objectives. The DC-8 aircraft was equipped with the NCAR NOxyO3 instrument, the NASA Langley Airborne Differential Absorption Lidar (DIAL) system, the Forward Scattering Spectrometer Probe (FSSP), the Microwave Temperature Profiler (MTP), the Multiple-Angle Aerosol Spectrometer Probe (MASP), and the diode laser spectrometer system, historically known as the Differential Absorption Carbon monOxide Measurement (DACOM). The NCAR NOxyO3 is a type of 4-channel chemiluminescence instrument that was used to quantify NOx (NO and NO2), NOy (total reactive nitrogen), and ozone (O3) in the air. The DIAL system used four lasers to make DIAL O3 profiles, along with collecting data on aerosol backscattering, aerosol depolarization ratio, aerosol extinction, and aerosol optical depth. The FSSP is an optical particle counter that measured particle size distribution. The MTP is a passive microwave radiometer that measured natural thermal emissions and was used during TOTE-VOTE to record temperature. The MASP spectrometer collected in-situ measurements of particle concentration, particle size distribution, and particle extinction. Along with the MASP\u2019s in-situ measurements, the DACOM spectrometer utilized three diode lasers at different wavelengths to take in-situ measurements of N2O, CO, CH4, and CO2 for TOTE-VOTE. Ground-based instruments collected lidar data while balloon sondes gathered information on wind direction, wind speed, atmospheric pressure, and air temperature.",
-            "title": "Tropical Ozone Transport Experiment \u2013 Vortex Ozone Transport Experiment (TOTE-VOTE) DC-8 In Situ Trace Gas Data",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC%2FSUBORBITAL%2FTOTE-VOTE_TraceGas_AircraftInSitu_DC8_Data_1",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC%2FSUBORBITAL%2FTOTE-VOTE_TraceGas_AircraftInSitu_DC8_Data_1",
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
-                    "downloadURL": "https://science-data.larc.nasa.gov/lidar/tvo/totevote.html",
-                    "description": "TOTE-VOTE DIAL Aerosol and Ozone Distribution Images",
                     "@type": "dcat:Distribution",
+                    "description": "TOTE-VOTE DIAL Aerosol and Ozone Distribution Images",
+                    "downloadURL": "https://science-data.larc.nasa.gov/lidar/tvo/totevote.html",
+                    "mediaType": "text/html",
                     "title": "View the primary investigator's documentation for this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://agupubs.onlinelibrary.wiley.com/doi/abs/10.1029/2000JD900648",
-                    "description": "Aircraft observations of thin cirrus clouds near the tropical tropopause",
                     "@type": "dcat:Distribution",
+                    "description": "Aircraft observations of thin cirrus clouds near the tropical tropopause",
+                    "downloadURL": "https://agupubs.onlinelibrary.wiley.com/doi/abs/10.1029/2000JD900648",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://agupubs.onlinelibrary.wiley.com/doi/abs/10.1029/1998GL900066",
-                    "description": "The in-flight sensitivity of Gold-Tube NOy converters to HCN",
                     "@type": "dcat:Distribution",
+                    "description": "The in-flight sensitivity of Gold-Tube NOy converters to HCN",
+                    "downloadURL": "https://agupubs.onlinelibrary.wiley.com/doi/abs/10.1029/1998GL900066",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://agupubs.onlinelibrary.wiley.com/doi/abs/10.1029/97JD03129",
-                    "description": "Lidar temperature measurements during the Tropical Ozone Transport Experiment (TOTE)/Vortex Ozone Transport Experiment (VOTE) mission",
                     "@type": "dcat:Distribution",
+                    "description": "Lidar temperature measurements during the Tropical Ozone Transport Experiment (TOTE)/Vortex Ozone Transport Experiment (VOTE) mission",
+                    "downloadURL": "https://agupubs.onlinelibrary.wiley.com/doi/abs/10.1029/97JD03129",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://agupubs.onlinelibrary.wiley.com/doi/abs/10.1029/98GL00231",
-                    "description": "Correlative stratospheric ozone measurements with the airborne UV DIAL system during TOTE/VOTE",
                     "@type": "dcat:Distribution",
+                    "description": "Correlative stratospheric ozone measurements with the airborne UV DIAL system during TOTE/VOTE",
+                    "downloadURL": "https://agupubs.onlinelibrary.wiley.com/doi/abs/10.1029/98GL00231",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/TOTE-VOTE/TraceGas_AircraftInSitu_DC8_Data_1/",
-                    "description": "ASDC Direct Data Download for TOTE-VOTE_TraceGas_AircraftInSitu_DC8_Data_1",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for TOTE-VOTE_TraceGas_AircraftInSitu_DC8_Data_1",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/TOTE-VOTE/TraceGas_AircraftInSitu_DC8_Data_1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2736766511-LARC_ASDC",
-                    "description": "Earthdata Search for TOTE-VOTE_TraceGas_AircraftInSitu_DC8_Data_1",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for TOTE-VOTE_TraceGas_AircraftInSitu_DC8_Data_1",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2736766511-LARC_ASDC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/ASDC/SUBORBITAL/TOTE-VOTE_TraceGas_AircraftInSitu_DC8_Data_1",
-                    "description": "DOI for TOTE-VOTE_TraceGas_AircraftInSitu_DC8_Data_1",
                     "@type": "dcat:Distribution",
+                    "description": "DOI for TOTE-VOTE_TraceGas_AircraftInSitu_DC8_Data_1",
+                    "downloadURL": "https://doi.org/10.5067/ASDC/SUBORBITAL/TOTE-VOTE_TraceGas_AircraftInSitu_DC8_Data_1",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 }
             ],
+            "identifier": "C2736766511-LARC_ASDC",
+            "issued": "1995-12-06",
+            "keyword": [
+                "earth science",
+                "atmospheric chemistry",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.5067/ASDC/SUBORBITAL/TOTE-VOTE_TraceGas_AircraftInSitu_DC8_Data_1",
+            "language": [
+                "en-US"
+            ],
+            "modified": "1996-02-19",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/LARC/SD/ASDC"
+            },
             "spatial": "<?xml version=\"1.0\" encoding=\"UTF-8\"?><gml:Polygon xmlns:gml=\"http://www.opengis.net/gml/3.2\" srsName=\"EPSG:9825\"><gml:outerBoundaryIs><gml:LinearRing><gml:posList>-23.1 -180.0 -23.1 180.0 90.0 180.0 90.0 -180.0 -23.1 -180.0</gml:posList></gml:LinearRing></gml:outerBoundaryIs><gml:innerBoundaryIs></gml:innerBoundaryIs></gml:Polygon>",
+            "temporal": "1995-12-03T00:00:00Z/1996-02-20T00:00:00Z",
             "theme": [
                 "TOTE-VOTE",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Tropical Ozone Transport Experiment \u2013 Vortex Ozone Transport Experiment (TOTE-VOTE) DC-8 In Situ Trace Gas Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/MODIS/MCD43D28.061",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Crystal Schaaf, Zhuosen Wang. 2021-02-22. MODIS/Terra+Aqua BRDF/Albedo Parameter1 Shortwave Daily L3 Global 30ArcSec CMG V061. Sioux Falls, South Dakota, USA. Archived by National Aeronautics and Space Administration, U.S. Government, NASA EOSDIS Land Processes Distributed Active Archive Center. https://doi.org/10.5067/MODIS/MCD43D28.061. https://doi.org/10.5067/MODIS/MCD43D28.061. The DOI landing page provides citations in APA and Chicago styles..",
-            "issued": "2021-02-22",
-            "temporal": "2000-02-16T00:00:00Z/2024-05-20T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2021-02-22",
-            "keyword": [
-                "surface radiative properties",
-                "land surface",
-                "national geospatial data asset",
-                "ngda",
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
-            "identifier": "C2540268581-LPCLOUD",
-            "description": "The MCD43D28 Version 6.1 Bidirectional Reflectance Distribution Function and Albedo (BRDF/Albedo) Model Parameter dataset is produced daily using 16 days of Terra and Aqua Moderate Resolution Imaging Spectroradiometer (MODIS) data at 30 arc second (1,000 meter) resolution. Data are temporally weighted to the ninth day which is reflected in the Julian date in the file name. This Climate Modeling Grid (CMG) product covers the entire globe for use in climate simulation models. Due to the large file size, each MCD43D product contains just one data layer. Each of the three model parameters (isotropic, volumetric, and geometric) for each of the MODIS bands 1 through 7 and the visible, near infrared (NIR), and shortwave bands included in MCD43C1 (https://doi.org/10.5067/MODIS/MCD43C1.061) are stored in a separate file as MCD43D01 through MCD43D30. \r\n\r\nMCD43D28 is the BRDF isotropic parameter for the MODIS shortwave broadband. The isotropic parameter, in conjunction with the volumetric and geometric parameters, is used to derive the BRDF/Albedo values for the MODIS shortwave broadband.\r\n\r\nImprovements/Changes from Previous Versions\r\n\r\n* The Version 6.1 Level-1B (L1B) products have been improved by undergoing various calibration changes that include: changes to the response-versus-scan angle (RVS) approach that affects reflectance bands for Aqua and Terra MODIS, corrections to adjust for the optical crosstalk in Terra MODIS infrared (IR) bands, and corrections to the Terra MODIS forward look-up table (LUT) update for the period 2012 - 2017.\r\n* A polarization correction has been applied to the L1B Reflective Solar Bands (RSB).",
-            "release-place": "Sioux Falls, South Dakota, USA",
             "creator": "Crystal Schaaf, Zhuosen Wang",
-            "title": "MODIS/Terra+Aqua BRDF/Albedo Parameter1 Shortwave Daily L3 Global 30ArcSec CMG V061",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The MCD43D28 Version 6.1 Bidirectional Reflectance Distribution Function and Albedo (BRDF/Albedo) Model Parameter dataset is produced daily using 16 days of Terra and Aqua Moderate Resolution Imaging Spectroradiometer (MODIS) data at 30 arc second (1,000 meter) resolution. Data are temporally weighted to the ninth day which is reflected in the Julian date in the file name. This Climate Modeling Grid (CMG) product covers the entire globe for use in climate simulation models. Due to the large file size, each MCD43D product contains just one data layer. Each of the three model parameters (isotropic, volumetric, and geometric) for each of the MODIS bands 1 through 7 and the visible, near infrared (NIR), and shortwave bands included in MCD43C1 (https://doi.org/10.5067/MODIS/MCD43C1.061) are stored in a separate file as MCD43D01 through MCD43D30. \r\n\r\nMCD43D28 is the BRDF isotropic parameter for the MODIS shortwave broadband. The isotropic parameter, in conjunction with the volumetric and geometric parameters, is used to derive the BRDF/Albedo values for the MODIS shortwave broadband.\r\n\r\nImprovements/Changes from Previous Versions\r\n\r\n* The Version 6.1 Level-1B (L1B) products have been improved by undergoing various calibration changes that include: changes to the response-versus-scan angle (RVS) approach that affects reflectance bands for Aqua and Terra MODIS, corrections to adjust for the optical crosstalk in Terra MODIS infrared (IR) bands, and corrections to the Terra MODIS forward look-up table (LUT) update for the period 2012 - 2017.\r\n* A polarization correction has been applied to the L1B Reflective Solar Bands (RSB).",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMODIS%2FMCD43D28.061",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMODIS%2FMCD43D28.061",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "application/x-hdf",
-                    "downloadURL": "https://e4ftl01.cr.usgs.gov/MOTA/MCD43D28.061/",
-                    "description": "LP DAAC Data Pool provides direct access to available products via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "LP DAAC Data Pool provides direct access to available products via HTTPS.",
+                    "downloadURL": "https://e4ftl01.cr.usgs.gov/MOTA/MCD43D28.061/",
+                    "mediaType": "application/x-hdf",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "application/x-hdf",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=C2540268581-LPCLOUD",
-                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=C2540268581-LPCLOUD",
+                    "mediaType": "application/x-hdf",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/MODIS/MCD43D28.061",
-                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
+                    "downloadURL": "https://doi.org/10.5067/MODIS/MCD43D28.061",
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
-                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/filespec/MODIS/61/MCD43D28",
-                    "description": "The File Specification provides a description of the product file including Scientific Data Sets and their attributes.",
                     "@type": "dcat:Distribution",
+                    "description": "The File Specification provides a description of the product file including Scientific Data Sets and their attributes.",
+                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/filespec/MODIS/61/MCD43D28",
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
-                    "downloadURL": "https://opendap.cr.usgs.gov/opendap/hyrax/DP137/MOTA/MCD43D28.061/contents.html",
-                    "description": "Access data via Open-source Project for a Network Data Access Protocol",
                     "@type": "dcat:Distribution",
+                    "description": "Access data via Open-source Project for a Network Data Access Protocol",
+                    "downloadURL": "https://opendap.cr.usgs.gov/opendap/hyrax/DP137/MOTA/MCD43D28.061/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 }
             ],
+            "identifier": "C2540268581-LPCLOUD",
+            "issued": "2021-02-22",
+            "keyword": [
+                "surface radiative properties",
+                "land surface",
+                "national geospatial data asset",
+                "ngda",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/MODIS/MCD43D28.061",
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
+            "title": "MODIS/Terra+Aqua BRDF/Albedo Parameter1 Shortwave Daily L3 Global 30ArcSec CMG V061"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://nasa3d.arc.nasa.gov/detail/mkiii-suit",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2018-06-25",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
-            "references": [
-                "http://www.nasa.gov/mission_pages/shuttle/main/index.html"
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Beth Beck",
+                "hasEmail": "mailto:beth.beck@nasa.gov"
+            },
+            "description": "Both the JSC Mark III and the ARC AX-5 suit have been designed to operate at a pressure of 8.3 psi. Current space shuttle spacesuits operate at 4.3 psi and require a time-consuming pre-breathing operation prior to the beginning of any spacewalk. Polygons: 34892 Vertices: 35222",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://nasa3d.arc.nasa.gov/shared_assets/models/mkiii-suit/MKIII.3DS.zip",
+                    "mediaType": "image/x-3ds"
+                }
             ],
+            "identifier": "NASA-378",
+            "issued": "2018-06-25",
             "keyword": [
                 "mark iii",
                 "suit",
@@ -537610,367 +537619,367 @@
                 "astronaut",
                 "3d model"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Beth Beck",
-                "hasEmail": "mailto:beth.beck@nasa.gov"
-            },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Aeronautics and Space Administration"
-            },
-            "identifier": "NASA-378",
-            "description": "Both the JSC Mark III and the ARC AX-5 suit have been designed to operate at a pressure of 8.3 psi. Current space shuttle spacesuits operate at 4.3 psi and require a time-consuming pre-breathing operation prior to the beginning of any spacewalk. Polygons: 34892 Vertices: 35222",
-            "title": "NASA 3D Models: Mark III Spacesuit",
+            "landingPage": "http://nasa3d.arc.nasa.gov/detail/mkiii-suit",
+            "modified": "2020-01-29",
             "programCode": [
                 "026:045",
                 "026:046"
             ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://nasa3d.arc.nasa.gov/shared_assets/models/mkiii-suit/MKIII.3DS.zip",
-                    "mediaType": "image/x-3ds"
-                }
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Aeronautics and Space Administration"
+            },
+            "references": [
+                "http://www.nasa.gov/mission_pages/shuttle/main/index.html"
             ],
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Management/Operations"
-            ]
+            ],
+            "title": "NASA 3D Models: Mark III Spacesuit"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://techport.nasa.gov/view/11697",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2011-10-01",
-            "temporal": "2011-10-01T00:00:00Z/2014-09-01T00:00:00Z",
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
-                "kennedy space center",
-                "project"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Nancy Zeitlin",
                 "hasEmail": "mailto:nancy.p.zeitlin@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Human Exploration and Operations Mission Directorate"
-            },
-            "identifier": "TECHPORT_11697",
             "description": "&lt;p&gt;The purpose of this project is to develop state-of-the-art, green precision cleaning technologies for NASA&amp;rsquo;s 21&lt;sup&gt;st&lt;/sup&gt; Century Launch Complex thus eliminating long-term environmental costs to the Program.&amp;nbsp; Precision cleaning is of critical importance in the aerospace industry.&amp;nbsp; Failure to clean to specified levels may result in problems ranging from impaired performance to catastrophic failure.&amp;nbsp;&lt;/p&gt;&lt;p&gt;Of particular concern is the cleaning of systems containing strong oxidizers such as liquid oxygen (LOX) or hypergolic fuels.&amp;nbsp; Currently, precision cleaning at Kennedy Space Center is performed using dual-solvent process in which the first solvent, Vertrel MCA, is used to clean the component and a second solvent, HFE-7100, is used as a final rinse and analytical test fluid.&amp;nbsp; Highly fluorinated compounds such as those used in Vertrel MCA are extremely persistent in the environment and are potent greenhouse gases. Continued use of this or similar solvents will lead to high remediation costs that must be carried by the Program for years to come.&lt;/p&gt;&lt;p&gt;Historically, precision cleaning has used chlorofluorocarbons (CFCs), such as Freon, because it was non-toxic and performed extremely wll.&amp;nbsp; When Freon, and other CFCs, were banned due to their harmful environmental effects, new solvents were identified that were similar compounds but were not yet regulated.&amp;nbsp; Eventually, these solvents also become regulated and unavailable for use.&amp;nbsp; This project specifically did not consider halogenated solvents in order to find solvents or technologies that would not face future environmental regulations.&lt;/p&gt;",
-            "title": "Alternative Solvents through Green Chemistry Project",
-            "programCode": [
-                "026:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "http://techport.nasa.gov/xml-api/11697",
                     "mediaType": "application/xml"
                 }
-            ]
+            ],
+            "identifier": "TECHPORT_11697",
+            "issued": "2011-10-01",
+            "keyword": [
+                "active",
+                "kennedy space center",
+                "project"
+            ],
+            "landingPage": "http://techport.nasa.gov/view/11697",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Human Exploration and Operations Mission Directorate"
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
+            "temporal": "2011-10-01T00:00:00Z/2014-09-01T00:00:00Z",
+            "title": "Alternative Solvents through Green Chemistry Project"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MEX-M-MARSIS-5-DDR-ELEDENS%2FBMAG-EXT4V1.0",
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
+            "description": "This data set tabulates local electron densities and local magnetic field strengths magnetic field strengths obtained from Mars Advanced Radar for Subsurface and Ionosphere Sounding (MARSIS) Active Ionospheric Sounding (AIS) mode ionograms.  The electron density is obtained by measuring the increment in frequency between the plasma frequency harmonics, visible as bright vertical lines at low frequency and delay time in many MARSIS ionograms.  Similarly, the local magnetic field strength is found by measuring the difference in delay time between electron cyclotron echoes, visible as bright horizontal lines at low frequency on many ionograms.  Both the measured quantity and the derived result are included in the archive product.  We also include a data quality flag giving the impression of the archivist as to how reliable each result is.  This archive product includes only data from the nominal mission, which starts about orbit 1850 and ends on orbit 2539.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mex-m-marsis-5-ddr-eledens-bmag-ext4v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "mars",
+                "mars express"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MEX-M-MARSIS-5-DDR-ELEDENS%2FBMAG-EXT4V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mex-m-marsis-5-ddr-eledens-bmag-ext4v1.0",
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
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-2-PRL-67PCHURYUMOV-M07B-V1.0",
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
+            "description": "This data set contains raw EDR images acquired by the OSIRIS Wide Angle\nCamera during the prelanding phase of the Rosetta mission at the comet 67P,\ncovering the period from 2014-09-16 to 2014-09-23.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-2-prl-67pchuryumov-m07b-v1.0_bitr-2wih",
+            "issued": "2018-06-26",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-2-PRL-67PCHURYUMOV-M07B-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-2-prl-67pchuryumov-m07b-v1.0_bitr-2wih",
-            "description": "This data set contains raw EDR images acquired by the OSIRIS Wide Angle\nCamera during the prelanding phase of the Rosetta mission at the comet 67P,\ncovering the period from 2014-09-16 to 2014-09-23.",
-            "title": "ROSETTA-ORBITER COMET PRELANDING OSIWAC 2 EDR MTP 007B V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "ROSETTA-ORBITER COMET PRELANDING OSIWAC 2 EDR MTP 007B V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://c3.nasa.gov/dashlink/resources/634/",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2012-12-04",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
-            "keyword": [
-                "nasa",
-                "ames",
-                "dashlink"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Bryan Matthews",
                 "hasEmail": "mailto:bryan.l.matthews@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Dashlink"
-            },
-            "identifier": "DASHLINK_634",
             "description": "The following zip files contain individual flight recorded data in Matlab file format. There are 186 parameters each with a data structure that contains the following:\r\n\r\n<pre>\r\n-sensor recordings\r\n-sampling rate\r\n-units\r\n-parameter description\r\n-parameter ID\r\n</pre>",
-            "title": "Flight Data For Tail 656",
-            "programCode": [
-                "026:029"
-            ],
             "distribution": [
                 {
-                    "mediaType": "application/zip",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Tail_656_1.zip",
-                    "description": "Tail 656 Set 1",
                     "@type": "dcat:Distribution",
+                    "description": "Tail 656 Set 1",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Tail_656_1.zip",
+                    "mediaType": "application/zip",
                     "title": "Tail_656_1.zip"
                 },
                 {
-                    "mediaType": "application/zip",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Tail_656_2.zip",
-                    "description": "Tail 656 Set 2",
                     "@type": "dcat:Distribution",
+                    "description": "Tail 656 Set 2",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Tail_656_2.zip",
+                    "mediaType": "application/zip",
                     "title": "Tail_656_2.zip"
                 },
                 {
-                    "mediaType": "application/zip",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Tail_656_3.zip",
-                    "description": "Tail 656 Set 3",
                     "@type": "dcat:Distribution",
+                    "description": "Tail 656 Set 3",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Tail_656_3.zip",
+                    "mediaType": "application/zip",
                     "title": "Tail_656_3.zip"
                 },
                 {
-                    "mediaType": "application/zip",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Tail_656_4.zip",
-                    "description": "Tail 656 Set 4",
                     "@type": "dcat:Distribution",
+                    "description": "Tail 656 Set 4",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Tail_656_4.zip",
+                    "mediaType": "application/zip",
                     "title": "Tail_656_4.zip"
                 },
                 {
-                    "mediaType": "application/zip",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Tail_656_5.zip",
-                    "description": "Tail 656 Set 5",
                     "@type": "dcat:Distribution",
+                    "description": "Tail 656 Set 5",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Tail_656_5.zip",
+                    "mediaType": "application/zip",
                     "title": "Tail_656_5.zip"
                 },
                 {
-                    "mediaType": "application/zip",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Tail_656_6.zip",
-                    "description": "Tail 656 Set 6",
                     "@type": "dcat:Distribution",
+                    "description": "Tail 656 Set 6",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Tail_656_6.zip",
+                    "mediaType": "application/zip",
                     "title": "Tail_656_6.zip"
                 },
                 {
-                    "mediaType": "application/zip",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Tail_656_7.zip",
-                    "description": "Tail 656 Set 7",
                     "@type": "dcat:Distribution",
+                    "description": "Tail 656 Set 7",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Tail_656_7.zip",
+                    "mediaType": "application/zip",
                     "title": "Tail_656_7.zip"
                 },
                 {
-                    "mediaType": "application/zip",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Tail_656_8.zip",
-                    "description": "Tail_656 Set 8\n",
                     "@type": "dcat:Distribution",
+                    "description": "Tail_656 Set 8\n",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Tail_656_8.zip",
+                    "mediaType": "application/zip",
                     "title": "Tail_656_8.zip"
                 }
             ],
-            "accrualPeriodicity": "irregular"
+            "identifier": "DASHLINK_634",
+            "issued": "2012-12-04",
+            "keyword": [
+                "nasa",
+                "ames",
+                "dashlink"
+            ],
+            "landingPage": "https://c3.nasa.gov/dashlink/resources/634/",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:029"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Dashlink"
+            },
+            "title": "Flight Data For Tail 656"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-4-ESC3-67P-M19-STR-REFL-V1.0",
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
+            "description": "This CODMAC level 4 data set contains solar stray light corrected, radiometric calibrated and geometric distortion corrected (resampled) image data in in reflectance units (normalized and thus without unit), acquired by the OSIRIS Narrow Angle Camera on the Rosetta spacecraft during the COMET ESCORT 3 mission phase, covering the period from 2015-07-28T23:25:00.000 to 2015-08-25T23:24:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V1.0 is the first version of this dataset: Lien corrected dataset after October 2018 PSA/PDS external peer review.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-4-esc3-67p-m19-str-refl-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-4-ESC3-67P-M19-STR-REFL-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-4-esc3-67p-m19-str-refl-v1.0",
-            "description": "This CODMAC level 4 data set contains solar stray light corrected, radiometric calibrated and geometric distortion corrected (resampled) image data in in reflectance units (normalized and thus without unit), acquired by the OSIRIS Narrow Angle Camera on the Rosetta spacecraft during the COMET ESCORT 3 mission phase, covering the period from 2015-07-28T23:25:00.000 to 2015-08-25T23:24:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V1.0 is the first version of this dataset: Lien corrected dataset after October 2018 PSA/PDS external peer review.",
-            "title": "ROSETTA-ORBITER 67P OSINAC 4 ESC3-MTP019 RDR-STR-REFL V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P OSINAC 4 ESC3-MTP019 RDR-STR-REFL V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC2-0711-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 2 phase 2015-03-11 to 2015-06-30. It is a Global Gravity measurement at the comet 67P and covers the time 2015-04-16T06:02:40.000 to 2015-04-16T13:10:07.500.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc2-0711-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC2-0711-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc2-0711-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 2 phase 2015-03-11 to 2015-06-30. It is a Global Gravity measurement at the comet 67P and covers the time 2015-04-16T06:02:40.000 to 2015-04-16T13:10:07.500.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 2 0711 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 2 0711 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MEX-M-MRS-1%2F2%2F3-EXT3-3021-V1.0",
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
+            "description": "This is a Mars Express Radio Science data set, collected during the extended mission phase 2010-01-01 to 2012-12-31. It is a Global Gravity measurement and covers the time 2011-07-19T22:40:44.000 to 2011-07-19T23:05:10.949.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mex-m-mrs-1-2-3-ext3-3021-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "mars express",
+                "mars"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MEX-M-MRS-1%2F2%2F3-EXT3-3021-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mex-m-mrs-1-2-3-ext3-3021-v1.0",
-            "description": "This is a Mars Express Radio Science data set, collected during the extended mission phase 2010-01-01 to 2012-12-31. It is a Global Gravity measurement and covers the time 2011-07-19T22:40:44.000 to 2011-07-19T23:05:10.949.",
-            "title": "MARS EXPRESS MARS MRS 1/2/3\n                                     EXTENDED MISSION 3 3021 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "MARS EXPRESS MARS MRS 1/2/3\n                                     EXTENDED MISSION 3 3021 V1.0"
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
+            "description": "CRaTER, DLRE, LAMP, LEND, LOLA, LROC, RSS",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://pds.jpl.nasa.gov/tools/subscription_service/SS-20140314.shtml",
+                    "mediaType": "application/html"
+                }
             ],
+            "identifier": "NASA-448",
+            "issued": "2018-06-25",
             "keyword": [
                 "crater",
                 "lola",
@@ -537980,152 +537989,157 @@
                 "lamp",
                 "dlre"
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
-            "identifier": "NASA-448",
-            "description": "CRaTER, DLRE, LAMP, LEND, LOLA, LROC, RSS",
-            "title": "PDS Lunar Reconnaissance Orbiter Data Release 17",
-            "programCode": [
-                "026:005"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://pds.jpl.nasa.gov/tools/subscription_service/SS-20140314.shtml",
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
+            "title": "PDS Lunar Reconnaissance Orbiter Data Release 17"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC2-0776-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 2 phase 2015-03-11 to 2015-06-30. It is a Global Gravity measurement at the comet 67P and covers the time 2015-05-15T05:03:05.000 to 2015-05-15T07:01:20.500.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc2-0776-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC2-0776-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc2-0776-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 2 phase 2015-03-11 to 2015-06-30. It is a Global Gravity measurement at the comet 67P and covers the time 2015-05-15T05:03:05.000 to 2015-05-15T07:01:20.500.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 2 0776 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 2 0776 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MER1-M-MTES-4-EMR-V1.0",
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
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mer1-m-mtes-4-emr-v1.0_bj36-zvun",
+            "issued": "2018-06-26",
+            "keyword": [
+                "mars",
+                "mars exploration rover"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MER1-M-MTES-4-EMR-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mer1-m-mtes-4-emr-v1.0_bj36-zvun",
-            "description": "This archive contains Mars Exploration Rover Miniature Thermal Emission Spectrometer (Mini-TES) Emissivity Reduced Data Record (EMR) products and ancillary files. The Mini-TES EMR products archived on this volume are the original products used during mission operations by the Mars Exploration Rover project.",
-            "title": "MER1 MARS MINIATURE THERMAL EMISSION SPECTROMETER EMR V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "MER1 MARS MINIATURE THERMAL EMISSION SPECTROMETER EMR V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-X-RPCMAG-4-CVP-RESAMPLED-V9.0",
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
-                "checkout",
-                "international rosetta mission"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This dataset contains RESAMPLED DATA (CODMAC LEVEL 4) of the two\ncommissioning phases CVP1 and CVP2 and of the interference campaign  of the\nROSETTA orbiter magnetometer RPCMAG. Included are data from the time interval\nMarch 17, 2004 until October 14, 2004.\nThe current version of the dataset is V9.0.\nThe difference to the datasets of earlier versions is mainly a significantly\nimproved sensor temperature model, more detailed documentation about magnetic\ndisturbance sources, more data handling information for the user and\nalso an improved quality flagging system.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-x-rpcmag-4-cvp-resampled-v9.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "checkout",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-X-RPCMAG-4-CVP-RESAMPLED-V9.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-x-rpcmag-4-cvp-resampled-v9.0",
-            "description": "This dataset contains RESAMPLED DATA (CODMAC LEVEL 4) of the two\ncommissioning phases CVP1 and CVP2 and of the interference campaign  of the\nROSETTA orbiter magnetometer RPCMAG. Included are data from the time interval\nMarch 17, 2004 until October 14, 2004.\nThe current version of the dataset is V9.0.\nThe difference to the datasets of earlier versions is mainly a significantly\nimproved sensor temperature model, more detailed documentation about magnetic\ndisturbance sources, more data handling information for the user and\nalso an improved quality flagging system.",
-            "title": "ROSETTA-ORBITER CHECK RPCMAG 4 CVP CALIBRATED V9.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER CHECK RPCMAG 4 CVP CALIBRATED V9.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.nasa.gov/d/bj4u-ajez",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "GeneLab Outreach",
+                "hasEmail": "mailto:genelab-outreach@lists.nasa.gov"
+            },
+            "description": "The whole-genome sequences of eight fungal strains that were selected for exposure to microgravity at the International Space Station are presented here. These baseline sequences will help to understand the observed production of novel bioactive compounds.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "GeneLab Study Page",
+                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-132",
+                    "mediaType": "text/html",
+                    "title": "Whole genome sequencing and assembly of Eukaryotic microbes isolated from ISS environmental surface Kirovograd region soil Chernobyl Nuclear Power Plant and Chernobyl Exclusion Zone"
+                }
+            ],
+            "identifier": "nasa_genelab_GLDS-132_bj4u-ajez",
             "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
             "keyword": [
                 "sample collection",
                 "radiation",
@@ -538134,47 +538148,35 @@
                 "nucleic acid sequencing",
                 "library construction"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "GeneLab Outreach",
-                "hasEmail": "mailto:genelab-outreach@lists.nasa.gov"
-            },
+            "landingPage": "https://data.nasa.gov/d/bj4u-ajez",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "nasa_genelab_GLDS-132_bj4u-ajez",
-            "description": "The whole-genome sequences of eight fungal strains that were selected for exposure to microgravity at the International Space Station are presented here. These baseline sequences will help to understand the observed production of novel bioactive compounds.",
-            "title": "Whole genome sequencing and assembly of Eukaryotic microbes isolated from ISS environmental surface Kirovograd region soil Chernobyl Nuclear Power Plant and Chernobyl Exclusion Zone",
-            "programCode": [
-                "026:005"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-132",
-                    "description": "GeneLab Study Page",
-                    "@type": "dcat:Distribution",
-                    "title": "Whole genome sequencing and assembly of Eukaryotic microbes isolated from ISS environmental surface Kirovograd region soil Chernobyl Nuclear Power Plant and Chernobyl Exclusion Zone"
-                }
-            ],
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "Whole genome sequencing and assembly of Eukaryotic microbes isolated from ISS environmental surface Kirovograd region soil Chernobyl Nuclear Power Plant and Chernobyl Exclusion Zone"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-NAVCAM-2-EXT1-MTP025-V1.1",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This dataset contains ROSETTA NAVCAM RAW DATA of the Extension 1 Phase from 12th Jan 2016 to 9th Feb 2016 when at the vicinity of target 67P/CG. This data set V1.1 supersedes the V1.0. It includes updates of the Browse images, clarification of calibration target, document updates and resolve other minor outstanding errata.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-navcam-2-ext1-mtp025-v1.1",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2021-05-21",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "international rosetta mission",
                 "alpha lyr",
@@ -538183,305 +538185,305 @@
                 "scat light",
                 "67p/churyumov-gerasimenko 1 (1969 r1)"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-NAVCAM-2-EXT1-MTP025-V1.1",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-navcam-2-ext1-mtp025-v1.1",
-            "description": "This dataset contains ROSETTA NAVCAM RAW DATA of the Extension 1 Phase from 12th Jan 2016 to 9th Feb 2016 when at the vicinity of target 67P/CG. This data set V1.1 supersedes the V1.0. It includes updates of the Browse images, clarification of calibration target, document updates and resolve other minor outstanding errata.",
-            "title": "ROSETTA-ORBITER 67P NAVCAM 2 ROSETTA EXTENSION 1 MTP025 V1.1",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P NAVCAM 2 ROSETTA EXTENSION 1 MTP025 V1.1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/V9OBAWL8XE4H",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "AMMR Air and Brightness Temperature Data, Wakasa Bay, Version 1. Version 1. Archived by National Aeronautics and Space Administration, U.S. Government, NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/V9OBAWL8XE4H.",
-            "issued": "2003-01-14",
-            "temporal": "2003-01-14T00:00:00Z/2003-02-03T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2003-02-03",
-            "keyword": [
-                "earth science",
-                "atmospheric temperature",
-                "atmosphere",
-                "spectral/engineering",
-                "microwave"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "James Wang",
                 "hasEmail": "mailto:jwang@pop900.gsfc.nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA NSIDC DAAC"
-            },
-            "identifier": "C1386204122-NSIDCV0",
             "description": "The Wakasa Bay Field Campaign was conducted to validate rainfall algorithms developed for the Advanced Microwave Scanning Radiometer - Earth Observing System (AMSR-E).",
-            "title": "AMMR Air and Brightness Temperature Data, Wakasa Bay, Version 1",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FV9OBAWL8XE4H",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FV9OBAWL8XE4H",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/AVDM/data/rainfall/wakasa_bay/AMMR/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/AVDM/data/rainfall/wakasa_bay/AMMR/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/AVDM/data/rainfall/wakasa_bay/AMMR/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/AVDM/data/rainfall/wakasa_bay/AMMR/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/V9OBAWL8XE4H",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/V9OBAWL8XE4H",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/V9OBAWL8XE4H",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/V9OBAWL8XE4H",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C1386204122-NSIDCV0",
+            "issued": "2003-01-14",
+            "keyword": [
+                "earth science",
+                "atmospheric temperature",
+                "atmosphere",
+                "spectral/engineering",
+                "microwave"
+            ],
+            "landingPage": "https://doi.org/10.5067/V9OBAWL8XE4H",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2003-02-03",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA NSIDC DAAC"
+            },
             "spatial": "134.0313 30.6763 150.3528 41.476",
+            "temporal": "2003-01-14T00:00:00Z/2003-02-03T23:59:59.999Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "AMMR Air and Brightness Temperature Data, Wakasa Bay, Version 1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/SD6WORV4GX8P",
             "citation": "Nadia Smith. 2019-01-15. SNDRSNIML2CPS. Version 2.1. Sounder SIPS: Suomi NPP CrIMSS Level 2 CLIMCAPS Full Spectral Resolution: retrieved atmospheric state V2.1. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/SD6WORV4GX8P. https://disc.gsfc.nasa.gov/datacollection/SNDRSNIML2CPS_2.1.html. Digital Science Data.",
-            "issued": "2015-11-02",
-            "temporal": "2015-11-02T00:00:00Z/2024-08-12T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2021-05-21",
-            "references": [
-                "https://doi.org/DOI  10.3390/rs11101227",
-                "https://doi.org/10.1109/TGRS.2012.2220369",
-                "https://doi.org/10.1016/S0022-4073(97)00169-6",
-                "https://doi.org/10.1109/TGRS.2002.808236",
-                "https://doi.org/10.1029/2005/JD007020",
-                "https://doi.org/10.5194/amt-13-4437-2020"
-            ],
-            "keyword": [
-                "atmosphere",
-                "atmospheric temperature",
-                "land surface",
-                "clouds",
-                "atmospheric water vapor",
-                "atmospheric radiation",
-                "altitude",
-                "precipitation",
-                "air quality",
-                "atmospheric chemistry",
-                "ocean temperature",
-                "earth science",
-                "oceans",
-                "surface thermal properties"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Lena Iredell",
                 "hasEmail": "mailto:lena.iredell@nasa.gov"
             },
+            "creator": "Nadia Smith",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C2790892760-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Not provided"
-            },
             "description": "The CLIMCAPS (Community Long-term Infrared Microwave Coupled Product System) algorithm is used to analyze data from the Cross-track Infrared Sounder/Advanced Technology Microwave Sounder (CrIS/ATMS) instruments, also known as CrIMSS (Cross-track Infrared and Microwave Sounding Suite). The CrIS/ATMS instruments used for this product are on board the Suomi National Polar-orbiting Partnership (SNPP) platform and use the Full Spectral Resolution (FSR) data. The CrIS instrument is a Fourier transform spectrometer with a total of 2211 FSR infrared sounding channels covering the longwave (645-1095 cm-1), midwave (1210-1750 cm-1), and shortwave (2000-2550 cm-1) spectral regions. The ATMS instrument  is a cross-track scanner with 22 channels in spectral bands from 23 GHz through 183 GHz.\n\nThe CLIMCAPS algorithm uses an Optimal Estimation methodology and uses an a-priori first guess to start the process. A CLIMCAPS sounding is comprised of a set of parameters that characterizes the full atmospheric state and includes a variety of geophysical parameters derived from the CrIMSS data. These include surface temperature and infrared emissivity; full atmosphere profiles of temperature, water vapor and ozone; infrared effective cloud top characteristics; carbon monoxide, methane, carbon dioxide, sulfur dioxide, nitrous oxide, and nitric acid.\n\nA level 2 granule has been set as 6 minutes of data, 30 footprints cross track by 45 lines along track. There are 240 granules per day, with an orbit repeat cycle of approximately 16 day.\n \nThe CLIMCAPS algorithm uses data from the second Modern-Era Retrospective analysis for Research and Applications (MERRA-2) as a first-guess for the atmospheric state.  Because MERRA-2 products typically have a latency from 3 to 7 weeks, so too do the CLIMCAPS products.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "SNDRSNIML2CPS",
-            "creator": "Nadia Smith",
-            "graphic-preview-description": "Sample plot of CrIS/ATMS CLIMCAPS Level 2.1 retrieval.",
-            "title": "Sounder SIPS: Suomi NPP CrIMSS Level 2 CLIMCAPS Full Spectral Resolution: retrieved atmospheric state V2.1 (SNDRSNIML2CPS) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/SNDRSNIML2CPS_2.1.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSD6WORV4GX8P",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSD6WORV4GX8P",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/SNDRSNIML2CPS_2.1.png",
-                    "description": "Sample plot of CrIS/ATMS CLIMCAPS Level 2.1 retrieval.",
                     "@type": "dcat:Distribution",
+                    "description": "Sample plot of CrIS/ATMS CLIMCAPS Level 2.1 retrieval.",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/SNDRSNIML2CPS_2.1.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/SNDRSNIML2CPS_2.1.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/SNDRSNIML2CPS_2.1.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sounder.gesdisc.eosdis.nasa.gov/data/SNPP_Sounder_Level2/SNDRSNIML2CPS.2.1/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://sounder.gesdisc.eosdis.nasa.gov/data/SNPP_Sounder_Level2/SNDRSNIML2CPS.2.1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sounder.gesdisc.eosdis.nasa.gov/opendap/SNPP_Sounder_Level2/SNDRSNIML2CPS.2.1/",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://sounder.gesdisc.eosdis.nasa.gov/opendap/SNPP_Sounder_Level2/SNDRSNIML2CPS.2.1/",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=SNDRSNIML2CPS+2.1",
-                    "description": "Search the Earthdata website",
                     "@type": "dcat:Distribution",
+                    "description": "Search the Earthdata website",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=SNDRSNIML2CPS+2.1",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Sounder/CLIMCAPS.V2.1.README.pdf",
-                    "description": "CLIMCAPS L2 Product User Guide:File Format and Definition",
                     "@type": "dcat:Distribution",
+                    "description": "CLIMCAPS L2 Product User Guide:File Format and Definition",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Sounder/CLIMCAPS.V2.1.README.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's read me document"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Sounder/L2_CLIMCAPS_V2.to.V2.1_Mapping.pdf",
-                    "description": "Mapping of data variables from v2 CLIMCAPS to V2.1 CLIMCAPS CPS",
                     "@type": "dcat:Distribution",
+                    "description": "Mapping of data variables from v2 CLIMCAPS to V2.1 CLIMCAPS CPS",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Sounder/L2_CLIMCAPS_V2.to.V2.1_Mapping.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's product usage"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Sounder/CLIMCAPS.V1.ATBD.pdf",
-                    "description": "CLIMCAPS ATBD",
                     "@type": "dcat:Distribution",
+                    "description": "CLIMCAPS ATBD",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Sounder/CLIMCAPS.V1.ATBD.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's algorithm theoretical basis document"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Sounder/CLIMCAPS.V2.Test.Report.pdf",
-                    "description": "Product quality assessment guide",
                     "@type": "dcat:Distribution",
+                    "description": "Product quality assessment guide",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Sounder/CLIMCAPS.V2.Test.Report.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's product quality assessment"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://airs.jpl.nasa.gov/data/guides-docs/climcaps-science/",
-                    "description": "CLIMCAPS Science Application Guide (Digital version)",
                     "@type": "dcat:Distribution",
+                    "description": "CLIMCAPS Science Application Guide (Digital version)",
+                    "downloadURL": "https://airs.jpl.nasa.gov/data/guides-docs/climcaps-science/",
+                    "mediaType": "text/html",
                     "title": "View this dataset's product usage"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Sounder/CLIMCAPS_V2.1_L2_science_guides.pdf",
-                    "description": "CLIMCAPS Science Application Guide",
                     "@type": "dcat:Distribution",
+                    "description": "CLIMCAPS Science Application Guide",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Sounder/CLIMCAPS_V2.1_L2_science_guides.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's product usage"
                 }
             ],
+            "graphic-preview-description": "Sample plot of CrIS/ATMS CLIMCAPS Level 2.1 retrieval.",
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/SNDRSNIML2CPS_2.1.png",
+            "identifier": "C2790892760-GES_DISC",
+            "issued": "2015-11-02",
+            "keyword": [
+                "atmosphere",
+                "atmospheric temperature",
+                "land surface",
+                "clouds",
+                "atmospheric water vapor",
+                "atmospheric radiation",
+                "altitude",
+                "precipitation",
+                "air quality",
+                "atmospheric chemistry",
+                "ocean temperature",
+                "earth science",
+                "oceans",
+                "surface thermal properties"
+            ],
+            "landingPage": "https://doi.org/10.5067/SD6WORV4GX8P",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2021-05-21",
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
+            "series-name": "SNDRSNIML2CPS",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2015-11-02T00:00:00Z/2024-08-12T00:00:00Z",
             "theme": [
                 "SUOMI-NPP",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Sounder SIPS: Suomi NPP CrIMSS Level 2 CLIMCAPS Full Spectral Resolution: retrieved atmospheric state V2.1 (SNDRSNIML2CPS) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC4-1250-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 4 phase 2015-10-22 to 2015-12-31. It is a Global Gravity measurement at the comet 67P and covers the time 2015-12-11T08:06:35.000 to 2015-12-11T15:45:12.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc4-1250-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC4-1250-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc4-1250-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 4 phase 2015-10-22 to 2015-12-31. It is a Global Gravity measurement at the comet 67P and covers the time 2015-12-11T08:06:35.000 to 2015-12-11T15:45:12.000.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 4 1250 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 4 1250 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-3-ESC3-67PCHURYUMOV-M18-V3.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This CODMAC level 3 data set contains radiometric calibrated image data in W/m^2/sr/nm, acquired by the OSIRIS Narrow Angle Camera on the Rosetta spacecraft during the COMET ESCORT 3 mission phase, covering the period from 2015-06-30T23:25:00.000 to 2015-07-28T23:24:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V3.0 supersedes previous deliveries of the same dataset with the following changes since the last version: Lien corrected dataset after the July and October 2018 PSA/PDS external peer reviews. Updated documentation and ancillary files, added document on bandpass filter. Updated SCIENCE_USER_GUIDE_V03.PDF to include one section about FAQ and one section about image data quality. Added shutter backtravel and readout issues to image quality map. Updated DATA_QUALITY_ID keyword in image header. Improved handling of images with missing packets. Included FITs files. Browse products changed to the same size as the original image.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-3-esc3-67pchuryumov-m18-v3.0",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2021-05-21",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "international rosetta mission",
                 "zeta cas",
@@ -538489,169 +538491,180 @@
                 "vega",
                 "pluto"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-3-ESC3-67PCHURYUMOV-M18-V3.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-3-esc3-67pchuryumov-m18-v3.0",
-            "description": "This CODMAC level 3 data set contains radiometric calibrated image data in W/m^2/sr/nm, acquired by the OSIRIS Narrow Angle Camera on the Rosetta spacecraft during the COMET ESCORT 3 mission phase, covering the period from 2015-06-30T23:25:00.000 to 2015-07-28T23:24:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V3.0 supersedes previous deliveries of the same dataset with the following changes since the last version: Lien corrected dataset after the July and October 2018 PSA/PDS external peer reviews. Updated documentation and ancillary files, added document on bandpass filter. Updated SCIENCE_USER_GUIDE_V03.PDF to include one section about FAQ and one section about image data quality. Added shutter backtravel and readout issues to image quality map. Updated DATA_QUALITY_ID keyword in image header. Improved handling of images with missing packets. Included FITs files. Browse products changed to the same size as the original image.",
-            "title": "ROSETTA-ORBITER 67P OSINAC 3 ESC3-MTP018 RDR V3.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P OSINAC 3 ESC3-MTP018 RDR V3.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.nasa.gov/d/bjhj-g4bv",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "keyword": [
-                "genotype   spaceflight   altered gravity   light",
-                "treatmemt protocol   nucleic acid extraction   spike-in protocol   library construction   nucleic acid sequencing"
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
-            "identifier": "nasa_genelab_GLDS-346_bjhj-g4bv",
             "description": "Traveling to nearby extraterrestrial objects having a reduced gravity level (partial gravity) compared to Earth s gravity is becoming a realistic objective for space agencies. The use of plants as part of life support systems will require a better understanding of the interactions among plant growth responses including tropisms under partial gravity conditions. Here we present results from the Seedling Growth space experiments on the ISS to complement the previously released GLDS-251 dataset including seeds of Arabidopsis thaliana wildtype plants. Seeds were germinated and seedlings grew for six days under different gravity levels namely micro-g several intermediate partial-g levels and 1g and were subjected to irradiation with blue light for the last 48 hours. RNA was extracted was obtained for 20 wildtype samples for subsequent RNAseq analysis in GLDS-251 here we add 36 samples from similarly exposed PhyA and PhyB mutants.",
-            "title": "RNAseq analysis of the response of Arabidopsis thaliana phytochrome mutants (PhyA PhyB) to fractional gravity under blue-light stimulation during spaceflight",
-            "programCode": [
-                "026:005"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-346",
-                    "description": "GeneLab Study Page",
                     "@type": "dcat:Distribution",
+                    "description": "GeneLab Study Page",
+                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-346",
+                    "mediaType": "text/html",
                     "title": "RNAseq analysis of the response of Arabidopsis thaliana phytochrome mutants (PhyA PhyB) to fractional gravity under blue-light stimulation during spaceflight"
                 }
             ],
+            "identifier": "nasa_genelab_GLDS-346_bjhj-g4bv",
+            "issued": "2021-05-21",
+            "keyword": [
+                "genotype   spaceflight   altered gravity   light",
+                "treatmemt protocol   nucleic acid extraction   spike-in protocol   library construction   nucleic acid sequencing"
+            ],
+            "landingPage": "https://data.nasa.gov/d/bjhj-g4bv",
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
+            "title": "RNAseq analysis of the response of Arabidopsis thaliana phytochrome mutants (PhyA PhyB) to fractional gravity under blue-light stimulation during spaceflight"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/Nimbus-7/CZCS/L1/DATA/1",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/GSFC/SED/ESD/GCDC/OB.DAAC. https://doi.org/10.5067/Nimbus-7/CZCS/L1/DATA/1.",
-            "issued": "2015-09-10",
-            "temporal": "1978-10-30T00:00:00Z/1986-06-22T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2015-09-09",
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
-            "identifier": "C1200034503-OB_DAAC",
             "description": "The Coastal Zone Color Scanner Experiment (CZCS) was the first instrument devoted to\nthe measurement of ocean color and flown on a spacecraft. Although other instruments\nflown on other spacecraft had sensed ocean color, their spectral bands, spatial\nresolution and dynamic range were optimized for land or meteorological use and had\nlimited sensitivity in this area, whereas in CZCS, every parameter was optimized for\nuse over water to the exclusion of any other type of sensing. CZCS had six spectral\nbands, four of which were used primarily for ocean color. These were of a 20 nanometer\nbandwidth centered at 443, 520, 550, and 670 nm. Band 5 had a 100 nm bandwidth centered\nat 750 nm and a dynamic range more suited to land. Band 6 operated in the 10.5 to 12.5\nmicrometer region and sensed emitted thermal radiance for derivation of equivalent\nblack body temperature. (This thermal band failed within the first year of the mission,\nand so was not used in the global processing effort.) Bands 1-4 were preset to view\nwater only and saturated when the IFOV was over most types of land surfaces, or clouds.",
-            "title": "Nimbus-7 Coastal Zone Color Scanner (CZCS) Data Regional Data",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FNimbus-7%2FCZCS%2FL1%2FDATA%2F1",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FNimbus-7%2FCZCS%2FL1%2FDATA%2F1",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://oceandata.sci.gsfc.nasa.gov/CZCS/L1/",
-                    "description": "NASA Ocean Color Web - Data Distribution Site",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Ocean Color Web - Data Distribution Site",
+                    "downloadURL": "https://oceandata.sci.gsfc.nasa.gov/CZCS/L1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/data/czcs",
-                    "description": "NASA Ocean Color Web - Instrument Description Page",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Ocean Color Web - Instrument Description Page",
+                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/data/czcs",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/atbd/",
-                    "description": "NASA Ocean Color Web - Algorithm Descriptions",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Ocean Color Web - Algorithm Descriptions",
+                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/atbd/",
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
-                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/data/10.5067/Nimbus-7/CZCS/L1/DATA/1",
-                    "description": "OB.DAAC CZCS Nimbus-7 L1 Data Landing Page",
                     "@type": "dcat:Distribution",
+                    "description": "OB.DAAC CZCS Nimbus-7 L1 Data Landing Page",
+                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/data/10.5067/Nimbus-7/CZCS/L1/DATA/1",
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
+            "identifier": "C1200034503-OB_DAAC",
+            "issued": "2015-09-10",
+            "keyword": [
+                "ocean optics",
+                "earth science",
+                "oceans"
+            ],
+            "landingPage": "https://doi.org/10.5067/Nimbus-7/CZCS/L1/DATA/1",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2015-09-09",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GCDC/OB.DAAC"
+            },
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "1978-10-30T00:00:00Z/1986-06-22T23:59:59Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Nimbus-7 Coastal Zone Color Scanner (CZCS) Data Regional Data"
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
+                    "downloadURL": "http://pmm.nasa.gov/data-access/downloads/trmm",
+                    "mediaType": "text/html"
+                }
+            ],
+            "identifier": "NASA-0000105",
             "issued": "2018-06-25",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
             "keyword": [
                 "climate",
                 "nasa",
@@ -538666,65 +538679,30 @@
                 "water",
                 "water cycle"
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
-            "identifier": "NASA-0000105",
-            "description": "Tropical Rainfall Measuring Mission (TRMM) data products are currently available from 1998 to the present. Global Precipitation Measurement (GPM) mission data products are currently available from March 2014 to the present. TRMM and GPM are joint missions between NASA and the Japan Aerospace Exploration Agency (JAXA) designed to monitor and study global precipitation. Here we outline the types of products currently available for TRMM and GPM and the various ways to query, view and download these precipitation products.",
-            "title": "Precipitation Measurement Missions Data Access",
-            "programCode": [
-                "026:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://pmm.nasa.gov/data-access/downloads/trmm",
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
-            "landingPage": "http://nasa3d.arc.nasa.gov/detail/kepler-372",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2018-06-25",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
-            "references": [
-                "http://kepler.nasa.gov/"
-            ],
-            "keyword": [
-                "kepler",
-                "3d model",
-                "spacecraft",
-                "satellite"
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
-            "identifier": "NASA-374",
             "description": "Model of the Kepler spacecraft. Polygons: 372 Vertices: 418",
-            "title": "NASA 3D Models: Kepler",
-            "programCode": [
-                "026:045",
-                "026:046"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -538732,23 +538710,47 @@
                     "mediaType": "application/octet-stream"
                 }
             ],
-            "accrualPeriodicity": "irregular",
+            "identifier": "NASA-374",
+            "issued": "2018-06-25",
+            "keyword": [
+                "kepler",
+                "3d model",
+                "spacecraft",
+                "satellite"
+            ],
+            "landingPage": "http://nasa3d.arc.nasa.gov/detail/kepler-372",
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
+                "http://kepler.nasa.gov/"
+            ],
             "theme": [
                 "Management/Operations"
-            ]
+            ],
+            "title": "NASA 3D Models: Kepler"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-J-LORRI-2-JUPITER-V1.1",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This data set contains Raw data taken by the New Horizons Long Range Reconnaissance Imager instrument during the Jupiter encounter mission phase.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-j-lorri-2-jupiter-v1.1_bjs6-ccb5",
             "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "j7 elara",
                 "new horizons",
@@ -538762,68 +538764,44 @@
                 "callisto",
                 "calibration"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-J-LORRI-2-JUPITER-V1.1",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-j-lorri-2-jupiter-v1.1_bjs6-ccb5",
-            "description": "This data set contains Raw data taken by the New Horizons Long Range Reconnaissance Imager instrument during the Jupiter encounter mission phase.",
-            "title": "NEW HORIZONS LORRI JUPITER ENCOUNTER V1.1",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "NEW HORIZONS LORRI JUPITER ENCOUNTER V1.1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5270/esa-91oxxtk",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Copernicus Sentinel data processed by ESA, Rutherford Appleton Laboratory (RAL). 2019-07-18. S5P_L2__NP_BD3. Version 1. Sentinel-5P TROPOMI SNPP VIIRS cloud product band 3 (UVIS detector) 1-Orbit L2 7km x 3.5km. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5270/esa-91oxxtk. https://disc.gsfc.nasa.gov/datacollection/S5P_L2__NP_BD3_1.html. Digital Science Data.",
-            "issued": "2018-07-18",
-            "temporal": "2018-04-30T00:41:24Z/2022-01-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2018-07-18",
-            "keyword": [
-                "clouds",
-                "atmosphere",
-                "earth science"
-            ],
-            "data-presentation-form": "Digital Science Data",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Richard Siddans",
                 "hasEmail": "mailto:richard.siddans@stfc.ac.uk"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
-            "identifier": "C1622747253-GES_DISC",
-            "description": "Starting from August 6th in 2019, Sentinel-5P TROPOMI along-track high spatial resolution (~5.5km at nadir) has been implemented.\nFor data after August 6th of 2019, please check S5P_L2__NP_BD3 data collection.\n\nThe Copernicus Sentinel-5 Precursor (Sentinel-5P or S5P) satellite mission is one of the European Space Agency's (ESA) new mission family - Sentinels, and it is a joint initiative between the Kingdom of the Netherlands and the ESA. The sole payload on Sentinel-5P is the TROPOspheric Monitoring Instrument (TROPOMI), which is a nadir-viewing 108 degree Field-of-View push-broom grating hyperspectral spectrometer, covering the wavelength of ultraviolet-visible (UV-VIS, 270nm to 495nm), near infrared (NIR, 675nm to 775nm), and shortwave infrared (SWIR, 2305nm-2385nm). Sentinel-5P is the first of the Atmospheric Composition Sentinels and is expected to provide measurements of ozone, NO2, SO2, CH4, CO, formaldehyde, aerosols and cloud at high spatial, temporal and spectral resolutions.\n\nCopernicus Sentinel-5P is flying in a loose formation with U.S. Suomi National Polar-orbiting Partnership (SNPP) so that S5P is able to utilize the high spatial resolution capability of the Visible Infrared Imager Radiometer Suite (VIIRS) instrument. S5P_L2_NP_BDx product contains VIIRS cloud information for each S5P across-track observation in a given band (i.e. band 3, band 6 and band 7). In addition to the nominal filed-of-view (FOV), the S5P_NPPC products are also generated for three scaled FOVs both in along and across-track directions to account for the presence of cloud covering a more extended area than the nominal FOV. The main output of S5P_L2_NP_BDx are the number of VIIRS pixels classified as confidently cloudy, probably cloudy, probably clear, and confidently clear; and the VIIRS sun-normalized radiance information in band M7, M9, and M11 such as mean, standard deviation, as well as number of valid radiance contributions.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "S5P_L2__NP_BD3",
             "creator": "Copernicus Sentinel data processed by ESA, Rutherford Appleton Laboratory (RAL)",
-            "title": "Sentinel-5P TROPOMI SNPP VIIRS cloud product band 3 (UVIS detector) 1-Orbit L2 7km x 3.5km V1 (S5P_L2__NP_BD3) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/S5P_OFFL_L2__NP_BD3_1.png",
-            "programCode": [
-                "026:001"
-            ],
+            "data-presentation-form": "Digital Science Data",
+            "description": "Starting from August 6th in 2019, Sentinel-5P TROPOMI along-track high spatial resolution (~5.5km at nadir) has been implemented.\nFor data after August 6th of 2019, please check S5P_L2__NP_BD3 data collection.\n\nThe Copernicus Sentinel-5 Precursor (Sentinel-5P or S5P) satellite mission is one of the European Space Agency's (ESA) new mission family - Sentinels, and it is a joint initiative between the Kingdom of the Netherlands and the ESA. The sole payload on Sentinel-5P is the TROPOspheric Monitoring Instrument (TROPOMI), which is a nadir-viewing 108 degree Field-of-View push-broom grating hyperspectral spectrometer, covering the wavelength of ultraviolet-visible (UV-VIS, 270nm to 495nm), near infrared (NIR, 675nm to 775nm), and shortwave infrared (SWIR, 2305nm-2385nm). Sentinel-5P is the first of the Atmospheric Composition Sentinels and is expected to provide measurements of ozone, NO2, SO2, CH4, CO, formaldehyde, aerosols and cloud at high spatial, temporal and spectral resolutions.\n\nCopernicus Sentinel-5P is flying in a loose formation with U.S. Suomi National Polar-orbiting Partnership (SNPP) so that S5P is able to utilize the high spatial resolution capability of the Visible Infrared Imager Radiometer Suite (VIIRS) instrument. S5P_L2_NP_BDx product contains VIIRS cloud information for each S5P across-track observation in a given band (i.e. band 3, band 6 and band 7). In addition to the nominal filed-of-view (FOV), the S5P_NPPC products are also generated for three scaled FOVs both in along and across-track directions to account for the presence of cloud covering a more extended area than the nominal FOV. The main output of S5P_L2_NP_BDx are the number of VIIRS pixels classified as confidently cloudy, probably cloudy, probably clear, and confidently clear; and the VIIRS sun-normalized radiance information in band M7, M9, and M11 such as mean, standard deviation, as well as number of valid radiance contributions.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5270%2Fesa-91oxxtk",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5270%2Fesa-91oxxtk",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
@@ -538833,309 +538811,309 @@
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/S5P_L2__NP_BD3_1.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/S5P_L2__NP_BD3_1.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://tropomi.gesdisc.eosdis.nasa.gov/opendap/S5P_TROPOMI_Level2/S5P_L2__NP_BD3.1/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://tropomi.gesdisc.eosdis.nasa.gov/opendap/S5P_TROPOMI_Level2/S5P_L2__NP_BD3.1/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://tropomi.gesdisc.eosdis.nasa.gov/data/S5P_TROPOMI_Level2/S5P_L2__NP_BD3.1",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://tropomi.gesdisc.eosdis.nasa.gov/data/S5P_TROPOMI_Level2/S5P_L2__NP_BD3.1",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=S5P_L2__NP_BD3_1",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=S5P_L2__NP_BD3_1",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sentinel.esa.int/documents/247904/2476257/Sentinel-5P-NPP-ATBD-NPP-Clouds",
-                    "description": "Algorithm Theoretical Basis Document",
                     "@type": "dcat:Distribution",
+                    "description": "Algorithm Theoretical Basis Document",
+                    "downloadURL": "https://sentinel.esa.int/documents/247904/2476257/Sentinel-5P-NPP-ATBD-NPP-Clouds",
+                    "mediaType": "text/html",
                     "title": "View this dataset's algorithm theoretical basis document"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sentinel.esa.int/documents/247904/3541451/Sentinel-5P-Mission-Performance-Centre-NPP-Cloud-Readme",
-                    "description": "README Document",
                     "@type": "dcat:Distribution",
+                    "description": "README Document",
+                    "downloadURL": "https://sentinel.esa.int/documents/247904/3541451/Sentinel-5P-Mission-Performance-Centre-NPP-Cloud-Readme",
+                    "mediaType": "text/html",
                     "title": "View this dataset's read me document"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sentinel.esa.int/documents/247904/2474726/Sentinel-5P-Level-2-Product-User-Manual-NPP-Cloud-product",
-                    "description": "Product User Manual Document",
                     "@type": "dcat:Distribution",
+                    "description": "Product User Manual Document",
+                    "downloadURL": "https://sentinel.esa.int/documents/247904/2474726/Sentinel-5P-Level-2-Product-User-Manual-NPP-Cloud-product",
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
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/S5P_OFFL_L2__NP_BD3_1.png",
+            "identifier": "C1622747253-GES_DISC",
+            "issued": "2018-07-18",
+            "keyword": [
+                "clouds",
+                "atmosphere",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5270/esa-91oxxtk",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2018-07-18",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
+            },
+            "release-place": "Greenbelt, MD, USA",
+            "series-name": "S5P_L2__NP_BD3",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2018-04-30T00:41:24Z/2022-01-17T00:00:00Z",
             "theme": [
                 "Sentinel-5P",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Sentinel-5P TROPOMI SNPP VIIRS cloud product band 3 (UVIS detector) 1-Orbit L2 7km x 3.5km V1 (S5P_L2__NP_BD3) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC4-1256-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 4 phase 2015-10-22 to 2015-12-31. It is a Global Gravity measurement at the comet 67P and covers the time 2015-12-13T18:08:55.000 to 2015-12-14T03:40:15.500.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc4-1256-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC4-1256-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc4-1256-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 4 phase 2015-10-22 to 2015-12-31. It is a Global Gravity measurement at the comet 67P and covers the time 2015-12-13T18:08:55.000 to 2015-12-14T03:40:15.500.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 4 1256 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 4 1256 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.nasa.gov/d/bjtj-w8rd",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "keyword": [
-                "nucleic acid extraction   library construction   nucleic acid sequencing   sequence analysis data transformation   sample collection",
-                "weightlessness simulation"
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
-            "identifier": "nasa_genelab_GLDS-91_bjtj-w8rd",
             "description": "Here in this study we systematically examined the patterns of DNA methylation and hydroxy-methylation with its functional implications in gene regulation for the cultured TK6 lymphoblastoid cells upon exposure to micro-gravity conditions. The results reported here indicate that simulated microgravity alters methylation patterns in a limited way and subsequently the expression of genes involved in stress response like ATF3 FBXO17 MAP3K13 and VCL in TK6 cells. Overall design: Examination of RNA-seq with 2 replicates each for 1 cell type",
-            "title": "A study of gene expression influenced by simulated microgravity in human lymphoblastoid cells",
-            "programCode": [
-                "026:005"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-91",
-                    "description": "GeneLab Study Page",
                     "@type": "dcat:Distribution",
+                    "description": "GeneLab Study Page",
+                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-91",
+                    "mediaType": "text/html",
                     "title": "A study of gene expression influenced by simulated microgravity in human lymphoblastoid cells"
                 }
             ],
-            "accrualPeriodicity": "irregular",
+            "identifier": "nasa_genelab_GLDS-91_bjtj-w8rd",
+            "issued": "2018-06-26",
+            "keyword": [
+                "nucleic acid extraction   library construction   nucleic acid sequencing   sequence analysis data transformation   sample collection",
+                "weightlessness simulation"
+            ],
+            "landingPage": "https://data.nasa.gov/d/bjtj-w8rd",
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
+            "title": "A study of gene expression influenced by simulated microgravity in human lymphoblastoid cells"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-4-PRL-67P-M07-INF-REFL-V1.0",
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
+            "description": "This CODMAC level 4 data set contains solar stray-light corrected, in-field stray-light corrected,  radiometric calibrated and geometric distortion corrected  (resampled) image data in reflectance units (normalized  and thus without unit),  acquired by the OSIRIS Narrow Angle Camera on the Rosetta spacecraft  during the PRELANDING mission phase, covering the period  from 2014-09-02T10:00:00.000 to 2014-09-23T09:59:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V1.0 is the first version of this dataset: Lien corrected dataset after September 2019 PSA/PDS external peer review.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-4-prl-67p-m07-inf-refl-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-4-PRL-67P-M07-INF-REFL-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-4-prl-67p-m07-inf-refl-v1.0",
-            "description": "This CODMAC level 4 data set contains solar stray-light corrected, in-field stray-light corrected,  radiometric calibrated and geometric distortion corrected  (resampled) image data in reflectance units (normalized  and thus without unit),  acquired by the OSIRIS Narrow Angle Camera on the Rosetta spacecraft  during the PRELANDING mission phase, covering the period  from 2014-09-02T10:00:00.000 to 2014-09-23T09:59:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V1.0 is the first version of this dataset: Lien corrected dataset after September 2019 PSA/PDS external peer review.",
-            "title": "ROSETTA-ORBITER 67P OSINAC 4 PRL-MTP007 RDR-INF-REFL V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P OSINAC 4 PRL-MTP007 RDR-INF-REFL V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=PHX-M-MET-2-PT-EDR-V1.0",
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
+            "description": "The PHX METEOROLOGICAL DATA product contains pre-processed (Digital Numbers) temperature and pressure data. The temperature data was collected at 250, 500 and 1000mm above the Phoenix Lander deck, and the pressure data was collected at (nearly) the height of the Lander deck. Nominally the data was collected at 2 sec resolution, but is also provided at 512 sec averages (with distribution statistics).",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.phx-m-met-2-pt-edr-v1.0_bjvk-ixhr",
+            "issued": "2018-06-26",
+            "keyword": [
+                "mars",
+                "phoenix"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=PHX-M-MET-2-PT-EDR-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.phx-m-met-2-pt-edr-v1.0_bjvk-ixhr",
-            "description": "The PHX METEOROLOGICAL DATA product contains pre-processed (Digital Numbers) temperature and pressure data. The temperature data was collected at 250, 500 and 1000mm above the Phoenix Lander deck, and the pressure data was collected at (nearly) the height of the Lander deck. Nominally the data was collected at 2 sec resolution, but is also provided at 512 sec averages (with distribution statistics).",
-            "title": "PHOENIX MARS METEOROLOGICAL PRESSURE / TEMPERATURE EDR V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "PHOENIX MARS METEOROLOGICAL PRESSURE / TEMPERATURE EDR V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-4-PRL-67P-M05-INF-REFL-V1.0",
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
+            "description": "This CODMAC level 4 data set contains solar stray-light corrected, in-field stray-light corrected,  radiometric calibrated and geometric distortion corrected  (resampled) image data in reflectance units (normalized  and thus without unit),  acquired by the OSIRIS Narrow Angle Camera on the Rosetta spacecraft  during the PRELANDING mission phase, covering the period  from 2014-07-02T08:35:00.000 to 2014-08-01T09:59:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V1.0 is the first version of this dataset: Lien corrected dataset after September 2019 PSA/PDS external peer review.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-4-prl-67p-m05-inf-refl-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-4-PRL-67P-M05-INF-REFL-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-4-prl-67p-m05-inf-refl-v1.0",
-            "description": "This CODMAC level 4 data set contains solar stray-light corrected, in-field stray-light corrected,  radiometric calibrated and geometric distortion corrected  (resampled) image data in reflectance units (normalized  and thus without unit),  acquired by the OSIRIS Narrow Angle Camera on the Rosetta spacecraft  during the PRELANDING mission phase, covering the period  from 2014-07-02T08:35:00.000 to 2014-08-01T09:59:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V1.0 is the first version of this dataset: Lien corrected dataset after September 2019 PSA/PDS external peer review.",
-            "title": "ROSETTA-ORBITER 67P OSINAC 4 PRL-MTP005 RDR-INF-REFL V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P OSINAC 4 PRL-MTP005 RDR-INF-REFL V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5270/S5P-0wafvaf",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Copernicus Sentinel data processed by ESA, Koninklijk Nederlands Meteorologisch Instituut (KNMI). 2019-08-19. S5P_L2__AER_AI_HiR. Version 1. Sentinel-5P TROPOMI Aerosol Index 1-Orbit L2 5.5km x 3.5km. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5270/S5P-0wafvaf. https://disc.gsfc.nasa.gov/datacollection/S5P_L2__AER_AI_HiR_1.html. Digital Science Data.",
-            "issued": "2017-05-05",
-            "temporal": "2019-08-06T02:41:41Z/2022-01-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2017-05-05",
-            "keyword": [
-                "atmosphere",
-                "earth science",
-                "aerosols"
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
-            "identifier": "C1627516285-GES_DISC",
-            "description": "Starting from August 6th in 2019, Sentinel-5P TROPOMI along-track high spatial resolution (~5.5km at nadir) has been implemented.\nFor data before August 6th of 2019, please check S5P_L2__AER_AI_1 data collection.\n\nThe Copernicus Sentinel-5 Precursor (Sentinel-5P or S5P) satellite mission is one of the European Space Agency's (ESA) new mission family - Sentinels, and it is a joint initiative between the Kingdom of the Netherlands and the ESA. The sole payload on Sentinel-5P is the TROPOspheric Monitoring Instrument (TROPOMI), which is a nadir-viewing 108 degree Field-of-View push-broom grating hyperspectral spectrometer, covering the wavelength of ultraviolet-visible (UV-VIS, 270nm to 495nm), near infrared (NIR, 675nm to 775nm), and shortwave infrared (SWIR, 2305nm-2385nm). Sentinel-5P is the first of the Atmospheric Composition Sentinels and is expected to provide measurements of ozone, NO2, SO2, CH4, CO, formaldehyde, aerosols and cloud at high spatial, temporal and spectral resolutions.\n\nThe TROPOMI UV Aerosol Index has been calculated based on wavelength dependent changes in Rayleigh scattering in the UV spectral range where ozone absorption is weak. A residual value is calculated from measured top-of-atmosphere (TOA) reflectance and per-calculated theoretical reflectance for a Rayleigh scattering-only atmosphere given a wavelength pair. TROPOMI UVAI products use the classical wavelength pair of 340/380 nm, and the OMI chosen 354/388 nm pair for the long-term continuous AI record. Figure 1 shows TROPOMI UVAI of orbit# 4060.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "S5P_L2__AER_AI_HiR",
             "creator": "Copernicus Sentinel data processed by ESA, Koninklijk Nederlands Meteorologisch Instituut (KNMI)",
-            "title": "Sentinel-5P TROPOMI Aerosol Index 1-Orbit L2 5.5km x 3.5km V1 (S5P_L2__AER_AI_HiR) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/S5P_OFFL_L2__AER_AI_HiR_1.png",
-            "programCode": [
-                "026:001"
-            ],
+            "data-presentation-form": "Digital Science Data",
+            "description": "Starting from August 6th in 2019, Sentinel-5P TROPOMI along-track high spatial resolution (~5.5km at nadir) has been implemented.\nFor data before August 6th of 2019, please check S5P_L2__AER_AI_1 data collection.\n\nThe Copernicus Sentinel-5 Precursor (Sentinel-5P or S5P) satellite mission is one of the European Space Agency's (ESA) new mission family - Sentinels, and it is a joint initiative between the Kingdom of the Netherlands and the ESA. The sole payload on Sentinel-5P is the TROPOspheric Monitoring Instrument (TROPOMI), which is a nadir-viewing 108 degree Field-of-View push-broom grating hyperspectral spectrometer, covering the wavelength of ultraviolet-visible (UV-VIS, 270nm to 495nm), near infrared (NIR, 675nm to 775nm), and shortwave infrared (SWIR, 2305nm-2385nm). Sentinel-5P is the first of the Atmospheric Composition Sentinels and is expected to provide measurements of ozone, NO2, SO2, CH4, CO, formaldehyde, aerosols and cloud at high spatial, temporal and spectral resolutions.\n\nThe TROPOMI UV Aerosol Index has been calculated based on wavelength dependent changes in Rayleigh scattering in the UV spectral range where ozone absorption is weak. A residual value is calculated from measured top-of-atmosphere (TOA) reflectance and per-calculated theoretical reflectance for a Rayleigh scattering-only atmosphere given a wavelength pair. TROPOMI UVAI products use the classical wavelength pair of 340/380 nm, and the OMI chosen 354/388 nm pair for the long-term continuous AI record. Figure 1 shows TROPOMI UVAI of orbit# 4060.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5270%2FS5P-0wafvaf",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5270%2FS5P-0wafvaf",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
@@ -539145,475 +539123,473 @@
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/S5P_L2__AER_AI_HiR_1.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/S5P_L2__AER_AI_HiR_1.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://tropomi.gesdisc.eosdis.nasa.gov/opendap/S5P_TROPOMI_Level2/S5P_L2__AER_AI_HiR.1/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://tropomi.gesdisc.eosdis.nasa.gov/opendap/S5P_TROPOMI_Level2/S5P_L2__AER_AI_HiR.1/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://tropomi.gesdisc.eosdis.nasa.gov/opendap/S5P_TROPOMI_Level2/S5P_L2__AER_AI_HiR.1/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://tropomi.gesdisc.eosdis.nasa.gov/opendap/S5P_TROPOMI_Level2/S5P_L2__AER_AI_HiR.1/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
```

